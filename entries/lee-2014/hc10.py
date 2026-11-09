"""Loading and intrinsic measures for CRCNS hc-10 (Lee, Krook-Magnuson, Bezaire & Soltesz 2016).

The data set is one zip, ``hc-10/live/Soltesz_data.zip``, in the public S3 bucket
``crcnsarchive``. CRCNS data sets are not versioned (docs/archives.md): the version is
recorded as ``crcns:hc-10/unversioned`` and the zip is identified by its MD5 sum in the data
set's ``checksums.md5`` (``ZIP_MD5`` below), which ``open_zip`` checks while streaming.

Each ATF file holds the current-step sweeps of one cell, one voltage column (mV) per sweep and
no current column. The step levels are those of the data descriptor's table (``STEPS_PA``):
-400:50:+550 pA for the pyramidal cells (PCs) of Lee et al. (2014), -300:50:+N pA for the
PV+ basket cells. Sweeps are taken in file order, one step each.

Where each parameter comes from:

- Step onset and length: measured from the data (``step_window``), the sample with the
  largest drop of the mean of the hyperpolarizing sweeps; the step is 1 s, as the
  Supplemental Experimental Procedures 2B state ("1s-long step currents").
- Steady state, 0.8 to 1.0 s after step onset: Supplemental Experimental Procedures 2B
  ("measured at steady state (0.8s -1.0s from the start of 1s-long current steps)"), and,
  for the sag, the claim figs1h-sag's criterion.
- Pre-step baseline, the 0.2 s before the step onset: a standard choice that cannot change a
  result (the pre-step voltage is flat, see the notebook's data check).
- Spike detection, upward crossing of 0 mV: the claim figs1e-if-curves's criterion, which
  calls it a standard choice.
- Firing frequency, readings (a) spikes in the 1 s step per second and (b) (spikes - 1) over
  the first-to-last spike interval: the claim figs1e-if-curves's criterion. Under (b) a
  sweep with fewer than two spikes has no interval and is given 0 Hz, a standard choice
  (it affects only sweeps at the rheobase).
- Input resistance, readings (a) slope of steady-state voltage against current over the
  steps -100 to +100 pA, (b) mean of change over current over the four non-zero steps: the
  claim figs1f-input-resistance's criterion.
- Sag, peak (most negative voltage in the step) minus steady state: the claim figs1h-sag's
  criterion.
"""

import hashlib
import io
import zipfile

import fsspec
import numpy as np

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-10/live/Soltesz_data.zip"
DATASET = "crcns:hc-10/unversioned"
DOI = "10.6080/K00P0WXQ"
# MD5 of Soltesz_data.zip in hc-10/live/checksums.md5
ZIP_MD5 = "99bc6c87c503c724a1e692f520e25162"

FS = 10_000.0  # Hz, from the time column (0.1 ms steps); the Methods give 10 kHz

# Cell names, groups and step ranges from the data descriptor's table (v0.7, Dec 2016).
PCS = {
    "dPC": ["D1_25abf", "D1_45abf", "D2_06abf", "D2_49abf", "D3_55abf", "D4_11abf",
            "D5_15abf", "D6_19abf", "D7"],
    "sPC": ["S1_04abf", "S1_47abf", "S2_08abf", "S2_31abf", "S2_51abf", "S3_13abf", "S4",
            "S5_21abf"],
}
PVBCS = {"PV34": 500, "PV36": 800, "PV37": 500, "PV38": 300, "PV72": 400, "PV80": 450}


def steps_pa(cell):
    """Step levels in pA, in sweep order, from the data descriptor's table."""
    if cell in PVBCS:
        return np.arange(-300, PVBCS[cell] + 1, 50)
    return np.arange(-400, 551, 50)


def member_name(names, cell):
    """The zip member of a cell. PV34 is deposited twice (PVBC_PV34.atf and
    PV34_PVBC_mouse.atf, identical bytes); PVBC_PV34.atf is used."""
    if cell in PVBCS:
        return f"Soltesz_data/PVBC_{cell}.atf"
    hits = [n for n in names if n.split("/")[-1].startswith(cell + "_intrinsic")]
    assert len(hits) == 1, (cell, hits)
    return hits[0]


def open_zip(check_md5=True):
    """Open the zip in place over HTTP range requests. With check_md5, stream the whole
    zip once through MD5 (in memory, nothing written) and compare with checksums.md5."""
    if check_md5:
        h = hashlib.md5()
        with fsspec.open(URL, block_size=2**20) as f:
            for chunk in iter(lambda: f.read(2**22), b""):
                h.update(chunk)
        assert h.hexdigest() == ZIP_MD5, h.hexdigest()
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def parse_atf(raw):
    """Parse an ATF 1.0 text file: returns (header lines, column titles, data array)."""
    lines = raw.decode("latin1").splitlines()
    assert lines[0].startswith("ATF")
    n_header = int(lines[1].split()[0])
    header = lines[2:2 + n_header]
    titles = [t.strip('"') for t in lines[2 + n_header].split("\t")]
    data = np.loadtxt(io.StringIO("\n".join(lines[3 + n_header:])), delimiter="\t")
    return header, titles, data


def load_cell(z, cell):
    """Voltage of one cell: dict with time (s), v (samples x sweeps, mV), steps (pA),
    header and titles."""
    header, titles, data = parse_atf(z.read(member_name(z.namelist(), cell)))
    steps = steps_pa(cell)
    v = data[:, 1:]
    assert v.shape[1] == len(steps), (cell, v.shape, len(steps))
    return {"cell": cell, "t": data[:, 0], "v": v, "steps": steps, "header": header,
            "titles": titles}


def step_window(v, steps):
    """Onset and offset sample of the step, from the mean of the hyperpolarizing sweeps:
    onset at the largest drop, offset at the largest rise."""
    m = v[:, steps < 0].mean(axis=1)
    dm = np.diff(m)
    on = int(np.argmin(dm)) + 1
    off = int(np.argmax(dm[on:])) + on + 1
    return on, off


def spike_times(x, t, on, off):
    """Times (s) of upward crossings of 0 mV within the step."""
    seg = x[on:off]
    idx = np.where((seg[1:] >= 0) & (seg[:-1] < 0))[0] + 1 + on
    return t[idx]


def firing(cell_data, on, off):
    """Per sweep: spike count, rate reading (a) and rate reading (b) in Hz."""
    t, v = cell_data["t"], cell_data["v"]
    dur = (off - on) / FS
    counts, ra, rb = [], [], []
    for k in range(v.shape[1]):
        st = spike_times(v[:, k], t, on, off)
        counts.append(len(st))
        ra.append(len(st) / dur)
        rb.append((len(st) - 1) / (st[-1] - st[0]) if len(st) >= 2 else 0.0)
    return np.array(counts), np.array(ra), np.array(rb)


def baseline(v, on):
    """Mean voltage over the 0.2 s before the step onset, per sweep."""
    return v[on - int(0.2 * FS):on].mean(axis=0)


def steady_state(v, on):
    """Mean voltage 0.8 to 1.0 s after step onset, per sweep."""
    return v[on + int(0.8 * FS):on + int(1.0 * FS)].mean(axis=0)


def input_resistance(cell_data, on):
    """Input resistance (MOhm) under readings (a) and (b), from the -100 to +100 pA steps."""
    steps, v = cell_data["steps"], cell_data["v"]
    sel = (steps >= -100) & (steps <= 100)
    i = steps[sel].astype(float)
    ss = steady_state(v, on)[sel]
    dv = ss - baseline(v, on)[sel]
    slope = np.polyfit(i, ss, 1)[0] * 1000.0  # mV/pA -> MOhm
    nz = i != 0
    ratio = np.mean(dv[nz] / i[nz]) * 1000.0
    return slope, ratio


def sag(cell_data, on, step):
    """Sag (mV) at one step: steady state minus the most negative voltage in the step."""
    k = int(np.where(cell_data["steps"] == step)[0][0])
    x = cell_data["v"][:, k]
    peak = x[on:on + int(1.0 * FS)].min()
    return steady_state(x[:, None], on)[0] - peak

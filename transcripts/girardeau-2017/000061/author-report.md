I've finished attempt `000061-girardeau-2017-02`. Of the 32 claims, 7 were tested (5 reproduced, 2 not reproduced) and 25 are blocked. The notebook ran from a clean environment in 6.8 minutes, the record is written, and the handover is built in `executed/000061-girardeau-2017/handover/`. Nothing is committed.

The main reason for so many blocks: most of the rewritten claims are about putative pyramidal cells, and the dandiset has no putative cell types and no spike waveforms. Five Rat08 files (20130709 to 20130713) do have a `cell_type` column that the earlier attempt never read. It marks only cells identified as excitatory or inhibitory, which looks like the paper's monosynaptic identification step alone, and no file has six identified excitatory hippocampal units.

**Version.** I kept 0.250624.0426. The paper cites no DANDI version, no later version has been published, and the draft holds the same 40 assets with metadata changes only. Since the version did not change, the helper constant and the `dandi:` relation stay as they were.

### 1. Outcome per claim (earlier outcome in brackets)

**Tested:**
- `unit-counts`: not reproduced. The dandiset has 40 sessions and 4702 units against the paper's 61 and 7,390. [no claim before]
- `habituation-over-days`: reproduced. Laps come from reward times; the pooled Spearman p is 0.011 to 0.046 and the correlation is positive in all 4 rats. [no claim]
- `bla-pyr-sleep-firing-increase`: reproduced on the 152 identified excitatory BLA cells of the 5 typed Rat08 files. [no claim]
- `bla-int-sleep-firing`: not reproduced. The REM/wake test gives p = 0.020 where the claim says no change, and the NREM decrease has p = 0.26. [no claim]
- `reactivation-all-cell-pairs`: reproduced. EV exceeds REV in 13 of 15 sessions, p = 0.00031. [no claim]
- `cen-no-reactivation`: reproduced (NREM p = 0.30, REM p = 0.25). [no claim]
- `ripple-rate-unchanged`: reproduced (p = 0.26 over 23 sessions). [no claim]

**Blocked, too large (no position):** `rats-learn-puff-location` [was also blocked, too large], plus `each-rat-learns-puff-location`, `dz-speed-slower-post-run` and `puff-location-no-speed-bias` [no claims].

**Blocked, metadata insufficient (no putative cell types):** 21 claims. These include the ones that kept their ids:
- `hpc-bla-reactivation-post-sleep` [reproduced]
- `reactivation-peaks-at-ripples` [reproduced]
- `bla-ripple-up-subgroup` [reproduced]
- `reactivation-involves-ripple-up-cells` [reproduced]
- `aversive-direction-stronger` [not reproduced]

Each now uses the paper's measure on pyramidal cells, which cannot be selected here. The earlier outcomes rested on measures the paper does not use. Where the claims file defines an all-cell part, I show it as a description that decides nothing; for example, all-cell air puff against safe gives p = 0.48.

### 2. Earlier findings
- **Still present (the files are unchanged):** epochs stored in milliseconds; video timestamps in milliseconds and off the session clock; the wrong spike index in ten files; files missing units, sleep states or ripples; no position tracking; the undescribed `trials` table; the undescribed ripple labels.
- **Still present in the dandiset:** the undescribed region labels. The paper's Supplementary Fig. 3 now names the structures they match.
- **Partly fixed:** the methods are now available (full text plus the paper's code), but the dandiset still links no code.

### 3. New findings
- The putative cell types and waveforms are missing, and the `cell_type` column covers only 5 of 33 files with units.
- The dandiset holds 40 of 61 sessions and 4702 of 7,390 units, and does not say which rat is which of the paper's rats 1 to 4.

I added three questions in `questions/000061.yaml`:
- Can a claim be judged on lap reading c alone, since readings a and b cannot be run?
- Can the firing-rate claims be judged on identified cells alone (O4 reading a)?
- Could the all-cell parts of the three claims blocked only through `depends_on` be judged on their own? If yes, `reactivation-peaks-at-ripples` might become partially reproduced and `direction-all-cell-pairs` reproduced.

### 4. Where the protocol did not fit a repeat attempt
- **`entry.py check` fails on the deprecated `-01` record.** It holds every attempt of the entry to the current claims file, so `-01` has 29 errors: 26 claims without outcomes and 3 notebook tags that no longer exist. All 29 errors are in `-01`; the new record passes. Because of this I ran `entry.py run` instead of `all`. I left both `-01` and the tool unchanged; the checker probably needs to skip deprecated records.
- **The repeat-attempt section assumes the claims file is kept and the dandiset has changed.** Here it was the reverse: the dandiset is unchanged and the claims file was rewritten. So no earlier finding could be fixed, and most outcome changes come from the new claims, not the data.
- **The blocking rule for dependencies blocks claims whose all-cell tests could run.** A claim that depends on a blocked claim is blocked, even when its own all-cell test needs nothing from that claim.

One unrelated thing: untracked dotfiles (`.bashrc`, `.vscode` and others) appear in the working tree. I did not create them and left them alone.

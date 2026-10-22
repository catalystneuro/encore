# Fixing Conversions from Registry Findings

Every attempt in the registry records findings about the dandiset it used: metadata that disagrees with the files, data the description promises but the dandiset lacks, units or clocks that are wrong. For the dandisets CatalystNeuro converted, these findings are a list of things we may be able to fix. This page is the process for working through them, one dandiset at a time, with the person who converted it. The dandisets and their status are in [conversion-tracker.md](conversion-tracker.md).

The findings were written by AI agents and checked by other agents, not by anyone who knows the data. Expect most of them to hold and some to be wrong. A wrong finding is worth reporting too: open an issue on this repository saying which finding and why, so the protocol can improve.

## Steps

### 1. Open the Issue

Draft the issue for the conversion repository from the registry:

```bash
python tools/conversion_issue.py 000559 > issue.md
```

The first line is the title and the rest is the body, with one checklist item per finding and the steps below. Post it on the conversion repository and put its link in the tracker.

### 2. Triage Each Finding

For each finding, say in the issue whether it holds, and if it does, where it comes from:

- the conversion code (a bug, or a value written wrongly);
- information the source has that the conversion dropped (a column read but never written, a session that failed without anyone noticing);
- something the source data does not contain, which only the lab can supply;
- the paper itself, which needs no change to the dandiset.

Read the conversion code and the small files it reads (metadata YAMLs, session tables) before the large ones. A large parquet or HDF5 file can often be checked without downloading it: its footer or header holds the column names and statistics, and a range request reads one part. The 000559 issue ([datta-lab-to-nwb#111](https://github.com/catalystneuro/datta-lab-to-nwb/issues/111)) is a worked example.

### 3. Fix What the Conversion Can Fix

Open a pull request on the conversion repository, linked to the issue. Keep to findings that hold. Where the fix needs a fact from the paper, such as a stimulation wavelength, cite the Methods; where it needs one the paper does not give, ask the lab and leave it out until they answer.

### 4. Test on a Few Sessions

Convert a handful of sessions chosen to exercise each fix, open the files, check that each finding is gone, and run NWB Inspector on them. This does not need the whole dataset or much disk. If the source is a large table read once per session, split it by session first (one pass that writes a file per session); it turns every later read into a small one.

### 5. Re-convert and Upload to the Draft

Re-convert the dataset and upload it to the dandiset's draft. The published version does not change until a new version is published, so the draft is the place to check the fix. Validate the Dandiset metadata before the upload, and add the conversion repository to the metadata's related resources if it is not there yet. Only the NWB files need replacing when external videos have not changed.

### 6. Re-check with the Registry

Open a [run request](https://github.com/catalystneuro/reproduction-registry/issues/new?template=run-request.yml) for the draft, with the conversion's issue or pull request under "Why" ([queue.md](queue.md)). The repeat attempt runs the full protocol against the new files and says, for each earlier finding, whether it is fixed, partly fixed or still present, as the [001754 repeat](pilot-notes.md) did. It also catches anything the fix broke. Fix what it reports and repeat this step if needed.

### 7. Publish

When the re-check looks right, publish a new version of the dandiset, update the tracker and close the issue.

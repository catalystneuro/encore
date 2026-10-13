# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: design draft. No reproduction has been attempted yet.

- [`docs/design.md`](docs/design.md): the design, phasing and open decisions.
- [`tools/build_targets.py`](tools/build_targets.py): builds the queue of
  targets (dandisets that name a paper) from the public DANDI API.
- [`targets/dandisets.json`](targets/dandisets.json): the generated queue.
- [`targets/pilot.yaml`](targets/pilot.yaml): the eight targets for the pilot.
- [`schemas/`](schemas): draft schemas for claims and attempts, to be revised
  after the pilot.

```bash
python tools/build_targets.py     # standard library only, no token needed
```

Code and notebooks are under the [Apache-2.0 license](LICENSE).

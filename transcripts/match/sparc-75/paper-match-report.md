SPARC:75 has one linked paper, and I judged it `partial`. The match file `papers/match/sparc-75.yaml` passes validation.

**doi:10.1073/pnas.2023807118** ("Imaging in vivo acetylcholine release in the peripheral nervous system with a fluorescent nanosensor"): `partial`, with `data_in: SPARC:108`.
- **Deciding evidence:** the paper's Data Availability section names a different dataset as its data: "Data have been deposited in https://discover.blackfynn.com/ (DOI: 10.26275/w027-cisv)". That DOI is SPARC:108, which holds the sensor characterization, the in vitro calibrations and the in vivo stimulation imaging.
- **Why partial and not other_data:** SPARC:75 holds confocal stacks of one mouse submandibular ganglion stained ex vivo with bungarotoxin and with the nanosensor. The paper uses that staining to show where the nanosensor binds ("Ex vivo staining of freshly isolated SMG with BTX-AF647…", SI Appendix Fig. S5, Fig. 3D).
- **What can be tested here:** only that localization finding. The paper's main findings rest on SPARC:108, and the note in `targets/sparc.json` also lists datasets 108 and 75 as the two datasets of this paper.
- **One uncertainty:** I could not extract text from the supplement PDF, so I have not read the Fig. S5 caption itself. The match rests on the main text's description of the BTX staining and the dataset's own description.

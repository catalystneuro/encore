I judged the one paper the dataset links to as **primary**: doi:10.1126/science.adi0858, Chan et al., "Olfaction in the Anthropocene: NO3 negatively affects floral scent and nocturnal pollination".

**Deciding evidence:** the paper's data statement says "Data are available at (28) and (40)". Reference 40 is this dataset, Dryad 10.5061/dryad.vt4b8gtzk. Reference 28 only points to the supplementary materials.

The automated checks had held this paper back because it also cites three Zenodo records. None of them holds data: 8411927 is the lab's analysis code, and 1553349 and 5500717 are releases of GEOS-Chem, an atmospheric model. The dataset's file names match the paper's figures and tables, for example `Fig_S5C_Manduca_dose_response_wind_tunnel_behavior_data.xlsx` and the `TableS1_FigS3_CAPS_*.dat` files.

I added the verdict, reason and quoted evidence to `papers/match/dryad-vt4b8gtzk.yaml` and kept the checks the script wrote. `python tools/paper_match.py validate` passes.

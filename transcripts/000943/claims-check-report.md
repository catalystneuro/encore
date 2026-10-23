I've checked the claims file and made seven corrections; it is ready for an attempt.

**Checker result** after my changes: `31 claims, 30 quotes, 45 statistical values, 0 problems`.

I also cloned the paper's code at the commit the file cites (670c45a) and compared the criteria with the R notebooks and the relevant Python functions. The cited code details match apart from the points below.

**Changes, by claim**
- **supp1-recording-summary:** the expected value 179.1 was labelled as a mean over all sessions. The table's Average row is a mean over the nine mice (the nine per-mouse means average to 179.1), so I relabelled it.
- **fig3s4-stable-cells:** the legend's wording (more than 85% of trials) is now the main reading. The code's proportion of rolling windows is now a variant. The protocol puts the paper's text before the code when they disagree.
- **fig6b-stable-beaconed-similar:** the same change for which sessions count as stable. fig6b-stable-uncued-reduced inherits it.
- **fig6a-stable-stop-density:** stable sessions now refer to fig6b-stable-beaconed-similar, so the same main and variant readings apply.
- **fig6e-hit-try-run:** the Methods' split of misses into tries and runs (95th percentile of hit-trial speeds) is now the main reading, with the code's 95% normal interval as a variant. Before, the file treated them as equal readings, which contradicted its own opening comment and the protocol.
- **fig4e-agreement-above-shuffle:** the criterion no longer requires real agreement to be above the shuffled agreement. The statement and the legend only say the two differ; the direction will be reported.
- **fig6s2-template-method:** added the beaconed odds-ratio p = 0.4 from the supplement 2H legend, which had been left out.
- **Opening comment:** now says which stability reading is the main one.

**Still open**
- Four claims (fig2e-nongrid-classes, fig6a-stable-stop-density, fig6c-epoch-stop-density, fig6s1-speed-profiles) rest on words the paper does not measure, such as "similar" and "spatial". The file judges them with tests it names as readings: a Fisher test, the reward-zone mean against its standard error, where the profile peaks, and a mean within 1 SD. None of these comes from the paper, and the outcomes depend on them.
- **fig4e-grid-agreement-higher:** all the printed T values are negative, so which way the paper's contrasts run is unclear. The criterion takes the direction from the text, and the statement's "more variable" is not tested.
- **grid-cell-count:** the paper does not say whether units are counted once per session or once per recording day.
- **grid-field-size-spacing:** field size and grid spacing are defined only in the preprocessing code, which the paper does not pin to a commit.

**Ready:** yes. The `checks` entry is appended with `ready: true`, and nothing is committed.

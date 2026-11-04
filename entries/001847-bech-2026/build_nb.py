"""Builds reproduce_bech_2026.ipynb from the cells below (kept with the entry so the notebook can be regenerated)."""
import nbformat as nbf

cells = []


def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip())
    if tags:
        c.metadata["tags"] = tags
    cells.append(c)


def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip())
    if tags:
        c.metadata["tags"] = tags
    cells.append(c)


md("""
# Reproducing Bech, Dard et al. (eLife) from dandiset 001847

Paper: Bech, Dard, Lebert, Smith, Bisi, Renard, Crochet & Petersen, "Retrosplenial cortex enables
context-dependent goal-directed sensorimotor transformation", eLife reviewed preprint,
doi:10.7554/eLife.109717. Claims: `claims/001847/10.7554-elife.109717.yaml`, written from the eLife
Reviewed Preprint version 1 (30 December 2025), its Methods and figure-supplement legends.

Dataset: DANDI:001847, version **0.260610.1400** (doi:10.48324/dandi.001847/0.260610.1400). The paper
cites no dandiset version; this is the only published version and the most recent one, and it is
the version the READMEs of the paper's two analysis repositories name. The draft has the same 1497
assets. Every file is streamed; nothing is downloaded.

Outside input: the session lists of the paper's processing code
(github.com/LSENS-BMI-EPFL/Bech_Dard_process_NWB at commit 212a6310, `configs/session_groups`). The
claims file selects sessions by these lists, and they are the only record of which mice carry
VGAT-ChR2, jRGECO1a, GCaMP6f, tdTomato or GFP, and which sessions are Context Off or muscimol days:
the files give the genotype "WT" for every subject but one. They name sessions only, so they are
used as labels (`with_labels`) and their link is tested in `session-list-link`.

| claim | tested here |
|---|---|
| session-list-link (added) | tested |
| expert-sessions, fig1c (3 claims), fig1d, fig1e, fig1g, fig1f, fig1h, supp1c, supp1d | tested |
| fig1i-pupil-larger-wplus, fig1i-posture-before-lick, fig1j-jaw-speed-context, fig3c-jaw-onset | tested |
| fig2c, fig2d, fig2e (2 claims), fig2-no-effect-control-mice, fig2cd-rsc, fig2f | run under every reading; blocked where the readings disagree |
| supp2-muscimol-ws1-rsc | tested |
| fig3e, fig3f, fig3-gcamp-consistent-controls-flat | tested on the grid ROI traces |
| fig3h-rsc-first-context-discrimination | tested, ROI part on the grid ROI traces and pixel part on windowed reads of the ΔF/F0 stack |
| fig4c, fig4d, fig4e, fig4fg, supp4d | tested on the grid ROI traces |
| fig1k-model-accuracy, fig1k-context-strongest-feature, fig1l-shap-whisker-trial-in-block | tested (the code's XGBoost model rebuilt) |
| fig4b (3 claims) | blocked, too_large (pixel stack); a variant on the grid ROI traces is shown |
| supp3c-rsc-projects-to-wm | blocked, data_missing |
""")

code("""
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from scipy import stats
import bech
pd.set_option('display.width', 200); pd.set_option('display.max_columns', 40)
A = bech.list_assets()
T, E, M = bech.load_trials(A)
LISTS = {n: bech.code_list(n) for n in [
    'sessions_Context_sessions', 'sessions_Context_sessions_expert', 'sessions_Context_sessions_opto',
    'sessions_Context_sessions_opto_control', 'sessions_Context_sound_off', 'sessions_Context_sound_off_only',
    'sessions_Context_muscimol_wS1', 'sessions_Context_muscimol_fpS1', 'sessions_Context_muscimol_RSC',
    'sessions_Context_ringer_wS1', 'sessions_Context_ringer_fpS1', 'sessions_Context_ringer_RSC',
    'sessions_Context_sessions_expert_WF_jrGECO', 'sessions_Context_sessions_expert_WF_gcamp',
    'sessions_Context_sessions_expert_WF_tomato', 'sessions_Context_sessions_expert_WF_GFP',
    'sessions_Context_sessions_wf_opto', 'sessions_Context_sessions_wf_opto_photoactivation',
    'session_context_expert_behaviour_model']}
""", tags=["load"])

md("## Data check")
code("""
print('assets', len(A), 'subjects', A.subject.nunique(), 'by kind:', A.kind.value_counts().to_dict())
print('files whose trial table could not be read:', M.error.notna().sum() if 'error' in M else 0)
if 'error' in M: print(M.loc[M.error.notna(), ['session_id', 'error']].to_string())
print('session types (experiment_description):', M.session_type.value_counts().to_dict())
print('genotype field:', M.genotype.value_counts().to_dict())
print('session_description prefixes:', M.session_description.str.replace(r'[-+]?\\d+$', '', regex=True).value_counts().to_dict())
print('trials', len(T), 'sessions with trials', T.session_id.nunique(), 'mice', T.mouse_id.nunique())
print('trial types', T.trial_type.value_counts().to_dict(), '| context', T.context.value_counts().to_dict(),
      '| noise', T.context_background.value_counts().to_dict())
print('perf code x trial type'); print(pd.crosstab(T.perf, T.trial_type))
print('early_lick equals perf 6 for', (T.early_lick.eq(1) == T.perf.eq(6)).mean().round(4), 'of trials')
print('lick_flag 1 with no lick_time:', ((T.lick_flag == 1) & T.lick_time.isna()).sum(),
      '| lick_time - stim_time on lick trials without early lick (s):',
      (T.lick_time - T.stim_time)[(T.lick_flag == 1) & (T.early_lick == 0) & (T.trial_type != 'no_stim_trial')].describe().round(3).to_dict())
print('whisker amplitude', T.loc[T.trial_type == 'whisker_trial', 'whisker_stim_amplitude'].value_counts().head().to_dict(),
      '| whisker duration (ms)', T.loc[T.trial_type == 'whisker_trial', 'whisker_stim_duration'].value_counts().head().to_dict())
print('auditory frequency', T.loc[T.trial_type == 'auditory_trial', 'auditory_stim_frequency'].value_counts().head().to_dict(),
      '| duration (ms)', T.loc[T.trial_type == 'auditory_trial', 'auditory_stim_duration'].value_counts().head().to_dict())
# reward available only for whisker trials in W+ and for auditory trials
print('reward_available by trial type and context'); print(T.groupby(['trial_type', 'context']).reward_available.mean().round(3))
# noise to context: each mouse has one W+ noise
nz = T.groupby(['mouse_id', 'context']).context_background.agg(lambda x: x.value_counts(normalize=True).iloc[0]).unstack()
print('fraction of trials with the majority noise per mouse and context, min:', nz.min().round(3).to_dict())
# epochs against trial context
E2 = E.copy(); E2['ctx'] = (E2.epoch == 'rewarded').astype(int)
print('epochs', len(E2), '| epoch duration (s)', (E2.stop - E2.start).describe().round(1).to_dict())
chk = []
for sid, g in T.groupby('session_id'):
    e = E2[E2.session_id == sid]
    if len(e) == 0: continue
    i = np.searchsorted(e.start.values[np.argsort(e.start.values)], g.start_time.values, side='right') - 1
    es = e.sort_values('start')
    ctx = np.where(i >= 0, es.ctx.values[np.clip(i, 0, None)], -1)
    chk.append((ctx == g.context.values).mean())
print('fraction of trials whose context matches the epoch they fall in: median', np.median(chk).round(4), 'min', np.min(chk).round(4), 'sessions', len(chk))
blocks_e = E2.groupby('session_id').size(); blocks_t = T.groupby('session_id').block.max() + 1
print('blocks per session, epochs against context runs of the trial table: equal in',
      (blocks_e.reindex(blocks_t.index) == blocks_t).mean().round(3), 'of sessions')
# duplicates
h = T.groupby('session_id').start_time.apply(lambda x: hash(tuple(np.round(x.values, 3))))
print('sessions with identical trial times as another session:', h.duplicated(keep=False).sum())
""", tags=["sanity"])

md("""
### session-list-link

The code's session lists are matched to the dandiset's sessions by identifier (`PB170_20240220_155608`
in the code is `ses-PB170-20240220-155608` here). The lists also state counts in the claims file's
opening comment, which are compared.
""")
code("""
S = set(A.session_id)
expect = {'sessions_Context_sessions': (65, 1449), 'sessions_Context_sessions_expert': (41, 201),
          'sessions_Context_sessions_opto': (7, 56), 'sessions_Context_sessions_opto_control': (4, 39),
          'sessions_Context_sound_off': (7, 21), 'sessions_Context_sessions_expert_WF_jrGECO': (6, 25),
          'sessions_Context_sessions_expert_WF_gcamp': (8, 33), 'sessions_Context_sessions_expert_WF_tomato': (4, 15),
          'sessions_Context_sessions_expert_WF_GFP': (6, 24), 'sessions_Context_sessions_wf_opto': (4, 40),
          'sessions_Context_sessions_wf_opto_photoactivation': (2, 6), 'session_context_expert_behaviour_model': (21, 60)}
rows = []
for n, l in LISTS.items():
    rows.append((n, len(l), len(set(l) & S), len(set(l) & set(T.session_id)), len({x.split('_')[0] for x in l}), expect.get(n)))
link = pd.DataFrame(rows, columns=['list', 'sessions', 'in dandiset', 'with trial table', 'mice', 'claims file (mice, sessions)'])
print(link.to_string())
allids = set().union(*LISTS.values())
print('sessions named by any list', len(allids), 'found', len(allids & S), f'({len(allids & S) / len(allids):.1%})')
missing = sorted(set(LISTS['sessions_Context_sessions']) - S)
print('pool list sessions not in the dandiset:', len(missing), missing[:10])
pool = LISTS['sessions_Context_sessions']
plain = {'_'.join(x.split('_')[:3]) for x in missing}
print('of these, the plain identifier is in the dandiset:', len(plain & S), '| also listed plainly in the pool list:', len(plain & set(pool)),
      '| pool list entries', len(pool), 'distinct', len(set(pool)), 'distinct sessions after cutting the suffix', len({'_'.join(x.split('_')[:3]) for x in pool}))
print('pool list sessions in the dandiset without a readable trial table:', sorted((set(pool) & S) - set(T.session_id)))
# session types of the listed sessions agree with the list's purpose
st = M.set_index('session_id').session_type
for n in ['sessions_Context_sessions_opto', 'sessions_Context_sessions_opto_control', 'sessions_Context_sessions_wf_opto',
          'sessions_Context_sessions_expert_WF_jrGECO', 'sessions_Context_muscimol_wS1', 'sessions_Context_ringer_RSC']:
    print(n, st.reindex(LISTS[n]).value_counts().to_dict())
opto = T[T.session_id.isin(LISTS['sessions_Context_sessions_opto'])]
print('opto list: sites per session', opto[opto.opto_stim == 1].groupby('session_id').apply(lambda g: len(set(zip(g.opto_grid_ap, g.opto_grid_ml)))).describe().round(1).to_dict())
""", tags=["claim:session-list-link"])
md("""
**Result: partially reproduced.** Every session of every list a claim selects from is in the dandiset under the same identifier with a readable trial table, and those lists' counts of mice and sessions equal the claims file's. The pool list `sessions_Context_sessions`, used for the expert rule's pool variant, does not match in full: it has 1451 entries for the stated 1449, 30 of them carry a processing-date suffix and are not dandiset identifiers, and 3 of its sessions have no readable trial table (printed above). 98.0% of the sessions named by any list are found.
""")

md("""
## Behaviour (Figure 1 and its supplement)

Selection readings for "expert sessions" (claims file, opening comment): (a) the Methods' rule recomputed on
every behavioural session of the dataset (session description `whisker_context`), (b) the code's
list `sessions_Context_sessions_expert`.

### expert-sessions
> The expert sessions of the behavioural data come from 41 mice and number 201, with an average of 23 context blocks per session.
""")
code("""
behS = M[M.session_description.str.startswith('whisker_context')].session_id
beh = T[T.session_id.isin(behS)]
con = bech.block_contrast(beh, 'epochs'); ex = bech.is_expert(con, seed=1)
expA = sorted(s for s, (lo, e) in ex.items() if e)
expB = LISTS['sessions_Context_sessions_expert']
con20 = bech.block_contrast(beh, '20'); ex20 = bech.is_expert(con20, seed=2)
exp20 = sorted(s for s, (lo, e) in ex20.items() if e)
nblocks = (T.groupby('session_id').block.max() + 1)
nb_ep = E.groupby('session_id').size()
for name, Sx in [('(a) rule, epoch blocks', expA), ('rule, 20-trial blocks (variant)', exp20), ('(b) code list', expB)]:
    print(f'{name}: sessions {len(Sx)}, mice {len({s.split("_")[0] for s in Sx})}, '
          f'blocks per session (epochs) {nb_ep.reindex(Sx).mean():.2f}, (context runs) {nblocks.reindex(Sx).mean():.2f}')
print('behavioural sessions tested', len(con), '| with < 2 contrasts', sum(len(c) < 2 for c in con.values()))
print('overlap of (a) with the code list', len(set(expA) & set(expB)), 'of', len(expB))
print('overlap of the 20-trial variant with the code list', len(set(exp20) & set(expB)))
inpool = set(LISTS['sessions_Context_sessions'])
eA_pool = [s for s in expA if s in inpool]
print('(a) restricted to the code pool list: sessions', len(eA_pool), 'mice', len({s.split('_')[0] for s in eA_pool}))
lo = pd.Series({s: v[0] for s, v in ex.items()})
print('lower bound of the code-list sessions under the rule: min', lo.reindex(expB).min().round(3), ', below 0.375:', (lo.reindex(expB) <= 0.375).sum())
# which sessions the rule is run on: session types, and the 60 sessions described 'context_...'
print('session types of the sessions tested:', M[M.session_id.isin(con)].session_type.value_counts().to_dict())
ctxS = M[M.session_description.str.startswith('context_')]
print('sessions described context_...:', len(ctxS), 'mice', sorted(ctxS.mouse_id.unique()), 'types', ctxS.session_type.value_counts().to_dict())
print('   in the code lists:', {n: len(set(ctxS.session_id) & set(l)) for n, l in LISTS.items() if set(ctxS.session_id) & set(l)})
conC = bech.block_contrast(T[T.session_id.isin(ctxS.session_id)], 'epochs'); exC = bech.is_expert(conC, seed=3)
withC = expA + sorted(s for s, (l_, e) in exC.items() if e)
onlyB = [s for s in expA if M.set_index('session_id').session_type.get(s) == 'behaviour_only_session']
for name, Sx in [('variant, rule also on the context_ sessions', withC), ('variant, rule on behaviour_only sessions only', onlyB)]:
    print(f'{name}: sessions {len(Sx)}, mice {len({s.split("_")[0] for s in Sx})}, blocks per session (epochs) {nb_ep.reindex(Sx).mean():.2f}')
""", tags=["claim:expert-sessions"])
md("""
**Result: not reproduced under the rule.** The Methods' rule applied to every behavioural session gives
the session and mouse counts printed above, outside the tolerance of 201 ± 20.1 sessions and 41 ± 4.1
mice; neither variant (the rule with the `context_` sessions added, 322 sessions in 52 mice, or on
behaviour-only sessions, 112 sessions in 42 mice) gives all three counts within tolerance. The code's list
matches the paper's counts and its blocks per session are within 23 ± 2.3.
""")

code("""
def lick_by_mouse(Sx):
    D = T[T.session_id.isin(Sx) & (T.early_lick == 0)]
    return bech.mouse_avg(D, 'lick_flag', ['trial_type', 'context']).pivot_table('lick_flag', 'mouse_id', ['trial_type', 'context']) * 100
LB = {'a': lick_by_mouse(expA), 'b': lick_by_mouse(expB)}
for k, m in LB.items():
    print(f'reading ({k}), {len(m)} mice: mean'); print(m.mean().round(1).to_string()); print('SD'); print(m.std().round(1).to_string())
""")

md("""
### fig1c-auditory-hit-both-contexts
> In expert sessions mice lick to the auditory tone in both contexts, with hit rates of 96 ± 4% in W+ and 94 ± 5% in W- (mean ± SD over 41 mice).
""")
code("""
for k, m in LB.items():
    wp, wm = m[('auditory_trial', 1)].mean(), m[('auditory_trial', 0)].mean()
    print(f'({k}) auditory W+ {wp:.1f} (96 ± 4: {abs(wp - 96) <= 4}), W- {wm:.1f} (94 ± 5: {abs(wm - 94) <= 5}); n mice {len(m)}')
    print('   by mouse, min W+ / W-:', m[('auditory_trial', 1)].min().round(1), m[('auditory_trial', 0)].min().round(1))
""", tags=["claim:fig1c-auditory-hit-both-contexts"])
md("""
**Result: reproduced under reading (b).** With the code's list the auditory hit rates are within the
paper's SDs in both contexts (printed above); under reading (a) the W- value is below the tolerance.
The criterion accepts either reading of the selection, and reading (b) is the one whose mice and sessions
are the paper's (41 mice and 201 sessions, expert-sessions).
""")

md("""
### fig1c-whisker-context-modulation
> Licking to the whisker stimulus depends strongly on context, 84 ± 6% in W+ against 32 ± 7% in W- (mean ± SD over mice).
""")
code("""
for k, m in LB.items():
    wp, wm = m[('whisker_trial', 1)].mean(), m[('whisker_trial', 0)].mean()
    r = stats.ttest_rel(m[('whisker_trial', 1)], m[('whisker_trial', 0)])
    print(f'({k}) whisker W+ {wp:.1f} (84 ± 6: {abs(wp - 84) <= 6}), W- {wm:.1f} (32 ± 7: {abs(wm - 32) <= 7}); paired t {r.statistic:.1f}, p {r.pvalue:.1e}, n {len(m)}')
""", tags=["claim:fig1c-whisker-context-modulation"])
md("**Result: reproduced.** Both means are within tolerance under both readings (printed above).")

md("""
### fig1d-independent-of-noise-identity
> The context modulation of whisker licking holds whichever background noise (pink or brown) is associated with each context.
""")
code("""
wplus_noise = T[T.context == 1].groupby('mouse_id').context_background.agg(lambda x: x.value_counts().index[0])
for k, m in LB.items():
    for noise in ['pink', 'brown']:
        mm = m[m.index.map(wplus_noise) == noise]
        r = stats.ttest_rel(mm[('whisker_trial', 1)], mm[('whisker_trial', 0)])
        print(f'({k}) W+ noise {noise}: {len(mm)} mice, whisker W+ {mm[("whisker_trial", 1)].mean():.1f}, '
              f'W- {mm[("whisker_trial", 0)].mean():.1f}, paired t {r.statistic:.1f}, p {r.pvalue:.1e}')
""", tags=["claim:fig1d-independent-of-noise-identity"])
md("**Result: reproduced.** In both groups of mice, under both readings, W+ is higher with p < 0.05 (printed above).")

md("""
### fig1c-catch-higher-wplus
> Catch-trial (spontaneous) lick rates are low but slightly higher in W+ blocks, 13 ± 7% against 4 ± 2% in W-.
""")
code("""
for k, m in LB.items():
    wp, wm = m[('no_stim_trial', 1)].mean(), m[('no_stim_trial', 0)].mean()
    r = stats.ttest_rel(m[('no_stim_trial', 0)], m[('no_stim_trial', 1)])
    print(f'({k}) catch W+ {wp:.1f} (13 ± 7: {abs(wp - 13) <= 7}), W- {wm:.1f} (4 ± 2: {abs(wm - 4) <= 2}); '
          f't (W- vs W+) {r.statistic:.2f}, p {r.pvalue:.1e}; paper t = -9, p = 1.6e-10')
""", tags=["claim:fig1c-catch-higher-wplus"])
md("**Result: reproduced.** Both means within tolerance, W+ higher, p < 0.05, under both readings.")

md("""
### fig1g-first-trial-switch
> Mice change their whisker response at the first whisker trial after a context change, from 26 ± 8% to 73 ± 13% from W- to W+, and from 87 ± 7% to 57 ± 13% from W+ to W-.
""")
code("""
TR = {}
for k, Sx in [('a', expA), ('b', expB)]:
    tr = bech.transition_table(T[T.session_id.isin(Sx)])
    TR[k] = tr.groupby(['mouse_id', 'session_id', 'direction', 'position']).lick.mean().groupby(['mouse_id', 'direction', 'position']).mean().unstack([1, 2]) * 100
exp_vals = {('W-toW+', -1): 26, ('W-toW+', 1): 73, ('W+toW-', -1): 87, ('W+toW-', 1): 57}
tol = {('W-toW+', -1): 8, ('W-toW+', 1): 13, ('W+toW-', -1): 7, ('W+toW-', 1): 13}
for k, pm in TR.items():
    print(f'reading ({k}), {len(pm)} mice')
    for key, v in exp_vals.items():
        print(f'   {key}: {pm[key].mean():.1f} (expected {v} ± {tol[key]}: {abs(pm[key].mean() - v) <= tol[key]}), SD {pm[key].std():.1f}')
    for d in ['W-toW+', 'W+toW-']:
        r = stats.ttest_rel(pm[(d, 1)], pm[(d, -1)])
        print(f'   {d}: t {r.statistic:.1f}, p {r.pvalue:.1e}, Bonferroni x2 {min(1, 2 * r.pvalue):.1e}')
""", tags=["claim:fig1g-first-trial-switch"])
md("**Result: reproduced.** The four values are within the paper's SDs and both tests give p < 0.05 in the stated direction, under both readings (printed above).")

md("""
### fig1f-gradual-further-adaptation
> After the first whisker trial of a new block, whisker responses adapt slightly further over the following whisker trials, the second whisker trial already closer to the new context than the first.
""")
code("""
for k, pm in TR.items():
    print(f'reading ({k}): mean lick probability (%) by position'); print(pm.mean().unstack(0).round(1).T.to_string())
    for d, sgn in [('W-toW+', 1), ('W+toW-', -1)]:
        m1, m2, m4 = pm[(d, 1)].mean(), pm[(d, 2)].mean(), pm[(d, 4)].mean()
        r = stats.ttest_rel(pm[(d, 2)], pm[(d, 1)])
        print(f'   {d}: +2 closer than +1: {sgn * (m2 - m1) > 0}; +4 at least as close as +2: {sgn * (m4 - m2) >= 0} '
              f'(+1 {m1:.1f}, +2 {m2:.1f}, +4 {m4:.1f}); +2 vs +1 t {r.statistic:.1f}, p {r.pvalue:.1e}')
""", tags=["claim:fig1f-gradual-further-adaptation"])
md("**Result: reproduced.** In both directions and under both selections, trial +2 is closer to the new context than +1 and +4 at least as close as +2, with paired t of +2 against +1 above 9 in absolute value.")

md("""
### fig1h-temporal-integration
> The lick probability to the first whisker trial of a block rises with the time elapsed since a transition to W+ and falls with it after a transition to W-, while the last whisker trial before a transition shows no sign of anticipating the switch.

Transition time is the start of the new context epoch. Bins of 10 s, bin -1 = [-10, 0) s, bin +1 = [0, 10) s.
""")
code("""
def fig1h_table(Sx, drop_early):
    rows = []
    D = T[T.session_id.isin(Sx) & (T.trial_type == 'whisker_trial')]
    if drop_early: D = D[D.early_lick == 0]
    for sid, g in D.groupby('session_id'):
        g = g.sort_values('start_time'); full = T[T.session_id == sid].sort_values('start_time')
        for b in range(1, full.block.max() + 1):
            tt = full[full.block == b].start_time.min()  # first trial of the new block
            ep = E[(E.session_id == sid)]
            # transition time: start of the epoch the first trial of the block falls in
            st = ep.start.values; st = st[st <= tt + 1e-6]
            t0 = st.max() if len(st) else tt
            pre, post = g[g.block == b - 1], g[g.block == b]
            ctx = full[full.block == b].context.iloc[0]
            if len(pre): rows.append((sid, 'To W+' if ctx == 1 else 'To W-', pre.stim_time.iloc[-1] - t0, pre.lick_flag.iloc[-1]))
            if len(post): rows.append((sid, 'To W+' if ctx == 1 else 'To W-', post.stim_time.iloc[0] - t0, post.lick_flag.iloc[0]))
    R = pd.DataFrame(rows, columns=['session_id', 'transition', 't', 'lick'])
    R['bin'] = np.where(R.t < 0, np.floor(R.t / 10).astype(int), np.floor(R.t / 10).astype(int) + 1)
    return R
def expo(t, A_, tau, C): return A_ * np.exp(-t / tau) + C
from scipy.optimize import curve_fit
for k, Sx in [('a', expA), ('b', expB)]:
    for drop in [False, True]:
        R = fig1h_table(Sx, drop)
        tab = R[(R.bin >= -5) & (R.bin <= 5)].groupby(['transition', 'bin']).lick.agg(['mean', 'size']).unstack(0)
        print(f'reading ({k}), early licks {"dropped" if drop else "kept (code)"}'); print(tab.round(3).to_string())
        for tr, sgn in [('To W+', 1), ('To W-', -1)]:
            y = tab[('mean', tr)].reindex([-1, 1, 2, 3, 4, 5]).values; x = np.array([0, 1, 2, 3, 4, 5])
            try:
                p, _ = curve_fit(expo, x, y, p0=[y[0] - y[-1], 3, y[-1]], bounds=([-np.inf, 0.1, -np.inf], [np.inf, 50, np.inf]), maxfev=10000)
                f1, f5 = expo(1, *p), expo(5, *p)
                print(f'   {tr}: fit A {p[0]:.3f}, tau {p[1]:.2f} bins, C {p[2]:.3f}; fitted +1 {f1:.3f}, +5 {f5:.3f}; in the stated direction: {sgn * (f5 - f1) > 0}')
            except Exception as e:
                print('   fit failed', tr, e)
            pre = R[(R.transition == tr) & (R.bin >= -5) & (R.bin <= -1)]
            bm = pre.groupby('bin').lick.mean()
            rr = stats.pearsonr(bm.index * 10 - 5, bm.values)
            b1 = pre[pre.bin == -1].lick; b25 = pre[pre.bin <= -2].lick
            ft = stats.fisher_exact([[b1.sum(), len(b1) - b1.sum()], [b25.sum(), len(b25) - b25.sum()]])
            print(f'   {tr} anticipation: (a) Pearson r {rr.statistic:.2f}, p {rr.pvalue:.3f}; (b) bin -1 {b1.mean():.3f} vs bins -5..-2 {b25.mean():.3f}, Fisher p {ft.pvalue:.3f}')
""", tags=["claim:fig1h-temporal-integration"])
md("**Result: reproduced.** The fitted values rise from bin +1 to +5 after transitions to W+ and fall after transitions to W-, under every selection and early-lick reading, and neither anticipation reading finds an effect (all p above 0.05).")

md("""
### supp1c-wplus-blocks-longer
> Whisker-rewarded context blocks last longer than whisker-non-rewarded blocks (196 ± 13 against 185 ± 4 s).
""")
code("""
E['dur'] = E.stop - E.start
for k, Sx in [('a', expA), ('b', expB)]:
    D = E[E.session_id.isin(Sx)]
    m = D.groupby(['mouse_id', 'session_id', 'epoch']).dur.mean().groupby(['mouse_id', 'epoch']).mean().unstack()
    r = stats.ttest_rel(m.rewarded, m['non-rewarded'])
    print(f'({k}) {len(m)} mice: W+ {m.rewarded.mean():.1f} ± {m.rewarded.std():.1f} s (196 ± 13: {abs(m.rewarded.mean() - 196) <= 13}), '
          f'W- {m["non-rewarded"].mean():.1f} ± {m["non-rewarded"].std():.1f} s (185 ± 4: {abs(m["non-rewarded"].mean() - 185) <= 4}); t {r.statistic:.2f}, p {r.pvalue:.1e}')
    print('    epoch durations range (s)', D.dur.min().round(1), D.dur.max().round(1))
""", tags=["claim:supp1c-wplus-blocks-longer"])
md("**Result: reproduced under the code's list.** W+ 195.5 s and W- 185.4 s, both within tolerance, W+ longer with p 3.4e-6; under the rule the W- mean is outside its tolerance. As for fig1c-auditory-hit-both-contexts, the code's list is the reading whose mice and sessions are the paper's.")

md("""
### supp1d-faster-response-wplus
> Spout contact after the stimulus is slightly faster in W+ than in W-, for auditory (370 ± 9 against 400 ± 9 ms) and whisker trials (392 ± 9 against 418 ± 9 ms).
""")
code("""
for k, Sx in [('a', expA), ('b', expB)]:
    D = T[T.session_id.isin(Sx) & (T.early_lick == 0) & (T.lick_flag == 1) & T.trial_type.isin(['auditory_trial', 'whisker_trial'])].copy()
    D['rt'] = (D.lick_time - D.stim_time) * 1000
    m = bech.mouse_avg(D, 'rt', ['trial_type', 'context']).pivot_table('rt', 'mouse_id', ['trial_type', 'context'])
    print(f'reading ({k})')
    for tt, (ep, em) in [('auditory_trial', (370, 400)), ('whisker_trial', (392, 418))]:
        mm = m[tt].dropna()
        r = stats.ttest_rel(mm[1], mm[0])
        print(f'   {tt}: W+ {mm[1].mean():.0f} (SD {mm[1].std():.0f}, SEM {mm[1].sem():.0f}; {ep} ± 9: {abs(mm[1].mean() - ep) <= 9}), '
              f'W- {mm[0].mean():.0f} (SD {mm[0].std():.0f}, SEM {mm[0].sem():.0f}; {em} ± 9: {abs(mm[0].mean() - em) <= 9}); '
              f't {r.statistic:.2f}, p x2 {min(1, 2 * r.pvalue):.1e}, mice {len(mm)}')
# variant: lick time measured from the opening of the response window (response_window_start_time)
D = T[T.session_id.isin(expB) & (T.early_lick == 0) & (T.lick_flag == 1) & T.trial_type.isin(['auditory_trial', 'whisker_trial'])].copy()
print('response window start minus stimulus time (ms):', ((D.response_window_start_time - D.stim_time) * 1000).round().value_counts().head(3).to_dict())
D['rt'] = (D.lick_time - D.response_window_start_time) * 1000
m = bech.mouse_avg(D, 'rt', ['trial_type', 'context']).pivot_table('rt', 'mouse_id', ['trial_type', 'context'])
print('variant, lick time minus response window start, reading (b):',
      {f'{tt} {"W+" if c else "W-"}': round(m[(tt, c)].mean()) for tt in ['auditory_trial', 'whisker_trial'] for c in (1, 0)})
""", tags=["claim:supp1d-faster-response-wplus"])
md("**Result: partially reproduced.** W+ is faster for both trial types with corrected p below 0.05 and t-values equal to the paper's, but every mean is about 100 ms above the paper's value, outside the 9 ms tolerance. Measured from the opening of the response window, 100 ms after the stimulus in almost every trial, the means come close to the paper's (variant, printed above), which suggests the paper timed spout contact from that point; the criterion times it from the stimulus.")

md("""
### fig1e-context-off-no-discrimination
> When the two context noises are replaced by constant white noise, keeping the block reward structure, mice no longer discriminate between the context blocks in their whisker responses.
""")
code("""
off = LISTS['sessions_Context_sound_off_only']; on = sorted(set(LISTS['sessions_Context_sound_off']) - set(off))
print('Off sessions', len(off), 'On sessions', len(on))
print('noise on Off days:', T[T.session_id.isin(off)].context_background.value_counts().to_dict())
tr = bech.transition_table(T[T.session_id.isin(off)])
pm = tr.groupby(['mouse_id', 'session_id', 'direction', 'position']).lick.mean().groupby(['mouse_id', 'direction', 'position']).mean().unstack([1, 2]) * 100
for d in ['W-toW+', 'W+toW-']:
    r = stats.ttest_rel(pm[(d, 1)], pm[(d, -1)])
    print(f'Off, {d}: -1 {pm[(d, -1)].mean():.1f}, +1 {pm[(d, 1)].mean():.1f}, t {r.statistic:.2f}, p {r.pvalue:.3f}, mice {pm[(d, 1)].notna().sum()}')
for name, Sx in [('Off', off), ('On', on)]:
    m = lick_by_mouse(Sx)
    r = stats.ttest_rel(m[('whisker_trial', 1)], m[('whisker_trial', 0)])
    print(f'{name}: whisker W+ {m[("whisker_trial", 1)].mean():.1f}, W- {m[("whisker_trial", 0)].mean():.1f}, '
          f'difference {(m[("whisker_trial", 1)] - m[("whisker_trial", 0)]).mean():.1f}, t {r.statistic:.2f}, p {r.pvalue:.3g} (variant)')
""", tags=["claim:fig1e-context-off-no-discrimination"])
md("**Result: reproduced.** On the Off days neither transition direction changes whisker licking (p 0.275 and 0.545); the W+ against W- variant gives p 0.077.")


md("""
## Optogenetic inactivation (Figure 2)

The opto-map rule of the claims file: per mouse, context, trial type and site, all the mouse's
sessions pooled, ΔP(Lick) = P(lick | laser at the site) - P(lick | control, laser off the brain).
Nulls: (i) the Methods (Figures 2C-E), block labels of whole blocks permuted within each session and ΔP
recomputed; (ii) the Figure 2 legend and the code, lick outcomes permuted across the trials of that trial
type and context within each session. 10,000 shuffles each (a count that is a standard choice). d' is
|Cohen's d| between the null pooled over mice and the per-mouse ΔP. Thresholds (a) 0.5, (b) 0.8, (c) 2.
A site has an effect of a sign when the mean ΔP over mice has that sign and d' passes the threshold.
Early-lick trials are kept, as the code builds this table from the full trial table
(figure2_analysis.py:20-40).
""")
code("""
import warnings; warnings.filterwarnings('ignore')
OPTO_MICE = sorted({s.split('_')[0] for s in LISTS['sessions_Context_sessions_opto']})
CTRL_MICE = sorted({s.split('_')[0] for s in LISTS['sessions_Context_sessions_opto_control']})
O = T[T.session_id.isin(LISTS['sessions_Context_sessions_opto'])]
OC = T[T.session_id.isin(LISTS['sessions_Context_sessions_opto_control'])]
print('opto mice', OPTO_MICE, '| control mice', CTRL_MICE)
print('control trials (opto_stim 0) laser coordinates:', O[O.opto_stim == 0][['opto_grid_ap', 'opto_grid_ml']].value_counts().to_dict())
st = O[O.opto_stim == 1]
print('stimulated sites', st.groupby(['opto_grid_ap', 'opto_grid_ml']).ngroups, '| AP values', sorted(st.opto_grid_ap.unique()), '| ML values', sorted(st.opto_grid_ml.unique()))
print('trials per mouse, site, context and trial type: median', st.groupby(['mouse_id', 'opto_grid_ap', 'opto_grid_ml', 'context', 'trial_type']).size().median())
MAPS = {}
for null, seed in [('blocks', 11), ('trials', 12)]:
    obs, summ = bech.opto_map(O, OPTO_MICE, null=null, n_shuffle=10000, seed=seed)
    summ['name'] = summ.site.map({v: k for k, v in bech.SITES.items()})
    MAPS[null] = summ
OBS = obs
obsC, summC = bech.opto_map(OC, CTRL_MICE, null='trials', n_shuffle=10000, seed=13)
summC['name'] = summC.site.map({v: k for k, v in bech.SITES.items()})
print('sites per (context, trial type):', MAPS['trials'].groupby(['context', 'trial_type']).size().to_dict())
print('mice per site:', MAPS['trials'].n_mice.value_counts().to_dict())
for null, S in MAPS.items():
    print(f'null ({"i" if null == "blocks" else "ii"}) {null}: dP and d prime at the named sites')
    print(S[S.name.notna()].pivot_table(['dP_mean', 'dprime'], 'name', ['trial_type', 'context']).round(2).to_string())
    print('   null mean over sites, range', S.null_mean.min().round(3), S.null_mean.max().round(3), '| null SD range', S.null_sd.min().round(3), S.null_sd.max().round(3))
print('dP range over all sites', OBS.dP.min().round(2), OBS.dP.max().round(2))
THR = {'a': 0.5, 'b': 0.8, 'c': 2.0}
def effect(S, name, ctx, ttype, thr):
    r = S[(S.name == name) & (S.context == ctx) & (S.trial_type == ttype)]
    if len(r) == 0: return 0
    r = r.iloc[0]
    return int(np.sign(r.dP_mean)) if r.dprime >= thr else 0
def readings():
    for nl in ['blocks', 'trials']:
        for tk, tv in THR.items():
            yield f'null {"i" if nl == "blocks" else "ii"}, d>={tv}', MAPS[nl], tv
FIG4_OMIT = [(1.5, 5.5), (2.5, 4.5), (2.5, 5.5)]  # sites the Figure 4 code leaves out besides AP 3.5 (plot utils/figure4C_G.py)
print('stimulated sites after dropping AP 3.5:', MAPS['trials'].site.nunique(), '| of these, sites the Figure 4 code also leaves out:',
      sorted(set(MAPS['trials'].site) & set(FIG4_OMIT)))
# null (i) on synthetic data: 4 mice, 3 sessions of 20 blocks, the laser lowers licking by 0.2 at one site in both contexts
rs = np.random.default_rng(5); syn = []
for mo in range(4):
    for se in range(3):
        for b in range(20):
            for k in range(20):
                laser = rs.random() < 0.5
                p = 0.6 - (0.2 if laser else 0)
                syn.append((f'M{mo}', f'M{mo}_s{se}', b, b % 2, int(laser), 1.5 if laser else 0, 1.5 if laser else 0, 'whisker_trial', int(rs.random() < p), se * 1e4 + b * 100 + k))
syn = pd.DataFrame(syn, columns=['mouse_id', 'session_id', 'block', 'context', 'opto_stim', 'opto_grid_ap', 'opto_grid_ml', 'trial_type', 'lick_flag', 'start_time'])
for nl in ['blocks', 'trials']:
    _, sy = bech.opto_map(syn, [f'M{m}' for m in range(4)], null=nl, n_shuffle=1000, seed=4)
    print(f'synthetic, true dP -0.2 in both contexts, null ({"i" if nl == "blocks" else "ii"}):', sy[['context', 'dP_mean', 'null_mean', 'dprime']].round(3).to_dict('records'))
""")

md("""
### fig2c-catch-little-effect
> Optogenetic inactivation of cortical sites has little effect on licking in catch trials in either context.
""")
code("""
res = {}
for lab, S, thr in readings():
    c = S[S.trial_type == 'no_stim_trial']
    n = {ctx: int((c[c.context == ctx].dprime >= thr).sum()) for ctx in (0, 1)}
    res[lab] = max(n.values()) <= 3
    c39 = c[~c.site.isin(FIG4_OMIT)]
    n39 = {ctx: int((c39[c39.context == ctx].dprime >= thr).sum()) for ctx in (0, 1)}
    print(f'{lab}: sites with an effect W- {n[0]}, W+ {n[1]} (of {c[c.context == 0].shape[0]}); at most 3: {res[lab]} | '
          f'on the {c39[c39.context == 0].shape[0]} sites of the Figure 4 code: W- {n39[0]}, W+ {n39[1]}')
print('largest mean |dP| over sites in catch trials:', MAPS['trials'][MAPS['trials'].trial_type == 'no_stim_trial'].dP_mean.abs().max().round(3))
print('all readings agree:', len(set(res.values())) == 1, set(res.values()))
""", tags=["claim:fig2c-catch-little-effect"])
md("**Result: blocked (methods_underspecified).** Five readings find at most 3 affected sites, but the trial-shuffle null at d' 0.5 finds 7 (W-) and 11 (W+), so the readings disagree.")

md("""
### fig2d-auditory-a1-frontal
> In auditory trials, inactivating auditory cortex and frontal premotor regions reduces lick probability, similarly in both contexts.
""")
code("""
res = {}
for lab, S, thr in readings():
    ok = {}
    for ctx in (0, 1):
        a1 = effect(S, 'A1', ctx, 'auditory_trial', thr) == -1
        fr = any(effect(S, n, ctx, 'auditory_trial', thr) == -1 for n in ['wM1', 'wM2', 'ALM'])
        ok[ctx] = a1 and fr
    res[lab] = 'reproduced' if all(ok.values()) else ('partially' if any(ok.values()) else 'not')
    print(f'{lab}: W- {ok[0]}, W+ {ok[1]} -> {res[lab]}')
S = MAPS['trials']
print(S[S.name.isin(['A1', 'wM1', 'wM2', 'ALM']) & (S.trial_type == 'auditory_trial')].pivot_table('dP_mean', 'name', 'context').round(3))
print('all readings agree:', len(set(res.values())) == 1, set(res.values()))
""", tags=["claim:fig2d-auditory-a1-frontal"])
md("**Result: blocked (methods_underspecified).** The trial-shuffle null at d' 0.5 and 0.8 reproduces the claim; the same null at 2 and the block-label null at every threshold do not.")

md("""
### fig2e-whisker-sensory-premotor-reduction
> In whisker trials, inactivating wS1, wS2 and anterior premotor regions (wM1/2, ALM) reduces lick probability in both contexts.
""")
code("""
res = {}
for lab, S, thr in readings():
    ok = {}
    for ctx in (0, 1):
        ok[ctx] = (effect(S, 'wS1', ctx, 'whisker_trial', thr) == -1 and effect(S, 'wS2', ctx, 'whisker_trial', thr) == -1
                   and any(effect(S, n, ctx, 'whisker_trial', thr) == -1 for n in ['wM1', 'wM2', 'ALM']))
    res[lab] = 'reproduced' if all(ok.values()) else ('partially' if ok[1] else 'not')
    print(f'{lab}: W- {ok[0]}, W+ {ok[1]} -> {res[lab]}')
print('all readings agree:', len(set(res.values())) == 1, set(res.values()))
""", tags=["claim:fig2e-whisker-sensory-premotor-reduction"])
md("**Result: blocked (methods_underspecified).** Reproduced under the trial-shuffle null at d' 0.5 and 0.8, not under it at 2 nor under the block-label null.")

md("""
### fig2e-rsc-tjs1-increase-wminus
> Inactivating tongue-jaw somatosensory cortex (tjS1) or retrosplenial cortex (RSC) increases lick probability in whisker trials specifically in the W- context.
""")
code("""
for rsc in ['RSC', 'RSC_2']:
    res = {}
    for lab, S, thr in readings():
        ok = {n: effect(S, n, 0, 'whisker_trial', thr) == 1 and effect(S, n, 1, 'whisker_trial', thr) != 1 for n in ['tjS1', rsc]}
        res[lab] = 'reproduced' if all(ok.values()) else ('partially' if any(ok.values()) else 'not')
        print(f'{rsc}, {lab}: {ok} -> {res[lab]}')
    print(rsc, 'all readings agree:', len(set(res.values())) == 1, set(res.values()))
for nl, S in MAPS.items():
    print(nl, S[S.name.isin(['tjS1', 'RSC', 'RSC_2']) & (S.trial_type == 'whisker_trial')].pivot_table(['dP_mean', 'dprime'], 'name', 'context').round(3).to_string())
print('per mouse dP, whisker W-:'); print(OBS[(OBS.trial_type == 'whisker_trial') & (OBS.context == 0) & OBS.site.isin([bech.SITES['RSC'], bech.SITES['tjS1']])].pivot_table('dP', 'mouse_id', 'site').round(2))
""", tags=["claim:fig2e-rsc-tjs1-increase-wminus"])
md("**Result: blocked (methods_underspecified).** The readings give reproduced (trial shuffle, d' 0.8), partially reproduced (0.5) and not reproduced (2, and every block-label reading).")

md("""
### fig2cd-rsc-no-effect-catch-auditory
> Inhibiting RSC does not change performance in catch or auditory trials, so the effect of RSC inactivation needs the context-sensitive whisker stimulus.
""")
code("""
for rsc in ['RSC', 'RSC_2']:
    res = {}
    for lab, S, thr in readings():
        eff = {(tt, c): effect(S, rsc, c, tt, thr) for tt in ['no_stim_trial', 'auditory_trial'] for c in (0, 1)}
        res[lab] = all(v == 0 for v in eff.values())
        print(f'{rsc}, {lab}: no effect in any group: {res[lab]}  {eff}')
    print(rsc, 'all readings agree:', len(set(res.values())) == 1, set(res.values()))
for nl, S in MAPS.items():
    print(nl); print(S[S.name.isin(['RSC', 'RSC_2']) & S.trial_type.isin(['no_stim_trial', 'auditory_trial'])].pivot_table(['dP_mean', 'dprime'], 'name', ['trial_type', 'context']).round(3).to_string())
""", tags=["claim:fig2cd-rsc-no-effect-catch-auditory"])
md("**Result: blocked (methods_underspecified).** The trial-shuffle null finds a catch-trial effect at RSC at d' 0.5 and 0.8 and none at 2; the block-label null finds none.")

md("""
### fig2-no-effect-control-mice
> In control mice without ChR2, light at the grid sites causes no significant change in lick probability at any site.
""")
code("""
print('control mice', CTRL_MICE, 'sites', summC.site.nunique(), 'mice per site', summC.n_mice.value_counts().to_dict())
for tk, tv in THR.items():
    n = int((summC.dprime >= tv).sum())
    print(f'd >= {tv}: site, trial type and context groups passing: {n} of {len(summC)}')
print('largest d prime', summC.dprime.max().round(2), 'at', summC.loc[summC.dprime.idxmax(), ['site', 'trial_type', 'context']].tolist(),
      '| largest |dP|', summC.dP_mean.abs().max().round(3))
print(summC.sort_values('dprime', ascending=False).head(8)[['context', 'trial_type', 'site', 'dP_mean', 'dprime']].round(3).to_string())
""", tags=["claim:fig2-no-effect-control-mice"])
md("**Result: blocked (methods_underspecified).** In the control mice 61 and 20 groups pass d' 0.5 and 0.8 and none passes 2 (largest 1.80), so the thresholds disagree.")

md("""
### fig2f-latency-frontal-not-rsc
> Lick latency increases during inactivation of frontal areas but does not change during inactivation of RSC or tjS1.
""")
code("""
D = O[(O.early_lick == 0) & (O.lick_flag == 1) & (((O.trial_type == 'auditory_trial')) | ((O.trial_type == 'whisker_trial') & (O.context == 1)))].copy()
D['rt'] = (D.lick_time - D.stim_time) * 1000
D['site'] = list(zip(D.opto_grid_ap.round(2), D.opto_grid_ml.round(2)))
D.loc[D.opto_stim == 0, 'site'] = 'control'
rows = []
for tt, G in D.groupby('trial_type'):
    pm = G.groupby(['mouse_id', 'site']).rt.mean().unstack()
    for name in ['wM1', 'wM2', 'ALM', 'RSC', 'RSC_2', 'tjS1', 'wS1', 'A1']:
        s = bech.SITES[name]
        x = pm[s].dropna(); c = pm.loc[x.index, 'control']
        rows.append((tt, name, (x - c).mean(), abs(bech.dprime(x.values, c.values)), len(x)))
LAT = pd.DataFrame(rows, columns=['trial_type', 'name', 'dRT_ms', 'dprime', 'n_mice'])
print(LAT.round(2).to_string())
for tk, tv in THR.items():
    fr = any(((LAT.name == n) & (LAT.dRT_ms > 0) & (LAT.dprime >= tv)).any() for n in ['wM1', 'wM2', 'ALM'])
    nochange = not ((LAT.name.isin(['RSC', 'tjS1'])) & (LAT.dprime >= tv)).any()
    print(f'd >= {tv}: frontal increase {fr}; RSC and tjS1 unchanged {nochange} ->', 'reproduced' if fr and nochange else ('partially' if fr or nochange else 'not'))
""", tags=["claim:fig2f-latency-frontal-not-rsc"])
md("**Result: blocked (methods_underspecified).** Reproduced at d' 0.5 and 0.8; at 2 no frontal site passes, which gives partially reproduced.")

md("""
### supp2-muscimol-ws1-rsc
> Muscimol in wS1 significantly reduces whisker-trial lick probability in W- and W+, while muscimol in RSC gives a non-significant positive trend in whisker-trial licking in W-; pharmacological inactivation is consistent with the optogenetic results.

As process main_analysis/figure2_supp_stats.py: early licks dropped, session number by date within
mouse and condition (third sessions dropped), statistic (muscimol day 2 - day 1) - (Ringer day 2 - day 1),
two-level bootstrap (mice, then trials), 100,000 iterations, seed 42, p = twice the tail beyond 0 on
the side opposite the observed sign. Whisker trials.
""")
code("""
def pharma(cond):
    D = T[T.session_id.isin(LISTS[f'sessions_Context_{cond}']) & (T.early_lick == 0)].copy()
    D['date'] = pd.to_datetime(D.session_id.str.split('_').str[1])
    D['sn'] = D.groupby('mouse_id').date.rank(method='dense')
    return D[D.sn != 3]
rng_seed = 42
for area in ['wS1', 'fpS1', 'RSC']:
    Mu, Ri = pharma(f'muscimol_{area}'), pharma(f'ringer_{area}')
    print(f'{area}: muscimol mice {Mu.mouse_id.nunique()} sessions {Mu.session_id.nunique()}, Ringer mice {Ri.mouse_id.nunique()} sessions {Ri.session_id.nunique()}')
    for ctx in (0, 1):
        g = {}
        for k, D in [('m', Mu), ('r', Ri)]:
            for sn in (1, 2):
                x = D[(D.trial_type == 'whisker_trial') & (D.context == ctx) & (D.sn == sn)]
                g[(k, sn)] = [v.lick_flag.values.astype(float) for _, v in x.groupby('mouse_id')]
        o, bs, _ = bech.hier_boot(g, n_iter=100000, seed=rng_seed)
        p = 2 * ((bs >= 0).mean() if o < 0 else (bs <= 0).mean()); p = min(p, 1.0)
        dm = np.concatenate(g[('m', 2)]).mean() - np.concatenate(g[('m', 1)]).mean()
        dr = np.concatenate(g[('r', 2)]).mean() - np.concatenate(g[('r', 1)]).mean()
        print(f'   {"W+" if ctx else "W-"} whisker: muscimol change {dm:+.3f}, Ringer change {dr:+.3f}, statistic {o:+.3f}, '
              f'95% CI [{np.percentile(bs, 2.5):+.3f}, {np.percentile(bs, 97.5):+.3f}], p {p:.5f} (resolution 2e-5)')
# the injection day is the second date of each mouse in the list (the code's ranking); the files type some sessions pharma_session
STYPE = M.set_index('session_id').session_type
for area in ['wS1', 'fpS1', 'RSC']:
    for cond in ['muscimol', 'ringer']:
        d = pd.DataFrame({'session_id': LISTS[f'sessions_Context_{cond}_{area}']}); d['mouse'] = d.session_id.str.split('_').str[0]
        d['rank'] = d.groupby('mouse').session_id.transform(lambda s: pd.to_datetime(s.str.split('_').str[1]).rank(method='dense')).astype(int)
        d['type'] = d.session_id.map(STYPE)
        print(f'{area} {cond}: sessions by date rank and session_type', d.groupby(['rank', 'type']).size().to_dict())
""", tags=["claim:supp2-muscimol-ws1-rsc"])
md("**Result: reproduced.** wS1 muscimol lowers whisker licking in both contexts (p 0.00032 in W-, below 2e-5 in W+), and RSC muscimol gives a positive W- change with p 0.060, inside 0.05 to 0.1.")


md("""
## Widefield imaging (Figure 3, Figure 4C, supplement 4D)

Grid ROI ΔF/F0 traces (`brain_grid_fluorescence/dff0_grid_traces`, 42 circles at the grid sites,
named by (AP, ML)), aligned on the stimulus time of each trial. The claims file's conventions:
correct trials only, averages over trials per session, then sessions per mouse, then mice; d' across
mice, signed, ddof 0. Baseline readings: (a) 50 ms and (b) 250 ms before the stimulus (Methods), and the
code's 100 ms as a variant. Mouse lines come from the code's lists (session-list-link).
""")
code("""
WF_LISTS = ['sessions_Context_sessions_expert_WF_jrGECO', 'sessions_Context_sessions_expert_WF_gcamp',
            'sessions_Context_sessions_expert_WF_tomato', 'sessions_Context_sessions_expert_WF_GFP',
            'sessions_Context_sessions_wf_opto', 'sessions_Context_sessions_wf_opto_photoactivation']
wf_ids = sorted(set().union(*[LISTS[n] for n in WF_LISTS]))
G = bech.load_grid(A[A.session_id.isin(wf_ids)], pre=0.3, post=0.3, n=8)
print('sessions loaded', len(G), 'failed', [k for k, v in G.items() if v[0] is None])
rates = pd.Series({k: round(1 / np.median(np.diff(v[1]))) for k, v in G.items()})
print('frame rate (Hz) per session:', rates.value_counts().to_dict())
for n in WF_LISTS:
    print(n, 'rates', rates.reindex(LISTS[n]).value_counts().to_dict())
lags = np.concatenate([v[3][np.isfinite(v[2][:, 0, 0])] for v in G.values()])
print('trials inside the imaging: ', len(lags), 'of', sum(len(v[3]) for v in G.values()), '| lag of the first frame after the stimulus (ms): median', round(np.nanmedian(lags) * 1000, 1), 'max', round(np.nanmax(lags) * 1000, 1))
# trials whose first frame after the stimulus comes more than one frame late (a gap in the imaging)
LATE = {k: (v[3] > np.median(np.diff(v[1])) + 1e-6) & np.isfinite(v[2][:, 0, 0]) for k, v in G.items()}
lt = pd.Series({k: int(v.sum()) for k, v in LATE.items()})
print('trials with a lag above one frame:', lt.sum(), 'of', len(lags), 'in', (lt > 0).sum(), 'of', len(lt), 'sessions; per list:',
      {n.replace('sessions_Context_sessions_', ''): int(lt.reindex(LISTS[n]).sum()) for n in WF_LISTS})
allv = np.concatenate([np.nanpercentile(v[2], [1, 99]) for v in G.values()])
print('dF/F0 1st to 99th percentile over sessions:', np.round(allv.min(), 4), np.round(allv.max(), 4))
names0 = G[wf_ids[0]][0]; print('grid ROI names', len(names0), names0[:3], '...')
print('all sessions have the same ROI order:', all(v[0] == names0 for v in G.values()))
ROI = ['wS1', 'wS2', 'wM1', 'wM2', 'ALM', 'tjS1', 'tjM1', 'A1', 'RSC']
SIDX = bech.site_index(names0)
COL = {n: SIDX[bech.SITES[n]] for n in ROI + ['RSC_2']}
TT = T.set_index(['session_id', T.groupby('session_id').cumcount()])

def trial_table(sid):
    return T[T.session_id == sid].sort_values('start_time').reset_index(drop=True)

def mouse_traces(sids, select, baseline_ms, subtract=True, drop_late=False):
    # per mouse mean trace (time x site): trials -> session -> mouse. select(trials) -> boolean mask
    per = {}
    for sid in sids:
        names, t, W, lag = G[sid]
        tr = trial_table(sid)
        assert len(tr) == W.shape[0], sid
        m = select(tr).values
        if drop_late: m = m & ~LATE[sid]
        if m.sum() == 0: continue
        X = W[m]
        if subtract:
            b = (t < 0) & (t >= -baseline_ms / 1000 - 1e-9)
            X = X - np.nanmean(X[:, b, :], axis=1, keepdims=True)
        per.setdefault(sid.split('_')[0], []).append((t, np.nanmean(X, 0)))
    out = {}
    for mouse, lst in per.items():
        t = lst[0][0]
        out[mouse] = (t, np.mean([x for _, x in lst], 0), len(lst))
    return out

def stack(mt):
    mice = sorted(mt); t = mt[mice[0]][0]
    return t, np.stack([mt[m][1] for m in mice]), mice

wplus_hit = lambda tr: (tr.trial_type == 'whisker_trial') & (tr.context == 1) & (tr.lick_flag == 1)
wminus_miss = lambda tr: (tr.trial_type == 'whisker_trial') & (tr.context == 0) & (tr.lick_flag == 0)
aud_hit = lambda c: (lambda tr: (tr.trial_type == 'auditory_trial') & (tr.context == c) & (tr.lick_flag == 1))
BASES = [50, 250, 100]
JR = LISTS['sessions_Context_sessions_expert_WF_jrGECO']
""")

md("""
### fig3e-auditory-similar-across-contexts
> Auditory-evoked cortical activity is similar in W+ and W-, beginning in A1, then RSC, then medial secondary motor regions (wM1/2), then orofacial motor cortices (tjS1, ALM).
""")
code("""
res = {}
for base in BASES:
    t, Xp, mice = stack(mouse_traces(JR, aud_hit(1), base)); _, Xm, _ = stack(mouse_traces(JR, aud_hit(0), base))
    d = bech.dprime(Xp, Xm)
    w = (t >= 0.02 - 1e-9) & (t <= 0.12 + 1e-9)
    maxd = {n: np.nanmax(np.abs(d[w, COL[n]])) for n in ROI}
    similar = all(v <= 2 for v in maxd.values())
    print(f'baseline {base} ms, {len(mice)} mice; max |d prime| W+ vs W- from 20 to 120 ms:', {k: round(v, 2) for k, v in maxd.items()}, '-> similar', similar)
    for ctx, X in [('W+', Xp), ('W-', Xm)]:
        mtr = X.mean(0); w0 = (t >= -1e-9) & (t <= 0.12 + 1e-9)
        for rd in ['peak', 'half']:
            tim = {}
            for n in ROI:
                y = mtr[w0, COL[n]]; tt = t[w0]
                tim[n] = tt[np.argmax(y)] if rd == 'peak' else tt[np.argmax(y >= y.max() / 2)]
            twm = min(tim['wM1'], tim['wM2'])
            order = tim['A1'] < tim['RSC'] < twm < min(tim['tjS1'], tim['ALM'])
            a1first = tim['A1'] <= min(tim[n] for n in ROI)
            oc = 'reproduced' if similar and order else ('partially' if similar and a1first else 'not')
            res[(base, ctx, rd)] = oc
            print(f'   {ctx} {rd}: times (ms)', {k: int(round(v * 1000)) for k, v in tim.items()}, f'order holds {order}, A1 first {a1first} -> {oc}')
print('outcomes per reading:', res)
print('baselines (a) and (b) agree:', len({v for k, v in res.items() if k[0] in (50, 250)}) == 1)
""", tags=["claim:fig3e-auditory-similar-across-contexts"])
md("**Result: partially reproduced.** No ROI reaches |d'| 2 between contexts and A1 is first under every reading, but the order RSC, wM1/2, tjS1 and ALM is not found.")

md("""
### fig3f-whisker-divergence-after-50ms
> In whisker trials, wS1 and wS2 activate similarly in both contexts early after the stimulus, and from about 50 ms activity diverges, with more activity in RSC and wM1/2 in W+ than in W-.
""")
code("""
D3 = {}
for base in BASES:
    t, Xp, mice = stack(mouse_traces(JR, wplus_hit, base)); _, Xm, _ = stack(mouse_traces(JR, wminus_miss, base))
    d = bech.dprime(Xp, Xm); D3[base] = (t, d, Xp, Xm)
    e = (t >= 0.02 - 1e-9) & (t <= 0.05 + 1e-9); l = (t >= 0.05 - 1e-9) & (t <= 0.12 + 1e-9)
    early = {n: np.nanmax(np.abs(d[e, COL[n]])) for n in ['wS1', 'wS2']}
    late = {n: np.nanmax(d[l, COL[n]]) for n in ['RSC', 'wM1', 'wM2']}
    ok_early = all(v <= 2 for v in early.values()); rsc = late['RSC'] > 2; wm = max(late['wM1'], late['wM2']) > 2
    oc = 'reproduced' if ok_early and rsc and wm else ('partially' if ok_early and (rsc or wm) else 'not')
    print(f'baseline {base} ms, {len(mice)} mice: early max |d| {dict((k, round(v, 2)) for k, v in early.items())}; '
          f'late max d {dict((k, round(v, 2)) for k, v in late.items())} -> {oc}')
    print('   d prime by time (ms) for RSC, wM1, wM2, wS1, wS2:')
    sel = (t >= -1e-9) & (t <= 0.15)
    print(pd.DataFrame({n: d[sel, COL[n]] for n in ['RSC', 'wM1', 'wM2', 'wS1', 'wS2']}, index=np.round(t[sel] * 1000).astype(int)).round(2).T.to_string())
""", tags=["claim:fig3f-whisker-divergence-after-50ms"])
md("**Result: reproduced.** wS1 and wS2 stay below |d'| 2 from 20 to 50 ms, and RSC, wM1 and wM2 pass d' 2 between 50 and 120 ms under every baseline.")

md("""
### fig3h-rsc-first-context-discrimination
> RSC is the first cortical area to discriminate the contexts in whisker trials, both in the pixel-wise maps and in the ROI averages, the time of the first d' above 2 between W+ and W-.

ROI part on the grid ROI traces. Pixel part on the ΔF/F0 image stack (`processing/ophys/dff0`): only the
frames of the selected trials are read (250 ms before to 120 ms after the stimulus, 38 frames per trial),
baseline-subtracted per trial, averaged per session, then per mouse; d' per pixel across the 6 mice; for
each ROI the earliest crossing among the pixels of its 1 mm circle (the file's grid masks,
`grid_areas/brain_grid_area_segmentation`), with the code's Gaussian smoothing of sigma 1 pixel on the
mouse-average images and without it as a variant. The Methods for Figure 3H define d' as that "shown in
Figure 3F bottom row", whose Methods (Figures 3E&F) subtract the 50 ms baseline.
""")
code("""
def first_cross(t, dfun, start):
    first = {}
    for n in ['wS1', 'wS2', 'wM1', 'RSC', 'ALM', 'tjS1']:
        w = [k for k in range(len(t)) if t[k] >= start - 1e-9 and dfun(k, n) > 2]
        first[n] = int(round(t[w[0]] * 1000)) if w else None
    valid = {k: v for k, v in first.items() if v is not None}
    best = min(valid.values()) if valid else None
    rsc = first['RSC'] is not None and first['RSC'] == best
    tie = sum(v == best for v in valid.values()) > 1 if valid else None
    return first, rsc, tie
H = {}
print('ROI part')
for base in BASES:
    t, d, _, _ = D3[base]
    for start in [0.02, 0.03]:
        first, rsc, tie = first_cross(t, lambda k, n: d[k, COL[n]], start)
        H[('roi', base, start)] = 'reproduced' if rsc and not tie else ('tie' if rsc else 'not')
        print(f'   baseline {base} ms, from {int(start * 1000)} ms: first d>2 (ms) {first}; RSC earliest {rsc}, tie {tie}')
print('   trials whose first frame after the stimulus is more than one frame late, jRGECO1a sessions:', int(sum(LATE[k].sum() for k in JR)))
# pixel part
pgroups = {sid: {'W+ hit': np.where(wplus_hit(trial_table(sid)))[0], 'W- miss': np.where(wminus_miss(trial_table(sid)))[0]} for sid in JR}
import time
t_pix = time.time()
PIX = bech.load_pixels(A[A.session_id.isin(JR)], pgroups, n=12)
t_pix = time.time() - t_pix
GB_PIX = sum(v['n']['W+ hit'] + v['n']['W- miss'] for v in PIX.values() if 'n' in v) * (bech.PIX_PRE + bech.PIX_POST) * 125 * 160 * 8 / 1e9
print(f'pixel reads: {GB_PIX:.1f} GB in {t_pix / 60:.1f} min, {GB_PIX / t_pix * 1000:.0f} MB/s with 12 parallel reads')
print('pixel part: sessions failed', [k for k, v in PIX.items() if 'error' in v])
P0 = next(iter(PIX.values()))
print('stack', P0['info'], '| trials read per session, W+ hits', pd.Series({k: v['n']['W+ hit'] for k, v in PIX.items()}).describe().round(0).to_dict(),
      '| W- misses', pd.Series({k: v['n']['W- miss'] for k, v in PIX.items()}).describe().round(0).to_dict())
print('pixels without data (NaN, outside the brain) per frame:', int(np.isnan(P0['means']['W+ hit'][50][0]).sum()), 'of', P0['means']['W+ hit'][50][0].size,
      '| grid masks identical in every session:', all((v['masks'] == P0['masks']).all() for v in PIX.values()),
      '| pixels per ROI circle', int(P0['masks'][SIDX[bech.SITES['RSC']]].sum()))
from scipy.ndimage import gaussian_filter
JR_MICE = sorted({s.split('_')[0] for s in JR})
tp = np.arange(bech.PIX_POST) / 100
for base in BASES:
    for smooth in (True, False):
        X = {}
        for g in ('W+ hit', 'W- miss'):
            per = []
            for mo in JR_MICE:
                x = np.mean([v['means'][g][base] for k, v in PIX.items() if k.startswith(mo + '_') and v['n'][g] > 0], 0)
                if smooth: x = np.stack([gaussian_filter(np.nan_to_num(f), 1) for f in x])
                per.append(x)
            X[g] = np.stack(per)
        dp = bech.dprime(X['W+ hit'], X['W- miss'])
        masks = {n: P0['masks'][SIDX[bech.SITES[n]]].astype(bool) for n in ROI}
        for start in [0.02, 0.03]:
            first, rsc, tie = first_cross(tp, lambda k, n: np.nanmax(dp[k][masks[n]]), start)
            H[('pixel', smooth, base, start)] = 'reproduced' if rsc and not tie else ('tie' if rsc else 'not')
            print(f'   pixels, {"smoothed" if smooth else "unsmoothed (variant)"}, baseline {base} ms, from {int(start * 1000)} ms: first d>2 (ms) {first}; RSC earliest {rsc}, tie {tie}')
for base in [50, 250]:
    v = {H[('roi', base, s)] for s in (0.02, 0.03)} | {H[('pixel', True, base, s)] for s in (0.02, 0.03)}
    print(f'baseline {base} ms, ROI and smoothed pixel versions, both exclusion readings:', v)
""", tags=["claim:fig3h-rsc-first-context-discrimination"])
md("**Result: reproduced, resting on an assumption.** With the 50 ms baseline, which the Methods for Figure 3H take from Figure 3F, RSC is the earliest area in both the ROI ranking and the smoothed pixel version, under both exclusion readings, with no tie. With the 250 ms baseline RSC is first in the ROI ranking but ties with wM1 in the pixel version (50 ms), which counts as partially reproduced; the unsmoothed pixel variant at 250 ms puts wM1 and tjS1 first.")

md("""
### fig3-gcamp-consistent-controls-flat
> GCaMP6f mice show whisker-evoked dynamics consistent with jRGECO1a mice, and calcium-insensitive tdTomato and GFP control mice show none of these dynamics.

Evoked response at an ROI: d' >= 1 across mice between the (not baseline-subtracted) value at some time
from 20 to 120 ms and the mean of the baseline window, W+ hits, the Methods' rule for Figure 3C applied to ΔF/F0.
""")
code("""
def evoked(sids, base):
    t, X, mice = stack(mouse_traces(sids, wplus_hit, base, subtract=False))
    b = (t < 0) & (t >= -base / 1000 - 1e-9)
    B = np.nanmean(X[:, b, :], 1)
    w = (t >= 0.02 - 1e-9) & (t <= 0.12 + 1e-9)
    dd = np.array([bech.dprime(X[:, i, :], B) for i in np.where(w)[0]])
    return dd, mice
res = {}
for base in BASES:
    for line, n in [('GCaMP6f', 'sessions_Context_sessions_expert_WF_gcamp'), ('tdTomato', 'sessions_Context_sessions_expert_WF_tomato'), ('GFP', 'sessions_Context_sessions_expert_WF_GFP')]:
        sids = LISTS[n]
        dd, mice = evoked(sids, base)
        ev = np.nanmax(dd[:, COL['wS1']])
        t, Xp, _ = stack(mouse_traces(sids, wplus_hit, base)); _, Xm, _ = stack(mouse_traces(sids, wminus_miss, base))
        d = bech.dprime(Xp, Xm)
        l = (t >= 0.05 - 1e-9) & (t <= 0.12 + 1e-9); w = (t >= 0.02 - 1e-9) & (t <= 0.12 + 1e-9)
        ctxd = max(np.nanmax(d[l, COL[k]]) for k in ['RSC', 'wM1', 'wM2'])
        anyd = max(np.nanmax(np.abs(d[w, COL[k]])) for k in ROI)
        peak = np.nanmax(Xp.mean(0)[w, COL['wS1']])
        res[(base, line)] = (ev, ctxd, anyd)
        print(f'baseline {base} ms, {line} ({len(mice)} mice): wS1 evoked d max {ev:.2f}, wS1 mean peak dF/F0 {peak:.4f}; '
              f'max W+ > W- d in RSC/wM1/wM2 (50-120 ms) {ctxd:.2f}; max |d| W+ vs W- over ROIs (20-120 ms) {anyd:.2f}')
    g = res[(base, 'GCaMP6f')]; gc = g[0] >= 1 and g[1] > 2
    ctrl = all(res[(base, l)][0] < 1 and res[(base, l)][2] <= 2 for l in ['tdTomato', 'GFP'])
    print(f'   GCaMP6f part {gc}; controls part {ctrl} ->', 'reproduced' if gc and ctrl else ('partially' if gc or ctrl else 'not'))
""", tags=["claim:fig3-gcamp-consistent-controls-flat"])
md("**Result: partially reproduced.** The GCaMP6f part holds under every baseline; tdTomato and GFP mice have no evoked wS1 response but do show W+ against W- differences above d' 2.")

md("""
### fig4c-inhibition-propagates-forward
> Inhibiting wS1 decreases activity widely across cortex, inhibiting wM1/2 decreases activity among motor areas while leaving whisker sensory responses intact, and inhibiting RSC does not increase activity in wM1/2 or tongue-jaw motor regions.

Whisker trials in W+, the 4 widefield-with-optogenetics mice (50 Hz imaging), by laser site; control is
laser off the brain (opto_stim 0). Peak ΔF/F0 from 50 to 120 ms per ROI.
""")
code("""
WO = LISTS['sessions_Context_sessions_wf_opto']
def site_sel(site):
    def f(tr):
        base = (tr.trial_type == 'whisker_trial') & (tr.context == 1)
        if site == 'control': return base & (tr.opto_stim == 0)
        ap, ml = bech.SITES[site]
        return base & (tr.opto_stim == 1) & np.isclose(tr.opto_grid_ap, ap) & np.isclose(tr.opto_grid_ml, ml)
    return f
wo_trials = T[T.session_id.isin(WO)]
print('wf-opto sites stimulated:', wo_trials[wo_trials.opto_stim == 1].groupby(['opto_grid_ap', 'opto_grid_ml']).size().shape[0],
      '| control laser coordinates', wo_trials[wo_trials.opto_stim == 0][['opto_grid_ap', 'opto_grid_ml']].value_counts().to_dict())
DROP_LATE = False
def peaks(sids, site, base):
    mt = mouse_traces(sids, site_sel(site), base, drop_late=DROP_LATE)
    t, X, mice = stack(mt)
    w = (t >= 0.05 - 1e-9) & (t <= 0.12 + 1e-9)
    return pd.DataFrame(np.nanmax(X[:, w, :], 1)[:, [COL[n] for n in ROI]], index=mice, columns=ROI)
def fig4c(sids, base, sites):
    C = peaks(sids, 'control', base)
    out = {}
    for s in sites:
        P = peaks(sids, s, base)
        diff = P.mean() - C.loc[P.index].mean(); sd = C.loc[P.index].std(ddof=1)
        out[s] = (diff, sd, P.mean(), len(P))
    return C, out
print('late-frame trials in the wf-opto sessions:', int(sum(LATE[k].sum() for k in WO)), 'of', int(sum(len(LATE[k]) for k in WO)))
for base, DROP_LATE in [(50, False), (250, False), (50, True)]:
    if DROP_LATE: print('variant: trials whose first frame after the stimulus is more than one frame late left out')
    C, out = fig4c(WO, base, ['wS1', 'wM1', 'wM2', 'RSC'])
    print(f'baseline {base} ms; control peak (mean over {len(C)} mice):', C.mean().round(4).to_dict())
    dec = {s: (o[0] < -o[1]) for s, o in out.items()}
    for s, o in out.items():
        print(f'   laser at {s} ({o[3]} mice): peak minus control', o[0].round(4).to_dict(), '| decreased:', [k for k, v in dec[s].items() if v])
    p1 = dec['wS1'].sum() > len(ROI) / 2
    p2 = any(dec[s][['wM1', 'wM2', 'ALM', 'tjM1']].any() and not dec[s][['wS1', 'wS2']].any() for s in ['wM1', 'wM2'])
    up = out['RSC'][0] > out['RSC'][1]
    p3 = not up[['wM1', 'wM2', 'ALM', 'tjM1', 'tjS1']].any()
    p1, p2, p3 = bool(p1), bool(p2), bool(p3)
    n = int(p1) + int(p2) + int(p3)
    print(f'   parts: wS1 widespread {p1} ({dec["wS1"].sum()} of {len(ROI)}), wM1/2 motor only {p2}, RSC no increase {p3} ->',
          'reproduced' if n == 3 else ('partially' if n == 2 else 'not'))
DROP_LATE = False
""", tags=["claim:fig4c-inhibition-propagates-forward"])
md("**Result: reproduced.** All three parts hold under both baselines; wS1 inhibition lowers 7 of 9 ROIs, wM1 inhibition lowers motor ROIs and not wS1 or wS2, and RSC inhibition raises no motor ROI.")

md("""
### supp4d-photoactivation-control
> In mice expressing jRGECO1a without ChR2, the laser gives only a local photoactivation effect and none of the widespread inhibition seen in ChR2 mice.
""")
code("""
PA = LISTS['sessions_Context_sessions_wf_opto_photoactivation']
pa_tr = T[T.session_id.isin(PA)]
print('photoactivation sessions', len(PA), 'mice', pa_tr.mouse_id.nunique(), '| sites', pa_tr[pa_tr.opto_stim == 1].groupby(['opto_grid_ap', 'opto_grid_ml']).size().to_dict())
print('frame rates', rates.reindex(PA).to_dict())
for base in [50, 250]:
    C = peaks(PA, 'control', base)
    for s in ['wS1', 'wM1', 'wM2']:
        try:
            P = peaks(PA, s, base)
        except Exception as e:
            print(f'baseline {base}: no trials at {s}'); continue
        diff = P.mean() - C.loc[P.index].mean(); sd = C.loc[P.index].std(ddof=1)
        others = [r for r in ROI if r != s]
        fall = int((diff[others] < -sd[others]).sum())
        print(f'baseline {base} ms, laser at {s} ({len(P)} mice): stimulated ROI minus control {diff[s]:+.4f}; '
              f'other ROIs below control by more than SD: {fall} of {len(others)} -> holds {diff[s] > 0 and fall < len(others) / 2}')
        print('    differences', diff.round(4).to_dict())
""", tags=["claim:supp4d-photoactivation-control"])
md("**Result: reproduced.** At wS1, wM1 and wM2 the stimulated ROI rises above control and at most 1 of 8 other ROIs falls by more than the control SD.")


md("""
## Orofacial tracking (Figure 1I-J, Figure 3B-C)

Sessions: the four widefield expert groups (claims file, 24 mice, 97 sessions). The DLC series are
stored in pixels (with a `conversion` of 1/28 or 1/24 and the unit "seconds"); the measures are
computed from the tracked points as the Methods define them (Behavioral kinematics; Figures 1I-J),
with the side camera's 28 pixels/mm (Methods, Behavior videography). Whisker trials only, early-lick
trials dropped, mean over the 2 s before the stimulus per trial, then per session, then per mouse.
""")
code("""
FACE = sorted(set().union(*[LISTS[n] for n in WF_LISTS[:4]]))
DLC = bech.load_dlc(A[A.session_id.isin(FACE)], n=8)
bad = {k: v['error'] for k, v in DLC.items() if 'error' in v}
print('sessions', len(DLC), 'mice', len({k.split('_')[0] for k in DLC}), '| failed to load:', bad)
ok = {k: v for k, v in DLC.items() if 'error' not in v}
print('video rate (Hz):', pd.Series({k: round(v['rate']) for k, v in ok.items()}).value_counts().to_dict())
frac = pd.DataFrame({k: v['frac'] for k, v in ok.items()}).T
print('fraction of points passing the likelihood filter, by body part:'); print(frac.describe().round(3).to_string())
print('sessions kept (>= 70% of points):', (frac >= bech.KEEP_FRACTION).sum().to_dict())
pre = []
for k, v in ok.items():
    p = v['pre'].copy(); tr = trial_table(k) if k in G else T[T.session_id == k].sort_values('start_time').reset_index(drop=True)
    assert len(tr) == len(p)
    p = pd.concat([tr[['trial_type', 'context', 'lick_flag', 'early_lick']].reset_index(drop=True), p], axis=1)
    p['session_id'] = k; p['mouse_id'] = k.split('_')[0]
    for part, cols in [('pupil', ['pupil', 'stored_pupil_area']), ('jaw', ['jaw', 'jaw_speed', 'jaw_speed_x200']), ('whisker', ['whisker_angle', 'whisker_speed', 'stored_whisker_angle', 'stored_whisker_speed'])]:
        if frac.loc[k, part] < bech.KEEP_FRACTION: p[cols] = np.nan
    pre.append(p)
PRE = pd.concat(pre, ignore_index=True)
PW = PRE[(PRE.trial_type == 'whisker_trial') & (PRE.early_lick == 0)]
print('whisker trials', len(PW), '| value ranges (1st, 99th percentile):')
for c in ['pupil', 'jaw', 'whisker_angle', 'jaw_speed', 'whisker_speed', 'stored_pupil_area', 'stored_whisker_angle', 'stored_whisker_speed']:
    print('  ', c, np.nanpercentile(PW[c], [1, 99]).round(3), 'missing', PW[c].isna().mean().round(3))
def mouse_means(col, by):
    s = PW.dropna(subset=[col]).groupby(['mouse_id', 'session_id', by])[col].mean()
    return s.groupby(['mouse_id', by]).mean().unstack()
def paired(col, by, a, b):
    m = mouse_means(col, by).dropna()
    r = stats.ttest_rel(m[a], m[b])
    return m, r
""")

md("""
### fig1i-pupil-larger-wplus
> Before the whisker stimulus, pupil area is larger in W+ than in W- (0.52 ± 0.13 against 0.50 ± 0.12 mm2), while whisker angle and jaw opening show no general effect of context.
""")
code("""
for col in ['pupil', 'whisker_angle', 'jaw', 'stored_whisker_angle']:
    m, r = paired(col, 'context', 1, 0)
    print(f'{col}: W+ {m[1].mean():.3f} ± {m[1].std():.3f}, W- {m[0].mean():.3f} ± {m[0].std():.3f}, mice {len(m)}, '
          f't {r.statistic:.2f}, p {r.pvalue:.4f}, Bonferroni x20 {min(1, 20 * r.pvalue):.4f}')
m, r = paired('pupil', 'context', 1, 0)
print('pupil within tolerance:', abs(m[1].mean() - 0.52) <= 0.13, abs(m[0].mean() - 0.50) <= 0.12, '| W+ larger with corrected p < 0.05:', m[1].mean() > m[0].mean() and 20 * r.pvalue < 0.05)
print('per mouse W+ minus W- pupil (mm2):', (m[1] - m[0]).round(4).to_dict())
""", tags=["claim:fig1i-pupil-larger-wplus"])
md("**Result: reproduced.** Pupil area 0.53 and 0.51 mm2, W+ larger with corrected p below 0.05, and no corrected context effect on whisker angle or jaw opening.")

md("""
### fig1i-posture-before-lick
> Independently of context, before trials in which the mouse then licks to the whisker stimulus the jaw rests more open (0.27 ± 0.05 against 0.23 ± 0.04 mm) and the whisker is more posterior (97.3 ± 13 against 98.6 ± 12 degrees).
""")
code("""
for col, (el, en, tl, tn) in [('jaw', (0.27, 0.23, 0.05, 0.04)), ('whisker_angle', (97.3, 98.6, 13, 12)), ('stored_whisker_angle', (97.3, 98.6, 13, 12))]:
    m, r = paired(col, 'lick_flag', 1, 0)
    print(f'{col}: lick {m[1].mean():.3f} ± {m[1].std():.3f} ({el} ± {tl}: {abs(m[1].mean() - el) <= tl}), no lick {m[0].mean():.3f} ± {m[0].std():.3f} '
          f'({en} ± {tn}: {abs(m[0].mean() - en) <= tn}), mice {len(m)}, t {r.statistic:.2f}, p x20 {min(1, 20 * r.pvalue):.4f}')
""", tags=["claim:fig1i-posture-before-lick"])
md("**Result: reproduced.** The jaw is more open and the whisker angle smaller before lick trials, all four means within tolerance and both corrected p below 0.05. `whisker_angle` is the Methods' angle computed from the tracked points; `stored_whisker_angle`, the file's series, is a variant and gives the paper's values.")

md("""
### fig1j-jaw-speed-context
> Pre-stimulus jaw speed is higher in the rewarded context (3.0 ± 1.0 against 2.5 ± 0.8 mm/s), and also before lick than before no-lick trials, while whisking speed shows no effect of context or lick.
""")
code("""
for col in ['jaw_speed', 'jaw_speed_x200', 'whisker_speed', 'stored_whisker_speed']:
    for by in ['context', 'lick_flag']:
        m, r = paired(col, by, 1, 0)
        print(f'{col} by {by}: 1 {m[1].mean():.3f} ± {m[1].std():.3f}, 0 {m[0].mean():.3f} ± {m[0].std():.3f}, mice {len(m)}, t {r.statistic:.2f}, p x20 {min(1, 20 * r.pvalue):.4f}')
m, r = paired('jaw_speed', 'context', 1, 0); m2, r2 = paired('jaw_speed', 'lick_flag', 1, 0)
print('within tolerance: W+', abs(m[1].mean() - 3.0) <= 1.0, 'W-', abs(m[0].mean() - 2.5) <= 0.8, 'lick', abs(m2[1].mean() - 2.8) <= 0.28, 'no lick', abs(m2[0].mean() - 2.6) <= 0.7)
""", tags=["claim:fig1j-jaw-speed-context"])
md("**Result: partially reproduced.** Jaw speed is higher in W+ and before lick with corrected p below 0.05 and all four means within tolerance, but whisker speed is also higher in W+ (corrected p 0.018), where the claim states no effect.")

md(r"""
## Gradient-boosted model of the whisker-trial choice (Figure 1K-L)

As the claims file gives it (process main_analysis/model_context_behaviour.py; configs/analysis_params/
whisker_classification.yaml; explain_behaviour v1.0.1 preprocessing/trial_features.py and
models/behavioural_analysis_GBM.py, read at the commits the claims file cites): the code's 60 sessions of
21 mice; early licks dropped; the five DLC features of the code (`bech._model_one`); the trial features of
explain_behaviour (`bech.model_features`); whisker trials only; one session held out (numpy default_rng(20),
choice over the sessions in list order); categorical columns coded by sorted value; a stratified 67/33 split
(random_state 123); Optuna TPE (seed 123, 1000 trials, 80/20 inner split, random_state 123, binary log
loss, early stopping 100 rounds on the inner validation split); the final model fitted with early stopping
on the test split, as the code does, and on the inner validation split as a variant; balanced accuracy on
the test split. XGBoost runs on 4 threads (the code sets 20 for the search), which can change the fitted
trees slightly.
""")
code(r"""
import xgboost as xgb, optuna
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score, log_loss
MODEL_S = LISTS['session_context_expert_behaviour_model']
MF = bech.load_model_features(A[A.session_id.isin(MODEL_S)], n=8)
print('sessions', len(MF), '| kept or skipped by the 30% rule of the code:', pd.Series({k: v[1] for k, v in MF.items()}).value_counts().to_dict())
MDF = pd.concat([MF[s][0] for s in MODEL_S if MF[s][0] is not None], ignore_index=True)
MFE = bech.model_features(MDF)
FEAT = ['context', 'subject', 'cum_water', 'prev_trial_correct', 'whisker_trial_in_block', 'prev_trial_water', 'last_stimulus_type',
        'prev_whisker_rewarded', 'time_since_last_stimulus', 'lick_flag', 'pupil_area_nanmean', 'jaw_y_nanmean', 'whisker_velocity_mean_abs',
        'whisker_angle_mean', 'jaw_y_mean_abs_diff']
LABELS = ['Context', 'Mouse ID', 'Cumulative water', 'Previous trial correct', 'Whisker trial in block', 'Previous trial water', 'Last stimulus type',
          'Previous whisker rewarded', 'Time since last stimulus', 'Lick flag', 'Pupil Area', 'Jaw y', 'Whisker Speed', 'Whisker Angle', 'Jaw Speed']
MW = MFE[MFE.trial_type == 'whisker_trial']
test_session = np.random.default_rng(20).choice(MW['session'].unique())
MWt, MW = MW[MW.session == test_session], MW[MW.session != test_session]
def code_cats(Xd, maps=None):
    Xd = Xd.copy(); maps = maps or {}
    for col in ['Context', 'Mouse ID', 'Previous trial correct', 'Previous whisker rewarded', 'Last stimulus type']:
        if col not in maps:
            u = Xd[col].unique()
            try: u = np.sort(u)
            except TypeError: pass
            maps[col] = {v: i for i, v in enumerate(u)}
        Xd[col] = Xd[col].map(maps[col])
    return Xd, maps
MX, CMAP = code_cats(MW[FEAT].rename(columns=dict(zip(FEAT, LABELS))))
My = MX.pop('Lick flag').astype(int)
print('whisker trials', len(MX), 'in', MW.session.nunique(), 'sessions of', MW.subject.nunique(), 'mice; held-out session', test_session, len(MWt), 'trials')
print('lick rate', round(My.mean(), 3), '| missing values per feature:', MX.isna().mean().round(3)[MX.isna().mean() > 0].to_dict())
print('feature ranges:', {c: (round(float(MX[c].min()), 2), round(float(MX[c].max()), 2)) for c in MX.columns})
Xtr, Xte, ytr, yte = train_test_split(MX, My, test_size=0.33, random_state=123, stratify=My)
Xo, Xv, yo, yv = train_test_split(Xtr, ytr, test_size=0.2, random_state=123)
def objective(trial):
    p = dict(subsample=trial.suggest_float('subsample', 0.1, 1), learning_rate=trial.suggest_float('learning_rate', 0.0001, 0.5, log=True),
             max_depth=trial.suggest_int('max_depth', 7, 20), min_child_weight=trial.suggest_int('min_child_weight', 1, 200),
             reg_alpha=trial.suggest_float('reg_alpha', 0.001, 10, log=True), reg_lambda=trial.suggest_float('reg_lambda', 0.001, 10, log=True),
             gamma=trial.suggest_float('gamma', 0, 20), colsample_bytree=trial.suggest_float('colsample_bytree', 0.5, 1),
             colsample_bylevel=trial.suggest_float('colsample_bylevel', 0.5, 1), colsample_bynode=trial.suggest_float('colsample_bynode', 0.5, 1),
             n_estimators=trial.suggest_int('n_estimators', 100, 1000), scale_pos_weight=trial.suggest_float('scale_pos_weight', 1, 10))
    m = xgb.XGBClassifier(**p, eval_metric='logloss', early_stopping_rounds=100, random_state=123, verbosity=0, n_jobs=4)
    m.fit(Xo, yo, eval_set=[(Xv, yv)], verbose=False)
    return log_loss(yv, m.predict_proba(Xv)[:, 1])
optuna.logging.set_verbosity(optuna.logging.WARNING)
study = optuna.create_study(direction='minimize', sampler=optuna.samplers.TPESampler(seed=123))
study.optimize(objective, n_trials=1000)
print('Optuna trials', len(study.trials), '| best inner log loss', round(study.best_value, 4), '| best parameters', {k: round(v, 4) for k, v in study.best_params.items()})
def fit_final(Xe, ye):
    m = xgb.XGBClassifier(**study.best_params, objective='binary:logistic', eval_metric='logloss', early_stopping_rounds=100, random_state=123, verbosity=0, n_jobs=4)
    return m.fit(Xtr, ytr, eval_set=[(Xe, ye)], verbose=False)
GBM = fit_final(Xte, yte)
""")
md(r"""
### fig1k-model-accuracy
> A gradient-boosted tree model of the whisker-trial lick choice, from task, history and orofacial features, reaches a cross-validated accuracy of 0.78 on held-out test trials.

Chance for balanced accuracy is 0.5; the accuracy of a model fitted with the lick labels permuted is shown as a reference.
""")
code(r"""
ba = balanced_accuracy_score(yte, GBM.predict(Xte))
print(f'balanced accuracy, test split: {ba:.3f} (0.78 ± 0.078: {abs(ba - 0.78) <= 0.078}) | train {balanced_accuracy_score(ytr, GBM.predict(Xtr)):.3f} | trees {GBM.best_iteration + 1}')
GBMv = fit_final(Xv, yv)
print(f'variant, early stopping on the inner validation split: {balanced_accuracy_score(yte, GBMv.predict(Xte)):.3f}')
Xh, _ = code_cats(MWt[FEAT].rename(columns=dict(zip(FEAT, LABELS))), CMAP); yh = Xh.pop('Lick flag').astype(int)
print(f'held-out session {test_session}: balanced accuracy {balanced_accuracy_score(yh, GBM.predict(Xh)):.3f} on {len(yh)} trials')
yperm = pd.Series(np.random.default_rng(31).permutation(ytr.values), index=ytr.index)
mp = xgb.XGBClassifier(**study.best_params, objective='binary:logistic', eval_metric='logloss', early_stopping_rounds=100, random_state=123, verbosity=0, n_jobs=4)
mp.fit(Xtr, yperm, eval_set=[(Xte, yte)], verbose=False)
print(f'reference, labels of the training split permuted: {balanced_accuracy_score(yte, mp.predict(Xte)):.3f} (chance 0.5)')
""", tags=["claim:fig1k-model-accuracy"])
md("**Result: reproduced.** The balanced accuracy on the test split is within 0.78 ± 0.078, against 0.50 for the model fitted on permuted labels (printed above).")
md(r"""
### fig1k-context-strongest-feature
> Among the model's features, context gives the largest drop in accuracy when permuted, followed by whether the previous whisker trial was rewarded, the cumulative number of rewards and the index of the whisker trial in the block.

Each feature permuted 10,000 times on the test split, the drop in balanced accuracy recorded (claims file).
""")
code(r"""
rng_pi = np.random.default_rng(32)
BOOST, ITR = GBM.get_booster(), (0, GBM.best_iteration + 1)
Xn, yn = Xte.values.astype(np.float32), yte.values
def bacc(p):  # balanced accuracy of the 0.5-threshold prediction, as GBM.predict gives it
    return 0.5 * ((p[yn == 1] > 0.5).mean() + (p[yn == 0] <= 0.5).mean())
base_ba = bacc(BOOST.inplace_predict(Xn, iteration_range=ITR))
print('balanced accuracy of the fast predictor equals that of the model:', np.isclose(base_ba, balanced_accuracy_score(yte, GBM.predict(Xte))))
drops = {}
for j, col in enumerate(Xte.columns):
    Xp_ = Xn.copy(); d = np.empty(10000)
    for i in range(10000):
        Xp_[:, j] = rng_pi.permutation(Xn[:, j])
        d[i] = base_ba - bacc(BOOST.inplace_predict(Xp_, iteration_range=ITR))
    drops[col] = (d.mean(), d.std(), np.percentile(d, 2.5), np.percentile(d, 97.5))
PI = pd.DataFrame(drops, index=['mean drop', 'SD', '2.5%', '97.5%']).T.sort_values('mean drop', ascending=False)
print(PI.round(4).to_string())
top = list(PI.index)
print('order:', top[:5], '| context first:', top[0] == 'Context', '| next three as stated:', top[1:4] == ['Previous whisker rewarded', 'Cumulative water', 'Whisker trial in block'],
      '| the three in the top five:', set(['Previous whisker rewarded', 'Cumulative water', 'Whisker trial in block']) <= set(top[:5]))
""", tags=["claim:fig1k-context-strongest-feature"])
md("**Result: reproduced.** Context gives the largest mean drop in balanced accuracy, followed in order by previous whisker rewarded, cumulative water and whisker trial in block (printed above).")
md(r"""
### fig1l-shap-whisker-trial-in-block
> The SHAP values of the whisker-trial-in-block feature follow the behaviour, with a single-trial change after a context transition and a slower further component.

Interventional TreeExplainer, 100 background trials from the training split (random_state 123), over the
training and test trials; whisker trials 5 to 8 of a block relabelled -4 to -1 (claims file).
""")
code(r"""
import shap
Xall = pd.concat([Xtr, Xte]).astype(float)
bg = Xtr.sample(min(100, len(Xtr)), random_state=123).astype(float)
expl = shap.TreeExplainer(GBM, data=bg, feature_perturbation='interventional', model_output='raw')
SV = expl.shap_values(Xall)
sv = pd.DataFrame({'pos': Xall['Whisker trial in block'].values, 'ctx': Xall['Context'].values,
                   'shap': SV[:, list(Xall.columns).index('Whisker trial in block')]})
sv['rel'] = np.where(sv.pos >= 5, sv.pos - 9, sv.pos)
ctx_code = {v: k for k, v in CMAP['Context'].items()}
sv['context'] = sv.ctx.map(ctx_code)
print('positions in block:', sv.pos.value_counts().sort_index().to_dict())
tab = sv.groupby(['context', 'rel']).shap.agg(['mean', 'count']).unstack(0)
print(tab.round(4).to_string())
m = sv.groupby(['context', 'rel']).shap.mean()
res = {}
for newc, oldc, sgn, name in [(1, 0, 1, 'W- to W+'), (0, 1, -1, 'W+ to W-')]:
    s1, s2, sm1 = m[(newc, 1)], m[(newc, 2)], m[(oldc, -1)]
    flip = sgn * s1 > 0 and sgn * sm1 < 0
    further = sgn * s2 > sgn * s1
    res[name] = (flip, further)
    print(f'{name}: trial -1 (old block) {sm1:+.4f}, trial 1 {s1:+.4f}, trial 2 {s2:+.4f} -> sign change toward the new context {flip}, trial 2 further {further}')
print('base value', np.round(expl.expected_value, 4), '| SHAP range of the feature', sv.shap.min().round(3), sv.shap.max().round(3))
# variant: the SHAP values of context and whisker trial in block summed, the model's account of both features together
sv['both'] = sv.shap + SV[:, list(Xall.columns).index('Context')]
mb = sv.groupby(['context', 'rel']).both.mean()
print('variant, context + whisker trial in block:', mb.unstack(0).round(3).to_dict())
for newc, oldc, sgn, name in [(1, 0, 1, 'W- to W+'), (0, 1, -1, 'W+ to W-')]:
    print(f'   {name}: trial -1 {mb[(oldc, -1)]:+.3f}, trial 1 {mb[(newc, 1)]:+.3f}, trial 2 {mb[(newc, 2)]:+.3f}, trial 4 {mb[(newc, 4)]:+.3f}')
""", tags=["claim:fig1l-shap-whisker-trial-in-block"])
md("**Result: not reproduced as the criterion reads it.** In both directions the SHAP value of whisker trial in block at trial 1 of the new block does not take the sign of the new context: it moves against it (negative after W- to W+, positive after W+ to W-), and trial 2 then moves toward the new context. The feature carries the one-trial lag of the behaviour, while context carries the switch (variant with both features summed, printed above).")

md("""
### fig3c-jaw-onset
> Jaw opening, the first movement, begins 108 ± 24 ms after the sensory stimulus, so the first 120 ms after the stimulus largely precede movement.

jRGECO1a mice. As the Methods (Figures 3B and 3C): jaw opening filtered at 60% likelihood (points below it
set missing, not dropped trials), and, "as in Figures 1I&J", the jaw dropped for a session when under 70%
of its points pass (the variant without this rule is shown); each trial centred on its mean over the 250 ms
before the stimulus; traces averaged within session, then over sessions per mouse. Methods' onset rule:
per mouse, the d' (ddof 0) at each time between the trial values of jaw opening (missing points left out)
and the trials' pre-stimulus mean (0 after centring); onset is the first time after the stimulus with d' >= 1.
The d' over session means is a variant. Trial sets: (a) the Methods' correct whisker trials, W+ hits and
W- misses pooled (Figure 3B: "correct trials (i.e. licks to whisker in W+ and no licks in W-)"), (b) W+
whisker hits, (c) the code's auditory and whisker hits, and the Figure 3C legend's groups (auditory hits
in W+ and W-, whisker hits in W-). The code's rule (per trial, the first time |jaw| over its pre-stimulus
SD exceeds 3, averaged per session, then mouse) is a variant.
""")
code("""
sets = {'(a) correct whisker, W+ hits and W- misses': lambda tr: (tr.trial_type == 'whisker_trial') & (tr.lick_flag == tr.context),
        '(b) W+ whisker hits': lambda tr: (tr.trial_type == 'whisker_trial') & (tr.context == 1) & (tr.lick_flag == 1),
        '(c) auditory and whisker hits (code)': lambda tr: tr.trial_type.isin(['whisker_trial', 'auditory_trial']) & (tr.lick_flag == 1),
        'auditory hits W+': lambda tr: (tr.trial_type == 'auditory_trial') & (tr.context == 1) & (tr.lick_flag == 1),
        'auditory hits W-': lambda tr: (tr.trial_type == 'auditory_trial') & (tr.context == 0) & (tr.lick_flag == 1),
        'whisker hits W-': lambda tr: (tr.trial_type == 'whisker_trial') & (tr.context == 0) & (tr.lick_flag == 1)}
def first_d1(t, J):
    # J: values x time, centred on the pre-stimulus mean; d' of each time against the zero baseline means
    d = np.array([bech.dprime(J[np.isfinite(J[:, i]), i], np.zeros(np.isfinite(J[:, i]).sum())) if np.isfinite(J[:, i]).sum() > 2 else np.nan
                  for i in range(J.shape[1])])
    post = np.where((t > 0) & (d >= 1))[0]
    return t[post[0]] * 1000 if len(post) else np.nan
print('jaw points passing 60% likelihood per jRGECO1a session:', frac.reindex(JR).jaw.round(2).to_dict())
F3C = {}
for keep70 in (True, False):
    print('70% session rule (Methods, Figures 1I-J)' if keep70 else 'variant, without the 70% session rule')
    for name, sel in sets.items():
        rows = []
        for mouse in sorted({s.split('_')[0] for s in JR}):
            sids = [s for s in JR if s.startswith(mouse + '_') and s in ok and (not keep70 or frac.loc[s, 'jaw'] >= bech.KEEP_FRACTION)]
            Js, Ss, codes = [], [], []
            for sid in sids:
                tr = trial_table(sid); t = ok[sid]['jaw_t']
                J = ok[sid]['jaw_traces'][(sel(tr) & (tr.early_lick == 0)).values]
                b = (t < 0) & (t >= -0.25 - 1e-9)
                with np.errstate(all='ignore'):
                    bm = np.nanmean(J[:, b], 1); bs = np.nanstd(J[:, b], 1)
                    keep = np.isfinite(bm)
                    J, bs = J[keep] - bm[keep, None], bs[keep]
                    if len(J) == 0: continue
                    Js.append(J); Ss.append(np.nanmean(J, 0))
                    z = np.abs(J) / bs[:, None]
                    f1 = [t[np.where((t > 0) & (zz > 3))[0][0]] * 1000 for zz in z if ((t > 0) & (zz > 3)).any()]
                    codes.append(np.mean(f1) if f1 else np.nan)
            if not Js:
                rows.append((mouse, len(sids), 0, 0, np.nan, np.nan, np.nan, np.nan)); continue
            J = np.concatenate(Js); S_ = np.array(Ss)
            post_ = (t > 0) & (t <= 0.15)
            rows.append((mouse, len(Ss), len(J), round(float(np.isnan(J[:, post_]).mean()), 3), first_d1(t, J),
                         first_d1(t, S_) if len(S_) > 2 else np.nan, np.nanmean(codes), np.nan))
        R = pd.DataFrame(rows, columns=['mouse', 'sessions', 'trials', 'missing_0_150ms', 'onset_ms', 'onset_session_dprime', 'code_rule_ms', '_']).drop(columns='_').set_index('mouse')
        v = R.onset_ms
        F3C[(keep70, name)] = v.mean()
        print(f'  {name}: Methods onset {v.mean():.1f} ± SD {v.std():.1f} ms over {v.notna().sum()} mice (108 ± 24: {abs(v.mean() - 108) <= 24}); '
              f'd prime over session means {R.onset_session_dprime.mean():.1f} ({R.onset_session_dprime.notna().sum()} mice with 3 or more sessions); code rule {R.code_rule_ms.mean():.1f}')
        print('    per mouse:', R.round(1).to_dict('index'))
""", tags=["claim:fig3c-jaw-onset"])
md("**Result: reproduced, resting on an assumption.** With the Methods' correct whisker trials (a) and the 70% session rule the mean onset is within 108 ± 24 ms, and so it is without the rule. With W+ whisker hits only (b), with the code's auditory and whisker hits (c), and for auditory hits it is below the tolerance. The assumption is the Methods' trial set (a).")


md("""
## Low-dimensional trajectories under inhibition (Figure 4D-G)

As the Methods (Principal component analysis; Figure 4D; Figures 4E-G) and plot
utils/figure4C_G.py:434-535: the 4 widefield-with-optogenetics mice; grid ROI ΔF/F0 without baseline
subtraction, from -150 to 150 ms around trial onset (the whisker or catch stimulus); the 39 grid sites
the code keeps (AP 3.5 and (1.5, 5.5), (2.5, 4.5), (2.5, 5.5) left out). Control trials (laser off the
brain), whisker and catch, averaged per mouse over all its trials (the pseudosession), then over mice by
context, trial type, lick and time; StandardScaler and PCA with 15 components fitted on that matrix;
each component's sign set so that its wS1 loading is positive (the code's enforce_sign_consistency on
the wS1 column). Trials at each stimulated site, all trials pooled, are projected per mouse.
""")
code("""
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
KEEP = sorted([s for s in SIDX if s[0] != 3.5 and s not in [(1.5, 5.5), (2.5, 4.5), (2.5, 5.5)]], key=lambda s: str(s))
KC = [SIDX[s] for s in KEEP]
print('sites used', len(KEEP))
def pseudo(sids, select):
    # per mouse mean over all selected trials pooled across sessions: dict mouse -> (t, time x site)
    acc = {}
    for sid in sids:
        names, t, W, lag = G[sid]; tr = trial_table(sid); m = select(tr).values
        if m.sum() == 0: continue
        acc.setdefault(sid.split('_')[0], []).append(W[m][:, :, KC])
    out = {}
    for mouse, lst in acc.items():
        X = np.concatenate(lst); out[mouse] = (t, np.nanmean(X, 0), len(X))
    return out
def sel(tt, ctx, lick=None, site='control'):
    def f(tr):
        m = (tr.trial_type == tt) & (tr.context == ctx)
        if lick is not None: m &= tr.lick_flag == lick
        if site == 'control': return m & (tr.opto_stim == 0)
        return m & (tr.opto_stim == 1) & np.isclose(tr.opto_grid_ap, site[0]) & np.isclose(tr.opto_grid_ml, site[1])
    return f
rows, ctrl_mouse = [], {}
for ctx in (0, 1):
    for tt in ['whisker_trial', 'no_stim_trial']:
        for lick in (0, 1):
            pm = pseudo(WO, sel(tt, ctx, lick))
            t = next(iter(pm.values()))[0]; w = (t >= -0.15 - 1e-9) & (t <= 0.15 + 1e-9)
            X = np.stack([v[1][w] for v in pm.values()])
            ctrl_mouse[(ctx, tt, lick)] = {m: v[1][w] for m, v in pm.items()}
            rows.append(((ctx, tt, lick), np.nanmean(X, 0)))
tw = t[w]
Mtx = np.concatenate([r[1] for r in rows])
scaler = StandardScaler().fit(Mtx)
pca = PCA(n_components=15).fit(np.nan_to_num(scaler.transform(Mtx)))
wS1col = KEEP.index(bech.SITES['wS1'])
sgn = np.sign(pca.components_[:, wS1col]); sgn[sgn == 0] = 1
proj = lambda X: (pca.transform(np.nan_to_num(scaler.transform(X))) * sgn)
print('time samples', len(tw), tw.round(2), '| variance explained by PC1-5', pca.explained_variance_ratio_[:5].round(3), 'cumulative 15', pca.explained_variance_ratio_.sum().round(3))
print('sign flips applied (wS1 loading made positive), PC1-3:', sgn[:3])
print('loadings after the sign convention, PC1-3, named sites:')
print(pd.DataFrame((pca.components_[:3] * sgn[:3, None]).T, index=[str(s) for s in KEEP], columns=['PC1', 'PC2', 'PC3'])
      .loc[[str(bech.SITES[n]) for n in ['wS1', 'wS2', 'wM1', 'wM2', 'ALM', 'tjS1', 'tjM1', 'A1', 'RSC', 'RSC_2']]]
      .set_axis(['wS1', 'wS2', 'wM1', 'wM2', 'ALM', 'tjS1', 'tjM1', 'A1', 'RSC', 'RSC_2']).round(3).T.to_string())
ctrl_pc3 = {k: proj(v)[:, 2] for k, v in rows}
STIM = {}
for site_name in ['wS1', 'wS2', 'wM1', 'wM2', 'ALM', 'RSC', 'RSC_2', 'tjS1', 'tjM1', 'A1']:
    for ctx in (0, 1):
        pm = pseudo(WO, sel('whisker_trial', ctx, None, bech.SITES[site_name]))
        STIM[(site_name, ctx)] = {m: proj(v[1][w])[:, 2] for m, v in pm.items()}
ALLSITE = {}
for s in KEEP:
    for ctx in (0, 1):
        pm = pseudo(WO, sel('whisker_trial', ctx, None, s))
        ALLSITE[(s, ctx)] = {m: proj(v[1][w])[:, 2] for m, v in pm.items()}
post = tw >= -1e-9
""")

md("""
### fig4d-trajectories-follow-lick
> Projected onto PC3, inactivation of wS1, wS2, wM1/2 and ALM drives the trajectory away from the control-lick trajectory toward no-lick, while inhibition of RSC and tjS1 gives trajectories that follow the control-lick trajectory in both contexts.
""")
code("""
close = {}
for ctx in (0, 1):
    L1, L0 = ctrl_pc3[(ctx, 'whisker_trial', 1)][post], ctrl_pc3[(ctx, 'whisker_trial', 0)][post]
    print(f'{"W+" if ctx else "W-"}: control lick PC3 {L1.round(2)}; no lick {L0.round(2)}')
    for s in ['wS1', 'wS2', 'wM1', 'wM2', 'ALM', 'RSC', 'RSC_2', 'tjS1']:
        tr_ = np.mean(list(STIM[(s, ctx)].values()), 0)[post]
        dl, dn = np.mean((tr_ - L1) ** 2), np.mean((tr_ - L0) ** 2)
        close[(s, ctx)] = 'lick' if dl < dn else 'no lick'
        print(f'   {s}: MSD to lick {dl:.3f}, to no lick {dn:.3f} -> closer to {close[(s, ctx)]} (mice {len(STIM[(s, ctx)])})')
for rsc in ['RSC', 'RSC_2']:
    rt = all(close[(s, c)] == 'lick' for s in [rsc, 'tjS1'] for c in (0, 1))
    others = {c: [close[(s, c)] == 'no lick' for s in ['wS1', 'wS2', 'ALM']] + [close[('wM1', c)] == 'no lick' or close[('wM2', c)] == 'no lick'] for c in (0, 1)}
    full = rt and all(all(v) for v in others.values())
    part = rt and all(sum(v) >= 2 for v in others.values())
    print(rsc, '-> reproduced' if full else ('-> partially' if part else '-> not'), '| RSC and tjS1 closer to lick in both:', rt, '| others closer to no lick:', others)
""", tags=["claim:fig4d-trajectories-follow-lick"])
md("**Result: not reproduced.** RSC (-1.5, 0.5) is closer to no-lick in W-, and wS1, wS2, wM1/2 and ALM are not closer to no-lick in W-.")

md("""
### fig4e-rsc-tjs1-smaller-angle
> The PC3 trajectories under RSC and tjS1 inhibition make smaller angles with the control-lick trajectory than those under inhibition of the other regions, which decreased lick probability.
""")
code("""
def angle(v1, v2):
    return np.degrees(np.arccos(np.clip(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), -1, 1)))
def site_angles(store, ctx, code_variant=False):
    L1 = np.mean([v for v in ctrl_mouse_pc3(ctx).values()], 0)
    out = {}
    for key, per in store.items():
        if key[1] != ctx: continue
        vals = []
        for m, tr_ in per.items():
            a, b = tr_[post], L1[post]
            if code_variant:
                mn = min(tr_[post].min(), 0) if False else tr_[post].min()
                a, b = a + mn, b + mn
            vals.append(angle(a, b))
        out[key[0]] = np.mean(vals)
    return out
def ctrl_mouse_pc3(ctx):
    return {m: proj(x)[:, 2] for m, x in ctrl_mouse[(ctx, 'whisker_trial', 1)].items()}
for variant in [False, True]:
    print('code variant (minimum added)' if variant else 'Methods angle')
    res = {}
    for ctx in (0, 1):
        ang = site_angles(STIM, ctx, variant)
        print(f'   {"W+" if ctx else "W-"}:', {k: round(v, 1) for k, v in ang.items()})
        for rsc in ['RSC', 'RSC_2']:
            small = max(ang[rsc], ang['tjS1']) < min(ang['wS1'], ang['wS2'], ang['ALM']) and max(ang[rsc], ang['tjS1']) < max(ang['wM1'], ang['wM2'])
            res[(rsc, ctx)] = small
    for rsc in ['RSC', 'RSC_2']:
        n = int(bool(res[(rsc, 0)])) + int(bool(res[(rsc, 1)]))
        print('  ', rsc, {('W+' if c else 'W-'): res[(rsc, c)] for c in (0, 1)}, '->', 'reproduced' if n == 2 else ('partially' if n == 1 else 'not'))
""", tags=["claim:fig4e-rsc-tjs1-smaller-angle"])
md("**Result: partially reproduced.** RSC and tjS1 have the smallest angles in W+; in W- the RSC (-1.5, 0.5) angle is above those of wM1, wM2 and ALM.")

md("""
### fig4fg-angle-predicts-lick-change
> Across all inactivated sites, in W+ and in W-, the angle between the inhibition and control-lick trajectories relates to the change in lick probability the inhibition evokes.
""")
code("""
WO_MICE = sorted({s.split('_')[0] for s in WO})
obs_wo, _ = bech.opto_map(T[T.session_id.isin(WO)], WO_MICE, null='trials', n_shuffle=10, seed=21)
dpw = obs_wo[obs_wo.trial_type == 'whisker_trial'].groupby(['context', 'site']).dP.mean()
for variant in [False, True]:
    for ctx in (0, 1):
        ang = site_angles(ALLSITE, ctx, variant)
        sites = [s for s in ang if (ctx, s) in dpw.index]
        x = np.array([ang[s] for s in sites]); y = np.array([dpw[(ctx, s)] for s in sites])
        r = stats.linregress(x, y)
        print(f'{"code angle" if variant else "Methods angle"}, {"W+" if ctx else "W-"}: {len(sites)} sites, r {r.rvalue:.2f}, p {r.pvalue:.2g}, slope {r.slope:.4f} dP per degree; angle range {x.min():.1f} to {x.max():.1f}, dP range {y.min():.2f} to {y.max():.2f}')
""", tags=["claim:fig4fg-angle-predicts-lick-change"])
md("**Result: reproduced.** The correlation of angle with dP over 39 sites is negative with p below 0.05 in both contexts, for both angle definitions.")

md("""
## Pre-stimulus correlations (Figure 4A-B), a variant on the grid ROI traces

The three fig4b claims are blocked: the criterion uses seed-to-pixel correlation maps of the ΔF/F0 stack
in the 2 s before every trial, masked by a block-shuffle null. The reads alone are estimated below from the
rate measured for the pixel part of fig3h; with the rest of this notebook they do not fit the
notebook limit of 60 minutes. As a variant
that does not decide the outcome, the zero-lag Pearson correlations between the grid ROI traces of the
seven seeds (1 mm circles at the seed sites) in the 2 s before each trial start are computed, whisker
trials, correct (W+ hits, W- misses) and incorrect (W+ misses, W- hits), averaged per session, then per
mouse; the paired d' (mean of the W- minus W+ differences over their SD, ddof 1) and the related t-test
with Bonferroni x7 are given for the code's seven pairs. No null, so the connectivity claim is not
addressed.
""")
code("""
SEEDS = ['wS1', 'wS2', 'wM1', 'RSC', 'ALM', 'tjM1', 'tjS1']
PAIRS = [('ALM', 'tjM1'), ('ALM', 'tjS1'), ('tjM1', 'tjS1'), ('wM1', 'ALM'), ('wM1', 'tjM1'), ('wS1', 'wS2'), ('wS2', 'wM1')]
PC = bech.load_precorr(A[A.session_id.isin(JR)], [bech.SITES[s] for s in SEEDS], n=8)
n_all = int(T[T.session_id.isin(JR)].shape[0]); gb = n_all * 200 * 125 * 160 * 8 / 1e9
print(f'seed-to-pixel maps would need 200 frames for each of the {n_all} trials of the jRGECO1a sessions, {gb:.0f} GB; '
      f'at the rate of the fig3h pixel reads, {gb / (GB_PIX / t_pix) / 60:.0f} min of reading')
print('sessions failed', [k for k, v in PC.items() if isinstance(v, str)])
rows = []
for sid, C in PC.items():
    tr = trial_table(sid); assert len(tr) == len(C)
    w = (tr.trial_type == 'whisker_trial').values; corr = (tr.lick_flag == tr.context).values
    for ctx in (0, 1):
        for oc, m in [('correct', corr), ('incorrect', ~corr)]:
            s_ = w & (tr.context.values == ctx) & m & np.isfinite(C[:, 0, 1])
            if s_.sum() == 0: continue
            mc = C[s_].mean(0)
            for a, b in PAIRS:
                rows.append((sid.split('_')[0], sid, ctx, oc, f'{a}-{b}', mc[SEEDS.index(a), SEEDS.index(b)], s_.sum()))
R4 = pd.DataFrame(rows, columns=['mouse', 'session', 'context', 'outcome', 'pair', 'r', 'n'])
print('whisker trials with a full 2 s window per session and group, median:', R4.groupby(['session', 'context', 'outcome']).n.first().groupby(['context', 'outcome']).median().to_dict())
Mm = R4.groupby(['mouse', 'context', 'outcome', 'pair']).r.mean().unstack(['outcome', 'context'])
for oc in ['correct', 'incorrect']:
    print(oc, 'trials, mice', Mm.index.get_level_values(0).nunique())
    for a, b in PAIRS:
        x = Mm.xs(f'{a}-{b}', level='pair'); wm, wp = x[(oc, 0)].values, x[(oc, 1)].values
        dd = wm - wp; tt = stats.ttest_rel(wm, wp)
        print(f'   {a}-{b}: W- {wm.mean():.3f}, W+ {wp.mean():.3f}, W- minus W+ {dd.mean():+.3f}, paired d {dd.mean() / dd.std(ddof=1):+.2f}, t {tt.statistic:.2f}, p x7 {min(1, 7 * tt.pvalue):.3f}')
print('W+ incorrect minus W+ correct:', {f'{a}-{b}': round(float((Mm.xs(f'{a}-{b}', level='pair')[('incorrect', 1)] - Mm.xs(f'{a}-{b}', level='pair')[('correct', 1)]).mean()), 3) for a, b in PAIRS})
""", tags=["claim:fig4b-wminus-higher-correlation-correct"])
md("**Result: blocked (too_large).** The pixel analysis the criterion needs was not run. In the ROI-trace variant, before correct trials W- is higher than W+ for 5 of the 7 pairs (paired d' at or above 0.8 for 4 of them) and lower for wM1-ALM and wM1-tjM1, and no pair passes the corrected t-test; before incorrect trials no pair has a W- minus W+ d' of 0.8 or more.")


md("""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

| claim | outcome |
|---|---|
| session-list-link | partially reproduced (every list a claim uses matches; the pool list does not in full) |
| expert-sessions | not reproduced (the Methods' rule selects more sessions and mice; the code's list matches) |
| fig1c-auditory-hit-both-contexts, fig1c-whisker-context-modulation, fig1d, fig1c-catch-higher-wplus, fig1e, fig1g, fig1f, fig1h, supp1c | reproduced |
| supp1d-faster-response-wplus | partially reproduced (tests match, means about 100 ms longer) |
| fig1i-pupil-larger-wplus, fig1i-posture-before-lick | reproduced |
| fig1j-jaw-speed-context | partially reproduced (jaw holds; whisker speed differs by context) |
| fig1k-model-accuracy, fig1k-context-strongest-feature | reproduced |
| fig1l-shap-whisker-trial-in-block | not reproduced (trial 1 of a block moves against the new context; trial 2 toward it) |
| fig2c, fig2d, fig2e (2 claims), fig2-no-effect-control-mice, fig2cd-rsc, fig2f | blocked, methods_underspecified (the null and threshold readings disagree) |
| supp2-muscimol-ws1-rsc | reproduced |
| fig3c-jaw-onset | reproduced, resting on the Methods' correct whisker trials (assumption) |
| fig3e-auditory-similar-across-contexts | partially reproduced (similar, A1 first; the order of the others not found) |
| fig3f-whisker-divergence-after-50ms | reproduced |
| fig3h-rsc-first-context-discrimination | reproduced, resting on the 50 ms baseline (assumption); a tie in the pixel version with the 250 ms baseline |
| fig3-gcamp-consistent-controls-flat | partially reproduced (GCaMP6f holds; control mice also show W+ vs W- differences) |
| supp3c-rsc-projects-to-wm | blocked, data_missing |
| fig4b (3 claims) | blocked, too_large (pixel stack); an ROI-trace variant is shown |
| fig4c-inhibition-propagates-forward, supp4d-photoactivation-control, fig4fg-angle-predicts-lick-change | reproduced |
| fig4d-trajectories-follow-lick | not reproduced |
| fig4e-rsc-tjs1-smaller-angle | partially reproduced (W+ only at RSC (-1.5, 0.5); both contexts at (-0.5, 0.5)) |

Differences from the paper's method: session groups and mouse lines come from the code's lists, since the
files do not record the lines; the opto-map nulls and thresholds are run under every reading the claims
file names; the Figure 3H pixel maps are computed from windowed reads of the stack, while the Figure 4A-B
seed-to-pixel correlations are not run (an ROI-trace variant is shown); the gradient-boosted model of
Figure 1K-L is rebuilt from the code and run with 4 threads.

What was found about the dataset: the subject genotype is "WT" for every mouse but one, so no file says
which mice carry VGAT-ChR2, jRGECO1a, GCaMP6f, tdTomato or GFP; session type and day (Context Off, muscimol
or Ringer, baseline or injection) are not recorded in a usable form; the DLC series carry the unit
"seconds" and a `conversion` of 1/28 or 1/24 that does not turn them into the units of the paper (the
whisker angle is stored in degrees, the pupil area in square pixels); three files have no context epochs;
lick_time minus the stimulus time is about 100 ms longer than the paper's spout-contact times; the Context
Off sessions still label their trials pink and brown noise. The printed outputs above give the numbers.
""")

nbf.write(nbf.v4.new_notebook(cells=cells, metadata={"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}}),
          "reproduce_bech_2026.ipynb")

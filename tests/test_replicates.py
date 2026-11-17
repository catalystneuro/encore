"""tools/replicates.py: the agreement of a paper's runs, claim by claim."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import replicates  # noqa: E402

R, P, N, B = "reproduced", "partially_reproduced", "not_reproduced", "blocked"


def test_runs_that_agree_on_every_claim_have_a_kappa_of_one():
    table = [[R, R, R], [N, N, N], [B, B, B], [P, P, P]]
    assert replicates.fleiss_kappa(table) == 1 and replicates.pairwise(table) == 1


def test_kappa_follows_the_textbook_formula():
    # Two claims, two runs: one agreed (R, R), one not (R, N). P-bar = 0.5; p_R = 0.75, p_N = 0.25, so P_e = 0.625
    # and kappa = (0.5 - 0.625) / 0.375 = -1/3.
    table = [[R, R], [R, N]]
    assert abs(replicates.fleiss_kappa(table) - (-1 / 3)) < 1e-9 and replicates.pairwise(table) == 0.5


def test_kappa_is_undefined_with_one_run_or_one_outcome_everywhere():
    assert replicates.fleiss_kappa([[R], [N]]) is None and replicates.fleiss_kappa([[R, R], [R, R]]) is None


def test_a_claim_a_run_did_not_record_is_left_out_of_kappa_and_of_the_pairs():
    table = [[R, R, None], [N, N, N]]
    assert replicates.pairwise(table) == 1 and replicates.fleiss_kappa(table) is None   # only N left, all agree


def test_the_score_counts_half_a_partial_and_leaves_out_the_blocked():
    assert replicates.score([R, P, N, B, None]) == 0.5 and replicates.score([B]) is None

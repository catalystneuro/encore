# Yu, Gutnisky, Hires & Svoboda (2016) from CRCNS ssc-7

This entry tests the findings of [Yu et al. (2016)](https://doi.org/10.1038/nn.4412) on
[CRCNS ssc-7](https://doi.org/10.6080/K0T43R01). The data set holds spikes and membrane potential
of VPM units, L4 excitatory neurons and L4 fast-spiking interneurons in mice that localized a pole
with their whiskers. It also holds whisker tracking, touch annotations, licks and optogenetic
trials, and recordings after infraorbital nerve (ION) transection. The notebook streams the data
set's single archive, `data.tar.gz`, once from the public bucket and reduces each NWB file in
memory. It takes about twenty minutes, most of it streaming.

| Claim | Outcome |
|---|---|
| Task performance, touches per trial and reaction time | Partially reproduced |
| VPM baseline rate (5.1 spikes/s, median 3.3) | Partially reproduced |
| VPM touch response (spikes per touch, latency, duration) | Partially reproduced |
| Most VPM neurons increase their rate with whisking (25 of 29) | Reproduced |
| VPM rate rises severalfold with whisking | Reproduced |
| VPM rate is modulated by whisking phase | Reproduced |
| VPM rate and whisking amplitude co-vary across trials | Reproduced |
| Example neuron E No. 1 (rest, threshold, touch PSP, whisking) | Reproduced |
| Example neurons E No. 24 and 32, whisking Vm change | Reproduced |
| L4 E resting Vm, -76 to -45 mV | Reproduced |
| L4 E touch PSP latency and amplitude | Partially reproduced |
| L4 E whisking Vm change, 1.2 mV | Reproduced |
| Touch moves L4 E Vm closer to threshold than whisking | Partially reproduced |
| L4 E effective reversal potentials of touch and whisking | Reproduced |
| Whisking raises L4 E Vm fluctuations above 10 Hz | Reproduced |
| Fig. 3: inhibition at rest and depolarized (two claims) | Blocked: data missing |
| FS baseline rate | Reproduced |
| FS touch PSP | Reproduced |
| FS spikes per touch and latency | Partially reproduced |
| Most FS neurons increase their rate with whisking (23 of 26) | Reproduced |
| FS whisking depolarization | Partially reproduced |
| FS rate doubles with whisking | Reproduced |
| FS phase coupling, single sinusoid or second harmonic | Partially reproduced |
| FS Vm fluctuations above 10 Hz rise in some cells | Reproduced |
| L4 E neurons respond to touch, not to whisking | Not reproduced |
| TRN photoactivation reduces thalamic multiunit activity | Blocked: data missing |
| Thalamic photoinhibition hyperpolarizes L4 E neurons, with its latency | Partially reproduced |
| Thalamic photoinhibition reduces FS activity (4%, 13%, 32%) | Partially reproduced |
| The reduction is dose dependent | Reproduced |
| Rabies tracing labels VPM more than POM | Blocked: data missing |
| After ION cut: performance at chance | Reproduced |
| After ION cut: no L4 E touch PSP | Not reproduced |
| After ION cut: smaller L4 E whisking depolarization | Partially reproduced |
| After ION cut: L4 E phase locking abolished | Reproduced |
| After ION cut: no change of L4 E Vm spectra with whisking | Reproduced |
| After ION cut: no FS touch spikes | Reproduced |
| After ION cut: no FS whisking activation | Reproduced |
| After ION cut: FS phase locking reduced | Reproduced |
| After ION cut: L5 FS neurons still respond to whisking | Blocked: data missing |
| PV suppression changes L4 E responses (Kruskal-Wallis) | Reproduced |
| PV suppression raises L4 E rates | Partially reproduced |
| With PV suppressed, L4 E neurons follow whisking | Reproduced |
| PV suppression and touch-evoked spikes (no mean change) | Not reproduced |
| PV suppression and touch detection (AUC) | Not reproduced |
| AUC groups and their rates | Not reproduced |
| eNpHR inhibits 3 of 4 PV neurons, with its latencies | Partially reproduced |
| PV suppression raises false alarms in most mice | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several outcomes rest on assumptions, recorded in the attempt: which tracked whisker series is the
principal whisker (the files do not say), how the light-onset latency is read, and whether the
first touch of a trial tagged passive enters the touch-detection (AUC) analysis. The data set
mixes time units in its cortical whisker timestamps, and it lacks the thalamic multiunit
recordings, the rabies tracing and the recordings with depolarizing current injection.

# 001754, Knierim, McNaughton and Poe 2000

Two claims reproduced, two not reproduced and three blocked, all on the
dandiset alone. This was the first attempt to need the third round: the
final revision found that the lookup of positions did not drop spikes at
the tracker's "position lost" value, as the claims file requires; with them
dropped, 12 of 25 cells of one rat are spatially selective (0.48 against the
criterion's 0.5), and it proposed moving the main claim from partially to
not reproduced. The third-round verifier checked that the change follows
the criterion and was not chosen for its result (it moves the result against
the claim), and agreed; the record says the call sits on the bound.

The dandiset was converted by CatalystNeuro (catalystneuro/mcnaughton2000-to-nwb),
so its findings are about our own conversion: the two rats' files from the
same flight day hold the same position trace, so whose position it is during
the second rat's sessions cannot be established; position is stored only at
spike times; rate maps cannot be linked to units, because the cell number
was read from old Windows short file names; eight rate maps are copies of
another; units merge per-epoch spike files without saying they are one
neuron; the unit table lacks columns the conversion README lists; and the
description reports theta and ripples, but there is no EEG.

The author's points on the protocol: other summaries of a paper with a
three-sentence abstract as claim sources; "the paper's own test" when the
test cannot be read; a clock check with neither trials nor continuous
annotations; a broken identifier inside the dandiset; one trace shared by
two subjects as a kind of duplicate; and conversion code read in place of
paper code.

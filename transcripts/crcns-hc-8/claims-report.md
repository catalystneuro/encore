I stopped without writing a claims file, because the paper text is missing parts the claims would need. Nothing was written under `claims/crcns-hc-8/`.

**Text read:** `paper/10.3389-fphys.2016.00425.txt`, the version of record (PMC5037237, from Europe PMC full-text XML). It has the main text, the Methods (2.1 to 2.11), the Results, the Discussion and the figure legends. There is no PDF of the paper under `paper/`, only the dataset's own description, and I read that only to see which experiments the dataset holds.

**What is missing:**
1. **The supplement.** The text only points to it ("Click here for additional data file", journal.frontiersin.org/article/10.3389/fphys.2016.00425). Results in the main text depend on its figures:
   - Figure S8 holds the correlation of 0.23 between complexity and susceptibility.
   - Figure S9 holds the correlations of 0.296 and 0.197 between complexity and the size and duration fit ranges.
   - Figure S2 holds the finite-recording-length bias that explains the second complexity peak in the cortical branching model.
   - Figure S1 and Figures S3 to S7 hold the example sub-sampling fits and the example culture power-law fit, shape collapse and complexity analyses.
2. **Equations 1 to 14.** Converting the XML to text dropped all of them. They define the measures the criteria would test:
   - the power laws and the relation between the critical exponents (Eqs. 1 to 4);
   - the shape collapse scaling (Eqs. 5 to 7);
   - entropy, integration and neural complexity (Eqs. 8 to 10);
   - the basic and corrected branching ratios (Eqs. 11 to 13);
   - susceptibility (Eq. 14).
3. **The numbers in Figure 8 and the other result figures.** The critical exponents τ, α and 1/σνz for the cultures, given as mean ± SD, appear only inside the Figure 8 panels. The main finding that the exponents agree with earlier studies rests on them. With no PDF I cannot read them, and the same goes for Figures 7, 9, 10, 11 and 12.

**Code:** the paper names the NCC MATLAB toolbox (Marshall et al., 2016; Timme, 2016) but the text gives no repository link, and the reference list came through empty. I did not read any code.

**Needed to continue:** the publisher's PDF, with its equations and figures, and the Frontiers supplementary file. Once both are under `paper/`, the claims file can be written. That makes 0 claims, 0 quotes, 0 statistics and 0 criteria, and since no claims were drafted, no open method details were named.

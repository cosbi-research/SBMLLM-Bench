<a id='aed88a06-e9eb-4195-a3a7-ba45ae1b522e'></a>

<::logo: Elsevier
NON SOLUS
This logo features a detailed black and white illustration of a tree with a man and a woman standing beneath it, accompanied by the text "NON SOLUS" on a banner.::>

<a id='9c6a944c-cfb7-4fd0-95cb-cc04838d71c4'></a>

Biophysical Chemistry 104 (2003) 573–589

<a id='51c8d519-e67a-4393-a3ba-ff7911429703'></a>

Biophysical
Chemistry

<a id='c9322b4b-792c-4113-a682-7846ca242ab8'></a>

www.elsevier.com/locate/bpc

<a id='c889d1bd-902c-4971-90e1-45328f7f985d'></a>

A kinetic model of the cyclin E/Cdk2 developmental timer in
Xenopus laevis embryos

<a id='58af1b5c-ee68-478c-ad65-28ca59a65d72'></a>

Andrea Ciliberto, Matthew J. Petrus, John J. Tyson, Jill C. Sible*
Biology Department, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061-0406, USA

<a id='50d62c25-9f3f-4518-8115-13808935c9ff'></a>

Received 20 December 2002; received in revised form 10 March 2003; accepted 10 March 2003

<a id='f7b08fdd-3cf1-45cd-9705-7c4fb4417985'></a>

# Abstract

Early cell cycles of _Xenopus laevis_ embryos are characterized by rapid oscillations in the activity of two cyclin-dependent kinases. Cdk1 activity peaks at mitosis, driven by periodic degradation of cyclins A and B. In contrast, Cdk2 activity oscillates twice per cell cycle, despite a constant level of its partner, cyclin E. Cyclin E degrades at a fixed time after fertilization, normally corresponding to the midblastula transition. Based on published data and new experiments, we constructed a mathematical model in which: (1) oscillations in Cdk2 activity depend upon changes in phosphorylation, (2) Cdk2 participates in a negative feedback loop with the inhibitory kinase Wee1; (3) cyclin E is cooperatively removed from the oscillatory system; and (4) removed cyclin E is degraded by a pathway activated by cyclin E/Cdk2 itself. The model's predictions about embryos injected with Xic1, a stoichiometric inhibitor of cyclin E/Cdk2, were experimentally validated.

© 2003 Elsevier Science B.V. All rights reserved.

<a id='7d28ded5-9352-4307-b978-028894a83346'></a>

Keywords: Cyclin E; Cyclin-dependent kinase 2 (Cdk2); Wee1; Xic1; Midblastula transition; Mathematical model

<a id='c1bd94dc-019d-48c0-86e9-adf7e30bb8c5'></a>

## 1. Introduction

The chromosome replication-division cycle of
cell-free extracts derived from *Xenopus laevis* eggs
has been well characterized by rigorous experi-
mentation [1-12] and mathematical modeling
[13-16]. In the egg extract system, the chromo-
some cycle is driven by oscillations in the activity

<a id='47f95d2d-2c89-4d4f-a0f4-29bab62fdd60'></a>

_Abbreviations_: Cdk, cyclin-dependent kinase; MPF, M-phase promoting factor; MBT, midblastula transition; ODE, ordinary differential equation; pf, post-fertilization.
*Corresponding author. Tel.: +1-540-231-1842; fax: +1-540-231-9307.
_E-mail addresses_: siblej@vt.edu (J.C. Sible),
ancilibe@vt.edu (A. Ciliberto),
mapetrus@vt.edu (M.J. Petrus), tyson@vt.edu (J.J. Tyson).

<a id='696f09d1-5bb3-4907-af25-d0f92c010425'></a>

of M-phase promoting factor (MPF), a dimer of a catalytic subunit, Cdk1, and a regulatory subunit, cyclin A1 or B [3]. Oscillations in MPF activity depend upon a negative feedback loop in which active MPF promotes degradation of mitotic cyclins [12,17]. MPF activity is also modulated by inhibitory phosphorylation on threonine 14 and tyrosine 15. These sites are phosphorylated by Wee1 and Myt1 [5,6], and dephosphorylated by Cdc25 [7,8]. The autocatalytic nature of MPF activation [18–20] depends upon positive feedback loops, whereby MPF activates Cdc25 [11,21] and inhibits Wee1 [5].

<a id='a2955853-e45a-4d3c-86d4-3540a66ab9d6'></a>

Cell cycle controls in intact, developing _Xenopus_
embryos present additional experimental and theo-

<a id='ae39a9f6-a1ed-479f-9d83-28b8f2f62dcc'></a>

0301-4622/03/$ - see front matter  2003 Elsevier Science B.V. All rights reserved.
doi:10.1016/S0301-4622(03)00060-7

<!-- PAGE BREAK -->

<a id='3dc77eae-2dca-4958-87e5-b5161d16e1db'></a>

574

<a id='09bcb6d1-7954-47f3-95ae-5d9ca5c3dcf1'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='916d5ce4-95b9-4c0a-acf2-21e35a83fb28'></a>

retical challenges. After fertilization, the egg and
sperm nuclei undergo DNA replication, nuclear
fusion and the first mitotic division. The next 11
embryonic cell cycles are rapid, synchronous oscil-
lations between DNA replication and mitosis, lack-
ing intervening gap phases, cell growth and cell
cycle checkpoints. After the 12th division, the
Xenopus embryo undergoes the midblastula tran-
sition (MBT), when cells become motile, embry-
onic transcription begins and the cell cycle
acquires the gap phases and checkpoints of a
typical somatic cell [22,23].

<a id='60a956fe-ebc5-4be9-aae8-c345129aaf3a'></a>

The mechanisms of 'cell cycle remodeling' [24] are not fully understood, but recent evidence suggests that remodeling depends in part on a maternal developmental timer driven by oscillations in the activity of cyclin E/Cdk2 [25]. During cleavage cycles 2–12 in the frog, the cyclin E level is constant, while cyclin E-associated kinase activity (cyclin E/Cdk2) oscillates twice per cell cycle [25,26]. Cyclin E/Cdk2 activity promotes DNA replication [27,28] and is essential for centrosome duplication [29,30]. At the MBT, maternally supplied cyclin E is degraded [25,26,31,32] and Cdk2 activity declines [25], coincident with remodeling of the cell cycle. Maternal cyclin E mRNA disappears some hours later [32].

<a id='65e5820c-dbfc-4287-8ca9-a76015f12235'></a>

Injection of embryos with Δ34Xic1 (a recombinant, truncated form of the cyclin-dependent kinase (Cdk) inhibitor, Xic1) specifically inhibits cyclin E/Cdk2, causes a 25% increase in interdivision time, and delays both the MBT (zygotic transcription) and the degradation of cyclin E until approximately the correct nucleocytoplasmic ratio [25]. Although this observation suggests that cyclin E degradation is causally related to the MBT, the two events can be dissociated. Cycloheximide treatment (which inhibits protein synthesis) blocks cell division and the MBT, but does not prevent cyclin E degradation. Nor does α-amanitin treatment (which blocks zygotic transcription at the MBT) prevent cyclin E degradation [25]. Furthermore, oscillations in cyclin E/Cdk2 also occur independently of protein synthesis, the nucleocytoplasmic ratio and embryonic transcription [25].

<a id='d4936644-a465-43b0-935e-ec96879d4ea4'></a>

We have built a mathematical model of the cyclin E/Cdk2 developmental timer that describes both the oscillations in Cdk2 activity and the abrupt destruction of cyclin E coincident with the MBT. The model was constructed along the same lines as the Novak-Tyson model of MPF oscilla- tions in frog egg extracts [13], taking into account the similarities and differences between cyclin B/ Cdk1 regulation and cyclin E/Cdk2 regulation. For both Cdk1 and Cdk2, there are no abundant Cdk inhibitors expressed during this time [33]; hence, oscillations are due to either periodic syn- thesis and degradation of cyclin partners, or peri- odic phosphorylation and dephosphorylation of kinase subunits (or both). Pre-MBT oscillations of Cdk1 activity are driven by periodic cyclin deg- radation [34], but pre-MBT oscillations of Cdk2 activity are not [25]. Although early reports indi- cated no periodic tyrosine phosphorylation of either Cdk1 or Cdk2 until the MBT [26,35], subsequent studies with a sensitive antibody have detected periodic tyrosine phosphorylation of a Cdk in pre-MBT *Xenopus* embryos [36]. Further- more, Cdk2 activity is regulated in cell-free egg extracts by such phosphorylation events [37]. Therefore, if oscillations in Cdk2 activity are generated by a negative feedback loop (as for Cdk1), the inhibitory phosphorylation state of Cdk2 (rather than cyclin level) is the likely posi- tion of the negative feedback.

<a id='919b0a9b-b9cf-4952-952a-870bfb3ba22c'></a>

A second important distinction between the
regulation of Cdk1 and Cdk2 activity is the rapid
destruction of cyclin E at the MBT. Because the
only manipulation known to delay the degradation
of cyclin E is to inhibit Cdk2 activity directly
[25], we propose that degradation of cyclin E is
intrinsically dependent on Cdk2 activity.

<a id='52ca6b4f-44d3-4709-8ceb-60b4bfafa6f5'></a>

Based on the experimental literature, we developed a mathematical model to describe the oscillations in cyclin E/Cdk2 activity and the abrupt degradation of cyclin E at the MBT in the intact *Xenopus* embryo. New experiments were performed to help construct the model. The model should provide a framework around which to design future experiments that will specify the details of a revised, second-generation model.

<!-- PAGE BREAK -->

<a id='14d5917c-fd5b-4aa6-9930-3b4d5dc70dc5'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='4ee83601-d5cc-40bf-8bdf-b89d7382af48'></a>

575

<a id='60888f14-e831-48d3-80f6-57b7c3fdf5ec'></a>

## 2. Experimental methods

### 2.1. Maintenance and manipulation of embryos

Eggs from wild-type _Xenopus laevis_ (Xenopus Express) were fertilized in vitro, dejellied in 2% cysteine in 0.1× MMR (0.5 mM HEPES, pH 7.8, 10 mM NaCl, 0.2 mM KCl, 0.1 mM MgSO4, 0.2 mM CaCl2, 0.01 mM EDTA) and maintained in 0.1× MMR. Embryos were collected at stages spanning the MBT and staged according to Nieuwkoop and Faber [38]. In some experiments, fertilized eggs were injected with indicated amounts of glutathione _S_-transferase (GST)-tagged Xic1-C or GST-tagged Δ34Xic1 protein dissolved in Xic1 buffer (20 mM HEPES, pH 7.5, 88 mM NaCl, 20 mM β-mercaptoethanol, 7.5 mM MgCl2, 5% glycerol) at a concentration of 0.08–0.33 mg/ml. As described by Su et al. [39], Xic1-C contains amino acids 97–210 and Δ34Xic1 contains amino acids 25–210 of the Xic1 protein. The Xic1 proteins were gifts of James Maller (Howard Hughes Medical Institute, University of Colorado Health Sciences Center). Microinjected embryos were maintained in 5% Ficoll in 0.1× MMR, and snap-frozen at the time points indicated. Some embryos were also injected with 50 ng of α-amanitin dissolved in H2O. In some experiments, fertilized eggs were injected with buffer or 15 ng of mRNA encoding luciferase or XChk1 (transcribed in vitro using the mMessage mMachine kit from Ambion), as described elsewhere [40].

<a id='ca9bd239-c94c-49d3-9f9d-c2ba83f31b95'></a>

2.2. Immunoblotting

Embryos were collected at the times indicated,
snap-frozen on dry ice and homogenized in EB
buffer (20–30 mM HEPES, pH 7.5, 15 mM
MgCl2, 20 mM EGTA, 1 mM dithiothreitol, 1 mM
sodium vanadate, 1 mM microcystin, 1 mM phenyl-
methylsulfonyl fluoride, and 3 µg/ml each leupep-
tin, pepstatin and chymostatin, with or without 80
mM β-glycerophosphate and 50 mM sodium flu-
oride). Embryo lysates were resolved by sodium
dodecyl sulfate-polyacrylamide gel electrophoresis
(SDS-PAGE), transferred to nitrocellulose mem-
branes, and hybridized with antibodies, as previ-

<a id='8753ab6c-1df9-429d-93d9-f8f46381dc1c'></a>

ously described [40,41]. The cyclin E antibody
was purified from serum provided by Rebecca
Hartley (University of New Mexico Health Sci-
ences Center). Xic1 antibodies were generously
provided by James Maller (Howard Hughes Med-
ical Institute, University of Colorado Health Sci-
ences Center). To visualize immunoreactive
proteins, a horseradish peroxidase-conjugated sec-
ondary antibody was hybridized, and chemilumi-
nescence from the secondary antibody was
detected with the ECL Plus (Amersham) kit.

<a id='1fd7ab13-99c0-4d2d-9e6c-266600d9adb3'></a>

2.3. Immunoprecipitation and kinase assays of cyclin/Cdk complexes

Embryos injected at the one-cell stage with 5 ng of Xic-C or Δ34Xic1 were collected at the time indicated, and antibodies against cyclin B or cyclin E were used to immunoprecipitate cyclin B/Cdk1 or cyclin E/Cdk2 complexes, respectively, as described by Kappas et al. [40]. Cyclin antibodies were provided by James Maller (Howard Hughes Institute, University of Colorado Health Sciences Center).

<a id='6026d1c9-5b3b-4b88-9e5a-3113e221bcd2'></a>

3. Mathematical modeling and computational simulation

Mathematical models of hypothetical molecular mechanisms for regulation of cyclin E/Cdk2 activity were constructed by translating a mechanism into a set of ordinary differential equations (ODEs) by standard principles of biochemical kinetics [42]. The ODEs were then provided as input to XPP-AUT, a simulation and analysis software system, freely downloadable from http://www.math.pitt.edu/~bard/xpp/xpp.html. XPP runs on the UNIX operating system. Parameter values were chosen by trial and error, to fit the basic phenomenological properties of the control system (rapid fluctuations in cyclin E/Cdk2 activity followed by abrupt degradation of cyclin E).

<a id='d3c888d1-3920-4f23-b2fb-6d881430524e'></a>

## 4. Results

### 4.1. Key assumptions

Based on the experimental evidence summarized in Section 1, a set of assumptions upon which the

<!-- PAGE BREAK -->

<a id='c63e93f1-e7ed-4292-ab95-98807f0d49cb'></a>

576

<a id='c849b4b9-19cd-4ca7-85b9-7b7caccbc582'></a>

A. Ciliberto et al. / *Biophysical Chemistry* 104 (2003) 573–589

<a id='f421125a-27db-4e60-9882-8a47e7530402'></a>

mathematical model would be based was devel-
oped (Table 1). Some assumptions are well
grounded in the experimental literature (assump-
tions 1–3), others remain to be tested (assumption
4) and several (assumptions 5–7) were tested by
us experimentally, as described below.

<a id='f24d344f-7ac1-4b4f-a765-c0784ba85425'></a>

### 4.1.1. Reagents that inhibit Cdk2 delay the degradation of cyclin E
A fundamental assumption of our working model is that degradation of cyclin E at the MBT results from a cooperative transition in cyclin E/Cdk2 forms. This assumption is based upon published studies demonstrating that cyclin E is degraded at a fixed time post-fertilization, independent of protein synthesis (hence, independent of Cdk1 activity, which requires continued synthesis of mitotic cyclins A and B), cell number, the nucleocytoplasmic ratio and zygotic transcription [25,32]. Furthermore, the only manipulation known to alter the timing of cyclin E degradation is microinjection of A34Xic1, a recombinant protein that specifically inhibits Cdk2 but not Cdk1 activity [25]. Because A34Xic1 delays the degradation of cyclin E, it seemed likely that the timing mechanism for cyclin E degradation depends upon cyclin E/Cdk2 activity itself.

<a id='eda9e5ad-fc94-4d67-a474-41f3dba3fbf7'></a>

If this assumption were correct, then other rea-
gents that interfere with cyclin E/Cdk2 activity
should also block or delay the degradation of
cyclin E. Expression of exogenous XChk1 in
Xenopus embryos inhibits both Cdk1 and Cdk2
activity [40]; therefore, expression of XChk1
should also block or delay the degradation of
cyclin E. To test this prediction, embryos were
injected with 15 ng of mRNA encoding FLAG-
tagged XChk1. Negative control embryos were

<a id='4416ab4f-29d4-433c-a590-db25b6f1466b'></a>

<::Western blot showing two panels. The top panel detects FLAG protein and the bottom panel detects cyclin E. The left vertical axis shows molecular weight markers: 111, 77, 48, 34 for the top panel, and 77, 48, 34 for the bottom panel. The horizontal axis at the top indicates 'hours pf:' 4, 5, 7, 9 under 'buffer' treatment, and 4, 5, 7, 9 under 'XCHK mRNA' treatment. In the FLAG panel (top), a protein band around 48 kDa is visible, increasing in intensity from 5 to 9 hours in the 'XCHK mRNA' condition, with no detectable band in the 'buffer' condition. In the cyclin E panel (bottom), protein bands are visible around 48 kDa across all 'buffer' and 'XCHK mRNA' conditions and time points. The entire blot is labeled 'MBT' diagonally at the bottom left.: Western blot::>

<a id='e1b5b12f-95c1-4a50-b818-dcc7c038953a'></a>

Fig. 1. Expression of XChk1 delays the degradation of cyclin E in *Xenopus* embryos. Embryos were injected with buffer or 15 ng of mRNA encoding XChk1. Embryos were collected at the time points indicated and analyzed for cyclin E protein content. The migration of molecular weight standards in kDa is indicated. In other experiments, control embryos were injected with mRNA encoding luciferase, and the delay in cyclin E degradation was shown to be a specific effect of XChk1 (data not shown).

<a id='290da1cb-7eab-44ef-8a41-77cd85adc00c'></a>

injected with buffer or 15 ng of mRNA encoding
FLAG-tagged luciferase. Embryos were collected
at the times indicated and analyzed for cyclin E
content by immunoblotting (Fig. 1). Analogous to
embryos injected with △34Xic1, cyclin E degra-
dation was delayed in embryos overexpressing
XChk1 compared to both buffer (Fig. 1) and
luciferase controls (not shown), supporting the
hypothesis that timing of cyclin E degradation
depends directly on Cdk2 activity.

<a id='8a838317-2337-4638-9186-21f7681c4845'></a>

Table 1
Key assumptions of the cyclin E/Cdk2 kinetic model
<table id="3-1">
<tr><td id="3-2">1</td><td id="3-3">Constant level of cyclin E</td><td id="3-4">[25,26,31,32]</td></tr>
<tr><td id="3-5">2</td><td id="3-6">No abundant CKI inhibitor</td><td id="3-7">[33,50]</td></tr>
<tr><td id="3-8">3</td><td id="3-9">Regulation of Cdk2 activity by phosphorylation</td><td id="3-a">[37,40]</td></tr>
<tr><td id="3-b">4</td><td id="3-c">Negative feedback loop in Cdk2 oscillations</td><td id="3-d">To be tested</td></tr>
<tr><td id="3-e">5</td><td id="3-f">Timing of cyclin E degradation linked to Cdk2 activity</td><td id="3-g">[25], Fig. 1</td></tr>
<tr><td id="3-h">6</td><td id="3-i">No return of Cdk2 activity in Xic-injected embryos</td><td id="3-j">Fig. 2</td></tr>
<tr><td id="3-k">7</td><td id="3-l">Degradation of cyclin E independent of transcription</td><td id="3-m">[25], Fig. 3</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='5f8e9824-bd27-4b83-8a9e-2c13d5bc27e7'></a>

A. Ciliberto et al. / *Biophysical Chemistry* 104 (2003) 573–589

<a id='da0359ef-3291-48be-96b7-4e709af6fee0'></a>

577

<a id='ab46917d-33dc-4688-a348-5b679e0ebc2f'></a>

<::transcription of the content : chart::>
<::chart::>
Fig. 2. Cyclin E degradation in Δ34Xic1-treated embryos does not depend upon transient cyclin E/Cdk2 activity. Embryos microinjected with 5 ng of Xic1-C or Δ34Xic1 were collected at the times indicated, cyclin E/Cdk2 was immunoprecipitated and immunoprecipitates were analyzed for histone H1 kinase activity. cpm, counts per minute ³²P incorporated into histone H1. Values plotted represent raw cpm—background cpm on gel (1209 cpm). Cyclin B/Cdk1 immunoprecipitates indicated no inhibition of Cdk1 by Δ34Xic1 (not shown).

**Line chart showing incorporation of ³²P (cpm) over hours pf.**

**Y-axis:** incorporation of ³²P (cpm), ranging from 0 to 14000 in increments of 2000.

**X-axis:** hours pf, with points at 4, 6, 8, 10, and 13.

**Legend:**
- `Xic-C`: represented by black diamonds connected by a dashed line.
- `Δ34Xic`: represented by black squares connected by a solid line.

**Data points:**
- **Xic-C line:**
  - At 4 hours pf: approx. 13000 cpm
  - At 6 hours pf: approx. 8000 cpm
  - At 8 hours pf: approx. 2500 cpm
  - At 10 hours pf: approx. 2000 cpm
  - At 13 hours pf: approx. 1500 cpm

- **Δ34Xic line:**
  - At 4 hours pf: approx. 2000 cpm
  - At 6 hours pf: approx. 2500 cpm
  - At 8 hours pf: approx. 2800 cpm
  - At 10 hours pf: approx. 3000 cpm
  - At 13 hours pf: approx. 2000 cpm
<::/chart::>

<a id='d8f478b1-8451-49e4-b947-43e5d9da4170'></a>

_4.1.2. Cyclin E degradation in Xic1-treated embry-os does not depend upon transient cyclin E/Cdk2 activity_

<a id='908fc22c-bdeb-4fa1-94e6-f50fbcabde2e'></a>

When embryos are microinjected with 5 ng of
Δ34Xic1, cyclin E/Cdk2 activity is inhibited by
more than 90% without inhibition of Cdk1 activity
[25]. Intuitively, we would predict that cyclin E
degradation would be blocked indefinitely (or until
embryos died by necrosis) in Δ34Xic1-injected
embryos. However, the degradation of cyclin E
does occur, only several hours delayed, when

<a id='d0749a69-5f67-4ad7-a96c-25da9bf6c5a2'></a>

embryos have reached the nucleocytoplasmic ratio
of the MBT [25]. This observation challenges the
hypothesis that cyclin E degradation is directly
linked to cyclin E/Cdk2 activity.

<a id='44f2d1c7-c1be-4be3-baf2-ec7d7a04f249'></a>

One possible explanation for the eventual degradation of cyclin E in Δ34Xic1-injected embryos is that cyclin E/Cdk2 activity resumes transiently, prior to the degradation of cyclin E, at approximately 9 h post-fertilization (pf). This scenario played a central role in a preliminary mathematical model that simulated the delay in degradation of cyclin E in Δ34Xic1-injected embryos. However, kinase assays performed on embryos injected with Δ34Xic1 detected no transient peak of Cdk2 activity (Fig. 2), even when samples were collected at 30-min intervals (not shown), ruling out this particular model.

<a id='b72f37fc-d5c1-4b53-bf8a-71776f2ee7c2'></a>

4.1.3. _Cyclin E degradation in Xic1-treated embryos does not depend upon zygotic transcription_

It could be that degradation of cyclin E in embryos injected with Δ34Xic1 is initiated by zygotic transcription at the MBT, since transcription initiates coincident with cyclin E degradation in Δ34Xic1-injected embryos [25]. To determine whether a product of zygotic transcription turned on degradation of maternal cyclin E, independent of cyclin E/Cdk2 activity, embryos were injected with H₂O, α-amanitin (an inhibitor of transcription), Δ34Xic1, or a combination of α-amanitin and Δ34Xic1 (Fig. 3). In embryos injected with H₂O or α-amanitin, cyclin E disappeared between

<a id='e8f26a84-6f80-4ec6-908f-d51a9aa6de08'></a>

<::Immunoblot showing cyclin E protein levels. The blot is organized into four main conditions for injected compounds: H2O, α-amanitin, Δ34Xic, and α-amanitin + Δ34Xic. For each condition, samples were taken at hours pf (post-fertilization): 5, 7, 10, and 15. On the left, molecular weight standards are indicated at 68.8 kDa and 52.5 kDa. An arrow on the right points to the detected cyclin E band. Below the blot, developmental stages are indicated: MBT and gastrulation. The blot shows bands for cyclin E protein varying across conditions and time points. Fig. 3. Zygotic transcription is not required for degradation of cyclin E. Embryos were injected at the one-cell stage with H₂O, 50 ng of α-amanitin, 5 ng of Δ34Xic1, or 50 ng of α-amanitin and 5 ng of Δ34Xic1. Embryos were collected at the indicated times pf and analyzed by immunoblotting for steady-state level of cyclin E protein. The migration of molecular weight standards in kDa is indicated.: figure::>

<!-- PAGE BREAK -->

<a id='0c743dbe-ff2a-4c23-a7f7-14c803bc6118'></a>

578

<a id='f31e9db1-f6d5-4934-afd4-a10c13247032'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='797792d0-8da9-41c4-8047-42f97113f2eb'></a>

5 and 7 h pf, consistent with previous reports that degradation of maternal cyclin E at the MBT does not depend on transcription [25,32]. As predicted [25], degradation of cyclin E was delayed in embryos injected with A34Xic1 and was complete by 10 h pf. In embryos injected with both α-amanitin and A34Xic1, cyclin E was degraded at the same time as in embryos injected with A34Xic1 alone, ruling out the possibility of redundant degradation mechanisms, one dependent upon transcription and the other upon cyclin E/Cdk2 activity. These results indicate that transcription at the MBT is not required for the eventual degradation of cyclin E in embryos lacking cyclin E/ Cdk2 activity.

<a id='94deb9db-7313-4661-9668-1c90a5288fe7'></a>

4.2. *Kinetic model of the cyclin E/Cdk2 developmental timer*

<a id='b4f01f2b-f770-481b-93ff-e0f494d70034'></a>

Based on the information summarized in Section
1 and the new data presented in Figs. 1–3, a
working model of the cyclin E/Cdk2 control
system was developed (Fig. 4). The model is
composed of three modules: a negative feedback
oscillator, a positive feedback switch and an irre-
versibly activated pathway for cyclin E
degradation.

<a id='971a755d-a9a5-4c8b-8d92-6fef40c8e69e'></a>

4.2.1. *Negative feedback oscillator*
A maternal store of cyclin E combines with free Cdk2 monomers to form active cyclin E/Cdk2 dimers. In the model, we assume cyclin E/Cdk2 dimers can be transformed between an inactive, phosphorylated form (PCdk2:CycE) and an active, non-phosphorylated form (Cdk2:CycE) by the action of a kinase, Wee1, and a phosphatase, Cdc25A. This assumption is based on evidence that Cdk2 is regulated by tyrosine phosphorylation [37,40]. For simplicity, we assume that Cdc25A is present at constant activity in the early embryo, and that Wee1 is periodically activated by cyclin E/Cdk2, indirectly through the action of a hypothetical kinase, Kin. (Cdc25C was not included in the model because dominant-negative Cdc25C does not affect cell cycle length in embryos [36].) In the model, Kin phosphorylates and inactivates Wee1, and cyclin E/Cdk2 phosphorylates and inactivates Kin. These interactions create a delayed negative feedback loop, consisting of three inacti-

<a id='9f9ebf69-de38-4970-a61a-2f676fccc04d'></a>

<::flowchart: Fig. 4. A theoretical molecular mechanism of the cyclin E/Cdk2 developmental timer. The diagram illustrates the interactions of Cyclin E/Cdk2 with regulatory proteins and its degradation pathway. The oscillatory subsystem involves active Cyclin E/Cdk2 (labeled "cyc E Cdk2"), which can be phosphorylated to P-Cyc E/Cdk2 ("P - cyc E Cdk2"). Cdc25A converts P-Cyc E/Cdk2 back to active Cyc E/Cdk2. Wee1, in both its unphosphorylated and phosphorylated forms ("Wee1" and "Wee1 - P"), inhibits the active Cyc E/Cdk2. Wee1 and Wee1-P interconvert. In the negative feedback loop, active Cyc E/Cdk2 activates Kinase ("Kin"). Kinase ("Kin") can be phosphorylated to Kin-P ("Kin - P"), and they interconvert. Kinase ("Kin") activates Wee1, creating a time lag in the negative feedback loop. For removal and degradation, active Cyc E/Cdk2 enters a "hatched box" mechanism for removal from the oscillatory subsystem. This removal step is cooperative, meaning the more Cyc E/Cdk2 is bound to the hatched box, the faster the association reaction. From the hatched box, Cyc E/Cdk2 is broken down into its components (Cdk2 and fragmented parts, represented by small dots, and a separate hatched box). The 'removed' form of Cyc E/Cdk2 (from the hatched box) activates the degradation system ("Deg"). The 'Deg' system itself can exist in an inactive or active form, indicated by two circular shapes labeled 'Deg', one with a segmented interior.::>

<a id='6fef3cd3-7a32-40b4-bd56-9e245d834a9b'></a>

vating phosphorylation steps in sequence (Cdk2-Kin-Wee1-|Cdk2). (A delayed feedback in which Kin activates Cdc25A would be an alter-native possibility.) The parameters in the model are adjusted to create limit cycle oscillations with a period of approximately 15 min (two peaks per mitotic cycle). Because a two-component negative feedback loop (Cdk2- Weel-|Cdk2) cannot oscillate [43], we are compelled to introduce the hypothetical kinase (as the simplest case of some process that provides a delay between the actions of Cdk2 and Weel).

<a id='53afe6f3-8afb-4e04-ae68-fd81f28ffdf1'></a>

4.2.2. *Positive feedback switch*
To model the abrupt degradation of cyclin E at
approximately 7 h pf, it is proposed that cyclin E/

<!-- PAGE BREAK -->

<a id='e1bae09b-3088-4d0a-b33d-fd6547423d1f'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='7ec6febf-ddf5-4e53-b419-4e3a48a96a97'></a>

579

<a id='6fdf4d7e-05d8-40d9-9fe7-eb1e8e6d3361'></a>

Cdk2 is removed from the oscillatory subsystem in a cooperative fashion through a positive feed-back loop. Subsequently, the removed form of cyclin E is degraded, probably by the SCF/ proteasome pathway. 'Removed' cyclin E/Cdk2 could correspond to a change in phosphorylation state, localization or some other property of cyclin E. Qualitatively, it is predicted that, during the first 7 h of embryonic development, most cyclin E will cycle between active (unphosphorylated) and inac- tive (Cdk2-phosphorylated) forms. During these oscillations, an increasing fraction of cyclin E/ Cdk2 dimers is removed from the oscillating forms, eventually stimulating rapid, cooperative (autocatalytic) removal of cyclin E/Cdk2, which quenches the oscillation.

<a id='43366bee-0b01-4811-888f-9ab5aac4270f'></a>

### 4.2.3. Cyclin E degradation
After a further delay, the cyclin E degradation machinery ('Deg') activates, and the whole removed pool of cyclin E is degraded. We suppose that Deg is activated by the unphosphorylated form of removed cyclin E/Cdk2 dimers (Cdk2:CycErem) and that only removed cyclin E is targeted by Deg. Furthermore, the concentration of Cdk2:CycErem must exceed a certain threshold [Table 2, θ in Eq. (7)] before it can activate Deg. As cyclin E is destroyed, we presume that Deg remains active.

<a id='484866d7-4a56-4e86-b266-12093f6b8778'></a>

4.2.4. Effect of Δ34Xic1
We assume that (1) Xic1 binds strongly to all forms of cyclin E/Cdk2 and blocks any catalytic activity they may have; nonetheless, (2) Xic1 binding does not interfere with removal of cyclin E/Cdk2. Furthermore, we assume that Xic1 bound to removed forms of cyclin E/Cdk2 is slowly degraded, possibly in association with chromatin [44–46]. As Xic1 is degraded, [Cdk2:CycErem] increases and subsequently activates cyclin E degradation. Under these assumptions, Xic1 injections are expected to quench oscillations of cyclin E/Cdk2 activity and to delay (but not eliminate) cyclin E degradation.

<a id='64a027e2-c335-418b-a073-e019a499b629'></a>

### 4.2.5. Further assumptions
The removed forms of cyclin E/Cdk2 are not subject to phosphorylation and dephosphorylation by Wee1 and Cdc25 and do not phosphorylate

<a id='1a358ecb-c3d3-47f6-8033-ffa8b532d179'></a>

Kin. These assumptions make the model slightly
easier to understand, but they are not necessary.
Models in which these assumptions are not made
behave very similarly to the model simulated here
(not shown).

<a id='d11879e5-0e38-4323-8778-02862820d14c'></a>

4.2.6. The model
A mathematical model (the differential equa-
tions in Table 2) can be derived from the molecular
wiring diagram (Fig. 4) using standard rate laws
of biochemical kinetics. Basal parameter values
are proposed in Table 3. These values were chosen
to reproduce the basic quantitative characteristics
of the cyclin E/Cdk2 timer in normal frog embry-
os. We assume that, at t=0 (fertilization, or shortly
thereafter), the cyclin E/Cdk2 oscillator is in full
swing and no cyclin E is removed from the
oscillatory system.

<a id='86357146-4928-40fe-918b-b3100a6c2984'></a>

4.3. *Numerical simulations and experimental validation: testing the model*

<a id='b503f393-1abf-4aa8-a33d-18a10bc311f4'></a>

4.3.1. _The model reproduces the fundamental fea-tures of the cyclin E/Cdk2 timer_

Fig. 5 presents a numerical solution of the kinetic equations (Table 2) using the basal param-eter values proposed for unperturbed embryos (Table 3). The model reproduces the fundamental observations driving this study: (1) cyclin E is a stable protein at first and then rapidly degraded at the MBT [25,32]; and (2) cyclin E/Cdk2 activity oscillates twice per cell cycle before the MBT [25] (Fig. 5a). We did not attempt to model cycle 1, which is longer than cycles 2–12 and involves cyclin E degradation [26].

<a id='999e767a-9489-45c6-b9fa-96bd9564af9b'></a>

An appreciation of the regulatory mechanisms behind the oscillations in kinase activity and the abrupt degradation of cyclin E unfolds from graphing the concentrations of the four forms of cyclin E/Cdk2 over time (Fig. 5b). Oscillations in cyclin E/Cdk2 activity prior to the MBT derive from the periodic phosphorylation and dephosphorylation of Cdk2, as a consequence of the negative feedback loop with Wee1. As removed dimers accumulate, Deg is activated and removed cyclin E is degraded.

<a id='b71220dd-1ca8-4b95-b1de-656304ef682a'></a>

Because no steps in the model (Fig. 4) involve
protein synthesis, the model is consistent with the
fact that oscillations in cyclin E/Cdk2 activity
[25] and disappearance of cyclin E at a fixed time

<!-- PAGE BREAK -->

<a id='52c03be0-8c39-4588-8e82-96952dd59d0f'></a>

580 A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='c73c8c58-d97b-44fb-bf8c-abceff1b3d9c'></a>

Table 2
Differential equations describing the model in Fig. 3

1
d/dt [Cdk2:CycE] = -k_wee[Wee1*][Cdk2:CycE] + k_25A[PCdk2:CycE] - k_onΦ[Cdk2:CycE]
+ k_off[Cdk2:CycE^rem] - k_assoc[Xic][Cdk2:CycE] + k_dissoc[Xic:Cdk2:CycE]

2
d/dt [PCdk2:CycE] = +k_wee[Wee1*][Cdk2:CycE] - k_25A[PCdk2:CycE] - k_onΦ[PCdk2:CycE]
+ k_off[PCdk2:CycE^rem] - k_assoc[Xic][PCdk2:CycE] + k_dissoc[Xic:PCdk2:CycE]

3
d/dt [Wee1*] = + J_wact + k_wact([Wee1_total] - [Wee1*]) / (J_wact + [Wee1*]) - k_winact[Kin*][Wee1*] / (J_winact + [Wee1*])

4
d/dt [Kin*] = + J_iact + k_iact(1 - [Kin*]) / (J_iact + [Kin*]) - k_iinact[Cdk2:CycE][Kin*] / (J_iinact + [Kin*])

5
d/dt [Cdk2:CycE^rem] = +k_onΦ[Cdk2:CycE] - k_off[Cdk2:CycE^rem] - k_edeg[Deg][Cdk2:CycE^rem]
+ k_xdeg[Xic:Cdk2:CycE^rem] - k_assoc[Xic][Cdk2:CycE^rem] + k_dissoc[Xic:Cdk2:CycE^rem]

6
d/dt [PCdk2:CycE^rem] = +k_onΦ[PCdk2:CycE] - k_off[PCdk2:CycE^rem]
- k_edeg[Deg][PCdk2:CycE^rem] + k_xdeg[Xic:PCdk2:CycE^rem]
- k_assoc[Xic][PCdk2:CycE^rem] + k_dissoc[Xic:PCdk2:CycE^rem]

7
d/dt [Deg*] = k_dactHeav([Cdk2:CycE^rem] - 0)

8
d/dt [Xic] = -k_assoc[Xic]([Cdk2:CycE] + [PCdk2:CycE] + [Cdk2:CycE^rem] + [PCdk2:CycE^rem])
+ k_dissoc([Xic:Cdk2:CycE] + [Xic:PCdk2:CycE] + [Xic:Cdk2:CycE^rem] + [Xic:PCdk2:CycE^rem])

9
d/dt [Xic:Cdk2:CycE] = +k_assoc[Xic][Cdk2:CycE] - k_dissoc[Xic:Cdk2:CycE]
- k_onΦ[Xic:Cdk2:CycE] + k_off[Xic:Cdk2:CycE^rem]
- k_wee[Wee1*][Xic:Cdk2:CycE] + k_25A[Xic:PCdk2:CycE]

10
d/dt [Xic:PCdk2:CycE] = +k_assoc[Xic][PCdk2:CycE] - k_dissoc[Xic:PCdk2:CycE]
- k_onΦ[Xic:PCdk2:CycE] + k_off[Xic:PCdk2:CycE^rem]
+ k_wee[Wee1*][Xic:Cdk2:CycE] - k_25A[Xic:PCdk2:CycE]

11
d/dt [Xic:Cdk2:CycE^rem] = +k_assoc[Xic][Cdk2:CycE^rem] - k_dissoc[Xic:Cdk2:CycE^rem]
+ k_onΦ[Xic:Cdk2:CycE] - k_off[Xic:Cdk2:CycE^rem]
- k_edeg[Deg][Xic:Cdk2:CycE^rem] - k_xdeg[Xic:Cdk2:CycE^rem]

12
d/dt [Xic:PCdk2:CycE^rem] = +k_assoc[Xic][PCdk2:CycE^rem] - k_dissoc[Xic:PCdk2:CycE^rem]
+ k_onΦ[Xic:PCdk2:CycE] - k_off[Xic:PCdk2:CycE^rem]
- k_edeg[Deg][Xic:PCdk2:CycE^rem] - k_xdeg[Xic:PCdk2:CycE^rem]

13
d/dt [Xic^rem] = +k_edeg[Deg][Xic:Cdk2:CycE^rem] + k_edeg[Deg][Xic:PCdk2:CycE^rem] - k_xdeg[Xic^rem]

<a id='c5b4f61d-0050-4c8f-971a-56a0d405eea2'></a>

All concentration variables are expressed in arbitrary units, i.e. they are dimensionless numbers. Hence, all rate constants (_k_ values) have units time⁻¹. In the text, 1 AU of Xic and CycE concentration is estimated to be approximately 33 nM. Φ = _ε_ + [Pool]ⁿ / _L_ⁿ + [Pool]ⁿ.
Heav(_x_) = {0, if _x_<0; 1, if _x_≥0}.
[Pool] = [Cdk2:CycErem] + [PCdk2:CycErem] + [Xic:Cdk2:CycErem] + [Xic:PCdk2:CycErem]. Φ is a Hill function describing the cooperativity of Cdk2:CycE removal. It depends on [Pool], the 'total pool' of removed cyclin E. Heav(_x_) is the Heaviside function, a common mathematical expression for a switch. _θ_ is the threshold Cdk2 activity for turning on the switch. The activation kinetics of Wee1 and Kin are assumed to be zero-order ultrasensitive switches [51].

<!-- PAGE BREAK -->

<a id='fb93f937-eede-4a29-adb1-dc33a16539d9'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='aad8ef7b-af88-4455-9aeb-2550b7d172bb'></a>

581

<a id='063f6a7a-c421-4401-b203-d251fc24b52b'></a>

Table 3
Basal parameter values for the differential equations in Table 1

<a id='6e3fc6b3-36c9-4328-ba3c-6dce488a5de5'></a>

Rate constants (min⁻¹)
kwee = 1.5, k25A = 0.1, kon = 0.02, koff = 0.0001, kassoc = 0.1, kdissoc = 0.001, kwact = 0.75, kwinact = 1.5,
kiact = 0.15, kiinact = 0.6, kedeg = 0.017, kxdeg = 0.01, kdact = 0.023

Other constants (dimensionless)
Jwact = 0.01, Jwinact = 0.01, Jiact = 0.01, Jiinact = 0.01, θ = 0.3, ε = 0.001, L = 0.4, n = 4, [Wee1total] = 8

<a id='9041afcc-8801-4d46-96e2-4bcc159b8080'></a>

Initial concentrations (arbitrary units)
[Cdk2:CycE]=0.06, [PCdk2:CycE]=0.94, [Wee1*]=1.02, [Kin*]=0.60, [Deg*] = 0,
[all 'removed' forms] =0, [all Xic-bound forms] =0, [Xic] = adjustable

<a id='8e041d20-669f-4ff6-a067-064d2cdc3e69'></a>

post-fertilization [25,32] occur, even when embry-
os are treated with cycloheximide to block protein
synthesis, a critical constraint from the experimen-
tal literature [25].

<a id='2239af46-121e-4b99-abff-99f5e03b3768'></a>

### 4.3.2. Exogenous Δ34Xic1 is degraded prior to the disappearance of cyclin E
A major challenge in developing the model was the experimental result that embryos microinjected with Δ34Xic1 eventually degrade cyclin E, with a delay of only several hours [25]. If cyclin E degradation were intrinsically linked to cyclin E/Cdk2 activity as we assume, and if Δ34Xic1 inhibits cyclin E/Cdk2 activity by more than 90% [25], then cyclin E levels might persist indefinitely in Δ34Xic1-injected embryos. That this is not the

<a id='b776a01c-132b-4f4d-bad6-3a91adcb1fd1'></a>

case suggests that Xic1 is eventually lost from the treated embryos. In the model, we assume that Xic1 bound to the removed forms of cyclin E/ Cdk2 is subject to steady degradation. Simulations show that this reasonable assumption is sufficient to account for Xic1 and cyclin E fates in treated embryos (Fig. 6). To simulate the effect of inject- ing Δ34Xic1, the initial concentration of Xic1 in the model was set to 3. {In simulations of unper- turbed embryos (Fig. 5), [total Xic1]=0, based on the data of [33,50].} Simulations indicate that most cyclin E/Cdk2 associates with Xic1, and this complex gradually shifts to the pool of removed forms, peaking approximately 7 h pf (Fig. 6a). Once in the removed pool, Xic1 is degraded there, consistent with experiments in egg extracts

<a id='0145c228-8e4d-4e7d-9b15-3aa9d4346d60'></a>

<::chart::>
(a) Plot showing [Deg*], [Cdk2:CycE], and [CycE Tot] over time. The y-axis ranges from 0 to 1.2. The x-axis is "Hours post fertilization" and ranges from 0 to 16. The [Deg*] curve is a dashed line that is high, drops sharply around 6 hours, and then remains low. The [CycE Tot] curve is a dashed-dotted line that is high, drops sharply around 6 hours, and then remains low. The [Cdk2:CycE] curve is a solid line showing rapid oscillations initially, decreasing in amplitude and frequency, and then dropping to zero around 6 hours.
(b) Plot showing [PCdk2:CycE], [Cdk2:CycE], [Cdk2:CycErem], and [PCdk2:CycErem] over time. The y-axis ranges from 0 to 1. The x-axis is "Hours post fertilization" and ranges from 0 to 16. The legend indicates:
- [PCdk2:CycE]: dotted line
- [Cdk2:CycE]: solid line
- [Cdk2:CycErem]: dashed-dotted line
- [PCdk2:CycErem]: dashed line
All four curves show initial oscillations or high levels, followed by a decrease to near zero after approximately 6-8 hours.
Fig. 5. The mathematical model is consistent with the dynamics observed for cyclin E/Cdk2 in normal frog embryos. (a) Numerical simulation of the equations in Table 2, given the parameter values in Table 3. The control system exhibits rapid oscillations in Cdk2 activity (period approx. 15 min) followed by abrupt degradation of cyclin E at approximately 6 h pf. (b) The four forms of cyclin E/Cdk2.
<::>

<!-- PAGE BREAK -->

<a id='0a5d1ee7-a972-46cf-b7b0-e4892cf10b07'></a>

582

<a id='7e633fcd-6ef9-4c28-ba88-76f4675832b2'></a>

A. Ciliberto et al. / *Biophysical Chemistry* 104 (2003) 573–589

<a id='6b61d5a0-5d69-452a-abb7-7ac4e4e3676e'></a>

<::(a) A line graph titled "Hours post fertilization" on the x-axis, ranging from 0 to 16, and an unlabeled y-axis ranging from 0 to 1. The graph shows the concentration of four different components over time:1. A dashed-dotted line represents "[Cdk2:CycE:Xic1]", starting at a high concentration (around 0.8) and decreasing over time.2. A dashed line represents "[Cdk2:CycErem:Xic1]", starting at a low concentration, peaking around 0.7 at approximately 7 hours, and then decreasing.3. A dotted line represents "[Cdk2:CycE]", remaining at a very low concentration for the entire duration, with a slight peak around 0.1 at approximately 5 hours.4. A dashed-dotted line represents "[Xic1rem]", starting at a low concentration, peaking around 0.2 at approximately 10 hours, and then decreasing.: chart::>

<a id='9bb45c47-6166-4fbe-b9f9-32f6ec39ecd9'></a>

(b)
<::Line graph showing concentration over time. The x-axis is labeled "Hours post fertilization" and ranges from 0 to 16. The y-axis is unlabeled and ranges from 0 to 3.
Three lines are plotted:
- A solid line labeled "[Xic1]" starts at approximately 2, decreases gradually, then sharply, reaching near 0 by 10 hours.
- A dashed line labeled "[Cdk2:CycErem]" starts at 0, increases to a peak of approximately 0.4 around 9 hours, and then decreases back to 0 by 12 hours.
- A dash-dot line labeled "[Deg*]" starts at 0, remains at 0 until approximately 9 hours, then sharply increases to 1 and remains constant at 1 until 16 hours.
: chart::>
(d)

<a id='7f57f8a9-1b25-46db-a779-24f59518c5c2'></a>

(c)<::chart: A line graph titled "Fig. 6. Exogenous Δ34Xic1 is degraded prior to the destruction of cy [Xic1 total]/[Xic1]initial is plotted." The y-axis ranges from 0 to 1.0, with major ticks at 0, 0.2, 0.4, 0.6, 0.8, and 1.0. The x-axis is labeled "Hours post fertilization" and ranges from 0 to 16, with major ticks at 0, 4, 8, 12, and 16. Two lines are plotted: a dashed line labeled "[Xic1 total]" starts at a relative concentration of 1.0, gradually decreases, and then drops sharply between approximately 10 and 14 hours. A solid line labeled "[CycE Total]" remains at a relative concentration of 1.0 until approximately 9 hours, then drops sharply between approximately 9 and 12 hours, reaching near 0 by 12 hours.::>(d) Experiments. Embryos were injected time points and analyzed by immunoblotting for content of cyclin E ar indicated on the left. Note: Xic1-C reacts weakly with the Xic1 antibo Δ34Xic1.

<a id='6980fa08-409f-4449-98c9-9335081a7d3b'></a>

<::Western blot showing protein expression over time under two conditions. The blot is divided into two main panels.

Top Panel:
-   **Conditions:** GST-Xic-C and GST-Δ34Xic
-   **Time points (hours pf):** 4, 6, 8, 10, 13 for each condition.
-   **Protein detected:** cyclin E (indicated by an arrow on the right).
-   **Molecular weight markers (left):** 49.5, 37.4, 26.0.
-   **Observations:** Cyclin E shows relatively stable expression under GST-Xic-C. Under GST-Δ34Xic, cyclin E expression appears to increase slightly at 6 and 8 hours, then decrease.

Bottom Panel:
-   **Conditions:** GST-Xic-C and GST-Δ34Xic (same as top panel).
-   **Time points (hours pf):** 4, 6, 8, 10, 13 for each condition.
-   **Proteins detected (indicated by arrows on the right):** Δ34Xic1 (upper band) and Xic-C (lower band).
-   **Molecular weight marker (left):** 37.4.
-   **Observations:** Under GST-Xic-C, Xic-C is weakly present at early time points. Under GST-Δ34Xic, Δ34Xic1 shows strong expression peaking around 6-8 hours, while Xic-C is not prominently visible.::>

<a id='c60185a2-40ad-4994-baec-82051462b425'></a>

Fig. 6. Exogenous Δ34Xic1 is degraded prior to the destruction of cyclin E. (a,b,c) Simulation. [Xic1]initial=3. In panel (c),
[Xic1total]/[Xic1]initial is plotted. (d) Experiments. Embryos were injected with 5 ng of Xic1-C or Δ34Xic1, collected at the indicated
time points and analyzed by immunoblotting for content of cyclin E and Xic1. The migration of molecular weight standards is
indicated on the left. Note: Xic1-C reacts weakly with the Xic1 antibody, but is detected and is degraded at the same time as
Δ34Xic1.

<a id='f122f321-8a02-4f18-8e4e-732b73c5e6d3'></a>

[44,45]. As long as free Xic1 is present in the cell,
cyclin E/Cdk2 complexes that lose their Xic1
partner will quickly pick up another. Between 5
and 9 h, a steady drop in concentration of free
Xic1 is observed, with only a modest rise in
removed cyclin E/Cdk2 (Fig. 6b). Once the sup-
ply of Xic1 is exhausted, the unphosphorylated
form of removed cyclinE/Cdk2 can turn on Deg
(Fig. 6b) and cyclin E is degraded (Fig. 6c). We
assume that removed cyclin E/Cdk2 is not immu-

<a id='6255b141-dc7b-43ce-ab18-ba9a5e02f9ab'></a>

noprecipitated and detected in H1 kinase assays
because we do not detect a transient peak in cyclin
E/Cdk2 activity between the degradation of
microinjected \u039434Xic1 and the degradation of
cyclin E (Fig. 2 and data not shown). Alternatively,
the peak in removed cyclin E/Cdk2 may be too
transient or too low in amplitude to be detected in
our kinase assays.

<a id='8641e02d-fc85-4af6-ae60-59a4985ef942'></a>

Plotting levels of A34Xic1 and cyclin E over
time (Fig. 6c) indicates that (1) cyclin E is

<!-- PAGE BREAK -->

<a id='6932f2cf-ff54-4c57-89b6-bf2b34c92345'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='c8aea980-8767-4ecb-aafe-1e401f89aff6'></a>

583

<a id='97191a15-94c2-480e-99a7-cdb3214f16d5'></a>

<::chart: (a) Simulation. The chart shows Total cyclin E (y-axis, ranging from 0 to 1) over Hours post fertilization (x-axis, ranging from 0 to 16). Four curves represent different initial amounts of Xic1: 0, 1.5, 3, and 6. All curves start at a cyclin E level of 1.0 and decrease over time, indicating degradation. The degradation of cyclin E is progressively delayed as the initial Xic1 amount increases. For example, the curve for Xic1=0 shows rapid degradation around 7 hours, while the curve for Xic1=6 shows degradation starting much later, around 10-12 hours.::> <::immunoblot: (b) Experiment. This panel displays immunoblots for cyclin E content at different time points (hours pf: 5, 7, 8, 9, 10, 11) for varying amounts of Δ34Xic1 injected (0, 2.5, 5, 10 ng). Each row corresponds to a different injection amount of Δ34Xic1. Arrows on the right side of each row indicate the position of the cyclin E band. For 0 ng Δ34Xic1 injected, cyclin E bands are strong at 5 hours and diminish by 9-10 hours. As the injected Δ34Xic1 increases to 2.5, 5, and 10 ng, the degradation of cyclin E is delayed, with prominent bands visible at later time points (e.g., up to 11 hours for 10 ng Δ34Xic1).::> Fig. 7. Timing of cyclin E degradation is dependent upon the dose of Δ34Xic1. (a) Simulation. Total cyclin E for different amounts of Xic1 added to the system. As in Fig. 6, Xic1 is degraded prior to cyclin E. The times when one-half of the original Xic1 has been degraded are 6.4, 7.6 and 10 h for [Xic1]initial = 1.5, 3 and 6, respectively The times when one-half of the original cyclin E has been degraded are 7, 7.7, 10.3 and 15.4 h for [Xic1]initial =0, 1.5, 3 and 6, respectively. (b) Experiment. Embryos were injected with 0, 2.5, 5 or 10 ng of Δ34Xic1, collected at the time points indicated, and analyzed by immunoblotting for content of cyclin E. Arrows denote the position of cyclin E.

<a id='852a1e40-7b71-4841-91fb-3892d2eb4e65'></a>

degraded abruptly at approximately 10 h pf, con-
sistent with observations [25], and (2) A34Xic1 is
degraded a few hours before cyclin E.

<a id='76b10c61-ced9-4424-9a19-50ec7ccdf789'></a>

Since the content of Δ34Xic1 over time had not been monitored in previous studies of Δ34Xic1- injected embryos, the theoretical prediction that Δ34Xic1 would be degraded prior to the degrada- tion of cyclin E was tested experimentally. Embry- os were injected with 5 ng of Xic1-C or Δ34Xic1 at the one-cell stage, collected at multiple time points and analyzed for content of cyclin E and Xic1 (Fig. 6d). The level of Δ34Xic1 dropped sharply between 6 and 8 h pf, prior to the degra- dation of cyclin E between 8 and 10 h pf, confirm- ing this prediction of the model.

<a id='4e030320-b3da-4351-ae6c-191f6788253a'></a>

4.3.3. *Cyclin E degradation is progressively delayed by increasing amounts of Δ34Xic1*

As a final test of the model, the dose of Δ34Xic1 was altered in simulations to determine the effect on cyclin E degradation. Simulations (Fig. 7a) suggested that the timing of cyclin E degradation should be inversely correlated to the quantity of Δ34Xic1 injected over at least a four-fold range.

<a id='5cd6cbc7-6fc3-4dea-9e4b-66943c1756ce'></a>

To test this prediction experimentally, embryos were injected with 0, 2.5, 5 or 10 ng of Δ34Xic1. The total injection volume was kept constant. Embryos were analyzed for the degradation of cyclin E at multiple time points (Fig. 7b). In embryos lacking Δ34Xic1, most cyclin E degradation occurred between 5 and 7 h pf. In embryos injected with 2.5 or 5 ng of Δ34Xic1, cyclin E degradation occurred 7–8 and 9–10 h pf, respectively. Little degradation of cyclin E was detected in embryos injected with 10 ng of Δ34Xic1, even as late as 11 h pf. The simulations and experimental data correlate well, further supporting the theoretical basis of the model.

<a id='39e7bada-918f-4cb5-87e7-031ba73bab67'></a>

These observations allow us to estimate the 'arbitrary units' of Xic1 concentration in the model. [Total Xic1]=1 AU corresponds to 1.67 ng of Δ34Xic1 per embryo (1.5 AU simulates activity of 2.5 ng of Δ34Xic1; 3 AU simulates 5 ng of Δ34Xic1, etc.), which is a concentration of approximately 33 nM (assuming one embryo is equivalent to 1.0 µl and the molecular weight of Δ34Xic1 is 50 000 g/mol). Since Xic1 and cyclin E/Cdk2 bind in 1:1 stoichiometry, this means that [total

<!-- PAGE BREAK -->

<a id='62975caf-e305-46da-8e35-0803fa1a821f'></a>

584

<a id='05886d92-91dc-47f8-beeb-5ab77ec7839a'></a>

A. Ciliberto et al. / *Biophysical Chemistry* 104 (2003) 573–589

<a id='1d60bd2e-0403-4992-bb41-e783599f6193'></a>

cyclin E]=1 AU also corresponds to approximate-
ly 33 nM.

<a id='9005d365-3c45-435b-a2cd-7761a294cac9'></a>

# 5. Discussion

By combining computational and experimental approaches, we have built a model of the cyclin E/Cdk2 developmental timer in early *Xenopus* embryos. Development of the model was constrained by experimental evidence obtained from intact *Xenopus* embryos: (1) oscillations in cyclin E/Cdk2 occur twice per cell cycle prior to the MBT [25]; (2) the level of cyclin E remains constant during this time [25,32]; and (3) cyclin E is degraded at a fixed time post-fertilization, independent of cell number, protein synthesis, nucleocytoplasmic ratio and zygotic transcription [25,32]. The model faithfully reproduces 22 oscillations in cyclin E/Cdk2 activity and degradation of cyclin E at approximately 6–7 h pf, independent of protein synthesis. Experimental evidence that the degradation of cyclin E is delayed in embryos microinjected with 5 ng of Δ34Xic1 [25] also agrees with the simulations.

<a id='1d056c10-cb27-4c8a-b58e-209e49cfc42b'></a>

The model is composed of three 'modules': an oscillatory module, based on a delayed negative feedback loop; a switching module, based on cooperative removal of cyclin E/Cdk2; and a proteolysis module, based on irreversible activation of the cyclin E degradation pathway.

<a id='6cd488f9-7f97-4cb8-9dfe-70521060259e'></a>

5.1. Oscillatory module

In the oscillatory module, oscillations in cyclin E/Cdk2 activity do not depend on cyclin E synthesis or degradation, because total cyclin E level is quite constant throughout the early stages of frog embryogenesis [25]. Nor are these oscillations attributable to periodic fluctuations in a stoichiometric inhibitor, Xic1, because Xic1 is not normally present in the early embryo [33]. That leaves reversible inhibitory phosphorylation of Cdk2 as the prime suspect for generating oscillations in cyclin E/Cdk2 activity. To the best of our knowledge, oscillations in the phosphorylation state of Cdk2 have not been measured in intact embryos and may be difficult to observe because the oscillations are rapid and may be localized within

<a id='4595c340-17f0-4add-9aaf-8de608dc4e23'></a>

nuclei. On the other hand, Cdk2 activity is regu-
lated by reversible phosphorylation in extracts
[37], and embryos microinjected with XChk1,
which promotes tyrosine phosphorylation of Cdks,
have reduced cyclin E/Cdk2 activity [40]. If cyclin
E/Cdk2 oscillations derive from reversible phos-
phorylation alone, then the components must be
involved in a negative feedback loop, with cyclin
E/Cdk2 either promoting Weel activity or inhib-
iting Cdc25. This supposition is in sharp contrast
to the case of cyclin B/Cdk1, which inhibits Weel
and activates Cdc25. In that case, oscillations
depend on Cdk1 turning on cyclin B degradation
by activating Fizzy/APC [12]. Therefore, Cdk2
oscillations are fundamentally different from Cdk1
oscillations.

<a id='d33978ec-7b0d-4642-9313-fa0f159902ab'></a>

At this point, the oscillatory module in Fig. 4 is purely hypothetical and awaits experimental validation. It should also be kept in mind that a negative feedback loop, whereby cyclin E/Cdk2 indirectly *inhibits* Cdc25, might be an alternative basis for oscillations in Cdk2 activity.

<a id='011c744e-af14-4b86-a6bd-9ce7bbbc2885'></a>

5.2. Switching module

The second major assumption in the model is that the timing of cyclin E degradation depends upon cyclin E/Cdk2 activity, in particular upon removed cyclin E/Cdk2. In support of this assumption, degradation of cyclin E is delayed when Cdk2 activity is inhibited by either A34Xic1 [25] or XChk1 (Fig. 1). However, in A34Xic1-injected embryos, cyclin E is eventually degraded. The model incorporates the idea that cyclin E/Cdk2 promotes chromatin association and subsequent degradation of Xic1, as suggested by the experiments of Furstenthal et al. [45]. In simulations of A34Xic1-injected embryos, cyclin E is degraded some hours after degradation of A34Xic1 (Fig. 6c). This prediction was validated experimentally (Fig. 6d).

<a id='af4c8d5f-9e1a-4935-a9db-c7533e4e5e5b'></a>

Initially, we assumed that 'removed' cyclin E
was chromatin-bound cyclin E, and that association
of cyclin E with chromatin was cooperative. This
assumption was based on data indicating that
cyclin E/Cdk2 associates with chromatin [47] and
is responsible for loading Xic1 onto chromatin,
where Xic1 is then degraded [44,45]. However,

<!-- PAGE BREAK -->

<a id='119225b0-2dd8-4230-8a17-3fcb87c397ea'></a>

A. Ciliberto et al. / *Biophysical Chemistry* 104 (2003) 573–589

<a id='bbebdde0-8815-4f98-9aa0-1b63d144dd2d'></a>

585

<a id='9d0388eb-1509-4a72-aa46-23f8286b59b7'></a>

Table 4
Differential equations used for bifurcation analysis in Fig. 8

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>1</td><td>$\frac{d}{dt}$[Cdk2:CycE] = -$k_{wee}$[Wee1*][Cdk2:CycE]+$k_{25A}$($E_{tot}$ -$H$-[Cdk2:CycE])</td></tr><tr><td>3</td><td>$\frac{d}{dt}$[Wee1*]=$\frac{k_{wact}$([Wee1$_{total}$]-[Wee1*])}{J_{wact}$+[Wee1$_{total}$]-[Wee1*]}$-$\frac{k_{winact}$[Kin*][Wee1*]}{J_{winact}$+[Wee1*]}</td></tr><tr><td>4</td><td>$\frac{d}{dt}$[Kin*]=$\frac{k_{iact}$(1-[Kin*])}{J_{iact}$+1-[Kin*]}$-$\frac{k_{iinact}$[Cdk2:CycE][Kin*]}{J_{iinact}$+[Kin*]}</td></tr><tr><td>5</td><td>$\frac{d}{dt}$H=+$k_{on}$$\frac{\epsilon+H^n}{L^n+H^n}$$\times$($E_{tot}$-$H$)-$k_{off}$H</td></tr></tbody></table>

In the simplified model, cyclin E degradation and Xic1 binding are ignored. These equations are carried over from Table 2, with the understanding that $H$= [removed forms of Cdk2:CycE] and $E_{tot}$ = [all forms of Cdk2:CycE].

<a id='58b388bd-b1e0-4251-9638-f770450d11c1'></a>

binding of cyclin E/Cdk2 to chromatin depends
upon DNA replication cycles [47], inconsistent
with observations that degradation of cyclin E
occurs at a fixed time, even in cycloheximide-
treated embryos (in which DNA replication is
blocked indirectly) [25,41]. Therefore, we aban-
doned the specific model of chromatin binding.

<a id='54434c36-fd89-46d3-b641-3b4a20b5381f'></a>

Alternatively, 'removed' cyclin E/Cdk2 could be a posttranslationally modified form. When cyclin E is autophosphorylated by cyclin E/Cdk2, it binds an F-box protein and becomes ubiquitin-ated and degraded by the SCF (reviewed in [48]). If autophosphorylated cyclin E/Cdk2 were rapidly degraded, then the removal step would not be cooperative. Therefore, a sufficient time delay is needed between autophosphorylation and degra-dation of cyclin E. Since cyclin E needs to be phosphorylated at a second site prior to degrada-tion [49], the time delay could exist if autophos-phorylated cyclin E/Cdk2 were to phosphorylate and activate another kinase (e.g. Deg). One dis-crepancy with our model is that Xic should inhibit the removal of cyclin E in this case, since 'remov-al' depends upon cyclin E/Cdk2 catalytic activity. A key assumption of the model is that removal is not inhibited by Xic. Clearly, the details of the removal step are speculative and need to be deter-mined by future experimentation. Therefore, the removal mechanism remains deliberately general in the model.

<a id='fcc013ad-12ad-4a36-b7f2-8562d1954e25'></a>

5.3. *Degradation module*

We have not attempted to model the molecular
machinery of cyclin E degradation, because it does

<a id='aa53acc7-aa4c-4a84-8761-e442704f94a5'></a>

not feedback, as far as we know, on the dynamics
of the oscillatory and switching modules. To keep
this part of the model as simple as possible, we
use a 'Heaviside function' to switch on cyclin E
degradation in an irreversible fashion, after a
sufficient amount of Cdk2:CycErem has accu-
mulated.

<a id='dbf3991b-7056-4480-ab84-9cdb8debaaa6'></a>

5.4. *Bifurcation analysis of the mathematical model*

<a id='60ec4ca9-2560-443b-aec0-7f55c5340bcd'></a>

To understand better the fundamental behavior
of the cyclin E/Cdk2 developmental timer, bifur-
cation analysis was applied to a simplified version
of the model. (A primer on bifurcation analysis is
available in [15].) Because our aim was to uncover
the dynamics of the oscillatory and switching
modules, we have eliminated Xic1 binding and
cyclin E degradation from the network (see Table
4). A numerical simulation of these equations is
presented in Fig. 8a. Removed cyclin E/Cdk2
(dashed line) increases abruptly at approximately
6 h pf, indicative of cooperativity, as postulated
by the model. Oscillations in active free cyclin E/
Cdk2 (solid line) are created by the negative
feedback loop involving Wee1 and quenched by
the cooperative removal of cyclin E/Cdk2.

<a id='f34d4203-5c2a-483b-9074-0d0fdc17f4c6'></a>

In Fig. 8b, we consider the behavior of the
negative feedback loop as a function of the fraction
of removed cyclin E. That is, we fix [Cdk2:
CycErem] + [PCdk2:CycErem]=H=constant, and
study the behavior of the negative feedback loop
as a function of the value of H. For 0<H<0.45,
the steady-state solution of the negative feedback

<!-- PAGE BREAK -->

<a id='7167b101-c9f8-42f6-9d2b-2ca6131a43c4'></a>

586 A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589<::chart::>(a) Graph showing concentration over time. The y-axis ranges from 0 to 1.2. The x-axis is "Hours post fertilization" and ranges from 0 to 16. There are two curves: a solid oscillating curve labeled "[Cdk2:CycE]" and a dashed curve rising from 0 to approximately 1.0, labeled "[Cdk2:CycErem]+[PCdk2:CycErem]".(b) Graph showing concentration and period as a function of another concentration. The left y-axis is "[Cdk2:CycE]" ranging from 0 to 0.5. The right y-axis is "Period (min)" ranging from 0 to 16. The x-axis is "[Cdk2:CycE] + [PCdk2:CycEm]" ranging from 0 to 1. There are three series plotted: a solid line decreasing from 8 to 0, representing the Period (min); black filled circles showing a concentration that increases then decreases; and open diamonds showing another concentration that increases then decreases, reaching higher values than the black filled circles.::>

<a id='2c8df98a-689d-4320-bf40-567cb57cd0e1'></a>

<::Figure 8. Bifurcation analysis of the cyclin E/Cdk2 developmental timer. (a) Simulation of the equations in Table 4. Removed cyclin E/Cdk2 (dashed line; H=[Cdk2:CycErem] + [P Cdk2:CycErem]) and active, unremoved cyclin E/Cdk2 (solid line) as functions of time. (b) Dependence of negative feedback oscillations on H. The ordinate is [Cdk2:CycE], except for the open diamonds, which indicate the period of oscillation (scale on right). Solid line, stable steady state; dashed line, unstable steady state; black circles, maximum and minimum values of [Cdk2:CycE] during the course of an oscillation at fixed H. The control system undergoes a Hopf bifurcation at H=0.45. (c) Bistability in the positive feedback module. We plot dH/dt as a function of H for two values of koff. The system is monostable (one steady state, where dH/dt=0) for koff=0.0001 (solid line) and bistable (three steady states) for koff=0.01 (dashed line). (d) Oscillations in the negative feedback module, H=0. Symbols as in panel (b). The steady state is unstable between the two points of Hopf bifurcation at τ=4×10⁻⁴ and 12 (see text).: chart::>

<a id='3dcc06eb-b3be-4d7f-8385-609191c01551'></a>

loop (_dashed line_) is unstable, and the network
executes sustained oscillations (the black circles
indicate the maximum and minimum values of
active cyclin E/Cdk2 over the course of an oscil-

<a id='5add99d3-6b80-4a75-83ec-d3e6c6f06da3'></a>

lation) with period close to 14 min (open dia-
monds). For 0.45<H<1, the negative feedback
loop has a stable steady state (solid line) and no
sustained oscillations. At H=0.45, the negative

<!-- PAGE BREAK -->

<a id='d1281cdc-3717-46e9-b500-0f5376cfcf57'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='81e92309-0cf6-438a-9fe1-c68318d7c923'></a>

587

<a id='86213b5f-6adb-4ec2-9dca-88cb96df82fd'></a>

feedback loop is said to undergo a Hopf bifurca-
tion. Now, comparing Fig. 8a,b, we observe that
as H increases from 0 to 0.45 (during the first 5
h pf), the negative feedback loop oscillates with a
period of approximately 14 min. However, as soon
as H exceeds the Hopf-bifurcation point, the oscil-
lations are quickly lost.

<a id='c081f2cb-4e9a-4415-9e29-b7c19762c291'></a>

To see why H increases as in Fig. 8a, we plotted the rate of change of H (dH/dt) as a function of H in Fig. 8c. When dH/dt is positive, H increases; when dH/dt is negative, H decreases. Steady states exist wherever dH/dt=0. For the parameter set used here (solid line), a single stable steady state exists at H close to 1. Hence, starting with H=0 (no removed cyclin E/Cdk2), H must increase until it reaches the steady state, where most cyclin E/Cdk2 is removed. Note, however, that the rate of increase of H is, at first, very small (dH/ dt≈0.0008) and then accelerates rapidly by nearly 10-fold. This acceleration is a reflection of the cooperative removal of cyclin E/Cdk2 in the model.

<a id='f85687e3-35df-4ccc-89ab-aaecee21cb6e'></a>

Cooperative removal is a form of positive feedback (autocatalysis) that can easily create bistable behavior. If the dissociation rate constant, k_off, is increased from 0.0001 to 0.01, then dH/dt as a function of H is modified (dashed line) so that there now exist two stable steady states: one with H≈0.1 (little removed cyclin E), and another with H≈0.7 (most cyclin E removed). At the lower steady state, the negative feedback loop will be in its oscillatory regime, and at the upper steady state, the negative feedback loop will be quiescent. This behavior of the control system is entirely different from what is observed. We have chosen our parameter set (Table 3) to bring the control system close to but not within its region of bistability. With this choice, H increases slowly at first, pulling the oscillatory module past its Hopf bifurcation, and then H increases rapidly, as most of the cyclin E is removed from the oscillatory system.

<a id='285e1ae9-3464-4828-bf38-1e64b1cbf3b6'></a>

Finally, we have mentioned several times that
oscillations in the negative feedback loop require
an intermediate, Kin, between cyclin E/Cdk2 and
Weel. Kin introduces a time delay between acti-
vation of cyclin E/Cdk2 and subsequent increase
in Weel activity. This time delay depends on the
characteristic time, т, required for cyclin E/Cdk2

<a id='949cc227-bbce-4e56-8229-5d615dca6c31'></a>

to inactivate Kin (τ=1/k_iinact). The basal value of
τ is 1.67 (see Table 3). As τ decreases, the time
delay in the negative feedback loop becomes
negligible, and oscillations disappear at a Hopf
bifurcation, at τ=4×10⁻⁴ in Fig. 8d. (To keep
the relative activity of Kin fixed, we steadily
increase both k_iact and k_iinact, keeping their ratio
constant at k_iact/k_iinact=0.25.) The amplitude of
oscillation becomes quite small, even for τ <0.05.
In other words, oscillations in the negative feed-
back loop require an intermediate that introduces
a minimal time lag between cyclin E/Cdk2 and
Wee1. Fig. 8d shows that oscillations are also lost
if τ becomes too large (τ>12).

<a id='bdb2463b-a9b3-46aa-9ae4-075092904ed8'></a>

5.5. Future developments

The model presented here will be refined as new experimental data become available. Most importantly, experiments are needed to identify whether Kin exists and functions in a negative feedback loop between cyclin E/Cdk2 and Wee1. Alternatively, does negative feedback exist between cyclin E/Cdk2 and Cdc25? In addition, the specific nature of 'removed' cyclin E needs to be determined.

<a id='e71f2b83-59e4-4345-83a4-062f16ca6a10'></a>

## Acknowledgments

We are grateful to Dr Rebecca Hartley (University of New Mexico Health Sciences Center) for the cyclin E antibody, and to Dr James Maller (Howard Hughes Medical Institute, University of New Mexico Health Sciences Center) for the Xic1 protein and cyclin antibodies. The experiment in Fig. 1 was performed by JCS while in Dr Maller's lab. We appreciate Dr Monica Murakami's (National Cancer Institute; NIH) help with preliminary Wee1 studies. This work has been supported by the National Institutes of Health (Grant Numbers R01-GM59688 to JCS, R01-GM64339 to JJT), the Defense Advanced Research Projects Agency—Biocomputation Program (AFRL #F30602-02-0572), the National Science Foundation—Biocomplexity Program (MCB-0083315), and the Research Division of Virginia Tech.

<!-- PAGE BREAK -->

<a id='a295db2d-129e-489e-902c-8d59a3801977'></a>

588

<a id='88ca4cac-356a-44ed-b206-d5ecc8073fbb'></a>

A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589

<a id='5c20da88-2c4a-41fb-9aa7-ebe96a2b66e3'></a>

# References

1. M.J. Solomon, M. Glotzer, T.H. Lee, M. Phillippe, M.W. Kirschner, Cyclin activation of p34cde2, Cell 63 (1990) 1013-1024.
2. M.J. Solomon, T.H. Lee, M.W. Kirschner, Role of phosphorylation in p34cde2 activation: identification of an activating kinase, Mol. Cell. Biol. 3 (1992) 13-27.
3. A.W. Murray, M.W. Kirschner, Cyclin synthesis drives the early embryonic cell cycle, Nature 339 (1989) 275-280.
4. A. Devault, D. Fesquet, J.-C. Cavadore, et al., Cyclin A potentiates maturation-promoting factor activation in the early *Xenopus* embryo via inhibition of the tyrosine kinase that phosphorylates cdc2, J. Cell Biol. 118 (1992) 1109-1120.
5. P.R. Mueller, T.R. Coleman, W.G. Dunphy, Cell cycle regulation of a *Xenopus* Wee1-like kinase, Mol. Biol. Cell 6 (1995) 119-134.
6. P.R. Mueller, T.R. Coleman, A. Kumagai, W.G. Dunphy, Myt1: a membrane-associated inhibitory kinase that phosphorylates cdc2 on both threonine-14 and tyrosine-15, Science 270 (1995) 86-90.
7. J. Gautier, M.J. Solomon, R.N. Booher, J.F. Bazan, M.W. Kirschner, cdc25 is a specific tyrosine phosphatase that directly activates p34cdc2, Cell 67 (1991) 197-211.
8. A. Kumagai, W.G. Dunphy, The cdc25 protein controls tyrosine dephosphorylation of the cdc2 protein in a cell-free system, Cell 64 (1991) 903-914.
9. A. Kumagai, W.G. Dunphy, Regulation of the cdc25 protein during the cell cycle in *Xenopus* extracts, Cell 70 (1992) 139-151.
10. C. Smythe, J.W. Newport, Coupling of mitosis to the completion of S-phase in *Xenopus* occurs via modulation of the tyrosine kinase that phosphorylates p34cdc2, Cell 68 (1992) 787-797.
11. T. Izumi, J.L. Maller, Elimination of cdc2 phosphorylation sites in the cdc25 phosphatase blocks initiation of M-phase, Mol. Biol. Cell 4 (1993) 1337-1350.
12. T. Lorca, A. Castro, A.M. Martinez, et al., *Fizzy* is required for activation of the APC/cyclosome in *Xenopus* egg extracts, EMBO J. 17 (1998) 3565-3575.
13. B. Novak, J.J. Tyson, Numerical analysis of a comprehensive model of M-phase control in *Xenopus* oocyte extracts and intact embryos, J. Cell Sci. 106 (1993) 1153-1168.
14. B. Novak, J.J. Tyson, Quantitative analysis of a molecular model of M-phase control in *Xenopus* oocyte extracts and intact embryos, J. Theor. Biol. 173 (1995) 283-305.
15. M.T. Borisuk, J.J. Tyson, Bifurcation analysis of a model of mitotic control in frog eggs, J. Theor. Biol. 195 (1998) 69-85.
16. G. Marlovits, C.J. Tyson, B. Novak, J.J. Tyson, Modeling M-phase control in *Xenopus* oocyte extracts: the

<a id='9aa24c58-89d3-4083-bffc-3ffd2bb411b0'></a>

surveillance mechanism for unreplicated DNA, Biophys. Chem. 72 (1998) 169–184.

[17] M.A. Felix, J.C. Labbe, M. Doree, T. Hunt, E. Karsenti, Triggering of cyclin degradation in interphase extracts of amphibian eggs by cdc2 kinase, Nature 346 (1990) 379–382.

[18] Y. Masui, C. Markert, Cytoplasmic control of nuclear behavior during meiotic maturation of frog oocytes, J. Exp. Zool. 177 (1971) 129–146.

[19] J. Gerhart, M. Wu, M. Kirschner, Cell cycle dynamics of an M-phase-specific cytoplasmic factor in Xenopus laevis oocytes and eggs, J. Cell. Biol. 98 (1984) 1247–1255.

[20] M. Cyert, M. Kirschner, Regulation of MPF activity in vitro, Cell 53 (1988) 185–195.

[21] A. Kumagai, W.G. Dunphy, Regulation of Xenopus cdc25 protein, Methods Enzymol. 283 (1997) 564–571.

[22] J. Newport, M. Kirschner, A major developmental transition in early Xenopus embryos: I. Characterization and timing of cellular changes at the midblastula stage, Cell 30 (1982) 675–686.

[23] J. Newport, M. Kirschner, A major developmental transition in early Xenopus embryos: II. Control of the onset of transcription, Cell 30 (1982) 687–696.

[24] D.L. Frederick, M.T. Andrews, Cell cycle remodeling requires cell-cell interactions in developing Xenopus embryos, J. Exp. Zool. 270 (1994) 410–416.

[25] R.S. Hartley, J.C. Sible, A.L. Lewellyn, J.L. Maller, A role for cyclin E/Cdk2 in the timing of the midblastula transition in Xenopus embryos, Dev. Biol. 188 (1997) 312–321.

[26] R.S. Hartley, R.E. Rempel, J.L. Maller, In vivo regulation of the early embryonic cell cycles in Xenopus, Dev. Biol. 173 (1996) 408–419.

[27] P.K. Jackson, S. Chevalier, M. Philippe, M.W. Kirschner, Early events in DNA replication require cyclin E and are blocked by p21CIP1, J. Cell Biol. 130 (1995) 755–769.

[28] U.P. Strausfeld, M. Howell, R. Rempel, J.L. Maller, T. Hunt, J.J. Blow, Cip1 blocks the initiation of DNA replication in Xenopus extracts by inhibition of cyclin-dependent kinases, Curr. Biol. 4 (1994) 876–883.

[29] E.H. Hinchcliffe, C. Li, E.A. Thompson, J.L. Maller, G. Sluder, Requirements of Cdk2-cyclin E activity of repeated centrosome reproduction in Xenopus egg extract, Science 283 (1999) 851–854.

[30] K.R. Lacey, P.K. Jackson, T. Stearns, Cyclin-dependent kinase control of centrosome duplication, Proc. Natl. Acad. Sci. USA 96 (1999) 2817–2822.

[31] R.E. Rempel, S.B. Sleight, J.L. Maller, Maternal Xenopus Cdk2–cyclin E complexes function during meiotic and early embryonic cell cycles that lack a G1-phase, J. Biol. Chem. 270 (1995) 6843–6855.

[32] J.A. Howe, J.W. Newport, A developmental timer regulates degradation of cyclin E1 at the midblastula

<!-- PAGE BREAK -->

<a id='0d9378fe-0c76-45e2-8ad7-156a07cd9a43'></a>

*A. Ciliberto et al. / Biophysical Chemistry 104 (2003) 573–589*

<a id='d14421c3-d106-496e-a79a-12440628821a'></a>

589

<a id='ea8ae02d-ba1a-46f6-b0c7-3bb93ca697bd'></a>

transition during *Xenopus* embryogenesis, Proc. Natl. Acad. Sci. USA 93 (1996) 2060–2064.

[33] W. Shou, W.G. Dunphy, Cell cycle control by *Xenopus* p28Kix1, a developmentally regulated inhibitor of cyclin-dependent kinases, Mol. Biol. Cell 7 (1996) 457–469.

[34] A.W. Murray, M.J. Solomon, M.W. Kirschner, The role of cyclin synthesis and degradation in the control of maturation promoting factor activity, Nature 339 (1989) 280–286.

[35] J.E. Ferrell, M. Wu, J.C. Gerhart, G.S. Martin, Cell cycle tyrosine phosphorylation of p34cdc2 and a microtubule-associated protein kinase homolog in *Xenopus* oocytes and eggs, Mol. Cell. Biol. 11 (1991) 1965–1971.

[36] S. Kim, C. Li, J. Maller, A maternal form of the phosphatase Cdc25A regulates early embryonic cell cycles in *Xenopus laevis*, Dev. Biol. 212 (1999) 381–391.

[37] V. D'Angiolella, V. Costanzo, M.E. Gottesman, E.V. Avvedimento, J. Gautier, D. Grieco, Role for cyclin-dependent kinase 2 in mitosis exit, Curr. Biol. 11 (2001) 1221–1226.

[38] P.D. Nieuwkoop, J. Faber, Normal Table of *Xenopus laevis*, North Holland Publishing Company, Amsterdam, 1975.

[39] J.-Y. Su, R.E. Rempel, E. Erikson, J.L. Maller, Cloning and characterization of the *Xenopus* cyclin-dependent kinase inhibitor p27Xic1, Proc. Natl. Acad. Sci. USA 92 (1995) 10187–10191.

[40] N. Kappas, P. Savage, K.C. Chen, A.T. Walls, J.C. Sible, Dissection of the XChk1 signaling pathway in *Xenopus laevis* embryos, Mol. Biol. Cell 11 (2000) 3101–3108.

[41] J.C. Sible, J.A. Anderson, A.L. Lewellyn, J.L. Maller, Zygotic transcription is required to block a maternal program of apoptosis in *Xenopus* embryos, Dev. Biol. 189 (1997) 335–346.

<a id='516048ba-561c-4c1c-b184-914be00f1e69'></a>

[42] J.J. Tyson, B. Novak, G.M. Odell, K. Chen, C.D. Thron, Chemical kinetic theory: understanding cell-cycle regulation, Trends Biochem. Sci. 21 (1996) 89–96.
[43] J.S. Griffith, Mathematics of cellular control processes. I. Negative feedback to one gene, J. Theor. Biol. 20 (1968) 202–208.
[44] C. Swanson, J. Ross, P.K. Jackson, Nuclear accumulation of cyclin E/Cdk2 triggers a concentration-dependent switch for the destruction of p27Xic1, Proc. Natl. Acad. Sci. USA 97 (2000) 7796–7801.
[45] L. Furstenthal, C. Swanson, B.K. Kaiser, A.G. Eldridge, P.K. Jackson, Triggering ubiquitination of a CDK inhibitor at origins of replication, Nat. Cell Biol. 3 (2001) 715–722.
[46] L.-C. Chuang, P.R. Yew, Regulation of nuclear transport and degradation of the Xenopus cyclin-dependent kinase inhibitor, p27Xic1, J. Biol. Chem. 276 (2001) 1610–1617.
[47] L. Furstenthal, B. Kaiser, C. Swanson, P. Jackson, Cyclin E uses Cdc6 as a chromatin-associated receptor required for DNA replication, J. Cell Biol. 152 (2001) 1267–1278.
[48] J. Bartek, J. Lukas, Order from destruction, Science 294 (2001) 66–67.
[49] H. Strohmaler, C.H. Spruck, P. Kaiser, K.-A. Won, O. Sangfelt, S.I. Reed, Human F-box protein hCdc4 targets cyclin E for proteolysis and is mutated in a breast cancer cell line, Nature 413 (2001) 316–322.
[50] C.V. Finkelstein, L.G. Chen, J.L. Maller, A role for G1/S cyclin-dependent protein kinases in the apoptotic response to ionizing radiation, J. Biol. Chem. 277 (2002) 38476–38485.
[51] A. Goldbeter, D.E.J. Koshland, An amplified sensitivity arising from covalent modification in biological systems, Proc. Natl. Acad. Sci. USA 78 (1981) 6840–6844.
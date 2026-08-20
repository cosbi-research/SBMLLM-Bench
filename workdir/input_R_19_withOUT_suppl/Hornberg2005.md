<a id='0f9297b2-fe83-4dc2-8483-3e77610e90a4'></a>

Oncogene (2005) 24, 5533-5542
© 2005 Nature Publishing Group All rights reserved 0950-9232/05 $30.00

<a id='b99755ed-97ce-420d-8c5b-74385d94eeef'></a>

<::logo: [npg]
npg
The logo features the letters "npg" in white, enclosed within a solid black circular shape.::>

<a id='dd8667ba-4851-43f7-9073-daf34cd9938d'></a>

www.nature.com/onc

<a id='03f57832-8da9-427b-940d-e72821fc270b'></a>

ORIGINAL PAPERS
Control of MAPK signalling: from complexity to what really matters

<a id='5111b32d-f72b-4780-bb41-958639b14044'></a>

Jorrit J Hornberg  , Bernd Binder , Frank J Bruggeman , Birgit Schoeberl , Reinhart Heinrich 
and Hans V Westerhoff*,1,4

<a id='2ecf62b1-8459-4d8b-8784-c44b82ad6caf'></a>

¹Department of Molecular Cell Physiology, Institute of Molecular Cell Biology, Faculty of Earth and Life Sciences, Vrije Universiteit, Amsterdam, The Netherlands; ²Department of Theoretical Biophysics, Humboldt University, Berlin, Germany; ³Merrimack Pharmaceuticals, Cambridge, MA, USA; ´Mathematical Biochemistry, Swammerdam Institute for Life Sciences, University of Amsterdam, Amsterdam, The Netherlands

<a id='8d4239ae-70af-4fa6-9bb8-64b9d030e81c'></a>

Oncogenesis results from changes in kinetics or in abundance of proteins in signal transduction networks. Recently, it was shown that control of signalling cannot reside in a single gene product, and might well be dispersed over many components. Which of the reactions in these complex networks are most important, and how can the existing molecular information be used to understand why particular genes are oncogenes whereas others are not? We implement a new method to help address such questions. We apply control analysis to a detailed kinetic model of the epidermal growth factor-induced mitogen-activated protein kinase network. We determine the control of each reaction with respect to three biologically relevant characteristics of the output of this network: the amplitude, duration and integrated output of the transient phosphorylation of extracellular signal-regulated kinase (ERK). We confirm that control is distributed, but far from randomly: a small proportion of reactions substantially control signalling. In particular, the activity of *Raf* is in control of all characteristics of the transient profile of ERK phosphorylation, which may clarify why *Raf* is an oncogene. Most reactions that really matter for one signalling characteristic are also important for the other characteristics. Our analysis also predicts the effects of mutations and changes in gene expression.

*Oncogene* (2005) **24**, 5533–5542. doi:10.1038/sj.onc.1208817; published online 20 June 2005

<a id='4b7cef38-9290-462b-a09a-5fb38cb4d97a'></a>

**Keywords:** MAPK signalling; control analysis; kinetic model; systems biology
---


<a id='c683c1da-f824-4499-ba99-c03d4a4ef705'></a>

# Introduction
Cellular decisions with respect to division, differentia-
tion and apoptosis involve signal transduction. The
complexity of signal transduction networks is over-

<a id='038b7be6-5949-4ad9-b88a-cea9059601ad'></a>

*Correspondence: HV Westerhoff, Department of Molecular Cell Physiology, Institute of Molecular Cell Biology, Faculty of Earth and Life Sciences, Vrije Universiteit Amsterdam, De Boelelaan 1085, 1085 HV Amsterdam, The Netherlands; E-mail: hw@bio.vu.nl
These authors have contributed equally to this work
Received 18 October 2004; revised 18 March 2005; accepted 26 April 2005; published online 20 June 2005

<a id='29733286-2f8f-4953-afe3-3534ac6faf4e'></a>

whelming because of their large numbers of interacting constituents, by their complicated circuitry, involving feed forward, feedback and crosstalk, and by the fact that the kinetics of interaction matter (Huang and Ferrell, 1996; Kholodenko et al., 1999). As a result of this complexity, apparently simple but highly important questions remain unanswered. For instance, is a small number of reactions responsible for the behaviour of the entire system (and ultimately, for cellular behaviour) and if so, which are these reactions? This issue was made acute recently, when the old simplifying paradigm of single rate-limiting steps for signal transduction was falsified and replaced by the principle that control of signal transduction must add up to a total control strength, but may well be disperse (Hornberg et al., 2005).

<a id='880966d5-99f6-49ba-8890-139950a8fc9c'></a>

Is the control of signal transduction and hence of proliferation, differentiation and apoptosis always disperse then? Is there little hope of tinkering with that control once it has gone away? Such questions may be answered by detailed and extensive quantitative experimentation with inhibitors and activators of signal transduction proteins. However, both the arsenal and the specificity of these are limited. The frustrating conclusion seems to be that notwithstanding the considerable and increasing amount of molecular information concerning signal transduction pathways, we have no way of understanding how they are controlled, and hence no rational ways of finding targets for interfering with the processes.

<a id='772a99cc-806d-4048-b0c7-00a5cf538845'></a>

Signalling through one of the networks is initiated by the binding of epidermal growth factor (EGF) to its receptor (EGFR) and signals towards cell division and differentiation (Lewis et al., 1998; Cobb, 1999). The signal is propagated by recruited adaptor proteins, G-protein activation, (de-)phosphorylation reactions and the activation of the extracellular signal-regulated kinase (ERK). This mitogen-activated protein kinase (MAPK) pathway is constitutively activated by mutations in many human tumours (Hoshino et al., 1999). Active ERK has several cytoplasmic and nuclear targets, such as transcription factors that influence expression of genes involved in cell cycle progression (Treisman, 1996; Lewis et al., 1998), and it is required for the proliferation of fibroblasts (Pagès et al., 1993). Decisive for the type of cellular response that is evoked by MAPK signalling

<!-- PAGE BREAK -->

<a id='81d71c89-7efc-4bc2-aa7e-a927d4e697bb'></a>

<::logo: [NPG]npg5534A black circle with white text "npg" above the number "5534", separated by a horizontal line.::>

<a id='65663543-9654-4edf-9512-9a13a3866889'></a>

Control of MAPK signalling
JJ Hornberg et al
___

<a id='8cc77064-4c53-4f31-a961-084c19689ed7'></a>

are the magnitude and duration (transient versus
sustained) of ERK activation (Marshall, 1995; Tombes
et al., 1998; Cook et al., 1999). Again because of the
tremendous complexity of the pathway, it is understood,
which processes and proteins determine the dynamic
time profile of ERK activity and hence the choice
between proliferation and differentiation.

<a id='fdb01df8-c023-4c36-9372-77350d283bce'></a>

Putting all the available molecular information in a computer replica of the biological process and then interrogating that replica may help in such cases (Snoep and Westerhoff, 2005). This has been demonstrated for metabolic networks (Schuster and Holzhutter, 1995; Bakker et al., 1999; Teusink et al., 2000). Here, we extend this strategy to the MAPK pathway, by interrogating the largest kinetic model of EGF-induced signal transduction (Schoeberl et al., 2002) in terms of what controls its signal transduction activity.

<a id='bce9dfb8-e897-41d9-84cf-017ce2d5c542'></a>

How can one figure out which steps control network functioning? Metabolic control analysis (MCA) determines which enzymes control the steady flux through a metabolic pathway (Kacser and Burns, 1973; Heinrich and Rapoport, 1974; Westerhoff and Van Dam, 1987; Fell, 1992). The control of steady-state metabolic flux can be well distributed (and not necessarily uniformly) among many processes (Groen et al., 1982). MCA has been developed much less for dynamics; however, for signal transduction, the important feature appears to be the amplitude of a transient peak, the duration of signalling and the overall signal strength; steady states may not exist, or the steady-state levels may be irrelevant. Classical MCA therefore does not apply to signal transduction. We recently extended MCA to the dynamics of signal transduction, however (Hornberg et al., 2005). This revealed some principles, including that the dynamics of signal transduction must be determined by more than one process, and differently for the many characteristics of those dynamics. This suggests that control of signal transduction is spread almost equally over all components. Only detailed analysis of specific cases can show, however, whether control is as disperse as it can be in principle. The analysis of which proteins and reactions are in control of a signalling pathway is of vital importance not only for understanding of the system, but also for drug design, since it helps choosing potential drug targets according to the magnitude of their control on cell proliferation (Bakker et al., 1999; Cascante et al., 2002).

<a id='0cc75402-0ceb-494c-974e-cb42536aac29'></a>

Studies that combine quantitative experimentation and mathematical modelling have proven to describe the functioning of the EGFR pathway (Kholodenko et al., 1999), feedback circuitry (Asthagiri and Lauffenburger, 2001), MAPK signalling (Schoeberl et al., 2002) and the Wnt pathway (Lee et al., 2003). They have also predicted phenomena such as ultrasensitivity (Huang and Ferrell, 1996), learning (Bruggeman et al., 2000), bistability (Bhalla and Iyengar, 1999) and oscillatory behaviour (Kholodenko, 2000). Theoretical studies have elucidated principles of signalling networks (Heinrich et al., 2002), some of which have been confirmed experimentally (Hornberg et al., 2005). These studies have contributed much to the general understanding of

<a id='54a1465c-46c0-416f-b4e7-b93b336ab07c'></a>

the functioning of signalling networks, but there is still a lack of understanding of (i) which processes and proteins are most important for signalling and (ii) why certain genes are oncogenes or tumour suppressor genes, whereas other genes appear not to be important for the development of cancer.

<a id='7297da80-1bf6-4ef2-8546-5b30ff5f6ff1'></a>

We here apply the dynamic extension of MCA to the
MAPK pathway and calculate for its computer replica
how the control is distributed. The results are much less
random than expected, and may help explain oncogene
distributions.

<a id='d99da5b0-de69-4dee-bf39-b3f76b06c87d'></a>

## Results

A computer model of EGF-induced signal transduction

The computer replica of EGF-induced signalling through the MAPK cascade that we use here contains 148 molecular processes and 103 variable molecular species (Figure 1). It is an updated version of previous models (Kholodenko et al., 1999; Schoeberl et al., 2002) and should be close to containing the best available experimental data on the pathway (cf. Supplementary Tables 1 and 2): It describes signal transduction all the way from EGF binding at the cellular membrane to the phosphorylation of ERK. The molecular processes include association, dissociation, as well as covalent (de-)modification and degradation events and have all been described with mass-action kinetics. Signalling is initiated by binding of EGF to EGFR, followed by the dimerization and subsequent autophosphorylation of EGFR. Signal propagation involves either of the two routes, both leading to the activation of the small G-protein Ras. One route starts with the binding of the 'Src homology and collagen domain protein' (Shc) to the phosphorylated, ligand-bound, dimerized receptor followed by the binding of the growth factor receptor-binding protein 2 (Grb2). The other commences directly with the binding of Grb2. In both routes, the association of Grb2 with the complex that includes EGFR recruits Sos to the cytoplasmic surface of the membrane. The model also includes an elaborate description of the processes involved in the internalization and the degradation of the various receptor complexes (cf. Supplementary Table 1). The recruitment of Sos brings the latter in close proximity to its membrane-anchored target, that is, Ras. Contact between Sos and Ras leads to the activation of the latter through the formation of Ras-GTP. Ras-GTP dissociates from the receptor complex, which then dissociates further. The inactivation of Ras-GTP involves the activity of a GTPase-activating protein (GAP). Although the kinase by which Raf is phosphorylated is not known (the exact mechanism is subject to ongoing research and discussion), the model we used assumes that Raf phosphorylation is caused directly by a free Ras-GTP molecule. Phosphorylated Raf has intrinsic kinase activity and can phosphorylate MAPK/ERK kinase (MEK), which in its doubly phosphorylated form can phosphorylate ERK. Raf, MEK and ERK can be dephosphorylated by

<a id='c945e61a-3ef5-4251-9e05-dea643811aca'></a>

Oncogene

<!-- PAGE BREAK -->

<a id='771d9a4c-bfd6-4979-9c34-6dfec9d12973'></a>

Control of MAPK signalling
JJ Hornberg et al

<a id='072473f2-9199-4dc3-8eaf-697fec853982'></a>

<::logo: [NPG]npgA black circle with white letters "npg" in the center.::>

<a id='3518915a-8e1c-4e51-8eb2-312ea253d7d1'></a>

5535

<a id='1f471be1-4038-4b2e-9bb5-c9a6a0e35bf4'></a>

<::A complex biological pathway diagram showing interactions between various proteins and enzymes. The diagram starts with EGF and EGFR, leading to a cascade of phosphorylation, complex formation, and activation/deactivation steps, ultimately involving Ras, Raf, MEK, and ERK pathways. Key components and reactions include:

**Top Left:**
- EGF
- EGFR
- EGF-EGFR
- (EGF-EGFR)*2
- EGFideg
- EGFI
- EGFRI
- EGFRideg
- v13, v-6, v6, v61, v10, v60 (reaction labels)

**Top Middle:**
- ATP, ADP
- GAP
- (EGF-EGFR)*2-GAP
- (EGF-EGFRi*)*2
- (EGF-EGFR)*2deg
- v3, v7, v8, v14, v12, v62 (reaction labels)

**Central Pathway (leading from EGFR complexes):**
- Shc
- Pi
- (EGF-EGFR)*2-GAP-Shc
- ATP, ADP
- (EGF-EGFR)*2-GAP-Shc*
- Grb2
- Sos
- (EGF-EGFR)*2-GAP-Shc*-Grb2
- Shc*-Grb2
- (EGF-EGFR)*2-GAP
- Grb2Sos
- Sos
- Shc*-Grb2-Sos
- (EGF-EGFR)*2-GAP-Shc*-Grb2-Sos
- Ras-GDP
- (EGF-EGFR)*2-GAP-Shc*-Grb2-Sos-Ras-GTP
- Prot
- (EGF-EGFR)*2-GAP-Shc*-Grb2-Sos-Prot
- v22,69, v36, v23,70, v24,71, v39,82, v41,83, v32,79, v40, v33, v26,73, v31,78, v118 (reaction labels)

**Right Pathway (Grb2-Sos branch):**
- Grb2
- Sos
- (EGF-EGFR)*2-GAP-Grb2
- (EGF-EGFR)*2-GAP-Grb2-Sos
- Ras-GDP
- (EGF-EGFR)*2-GAP-Grb2-Sos-Ras-GDP
- Ras-GTP
- (EGF-EGFR)*2-GAP-Grb2-Sos-Ras-GTP
- v16,63, v37,81, v35, v17,64, v34,80, v18,65, v21,68, v19,66, v20,67 (reaction labels)

**Ras-GTP to ERK Pathway:**
- Ras-GTP
- Phosphatase1
- Raf
- Raf-Ras-GTP
- Raf-P'ase1
- P'ase1
- MEK
- MEK-Raf
- MEK-P
- MEK-P-Raf
- Raf*
- MEK-P-P'ase2
- Phosphatase2
- MEK-PP-P'ase2
- MEK-PP
- ERK
- ERK-MEK-PP
- ERK-P
- ERK-P-MEK-PP
- MEK-PP
- ERK-P-P'ase3
- ERK-PP-P'ase3
- ERK-PP
- Phosphatase3
- v30,77, v27,74, v29,76, v28,75, v42,84, v43,85, v44,86, v45,87, v46,88, v47,89, v51,93, v50,92, v49,91, v48,90, v52,94, v53,95, v54,96, v55,97, v59,101, v58,100, v57,99, v56,98 (reaction labels)

**Degradation Pathways:**
- (EGF-EGFR)*2-GAP-Shc*-Grb2-Sos-ERK-PP
- (EGF-EGFR)*2-GAP-Shc*-Grb2-Sos*deg ERK-PP
- v128,129, v144,147 (reaction labels)
- (EGF-EGFR)*2-GAP-Grb2-Sos-ERK-PP
- (EGF-EGFR)*2-GAP-Grb2-Sos deg ERK-PP
- v126,127, v143,146 (reaction labels)
: diagram::>

<a id='97782c56-5cc2-4ed4-b6d5-32f4d4b14b70'></a>

Figure 1 The biochemical scheme of the signal transduction network. Most of the molecular species, reactions that refer to internalized receptor-associated species, have not been depicted. The reaction numbers are depicted in grey. Some reactions have two reaction numbers: the second reaction number always refers to the internalized counterpart

<a id='347e7a69-ee8a-43d9-b340-0f12b0557ecd'></a>

various phosphatases (Millward et al., 1999; Todd et al.,
1999; Keyse, 2000); in the model, this is described in
terms of the different phosphatase activities, one for
each kinase. The model includes the negative feedback
loop from doubly phosphorylated ERK (ERK-PP) to
Sos. This causes the dissociation of Grb2-Sos from the
receptor complex (Buday et al., 1995; Dong et al., 1996;
Porfiri and McCormick, 1996). The model does not
account for different isoforms of proteins. This means
that isoform specificity (for instance, displayed by
different Raf or ERK proteins) cannot be considered
in this model.

<a id='611ff8b4-5b5e-4229-8370-b9d50919253e'></a>

In the absence of stimulation by EGF, the system is in a stable steady state, in which ERK is not phosphory-lated (for the other characteristics of this reference state, see Supplementary Table 2). The model distinguishes between two pools of ERK-PP: one is located freely in the cytoplasm and the other is associated with the internalized receptor. This 'internalized' ERK-PP makes up at most 1.2% of the total ERK~PP concentration. Figure 2 displays the computed transient profile of the total ERK-PP concentration, that is, the sum of the two pools. This transient profile qualitatively corresponds to experimental work describing the ERK phosphorylation kinetics (Hornberg et al., 2004). Upon addition of EGF at t=0, the total concentration of ERK-PP rapidly increases so as to attain ~50% of the total concentra-tion of ERK within ~5min. Then, the ERK-PP

<a id='e1517d77-31ae-415b-810f-aa89c499b43e'></a>

<::transcription of the content: chart::>
**Figure 2** The transient profile of ERK ~PP as a function of time upon the addition of EGF at time zero calculated with the kinetic model. The definitions of the three quantities that characterize the transient profile, that is, amplitude, duration and integrated response, are depicted.

Line chart titled 'The transient profile of ERK ~PP as a function of time upon the addition of EGF at time zero calculated with the kinetic model'.
X-axis: Time [min], ranging from 0 to 100.
Y-axis: ERK-PP [molecules/cell], ranging from 0 to 15 x 10^6.

Legend: [ERK-PP]t (solid line).

The chart shows a solid line representing ERK-PP concentration over time. It rapidly increases from 0 to a peak around 12 x 10^6 molecules/cell at approximately 5 minutes, then gradually decreases, reaching near zero by 80 minutes.

Annotations on the chart:
- 'amplitude (A)' is indicated at the peak of the solid line.
- 'integral (I) I = ∫[ERK-PP] dt' is shown as the area under the solid curve.
- A dashed horizontal line is labeled '10% of A', indicating 10% of the amplitude. The segment of the solid line above this dashed line is used to define 'duration (d)'.
::>

<a id='b05c08ac-1f24-4cf6-bddb-bcdfc812bfb0'></a>

concentration slowly decays to zero, passing 10% of
its maximal activation level at ~65 min.

<a id='33ef7d95-331d-474a-8e22-36b53aec823d'></a>

_Which processes are important and how important are they?_

<a id='3558d7b2-bd53-4a39-9b02-6622743df9a9'></a>

The time dependence of the activation of ERK is an
important determinant of the subsequent cellular
response, for example, it decides between cell division

<a id='77dd0a34-ae89-4dd5-823a-990178ce78c8'></a>

Oncogene

<!-- PAGE BREAK -->

<a id='7c36b76f-f495-40d7-a96f-3733e2954d44'></a>

<::logo: npg
npg
5536
Black circle with white text "npg" above a line and the number "5536"::>

<a id='371892c5-e9d8-4878-a694-b6d9567440ef'></a>

Control of MAPK signalling
---
JJ Hornberg et al

<a id='46584d5b-f5e3-45ed-8620-540aa9ead9d9'></a>

and differentiation (Marshall, 1995; Tombes et al., 1998). We focused on three characteristics of the transient activation profile of ERK (Figure 2). The first was the amplitude (A), defined as the maximal ERK-PP concentration that was attained. The second characteristic was the duration (d) of signalling, defined as the total time for which the ERK-PP concentration exceeded 10% of its amplitude. The third characteristic was the integrated response (I), defined as the time integral of the activated ERK concentration between time 0 and 100 min. This measure can be regarded as the total output of the pathway; for linear downstream kinetics, it would be proportional to the number of downstream molecules that are activated. Indeed, the time-integrated value of ERK activity upon fibronectin stimulation was shown to be directly proportional to the induced amount of DNA synthesis (Asthagiri et al., 2000).

<a id='6c2fd5ae-c26b-4f95-bbcf-c7d8d55c0a5f'></a>

We determined how important each of the 148 molecular processes was for each of these three characteristics, essentially by calculating how strongly the characteristic changed when the process was activated by 1%. The percentage change in that characteristic was then called the coefficient for the control of that characteristic by the process. The control coefficient C4, for instance, quantifies the control exercised by the receptor internalization process (process 7) on the amplitude (A). If for a 1% activation of process 7, the amplitude increases by 1%, then the amplitude follows precisely the activity of the process and the corresponding control coefficient is 1. If, however, the amplitude only increases by 0.3%, the control is less, although significant, as indicated by a control coefficient Cf of 0.3. (The actual quantification and definition of this control coefficient was performed more precisely, cf. Supplementary information.)

<a id='d807dea8-1119-4a01-859d-9ecd3038f11f'></a>

The entire set of control coefficients can be found in
Supplementary Table 3. The individual sums of the
control coefficients (calculated by a small perturbation)
on amplitude, duration and integrated response were in
accordance with the summation theorems we recently
discovered (Hornberg et al., 2005).

<a id='2ffd5366-98cf-410b-86cb-93f564692e09'></a>

*Most reactions in the network are not that important for signalling to ERK*

A paradigm of classical biochemistry was that pathways should have a single controlling step. This paradigm was never proven to be true. For signal transduction pathways, the theorems we recently discovered (Hornberg et al., 2005) replace the previous paradigm by a paradigm with a foundation: Total control should amount to a certain magnitude, but the control may well be distributed over many steps. This opens up the possibility that control is almost equally distributed over all steps in the pathway. To examine whether EGF-ERK signal transduction is indeed that complex, we display a histogram of the control coefficients on amplitude, duration and integrated response (Figure 3). It suggests that the maximum possible complexity is not attained in this pathway: calculated control was far from

<a id='2fd9cfa2-4b56-47eb-8d60-42f2e796c5f3'></a>

<::Figure 3: Histograms that depict the frequencies of the three types of control coefficients calculated for the differentially small perturbations. The figure consists of three sub-figures (a), (b), and (c).

(a) Histogram for the amplitude:
- Y-axis labeled "frequency" from 0 to 80.
- X-axis labeled "value of control coefficient on amplitude" ranging from -0.08 to 0.08.
- The majority of the bars are clustered around 0.00, with the two highest bars reaching approximately 75 and 60 on the frequency axis.

(b) Histogram for the duration:
- Y-axis labeled "frequency" from 0 to 80.
- X-axis labeled "value of control coefficient on duration" ranging from -0.8 to 0.8.
- The majority of the bars are clustered around 0.0, with the two highest bars reaching approximately 65 and 58 on the frequency axis.

(c) Histogram for the integrated response (also labeled as 'integrated output' in the x-axis):
- Y-axis labeled "frequency" from 0 to 80.
- X-axis labeled "value of control coefficient on integrated output" ranging from -1.2 to 1.2.
- The majority of the bars are clustered around 0.0, with the two highest bars reaching approximately 70 and 60 on the frequency axis.
: chart::>

<a id='5afdc87b-8548-4230-a134-cd5d440fe59c'></a>

uniformly distributed over all processes. Most reactions had a control coefficient that was very close to zero and only a small group of reactions exercised much control. This is a surprising result considering that there are 148 reactions that could have exercised much control, and, for each signalling characteristic, as many control coefficients.

<a id='2b8c0bfe-578a-451b-b90d-232b3e4a33c1'></a>

Oncogene

<!-- PAGE BREAK -->

<a id='17353cfa-b9f2-441b-8619-b087b2065ff3'></a>

Control of MAPK signalling
JJ Hornberg et al

<a id='a2ea0400-5ffb-4ae3-8b09-e5515b6f8fda'></a>

<::logo: NPG
npg
A black circular logo with white lowercase letters "npg" in the center.::>

<a id='024956d3-9e17-429b-967e-adf9b93539b2'></a>

_EGF-induced signalling to ERK: which reactions are in control?_

<a id='b038d343-102b-4275-9cee-7a09e020cbf6'></a>

For practical purposes, we here define a control coefficient to be 'substantial' if it is not smaller in absolute value than 10% of the largest control coefficient. Table 1 displays the 'substantial' positive and the 'substantial' negative control coefficients for control on the amplitude, the duration and the integrated response. For instance, with respect to the control on amplitude, only eight out of the 148 processes were found to display substantial control coefficients (five reactions with positive control and three with negative control). In Supplementary Figure S1, the control coefficients of Table 1 are depicted super-imposed on the biochemical scheme of the signalling network. The trend that becomes apparent is that many of the largest control coefficients are associated with reactions that involve Raf, MEK and ERK. This was irrespective of the system property for which the control distribution was calculated.

<a id='724f2cee-f854-4dc4-9c7a-2ba797019c94'></a>

In order to further classify processes that exert high
control, we simplified the extensive reaction scheme of
Figure 1 into a simpler 'textbook' type displayed in
Figure 4. We grouped reactions that are directly
involved in the same biochemical process. For example,
the biochemical process 'EGFR activation' included

<a id='9a5cb7d3-c155-464e-af9f-e7beb5321fa2'></a>

reaction 1 (i.e. EGF binds to EGFR), reaction 2 (EGFR
dimerization) and reaction 3 (EGFR phosphorylation).
In this way, each of the 148 reactions was assigned to
any of 13 different biochemical processes, that is (1)
EGFR activation, (2) recruitment of Shc, Grb2 and/or
Sos, (3) Ras activation, (4) Ras inactivation, (5) acti-
vation of Raf, (6) Raf dephosphorylation, (7) MEK
phosphorylation by Raf, (8) MEK dephosphorylation,
(9) ERK phosphorylation by MEK, (10) ERK depho-
sphorylation, (11) the negative feedback from ERK to
Sos, (12) internalization of EGFR-associated complexes
and (13) degradation reactions (for complete overview
of which reaction was assigned to which biochemical
process, see Supplementary Table 4). To calculate how
much control such a biochemical process exerts on the
amplitude, duration and integral of the ERK-PP profile
(signal output), we determined the impact control
coefficient (Kholodenko and Westerhoff, 1993) of each
of the 13 biological processes by taking the sum of the
control coefficients of all molecular reactions that were
assigned to each biochemical process. The impact
control coefficients were calculated for small perturba-
tions and the results, depicted in Figure 4 (cf.
Supplementary Table 5), show that most control resided
within only a small number of processes. 'Raf depho-
sphorylation' and 'MEK phosphorylation by Raf
exercised high control on all characteristics of the signal

<a id='e504fc87-77ae-4013-a75a-28b5de12167b'></a>

Table 1 The most substantial positive and the most substantial negative control coefficients on amplitude, duration and integrated response
<table id="4-1">
<tr><td id="4-2">V</td><td id="4-3">Reaction</td><td id="4-4" colspan="3">Small perturbation</td><td id="4-5" colspan="3">+ 50% perturbation</td><td id="4-6" colspan="3">-50% perturbation</td></tr>
<tr><td id="4-7"></td><td id="4-8"></td><td id="4-9">Amp</td><td id="4-a">Dur</td><td id="4-b">Int</td><td id="4-c">Amp</td><td id="4-d">Dur</td><td id="4-e">Int</td><td id="4-f">Amp</td><td id="4-g">Dur</td><td id="4-h">Int</td></tr>
<tr><td id="4-i">26</td><td id="4-j">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] + [Ras-GDP] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]</td><td id="4-k">0.006</td><td id="4-l">0.038</td><td id="4-m">0.070</td><td id="4-n">0.004</td><td id="4-o">0.026</td><td id="4-p">0.048</td><td id="4-q">0.013</td><td id="4-r">0.070</td><td id="4-s">0.130</td></tr>
<tr><td id="4-t">27</td><td id="4-u">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] + [Ras-GTP]</td><td id="4-v">0.021</td><td id="4-w">0.125</td><td id="4-x">0.236</td><td id="4-y">0.012</td><td id="4-z">0.089</td><td id="4-A">0.168</td><td id="4-B">0.075</td><td id="4-C">0.221</td><td id="4-D">0.403</td></tr>
<tr><td id="4-E">31</td><td id="4-F">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] + [Ras-GDP]</td><td id="4-G">-0.001</td><td id="4-H">0.138</td><td id="4-I">0.203</td><td id="4-J">-0.001</td><td id="4-K">0.128</td><td id="4-L">0.192</td><td id="4-M">-0.001</td><td id="4-N">0.151</td><td id="4-O">0.214</td></tr>
<tr><td id="4-P">42</td><td id="4-Q">[Raf*] + [Phosphatasel] ↔ [Raf*-Phosphatasel]</td><td id="4-R">-0.072</td><td id="4-S">-0.699</td><td id="4-T">-1.130</td><td id="4-U">-0.609</td><td id="4-V">-0.438</td><td id="4-W">-0.927</td><td id="4-X">-0.030</td><td id="4-Y">-1.249</td><td id="4-Z">-1.965</td></tr>
<tr><td id="4-10">43</td><td id="4-11">[Raf*-Phosphatasel] → [Raf] + [Phosphatasel]</td><td id="4-12">-0.015</td><td id="4-13">-0.146</td><td id="4-14">-0.235</td><td id="4-15">-0.013</td><td id="4-16">-0.098</td><td id="4-17">-0.159</td><td id="4-18">-0.017</td><td id="4-19">-0.283</td><td id="4-1a">-0.457</td></tr>
<tr><td id="4-1b">44</td><td id="4-1c">[MEK] + [Raf*] ↔ [MEK-Raf*]</td><td id="4-1d">0.044</td><td id="4-1e">0.640</td><td id="4-1f">0.924</td><td id="4-1g">0.019</td><td id="4-1h">0.570</td><td id="4-1i">0.820</td><td id="4-1j">0.815</td><td id="4-1k">0.667</td><td id="4-1l">1.212</td></tr>
<tr><td id="4-1m">46</td><td id="4-1n">[MEK-P]+[Raf*] ↔ [MEK-P-Raf*]</td><td id="4-1o">0.042</td><td id="4-1p">0.191</td><td id="4-1q">0.419</td><td id="4-1r">0.019</td><td id="4-1s">0.165</td><td id="4-1t">0.353</td><td id="4-1u">0.696</td><td id="4-1v">0.170</td><td id="4-1w">0.761</td></tr>
<tr><td id="4-1x">49</td><td id="4-1y">[MEK-PP-Phosphatase2] → [MEK-P] + [Phosphatase2]</td><td id="4-1z">-0.006</td><td id="4-1A">-0.453</td><td id="4-1B">-0.607</td><td id="4-1C">-0.006</td><td id="4-1D">-0.344</td><td id="4-1E">-0.450</td><td id="4-1F">-0.006</td><td id="4-1G">-0.720</td><td id="4-1H">-0.973</td></tr>
<tr><td id="4-1I">51</td><td id="4-1J">[MEK-P-Phosphatase2] → [MEK]+[Phosphatase2]</td><td id="4-1K">-0.002</td><td id="4-1L">-0.470</td><td id="4-1M">-0.440</td><td id="4-1N">-0.002</td><td id="4-1O">-0.355</td><td id="4-1P">-0.341</td><td id="4-1Q">-0.002</td><td id="4-1R">-0.686</td><td id="4-1S">-0.609</td></tr>
<tr><td id="4-1T">52</td><td id="4-1U">[ERK]+[MEK-PP] ↔ [ERK-MEK-PP]</td><td id="4-1V">0.001</td><td id="4-1W">0.202</td><td id="4-1X">0.172</td><td id="4-1Y">0.001</td><td id="4-1Z">0.161</td><td id="4-20">0.133</td><td id="4-21">0.001</td><td id="4-22">0.286</td><td id="4-23">0.254</td></tr>
<tr><td id="4-24">53</td><td id="4-25">[ERK-MEK-PP] → [ERK-P]+[MEK-PP]</td><td id="4-26">0.000</td><td id="4-27">0.184</td><td id="4-28">0.158</td><td id="4-29">0.000</td><td id="4-2a">0.119</td><td id="4-2b">0.103</td><td id="4-2c">0.000</td><td id="4-2d">0.402</td><td id="4-2e">0.342</td></tr>
<tr><td id="4-2f">54</td><td id="4-2g">[ERK-P]+[MEK-PP] ↔ [ERK-P-MEK-PP]</td><td id="4-2h">0.015</td><td id="4-2i">0.198</td><td id="4-2j">0.327</td><td id="4-2k">0.010</td><td id="4-2l">0.155</td><td id="4-2m">0.266</td><td id="4-2n">0.030</td><td id="4-2o">0.288</td><td id="4-2p">0.442</td></tr>
<tr><td id="4-2q">55</td><td id="4-2r">[ERK-P-MEK-PP]→[ERK-PP]+[MEK-PP]</td><td id="4-2s">0.066</td><td id="4-2t">-0.404</td><td id="4-2u">-0.207</td><td id="4-2v">0.038</td><td id="4-2w">-0.315</td><td id="4-2x">-0.181</td><td id="4-2y">0.699</td><td id="4-2z">-0.709</td><td id="4-2A">0.119</td></tr>
<tr><td id="4-2B">57</td><td id="4-2C">[ERK-PP-Phosphatase3] → [ERK-P]+[Phosphatase3]</td><td id="4-2D">-0.080</td><td id="4-2E">0.216</td><td id="4-2F">-0.091</td><td id="4-2G">-0.164</td><td id="4-2H">0.184</td><td id="4-2I">-0.123</td><td id="4-2J">-0.061</td><td id="4-2K">0.327</td><td id="4-2L">-0.071</td></tr>
<tr><td id="4-2M">59</td><td id="4-2N">[ERK-P-Phosphatase3] → [ERK] + [Phosphatase3]</td><td id="4-2O">0.000</td><td id="4-2P">-0.389</td><td id="4-2Q">-0.347</td><td id="4-2R">0.000</td><td id="4-2S">-0.335</td><td id="4-2T">-0.296</td><td id="4-2U">-0.001</td><td id="4-2V">-0.492</td><td id="4-2W">-0.440</td></tr>
<tr><td id="4-2X">74</td><td id="4-2Y">[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] + [Ras-GTPi]</td><td id="4-2Z">-0.005</td><td id="4-30">-0.043</td><td id="4-31">-0.090</td><td id="4-32">-0.005</td><td id="4-33">-0.037</td><td id="4-34">-0.075</td><td id="4-35">-0.006</td><td id="4-36">-0.052</td><td id="4-37">-0.112</td></tr>
<tr><td id="4-38">84</td><td id="4-39">[Rafi*] + [Phosphatasel] → [Rafi*-Phosphatasel]</td><td id="4-3a">0.000</td><td id="4-3b">-0.086</td><td id="4-3c">-0.088</td><td id="4-3d">0.000</td><td id="4-3e">-0.059</td><td id="4-3f">-0.060</td><td id="4-3g">-0.002</td><td id="4-3h">-0.167</td><td id="4-3i">-0.190</td></tr>
<tr><td id="4-3j">86</td><td id="4-3k">[MEK] + [Rafi*] ↔ [MEK-Rafi*]</td><td id="4-3l">0.001</td><td id="4-3m">0.106</td><td id="4-3n">0.110</td><td id="4-3o">0.001</td><td id="4-3p">0.103</td><td id="4-3q">0.108</td><td id="4-3r">0.000</td><td id="4-3s">0.109</td><td id="4-3t">0.112</td></tr>
<tr><td id="4-3u">93</td><td id="4-3v">[MEKi-P-Phosphatase2] → [MEK]+[Phosphatase2]</td><td id="4-3w">0.000</td><td id="4-3x">-0.089</td><td id="4-3y">-0.074</td><td id="4-3z">0.000</td><td id="4-3A">-0.068</td><td id="4-3B">-0.059</td><td id="4-3C">0.000</td><td id="4-3D">-0.126</td><td id="4-3E">-0.099</td></tr>
<tr><td id="4-3F">118</td><td id="4-3G">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[Prot] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Prot]</td><td id="4-3H">-0.007</td><td id="4-3I">-0.146</td><td id="4-3J">-0.216</td><td id="4-3K">-0.008</td><td id="4-3L">-0.122</td><td id="4-3M">-0.182</td><td id="4-3N">-0.007</td><td id="4-3O">-0.183</td><td id="4-3P">-0.270</td></tr>
<tr><td id="4-3Q">124</td><td id="4-3R">Prot</td><td id="4-3S">-0.001</td><td id="4-3T">-0.054</td><td id="4-3U">-0.077</td><td id="4-3V">-0.001</td><td id="4-3W">-0.047</td><td id="4-3X">-0.067</td><td id="4-3Y">-0.001</td><td id="4-3Z">-0.065</td><td id="4-40">-0.092</td></tr>
<tr><td id="4-41">140</td><td id="4-42">[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] → [(EGF-EG-FRi*)2deg]</td><td id="4-43">0.000</td><td id="4-44">-0.056</td><td id="4-45">-0.059</td><td id="4-46">0.000</td><td id="4-47">-0.054</td><td id="4-48">-0.056</td><td id="4-49">0.000</td><td id="4-4a">-0.058</td><td id="4-4b">-0.061</td></tr>
</table>

<a id='965e4227-2378-4ff3-9645-4d0dbcf83f0e'></a>

The control coefficients calculated with small and large perturbations ($\Delta p/p$ of $10^{-6}$, $+0.5$ and $-0.5$, respectively) are shown. The significantly positive and negative control coefficients are displayed in bold and italic, respectively

<a id='ddea0260-d89b-47b8-8b41-2edd3860b7c1'></a>

Oncogene

<a id='ec4def79-b17c-4f65-8c10-91d48169a151'></a>

5537

<!-- PAGE BREAK -->

<a id='ba2e36ae-a387-429b-87c6-28b1042c0411'></a>

<::logo: [Unidentifiable] npg 5538 A black circle with "npg" in white text, above a horizontal line and the number "5538".::>

<a id='750a0681-c896-4786-bac0-b2aff6c472d9'></a>

Control of MAPK signalling
JJ Hornberg et al

<a id='64be8336-1bed-4220-8313-9f04e00ae93f'></a>

<::
EGF
  ↓
EGFR ---0.00, 0.03, 0.03---> EGFR-P
  ↓
  0.00
  0.03
  0.06
  ↓
Shc
  ↓
Grb2
  ↓
Sos
  ↓
EGFR-P / Shc / Grb2 / Sos
  ↓                      ↓
  -0.02                  0.00
  -0.27                  0.00
  -0.43                  0.00
  ↓                      ↓
Internalization        Ras-GDP ---0.00, 0.28, 0.43---> Ras-GTP
  ↓                                ↑           ↓
  0.00                              0.00        0.01
  -0.17                             0.01
  -0.18
  ↓
Degradation


Ras-GTP ---0.02, 0.12, 0.21---> Raf ---0.09, 0.95, 1.47---> Raf-P
            ↑                     ↑
            -0.09
            -0.95
            -1.47
            ↓
            MEK ---0.08, 0.17, 0.44---> MEK-PP
            ↑
            -0.01
            -1.03
            -1.12
            ↓
            ERK --- -0.08, -0.17, -0.44---> ERK-PP
: chart::>

Figure 4 Control by biological processes. Each of the 148 reactions in the model was assigned to one of the 13 biological processes represented here by the drawn arrows. The numbers represent the control of that process on signal amplitude (top), duration (middle) and integrated response (lower). Control was calculated in terms of the 'impact control coefficient' of the biological processes (i.e. the sum of the control coefficients of the reactions involved in that process). This was performed for the control coefficients determined with the small perturbations (this figure) and by -50% and +50% perturbations (see Supplementary Figure S2)

<a id='e421fa33-c556-466e-86b6-61f657d6006a'></a>

output. The amplitude of signalling was also controlled by 'ERK phosphorylation by MEK' and 'ERK dephosphorylation', whereas signal duration and integrated output were further controlled by 'MEK dephosphorylation'.

<a id='ab87fc53-16c7-4fff-8463-d6810d4f938f'></a>

Since, in practice, most changes of activities are not small, we also calculated the control of the biological process of signal transduction from EGF to ERK-PP by using the control coefficients that were determined after -50 and +50% perturbations of the reaction rates (Supplementary Figure S2 and Supplementary Table 5). In either case, the process with the most control on either signalling characteristic was either 'Raf dephosphorylation' or 'MEK phosphorylation by Raf'. 'MEK dephosphorylation' also exerted relatively high control on signal duration and integrated response.

<a id='aefb9aa5-19a0-4487-aad0-d5732aad97db'></a>

And, only certain proteins are important
The control considered so far was that by molecular and
biochemical processes. This does not necessarily indicate

<a id='efd5916c-06dc-4d0b-a1c4-59c42c4a3dec'></a>

the importance of proteins. We also addressed the
question of how changes in the concentration of the
proteins (caused by e.g. changes in gene expression)
influenced signalling through the network. We calcu-
lated the fractional change in the three signalling
characteristics caused by a fractional change in the total
concentration of any protein (Kholodenko and Wes-
terhoff, 1993). This measure corresponds to the response
coefficient of MCA (Kacser and Burns, 1973). We have
calculated these three response coefficients for all
proteins in the network.

<a id='2c36fe3a-eae5-426f-9257-863a37a0b7b0'></a>

Table 2 shows the coefficients quantifying the responses of the three characteristics of signalling to ERK to changes in the concentrations of the proteins in the network. Again we define a 'substantial' response coefficient as that whose absolute value exceeded 10% of the highest response coefficient. Signalling duration and the integrated output were affected most by changes in the concentrations of Ras, MEK and ERK (positive effect) and the phosphatases 1, 2 and 3 (negative effect). When small changes in protein concentrations were applied, the amplitude was, surprisingly, sensitive solely to the concentration of ERK and its phosphatase. When large changes in protein concentrations were considered, the amplitude also became sensitive to an increase in the concentration of phosphatase 1 (negative effect) as well as to a decrease in the concentrations of Ras and MEK (positive effect). Changes in the concentrations of EGF, the adaptor proteins and Raf did not affect the output of MAPK signalling much.

<a id='134c580f-46ca-4aa0-bfea-c3696f936245'></a>

_Control of amplitude, duration and integrated response; is it all the same?_

We have shown how control on signalling amplitude, duration and integrated response is distributed over the processes in the network. An interesting question to address is whether reactions, which have high control on one of the three characteristics of signalling output, also tend to have a high control on the other two characteristics. In other words, are there reactions in the network that control all three characteristics of signalling to ERK to a high extent? To address this point, the values of the three types of control coefficients are displayed as a function of each other in Figure 5. Figure 5c shows that the reactions that had a high control on the duration of the ERK-PP signal also tended to have significant control on the integrated response of the ERK-PP profile, which is reflected by a relatively high correlation coefficient of R=0.88. This positive correlation between individual processes controlling the signal amplitude and those controlling the signal duration was expected intuitively and has also been shown for simple linear cascades (Heinrich et al., 2002; Hornberg et al., 2005). However, for simple cascades, high control on signal duration always coincided with a high control on amplitude. In the more complex signalling network under consideration here, these two control coefficients are no longer covariant, as is illustrated by a small correlation coefficient of R=0.07.

<a id='9a812b02-17b2-44b0-85dd-34ecdd73dd3a'></a>

Oncogene

<!-- PAGE BREAK -->

<a id='171bb018-3d8e-4edb-afb4-0dd55650b965'></a>

Control of MAPK signalling
JJ Hornberg et al
---

<a id='dbc9408d-4424-4942-baed-c94e56794059'></a>

<::logo: NPG
npg
A black circular logo with white lowercase letters "npg" in the center.::>

<a id='479c7ec0-c6ab-498c-93ea-583d0a8efb9c'></a>

5539

<a id='799b3342-d593-4dee-8c6c-3cedc6972b99'></a>

Table 2 Response coefficients
<table id="6-1">
<tr><td id="6-2"></td><td id="6-3" colspan="3">Small perturbation</td><td id="6-4" colspan="3">+ 50% perturbation</td><td id="6-5" colspan="3">-50% perturbation</td></tr>
<tr><td id="6-6"></td><td id="6-7">Amp</td><td id="6-8">Dur</td><td id="6-9">Int</td><td id="6-a">Amp</td><td id="6-b">Dur</td><td id="6-c">Int</td><td id="6-d">Amp</td><td id="6-e">Dur</td><td id="6-f">Int</td></tr>
<tr><td id="6-g">EGF</td><td id="6-h">0.00</td><td id="6-i">0.00</td><td id="6-j">0.00</td><td id="6-k">0.00</td><td id="6-l">0.00</td><td id="6-m">0.00</td><td id="6-n">0.00</td><td id="6-o">0.00</td><td id="6-p">0.00</td></tr>
<tr><td id="6-q">EGFR</td><td id="6-r">0.01</td><td id="6-s">0.17</td><td id="6-t">0.28</td><td id="6-u">0.00</td><td id="6-v">0.11</td><td id="6-w">0.20</td><td id="6-x">0.02</td><td id="6-y">0.27</td><td id="6-z">0.40</td></tr>
<tr><td id="6-A">Prot</td><td id="6-B">-0.02</td><td id="6-C">-0.32</td><td id="6-D">-0.49</td><td id="6-E">-0.02</td><td id="6-F">-0.25</td><td id="6-G">-0.37</td><td id="6-H">-0.01</td><td id="6-I">-0.51</td><td id="6-J">-0.78</td></tr>
<tr><td id="6-K">shc</td><td id="6-L">0.00</td><td id="6-M">-0.01</td><td id="6-N">0.00</td><td id="6-O">0.00</td><td id="6-P">-0.03</td><td id="6-Q">-0.03</td><td id="6-R">0.00</td><td id="6-S">0.02</td><td id="6-T">0.03</td></tr>
<tr><td id="6-U">Grb2</td><td id="6-V">0.00</td><td id="6-W">-0.01</td><td id="6-X">-0.01</td><td id="6-Y">0.00</td><td id="6-Z">-0.01</td><td id="6-10">-0.01</td><td id="6-11">0.00</td><td id="6-12">-0.01</td><td id="6-13">-0.01</td></tr>
<tr><td id="6-14">Sos</td><td id="6-15">0.00</td><td id="6-16">0.01</td><td id="6-17">0.02</td><td id="6-18">0.00</td><td id="6-19">0.01</td><td id="6-1a">0.01</td><td id="6-1b">0.00</td><td id="6-1c">0.02</td><td id="6-1d">0.03</td></tr>
<tr><td id="6-1e">grb2sos</td><td id="6-1f">0.00</td><td id="6-1g">-0.02</td><td id="6-1h">0.00</td><td id="6-1i">0.00</td><td id="6-1j">-0.02</td><td id="6-1k">-0.02</td><td id="6-1l">0.01</td><td id="6-1m">0.01</td><td id="6-1n">0.04</td></tr>
<tr><td id="6-1o">Ras-GDP</td><td id="6-1p">0.08</td><td id="6-1q">0.84</td><td id="6-1r">1.30</td><td id="6-1s">0.03</td><td id="6-1t">0.73</td><td id="6-1u">1.12</td><td id="6-1v">1.95</td><td id="6-1w">1.07</td><td id="6-1x">1.97</td></tr>
<tr><td id="6-1y">GAP</td><td id="6-1z">0.02</td><td id="6-1A">0.21</td><td id="6-1B">0.32</td><td id="6-1C">0.01</td><td id="6-1D">0.10</td><td id="6-1E">0.18</td><td id="6-1F">0.06</td><td id="6-1G">0.40</td><td id="6-1H">0.56</td></tr>
<tr><td id="6-1I">Raf</td><td id="6-1J">0.00</td><td id="6-1K">0.01</td><td id="6-1L">0.01</td><td id="6-1M">0.00</td><td id="6-1N">0.01</td><td id="6-1O">0.01</td><td id="6-1P">0.00</td><td id="6-1Q">0.02</td><td id="6-1R">0.03</td></tr>
<tr><td id="6-1S">Pl</td><td id="6-1T">-0.09</td><td id="6-1U">-0.95</td><td id="6-1V">-1.47</td><td id="6-1W">-1.25</td><td id="6-1X">-0.56</td><td id="6-1Y">-1.40</td><td id="6-1Z">-0.03</td><td id="6-20">-1.64</td><td id="6-21">-2.57</td></tr>
<tr><td id="6-22">MEK</td><td id="6-23">0.05</td><td id="6-24">0.90</td><td id="6-25">1.24</td><td id="6-26">0.02</td><td id="6-27">0.88</td><td id="6-28">1.18</td><td id="6-29">1.14</td><td id="6-2a">0.85</td><td id="6-2b">1.49</td></tr>
<tr><td id="6-2c">P2</td><td id="6-2d">-0.01</td><td id="6-2e">-1.03</td><td id="6-2f">-1.12</td><td id="6-2g">-0.01</td><td id="6-2h">-0.70</td><td id="6-2i">-0.76</td><td id="6-2j">-0.01</td><td id="6-2k">-1.94</td><td id="6-2l">-2.08</td></tr>
<tr><td id="6-2m">ERK</td><td id="6-2n">1.91</td><td id="6-2o">0.70</td><td id="6-2p">2.74</td><td id="6-2q">1.91</td><td id="6-2r">0.53</td><td id="6-2s">3.15</td><td id="6-2t">1.85</td><td id="6-2u">1.18</td><td id="6-2v">1.94</td></tr>
<tr><td id="6-2w">P3</td><td id="6-2x">-0.94</td><td id="6-2y">-0.49</td><td id="6-2z">-1.67</td><td id="6-2A">-1.02</td><td id="6-2B">-0.53</td><td id="6-2C">-1.35</td><td id="6-2D">-0.93</td><td id="6-2E">-0.47</td><td id="6-2F">-2.10</td></tr>
</table>
The relative importance of the concentration of each protein (or protein complex) for the signalling amplitude, duration and integrated response
was calculated with small (actual response coefficient) and large (to mimic changes in gene expression) perturbations ($\Delta p/p$ of $10^{-6}$, $+0.5$ and $-0.5$,
respectively). The substantially positive and negative response coefficients are displayed in bold and italic, respectively

<a id='8b180c0b-69ca-468d-a2d1-ca7a14d8c771'></a>

_Large versus small perturbations_

Above, we calculated the control coefficients by perturbing the rate constants only very mildly. We also investigated whether the size of the perturbation affected the distribution of control over all reactions. We found that the magnitude of the control coefficients was affected by the size of the perturbation, but, importantly, the order in which the processes were ranked on the basis of their control coefficients did not change (cf. Supplementary Figure S3).

<a id='8e71ec0e-4224-4c68-bdc7-6bd8f174adaf'></a>

## Discussion
Most alterations that cause oncogenic transformation occur in components of signal transduction pathways that control key cellular processes such as cell division, apoptosis, angiogenesis and cell adhesion (Hanahan and Weinberg, 2000). The growing knowledge of how signalling proteins function and interact with each other has enabled us to draw maps of large networks, and has at the same time overwhelmed us with its enormous complexity. Complete understanding of signalling is therefore a difficult task, and it cannot be attained on the basis of interaction maps alone.

<a id='5c3ed557-76df-4d7d-a908-4d6a1b017893'></a>

In this study, we have applied control analysis to a detailed kinetic model of EGF-induced MAPK signalling (Schoeberl et al., 2002), which plays a pivotal role in the development of cancer. Some components of the MAPK network are well-known oncogenes, such as *Ras* and *Raf*, causing the pathway to be constitutively active in tumour cells (Bos, 1989; Hoshino et al., 1999; Davies et al., 2002), and have therefore been taken to be promising targets for rationalized therapies against cancer (Sebolt-Leopold, 2000). For each of the 148 processes in the network, we calculated to what extent it controls the output of the MAPK pathway, that is, the concentration of ERK-PP. Experimental studies have

<a id='ca0f4970-b97a-456f-b725-c6ce2412ba0c'></a>

shown that the time profile of ERK phosphorylation is essential for which response is evoked (Marshall, 1995; Tombes et al., 1998; Cook et al., 1999). Three metrics that together describe the shape of the transient ERK-PP time profile were analysed, that is, its (i) amplitude, (ii) duration and (iii) integrated output (Hornberg et al., 2005). Most reactions in the network do not control these characteristics at all (or to a very small extent). Although this may be a striking result (why would there be so many reactions if they do not control the output?), it is important information for clinicians and researchers alike, because not many reactions may be modulated in order to change the output. The next step is to identify those reactions.

<a id='1593419b-dd48-41da-bcfe-b890ae7e6b71'></a>

Which reactions are in control? The reactions with the highest control coefficients involved binding of Raf, MEK and ERK to each other and to their respective phosphatases and the (de-)phosphorylation reactions in which these proteins were involved. We classified all 148 reactions into 13 groups of 'biological processes' (cf. Figure 4 and Supplementary Figure S2). The processes that highly controlled all characteristics of the ERK-PP profile (amplitude, duration and integrated response) were 'MEK phosphorylation by Raf' and 'Raf dephosphorylation'. The activity of Raf is thus identified as important for ERK phosphorylation. This is in accordance with the experimentally verified claim that Raf is a potent oncogene (Rapp et al., 1983; Magnuson et al., 1994; Davies et al., 2002). Total malignant behaviour is of course controlled by multiple pathways (Hahn et al., 1999; Hanahan and Weinberg, 2000; Vogelstein and Kinzler, 2004). However, a process such as cell cycle progression can, although controlled by multiple pathways, very well be affected by a mutation in a single oncogene. Since signalling to ERK contributes to cell cycle progression and is known to play an important role in the development of cancer (Lewis et al., 1998; Hoshino et al., 1999), cells that acquire a mutation in a gene within the MAPK pathway will only attain a

<a id='aa422408-bc46-433f-a452-27ae1def7407'></a>

Oncogene

<!-- PAGE BREAK -->

<a id='a9be06d0-d8eb-451e-a777-137fc7c78407'></a>

<::logo: [npg]
npg
Black circular logo with white text "npg" and a horizontal line underneath::>

<a id='ffd890f9-3df8-4838-a356-0083b0ae7a9d'></a>

Control of MAPK signalling
JJ Hornberg et al

<a id='5105c33d-ceea-4f7e-83fc-2ddbb66a3fb5'></a>

5540

<a id='5ee3694c-c585-45ac-9570-b8630362b3d8'></a>

<::chart: a) Scatter plot with 'control coefficients on duration' on the y-axis (ranging from -0.8 to 0.8) and 'control coefficients on amplitude' on the x-axis (ranging from -0.08 to 0.08). The plot shows several data points and a dashed regression line with the equation y = 2.74x + 0.007 and R² = 0.08. b) Scatter plot with 'control coefficients on integral' on the y-axis (ranging from -1.2 to 1.2) and 'control coefficients on amplitude' on the x-axis (ranging from -0.08 to 0.08). The plot shows several data points and a dashed regression line with the equation y = 7.49x + 0.007 and R² = 0.33. c) Scatter plot with 'control coefficients on integral' on the y-axis (ranging from -1.2 to 1.2) and 'control coefficients on duration' on the x-axis (ranging from -0.8 to 0.8). The plot shows several data points and a dashed regression line with the equation y = 1.25x + 0.002 and R² = 0.88. Figure 5 Correlations between control coefficients on the three signalling characteristics: (a) signal duration and integrated response, (b) signal duration and signal amplitude and (c) signal amplitude and integrated response. In each case, regression lines are depicted (dashed lines), and their linear function and the R²-value are shown
::>

<a id='b2ccb451-ef99-4180-8ba3-7b2d8334baf0'></a>

growth advantage if the mutation is in a gene that is actually important for signalling to ERK. Hence, the fact that Raf is important for ERK phosphorylation is a plausible explanation for why cells with mutations in _Raf_ attain a growth advantage.

<a id='788b8226-fdb4-4ecc-9e35-b98c72857578'></a>

Additionally, we found 'MEK dephosphorylation' to
have high control on the duration and integrated
output, and 'MEK phosphorylates ERK' on the

<a id='33f16c5d-9d20-485c-a709-54a77acb5ae2'></a>

amplitude. MEK has not been identified as an oncogene.
However, expression of genetically mutated constitu-
tively active MEK is sufficient to cause cellular
transformation (Mansour et al., 1994).

<a id='da9fad7c-80ff-44b8-86b5-f21980178464'></a>

Although most reactions with high control are associated with Raf, or for duration and integrated output also with MEK, the total control was distributed over more than just these processes. Reactions that lead to the internalization of EGFR and EGFR-associated complexes exert negative control (4-5 times less than the most important reactions) on duration and integrated output. This means that, even though signalling from EGFR continues after internalization (Haugh et al., 1999; Oksvold et al., 2001), a change in the rate of internalization still affects the output of ERK signalling, possibly because internalized EGFR is exclusively targeted for degradation.

<a id='2ae2e3d5-a233-4ea3-8f48-d1bbf47b5a9b'></a>

Comparison of the control we calculated from the known molecular properties with experimental findings also leads to more research avenues. EGFR activation hardly exerted any control. Yet, constitutively active mutant receptors are commonly expressed in various human tumours (Pedersen et al., 2001). As EGFR represents the starting point of distinct signalling pathways (Carpenter, 2000), a plausible explanation might be that the growth advantage caused by such mutations is not mediated via signalling to ERK. The well-known oncogene *Ras* is at a branch point of an array of signalling pathways (Campbell et al., 1998). Although we do find that reactions that involve the activation and inactivation of Ras exert control on ERK signalling duration (and integrated output), this might explain why these processes are 4–5 times less important for signalling to ERK than Raf activity, Raf dephosphorylation or MEK dephosphorylation. A further inspiring result is that a reaction that was thought to inactivate signalling to ERK, that is, the inactivation of Ras by GAP, had positive control on the duration and integrated response. This result clearly shows the usefulness of calculations for comprehending the sometimes anti-intuitive behaviour of complex networks, and provides an interesting topic for further research.

<a id='8039e04a-7448-421d-b1ee-4f1dc3ccb9f0'></a>

A general issue that often emerges when analysing a model (either an experimental or a computational one) of a large and complex biological system is the fact that reality is more complex than the model. Intrinsic simplifications and assumptions often have to be made, since the available information on the system is not always complete. The model of the EGF-induced MAPK signalling network we analysed here, although already elaborate with 148 reactions, is not complete yet and will require continuous updates wherever possible. These may include specificity of different isoforms of components of the network (e.g. ERK1 and ERK2), additional feedback loops, the spatial resolution (e.g. different cellular compartments), the role of scaffold proteins (e.g. KSR), the effect of multiple phosphoryla- tion and dephosphorylation events on the same protein (e.g. Raf), diffusion, etc. Such updates could have implications for the values of the reported control coefficients. For some simplifications currently in the

<a id='9ce9de12-2fbe-4fea-882c-259375454a59'></a>

Oncogene

<!-- PAGE BREAK -->

<a id='c59cc1d1-0279-4552-b63b-51b3f1e75ee8'></a>

Control of MAPK signalling
JJ Hornberg et al
___

<a id='0e8e6708-0379-4ae9-bc56-16f2010109d3'></a>

<::logo: [npg]
npg
The logo features the letters "npg" in white, enclosed within a solid black circular shape.::>

<a id='614b3259-0807-4758-9d93-a6047b19f5e1'></a>

model, we predict that they are not likely to affect the control distribution. For instance, the activation of Raf is modelled as a one-step process, whereas in reality more than one step is involved. Since one can agglomerate subprocesses into a module process (Brug- geman et al., 2002), no implications are expected for the control distribution we report here. In a more detailed model, control exercised by the module 'Raf activation' will be distributed over the subprocesses. For other simplifications, it is difficult to predict how they affect the control distribution. For instance the action of feedback loops, such as the upregulation of MAPK phosphatases or Sprouty, is likely to affect the steady- state ERK-PP concentration. How the control distribu- tion would be affected by the fact that the participating proteins are not homogeneously distributed over the cell is also unclear. As a result of recruitment of proteins from the cytosol to the membrane, they may become highly concentrated on a 2D surface (Kholodenko et al., 2000). With increasing quantitative information, it should become possible to incorporate such issues into the model. However, the current model is, to our knowledge, the most complete and detailed model of this system available at present, and it reproduces reality well (Periwal and Szallasi, 2002). The fact that we found that most reactions of this complex net- work are not important for the output of the system suggests that the system displays a certain unexpected robustness and, hence, that many simplifications (reac- tions that are not in the model but do function in reality) may not affect the outcome nor our conclusions to a large extent.

<a id='33a953ad-7ab3-4b5c-a175-3524f89179b6'></a>

The insights gained on the control distribution seem largely independent of what characteristic of the dynamic ERK-PP time profile is analysed. For all three processes, control is distributed and not confined to one process. The processes that are most important for the integrated output are the same reactions that are most important for the duration and also tend to control the amplitude.

<a id='9fcfeefa-36b1-4351-8263-bcf974ada4bb'></a>

Also, the effects of changes in the concentrations of signal transduction proteins, such as caused by over-expression or 'silencing', were examined. We found that ERK-PP hardly responded to changes in the concentrations of either EGF, or the adaptor proteins She and Grb2, or Sos or Raf. Thus, while the ERK-PP time profile strongly depended on the activity of Raf and on Raf dephosphorylation, it was certainly not limited by expression of Raf.

<a id='a0b55c1b-4c48-4c33-b2ea-93ce419bc6fb'></a>

In summary, we have determined which reactions
in the complex EGF-induced MAPK network are
important and which are not. This study reveals for
the first time how signalling output is controlled in such
a large-scale complex network. We found the Raf
protein to be involved in the processes that were
identified as important with respect to the amplitude,
duration and integrated response of the signalling
output. Control analysis of accurate mathematical
models is a promising tool for the discovery of a new
category of drug targets (Bakker et al., 1999; Cascante
et al., 2002) and, as shown here, also for the under-

<a id='295d73dc-f89d-41c1-bc48-8c85781a95e8'></a>

standing and prediction of the functioning of complex signalling networks.

<a id='9446d341-0ec1-40cf-8422-9995c64d53d1'></a>

## Materials and methods

The original kinetic model of EGF-induced signalling through the MAPK cascade (Schoeberl et al., 2002) was updated (cf. Supplementary Tables 1 and 2 and www.mpi-magdeburg.mpg.de/people/schoeberl/schoeberl.html) and implemented in Mathematica 5.0 (Wolfram Research Inc., Mathematica, Version 5.0, Champaign, IL, USA; cf. www.siliconcell.net for the model).

<a id='f8507b4a-96e4-4e8b-b327-a65c01205ef1'></a>

The control and response coefficients were calculated with a fractional change in the parameter values Δp/p of 1 × 10⁻⁶ (d lnp), -0.5 and +0.5. All parameter changes were applied at t = 0 (which is the time point of EGF administration), to allow for a fair comparison with the reference model. As part of the theory, MCA embodies summation theorems of control coefficients. Summation theorems relate the sum of all the control coefficients on a certain systemic property to a constant value. We recently derived the following laws for the control of signal transduction (Hornberg et al., 2005):

<a id='2ff979d0-e605-406f-bfd0-6f950073d956'></a>

$$\sum_{i=1}^{n} C_i^A = 0, \sum_{i=1}^{n} C_i^d = -1, \text{ and } \sum_{i=1}^{n} C_i^I = -1.$$

<a id='12d48a44-a87f-49e8-8a3e-9c2cc2ea5450'></a>

The control coefficients (denoted by C) quantify the extent to which a characteristic of the dynamic time profile (such as the signalling amplitude A, the duration d or the integrated output I) is controlled by the activities of all the n processes I, that is,
$C_i^A = \frac{d\log(A)}{d\log(a_i)} = \frac{dA/A}{da_i/a_i}$, where $a_i$ is any factor multiplying both the forward and the reverse rate of process i (Westerhoff and Van Dam, 1987). The above summation laws dictate that these control coefficients sum to constant values: The sum of all control coefficients on the amplitude of signalling always equals 0. This implies that all reactions of the network with positive control (such as activating processes catalysed by kinases) are exactly as important for amplitude as all reactions with negative control (such as inactivating processes catalysed by phosphatases). All control coefficients on the duration of signalling and the integrated response must sum to -1. This implies that the inactivating reactions (which cause shorter duration) exert more control on these properties than activating reactions (which cause longer duration) (Heinrich et al., 2002; Hornberg et al., 2005). The summation theorems are strictly only valid for control coefficients calculated for very small changes in the activities of the processes.

<a id='217af5aa-d96a-4b26-973e-29ec82ade35d'></a>

Abbreviations
EGF, epidermal growth factor; EGFR, EGF receptor; ERK,
extracellular signal-regulated kinase; ERK-PP, doubly phos-
phorylated ERK; Grb2, growth factor receptor binding
protein 2; MAPK, mitogen-activated protein kinase; MCA,
metabolic control analysis; MEK, MAPK/ERK kinase; Shc,
Src homology and collagen domain protein.

<a id='9068ce14-f362-4cb3-8933-e59a40ebe028'></a>

## Acknowledgements
We thank Jan Lankelma for stimulating discussions. This work was partly sponsored by a joint grant of the Netherlands Organization for Scientific Research (NWO) and the German Research Foundation (DFG) to stimulate collaborations between Dutch and German graduate schools.

<a id='75280f21-4616-44a0-9c0c-62aa511a448f'></a>

Oncogene

<a id='fa9e15f7-5d35-47ab-8894-77861d605013'></a>

5541

<!-- PAGE BREAK -->

<a id='7aff86ba-e326-4ad0-aff0-6ca75e4bdeb9'></a>

<::logo: [NPG]npgA black circle with the letters "npg" in white, lowercase text::>

<a id='cc329ee3-f372-4597-afd4-e1367f71511a'></a>

Control of MAPK signalling JJ Hornberg et al

<a id='f0f10633-9487-4ef6-a634-43505c25dcb7'></a>

--- 5542

<a id='36f07530-6e0c-4176-bf32-5e3df23bd016'></a>

References

Asthagiri AR and Lauffenburger DA. (2001). Biotechnol. Prog., 17, 227-239.
Asthagiri AR, Reinhart CA, Horwitz AF and Lauffenburger DA. (2000). J. Cell Sci., 113 (Partt 24), 4499-4510.
Bakker BM, Michels PA, Opperdoes FR and Westerhoff HV. (1999). J. Biol. Chem., 274, 14551-14559.
Bhalla US and Iyengar R. (1999). Science, 283, 381-387.
Bos JL. (1989). Cancer Res., 49, 4682-4689.
Bruggeman F, Westerhoff H, Hoek J and Kholodenko B. (2002). J. Theor. Biol., 218, 507.
Bruggeman FJ, van Heeswijk WC, Boogerd FC and Westerhoff HV. (2000). Biol. Chem., 381, 965-972.
Buday L, Warne PH and Downward J. (1995). Oncogene, 11, 1327-1331.
Campbell SL, Khosravi-Far R, Rossman KL, Clark GJ and Der CJ. (1998). Oncogene, 17, 1395-1413.
Carpenter G. (2000). BioEssays, 22, 697-707.
Cascante M, Boros LG, Comin-Anduix B, de Atauri P, Centelles JJ and Lee PW. (2002). Nat. Biotechnol., 20, 243-249.
Cobb MH. (1999). Prog. Biophys. Mol. Biol., 71, 479-500.
Cook SJ, Aziz N and McMahon M. (1999). Mol. Cell. Biol., 19, 330-341.
Davies H, Bignell GR, Cox C, Stephens P, Edkins S, Clegg S, Teague J, Woffendin H, Garnett MJ, Bottomley W, Davis N, Dicks E, Ewing R, Floyd Y, Gray K, Hall S, Hawes R, Hughes J, Kosmidou V, Menzies A, Mould C, Parker A, Stevens C, Watt S, Hooper S, Wilson R, Jayatilake H, Gusterson BA, Cooper C, Shipley J, Hargrave D, Pritchard-Jones K, Maitland N, Chenevix-Trench G, Riggins GJ, Bigner DD, Palmieri G, Cossu A, Flanagan A, Nicholson A, Ho JW, Leung SY, Yuen ST, Weber BL, Seigler HF, Darrow TL, Paterson H, Marais R, Marshall CJ, Wooster R, Stratton MR and Futreal PA. (2002). Nature, 417, 949-954.
Dong C, Waters SB, Holt KH and Pessin JE. (1996). J. Biol. Chem., 271, 6328-6332.
Fell DA. (1992). Biochem. J., 286, 313-330.
Groen AK, Wanders RJ, Westerhoff HV, van der Meer R and Tager JM. (1982). J. Biol. Chem., 257, 2754-2757.
Hahn WC, Counter CM, Lundberg AS, Beijersbergen RL, Brooks MW and Weinberg RA. (1999). Nature, 400, 464-468.
Hanahan D and Weinberg RA. (2000). Cell, 100, 57-70.
Haugh JM, Huang AC, Wiley HS, Wells A and Lauffenburger DA. (1999). J. Biol. Chem., 274, 34350-34360.
Heinrich R, Neel BG and Rapoport TA. (2002). Mol. Cell, 9, 957-970.
Heinrich R and Rapoport TA. (1974). Eur. J. Biochem., 42, 89-95.
Hornberg JJ, Bruggeman FJ, Binder B, Geest CR, Bij de Vaate AJM, Lankelma J, Heinrich R and Westerhoff HV. (2005). FEBS J., 272, 244-258.
Hornberg JJ, Tijssen MR and Lankelma J. (2004). Eur. J. Biochem., 271, 3905-3913.
Hoshino R, Chatani Y, Yamori T, Tsuruo T, Oka H, Yoshida O, Shimada Y, Ari-i S, Wada H, Fujimoto J and Kohno M. (1999). Oncogene, 18, 813-822.

<a id='d1c2c5df-6dfa-4905-a16e-a5190760f910'></a>

Huang CY and Ferrell Jr JE. (1996). Proc. Natl. Acad. Sci. USA, **93**, 10078-10083.
Kacser H and Burns JA. (1973). Symp. Soc. Exp. Biol., **27**, 65-104.
Keyse SM. (2000). Curr. Opin. Cell Biol., **12**, 186-192.
Kholodenko BN and Westerhoff HV. (1993). FEBS Lett., **320**, 71-74.
Kholodenko BN. (2000). Eur. J. Biochem., **267**, 1583-1588.
Kholodenko BN, Demin OV, Moehren G and Hoek JB. (1999). J. Biol. Chem., **274**, 30169-30181.
Kholodenko BN, Hoek JB and Westerhoff HV. (2000). Trends Cell Biol., **10**, 173-178.
Lee E, Salic A, Kruger R, Heinrich R and Kirschner MW. (2003). *pLoS Biol.*, **1**, e10.
Lewis TS, Shapiro PS and Ahn NG. (1998). Adv. Cancer Res., **74**, 49-139.
Magnuson NS, Beck T, Vahidi H, Hahn H, Smola U and Rapp UR. (1994). *Semin. Cancer Biol.*, **5**, 247-253.
Mansour SJ, Matten WT, Hermann AS, Candia JM, Rong S, Fukasawa K, Vande Woude GF and Ahn NG. (1994). *Science*, **265**, 966-970.
Marshall CJ. (1995). *Cell*, **80**, 179-185.
Millward TA, Zolnierowicz S and Hemmings BA. (1999). *Trends Biochem. Sci.*, **24**, 186-191.
Oksvold MP, Skarpen E, Wierod L, Paulsen RE and Huitfeldt HS. (2001). *Eur. J. Cell Biol.*, **80**, 285-294.
Pagès G, Lenormand P, L'Allemain G, Chambard JC, Meloche S and Pouyssegur J. (1993). *Proc. Natl. Acad. Sci. USA*, **90**, 8319-8323.
Pedersen MW, Meltorn M, Damstrup L and Poulsen HS. (2001). *Ann. Oncol.*, **12**, 745-760.
Periwal V and Szallasi Z. (2002). *Nat. Biotechnol.*, **20**, 345-346.
Porfiri E and McCormick F. (1996). *J. Biol. Chem.*, **271**, 5871-5877.
Rapp UR, Goldsborough MD, Mark GE, Bonner TI, Groffen J, Reynolds Jr FH and Stephenson JR. (1983). *Proc. Natl. Acad. Sci. USA*, **80**, 4218-4222.
Schoeberl B, Eichler-Jonsson C, Gilles ED and Muller G. (2002). *Nat. Biotechnol.*, **20**, 370-375.
Schuster R and Holzhutter HG. (1995). *Eur. J. Biochem.*, **229**, 403-418.
Sebolt-Leopold JS. (2000). *Oncogene*, **19**, 6594-6599.
Snoep JL and Westerhoff HV. (2005). *Curr. Genomics*, **5**, 687-697.
Teusink B, Passarge J, Reijenga CA, Esgalhado E, van der Weijden CC, Schepper M, Walsh MC, Bakker BM, van Dam K, Westerhoff HV and Snoep JL. (2000). *Eur. J. Biochem.*, **267**, 5313-5329.
Todd JL, Tanner KG and Denu JM. (1999). *J. Biol. Chem.*, **274**, 13271-13280.
Tombes RM, Auer KL, Mikkelsen R, Valerie K, Wymann MP, Marshall CJ, McMahon M and Dent P. (1998). *Biochem. J.*, **330**, 1451-1460.
Treisman R. (1996). *Curr. Opin. Cell Biol.*, **8**, 205-215.
Vogelstein B and Kinzler KW. (2004). *Nat. Med.*, **10**, 789-799.
Westerhoff HV and Van Dam K. (1987). *Thermodynamics, Control of Biological Free-energy Transduction*. Elsevier: Amsterdam.

<a id='838950a9-3458-4412-b363-9f2d865fce99'></a>

Supplementary Information accompanies the paper on Oncogene website (http://www.nature.com/onc)

<a id='2d3c2d73-7739-4f7b-887d-3122f4b7cb54'></a>

Oncogene
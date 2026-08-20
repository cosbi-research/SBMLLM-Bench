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

# Supplementary materials

<a id='993fe137-5228-4246-808d-36506a924aa4'></a>

Supplementary Table 1: reactions and rate equations

<a id='42c93be3-e09a-4fec-aa59-9d3c108cb4cc'></a>

<table><thead><tr><th>v</th><th>reactions</th><th>rate equations</th></tr></thead><tbody><tr><td>1</td><td>[EGFR]+[EGF] → [EGF-EGFR]</td><td>k1 * c(1) * c(2) -kd1 * c(3)</td></tr><tr><td>2</td><td>[EGF-EGFR]+[EGF-EGFR] → [(EGF-EGFR)2]</td><td>k2 * c(3) * c(3) -kd2 * c(4)</td></tr><tr><td>3</td><td>[(EGF-EGFR)2] → [(EGF-EGFR*)2]</td><td>k3 * c(4) * 1 -kd3 * c(5)</td></tr><tr><td>4</td><td>[(EGF-EGFR*)2-GAP-Grb2]+[Prot] → [(EGF-EGFR*)2-GAP-Grb2-Prot]</td><td>k4 * c(23) * c(12) -kd4 * c(7)</td></tr><tr><td>5</td><td>[(EGF-EGFR*)2-GAP-Grb2-Prot] → [(EGF-EGFRi*)2-GAP-Grb2]+[Proti]</td><td>k5 * c(18) * c(9) -kd5 * c(7)</td></tr><tr><td>6</td><td>[EGFR] → [EGFRI]</td><td>k6 * c(2) * 1 -kd6 * c(6)</td></tr><tr><td>7</td><td>[(EGF-EGFR*)2] → [(EGF-EGFRi*)2]</td><td>k6 * c(5) * 1 -kd6 * c(8)</td></tr><tr><td>8</td><td>[(EGF-EGFR*)2]+[GAP] → [(EGF-EGFR*)2-GAP]</td><td>k8 * c(5) * c(14) -kd8 * c(15)</td></tr><tr><td>9</td><td>[(EGF-EGFR*)2-GAP] → [(EGF-EGFRI*)2-GAP]</td><td>k6 * c(23) * 1 -kd6 * c(18)</td></tr><tr><td>10</td><td>[EGFRI]+[EGFi] → [EGF-EGFRI]</td><td>k10b * c(6) * c(16) -kd10 * c(10)</td></tr><tr><td>11</td><td>[EGF-EGFRi]+[EGF-EGFRi] → [(EGF-EGFRI)2]</td><td>k2 * c(10) * c(10) -kd2 * c(11)</td></tr><tr><td>12</td><td>[(EGF-EGFRI)2] → [(EGF-EGFRI*)2]</td><td>k3 * c(11) * 1 -kd3 * c(8)</td></tr><tr><td>13</td><td>→ [EGFR]</td><td>k13 * 1 * 1 -kd13 * c(2)</td></tr><tr><td>14</td><td>[(EGF-EGFRI*)2]+ [GAP] → [(EGF-EGFRI*)2-GAP]</td><td>k8 * c(8) * c(14) -kd8 * c(17)</td></tr><tr><td>15</td><td>[Proti] → [Prot]</td><td>k15 * c(9) * 1 -kd15 * c(12)</td></tr><tr><td>16</td><td>[(EGF-EGFR*)2-GAP]+[Grb2] → [(EGF-EGFR*)2-GAP-Grb2]</td><td>k16 * c(22) * c(15) -kd63 * c(23)</td></tr><tr><td>17</td><td>[(EGF-EGFR*)2-GAP-Grb2]+[Sos] → [(EGF-EGFR*)2-GAP-Grb2-Sos]</td><td>k17 * c(24) * c(23) -kd17 * c(25)</td></tr><tr><td>18</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos]+[Ras-GDP] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP]</td><td>k18 * c(26) * c(25) -kd18 * c(27)</td></tr><tr><td>19</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP] → [(EGF-EGFR*)2-GAP-Grb2-Sos]+[Ras-GTP]</td><td>k19 * c(28) * c(25) -kd19 * c(27)</td></tr><tr><td>20</td><td>[Ras-GTP*]+[(EGF-EGFR*)2-GAP-Grb2-Sos] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP]</td><td>k20 * c(25) * c(43) -kd20 * c(29)</td></tr><tr><td>21</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP] ↔ [(EGF-EGFR*)2-GAP-Grb2-Sos]+[Ras-GDP]</td><td>k21 * c(25) * c(26) -kd21 * c(29)</td></tr><tr><td>22</td><td>[(EGF-EGFR*)2-GAP]+[Shc] → [(EGF-EGFR*)2-GAP-Shc]</td><td>k22 * c(31) * c(15) -kd22 * c(32)</td></tr><tr><td>23</td><td>[(EGF-EGFR*)2-GAP-Shc] → [(EGF-EGFR*)2-GAP-Shc*]</td><td>k23 * c(32) * 1 -kd23 * c(33)</td></tr><tr><td>24</td><td>[(EGF-EGFR*)2-GAP-Shc*]+[Grb2] → [(EGF-EGFR*)2-GAP-Shc*-Grb2]</td><td>k16 * c(22) * c(33) -kd24 * c(34)</td></tr><tr><td>25</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2]+[Sos] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]</td><td>k25 * c(24) * c(34) -kd25 * c(35)</td></tr><tr><td>26</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]</td><td>k18 * c(26) * c(35) -kd18 * c(36)</td></tr><tr><td>27</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] + [Ras-GTP]</td><td>k19 * c(35) * c(28) -kd19 * c(36)</td></tr><tr><td>28</td><td>[Raf]+[Ras-GTP] → [Raf-Ras-GTP]</td><td>k28 * c(28) * c(41) -kd28 * c(42)</td></tr><tr><td>29</td><td>[Raf-Ras-GTP] → [Raf*]+[Ras-GTP*]</td><td>k29 * c(43) * c(45) -kd29 * c(42)</td></tr><tr><td>30</td><td>[Ras-GTP*]+[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]</td><td>k20 * c(35) * c(43) -kd20 * c(37)</td></tr><tr><td>31</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP]</td><td>k21 * c(35) * c(26) -kd21 * c(37)</td></tr><tr><td>32</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] ↔ [(EGF-EGFR*)2-GAP]+[Shc*-Grb2-Sos]</td><td>k32 * c(15) * c(38) -kd32 * c(35)</td></tr><tr><td>33</td><td>[Shc*-Grb2-Sos] → [Grb2-Sos]+[Shc*]</td><td>k33 * c(40) * c(30) -kd33 * c(38)</td></tr><tr><td>34</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos] → [(EGF-EGFR*)2-GAP]+[Grb2-Sos]</td><td>k34 * c(15) * c(30) -kd34 * c(25)</td></tr></tbody></table>

<!-- PAGE BREAK -->

<a id='7d59e776-e440-4cdd-8793-d4f2a6b149b7'></a>

35 [Grb2-Sos] → [Grb2] +[Sos]
36 [Shc*] → [Shc]
37 [(EGF-EGFR*)2-GAP-Shc*] → [(EGF-EGFR*)2-GAP]+[Shc*]
38 [Shc*]+[Grb2] → [Shc*-Grb2]
39 [(EGF-EGFR*)2-GAP-Shc*-Grb2] → [(EGF-EGFR*)2-GAP]+[Shc*-Grb2]
40 [Shc*-Grb2]+[Sos] → [Shc*-Grb2-Sos]
41 [(EGF-EGFR*)2-GAP-Shc*] + [Grb2-Sos] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]
42 [Raf*]+[Phosphatase1] → [Raf*-Phosphatase1]
43 [Raf*-Phosphatase1] → [Raf]+[Phosphatase1]
44 [MEK] + [Raf*] → [MEK-Raf*]
45 [MEK-Raf*] → [MEK-P] +[Raf*]
46 [MEK-P]+[Raf*] → [MEK-P-Raf*]
47 [MEK-P-Raf*] → [MEK-PP] + [Raf*]
48 [MEK-PP]+[Phosphatase2] → [MEK-PP-Phosphatase2]
49 [MEK-PP-Phosphatase2] → [MEK-P] + [Phosphatase2]
50 [MEK-P]+[Phosphatase2] → [MEK-P-Phosphatase2]
51 [MEK-P-Phosphatase2] → [MEK]+[Phosphatase2]
52 [ERK]+[MEK-PP] → [ERK-MEK-PP]
53 [ERK-MEK-PP] → [ERK-P]+[MEK-PP]
54 [ERK-P]+[MEK-PP] ↔ [ERK-P-MEK-PP]
55 [ERK-P-MEK-PP] → [ERK-PP]+[MEK-PP]
56 [ERK-PP]+[Phosphatase3] → [ERK-PP-Phosphatase3]
57 [ERK-PP-Phosphatase3] → [ERK-P]+[Phosphatase3]
58 [ERK-P] + [Phosphatase3] → [ERK-P-Phosphatase3]
59 [ERK-P-Phosphatase3] → [ERK]+[Phosphatase3]
60 [EGFRI] → [EGFRideg]
61 [EGFi]→ [EGFideg]
62 [(EGF-EGFRi*)2] → [(EGF-EGFRi*)2deg]
63 [(EGF-EGFRi*)2-GAP]+[Grb2] → [(EGF-EGFRi*)2-GAP-Grb2]
64 [(EGF-EGFRi*)2-GAP-Grb2]+[Sos] → [(EGF-EGFRi*)2-GAP-Grb2-Sos]
65 [(EGF-EGFRi*)2-GAP-Grb2-Sos]+[Ras-GDP] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP]
66 [(EGF-EGFRI*)2-GAP-Grb2-Sos-Ras-GDP] ↔ [(EGF-EGFRI*)2-GAP-Grb2-Sos]+[Ras-GTPi]
67 [Ras-GTPi*]+[(EGF-EGFRi*)2-GAP-Grb2-Sos] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTPi]
68 [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP] ↔ [(EGF-EGFRI*)2-GAP-Grb2-Sos]+[Ras-GDP]
69 [(EGF-EGFRi*)2-GAP]+[Shc] → [(EGF-EGFRi*)2-GAP-Shc]
70 [(EGF-EGFR*)2-GAP-Shc] → [(EGF-EGFR*)2-GAP-Shc*]
71 [(EGF-EGFRi*)2-GAP-Shc*]+[Grb2] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2]

<a id='b2c93b05-862c-4c8e-9bd4-b2ef05481fa4'></a>

k35 * c(24) * c(22) -kd35 * c(30)
k36 * c(40) * 1 -kd36 * c(31)
k37 * c(15) * c(40) -kd37 * c(33)
k16 * c(22) * c(40) -kd24 * c(39)
k37 * c(15) * c(39) -kd37 * c(34)
k40 * c(24) * c(39) -kd40 * c(38)
k41 * c(30) * c(33) -kd41 * c(35)
k42 * c(44) * c(45) -kd42 * c(46)
k43 * c(41) * c(44) -kd43 * c(46)
k44 * c(47) * c(45) -kd52 * c(48)
k45 * c(49) * c(45) -kd45 * c(48)
k44 * c(49) * c(45) -kd52 * c(50)
k47 * c(51) * c(45) -kd47 * c(50)
k48 * c(51) * c(53) -kd48 * c(52)
k49 * c(49) * c(53) -kd49 * c(52)
k50 * c(53) * c(49) -kd50 * c(54)
k49 * c(47) * c(53) -kd49 * c(54)
k52 * c(55) * c(51) -kd44 * c(56)
k53 * c(51) * c(57) -kd53 * c(56)
k52 * c(51) * c(57) -kd44 * c(58)
k55 * c(59) * c(51) -kd55 * c(58)
k56 * c(59) * c(60) -kd56 * c(61)
k57 * c(57) * c(60) -kd57 * c(61)
k58 * c(60) * c(57) -kd58 * c(62)
k57 * c(55) * c(60) -kd57 * c(62)
k60 * c(6) * 1 -kd60 * c(86)
k61 * c(16) * 1 -kd61 * c(13)
k60 * c(8) * 1 -kd60 * c(87)
k16 * c(17) * c(22) -kd63 * c(18)
k17 * c(24) * c(18) -kd17 * c(19)
k18 * c(26) * c(19) -kd18 * c(20)
k19 * c(69) * c(19) -kd19 * c(20)
k20 * c(71) * c(19) -kd20 * c(21)
k21 * c(19) * c(26) -kd21 * c(21)
k22 * c(31) * c(17) -kd22 * c(63)
k23 * c(63) * 1 -kd23 * c(64)
k16 * c(22) * c(64) -kd24 * c(65)

<!-- PAGE BREAK -->

<a id='c23c8158-1b50-4d05-9174-4b1d9a25d5b7'></a>

72 [(EGF-EGFRi*)2-GAP-Shc*-Grb2]+[Sos] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]
73 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]
74 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] + [Ras-GTPi]
75 [Raf]+[Ras-GTPi] → [Raf-Ras-GTPi]
76 [Raf-Ras-GTPi] → [Rafi*]+[Ras-GTPi*]
77 [Ras-GTPi*]+[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]
78 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP]
79 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] ↔ [(EGF-EGFRI*)2-GAP]+[Shc-Grb2-Sos]
80 [(EGF-EGFRi*)2-GAP-Grb2-Sos] ↔ [(EGF-EGFRi*)2-GAP]+[Grb2-Sos]
81 [(EGF-EGFRi*)2-GAP-Shc*] ↔ [(EGF-EGFRi*)2-GAP]+[Shc*]
82 [(EGF-EGFRi*)2-GAP-Shc*-Grb2] ↔ [(EGF-EGFRi*)2-GAP]+[Shc*-Grb2]
83 [(EGF-EGFRi*)2-GAP-Shc*] + [Grb2-Sos] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]
84 [Rafi*]+[Phosphatase1] ↔ [Rafi*-Phosphatase1]
85 [Rafi*-Phosphatase1] → [Raf]+[Phosphatase1]
86 [MEK] + [Rafi*] ↔ [MEK-Rafi*]
87 [MEK-Rafi*] → [MEKI-P] + [Rafi*]
88 [MEKI-P]+[Rafi*] ↔ [MEK-P-Rafi*]
89 [MEK-P-Rafi*] → [MEKI-PP] + [Rafi*]
90 [MEKI-PP]+[Phosphatase2] ↔ [MEKI-PP-Phosphatase2]
91 [MEKI-PP-Phosphatase2] → [MEKI-P] + [Phosphatase2]
92 [MEKI-P]+[Phosphatase2] ↔ [MEKI-P-Phosphatase2]
93 [MEKI-P-Phosphatase2] → [MEK]+[Phosphatase2]
94 [ERK]+[MEKI-PP] ↔ [ERK-MEKI-PP]
95 [ERK-MEKI-PP] → [ERKI-P]+[MEKI-PP]
96 [ERKI-P]+[MEKI-PP] ↔ [ERKI-P-MEKI-PP]
97 [ERKI-P-MEKI-PP] → [ERKI-PP]+[MEKI-PP]
98 [ERKI-PP]+[Phosphatase3] ↔ [ERKI-PP-Phosphatase3]
99 [ERKI-PP-Phosphatase3] → [ERKI-P]+[Phosphatase3]
100 [ERKI-P] + [Phosphatase3] ↔ [ERKI-P-Phosphatase3]
101 [ERKI-P-Phosphatase3] → [ERK]+[Phosphatase3]
102 [(EGF-EGFR*)2-GAP] → [(EGF-EGFRI*)2-GAP]
103 [(EGF-EGFR*)2-GAP-Shc] → [(EGF-EGFRi*)2-GAP-Shc]
104 [(EGF-EGFR*)2-GAP-Shc*] → [(EGF-EGFRI*)2-GAP-Shc*]
105 [(EGF-EGFR*)2-GAP-Grb2-Sos] → [(EGF-EGFRi*)2-GAP-Grb2-Sos]
106 [(EGF-EGFR*)2-GAP-Grb2-Sos]+[Prot] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Prot]
107 [(EGF-EGFR*)2-GAP-Grb2-Sos-Prot] → [ (EGF-EGFRi*)2-GAP-Grb2-Sos]+[Proti]
108 [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP]

<a id='5a4e01d9-3661-42e3-82b9-ed9c07ba2796'></a>

k25* c(24) * c(65) -kd25* c(66)
k18* c(26) * c(66) -kd18* c(67)
k19* c(66) * c(69) -kd19* c(67)
k28* c(69) * c(41) -kd28* c(70)
k29* c(71) * c(72) -kd29* c(70)
k20* c(71) * c(66) -kd20* c(68)
k21* c(66) * c(26) -kd21 * c(68)
k32* c(17) * c(38) -kd32 * c(66)
k34* c(17) * c(30) -kd34* c(19)
k37* c(17) * c(40) -kd37 * c(64)
k37* c(17) * c(39) -kd37* c(65)
k41* c(30) * c(64) -kd41* c(66)
k42* c(44) * c(72) -kd42* c(73)
k43* c(41) * c(44) -kd43 * c(73)
k44* c(47) * c(72) -kd52* c(74)
k45* c(75) * c(72) -kd45* c(74)
k44* c(72) * c(75) -kd52* c(76)
k47* c(72) * c(77) -kd47* c(76)
k48* c(77) * c(53) -kd48* c(78)
k49* c(75) * c(53) -kd49* c(78)
k50* c(53) * c(75) -kd50* c(79)
k49* c(47) * c(53) -kd49* c(79)
k52*c(55) * c(77) -kd44* c(80)
k53* c(81) * c(77) -kd53 * c(80)
k52* c(77) * c(81) -kd44* c(82)
k55* c(83) * c(77) -kd55* c(82)
k56* c(83) * c(60) -kd56* c(84)
k57* c(81) * c(60) -kd57* c(84)
k58* c(60) * c(81) -kd58* c(85)
k57* c(55) * c(60) -kd57 * c(85)
k6* c(15)* 1-kd6 * c(17)
k6* c(32) * 1 -kd6* c(63)
k6 * c(33) * 1 -kd6* c(64)
k6* c(25) * 1 -kd6 * c(19)
k4* c(25) * c(12) -kd4 * c(88)
k5* c(9) * c(19) -kd5* c(88)
k6* c(27) * 1 -kd6 * c(20)

<!-- PAGE BREAK -->

<a id='07d5aaab-960d-49ed-be5e-5251ab65ddcc'></a>

109 [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP]+[Prot] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP-Prot]
110 [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP-Prot] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP]+[Proti]
111 [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP]
112 [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP]+[Prot] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP-Prot]
113 [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP-Prot] → [ (EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP]+[Proti]
114 [(EGF-EGFR*)2-GAP-Shc*-Grb2] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2]
115 [(EGF-EGFR*)2-GAP-Shc*-Grb2]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Prot]
116 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Prot] → [ (EGF-EGFRi*)2-GAP-Shc*-Grb2]+[Proti]
117 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]→ [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos]
118 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Prot]
119 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Prot] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]+[Proti]
120 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]
121 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP-Prot]
122 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP-Prot] → [ (EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]+[Proti]
123 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]
124 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP-Prot]
125 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP-Prot] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]+[Proti]
126 [(EGF-EGFR*)2-GAP-Grb2-Sos]+[ERK-PP] → [(EGF-EGFR*)2-GAP-Grb2-Sos-ERK-PP]
127 [(EGF-EGFRi*)2-GAP-Grb2-Sos]+[ERKI-PP] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-ERKI-PP]
128 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[ERK-PP] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-ERK-PP]
129 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]+[ERKI-PP] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-ERKI-PP]
130 [Sos]+[ERK-PP] → [Sos-ERK-PP]
131 [Sos]+[ERKI-PP] → [Sos-ERKI-PP]
132 [(EGF-EGFRi*)2-GAP] → [(EGF-EGFRI*)2deg]
133 [(EGF-EGFRi*)2-GAP-Grb2] → [(EGF-EGFRi*)2deg]
134 [(EGF-EGFRi*)2-GAP-Grb2-Sos] → [(EGF-EGFRi*)2deg]
135 [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP] → [(EGF-EGFRi*)2deg]
136 [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP] → [(EGF-EGFRi*)2deg]
137 [(EGF-EGFRi*)2-GAP-Shc] → [(EGF-EGFRi*)2deg]
138 [(EGF-EGFRi*)2-GAP-Shc*] → [(EGF-EGFRi*)2deg]
139 [(EGF-EGFRi*)2-GAP-Shc*-Grb2] → [(EGF-EGFRi*)2deg]
140 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] → [(EGF-EGFRi*)2deg]
141 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] → [(EGF-EGFRi*)2deg]
142 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] → [(EGF-EGFRi*)2deg]
143 [(EGF-EGFR*)2-GAP-Grb2-Sos-ERK-PP] → [(EGF-EGFR*)2-GAP-Grb2-Sos]deg+[ERK-PP]
144 [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-ERK-PP] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]deg+[ERK-PP]
145 [Sos-ERK-PP] → [Sosi]+[ERK-PP]

<a id='db2b2d97-b946-49dd-a652-f6967d65c692'></a>

k4* c(27) * c(12) -kd4* c(89)
k5* c(9) * c(20) -kd5 * c(89)
k6* c(29) * 1 -kd6 * c(21)
k4* c(29) * c(12) -kd4 * c(90)
k5* c(9) * c(21) -kd5 * c(90)
k6* c(34) * 1 -kd6 * c(65)
k4* c(34) * c(12) -kd4* c(91)
k5* c(9) * c(65) -kd5* c(91)
k6* c(35) * 1 -kd6 * c(66)
k4* c(35) * c(12) -kd4* c(92)
k5* c(9) * c(66) -kd5 * c(92)
k6* c(36) * 1 -kd6 * c(67)
k4* c(36) * c(12) -kd4 * c(93)
k5* c(9) * c(67) -kd5 * c(93)
k6* c(37) * 1 -kd6 * c(68)
k4* c(37) * c(12) -kd4 * c(94)
k5* c(68) * c(9) -kd5 * c(94)
k126* c(59) * c(25) -kd126* c(95)
k126* c(83) * c(19) -kd126* c(96)
k126* c(59) * c(35) -kd126* c(97)
k126* c(83) * c(66) -kd126* c(98)
k126* c(59) * c(24) -kd126* c(101)
k126* c(83) * c(24) -kd126* c(102)
k60* c(17) * 1 -kd60* c(87)
k60* c(18) * 1 -kd60* c(87)
k60* c(19) * 1 -kd60* c(87)
k60* c(20)* 1-kd60* c(87)
k60* c(21) * 1 -kd60* c(87)
k60* c(63) * 1 -kd60 * c(87)
k60* c(64) * 1 -kd60 * c(87)
k60* c(65) * 1 -kd60 * c(87)
k60* c(66) * 1 -kd60* c(87)
k60* c(67) * 1 -kd60 * c(87)
k60* c(68) * 1 -kd60* c(87)
k127* c(59) * c(99) -kd127* c(95)
k127* c(59) * c(99) -kd127* c(97)
k127* c(59) * c(103) -kd127* c(101)

<!-- PAGE BREAK -->

<a id='78e6dfdf-177c-45b0-91c9-f3b21b98140a'></a>

146 [(EGF-EGFRi*)2-GAP-Grb2-Sos-ERKI-PP] ↔ [(EGF-EGFRi*)2-GAP-Grb2-Sos]deg+[ERKI-PP]
k127* c(83)* c(100) -kd127* c(96)
147 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-ERKI-PP] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]deg+[ERKi-PP]
k127* c(83)* c(100) -kd127* c(98)
148 [Sos-ERK-PPi] ↔ [Sosi]+[ERK-PPi]
k127* c(83)* c(103) -kd127* c(102)

<!-- PAGE BREAK -->

<a id='49744f95-a261-4f62-aa98-dc79364cffeb'></a>

Supplementary table 2: parameter values and initial conditions
<table id="5-1">
<tr><td id="5-2">parameter</td><td id="5-3">value*</td><td id="5-4"></td><td id="5-5">c</td><td id="5-6">components</td><td id="5-7">initial concentrations**</td></tr>
<tr><td id="5-8">k1</td><td id="5-9">3.00E+07</td><td id="5-a"></td><td id="5-b">c1</td><td id="5-c">EGF</td><td id="5-d">5.00E-08</td></tr>
<tr><td id="5-e">kd1</td><td id="5-f">3.84E-03</td><td id="5-g"></td><td id="5-h">c2</td><td id="5-i">EGFR</td><td id="5-j">5.00E+04</td></tr>
<tr><td id="5-k">k10</td><td id="5-l">1.40E+05</td><td id="5-m"></td><td id="5-n">c3</td><td id="5-o">EGF-EGFR</td><td id="5-p">0.00E+00</td></tr>
<tr><td id="5-q">k10b</td><td id="5-r">5.43E-02</td><td id="5-s"></td><td id="5-t">c4</td><td id="5-u">(EGF-EGFR)2</td><td id="5-v">0.00E+00</td></tr>
<tr><td id="5-w">kd10b</td><td id="5-x">0.00E+00</td><td id="5-y"></td><td id="5-z">c5</td><td id="5-A">(EGF-EGFR*)2</td><td id="5-B">0.00E+00</td></tr>
<tr><td id="5-C">kd10</td><td id="5-D">1.10E-02</td><td id="5-E"></td><td id="5-F">c6</td><td id="5-G">EGFRI</td><td id="5-H">0.00E+00</td></tr>
<tr><td id="5-I">k2</td><td id="5-J">1.66E-05</td><td id="5-K"></td><td id="5-L">c7</td><td id="5-M">(EGF-EGFR*)2-GAP-Grb2-Prot</td><td id="5-N">0.00E+00</td></tr>
<tr><td id="5-O">kd2</td><td id="5-P">1.00E-01</td><td id="5-Q"></td><td id="5-R">c8</td><td id="5-S">(EGF-EGFRI*)2</td><td id="5-T">0.00E+00</td></tr>
<tr><td id="5-U">k3</td><td id="5-V">1.00E+00</td><td id="5-W"></td><td id="5-X">c9</td><td id="5-Y">Proti</td><td id="5-Z">0.00E+00</td></tr>
<tr><td id="5-10">kd3</td><td id="5-11">1.00E-02</td><td id="5-12"></td><td id="5-13">c10</td><td id="5-14">EGF-EGFRI</td><td id="5-15">0.00E+00</td></tr>
<tr><td id="5-16">k4</td><td id="5-17">1.73E-07</td><td id="5-18"></td><td id="5-19">c11</td><td id="5-1a">(EGF-EGFRI)2</td><td id="5-1b">0.00E+00</td></tr>
<tr><td id="5-1c">kd4</td><td id="5-1d">1.66E-03</td><td id="5-1e"></td><td id="5-1f">c12</td><td id="5-1g">Prot</td><td id="5-1h">8.10E+04</td></tr>
<tr><td id="5-1i">kd5</td><td id="5-1j">1.46E-02</td><td id="5-1k"></td><td id="5-1l">c13</td><td id="5-1m">EGFideg</td><td id="5-1n">0.00E+00</td></tr>
<tr><td id="5-1o">k5</td><td id="5-1p">0.00E+00</td><td id="5-1q"></td><td id="5-1r">c14</td><td id="5-1s">GAP</td><td id="5-1t">1.20E+04</td></tr>
<tr><td id="5-1u">k6</td><td id="5-1v">5.00E-04</td><td id="5-1w"></td><td id="5-1x">c15</td><td id="5-1y">(EGF-EGFR*)2-GAP</td><td id="5-1z">0.00E+00</td></tr>
<tr><td id="5-1A">kd6</td><td id="5-1B">5.00E-03</td><td id="5-1C"></td><td id="5-1D">c16</td><td id="5-1E">EGFI</td><td id="5-1F">0.00E+00</td></tr>
<tr><td id="5-1G">k8</td><td id="5-1H">1.66E-06</td><td id="5-1I"></td><td id="5-1J">c17</td><td id="5-1K">(EGF-EGFRI*)2-GAP</td><td id="5-1L">0.00E+00</td></tr>
<tr><td id="5-1M">kd8</td><td id="5-1N">2.00E-01</td><td id="5-1O"></td><td id="5-1P">c18</td><td id="5-1Q">(EGF-EGFRI*)2-GAP-Grb2</td><td id="5-1R">0.00E+00</td></tr>
<tr><td id="5-1S">k13</td><td id="5-1T">4.28E+04</td><td id="5-1U"></td><td id="5-1V">c19</td><td id="5-1W">(EGF-EGFRi*)2-GAP-Grb2-Sos</td><td id="5-1X">0.00E+00</td></tr>
<tr><td id="5-1Y">kd13</td><td id="5-1Z">0.00E+00</td><td id="5-20"></td><td id="5-21">c20</td><td id="5-22">(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP</td><td id="5-23">0.00E+00</td></tr>
<tr><td id="5-24">k15</td><td id="5-25">1.00E+04</td><td id="5-26"></td><td id="5-27">c21</td><td id="5-28">(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP</td><td id="5-29">0.00E+00</td></tr>
<tr><td id="5-2a">Ikd15</td><td id="5-2b">0.00E+00</td><td id="5-2c"></td><td id="5-2d">c22</td><td id="5-2e">Grb2</td><td id="5-2f">1.10E+04</td></tr>
<tr><td id="5-2g">k16</td><td id="5-2h">1.66E-05</td><td id="5-2i"></td><td id="5-2j">c23</td><td id="5-2k">(EGF-EGFR*)2-GAP-Grb2</td><td id="5-2l">0.00E+00</td></tr>
<tr><td id="5-2m">kd16</td><td id="5-2n">0.00E+00</td><td id="5-2o"></td><td id="5-2p">c24</td><td id="5-2q">Sos</td><td id="5-2r">2.63E+04</td></tr>
<tr><td id="5-2s">k17</td><td id="5-2t">1.66E-05</td><td id="5-2u"></td><td id="5-2v">c25</td><td id="5-2w">(EGF-EGFR*)2-GAP-Grb2-Sos</td><td id="5-2x">0.00E+00</td></tr>
<tr><td id="5-2y">Ikd17</td><td id="5-2z">6.00E-02</td><td id="5-2A"></td><td id="5-2B">c26</td><td id="5-2C">Ras-GDP</td><td id="5-2D">7.20E+04</td></tr>
<tr><td id="5-2E">Ik18</td><td id="5-2F">2.50E-05</td><td id="5-2G"></td><td id="5-2H">c27</td><td id="5-2I">(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP</td><td id="5-2J">0.00E+00</td></tr>
<tr><td id="5-2K">Ikd18</td><td id="5-2L">3.80E+04</td><td id="5-2M"></td><td id="5-2N">C28</td><td id="5-2O">Ras-GTP</td><td id="5-2P">0.00E+00</td></tr>
<tr><td id="5-2Q">k19</td><td id="5-2R">1.66E-07</td><td id="5-2S"></td><td id="5-2T">C29</td><td id="5-2U">(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP</td><td id="5-2V">0.00E+00</td></tr>
<tr><td id="5-2W">kd19</td><td id="5-2X">5.00E-01</td><td id="5-2Y"></td><td id="5-2Z">c30</td><td id="5-30">Grb2-Sos</td><td id="5-31">4.00E+04</td></tr>
<tr><td id="5-32">k20</td><td id="5-33">3.50E-06</td><td id="5-34"></td><td id="5-35">c31</td><td id="5-36">Shc</td><td id="5-37">1.01E+05</td></tr>
<tr><td id="5-38">kd20</td><td id="5-39">4.00E-01</td><td id="5-3a"></td><td id="5-3b">c32</td><td id="5-3c">(EGF-EGFR*)2-GAP-SHC</td><td id="5-3d">0.00E+00</td></tr>
<tr><td id="5-3e">k21</td><td id="5-3f">3.66E-07</td><td id="5-3g"></td><td id="5-3h">c33</td><td id="5-3i">(EGF-EGFR*)2-GAP-SHC*</td><td id="5-3j">0.00E+00</td></tr>
<tr><td id="5-3k">kd21</td><td id="5-3l">2.30E-02</td><td id="5-3m"></td><td id="5-3n">c34</td><td id="5-3o">(EGF-EGFR*)2-GAP-SHC*-Grb2</td><td id="5-3p">0.00E+00</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='9e47ae3a-205b-4688-87a7-623ac68f5ed6'></a>

<table id="6-1">
<tr><td id="6-2">k22</td><td id="6-3">3.50E-05</td><td id="6-4"></td><td id="6-5">c35</td><td id="6-6">(EGF-EGFR*)2-GAP-SHC*-Grb2-Sos</td><td id="6-7">0.00E+00</td></tr>
<tr><td id="6-8">kd22</td><td id="6-9">1.00E-01</td><td id="6-a"></td><td id="6-b">c36</td><td id="6-c">(EGF-EGFR*)2-GAP-SHC*-Grb2-Sos-Ras-GDP</td><td id="6-d">0.00E+00</td></tr>
<tr><td id="6-e">k23</td><td id="6-f">6.00E+00</td><td id="6-g"></td><td id="6-h">c37</td><td id="6-i">(EGF-EGFR*)2-GAP-SHC*-Grb2-Sos-Ras-GTP</td><td id="6-j">0.00E+00</td></tr>
<tr><td id="6-k">kd23</td><td id="6-l">6.00E-02</td><td id="6-m"></td><td id="6-n">c38</td><td id="6-o">Shc*-Grb2-Sos</td><td id="6-p">0.00E+00</td></tr>
<tr><td id="6-q">kd24</td><td id="6-r">5.50E-01</td><td id="6-s"></td><td id="6-t">c39</td><td id="6-u">Shc*-Grb2</td><td id="6-v">0.00E+00</td></tr>
<tr><td id="6-w">k25</td><td id="6-x">1.66E-05</td><td id="6-y"></td><td id="6-z">c40</td><td id="6-A">Shc*</td><td id="6-B">0.00E+00</td></tr>
<tr><td id="6-C">kd25</td><td id="6-D">2.14E-02</td><td id="6-E"></td><td id="6-F">c41</td><td id="6-G">Raf</td><td id="6-H">4.00E+04</td></tr>
<tr><td id="6-I">k28</td><td id="6-J">1.66E-06</td><td id="6-K"></td><td id="6-L">c42</td><td id="6-M">Raf-Ras-GTP</td><td id="6-N">0.00E+00</td></tr>
<tr><td id="6-O">kd28</td><td id="6-P">5.30E-03</td><td id="6-Q"></td><td id="6-R">c43</td><td id="6-S">Ras-GTP*</td><td id="6-T">0.00E+00</td></tr>
<tr><td id="6-U">k29</td><td id="6-V">1.17E-02</td><td id="6-W"></td><td id="6-X">c44</td><td id="6-Y">Phosphatase1</td><td id="6-Z">4.00E+04</td></tr>
<tr><td id="6-10">kd29</td><td id="6-11">1.00E+00</td><td id="6-12"></td><td id="6-13">c45</td><td id="6-14">Raf*</td><td id="6-15">0.00E+00</td></tr>
<tr><td id="6-16">kd32</td><td id="6-17">1.00E-01</td><td id="6-18"></td><td id="6-19">c46</td><td id="6-1a">Raf*-phosphatase1</td><td id="6-1b">0.00E+00</td></tr>
<tr><td id="6-1c">k32</td><td id="6-1d">4.00E-07</td><td id="6-1e"></td><td id="6-1f">c47</td><td id="6-1g">MEK</td><td id="6-1h">2.10E+07</td></tr>
<tr><td id="6-1i">kd33</td><td id="6-1j">2.00E-01</td><td id="6-1k"></td><td id="6-1l">c48</td><td id="6-1m">MEK-Raf*</td><td id="6-1n">0.00E+00</td></tr>
<tr><td id="6-1o">k33</td><td id="6-1p">3.50E-05</td><td id="6-1q"></td><td id="6-1r">c49</td><td id="6-1s">MEK-P</td><td id="6-1t">0.00E+00</td></tr>
<tr><td id="6-1u">kd34</td><td id="6-1v">3.00E-02</td><td id="6-1w"></td><td id="6-1x">c50</td><td id="6-1y">MEK-P-Raf*</td><td id="6-1z">0.00E+00</td></tr>
<tr><td id="6-1A">k34</td><td id="6-1B">7.50E-06</td><td id="6-1C"></td><td id="6-1D">c51</td><td id="6-1E">MEK-PP</td><td id="6-1F">0.00E+00</td></tr>
<tr><td id="6-1G">kd35</td><td id="6-1H">1.50E-03</td><td id="6-1I"></td><td id="6-1J">c52</td><td id="6-1K">MEK-PP-phosphatase2</td><td id="6-1L">0.00E+00</td></tr>
<tr><td id="6-1M">k35</td><td id="6-1N">7.50E-06</td><td id="6-1O"></td><td id="6-1P">c53</td><td id="6-1Q">phosphatase2</td><td id="6-1R">4.00E+04</td></tr>
<tr><td id="6-1S">k36</td><td id="6-1T">5.00E-03</td><td id="6-1U"></td><td id="6-1V">c54</td><td id="6-1W">MEK-P-phosphatase2</td><td id="6-1X">0.00E+00</td></tr>
<tr><td id="6-1Y">kd36</td><td id="6-1Z">0.00E+00</td><td id="6-20"></td><td id="6-21">c55</td><td id="6-22">ERK</td><td id="6-23">2.21E+07</td></tr>
<tr><td id="6-24">kd37</td><td id="6-25">3.00E-01</td><td id="6-26"></td><td id="6-27">c56</td><td id="6-28">ERK-MEK-PP</td><td id="6-29">0.00E+00</td></tr>
<tr><td id="6-2a">k37</td><td id="6-2b">1.50E-06</td><td id="6-2c"></td><td id="6-2d">c57</td><td id="6-2e">ERK-P</td><td id="6-2f">0.00E+00</td></tr>
<tr><td id="6-2g">k40</td><td id="6-2h">5.00E-05</td><td id="6-2i"></td><td id="6-2j">c58</td><td id="6-2k">ERK-P-MEK-PP</td><td id="6-2l">0.00E+00</td></tr>
<tr><td id="6-2m">kd40</td><td id="6-2n">6.40E-02</td><td id="6-2o"></td><td id="6-2p">c59</td><td id="6-2q">ERK-PP</td><td id="6-2r">0.00E+00</td></tr>
<tr><td id="6-2s">k41</td><td id="6-2t">5.00E-05</td><td id="6-2u"></td><td id="6-2v">c60</td><td id="6-2w">phosphatase3</td><td id="6-2x">1.00E+07</td></tr>
<tr><td id="6-2y">kd41</td><td id="6-2z">4.29E-02</td><td id="6-2A"></td><td id="6-2B">c61</td><td id="6-2C">ERK-PP-phosphatase3</td><td id="6-2D">0.00E+00</td></tr>
<tr><td id="6-2E">k42</td><td id="6-2F">1.18E-04</td><td id="6-2G"></td><td id="6-2H">c62</td><td id="6-2I">ERK-P-phosphatase3</td><td id="6-2J">0.00E+00</td></tr>
<tr><td id="6-2K">kd42</td><td id="6-2L">2.00E-01</td><td id="6-2M"></td><td id="6-2N">c63</td><td id="6-2O">(EGF-EGFRI*)2-GAP-SHC</td><td id="6-2P">0.00E+00</td></tr>
<tr><td id="6-2Q">kd43</td><td id="6-2R">1.00E+00</td><td id="6-2S"></td><td id="6-2T">c64</td><td id="6-2U">(EGF-EGFRI*)2-GAP-SHC*</td><td id="6-2V">0.00E+00</td></tr>
<tr><td id="6-2W">k43</td><td id="6-2X">0.00E+00</td><td id="6-2Y"></td><td id="6-2Z">c65</td><td id="6-30">(EGF-EGFRi*)2-GAP-SHC*-Grb2</td><td id="6-31">0.00E+00</td></tr>
<tr><td id="6-32">kd44</td><td id="6-33">1.83E-02</td><td id="6-34"></td><td id="6-35">c66</td><td id="6-36">(EGF-EGFRI*)2-GAP-SHC*-Grb2-Sos</td><td id="6-37">0.00E+00</td></tr>
<tr><td id="6-38">kd45</td><td id="6-39">3.81E+04</td><td id="6-3a"></td><td id="6-3b">c67</td><td id="6-3c">(EGF-EGFRI*)2-GAP-SHC*-Grb2-Sos-Ras-GDP</td><td id="6-3d">0.00E+00</td></tr>
<tr><td id="6-3e">k45</td><td id="6-3f">0.00E+00</td><td id="6-3g"></td><td id="6-3h">c68</td><td id="6-3i">(EGF-EGFRi*)2-GAP-SHC*-Grb2-Sos-Ras-GTP</td><td id="6-3j">0.00E+00</td></tr>
<tr><td id="6-3k">kd47</td><td id="6-3l">3.82E+04</td><td id="6-3m"></td><td id="6-3n">c69</td><td id="6-3o">Ras-GTPi</td><td id="6-3p">0.00E+00</td></tr>
<tr><td id="6-3q">k47</td><td id="6-3r">0.00E+00</td><td id="6-3s"></td><td id="6-3t">c70</td><td id="6-3u">Raf-Ras-GTPi</td><td id="6-3v">0.00E+00</td></tr>
<tr><td id="6-3w">k48</td><td id="6-3x">2.38E-01</td><td id="6-3y"></td><td id="6-3z">c71</td><td id="6-3A">Ras-GTPi</td><td id="6-3B">0.00E+00</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='7a052dbc-5af2-402d-b762-0d17e491fff1'></a>

<table id="7-1">
<tr><td id="7-2">kd48</td><td id="7-3">8.00E-01</td><td id="7-4"></td><td id="7-5">c72</td><td id="7-6">Rafi*</td><td id="7-7">0.00E+00</td></tr>
<tr><td id="7-8">kd49</td><td id="7-9">5.80E-02</td><td id="7-a"></td><td id="7-b">c73</td><td id="7-c">Rafi*-phosphatase1</td><td id="7-d">0.00E+00</td></tr>
<tr><td id="7-e">k49</td><td id="7-f">0.00E+00</td><td id="7-g"></td><td id="7-h">c74</td><td id="7-i">MEK-Rafi*</td><td id="7-j">0.00E+00</td></tr>
<tr><td id="7-k">k50</td><td id="7-l">4.50E-07</td><td id="7-m"></td><td id="7-n">c75</td><td id="7-o">MEKI-P</td><td id="7-p">0.00E+00</td></tr>
<tr><td id="7-q">kd50</td><td id="7-r">5.00E-01</td><td id="7-s"></td><td id="7-t">c76</td><td id="7-u">MEK-P-Rafi*</td><td id="7-v">0.00E+00</td></tr>
<tr><td id="7-w">kd52</td><td id="7-x">3.30E-02</td><td id="7-y"></td><td id="7-z">c77</td><td id="7-A">MEKI-PP</td><td id="7-B">0.00E+00</td></tr>
<tr><td id="7-C">kd53</td><td id="7-D">1.60E+01</td><td id="7-E"></td><td id="7-F">c78</td><td id="7-G">MEKI-PP-phosphatase2</td><td id="7-H">0.00E+00</td></tr>
<tr><td id="7-I">k53</td><td id="7-J">0.00E+00</td><td id="7-K"></td><td id="7-L">c79</td><td id="7-M">MEKi-P-phosphatase2</td><td id="7-N">0.00E+00</td></tr>
<tr><td id="7-O">kd55</td><td id="7-P">3.82E+04</td><td id="7-Q"></td><td id="7-R">c80</td><td id="7-S">ERKI-MEKI-PP</td><td id="7-T">0.00E+00</td></tr>
<tr><td id="7-U">k5</td><td id="7-V">0.00E+00</td><td id="7-W"></td><td id="7-X">c81</td><td id="7-Y">ERKI-P</td><td id="7-Z">0.00E+00</td></tr>
<tr><td id="7-10">kd56</td><td id="7-11">6.00E-01</td><td id="7-12"></td><td id="7-13">c82</td><td id="7-14">ERKI-P-MEKI-PP</td><td id="7-15">0.00E+00</td></tr>
<tr><td id="7-16">k56</td><td id="7-17">2.35E-05</td><td id="7-18"></td><td id="7-19">c83</td><td id="7-1a">ERKI-PP</td><td id="7-1b">0.00E+00</td></tr>
<tr><td id="7-1c">Ikd57</td><td id="7-1d">2.46E-01</td><td id="7-1e"></td><td id="7-1f">c84</td><td id="7-1g">ERKI-PP-phosphatase3</td><td id="7-1h">0.00E+00</td></tr>
<tr><td id="7-1i">k57</td><td id="7-1j">0.00E+00</td><td id="7-1k"></td><td id="7-1l">c85</td><td id="7-1m">ERKi-P-phosphatase3</td><td id="7-1n">0.00E+00</td></tr>
<tr><td id="7-1o">k58</td><td id="7-1p">8.33E-02</td><td id="7-1q"></td><td id="7-1r">980</td><td id="7-1s">EGFRideg</td><td id="7-1t">0.00E+00</td></tr>
<tr><td id="7-1u">kd58</td><td id="7-1v">5.00E-01</td><td id="7-1w"></td><td id="7-1x">c87</td><td id="7-1y">(EGF-EGFRi*)2deg</td><td id="7-1z">0.00E+00</td></tr>
<tr><td id="7-1A">k52</td><td id="7-1B">8.91E-01</td><td id="7-1C"></td><td id="7-1D">c88</td><td id="7-1E">(EGF-EGFR*)2-GAP-Grb2-Sos-Prot</td><td id="7-1F">0.00E+00</td></tr>
<tr><td id="7-1G">k44</td><td id="7-1H">1.95E-01</td><td id="7-1I"></td><td id="7-1J">c89</td><td id="7-1K">(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP-Prot</td><td id="7-1L">0.00E+00</td></tr>
<tr><td id="7-1M">k60</td><td id="7-1N">5.50E-03</td><td id="7-1O"></td><td id="7-1P">c90</td><td id="7-1Q">(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP-Prot</td><td id="7-1R">0.00E+00</td></tr>
<tr><td id="7-1S">Ikd60</td><td id="7-1T">0.00E+00</td><td id="7-1U"></td><td id="7-1V">c91</td><td id="7-1W">(EGF-EGFR*)2-GAP-SHC*-Grb2-Prot</td><td id="7-1X">0.00E+00</td></tr>
<tr><td id="7-1Y">k61</td><td id="7-1Z">6.70E-04</td><td id="7-20"></td><td id="7-21">c92</td><td id="7-22">(EGF-EGFR*)2-GAP-SHC*-Grb2-Sos-Prot</td><td id="7-23">0.00E+00</td></tr>
<tr><td id="7-24">kd61</td><td id="7-25">0.00E+00</td><td id="7-26"></td><td id="7-27">c93</td><td id="7-28">(EGF-EGFR*)2-GAP-SHC*-Grb2-Sos-Ras-GDP-Prot</td><td id="7-29">0.00E+00</td></tr>
<tr><td id="7-2a">kd63</td><td id="7-2b">2.75E-01</td><td id="7-2c"></td><td id="7-2d">c94</td><td id="7-2e">(EGF-EGFR*)2-GAP-SHC*-Grb2-Sos-Ras-GTP-Prot</td><td id="7-2f">0.00E+00</td></tr>
<tr><td id="7-2g">k63</td><td id="7-2h">0.00E+00</td><td id="7-2i"></td><td id="7-2j">c95</td><td id="7-2k">(EGF-EGFR*)2-GAP-Grb2-Sos-ERK-PP</td><td id="7-2l">0.00E+00</td></tr>
<tr><td id="7-2m">k126</td><td id="7-2n">1.66E-07</td><td id="7-2o"></td><td id="7-2p">960</td><td id="7-2q">(EGF-EGFRi*)2-GAP-Grb2-Sos-ERKI-PP</td><td id="7-2r">0.00E+00</td></tr>
<tr><td id="7-2s">kd126</td><td id="7-2t">2.00E+00</td><td id="7-2u"></td><td id="7-2v">c97</td><td id="7-2w">(EGF-EGFR*)2-GAP-SHC*-Grb2-Sos-ERK-PP</td><td id="7-2x">0.00E+00</td></tr>
<tr><td id="7-2y">kd127</td><td id="7-2z">1.00E-04</td><td id="7-2A"></td><td id="7-2B">c98</td><td id="7-2C">(EGF-EGFRI*)2-GAP-SHC*-Grb2-Sos-ERKI-PP</td><td id="7-2D">0.00E+00</td></tr>
<tr><td id="7-2E">k127</td><td id="7-2F">0.00E+00</td><td id="7-2G"></td><td id="7-2H">c99</td><td id="7-2I">(EGF-EGFR*)2-GAP-Grb2-Sos deg</td><td id="7-2J">0.00E+00</td></tr>
<tr><td id="7-2K"></td><td id="7-2L"></td><td id="7-2M"></td><td id="7-2N">c100</td><td id="7-2O">(EGF-EGFR*)2-GAP-Grb2-Sos deg</td><td id="7-2P">0.00E+00</td></tr>
<tr><td id="7-2Q"></td><td id="7-2R"></td><td id="7-2S"></td><td id="7-2T">c101</td><td id="7-2U">Sos-ERK-PP</td><td id="7-2V">0.00E+00</td></tr>
<tr><td id="7-2W"></td><td id="7-2X"></td><td id="7-2Y"></td><td id="7-2Z">c102</td><td id="7-30">Sos-ERKI-PP</td><td id="7-31">0.00E+00</td></tr>
<tr><td id="7-32"></td><td id="7-33"></td><td id="7-34"></td><td id="7-35">c103</td><td id="7-36">Sosi</td><td id="7-37">0.00E+00</td></tr>
</table>

<a id='538fc042-2962-4e6d-bf01-b40f85130523'></a>

* first order rate constants in 1/s and second order rate constants in [M-1 s-1]
** in molecules per cell

<!-- PAGE BREAK -->

<a id='a861c7c5-93f3-40a6-bada-78e40c1ca37c'></a>

Supplementary table 3: control coefficients on amplitude A, duration d and integrated response I
for all 148 reactions calculated by small or large perturbations
<table id="8-1">
<tr><td id="8-2" rowspan="2">V</td><td id="8-3" colspan="3">small perturbations (δp/p= 10^-6)</td><td id="8-4" colspan="3">large perturbations (δp/p= - 0.5)</td><td id="8-5" colspan="3">large perturbations (δp/p= 0.5)</td></tr>
<tr><td id="8-6">A</td><td id="8-7">d</td><td id="8-8">l</td><td id="8-9">A</td><td id="8-a">d</td><td id="8-b">I</td><td id="8-c">A</td><td id="8-d">d</td><td id="8-e">I</td></tr>
<tr><td id="8-f">1</td><td id="8-g">9.91E-06</td><td id="8-h">5.60E-05</td><td id="8-i">1.07E-04</td><td id="8-j">2.69E-05</td><td id="8-k">1.36E-04</td><td id="8-l">2.58E-04</td><td id="8-m">5.88E-06</td><td id="8-n">3.61E-05</td><td id="8-o">6.56E-05</td></tr>
<tr><td id="8-p">2</td><td id="8-q">9.83E-05</td><td id="8-r">4.96E-04</td><td id="8-s">8.98E-04</td><td id="8-t">2.09E-04</td><td id="8-u">9.80E-04</td><td id="8-v">1.81E-03</td><td id="8-w">6.26E-05</td><td id="8-x">3.30E-04</td><td id="8-y">5.86E-04</td></tr>
<tr><td id="8-z">3</td><td id="8-A">2.82E-05</td><td id="8-B">1.04E-04</td><td id="8-C">2.18E-04</td><td id="8-D">7.37E-05</td><td id="8-E">2.53E-04</td><td id="8-F">5.29E-04</td><td id="8-G">1.67E-05</td><td id="8-H">6.21E-05</td><td id="8-I">1.26E-04</td></tr>
<tr><td id="8-J">4</td><td id="8-K">-1.45E-04</td><td id="8-L">-7.24E-03</td><td id="8-M">-1.10E-02</td><td id="8-N">-1.50E-04</td><td id="8-O">-7.83E-03</td><td id="8-P">-1.19E-02</td><td id="8-Q">-1.40E-04</td><td id="8-R">-6.74E-03</td><td id="8-S">-1.02E-02</td></tr>
<tr><td id="8-T">5</td><td id="8-U">-4.26E-05</td><td id="8-V">-1.01E-03</td><td id="8-W">-1.35E-03</td><td id="8-X">-4.90E-05</td><td id="8-Y">-1.73E-03</td><td id="8-Z">-2.20E-03</td><td id="8-10">-3.79E-05</td><td id="8-11">-7.27E-04</td><td id="8-12">-9.99E-04</td></tr>
<tr><td id="8-13">6</td><td id="8-14">-1.82E-06</td><td id="8-15">4.04E-05</td><td id="8-16">4.08E-05</td><td id="8-17">-2.04E-06</td><td id="8-18">4.46E-05</td><td id="8-19">4.16E-05</td><td id="8-1a">-1.72E-06</td><td id="8-1b">3.83E-05</td><td id="8-1c">3.80E-05</td></tr>
<tr><td id="8-1d">7</td><td id="8-1e">-7.16E-04</td><td id="8-1f">1.41E-02</td><td id="8-1g">1.60E-02</td><td id="8-1h">-7.43E-04</td><td id="8-1i">1.94E-02</td><td id="8-1j">2.22E-02</td><td id="8-1k">-6.91E-04</td><td id="8-1l">1.09E-02</td><td id="8-1m">1.22E-02</td></tr>
<tr><td id="8-1n">8</td><td id="8-1o">4.00E-03</td><td id="8-1p">2.54E-02</td><td id="8-1q">4.60E-02</td><td id="8-1r">8.79E-03</td><td id="8-1s">4.86E-02</td><td id="8-1t">8.88E-02</td><td id="8-1u">2.54E-03</td><td id="8-1v">1.71E-02</td><td id="8-1w">3.08E-02</td></tr>
<tr><td id="8-1x">9</td><td id="8-1y">6.17E-06</td><td id="8-1z">1.44E-03</td><td id="8-1A">2.00E-03</td><td id="8-1B">6.22E-06</td><td id="8-1C">1.45E-03</td><td id="8-1D">2.02E-03</td><td id="8-1E">6.15E-06</td><td id="8-1F">1.43E-03</td><td id="8-1G">1.99E-03</td></tr>
<tr><td id="8-1H">10</td><td id="8-1I">-2.01E-08</td><td id="8-1J">-1.55E-06</td><td id="8-1K">3.59E-06</td><td id="8-1L">1.84E-09</td><td id="8-1M">2.68E-07</td><td id="8-1N">3.97E-07</td><td id="8-1O">5.45E-10</td><td id="8-1P">8.76E-08</td><td id="8-1Q">1.28E-07</td></tr>
<tr><td id="8-1R">11</td><td id="8-1S">7.75E-06</td><td id="8-1T">3.11E-05</td><td id="8-1U">6.05E-05</td><td id="8-1V">8.34E-06</td><td id="8-1W">3.94E-05</td><td id="8-1X">6.37E-05</td><td id="8-1Y">7.32E-06</td><td id="8-1Z">2.68E-05</td><td id="8-20">5.34E-05</td></tr>
<tr><td id="8-21">12</td><td id="8-22">1.79E-06</td><td id="8-23">4.66E-06</td><td id="8-24">7.97E-06</td><td id="8-25">3.06E-06</td><td id="8-26">1.10E-05</td><td id="8-27">2.21E-05</td><td id="8-28">1.19E-06</td><td id="8-29">4.19E-06</td><td id="8-2a">8.58E-06</td></tr>
<tr><td id="8-2b">13</td><td id="8-2c">1.64E-05</td><td id="8-2d">2.51E-02</td><td id="8-2e">2.51E-02</td><td id="8-2f">1.63E-05</td><td id="8-2g">2.75E-02</td><td id="8-2h">2.65E-02</td><td id="8-2i">1.63E-05</td><td id="8-2j">2.28E-02</td><td id="8-2k">2.37E-02</td></tr>
<tr><td id="8-2l">14</td><td id="8-2m">3.86E-04</td><td id="8-2n">3.63E-02</td><td id="8-2o">5.29E-02</td><td id="8-2p">4.28E-04</td><td id="8-2q">6.48E-02</td><td id="8-2r">8.73E-02</td><td id="8-2s">3.49E-04</td><td id="8-2t">2.48E-02</td><td id="8-2u">3.79E-02</td></tr>
<tr><td id="8-2v">15</td><td id="8-2w">8.52E-08</td><td id="8-2x">0.00E+00</td><td id="8-2y">2.70E-06</td><td id="8-2z">-8.91E-10</td><td id="8-2A">-1.25E-08</td><td id="8-2B">-1.67E-08</td><td id="8-2C">-3.45E-10</td><td id="8-2D">-4.01E-09</td><td id="8-2E">-7.76E-09</td></tr>
<tr><td id="8-2F">16</td><td id="8-2G">-5.69E-06</td><td id="8-2H">8.52E-04</td><td id="8-2I">8.64E-04</td><td id="8-2J">-1.08E-05</td><td id="8-2K">1.30E-03</td><td id="8-2L">1.27E-03</td><td id="8-2M">-3.76E-06</td><td id="8-2N">6.35E-04</td><td id="8-2O">6.52E-04</td></tr>
<tr><td id="8-2P">17</td><td id="8-2Q">-1.44E-04</td><td id="8-2R">-1.13E-03</td><td id="8-2S">-2.69E-03</td><td id="8-2T">-2.13E-04</td><td id="8-2U">-1.66E-03</td><td id="8-2V">-3.97E-03</td><td id="8-2W">-1.09E-04</td><td id="8-2X">-8.50E-04</td><td id="8-2Y">-2.03E-03</td></tr>
<tr><td id="8-2Z">18</td><td id="8-30">9.92E-04</td><td id="8-31">7.38E-03</td><td id="8-32">1.44E-02</td><td id="8-33">1.68E-03</td><td id="8-34">1.21E-02</td><td id="8-35">2.35E-02</td><td id="8-36">7.05E-04</td><td id="8-37">5.32E-03</td><td id="8-38">1.04E-02</td></tr>
<tr><td id="8-39">19</td><td id="8-3a">3.62E-03</td><td id="8-3b">2.38E-02</td><td id="8-3c">4.66E-02</td><td id="8-3d">4.76E-03</td><td id="8-3e">2.94E-02</td><td id="8-3f">5.73E-02</td><td id="8-3g">2.92E-03</td><td id="8-3h">2.00E-02</td><td id="8-3i">3.93E-02</td></tr>
<tr><td id="8-3j">20</td><td id="8-3k">1.53E-06</td><td id="8-3l">2.08E-03</td><td id="8-3m">3.51E-03</td><td id="8-3n">3.09E-06</td><td id="8-3o">3.90E-03</td><td id="8-3p">6.58E-03</td><td id="8-3q">9.72E-07</td><td id="8-3r">1.42E-03</td><td id="8-3s">2.39E-03</td></tr>
<tr><td id="8-3t">21</td><td id="8-3u">-1.85E-04</td><td id="8-3v">3.69E-02</td><td id="8-3w">6.01E-02</td><td id="8-3x">-1.92E-04</td><td id="8-3y">3.87E-02</td><td id="8-3z">6.27E-02</td><td id="8-3A">-1.78E-04</td><td id="8-3B">3.53E-02</td><td id="8-3C">5.77E-02</td></tr>
<tr><td id="8-3D">22</td><td id="8-3E">1.77E-03</td><td id="8-3F">4.46E-02</td><td id="8-3G">7.44E-02</td><td id="8-3H">2.91E-03</td><td id="8-3I">6.60E-02</td><td id="8-3J">1.06E-01</td><td id="8-3K">1.28E-03</td><td id="8-3L">3.38E-02</td><td id="8-3M">5.79E-02</td></tr>
<tr><td id="8-3N">23</td><td id="8-3O">1.59E-04</td><td id="8-3P">1.35E-03</td><td id="8-3Q">2.60E-03</td><td id="8-3R">3.19E-04</td><td id="8-3S">2.68E-03</td><td id="8-3T">5.16E-03</td><td id="8-3U">1.06E-04</td><td id="8-3V">8.99E-04</td><td id="8-3W">1.73E-03</td></tr>
<tr><td id="8-3X">24</td><td id="8-3Y">8.45E-05</td><td id="8-3Z">3.45E-04</td><td id="8-40">5.48E-04</td><td id="8-41">1.11E-04</td><td id="8-42">4.55E-04</td><td id="8-43">7.15E-04</td><td id="8-44">6.82E-05</td><td id="8-45">2.78E-04</td><td id="8-46">4.41E-04</td></tr>
<tr><td id="8-47">25</td><td id="8-48">-3.46E-04</td><td id="8-49">-3.67E-03</td><td id="8-4a">-7.35E-03</td><td id="8-4b">-3.97E-04</td><td id="8-4c">-4.17E-03</td><td id="8-4d">-8.36E-03</td><td id="8-4e">-3.07E-04</td><td id="8-4f">-3.28E-03</td><td id="8-4g">-6.56E-03</td></tr>
<tr><td id="8-4h">26</td><td id="8-4i">5.78E-03</td><td id="8-4j">3.78E-02</td><td id="8-4k">7.04E-02</td><td id="8-4l">1.34E-02</td><td id="8-4m">7.03E-02</td><td id="8-4n">1.30E-01</td><td id="8-4o">3.67E-03</td><td id="8-4p">2.59E-02</td><td id="8-4q">4.84E-02</td></tr>
<tr><td id="8-4r">27</td><td id="8-4s">2.14E-02</td><td id="8-4t">1.25E-01</td><td id="8-4u">2.36E-01</td><td id="8-4v">7.52E-02</td><td id="8-4w">2.21E-01</td><td id="8-4x">4.03E-01</td><td id="8-4y">1.17E-02</td><td id="8-4z">8.89E-02</td><td id="8-4A">1.68E-01</td></tr>
<tr><td id="8-4B">28</td><td id="8-4C">1.21E-03</td><td id="8-4D">5.05E-03</td><td id="8-4E">8.06E-03</td><td id="8-4F">3.39E-03</td><td id="8-4G">9.51E-03</td><td id="8-4H">1.57E-02</td><td id="8-4I">6.29E-04</td><td id="8-4J">3.38E-03</td><td id="8-4K">5.25E-03</td></tr>
<tr><td id="8-4L">29</td><td id="8-4M">6.10E-06</td><td id="8-4N">1.68E-04</td><td id="8-4O">1.84E-04</td><td id="8-4P">1.71E-05</td><td id="8-4Q">3.58E-04</td><td id="8-4R">4.01E-04</td><td id="8-4S">3.51E-06</td><td id="8-4T">1.11E-04</td><td id="8-4U">1.18E-04</td></tr>
<tr><td id="8-4V">30</td><td id="8-4W">2.69E-05</td><td id="8-4X">8.40E-03</td><td id="8-4Y">1.30E-02</td><td id="8-4Z">5.30E-05</td><td id="8-50">1.60E-02</td><td id="8-51">2.46E-02</td><td id="8-52">1.80E-05</td><td id="8-53">5.69E-03</td><td id="8-54">8.79E-03</td></tr>
<tr><td id="8-55">31</td><td id="8-56">-1.30E-03</td><td id="8-57">1.38E-01</td><td id="8-58">2.03E-01</td><td id="8-59">-1.34E-03</td><td id="8-5a">1.51E-01</td><td id="8-5b">2.14E-01</td><td id="8-5c">-1.25E-03</td><td id="8-5d">1.28E-01</td><td id="8-5e">1.92E-01</td></tr>
<tr><td id="8-5f">32</td><td id="8-5g">-3.13E-03</td><td id="8-5h">-2.20E-02</td><td id="8-5i">-5.51E-02</td><td id="8-5j">-2.75E-03</td><td id="8-5k">-1.63E-02</td><td id="8-5l">-5.24E-02</td><td id="8-5m">-3.47E-03</td><td id="8-5n">-2.41E-02</td><td id="8-5o">-5.33E-02</td></tr>
<tr><td id="8-5p">33</td><td id="8-5q">-1.87E-05</td><td id="8-5r">-1.90E-04</td><td id="8-5s">-6.65E-04</td><td id="8-5t">-3.57E-05</td><td id="8-5u">-3.22E-04</td><td id="8-5v">-1.26E-03</td><td id="8-5w">-1.26E-05</td><td id="8-5x">-1.30E-04</td><td id="8-5y">-4.48E-04</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='812a75d3-169a-4eaa-9ea3-49e240fb043a'></a>

<table id="9-1">
<tr><td id="9-2">34</td><td id="9-3">2.75E-04</td><td id="9-4">-5.21E-04</td><td id="9-5">2.49E-03</td><td id="9-6">3.79E-04</td><td id="9-7">-4.51E-04</td><td id="9-8">3.60E-03</td><td id="9-9">2.14E-04</td><td id="9-a">-5.15E-04</td><td id="9-b">1.87E-03</td></tr>
<tr><td id="9-c">35</td><td id="9-d">1.12E-04</td><td id="9-e">1.90E-03</td><td id="9-f">2.98E-03</td><td id="9-g">1.57E-04</td><td id="9-h">2.28E-03</td><td id="9-i">3.54E-03</td><td id="9-j">9.02E-05</td><td id="9-k">1.66E-03</td><td id="9-l">2.63E-03</td></tr>
<tr><td id="9-m">36</td><td id="9-n">1.33E-04</td><td id="9-o">-1.05E-02</td><td id="9-p">1.68E-02</td><td id="9-q">1.46E-04</td><td id="9-r">1.72E-02</td><td id="9-s">5.54E-02</td><td id="9-t">1.23E-04</td><td id="9-u">-1.98E-02</td><td id="9-v">-2.06E-03</td></tr>
<tr><td id="9-w">37</td><td id="9-x">-1.04E-03</td><td id="9-y">-1.18E-02</td><td id="9-z">-3.51E-02</td><td id="9-A">-9.65E-04</td><td id="9-B">-9.04E-03</td><td id="9-C">-3.52E-02</td><td id="9-D">-1.11E-03</td><td id="9-E">-1.30E-02</td><td id="9-F">-3.32E-02</td></tr>
<tr><td id="9-G">38</td><td id="9-H">-2.79E-05</td><td id="9-I">-1.03E-03</td><td id="9-J">-1.16E-03</td><td id="9-K">-4.26E-05</td><td id="9-L">-1.82E-03</td><td id="9-M">-2.02E-03</td><td id="9-N">-2.09E-05</td><td id="9-O">-7.20E-04</td><td id="9-P">-8.14E-04</td></tr>
<tr><td id="9-Q">39</td><td id="9-R">-5.65E-05</td><td id="9-S">5.39E-04</td><td id="9-T">-3.55E-04</td><td id="9-U">-6.40E-05</td><td id="9-V">6.52E-04</td><td id="9-W">-4.01E-04</td><td id="9-X">-5.06E-05</td><td id="9-Y">4.57E-04</td><td id="9-Z">-3.28E-04</td></tr>
<tr><td id="9-10">40</td><td id="9-11">-2.95E-05</td><td id="9-12">-7.09E-04</td><td id="9-13">-9.17E-04</td><td id="9-14">-5.23E-05</td><td id="9-15">-1.30E-03</td><td id="9-16">-1.68E-03</td><td id="9-17">-2.04E-05</td><td id="9-18">-4.85E-04</td><td id="9-19">-6.28E-04</td></tr>
<tr><td id="9-1a">41</td><td id="9-1b">1.49E-03</td><td id="9-1c">1.49E-02</td><td id="9-1d">4.07E-02</td><td id="9-1e">3.14E-03</td><td id="9-1f">3.20E-02</td><td id="9-1g">7.40E-02</td><td id="9-1h">9.75E-04</td><td id="9-1i">9.25E-03</td><td id="9-1j">2.75E-02</td></tr>
<tr><td id="9-1k">42</td><td id="9-1l">-7.24E-02</td><td id="9-1m">-6.99E-01</td><td id="9-1n">-1.13E+00</td><td id="9-1o">-2.96E-02</td><td id="9-1p">-1.25E+00</td><td id="9-1q">-1.96E+00</td><td id="9-1r">-6.09E-01</td><td id="9-1s">-4.38E-01</td><td id="9-1t">-9.27E-01</td></tr>
<tr><td id="9-1u">43</td><td id="9-1v">-1.52E-02</td><td id="9-1w">-1.46E-01</td><td id="9-1x">-2.35E-01</td><td id="9-1y">-1.73E-02</td><td id="9-1z">-2.83E-01</td><td id="9-1A">-4.57E-01</td><td id="9-1B">-1.34E-02</td><td id="9-1C">-9.80E-02</td><td id="9-1D">-1.59E-01</td></tr>
<tr><td id="9-1E">44</td><td id="9-1F">4.40E-02</td><td id="9-1G">6.40E-01</td><td id="9-1H">9.24E-01</td><td id="9-1I">8.15E-01</td><td id="9-1J">6.67E-01</td><td id="9-1K">1.21E+00</td><td id="9-1L">1.94E-02</td><td id="9-1M">5.70E-01</td><td id="9-1N">8.20E-01</td></tr>
<tr><td id="9-1O">45</td><td id="9-1P">2.92E-03</td><td id="9-1Q">1.20E-02</td><td id="9-1R">1.97E-02</td><td id="9-1S">7.07E-03</td><td id="9-1T">2.27E-02</td><td id="9-1U">3.73E-02</td><td id="9-1V">1.70E-03</td><td id="9-1W">8.04E-03</td><td id="9-1X">1.32E-02</td></tr>
<tr><td id="9-1Y">46</td><td id="9-1Z">4.20E-02</td><td id="9-20">1.91E-01</td><td id="9-21">4.19E-01</td><td id="9-22">6.96E-01</td><td id="9-23">1.70E-01</td><td id="9-24">7.61E-01</td><td id="9-25">1.94E-02</td><td id="9-26">1.65E-01</td><td id="9-27">3.53E-01</td></tr>
<tr><td id="9-28">47</td><td id="9-29">1.31E-03</td><td id="9-2a">2.75E-03</td><td id="9-2b">5.91E-03</td><td id="9-2c">2.73E-03</td><td id="9-2d">5.35E-03</td><td id="9-2e">1.15E-02</td><td id="9-2f">8.59E-04</td><td id="9-2g">1.86E-03</td><td id="9-2h">3.98E-03</td></tr>
<tr><td id="9-2i">48</td><td id="9-2j">-3.31E-04</td><td id="9-2k">-2.80E-02</td><td id="9-2l">-3.64E-02</td><td id="9-2m">-6.26E-04</td><td id="9-2n">-5.45E-02</td><td id="9-2o">-7.10E-02</td><td id="9-2p">-2.26E-04</td><td id="9-2q">-1.88E-02</td><td id="9-2r">-2.45E-02</td></tr>
<tr><td id="9-2s">49</td><td id="9-2t">-5.90E-03</td><td id="9-2u">-4.53E-01</td><td id="9-2v">-6.07E-01</td><td id="9-2w">-6.32E-03</td><td id="9-2x">-7.20E-01</td><td id="9-2y">-9.73E-01</td><td id="9-2z">-5.63E-03</td><td id="9-2A">-3.44E-01</td><td id="9-2B">-4.50E-01</td></tr>
<tr><td id="9-2C">50</td><td id="9-2D">1.79E-04</td><td id="9-2E">8.50E-03</td><td id="9-2F">2.02E-02</td><td id="9-2G">3.36E-04</td><td id="9-2H">1.70E-02</td><td id="9-2I">3.86E-02</td><td id="9-2J">1.22E-04</td><td id="9-2K">5.66E-03</td><td id="9-2L">1.37E-02</td></tr>
<tr><td id="9-2M">51</td><td id="9-2N">-1.69E-03</td><td id="9-2O">-4.70E-01</td><td id="9-2P">-4.40E-01</td><td id="9-2Q">-1.67E-03</td><td id="9-2R">-6.86E-01</td><td id="9-2S">-6.09E-01</td><td id="9-2T">-1.71E-03</td><td id="9-2U">-3.55E-01</td><td id="9-2V">-3.41E-01</td></tr>
<tr><td id="9-2W">52</td><td id="9-2X">7.98E-04</td><td id="9-2Y">2.02E-01</td><td id="9-2Z">1.72E-01</td><td id="9-30">1.44E-03</td><td id="9-31">2.86E-01</td><td id="9-32">2.54E-01</td><td id="9-33">5.66E-04</td><td id="9-34">1.61E-01</td><td id="9-35">1.33E-01</td></tr>
<tr><td id="9-36">53</td><td id="9-37">-1.42E-04</td><td id="9-38">1.84E-01</td><td id="9-39">1.58E-01</td><td id="9-3a">-1.84E-04</td><td id="9-3b">4.02E-01</td><td id="9-3c">3.42E-01</td><td id="9-3d">-1.08E-04</td><td id="9-3e">1.19E-01</td><td id="9-3f">1.03E-01</td></tr>
<tr><td id="9-3g">54</td><td id="9-3h">1.49E-02</td><td id="9-3i">1.98E-01</td><td id="9-3j">3.27E-01</td><td id="9-3k">2.97E-02</td><td id="9-3l">2.88E-01</td><td id="9-3m">4.42E-01</td><td id="9-3n">9.97E-03</td><td id="9-3o">1.55E-01</td><td id="9-3p">2.66E-01</td></tr>
<tr><td id="9-3q">55</td><td id="9-3r">6.58E-02</td><td id="9-3s">-4.04E-01</td><td id="9-3t">-2.07E-01</td><td id="9-3u">6.99E-01</td><td id="9-3v">-7.09E-01</td><td id="9-3w">1.19E-01</td><td id="9-3x">3.77E-02</td><td id="9-3y">-3.15E-01</td><td id="9-3z">-1.81E-01</td></tr>
<tr><td id="9-3A">56</td><td id="9-3B">-1.22E-03</td><td id="9-3C">-9.41E-03</td><td id="9-3D">-2.69E-02</td><td id="9-3E">-2.31E-03</td><td id="9-3F">-1.30E-02</td><td id="9-3G">-4.54E-02</td><td id="9-3H">-8.33E-04</td><td id="9-3I">-7.18E-03</td><td id="9-3J">-1.91E-02</td></tr>
<tr><td id="9-3K">57</td><td id="9-3L">-7.97E-02</td><td id="9-3M">2.16E-01</td><td id="9-3N">-9.08E-02</td><td id="9-3O">-6.05E-02</td><td id="9-3P">3.27E-01</td><td id="9-3Q">-7.06E-02</td><td id="9-3R">-1.64E-01</td><td id="9-3S">1.84E-01</td><td id="9-3T">-1.23E-01</td></tr>
<tr><td id="9-3U">58</td><td id="9-3V">-1.05E-04</td><td id="9-3W">3.29E-03</td><td id="9-3X">1.81E-02</td><td id="9-3Y">-1.76E-04</td><td id="9-3Z">1.02E-02</td><td id="9-40">3.43E-02</td><td id="9-41">-7.47E-05</td><td id="9-42">1.58E-03</td><td id="9-43">1.22E-02</td></tr>
<tr><td id="9-44">59</td><td id="9-45">-4.20E-04</td><td id="9-46">-3.89E-01</td><td id="9-47">-3.47E-01</td><td id="9-48">-5.62E-04</td><td id="9-49">-4.92E-01</td><td id="9-4a">-4.40E-01</td><td id="9-4b">-3.33E-04</td><td id="9-4c">-3.35E-01</td><td id="9-4d">-2.96E-01</td></tr>
<tr><td id="9-4e">60</td><td id="9-4f">3.79E-08</td><td id="9-4g">-6.53E-05</td><td id="9-4h">-7.28E-05</td><td id="9-4i">-7.25E-08</td><td id="9-4j">-7.87E-05</td><td id="9-4k">-9.12E-05</td><td id="9-4l">-6.18E-08</td><td id="9-4m">-5.67E-05</td><td id="9-4n">-6.51E-05</td></tr>
<tr><td id="9-4o">61</td><td id="9-4p">8.52E-08</td><td id="9-4q">9.33E-06</td><td id="9-4r">1.42E-05</td><td id="9-4s">2.78E-10</td><td id="9-4t">8.75E-06</td><td id="9-4u">1.00E-05</td><td id="9-4v">1.13E-10</td><td id="9-4w">8.42E-06</td><td id="9-4x">9.80E-06</td></tr>
<tr><td id="9-4y">62</td><td id="9-4z">5.86E-05</td><td id="9-4A">-3.63E-02</td><td id="9-4B">-3.83E-02</td><td id="9-4C">6.11E-05</td><td id="9-4D">-3.16E-02</td><td id="9-4E">-3.72E-02</td><td id="9-4F">5.63E-05</td><td id="9-4G">-3.47E-02</td><td id="9-4H">-3.56E-02</td></tr>
<tr><td id="9-4I">63</td><td id="9-4J">1.19E-05</td><td id="9-4K">2.77E-03</td><td id="9-4L">4.19E-03</td><td id="9-4M">1.65E-05</td><td id="9-4N">4.44E-03</td><td id="9-4O">6.66E-03</td><td id="9-4P">9.21E-06</td><td id="9-4Q">2.01E-03</td><td id="9-4R">3.06E-03</td></tr>
<tr><td id="9-4S">64</td><td id="9-4T">6.25E-05</td><td id="9-4U">2.54E-03</td><td id="9-4V">4.50E-03</td><td id="9-4W">9.05E-05</td><td id="9-4X">3.85E-03</td><td id="9-4Y">6.73E-03</td><td id="9-4Z">4.77E-05</td><td id="9-50">1.90E-03</td><td id="9-51">3.37E-03</td></tr>
<tr><td id="9-52">65</td><td id="9-53">-2.84E-04</td><td id="9-54">-4.35E-03</td><td id="9-55">-9.37E-03</td><td id="9-56">-4.54E-04</td><td id="9-57">-6.88E-03</td><td id="9-58">-1.49E-02</td><td id="9-59">-2.07E-04</td><td id="9-5a">-3.19E-03</td><td id="9-5b">-6.83E-03</td></tr>
<tr><td id="9-5c">66</td><td id="9-5d">-1.03E-03</td><td id="9-5e">-1.19E-02</td><td id="9-5f">-2.64E-02</td><td id="9-5g">-1.17E-03</td><td id="9-5h">-1.39E-02</td><td id="9-5i">-3.14E-02</td><td id="9-5j">-9.16E-04</td><td id="9-5k">-1.04E-02</td><td id="9-5l">-2.28E-02</td></tr>
<tr><td id="9-5m">67</td><td id="9-5n">-2.25E-05</td><td id="9-5o">-5.41E-04</td><td id="9-5p">-1.10E-03</td><td id="9-5q">-3.96E-05</td><td id="9-5r">-1.00E-03</td><td id="9-5s">-2.04E-03</td><td id="9-5t">-1.56E-05</td><td id="9-5u">-3.70E-04</td><td id="9-5v">-7.54E-04</td></tr>
<tr><td id="9-5w">68</td><td id="9-5x">-2.65E-05</td><td id="9-5y">9.00E-03</td><td id="9-5z">1.32E-02</td><td id="9-5A">-2.75E-05</td><td id="9-5B">9.33E-03</td><td id="9-5C">1.37E-02</td><td id="9-5D">-2.58E-05</td><td id="9-5E">8.70E-03</td><td id="9-5F">1.28E-02</td></tr>
<tr><td id="9-5G">69</td><td id="9-5H">-1.06E-03</td><td id="9-5I">-4.14E-02</td><td id="9-5J">-6.50E-02</td><td id="9-5K">-1.60E-03</td><td id="9-5L">-4.77E-02</td><td id="9-5M">-8.12E-02</td><td id="9-5N">-7.96E-04</td><td id="9-5O">-3.65E-02</td><td id="9-5P">-5.48E-02</td></tr>
<tr><td id="9-5Q">70</td><td id="9-5R">-1.08E-04</td><td id="9-5S">-9.33E-06</td><td id="9-5T">-8.10E-04</td><td id="9-5U">-2.11E-04</td><td id="9-5V">-1.23E-05</td><td id="9-5W">-1.58E-03</td><td id="9-5X">-7.27E-05</td><td id="9-5Y">-6.07E-06</td><td id="9-5Z">-5.42E-04</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='577bb6f4-7fc8-4736-8e6a-3d86c01b7449'></a>

<table id="10-1">
<tr><td id="10-2">71</td><td id="10-3">-2.54E-05</td><td id="10-4">-1.17E-04</td><td id="10-5">-2.45E-04</td><td id="10-6">-3.31E-05</td><td id="10-7">-1.53E-04</td><td id="10-8">-3.23E-04</td><td id="10-9">-2.07E-05</td><td id="10-a">-9.38E-05</td><td id="10-b">-1.99E-04</td></tr>
<tr><td id="10-c">72</td><td id="10-d">1.27E-04</td><td id="10-e">2.27E-03</td><td id="10-f">4.22E-03</td><td id="10-g">1.48E-04</td><td id="10-h">2.61E-03</td><td id="10-i">4.83E-03</td><td id="10-j">1.11E-04</td><td id="10-k">2.01E-03</td><td id="10-l">3.74E-03</td></tr>
<tr><td id="10-m">73</td><td id="10-n">-1.45E-03</td><td id="10-o">-1.49E-02</td><td id="10-p">-2.99E-02</td><td id="10-q">-2.35E-03</td><td id="10-r">-2.44E-02</td><td id="10-s">-4.94E-02</td><td id="10-t">-1.05E-03</td><td id="10-u">-1.08E-02</td><td id="10-v">-2.14E-02</td></tr>
<tr><td id="10-w">74</td><td id="10-x">-5.40E-03</td><td id="10-y">-4.28E-02</td><td id="10-z">-8.95E-02</td><td id="10-A">-6.07E-03</td><td id="10-B">-5.23E-02</td><td id="10-C">-1.12E-01</td><td id="10-D">-4.83E-03</td><td id="10-E">-3.66E-02</td><td id="10-F">-7.49E-02</td></tr>
<tr><td id="10-G">75</td><td id="10-H">-7.84E-04</td><td id="10-I">-9.17E-05</td><td id="10-J">-7.37E-04</td><td id="10-K">-1.09E-03</td><td id="10-L">7.26E-05</td><td id="10-M">-5.89E-04</td><td id="10-N">-5.72E-04</td><td id="10-O">-1.06E-04</td><td id="10-P">-6.18E-04</td></tr>
<tr><td id="10-Q">76</td><td id="10-R">-3.83E-05</td><td id="10-S">9.33E-06</td><td id="10-T">-6.85E-06</td><td id="10-U">-7.62E-05</td><td id="10-V">1.89E-05</td><td id="10-W">-2.26E-05</td><td id="10-X">-2.56E-05</td><td id="10-Y">5.82E-06</td><td id="10-Z">-8.67E-06</td></tr>
<tr><td id="10-10">77</td><td id="10-11">-1.25E-04</td><td id="10-12">-2.54E-03</td><td id="10-13">-4.69E-03</td><td id="10-14">-2.21E-04</td><td id="10-15">-4.74E-03</td><td id="10-16">-8.74E-03</td><td id="10-17">-8.76E-05</td><td id="10-18">-1.73E-03</td><td id="10-19">-3.21E-03</td></tr>
<tr><td id="10-1a">78</td><td id="10-1b">-1.40E-04</td><td id="10-1c">3.02E-02</td><td id="10-1d">3.88E-02</td><td id="10-1e">-1.45E-04</td><td id="10-1f">3.17E-02</td><td id="10-1g">4.03E-02</td><td id="10-1h">-1.35E-04</td><td id="10-1i">2.88E-02</td><td id="10-1j">3.74E-02</td></tr>
<tr><td id="10-1k">79</td><td id="10-1l">1.18E-03</td><td id="10-1m">3.82E-02</td><td id="10-1n">6.13E-02</td><td id="10-1o">1.30E-03</td><td id="10-1p">5.66E-02</td><td id="10-1q">8.22E-02</td><td id="10-1r">1.08E-03</td><td id="10-1s">2.90E-02</td><td id="10-1t">4.94E-02</td></tr>
<tr><td id="10-1u">80</td><td id="10-1v">-6.23E-05</td><td id="10-1w">-5.88E-04</td><td id="10-1x">-9.23E-04</td><td id="10-1y">-7.55E-05</td><td id="10-1z">-7.35E-04</td><td id="10-1A">-1.15E-03</td><td id="10-1B">-5.32E-05</td><td id="10-1C">-4.87E-04</td><td id="10-1D">-7.67E-04</td></tr>
<tr><td id="10-1E">81</td><td id="10-1F">2.41E-04</td><td id="10-1G">2.58E-02</td><td id="10-1H">3.68E-02</td><td id="10-1I">2.48E-04</td><td id="10-1J">3.55E-02</td><td id="10-1K">4.83E-02</td><td id="10-1L">2.33E-04</td><td id="10-1M">2.01E-02</td><td id="10-1N">2.97E-02</td></tr>
<tr><td id="10-1O">82</td><td id="10-1P">1.99E-05</td><td id="10-1Q">2.34E-03</td><td id="10-1R">3.28E-03</td><td id="10-1S">2.26E-05</td><td id="10-1T">2.78E-03</td><td id="10-1U">3.87E-03</td><td id="10-1V">1.75E-05</td><td id="10-1W">2.02E-03</td><td id="10-1X">2.84E-03</td></tr>
<tr><td id="10-1Y">83</td><td id="10-1Z">-5.66E-04</td><td id="10-20">-1.25E-02</td><td id="10-21">-2.27E-02</td><td id="10-22">-9.72E-04</td><td id="10-23">-1.83E-02</td><td id="10-24">-3.42E-02</td><td id="10-25">-3.99E-04</td><td id="10-26">-9.53E-03</td><td id="10-27">-1.70E-02</td></tr>
<tr><td id="10-28">84</td><td id="10-29">8.67E-06</td><td id="10-2a">-8.60E-02</td><td id="10-2b">-8.78E-02</td><td id="10-2c">-1.80E-03</td><td id="10-2d">-1.67E-01</td><td id="10-2e">-1.90E-01</td><td id="10-2f">4.00E-04</td><td id="10-2g">-5.93E-02</td><td id="10-2h">-5.98E-02</td></tr>
<tr><td id="10-2i">85</td><td id="10-2j">-1.15E-04</td><td id="10-2k">-1.80E-02</td><td id="10-2l">-1.89E-02</td><td id="10-2m">-3.36E-04</td><td id="10-2n">-3.54E-02</td><td id="10-2o">-3.76E-02</td><td id="10-2p">-6.30E-05</td><td id="10-2q">-1.21E-02</td><td id="10-2r">-1.26E-02</td></tr>
<tr><td id="10-2s">86</td><td id="10-2t">5.41E-04</td><td id="10-2u">1.06E-01</td><td id="10-2v">1.10E-01</td><td id="10-2w">-2.65E-05</td><td id="10-2x">1.09E-01</td><td id="10-2y">1.12E-01</td><td id="10-2z">6.87E-04</td><td id="10-2A">1.03E-01</td><td id="10-2B">1.08E-01</td></tr>
<tr><td id="10-2C">87</td><td id="10-2D">-8.13E-04</td><td id="10-2E">8.78E-04</td><td id="10-2F">3.15E-04</td><td id="10-2G">-1.06E-03</td><td id="10-2H">1.98E-03</td><td id="10-2I">1.60E-03</td><td id="10-2J">-6.18E-04</td><td id="10-2K">5.51E-04</td><td id="10-2L">7.35E-05</td></tr>
<tr><td id="10-2M">88</td><td id="10-2N">-5.54E-04</td><td id="10-2O">-3.66E-03</td><td id="10-2P">-5.12E-03</td><td id="10-2Q">-9.81E-04</td><td id="10-2R">-3.06E-03</td><td id="10-2S">-5.45E-03</td><td id="10-2T">-2.98E-04</td><td id="10-2U">-3.75E-03</td><td id="10-2V">-4.17E-03</td></tr>
<tr><td id="10-2W">89</td><td id="10-2X">-3.44E-05</td><td id="10-2Y">-3.73E-05</td><td id="10-2Z">-5.84E-05</td><td id="10-30">-6.60E-05</td><td id="10-31">-7.00E-05</td><td id="10-32">-1.10E-04</td><td id="10-33">-2.31E-05</td><td id="10-34">-2.39E-05</td><td id="10-35">-3.83E-05</td></tr>
<tr><td id="10-36">90</td><td id="10-37">-1.61E-06</td><td id="10-38">4.23E-04</td><td id="10-39">8.51E-04</td><td id="10-3a">-4.38E-06</td><td id="10-3b">8.32E-04</td><td id="10-3c">1.66E-03</td><td id="10-3d">-9.16E-07</td><td id="10-3e">2.84E-04</td><td id="10-3f">5.74E-04</td></tr>
<tr><td id="10-3g">91</td><td id="10-3h">-2.69E-04</td><td id="10-3i">1.97E-03</td><td id="10-3j">5.83E-03</td><td id="10-3k">-2.91E-04</td><td id="10-3l">-3.42E-03</td><td id="10-3m">-9.88E-04</td><td id="10-3n">-2.49E-04</td><td id="10-3o">1.20E-03</td><td id="10-3p">4.06E-03</td></tr>
<tr><td id="10-3q">92</td><td id="10-3r">6.01E-05</td><td id="10-3s">4.30E-03</td><td id="10-3t">7.12E-03</td><td id="10-3u">1.09E-04</td><td id="10-3v">8.47E-03</td><td id="10-3w">1.35E-02</td><td id="10-3x">4.14E-05</td><td id="10-3y">2.87E-03</td><td id="10-3z">4.82E-03</td></tr>
<tr><td id="10-3A">93</td><td id="10-3B">-6.32E-05</td><td id="10-3C">-8.94E-02</td><td id="10-3D">-7.41E-02</td><td id="10-3E">-6.72E-05</td><td id="10-3F">-1.26E-01</td><td id="10-3G">-9.88E-02</td><td id="10-3H">-5.97E-05</td><td id="10-3I">-6.82E-02</td><td id="10-3J">-5.89E-02</td></tr>
<tr><td id="10-3K">94</td><td id="10-3L">-6.52E-04</td><td id="10-3M">-2.79E-03</td><td id="10-3N">-8.97E-03</td><td id="10-3O">-7.66E-04</td><td id="10-3P">-4.10E-03</td><td id="10-3Q">-1.01E-02</td><td id="10-3R">-5.94E-04</td><td id="10-3S">-2.13E-03</td><td id="10-3T">-8.28E-03</td></tr>
<tr><td id="10-3U">95</td><td id="10-3V">-3.26E-04</td><td id="10-3W">-1.98E-03</td><td id="10-3X">-2.14E-04</td><td id="10-3Y">-5.47E-04</td><td id="10-3Z">-2.28E-03</td><td id="10-40">-2.99E-04</td><td id="10-41">-2.31E-04</td><td id="10-42">-1.71E-03</td><td id="10-43">-1.96E-04</td></tr>
<tr><td id="10-44">96</td><td id="10-45">9.60E-04</td><td id="10-46">-1.99E-03</td><td id="10-47">-6.10E-04</td><td id="10-48">1.08E-03</td><td id="10-49">-2.34E-03</td><td id="10-4a">-1.34E-03</td><td id="10-4b">8.18E-04</td><td id="10-4c">-1.56E-03</td><td id="10-4d">6.29E-05</td></tr>
<tr><td id="10-4e">97</td><td id="10-4f">-3.84E-04</td><td id="10-4g">-8.36E-04</td><td id="10-4h">-1.26E-03</td><td id="10-4i">-4.52E-04</td><td id="10-4j">-3.06E-03</td><td id="10-4k">-3.02E-03</td><td id="10-4l">-3.30E-04</td><td id="10-4m">-3.54E-04</td><td id="10-4n">-7.13E-04</td></tr>
<tr><td id="10-4o">98</td><td id="10-4p">-1.51E-05</td><td id="10-4q">9.64E-05</td><td id="10-4r">-1.87E-06</td><td id="10-4s">-4.75E-05</td><td id="10-4t">1.91E-04</td><td id="10-4u">-2.63E-05</td><td id="10-4v">-7.81E-06</td><td id="10-4w">6.36E-05</td><td id="10-4x">-3.95E-06</td></tr>
<tr><td id="10-4y">99</td><td id="10-4z">-7.91E-04</td><td id="10-4A">2.75E-03</td><td id="10-4B">1.78E-03</td><td id="10-4C">-1.77E-03</td><td id="10-4D">5.49E-03</td><td id="10-4E">3.23E-03</td><td id="10-4F">-4.34E-04</td><td id="10-4G">1.82E-03</td><td id="10-4H">1.21E-03</td></tr>
<tr><td id="10-4I">100</td><td id="10-4J">5.31E-04</td><td id="10-4K">3.38E-03</td><td id="10-4L">7.88E-03</td><td id="10-4M">1.04E-03</td><td id="10-4N">6.91E-03</td><td id="10-4O">1.57E-02</td><td id="10-4P">3.57E-04</td><td id="10-4Q">2.23E-03</td><td id="10-4R">5.25E-03</td></tr>
<tr><td id="10-4S">101</td><td id="10-4T">1.44E-03</td><td id="10-4U">1.35E-03</td><td id="10-4V">2.06E-03</td><td id="10-4W">2.94E-03</td><td id="10-4X">-4.21E-04</td><td id="10-4Y">1.81E-03</td><td id="10-4Z">9.51E-04</td><td id="10-50">1.20E-03</td><td id="10-51">1.62E-03</td></tr>
<tr><td id="10-52">102</td><td id="10-53">3.96E-06</td><td id="10-54">4.46E-03</td><td id="10-55">6.15E-03</td><td id="10-56">3.94E-06</td><td id="10-57">4.50E-03</td><td id="10-58">6.20E-03</td><td id="10-59">3.87E-06</td><td id="10-5a">4.43E-03</td><td id="10-5b">6.10E-03</td></tr>
<tr><td id="10-5c">103</td><td id="10-5d">-2.62E-06</td><td id="10-5e">7.62E-04</td><td id="10-5f">9.37E-04</td><td id="10-5g">-2.68E-06</td><td id="10-5h">7.62E-04</td><td id="10-5i">9.35E-04</td><td id="10-5j">-2.68E-06</td><td id="10-5k">7.60E-04</td><td id="10-5l">9.32E-04</td></tr>
<tr><td id="10-5m">104</td><td id="10-5n">3.12E-05</td><td id="10-5o">8.49E-03</td><td id="10-5p">1.11E-02</td><td id="10-5q">3.16E-05</td><td id="10-5r">8.61E-03</td><td id="10-5s">1.13E-02</td><td id="10-5t">3.09E-05</td><td id="10-5u">8.38E-03</td><td id="10-5v">1.10E-02</td></tr>
<tr><td id="10-5w">105</td><td id="10-5x">6.30E-05</td><td id="10-5y">8.42E-03</td><td id="10-5z">1.19E-02</td><td id="10-5A">6.46E-05</td><td id="10-5B">8.66E-03</td><td id="10-5C">1.23E-02</td><td id="10-5D">6.15E-05</td><td id="10-5E">8.20E-03</td><td id="10-5F">1.16E-02</td></tr>
<tr><td id="10-5G">106</td><td id="10-5H">-1.29E-03</td><td id="10-5I">-3.63E-02</td><td id="10-5J">-5.64E-02</td><td id="10-5K">-1.35E-03</td><td id="10-5L">-4.24E-02</td><td id="10-5M">-6.62E-02</td><td id="10-5N">-1.23E-03</td><td id="10-5O">-3.17E-02</td><td id="10-5P">-4.93E-02</td></tr>
<tr><td id="10-5Q">107</td><td id="10-5R">-4.09E-04</td><td id="10-5S">-5.38E-03</td><td id="10-5T">-8.07E-03</td><td id="10-5U">-4.74E-04</td><td id="10-5V">-8.94E-03</td><td id="10-5W">-1.27E-02</td><td id="10-5X">-3.60E-04</td><td id="10-5Y">-3.94E-03</td><td id="10-5Z">-6.10E-03</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='415779aa-56f7-4962-bc6e-d3beed058301'></a>

<table id="11-1">
<tr><td id="11-2">108</td><td id="11-3">-3.91E-06</td><td id="11-4">2.15E-04</td><td id="11-5">3.33E-04</td><td id="11-6">-4.24E-06</td><td id="11-7">2.14E-04</td><td id="11-8">3.30E-04</td><td id="11-9">-3.67E-06</td><td id="11-a">2.15E-04</td><td id="11-b">3.32E-04</td></tr>
<tr><td id="11-c">109</td><td id="11-d">-7.37E-04</td><td id="11-e">-3.71E-03</td><td id="11-f">-7.27E-03</td><td id="11-g">-7.68E-04</td><td id="11-h">-3.94E-03</td><td id="11-i">-7.69E-03</td><td id="11-j">-7.09E-04</td><td id="11-k">-3.51E-03</td><td id="11-l">-6.89E-03</td></tr>
<tr><td id="11-m">110</td><td id="11-n">-2.06E-04</td><td id="11-o">-1.02E-03</td><td id="11-p">-2.15E-03</td><td id="11-q">-2.30E-04</td><td id="11-r">-1.42E-03</td><td id="11-s">-2.95E-03</td><td id="11-t">-1.84E-04</td><td id="11-u">-8.22E-04</td><td id="11-v">-1.75E-03</td></tr>
<tr><td id="11-w">111</td><td id="11-x">-7.70E-06</td><td id="11-y">8.44E-04</td><td id="11-z">1.04E-03</td><td id="11-A">-7.85E-06</td><td id="11-B">8.57E-04</td><td id="11-C">1.06E-03</td><td id="11-D">-7.74E-06</td><td id="11-E">8.37E-04</td><td id="11-F">1.04E-03</td></tr>
<tr><td id="11-G">112</td><td id="11-H">-2.23E-04</td><td id="11-I">-1.44E-02</td><td id="11-J">-2.20E-02</td><td id="11-K">-2.33E-04</td><td id="11-L">-1.62E-02</td><td id="11-M">-2.48E-02</td><td id="11-N">-2.14E-04</td><td id="11-O">-1.30E-02</td><td id="11-P">-1.98E-02</td></tr>
<tr><td id="11-Q">113</td><td id="11-R">-4.76E-05</td><td id="11-S">-1.81E-03</td><td id="11-T">-2.41E-03</td><td id="11-U">-5.39E-05</td><td id="11-V">-3.16E-03</td><td id="11-W">-4.06E-03</td><td id="11-X">-4.26E-05</td><td id="11-Y">-1.28E-03</td><td id="11-Z">-1.75E-03</td></tr>
<tr><td id="11-10">114</td><td id="11-11">4.62E-06</td><td id="11-12">8.66E-04</td><td id="11-13">1.10E-03</td><td id="11-14">4.55E-06</td><td id="11-15">8.71E-04</td><td id="11-16">1.11E-03</td><td id="11-17">4.53E-06</td><td id="11-18">8.65E-04</td><td id="11-19">1.10E-03</td></tr>
<tr><td id="11-1a">115</td><td id="11-1b">-1.56E-04</td><td id="11-1c">-5.35E-03</td><td id="11-1d">-7.72E-03</td><td id="11-1e">-1.60E-04</td><td id="11-1f">-5.70E-03</td><td id="11-1g">-8.21E-03</td><td id="11-1h">-1.52E-04</td><td id="11-1i">-5.05E-03</td><td id="11-1j">-7.29E-03</td></tr>
<tr><td id="11-1k">116</td><td id="11-1l">-4.76E-05</td><td id="11-1m">-7.52E-04</td><td id="11-1n">-1.02E-03</td><td id="11-1o">-5.45E-05</td><td id="11-1p">-1.25E-03</td><td id="11-1q">-1.59E-03</td><td id="11-1r">-4.21E-05</td><td id="11-1s">-5.48E-04</td><td id="11-1t">-7.74E-04</td></tr>
<tr><td id="11-1u">117</td><td id="11-1v">1.93E-04</td><td id="11-1w">2.46E-02</td><td id="11-1x">3.12E-02</td><td id="11-1y">1.97E-04</td><td id="11-1z">2.53E-02</td><td id="11-1A">3.20E-02</td><td id="11-1B">1.88E-04</td><td id="11-1C">2.39E-02</td><td id="11-1D">3.04E-02</td></tr>
<tr><td id="11-1E">118</td><td id="11-1F">-7.42E-03</td><td id="11-1G">-1.46E-01</td><td id="11-1H">-2.16E-01</td><td id="11-1I">-6.81E-03</td><td id="11-1J">-1.83E-01</td><td id="11-1K">-2.70E-01</td><td id="11-1L">-8.03E-03</td><td id="11-1M">-1.22E-01</td><td id="11-1N">-1.82E-01</td></tr>
<tr><td id="11-1O">119</td><td id="11-1P">-2.43E-03</td><td id="11-1Q">-2.26E-02</td><td id="11-1R">-3.50E-02</td><td id="11-1S">-2.81E-03</td><td id="11-1T">-3.67E-02</td><td id="11-1U">-5.30E-02</td><td id="11-1V">-2.15E-03</td><td id="11-1W">-1.69E-02</td><td id="11-1X">-2.71E-02</td></tr>
<tr><td id="11-1Y">120</td><td id="11-1Z">-7.23E-05</td><td id="11-20">4.94E-04</td><td id="11-21">5.44E-04</td><td id="11-22">-7.50E-05</td><td id="11-23">4.88E-04</td><td id="11-24">5.23E-04</td><td id="11-25">-6.98E-05</td><td id="11-26">5.03E-04</td><td id="11-27">5.57E-04</td></tr>
<tr><td id="11-28">121</td><td id="11-29">-4.48E-03</td><td id="11-2a">-2.10E-02</td><td id="11-2b">-4.13E-02</td><td id="11-2c">-4.30E-03</td><td id="11-2d">-2.18E-02</td><td id="11-2e">-4.25E-02</td><td id="11-2f">-4.64E-03</td><td id="11-2g">-2.04E-02</td><td id="11-2h">-4.04E-02</td></tr>
<tr><td id="11-2i">122</td><td id="11-2j">-1.27E-03</td><td id="11-2k">-5.96E-03</td><td id="11-2l">-1.27E-02</td><td id="11-2m">-1.42E-03</td><td id="11-2n">-8.19E-03</td><td id="11-2o">-1.71E-02</td><td id="11-2p">-1.14E-03</td><td id="11-2q">-4.84E-03</td><td id="11-2r">-1.04E-02</td></tr>
<tr><td id="11-2s">123</td><td id="11-2t">-4.82E-05</td><td id="11-2u">2.29E-03</td><td id="11-2v">2.26E-03</td><td id="11-2w">-4.85E-05</td><td id="11-2x">2.32E-03</td><td id="11-2y">2.29E-03</td><td id="11-2z">-4.77E-05</td><td id="11-2A">2.26E-03</td><td id="11-2B">2.23E-03</td></tr>
<tr><td id="11-2C">124</td><td id="11-2D">-1.21E-03</td><td id="11-2E">-5.43E-02</td><td id="11-2F">-7.73E-02</td><td id="11-2G">-1.24E-03</td><td id="11-2H">-6.49E-02</td><td id="11-2I">-9.21E-02</td><td id="11-2J">-1.18E-03</td><td id="11-2K">-4.68E-02</td><td id="11-2L">-6.67E-02</td></tr>
<tr><td id="11-2M">125</td><td id="11-2N">-2.70E-04</td><td id="11-2O">-6.67E-03</td><td id="11-2P">-8.70E-03</td><td id="11-2Q">-3.07E-04</td><td id="11-2R">-1.15E-02</td><td id="11-2S">-1.42E-02</td><td id="11-2T">-2.41E-04</td><td id="11-2U">-4.77E-03</td><td id="11-2V">-6.42E-03</td></tr>
<tr><td id="11-2W">126</td><td id="11-2X">-1.06E-06</td><td id="11-2Y">1.55E-06</td><td id="11-2Z">4.10E-06</td><td id="11-30">-1.86E-06</td><td id="11-31">-2.02E-06</td><td id="11-32">-3.86E-06</td><td id="11-33">-6.26E-07</td><td id="11-34">-6.88E-07</td><td id="11-35">-1.32E-06</td></tr>
<tr><td id="11-36">127</td><td id="11-37">-6.26E-08</td><td id="11-38">0.00E+00</td><td id="11-39">-2.17E-06</td><td id="11-3a">8.51E-09</td><td id="11-3b">3.97E-08</td><td id="11-3c">8.59E-08</td><td id="11-3d">2.83E-09</td><td id="11-3e">1.34E-08</td><td id="11-3f">2.82E-08</td></tr>
<tr><td id="11-3g">128</td><td id="11-3h">-3.75E-06</td><td id="11-3i">-7.77E-06</td><td id="11-3j">-7.77E-06</td><td id="11-3k">-7.53E-06</td><td id="11-3l">-1.11E-05</td><td id="11-3m">-2.44E-05</td><td id="11-3n">-2.54E-06</td><td id="11-3o">-3.79E-06</td><td id="11-3p">-8.31E-06</td></tr>
<tr><td id="11-3q">129</td><td id="11-3r">-5.91E-08</td><td id="11-3s">-3.11E-06</td><td id="11-3t">-6.26E-06</td><td id="11-3u">3.27E-08</td><td id="11-3v">1.23E-07</td><td id="11-3w">2.69E-07</td><td id="11-3x">1.11E-08</td><td id="11-3y">4.19E-08</td><td id="11-3z">9.18E-08</td></tr>
<tr><td id="11-3A">130</td><td id="11-3B">-4.41E-07</td><td id="11-3C">0.00E+00</td><td id="11-3D">8.56E-07</td><td id="11-3E">-1.03E-06</td><td id="11-3F">2.84E-06</td><td id="11-3G">6.44E-06</td><td id="11-3H">-3.46E-07</td><td id="11-3I">9.51E-07</td><td id="11-3J">2.16E-06</td></tr>
<tr><td id="11-3K">131</td><td id="11-3L">7.21E-08</td><td id="11-3M">-1.55E-06</td><td id="11-3N">-3.16E-06</td><td id="11-3O">-1.19E-09</td><td id="11-3P">3.05E-08</td><td id="11-3Q">6.48E-08</td><td id="11-3R">-5.16E-10</td><td id="11-3S">1.03E-08</td><td id="11-3T">1.86E-08</td></tr>
<tr><td id="11-3U">132</td><td id="11-3V">1.93E-05</td><td id="11-3W">-1.41E-02</td><td id="11-3X">-1.63E-02</td><td id="11-3Y">1.94E-05</td><td id="11-3Z">-1.44E-02</td><td id="11-40">-1.67E-02</td><td id="11-41">1.93E-05</td><td id="11-42">-1.39E-02</td><td id="11-43">-1.60E-02</td></tr>
<tr><td id="11-44">133</td><td id="11-45">7.05E-06</td><td id="11-46">-3.62E-03</td><td id="11-47">-4.12E-03</td><td id="11-48">7.11E-06</td><td id="11-49">-3.67E-03</td><td id="11-4a">-4.18E-03</td><td id="11-4b">7.04E-06</td><td id="11-4c">-3.58E-03</td><td id="11-4d">-4.07E-03</td></tr>
<tr><td id="11-4e">134</td><td id="11-4f">8.35E-05</td><td id="11-4g">-1.79E-02</td><td id="11-4h">-1.97E-02</td><td id="11-4i">8.52E-05</td><td id="11-4j">-1.89E-02</td><td id="11-4k">-2.10E-02</td><td id="11-4l">8.16E-05</td><td id="11-4m">-1.70E-02</td><td id="11-4n">-1.86E-02</td></tr>
<tr><td id="11-4o">135</td><td id="11-4p">1.86E-05</td><td id="11-4q">-8.27E-04</td><td id="11-4r">-1.03E-03</td><td id="11-4s">1.86E-05</td><td id="11-4t">-8.30E-04</td><td id="11-4u">-1.03E-03</td><td id="11-4v">1.83E-05</td><td id="11-4w">-8.22E-04</td><td id="11-4x">-1.02E-03</td></tr>
<tr><td id="11-4y">136</td><td id="11-4z">2.92E-06</td><td id="11-4A">-3.02E-03</td><td id="11-4B">-3.30E-03</td><td id="11-4C">2.91E-06</td><td id="11-4D">-3.07E-03</td><td id="11-4E">-3.37E-03</td><td id="11-4F">2.87E-06</td><td id="11-4G">-2.96E-03</td><td id="11-4H">-3.25E-03</td></tr>
<tr><td id="11-4I">137</td><td id="11-4J">9.57E-06</td><td id="11-4K">-2.04E-03</td><td id="11-4L">-2.14E-03</td><td id="11-4M">9.46E-06</td><td id="11-4N">-2.04E-03</td><td id="11-4O">-2.15E-03</td><td id="11-4P">9.45E-06</td><td id="11-4Q">-2.04E-03</td><td id="11-4R">-2.15E-03</td></tr>
<tr><td id="11-4S">138</td><td id="11-4T">4.90E-05</td><td id="11-4U">-2.28E-02</td><td id="11-4V">-2.49E-02</td><td id="11-4W">4.92E-05</td><td id="11-4X">-2.35E-02</td><td id="11-4Y">-2.57E-02</td><td id="11-4Z">4.87E-05</td><td id="11-50">-2.22E-02</td><td id="11-51">-2.42E-02</td></tr>
<tr><td id="11-52">139</td><td id="11-53">7.45E-06</td><td id="11-54">-2.17E-03</td><td id="11-55">-2.34E-03</td><td id="11-56">7.47E-06</td><td id="11-57">-2.18E-03</td><td id="11-58">-2.36E-03</td><td id="11-59">7.43E-06</td><td id="11-5a">-2.16E-03</td><td id="11-5b">-2.33E-03</td></tr>
<tr><td id="11-5c">140</td><td id="11-5d">4.19E-04</td><td id="11-5e">-5.57E-02</td><td id="11-5f">-5.85E-02</td><td id="11-5g">4.29E-04</td><td id="11-5h">-5.79E-02</td><td id="11-5i">-6.14E-02</td><td id="11-5j">4.09E-04</td><td id="11-5k">-5.36E-02</td><td id="11-5l">-5.59E-02</td></tr>
<tr><td id="11-5m">141</td><td id="11-5n">1.01E-04</td><td id="11-5o">-3.13E-03</td><td id="11-5p">-3.72E-03</td><td id="11-5q">1.01E-04</td><td id="11-5r">-3.15E-03</td><td id="11-5s">-3.75E-03</td><td id="11-5t">9.97E-05</td><td id="11-5u">-3.12E-03</td><td id="11-5v">-3.70E-03</td></tr>
<tr><td id="11-5w">142</td><td id="11-5x">1.51E-05</td><td id="11-5y">-9.72E-03</td><td id="11-5z">-1.00E-02</td><td id="11-5A">1.54E-05</td><td id="11-5B">-9.98E-03</td><td id="11-5C">-1.03E-02</td><td id="11-5D">1.52E-05</td><td id="11-5E">-9.47E-03</td><td id="11-5F">-9.78E-03</td></tr>
<tr><td id="11-5G">143</td><td id="11-5H">-2.15E-07</td><td id="11-5I">-5.32E-04</td><td id="11-5J">-7.04E-04</td><td id="11-5K">-2.49E-07</td><td id="11-5L">-5.30E-04</td><td id="11-5M">-7.04E-04</td><td id="11-5N">-2.50E-07</td><td id="11-5O">-5.29E-04</td><td id="11-5P">-7.03E-04</td></tr>
<tr><td id="11-5Q">144</td><td id="11-5R">-1.14E-06</td><td id="11-5S">-1.82E-03</td><td id="11-5T">-2.30E-03</td><td id="11-5U">-1.16E-06</td><td id="11-5V">-1.82E-03</td><td id="11-5W">-2.31E-03</td><td id="11-5X">-1.16E-06</td><td id="11-5Y">-1.82E-03</td><td id="11-5Z">-2.30E-03</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='1f574762-e6cf-4760-ad28-0b34a7a02f5d'></a>

<table id="12-1">
<tr><td id="12-2">145</td><td id="12-3">3.41E-06</td><td id="12-4">-5.66E-04</td><td id="12-5">-8.59E-04</td><td id="12-6">3.35E-06</td><td id="12-7">-5.60E-04</td><td id="12-8">-8.52E-04</td><td id="12-9">3.34E-06</td><td id="12-a">-5.73E-04</td><td id="12-b">-8.68E-04</td></tr>
<tr><td id="12-c">146</td><td id="12-d">1.96E-07</td><td id="12-e">0.00E+00</td><td id="12-f">2.52E-06</td><td id="12-g">-1.73E-10</td><td id="12-h">-1.39E-06</td><td id="12-i">-1.73E-06</td><td id="12-j">-3.35E-10</td><td id="12-k">-1.39E-06</td><td id="12-l">-1.73E-06</td></tr>
<tr><td id="12-m">147</td><td id="12-n">-8.52E-08</td><td id="12-o">-3.11E-06</td><td id="12-p">-8.22E-07</td><td id="12-q">-7.00E-10</td><td id="12-r">-3.88E-06</td><td id="12-s">-4.79E-06</td><td id="12-t">-8.34E-10</td><td id="12-u">-3.88E-06</td><td id="12-v">-4.78E-06</td></tr>
<tr><td id="12-w">148</td><td id="12-x">-2.05E-07</td><td id="12-y">-3.11E-06</td><td id="12-z">-1.37E-06</td><td id="12-A">3.37E-08</td><td id="12-B">-3.18E-06</td><td id="12-C">-5.15E-06</td><td id="12-D">3.35E-08</td><td id="12-E">-3.19E-06</td><td id="12-F">-5.15E-06</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='5f03a7c4-cf0c-46b2-afb2-ce644a65bfc8'></a>

<table id="13-1">
<tr><td id="13-2">V</td><td id="13-3">reactions</td><td id="13-4">biological process</td></tr>
<tr><td id="13-5">1</td><td id="13-6">[EGFR]+[EGF]↔[EGF-EGFR]</td><td id="13-7">receptor activation</td></tr>
<tr><td id="13-8">2</td><td id="13-9">[EGF-EGFR]+[EGF-EGFR]↔[(EGF-EGFR)2]</td><td id="13-a">receptor activation</td></tr>
<tr><td id="13-b">3</td><td id="13-c">[(EGF-EGFR)2]↔[(EGF-EGFR*)2]</td><td id="13-d">receptor activation</td></tr>
<tr><td id="13-e">4</td><td id="13-f">[(EGF-EGFR*)2-GAP-Grb2]+[Prot]↔[(EGF-EGFR*)2-GAP-Grb2-Prot]</td><td id="13-g">internalization</td></tr>
<tr><td id="13-h">5</td><td id="13-i">[(EGF-EGFR*)2-GAP-Grb2-Prot] → [(EGF-EGFR*)2-GAP-Grb2]+[Prot]</td><td id="13-j">internalization</td></tr>
<tr><td id="13-k">6</td><td id="13-l">[EGFR] ↔ [EGFRi]</td><td id="13-m">internalization</td></tr>
<tr><td id="13-n">7</td><td id="13-o">[(EGF-EGFR*)2] → [(EGF-EGFR*)2]</td><td id="13-p">internalization</td></tr>
<tr><td id="13-q">8</td><td id="13-r">[(EGF-EGFR*)2]+[GAP] ↔ [(EGF-EGFR*)2-GAP]</td><td id="13-s">Ras inactivation</td></tr>
<tr><td id="13-t">9</td><td id="13-u">[(EGF-EGFR*)2-GAP] → [(EGF-EGFR*)2-GAP]</td><td id="13-v">Ras inactivation</td></tr>
<tr><td id="13-w">10</td><td id="13-x">[EGFR]+[EGF] ↔ [EGF-EGFR]</td><td id="13-y">receptor activation</td></tr>
<tr><td id="13-z">11</td><td id="13-A">[EGF-EGFR]+[EGF-EGFR] ↔ [(EGF-EGFR)2]</td><td id="13-B">receptor activation</td></tr>
<tr><td id="13-C">12</td><td id="13-D">[(EGF-EGFR)2] ↔ [(EGF-EGFR*)2]</td><td id="13-E">receptor activation</td></tr>
<tr><td id="13-F">13</td><td id="13-G">→ [EGFR]</td><td id="13-H">receptor activation</td></tr>
<tr><td id="13-I">14</td><td id="13-J">[(EGF-EGFR*)2] + [GAP] ↔ [(EGF-EGFR*)2-GAP]</td><td id="13-K">Ras inactivation</td></tr>
<tr><td id="13-L">15</td><td id="13-M">[Prot] → [Prot]</td><td id="13-N">internalization</td></tr>
<tr><td id="13-O">16</td><td id="13-P">[(EGF-EGFR*)2-GAP]+[Grb2] ↔ [(EGF-EGFR*)2-GAP-Grb2]</td><td id="13-Q">recruitment</td></tr>
<tr><td id="13-R">17</td><td id="13-S">[(EGF-EGFR*)2-GAP-Grb2]+[Sos] ↔ [(EGF-EGFR*)2-GAP-Grb2-Sos]</td><td id="13-T">recruitment</td></tr>
<tr><td id="13-U">18</td><td id="13-V">[(EGF-EGFR*)2-GAP-Grb2-Sos]+[Ras-GDP] ↔ [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP]</td><td id="13-W">Ras activation</td></tr>
<tr><td id="13-X">19</td><td id="13-Y">[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP] ↔ [(EGF-EGFR*)2-GAP-Grb2-Sos]+[Ras-GTP]</td><td id="13-Z">Ras activation</td></tr>
<tr><td id="13-10">20</td><td id="13-11">[Ras-GTP]+[(EGF-EGFR*)2-GAP-Grb2-Sos] ↔ [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP]</td><td id="13-12">Ras inactivation</td></tr>
<tr><td id="13-13">21</td><td id="13-14">[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP] ↔ [(EGF-EGFR*)2-GAP-Grb2-Sos]+[Ras-GDP]</td><td id="13-15">Ras inactivation</td></tr>
<tr><td id="13-16">22</td><td id="13-17">[(EGF-EGFR*)2-GAP]+[Shc] ↔ [(EGF-EGFR*)2-GAP-Shc]</td><td id="13-18">recruitment</td></tr>
<tr><td id="13-19">23</td><td id="13-1a">[(EGF-EGFR*)2-GAP-Shc] ↔ [(EGF-EGFR*)2-GAP-Shc*]</td><td id="13-1b">recruitment</td></tr>
<tr><td id="13-1c">24</td><td id="13-1d">[(EGF-EGFR*)2-GAP-Shc*]+[Grb2] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2]</td><td id="13-1e">recruitment</td></tr>
<tr><td id="13-1f">25</td><td id="13-1g">[(EGF-EGFR*)2-GAP-Shc*-Grb2]+[Sos] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]</td><td id="13-1h">recruitment</td></tr>
<tr><td id="13-1i">26</td><td id="13-1j">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]</td><td id="13-1k">Ras activation</td></tr>
<tr><td id="13-1l">27</td><td id="13-1m">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] + [Ras-GTP]</td><td id="13-1n">Ras activation</td></tr>
<tr><td id="13-1o">28</td><td id="13-1p">[Raf]+[Ras-GTP] ↔ [Raf-Ras-GTP]</td><td id="13-1q">Ras activates Raf</td></tr>
<tr><td id="13-1r">29</td><td id="13-1s">[Raf-Ras-GTP] ↔ [Raf*]+[Ras-GTP*]</td><td id="13-1t">Ras activates Raf</td></tr>
<tr><td id="13-1u">30</td><td id="13-1v">[Ras-GTP*]+[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]</td><td id="13-1w">Ras inactivation</td></tr>
<tr><td id="13-1x">31</td><td id="13-1y">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP]</td><td id="13-1z">Ras inactivation</td></tr>
<tr><td id="13-1A">32</td><td id="13-1B">[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] ↔ [(EGF-EGFR*)2-GAP]+[Shc*-Grb2-Sos]</td><td id="13-1C">recruitment</td></tr>
<tr><td id="13-1D">33</td><td id="13-1E">[Shc*-Grb2-Sos] ↔ [Grb2-Sos]+[Shc*]</td><td id="13-1F">recruitment</td></tr>
<tr><td id="13-1G">34</td><td id="13-1H">[(EGF-EGFR*)2-GAP-Grb2-Sos] ↔ [(EGF-EGFR*)2-GAP]+[Grb2-Sos]</td><td id="13-1I">recruitment</td></tr>
</table>

<a id='156927e3-a4e6-4760-914c-e73cc823a94d'></a>

Supplementary table 4: control by biochemical processes

<!-- PAGE BREAK -->

<a id='fcac4455-433e-40c1-9e55-7406e9de43ee'></a>

35. [Grb2-Sos] ↔ [Grb2] +[Sos]
36. [Shc*] ↔ [Shc]
37. [(EGF-EGFR*)2-GAP-Shc*] ↔ [(EGF-EGFR*)2-GAP]+[Shc*]
38. [Shc*]+[Grb2] ↔ [Shc*-Grb2]
39. [(EGF-EGFR*)2-GAP-Shc*-Grb2] ↔ [(EGF-EGFR*)2-GAP]+[Shc*-Grb2]
40. [Shc*-Grb2]+[Sos] ↔ [Shc*-Grb2-Sos]
41. [(EGF-EGFR*)2-GAP-Shc*] + [Grb2-Sos] ↔ [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]
42. [Raf*]+[Phosphatase1] ↔ [Raf*-Phosphatase1]
43. [Raf*-Phosphatase1] ↔ [Raf]+[Phosphatase1]
44. [MEK] + [Raf*] ↔ [MEK-Raf*]
45. [MEK-Raf*] ↔ [MEK-P] +[Raf*]
46. [MEK-P]+[Raf*] ↔ [MEK-P-Raf*]
47. [MEK-P-Raf*] ↔ [MEK-PP] + [Raf*]
48. [MEK-PP]+[Phosphatase2] ↔ [MEK-PP-Phosphatase2]
49. [MEK-PP-Phosphatase2] ↔ [MEK-P] + [Phosphatase2]
50. [MEK-P]+[Phosphatase2] ↔ [MEK-P-Phosphatase2]
51. [MEK-P-Phosphatase2] ↔ [MEK]+[Phosphatase2]
52. [ERK]+[MEK-PP] ↔ [ERK-MEK-PP]
53. [ERK-MEK-PP] ↔ [ERK-P]+[MEK-PP]
54. [ERK-P]+[MEK-PP] ↔ [ERK-P-MEK-PP]
55. [ERK-P-MEK-PP] ↔ [ERK-PP]+[MEK-PP]
56. [ERK-PP]+[Phosphatase3] ↔ [ERK-PP-Phosphatase3]
57. [ERK-PP-Phosphatase3] ↔ [ERK-P]+[Phosphatase3]
58. [ERK-P] + [Phosphatase3] ↔ [ERK-P-Phosphatase3]
59. [ERK-P-Phosphatase3] ↔ [ERK]+[Phosphatase3]
60. [EGFRI] ↔ [EGFRideg]
61. [EGFi] ↔ [EGFideg]
62. [(EGF-EGFRi*)2] ↔ [(EGF-EGFRi*)2deg]
63. [(EGF-EGFRi*)2-GAP]+[Grb2] ↔ [(EGF-EGFRi*)2-GAP-Grb2]
64. [(EGF-EGFRi*)2-GAP-Grb2]+[Sos] ↔ [(EGF-EGFRi*)2-GAP-Grb2-Sos]
65. [(EGF-EGFRi*)2-GAP-Grb2-Sos]+[Ras-GDP] ↔ [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP]
66. [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP] ↔ [(EGF-EGFRi*)2-GAP-Grb2-Sos]+[Ras-GTPi]
67. [Ras-GTPi*]+[(EGF-EGFRi*)2-GAP-Grb2-Sos] ↔ [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTPi]
68. [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP] ↔ [(EGF-EGFRi*)2-GAP-Grb2-Sos]+[Ras-GDP]
69. [(EGF-EGFRi*)2-GAP]+[Shc] ↔ [(EGF-EGFRi*)2-GAP-Shc]
70. [(EGF-EGFR*)2-GAP-Shc] ↔ [(EGF-EGFR*)2-GAP-Shc*]
71. [(EGF-EGFRi*)2-GAP-Shc*]+[Grb2] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2]

<a id='08b27033-67a2-4817-8af8-c64e1350c54a'></a>

recruitment
recruitment
recruitment
recruitment
recruitment
recruitment
recruitment
Raf dephosphorylation
Raf dephosphorylation
Raf phosphorylates MEK
Raf phosphorylates MEK
Raf phosphorylates MEK
Raf phosphorylates MEK
MEK dephosphorylation
MEK dephosphorylation
MEK dephosphorylation
MEK dephosphorylation
ERK phosphorylation
ERK phosphorylation
ERK phosphorylation
ERK phosphorylation
ERK dephosphorylation
ERK dephosphorylation
ERK dephosphorylation
ERK dephosphorylation
degradation
degradation
degradation
recruitment
recruitment
Ras activation
Ras activation
Ras inactivation
Ras inactivation
recruitment
recruitment
recruitment

<!-- PAGE BREAK -->

<a id='7a5b8fb3-2ac6-4f3e-b3d4-43d68e3a015c'></a>

72 [(EGF-EGFRi*)2-GAP-Shc*-Grb2]+[Sos] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]
73 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]
74 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] + [Ras-GTPi]
75 [Raf]+[Ras-GTPi] → [Raf-Ras-GTPi]
76 [Raf-Ras-GTPi] → [Rafi*]+[Ras-GTPi*]
77 [Ras-GTPi*]+[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]
78 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos]+[Ras-GDP]
79 [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] ↔ [(EGF-EGFRi*)2-GAP]+[Shc-Grb2-Sos]
80 [(EGF-EGFRi*)2-GAP-Grb2-Sos] → [(EGF-EGFRi*)2-GAP]+[Grb2-Sos]
81 [(EGF-EGFRi*)2-GAP-Shc*] → [(EGF-EGFRi*)2-GAP]+[Shc*]
82 [(EGF-EGFRi*)2-GAP-Shc*-Grb2] → [(EGF-EGFRi*)2-GAP]+[Shc*-Grb2]
83 [(EGF-EGFRi*)2-GAP-Shc*] + [Grb2-Sos] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]
84 [Rafi*]+[Phosphatase1] → [Rafi*-Phosphatase1]
85 [Rafi*-Phosphatase 1] → [Raf]+[Phosphatase1]
86 [MEK] + [Rafi*] → [MEK-Rafi*]
87 [MEK-Rafi*] → [MEKi-P] +[Rafi*]
88 [MEKI-P]+[Rafi*] → [MEK-P-Rafi*]
89 [MEK-P-Rafi*] → [MEKI-PP] + [Rafi*]
90 [MEKI-PP]+[Phosphatase2] → [MEKI-PP-Phosphatase2]
91 [MEKI-PP-Phosphatase2] → [MEKi-P] + [Phosphatase2]
92 [MEKI-P]+[Phosphatase2] → [MEKi-P-Phosphatase2]
93 [MEKI-P-Phosphatase2] → [MEK]+[Phosphatase2]
94 [ERK]+[MEKI-PP] → [ERK-MEKI-PP]
95 [ERK-MEKI-PP] → [ERKI-P]+[MEKI-PP]
96 [ERKI-P]+[MEKI-PP] → [ERKI-P-MEKI-PP]
97 [ERKI-P-MEKI-PP] → [ERKI-PP]+[MEKI-PP]
98 [ERKI-PP]+[Phosphatase3] → [ERKI-PP-Phosphatase3]
99 [ERKI-PP-Phosphatase3] → [ERKi-P]+[Phosphatase3]
100 [ERKI-P] + [Phosphatase3] → [ERKI-P-Phosphatase3]
101 [ERKI-P-Phosphatase3] → [ERK]+[Phosphatase3]
102 [(EGF-EGFR*)2-GAP] → [(EGF-EGFRi*)2-GAP]
103 [(EGF-EGFR*)2-GAP-Shc] → [(EGF-EGFRi*)2-GAP-Shc]
104 [(EGF-EGFR*)2-GAP-Shc*] → [(EGF-EGFRi*)2-GAP-Shc*]
105 [(EGF-EGFR*)2-GAP-Grb2-Sos] → [(EGF-EGFRI*)2-GAP-Grb2-Sos]
106 [(EGF-EGFR*)2-GAP-Grb2-Sos]+[Prot] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Prot]
107 [(EGF-EGFR*)2-GAP-Grb2-Sos-Prot] → [ (EGF-EGFRi*)2-GAP-Grb2-Sos]+[Proti]
108 [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP] → [(EGF-EGFRI*)2-GAP-Grb2-Sos-Ras-GDP]

<a id='0b4764a4-7531-4a3f-b9c6-e212bda0af04'></a>

recruitment
Ras activation
Ras activation
Ras activates Raf
Ras activates Raf
Ras inactivation
Ras inactivation
recruitment
recruitment
recruitment
recruitment
recruitment
Raf dephosphorylation
Raf dephosphorylation
Raf phosphorylates MEK
Raf phosphorylates MEK
Raf phosphorylates MEK
Raf phosphorylates MEK
MEK dephosphorylation
MEK dephosphorylation
MEK dephosphorylation
MEK dephosphorylation
ERK phosphorylation
ERK phosphorylation
ERK phosphorylation
ERK phosphorylation
ERK dephosphorylation
ERK dephosphorylation
ERK dephosphorylation
ERK dephosphorylation
internalization
internalization
internalization
internalization
internalization
internalization
internalization

<!-- PAGE BREAK -->

<a id='c9a165e6-512e-4e82-9c61-7ae8ee7f9bc7'></a>

<table><thead><tr><th>Col 1</th><th>Reaction/Interaction</th><th>Category</th></tr></thead><tbody><tr><td>109</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP]+[Prot] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP-Prot]</td><td>internalization</td></tr><tr><td>110</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GDP-Prot] → [ (EGF-EGFRI*)2-GAP-Grb2-Sos-Ras-GDP]+[Proti]</td><td>internalization</td></tr><tr><td>111</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP]</td><td>internalization</td></tr><tr><td>112</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP]+[Prot] → [(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP-Prot]</td><td>internalization</td></tr><tr><td>113</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-Ras-GTP-Prot] → [(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP]+[Proti]</td><td>internalization</td></tr><tr><td>114</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2]</td><td>internalization</td></tr><tr><td>115</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Prot]</td><td>internalization</td></tr><tr><td>116</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Prot] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2]+[Proti]</td><td>internalization</td></tr><tr><td>117</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos]</td><td>internalization</td></tr><tr><td>118</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Prot]</td><td>internalization</td></tr><tr><td>119</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Prot] → [ (EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]+[Proti]</td><td>internalization</td></tr><tr><td>120</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]</td><td>internalization</td></tr><tr><td>121</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP-Prot]</td><td>internalization</td></tr><tr><td>122</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GDP-Prot] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP]+[Proti]</td><td>internalization</td></tr><tr><td>123</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]</td><td>internalization</td></tr><tr><td>124</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]+[Prot] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP-Prot]</td><td>internalization</td></tr><tr><td>125</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-Ras-GTP-Prot] → [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP]+[Proti]</td><td>internalization</td></tr><tr><td>126</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos]+[ERK-PP] → [(EGF-EGFR*)2-GAP-Grb2-Sos-ERK-PP]</td><td>negative feedback loop</td></tr><tr><td>127</td><td>[(EGF-EGFRi*)2-GAP-Grb2-Sos]+[ERKI-PP] → [(EGF-EGFRI*)2-GAP-Grb2-Sos-ERKI-PP]</td><td>negative feedback loop</td></tr><tr><td>128</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]+[ERK-PP] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-ERK-PP]</td><td>negative feedback loop</td></tr><tr><td>129</td><td>[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]+[ERKI-PP] → [(EGF-EGFRI*)2-GAP-Shc*-Grb2-Sos-ERKI-PP]</td><td>negative feedback loop</td></tr><tr><td>130</td><td>[Sos]+[ERK-PP] → [Sos-ERK-PP]</td><td>negative feedback loop</td></tr><tr><td>131</td><td>[Sos]+[ERKI-PP] → [Sos-ERKI-PP]</td><td>negative feedback loop</td></tr><tr><td>132</td><td>[(EGF-EGFRi*)2-GAP] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>133</td><td>[(EGF-EGFRi*)2-GAP-Grb2] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>134</td><td>[(EGF-EGFRi*)2-GAP-Grb2-Sos]→ [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>135</td><td>[(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GDP] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>136</td><td>[(EGF-EGFRi*)2-GAP-Grb2-Sos-Ras-GTP] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>137</td><td>[(EGF-EGFRi*)2-GAP-Shc] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>138</td><td>[(EGF-EGFRi*)2-GAP-Shc*] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>139</td><td>[(EGF-EGFRi*)2-GAP-Shc*-Grb2] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>140</td><td>[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>141</td><td>[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GDP] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>142</td><td>[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-Ras-GTP] → [(EGF-EGFRi*)2deg]</td><td>degradation</td></tr><tr><td>143</td><td>[(EGF-EGFR*)2-GAP-Grb2-Sos-ERK-PP] → [(EGF-EGFR*)2-GAP-Grb2-Sos]deg+[ERK-PP]</td><td>negative feedback loop</td></tr><tr><td>144</td><td>[(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos-ERK-PP] → [(EGF-EGFR*)2-GAP-Shc*-Grb2-Sos]deg+[ERK-PP]</td><td>negative feedback loop</td></tr><tr><td>145</td><td>[Sos-ERK-PP] → [Sosi]+[ERK-PP]</td><td>negative feedback loop</td></tr></tbody></table>

<!-- PAGE BREAK -->

<a id='f1fa620b-7789-45c6-8d1c-092483a15b18'></a>

<table><thead><tr><th>Col 1</th><th>Col 2</th><th>Col 3</th></tr></thead><tbody><tr><td>146</td><td>[(EGF-EGFRi*)2-GAP-Grb2-Sos-ERKI-PP] ↔ [(EGF-EGFRi*)2-GAP-Grb2-Sos]deg+[ERKi-PP]</td><td>negative feedback loop</td></tr><tr><td>147</td><td>[(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos-ERKI-PP] ↔ [(EGF-EGFRi*)2-GAP-Shc*-Grb2-Sos]deg+[ERKi-PP]</td><td>negative feedback loop</td></tr><tr><td>148</td><td>[Sos-ERK-PPi] ↔ [Sosi]+[ERK-PPi]</td><td>negative feedback loop</td></tr></tbody></table>

<!-- PAGE BREAK -->

<a id='33ea791b-de8d-41ec-8d27-8e56785dd6e2'></a>

<table id="18-1">
<tr><td id="18-2" rowspan="2">biological process</td><td id="18-3" colspan="3">small perturbations (δp/p= 10^-6)</td><td id="18-4" colspan="3">large perturbations (δp/p= - 0.5)</td><td id="18-5" colspan="3">large perturbations (δp/p= 0.5)</td></tr>
<tr><td id="18-6">A</td><td id="18-7">d</td><td id="18-8">l</td><td id="18-9">A</td><td id="18-a">d</td><td id="18-b">I</td><td id="18-c">A</td><td id="18-d">d</td><td id="18-e">I</td></tr>
<tr><td id="18-f">receptor activation</td><td id="18-g">0.0002</td><td id="18-h">0.0257</td><td id="18-i">0.0264</td><td id="18-j">0.0003</td><td id="18-k">0.0289</td><td id="18-l">0.0292</td><td id="18-m">0.0001</td><td id="18-n">0.0233</td><td id="18-o">0.0245</td></tr>
<tr><td id="18-p">recruitment</td><td id="18-q">-0.0010</td><td id="18-r">0.0322</td><td id="18-s">0.0626</td><td id="18-t">0.0016</td><td id="18-u">0.1265</td><td id="18-v">0.1790</td><td id="18-w">-0.0021</td><td id="18-x">-0.0055</td><td id="18-y">0.0122</td></tr>
<tr><td id="18-z">Ras activation</td><td id="18-A">0.0236</td><td id="18-B">0.1197</td><td id="18-C">0.2127</td><td id="18-D">0.0850</td><td id="18-E">0.2358</td><td id="18-F">0.4065</td><td id="18-G">0.0120</td><td id="18-H">0.0792</td><td id="18-I">0.1403</td></tr>
<tr><td id="18-J">Ras inactivation</td><td id="18-K">0.0026</td><td id="18-L">0.2846</td><td id="18-M">0.4267</td><td id="18-N">0.0073</td><td id="18-O">0.3595</td><td id="18-P">0.5294</td><td id="18-Q">0.0012</td><td id="18-R">0.2488</td><td id="18-S">0.3778</td></tr>
<tr><td id="18-T">Ras activates Raf</td><td id="18-U">0.0004</td><td id="18-V">0.0051</td><td id="18-W">0.0075</td><td id="18-X">0.0022</td><td id="18-Y">0.0100</td><td id="18-Z">0.0155</td><td id="18-10">0.0000</td><td id="18-11">0.0034</td><td id="18-12">0.0047</td></tr>
<tr><td id="18-13">Raf dephosphorylation</td><td id="18-14">-0.0877</td><td id="18-15">-0.9487</td><td id="18-16">-1.4714</td><td id="18-17">-0.0491</td><td id="18-18">-1.7354</td><td id="18-19">-2.6498</td><td id="18-1a">-0.6217</td><td id="18-1b">-0.6079</td><td id="18-1c">-1.1578</td></tr>
<tr><td id="18-1d">Raf phosphorylates MEK</td><td id="18-1e">0.0894</td><td id="18-1f">0.9486</td><td id="18-1g">1.4726</td><td id="18-1h">1.5186</td><td id="18-1i">0.9727</td><td id="18-1j">2.1294</td><td id="18-1k">0.0411</td><td id="18-1l">0.8454</td><td id="18-1m">1.2942</td></tr>
<tr><td id="18-1n">MEK dephosphorylation</td><td id="18-1o">-0.0080</td><td id="18-1p">-1.0257</td><td id="18-1q">-1.1240</td><td id="18-1r">-0.0085</td><td id="18-1s">-1.5643</td><td id="18-1t">-1.6993</td><td id="18-1u">-0.0077</td><td id="18-1v">-0.7765</td><td id="18-1w">-0.8511</td></tr>
<tr><td id="18-1x">ERK phosphorylation</td><td id="18-1y">0.0809</td><td id="18-1z">0.1721</td><td id="18-1A">0.4389</td><td id="18-1B">0.7294</td><td id="18-1C">0.2552</td><td id="18-1D">1.1425</td><td id="18-1E">0.0478</td><td id="18-1F">0.1141</td><td id="18-1G">0.3115</td></tr>
<tr><td id="18-1H">ERK dephosphorylation</td><td id="18-1I">-0.0803</td><td id="18-1J">-0.1718</td><td id="18-1K">-0.4353</td><td id="18-1L">-0.0614</td><td id="18-1M">-0.1555</td><td id="18-1N">-0.5006</td><td id="18-1O">-0.1642</td><td id="18-1P">-0.1507</td><td id="18-1Q">-0.4173</td></tr>
<tr><td id="18-1R">negative feedback loop</td><td id="18-1S">0.0000</td><td id="18-1T">-0.0029</td><td id="18-1U">-0.0039</td><td id="18-1V">0.0000</td><td id="18-1W">-0.0029</td><td id="18-1X">-0.0039</td><td id="18-1Y">0.0000</td><td id="18-1Z">-0.0029</td><td id="18-20">-0.0039</td></tr>
<tr><td id="18-21">internalization</td><td id="18-22">-0.0209</td><td id="18-23">-0.2677</td><td id="18-24">-0.4279</td><td id="18-25">-0.0210</td><td id="18-26">-0.3469</td><td id="18-27">-0.5411</td><td id="18-28">-0.0210</td><td id="18-29">-0.2219</td><td id="18-2a">-0.3602</td></tr>
<tr><td id="18-2b">degradation</td><td id="18-2c">0.0008</td><td id="18-2d">-0.1713</td><td id="18-2e">-0.1846</td><td id="18-2f">0.0008</td><td id="18-2g">-0.1713</td><td id="18-2h">-0.1892</td><td id="18-2i">0.0008</td><td id="18-2j">-0.1654</td><td id="18-2k">-0.1766</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='a50173a7-abf6-47a4-ac02-7ccc389fde0d'></a>

Supplementary table 5: response coefficients
<table id="19-1">
<tr><td id="19-2" rowspan="2">protein</td><td id="19-3" colspan="3">small perturbations (δp/p= 10^-6)</td><td id="19-4" colspan="3">large perturbations (δp/p= - 0.5)</td><td id="19-5" colspan="3">large perturbations (δp/p= 0.5)</td></tr>
<tr><td id="19-6">A</td><td id="19-7">d</td><td id="19-8">l</td><td id="19-9">A</td><td id="19-a">d</td><td id="19-b">I</td><td id="19-c">A</td><td id="19-d">d</td><td id="19-e">I</td></tr>
<tr><td id="19-f">EGF</td><td id="19-g">0.00E+00</td><td id="19-h">2.00E-04</td><td id="19-i">1.00E-04</td><td id="19-j">0.00E+00</td><td id="19-k">0.00E+00</td><td id="19-l">1.00E-04</td><td id="19-m">0.00E+00</td><td id="19-n">2.00E-04</td><td id="19-o">3.00E-04</td></tr>
<tr><td id="19-p">EGFR</td><td id="19-q">8.00E-03</td><td id="19-r">1.71E-01</td><td id="19-s">2.75E-01</td><td id="19-t">4.80E-03</td><td id="19-u">1.15E-01</td><td id="19-v">1.99E-01</td><td id="19-w">2.18E-02</td><td id="19-x">2.65E-01</td><td id="19-y">4.02E-01</td></tr>
<tr><td id="19-z">Prot</td><td id="19-A">-1.67E-02</td><td id="19-B">-3.22E-01</td><td id="19-C">-4.90E-01</td><td id="19-D">-2.20E-02</td><td id="19-E">-2.47E-01</td><td id="19-F">-3.70E-01</td><td id="19-G">-1.29E-02</td><td id="19-H">-5.12E-01</td><td id="19-I">-7.78E-01</td></tr>
<tr><td id="19-J">shc</td><td id="19-K">1.30E-03</td><td id="19-L">-1.26E-02</td><td id="19-M">-2.90E-03</td><td id="19-N">8.00E-04</td><td id="19-O">-3.29E-02</td><td id="19-P">-2.71E-02</td><td id="19-Q">2.50E-03</td><td id="19-R">1.92E-02</td><td id="19-S">3.32E-02</td></tr>
<tr><td id="19-T">Grb2</td><td id="19-U">7.00E-04</td><td id="19-V">-8.60E-03</td><td id="19-W">-8.40E-03</td><td id="19-X">5.00E-04</td><td id="19-Y">-9.40E-03</td><td id="19-Z">-1.04E-02</td><td id="19-10">8.00E-04</td><td id="19-11">-7.60E-03</td><td id="19-12">-6.10E-03</td></tr>
<tr><td id="19-13">Sos</td><td id="19-14">-3.00E-04</td><td id="19-15">9.40E-03</td><td id="19-16">1.70E-02</td><td id="19-17">-5.00E-04</td><td id="19-18">6.10E-03</td><td id="19-19">1.11E-02</td><td id="19-1a">3.00E-04</td><td id="19-1b">1.59E-02</td><td id="19-1c">2.83E-02</td></tr>
<tr><td id="19-1d">RasGDP</td><td id="19-1e">8.26E-02</td><td id="19-1f">8.40E-01</td><td id="19-1g">1.30E+00</td><td id="19-1h">2.59E-02</td><td id="19-1i">7.28E-01</td><td id="19-1j">1.12E+00</td><td id="19-1k">1.95E+00</td><td id="19-1l">1.07E+00</td><td id="19-1m">1.97E+00</td></tr>
<tr><td id="19-1n">GAP</td><td id="19-1o">1.62E-02</td><td id="19-1p">2.05E-01</td><td id="19-1q">3.24E-01</td><td id="19-1r">8.90E-03</td><td id="19-1s">9.74E-02</td><td id="19-1t">1.81E-01</td><td id="19-1u">5.88E-02</td><td id="19-1v">3.98E-01</td><td id="19-1w">5.60E-01</td></tr>
<tr><td id="19-1x">grb2sos</td><td id="19-1y">2.00E-03</td><td id="19-1z">-1.70E-02</td><td id="19-1A">-4.60E-03</td><td id="19-1B">1.00E-03</td><td id="19-1C">-2.23E-02</td><td id="19-1D">-1.92E-02</td><td id="19-1E">6.20E-03</td><td id="19-1F">5.60E-03</td><td id="19-1G">3.83E-02</td></tr>
<tr><td id="19-1H">Raf</td><td id="19-1I">4.00E-04</td><td id="19-1J">8.80E-03</td><td id="19-1K">1.33E-02</td><td id="19-1L">-1.00E-04</td><td id="19-1M">5.10E-03</td><td id="19-1N">7.40E-03</td><td id="19-1O">3.60E-03</td><td id="19-1P">2.40E-02</td><td id="19-1Q">3.29E-02</td></tr>
<tr><td id="19-1R">phosphatase 1</td><td id="19-1S">-8.78E-02</td><td id="19-1T">-9.49E-01</td><td id="19-1U">-1.47E+00</td><td id="19-1V">-1.25E+00</td><td id="19-1W">-5.58E-01</td><td id="19-1X">-1.40E+00</td><td id="19-1Y">-3.04E-02</td><td id="19-1Z">-1.64E+00</td><td id="19-20">-2.57E+00</td></tr>
<tr><td id="19-21">MEK</td><td id="19-22">4.96E-02</td><td id="19-23">9.03E-01</td><td id="19-24">1.24E+00</td><td id="19-25">2.09E-02</td><td id="19-26">8.75E-01</td><td id="19-27">1.18E+00</td><td id="19-28">1.14E+00</td><td id="19-29">8.47E-01</td><td id="19-2a">1.49E+00</td></tr>
<tr><td id="19-2b">phosphatase 2</td><td id="19-2c">-9.60E-03</td><td id="19-2d">-1.03E+00</td><td id="19-2e">-1.12E+00</td><td id="19-2f">-1.03E-02</td><td id="19-2g">-7.03E-01</td><td id="19-2h">-7.56E-01</td><td id="19-2i">-9.00E-03</td><td id="19-2j">-1.94E+00</td><td id="19-2k">-2.08E+00</td></tr>
<tr><td id="19-2l">ERK</td><td id="19-2m">1.91E+00</td><td id="19-2n">7.02E-01</td><td id="19-2o">2.74E+00</td><td id="19-2p">1.91E+00</td><td id="19-2q">5.31E-01</td><td id="19-2r">3.15E+00</td><td id="19-2s">1.85E+00</td><td id="19-2t">1.18E+00</td><td id="19-2u">1.94E+00</td></tr>
<tr><td id="19-2v">phosphatase 3</td><td id="19-2w">-9.43E-01</td><td id="19-2x">-4.86E-01</td><td id="19-2y">-1.67E+00</td><td id="19-2z">-1.02E+00</td><td id="19-2A">-5.28E-01</td><td id="19-2B">-1.35E+00</td><td id="19-2C">-9.27E-01</td><td id="19-2D">-4.65E-01</td><td id="19-2E">-2.10E+00</td></tr>
</table>
<a id='f5c4e34e-6c62-4eb6-86a3-3a6c387b5b65'></a>

npj | Systems Biology
and Applications

<a id='dbb9c163-cc33-4c3b-a2c8-3359fb847d51'></a>

www.nature.com/npjsba

<a id='87ab9d63-24e7-47ea-a4b1-8dc686f6df33'></a>

ARTICLE OPEN
A Clb/Cdk1-mediated regulation of Fkh2 synchronizes CLB
expression in the budding yeast cell cycle

<a id='5bef57ce-28cd-41f9-be88-0b5877e58f69'></a>

Christian Linke ¹², Anastasia Chasapi³, Alberto González-Novo⁴, Istabrak Al Sawad¹, Silvia Tognetti⁴, Edda Klipp⁵, Mart Loog⁶,
Sylvia Krobitsch², Francesc Posas⁴, Ioannis Xenarios³ and Matteo Barberis¹²

<a id='2f3ca187-fd87-438f-8274-5b4f57cc0b07'></a>

Precise timing of cell division is achieved by coupling waves of cyclin-dependent kinase (Cdk) activity with a transcriptional oscillator throughout cell cycle progression. Although details of transcription of cyclin genes are known, it is unclear which is the transcriptional cascade that modulates their expression in a timely fashion. Here, we demonstrate that a Clb/Cdk1-mediated regulation of the Fkh2 transcription factor synchronizes the temporal mitotic CLB expression in budding yeast. A simplified kinetic model of the cyclin/Cdk network predicts a linear cascade where a Clb/Cdk1-mediated regulation of an activator molecule drives CLB3 and CLB2 expression. Experimental validation highlights Fkh2 as modulator of CLB3 transcript levels, besides its role in regulating CLB2 expression. A Boolean model based on the minimal number of interactions needed to capture the information flow of the Clb/Cdk1 network supports the role of an activator molecule in the sequential activation, and oscillatory behavior, of mitotic Clb cyclins. This work illustrates how transcription and phosphorylation networks can be coupled by a Clb/Cdk1-mediated regulation that synchronizes them.

npi Systems Biology and Applications (2017)3:7; doi:10.1038/s41540-017-0008-1

<a id='e6aa9b93-7bba-42d6-930f-c32f69100081'></a>

## INTRODUCTION

In budding yeast, coordination of cell cycle transitions is achieved by periodic changes in the activity of the kinase Cdk1, which is regulated by temporal waves of expression of phase-specific cyclins.<sup>1</sup>, <sup>2</sup> Four waves of cell cycle-dependent transcription of cyclins are recognized: a wave of G1 cyclins (Cln1-3) is essential for passing START at the G1/S transition, whereas three waves of B-type cyclins (Clb5,6, Clb3,4, and Clb1,2) control DNA replication dynamics and mitotic entry/exit through S-to-M phases.<sup>3</sup>, <sup>4</sup> Successive oscillations of cyclin/Cdk1 activities ensure unidirectionality and correct timing of cell cycle transcriptional regulation. Although the yeast cell cycle has been studied extensively, it is not yet fully understood how these kinase activities interconnect precisely with the various transcriptional mechanisms driving a timely cell cycle progression. Cdk1 is not the main regulator of transcriptional oscillations,<sup>5</sup> however, cyclin/Cdk1 activity contributes to the robustness of transcriptional oscillations by (i) modulating the activity of transcription factors, and (ii) acting as their effector to trigger the ordered program of cyclin expression.<sup>6</sup> Moreover, transcription network and Cdk1-driven phosphorylation events are coupled by feed-forward loops to convert periodic oscillations of Cdk activity in transcriptional response.<sup>7</sup> This ensures that the precise temporal sequence of cell cycle events is maintained.

<a id='1e2587a9-0c17-49b4-b9b1-157ef1224dd4'></a>

A precise knowledge of the axis cyclin/Cdk1-transcriptional
regulation throughout all cell cycle phases is still lacking. However,
transcriptional regulation of the _CLB2_ cluster that drives G2/M
gene expression has been widely investigated, and the forkhead

<a id='d990ebcb-b276-4caf-949b-abd581f4fb7e'></a>

(Fkh) transcription factors Fkh1 and Fkh2 were identified as essential in this process. 8, 9 Fkh1 and Fkh2 transcripts display a peak in S phase, and their periodic activity is dependent on cell cycle-regulated recruitment of the coactivator Ndd1 at the S/G2 transition. 8 Although Fkh1 and Fkh2 have overlapping functions, only Fkh2 can associate with Ndd1 to regulate CLB2 expression. 9 Fkh2 and Ndd1 are phosphorylated by Clb5/Cdk1, thus triggering recruitment of Ndd1 to Fkh2 to CLB2 promoter, and subsequently by Clb2/Cdk1 that further stabilizes the Fkh2-Ndd1 interaction by a positive feedback loop. 10 Fkh2 phosphorylation is not abolished in a clb5Δ strain, suggesting that other Clb/Cdk1 complexes may also play a role in Fkh2 activation. Remarkably, in the absence of Clb3, Clb4, and Clb5, the CLB2 promoter is not fully active with Clb2 being highly unstable. 11 Thus, multiple Clb/Cdk1 complexes could phosphorylate Fkh2 and/or Ndd1 to generate a basal level of CLB2 expression that would then rapidly increase due to the Clb2/Cdk1-mediated positive feedback loop.

<a id='f009e4b3-46fa-414c-806a-32b2e92588e2'></a>

Although many details of the transcription of cyclin genes are
known,⁶ there is still a lack of understanding of precise
transcriptional mechanisms regulating the relative timing of
waves of _CLB_ activation. In order to address this issue, we
employed a simplified mathematical model¹² of the cyclin/Cdk1
network to design new experiments addressing how timely waves
of _CLB_ expression may occur. Minimal models have been
developed, which are able to account for properties of wild type
cells.¹³ With a combined computational and experimental
approach we unravelled that a cyclin/Cdk1-dependent regulation
of the transcription factor Fkh2 is able to drive timely waves of

<a id='72892b81-08df-4a3c-aaa8-2692c65e5b0d'></a>

1Synthetic Systems Biology and Nuclear Organization, Swammerdam Institute for Life Sciences, University of Amsterdam, Amsterdam 1098 XH, The Netherlands; 2Max Planck Institute for Molecular Genetics, Berlin 14195, Germany; 3Vital-IT group, Swiss Institute of Bioinformatics, University of Lausanne, CH-1015 Lausanne, Switzerland; 4Cell Signaling Unit, Departament de Ciències Experimentals i de la Salut, Universitat Pompeu Fabra, Barcelona 08003, Spain; 5Institute for Biology, Theoretical Biophysics, Humboldt University Berlin, Berlin 10115, Germany and 6Institute of Technology, University of Tartu, Tartu 50411, Estonia
Correspondence: Matteo Barberis (M.Barberis@uva.nl)
Christian Linke and Matteo Barberis contributed equally to the practical realization of the work

<a id='468197f0-7e94-4a41-9c2a-06ea827bddb6'></a>

Received: 20 October 2016 Revised: 29 November 2016 Accepted: 13 December 2016
Published online: 06 March 2017

<a id='19fc229e-5fc1-43a7-801e-6021d80a28c0'></a>

Published in partnership with the Systems Biology Institute

<a id='2bb9a3df-4d42-494d-ac29-59599a14a67b'></a>

<::logo: npj nature partner journals
nature partner journals
The logo features the letters "npj" in red, followed by "nature partner journals" in grey, with "nature" in red.::>

<!-- PAGE BREAK -->

<a id='137fc2ef-d632-4df5-bfeb-cec9168a1f05'></a>

npj

<a id='18e12784-7a44-4309-91d5-2036c382293f'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al

<a id='45e5254c-71e2-4c9f-955d-69545e10e227'></a>

2

<a id='ef0a0bbb-a2b7-4f69-9441-60c16e906414'></a>

mitotic *CLB* expression. Furthermore, a Boolean model based on the minimal number of interactions needed to capture the information flow of the Clb/Cdk1 network supports the role of an activator molecule in the sequential activation, and oscillatory behavior, of mitotic Clb cyclins. Our data reveal that Clb waves are temporally synchronized by Fkh2-mediated regulation of mitotic *CLB* genes, and that a Clb/Cdk1-mediated regulation of Fkh2 modulates the *CLB* cascade.

<a id='c21c7789-8839-4daf-9dd6-c944ef1248c6'></a>

## RESULTS
A transcriptional regulation driving waves of mitotic CLB expression is predicted by kinetic modeling
To investigate whether a linear cascade of transcriptional activation is compatible with sequential waves of Clb cyclins, we employed a minimal kinetic model previously published by Barberis and colleagues,¹² for which the system property "Clb wave formation", is robust to parameter's choice. We systematically compared networks that differ in Clb/Cdk1-mediated regulations at mitotic CLB promoters (indicated in red color in Fig. 1a). Specifically, we investigated the role of: (i) Clb5,6/Cdk1 on CLB3,4 transcription (Fig. 1a, arrow A, kA), (ii) Clb3,4/Cdk1 on CLB1,2 transcription (Fig. 1a, arrow B, kB), and (iii) Clb5,6/Cdk1 on CLB1,2 transcription (Fig. 1a, arrow C, kc). Simulation of the minimal network showed alternate Clb waves in time, each wave deriving from the sum of all complexes in which each Clb is present (Fig. 1b; see Supplementary Text for details on model equations and kinetic parameters).¹² We analyzed three versions of this network, where reactions kA (Fig. 1c), kB (Fig. 1d) and kc (Fig. 1e) were neglected, respectively; conversely, the Clb1,2/Cdk1-mediated feedback loop on CLB1,2 (Fig. 1a, arrow D, kD) was always present. In Fig. 1c computed time courses of total levels of Clb5,6, Clb3,4 and Clb1,2 are shown when kA is removed. The simulation revealed no temporal coordination between the times of Clb appearance, with Clb3,4 peaking earlier than Clb5,6. Varying the value of kA resulted in a non correct order (Supplementary Fig. S1a) or to a steady state level (Supplementary Fig. S1b) of Clb waves, respectively. This would lead in vivo to a high Clb2 level and, thus, to cells arrested before cell division. When kB was removed from the network, no temporal coordination was observed between the peaks of Clb3,4 and Clb1,2 (Fig. 1d). Varying the value of kB resulted in Clb3,4 and Clb1,2 peaks appearing at the same time (Supplementary Fig. S1c) or to a steady state level of Clb1,2 (Supplementary Fig. S1d). Remarkably, when kc was removed from the network, oscillation of Clb cyclins was observed (Fig. 1e); this behavior was maintained after decreasing (Supplementary Fig. S1e) or increasing (Supplementary Fig. S1f) the value of kc. In addition, simulating the model with a wide range of parameter sets show that waves of Clb cyclins are brought about more consistently when the linear cascade is present, and that the value of kc is lower than those of kA and kB (data not shown). These results suggest that a linear cascade activating Clb cyclins may be required to generate staggered waves of Clb/Cdk1 kinase activities throughout cell cycle progression. The only regulation that has been shown to promote CLB2 transcription occurs via Clb5/Cdk1-mediated activation of the transcription factor Fkh2¹⁰ (Fig. 1a, regulation C). Our computational analysis shows that this regulation is per se not sufficient to temporally coordinate Clb waves in absence of either regulation A or B. Thus, two possible scenarios are predicted: (1) CLB2 transcription occurs only through a Clb5/Cdk1-mediated activation of Clb3, or (2) a moderate, but not high, regulation C may contribute to the occurrence of serial Clb waves.

<a id='161e7961-eecf-44af-a24a-17b640273a51'></a>

To investigate the transcriptional requirements for the forma-
tion of Clb cyclin waves, we tested the impact of a specific
parameter choice on the delay between their peaks by performing
a global sensitivity analysis (see Supplementary Materials and

<a id='8541a238-6db0-449d-b3e5-acf4df794c96'></a>

Methods for details).12 We compared the minimal network to the versions where only *k*C is active (left branch) or where only *k*A and *k*B are active (right branch). The pairwise comparison of different network structures showed that a change of parameter values affects strongly the distance between peaks of any Clb cyclin (Fig. 1 and Supplementary Fig. S1). If only the left branch is active, time delays tended to be smaller for the distance between Clb5,6–Clb3,4, and Clb3,4–Clb1,2 (Fig. 1f, g) and, consequently, between Clb5,6–Clb1,2 (Supplementary Fig. S1g). Remarkably, for the three peak distances, a positive effect on time delays was observed when only the right branch is active (Fig. 1h, i, Supplementary Fig. S1h), being the correlation indexes close to 1. Together, these analyses predict that regulation of time delays between Clb cyclins, thereby their oscillations, is essentially triggered by a linear cascade of CLB activation.

<a id='fe82a3d3-22f2-486e-8614-69d4b9c60ed3'></a>

Fkh2 is responsible for the timely onset of Clb3 protein
To investigate the linear cascade of regulation predicted by the kinetic modeling, we tested the role of the transcription factors Fkh1 and Fkh2 that are active in the temporal window where mitotic Clb cyclins are transcribed. 14, 15 Mitotic CLB mRNA levels were measured in fkh1Δ, fkh2Δ, or fkh1Δfkh2Δ strains by quantitative real-time PCR on cells arrested in G2/M phase with nocodazole (Fig. 2a) and in S phase with hydroxyurea (Supplementary Fig. S2b). These treatments revealed reduced CLB1 and CLB2 mRNA levels in fkh2Δ and fkh1Δfkh2Δ mutants and a less prominent effect of fkh1Δ as compared to wild type, as previously observed. 16 This pattern was observed also for CLB3, whereas CLB4 mRNA levels were affected in fkh2Δ and fkh1Δfkh2Δ mutants only in nocodazole treatment but were increased in fkh1Δ cells (Fig. 2a). Thus, Fkh2 may act as positive regulator of CLB3 and CLB4 transcription. Contrarily, Fkh1 may act as negative regulator of CLB4 transcription, providing further support to earlier experimental and computational analyses proposing that Fkh1 binds to the CLB4 promoter. 15, 17 We then investigated whether Fkh1 and Fkh2 bind to CLB promoters by chromatin immunoprecipitation (ChIP) (see Supplementary Materials and Methods). An enrichment of Fkh2 (Fig. 2b) and Fkh1 (Supplementary Fig. S2c) was observed at CLB1 and CLB2 promoters, as expected. Remarkably, a significative enrichment of Fkh1 and Fkh2 was detected at the CLB3 promoter, consistent with RNA Pol II occupancy data (Supplementary Fig. S2d), but not at the CLB4 promoter. We conclude that Fkh1 and Fkh2 regulate CLB3 transcription. Remarkably, a strong enrichment of Ndd1, coactivator of Fkh2, at the CLB3 promoter was also observed (Fig. 2c), consistent with the fact that Ndd1 is required for Fkh2 periodic activity, 8 and that the Fkh2/Ndd1 complex may regulate CLB3 transcription.

<a id='1995b3fe-b793-48be-b5f1-86c5cb2e858b'></a>

To determine the direct role of Fkh1 and Fkh2 in Clb3
regulation, we investigated its protein levels in fkh1A or fkh2A
strains in a time course experiment with G1-elutriated cells
(see Supplementary Materials and Methods for details). In the
same yeast strain, the levels of Sic1, Clb5, and Clb2 (the latter not
visualized) were used as reference. 12 In the fkh1A strain the
temporal window of maximal Clb3 expression is similar, but its
levels accumulate at a lower amount as compared to wild type
(Fig. 2d, e). The fkh2A strain instead accumulates Clb3 levels earlier
as compared to wild type, and the temporal window of maximal
Clb3 expression is delayed, with a protein amount strongly
reduced, as compared to wild type (Fig. 2d, e); the delay was also
confirmed by FACS analyses (Supplementary Fig. S2e). Notably,
Clb3 may be still produced in fkh2A cells, indicating that Fkh1 or
other, yet unknown transcription factors, may partially overlap
with Fkh2 to promote CLB3 transcription. Together, these data
confirm our model prediction, and demonstrate the role of Fkh2 in
the regulation of the temporal appearance of Clb3 protein levels.
Of note, we observe that a premature accumulation of Clb5
protein levels occurs upon Fkh2 deletion, already at early time

<a id='6785246a-c92a-4725-979d-52e7ac201c4e'></a>

npj Systems Biology and Applications (2017) 7

<a id='69164d02-9458-4627-83eb-abbf3b4d457e'></a>

Published in partnership with the Systems Biology Institute

<!-- PAGE BREAK -->

<a id='2894b913-75f4-465d-825a-7a73f9a8521c'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al
___

<a id='5e7565b9-e63b-4bea-a5ac-975a0da7f0e9'></a>

npj

<a id='a01d549d-28b8-46e6-80e1-32f379fd4380'></a>

3

<a id='8f46dce6-3972-4fc3-86ff-a6503ce35159'></a>

a <::Regulatory network diagram showing the interactions between Sic1, Cdk1/Clbs, and various Cdk1-Clb complexes. The diagram illustrates activation, inhibition, and degradation pathways with numbered steps. Key components are: Sic1, Cdk1/Clbs, Cdk1-Clb5,6, Cdk1-Clb5,6-Sic1, Clb5,6, Cdk1-Clb3,4, Cdk1-Clb3,4-Sic1, Clb3,4, Cdk1-Clb1,2, Cdk1-Clb1,2-Sic1, and Clb1,2. Red lines highlight specific interactions or pathways, with labels A, B, C, and D indicating points of intervention or specific regulatory steps.: diagram::> b <::Line graph showing the concentration of Clb5,6tot, Clb3,4tot, and Clb1,2tot over time (minutes). Parameters: A = 100, B = 1000, C = 100, D = 100. X-axis: Time (minutes), from 0 to 60. Y-axis: Concentration (a.u.), from 0 to 1.5. The Clb5,6tot curve peaks at approximately 1.3 a.u. around 25 minutes. The Clb3,4tot curve peaks at approximately 1.0 a.u. around 30 minutes. The Clb1,2tot curve shows a lower peak of about 0.3 a.u. around 35-40 minutes.: chart::> c <::Line graph showing the concentration of Clb5,6tot, Clb3,4tot, and Clb1,2tot over time (minutes). Parameters: B = 1000, C = 100, D = 100. X-axis: Time (minutes), from 0 to 60. Y-axis: Concentration (a.u.), from 0 to 1.5. The Clb5,6tot curve peaks at approximately 1.3 a.u. around 25 minutes. The Clb3,4tot curve peaks at approximately 0.3 a.u. around 30 minutes. The Clb1,2tot curve remains very low, barely rising above 0.1 a.u.: chart::> d <::Line graph showing the concentration of Clb5,6tot, Clb3,4tot, and Clb1,2tot over time (minutes). Parameters: A = 100, C = 100, D = 100. X-axis: Time (minutes), from 0 to 60. Y-axis: Concentration (a.u.), from 0 to 1.5. The Clb5,6tot curve peaks at approximately 1.5 a.u. around 20 minutes. The Clb3,4tot curve peaks at approximately 1.0 a.u. around 30 minutes. The Clb1,2tot curve shows a lower peak of about 0.3 a.u. around 35-40 minutes.: chart::> e <::Line graph showing the concentration of Clb5,6tot, Clb3,4tot, and Clb1,2tot over time (minutes). Parameters: A = 100, B = 1000, D = 100. X-axis: Time (minutes), from 0 to 60. Y-axis: Concentration (a.u.), from 0 to 1.5. The Clb5,6tot curve peaks at approximately 1.5 a.u. around 20 minutes. The Clb3,4tot curve peaks at approximately 1.0 a.u. around 30 minutes. The Clb1,2tot curve shows a lower peak of about 0.3 a.u. around 35-40 minutes.: chart::>

<a id='a50593fe-b9ff-45cc-a130-ba0cf3501814'></a>

<::Figure: The image contains two schematic diagrams and four scatter plots labeled f, g, h, and i. The schematic diagrams depict a regulatory network related to Sic1 and Cdk1-Clb complexes.

**Top Diagram (Left Branch):** This diagram shows a hierarchical structure starting with Sic1 at the top. Branches are numbered (e.g., 1, 2, 6, 15, 7, 8, 11, 9, 10, 26). Three main nodes are labeled: Cdk1-Clb5,6, Cdk1-Clb3,4, and Cdk1-Clb1,2. A specific pathway is highlighted in red, leading from Sic1 down to Cdk1-Clb1,2, then branching into 'C' and 'D'. The numbers 9 and 10 are associated with branch D.

**Bottom Diagram (Right Branch):** This diagram is structurally similar to the top one, also starting with Sic1 and featuring the same numbered branches and labeled nodes (Cdk1-Clb5,6, Cdk1-Clb3,4, Cdk1-Clb1,2). A different pathway is highlighted in red, originating from the branch connected to Cdk1-Clb5,6 and labeled 'A', then continuing through Cdk1-Clb3,4, labeled 'B', and finally leading to Cdk1-Clb1,2, which then branches into 'D'. The numbers 9 and 10 are associated with branch D.

**Scatter Plot f:**
- Title: f
- Conditions: C = 10 <= 100 <= 1000, D = 10 <= 100 <= 1000
- Correlation coefficient: r = 0.361
- Y-axis: t3.4 - t5.6 (min) [left branch]
- X-axis: t3.4 - t5.6 (min) [fully connected]
- Description: The plot shows a scatter of points, heavily concentrated near the origin (0,0) and spreading outwards, indicating a weak positive correlation.

**Scatter Plot g:**
- Title: g
- Conditions: C = 10 <= 100 <= 1000, D = 10 <= 100 <= 1000
- Correlation coefficient: r = 0.329
- Y-axis: t1.2 - t3.4 (min) [left branch]
- X-axis: t1.2 - t3.4 (min) [fully connected]
- Description: Similar to plot f, this scatter plot also shows points concentrated near the origin and spreading, suggesting a weak positive correlation.

**Scatter Plot h:**
- Title: h
- Conditions: A = 10 <= 100 <= 1000, B = 100 <= 1000 <= 10000, D = 10 <= 100 <= 1000
- Correlation coefficient: r = 0.995
- Y-axis: t3.4 - t5.6 (min) [right branch]
- X-axis: t3.4 - t5.6 (min) [fully connected]
- Description: This plot displays a strong positive linear correlation, with points tightly clustered along a diagonal line extending from the origin, indicating a very high correlation.

**Scatter Plot i:**
- Title: i
- Conditions: A = 10 <= 100 <= 1000, B = 100 <= 1000 <= 10000, D = 10 <= 100 <= 1000
- Correlation coefficient: r = 0.993
- Y-axis: t1.2 - t3.4 (min) [right branch]
- X-axis: t1.2 - t3.4 (min) [fully connected]
- Description: Similar to plot h, this plot also shows a strong positive linear correlation, with points tightly aligned along a diagonal line from the origin, indicating a very high correlation.
::>

<a id='debac09c-c82c-42c7-a4dd-929fff5caba8'></a>

Published in partnership with the Systems Biology Institute

<a id='5601cc0c-ce4f-4777-afc8-5dbe0ea452db'></a>

npj Systems Biology and Applications (2017) 7

<!-- PAGE BREAK -->

<a id='0d4108f4-60b8-4995-a636-f1a6928a64b8'></a>

<::npj
: figure::>

<a id='befee46e-d934-4e40-a556-c5a66b4641b6'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al

<a id='95ab2042-89b0-41a5-a6a6-36fb7f3aa611'></a>

4
Fig. 1 Kinetic model of Clb/Cdk1 regulation and computational time courses of total Clb cyclins levels. **a** Network highlighting in *red* the sequential transcriptional activation of Clb cylins, thereby Clb/Cdk1 activities (k_A, k_B, k_C, and k_D). **b** Simulations of the network in Fig. 1a are carried out with standard values of parameters, as reported in *Supplementary Text* for details. ¹² **c-e** Model variants were generated starting from the network in Fig. 1a by varying values of k_A (**c**), k_B (**d**), and k_C (**e**), as indicated on each simulation panel and described in the text. The model variants were implemented by ordinary differential equations, with the parameters used for the simulations having the same value among all variants (see *Supplementary Text* for model description and the full set of equations). ¹² **f-i** Prediction and validation of the transcriptional regulation responsible for the delay between waves of Clb cyclins. The graphs report the time delay observed between maximum levels (peaks) of Clb cyclins for binary combinations between the minimal model—where Clb/Cdk1 complexes are connected via four transcriptional regulations—and two model variants, independently. **f, g** Time delay calculated for the left branch (only k_C active) between Clb5,6 and Clb3,4 (t_3,4−t_5,6) (**f**) and Clb3,4 and Clb1,2 (t_1,2−t_3,4) (**g**). **h, i** Time delay calculated for the right branch (only k_A and k_B active) between Clb5,6 and Clb3,4 (t_3,4−t_5,6) (**h**) and Clb3,4 and Clb1,2 (t_1,2−t_3,4) (**i**). Each parameter of the network may vary from its selected value to the same value multiplied for a random real value comprised between 0.1 and 10, as indicated on each simulation panel

<a id='2a3093b0-d08a-4cde-8559-69b4809bd1af'></a>

aNOC treatment<::bar chart showing Fold change (mRNA) on the y-axis, ranging from 0.0 to 1.6, for genes TSA1, ACT1, CLB1, CLB2, CLB3, CLB4 on the x-axis. The chart compares four conditions: wild type (dark grey bars), fkh1Δ (light grey bars), fkh2Δ (white bars with dark outline), and fkh1Δfkh2Δ (white bars).::>bFkh2 binding<::bar chart showing Fold change (protein) on the y-axis, ranging from 0 to 7, for genes TSA1, ACT1, CLB1, CLB2, CLB3, CLB4 on the x-axis.::>cNdd1 binding<::bar chart showing Fold change (protein) on the y-axis, ranging from 0 to 7, for genes TSA1, ACT1, CLB1, CLB2, CLB3, CLB4 on the x-axis.::>dTime (min) 0 30 60 80 90 100 110 120 130 140 150 160 170 180<::Western blot images for three genotypes: wild type, fkh1Δ, and fkh2Δ. Each genotype section shows protein bands over time for Clb3-TAP, Sic1-TAP, Clb5-HA, and G6PDH.::>e<::bar chart showing Clb3-TAP amount on the y-axis, ranging from 0 to 50, against Time (min) on the x-axis, with labels at 0, 30, 60, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180. The chart compares three conditions: wild type (dark grey bars), fkh1Δ (light grey bars), and fkh2Δ (white bars with dark outline).::>

<a id='9226ea6d-239f-4e8d-b3c6-75482de0dedd'></a>

Fig. 2 Fkh1 and Fkh2 regulate dynamics of mitotic Clb cyclins in a cell cycle-dependent manner. a Quantitative real-time PCR of mitotic CLB transcripts in yeast cells treated with nocodazole (NOC). Total mRNA was isolated from arrested wild type, fkh1Δ, fkh2Δ, and fkh1Δfkh2Δ cells, and CLB1, CLB2, CLB3, and CLB4 mRNA levels were measured. ACT1 and TSA1 genes were used as negative controls, as they are not affected by cell cycle dynamics. Error bars on the histograms represent SDs from the mean of three independent experiments; p-values are indicated on the histograms in Supplementary Fig. S2a. Nocodazole-arrested cells show that fkh2Δ affects both CLB3 and CLB4 transcript accumulation, whereas fkh1Δ affects CLB4 transcript accumulation. b, c Binding of Fkh2 (b) and Ndd1 (c) to mitotic CLB promoter regions. Chromatin immunoprecipitation was performed by precipitating protein/DNA complexes from cells grown in exponential phase using an anti-Myc antibody. ACT1 and TSA1 genes were used as negative controls, whereas CLB1 and CLB2 genes as positive controls. Error bars on the histograms represent SDs from the mean of three independent experiments. d, e Fkh2 controls the timing of Clb3 protein expression. d Time course of Clb2-18Myc, Clb3-TAP, Clb5-HA and Sic1-TAP are shown for wild type (YAN49), fkh1Δ (YAG20), and fkh2Δ (YAG21) strains. Yeast cells were synchronized by centrifugal elutriation in YPD at 30 °C, released into fresh YPD at 30 °C, and sampled for western blot analysis at the indicated times. Clb3 levels were quantified in wild type, fkh1Δ and fkh2Δ strains (e). The experiments were performed at the same time, and the membranes processed identically, with the same antibody aliquots and then exposed to the same levels. fkh1Δ resulted in an decreased amount of Clb3 produced and no time delay as compared to wild type, whereas fkh2Δ resulted in both a decreased amount of Clb3 produced and a time delay as compared to wild type. The result is representative of three independent experiments

<a id='9516e836-4732-4ed9-b204-ad4798f237d8'></a>

npj Systems Biology and Applications (2017) 7

<a id='44441c70-2804-4cd2-8b23-d4bb6d491158'></a>

Published in partnership with the Systems Biology Institute

<!-- PAGE BREAK -->

<a id='a848c6dc-8bbb-4e80-92c2-488e74ee90c1'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke *et al*
---

<a id='a4694a47-1c86-421c-87a2-7b772b016158'></a>

npj

<a id='38d848cf-e303-4831-907c-5cb689825113'></a>

points of the time course (Fig. 2d). However, our quantitative
real-time PCR analyses did not show any effect of Fkh2 on CLB5
mRNA levels (see Supplementary Text and Supplementary Fig.
S2f). This suggests that other mechanisms, such as a reduced
degradation of Clb5 due to a reduced CLB2 transcription/
translation and of Clb2/Cdk1 complexes that activate the APC
machinery, 18 may be responsible for the early accumulation of
Clb5 protein levels.

<a id='4f8cef09-90c2-4e86-9357-f40c7decebfb'></a>

Remarkably, since we discovered that Fkh2 promotes _CLB3_ transcription, Clb3/Cdk1 may phosphorylate this transcription factor at _CLB3_ promoter, through a positive feedback loop to produce additional Clb3 protein, and at _CLB2_ promoter to produce Clb2. In order to explore computationally the possible contribu-tion of these regulations, we investigated their ability to generate the characteristic behavior of the waves of Clb cyclins. Our simulations revealed that a positive feedback loop on _CLB3_ transcription may provide an additional, but not _per se_ sufficient mechanism to shape Clb waves (see Supplementary Text and Supplementary Fig. S3).

<a id='def2fa2a-c375-401a-b443-e93d372c38e6'></a>

Clb3, but not Clb2, co-localizes with Fkh2/Ndd1in HU-treated cells
The transcription factor Fkh2 acts in a DNA-bound complex with the transcription factor Mcm1 to regulate cell cycle-dependent expression of the _CLB2_ cluster, and binding of Fkh2 requires prior binding by Mcm1.$^{9, 10}$ Since Fkh2 is involved in the transcription of both _CLB3_ and _CLB2_ genes, Clb5/Cdk1 may phosphorylate this transcription factor at both promoters. Our kinetic model predicted an involvement of an activator molecule—which we have shown to be the transcription factor Fkh2—by Clb3/Cdk1, in order to promote _CLB2_ expression. To address this aspect, we first investigated whether Clb3 co-localized with Fkh2. We followed the association of Fkh2 and its coactivator Ndd1 in time by bimolecular fluorescence complementation (BiFC) (see Supplementary Materials and Methods for details and Fig. S4a), after α-factor-mediated synchronization of cells in G1 phase. The presence of a yellow fluorescent signal, also called BiFC signal, highlighted a nuclear localization of the Fkh2/Ndd1 complex formation starting from the early S to G2/M phase (Supplementary Fig. S4b). Specifically, the BiFC signals stably appear at 30 min after α-factor synchronization, which corresponds to the time at which the _CLB2_ promoter is active$^{8}$ following the recruitment of Ndd1 to chromatin in a cell cycle-specific manner.$^{19}$ Subsequently, Clb3-CFP was integrated in the genome of these cells under control of the endogenous promoter to follow its co-localization with the BiFC signals, and Clb2-CFP was used as control for the experiment. In hydroxyurea-treated cells, Clb3 clearly co-localizes with the BiFC signals, whereas a very low, not localized Clb2-CFP signal is detected (Fig. 3a). The co-localization of Clb2 with the Ndd1/Fkh2 complex occurs later in mitosis, as previously shown$^{10}$ (data not shown). This finding indicates that Clb3 co-localizes with the Fkh2/Ndd1 complex before Clb2 accumulation, and suggests a functional interaction between Clb3 and this complex to activate the _CLB2_ promoter.

<a id='8bb9bb1f-1180-4e80-a794-38090c008bc9'></a>

Clb3 interacts with Fkh2/Ndd1 and, together with Cdk1,
phosphorylates Fkh2
To address the potential association between Clb3 and Fkh2, we
performed a Yeast-two-Hybrid assay. Bait (pBTM117) and prey
(pACT4) constructs were generated for Fkh2 and Clb cyclins
(see Supplementary Materials and Methods for details), 12, 20 with
the potential interacting partners being overexpressed. Fkh2 full-
length and a truncated, C-terminal region of the protein Fkh2387
(amino acids 387-862) (see Supplementary Fig. S5a for a
schematic representation of the constructs used in this study)
were tested. Both Fkh2 full-length (Supplementary Fig. S5b) and
Fkh2387 (Fig. 3b) showed a clear interaction with Clb3 as well as
with the other Clb cyclins. The interactions between Fkh2387 and

<a id='f2b7cc13-ad00-4764-b1fc-35662d0704a9'></a>

Clb cyclins were validated independently by a GST pull-down
assay (Supplementary Fig. S5e).

<a id='84057c81-7436-42ad-8c1a-7ff802b7e39c'></a>

Subsequently, Fkh2 phosphorylation by the Clb3/Cdk1 complex was tested by immunoprecipitating Clb3/Cdk1 from a yeast lysate that expressed HA-tagged Clb3 and incubating it with bacterially expressed and purified GST-Fkh2 (see Supplementary Materials and Methods for details). We observed that Fkh2 is a substrate of the Clb3-associated kinase activity, as compared to a wild-type strain where Clb3 was not tagged (negative control) (Fig. 3c). Prompted by this result, we have tested whether Clb3/Cdk1 was able to phosphorylate Fkh2 in vivo. To this aim, Fkh2 mobility was detected in a Phos-tag gel in wild type, clb3Δ, clb4Δ, and clb3Δclb4Δ synchronized in G1 phase with α-factor. Fkh2 was phosphorylated in a similar manner in all tested strains (Fig. 3d, left panel). Then, we hypothesized that, in absence of Clb3 and Clb4, Clb2 could replace them. Thus, we have introduced a clb2Δ mutation in wild type and clb3Δclb4Δ strains, and observed a clear decrease in Fkh2 mobility in the clb2Δclb3Δclb4Δ strain as compared to the clb2Δ strain, indicating a role for Clb3,4 in Fkh2 phosphorylation (Fig. 3d, right panel). In order to provide further evidence of the Clb3/Cdk1-mediated phosphorylation on Fkh2, we have tested the kinase activity of Clb3/Cdk1 isolated from a wild-type yeast lysate on a bacterially expressed Fkh2, either full-length or variants carrying single point mutations in two phosphorylation sites (S683 and T697). Both phosphosites are located in the C-terminal region of Fkh2, and have been shown to be phosphorylated by Clb2/Cdk1.10 Deletion of these residues leads to a reduction of the amount of Fkh2 phosphorylated.10 We observed that the Clb3-associated kinase activity is reduced on both mutants between 20% to 40% as compared to a full-length Fkh2 (Fig. 3e), indicating that the phosphosites S683 and T697 mediate the activation of Fkh2 by all Clb/Cdk1 kinase complexes. Altogether, our data confirm that Fkh2 interacts with Clb5, as reported previously,10 and with all Clb cyclins, and show that Clb3/ Cdk1 interacts with, and phosphorylates, Fkh2.

<a id='beb6d632-9c17-4ffe-9b68-3434ce5d727c'></a>

Besides interacting with and phosphorylating Fkh2, Clb3,4/Cdk1 may also play a role in Ndd1 phosphorylation in vivo to prime CLB2 transcription. Associations of Ndd1 with Clb2 and Clb3 have been detected in a high-throughput genome-wide screening for complexes, 21 but they were not independently validated. To test the Ndd1/Clb2 and Ndd1/Clb3 potential associations, haploid yeast cells expressing the C-terminal region of the Venus protein fused to the C-terminal region of Ndd1 (Ndd1-VC) were transformed with a plasmid carrying the N-terminal region of the Venus protein fused to the C-terminal region of Clb1-4 (VN-Clb1-4). The BiFC signal was observed only for the Ndd1/Clb2 and Ndd1/Clb3 pairs (Fig. 3f). These interactions were further validated by Yeast-two-Hybrid (Fig. S5f) and GST pull-down (Supplementary Fig. S5g) assays, respectively. Our data, together with the evidence showing that Ndd1 is a substrate of the Clb3-associated kinase activity, 22 support the hypothesis that the Fkh2/Ndd1 complex may be regulated by all Clb/Cdk1 complexes.

<a id='a31e9904-4d49-45a8-b53a-f45df7655fbc'></a>

Clb5/Cdk1 and Clb3/Cdk1 are responsible for a sequential mitotic CLB expression
The data presented provide an overall scenario in which the various Clb/Cdk1 complexes are responsible for the transcription of both _CLB3_ and _CLB2_ after phosphorylation, and activation, of the transcription factor Fkh2. Thus, this scenario predicts that the first Clb/Cdk1 complex activated, Clb5/Cdk1, would promote the transcription of _CLB3_ and activation of the next kinase complex in the signaling cascade, Clb3/Cdk1, which ultimately—together with Clb5/Cdk1—would be responsible for the transcription of _CLB2_ and activation of the last kinase complex of the cascade, Clb2/Cdk1. To investigate the role of each Clb/Cdk1 complex on _CLB_ transcription suggested by both computational and experi- mental analyses, we tested the influence of Clb5,6 and Clb3,4 on

<a id='77b309f1-d777-479f-940f-af2729b835bc'></a>

Published in partnership with the Systems Biology Institute

<a id='c2b8e97e-753d-4219-abd8-e4f46be698d8'></a>

npj Systems Biology and Applications (2017) 7

<a id='f48310fc-c0f7-4b85-9e2d-750e32d719dc'></a>

5

<!-- PAGE BREAK -->

<a id='31129558-0da1-4126-842a-d46155dbc69b'></a>

<::npj
: figure::>

<a id='4a4872c7-3511-405f-919a-fcf1371da5c1'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al

<a id='73d28a84-2f12-4ddb-a7f8-a2347ea2dd49'></a>

6

<a id='a40997fa-8399-4265-84cd-3006f9da7089'></a>

a Transmitted light <::microscope images: Two brightfield microscope images of yeast cells, each with a 5 μm scale bar. The cells appear as small, light-colored spheres against a grey background.::> Venus Ndd1/Fkh2 <::microscope images: Two fluorescent microscope images showing yeast cells with yellow fluorescence. The cells are irregularly shaped, with bright yellow signals.::> Clb3-CFP <::microscope images: A fluorescent microscope image showing yeast cells with cyan fluorescence. The cells are irregularly shaped, with bright cyan signals.::> Clb2-CFP <::microscope images: A fluorescent microscope image showing yeast cells with cyan fluorescence. The cells are irregularly shaped, with bright cyan signals.::> HU treatment <::histograms: Two histograms, both with 'Count' on the y-axis (0 to 200) and 'FL2-H' on the x-axis (0 to 1000). Both histograms show a prominent peak around FL2-H values of 200-300, indicating a population of cells with similar fluorescence intensity.::> b pBTM + pACT pBTM-Fkh2₃₈₇ + pACT pBTM-Fkh2₃₈₇ + pACT-Clb1 pBTM + pACT-Clb1 pBTM-Fkh2₃₈₇ + pACT-Clb2 pBTM + pACT-Clb2 pBTM-Fkh2₃₈₇ + pACT-Clb3 pBTM + pACT-Clb3 pBTM-Fkh2₃₈₇ + pACT -Clb4 pBTM + pACT-Clb4 pBTM-Fkh2₃₈₇ + pACT-Clb5 pBTM + pACT-Clb5 pBTM-Fkh2₃₈₇ + pACT-Clb6 pBTM + pACT-Clb6 pBTM-F4 + pACT-PABC1 β-Galactosidase SDII SDIV <::yeast two-hybrid assay results: A panel showing results from a yeast two-hybrid assay. The leftmost column lists 16 different plasmid combinations. To the right, there are three columns of agar plate patches, labeled 'β-Galactosidase', 'SDII', and 'SDIV'. Each row corresponds to a plasmid combination and shows three patches. In the 'β-Galactosidase' column, blue coloration indicates positive interaction (e.g., pBTM-Fkh2₃₈₇ + pACT-Clb3, pBTM-Fkh2₃₈₇ + pACT-Clb4, pBTM-F4 + pACT-PABC1 show strong blue). The 'SDII' and 'SDIV' columns show growth on selective media, with larger patches indicating stronger growth. For example, pBTM-Fkh2₃₈₇ + pACT-Clb3 and pBTM-Fkh2₃₈₇ + pACT-Clb4 show robust growth on both SDII and SDIV, consistent with their β-Galactosidase activity.::>

<a id='aef1b3fe-1403-4969-9e2b-c4690323204b'></a>

c GST-Fkh2 Clb3-HA No tag <::Western blot and autoradiogram. The blot is divided into two columns, 'Clb3-HA' and 'No tag', under the heading 'GST-Fkh2'. There are four rows of bands. The first row, labeled '³²P' (autoradiogram), shows a strong band in the 'Clb3-HA' lane and a very faint band in the 'No tag' lane. The second row, labeled 'α-GST' (Western blot), shows a band of similar intensity in both 'Clb3-HA' and 'No tag' lanes. The third row, labeled 'α-HA' (Western blot), shows a strong band in the 'Clb3-HA' lane and no band in the 'No tag' lane. The fourth row, labeled 'IP input (Cdk1)' (Western blot), shows bands of similar intensity in both lanes.:> α-HA IP + Kinase assay d kDa 116- <::Western blot. The blot shows protein bands around the 116 kDa marker. The lanes are grouped by strain and treatment: wild type (α-factor, Release), clb3Δ (α-factor, Release), clb4Δ (α-factor, Release), clb3Δclb4Δ (α-factor, Release), clb2Δ (α-factor, Release), and clb2Δclb3Δclb4 (α-factor, Release). In the wild type lane, a prominent band is visible in the 'α-factor' condition, which is slightly less intense in 'Release'. Similar patterns are observed across all mutant strains, with varying intensities of the band in both 'α-factor' and 'Release' conditions.::> e HistoneH1 Fkh2_full-length Fkh2_S683A Fkh2_S697A <::Western blot. The blot is arranged in three rows and four columns. The columns represent different samples: 'HistoneH1', 'Fkh2_full-length', 'Fkh2_S683A', and 'Fkh2_S697A'. The rows are labeled on the right: '←Clb2-Cdk1', '←Clb3-Cdk1', and '←Input'. In the 'Clb2-Cdk1' row, bands are visible across all Fkh2 samples, with 'HistoneH1' showing a distinct band. In the 'Clb3-Cdk1' row, bands are also visible across all Fkh2 samples and 'HistoneH1'. The 'Input' row shows bands for all Fkh2 samples, indicating protein presence.::> ■Fkh2_full-length ■Fkh2_S683A ■Fkh2_S697A <::Bar chart titled 'Phosphorylation (a.u.)' on the y-axis, ranging from 0 to 1.2. The x-axis shows two conditions: 'Clb2/Cdk1' and 'Clb3/Cdk1'. A legend indicates the bars: black for 'Fkh2_full-length', dark grey for 'Fkh2_S683A', and light grey for 'Fkh2_S697A'. For 'Clb2/Cdk1': 'Fkh2_full-length' has a phosphorylation value of approximately 1.0, 'Fkh2_S683A' is around 0.6, and 'Fkh2_S697A' is also around 0.6. For 'Clb3/Cdk1': 'Fkh2_full-length' has a phosphorylation value of approximately 1.0, 'Fkh2_S683A' is around 0.7, and 'Fkh2_S697A' is around 0.8. Error bars are present on all bars.::> Clb2/Cdk1 Clb3/Cdk1

<a id='2954b2f9-7e63-4ace-ba0e-4d490a04ed05'></a>

f
<::Figure showing microscopy images of yeast cells under different conditions. The figure is arranged in a 2x4 grid.

**Row 1: Transmitted light images**
- **Column 1 (+VN-Clb1):** Grey-scale image of numerous circular yeast cells, some budding, against a light background. A 5 µm scale bar is present.
- **Column 2 (+VN-Clb2):** Grey-scale image of numerous circular yeast cells, some budding, against a light background. A 5 µm scale bar is present.
- **Column 3 (+VN-Clb3):** Grey-scale image of numerous circular yeast cells, some budding, against a light background. A 5 µm scale bar is present.
- **Column 4 (+VN-Clb4):** Grey-scale image of numerous circular yeast cells, some budding, against a light background. A 5 µm scale bar is present.

**Row 2: Venus (Ndd1/Clb) fluorescent images**
- **Column 1 (+VN-Clb1):** Dark background with scattered small, bright yellow, circular fluorescent signals representing yeast cells.
- **Column 2 (+VN-Clb2):** Dark background with scattered small, bright yellow, circular fluorescent signals representing yeast cells.
- **Column 3 (+VN-Clb3):** Dark background with numerous small to medium-sized, very bright yellow, circular fluorescent signals representing yeast cells, indicating strong fluorescence.
- **Column 4 (+VN-Clb4):** Dark background with numerous small to medium-sized, bright yellow, circular fluorescent signals representing yeast cells, indicating strong fluorescence.
: figure::>

<a id='232f09d0-4b05-428d-b01e-448a5f27c255'></a>

npj Systems Biology and Applications (2017) 7

<a id='ef283639-29a8-4bcc-9086-b951009425a7'></a>

Published in partnership with the Systems Biology Institute

<!-- PAGE BREAK -->

<a id='5ca09514-2f1a-4787-9be1-d7fb0fa6e0c4'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al

<a id='1c8e2739-bfc0-4622-a586-db0981f7c06f'></a>

npj

<a id='720664f2-cd4c-4f1d-be94-cd0ec9d4fc68'></a>

Fig. 3 Clb3/Cdk1 co-localizes with, interacts and phosphorylates the Ndd1/Fkh2 complex.
a Co-colocalization of Clb3 and Clb2 with the Ndd1/Fkh2 complex. Yeast cells expressing Ndd1-VC and carrying Clb3-CFP or Clb2-CFP integrated in the genome were transformed with the plasmid p426-VN-Fkh2. Selected transformants were synchronized in S phase with hydroxyurea (HU) and monitored for the fluorescent (BiFC) signal. A co-localization with the BiFC signal is shown for Clb3. Growth arrest was examined by staining with propidium iodide and FACS analysis.
b Fkh2 C-terminal region (Fkh2387) associates with Clb cyclins by Yeast-two-Hybrid assay. Yeast cells expressing the fusion proteins LexA-Fkh2387 (pBTM-Fkh2387) and AD-Clb1-6 (pACT-Clb1-6) were spotted onto SDII and SDIV selective media or on a membrane for detection of the β-galactosidase activity. The interaction between ATXN2-FD and PABC was used as positive control. 12 At least three independent transformations have been performed, and four clones were tested in each experiment.
c Fkh2 is a substrate of Clb3/Cdk1 kinase activity in vitro. Yeast lysate expressing Clb3-HA was incubated with GST-Fkh2 expressed and purified from E. coli. After the kinase assay, the membrane was plotted using antibodies against GST (to detect Fkh2), HA (to detect Clb3), and PSTAIR (to detect Cdk1). The accuracy of the result was verified by monitoring that a similar amount of Cdk1 kinase in the immunoprecipitation (IP), and of GST-Fkh2 was used in the assay.
d Fkh2 is phosphorylated in vivo by Clb3/Cdk1 kinase activity. Wild type, clb3Δ, clb4Δ, clb3Δclb4Δ, clb2Δ, and clb2Δclb3Δclb4Δ were grown at 25 °C in YPD medium and then synchronized in G1 phase with α-factor, before releasing them into fresh medium for 50 min (Release). Protein extracts were analyzed in 6% polyacrylamide gel electrophoresis (PAGE) 10 μM Phos-tag gel and Fkh2-6HA was followed by western blot.
e Fkh2 phosphosite specificity of Clb3/Cdk1. Fkh2 full-length and mutants (S684A and S697A) were isolated from bacterial protein extracts and phosphorylated by Clb2/Cdk1 and Clb3/Cdk1 isolated from yeast extracts containing overexpressed Clb2-TAP or Clb3-TAP. An excess of purified Fkh2 was added to fully saturate the cyclin/Cdk1 complexes. Kinase reactions were started by adding purified Clb2/Cdk1 or Clb3/Cdk1, and 32P-ATP to the mixture. Histone H1 was used as a control, and standard sodium dodecyl sulfate-PAGE was used to separate phosphorylated species. Quantification of the phosphorylation extent (arbitrary units) is realized with PhosphoImager, as average from two different time points; values relative to a full-length Fkh2 are shown. The result is representative of three independent experiments.
f Clb3 associates with Ndd1 by BiFC. Yeast cells expressing the fusion protein Ndd1-VC were transformed with the plasmids p426-VN-Clb1, p426-VN-Clb2, p426-VN-Clb3, and p426-VN-Clb4, respectively. Detection of the fluorescent (BiFC) signal was revealed by fluorescence microscopy

<a id='bbb35db7-7acb-4c5e-a317-5daa70017434'></a>

a<::bar chart::NOC treatment. The y-axis is 'Fold change (mRNA)' ranging from 0.0 to 1.6. The x-axis shows four gene categories: TSA1, ACT1, CLB2, and CLB3. For each gene, there are four bars representing different cell types, as indicated by the legend below the chart: wild type (black bar), fkh2Δ (dark gray bar), clb3Δclb4Δ (light gray bar), and clb5Δclb6Δ (white bar). Error bars indicate standard deviation. For TSA1, all four cell types show fold change around 1.0. For ACT1, all four cell types show fold change around 1.0. For CLB2, wild type is around 1.0, fkh2Δ is around 0.65, clb3Δclb4Δ is around 0.55, and clb5Δclb6Δ is around 0.5. For CLB3, wild type is around 1.0, fkh2Δ is around 0.6, clb3Δclb4Δ is around 0.5, and clb5Δclb6Δ is around 0.75.::>b<::schematic::A regulatory network diagram showing connections between Fkh/Ndd1 and Clb/Cdk1 complexes, divided into four regions: A, B, C, and D. Region A (top right, red dashed box) shows MBF activating CLB5 transcription, which leads to Clb5. Clb5 has known interactions (solid red arrows) affecting Clb3 and Clb2. Region B (middle right, blue dashed box) shows Fkh1 and Fkh2, along with Ndd1, regulating CLB3 transcription, leading to Clb3. Clb3 also has known interactions (solid blue arrows) affecting Clb2. Region C (left, gray dashed box) shows Fkh1 and Ndd1 interacting with Fkh2 and Ndd1. Region D (bottom center, gray dashed box) shows Fkh1 and Fkh2, along with Ndd1, regulating CLB2 transcription, leading to Clb2. Colored solid arrows represent known interactions. Colored dashed arrows (red, blue, green) represent newly unraveled interactions between Fkh2/Ndd1 and Clb/Cdk1 complexes. Gray dashed arrows represent newly unraveled interactions between Fkh1/Ndd1 and Clb/Cdk1 complexes. Specific interactions include: - Clb5 (from A) activates Clb3 (blue dashed arrow) and Clb2 (red dashed arrow). - Fkh2/Ndd1 (from B) activates CLB3 transcription. - Fkh2/Ndd1 (from D) activates CLB2 transcription. - Clb3 (from B) inhibits Fkh2/Ndd1 (blue dashed arrow). - Clb2 (from D) inhibits Fkh2/Ndd1 (green dashed arrow). - Fkh1/Ndd1 (from C) has gray dashed arrow interactions with Fkh2/Ndd1 and Clb3. - Fkh1/Ndd1 (from D) has gray dashed arrow interactions with Fkh2/Ndd1 and Clb2.::>Fig. 4 a Quantitative real-time PCR of mitotic CLB transcripts in yeast cells treated with nocodazole. Total mRNA was isolated from arrested wild type, fkh2Δ, clb3Δclb4Δ, or clb5Δclb6Δ cells, and CLB2 and CLB3 mRNA levels were measured. ACT1 and TSA1 genes were used as negative controls, as they are not affected by cell cycle dynamics. Error bars on the histograms represent SDs from the mean of three independent experiments; p-values are indicated on the histograms in Supplementary Fig. S5h. Nocodazole-arrested cells show that clb3Δclb4Δ affects CLB2 transcript accumulation, whereas clb5Δclb6Δ affects both CLB2 and CLB3 transcript accumulation. b Schematic view of the regulatory connections involving the Fkh/Ndd1 and Clb/Cdk1 complexes. Colored solid arrows refer to the known interactions reported in literature; colored dashed arrows refer to the newly unraveled interactions between Fkh2/Ndd1 and Clb/Cdk1 complexes; gray dashed arrows refer to the newly unraveled interactions between Fkh1/Ndd1 and Clb/Cdk1 complexes. See text for details

<a id='eac54a1c-3e89-4d97-aea1-4ef2e0a77de7'></a>

both CLB3 and CLB2 transcript levels. Mitotic CLB mRNA levels were measured in fkh2Δ, clb3Δclb4Δ, or clb5Δclb6Δ strains after nocodazole treatment by quantitative real-time PCR. The fkh2Δ strain was used as a control for the experiment, leading to a reduction of both CLB2 and CLB3 mRNA levels as compared to wild type (Fig. 4a), as shown in Fig. 2a. Reduced CLB2 mRNA levels were observed in clb3Δclb4Δ mutants, whereas no CLB3 transcripts were detected, as expected (Fig. 4a). Furthermore, reduced mRNA levels were observed for both CLB2 and CLB3 in clb5Δclb6Δ mutants as compared to wild type, with the former being strongly affected as compared to the latter (Fig. 4a). This result indicates that Clb5,6 promotes CLB3 transcription, and that both Clb5,6 and Clb3,4 impact on CLB2 transcription (Fig. 4a). Thus, this evidence recapitulates both computational and experimental analyses, indicating that both Clb5/Cdk1 and Clb3/Cdk1 promote CLB2 transcription, and that their progressive activation through Fkh2 guarantees timely waves of Clb cyclins throughout cell cycle progression.

<a id='5ab7600c-6646-43fd-9f4a-25c8a6930afc'></a>

In summary, our data support the hypothesis that the Fkh2/ Ndd1 complex may be regulated by all Clb/Cdk1complexes for the activation of CLB3 and CLB2 promoters (Fig. 4b, colored dotted lines). Regulation mediated by Clb/Cdk1 complexes might occur also on Fkh1/Ndd1 (Fig. 4b, gray dotted lines), as we observed its interaction with some of the Clb cyclins (Supplementary Fig. S6). Remarkably, cooperativity between Ndd1 and Fkh1 was predicted by computational work, 23 and we observed this specific interac- tion both in vitro and in vivo (Supplementary Fig. S7).

<a id='c1b9825e-65cf-4747-ba2d-501dbcbd0660'></a>

A linear *CLB* cascade is required to generate temporal oscillations of Clb waves
To theoretically investigate the contribution of the known regulatory interactions of the minimal cyclin network (Fig. 1a)¹² as well as of the newly unraveled transcriptional cascade activating *CLB* genes to the waves of Clb activation, we employed an independent, qualitative modeling approach, the Boolean modeling, to identify the possible network structure(s) able to reproduce this oscillatory behavior. A prior knowledge network (PKN) of the interactions among four nodes encompassing the mitotic cyclins Clb5, Clb3 and Clb2, and the cyclin-dependent inhibitor Sic1²⁴ was modeled (Fig. 5a) following the strategy shown in Fig. 5b (for simplicity, each node was assumed to represent the four cell cycle phases: Sic1 (G1), Clb5 (S), Clb3 (G2), and Clb2 (M). This approach, which does not rely on the use of rate constants for the model reactions as compared to kinetic modeling, has been employed to implement all known

<a id='31ca9270-4901-444e-b86b-781658de6bf5'></a>

Published in partnership with the Systems Biology Institute

<a id='f13215eb-3da2-4f66-ad9f-b670eff19bca'></a>

npj Systems Biology and Applications (2017) 7

<a id='a134d633-7523-436f-882d-524d151d24ca'></a>

7

<!-- PAGE BREAK -->

<a id='05b41591-8c47-439e-8d44-2920e9a7044d'></a>

npj

<a id='90e6ba91-7ecb-447e-906f-e094ffd0b65b'></a>

Fkh2-dependent regulation of mitotic cyclin waves C Linke et al

<a id='e83c537f-0246-42be-ae04-3144966b2bd7'></a>

a
<::Diagram showing a network of interactions between four components: Sic1 (gray circle), Clb5 (red circle), Clb3 (blue circle), and Clb2 (green circle). Arrows indicate activation, and dashed lines indicate inhibition. Clb5 inhibits Sic1. Sic1 inhibits Clb5. Clb5 activates Clb2 and Clb3. Clb2 activates Clb5. Clb3 activates Clb5. Clb2 inhibits Sic1. Clb3 inhibits Sic1. There are self-activation loops for Clb2 and Clb3. A red arrow from Clb3 inhibits Clb2. A red dashed arrow from Clb2 inhibits Clb3. A red arrow indicates activation from Clb5 to Clb2 and Clb3, and a red dashed arrow indicates inhibition from Clb3 to Clb2. There is a red dashed arrow from Clb2 to Clb3. There are also interactions where Clb5 activates Clb2 and Clb3, and Clb2 and Clb3 activate Clb5.: diagram::>
b
<::Flowchart depicting a model building and filtering strategy. The process starts with four colored circles representing components: Clb5 (red), Sic1 (gray), Clb3 (blue), and Clb2 (green). These components, combined with a document icon, lead to the step "List of all possible interactions". This step then generates a collection of minimal models, represented by multiple sets of four colored circles. The next step, labeled "GenYsis", processes these models. Following GenYsis, a filter is applied for "expected attractors", represented by a trapezoid containing numerical states (e.g., "1000 0100 0110"). This filtering results in a refined set of minimal models. These models then undergo a step labeled "SQUAD", which leads to another filter for "expected curves", represented by a trapezoid containing multiple line graphs. The outcome is a "List of minimal models reproducing experimental observations", shown as a grid of various colored circles. Finally, these models undergo "MaBoSS" and "Cross validation", leading to the conclusion: "All 6 candidates produce same attractors when simulated with a different qualitative strategy.": flowchart::>
List of all possible interactions
All minimal models
Filter for expected attractors
Filter for expected curves
List of minimal models
reproducing experimental
observations
Cross validation
All 6 candidates produce same
attractors when simulated with
a different qualitative strategy
c
<::Three network diagrams, labeled 1, 2, and 3. Each diagram shows four nodes: Clb5 (red circle), Sic1 (gray circle), Clb3 (blue circle), and Clb2 (green circle). Lines with arrows indicate interactions, and '&' symbols represent AND gates.

Diagram 1:
- Clb5 activates Sic1.
- Sic1 inhibits Clb5.
- Clb5 activates Clb3 and Clb2.
- Clb3 activates Clb5.
- Clb2 activates Clb5.
- Clb3 and Clb2 inhibit Sic1.

Diagram 2:
- Clb5 activates Sic1.
- Sic1 inhibits Clb5.
- Clb5 activates Clb3 and Clb2.
- Clb3 and Clb2 activate Clb5 via an AND gate.
- Clb3 and Clb2 inhibit Sic1 via an AND gate.

Diagram 3:
- Clb5 activates Sic1.
- Sic1 inhibits Clb5.
- Clb5 activates Clb3 and Clb2.
- Clb3 activates Clb5.
- Clb2 activates Clb5.
- Clb3 and Clb2 inhibit Sic1 via an AND gate.: diagram::>
d
Sic1 Clb5 Clb3 Clb2
Clb2 dosage = 1
<::Line graph titled "Clb2 dosage = 1" showing the concentration of four components over time. The x-axis represents "Time steps" from 0 to 15. The y-axis represents concentration from 0.0 to 1.0. The legend indicates: Sic1 (black squares), Clb5 (red triangles), Clb3 (blue squares), and Clb2 (green circles). The graph shows oscillatory behavior for Sic1, Clb5, and Clb3, while Clb2 remains at a low, constant level (near 0). Sic1 and Clb3 concentrations peak around 0.8-1.0, while Clb5 peaks slightly lower. Sic1 and Clb5 show inverse oscillations, and Clb3 generally follows Sic1's pattern but with higher peaks.: chart::>
Clb2 dosage = 5
<::Line graph titled "Clb2 dosage = 5" showing the concentration of four components over time. The x-axis represents "Time steps" from 0 to 15. The y-axis represents concentration from 0.0 to 5.0. The legend is the same as the previous graph. In this graph, Clb2 concentration is constant at 5.0. Sic1, Clb5, and Clb3 show significantly dampened oscillations compared to the "Clb2 dosage = 1" graph, with concentrations remaining low (mostly below 1.0) and less distinct peaks.: chart::>
Clb2 dosage = 30
<::Line graph titled "Clb2 dosage = 30" showing the concentration of four components over time. The x-axis represents "Time steps" from 0 to 15. The y-axis represents concentration from 0.0 to 30.0. The legend is the same as the previous graph. Clb2 concentration is constant at 30.0. Sic1, Clb5, and Clb3 concentrations are very low, almost at zero, with no noticeable oscillations. An inset graph is provided, showing a magnified view of the y-axis from 0.0 to 1.0, where Sic1 and Clb5 show minimal activity (brief, small peaks below 0.2) between time steps 7 and 12, while Clb3 remains near zero.: chart::>
Time steps

<a id='76ef36c3-cf97-41d2-a6d6-26668eb3c59a'></a>

npj Systems Biology and Applications (2017) 7

<a id='92ef6d00-a87c-4e60-a0eb-8f9b0a3cb5a6'></a>

Published in partnership with the Systems Biology Institute

<a id='8ee98f25-3d39-4c20-a3e1-105a464ec6f1'></a>

8

<!-- PAGE BREAK -->

<a id='e460cc3c-550c-4bd5-9422-51ae46a51c54'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al

<a id='1ff81da3-d94d-4c68-9c33-0a2955fd674a'></a>

npj

<a id='222c81d1-4fd0-4b9f-ac10-9dadf5cbb355'></a>

9

<a id='c2163c8e-6193-4a3b-a304-9f7613779fee'></a>

**Fig. 5** Expected oscillations in the Clb cyclin network and definition of Boolean attractor candidates. **a** Minimal prior knowledge network (PKN) encompassing the interactions among Clb5 (*red*), Clb3 (*blue*), Clb2 (*green*), and their inhibitor Sic1 (*black*). Known interactions are indicated with *solid lines*.

2 For the newly unraveled interactions, both potential activatory and inhibitory regulations are considered: interactions mimicking positive regulations of an early Clb/Cdk1 complex on the next one through the Fkh2 transcription factor are indicated with *solid red lines*; interactions mimicking negative regulations of an early Clb/Cdk1 complex on the next one through the Fkh2 transcription factor are indicated with *dashed black lines*. **b** Boolean modeling strategy. Novel and known interactions occurring among Clbs and Sic1 were implemented in the models, which were then filtered for the expected attractors (by using GenYsis) and for the expected curves (by using SQUAD). The collection of minimal models reproducing the experimental observations was then validated by using a different qualitative strategy (MaBoSS). **c** Minimal candidate models reproducing experimental Clb and Sic1 waves and satisfying *CLB2* overexpression experiments.

27 The minimal models 2 and 3 satisfy the known experimental conditions (wild type, *SIC1* overexpression and *sic1Δ*) by both Boolean simulations (GenYsis) and standarized ODE simulations (SQUAD). Arrows and circles denote activations and inhibitions, respectively. **d** SQUAD simulations of *CLB2* overexpression experiments for the minimal model 2. From *top to bottom* are plotted simulations of an increase dosage of Clb2: 1 (*upper panel*), 5 (*mid panel*), and 30 (*bottom panel*). The insert in the *bottom panel* represents a magnification of Sic1, Clb5, and Clb3 oscillations when Clb2 is set to 30. It shall be noted that by the computational time *t* = 15 the cycles are progressively reduced when increasing the Clb2 level. The results are in agreement with the experimental observations.

27

<a id='3076c66a-19e5-40cc-9feb-5d4185cf012b'></a>

<table id="8-1">
<tr><td id="8-2" colspan="3">Table 1. Minimal model edge pool</td></tr>
<tr><td id="8-3">Clb2</td><td id="8-4">→</td><td id="8-5">Sic1</td></tr>
<tr><td id="8-6">Clb2 &amp; Clb3</td><td id="8-7">→</td><td id="8-8">Sic1</td></tr>
<tr><td id="8-9">^Clb2</td><td id="8-a">┬</td><td id="8-b">Sic1</td></tr>
<tr><td id="8-c">Sic1 &amp; Clb2</td><td id="8-d">┬</td><td id="8-e">Clb5</td></tr>
<tr><td id="8-f">Sic1 &amp; Clb3 &amp; Clb2</td><td id="8-g">→</td><td id="8-h">Clb5</td></tr>
<tr><td id="8-i">Clb5</td><td id="8-j">→</td><td id="8-k">Clb3</td></tr>
<tr><td id="8-l">^Clb5 &amp; Sic1</td><td id="8-m">→</td><td id="8-n">Clb3</td></tr>
<tr><td id="8-o">Clb3</td><td id="8-p">→</td><td id="8-q">Clb2</td></tr>
<tr><td id="8-r">^Clb3</td><td id="8-s">→</td><td id="8-t">Clb2</td></tr>
<tr><td id="8-u">Sic1 &amp; ^Clb3</td><td id="8-v">→</td><td id="8-w">Clb2</td></tr>
<tr><td id="8-x" colspan="3">List of regulatory rules not contradicting any of the transitions for attractors (wild type and SIC1 overexpression) and steady states (sic1Δ). This edge pool is the result of filtering the attractor candidate B (see Supplementary Fig. S8b). Three logical rules can specify the regulation of Sic1 and Clb2, and two logical rules can specify the regulation of Clb5 and Clb3. The symbol used are: ^, NOT; &amp;, AND; →, activation; —, inhibition.</td></tr>
</table>

<a id='57d729e9-0c65-432c-9bd6-74d804e99ca7'></a>

regulations occurring among Clbs and Sic1 (ref. 12) as well our
newly unraveled interactions. Furthermore, both activatory and
inhibitory regulations were considered, to not exclude any
potential direct or indirect modes that may have an impact on
the formation of Clb waves. Various optimization strategies to
analyze the PKN (see Supplementary Text for details) were not
able to reproduce the behavior of three experimental conditions,
i.e., wild type, deletion of SIC1 and overexpression of SIC1, which
have definite phenotypes regarding the formation of Clb waves.<sup>12</sup>
Possible attractors that reproduce these conditions were then
generated (Supplementary Fig. S8a–S8d), by creating a set of
networks with a minimum number of edges satisfying specific
rules (see Supplementary Text for details on edge filtering and
Table 1) corresponding to the current knowledge of the regulation
among Clbs and Sic1 as well as to our novel experimental findings.
Starting from the edge pool, i.e., the collection of all possible
edges (640) generated previously, the possible minimal models
constructed were 36. These models were simulated by using
GenYsis,<sup>25</sup> reproducing the Boolean attractors expected for the
three experimental conditions. Subsequently, models were filtered
by selecting only those that reproduced the waves of nodes
during qualitative ordinary differential equation (ODE) simulations
by using SQUAD.<sup>26</sup> Among the 36 candidate models that were
simulated, only 6 reproduced the waves observed experimentally
(Supplementary Fig. S9a–S9c).

<a id='5bcc54c6-2051-4ed8-b931-7dedcd731d1c'></a>

In order to restrict further the plausible model candidates, the
effect *CLB* overexpression was simulated and compared to the
known experimental phenotypes. Clb2 can be overexpressed up
to ten-fold as compared to its endogenous level without
significantly reducing cell viability.²⁷ When the 6 model

<a id='86d7238b-e279-4db7-b47e-b01611a80b5b'></a>

<::flowchart: Model for the transcriptional regulation of the mitotic Clb cascade::>
<::caption: Fig. 6 Model for the transcriptional regulation of the mitotic Clb cascade. A coherent type 1 feed-forward loop may activate CLB genes. Our data indicate a linear activation of Clb cyclins via the Fkh2 transcription factor: Clb5/Cdk1 promotes CLB3 transcription (arrow A), Clb3/Cdk1 promotes CLB2 transcription (arrow B) together with Clb5/Cdk1 (arrow C), and Clb2/Cdk1 promotes CLB2 transcription by a positive feedback loop (arrow D). For the sake of clarity, Cdk1 subunit has been omitted. Arrows represent activating interactions::>

<a id='73823fab-cb05-459d-bbb5-175f7a228630'></a>

candidates were tested, two of them (models 2 and 3) were able to reproduce the expected result; the minimal model 2 is shown in Fig. 5c and its simulations are reported in Supplementary Fig. S9d (see Supplementary Fig. S9e for simulations of the minimal model 3). A further increase in Clb2 level reaches a threshold that leads to the inhibition of mitotic exit;27 this is confirmed by our simulations, showing that in these two models the systems collapses when the level of Clb2 is increased upon a certain level (Fig. 5d). The same behavior was observed for the minimal model 3 (see Supplementary Fig. S9f). The structure of the minimal models 2 and 3 is compatible with a sequential, direct activation of mitotic Clb cyclins (Clb5 → Clb3 → Clb2) to produce periodic Clb oscillations that alternate to Sic1. These findings were also independently validated by applying a probabilistic Monte-Carlo approach (see Supplementary Text for details and Supplementary Fig. S10a-S10c).28 With this strategy, we verify that the results obtained with SQUAD are not software-specific, but can be extended to different qualitative methodologies.

<a id='a2338964-dffa-4e7e-96da-bcc1ceb08c58'></a>

Together, our analyses support the experimental findings by showing that a linear transcriptional cascade of _CLB_ activation controls the sequential appearance of waves of Clb cyclins.

<a id='a0229d21-109a-4f05-9beb-1a3b1aa0f109'></a>

Published in partnership with the Systems Biology Institute

<a id='428b8def-36ce-4cc7-bd34-e9779d28923f'></a>

npj Systems Biology and Applications (2017) 7

<!-- PAGE BREAK -->

<a id='8448d88e-8ba2-471a-b8a2-c7230da1e072'></a>

npj

<a id='c0b9760e-a298-4ae6-a484-269f3d7e1b12'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al

<a id='51e5dc2d-e4ef-439c-b689-81fff223a983'></a>

## DISCUSSION
Precise order of cell cycle events is dependent on gradual changes
in substrate specificity of cyclin-dependent kinases, which is
mediated by phase-specific cyclins.29-31 Sequential activation of
cyclins occurs with a characteristic staggered behavior known as
waves of cyclins,1, 2 and oscillations in their level ensure a robust
timing of cell cycle progression. For this timing to be achieved, an
interplay between cyclins, cyclin/Cdk1 activities, and the transcrip-
tion network has been recently deciphered.5, 7, 32, 33 It has been
shown that the mechanism by which transcription of mitotic CLB
cyclin genes is controlled involves Cdk activities and forkhead
transcription factors (Fkhs).4, 34

<a id='b6d7714c-6325-4849-a1d1-298a12c96f55'></a>

We shed new light on the molecular regulation at the basis of the staggered timing of mitotic Clb cyclin waves, by predicting computationally, and validating experimentally, a network motif able to drive the transcriptional activation of CLB genes (Fig. 6). We propose that Fkh2 is activated by sequential accumulation of phase-specific Clb/Cdk1complexes, thus providing a rationale explanation for the sequential appearance of Clb cyclins. Although Fkh2 and Fkh1 are homologous with overlapping functions, Fkh1 showed a stable interaction with at least one cyclin for each Clb subtype, i.e., Clb2, Clb3, and Clb5 (Supplementary Fig. S6a), which represent the more abundant fraction of Clb-associated Cdk1 activities. 35 Accumulation of CLB3 and CLB4 transcripts is decreased in fkh2Δ mutants; conversely, Fkh1 deletion did not affect accumulation of CLB3 transcript levels but led to an increase of CLB4 transcripts in both hydroxyurea- and nocodazole-arrested cells (Supplementary Fig. S2b and Fig. 2a, respectively), suggesting a potential involvement of Fkh1 in CLB4 gene repression during cell cycle progression. Although both Fkh1 and Fkh2 regulate CLB3 transcription and are significantly recruited to the CLB3 promoter, the timely onset of Clb3 protein is affected only in fkh2Δ but not in fkh1Δ cells (Fig. 2d), indicating that Fkh2 controls directly CLB3 expression. Interestingly, the slight inhibitory effect of Fkh1 observed on CLB3 transcription seems to be reflected on the amount of Clb3 protein accumulated but not on its temporal appearance, thus suggesting a yet unknown mechanism by which Fkh1 may modulate Clb3 protein levels. The topology that emerges from these data, in which (i) sequential waves of CLB cyclins transcription are synchronized by Fkh2 and (ii) mitotic Clb/ Cdk1 activities modulate Fkh2 (Fig. 4b), was further validated by computer-based Boolean modeling approaches. This qualitative modeling strategy has been employed to simulate cell cycle dynamics. 36 We identified minimal models of Clb/Cdk1 regulation that produced robust, cyclic oscillations of the mitotic Clb states, compatible with the involvement of an activator molecule—which we have shown to be the Fkh transcription factor Fkh2—in a linear Clb activation. Thus, our experimental and computational analyses pinpoint that Fkh2, major regulator of cell division, controls the temporal expression of mitotic CLB waves, and its activity is modulated by Clb/Cdk1 complexes throughout the cell cycle. In support of this scenario, both Clb5/Cdk1 and Clb3/Cdk1 may promote CLB2 transcription (Fig. 4a)—either by a linear cascade (Clb5 → Clb3 → Clb2) or by a feed-forward loop in which the linear cascade has been shown here to cover a major role—by phosphorylating Fkh2 10 (Fig. 3c, d), and their progressive activation through Fkh2 guarantees timely waves of Clb cyclins throughout cell cycle progression. Interestingly, the phosphosites S683 and T697, both located in the C-terminal region of Fkh2, are recognized by all Clb/Cdk1 kinase activities, and their deletion leads to a reduction on the amount of Fkh2 phosphorylated 10 (Fig. 3e).

<a id='7747066f-b6fc-4b24-b0bb-c441f551022a'></a>

The model of a linear activation of Clb cyclins via Fkh2 may be
part of the classical coherent type 1 feed-forward loop often found
in biochemical networks,³⁷ and it is highly favored during the
evolution of transcriptional networks in budding yeast.¹⁴ This
regulatory mode can sustain temporal Clb oscillations by creating

<a id='5aa6de97-6db0-4450-9768-8f8083971696'></a>

a delay that depends on the logical function between two inputs, Clb5/Cdk1 (X) and Clb3/Cdk1 (Y). X positively regulates Y, and both jointly regulate the common target CLB2 (Z); strikingly, each connection (X→Y, Y Z and X→Z) is in place by the activation of Fkh2 (Fig. 6). The coherent feed-forward loop may serve as a delay element: it responds rapidly to stimuli in one direction (from Clb2 ON to Clb5 OFF for cell cycle re-entry), and at a delay to steps in the opposite direction (from Clb2 OFF to Clb5 ON for cell cycle progression). This may allow for a rapid response and sustained oscillations.38 Feed-forward loops may be seen as a multistep ultrasensitivity,39 where small changes in the level or activity of X can be amplified at the target gene Z because of the combined action of X and Y. Of note, within this regulatory motif, a Clb3/ Cdk1-mediated positive feedback loop on CLB3 transcription (Y→Y) may contribute to timely shape certain Clb waves, without being sufficient per se to generate their oscillatory pattern, for which presence of the direct regulation of Clb3/Cdk1 on CLB2 transcription (Y→Z) is required. However, it is at present not known whether CLB2 expression is dependent on the accumula- tion of adequate levels or activities of both Clb5/Cdk1 and Clb3/ Cdk1 in a threshold-like fashion.

<a id='dea0f042-5da6-49c4-89be-0c97304907fa'></a>

In conclusion, our findings suggest a potential involvement of differential phosphorylation mechanisms⁴⁰ mediated by various Clb/Cdk1 activities for the Fkh1/Fkh2-dependent regulation of phase-specific *CLB* genes. These details have been not yet elucidated, and are currently under investigation in our laboratory. Remarkably, although the C-terminal domain of Fkh2 (amino acids 458–862)—which is missing in Fkh1—contains the majority of Clb/Cdk1 target sites,¹⁰ it does interact weakly with Clb cyclins (Supplementary Fig. S5c). Contrarily, a longer fragment (amino acids 387–862) including a part of the forkhead DNA-binding domain (FKH) revealed a strong interaction with all Clb cyclins (Fig. 3b), thus suggesting that recruitment of Fkh2 is potentially mediated by this region. We speculate that a cooperativity of Clb/Cdk1-dependent phosphorylations could promote the activation of Fkh2 in order to drive timely waves of *CLB* expression. This regulatory mode coupling Clb/Cdk1 activity and transcription may fine tunes the *precise* cell cycle timing, pinpointing a design principle in cell division.

<a id='511fddb7-e33a-41a0-a105-698678c88810'></a>

# MATERIALS AND METHODS
## Yeast strains and plasmids
Yeast strains, plasmids and growth conditions used in this study are described in Supplementary Materials and Methods.

<a id='b01976fc-a9e0-49d9-a154-61d148012dff'></a>

Cell synchronization, cytometry analysis, and western blot
Cell synchronization, cytometry analysis, and western blot were performed
as previously described,  with modifications as described in Supplementary Materials and Methods.

<a id='4273f99d-825e-4642-9ad5-c9409f4ed819'></a>

In vitro kinase assays
For the assay in Fig. 3c, GST-Fkh1 and GST-Fkh2 were expressed in E. coli
and purified using glutathione-Sepharose beads. To obtain the Clb3/Cdk1
complex, the W303 strain and a strain expressing Clb3-HA from its
chromosomal locus were used. For the assay in Fig. 3e, Clb2/Cdk1 and
Clb3/Cdk1 complexes were isolated from the W303 strain. Yeast cells were
transformed with plasmids expressing C-terminal TAP-tagged Clb2 and
Clb3 under galactose (GAL1) promoter (pRSAB1234GAL-CLB2-TAP and
pRSAB1234GAL-CLB3-TAP). The kinase assays were performed as described
in Supplementary Materials and Methods.

<a id='3ba39c12-415b-4ccf-9452-8e73ba838f98'></a>

In vivo phosphorylation assay
For the assay in Fig. 3d, yeast cells were grown at 25 °C in yeast extract peptone dextrose (YPD) and synchronized in G1 phase with a-factor. Samples were collected every 10 min for 90 min after synchronous release, and extracted proteins of the most relevant time points were applied to a 6% polyacrylamide gel electrophoresis (PAGE) gel added with Phos-tag

<a id='af9406cc-1f51-402c-bd18-c6ba3617d68c'></a>

npj Systems Biology and Applications (2017) 7

<a id='7779567c-1d74-450a-af46-01da70357563'></a>

Published in partnership with the Systems Biology Institute

<a id='08b29ad0-e2ae-4840-b281-d9c62a86e669'></a>

10

<!-- PAGE BREAK -->

<a id='9b3e54a5-1679-44d8-81cf-9bf03346d813'></a>

(Wako) and MnCl2 for 2 h at 100 V in the cold. Proteins were transferred to a polyvinylidene difluoride membrane, and Fkh2-6HA was analyzed by western blot using an anti-HA antibody. The kinase assay was performed as described in Supplementary Materials and Methods.

<a id='7afdf8b9-941e-4de5-ad7e-a82fa2f7503f'></a>

Protein-protein interaction assays
Yeast-two-Hybrid screen, GST pull-down and BiFC assays were performed
as previously described2, 0 with modifications as described in Supplementary Materials and Methods.

<a id='0243391e-bddf-4afc-9f8a-7cfa942460d7'></a>

ChIP and real-time PCR
ChIP and quantitative, real-time PCR were performed as previously
described20 with modifications as described in Supplementary Materials
and Methods.

<a id='b071d8f3-4826-4208-ba2d-c227127fa455'></a>

Kinetic and Boolean modeling
Kinetic modeling and global sensitivity analysis were performed as previously described with modifications as described in Supplementary Materials and Methods. Boolean simulations were performed with GenYsis, which uses efficient, reduced ordered binary decision diagrams based algorithms to efficiently compute cyclic attractors. All simulations were performed using the synchronous mode. Continuous simulations were performed with SQUAD, which converts a given network into a discrete dynamical (standardized ODEs) system, and it uses a binary decision diagram algorithm to identify all the steady states of the system. Independent validation of the logical models was performed with MaBoSS, which is based on continuous time Markov processes applied on Boolean state spaces, and translates a set of ODEs on probability distributions. Boolean simulations and analysis of the networks were performed as described in Supplementary Materials and Methods.

<a id='cb12afaa-c7e0-4ffa-b96b-1166416c058f'></a>

## ACKNOWLEDGEMENTS
We thank Eva Dittinger for performing part of the cloning in early stages of the research, Hans Lehrach for providing financial support from the Max Planck Society, and Paul Verbruggen for help with the final layout of the figures. We also thank Gustav Ammerer, Steven Haase, Bruce Futcher, Jens Nielsen, and Hans Westerhoff for valuable discussions. This work was supported by the SILS Starting Grant of the University of Amsterdam, UvA to M.B., by the UvA-Systems Biology Research Priority Area grant to M.B., and by the ENFIN Network of Excellence grant funded by the European Commission to M.B. (within contract number LSHG-CT-2005-518254 to E. K.). We also acknowledge the grant from the European Commission UNICELLSYS, contract number HEALTH-2007-201142 to E.K., S.K., and F.P.); the Spanish Ministry of Economy and Competitiveness (BFU2012-33503 and FEDER) and by Fundación Botín, by Banco Santander through its Santander Universities Global Division to F.P.; the SNSF Swiss National Science Foundation (contract number 132392, SYNERGIA) and State Secretariat for Science Research and Innovation (SEFRI) to I.X.

<a id='3986a970-1de1-4805-b8a5-ed2391876ec7'></a>

## AUTHOR CONTRIBUTIONS
M.B. conceived the idea and the study, designed and co-ordinated the experimental and computational investigations. M.B. performed the kinetic modeling analyses. C.L., A.G.-N, I.A.S., S.T. and M.B. carried out the experiments; C.L. and M.B. designed and performed the majority of the experiments: A.G.-N. carried out the experiments for Figs. 2 h and 3c; I.A.S. carried out the experiments for Figs. 4a and Supplementary Fig. S2f; S.T. re-blotted and quantified the experiments for Fig. 2d, e, and carried out the experiments for Fig. 3d. A.C. and M.B. performed the Boolean modeling analyses. E.K., M.L., S.K., F.P., I.X. and M.B. contributed new reagents/analytical tools. C.L., A.C., A.G.-N, F.P., I.X., and M.B. analyzed the data. C.L., A.C., A.G.-N. and M.B. assembled the Supplementary Information. M.B. wrote the paper. M.B. provided scientific leadership and supervised the study.

<a id='3e0bef3c-0f99-4756-8b0f-9d66117d0ff7'></a>

## COMPETING INTERESTS
The authors declare no conflict of interest.

<a id='ce6d0a38-98ec-4d66-a4ea-afb32711bbdf'></a>

# REFERENCES
1. Futcher, B. Cyclins and the wiring of the yeast cell cycle. Yeast **12**, 1635-1646 (1996).
2. Nasmyth, K. Control of the yeast cell cycle by the Cdc28 protein kinase. *Curr. Opin. Cell Biol.* **5**, 166-179 (1993).

<a id='1af2df62-87a9-40df-902b-c032942e9037'></a>

3. Bloom, J. & Cross, F. R. Multiple levels of cyclin specificity in cell-cycle control. Nat. Rev. Mol. Cell Biol. 8, 149–160 (2007).
4. Breeden, L. L. Cyclin transcription: Timing is everything. Curr. Biol. 10, R586–R588 (2000).
5. Orlando, D. A. et al. Global control of cell cycle transcription by coupled CDK and network oscillators. Nature 453, 944–947 (2008).
6. Haase, S. B. & Wittenberg, C. Topology and control of the cell-cycle-regulated transcriptional circuitry. Genetics 196, 65–90 (2014).
7. Csikász-Nagy, A. et al. Cell cycle regulation by feed-forward loops coupling transcription and phosphorylation. Mol. Syst. Biol. 5, 236 (2009).
8. Koranda, M., Schleiffer, A., Endler, L. & Ammerer, G. Forkhead-like transcription factors recruit Ndd1 to the chromatin of G2/M-specific promoters. Nature 406, 94–98 (2000).
9. Kumar, R., Reynolds, D. M., Shevchenko, A., Goldstone, S. D. & Dalton, S. Forkhead transcription factors, Fkh1p and Fkh2p, collaborate with Mcm1p to control transcription required for M-phase. Curr. Biol. 10, 896–906 (2000).
10. Pic-Taylor, A., Darieva, Z., Morgan, B. A. & Sharrocks, A. D. Regulation of cell cycle-specific gene expression through cyclin-dependent kinase-mediated phosphor-ylation of the forkhead transcription factor Fkh2p. Mol. Cell. Biol. 24, 10036–10046 (2004).
11. Yeong, F. M., Lim, H. H., Wang, Y. & Surana, U. Early expressed Clb proteins allow accumulation of mitotic cyclin by inactivating proteolytic machinery during S phase. Mol. Cell. Biol. 21, 5071–5081 (2001).
12. Barberis, M. et al. Sic1 plays a role in timing and oscillatory behaviour of B-type cyclins. Biotechnol. Adv. 30, 108–130 (2012).
13. Gérard, C., Tyson, J. J., Coudreuse, D. & Novák, B. Cell cycle control by a minimal Cdk network. PLoS Comput. Biol. 11, e1004056 (2015).
14. Lee, T. I. et al. Transcriptional regulatory networks in Saccharomyces cerevisiae. Science 298, 799–804 (2002).
15. Simon, I. et al. Serial regulation of transcriptional regulators in the yeast cell cycle. Cell 106, 697–708 (2001).
16. Hollenhorst, P. C., Pietz, G. & Fox, C. A. Mechanisms controlling differential promoter-occupancy by the yeast forkhead proteins Fkh1p and Fkh2p: implica-tions for regulating the cell cycle and differentiation. Genes Dev 15, 2445–2456 (2001).
17. Vohradsky, J. Stochastic simulation for the inference of transcriptional control network of yeast cyclins genes. Nucleic Acids Res 40, 7096–7103 (2012).
18. Wäsch, R. & Cross, F. R. APC-dependent proteolysis of the mitotic cyclin Clb2 is essential for mitotic exit. Nature 418, 556–562 (2002).
19. Darieva, Z. et al. Cell cycle-regulated transcription through the FHA domain of Fkh2p and the coactivator Ndd1p. Curr. Biol. 13, 1740–1745 (2003).
20. Linke, C., Klipp, E., Lehrach, H., Barberis, M. & Krobitsch, S. Fkh1 and Fkh2 associate with Sir2 to control CLB2 transcription under normal and oxidative stress con-ditions. Front. Physiol 4, 173 (2013).
21. Breitkreutz, A. et al. A global protein kinase and phosphatase interaction network in yeast. Science 328, 1043–1046 (2010).
22. Kõivomägi, M. et al. Dynamics of Cdk1 substrate specificity during the cell cycle. Mol. Cell 42, 610–623 (2011).
23. Tsai, H. K., Lu, H. H. & Li, W. H. Statistical methods for identifying yeast cell cycle transcription factors. Proc. Natl Acad. Sci. USA 102, 13532–13537 (2005).
24. Barberis, M. Sic1 as a timer of Clb cyclin waves in the yeast cell cycle–design principle of not just an inhibitor. FEBS J. 279, 3386–3410 (2012).
25. Garg, A., Di Cara, A., Xenarios, I., Mendoza, L. & De Micheli, G. Synchronous versus asynchronous modeling of gene regulatory networks. Bioinformatics 24, 1917–1925 (2008).
26. Di Cara, A., Garg, A., De Micheli, G., Xenarios, I. & Mendoza, L. Dynamic simulation of regulatory networks using SQUAD. BMC Bioinformatics 8, 462 (2007).
27. Cross, F. R., Schroeder, L., Kruse, M. & Chen, K. C. Quantitative characterization of a mitotic cyclin threshold regulating exit from mitosis. Mol. Biol. Cell 16, 2129–2138 (2005).
28. Stoll, G., Viara, E., Barillot, E. & Calzone, L. Continuous time Boolean modeling for biological signaling: application of Gillespie algorithm. BMC Syst. Biol. 6, 116 (2012).
29. Archambault, V. et al. Targeted proteomic study of the cyclin-Cdk module. Mol. Cell 14, 699–711 (2004).
30. Jin, F. et al. Temporal control of the dephosphorylation of Cdk substrates by mitotic exit pathways in budding yeast. Proc. Natl Acad. Sci. USA 105, 16177–16182 (2008).
31. Loog, M. & Morgan, D. O. Cyclin specificity in the phosphorylation of cyclin-dependent kinase substrates. Nature 434, 104–108 (2005).
32. Chymkowitch, P. et al. Cdc28 kinase activity regulates the basal transcription machinery at a subset of genes. Proc. Natl Acad. Sci. USA 109, 10450–10455 (2012).
33. Simmons Kovacs, L. A. et al. Cyclin-dependent kinases are regulators and effectors of oscillations driven by a transcription factor network. Mol. Cell 45, 669–679 (2012).

<a id='2f23ce4c-6ba5-42dc-9526-83994539eeee'></a>

Published in partnership with the Systems Biology Institute

<a id='904a6356-d485-4851-ae66-9f56d3e8bd91'></a>

npj Systems Biology and Applications (2017) 7

<a id='0f8c8e64-bf7b-44c4-8e6e-5b3985b4b0fa'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al
---

<a id='3e3e79ad-8f64-4713-b9bd-8f41b3196be3'></a>

npj
—
11

<!-- PAGE BREAK -->

<a id='56ac976a-8a62-425b-982e-5f6f4738bf81'></a>

<::npj logo::>

<a id='3d8364f2-1b4a-489d-bdbd-714106088fd9'></a>

Fkh2-dependent regulation of mitotic cyclin waves
C Linke et al

<a id='a5725787-6577-48ba-a8d2-77f6f2825e43'></a>

12

34. Jorgensen, P. & Tyers, M. The fork'ed path to mitosis. Genome Biol. 1,
1022.1-1022.4 (2000).
35. Grandin, N. & Reed, S. I. Differential function and expression of Saccharomyces
cerevisiae B-type cyclins in mitosis and meiosis. Mol. Cell. Biol. 13, 2113-2125 (1993).
36. Barberis, M., Todd, R. G. & van der Zee, L. Advances and challenges in logical
modeling of cell cycle regulation: perspective for multi-scale, integrative yeast
cell models. FEMS Yeast Res. 17, 1-15 (2017).
37. Alon, U. Network motifs: theory and experimental approaches. Nat. Rev. Genet. 8,
450-461 (2007).
38. Le, D. H. & Kwon, Y. K. A coherent feedforward loop design principle to sustain
robustness of biological networks. Bioinformatics 29, 630-637 (2013).
39. Goldbeter, A. & Koshland, D. E. Jr Ultrasensitivity in biochemical systems con-
trolled by covalent modification. Interplay between zero-order and multistep
effects. J. Biol. Chem 259, 14441-14447 (1984).

<a id='a24008eb-b6c9-4c66-857b-07187cbd7806'></a>

40. Holt, L. J. et al. Global analysis of Cdk1 substrate phosphorylation sites provides insights into evolution. *Science* **325**, 1682–1686 (2009).

<a id='04734aca-cf70-476d-b42b-12022effba82'></a>

CC BY
This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/

<a id='9699b68f-099c-4b36-8cc7-44e2aba7fdf8'></a>

© The Author(s) 2017

<a id='57351312-1b71-4e28-8e90-11db1bd12b4c'></a>

Supplementary Information accompanies the paper on the _npj Systems Biology and Applications_ website (doi:10.1038/s41540-017-0008-1).

<a id='641b4868-8877-4002-be90-7d635a21ca9c'></a>

npj Systems Biology and Applications (2017) 7

<a id='7199586a-6f81-4d06-80b3-b6d0bdca374e'></a>

Published in partnership with the Systems Biology Institute

# Supplementary materials

<a id='4a0ee581-1ebf-4253-b475-bee101b2c5a0'></a>

Barberis M. et al.

<a id='e0f40cef-ea3e-45d4-90aa-361dfc0b74b9'></a>

Supplementary Information

<a id='cd649af0-fdbf-4536-b644-63911b05ef9c'></a>

A Clb/Cdk1-mediated regulation of Fkh2 synchronizes _CLB_ expression in

<a id='b0a06fff-2d9d-4f5f-8aa9-a9838a85e524'></a>

the budding yeast cell cycle

<a id='3eff52f0-655e-43dc-9304-c285672364ae'></a>

Christian Linke, Anastasia Chasapi, Alberto Gonz&aacute;lez-Novo, Istabrak Al Sawad,
Silvia Tognetti, Edda Klipp, Mart Loog, Sylvia Krobitsch, Francesc Posas, Ioannis Xenarios,
Matteo Barberis

<a id='92865d42-fb82-4192-a7eb-d1de6360ab90'></a>

Correspondence: M Barberis (M.Barberis@uva.nl)

<a id='afcfdac3-bc60-4302-a7e2-e8847f530878'></a>

- 1 -

<!-- PAGE BREAK -->

<a id='7ffb8a5e-1a69-4882-84eb-76172424a288'></a>

Barberis M. et al.

<a id='5c0bbe9b-bbac-4e06-9197-4757bb7072e8'></a>

**Supplementary Text**

<a id='e2af4cc0-05dc-41d3-a795-d0cd16cf4f90'></a>

**Ordinary differential equations (ODEs) describing the dynamics of Clb/Cdk1 activation**

The kinetic model presented is based on a previously published model by Barberis and colleagues.1
The biochemical reactions of the network shown in Figure 1a are implemented by mass action
kinetics, which describe the condensed and highly simplified transcriptional regulation processes
considered. The equations are listed in the below:

<a id='ebc67a61-4825-40bf-bdb8-5ba512cd5944'></a>

$$\frac{d[Sic 1]}{dt} = -k_2[Sic 1]\times[Cdk 1-Clb 5,6] + k_3[Cdk 1-Clb 5,6-Sic 1] - k_{11}[Sic 1]\times[Cdk 1-Clb 1,2] + k_{12}[Cdk 1-Clb 1,2-Sic 1] - k_{15}[Sic 1]\times[Cdk 1-Clb 3,4] + k_{16}[Cdk 1-Clb 3,4-Sic 1] - k_{26}[Sic 1]$$

$$\frac{d[Cdk 1-Clb 5,6]}{dt} = k_1 - k_2[Sic 1]\times[Cdk 1-Clb 5,6] + k_3[Cdk 1-Clb 5,6-Sic 1] + k_5[Cdk 1-Clb 5,6-Sic 1]\times\dot{i}(1+[Cdk 1-Clb 5,6]+[Cdk 1-Clb 3,4]+[Cdk 1-Clb 1,2]) + \dot{i}$$

$$-k_6[Cdk 1-Clb 5,6]$$

$$\frac{d[Cdk 1-Clb 5,6-Sic 1]}{dt} = k_2[Sic 1]\times[Cdk 1-Clb 5,6] - k_3[Cdk 1-Clb 5,6-Sic 1] - k_5[Cdk 1-Clb 5,6-Sic 1]\times\dot{i}(1+[Cdk 1-Clb 5,6]+[Cdk 1-Clb 3,4]+[Cdk 1-Clb 1,2]) + \dot{i}$$

$$-k_4[Cdk 1-Clb 5,6-Sic 1]$$

$$\frac{d[Sic 1 \otimes re5]}{dt} = k_5[Cdk 1-Clb 5,6-Sic 1]\times\dot{i}(1+[Cdk 1-Clb 5,6]+[Cdk 1-Clb 3,4]+[Cdk 1-Clb 1,2])\dot{i}$$

$$\frac{d[Clb 5,6 \otimes]}{dt} = k_4[Cdk 1-Clb 5,6-Sic 1] + k_6[Cdk 1-Clb 5,6]$$

$$\frac{d[Cdk 1-Clb 3,4]}{dt} = k_7(1+k_A[Cdk 1-Clb 5,6]) - k_{15}[Sic 1]\times[Cdk 1-Clb 3,4] + k_{16}[Cdk 1-Clb 3,4-Sic 1] - k_8[Cdk 1-Clb 3,4]$$

$$\frac{d[Cdk 1-Clb 3,4-Sic 1]}{dt} = k_{15}[Sic 1]\times[Cdk 1-Clb 3,4] - k_{16}[Cdk 1-Clb 3,4-Sic 1] - k_{18}[Cdk 1-Clb 3,4-Sic 1]\times\dot{i}(1+[Cdk 1-Clb 5,6]+[Cdk 1-Clb 3,4]+[Cdk 1-Clb 1,2]) + \dot{i}$$

$$-k_{17}[Cdk 1-Clb 3,4-Sic 1]$$

$$\frac{d[Sic 1 \otimes re18]}{dt} = k_{18}[Cdk 1-Clb 3,4-Sic 1]\times\dot{i}(1+[Cdk 1-Clb 5,6]+[Cdk 1-Clb 3,4]+[Cdk 1-Clb 1,2])\dot{i}$$

$$\frac{d[Clb 3,4 \otimes]}{dt} = k_{17}[Cdk 1-Clb 3,4-Sic 1] + k_8[Cdk 1-Clb 3,4]$$

$$\frac{d[Cdk 1-Clb 1,2]}{dt} = k_9(1+k_D[Cdk 1-Clb 1,2]+k_B[Cdk 1-Clb 3,4]+k_C[Cdk 1-Clb 5,6]) - k_{11}[Sic 1]\times[Cdk 1-Clb 1,2] + k_{12}[Cdk 1-Clb 1,2-Sic 1] - k_{10}[Cdk 1-Clb 1,2]$$

<a id='5e668c2f-18b3-449e-b2f2-7191f0d839db'></a>

- 2 -

<!-- PAGE BREAK -->

<a id='f989013f-b8c5-48fc-be59-a76319d8fba0'></a>

Barberis M. et al.

<a id='5655fd29-a930-4bf6-9e62-76508ed41d1b'></a>

d [Cdk 1\cdot Clb 1,2\cdot Sic 1] / dt = k 11 [Sic 1] \times [Cdk 1\cdot Clb 1,2] - k 12 [Cdk 1\cdot Clb 1,2\cdot Sic 1] - k 14 [Cdk 1\cdot Clb 1,2\cdot Sic 1] \times (1 + [Cdk 1\cdot Clb 5,6] + [Cdk 1\cdot Clb 3,4] + [Cdk 1\cdot Clb 1,2]) + \dot{i}

<a id='fa4512e0-8931-48f9-83c9-c0cb8f7a45bf'></a>

-k 13 [Cdk 1·Clb 1,2·Sic 1]

<a id='c647c822-094c-4c3d-829e-1cfc9ff745ff'></a>

$$\frac{d[Sic\ 1\ \otimes\ re14]}{dt} = k_{14}[Cdk\ 1\ \cdot\ Clb\ 1,2\ \cdot\ Sic\ 1] \times (1 + [Cdk\ 1\ \cdot\ Clb\ 5,6] + [Cdk\ 1\ \cdot\ Clb\ 3,4] + [Cdk\ 1\ \cdot\ Clb\ 1,2])\ \text{¿}$$

<a id='a0cf508c-1db1-4b52-9152-c3e6da34e7e0'></a>

d[Clb 1,2 ⊗]/dt = k_13 [Cdk 1 · Clb 1,2 · Sic 1] + k_10 [Cdk 1 · Clb 1,2]

<a id='9c4214cd-47db-47a5-8b2a-b5aa04f7d1c7'></a>

**Kinetic parameters describing the dynamics of Clb/Cdk1 activation**
Kinetic parameters of the network shown in Figure 1a  are listed in the following. Sicl initial concentration is set to 5 in all simulations, whereas initial concentration of other components is set to zero. Concentrations are given in dimensionless units, and rate constants are given in time  .

<a id='a98d5d71-f3ca-49bf-9a07-cd8640c56f13'></a>

<table id="2-1">
<tr><td id="2-2">Parameter</td><td id="2-3">Description of process</td><td id="2-4">Parameter</td><td id="2-5">Description of process</td></tr>
<tr><td id="2-6">k1 = 0.1</td><td id="2-7">Cdk1-Clb5,6 production</td><td id="2-8" rowspan="2">kA = 100</td><td id="2-9" rowspan="2">CLB3,4 transcription regulated by Cdk1-Clb5,6</td></tr>
<tr><td id="2-a">k2 = 5</td><td id="2-b">Sic1 binding to Cdk1-Clb5,6</td></tr>
<tr><td id="2-c">k3 = 0.5</td><td id="2-d">Cdk1-Clb5,6-Sic1 dissociation</td><td id="2-e" rowspan="2">kB = 1000</td><td id="2-f" rowspan="2">CLB1,2 transcription regulated by Cdk1-Clb3,4</td></tr>
<tr><td id="2-g">k4 = 0.01</td><td id="2-h">Clb5,6 degradation (ternary)</td></tr>
<tr><td id="2-i">k5 = 0.05</td><td id="2-j">Sic1 degradation (Clb-regulated)</td><td id="2-k" rowspan="2">kC = 100</td><td id="2-l" rowspan="2">CLB1,2 transcription regulated by Cdk1-Clb5,6</td></tr>
<tr><td id="2-m">k6 = 0.7</td><td id="2-n">Clb5,6 degradation (binary)</td></tr>
<tr><td id="2-o">k7 = 0.01</td><td id="2-p">Cdk1-Clb3,4 production</td><td id="2-q" rowspan="2">kD = 100</td><td id="2-r" rowspan="2">CLB1,2 transcription regulated by Cdk1-Clb1,2</td></tr>
<tr><td id="2-s">k8 = 0.7</td><td id="2-t">Clb3,4 degradation (binary)</td></tr>
<tr><td id="2-u">k9 = 0.001</td><td id="2-v">Cdk1-Clb1,2 production</td><td id="2-w"></td><td id="2-x"></td></tr>
<tr><td id="2-y">k10=0.7</td><td id="2-z">Clb1,2 degradation (binary)</td><td id="2-A"></td><td id="2-B"></td></tr>
<tr><td id="2-C">kl1=5</td><td id="2-D">Sic1 binding to Cdk1-Clb1,2</td><td id="2-E"></td><td id="2-F"></td></tr>
<tr><td id="2-G">k12=0.5</td><td id="2-H">Cdk1-Clb1,2-Sic1 dissociation</td><td id="2-I"></td><td id="2-J"></td></tr>
<tr><td id="2-K">k13 = 0.01</td><td id="2-L">Clb1,2 degradation (ternary)</td><td id="2-M"></td><td id="2-N"></td></tr>
<tr><td id="2-O">k14=0.05</td><td id="2-P">Sic1 degradation (Clb-regulated)</td><td id="2-Q"></td><td id="2-R"></td></tr>
<tr><td id="2-S">k15=5</td><td id="2-T">Sic1 binding to Cdk1-Clb3,4</td><td id="2-U"></td><td id="2-V"></td></tr>
<tr><td id="2-W">k16=0.5</td><td id="2-X">Cdk1-Clb3,4-Sic1 dissociation</td><td id="2-Y"></td><td id="2-Z"></td></tr>
<tr><td id="2-10">k17=0.01</td><td id="2-11">Clb3,4 degradation (ternary)</td><td id="2-12"></td><td id="2-13"></td></tr>
<tr><td id="2-14">k18=0.05</td><td id="2-15">Sic1 degradation (Clb-regulated)</td><td id="2-16"></td><td id="2-17"></td></tr>
<tr><td id="2-18">k26 = 0.001</td><td id="2-19">Sic1 degradation (basal)</td><td id="2-1a"></td><td id="2-1b"></td></tr>
</table>

<a id='032f1fa2-05cf-4b55-8c95-7428c678d1a0'></a>

Fkh2 is not responsible of the premature Clb5 protein accumulation

<a id='f509bb56-ea68-4440-be91-ebc867f56f97'></a>

- 3 -

<!-- PAGE BREAK -->

<a id='4705687f-8c2e-4039-97c0-6988ec0b5b66'></a>

Barberis M. et al.

<a id='17e27547-c601-4b48-ad1e-e82e3f401dbf'></a>

To investigate the potential role of Fkh2 removal on _CLB5_ transcription, _CLB5_ mRNA levels were measured in _fkh1Δ_, _fkh2Δ_ or _fkh1Δfkh2Δ_ strains after α-factor treatment by quantitative Real-Time PCR. The _fkh2Δ_ strain did not show any change in _CLB5_ mRNA levels as compared to wild type (Supplementary Figure S2f). Contrarily, a slight increase _CLB5_ mRNA levels was observed in _fkh1Δ_ as well as in _fkh1Δfkh2Δ_ mutants, as compared to wild type (Supplementary Figure S2f).
This result indicates that Fkh2 is not involved in _CLB5_ transcription. The premature accumulation of Clb5 protein observed in _fkh2Δ_ cells may be explained as follows. In absence of Fkh2, _CLB2_ transcription as well translation are reduced and less Clb2/Cdk1 kinase complex is available to activate the APC machinery², thus leading to a reduced degradation of Clb5 that can accumulate earlier as compared to wild type. Fkh1 may be involved in _CLB5_ transcription; however, further analyses are required to clarify this process.

<a id='67dc3cd5-95d2-4257-8f33-c2236b03be47'></a>

A Clb3/Cdk1-mediated positive feedback loop may be involved in *CLB3* transcription, but is
not sufficient to drive mitotic Clb waves

We employed the kinetic model presented in Figure 1a and implemented the Clb3,4/Cdk1-mediated
positive feedback loop on *CLB3,4* transcription (indicated as FL in Supplementary Figure S3).
Subsequently, we systematically compared network structures that differ for FL presence or absence,
as well as for the presence/absence of the direct regulation of Clb3/Cdk1 on *CLB2* transcription
(Figure 1a, arrow B, k<sub>B</sub>). Our analyses reveal that the presence of FL is compatible with the
occurrence of a number of waves, although not for all Clb/Cdk1 complexes. Specifically, FL may be
involved in shaping the Clb5,6/Cdk1 wave (Supplementary Figures S3o and S3p), supporting the
fact that Clb3/Cdk1, together with the other mitotic Clb1-4/Cdk1 complexes may contribute to
abolish the Clb5/Cdk1 activity by activating APC. However, FL is per se not sufficient to explain the
wave-like behaviour of Clb3,4/Cdk1, and an increase of its extent in presence of variable k<sub>B</sub> values
(Supplementary Figures S3a and S3b, Supplementary Figures S3e and S3f, Supplementary
Figures S3i and S3j) or in absence of k<sub>B</sub> (Supplementary Figures S3m and S3n) abolishes the
oscillations of all Clb/Cdk1 complexes. In an *in vivo* scenario, increasing levels of Clb3 due to a
continuous FL may be counteracted by APC rates, in order to preserve the proper temporal window in

<a id='1b1fa314-57a2-40ea-b01c-de7b93df382c'></a>

- 4 -

<!-- PAGE BREAK -->

<a id='30f67f25-cadf-4351-b76e-3dc380d148c5'></a>

Barberis M. et al.

<a id='c3b63675-8a8e-4bb4-9055-4012a11af084'></a>

which the waves of Clb cyclins are active. The simulations revealed that, when the waves are observed, Clb1,2 is not synchronized if kB is low, peaking at the same time than Clb3,4 (Supplementary Figures S3p and S3q, Supplementary Figures S3k and S3l). When the extent of kB increases, waves of cyclins begin to be successive in their maximum peaks, showing the characteristic oscillatory behaviour (Supplementary Figures S3g and S3h, Supplementary Figures S3c and S3d). Altogether, our computational analyses do not exclude that the Clb3/Cdk1-mediated positive feedback loop on Fkh2 may be involved on CLB3 transcription. However, in order to achieve the characteristic oscillatory pattern as well as separation of Clb maximum peaks, presence of the direct regulation of Clb3/Cdk1 on CLB2 transcription (kB) is required. This result supports the structure of the model presented in Figure 1a, where the positive feedback loop on CLB3 transcription may provide an additional, but not per se sufficient, mechanism to shape Clb waves.

<a id='56f8ca31-cae2-4c30-b67f-bfefdb22637f'></a>

**Fkh2 full-length interacts with Clb cyclins**

Fkh2 full-length and a truncated, C-terminal region of the protein (aa. 387–862, Fkh2387) that lacks the highly conserved FHA domain as well as of the majority of the FKH domain (**Supplementary Figure S5a**) were tested. The full-length protein showed a basal, strong auto-activation (**Supplementary Figure S5b**). However, treatment with 3-amino-1,2,4-triazole (3-AT), used to measure the relative strength of interactions, strongly reduced the auto-activation and allowed to detect the interaction of Fkh2 with a number of Clb cyclins among which Clb3 (**Supplementary Figure S5b**). Testing Fkh2 and Clb1-6 cyclins in the reverse combination did not lead to a conclusive result (**Supplementary Figure S5d**). Strikingly, Fkh2387 prevented the auto-activation, showing a clear interaction with Clb3 as well as with the other Clb cyclins (**Figure 3b**). The interactions were validated independently by a GST pull-down assay (**Supplementary Figure S5e**).

<a id='8687e53e-7f77-498f-b9e1-79a65f999243'></a>

**Fkh1/Ndd1 may be substrate of Clb/Cdk1 kinase activities**
A regulation mediated by Clb/Cdk1 complexes might occur also on Fkh1/Ndd1 (**Figure 3f**, gray
dotted lines), as we observed its interaction with some of the Clb cyclins in both Yeast-two-Hybrid
(**Supplementary Figures S6a–S6c**) and GST pull-down (**Supplementary Figure S6d**) assays.

<a id='1d6a5702-5f78-4da5-898e-57ddbf0f9e2c'></a>

- 5 -

<!-- PAGE BREAK -->

<a id='b4c3835d-0e10-447f-b11f-bdc567aecb4b'></a>

Barberis M. et al.

<a id='51c198eb-6819-4018-bf68-6bc132a4b01b'></a>

Remarkably, cooperativity between Ndd1 and Fkh1 was predicted by computational work³, and we observed this specific interaction _in vitro_ by Yeast-two-Hybrid (Supplementary Figure S7a), GST pull-down (Supplementary Figure S7b) assays, and _in vivo_ by the BiFC method (Supplementary Figure S7c). Furthermore, our data indicate that the interaction between Ndd1 and Fkh1 occurs starting from the late S to G2/M phase (Supplementary Figure S7d). Further analyses are needed to investigate (i) whether a feedback mediated by Clb/Cdk1 complexes can occur in Fkhl regulation, and (ii) how Fkh1/Ndd1 oscillation may correlate temporally with the transcriptional modulation of mitotic _CLB_ genes.

<a id='9643721d-31da-4924-9661-b9d3bd9c1cac'></a>

Prior knowledge network (PKN)-based optimization of Clb cyclin regulation
A prior knowledge network (PKN) of the interactions among four nodes encompassing the mitotic cyclins Clb5, Clb3 and Clb2, and the cyclin-dependent inhibitor Sic1was modelled, with each node assumed to represent the four cell cycle phases: Sic1 (G1), Clb5 (S), Clb3 (G2) and Clb2 (M). For the analysis of the PKN following optimization strategies were used. Initially, different versions of the PKN of Clb cyclin regulation shown in *Figure 4a* were simulated by using *GenYsis*⁴, by filtering the network interactions based on their level of confidence. However, none of the simulated models was able to reproduce the behaviour of three experimental conditions: wild type, deletion of *SIC1* and overexpression of *SIC1*, which have been shown experimentally to have definite phenotypes regarding the formation of Clb waves.¹ Specifically, wild type and *SIC1* overexpressing strains show a sequential appearance of Clb5, Clb3 and Clb2 after decrease of Sic1, and their subsequent removal from the cell when Sic1 levels increase at the end of the cell cycle. Of note, the wave-like pattern is delayed in *SIC1* overexpression. The alternating appearance/removal of activators (Clb cyclins) and inhibitor (Sic1) guarantees the overall cyclic behavior. Conversely, cyclin waves are abolished in a *sic1Δ* strain, with Clb levels reaching different plateau; in Boolean terms, this condition would be represented by the steady state, with Sic1 equal to 0, and all Clb cyclins equal to 1. In all simulations, Sic1 was constantly activated, suppressing the appearance of all Clb cyclins. For this reason, the optimization was subsequently conducted systematically, by assessing whether a network - similar to the PKN - reproducing the expected phenotypes of the three aforementioned experimental conditions

<a id='7023eb73-bae7-4310-92ef-bae1c775c3d4'></a>

- 6 -

<!-- PAGE BREAK -->

<a id='88b36753-60e9-4837-95b1-23fbf9a61f03'></a>

Barberis M. et al.

<a id='e1b8eff2-cbf7-418a-bc5d-dd11d67fc825'></a>

can be found. For this, two parallel strategies were followed: (a) reducing the network complexity, and (b) adding interactions potentially missing to the PKN. In the first case, i.e., the network reduction, a genetic algorithm was employed starting from the initial PKN network, in order to test the existence of a reduced model that satisfies the phenotypes of the three aforementioned experimental conditions. The genetic algorithm³ requires a set of interactions that is used as a pool from which the model can be constructed. Additionally, a set of parameters is provided in order to optimize the network; this set corresponds to parameters values that generate (i) an attractor with all nodes oscillating in wild type and *SIC1* overexpression, and (ii) a steady state with all Clb cyclins ON in a *SIC1* deletion. After several iterations of the algorithm, no model solution was found, based on the given interactions, that fully satisfies the outcome of the three experimental conditions. In the second case, i.e., the addition of regulations potentially missing to the PKN, the inverse approach was employed. First, the collection of all possible edges of the system was identified, referred to as edge pool. The edge pool included all possible interactions involving one, two, three or four nodes acting as co-regulators (for example, A→B, A&C→B, A&C&D→B, A&B&C&D→B). The interactions include activations (→), inhibitions (⊣), and NOT (^) (for example ^A→B). For the network of four nodes (Sic1, Clb5, Clb3 and Clb2), the edge pool contains a total of 640 edges. Subsequently, all PKN+1 networks were constructed by adding one edge from the edge pool (a list of all possible interactions involving Clb5, Clb3, Clb2 and Sic1 was created, as well as an equal number of models; each model consists of the initial PKN plus one interaction of the aforementioned list, i.e., PKN+1), in order to investigate whether the phenotypes observed experimentally would derive from missing interaction(s). After the analyses, none of the simulated networks satisfies the outcome of the three experimental conditions.

<a id='26a0c552-d77f-450c-bbf8-9088e4e4a8c8'></a>

Edge filtering analysis for selection of minimal model(s) of Clb cyclin regulation

Considering that all nodes of the network are expected to oscillate, a rule was specified that each node should have an incoming edge that leads to its activation; therefore, a minimal model should have at least four edges, one for the regulation of each node. Furthermore, auto-regulations were not allowed, as they would isolate the auto-regulated node from the system being the only incoming edge for that

<a id='2f19d997-61d5-41f3-a785-492d7466e8aa'></a>

- 7-

<!-- PAGE BREAK -->

<a id='22a0efa7-1206-443b-8177-b6883fe85632'></a>

Barberis M. et al.

<a id='097bbb81-52cc-4ec2-8464-85981ff9ac9b'></a>

node. Thus, the models generated should have four edges, with one input per node, and no auto-regulations. We employed a reconstruction approach, where we initially defined the collection of possible transitions; subsequently, for a given transition, the regulatory rules that would not allow a transition to happen were removed from the edge pool, by filtering the edges that are able to reproduce the attractors (wild type and *SICI* overexpression) and steady states (*sic1Δ*). Only one of the three candidate attractors resulted in an edge collection that was used to construct the minimal model candidates (attractor B in **Supplementary Figure S8b**). The edge filtering analysis to reduce the possible edge pool by including only the regulatory rules that do not contradict any of the node transitions is explained in the following. A simple example is used by considering the transition 0100→0110, which is present in one of the candidate wild type attractors (see attractor B in **Supplementary Figure S8b**). In this vector, the nodes are represented in the following order: Sic1–Clb5–Clb3–Clb2. The transition considered indicates the activation of Clb3, whereas the other nodes maintain their previous activation state. In order to investigate the modes of Clb3 activation, we will demonstrate the edge filtering procedure by testing the plausibility of four regulatory rules: Sic1→Clb3, ^Sic1→Clb3, Sic1&Clb5→Clb3, ^Sic1&Clb5→Clb3.

<a id='985e248a-27a9-48d8-a4a0-fc4be0ffec60'></a>

*Sic1→Clb3 and ^Sic1→Clb3 logical rules.* The state of Clb3 at time *t*+1 is defined by the state of its regulators at time *t*. If Sic1 is the only regulator of Clb3 (Sic1→Clb3), then Clb3 will be active (1) at time *t*+1 if and only if Sic1 is active (1) at time *t*. However, this is not true, as Sic1 state at time *t* is 0; therefore, Sic1→Clb3 can not be the logical rule regulating Clb3 and it will be removed from the edge pool. ^Sic1→Clb3 can interpreted as if the absence of Sic1 (NOT Sic1) triggers Clb3 activation, meaning that Clb3 will be active (1) at time *t*+1 if and only if Sic1 is inactive (0) at time *t*. This is true, therefore the logical rule ^Sic1→Clb3 is not removed from the edge pool.

<a id='85ccb409-dad4-4c9b-b1f5-b322a779205e'></a>

Sic1&Clb5→Clb3 and ^Sic1&Clb5→Clb3 logical rules. When examining the cases of AND (&) regulatory rules, the state of all nodes included in the regulatory rule have to be taken into account.
The regulation is effective if the state of all nodes included satisfies the logical rule. At time t, Sic1 is inactive (0) and Clb5 is active (1); in this scenario, Clb3 switches from 0 to 1 at time t+1. If both Sic1 and Clb5 participate in the regulation of Clb3, the only AND rule configuration that would trigger the activation of Clb3 is ^Sic1&Clb5→Clb3, with inactive Sic1 (0) and active Clb5 (1) at time t. This

<a id='6bd9adb4-aecb-4738-816e-9eb9c5ae5082'></a>

- 8 -

<!-- PAGE BREAK -->

<a id='f1bbbc1e-a33a-4a7b-842c-d79adc86260e'></a>

Barberis M. et al.

<a id='9ff27b2b-1e42-4597-af6b-32d7a303a358'></a>

logical rule will be maintained in the edge pool. Conversely, the logical rule Sic1&Clb5→Clb3 is not true, and it will be removed from the edge pool.

<a id='68446f4b-9b0b-4f13-9020-34fbbeca62ff'></a>

Out of all possible 640 edges, only 10 did not contradict the state transitions of the candidate attractor B, whereas the other candidate attractors could not be reached with a minimal model setting (see Table 1 for the regulatory rules specifying the minimal model edge pool), and the possible minimal models constructed were reduced to 36. In the other two cases (attractor A and attractor C), the regulatory rules that did not contradict any transition were very few and, more importantly, not all nodes were regulated being all possible incoming edges filtered out. Without all nodes being regulated, it is not possible to obtain a cyclic attractor during the simulation, thus, the attractors A and C were rejected. Subsequently, the 36 models were filtered by selecting only those that reproduced the waves of nodes during qualitative ODE simulations by using SQUAD.⁶

<a id='14704d65-32ad-4c1e-8a68-7fa3c16846c0'></a>

**Boolean model validation using continuous time Markov process**

In order to independently validate our findings, the model candidates were simulated by applying Kinetic Monte-Carlo (or Gillespie algorithm) on the Boolean state space. MaBoSS describes the behavior of heterogeneous cell population by applying continuous and discrete Markov processes on Boolean networks. This software associates transition rates to each node, computes the temporal evolution of probability distributions and estimates stationary distributions. Given some initial conditions, MaBoSS produces time trajectories, and time evolution of probabilities for each network state are estimated. Since MaBoSS describes cell population rather than single cells, the probabilities of all states converge to a constant when time tends to infinity. The Boolean feedback loops depends only on the topology of the regulations and not on transition rates or time; however, such cycles cannot be linked perfectly to periodic behavior of instantaneous probabilities that MaBoSS uses, because the set of these probabilities cannot be perfectly periodic. They can display damped oscillations, or no oscillation at all. When simulating our models, damped oscillations were observed, with the probability distributions of all network states tending to a stationary distribution (Supplementary Figure S10a). The entropy and transition entropy measurements that MaBoSS provides can be used to characterize cyclic stationary distributions. These measurements are defined

<a id='0be42184-ab42-429b-947f-149a5c340fd4'></a>

- 9 -

<!-- PAGE BREAK -->

<a id='8f099f16-0a29-4688-9636-fa4bab48c340'></a>

Barberis M. et al.

<a id='ab0a8ced-3f72-4092-9cac-1304de3199ea'></a>

in Stoll et al., 2012: "The **Entropy (H)** measures the disorder of the system. Maximum entropy means that all states have the same probability; H=0 means that one of the states has a probability of one" (i.e., steady state) and "The **Transition Entropy (TH)** characterizes the system at the level of a single trajectory. For each state S, there exists a set of possible transitions. TH(S)=0 if there is no transition from S to any other state." To identify a cyclic stationary distribution, i.e., a stationary distribution that contains a cyclic attractor, the entropy H has to be non-zero and the transition entropy TH has to be 0. This is indeed observed when simulating our networks (**Supplementary Figure S10b**). To maintain the cyclic behavior of the probabilities, MaBOSS can simulate discrete time.

**Supplementary Figure S10c** shows that the cyclic behavior of the models is clearly maintained, with a much slower decrease through time due to the stochastic events. Altogether, both continuous and discrete MaBOSS simulations validate the results obtained with GenYsis⁴ and SQUAD⁶. In the case of continuous time simulation, an attractor was retrieved with a state probability graph similar to the state transition graph obtained with GenYsis/SQUAD. In the case of discrete time simulation, probability-based that describe cell populations (instead of single cell SQUAD simulations), damped oscillation were observed where each state has similar probabilities. However, looking at the asymptotic behavior of entropy (not converging to 0) and transition entropy (converging to 0), the stationary distribution can be characterized as cyclic stationary distribution.

<a id='0ef7ade5-66bb-4286-8c7c-e491affc58f3'></a>

References for Supplementary Text

<a id='ed0b4dde-35a3-4e83-8fd2-adcebe508927'></a>

- 10 -

<!-- PAGE BREAK -->

<a id='013ab73f-2d1e-45a4-ae65-1a253b22c177'></a>

Barberis M. et al.

<a id='c3cfeecc-cd27-4f90-98e5-4bf40e5d9313'></a>

1. Barberis, M. *et al*. Sic1 plays a role in timing and oscillatory behaviour of B-type cyclins. *Biotechnol. Adv.* **30**, 108–130 (2012).
2. Wäsch, R. & Cross, F. R. APC-dependent proteolysis of the mitotic cyclin Clb2 is essential for mitotic exit. *Nature* **418**, 556–562 (2002).
3. Tsai, H. K., Lu, H. H. & Li, W. H. Statistical methods for identifying yeast cell cycle transcription factors. *Proc. Natl. Acad. Sci. USA* **102**, 13532–13537 (2005).
4. Garg, A., Di Cara, A., Xenarios, I., Mendoza, L. & De Micheli, G. Synchronous versus asynchronous modeling of gene regulatory networks. *Bioinformatics* **24**, 1917–1925 (2008).
5. Dorier, J., Crespo, I., Niknejad, A., Liechti, R., Ebeling, M. & Xenarios, I. Boolean regulatory network reconstruction using literature based knowledge with a genetic algorithm optimization method. *BMC Bioinformatics* **17**, 410.
6. Di Cara, A., Garg, A., De Micheli, G., Xenarios, I. & Mendoza, L. Dynamic simulation of regulatory networks using SQUAD. *BMC Bioinformatics* **8**, 462 (2007).
7. Stoll, G., Viara, E., Barillot, E. & Calzone, L. Continuous time Boolean modeling for biological signaling: application of Gillespie algorithm. *BMC Syst. Biol.* **6**, 116 (2012).

<a id='18b79d2c-eaee-4ce5-9717-c81060d3432b'></a>

Supplementary Figure Legends

<a id='2905ab53-0ef0-4536-ac2d-954cf531ec98'></a>

- 11-

<!-- PAGE BREAK -->

<a id='325f0dd3-3b30-49cc-944f-592f8daacd82'></a>

Barberis M. et al.

<a id='a750c204-2e50-4b1c-a039-c4a525193331'></a>

Figure S1. Kinetic model variants of Clb/Cdk1 regulation and computational time courses of total Clb cyclins levels. (a–f) Simulations of the model variants were generated starting from the network in Figure 1a by varying values of k_A (reducing or increasing of 10-fold its initial level, from 100 to 10 or to 1000) (a and b), k_B (reducing or increasing of 10-fold its initial value, from 1000 to 100 or to 10000) (c and d) and k_C (reducing or increasing of 10-fold its initial value, from 100 to 10 or to 1000) (e and f). The model variants were implemented by ordinary differential equations, with the parameters used for the simulations having the same value among all variants (see Supplemental

<a id='aeb28567-0ca6-4e17-9083-21ba45fcc612'></a>

Text for the full set of equations and parameter values¹). (g and h) Impact of transcriptional regulations on the delay between peaks of Clb cyclins. The graphs report the time delay observed between maximum levels of Clb cyclins for binary combinations between the minimal model – where Clb/Cdk1 complexes are connected via four transcriptional regulations – and two model variants, independently. (g) Time delay calculated for the left branch (only kC active) between Clb5,6 and Clb1,2 (t1,2-t5,6). (h) Time delay calculated for the right branch (only kA and kB active) between Clb5,6 and Clb1,2 (t1,2-t5,6). Each parameter of the network may vary from its selected value to the same value multiplied for a random real value comprised between 0.1 and 10, as indicated on each simulation panel.

<a id='c18ae4eb-e796-4933-b880-cb81efe95868'></a>

Figure S2. Fkhl and Fkh2 regulate dynamics of mitotic Clb cyclins in a cell cycle- dependent manner. (a) Quantitative Real-Time PCR of mitotic _CLB_ transcripts in yeast cells treated with nocodazole (NOC). Total mRNA was isolated from arrested wild type, _fkh1Δ_, _fkh2Δ_ and _fkh1Δfkh2Δ_ cells, and _CLB1_, _CLB2_, _CLB3_ and _CLB4_ mRNA levels were measured. _ACT1_ and _TSA1_ genes were used as negative controls, as they are not affected by cell cycle dynamics. Error bars on the histograms represent SDs from the mean of three independent experiments; p-values are indicated on the histograms. Nocodazole-arrested cells show that _fkh2Δ_ affects both _CLB3_ and _CLB4_ transcript accumulation, whereas _fkh1Δ_ affects _CLB4_ transcript accumulation. (b) Quantitative Real-Time PCR of mitotic _CLB_ transcripts in yeast cells treated with hydroxyurea (HU). Total mRNA was isolated

<a id='4e494020-48eb-4fcc-8e6b-e42fd76247c9'></a>

- 12 -

<!-- PAGE BREAK -->

<a id='9b058e53-de3e-4411-8761-45023b491d9e'></a>

Barberis M. et al.

<a id='4d459be8-23b5-438a-8a63-e0b8ca2a1b48'></a>

from arrested wild type, _fkh1Δ_, _fkh2Δ_ and _fkh1Δfkh2Δ_ cells, and _CLB1, CLB2, CLB3_ and _CLB4_ mRNA levels were measured. _ACT1_ and _TSA1_ genes were used as negative controls, as they are not affected by cell cycle dynamics. Error bars on the histograms represent SDs from the mean of three independent experiments; p-values are indicated on the histograms. Hydroxyurea-arrested cells show that _fkh2Δ_ affects _CLB3_ but not _CLB4_ transcript accumulation, whereas _fkh1Δ_ affects _CLB4_ transcript accumulation. **(c)** Binding of Fkh1 to mitotic _CLB_ promoter regions. Chromatin immunoprecipitation was performed by precipitating protein/DNA complexes from cells grown in exponential phase using an anti-Myc antibody. _ACT1_ and _TSA1_ genes were used as negative controls, whereas _CLB1_ and _CLB2_ genes as positive controls. Error bars on the histograms represent SDs from the mean of three independent experiments. **(d)** RNA polymerase II occupancy at mitotic _CLB_ promoters. Association of RNA polymerase II to _CLB1, CLB2, CLB3_ and _CLB4_ promoters was tested using an anti-RNA polymerase antibody. _ACT1_ and _TSA1_ genes were used as negative controls, whereas _CLB1_ and _CLB2_ genes as positive controls. Error bars on the histograms represent SDs from the mean of two independent experiments. **(e)** Cell synchrony of wild type, _fkh1Δ_ and _fkh2Δ_ strains. Yeast cells were sampled to measure DNA content by flow cytometry at the same time points analysed for the Western blot analysis. Fkh2, but not Fkh1, deletion results in a delayed cell division, as it can be observed when comparing DNA profiles of deletion and wild type strains. **(f)** Quantitative Real-Time PCR of _CLB5_ transcripts in yeast cells treated with α-factor. Total mRNA was isolated from arrested wild type, _fkh1Δ, fkh2Δ_ or _fkh1Δfkh2Δ_ cells, and _CLB5_ mRNA levels were measured. _ACT1_ and _TSA1_ genes were used as negative controls. Error bars on the histograms represent SDs from the mean of three independent experiments; p-values are not indicated on the histograms, as they are not statistically significant. α-factor-arrested cells show that Fkh1, but not Fkh2, affects _CLB5_ transcript accumulation.

<a id='5a3e7c86-9206-4400-9037-f402a91d81f0'></a>

Figure S3. Contribution of the Clb3,4-mediated positive feedback loop on the formation of Clb
waves. (a–q) Simulations of the model variants were generated starting from the network in Figure
1a by varying values of k B and FL between 0 and 1000, as shown on each simulation panel. The effect
of an increase of FL was tested in presence of variable k B values – high (k B = 1000, a–d), medium (k B

<a id='c1a9d5b9-0502-4424-a79a-0c63feac7306'></a>

- 13 -

<!-- PAGE BREAK -->

<a id='40d013f4-c1c4-4a90-bc60-91815943afec'></a>

Barberis M. et al.

<a id='36e01e7c-fdfd-4944-968c-ac7674efd9e8'></a>

= 100, **e-h**) or low (*k*B = 10, **i-l**) -- or in absence of *k*B (*k*B = 0, **m-q**). Computational time courses of total Clb cyclins levels are shown. The model variants were implemented by ordinary differential equations, as described in **Supplementary Figure S1**.

<a id='95b89f35-c1aa-43c3-a6cc-91b09cbec51a'></a>

Figure S4. Time course analysis of the association between Ndd1 and Fkh2. (a) Haploid yeast cells expressing the C-terminal region of the Venus protein fused to the C-terminal region of Ndd1 (Ndd1-VC) were transformed with the p426 plasmid carrying the N-terminal region of the Venus protein fused to the C-terminal region of Fkh2 (VN-Fkh2) under the control of the constitutive GPD promoter. Detection of the fluorescent signal by Bimolecular Fluorescence Complementation (BiFC) as well as DAPI stained nuclei was revealed by fluorescence microscopy. (b) Cells co-expressing Ndd1-VC and VN-Fkh2 were synchronized in G1 phase with a-factor, and the presence of a fluorescent signal, also called BiFC signal (identified as yellow bright spots, clearly distinguishable from the fluorescence background of yeast cells) was monitored. Arrested cells were released into fresh media and samples were collected every 10 min. DNA content of samples was determined by staining with propidium iodide and FACS analysis. Absence of the BiFC signal is observed in early G1 phase (0–10 min). The BiFC signal indicating an interaction between Fkh2 and Ndd1 is observed starting from late G1 phase (10–20 min), in agreement with Fkh2 phosphorylation being detectable 10 to 20 min after a-factor release2, until G2/M phase (70 min), supporting the view that Fkh2 is active in this temporal window.3 The BiFC signals decrease progressively in late mitosis (80 – 90 min), when the cells prepare to start a new round of cell division.

<a id='42a718b2-49b1-48b4-bdb4-4814b28ca9fb'></a>

Figure S5. Association of Fkh2 and Ndd1 with Clb cyclins. (a) Schematic representation of full-length Fkh1 and Fkh2 and a series of deletion constructs used in this study. The locations of the Forkhead domain (FKH) and Forkhead associated domain (FHA) are indicated. (b–d and f) Fkh2 and Ndd1 associate with Clb cyclins by GST pull-down assay. Yeast cells expressing the fusion proteins LexA-Fkh2 (pBTM-Fkh2) and AD-Clb1-6 (pACT-Clb1-6) (b), LexA-Fkh2458 (pBTM-Fkh2458) and AD-Clb1-6 (pACT-Clb1-6) (c), LexA-Clb1-6 (pBTM-Clb1-6) and AD-Fkh2 (pACT-Fkh2) (d), and LexA-Clb1-6 (pBTM-Clb1-6) and AD-Ndd1 (pACT-Ndd1) (f) were spotted onto SDII and SDIV

<a id='ddaee314-0c55-426f-9780-ea5092d5e634'></a>

- 14 -

<!-- PAGE BREAK -->

<a id='d9642447-653e-4278-8671-080f366aec0c'></a>

Barberis M. et al.

<a id='037517ee-0500-4d62-b6cc-2615733b36e1'></a>

selective media or on a membrane for detection of the -galactosidase activity. 3-amino-1,2,4-triazole
(3-AT) was used to measure the relative strength of interactions, and its concentration is indicated for
each assay. (b) Yeast cells expressing fusion proteins LexA-Fkh2 (pBTM-Fkh2) and AD-Clb1-6
(pACT-Clb1-6) were able to growth on selective SDIV medium. As expected, no growth of yeast
expressing control proteins LexA (pBTM) and AD (pACT), or LexA (pBTM) and AD-Clb1-6
(pACT-Clb1-6), negative controls in the assay, was observed on SDIV. Although growth of yeast
cells on this medium was observed for a potential interaction of Fkh2 with all mitotic Clb cyclins, this
is also the case for the expression of the LexA-Fkh2 negative control per se, indicating auto-
activation of reporter genes, as previously observed. To decrease the non-specific growth observed
for LexA-Fkh2, as well as to investigate the relative strength of interactions, 3-amino-1,2,4-triazole
(3'AT) was added to the media. Yeast cells expressing fusion proteins LexA-Fkh2 and all AD-Clb
cyclins are able to grow on selective 3'AT medium, however, LexA-Fkh2 still shows a basal auto-
activation, leaving an uncertainty about the veridity of Fkh2/Clb interactions. (c) Yeast cells
expressing fusion proteins LexA-Fkh2458 (pBTM-Fkh2458) and AD-Clb1-6 (pACT-Clb1-6) were able
to growth on selective SDIV medium. As expected, no growth of yeast expressing the negative
controls was observed on SDIV. Growth of yeast cells on this medium was observed in
correspondence of the potential interaction of Fkh2 with all mitotic Clb cyclins. (d) Testing Fkh2 and
Clb1-6 in the reverse combination, by using LexA-Clb1-6 (pBTM-Clb1-6) and AD-Fkh2 (pACT-
Fkh2) also did not lead to a conclusive result, as some of the negative control show auto-activation of
reporter genes and the use of 3'AT abolishes the majority of the potential Fkh2/Clb interactions. (f)
Only yeast cells co-expressing fusion proteins LexA-Clb2 (pBTM-Clb2) or LexA-Clb3 (pBTM-Clb3)
and AD-Ndd1 (pACT-Ndd1) were able to grow on selective SDIV media. No growth of yeast
expressing negative control proteins (pBTM and pACT, or pBTM-Clb1,5,6 not conclusive for
pBTM-Clb4 and PACT, or pBTM and PACT-Ndd1) was observed on SDIV medium after 3'AT
was added, with the exception of the co-expression of pBTM-Clb4 and pACT. The interaction
between the C-terminal domain of human ATXN2, ATXN2-FD, and the C-terminal domain of human
PABP, PABC, was used as positive control. At least three independent transformations have been
performed and four clones were tested in each experiment. (e and g) Fkh2 and Ndd1 associate with

<a id='5b106b90-1e3d-4904-bb5e-629aac7165ee'></a>

- 15 -

<!-- PAGE BREAK -->

<a id='1eaf8cc7-f34f-44f3-b0d0-508d1e48727c'></a>

Barberis M. et al.

<a id='ef2761a3-a7a5-4aef-80c4-bf71a5836cb1'></a>

Clb cyclins by GST pull-down assay. Bacterial expressed proteins GST and GST-Clb1-6 were immobilized on Glutathione Sepharose beads and incubated with lysate from yeast cells expressing Myc-tagged Fkh2 (e) or Myc-tagged Ndd1 (g) from their endogenous promoters. Fkh2-Myc or Ndd1-Myc lysates served as a loading controls (lanes 1). Sepharose beads (lanes 2) and immobilized GST (lanes 3) were used as negative controls. Precipitation of Fkh2-Myc or Ndd1-Myc bound on GST-Clb1-6 (lanes 4-9) was detected with rabbit α-Myc antibody. The loading controls for GST-Clb1-6 are shown at the bottom of **Supplementary Figure S5e**. All assays have been performed three times, and one representative is shown. (h) Quantitative Real-Time PCR of mitotic *CLB* transcripts in yeast cells treated with nocodazole. Total mRNA was isolated from arrested wild type, *fkh2Δ*, *clb3Δclb4Δ* or *clb5Δclb6Δ* cells, and *CLB2* and *CLB3* mRNA levels were measured. *ACT1* and *TSA1* genes were used as negative controls, as they are not affected by cell cycle dynamics. Error bars on the histograms represent SDs from the mean of three independent experiments; p-values are indicated on the histograms. Nocodazole-arrested cells show that *clb3Δclb4Δ* affects *CLB2* transcript accumulation, whereas *clb5Δclb6Δ* affects both *CLB2* and *CLB3* transcript accumulation.

<a id='1c8e3ec1-3d72-4d47-bbec-39226df043a1'></a>

Figure S6. Association of Fkh1 with Clb cyclins. (a–c) For the Yeast-two-Hybrid assay, yeast cells expressing the fusion proteins LexA-Fkh1 (pBTM-Fkh1) and AD-Clb1-6 (pACT-Clb1-6) (a), LexA-Clb1-6 (pBTM-Clb1-6) and AD-Fkh1 (pACT-Fkh1) (b), and LexA-Fkh1360 (pBTM- Fkh1360) and AD-Clb1-6 (pACT-Clb1-6) (c) were spotted onto SDII and SDIV selective media or on a membrane for detection of the β-galactosidase activity. 3-amino-1,2,4-triazole (3-AT) was used to measure the relative strength of interactions, and its concentration is indicated for each assay. (c) A truncated, C-terminal region of Fkh1 (aa. 360–484, Fkh1360) that lacks the Forkhead associated domain (FHA, aa. 76–162) as well as the majority of the Forkhead domain (FKH, aa. 301–391), is able to interact specifically with Clb2. The interaction between the C-terminal domain of human ATXN2, ATXN2-FD, and the C-terminal domain of human PABP, PABC, was used as positive control. At least three independent transformations have been performed and four clones were tested in each experiment. (d) For the GST pull-down assay, bacterial expressed proteins GST and GST-Clb1-6 were immobilized on Glutathine Sepharose beads and incubated with lysate from yeast cells expressing Myc-tagged

<a id='865411d1-c736-4d59-b3ae-ee52cde96f9e'></a>

- 16 -

<!-- PAGE BREAK -->

<a id='8406395f-268d-4fb6-8bf0-ac6718a0e730'></a>

Barberis M. et al.

<a id='351c2867-4e1b-488a-abf8-f8086b957724'></a>

Fkh1 from its endogenous promoter. Fkh1-Myc lysate served as a loading control (lane 1). Sepharose beads (lane 2) and immobilized GST (lane 3) were used as negative controls. Precipitation of Fkh1- Myc bound on GST-Clb1-6 (lanes 4-9) was detected with rabbit α-Myc antibody. The loading controls for GST-Clb1-6 are shown at the bottom of **Supplementary Figure S5e**. All assays have been performed three times, and one representative is shown.

<a id='a32eae9f-a7b4-4c42-af35-00f179f961fb'></a>

Figure S7. Ndd1 interacts with both Fkh1 and Fkh2 in vitro and in vivo. (a) Ndd1 associates with Fkh1 and Fkh2 by Yeast-two-Hybrid assay. Yeast cells expressing the fusion proteins LexA-Fkh1 and LexA-Fkh2 (pBTM-Fkh1 and pBTM-Fkh2) and AD-Ndd1 (pACT-Ndd1) were spotted onto SDII and SDIV selective media or on a membrane for detection of the β-galactosidase activity. 10 mM 3-amino-1,2,4-triazole (3-AT) was used to measure the relative strength of interactions. The interaction between ATXN2-FD and PABC was used as positive control. At least three independent transformations have been performed and four clones were tested in each experiment. (b) Ndd1 associates with Fkh1 and Fkh2 by GST pull-down assay. Bacterial expressed proteins GST, GST-Fkh1 and GST-Fkh2 were immobilized on Glutathione Sepharose beads and incubated with lysate from yeast cells expressing Myc-tagged Ndd1 from its endogenous promoter. Ndd1-Myc lysate served as a loading control (lane 1). Sepharose beads (lane 2) and immobilized GST (lane 3) were used as negative controls. Precipitation of Ndd1-Myc bound on GST-Fkh1 and on GST-Fkh2 (lanes 4-5) was detected with rabbit α-Myc antibody. The loading controls for GST-Fkh1-2 are shown at the bottom of the panel. All assays have been performed three times, and one representative is shown. (c and d) Ndd1 associates with Fkh1 and Fkh2 by Bimolecular Fluorescent Complementation (BiFC). (c) Haploid yeast cells expressing the C-terminal region of the Venus protein fused to the C-terminal region of Ndd1 (Ndd1-VC) were transformed with the p426 plasmid carrying the N-terminal region of the Venus protein fused to the C-terminal region of Fkh2 (VN-Fkh2) or Fkh1 (VN-Fkh1), respectively. Cells transformed with the plasmid p426-VN were used as control (top panel). Detection of the fluorescent (BiFC) signal as well as DAPI stained nuclei was revealed by fluorescence microscopy. The BiFC signal was observed for both Ndd1/Fkh2 (mid panel) and Ndd1/Fkh1 (bottom panel) pairs, highlighting a nuclear localization of the fluorescent signal. (d) Time course analysis of

<a id='b81ca2ba-10d8-430b-b00a-8c397fcd85a3'></a>

- 17 -

<!-- PAGE BREAK -->

<a id='32ec6741-c49b-4d34-8bcc-0f09a8bfb817'></a>

Barberis M. et al.

<a id='1fb52215-ea40-4b7e-8126-15b711bb4c01'></a>

the association between Ndd1 and Fkh1. Yeast cells co-expressing Venus fusion proteins Ndd1-VC and VN-Fkh1 were synchronized in G1 phase with α-factor, and the presence of the BiFC signal was monitored. Arrested cells were released into fresh media and samples were collected every 10 min. DNA content of samples was determined by staining with propidium iodide and FACS analysis. Absence of the BiFC signal was observed from G1 to mid-S phase (0 – 30 min), whereas its presence indicating an interaction between Fkh1 and Ndd1 was observed starting from late-S to G2/M phase (40 – 70 min), supporting the view of Fkh1 being present in this temporal window.³ The BiFC signals decrease progressively in late mitosis (80 – 90 min), when the cells prepare to start a new round of cell division.

<a id='83871509-2a40-43a6-a1b1-f5568f19e7b6'></a>

Figure S8. Expected oscillations in the Clb cyclin network and Boolean attractor candidates. (a) Qualitative representation of expression waves for Sic1 (black), Clb5 (red), Clb3 (blue) and Clb2 (green) in wild type cells (upper panel). Clb cyclins appear and disappear sequentially, one after the other one, alternating their presence with Sic1 oscillations. The "Booleanized" version of the expression waves (bottom panel) allows to retrieve the Boolean attractor by setting activity thresholds. Each state between any activity transition is translated into a Boolean vector. (b) Attractor candidates (A, B, C) expected for wild type, with Sic1, Clb5, Clb3 and Clb2 displaying alternating oscillatory states. (c) Attractor candidates (A, B, C) expected for _SIC1_ overexpression, with Clb5, Clb3 and Clb2 displaying alternating oscillatory states. As compared to wild type, the state of Sic1 is constantly set to 1 to mimic its overexpression. (d) Attractor candidate (A) expected for _sic1Δ_, with Clb5, Clb3 and Clb2 displaying steady states (Boolean value equal to 1). As compared to wild type, the state of Sic1 is constantly set to 0 to mimic its deletion.

<a id='d91124e1-e8e6-47d6-a8b7-7292a411a66e'></a>

Figure S9. Minimal candidate models reproducing experimental Clb and Sic1 waves. (a) Six minimal models that satisfy the known experimental conditions (wild type, *SIC1* overexpression and *sic1*Δ) by both Boolean simulations (GenYsis) and standardized ordinary differential equation (ODE) simulations (SQUAD). Arrows and circles denote activations and inhibitions, respectively. A number of interactions appear in more than one model, with Sic1&Clb2---Clb5 being the only interaction in

<a id='b77a9fee-d20b-499c-8ebe-4bb29cd4100b'></a>

- 18 -

<!-- PAGE BREAK -->

<a id='67e0c9c3-b725-4251-857e-b627416758f7'></a>

Barberis M. et al.

<a id='0eebc1a0-1ad9-46cd-b883-e71dc4137f71'></a>

common among all models. (b and d-f) SQUAD simulations of the simplest minimal model candidate (model 1) (b), the minimal model 2 (d) and the minimal model 3 (e). From top to bottom are plotted simulations of wild type (upper panel), _SIC1_ overexpression (mid panel) and _sic1_Δ (bottom panel). It shall be noted that by the computational time t=15 wild type cells have entered the fourth cycle, whereas _SIC1_ overexpressed cells show a delay as compared to wild type, having just completed the third cycle. The results are in agreement with the experimental observations¹. (c) Boolean wild type attractor (B) for the simplest minimal model candidate (model 1). (f) SQUAD simulations of _CLB2_ overexpression experiments for the minimal model 3. From top to bottom are plotted simulations of an increase dosage of Clb2: 1 (upper panel), 5 (mid panel) and 30 (bottom panel). The insert in the bottom panel represents a magnification of Sic1, Clb5 and Clb3 oscillations when Clb2 is set to 30. It shall be noted that by the computational time t=15 the cycles are progressively reduced when increasing the Clb2 level. The results are in agreement with the experimental observations.⁵

<a id='777cff9c-a42c-441f-88cf-09cd6b8a85bb'></a>

Figure S10. Validation of Boolean models output by continuous time Markov process. (a) Standard continuous Markov process simulation applying a Kinetic Monte-Carlo (or Gillespie algorithm) approach by using MaBoSS. The probability distributions for network states tend to stationary distribution; however, the sequence of states retrieved during the first cell cycle corresponds to the wild type attractor obtained with GenYsis and SQUAD. (b) Entropy (H) and transition entropy (TH) distributions. The network simulation results in H being non-zero and TH being roughly 0, and indicates that the stationary distribution shown in panel A contains a cyclic attractor. (c) Discrete time simulation using MaBoSS. The cyclic behavior of the network can be clearly observed, despite the state probabilities reduce with time. The colour legend corresponds to the one used in panel A.

<a id='65c98921-b248-47fd-86a5-741eec21a414'></a>

- 19 -

<!-- PAGE BREAK -->

<a id='9f8c54ad-a61e-4e97-995f-05c82605622f'></a>

Barberis M. et al.

<a id='bb88d070-ed52-4375-8123-3b78c5d203ec'></a>

References for Supplementary Figure Legends

<a id='b6ffc180-42c4-4c62-bdee-4becfe528c19'></a>

1. Barberis, M. et al. Sic1 plays a role in timing and oscillatory behaviour of B-type cyclins. *Biotechnol. Adv.* **30**, 108–130 (2012).
2. Pic-Taylor, A., Darieva, Z., Morgan, B. A. & Sharrocks, A. D. Regulation of cell cycle-specific gene expression through cyclin-dependent kinase-mediated phosphorylation of the forkhead transcription factor Fkh2p. *Mol. Cell. Biol.* **24**, 10036–10046 (2004).
3. Simon, I. et al. Serial regulation of transcriptional regulators in the yeast cell cycle. *Cell* **106**, 697–708 (2001).
4. Linke, C., Klipp, E., Lehrach, H., Barberis, M. & Krobitsch, S. Fkh1 and Fkh2 associate with Sir2 to control CLB2 transcription under normal and oxidative stress conditions. *Front. Physiol.* **4**, 173 (2013).
5. Cross, F. R., Schroeder, L., Kruse, M. & Chen, K. C. Quantitative characterization of a mitotic cyclin threshold regulating exit from mitosis. *Mol. Biol. Cell.* **16**, 2129–2138 (2005).

<a id='b6b82689-ff1f-464e-ba79-e50bb932ba5b'></a>

- 20 -

<!-- PAGE BREAK -->

<a id='734367f6-e548-4482-bbb5-adad4ceb9668'></a>

Barberis M. et al.

<a id='c658c35c-944c-486d-905e-a402244e1e37'></a>

**Supplementary Materials and Methods**

<a id='b3471889-e2e4-42c2-8adf-d7e6d579bd9d'></a>

Yeast strains

Yeast strains BY4741 (_MATa his3Δ1 leu2Δ0 met15Δ0 ura3Δ0_) and L40ccua (_MATa his3-200 trp1-901 leu2-3,112 LYS2::(lexAop)4-HIS3 ura3::(lexAop)8-lacZ ADE2::(lexAop)8-URA3 gal80 canR cyh2R_) were used to generate the variant strains used in this study (see **Supplementary Table S1**).

Generally, a one-step PCR-mediated gene targeting procedure was carried out for genetic manipulations.¹ To generate the respective gene deletion strains, the plasmid pUG6 (accession number P30114, Euroscarf) was used as template to amplify a gene-specific loxP-flanked G418 cassette. Then, the amplified DNA cassette was used for transformation.¹ After selection of transformants and verification of the correct chromosomal integration of the loxP-flanked cassette, a yeast clone was transformed with the plasmid pSH47 (accession number P30119, Euroscarf) to express Cre-recombinase for excision of the integrated gene-specific loxP-flanked cassette. Subsequently, transformants were incubated on selective medium containing 1 mg/ml 5-fluoroorotic acid (Zymo Research), and grown yeast clones were analysed for uracil auxotrophy. To generate double gene deletions, a second integration cassette was amplified using plasmid pUG6 as template and used to transform the corresponding deletion strains, and processed as described above. To express Myc-tagged Fkh1, Fkh2 and Ndd1 in yeast, the plasmid pYM18 containing a 9-_MYC_ sequence (accession number P30304, Euroscarf) was used as template for the amplification of the respective gene-specific integration cassettes. To perform time course experiments three isogenic BY4741 derivative strains were used, YAN49 (_CLB3-TAP:HIS3, SIC1-TAP:KanMX::Nat, CLB2-18MycKl:KanMx::URA3, CLB5-6HA:KanMx_), generated by tagging one of each of Clb pairs along with Sic1, and two variants, YAG20 (_CLB3-TAP:HIS3, SIC1-TAP:KanMX::Nat, CLB2-18MycKl:KanMx::URA3, CLB5-6HA:KanMx, fkh1::HPH_) and YAG21 (_CLB3-TAP:HIS3, SIC1-TAP:KanMX::Nat, CLB2-18MycKl:KanMx::URA3, CLB5-6HA:KanMx, fkh2::HPH_), obtained by inserting a cassette containing the Hygromycin B kinase gene (_HPH_) to disrupt _FKH1_ and _FKH2_ genes, respectively (see **Supplementary Table S1**). To perform in vivo phosphorylation assays six

<a id='ac193f62-cb20-4bc7-b5f7-06ea5f47b923'></a>

- 21 -

<!-- PAGE BREAK -->

<a id='d190199d-4a77-4bee-b69d-0686b2d3de71'></a>

Barberis M. et al.

<a id='b1584266-97ba-4ef9-817a-71f80c9b37e0'></a>

isogenic BY4741 derivative strains were used, YAG135 (FKH2-6HA-hphNTI, bar1::LEU2), YST44 (FKH2-6HA-hph, bar1::LEU2, clb3::TRP1), YST45 (FKH2-6H-hph, bar1::LEU2, clb4::HIS3), YST46 (FKH2-6HA-hph, bar1::LEU2, clb3::TRP1, clb4::HIS3), YST47 (FKH2-6HA-hph, bar1::LEU2, clb2::URA3) and YST50 (FKH2-6HA-hph, bar1::LEU2, clb2::URA3, clb3::TRP1, clb4::HIS3), generated by tagging Fkh2 (see Supplementary Table S1). To perform the Bimolecular Fluorescence Complementation analyses (see below) the plasmid pFA6a-Venus-C (accession number EF210810)² was used to generate the Ndd1-Venus-C fusion cassette, and the plasmid pYM30 (accession number P30242, Euroscarf) was used to generate Clb1-CFP, Clb2-CFP, Clb3-CFP and Clb4-CFP integration cassettes. Genetic manipulations of all strains generated in this study were validated by PCR analysis. To generate clb3Δclb4Δ (MATa his3Δ1 leu2Δ0 met15Δ0 ura3Δ0 clb3::LEU2 clb4::KanMX6) and clb5Δclb6Δ (MATa his3Δ1 leu2Δ0 met15Δ0 ura3Δ0 clb5::KanMX6 clb6::LEU2) double mutants, a standard PCR-mediated gene targeting procedure was carried out as described previously.³ For single deletion of CLB4 and CLB5, the plasmid pUG6 (accession number P30114, Euroscarf) was used as a template and the oligonucleotides Fwd/Rev-clb4Δ or Fwd/Rev-clb5Δ to amplify the gene-specific KanMX6 integration cassettes. Then, the amplified DNA cassettes were used to transform wild type cells.¹ After selection of transformants and verification of the correct chromosomal integration of the selection marker cassette, a respective yeast clone was used to generate double gene deletions. For the amplification of CLB3- and CLB6-specific integration cassettes, plasmid pACT4-1b⁴ and the oligonucleotide pair Fwd/Rev-clb3Δ or Fwd/Rev-clb6Δ was used to generate the respective LEU2 integration cassette. The corresponding deletion strains were transformed and selected clones verified for positive gene disruption. Yeast strains were grown in yeast peptone dextrose (YPD) or synthetic complete (SC) media containing 2% glucose as carbon source with respective antibiotics and auxotrophic additives at 30 °C.

<a id='e4cc460a-b378-4b87-a116-d4f41d1912ce'></a>

Plasmids

Plasmids pACT4-1b and pBTM117c⁴ were a kind gift from Erich Wanker (Max Delbrück Center for Molecular Medicine, Berlin, Germany). Plasmids encoding the full length fusion proteins LexA-Clb1-6 and LexA-Fkh1-2 were generated as described previously.³⁵ The open reading frame of the

<a id='1d2cb5e0-4145-4aa3-8dc2-2c683afb6e1b'></a>

- 22 -

<!-- PAGE BREAK -->

<a id='49711404-dc4a-4d5d-aa47-76521818825d'></a>

Barberis M. et al.

<a id='f0b07b4b-4f84-4b78-bccc-55651223390c'></a>

respective genes was amplified using genomic DNA isolated from BY4741 strain as DNA template and oligonucleotides Fwd-clb1s, Rev-clb1n; Fwd-clb2s, Rev-clb2n; Fwd-clb3s, Rev-clb3n; Fwd- clb4s, Rev-clb4n; Fwd-clb5s, Rev-clb5n; Fwd-clb6s, Rev-clb6n and Fwd-fkh1s, Rev-fkh1n; Fwd- fkh2s, Rev-fkh2n (see Supplementary Table S2). For the generation of LexA-Ndd1, oligonucleotides Fwd-ndd1s and Rev-ndd1n were used. To amplify fragments of *fkh1* and *fkh2* encoding the C-terminal part of the protein Fwd-fkh1_360s, Rev-fkh1n and Fwd-fkh2_387s, Rev- fkh2n were used. The amplified DNA fragments were purified and cloned into the cloning plasmid pJET1.2/blunt (CloneJET PCR Cloning Kit, Fermentas). Subsequently, the sequence of the constructs obtained was validated by sequencing, and the plasmid DNA verified was then treated with the restriction endonucleases *SalI* and *NotI*, purified and subcloned into the *SalI/NotI* sites of pBTM117c and pACT41b. For the construction of the plasmid p426GPD-VN encoding the N-terminal region of the Venus protein, a PCR was performed using plasmid pFA6a-Venus-N (accession number EF210809)2 as DNA template and primer pair Fwd-venus-Nb and Rev-venus-Ne. Subsequently, the resultant DNA fragment was subcloned into the plasmid pJET1.2/blunt to generate the plasmid pJET1.2-VN. After sequence validation, the plasmid pJET1.2/VN was treated with the restriction endonucleases *BamHI* and *EcoRI*, and the resultant DNA fragment was ligated into the *BamHI/EcoRI* sites of the plasmid p426GPD.6 The plasmids p426GPD-VN-Fkh1, p426GPD-VN-Fkh2, p426GPD- VN-Clb1, p426GPD-VN-Clb2, p426GPD-VN-Clb3 and p426GPD-VN-Clb4 were generated to express N-terminal Venus-N-tagged Fkh1, Fkh2, Clb1, Clb2, Clb3 and Clb4. To this purpose, the open reading frame of *FKHI*, *FKH2*, and *CLB2* was amplified using genomic DNA as template and primer pairs Fwd-F1e, Rev-F1x; Fwd-F2e, Rev-F2x and Fwd-clb2VNe/s, Rev-clb2VNn/x (see Supplementary Table S2). After PCR, resultant DNA fragments were subloned into the plasmid pJET1.2/blunt. Subsequently, sequences were validated, and the respective plasmid DNA was treated with the restriction endonucleases *EcoRI* and *XhoI*. After purification, the DNA fragments were subcloned into the *EcoRI/XhoI* sites of the plasmid p426GPD-VN. To generate p426GPD-VN-Clb1, p426GPD-VN-Clb3 and p426GPD-VN-Clb4, the plasmid p426GPD-VN-Clb2 was treated with the restriction endonucleases *SalI/NotI* and the digested DNA fragments of *CLB1*, *CLB3* and *CLB4* were purified and subcloned. For the GST pull-down experiments, the plasmids pGEX6p2-Clb1,

<a id='80b413c6-e804-4765-91e1-121aa35f335d'></a>

- 23 -

<!-- PAGE BREAK -->

<a id='0ba0db14-6c2c-4bb5-8b11-a0c0ca81895f'></a>

Barberis M. et al.

<a id='069dc8e2-7dcc-43cb-aa0b-a556c4835947'></a>

pGEX6p2-Clb2, pGEX6p2-Clb3, pGEX6p2-Clb4, pGEX6p2-Clb5, pGEX6p2-Clb6 and pGEX6p2-
Ndd1 encoding the open reading frame of the respective genes fused to _GST_ were generated
subcloning the respective DNA fragments treated with the restriction endonucleases _Sal_I and _Not_I
into the _Sal_I/_Not_I sites of the plasmid pGEX6p2 (Phamarcia Biotech).

<a id='bd153b2d-6510-4bd1-bb88-54e5cdf18b3f'></a>

Cell synchronization

For the time course experiments where Clb2-18Myc, Clb3-TAP, Clb5-HA and Sic1-TAP were detected over time, yeast cultures synchronized in G1 phase were obtained by centrifugal elutriation as described previously⁵. For other synchronization experiments, overnight cultures of yeast strains were diluted to an OD₆₀₀ ~ 0.1–0.2 and cultures further incubated to an OD₆₀₀ ~ 0.6. To induce cell cycle arrest in G1 phase, cells were treated with α-factor (15 µg/ml, Universitat Pompeu Fabra, Barcelona, Spain) and further incubated for 2.5 h at 30 °C. Arrest of cells in S phase or metaphase was achieved by adding 75 mM hydroxyurea (Sigma-Aldrich) or 5 µg/ml nocodazole (AppliChem), respectively. Subsequently, cultures were incubated for additional 2 h at 30°C. In the time course experiments performed employing the Bimolecular Fluorescence Complementation analysis (see below), α-factor was added to the cultures as described above and arrested cells were harvested after incubation for 2 h at 30 °C. Cell pellets were then washed twice with the respective medium, fresh medium was added and cultures were further incubated. Samples were taken every 10 min for a total time of 120 min, and analysed by fluorescence microscopy and flow cytometry (FACS).

<a id='a66b0a5f-cae9-4233-b05d-662443108ff3'></a>

## Cytometry analysis

For FACS analysis, cells were fixed in 70% ethanol and treated overnight with RNAse A (0.25 mg/ml final concentration, Sigma-Aldrich) and Proteinase K (0.5 mg/ml final concentration, Sigma-Aldrich) in 50 mM sodium citrate. DNA was stained with propidium iodide, and a total of 10,000 cells were analysed in a flow cytometer (FACSCalibur, Becton Dickinson Immunocytometry Systems, USA).

<a id='3359d6d9-2762-45b7-ae81-6150d8ecf797'></a>

- 24 -

<!-- PAGE BREAK -->

<a id='43cfa8b1-3e25-4882-974e-5946ce8751ac'></a>

Barberis M. et al.

<a id='efdb5775-18c2-4605-b9d9-e48d8fb1a12c'></a>

## Western blot

For protein quantification of the time course experiments where Clb2, Clb3, Clb5 and Sicl were detected over time, TCA protein extracts and protein detection followed the protocol described previously. For the other analyses, protein samples were loaded and separated using 10% SDS gels, transferred onto a nitrocellulose Protran membrane (PerkinElmer), and membranes were treated with mouse a-Myc tag antibody (1:10.000, Millipore) as well as the corresponding peroxidase (POD)-coupled secondary antibody (1:10.000, a-mouse IgG POD conjugate, Sigma Aldrich). Membranes were treated with Western Lighting luminol reagent (PerkinElmer) and exposed to a high performance chemiluminescence film (GE Healthcare) to visualize proteins. In addition, polyacrylamide gels were incubated in staining solution (40% Methanol, 7% Acetic acid, 0.1% Coomassie Brilliant Blue R250) to verify an equal loading of samples. De-staining of gels was performed in 40% Methanol and 10% Acetic acid.

<a id='b086fc93-5a07-4313-9392-81b8aca8256e'></a>

In vitro kinase assays

For the assay in Figure 3c, GST-Fkh2 was expressed in _E. coli_ and purified using glutathione-Sepharose beads. To obtain the Clb3/Cdk1 complex, the W303 strain and a strain expressing Clb3-HA from its chromosomal locus were used. 100 ml cultures at OD660 ~ 0.8 were collected and total amount of protein was subjected to immunoprecipitation with anti-HA antibody and protein A-Sepharose beads. For the kinase assay, immunoprecipitated Clb3/Cdk1 was incubated with bacterially expressed GST-Fkh2 for 30 min at 30 °C. The entire kinase assay was loaded on a gel, transferred to a membrane and exposed to detect phosphorylation. After developing the kinase assay, the membrane was subsequently plotted using antibodies against GST (substrate levels) and HA (to detect cyclin). Input levels were determined loading 5% of the total amount of protein used in the immunoprecipitation in a gel and Cdk1 was detected using anti-PSTAIR antibodies (Millipore). For the assay in Figure 3e, Clb2/Cdk1 and Clb3/Cdk1 complexes were isolated from the W303 strain (_MATa ade2-1 ura3-1 his3-11,15 trp1-1 leu2-3,112 can1-100_). Yeast cells were transformed with plasmids expressing C-terminal TAP-tagged Clb2 and Clb3 under galactose (GAL1) promoter (pRSAB1234GAL-CLB2-TAP and pRSAB1234Gal-CLB3-TAP). Transformants were grown in

<a id='a031109e-5e47-4271-8b51-4279796f6709'></a>

- 25 -

<!-- PAGE BREAK -->

<a id='fdd2a5d5-cfef-410a-89fa-d3da7d754156'></a>

Barberis M. et al.

<a id='2c4c0254-91c2-463d-96da-79ccc605cd6b'></a>

selective medium supplemented with 2% galactose to log phase (OD ~ 0.7), harvested by centrifugation and TAP-purification of cyclin/Cdk1 complexes was performed with IgG beads (Roche) as described previously.7,8 Cks1 was purified as described previously.9 For isolation of GST-tagged full-length and mutated variants of Fkh2 (pGEX-Fkh2, pGEX-Fkh2_S683A and pGEX-Fkh2_S697A), the respective bacterial protein lysates were incubated with Glutathione Sepharose 4B beads (GE Healthcare) for 8 h at 4 °C as described in the GST Pull-Down Assay section. Then, the beads were washed twice with 1 × PBS and incubated with 300 µl of elution buffer (10 Mm reduced gluthathione, 50 mM TrisHCl, pH 7,4) for 10 min. Samples of eluted proteins were separated by 10% SDS-PAGE and gels stained with Coomassie brilliant blue G-250 (Sigma). The respective protein band intensities were quantified by ImageQuant TL software (GE Healthcare) and protein concentrations determined using variable amounts of bovine serum albumine (BSA) as standard. The kinase reactions were performed according to the standard phosphorylation assay protocol.10 About 10 nM of the purified kinase complex was used. The assay mixture contained 50 mM HEPES pH7.4, 5 mM MgCl2, 150 mM NaCl, 0.1% NP-40, 20 mM imidazole, 2% glycerol, 2 mM EGTA, 0.2 mg/ml BSA, 500 nM Cks1 and 500 mM ATP (with added [c-32P]ATP (Perkin Elmer)). Substrate-cyclin/Cdk1 complex formation was initiated by adding pre-incubation mixture (50 mM HEPES pH7.4, 5 mM MgCl2, 150 mM NaCl, 0.2 mg/ml BSA and 500 mM ATP) and [c-32P]ATP to an excess amount of purified substrate (200 - 400 nM). Aliquots were taken after 8 and 16 min of incubation and reaction was stopped by adding SDS sample buffer (200 mM TrisHCl pH 6.8, 400 mM DTT, 8% SDS, 0,4% bromophenol blue, 40% glycerol). In a similar assay composition, the Histone H1 was used as a positive control. Phosphorylated substrate species were detected by a PhosphorImager (GE Healthcare). Quantification was performed with ImageQuant TL software (GE Healthcare).

<a id='de8a8ed5-d644-4859-898b-e66e7797793f'></a>

**In vivo phosphorylation assay**
Yeast cells were grown at 25 C in YPD to OD660 ~ 0.4 and synchronized in G1 phase with α-factor (2 g/ml) for 3 h, before releasing into fresh medium. Samples were collected every 10 min for 90 min after synchronous release, and extracted proteins of the most relevant time points were applied to a

<a id='2e7ab342-7909-4578-9d42-28e157d0c5a0'></a>

- 26 -

<!-- PAGE BREAK -->

<a id='b03c62c7-645f-43ba-addd-5de0b976eb17'></a>

Barberis M. et al.

<a id='9699ed4f-4867-421b-a250-a5743341a5e7'></a>

6% PAGE gel added with 10 μM Phos-tag (Wako) and 20 μM MnCl2 for 2 h at 100 V in the cold.
Proteins were transferred to a PVDF membrane for 2 h at 200 mA on ice. Fkh2-6HA was analysed by
Western blot using an anti-HA antibody.

<a id='32d0dd77-e6bd-45c0-a6b6-c56d06a9ce05'></a>

Yeast-Two-Hybrid screen
L40ccua cells were transformed with the respective pBTM117c and pACT4-1b plasmids as indicated.
Transformants were selected on synthetic complete SDII medium lacking tryptophan and leucine.
Subsequently, overnight cultures of single colonies (96 well format) were spotted on SDII and SDIV
selection media, the latter lacking tryptophan, leucine, histidine and uracil. Reporter gene activity was
reduced by adding 3-amino-1,2,4-triazole (Sigma-Aldrich) to SDIV medium in the indicated
concentrations. For detection of B-galactosidase activity, cells were spotted on SDII media covered
with a nylon membrane (Magna Charge Nylon Transfer membrane, Micro Separation Inc.) and
staining was performed as described previously.¹¹ Plates were incubated for 5 days at 30 °C, and cell
viability was monitored.

<a id='a570868b-af0a-4c12-8f04-2de8d209bedd'></a>

GST pull-down assay

Pull-down assays were performed as described previously.⁵ E. coli cells XL1blue (endA1 gyrA96(nalR) thi-1 recA1 relA1 lac glnV44 F'[ ::Tn10 proAB⁺ lacIq Δ(lacZ)M15] hsdR17(rK⁻ mK⁺); Stratagene) were transformed with the plasmid pGEX6p2 carrying the indicated genes and incubated in LB media. At OD600 of ~ 0.5 – 0.7, expression of proteins was induced by adding 1 mM isopropylbeta-D-thiogalactopyranoside (IPTG, Fermentas), and cultures were incubated for additional 3 h at 37°C. Subsequently, cells were harvested and lysed in GST-binding buffer (20 mM TrisHCl pH 7.9, 125 mM NaCl, 5 mM MgCl2, 0.5 mM DTT, 10 mg/ml Lysozym; Sigma Aldrich). Then, cell lysates were sonicated 10 times for 10 sec (Branson Sonifier W250), and 10% Glycerol and 0.1% NP-40 were added. After centrifugation (25 min, 20.000 rcf, 4 °C), Glutathione Sepharose 4B beads (GE Healthcare) were added to the supernatants containing the expressed GST-tagged proteins and incubated for 8 h at 4 °C. Then, beads were washed with GST-binding buffer, added to 1 ml yeast protein lysates (5 µg/µl total protein) that were prepared from yeast cells expressing Myc-tagged

<a id='2be4d30c-c837-4b1b-8974-01893ab596a8'></a>

- 27 -

<!-- PAGE BREAK -->

<a id='be5abbfb-c982-4147-8dfb-68c3a6d072cc'></a>

Barberis M. et al.

<a id='fc94a0d9-cf06-4a70-8511-9029bcffb70f'></a>

Fkh1, Fkh2 or Ndd1, and incubated overnight at 4 °C. To this purpose, 200 ml of yeast cultures (OD600~0.7) were harvested by centrifugation, cell pellets were washed with phosphate-buffered saline solution (PBS; 137 mM NaCl, 2.7 mM KCl, 10 mM Na2HPO4, 2 mM KH2PO4, pH 7.4), frozen in liquid nitrogen and lysed with glass beads (Sigma Aldrich, acid washed) by vigorous shaking. Finally, pull-down samples were washed twice with ice-cold GST-binding buffer and proteins bound were eluted with SDS sample buffer.

<a id='4928cedb-33f7-4232-94d8-b296f93fd548'></a>

Bimolecular Fluorescence Complementation (BiFC) assay and fluorescence microscopy
Haploid yeast cells expressing the C-terminal region of the Venus protein fused to the C-terminal
region of Ndd1 (Ndd1-VC) were transformed either with plasmids p426GPD-VN-Fkh1, p426GPD-
VN-Fkh2, p426GPD-VN-Clb1, p426GPD-VN-Clb2, p426GPD-VN-Clb3 or p426GPD-VN-Clb4
encoding fusion proteins between the N-terminal region of Venus and the N-terminal region of the
selected proteins. Subsequently, yeast clones were isolated and cultured in liquid SC media (OD600 ~
0.6). Staining of the nucleus was performed by adding 2.5 µg/ml 4',6-diamidino-2-phenylindole
(DAPI, Sigma-Aldrich) to the media. After 20 min, cells were harvested by centrifugation, washed
once with 1 x PBS and monitored for a Venus-dependent fluorescent (BiFC) signal using a Zeiss
Axiolmager Z1 microscope (Carl Zeiss AG, Germany) with a Plan-NeoFluar 60 × / 1.3 NA oil
immersion objective. Fluorescence images were taken using a standard fluorescein isothiocyanate
filter set (excitation band pass filter, 450-490 nm; beam splitter, 510 nm; emission band pass filter,
515-565 nm), and recorded on a Zeiss Axiocam Mrm (Carl Zeiss AG) with 2 × 2 binning.

<a id='9cdbe6c7-ed23-44f5-b6e4-8e7d92544162'></a>

## Chromatin immunoprecipitation (ChIP)

ChIP assays were performed essentially as described previously.³ Cultures of yeast cells expressing Myc-tagged Fkh1, Fkh2 or Ndd1 as well as wild type and deletion strains of _fkh1Δ_ and _fkh2Δ_ were grown to mid-exponential phase and cross-linked by adding formaldehyde (16% stock solution in methanol-free water, Ultra Pure EM Grade, Polysciences Inc.) to a final concentration of 1%. Cells were then harvested by centrifugation and cell pellets resuspended in pre-cooled lysis buffer (50 mM HEPES/KOH, pH 7.5, 500 mM NaCl, 1 mM EDTA, 1% Triton X-100, 0.1% DOC, 0.1% SDS,

<a id='ab99e645-227b-4e0a-ad27-8040885cedde'></a>

- 28 -

<!-- PAGE BREAK -->

<a id='f7906a36-c17c-4824-8c89-96a2aa9d5e26'></a>

Barberis M. et al.

<a id='02d40be9-f631-4e37-a547-2b38dc252d42'></a>

complete protease inhibitor cocktail, Roche Diagnostics GmbH). Glass beads (acid-washed, 425-600 µm in diameter, Sigma-Aldrich) were added to the samples, which were then vortexed 3 times for 90 sec. Subsequently, the soluble protein-DNA fraction was sonicated 3 times for 10 sec (Branson Sonifier W250). For the immunoprecipitation, 5 µg of mouse α-Myc tag antibody (Millipore) were added to cell lysates, which were then incubated on a rotation wheel for additional for 2 h at 4°C. To immobilize the immune complex, 50 µl of pre-cooled Protein A/G agarose mix in 1 × PBS (50% mix of Protein A/G agarose, immobilized protein, Roche) were added to the lysates, which were further incubated for 4 h at 4°C. Beads were then washed twice with lysis buffer, once with DOC buffer (10 mM Tris-Cl, pH 8, 250 mM LiCl, 0.5% NP-40, 0.5% DOC, 1 mM EDTA, pH 8) and twice with 1 × TE (Tris-Cl 10 mM, EDTA 1 mM, pH 8). Finally, immunoprecipitated complexes were eluted by adding TES buffer (Tris-Cl 50 mM, EDTA 10 mM, 1% SDS pH 8). Reverse cross-linking was performed by incubating samples overnight at 65 °C. Then, samples were treated with 0.2 µg/ml RNase A (Sigma-Aldrich) for 2 h at room temperature and 0.2 µg/ml Proteinase K (Sigma-Aldrich) was added prior incubation for 2 h at 55 °C. Extraction of DNA was performed using phenol:chloroform:isoamyl alcohol (25:24:1, Sigma-Aldrich) and precipitated with ethanol supplemented with 5 M NaCl and 1 µl LPA (Linear PolyAcrylamide, GenElute-LPA, stock: 25 mg/ml, Sigma-Aldrich, Germany). Precipitated DNA was analysed by quantitative Real-Time PCR using CLB promoter-specific oligonucleotides.

<a id='212e3a42-56d8-4614-83b2-96a20c1e7cdb'></a>

Real-Time PCR

Total RNA was isolated from yeast cells using the RiboPure Yeast Kit (Applied Biosystems, Ambion, Inc., USA) according to the manufacturer's instructions. RNA was converted to cDNA using the SuperScript II Double-Stranded cDNA Synthesis Kit (Invitrogen, USA) according to the manufacturer's instructions. The quantification of PCR products was performed using the fluorescent dye SYBR Green (Applied Biosystems) and a Real-Time PCR machine (Applied Biosystems, 7900 HT Real-Time PCR System). Analysis of ChIP samples was performed amplifying promotor regions of genes *CLB1*: Fwd-clb1_prom, Rev-clb1_prom; *CLB2*: Fwd-clb2_prom, Rev-clb2_prom; *CLB3*: Fwd-clb3_prom, Rev-clb3_prom and *CLB4*: Fwd-clb4_prom, Rev-clb4_prom. Oligonucleotides for

<a id='cf9b2c1c-bead-4478-9f8a-6fd3bbe1858c'></a>

- 29 -

<!-- PAGE BREAK -->

<a id='c78ebca9-c731-402b-b6ac-120e284cb770'></a>

Barberis M. et al.

<a id='752beef6-9950-480b-8b2a-1dc7dbd92c9f'></a>

open reading frames Fwd-clb1_orf, Rev-clb1_orf; Fwd-clb2_orf, Rev-clb2_orf; Fwd-clb3_orf, Rev-clb3_orf and Fwd-clb4_orf, Rev-clb4_orf were used to analyse transcription of _CLB1_, _CLB2_, _CLB3_ and _CLB4_ genes. _TSA1_ (Fwd-tsa1_orf, Rev-tsa1_orf) and _ACT1_ (Fwd-tsa1_orf, Rev-tsa1_orf) were used as a reference. All oligonucleotide sequences are listed in see **Supplementary Table S2**.

<a id='f2547bf8-1dec-4ead-b12f-fe1652df3a43'></a>

Kinetic modeling and global sensitivity analysis
The kinetic models of Clb/Cdk1 regulation were generated starting from the network described previously.5 After basal, constant production of Clb5,6/Cdk1 (k₁), Sic1 binds to it forming the Clb5,6/Cdk1-Sic1 ternary complex (k2), which is also dissociated (k3). When Sic1 is degraded first by Cln1,2/Cdk1 (k5) and secondarily by all Clb/Cdk1 complexes, Clb5,6/Cdk1, Clb3,4/Cdk1 and Clb1,2/Cdk1, (k5), Clb5,6/Cdk1 promote Clb3,4/Cdk1 activation (kA), in addition to its basal, constant production (k7). Clb5,6 in the Clb5,6/Cdk1-Sic1 ternary complex are also degraded (k4). The role of Cln1,2/Cdk1 on Sic1 degradation is not included explicitly, but is incorporated as a basal activity in the reaction rate k5. Subsequently, Clb3,4/Cdk1 promote Clb1,2/Cdk1 activation (kB) together with Clb5,6/Cdk1 (kc), in addition to its basal, constant production (k9). Moreover, Clb1,2/Cdk1 promote their own activation by a positive feedback loop (kD). The basal degradation of Clb5,6, Clb3,4, Clb1,2 and Sic1 (k6, k8, k10 and k26, respectively) is also considered. The network incorporates explicitly regulation of Clb/Cdk1 production (k1, k7, k9), lumping together the processes from gene transcription to complex formation into a single step. The variants of the kinetic model were implemented by ordinary differential equations, and all parameters used for the simulations have the same value within all networks (see Supplementary Text for details on the full set of equations and parameters5). To analyse the influence of parameter values on the time delay between the peaks of Clb cyclins, a global sensitivity analysis was performed with a Monte Carlo approach. Random parameter sampling was employed to estimate the sensitivities of the network with respect to parameters, without knowing their precise values. We randomly selected 10,000 parameter sets and simulated in each case different variants of the network. In the analysis, all parameters of the network may vary between 0.1-fold and 10-fold of their default values. The simulations were run with the software Mathematica® Version 10, Wolfram Research.

<a id='7c1475b5-e596-4d63-8d10-6eb8e3491efc'></a>

- 30 -

<!-- PAGE BREAK -->

<a id='eb7df2d5-90d7-45f0-aeea-5a8eedcdc400'></a>

Barberis M. et al.

<a id='80996350-cd90-4c2f-bccd-5d835cbbbc4f'></a>

# Boolean simulations using GenYsis

Boolean simulations and _in silico_ gene perturbations were performed with GenYsis2, a toolbox that uses efficient, reduced ordered binary decision diagrams based algorithms for attractor identification and gene perturbations. Reduced ordered binary decision diagrams (ROBDDs or in short BDDs) are directed acyclic graphs that can represent large Boolean functions in a space efficient manner, and are computationally suitable for complex Boolean operations (e.g., logical AND, OR, etc.) and set operations (e.g., Union, Intersection, etc.). To map gene regulatory networks on BDDs, the regulatory relations of the network have to be transformed into Boolean functions, representing the dynamics of a model. All the operations that can be performed on Boolean functions can also be performed on their corresponding BDD representations. 2 GenYsis uses this strategy to efficiently compute cyclic attractors of large networks that are not feasible using other existing software. The toolbox can be used for synchronous and asynchronous simulations, as well as single or multiple _in silico_ perturbations. The available perturbation experiments comprise deletion, overexpression and fixed initial state experiments. All simulations were performed using the synchronous mode, and several perturbations were tested (i.e., deletion and overexpression of the cyclin-dependent kinase inhibitor Sicl or overexpression of the mitotic cyclin Clb2). The binaries of the software are available for Linux and Mac OS X in the following address: http://www.vital-it.ch/software/genYsis

<a id='c60739db-61f7-4a1a-8f5b-76d20a7c73c2'></a>

## Qualitative dynamic simulations using SQUAD

Continuous simulations of Clb sequential expression were performed with SQUAD  , a software providing dynamical simulations of signaling networks that uses a standardized qualitative dynamical systems approach. SQUAD converts a given network into a discrete dynamical system, and it uses a binary decision diagram algorithm to identify all the steady states of the system. The algorithm used is based on the same principles as GenYsis, therefore providing comparable results. After identification of an attractor or a steady state, SQUAD creates a continuous dynamical system and localizes its steady states that are located near the steady states of the discrete system. The software permits to simulate the continuous system by using a system of standardized ODEs to simulate the

<a id='690f205e-b09f-4ae6-bdc3-3b2eca45157b'></a>

- 31 -

<!-- PAGE BREAK -->

<a id='9e0a79d8-d36d-4b5c-8065-ceea1aa4b602'></a>

Barberis M. et al.

<a id='7aba21dd-252f-40d1-af55-c556b7e7f6e3'></a>

behavior of the network in time, allowing for the modification of several parameters such as decay
rate of each component. Additionally, SQUAD includes a framework for perturbing networks in a
manner similar to GenYsis, thus allowing to observe the effect of gene perturbations in a dynamic
fashion. 13 The software is publicly available at http://www.vital-it.ch/software/SQUAD/

<a id='b8b05ba0-e794-49c5-ab8a-eb30f896e377'></a>

## Boolean model validation using MaBoSS

In order to cross-verify the results obtained using GenYsis and SQUAD, an independent software called MaBoSS was used.14 MaBoSS is a framework for qualitative modeling that runs continuous simulations in time. Similarly to SQUAD, MaBoSS aims to bridge the gap between qualitative and quantitative approaches, and it is based on continuous time Markov processes applied on Boolean state spaces. MaBoSS uses a generalization of Boolean equations, in order to describe the temporal evolution of the modeled biological process. Mathematically, this approach can be translated in a set of ordinary differential equations (ODEs) on probability distributions. The software is able to simulate such a system by applying Kinetic Monte-Carlo algorithm on the Boolean state space, and it can thereafter compute the temporal evolution of probability distributions and estimate stationary distributions.14 MaBoSS can be downloaded at https://maboss.curie.fr/

<a id='d8979b6c-e441-422e-916d-94a5c768129a'></a>

References for Supplementary Materials and Methods

<a id='53a989c6-9c2c-4d36-86ee-377fb6b710ae'></a>

- 32 -

<!-- PAGE BREAK -->

<a id='09a157bb-7a31-4506-afd4-3f5556588396'></a>

Barberis M. et al.

<a id='635de055-2b71-4d07-9cae-148ec011bec5'></a>

1. Longtine, M. S. et al. Additional modules for versatile and economical PCR-based gene deletion and modification in Saccharomyces cerevisiae. Yeast 14, 953-961 (1998).
2. Sung, M. K. & Huh, W. K. Bimolecular fluorescence complementation analysis system for in vivo detection of protein-protein interaction in Saccharomyces cerevisiae. Yeast 24, 767-775 (2007).
3. Linke, C., Klipp, E., Lehrach, H., Barberis, M. & Krobitsch, S. Fkh1 and Fkh2 associate with Sir2 to control CLB2 transcription under normal and oxidative stress conditions. Front. Physiol. 4, 173 (2013).
4. Stelzl, U. et al. A human protein-protein interaction network: a resource for annotating the proteome. Cell 122, 957-968 (2005).
5. Barberis, M. et al. Sic1 plays a role in timing and oscillatory behaviour of B-type cyclins. Biotechnol. Adv. 30, 108-130 (2012).
6. Mumberg, D., Müller, R. & Funk, M. Yeast vectors for the controlled expression of heterologous proteins in different genetic backgrounds. Gene 156, 119-122 (1995).
7. Puig, O. et al. The tandem affinity purification (TAP) method: a general procedure of protein complex purification. Methods 24, 218-229 (2001).
8. Ubersax, J. A. et al. Targets of the cyclin-dependent kinase Cdk1. Nature 425, 859-864 (2003).
9. Reynard, G. J., Reynolds, W., Verma, R. & Deshaies, R. J. Cks1 is required for G1 cyclin-cyclin-dependent kinase activity in budding yeast. Mol. Cell. Biol. 20, 5858-5864 (2000).
10. Kõivomägi, M. et al. Cascades of multisite phosphorylation control Sic1 destruction at the onset of S phase. Nature 480, 128-131 (2011).
11. Ralser, M. et al. Ataxin-2 and huntingtin interact with endophilin-A complexes to function in plastin-associated pathways. Hum. Mol. Genet. 14, 2893-2909 (2005).
12. Garg, A., Di Cara, A., Xenarios, I., Mendoza, L. & De Micheli, G. Synchronous versus asynchronous modeling of gene regulatory networks. Bioinformatics 24, 1917–1925 (2008).

<a id='4aabd35c-89d1-4e20-b62d-bfe6de820157'></a>

- 33 -

<!-- PAGE BREAK -->

<a id='62c6f1f0-05c8-44ef-9f49-111fac652f02'></a>

Barberis M. et al.

<a id='da710a51-c3fc-4989-b337-95a59c82b714'></a>

13. Di Cara, A., Garg, A., De Micheli, G., Xenarios, I. & Mendoza, L. Dynamic simulation of regulatory networks using SQUAD. *BMC Bioinformatics* **8**, 462 (2007).
14. Stoll, G., Viara, E., Barillot, E. & Calzone, L. Continuous time Boolean modeling for biological signaling: application of Gillespie algorithm. *BMC Syst. Biol.* **6**, 116 (2012).

<a id='b2d1cb11-50a9-4106-8322-685b827477d2'></a>

- 34 -

<!-- PAGE BREAK -->

<a id='408539ac-930a-4624-9faf-42210ce57d5b'></a>

Barberis M. et al.

<a id='b3590552-276d-421e-86ae-ef7702d208c4'></a>

Supplementary Tables

<a id='4c551910-7ba7-4915-b564-925b18e85810'></a>

Table S1. Yeast strains used in this study.
<table id="34-1">
<tr><td id="34-2">Strain</td><td id="34-3">Genotype</td><td id="34-4">Source</td></tr>
<tr><td id="34-5">L40ccua</td><td id="34-6">MATa his3_200 trp1-901 leu2-3,112</td><td id="34-7">Ralser et al, 2005</td></tr>
<tr><td id="34-8"></td><td id="34-9">LYS2::(lexAop)4-HIS3 ura3::(lexAop)8-lacZ</td><td id="34-a"></td></tr>
<tr><td id="34-b"></td><td id="34-c">ADE2::(lexAop)8-URA3 gal80 canR cyh2R</td><td id="34-d"></td></tr>
<tr><td id="34-e">BY4741</td><td id="34-f">MATa his3Δ1 leu2Δ0 met15Δ0 ura3Δ0</td><td id="34-g">Euroscarf</td></tr>
<tr><td id="34-h">W303</td><td id="34-i">MATa ade2-1 ura3-1 his3-11,15 trp1-1 leu2-3,112 can1-100</td><td id="34-j">Euroscarf</td></tr>
<tr><td id="34-k">YAN49</td><td id="34-l">CLB3-TAP:HIS3, SIC1-TAP:KanMX::Nat</td><td id="34-m">Barberis et al, 2012</td></tr>
<tr><td id="34-n"></td><td id="34-o">CLB2-18MycKl:KanMx::URA3, CLB5-6HA:KanMx</td><td id="34-p"></td></tr>
<tr><td id="34-q">YAG20</td><td id="34-r">CLB3-TAP:HIS3, SIC1-TAP:KanMX::Nat</td><td id="34-s">This study</td></tr>
<tr><td id="34-t"></td><td id="34-u">CLB2-18MycKl:KanMx::URA3, CLB5-6HA:KanMx</td><td id="34-v"></td></tr>
<tr><td id="34-w"></td><td id="34-x">fkh1::HPH</td><td id="34-y"></td></tr>
<tr><td id="34-z">YAG21</td><td id="34-A">CLB3-TAP:HIS3, SIC1-TAP:KanMX::Nat</td><td id="34-B">This study</td></tr>
<tr><td id="34-C"></td><td id="34-D">CLB2-18MycKl:KanMx::URA3, CLB5-6HA:KanMx</td><td id="34-E"></td></tr>
<tr><td id="34-F"></td><td id="34-G">fkh2::HPH</td><td id="34-H"></td></tr>
<tr><td id="34-I">YAG135</td><td id="34-J">FKH2-6HA-hphNTI, bar1::LEU2</td><td id="34-K">This study</td></tr>
<tr><td id="34-L">YST44</td><td id="34-M">FKH2-6HA-hph, bar1::LEU2, clb3::TRP1</td><td id="34-N">This study</td></tr>
<tr><td id="34-O">YST45</td><td id="34-P">FKH2-6H-hph, bar1::LEU2, clb4::HIS3</td><td id="34-Q">This study</td></tr>
<tr><td id="34-R">YST46</td><td id="34-S">FKH2-6HA-hph, bar1::LEU2, clb3::TRP1, clb4::HIS3</td><td id="34-T">This study</td></tr>
<tr><td id="34-U">YST47</td><td id="34-V">FKH2-6HA-hph, bar1::LEU2, clb2::URA3</td><td id="34-W">This study</td></tr>
<tr><td id="34-X">YST50</td><td id="34-Y">FKH2-6HA-hph, bar1::LEU2, clb2::URA3, clb3::TRP1</td><td id="34-Z">This study</td></tr>
<tr><td id="34-10"></td><td id="34-11">clb4::HIS3</td><td id="34-12"></td></tr>
<tr><td id="34-13">Fkhl-Myc</td><td id="34-14">MATa FKHI-MYC9::kanMX6</td><td id="34-15">Linke et al, 2013</td></tr>
<tr><td id="34-16">Fkh2-Myc</td><td id="34-17">MATa FKH2-MYC9::natNT2</td><td id="34-18">Linke et al, 2013</td></tr>
<tr><td id="34-19">Ndd1-Myc</td><td id="34-1a">MATa NDD1-MYC9::kanMX6</td><td id="34-1b">This study</td></tr>
<tr><td id="34-1c">fkhlΔ</td><td id="34-1d">MATa fkh1::</td><td id="34-1e">Linke et al, 2013</td></tr>
<tr><td id="34-1f">fkh2Δ</td><td id="34-1g">MATa fkh2::</td><td id="34-1h">Linke et al, 2013</td></tr>
</table>

<a id='f1a5db26-6203-43e2-a65e-8fae47e0846e'></a>

- 35 -

<!-- PAGE BREAK -->

<a id='82e423c7-8bc3-46ae-a986-70626b06898b'></a>

Barberis M. et al.

<a id='809dd397-84ba-4a94-bf9c-dd31e7824c60'></a>

<table><thead><tr><th>Col 1</th><th>Col 2</th><th>Col 3</th></tr></thead><tbody><tr><td>fkh1Δ fkh2Δ</td><td>MATa fkh1:: fkh2::</td><td>Linke et al, 2013</td></tr><tr><td>Ndd1-VC/VN</td><td>MATa NDD1-VC::his3MX6 p426GPDpr-VN</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Fkh1</td><td>MATa NDD1-VC::his3MX6 p426GPDpr-VN-FKH1</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Fkh2</td><td>MATa NDD1-VC::his3MX6 p426GPDpr-VN-FKH2</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Clb1</td><td>MATa NDD1-VC::his3MX6 p426GPDpr-VN-CLB1</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Clb2</td><td>MATa NDD1-VC::his3MX6 p426GPDpr-VN-CLB2</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Clb3</td><td>MATa NDD1-VC::his3MX6 p426GPDpr-VN-CLB3</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Clb4</td><td>MATa NDD1-VC::his3MX6 p426GPDpr-VN-CLB4</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Fkh2</td><td>MATa NDD1-VC::his3MX6 CLB2-CFP::kanMX6</td><td></td></tr><tr><td>Clb2-CFP</td><td>p426GPDpr-VN-FKH2</td><td>This study</td></tr><tr><td>Ndd1-VC/VN-Fkh2</td><td>MATa NDD1-VC::his3MX6 CLB3-CFP::kanMX6</td><td></td></tr><tr><td>Clb3-CFP</td><td>p426GPDpr-VN-FKH2</td><td>This study</td></tr><tr><td>clb3Δclb4Δ</td><td>MATa his3Δ1 leu2Δ0 met15Δ0 ura3Δ0 clb3::LEU2<br>clb4::KanMX6</td><td>This study</td></tr><tr><td>clb5Δclb6Δ</td><td>MATa his3Δ1 leu2Δ0 met15Δ0 ura3Δ0 clb5::KanMX6<br>clb6::LEU2</td><td>This study</td></tr></tbody></table>

<a id='494746ef-5b77-4065-82d2-c798a3c83a3a'></a>

- 36 -

<!-- PAGE BREAK -->

<a id='5c7f21fe-fbe3-47f1-90cf-2f93e6d47442'></a>

Barberis M. et al.

<a id='1fef68e2-cb0a-4ebb-93b3-55428a9e7a38'></a>

Table S2. Oligonucleotides used in this study.

<a id='89a67cba-76a0-4855-b892-8a3a7182b16a'></a>

<table id="36-1">
<tr><td id="36-2">Primer</td><td id="36-3">Sequence</td></tr>
<tr><td id="36-4">Fwd-clbls</td><td id="36-5">5&#x27;-GCTTGTCGACTAATCTTCTCATAATG-3&#x27;</td></tr>
<tr><td id="36-6">Rev-clbln</td><td id="36-7">5&#x27;-ATTGCGGCCGCTTCACTCATGCAATG-3&#x27;</td></tr>
<tr><td id="36-8">Fwd-clb2s</td><td id="36-9">5&#x27;-CAGTCGACATTGATCTTATAGATGTCC-3&#x27;</td></tr>
<tr><td id="36-a">Rev-clb2n</td><td id="36-b">5&#x27;-ATTGCGGCCGCTTCTCATTCATGCAAGG-3&#x27;</td></tr>
<tr><td id="36-c">Fwd-clb3s</td><td id="36-d">5&#x27;-CTGAGTCGACAATGCATCATAACTCAC-3&#x27;</td></tr>
<tr><td id="36-e">Rev-clb3n</td><td id="36-f">5&#x27;-TATGCGGCCGCTTTAGTTAGATCTTTC-3&#x27;</td></tr>
<tr><td id="36-g">Fwd-clb4s</td><td id="36-h">5&#x27;-GATAGTCGACACAGATGATGCTTGAAG-3&#x27;</td></tr>
<tr><td id="36-i">Rev-clb4n</td><td id="36-j">5&#x27;-GAAGCGGCCGCAAGATGAGTAAGTTAG-3&#x27;</td></tr>
<tr><td id="36-k">Fwd-clb5s</td><td id="36-l">5&#x27;-GTAAGTCGACAACAATGGGAGAGAAC-3&#x27;</td></tr>
<tr><td id="36-m">Rev-clb5n</td><td id="36-n">5&#x27;-GTAGCGGCCGCATTACTAGTACTAATC-3&#x27;</td></tr>
<tr><td id="36-o">Fwd-clb6s</td><td id="36-p">5&#x27;-GCATGTCGACTAAAATGAATTGTATC-3&#x27;</td></tr>
<tr><td id="36-q">Rev-clb6n</td><td id="36-r">5&#x27;-TATGCGGCCGCTGATCTATGTTTCAAC-3&#x27;</td></tr>
<tr><td id="36-s">Fwd-fkh1s</td><td id="36-t">5&#x27;-GTCAGTCGACTATGTCTGTTACCAGTAG-3&#x27;</td></tr>
<tr><td id="36-u">Fwd-fkh1_360s</td><td id="36-v">5&#x27;-TATTGTCGACCTTCGAGAAGGTGCC-3&#x27;</td></tr>
<tr><td id="36-w">Rev-fkh1n</td><td id="36-x">5&#x27;-AATGCGGCCGCTGAATTTCAACTCAG-3&#x27;</td></tr>
<tr><td id="36-y">Fwd-fkh2s</td><td id="36-z">5&#x27;-TGAAGTCGACAATGTCCAGCAGCAAT-3&#x27;</td></tr>
<tr><td id="36-A">Fwd-fkh2_387s</td><td id="36-B">5&#x27;-TACTGTCGACCATTAGGCATAATTTATC-3&#x27;</td></tr>
<tr><td id="36-C">Rev-fkh2n</td><td id="36-D">5&#x27;-ATTGCGGCCGCTTAGTTGTTGATAATAC-3&#x27;</td></tr>
<tr><td id="36-E">Fwd-ndd1s</td><td id="36-F">5&#x27;-AGATGTCGACTATGGACAGAGATATAAG-3&#x27;</td></tr>
<tr><td id="36-G">Rev-ndd1n</td><td id="36-H">5&#x27;-TAAGCGGCCGCAAGTTTGGTTAATATTAC-3&#x27;</td></tr>
<tr><td id="36-I">Fwd-venus-Nb</td><td id="36-J">5&#x27;-TAGGATCCATGGTGAGCAAGGGCG-3&#x27;</td></tr>
<tr><td id="36-K">Rev-venus-Ne</td><td id="36-L">5&#x27;-TCGAATTCCTCGATGTTGTGGCGGAT-3&#x27;</td></tr>
<tr><td id="36-M">Fwd-fkh1VNe</td><td id="36-N">5&#x27;-AGAATTCTCGACTATGTCTGTTACC-3&#x27;</td></tr>
<tr><td id="36-O">Rev-fkh1VNx</td><td id="36-P">5&#x27;-CTCTCGAGTCAACTCAGAGAGGAATTG-3&#x27;</td></tr>
<tr><td id="36-Q">Fwd-fkh2VNe</td><td id="36-R">5&#x27;-AGAATTCTCGACAATGTCCAGCAGC-3&#x27;</td></tr>
<tr><td id="36-S">Rev-fkh2VNx</td><td id="36-T">5&#x27;-GTCTCGAGTTAGTTGTTGATAATACTG-3&#x27;</td></tr>
<tr><td id="36-U">Fwd-clb2VNe/s</td><td id="36-V">5&#x27;-AAGAATTCAGGTCGACGATGTCCAACCCAATAG-3&#x27;</td></tr>
<tr><td id="36-W">Rev-clb2VNn/x</td><td id="36-X">5&#x27;-TTCTCGAGTGCGGCCGCTTCTCATTCATGC-3&#x27;</td></tr>
</table>

<a id='3e7f1193-c404-4d47-80cc-4d5becf7dfb4'></a>

- 37 -

<!-- PAGE BREAK -->

<a id='0bf40319-7953-4571-a2ad-180ffb40c535'></a>

Barberis M. et al.

<a id='cec62061-a75a-4ff7-84d1-024e94cae344'></a>

<table id="37-1">
<tr><td id="37-2">Fwd-fkh1-Myc</td><td id="37-3">5&#x27;-CGTAACAACAAACGCAAACGTGAACAATTCCTCTCTGAGT GCTAGTGGTGAACAAAAG-3&#x27;</td></tr>
<tr><td id="37-4">Rev-fkh1-Myc</td><td id="37-5">5&#x27;-TATTGTTTAATAATACATATGGGTTCGACGACGCTGAATT TAGTGGATCTGATATCATCG-3&#x27;</td></tr>
<tr><td id="37-6">Fwd-fkh2-Myc</td><td id="37-7">5&#x27;-ACTAGATACGGATGGTGCAAAGATCAGTATTATCAACAAC GCTAGTGGTGAACAAAAG-3&#x27;</td></tr>
<tr><td id="37-8">Rev-fkh2-Myc</td><td id="37-9">5&#x27;-TTCATTTCTTTAGTCTTAGTGATTCACCTTGTTTCTTGTC TAGTGGATCTGATATCATCG-3&#x27;</td></tr>
<tr><td id="37-a">Fwd-ndd1-Myc</td><td id="37-b">5&#x27;-CTGTAATTCTAAATCTAATGGAAATTTATTCAATTCACAG GCTAGTGGTGAACAAAAG-3&#x27;</td></tr>
<tr><td id="37-c">Rev-ndd1-Myc</td><td id="37-d">5&#x27;-TTCCATAAAAAAAAAAGGTGAGATGCAAGTTTGGTTAATA TAGTGGATCTGATATCATCG-3&#x27;</td></tr>
<tr><td id="37-e">Fwd-fkh1Δ</td><td id="37-f">5&#x27;-TGTGCGTTCAATTAGCAAAGAAAGGCTTGGAGAGACACAG GTACGCTGCAGGTCGACAAC-3&#x27;</td></tr>
<tr><td id="37-g">Rev-fkh1Δ</td><td id="37-h">5&#x27;-TATTGTTTAATAATACATATGGGTTCGACGACGCTGAATT CTAGTGGATCTGATATCACC-3&#x27;</td></tr>
<tr><td id="37-i">Fwd-fkh2Δ</td><td id="37-j">5&#x27;-GTGCTCCCTCCGTTTCCTTTATTGAAACTTTATCAATGCG GTACGCTGCAGGTCGACAAC-3&#x27;</td></tr>
<tr><td id="37-k">Rev-fkh2Δ</td><td id="37-l">5&#x27;-TTCATTTCTTTAGTCTTAGTGATTCACCTTGTTTCTTGTC CTAGTGGATCTGATATCACC-3&#x27;</td></tr>
<tr><td id="37-m">Fwd-ndd1-VN</td><td id="37-n">5&#x27;-CTGTAATTCTAAATCTAATGGAAATTTATTCAATTCACAG GGTCGACGGATCCCCGGGTT-3&#x27;</td></tr>
<tr><td id="37-o">Rev-ndd1-VN</td><td id="37-p">5&#x27;-TCGATTAAAAAAAAAAGGTGAGATGCAAGTTTGGTTAATA TCGATGAATTCGAGCTCGTT-3&#x27;</td></tr>
<tr><td id="37-q">Fwd-clb2-CFP</td><td id="37-r">5&#x27;-GGTTAGAAAAAACGGCTATGATATAATGACCTTGCATGAA GGAGCAGGTGCTGGTGCTGG-3&#x27;</td></tr>
<tr><td id="37-s">Rev-clb2-CFP</td><td id="37-t">5&#x27;-CGATTATCGTTTTAGATATTTTAAGCATCTGCCCCTCTT CTAGTGGATCTGATATCATCG-3&#x27;</td></tr>
<tr><td id="37-u">Fwd-clb3-CFP</td><td id="37-v">5&#x27;-GAAGTGGATAGCATTAGCTGAACACAGAGTAGAAAGATCTAA CGGAGCAGGTGCTGGTGCTGG-3&#x27;</td></tr>
</table>

<a id='0dfc2dde-c4d8-464a-ba2f-9fda998a6c3b'></a>

- 38 -

<!-- PAGE BREAK -->

<a id='8cd846f2-4409-40cf-af25-386c53adde3e'></a>

Barberis M. et al.

<a id='7814670f-7ccd-4a54-ad83-3f4ee4b824f4'></a>

Rev-clb3-CFP: 5'-CTTTTTCCTTTGTTGATGCCATGTCTCGAGCTGAGGCTTTCTAGTGGATCTGATATCATCG-3'

Fwd-tsal_orf: 5'-ATGGTCGCTCAAGTTCAAAAG-3'

Rev-tsal_orf: 5'-CGTACTTACCCTTGTATTTGTCCAA-3'

Fwd-act1_orf: 5'-ATGTGTAAAGCCGGTTTTGC-3'

Rev-act1_orf: 5'-TGACCCATACCGACCATGATA-3'

Fwd-clb1_orf: 5'-CAGTCTAGGACGTTAGC-3'

Rev-clb1_orf: 5'-GTCGTGAATAGTAGATCC-3'

Fwd-clb1_prom: 5'-CAGACGCGCTTCAATTAG-3'

Rev-clb1_prom: 5'-GTTACCGTTGACGTGAG-3'

Fwd-clb2_orf: 5'-GGAATGTACAAGGTTGG-3'

Rev-clb2_orf: 5'-CAAATTGCTGACTACTTGG-3'

Fwd-clb2_prom: 5'-GTGCAAGTTCAAGGCAC-3'

Rev-clb2_prom: 5'-CATGCTATGAGATGCTAG-3'

Fwd-clb3_orf: 5'-GGATCGTCCAAGTACATG-3'

Rev-clb3_orf: 5'-CAGCAATGAAGAGTGAG-3'

Fwd-clb3_prom: 5'-GCAAGAACATGGACAC-3'

Rev-clb3_prom: 5'-GTGCAACACTATTCGCATC-3'

Fwd-clb4_orf: 5'-CTCTTCTACTGATGACGAAC-3'

Rev-clb4_orf: 5'-CTGTCCAGCTCAGTCTG-3'

Fwd-clb4_prom: 5'-CTAGAAGATTAGCAAGAT-3'

Rev-clb4_prom: 5'-GAGGTTGTACCGTATACC-3'

Fwd-clb3Δ: 5'-CGTTATATCAACCATCAAAGGAAGCTTTAATCTTCTCATAGGAACTGTGGGAATACTCAG-3'

Rev-clb3Δ: 5'-CTTTTTCCTTTGTTGATGCCATGTCTCGAGCTGAGGCTTTCA GAAGCTTTGGACTTCTTC-3'

Fwd-clb4Δ: 5'-CGGATACTAGGCTGCCCTGATCAAACAAGGAAATTGACAGG TACGCTGCAGGTCGACAAC-3'

Rev-clb4Δ: 5'-CGAAACCAAAACTGAAGCAAATGGTGTTAAGATGAGTAAGCTAGTGGATCTGATATCACC-3'

<a id='2264f1cd-c582-4d27-9b03-4e1ceb57f07b'></a>

- 39 -

<!-- PAGE BREAK -->

<a id='e832a744-4f5b-4793-bb4e-4cc4f0b2f993'></a>

Barberis M. et al.

<a id='a4354644-4672-470e-809c-d1cda328220c'></a>

<table id="39-1">
<tr><td id="39-2">Fwd-clb5Δ</td><td id="39-3">5&#x27;-TTTCCCTGTATTTAAAGCCGCTGAACACCTTTACTGAACAGT ACGCTGCAGGTCGACAAC-3&#x27;</td></tr>
<tr><td id="39-4">Rev-clb5Δ</td><td id="39-5">5&#x27;-GTAAAGAGTATGCGAATTCATGAGCATTACTAGTACTAATCT AGTGGATCTGATATCACC-3&#x27;</td></tr>
<tr><td id="39-6">Fwd-clb6Δ</td><td id="39-7">5&#x27;-TTATTCTCTGATATTCTCTCCCTCCTTTTAAATTTTTAAAGG AACTGTGGGAATACTCAG-3&#x27;</td></tr>
<tr><td id="39-8">Rev-clb6Δ</td><td id="39-9">5&#x27;-AGATGCAGGGGGTTAGCTGGCTATAATTTTGATCTATGTT CAGAAGCTTTGGACTTCTTC-3&#x27;</td></tr>
</table>

<a id='bbca41c8-9fae-4a3e-8945-464407642bcc'></a>

- 40 -
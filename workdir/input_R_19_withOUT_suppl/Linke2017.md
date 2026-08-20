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
<a id='92e7887d-30ab-4078-9043-f7747b1249ce'></a>

Proc. Natl. Acad. Sci. USA
Vol. 96, pp. 11352–11357, September 1999
Cell Biology

<a id='24737e49-0310-41d9-a7eb-23d05db4fab4'></a>

A quantitative analysis of the kinetics of the G2 DNA damage checkpoint system

<a id='be8a1b5d-165d-408d-a597-4eb8e7a4ae83'></a>

BALTAZAR D. AGUDA*

<a id='e04a33b5-5617-484e-8626-15e0da0e1f2e'></a>

Department of Chemistry and Biochemistry, Laurentian University, Sudbury, Ontario, Canada P3E 2C6

<a id='f1715090-3f3e-41c6-93bc-cb46c737991c'></a>

Edited by Joan V. Ruderman, Harvard Medical School, Boston, MA, and approved July 19, 1999 (received for review March 29, 1999)

<a id='601f4201-6703-4315-82ff-d4cef0865cc5'></a>

ABSTRACT A detailed model of the G2 DNA damage checkpoint (G2DDC) system is presented that includes complex regulatory networks of the mitotic kinase Cdc2, phosphatase Cdc25, Wee1 kinase, and damage signal transduction pathways involving Chk1 and p53. Assumptions on the kinetic equations of the G2DDC are made, and computer simulations are carried out to demonstrate how the various subsystems operate to delay or arrest cell cycle progression. The detailed model could be used to explain various experiments relevant to G2DDC reported recently, including the nuclear export of 14-3-3-bound Cdc25, the down-regulation of cyclin B1 expression by p53, the effect of Chk1 and p53 on Cdc25 levels, and Wee1 degradation. It also is shown that, under certain conditions, p53 is necessary to sustain a G2 arrest.

<a id='0b0fc2a6-ace1-4210-b580-eed332700a1f'></a>

It is very important to study cell cycle checkpoints because they are windows into the inner workings of the complex process of cell division. Checkpoints can be classified as either intrinsic or extrinsic depending on whether or not they are considered as part of the cell cycle engine (1, 2). The current view of the checkpoint that arrests or delays the cell cycle at G2 as a result of DNA damage (henceforth called the G2 DNA damage checkpoint or G2DDC) is that it is an extrinsic mechanism by which damage signal transduction pathways impinge on the cell cycle machinery. I will discuss how the G2DDC perturbs this machinery where it is vulnerable and analyze the kinetics of the checkpoint.

<a id='267185a9-e656-4dc5-a860-a16171ef0bfa'></a>

Models of the G2DDC have been proposed previously (3–5), but they are schematic at best and lack kinetic details. In this paper, I present a detailed molecular mechanism of the G2DDC system and carry out computer simulations based on certain assumptions on the kinetics of the component processes. To simplify my analysis, I first break down the complex G2DDC network into subsystems, understand the intrinsic dynamics of each subsystem, and show how these subsytems interact to elicit a checkpoint response. I will show that my detailed model could explain recent experimental results such as those of Bunz et al. (6), Innocente et al. (7), Lopez-Girona et al. (8), and Toyoshima et al. (9).

<a id='9885952e-73f4-40fb-977b-c0b6aab0f9a3'></a>

The reader is warned that several steps of the detailed model presented here must be regarded as tentative for now because of insufficient or lack of evidence that these steps actually occur in vivo. However, there are good reasons why I think it is not unreasonable to attempt a quantitative study of the G2DDC at this time. In the mathematical field of reaction network analysis, some promising results show that just knowing the structure of the network is sufficient to deduce certain possible behavior of a network independent of the values of the rate parameters; see for example the work of Feinberg and Horn (10). In addition, the type of dynamics a system exhibits usually depends on ratios of rate parameters instead of their absolute values; therefore, it is not necessary that exact pa-

<a id='559b0287-d088-49e8-989c-0b0e0b9bd9a2'></a>

The publication costs of this article were defrayed in part by page charge payment. This article must therefore be hereby marked "advertisement" in accordance with 18 U.S.C. 1734 solely to indicate this fact.

<a id='d950ec73-6325-47d1-9a5b-3816a0463d87'></a>

PNAS is available online at www.pnas.org.

<a id='ac5141c0-5afe-4472-a38b-f96bf80188cd'></a>

rameter values be known to understand the types of behavior that a system can exhibit. As an example, the reader is referred to the pioneering work on cell cycle modeling by Novak and Tyson (11). Important dynamical information can be inferred from the structure of a given network and, because many of the G2DDC pathways have been identified or postulated, a quantitative kinetic study of this important checkpoint system could lead to a better perspective and understanding of this complex experimental system.

<a id='f38afc94-9f2c-4ce5-ac36-88dadcbc0f62'></a>

The G2DDC and Its Subsystems

An overview of the G2DDC system is given in Fig. 1, which
shows that the basic checkpoint targets are the cyclin-
dependent kinase (CDK) Cdc2 and its primary regulators,
Cdc25 and Wee1. For its activation, Cdc2 requires binding with
cyclin B and the active Cdc2/cyclin B complex often is referred
to as MPF (for maturation-promoting factor). I subdivide the
G2DDC system into the following subsystems: (i) MPF sub-
system, (ii) Cdc25 subsystem, (iii) Wee1 subsytem, and (iv)
DNA damage signal transduction pathways. I will discuss the
details of these subsytem and show how they are coupled to
each other.

<a id='39575896-029c-4931-8fe2-2c49ba1b316d'></a>

The DNA damage signal transduction pathways summarized in Fig. 1 involve the Chk1 kinase and p53. The Chk1 pathway inhibits the activity of Cdc25 whereas p53 could down-regulate MPF activity [via the induction of the CDK inhibitor p21 (6) or the repression of cyclin B1 transcription (7)] and down-regulate Cdc25 activity via 14–3–3 proteins as will be discussed in more detail below (12).

<a id='5f00f794-60f8-4bcf-a2c2-318a2381efd4'></a>

What is the logic behind the architecture of the G2DDC shown in Fig. 1? I propose a general answer at this point: an antagonistic interaction between MPF and Wee1 exists (Wee1 inhibits MPF activity by tyrosine phosphorylation while MPF phosphorylates Wee1, leading to the latter's degradation) and Wee1 dominates at first and prevents entry into mitosis; once Cdc25 accumulates inside the nucleus, MPF activity increases rapidly (because of a positive feedback loop between Cdc25 and MPF) and Wee1 eventually loses its battle with MPF, thereby allowing the cell to undergo mitosis. I now will describe the details of the implementation of this picture of the G2-M cell cycle transition and the G2DDC system.

<a id='f975b87d-129b-4954-920e-31380cb162c7'></a>

## The MPF Subsystem

A certain threshold of MPF activity must be reached for a cell to initiate mitosis; thus, a G2-M checkpoint necessarily involves, directly or indirectly, the regulation of MPF. Excellent reviews on MPF regulation are already available (11, 13), and I give only a summary here. Activation of Cdc2 requires binding with cyclin B and phosphorylation on Thr-161 by a CDK-activating kinase. Cdc2 is inactive when its Tyr-15 and

<a id='8dfd5b98-0e99-4627-a2c2-b52a88e16b64'></a>

This paper was submitted directly (Track II) to the *Proceedings* office.
Abbreviations: CDK, cyclin-dependent kinase; MPF, maturation-promoting factor; G2DDC, G2 DNA damage checkpoint.
*To whom reprint requests should be addressed. E-mail: daguda@nickel.laurentian.ca.

<a id='7fb59a51-4d80-498f-9c6c-9b8a349725d5'></a>

11352

<!-- PAGE BREAK -->

<a id='7a643610-3730-415f-9d56-39fe362e5602'></a>

Cell Biology: Aguda

<a id='172e9f8c-dc76-4118-88b6-21d1f2f88000'></a>

Proc. Natl. Acad. Sci. USA 96 (1999)

<a id='54c3a74f-9a34-4607-90b3-d66ac885c047'></a>

11353

<a id='ec8ebfd5-b3d7-41ed-8c05-bef0ec78be0e'></a>

<::transcription of the content: flowchart::>
FIG. 1. Schematic diagram of the G2DDC system showing the subsystems involving Wee1, MPF, Cdc25, and signal transduction pathways.

The flowchart illustrates the G2DDC system. At the top, "DNA damage" is indicated, which leads to the activation of "Chk1" and "p53".

- Chk1 has inhibitory effects on "active MPF" and "active Cdc25".
- p53 also has an inhibitory effect on "active MPF".

Three main components are shown in boxes:
- "active Wee1": This inhibits "active MPF".
- "active MPF": This is central to the diagram. It is inhibited by active Wee1, Chk1, and p53. It activates "active Cdc25" and is also activated by "active Cdc25" (indicated by double-headed arrows between them). Active MPF leads to "mitosis" (indicated by a downward arrow).
- "active Cdc25": This is inhibited by Chk1. It activates "active MPF" and is also activated by "active MPF" (indicated by double-headed arrows between them).
::>

<a id='0f8d3b57-3fd8-4690-a2a9-d954185ad0a2'></a>

Thr-14 residues are phosphorylated by Wee1/Myt1 kinases,
and the phosphatase Cdc25 is required to remove the phos-
phate groups from these residues and activate Cdc2. I refer the
reader to the paper of Novak and Tyson (11) for a more
detailed discussion of MPF regulation. I consider the network
given in Fig. 2, which, although simplified, is sufficient to
represent the transition between the inactive and active forms
of MPF.

<a id='d3d01da8-8302-45c0-84cb-5d2de2259e14'></a>

In Fig. 2, preMPF refers to the inactive Cdc2/cyclin B complexes that are phosphorylated on Tyr-15 and/or Thr-14, and MPF represents the active Cdc2/cyclin B. Activation of MPF from preMPF is represented by a single process (reaction 9) whose rate expression, v9, reflects the contributions of the active forms of Cdc25. The rate expression v9 is given in Table 1; there the factor {[aCdc25]+[aCdc25Ps216]} represents the total active Cdc25 (the different forms of Cdc25 will be discussed later). The active forms aCdc25 and aCdc25Ps216 are assumed to have the same activity (i.e., same value of k9 in Table 1). The second term in v9 represents Cdc25-independent pathways of MPF activation (e.g., see Zheng and Ruderman, ref. 26). The deactivation of MPF (reaction -9 in Fig. 2) is carried out by Wee1/Myt1 kinases and is given the rate expression v-9 in Table 1.

<a id='687f1fd8-0a5d-444d-bf51-de69d48400b6'></a>

Reaction 14 is a gross representation of the transcriptional and translational processes for cyclin B, as well as dimerization with Cdc2 and its phosphorylation by CDK-activating kinase, which are involved in forming the inactive preMPF. Furthermore, the translocation of MPF into the nucleus before the onset of mitosis is included in reaction 14. It is well known (11) that the activity of MPF fluctuates in cycling cells; MPF activity is low through most of interphase and increases significantly before mitosis, and then drops when mitosis

<a id='5b4761fc-c9c3-4ac1-95c0-fe7d9ba887f7'></a>

<::diagram: FIG. 2. The MPF subsystem. The reaction numbers correspond to the rate expressions in Table 1.The diagram illustrates the MPF subsystem with preMPF and MPF as key components. An arrow labeled '14' originating from 'p53' points to a horizontal bar inhibiting 'preMPF'. 'preMPF' converts to 'MPF' via an arrow labeled '9', which is positively regulated by 'active Cdc25' (dashed arrow with '+'). 'MPF' converts back to 'preMPF' via an arrow labeled '-9', which is positively regulated by 'Wee1' (dashed arrow with '+'). From 'p21', there are arrows labeled '20', '21', and '22' pointing towards it. An arrow labeled '20' originates from 'p53' (dashed arrow with '+') and points to 'p21'. 'p21' negatively regulates 'MPF' with a 'T' shaped inhibition line. 'MPF' and 'p21' combine to form 'p21/MPF' via an arrow labeled '23'. 'p21/MPF' also dissociates back into 'p21' and 'MPF' via an arrow labeled '-23'. An arrow labeled '15' originates from 'MPF' and points outwards, with a dashed arrow indicating positive regulation from 'MPF' itself.::>

<a id='b5a84ffb-d7d8-4907-ad42-cb5cd98ab76d'></a>

Table 1. Rate expressions

v₁ = k₁[Chk1][Rad3]
v₋₁ = k₋₁[Chk1P]
v₂ = k₂[Chk1P][aCdc25] + kctak₁[aCdc25]
v₋₂ = k₋₂[aCdc25Ps216]
v₂' = k₂'[Chk1P][iCdc25] + kctak₁'[iCdc25]
v₃' = k₃'[iCdc25Ps216][14-3-3]
v₋₃' = k₋₃[iCdc25Ps216/14-3-3]
v₄ = k₄
v₅ = k₅[Rad3]
v₆ = k₆[p53]
v₇ = k₇[MPF][iCdc25] + kPlk₁[iCdc25]
v₋₇ = k₋₇[aCdc25]
v₈ = k₈[MPF][Wee1] + k₈'[Wee1]
v₋₈ = k₋₈[Wee1P]
v₉ = k₉{[aCdc25] + [aCdc25Ps216]}[preMPF] + k₉'[preMPF]
v₋₉ = k₋₉[MPF][Wee1]
v₁₀ = k₁₀
v₁₁ = k₁₁[p53]
v₁₂ = k₁₂[14-3-3]
v₁₃ = k₁₃
v₁₄ = k₁₄/(1 + k₁₄'[p53])
v₁₅ = k₁₅[MPF][MPF]
v₁₆ = k₁₆
v₁₇ = k₁₇[Wee1P]
v₁₈ = k₁₈[MPF][iCdc25Ps216] + kPlk₁'[iCdc25Ps216]
v₋₁₈ = k₋₁₈[aCdc25Ps216]
v₂₀ = k₂₀[p53]
v₂₁ = k₂₁
v₂₂ = k₂₂[p21]
v₂₃ = k₂₃[MPF][p21]
v₋₂₃ = k₋₂₃[p21/MPF]

<a id='ea8a7181-91c5-4a75-a315-b7f3ee0b0772'></a>

begins. In the present work, I am not concerned with the oscillations of MPF activity; instead, we focus our attention on the G2-M transition. I make an assumption that reaction 14 is negatively regulated by p53 in accordance with the recent report of Innocente et al. (7) (see the denominator of v14 in Table 1). Note that v14 is assumed to be directly proportional to the rate of cyclin B synthesis because the level of total Cdc2 is fairly constant throughout the cell cycle. Cyclin B degradation is represented by reaction 15 with rate given by v15 in Table 1. The kinetics in v15 accounts for the fact that MPF stimulates its own degradation (11). One also could include the export of cyclin B from the nucleus, which also has been shown to affect the operation of the G2DDC (9).

<a id='649eafbf-78fd-4d22-ab25-a86775802a6d'></a>

The CDK inhibitor p21 can interact directly with MPF as represented by reactions 23 and -23. Bunz *et al.* (6) implicate p21 as a requirement to sustain G2 arrest after DNA damage. Bates *et al.* (14) also showed that p21 does contribute to a delay in G2 but suggest that the mechanism could be indirect because of the inefficient association of p21 and cyclin B1. In Fig. 2, I assume that p21 forms a complex with active MPF; it also may be possible that p21 complexes with preMPF (15) because of the observation that p21 could block the cell cycle early in G2 or late S-phase before the activation of MPF (14). In my simulations, I will assume inhibitory levels of p21 despite the knowledge that stoichiometric levels of p21 do not abolish MPF kinase activity whereas higher levels of p21 do (16, 17). There are p53-dependent and p53-independent expressions of p21 that are represented by the rates V20 and V21, respectively (see Fig. 2 and Table 1). The rate of degradation of p21 is given by V22, and the rates of reversible association of p21 with MPF are given by V23 and V-23 in Table 1.

<a id='9de31bf5-3aac-40de-8f04-83571ae2164f'></a>

The kinetic equations for the MPF subsystem are given in Table 2. To understand the intrinsic dynamics of the MPF subsystem, I integrated the differential equations involving the protein levels [preMPF], [MPF], [p21], and [p21/MPF]. Note that v9 has the factor {[aCdc25]+[aCdc25Ps216]}, which corresponds to the total activity of Cdc25 and, because of the positive feedback loop between MPF and Cdc25, is proportional to active [MPF]. Thus, to simulate the interaction of the MPF subsystem with the Cdc25 subsystem, I replace total active Cdc25 with MPF. Similarly, [Wee1] in the expression of v9 is replaced with {1/(1+[MPF])} to indicate the inhibitory effect of MPF on Wee1 and vice versa.

<a id='f86030a7-d212-42cf-b1b9-cf079960f893'></a>

Fig. 3 is a plot of the percentage of active MPF (over total
MPF measured at steady state) versus k14 (which is propor-
tional to the rate of formation of preMPF). Also shown in this
figure is the increase of [total MPF] with increasing k14.
Observe in Fig. 3 that the increase in activity of MPF does not
parallel the increase in total MPF. The figure shows a switching
threshold value of [total MPF] where a marked increase in the

<!-- PAGE BREAK -->

<a id='6b08d5ae-559c-4cb9-a97a-464c65aee350'></a>

11354 Cell Biology: Aguda

<a id='a07f439e-ee10-4b3c-9581-7c0baae88764'></a>

Proc. Natl. Acad. Sci. USA 96 (1999)

<a id='da2b3440-6ecd-4302-b54b-d5d6d8db39e8'></a>

Table 2. Kinetic equations

Signal transduction subsystem
d[Chk1P]/dt = V1 - V-1
d[Rad3]/dt = V4 - V5
d[p53]/dt = V10 - V11

MPF subsystem
d[preMPF]/dt = V14 + V-9 - V9
d[MPF]/dt = V9 + V-23 - (V-9 + V23 + V15)
d[p21]/dt = V20 + V21 + V-23 - (V22 + V23)
d[p21/MPF]/dt = V23 - V-23

Cdc25 subsystem
d[iCdc25]/dt = V-7 + V-3' - (V7 + V2')
d[iCdc25Ps216]/dt = V2' + V-18 - (V18 + V3')
d[iCdc25Ps216/14-3-3]/dt = V3' - V-3'
d[aCdc25]/dt = V7 + V-2 - (V-7 + V2)
d[aCdc25Ps216]/dt = V2 + V18 - (V-2 + V-18)
d[14-3-3]/dt = V6 + V13 + V-3' - (V3' + V12)

Wee1 subsystem
d[Wee1]/dt = V16 + V-8 - V8
d[Wee1P]/dt = V8 - (V-8 + V17)

The rate expressions ViS are given in Table 1.

<a id='3dca4764-55fb-4dcf-ba65-a3cfa2ab5834'></a>

activity of MPF occurs. Note that when log k₁₄ has the value
of about -3, practically all of MPF is active.

<a id='ea9d03a1-dce7-4c51-bfa8-1b217c09688f'></a>

The protein p53 affects the MPF subsystem through v20 (corresponding to the expression of p21) and through the negative regulation of cyclin B expression as represented in v14. The effect of these p53 pathways on MPF will be shown later.

<a id='5486de07-b312-40c9-9bf4-56b44b85a3fd'></a>

The Cdc25 Subsystem

Recent reports on the G2DDC points to Cdc25 as an impor- tant link with the cell cycle (3, 5). Important details of Cdc25 regulation are summarized in Fig. 4. The inactive form of Cdc25 (symbolized by *i*Cdc25) is hypophosphorylated and active Cdc25 (symbolized by *a*Cdc25) is obtained after further phosphorylation by the kinase Plk1 (18) and by MPF itself (13, 19). Thus, reaction 7 is given the expression v7 in Table 1. I will assume that [Plk1] is constant and is subsumed in the param- eter kPlk1.

<a id='a0f8c3a3-4266-49b8-b813-5a60c3a61046'></a>

When Cdc25 is phosphorylated on Ser-216, it was shown that 14–3–3 proteins bind with Cdc25 (3, 5, 20–22). Ser-216 phosphorylation of Cdc25 has been shown to be carried out by kinases CTAK1 (23) and Chk1 (22, 24) in vitro. [Recently, Matsuoka, Huang, and Elledge (25) identified Chk2, which, in vitro, could phosphorylate Cdc25 on Ser-216; I will not include

<a id='929d160b-f1cc-42d5-a0ca-ce8545b29ef1'></a>

<::line chart::> A line graph titled "Percentage of active MPF (curve a) and total MPF (curve b) versus log k14, the rate of expression of preMPF." The Y-axis is labeled "% active MPF & Total MPF" and ranges from 0 to 100. The X-axis is labeled "log k14" and ranges from -8 to -2. Curve 'a' (Percentage of active MPF) starts at approximately 10% at log k14 = -8, remains relatively flat, then rises sharply from approximately log k14 = -5 to -4, reaching nearly 100% by log k14 = -3. Curve 'b' (Total MPF) starts near 0% at log k14 = -8, remains very low, then rises sharply from approximately log k14 = -4 to -2, reaching nearly 100% by log k14 = -2.<::FIG. 3. Percentage of active MPF (curve a) and total MPF (curve b) versus log k14, the rate of expression of preMPF. Protein levels are measured at steady state and are dimensionless. Parameter values (dimensionless): k9 = k.9 = k.9′ =1.0, k9′ = k20[p53] = k22 =0.1, k15 =10-6, k21 = 0.01, k23 = k-23 =0.0. All integrations carried out in this paper use the routine LSODE (35).

<a id='4d4bae3a-fa6b-4699-b93d-b75211f336ad'></a>

<::FIG. 4. The Cdc25 subsystem. The reaction numbers correspond to the rate expressions in Table 1.: diagram::>The diagram illustrates the Cdc25 subsystem, showing the interconversion between different states of Cdc25 and its regulation. The key components are: aCdc25, aCdc25Ps216, iCdc25, iCdc25Ps216, and iCdc25Ps216/14-3-3. 14-3-3 is also shown as a separate entity.The transitions and regulatory interactions are as follows:1.  **aCdc25 and iCdc25 Interconversion:**-   aCdc25 converts to iCdc25 via reaction -7, influenced by MPF and Plk1.-   iCdc25 converts to aCdc25 via reaction 7, influenced by MPF and Plk1.2.  **Phosphorylation at Ser216:**-   aCdc25 converts to aCdc25Ps216 via reaction 2, influenced by C-TAK1 and Chk1P.-   aCdc25Ps216 converts back to aCdc25 via reaction -2.-   iCdc25 converts to iCdc25Ps216 via reaction 2', influenced by C-TAK1 and Chk1P.-   iCdc25Ps216 converts back to iCdc25 via reaction -2'.3.  **Interconversion between phosphorylated forms:**-   aCdc25Ps216 converts to iCdc25Ps216 via reaction -18, influenced by MPF and Plk1.-   iCdc25Ps216 converts to aCdc25Ps216 via reaction 18, influenced by MPF and Plk1.4.  **14-3-3 Binding:**-   iCdc25Ps216 converts to iCdc25Ps216/14-3-3 via reaction 3'.-   iCdc25Ps216/14-3-3 converts back to iCdc25Ps216 via reaction -3'.5.  **Regulation of 14-3-3:**-   14-3-3 is formed or activated by inputs labeled 12 and 13.-   p53 influences 14-3-3 via reaction 6.

<a id='70279177-7131-4af5-b266-131008282185'></a>

this information in my present model.] Although I will assume it in my modeling of the G2DDC, it has not been demonstrated in vivo that Cdc25 phosphorylation on Ser-216 actually occurs in response to DNA damage. The rate expressions for Ser-216 phosphorylation of iCdc25 and aCdc25 are given by V2 and V2' in Table 1. It is assumed that the Ser-216-phosphorylated inactive Cdc25 (symbolized by iCdc25Ps216) still can be activated by MPF and Plk1 as represented by reaction 18 with rate V18 in Table 1.

<a id='93ccf331-d813-472e-84ce-a49a2a031520'></a>

In accordance with the experiments of Kumagai et al. (20),
I will assume that 14-3-3 proteins can bind only to the
Ser-216-phosphorylated inactive form of Cdc25; the rate of
this binding is given by v3 in Table 1. I also assume that
iCdc25Ps16/14-3-3 is dephosphorylated at Ser-216 after
which 14-3-3 and iCdc25 are separated (4); this process has
the rate v-3 given in Table 1. The rate expressions for the
dephosphorylation processes -7, -2, and -18 are given in
Table 1.

<a id='ab7edb98-cc8c-46f3-b211-e6d5a731f3a2'></a>

The last member of this subsystem are the 14-3-3 proteins. According to Hermeking et al. (12), 14-3-3σ are strongly induced after γ-irradiation and by other DNA damaging agents, and the induction depends on p53; the rate of this process is given by v6 in Table 1. Lastly, in this subsystem, v13 is the rate of p53-independent expression of 14-3-3 proteins and v12 is their rate of degradation (see Table 1). I have not included in the present subsystem analysis the effect of 14-3-3 proteins on the intracellular localization of Cdc25 (4, 8) but will do so later in the simulation of the whole checkpoint system.

<a id='b6e13265-b26a-40f2-8796-7de9555b2741'></a>

It has been reported that total Cdc25 levels do not vary significantly during the cell cycle (27). This statement is not true for the nuclear levels of Cdc25 (8) but for the present subsytem analysis I initially assume that the sum of all different species of Cdc25 is constant. The DNA damage signal through the Chk1 pathway affects v2 and v2', and the p53 pathway affects v6 (see Fig. 4). Note that v7 and V18 are proportional to [MPF], which, in the present analysis of this isolated subsystem, is replaced by the total active Cdc25, i.e., {[aCdc25]+[aCdc25Ps216]}, to account for the positive feedback loop between Cdc25 and MPF.

<a id='d127276d-5cb0-40af-a0f7-961f09090cdd'></a>

To understand the intrinsic kinetics of the Cdc25 subsystem,
the differential equations involving [iCdc25], [iCdc25Ps216],
[iCdc25Ps216/14-3-3], [aCdc25], [aCdc25Ps216], and [14-3-
3] found in Table 2 are integrated. Fig. 5 shows a plot of the
percentage of active Cdc25 (i.e., {[aCdc25] + [aCdc25Ps216]})
versus [total Cdc25]. The effect of two different strengths of
the DNA damage signal influencing rates v2 and v2' via Chk1
are shown in Fig. 5 where curve b corresponds to a 100-fold
increase in the signal strength over that of curve a. Fig. 5
demonstrates that the percentage of active Cdc25 depends on
[total Cdc25] and the strength of the damage signal. For
example, when [total Cdc25] = 5 (see Fig. 5), a 100-fold
increase in the damage signal decreases the activity from 50%
to 3%. Increased [total Cdc25] renders the system less sensitive
to the damage signal.

<!-- PAGE BREAK -->

<a id='91eff7ee-94be-4f4a-b2ab-f62fb68366d4'></a>

Cell Biology: Aguda<::chart: line graph::
FIG. 5. Percentage of active Cdc25 (measured at steady state) versus total Cdc25. The y-axis is labeled "% active Cdc25" and ranges from 0 to 80. The x-axis is labeled "[total Cdc25]" and ranges from 0 to 30. Two curves are plotted:
- Curve a: Shows a steep increase in % active Cdc25, starting around 10% at total Cdc25 = 0, rising to about 50% at total Cdc25 = 5, and then gradually increasing to approximately 73% at total Cdc25 = 30.
- Curve b: Shows a delayed and less steep increase in % active Cdc25, remaining near 0% until total Cdc25 is around 10, then rising to approximately 53% at total Cdc25 = 30.
Curve b corresponds to a 100-fold increase in the DNA damage signal strength over that of curve a. Parameter values (dimensionless) for curve a: k₂([Chk1P]+[CTAK1]) = kPlk1 = k₁₂ = kPlk1' = 0.1, k₋₂ = k₋₃' = k₋₇ = k₋₁₈ = k₆[p53] = 0.01, k₂'([Chk1P]+[CTAK1]) = k₃' = k₇ = k₁₃=k₁₈=1.0. Parameter values for curve b are exactly the same as those of curve a except k₂([Chk1P]+[CTAK1]) = 10 and k₂'([Chk1P]+[CTAK1]) = 100.::>

<a id='934f5843-64d1-495f-adaf-4478816b222b'></a>

## The Wee1 Subsystem

This subsystem is shown in Fig. 6. Observed levels of Wee1 proteins (13) do not allow us to assume that the total Wee1 is constant and therefore I introduce reactions 16 (Wee1 expression) and 17 (Wee1 degradation) with rates v16 and v17, respectively (see Table 1). It has been observed that Wee1 is transiently hyperphosphorylated during M-phase and then degraded (see ref. 13 and references therein). In a recent paper, Michael and Newport (28) showed that Wee1 was degraded in a Cdc34-dependent manner (in Xenopus egg extracts); furthermore, those authors concluded that Wee1 degradation is required for entry into mitosis and that this degradation is inhibited when DNA replication is blocked.

<a id='67082e28-f5d0-4360-9038-0f38f563065f'></a>

The regulation of the activity of Wee1 by MPF (13) is represented by the first term in the rate v8 in Table 1. Although Chk1 has been shown to phosphorylate Wee1 in vitro (29), this phosphorylation does not alter Wee1 activity toward Cdc2; hence, Chk1 is not assumed to affect process 8. The second term in the expression for v8 accounts for MPF-independent phosphorylation of Wee1. The dephosphorylation of Wee1P (hyperphosphorylated form of Wee1) is assumed to occur with the rate v-8 in Table 1.

<a id='c0aa26ae-b180-4e0c-b92e-521fca9ea706'></a>

The kinetic equations of the Wee1 subsystem are given in
Table 2. Because the DNA damage signal via either Chk1 or
p53 pathway does not affect v8 or V-8, an analysis of the effect
of the DNA damage signal on the Wee1 subsystem separate
from the MPF or Cdc25 subsystems is not necessary. Indeed,
my previous mathematical analysis of the coupling between the
MPF and Wee1 subsystems (31) has suggested that Wee1 may
not be an essential target of Chk1.

<a id='a85c0f4e-4006-4825-ade6-105786d38a38'></a>

The DNA Damage Signal Transduction Subsystems G₂ DNA damage signal transduction includes the Rad3/Chk1 and the p53 pathways (see Fig. 7). These pathways impinge on <::MPF, indicated by a dashed arrow and a '+' sign, activates the conversion of Wee1 to Wee1P (reaction 8). Wee1 is also formed from an input (reaction 16). Wee1P is converted back to Wee1 (reaction -8) and also has an output (reaction 17). FIG. 6. The Wee1 subsystem. The reaction numbers correspond to the rate expressions in Table 1.: diagram::>

<a id='5a98fca8-475c-4b2c-aa9d-9aa5af8a94b2'></a>

Proc. Natl. Acad. Sci. USA 96 (1999) 11355

<::flowchart
- DNA damage is shown at the top, represented by two asterisk-like symbols.
- From DNA damage, a dashed arrow labeled "4" points to "Rad3/ATM".
- From DNA damage, a dashed arrow labeled "10" points to "p53".
- From Rad3/ATM, an arrow labeled "5" points left.
- From Rad3/ATM, a dashed arrow with a plus sign (indicating activation) points downwards to influence the Chk1/Chk1P cycle.
- A curved arrow labeled "1" goes from "Chk1" to "Chk1P".
- A curved arrow labeled "-1" goes from "Chk1P" back to "Chk1".
- From p53, an arrow labeled "11" points downwards and to the right.

FIG. 7. DNA damage signal transduction pathways. The reaction numbers correspond to the rate expressions in Table 1.
: flowchart::>

<a id='c16da384-c56e-4270-98f3-a0d5166c0a99'></a>

the subsystems described above. The Rad3/Chk1 pathway is
still poorly understood, and other proteins that could be
involved are still being identified (4). In humans, Rad3 ho-
mologs are the _ataxia telan-giectasia mutated_ (ATM) and
ATM-related kinases. Recent results suggest that the Rad
proteins are activated as a result of DNA damage and act
upstream of Chk1. Chk1 is found to be phosphorylated as a
result of the damage signal (22, 24, 32).

<a id='25ccf827-96d5-4115-bef9-0315262a2257'></a>

I will assume in my model that Rad3/ATM protein is activated at some fixed rate v4 because of DNA damage. This protein is assumed degraded at a rate v5 (see Table 1). It also is assumed that a fixed level of total Chk1 exists. Recent work of Matsuoka, Huang, and Elledge (25) also has pointed to another protein kinase, Chk2, which also phosphorylates Cdc25; for simplicity, I will not include Chk2 in my present model.

<a id='ad4d6f12-f0a0-4544-9525-c9b7d5f6f272'></a>

The other important member of the damage signal transduction is p53. It is well known that G1 arrest involves p53 as a major player (33). Recent work of Hermeking et al. (12) showed that the induction of 14-3-3 proteins is mediated by p53; and recent experiments of Bunz et al. (6) have shown that, indeed, p53 is also important in G2 arrest of the cell cycle. I will assume that because of DNA damage, p53 is activated at the rate v10 (see Table 1) and degraded or inactivated at the rate v11. Recent results (30, 34) suggest that ATM also could contribute to the phosphorylation of p53 in vivo; thus, the Rad3/Chk1 and p53 pathways could be coupled but, for simplicity, my computer simulations assume otherwise.

<a id='964a3951-74ef-4b34-a352-efdd177447ec'></a>

Kinetics of the Checkpoint System

The entire set of differential equations representing the kinetics of the coupled subsystems is given in Table 2. In the integration and computer simulations of the whole G2DDC system, and as far as understanding the qualitative dynamical behavior of the system, I have assumed that the effects of Plk1 and CTAK1 can be ignored. To simulate the intracellular distribution of Cdc25, I have included a rate vex for the nuclear export of 14-3-3-bound Cdc25 (see ref. 8), and a rate vin for the rate of nuclear import of iCdc25 (see Fig. 8 for expressions of vex and vin).

<a id='17173a7e-c786-4b63-8005-3fc0b702ddc2'></a>

Fig. 8 gives the temporal variations of MPF, Wee1, and total active Cdc25 in the absence of DNA damage. As foreshadowed by the schematic diagram given in Fig. 1, Wee1 decreases sharply as soon as MPF starts increasing autocatalytically. Increasing MPF activity leads to increased phosphorylation and degradation of Wee1 (reactions 8 and 17 in Fig. 6). This result agrees well with Michael and Newport (28) who suggested that Wee1 degradation is a prerequisite for entry into mitosis. Another interesting feature of the kinetics shown in Fig. 8 is the identical switch-on time for the activities of MPF and Cdc25, which is caused by the positive feedback loop

<!-- PAGE BREAK -->

<a id='13076e96-d86c-4ab1-b02e-3c5dc09a138f'></a>

11356 Cell Biology: Aguda

<a id='48fc2872-f3a5-47a3-94a7-6cb9f6646649'></a>

Proc. Natl. Acad. Sci. USA 96 (1999)

<a id='bec120fd-0b78-46ed-bb3d-5203141d1abe'></a>

<::chart: line graph::>The chart displays protein levels over time. The x-axis is labeled "time" and ranges from 0 to 4000. The y-axis is labeled "protein levels" and ranges from 0 to 0.5. Three lines are plotted:
1. A thin line labeled "Wee1" starts at 0, rises to a peak of approximately 0.27 around time 1400, and then declines to near zero.
2. A thick line labeled "MPF" starts at 0, sharply increases to a peak of approximately 0.47 around time 1900, and then decreases to stabilize around 0.23.
3. A thin line labeled "total aCdc25" starts at 0, rises to a small peak of approximately 0.02 around time 1900, and then decreases to stabilize around 0.01.

FIG. 8. Active MPF, total active Cdc25, and Wee1 as a function of time. No DNA damage is assumed here, i.e., k₄ = k₁₀ = 0. Nuclear export of iCdc25Ps216/14–3–3 has the rate vₑₓ = kₑₓ[iCdc25Ps216/14–3–3] with kₑₓ = 1, and nuclear import of iCdc25 has the rate vᵢₙ = 10⁻⁵. Each of the following parameters has the value 1.0: k₁, k₅, k₇, k₁₈, k₉, k₁₁, k₁₃, k₋₈, k₋₉, k₋₂₃, k₁₄′; each of the following is equal to 0.1: k₈, k₁₂, k₂₂, k₂₃, k₂₀; each of the following is equal to 0.01: k₆, k₁₇, k₂, k₂′, k₋₂, k₋₇, k₋₁₈, k₂₁; the following are set to zero: kₚₗₖ₁, kₚₗₖ₁′, k꜀ₜₐₖ₁, k꜀ₜₐₖ₁′, k₈′, k₉′, k₋₃′; k₋₁ = 10; k₁₄ = 5 × 10⁻⁴; k₁₅ = 10⁻²; k₁₆ = 2 × 10⁻⁴; k₃′ = 100; [totalChk1] = 1. Initial conditions: [Chk1P] = [iCdc25] = [aCdc25] = [preMPF] = 10⁻⁶; [MPF] = 10⁻⁸; [iCdc25Ps216] = 2 × 10⁻⁵; [Wee1] = 10⁻³; [iCdc25Ps216/14–3–3] = 0.03; [14–3–3] = 2; all other species are zero. All parameters and variables are dimensionless. 

<a id='79c4f827-9fca-4104-b36e-fdc5484c3225'></a>

between these two proteins (and is reminiscent of the phe-
nomenon of transcritical bifurcation explained in ref. 31).
To simulate the DNA damage signal transduction, I inves-
tigated the individual as well as combined effects of the
Rad3/Chk1 pathway and the p53 pathway on the activation of
MPF. Activation of p53 is assumed to increase the rates of
reactions 20 and 6 (see Figs. 2 and 4, respectively) and decrease
the rate of process 14 (see Fig. 2). The values of the parameters
k20, k6 and k14' associated with the p53 pathway were assigned
arbitrarily (see Fig. 8 for values) because no experimental
measurements are available. Fig. 9 shows the activity of MPF
when there is no DNA damage (curve 1), when only the
Rad3/Chk1 pathway is operational (curve 2), when only the
p53 pathway is operational (curve 3), and when both pathways
are operational (curve 4). The simulations in Fig. 9 were
performed to demonstrate a possible explanation of the ex-
periments reported by Bunz et al. (6) regarding the necessity

<a id='da1b8761-7ba1-4396-9f12-c498555957e9'></a>

<::chart: line graph::>FIG. 9. Effect of the DNA damage signal transduction pathways on MPF. The x-axis is labeled "time" and ranges from 0 to 10000. The y-axis is labeled "[MPF]" and ranges from 0 to 1. Four curves are plotted: Curve 1 (dashed line) shows MPF peaking around 0.45 at time ~2000, then settling around 0.25. Curve 2 (solid line) shows MPF staying at 0 until ~6000, then sharply peaking at 1 at time ~6500, and settling around 0.25. Curve 3 (solid line) shows MPF peaking around 0.4 at time ~2000, then settling around 0.2. Curve 4 (solid line, indicated by an arrow) shows MPF staying at 0 throughout the entire time range. Curve 1: no DNA damage, k₄ = k₁₀ = 0; curve 2: Chk1 pathway is on, p53 pathways are off, k₄ = 0.2, k₁₀ = 0; curve 3: p53 pathways are on, Chk1 pathway is off, k₄ = 0, k₁₀ = 0.2; curve 4: both Chk1 and p53 pathways are on, k₄ = k₁₀ = 0.2. Other parameters and initial conditions are the same as in Fig. 8.

<a id='c8eeabfc-ab21-4236-8cb1-b617d9d72f99'></a>

of p53 in sustaining G2 cell cycle arrest after DNA damage. With the parameter values chosen for Fig. 9, the DNA damage signal through the Rad3/Chk1 pathway generates a substantial delay in the switch-on time for MPF (curve 2). However, this delay leads to a doubling of the MPF peak activity (compared with that of curve 1), which then could allow the cell to overcome the G2 delay. Although the choice of parameters for the p53 signal transduction pathway results only in a minor disturbance on MPF activity (curve 3), coupling between the p53 pathway and the Rad3/Chk1 pathway leads to the abrupt disappearance of MPF activity and hence a sustained G2 arrest (curve 4).

<a id='7b0f0d34-2a5e-4dfa-8b83-cc190f2513b8'></a>

## Conclusions

I have presented a detailed model of the G2DDC system based on known or postulated pathways reported in the current literature. A major difficulty in a kinetic study of this complex system is that practically no data on the rate parameters are available, which would render such a quantitative modeling task seemingly pointless. Nevertheless, an important question that could be decided by my detailed G2DDC model is whether or not there exists a set of kinetic parameters that could generate all the well-established experimental behavior of the system. If no such set of parameters exists, then the model must be modified by adding other necessary pathways and/or deleting questionable ones. This is really an essential objective that was carried out in my initial study of the detailed model presented here.

<a id='965642b1-df70-4b20-a730-7d9cd3a60da5'></a>

I have shown (Fig. 8) that, because of the mutual negative regulation of each other's activities, Weel's degradation is necessary for MPF's activation and subsequent entry into mitosis, in accordance with the report of Michael and Newport (28). I also have demonstrated (Fig. 9) that, under certain parameter values, a G2 arrest after DNA damage cannot be sustained by the Rad3/Chk1 pathway without the help of the p53 pathway, in agreement with the experiments of Bunz et al. (6); however, this may only be a special case because my detailed model suggests several points where the checkpoint signal transduction pathways could impinge on the intrinsic G2-M cell cycle machinery and the efficacy of these pathways in generating a G2 arrest could vary according to cell types and other conditions. For example, the Rad3/Chk1 pathway alone can shut off MPF activity by increasing the value of the parameter k4 in Fig. 9. As shown in Figs. 2 and 4, points where the DNA damage signal would influence the cell cycle include reactions 2, 2', 6, 20, and 14.

<a id='4f594b66-339b-4bc4-91f0-1a321cd9e36d'></a>

Despite the complexity of the different subsystems of the G2DDC, understanding the switching behavior of this checkpoint system is facilitated by analyzing the consequences of the positive coupling between the phosphorylation-dephosphorylation (PD) cycles of MPF and Cdc25. In an earlier analysis of the G2DDC (31), I emphasized the importance of the existence of a transcritical bifurcation point inherent in the coupling between these PD cycles; this bifurcation point gives a threshold value above which both activities of MPF and Cdc25 are switched on at the same time, as seen in Fig. 8. According to ref. 31, the transcritical bifurcation point is given by a critical value of the product p = [total MPF] × [total Cdc25] where values inside the square brackets are total concentrations. The critical value of p is a function of the kinetic parameters involved in the PD cycles of MPF and Cdc25. If either [total MPF] or [total Cdc25] decreases so that their product p is less than the critical value, then both activities of MPF and Cdc25 are turned off. Thus, the nuclear export of 14-3-3-bound Cdc25 could lead to a subcritical value of p in the nucleus and turns MPF activity off, in agreement with Lopez-Girona et al. (8). The observation of Toyoshima et al. (9) on the nuclear export of cyclin B1 and its role in the G2DDC is also readily explained by the resulting decrease in

<!-- PAGE BREAK -->

<a id='449b05cd-a2ce-4948-a3df-592915016334'></a>

Cell Biology: Aguda

<a id='3bad5ad9-3e07-441a-b06f-5f69a5afe9cd'></a>

Proc. Natl. Acad. Sci. USA 96 (1999)

<a id='54137ee7-946f-4b29-8eff-838dde7ded90'></a>

11357

<a id='c1a07c93-7bce-40c9-a07a-1b0f707dbefb'></a>

total MPF, which would lower _p_ below its critical value. Lastly,
the recent report of Innocente _et al._ (7) on the negative
regulation of cyclin B1 expression by p53 (leading to a decrease
in total MPF in the nucleus), which induces a G2 arrest, also
could be explained in terms of a resulting subcritical value of
the product _p_. It would be very interesting if such a critical
value of _p_ can be experimentally demonstrated to exist.

<a id='e68e9f77-551d-4b98-bc6f-e4e5a9eb7a7a'></a>

I thank Paul Graves for stimulating discussions and helpful com-
ments. This work is supported by a grant from the Natural Sciences and
Engineering Research Council of Canada and a Laurentian University
Research Fund grant.

1. Elledge, S. J. (1996) Science **274**, 1664–1672.
2. Murray, A. & Hunt, T. (1993) *The Cell Cycle* (Freeman, New
York).
3. Nurse, P. (1997) *Cell* **91**, 865–867.
4. Russell, P. (1998) *Trends Biochem. Sci.* **23**, 399–402.
5. Weinert, T. (1997) *Science* **277**, 1450–1451.
6. Bunz, F., Dutriaux, A., Lengauer, C., Waldman, T., Zhou, S.,
Brown, J. P., Sedivy, J. M., Kinzler, K. W. & Vogelstein, B. (1998)
*Science* **282**, 1497–1501.
7. Innocente, S. A., Abrahamson, J. L. A., Cogswell, J. P. & Lee,
J. M. (1999) *Proc. Natl. Acad. Sci. USA* **96**, 2147–2152.
8. Lopez-Girona, A., Furnari, B., Mondesert, O. & Russell, P.
(1999) *Nature* (London) **397**, 172–175.
9. Toyoshima, F., Moriguchi, T., Wada, A., Fukuda, M. & Nishida,
E. (1998) *EMBO J.* **17**, 2728–2735.
10. Feinberg, M. & Horn, F. J. M. (1974) *Chem. Eng. Sci.* **29**, 775.
11. Novak, B. & Tyson, J. J. (1993) *J. Cell Sci.* **106**, 1153–1168.
12. Hermeking, H., Lengauer, C., Polyak, K., He, T.-C., Zhang, L.,
Thiagalingam, S., Kinzler, K. W. & Vogelstein, B. (1997) *Mol.*
*Cell* **1**, 3–11.
13. Poon, R. Y. C., Chau, M. S., Yamashita, K. & Hunter, T. (1997)
*Cancer Res.* **57**, 5168–5178.
14. Bates, S., Ryan, K. M., Phillips, A. C. & Vousden, K. H. (1998)
*Oncogene* **17**, 1691–1703.

<a id='b3001025-4387-4073-99b3-3a368b6c37f3'></a>

15. Cai, K. & Dynlacht, B. D. (1998) Proc. Natl. Acad. Sci. USA **95**,
12254–12259.
16. Pines, J. (1997) Biochim. Biophys. Acta **1332**, M39–M42.
17. Harper, J. W. (1997) Cancer Surv. **29**, 91–107.
18. Kumagai, A. & Dunphy, W. G. (1996) Science **273**, 1377–1380.
19. Izumi, T. & Maller, J. L. (1993) Mol. Biol. Cell **4**, 1337–1350.
20. Kumagai, A., Yakowec, P. S. & Dunphy, W. G. (1998) Mol. Biol.
Cell **9**, 345–354.
21. Peng, C.-Y., Graves, P. R., Thoma, R. S., Wu, Z., Shaw, A. S. &
Piwnica-Worms, H. (1997) Science **277**, 1501–1505.
22. Sanchez, Y., Wong, C., Thoma, R. S., Richman, R., Wu, Z.,
Piwnica-Worms, H. & Elledge, S. J. (1997) Science **277**, 1497–
1501.
23. Peng, C.-Y., Graves, P. R., Ogg, S., Thoma, R. S., Byrnes, M. J.,
Wu, Z., Stephenson, M. T. & Piwnica-Worms, H. (1998) Cell
Growth Differ. **9**, 197–208.
24. Furnari, B., Rhind, N. & Russell, P. (1997) Science **277**, 1495–
1497.
25. Matsuoka, S., Huang, M. & Elledge, S. J. (1998) Science **282**,
1893–1897.
26. Zheng, X.-F. & Ruderman, J. V. (1993) Cell **75**, 155–164.
27. Girard, F., Strausfeld, U., Cavadore, J.-C., Russell, P., Fernan-
dez, A. & Lamb, N. J. C. (1992) J. Cell Biol. **118**, 785–794.
28. Michael, W. M. & Newport, J. (1998) Science **282**, 1886–1889.
29. O'Connell, M. J., Raleigh, J. M., Verkade, H. M. & Nurse, P.
(1997) EMBO J. **16**, 545–554.
30. Banin, S., Moyal, L., Shieh, S.-Y., Taya, Y., Anderson, C. W.,
Chessa, L., Smorodinsky, N. I., Prives, C., Reiss, Y., Shiloh, Y. &
Ziv, Y. (1998) Science **281**, 1674–1677.
31. Aguda, B. D. (1999) Oncogene **18**, 2846–2851.
32. Walworth, N. C. & Bernards, R. (1996) Science **271**, 353–356.
33. Carr, A. M. (1996) Science **271**, 314–315.
34. Canman, C. E., Lim, D.-S., Cimprich, K. A., Taya, Y., Tamai, K.,
Sakaguchi, K., Appella, E., Kastan, M. B. & Siliciano, J. D. (1998)
Science **281**, 1677–1679.
35. Hindmarsch, A. C. (1980) ACM Signum Newslett. **15**, 10.
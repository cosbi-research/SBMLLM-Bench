<a id='da35a675-9fe7-4b79-b047-d44b429b80d9'></a>

BioSystems 103 (2011) 384–391

<a id='70dc9e47-2f0a-4a46-84c6-c88ac4dd2b08'></a>

<::logo: Elsevier
NON SOLLUS
The logo features a detailed illustration of a tree with a figure tending to it, and a banner with text, all above the company name in orange text.::>

<a id='cb846046-37ca-490a-a184-9d81deb90e27'></a>

Contents lists available at ScienceDirect

<a id='775ce903-0cfa-41e5-84af-aea62712c964'></a>

BioSystems

<a id='59308fec-deaa-4e21-8423-4816e81f5dba'></a>

journal homepage: www.elsevier.com/locate/biosystems

<a id='20d12b79-ac18-4c17-846b-3a5a57385216'></a>

Elsevier

<::transcription of the content
: illustration::>

Bio Systems
Journal of Biological and Informative Processing Science

<a id='e76b7673-e62e-4c25-b979-b08ead452723'></a>

Mathematical modeling of cell cycle regulation in response to DNA damage:
Exploring mechanisms of cell-fate determination

<a id='ebd927b2-7341-4dd0-8d9a-1f5898fe4062'></a>

Kazunari Iwamoto a,c, Hiroyuki Hamadaa, Yukihiro Eguchib, Masahiro Okamoto a, b, *
a Laboratory for Bioinformatics, Graduate School of Systems Life Sciences, Kyushu University, 3-1-1 Maidashi, Higashi-ku, Fukuoka 812-8582, Japan
b Division of Bioprocess Design, Bio-architecture Center, Kyushu University, 6-10-1 Hakozaki, Higashiku, Fukuoka 812-8581, Japan
c Japan Society for the Promotion of Science, 8 Ichibancho, Chiyoda-ku, Tokyo 102-8472, Japan

<a id='bffecbb5-535b-469f-91db-35b0e60ca518'></a>

## ARTICLE INFO

Article history:
Received 22 September 2010
Received in revised form 9 November 2010
Accepted 15 November 2010

Keywords:
Cell fate
Whole cell cycle regulation
p53 oscillation
Cell cycle arrest

<a id='857c43cb-dce4-47f7-b922-4d20b3721bbe'></a>

ABSTRACT
After DNA damage, cells activate p53, a tumor suppressor gene, and select a cell fate (e.g., DNA repair, cell cycle arrest, or apoptosis). Recently, a p53 oscillatory behavior was observed following DNA damage. However, the relationship between this p53 oscillation and cell-fate selection is unclear. Here, we present a novel model of the DNA damage signaling pathway that includes p53 and whole cell cycle regulation and explore the relationship between p53 oscillation and cell fate selection. The simulation run without DNA damage qualitatively realized experimentally observed data from several cell cycle regulators, indicating that our model was biologically appropriate. Moreover, the comprehensive sensitivity analysis for the proposed model was implemented by changing the values of all kinetic parameters, which revealed that the cell cycle regulation system based on the proposed model has robustness on a fluctuation of reaction rate in each process. Simulations run with four different intensities of DNA damage, i.e. Low-damage, Medium-damage, High-damage, and Excess-damage, realized cell cycle arrest in all cases. Low-damage, Medium-damage, High-damage, and Excess-damage corresponded to the DNA damage caused by 100, 200, 400, and 800J/m² doses of UV-irradiation, respectively, based on expression of p21, which plays a crucial role in cell cycle arrest. In simulations run with High-damage and Excess-damage, the length of the cell cycle arrest was shortened despite the severe DNA damage, and p53 began to oscillate. Cells initiated apoptosis and were killed at 400 and 800J/m² doses of UV-irradiation, corresponding to High-damage and Excess-damage, respectively. Therefore, our model indicated that the oscillatory mode of p53 profoundly affects cell fate selection.

© 2010 Elsevier Ireland Ltd. All rights reserved.

<a id='fd7d0027-fb24-489e-946d-9f8c5ce6c7f5'></a>

## 1. Introduction
The series of reaction processes by which a parent cell divides into two daughter cells, called the cell cycle, consists of five phases, Gap1 (G1), DNA synthesis (S), Gap2 (G2), Mitosis (M), and Quiescence (G0), and has significant influence on cellular dynamics, including cell proliferation and differentiation (Tessema et al., 2004). Although most mammalian cells normally remain in a resting state, either G0 phase or early G1 phase, the cell cycle progresses to S phase beyond the restriction point when particular growth factors stimulate a cell sufficiently. After DNA replication during S phase, the cell cycle progresses through G2 phase to M phase. During M phase, the cell divides into two daughter cells, which

<a id='19bf0916-4974-411b-b2d2-90cf61fd2cda'></a>

--- 
* Corresponding author at: Laboratory for Bioinformatics, Graduate School of
Systems Life Sciences, Kyushu University, 3-1-1 Maidashi, Higashi-ku, Fukuoka 812-
8582, Japan. Tel.: +81 092 642 6691; fax: +81 092 642 6744.
E-mail address: okahon@brs.kyushu-u.ac.jp (M. Okamoto).

<a id='9b708926-5fe6-46ca-b8b7-07ef656751fd'></a>

0303-2647/$- see front matter © 2010 Elsevier Ireland Ltd. All rights reserved.
doi:10.1016/j.biosystems.2010.11.011

<a id='f2a3d3ee-a51a-4b09-aedc-adb5cabc694a'></a>

represents completion of cell cycle progression. Such cell cycle progression is precisely regulated by several complicated networks which consist of diverse biochemical species, such as genes and proteins (Kohn, 1999). In these networks, the most essential biochemical species are cyclin-dependent kinases (Cdk), which bind to cyclins (Cyc) and form binary Cyc/Cdk complexes, some of which are dephosphorylated and activated by the phosphatase, cell division cycle (CDC)25. The expression of different types of Cycs and Cdks plays an important role in cell cycle progression (Hochegger et al., 2008). Specifically, CycD, induced by cell growth factors, activates Cdk4 (CycD/Cdk4) in early G1 phase, and CycE activates Cdk2 (CycE/Cdk2) between late G1 phase and S phase (G1/S phase). Subsequently, CycA activates Cdk2 (CycA/Cdk2) between late G1 phase and early M phase, and CycB activates Cdk1 (CycB/Cdk1) between G2 phase and M phase (G2/M phase). Additionally, activation of these Cyc/Cdk complexes is counteracted by several types of Cdk inhibitors (CKI), including p16, p21, and p27, halting cell cycle progression. Although p16 inhibits the activation of CycD/Cdk4 specifically, both p21 and p27 suppress activation of

<!-- PAGE BREAK -->

<a id='0e2c6fd5-d4ed-4631-a8a2-2c4060d80188'></a>

K. Iwamoto et al. / BioSystems 103 (2011) 384–391

<a id='0f9f2249-2065-482f-b1b3-55cefd4e6c92'></a>

385

<a id='7eab92aa-d934-4d5f-94a4-4c4e2ff24794'></a>

multiple Cyc/Cdk complexes (Ragione et al., 1996; Xiong et al., 1993; Toyoshima and Hunter, 1994). Thus, cell cycle progression is regulated by sophisticated mechanisms involving many chemical species, including Cycs, Cdks, and CKIs.

<a id='23092966-a56d-4224-9cf4-8bdd563ae3e0'></a>

Cells are often damaged by ultraviolet (UV)-irradiation, ionization-radiation (IR), or toxic chemical species that can cause breaks in double-stranded DNA. When DNA is damaged, a DNA damage signal activates a DNA damage signaling pathway. To repair the damaged DNA, the signaling pathway interacts with the cell cycle regulation mechanism and temporarily arrests cell cycle progression as follows: (Iliakis et al., 2003) (1) DNA damage activates both Ataxia telangiectasia mutated (ATM) and Rad3-related (ATR) protein kinases, (2) ATM and ATR activate p53 and checkpoint kinase 1 (Chk1), (3) activated p53 promotes the synthesis of p21 and 14-3-3σ, (4) Chk1 phosphorylates Cdc25, which binds to 14-3-3σ (14-3-3σ/Cdc25), (5) p21 binds to Cyc/Cdk complexes, inducing cell cycle arrest, (6) the 14-3-3σ/Cdc25 complex moves to the cytoplasm, also inducing cell cycle arrest. Thus, the DNA damage signaling pathway directly acts on the cell cycle regulation mechanism, contributing to cellular homeostasis and genetic stability. Moreover, cells with severe DNA damage may induce apoptosis and execute programmed cell death (Li and Ho, 1998; Roos and Kaina, 2006).

<a id='68a4617e-d8af-4195-9ffa-ed59959def13'></a>

These biological findings suggest that cells can evaluate the intensity of DNA damage and select an appropriate cell fate, such as DNA repair, cell cycle arrest, or apoptosis. However, it is unclear how the cell determines the appropriate cell fate. A verification of the relationship between the intensity of DNA damage and the dynamic behavior of the biochemical species involved in cell cycle regulation mechanism and the DNA damage signaling pathway is indispensable for elucidating the mechanism of cell fate deter- mination. Although it is difficult to visualize these complicated relationships using only experimentally observed data, one can comprehensively verify these relationships with a numerical model that applies experimental data to a kinetic mathematical model that integrates the cell cycle regulation mechanism with the DNA damage signaling pathway. Many researchers have constructed useful kinetic mathematical models of the cell cycle regulation mechanism to evaluate the interactions of biochemical species (Qu et al., 2003; Novak and Tyson, 2004; Csikasz-Nagy et al., 2006; Iwamoto et al., 2008; Tashima et al., 2008; Hamada et al., 2009; Ling et al., 2010). Moreover, experimental studies demonstrate that p53, a key component of the DNA damage signaling pathway, exhibits oscillatory behavior following γ-irradiation-induced DNA damage to cells (Lev Bar-Or et al., 2000; Batchelor et al., 2008). Based on these experimental findings, several kinetic mathematical mod- els of the DNA damage signaling pathway have been constructed, and they demonstrate that negative feedback effects between p53 and Mdm2 are responsible for the oscillatory dynamics of p53 (Lev Bar-Or et al., 2000; Batchelor et al., 2008). Toettcher et al. (2009) constructed a comprehensive kinetic mathematical model (Toettcher's model) that integrates the cell cycle regulation mech- anism (Csikasz-Nagy et al., 2006) with the DNA damage signaling pathway (Batchelor et al., 2008), and identified p21-mediated inhi- bition of Cyc/Cdk as a dominant factor that properly regulates cell cycle arrest and prevents endoreduplication. However, Toettcher's model did not take the variation of intensity of DNA damage into consideration; therefore, it cannot be used to verify the relationship between the intensity of DNA damage and the dynamic behavior of biochemical species involved in the cell cycle regulation mech- anism or the DNA damage signaling pathway. Currently, there is no effective kinetic mathematical model that can be used to verify the effect of the intensity of DNA damage on cell cycle progression. A kinetic mathematical model that can verify the effects of differ- ing intensities of DNA damage is indispensable to elucidating the mechanism of cell fate determination following DNA damage.

<a id='251d0817-95b4-40d0-803a-4e21b8307860'></a>

In a previous study, we constructed a kinetic mathematical model in which the DNA damage signaling pathway interferes with G1/S progression of the cell cycle (G1/S model) and qualitatively confirmed that DNA damage induces cell cycle arrest (Iwamoto et al., 2008). Moreover, Tashima et al. (2006) constructed a kinetic mathematical model in which the DNA damage signaling pathway interferes with G2/M progression of the cell cycle (G2/M model), and this model realized cell cycle arrest with various intensity of DNA damage.

<a id='b38f5a0b-1518-4710-acfc-acc62ccd3a78'></a>

In the current study, we constructed a novel kinetic mathemat-ical model (proposed model) that integrates the G1/S model with the G2/M model, and we assessed and confirmed the biological plausibility of the proposed model by validating several numeri-cally simulated time courses of the levels of individual biochemical species. Next, we explored the robustness of proposed model by applying the sensitivity analysis for the kinetic parameters. Fur-thermore, we also quantitatively identified the intensity of DNA damage in the proposed model based on experimentally observed data reported by Li and Ho (1998), and we evaluated the effect of different intensities of DNA damage on cell cycle arrest. Finally, we discuss the mechanism by which cells determine an appropriate cell fate. These results will contribute to an elucidation of dominant factors that determine cell fate and will be useful for developing novel therapeutic systems for tumor tissue.

<a id='d09d89b7-5769-42c6-8927-142db0b1638d'></a>

## 2. Mathematical model

### 2.1. G1/S and S/G2 transitions

The transcription factor E2F plays an essential role in DNA replication and is repressed by the binding of retinoblastoma protein (Rb) in G1. As normal cells are sufficiently stimulated by the cell growth factors, CycD is synthesized, and G1 progression is initiated. CycD binds to Cdk4 to form the activated binary complex CycD/Cdk4 (Fig. S1). The CycD/Cdk4 complex phosphorylates Rb bound to E2F, which becomes the hypophosphorylated form (Rb-PP). Furthermore, the Rb-PP phosphorylated by both CycE/Cdk2 and CycA/Cdk2 becomes the hyperphosphorylated form (Rb-PPP). Rb-PPP disassociates from Rb-PP/E2F and E2F is activated (Fig. S1). Activated E2F induces the transcriptional activation of CycE, CycA, Cdc25A, and several genes required for DNA replication (Helin, 1998). CycE and CycA bind to separate inactive Cdk2 molecules to form inactive complexes, iCycE/Cdk2 and iCycA/Cdk2, respectively. Cdc25A dephosphorylates and activates iCycE/Cdk2 and iCycA/Cdk2, which then form activated binary complexes, aCycE/Cdk2 and aCycA/Cdk2, respectively (Fig. S2). The phosphorylation of Rb-PP by both aCycE/Cdk2 and aCycA/Cdk2 leads to the further dissociation of Rb-PPP and E2F and concomitant the activation of E2F. Thus, the positive feedback loop between Rb/E2F complexes and two types of Cyc/Cdk complexes plays a central role in the G1 progression (Figs. S1 and S2). Sufficient expression of both aCycE/Cdk2 and E2F initiates DNA replication and drives the progression to S phase (Woo and Poon, 2003; Matsumura et al., 2003). After completing DNA replication during S phase, aCycA/Cdk2 promotes the degradation of E2F (Xu et al., 1994). The decrease in E2F reduces the synthesis of CycE and formation of aCycE/Cdk2, which causes the progression to G2 phase. There are three Cdk inhibitors (CKIs), p16, p21, and p27, that regulate G1/S progression (Figs. S1 and S2). p16 specifically inhibits the activation of CycD/Cdk4, and both p21 and p27 repress aCycE/Cdk2 and aCycA/Cdk2 (Parry et al., 1995; LaBaer et al., 1997). In particular, the expression of p21 is upregulated with DNA damage, which inhibits the positive feedback loop between Rb/E2F complexes and both types of Cyc/Cdk complexes (Fig. S2).

<!-- PAGE BREAK -->

<a id='54989fc8-9a7c-4aa2-bb37-7713a6b0a426'></a>

386

<a id='1bf18c34-5c40-4bb4-a4be-1af8806ab005'></a>

K. Iwamoto et al. / BioSystems 103 (2011) 384–391

<a id='6c4e2516-a31a-49e7-aaf4-b2640356a67b'></a>

<::chart: Diagram of key regulators in a proposed model integrating the G1/S model with the G2/M model. The diagram consists of various components represented by circles (regulators of cell cycle regulation) and squares (components of the DNA damage signaling pathway), connected by blue arrows for activation and red blunt lines for inhibition. A legend in the top right corner indicates: Activation (blue arrow), Inhibition (red blunt line).The diagram can be broken down into:1.  **DNA Damage Pathway (Top)**:    - DNA damage is sensed, leading to the activation of ATM/ATR.    - ATM/ATR activates Mdm2, p53, and Chk1.    - Mdm2 inhibits p53.    - p53 activates p21 and 14-3-3σ.    - Chk1 inhibits Cdc25C and activates 14-3-3σ.    - 14-3-3σ inhibits Cdc25C.2.  **Cell Cycle Regulation Pathway (Middle)**:    - **G1 Phase Regulators**:        - p16 inhibits CycD.        - CycD activates E2F.        - p27 inhibits CycE.        - p21 inhibits CycE, CycA, and Cdc25C.        - E2F activates CycE and CycA.    - **S Phase Regulators**:        - CycE activates CycA.    - **G2/M Phase Regulators**:        - CycA activates CycB.        - CycB inhibits Wee1.        - Wee1 inhibits CycB.        - Cdc25C activates CycB.        - CycB activates APC/Cdc20.        - APC/Cdc20 inhibits CycB and CycA.        - APC/Cdc20 activates APC/Cdh1.        - APC/Cdh1 inhibits CycE and CycA.        - APC/Cdh1 activates E2F.3.  **Cell Cycle Phases (Bottom Bar)**:    - G1 (green)    - S (blue)    - G2 (red)    - M (orange)    - G1 (green)Fig. 1. Diagram of key regulators in the proposed model which integrates the G1/S model with the G2/M model. Circle and square species represent regulators of the cell cycle regulation mechanism and components of the DNA damage signaling pathway, respectively. The approximate cell cycle phases are shown at the bottom. The details of proposed model and abbreviations are shown in supplemental information Figs. S1–S4. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)::>

<a id='2ec9f7f6-21c1-4610-a390-fe2c659e508d'></a>

2.2. G2/M and M/G1 transitions

From late S phase to G2 phase, aCycA/Cdk2 activates the tran-
scription factor NF-Y, which induces the transcriptional activation
of CycB (Chae et al., 2004). CycB binds to Cdk1 and forms an inac-
tivated complex iCycB/Cdk1 (Fig. S3). Although the iCycB/Cdk1
is dephosphorylated by Cdc25C to become activated complex
aCycB/Cdk1, aCycB/Cdk1 is continuously phosphorylated and inac-
tivated by Wee1 (Fig. S3). The aCycB/Cdk1 complex has a nuclear
export signal, unlike CycD/Cdk4, CycE/Cdk2, and CycA/Cdk2; there-
fore, it localizes to the cytoplasm in G2 phase (aCycB/Cdk1cyto)
(Takizawa and Morgan, 2000). Concurrently, aCycA/Cdk2 causes
chromosome condensation and drives the progression to M phase
(Furuno et al., 1999; Gong et al., 2007). In M phase, CycF mediates
the transport of aCycB/Cdk1cyto to the nucleus (aCycB/Cdk1nuc),
which is followed by M phase reactions, such as the chromosome
condensation and nuclear breakdown (Li et al., 1997; Kong et al.,
2000). Thereafter, the anaphase promoting complex/cyclosome
(APC/C) binds to Cdc20 to form APC/Ccdc20, followed by activa-
tion of aCycB/Cdk1nuc, and forms activated APC/Ccdc20. Activated
APC/Ccdc20 promotes the degradation of securin, CycA, and CycB
and induces several reactions that promote exit from M exit, e.g.,
chromosome segregation (Castro et al., 2005) (Fig. S3). The degrada-
tion of CycA and CycB inactivates aCycA/Cdk2 and aCycB/Cdk1nuc,
respectively, which activates APC/Ccdh1 (Figs. S2 and S3). Activated
APC/Ccdh1 promotes degradation of CycA, CycB, and Cdc20, inac-
tivating aCycA/Cdk2, aCycB/Cdk1nuc, and APC/Ccdc20, respectively
(Figs. S2 and S3). Sufficient decline in aCycB/Cdk1nuc mediated by
both APC/Ccdc20 and APC/Ccdh1 induces exit from M phase, which
marks completion of cell cycle progression (Xu and Chang, 2007).
The expression of p21 is specifically upregulated when the DNA
damage occurs, and p21 binds to aCycA/Cdk2 and aCycB/Cdk1,
repressing their activity (LaBaer et al., 1997). Moreover, the activa-

<a id='8ca7f6f7-8a12-41c5-9d4b-083e15646bb6'></a>

tion of APC/Ccdc20 is blocked by p21-mediated inhibition of Cyc/Cdk complexes (Figs. S2 and S3).

<a id='13c88044-5a2d-4a72-aef2-0a34f95a9aff'></a>

### 2.3. DNA damage signaling pathway

When DNA damage, such as double strand breaks, is generated by IR- and UV-irradiation, both ATM and ATR (ATM/ATR) are activated by DNA damage signal transduction (Fig. S4). Activated ATM/ATR phosphorylates and activates both p53 and Chk1 (Canman et al., 1998; Bartek and Lukas, 2003). Activated p53 induces transcriptional activation of Mdm2, p21, and 14-3-3σ. Activated Mdm2 promotes degradation of p53, forming a negative feedback loop between p53 and Mdm2 (Fig. S4). This negative feedback loop can produce oscillatory dynamic behaviors of both p53 and Mdm2 (Lev Bar-Or et al., 2000; Batchelor et al., 2008). p21 binds to aCycE/Cdk2, aCycA/Cdk2, and CycB/Cdk1, repressing their activity, which induces G1 arrest and G2 arrest (Figs. S2 and S3). Additionally, Cdc25C phosphorylated by Chk1 is exported to the cytoplasm by 14-3-3σ. As a result, the activation of CycB/Cdk1 is inhibited, and G2 arrest is induced.

<a id='4f8133d8-b1b4-4b70-90ab-25796bb07cf1'></a>

## 2.4. Proposed model
The reaction processes of S/G2 phase, which include both synthesis of CycA and NF-Y-mediated synthesis of CycB, were incorporated into the G1/S model (Figs. S1 and S2). Additionally, the G2/M model was expanded by including several biochemical species that play important roles in the transition from M to G1 transition, the dynamic behavior of CycB/Cdk1 in the nucleus and cytoplasm, APC/Ccdc20, and APC/Ccdh1 (Fig. S3). The DNA damage signaling pathway in the proposed model was represented by integrating the p53 model structured by Lev Bar-Or et al. (2000) with the activation of p53 induced by ATM/ATR (Fig. S4). Fig. 1

<!-- PAGE BREAK -->

<a id='cfa6d7bc-9b75-420d-8168-541b52a9404b'></a>

K. Iwamoto et al. / BioSystems 103 (2011) 384-391

<a id='5f0cc38c-e607-4228-bed0-2785f1893a93'></a>

387

<a id='7bfe5fd8-7081-4a5a-b975-a720f6a8e850'></a>

shows the reaction scheme of the proposed model, which inte-
grated the G1/S model, the G2/M model, and the DNA damage
signaling pathway. The proposed model consists of 54 dependent
variables and 137 kinetic parameters (Tables S1–S3). Both initial
conditions and kinetic parameters in the proposed model, which
qualitatively realize observed data on several notable cell cycle reg-
ulators, including CycE, CycA, CycB, and p27, were estimated based
on values described in previous reports (Lev Bar-Or et al., 2000;
Iwamoto et al., 2008; Tashima et al., 2006).

<a id='86f8df10-9b46-43f9-9f99-8b2974b43e9e'></a>

## 2.5. Numerical analysis
DNA damage was represented by a single dependent variable, DNA damage signal (DDS), in the proposed model (Fig. S4). In the numerical simulations, the values of DDS were set as follows: 0 (No-damage), 0.002 (Low-damage), 0.004 (Medium-damage), 0.008 (High-damage), and 0.016 (Excess-damage). The numerical simulations were run by employing the software XPPAUT (Ermentrout, 2002), and the time courses of total CycE (tCycE), total CycA (tCycA), total CycВ (tCycB), аСусE/Cdk2, p27, APC/Ccdc20, p21 and p53 were calculated. Here, tCycE represents the total amount of both CycE and all complexes related to CycE (Fig. S2). Similarly, tCycA and tCycB represent the specific cyclin and all related complexes (Figs. S2 and S3).

<a id='aff0a739-eeec-43b3-85bd-08cf2275cd83'></a>

First, we performed the sensitivity analysis of kinetic parameters in the proposed model without DNA damage to evaluate the robustness of proposed model. Here, the robustness is whether the cell cycle normally proceeds one period (G1 → S → G2 → M), which was determined by the peak value of tCycB that involved in the M phase progression. The values of kinetic parameters described in Table S2 were regarded as 100% (Standard), and the peak values of tCycB were calculated by changing the values of 137 kinetic parameters, one by one, from 50% to 200% at 10% interval. Under all conditions, the sensitivity of kinetic parameter (Variation) was evaluated by using the following equation.

<a id='307082f0-6202-436f-9742-e4f1fc866ae9'></a>

Variation (%) = PV<sub>change</sub> / PV<sub>standard</sub> × 100 (1)

where, PV<sub>change</sub> and PV<sub>standard</sub> represented the peak values of tCycB in changed kinetic parameter and in Standard shown in Table S2, respectively.

<a id='89136b4b-1ac8-41bc-8320-abc11b91feec'></a>

Next, based on the time course data of above mentioned notable chemical species, we identified the boundaries between the phases of the cell cycle, and we verified the delay at the G1/S boundary, the dynamic behavior of p53, and the concentration of the total amount of p21 after the occurrence of DNA damage. Finally, we elucidated the effect of different intensities of DNA damage on the cell cycle from these results.

<a id='7d5c7e6d-cf60-4183-b819-406b5570be65'></a>

## 3. Results and discussion

### 3.1. Normal cell cycle progression

The numerical simulation using the proposed model was run without DNA damage (DDS=0) to calculate the time course of several notable cell cycle regulators, total CycE (tCycE), total CycA (tCycA), total CycB (tCycB), aCycE/Cdk2, p27, and APC/Ccdc20 (Fig. 2). As shown in Fig. 2, the concentration of p27, which is sustained at high level in early G1 phase (Donjerkovic and Scott, 2000), decreased as the concentration of aCycE/Cdk2 increased in this simulation. The decline of p27 concentration was caused by the aCycE/Cdk2-dependent degradation of p27; this result was in good agreement with biological findings reported by Sheaff et al. (1997). The aCycE/Cdk2 complex induced activation of E2F, which positively regulated both the synthesis of CycE and CycA (Figs. S1 and S2). Therefore, the concentration of tCycE increased

<a id='2dfe9570-4a85-4579-9102-fcd1dea2c1c8'></a>

<::chart: line chart::>Fig. 2. Time courses of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, and APC/Ccdc20 resulting from a simulation run without DNA damage and using the proposed model. The x-axis is "Time (-)" ranging from 0 to 6000. The left y-axis is "Concentration (-)" ranging from 0 to 20. The right y-axis is "Concentration of APC/C (-)" ranging from 0 to 1. The chart shows the following lines: p27 (decreasing from ~14 to 0, then increasing slightly), tCycE (low, then sharply increasing to ~16 around 2300, then decreasing), aCycE/Cdk2 (low, then increasing to ~3 around 2800, then decreasing), tCycA (low, then increasing to ~8 around 3800, then decreasing), tCycB (low, then increasing to ~4 around 4500, then decreasing), and APC/Ccdc20 (low, then sharply increasing to ~0.8 around 4800, then decreasing). tCycE represents the total amount of CycE and all complexes related to CycE (Fig. S2). Similarly, tCycA and tCycB represent the respective cyclins and their related complexes (Figs. S2 and S3). The value of the DDS was set to 0. <::/chart::>

<a id='c188926f-76a0-47b2-b6fd-75ef3b53aa32'></a>

rapidly and reached its peak level because of the positive feed-back loop between E2F and CycE (Fig. 2). Such dynamic behavior of tCycE was in good agreement with biological findings reported by Ohtsubo et al. (1995), and the timing of the tCycE peak was identified as the G1/S boundary (2329 timesteps in Fig. 2). Subsequently, with the increase in tCycA concentration, the degradation of E2F was facilitated by aCycA/Cdk2 (Xu et al., 1994), which led to the decline of aCycE/Cdk2 and tCycE concentrations (Fig. 2). Since the decrease in aCycE/Cdk2, which plays an important role in DNA replication, implied the completion of DNA replication (Woo and Poon, 2003), the time at which the concentration of aCycE/Cdk2 was reduced was identified as the S/G2 boundary (3293 timesteps in Fig. 2). In contrast, the concentration of tCycA and tCycB sequentially reached their peak levels (Fig. 2). The increase in tCycB concentration resulted from the upregulation of CycB tran-scription by the transcription factor NF-Y, which had been activated by aCycA/Cdk2 (Chae et al., 2004). The sequential peaks in tCycA and tCycB concentration were characteristic of dynamics in G2 and M phase (Zhu et al., 2004; Hochegger et al., 2008). Since the aCycA/Cdk2 complex drives the progression from G2 phase to M phase (Furuno et al., 1999; Gong et al., 2007), in this simulation, the peak time of tCycA was identified as the G2/M boundary (4222 timesteps in Fig. 2). After the G2/M transition, the aCycB/Cdk1 that had been localized in the cytoplasm during G2 phase moved to the nucleus (aCycB/Cdk1nuc). aCycB/Cdk1nuc activated and upregulated APC/Ccdc20, which then downregulated tCycA and tCycB by promot-ing the degradation of CycA and CycB (Fig. 2). In addition, APC/Ccdc20 can induce several reactions related to exit from M phase, such as chromosome segregation (Zachariae and Nasmyth, 1999). The peak time of APC/Ccdc20 was identified as the M/G1 boundary (4691 timesteps in Fig. 2).

<a id='1678cbd9-9b6d-4a5f-a44f-4107d049e77d'></a>

Once the time course of the key regulators - tCycE, tCycA, tCycB, aCycE/Cdk2, p27, and APC/Ccdc20 - was confirmed, the timescale in the proposed model was converted to real time based on the times of peak tCycE and tCycA concentration, which were identified as the G1/S and the G2/M boundary, respectively (Fig. 3). The differ- ence between the times of peak tCycE and tCycA concentrations in the proposed model was about 1890 timesteps (Fig. 2). Accord- ing to the biological finding reported by Ohtsubo et al. (1995), the time-lag between expression of CycE and CycA is about 10 h in real time. Hence, 189 timesteps in the proposed model might correspond to an hour in real time. Then, the peak times of tCycE and tCycA concentrations in the proposed model were calculated

<!-- PAGE BREAK -->

<a id='72f7831f-382c-42aa-900a-e328ed70bea9'></a>

388

<a id='b517176f-a704-48ec-94b7-b07ed9180971'></a>

K. Iwamoto et al. / BioSystems 103 (2011) 384-391

<a id='9fd79f3f-3ab1-4d5d-b701-75bd2bfea7b5'></a>

<::Figure: Line graph::> Fig. 3. Time course of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, APC/Ccdc20, p53, and p21 compared with real-time data in the case of No-damage. The graph consists of two stacked panels, both sharing a common x-axis labeled "Time (h)" ranging from 0 to 32. The cell cycle phase is indicated between the upper and lower graphs with colored bars and labels: G1 (green), S (blue), G2 (red), M (purple), and G1 (green). The DDS value was set to 0. The times of peak tCycE, tCycA, and APC/Ccdc20 corresponded to the G1/S (12.32 h), the G2/M (22.34 h) and the M/G1 boundaries (24.82 h), respectively. The time of rapid decrease of aCycE/Cdk2 corresponded as the S/G2 boundary (17.42 h). The top panel has a left y-axis labeled "Concentration (-)" ranging from 0 to 20, and a right y-axis labeled "Concentration of APC/C (-)" ranging from 0 to 1. This panel shows time courses for: p27 (red line, decreasing then increasing), tCycE (green line, peaking around 14h), aCycE/Cdk2 (light blue line, peaking around 18h), tCycA (dark blue line, peaking around 22h), tCycB (purple line, peaking around 24h), and APC/Ccdc20 (orange line, peaking around 24h). The bottom panel has a left y-axis labeled "Concentration (-)" ranging from 0 to 2.5. This panel shows time courses for p53 and p21, both represented by low, relatively flat lines near zero. <::/Figure::>

<a id='ccbd1f5c-e4f5-4e1b-b19c-4fc75e30123d'></a>

as 12.32 and 22.34 h in real time, respectively (Fig. 3). Ohtsubo
et al. (1995) reported that CycE and CycA are expressed 12–16
and 20–24 h, respectively, after the initiation of G1 progression.
Accordingly, the times of peak tCycE and tCycA concentrations in
the proposed model were in good agreement with experimentally
observed data. Moreover, the time required for one cell cycle in the
proposed model was 24.82 h (Fig. 3) and nearly equal to the time
required for one cell cycle in normal mammalian cells (about 24 h).

<a id='2af6b4b3-ab9f-4f04-b468-0616f5258960'></a>

In order to evaluate the robustness of proposed model, we cal- calculated the Variation based on Eq. (1) with changing the value of all kinetic parameters, one by one, from 50% to 200%. Variation is the ratio of peak level of tCycB in changed kinetic parameter to that in Standard shown in Table S2, which makes it possible for us to eval- uate a sensitivity of each kinetic parameter in the proposed model. Table 1 showed the notable kinetic parameters which caused a rel- atively major change in Variation on those range. Those kinetic parameters associated with following biochemical reactions: k9 is the synthesis constant of CycA induced by aB-Myb (Fig. S2), k105 is the synthesis constant of iB-Myb induced by E2F (Fig. S1), k107 is the degradation constant of aB-Myb (Fig. S1), k124 involves in the activation from iAPC/Ccdh1 to aAPC/Ccdh1 promoted by both aCycA/Cdk2 and aCycB/Cdk1 nuc (Fig. S3), k125 involves in the inac- tivation from aAPC/Ccdh1 to iAPC/Ccdh1 (Fig. S3). The decline in k9, k105 and k124 decreased Variation, and the increase in them led the increment in Variation (Table 1). On the other hand, k107 and k125 showed the opposite tendency for k9, k105 and k124 (Table 1). In the range changing kinetic parameter values, moreover, the maximum and minimum values of Variation were 156% and 38%, respectively (Table 1). Xu and Chang (2007) reported that the peak level of tCycB in the cell cycle progression was 2.92 ± 1.7 µM. The coefficient of variation is around 58%, which implies that the peak level of tCycB is observed in the range from 42% to 158% in the cell cycle pro- gression. When the kinetic parameter in the proposed model was changed between 50% and 200%, Variation was changed in the range from 38% to 156%, which was in good agreement with the biological findings (Xu and Chang, 2007). Since the proposed model realized

<a id='6ca7a00c-c37e-4d29-b8b3-c37e54389000'></a>

Table 1
Variation of the kinetic parameters in the proposed model.

<table id="4-1">
<tr><td id="4-2">Degree of change in kinetic</td><td id="4-3" colspan="5">Kinetic parameters</td></tr>
<tr><td id="4-4">parameter (%)</td><td id="4-5">k₉</td><td id="4-6">k₁₀₅</td><td id="4-7">k₁₀₇</td><td id="4-8">k₁₂₄</td><td id="4-9">k₁₂₅</td></tr>
<tr><td id="4-a">200</td><td id="4-b">156%</td><td id="4-c">156%</td><td id="4-d">41%</td><td id="4-e">147%</td><td id="4-f">44%</td></tr>
<tr><td id="4-g">190</td><td id="4-h">152%</td><td id="4-i">152%</td><td id="4-j">46%</td><td id="4-k">144%</td><td id="4-l">49%</td></tr>
<tr><td id="4-m">180</td><td id="4-n">148%</td><td id="4-o">148%</td><td id="4-p">51%</td><td id="4-q">141%</td><td id="4-r">53%</td></tr>
<tr><td id="4-s">170</td><td id="4-t">144%</td><td id="4-u">144%</td><td id="4-v">56%</td><td id="4-w">137%</td><td id="4-x">58%</td></tr>
<tr><td id="4-y">160</td><td id="4-z">139%</td><td id="4-A">139%</td><td id="4-B">62%</td><td id="4-C">134%</td><td id="4-D">63%</td></tr>
<tr><td id="4-E">150</td><td id="4-F">134%</td><td id="4-G">134%</td><td id="4-H">68%</td><td id="4-I">129%</td><td id="4-J">69%</td></tr>
<tr><td id="4-K">140</td><td id="4-L">129%</td><td id="4-M">129%</td><td id="4-N">74%</td><td id="4-O">125%</td><td id="4-P">74%</td></tr>
<tr><td id="4-Q">130</td><td id="4-R">122%</td><td id="4-S">122%</td><td id="4-T">80%</td><td id="4-U">120%</td><td id="4-V">80%</td></tr>
<tr><td id="4-W">120</td><td id="4-X">116%</td><td id="4-Y">116%</td><td id="4-Z">87%</td><td id="4-10">114%</td><td id="4-11">86%</td></tr>
<tr><td id="4-12">110</td><td id="4-13">108%</td><td id="4-14">108%</td><td id="4-15">93%</td><td id="4-16">107%</td><td id="4-17">93%</td></tr>
<tr><td id="4-18">100a</td><td id="4-19">100%</td><td id="4-1a">100%</td><td id="4-1b">100%</td><td id="4-1c">100%</td><td id="4-1d">100%</td></tr>
<tr><td id="4-1e">90</td><td id="4-1f">91%</td><td id="4-1g">91%</td><td id="4-1h">107%</td><td id="4-1i">91%</td><td id="4-1j">107%</td></tr>
<tr><td id="4-1k">80</td><td id="4-1l">80%</td><td id="4-1m">80%</td><td id="4-1n">114%</td><td id="4-1o">81%</td><td id="4-1p">115%</td></tr>
<tr><td id="4-1q">70</td><td id="4-1r">69%</td><td id="4-1s">69%</td><td id="4-1t">121%</td><td id="4-1u">69%</td><td id="4-1v">124%</td></tr>
<tr><td id="4-1w">60</td><td id="4-1x">56%</td><td id="4-1y">56%</td><td id="4-1z">127%</td><td id="4-1A">55%</td><td id="4-1B">133%</td></tr>
<tr><td id="4-1C">50</td><td id="4-1D">41%</td><td id="4-1E">41%</td><td id="4-1F">134%</td><td id="4-1G">38%</td><td id="4-1H">143%</td></tr>
</table>

a 100% is the values of original kinetic parameters described in Table S2.
Definitions of kinetic parameters were as follows: k₉: Cyclin A synthesis by aB-Myb
(Fig. S2), k₁₀₅: iB-Myb synthesis by E2F (Fig. S1), k₁₀₇: aB-Myb degradation (Fig. S1),
k₁₂₄: activation from iAPC/C-Cdh1 to aAPC/C-Cdh1 promoted by aCycA/CDK2 and
aCycB/CDK1nuc (Fig. S3), k₁₂₅: inactivation from aAPC/C-Cdh1 to iAPC/C-Cdh1
(Fig. S3).

<a id='8233010a-000e-4a69-acc7-848dd38430a1'></a>

the cell cycle progression as the value of kinetic parameter was
changed between 50% and 200%, the cell cycle regulation system
based on the proposed model has the robustness on a fluctuation
of reaction rate in each reaction process.

<a id='dcb0fe70-5c06-4ae0-acdc-c5b821fbdb06'></a>

Therefore, the dynamics of several notable cell cycle regulators
in the proposed model agreed with experimentally observed data
from several biochemical species, demonstrating that the proposed
model should be biologically appropriate.

<a id='253c112e-c277-42f7-a306-9f12548ad22a'></a>

3.2. Effect of DNA damage on the cell cycle progression

To evaluate the effects of DNA damage on cell cycle progression, the numerical simulation using a DDS value of 0.002 at 0 h (G1 phase) and the proposed model was carried out (Fig. 4). The time courses of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, APC/Cdc20, p21, and p53 are shown in Fig. 4. Without DNA damage, the concentrations of both p53 and p21 were maintained at low level, and the G1/S boundary occurred at 12.32 h (Fig. 3). In contrast, with DNA damage, the concentrations of both p53 and p21 increased after the DNA damage occurred, and the G1/S boundary occurred at 12.59 h (Fig. 4). The DNA damage resulted in upregulation of p53; activation of ATM/ATR promoted synthesis of p21 leading to this upregulation of p53 (Fig. S4). The p21-dependent inhibition of aCycE/Cdk2 and aCycA/Cdk2 disturbed activation of E2F, which led to the retardation of CycE synthesis. Hence, the G1/S boundary in the numerical simulation with DNA damage was delayed relative to the G1/S boundary in the simulation without DNA damage (i.e., G1 arrest was achieved by DNA damage). Several experimental results showed that upregulation of p21 and G1 arrest are induced when DNA damage is caused by IR- or UV-irradiation in G1 phase (Di Leonardo et al., 1994; Dulic et al., 1994; Pellegata et al., 1996; Chang et al., 1999). As shown in Figs. 3 and 4, the simulation results using the proposed model realized several established biological findings, therefore, the proposed model can be used to evaluate the effects of DNA damage on cell cycle progression.

<a id='f5dea539-4333-41cb-82ef-bf3564c3233c'></a>

3.3. *Comparison of simulation results of the proposed model with experimental results*

To identify the intensity of DNA damage in the proposed model quantitatively, numerical simulations using the proposed model

<!-- PAGE BREAK -->

<a id='7490f9af-6a14-43f3-b8f5-33f0c9deb5cf'></a>

K. Iwamoto et al. / BioSystems 103 (2011) 384-391

<a id='61ddfae8-b718-4ad4-ae5e-babb0692dd50'></a>

389

<a id='dfa92176-71c8-45a2-8c16-9c98bd6ecdf5'></a>

<::Figure: A two-panel line graph illustrating the time course of various proteins and complexes. The x-axis for both panels is 'Time (h)' ranging from 0 to 32 hours. Below the top panel, colored bars indicate cell cycle phases: G1 (0-12.58 h, light green), S (12.58-19 h, light blue), G2 (19-21.5 h, red), M (21.5-24 h, purple), and G1 (24-32 h, light green). The DDS value was set to 0.002, and DNA damage occurred at 0 h (in G1 phase).

**Top Panel:**
- Left Y-axis: 'Concentration (-)' from 0 to 20.
- Right Y-axis: 'Concentration of APC/C (-)' from 0 to 1.
- **p27 (red line):** Starts high (~13) at 0h, gradually decreases to ~7 by 12h, then drops sharply to near 0 by 16h, remaining low.
- **tCycE (green line):** Starts low (~1), rises sharply to a peak of ~16 around 13h, then decreases to ~1 by 20h, and remains low.
- **aCycE/Cdk2 (light blue line):** Starts at 0, rises to a peak of ~2.5 around 14h, then drops to 0 by 18h.
- **tCycA (dark blue line):** Starts at 0, rises to a peak of ~8 around 20h, then decreases to near 0 by 26h.
- **tCycB (purple line):** Starts at 0, rises to a peak of ~6 around 22h, then drops to near 0 by 26h.
- **APC/Ccdc20 (orange line):** Starts at 0, rises sharply to a peak of ~0.8 around 23h, then drops to near 0 by 26h.

**Bottom Panel:**
- Y-axis: 'Concentration (-)' from 0 to 2.
- **p53 (black line):** Starts at 0, rises sharply to a saturation curve around 8h, reaching a plateau of ~0.8, and remains constant.
- **p21 (teal line):** Starts at 0, rises to a small peak of ~0.2 around 8h, drops to near 0 by 12h, shows another small rise to ~0.2 around 26h, and then decreases.

Fig. 4. Time course of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, APC/Ccdc20, p53, and p21 resulting from the simulation run with the Low-damage value. The cell cycle phase is indicated between the upper and lower graphs. DNA damage occurred at 0 h (in G1 phase), and the DDS value was set to 0.002. The time of the G1/S boundary was 12.58 h, and the dynamic behavior of p53 achieved a saturation curve.::>

<a id='84af2f31-3471-427e-8a41-0ac0405db03e'></a>

<::Figure: A two-panel line graph showing the time course of various cell cycle proteins and complexes. The top panel, titled "Concentration (-)" on the left y-axis (ranging from 0 to 20) and "Concentration of APC/C (-)" on the right y-axis (ranging from 0 to 1), displays lines for tCycE, tCycA, tCycB, aCycE/Cdk2, p27, and APC/Ccdc20 over time. Below this panel, colored horizontal bars indicate cell cycle phases: G1 (green), S (light blue), G2 (pink), M (purple), and G1 (green) again. The bottom panel, with a left y-axis labeled "Concentration (-)" (ranging from 0 to 2), shows oscillating lines for p53 and p21. Both panels share a common x-axis labeled "Time (h)" (ranging from 0 to 32). Fig. 6. Time course of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, APC/Ccdc20, p53, and p21 resulting from the simulation run with the high-damage value. The cell cycle phase is indicated between the upper and lower graphs. DNA damage occurred at 0 h (in G1 phase), and the DDS value was set to 0.008. The time of the G1/S boundary was 12.68 h, and the dynamic behavior of p53 was the oscillatory.:chart::>

<a id='7c987179-ab3b-445e-aa4b-90dc3445e2b2'></a>

and different intensities of DNA damage were run. The DDS values were set to 0.002 (Low-damage), 0.004 (Medium-damage), 0.008 (High-damage), and 0.016 (Excess-damage), and the time course of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, APC/Ccdc20, p53, and p21 were calculated (Figs. 4-7). Table 2 shows the concentration of tot_p21 (i.e., the total amount of p21 and all complexes related to p21) and the status of p53 24h after the occurrence of the DNA damage as estimated by the numerical simulations. Li and Ho (1998) exam- ined the expression of p21 and other cellular responses 24 h after

<a id='09d9b5bc-9cd1-425f-8306-ddb9ae397031'></a>

irradiation with various doses of UV; their experimental results
are summarized in Table 3. Generally, p21 levels declined as the
dose of radiation was increased from 200 to 800J/m²; however,
lower p21 levels resulted from irradiation with 100J/m² than with
200J/m² (Table 3). Similarly, the concentration of tot_p21 in the
proposed model decreased with higher DDS values, except that the
p21 level associated with Low-damage was lower than the p21
level associated with the Medium-damage. Comparison of Li and

<a id='c6121322-747c-4b60-9995-1c66bd68f0f2'></a>

<::chart: The figure displays two stacked line graphs showing the time course of various cellular components and their concentrations, with a common x-axis for 'Time (h)' ranging from 0 to 32. The cell cycle phases (G1, S, G2, M, G1) are indicated by colored bands between the upper and lower graphs. The upper graph has a left y-axis labeled 'Concentration (-)' from 0 to 20 and a right y-axis labeled 'Concentration of APC/C (-)' from 0 to 1. It shows the concentrations of:  - tCycE: Starts low, peaks around 12-16 h at ~16, then decreases.  - tCycA: Starts low, increases around 16 h, peaks around 20-24 h at ~8, then decreases.  - tCycB: Starts low, increases around 20 h, peaks around 24-28 h at ~8, then decreases.  - aCycE/Cdk2: Shows a small peak around 12 h.  - p27: Starts high at ~14, decreases steadily, then slightly increases around 28 h.  - APC/Ccdc20: Starts low, peaks around 24-28 h at ~0.8, then decreases. The lower graph has a left y-axis labeled 'Concentration (-)' from 0 to 2. It shows the concentrations of:  - p53: Increases rapidly from 0 to ~1.5 by 8 h and then remains saturated at ~1.5.  - p21: Starts low, peaks around 8-12 h at ~0.4, decreases, then shows a small increase around 28 h.  Fig. 5. Time course of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, APC/Ccdc20, p53, and p21 resulting from the simulation run with the Medium-damage value. The cell cycle phase is indicated between the upper and lower graphs. DNA damage occurred at 0 h (in G1 phase), and the DDS value was set to 0.004. The time of the G1/S boundary was 12.85 h and the dynamic behavior of p53 achieved a saturation curve.::>

<a id='7e509742-194d-416e-9558-21732b1d31fe'></a>

<::figure: chart::>Fig. 7. Time course of tCycE, tCycA, tCycB, aCycE/Cdk2, p27, APC/Ccdc20, p53, and p21 resulting from the simulation run with the excess-damage value. The cell cycle phase is indicated between the upper and lower graphs. DNA damage occurred at 0 h (in G1 phase), and the DDS value was set to 0.016. The time of the G1/S boundary was 12.67 h, and the dynamic behavior of p53 was oscillatory. The figure consists of two stacked line graphs sharing the same x-axis, 'Time (h)', which ranges from 0 to 32. The cell cycle phases G1, S, G2, M, and G1 are indicated by colored bars between the two graphs. The upper graph has a left y-axis labeled 'Concentration (-)' ranging from 0 to 20, and a right y-axis labeled 'Concentration of APC/C (-)' ranging from 0 to 1. This graph shows the time course of: p27 (red line, starts high, decreases), tCycE (green line, peaks around 16), aCycE/Cdk2 (light blue line, peaks around 4), tCycA (purple line, peaks around 8), tCycB (dark blue line, peaks around 4), and APC/Ccdc20 (orange line, peaks around 0.8 on the right axis). The lower graph has a y-axis labeled 'Concentration (-)' ranging from 0 to 2. This graph shows the time course of p53 (black line) and p21 (teal line). p53 exhibits oscillatory behavior with peaks up to 1.75, while p21 shows smaller, correlated oscillations remaining below 0.25.<::>

<!-- PAGE BREAK -->

<a id='7d65ae95-4a4a-4a94-94ef-1f0c89537489'></a>

390

<a id='ffcce81a-5aba-41e8-b89c-8d308476119c'></a>

K. Iwamoto et al. / BioSystems 103 (2011) 384–391

<a id='9ea0339f-415f-4112-ba2c-c1c9066f5ec4'></a>

Table 2
The concentration of tot_p21 and dynamic behavior of p53 resulting from numerical
simulations run with DNA damage and using the proposed model.

<table id="6-1">
<tr><td id="6-2">DNA damage</td><td id="6-3">tot.p21</td><td id="6-4">Dynamic behavior of p53</td></tr>
<tr><td id="6-5">Low-damage</td><td id="6-6">1.72</td><td id="6-7">Saturation curve</td></tr>
<tr><td id="6-8">Medium-damage</td><td id="6-9">3.14</td><td id="6-a">Saturation curve</td></tr>
<tr><td id="6-b">High-damage</td><td id="6-c">1.54</td><td id="6-d">Oscillation</td></tr>
<tr><td id="6-e">Excess-damage</td><td id="6-f">0.88</td><td id="6-g">Oscillation</td></tr>
</table>

The value of DDS was set as follows: 0.002 (Low-damage), 0.004 (Medium-damage),
0.008 (High-damage), and 0.016 (Excess-damage).
The tot_p21 represents the concentration of the total amount of p21 and all com-
plexes related to p21 24 h after DNA damage in simulations using the proposed
model (Figs. S1–S3).

<a id='560ad4cc-4e0f-4880-886a-ade13f116eb1'></a>

Ho's data with the results of the numerical simulations suggests that Low-, Medium-, High-, and Excess-damage in the proposed model correspond to actual DNA damage caused by UV-irradiation doses of 100, 200, 400, and 800 J/m², respectively. The times of G1/S boundary achieved by numerical simulations run with DNA dam- age and based on the proposed model were 12.59 (Low-damage), 12.85 (Medium-damage), 12.68 (High-damage) and 12.67 (Excess- damage) h, and G1 arrest was induced in all cases (Figs. 4–7). Chang et al. (1999) reported that cells arrest in G1 after exposure to 5 or 20 Gy of IR-irradiation. This biological finding suggests that cell cycle arrest is induced independently of the intensity of DNA damage, which is generally in good agreement with the simulation results shown in Figs. 4–7. Moreover, the duration of the G1 arrest in sim- ulations with High- and Excess-damage was shorter than that in simulations with the Medium-damage (Figs. 5–7). Since the G1 arrest was induced by p21-dependent inhibition of aCycE/Cdk2 and aCycA/Cdk2, the duration of the G1 arrest depended on the expres- sion of p21. The expressions of p21 in simulations with High- and Excess-damage were lower than that in the simulation with the Medium-damage (Table 2), which suggested that the duration of the G1 arrest was shortened by the decrease in p21 expression.

<a id='e90ed2f2-0ca1-4788-b4d6-50cde488caa6'></a>

The synthesis of p21 was also regulated by p53 in the pro-posed model (Fig. S2). The dynamic behavior of p53 in numerical simulations run with High- and Excess-damage was oscillatory and this oscillation caused a decline in p21 (Figs. 6 and 7). Lev Bar-Or et al. (2000) and Batchelor et al. (2008) reported that p53 showed oscillatory behavior following severe DNA damage caused by y-irradiation. Based on these biological findings, the oscillatory behaviors of p53 in the simulation were biologically appropriate dynamics. Furthermore, apoptosis was induced in numerical sim-ulations run with High- and Excess-damage values (Table 2). These results implied that the oscillatory behavior of p53 was impor-tant to the induction of apoptosis. Recently, Wee et al. (2009) constructed a mathematical model that integrated the p53-AKT network with the downstream signaling pathways from p53 to apoptosis induction, and they reported that the oscillatory behavior of p53 affected cell fate, specifically the choice between cell cycle arrest/DNA repair and apoptosis. As shown in Table 2, the oscil-latory behavior of p53 caused a decline in tot_p21. Decreases in p21 expression cause upregulation of the caspase-3, which induces apoptosis (Gervais et al., 1998). Therefore, although cell cycle arrest

<a id='754f5842-840b-4fdb-9230-4261f90ca4c7'></a>

Table 3
Summarized experimental results reported by Li and Ho (1998).

<table id="6-h">
<tr><td id="6-i">UV dose (J/m²)</td><td id="6-j">Rank of p21 protein level</td><td id="6-k">Cellular response</td></tr>
<tr><td id="6-l">100</td><td id="6-m">2nd</td><td id="6-n">Cell cycle arrest</td></tr>
<tr><td id="6-o">200</td><td id="6-p">1st</td><td id="6-q">Cell cycle arrest</td></tr>
<tr><td id="6-r">400</td><td id="6-s">3rd</td><td id="6-t">Apoptosis</td></tr>
<tr><td id="6-u">800</td><td id="6-v">4th</td><td id="6-w">Apoptosis</td></tr>
</table>

The p21 protein was extracted 24 h after UV-irradiation.
These data were extracted from the experimental results reported by Li and Ho
(1998).

<a id='b31fb7c3-e97c-482f-8cdf-07d472c8f853'></a>

was realized in all numerical simulations run with non-zero DNA
damage, apoptosis was only induced in simulations that resulted in
p53 oscillation, specifically those with High- and Excess-damage.
The observation of the dynamic behavior of p53 would provide the
important findings in the cell fate determination after DNA damage.
In our ongoing work, we have constructed a mathematical model
that integrates the proposed model with the apoptosis induction
pathway to analyze in detail the relationship between the oscilla-
tory behavior of p53 and the induction of apoptosis.

<a id='e2a9deba-e794-4a16-8b11-9283e58dbf36'></a>

## 4. Conclusion

In this study, we constructed a novel mathematical model in which the DNA damage signaling pathway interacts with the cell cycle regulation mechanism (proposed model) and analyzed the influence of different intensities of DNA damage on cell cycle progression and the dynamics of biochemical species important to cell cycle regulation. In the simulation using the proposed model and run without DNA damage, the simulation result qualitatively realized experimentally observed data from several cell cycle regulators, tCycE, tCycA, tCycB, aCycE/Cdk2, p27, and APC/Ccdc20. Next, we performed the sensitivity analysis of kinetic parameters in the proposed model. As a result, the proposed model realized the cell cycle progression in the case of changing the kinetic parameters in the range from 50% to 200%, indicating the robustness of proposed model. Moreover, the numerical simulations using the proposed model and run with DNA damage in G1 phase resulted in the induction of G1 arrest, which was in good agreement with several biological findings. Finally, four simulations of the proposed model each with a different intensity of DNA damage (i.e., Low-damage, Medium-damage, High-damage, and Excess-damage) were run to examine the duration of G1 arrest, the dynamic behavior of p53, and the expression of p21. Based on a comparison between biological finding on the expression of p21 and simulation results, Low-damage, Medium-damage, High-damage, and Excess-damage in the proposed model corresponded to the DNA damage generated by 100, 200, 400, and 800J/m² doses of UV-irradiation, respectively. This close correlation with biological findings from irradiation experiments demonstrated that the proposed model was effective for evaluating the effect of UV-irradiation on cell cycle progression. High- and Excess-damage resulted in both a shortening of the duration of the G1 arrest and p53 oscillation. The synthetic rate of p21, which affects cell cycle progression, declined in response to p53 oscillation because p21 synthesis was regulated by p53 in the proposed model. Furthermore, it is well known that apoptosis is induced by High- and Excess-damage. Therefore, the p53 oscillation may play an important role in the decision between cell survival and programmed cell death when DNA damage occurs.

<a id='b88748d5-9b63-4087-b5a2-a282442090fd'></a>

**Acknowledgement**

This work was done by the support of a Research Fellowship of the Japan Society for the Promotion of Science.

<a id='cc7f68f2-77b2-4b06-8139-355283d10ed9'></a>

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.biosystems.2010.11.011.

<a id='7c4e173f-3e1b-464f-ab71-248c64c1da82'></a>

## References

Bartek, J., Lukas, J., 2003. Chk1 and Chk2 kinases in checkpoint control and cancer. Cancer Cell 3 (5), 421-429.

Batchelor, E., Mock, C.S., Bhan, I., Loewer, A., Lahav, G., 2008. Recurrent initiation: a mechanism for triggering p53 pulses in response to DNA damage. Mol. Cell 30, 277-289.

<!-- PAGE BREAK -->

<a id='44e8e7e7-0f7a-4e0e-8604-b56310fb8276'></a>

K. Iwamoto et al. / BioSystems 103 (2011) 384–391

<a id='a18878a6-5eda-4a80-be52-ad9eaed4f345'></a>

391

<a id='ea846ce0-92b2-489c-bdcd-a547ee306722'></a>

Canman, C.E., Lim, D.S., Cimprich, K.A., Taya, Y., Tamai, K., Sakaguchi, K., Appella,
E., Kastan, M.B., Siliciano, J.D., 1998. Activation of the ATM kinase by ionizing
radiation and phosphorylation of p53. Science 281 (5383), 1677–1679.
Castro, A., Bernis, C., Vigneron, S., Labbe, J.C., Lorca, T., 2005. The anaphase-
promoting complex: a key factor in the regulation of cell cycle. Oncogene 24,
314–325.
Chae, H.D., Yun, J., Bang, Y.J., Shin, D.Y., 2004. Cdk2-dependent phosphorylation
of the NF-Y transcription factor is essential for the expression of the cell
cycle-regulatory genes and cell cycle G1/S and G2/M transitions. Oncogene 23,
4084–4088.
Chang, D., Chen, F., Zhang, F., McKay, B.C., Ljungman, M., 1999. Dose-dependent
effects of DNA-damaging agents on p53-mediated cell cycle arrest. Cell Growth
Differ. 10, 155–162.
Csikasz-Nagy, A., Battogtokh, D., Chen, K.C., Novak, B., Tyson, J.J., 2006. Analysis of
a generic model of eukaryotic cell-cycle regulation. Biophys. J. 90 (12), 4361–
4379.
Di Leonardo, A., Linke, S.P., Clarkin, K., Wahl, G.M., 1994. DNA damage triggers a
prolonged p53-dependent G1 arrest and long-term induction of Cip1 in normal
human fibroblasts. Genes Dev. 8, 2540–2551.
Donjerkovic, D., Scott, D.W., 2000. Regulation of the G1 phase of the mammalian cell
cycle. Cell Res. 10, 1–16.
Dulic, V., Kaufmann, W.K., Wilson, S.J., Tlsty, T.D., Lees, E., Harper, J.W., Elledge, S.J.,
Reed, S.I., 1994. p53-dependent inhibition of cyclin-dependent kinase activi-
ties in human fibroblasts during radiation-induced G1 arrest. Cell 76, 1013–
1023.
Ermentrout, B., 2002. Simulating, Analyzing, and Animating Dynamical Systems: A
Guide to XPPAUT for Researchers and Students. Soc. for Industrial and Applied
Math, Philadelphia.
Furuno, N., Elzen, N.D., Pines, J., 1999. Human Cyclin A is required for mitosis until
mid prophase. J. Cell Biol. 147, 295–306.
Gervais, J.L.M., Seth, P., Zhang, H., 1998. Cleavage of CDK inhibitor p21Cip1/Waf1 by
caspases is an early event during DNA damage-induced apoptosis. J. Biol. Chem.
273 (30), 19207–19212.
Gong, D., Pomerening, J.R., Myers, J.W., Gustavsson, C., Jones, J.T., Hahn, A.T., Meyer,
T., Ferrell Jr., J.E., 2007. Cyclin A2 regulates nuclear-envelope breakdown and the
nuclear accumulation of Cyclin B1. Curr. Biol. 17 (1), 85–91.
Hamada, H., Tashima, Y., Kisaka, Y., Iwamoto, K., Hanai, T., Eguchi, Y., Okamoto, M.,
2009. Sophisticated framework between cell cycle arrest and apoptosis induc-
tion based on p53 dynamics. PLoS ONE 4 (3), e4795.
Helin, K., 1998. Regulation of cell proliferation by the E2F transcription factors. Curr.
Opin. Genet. 8, 28–35.
Hochegger, H., Takeda, S., Hunt, T., 2008. Cyclin-dependent kinases and cell-cycle
transitions: does one fit all? Nat. Rev. Mol. Cell Biol. 9, 910–916.
Iliakis, G., Wang, Y., Guan, J., Wang, H., 2003. DNA damage checkpoint control in cells
exposed to ionizing radiation. Oncogene 22, 5834–5847.
Iwamoto, K., Tashima, Y., Hamada, H., Eguchi, Y., Okamoto, M., 2008. Mathematical
modeling and sensitivity analysis of G1/S phase in the cell cycle including the
DNA-damage signal transduction pathway. Biosystems 94, 109–117.
Kohn, K.W., 1999. Molecular interaction map of the mammalian cell cycle control
and DNA repair systems. Mol. Biol. Cell 10, 2703–2734.
Kong, M., Barnes, E.A., Ollendorff, V., Donoghue, D.J., 2000. Cyclin F regulates the
nuclear localization of cyclin B1 through a cyclin-cyclin interaction. EMBO J. 19,
1378–1388.
LaBaer, I., Garrett, M.D., Stevenson, L.F., Slingerland, J.M., Sandhu, C., Chou, H.S., Fat-
taey, A., Harlow, E., 1997. New functional activities for the p21 family of CDK
inhibitors. Genes Dev. 11 (7), 847–862.
Lev Bar-Or, R., Maya, R., Lee, A.S., Uri, A., Arnold, J.L., Moshe, O., 2000. Generation
of oscillations by the p53-Mdm2 feedback loop: a theoretical and experimental
study. Proc. Natl. Acad. Sci. U.S.A. 97, 11250–11255.
Li, G., Ho, V.C., 1998. p53-dependent DNA repair and apoptosis respond differently
to high- and low-dose ultraviolet radiation. Br. J. Dermatol. 139, 3–10.

<a id='19256105-1471-4475-a519-7b72574e6bf4'></a>

Li, J., Meyer, A.N., Donoghue, D.J., 1997. Nuclear localization of cyclin B1 mediates its biological activity and is regulated by phosphorylation. Proc. Natl. Acad. Sci. U.S.A. 94, 502-507.
Ling, H., Kulasiri, D., Samarasinghe, S., 2010. Robustness of G1/S checkpoint path-ways in cell cycle regulation based on probability of DNA-damaged cells passing as healthy cells. Biosystems 101, 213-221.
Matsumura, I., Tanaka, H., Kanakura, Y., 2003. E2F1 and c-Myc in cell growth and death. Cell Cycle 2 (4), 333-338.
Novak, B., Tyson, J.J., 2004. A model for restriction point control of the mammalian cell cycle. J. Theor. Biol. 230, 563-579.
Ohtsubo, M., Theodoras, A.M., Schumacher, J., Roberts, J.M., Pagano, M., 1995. Human cyclin E, a nuclear protein essential for the G1-to-S phase transition. Mol. Cell. Biol. 15, 2612-2624.
Parry, D., Bates, S., Mann, D.J., Peters, G., 1995. Lack of cyclin D-Cdk complexes in Rb-negative cells correlates with high levels of p16INK4/MTS1 tumour suppressor gene product. EMBO J. 14 (3), 503-511.
Pellegata, N.S., Antoniono, R.J., Redpath, J.L., Stanbridge, E.J., 1996. DNA damage and p53-mediated cell cycle arrest: a reevaluation. Proc. Natl. Acad. Sci. U.S.A. 93, 15209-15214.
Qu, Z., Weiss, J.N., MacLellan, W.R., 2003. Regulation of the mammalian cell cycle: a model of the G1-to-S transition. Am. J. Physiol. Cell Physiol. 284, 349-364.
Ragione, F.D., Russo, G.L., Oliva, A., Mercurio, C., Mastropietro, S., Pietra, V.D., Zappia, V., 1996. Biochemical characterization of p16INK4- and p18-containing com-plexes in human cell lines. J. Biol. Chem. 271, 15942-15949.
Roos, W.P., Kaina, B., 2006. DNA damage-induced cell death by apoptosis. Trends Mol. Med. 12 (9), 440-450.
Sheaff, R.J., Groudine, M., Gordon, M., Roberts, J.M., Clurman, B.E., 1997. Cyclin E-CDK2 is a regulator of p27kip1. Genes Dev. 11, 1464-1478.
Takizawa, C.G., Morgan, D.O., 2000. Control of mitosis by changes in the subcel-lular location of cyclin-B1-Cdk1 and Cdc25C. Curr. Opin. Cell Biol. 12, 658-665.
Tashima, Y., Kisaka, Y., Hanai, T., Hamada, H., Eguchi, Y., Okamoto, M., 2006. Math-ematical modeling of G2/M phase in cell cycle with involving the p53/Mdm2 oscillation system. Proc. Int. Fed. Med. Biomed. Eng. 14, 195-198.
Tashima, Y., Hamada, H., Okamoto, M., Hanai, T., 2008. Prediction of key factor con-trolling G1/S phase in the mammalian cell cycle using system analysis. J. Biosci. Bioeng. 106 (4), 368-374.
Tessema, M., Lehmann, U., Kreipe, H., 2004. Cell cycle and no end. Virchows Archiv. 444, 313-323.
Toettcher, J.E., Loewerc, A., Ostheimerd, G.J., Yaffe, M.B., Tidor, B., Lahav, G., 2009. Distinct mechanisms act in concert to mediate cell cycle arrest. Proc. Natl. Acad. Sci. U.S.A. 106 (3), 785-790.
Toyoshima, H., Hunter, T., 1994. p27, a novel inhibitor of G1 cyclin-Cdk protein kinase activity, is related to p21. Cell 78 (1), 67-74.
Wee, K.B., Surana, U., Aguda, B.D., 2009. Oscillations of the p53-Akt network: impli-cations on cell survival and death. PLoS ONE 4 (2), e4407.
Woo, R.A., Poon, R.Y., 2003. Cyclin-dependent kinases and S phase control in mam-malian cells. Cell Cycle 2 (4), 316-324.
Xiong, Y., Hannon, G.J., Zhang, H., Casso, D., Kobayashi, R., Beach, D., 1993. p21 is a universal inhibitor of cyclin kinases. Nature 366, 701-704.
Xu, N., Chang, D.C., 2007. Different thresholds of MPF inactivation are responsible for controlling different mitotic events in mammalian cell division. Cell Cycle 6 (13), 1639-1645.
Xu, M., Sheppard, K.A., Peng, C.Y., Yee, A.S., Piwnica-Worms, H., 1994. Cyclin A/CDK2 binds directly to E2F-1 and inhibits the DNA-binding activity of E2F-1/DP-1 by phosphorylation. Mol. Cell Biol. 14, 8420-8431.
Zachariae, W., Nasmyth, K., 1999. Whose end is destruction: cell division and the anaphase-promoting complex. Genes Dev. 13, 2039-2058.
Zhu, W., Giangrande, P.H., Nevins, J.R., 2004. E2Fs link the control of G1/S and G2/M transcription. EMBO J. 23, 4615-4626.

# Supplementary materials

<a id='d6dc688e-2141-409a-b3a2-2e5d86bd3a11'></a>

<::Biological Pathway Diagram:

The diagram illustrates a complex regulatory network involving various proteins and complexes, primarily focusing on cell cycle control. Nodes are represented by ellipses and reactions/interactions by arrows, with associated rate constants (k values).

**Top Left:**
- GFs (Growth Factors) activate CycD (k1).
- CycD is degraded or exits (k2).
- CycD and Cdk4 form CycD/Cdk4 complex (forward k3, reverse k4).

**Middle Section:**
- CycD/Cdk4 is degraded or exits (k44).
- p21 interacts with CycD/Cdk4 to form p21/CycD/Cdk4 complex (k19).
- p21/CycD/Cdk4 is degraded or exits (k18).
- p27 interacts with CycD/Cdk4 to form p27/CycD/Cdk4 complex (k20).
- p27/CycD/Cdk4 is degraded or exits (k21).

**Rb-E2F Pathway:**
- CycD/Cdk4, p21/CycD/Cdk4, and p27/CycD/Cdk4 all activate (phosphorylate) Rb/E2F to form Rb-PP/E2F (k46, k48, k47 respectively).
- Rb-PP/E2F is further phosphorylated by aCycE/Cdk2 (k49) and aCycA/Cdk2 (k50) to form Rb-PPP.
- Rb-PPP can dephosphorylate to Rb (k55).
- Rb-PPP releases E2F.
- E2F is degraded or exits (k52, k51, k53, k54).
- Rb can bind to E2F to form Rb/E2F (k45).
- Rb is degraded or exits (k57).

**p16 and Rb Regulation:**
- p16 is degraded or exits (k43).
- p16 and Rb can interact (k40, k42).
- p16 inhibits Rb (red T-bar, k41).
- Rb inhibits CycD/Cdk4, p21/CycD/Cdk4, and p27/CycD/Cdk4 complexes (red T-bars, k56, k58, k59).

**Myb Pathway:**
- E2F activates iB-Myb (k105).
- iB-Myb is converted to aB-Myb by aCycA/Cdk2 (k106).
- aB-Myb is degraded or exits (k107).

**Overall, the diagram illustrates the intricate interactions between cyclins, CDKs, CDK inhibitors (p21, p27, p16), and the Rb-E2F pathway, which are central to cell cycle progression and regulation.**
: diagram::>

<a id='4dff851a-3d9c-4d10-a0c6-ed25d97a6e0a'></a>

<::Biological pathway diagram showing interactions between various cell cycle regulators. The diagram consists of several oval-shaped nodes representing different proteins or protein complexes, and arrows indicating reactions or regulatory steps with associated rate constants (k values) and modifiers.nnNodes:n- iCdc25An- aCdc25An- CycEn- iCycE/Cdk2n- aCycE/Cdk2n- Cdk2n- CycAn- iCycA/Cdk2n- aCycA/Cdk2n- NF-Yn- p27/aCycE/Cdk2n- p27n- p21/aCycE/Cdk2n- p21n- p27/aCycA/Cdk2n- p21/aCycA/Cdk2nnReactions/Interactions:n- Input to iCdc25A (k80).n- iCdc25A to aCdc25A (k82).n- aCdc25A to iCdc25A (k85).n- iCdc25A degradation (k83, aChk1).n- aCdc25A degradation (k86, aChk1, k84).n- E2F activates CycE (k5).n- CycE degradation (k6).n- CycE and Cdk2 form iCycE/Cdk2 (k7, k16).n- iCycE/Cdk2 dissociates to CycE (k8).n- iCycE/Cdk2 to aCycE/Cdk2 (k23).n- aCycE/Cdk2 to iCycE/Cdk2 (k22).n- Cdk2 to aCycE/Cdk2 (k17).n- Cdk2 degradation/inactivation by aAPC/Cdc20, aAPC/Cdh1 (k14).n- Cdk2 and CycA form iCycA/Cdk2 (k15, k12).n- CycA degradation (k10).n- E2F, aB-Myb, NF-Y activate CycA (k130, k9, k75).n- CycA degradation/inactivation by aAPC/Cdc20, aAPC/Cdh1 (k126, k127).n- iCycA/Cdk2 to aCycA/Cdk2 (k29).n- aCycA/Cdk2 to iCycA/Cdk2 (k28, aCdc25A).n- NF-Y degradation (k89, k90).n- aCycE/Cdk2 to p27/aCycE/Cdk2 (k24).n- p27/aCycE/Cdk2 to p27 (k25).n- p27/aCycE/Cdk2 degradation/dissociation (k35, aCycE/Cdk2; k36, aCycA/Cdk2).n- p27 degradation (k34).n- aCycE/Cdk2 to p27 (k26).n- aCycE/Cdk2 to p21/aCycE/Cdk2 (k27).n- p21/aCycE/Cdk2 to p21 (k39).n- p21/aCycE/Cdk2 degradation (k30).n- p21 degradation (k38, p53; k37).n- aCycA/Cdk2 to p27/aCycA/Cdk2 (k32).n- p27/aCycA/Cdk2 degradation (k31).n- aCycA/Cdk2 to p21/aCycA/Cdk2 (k33).n- p21/aCycA/Cdk2 to p21.n- p21 activates iCycA/Cdk2.::>

<a id='18d049e2-20a6-4ee7-b50e-0498feb5ce4b'></a>

<::Biological pathway diagram showing interactions between various cell cycle regulators and their active/inactive forms, represented by nodes (oval shapes) and directed edges (arrows) with associated rate constants (k-values) or labels. The diagram includes the following components and their interactions:NF-Y activates CycB via k91.CycB is involved in a reversible reaction with iCycB/Cdk1cyto (k93, k92).Cdk1 activates iCycB/Cdk1cyto via k94.iCycB/Cdk1cyto activates aCycB/Cdk1cyto via k95.aCycB/Cdk1cyto is deactivated by aChk1 to iCycB/Cdk1cyto via k96.iCycB/Cdk1cyto transitions to iCycB/Cdk1nuc via k97.iCycB/Cdk1nuc transitions to iCycB/Cdk1cyto via k98.iCycB/Cdk1nuc activates aCycB/Cdk1nuc via k133.aCycB/Cdk1nuc is deactivated to iCycB/Cdk1nuc via k134.aCycB/Cdk1nuc transitions out via k136.aCycB/Cdk1nuc activates p21/aCycB/Cdk1 via k103.p21/aCycB/Cdk1 deactivates aCycB/Cdk1nuc via k104.p21 activates p21/aCycB/Cdk1.Wee1 is involved in a reversible reaction with Wee1p (k100, k101).Wee1p transitions out via k102.Wee1 deactivates aCycB/Cdk1nuc via k99.iCdc25C is activated by aCycB/Cdk1cyto or aCycB/Cdk1nuc to aCdc25C via k109.iCdc25C is deactivated by aChk1 to iCdc25C via k108.aCdc25C transitions out via k114.aCdc25C is deactivated by aChk1 to iCdc25C via k113.iCdc25C Ps216 is activated by aCycB/Cdk1cyto or aCycB/Cdk1nuc to aCdc25C Ps216 via k115.iCdc25C Ps216 is deactivated by aChk1 to iCdc25C Ps216 via k111.aCdc25C Ps216 transitions out via k116.aCdc25C Ps216 is deactivated by aChk1 to iCdc25C Ps216 via k112.14-3-3σ/iCdc25CPs216 transitions out via k121.14-3-3σ activates 14-3-3σ/iCdc25CPs216 via k120.14-3-3σ transitions out via k119.p53 activates 14-3-3σ via k117.aCycA/cdk2 activates 14-3-3σ via k118.iAPC/C^Cdh1 is involved in a reversible reaction with aAPC/C^Cdh1 (k124, k125).aCycB/Cdk1cyto activates iAPC/C^Cdh1 via k124.CycB activates aAPC/C^Cdh1 (k128, k129).iCycB/Cdk1nuc activates aAPC/C^Cdh1 (k135, k137).iAPC/C^Cdc20 is involved in a reversible reaction with aAPC/C^Cdc20 (k122, k123).aCycB/Cdk1nuc activates iAPC/C^Cdc20.aCycB/Cdk1cyto transitions to aCycB/Cdk1nuc via k131.aCycB/Cdk1nuc transitions to aCycB/Cdk1cyto via k132.::>

<a id='3a154dd9-8012-44c2-bdf9-0e391e343b7b'></a>

<::Flowchart illustrating a DNA damage response pathway.The pathway is initiated by a 'DNA damage signal' which is represented by a red jagged line.This signal leads to damaged DNA (represented by 'XXX' with a lightning bolt).From damaged DNA, an arrow labeled 'k72' points to 'Repair'.The 'DNA damage signal' also activates 'p53' (red arrow) and 'ATM/ATR' (red arrow).ATM/ATR is activated by damaged DNA (blue arrow labeled 'k78').ATM/ATR activates 'p53' (blue arrow labeled 'k60').p53 inhibits ATM/ATR (blue blunt-ended arrow labeled 'k61').p53 degrades (arrow labeled 'k62').ATM/ATR activates 'Im' (blue arrow labeled 'k79').ATM/ATR activates 'iChk1' (blue arrow labeled 'k88').iChk1 (inactive Chk1) converts to 'aChk1' (active Chk1), and 'aChk1' converts back to 'iChk1' (arrow labeled 'k87').p53 activates 'Im' (blue arrow labeled 'k70/k71').Im activates 'Mdm2' (blue arrow labeled 'k63').Im degrades (arrow labeled 'k67').Mdm2 inhibits 'p53' (red blunt-ended arrow).Mdm2 activates 'Im' (blue arrow labeled 'k66, k65').Mdm2 degrades (arrow labeled 'k64').: flowchart::>

<a id='75df0a18-4de7-4797-82ce-2497cf1443ac'></a>

<table id="0-1">
<tr><td id="0-2">Chemical species</td><td id="0-3">Initial value</td><td id="0-4">Chemical species</td><td id="0-5">Initial value</td><td id="0-6">Chemical species</td><td id="0-7">Initial value</td></tr>
<tr><td id="0-8">Y1</td><td id="0-9">3.00e-02</td><td id="0-a">Y19</td><td id="0-b">1.00e-03</td><td id="0-c">Y37</td><td id="0-d">1.00e-03</td></tr>
<tr><td id="0-e">Y2</td><td id="0-f">1.00e-03</td><td id="0-g">Y20</td><td id="0-h">1.95e+00</td><td id="0-i">Y38</td><td id="0-j">0</td></tr>
<tr><td id="0-k">Y3</td><td id="0-l">4.00e-05</td><td id="0-m">Y21</td><td id="0-n">1.00e-03</td><td id="0-o">Y39</td><td id="0-p">0</td></tr>
<tr><td id="0-q">Y4</td><td id="0-r">5.00e+00</td><td id="0-s">Y22</td><td id="0-t">0</td><td id="0-u">Y40</td><td id="0-v">0</td></tr>
<tr><td id="0-w">Y5</td><td id="0-x">1.50e+01</td><td id="0-y">Y23</td><td id="0-z">1.00e-02</td><td id="0-A">Y41</td><td id="0-B">0</td></tr>
<tr><td id="0-C">Y6</td><td id="0-D">7.50e+00</td><td id="0-E">Y24</td><td id="0-F">5.00e-02</td><td id="0-G">Y42</td><td id="0-H">1.00e-06</td></tr>
<tr><td id="0-I">Y7</td><td id="0-J">1.00e-03</td><td id="0-K">Y25</td><td id="0-L">2.65e-02</td><td id="0-M">Y43</td><td id="0-N">1.00e-06</td></tr>
<tr><td id="0-O">Y8</td><td id="0-P">1.00e-03</td><td id="0-Q">Y26</td><td id="0-R">2.35e-04</td><td id="0-S">Y44</td><td id="0-T">3.00e-02</td></tr>
<tr><td id="0-U">Y9</td><td id="0-V">4.00e-04</td><td id="0-W">Y27</td><td id="0-X">0</td><td id="0-Y">Y45</td><td id="0-Z">0</td></tr>
<tr><td id="0-10">Y10</td><td id="0-11">1.00e-04</td><td id="0-12">Y28</td><td id="0-13">1.00e-03</td><td id="0-14">Y46</td><td id="0-15">2.00e+00</td></tr>
<tr><td id="0-16">Y</td><td id="0-17">1.40e+01</td><td id="0-18">Y29</td><td id="0-19">1.00e-04</td><td id="0-1a">Y47</td><td id="0-1b">3.00e-02</td></tr>
<tr><td id="0-1c">Y12</td><td id="0-1d">1.00e-03</td><td id="0-1e">Y30</td><td id="0-1f">9.90e-01</td><td id="0-1g">Y48</td><td id="0-1h">9.00e-01</td></tr>
<tr><td id="0-1i">Y13</td><td id="0-1j">1.00e+00</td><td id="0-1k">Y31</td><td id="0-1l">1.00e-02</td><td id="0-1m">Y49</td><td id="0-1n">1.00e-01</td></tr>
<tr><td id="0-1o">Y14</td><td id="0-1p">1.00e-04</td><td id="0-1q">Y32</td><td id="0-1r">0</td><td id="0-1s">Y50</td><td id="0-1t">1.00e-01</td></tr>
<tr><td id="0-1u">Y15</td><td id="0-1v">0</td><td id="0-1w">Y33</td><td id="0-1x">0</td><td id="0-1y">Y51</td><td id="0-1z">9.00e-01</td></tr>
<tr><td id="0-1A">Y16</td><td id="0-1B">0</td><td id="0-1C">Y34</td><td id="0-1D">1.00e+01</td><td id="0-1E">Y52</td><td id="0-1F">0</td></tr>
<tr><td id="0-1G">Y17</td><td id="0-1H">0</td><td id="0-1I">Y35</td><td id="0-1J">1.00e-04</td><td id="0-1K">Y53</td><td id="0-1L">0</td></tr>
<tr><td id="0-1M">Y18</td><td id="0-1N">0</td><td id="0-1O">Y36</td><td id="0-1P">1.00e-04</td><td id="0-1Q">Im</td><td id="0-1R">0</td></tr>
</table>
Abbreviations are as follows: Y₁: CycD, Y₂: CycE, Y₃: CycA, Y₄: Cdk4, Y₅: Cdk2, Y₆: CycD/Cdk4, Y₇: iCycE/Cdk2, Y₈: aCycE/Cdk2, Y₉: iCycA/Cdk2, Y₁₀: aCycA/Cdk2, Y₁₁:
p27, Y₁₂: p27/CycD/Cdk4, Y₁₃: p27/CycE/Cdk2, Y₁₄: p27/CycA/Cdk2, Y₁₅: p21, Y₁₆: p21/CycD/Cdk4, Y₁₇: p21/CycE/Cdk2, Y₁₈: p21/CycA/Cdk2, Y₁₉: p16, Y₂₀: Rb/E2F, Y₂₁:
Rb-PP/E2F, Y₂₂: E2F, Y₂₃: Rb-PPP, Y₂₄: Rb, Y₂₅: p53, Y₂₆: Mdm2, Y₂₇: ATM/ATR, Y₂₈: iCdc25A, Y₂₉: aCdc25A, Y₃₀: iChk1, Y₃₁: aChk1, Y₃₂: NF-Y, Y₃₃: CycB, Y₃₄: Cdk1, Y₃₅:
iCycB/Cdk1cyto, Y₃₆: aCycB/Cdk1cyto, Y₃₇: Wee1, Y₃₈: Wee1p, Y₃₉: p21/CycB/Cdk1, Y₄₀: iB-Myb, Y₄₁: aB-Myb, Y₄₂: iCdc25C, Y₄₃: aCdc25C, Y₄₄: iCdc25CPs216, Y₄₅:
aCdc25CPs216, Y₄₆: 14-3-3σ, Y₄₇: 14-3-3σ/iCdc25CPS216, Y₄₈: iAPC/Ccdc20, Y₄₉: aAPC/Ccdc20, Y₅₀: iAPC/Ccdh1, Y₅₁: aAPC/Ccdh1, Y₅₂: iCycB/Cdk1nuc, Y₅₃:
aCycB/Cdk1nuc, Im: Intermediate, DDS: DNA damage signal

<a id='828383aa-2940-46a2-9806-dcd473cff6b4'></a>

<table id="0-1">
<tr><td id="0-2">Kinetic parameter</td><td id="0-3">Value</td><td id="0-4">Kinetic parameter</td><td id="0-5">Value</td><td id="0-6">Kinetic parameter</td><td id="0-7">Value</td><td id="0-8">Kinetic parameter</td><td id="0-9">Value</td></tr>
<tr><td id="0-a">k_1</td><td id="0-b">5.00e-04</td><td id="0-c">k_36</td><td id="0-d">1.50e-03</td><td id="0-e">k_71</td><td id="0-f">4.00e-03</td><td id="0-g">K106</td><td id="0-h">5.00e-02</td></tr>
<tr><td id="0-i">k_2</td><td id="0-j">5.00e-04</td><td id="0-k">k_37</td><td id="0-l">5.00e-05</td><td id="0-m">k_72</td><td id="0-n">1.00e-08</td><td id="0-o">K107</td><td id="0-p">2.00e-03</td></tr>
<tr><td id="0-q">k_3</td><td id="0-r">5.00e-03</td><td id="0-s">k_38</td><td id="0-t">1.00e-03</td><td id="0-u">k_73</td><td id="0-v">3.00e+00</td><td id="0-w">K108</td><td id="0-x">1.00e-05</td></tr>
<tr><td id="0-y">k_4</td><td id="0-z">2.50e-03</td><td id="0-A">k_39</td><td id="0-B">5.00e-03</td><td id="0-C">k_74</td><td id="0-D">7.72e-01</td><td id="0-E">K109</td><td id="0-F">1.00e-02</td></tr>
<tr><td id="0-G">k5</td><td id="0-H">1.00e-01</td><td id="0-I">K40</td><td id="0-J">2.00e-03</td><td id="0-K">K75</td><td id="0-L">1.00e-05</td><td id="0-M">k₁₁₀</td><td id="0-N">1.00e+00</td></tr>
<tr><td id="0-O">k6</td><td id="0-P">2.50e-03</td><td id="0-Q">K41</td><td id="0-R">5.00e-05</td><td id="0-S">K76</td><td id="0-T">5.56e-02</td><td id="0-U">k₁₁₁</td><td id="0-V">1.00e-03</td></tr>
<tr><td id="0-W">k7</td><td id="0-X">2.50e-03</td><td id="0-Y">k42</td><td id="0-Z">1.00e-04</td><td id="0-10">k77</td><td id="0-11">2.00e-02</td><td id="0-12">k₁₁₂</td><td id="0-13">1.00e-02</td></tr>
<tr><td id="0-14">k8</td><td id="0-15">2.50e-05</td><td id="0-16">K43</td><td id="0-17">5.00e-04</td><td id="0-18">k78</td><td id="0-19">2.00e-01</td><td id="0-1a">k₁₁₃</td><td id="0-1b">1.00e-03</td></tr>
<tr><td id="0-1c">ko</td><td id="0-1d">3.00e-04</td><td id="0-1e">K44</td><td id="0-1f">5.00e-04</td><td id="0-1g">K79</td><td id="0-1h">1.00e-02</td><td id="0-1i">k₁₁₄</td><td id="0-1j">1.00e-04</td></tr>
<tr><td id="0-1k">k10</td><td id="0-1l">5.00e-04</td><td id="0-1m">K45</td><td id="0-1n">5.00e-05</td><td id="0-1o">k80</td><td id="0-1p">4.00e-02</td><td id="0-1q">k₁₁₅</td><td id="0-1r">1.00e-02</td></tr>
<tr><td id="0-1s">k11</td><td id="0-1t">5.00e-04</td><td id="0-1u">K46</td><td id="0-1v">2.50e-03</td><td id="0-1w">K81</td><td id="0-1x">1.00e-03</td><td id="0-1y">K₁₁₆</td><td id="0-1z">1.00e+00</td></tr>
<tr><td id="0-1A">k12</td><td id="0-1B">2.00e-04</td><td id="0-1C">K47</td><td id="0-1D">2.50e-03</td><td id="0-1E">K82</td><td id="0-1F">5.00e-02</td><td id="0-1G">k₁₁₇</td><td id="0-1H">1.00e+00</td></tr>
<tr><td id="0-1I">k13</td><td id="0-1J">5.00e-04</td><td id="0-1K">K48</td><td id="0-1L">2.50e-03</td><td id="0-1M">K83</td><td id="0-1N">5.00e-03</td><td id="0-1O">K₁₁₈</td><td id="0-1P">1.00e-02</td></tr>
<tr><td id="0-1Q">K14</td><td id="0-1R">7.50e-03</td><td id="0-1S">K49</td><td id="0-1T">4.00e-02</td><td id="0-1U">K84</td><td id="0-1V">1.00e-03</td><td id="0-1W">k₁₁₉</td><td id="0-1X">1.00e+00</td></tr>
<tr><td id="0-1Y">k₁₅</td><td id="0-1Z">5.00e-03</td><td id="0-20">k₅₀</td><td id="0-21">2.50e-03</td><td id="0-22">k₈₅</td><td id="0-23">5.00e-03</td><td id="0-24">k₁₂₀</td><td id="0-25">1.00e+02</td></tr>
<tr><td id="0-26">k₁₆</td><td id="0-27">5.00e-03</td><td id="0-28">k₅₁</td><td id="0-29">5.00e-08</td><td id="0-2a">k₈₆</td><td id="0-2b">5.00e-04</td><td id="0-2c">k₁₂₁</td><td id="0-2d">1.00e+00</td></tr>
<tr><td id="0-2e">k₁₇</td><td id="0-2f">5.00e-02</td><td id="0-2g">k₅₂</td><td id="0-2h">5.00e-07</td><td id="0-2i">k₈₇</td><td id="0-2j">1.00e+00</td><td id="0-2k">k₁₂₂</td><td id="0-2l">5.00e-03</td></tr>
<tr><td id="0-2m">k₁₈</td><td id="0-2n">5.00e-04</td><td id="0-2o">k₅₃</td><td id="0-2p">5.00e-05</td><td id="0-2q">k₈₈</td><td id="0-2r">1.00e+00</td><td id="0-2s">k₁₂₃</td><td id="0-2t">1.00e-02</td></tr>
<tr><td id="0-2u">k₁₉</td><td id="0-2v">5.00e-03</td><td id="0-2w">k₅₄</td><td id="0-2x">1.00e-02</td><td id="0-2y">k₈₉</td><td id="0-2z">1.00e-03</td><td id="0-2A">k₁₂₄</td><td id="0-2B">1.00e-02</td></tr>
<tr><td id="0-2C">k20</td><td id="0-2D">5.00e-04</td><td id="0-2E">K55</td><td id="0-2F">5.00e-08</td><td id="0-2G">K90</td><td id="0-2H">5.00e-04</td><td id="0-2I">k125</td><td id="0-2J">5.00e-03</td></tr>
<tr><td id="0-2K">k21</td><td id="0-2L">5.00e-05</td><td id="0-2M">K56</td><td id="0-2N">5.00e-05</td><td id="0-2O">k91</td><td id="0-2P">2.00e-02</td><td id="0-2Q">k126</td><td id="0-2R">5.00e-03</td></tr>
<tr><td id="0-2S">k22</td><td id="0-2T">6.00e-03</td><td id="0-2U">K57</td><td id="0-2V">5.00e-03</td><td id="0-2W">k92</td><td id="0-2X">5.00e-03</td><td id="0-2Y">k127</td><td id="0-2Z">5.00e-03</td></tr>
<tr><td id="0-30">K23</td><td id="0-31">1.75e-03</td><td id="0-32">K58</td><td id="0-33">5.00e-05</td><td id="0-34">K93</td><td id="0-35">1.25e-03</td><td id="0-36">K128</td><td id="0-37">1.00e-03</td></tr>
<tr><td id="0-38">K24</td><td id="0-39">2.25e-02</td><td id="0-3a">k59</td><td id="0-3b">5.00e-04</td><td id="0-3c">K94</td><td id="0-3d">2.50e-04</td><td id="0-3e">k129</td><td id="0-3f">3.00e-01</td></tr>
<tr><td id="0-3g">K25</td><td id="0-3h">1.75e-04</td><td id="0-3i">K60</td><td id="0-3j">1.00e-04</td><td id="0-3k">k95</td><td id="0-3l">5.00e-02</td><td id="0-3m">k130</td><td id="0-3n">3.00e-06</td></tr>
<tr><td id="0-3o">k26</td><td id="0-3p">2.25e-02</td><td id="0-3q">K61</td><td id="0-3r">7.00e-02</td><td id="0-3s">K96</td><td id="0-3t">1.00e-04</td><td id="0-3u">k131</td><td id="0-3v">1.00e-02</td></tr>
<tr><td id="0-3w">K27</td><td id="0-3x">1.75e-04</td><td id="0-3y">k62</td><td id="0-3z">1.00e-03</td><td id="0-3A">K97</td><td id="0-3B">5.00e-03</td><td id="0-3C">k132</td><td id="0-3D">5.00e-05</td></tr>
<tr><td id="0-3E">k28</td><td id="0-3F">9.00e-04</td><td id="0-3G">K63</td><td id="0-3H">9.40e-04</td><td id="0-3I">k98</td><td id="0-3J">5.00e-03</td><td id="0-3K">k133</td><td id="0-3L">5.00e-04</td></tr>
<tr><td id="0-3M">k29</td><td id="0-3N">5.00e-05</td><td id="0-3O">K64</td><td id="0-3P">2.00e-02</td><td id="0-3Q">K99</td><td id="0-3R">2.00e-04</td><td id="0-3S">k134</td><td id="0-3T">1.00e-02</td></tr>
<tr><td id="0-3U">k30</td><td id="0-3V">2.50e-03</td><td id="0-3W">K65</td><td id="0-3X">9.50e+00</td><td id="0-3Y">k100</td><td id="0-3Z">1.00e-01</td><td id="0-40">k135</td><td id="0-41">5.00e-03</td></tr>
<tr><td id="0-42">k31</td><td id="0-43">1.75e-04</td><td id="0-44">K66</td><td id="0-45">1.00e+01</td><td id="0-46">K101</td><td id="0-47">1.00e+00</td><td id="0-48">K136</td><td id="0-49">5.00e-03</td></tr>
<tr><td id="0-4a">k32</td><td id="0-4b">2.50e-03</td><td id="0-4c">K67</td><td id="0-4d">5.00e-03</td><td id="0-4e">k102</td><td id="0-4f">1.00e+00</td><td id="0-4g">k137</td><td id="0-4h">3.00e-02</td></tr>
<tr><td id="0-4i">k33</td><td id="0-4j">1.75e-04</td><td id="0-4k">k68</td><td id="0-4l">5.00e-02</td><td id="0-4m">K103</td><td id="0-4n">2.25e-02</td><td id="0-4o">DDS</td><td id="0-4p">*</td></tr>
<tr><td id="0-4q">K34</td><td id="0-4r">5.00e-08</td><td id="0-4s">k69</td><td id="0-4t">8.00e-04</td><td id="0-4u">K104</td><td id="0-4v">1.75e-04</td><td id="0-4w"></td><td id="0-4x"></td></tr>
<tr><td id="0-4y">k35</td><td id="0-4z">5.00e-02</td><td id="0-4A">K70</td><td id="0-4B">6.00e+00</td><td id="0-4C">K105</td><td id="0-4D">5.00e-02</td><td id="0-4E"></td><td id="0-4F"></td></tr>
</table>

<a id='a142bcbc-1f1a-4747-bf7b-1bbf8480e8c2'></a>

* The values of DDS were as follows: 0 (No-damage), 0.002 (Low-damage), 0.004 (Medium-damage), 0.008 (High-damage), and 0.016 (Excess-damage).

<a id='b60870da-fd20-4fbb-b2d5-292cdfc4d2a5'></a>

dY₁/dt = k₁ + k₄Y₆ - (k₂ + k₃Y₄)Y₁
dY₂/dt = k₅Y₂₂ + k₈Y₇ - (k₆ + k₇Y₅)Y₂
dY₃/dt = k₉Y₄₁ + k₁₃₀Y₂₂ + k₁₂Y₉ + k₇₅Y₃₂ - (k₁₀ + k₁₁Y₅ + k₁₂₆Y₄₉ + k₁₂₇Y₅₁)Y₃
dY₄/dt = k₄Y₆ + k₁₃Y₆ - k₃Y₁Y₄
dY₅/dt = k₈Y₇ + k₁₂Y₉ + k₁₄Y₁₀(Y₄₉ + Y₅₁) + k₁₅Y₉(Y₄₉ + Y₅₁) + k₁₆Y₇ + k₁₇Y₈Y₈ - (k₇Y₂ + k₁₁Y₃)Y₅
dY₆/dt = k₃Y₁Y₄ + k₁₉Y₁₆ + k₂₁Y₁₂ - (k₄ + k₁₃ + k₁₈Y₁₅ + k₂₀Y₁₁ + k₄₄Y₁₉)Y₆
dY₇/dt = k₇Y₂Y₅ + k₂₃Y₈ - (k₈ + k₂₂Y₂₉ + k₁₆)Y₇
dY₈/dt = k₂₂Y₇Y₂₉ + k₂₅Y₁₃ + k₂₇Y₁₇ - (k₂₃ + k₂₄Y₁₁ + k₂₆Y₁₅ + k₁₇Y₈)Y₈
dY₉/dt = k₁₁Y₃Y₅ + k₂₉Y₁₀ - (k₁₂ + k₂₈Y₂₉ + k₁₅(Y₄₉ + Y₅₁))Y₉
dY₁₀/dt = k₂₈Y₉Y₂₉ + k₃₁Y₁₄ + k₃₃Y₁₈ - (k₂₉ + k₃₀Y₁₁ + k₃₂Y₁₅ + k₁₄(Y₄₉ + Y₅₁))Y₁₀
dY₁₁/dt = k₃₄ + k₂₁Y₂₁ + k₂₅Y₁₃ + k₃₁Y₁₄ - (k₃₅Y₈ + k₃₆Y₁₀ + k₂₀Y₆ + k₂₄Y₈ + k₃₀Y₁₀)Y₁₁
dY₁₂/dt = k₂₀Y₆Y₁₁ - k₂₁Y₁₂
dY₁₃/dt = k₂₄Y₈Y₁₁ - k₂₅Y₁₃
dY₁₄/dt = k₃₀Y₁₀Y₁₁ - k₃₁Y₁₄
dY₁₅/dt = k₃₇ + k₃₈Y₂₅ + k₁₉Y₁₆ + k₂₇Y₁₇ + k₃₃Y₁₈ + k₁₀₄Y₃₉ - (k₃₉ + k₁₈Y₆ + k₂₆Y₈ + k₃₂Y₁₀ + k₁₀₃Y₅₃)Y₁₅
dY₁₆/dt = k₁₈Y₆Y₁₅ - k₁₉Y₁₆
dY₁₇/dt = k₂₆Y₈Y₁₅ - k₂₇Y₁₇
dY₁₈/dt = k₃₂Y₁₀Y₁₅ - k₃₃Y₁₈
dY₁₉/dt = k₄₀ + k₄₁/(1 + k₄₂Y₂₄) - (k₄₃ + k₄₄Y₆)Y₁₉
dY₂₀/dt = k₄₅Y₂₂Y₂₄ - (k₄₆Y₆ + k₄₇Y₁₂ + k₄₈Y₁₆)Y₂₀
dY₂₁/dt = k₄₆Y₆Y₂₀ + k₄₇Y₁₂Y₂₀ + k₄₈Y₁₆Y₂₀ - (k₄₉Y₈ + k₅₀Y₁₀)Y₂₁
dY₂₂/dt = k₄₉Y₈Y₂₁ + k₅₀Y₁₀Y₂₁ + k₅₁Y₂₂ + k₅₂ - (k₄₅Y₂₄ + k₅₃ + k₅₄Y₁₀)Y₂₂
dY₂₃/dt = k₄₉Y₈Y₂₁ + k₅₀Y₁₀Y₂₁ - k₅₅Y₂₃
dY₂₄/dt = k₅₆ + k₅₈/(1 + k₅₉Y₁₉) + k₅₅Y₂₃ - (k₅₇ + k₄₅Y₂₂)Y₂₄
dY₂₅/dt = k₆₀ + k₆₁Y₂₇ - (deg(t)Y₂₆ + k₆₂)Y₂₅
dY₂₆/dt = k₆₃ + (k₆₆Im⁵⁰)/(k₆₅⁵⁰ + Im⁵⁰) - k₆₄Y₂₆
dY₂₇/dt = k₇₈sig(t) - k₇₉Y₂₇
dY₂₈/dt = k₈₀Y₂₂ + k₈₅Y₂₉ - (k₈₁Y₃₁ + k₈₂(Y₈ + Y₁₀) + k₈₃)Y₂₈
dY₂₉/dt = k₈₂(Y₈ + Y₁₀)Y₂₈ - (k₈₄Y₃₁ + k₈₅ + k₈₆)Y₂₉
dY₃₀/dt = k₈₇Y₃₁ - k₈₈Y₂₇Y₃₀
dY₃₁/dt = k₈₈Y₂₇Y₃₀ - k₈₇Y₃₁
dY₃₂/dt = k₈₉Y₁₀ - k₉₀Y₃₂
dY₃₃/dt = k₉₁Y₃₂ + k₉₄Y₃₅ - (k₉₂ + k₉₃Y₃₄ + k₁₂₈Y₄₉ + k₁₂₉Y₅₁)Y₃₃
dY₃₄/dt = k₉₄Y₃₅ + k₉₇Y₃₅(Y₄₉ + Y₅₁) + k₉₈Y₃₆(Y₄₉ + Y₅₁) - k₉₃Y₃₃Y₃₄
dY₃₅/dt = k₉₃Y₃₃Y₃₄ + k₉₆Y₃₆ - (k₉₄ + k₉₅(Y₄₃ + Y₄₅) + k₉₇(Y₄₉ + Y₅₁))Y₃₅
dY₃₆/dt = k₉₅(Y₄₃ + Y₄₅)Y₃₅ + k₁₃₂Y₅₃ - (k₉₆ + k₉₈(Y₄₉ + Y₅₁) + k₁₃₁Y₃₆)Y₃₆
dY₃₇/dt = k₉₉ + k₁₀₁Y₃₈ - k₁₀₀Y₅₃Y₃₇
dY₃₈/dt = k₁₀₀Y₅₃Y₃₇ - (k₁₀₁ + k₁₀₂)Y₃₈
dY₃₉/dt = k₁₀₃Y₅₃Y₁₅ - k₁₀₄Y₃₉
dY₄₀/dt = k₁₀₅Y₂₂ - k₁₀₆Y₁₀Y₄₀
dY₄₁/dt = k₁₀₆Y₁₀Y₄₀ - k₁₀₇Y₄₁
dY₄₂/dt = k₁₀₈ + k₁₀₉Y₄₃ - (k₁₁₀(Y₃₆ + Y₅₃) + k₁₁₁Y₃₁)Y₄₂
dY₄₃/dt = k₁₁₀(Y₃₆ + Y₅₃)Y₄₂ + k₁₁₂Y₄₅ - (k₁₀₉Y₄₃ + k₁₁₃Y₃₁ + k₁₁₄)Y₄₃
dY₄₄/dt = k₁₁₁Y₃₁Y₄₂ + k₁₁₅Y₄₅ - (k₁₁₆(Y₃₆ + Y₅₃) + k₁₂₀Y₄₆)Y₄₄
dY₄₅/dt = k₁₁₃Y₃₁Y₄₃ + k₁₁₆(Y₃₆ + Y₅₃)Y₄₄ - (k₁₁₅ + k₁₁₂)Y₄₅
dY₄₆/dt = k₁₁₇ + k₁₁₈Y₂₅ - (k₁₁₉ + k₁₂₀Y₄₄)Y₄₆

<!-- PAGE BREAK -->

<a id='ab5469cf-48df-4954-9949-32d06c80e8fe'></a>

dY47/dt = k120Y44Y46 - k121Y47
dY48/dt = k122Y49Y51 - k123Y48Y53
dY49/dt = k123Y48Y53 - k122Y49Y51
dY50/dt = k124Y51(Y53 + Y10) - k125Y50
dY51/dt = k125Y50 - k124Y51(Y53 + Y10)
dY52/dt = k133Y53Y37 - (k134(Y43 + Y45) + k136(Y49 + Y51))Y52
dY53/dt = k131Y36Y36 + k134(Y43 + Y45)Y52 + k104Y39 - (k132 + k133Y37 + k135Y49 + k137Y51 + k103Y15)Y53
dIm/dt = k70Y25sig(t)/(1 + k71Y25Y26) - k67Im
sig(t) = DDS * exp(-k72 * time)
deg(t) = k76 - k74 * (sig(t) - DDS * exp(-k77 * DDS * time))

<a id='b3dce124-8c95-4f97-ac80-bb00d9bc07c5'></a>

Abbreviations are shown in Table S1.
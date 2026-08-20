<a id='5ca03456-8140-43d8-9044-e67ec0c995a3'></a>

<::logo: [Unknown]Check for updatesA small, gray square button with a colorful circular icon featuring a red flag-like shape inside.::>

<a id='7d7ad5fc-a4a0-4151-9da4-3bcad1f60818'></a>

A comprehensive model for the proliferation-
quiescence decision in response to endogenous DNA
damage in human cells

<a id='3dbc1c7d-f4f9-4de2-b9ea-d30497c433ad'></a>

Frank S. Heldta,1,2, Alexis R. Barrb,1, Sam Cooperb,c, Chris Bakalb, and Béla Nováka,2

*Department of Biochemistry, University of Oxford, OX1 3QU Oxford, United Kingdom; bDivision of Cancer Biology, The Institute of Cancer Research, SW3 6JB London, United Kingdom; and cDepartment of Computational Systems Medicine, Imperial College, SW7 2AZ London, United Kingdom

<a id='f8cacc77-4a50-4206-956f-31b1a98e25bb'></a>

Edited by Tim Hunt, Cancer Research UK, London, United Kingdom, and approved January 29, 2018 (received for review August 31, 2017)

<a id='5c9655dd-eb5b-4400-be0a-d42eb95cc4fe'></a>

Human cells that suffer mild DNA damage can enter a reversible state of growth arrest known as quiescence. This decision to temporarily exit the cell cycle is essential to prevent the propagation of mutations, and most cancer cells harbor defects in the underlying control system. Here we present a mechanistic mathematical model to study the proliferation-quiescence decision in nontransformed human cells. We show that two bistable switches, the restriction point (RP) and the G1/S transition, mediate this decision by integrating DNA damage and mitogen signals. In particular, our data suggest that the cyclin-dependent kinase inhibitor p21 (Cip1/Waf1), which is expressed in response to DNA damage, promotes quiescence by blocking positive feedback loops that facilitate G1 progression downstream of serum stimulation. Intriguingly, cells exploit bistability in the RP to convert graded p21 and mitogen signals into an all-or-nothing cell-cycle response. The same mechanism creates a window of opportunity where G1 cells that have passed the RP can revert to quiescence if exposed to DNA damage. We present experimental evidence that cells gradually lose this ability to revert to quiescence as they progress through G1 and that the onset of rapid p21 degradation at the G1/S transition prevents this response altogether, insulating S phase from mild, endogenous DNA damage. Thus, two bistable switches conspire in the early cell cycle to provide both sensitivity and robustness to external stimuli.

<a id='9e22cf67-bd02-417f-b1b8-03bad421100e'></a>

cell cycle | DNA damage | proliferation-quiescence decision | mathematical
modelling | live-cell imaging

<a id='3bc7fbff-be74-4fee-b88f-b140f0e7354f'></a>

Living systems strive to proliferate and to protect their genomic information from harm. On the cellular level, these two aims have to be balanced to avoid the accumulation of deleterious mutations that can lead to cell death or cancer. Therefore, cells have evolved mechanisms to postpone proliferation in response to DNA damage. In particular, they can enter a reversible state of growth arrest after mitosis known as quiescence (1), which provides time for DNA repair and prevents the propagation of damage to future generations. However, how and when the decision between proliferation and quiescence is made, and how decision-making is implemented on a molecular level, remains elusive.

<a id='caa2226a-50c6-4c24-9581-5db71f88ef3c'></a>

Cell proliferation is regulated by a series of steps known as the cell cycle, which is driven by cyclin-dependent kinases (Cdks) and their regulatory counterparts, the cyclins (2, 3). The activation of Cdk2 by either cyclin E (CycE) or cyclin A (CycA) controls commitment to proliferation and initiation of DNA synthesis (4). However, Cdk2 activity can be opposed by p21 (Cip1/Waf1), a stoichiometric inhibitor that is under the control of the DNA damage-induced transcription factor p53 (5, 6). Thus, p21 acts as a damage-dependent brake on cell-cycle progression. p21 can also bind to proliferating cell nuclear antigen (PCNA), a vital component of the DNA replication machinery (7), where it competes with DNA processivity factors for PCNA binding and thus blocks DNA synthesis directly (8–10). These mechanisms enable p21 to maintain genome stability downstream of DNA damage by preventing the propagation of mutations to future cellular generations, which could otherwise lead to decreased

<a id='2da3cd7e-792b-44f3-ae8d-864f37cb3de7'></a>

cell fitness or tumorigenesis. This is consistent with observations
that p21 mouse models show enhanced tumorigenesis (6, 11)
and that p21 is required for the maintenance of hematopoietic
and forebrain neural stem cells (12, 13).

<a id='083c1430-aebd-4a27-8556-65d6d22d72be'></a>

Using live single-cell imaging, Spencer et al. (14) have shown that, following mitosis, proliferating cells bifurcate into one pop- ulation that rapidly accumulates Cdk2 activity and reenters the cell cycle and another, quiescent population where Cdk2 activity is down-regulated. This bifurcation is controlled by both mitogen stimulation and p21 expression (14, 15). Recently, we and others have observed that p21 protein levels show high cell-to-cell vari- ability in genetically identical, nontransformed cells due to in- trinsic DNA damage suffered during unperturbed growth (16, 17). Frequently, this damage occurs during DNA replication, causing p21 accumulation in the G2 and M phases of a mother cell's cycle. p21 is then inherited by daughter cells at cell division and deter- mines their decision to proliferate. These results suggest that p21 is part of a control system that integrates information across generations to determine cell fate. In addition, the proliferation- quiescence decision appears to be reversible since DNA damage or extrinsic stress applied in G1 can revert cells back to a quiescent state (18). This window of reversibility is thought to be closed by the inactivation of the anaphase-promoting complex/cyclosome (APC/Cdh1), a ubiquitin ligase that targets many cell-cycle regu- lators for degradation during G1, including CycA.

<a id='4c226f38-d3ff-47f0-abec-8b3d43d68e28'></a>

### Significance

Controlled transitions of human cells between proliferating and nonproliferating states are essential for normal development and tissue homeostasis. To understand how the decision to proliferate is made in response to positive input from growth factors and negative input from the DNA damage response, we have built a mathematical model of the underlying molecular network, based on data from live cell-imaging experiments. Our model suggests that two major cell-cycle transitions are crucial for decision making: the restriction point, which integrates pro- and antiproliferative signals, and the G1/S transition, which temporarily insulates cells from some aspects of the DNA damage response. Together, our model gives mechanistic insight into how cells maintain both sensitivity and robustness to external signals.

<a id='264fdfbb-a1d6-471d-833f-a4598ddaaf13'></a>

Author contributions: F.S.H., A.R.B., C.B., and B.N. designed research; F.S.H., A.R.B., C.B., and B.N. performed research; F.S.H., A.R.B., S.C., and B.N. analyzed data; and F.S.H., A.R.B., and B.N. wrote the paper.

<a id='f1bf2583-eeb4-44d0-9c2c-aabe1fe69b94'></a>

The authors declare no conflict of interest.

<a id='3162328c-0175-4720-b3b3-33316a525193'></a>

This article is a PNAS Direct Submission.
Published under the PNAS license.

<a id='104aa5c1-b6a7-4e2f-bde6-927cbdbc8821'></a>

1F.S.H. and A.R.B. contributed equally to this work.
2To whom correspondence may be addressed. Email: stefan.heldt@bioch.ox.ac.uk or bela. novak@bioch.ox.ac.uk.

<a id='e94a1fb7-6a36-4dcb-9550-c3ff2543656f'></a>

This article contains supporting information online at www.pnas.org/lookup/suppl/doi:10.
1073/pnas.1715345115/-/DCSupplemental.
Published online February 20, 2018

<a id='e3d4b87f-7242-4f75-9a08-d0946fa600ff'></a>

2532-2537 | PNAS | March 6, 2018 | vol. 115 | no. 10

<a id='adf8c916-2098-4794-9236-2db224d20007'></a>

www.pnas.org/cgi/doi/10.1073/pnas.1715345115

<!-- PAGE BREAK -->

<a id='8cbe213c-3873-4edc-b056-016f39eaf2b9'></a>

Motivated by these experiments, we aimed to gain a systems-level understanding of the proliferation-quiescence decision and its response to endogenous, naturally occurring DNA damage. In a previous study, we developed and experimentally validated a mathematical model for p21 regulation, revealing a bistable switch at the G1/S transition that controls p21 degradation (16). Here, we augment this model with the restriction point (RP), a second major cell-cycle transition that gates cell-cycle entry. We show that, by promoting p21 synthesis, DNA damage can prevent passage through the RP and that, due to its bistable nature, the RP converts a graded p21 signal into an all-or-nothing cell-cycle decision. Our model also suggests that DNA damage in post-RP G1 can reverse the decision to proliferate and reset cells to a pre-RP state. This window of reversibility ends at the G1/S transition when rapid p21 degradation prevents a response to DNA damage, which is vital to avoid premature S-phase exit. Finally, we show that G1 cells progressively lose the ability to revert to quiescence as they approach the G1/S transition and that the loss of G1 regulators compromises the control system leading to different forms of dysregulated growth. Hence, our study demonstrates how cellular decision-making integrates information over time and how bistable switches can make cells both sensitive and tolerant to external stimuli.

<a id='c2043535-aa22-4620-b95e-feab576c222c'></a>

## Results

**Developing a Model for Early Cell-Cycle Regulation.** To understand the control of cell-cycle entry and subsequent progression, we built a mechanistic mathematical model of the underlying regulatory network (Fig. 1A). Our model links the two main transitions of early cell-cycle regulation: the RP, where cells commit to proliferation, and the G1/S transition, marking the onset of DNA replication (see _SI Appendix_ for details). The G1/S module of the model is based on our previous work on p21 dynamics (16) extended here by explicitly distinguishing between CycE and CycA. G1 progression was modeled as follows: Passage through the RP requires growth factor-dependent hyperphosphorylation of the retinoblastoma protein (Rb), which alleviates inhibition of E2F transcription factors (19). Once active, E2Fs drive their own expression as well as the synthesis of CycE and CycA, both of which promote Cdk2 activity, further reinforcing Rb inhibition (20, 21). E2F-dependent transcription also causes expression of the early mitotic inhibitor (Emi1), an inhibitor of APC/C<sup>Cdh1</sup> (Cdh1), which is responsible for degradation of CycA during G1. Increasing levels of CycE:Cdk2 and CycA:Cdk2 then activate replication complexes (aRCs), initiating S phase. DNA damage can halt this process by up-regulating p53, which causes p21 expression, inhibiting both Cdk2 activity and DNA replication (5, 6). This is counteracted by two p21 degradation pathways depending on either Cdk2 or PCNA in aRCs (22).

<a id='5e75f983-5332-45c3-a21b-a31d70c0c790'></a>

Deterministic simulations of this model show a distinct peak in
CycE:Cdk2 levels as well as an abrupt increase in CycA:Cdk2, at
the G1/S transition (Fig. 1B), in good agreement with quantitative
live-cell imaging data (23). Here, the accumulation of CycA is fa-
cilitated by the rapid inactivation of Cdh1 at S-phase entry, which is
caused by both Emil expression and increased Cdk2 activity. We
also observe the presence of p21 both before and after S phase,
while the inhibitor is absent during DNA replication, as has been
shown experimentally (24). To capture the large cell-to-cell het-
erogeneity in p21 protein levels that has been reported, we per-
formed stochastic simulations (Fig. 1C, Top). We assumed that
DNA damage occurs randomly throughout the cell cycle but is
more likely to occur during S phase, when chromosome replication
takes place (25). The resulting simulations recapitulate both the
spread and general pattern of experimental p21 levels (Fig. 1 C and
D) as well as the length of G1 and S phase (Fig. 1E), suggesting
that we can use the model to further analyze p21 dynamics in the
early cell cycle.

<a id='c6c0a397-6836-4492-8091-2df6692aa2d1'></a>

<::chart: A model of early cell-cycle progression::>

<::flowchart: (A) Influence diagram of the cell-cycle model::>
RP and G1 progression:
- GF activates Rb
- Rb inhibits E2F
- E2F activates CycE Cdk2
- E2F activates CycA Cdk2
- p21 inhibits CycE Cdk2
- CycE Cdk2 inhibits Rb
- CycE Cdk2 activates Emi1
- CycA Cdk2 activates Emi1
- Emi1 inhibits Cdh1
- Cdh1 inhibits CycA Cdk2

G1/S transition:
- p21 inhibits CycE Cdk2
- p21 inhibits CycA Cdk2
- CycE Cdk2 activates aRC
- CycA Cdk2 activates aRC
- aRC activates S-phase
- Damage activates p53
- p53 activates p21
- Cdh1 inhibits CycA Cdk2

<::line graph: (B) Deterministic simulation of the model in A::>
- X-axis: time from cytokinesis (h), from 0 to 20.
- Top Y-axis: rel. level (AU), from 0 to 2.
  - S-phase is a shaded area from approximately 8 to 18 hours.
  - Lines show the relative levels of: p21 (green, low, small peak around 7h), aRC (brown, rises after 8h), CycE (light blue, peaks around 8-10h), CycA (purple, rises after 10h).
- Bottom Y-axis: rel. level (AU), from 0 to 4.
  - Lines show the relative levels of: act. Cdh1 (dark brown, high, drops around 8h, rises after 18h), Emi1 (orange, low, rises after 8h).

<::line graph: (C) p21 levels from stochastic simulations (Top; n = 30) and experiments in individual hTert-RPE1 cells (Bottom; n = 29)::>
- X-axis: time from G1/S transition (h), from -5 to 15.
- S-phase is a shaded area from 0 to 8 hours.
- Top panel (Simulation):
  - Y-axis: p21 (AU), from 0 to 2.
  - Multiple green lines show p21 levels, generally low during S-phase and rising afterward.
- Bottom panel (Experiment):
  - Y-axis: p21 (AU), from 0 to 50.
  - Multiple green lines show p21 levels, generally low during S-phase and rising afterward.

<::scatter plot: (D) Maximum p21 level in G1 and G2 phase in stochastic simulations (Sim; n = 200) and experiments (Exp; n = 186)::>
- Y-axis: rel. p21 level (-), from 0 to 6.
- X-axis categories: G1 and G2.
- Data points for Sim (green circles) and Exp (red circles) are shown for both G1 and G2.
- Labels above the data indicate "n.s." (not significant) for both G1 and G2 comparisons.

<::scatter plot: (E) Comparison of G1- and S-phase lengths in stochastic simulations (Sim; n = 200) and experiments (Exp; n = 186)::>
- Y-axis: phase length (h), from 0 to 20.
- X-axis categories: G1 and S.
- Data points for Sim (green circles) and Exp (red circles) are shown for both G1 and S.
- Labels above the data indicate "n.s." (not significant) for both G1 and S comparisons.

<::line graph: (F) Stochastic simulation of a cell that suffers DNA damage in G1/S transition phase::>
- X-axis: time from cytokinesis (h), from 0 to 20.
- Y-axis: rel. level (AU), from 0 to 1.5.
- A black square pulse labeled "damage" is present from approximately 2 to 7 hours.
- S-phase is a shaded area from approximately 8 to 13 hours.
- A green line labeled "p21" shows the p21 level, which rises during the damage period, then drops, and rises again after S-phase.

<::line graph: (G) Stochastic simulation of a cell that suffers DNA damage in S-phase::>
- X-axis: time from cytokinesis (h), from 0 to 20.
- Y-axis: rel. level (AU), from 0 to 1.5.
- S-phase is a shaded area from approximately 8 to 13 hours.
- A black square pulse labeled "damage" is present from approximately 8 to 13 hours, coinciding with S-phase.
- A green line shows the p21 level, which rises during the damage period in S-phase and remains elevated afterwards.

<a id='5cc5d35a-9750-4adf-968e-467a03753b36'></a>

Our model attributes the heterogeneity in p21 levels primarily to the stochasticity of DNA damage—that is, the spontaneous occurrence and subsequent repair of DNA lesions. However, we also observe a dependence of p21 expression on the cell-cycle stage (Fig. 1 F and G). In particular, DNA damage in G1 phase causes an immediate increase in p21 (Fig. 1F), while S-phase cells do not show such an increase and delay p21 accumulation until after the completion of DNA replication (Fig. 1G). As previously described, this is due to the presence of a bistable switch at the G1/ S transition (ref. 16 and SI Appendix, Fig. S1 A and B). This switch promotes rapid p21 degradation during DNA replication (SI Appendix, Fig. S1C), while it allows p21 levels to vary in G1 and G2 phase. Thus, intrinsic DNA damage that occurs during S phase results in elevated p21 protein levels in G2, and these elevated levels may persist for some time, even after the damage has been repaired (Fig. 1F).

<a id='a98ab403-6161-4302-9c6f-deba3b9ae3cf'></a>

**Inherited p21 Promotes Quiescence by Blocking Passage Through the RP.** Having observed that DNA damage generated during DNA synthesis can lead to increased p21 expression only after S-phase exit, we wanted to understand how this affects cell-cycle progression. Single-cell imaging data during unperturbed growth suggests that a moderate increase in p21 levels in G2 or M phase does not impair progression through these stages (Fig. 24). Instead, p21 protein is transferred from mother to daughter cells, where it can promote quiescence (16). Consistent with this, quiescent cells have been shown to contain high amounts of p21 as well as increased levels of hypophosphorylated Rb (14). The Rb

<a id='d7049708-9249-4204-b57f-ca810a2cc92b'></a>

Heldt et al.

<a id='32bad238-a3ed-4dee-8999-936b210f6ca2'></a>

PNAS | March 6, 2018 | vol. 115 | no. 10 | 2533

<a id='5b90c29a-da76-4228-8770-3da88de02b5e'></a>

<::logo: PNAS
PNAS
This logo features the acronym "PNAS" in a dark blue, sans-serif font, oriented vertically.::>

<a id='2e16ad73-32a4-42a2-8597-a83abe6fc2bc'></a>

SYSTEMS BIOLOGY

<!-- PAGE BREAK -->

<a id='599425f8-9f46-4e90-b752-bc7de48bb7e8'></a>

<::figure: Fig. 2. p21 impairs RP passage.
(A) A line graph titled "p21 (AU)" on the y-axis versus "time (h)" on the x-axis. The y-axis ranges from 0 to 100. The x-axis ranges from 0 to 60. A green line shows the p21 level over time. Shaded regions indicate "S-phase" from approximately 5-15 h and 25-35 h. Dashed vertical lines indicate "division" at approximately 5 h, 15 h, 20 h, 35 h, and 40 h. The p21 level is generally low, with spikes around the division and S-phase regions, and then increases significantly after 40 h.
(B) A subnetwork diagram. Growth Factor (GF) activates Rb. Rb inhibits E2F. E2F activates CycE Cdk2 and CycA Cdk2. CycE Cdk2 and CycA Cdk2 both activate E2F, forming two positive feedback loops (+). p21 inhibits CycE Cdk2 and CycA Cdk2. The diagram shows GF -> Rb -| E2F -> CycE Cdk2 -> E2F and E2F -> CycA Cdk2 -> E2F. p21 -| CycE Cdk2 and p21 -| CycA Cdk2.
(C) A bifurcation diagram showing "active E2F (AU)" on the y-axis versus "growth factors (AU)" on the x-axis. The y-axis ranges from 0 to 1. The x-axis ranges from 0 to 1. A solid purple line represents a stable steady state labeled "prolif." (proliferating) at high E2F activity. A solid purple line represents a stable steady state labeled "quies." (quiescent) at low E2F activity. A dashed purple line represents an unstable steady state connecting the two. An arrow pointing upwards from "quies." to "prolif." is labeled "RP passage".
(D) A bifurcation diagram showing "active E2F (AU)" on the y-axis versus "p21 (AU)" on the x-axis. The y-axis ranges from 0 to 1. The x-axis ranges from 0 to 2. A solid purple line represents a stable steady state labeled "prolif." at high E2F activity. A solid purple line represents a stable steady state labeled "quies." at low E2F activity. A dashed purple line represents an unstable steady state connecting the two. Arrows indicate the fate of cells, moving towards either the "prolif." or "quies." state depending on the p21 level relative to the threshold.
(E) A line graph showing "p21 (AU)" on the y-axis versus "time from cytokinesis (h)" on the x-axis. The y-axis ranges from 0 to 1. The x-axis ranges from 0 to 20. Two example traces are shown: a green line labeled "prolif." which decreases from approximately 0.5 to 0.1 over 20 h, and a gray line labeled "quies." which remains around 0.8-0.9 over 20 h. To the right of the graph, marginal histograms depict initial p21 levels for additional simulations, grouped into quiescent (gray bars) and proliferating (green bars) cells (n = 500). The gray bars are concentrated at higher p21 levels, and green bars at lower p21 levels.
(F) A line graph showing "Cdk2 activity (AU)" on the y-axis versus "time from cytokinesis (h)" on the x-axis. The y-axis ranges from 0 to 2. The x-axis ranges from 0 to 20. Multiple blue lines represent "prolif." cells, showing increasing Cdk2 activity from 0 to 2 over 20 h. Multiple gray lines represent "quies." cells, showing Cdk2 activity remaining near 0 over 20 h (n = 30). (A) Experimental data of a cell that enters the cell cycle twice before becoming quiescent. (B) Subnetwork of the RP comprising two positive feedback loops (+). (C) Stable (solid) and unstable (dashed) steady states of E2F activity with respect to growth factor signaling. Diagram was calculated from the model in the absence of p21 using the subnetwork in B. (D) E2F activity in response to p21 at high growth factor levels based on the subnetwork in B. Arrows indicate the fate of cells on either side of the threshold. Total p21 levels were kept constant at the indicated level. (E) Stochastic simulations of two cells with different initial p21 levels using the full model in Fig. 1A. Marginal histograms depict initial p21 levels of additional simulations grouped into quiescent (gray) and proliferating (green) cells (n = 500). (F) Cdk2 activity from stochastic simulations of cells with different initial p21 levels as shown in E (n = 30). prolif, proliferating; quies, quiescent.::>

<a id='d9b8ce84-8e95-49df-89d4-450167bbb7d6'></a>

protein is an essential component of a positive feedback system that creates the RP (Fig. 2B). An inherent property of positive feedback is its ability to create discontinuous switches (26), and a bistable Rb–E2F switch has been reported to underlie the RP (27). Our model supports this notion, showing bistability in E2F activity in the absence of p21, with low concentrations of growth factors attracting cells to the quiescent state (Fig. 2C). Once a certain threshold of mitogens is reached, Rb is hyperphosphorylated and E2F is rapidly activated, facilitating progression through the RP. Note that this transition is irreversible in the absence of DNA damage such that cells become independent of growth factor stim-ulation once in the proliferating state, a hallmark of the RP (28).

<a id='fa37e121-cb5d-4e5c-b402-9dd4c0e713ee'></a>

Extending on the previously known bistability of the RP, our model suggests that p21 can modulate the Rb-E2F switch such that cells can enter quiescence even under high growth factor stimula- tion if they contain increased p21 levels (Fig. 2D). This mechanism primarily depends on p21's ability to inhibit Cdk2 activity and thereby prevent activation of the positive feedback loops that are required to pass the RP (SI Appendix, Fig. S2A). Due to bistability, cells on either side of the p21 threshold exhibit very different fates. While cells with subthreshold p21 levels continue to cycle, their suprathreshold counterparts enter quiescence (Fig. 2E). This di- viding behavior is even more apparent when considering Cdk2 activity (Fig. 2F). Both populations show an initial decrease in Cdk2 activity at the end of mitosis as CycA is degraded by the APC/CCdc20. However, Cdk2 activity rapidly recovers in cells that contain low p21 levels, while high p21 levels prevent this recovery, in excellent agreement with live-cell imaging (14, 16). The stark contrast between both populations and the fact the intermediate states are rarely observed provide further evidence that bistability is indeed at the core of the proliferation-quiescence decision.

<a id='a7ce4584-afa9-4ec2-8052-82f305e005b8'></a>

In summary, our model suggests that p21 interferes with a bistable switch that controls RP passage to convert a graded

<a id='7bde63c6-a4fe-46da-9c4e-9e2978270e57'></a>

p21 signal, which can be inherited from the mother cell (_SI_ Appendix, Fig. S2 _B_ and _C_), into an all-or-nothing cell fate decision. It also shows that mitogen stimulation is necessary, but not sufficient, for proliferation.

<a id='54443640-3255-4536-a61e-ddde26440716'></a>

p21 Degradation Controls Whether the Proliferation Decision Can Be
Reversed. In addition to mitogen stimulation and past DNA dam-
age that control whether a cell enters the cell cycle in the first
place, it has been shown that the decision to proliferate can be
reversed by exposure to stress and DNA damage in the G1 phase
(18). One mechanism that may mediate this response is an in-
creased expression of p21, which inhibits cyclin:Cdk2 activity and
DNA synthesis (Fig. 3A). Indeed, our simulations show that DNA
damage incurred during the G1 phase can reverse Cdk2 activation,
pushing cells back into a pre-RP state with low Cdk2 activity and
unphosphorylated Rb (SI Appendix, Fig. S3A). However, whether
the decision to proliferate is reversible depends on both the
strength of DNA damage and its timing (Fig. 3B). Specifically, our
model predicts that cells in early G1 phase are particularly sus-
ceptible to arrest, with low levels of DNA damage being sufficient
to reset the cell cycle. As cells move toward S phase, they pro-
gressively lose this sensitivity such that more, or more sustained,
DNA damage is required to revert to quiescence. Intriguingly, our
simulations suggest that S-phase cells completely lose the ability to
enter p21-induced quiescence in response to the low levels of in-
trinsic DNA damage we consider here.

<a id='3d2a831b-9283-46a1-8f14-df189dc28bd0'></a>

<::figure: Fig. 3. p21 degradation controls the ability to enter DNA damage-induced quiescence. (A) Subnetwork of DNA damage-induced control of early cell-cycle progression including Skp2- and Cdt2-dependent p21 degradation pathways. The diagram shows 'Damage' impacting 'p21'. 'Skp2' and 'Cdt2' both lead to the degradation of 'p21'. 'p21' inhibits 'CycE Cdk2' and 'CycA Cdk2'. 'CycE Cdk2' and 'CycA Cdk2' promote 'aRC'. 'aRC' inhibits 'p21'. (B) Effect of DNA damage of variable strength and timing on the decision to proliferate (Bottom) in deterministic simulations of the full model in Fig. 1A. Damage was present from the indicated time until the end of the simulation. Time course of an undamaged cell is shown for comparison (Top). The top plot, labeled 'unperturbed', shows relative levels (AU) over time after cytokinesis (h). Lines represent 'act. Cdh1' (black), 'p21' (green), 'act. Cdk2' (light blue), and 'aRC' (brown), with an area shaded 'S-phase'. The bottom plot shows damage (AU) on the y-axis (0-3) versus time of damage (h) on the x-axis (0-12). The plot is divided into 'quiescent' (brown area) and 'proliferating' (light blue area) regions. (C, E, and G) Experimental data showing the percentage of control-siRNA (C; n = 55, 77), Skp2-depleted (E; n = 71, 107), and Cdt2-depleted (G; n = 32, 52) cells that enter S phase or arrest after treatment with DMSO or CPT at the indicated time postmitosis. These panels consist of bar charts showing '% of cells' on the y-axis (0-100) and 'time in G1 before drug addition (h)' on the x-axis (0-5). Each panel has two sub-panels: one for 'DMSO' treatment and one for 'CPT' treatment. Bars are colored for 'S-phase' (light blue) and 'arrest' (brown). (D and F) Same as in the Bottom of B for Skp2-depleted (D) and Cdt2-depleted (F) cells. These plots are similar to the bottom plot of panel B, showing damage (AU) versus time of damage (h), with regions for 'quiescent' (brown) and 'proliferating' (light blue). Panel D is labeled 'Skp2 depleted' and Panel F is labeled 'Cdt2 depleted'. act, active; rel, relative.::>

<a id='ca296ee0-aec0-4691-ab7e-49589e02aeb0'></a>

2534

<a id='e357dea7-fb3c-48cc-baa6-8ac071507792'></a>

www.pnas.org/cgi/doi/10.1073/pnas.1715345115

<a id='3379097e-8c27-4adc-a46c-b1b17eec149d'></a>

Heldt et al.

<!-- PAGE BREAK -->

<a id='4aa1115f-cf56-450f-9c23-3c0f8c58a359'></a>

To test these model predictions, we introduced DNA damage into asynchronously cycling hTert-RPE1 cells with endogenously labeled mRuby-PCNA and p21-GFP and followed their cell-cycle fates and p21-GFP levels by time-lapse imaging. We imaged cells for 5 h to determine when they exited mitosis, before treating them with the DNA damage-inducing drug Camptothecin (CPT). We then tracked cells for a further 20 h to see whether they would enter S phase or arrest. Control cells that were treated with DMSO almost exclusively entered S phase, showing no bias for the length of time spent in G1 before treatment (Fig. 3C and SI Appendix, Fig. S3B). In sharp contrast, CPT-treated cells became increasingly less likely to enter quiescence the more time they had spent in G1. This is consistent with our model prediction that cells become less sensitive to DNA damage as they progress toward S phase. Note that while we see an all-or-none response on the single-cell level—that is, a cell either enters quiescence or fully commits to the cell cycle—experimental results compiled from multiple cells show a fractional response due to cell-to-cell variability.

<a id='15ce7d74-5761-4a06-b0a7-eb768be8b39a'></a>

Our model specifically predicts that cells lose the ability to enter quiescence because of an increasing rate of p21 degradation. Two ubiquitin ligases can mediate p21 degradation: SCFSkp2 and CRL4Cdt2 (Fig. 3A) (22). We recently showed that it is Skp2 that controls the turnover of p21 in G1 (16). Simulating our model in the absence of Skp2 suggests that this perturbation would cause cells to remain highly sensitive to DNA damage until late G1 (Fig. 3D). To test this prediction, we depleted Skp2 using siRNA and repeated the above experiment. Consistent with our model, only those Skp2-depleted cells that were most advanced in G1 before CPT addition avoided quiescence (Fig. 3E). Furthermore, we find that while increasingly higher CPT doses are required to trigger quiescence in control cells as they advance in G1 (SI Appendix, Fig. S3C), Skp2 depletion leads to an abrupt, less drug dose-dependent transition (SI Appendix, Fig. S3D), as suggested by our model.

<a id='a1a5fb82-6287-4aba-ac6c-319781ad66f7'></a>

A further model prediction is that cells become insensitive to p21-induced quiescence during S phase because of strong Cdt2-mediated p21 degradation. More precisely, our simulations suggest that Cdt2 depletion would weaken the G1/S bistable switch (SI Appendix, Fig. S1D). This would allow p21 to reaccumulate during S phase (SI Appendix, Fig. S3E), such that now even S-phase cells become susceptible to DNA damage-induced quiescence (Fig. 3F). However, susceptibility of Cdt2-depleted cells to quiescence in early and mid-G1 would be unaffected. To test this, we depleted Cdt2 in hTert-RPE1 cells. Indeed, we observed that when these cells were treated with CPT in early and mid-G1, they were still able to enter S phase (Fig. 3G). However, these cells only spend a short amount of time in S phase, and more importantly, they reaccumulate p21 during DNA replication (SI Appendix, Fig. S3 F and G), indicative of a reversion to quiescence.
Taken together, these data confirm our model predictions that Skp2-dependent p21 degradation leads to a progressive loss of sensitivity to DNA damage-induced quiescence in G1, which culminates in the Cdt2-mediated tolerance of DNA damage during S phase.

<a id='f58269cb-964c-4449-a51f-bf5de421b34d'></a>

**Loss of p21 and Rb Causes Uncontrolled Proliferation.** The results above indicate that the Rb-p21 control network integrates signals from mitogen stimulation and DNA damage to mediate the proliferation-quiescence decision. Considering that many cancer cells have lost the ability to properly respond to these stimuli (29, 30), we used our model to explore which changes in the molecular network would compromise decision-making. With intact control, mitogen stimulation is necessary for proliferation such that cells below a certain threshold remain quiescent (Fig. 4A). Once this threshold is exceeded, the ratio between growth factor signaling and DNA damage—that is, between the stimulation of Cdk2 activity by E2F-mediated cyclin synthesis and its inhibition by p21—controls proliferation. The molecular network integrates

<a id='5fbfcbcd-8094-461d-a7aa-65ea6409698a'></a>

<::chart: The figure displays four 2D plots (A, B, C, D) illustrating the simulated effect of growth factors and DNA damage on cell proliferation (blue) and quiescence (red) decisions under different conditions. Each plot has 'growth factors (AU)' on the x-axis (from 0 to 1) and 'damage (AU)' on the y-axis (from 0 to 4). The legend indicates 'quiescent' for red areas and 'proliferating' for blue areas. Fig. 4. Protein loss leads to deregulated proliferation. (A–D) Simulated effect of the presence of growth factors and DNA damage on the proliferation (blue)–quiescence (red) decision in unperturbed cells (A) and cells depleted for Rb (B), p21 (C), and Cdh1 (D). The indicated amount of damage and growth factors was present from the start of the simulation. (A) Unperturbed cells: The plot is predominantly red (quiescent), with a small blue (proliferating) region appearing at high growth factors and very low damage. (B) Cells depleted for Rb (-Rb): A large blue (proliferating) region covers most of the plot, particularly at lower damage levels, with a red (quiescent) region appearing at higher damage levels. (C) Cells depleted for p21 (-p21): The plot shows a clear vertical division. The left side (low growth factors) is red (quiescent), while the right side (high growth factors) is blue (proliferating), with the transition occurring around growth factors = 0.4. (D) Cells depleted for Cdh1 (-Cdh1): The plot shows a blue (proliferating) region at lower damage levels that tapers off as damage increases, while a red (quiescent) region occupies the upper part of the plot, increasing with damage across all growth factor levels.::>

<a id='f9b4bc14-817a-4fb9-9cae-c2815e56c87c'></a>

both stimuli, and high amounts of damage or reduced mitogen
levels will promote quiescence. Due to the presence of a bistable
switch, these continuous inputs are converted into a discontinuous,
all-or-nothing cell fate decision, resulting in a sharp boundary
between fates.

<a id='d02c946e-0ff1-4f84-be12-eec2cf2f9ed7'></a>

According to our model, a missing or nonfunctional Rb protein removes the necessity for mitogen stimulation, with cells pro- liferating in the absence of growth factors (Fig. 4B), as has been found experimentally (31, 32). However, the system retains its ability to respond to DNA damage, albeit at much reduced sensi- tivity—that is, the transition to a quiescent regime occurs at higher DNA damage levels. The latter is due to uninhibited E2F pro- moting substantial cyclin synthesis and Cdk2 activity, which re- quires a higher level of p21 induction to overcome. Loss of p21 protein has the opposite effect, abolishing DNA damage-induced quiescence, with the control by mitogens remaining in place (Fig. 4C). Finally, removal of Cdh1, another negative regulator of Cdk2 activity, makes cells less prone to enter quiescence in general. This is due to the increased accumulation of CycA:Cdk2 in the G1 phase that provides another source of kinase activity that can promote RP passage (Fig. 4D). However, the Cdh1-depleted sys- tem still responds to both mitogen stimulation and DNA damage.

<a id='05596164-a60a-409c-9c4a-bacb9fab67f1'></a>

We decided to test the predictive value of our model by mea-
suring the response of p21-proficient versus p21-knockout (p21KO,
ref. 16) cells to a range of concentrations of growth factors and
DNA damage. Consistent with our model prediction, we find that
p21KO cells proliferate much more readily (_SI Appendix, Fig. S4_).
Quiescence is only triggered at very high drug doses, most likely by
DNA damage-sensing signaling pathways that can cause cell cycle
arrest under high levels of exogenous DNA damage, which we did
not consider in the model presented here of the cellular response
to relatively lower levels of endogenous DNA damage.

<a id='ee16859f-19cb-4964-aed5-0c0e6022fe9f'></a>

In summary, our model suggests that the molecular network
that controls the proliferation-quiescence decision integrates
growth factor signaling and DNA damage into an all-or-nothing
cell fate decision. Loss of Rb and p21 compromises the ability to
enter quiescence in response to loss of mitogens and DNA
damage, respectively, while Cdh1-depleted cells are more likely
to proliferate in general.

<a id='69a6d76f-b9d5-4ac7-b4cc-dc805053bbda'></a>

**Discussion**
In this study, we developed a unifying model for the proliferation-
quiescence decision in mammalian cells based on live single-cell
imaging experiments. We show that two bistable switches underpin

<a id='618a0f6d-9b92-4fc7-9f5d-f906240626c4'></a>

Heldt et al.

<a id='5eddfe94-c43b-40f4-999a-9ba08694bb0c'></a>

PNAS | March 6, 2018 | vol. 115 | no. 10 | 2535

<a id='1eea950e-0b93-4c48-bbe4-865729376e9a'></a>

<::logo: [PNAS] PNAS A dark blue, vertically oriented rectangular shape with white serif text "PNAS" stacked vertically within it.::>

<a id='dc4e43f6-6c3f-43c9-8529-14d78312a257'></a>

SYSTEMS BIOLOGY

<!-- PAGE BREAK -->

<a id='bb2b5cb7-04b7-474d-be2c-3001d28332c1'></a>

this decision: the RP, which mediates quiescence in response to
serum starvation and DNA damage, and the G1/S transition,
allowing cells to tolerate intrinsic DNA damage during S phase.
The interplay between these switches establishes a window of re-
versibility, where cells otherwise committed to proliferation can
revert to quiescence by expressing the Cdk inhibitor protein p21.

<a id='55815667-adb7-4db1-824f-3afcf935d560'></a>

The RP has long been recognized as a prototype example of a bistable commitment point in cell-cycle progression, converting a graded mitogen signal into an all-or-none decision to proliferate (27). Our model suggests that p21 expression interferes with this switch by interrupting a positive Cdk2-Rb-E2F feedback loop. This establishes a p21 threshold for RP passage. Above this threshold, p21 prevents E2F activation by blocking Rb hyperphosphorylation, while at subthreshold levels, Cdk2 can overcome p21 inhibition and phosphorylate Rb. Indeed, cells that exit mitosis with low p21 levels have been shown to maintain residual Cdk2 activity and Rb hyperphosphorylation, which facilitates their reentry into the cell cycle (14, 16). By contrast, intrinsic DNA damage incurred during S or G2 phases can increase p21 to suprathreshold levels, promoting quiescence in the subsequent cell cycle. We thus suggest that p21 connects the DNA damage response to the RP switch, where a continuous p21 signal is converted into an all-or-none cell-cycle response (Fig. 5A). Spontaneous DNA damage during unperturbed growth can thus lead to a quiescent subpopulation of cells characterized by low Cdk2 activity and high p21 levels. However, this quiescent subpopulation is absent in cell lines that have lost Rb or p53 function (23), as is the case in many cancers (29, 30).

<a id='d2096c21-ba9d-4b4b-989d-53ea2ff5b794'></a>

When first proposed, the RP was described as a transition that renders cell-cycle progression independent of growth-factor stimulation (33, 34). In our model, the RP is indeed an irreversible switch that can maintain the proliferative state in the absence of mitogens. However, for the transition to occur in the first place, a certain mitogen threshold has to be exceeded such that Rb can become hyperphosphorylated and E2F activated. We show that this threshold is controlled by p21 levels. However, growth factors remain a necessary condition for cell-cycle entry even in the complete absence of p21. Consistent with this, p21-knockout cells enter quiescence under serum starvation conditions (15, 16). Our model also suggests that once a critical serum level is reached, the decision to proliferate depends on the ratio of mitogen stimulation and DNA damage, in agreement with experimental results showing that competition between p21 and mitogen-regulated cyclin D1:Cdk4 controls cell-cycle entry (35). The RP, hence, serves as a hub that integrates growth signals, which promote cyclin:Cdk2 activity, and DNA damage, which counteracts Cdk2 through p21 expression. In support of this, increasing serum concentrations drive more cells into the proliferating state, while DNA damage and high p21 levels cause quiescence (14–16).

<a id='9181975d-3579-46bc-9bf4-4b81be0078de'></a>

Previous studies have argued in favor of a singular decision
point or window for cell-cycle entry either located at the end of

<a id='43dfc181-72ab-473e-bc9d-08dfd24ec55d'></a>

mitosis, in mid-G1, or at the G1/S transition (14, 18, 33). Our simulations suggest that the interaction between the RP switch and the G1/S transition creates a decision window that extends at least throughout the entirety of G1 phase, where it integrates signals from mitogen-related pathways and DNA damage. During this window, cells that are committed to proliferation based on growth factor stimulation may revert to quiescence through DNA damage-induced p21 expression (Fig. 5B). Once cells do enter S phase, strong p21 degradation by Cdt2 prevents p21 reexpression, insulating S phase from mild, intrinsic DNA damage (Fig. 5C). This provides a mechanistic explanation for recent data showing that, in contrast to G1 and G2, S phase is comparatively insensitive to DNA damage (36). We speculate that this insensitivity is important to prevent cells from entering growth arrest with partly replicated DNA, from which they could later reemerge, starting a second round of replication.

<a id='2369a289-ae6e-4edf-b64c-56e18961bd1a'></a>

A recent study proposed that APC/C<sup>Cdh1</sup> inactivation consti-
tutes a point of no return for cell-cycle entry, preventing cells from
entering quiescence in response to exogenous stress (18). How-
ever, Cdh1 inactivation temporally overlaps with the G1/S tran-
sition and thus with the onset of Cdt2-mediated p21 degradation.
Moreover, by facilitating CycA:Cdk2 accumulation, the in-
activation of Cdh1 not only promotes the G1/S transition but also
strengthens p21 degradation via the Skp2-dependent pathway.
Hence, Cdh1 regulation and p21 control are intimately linked.
Nevertheless, our data suggest that it is p21 degradation that ul-
timately mediates the tolerance of intrinsic DNA damage. Two
observations support this notion. First, compromising p21 degra-
dation by Cdt2 depletion allows p21 reaccumulation during S
phase and premature S-phase exit despite Cdh1 control remaining
in place. Second, Emil-depleted cells that are treated with a Cdk
inhibitor around the time of Cdh1 inactivation—that is, at S-phase
entry—show an immediate reactivation of Cdh1 (18). However,
when the same experiment is conducted in the absence of Cdk
inhibition but presence of a DNA-damaging drug, Cdh1 reac-
tivation occurs only after a delay of several hours (18). We pro-
pose that, in this experiment, Cdh1 reactivation is caused by DNA
damage-induced p21 inhibiting Cdk activity and that the observed
delay results from S phase preventing p21 accumulation (*SI Ap-
pendix, Fig. S3 H and I*). Thus, p21 degradation protects S-phase
progression even when Cdh1 control is compromised.

<a id='1586e9c3-dfc4-43b6-85ae-30604817e973'></a>

Taken together, we show that bistable transitions serve two different purposes during cell-cycle entry. The RP switch integrates growth and damage signals, translating them into an all-or-none decision to proliferate, while the G1/S transition temporarily insulates cell-cycle progression from the p21-mediated DNA damage response during S phase. Hence, these ubiquitous control motifs can provide both sensitivity and robustness to external stimuli.

<a id='02f2f2e3-18f4-4696-b375-f1c9f619ba8c'></a>

<::diagram: Fig. 5. Regulation of the proliferation-quiescence decision. The RP establishes a bistable switch with two distinct cell fates: quiescence and proliferation. (A) p21 carried over from the previous cycle can drive cells into quiescence by tipping the balance toward low Cdk2 activity, counteracting growth factor-mediated passage through the RP. The diagram for (A) is titled "Late mitosis and early G1-phase". It shows a seesaw pivoted at "RP". The left side, representing Cdk2, is labeled "low high" and shows a low Cdk2 level. A spring labeled "GF" is pushing up the left side. The right side, representing p21, is labeled "low high" and shows a high p21 level. A significant amount of green liquid (p21) has accumulated on the left side of the seesaw, causing it to tilt heavily towards the left, indicating a state of "quiescence" (brown box) over "proliferation" (blue box). (B) If initial p21 levels are low, growth factors can induce the reaccumulation of cyclin:Cdk2. However, DNA damage incurred during G1 phase may reverse the decision to proliferate by promoting p21 accumulation and Cdk2 inhibition. The diagram for (B) is titled "G1-phase". The seesaw is pivoted at "RP". The left side, representing Cdk2, is labeled "low high" and shows a higher Cdk2 level than in (A). A spring labeled "GF" pushes up the left side. The right side, representing p21, is labeled "low high" and shows a low p21 level. A dropper labeled "Damage" is shown adding green liquid (p21) onto the left side of the seesaw, which is beginning to accumulate and tilt the seesaw towards "quiescence" (brown box) over "proliferation" (blue box). (C) In S phase, cells are insensitive to p21-induced quiescence as the Cdk inhibitor can no longer accumulate due to strong degradation. The diagram for (C) is titled "S-phase". The seesaw is pivoted at "RP". The left side, representing Cdk2, is labeled "low high" and shows a high Cdk2 level. The right side, representing p21, is labeled "low high" and shows a very low p21 level (only a small drop). A dropper labeled "Damage" is adding green liquid (p21) onto the seesaw, but the seesaw is tilted steeply towards the right, causing the liquid to flow off the right end, preventing accumulation. This indicates a state of "proliferation" (blue box) over "quiescence" (brown box).::>

<a id='e5c749d2-2702-45a6-98f8-19514fc94f53'></a>

2536

<a id='34f30888-3808-4d75-abac-a6bd4226eab9'></a>

www.pnas.org/cgi/doi/10.1073/pnas.1715345115

<a id='e28236dc-23da-49c0-83cd-ca210eed3178'></a>

Heldt et al.

<!-- PAGE BREAK -->

<a id='14f5656a-6a85-499e-8537-e20f911e469c'></a>

**Methods**

**Live Cell Imaging.** Both alleles of the endogenous CDKN1A locus were labeled at the C terminus with GFP in hTert-RPE1 cells, generating a cell line where all p21 protein was labeled with GFP (16). In the same cells, a single allele of PCNA was labeled at the N terminus with mRuby, to determine the timing of the G1/S transition, S-phase exit, and mitosis (37). To follow p21-GFP dynamics across the cell cycle, asynchronously cycling cultures growing in phenol red-free DMEM plus 10% FBS were imaged every 10 min on the Opera HCS microscope, using a 20x objective (N.A. 0.45) for up to 72 h. Automated image analysis was used to extract p21-GFP levels over time, relative to cell-cycle transitions (38).

<a id='70fc47cd-565f-4887-9bef-983295d47830'></a>

To test the sensitivity of G1 cells to DNA damage, cells were reverse-transfected with either control, Skp2-, or Cdt2-targeting siRNAs (Dharmacon ONTTargetPlus siRNA pools) 24 h before time-lapse imaging, using Lipofectamine RNAiMax (Invitrogen), according to the manufacturer's instructions. Efficient depletion of Skp2 and Cdt2 protein levels by these siRNAs has been previously evaluated in this cell line (see ref. 16). Cells were filmed for 5 h before the addition of CPT or DMSO, and filming was continued for 20 h postdrug addition. mRuby-PCNA expression in these cells was used to determine the time of mitotic exit and the time of S-phase entry. A cell was classified as quiescent if it spent more than 600 min in G1, which we previously showed is consistent with a lack of both Rb hyperphosphorylation and Cdk2 activity (16).

<a id='3c169e3b-2aeb-4d69-add0-eae56fe82022'></a>

Analysis of Proliferation-Quiescence Decisions in Response to p21 Knockout.
hTert-RPE1 mRuby-PCNA p21-wild-type or hTert-RPE1 mRuby-PCNA
p21KO cells (16) were plated in a 384-well CellCarrier plate at a density of
2,000 cells per well in DMEM with 10% FBS. Once cells had attached, cells
were washed three times in PBS and replaced with DMEM containing no FBS.
Cells were serum-starved in this way for 72 h. We then added a range of
concentrations of FBS and CPT in DMEM to cells and incubated for a further
24 h before fixing in 4% paraformaldehyde. Cells were permeabilized in PBS/

<a id='78846e0c-fe71-4513-9641-2e9e92cd2750'></a>

1. Yao G (2014) Modelling mammalian cellular quiescence. Interface Focus 4:20130074.
2. Murray AW (2004) Recycling the cell cycle: Cyclins revisited. Cell 116:221-234.
3. Hochegger H, Takeda S, Hunt T (2008) Cyclin-dependent kinases and cell-cycle transitions: Does one fit all? Nat Rev Mol Cell Biol 9:910-916.
4. Bertoli C, Skotheim JM, de Bruin RAM (2013) Control of cell cycle transcription during G1 and S phases. Nat Rev Mol Cell Biol 14:518-528.
5. el-Deiry WS, et al. (1993) WAF1, a potential mediator of p53 tumor suppression. Cell 75:817-825.
6. Abbas T, Dutta A (2009) p21 in cancer: Intricate networks and multiple activities. Nat Rev Cancer 9:400-414.
7. Moldovan GL, Pfander B, Jentsch S (2007) PCNA, the maestro of the replication fork. Cell 129:665-679.
8. Waga S, Hannon GJ, Beach D, Stillman B (1994) The p21 inhibitor of cyclin-dependent kinases controls DNA replication by interaction with PCNA. Nature 369:574-578.
9. Bruning JB, Shamoo Y (2004) Structural and thermodynamic analysis of human PCNA with peptides derived from DNA polymerase-delta p66 subunit and flap endonuclease-1. Structure 12:2209-2219.
10. Cayrol C, Knibiehler M, Ducommun B (1998) p21 binding to PCNA causes G1 and G2 cell cycle arrest in p53-deficient cells. Oncogene 16:311-320.
11. Martín-Caballero J, Flores JM, García-Palencia P, Serrano M (2001) Tumor susceptibility of p21(Waf1/Cip1)-deficient mice. Cancer Res 61:6234-6238.
12. Cheng T, et al. (2000) Hematopoietic stem cell quiescence maintained by p21cip1/waf1. Science 287:1804-1808.
13. Kippin TE, Martens DJ, van der Kooy D (2005) p21 loss compromises the relative quiescence of forebrain stem cell proliferation leading to exhaustion of their proliferation capacity. Genes Dev 19:756-767.
14. Spencer SL, et al. (2013) The proliferation-quiescence decision is controlled by a bifurcation in CDK2 activity at mitotic exit. Cell 155:369-383.
15. Overton KW, Spencer SL, Noderer WL, Meyer T, Wang CL (2014) Basal p21 controls population heterogeneity in cycling and quiescent cell cycle states. Proc Natl Acad Sci USA 111:E4386-E4393.
16. Barr AR, et al. (2017) DNA damage during S-phase mediates the proliferation-quiescence decision in the subsequent G1 via p21 expression. Nat Commun 8:14728.
17. Arora M, Moser J, Phadke H, Basha AA, Spencer SL (2017) Endogenous replication stress in mother cells leads to quiescence of daughter cells. Cell Rep 19:1351-1364.
18. Cappell SD, Chung M, Jaimovich A, Spencer SL, Meyer T (2016) Irreversible APC(Cdh1) inactivation underlies the point of no return for cell-cycle entry. Cell 166:167-180.
19. Frolov MV, Dyson NJ (2004) Molecular mechanisms of E2F-dependent activation and pRB-mediated repression. J Cell Sci 117:2173-2181.
20. Bracken AP, Ciro M, Cocito A, Helin K (2004) E2F target genes: Unraveling the biology. Trends Biochem Sci 29:409-417.
21. Massagué J (2004) G1 cell-cycle control and cancer. Nature 432:298-306.
22. Starostina NG, Kipreos ET (2012) Multiple degradation pathways regulate versatile CIP/KIP CDK inhibitors. Trends Cell Biol 22:33-41.

<a id='3b42d032-2844-41e5-a69d-59963666df5b'></a>

0.2% TritonX-100, blocked in 2% BSA/PBS, and immunostained with phos-pho-807/811 Rb antibody (CST 9308) to differentiate between quiescent and proliferating cells. Phospho-Rb antibody was detected by goat anti-rabbit Alexa 647 secondary antibody (ThermoFisher), and Hoescht was used to la-bel nuclei. Plates were imaged on an Opera HCS (PerkinElmer) using a 20x objective, N.A. 0.45. Automated image analysis was performed using Columbus to determine the percentage of quiescent cells per condition. Briefly, nuclei were segmented using the Hoescht stain, and mitotic, dead, and poorly segmented cells were excluded, using intensity and morphology thresholds. The phospho-Rb intensity was quantified for each nucleus, and by calculating a threshold for proliferating cells, we could extract the per-centage of quiescent cells per condition.

<a id='2020aa4a-9c83-44dd-8302-5afa4f0f64e8'></a>

Mathematical Modeling. Our model of cell-cycle progression (Fig. 1A) comprises a set of ordinary differential equations (see SI Appendix for details), which provide the basis for deterministic and stochastic simulations shown in the main text. A deterministic version of the model was prepared using the Systems Biology Toolbox 2 (39) for MatLab (version 9.1.0 R2016b) and simulated with the CVODE routine (40). Bifurcation diagrams were calculated using the freely available software XPP-Aut (41). We simulated a stochastic version of the model using custom-made MatLab code of the stochastic simulation algorithm, also known as Gillespie's algorithm (reviewed in ref. 42), according to the sorting direct method (43). The model is provided as Dataset S1, and different versions of it are available at www.cellcycle.org.uk/publication. The model has also been deposited in BioModels (44) and assigned the identifier MODEL1703030000.

<a id='f976a200-b0b4-421f-b36c-8752206d6c79'></a>

ACKNOWLEDGMENTS. We thank John J. Tyson and Scott Rata for critical reading of the manuscript and helpful discussions. The groups of C.B. and B.N. are funded by the Biotechnology and Biological Sciences Research Council Strategic LoLa Grant BB/M00354X/1.

<a id='3fba21ba-3008-497d-963e-64007e1f8e60'></a>

23. Barr AR, Heldt FS, Zhang T, Bakal C, Novák B (2016) A dynamical framework for the all-or-none G1/S transition. Cell Syst 2:27–37.
24. Dulić V, Stein GH, Far DF, Reed SI (1998) Nuclear accumulation of p21Cip1 at the onset of mitosis: A role at the G2/M-phase transition. Mol Cell Biol 18:546–557.
25. Bartek J, Lukas C, Lukas J (2004) Checking on DNA damage in S phase. Nat Rev Mol Cell Biol 5:792–804.
26. Tyson JJ, Chen KC, Novak B (2003) Sniffers, buzzers, toggles and blinkers: Dynamics of regulatory and signaling pathways in the cell. Curr Opin Cell Biol 15:221–231.
27. Yao G, Lee TJ, Mori S, Nevins JR, You L (2008) A bistable Rb–E2F switch underlies the restriction point. Nat Cell Biol 10:476–482.
28. Zetterberg A, Larsson O, Wiman KG (1995) What is the restriction point? Curr Opin Cell Biol 7:835–842.
29. Sherr CJ (1996) Cancer cell cycles. Science 274:1672–1677.
30. Malumbres M, Barbacid M (2001) To cycle or not to cycle: A critical decision in cancer. Nat Rev Cancer 1:222–231.
31. Dannenberg J-H, van Rossum A, Schuijff L, te Riele H (2000) Ablation of the retino-blastoma gene family deregulates G(1) control causing immortalization and increased cell turnover under growth-restricting conditions. Genes Dev 14:3051–3064.
32. Sage J, et al. (2000) Targeted disruption of the three Rb-related genes leads to loss of G(1) control and immortalization. Genes Dev 14:3037–3050.
33. Pardee AB (1974) A restriction point for control of normal animal cell proliferation. Proc Natl Acad Sci USA 71:1286–1290.
34. Zetterberg A, Larsson O (1985) Kinetic analysis of regulatory events in G1 leading to proliferation or quiescence of Swiss 3T3 cells. Proc Natl Acad Sci USA 82:5365–5369.
35. Yang HW, Chung M, Kudo T, Meyer T (2017) Competing memories of mitogen and p53 signalling control cell-cycle entry. Nature 549:404–408.
36. Chao HX, et al. (2017) Orchestration of DNA damage checkpoint dynamics across the human cell cycle. Cell Syst 5:445–459.e5.
37. Zerjatke T, et al. (2017) Quantitative cell cycle analysis based on an endogenous all-in-one reporter for cell tracking and classification. Cell Rep 19:1953–1966.
38. Cooper S, Barr AR, Glen R, Bakal C (2017) NucliTrack: An integrated nuclei tracking application. Bioinformatics 33:3320–3322.
39. Schmidt H, Jirstrand M (2006) Systems biology toolbox for MATLAB: A computational platform for research in systems biology. Bioinformatics 22:514–515.
40. Cohen S, Hindmarsh AC (1996) CVODE, a stiff/nonstiff ODE solver in C. Comput Phys 10:138–143.
41. Ermentrout B (2002) Simulating, Analyzing, and Animating Dynamical Systems (Society for Industrial and Applied Mathematics, Philadelphia).
42. Gillespie DT (2007) Stochastic simulation of chemical kinetics. Annu Rev Phys Chem 58: 35–55.
43. McCollum JM, Peterson GD, Cox CD, Simpson ML, Samatova NF (2006) The sorting direct method for stochastic simulation of biochemical systems with varying reaction execution behavior. Comput Biol Chem 30:39–49.
44. Chelliah V, et al. (2015) BioModels: Ten-year anniversary. Nucleic Acids Res 43: D542–D548.

<a id='293e67ac-89ac-4635-a9c8-007d3883f66c'></a>

Heldt et al.

<a id='0a935e5d-bcdb-4b3f-ae16-4f158bd316cb'></a>

PNAS | March 6, 2018 | vol. 115 | no. 10 | 2537

<a id='d6c8ca4e-e9d1-4d46-9073-34d28de63d95'></a>

<::logo: PNAS
PNAS
This logo features the acronym "PNAS" in a dark blue, serif font, oriented vertically.::>

<a id='cabc99be-2d3a-4d9a-92d7-bb0f1a890654'></a>

SYSTEMS BIOLOGY
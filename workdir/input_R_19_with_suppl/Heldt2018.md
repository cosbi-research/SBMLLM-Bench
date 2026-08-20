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

# Supplementary materials

<a id='9e0a19c9-eebe-4ade-9ec0-66cec5cde257'></a>

# Supporting Information

A comprehensive model for the proliferation-quiescence decision in response to endogenous DNA damage in human cells

Frank S. Heldt, Alexis R. Barr, Sam Cooper, Chris Bakal, Béla Novák

<a id='fb86f918-40ab-4584-adb2-8622fc27c628'></a>

<table id="0-1">
<tr><td id="0-2" colspan="2">Contents</td></tr>
<tr><td id="0-3">Supporting figures ....................</td><td id="0-4">.2</td></tr>
<tr><td id="0-5">Mathematical modelling....................................</td><td id="0-6">.6</td></tr>
<tr><td id="0-7">Restriction point .....................................................................................................</td><td id="0-8">.6</td></tr>
<tr><td id="0-9">Synthesis and degradation of cyclins and Emi1.....................................................</td><td id="0-a">.6</td></tr>
<tr><td id="0-b">Inactivation of APC/C Cdh1</td><td id="0-c">.7</td></tr>
<tr><td id="0-d">p21 dynamics and Cdk2 inhibition</td><td id="0-e">.7</td></tr>
<tr><td id="0-f">Activation of DNA replication</td><td id="0-g">.8</td></tr>
<tr><td id="0-h">PCNA dynamics</td><td id="0-i">.9</td></tr>
<tr><td id="0-j">DNA damage and repair</td><td id="0-k">.9</td></tr>
<tr><td id="0-l">Cdh1 activity reporter.........................................................................................................</td><td id="0-m">9</td></tr>
<tr><td id="0-n">Computation .............................................................</td><td id="0-o">10</td></tr>
<tr><td id="0-p">Model parameters...................................................................................................</td><td id="0-q">10</td></tr>
<tr><td id="0-r">Supporting tables.................................................................................................</td><td id="0-s">12</td></tr>
<tr><td id="0-t">Supporting references...........................................................................................</td><td id="0-u">14</td></tr>
</table>

<a id='63174f6c-b024-4835-936c-9754bb67fffc'></a>

1

<!-- PAGE BREAK -->

<a id='3ff77f10-a3da-4db6-b7a2-f1fd6e3ba6c4'></a>

Supporting figures

A
<::diagram
: A diagram illustrating molecular interactions. "Damage" is shown impacting "p21". "p21" interacts with "Skp2" and "aRC". "Skp2" is also connected to "CycE Cdk2" and "CycA Cdk2". "CycE Cdk2" interacts with "Cdt2" and "aRC".
::>

B
G1/S transition S/G2 transition
<::chart
: Two bifurcation diagrams. The left chart, titled "G1/S transition", plots p21 (AU) against cyclin:Cdk2 level (AU). It shows multiple green curves, some solid and some dotted, with an upward arrow indicating "increasing damage" and a downward arrow pointing to a region labeled "G1/S". The right chart, titled "S/G2 transition", plots p21 (AU) against aRC (AU). It also shows multiple green curves, some solid and some dotted.
::>

C
<::chart
: Three stacked line charts over time from cytokinesis (h) from 0 to 20. A shaded region from approximately 6 to 14 hours is labeled "S-phase" across all three charts.
Top chart: Plots relative level (AU) from 0 to 1.5. Shows lines for "p21" (green), "CycA" (purple), "aRC" (brown), and "CycE" (light blue).
Middle chart: Plots degradation rate (1/min) from 0 to 0.04. Shows a line for "Skp2-dependent" degradation.
Bottom chart: Plots degradation rate (1/min) from 0 to 0.4. Shows a line for "Cdt2-dependent" degradation.
::>

D
<::chart
: A line chart plotting p21 level (AU) from 0 to 2 against cyclin:Cdk2 level (AU) from 0 to 2. It shows three distinct lines: "unperturbed" (green, solid then dotted), "-Skp2" (light blue, dotted), and "-Cdt2" (red, solid).
::> 

<a id='41bd93ff-c83b-47f4-9e35-7f1f46359087'></a>

Fig. S1. A bistable switch controls p21 levels (related to Fig. 1). (A) Subnetwork of p21 regulation comprising three mutual inhibition motifs that involve Skp2- and Cdt2-dependent degradation pathways. (B) Stable (solid) and unstable (dashed) steady states of p21 during S-phase entry (left) and exit (right), calculated from the model using the subnetwork in A. Each line represents a different level of constant DNA damage. The G1/S transition is indicated for intermediate damage levels. Note the difference in y-axis scales. (C) Dynamics of cell cycle regulators (top), Skp2-dependent p21 degradation (middle) and Cdt2-dependent p21 degradation (bottom) in deterministic simulations. p21 degradation via Skp2 is linked to CycE- and CycA-associated Cdk2 activity, while Cdt2-dependent degradation depends on active replication complexes (aRC). Note the differences in y-axis scales between middle and bottom panels. (D) G1/S transition for low levels of DNA damage in a control simulation (unperturbed) and in the absence of Skp2 (-Skp2) and Cdt2 (-Cdt2). Note that the -Cdt2 curve overlaps with the control simulation for low cyclin:Cdk2 levels.

<a id='4a544e06-dd5e-406c-bfc3-66ee8ae6afc0'></a>

2

<!-- PAGE BREAK -->

<a id='2fefac96-3b57-4af5-96b5-fd8ff4895224'></a>

<::chart: Fig. S2. p21 impairs RP passage (related to Fig. 2). The figure contains three subplots (A, B, C).

(A) A bifurcation diagram showing active E2F (AU) on the y-axis (0 to 1) versus growth factors (AU) on the x-axis (0 to 1). Multiple curves represent different levels of total p21. A dotted curve is labeled "p21 = 0". Other curves, some solid and some dotted, are labeled "1", "1.25", and "1.5". This plot is the same as in Fig. 2C except that total p21 was set to the indicated level.

(B) A time-series plot showing p21 (AU) on the y-axis (0 to 1.5) versus time from cytokinesis (h) on the x-axis (0 to 20). A shaded region labeled "S-phase" is present from approximately 6h to 12h. A black horizontal bar labeled "damage" is shown within the S-phase region. Multiple green curves, increasing from bottom to top, represent deterministic simulations of cells suffering increasing amounts of DNA damage during S-phase.

(C) A plot showing final p21 level (AU) on the y-axis (0 to 4) versus damage (AU) on the x-axis (0 to 2). A green curve with circular markers shows the final p21 level of cells from subplot (B) over the strength of DNA damage. A dashed horizontal line labeled "quiescence threshold" is present at approximately p21 level 1.5. This dashed line indicates the p21 level that would cause quiescence in daughter cells assuming that p21 protein is inherited but the damage repaired.::>

<a id='4169c401-ebfa-4865-a6b0-b0df27d54152'></a>

3

<!-- PAGE BREAK -->

<a id='17e5673f-3503-4acf-867f-2e1bf106bee3'></a>

<::chart: Fig. S3. p21 degradation controls reversibility of proliferation decision (related to Fig. 3). (A) Deterministic simulation of a cell that suffers DNA damage during G1-phase and enters quiescence (solid) using the full model in Fig. 1A. An undamaged cell is shown for comparison (dashed). The chart shows relative level (AU) on the y-axis and time from cytokinesis (h) on the x-axis. Two sets of lines are plotted: 'active Cdk2' (blue) and 'p21' (green). Solid lines represent a cell with damage, where 'damage' is indicated by a black horizontal bar from 2 to 4 hours. Dashed lines represent an undamaged cell. The 'active Cdk2' level starts around 0.5, increases to about 2.5 for the damaged cell and 1.5 for the undamaged cell, then decreases. The 'p21' level starts around 0.5, increases to about 1.5 for the damaged cell and stays low for the undamaged cell. (B) Percentage of unperturbed cells that enter S-phase or arrest after treatment with DMSO or CPT at the indicated time post-mitosis (n = 45, 59). Note that cells in this experiment were only imaged for 4 h prior to drug addition. The chart shows two bar graphs. The y-axis represents '% of cells' from 0 to 100. The x-axis represents 'time in G1 before drug addition (h)' from 0 to 4. The left graph is 'unper. + DMSO', showing that for all time points (0, 1, 2, 3, 4), the majority of cells (approx. 80-90%) enter 'S-phase' (light blue) and a small percentage (approx. 10-20%) 'arrest' (dark red). The right graph is 'unper. + CPT', showing that for time points 0, 1, 2, 3, 4, the majority of cells (approx. 80-90%) 'arrest' (dark red) and a small percentage (approx. 10-20%) enter 'S-phase' (light blue). (C, D) Percentage of control siRNA-treated (B; n = 292) and Skp2-depleted (C; n = 279) cells that enter S-phase (red to blue) in experiments after treatment with the indicated amount of CPT at the indicated time post-mitosis. Note that Fig. 3 and S3B show a different set of experiments, which were conducted at a single concentration of 1.25 µM CPT. (C) The heatmap is titled 'Ctrl'. The y-axis represents 'CPT level (µM)' with values 0, 0.3125, 0.625, 1.25, 2.5, 5. The x-axis represents 'time in G1 before drug addition (h)' from 0 to 5. The color bar ranges from 0 to 100. Dark red indicates a low percentage of S-phase cells, while light blue indicates a high percentage. For CPT level 0, all time points are light blue. For CPT levels 0.3125 to 5, the percentage of S-phase cells decreases (redder color) as CPT level increases and at earlier times in G1. (D) The heatmap is titled '-Skp2'. The y-axis represents 'CPT level (µM)' with values 0, 0.3125, 0.625, 1.25, 2.5, 5. The x-axis represents 'time in G1 before drug addition (h)' from 0 to 5. The color bar ranges from 0 to 100. The heatmap shows generally more light blue (higher S-phase entry) compared to (C), especially at higher CPT levels and earlier times in G1. (E) p21 levels from stochastic simulations of Cdt2-depleted cells in the absence of extrinsic DNA damage (n = 30). The line chart is titled 'Cdt2 depleted'. The y-axis represents 'p21 (AU)' from 0 to 2. The x-axis represents 'time from G1/S transition (h)' from -5 to 15. Multiple green lines represent individual cell simulations. A shaded pink region indicates 'S-phase' from approximately 0 to 5 hours. The p21 levels show fluctuating patterns, generally starting low and increasing, with some cells showing peaks during S-phase. (F, G) Experimental p21 levels in control-siRNA (F; n = 10) and Cdt2-depleted (G; n = 10) hTert-RPE1 cells that entered S-phase after being treated with CPT at the times indicated by black dots. (F) The line chart is titled 'Ctrl + CPT'. The y-axis represents 'p21 (AU)' (multiplied by 10^3) from 0 to 1.5. The x-axis represents 'time from G1/S transition (h)' from -5 to 15. Multiple green lines represent p21 levels. Black dots on the x-axis at 0 and 5 hours indicate CPT treatment times. p21 levels remain low. (G) The line chart is titled '-Cdt2 + CPT'. The y-axis represents 'p21 (AU)' (multiplied by 10^3) from 0 to 1.5. The x-axis represents 'time from G1/S transition (h)' from -5 to 15. Multiple green lines represent p21 levels. Black dots on the x-axis at 0 and 5 hours indicate CPT treatment times. p21 levels show a significant increase after CPT treatment. (H, I) Deterministic simulations of an unperturbed (H) and an Emi1-depleted (I) cell that suffer damage after S-phase entry. Note the re-activation of Cdh1 in G2-phase in response to DNA damage in the absence of Emi1. (H) The line chart is titled 'unperturbed'. The y-axis represents 'relative level' from 0 to 3. The x-axis represents 'time from cytokinesis (h)' from 0 to 25. A shaded pink region indicates 'S-phase' from approximately 5 to 13 hours. A black horizontal bar indicates 'damage' from approximately 13 to 15 hours. Two lines are plotted: 'active Cdh1' (black) and 'p21' (green). 'active Cdh1' starts high, drops during S-phase, and remains low. 'p21' remains low until damage, then increases. (I) The line chart is titled 'Emi1 depleted'. The y-axis represents 'relative level' from 0 to 3. The x-axis represents 'time from cytokinesis (h)' from 0 to 25. A shaded pink region indicates 'S-phase' from approximately 5 to 13 hours. A black horizontal bar indicates 'damage' from approximately 13 to 15 hours. Two lines are plotted: 'active Cdh1' (black) and 'p21' (green). 'active Cdh1' starts high, drops during S-phase, and re-activates (increases) after damage. 'p21' remains low until damage, then increases.::>

<a id='94e0648e-c3e3-4d1f-9882-2f4d2538d61e'></a>

4

<!-- PAGE BREAK -->

<a id='aee11da4-03b6-4536-b4b5-bc9ffe342c3b'></a>

<::chart: heatmap::>Fig. S4. Loss of p21 leads to deregulated proliferation (related to Fig. 4). (A, B) Percentage of wild-type (A; n = 41224) and p21-knockout (B; n = 133004) cells that enter S-phase (red to blue) in experiments after treatment with the indicated amount of CPT and growth factors (FBS) that were present from the beginning until the end of the experiment. Cells were serum-starved for 72 h before the experiment.The figure shows two heatmaps, A and B, with a common color scale.The color scale ranges from 0 (red) to 100 (blue), with 50 in the middle. The y-axis for both heatmaps is "CPT level (μM)" with values 0, 0.3125, 0.625, 1.25, 2.5, and 5. The x-axis for both heatmaps is "FBS level (%)" with values 0, 0.625, 1.25, 2.5, 5, and 10.A) Heatmap titled "wild type". The top rows (CPT levels 5, 2.5, 1.25, 0.625 μM) are predominantly dark red. The row for CPT level 0.3125 μM shows a transition from red at low FBS levels to light blue at higher FBS levels (from 0.625% to 10%). The bottom row for CPT level 0 μM is light blue across all FBS levels.B) Heatmap titled "-p21". The top row for CPT level 5 μM is dark red. The row for CPT level 2.5 μM is red at low FBS levels, transitioning to lighter red/brown at higher FBS levels. The row for CPT level 1.25 μM shows a transition from red at low FBS levels to light blue at higher FBS levels. The rows for CPT levels 0.625, 0.3125, and 0 μM are predominantly light blue across all FBS levels.<::/chart::>

<a id='c004db0e-bf3d-48cd-b0ce-d988ff7cd657'></a>

5

<!-- PAGE BREAK -->

<a id='8d4902b2-8e8a-4a98-b598-2fc27f32d3b6'></a>

**Mathematical modelling**
***Restriction point***
Entry into the cell cycle is control by the restriction point. In order to pass through it, cells hyper-phosphorylate the Rb protein (_Rb_), an inhibitor of the transcription factor E2F (1).

d(Rb_u)
--- = -r_Rb^Ph * Rb_u + k_Rb^Dp * Rb_p
dt

(1)

... Dh . Dh --- . Dh

<a id='8e1458ad-9ad7-436b-8e20-addb66721e11'></a>

with r^(Ph)_Rb = k^(Ph)_(Rb,Cd) · Cd + k^(Ph)_(Rb,Ce) · Ce + k^(Ph)_(Rb,Ca) · Ca,

<a id='7b03da4c-68ca-4946-ac2a-0279bf83afda'></a>

and $Rb_t = Rb_u + Rb_p = Rb + RbE2F + Rb_p,$

<a id='624e9a86-c646-4bac-a448-6a08b1e05f4c'></a>

where Rb_t, Rb_p, and Rb_u denote total, hyper- and hypo-phosphorylated Rb, respectively. The latter comprises both free Rb (Rb) and Rb:E2F complexes (RbE2F). In our model, phosphorylation occurs with rate r^Ph_Rb and is mediated by three cyclin:Cdk complexes: CycD:Cdk4/6 (Cd), CycE:Cdk2 (Ce) and CycA:Cdk2 (Ca) with their specific phosphorylation rates k^Ph_{Rb,Cd}, k^Ph_{Rb,Ce} and k^Ph_{Rb,Ca}, respectively (2). The dephosphorylation rate is k^{Dp}_{Rb}. In its hypo-phosphorylated state Rb binds free E2F (E2F) impairing its ability to promote transcription (1). Hence, we assumed that Rb (hyper-)phosphorylation prevents E2F binding and leads to the dissociation of Rb:E2F complexes.

<a id='737e5f26-e73e-4d1d-862d-9f14bed29059'></a>

$$\frac{\text{d}(E2F_t)}{\text{dt}} = r_{E2F}^{Sy} - k_{E2F}^{De} \cdot E2F_t \quad (2)$$

<a id='c898953a-b4c0-43f1-a4d3-2cc9d5996f41'></a>

$$\frac{d(E2F)}{dt} = r_{E2F}^{Sy} - k_{E2F}^{De} \cdot E2F - k_{RbE2F}^{As} \cdot Rb \cdot E2F + (k_{RbE2F}^{Ds} + r_{Rb}^{Ph}) \cdot RbE2F, \quad (3)$$

<a id='c947c6d4-f90d-4577-bb1f-2b55255d0614'></a>

with $r_{E2F}^{Sy} = k_{E2F}^{Sy} + k_{E2F,E2F}^{Sy} \frac{E2F}{j_{E2F}^{Sy} + E2F}$

<a id='90b27674-40d3-46ba-8bf4-da56fb5b9490'></a>

and $E2F_t = E2F + RbE2F.$

<a id='5f12c363-f075-4d01-a2da-58cf049227eb'></a>

Here, E2F_t and E2F are total and free E2F, respectively, and r^Sy_E2F and k^De_E2F denote the E2F synthesis and degradation rate, respectively. Note that E2F promotes its own transcription (3). Hence, we assumed that synthesis occurs with a constitutive rate (k^Sy_E2F) and an E2F-dependent rate (k^Sy_{E2F,E2F}), where half-maximal synthesis is reach at J^Sy_E2F. Association and dissociation of Rb and E2F are described by the rates k^As_{RbE2F} and k^Ds_{RbE2F}, respectively.

<a id='989e0f5a-4e89-4c72-913e-44f03b799bf5'></a>

_**Synthesis and degradation of cyclins and Emi1**_
Activation of E2F drives the synthesis of a battery of genes that are essential for early cell cycle progression (2, 3). Among these are Emi1 (_E1_), CycE (_Ce_) and CycA (_Ca_).

<a id='e94acdbf-3ddc-47af-835c-74bdfc2b997d'></a>

d(E1_t) / dt = k_E1^Sy * E2F - k_E1,C1^De * E1C1 - k_E1^De * E1, (4)
d(Ce_t) / dt = k_Ce^Sy * E2F - r_Ce^De * Ce_t, (5)
VCe

<a id='519a89a8-6886-49fc-b480-25a154d5a1bf'></a>

d(Ca_t)
---
dt
= k_Ca^Sy \cdot E2F - r_Ca^De \cdot Ca_t

with r_Ce^De = k_Ce^De + k_{Ce,Ca}^De \cdot Ca

(6)

<a id='3dc6beb5-f51d-45a7-8b3f-88f8b06d6615'></a>

r_Ca^{De} = k_Ca^{De} + k_{Ca,C1}^{De} \cdot C1,
and E1_t = E1 + E1C1,

<a id='e3e91d38-777c-445c-bc35-a539966cad9b'></a>

where the index t denotes total protein levels including all complexes that contain the protein. C1 and E1C1 correspond to APC/C<sup>Cdh1</sup> and its complex with Emi1, respectively (see

<a id='8b8317bc-9f34-44f6-874c-ed4bb56ae840'></a>

6

<!-- PAGE BREAK -->

<a id='7f67a0c9-3b93-4cda-a2bd-ebb6de8a4228'></a>

below). The synthesis rates of Emi1, CycE and CycA are k<sup>Sy</sup><sub>E1</sub>, k<sup>Sy</sup><sub>Ce</sub> and k<sup>Sy</sup><sub>Ca</sub>, respectively, while degradation occurs with the constitutive rates k<sup>De</sup><sub>E1</sub>, k<sup>De</sup><sub>Ce</sub> and k<sup>De</sup><sub>Ca</sub>. In addition, Emi1 in Emi1:APC/C<sup>Cdh1</sup> complexes and CycA are degraded with the APC/C<sup>Cdh1</sup>-dependent rates k<sup>De</sup><sub>E1,C1</sub> and k<sup>De</sup><sub>Ca,C1</sub>, respectively (4), while CycE is degraded with the CycA-dependent rate k<sup>De</sup><sub>Ce,Ca</sub> (5, 6). Note that since Cdk2 is in excess over its cyclins (7), Ce and Ca as well as their related variables correspond directly to the levels of CyclE:Cdk2 and CyclA:Cdk2 complexes, respectively.

<a id='5bbd2841-1d14-4f1a-830b-cfcfb344509e'></a>

Inactivation of APC/C<sup>Cdh1</sup>

APC/C<sup>Cdh1</sup> is an ubiquitin E3 ligase that is active from late mitosis to late G1-phase and targets key cell cycle regulators for degradation (4, 8). Its inhibition by Emi1 and by cyclin:Cdk2-mediated phosphorylation is crucial for G1/S progression (4, 9). Therefore, we assumed that APC/C<sup>Cdh1</sup> can exists in a free, active form (C1) as well as two inactive forms: as part of an Emi1:APC/C<sup>Cdh1</sup> complex (E1C1) and as a free but Cdk2-phosphorylated form (C1<sub>p</sub>).

<a id='49514a75-7ace-4711-91d3-f3d60b16b648'></a>

d(C1) / dt - r_C1^Ph · C1 + k_C1^Dp · C1p - k_E1C1^As · E1 · C1 + (k_E1C1^Ds + k_E1,C1^De) · E1C1, (7)
d(E1C1) / dt = -r_C1^Ph · E1C1 + k_E1C1^As · E1 · C1 - (k_E1C1^Ds + k_E1,C1^De) · E1C1, (8)

with r_C1^Ph = k_C1^Ph + k_C1,Ce^Ph · Ce + k_C1,Ca^Ph · Ca,
and C1_t = C1 + C1_p + E1C1.

<a id='b8347373-99cd-4297-a0a8-0b1abb35570c'></a>

Here, phosphorylation occurs with rate r^Ph^C1 comprising the constitutive rate k^Ph^C1 as well as the cyclin:Cdk2-dependent rates k^Ph^C1,Ce and k^Ph^C1,Ca. We assumed that Emi1:APC/C^Cdh1 complexes dissociate upon phosphorylation. Dephosphorylation is described by k^Pp^C1. The rates of association and dissociation of APC/C^Cdh1 and Emi1 are k^As^E1C1 and k^Ds^E1C1, respectively. Note that Emi1 is assumed to act as a pseudo-substrate for the APC/C (10). Hence, we chose k^De^E1,C1 > k^De^E1 (see Eq. (4)).

<a id='2e308079-ff8f-4024-8361-e288dea7ce12'></a>

_**p21 dynamics and Cdk2 inhibition**_
Activation of Cdk2 drives G1/S progression but its kinase activity is opposed by the stoichiometric inhibitor p21 (11). Hence, our model accounts for free p21 (_P21_) and its ability to bind active CycE:Cdk2 (_Ce_) and CycA:Cdk2 (_Ca_) complexes. The resulting complexes of CycE:Cdk2:p21 (_CeP21_) and CycA:Cdk2:p21 (_CaP21_) are considered inactive.

<a id='516363c0-46dd-410a-a9e8-c73dce60648b'></a>

d(P21t)
---
 dt
= kP21Sy + kP21,P53Sy · P53 - rP21De · P21t, (9)

<a id='1fb734b3-4a37-41d6-8087-f52dac73cedb'></a>

d(CeP21)
---
dt
= k^As^CyP21 · P21 · Ce – (k^Ds^CyP21 + r^De^Ce + r^De^P21) · CeP21, (10)

d(CaP21)
---
dt
= k^As^CyP21 · P21 · Ca – (k^Ds^CyP21 + r^De^Ca + r^De^P21) · CaP21, (11)

<a id='baa5e636-4d33-45f9-a267-62b08dfc5203'></a>

with $r_{P21}^{De} = k_{P21}^{De} + k_{P21,Cy}^{De} \cdot Skp2 \cdot (Ce + Ca) + k_{P21,RCa}^{De} \cdot Cdt2 \cdot Rc_a$
$P21_t = P21 + CeP21 + CaP21 + Pcna_1 + Rc_1,$

<a id='04e29d73-8607-4604-873c-d25b4096ede2'></a>

<::Ce_t = Ce + CeP21,
Ca_t = Ca + CaP21.
: figure::>

<a id='81d1e594-bdb1-4e5f-bcc6-b2b2682f0951'></a>

7

<!-- PAGE BREAK -->

<a id='046861fa-3ab9-41c5-a106-71d92bda582b'></a>

Here, synthesis of p21 occurs with the constitutive rate k<sup>Sy</sup><sub>P21</sub> and the p53-dependent rate k<sup>Sy</sup><sub>P21,P53</sub>, where *P53* denotes the transcription factor p53 (12). The degradation rate of p21 is denoted r<sup>De</sup><sub>P21</sub> and comprises a constitutive rate (k<sup>De</sup><sub>P21</sub>) as well as a cyclin:Cdk2-dependent rate (k<sup>De</sup><sub>P21,Cy</sub>) that is linked to the ubiquitin E3 ligase SCF<sup>Skp2</sup> (*Skp2*, (13, 14)). In addition, CRL4<sup>Cdt2</sup> (*Cdt2*), which is recruited to chromatin-bound PCNA within active replication complexes (*Rc<sub>a</sub>*, see below), can mediate p21 degradation with rate k<sup>De</sup><sub>P21,RCa</sub> (13, 15). In our model, free p21 can bind to cyclin:Cdk2 complexes with rate k<sup>As</sup><sub>CyP21</sub> and dissociate from these complexes with rate k<sup>Ds</sup><sub>CyP21</sub>. Furthermore, the total amount of p21 (P21<sub>t</sub>) comprises free p21 (*P21*) as well as p21 in complexes with cyclin:Cdk2 (*CeP21* and *CaP21*), PCNA (*Pcna<sub>i</sub>*), and replication complexes (*Rc<sub>i</sub>*, see below).

<a id='f061bb51-86d6-4e10-863f-acf19f1acc8a'></a>

*Activation of DNA replication*
During S-phase, DNA is synthesised by specialised replication complexes that assemble on licensed replication origins once there is sufficient Cdk2 activity (16). Therefore, we assumed that Cdk2 activates pre-replication complexes (_Rc_) such that they are primed (_Rc_p) for the loading of DNA processivity factors.

<a id='2632ece4-065f-4165-976e-ffac9fd9ae3f'></a>

d(Rc) / dt = -r_Rc^Ph · Rc + k_Rc^Dp · Rc_p - r_Rc^Ds · Rc,

(12)

<a id='0e755328-e3f4-4c25-bcf7-1592fe7b8d7e'></a>

with $r_{Rc}^{Ph} = k_{Rc}^{Ph} \frac{(Ce+Ca)^n}{(j_{Cy})^n + (Ce+Ca)^{n'}}$

<a id='3b5c1add-29d4-41eb-b52b-fde69969b725'></a>

where priming occurs with rate k_Rc^Ph in an ultrasensitive fashion with hill coefficient n at a cyclin:Cdk2 threshold of j_Cy. Primed replication complexes can revert back to an unprimed state with a small rate k_Rc^Dp and replication complexes are disassembled upon completion of S-phase with rate r_Rc^Ds (see below). Once primed, replication complexes can bind PCNA, which forms a trimeric complex around the DNA that serves as a sliding platform for other processivity factors (17). We assumed that either free PCNA (PCNA_a) or PCNA:p21 complexes (PCNA_i) are bound leading to the formation of active (Rc_a) or inactive (Rc_i) replication complexes, respectively.

<a id='a8c2d0a7-5c52-4e5f-a023-a1c5ca8dbabd'></a>

d(Rc_p) / dt = r_Rc^Ph * Rc - k_Rc^Dp * Rc_p - k_RcPc^As * (Pcna_a + Pcna_i) * Rc_p + k_RcPc^Ds * (Rc_a + Rc_i)
- r_Rc^Ds * Rc_p, (13)

d(Rc_a) / dt = -k_PcP21^As * P21 * Rc_a + (k_PcP21^Ds + r_P21^De) * Rc_i + k_RcPc^As * Pcna_a * Rc_p - k_RcPc^Ds * Rc_a
- r_Rc^Ds * Rc_a, (14)

d(Rc_i) / dt = k_PcP21^As * P21 * Rc_a - (k_PcP21^Ds + r_P21^De) * Rc_i + k_RcPc^As * Pcna_i * Rc_p - k_RcPc^Ds * Rc_i
- r_Rc^Ds * Rc_i. (15)

<a id='acfa666d-a7cb-4df5-b4ff-cb537cebcea1'></a>

The rates of PCNA loading and unloading are $k_{RcPc}^{As}$ and $k_{RcPc}^{Ds}$, respectively. Also note that p21 is the strongest known binding partner of PCNA (18) and it was proposed to compete with other PCNA-binding proteins (17, 19). Thus, we assumed that binding of p21 to active replication complexes with rate $k_{PcP21}^{As}$ (or binding of PCNA:p21 to primed replication complexes) creates inactive replication complexes (20, 21). The dissociation of p21 from PCNA occurs with rate $k_{PcP21}^{Ds}$. In our model, active replication complexes synthesise DNA ($DNA$) and once DNA replication is finished, replication complexes disassemble with rate $r_{Rc}^{Ds}$.

<a id='2a3480d3-8fd3-4ece-8356-d0e2e91c8f87'></a>

d(DNA) / dt = k_DNA^Sy * Rca
and r_Rc^Ds = H(DNA - 1),

(16)

<a id='eeb41fd7-4466-4f6a-9f4b-030b2db94ab4'></a>

8

<!-- PAGE BREAK -->

<a id='dfa63dbd-1e2b-41e9-88a8-ebd38327c53a'></a>

where k^Sy_DNA is the DNA synthesis rate and *H* the Heaviside function.

<a id='3b0da469-eeb3-4007-b831-a81f4997c531'></a>

**PCNA dynamics**
We assumed that free PCNA in the nucleus (*Pcna*<sub>a</sub>) is replenished from a cytoplasmic pool and that p21 can bind to PCNA creating PCNA:p21 complexes (*Pcna*<sub>i</sub>, (18)).

<a id='c8af923c-bd4b-4252-b492-dbe29fd0dc5a'></a>

d(Pcna_a)
---
dt
= k_Pc^Im - k_PcP21^As * P21 * Pcna_a + (k_PcP21^Ds + r_P21^De) * Pcna_i
- (k_Pc^Ex + k_Rc_Pc^As * Rc_p) * Pcna_a + (k_Rc_Pc^Ds + r_Rc^Ds) * Rc_a, (17)

d(Pcna_i)
---
dt
= k_PcP21^As * P21 * Pcna_a - (k_PcP21^Ds + r_P21^De) * Pcna_i
- (k_Pc^Ex + k_Rc_Pc^As * Rc_p) * Pcna_i + (k_Rc_Pc^Ds + r_Rc^Ds) * Rc_i. (18)

<a id='2e2b810c-bed4-48c9-ba86-d005ecc1c9d1'></a>

Here, k_Pc^Im and k_Pc^Ex denote the nuclear import and export rate PCNA, respectively. The association and dissociation of p21 and PCNA occur with rate k_PcP21^As and k_PcP21^Ds, respectively. The binding and unbinding rates of PCNA and replication complexes are k_RcPc^As and k_RcPc^Ds, respectively.

<a id='0c3f8a6e-bea6-461a-a5f5-63fb8bec4d2f'></a>

_**DNA damage and repair**_

In our model, DNA damage (_Dam_) can either occur independent of the cell cycle stage or specifically during DNA replication. It induces the expression of p53 (_P53_), which promotes damage repair processes (22).

<a id='2572ad16-72d2-48cd-bee8-05ab5c0647b7'></a>

d(Dam) = kDam^Ge + kDam,RC_a^Ge * RC_a - rDam^Re * Dam,
dt

(19)

<a id='2d3e7423-920a-41d9-a4c6-d86d14ddd04a'></a>

d(P53)
--- = k^Sy_P53 - r^De_P53 · P53, (20)
dt

<a id='5a1e2af3-bc99-4a09-8048-4533b25f1b6f'></a>

with $r_{\text{Dam}}^{\text{Re}} = k_{\text{Dam}}^{\text{Re}} + k_{\text{Dam,P53}}^{\text{Re}} \frac{\text{P53}}{j_{\text{Dam}}+\text{Dam}'}$

and $r_{\text{P53}}^{\text{De}} = \frac{k_{\text{P53}}^{\text{De}}}{j_{\text{P53}}+\text{Dam}'}$

<a id='91382dd9-d2bf-406b-85f0-a92a50398a62'></a>

where k^Ge^~Dam~ and k^Ge^~Dam,RC a~ correspond to the constitutive and DNA replication-dependent rates of damage induction, respectively. Damage is repaired with a constitutive rate (k^Re^~Dam~) and a p53-dependent rate (k^Re^~Dam,P53~) assuming that p53 expression triggers repair processes. The latter reaches its half-maximal rate at a damage level of j^~Dam~. Since DNA damage has been shown to stabilize p53 (23), we assumed that p53 synthesis occurs with a constitutive rate (k^Sy^~P53~), while degradation occurs with rate k^De^~P53~, which is inversely proportional to the sum of DNA damage and an inhibition constant j^~P53~.

<a id='6fd3f0db-7ec1-4b18-bd26-e0e3edb744b7'></a>

***Cdh1 activity reporter***

In order to compare our simulation results with measurements of Cdh1 activity obtained by following the degradation of a model APC/CCdh1 substrate (24), we simulated such an activity probe (_Pr_).

<a id='2c586654-0e27-44a6-8b19-e22379c88840'></a>

$\frac{d(Pr)}{dt} = k_{Pr}^{Sy} - (k_{Pr}^{De} + k_{Ca,C1}^{De} \cdot C1) \cdot Pr,\quad(21)$

<a id='57e3eee4-192f-4c84-9717-1508e5f070a9'></a>

where the constitutive synthesis and degradation rates of the probe are k_Pr^Sy and k_Pr^De, respectively, and, without loss of generality, the Cdh1-dependent degradation rate k_Ca,C1^De is the same than for CycA. Based on the analysis of experimental data (24), we calculated Cdh1 activity (C1_act) using the following equation.

<a id='72244d08-8b78-47b9-8967-810ef13510e2'></a>

9

<!-- PAGE BREAK -->

<a id='1dfc35d9-1c19-48d8-8517-6f995c72d9f6'></a>

$$C1_{act} = \frac{k_{Pr}^{Sy} - \frac{\Delta(Pr + Bg)}{\Delta t}}{Pr + Bg}$$ (22)

<a id='f7f317d9-cc07-443a-925e-983f3b17ab96'></a>

Here, we added a small background signal (_Bg_) to reflect that while small changes in probe
concentration can be accurately calculated from numerical data they might be below the
signal-to-noise ratio in experiments.

<a id='dea4ab81-5ccd-46e1-bab8-aa81bcd33878'></a>

## Computation
A deterministic version of the model was prepared using the Systems Biology Toolbox 2 (25) for MatLab (version 9.1.0 R2016b) and simulated with the CVODE routine (26). Bifurcation diagrams were calculated using the freely available software XPP-Aut (27). The model is provided as Dataset S1 and different versions of it are available at www.cellcycle.org.uk/publication. The model was also deposited in BioModels (28) and assigned the identifier MODEL1703030000.

<a id='5b739012-46df-4524-99ee-e0d8c3c7e303'></a>

We simulated a stochastic version of the model using custom-made MatLab code of the stochastic simulation algorithm, also known as Gillespie's algorithm (reviewed in (29)), according to the sorting direct method (30). To this end, the rate expressions of the deterministic model were converted into propensity functions, which requires the transformation of the relative levels of cell cycle regulators into numbers of molecules. Here, we followed the system in a control volume containing on average 1000 molecules/AU of protein and 1 event/AU of DNA damage. Hence, most of the simulated cell-to-cell variability originates in the stochastic infliction of DNA damage, while transcriptional and translational noise play only a minor role. To account for the extrinsic noise observed in our experiments, i.e., the variability in p21 levels after cell division, we chose the initial p21 level for each cell (simulation run) from a log-normal distribution with µ = -0.5 and σ = 0.3. This distribution is based on the distribution of initial p21 levels estimated from experiments (μ = 2.4, σ = 0.3), which was rescaled to account for the difference in p21 level between experiments and simulations. For the simulation of depletion experiments Skp2 and/or Cdt2 were reduced to 1%.

<a id='ed11d580-09b0-409b-be36-defbc37e2ca8'></a>

To classify cells as either proliferating or quiescent we used the fact that these two fates represent attractors in state space in our model (see Fig. 2C-F). In particular, quiescent cells are characterised by high p21 levels as well as low Cdk2 activity, Rb hypo-phosphorylation and low E2F activity, which prevents entry into S-phase. Hence, simulated cells that maintain these features were classified as quiescent, while cells that did enter S-phase were deemed proliferating.

<a id='c2e3e084-8532-47ca-81fa-75bb69e09d62'></a>

**Model parameters**
Parameter values and non-zero initial conditions of the model are listed in Tables S1 and S2, respectively. A large part of the parameter set is based on our previously published study of p21 dynamics (31), where the model was parameterised to capture p21 dynamics in individual, unperturbed hTert-RPE1 cells as well as in perturbation experiments such as upon depletion of Skp2 and Cdt2. This includes parameters for p21 synthesis and degradation, the import, export, phosphorylation and binding of PCNA, and the dynamics of p53 and DNA damage. Parameter values for the newly added restriction point module are based on experimental observations and were adapted to reproduce cell cycle progression in RPE1 cells (see Fig. 1C-E). In particular, we assumed that in its hypo-phosphorylated state Rb binds tightly to E2F as it was shown to act as a stoichiometric inhibitor (1). Synthesis and degradation of E2F were chosen to yield a bistable response, which was found experimentally (32). Inhibition of APC/C⁷ᐦ⁷ by Emil was modelled via a pseudo-substrate

<a id='2c3086c6-05c0-4a31-8a3c-854c5d0b3b78'></a>

10

<!-- PAGE BREAK -->

<a id='b30982ad-0612-4738-8217-9474aeb931ba'></a>

inhibitor mechanism (10), implying tight binding of both and a slow turnover of Emi1 by Cdh1. Synthesis and degradation of Emi1 and phosphorylation of APC/C<sup>Cdh1</sup> were adjusted to yield a rapid, switch-like inactivation of APC/C<sup>Cdh1</sup> at the G1/S transition based on measurements of APC/C activity (24). Parameters for CycE and CycA synthesis and degradation were chosen to qualitatively match the measurements of both proteins in live, single cells (9) and of overall Cdk2 activity (31, 33), while accounting for the length of cell cycle phases in RPE1 cells (see Fig. 1E). Local parameter sensitivities (see Table S1) were calculated according to

<a id='774dc4f3-0a21-4cd9-85dc-112a738bcb4f'></a>

S_θ = \frac{\Delta M}{M} \frac{\theta}{\Delta \theta}

with

\frac{\Delta M}{M} = \frac{1}{N_v N_t} \sum_{v,t} \left(\frac{y_v(\theta, t) - y_v(\theta^*, t)}{\sigma_v}\right)^2

<a id='028c0777-6f0e-4901-8b77-011732a3090b'></a>

where Sθ is the local sensitivity of parameter θ, comprising the relative change in model output M with respect to the relative change in parameter θ. The relative change in model output was defined as the squared change in state variable V at time t given the original parameter set (yv(θ, t)) and the same output in response to a parameter change (yv(θ*, t)), normalised by the maximum value of variable V (σv), which was summed over all time points and state variables and normalised to the number of simulated time points (Nt) and state variables (Nv), following (34).

<a id='f14c201e-33e1-47a1-ac39-05a95b598e9a'></a>

11

<!-- PAGE BREAK -->

<a id='414be66d-ed6a-419c-9be1-bfd0470f0b73'></a>

Supporting tables

<a id='2fce4ae1-b52a-400b-bb3c-2dfabc505626'></a>

<table id="11-1">
<tr><td id="11-2" colspan="2">Table S1. Parameters of the mathematical model.</td><td id="11-3"></td><td id="11-4"></td><td id="11-5"></td></tr>
<tr><td id="11-6">Parameter</td><td id="11-7">Description</td><td id="11-8">Value</td><td id="11-9">Unit</td><td id="11-a">Local Sensitivity (%)</td></tr>
<tr><td id="11-b">Bg</td><td id="11-c">background of Cdh1-activity probe</td><td id="11-d">0.05</td><td id="11-e">AU</td><td id="11-f">—</td></tr>
<tr><td id="11-g">C1t</td><td id="11-h">total APC/CCdh1 level</td><td id="11-i">1</td><td id="11-j">AU</td><td id="11-k">0.26</td></tr>
<tr><td id="11-l">Cd</td><td id="11-m">relative CycD:Cdk4/6 level</td><td id="11-n">0.65</td><td id="11-o">AU</td><td id="11-p">1.33</td></tr>
<tr><td id="11-q">Cdt2</td><td id="11-r">relative CRL4Cdt2 level</td><td id="11-s">1 (0.01a)</td><td id="11-t">–</td><td id="11-u">0.01</td></tr>
<tr><td id="11-v">Rb t</td><td id="11-w">total Rb level</td><td id="11-x">5</td><td id="11-y">AU</td><td id="11-z">4.42</td></tr>
<tr><td id="11-A">Skp2</td><td id="11-B">relative SCFSkp2 level</td><td id="11-C">1 (0.01a)</td><td id="11-D">–</td><td id="11-E">0.14</td></tr>
<tr><td id="11-F">jcy</td><td id="11-G">Cdk2 threshold for RC priming</td><td id="11-H">1.8</td><td id="11-I">AU</td><td id="11-J">2.4</td></tr>
<tr><td id="11-K">jDam</td><td id="11-L">DNA damage threshold for repair</td><td id="11-M">0.5</td><td id="11-N">AU</td><td id="11-O">0.002</td></tr>
<tr><td id="11-P">JP53</td><td id="11-Q">inhibition constant of p53 degradation</td><td id="11-R">0.01</td><td id="11-S">AU</td><td id="11-T">1·10-4</td></tr>
<tr><td id="11-U">J E2F</td><td id="11-V">Michealis-Menten constant for E2F synthesis</td><td id="11-W">0.2</td><td id="11-X">AU</td><td id="11-Y">0.7</td></tr>
<tr><td id="11-Z">k CyP21</td><td id="11-10">association of p21 and cyclin:Cdk2</td><td id="11-11">1</td><td id="11-12">1/(AU·min)</td><td id="11-13">0.002</td></tr>
<tr><td id="11-14">k E1C1</td><td id="11-15">association of Emi1 and APC/Cdh1</td><td id="11-16">10</td><td id="11-17">1/(AU·min)</td><td id="11-18">0.1</td></tr>
<tr><td id="11-19">KAS KPCP21</td><td id="11-1a">association of PCNA and p21</td><td id="11-1b">100</td><td id="11-1c">1/(AU·min)</td><td id="11-1d">0.001</td></tr>
<tr><td id="11-1e">kRbE2F (As)</td><td id="11-1f">association of Rb and E2F</td><td id="11-1g">5</td><td id="11-1h">1/(AU·min)</td><td id="11-1i">0.34</td></tr>
<tr><td id="11-1j">kRcPc (As)</td><td id="11-1k">association of primed RCs and PCNA</td><td id="11-1l">0.01</td><td id="11-1m">1/(AU·min)</td><td id="11-1n">0.45</td></tr>
<tr><td id="11-1o">kCa (De)</td><td id="11-1p">constitutive CycA degradation</td><td id="11-1q">0.01</td><td id="11-1r">1/min</td><td id="11-1s">0.15</td></tr>
<tr><td id="11-1t">kCa,C1 (De)</td><td id="11-1u">APC/Cdh1-mediated CycA degradation</td><td id="11-1v">2</td><td id="11-1w">1/(AU·min)</td><td id="11-1x">0.16</td></tr>
<tr><td id="11-1y">kCe (De)</td><td id="11-1z">constitutive CycE degradation</td><td id="11-1A">0.004</td><td id="11-1B">1/min</td><td id="11-1C">0.89</td></tr>
<tr><td id="11-1D">k Ce,Ca (superscript De)</td><td id="11-1E">CycA:Cdk2-mediated CycE degradation</td><td id="11-1F">0.015</td><td id="11-1G">1/(AU·min)</td><td id="11-1H">0.48</td></tr>
<tr><td id="11-1I">k E1 (superscript De)</td><td id="11-1J">constitutive Emi1 degradation</td><td id="11-1K">0.0005</td><td id="11-1L">1/min</td><td id="11-1M">0.002</td></tr>
<tr><td id="11-1N">k E1,C1 (superscript De)</td><td id="11-1O">APC/Cdh1-mediated Emi1 degradation</td><td id="11-1P">0.005</td><td id="11-1Q">1/min</td><td id="11-1R">0.01</td></tr>
<tr><td id="11-1S">k E2F (superscript De)</td><td id="11-1T">constitutive E2F degradation</td><td id="11-1U">0.05</td><td id="11-1V">1/min</td><td id="11-1W">10.55</td></tr>
<tr><td id="11-1X">k P21 (superscript De)</td><td id="11-1Y">constitutive p21 degradation</td><td id="11-1Z">0.0025</td><td id="11-20">1/min</td><td id="11-21">0.05</td></tr>
<tr><td id="11-22">k
De
P21,Cy</td><td id="11-23">cyclin:Cdk2-mediated p21 degradation</td><td id="11-24">0.007</td><td id="11-25">1/(AU·min)</td><td id="11-26">0.14</td></tr>
<tr><td id="11-27">k
De
P21,RCa</td><td id="11-28">RCa-mediated p21 degradation</td><td id="11-29">1</td><td id="11-2a">1/(AU·min)</td><td id="11-2b">0.005</td></tr>
<tr><td id="11-2c">k
De
P53</td><td id="11-2d">DNA damage-dependent p53 degradation</td><td id="11-2e">0.05</td><td id="11-2f">AU/min</td><td id="11-2g">0.02</td></tr>
<tr><td id="11-2h">k
De
Pr</td><td id="11-2i">constitutive degradation of Cdh1-activity probe</td><td id="11-2j">0.0001</td><td id="11-2k">1/min</td><td id="11-2l">1·10-5</td></tr>
<tr><td id="11-2m">k
Dp
C1</td><td id="11-2n">dephosphorylation of APC/CCdh1</td><td id="11-2o">0.05</td><td id="11-2p">1/min</td><td id="11-2q">0.17</td></tr>
<tr><td id="11-2r">kDpRb</td><td id="11-2s">dephosphorylation of Rb</td><td id="11-2t">0.05</td><td id="11-2u">1/min</td><td id="11-2v">3.61</td></tr>
<tr><td id="11-2w">kDpRc</td><td id="11-2x">dephosphorylation of primed RCs</td><td id="11-2y">0.05</td><td id="11-2z">1/min</td><td id="11-2A">0.2</td></tr>
<tr><td id="11-2B">kDsCyP21</td><td id="11-2C">dissociation of cyclin:Cdk2:p21 complexes</td><td id="11-2D">0.05</td><td id="11-2E">1/min</td><td id="11-2F">0.001</td></tr>
<tr><td id="11-2G">kDSE1C1</td><td id="11-2H">dissociation of Emi1:APC/Cdh1 complexes</td><td id="11-2I">0.01</td><td id="11-2J">1/min</td><td id="11-2K">1·10-5</td></tr>
<tr><td id="11-2L">kDsPcP21</td><td id="11-2M">dissociation of PCNA:p21 complexes</td><td id="11-2N">0.01</td><td id="11-2O">1/min</td><td id="11-2P">1·10-4</td></tr>
<tr><td id="11-2Q">k Ds RbE2F</td><td id="11-2R">dissociation of Rb:E2F complexes</td><td id="11-2S">0.005</td><td id="11-2T">1/min</td><td id="11-2U">6·10-5</td></tr>
<tr><td id="11-2V">k Ds RCpPC</td><td id="11-2W">dissociation of RCp:PCNA complexes</td><td id="11-2X">0.001</td><td id="11-2Y">1/min</td><td id="11-2Z">0.01</td></tr>
<tr><td id="11-30">k Ex PC</td><td id="11-31">PCNA export from the nucleus</td><td id="11-32">0.006</td><td id="11-33">1/min</td><td id="11-34">0.91</td></tr>
<tr><td id="11-35">k Ge Dam</td><td id="11-36">replication-independent DNA damage</td><td id="11-37">0.001</td><td id="11-38">AU/min</td><td id="11-39">0.01</td></tr>
<tr><td id="11-3a">k Ge Dam,RCa</td><td id="11-3b">replication-dependent DNA damage</td><td id="11-3c">0.012</td><td id="11-3d">1/min</td><td id="11-3e">0.01</td></tr>
<tr><td id="11-3f">kPCIm</td><td id="11-3g">PCNA import into the nucleus</td><td id="11-3h">0.003</td><td id="11-3i">AU/min</td><td id="11-3j">1</td></tr>
<tr><td id="11-3k">kC1Ph</td><td id="11-3l">constitutive APC/Cdh1 phosphorylation</td><td id="11-3m">0</td><td id="11-3n">1/min</td><td id="11-3o"></td></tr>
<tr><td id="11-3p">kC1,CaPh</td><td id="11-3q">CycA:Cdk2-mediated APC/Cdh1 phosphorylation</td><td id="11-3r">1</td><td id="11-3s">1/(AU·min)</td><td id="11-3t">0.01</td></tr>
<tr><td id="11-3u">kC1,CePh</td><td id="11-3v">CycE:Cdk2-mediated APC/Cdh1 phosphorylation</td><td id="11-3w">0.01</td><td id="11-3x">1/(AU·min)</td><td id="11-3y">5·10-4</td></tr>
<tr><td id="11-3z">kRbCaPh</td><td id="11-3A">CycA:Cdk2-mediated Rb phosphorylation</td><td id="11-3B">0.3</td><td id="11-3C">1/(AU·min)</td><td id="11-3D">0.13</td></tr>
</table>

<a id='aa5594d1-e6fd-43a0-8ace-6bbd255b1d0e'></a>

12

<!-- PAGE BREAK -->

<a id='6de5a53c-5f26-4ed7-95e8-662e13705e19'></a>

<table id="12-1">
<tr><td id="12-2">kRbCd Ph</td><td id="12-3">CycD:Cdk4/6-mediated Rb phosphorylation</td><td id="12-4">0.2</td><td id="12-5">1/(AU·min)</td><td id="12-6">1.33</td></tr>
<tr><td id="12-7">kRbCe Ph</td><td id="12-8">CycE:Cdk2-mediated Rb phosphorylation</td><td id="12-9">0.3</td><td id="12-a">1/(AU·min)</td><td id="12-b">1.68</td></tr>
<tr><td id="12-c">kRc Ph</td><td id="12-d">cyclin:Cdk2-mediated priming of RCs</td><td id="12-e">0.1</td><td id="12-f">1/min</td><td id="12-g">0.27</td></tr>
<tr><td id="12-h">kDam Re</td><td id="12-i">p53-independent DNA damage repair</td><td id="12-j">0.001</td><td id="12-k">1/min</td><td id="12-l">0.001</td></tr>
<tr><td id="12-m">kDam,P53 Re</td><td id="12-n">p53-dependent DNA damage repair</td><td id="12-o">0.005</td><td id="12-p">1/min</td><td id="12-q">0.001</td></tr>
<tr><td id="12-r">k_{Ca}^{Sy}</td><td id="12-s">constitutive CycA synthesis</td><td id="12-t">0.02</td><td id="12-u">1/min</td><td id="12-v">0.52</td></tr>
<tr><td id="12-w">k_{Ce}^{Sy}</td><td id="12-x">constitutive CycE synthesis</td><td id="12-y">0.01</td><td id="12-z">1/min</td><td id="12-A">2.14</td></tr>
<tr><td id="12-B">k_{Dna}^{Sy}</td><td id="12-C">DNA synthesis by active RCs</td><td id="12-D">0.0093</td><td id="12-E">1/min</td><td id="12-F">0.73</td></tr>
<tr><td id="12-G">k_{E1}^{Sy}</td><td id="12-H">constitutive Emi1 synthesis</td><td id="12-I">0.005</td><td id="12-J">1/min</td><td id="12-K">0.26</td></tr>
<tr><td id="12-L">k_{E2F}^{Sy}</td><td id="12-M">constitutive E2F synthesis</td><td id="12-N">0.03</td><td id="12-O">AU/min</td><td id="12-P">4.94</td></tr>
<tr><td id="12-Q">kSy E2F,E2F</td><td id="12-R">E2F-dependent E2F synthesis</td><td id="12-S">0.04</td><td id="12-T">AU/min</td><td id="12-U">4.09</td></tr>
<tr><td id="12-V">kSy P21</td><td id="12-W">constitutive p21 synthesis</td><td id="12-X">0.002</td><td id="12-Y">AU/min</td><td id="12-Z">0.14</td></tr>
<tr><td id="12-10">kSy P21,P53</td><td id="12-11">p53-dependent p21 synthesis</td><td id="12-12">0.008</td><td id="12-13">1/min</td><td id="12-14">0.02</td></tr>
<tr><td id="12-15">kSy P53</td><td id="12-16">constitutive p53 synthesis</td><td id="12-17">0.05</td><td id="12-18">AU/min</td><td id="12-19">0.02</td></tr>
<tr><td id="12-1a">kSy Pr</td><td id="12-1b">constitutive synthesis of Cdh1 activity probe</td><td id="12-1c">0.01</td><td id="12-1d">AU/min</td><td id="12-1e">0.04</td></tr>
<tr><td id="12-1f">n</td><td id="12-1g">hill coefficient for priming of RCs</td><td id="12-1h">6</td><td id="12-1i"></td><td id="12-1j">0.29</td></tr>
</table>
ªin simulations of depletion experiments

<a id='78fcb437-6e86-49bd-ade1-76639eeb7b9b'></a>

<table id="12-1k">
<tr><td id="12-1l" colspan="4">Table S2. Non-zero initial conditions of the mathematical model.a</td></tr>
<tr><td id="12-1m">Variable</td><td id="12-1n">Description</td><td id="12-1o">Value</td><td id="12-1p">Unit</td></tr>
<tr><td id="12-1q">Cat</td><td id="12-1r">CycA:Cdk2 level</td><td id="12-1s">1.2</td><td id="12-1t">AU</td></tr>
<tr><td id="12-1u">Cet</td><td id="12-1v">CycE:Cdk2 level</td><td id="12-1w">0.5</td><td id="12-1x">AU</td></tr>
<tr><td id="12-1y">P21t</td><td id="12-1z">total p21 level</td><td id="12-1A">0.6</td><td id="12-1B">AU</td></tr>
<tr><td id="12-1C">Рспаа</td><td id="12-1D">free PCNA in the nucleus</td><td id="12-1E">0.5</td><td id="12-1F">AU</td></tr>
<tr><td id="12-1G">Rc</td><td id="12-1H">pre-replication complexes</td><td id="12-1I">1</td><td id="12-1J">AU</td></tr>
</table>
ªThese values correspond to a newly-born cell.

<a id='5de5fe91-b72d-4040-b9a2-eb37ef8f34a3'></a>

13

<!-- PAGE BREAK -->

<a id='e6f01f54-c6ab-4134-bf3c-04bb630054c9'></a>

Supporting references
1. Frolov MV, Dyson NJ (2004) Molecular mechanisms of E2F-dependent activation and pRB-mediated repression. J Cell Sci 117(11):2173–2181.
2. Bertoli C, Skotheim JM, de Bruin RAM (2013) Control of cell cycle transcription during G1 and S phases. Nat Rev Mol Cell Biol 14(8):518–528.
3. Bracken AP, Ciro M, Cocito A, Helin K (2004) E2F target genes: unraveling the biology. Trends Biochem Sci 29(8):409–417.
4. Pines J (2011) Cubism and the cell cycle: the many faces of the APC/C. Nat Rev Mol Cell Biol 12(7):427–438.
5. Kalaszczynska I, et al. (2009) Cyclin A is redundant in fibroblasts but essential in hematopoietic and embryonic stem cells. Cell 138(2):352–365.
6. Won KA, Reed SI (1996) Activation of cyclin E/CDK2 is coupled to site-specific autophosphorylation and ubiquitin-dependent degradation of cyclin E. EMBO J 15(16):4182–4193.
7. Arooz T, et al. (2000) On the concentrations of cyclins and cyclin-dependent kinases in extracts of cultured human cells. Biochemistry (Mosc) 39(31):9494–9501.
8. Sivakumar S, Gorbsky GJ (2015) Spatiotemporal regulation of the anaphase-promoting complex in mitosis. Nat Rev Mol Cell Biol 16(2):82–94.
9. Barr AR, Heldt FS, Zhang T, Bakal C, Novák B (2016) A Dynamical Framework for the All-or-None G1/S Transition. Cell Syst 2(1):27–37.
10. Miller JJ, et al. (2006) Emi1 stably binds and inhibits the anaphase-promoting complex/cyclosome as a pseudosubstrate inhibitor. Genes Dev 20(17):2410–2420.
11. Harper JW, et al. (1995) Inhibition of cyclin-dependent kinases by p21. Mol Biol Cell 6(4):387–400.
12. El-Deiry WS, et al. (1993) WAF1, a potential mediator of p53 tumor suppression. Cell 75(4):817–825.
13. Starostina NG, Kipreos ET (2012) Multiple degradation pathways regulate versatile CIP/KIP CDK inhibitors. Trends Cell Biol 22(1):33–41.
14. Frescas D, Pagano M (2008) Deregulated proteolysis by the F-box proteins SKP2 and beta-TrCP: tipping the scales of cancer. Nat Rev Cancer 8(6):438–449.
15. Havens CG, Walter JC (2011) Mechanism of CRL4(Cdt2), a PCNA-dependent E3 ubiquitin ligase. Genes Dev 25(15):1568–1582.
16. Diffley JFX (2004) Regulation of early events in chromosome replication. Curr Biol 14(18):R778–R786.
17. Moldovan G-L, Pfander B, Jentsch S (2007) PCNA, the maestro of the replication fork. Cell 129(4):665–679.
18. Bruning JB, Shamoo Y (2004) Structural and thermodynamic analysis of human PCNA with peptides derived from DNA polymerase-delta p66 subunit and flap endonuclease-1. Structure 12(12):2209–2219.
19. Waga S, Hannon GJ, Beach D, Stillman B (1994) The p21 inhibitor of cyclin-dependent kinases controls DNA replication by interaction with PCNA. Nature 369(6481):574–578.
20. Cayrol C, Knibiehler M, Ducommun B (1998) p21 binding to PCNA causes G1 and G2 cell cycle arrest in p53-deficient cells. Oncogene 16(3):311–320.
21. Rousseau D, et al. (1999) Growth inhibition by CDK-cyclin and PCNA binding domains of p21 occurs by distinct mechanisms and is regulated by ubiquitin-proteasome pathway. Oncogene 18(30):4313–4325.
22. Menon V, Povirk L (2014) Involvement of p53 in the repair of DNA double strand breaks: multifaceted Roles of p53 in homologous recombination repair (HRR) and non-homologous end joining (NHEJ). Subcell Biochem 85:321–336.
23. Kruse J-P, Gu W (2009) Modes of p53 regulation. Cell 137(4):609–622.
24. Cappell SD, Chung M, Jaimovich A, Spencer SL, Meyer T (2016) Irreversible APC(Cdh1) Inactivation Underlies the Point of No Return for Cell-Cycle Entry. Cell 166(1):167–180.

<a id='2d0d82a8-d040-407e-b5ea-379b4e832a22'></a>

14

<!-- PAGE BREAK -->

<a id='c1e87968-c5b0-46f2-8afd-16dfe9b79e72'></a>

25. Schmidt H, Jirstrand M (2006) Systems Biology Toolbox for MATLAB: a computational platform for research in systems biology. *Bioinformatics* 22(4):514–515.
26. Cohen S, Hindmarsh AC (1996) CVODE, a stiff/nonstiff ODE solver in C. *Computers in Physics*, pp 138–143.
27. Ermentrout B (2002) *Simulating, Analyzing, and Animating Dynamical Systems* (Society for Industrial and Applied Mathematics) doi:10.1137/1.9780898718195.
28. Chelliah V, et al. (2015) BioModels: ten-year anniversary. *Nucleic Acids Res* 43(D1):D542–D548.
29. Gillespie DT (2007) Stochastic Simulation of Chemical Kinetics. *Annu Rev Phys Chem* 58(1):35–55.
30. McCollum JM, Peterson GD, Cox CD, Simpson ML, Samatova NF (2006) The sorting direct method for stochastic simulation of biochemical systems with varying reaction execution behavior. *Comput Biol Chem* 30(1):39–49.
31. Barr AR, et al. (2017) DNA damage during S-phase mediates the proliferation-quiescence decision in the subsequent G1 via p21 expression. *Nat Commun* 8:14728.
32. Yao G, Lee TJ, Mori S, Nevins JR, You L (2008) A bistable Rb–E2F switch underlies the restriction point. *Nat Cell Biol* 10(4):476–482.
33. Spencer SL, et al. (2013) The proliferation-quiescence decision is controlled by a bifurcation in CDK2 activity at mitotic exit. *Cell* 155(2):369–383.
34. Gutenkunst RN, et al. (2007) Universally Sloppy Parameter Sensitivities in Systems Biology Models. *PLoS Comput Biol* 3(10):e189.

<a id='28de9f91-250b-4107-8669-88abff58c07b'></a>

15
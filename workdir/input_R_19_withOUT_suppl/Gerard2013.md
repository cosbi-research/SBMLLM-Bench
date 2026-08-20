<a id='d00694ae-4f5d-4a06-94df-cc0c8bc13844'></a>

Biophysical Journal Volume 104 March 2013 1367–1379

<a id='f994841b-047b-42a5-ab2d-a9bdcd69b27d'></a>

1367

<a id='bce24636-d3fa-46aa-8616-3f6560d69ae4'></a>

Minimal Models for Cell-Cycle Control Based on Competitive Inhibition
and Multisite Phosphorylations of Cdk Substrates

<a id='a45bf651-e69a-423b-b9cc-5188e9904b80'></a>

Claude Gérard,† John J. Tyson,‡ and Béla Novák†*
†Oxford Centre for Integrative Systems Biology, Department of Biochemistry, University of Oxford, Oxford, United Kingdom; and ‡Department of
Biological Sciences, Virginia Polytechnic Institute and State University, Blacksburg, Virginia

<a id='a9a0406b-191c-4679-9e43-fdb4cac16e1c'></a>

ABSTRACT The eukaryotic cell cycle is characterized by alternating oscillations in the activities of cyclin-dependent kinase (Cdk) and the anaphase-promoting complex (APC). Successful completion of the cell cycle is dependent on the precise, temporally ordered appearance of these activities. A modest level of Cdk activity is sufficient to initiate DNA replication, but mitosis and APC activation require an elevated Cdk activity. In present-day eukaryotes, this temporal order is provided by a complex network of regulatory proteins that control both Cdk and APC activities via sharp thresholds, bistability, and time delays. Using simple computational models, we show here that these dynamical features of cell-cycle organization could emerge in a control system driven by a single Cdk/cyclin complex and APC wired in a negative-feedback loop. We show that ordered phosphorylation of cellular proteins could be explained by multisite phosphorylation/dephosphorylation and competition of substrates for interconverting kinase (Cdk) and phosphatase. In addition, the competition of APC substrates for ubiquitylation can create and maintain sustained oscillations in cyclin levels. We propose a sequence of models that gets closer and closer to a realistic model of cell-cycle control in yeast. Since these models lack the elaborate control mechanisms characteristic of modern eukaryotes, they suggest that bistability and time delay may have characterized eukaryotic cell divisions before the current cell-cycle control network evolved in all its complexity.

<a id='e9c7aaed-7869-4874-95ba-510f40d199dc'></a>

# INTRODUCTION

Progression through the eukaryotic cell cycle is a classic example of temporal and spatial organization in the per-petuation of life. In one stage of the cell cycle, called the S phase, the cell replicates its genetic material and packs the two identical sister chromatids into chromosomes. At a later stage, these replicated sister chromatids are segre-gated to opposite poles of the predivisional cell, in a spatially organized process called mitosis. A new round of DNA replication should only take place in the next cycle, after completion of the previous mitosis (M phase). Strict alterna-tion of S and M phases is essential for successful cell prolif-eration; therefore, the molecular mechanisms responsible for temporal ordering of these two events are fundamental for all eukaryotic life.

<a id='fa2fea25-1364-4836-b001-3dcf71183b9d'></a>

Both S and M phases are triggered by the phosphorylation
of cellular proteins required for DNA replication and
mitosis by cyclin-dependent kinases (Cdks). A Cdk is active
as a protein kinase only in complex with a regulatory
subunit, called cyclin. In present-day eukaryotes, different
Cdk/cyclin complexes are responsible for initiation of the
S and M phases, which suggests a qualitative model of
cell-cycle control. According to the qualitative model, the
temporal order of the S and M phases is a consequence of
alternating oscillations of at least two Cdk/cyclin complexes
with different substrate specificities. This might be true, but
it is difficult to reconcile with the fact that a single Cdk/

<a id='83f28df7-d986-498f-9da1-5e507bda9c35'></a>

Submitted November 9, 2012, and accepted for publication February 12,
2013.

<a id='994241eb-7d85-4c9c-ab58-3167306b44d7'></a>

*Correspondence: bela.novak@bioch.ox.ac.uk
Editor: Dennis Bray.

© 2013 by the Biophysical Society
0006-3495/13/03/1367/13 $2.00

<a id='117995da-9685-4dd1-a15b-c14d3c9322d6'></a>

cyclin complex (Cdk/cyclin-B) can provide perfect temporal order in the eukaryotic cell cycle (1–3). This observation led to the proposal of a quantitative model of cell-cycle control according to which the oscillation of a single Cdk activity between low and high values is the only fundamental requirement for ordered cell-cycle progression provided that small Cdk activity is sufficient to trigger DNA replication but higher activity is required to bring about the M phase (1–5). Since phosphorylation of S- and M-phase substrates is a reversible process counter- acted by protein phosphatases (PPases), there are two (possibly overlapping) explanations for the quantitative model: S-phase substrates may have higher affinities for Cdk than do M-phase substrates, or they may be less suscep- tible to counteracting PPase activities. The presence of large amounts of S and M substrates of the interconverting enzymes (Cdk and PPase) could create a competition among the substrates, and this competition for Cdk and PPase could be the underlying mechanism responsible for temporal ordering of the S and M phases (in the quantitative model). This competition is further amplified by the fact that several Cdk target proteins are phosphorylated on more than one site (multisite phosphorylation) (6,7). Hence, the several hundred Cdk targets with multiple phosphorylation sites can easily account for an overall concentration of Cdk phos- phosites in the millimolar range (6).

<a id='a02c7e3a-b8eb-4acf-9f55-8c7bf434b18a'></a>

Although Cdk activity is dominant from the start of DNA
replication until the meta/anaphase transition of mitosis,
the ubiquitin-ligase activity of the anaphase-promoting
complex (APC) is dominant for the rest of the cell cycle
(from mitosis through G1 until the next S phase). The

<a id='aad07705-34f9-4ff3-bff5-1e5105455fe1'></a>

<::A logo with a red bookmark icon inside a blue-ringed circle, next to the text "CrossMark".
: figure::>

<a id='15c5c439-e736-4010-96fd-5bd371d9383a'></a>

http://dx.doi.org/10.1016/j.bpj.2013.02.012

<!-- PAGE BREAK -->

<a id='cbf11171-54a1-4e55-b3d6-0c2148c8de8c'></a>

1368

<a id='a8158941-120e-4347-a92a-69cea0625154'></a>

Gérard et al.

<a id='069d5ac1-fcca-486c-bfc9-6ca21e115422'></a>

APC is a molecular machine that drives chromosome segre-gation and exit from mitosis by targeting securin and mitotic cyclins for degradation (8). Similar to Cdks, the APC also modifies many cellular proteins and targets them for proteasome-dependent degradation. In addition, ubiquitylation by the APC is also a multistep process, because the substrates must be polyubiquitylated (in more than four places) to be recognized by the proteasome. Therefore, competition for substrates can also signifi-cantly influence the dynamics of APC-dependent protein degradation (9).

<a id='28952d61-31db-48e9-8109-abe39ef4d8f2'></a>

In this work, we explore the role of substrate competition with respect to these two fundamental cell-cycle regulators, Cdk and APC. We ask the question, what are the emergent properties of a dynamical network when the substrates of Cdk and APC compete with each other? Our work is strongly influenced by theoretical work on substrate com- petition in specific signal-transduction pathways (10) and in more general settings (11,12).

<a id='c847059f-e67b-4f69-aed9-563fa777c356'></a>

## RESULTS
### Competition between two groups of substrates for Cdk and its counteracting PPase

*Case 1: singly phosphorylated substrates*

We categorize the numerous substrates of Cdk and its counteracting PPase into two groups, S substrates and M substrates, and we assume that with respect to their inter- converting enzymes, substrates in one group have similar kinetic properties, which are different from the properties of the other group. S represents substrates that must be phosphorylated (or dephosphorylated) for S-phase progres- sion, whereas M indicates the group of substrates whose phosphorylation state is crucial for progression through mitosis (Fig. 1). Our grouping is independent of whether phosphorylation activates or inhibits the substrates. For example, we imagine that both DNA-replication licensing factors (e.g., Cdc18 and Cdt1), which are inhibited by Cdk phosphorylation, and replication initiator proteins (e.g., Sld1), which are activated, belong to the S group of substrates. Initially, we consider the case where both pools of substrates are singly phosphorylated and dephos- phorylated by Cdk and PPase, according to Michaelis- Menten kinetics. The unphosphorylated forms (S and M) and the phosphorylated forms (S<sub>p</sub> and M<sub>p</sub>) mutually inhibit each other's interconversion in a competitive manner (Fig. 1).

<a id='7539a966-7e44-4b38-bdf4-2f39be51269e'></a>

Note that the letters S and M refer to several different
ideas, depending on context. The S phase and M phase
are temporally separate phases of the cell cycle, in which
DNA is synthesized and mitotic division is carried out,
respectively. S substrates and M substrates refer to proteins
that are phosphorylated and/or dephosphorylated during the
S phase and M phase of the cell cycle. The letters S and M

<a id='0fa48f6a-2a38-4279-bdab-159055646e37'></a>

<::figure: FIGURE 1 Scheme of a minimal model for the ordered progression of DNA replication and mitosis. (A) Model containing two groups of substrates (S and M) that can each be phosphorylated once by a Cdk/cyclin complex. Phosphorylation of S promotes progression into DNA replication, whereas phosphorylation of M brings about the entry into mitosis. The dynamics of the model is based on substrate competition between S and M for phosphorylation by Cdk and between S_p and M_p for dephosphorylation by PPase. In this version of the model, as well as in all models of this study, the kinetics of phosphorylation/dephosphorylation are described by a Goldbeter-Koshland switch (13). (B and C) Bifurcation diagrams of the phosphorylated substrates for DNA replication, S_p (B), and mitosis, M_p (C), as functions of Cdk activity. In both cases, low Cdk activity results in low levels of S_p and M_p (the G1 state), whereas high Cdk activity promotes full phosphorylation of S and M (the S/G2/M state). For intermediate Cdk activity, the model exhibits bistability in the phosphorylation of S and M. As Cdk activity rises from 0.1 to 0.25 along the lower branch of the bistable switch, the S substrates become significantly phosphorylated (B), whereas the M substrates remain unphosphorylated (C), which suggests that cells enter the S phase (DNA synthesis) before they commit to mitosis. However, as soon as Cdk activity exceeds ~0.26, M substrates are abruptly phosphorylated and the cell enters mitosis. Parameter values for the simulations are given in Section 1 of Supplement 1 in the Supporting Material.

(A) Diagram showing a regulatory network. Components are S, S_p, M, M_p, and Cdk. Double-headed arrows indicate interconversion between S and S_p, and between M and M_p. Blue arrows from Cdk point to the S to S_p conversion and the M to M_p conversion, indicating Cdk promotes phosphorylation. Red blunt-ended lines indicate inhibition. S_p inhibits Cdk. M_p inhibits Cdk. S inhibits M. M inhibits S. There are also red blunt-ended lines from S_p pointing to S and from M_p pointing to M, suggesting dephosphorylation or negative regulation of the phosphorylated state.

(B) Bifurcation diagram. The x-axis is 'Cdk' ranging from 0.1 to 0.4. The y-axis is 'Phosphorylated substrates for DNA replication, S_p' ranging from 0 to 1. The plot shows a curve that starts near S_p=0 for low Cdk values (around 0.1). As Cdk increases, S_p remains near 0 until approximately Cdk=0.22, where it sharply transitions to S_p=1. There is a bistable region indicated by a solid line for the lower stable branch, a dashed red line for the unstable branch, and a solid line for the upper stable branch. The lower branch goes from (0.1, 0) to (approximately 0.22, 0) then rises sharply. The unstable branch (dashed red) goes from (approximately 0.22, 0) to (approximately 0.24, 1). The upper branch starts at (approximately 0.24, 1) and stays at S_p=1 as Cdk increases to 0.4.

(C) Bifurcation diagram. The x-axis is 'Cdk' ranging from 0.1 to 0.4. The y-axis is 'Phosphorylated substrates for mitosis, M_p' ranging from 0 to 1. The plot shows a curve that starts near M_p=0 for low Cdk values (around 0.1). As Cdk increases, M_p remains near 0 until approximately Cdk=0.26, where it sharply transitions to M_p=1. Similar to (B), there is a bistable region with a solid line for the lower stable branch, a dashed red line for the unstable branch, and a solid line for the upper stable branch. The lower branch goes from (0.1, 0) to (approximately 0.26, 0) then rises sharply. The unstable branch (dashed red) goes from (approximately 0.24, 0) to (approximately 0.26, 1). The upper branch starts at (approximately 0.26, 1) and stays at M_p=1 as Cdk increases to 0.4.::>

<a id='6138192e-b7cc-4488-bf79-5e188b272e24'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='3579c2e5-512b-432a-8018-f030c3913799'></a>

Cell-Cycle Order by Substrate Competition

<a id='7689b07d-461a-42c1-b19a-354f3494e9c1'></a>

1369

<a id='7059f4da-8eaa-4048-b3d3-ce65eed34873'></a>

(S_P and M_P) are the names of generic representatives of S substrates and M substrates (or their phosphorylated forms). In equations, *S* and *M* (S_P and M_P) represent the concentrations (real numbers) of these proteins.

<a id='c0034aa8-9705-44df-8be1-fb027b4c9326'></a>

The kinetic equations describing the time evolution of the concentrations of the phosphorylated forms of S and M are given by

<a id='934383ae-0695-41ef-95a3-c934bd7ca531'></a>

dSp/dt = k1S × Cdk × S / (K1S [1 + (M / K1M)] + S) - V2S × Sp / (K2S [1 + (Mp / K2M)] + Sp) (1)

<a id='8636cdb8-e518-4759-a8f7-0c83761d1f7e'></a>

dMₚ / dt = k₁M × Cdk × M / (K₁M [1 + (S / K₁S)]) + M - V₂M

× Mₚ / (K₂M [1 + (Sₚ / K₂S)]) + Mₚ (2)

where S = Sₜ - Sₚ, M = Mₜ - Mₚ, and Sₜ and Mₜ are constants (total concentrations of S and M substrates). In these equations, Cdk is the activity of Cdk/cyclin complex.

<a id='afdb9895-97a3-4940-ae0b-9cefcdf29e76'></a>

The definitions of the kinetic parameters used in our calculations, together with their numerical values, are listed in Supplement 1 of the Supporting Material. Since we consider the PPase activity to be constant, we have included it in the corresponding rate constants as maximal rates (_V_). We scale the concentrations of both substrates (_S_ and _M_) and their Michaelis constants to the total concentration of phosphoacceptor sites in the cell (substrate concentration multiplied by the average number of phosphorylation sites/substrate). Therefore, our total substrate concentrations (_S_T and _M_T) are equal to 1, whereas the Michaelis constants are <<1. Because the Michaelis constants are all <<1, the phosphorylation and dephosphorylation reactions in our models behave as Goldbeter-Koshland switches (13). As a consequence, the extent of phosphorylation of _S_ and _M_ substrates is an ultrasensitive function of the ratio of activities of Cdk and PPase. In all the models proposed here, the phosphatase activity is considered to be constant. Thus, the extent of phosphorylation of _S_ and _M_ substrates is only a function of Cdk activity. We assume a constant activity of the phosphatase for the sake of simplicity, to keep the models as minimal as possible. However, it is known that phosphatase activities are regulated in present-day eukaryotic cell cycles. For example, the activity of PP2A-B55 plays a key role in the Greatwall pathway regulating mitosis in higher eukaryotes (14,15), and the activity of Cdc14 phosphatase is critical for mitotic exit in budding yeast (16).

<a id='25fef09e-368c-43d4-a23f-5710879fda2f'></a>

We find that competitive inhibitions among substrates of two Goldbeter-Koshland switches create a bistable response in terms of substrate phosphorylations (Fig. 1). We illustrate the bistable behavior on one-parameter bifurcation diagrams for both S_p (Fig. 1 B) and M_p (Fig. 1 C) as functions of Cdk (the bifurcation parameter). Both Cdk substrates stay unphosphorylated at small values of Cdk, whereas both of them get fully phosphorylated at high values. However, the phosphorylation threshold is much sharper for M substrates than for S substrates. Both types of substrate get dephosphorylated below a certain Cdk activity threshold, which is smaller than the phosphorylation threshold. Observe that the dephosphorylation threshold is sharper for S substrates than for M substrates. Between the two thresholds, both low- and high-phosphorylation steady states coexist and the system is said to be bistable. The difference in the sharpness of the two thresholds influences the dynamics of phosphorylation and dephosphorylation of the two types of substrate. Indeed, when Cdk activity rises, S substrates get phosphorylated earlier than M substrates, whereas when Cdk activity falls, the opposite is true.

<a id='120ea64c-3032-4a5b-b60d-90fbd794db58'></a>

Using a model for the double phosphorylations of MAP
kinases, Kholodenko and colleagues predicted a similar
bistable response (10,17). The difference between our
model and that of Kholodenko is that we consider two
different substrates phosphorylated at one site each, whereas
they studied double phosphorylation of a single substrate
(MAP kinases).

<a id='64cfd3dd-3b15-4b3c-8ea4-286d1942fa70'></a>

In summary, two groups of competitive monophosphorylated Cdk substrates can create a bistable switch with coexisting barely and fully phosphorylated states, but the fully phosphorylated states of S and M substrates are mostly overlapping, as functions of Cdk activity.

<a id='2de17ad6-d2a4-4839-8485-f842bf1dca50'></a>

The minimal model proposed in Fig. 1 might be suffi-
cient to explain the ordered progression of the S and M
phases, if phosphorylation of only a fraction of S sub-
strates is sufficient to trigger DNA replication, whereas
most M-phase substrates must be phosphorylated to enter
mitosis. However, in the next section, we will see that,
under more realistic assumptions, it is possible to achieve
more robust, ordered progression from DNA replication
to mitosis.

<a id='af32f394-084c-4083-8249-e9383bfbc16a'></a>

Case 2: doubly phosphorylated substrates
Allowing for double phosphorylation of S and M substrates, we construct a network (Fig. 2) of coupled Kholodenko-type bistable switches. Unphosphorylated and monophosphorylated substrates are competing for phosphorylation by the kinase Cdk, whereas the monophosphorylated and doubly phosphorylated substrates are competing for dephosphorylation by the counteracting PPase.

<a id='f47ddaf4-89c9-4349-a1fb-ea2acf0baf19'></a>

The kinetic equations describing the time evolution of the
unphosphorylated forms of S and M, and the doubly phos-
phorylated forms (Spp and Mpp) are given by Eqs. 3–6.

<a id='fffa2e44-7aef-448e-a325-4f3ddd70c6b5'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='a729f6e5-7984-40a3-ba3f-9f9d9ab940b5'></a>

1370

<a id='dce59c8d-79d6-4362-a7d2-fb737bda907e'></a>

Gérard et al.

<a id='127f8a4b-c6bf-4462-86bd-0beaae9e069f'></a>

<::Figure 2: A model for the ordered progression of DNA replication and mitosis based on double phosphorylation of S and M substrates.::>
<::chart
: **A** Diagram showing the phosphorylation and dephosphorylation of S and M substrates. Cdk (kinase) promotes phosphorylation (blue arrows). PPase (phosphatase) promotes dephosphorylation (red arrows with blunt ends indicating inhibition). The states are S, S_p, S_pp for DNA replication substrates and M, M_p, M_pp for mitosis substrates. Arrows indicate transitions between states (e.g., S <-> S_p <-> S_pp, and M <-> M_p <-> M_pp).
  - Phosphorylation: Cdk activates S to S_p, S_p to S_pp, M to M_p, M_p to M_pp.
  - Dephosphorylation (inhibited by indicated species):
    - S_p to S inhibited by S_pp, M_p, M_pp.
    - S_pp to S_p inhibited by S, M, M_p.
    - M_p to M inhibited by S, S_p, M.
    - M_pp to M_p inhibited by S_p, S_pp.
: **B** Bifurcation diagram for DNA replication substrates. X-axis: Cdk activity (0 to 0.4). Y-axis: Substrates for DNA replication phosphorylated twice S_pp (0 to 1). The graph shows a curve with a bistable region. A stable branch goes from S_pp=0 at Cdk=0, increases slightly, then jumps to S_pp=1 around Cdk=0.06 (point P1 to D2). A dashed red line indicates an unstable branch between P1 and D2.
: **C** Bifurcation diagram for mitosis substrates. X-axis: Cdk activity (0 to 0.4). Y-axis: Substrates for mitosis phosphorylated twice M_pp (0 to 1). The graph shows a curve with a bistable region. A stable branch goes from M_pp=0 at Cdk=0, increases slightly, then jumps to M_pp=1 around Cdk=0.24 (point P2 to D1). A dashed red line indicates an unstable branch between P2 and D1.::>
FIGURE 2 A model for the ordered progression of DNA replication and mitosis based on double phosphorylation of S and M substrates. (A) A kinase, Cdk, can phosphorylate twice the substrates required for DNA replication, S, and mitosis, M. The unphosphorylated (S and M) or mono-phosphorylated (S_p and M_p) substrates compete for phosphorylation by the kinase, while the monophosphorylated and twice-phosphorylated (S_pp and M_pp) substrates compete for dephosphorylation by the counter-acting PPase. (B and C) Bifurcation diagrams of S_pp and M_pp as functions of Cdk activity. As Cdk activity increases from 0, the system passes through two domains of bistability. At the edge of the first domain (Cdk ≈ 0.06), the S substrates become fully phosphorylated and the cell commences DNA replication. Only later, when Cdk activity increases beyond the edge of the second bistability domain (Cdk ≈ 0.24) do the M substrates become fully phosphorylated, at which point the cell enters mitosis. Parameter values for these simulations are given in Section 2 of Supplement 1 in the Supporting Material

<a id='8ef755dd-6714-46fa-a1d7-06c49ee8b6ad'></a>

$$\frac{dS}{dt} = V_{2S} \times \frac{S_P}{K_{2S} \left[1 + \left(\frac{S_{PP}}{K_{4S}}\right) + \left(\frac{M_P}{K_{2M}}\right) + \left(\frac{M_{PP}}{K_{4M}}\right)\right] + S_P} - k_{1S} \times Cdk \times \frac{S}{K_{1S} \left[1 + \left(\frac{S_P}{K_{3S}}\right) + \left(\frac{M}{K_{1M}}\right) + \left(\frac{M_P}{K_{3M}}\right)\right] + S} \quad (3)$$

<a id='189ed642-29fc-469a-932b-4c1b9d900348'></a>

dSPP / dt = k3S × Cdk

× SP / (K3S [1 + (S / K1S) + (M / K1M) + (MP / K3M)] + SP) - V4S

× SPP / (K4S [1 + (SP / K2S) + (MP / K2M) + (MPP / K4M)] + SPP)

(4)

<a id='ef9d87d6-4e12-494d-8822-92441eeb74bb'></a>

$$\frac{dM}{dt} = V_{2M} \times \frac{M_P}{K_{2M}\left[1 + \left(\frac{M_{PP}}{K_{4M}}\right) + \left(\frac{S_P}{K_{2S}}\right) + \left(\frac{S_{PP}}{K_{4S}}\right)\right] + M_P} - k_{1M} \times Cdk \times \frac{M}{K_{1M}\left[1 + \left(\frac{M_P}{K_{3M}}\right) + \left(\frac{S}{K_{1S}}\right) + \left(\frac{S_P}{K_{3S}}\right)\right] + M} \quad (5)$$

<a id='3d00afe1-22ab-4cb5-9623-ea6c781106b9'></a>

dM_PP / dt = k_3M × Cdk

× M_P / (K_3M [1 + (M / K_1M) + (S / K_1S) + (S_P / K_3S)] + M_P) - V_4M

× M_PP / (K_4M [1 + (M_P / K_2M) + (S_P / K_2S) + (S_PP / K_4S)] + M_PP)

(6)

The monophosphorylated forms are calculated from the conservation equations

<a id='b5d846d5-0d8d-4696-af1f-e187c3d48652'></a>

Sp = ST - S - Spp and Mp = MT - M - Mpp.

<a id='8f2f35c5-718c-45e5-bd99-a2e690106678'></a>

Supplement 1 of the Supporting Material provides the numerical values of the kinetic parameters used in our calculations. As before, the steady-state responses of Spp and Mpp are illustrated on bifurcation diagrams (Fig. 2, B and C), using Cdk as the bifurcation parameter (assuming constant activity of PPase). Competition between the two substrates for Cdk and PPase creates bistability, as in the monophosphorylated case. However, in this case, the thresholds for phosphorylation and dephosphorylation of S and M substrates are different, which creates two domains

<a id='e87d5ca1-e971-42f6-96f2-52043fb2e7a5'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='64c24cf4-1fc3-4453-8c93-5ee25283858f'></a>

Cell-Cycle Order by Substrate Competition

<a id='91ba579f-8d09-46b8-9572-febb4e943b19'></a>

1371

<a id='3e607fa5-cd51-4182-8b53-40a86b1259e3'></a>

of bistability with four saddle-node bifurcation points (P1, P2, D1, and D2). Therefore, when Cdk activity is rising, the DNA replication substrates (S) get doubly phos- phorylated above P1, whereas the mitotic substrates stay unphosphorylated. Double phosphorylation of M substrates requires Cdk activity to pass a higher threshold (P2). This difference in the phosphorylation thresholds could explain why cells initiate DNA replication earlier than they enter into mitosis.

<a id='e2f630da-fec1-4b9c-9e75-a5b06f7f7ea7'></a>

In Fig. 3, we show that whereas the singly-
phosphorylated-substrates model (Fig. 1 A) exhibits a single
domain of bistability (see Supplement 2 of the Supporting
Material: Domain of bistability for the singly phos-
phorylated substrates model), the doubly-phosphorylated-
substrates model (Fig. 2 A) exhibits two domains of
bistability. The single domain of bistability in Fig. 3 A
separates a region where the substrates for DNA replica-

<a id='68526d7c-654f-4a57-b317-4dde2214207f'></a>

A Singly phosphorylated substrates <::chart: A log-log plot showing k1M on the y-axis (ranging from 0.001 to 100) versus Cdk on the x-axis (ranging from 0.001 to 10). A closed, roughly elliptical region is shown in the center of the plot, labeled "Bistability" with an arrow pointing to it. To the left of this region, the text "Low levels of Sp & Mp" is displayed. To the right of this region, the text "High levels of Sp & Mp" is displayed.::>

<a id='96d7eb4a-6e21-4def-9598-c81cc65ea29a'></a>

B Doubly phosphorylated substrates<::Two-parameter bifurcation diagram: chart. The chart shows k1M on the y-axis (log scale, from 0.001 to 100) versus Cdk on the x-axis (log scale, from 0.001 to 10). The diagram is divided into several regions by curved lines:
- Top-left region is labeled "Bistability".
- Mid-left region is labeled "Low Spp & Mpp".
- Bottom-right region is labeled "High Spp & low Mpp".
- Mid-right region is labeled "Bistability".
- Top-right region is labeled "High Spp & Mpp".
This diagram corresponds to the model with doubly phosphorylated substrates, which has two domains of bistability. Regions where the steady-state levels of phosphorylated substrates (Spp and Mpp) are high or low are indicated.: chart::>
FIGURE 3 Two-parameter bifurcation diagrams (k1M versus Cdk) for the models in Figs. 1 and 2. (A) The model with singly phosphorylated substrates has a single domain of bistability. (B) The model with doubly phosphorylated substrates has two domains of bistability. Regions where the steady-state levels of phosphorylated substrates (Sp and Mp in A and Spp and Mpp in B) are high or low are indicated. Other parameter values used in these calculations are given in Supplement 1 of the Supporting Material.

<a id='ebe2eaa6-709f-47db-b934-3469fbf0427b'></a>

tion and mitosis are mainly unphosphorylated (for low Cdk activity) from a region where they are mainly phosphorylated (for high Cdk activity). The two domains of bistability in Fig. 3 B provide a more robust separation of the phosphorylation of S-phase substrates from M-phase substrates. Starting from a low level of Cdk, the first domain of bistability delimits a region of low Spp from a region of high Spp, whereas M stays mainly in an unphosphorylated state. The second domain of bistability separates regions of low and high Mpp. By allowing a separation in the thresholds for S and M phosphorylation, the two steps of substrate phosphorylation and dephosphorylation improve the separation between the phases of DNA replication and mitosis. Moreover, the model shows that the bistability domains are enlarged, with two steps of phosphorylation and dephosphorylation of S and M substrates as compared to a single step (compare Fig. 3, A and B).

<a id='1586c0e6-e1ef-4f48-802c-84b2b55150a3'></a>

Returning to Fig. 2, B and C, we observe that when Cdk
activity is dropping, the two groups of substrates get
dephosphorylated at different Cdk activities: M substrates
get dephosphorylated first (below D1), whereas Spp disap-
pears later (below D2). Because replication licensing factors
belong to the S-group of substrates, this temporal difference
in dephosphorylation can explain why cells license replica-
tion origins only after they exit from mitosis. Indeed, the
relicensing of replication origins only after Cdk activity
drops below a low threshold is critical for the subsequent
rise in activity to trigger S-phase onset and hence for the
proper alternation of the S and M phases.

<a id='c25a6951-a805-49f1-aae5-bbf6049ee68f'></a>

This temporal ordering of phosphorylation and dephos-
phorylation of S and M substrates requires an oscillation
of Cdk activity, which we discuss in the next section.

<a id='e176be0d-3797-4110-b6b9-0bd172ee57f0'></a>

## Competition between APC substrates can create an important time delay

_Case 1: competition-dependent oscillations_

APC gets activated during mitosis, because it is one of the M-phase substrates of Cdk (18). Active APC polyubiquity-lates many proteins, which targets them to proteasome-dependent degradation and thereby drives the cell out of mitosis. However, successful exit from mitosis requires the degradation of only two proteins in budding yeast cells (19) and fruit fly cells (20). One of these proteins is cyclin B (CycB), which is required for Cdk activity in mitosis. CycB degradation destabilizes the mitotic state by inacti-vating Cdk, which results in APC inactivation as well. The other protein is securin, an inhibitor of anaphase sepa-ration of sister chromatids. Securin degradation releases separase, a protease that cleaves a component of the cohesin complex that holds together the sister-chromatid pairs. In this section, we develop a model assuming that securin and CycB competitively inhibit each other for

<a id='dadff9fe-ab54-48fe-8fdc-f2a24e9ea6ab'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='f728dbd7-a28f-45c9-8c3e-91f22095f8cd'></a>

1372

<a id='6ad9a1f7-e51c-4a23-9f11-9fad00ff0dce'></a>

Gérard et al.

<a id='8eed35b8-94ae-4daa-a066-ec984db66e7c'></a>

A <::diagram: A regulatory network diagram showing the interactions between several components. An incoming arrow points to "Cdk/cyclin". "Cdk/cyclin" has a blue downward arrow pointing to "APCp". "APCp" has a double-headed arrow connecting it to "APC". "APCp" has a blue downward arrow pointing to an unlabelled line, which then has a red bar indicating inhibition pointing to "Cyclin". "Cdk/cyclin" has a red bar indicating inhibition pointing to "Securin". An incoming arrow points to "Securin". "Securin" has a red bar indicating inhibition pointing to "Cyclin".::> B <::chart: A line graph titled "Cdk/cyclin, securin, Mp (APCP)" showing the concentration of different components over time. The x-axis is "Time" ranging from 60 to 120. The y-axis is "Cdk/cyclin, securin, Mp (APCP)" ranging from 0 to 1. Three oscillating lines are plotted: a black line labeled "Cdk", a red line labeled "APCP", and a green line labeled "Securin". All three lines show periodic fluctuations, with Cdk and APCP being largely in phase, and Securin lagging.::> C <::chart: A line graph titled "Cdk/cyclin" showing a phase portrait. The x-axis is "Mp (APCP)" ranging from 0 to 1. The y-axis is "Cdk/cyclin" ranging from 0 to 1.5. Two main closed curves are shown: a black one and a blue one. The blue curve has an arrow indicating a counter-clockwise direction of progression.::> D <::chart: A line graph titled "Mp (APCP)" showing a bifurcation diagram. The x-axis is "Rate of synthesis of Cdk/cyclin, Vscdk" on a logarithmic scale from 0.001 to 0.1. The y-axis is "Mp (APCP)" ranging from 0 to 1. The graph displays a hysteresis loop, with stable steady states (black lines) at low and high Vscdk values, and an oscillatory region (blue and dashed red lines) in between. The dashed red line represents unstable steady states.::> E <::chart: A line graph titled "Cdk/cyclin, Securin" showing the relationship between Cdk/cyclin, Securin, and Mp (APCP). The x-axis is "Mp (APCP)" ranging from 0 to 0.8. The y-axis is "Cdk/cyclin, Securin" ranging from 0 to 10. Two lines are plotted: a black line labeled "Cdk" and a red line labeled "Securin". Both Cdk and Securin concentrations decrease as Mp (APCP) increases, with a sharp drop around Mp (APCP) = 0.4.::>

<a id='0b158e51-993b-43da-b1e6-0f2ae95232b8'></a>

FIGURE 4 A minimal, embryonic-type cell-
cycle oscillator. (A) Scheme of a three-variable
oscillator based on negative feedback between
Cdk/cyclin and APC. Cdk ensures the phosphoryla-
tion of APC, which then promotes the degradation
of Cdk/cyclin. A time delay is introduced by
competitive inhibition between Cdk/cyclin and
securin for polyubiquitylation by APC. (B) Time
course of sustained oscillations of Cdk/cyclin,
securin, and the phosphorylated form of APC. (C)
The limit cycle (closed curve) is projected onto
the Cdk/cyclin versus APCp plane. The arrow indi-
cates the direction of motion along the limit cycle.
Black curves are the Cdk/cyclin and APCp null-
clines. (D) Bifurcation diagram. APCp as a function
of the rate of synthesis of Cdk/cyclin, Vscdk. Solid
curves indicate stable steady states (for low and
high values of Vscdk) and stable limit cycles (for
intermediate values of Vsedk); dashed curves indi-
cate unstable steady states and unstable oscilla-
tions. (E) Cdk/cyclin and securin nullclines when
APCP is considered as a parameter. Parameter
values for the simulations are given in Section 3
of Supplement 1 in the Supporting Material.

<a id='684b89b0-8f48-4744-b3ca-de9bcdb0a2ce'></a>

APC-dependent degradation (Fig. 4 A). That securin and
CycB compete with each other for APC-dependent ubiqui-
tylation has been demonstrated experimentally in mouse
oocytes (21).

<a id='9efeccf1-2c3f-4154-a6eb-c003aa8f278b'></a>

The kinetic equations describing the time evolution of the Cdk/CycB complex (*Cdk*), of the phosphorylated form of APC (*APC*<sub>P</sub>), and of securin (*Sec*) are given by Eqs. 7 to 9:

<a id='68034e08-ee53-45ac-be44-66f882b55590'></a>

<::dCdk / dt = Vscdk - k_d1cdk × Cdk - k_dcdk × APC_P × (Cdk / (K_dcdk [1 + (Sec / K_dsec)] + Cdk)) (7): figure::>

<a id='a1295081-46b8-4c19-b3b5-4f6b8cfff7d0'></a>

$$\frac{dAPC_P}{dt} = k_{2APC} \times Cdk \times \frac{APC}{K_{2APC} + APC} - V_{1APC} \times \frac{APC_P}{K_{1APC} + APC_P} \quad (8)$$

<a id='d112c1e0-5d6f-453d-a0a0-aff4351bfe34'></a>

dSec/dt = Vsec - kdlsec × Sec - kdsec × APCP × (Sec / (Kdsec[1 + (Cdk/Kdcdk)] + Sec)) , (9)

<a id='8663c212-5d10-4e3e-bae1-7e460a921722'></a>

with the conservation equation

<a id='d7f2f797-bd3b-43dc-95f7-129bfecacba6'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='93939850-53d4-4940-b392-b675ea3f3e2d'></a>

Cell-Cycle Order by Substrate Competition

<a id='d5c42e95-3238-481b-9c66-d1b2f1797043'></a>

1373

<a id='f0459059-0dc0-46ef-9e93-0b53ac2882ce'></a>

APC = APC_T - APC_P.

<a id='a2c305d4-cecf-426b-8879-a9649b3c9cd8'></a>

Supplement 1 in the Supporting Material shows the list of parameters together with their numerical values used in our simulations in Fig. 4. Since (we assume) securin is a better APC substrate than CycB, securin delays CycB degradation (Fig. 4 B), which creates a time delay in the negative-feedback loop between Cdk/CycB and the APC. This time-delayed negative-feedback loop generates oscillations in CycB and securin levels and in APC activity (Fig. 4 B). In the absence of securin the two-component negative-feedback loop cannot show sustained oscillations (not shown).

<a id='7174bc04-1054-4bc7-906d-1fcaa98fa217'></a>

A projection of the limit cycle on the Cdk-versus-APC<sub>P</sub>
phase plane is illustrated in Fig. 4 C. The APC<sub>P</sub> nullcline is
sigmoidal, because the APC is regulated by a Goldbeter-
Koshland switch. A threshold characterizes the Cdk
nullcline, because securin is the preferential APC substrate
(Fig. 4 E). Indeed, securin is degraded more rapidly
than Cdk when the level of APC<sub>P</sub> increases. Sustained oscil-
latory behavior, corresponding to cell-cycle progression,
appears only in a certain range of CycB synthesis rate (V<sub>scdk</sub>),
as illustrated by the one-parameter bifurcation diagram in
Fig. 4 D. A similar dynamical behavior is observed with
the rate of synthesis of securin, V<sub>ssec</sub> (not shown). The
fact that the model oscillates only in a particular window
of V<sub>scdk</sub> or V<sub>ssec</sub> values suggests that appropriate levels of
Cdk/cyclin and securin are needed to ensure that the time
delay in the negative-feedback loop is consistent with sus-
tained oscillations.

<a id='357cd4c5-b2ee-4636-956d-bbdc2253b8bd'></a>

Case 2: competition-independent oscillations

So far, we have a minimal cell-cycle oscillator, based
on competitive inhibition between CycB and securin for
APC-dependent degradation. Next, we extend the minimal
model by including double phosphorylation of APC. In
this case, there is competitive inhibition between the
different phosphoforms of APC for phosphorylation by
Cdk/cyclin and dephosphorylation by PPase (Fig. 5 A).
This extended model also exhibits sustained oscillations
(Fig. 5 B). In the extended model, securin degradation is
no longer necessary for sustained oscillation (Fig. 5 C),
because APC behaves as a bistable switch in response to
changing Cdk activity (Fig. 5, D and E). Indeed, bistability
generates a hysteretic response, which creates a time delay
in the dynamic network that can compensate for the absence
of securin (22). Superimposed on the bistable switch are
the limit-cycle oscillations (closed curves) of the model in
the presence (Fig. 5 D) or absence (Fig. 5 E) of securin.
We observe that the limit cycle surrounds completely
the bistable switch in the presence of securin, whereas it
does not reach the upper branch of the bistable switch
in the absence of securin. The fact that securin is not
needed for sustained oscillations and repetitive cycling is
in agreement with experimental observations that securin

<a id='5f188c92-c366-432e-a924-e8d2b7412f75'></a>

is not necessary for cell-cycle progression in yeasts (23)
or mammalian cells (24).

<a id='5db88b93-8140-44b0-8ae5-ff84bdcf96b5'></a>

The role of securin in the dynamics of the negative-
feedback oscillator model with double phosphorylation of
APC is illustrated in one-parameter bifurcation diagrams
(Fig. 5, F and G). Although securin is not needed for the
limit-cycle oscillations, securin increases the amplitude of
oscillations because it extends the time delay. To our
knowledge, there is no experimental evidence that securin
influences the amplitude of CycB oscillations.

<a id='9da2b277-c85d-4190-9879-dfce109474d1'></a>

In conclusion, a minimal model of cell-cycle regulation, based on the Cdk-APC negative-feedback loop, can exhibit sustained oscillations due to time delays that come from three different sources:
1. competitive inhibition between securin and cyclin for APC-dependent degradation;
2. a bistable switch in the phosphorylation state of APC;
3. inhibitory phosphorylation of Cdk/CycB complexes, a mechanism that is not discussed here, but see Novak and Tyson (25).

<a id='db755bad-ebcb-4559-a83f-b8806d488715'></a>

A substrate competition model for eukaryotic
cell-cycle oscillations

Combining our models for ordered progression through
DNA replication and mitosis (Fig. 2) and for a minimal
cell-cycle oscillator (Figs. 4 and 5), we now propose a simple
model for cell-cycle regulation based on competition of
substrates for phosphorylation by Cdk and ubiquitylation
by APC (see Fig. 6 A). This model incorporates two groups
of substrates, one required for DNA replication (S) and one
for mitosis (M), and a resetting mechanism for inactivation
of Cdk/CycB at the end of mitosis due to the aforemen-
tioned negative-feedback loop. To this end, we assume
that APC is one of the M-phase substrates of Cdk and PPase.

<a id='666ef912-294f-4041-b58a-401c638528bb'></a>

A characteristic feature of cell division in growing cells is that they divide as often as they double their cytoplasmic mass (balanced growth and division). To capture this feature of cell-cycle control, we make the rate of cyclin synthesis proportional to cell mass, which (we assume) is increasing exponentially. We also assume that cell mass is halved when Cdk activity drops below a certain threshold at the end of mitosis. Observe that in this model, in addition to the negative feedback between Cdk/cyclin and APC, there is a second negative-feedback loop between cell mass and Cdk activity, because cell growth drives increased CycB synthesis, whereas Cdk activation in mitosis eventually leads to a reduction in cell mass at division.

<a id='f243dd75-0716-44a0-ad46-8a7d046c4b39'></a>

Time courses of _S_, Spp, APCpp, Cdk, Sec, and cell mass are shown in Fig. 6 _B_. Although this model generates growth-controlled oscillations in cell-cycle regulators and their substrates (Fig. 6 _B_), the duration of the G1 phase, when Cdk activity is low, is much too short. To understand the dynamical basis of these oscillations, we performed

<a id='575e1c82-0bb0-4cce-a966-0c10c3ef21d2'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='4840c54c-4bd7-4379-ad55-1c3949c385c1'></a>

1374

<a id='3055eef0-5f05-4406-b823-28646d7f50f8'></a>

Gérard et al.

<a id='5ddfec2f-5cbd-4559-8da9-ff4a51f44751'></a>

A <::Diagram showing a regulatory network. It depicts the interactions between M, Mp, Mpp, Cdk/cyclin, Securin, and Cyclin. Cdk/cyclin activates M, and M activates Mp. Mp inhibits M, and Mpp inhibits M. M also inhibits Mpp. Cdk/cyclin also activates Securin and Cyclin. Both Securin and Cyclin inhibit Cdk/cyclin. This forms a complex network of activations and inhibitions.: diagram::>

B With securin <::Line graph showing the time course of Cdk/cyclin, securin, and Mpp (APCpp) with securin. The x-axis represents Time from 60 to 120. The y-axis represents the concentration of Cdk/cyclin, securin, and Mpp (APCpp) from 0 to 1. There are three oscillating curves: a black line labeled "Cdk" that peaks around 75 and 105, a red line labeled "APCpp" that peaks slightly after Cdk, and a green line labeled "Securin" that peaks when Cdk and APCpp are low, around 85 and 115.: line graph::>

C Without securin <::Line graph showing the time course of Cdk/cyclin, securin, and Mpp (APCpp) without securin. The x-axis represents Time from 60 to 120. The y-axis represents the concentration of Cdk/cyclin, securin, and Mpp (APCpp) from 0 to 1. There are three oscillating curves: a black line labeled "Cdk" that peaks around 70, 85, 100, and 115, a red line labeled "APCpp" that peaks slightly after Cdk, and a green line labeled "Securin" that peaks when Cdk and APCpp are low, around 78, 93, and 108. The oscillations are more frequent and the securin levels are lower compared to the 'With securin' graph.: line graph::>

D <::Phase portrait graph with Cdk/cyclin on the x-axis (0 to 1) and Mpp (APCpp) on the y-axis (0 to 1). A large blue closed loop with counter-clockwise arrows indicates a limit cycle. A dashed red line and a solid black line represent nullclines or unstable/stable steady states.: phase portrait::>

E <::Phase portrait graph with Cdk/cyclin on the x-axis (0 to 1) and Mpp (APCpp) on the y-axis (0 to 1). A smaller blue closed loop with counter-clockwise arrows indicates a limit cycle. A dashed red line and a solid black line represent nullclines or unstable/stable steady states. This limit cycle is smaller than the one in graph D.: phase portrait::>

F <::Bifurcation diagram with the Rate of synthesis of Cdk/cyclin, Vscdk, on a logarithmic x-axis (0.001 to 0.1) and Mpp (APCpp) on the y-axis (0 to 1). It shows two stable branches (solid black and blue lines) and an unstable branch (dashed red line) indicating bistability over a range of Vscdk values. The blue line represents the lower stable state and the black line represents the upper stable state.: bifurcation diagram::>

G <::Bifurcation diagram with the Rate of synthesis of Cdk/cyclin, Vscdk, on a logarithmic x-axis (0.001 to 0.1) and Mpp (APCpp) on the y-axis (0 to 1). It shows two stable branches (solid black and blue lines) and an unstable branch (dashed red line). The blue line shows a more complex shape with a peak, indicating a different bifurcation behavior compared to graph F. This also indicates bistability over a range of Vscdk values.: bifurcation diagram::>

<a id='1c70046e-4e84-462e-a233-5d660ce6d475'></a>

FIGURE 5 Minimal oscillator with two steps of phosphorylation and dephosphorylation of M substrates (namely, APC). (A) Schematic diagram. Cdk/cyclin phosphorylates M and M_p, and the doubly phosphorylated form of M (M_pp) promotes the degradation of Cdk/cyclin. The different phos- phoforms of M compete for phosphorylation by Cdk and dephosphorylation by PPase. (B and C) Time evolution of Cdk/cyclin, securin, and M_pp in the presence or absence, respectively, of securin. (D and E) For the cases with and without securin, the limit cycle (closed curve) is projected onto the APC_pp-versus-Cdk/cyclin phase plane. The S-shaped curve is the APC_pp nullcline. For inter- mediate values of Cdk/cyclin, a region of bist- ability is present in the phosphorylation state of APC, whether or not securin is present. Arrows indicate the direction of motion along the limit cycle. (F and G) Bifurcation diagrams for M_pp versus V_scdk in the presence or absence, respec- tively, of securin. Solid curves indicate stable steady states or maxima and minima of the sus- tained oscillations, and dashed curves indicate unstable states. With securin present, the limit- cycle region is bounded by a SNIC bifurcation at V_scdk \approx 0.005 and a Hopf bifurcation at V_scdk \approx 0.15. In the absence of securin, sustained oscilla- tions are still possible, and in this case, the limit- cycle region is bounded by two Hopf bifurcations. Parameter values for the simulations are given in Section 4 of Supplement 1 in the Supporting Material.

<a id='a65f439e-4761-4d0e-8547-018747ed838d'></a>

bifurcation analysis of the regulatory proteins as functions
of cell mass (Fig. 6, C–E). The bifurcation diagrams reveal
stable limit cycles arising at a supercritical Hopf bifurcation

<a id='4be7a867-946e-4935-aaac-1a917f0ae3da'></a>

and growing quickly to large amplitude just beyond the
bifurcation point. For small cell mass, the model is charac-
terized by a stable steady state corresponding to cell-cycle

<a id='3d184da0-7043-479e-a100-4df4bb41c33a'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='6f8865c2-d89c-4073-a508-37525480e0ca'></a>

Cell-Cycle Order by Substrate Competition

<a id='0c5de29b-98ae-4683-baa4-98c98197949c'></a>

1375

<a id='ce3abedc-a842-49a4-aed0-2dea649c9530'></a>

<::Figure A: A biological pathway diagram illustrating the regulation of Cdk/cyclin activity and its downstream effects in a system without Cdh1. The diagram shows the following components and interactions:

**Central Regulator:**
- Cdk/cyclin: A central molecule.

**Inputs and Outputs of Cdk/cyclin:**
- Mass: Promotes Cdk/cyclin activity (black arrow).
- Securin: Produced by Cdk/cyclin (blue arrow), and inhibits Cdk/cyclin (red T-bar).
- Cyclin: Produced by Cdk/cyclin (blue arrow), and inhibits Cdk/cyclin (red T-bar).

**Upper Pathway (S-phase related states):**
- **S state:**
  - Inhibited by M, Mp (red T-bar).
  - Inhibited by Sp (red T-bar).
- **S <-> Sp transition:**
  - Cdk/cyclin promotes S to Sp (blue arrow).
- **Sp state:**
  - Inhibited by Spp, Mp, Mpp (red T-bar).
  - Promotes Spp (red curved arrow).
  - Inhibited by Spp (red curved arrow).
- **Sp <-> Spp transition:**
  - Cdk/cyclin promotes Sp to Spp (blue arrow).
- **Spp state:**
  - Inhibited by S, M, Mp (red T-bar).

**Lower Pathway (M-phase related states):**
- **M state:**
  - Inhibited by Mpp, Sp, Spp (red T-bar).
  - Inhibited by Mp (red T-bar).
- **M <-> Mp transition:**
  - Cdk/cyclin promotes M to Mp (blue arrow).
- **Mp state:**
  - Inhibited by Sp, Spp (red T-bar).
  - Promotes Mpp (red curved arrow).
  - Inhibited by Mpp (red curved arrow).
- **Mp <-> Mpp transition:**
  - Cdk/cyclin promotes Mp to Mpp (blue arrow).
- **Mpp state:**
  - Inhibited by M, S, Sp (red T-bar).

**Overall Context:** Without Cdh1
: pathway::>

<a id='bb47e902-0629-4d6b-b208-fc66a496d184'></a>

Without Cdh1<::figure: The figure displays four plots (B, C, D, E) illustrating cell cycle dynamics without Cdh1. Panel B is a line graph showing the time evolution of several cell cycle components. The y-axis is labeled "S, Spp, APCpp, Cdk/cyclin, securin and mass of the cell" ranging from 0 to 1.4. The x-axis is "Time" ranging from 0 to 400. Multiple lines are plotted: securin (green), S (blue), Spp (orange), APCpp (black), Cdk (red), and mass (grey). Panels C, D, and E are bifurcation diagrams showing hysteresis loops. Panel C plots "Cdk/cyclin" (y-axis, 0 to 0.6) against "Mass of the cell" (x-axis, 0 to 0.3). Panel D plots "Spp" (y-axis, 0 to 1.2) against "Mass of the cell" (x-axis, 0 to 0.3). Panel E plots "Mpp (APCpp)" (y-axis, 0 to 0.8) against "Mass of the cell" (x-axis, 0 to 0.3). All three bifurcation diagrams (C, D, E) show trajectories with upward and downward arrows, indicating transitions.::>arrest. Superimposing the cell-cycle trajectories (Fig. 6 B) on the bifurcation diagrams (Fig. 6, C–E, closed curves) indicates that cells are cycling in the limit-cycle domain (see below). In t is cell-mass depe division.

<a id='5bd5495d-dfd0-4491-b7af-28f737f53503'></a>

FIGURE 6 A model of Cdk oscillations with sequential activation of DNA replication and mitosis. (A) Schematic diagram, combining the basic features of Figs. 2 A and 4 A. Two types of substrate competition are present in this model: 1), competitive inhibition between the different phosphoforms of S and M substrates for Cdk and its counteracting PPase; and 2), competitive inhibition between Cdk/cyclin and securin for ubiquitylation by active APC (APCpp). Growth control of the cell cycle is incorporated by assuming that the rate of synthesis of Cdk/cyclin is proportional to the mass of the cell. (B) Time courses of Cdk/cyclin, S, SPP APCpp, securin, and cell mass. In these simulations, mass increases exponentially with a doubling time of 190 time units. The rate of cyclin synthesis, Vscdk in Eq. 7, is multiplied by mass to couple cyclin accumulation to cell growth. Binary cell division is assumed to occur when Cdk drops below a chosen threshold (0.02) at the end of mitosis. Phosphorylation of S, i.e., initiation of DNA replication, precedes phosphorylation of APC, i.e., entry into mitosis. (C-E) Bifurcation diagrams of Cdk/cyclin, Spp, and APCpp are shown as functions of cell mass, considered as a parameter. Solid curves indicate stable steady states or maxima and minima of the sustained oscillations, dashed curves indicate unstable states, and closed curves indicate cell-cycle trajectory from B. Parameter values for the simulations are given in section 5 of Supplement 1 in the Supporting Material.

<a id='d92586b4-7b1a-4c15-b9cc-70e72975b27a'></a>

arrest. Superimposing the cell-cycle trajectories (Fig. 6 B) on the bifurcation diagrams (Fig. 6, C-E, closed curves) indicates that cells are cycling in the limit-cycle domain above the bifurcation point. Since the cycle time is identical to the mass doubling time, these cycles are growth-controlled, but they lack a bona fide size-control checkpoint. A size-control checkpoint represents a steady state that blocks cell-cycle oscillations until a critical size is reached

<a id='61ffadbd-4761-4d8d-a2a4-043eace16ee0'></a>

(see below). In this network, the period of the oscillation is cell-mass dependent, which allows balanced growth and division.

<a id='e9244fcb-0180-486d-be89-fc48b8373609'></a>

Nongrowing, quiescent cells usually arrest in the G1
phase of the cell cycle without any Cdk activity, but this
model has a stable steady state of low Cdk activity only at
vanishingly small cell mass, because after exiting from
mitosis, APC turns off in response to the drop in Cdk

<a id='13ec2a3b-d208-44cb-802b-ad5a454d16ec'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='b82be15b-095d-46fa-b740-eee958c47804'></a>

1376

<a id='24062460-0f7d-4cb2-9b9f-cdd95411006b'></a>

Gérard et al.

<a id='681ff6a8-11f7-4989-b3b0-e3a1e0dbdf1e'></a>

activity, and the inactivation of APC allows cyclin to rise
again. However, in present-day eukaryotes, an APC regu-
lator, called Cdh1, gets activated by dephosphorylation at
mitotic exit. Active Cdh1 promotes the degradation of
cyclin and securin (see Fig. 7 A), whereas Cdk/cyclin

<a id='555ba9e8-35d8-4472-9166-67649b9a0ed5'></a>

inhibits Cdh1 by phosphorylation. This double-negative-
feedback loop (Cdh1 degrades cyclin, Cdk/cyclin inhibits
Cdh1) gives rise to a stable G1-like steady state (Fig. 7 B)
characterized by a high level of dephosphorylated, active
Cdh1 (S substrate) and a low level of Cdk/cyclin. In effect,

<a id='979dbbce-1e61-4d9a-917d-7222c009f1b3'></a>

A <::Diagram of a regulatory network. The diagram shows several molecular species and their interactions, including activation (blue arrows) and inhibition (red T-bars). The central component is "Cdk/cyclin".

**Main Pathways:**

1.  **Mass to Cdk/cyclin:**
    *   "Mass" activates "Cdk/cyclin".

2.  **Cdh1 phosphorylation pathway:**
    *   "Cdh1" can be phosphorylated to "Cdh1p", which can be further phosphorylated to "Cdh1pp". These interconversions are bidirectional.
    *   **Cdh1 to Cdh1p:**
        *   Inhibited by "Cdh1pp, Mp, Mpp".
        *   Promoted by "Cdk/cyclin" (via "M, Mp").
    *   **Cdh1p to Cdh1pp:**
        *   Inhibited by "Mp, Mpp".
        *   Promoted by "Cdk/cyclin" (via "Cdh1, M, Mp").
    *   Red curved arrows indicate self-regulation or complex feedback within this pathway.

3.  **M phosphorylation pathway:**
    *   "M" can be phosphorylated to "Mp", which can be further phosphorylated to "Mpp". These interconversions are bidirectional.
    *   **M to Mp:**
        *   Inhibited by "Mpp, Cdh1p, Cdh1pp".
        *   Promoted by "Cdk/cyclin" (via "Cdh1, Cdh1p").
    *   **Mp to Mpp:**
        *   Inhibited by "Cdh1p, Cdh1pp".
        *   Promoted by "Cdk/cyclin" (via "M, Cdh1, Cdh1p").
    *   Red curved arrows indicate self-regulation or complex feedback within this pathway.

4.  **Securin and Cyclin pathway:**
    *   "Cdk/cyclin" activates a process that leads to the production of "Securin".
    *   "Cdh1" inhibits the process leading to "Securin" production.
    *   "Securin" promotes "Cyclin" production.
    *   "Cdh1" inhibits "Cyclin" production.
    *   There is an arrow from "Cdk/cyclin" leading to the pathway involving "Securin" and "Cyclin".

**Overall, the diagram illustrates a complex regulatory network involving Cdk/cyclin, different phosphorylation states of Cdh1 and M, and their influence on Securin and Cyclin levels.**: flowchart::>

<a id='5862f0e9-11ea-4390-814f-b675c70605f9'></a>

With Cdh1<::A multi-panel chart showing cell cycle dynamics. The overall title is "With Cdh1". The chart consists of four subplots labeled B, C, D, and E.: chart::>Biophysical Journal 104(6) 1367-1379

<a id='795821ea-5c40-47df-8dad-88fe847aa174'></a>

FIGURE 7 Dynamical behavior of the final model with Cdh1 as an S substrate. (A) Schematic diagram. (_B_) Time courses of Cdk/cyclin, S (Cdh1), Spp (Cdh1pp), APCpp, securin, and cell mass. Notice that Cdh1 allows an extended G1 phase where S is unphosphorylated (compare Fig. 7 _B_ with Fig. 6 _B_). In this case, terms for Cdk degradation by Cdh1, kcdk2 × Cdk × S, and for securin degradation by Cdh1, kdsec2 × Sec × S, are added to Eqs. 7 and 9, respectively. (_C–E_) Bifurcation diagrams of Cdk/cyclin, Spp, and APCpp are plotted as functions of cell mass, considered as a parameter. Superimposed on these bifurcation diagrams are the limit-cycle oscillations (_closed curve_) in _B_. Parameter values for the simulations are given in section 5 of Supplement 1 in the Supporting Material.

<!-- PAGE BREAK -->

<a id='6ad0afa7-1bda-41e2-8e4b-d0f74991d96e'></a>

Cell-Cycle Order by Substrate Competition

<a id='c7a75e50-ead8-4d97-90b7-e0d2f5710b9d'></a>

1377

<a id='94ec4857-993e-47b2-8c19-20af4aac092d'></a>

Cdh1 is as an amplifier of APC function. Once APC becomes active, Cdk activity falls due to the degradation of cyclin by APC. The reduction in Cdk activity allows dephosphorylation and activation of Cdh1, which takes over the APC's role of degrading cyclin and securin.

<a id='07d12917-2e23-4453-8589-bd40a573c7db'></a>

This G1-like steady state is evident in the bifurcation diagrams (Fig. 7, C–E) for the network in Fig. 7 A. The G1-like steady state gives way to large-amplitude limit-cycle oscillations at a saddle node bifurcation point on an invariant circle (SNIC) at cell mass ≈ 0.21. Superimposing the cell-cycle trajectories of Fig. 7 B on the bifurcation diagrams indicates that in each cycle, the cell oscillates back and forth across the SNIC bifurcation. As cell mass increases during the G1 phase, the cell crosses this bifurcation point and enters transiently into a domain of sustained oscillations. The level of Cdk/cyclin increases during S/G2/M, eventually activating the APC. Once activated, the APC promotes degradation of Cdk/CycB, which triggers cell division and resetting of the cell cycle back to the G1-like steady state. In our experience, a SNIC bifurcation provides more reliable growth control of the cell-division cycle than does a Hopf bifurcation (26).

<a id='09e33524-50f9-4cad-aa01-055ebbb426af'></a>

## DISCUSSION
The eukaryotic cell cycle is controlled by alternating activities of Cdks and the APC. Cdk/cyclin complexes phosphorylate proteins required for DNA replication (S phase) and mitosis (M phase). APC-dependent ubiquitylation targets proteins for degradation by the proteasome. Since both Cdk and APC have numerous substrates in eukaryotic cells and modify those substrates at multiple sites, it is reasonable to assume competition among these substrates for their catalysts. Numerous theoretical studies have stressed the role of phosphorylation/dephosphorylation cycles and substrate competition in cell signaling to promote bistable behavior and ultrasensitive response (10,17,27–29). A study based on both theoretical and experimental approaches also showed that ultrasensitivity in the inactivation of the kinase Weel, a critical G2/M regulator of the cell cycle, could emerge as a result of substrate competition (30). Inspired by these studies, we have analyzed here the potential role of substrate competition and/or multisite modification of Cdk and APC substrates in the regulation of the eukaryotic cell cycle.

<a id='585057d4-abef-4c46-a452-d20a28415b26'></a>

First, we show that competition between two groups of Cdk substrates, whose phosphorylations are required for DNA replication (S) and mitosis (M), generates bistable behavior (Figs. 1 and 2). In these models, the substrates are competing for both of their interconverting enzymes, Cdk and its counteracting PPase. We show that the number of bistable domains is dependent on the number of phos- phorylation sites on the substrates. With single-site phos- phosphorylation of both S and M substrates, only one domain of bistability is generated, with sharp kinase/phosphatase

<a id='85f1cecb-338f-44ce-bb7c-6aa0d1e5214b'></a>

thresholds. Hence, as Cdk activity rises and falls, both S and M substrates are phosphorylated and dephosphorylated simultaneously (Fig. 1). Therefore, a single competitive phosphorylation/dephosphorylation cycle of S and M substrates cannot explain the temporal separation of DNA replication and mitosis during cell-cycle progression. However, double phosphorylation of S and M substrates can provide two domains of bistability with separate phosphorylation/dephosphorylation thresholds of S and M substrates (Figs. 2 and 3). The different thresholds could explain why S and M substrates get phosphorylated at different levels of rising Cdk activity, and hence why DNA replication precedes mitosis. Furthermore, S-phase substrates are dephosphorylated at a lower kinase/phosphatase ratio than mitotic substrates, which could explain why the block of rereplication is released only after cells exit from mitosis.

<a id='9aab5cec-9ef1-4e41-8f2f-95b3bb89a61b'></a>

These observations suggest that multisite phosphorylation of competitive S and M substrates is a possible theoretical foundation of the so called quantitative model for cell-cycle progression (2–5). The quantitative model is supported by experimental observations showing that oscillation of a single Cdk/cyclin fusion protein in fission yeast is sufficient to trigger the major cell-cycle events in proper sequence (3). These authors showed that DNA replication commences in response to a low activity of Cdk/cyclin, whereas mitosis requires Cdk/cyclin to cross a much higher activity threshold (3).

<a id='8b5afe3b-e111-4efa-b39e-c0b2733cfd32'></a>

We have also analyzed the dynamical consequences of substrate competition and multisite phosphorylation in case of APC-catalyzed polyubiquitylation of proteins, which leads to their degradation by proteasomes. APC is activated by Cdk/cyclin-dependent phosphorylation, and one of its targets is cyclin itself, which creates a negative-feedback loop. We show that this negative feedback can drive sustained limit-cycle oscillations if
1. another APC substrate competitively inhibits cyclin degradation (Fig. 4), or
2. the APC is activated by Cdk/cyclin-dependent multisite phosphorylation (Fig. 5).

<a id='50345260-d7cd-49b6-bf8d-0b5b812da4c8'></a>

Since cyclin and securin are the only essential APC substrates in yeast and *Drosophila*, we assume that securin is delaying cyclin degradation. However, securin is not an essential protein for cell cycle oscillations in yeast. Perhaps some APC substrate other than securin is ubiquitylated faster than cyclin and accounts for the time delay, but more likely, the time delay is attributable to the fact that APC activation requires Cdk-dependent phosphorylation at numerous sites. If at least two of these sites are competing for Cdk and PPase, then a bistable switch is created that generates the required time delay for the negative feedback to oscillate. We show that a combination of these two time- delay mechanisms (competition of APC substrates and APC multisite phosphorylation) creates a robust, periodic

<a id='94a35770-1a7b-4506-bf74-1c5a522bc7fe'></a>

Biophysical Journal 104(6) 1367-1379

<!-- PAGE BREAK -->

<a id='66835e19-7d89-4d33-9979-cee72e7b4439'></a>

1378

<a id='2f165b0a-1b9e-4280-bcac-86406a4063f8'></a>

Gérard et al.

<a id='40e6fad5-7f8c-4b9f-9a1f-aede9085215a'></a>

fluctuation of Cdk/cyclin activity that could be the heart of
the eukaryotic cell-cycle clock.

<a id='0cebb0bc-945c-48a8-b39b-29ab9f075c32'></a>

By combining this clock model with the model for ordered phosphorylation of Cdk substrates, we create a simple, effective model for the eukaryotic cell cycle. In this model, the clock mechanism guarantees the fluctuation of Cdk/cyclin activity between low and high values by periodic activation of APC (Fig. 6). Rising Cdk activity phosphorylates DNA-replication substrates (S) first and mitotic substrates (M) later. Assuming that the rate of cyclin synthesis is proportional to the size of the cell, the oscillator adjusts its period to the mass doubling time. Therefore, cell mass is doubled during the cell cycle and halved at cell division.

<a id='d87d6a97-a79d-4f71-ba74-3d371d9a0491'></a>

To account for the extended G1 phase in most eukaryotic cell cycles, we have supplemented the model with a role for Cdh1-dependent activation of the APC after exit from mitosis. At the G1/S transition, Cdh1 gets inhibited by Cdk-dependent phosphorylation and stays inactive until mitotic exit, when PPase activity prevails over Cdk. Since the temporal profile of Cdh1 phosphorylation is identical to that of S substrates, we identify active Cdh1 with un-phosphorylated S substrates. With this simple extension, the model describes G1 size-controlled cell cycles of eukaryotes (Fig. 7).

<a id='fe17f9aa-7974-4d50-97e1-5b5d45a5c9b4'></a>

Many experimental and theoretical studies have emphasized the importance of these molecular regulatory mechanisms for correct progression through the eukaryotic cell cycle. These studies, pertaining to embryos (25,31-33), yeast cells (34,35), and mammalian cells (36-44), have amply demonstrated that cell-cycle progression is driven by interlaced positive and negative-feedback loops in the regulation of cyclin-dependent kinases. The model proposed here suggests that cell-cycle regulation depends on at least two levels of bistability, the first from positive-feedback loops embedded in the molecular regulatory network itself, and the second from the intrinsic kinetics of competition between different substrates for protein kinases or for ubiquitin ligases. From an evolutionary point of view, because many of the sophisticated positive-feedback loops in the regulatory mechanism were probably missing in primitive cells, the second source of bistability might have been of great importance for the ordered progression of DNA replication and mitosis in the earliest eukaryotes.

<a id='73d4bbe7-5426-4212-b895-e4829c57c658'></a>

## SUPPORTING MATERIAL

Parameters of the five models and Domain of bistability for the singly-phosphorylated-substrates model, and references (45–49) are available at http://www.biophysj.org/biophysj/supplemental/S0006-3495(13)00202-6.

<a id='ca86a1bb-51cc-45b9-aaa9-e444fc5b262e'></a>

C.G. holds a postdoctoral research fellowship from the Foundation Philippe Wiener–Maurice Anspach. J.J.T. is supported by grants from the National Institutes of Health (5R01-GM078989-07 and 1U54-CA149147-03). The work in B.N.'s group was supported by Biotechnology and Biological

<a id='3a6a890e-e404-45b9-b6a0-711f63a0c297'></a>

Sciences Research Council and by the European Community's Seventh
Framework Programmes UniCellSys/201142 and MitoSys/241548.

<a id='a0bf19dd-1c3e-49f1-8593-a7226bf0e7aa'></a>

## REFERENCES

1.  Fisher, D. L., and P. Nurse. 1996. A single fission yeast mitotic cyclin B p34cdc2 kinase promotes both S-phase and mitosis in the absence of G1 cyclins. *EMBO J.* 15:850–860.
2.  Stern, B., and P. Nurse. 1996. A quantitative model for the cdc2 control of S phase and mitosis in fission yeast. *Trends Genet.* 12:345–350.
3.  Coudreuse, D., and P. Nurse. 2010. Driving the cell cycle with a minimal CDK control network. *Nature.* 468:1074–1079.
4.  Uhlmann, F., C. Bouchoux, and S. López-Avilés. 2011. A quantitative model for cyclin-dependent kinase control of the cell cycle: revisited. *Philos. Trans. R. Soc. Lond. B Biol. Sci.* 366:3572–3583.
5.  Oikonomou, C., and F. R. Cross. 2011. Rising cyclin-CDK levels order cell cycle events. *PLoS ONE.* 6:e20788.
6.  Kõivomägi, M., E. Valk, ..., M. Loog. 2011. Dynamics of Cdk1 substrate specificity during the cell cycle. *Mol. Cell.* 42:610–623.
7.  Holt, L. J., B. B. Tuch, ..., D. O. Morgan. 2009. Global analysis of Cdk1 substrate phosphorylation sites provides insights into evolution. *Science.* 325:1682–1686.
8.  Murray, A. W. 2004. Recycling the cell cycle: cyclins revisited. *Cell.* 116:221–234.
9.  Rape, M., S. K. Reddy, and M. W. Kirschner. 2006. The processivity of multiubiquitination by the APC determines the order of substrate degradation. *Cell.* 124:89–103.
10. Ortega, F., J. L. Garcés, ..., M. Cascante. 2006. Bistability from double phosphorylation in signal transduction. Kinetic and structural requirements. *FEBS J.* 273:3915–3926.
11. Qiao, L., R. B. Nachbar, ..., S. Y. Shvartsman. 2007. Bistability and oscillations in the Huang-Ferrell model of MAPK signaling. *PLoS Comput. Biol.* 3:1819–1826.
12. Ventura, A. C., J. A. Sepulchre, and S. D. Merajver. 2008. A hidden feedback in signaling cascades is revealed. *PLoS Comput. Biol.* 4:e1000041.
13. Goldbeter, A., and D. E. Koshland, Jr. 1981. An amplified sensitivity arising from covalent modification in biological systems. *Proc. Natl. Acad. Sci. USA.* 78:6840–6844.
14. Vigneron, S., E. Brioudes, ..., A. Castro. 2009. Greatwall maintains mitosis through regulation of PP2A. *EMBO J.* 28:2786–2793.
15. Castilho, P. V., B. C. Williams, ..., M. L. Goldberg. 2009. The M phase kinase Greatwall (Gwl) promotes inactivation of PP2A/B55δ, a phosphatase directed against CDK phosphosites. *Mol. Biol. Cell.* 20:4777–4789.
16. Queralt, E., and F. Uhlmann. 2008. Cdk-counteracting phosphatases unlock mitotic exit. *Curr. Opin. Cell Biol.* 20:661–668.
17. Markevich, N. I., J. B. Hoek, and B. N. Kholodenko. 2004. Signaling switches and bistability arising from multisite phosphorylation in protein kinase cascades. *J. Cell Biol.* 164:353–359.
18. Pines, J. 2011. Cubism and the cell cycle: the many faces of the APC/C. *Nat. Rev. Mol. Cell Biol.* 12:427–438.
19. Thornton, B. R., and D. P. Toczyski. 2003. Securin and B-cyclin/CDK are the only essential targets of the APC. *Nat. Cell Biol.* 5:1090–1094.
20. Oliveira, R. A., R. S. Hamilton, ..., K. Nasmyth. 2010. Cohesin cleavage and Cdk inhibition trigger formation of daughter nuclei. *Nat. Cell Biol.* 12:185–192.
21. Marangos, P., and J. Carroll. 2008. Securin regulates entry into M-phase by modulating the stability of cyclin B. *Nat. Cell Biol.* 10:445–451.
22. Novak, B., and J. J. Tyson. 2008. Design principles of biochemical oscillators. *Nat. Rev. Mol. Cell Biol.* 9:981–991.

<a id='695a0236-ec3f-42f5-9f13-2bf511626631'></a>

Biophysical Journal 104(6) 1367–1379

<!-- PAGE BREAK -->

<a id='de19650a-b657-42f2-9d63-ac9bb3a9fa77'></a>

Cell-Cycle Order by Substrate Competition

<a id='90182567-95cf-4349-baf4-4ce6df3b32f9'></a>

1379

<a id='a70ace39-e307-4297-961d-101de920e448'></a>

23. Alexandru, G., F. Uhlmann, ..., K. Nasmyth. 2001. Phosphorylation of the cohesin subunit Scc1 by Polo/Cdc5 kinase regulates sister chromatid separation in yeast. Cell. 105:459–472.
24. Mei, J., X. Huang, and P. Zhang. 2001. Securin is not required for cellular viability, but is required for normal growth of mouse embryonic fibroblasts. Curr. Biol. 11:1197–1201.
25. Novak, B., and J. J. Tyson. 1993. Numerical analysis of a comprehensive model of M-phase control in Xenopus oocyte extracts and intact embryos. J. Cell Sci. 106:1153–1168.
26. Tyson, J. J., A. Csikasz-Nagy, and B. Novak. 2002. The dynamics of cell cycle regulation. Bioessays. 24:1095–1109.
27. Salazar, C., and T. Höfer. 2006. Competition effects shape the response sensitivity and kinetics of phosphorylation cycles in cell signaling. Ann. N. Y. Acad. Sci. 1091:517–530.
28. Salazar, C., A. Brümmer, ..., T. Höfer. 2010. Timing control in regulatory networks by multisite protein modifications. Trends Cell Biol. 20:634–641.
29. Thomson, M., and J. Gunawardena. 2009. Unlimited multistability in multisite phosphorylation systems. Nature. 460:274–277.
30. Kim, S. Y., and J. E. Ferrell, Jr. 2007. Substrate competition as a source of ultrasensitivity in the inactivation of Wee1. Cell. 128:1133–1145.
31. Tyson, J. J. 1991. Modeling the cell division cycle: cdc2 and cyclin interactions. Proc. Natl. Acad. Sci. USA. 88:7328–7332.
32. Goldbeter, A. 1991. A minimal cascade model for the mitotic oscillator involving cyclin and cdc2 kinase. Proc. Natl. Acad. Sci. USA. 88:9107–9111.
33. Ferrell, Jr., J. E., and E. M. Machleder. 1998. The biochemical basis of an all-or-none cell fate switch in Xenopus oocytes. Science. 280:895–898.
34. Chen, K. C., L. Calzone, ..., J. J. Tyson. 2004. Integrative analysis of cell cycle control in budding yeast. Mol. Biol. Cell. 15:3841–3862.
35. Barik, D., W. T. Baumann, ..., J. J. Tyson. 2010. A model of yeast cell-cycle regulation based on multisite phosphorylation. Mol. Syst. Biol. 6:405.
36. Aguda, B. D. 1999. A quantitative analysis of the kinetics of the G(2) DNA damage checkpoint system. Proc. Natl. Acad. Sci. USA. 96:11352–11357.
37. Qu, Z., J. N. Weiss, and W. R. MacLellan. 2003. Regulation of the mammalian cell cycle: a model of the G1-to-S transition. Am. J. Physiol. Cell Physiol. 284:C349–C364.

<a id='72e46ffa-3613-46f1-bc83-f07ec6e0c5f3'></a>

38. Yang, L., W. R. MacLellan, ..., Z. Qu. 2004. Multisite phosphorylation and network dynamics of cyclin-dependent kinase signaling in the eukaryotic cell cycle. *Biophys. J.* 86:3432–3443.
39. Swat, M., A. Kel, and H. Herzel. 2004. Bifurcation analysis of the regulatory modules of the mammalian G1/S transition. *Bioinformatics.* 20:1506–1511.
40. Novák, B., and J. J. Tyson. 2004. A model for restriction point control of the mammalian cell cycle. *J. Theor. Biol.* 230:563–579.
41. Pfeuty, B., and K. Kaneko. 2009. The combination of positive and negative feedback loops confers exquisite flexibility to biochemical switches. *Phys. Biol.* 6:046013.
42. Gérard, C., and A. Goldbeter. 2009. Temporal self-organization of the cyclin/Cdk network driving the mammalian cell cycle. *Proc. Natl. Acad. Sci. USA.* 106:21643–21648.
43. Chauhan, A., S. Lorenzen, ..., S. Bernard. 2011. Regulation of mammalian cell cycle progression in the regenerating liver. *J. Theor. Biol.* 283:103–112.
44. Gérard, C., D. Gonze, and A. Goldbeter. 2012. Effect of positive feedback loops on the robustness of oscillations in the network of cyclindependent kinases driving the mammalian cell cycle. *FEBS J.* 279:3411–3431.
45. Bouchoux, C., and F. Uhlmann. 2011. A quantitative model for ordered Cdk substrate dephosphorylation during mitotic exit. *Cell.* 147:803–814.
46. Loog, M., and D. O. Morgan. 2005. Cyclin specificity in the phosphorylation of cyclin-dependent kinase substrates. *Nature.* 434:104–108.
47. Schweiger, R., and M. Linial. 2010. Cooperativity within proximal phosphorylation sites is revealed from large-scale proteomics data. *Biol. Direct.* 5:6.
48. Weinman, E. J., D. Steplock, ..., S. Shenolikar. 2010. Cooperativity between the phosphorylation of Thr<sup>95</sup> and Ser<sup>77</sup> of NHERF-1 in the hormonal regulation of renal phosphate transport. *J. Biol. Chem.* 285:25134–25138.
49. Pullen, N., N. G. Brown, ..., M. Akhtar. 1993. Cooperativity during multiple phosphorylations catalyzed by rhodopsin kinase: supporting evidence using synthetic phosphopeptides. *Biochemistry.* 32:3958–3964.

<a id='a0b1e28b-bfca-4058-8400-e3054d42ea9b'></a>

Biophysical Journal 104(6) 1367–1379
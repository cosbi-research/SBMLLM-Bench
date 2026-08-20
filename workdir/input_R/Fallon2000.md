<a id='def639ae-49f4-496b-8835-93a97c82fdf7'></a>

Biotechnol. Prog. 2000, 16, 905–916

<a id='4748ddfb-75e7-49e6-a449-0cf5e5754883'></a>

905

<a id='37cd2d5a-4d02-4261-945c-93ee37c0f810'></a>

Computational Model for Effects of Ligand/Receptor Binding Properties on Interleukin-2 Trafficking Dynamics and T Cell Proliferation Response

<a id='8f411521-c6db-47c5-9269-18736c11b4c9'></a>

Eric M. Fallon†,‡, and Douglas A. Lauffenburger†,‡,,,*
Department of Chemical Engineering, Biotechnology Process Engineering Center, and Division of Bioengineering
& Environmental Health, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139

<a id='412847c4-e3ae-451b-b63c-2a59198d6510'></a>

Multisubunit cytokine receptors such as the heterotrimeric receptor for interleukin-2 (IL-2) are ubiquitous in hematopoeitic cell types of importance in biotechnology and are crucial regulators of cell proliferation and differentiation behavior. Dynamics of cytokine/receptor endocytic trafficking can significantly impact cell responses through effects of receptor down-regulation and ligand depletion, and in turn are governed by ligand/receptor binding properties. We describe here a computational model for trafficking dynamics of the IL-2 receptor (IL-2R) system, which is able to predict T cell proliferation responses to IL-2. This model comprises kinetic equations describing binding, internalization, and postendocytic sorting of IL-2 and IL-2R, including an experimentally derived dependence of cell proliferation rate on these properties. Computational results from this model predict that IL-2 depletion can be reduced by decreasing its binding affinity for the IL-2R βγ subunit relative to the α subunit at endosomal pH, as a result of enhanced ligand sorting to recycling vis-à-vis degradation, and that an IL-2 analogue with such altered binding properties should exhibit increased potency for stimulating the T cell proliferation response. These results are in agreement with our recent experimental findings for the IL-2 analogue termed 2D1 [Fallon, E. M. et al. J. Biol. Chem. 2000, 275, 6790–6797]. Thus, this type of model may enable prediction of beneficial cytokine/receptor binding properties to aid development of molecular design criteria for improvements in applications such as in vivo cytokine therapies and in vitro hematopoietic cell bioreactors.

<a id='d224be9d-ad9e-4231-bbcb-12ace007ad8e'></a>

## Introduction
A complex network of molecular and cellular events underlies the diverse responses of the mammalian immune system. Cytokines play an essential role in this system by tightly regulating communication among cells and have thus been explored as a means of therapeutic intervention (1). These proteins exhibit their functionality by binding to specific cell-surface receptors with very high affinity (2). Therefore, optimum response requires delivery of cytokines to target cells at very low concentrations (ca. 10-10-10-12 M). These low levels are difficult to sustain because of rapid clearance via physiological mechanisms in the kidney, liver, and/or lung. In addition, negative feedback is often provided via specific endocytosis of ligand upon binding to its cognate receptor (3). This down-regulatory mechanism can be a significant cause of systemic cytokine depletion, as has been demonstrated with GCSF (4). This creates the need to deliver dangerously high doses in order to maintain reasonable

<a id='6dabd820-5633-4c69-a114-f3f7908d0d59'></a>

* Tel: (617) 252-1629. FAX: (617) 258-0204. E-mail: lauffen@mit.edu.
† Department of Chemical Engineering.
‡ Biotechnology Process Engineering Center.
§ Division of Bioengineering & Environmental Health.
‖ Present address: IDEC Pharmaceuticals Corporation, 11011 Torreyana Road, San Diego, CA 92121.

<a id='1aa56748-4cbb-4a8e-a458-1eed68a594a0'></a>

in vivo cytokine concentrations (5, 6). These doses often
produce toxic, sometimes lethal, side effects (7, 8).

<a id='3315ed24-ca32-409b-8516-996031473b29'></a>

Interleukin-2 (IL-2) was one of the earliest isolated cytokines, and its function is crucial in governing the expansion and differentiation of several hematopoietic cell types (9, 10). It was originally termed T cell growth factor (TCGF) on the basis of its critical role as a proliferative signal for CD4+ T-lymphocytes and has been involved in numerous clinical studies in the treatment of AIDS (11-15). IL-2 has also been utilized as an adjuvant for cancer therapy on the basis of its stimulation of CD8+ or cytotoxic T cells (16-19). Unfortunately, systemic toxicity has been a major setback in broadening FDA approval of IL-2. The pleiotropic effects of IL-2 on multiple hematopoeitic cell types can create undesired stimulation of cell types other than T cells, since various cells express different isoforms of IL-2 receptor subunits. Cell receptor-level pharmacodynamic issues may, therefore, be important for understanding the effects of IL-2 in vivo and in expanding its therapeutic applicability (20, 21). In addition, cell-level pharmacokinetic analysis requires consideration of receptor-mediated endocytic degradation of cytokine molecules that, over time, can lead to depletion of ligand from the extracellular medium (22).

<a id='7936e6a9-dda3-4975-9cb8-4790a85fde74'></a>

The IL-2 receptor on activated T-lymphocytes consists of α, β, and γ subunits, the latter two of which are shared

<a id='bca2a02a-00ac-4bc9-9cdb-72baee9c71db'></a>

10.1021/bp000097t CCC: $19.00

<a id='46cb9e94-a59d-483c-938f-aba5191b8f1e'></a>

© 2000 American Chemical Society and American Institute of Chemical Engineers Published on Web 09/14/2000

<!-- PAGE BREAK -->

<a id='a78c0037-8c41-4bc8-8986-433e2e05db7c'></a>

906

<a id='b47bf9e3-0fb8-410d-861d-8c98617f4bc7'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='09155f64-ec10-488c-925d-31c3024e020a'></a>

among several other interleukins (23, 24). The α subunit is exclusive to IL-2, and its expression levels are 10- to 100-fold greater than those of β or γ on antigen-activated T cells (9). The α subunit enhances the affinity of the IL-2R complex for soluble IL-2 (25–27) and is signaling-deficient, as it possesses only 13 residues in its cytoplasmic domain (28). The β and γ subunits have both been implicated in specific intracellular signaling pathways that are activated upon IL-2 binding (29, 30). The heterotrimeric IL-2 receptor binds its ligand with high affinity (K_D = 10 pM) and then undergoes rapid internalization and specific degradation of both IL-2 and the β and γ subunits (31–33). The β and γ subunits undergo specific lysosomal degradation along with bound IL-2, while the α subunit is constitutively recycled following postendocytic sorting (34). Therefore, receptor/ligand trafficking dynamics should influence the potency of IL-2 to at least as significant a degree as receptor binding affinity, as has been illustrated in the EGF ligand–receptor system (35, 36).

<a id='78b7cd47-1b50-4847-95ff-40c857534a3f'></a>

The effects of postendocytic trafficking dynamics on potency can be counterintuitive with respect to the binding affinity of ligand-receptor interactions. For example, an EGF mutant was shown to be a more potent mitogen than wild-type EGF despite possessing a 50-fold lower binding affinity to the EGF receptor (36). This result stemmed from a decreased internalization rate and increased recycling rate for both ligand and receptor, opposing the signal-attenuating effects of ligand depletion and receptor downregulation. An IL-2 variant with increased affinity for the α chain but reduced affinity for the βγ-complex demonstrated greater potency based on similar effects in a different system (37). This result is also counterintuitive because the mutation increased the ligand's affinity for the subunit not directly involved in signal transduction while decreasing the affinity for the chains that generate a mitogenic signal.

<a id='837b98ed-d603-407b-af56-7fef479a9c3f'></a>

A quantitative relationship between IL-2/IL-2R binding and T cell proliferation was initially proposed by Robb (38). Smith and co-workers later showed that only three elements were crucial for cell cycle progression in T cells: IL-2 concentration, IL-2R density, and the duration of the ligand/receptor interaction (39-41). This suggested that the dynamics of the IL-2/IL-2R interaction were crucial determinants of cellular function, and numerous studies have been undertaken to elucidate the nature of binding, internalization, and trafficking in this system (31-33, 42-47). Detailed mathematical models describing alternative mechanisms of IL-2 binding and endocytosis have been proposed, as have separate models for cytokine-induced T cell proliferation (48-52). Much of the experimental and computational work to date, however, has considered IL-2 trafficking independent from quantitative growth studies.

<a id='dbdc6271-b38b-4972-ac94-980ec1854e39'></a>

Our goal is to develop a quantitative framework for
relating molecular-level binding and trafficking events
to cell-level function as part of an integrated dynamic
system. This approach has yielded insight into the events
underlying mitogenic responses of fibroblasts to the EGF
family of ligands, thus aiding in the molecular manipula-
tion of cellular responses (35, 36, 53-55). We extend
similar analyses to the more therapeutically relevant IL-2
system and include the added level of complexity associ-
ated with its multisubunit receptor. The model follows
from experimental work wherein detailed binding, traf-
ficking, and mitogenesis studies were performed within
a single cell system. This work demonstrated that a
double mutant of IL-2, Leu18Met/Leul9Ser (termed

<a id='66ea77b3-4e1f-4f0a-b2b2-9c4d1ad0b512'></a>

<::diagram of a cellular process illustrating ligand-receptor binding, internalization, recycling, and degradation pathways. The diagram features a cell membrane separating the extracellular space (top) from the intracellular environment (bottom). Receptors are depicted as Y-shaped structures on the membrane and within vesicles, while ligands are small oval shapes.  Extracellular ligands bind to receptors on the cell surface with a forward rate constant `kf` and dissociate with a reverse rate constant `kr`. New receptors are synthesized and inserted into the membrane at a rate `ksyn`. Receptors on the cell surface can be degraded with a rate `kt`. Ligand-receptor complexes are internalized into an endosome with a rate constant `ke`. Within the "ENDOSOME" (labeled with volume `Ve`), ligands and receptors are shown. Ligands are recycled back, a process labeled "LIGAND RECYCLING" with a rate constant `kx`. Ligands within the endosome are subject to degradation, indicated by `μ(Cs)`. Receptors within the endosome can bind ligands with rate `kfe` and dissociate with rate `kre`. Receptors and complexes are ultimately transported to the "LYSOSOME" for degradation, a process labeled "RECEPTOR/COMPLEX DEGRADATION" with a rate constant `kh`. An arrow `Vs` points towards the endosome, indicating an input or source.::>

<a id='0ac14569-c69a-46a4-830b-a7d39f7451d6'></a>

Figure 1. Model schematic. This model follows the path of an extracellular ligand, beginning with the kinetics of binding to the IL-2 receptor (k<sub>f</sub> and k<sub>r</sub>) and receptor-mediated internalization (k<sub>e</sub>) into sorting endosomes (volume V<sub>e</sub>). The off-rate (k<sub>re</sub>) increases at this point as a result of the pH sensitivity of binding, and the on-rate (k<sub>fe</sub>) is recalculated using the K<sub>D</sub> for binding to the relevant IL-2Rβγ complex. Receptor-associated ligand is routed to lysosomal degradation (k<sub>h</sub>), while free ligand or that bound to IL-2Rα is recycled (k<sub>x</sub>). Steady-state receptor levels in the absence of ligand are described by constitutive internalization (k<sub>t</sub>) and biosynthesis (V<sub>s</sub>) rates. Ligand-receptor complexes stimulate new receptor synthesis (k<sub>syn</sub>) and cell proliferation (μ) during their lifetime on the cell surface.

<a id='3206a18d-d131-42f0-9600-c6fbb303e2c2'></a>

2D1), displayed reduced endocytic degradation when compared to wild-type IL-2 (WT) and that this effect was due to enhanced ligand recycling. The continuous flow of ligands through intracellular sorting pathways thus led to greater sustenance of 2D1 concentrations in cell culture and increased T-lymphocyte proliferation (37).
The objective of our modeling work is not to mimic these experimental results in specific detail but rather to elucidate insights concerning key molecular properties that should be considered in a ligand-based protein engineering approach to altering cell function. The insights derived from this model can aid in interpreting our experimental ligand/receptor trafficking and cell proliferation results, while highlighting receptor/ligand-binding parameters that may play a major role in governing ligand potency for applications of hematopoietic cells in biotechnology.

<a id='bd41afc0-ba81-4609-8a80-c3a4a5d9c410'></a>

# Methods

**Computational Model.** Our ligand trafficking model describes the fate of an IL-2 ligand upon binding, internalization, and postendocytic sorting via the heterotrimeric IL-2 receptor (Figure 1). A central goal of the model is to dynamically integrate IL-2-mediated molecular and cellular events that occur on multiple time scales. These include ligand-receptor binding events that transpire on the scale of seconds/minutes, endocytosis and sorting that develops over minutes/hours, and the proliferative response of cells to cell-surface IL-2/IL-2R complexes that manifests over hours/days in the presence of extracellular ligand (39). The model therefore illustrates the balance between cell receptor-mediated degradation of extracellular IL-2 and the cell's mitogenic response to intact ligand in the surrounding medium.

In a largely comprehensive form, the model could include individual kinetic rate processes for each of the

<a id='6ca3e0f5-2f39-428a-80e2-5d3160584778'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='374a50fd-0096-4466-8dcd-ab347749485a'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='95a41440-d1d7-405b-9703-173d272136e9'></a>

907

<a id='bb5ec122-4f85-4d98-a154-3785d2983350'></a>

receptor subunits (α, β, and γ) as well as all possible combinations of these and corresponding ligand-bound species. However, since only a small portion of these processes has been quantitatively characterized, this approach would introduce an unacceptable number of unknown model parameters. Therefore, we will simplify the model to the essential features for our objectives. As will be discussed below, IL-2 trafficking dynamics are essentially governed by the degree of binding to the αβγ receptor complex at the cell surface and by the degrees of binding to the α subunit and the βγ complex in the endosomal compartment. At the cell surface, endocytic internalization of IL-2 predominantly occurs via occupancy of the full heterotrimeric receptor complex. In the endosomal compartment, sorting of the ligand to recycling and lysosomal degradation are governed by occupancy of the α subunit and the βγ complex, respectively. Accordingly, we can satisfactorily account for IL-2 trafficking dynamics by considering the receptor to simply be the αβγ complex at the cell surface and the βγ complex in the endosomal compartment. Since the α subunit is found to sort differently from the βγ complex in the endosome, it must become uncoupled there (34); this could arise from a pH sensitivity of the receptor subunit coupling affinities. Thus, endosomal routing of IL-2 to lysosomal degradation will be proportional to the amount remaining bound to the βγ receptor complex while routing to recycling will be proportional to the amount dissociating from that complex with the α subunit.

<a id='7ce5cdc5-72d7-4cbb-82f0-7f29b073695a'></a>

The dynamic model simulates the fate of ligands and receptors upon introduction of a bolus concentration of ligand into the extracellular medium at time zero. In the absence of ligand, the number of cell-surface and internal receptors represents a balance between constitutive internalization (kt) and new receptor synthesis (Vs) (56). The presence of ligand causes both specific endocytosis of ligand–receptor complexes (ke) and up-regulation of receptor synthesis via intracellular signaling cascades (ksyn). Both of these processes have been observed and quantified in IL-2/T cell systems (57, 58). The binding of IL-2 to the high-affinity (αβγ) receptor complex has been well characterized, and resultant association (kf) and dissociation (kr) rate constants are indicated in Figure 1 (59, 60).

<a id='59c53d28-17a1-464f-a3f5-09b04ca80fc7'></a>

We take advantage of the experimentally established common sorting behavior of the ̒ and ̔ subunits by designating receptors (R) as the IL-2R̖̒̔ complex throughout the model. This assumption does not confound the analysis of ligand (L) binding with cell-surface receptors to form ligand/receptor complexes (C), despite the fact that IL-2R̒ is expressed in excess of the ̒ and ̔ chains. The ̒, ̒, and ̔ chains have been shown to co-localize even in the absence of IL-2 on the KIT-225 human T cell line (61), consistent with a model in which subunit dimers or even trimers may be preformed to a significant extent (62). Although IL-2R̒ can bind IL-2 with a K₄ ≈ 10 nM, at the ligand concentrations considered (<200 pM) the vast majority of these receptors are unbound. In addition, IL-2R̒ is internalized only as part of high-affinity (̒̒̔) receptors in the presence of IL-2 and cannot internalize IL-2 by itself (34, 63, 64). Thus, our model designation of the receptor variable, R, as the IL-2R̖̒̔ complex is clearly a simplifying assumption, but one that captures the essential features of ligand trafficking in this system— high affinity binding at the cell surface, and in the endosome sorting to recycling when dissociated and sorting to degradation when remaining bound.

<a id='ba433805-8188-44f5-9b69-89cf51857fbe'></a>

Nonspecific or fluid-phase uptake of ligand is neglected,
as this effect is typically apparent only at ligand concen-
trations greater than 10 nM (65). Thus, internalization
of IL-2 occurs solely via receptor-mediated endocytosis
(66, 67). Although this process is saturable at high ligand
concentrations, the low density of high affinity IL-2
receptors on T cells makes saturation an unlikely phe-
nomenon (68, 69), consistent with experimental studies
(37). As noted above, experimental evidence indicates
that the components of the IL-2/IL-2R complex undergo
differential sorting wherein IL-2Rα is recycled to the cell
surface while IL-2, IL-2Rβ, and IL-2Rγ all remain as-
sociated en route to lysosomes (34). Specific regions have
recently been identified in the cytoplasmic tails of both
the IL-2Rβ and γ chains that mediate specific sorting of
these subunits to degradation (31–33). No such signals
exist in the short 13-residue intracellular tail of IL-2Rα,
allowing it to follow the default-recycling pathway upon
dissociation from the IL-2/IL-2R complex (28). These
results implicate potential accessory proteins that may
be involved in endosomal retention and subsequent
lysosomal sorting of ligand-bound IL-2Rβγ complexes, as
has been postulated in the EGF system (70, 71). Although
this EGF pathway has been shown to be saturable at
high intracellular ligand concentrations, the relatively
low expression levels of IL-2Rβγ on T cells makes it
unlikely that the IL-2 system would exhibit such satura-
tion behavior (72, 73). Interleukin-2 sorting outcomes are
thus derived solely from association (kfe) and dissociation
(kre) rate constants that depict ligand binding to the IL-
2Rβγ complex in the endosome. Consideration of the
kinetics of these interactions may be important since
ligand enters endosomes as a component of bound ligand/
receptor complexes but can thus dissociate from and
rebind to receptors under endosomal conditions (74). The
binding of IL-2 to both the IL-2Rαβγ complex and the
IL-2Rβγ heterodimer has been well characterized at cell-
surface pH, as each is expressed on distinct hematopoeitic
cell types (59, 75).

<a id='fc8dad2a-1234-407a-81c2-7d581c56b701'></a>

Upon localization to endosomes, the IL-2Rα subunit uncouples from the IL-2/IL-2Rβγ complex (34). Free βγ heterodimer (termed Rᵢ) and IL-2 bound to this heterodimer (Cᵢ) are assumed to undergo degradation at a rate described by kₕ. The rate of generation of degraded ligand (Ld) is then calculated in order to determine recycling fractions or the percentage of ligand entering the cell that is released intact following endosomal sorting. Free intracellular IL-2 (Li) is considered to be subject to the same fate as intracellular IL-2Rα, namely, recycling with a first-order rate constant (kx). Thus, the sorting outcome of an internalized IL-2 molecule is described entirely by the kinetics of binding to IL-2Rβγ and the competing rates of recycling and degradation. Recycling and degradation rate constants represent the experimentally accessible lumped parameters that describe the translocation of molecules from sorting endosomes to late (recycling) endosomes or lysosomal compartments, respectively. The detailed molecular events underlying endosomal sorting have been modeled elsewhere and are not the focus of the present work (71, 76). Rather, this model seeks to relate the causal effects of endocytic ligand turnover on the functional response of T cells to physiologic concentrations of IL-2, as these cells are known to rapidly deplete IL-2 via this mechanism (59, 77).

<a id='81f478bb-31f3-4e54-888d-08b1ae12dbcf'></a>

Ligand-receptor complexes on the cell surface are
assumed to stimulate both new receptor synthesis ($k_{syn}$)
and mitogenesis, as both have been quantified experi-

<a id='890dc7b5-9227-47ba-8c72-438ce0f99ba5'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='cec48ccb-638c-401f-b2aa-ddcb60884658'></a>

908

<a id='c1c773a6-7214-428f-b2a7-c9d311dbd8e9'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='373dd533-dee1-4f0a-89ae-b93957faee35'></a>

<::transcription of the content: chart::>
Figure 2. Dependence of T cell proliferation rate on IL-2/IL-2R complex number (37). The chart displays T cell proliferation rate (d(cell density)/dt) on the y-axis (log scale, from 1 to 1000) versus Cell-Surface Complexes (#/cell) on the x-axis (linear scale, from 0 to 5000). Data points are shown for wild-type IL-2 (filled circles, •) and the 2D1 analogue (open circles, ○), each with error bars. A solid line represents the 'Model'. The change in cell number density was measured for various concentrations of wild-type IL-2 (•) and the 2D1 analogue (○) over 24-h intervals throughout 5-day proliferation experiments. Cell-surface complex numbers were calculated from simultaneous measurements of intact ligand concentration and receptor levels during the growth experiments, using the measured ligand/receptor binding affinity (see Table 1); data here are from reference 37. 
<::>

<a id='9c244c5b-76f4-4fc6-b982-840acf6988d5'></a>

mentally in IL-2/T cell systems (77, 78). Up-regulated expression of IL-2Rα subunits in response to exogenous IL-2 has been measured in activated peripheral blood lymphocytes, and the model includes a first-order rate constant to describe this process (58). The increase in α subunits can lead to some increase in the number of αβγ receptor complexes, depending on the stoichiometric and equilibrium properties of subunit interactions (75). The mitogenic response of T cells to IL-2 is less straightfor- ward to model from first principles, because cell cycle events occur over much longer time scales than the ligand–receptor binding interactions that initiate intra- cellular signaling cascades. Thus, we will incorporate an empirical relationship here, derived from our own ex- perimental studies (37). We have found from simulta- neous measurements of proliferation and ligand/receptor binding of a T cell line in response to IL-2 a dependence whereby the specific cell growth rate is minimal below a threshold number of IL-2/IL-2R complexes per cell and then rapidly increases to a relatively constant value above this threshold complex number (Figure 2). This type of relationship was envisioned from theoretical arguments by Cantrell and Smith (39, 40) and has also been observed in studies relating the mitogenic response of fibroblasts to EGF (35, 54). Our model uses a quantita- tive expression describing this dependence to relate the change in cell density (Y) to cell-surface complex number (C_s), as shown in eq 8 below. One can imagine simply using a piece-wise constant threshold expression instead, and likely there would be negligible difference in the computational results. Actually, the major predictions of the model are not critically sensitive to details of the cell proliferation kinetics, because the ligand depletion dy- namics are not substantially influenced by the observed cell density changes, which are less than a factor of 10 over the experimental time course.

<a id='06c4ccec-c86c-4fa0-8343-4e45d892cbf2'></a>

Corresponding to the concepts outlined above, the following equations govern the dynamic processes diagrammed in Figure 1. All symbols have been defined above, with the subscripts s and i referring to the cell surface and intracellular compartments, respectively.

<a id='e58941a2-8e98-4b0f-88cf-e40280a56231'></a>

dR_s / dt = -k_f * L[t] * R_s[t] + (k_r + k_syn) * C_s[t] - k_t * R_s[t] + V_s (1)

<a id='bd7f3789-ff98-4602-997f-249663416775'></a>

$$\frac{dC_s}{dt} = k_f \cdot L[t] \cdot R_s[t] - (k_r + k_e) \cdot C_s[t] \quad (2)$$ 

<a id='3b78f41e-4057-490a-891e-6b2e5282829b'></a>

dRᵢ/dt = -k_fe * Lᵢ[t] * Rᵢ[t] + k_re * Cᵢ[t] + k_t * R_S[t] - k_h * Rᵢ[t]
(3)

<a id='0ad414ed-fbfb-4d51-9c01-25e69174f5ae'></a>

dC_i / dt = k_fe * L_i[t] * R_i[t] - (k_re + k_h) * C_i[t] + k_e C_s[t] (4)

<a id='527370db-8375-4c8c-b459-8f7933b6f804'></a>

$$\frac{dL_i}{dt} = \frac{(-k_{fe} \cdot L_i[t] \cdot R_i[t] + k_{re} \cdot C_i[t])}{(V_e \cdot N_A)} - k_x \cdot L_i[t] \quad (5)$$ 
 
$$\frac{dL_d}{dt} = k_h \cdot C_i[t] \quad (6)$$


<a id='5bdb6491-7f69-4c09-b0dd-862aaa054fb1'></a>

$\frac{dL}{dt} = \frac{(-k_f \cdot L[t] \cdot R_S[t] + k_r \cdot C_s[t] + k_x \cdot L_i[t] \cdot V_e \cdot N_A) \cdot Y[t]}{(N_A)}$ (7)

<a id='00c62549-21e0-4d2a-abde-19dab4b1c6fb'></a>

$$\frac{dY}{dt} = \text{Max}\left\{\left[\frac{600\cdot C_s(t)}{250 + C_s(t)}\right] - 200,0\right\} \times 10^3 \quad (8)$$

<a id='9307ee77-d499-42c9-b601-9f297772a1d2'></a>

**Parameter Evaluation and Computational Procedure.** Base values for the parameters used in the model are listed in Table 1. All values are derived from previously reported literature data or from the experimental work related to the development of this model. Although these parameter estimates are heterogeneous in the sense that they derive from diverse lymphocytic cell types, as will be seen in the computational results the trends are insensitive to reasonable parameter value variations. No major qualitative behavioral differences are predicted as parameter values are changed over the range of a few orders of magnitude, and significant quantitative changes in calculated outcomes require at least an order-of-magnitude change in any particular paramater estimate.

<a id='96eeca36-7574-4fa0-891f-76b7d0532385'></a>

We consider the IL-2 analogue 2D1 in parallel with wild-type IL-2 in order to explore potential effects of ligand-based alterations in receptor binding affinities on postendocytic trafficking outcomes. Dissociation constants describing the binding of this variant to the high-affinity (αβγ) IL-2 receptor have been reported (79). Kinetics of wild-type IL-2/IL-2R binding were measured using radioreceptor assays on cell membrane preparations, and the resultant dissociation rate constant is used as the base value at cell-surface pH (60). Association rate constants for IL-2 and 2D1 binding to the IL-2Rαβγ complex are estimated by dividing this base value of the dissociation rate constant by the respective value of K D for each ligand. In the analysis that follows, dissociation rate constants are varied from 0.00138 to 0.138 min⁻¹ independent of the value of K D in order to distinguish effects of binding kinetics from equilibria.

<a id='a7468bbe-b360-4cc9-82bd-b100750b547c'></a>

The pH in sorting endosomes is decreased relative to the cell surface (~6.0 vs 7.2), and this pH drop has been shown to decrease the affinity of IL-2 ligands for both the a and ̥ IL-2R subunits (37). Receptor/ligand binding kinetic rate constants in endosomes for IL-2 and 2D1 are thus each estimated by multiplying the dissociation rate constant at pH 7.2 by the ratio of the experimentally

<a id='891d3b09-1237-4263-81a1-62a324f70edb'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='af54314a-7476-4132-84b5-ff46ce3a823a'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='988e3af1-144f-47da-be47-94b5c744bac2'></a>

909

<a id='ee3fda93-d171-481c-a330-6599903f4fea'></a>

Table 1. Model Parameters
<table id="4-1">
<tr><td id="4-2">parameter</td><td id="4-3">definition</td><td id="4-4">reference</td><td id="4-5">base value(s)</td></tr>
<tr><td id="4-6">kᵣ</td><td id="4-7">dissociation rate constant</td><td id="4-8">60</td><td id="4-9">0.0138 min⁻¹</td></tr>
<tr><td id="4-a">kᵢ</td><td id="4-b">association rate constant</td><td id="4-c">79</td><td id="4-d">kᵢ/11.1 pM⁻¹ min⁻¹ (IL-2)</td></tr>
<tr><td id="4-e">kᵣₑ</td><td id="4-f">dissociation rate constant, endosome</td><td id="4-g">37</td><td id="4-h">kᵢ/8.2 pM⁻¹ min⁻¹ (2D1) 8 kᵣ min⁻¹ (IL-2)</td></tr>
<tr><td id="4-i"></td><td id="4-j"></td><td id="4-k"></td><td id="4-l">5 kᵣ min⁻¹ (2D1)</td></tr>
<tr><td id="4-m">kte</td><td id="4-n">association rate constant, endosome</td><td id="4-o">37</td><td id="4-p">kre/1000 pM⁻¹ min⁻¹ (IL-2) kre/3000 pM⁻¹ min⁻¹ (2D1)</td></tr>
<tr><td id="4-q">kt</td><td id="4-r">constitutive internalization rate constant</td><td id="4-s">80</td><td id="4-t">0.007 min⁻¹</td></tr>
<tr><td id="4-u">Vs</td><td id="4-v">constitutive receptor synthesis rate</td><td id="4-w">47</td><td id="4-x">11 min⁻¹</td></tr>
<tr><td id="4-y">ksyn</td><td id="4-z">induced receptor synthesis rate</td><td id="4-A">58</td><td id="4-B">0.0011 min⁻¹</td></tr>
<tr><td id="4-C">ke</td><td id="4-D">internalization rate constant</td><td id="4-E">37</td><td id="4-F">0.04 min⁻¹</td></tr>
<tr><td id="4-G">k_k</td><td id="4-H">recycling rate constant</td><td id="4-I">84</td><td id="4-J">0.15 min⁻¹</td></tr>
<tr><td id="4-K">k_h</td><td id="4-L">degradation rate constant</td><td id="4-M">47</td><td id="4-N">0.035 min⁻¹</td></tr>
<tr><td id="4-O">V_e</td><td id="4-P">total endosomal volume</td><td id="4-Q">73</td><td id="4-R">10⁻¹⁴ L/cell</td></tr>
</table>

<a id='ee793e55-88f2-4b19-b720-cd468abead2f'></a>

measured IL-2Rβ subunit binding affinity at pH 6 to that
at pH 7.2. The β subunit value is used because it is the
primary determinant of the interaction between ligand
and βγ complex as the α subunit decouples.

<a id='f229b9aa-b38e-4d41-90b8-4b1084664413'></a>

A dynamic balance between biosynthesis and constitutive endocytosis defines the total receptor number at steady state, even in the absence of ligand. The constitutive internalization rate constant for IL-2 receptors on T cells has been determined from receptor decay from the cell surface while protein synthesis was chemically inhibited (80). In similar experiments, the reappearance of receptors was probed with radiolabeled IL-2 immediately following treatment of cells with trypsin (47). This reappearance was quantified over time to yield a constitutive receptor biosynthesis rate. In the presence of IL-2, overall receptor turnover is influenced by these constitutive rates and specific events that occur upon IL-2 binding to its receptor. IL-2 has been shown to induce synthesis of IL-2Rα, while the overall rate of IL-2Rαβγ receptor endocytosis is enhanced upon binding. This allows the cell to attenuate its response to the signaling competent IL-2Rβγ complex while retaining the capacity to bind IL-2. The result of these competing effects is the maintenance of a relatively constant population of high-affinity receptors on the cell surface, though the greater number of IL-2Rα subunits creates a net increase in the number of measurable receptors on the cell surface (59, 81, 82). Simultaneous measurement of receptor synthesis and endocytosis using receptor subunit specific antibodies permits calculation of a net induced receptor synthesis rate (58).

<a id='a38663ab-7f83-47b6-92f9-98f49983f343'></a>

The intracellular trafficking rate constants (kx and kh) describe the rate of movement of components from hypothetical postsorting recycling and degradation compartments, respectively. These transport rates have been shown to be dependent only on the endocytic apparatus and not on specific ligand–receptor systems (83). Thus, the recycling rate constant reported for the constitutively recycled transferrin receptor was used as an estimate of kx (84). Since we are considering kh as a lumped parameter that represents the outcome of potentially complex sorting events, the specific degradation rate previously reported for IL-2 receptors in T cells is employed in the model (47). Consideration of the sorting events undergone by soluble ligands in the endosome requires an estimate of the endosomal volume within the cell. Compiled results of several quantitative morphological studies are used to obtain the estimate of 10^-14 L/cell used in our model (71).

<a id='4cfc7000-7c56-49d9-8137-20b10b56fd93'></a>

Model equations are solved numerically using Math-
ematica (version 4.0, Wolfram Research) with nonzero
initial conditions, including the extracellular ligand
concentration and cell density at the start of a hypotheti-

<a id='e9ac8ec7-b410-4379-8449-666f283d0603'></a>

cal experiment. The initial cell-surface receptor number is ~1500 per cell as defined by the estimates of V_s and k_t shown in Table 1. This is representative of the number of high affinity IL-2 receptors found on both activated T-lymphocytes and on the KIT-225 cell line used in previous experiments. The initial internal receptor num- ber is similarly fixed at ~300 per cell by the estimates of V_s and k_h. Simulations are carried out for 5 days to mimic a ligand depletion/cell proliferation experiment. Intact ligand concentration (_L_), cell density (_Y_), and cell-surface complex number (_C_s) are calculated throughout the simulation.

<a id='77c8546d-0618-4c2f-9739-f983bf26a1d4'></a>

Sorting experiments are mimicked by performing simulations over a range of input ligand concentrations for 180 min, at which time sorting reaches steady-state following the initial perturbation due to introduction of extracellular ligand (72, 73). The values of R$_{s}$, R$_{i}$, C$_{i}$, and L$_{i}$ are recorded and used as inputs into a second simulation wherein these values serve as initial conditions along with zero extracellular ligand concentration (37). Degraded and intact ligand concentrations are recorded throughout this 15-min simulation and used to calculate recycling fractions, or the amount of ligand sorting to recycling vs the amount sorted to degradation.

<a id='bc7e6d37-aa2d-40bf-8fe7-fcf923219b54'></a>

# Results
Comparison of Base Model Predictions to Experimental Results with Wild-Type IL-2. The objective of this computational effort is to predict T cell proliferation responses to IL-2 from ligand/receptor binding properties as they influence receptor-mediated ligand trafficking dynamics. We have previously measured these two events simultaneously using the IL-2-dependent KIT-225 human T cell line (37). These cells rapidly degraded IL-2 via receptor-mediated endocytic depletion, and this effect was observed at both saturating and half-saturating concentrations with respect to the high-affinity IL-2 receptor. The kinetic parameters used in the model that describe binding, trafficking, and signaling events were accumulated from a variety of experimental sources. Therefore, to test the ability of our model to accurately predict the effects of molecular parameters on cell-mediated ligand depletion, simulations were performed using the trafficking parameters shown in Table 1, including those specific for wild-type IL-2. The experimentally observed depletion behavior is accurately predicted at both high and low ligand concentrations (Figure 3).

<a id='d5e33a11-1b9f-4ee0-940c-eea584c8e3c5'></a>

Results of 5-day proliferation experiments employing
10 pM and 100 pM IL-2 are shown along with model
predictions in Figure 4. The model incorporates a thresh-
old-type dependence of cell growth rate on cell-surface

<a id='3c7cdae7-12f9-4922-9b5e-369957339590'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='a38534d8-1e18-4544-9131-0d77c46352e1'></a>

910

<a id='e32c84bd-adc1-4469-8a49-163b2b5d7e04'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='05775450-c6fa-402a-b8d3-ae7731d437aa'></a>

<::chart: A line graph titled "Intact Ligand Concentration (pM)" on the y-axis, ranging from 0 to 100 in increments of 10, and "Time (min)" on the x-axis, ranging from 0 to 8000 in increments of 1000. The graph displays two sets of data: 1. A curve and filled square symbols representing experimental data and model predictions for an initial ligand concentration around 100 pM. The curve shows a gradual decrease from approximately 98 pM at 0 min to about 68 pM at 7000 min. The filled square symbols, representing experimental data, are scattered around the curve, with error bars indicating variability. 2. A second curve and filled circular symbols representing experimental data and model predictions for an initial ligand concentration around 10 pM. This curve shows a decrease from approximately 10 pM at 0 min to about 3 pM at 7000 min. The filled circular symbols, representing experimental data, are scattered around this lower curve. Figure 3. Ligand depletion base model prediction and experimental data. Intact concentrations of wild-type IL-2 in T cell cultures of density 2.5 × 10⁸ cells per liter. Experimental data (filled symbols) and model predictions (curves) using the base values for IL-2 (Table 1) are indicated. Simulations and experiments were performed at two initial ligand concentrations, as shown (data adapted, ref 37).::>

<a id='ce29e7cd-b707-40b5-9f8f-7b926a645614'></a>

<::chart: The chart, titled "Figure 4. Cell density base model prediction and experimental data," displays T cell densities (Cells per Liter) on the y-axis against Time (min) on the x-axis. The y-axis ranges from 0.E+00 to 1.E+09, and the x-axis ranges from 0 to 8000. Two sets of experimental data points are shown with error bars, along with their corresponding model predictions (curves). The black circles (●) represent T cell densities measured in the presence of 10 pM wild-type IL-2, showing a relatively stable density around 3.E+08 cells/Liter over time, matched by a flat model prediction curve. The black squares (■) represent T cell densities measured in the presence of 100 pM wild-type IL-2, showing an increasing density from approximately 2.5.E+08 to 9.E+08 cells/Liter over time, matched by an upward-sloping model prediction curve. The model predictions use base parameter values shown in Table 1 (data adapted, ref 37).::>

<a id='7dea82a2-4fd2-4764-8667-6de2963036b7'></a>

receptor/ligand complex number (see Figure 2). This functionality predicts negligible growth below a fixed value of Cs, and a relatively constant increase in cell density as long as Cs remains above this value. This behavior is shown clearly in Figure 4, as the higher ligand concentration serves to maintain Cs at a value above the growth response threshold while little proliferation is observed following exposure to an initial IL-2 concentration of 10 pM. Prediction of proliferation behavior during the first 2 days is problematic because during this period the cells are recovering from an imposed quiescence; this means that their specific growth growth rate is transitioning from zero to the empirical "quasi-steady-state" model expression, eq 8, in a manner we are not able to characterize. Thus, our model computations overpredict the cell growth effect during this initial period, but the later ligand depletion effects are not significantly influenced by this difference of less than a factor of 2 in cell number density.

<a id='37c25b8e-bb0d-4274-b730-28769dda65ec'></a>

**Effects of Ligand/Receptor Binding Kinetics.** The model describes a set of interrelated dynamic processes beginning with the ligand–receptor binding interaction at the cell surface. Alterations in the kinetics of binding should thus be expected to influence both the postendocytic ligand turnover rate and the lifetime of cell– surface complexes that signal for both new receptor synthesis and cell proliferation. The effects of altered binding kinetics on the receptor-mediated depletion of

<a id='da528962-f128-4d11-a0a5-7ce46041aedc'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5<::figure: The visual content consists of two line graphs, labeled A and B, depicting the effect of ligand-receptor binding kinetics.

**Graph A: Intact Ligand Concentration (pM) vs. Time (min)**
The y-axis represents Intact Ligand Concentration in pM, ranging from 0 to 10. The x-axis represents Time in minutes, ranging from 0 to 8000. Multiple lines are plotted, starting from 10 pM and decreasing over time. An arrow indicates "Decreasing Off-Rate", showing that lines with slower depletion rates correspond to lower off-rates.

**Graph B: Cell-Surface Complexes (#/cell) vs. Time (min)**
The y-axis represents Cell-Surface Complexes as number per cell, ranging from 0 to 250. The x-axis represents Time in minutes, ranging from 0 to 8000. Multiple lines are plotted, showing an initial rapid increase in complexes followed by a decrease. An arrow indicates "Decreasing Off-Rate", showing how the complex formation and dissociation change with varying off-rates.

Figure 5. Effect of ligand-receptor binding kinetics on ligand depletion at 10 pM ligand concentration. Intact ligand concentrations (A) and cell-surface complex numbers (B) are shown for hypothetical IL-2 analogues with dissociation rate constants (k_d) of 0.138, 0.069, 0.0276, 0.0138, 0.0069, 0.00345, and 0.00138 min⁻¹. The K_D is held constant at the wild-type value of 11.1 pM, and the association rate is adjusted accordingly for each scenario.::>

<a id='b21127e4-4a7d-4e7d-91ae-0e4611c4c928'></a>

ligand at an initial concentration of 10 pM are shown in Figure 5A. Roughly half of the available cell-surface receptors are initially bound at this concentration, since the K_D of the ligand is fixed at 11.1 pM. A decrease in the dissociation rate (and commensurate decrease in the association rate) leads to enhanced stability to endocytic degradation by cells at an initial density of 2.5 × 10^8 per liter. This effect is explained by observing the levels of cell-surface ligand–receptor complexes as illustrated in Figure 5B. Since ligand can undergo depletion only upon receptor binding, heightened levels of C_s lead to greater degradation. Concomitantly, the value of C_s declines more rapidly for greater initial complex numbers. These effects are apparent, though less pronounced when simulations are performed with an initial ligand concentration of 100 pM. Decreased kinetic rate constants slightly improve ligand stability in culture (Figure 6A). Cell-surface complex numbers rapidly reach a steady state under these conditions, and the heightened stability of ligand again correlates with decreased C_s levels (Figure 6B). Available receptors are nearly saturated at this initial concentration, thus the sensitivity of the system relative to small decreases in ligand concentration is diminished.

<a id='57e6866c-c4b0-4d4b-aeef-ccd3bb3d3676'></a>

The predicted growth response of T cells to IL-2
analogues with altered binding kinetics is shown for
initial ligand concentrations of 10 and 100 pM (Figure
7A and B, respectively). As cells deplete ligand, C_s can
fall below the threshold level required to stimulate cell
division. This effect is realized under conditions of low
initial ligand concentration, as shown in Figure 7A. At
an initial IL-2 concentration of 100 pM, C_s never falls
below the minimum value during the 5-day simulation,

<a id='0b1ef4dd-8b15-49a6-a6f7-eb68c341f21c'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='eb94488a-30e2-4835-a6e9-cae591364d68'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='1f718ac1-3567-4b63-b74e-5a911117bdb2'></a>

911

<a id='0a15a4cc-4727-4c23-9c27-b9b90e097767'></a>

<::chart: The image contains two line graphs, labeled A and B. Both graphs share the same x-axis, labeled "Time (min)", ranging from 0 to 8000. An arrow labeled "Decreasing Off-Rate" is present in both graphs, indicating the direction of change for the plotted lines. Figure 6. Effect of ligand—receptor binding kinetics on ligand depletion at 100 pM ligand concentration. Intact ligand concentrations (A) and cell-surface complex numbers (B) are shown for hypothetical IL-2 analogues with dissociation rate constants (k_r) of 0.138, 0.069, 0.0276, 0.0138, 0.0069, 0.00345, and 0.00138 min⁻¹. The K_D is held constant at the wild-type value of 11.1 pM, and the association rate is adjusted accordingly for each scenario. Graph A: This graph shows "Intact Ligand Concentration (pM)" on the y-axis, ranging from 0 to 100. Multiple lines start around 100 pM at Time 0 and gradually decrease over time. The lines diverge, with some decreasing faster than others, following the "Decreasing Off-Rate" arrow. Graph B: This graph shows "Cell-Surface Complexes (#/cell)" on the y-axis, ranging from 0 to 400. Multiple lines show an initial sharp increase from 0, then stabilize or slowly decrease. The lines are distinct, with some maintaining higher complex numbers than others, also following the "Decreasing Off-Rate" arrow.::>

<a id='384a4c5f-9c45-4913-bb81-1a174bc647e3'></a>

and cell growth is thus maintained at a relatively constant rate (Figure 7B). Although depressed binding kinetics lead to enhanced ligand stability, the greater half-life of intact IL-2 does not correspond to increased proliferation in this case. This counterintuitive result illustrates the dual role of cell-surface ligand–receptor complexes: as vehicles for the down-regulation of extra-cellular ligand and as components that stimulate the cell's proliferative response.

<a id='61078101-c08c-4320-ac38-36d530caeae5'></a>

Effects of Endosomal Ligand/Receptor Binding
Affinity. The characteristics of the heterotrimeric IL-2
receptor are unique in that its subunits are subject to
distinct postendocytic sorting outcomes. The a subunit
recycles to the cell surface, while the IL-2/IL-Rβγ complex
is routed to lysosomal degradation (34). Recycling is the
default pathway for membrane-bound components fol-
lowing internalization, implicating a specific endosomal
retention mechanism for the IL-2/IL-Rβγ complex (33, 42,
71). Therefore, upon internalization of the IL-2/IL-2Rαβγ
complex and subsequent dissociation of the a chain,
model predictions of ligand sorting outcomes incorporate
the binding affinity of IL-2 for the βγ complex at endo-
somal pH. The K_D for binding to this complex has been
measured for both wild-type IL-2 and the 2D1 analogue
at cell-surface conditions, as has the pH-sensitivity of the
affinity of these ligands for the α and β chains individu-
ally (37, 79). The effects of changes in this binding affinity
on receptor-mediated ligand depletion are shown for
initial ligand concentrations of 10 and 100 pM (Figure
8A and B, respectively). Cell-surface receptor–ligand
binding affinities are unchanged in these simulations.
Decreasing affinity for the lysosomally routed βγ complex
in endosomes leads predictably to improved stability of
ligand to cell-mediated degradation. The model is insen-

<a id='f7e3d8cb-575a-41f0-a56b-fb262ec175a4'></a>

<::chart: Two line graphs showing the effect of ligand-receptor binding kinetics on cell proliferation. Both graphs plot 'Cells per Liter' on the y-axis against 'Time (min)' on the x-axis. Multiple curves are shown in each graph, representing different dissociation rate constants (kr). An arrow labeled 'Decreasing Off-Rate' points from higher curves to lower curves in both plots. Graph A, for initial ligand concentration of 10 pM, shows cell proliferation curves that increase and then plateau at different maximum cell counts, with higher plateaus corresponding to lower off-rates. The y-axis ranges from 2.5E+08 to 4.5E+08. Graph B, for initial ligand concentration of 100 pM, shows cell proliferation curves that increase approximately linearly over time with different slopes, with higher slopes corresponding to lower off-rates. The y-axis ranges from 2.5E+08 to 1.2E+09. The x-axis for both graphs ranges from 0 to 8000 min. Figure 7. Effect of ligand—receptor binding kinetics on cell proliferation. T cell proliferation in response to hypothetical IL-2 analogues with dissociation rate constants (k_r) of 0.138, 0.069, 0.0276, 0.0138, 0.0069, 0.00345, and 0.00138 min⁻¹ is indicated for initial ligand concentrations of 10 (A) and 100 (B) pM. The K_D is held constant at the wild-type value of 11.1 pM, and the association rate is adjusted accordingly for each scenario.::>

<a id='93ef91d4-cc83-4d27-bbea-b89f9c2c4df6'></a>

sitive to whether ligand is free in the endosome or bound
to IL-2Rα and assumes both entities are routed solely to
recycling.

<a id='224129ce-f974-44e6-9f40-a66ad3e32462'></a>

Cell proliferation is greater in response to ligands exhibiting decreased affinity to the IL-2Rẞγ complex in endosomes. The effects of ligand depletion on cell growth are most apparent for initial ligand concentrations of 10 pM (Figure 9A). Proliferation in the presence of 100 pM ligand is relatively insensitive to the changes in endosomal binding affinity, indicating that Cₛ never falls below the threshold level required for growth in this scenario. As observed in the simulations incorporating altered cell-surface binding kinetics, responses are most sensitive to changes in the levels of stimulatory ligand when its concentration is near the Kᴅ value characterizing the ligand/receptor binding interaction.

<a id='31dd5a1e-5b2b-4fc9-bbc0-723f0ca12a79'></a>

The most important effect, therefore, is that of ligand/
receptor binding properties on the resulting ability of the
cell to maintain signaling ligand/receptor complexes at
levels above the threshold required for mitogenic re-
sponse (see Figure 2). This concept is directly illustrated
by plotting the specific growth rate of a cell population
versus the initial ligand concentration, as ligand/receptor
binding properties are varied. An example of this is
included in Figure 9, which demonstrates that decreasing
the binding affinity of IL-2 for the βγ receptor complex
in the endosomal compartment decreases the IL-2 con-
centration needed for half-maximal cell proliferation
response. Figure 9B illustrates the computational model
predictions, while Figure 9C shows experimental data
comparing the 2D1 analogue with wild-type IL-2.

<a id='bb8f8e8d-46e3-4834-ad84-cd978cbe3f5b'></a>

**Ligand Recycling**. Endosomal sorting forms the mechanistic basis for differences in receptor-mediated

<a id='300a8102-ec84-485e-86ee-5e00e3129ca5'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='4d4d9a44-d3b6-4208-a026-48c0529a080f'></a>

912

<a id='dc261af1-9336-45eb-a6c9-6ef85c600510'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='9b46d121-fd60-41d4-b34d-a514ad8ae6a4'></a>

<::chart: Figure 8. Effect of endosomal binding affinity on ligand depletion. The figure contains two plots, A and B, showing intact concentrations of hypothetical IL-2 analogues over time. Both plots have 'Intact Ligand Concentration (pM)' on the y-axis and 'Time (min)' on the x-axis. Multiple lines are plotted in each graph, representing endosomal dissociation constants (k_re_/k_fe_) of 10, 10², 10³, 3 × 10³, 3 × 10⁴, 3 × 10⁵, and 3 × 10⁶ pM. An arrow in both plots indicates 'Decreasing Affinity in Endosome', pointing towards curves with slower ligand depletion.  Panel A shows ligand concentrations for an initial ligand concentration of 10 pM, with the y-axis ranging from 0 to 10 pM. Panel B shows ligand concentrations for an initial ligand concentration of 100 pM, with the y-axis ranging from 0 to 100 pM. Cell-surface binding affinities are unaltered in this analysis, and the initial cell density is 2.5 × 10⁸ per liter.::>

<a id='c232ab74-cd2a-4c0a-b552-3120b2f62a9e'></a>

ligand depletion. The steady-state sorting behavior of a given ligand can be described by its recycling fraction. A recycling fraction is defined as the ratio of ligand that undergoes postendocytic recycling to all the ligand that leaves the sorting endosome and undergoes either degradation or recycling (72). We have previously determined endosomal sorting outcomes of IL-2 and 2D1 by directly measuring the ratio of intact radiolabeled ligand in the medium to the total radiolabeled ligand during 15-min chase periods after the sorting process reaches steady state (37).

<a id='5e36f008-6cd7-451b-bd79-73a454533898'></a>

We simulated these sorting experiments by computing model predictions over a range of input ligand concentrations for 180 min, at which time sorting reaches steady-state following the initial perturbation due to introduction of extracellular ligand (72, 73). The values of R_s, R_i, C_i, and L_i are recorded and used as inputs into a second simulation wherein these values serve as initial conditions along with zero extracellular ligand concentration (37). Degraded and intact ligand concentrations are recorded throughout this 15-min simulation and used to calculate recycling fractions, or the amount of ligand sorting to recycling vs the amount sorted to degradation. Although these simulations underestimate experimentally observed recycling fractions, they accurately predict increased recycling of 2D1 vs IL-2 at a given intracellular ligand concentration. The model also predicts an increase in recycling as the intracellular ligand concentration increases. This effect has been observed in the EGF system wherein the endosomal retention machinery can become saturated in cells overexpressing the EGF receptor, leading to increased recycling fractions (72, 76).

<a id='1762ba8b-2b4b-4959-81ae-53be43aadbf4'></a>

<::chart: Figure 9: Effect of endosomal binding affinity on cell proliferation and ligand potency.::>Figure 9. Effect of endosomal binding affinity on cell proliferation and ligand potency. T cell proliferation in response to hypothetical IL-2 analogues with endosomal dissociation constants (k_re_/k_fe_) of 10, 10², 10³, 3 × 10³, 3 × 10⁴, 3 × 10⁵, and 3 × 10⁶ pM are shown for initial ligand concentrations of 10 pM (A). Cell-surface binding affinities are unaltered in this analysis. (B) T cell specific growth rate computed during the period of 24–72 h, for the same set of model parameters and conditions. (C) Experimentally measured T cell specific growth rates for wild-type (●) and 2D1 analogue (○) during the period of 24–72 hours (37).

<a id='c7baf55b-1878-4f1e-a566-4e59e2837463'></a>

To more directly compare the experimental results with model predictions, recycling fractions are plotted for a fixed intracellular ligand concentration of 200 per cell (Figure 10A). This illustrates the model's underestimation of the recycling fraction seen experimentally for the 2D1 analogue. The value of K<sub>D</sub> for binding to the IL-2Rβγ complex at endosomal pH has not been measured directly for either wild-type IL-2 or the 2D1 mutein, and this parameter should have tremendous influence on ligand sorting outcomes. Endosomal K<sub>D</sub> was varied over several orders of magnitude, and simulated steady-state sorting experiments were performed. Recycling fractions at a fixed intracellular ligand concentration of 200 per cell are shown in Figure 10B. These results suggest that an order

<a id='ca420be9-099b-4012-b9f3-6d44b4f2621d'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='1fd8af1f-c495-4e21-866a-1b8985f635bf'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='c7fe9fd0-1dd0-4444-90b2-d962f9757498'></a>

913

<a id='3ae56e95-0050-4f81-a511-e21de62552dc'></a>

<::Figure 10: Effect of endosomal K$_{D}$ on sorting. Comparison of modeling results with experimental outcomes at C$_{i}$ = 200 per cell. (A) Bar chart showing Recycling Fraction on the y-axis (ranging from 0 to 50) and two categories on the x-axis: IL-2 and 2D1. There are two bars for each category, representing 'Model' (solid black) and 'Experiment' (gray with horizontal lines). For IL-2, the Model shows a Recycling Fraction of approximately 21, and Experiment shows approximately 28. For 2D1, the Model shows approximately 26, and Experiment shows approximately 48. Endosomal K$_{D}$ values of 1 (IL-2) and 1.6 (2D1) nM were used in obtaining the indicated model predictions. (B) Line graph showing Recycling Fraction on the y-axis (ranging from 0 to 50) and Endosomal K$_{D}$ (pM) on the x-axis (log scale, ranging from 10 to 10^4). The line shows an increasing trend, with data points at approximately: (10 pM, 2), (100 pM, 8), (1000 pM, 21), (2000 pM, 26), (4000 pM, 34), (10000 pM, 46). Results are shown from simulations of steady-state sorting experiments performed using indicated values of the endosomal K$_{D}$ (k$_{re}$/k$_{fe}$). Recycling fractions corresponding to an intracellular ligand concentration (bound + unbound) of 200 per cell are shown.: chart::>

<a id='a6a9203d-ffc8-4ad1-a4c7-a35a44e21290'></a>

of magnitude difference in endosomal binding affinity can account for the relative sorting behavior of IL-2 and the 2D1 variant. This is indeed greater than the factor of 3 difference assumed in the base model. Differences in the pH sensitivity of binding between members of the EGF family of ligands have been shown to directly impact trafficking outcomes in this system (73).

<a id='3d63fefb-6fd4-4500-a1b6-1a75f70bd653'></a>

## Discussion
We have described a computational model that predicts effects of modifications in IL-2/IL-2R binding parameters on the proliferative response of T cells to IL-2, via influence on trafficking dynamics that govern ligand concentration in the extracellular medium and correspondingly the number of ligand/receptor complexes that signal for mitogenesis. The computational results yield insights that resolve the recent counterintuitive finding of the 2D1 IL-2 analogue, which exhibits heightened potency without displaying increased binding affinity to its signaling receptor (37). This behavior is explained mechanistically by changes in the ligand's sorting behavior caused by differential binding affinity to receptor subunits that are routed to either lysosomal degradation or recycling. These results also imply that

<a id='9989c8dc-4436-48ba-a3e0-a0fa3debf145'></a>

the cellular response to a stimulatory ligand cannot be accurately predicted solely on the basis of knowledge of the ligand's receptor binding affinity at the cell surface. Ligands with equivalent affinities but dissimilar kinetics of binding can exhibit differences in both potency and stability to postendocytic degradation according to the model. Furthermore, reduced ligand depletion does not necessarily predict enhanced potency. Increases in cell-surface complex number lead to both greater down-regulation of extracellular ligand and increased proliferation as shown in Figures 5 through 7. Assuming the growth model in Figure 2 holds qualitatively, an optimal ligand would be one that maintains the minimum "threshold" number of signaling complexes required to generate a proliferative response over time. A greater number of complexes than this minimum value leads only to enhanced endocytic down-regulation without heightening the growth response. Since the concentration of active ligand decreases with time, a quantitative understanding of the competing rates of cell growth and postendocytic depletion can thus aid in predicting optimal ligand dosage rates in an in vivo or ex vivo setting. For example, an IL-2 analogue possessing a decreased affinity for the βγ receptor complex in the endosomal compartment is predicted to be more potent for generating a T cell proliferation response (Figure 9B,C), consistent with recent experimental findings (37).

<a id='b2f29b44-1823-4602-a5e9-2d88cdf46ba5'></a>

The model computational results illustrate the strong influence of endocytic sorting outcomes on depletion of ligand from the extracellular medium. Even a subtle increase in recycling fraction of a growth factor mutant greatly extends the analog's half-life over several days in culture, since the ligand is subjected to numerous endocytic cycles during this time. Hence, consideration of endosomal sorting behavior can provide an added level of intervention for protein engineering efforts aimed at improving the potency of regulatory ligands. Although screening for re-engineered cytokine mutants exhibiting altered sorting behavior might appear daunting, the model suggests that "matrix" criteria related to multiple ligand/receptor binding properties within distinct cellular compartments can suffice in fully defining the system (22). For instance, the only differences between IL-2 and its 2D1 analogue are their relative affinities for IL-2R subunits, and the sensitivity of these affinities to pH (see Table 1). These differences cause 2D1 to exhibit a higher recycling fraction than wild-type IL-2, as shown in Figure 10. Therefore, one could potentially screen for IL-2 variants with greater binding affinity for IL-2Rα or reduced affinity for IL-2Rβγ at endosomal pH and expect these variants to display increased recycling fractions relative to wild-type IL-2.

<a id='61c57ac3-4b51-4983-b55d-981a3536d012'></a>

Depletion of stimulatory ligands by cells in culture is an important issue both in tissue engineering applica-tions where the organization of multiple cell types is tightly controlled by extracellular cues and in biotech-nological arenas where optimal feeding conditions in mammalian cell bioreactors are desired (85, 86). Ligand/receptor binding affinities can be readily addressed experimentally through protein engineering and screen-ing technologies, which are becoming increasingly so-phisticated in terms of capability for selection of desired binding properties (87). Thus, the focus of parameter sensitivity analyses in the present work is on these binding interactions both at the cell surface and in sorting endosomes. Although these molecular events can be altered and quantified, it is the translation of these changes into predictable cellular responses that is of greatest interest to the biochemical or tissue engineer.

<a id='cfc46404-72a1-43dc-b80a-d42f36938f7a'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='5b21ee1c-5384-4c8c-ac32-43e60c64ea0d'></a>

914

<a id='8d1388b7-3037-40aa-8094-1a930fc5fa7b'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='258354f8-6c62-41ad-9140-6d906ea0e0d7'></a>

Our objective in developing this model has been not to quantitatively fit experimental data but rather to provide a tool with which one can analyze, interpret, and possibly even predict the dependence of cell-level functional behavior on molecular-level properties. This idea has been raised previously in studies of fibroblast proliferation responses to the EGF family of ligands (35, 36). Our present work advances the impact of this concept in two ways by applying it to the IL-2/IL-2R T cell system. First, it tests the significance of ligand/receptor trafficking effects in a system of strong therapeutic relevance. Second, it extends details of the binding and trafficking model to the class of heteromeric cytokine receptors, which involves interesting additional issues concerning the relationship of ligand/receptor binding processes to endosomal sorting mechanisms with the different receptor subunits. The insights gained here are likely to be useful for understanding and controlling of other cytokine-regulated cell systems, such as that of hematopoietic stem cell proliferation and differentiation (88).

<a id='9a894685-5e87-419b-a988-2142825508b3'></a>

Notation

IL-2 recombinant interleukin-2
IL-2R interleukin-2 receptor
EGF epidermal growth factor
NK natural killer
WT wild-type IL-2.

<a id='cb249e29-9b24-4c14-9e6a-81c766b43644'></a>

# Acknowledgment

We are grateful to Casim Sarkar for critical review of this manuscript, as well as crucial logistical help, and to Steve Wiley, Jason Haugh, and Dane Wittrup for helpful discussions. This work was partially supported by a grant from the NSF Biotechnology Process Engineering Center and an NIH Biotechnology Training Program fellowship (E.M.F.).

<a id='868e4a47-719a-4e0f-a9c5-3837a79b9670'></a>

# References and Notes

(1) Nicola, N. A. *Guidebook to Cytokines and Their Receptors*; Oxford University Press: New York, 1994.
(2) Paul, W. E.; Seder, R. A. Lymphocyte responses and cytokines. *Cell* **1994**, *76*, 241–251.
(3) Trowbridge, I. S. Endocytosis and signals for internalization. *Curr. Opin. Cell Biol.* **1991**, *3*, 634–641.
(4) Cohen, A. M. In *Therapeutic Proteins: Pharmacokinetics and Pharmacodynamics*; Kung, A., Baughman, R., Larrick, J., Eds.; W. H. Freeman and Co.: New York, 1993; pp 165–186.
(5) Metcalf, D.; Nicola, N. A. *The Hemopoietic Colony-Stimulating Factors—From Biology to Clinical Applications*; Cambridge University Press: New York, 1995.
(6) Ono, M. Physicochemical and biochemical characteristics of glycosylated recombinant human granulocyte colony stimulating factor (lenograstim). *Eur. J. Cancer* **1994**, *30A*, S7–S11.
(7) Vial, T.; Descotes, J. Immune-mediated side-effects of cytokines in humans. *Toxicology* **1995**, *105*, 31–57.
(8) Kung, A. H. C.; Baughman, R. A.; Larrick, J. W. *Therapeutic Proteins—Pharmacokinetics and Pharmacodynamics*. W. H. Freeman and Co.: New York, 1993.
(9) Theze, J.; Alzari, P. M.; Bertoglio, J. Interleukin-2 and its receptors: Recent advances and new immunological functions. *Immunol. Today* **1996**, *17*, 481–486.
(10) Smith, K. A. Interleukin-2: inception, impact and implications. *Science* **1988**, *240*, 1169–1176.
(11) Khatri, V. P. et al. Ultra-low dose interleukin-2 therapy promotes a type 1 cytokine profile in vivo in patients with AIDS and AIDS-associated malignancies. *J. Clin. Invest.* **1998**, *101*, 1373–1378.

<a id='bfe5ad69-60d7-4a66-b161-d1c7b3becd71'></a>

(12) Ghezzi, S. et al. Experiences in immune reconstitution. The rationale for interleukin-2 administration to HIV-infected individuals. J. Biol. Reg. Homeos. Ag. 1997, 11, 74-78.
(13) Kinter, A.; Fauci, A. S. Interleukin-2 and human immunodeficiency virus infection: Pathogenic mechanisms and potential for immunologic enhancement. Immunol. Res. 1996, 15, 1-15.
(14) Kovacs, J. A. et al. Controlled trial of interleukin-2 infusions in patients infected with the human immunodeficiency virus. N. Engl. J. Med. 1996, 335, 1350-1356.
(15) Jacobson, E. L.; Pilaro, F.; Smith, K. A. Rational interleukin 2 therapy for HIV positive individuals: daily low doses enhance immune function without toxicity. Proc. Natl. Acad. Sci. U.S.A. 1996, 93, 10405-10410.
(16) Noble, S.; Goa, K. L. Aldesleukin (recombinant interleukin-2)—A review of its pharmacological properties, clinical efficacy and tolerability in patients with metastatic melanoma. Biodrugs 1997, 7, 394-422.
(17) Jeal, W.; Goa, K. L. Aldesleukin (recombinant interleukin-2)—A review of its pharmacological properties, clinical efficacy and tolerability in patients with renal cell carcinoma. Biodrugs 1997, 7, 285-317.
(18) Vlasveld, L. T.; Rankin, E. M. Recombinant interleukin-2 in cancer—basic and clinical aspects. Cancer Treat. Rev. 1994, 20, 275-311.
(19) Whittington, R.; Faulds, D. Interleukin-2: A review of its pharmacological properties and therapeutic use in patients with cancer. Drugs 1993, 46, 446-514.
(20) Anderson, P. M.; Sorenson, M. A. Effects of route and formulation on clinical pharmacokinetics of interleukin-2. Clin. Pharmacokinet. 1994, 27, 19-31.
(21) Smith, K. A. Lowest dose interleukin-2 immunotherapy. Blood 1993, 81, 1414-1423.
(22) Lauffenburger, D. A.; Fallon, E. M.; Haugh, J. M. Scratching the (cell) surface: cytokine engineering for improved ligand/receptor trafficking dynamics. Chem. Biol. 1998, 5, R257-R263.
(23) Bazan, J. F. Structural design and molecular evolution of a cytokine receptor superfamily. Proc. Natl. Acad. Sci. U.S.A. 1990, 87, 6934-6938.
(24) Cosman, D. et al. A new cytokine receptor superfamily. TIBS 1990, 15, 265-270.
(25) Gutgsell, N. S.; Malek, T. R. Formation of high affinity IL-2 receptors is dependent on a nonligand binding region of the α subunit. J. Immunol. 1994, 153, 3899-3907.
(26) Forsten, K. E.; Lauffenburger, D. A. The role of low-affinity interleukin-2 receptors in autocrine ligand binding: alternative mechanisms for enhanced binding effect. Mol. Immunol. 1994, 31, 739-751.
(27) Kuziel, W. A.; Ju, G.; Grdina, T. A.; Greene, W. C. Unexpected effects of the IL-2 receptor α subunit on high affinity IL-2 receptor assembly and function detected with a mutant IL-2 analog. J. Immunol. 1993, 150, 3357-3365.
(28) Nikaido, T. et al. Molecular cloning of cDNA encoding human interleukin-2 receptor. Nature 1984, 311, 631-635.
(29) Sugamura, K. et al. The interleukin-2 receptor gamma chain: Its role in the multiple cytokine receptor complexes and T cell development in XSCID. Annu. Rev. Immunol. 1996, 14, 179-205.
(30) Friedman, M. C.; Migone, T. S.; Russell, S. M.; Leonard, W. J. Different interleukin 2 receptor β-chain tyrosines couple to at least two signaling pathways and synergistically mediate interleukin 2-induced proliferation. Proc. Natl. Acad. Sci. U.S.A. 1996, 93, 2077-2082.
(31) Subtil, A.; Dautry-Varsat, A. Several weak signals in the cytosolic and transmembrane domains of the interleukin-2 receptor-β chain allow for its efficient endocytosis. Eur. J. Biochem. 1998, 253, 525-530.
(32) Morelon, E.; Dautry-Varsat, A. Endocytosis of the common cytokine receptor γ(c) chain—Identification of sequences involved in internalization and degradation. J. Biol. Chem. 1998, 273, 22044-22051.
(33) Subtil, A.; Delepierre, M.; DautryVarsat, A. An α-helical signal in the cytosolic domain of the interleukin 2 receptor β chain mediates sorting towards degradation after endocytosis. J. Cell Biol. 1997, 136, 583-595.

<a id='59f4ad25-5092-464f-9711-8379d86f4d07'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='1f1c220e-aef9-4f7d-9bb5-9cebbe6ee031'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='fdc09d63-1a3c-43e8-963d-f6a2fe16ca43'></a>

915

<a id='6eec902f-0d40-4928-88a1-636b27a69ef2'></a>

(34) Hemar, A. et al. Endocytosis of interleukin 2 receptors in human T lymphocytes: distinct intracellular localization and fate of the receptor ̓, ̖, and ̗ chains. J. Cell Biol. 1995, 129, 55–64.
(35) Reddy, C. C.; Wells, A.; Lauffenburger, D. A. Receptor-mediated effects on ligand availability influence relative mitogenic potencies of epidermal growth factor and trans-forming growth factor ̓. J. Cell. Physiol. 1996, 166, 512–522.
(36) Reddy, C. C.; Niyogi, S. K.; Wells, A.; Wiley: H. S.; Lauffenburger, D. A. Engineering epidermal growth factor for enhanced mitogenic potency. Nature Biotechnol. 1996, 14, 1696–1699.
(37) Fallon, E. M.; Liparoto, S. F.; Lee, K. J.; Ciardelli, T. L.; Lauffenburger, D. A. Increased endosomal sorting of ligand to recycling enhances potency of an interleukin-2 analog. J. Biol. Chem. 2000, 275, 6790–6797.
(38) Robb, R. J. Human T-cell growth factor: purification, biochemical characterization, and interaction with a cellular receptor. Immunobiol. 1982, 161, 21–50.
(39) Smith, K. A. Cell growth signal transduction is quantal. Ann. N.Y. Acad. Sci. 1995, 766, 263–271.
(40) Cantrell, D. A.; Smith, K. A. The interleukin-2 T-cell system: a new cell growth model. Science 1984, 224, 1312–1316.
(41) Herzberg, V. L.; Smith, K. A. T-cell growth without serum. J. Immunol. 1987, 139, 998–1004.
(42) Subtil, A.; Rocca, A.; Dautry-Varsat, A. Molecular charac-terization of the signal responsible for the targeting of the interleukin 2 receptor ̖ chain toward intracellular degrada-tion. J. Biol. Chem. 1998, 273, 29424–29429.
(43) Subtil, A.; Hemar, A.; Dautry-Varsat, A. Rapid endocytosis of interleukin 2 receptors when clathrin-coated pit endocytosis is inhibited. J. Cell Sci. 1994, 107, 3461–3468.
(44) Duprez, V.; Smoljanovic, M.; Lieb, M.; Dautry-Varsat, A. Trafficking of interleukin 2 and transferrin in endosomal fractions of T lymphocytes. J. Cell Sci. 1994, 107, 1289–1295.
(45) Morelon, E.; Hemar, A.; Dautry-Varsat, A. Down-regulation of interleukin-2 ̖ and ̗ chains in human T lymphocytes. Transplant. Proc. 1995, 27, 2477.
(46) Duprez, V.; Ferrer, M.; Dautry-Varsat, A. High-affinity interleukin 2 receptor ̓ and ̖ chains are internalized and remain associated inside the cells after interleukin 2 endocy-tosis. J. Biol. Chem. 1992, 267, 18639–18643.
(47) Duprez, V.; Dautry-Varsat, A. Receptor-mediated endocy-tosis of interleukin-2 in a human tumor T cell line: degrada-tion of interleukin-2 and evidence for the absence of recycling of interleukin receptors. J. Biol. Chem. 1986, 261, 15450–15454.
(48) Forsten, K. E.; Lauffenburger, D. A. Autocrine ligand binding to cell receptors: mathematical analysis of competi-tion by solution ‘’decoys’’. Biophys. J. 1992, 61, 518–529.
(49) Goldstein, B.; Jones, D.; Kevrekidis, I. G.; Perelson, A. S. Evidence for p55–p75 heterodimers in the absence of IL-2 from Scatchard plot analysis. Int. Immunol. 1992, 4, 23–32.
(50) Borisova, L. R.; Kuznetsov, V. A. Structural and kinetic models of interleukin-2 internalization and interaction with a multi-subunit receptor. Chem. Phys. Reports 1996, 15, 117–136.
(51) Borisova, L. R.; Andreev, S. G.; Kuznetsov, V. A. Kinetics of T cell proliferation. A mathematical model and data analysis. Biol Membr. 1998, 15, 90–96.
(52) Burke, M. A. et al. Modeling the proliferative response of T cells to IL-2 and IL-4. Cell Immunol. 1997, 178, 42–52.
(53) Knauer, D. J.; Wiley: H. S.; Cunningham, D. D. Relation-ship between epidermal growth factor receptor occupancy and mitogenic response: quantitative analysis using a steady-state model system. J. Biol. Chem. 1984, 259, 5623–5631.
(54) Starbuck, C.; Wiley: H. S.; Lauffenburger, D. A. Epidermal growth factor binding and trafficking dynamics in fibro-blasts: relationship to cell proliferation. Chem. Eng. Sci. 1990, 45, 2367–2373.
(55) Starbuck, C.; Lauffenburger, D. A. Mathematical model for the effects of epidermal growth factor receptor trafficking dynamics on fibroblast proliferation responses. Biotechnol. Prog. 1992, 8, 132–143.

<a id='3b50ed2c-3ebc-44c3-98c4-ca1758200928'></a>

(56) Wiley: H. S.; Cunningham, D. D. A steady-state model for analyzing the cellular binding, internalization, and degradation of polypeptide ligands. **Cell 1981**, 25, 433-440.
(57) Chang, D. Z.; Wu, Z.; Ciardelli, T. L. A point mutation in interleukin-2 that alters ligand internalization. **J. Biol. Chem. 1996**, 271, 13349-13355.
(58) Smith, K. A.; Cantrell, D. A. Interleukin 2 regulates its own receptors. **Proc. Natl. Acad. Sci. U.S.A. 1985**, 82, 864-868.
(59) Smith, K. A. The interleukin-2 receptor. **Annu. Rev. Cell Biol. 1989**, 5, 397-425.
(60) Wang, H. M.; Smith, K. A. The interleukin-2 receptor: functional consequences of its bimolecular structure. **J. Exp. Med. 1987**, 166, 1055-1069.
(61) Damjanovich, S. et al. Preassembly of interleukin 2 (IL-2) receptor subunits on resting Kit 225 K6 T cells and their modulation by IL-2, IL-7, and IL-15: A fluorescence resonance energy transfer study. **Proc. Natl. Acad. Sci. U.S.A. 1997**, 94, 13134-13139.
(62) Grant, A. J. et al. The interleukin 2 receptor: the IL-2R α subunit alters the function of the IL-2R β subunit to enhance IL-2 binding and signaling by mechanisms that do not require binding of IL-2 to IL-2R α subunit. **Proc. Natl. Acad. Sci. U.S.A. 1992**, 89, 2165-2169.
(63) Hatakeyama, M. et al. Interleukin-2 receptor β chain gene: Generation of three receptor forms by cloned human α and β chain cDNAs. **Science 1989**, 244, 551-556.
(64) Nabholz, M.; Combe, M.; Corthesy, P.; Lowenthal, J.; Gabathuler, R. Interleukin 2 receptor traffic in a murine cytolytic T cell line. **Eur. J. Immunol. 1987**, 17, 783-790.
(65) Lauffenburger, D. A.; Linderman, J. J. Receptors: Models for Binding, Trafficking, and Signaling; Oxford University Press: New York, 1993.
(66) Sorkin, A.; Waters, C. Endocytosis of growth factor receptors. **Bio. Essays 1993**, 15, 375-382.
(67) Trowbridge, I. S.; Collawn, J. F.; Hopkins, C. R. Signal-dependent membrane protein trafficking in the endocytic pathway. **Annu. Rev. Cell Biol. 1993**, 9, 129-161.
(68) Lund, K. A.; Opresko, L. K.; Starbuck, C.; Walsh, B. J.; Wiley: H. S. Quantitative analysis of the endocytic system involved in hormone-induced receptor internalization. **J. Biol. Chem. 1990**, 265, 15713-15723.
(69) Wiley: H. S.; Cunningham, D. D. The endocytic rate constant: a cellular parameter for quantitating receptor-mediated endocytosis. **J. Biol. Chem. 1982**, 257, 4222-4229.
(70) Kurten, R. C.; Cadena, D. L.; Gill, G. N. Enhanced degradation of EGF receptors by a sorting nexin, SNX1. **Science 1996**, 272, 1008-1010.
(71) French, A. R.; Lauffenburger, D. A. Intracellular receptor/ligand sorting based on endosomal retention components. **Biotech. Bioeng. 1996**, 51, 281-297.
(72) French, A. R.; Sudlow, G. P.; Wiley: H. S.; Lauffenburger, D. A. Postendocytic trafficking of epidermal growth factor-receptor complexes is mediated through saturable and specific endosomal interactions. **J. Biol. Chem. 1994**, 269, 15749-15755.
(73) French, A. R.; Tadaki, D. K.; Niyogi, S. K.; Lauffenburger, D. A. Intracellular trafficking of epidermal growth factor family ligands is directly influenced by the pH sensitivity of the receptor/ligand interaction. **J. Biol. Chem. 1995**, 270, 4334-4340.
(74) Schiff, J. M.; Fischer, M. M.; Joner, A. L.; Underdown, B. J. Human IgA as a heterovalent ligand: switching from the asialoglycoprotein receptor to a secretory component during transport across the rat hepatocyte. **J. Cell Biol. 1984**, 102, 920-931.
(75) Waldmann, T. A. The multisubunit interleukin-2 receptor. **Annu. Rev. Biochem. 1989**, 58, 875-911.
(76) French, A. R.; Lauffenburger, D. A. Controlling receptor/ligand trafficking: effects of cellular and molecular properties on endosomal sorting. **Ann. Biomed. Eng. 1997**, 25, 690-707.
(77) Robb, R. J.; Munck, A.; Smith, K. A. T cell growth factor receptors: quantitation, specificity, and biological relevance. **J. Exp. Med. 1981**, 154, 1455-1474.

<a id='d55805a4-59e3-4596-a109-a2cb957a6ab3'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='3e2df9a6-4d18-4cbf-a2b0-267bb264d805'></a>

916

<a id='1ca2d2be-42b5-4736-a685-4b34ec22114b'></a>

Biotechnol. Prog., 2000, Vol. 16, No. 5

<a id='dabf26b2-3947-4dda-9602-439a62f1d2a6'></a>

(78) Robb, R. J.; Greene, W. C.; Rusk, C. M. Low and high affinity cellular receptors for interleukin2. Implications for the level of Tac antigen. J. Exp. Med. 1984, 160, 1126-1146.
(79) Berndt, W. G.; Chang, D. Z.; Smith, K. A.; Ciardelli, T. L. Mutagenic analysis of a receptor contact site on interleukin-2: preparation of an IL-2 analogue with increased potency. Biochemistry 1994, 33, 6571-6577.
(80) Hemar, A.; Lieb, M.; Subtil, A.; DiSanto, J. P.; Dautry-Varsat, A. Endocytosis of the β chain of interleukin-2 receptor requires neither interleukin-2 nor the γ chain. Eur. J. Immunol. 1994, 24, 1951-1955.
(81) Depper, J. M. et al. Interleukin-2 (IL-2) augments transcription of the IL-2 receptor gene. Proc. Natl. Acad. Sci. U.S.A. 1985, 82, 4230-4234.
(82) Duprez, V.; Cornet, V.; Dautry-Varsat, A. Down-regulation of high affinity interleukin 2 receptors in a human tumor T cell line: interleukin 2 increases the rate of surface receptor decay. J. Biol. Chem. 1988, 263, 12860-12865.
(83) Ward, D. M.; Ajioka, R.; Kaplan, J. Cohort movement of different ligands and receptors in the intracellular endocytic pathway of alveolar macrophages. J. Biol. Chem. 1989, 264, 8164-8170.

<a id='8ee36d4c-72f0-4957-aefa-a10d083c4ebf'></a>

(84) Ghosh, R. N.; Gelman, D. L.; Maxfield, F. R. Quantification of low-density lipoprotein and transferrin endocytic sorting in HEP2 cells using confocal microscopy. *J. Cell Sci.* **1994**, 107, 2177–2189.
(85) Saltzman, W. M. Growth-factor delivery in tissue engineer- ing. *MRS Bull.* **1996**, 21, 62–65.
(86) Zandstra, P. W.; Petzer, A. L.; Eaves, C. J.; Piret, J. M. Cellular determinants affecting the rate of cytokine depletion in cultures of human hematopoietic cells. *Biotech. Bioeng.* **1997**, 12, 909–914.
(87) VanAntwerp, J. J.; Wittrup, K. D. Fine affinity discrimina- tion by yeast surface display and flow cytometry. *Biotechnol. Prog.* **2000**, 16, 31–37.
(88) Eaves, C.; Miler, C.; Conneally, E.; Audet, J.; Oostendorp, R.; Cashman, J.; Zandstra, P.; Rose-John, S.; Piret, J.; Eaves, A. Introduction to stem cell biology in vitro: threshold to the future. *Ann. N.Y. Acad. Sci.* **1999**, 30, 1–8.

Accepted for publication August 7, 2000.

ΒΡ000097T

<a id='8ac40ef2-fed1-45a5-99f2-2d8823e84817'></a>

CORRECTIONS

<a id='2c0e3b5c-d7aa-4708-b988-0c1a5225ca76'></a>

DEVELOPMENT AND QUALIFICATION OF A
NOVEL VIRUS REMOVAL FILTER FOR CELL
CULTURE APPLICATIONS

<a id='d6973514-e8e5-4911-b75b-745e4f29d20c'></a>

Shengjiang Liu, Mark Carroll, Raquel Iverson,
Christine Valera, Joann Vennari, Kimberly Turco,
Robert Piper, Robert Kiss, and Herbert Lutz

<a id='7a0e1946-e972-428b-b54e-d93aca1eb044'></a>

2000, Volume 16, pages 425–434. Subsequent to the
publication of the original article, an error was discovered
in the label for the y-axis of Figure 13. The viable cell
density is correctly expressed as 10⁵/mL rather than
10⁶/mL. The correct figure is shown below.

<a id='6e03c448-c896-4285-b6f5-0fc9ab5b59b0'></a>

Growth by Hemacytometer Cell Counts<::chart: A line graph titled "Growth by Hemacytometer Cell Counts" shows Viable Cells (10^5/mL) on the logarithmic y-axis, ranging from 1 to 100, against Time (hours) on the x-axis, ranging from 0 to 500. The graph displays three stages of cell growth, both unfiltered and VBF filtered. The legend indicates: unfiltered stage 1 shown as ●, unfiltered stage 2 shown as ■, unfiltered stage 3 shown as ▲, VBF filtered stage 1 shown as O, VBF filtered stage 2 shown as □, and VBF filtered stage 3 shown as Δ.::>Figure 13. Growth comparison on viable cell number basis for inoculum and production stages.

<a id='ac4a6efc-c359-4765-a40c-f5b6e4809f69'></a>

BP9902934
Published on Web 08/04/2000

<a id='efa955e5-8dcf-4521-bab5-4b6a6386cf9a'></a>

15206033, 2000, 5, Downloaded from https://aiche.onlinelibrary.wiley.com/doi/10.1021/bp000097t by Universita Di Trento, Wiley Online Library on [22/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
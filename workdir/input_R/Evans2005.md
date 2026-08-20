<a id='93323ece-31de-410e-9e7f-b1cc2efe2a2b'></a>

INTERNATIONAL JOURNAL OF ADAPTIVE CONTROL AND SIGNAL PROCESSING
Int. J. Adapt. Control Signal Process. 2005; 19:395-417
Published online 6 January 2005 in Wiley InterScience (www.interscience.wiley.com) DOI:10.1002/acs.856

<a id='c5495e5b-c183-431c-abfb-2ecae638fbc3'></a>

Compartmental modelling of the uptake kinetics of the
anti-cancer agent topotecan in human breast cancer cells

<a id='2e038587-0b04-418e-814c-28fa028199bb'></a>

Neil D. Evans¹*,†, Rachel J. Errington², Michael J. Chapman³, Paul J. Smith⁴,
Michael J. Chappell¹ and Keith R. Godfrey¹

<a id='9c8d2237-b257-4997-80d9-16e3dffcf120'></a>

¹ *School of Engineering, University of Warwick, Coventry CV4 7AL, U.K.*
² *Department of Medical Biochemistry, University of Wales College of Medicine, Cardiff CF14 4XN, U.K.*
³ *School of MIS-Mathematics, Coventry University, Coventry CV1 5FB, U.K.*
⁴ *Department of Pathology, University of Wales College of Medicine, Cardiff CF14 4XN, U.K.*

<a id='f76e520a-f24a-46d6-919a-33162f959e9c'></a>

# SUMMARY
A compartmental model for the _in vitro_ uptake kinetics of the anti-cancer agent topotecan is proposed. This model provides a description of the activity of the drug, and subsequent delivery of active form to the nuclear DNA target. The unknown model parameters are estimated from two-photon laser-scanning microscopy data, which provide concentrations of topotecan (active plus inactive forms) in the extracellular region containing live human breast tumour cells (MCF-7 cell line), the cytoplasm and the nucleus. This determines an output structure for which the model is uniquely identifiable, that is, the unknown parameters are uniquely determined from noise-free, continuous and perfect data. The model allows _in silico_ predictions of the dose dependence of target binding. Copyright  2005 John Wiley & Sons, Ltd.

<a id='335595e7-2949-4f37-82ee-2b528f14cc26'></a>

KEY WORDS: compartmental models; identifiability; topotecan; drug kinetics; heterogeneity

<a id='54f830b3-cc9c-46d2-92c8-58c59d35a38d'></a>

## 1. INTRODUCTION

Topotecan (TPT) is a water-soluble derivative of Camptothecin (CPT) [1-3], an extract from the Chinese tree *Camptotheca acuminata* [1,2]. CPT has been found to act as a specific and reversible poison of the DNA enzyme topoisomerase I [4]. TPT has been approved for clinical use against ovarian and small cell lung carcinomas.

<a id='60059c16-9be5-4ffc-81a6-06b146220331'></a>

Topoisomerase I is a cellular enzyme that alleviates supercoiling in DNA by cleavage and re-ligation of one strand of the double-stranded DNA (dsDNA) [1,2,5, 6]. TPT targets topoisomerase I [5] and acts to trap it in a reversible ternary complex with DNA. It has been

<a id='d0471fb2-3db3-493d-a90b-541936eb1bf7'></a>

*Correspondence to: Neil D. Evans, School of Engineering, University of Warwick, Coventry CV4 7AL, U.K.
† E-mail: neil.evans@warwick.ac.uk

<a id='01ad1ff6-29c0-4e75-8046-a3fd121fb2d3'></a>

Contract/grant sponsor: Engineering and Physical Sciences Research Council of the U.K.; contract/grant number: GR/
M11943, GR/R70354
Contract/grant sponsor: Association for International Cancer Research

<a id='22c638c5-ddf0-461e-8176-cae3ad8d265c'></a>

Copyright  2005 John Wiley & Sons, Ltd.

<a id='4f9214a9-0771-49ea-81b5-a9ef1f61ad6e'></a>

Received 13 October 2004
Accepted 13 October 2004

<!-- PAGE BREAK -->

<a id='6c5b1a2d-5227-4303-b33f-b77362c8376d'></a>

396

<a id='5799d113-4bce-4fee-a9c4-b6d1f5c53976'></a>

N. D. EVANS ET AL.

<a id='be467609-4f9a-4db3-9ef2-affb8b7b7338'></a>

conjectured that collision between this complex and the DNA replication machinery results in dsDNA breaks, which result in cell death [3, 4, 6].

<a id='d4f30bd3-d0c3-42f1-900d-333fd61f8d68'></a>

The parent, ring-closed, lactone form (TPT-L) undergoes reversible hydrolysis to an open-ringed hydroxy acid form (TPT-H). The hydrolysis is pH-dependent, with the lactone form predominating at low pH (<4), and the hydroxy acid form at high pH (>10). It is TPT-L that is pharmacologically active, being responsible for maintenance of the TPT-topoisomerase I-DNA complex, and DNA binding [7, 8].

<a id='bd14dd0f-9677-48f7-9dc2-4658abd9baa5'></a>

In Reference [9] the reversible hydrolysis of TPT-L was modelled using a simple two compartment linear model, with the parameters estimated from high performance liquid chromatography (HPLC) data in buffers at different pH. This linear model was used as the basis for a five compartment non-linear model describing the uptake kinetics of TPT in a medium containing human lymphoma cells (SU-DHL-4 cell line). The non-linear model represents the kinetics of TPT in the whole population of cells, with parameters estimated from HPLC data.

<a id='5a4f3100-bbb4-4d60-ae17-7d904113b257'></a>

Topotecan is naturally fluorescent; it is an agent which can be excited using ultra-violet wavelengths (350–360 nm) and detected at a visible wavelength (peak emission at 540 nm). This is routinely used to quantify the amount of drug in cellular extracts [9] and human plasma by HPLC [10]. TPT exhibits a high two-photon absorption cross-section, a key property that has been elegantly applied in spectroscopy studies to determine the binding characteristics of drug to DNA [8]. In the current study the delivery and localization of the drug in single living cells is monitored using two-photon laser scanning microscopy. The optical sectioning capacity of this approach provides high-resolution spatial information depicting the compartmentalization of fluorescence intensity and hence topotecan concentration in the extra-cellular environment, the cell cytoplasm and the cell nucleus. Analysis of time-lapse sequences allows extraction of the unique drug kinetics for each sub-compartment, which provides the fundamental data for mathematical modelling and simulation.

<a id='6d6bcdf2-46f6-45fb-ac21-62b1c28ab96b'></a>

The microscopy experiments used to collect the data for parameter estimation impose an output structure on the postulated model, which consists of functions of the model variables that are directly measured. It is essential therefore, in order to obtain meaningful parameter estimates from the proposed experimental data, to verify that the output structure uniquely determines the unknown parameters in the postulated model [11]. Should this not be the case, it may prove necessary to examine the possibility of redesigning the experiment to obtain an output structure that does (uniquely determine the parameters). Hence a structural identifiability analysis [12-14] is a prerequisite to experiment design, system identification and parameter estimation.

<a id='32c8d911-c535-4d07-b089-8e7b425e7ba4'></a>

2. MATHEMATICAL MODEL

The compartmental model derived by Evans et al. [9, 15] is extended to allow for mixing in the medium by separating the medium into two separate pools: the medium environment into which the drug is added and a separate extracellular region in which the cells are located. It is only from this latter (extracellular) region that drug may enter the cells, and drug passing from the cells enters this region first. The cellular pool, comprising all of the individual cells, is divided into the cytoplasm and nucleus. This leads to a model with four experimental regions: the medium (denoted by subscript m), the extracellular region (denoted by subscript e), the cytoplasm (denoted by subscript c) and the nucleus (denoted by subscript n).

<a id='a680c202-8273-4c2f-87be-35c0d318cd69'></a>

Copyright  2005 John Wiley & Sons, Ltd.

<a id='3078f69f-0a4b-4182-8cb7-5cb9eac7ea6c'></a>

Int. J. Adapt. Control Signal Process. 2005; 19:395–417

<a id='190a029a-0a68-4c83-b50d-be0a1e938975'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='fa889f72-567e-4c4a-ae85-6fc00d1f9133'></a>

COMPARTMENTAL MODELLING

<a id='f45f667b-8b6d-49ef-94ba-13cb23b311d3'></a>

397

<a id='2f028401-653e-42be-a54c-9c3e41f9a6c0'></a>

A schematic of the extended compartmental model is shown in Figure 1, where _L_ and _H_ denote the concentrations of TPT-L and TPT-H, respectively, _L_m(_t_), _L_e(_t_), _L_c(_t_), _L_n(_t_) denote the concentrations, at time _t_ following administration of drug, of TPT-L in the medium, extracellular region, cytoplasm and nucleus; the corresponding variables for TPT-H are _H_m(_t_), _H_e(_t_) and _H_c(_t_). It is assumed, as in References [9, 15], that all drug in the nucleus is bound, and that only TPT-L binds to DNA. This is a simplification of the real situation in which the nucleus may contain unbound drug, and this assumption requires further experimental investigation.

<a id='422de817-be19-42f3-a9c0-738b5c271655'></a>

In each of the experimental pools, except the nucleus (in which all drug is assumed bound—see below), TPT undergoes reversible hydrolysis, which is pH dependent and can be modelled using a linear two compartment model [9]. Assuming no heterogeneity in pH across the medium and extracellular region, or in any other factors that might affect the hydrolysis, the rate constants are $k_{om}$ for the ring opening of TPT-L, and $k_{cm}$ for the ring closing for TPT-H, in both pools. The corresponding rate constants for the cytoplasm are $k_{oc}$ and $k_{cc}$.

<a id='5672b341-8f9b-4ae1-837f-3c97719535e3'></a>

Mixing between the medium and extracellular pools is modelled via first-order flows between them. It is assumed that the corresponding rate constants are the same for TPT-L and TPT-H, being kmi for flow from medium into extracellular region, and kmo for flow out of extracellular region into medium.

<a id='a71a938f-cfe9-4137-a984-b8970c2496b3'></a>

Flow between the extracellular region and cytoplasm is similarly modelled as first-order processes, but only TPT-L crosses the plasma membrane. This is consistent with previous observations and the physical properties of the hydroxy acid form with respect to the lipid bilayer traverse [16]. The rate constant for the influx of extracellular TPT-L into the cytoplasm is kᵢ, and the rate constant for the efflux of cytoplasmic TPT-L into the extracellular region is kₑ.

<a id='9ddf7e01-748f-4228-a9f3-50db474bddd9'></a>

The rate at which TPT-L binds to DNA is assumed to be proportional, with constant k_b, to the product of the concentrations of TPT-L in the cytoplasm, L_c(t), and free binding sites, B_F(t). If B_T denotes the total concentration of available DNA binding sites, then the concentration of free sites is the difference between B_T and the concentration of bound drug, namely L_n(t), that is B_F(t) = B_T - L_n(t). Dissociation of bound drug is assumed to occur at a first-order rate as either TPT-L, with rate constant k_dl, or TPT-H, with rate constant k_dh. The latter is motivated by the

<a id='bc146057-f533-4c62-83ac-95ee3923fd03'></a>

<::schematic diagram::>The diagram illustrates a three-compartment model representing the uptake kinetics of TPT. The main compartments are 'Medium', 'Extracellular region', and 'Cell'. The 'Cell' compartment further contains a 'Nucleus' sub-compartment. Each compartment contains two states, labeled 'L' (top circle) and 'H' (bottom circle), except for the Nucleus which contains 'L_n'.

**Medium Compartment:**
- 'Dose' enters the 'L_m' state.
- 'L_m' and 'H_m' interconvert with rate constants 'k_cm' (L_m to H_m) and 'k_om' (H_m to L_m).
- 'L_m' flows to 'L_e' in the Extracellular region with rate constant 'k_mi'.
- 'H_m' flows to 'H_e' in the Extracellular region with rate constant 'k_mi'.
- 'L_e' flows back to 'L_m' with rate constant 'k_mo'.
- 'H_e' flows back to 'H_m' with rate constant 'k_mo'.

**Extracellular Region Compartment:**
- Contains 'L_e' and 'H_e' states.
- 'L_e' and 'H_e' interconvert with rate constants 'k_cm' (L_e to H_e) and 'k_om' (H_e to L_e).
- 'L_e' flows to 'L_c' in the Cell with rate constant 'k_i'.
- 'L_c' flows back to 'L_e' with rate constant 'k_e'.

**Cell Compartment:**
- Contains 'L_c' and 'H_c' states.
- 'L_c' and 'H_c' interconvert with rate constants 'k_cc' (L_c to H_c) and 'k_oc' (H_c to L_c).
- An inner 'Nucleus' compartment contains 'L_n'.
- 'L_c' flows to 'L_n' with rate constant 'k_b B_F(t)'.
- 'L_n' flows back to 'L_c' with rate constant 'k_dl'.
- 'H_c' flows to 'L_n' with rate constant 'k_dh'.
- An equation is provided: 'B_F(t) = B_T - L_n(t)'.

Figure 1. Schematic of the mathematical model used to investigate the uptake kinetics of TPT in a culture medium containing human breast cells (MCF-7 cell line) in suspension.<::>

<a id='b284b5d0-480c-4838-aa6a-91cf4f949914'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='9f287d6b-10bc-40ad-a8db-c832399de0d2'></a>

Int. J. Adapt. Control Signal Process. 2005; 19:395–417

<a id='8b813d29-549e-456b-b923-39b906423f72'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='38c964d0-9442-4aa2-adbb-08713c467d27'></a>

398

<a id='1ce74165-3a3f-4ec0-afa1-8176ad514a89'></a>

N. D. EVANS *ET AL.*

<a id='ec4312ec-d005-4ecd-a3bf-a8e7167c2226'></a>

suggestion in Reference [17] that TPT-L may (reversibly) bind to DNA and then be converted to the hydroxy acid form.

<a id='21cf4293-4302-47e2-913b-21f723e10a2d'></a>

If Vm, Ve, Vc and Vn denote the volumes of the medium, extracellular region, cytoplasm and nucleus, respectively, then the postulated compartmental model for the uptake kinetics of TPT is given by the following system of ordinary differential equations:

<a id='61569dca-125b-4cb9-b5e7-eee65af2d789'></a>

$$\dot{L}_m = -(k_{om} + k_{mi})L_m + k_{cm}H_m + k_{mo}v_0L_e \quad (1)$$
$$\dot{H}_m = k_{om}L_m - (k_{cm} + k_{mi})H_m + k_{mo}v_0H_e \quad (2)$$
$$\dot{L}_e = \frac{k_{mi}}{v_0}L_m - (k_{mo} + k_{om} + k_i)L_e + k_{cm}H_e + \frac{k_e}{v_1}L_e \quad (3)$$
$$\dot{H}_e = \frac{k_{mi}}{v_0}H_m + k_{om}L_e - (k_{cm} + k_{mo})H_e \quad (4)$$

<a id='2f12652e-aa2d-4203-9193-7aa526405702'></a>

L̇c = ki v1 Le − (ke + koc)Lc + kcc Hc + kdl v2 Ln − kb(BT − Ln)Lc                                     (5)
Ḣc = koc Lc − kcc Hc + kdh v2 Ln                                                                     (6)

<a id='eef5f572-6bab-4d49-9c23-4d6d1ea618e4'></a>

$$\dot{L}_n = \frac{k_b}{v_2} (B_T - L_n) L_c - (k_{dl} + k_{dh}) L_n \quad (7)$$

<a id='6040c112-ee4b-44ca-b420-8024e9eec4c8'></a>

where v₀ = Vₑ/Vₘ, v₁ = Vₑ/V𝒸, and v₂ = Vₙ/V𝒸. Time t = 0 corresponds to the (first) administration of drug as a bolus injection. The corresponding initial conditions for the model are
Hₘ(0) = Lₑ(0) = Hₑ(0) = L𝒸(0) = H𝒸(0) = Lₙ(0) = 0 (8)

<a id='7290b63e-99d2-4a35-8324-7a2df6ed2bb5'></a>

together with

Lm(0) = (1 + v0)D                                                     (9)

<a id='01034ee7-9022-4597-bc0a-736d6f969f19'></a>

which gives the total combined concentration of active drug at $t = 0$ in the medium and extracellular region as $(1 + v_0)V_mD/(V_m + V_e) = D$.

<a id='0c991498-3fbf-4abe-aa0e-d161bbbead29'></a>

Evans et al. [9] obtained estimates for the volumes Vc and Vn from data collected from optical sectioning using a confocal microscope. The values obtained are 829 µm3 (SD = 232 µm3) for the average volume of the cytoplasm in a single cell, and 326 µm3 (SD = 85.5 µm3) for the average volume of the nucleus in a single cell. The culture medium has a volume of 2 ml (i.e. 2 &#x00D7; 1012 µm3) and so

<a id='428b4242-c3ed-41d3-b057-60904427e5aa'></a>

Vm + Ve = 2 × 10^12 ⇒ Ve = (2 × 10^12 v0) / (1 + v0) (μm^3)

<a id='c9994d25-2d04-4e61-906b-e13ce24656f7'></a>

Given that the culture medium contains 1 x 10⁵ cells, the cellular volume ratios are therefore given by

<a id='892326c4-fffe-4a4d-8b5b-29d799b9ecf6'></a>

v_1 = V_e / V_c = (v_0 / (1 + v_0)) ( (2 x 10^12) / ((1 x 10^5) x 829) ) = (αv_0) / (1 + v_0)

<a id='02930840-d4d4-426b-9e4e-3c1e119c1382'></a>

where α = 2.4125 × 10⁴, and v₂ = Vₙ/Vₐ = 326/829 = 3.9324 × 10⁻¹. Due to factors such as intracellular protein binding the actual cellular volume estimated here may not reflect the apparent volume of distribution.

<a id='2f88c2fd-38f3-4bfe-b28b-37061381df5a'></a>

Copyright  2005 John Wiley & Sons, Ltd.

<a id='761e59cb-9e20-4fea-a879-f5e24dd62877'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**: 395–417

<a id='600060c3-4dab-4620-bf25-df3712cb5ec6'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='42474ec8-6e79-476b-9960-211632f3a979'></a>

COMPARTMENTAL MODELLING

<a id='e4bc1abc-ad1b-4f12-af8b-0fcaba9f2e5d'></a>

399

<a id='64ffcd30-70df-4587-8ad9-3a1a59c08d36'></a>

Experimental data of the hydrolysis of TPT in buffers with different pH were used by Evans et al. [9] to obtain values for the corresponding rate constants against pH. In the experiments used to collect data for parameter estimation in this paper, the cells are seeded in a medium with pH 7.2. Assuming that the hydrolysis rate constants are primarily dependent on pH the corresponding values from [9] are used; these values are k_om = 1.5599 x 10^-4 s^-1 (9.3594 x 10^-3 min^-1) and k_cm = 2.9553 x 10^-4 s^-1 (1.7732 x 10^-2 min^-1).

<a id='a1f90be6-536c-4ace-b4db-5fcaefeae119'></a>

In the experiment used to collect data for parameter estimation, time is measured in seconds, concentrations are measured in µM and the initial dose D = 10 µM.

<a id='d6ddec1f-1332-41be-9209-df3b43c476e0'></a>

3. STRUCTURAL IDENTIFIABILITY
Before using the experimental data to estimate the unknown model parameters, it is first necessary to test that the output structure determined by the proposed experiments uniquely determines these parameters. Consider a postulated parametric model given by

<a id='f4391e91-39a6-424c-87d0-fbdeaabb22fc'></a>

x(t, p) = f(x(t, p), p)                                       (10)
x(0, p) = xo(p)                                                (11)

<a id='f1592ced-f136-4a2b-a400-76096a6971a4'></a>

where **p** = (p₁, ..., p_q)ᵀ is a vector comprising the unknown model parameters which lies in some open set Ω of feasible vectors; the state vector is **x**(_t_, **p**) = (_x_₁(t, **p**), ..., _x_ₙ(_t_, **p**))ᵀ, where _x_ᵢ(_t_, **p**) are the model variables; _M_**p**) is a connected open subset of Rⁿ such that **x**(_t_, **p**) ∈ _M_**p**) for all _t_≥0, and on this set _f_(·, **p**) is analytic. An experiment is planned in which _r_ (real) linear combinations of the model variables, _c_ᵢ₁(p)_x_₁(t, **p**) + ... + _c_ᵢₙ(p)_x_ₙ(t, **p**) (_i_ = 1, ..., _r_), are measured. This gives rise to the following output structure for the model:

<a id='5a59c92d-ffd8-4471-8a85-09e1cebb2ec3'></a>

y(t, p) = C(p)x(t, p) where C(p) = $$\begin{pmatrix} c_{11}(\mathbf{p}) & \dots & c_{1n}(\mathbf{p}) \\ \vdots & \ddots & \vdots \\ c_{r1}(\mathbf{p}) & \dots & c_{rn}(\mathbf{p}) \end{pmatrix}$$ (12)

<a id='db4b117c-3f02-474b-82ef-78c1d38adca1'></a>

In the experiment, input consists of a single impulse (injection of drug into the system) and so is included in the initial conditions x0(p). There are assumed to be no other external inputs to the model and so no further input terms are included in Equation (10).

<a id='bc31821a-98f2-4139-912d-c17095ee3e29'></a>

Definitions
A model of the form of Equations (10)-(12) is globally identifiable at **p** ∈ Ω if for any **p̄** ∈ Ω,
**y(t, p)** = **y(t, p̄)** for all *t* ≥ 0 implies that **p̄** = **p**.

<a id='0521bfd4-c370-4d64-ab17-13ca6cfe1de6'></a>

If there exists a positive real number ε such that for any p̄ ∈ Ω, ||p̄ - p|| < ε and y(t, p) = y(t, p̄)
for all t ≥ 0 implies that p̄ = p then the model, Equations (10)-(12), is locally identifiable at p ∈ Ω.
The model is said to be *structurally globally (locally)* identifiable if it is globally (locally)
identifiable at **p**, for generic **p**.

<a id='aab043a2-228c-46d4-852d-93580b1e0411'></a>

The tutorial paper by Godfrey and DiStefano III [14] provides details of the principal techniques for performing a structural identifiability analysis for linear systems. For non-linear systems, there are comparatively few techniques available, the most frequently used being the Taylor series approach [18] and the similarity transformation approach [19, 20]. The former is

<a id='00cb3b4d-1f22-4297-aae4-234b64c437b2'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='46184b16-8e32-48e7-bd7d-c540f635a90a'></a>

Int. J. Adapt. Control Signal Process. 2005; 19: 395–417

<a id='a415dd87-3762-4aa0-a4d4-065ce2abae37'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='c05f0800-e7c0-49b9-9667-28fb25b831bc'></a>

400

<a id='b98d0738-39b9-4090-ad09-aad05790f3d3'></a>

N. D. EVANS ET AL.

<a id='c615e5eb-5dde-4537-8d91-822caaf2c4fb'></a>

applicable to models of systems where the drug is administered via a bolus injection, and is applied by expanding the output as a Taylor series around t = 0 [18]. It can prove to be quite difficult computationally to show that a system is unidentifiable using the Taylor series approach, since it must be shown that a sufficient number of coefficients of the expansions have been considered. The method introduced by Evans et al. [21], which requires an observability criterion to be satisfied, can sometimes more readily show that a system is unidentifiable.

<a id='000b84e5-8829-473d-bf10-fa3b2ce4d468'></a>

The Taylor series approach is used, in the next section, to show that the model (1)-(9) is structurally globally identifiable. Since the coefficients in the Taylor series expansion of the output are unique, the approach reduces to that of determining whether different parameters can give rise to the same coefficients. Consider the following Taylor series expansions of the components of the output, y(t, p), about t = 0:

<a id='7c6454a6-95ed-44f7-ba4c-44869ba87788'></a>

y_i(t, p) = y_i(0, p) + t y_i^(1)(0, p) + (t^2 / 2!) y_i^(2)(0, p) + ... + (t^k / k!) y_i^(k)(0, p) + ... i = 1,...,r

<a id='e486dbcd-d87b-40b5-ad2c-fdfc6e3d60a5'></a>

where

<a id='d371ae39-b74f-4aa5-a627-8ab0ea72e368'></a>

$$y_i^{(k)}(0, \mathbf{p}) = \lim_{\tau \to 0^+} \frac{d^k y_i}{d\tau^k}(\tau, \mathbf{p}), \quad i = 1, 2, 3, \ldots$$

<a id='72169597-c58c-4760-9841-4b9f0d4628d2'></a>

Uniqueness of the coefficients in the expansions implies that if p̄ ∈ Ω is such that y(t, p) = y(t, p̄)
for all t≥0, then for each i = 1,...,r

<a id='ace8374a-b1df-474f-9890-131ac6388cf4'></a>

y_i^{(k)}(0, \mathbf{p}) = y_i^{(k)}(0, \bar{\mathbf{p}}) \text{ for all } k = 0, 1, 2, 3, \dots (13)

<a id='6e46817a-66f2-4011-a210-d9f5790996f2'></a>

where yᵢ⁽⁰⁾(0, **p**) = yᵢ(0, **p**). Model (1)–(9) is structurally globally identifiable if, for generic **p** ∈ Ω, the only **p̄** ∈ Ω satisfying (13) (for each *i* and all *k*) is **p̄** = **p**.

<a id='688ba223-c0a1-401d-bbc3-9f83f822ffa2'></a>

## 4. STRUCTURAL IDENTIFIABILITY ANALYSIS OF THE MODEL

In this section, the Taylor series approach is applied to the model described by Equations (1)–(7) with initial conditions given in Equations (8) and (9).
The vector **p** comprising the eleven unknown parameters of the model is given by

<a id='4851582f-23d5-4567-ad6b-95775c377fa8'></a>

p = (kmi, kmo, ki, ke, koc, kcc, kb, kdl, kdh, BT, v0)ⁿ

<a id='af1fd502-5f3f-4226-bc71-06cf81e34c70'></a>

Since each of the model parameters is positive, the set of admissible parameter vectors, Ω, consists of those vectors $(p_1,...,p_{11})^{\text{T}}$ such that $p_i > 0$ $(1\le i\le 11)$. The state vector $\mathbf{x}(t, \mathbf{p})$ is given by

<a id='75d7edeb-c3de-4ee6-b734-f5703b03034f'></a>

$\mathbf{x}(t, \mathbf{p}) = (L_m(t, \mathbf{p}), H_m(t, \mathbf{p}), L_e(t, \mathbf{p}), H_e(t, \mathbf{p}), L_c(t, \mathbf{p}), H_c(t, \mathbf{p}), L_n(t, \mathbf{p}))^T$
and the set $\mathbf{M}(\mathbf{p})$ is taken to be $\mathbb{R}^7$. The output function is given by

<a id='8977c77a-6dd5-497c-b551-af8c0fbcea79'></a>

y(t, \mathbf{p}) = (L_e(t, \mathbf{p}) + H_e(t, \mathbf{p}), L_c(t, \mathbf{p}) + H_c(t, \mathbf{p}), L_n(t, \mathbf{p}))^{\top}\n\n(14)\nthus, in terms of Equation (12), the output matrix C($\mathbf{p}$) is given by\n\n$\mathbf{C}(\mathbf{p}) = \begin{pmatrix} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix}$

<a id='21a6fb02-f975-4da8-a62d-39b07a06288c'></a>

Copyright  2005 John Wiley & Sons, Ltd.

<a id='b77b2928-b091-4e8d-85bc-5db26b1f64ec'></a>

Int. J. Adapt. Control Signal Process. 2005; 19:395–417

<a id='12e67282-d3d7-431e-9689-5fc2d7849f50'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='0a344bb3-50d9-418f-ba7a-80d1673019ad'></a>

COMPARTMENTAL MODELLING

<a id='44fa9260-a607-4ea2-8677-67573c29caa6'></a>

401

<a id='9bfa2690-712a-43c8-a7f1-214a21784358'></a>

The initial condition for the state space description of the model is given by
x₀(p) = ((1 + v₀)D, 0, 0, 0, 0, 0, 0)ᵀ

<a id='ac740a45-be50-443d-aa70-72bf9d47f36a'></a>

where $D$ is the known dose.
Let $\mathbf{p}$ denote an arbitrary parameter vector:
$\mathbf{p} = (k_{mi}, k_{mo}, k_i, k_e, k_{oc}, k_{cc}, k_b, k_{dl}, k_{dh}, B_T, v_0)^T$

<a id='b5001503-bde7-4930-8390-92e8de1ec451'></a>

such that y(t, p) = y(t, p̅) for all t≥0. To apply the Taylor series approach, successive coefficients of the Taylor series expansions of the components of y(t, p) and y(t, p̅) are equated to determine relations between p and p̅. These coefficients become increasingly complicated and cumbersome, which necessitates the use of a computer algebra system such as MATHEMATICA [22] or MAPLE [23]. The former was used to perform the following analysis (see Appendix A), while the latter was used independently to verify the results.

<a id='6edc092b-f2ad-45f1-bd16-515b95c65238'></a>

Setting $k = 0$ in Equation (13), for $i = 1, 2$ and $3$, yields no information since each of these coefficients is $0$. For $k = 1$, Equation (13) ($i = 1, 2$ and $3$) gives

<a id='8629d4a1-7662-4cd9-b5de-30e02e3e2e16'></a>

k̄_mi = k_mi(1 + v_0)v̄_0 / (1 + v̄_0)v_0
(15)

<a id='9954b495-0154-483e-b463-81534c5002c7'></a>

Now considering the next derivative (k = 2), and using the relation in Equation (15), yields

<a id='9059b3e1-633d-49b0-846d-62bc4f9a599c'></a>

$\bar{k}_{mo} = k_{mo} + \frac{k_i(\bar{v}_0 - v_0)}{\bar{v}_0(1 + v_0)} + \frac{k_{mi}(v_0 - \bar{v}_0)}{v_0(1 + \bar{v}_0)}$ and $\bar{k}_i = \frac{k_i v_0(1 + \bar{v}_0)}{(1 + v_0)\bar{v}_0}$ (16)

<a id='651b50b5-9e83-4423-9333-7bd0e9cfa172'></a>

From the next set of coefficients in the Taylor series expansions (k = 3), and using the relations in Equations (15) and (16) it follows that:

<a id='6c1c9299-317b-480e-ac21-3ea2408f72db'></a>

k_b bar = B_T k_b / B_T bar, k_e bar = k_e and v_0 bar = v_0

<a id='5f97433d-1347-46d6-958f-8d9b62f396e5'></a>

Considering all of these relations between the parameters in **p** and **p̄** together it is found that, for Equation (13) to be satisfied for each *i* and *k* = 0,..., 3, the following relationships must hold:

<a id='d6e9e3c6-6bbd-4cad-bc54-697cd87d6406'></a>

$\bar{k}_{mi} = k_{mi}$, $\bar{k}_{mo} = k_{mo}$, $\bar{k}_i = k_i$, $\bar{k}_b = \frac{B_T k_b}{B_T}$, $\bar{k}_e = k_e$ and $\bar{v}_0 = v_0$ (17)

<a id='9982fa99-90d4-49de-8496-563919da6160'></a>

Equating the fourth derivative terms ($k = 4$), and using the relations in Equation (17), gives

$\bar{k}_{dl} = k_{dl} + k_{dh} - \bar{k}_{dh}$ and $\bar{k}_{oc} = k_{oc}$ (18)

<a id='d0d13efe-3656-4323-9d48-3cc9f53b5774'></a>

From the next set of coefficients in the Taylor series expansions (_k_ = 5), and using the relations in Equations (17) and (18), it follows that:

$\bar{k}_{cc} = k_{cc} + \frac{B_T k_b (\bar{k}_{dh} - k_{dh})}{k_{oc}}$ (19)

<a id='9caaeeba-3c0d-43c6-a782-90353947bd24'></a>

Finally, equating the seventh set of coefficients in the Taylor series expansions (k = 6), and using the relations in Equations (17)–(19), yields

<a id='71889250-709c-4bda-a460-de44c53c3513'></a>

$\bar{k}_{dh} = k_{dh} \quad \text{and} \quad \bar{B}_T = B_T$

<a id='d320b042-ff9a-4475-a850-030e56a746d5'></a>

Therefore, for Equation (13) to be satisfied, it is necessary that
k̄_mi = k_mi, k̄_mo = k_mo, k̄_i = k_i, k̄_e = k_e, k̄_oc = k_oc, k̄_cc = k_cc, k̄_b = k_b

<a id='1b1300e1-e469-4df9-ac9c-792df76848df'></a>

$\bar{k}_{dl} = k_{dl}$, $\bar{k}_{dh} = k_{dh}$, $\bar{B}_T = B_T$ and $\bar{v}_0 = v_0$ (20)

<a id='805363d3-24a3-40ec-8d81-a2466472fa36'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

Int. J. Adapt. Control Signal Process. 2005; 19:395–417

<a id='aa3965d6-e250-40ca-8c49-a15bf03a5a15'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='e6e3f1e0-6ed7-41fc-a376-70eb18b68821'></a>

402

<a id='b3b2f5f0-37bf-4e6a-873d-b4ee8c44fcb4'></a>

N. D. EVANS ET AL.

<a id='3dec5251-65f7-40da-8216-35b4a7f08590'></a>

that is, p = p. Since this is true for generic p ∈ Ω, the model is structurally globally identifiable, i.e. all of the model parameters are uniquely determined by the output structure corresponding to the experiment performed to collect data for the purpose of parameter estimation.

<a id='d1e5c416-e23c-47af-9905-999298940cc5'></a>

## 5. PARAMETER ESTIMATION

The uptake of topotecan into each cellular compartment was monitored using two-photon laser scanning microscopy. The instrument set-up was calibrated so that the fluorescence response was linear for 0–15 µM topotecan making the conversion from fluorescence intensity (after background subtraction) to drug concentration easy to calculate. The dynamic fluorescent signatures representing concentration of drug were derived from each cellular compartment, including the nucleus, the cytoplasm and the medium. Signal-to-noise (_S/N_) during the uptake assay varied both temporally and spatially during the course of the assay. For these uptake sequences _S/N_ can be considered as _I_m/_I_StDev, where _I_m is mean intensity and _I_StDev represents the standard deviation obtained from each region of interest. Therefore during the course of the entire uptake assay the _S/N_ ranged from 1 to 10. This is a low _S/N_ value, normal for physiological imaging but would be considered inadequate for high resolution microscopy. This is why the signal represents a diffuse pattern in each compartment; a _S/N_ 10-fold greater would be required for this level of detection.

<a id='329dcd96-e9fa-4dd7-9871-2dbd1250265c'></a>

The commercial simulation software package FACSIMILE (MCPA Software, UK), which uses a robust (implicit) numerical integrator, is used to perform the parameter estimation. The optimization routine used to obtain parameter estimates involves the minimization of the weighted least-squares criterion given by

<a id='ab0e841d-1627-4b65-9954-9c42b6b919ab'></a>

$$RSS = \sum_{i=1}^{r} \sum_{j=1}^{N} \frac{(d_i(j) - y_i(t_j))^2}{\sigma_i^2} \quad (21)$$

<a id='e5c75d06-147c-4290-9d6a-39c047e3f1ad'></a>

where yᵢ(tⱼ) is the _i_th model output at the _j_th sampling time (tⱼ), dᵢ(j) is the corresponding experimental data point, and σᵢ is the standard error associated with the data series dᵢ = (dᵢ(1), ..., dᵢ(N)) [24]. The product σᵢ = _eRᵢ_, where _e_ is an estimate of the overall accuracy of the data and _Rᵢ_ is the range for dᵢ, is used in FACSIMILE as an initial estimate for the standard errors. Once parameter estimates have been obtained, the standard deviations of the residuals (dᵢ(j) - yᵢ(tⱼ)) (_i_ = 1, ..., _r_, _j_ = 1,..., _N_) are used in a subsequent stage of parameter fitting as new estimates for the standard errors. This process is continued iteratively. After each stage of fitting a normal probability plot [25] was used to test whether the weighted residuals were normally distributed, with zero mean and standard deviation of 1. Suppose that the residuals are ordered in an ascending list _r_₁ < _r_₂ < ... < _r_₂₇₀, let _zᵢ_ = (_i_ – 0.5)/270 (_i_ = 1,..., 270) and let _Zᵢ_ be the point in the normal cumulative distribution with probability _zᵢ_. If the _Zᵢ_ are plotted against the _rᵢ_, then the resulting approximately linear graph suggests that the residuals are normally distributed. This indicates the appropriateness of the constant standard errors σᵢ for each observation yᵢ.

<a id='e8578965-2c5d-40d0-8c9a-c70b0c43524a'></a>

FACSIMILE works in terms of internal parameters that are the natural logarithms of the model parameters. A statistical analysis is performed during the fitting procedure to detect parameters that are not well-determined by the data (NWD). Once detected the parameter values are fixed and then treated as unknown in subsequent tests. The standard deviation of the natural logarithm (SDLN) of each of the remaining fitted parameters, Pº, is estimated from the

<a id='3ac940d5-8e0f-402d-8c66-afd63b5aa8cf'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='41e99393-3534-48d0-a1ff-ea69195ac8e4'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**:395–417

<a id='87928329-dc82-4c5e-9d65-3afac6812f85'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='2688069f-569d-4f85-820a-0cb786ec1214'></a>

COMPARTMENTAL MODELLING

<a id='2e78242b-601d-457c-be01-768bc6b56a51'></a>

403

<a id='94588f09-6ed4-4804-b785-db7701ce7826'></a>

variance-covariance matrix of **P – P⁰** [24]. Assuming a normal distribution for the natural logarithms of the well-determined parameters, the 5 and 95% confidence limits are estimated for each.

<a id='c20e2e2c-d790-427b-98e5-6046b2c63b48'></a>

The data for the individual cells were averaged and the model (1)-(9) fitted to these averaged data. Assuming that TPT hydrolysis is only dependent on pH and that there are no other cellular factors affecting it, the cytoplasm rate constants koc and kcc were fixed at values estimated in Reference [9] for different pH buffered solutions. The values obtained in Reference [9] showed a linear correlation between pH and the value of the inactivation rate constant (ko), whilst there was no clearly observable correlation between pH and the value of the activation rate constant (kc). Therefore fixed values of pH were chosen (pH 7.0, 7.2 and 7.4), from those used for parameter estimation in Reference [9], to reflect a feasible range for cellular pH. The structural global identifiability of the model, including the parameters koc and kcc, demonstrates the uniqueness of the model output for given cellular hydrolysis rates. This provides justification for comparing the three fits, corresponding to pH 7.0, 7.2 and 7.4, to select values for koc and kcc, and hence estimate cellular pH.

<a id='7a903f9b-5de6-43f2-a02e-3f7ba65e491a'></a>

The fitted parameter values are presented in Table I, where it is seen that the same two of the nine parameters (kdh and BT) are not well-determined by the data. This means that small deviations from the obtained estimate for kdh will result in similar fits. The parameter BT is defined to be a bounded function of an unconstrained positive dummy parameter in order that the estimate will be in the range 0–90 µM. It is the dummy parameter that is used in the fitting and is not well-determined because small changes result in similar values of BT and hence fits. The final estimates for kdh and BT were obtained from many fits with various initial values. In terms of the root mean squared (RMS) error, the fits with the hydrolysis rate constants fixed at pH 7.0 (RMS = 0.1445) are better than the others (pH 7.2, 0.1493 and pH 7.4, 0.1526). Note from Table I that there is little variation in the values each parameter takes between the three different cases (pH 7.0, 7.2 and 7.4). The exception is kdh, which is also one of those parameters that is not-well-determined (NWD) by the data. This suggests that the parameter estimation for this model is not sensitive to the values for the cellular hydrolysis rate constants (within physiologically based bounds).

<a id='776a1eeb-fa2b-46be-bb52-7956856ff46e'></a>

Figure 2 shows the model fits with the hydrolysis rate constants (_k_oc and _k_ec) taking values corresponding to pH 7.0. The model fits corresponding to pH values 7.2 and 7.4 are almost indistinguishable from those shown in Figure 2. These fits show that there is close reproduction of the data by simulated output from the model with parameters taking values from Table I. Figure 2 also shows the normal probability plot for the weighted residuals for each of the fits, which suggest that the weighted residuals in each case are normally distributed with zero mean and standard deviation of 1.

<a id='9738bca9-6e4e-4bb9-87ad-a66c4bbe1c76'></a>

In Table II the estimated correlation matrix for the well-determined parameters in each of the fits are given. The parameter pairings that exhibit marked correlation are: kmi and v0 (0.89), kmi and ki (-0.86), kmo and v0 (0.70), kmo and ki (0.69), v0 and ki (-0.97), and kb and kdl (1.00). The first pairs relate to the extracellular region, and in particular the crossing of the medium/ extracellular or extracellular/cytoplasm region borders. The modelling of this involves the ratio of the volumes of the extracellular region and medium, v0 = Ve/Vm, indicating the importance of this parameter and subsequent dependence of other parameters on it. The parameters kb and kdl relate to the binding and dissociation of active TPT from DNA target. The high correlation of the logarithms of these parameters indicates that it is the product or ratio of these that is important for the fitting, that is, the affinity of the drug.

<a id='014ec3d6-ec5b-48d2-930f-5483af860927'></a>

Copyright  2005 John Wiley & Sons, Ltd.

<a id='a7ff3ca0-ec05-4fb8-9114-c2dbeaacda78'></a>

Int. J. Adapt. Control Signal Process. 2005; 19:395–417

<a id='a0e42a0f-e7be-47c7-97f8-81d3e606eb85'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='95b39cd1-a28f-47ea-9f9f-d2df96149704'></a>

404

<a id='0571a404-f4a8-46ec-bc25-c67aeb645eb6'></a>

N. D. EVANS ET AL.

<a id='6edbf178-87c2-4440-9636-db1bb59ef798'></a>

Table I. Parameter values for the model (1)–(9), estimated using two-photon scanning-laser microscopy
data.
<table id="9-1">
<tr><td id="9-2">Parameter</td><td id="9-3">Value</td><td id="9-4">SDLN</td><td id="9-5">5%</td><td id="9-6">95%</td><td id="9-7">pH</td></tr>
<tr><td id="9-8"></td><td id="9-9">1.3974 x 10-6</td><td id="9-a">0.0237</td><td id="9-b">1.3439 × 10-6</td><td id="9-c">1.4529 x 10-6</td><td id="9-d">7.0</td></tr>
<tr><td id="9-e">$k_{mi}$ (s$^{-1}$)</td><td id="9-f">1.4024 x 10-6</td><td id="9-g">0.0232</td><td id="9-h">1.3499 x 10-6</td><td id="9-i">1.4569 x 10-6</td><td id="9-j">7.2</td></tr>
<tr><td id="9-k"></td><td id="9-l">1.3993 × 10-6</td><td id="9-m">0.0233</td><td id="9-n">1.3466 × 10-6</td><td id="9-o">1.4541 × 10-6</td><td id="9-p">7.4</td></tr>
<tr><td id="9-q"></td><td id="9-r">8.5551 x 10-2</td><td id="9-s">0.0168</td><td id="9-t">8.3214 × 10-2</td><td id="9-u">8.7952 × 10-2</td><td id="9-v">7.0</td></tr>
<tr><td id="9-w">kmo (s⁻¹)</td><td id="9-x">8.5721 × 10⁻²</td><td id="9-y">0.0169</td><td id="9-z">8.3365 × 10⁻²</td><td id="9-A">8.8144 × 10⁻²</td><td id="9-B">7.2</td></tr>
<tr><td id="9-C"></td><td id="9-D">8.6046 × 10⁻²</td><td id="9-E">0.0170</td><td id="9-F">8.3668 × 10⁻²</td><td id="9-G">8.8491 × 10⁻²</td><td id="9-H">7.4</td></tr>
<tr><td id="9-I"></td><td id="9-J">2.2110 × 10⁻²</td><td id="9-K">0.0354</td><td id="9-L">2.0860 × 10⁻²</td><td id="9-M">2.3435 × 10⁻²</td><td id="9-N">7.0</td></tr>
<tr><td id="9-O">ki (s⁻¹)</td><td id="9-P">2.2244 x 10⁻²</td><td id="9-Q">0.0349</td><td id="9-R">2.1004 x 10⁻²</td><td id="9-S">2.3557 × 10⁻²</td><td id="9-T">7.2</td></tr>
<tr><td id="9-U"></td><td id="9-V">2.2542 x 10⁻²</td><td id="9-W">0.0354</td><td id="9-X">2.1267 x 10⁻²</td><td id="9-Y">2.3894 × 10⁻²</td><td id="9-Z">7.4</td></tr>
<tr><td id="9-10"></td><td id="9-11">7.8915 \times 10^{-3}</td><td id="9-12">0.0145</td><td id="9-13">7.7051 \times 10^{-3}</td><td id="9-14">8.0825 \times 10^{-3}</td><td id="9-15">7.0</td></tr>
<tr><td id="9-16">k_e (s^{-1})</td><td id="9-17">8.0247 \times 10^{-3}</td><td id="9-18">0.0142</td><td id="9-19">7.8399 \times 10^{-3}</td><td id="9-1a">8.2138 \times 10^{-3}</td><td id="9-1b">7.2</td></tr>
<tr><td id="9-1c"></td><td id="9-1d">8.1679 \times 10^{-3}</td><td id="9-1e">0.0137</td><td id="9-1f">7.9862 \times 10^{-3}</td><td id="9-1g">8.3537 \times 10^{-3}</td><td id="9-1h">7.4</td></tr>
<tr><td id="9-1i"></td><td id="9-1j">3.8085 \times 10^{-4}</td><td id="9-1k">0.0726</td><td id="9-1l">3.3796 \times 10^{-4}</td><td id="9-1m">4.2917 \times 10^{-4}</td><td id="9-1n">7.0</td></tr>
<tr><td id="9-1o">k_b (s^{-1} \mu M^{-1})</td><td id="9-1p">3.2414 \times 10^{-4}</td><td id="9-1q">0.0386</td><td id="9-1r">3.0420 \times 10^{-4}</td><td id="9-1s">3.4539 \times 10^{-4}</td><td id="9-1t">7.2</td></tr>
<tr><td id="9-1u"></td><td id="9-1v">3.0304 x 10^-4</td><td id="9-1w">0.0596</td><td id="9-1x">2.7474 x 10^-4</td><td id="9-1y">3.3425 x 10^-4</td><td id="9-1z">7.4</td></tr>
<tr><td id="9-1A"></td><td id="9-1B">5.5522 x 10^-2</td><td id="9-1C">0.0759</td><td id="9-1D">4.9008 x 10^-2</td><td id="9-1E">6.2900 x 10^-2</td><td id="9-1F">7.0</td></tr>
<tr><td id="9-1G">k_dl (s^-1)</td><td id="9-1H">4.6676 x 10^-2</td><td id="9-1I">0.0385</td><td id="9-1J">4.3810 x 10^-2</td><td id="9-1K">4.9729 x 10^-2</td><td id="9-1L">7.2</td></tr>
<tr><td id="9-1M"></td><td id="9-1N">4.3125 x 10^-2</td><td id="9-1O">0.0631</td><td id="9-1P">3.8873 x 10^-2</td><td id="9-1Q">4.7843 x 10^-2</td><td id="9-1R">7.4</td></tr>
<tr><td id="9-1S"></td><td id="9-1T">1.5639 x 10^-7</td><td id="9-1U">NWD</td><td id="9-1V">—</td><td id="9-1W">—</td><td id="9-1X">7.0</td></tr>
<tr><td id="9-1Y">$k_{dh} (s^{-1})$</td><td id="9-1Z">2.5812 x 10^{-7}</td><td id="9-20">NWD</td><td id="9-21">—</td><td id="9-22">—</td><td id="9-23">7.2</td></tr>
<tr><td id="9-24"></td><td id="9-25">2.3889 × 10^{-6}</td><td id="9-26">NWD</td><td id="9-27">—</td><td id="9-28">—</td><td id="9-29">7.4</td></tr>
<tr><td id="9-2a"></td><td id="9-2b">8.9972 × 10^1</td><td id="9-2c">NWD</td><td id="9-2d">—</td><td id="9-2e">—</td><td id="9-2f">7.0</td></tr>
<tr><td id="9-2g">$B_T (\mu M)$</td><td id="9-2h">8.9999 × 10^1</td><td id="9-2i">NWD</td><td id="9-2j">—</td><td id="9-2k">—</td><td id="9-2l">7.2</td></tr>
<tr><td id="9-2m"></td><td id="9-2n">8.9905 × 10^1</td><td id="9-2o">NWD</td><td id="9-2p">—</td><td id="9-2q">—</td><td id="9-2r">7.4</td></tr>
<tr><td id="9-2s"></td><td id="9-2t">1.5045 x 10-5</td><td id="9-2u">0.0350</td><td id="9-2v">1.4203 × 10-5</td><td id="9-2w">1.5937 × 10-5</td><td id="9-2x">7.0</td></tr>
<tr><td id="9-2y">VO</td><td id="9-2z">1.5073 x 10-5</td><td id="9-2A">0.0339</td><td id="9-2B">1.4256 × 10-5</td><td id="9-2C">1.5937 × 10-5</td><td id="9-2D">7.2</td></tr>
<tr><td id="9-2E"></td><td id="9-2F">1.4984 x 10-5</td><td id="9-2G">0.0347</td><td id="9-2H">1.4153 × 10-5</td><td id="9-2I">1.5863 × 10-</td><td id="9-2J">7.4</td></tr>
</table>

<a id='1cb2e796-a1d0-438e-96a0-5888f0b389ca'></a>

The cellular hydrolysis rate constants are fixed at values obtained in Reference [9] for different pH buffered solutions where: $k_{oc}$ = 1.2913 × 10$^{-4}$ s$^{-1}$ and $k_{cc}$ = 3.1578 × 10$^{-4}$ s$^{-1}$ (pH 7.0); $k_{oc}$ = 1.5599 × 10$^{-4}$ s$^{-1}$ and $k_{cc}$ = 2.9553 × 10$^{-4}$ s$^{-1}$ (pH 7.2); $k_{oc}$ = 1.9448 × 10$^{-4}$ s$^{-1}$ and $k_{cc}$ = 3.0895 × 10$^{-4}$ s$^{-1}$ (pH 7.4). NWD indicates that the estimate is not well-determined by the data.

<a id='8541972e-b008-4422-bd0d-0fe75ae2a1b6'></a>

One of the motivations for the mathematical modelling is to infer from the model information concerning parts of the system that are not directly measured. For example, in the cytoplasm it is the total concentration of TPT (Lc + Hc) that is measured using microscopy, and so one might wish to estimate from the model the relative concentrations of TPT-L and TPT-H in the cytoplasm (Lc and Hc respectively). Since the cellular hydrolysis rate constants (koc and kcc) are pH dependent and their values affect the equilibrium value of the ratio of active to inactive TPT in buffers (see Reference [9] for more details), it would be expected that the different fits would give rise to different predictions regarding the ratios of TPT-L to TPT-H in the different experimental locations. In fact, the predictions are almost indistinguishable between the fits except in the cytoplasm, where only the predicted values for TPT-H differ noticeably. This is

<a id='10d6a6c3-2901-45d8-b576-232f4567c937'></a>

Copyright &#169; 2005 John Wiley & Sons, Ltd.

<a id='606a9c8a-7c8b-44f5-8383-c81f7a397c89'></a>

_Int. J. Adapt. Control Signal Process. 2005; **19**:395–417_

<a id='594c69d2-08ab-417e-9e10-1b9e1843e9f9'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='4940a8aa-73ae-422d-94cf-bb276a772c1b'></a>

COMPARTMENTAL MODELLING

<a id='6dada79d-21cc-4e3d-b052-aeaa4617a761'></a>

405

<a id='390fab21-04e0-4709-9a4f-ecb1be0ac2ac'></a>

<::figure: A multi-panel figure showing simulated output from a model against experimental data, and normal probability plots for weighted residuals. The figure consists of six subplots labeled (a) through (f). Panels (a), (b), and (c) are line graphs showing Concentration (μM) on the y-axis versus Time (s) on the x-axis. Each graph displays experimental data points as circles and a simulated output as a solid line. Panel (a) shows the Extracellular region, panel (b) shows Cytoplasm, and panel (c) shows Nucleus. Panels (d), (e), and (f) are normal probability plots, showing data points on a grid with Ordered residuals on the x-axis and probability values on the y-axis. Panel (d) is for pH 7.0, panel (e) is for pH 7.2, and panel (f) is for pH 7.4. Figure 2. Simulated output from the model (1)-(9), with parameters taking values in Table I (pH 7.0), plotted (solid) against the experimental data (circles). The corresponding normal probability plots for the weighted residuals, for each of the fits, are shown in (d)-(f). (a) Extracellular region, (b) Cytoplasm, (c) Nucleus, (d) Normal probability (pH 7.0), (e) Normal probability plot (pH 7.2), (f) Normal probability plot (pH 7.4).::>

<a id='988e5519-ba45-45d9-83ec-f1943b618a1a'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='7da7be0f-dce4-4503-99e5-aad11c70bb9f'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**: 395-417

<a id='c647b24b-2594-4d72-8b69-baa963edee2f'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='751f6ec7-9ac5-4a1e-aefe-7a7b49dcb146'></a>

406

<a id='9c0756be-7a98-4d81-933f-b422c652cf01'></a>

N. D. EVANS ET AL.

<a id='d4b8e29f-e007-4a6a-a367-bc1aac69bef0'></a>

Table II. The estimated correlation matrix for the well-determined parameters, with the cellular hydrolysis rate constants fixed at values obtained in Reference [9] for buffered solutions with pH 7.0, pH 7.2 or pH 7.4, respectively.
<table id="11-1">
<tr><td id="11-2"></td><td id="11-3">kmi</td><td id="11-4">kmo</td><td id="11-5">v0</td><td id="11-6">ki</td><td id="11-7">kₑ</td><td id="11-8">k_b</td><td id="11-9">k_dll</td></tr>
<tr><td id="11-a" colspan="8">pH 7.0</td></tr>
<tr><td id="11-b">kmi</td><td id="11-c">1.000</td><td id="11-d">-0.322</td><td id="11-e">0.896</td><td id="11-f">-0.870</td><td id="11-g">0.082</td><td id="11-h">-0.015</td><td id="11-i">-0.013</td></tr>
<tr><td id="11-j">kmo</td><td id="11-k">-0.322</td><td id="11-l">1.000</td><td id="11-m">-0.707</td><td id="11-n">0.692</td><td id="11-o">0.005</td><td id="11-p">-0.058</td><td id="11-q">-0.057</td></tr>
<tr><td id="11-r">vo</td><td id="11-s">0.896</td><td id="11-t">-0.707</td><td id="11-u">1.000</td><td id="11-v">-0.971</td><td id="11-w">0.065</td><td id="11-x">0.015</td><td id="11-y">0.016</td></tr>
<tr><td id="11-z">kᵢ</td><td id="11-A">-0.870</td><td id="11-B">0.692</td><td id="11-C">-0.971</td><td id="11-D">1.000</td><td id="11-E">0.166</td><td id="11-F">-0.099</td><td id="11-G">-0.099</td></tr>
<tr><td id="11-H">kₑ</td><td id="11-I">0.082</td><td id="11-J">0.005</td><td id="11-K">0.065</td><td id="11-L">0.166</td><td id="11-M">1.000</td><td id="11-N">-0.317</td><td id="11-O">-0.318</td></tr>
<tr><td id="11-P">kᵦ</td><td id="11-Q">-0.015</td><td id="11-R">-0.058</td><td id="11-S">0.015</td><td id="11-T">-0.099</td><td id="11-U">-0.317</td><td id="11-V">1.000</td><td id="11-W">0.999</td></tr>
<tr><td id="11-X">k𝒹ₗ</td><td id="11-Y">-0.013</td><td id="11-Z">-0.057</td><td id="11-10">0.016</td><td id="11-11">-0.099</td><td id="11-12">-0.318</td><td id="11-13">0.999</td><td id="11-14">1.000</td></tr>
<tr><td id="11-15" colspan="8">pH 7.2</td></tr>
<tr><td id="11-16">kmi</td><td id="11-17">1.000</td><td id="11-18">-0.261</td><td id="11-19">0.882</td><td id="11-1a">-0.851</td><td id="11-1b">0.040</td><td id="11-1c">0.114</td><td id="11-1d">0.122</td></tr>
<tr><td id="11-1e">kmo</td><td id="11-1f">-0.261</td><td id="11-1g">1.000</td><td id="11-1h">-0.684</td><td id="11-1i">0.678</td><td id="11-1j">0.085</td><td id="11-1k">-0.242</td><td id="11-1l">-0.265</td></tr>
<tr><td id="11-1m">V0</td><td id="11-1n">0.882</td><td id="11-1o">-0.684</td><td id="11-1p">1.000</td><td id="11-1q">-0.972</td><td id="11-1r">-0.005</td><td id="11-1s">0.204</td><td id="11-1t">0.222</td></tr>
<tr><td id="11-1u">ki</td><td id="11-1v">-0.851</td><td id="11-1w">0.678</td><td id="11-1x">-0.972</td><td id="11-1y">1.000</td><td id="11-1z">0.232</td><td id="11-1A">-0.275</td><td id="11-1B">-0.294</td></tr>
<tr><td id="11-1C">ke</td><td id="11-1D">0.040</td><td id="11-1E">0.085</td><td id="11-1F">-0.005</td><td id="11-1G">0.232</td><td id="11-1H">1.000</td><td id="11-1I">-0.272</td><td id="11-1J">-0.290</td></tr>
<tr><td id="11-1K">k_b</td><td id="11-1L">0.114</td><td id="11-1M">-0.242</td><td id="11-1N">0.204</td><td id="11-1O">-0.275</td><td id="11-1P">-0.272</td><td id="11-1Q">1.000</td><td id="11-1R">0.995</td></tr>
<tr><td id="11-1S">k_dl</td><td id="11-1T">0.122</td><td id="11-1U">-0.265</td><td id="11-1V">0.222</td><td id="11-1W">-0.294</td><td id="11-1X">-0.290</td><td id="11-1Y">0.995</td><td id="11-1Z">1.000</td></tr>
<tr><td id="11-20" colspan="8">pH 7.4</td></tr>
<tr><td id="11-21">k_mi</td><td id="11-22">1.000</td><td id="11-23">-0.304</td><td id="11-24">0.889</td><td id="11-25">-0.866</td><td id="11-26">0.043</td><td id="11-27">0.048</td><td id="11-28">0.049</td></tr>
<tr><td id="11-29">k_mo</td><td id="11-2a">-0.304</td><td id="11-2b">1.000</td><td id="11-2c">-0.706</td><td id="11-2d">0.691</td><td id="11-2e">0.007</td><td id="11-2f">-0.038</td><td id="11-2g">-0.038</td></tr>
<tr><td id="11-2h">v0</td><td id="11-2i">0.889</td><td id="11-2j">-0.706</td><td id="11-2k">1.000</td><td id="11-2l">-0.974</td><td id="11-2m">0.034</td><td id="11-2n">0.054</td><td id="11-2o">0.055</td></tr>
<tr><td id="11-2p">ki</td><td id="11-2q">-0.866</td><td id="11-2r">0.691</td><td id="11-2s">-0.974</td><td id="11-2t">1.000</td><td id="11-2u">0.186</td><td id="11-2v">-0.103</td><td id="11-2w">-0.103</td></tr>
<tr><td id="11-2x">ke</td><td id="11-2y">0.043</td><td id="11-2z">0.007</td><td id="11-2A">0.034</td><td id="11-2B">0.186</td><td id="11-2C">1.000</td><td id="11-2D">-0.170</td><td id="11-2E">-0.172</td></tr>
<tr><td id="11-2F">kb</td><td id="11-2G">0.048</td><td id="11-2H">-0.038</td><td id="11-2I">0.054</td><td id="11-2J">-0.103</td><td id="11-2K">-0.170</td><td id="11-2L">1.000</td><td id="11-2M">0.998</td></tr>
<tr><td id="11-2N">kdl</td><td id="11-2O">0.049</td><td id="11-2P">-0.038</td><td id="11-2Q">0.055</td><td id="11-2R">-0.103</td><td id="11-2S">-0.172</td><td id="11-2T">0.998</td><td id="11-2U">1.000</td></tr>
</table>

<a id='96526bca-ddba-4cdd-900e-a6923e503a1a'></a>

shown in Figure 3, where the predictions for each pH value for TPT-L and TPT-H, and the ratio of TPT-L to TPT-H in the cytoplasm against time are compared. The principal difference between the predictions, with the hydrolysis rate constants taking values corresponding to different pH conditions, is the prediction for TPT-H in the cytoplasm, where these are seen to diverge over time. Beyond this there seems to be little effect.

<a id='803fbcf4-ef23-4dfd-942f-d38df91f6581'></a>

6. SENSITIVITY TO CELLULAR HYDROLYSIS RATE CONSTANTS
It was shown in the previous section (Figure 3) that the principal difference between model predictions using the different parameter values from Table I is that for TPT-H in the cytoplasm. Other simulated output does not seem to be sensitive to the different values assumed for the cellular hydrolysis rate constants (koc and kcc). In this section the impact of varying the values for koc and kcc is considered with respect to individual compartment concentrations and predicted dose response, particularly at the target, nuclear DNA.

<a id='be0e5eda-f546-4d5c-bfef-7e40eb82b3be'></a>

Copyright  2005 John Wiley & Sons, Ltd.

<a id='dacc1fba-cdeb-4e3e-a4e9-318d6e65c6dd'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**:395–417

<a id='e3f8e981-7f0a-432c-ae5d-3826bea4243a'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='cbd8e0db-e5df-4fe3-9c55-3fe4055b68b1'></a>

COMPARTMENTAL MODELLING

<a id='2868d5e3-5484-4dac-9b36-9eb58d89337b'></a>

407

<a id='87f26feb-1015-41ee-9265-b595cbbfdb2c'></a>

<::chart: This figure displays three plots (a), (b), and (c) showing simulated output from the model (1)–(9), with parameters taking values in Table I.  Plot (a) shows TPT-L concentration against time in the cytoplasm. The x-axis is 'Time (s)' ranging from 0 to 450. The y-axis is 'Concentration (μM)' ranging from 0 to 9. The plot contains three lines representing different pH values: pH 7.0 (light gray), pH 7.2 (medium gray), and pH 7.4 (dark gray). An inset zooms in on the time range 420-450 s and concentration range 8.3-8.7 μM, showing the same three lines. Plot (b) shows TPT-H concentration against time in the cytoplasm. The x-axis is 'Time (s)' ranging from 0 to 450. The y-axis is 'Concentration (μM)' ranging from 0 to 0.5. This plot also contains three lines for pH 7.0 (light gray), pH 7.2 (medium gray), and pH 7.4 (dark gray). Plot (c) shows the ratio, against time, of the concentrations of TPT-L and TPT-H. The x-axis is 'Time (s)' ranging from 0 to 450 (with labels at 50, 150, 250, 350, 450). The y-axis is 'Ratio L:H' ranging from 0 to 350 (with labels at 70, 140, 210, 280, 350). Similar to the other plots, there are three lines for pH 7.0 (light gray), pH 7.2 (medium gray), and pH 7.4 (dark gray). All three plots show concentration or ratio increasing with time, with variations based on pH levels.::>

<a id='41f130f5-fd96-4a51-9259-a026772a7bc0'></a>

6.1. *Model sensitivity*

The impact of varying the values for the cellular hydrolysis rate constants is shown in Figure 4. The parameters in the model were assigned values from the pH 7.0 fits in Table I and the hydrolysis rate constants varied in the range of 0.1–10 times the fixed value. These values are: for k_oc (a) 1.2913 × 10⁻⁵ s⁻¹, (b) 1.7217 × 10⁻⁵ s⁻¹, (c) 2.5826 × 10⁻⁵ s⁻¹, (d) 5.1652 × 10⁻⁵ s⁻¹, (e) 3.2283 × 10⁻⁴ s⁻¹, (f) 6.4565 × 10⁻⁴ s⁻¹, (g) 9.6848 × 10⁻⁴ s⁻¹ and (h) 1.2913 × 10⁻³ s⁻¹; and for k_cc (a) 3.1578 × 10⁻⁵ s⁻¹, (b) 4.2104 × 10⁻⁵ s⁻¹, (c) 6.3156 × 10⁻⁵ s⁻¹, (d) 1.2631 × 10⁻⁴ s⁻¹, (e) 7.8945 × 10⁻⁴ s⁻¹, (f) 1.5789 × 10⁻³ s⁻¹, (g) 2.3684 × 10⁻³ s⁻¹ and (h) 3.1578 × 10⁻³ s⁻¹. The only model variables exhibiting noticeable variation in simulations were L_c, H_c and L_n, when varying k_oc, and H_c when varying k_cc. The simulations show that the model is more sensitive to changes in the inactivation rate constant k_oc, and that the greatest variation occurs in the simulated concentration of TPT-H in the cytoplasm. This is not surprising since Evans et al. [9] found that the inactivation rate constant was generally better determined from data than the activation one (though the natural

<a id='493d60fa-5790-45ba-a281-695bd4efe75d'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='d1540d76-39a6-4349-92f6-1f4ae2d3ce63'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**:395–417

<a id='f97691e6-45e0-4aa1-9c71-85cfacae817a'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='788e27df-8efb-44ce-b10e-54cda2c8c332'></a>

408

<a id='2840ea21-9d65-486b-bbdf-4a5ca46eeb89'></a>

N. D. EVANS *ET AL.*

<a id='c6c52427-1349-49e2-9fe1-e4ba3b024754'></a>

<::Figure: A multi-panel line chart titled "Figure 4. Simulated output from the model (1)–(9), with parameters taking values in Table I (pH 7.0), while varying hydrolysis rate constants koc and kcc in the ranges (a) 1.2913 × 10⁻⁵ s⁻¹ to (h) 1.2913 × 10⁻³ s⁻¹, and (a) 3.1578 × 10⁻⁵ s⁻¹ to (h) 3.1578 × 10⁻³ s⁻¹, respectively." The figure consists of five subplots (a) through (e), each showing "Concentration (μM)" on the y-axis against "Time" on the x-axis, with multiple labeled lines (a) to (h) representing different rate constants. Most subplots include an inset with a zoomed-in view of a portion of the main plot. :chart::>

(a) Lc (varying koc): The x-axis is "Time (s)" from 0 to 60. The y-axis is "Concentration (μM)" from 0 to 10. Eight lines (a-h) are shown, all starting at 0, increasing to a peak concentration between 8 and 9 μM, and then gradually decreasing. The inset shows a magnified view of the declining phase of the curves from approximately 55 to 60 seconds, with concentrations ranging from 7.5 to 9.9 μM, labeled c,b,a, d, e, f, g, h from top to bottom.

(b) Hc (varying kcc): The x-axis is "Time (min)" from 0 to 60. The y-axis is "Concentration (μM)" from 0 to 22. Eight lines (a-h) are shown, all starting at 0 and steadily increasing over time. Line h shows the highest concentration, while line a shows the lowest. The inset shows a magnified view of the initial phase of the curves from approximately 0 to 60 minutes, with concentrations ranging from 0 to 0.5 μM, labeled a, b, c from bottom to top.

(c) Ic (varying kcc): The x-axis is "Time (min)" from 0 to 60. The y-axis is "Concentration (μM)" from 0 to 10. Eight lines (a-h) are shown, all starting at 0, increasing to a peak concentration between 9 and 10 μM, and then gradually decreasing. The inset shows a magnified view of the declining phase of the curves from approximately 55 to 60 minutes, with concentrations ranging from 7.9 to 8.2 μM, labeled f,g,h, e, a, b, c, d from top to bottom.

(d) Hn (varying kcc): The x-axis is "Time (min)" from 0 to 60. The y-axis is "Concentration (μM)" from 0 to 4. Eight lines (a-h) are shown, all starting at 0 and steadily increasing over time. Line h shows the highest concentration, while line a shows the lowest. A legend indicates the line styles for (a) through (h).

(e) Im (varying kcc): The x-axis is "Time (min)" from 0 to 60. The y-axis is "Concentration (μM)" from 0 to 14. Eight lines (a-h) are shown, all starting at 0, increasing to a peak concentration between 12 and 13 μM, and then gradually decreasing. The inset shows a magnified view of the declining phase of the curves from approximately 55 to 60 minutes, with concentrations ranging from 10.4 to 11.3 μM, labeled b,a, c, d, e, f, g, h from top to bottom.

<a id='098fed26-da75-4ff1-be65-40454e8206dc'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='8f28155c-f4a3-49a3-8db0-5602db4692cd'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**:395–417

<a id='eb512794-2994-4118-a216-244dcac99dd4'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='98f0fa1a-8f03-4f03-9418-6413c9f185c5'></a>

COMPARTMENTAL MODELLING

<a id='e2b91022-b551-4fb9-b31c-b82e7d5a4c31'></a>

409

<a id='51d9ff10-0779-4456-9730-ce4bdd46fa81'></a>

logarithms of the estimates were highly correlated), and variation in the values of koc and kec affects the hydrolysis of TPT in the cytoplasm. The lack of sensitivity of Le to variation in the hydrolysis rate constants suggests that this is not a key process for the presence of TPT-L in the cytoplasm, and so the flux of TPT-L across the plasma membrane and its binding/dissociation are more crucial.

<a id='a3203df2-7b61-483c-be33-5a8ad0d71ace'></a>

Most of the variation seen in the simulations for the model variables occurs after the first 7.5 min (the period over which the parameter fitting was performed). It is therefore seen that possible variation in the values for the cellular hydrolysis rate constants will predominantly affect model predictions concerning future behaviour (i.e. after the fitting time period). The further beyond the fitting time period simulations are performed the greater effect this variation will have. The time period of 1 h chosen for the simulations that gave rise to the results in Figure 4 might be considered as an appropriate one for therapeutic investigations.

<a id='45398719-74e8-49be-985c-f7d0379da967'></a>

6.2. Sensitivity of dose response
By varying the value of the model dose parameter D and exploring the effect this has upon the time course for nuclear TPT-L, possible therapeutic impact of different doses can be investigated, since the latter represents the target for TPT. If the impact of a dose is measured in terms of the total amount of TPT-L binding to DNA over the first hour following drug administration then this is represented, in terms of the model, as the area under the time series curve for Ln corresponding to D (AUC(Ln,D)). This can be regarded as the 'response' of the system to the dose corresponding to the value of D.

<a id='3a807f30-c7ed-47f2-929d-978ed661c582'></a>

To investigate the variation in model predictions for dose response arising from variation in the values taken by the cellular rate constants, simulations are performed with D taking values from 0.1 to 20 µM with koc and kcc also varied as in the last subsection. It is seen from Figure 5(c) that variation in kcc has little effect on the dose response (as measured by AUC(Ln,D)), particularly for low doses. For higher doses there is a small effect with larger values of kcc giving rise to greater accumulation of drug at the target. This is as a result of the TPT-H activation pathway providing increased concentration of TPT-L in the cytoplasm.

<a id='bd69b80b-5106-48b6-a082-c7106f779303'></a>

Although variation in the value of $k_{oc}$, the cellular TPT-L inactivation rate constant, has an increased effect on the dose response, this effect is small, particularly for low doses. Increasing the value of $k_{oc}$ decreases the accumulated amount of active drug reaching the target, with this effect becoming more pronounced with increasing dose. The overall dose response, for each fixed pair $k_{oc}$ and $k_{ec}$, is approximately linear so that doubling the dose doubles the area-under-curve for TPT-L at the target ($L_n$).


<a id='a7c37751-5b85-40eb-96db-6bdcefa9806e'></a>

7. CONCLUSIONS
A compartmental model of the _in vitro_ uptake kinetics of the anti-cancer agent topotecan (TPT) in human breast cancer cells (MCF-7 cell line) has been proposed in this paper. The model parameters were estimated using the computer package FACSIMILE and experimental data obtained using two-photon scanning-laser microscopy. Data from 13 individual cells were averaged so that a model representing TPT kinetics in a population could be obtained. The

<a id='8d55f790-0d95-4f53-9467-4bb1cb9ca6bf'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='e50dd2c1-a3ae-4e22-bcc6-d04fbb5052c4'></a>

_Int. J. Adapt. Control Signal Process. 2005; **19**:395–417_

<a id='bf0816f6-5e3f-4e44-b670-a87674c6bc46'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='4a2b41d4-6213-43a2-81c1-19636c18df55'></a>

410

<a id='03ea5b86-23af-42e1-874b-0678131eeb9a'></a>

N. D. EVANS ET AL.

<a id='57fbae3b-4c36-4ebf-b9e7-fc68750f4e6a'></a>

Figure 5. Area-under-curve (AUC) for L_n over 1 h against dose D, with the cellular hydrolysis rate constants k_oc and k_ce varying in the ranges (a) 1.2913 × 10⁻⁵ s⁻¹ to (h) 1.2913 × 10⁻³ s⁻¹, and (a) 3.1578 × 10⁻⁵ s⁻¹ to (h) 3.1578 × 10⁻³ s⁻¹, respectively. The values of k_oc and k_ce corresponding to pH 7.0, used in the fitting, are indicated with a plus ('+') symbol. The figure displays four plots arranged in a 2x2 grid:

(a) **Dose response (varying k_oc)**: A plot with Dose, D (µM) on the x-axis ranging from 0 to 20, and AUC(L_n, D) (µM hr) on the y-axis ranging from 0 to 21. Multiple curves are shown, starting from the origin and increasing non-linearly, with the curves being very close together, showing the area under the curve as a function of dose.

(b) **Dose response (varying k_oc)**: A zoomed-in plot of the dose response for varying k_oc. The x-axis is Dose, D (µM), ranging from 19 to 20. The y-axis is AUC(L_n, D) (µM hr), ranging from 18 to 20.5. Several distinct, slightly increasing curves are shown, labeled 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'. Curves 'a' and 'b' are very close at the bottom, while 'h' is at the top. A plus ('+') symbol is marked on curve 'd' at approximately Dose = 19.5 µM.

(c) **Dose response (varying k_ce)**: A plot with Dose, D (µM) on the x-axis ranging from 0 to 20, and AUC(L_n, D) (µM hr) on the y-axis ranging from 0 to 21. Similar to plot (a), multiple curves are shown, starting from the origin and increasing non-linearly, with the curves being very close together, showing the area under the curve as a function of dose.

(d) **Dose response (varying k_ce)**: A zoomed-in plot of the dose response for varying k_ce. The x-axis is Dose, D (µM), ranging from 19.6 to 20. The y-axis is AUC(L_n, D) (µM hr), ranging from 19.85 to 20.45. Several distinct, slightly increasing curves are shown, labeled 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'. Curves 'a', 'b', 'c', 'd' are very close at the bottom, while 'h' is at the top. A plus ('+') symbol is marked on curve 'd' at approximately Dose = 19.8 µM.

<a id='e54a7d05-a772-4b03-892f-5f6df60b80b0'></a>

simulated output from the model accurately reproduces the behaviour of the biochemical system being represented. In particular, the mixing effect in the extracellular medium evident from the microscopy data (note that there is a period of increase in extracellular concentration before approaching the input dose concentration value, 10 µM) is accurately modelled by extending the model proposed by Evans _et al._ [9]. This extension involves subdividing the medium compartments proposed in Reference [9] into a 'medium' compartment, into which the drug is added, and an 'extracellular region' compartment, within which the cells are located. A knowledge-based modelling approach was adopted in that the form of the mathematical model is based on prior biological information or assumptions. This allowed investigation of these assumptions.

<a id='b279741c-a363-4e43-86c0-6358a11e7620'></a>

To ensure that the parameter estimates obtained from the fitting would be meaningful a
formal structural identifiability analysis was performed using the Taylor series approach
proposed in Reference [18]. Such an analysis tests the uniqueness of the unknown model

<a id='601ca5e6-c897-485d-9acc-b8745a655416'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='bbb60f58-b424-4a90-bd85-b79830c3e875'></a>

_Int. J. Adapt. Control Signal Process._ 2005; **19**: 395–417

<a id='894086e8-2b7c-4b62-83b3-a39437be99db'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='94d8ebde-63c7-4e12-abed-20daff1ec41e'></a>

COMPARTMENTAL MODELLING

<a id='063b6bd2-3864-446a-ac80-6ce9931ed1d4'></a>

411

<a id='9d516bfc-5bb3-4f0c-a85e-467da212bdeb'></a>

parameters for a given model output, that is, the variables or combinations of variables that are to be directly measured, and is an important prerequisite to experiment design and parameter estimation. The compartmental model proposed in this experiment was found to be structurally globally identifiable with respect to the two-photon scanning-laser microscopy experiments used to collect data. This ensures that each model parameter can be uniquely determined from perfect, noise-free and continuous output data.

<a id='cbe6e4c9-076b-4e0c-9734-b39c4bf8d898'></a>

To test the hypothesis that cellular hydrolysis of TPT is dependent on cellular pH only, parameter estimates obtained in Reference [9] for hydrolysis in different pH buffers (phosphate buffered saline) were used for the corresponding rate constants. It was found that the values corresponding to a buffer with pH 7.0 produced better model fits, in terms of the residual sum of squares error. Further analysis showed that the model fits were not very sensitive to small variations in the values of the cellular hydrolysis rate constants.

<a id='a188c780-44d9-4000-89e7-ac473fada50a'></a>

One of the advantages of mathematical modelling is the flexibility to perform simulations over different time intervals, which allows predictions about future system behaviour to be made. It was found that the model predictions over an hour following drug administration are also relatively insensitive to the values of the cellular hydrolysis rate constants. The largest variation was obtained for the variable Hc, which is the concentration of TPT-H in the cytoplasm. Moreover, the model is more sensitive to variation in the inactivation rate constant koc, possibly as a result of its effect on the process of binding of TPT-L to target.

<a id='523420f3-1c61-4cf2-94e0-95a8f88a01d5'></a>

The model variable Lₙ, which is the concentration of TPT-L bound to DNA, represents the drug action and the integral of this variable corresponds to the total amount of active drug reaching the target. It is this variable, or the integral of it, that is likely to be a key factor in any pharmacodynamic modelling, that is, modelling of the effect of the drug. The model demonstrates an approximately linear response, in terms of the area under the Lₙ time series curve, to changes in the initial dose. Hence a doubling of dose results in a doubling of the total amount hitting the target. The predictions for Lₙ and the area under the Lₙ curve demonstrate little sensitivity to small changes in the values of the cellular hydrolysis rate constants. This shows that errors in the estimates for these parameter values will not have a large effect on the model predictions for dose response—demonstrating the validity of the model for such purposes.

<a id='1ddf82ea-bee6-409f-aa78-c266af21e47d'></a>

The present model does not seek to address inter-cellular heterogeneity, but rather represents the population response. This allows a model with fewer compartments and parameters. It is important though, if the kinetics of TPT in a tumour are to be modelled, to consider the impact of inter-cellular heterogeneity. This will allow the effects of individual cell drug resistance, such as different drug efflux pathways to be investigated. An investigation of this form may prove to be useful in the design of therapeutic regimens and provide insights into the development of drug resistance reversing agents.

<a id='f1c7d615-6d1d-46bd-bfb2-0edd823ad81e'></a>

APPENDIX A: STRUCTURAL IDENTIFIABILITY ANALYSIS WITHIN THE
SYMBOLIC COMPUTATION PACKAGE MATHEMATICA

<a id='026bc875-311d-475c-be8d-e699d7e8c5c2'></a>

In the following sections sample code for performing the structural identifiability analysis in the
symbolic package MATHEMATICA is provided. Use of such a package is invaluable when
performing a structural identifiability analysis.

<a id='0ae38c2d-2df7-4fb4-8cbb-7fd5641b7691'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='3a4062f0-2144-4236-b802-94a4d6118764'></a>

Int. J. Adapt. Control Signal Process. 2005; 19:395–417

<a id='4d4b5ee7-724d-4708-ad8c-f324cfcef31c'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='f1b9264d-019d-477c-add8-4df1854f23b8'></a>

412

<a id='61d6c859-37c7-477d-8b33-74c08eb65526'></a>

N. D. EVANS ET AL.

<a id='c116e121-6c4a-430c-a589-9b76e6ff4d51'></a>

A.1. Sample MATHEMATICA code

The first step is to encode the model, in this case by defining functions for the first derivatives (with respect to t) of the model variables:

Lm' [t_] := -(Kom + Kmi) Lm [t] + Kcm Hm [t] + Kmo v0 Le [t]
Hm' [t_] := Kom Lm [t] - (Kcm + Kmi) Hm [t] + Kmo v0 He [t]
Le' [t_] :=
Kmi
--- Lm [t] - (Kmo + Kom + Ki) Le [t] + Kcm He [t] +
v0
Ke
--- Lc [t]
v1
He' [t_] :=
Kmi
--- Hm [t] + Kom Le [t] - (Kcm + Kmo) He [t]
v0
Lc' [t_] := Ki v1 Le [t] - (Ke + Koc) Lc [t] +
Kcc Hc [t] + Kdl v2 Ln[t]
Hc' [t_] := Koc Lc [t] - Kcc Hc [t] + Kdh v2 Ln[t]
Ln' [t_] :=
Kb
--- (Bt - Ln[t]) Lc [t] - (Kdl + Kdh) Ln[t]
v2

together with the initial conditions:

<a id='a30b3b66-900a-4643-b096-868f0d7a6b3f'></a>

Lm[0] = (1 + v0) d; Hm[0] = 0; Le[0] = 0;
He[0] = 0; Lc[0] = 0; Hc[0] = 0; Ln[0] = 0;

<a id='ca558771-f5ee-4944-968e-b2c411aaa451'></a>

The output structure, i.e. **y(t, p)**, corresponding to the microscopy experiment is input as follows:

<a id='c2e814e3-e393-46ef-a48d-cf615794974e'></a>

y[t_] := {Le[t] + He[t], Lc[t] + Hc[t], Ln[t]}

<a id='2f2f854a-1b32-47eb-bd9a-be344869b498'></a>

Next, the fact that there is a relation between the parameters v0 and v1 has to be taken into account:

<a id='40e80378-02a6-4a25-b091-6c40a69ddb87'></a>

v1 = α v0 / (1 + v0);

<a id='c264329d-9a0a-4a1b-9813-5c7165e347d5'></a>

(a is a known value and is equal to 2.4125 × 10⁴). The first terms in the Taylor series expansions of the components of the output (k = 0 in Equation (13)) are zero:

<a id='451e1850-30b0-4e56-9e6b-ab0cd2a05df3'></a>

y[0]

<a id='8034461a-84a3-45ce-b2e4-9d03e053c88d'></a>

{0, 0, 0}

<a id='5c84a2fd-4407-4a24-a41a-906730e88ebf'></a>

The remaining terms in the Taylor series expansions of the components of the output
are obtained by taking successive derivatives (with respect to _t_) and substituting _t_ = 0.
To perform the identifiability analysis, suppose that there is a vector **p** with an overline such that the output
**y**(_t_, **p** with an overline) is identical to **y**(_t_, **p**). Coefficients of the expansions of the components of these outputs
are equated to obtain relations between the parameter vectors **p** and **p** with an overline. To do this in MATHE-
MATICA, successive terms in the expansions of the components of **y**(_t_, **p** with an overline) are obtained and then
the following set of substitution rules applied to obtain the corresponding terms in the

<a id='d2b56ec7-0d54-42d5-a139-022dab5ac80d'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='3995468c-bb44-4ad4-ba35-ba3e2ff1d513'></a>

_Int. J. Adapt. Control Signal Process. 2005; **19**:395–417_

<a id='90868ffb-a882-4bf3-be87-bc5560f561b5'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='e13da177-9b7f-47f6-84c2-1b2b439d1ec4'></a>

COMPARTMENTAL MODELLING

<a id='b05b8e33-65d9-4057-bb0e-cd076d35f5d4'></a>

413

<a id='ce090acd-cb7c-477a-ae88-201d17b05a55'></a>

expansions for y(t, p):

<a id='21397045-12a7-47b4-9667-318c9f4344b1'></a>

subst = {Kmi → Kmib, Kmo → Kmob, Ki → Kib,
Ke → Keb, Koc → Kocb, Kcc → Kccb, Kb → Kbb,
Kdl → Kdlb, Kdh → Kdhb, Bt → Btb, v0 → v0b};

<a id='688d2dc7-ce19-4ad7-ba6b-673f08331615'></a>

Thus, for example, if the parameter $k_{om}$ (Kom used in MATHEMATICA) is a component of the parameter vector **p**, then the corresponding parameter in $\bar{\mathbf{p}}$ is $\bar{k}_{om}$, and is denoted by Komb in MATHEMATICA.

<a id='5b2cae8d-6a84-4345-8efd-9bdc38080d2a'></a>

For k = 1, in Equation (13), it is seen that
yDer = D[y[t], t];
yCoeff = yDer /. t -> 0;
eqn = yCoeff[[1]] - (yCoeff[[1]] /. subst);
newSoln = Simplify[Solve[eqn == 0, {Kmib, Kmob,
Kib, Keb, Kocb, Kccb, Kbb, Kdlb, Kdhb, Btb, v0b}]]

<a id='0dc75bd2-72b0-42fd-ab93-08e5590d341e'></a>

Solve::svars :
Equations may not give solutions for all "solve" variables. More...

<a id='1780639e-5883-4ce0-8996-74a07d90495e'></a>

{{Kmib → Kmi (1+v0) v0b / v0 (1 + v0b)}}

<a id='d0285ad5-ab49-4d20-b7e0-c36220af2b11'></a>

This gives the following relation between $\bar{k}_{mi}$ and $k_{mi}$:
soln = newSoln[[1]]

<a id='a7c492b9-e350-4b6c-b4a5-2bbb911dae77'></a>

{Kmib → (Kmi (1+v0) v0b) / (v0 (1 + v0b))}

<a id='8cd77ad1-1111-45df-8c0e-e38fd15a7de2'></a>

For $k = 2$ in Equation (13), and using the previous relation (fourth line of code), it is seen that
yDer = D[yDer, t];
yCoeff = Simplify[yDer /. t → 0];
eqn = yCoeff - (yCoeff /. subst);
eqn = Simplify[eqn/. soln];
newSoln = Simplify[Solve[eqn == 0,
{Kmob, Kib, Keb, Kocb, Kccb, Kbb, Kdlb, Kdhb, Btb, v0b}]]

<a id='d49bd5a5-7b5b-4d6b-b38c-7e73d793cc33'></a>

Solve::svars :
Equations may not give solutions for all "solve" variables. More...

{{Kmob → Ki (-v0 + v0b) / ((1 + v0) v0b) + (Kmi v0 + Kmo v0 - Kmi v0b + Kmo v0 v0b) / (v0 + v0 v0b)
Kib → Ki v0 (1 + v0b) / ((1 + v0) v0b)}}

<a id='e5ca0e61-0cb8-4075-b5cb-963935c35f9b'></a>

Copyright  2005 John Wiley & Sons, Ltd.

<a id='13956334-839d-4cd1-a991-447835b108f5'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**:395–417

<a id='322e9c9d-97d8-4fc9-b0ce-6ac5e9566a5c'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='177170f2-0ff0-4d42-ad99-a3b138c22513'></a>

414

<a id='40a7f204-496a-4797-b052-a923b9466273'></a>

N. D. EVANS *ET AL.*

<a id='41ae8972-6d46-4a5f-9e29-284d3a26e4ad'></a>

which gives the following set of updated relations between the components of p
and p:

<a id='1e033b20-c160-43c3-b72d-1ab3b838653e'></a>

soln = Union[soln, newSoln[[1]]]

{Kib → Ki v0 (1 + v0b) / (1 + v0) v0b ,
Kmib → Kmi (1 + v0) v0b / v0 (1 + v0b)

Kmob → Ki (-v0 + v0b) / (1 + v0) v0b + Kmi v0 + Kmo v0 - Kmi v0b + Kmo v0 v0b / v0 + v0 v0b }

<a id='c61c18fe-f040-417e-912e-e268a78942a9'></a>

For _k_ = 3 in Equation (13) (using previous set, soln, of relations)

<a id='35593aad-9f26-4e22-88e4-18065cfaa4d3'></a>

yDer = D[yDer, t];
yCoeff = Simplify[yDer /. t→0];
eqn = yCoeff - (yCoeff /. subst);
eqn = Simplify[eqn /. soln];
newSoln = Simplify[
    Solve[eqn == 0, {Keb, Kocb, Kccb, Kbb, Kdlb, Kdhb, Btb, v0b}]]

<a id='424c3958-eabf-49bc-8134-581e5b871845'></a>

Solve::svars :
Equations may not give solutions for all "solve" variables. More...

<a id='7df3d6b8-7d1a-4afa-b10a-41f5e04882fc'></a>

{{kbb → Bt Kb / Btb, Keb → Ke, v0b → v0}}

<a id='58a446de-cae8-4bf8-adc3-9279b5f48f36'></a>

which gives rise to the following updated set of relations between the components of $\overline{p}$
and p:

<a id='a65fb517-5478-4d0f-ba98-5c3c8eb555d3'></a>

soln = Simplify[soln /. newSoln[[1]]];
soln = Union[soln, newSoln[[1]]]

<a id='24a37180-d385-4d4a-aed2-5ca909a98be4'></a>

{Kbb → Bt Kb / Btb, Keb → Ke, Kib → Ki,
Kmib → Kmi, Kmob → Kmo, v0b → v0}

<a id='08a00ba7-a245-4142-95cc-ee8773da72ad'></a>

The next term in the Taylor series ($k = 4$ in Equation (13)) yields the following information:

<a id='dbf84e10-f498-422b-8301-13af1457f402'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='538d4c19-be12-450f-a3cd-b65d1caadef3'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**:395–417

<a id='48e59f26-8a45-44d7-af0f-836f449cbc98'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='b6182ec9-e10c-4a61-986a-4bc708e462ea'></a>

COMPARTMENTAL MODELLING

<a id='af507d22-c4b8-4a33-ba9a-60293bbfa6a3'></a>

415

<a id='70daf41f-f482-4d1d-b092-fe0298c5398f'></a>

yDer = D[yDer, t];
yCoeff = Simplify[yDer /. t → 0];
eqn = yCoeff - (yCoeff /. subst);
eqn = Simplify[eqn /. soln];
newSoln =

<a id='bc245b9d-6b8d-497a-8b68-9ef4c1ea0fd5'></a>

Simplify[Solve[eqn == 0, {Kocb, Kccb, Kdlb, Kdhb, Btb}]]

<a id='588328ff-76d6-4db4-8e53-37effe16c39f'></a>

Solve::svars :
Equations may not give solutions for all "solve" variables. More...

<a id='66f43dd1-3705-4e21-aabe-da1bdf54c8d1'></a>

{{ Kd1b → Kdh - Kdhb + Kd1, Kocb → Koc }}

<a id='3804d7a8-b433-48d1-b9a4-695c82610610'></a>

and gives rise to the following updated set of relations:
soln = Simplify[soln /. newSoln[[1]]];
soln = Union[soln, newSoln[[1]]]

<a id='8cf336ed-fe9d-439c-a013-e68abdeea0dd'></a>

{Kbb → Bt Kb / Btb , Kdlb → Kdh - Kdhb + Kdl, Keb → Ke,
Kib → Ki, Kmib → Kmi, Kmob → Kmo, Kocb → Koc, v0b → v0}

<a id='a19bc334-dc5f-48bd-abe9-8e0e572d1ebd'></a>

For k = 5 in Equation (13), the following additional relations are obtained:
yDer = D[yDer, t];
yCoeff = Simplify[yDer /. t → 0];
eqn = yCoeff - (yCoeff /. subst);
eqn = Simplify[eqn /. soln];
newSoln = Simplify[Solve[eqn == 0, {Kccb, Kdhb, Btb}]]

<a id='43e1792a-6c20-498a-baf1-b5fb5c01e989'></a>

Solve::svars :
Equations may not give solutions for all "solve" variables. More...

<a id='6a4a9b12-cf58-471c-a541-456ceafac57a'></a>

{{Kccb → Bt Kb (-Kdh + Kdhb) + Kcc Koc / Koc}}

<a id='f0b37996-561e-48e9-9f7f-55d9d8988ce2'></a>

that give rise to the following updated set of relations between the components of p and p:
soln = Simplify[soln /. newSoln[[1]]];
soln = Union[soln, newSoln[[1]]]

<a id='3d16e8db-3d8f-4e87-bf6a-09da073984ec'></a>

{Kbb → Bt Kb / Btb , Kccb → (Bt Kb (-Kdh + Kdhb) + Kcc Koc) / Koc ,
Kdlb → Kdh - Kdhb + Kdl, Keb → Ke, Kib → Ki,
Kmib → Kmi, Kmob → Kmo, Kocb → Koc, v0b → v0}

<a id='46996d32-bff6-465a-a871-1a3617a0bfe8'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='9b48cea2-21c0-492e-9209-673aafdffdab'></a>

Int. J. Adapt. Control Signal Process. 2005; **19**:395–417

<a id='55a387e7-2c29-48b6-8489-4db527632a25'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='2af89ce2-1500-4136-b0e0-0fe8c20b896f'></a>

416

<a id='3125efb0-ce4f-4496-9391-4edb076cddb8'></a>

N. D. EVANS ET AL.

<a id='b6481f51-fdcd-4b97-bd3d-b3a48d4ddb9a'></a>

The final term in the Taylor series expansions needed for the identifiability analysis corresponds to $k = 6$ in Equation (13) and yields the following information:

```
yDer = D[yDer, t];
yCoeff = Simplify[yDer /. t -> 0];
eqn = yCoeff - (yCoeff / . subst);
eqn = Simplify[eqn /. soln];
newSoln = Simplify[Solve[eqn == 0, {Kdhb, Btb}]]
```

<a id='71d86192-63c4-4e08-a9e2-4560802a4389'></a>

{{Kdhb → Kdh, Btb → Bt}}

<a id='7953530d-246b-4b66-a294-e0a567850994'></a>

which gives rise to the complete set of relations between the components of p̅ and p:
soln = Simplify[soln /. newSoln[[1]]];
soln = Union[soln, newSoln[[1]]]


<a id='c94e53ae-6029-45d3-870d-089c2f52ef9f'></a>

{Btb → Bt, Kbb → Kb, Kccb → Kcc, Kdhb → Kdh, Kdlb → Kdl, Keb → Ke,
Kib → Ki, Kmib → Kmi, Kmob → Kmo, Kocb → Koc, v0b → v0}

<a id='24e92f62-70e9-4da3-81de-4ae671605863'></a>

This set shows that for the outputs y(t, p) and y(t, p̄) to be equal it is necessary that p̄ = p and so the model is globally identifiable. Since MATHEMATICA works in terms of generic parameters (in p) the model is seen to be structurally globally identifiable.

<a id='73dd97bf-d203-4d7e-b6c4-4f686611c44a'></a>

ACKNOWLEDGEMENTS

The authors gratefully acknowledge the support of the Engineering and Physical Sciences Research Council of the U.K. under Grants GR/M11943 and GR/R70354, and the Association for International Cancer Research (AICR) for grant support (PJS).

<a id='12a0beae-b08e-42c5-92ef-842b120f5ce8'></a>

REFERENCES
1. Bailly C. Topoisomerase I poisons and suppressors as anticancer drugs. *Current Medicinal Chemistry* 2000; 7:39-58.
2. O'Leary J, Muggia FM. Camptothecins: a review of their development and schedules of administration. *European Journal of Cancer* 1998; **34**(10):1500-1508.
3. Garcia-Carbonero R, Supko JG. Current perspectives on the clinical experience, pharmacology and continued development of the camptothecins. *Clinical Cancer Research* 2002; **8**(3):641-661.
4. Hsiang YH, Lui LF. Identification of mammalian DNA topoisomerase-I as an intracellular target of the anticancer drug camptothecin. *Cancer Research* 1988; **48**(7):1722-1726.
5. Wang JC. DNA topoisomerases. *Annual Review of Biochemistry* 1996; **65**:635-692.
6. Kohn KW, Shao RG, Pommier Y. How do drug-induced topoisomerase I-DNA lesions signal to the molecular interaction network that regulates cell cycle checkpoints, DNA replication, and DNA repair? *Cell Biochemistry and Biophysics* 2000; **33**(2):175-180.
7. Yao S, Murali D, Seetharamulu P, Haridas K, Petluru PNV, Reddy DG, Hausheer FH. Topotecan lactone selectively binds to double- and single-stranded DNA in the absence of topoisomerase I. *Cancer Research* 1998; **58**(17):3782-3786.
8. Gryczynski I, Gryczynski Z, Lakowicz JR, Yang DZ, Burke TG. Fluorescence spectral properties of the anticancer drug topotecan by steady-state and frequency domain fluorometry with one-photon and multi-photon excitation. *Photochemistry and Photobiology* 1999; **69**(4):421-428.

<a id='01e9b468-b248-4ebb-9a30-aa417fcaf894'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='b22e7b92-ed6e-4d1c-831a-3dd9458cdfa2'></a>

Int. J. Adapt. Control Signal Process. 2005; 19:395–417

<a id='0018d34a-8a2a-420e-a52c-db00f4bf30c7'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='59643441-5c47-48a2-b190-bf0cd53db2b1'></a>

COMPARTMENTAL MODELLING

<a id='f8d30c4e-078c-4dcc-a897-b45abba773ed'></a>

417

<a id='aab89426-9287-4aa6-bdcb-6074c7f2dcf4'></a>

9. Evans ND, Errington RJ, Shelley M, Feeney GP, Chapman MJ, Godfrey KR, Smith PJ, Chappell MJ. A mathematical model for the in vitro kinetics of the anti-cancer drug topotecan. Mathematical Biosciences 2004; 189:185–217.
10. Rosing H, Van Zomeren DM, Doyle E, Huinink WWT, Schellens JHM, Bult A, Beijnen JH. Quantification of topotecan and its metabolite N-desmethyltopotecan in human plasma, urine and faeces by high-performance liquid chromatographic methods. Journal of Chromatography B 1999; 727(1–2):191–203.
11. Jacquez JA. Compartmental Analysis in Biology and Medicine (3rd edn). BioMedware: Ann Arbor, 1996.
12. Bellman R, Ástrom KJ. On structural identifiability. Mathematical Biosciences 1970; 7:329–339.
13. Walter E. Identifiability of State Space Models. Springer: Berlin, 1982.
14. Godfrey KR, DiStefano III JJ. Identifiability of model parameters. In Identifiability of Parametric Models, Chapter 1, Walter E (ed.). Pergamon Press: Oxford, 1987; 1–20.
15. Evans ND, Errington RJ, Shelley M, Feeney GP, Chapman MJ, Godfrey KR, Smith PJ, Chappell MJ. Compartmental modelling to assess stability of topotecan bound to DNA. In Proceedings of the Fifth IFAC Symposium on Modelling and Control in Biomedical Systems, Feng DD, Carson ER (eds), Melbourne, Australia. Pergamon Press: Oxford, 21–23 August, 2003; 403–408.
16. Chourpa I, Millot JM, Sockalingum GD, Riou JF, Manfait M. Kinetics of lactone hydrolysis in antitumor drugs of camptothecin series as studied by fluorescence spectroscopy. Biochimica et Biophysica Acta 1998; 1379(3):353–366.
17. Streltsov SA. Action models for the antitumor drug camptothecin: formation of alkali-labile complex with DNA and inhibition of human DNA topoisomserase I. Journal of Biomolecular Structure and Dynamics 2002; 20:447–454.
18. Pohjanpalo H. System identifiability based on the power series expansion of the solution. Mathematical Biosciences 1978; 41:21–33.
19. Tunali ET, Tarn TJ. New results for identifiability of nonlinear systems. IEEE Transactions on Automatic Control 1987; 32:146–154.
20. Vajda S, Godfrey KR, Rabitz H. Similarity transformation approach to identifiability analysis of nonlinear compartmental models. Mathematical Biosciences 1989; 93:217–248.
21. Evans ND, Chapman MJ, Chappell MJ, Godfrey KR. Identifiability of uncontrolled nonlinear rational systems. Automatica 2002; 38:1799–1805.
22. Wolfram S. The Mathematica Book (4th edn). Mathematica Version 4. Wolfram Media/Cambridge University Press: Cambridge, U.K., 1999.
23. Heal KM, Hansen ML, Rickard KM. Maple V Learning Guide (Release 5). Springer: Berlin, New York, 1998.
24. AEA Technology. Facsimile (Version 4.0) Technical Reference. Harwell Laboratory: Didcot, Oxfordshire, U.K., 1995.
25. Clarke GM, Cooke D. A Basic Course in Statistics (4th edn). Arnold: London, 1998.

<a id='1277547c-dd3c-479c-87e5-0fe4c74c0aac'></a>

Copyright © 2005 John Wiley & Sons, Ltd.

<a id='0326a3b6-9ca1-44c7-84dd-2fd0d8a8cfd2'></a>

*Int. J. Adapt. Control Signal Process. 2005; **19**:395–417*

<a id='ccd6bdd6-92e2-4962-9548-2a060cbe1cc5'></a>

10991115, 2005, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/acs.856 by Universita Di Trento, Wiley Online Library on [19/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
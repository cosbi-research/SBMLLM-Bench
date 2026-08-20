<a id='77bda26e-40a9-4754-80e2-3e433be8f928'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='7f17f9e1-259a-4e06-bb93-cfb1ac7e6a98'></a>

<::logo: Elsevier
NON SOLLUS
ELSEVIER
The logo features a detailed illustration of a tree with a figure, a banner with text, and the brand name "ELSEVIER" in orange below it.::>

<a id='60ecadd0-372b-41db-b312-ebfe155d717f'></a>

Contents lists available at ScienceDirect

# Journal of Theoretical Biology

<a id='47f6fa3a-266a-4412-99c0-1dbdf624a28e'></a>

journal homepage: www.elsevier.com/locate/yjtbi

<a id='98d87dea-8d2a-4862-b33e-da91f848d343'></a>

<::logo: Journal of Theoretical Biology (Elsevier)
Journal of Theoretical Biology
Elsevier
The logo features dark red serif text on a light green and white marbled background, with a small publisher's emblem in the top left.::>

<a id='97adf670-00ae-4613-a51d-16d68baa24c6'></a>

Bifurcation and sensitivity analysis reveal key drivers of multistability in a model of macrophage polarization

<a id='bc9819a2-7c15-49d4-a85a-f0822e02bb08'></a>

<::logo: Software Update Feature
Check for updates
A circular icon features a red bookmark symbol on a blue and yellow background, positioned above the text "Check for updates" within a gray button.::>

<a id='90f8676d-bac5-4eb5-894c-e71fd026019e'></a>

Anna S Frank⁰, Kamila Larripⁱ, Hwayeon Ryu⁲, Ryan G. Snodgrass ⁳, Susanna Röblitz ⁰,*
⁰ Computational Biology Unit, Department of Informatics, University of Bergen, Bergen, Norway
ⁱ Department of Mathematics, Humboldt State University, Arcata, CA, USA
⁲ Department of Mathematics and Statistics, Elon University, Elon, NC, USA
⁳ Institute of Biochemistry, Goethe-University, Frankfurt, Germany

<a id='320cd440-3816-49ec-9db6-f8a1c5aec7af'></a>

## ARTICLE INFO

---

**Article history:**
Received 2 July 2020
Revised 24 September 2020
Accepted 1 October 2020
Available online 9 October 2020

---

**Keywords:**
Dynamical Systems
Steady States
Cellular Signaling
Phenotypes

<a id='9d04fbc9-104e-4cf8-a6c2-35901641e436'></a>

ABSTRACT

In this paper, we present and analyze a mathematical model for polarization of a single macrophage which, despite its simplicity, exhibits complex dynamics in terms of multistability. In particular, we demonstrate that an asymmetry in the regulatory mechanisms and parameter values is important for observing multiple phenotypes. Bifurcation and sensitivity analyses show that external signaling cues are necessary for macrophage commitment and emergence to a phenotype, but that the intrinsic macrophage pathways are equally important. Based on our numerical results, we formulate hypotheses that could be further investigated by laboratory experiments to deepen our understanding of macrophage polarization.

© 2020 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license (http:/creativecommons.org/licenses/by/4.0/).

<a id='51847c75-a645-4ccf-b7e8-515d9958cd3e'></a>

# 1. Introduction
Monocytes are immune cells that circulate in the blood and are recruited to (cancer) tissue (Orekhov et al., 2019), where they differentiate into macrophages. Macrophages are highly versatile immune cells which, among other roles, eliminate pathogens and damaged cells through phagocytosis. They play a critical role in innate immunity and help to initiate the adaptive immune response through antigen presentation and cytokine signaling. Due to their diverse functions and plasticity, macrophages are able to exhibit markedly different phenotypes, depending on the external signals they receive, e.g., microbial products, damaged cells, or cytokines. For example, based on cytokines stimulation, macrophages will polarize into different phenotypes, which can be activated (e.g., M1 or M2) or non-activated (e.g., M0) (Orekhov et al., 2019). The continuum of macrophage activation and the diverse spectrum of pro- and anti-inflammatory phenotypes result in nuanced immune regulations (Mosser and Edwards, 2008).

<a id='ae5bc04d-d548-44ec-97c4-67693d0d1841'></a>

A conceptual framework has been developed for the description
of macrophage activation with two polar extremes being the most
widely studied and best understood. On one end of the phenotype
spectrum, M1-like macrophages are classically activated by the

<a id='5c43ebe7-4cfa-4823-8f4a-8243c25a576a'></a>

* Corresponding author.
E-mail addresses: Anna-Simone.Frank@uib.no (A.S Frank), kamila.larripa@hum-boldt.edu (K. Larripa), hryu@elon.edu (H. Ryu), snodgrass@biochem.uni-frankfurt.de (R.G. Snodgrass), Susanna.Roblitz@uib.no (S. Röblitz).

<a id='25e64806-a3cc-4e25-9854-2e0d4f521bf9'></a>

cytokine interferon $\gamma$ (IFN$\gamma$) or by an endotoxin directly (Medzhitov, 2008). Once activated, M1-like macrophages release cytokines that inhibit the proliferation of nearby cells (including cancer cells) and initiate inflammation and an immune response.

<a id='1cd5f056-10fa-458f-bba2-0dec4364c327'></a>

At the other extreme, M2-like macrophages are induced by the interleukins (IL)-4 and -13, cytokines secreted by activated Th2 cells (Gordon, 2003). They tend to dampen inflammation and pro- mote tissue remodeling and tumor progression, for example through pro-angiogenic properties (Brown et al., 2017), immuno- suppression (e.g., IL-10 expression) (Kuang et al., 2009), remodel- ing of the extracellular matrix, or promotion of metastasis (Lin et al., 2001).

<a id='e744008b-c25f-47fe-af9e-8aef05a906a8'></a>

Mixed phenotypes also exist, which share some (but not all) sig-
nificant features with the M1- or M2-like phenotypes (Biswas and
Mantovani, 2010). The existence of mixed phenotypes has been
particularly demonstrated in the tumor microenvironment
(Umemura et al., 2008).

<a id='86f83999-fc8e-4c21-9ae2-f25e2c45c79b'></a>

Macrophage polarization is mediated in part, through the canonical Janus- or TYK2-kinases (JAK)-Signaling signal transducers and activators of transcription (STAT) signaling pathway. Activation of STATs is primarily driven by ligand-stimulated cytokine receptors whereby STATs become phosphorylated at a critical tyrosine residue leading to their release from the receptor complex where they then cross the nuclear membrane and reach chromatin. There they bind specific cognate DNA elements and participate in complex gene regulation processes. STAT phosphorylation kinetics have been extensively investigated in myeloid cells including

<a id='1aee8ba5-9643-418f-93b9-6d487d6986b3'></a>

https://doi.org/10.1016/j.jtbi.2020.110511
0022-5193/© 2020 The Author(s). Published by Elsevier Ltd.
This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

<!-- PAGE BREAK -->

<a id='c115ceda-f552-476f-b812-40cbc65ee246'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='7d4714ad-eadb-4d35-a371-4a773ac5d1cc'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='cb377d28-f181-4344-b8ef-17590f737796'></a>

macrophages. Following stimulation with cytokine signals, STAT phosphorylation, nuclear localization and DNA binding occur (Dickensheets et al., 1999; Namgaladze et al., 2015; Goenka and Kaplan, 2011; Kovarik et al., 1999). The balance between activation of STAT1 and STAT6 tightly regulates macrophage polarization and activity (Wang et al., 2014).

<a id='d3323b88-c7fa-482e-a22d-f4e27d102c53'></a>

Therefore, the phenotype expressed by a macrophage is identified through the specific STAT activation. M1 polarization is associated with STAT1 activity, whereas M2 polarization is associated with STAT6 activity (Martinez and Gordon, 2014).

<a id='6c8b0ca4-02d5-43f8-8e7d-34c948384b10'></a>

The M1 and M2 polarization process is dynamic and can be reversed under certain conditions. Individual macrophages can change their phenotype in response to local signaling cues (Wang et al. (2014); Lawrence and Natoli (2011); Zheng et al. (2017)). This can be especially pronounced in the tumor microenvironment and manifests in tumor associated macrophages, which can demonstrate both pro-tumoral and anti-tumoral activities (Saccani et al., 2006).

<a id='05a30fce-5890-45ae-83ec-0564dd305d26'></a>

Therefore, a better understanding of the polarization process of macrophages has the potential to guide the development of targeted cancer therapy to redirect the polarization towards a tumor suppressing microenvironment (Williams et al. 2016; Zheng et al. 2017; Cheng et al. 2019).

<a id='f6e0586f-cc36-46e2-b122-962c162c8e20'></a>

Mathematical modeling is a useful tool to better understand macrophage polarization by validating or testing hypothesis, and making predictions about possible dynamics. To our knowledge, three previous studies based on ordinary differential equations (ODEs) have modeled macrophage polarization and plasticity (Smith et al. 2016; Nickaeen et al. 2019; Zhao et al. 2019). While the authors in Nickaeen et al. (2019) showed bistable dynamics of macrophage phenotypes when exposed to external signaling cues, the authors in Smith et al. (2016) could show that after initial differentiation into M1 and M2, the M2 phenotype was ultimately dominating. Finally, the authors in Zhao et al. (2019) used a systems-level approach to present the complexity of signaling pathways and intracellular regulation which describe macrophage differentiation under IFN-y, IL-4 signaling, and cell stress (hypoxia). With their model, the authors in Zhao et al. (2019) could replicate experimental results on macrophage phenotype markers and transcription factor regulations upon external perturbations, also for the tumor microenvironment.

<a id='55c17235-40af-43e9-9090-97c3e6913c2f'></a>

All three models are built using generic formulations of self-stimulation and mutual inhibition, which are also common building blocks in immune cell differentiation models (Callard 2007; Yates et al. 2004). Similar modelling approaches as for T-cell differentiation have been used for macrophages in e.g., Nickaeen et al. (2019); Smith et al. (2016), as T-helper cells differentiate in a similar manner (Luckheeram et al. 2012; Martinez and Gordon 2014).

<a id='26192786-d1cd-43c3-9fea-271cd2c10814'></a>

Our goal is to use mathematical modeling to shed light on the polarization and regulatory signaling dynamics related to activation of macrophage phenotypes by specifically tracking STAT1 and STAT6 activation levels as proxies for M1 and M2 polarization, respectively. We aim to build a simple model, which includes less parameters than the previous models, but which shows similar complex dynam-ics. We aim for simplification in model formulation both biologically and mathematically. For the biological aspect, we aim at a simplified circuitry, as opposed to other ODE models that consider more path-ways, e.g. Smith et al. (2016, 2019), or that consider impact from other cells signaling in the immune system and cancer cells (Morales and Soto-Ortiz, 2018). We have consolidated a number of pathways in our model and are viewing macrophages in isolation other than an input signal. From a mathematical point of view, we present a 2-dimensional ODE model that is mathematically simpler than other non-ODE models with more complexity in their formula-tion, such as an agent-based approach (Nickaeen et al., 2019).

<a id='6fe2d6ca-0089-4674-9fe8-ba2c866f9d0e'></a>

The relatively low dimension of our ODE model allows us to conduct bifurcation and stability analyses to study its dynamical diversity, and to relate these dynamics to biological observations. In addition, Sobol's method is employed to i) guide the model reduction and ii) to identify the most sensitive drivers of the system dynamics. Finally, sensitive parameters are altered to study their effect on the dynamics.

<a id='8c1adca7-46e3-48a1-b46f-2ada6d4f2399'></a>

For the rest of this paper, Section 2 describes our mathematical
model in context of macrophage polarization and Section 3 con-
tains the conduction of the numerical methods. In Section 4, our
main results, consisting of bifurcation analysis (Section 4.1), GSA
(Section 4.2) and and perturbation analysis based on GSA results
(Section 4.3), are presented. We conclude with the Discussion in
Section 5. The Appendix section provides more details on numeri-
cal analysis and the applied methodology.

<a id='ea2959a3-3ce1-4149-a238-5289147c2a58'></a>

## 2. Mathematical model

Our mathematical model is based on the interactions specific to the macrophage lineage commitment signaling network. For this purpose, we simplify the network of macrophage functions in the liver from Sica et al. (2014), and consider only IFNγ (input signal S1) and IL-4 (input signal S2) as relevant cytokine signals. The levels of activated STAT1 (variable x₁ ) and STAT6 (variable x₂ ) are used in our model as proxies for the two macrophage activation states.

<a id='69599135-a37d-4c68-8f78-0b90193a8cd9'></a>

A schematic diagram of our model is given in Fig. 1. We model the dynamics of activated STATs with a pair of coupled nonlinear differential equations, described in Eqs. (1,2). The Eqs. (1,2) were adapted from the T-cell model in Yates et al. (2004). They are similar, but not the same, since the equation for x2 has a different structure.

<a id='12ceb0e5-4b9e-4d5f-83b7-e02e5a637624'></a>

\frac{d}{dt}x_{1}=(a_{1}\cdot H^{+}(x_{1},k_{1},n_{1})+S_{1})\cdot H^{-}(x_{2},p_{2},l_{2})+b_{1}-q_{1}x_{1} , (1)
\frac{d}{dt}x_{2}=a_{2}\cdot H^{+}(x_{2},k_{2},n_{2})+S_{2}\cdot H^{-}(x_{1},p_{1},l_{1})+b_{2}-q_{2}x_{2}. , (2)
H^{+}(x_{i},k_{i},n_{i})=\frac{x_{i}^{n_{i}}}{x_{i}^{n_{i}}+k_{i}^{n_{i}}} (3)
H^{-}(x_{i},p_{i},l_{i})=\frac{p_{i}^{l_{i}}}{p_{i}^{l_{i}}+x_{i}^{l_{i}}}. (4)

<a id='8997399e-d55d-4b27-9c02-6ec4941e89eb'></a>

All parameters are assumed to be constant, positive and real numbers, except n_1,2 and l_1,2, which are integers.
The description of all model parameters is provided in Table 1.

<a id='454fd661-8233-4eb8-af60-ce0bb65d3ce1'></a>

2.1. Model formulation

The equation for x₂ is based on the assumption that both type I
and type II interferons inhibit IL-4-induced STAT6 activation in

<::diagram
S₁⊣
b₁ → x₁
  a₁, k₁, n₁
  p₁, l₁ (red inhibiting arrow) → x₂
  p₂, l₂ (green inhibiting arrow) → x₂
x₁ (orange arrow self-stimulation) ↻
q₁ ← x₁
S₂⊣
b₂ → x₂
  a₂, k₂, n₂
  p₁, l₁ (red inhibiting arrow) → x₁
x₂ (orange arrow self-stimulation) ↻
q₂ ← x₂

Fig. 1. Schematic Diagram of Mathematical Model in Eqs. 1,2. Self-stimulation of x₁
and x₂ are represented via the orange arrows, while processes of mutual-inhibition
are shown by red and green inhibiting arrows. The incoming blue arrows depict x₁,₂
activation at basal rates (also in the absence of cytokine signaling), while the
incoming black arrows represent the respective activation of x₁ and x₂ via cytokines
(Sᵢ). Deactivation of x₁,₂ is illustrated by the outgoing black arrows. Note the
asymmetry in that x₂ (STAT2) inhibits both the input signal and self-stimulation,
but x₁ (STAT1) affects only the input signal.
:diagram::>

<a id='42d5dff6-fe9d-4776-87e7-9bf9a0784ab9'></a>



<!-- PAGE BREAK -->

<a id='92a6f708-8df7-40a3-b13b-fcf6648d014e'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='eecf834f-cc11-4cad-9fbe-d08afbd79829'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='36454b0f-9cdf-4e84-a38c-4022ffc398a0'></a>

Table 1
Model parameters in Eqs. 1, 2. Physical units for non-dimensionless parameters are
given in parentheses.
<table id="2-1">
<tr><td id="2-2">Parameter</td><td id="2-3">Description</td></tr>
<tr><td id="2-4">a₁,₂</td><td id="2-5">Strength of self-stimulation (1/day)</td></tr>
<tr><td id="2-6">b₁,₂</td><td id="2-7">Basal activation rates (1/day)</td></tr>
<tr><td id="2-8">n₁,₂</td><td id="2-9">Exponents in the Hill functions for self-stimulation</td></tr>
<tr><td id="2-a">k₁,₂</td><td id="2-b">Thresholds in the Hill functions for self-stimulation</td></tr>
<tr><td id="2-c">I₁,₂</td><td id="2-d">Exponents in the Hill functions for mutual inhibition</td></tr>
<tr><td id="2-e">P₁,₂</td><td id="2-f">Thresholds in the Hill function for mutual inhibition</td></tr>
<tr><td id="2-g">q₁,₂</td><td id="2-h">Deactivation rates (1/day)</td></tr>
<tr><td id="2-i">S₁,₂</td><td id="2-j">Input signal strength (1/day)</td></tr>
</table>

<a id='dec39bca-fd6f-40b9-935c-5a3e9e3a3ddb'></a>

human monocytes in a SOCS-1-dependent manner (Dickensheets et al., 1999), and therefore differs from the model formulation in Yates et al. (2004). This change results in an asymmetry in our equations in that STAT6 inhibits both the input signal and self-stimulation, but STAT1 affects only the input signal (Venkataraman et al., 1999). Furthermore, we reduced model complexity by fixing the Hill coefficient in Eq. (4) to 1. Also, the signal input function in Yates et al. (2004) was simplified to a single parameter (S1, S2, respectively) for each phenotype in our model.

<a id='e5037c52-7634-4109-becc-f245543601b8'></a>

In our model equations, the parameters a_i represent the maximal activation rate of STAT due to self-stimulation. STATs are, however, also activated at low background levels (b_i) in the absence of cytokine stimulation (Dempoya et al., 2012). STATs are also inactivated by dephosphorylation, and we assume this rate is linear (terms q_i x_i in the equations).

<a id='9ec7e0b2-7ff8-4665-a2e4-0bb5aa81dc0a'></a>

The fact that STAT1 and STAT6 are autocrine (Yarilina et al.,
2008; Goenka and Kaplan, 2011), is captured by the stimulating
Hill functions in the model Eqs. (1,2). Finally, we assume respective
activation of STAT1 and STAT6 via IFNγ (S₁) and IL-4 (S₂) (Ohmori
and Hamilton, 1997).

<a id='eea1535f-fa3f-42d9-88a2-d5e1dba5a815'></a>

We use stimulating (Eq. (3)) and inhibiting (Eq. (4)) Hill functions to describe STAT self-stimulation and mutual inhibition (Tyson and Novák, 2010), respectively. The rationale behind the choice of these generic functions is that self-stimulation and inhibition are complex, non-linear processes, which consist of several individual steps. For example, in the process of self-stimulation, cytokines from the macrophage are secreted to stimulate helper T-cell differentiation (Lee, 2019). Differentiated helper T-cells then secrete cytokines which in-turn stimulate the macrophage differentiation. However, detailed knowledge about these individual steps is unknown, which makes it difficult to derive mathematical equations for each step. In addition, we assume that the response in self-stimulation is sigmoidal, depending on the "dose" of input signals. Therefore, the Hill function is used and replaces the need to model the steps individually (Tyson and Novák, 2010). A similar argument was used for the inhibitory Hill function.

<a id='487fd51d-1991-4f9e-9932-fb18537ed455'></a>

In the Hill function of Eq. (3), kᵢ represents the signaling level at which STAT stimulation is half-maximal and the Hill coefficient nᵢ governs the steepness of the Hill function in that as this value grows, the function becomes more switch-like. For the inhibitory Hill function, the parameters play a similar role.

<a id='a27d0db1-d9a6-4da2-b1b5-31387345887d'></a>

## 3. Numerical methods

In this section we provide a detailed description of the numerical methods we employed.

<a id='ff2e4db1-4b22-4374-8af1-ce86a56956a5'></a>

### 3.1. Selection of model parameters

We explore parameter variations and analyze how the different parameter sets affect variability in the system states by using three parameter sets: the initial set Θ₀, and two variation sets, Θ₁ and Θ₂. The parameters in the initial set Θ₀ are adapted from Yates

<a id='96a0be9a-f8af-4f8f-bd5e-7ec2372bdca3'></a>

et al. (2004), while the variation sets Θ₁ and Θ₂ are derived using nullclines.

<a id='48b4a51b-e680-4c4b-bdb7-be8220c68b84'></a>

Parameter sets Θ₀ and Θ₁ are justified, because (i) the model formulation is very similar to the one in *Yates et al.* (2004), (ii) macrophage and T-cell immune responses are connected with respect to, e.g., cytokine signaling (*Lee, 2019*), and (iii) both immune response processes occur in the cell micro-environment. Given the preceding arguments, the same parameter units as in *Yates et al.* (2004) apply here. Since parameter set Θ₂ was derived from Θ₀ and Θ₁ by exploring the numerical properties of the macrophage model, we consider this parameter set also as biologically valid. All three parameter cases are presented in Table 2.

<a id='ffd4e8d6-7024-48a9-b420-f6f67aa6ee22'></a>

The only difference between Theta_0 and Theta_1, is the input signal values representing cytokine signal concentrations (S_i=3.75 vs. S_i=4 for i=1,2). The increase in S_i values from Theta_0 to Theta_1 could resemble a change in environmental conditions, in which input signal strength increases. Also, this change is made based on the nullclines using Theta_0 so that the set Theta_1 results in qualitatively different model dynamics.

<a id='54cf8df5-26fb-4840-83f0-3ffc40aa257f'></a>

Given the model results from Θ₁, we further make parameter variations for Θ₂. Specifically, we increase the strength of self-simulation, aᵢ, and degradation rate qᵢ for each variable. The last change is in the parameter n₁ that has been substantially increased to incorporate the enhanced self-stimulating effect for x₁.

<a id='36148337-def1-47e5-a2f7-b40271d62637'></a>

Finally, recall that the Hill exponents l₁ are set to 1 for all three parameter sets considered. This choice is based on global sensitivity analysis, in which those coefficients are not shown as sensitive parameters to the model dynamics. Moreover, due to the asymmetry in the model equations, an exponent of one in the Hill functions representing mutual inhibition is sufficient to cause multistability, in contrast to, e.g., the Collins toggle switch model (Gardner et al., 2000), which requires Hill exponents larger than one for bistability.

<a id='23697f77-28e5-42f8-a792-7fecc298b52d'></a>

## 3.2. Bifurcation and stability analysis

We expect our model, for all three case scenarios, \Theta_{0,1,2}, to exhibit at least bistable dynamics, similar to the original model. Thus, we first conduct bifurcation analysis to further investigate the impact of different parameter sets on model dynamics.

<a id='2eb5589f-540b-4b96-8a7d-6fa6a76ff8de'></a>

Bifurcation analysis aims to detect critical points of the bifurcation parameters, where the system dynamics change qualitatively in the long-term (Gul et al., 2018). Given the biological importance of external signaling cues (INF-γ and IL-4) in the macrophage polarization process (Wang et al., 2014), we are primarily interested in determining how the system dynamics change based on varying input signals (i.e., S₁ and S₂). We therefore consider S₁ and S₂ as main bifurcation parameters, with the other parameters set to their values in Table 2. The bifurcation diagrams from Eqs. (1,2) were obtained using the software package XPPAUT (Ermentrout, 2001). Details on numerical settings to draw bifurcation diagrams can be found in Appendix A.1.

<a id='bb2e6071-6c1a-4074-b014-497856a31170'></a>

We define states of STAT activation based on model-specific thresholds. An activation level is defined as low, if x_{1,2}≤1.0 and as high, if x_{1,2}>1.0. It is then the ratio of STAT1 to STAT6 activa- tion, that characterizes a macrophage phenotype. The threshold levels are chosen to allow a consistent classification of phenotype cases in our model, although they only represent relative levels. Stability analysis was performed by numerical simulations in Matlab.

<a id='000fda13-6bfa-4435-a74e-9e7464f02bac'></a>

## 3.3. Sensitivity analysis

We perform sensitivity analysis to identify parameter sets that have the greatest influence on the model outputs (e.g., STAT1 and STAT6 activation), and act as key drivers of macrophage polariza-

<a id='3915eccd-8e4c-44b5-8302-d35d165faa13'></a>

3

<!-- PAGE BREAK -->

<a id='5263b6d3-00f2-410d-9887-94d90ba8b085'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='889f5554-d1bc-4d19-8d34-7d02c4c636c7'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='9f10f70a-6047-4398-b95d-5c5455991569'></a>

Table 2
Parameter sets for numerical scenarios. The initial set $\Theta_{0}$ is adapted from Yates et al. (2004). In the two variation sets $\Theta_{1,2}$, bold numbers indicate the variations made compared to
the initial set $\Theta_{0}$.
<table id="3-1">
<tr><td id="3-2">Set</td><td id="3-3">a₁</td><td id="3-4">a₂</td><td id="3-5">b₁</td><td id="3-6">b₂</td><td id="3-7">n_1</td><td id="3-8">n_2</td><td id="3-9">k_1</td><td id="3-a">k_2</td><td id="3-b">l_1</td><td id="3-c">l_{2}</td><td id="3-d">p_{1}</td><td id="3-e">p_{2}</td><td id="3-f">q_{1}</td><td id="3-g">q_{2}</td><td id="3-h">S1</td><td id="3-i">S2</td></tr>
<tr><td id="3-j">Θ₀</td><td id="3-k">5</td><td id="3-l">5</td><td id="3-m">0.05</td><td id="3-n">0.05</td><td id="3-o">6</td><td id="3-p">6</td><td id="3-q">1</td><td id="3-r">1</td><td id="3-s">1</td><td id="3-t">1</td><td id="3-u">0.5</td><td id="3-v">1</td><td id="3-w">5</td><td id="3-x">5</td><td id="3-y">3.75</td><td id="3-z">3.75</td></tr>
<tr><td id="3-A">Θ₁</td><td id="3-B">5</td><td id="3-C">5</td><td id="3-D">0.05</td><td id="3-E">0.05</td><td id="3-F">6</td><td id="3-G">6</td><td id="3-H">1</td><td id="3-I">1</td><td id="3-J">1</td><td id="3-K">1</td><td id="3-L">0.5</td><td id="3-M">1</td><td id="3-N">5</td><td id="3-O">5</td><td id="3-P">4</td><td id="3-Q">4</td></tr>
<tr><td id="3-R">Θ₂</td><td id="3-S">15</td><td id="3-T">8</td><td id="3-U">0.05</td><td id="3-V">0.05</td><td id="3-W">22</td><td id="3-X">6</td><td id="3-Y">1</td><td id="3-Z">1</td><td id="3-10">1</td><td id="3-11">1</td><td id="3-12">0.5</td><td id="3-13">1</td><td id="3-14">5.8</td><td id="3-15">5.8</td><td id="3-16">5</td><td id="3-17">5</td></tr>
</table>

<a id='14fe4a30-ee6c-4024-8349-3b575b0338c9'></a>

tion. Local sensitivity analysis quantifies changes in the model with respect to perturbation of a single parameter at-a-time in the parameter space (Zi, 2011). In contrast to local sensitivity, Global Sensitivity Analysis (GSA) methods explore the effects of large variations of parameter values on model outcome by varying all parameters simultaneously. This difference makes GSA methods more applicable in cellular environments, where it is possible that multiple input parameters vary simultaneously within a large parameter range. We chose Sobol's method (Sobol, 2001) because it makes no assumptions about the relationship between model inputs and outputs in contrast to, for example, the Partial Rank Correlation Coefficient method, which requires monotonicity. Additionally, Sobol's method considers interactions between parameters. A detailed description of Sobol's method can be found in Appendix A.2.

<a id='b37f1abc-8122-4d14-b21b-6a43c1350450'></a>

We implemented Sobol's sensitivity analysis using the SALib package (Herman and Usher, 2017). We varied parameters 15% in each direction from their baseline values (i.e., parameter sets Θ0,1,2 in Table 2). We consider these scenarios separately. In all cases, we generated 300,000 parameter set samples. The selected outcome of interest for the analysis is the ratio of STAT1 to STAT6 activation, which is responsible for macrophage polarization to specific phenotypes.

<a id='04f56b99-62ee-4c71-b4e9-2ff443e8d82d'></a>

### 3.3.1. Perturbation in sensitive parameters
Based on results of the GSA, we explore the effect of perturba- tions in sensitive parameters on macrophage polarization dynam- ics. Firstly, to give an illustrative example, we will only consider perturbations in the most sensitive parameter ($q_2$) on case $\Theta_0$. Understanding the effect of dephosphorylation on system dynam-

<a id='7d89ef81-d747-4008-95ec-0b36c161f0c9'></a>

<::line chart: A 2D line plot titled "(a) Switch Behavior". The x-axis is labeled 't' and ranges from 0 to 40. The y-axis ranges from 0 to 2. Two lines are plotted: a blue line representing 'x_1' and an orange line representing 'x_2'. The blue line (x_1) starts around 1.2, quickly drops to approximately 0.35, remains stable, then increases to about 0.6 around t=22-25, and stabilizes at that value. The orange line (x_2) starts at 2, quickly drops to approximately 1.25, remains stable, then decreases to about 0.35 around t=22-25, and stabilizes at that value. The plot illustrates a switch in the stable values of x_1 and x_2 over time.: chart::>


<a id='0a3b2050-0f02-4eab-9136-9b901e6047db'></a>

<::A 2D phase plane plot. The x-axis is labeled "x_1" and ranges from 0 to 2. The y-axis is labeled "x_2" and ranges from 0 to 2. The plot shows a direction field represented by red arrows. There are three lines plotted: a black line representing a trajectory, a blue line labeled "Nullcline for x_1", and a green line labeled "Nullcline for x_2". The nullclines intersect at multiple points, and the trajectory follows the direction field, crossing the nullclines.: chart::>
(b) Phase Plane with Trajectory

<a id='057908f8-4380-4c2a-bfa8-1bf0e3c96dc3'></a>

<::A 2D plot titled "(c) Basin of Attraction". The x-axis is labeled x_1 and ranges from 0 to 2. The y-axis is labeled x_2 and ranges from 0 to 2. The plot area is filled with two distinct regions of dots. The upper left and lower left portions are filled with red dots. The lower right portion is filled with blue dots. A transition line separates the red and blue regions, starting around (0, 0.5) and curving downwards to around (2, 1). There is an asterisk marker at approximately (0.6, 0.35) within the red dotted region. There is a diamond marker at approximately (1.3, 0.2) within the blue dotted region. A legend in the top right corner indicates: red dots for (0.5952, 0.3545) and blue dots for (1.3152, 0.2166).: chart::>

<a id='b883db63-c371-47be-a986-cd3a716fb0c8'></a>

Fig. 2. (a): Numerical solution that converges to low/low steady state after switch with initial condition (x1,x2) = (1.2, 2); (b): its corresponding trajectory (in solid black) in the phase plane; (c): the basin of attraction for both stable fixed points.

<a id='5e67082a-9dfb-4755-8c47-bd2f518f08cf'></a>

4

<!-- PAGE BREAK -->

<a id='2c1717e0-0d33-4c85-a0cc-83728923b649'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='95d00af7-d9fa-489f-9b17-ee820617238a'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='3ad2608a-d5f6-4db4-9a41-a7e056e091b7'></a>

<::A figure containing two line charts, (a) and (b), depicting tristability. Both charts show variables x1 (blue line) and x2 (red line) plotted against time t, ranging from 0 to 40 on the x-axis and from 0 to 2 on the y-axis. A legend in the top right of each plot identifies the lines as x1 and x2. (a) Tristability: High x2/Low x1. In this plot, x1 starts high and quickly stabilizes around 0.35, while x2 also starts high and stabilizes around 1.3. (b) Tristability: Low x1/x2. In this plot, x1 starts high, drops, then rises to stabilize around 0.65, while x2 starts high and quickly stabilizes around 0.35.::>

<a id='f165009f-dee2-4d4a-95dd-42e87e77efd5'></a>

<::line graph::>A line graph shows two variables, x₁ (blue line) and x₂ (red line), plotted against time 't'. The x-axis ranges from 0 to 40, and the y-axis ranges from 0 to 2. The blue line (x₁) starts at approximately 2, dips to about 1.2, and then stabilizes at around 1.35. The red line (x₂) starts at approximately 1, quickly drops to about 0.2, and then stabilizes at this level. The legend indicates the blue line is x₁ and the red line is x₂. (c) Tristability: High x₁/Low x₂<::>

<a id='ce5ed69f-e18d-48a4-bb54-3da669157b87'></a>

<::(d) Phase Plane with TrajectoriesA phase plane plot with x1 on the x-axis (from 0 to 2) and x2 on the y-axis (from 0 to 2).The plot includes: - Red arrows representing the Direction field. - A blue line representing the Nullcline for x1. - A green line representing the Nullcline for x2. - Three black curves labeled (a), (b), and (c) representing trajectories.: chart::>
<::(e) Basin of AttractionA 2D plot showing basins of attraction with x1 on the x-axis (from 0 to 2) and x2 on the y-axis (from 0 to 2).The plane is divided into three distinct regions, each represented by a different color of dots and corresponding to a specific attraction point: - A green dotted region (top-left) corresponding to the attraction point (0.3565, 1.3150), marked with a black dot. - A red dotted region (bottom-left and central) corresponding to the attraction point (0.6495, 0.3602), marked with a black asterisk. - A blue dotted region (bottom-right) corresponding to the attraction point (1.3768, 0.2232), marked with a white diamond.: chart::>

<a id='44a230c5-4533-4101-86f4-1b41e6f970d4'></a>

Fig. 3. (a)-(c): Numerical solutions that converge to three different stable steady states with initial conditions (a) (x_{1},x_{2})=(1.2,2), (b) (x_{1},x_{2})=(1.2,1.2), and (c) (x_{1},x_{2})=(2,1); (d): their corresponding trajectories (in solid black) in the phase plane; (e): the basin of attraction for each stable fixed point.

<a id='520a29f8-8d19-4845-9eaa-a7161f603dfb'></a>

ics is especially important as deactivation rates change often in biological settings (ten Hoeve et al., 2002). We change q₂ and keep all other parameters fixed. This demonstrates the parameter's indi-

<a id='a21ea6c9-1dda-4f74-8c84-675d0a82404c'></a>

vidual effect on the relation between external input signals and
activation of transcription factors. Secondly, since there exists a
biochemical difference in STAT1 de-/phosphorylation compared

<a id='83b2de6c-b142-4d95-a438-02c31f79512f'></a>

5

<!-- PAGE BREAK -->

<a id='2069c2d4-74af-406d-9f29-dd759599a6ac'></a>

Anna S Frank, K. Larripa, H. Ryu et al. Journal of Theoretical Biology 509 (2021) 110511
<::chart: The image displays four subplots (a, b, c, d) illustrating quadstability.

(a) Quadstability: x₁ vs S₂
This subplot shows a 2D plot with S₂ on the x-axis (ranging from 0 to 20) and x₁ on the y-axis (ranging from 0 to 4). There are two curves: a red curve starting from x₁ ≈ 3.5 at S₂ = 0 and decreasing, then increasing, and a black curve forming a complex S-shape, showing multiple equilibria.

(b) Quadstability: x₂ vs S₁
This subplot shows a 2D plot with S₁ on the x-axis (ranging from -10 to 20) and x₂ on the y-axis (ranging from 0 to 4). A blue dashed vertical line is at S₁ = 0. There are two curves: a red curve starting from x₂ ≈ 4 at S₁ = -10 and decreasing, then increasing, and a black curve forming a complex S-shape, showing multiple equilibria, with parts of it crossing the blue dashed line.

(c) Quadstability: x₁ vs S₁
This subplot shows a 2D plot with S₁ on the x-axis (ranging from -10 to 20) and x₁ on the y-axis (ranging from 0 to 4). A blue dashed vertical line is at S₁ = 0. There are two curves: a red curve starting from x₁ ≈ 1 at S₁ = -10 and increasing linearly, and a black curve forming a complex S-shape, showing multiple equilibria, with parts of it crossing the blue dashed line.

(d) Quadstability: x₂ vs S₂
This subplot shows a 2D plot with S₂ on the x-axis (ranging from 0 to 20) and x₂ on the y-axis (ranging from 0 to 4). There are two curves: a red curve starting from x₂ ≈ 0 at S₂ = 0 and increasing, and a black curve forming a complex S-shape, showing multiple equilibria.:>


<a id='13804c2d-3ed3-4e56-962d-8803cef25a6b'></a>

Fig. 4. The bifurcation diagrams for varying input signals (S₁ and S₂) against the state variables x₁ and x₂ show quadstable dynamics (with the set Θ₂). The red solid lines represent stable fixed points, while the black solid lines represent unstable fixed points and saddle-nodes. The blue dashed line represents the situation where S₁ = 0. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

<a id='16ceb63c-08b2-4f13-a5ef-dc11241d0ca9'></a>

to STAT6 (Droescher et al., 2011,), we will model faster STAT1 deactivation rates ($q_1$) and investigate their effect on model dynamics.

<a id='73d7f019-df0d-4141-bdbf-1005642b9246'></a>

## 4. Model results
The results of the numerical simulations are presented in this section.

<a id='706c8d1c-8115-46cd-8915-4ac8a2eb1d27'></a>

4.1. Bifurcation and stability analysis reveal multistable macrophage phenotypes

<a id='a80c0986-b090-4e91-95b0-1d4769fe8895'></a>

We observe bistability, tristability, and quadstability for different combinations of S$_{1}$ and S$_{2}$ based on the three parameter cases $\Theta_{0,1,2}$ respectively.

<a id='0068c85f-3d17-44c1-ac3f-7208bf9c27cd'></a>

### 4.1.1. Bistable case
With the initial parameter set \( \Theta_0 \) we observe two stable fixed points, exhibiting bistable behavior. These steady states represent state variable ratios (\( x_1/x_2 \)) with i) high/low and ii) low/low levels. Detailed bifurcation diagrams are presented in Fig. 8 in Appendix A.3. We validate this bistable behavior by numerically solving Eqs. (1,2) with the parameter set \( \Theta_0 \). The most interesting behavior observed is that \( x_1 \) and \( x_2 \) go through a switch before converging to

<a id='f3bdd737-ead6-476c-a37f-8eadc5cb2ca8'></a>

their respective stable fixed points, as shown in Fig. 2(a). The solu-
tion trajectory of this switch behavior (in solid black) in the phase
plane is provided in Fig. 2(b). Note that only two fixed points are
present even though there seems to be another fixed point on
the upper left part in the phase plane because of the proximity of
the x₁ - and x₂-nullclines. The bistable behavior is further confirmed
by the basin of attraction shown in Fig. 2(c).

<a id='e79829be-b5d3-4b05-8a13-876d9729900d'></a>

4.1.2. *Tristable case*
With parameter set $\Theta_{1}$, three stable steady states of $(x_{1}/x_{2})$ are observed with i) high/low, ii) low/low, iii) low/high, levels. The third state represents a situation where STAT6 is presented at high levels, while STAT1 is present at low levels.

<a id='66b8ffc9-a87f-4993-9fdb-515456f8a0cf'></a>

Numerical solutions that converge to different stable fixed
points are shown in Fig. 3(a)-(c). The respective solution trajecto-
ries in the phase plane are shown in Fig. 3(d).

<a id='05029d0d-e5ae-41ca-92a7-705114097e6c'></a>

Because of the increased values S₁=S₂=4 for this case, there are two additional intersections between the x₁ and x₂-nullclines compared to the bistable case, as can be seen in the phase plane of Fig. 3(d). This results in the addition of two fixed points, one of which is stable and the other is unstable. Thus, if we start with the same initial condition used in Fig. 2(a), the trajectory converges to the new stable fixed point with high x₂/low x₁, which was not observed in the bistable case. As further confirmed by the basin

<a id='4a145a58-d0fe-41df-b8de-f58eaa7bbc7f'></a>

6

<!-- PAGE BREAK -->

<a id='a7e7d5b8-9c73-4969-be36-58d682e3f264'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='348b5167-3e5f-4c0f-b29d-149c2ff29d28'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='ddb30480-3458-40e8-a6bc-adef9bec9824'></a>

<::Line chart. The y-axis ranges from 0 to 3.5 in increments of 0.5. The x-axis is labeled 't' and ranges from 0 to 40 in increments of 10. The chart shows two lines. A legend indicates the blue line represents x₁ and the orange line represents x₂. The blue line (x₁) starts at approximately 0.8, quickly drops to around 0.35, and then remains constant. The orange line (x₂) starts at approximately 3.0, quickly drops to around 1.9, and then remains constant. (a) Quadstability: High x₂/Low x₁: chart::>

<a id='e2a7cc36-399c-4226-9c18-73e5a3553fe5'></a>

<::A line graph titled "(b) Quadstability: Low x₁/x₂". The x-axis is labeled "t" and ranges from 0 to 40. The y-axis ranges from 0 to 3.5. The graph displays two lines: a blue line labeled "x₁" and a red line labeled "x₂". Both lines start near the y-axis at t=0 and quickly stabilize to constant values. The blue line (x₁) stabilizes around 0.6, and the red line (x₂) stabilizes around 0.4.: chart::>

<a id='69f9d19c-a607-49e8-b376-3a4f49f4c06f'></a>

<::line chart::>A line chart showing two variables, x₁ (blue line) and x₂ (orange line), plotted against time 't'. The y-axis ranges from 0 to 3.5. The x-axis (time 't') ranges from 0 to 40. The blue line (x₁) starts at approximately 1.3 and quickly stabilizes around 1.4. The orange line (x₂) starts at approximately 3.0, rapidly decreases, and stabilizes around 1.5. The legend indicates the blue line is x₁ and the orange line is x₂.(c) Quadstability: High x₁/x₂<::>

<a id='8db04563-c265-42cd-931b-c1f1ff450e0b'></a>

<::line graph::>A line graph showing two variables, x₁ (blue line) and x₂ (orange line), over time (t) from 0 to 40. The y-axis ranges from 0 to 3.5. The blue line (x₁) starts around 1.8, quickly rises to just above 3, and then stabilizes at approximately 3.05. The orange line (x₂) starts around 0.8, quickly drops to just above 0, and then stabilizes at approximately 0.1. Legend: x₁ (blue line), x₂ (orange line). (d) Quadstability: High x₁/Low x₂<::>

<a id='6f9a94b4-c42b-4c67-a2de-c56b2acb3047'></a>

<::chart: A phase plane plot showing the dynamics of a system. The x-axis is labeled "x₁" and ranges from 0 to 3.5. The y-axis is labeled "x₂" and ranges from 0 to 3.5. The plot includes a direction field indicated by red arrows. A blue line represents the nullcline for x₁, forming a curved path with a loop. A green line represents the nullcline for x₂, forming a wavy path. Four black curves represent trajectories, labeled (a), (b), (c), and (d). Trajectory (a) starts in the upper left and moves towards the lower right. Trajectory (b) starts in the lower left and moves towards the upper right. Trajectory (c) starts in the upper right and moves towards the lower left. Trajectory (d) starts in the lower right and moves towards the upper left. The legend specifies: Direction field (red arrows), Nullcline for x₁ (blue line), and Nullcline for x₂ (green line). Caption: (e) Phase Plane with Trajectories::>

<a id='2bf7c93a-65a7-4d01-8423-19db496e52d9'></a>

<::A 2D scatter plot titled "Basin of Attraction" shows four distinct regions colored green, red, purple, and blue, representing basins of attraction. The x-axis is labeled "x₁" and ranges from 0 to 3.5. The y-axis is labeled "x₂" and ranges from 0 to 2.5. Four points are plotted and listed in a legend: a black solid circle at (0.3066, 1.8930) within the green region; a black asterisk at (0.6259, 0.3969) within the red region; a black open circle at (1.3820, 1.5095) within the purple region; and a black diamond at (3.0609, 0.1296) within the blue region.
: chart::>


<a id='115437f8-a4ba-4aa0-87bd-31a5e8512223'></a>

Fig. 5. (a)-(d): Numerical solutions that converges to four different stable steady states with initial conditions (a) (x1,x2) = (1,3), (b) (x1,x2) = (0.8,0.8), (c) (X1,X2) = (3,3), and (d) (X1,X2 = (2, 1); (e): their respective solution trajectories (in solid black) in the phase plane; (f): the basin of attraction for quadstable dynamics.

<a id='5fa047d3-1b55-421b-9e5d-a232ae024ab2'></a>

of attraction of Fig. 3(e), the other two stable fixed points remain as before. Bifurcation diagrams are presented in Fig. 9 in Appendix A.3.

<a id='e56e0f23-fcd9-434e-bc9b-de54ebba0647'></a>

It is the ratio of STAT1 (x~1~) to STAT6 (x~2~) activation levels that
defines the polarization of a macrophage into the M1 or M2 pheno-
type (Wang et al., 2014; Nickaeen et al., 2019). In our results, a high

<a id='4b69ec58-b534-4f66-b9d5-a9673dd2fd19'></a>

level of activated STAT1 in presence of low activated STAT6 levels
defines the M1 phenotype (Fraternale et al., 2015), while low levels
of activated STAT1 and high levels of activated STAT6 define the
M2 phenotype. Low STAT1 and STAT6 activation levels represent
a "hyporesponsive" phenotype that has not been described in the
current literature. This phenotype might however have biological

<a id='c8997ae0-a818-4a85-8e6c-469745a6e6fe'></a>

7

<!-- PAGE BREAK -->

<a id='4a90582c-545c-4be4-a9d2-82c7dcf6308f'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='26b3990b-85e7-40e1-b050-7560ac20ec62'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='18a08092-5494-41c4-9b0e-73c41fb1739b'></a>

<::Bar chart titled "(a) Bistable Case" displaying Sensitivity Index on the y-axis and various parameters (a1, a2, b1, b2, k1, k2, l1, l2, n1, n2, p1, p2, q1, q2, s1, s2) on the x-axis. The chart includes two sets of bars for each parameter: "Total Sensitivity" (blue) and "1st order Sensitivity" (cyan), each with error bars.::>

<a id='47c9a7b9-dd76-4601-ae76-9e4dfdb654ca'></a>

<::Bar chart showing Sensitivity Index for various parameters.
 The Y-axis is labeled "Sensitivity Index" and ranges from 0.0 to 0.5.
 The X-axis displays parameter labels: a1, a2, b1, b2, k1, k2, l1, l2, n1, n2, p1, p2, q1, q2, s1, s2.
 The legend indicates two types of sensitivity:
 - Blue bars: Total Sensitivity
 - Cyan bars: 1st order Sensitivity

 The approximate values for each parameter are as follows (Total Sensitivity, 1st order Sensitivity):
 - a1: (0.04, 0.01)
 - a2: (0.20, 0.02)
 - b1: (0.00, 0.00)
 - b2: (0.00, 0.00)
 - k1: (0.14, 0.04)
 - k2: (0.29, 0.08)
 - l1: (0.04, 0.01)
 - l2: (0.03, 0.00)
 - n1: (0.05, 0.00)
 - n2: (0.07, 0.01)
 - p1: (0.06, 0.01)
 - p2: (0.08, 0.02)
 - q1: (0.39, 0.14)
 - q2: (0.45, 0.18)
 - s1: (0.22, 0.06)
 - s2: (0.18, 0.03)
 Each bar includes error bars.
: bar chart::>
(b) Tristable Case

<a id='0b8ff757-8682-4789-987b-0503493f57c4'></a>

<::Bar chart showing Sensitivity Index. The y-axis is labeled "Sensitivity Index" ranging from 0.0 to 0.5. The x-axis shows various labels: a1, a2, b1, b2, k1, k2, l1, l2, n1, n2, p1, p2, q1, q2, s1, s2. Each x-axis label has two bars with error bars: a blue bar representing "Total Sensitivity" and a cyan bar representing "1st order Sensitivity".
- For a1, Total Sensitivity is around 0.12, 1st order Sensitivity is around 0.03.
- For a2, Total Sensitivity is around 0.38, 1st order Sensitivity is around 0.1.
- For b1 and b2, both sensitivities are close to 0.
- For k1, Total Sensitivity is around 0.07, 1st order Sensitivity is around 0.01.
- For k2, Total Sensitivity is around 0.39, 1st order Sensitivity is around 0.11.
- For l1, Total Sensitivity is around 0.03, 1st order Sensitivity is close to 0.
- For l2, Total Sensitivity is around 0.1, 1st order Sensitivity is around 0.02.
- For n1, Total Sensitivity is around 0.01, 1st order Sensitivity is close to 0.
- For n2, Total Sensitivity is around 0.1, 1st order Sensitivity is around 0.02.
- For p1, Total Sensitivity is around 0.07, 1st order Sensitivity is around 0.01.
- For p2, Total Sensitivity is around 0.06, 1st order Sensitivity is around 0.01.
- For q1, Total Sensitivity is around 0.22, 1st order Sensitivity is around 0.08.
- For q2, Total Sensitivity is around 0.52, 1st order Sensitivity is around 0.21.
- For s1, Total Sensitivity is around 0.03, 1st order Sensitivity is close to 0.
- For s2, Total Sensitivity is around 0.09, 1st order Sensitivity is around 0.02.
(c) Quadstable Case
: bar chart::>

<a id='85bb2bb7-e27b-4fc1-9b75-7266d0cc1a06'></a>

Fig. 6. Sobol Sensitivity Indices where outcome of interest is the ratio of STAT1 activation to STAT6 activation at steady state. This used baseline parameter values which give (a) bistable, (b) tristable and (c) quadstable dynamics. In all instances, the parameter q₂ has the highest total sensitivity index. The cases of bistability and tristability have the same most sensitive seven parameters q₂, q₁, k₂, S₁, k₁ a₂, S₂ with only the ordering of the last three altered. For the quadstable case, q₂ is also the most sensitive, with k₂ and a₂ moving up in the ordering compared to the previous two cases.

<a id='4ef37f65-9912-4dae-a222-d3c6d106ff59'></a>

relevance (e.g., for cancer therapy), as an intermittent phenotype between M1 and M2. For example, recent studies by Bronte and Murray (2015); Castiglione et al. (2016); Linde et al. (2012) have shown that tumors are initially characterized by M1 or an inter- mittent phenotype state, while advanced cancer is defined by M2 phenotype. It is therefore possible that this "hyporesponsive" phe- notype describes another intermittent phenotype that appears during this transition.

<a id='e2f221e0-9a85-48e6-bb67-25dcfbe86a7b'></a>

4.1.3. Quadstable case
Using the last parameter set Θ₂, our model demonstrates quadstable behavior. The detailed bifurcation diagrams are provided in Fig. 4, where red solid lines represent stable fixed points, and black solid lines represent both unstable fixed points and saddle-nodes. Three of the stable fixed points, i.e., low/low, high/low and low/high, (in Fig. 4(a)–(d)) are qualitatively the same as those in the tristable case.

<a id='c8f636fa-29ba-44bb-bc66-3e74cc6c847f'></a>

The situation where both STAT1 and STAT6 have high activation status is, however, unique to the quadstable case. High activation of both STAT1 and STAT6 shows the existence of an intermittent phenotype (Biswas and Mantovani, 2010), which bears characteris-

<a id='b9df45c2-1f34-4459-adb5-6576391dbff5'></a>

tics of both the M1 and M2 types. Several of such intermittent states have been identified, for example, M2a, M2b, M2c and M2d (Palma et al., 2018). The intermittent phenotype can also represent a transformation state, in which M1 branches to M2, and vice versa (Das et al., 2015).

<a id='16d14e1b-b9c9-40e5-a98a-8ec5fd151f32'></a>

To understand how a varying input signal changes the activa- tion of STAT1 and STAT6, we illustrate, based on Fig. 4(b)-(c), how one should read the bifurcation diagram: Fig. 4(b)-(c) have to be read simultaneously, starting from S₁ = 0 and then increasing the S₁ value while following the bifurcation trend. Note that while S₁ is varied, all other parameters values are kept unchanged. By varying S₁ from 0 to around 12, x₁ is on the lowest stable branch while x₂ is on the highest stable branch. Increasing S₁ input signal beyond 12, x₁ and x₂ will follow the bifurcation trend up and down, respectively, to the next stable branch with x₁ activation level between 1 and 2.2, and x₂ activation level between 1.8 and 1.3. To reach the third stable branch, input signal S₁ is decreased (to follow the bifurcation trend) until x₁ and x₂ jump from the second red branch to the third branch. The third branche spans values between 0.3 and 1 for x₁, and values between 0.3 and 0.7 for x₂. When on the third branch, S₁ input signal will be increased again,

<a id='369efea0-4053-4807-9e23-b05048b41251'></a>

8

<!-- PAGE BREAK -->

<a id='b1578321-4a03-4bf1-9ba7-532d902b528b'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='409a0733-38ce-4f42-a644-012a25d10738'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='ce6f80ec-49bb-47b7-a8a4-b624974be4d6'></a>

<::A 2D line plot titled "(a) Perturbed q_2-value: x_1 vs S_2". The x-axis is labeled S_2 and ranges from 0 to 20. The y-axis is labeled x_1 and ranges from 0 to 4. Multiple colored lines are plotted, showing complex, multi-branched curves. Several curves are labeled with numbers 1, 2, 3, and 4 near the top-left section of the plot.: chart::>

<a id='04624015-bf8f-4418-8e6e-405be0eef2c7'></a>

<::chart
Title: (c) Perturbed q₂-value: x₁ vs S₁
Description: A 2D line plot showing x₁ on the y-axis (ranging from 0 to 4) against S₁ on the x-axis (ranging from 0 to 20). Multiple colored curves are depicted, some with labels '1', '2', '3'.
Caption: Fig. 7. Case Θ₀ for varying q₂-values (q₂ = 3.8-label 1, q₂ = 4.5-label 2, q₂ = 6.9-label 3). Magenta and orange represent unstable branches, while blue, red, light green and dark green represent stable branches. (For interpretation of the references to color in this legend, the reader is referred to the web version of this article.)
::>

<a id='0e13af85-b8aa-4f45-a551-9938e58a5f1b'></a>

<::line chart: The chart shows multiple colored curves representing x2 versus S1. The x-axis is labeled "S1" and ranges from 0 to 20 in increments of 2. The y-axis is labeled "x2" and ranges from 0 to 4 in increments of 1. There are several distinct curves: a blue curve starting high on the left and ending low on the right; a red curve starting around x2=2, dipping down, and then rising; a green curve starting around x2=1.8, dipping down, and then rising; a black curve with labels "1" and "2" showing a loop; a cyan curve labeled "3" showing a smaller loop; and a magenta curve with a label "4" showing another loop. The curves exhibit complex, non-monotonic behavior. (b) Perturbed $q_2$-value: $x_2$ vs $S_1$ ::>

<a id='cd0832d8-c436-4d95-aec3-1aed734cdb27'></a>

<::chart: A 2D plot titled "(d) Perturbed q₂-value: x₂ vs S₂". The x-axis is labeled S₂ and ranges from 0 to 20. The y-axis is labeled x₂ and ranges from 0 to 4. Multiple curves are plotted: a blue curve, a red curve, a light green curve, a dark green curve, a black curve, a cyan curve, a magenta curve, and an orange curve. The magenta curve is labeled '1', the black curve is labeled '2', the cyan curve is labeled '3', and the orange curve is labeled '4'. The description states: "-label 4) with respect to baseline q₂-value (q₂ = 5–label 3). The colors, magenta, bark green represent stable ones. (For interpretation of the references to colour in this figure)"::>

<a id='f47ca515-9c62-48d4-b7dc-0f6ea9264ce1'></a>

at an input signal of around 7, both x₁ and x₂ will jump onto the
respectively highest and lowest branch. Fig. 4(a)-(d) can be read
similarly.

<a id='660fafc1-a60d-4f3d-9681-a27d50fde292'></a>

In Fig. 4(b)–(c), we observe furthermore that for high, S₁ > 18 levels, the state variables x₁ and x₂ are committed to highest and lowest activation levels, respectively.

<a id='6205f9ec-cf38-4bec-bd11-a93e54dd0b73'></a>

It is interesting that in the case of quadstability, the system is committed to the high/low state (see Fig. 4(b)–(c)) for high S₁ values, while this could not be observed for bistable or tristable situations. Biologically, an irreversible switch into the M1 phenotype means that the macrophage will no longer be able to change its phenotype when exposed to changing input signals. This suggests that for high self-stimulation in the presence of high INFγ and low IL-4 signals, the system can commit to M1 phenotype and stay reversible for the M2 phenotype. In parameter set Θ₂, STAT1 has higher self-stimulation than STAT6, i.e., a₁ > a₂ and n₁ > n₂. This might be a crucial driver for the commitment in the quadstable case, and the emergence of the intermittent phenotype.

<a id='c83b5ce3-2a78-4b2b-a755-8e4e4907c7f0'></a>

Numerical solutions that converge to different stable points are shown in Fig. 5(a)–(d). Their respective solution trajectories are presented in Fig. 5(e). The basin of attraction of Fig. 5(f) shows

<a id='d3a083ec-1d07-470d-bcc0-901b76b24d4b'></a>

the total of four stable fixed points, which indicates the quadstable dynamics.

<a id='2db194f2-2861-45dd-a61f-69f5d2297ce7'></a>

*4.2. Identification of key drivers of macrophage dynamics through global sensitivity analysis*

<a id='875b829b-55d3-4264-8036-375c28fadb97'></a>

We applied Sobol's method to the model output to identify the most sensitive parameters in our system. Because our goal is to identify phenotype commitment, and because we use STAT1 and STAT6 as proxies for the M1 and M2 phenotype, respectively, our model outcome of interest is the ratio of STAT1 and STAT6 at steady state: $f(x) = \frac{x_1}{x_2}$ when $dx_1/dt = dx_2/dt = 0$. Details of the implementation are included in Appendix A.2. The most sensitive parameters for the bistable case using total sensitivity as a metric are, in descending order, $q_2, q_1, k_2, S_1, k_1, a_2, S_2$ (see Fig. 6(a)). The four most sensitive parameters for bistable and tristable cases, shown in Fig. 6(a)-(b), respectively, agree and the next three most sensitive for each case are common ($k_1, a_2, S_2$) but reordered. Fig. 6(c) shows that the most sensitive parameters in the quadstable case are consistent with results from the previous two cases.

<a id='70ab3e82-e81c-4e9f-b931-a9f70e87e884'></a>



<!-- PAGE BREAK -->

<a id='2f4b3c36-42b5-4219-9d0e-629918030e5c'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='155b60e2-233a-4c84-980f-ec0adb66c066'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<::chart: (a) Bistability: x₁ vs S₂
Bifurcation diagram with X₁ on the y-axis (0 to 2, labeled 0, 0.5, 1, 1.5, 2) and S₂ on the x-axis (0 to 15, labeled 0, 5, 10, 15). A red curve starts near (0,0), increases, then folds back forming a loop, and continues rightward, decreasing. A black curve represents a segment of the loop.::>
<::chart: (b) Bistability: x₂ vs S₂
Bifurcation diagram with X₂ on the y-axis (0 to 2, labeled 0, 0.5, 1, 1.5, 2) and S₂ on the x-axis (0 to approximately 5, labeled 0). A red curve starts near (0,0), increases, then folds back forming a loop, and continues upward. A black curve represents a segment of the loop.::>

<::chart: (c) Bistability: x₁ vs S₁
Bifurcation diagram with X₁ on the y-axis (0 to 2, labeled 0, 0.5, 1, 1.5, 2) and S₁ on the x-axis (0 to 15, labeled 0, 5, 10, 15). A red curve starts near (0,0), increases, then folds back forming a loop, and continues rightward, increasing. A black curve represents a segment of the loop.::>
<::chart: (d) Bistability: x₂ vs S₁
Bifurcation diagram with X₂ on the y-axis (0 to 2, labeled 0, 0.5, 1, 1.5, 2) and S₁ on the x-axis (0 to approximately 5, labeled 0). A red curve starts near (0,0), increases, then folds back forming a loop, and continues upward. A black curve represents a segment of the loop.::>

Fig. 8. The bifurcation diagrams for varying input signals (S₁ and S₂) against the state variables x₁ and x₂.

<a id='f148a467-e2dc-4106-b493-1fa510e4d75d'></a>

<::chart: A bistability plot showing X₂ on the y-axis (from 0 to 2) against S₁ on the x-axis (from 0 to 15). The plot features a curve, partially red and partially black, demonstrating bistable dynamics. The curve rises, forms a loop, then descends and flattens out.::>

(b) Bistability: x₂ vs S₁

<::chart: A bistability plot showing X₂ on the y-axis (from 0 to 2) against S₂ on the x-axis (from 0 to 15). The plot features a curve, partially red and partially black, demonstrating bistable dynamics. The curve rises, forms a loop, descends, and then rises sharply again.::>

(d) Bistability: x₂ vs S₂
nst the state variables x₁ and x₂ show bistable dynamics (with the set Θ₀).

<a id='25e86e9e-be76-4f5e-ad79-d6c9751f51b1'></a>

In terms of the pathways, this indicates that deactivation rates of both STAT1 and STAT6 (q₁ and q₂, respectively) are highly sensitive, as well as the input signal for M1 polarization, INFγ (S₁). Parameters k₂ and k₁ are also sensitive, and both relate to the response of the Hill functions for self-stimulation. These parameters govern the concentration at which the switch takes place. In all cases, k₂ is more sensitive than k₁. Parameters S₂ and a₂ are the signaling input for M2 polarization (IL-4) and the maximum rate at which STAT6 stimulates its own activation via a regulative feedback mechanism.

<a id='c28bbf3c-fdbe-435e-9c6e-56f4dd4ee885'></a>

4.3. Effect of perturbation in deactivation rates q₁ and q₂

Fig. 7 illustrates that by perturbing q₂ the response of transcription factors to input signals changes. The change in response seems to occur with respect to the strength of the input signal, as well as according to stability. For example, in Fig. 7(b)–(c), lower q₂ values seem to increase the number of stable states, and to increase the external stimuli needed to evoke a fate change. This example indicates that deactivation rates can contribute to the robustness of the dynamical system to variations in external stimuli. In particular, it illustrates that deactivation of STAT1 and STAT6 plays an essential role in macrophage polarization, as deactivation rates indirectly

<a id='5c4fde67-aee3-4ed2-9028-ea5aaab91df9'></a>

affect inhibition of external input signals on the opposite state
variable, while self-stimulation affects its own state variable.

<a id='6f45400f-9441-4afd-a719-f352e861c3ab'></a>

For all three parameter sets (Θ$_{0,1,2}$), an increase in the deactivation rate for STAT1, q$_{1}$, leads to a reduction in the number of steady states. For example, in the quadstable case, the system shows first tristability, then bistability, and finally monostability upon an increase of q$_{1}$, whereby first the high/high, then the low/high, and finally the low/low steady state disappear. Consequently, a system with faster STAT1 deactivation rate tends to polarize more strongly towards the M2 phenotype.

<a id='8768d8a3-ef6d-4191-8e91-80c7af99e175'></a>

## 5. Discussion

In this work, we develop and explore a novel mathematical model for the dynamics of macrophage polarization and identify key parameters of the multi-stable dynamics. We validate that macrophage polarization is not strictly bipolar, but can consist of multiple phenotypes. Ours is the first 2-dimensional macrophage polarization model to show bistable, tristable and quadstable phenotypes. The insight gained from our model is that asymmetry in the model equations together with high non-linearity can result in high multi-stability. This is an important advance as we could validate previous biological findings on macrophage phenotypes, which so far have only been demonstrated by more detailed, com-

<a id='c98ba9a7-f933-4559-a5b9-b5dcc91f4a56'></a>

10

<!-- PAGE BREAK -->

<a id='a7064fb4-c748-4b51-a87e-fcc4770529fd'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='ccee4426-0012-4f5d-a76b-d7ab53cc8f12'></a>

Anna S Frank, K. Larripa, H. Ryu et al.Journal of Theoretical Biolog<::chart:Fig. 9. The bifurcation diagrams for varying input signals (S1 and S2) against the state variables x1 and x2 show tristable dynamics (with th
(a) Tristability: x1 vs S2
    - Y-axis: X1, from 0 to 2
    - X-axis: S2, from 0 to 15
    - A curve showing bifurcation, with red and black segments.
(b) Tristability: x2 vs S1
    - Y-axis: X2, from 0 to 2
    - X-axis: S1, from 0 to 15
    - A curve showing bifurcation, with red and black segments.
(c) Tristability: x1 vs S1
    - Y-axis: X1, from 0 to 2
    - X-axis: S1, from 0 to 15
    - A curve showing bifurcation, with red and black segments.
(d) Tristability: x2 vs S2
    - Y-axis: X2, from 0 to 2
    - X-axis: S2, from 0 to 15
    - A curve showing bifurcation, with red and black segments.::>

<a id='d62c31a7-08a3-4a9f-9935-b7f761209c4f'></a>

plex and multidimensional (dimensions > 2) macrophage models
e.g., Zhao et al. (2019), Nickaeen et al. (2019).

<a id='3bb74015-cc98-4a02-9704-c15aa76453e8'></a>

We could validate known phenotypes (i.e., M0, M1 and M2) and have uncovered an unknown, intermittent one (i.e., high/high) with a mixed phenotype expression (Orekhov et al., 2019). From a biological perspective, the intermittent phenotype might more likely be observed in in vivo settings than the extreme M1 and M2 cases, which are studied in cell cultures. According to Andrecut et al. (2011), the low/low state is a "metastable state of indeterminicy", which can switch to either M1 or M2 dependent on the input signals. This state is characterized by the fact that both STATs are at low expression level and is, according to Andrecut et al. (2011), characteristic for multipotent cells. Besides Andrecut et al. (2011), such an undetermined state has been previ- ously described in Nickaeen et al. (2019) for macrophages and in Yates et al. (2004) for T-cells. Given the characteristics of the low-low state, it is represented in a biological context by non- activated macrophages (Orekhov et al., 2019). Although, we cannot rule out that there exist more than four different phenotypes for our system, our findings are supported by those in Lu et al. (2013), where the authors identified a maximum of four stable states given a similar model formulation. To our knowledge, only one previous study by Nickaeen et al. (2019), which studied a more complex model and applied also two- and three-dimensional bifur- cation analyses, could identify a broader spectrum of known (e.g., M2a and M2b) and unknown macrophage phenotypes. Our identi-

<a id='2744fdd1-998f-4b2b-be56-6244be12aeff'></a>

fied unknown phenotype can however not be compared directly to those in Nickaeen et al. (2019), because the authors classified STAT activation into high, medium and low levels, while we only made a distinction between high and low. In addition, such classification states are model dependent.

<a id='0b7c00ac-6c2b-402f-80ec-a7c23cd96470'></a>

Both our work and Yates' paper (Yates et al., 2004) are examples of immune cell polarization modeled through the STAT pathways (in our case, macrophages, in Yates' case, helper T cells). The STAT pathway is a paradigm for membrane to nucleus signaling and has come to explain how a broad range of soluble factors, including cytokines, mediate cells' diverse functions, including polarization (Seif et al., 2017; Leonard, 2001; Villarino et al., 2017). Our model formulation is specific to what we know and understand about macrophage polarization in terms of specifically considering the signals IL-4 and IFNγ, but general STAT pathway modeling could be applicable to a wide variety of immune cells. By comparing models for different cell types (in which the models are parameter-ized with biologically justified values), a sensitivity analysis could reveal which parameters are most important for specific cell types.

<a id='12864d36-e6c2-4926-869d-b7ad017a05d0'></a>

Sensitivity analysis of our model revealed the high impact of the deactivation rates, $q_2$ and $q_1$, on the ratio of STAT1 to STAT6 activation at steady state, used as a proxy for M1 and M2 phenotype, respectively. Parameters $k_2$ and $a_2$ were also identified as sensitive because both of these parameters are related to the self-stimulation of STAT6 activation.

<a id='1438c927-1cb3-40c0-a54b-8075732f078d'></a>

11

<a id='8a62e7ae-23c0-4088-971b-9629239e2ede'></a>

he set Θ1).

<!-- PAGE BREAK -->

<a id='2a69849b-bb6b-4085-aa90-75b63ecc8c44'></a>

Anna S Frank, K. Larripa, H. Ryu et al.

<a id='50d587ab-b927-4c3a-86fa-f25b35404dd5'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='41c8e1d9-420c-4f79-b961-6a6c2ef7f533'></a>

Our most sensitive model parameters are similar to those identified in Torres et al. (2019,). The most sensitive parameters in our model ($k_1, k_2, a_2, q_1, q_2$) and in the models by Torres et al. (2019,) are parameters of activation and deactivation. The agreement in the sensitive parameters of our model with the previous models can therefore be considered a validation of the sensitivity analysis results.

<a id='e26d4f3b-9b0b-499c-b39f-e404a1e736bb'></a>

These sensitive parameters agree with results of our bifurcation analysis, where parameters of self-stimulation and deactivation seemed to have a profound impact on the dynamics. For example, in the quadstable case, parameters of self-stimulation might explain the observed system commitment and the emergence of an additional phenotype, while results of varying deactivation rates changed the response to external signaling cues, as can be seen in Fig. 7. It should be noted that the observed commitment to a phenotype is not specific to this macrophage model, but rather a generic property of a toggle switch circuit model type, of which the macrophage model is a variant. However, our results are unique in the sense that they identify the parameters that drive phenotype commitment, and thus might help in replicating macro-phage phenotype commitment in, e.g., laboratory experiments. The consistency in identifying sensitive parameters from bifurcation and sensitivity analyses is however expected, because a properly designed analysis should reveal bifurcation parameters to be sensitive (Marino et al. (2008)).

<a id='25c7e553-fd82-4217-9c29-2ff96717be47'></a>

In summary, bifurcation and sensitivity analyses showed that external signaling cues are necessary for macrophage commitment and emergence to a phenotype, but that the intrinsic macrophage pathway (represented by self-stimulative factors and deactivation) are equally important (Geeraerts et al., 2017; Biswas and Mantovani, 2012). It should be noted that the intrinsic pathways, which enabled fate commitment in the quadstable situation, are masked by the generic nature (i.e., Hill function) of our model. Intrinsic pathways in macrophages are in general variable (Geeraerts et al., 2017).

<a id='5b88d4f3-23f1-4d40-bfbc-002e333a325c'></a>

Our results support the expectation from the model diagram (Fig. 1) that the system's outcome also depends crucially on the self-stimulation of x2. Because the equations are not symmetric (i.e., in the second equation the stimulatory and inhibitory Hill functions are additive, not multiplicative as in the first equation), the parameters associated with STAT6 have a stronger impact on the model outcome. This observation is also reflected in the asymmetric values of a₁, n₁ and a2, n₂ in Θ2. The asymmetry illustrates that lower values of a2, n₂ have the same effect on systems dynamics as higher values of a₁, n₁. The parameters in Θ0,1 however are symmetric, because they were adapted from the mathematical model in Yates et al. (2004), which has a symmetric model structure. The need for an asymmetry in self-stimulation dynamics of STAT1 and STAT6 might be explained by the experimental finding that the signaling pathway induced by IFN-γ. dominates over the signaling pathway induced by IL-4, according to the authors in Piccolo et al. (2017). This explanation is furthermore in accordance with our finding of an irreversible switch to the M1 phenotype for high concentrations of INF-γ.

<a id='56b75b99-b101-4c5c-9c7d-9cb1f0120fe2'></a>

Although our model was build based on the inhibition of STATS activation via the SOCS inhibitors, we could also connect our results to the effect of another STAT1 inhibitor, namely, the SUMO conjugation (Droescher et al., 2011; Begitt et al., 2011), thanks to the general model formulation. SUMO conjugation leads to the biochemical difference in STAT1 de-/phosphorylation dynamics compared to STAT6 (Droescher et al., 2011). We investigated its effect by analyzing faster STAT1 deactivation rates, which seem to drive the model dynamics towards the M2 phenotype.

<a id='97556cfa-9a76-4d41-92a9-1a4a7e4fd632'></a>

Furthermore, we illustrated how STAT deactivation impacts
macrophage polarization by influencing the robustness to external

<a id='72a2453d-6291-43f1-b127-74d04ee61086'></a>

stimuli. The authors in Sridharan et al. (2015) pointed out that the effects of deactivation are, however, not well understood for macrophages. Therefore, future experiments could aim at inhibit- ing kinase or phosphatase activity, in order to quantify the (de-) phosphorylation rates with time (Gelens and Saurin, 2018). For example, applying the small molecule inhibitor for SUMOylation, that was recently developed by Lv et al. (2018), could yield good parameter estimates and thereby shed further insight through additional experiments. Finally the knowledge of sensitive param- eters for macrophage polarization might guide the conduction of future laboratory experiments and thus deepen our understanding of macrophage polarization.

<a id='b9eeacba-07fa-4a49-9aba-9eaaa625033d'></a>

Recent work (O'Neill et al., 2016; Galván-Peña and O'Neill, 2014; Kelly et al., 2015) indicates a resurgence of interest in immunometabolism and has revealed that through polarization, macrophages undergo a specific metabolic remodeling. M1-like inflammatory macrophages are known to employ a rapid activation of aerobic glycolysis to generate ATP (Ryan and O'Neill, 2020). Inhibition of aerobic glycolysis in macrophages blocks the M1-like phenotype even in the presence of IFNγ (Wang et al., 2018). Aerobic glycolysis is of particular importance in the STAT1 gene transcription pathway in IFN-γ stimulated macrophages (Mills et al., 2016) due to its production of ATP from glycolytic throughput (Wang et al., 2018). Although glycolysis is not as efficient at generating ATP as its alternative pathway (oxidative phosphorylation), it can be upregulated many-fold and therefore results in a faster production of ATP compared with oxidative phosphorylation (Phan et al., 2017).

<a id='717934ac-f0fd-4961-a63b-dd89454c2d33'></a>

In sum, we suggest the following hypotheses, which resulted from our analyses, to be tested experimentally:

<a id='e9e963d3-20fa-4d6c-b017-51c6fbf8baaf'></a>

H1: The response-time and sensitivity of STATs to cytokine signaling levels can be altered by changing deactivation rates.
H2: Once macrophages are committed to a phenotype, further stimulation via cytokines leaves them unchanged.
H3: Intrinsic pathway characteristics, which correspond to aspects of self-stimulation and deactivation, determine the range and variability of observable macrophage phenotypes.
H4: There exist intermittent phenotypes with equal STAT activation levels (i.e., defined by STAT phosphorylation levels) in laboratory experiments settings.

<a id='0f07c00e-4113-41af-8134-a08ec5e8068f'></a>

These hypotheses generate the following suggestions for biological experiments: (1) One could begin with IL-4 polarized macrophages (M2 phenotype) and IFNγ stimulated macrophages (M1 phenotype), and then stimulate each with the opposite cytokine, examining subsequent levels of STAT1/6 phosphorylation in addition to the gene expression of classic STAT6 target genes as well as IFN-stimulated genes (ISGs). This experiment could reveal how dominant one stimuli is compared to the other in terms of re-polarizing cells. Of course, this experiment depends on the concentration of the cytokines, but this can be normalized if one selects concentrations that induce equivalent levels of phosphorylation, nuclear localization and DNA binding. (2) An additional experiment might involve polarizing naïve macrophages with mixed concentrations of IL-4 and IFNγ and collecting the time series data for STAT activation and gene expression of target genes to determine which stimuli is more dominant.

<a id='195c9884-7241-4dff-9403-eea32b0c3625'></a>

## 5.1. Model limitations and future work
A clear advantage of our model is its simplicity and its ability to exhibit complex dynamics in terms of multistability. One limitation due to the simplicity is that spatial distributions or different

<a id='3d4efccc-9d28-4f4c-b744-ba3b9045b469'></a>

12

<!-- PAGE BREAK -->

<a id='17b83f75-6b1e-4d7b-b9e9-3bba5faf1bc2'></a>

_Anna S Frank, K. Larripa, H. Ryu et al._

<a id='377bf805-1226-47a1-ba02-dfd3cfd377bf'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='22b369da-07b9-4fea-bd60-00c1bca1f345'></a>

D = ∫ f²(x) - (f₀)² dx (6)

<a id='735d2677-8b8b-472e-aecc-8aefaf734c38'></a>

The partial variances from squaring and integrating the right hand side of Eq. (5) are of the form

<a id='92cb18fd-95a9-48f5-ad66-1b7b1ed56159'></a>

D_{i_1, i_2, ..., i_k} = \int \cdots \int f^2(x_{i_1}, x_{i_2}, ..., x_{i_s})dx_{i_1} dx_{i_2} ... dx_{i_s} (7)

<a id='3566ec39-0193-4e76-b67b-256fe27896a4'></a>

These integrals can then be approximated with Monte Carlo integration, and the Sobol sensitivity indices are calculated by the ratio of partial to total variance, representing the fraction of total variance which is attributed to individual model parameters or to combinations of parameters.

<a id='5ebbdd9c-e2ef-4a14-8d32-74a3d6394f1d'></a>

S_i1 i2 ... is = D_i1 i2 ... is / D (8)

<a id='86d14fea-4f0e-4f2c-81b7-fa4c4d9b0dca'></a>

Furthermore, the total effect sensitivity index was proffered as an extension of the Sobol sensitivity index to quantify the overall effect of a parameter alone and in combination with any other parameters on model output (Homma and Saltelli, 1996). This is defined to be

$S_{T_i} = S_i + S_{ci}$

(9)

<a id='ec1c18a3-db9e-43ef-a1be-9b62f623c6c3'></a>

where _S_ci is the set of sensitivity indices in which parameter _x_i appears.

<a id='8b1346f6-9754-4a08-a6c7-880abef27bc6'></a>

A.3. Bifurcation diagrams for the bistable and tristable case

<a id='4b0e9021-f7df-4696-9ca2-6ebf313483eb'></a>

Figs. 8 and 9 show the bifurcation diagrams for the bistable and tristable case.

<a id='8164df53-7a7c-4d28-99f3-8c7ecf0f6d6e'></a>

## References
Andrecut, M., Halley, J.D., Winkler, D.A., Huang, S., 2011. A general model for binary cell fate decision gene circuits with degeneracy: indeterminacy and switch behavior in the absence of cooperativity. PloS One 6,. https://doi.org/10.1371/journal.pone.0019358 e193518.

<a id='5a7f6b89-3520-4f7b-b735-842135689e18'></a>

Begitt, A., Droescher, M., Knobeloch, K.P., Vinkemeier, U., 2011. Sumo conjugation of STAT1 protects cells from hyperresponsiveness to IFNy. Blood 118, 1002–1007. https://doi.org/10.1182/blood-2011-04-347930.

<a id='2f09ccaf-8a7c-4810-8876-d45146a8189d'></a>

Biswas, S.K., Mantovani, A., 2010. Macrophage plasticity and interaction with
lymphocyte subsets: cancer as a paradigm. Nat. Immunol. 11, 889–896. https://
doi.org/10.1038/ni.1937.

<a id='6b94678e-3efb-492c-82db-4da25ef5644f'></a>

Biswas, S.K., Mantovani, A., 2012. Orchestration of metabolism by macrophages. Cell Metab. 15, 432–437. https://doi.org/10.1016/j.cmet.2011.11.013.

<a id='3a1e406c-80d0-402f-9e3b-88a2284966fe'></a>

Bronte, V., Murray, P.J., 2015. Understanding local macrophage phenotypes in disease: modulating macrophage function to treat cancer. Nat. Med. 21, 117-119. [https://doi.org/10.1038/nm.3794](https://doi.org/10.1038/nm.3794).

<a id='0c5bbf58-4f7f-415b-b625-b63727324f0b'></a>

Brown, J.M., Recht, L., Strober, S., 2017. The promise of targeting macrophages in cancer therapy. Clin. Cancer Res. 23, 3241-3250. https://doi.org/10.1158/1078-0432.CCR-16-3122.

<a id='714c6f2f-6993-4d98-9f38-cd4cfaee79f6'></a>

Callard, R.E., 2007. Decision-making by the immune response. Immunol. Cell Biol. 85, 300–305.

<a id='facd000f-fbf6-4d24-a089-1ace7e704829'></a>

Castiglione, F., Tieri, P., Palma, A., Jarrah, A.S., 2016. Statistical ensemble of gene regulatory networks of macrophage differentiation. BMC Bioinf. 17, 506. https://doi.org/10.1186/s12859-016-1363-4.

<a id='988e1ee2-9a53-48fd-9364-09e9b3ce6e59'></a>

Cheng, H., Wang, Z., Fu, L., Xu, T., 2019. Macrophage polarization in the development and progression of ovarian cancers: an overview. Front. Oncol. 9, 421. https://doi.org/10.3389/fonc.2019.00421.

<a id='e9d59715-f2bf-465a-863b-6dc3083d1d00'></a>

Das, A., Sinha, M., Datta, S., Abas, M., Chaffee, S., Sen, C.K., Roy, S., 2015. Monocyte
and macrophage plasticity in tissue repair and regeneration. Am. J. Pathol. 185,
2596–2606. https://doi.org/10.1016/j.ajpath.2015.06.001.

<a id='d4324303-de62-4434-8391-4b65b235c13a'></a>

Dempoya, J., Matsumiya, T., Imaizumi, T., Hayakari, R., Xing, F., Yoshida, H., Okumura, K., Satoh, K., 2012. Double-stranded RNA induces biphasic STAT1 phosphorylation by both type I interferon (IFN)-dependent and type I IFN-independent pathways. J. Virol. 86, 12760–12769. https://doi.org/10.1128/JVI.01881-12.

<a id='5cc785c3-60a3-42d6-a240-40c7e82dcb7c'></a>

Dickensheets, H.L., Venkataraman, C., Schindler, U., Donnelly, R.P., 1999. Interferons inhibit activation of STAT6 by interleukin 4 in human monocytes by inducing SOCS-1 gene expression. Proc. Natl. Acad. Sci. USA 96, 10800–10805. https://doi.org/10.1073/pnas.96.19.10800.

<a id='4f68c3ae-6760-4a19-8808-7afbdff6ca3e'></a>

Dorrington, M.G., Fraser, I.D., 2019. NF-κB signaling in macrophages: dynamics,
crosstalk, and signal integration. Front. Immunol. 10, 705. https://doi.org/
10.3389/fimmu.2019.00705.

<a id='bccac19d-952f-4ed7-b49c-5f27320e27cc'></a>

Droescher, M., Begitt, A., Marg, A., Zacharias, M., Vinkemeier, U., 2011. Cytokine-induced paracrystals prolong the activity of STAT transcription factors and provide a model for the regulation of protein-solubility by SUMO. J. Biol. Chem. 286, 18731–18746. https://doi.org/10.1074/jbc.M111.235978.

<a id='c39869b3-47de-47fa-a585-f0360c952f2a'></a>

Ermentrout, B., 2001. XPPAUT 5.0-the differential equations tool. http://www. math. pitt. edu/bard/xpp/xpp. html (accessed November, 2019)..
Fraternale, A., Brundu, S., Magnani, M., 2015. Polarization and repolarization of macrophages. J. Clin. Cell. Immunol. 6, 2. https://doi.org/10.4172/2155-9899.1000319.

<a id='dff12f8a-1637-44fd-a76f-999a1579eb46'></a>

Galván-Peña, S., O'Neill, L.A., 2014. Metabolic reprograming in macrophage
polarization. Front. Immunol. 5, 420.
Gardner, T.S., Cantor, C.R., Collins, J.J., 2000. Construction of a genetic toggle switch
in Escherichia coli. Nature 403, 339-342.

<a id='d9f16867-a3f4-46fd-afa4-a8d9743864b1'></a>

Geeraerts, X., Bolli, E., Fendt, S.M., Van Ginderachter, J.A., 2017. Macrophage metabolism as therapeutic target for cancer, atherosclerosis, and obesity. Front. Immunol. 8, 289. https://doi.org/10.3389/fimmu.2017.00289.

<a id='eb122e15-2444-4fb1-bbd9-702cbfad6b90'></a>

Gelens, L., Saurin, A.T., 2018. Exploring the function of dynamic phosphorylation-
dephosphorylation cycles. Dev. Cell 44, 659-663. https://doi.org/10.1016/j.
devcel.2018.03.002.

<a id='d09ca584-3a9a-4ad9-831b-f0191c58eafc'></a>

Goenka, S., Kaplan, M.H., 2011. Transcriptional regulation by STAT6. Immunol. Res. 50, 87–96. https://doi.org/10.1007/s12026-011-8205-2.
Gordon, S., 2003. Alternative activation of macrophages. Nat. Rev. Immunol. 3, 23–35. https://doi.org/10.1038/nri978.

<a id='6213baee-12e2-43ea-ba51-9655173ff8f3'></a>

Gul, R., Bernhard, S., 2018. Sensitivity analysis: a useful tool for bifurcation analysis.
In: Lopez-Ruiz, R. (Ed.), Complexity in Biological and Physical Systems:
Bifurcations, Solitons and Fractals. Intech Open Limited, London, UK, p. 69.
https://doi.org/10.5772/intechopen.72345. Chapter 4.

<a id='50e36a7c-157e-44c9-bb95-a38ebf6d43cb'></a>

Herman, J., Usher, W., 2017. SALib: an open-source python library for sensitivity analysis. J. Open Source Softw. 2. 10.21105/joss.00097.
ten Hoeve, J., de Jesus Ibarra-Sanchez, M., Fu, Y., Zhu, W., Tremblay, M., David, M., Shuai, K., 2002. Identification of a nuclear STAT1 protein tyrosine phosphatase. Mol. Cell Biol. 22, 5662-5668. https://doi.org/10.1128/mcb.22.16.5662-5668.2002.

<a id='8f6f3c37-c546-4dc5-a810-b4d878287e5d'></a>

Homma, T., Saltelli, A., 1996. Importance measures in global sensitivity analysis of nonlinear models. Reliab. Eng. Syst. Saf. 52, 1–17. https://doi.org/10.1016/0951-8320(96)00002-6.

<a id='b5868259-2c37-4d29-8048-ddd86d22cc0a'></a>

Kelly, B., O'neill, L.A., 2015. Metabolic reprogramming in macrophages and dendritic cells in innate immunity. Cell Res. 25, 771–784.
Kovarik, P., Stoiber, D., Eyers, P.A., Menghini, R., Neininger, A., Gaestel, M., Cohen, P., Decker, T., 1999. Stress-induced phosphorylation of STAT1 at Ser727 requires p38 mitogen-activated protein kinase whereas IFN-γ) uses a different signaling pathway. Proc. Nat. Acad. Sci. 96, 13956–13961.

<a id='6993d7bd-e274-4e7e-9f0a-cd241feccb9e'></a>

Kuang, D.M., Zhao, Q., Peng, C., Xu, J., Zhang, J.P., Wu, C., Zheng, L., 2009. Activated monocytes in peritumoral stroma of hepatocellular carcinoma foster immune privilege and disease progression through pd-11. J. Exp. Med. 206, 1327-1337. https://doi.org/10.1084/jem.20082173.

<a id='008e230e-9986-473d-b399-435ab06950ad'></a>

Lawrence, T., Natoli, G., 2011. Transcriptional regulation of macrophage polarization: enabling diversity with identity. Nat. Rev. Immunol. 11, 750-761. https://doi.org/10.1038/nri3088.

<a id='679dd02c-291c-4c87-8914-1b65fab2b1e9'></a>

Lee, K.Y., 2019. M1 and M2 polarization of macrophages: a mini-review. Med. Biol.
Sci. Eng. 2, 1-5. https://doi.org/10.30579/mbse.2019.2.1.1.
Leonard, W.J., 2001. Role of JAK kinases and STATs in cytokine signal transduction.
Int. J. Hematol. 73, 271-277.

<a id='3fad4c16-c906-4a49-a775-90535b2b0a63'></a>

Lin, E.Y., Nguyen, A.V., Russell, R.G., Pollard, J.W., 2001. Colony-stimulating factor 1 promotes progression of mammary tumors to malignancy. J. Exp. Med. 193, 727-740. https://doi.org/10.1084/jem.193.6.727.

<a id='dd08beb3-b8f4-4a20-b9f1-617a222dfa85'></a>

Linde, N., Gutschalk, C.M., Hoffmann, C., Yilmaz, D., Mueller, M.M., 2012. Integrating
macrophages into organotypic co-cultures: a 3d in vitro model to study tumor-
associated macrophages. PLoS One 7, https://doi.org/10.1371/journal.
pone.0040058 e40058.

<a id='67e82231-65a1-47b5-a9ec-8c71a19c0e50'></a>

Lu, M., Jolly, M.K., Gomoto, R., Huang, B., Onuchic, J., Ben-Jacob, E., 2013. Tristability in cancer-associated microRNA-TF chimera toggle switch. J. Phys. Chem. B 117, 13164–13174. https://doi.org/10.1021/jp403156m.

<a id='bcb369da-e62b-4f5a-ba5c-f13e73ed398c'></a>

Luckheeram, R.V., Zhou, R., Verma, A.D., Xia, B., 2012. Cd4+ T cells: differentiation
and functions. Clin. Dev. Immunol. 2012, https://doi.org/10.1155/2012/925135
925135.

<a id='38638963-a253-4f83-a52e-80ea41816b31'></a>

Lv, Z., Yuan, L., Atkison, J.H., Williams, K.M., Vega, R., Sessions, E.H., Divlianska, D.B.,
Davies, C., Chen, Y., Olsen, S.K., 2018. Molecular mechanism of a covalent
allosteric inhibitor of SUMO E1 activating enzyme. Nat. Commun. 9, 5145.
https://doi.org/10.1038/s41467-018-07015-1.

<a id='1f65bb1b-870c-4b04-afaa-107abcaaf899'></a>

Marino, S., Hogue, I.B., Ray, C.J., Kirschner, D.E., 2008. A methodology for performing global uncertainty and sensitivity analysis in systems biology. J. Theor. Biol. 254, 178-196. https://doi.org/10.1016/j.jtbi.2008.04.011.
Martinez, F.O., Gordon, S., 2014. The M1 and M2 paradigm of macrophage activation: time for reassessment. F1000Prime Rep. 6. 10.12703/P6-13.

<a id='e6a95c27-1e38-41ef-b0ab-c7a44b5debd7'></a>

Medzhitov, R., 2008. Origin and physiological roles of inflammation. Nature 454,
428–435. https://doi.org/10.1038/nature07201.
Mille CT, Vollu D, Logan A, Costa AC, Varma M, Druent CE, Tourlomoucic D

<a id='4bd9b690-4bff-45a1-8a73-3f347ff43c68'></a>

Mills, E.L., Kelly, B., Logan, A., Costa, A.S., Varma, M., Bryant, C.E., Tourlomousis, P.,
Däbritz, J.H.M., Gottlieb, E., Latorre, I., et al., 2016. Succinate dehydrogenase
supports metabolic repurposing of mitochondria to drive inflammatory
macrophages. Cell 167, 457–470.

<a id='0790a3b9-6876-40db-925b-654523c7176f'></a>

Morales, V., Soto-Ortiz, L., 2018. Modeling macrophage polarization and its effect on cancer treatment success. Open J. Immunol. 8, 36.

<a id='44b8e54f-f5c9-4a83-a2c3-503914a03d2c'></a>

Mosser, D.M., Edwards, J.P., 2008. Exploring the full spectrum of macrophage activation. Nat. Rev. Immunol. 8, 958–969. https://doi.org/10.1038/nri2448.

<a id='c00be7dd-50f0-440e-9e76-eb033b9b45cc'></a>

14

<!-- PAGE BREAK -->

<a id='66725f59-d81b-4e58-a170-5e6d4675820d'></a>

_Anna S Frank, K. Larripa, H. Ryu et al._

<a id='1b02063a-0147-4864-a54f-803bb45d892f'></a>

Journal of Theoretical Biology 509 (2021) 110511

<a id='ba323fa8-e03d-4177-8e42-2ea4d9596dea'></a>

Namgaladze, D., Snodgrass, R.G., Angioni, C., Grossmann, N., Dehne, N., Geisslinger, G., Brüne, B., 2015. AMP-activated protein kinase suppresses arachidonate 15-lipoxygenase expression in interleukin 4-polarized human macrophages. J. Biol. Chem. 290, 24484–24494.

<a id='626dde3d-20d1-4222-8f57-8c1a29157f16'></a>

Nickaeen, N., Ghaisari, J., Heiner, M., Moein, S., Gheisari, Y., 2019. Agent-based modeling and bifurcation analysis reveal mechanisms of macrophage polarization and phenotype pattern distribution. Sci. Rep. 9, 12764. https://doi.org/10.1038/s41598-019-48865-z.

<a id='3d04ecdd-8e1c-45a8-93cd-5a5326c177ca'></a>

Ohmori, Y., Hamilton, T.A., 1997. Il-4-induced STAT6 suppresses IFN-gamma-stimulated STAT1-dependent transcription in mouse macrophages. J. Immunol. 159, 5474–5482.

<a id='45c26245-45e0-4b5b-a155-a61ac6cc24ab'></a>

O'Neill, L.A., Kishton, R.J., Rathmell, J., 2016. A guide to immunometabolism for
immunologists. Nat. Rev. Immunol. 16, 553.
Orekhov, A.N., Orekhova, V.A., Nikiforov, N.G., Myasoedova, V.A., Grechko, A.V.,
Romanenko, E.B., Zhang, D., Chistiakov, D.A., 2019. Monocyte differentiation and
macrophage polarization. Vessel Plus 3. 10.20517/2574-1209.2019.04.

<a id='a941c0df-896c-4645-8c2c-7c9555ee535e'></a>

Palma, A., Jarrah, A.S., Tieri, P., Cesareni, G., Castiglione, F., 2018. Gene regulatory network modeling of macrophage differentiation corroborates the continuum hypothesis of polarization states. Front. Physiol. 9, 1659. https://doi.org/10.3389/fphys.2018.01659.

<a id='e16d4f30-73ed-494c-926b-47f770479623'></a>

Phan, A.T., Goldrath, A.W., Glass, C.K., 2017. Metabolic and epigenetic coordination of T cell and macrophage immunity. Immunity 46, 714–729.

<a id='e1a61a31-577b-4fdb-b48d-ee6b845c38ff'></a>

Piccolo, V., Curina, A., Genua, M., Ghisletti, S., Simonatto, M., Sab&ograve;, A., Amati, B., Ostuni, R., Natoli, G., 2017. Opposing macrophage polarization programs show extensive epigenomic and transcriptional cross-talk. Nat. Immunol. 18, 530–540. https://doi.org/10.1038/ni.3710.

<a id='5b212865-1328-4c5f-b2af-6d7f6db7db5e'></a>

Ryan, D.G., O'Neill, L.A., 2020. Krebs cycle reborn in macrophage immunometabolism. Annu. Rev. Immunol. 38, 289-313.

<a id='7627c9df-19ed-4530-b751-2cf632cb6947'></a>

Saccani, A., Schioppa, T., Porta, C., Biswas, S.K., Nebuloni, M., Vago, L., Bottazzi, B.,
Colombo, M.P., Mantovani, A., Sica, A., 2006. p50 nuclear factor-κB
overexpression in tumor-associated macrophages inhibits M1 inflammatory
responses and antitumor resistance. Cancer Res. 66, 11432–11440. https://doi.
org/10.1158/0008-5472.CAN-06-1867.

<a id='33923165-30f2-46b5-a834-6ea4ccf57183'></a>

Seif, F., Khoshmirsafa, M., Aazami, H., Mohsenzadegan, M., Sedighi, G., Bahar, M., 2017. The role of JAK-STAT signaling pathway and its regulators in the fate of T helper cells. Cell Commun. Signal. 15, 1-13.

<a id='eefa11d8-47f5-4e62-b472-9ed2c5cb7dfc'></a>

Sica, A., Invernizzi, P., Mantovani, A., 2014. Macrophage plasticity and polarization in liver homeostasis and pathology. Hepatology 59, 2034–2042. https://doi.org/10.1002/hep.26754.

<a id='0b55f9bd-e26c-4db2-8682-b473f8479a63'></a>

Smith, T.D., Tse, M.J., Read, E.L., Liu, W.F., 2016. Regulation of macrophage polarization and plasticity by complex activation signals. Integr. Biol. (Camb.) 8, 946–955. https://doi.org/10.1039/c6ib00105j

<a id='207facd7-e71a-4bc1-95d5-04e2a3756785'></a>

Sobol, I.M., 2001. Global sensitivity indices for nonlinear mathematical models and their Monte Carlo estimates. Math. Comput. Simulat. 55, 271–280. https://doi.org/10.1016/S0378-4754(00)00270-6.

<a id='a2e7ba46-ffe5-409f-90a3-0a4e06dc4a53'></a>

Sridharan, R., Cameron, A.R., Kelly, D.J., Kearney, C.J., O'Brien, F.J., 2015. Biomaterial
based modulation of macrophage polarization: a review and suggested design

<a id='79b27891-e646-4741-9953-592f98e8871b'></a>

principles. Mater. Today 18, 313–325. https://doi.org/10.1016/j.mattod.2015.01.019.

<a id='77c3b1de-2f59-48d9-b696-435bc6533ff7'></a>

Torres, M., Wang, J., Yannie, P.J., Ghosh, S., Segal, R.A., Reynolds, A.M., 2019.
Identifying important parameters in the inflammatory process with a
mathematical model of immune cell influx and macrophage polarization.
PLoS Comput. Biol. 15, https://doi.org/10.1371/journal.pcbi.1007172
e1007172.

<a id='af5e91da-51bb-4ecf-8a8e-cdd1715b92f3'></a>

Tyson, J.J., Novák, B., 2010. Functional motifs in biochemical reaction networks. Ann.
Rev. Phys. Chem. 61, 219–240. https://doi.org/10.1146/
annurev.physchem.012809.103457.

<a id='6ba13175-393e-4e78-94c6-ce3ce8c3401a'></a>

Umemura, N., Saio, M., Suwa, T., Kitoh, Y., Bai, J., Nonaka, K., Ouyang, G.F., Okada, M., Balazs, M., Adany, R., et al., 2008. Tumor-infiltrating myeloid-derived suppressor cells are pleiotropic-inflamed monocytes/macrophages that bear M1-and M2-type characteristics. J. Leukoc. Biol. 83, 1136-1144. https://doi.org/10.1189/jlb.0907611.

<a id='9d211224-12f7-4780-8fdc-6164c27fca0a'></a>

Venkataraman, C., Leung, S., Salvekar, A., Mano, H., Schindler, U., 1999. Repression of IL-4-induced gene expression by IFN-y) requires STAT1 activation. J. Immunol. 162, 4053-4061.

<a id='89f10e25-1241-4f43-8953-5d05c108098e'></a>

Villarino, A.V., Kanno, Y., O'Shea, J.J., 2017. Mechanisms and consequences of JAK-
STAT signaling in the immune system. Nat. Immunol. 18, 374.
Wang. F.. Zhang. S.. leon. R.. Vuckovic. I.. liang. X.. Lerman. A.. Folmes. C.D.. Dzeia. P.

<a id='41efd1c7-b5dd-4c19-95bf-be0b39b9870d'></a>

Wang, F., Zhang, S., Jeon, R., Vuckovic, I., Jiang, X., Lerman, A., Folmes, C.D., Dzeja, P. D., Herrmann, J., 2018. Interferon gamma induces reversible metabolic reprogramming of M1 macrophages to sustain cell viability and pro-inflammatory activity. EBioMedicine 30, 303-316.

<a id='9c48c852-b4d2-4a18-8989-ca54cbc89ea1'></a>

Wang, N., Liang, H., Zen, K., 2014. Molecular mechanisms that influence the macrophage M1–M2 polarization balance. Front. Immunol. 5, 614. https://doi. org/10.3389/fimmu.2014.00614.

<a id='bb12420d-0003-49b6-b360-096b4c47819f'></a>

Williams, C.B., Yeh, E.S., Soloff, A.C., 2016. Tumor-associated macrophages: unwitting accomplices in breast cancer malignancy. NPJ Breast Cancer 2, 15025. https://doi.org/10.1038/npjbcancer.2015.25.

<a id='ffcb6810-41a3-46cc-9c1d-9455199a498a'></a>

Yarilina, A., Park-Min, K.H., Antoniv, T., Hu, X., Ivashkiv, L.B., 2008. TNF activates an
IRF1–dependent autocrine loop leading to sustained expression of chemokines
and STAT1–dependent type I interferon–response genes. Nat. Immunol. 9, 378–
387. https://doi.org/10.1038/ni1576.

<a id='35cf7644-b8ba-4135-ada5-a752d5dbbf4d'></a>

Yates, A., Callard, R., Stark, J., 2004. Combining cytokine signalling with T-bet and GATA-3 regulation in Th1 and Th2 differentiation: a model for cellular decision-making. J. Theor. Biol. 231, 181–196. https://doi.org/10.1016/j.jtbi.2004.06.013.

<a id='98a34935-93fb-411a-b9c0-0e9f820e2ca1'></a>

Zhao, C., Mirando, A.C., Sov, R.J., Medeiros, T.X., Annex, B.H., Popel, A.S., 2019. A mechanistic integrative computational model of macrophage polarization: Implications in human pathophysiology. PLoS Comput. Biol. 15,. https://doi.org/ 10.1371/journal.pcbi.1007468 e1007468.

<a id='930a308f-2c50-4ee7-9f45-07f51f652bbf'></a>

Zheng, X., Turkowski, K., Mora, J., Brüne, B., Seeger, W., Weigert, A., Savai, R., 2017.
Redirecting tumor-associated macrophages to become tumoricidal effectors as
a novel strategy for cancer therapy. Oncotarget 8, 48436–48452. 10.18632/
oncotarget.17061.

<a id='a4ae7b38-78eb-40f7-a9d5-1b4d1127d182'></a>

Zi, Z., 2011. Sensitivity analysis approaches applied to systems biology models. IET Syst. Biol. 5, 336-346. https://doi.org/10.1049/iet-syb.2011.0015.

<a id='52f577f0-91f5-49ed-9a63-7bdf55d56d5a'></a>

15
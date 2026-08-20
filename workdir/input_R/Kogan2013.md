<a id='1491eb61-1f81-4ffa-a0c7-e17e8acfe91f'></a>

DISCRETE AND CONTINUOUS
DYNAMICAL SYSTEMS SERIES B
Volume 18, Number 4, June 2013

<a id='08b6a78d-3d1b-44e5-be30-ed48f2ea60e2'></a>

doi:10.3934/dcdsb.2013.18.1017

<a id='eb36f8da-b943-4c0e-ae42-3f3d3df5e051'></a>

pp. 1017–1030

<a id='76f0ce7b-5a9f-4a9d-9f13-60f74db0514b'></a>

A MATHEMATICAL MODEL FOR THE
IMMUNOTHERAPEUTIC CONTROL OF THE TH1/TH2
IMBALANCE IN MELANOMA

<a id='2ec13d66-7323-48f4-8bdb-00a8deb29e54'></a>

YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI
10 Hate'ena St., P.O.B. 282, Bene Ataroth 60991, Israel

<a id='fec56892-f6ae-42d3-b71f-41773b0be9f9'></a>

ABSTRACT. Aggressive cancers develop immune suppression mechanisms, allowing them to evade specific immune responses. Patients with active melanoma are polarized towards a T helper (Th) 2-type immune phenotype, which subverts effective anticancer Th1-type cellular immunity. The pro-inflammatory factor, interleukin (IL)-12, can potentially restore Th1 responses in such patients, but still shows limited clinical efficacy and substantial side effects. We developed a model for the Th1/Th2 imbalance in melanoma patients and its regulation via IL-12 treatment. The model focuses on the interactions between the two Th cell types as mediated by their respective key cytokines, interferon (IFN)-γ and IL-10. Theoretical and numerical analysis showed a landscape consisting of a single, globally attracting steady state, which is stable under large ranges of relevant parameter values. Our results suggest that in melanoma, the cellular arm of the immune system cannot reverse tumor immunotolerance naturally, and that immunotherapy may be the only way to overturn tumor dominance. We have shown that given a toxicity threshold for IFNγ, the maximal allowable IL-12 concentration to yield a Th1-polarized state can be estimated. Moreover, our analysis pinpoints the IL-10 secretion rate as a significant factor influencing the Th1:Th2 balance, suggesting its use as a personal immunomarker for prognosis.

<a id='7174bd96-c9ff-43cf-919c-c52953926b57'></a>

1. **Introduction.** Tumors can successfully escape natural host immunity in a multiphase process, collectively termed cancer immune editing. Immunoediting involves a critical shift from immunosurveillance to immunotolerance to the tumor, causing anticancer immune pathways to be heavily inhibited. As part of this process, CD4+ T lymphocytes are driven to a suppressive state; instead of adopting a "Type-1" T helper 1 (Th1) phenotype that favors cellular immunity, these cells take on a "Type-2" T helper 2 (Th2) phenotype, which drives humoral responses while suppressing cytotoxic effector functions [1, 2, 3].

<a id='817d818a-87e0-43b2-a9e8-399dffe6dd27'></a>

This severe Th1/Th2 imbalance is particularly eminent in the case of melanoma,
a clinically aggressive cancer, resistant to chemotherapy and radiation therapy
[4, 1]. Immune profiles in the sera of melanoma patients display a clear Th2-
dominant cytokine pattern, consisting of marked reductions in the Th1 cytokines
interferon (IFN$\gamma$) and interleukin (IL)-2 [5, 6] together with elevated levels of the

<a id='f89d7695-09cd-446f-96d8-f58e3a581dab'></a>

2010 Mathematics Subject Classification. 92B05, 37N25.
Key words and phrases. Interleukin-12, interleukin-10, interferon-y, phase plane analysis, ODE,
cancer, immune system.
The authors are supported by the Chai Foundation

<a id='018576f0-95d5-451a-b85f-4e8073a20e7e'></a>

1017

<!-- PAGE BREAK -->

<a id='33ee828e-9723-4917-bd97-741cacd95643'></a>

1018

<a id='20f5f814-c805-48f8-96a6-902b6eec01da'></a>

YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI

<a id='121f0563-cd15-4b69-8f15-92e228891b07'></a>

Th2 cytokines IL-10 [7, 5, 8, 6] and IL-4 [7, 5]. In other melanoma patients, lym-phatic regions in proximity to the tumor site have been found immunologically sub-responsive, containing reduced immune effector populations [4, 9] and higher IL-10 levels [10, 11]. Likewise, CD4+ T cells derived from individuals with melanoma showed a Th2-type profile upon activation ex vivo, indicative of a restrained immune state [12, 13]. Thus, while some level of immune activation in melanoma-bearing pa-tients exists, it mostly takes the form of a Th2-mediated chronic inflammatory state [7]. To achieve optimal clinical benefit, successful immunotherapeutic interventions must therefore break tumor tolerance, and overcome the Th2-skewed immunity by restoring beneficial specific anticancer Th1 responses.

<a id='3b76eb7c-59a3-4752-8aef-6faf3e3d8b0f'></a>

IL-12 is a potent multifunctional cytokine and a key regulator of cellular immu-
nity [14, 15, 16, 17]. Discovered first in 1989, the protein, a derivative of activated
dendritic cells (DC), has been found to boost immune pathways that are effective
against intracellular pathogens and cancer cells. An essential component and driving
force of Th1-type immunity, IL-12 drives antigen-activated CD4+ T cells to develop
into Th1 cells, and promotes the expansion and killing functions of activated natural
killer (NK) cells and cytotoxic T lymphocytes (CTL), predominantly through an
IFNγ-dependent mechanism [14, 16]. Promising antitumor effects induced by IL-12
in several experimental mouse models of solid cancers have supported its clinical use
as a potential cancer immunotherapeutic agent [15, 16, 17]. However, in patients
with melanoma or other malignancies, the response rate to systemic IL-12 therapy
has been rather low (2-10%), treatment being often accompanied by substantial side
effects, i.e. hepatitis, fever, and cytokine storms [15, 16, 17]. The National Cancer
Institute (NCI) has recently ranked IL-12 as a high-potential anticancer factor, but
the cytokine has been poorly studied in the clinical setting, and its development as
an immune-based oncotherapy was discontinued [17, 18].

<a id='4165a953-5222-4bb0-aca8-d26669c33701'></a>

The mechanisms that limit the efficacy of IL-12 in melanoma remain elusive. Some immunosuppressive effects of the cytokine are also known, possibly complicating its use [16]. Moreover, pharmacokinetic (PK) profiles in cancer patients reveal that the IL-12-induced effects appear progressively inhibited during continuous treatment cycles, suggesting that there is a gradual decrease in responsiveness to the cytokine [15, 16, 17]. Finally, the significant toxicity of IL-12 is a major hindrance to its use [17, 18]. In view of these considerations, careful control of the IL-12 regimen, to prevent the Th2-bias and restore Th1-immunity in melanoma patients in a safe manner, could potentially improve therapeutic efficacy of this drug.

<a id='66732b4f-63c3-483d-a540-946cd9751da1'></a>

Improved strategies for IL-12 application can be based on biomathematical mod-
eling and analysis. Such methods allow integration of mechanistic models and
multiscale data to describe and predict dynamical processes, thus bypassing the
need for tedious and time-consuming experimentation [19]. In a number of cases,
theoretical modeling has provided insight into the underlying processes of immu-
nity to cancer and its dynamics (as reviewed in [20]). Past models have specif-
ically tackled immune-modulating treatments, such as cytokine immunotherapy
[21, 22, 23, 24, 25, 26] and cellular/antibody-based treatments [27, 28, 29, 30, 31, 32]
with some models validated retrospectively and prospectively by preclinical and
patient data [33, 26, 29]. The basic features of Th1/Th2 development, and the
intracellular pathways governing it, have been mathematically modeled in previous
studies [34, 35, 36, 37, 38, 39, 40, 41]. However, this switch factor of the immune
response has yet to be fully analyzed from the perspective of malignancy.

<!-- PAGE BREAK -->

<a id='1a3f49de-bf01-4c43-993a-e8af9d81bf41'></a>

MELANOMA IMMUNE BALANCE CONTROLLED BY IL-12

<a id='e23617ee-592d-477a-8417-ac087f0de304'></a>

1019

<a id='f0007620-e2d8-45d7-b635-c59fb3df7825'></a>

Here, we modeled the Th1/Th2 interplay characteristic of the immune state in melanoma patients. Our analysis aims to characterize the possible behavior of the system as controlled by the critical parameters. In particular, the potential influence of IL-12 therapy on the balance of Type-1 vs. Type-2 responses is analyzed and it is suggested that the pathological Th1/Th2 imbalance is dominated by the tumor, so that immunotherapy, preferably personalized, may be the only way to reverse to the healthy steady state of the immune system.

<a id='7bbed8c0-b9a5-4677-9bc2-8d8696120e00'></a>

2. Model construction.

2.1. The general form of the model. Our model describes the dynamic relationships between CD4+ T helper (Th) cells of the Th1-type with their associated cytokines and those of the Th2-type with their cytokines, that occur in the tumor draining lymph nodes (LN) of melanoma patients. Accordingly, we consider four dynamic variables: (i) the density of activated Th1 CD4+ cells ($T_1$), (ii) the density of activated Th2 CD4+ cells ($T_2$), (iii) the concentration of IL-10 ($I$) and (iv) the concentration of IFN$\gamma$ ($G$). In addition, we consider the effect of exogenous IL-12 ($L$), administered to the patients. Cells are measured in $cell/ml$. All the cytokines are measured in $ng/ml$. Our model (see Fig. 1 for schematic description) is based on the following assumptions:

1. The active Th cells are recruited at a rate that depends on the concentration of the respective cytokines. Activation and expansion of each CD4+ subpopulation are represented by a single term.
2. Activated Th cells have first-order elimination.
3. IL-10 reduces the activation rate of Th1 cells, while IFN$\gamma$ reduces the activation rate of Th2 cells.
4. IFN$\gamma$ is secreted by Th1 cells and IL-10 is secreted by Th2 cells.
5. In addition, NK and CTL produce IFN$\gamma$ and DC and tumor cells produce IL-10 at a constant rate.
6. Both cytokines have first-order elimination.
7. IL-10 inhibits IFN$\gamma$ secretion by Th1 cells, but not by NK cells and CTL.
8. IFN$\gamma$ inhibits IL-10 secretion by DC, but not by Th2 cells.
9. IL-12 increases IFN$\gamma$ secretion and recruitment of Th1 cells, and decreases Th2 cells recruitment.

The above assumptions lead to a system of ODEs of the following general form:

$T_1 = r_1 \cdot f_1(I) \cdot g_1(L) - \mu_1 \cdot T_1$,

$T_2 = r_2 \cdot f_2(G) \cdot g_2(L) - \mu_2 \cdot T_2$,

$\dot{G} = p_G \cdot g_G(L) + q_G \cdot T_1 \cdot h_G(L) \cdot f_G(I) - \mu_G \cdot G$,

$\dot{I} = p_I \cdot f_I(G) + q_I \cdot T_2 - \mu_I \cdot I$.

(1)

<a id='a8498eb0-915e-4e3e-a6dc-d022f8e240d9'></a>

In this general notation, $f_1$, $f_2$, $f_G$, $f_I$ and $g_2$ are decreasing functions and $g_1$, $g_G$ and $h_G$ are increasing functions. All the functions are defined for any positive argument, have value of 1 at zero, are positive and monotonic and tend to nonnegative asymptotic value at infinity. The constant parameters describe turnover rates: $r_1$ and $r_2$ are maximal recruitment rates for the Th1 and Th2 subpopulations, respectively; $μ_1$ and $μ_2$ are the elimination rates for the Th1 and Th2 subpopulations, respectively; $p_G$ is the production rate of IFN$\gamma$ by NK cells and CTL; $q_G$ is the production rate of IFN$\gamma$ per Th2 cell; $p_I$ is the production rate of IL-10 by DC; $q_I$

<!-- PAGE BREAK -->

<a id='fd3603ab-1601-45d1-90e0-41b6f510b636'></a>

1020 YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI<::flowchart: FIGURE 1. Scheme of our mathematical model for the Th1/Th2 immune state under IL-12 regulation. The model is composed of the two main CD4+ Th cell types that drive cellular immunity (Th1) and humoral immunity (Th2), and the main cytokines they secrete, IFNγ and IL-10, respectively. These cytokines are also derived from NK cells and CTL, as well as DC and tumor cells. The Th1 and Th2 arms reciprocate negative control on one another: IFNγ hinders the recruitment of Th2 cells and the release of IL-10 from DC, while IL-10 inhibits Th1 recruitment and its secretion of IFNγ. Introducing IL-12 into the system gives rise to a Type-1 response, by stimulating Th1 recruitment and release of IFNγ, and concomitantly inhibiting the development of Th2 cells. The diagram illustrates the interactions between various immune components. At the top, IL-12 (represented by small ovals) stimulates Th1 (a large grey circle) and IFNγ (a rectangle containing small ovals), and inhibits Th2 (another large grey circle). Th1 releases IFNγ, and Th2 releases IL-10 (a rectangle containing small ovals). IFNγ is also released by NK, CTL (a grey circle at the bottom left), and IL-10 is also released by DC, Tumor (a grey circle at the bottom right). IFNγ inhibits Th2 and the release of IL-10 from DC. IL-10 inhibits Th1 and the secretion of IFNγ. The legend defines the arrow types: Release is represented by a dotted line, Recruitment by a solid arrow, Inhibition by a blunt arrow, and Stimulation by a solid arrow.: flowchart::>

<a id='42fb42f8-0a4e-429f-ab80-1f0d8803f3bf'></a>

is the production rate of IL-10 per Th1 cell; $\mu_G$ and $\mu_I$ are the elimination rates of IFN$\gamma$ and IL-10, respectively. All the rate parameters are positive.

<a id='e84afd60-cd55-4e26-a360-f0a7a31f0279'></a>

## 2.2. Implementation of the general functions and parameter estimation.
All the general functions used in system (1) were implemented by hyperbolae, follow-ing inspection of the available experimental data (see below). Increasing functions have the form $F(x) = 1+a_{max} \cdot \frac{x}{x+b}$, so that $F(0) = 1$, $\lim_{x\to\infty} F(x) = 1+a_{max}$ and $F(b) = \frac{a_{max}+1}{2}$. Decreasing functions are of the form $F(x) = a_{min}+(1-a_{min})\cdot \frac{b}{x+b}$, so that $F(0) = 1$, $\lim_{x\to\infty} F(x) = a_{min}$ and $F(b) = \frac{a_{min}+1}{2}$. Specifically,

<a id='eb26915e-0c48-4946-88b5-fff009be4032'></a>

f1(I) = a1 + (1 - a1) • (b1 / (I + b1))

<!-- PAGE BREAK -->

<a id='e2a13945-87a3-4a64-9d42-d854adb08851'></a>

MELANOMA IMMUNE BALANCE CONTROLLED BY IL-12                                                                         1021

<a id='071b0276-6eb9-4ca2-9866-1f7ad7a1391a'></a>

g1(L) = 1 + c1 * L / (L + d1)

f2(G) = a2 + (1 - a2) * b2 / (G + b2)

g2(L) = c2 + (1 - c2) * d2 / (L + d2)

fG(I) = aG + (1 - aG) * bG / (I + bG)

gG(L) = 1 + cG * L / (L + dG)

hG(L) = 1 + eG * L / (L + fG)

fI(G) = aI + (1 - aI) * bI / (G + bI)

<a id='1f2cdfec-a69e-431c-b3d5-3e881f47da4b'></a>

We assumed that Th1 and Th2 cells have the same elimination rate ($μ_1 = μ_2 = μ_T$) and maximal recruitment rate ($r_1 = r_2 = r_T$). In addition, the half-effect concentration of IL-12 is the same, $d_1 = d_2$, for both populations. Following the estimation of the effect functions, we arrive at the following system of four ODEs:

<a id='399e6d38-49e8-4ccf-8fb1-75a9f217a2a8'></a>

$$\dot{T}_1 = r_T \cdot \left( \frac{b_1}{I+b_1} \right) \cdot \left( 1 + \frac{c_1 \cdot L}{L+d_1} \right) - \mu_T \cdot T_1,$$$$\dot{T}_2 = r_T \cdot \left( \frac{b_2}{G+b_2} \right) \cdot \left( c_2 + \frac{(1-c_2) \cdot d_1}{L+d_1} \right) - \mu_T \cdot T_2,$$$$\dot{G} = p_G \cdot \left( 1 + \frac{c_G \cdot L}{L+d_G} \right) + q_G \cdot T_1 \cdot \left( 1 + \frac{e_G \cdot L}{L+f_G} \right) \cdot \left( a_G + \frac{(1-a_G) \cdot b_G}{I+b_G} \right) - \mu_G \cdot G, \quad (2)$$$$\dot{I} = p_I \cdot \left( a_I + \frac{(1-a_I) \cdot b_I}{G+b_I} \right) + q_I \cdot T_2 - \mu_I \cdot I.$$

<a id='fc2351e3-8c4d-4066-865b-7d887c02dd09'></a>

The values and ranges for the parameters (Table 1) were estimated using pub-lished experimental data. These values were either taken directly from experimental measurements, or obtained by fitting the relevant functions to the reported data. We determined the representative ("average") values for all the parameters, and when possible, also derived their biologically plausible ranges.

<a id='44f968d9-4b9f-465b-903a-9fd7240cfbe7'></a>

3. Model analysis.

<a id='86345da0-a8db-4810-8b61-d3a6960a6ae2'></a>

3.1. **The cytokine subsystem.** Careful inspection of the evaluated parameters (Table 1) reveals that system (2) can be separated into two parts, with respect to the time scale. Cell dynamics (the first two equations) evolve on a much slower scale than cytokine dynamics (the last two equations), the difference in the elimination rates being 2 orders of magnitude. This allows an approximation for this system, assuming that on the time scale of the cytokine subsystem, the cell concentrations T₁ and T₂ do not change, and on the scale of cell dynamics, the cytokine concentrations G and I are at quasi-steady state, determined by the parameters and the current values of T₁ and T₂. In this subsection, we investigate the dynamics of the cytokine

<!-- PAGE BREAK -->

<a id='24fb799e-6ed9-4462-b70c-52df0bd323b5'></a>

1022

<a id='ff161937-d270-4d40-af06-dca7bfddb1f9'></a>

YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI

<a id='10e97584-142b-48a3-887d-da84d6699674'></a>

<table id="5-1">
<tr><td id="5-2">Parameter</td><td id="5-3">Units</td><td id="5-4">Average value</td><td id="5-5">Range</td></tr>
<tr><td id="5-6">μT</td><td id="5-7">h⁻¹</td><td id="5-8">10⁻³</td><td id="5-9">5·10⁻⁴–5·10⁻³</td></tr>
<tr><td id="5-a">rT</td><td id="5-b">cell·ml⁻¹·h⁻¹</td><td id="5-c">10³</td><td id="5-d">10²–10⁴</td></tr>
<tr><td id="5-e">a1</td><td id="5-f">—</td><td id="5-g">0</td><td id="5-h">—</td></tr>
<tr><td id="5-i">b1</td><td id="5-j">ng·ml⁻¹</td><td id="5-k">0.35</td><td id="5-l">0.07–0.8</td></tr>
<tr><td id="5-m">a_2</td><td id="5-n"></td><td id="5-o">0</td><td id="5-p"></td></tr>
<tr><td id="5-q">b_2</td><td id="5-r">ng \cdot ml^{-1}</td><td id="5-s">0.18</td><td id="5-t">0.03 - 0.2</td></tr>
<tr><td id="5-u">\mu_G</td><td id="5-v">h^{-1}</td><td id="5-w">0.6</td><td id="5-x">0.45 - 1</td></tr>
<tr><td id="5-y">q_G</td><td id="5-z">ng \cdot cell^{-1} \cdot h^{-1}</td><td id="5-A">10^{-7}</td><td id="5-B">5 \cdot 10^{-8} - 5 \cdot 10^{-7}</td></tr>
<tr><td id="5-C">p_G</td><td id="5-D">ng \cdot ml^{-1} \cdot h^{-1}</td><td id="5-E">1.6 \cdot 10^{-2}</td><td id="5-F">5 \cdot 10^{-4} - 1.5</td></tr>
<tr><td id="5-G">aG</td><td id="5-H">—</td><td id="5-I">0.59</td><td id="5-J">0.5 – 0.67</td></tr>
<tr><td id="5-K">bG</td><td id="5-L">ng·ml⁻¹</td><td id="5-M">0.13</td><td id="5-N">0.06 – 0.2</td></tr>
<tr><td id="5-O">μI</td><td id="5-P">h⁻¹</td><td id="5-Q">0.36</td><td id="5-R">0.27 – 0.6</td></tr>
<tr><td id="5-S">qI</td><td id="5-T">ng·cell⁻¹·h⁻¹</td><td id="5-U">10⁻⁷</td><td id="5-V">4·10⁻⁹ – 5·10⁻⁶</td></tr>
<tr><td id="5-W">pI</td><td id="5-X">ng·ml⁻¹·h⁻¹</td><td id="5-Y">0.5</td><td id="5-Z">2·10⁻⁴ – 10</td></tr>
<tr><td id="5-10">aI</td><td id="5-11">—</td><td id="5-12">0.12</td><td id="5-13">—</td></tr>
<tr><td id="5-14">bI</td><td id="5-15">ng·ml-1</td><td id="5-16">0.025</td><td id="5-17">—</td></tr>
<tr><td id="5-18">c1</td><td id="5-19">—</td><td id="5-1a">30</td><td id="5-1b">7–60</td></tr>
<tr><td id="5-1c">d1,d2</td><td id="5-1d">ng·ml-1</td><td id="5-1e">0.8</td><td id="5-1f">0.1–1.5</td></tr>
<tr><td id="5-1g">c2</td><td id="5-1h">—</td><td id="5-1i">0.1</td><td id="5-1j">—</td></tr>
<tr><td id="5-1k">c G</td><td id="5-1l">—</td><td id="5-1m">12</td><td id="5-1n">1 – 20</td></tr>
<tr><td id="5-1o">d G</td><td id="5-1p">ng · ml -1</td><td id="5-1q">0.05</td><td id="5-1r">0.02 – 0.1</td></tr>
<tr><td id="5-1s">e G</td><td id="5-1t">—</td><td id="5-1u">5.4</td><td id="5-1v">—</td></tr>
<tr><td id="5-1w">f G</td><td id="5-1x">ng · ml -1</td><td id="5-1y">0.22</td><td id="5-1z">—</td></tr>
</table>
TABLE 1. Values and ranges of model parameters, used for the
analysis. The last eight parameters describe the effects of IL-12.

<a id='e05a6fe6-9926-4849-9732-c42688bc06f3'></a>

subsystem, assuming L = 0 and T₁ and T₂ have constant values. Under these assumptions this subsystem becomes

<a id='81ed7858-7a5d-47c1-9b23-4b8f0fd65701'></a>

G_dot = p_G + q_G * T_1 * (a_G + (1 - a_G) * b_G / (I + b_G)) - mu_G * G, (3)
I_dot = p_I * (a_I + (1 - a_I) * b_I / (G + b_I)) + q_I * T_2 - mu_I * I.

<a id='0d4b8eeb-3d76-46d9-9ad0-91fd442f01b3'></a>

For given values of $T_1$ and $T_2$, the set

<a id='6d523346-9320-4840-8bec-2e82de90701f'></a>

{ (G, I) | 0 ≤ G ≤ (pG + qG · T1) / μG , 0 ≤ I ≤ (pI + qI · T2) / μI }

<a id='4c2ed3e5-2c6d-4a37-ba9d-96012d7c8247'></a>

is clearly an invariant rectangle, so that, if initial values are in this set, then for all
t, the point (G(t), I(t)) will remain there. We focus on the behavior of the system
in this biologically relevant region. A steady state for this subsystem is determined
by the system of two nullclines:

<a id='83b086fb-a583-47ee-b3c8-ae2728652fe5'></a>

G = \frac{p_G}{\mu_G} + \frac{q_G \cdot T_1}{\mu_G} \cdot \left(a_G + \frac{(1 - a_G) \cdot b_G}{I + b_G}\right)

I = \frac{p_I}{\mu_I} \cdot \left(a_I + \frac{(1 - a_I) \cdot b_I}{G + b_I}\right) + \frac{q_I \cdot T_2}{\mu_I} (4)

<!-- PAGE BREAK -->

<a id='5b1c411c-1429-40aa-b64d-f2c8a0fd20e7'></a>

MELANOMA IMMUNE BALANCE CONTROLLED BY IL-12

<a id='dd9fc709-93fe-4650-8604-b848765d9f77'></a>

1023

<a id='2d71d786-946e-4b39-8b1e-e5719f80894e'></a>

It is easily seen that these nullclines define two hyperbolae in the $(G, I)$-plane, which have exactly one intersection point. In Fig. 2A we plot the nullclines for different values of $T_1$ and $T_2$. The intersections give the quasi-steady state points for the relevant cell concentrations.

<a id='1c0ebdb5-c2c8-4beb-ae52-061d645f362c'></a>

<::chart: FIGURE 2. Phase portrait of the cytokine subsystem. The figure contains two plots, A and B. Plot A displays solutions for the first and the second equations of system (3) for different values of T₁ and T₂ in the range (0, 2·10⁶). The x-axis is 'IL-10 concentration (ng·ml⁻¹)' and the y-axis is 'IFNγ concentration (ng·ml⁻¹)'. Multiple solid and dotted curves are shown. Plot B presents a phase portrait for T₁ = 5·10⁵, T₂ = 10⁶. The x-axis is 'IL-10 concentration (ng·ml⁻¹)' and the y-axis is 'IFNγ concentration (ng·ml⁻¹)'. Solid lines indicate the nullclines, and their intersection represents the unique steady state. Points mark the trajectories of the system for five random initial values, converging towards the steady state. The plot also shows a vector field.::>

<a id='3c0a4400-4d68-455d-b721-066728bce685'></a>

Defining ($G^*$, $I^*$) to be the unique steady state of system (3), we can write the
Jacobi matrix:

$J_{G,I} = \begin{pmatrix} -\mu_G & a_{21} \\ a_{12} & -\mu_I \end{pmatrix}$, (5)

<a id='4a3a73c6-923d-4c2b-9cc0-1e1d04bf6009'></a>

where $a_{21} = -\frac{p_I(1-a_I)b_I}{(G^*+b_I)^2}$, $a_{1,2} = -\frac{q_GT_1(1-a_G)b_G}{(I^*+b_G)^2}$. Substituting the steady-state equations (4), we can write $a_{12}a_{21} = \frac{(\mu_I I^*-q_IT_2-p_Ia_I)(\mu_G G^*-q_GT_1a_G-p_G)}{(I^*+b_G)(G^*+b_I)} < \mu_I\mu_G$.
Therefore, the characteristic polynomial of $J_{G,I}$, which has the form $P_{G,I}(\lambda) = (\lambda + \mu_G)(\lambda + \mu_I) - a_{12}a_{21}$, has both roots with a negative real part, i.e. the eigenvalues of $J_{G,I}$ have a negative real part and the unique steady state $(G^*, I^*)$ is locally asymptotically stable. Phase portrait and simulation results shown in Fig. 2 demonstrate that the steady state is globally asymptotically stable, at least in the invariant rectangle. Indeed, the global stability of the steady state is demonstrated by a straightforward application of Benedixson negative criterion: if we denote the two r.h.s. functions of system (3) by $F_1$ and $F_2$, then $\frac{\partial F_1}{\partial G} + \frac{\partial F_2}{\partial I} = -\mu_G - \mu_I < 0$.

<a id='74d4d9fd-e1e5-4e71-9280-914ac4febe8d'></a>

3.2. **The full system with no treatment.** In this subsection we focus on system (2), with _L_ = 0, i.e. without exogenous IL-12. Under this assumption, the system

<!-- PAGE BREAK -->

<a id='e8341510-eb97-4baa-b049-5c5013e6539b'></a>

1024 YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI

<a id='59aa6064-777f-44f5-8c78-f90ec55b259e'></a>

becomes:

$T_1 = r_T \cdot \left(\frac{b_1}{I + b_1}\right) - \mu_T \cdot T_1,$

$T_2 = r_T \cdot \left(\frac{b_2}{G + b_2}\right) - \mu_T \cdot T_2,$

$\dot{G} = p_G + q_G \cdot T_1 \cdot \left(a_G + \frac{(1 - a_G) \cdot b_G}{I + b_G}\right) - \mu_G \cdot G,$

$\dot{I} = p_I \cdot \left(a_I + \frac{(1 - a_I) \cdot b_I}{G + b_I}\right) + q_I \cdot T_2 - \mu_I \cdot I.$

(6)

<a id='a972fd1b-ad73-4b3b-a335-05879ca1b266'></a>

It is easy to see that the range R, defined by $0 \leq T_1 \leq \frac{r_T}{\mu_T}$, $0 \leq T_2 \leq \frac{r_T}{\mu_T}$, $0 \leq G \leq \frac{p_G+q_G \cdot \frac{r_T}{\mu_T}}{\mu_G}$, $0 \leq I \leq \frac{p_I+q_I \cdot \frac{r_T}{\mu_T}}{\mu_I}$, is invariant for system (6). Similarly to the previous section, here we focus on this biologically relevant domain.

<a id='4294792c-0e24-4f72-b6a2-cca00d1b1fd8'></a>

In order to determine the steady states, the following system of equations has to be solved:

$T_1 = \frac{r_T b_1}{\mu_T(I + b_1)}$

$T_2 = \frac{r_T b_2}{\mu_T(G + b_2)}$

$G = \frac{p_G}{\mu_G} + \frac{q_G \cdot T_1}{\mu_G} \cdot \left(a_G + \frac{(1 - a_G) \cdot b_G}{I + b_G}\right)$,

$I = \frac{p_I}{\mu_I} \cdot \left(a_I + \frac{(1 - a_I) \cdot b_I}{G + b_I}\right) + \frac{q_I \cdot T_2}{\mu_I}$. (7)

<a id='cdc9b8a0-71a6-4905-9768-9b0895dc7b96'></a>

Substitution of the first two equations of system (7) into the last two equations gives:

<a id='f1d3b9ab-40b3-4dcb-b57d-462fd93c4978'></a>

G = \frac{p_G}{\mu_G} + \frac{q_G \cdot r_T b_1}{\mu_G \mu_T (I + b_1)} \cdot \left(a_G + \frac{(1 - a_G) \cdot b_G}{I + b_G}\right)
I = \frac{p_I}{\mu_I} \cdot \left(a_I + \frac{(1 - a_I) \cdot b_I}{G + b_I}\right) + \frac{q_I \cdot r_T b_2}{\mu_I \mu_T (G + b_2)} \quad (8)

<a id='764550e9-c6f8-40b0-a356-822507c0d875'></a>

In the first of these two equations, $G$ monotonically decreases from $\frac{p_G}{\mu_G} + \frac{q_G r_T}{\mu_G \mu_T}$ to $\frac{p_G}{\mu_G}$, when $I$ grows from 0 to infinity. Similarly, in the second equation $I$ monotonically decreases from $\frac{p_I}{\mu_I} + \frac{q_I r_T}{\mu_I \mu_T}$ to $\frac{p_I a_I}{\mu_I}$, when $G$ grows from 0 to infinity. It is also easy to see that for $G > 0, I > 0$, the r.h.s. in both equations has a positive second derivative. Therefore, this system admits a unique solution; that is, there exists a unique steady state for system (6), $(T_1^*, T_2^*, G^*, I^*) \in R$. We numerically computed this steady state, as shown in Fig. 3, for a range of parameter values. In order to estimate its stability, we considered the Jacobi matrix

<a id='f2f2466b-907f-4013-99d9-702b3b32c6a2'></a>

$$J = \begin{pmatrix}
-\mu_T & 0 & q_G \left(a_G + \frac{(1-a_G)b_G}{I^*+b_G}\right) & 0 \\
0 & -\mu_T & 0 & q_I \\
0 & -\frac{r_T b_2}{(G^*+b_2)^2} & -\mu_G & -\frac{p_I(1-a_I)b_I}{(G^*+b_I)^2} \\
-\frac{r_T b_I}{(I^*+b_I)^2} & 0 & -\frac{q_G T_I^*(1-a_G)b_G}{(I^*+b_G)^2} & -\mu_I
\end{pmatrix} . (9)$$

<a id='a5076c98-c0f8-406d-b2da-878c7097302b'></a>

This matrix was computed for 100 different parameter sets randomly sampled within
the defined ranges. In all these computations, all the eigenvalues of J had a negative
real part. We simulated the model starting from randomly chosen initial points in

<!-- PAGE BREAK -->

<a id='88f76b1d-1445-4d8a-b226-714503f9215c'></a>

MELANOMA IMMUNE BALANCE CONTROLLED BY IL-12

<a id='e055559c-2c09-4f33-a770-2547488f4134'></a>

1025

<a id='2421cfb4-318c-4f76-aaa1-04b57b4970ef'></a>

the invariant domain $R$, and always observed conversion of the system to the unique steady state. This indicates that in the absence of therapy the unique steady state is globally attractive.

<a id='ec911037-3fb2-4e6d-bf6d-01070ad9b168'></a>

<::chart: Two scatter plots, labeled A and B, side-by-side. Both plots share a common y-axis label: "Th cells (cell \u00b7 ml\u207b\u00b9)". Each plot displays two data series: one represented by open circles and the other by points (dots).

**Plot A:**
- Y-axis scale: 0 to 9 x 10\u2075
- X-axis label: "IL-10 production per Th2 cell (ng \u00b7 ml\u207b\u00b9) x 10\u207b\u2076"
- X-axis scale: 0 to 6
- Data series (open circles): Decreases from approximately 1.8 x 10\u2075 to near 0 as the x-value increases.
- Data series (points): Increases from approximately 8 x 10\u2075 to 8.5 x 10\u2075 as the x-value increases.

**Plot B:**
- Y-axis scale: 2 x 10\u2075 to 8 x 10\u2075
- X-axis label: "IL-10 production by other cells (ng \u00b7 ml\u207b\u00b9)"
- X-axis scale: 0 to 1
- Data series (open circles): Decreases from approximately 7 x 10\u2075 to near 0 as the x-value increases.
- Data series (points): Increases from approximately 6.5 x 10\u2075 to 7.5 x 10\u2075 as the x-value increases.

**Caption:**
FIGURE 3. Steady-state values of Th1 (open circles) and Th2 (points) cell populations, as a function of the rate of IL-10 secretion by Th2 cells (A) and by DC and tumor cells (B).::>

<a id='cca0987b-65df-499f-992c-518daf70ffd0'></a>

3.3. **Effect of IL-12.** As shown in the previous subsections, our model describes the basic state of immune imbalance in melanoma patients, with the immune system skewed towards Th2, as reflected by higher numbers of Th2 cells and lower numbers of Th1 cells. To study the feasibility of immunotherapy by IL-12, we used our model to examine how different levels of the cytokine can affect the cellular immune balance discussed here. We computed the steady-state densities of activated T helper cells as a function of the IL-12 concentration (i.e. using L as a controlled parameter). For any given value of L, system (2) has the same general properties as determined in the previous subsection for the case L = 0. Increase in L causes a change to domain R (increase of maximal values of T₁ and G and decrease in those of T₂ and I) and also changes the steady-state values. The dependence of the steady state of the system on L is demonstrated in Fig. 4 for the average parameter values. Using this computation one can estimate the effect of different IL-12 concentrations on the Th1/Th2 balance.

<a id='570accec-6e60-41ae-a5b9-c6a621c4db32'></a>

3.4. **Limitation on IL-12 due to toxicity.** The major adverse effects observed while treating melanoma patients with IL-12 are likely a result of an excessive Th1 response. In a phase I study in renal cell carcinoma patients, IL-12 therapy was well tolerated, whereas in a subsequent phase II study in similar settings (yet a slightly different regimen), severe and life-threatening toxicities were observed in most patients [43]. Comparison between the two clinical trials shows that the toxicity-associated mortality due to IL-12 is accompanied by high levels of IFNγ. This toxicity determines the maximum allowable concentration of IL-12, such that IFNγ does not cross a given toxicity threshold. For a given set of model parameters, this allows to determine the value L_max of L that maximizes the Th1 cell density in the LN, T_1, while having the IFNγ concentration below the toxicity threshold G_tox. Fig. 4 demonstrates the potential application of such an approach: along

<!-- PAGE BREAK -->

<a id='4e7d1347-68b9-4d43-adc0-75282fe9b1fd'></a>

1026
YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI

<::chart: A 2D line plot showing the effect of IL-12 concentration on steady-state cell populations and IFNγ concentration. The x-axis is 'IL12 concentration (ng · ml⁻¹)', ranging from 0 to 1. The left y-axis is 'Th cells (cell · ml⁻¹)' scaled by 'x 10⁶', ranging from 0 to 10. The right y-axis is 'IFNγ (ng · ml⁻¹)', ranging from 0 to 1.5. Three data series are plotted: Th1 cells (open circles) show an increasing trend with IL-12 concentration, Th2 cells (points) show a very low and slightly decreasing trend, and IFNγ concentration (crosses), plotted against the right y-axis, also shows an increasing trend with IL-12 concentration. A horizontal broken line is drawn at 6 x 10⁶ Th cells (left axis) and 1 ng · ml⁻¹ IFNγ (right axis). A vertical broken line is drawn at approximately 0.5 ng · ml⁻¹ IL-12 concentration, indicating the intersection point with the horizontal line and the data series. The caption reads: 'FIGURE 4. IL-12 effect on steady-state cell populations. Th1 (open circles) and Th2 (points) cell counts are shown for various IL-12 concentrations; see left axis for units. Corresponding IFNγ concentrations are shown by crosses; see right axis for units. The horizontal broken line shows the toxicity threshold of IFNγ (Gtox) and the vertical line shows the corresponding maximal allowable IL-12 concentration and Th1 cell count.':>


<a id='5a62ad7f-13cd-4da9-985a-3c18d44ed5dd'></a>

with the values of Th cell levels, we computed the corresponding values of IFNγ. The limitation on IFNγ, $G_{tox} = 1 \frac{ng}{ml}$, imposes a corresponding limitation on the allowable IL-12 concentration. In the example presented here, the maximal tolerable concentration of IL-12 is $0.52 ng/ml$, and the corresponding level of the Th1 cells is ca. $7.8 \cdot 10^6 cell/ml$, while the Th2 cells are reduced to $9.9 \cdot 10^4 cell/ml$.

<a id='b9d15aad-8dd5-4530-b0c6-9d75c1079716'></a>

4. Discussion. It has long been recognized that melanoma is an immunogenic tumor, and the immune response is an important factor in the control of this disease [1, 42]. Melanoma is perhaps one of the cancer indications that respond most significantly to immunotherapy, and several immune-based agents and cellular vaccines are being developed specifically for this indication [1]. Nonetheless, cytokine therapy for melanoma still suffers from major drawbacks. Food and Drug Administration (FDA)-approved immune-based treatments for this indication (IFNα and IL-2) are challenging to administer, due to harsh toxicity profiles, coupled with the limited efficacy of these drugs at the higher doses [1, 4]. IL-12 is no exception; despite the well-accepted immune potency of this cytokine, its development was halted, and optimal strategies for its application are still lacking [17, 18]. Our current work can thus be viewed as a first step towards rationalizing IL-12 therapy.

<a id='a57f0fa1-1912-4500-b4e3-420c21343d7d'></a>

The mathematical model presented here describes the pathological immune sys-
tem and its basic interactions. The work is new in tackling the Th1/Th2 imbalance
in cancerous conditions, and particularly in melanoma; the data used for calibrating

<!-- PAGE BREAK -->

<a id='3f8eeb91-4bac-45bb-bf23-4261bdd3ce57'></a>

MELANOMA IMMUNE BALANCE CONTROLLED BY IL-12

<a id='23fadd90-56c3-43ef-8f0e-fb7dc6efb42c'></a>

1027

<a id='f2b61947-60f7-4ce4-83aa-5819df30465d'></a>

the model parameters were partly obtained from clinical melanoma studies, allow-ing to adjust the system to accurately portray the Th2-bias in the tumor-dominant scenario.

<a id='1e15068c-ecb5-4e9e-aa8d-9ad41c2bfe6a'></a>

By analyzing the phase plane of the system we have examined whether or not the pathological immune phenotype can be in a stable steady state, conferring competitive advantage to the tumor. Further investigation yields insights on the prospects of reversing the pathological Th1/Th2 imbalance towards a more favorable position. Our analysis suggests that the described system has a unique steady state, which appears to be globally attracting. This is supported by the findings that (i) the fast subsystem of the cytokines globally converges to the stable steady state; (ii) the unique steady state of the full system is locally stable for different samples of parameter values; (iii) all the simulations with randomly sampled parameter values and initial values converge directly to this steady state. These results imply that, on its own, the cellular arm of the immune system, with its major cytokine, IFNγ, cannot reverse tumor immunotolerance, giving a stable upper hand to the disease. Immunotherapy by a Th1-stimulating factor may be the only means to induce the necessary shift.

<a id='f87f93d0-4317-4835-a6ed-40627867155e'></a>

Is immunotherapy by IL-12 sufficient for achieving the goal of subverting the Th1/Th2 balance towards a Th1-dominant state? Our analysis shows that IL-12 can be applied at levels that allow Th1 polarization concomitant with a Th2 reduction, while keeping IFN$\gamma$ concentrations in check. We have shown that an IL-12 level of 0.52 ng/ml suffices for yielding a Th1:Th2 ratio of ca. 80, with an IFN$\gamma$ level still below a feasible toxicity threshold. However, the phase plane analysis also shows that if therapy by IL-12 is relieved, the Th1:Th2 ratio will monotonically reverse to its previous Th2-dominated imbalance. The reason for this may be that the model currently does not account for immune mechanisms that could stabilize the system at Th1-polarized states.

<a id='8a43eb3b-2156-47c5-b4f1-0890890b919f'></a>

We have shown that production of IL-10, the major driving force of Th2 polar-
ization, is a highly influential parameter in this system. As shown in section 3.2, the
IL-10 secretion rate can significantly alter the balance between the numbers of Th1
and Th2 cells. Since IL-10 levels likely vary between patients and in different stages
of the disease, this result underscores the possibility to use the IL-10 secretion rate
as a personal indicator of prognosis, as well as the need to take into account the
IL-10 level when determining personalized immunotherapeutic schedules for cancer
patients [31].

<a id='70cd4825-4569-4b97-b4ed-ad2f08498ac7'></a>

It still remains to be investigated whether or not the Th1 advantage that we
have pinpointed suffices for mounting an efficacious immune response that could
yield a clinically observable reduction in the tumor, or at least allow for stabilizing
the disease. For this purpose, the simplified mathematical system herein is now
being further elaborated to consider the complexity of the cellular response to the
growing tumor. An appropriate mathematical description of the tumor dynamics,
together with other critical components of the anticancer immune response, such
as dendritic cells (the source of endogenous IL-12) and cytotoxic tumor killing cells
(CD8+ T lymphocytes and NK cells) [3], would be required. Such future extensions
of this model will enable more in-depth analysis of the interplay between the im-
mune response and tumor dynamics, and help assess whether the pinpointed IL-12
treatment is in fact effective. In addition, a PK model of IL-12 will be coupled with
our model to simulate realistic treatment scenaria for planning clinical IL-12 sched-
ules. Prospective mathematical endeavors may also aid in determining the benefit of

<!-- PAGE BREAK -->

<a id='8de87088-672b-4e14-9068-fec39650ba8c'></a>

1028 YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI

<a id='7a368af7-34a5-43ad-bbe0-e843b1dee343'></a>

alternative IL-12 administration methods under investigation, i.e. delivery via gene therapy, as a vaccine adjuvant, or in combinational with other immune-boosting cytokines [44, 17].

<a id='51ab7123-fc4f-48b5-a4e8-eb25c754e3d0'></a>

## REFERENCES

1. J. M. Kirkwood, A. A. Tarhini, M. C. Panelli, S. J. Moschos, H. M. Zarour, L. H. Butterfield and H. J. Gogas, Next generation of immunotherapy for melanoma, J. Clin. Oncol., **26** (2008), 3445-3455.
2. G. P. Dunn, A. T. Bruce, H. Ikeda, L. J. Old and R. D. Schreiber, Cancer immunoediting: From immunosurveillance to tumor escape, Nat. Immunol., **3** (2002), 991-998.
3. W. H. Fridman, F. Pages, C. Sautes-Fridman and J. Galon, The immune contexture in human tumours: impact on clinical outcome, Nat. Rev. Cancer, **12** (2012), 298-306.
4. A. J. Cochran, R. R. Huang, J. Lee, E. Itakura, S. P. L. Leong and R. Essner, Tumour-induced immune modulation of sentinel lymph nodes, Nat. Rev. Immunol., **6(9)** (2006), 659-670.
5. L. Lauerova, L. Dusek, M. Simickova, I. Kocak, M. Vagundova, J. Zaloudik and J. Kovarik, Malignant melanoma associates with Th1/Th2 imbalance that coincides with disease progression and immunotherapy response, Neoplasma, **49** (2002), 159-166.
6. R. Botella-Estrada, M. Escudero, J. E. O'Connor, E. Nagore, B. Fenollosa, O. Sanmartin, C. Requena and C. Guillen, Cytokine production by peripheral lymphocytes in melanoma, Eur. Cytokine Netw., **16** (2005), 47-55.
7. W. K. Nevala, C. M. Vachon, A. A. Leontovich, C. G. Scott, M. A. Thompson and S. N. Markovic, Evidence of systemic Th2-driven chronic inflammation in patients with metastatic melanoma, Clin. Cancer Res., **15** (2009), 1931-1939.
8. W. Dummer, J. C. Becker, A. Schwaaf, M. Leverkus, T. Moll and E. B. Brocker, Elevated serum levels of interleukin-10 in patients with metastatic malignant melanoma, Melanoma Res., **5** (1995), 67-68.
9. A. M. Lana, D. R. Wen and A. J.Cochran, The morphology, immunophenotype and distribution of paracortical dendritic leucocytes in lymph nodes regional to cutaneous melanoma, Melanoma Res., **11** (2001), 401-410.
10. R. Botella-Estrada, F. Dasi, D. Ramos, E. Nagore, M. J. Herrero, J. Gimenez, C. Fuster, O. Sanmartin, C. Guillen and S. Alino, Cytokine expression and dendritic cell density in melanoma sentinel nodes, Melanoma Res., **15** (2005), 99-106.
11. J. H. Lee, H. Torisu-Itakara, A. J. Cochran, A. Kadison, Y. Huynh, D. L. Morton and R. Essner, Quantitative analysis of melanoma-induced cytokine-mediated immunosuppression in melanoma sentinel nodes, Clin. Cancer Res., **11** (2005), 107-112.
12. T. Tatsumi, L. S. Kierstead, E. Ranieri, L. Gesualdo, F. P. Schena, J. H. Finke, R. M. Bukowski, J. Mueller-Berghaus, J. M. Kirkwood, W. W. Kwok and W. J. Storkus, Disease-associated bias in T helper type 1 (Th1)/Th2 CD4+ T cell responses against MAGE-6 in HLA-DRB10401+ patients with renal cell carcinoma or melanoma, J. Experimental Medicine, **196** (2002), 619-628.
13. D. D. Kharkevitch, D. Seito, G. C. Balch, T. Maeda, C. M. Balch and K. Itoh, Characterization of autologous tumor-specific T-helper 2 cells in tumor-infiltrating lymphocytes from a patient with metastatic melanoma, Int. J. Cancer, **58** (1994), 317-323.
14. G. Trinchieri, Interleukin-12: A proinflammatory cytokine with immunoregulatory functions that bridge innate resistance and antigen-specific adaptive immunity, Annu. Rev. Immunol., **13** (1995), 251-276.
15. M. P. Colombo and G. Trinchieri, Interleukin-12 in anti-tumor immunity and immunotherapy, Cytokine Growth Factor Rev., **13** (2002), 155-168.
16. G. Trinchieri, Interleukin-12 and the regulation of innate resistance and adaptive immunity, Nat. Rev. Immunol., **3** (2003), 133-146.
17. M. Del Vecchio, E. Bajetta, S. Canova, M. T. Lotze, A. Wesa, G. Parmiani and A. Anichini, Interleukin-12: biological properties and clinical application, Clin. Cancer Res., **13** (2007), 4677-4685.
18. M. A. Cheever, Twelve immunotherapy drugs that could cure cancers, Immunol. Rev., **222** (2008), 357-368.
19. Z. Agur, From the evolution of toxin resistance to virtual clinical trials: The role of mathematical models in oncology, Future Oncol., **6** (2010), 917-927.

<!-- PAGE BREAK -->

<a id='50942c49-8dff-4f37-aebe-4acd4573f406'></a>

MELANOMA IMMUNE BALANCE CONTROLLED BY IL-12 1029

[20] R. Eftimie, J. L. Bramson and D. J. Earn, *Interactions between the immune system and cancer: A brief review of non-spatial mathematical models*, Bull. Math. Biol., **73** (2011), 2-32.
[21] D. Kirschner and J. C. Panetta, *Modeling immunotherapy of the tumor-immune interaction*, J. Math. Biol., **37** (1998), 235-252.
[22] F. Nani and H. I. Freedman, *A mathematical model of cancer treatment by immunotherapy*, Math. Biosci., **163** (2000), 159-199.
[23] L. G. de Pillis, W. Gu and A. E. Radunskaya, *Mixed immunotherapy and chemotherapy of tumors: Modeling, applications and biological interpretations*, J. Theor. Biol., **238** (2006), 841-862.
[24] A. Cappuccio, M. Elishmereni and Z. Agur, *Cancer immunotherapy by interleukin-21: Potential treatment strategies evaluated in a mathematical model*, Cancer Res, **66** (2006), 7293-7300.
[25] A. Cappuccio, M. Elishmereni and Z. Agur, *Optimization of interleukin-21 immunotherapeutic strategies*, J. Theor. Biol., **248** (2007), 259-266.
[26] M. Elishmereni, Y. Kheifetz, H. Sondergaard, R. V. Overgaard and Z. Agur, *An integrated disease/pharmacokinetic/pharmacodynamic model suggests improved interleukin-21 regimens validated prospectively for mouse solid cancers*, PLoS Comput. Biol., **7** (2011), e1002206.
[27] N. Kronik, Y. Kogan, V. Vainstein and Z. Agur, *Improving alloreactive CTL immunotherapy for malignant gliomas using a simulation model of their interactive dynamics*, Cancer Immunol. Immunother., **57** (2008), 425-439.
[28] N. Kronik, Y. Kogan, M. Elishmereni, K. Halevi-Tobias, S. Vuk-Pavlovic and Z. Agur, *Predicting outcomes of prostate cancer immunotherapy by personalized mathematical models*, PLoS One, **5** (2010), e15482.
[29] Y. Kogan, K. Halevi-Tobias, M. Elishmereni, S. Vuk-Pavlovic and Z. Agur, *Reconsidering the paradigm of cancer immunotherapy by computationally aided real-time personalization*, Cancer Res., **72** (2012), 2218-2227.
[30] E. Jager, V. H. van der Velden, J. G. te Marvelde, R. B. Walter, Z. Agur and V. Vainstein, *Targeted drug delivery by gemtuzumab ozogamicin: mechanism-based mathematical model for treatment strategy improvement and therapy individualization*, PLoS One, **6** (2011), e24265.
[31] Z. Agur and S. Vuk-Pavlovic, *Mathematical modeling in immunotherapy of cancer: Personalizing clinical trials*, Mol. Ther., **20** (2012), 1-2.
[32] F. Castiglione and B. Piccoli, *Cancer immunotherapy, mathematical modeling and optimal control*, J. Theor. Biol., **247** (2007), 723-732.
[33] L. G. de Pillis, A. E. Radunskaya and C. L. Wiseman *A validated mathematical model of cell-mediated immune response to tumor growth*, Cancer Res., **65** (2005), 7950-7958.
[34] M. A. Fishman and A. S. Perelson, *Th1/Th2 cross regulation*, J. Theor. Biol., **170** (1994), 25-56.
[35] M. A. Fishman and L. A. Segel, *Modeling immunotherapy for allergy*, Bull. Math. Biol., **58** (1996), 1099-1121.
[36] M. A. Fishman and A. S. Perelson, *Th1/Th2 differentiation and cross-regulation*, Bull. Math. Biol., **61** (1999), 403-436.
[37] A. Yates, C. Bergmann, J. L. Van Hemmen, J. Stark and R. Callard, *Cytokine-modulated regulation of helper T cell populations*, J. Theor. Biol., **206** (2000), 539-560.
[38] C. Bergmann, J. L. Van Hemmen and L. A.Segel, *Th1 or Th2: How an appropriate T helper response can be made*, Bull. Math. Biol., **63** (2001), 405-430.
[39] A. Yates, R. Callard and J. Stark, *Combining cytokine signalling with T-bet and GATA-3 regulation in Th1 and Th2 differentiation: a model for cellular decision-making*, J. Theor. Biol., **231** (2004), 181-196.
[40] R. E. Callard, *Decision-making by the immune response*, Immunol. Cell Biol., **85** (2007), 300-305.
[41] F. Gross, G. Metzner and U. Behn, *Mathematical modeling of allergy and specific immunotherapy: Th1-Th2-Treg interactions*, J. Theor. Biol., **269** (2011), 70-78.
[42] M. L. Disis, *Immunologic biomarkers as correlates of clinical response to cancer immunotherapy*, Cancer Immunol. Immunother., **60** (2011), 433-442.
[43] J. P. Leonard, M. L. Sherman, G. L. Fisher, L. J. Buchanan, G. Larsen, M. B. Atkins, J. A. Sosman, J. P. Dutcher, N. J. Vogelzang and J. L. Ryan, *Effects of single-dose interleukin-12 exposure on interleukin-12-associated toxicity and interferon-gamma production*, Blood, **90** (1997), 2541-2548.

<!-- PAGE BREAK -->

<a id='ffd9b9fc-78b8-4aa4-9d6c-bf9c36456ad0'></a>

1030                                YURI KOGAN, ZVIA AGUR AND MORAN ELISHMERENI

<a id='411c1ee8-4aab-4be2-8957-7479a09698f2'></a>

[44] J. M. Weiss, J. J. Subleski, J. M. Wigginton, R. H. Wiltrout, Immunotherapy of cancer by IL-12-based cytokine combinations, Expert Opin. Biol. Ther., 7 (2007), 1705-1721.

<a id='e7d62e2b-2a90-478a-b7a8-e3906964c883'></a>

Received May 2012; revised August 2012.

E-mail address: yuri@imbm.org
E-mail address: agur@imbm.org
E-mail address: moran@imbm.org
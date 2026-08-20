<a id='d22bc72b-4012-4136-9998-fc4c627cafa9'></a>

Hindawi
Computational and Mathematical Methods in Medicine
Volume 2019, Article ID 7576591, 16 pages
https://doi.org/10.1155/2019/7576591

<a id='a10b4f22-bece-4486-a164-4bd6d093bb32'></a>

_Research Article_

**Mathematical Analysis of a Mathematical Model of Chemovirotherapy: Effect of Drug Infusion Method**

<a id='4d3166d0-ecec-4ce4-bb88-3108c987a15d'></a>

**Joseph Malinzi** (iD)

*Department of Mathematics, University of Eswatini, Private Bag 4, Kwaluseni, Eswatini*
Correspondence should be addressed to Joseph Malinzi; josephmalinzi@aims.ac.za
Received 17 November 2018; Revised 14 January 2019; Accepted 28 January 2019; Published 11 March 2019
Guest Editor: Madjid Soltani

<a id='e4d47049-82ce-4ae1-b163-d1f0644574bd'></a>

Copyright  2019 Joseph Malinzi. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

<a id='29b7a349-6971-4e60-8b8f-e9c48e20ff2d'></a>

A mathematical model for the treatment of cancer using chemovirotherapy is developed with the aim of determining the efficacy of three drug infusion methods: constant, single bolus, and periodic treatments. The model is in the form of ODEs and is further extended into DDEs to account for delays as a result of the infection of tumor cells by the virus and chemotherapeutic drug responses. Analysis of the model is carried out for each of the three drug infusion methods. Analytic solutions are determined where possible and stability analysis of both steady state solutions for the ODEs and DDEs is presented. The results indicate that constant and periodic drug infusion methods are more efficient compared to a single bolus injection. Numerical simulations show that with a large virus burst size, irrespective of the drug infusion method, chemovirotherapy is highly effective compared to either treatments. The simulations further show that both delays increase the period within which a tumor can be cleared from body tissue.

<a id='4c96805e-2b15-455e-83f5-39dadd165f68'></a>

## 1. Introduction
Tumors possess mechanisms that suppress antitumor activity such as ligands that block natural killer cells and cytotoxic tumor infiltrating cell functions [1]. Greatly because of this, successful cancer treatment often requires a combination of treatment regimens.

<a id='eb226763-9be0-4dac-a2f3-e02a85032e80'></a>

Nearly all traditional monotherapies, including che-
motherapy, surgery, and radiation therapy are not a definite
cure for cancer and are highly toxic [2]. Chemotherapy for
example, which is the most commonly used regimen, in-
volves the use of medical drugs to lyse cancer cells. These
chemotherapeutic drugs circulate in the body and kill
rapidly multiplying cells nonselectively, which ultimately
results into the destruction of both healthy and cancerous
cells [2, 3]. Chemotherapy can thus be toxic to a patient with
adverse side effects and can also damage their immune
system [2].

<a id='57b08485-d289-43ba-9775-af498ecd297d'></a>

Presently, combination cancer treatment is a centerpiece
of cancer therapy [4]. The amalgamation of anticancer drugs
increases efficacy compared to single-drug treatments.
Further, anticancer drug combination provides therapeutic
benefits such as reducing tumor growth, arresting mitoti-
cally active cells, reducing the population of cancer stem

<a id='800d123a-52cf-4713-ab27-aede26363570'></a>

cells, and inducing apoptosis [4]. Despite the fact that combination therapy might as well be toxic if one of the agents used is chemotherapeutic, the toxicity is lesser because different pathways would be targeted [4]. Moreover with the use of combination therapy, the toxicity on normal cells can be prevented while concurrently producing cytotoxic effects on cancer cells [4, 5].

<a id='46b7a20a-51c4-44af-9ae8-cc4be1bde7cb'></a>

In the recent past, virotherapy, a less toxic treatment has been identified as a possible cancer remedy [6-11]. Virotherapy involves the use of oncolytic viruses that infect, multiply, and directly lyse cancer cells with less or no toxicity [9]. Their tumor specific properties allow for viral binding, entry, and replication [12]. Oncolytic viruses can greatly enhance the cytotoxic mechanisms of chemotherapeutic drugs [13]. Further, chemotherapeutic drugs lyse fast multiplying cells and, in general, virus infected tumor cells quickly replicate [14].

<a id='49347815-ecee-4017-9d75-fc2e62a505c8'></a>

Chemovirotherapy is a combination treatment strategy that involves the use of oncolytic viruses and chemotherapeutic drugs. Recent experimental and mathematical studies have shown that chemovirotherapy is a plausible cancer treatment and leads to enhanced therapeutic effects not achievable when either therapies are independently used [12, 13, 15-20]. Nguyen et al. [12] gave an account of the

<!-- PAGE BREAK -->

<a id='51007493-7463-45eb-adba-384ee93776fb'></a>

2

<a id='7a06b8bd-6a33-4d29-a376-9be2cd153448'></a>

Computational and Mathematical Methods in Medicine

<a id='f896f18a-9ddf-4fec-adfc-54f9a5785f72'></a>

mechanisms through which drugs can successfully be used in a combination with oncolytic viruses. They however note that the success of this combination depends on several factors including the type of oncolytic virus- (OV-) drug combination used, the timing, frequency, dosage, and cancer type targeted. To date, the best method of OV drug delivery is debatable [21, 22].

<a id='0a1f98f4-9ee0-4e16-a040-4df7aba814c0'></a>

The main goal of this study is to, thus, consider and compare the efficacy of three drug infusion methods, use mathematical analysis to predict the outcome of OV-drugs combination treatment and determine the effect of drug response and virus infection delays. To this end, we construct a mathematical model in the form of ODEs which we later extend to DDEs to include the virus infection and drug response delays. The model constructed combines elements from existing mathematical models [10, 11, 19, 20, 23–30]. Tian [10] presented a mathematical model that incorporates burst size for oncolytic virotherapy. His study showed that virotherapy is highly effective provided that viruses with large burst sizes are used. Malinzi et al. [19] constructed a spatiotemporal mathematical model to investigate the outcome of chemovirotherapy. Their study suggested that combining chemotherapeutic drugs with oncolytic viruses is more efficient than using either treatments alone. A similar study by Malinzi et al. [20] indicates that chemotherapy alone is capable of clearing tumor cells from body tissue if the drug efficacy is greater than the tumor growth rate. Nevertheless, the study contends that oncolytic viruses highly enhance chemotherapy in lysing tumor cells. The study further postulates that half the maximum tolerated doses of chemotherapy and virotherapy optimize chemovirotherapy, thus answering a very pertinent question in combination cancer therapy.

<a id='bb5d1314-ebcc-4cca-8cd0-cd700094697c'></a>

The article is organised as follows: Section 2 presents a comprehensive description of the both the ODE and DDE models and the underlying assumptions made in constructing them. In Section 3, the model without delay is analysed. First, without any form of treatment, then with either treatments (that is, with chemo only and virotherapy alone) and with both treatments. The delay model is then analysed in Section 4 and numerical experiments for both the ODE and DDE models are carried out in Section 5. Finally, before concluding in Section 7, a comparison of this study with related works is done is Section 6.

<a id='b876ca71-e311-49ef-a33c-f123dba5c97f'></a>

## 2. Model Description

2.1. Model without Delay. Time-dependent cell concentrations of uninfected tumor cells U (t), infected tumor cells I (t), a free virus population V (t), and a chemotherapeutic drug C(t) in an avascular tumor localization are considered. The uninfected tumor grows logistically at an intrinsic rate α per day, and the total tumor carrying capacity is K cells in a tumor nodule. The infected tumor cells die off at a rate δ per day. Virus multiplication in the tumor is represented by the function βU (t)V (t), where β is the virus replication rate measured per day per 10^6 cells or viruses. The response of the drug to the uninfected and infected

<a id='da8014b6-78e6-4361-8ba7-0556e627da38'></a>

tumor is, respectively, modelled by the functions
$\delta_0 U(t)C(t)$ and $\delta_1 I(t)C(t)$ where $\delta_0$ and $\delta_1$ are induced
lysis rates caused by the chemotherapeutic drug measured
per day per cell. Virus lifespan is taken to be $1/\gamma$ and its
production is considered to be $b\delta I$ where $b$ is the virus burst
size, measured in number of viruses per day per cell, and $\delta$
is the infected tumor cells' death rate measured per day.
Chemotherapeutic drug infusion into the body is modelled
with a function $g(t)$ and that the drug gets depleted from
body tissue at a rate $\lambda$ per day.

<a id='362b2c0e-5d8f-4721-85f9-d97a330203d5'></a>

Drug infusion into the body is simulated using (a)
a constant rate $g(t) = q$, (b) an exponential $g(t) =
q \exp(-at)$, and (c) a sinusoidal function $g(t) = q \sin^2 (at)$,
where $q$ is the rate of drug infusion. The constant $a$ de-
termines the exponential drug decay and period for the
sinusoidal infusion. Constant drug infusion may relate to
a situation where a patient is put on an intravenous injection
or a protracted venous infusion and the drug is constantly
pumped into the body [31, 32]. The exponential drug in-
fusion may relate a situation where a cancer patient is given
a single bolus and the drug exponentially decays in the body
tissue. This form of infusion is not common although it is
now used for some drugs, for example, a single dose of
carboplatin can be given to patients with testicular germ cell
tumors and breast cancer ([33, 34]). The third scenario is
possible when a cancer patient makes several visits to
a health facility and is given injections or anticancer drugs
periodically [35, 36].

<a id='6c8e485c-08f9-4a47-b7f2-f7da115eedbe'></a>

The assumptions above lead to the following system of nonlinear first-order differential equations (also similarly derived in [11, 19, 20]):

U̇(t) = αU(t)\left(1 - \frac{U(t) + I(t)}{K}\right) - βU(t)V(t) - δ₀U(t)C(t),

İ(t) = βU(t)V(t) - δ₁I(t) - δ₂I(t)C(t),

V̇(t) = bδI(t) - βU(t)V(t) - γV(t),

Ċ(t) = g(t) - λC(t),

<a id='4c2acb22-f127-4651-acc8-ac052c8db5f1'></a>

subject to initial concentrations

U(0) = U₀,
I(0) = I₀,
V(0) = V₀,
C(0) = C₀.

(2)

<a id='65ceb3ce-aea4-416f-87dd-f5fd3d01587a'></a>

2.2. Delay Model. The model is further extended to account for delays as a result of the infection of tumor cells by the virus and responses of the chemotherapeutic drug. In fact, the viruses need time to develop suitable responses when they meet the uninfected tumor cells (e.g., [37]). The drug does not instantaneously kill the cells (e.g., [38, 39]). By denoting the virus and chemotherapeutic response delays as τ₁ and τ₂, respectively, model (1)

<a id='e0dc2386-bdf5-4113-a489-5e63b91d92de'></a>

(1)

<!-- PAGE BREAK -->

<a id='3e0acc91-563d-4b17-b8ac-9e5085b19c07'></a>

3

<a id='2601d37f-9772-4071-b64f-c0a68b1eb063'></a>

Computational and Mathematical Methods in Medicine

<a id='c26d3aa9-8f8d-432c-a6e6-5bf62cf9c6c0'></a>

$$\dot{U}(t) = \alpha U(t) \left(1 - \frac{U(t) + I(t)}{K}\right) - \beta U(t-\tau_1)V(t-\tau_1) - \delta_0 U(t-\tau_2)C(t-\tau_2),$$ 
$$\dot{I}(t) = \beta U(t-\tau_1)V(t-\tau_1) - I(t) - \delta_1 I(t-\tau_2)C(t-\tau_2),$$ 
$$\dot{V}(t) = bI(t) - \beta U(t-\tau_1)V(t-\tau_1) - \gamma V(t),$$ 
$$\dot{C}(t) = g(t) - \lambda C(t).$$ 
(3)

<a id='a706ba67-10e9-4041-9ae6-d8f09d642bc1'></a>

### 3. Mathematical Analysis of Model without Delay

In this section, the model without delay (1) is analysed. The variables in system (1) are first rescaled by setting `t̄ = δt`, `U = KŪ`, `I = KĪ`, `V = V₀V̄`, and `C = C₀C̄`. Taking `V₀ = K`, the parameters are renamed to become

`ā = α/δ, β̄ = βV₀/δ, δ₀̄ = δ₀C₀/δ, δ₁̄ = δ₁C₀/δ, b̄ = bK/V₀, γ̄ = γ/δ` (4)

`φ = q/(δC₀), ψ = λ/δ, ā = a/δ`

<a id='ee22fa1e-fa2f-42cb-9104-25447dd4b902'></a>

For simplicity, we drop the bars and equation (1)
becomes

$\dot{U}(t) = \alpha U(t)(1 - U(t) - I(t)) - \beta U(t)V(t) - \delta_0 U(t)C(t)$,
$\dot{I}(t) = \beta U(t)V(t) - I(t) - \delta_1 I(t)C(t)$,
$\dot{V}(t) = bI(t) - \beta U(t)V(t) - \gamma V(t)$,
$\dot{C}(t) = \xi(t) - \psi C(t)$.
(5)

<a id='bbbbc6e2-de69-4a84-8d09-842cea3f63be'></a>

ξ(t) = φ, ξ(t) = φ exp(−at), and φ sin² (at), respectively,
are the constant, exponential, and sinusoidal infusion functions. For this model to be biologically meaningful, its solutions should be positive and bounded because they represent concentrations. Well-posedness theorems of model (5) are stated and proved in Appendix A.

<a id='e9b78426-099b-4259-992c-cb73984c2059'></a>

3.1. Model Solutions. To investigate the efficacy of each treatment and their combination, we first study the dynamics of the system without treatment. Without any form of treatment, model (5) is reduced to only one equation:

<a id='f511d2ed-cf18-4968-ad23-2d0c5f36be16'></a>

Ů (t) = αU (t) (1 – U (t)), (6)
U (0) = U₀,

<a id='1c5acd5e-a614-4cb3-9226-caa18fcf1d07'></a>

whose solution is

$U(t) = \frac{U_0}{(1-U_0)\exp(-\alpha t) + U_0}$ (7)

$\lim_{t \to \infty} U(t) = 1,$

<a id='c369df01-fce3-4890-ad43-90d0b8e56de7'></a>

implying that the tumor logistically grows to its maximum
fractional size. Next, the model (5) is analysed, with che-
motherapy, with virotherapy, and then with both treatments
incorporated. We obtain, where possible analytical and time
invariant solutions which predict the long term dynamics of
the model equation (1).

<a id='d3d68f61-9251-4949-8c52-b49abf19f10f'></a>

Without virotherapy (V (t) = 0), the system (5) is transformed to

Ů (t) = αU (t) (1 – U (t)) – δ₀U (t)C(t),
Ċ (t) = ξ (t) – ψC (t), (8)

<a id='8bd681d5-764c-49a2-beb8-503c059586c5'></a>

with U(0) = U₀ and C(0) = C₀. The second equation in equation (8) is a first-order linear ordinary differential equation which can easily be solved to give

C(t) = exp(-ψt)(∫ξ(t)exp(ψt)dt + R),
(9)

<a id='211b58d1-b93b-47bd-982f-e2a5fa27bf0a'></a>

where R is a constant of integration. The solution to the first
equation in equation (8) depends on the infusion function
͕(t). For a fixed infusion function ͕,

<a id='f6036470-e808-48af-9179-33b613c8ee79'></a>

U(t) = \frac{e^{\left(at-\left(\delta_0\phi t/\psi\right)+\left(\delta_0e^{\left(-\psi t\right)}/\psi\right)\right)}}{\alpha\int e^{\left(at-\left(\delta_0\phi t/\psi\right)+\left(\delta_0e^{\left(-\psi t\right)}/\psi\right)\right)}dt + \left(e^{\delta_0\psi}/U_0\right)} \text{ (10)}

C(t) = \left(C_0-\frac{\phi}{\psi}\right)e^{-\psi t} + \frac{\phi}{\psi}

<a id='af7254cf-2780-496f-958b-a53e4a7d2ef8'></a>

From the solution of C(t) in equation (10),
$$\lim_{t\to\infty} C(t) = \frac{\phi}{\psi} \quad (11)$$

<a id='06c1d397-ff7c-469e-b66e-2092c31eaf79'></a>

Biologically, it can be inferred that with a constant drug infusion and without virotherapy, the tumor is not completely cleared and a certain proportion of the drug remains in body tissue. The tumor clearance depends on the drug induced lysis of the tumor and the drug infusion rate which should be maximized and the tumor growth and drug decay rate which should be minimized.
For ξ(t) = φ exp(−at),

<a id='553710f7-b1ea-46c1-a01e-aae57b34ce9d'></a>

U(t) = (1/a) ∫ [e^((aat/a-ψ)-(αψt/a-ψ)+(cδ₀e^(-ψt)/(a-ψ))-(acδ₀e^(-ψt)/(a-ψ)ψ)+(δ₀φe^(-at)/(a-ψ)a))] / [e^((aat/a-ψ)-(αψt/a-ψ)+(cδ₀e^(-ψt)/(a-ψ))-(acδ₀e^(-ψt)/(a-ψ)ψ)+(δ₀φe^(-at)/(a-ψ)a))] dt + (e^(cδ₀/a-ψ) / U₀)'

C(t) = ( (C₀ψ - φ) / ψ - (φe^(-at+ψt)) / (a - ψ) ) e^(-ψt) , (12)

<!-- PAGE BREAK -->

<a id='072c3a1a-9940-4481-9782-f398661d1f77'></a>

4

<a id='9835b015-b2eb-4cf3-b0eb-9cf06754bfca'></a>

Computational and Mathematical Methods in Medicine

<a id='8330a2f2-1a14-4c46-959f-9f37e039045a'></a>

where $c = (C_0\psi - \phi/\psi)$.
From equation (12),

$\lim_{t\to\infty} C(t) = 0,$

$\lim_{t\to\infty} U(t) = U_*,\quad (13)$

<a id='3f3eb41c-d2de-496a-9039-78f9341a7841'></a>

where U_∗ is a fractional tumor cell concentration between 0 and 1. This suggests that with a single dosage infusion of the chemotherapeutic drug with exponential decay and without virotherapy, the tumor cannot be cleared from body tissue. The drug is also completely depleted from the body.
When ξ(t) = φ sin²(at) is substituted in equation (8),
the resulting differential equations are solved to give

<a id='29a25949-0889-455e-ba6a-a0c298eff5ed'></a>

$$C(t) = \frac{1}{2} \left( 2R - \frac{\psi^2 \cos(2at)e^{(\psi t)} + 2a\psi e^{(\psi t)} \sin(2at) - (4a^2 + \psi^2)e^{(\psi t)}\phi}{4a^2\psi + \psi^3} \right) e^{(-\psi t)} \quad (14)$$

<a id='3faaac7b-bc49-4f80-82f6-2780c0c43bc2'></a>

where

$R = C_0 + \frac{\psi^2 - \phi (4a^2 + \psi^2)}{2\psi (4a^2 + \psi^2)}$ (15)

$\lim_{t \to \infty} C(t) = C_* = f (a, \phi, \psi).

<a id='cd83fe27-f927-440c-9ab0-7205a9ac1e76'></a>

This suggests that with time, some drug concentration remains in the body tissue.

<a id='8575660c-055d-4cb0-b446-6e6152991739'></a>

**Theorem 1.** *The system (8), with constant infusion, has no periodic solutions for positive U (t) and C (t).*

<a id='274a1c23-ecd0-43e3-b9c5-6d2f4d6663f3'></a>

Proof. Using Dulac's criterion ([40]):
Suppose Ẋ = f (x) and f (x) is continuously differen-
tiable on a simply connected domain D ⊂ R. If there exists
a real valued function g(x) such that ∇ · (gẊ) = ∇ · (gf)
has one sign in D, then there are no closed orbits in D. Using
Dulac's criterion, it is sufficient to show that

∂/∂U (gU̇) + ∂/∂C (gĊ) ≠ 0, ∀U, C ∈ R+².
(16)

<a id='006f1e65-479d-481b-a5bc-b640d25df2f8'></a>

Consider

$g(U, C) = \frac{1}{UC}$

$\nabla \cdot (g\dot{X}) = \frac{\partial}{\partial U} (g\dot{U}) + \frac{\partial}{\partial C} (g\dot{C})$, (17)

$= -\left(\frac{\alpha}{C} + \frac{\xi(t)}{UC^2}\right) < 0, \quad \forall U, C \in (\mathbb{R}^+)^2.$ 

$\square$

<a id='ec964601-2669-48c1-8728-2d8b4cb16042'></a>

**Theorem 2.** _The system (8) has at least two steady states for each of the drug infusion functions:_

(1) For the constant drug infusion function $\xi(t) = \phi$, there are two steady states of equation (8): $(U = 0, C = (\phi/\psi))$ which is locally asymptotically stable provided that $\delta_0\phi > \alpha\psi$ and $(U = 1 - (\delta_0\phi/\alpha\psi), C = 0)$ which is locally asymptotically stable provided that $\delta_0\phi + \alpha\psi > 2\delta_0\phi\psi^2$; otherwise, it is unstable.

(2) For the exponential drug infusion $\xi(t) = \phi \exp(-at)$, equation (8) has two steady states: $(U = 0,

<a id='e2c6972d-f4c6-46c9-ad4c-006b8af4bdad'></a>

C = 0, W = 0) which is unstable and (U = 1, C = 0,
W = 0) which is locally asymptotically stable.

<a id='93f1a956-eecb-489f-a404-abf6467859b3'></a>

(3) For the sinusoidal infusion function, there are four steady states of equation (8): (U = 0, C = 0, W = 0), (U = 1, C = 1, W = 0), and (U = (ααψ – δ₀φ/ααψ), C = (φ/αψ), W = (φ/a)) which are unstable and (U = 0, C = (φ/αψ), W = (φ/a)) which is locally asymptotically stable if δ₀φ > ααψ and φ < 1.

<a id='1da9eaaa-cc50-442c-ae8a-6692663d6305'></a>

Proof.

(1) It is easy to show that when equation (8) is equated to zero, one obtains two steady states. The characteristic polynomial of the Jacobian matrix for equation (8) evaluated at (0, (φ/ψ)) is

λ² + \left(-\alpha + \frac{\delta₀\phi}{\psi} + \psi\right)\lambda + \delta₀\phi - \alpha\psi, (18)

<a id='0af2c4f3-ff76-4e6b-ac4f-bc17143bfada'></a>

whose roots $\lambda$ can only be negative if $\delta_0\phi > \alpha\psi$.
The characteristic polynomial evaluated at $(1-(\delta_0\phi/\alpha\psi), 0)$ is

$\lambda^2 + \left(-2\delta_0\phi\psi + \alpha + \frac{\delta_0\phi}{\psi} + \psi\right)\lambda - 2\delta_0\phi\psi^2 + \delta_0\phi + \alpha\psi,$ (19)

<a id='36cf8a7b-c2de-4e8e-a682-dcfab80e4276'></a>

whose roots are negative provided that $\delta_0\phi + \alpha\psi >$ $2\delta_0\phi\psi^2$.

<a id='4ebe5415-d7b0-4d56-b6cc-37a998442eba'></a>

(2) By letting W = φ exp(−at), equation (8) is turned into an autonomous system:

Ů(t) = αU(t)(1 − U(t)) − δ₀U(t)C(t),

Ċ(t) = W − ψC(t),

Ẁ(t) = −aW.
(20)

<a id='fb23fb52-56a9-419a-ae3e-50f835f33358'></a>

The eigenvalues of the Jacobian matrix for equation (20) evaluated at (0,0,0) which are -\u03c8, \u03b1, and 0 and at (1,0,0) which are -\u03b1, -\u03c8, and -\u03b1 are all negative.

<a id='27eb6f00-2754-4dba-bc2c-df886ad64bc9'></a>

(3) Similarly, by letting W = φ sin² t, equation (8) becomes the autonomous system:

<!-- PAGE BREAK -->

<a id='6d353d5f-933d-4026-926d-7e6baf8063a7'></a>

5

<a id='9663c8d3-d0bd-44d2-ad02-98a7bf73420e'></a>

Computational and Mathematical Methods in Medicine

Û(t) = αU(t)(1 − U(t)) − δ₀U(t)C(t),

Ċ(t) = W − ψC(t),

Ẇ(t) = [4aW(ϕ − W)]^1/2.

(21)

<a id='ba9ea704-5d1d-440a-9937-5362082c9cf1'></a>

The eigenvalues of the Jacobian matrix for equation (20) evaluated at (0,0,0) are -ψ, α, and 0 and the eigenvalues evaluated at (1,0,0) are ψ, -α, and 0. For the third steady state to exist, aαψ ≥ δ₀φ, and the eigenvalues evaluated at this state are (-(aαψ - δ₀φ/aψ), -(4aφ/√4φ(1-φ)), -ψ), implying that for it to be locally asymptotically stable, δ₀φ > aαψ; yet for this to happen, the steady state will not exist. The eigenvalues evaluated at (U = 0, C = (φ/aψ), W = (φ/a)) are (-(aαψ - δ₀φ/aψ), -(4aφ/√4φ(1-φ)), -ψ) implying that this steady state is locally asymptotically stable if δ₀φ > aαψ and φ < 1.

<a id='14bbc3ed-d0e1-47eb-ba24-afdabd2cac09'></a>

Theorems 1 and 2 show that there are no periodic so-lutions in the dynamics of equation (8) and with a constant drug infusion, the tumor can be eliminated from body tissue by chemotherapy provided that the combination of the chemotherapeutic drug-induced lysis of the tumor and the drug infusion is greater than the combination of the intrinsic tumor growth rate and the drug deactivation rate. The tumor can also be wiped out with a periodic drug infusion provided that the combination of the tumor-induced lysis by the drug and the dosage is greater than the intrinsic tumor growth rate and drug decay rate. With the exponential infusion method, the tumor is not removed from body tissue and may grow to its maximum size.

<a id='08bd0f0b-2b54-4e22-a3c1-3531ecdd4fa3'></a>

Without chemotherapy, equation (5) is reduced to

$\dot{U}(t) = \alpha U(t)(1-U(t)-I(t)) - \beta U(t)V(t),$

$\dot{I}(t) = \beta U(t)V(t) - I(t),$

$\dot{V}(t) = bI(t) - \beta U(t)V(t) - \gamma V(t).$ (22)

<a id='ba108bc4-5fc4-493e-99bd-dc4f3a908624'></a>

The analytical solutions to system (22) are not easy to obtain. The derivatives of equation (22) are therefore equated to zero to obtain time invariant solutions and investigate their stability by linearizing equation (22) about the steady states. □

<a id='81f08d72-367c-4a77-9ea5-2bf86e11226c'></a>

Theorem 3.

(1) If β + γ > bβ, the system (12) has two steady states: a tumor free cell state (0,0,0) which is unstable and an infection tumor free state (1,0,0) which is locally asymptotically stable.
(2) If bβ > β + γ, the system (22) has three steady states: the tumor free state (0,0,0) and the infected free state (1,0,0) which are unstable and a tumor dor-mant state:

<a id='cd1558c5-d895-4a2b-92c6-9af728d7515d'></a>

\begin{cases}U = \frac{\gamma}{(b-1)\beta^2} \\ I = \frac{\alpha\gamma(\beta(b-1)-\gamma)}{\beta(\beta(b-1)^2+\gamma(b-1))}\end{cases}, (23)
V = \frac{\alpha(\beta(b-1)-\gamma)}{(b-1)^2\beta^2+\alpha\gamma}, b > 1,

<a id='883ad40f-2e21-463a-b5d3-4aae573654d4'></a>

which is locally asymptotically stable if a₀, a₁, a₂ > 0
and a₁a₂ > a₀ where aᵢ are coefficients of the characteristic equation.

<a id='405dbc86-ab03-402f-93d5-bc75234803db'></a>

Proof.

(1) The characteristic equation evaluated at (0, 0, 0) is
λ³ + (γ - α + 1)λ² + (γ – αγ – α)λ – αγ = 0,
(λ – α) (λ + 1) (λ + γ) = 0, (24)
from which λ₁ = α, λ₂ = −1 and λ₃ = −γ, thus rendering it unstable.
The characteristic equation evaluated at (1, 0, 0) is
(λ + α)(λ² + λ(1 + β + γ) + β + γ - bβ) = 0, (25)
from which λ₁ = -α and λ² + λ(1 + β + γ) + β + γ - bβ = 0 which are all negative since β + γ > bβ.
(2) The characteristic polynomial evaluated at the tumor dormant state is λ³ + a₂λ² + a₁λ + a₀ = 0, where
a₂ = (2Aα + Aβ + Cβ - α + γ + 1),
a₁ = (2A²αβ – Aαβ + Cαβ – Abβ + 2Aαγ + Cβγ + 2Aα
+ Aβ + Cβ – αγ - α + γ),
a₀ = -2A²abβ + 2A²αβ + Aabβ + Cαβγ – Aαβ + 2Aαγ
+ Cβγ – αγ, (26)

<a id='654d2808-ed53-4903-9dfa-2b8aec147839'></a>

and A, B, C are the coordinates of the tumor dormant state. Using Routh–Hurwitz stability criterion, this state will only be locally asymptotically stable if a₀, a₁, a₂ > 0 and a₁a₂ > a₀. □

<a id='b40099a8-5162-464d-88fc-69944521243f'></a>

Since the infected tumor-free state is undesirable, the reverse of the condition β + γ > bβ is necessary for tumor eradication from body tissue. In other words, bβ > β + γ, that is, the product of the virus replication rate and their burst size should be greater than the sum of the burst size and virus replication rate. We also notice from equation (23) that

<a id='94800f3b-07b4-4b30-b2ca-d538c3cf116d'></a>

$$\lim_{\beta \to \infty} U = \lim_{b \to \infty} U = 0. \quad (27)$$

<a id='16eea862-5b04-430b-9ce1-7f9c544c992a'></a>

It is therefore evident that high virus replication rate ̖ and burst size _b_ lead to lower tumor cell concentrations. The

<!-- PAGE BREAK -->

<a id='6afc07db-0233-4e10-a0f7-ad292163fad2'></a>

6

<a id='9031521f-59dd-4a53-ae22-78158a723f5c'></a>

Computational and Mathematical Methods in Medicine

<a id='8ebfa912-65e8-46b0-a22f-0b336efef4ba'></a>

steady-state solutions of equation (23) involve many pa-rameters, thereby giving rise to large expressions in the conditions for its stability. It is therefore a difficult undertak-ing to infer biological implications from these conditions. Nevertheless, it can be observed that virotherapy may only succeed in eliminating cancer from body tissue when the virus deactivation rate is very small or even zero and the virus replication rate very high.

<a id='8662d70b-3e97-47a0-a6c8-70d18bd2b299'></a>

Next, the model with both treatments is analysed. For a constant drug infusion rate φ, the system (5) has three steady states;

<a id='3baee960-f6db-4b09-8744-12e8abb20dde'></a>

(i) Tumor-free steady state:

<a id='5cc720f1-cf5c-47c9-b096-cbf9c7e43f23'></a>

(U = 0, I = 0, V = 0, C = ̈̕/̓̈). (28)

<a id='364a0837-fc15-4e8e-92cb-b4de6e0fc3c8'></a>

Here, the tumor and viruses are cleared from body
tissue by the coupled treatment and a fraction of the
chemotherapeutic drug remains in body tissue. The
eigenvalues of the Jacobian matrix evaluated at this
state are

<a id='6bae8d18-ecae-4233-971d-43c6b2fe011c'></a>

λ₁ = - (δ₀φ - αψ) / ψ

λ₂ = - (δ₁φ + ψ) / ψ

λ₃ = -γ,

λ₄ = -ψ,

(29)

<a id='8d3f5105-d1c7-4b84-aaf9-64ba0bdca7b3'></a>

implying that this desirable state is locally asymptotically stable if δ₀φ > αψ. From this condition, in order to clear a tumor, the combination of the rate at which the drug kills the uninfected tumor cells and the drug infusion must be higher than the tumor growth rate and deactivation of the drug from body tissue.

<a id='7b3b870b-dcac-4f10-981d-c83e09679ca4'></a>

(ii) Infected tumor-free state:

$$(U = 1 - \frac{\delta_0\phi}{\alpha\psi}, I = 0, V = 0, C = \frac{\phi}{\psi})$$ (30)

<a id='a1c65363-9a85-4f4d-9fa6-73e249e47e91'></a>

In this state, the whole tumor is not cleared as a fraction of uninfected tumor cells remain and all the infected ones are cleared by the treatment combination. Using the parameter values in Table 1, the eigenvalues of the Jacobian matrix evaluated at the infected tumor-free state are 0.403, 8.13, and 2.598 ± 2.418i, implying that the infected tumor-free state is unstable.

<a id='ed3ad996-be19-4e10-ac51-d97fd9e73808'></a>

(iii) Tumor dormant state:

$$U = \frac{(\delta_1\phi + \psi)\gamma}{b\psi(b - 1) - \delta_1\phi\beta^2}, I = \frac{\Gamma\gamma}{(\delta_1\phi - (b-1)\psi)\beta^2}$$
$$V = \Gamma, C = \frac{\phi}{\psi}\quad(31)$$

<a id='ad7e7e1b-7370-4798-866b-cdefd1a04ae6'></a>

where

<a id='647ad81e-e81b-480a-9307-c78f2ce2c957'></a>

\Gamma = \frac{(\beta\delta_0\delta_1\phi^2 - b\beta\delta_0\phi\psi - \alpha\beta\delta_1\phi\psi - \alpha\delta_1\gamma\phi\psi + a\beta\psi^2 + \beta\delta_0\phi\psi - \alpha\beta\psi^2 - \alpha\gamma\psi^2)}{(b - 1)\beta^2\psi^2 + \alpha\beta\gamma\psi^2 - \beta^2\delta_1\phi\psi)} \quad (32)

<a id='c2ab78b5-4037-4529-8361-98f5adf2df5c'></a>

It is a difficult undertaking to investigate the stability of this state without substituting parameter values because of the many terms involved. Using the parameter values in Table 1, the eigenvalues are -0.031, -0.025, -1.01, and -8.13, implying that this state is stable.

<a id='c2104ebb-7d93-421c-aa09-a45e27b874a2'></a>

With the consideration of an exponential infusion
function ξ(t) = φ exp(−at), the equation (5) are first
turned into an autonomous system of differential equations
by letting W = φ exp(−at). This system has three steady
states:

<a id='8c106027-8ff7-4d36-8f9e-a7f99308619d'></a>

(i) A tumor-free state where all cell concentrations
diminish to zero:

(U = 0, I = 0, V = 0, C = 0, W = 0).

(33)

<a id='6ccef9d1-a9de-4f49-8519-67e85d805273'></a>

This state is unstable because the eigenvalues −γ, −ψ, −a, −1, and α are not all negative.

<a id='7c4db441-72fb-4ca8-8ff4-803aeaa99418'></a>

(ii) A state where the tumor grows to its maximum size:

<a id='0cb08b27-11da-4655-8123-b761060d3704'></a>

(U = 1, I = 0, V = 0, C = 0, W = 0). (34)

<a id='8c37000b-e41e-40a5-a68e-446560383f67'></a>

(iii) The characteristic polynomial evaluated at this state is equation (25) and this state is locally asymptot- ically stable if β + γ > βγ, otherwise it is unstable.

$$U = \frac{\gamma}{(b-1)\beta}, I = \frac{(ab-\alpha)\beta\gamma - \alpha\gamma^2}{(b-1)^2\beta^2 + (ab-\alpha)\beta\gamma}\quad (35)$$

$$V = \frac{(ab-\alpha)\beta - \alpha\gamma}{(b-1)\beta^2 + \alpha\beta\gamma}, C = 0, W = 0, b > 1.$$

<a id='4218a9e0-4fc6-4b97-9346-8545e2e5c058'></a>

The eigenvalues evaluated at this steady state are also big expressions and difficult to analyse analytically and extract conditions for stability. With the set of parameter values in Table 1, the eigenvalues are -0.1, -8.13, 1.054, and -0.014  0.085i, implying that this state is stable.

<a id='cfd8c1fb-f987-490b-8b90-3a0ad1bf8bb4'></a>

Similarly, with ξ (t) = φ sin² (at), one changes equation (5)
into an autonomous system of equations by letting W =
φ sin² (at). The autonomous system has six steady states:

<!-- PAGE BREAK -->

<a id='a907ffcf-d07b-4431-89c9-b0bc6ae89b3d'></a>

Computational and Mathematical Methods in Medicine

<a id='cde3b5fe-b3ef-432c-999d-6dd54feef56d'></a>

7

<a id='10903a37-885d-41f3-92dc-3cb257cddd6b'></a>

TABLE 1: Dimensional parameter values.
<table id="6-1">
<tr><td id="6-2">K</td><td id="6-3">α</td><td id="6-4">β</td><td id="6-5">δ</td><td id="6-6">γ</td><td id="6-7">b</td><td id="6-8">q</td><td id="6-9">λ</td><td id="6-a">δ₀</td><td id="6-b">δ₁</td></tr>
<tr><td id="6-c">106</td><td id="6-d">0.206</td><td id="6-e">0.001</td><td id="6-f">0.5115</td><td id="6-g">0.001</td><td id="6-h">10</td><td id="6-i">5</td><td id="6-j">4.16</td><td id="6-k">0.005</td><td id="6-l">0.006</td></tr>
<tr><td id="6-m">[41]</td><td id="6-n">[41]</td><td id="6-o">[41]</td><td id="6-p">[41]</td><td id="6-q">[41]</td><td id="6-r">[42]</td><td id="6-s">[23]</td><td id="6-t">[23]</td><td id="6-u">Estimated</td><td id="6-v">Estimated</td></tr>
</table>

<a id='6b2c2e63-08e6-424c-b2e4-967a9d728948'></a>

(i) Tumor-free state where all cell concentrations are wiped out of body tissue:

$(U = 0, I = 0, V = 0, C = 0, W = 0).$ (36)

The eigenvalues evaluated at this state are $-\gamma$, $-\psi$, $-a$, $-1$, and $\alpha$ implying that it is unstable.

(ii) A state where the tumor grows to its maximum size:

$(U = 1, I = 0, V = 0, C = 1, W = 0).$ (37)

The condition for stability of this state is same as with the exponential drug infusion case, that is, the state is locally asymptotically stable if $\beta + \gamma > \beta\gamma$.

(iii) Tumor-free state where some concentration of the drug remains:

$(U = 0, I = 0, V = 0, C = \frac{\phi}{a\psi}, W = \frac{\phi}{a}).$ (38)

<a id='4fad6466-03ec-4a2c-a3b2-6fd94ac106e2'></a>

This state is locally asymptotically stable if $\delta_0\phi > \alpha\psi$
and $(1/2) < \phi < 1$ because the eigenvalues evaluated at
this state are

$\frac{\delta_0\phi - \alpha\psi}{\psi}$,

$\frac{\delta_1\phi + \psi}{\psi}$,

$-\frac{2(2a\phi(\phi - \phi))}{\sqrt{4\phi(1-\phi)}}$,

$-\gamma$,

$-\psi$,
(39)

<a id='5539cfea-c1ad-4b30-8b56-7076f5dc206b'></a>

otherwise, it is unstable.

<a id='81a08b33-111d-4304-8a41-20f2478de124'></a>

(iv) Infected tumor-free state where all infected tumor cells are wiped but a certain proportion of the uninfected remains:

$$(U = \frac{a\alpha\psi - \delta_0\phi}{a\alpha\psi}, I = 0, V = 0, C = \frac{\phi}{a\psi}, W = \frac{\phi}{a})$$

$$a\alpha\psi \ge \delta_0\phi.$$
(40)

<a id='1ada0065-29d1-486e-83c5-75f28a1c9f4f'></a>

(v) Drug-free state where the chemotherapeutic drug is wiped out of body tissue and proportions of all the other cell concentrations remain:

$$U = \frac{\gamma}{(b-1)\beta}, I = \frac{(ab - \alpha)\beta\gamma - \alpha\gamma^2}{(b-1)^2\beta^2 + (ab - \alpha)\beta\gamma}$$ (41)

$$V = \frac{(ab - \alpha)\beta - \alpha\gamma}{(b-1)\beta^2 + \alpha\beta\gamma}, C = 0, W = 0, b > 1.$$

<a id='69b9e973-14ed-431f-89b9-13e757ee32c5'></a>

(vi) Tumor dormant state:

U = (δ₁φ + aψ)γ / ((ab - a)βψ - βδ₁φ'), I = Γ₂γ / (abψ - δ₁φ - aψ), V = γ₂ / aψ

C = φ / aψ, W = φ / a

<a id='e3a184a2-11a9-45e1-bb95-f2c40cd3b215'></a>

where (42)

<a id='876fc25b-a24c-4354-a63c-dd3594001ba4'></a>

$\Gamma_2 = \frac{a^2ab\beta\psi^2 - ab\beta\delta_0\phi\psi - \alpha\alpha\beta\delta_1\phi\psi - \alpha\alpha\delta_1\gamma\phi\psi - a^2\alpha\beta\psi^2 - a^2\alpha\gamma\psi^2 + \beta\delta_0\delta_1\phi^2 + \alpha\beta\delta_0\phi\psi}{(ab\beta\psi + \alpha\alpha\gamma\psi - \beta\delta_1\phi - a\beta\psi)a\beta\psi}$ (43)

<a id='f12ad4d8-e1f1-4403-b77a-83872564c3ac'></a>

The conditions for stability for the last three states all depend on huge expressions from which it is hard to extract meaningful biological implications. This analysis, however, suggests that with both treatments and using a sinusoidal type infusion, the tumor can be eliminated from body tissue provided that the combination of the drug infusion rate and the lysis rate of the tumor is greater than the combination of the tumor growth rate and rate of drug loss.

<a id='697f03ac-3f55-49e9-b237-e2f8ce6a701f'></a>

### 4. Mathematical Analysis of Delay Model
The nondimensionalised delay model is

<a id='f18edf95-8bd7-4b3d-9f59-031ff2950a1e'></a>

$$\dot{U}(t) = \alpha U(t) \left(1 - \frac{U(t) + I(t)}{K}\right) - \beta U(t - \tau_1)V(t - \tau_1)$$
$$\quad - \delta_0 U(t - \tau_2)C(t - \tau_2),$$
$$\dot{I}(t) = \beta U(t - \tau_1)V(t - \tau_1) - I(t) - \delta_1 I(t - \tau_2)C(t - \tau_2),$$
$$\dot{V}(t) = bI(t) - \beta U(t - \tau_1)V(t - \tau_1) - \gamma V(t),$$
$$\dot{C}(t) = \phi(t) - \psi C(t).$$

(44)

<a id='3c9cfa40-297b-47dd-a4ad-443349a9b9c5'></a>

Without virotherapy the model (44) in nondimensional
form becomes

<!-- PAGE BREAK -->

<a id='0177ce9a-f851-41e0-b19e-8761da4eae4b'></a>

8

<a id='ada48a52-04dd-4077-87b2-72397e4146f8'></a>

Computational and Mathematical Methods in Medicine

<a id='4170310b-0f14-4cc6-8707-c378a1951fb5'></a>

U̇(t) = αU(t)(1 - U(t)) - δ₀U(t - τ₂)C(t - τ₂), (45)
Ċ(t) = ϕ(t) - ψC(t).

<a id='077c6538-d100-414c-a50d-3e6ac63a6b72'></a>

The system (45) has two steady states: a tumor-free state T₀ = (0, (φ/ψ)) and a tumor dormant state (1 - (δ₀φ/αψ), 0), just as previously seen. Letting Z₁(t) = U(t) - U* and Z₄(t) = C(t) - C* where U*, C* are steady states of equation (45), the linearized model about (U*, C*) of equation (45) is

<a id='d7866fb3-8397-4af6-b6be-0ad73b9be24f'></a>

Ż₁(t) = αZ₁(t) - 2αU*Z₁(t) - δ₀U*Z₄(t-τ₂)
- δ₀C*Z₁(t-τ₂),
(46)

<a id='3b225952-ffda-4585-b7ba-64a9296fc103'></a>

Ż₄(t) = φ(t) – ψZ₄(t).

<a id='f2ccf77e-9aad-4b5c-a437-62a5d874d4bd'></a>

The characteristic equation of equation (46) evaluated at the tumor-free steady state is

<a id='11b9a32b-db98-4d14-adff-f6024574dfab'></a>

f(λ) = (λ + ψ) (λ - α + e^(-λτ₂)δ₀φ / ψ) = 0. (47)

<a id='2b033e58-44f0-4434-bc96-1b1365991284'></a>

For τ₂ = 0, we obtain the same characteristic polynomial as in the ODE case (Theorem 2). For τ₂ ≠ 0, equation (47) is a transcendental equation and therefore has infinitely many roots and also makes it nontrivial to determine these roots. Nonetheless, the following is noticed:

<a id='8e236203-64b4-490e-8f8c-81914fcd860b'></a>

Lemma 1.

(1) The tumor-free state T₀ is stable if τ₂ = (ψ/δ₀φ) and α = (δ₀φ/ψ), i.e., Equation (47) has a negative root -ψ and a zero double root.
(2) T₀ is stable for a sufficiently small τ₂, i.e., Equation (47) has negative real roots for 0 ≤ τ₂ ≤ τ₂₀.
(3) Equation (47) has a pair of purely imaginary roots ±iω if αψ ≤ δ₀φ and the other root is -ψ. Therefore, T₀ is unstable.

<a id='03d17157-b27d-4850-b1a3-00180d33c180'></a>

Proof.

(1) If τ₂ = (ψ/δ₀φ) and α = (δ₀φ/ψ), then

df/dλ = 2λ - α + (δ₀φe^(-λτ₂))/ψ - λτ₂ (δ₀φe^(-λτ₂))/ψ + ψ - τ₂δ₀φe^(-λτ₂),

d²f/dλ² = 2 - 2 (τ₂δ₀φe^(-λτ₂))/ψ + τ₂²δ₀φ( (λ/ψ) + 1).

<a id='54e66545-adeb-4266-b0d3-6b35b74f5e83'></a>

Form equation (48),

$$\frac{df}{d\lambda}\Big|_{\lambda=0} = 0,$$

$$\frac{d^2f}{d\lambda^2}\Big|_{\lambda=0} = \frac{\psi}{\delta_0\phi} > 0.$$

(49)

<a id='665a7bd5-f339-45c0-be3d-976dc39cec07'></a>

Thus, equation (47) has a double zero root.
(2) If we denote ρ(τ₂) + iω(τ₂) as the root of the equation (47), the tumor-free state is stable if

<a id='cb74ea86-60f8-4366-884c-22d922d48ef5'></a>

ρ(0) < 0. By continuity, if τ₂ > 0 is sufficiently small, we still have ρ(τ₂) < 0 and the tumor-free state is stable.

<a id='d1d2afec-0e39-45dc-b28f-0d437bc7912d'></a>

(3) If equation (47) has only purely imaginary roots, then the roots should be solutions to the equation

$\lambda - \alpha + \frac{e^{-\lambda\tau_2}\delta_0\phi}{\psi} = 0$. (50)

<a id='551ec3ca-4de8-4b82-8274-d4c42b51361b'></a>

Assume that λ = iω, ω > 0 is the root of equation (50).
Substituting λ = iω and separating real and imaginary parts,
one gets

$-α + \frac{\delta_0\phi}{\psi} \cos \omega\tau_2 = 0,$

$\omega - \frac{\delta_0\phi}{\psi} \sin \omega\tau_2 = 0.$ (51)

<a id='07033cbf-f7dd-4975-9870-3be3f757f536'></a>

Squaring both equations and adding gives

ω² + α² - δ₀φ² / ψ² = 0,
(52)

<a id='6d5ad6b3-3a38-44c6-94b7-202668096fc8'></a>

from which ω = ±√(((δ₀φ/ψ) + α) ((δ₀φ/ψ) – α)) if αψ > δ₀φ
and the critical values of τ₂ are

<a id='65134d4c-f893-455c-a59b-6d6f8cb48b53'></a>

τ_2k = 1/ω_+ (arccos(αψ / (δ_0φ))), k = 0, 1, 2, ... (53)

<a id='6331000a-2173-4e08-b8d1-c0b6d0151708'></a>

Without chemotherapy equation (44) becomes

U̇(t) = αU(t)(1 − U(t)) − βU(t − τ₁)V(t − τ₁),
İ(t) = βU(t − τ₁)V(t − τ₁) − I(t),
V̇(t) = bI(t) − βU(t − τ₁)V(t − τ₁) − γV(t).
(54)

<a id='b7a5ff98-8b5b-4354-b363-c153686ecc94'></a>

By letting $Z_1 (t) = U (t) - U^*$, $Z_2 (t) = I(t) - I^*$ and $Z_3 (t) = V (t) - V^*$ where $U^*, I^*$, and $V^*$ are steady states of equation (54), the linearized model about $(U^*, I^*, C^*)$ of equation (54) is

$\dot{Z}_1 (t) = \alpha Z_1 (t) - 2\alpha U^* Z_1 (t) + \alpha I^* Z_1 (t) - \alpha U^* Z_2 (t)$

$\quad + \beta V^* Z_1 (t - \tau_1) + \beta U^* Z_3 (t - \tau_1),$

$\dot{Z}_2 (t) = -\beta V^* Z_1 (t - \tau_1) + \beta U^* Z_3 (t - \tau_1) - Z_2 (t),$

$\dot{Z}_3 (t) = bZ_2 (t) + \beta V^* Z_1 (t - \tau_1) + \beta U^* Z_3 (t - \tau_1) - \gamma Z_3 (t).$

(55)

<a id='79638582-d91d-47fb-98c7-be1f9200ccf3'></a>

The characteristic equation of equation (55) at (1, 0, 0) is
$(\lambda + \alpha)[(\lambda + 1)(\lambda + \gamma + \beta e^{-\lambda\tau_1}) - b\beta e^{-\lambda\tau_1}] = 0. \quad (56)$

<a id='717d7882-efdf-4185-881f-64380be24344'></a>

For τ₁ = 0, we retrieve the same results as in Theorem 3.
For τ ≠ 0, we have a transcendental equation to solve. □

<a id='b3084f23-61ae-4700-90d8-8e793c7c1164'></a>

## 5. Numerical Simulations

### 5.1. Parameter Values. The parameter values used were obtained from fitted experimental data for untreated tumors and virotherapy in mice [41]. The tumor carrying capacity,

<a id='f5f10997-d8f5-4efa-bbde-297c35b5adf3'></a>

(48)

<!-- PAGE BREAK -->

<a id='6b9cd49e-f80c-43f1-b80c-58c63e318af1'></a>

9

<a id='63b1ddc1-9bdf-49e4-906e-1c7adabd311c'></a>

Computational and Mathematical Methods in Medicine

<a id='9624ee3e-250b-4b79-bdd2-b668105b0d4e'></a>

K, is taken to be 10⁶ cells per unit volume. The number of viruses produced per day *b* is to be in the range 10 – 1000 [42]. Drug infusion and decay rates *q* and λ agree with cancer pharmokinetic studies [33, 34].

<a id='d989f4a5-6438-475b-b213-7fd05f46ab4c'></a>

5.2. _Simulation Results._ Numerical simulations of the models (5) and (45) are presented, first with monotherapies followed with combination treatment. In all simulations, unless stated otherwise, initial concentrations are considered to be U₀ = 1, I₀ = 0, V₀ = 0.1, and C₀ = 0.1 with a high fractional untreated tumor cell count to necessitate clinical intervention. The equations were integrated using a Runge-Kutta fourth-order scheme and implemented in MATLAB. It is worth noting that the scale for the time and concentrations is, respectively, 1 unit ≈ 2 days and 1 unit = 10⁶ number of cells.

<a id='fcc670f9-04fe-491d-b3b2-544b67bd1640'></a>

Figure 1 shows numerical solutions of the chemo-only model (8). The figure shows that despite the drug infusion method, the tumor is not cleared from body tissue. These numerical solutions agree with the analytical results obtained in the previous sections that chemotherapy on its own may not clear all tumor cells in body tissue, and the tumor grows to its maximum size and the drug concentration decays to zero. Section 3 revealed that total tumor clearance from body tissue can possibly be achieved if δ₀φ > αψ. Nonetheless, the parameter values used do not conform to this condition.

<a id='d6e1e89b-698d-41b3-8c11-0e19c97ef898'></a>

Figure 2 shows the dynamics of the viro-only model. It is
clear from this figure that virotherapy alone could possibly
clear all tumor cells from body tissue provided that the virus
infection rate is high and with a large virus burst size. Fig-
ures 2(a) and 2(b) show a variation of the fractional tumor and
virus concentrations against time for different values of the
virus replication rate. It is noticed that with a small virus
infection rate for example β = 10⁻⁶, it takes a longer time to
clear the tumor cells. Figures 2(b) and 2(c) show a variation of
the fractional concentrations with two different burst sizes.
From these figures, we notice that when b = 10, it takes about
10 days to reduce the whole tumor concentrations to zero
while it takes only about 5 days with b = 100, implying that
a high virus burst size yields a quick recovery with virotherapy
treatment. These numerical intimations concur with the an-
alytical results established in Section 3.1.

<a id='1285bc4a-7d12-4ff4-9334-5a9e3f21f273'></a>

Figure 3 displays the dynamics of model (5) with both treatments. The numerical results are similar to those of Figure 2, only that with both treatments, it takes a shorter time to bring the tumor cell concentrations to zero. High values of the virus infection rate and burst size lead to tumor clearance in a shorter time period. Both Figures 2 and 3 show that an increase in the virus multiplication rate and burst size increase the infected tumor cells concentration. For example, comparing Figures 3(a) and 3(b), the number of infected tumor cells was about 0.15 × 10^6 when b = 15 and this increased to 0.35 × 10^6 when b = 25.

<a id='141f92c1-a776-4049-b12e-0f76143d36d6'></a>

Model (44) was simulated using dde23 in MATLAB. Figure 4 displays the numerical simulations for the delay model (44) with low and high values of τ₁ and τ₂, the virus, and chemotherapeutic delays. Since secondary transcription and viral protein synthesis can be delayed by about six to

<a id='3e988f69-b3da-4986-ab48-1d4703cc6419'></a>

eight hours [37], τ₁ was considered to be between 0.001 and 0.01. The chemotherapeutic response delay is higher than the virus response delay, thus τ₂ was taken to be between 0.1 and 0.3. The figure shows that when both delays are increased, the time it takes for cell concentration solutions to converge is slightly increased although they converge at the same steady states as without the delay. For τ₁ = 0.001 in Figure 4(a), it took about 4 days for the whole tumor to clear whereas it took about 8 days with τ₁ = 0.01 in Figure 4(b). Comparing Figures 4(b) and 4(c), when τ₂ was increased from 0.001 to 0.3, the time it took for the whole tumor to be cleared was increased from six to eight days. Initially there are oscillations for high values of the chemotherapeutic delay although the cell concentrations converge at the same steady states, just as the case with no delays. Figure 5 is a close up form of Figure 4 to display oscillations caused by the virus and drug delays. The oscillations only occur in the initial stages of treatment but later fade away. Nonetheless, the results in Figures 4 and 5 suggest that it is imperative to design viruses and drugs which are highly responsive in order to minimize these delays.

<a id='5cc2caea-c25a-45e0-897c-24b41b8e7dff'></a>

## 6. Discussion
The results in this study contend with previous experimental and mathematical studies that oncolytic viruses enhance chemotherapeutic drugs in the treatment of cancer [12,13,15–20]. A study by Ungerechts et al. [16] examined the synergy between a reprogrammed oncolytic virus and two chemotherapeutic drugs in the mantle cell lymphoma (MCL). They investigated the efficacy of different procedures of a measles virus in combination with fludarabine and cyclophosphamide (CPA). Their study suggested that that CPA administration before virotherapy enhanced oncolytic efficacy. An experimental study by Ulasov et al. [17] indicated that the combination of virotherapy and temozolomide is capable of eliminating malignant glioma. Their results showed that 90% of treated mice survived beyond the 100 days' mark after being treated. Another study by Alonso et al. [18] showed that the amalgamation of oncolytic adenovirus (ICOVIR-5) with either everolimus (RAD001) or temozolomide (TMZ) resulted in an enhanced antiglioma effect. Recent mathematical studies by Malinzi et al. [19, 20] assert that combining chemotherapeutic drugs with oncolytic viruses is more efficient than using either treatments alone. In [20], it is indicated that although chemotherapy alone may clear tumor cells from body tissue if drug efficacy is bigger than the tumor growth rate, the use of both OV and drugs leads to enhanced treatment effects.

<a id='8f5f64d2-6844-469e-8141-b04ccd33740a'></a>

Biologically, the reduction of a tumor to undetectable levels in less than a week is unrealistic in comparison to existing clinical and research studies [43]. The duration of cancer treatment depends on several factors including the type of cancer being treated and the patient cells' characteristics. This makes it hard to predict the time period to clear a tumor in body tissue. Moreover, a tumor can be reduced to insignificant levels but may later regrow [44]. Nevertheless, this study agrees with the fact that chemovirotherapy is highly likely to bring the tumor to

<!-- PAGE BREAK -->

<a id='04196db4-52a2-40b4-871f-6024c5109abf'></a>

10

<a id='b0180790-e038-4c96-a999-f5f146d0cf79'></a>

Computational and Mathematical Methods in Medicine

<a id='b2af3fb5-6240-4e66-8cd4-43c6e87c5f0b'></a>

<::chart: The figure contains three subplots (a), (b), and (c), each displaying a line graph of 'Fractional concentrations' (y-axis, ranging from 0 to 1) versus 'Time' (x-axis, ranging from 0 to 20). Each subplot shows two curves: one for 'Tumor' (red line with circular markers) and one for 'Chemotherapeutic drug' (blue line).

(a) In this subplot, representing a constant drug infusion, the 'Tumor' concentration starts around 0.8, decreases sharply to about 0.65, then gradually increases and stabilizes near 0.95. The 'Chemotherapeutic drug' concentration starts near 0.2, drops very quickly to almost 0, and then remains close to 0.

(b) In this subplot, representing an exponential drug infusion, the 'Tumor' concentration starts around 0.8, decreases sharply to about 0.65, then gradually increases and stabilizes near 0.95. The 'Chemotherapeutic drug' concentration starts near 0.2, drops very quickly to almost 0, and then remains close to 0.

(c) In this subplot, representing a sinusoidal drug infusion, the 'Tumor' concentration starts around 0.8, decreases sharply to about 0.65, then gradually increases and stabilizes near 0.95. The 'Chemotherapeutic drug' concentration starts near 0.2, drops very quickly to almost 0, and then remains close to 0.

FIGURE 1: Solutions of the model without virotherapy: equation (5) showing a variation of fractional concentrations with time, using (a) a constant, (b) an exponential, and (c) a sinusoidal drug infusion. The initial cell concentrations are U₀ = 0.8 and C₀ = 0.2.::>

<a id='5272a201-f019-4e0d-bbd6-17e600983648'></a>

<::figure: chart::>  
(a)  
Graph with x-axis "Time" from 0 to 5 and y-axis "Fractional cell concentrations" from 0 to 1.  
- Uninfected tumor (red line with circles): Values decrease from 1 at Time 0, passing through approximately 0.5 at Time 2.5, to approximately 0.05 at Time 5.  
- Infected tumor (black dashed line with asterisks): Values increase from 0 at Time 0, reaching a peak of approximately 0.32 at Time 3.5, then decrease to approximately 0.15 at Time 5.  
  
(b)  
Graph with x-axis "Time" from 0 to 5 and y-axis "Fractional cell concentrations" from 0 to 1.  
- Uninfected tumor (red line with circles): Values decrease rapidly from 1 at Time 0 to 0 at approximately Time 1.  
- Infected tumor (black dashed line with asterisks): Values increase rapidly from 0 at Time 0, reaching a peak of approximately 0.67 at Time 1.2, then decrease gradually to approximately 0.02 at Time 5.  
  
Legend for both plots:  
- Uninfected tumor (red line with circles)  
- Infected tumor (black dashed line with asterisks)  
<::>  
FIGURE 2: Continued.

<!-- PAGE BREAK -->

<a id='98871265-2bed-4e2a-93f4-17f7971bb8a4'></a>

Computational and Mathematical Methods in Medicine

<a id='56bf9775-f249-4074-99eb-b3910e58304e'></a>

11

<a id='a25ed654-ab63-4625-a924-897f45c72247'></a>

<::chart: Line chart showing fractional cell concentrations versus nondimensional time. Two subplots are presented: (c) and (d).:>
<::chart: Subplot (c): Line chart with 'Time' on the x-axis (0 to 5) and 'Fractional cell concentrations' on the y-axis (0 to 1). Two lines are plotted: 'Uninfected tumor' (red circles) which starts at 1 and drops to 0 around time 0.5, and 'Infected tumor' (black asterisks) which starts at 0, peaks around 0.8 at time 0.5-0.6, and then decreases towards 0. This subplot corresponds to b = 10, β = 10⁻⁶.:>
<::chart: Subplot (d): Line chart with 'Time' on the x-axis (0 to 5) and 'Fractional cell concentrations' on the y-axis (0 to 1). Two lines are plotted: 'Uninfected tumor' (red circles) which starts at 1 and drops to 0 around time 0.5, and 'Infected tumor' (black asterisks) which starts at 0, peaks around 0.95 at time 0.5-0.6, and then decreases towards 0. This subplot corresponds to b = 100, β = 10⁻⁶.:>
FIGURE 2: Solutions of model (12) without chemotherapy showing a variation of fractional concentrations with nondimensional time using low and high values of the virus replication rate β and burst size b, that is, (a) β = 10⁻⁶, b = 10; (b) β = 10⁻³, b = 10; (c) b = 10, β = 10⁻⁶; and (d) b = 100, β = 10⁻⁶.

<a id='31fcc04d-e14c-43f8-bd4c-43ed8d5214aa'></a>

undetectable levels in a short time period just as previously
established in [19, 20].

<a id='9c0af2bd-febf-4bd1-a983-33d6dd320f66'></a>

The mathematical model considered in this study is built on a couple of simplifying assumptions and thus omits pertinent biological aspects. For example, the drug infusion functions considered are not pragmatic. It is thus imperative to extend this study to consider more realistic drug infusion functions that describe all the important pharmacodynamics properties. Nonetheless, this study indicates that a cancer patient should not be given a single bolus injection as it is less effective compared to periodic or constant drug infusions.

<a id='39e5e205-5bd6-488e-baf3-5ff3eeab93c9'></a>

## 7. Conclusion
The aim of this study was to investigate the outcome of the amalgamation of chemotherapy and virotherapy in treating cancer using three different drug infusion methods and to compare the efficacy of using chemotherapy and virotherapy individually.

<a id='415c675f-d5e3-4ab5-8f2a-9092ae7af635'></a>

A mathematical model in the form of nonlinear and nonautonomous first-order ordinary differential equations was developed. It was extended into delay differential equations to account for delays as a result of the infection of tumor cells by the virus and chemotherapeutic drug responses. The model's well-posedness was shown by proving existence, positivity, and boundedness of the model solutions. Analysis of the model was done with each of the treatments and for each of the infusion functions. Exact solutions were determined where possible. Stability of the time invariant solutions was carried out to determine the conditions under which a tumor-free situation may be achieved. Numerical simulations for the ODE and DDE models were, respectively, carried out using ode23s and dde23 in MATLAB. The model analysis suggested the following:

<a id='8b8c8b93-6338-4455-bd03-e3fdf75fa811'></a>

(i) A tumor can grow to its maximum size in case where there is no treatment.
(ii) Chemotherapy alone is capable of clearing tumor cells in body tissue provided that the drug-induced lysis of the tumor and the drug infusion rate are maximized and the drug decay and tumor growth are minimized.
(iii) Constant and periodic drug infusions are more potent than a single bolus injection.
(iv) Successful virotherapy is highly dependent on virus burst size and infection rate.
(v) With the use of both chemotherapy and virother- apy, a tumor may be cleared from body tissue in less than a month.
(vi) Successful chemovirotherapy depends on the virus burst size and replication rate, chemotherapeutic drug lysis, infusion and decay rates, and the method of drug infusion.
(vii) Both the virus and chemotherapeutic response delays increase the period within which a tumor can be cleared from body tissue and thus treatment options should strive to minimize them by designing viruses and drugs which are highly responsive.

<a id='67c492b3-2d38-44ed-abc6-f1800c05c7ce'></a>

Appendix
A.1. Existence and Uniqueness

<a id='9b85eab9-360e-4e1f-ba92-503b780ec476'></a>

**Theorem 4.** *There exists a unique solution to the system of equation (5) in the region (U,I,V, C) ∈ R<sup>4</sup><sub>+</sub>.*

<a id='e3605d77-d3f2-4d44-93ac-41f50f20f6b3'></a>

Proof. The Picard-Lindel&ouml;f theorem [45] is used as
follows.

<!-- PAGE BREAK -->

<a id='5fe811c8-ecb6-47f5-9672-ce628588c0e6'></a>

12

<a id='eb32157f-4d07-4976-816b-a147092d8617'></a>

Computational and Mathematical Methods in Medicine

<a id='fa4d0794-8165-49df-86a5-cf4dfe59e94d'></a>

Consider the closed interval $I_{T}=[t_{0}-T,t_{0}+T]$ and the closed ball $B_{d}=\{y\in\mathbb{R}^{n}|\|y-x_{0}\|\le d\}$ in $\mathbb{R}^{n}$ where $T$ and $d$ are positive, real numbers. Suppose that the function
$f:I_{T}\times B_{d}\longrightarrow\mathbb{R}^{n}$, (A.1)

<a id='5ad24117-8be8-4827-9679-5616ac5d93ec'></a>

is continuous and that the partial derivatives in the Jacobian matrix $D_f$ where

$D_f = \begin{pmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_n}{\partial x_1} & \frac{\partial f_n}{\partial x_2} & \cdots & \frac{\partial f_n}{\partial x_n}
\end{pmatrix}, \quad (A.2)$

<a id='e5825422-4a9b-46a5-aad6-9b6155649bc0'></a>

exist and are continuous in $I_T \times B_d$. Then, there exists a $\delta > 0$
so that the initial value problem

<a id='dd10a962-044e-404d-b5de-775aee116fbd'></a>

dx/dt (t) = f (t, x),
x(t0) = x0,

(A.3)

<a id='d114dde8-91b8-4bb3-b6ed-f31415127d39'></a>

has a unique solution on the interval Iδ = [t₀ - δ, t₀ + δ]. It is sufficient to show that

<::
f = ⎛
⎜
f₁ := αU(t)(1 - U(t) - I(t)) - βU(t)V(t) - δ₀U(t)C(t)

f₂ := βU(t)V(t) - δI(t) - δ₁I(t)C(t)

f₃ := bI(t) - βU(t)V(t) - γV(t)

f₄ := ξ(t) - ψC(t)
⎝
(A.4)
: figure::>

<a id='66a48df9-161a-486b-bbc5-4770ae6f743e'></a>

D_f =
<::
$$
D_f = \begin{pmatrix}
\frac{\partial f_1}{\partial U} & \frac{\partial f_1}{\partial I} & \frac{\partial f_1}{\partial V} & \frac{\partial f_1}{\partial C} \\
\frac{\partial f_2}{\partial U} & \frac{\partial f_2}{\partial I} & \frac{\partial f_2}{\partial V} & \frac{\partial f_2}{\partial C} \\
\frac{\partial f_3}{\partial U} & \frac{\partial f_3}{\partial I} & \frac{\partial f_3}{\partial V} & \frac{\partial f_3}{\partial C} \\
\frac{\partial f_4}{\partial U} & \frac{\partial f_4}{\partial I} & \frac{\partial f_4}{\partial V} & \frac{\partial f_4}{\partial C}
\end{pmatrix}
$$
: figure::>

<a id='4bfe5128-67a0-43f5-bc80-dccee85a7c20'></a>

exist and are continuous on R⁴₊. The functions (A.4)
and (A.5) are polynomials and are therefore continuous
on R⁴. □

<a id='402f3de6-0437-4f94-be07-acd0df682e1c'></a>

## A.2. Boundedness and Positive Invariance

<a id='79a9fd6f-b959-43fd-8ca7-76c8b62a06a8'></a>

Theorem 5. if U (0) ≥ 0, I (0) ≥ 0, V (0) ≥ 0, and C (0) ≥ 0,
then U (t) ≥ 0, I (t) ≥ 0, V (t) ≥ 0, and C (t) ≥ 0 for all t ≥ 0.

<a id='7bc2bfaf-d794-4f3d-8f06-62780007889f'></a>

The same idea as in [10] is used to prove positiveness of the model solutions.

<a id='c43a475b-1b09-4199-b5e3-a3ad1f2b5431'></a>

*Proof.* Assuming that the Theory is not true, then there must be a time $t_1$ such that at least one of the solutions becomes zero first. Each possible case is investigated; if $U(t_1) = 0$ first, then $\dot{U}(t_1) = 0$. However, from the first equation in system (5), by the uniqueness of the solution, we know that $U(t) = 0$ for all $t \ge t_1$. The second equation then becomes $\dot{I}(t) = -I(t) - \delta I(t)C(t)$ and its solution is

<a id='5578154f-ed4e-4895-a032-36be0aed882f'></a>

$$I(t) = I(t_1)\exp\left(-\int_{t_1}^{t} (1 + \delta_1 C(s))ds\right), I(t) \geq 0. \tag{A.6}$$

<a id='cb1f59bf-25d6-4668-9dc2-7c02771e1b00'></a>

The third equation becomes V̇ (t) = bI (t) - γV (t). If you

<a id='d110c73c-3e04-4555-9968-edc324a92788'></a>

set
$\dot{V}(t) = bI(t) - \gamma = 0 \geq -\gamma V(t)$ so $V(t) \geq V(t_1)exp(-\gamma t)$,
$V(t) \geq 0$.

<a id='88a58bce-0daa-4e55-a71a-d7f444503c8f'></a>

Similarly, the fourth equation becomes Ċ = ξ (t) – ψC (t)

(A.7)

and its solution is

<a id='efee2cf7-7eda-46fe-bf31-9b2b5d1fa096'></a>

$$C(t) = \exp(-\psi t)\left(\int_{t_1}^{t} \phi(s)\exp(\psi s)ds + C(t_1)\right), \quad (A.8)$$

<a id='6f450805-1ca5-4544-a668-1681bcbbcadc'></a>

which implies that C(t) ≥ 0 for all t ≥ 0.
If I(t₁) = 0 first, then İ(t₁) = βU(t₁)V(t₁) ≥ 0, implying
that when t>t₁, I(t)≥0 since U(t), V(t), C(t) ≥0 as
assumed.

<a id='6dd44e0a-80d6-4392-a7ee-c60602277754'></a>

If $V(t_{1})=0$ first, $\dot{V}(t_{1})=by(t_{1})\ge0$, implying that when $t\ge t_{1}$, $V(t)\ge0$ since $U(t)$, $I(t)$, $C(t)\ge0$ as assumed.
If $C(t_{1})=0$ first, $\dot{C}(t_{1})=\phi(t_{1})\ge0$, so when $t\ge t_{1}$, $C(t)\ge0$ since $U(t)$, $I(t)$, $C(t)\ge0$ as assumed.

<a id='b3f53b70-ef8a-4f89-872c-1d549022bf95'></a>

If two solutions are zero (eg., U(t_1) = 0 and I(t_1) = 0)
simultaneously at t = t_1, then following the same steps
above, it is trivial to check that the other solutions will be
nonnegative for t > t_1.

<a id='e1c2f9dc-0bb3-4d9e-8077-acfff4c564e6'></a>

If three solutions are zero (eg., U (t₁) = 0, I (t₁) = 0, and
V (t₁) = 0) simultaneously at t = t₁, it is trivial to check that
the other solution will be nonnegative for t>t₁.

<a id='81862502-9d93-4ae0-b8fa-2f17faa800e0'></a>

If the four solutions are zero simultaneously at $t=t_1$,
from the uniqueness theorem, $U(t)=I(t)=V(t)=C(t)=$
0 for $t>t_1$. □

<a id='7ffee97e-9c1d-4fd2-b0a1-7d8f5e8fd96d'></a>

Theorem 6. The trajectories evolve in an attracting region
D = {(U, I, V, C) ∈ R⁴ | U(t) + I(t) ≤ 1, V(t) ≤ (b/γ), C(t) ≤ C(φ)}, where C(φ) depends on the drug infusion function
used.

<a id='f51d1282-563c-4dc7-8772-7df700aa0477'></a>

(A.5)

<!-- PAGE BREAK -->

<a id='5208f0f3-6f04-4d1a-8429-bbbf92627f0e'></a>

Computational and Mathematical Methods in Medicine

<a id='176d383b-7c54-4eca-9f64-6d0e0793f7bd'></a>

13

<a id='c34c99b9-2855-47d0-81a6-cedaf86bdd03'></a>

<::Figure: A set of six line graphs arranged in three rows, labeled (a), (b), and (c). Each row contains two graphs side-by-side. All graphs share the same axes and legends. The y-axis is labeled "Fractional tumor cell concentrations" and ranges from 0 to 1. The x-axis is labeled "Time" and ranges from 0 to 5. Each graph displays two lines: "Uninfected tumor" (represented by red circles connected by a solid line) and "Infected tumor" (represented by black asterisks connected by a dashed line).

(a) Top row:
  Left graph: The 'Uninfected tumor' line starts at 1, gradually decreases, and sharply drops to 0 around Time = 2. The 'Infected tumor' line starts near 0.1, peaks around 0.15 at Time = 1.5, and then decreases to 0 by Time = 3.
  Right graph: The 'Uninfected tumor' line starts at 1 and rapidly decreases to 0 by Time = 0.5. The 'Infected tumor' line starts near 0.1, sharply increases to a peak around 0.5 at Time = 0.7, and then gradually decreases to 0 by Time = 5.

(b) Middle row:
  Left graph: The 'Uninfected tumor' line starts at 1, gradually decreases, and sharply drops to 0 around Time = 1.8. The 'Infected tumor' line starts near 0.1, peaks around 0.5 at Time = 1.8, and then gradually decreases to near 0.1 by Time = 5.
  Right graph: The 'Uninfected tumor' line starts at 1 and rapidly decreases to 0 by Time = 0.5. The 'Infected tumor' line starts near 0.1, sharply increases to a peak around 0.7 at Time = 0.6, and then gradually decreases to 0 by Time = 5.

(c) Bottom row:
  Left graph: The 'Uninfected tumor' line starts at 1, gradually decreases, and sharply drops to 0 around Time = 1.9. The 'Infected tumor' line starts near 0.1, peaks around 0.4 at Time = 1.9, and then gradually decreases to near 0.1 by Time = 5.
  Right graph: The 'Uninfected tumor' line starts at 1 and rapidly decreases to 0 by Time = 0.5. The 'Infected tumor' line starts near 0.1, sharply increases to a peak around 0.7 at Time = 0.6, and then gradually decreases to 0 by Time = 5.::>

<a id='ea95eabc-d777-48b0-a77e-cda780d49f5f'></a>

FIGURE 3: Solutions of model (3) with both treatments showing a variation of fractional concentrations with time using high and low virus burst sizes, that is, b = 2 and b = 5 and with different drug infusion functions, that is, (a) constant, (b) exponential, and (c) sinusoidal.

<!-- PAGE BREAK -->

<a id='13b7f6af-acd0-4c67-9069-7cc1f5f52892'></a>

14

<a id='79fc7a5b-de04-41d2-9977-a6c4ff28bb9a'></a>

Computational and Mathematical Methods in Medicine

<a id='abd83fb2-c0b5-4e7f-bb95-f26941dda715'></a>

<::Four line charts showing fractional cell concentrations versus time: chart::>FIGURE 4: Solutions of delay model (15) showing a variation of fractional concentrations with time using (a) τ₁ = 0.001, τ₂ = 0.1; (b) τ₁ = 0.01, τ₂ = 0.1; (c) τ₁ = 0.001, τ₂ = 0.001; and (d) τ₁ = 0.001, τ₂ = 0.3. Each chart has 'Fractional cell concentrations' on the y-axis (ranging from 0 to 1) and 'Time' on the x-axis. A legend indicates 'Uninfected tumor' (red line with circle markers) and 'Infected tumor' (black dashed line with asterisk markers). (a) X-axis from 0 to 4. The red line starts at ~0.8 and decreases rapidly, then slowly, towards zero. The black line starts at ~0.1, peaks at ~0.25 around time 0.75, then decreases towards zero. (b) X-axis from 0 to 5. The red line starts at ~0.8 and decreases rapidly, then slowly, towards zero. The black line starts at ~0.1, peaks at ~0.3 around time 1.0, then decreases towards zero. (c) X-axis from 0 to 5. The red line starts at ~0.8 and decreases rapidly, then slowly, towards zero. The black line starts at ~0.1, peaks at ~0.25 around time 0.75, then decreases towards zero. (d) X-axis from 0 to 5. The red line starts at ~0.8 and decreases rapidly, then slowly, towards zero. The black line starts at ~0.1, peaks at ~0.3 around time 1.25, then decreases towards zero.

<a id='a9786355-5fed-43be-ac70-149962cfbf8b'></a>

<::chart: Two plots showing fractional cell concentrations over time. Both plots share the y-axis label "Fractional cell concentrations" (ranging from 0 to 1) and the x-axis label "Time" (ranging from 0 to 0.1). Each plot contains two lines: a red line with circles representing "Uninfected tumor" and a black line with asterisks representing "Infected tumor". Both lines exhibit damped oscillations, with the uninfected tumor concentration generally decreasing and the infected tumor concentration generally increasing before stabilizing. The plots are labeled as (a) and (b).:chart::>

FIGURE 5: Close up images of Figures 4(c) and 4(d) showing oscillations in cell concentrations.

<!-- PAGE BREAK -->

<a id='9f74a00d-7bf1-4b93-a478-d155b610d195'></a>

15

<a id='a847733e-cd93-4351-86a0-ea1eef8f6e5f'></a>

Computational and Mathematical Methods in Medicine

<a id='ad87b775-bafa-485f-b501-bfa25ad4ef74'></a>

Proof. From equation (1), we know that $U + I \le K$. This implies that $U + I \le 1$.

$\dot{V}(t) \le bI(t) - \gamma V(t)$,

$\dot{V}(t) \le b - \gamma V(t)$,

$V(t) \le \frac{b}{\gamma} - \frac{V_0 \exp(-\gamma t)}{\gamma}$,

$\lim_{t \to \infty} V(t) \le \frac{b}{\gamma}$, (A.9)

$\dot{C}(t) + \psi C(t) = \xi(t)$,

<a id='27a017ba-e4ba-409b-a12e-25aa0c5e844d'></a>

C(t) = exp(-ψt)(∫ξ(t)exp(ψt)dt + R),

<a id='ba6792d0-06a3-497d-a513-d2d272b397d0'></a>

where $R$ is an arbitrary constant of integration. For the
constant infusion function $\phi$, $\lim_{t\to\infty}C(t) = \phi/\psi$. For
$\xi(t) = \phi e^{-at}$, $\lim_{t\to\infty}C(t) = 0$, and for $\xi(t) = \phi \sin^2 (at)$,
$\lim_{t\to\infty}C(t) = (\psi + 2a/(4a^2 + \psi^2)) - (\phi/\psi)$. \u25A1

<a id='2a611e88-d452-4873-a7ce-c955caa44b07'></a>

**Theorem 7.** *The domain D is positive invariant for the model equation (5) and therefore biologically meaningful for the tumor, virus, and drug cell concentrations.*

<a id='c2787df7-9cfa-41e5-9ad9-106a9eef8539'></a>

_Proof._ The proof directly follows from proofs of Theorems 5 and 6. □

<a id='21632936-2073-480f-9e3d-7049fb2df015'></a>

## Data Availability
The data used to support the findings of this study are available from the corresponding author upon request.

<a id='36f0272b-6272-4bc4-bade-52d87d9bae82'></a>

**Conflicts of Interest**
The author declares that there are no conflicts of interest.

<a id='c6f18132-eae3-4086-819a-9631d7eecfa9'></a>

# Acknowledgments

This work was partially funded by the University of Kwa-zulu-Natal and the University of Eswatini.

<a id='1ddb113a-fc55-44ec-8131-70d1e13e943a'></a>

# References
1. V. Groh, J. Wu, C. Yee, and T. Spies, "Tumour-derived soluble MIC ligands impair expression of NKG2D and T-cell activation," *Nature*, vol. 419, no. 6908, pp. 734-738, 2002.
2. M. I. S. Costa, J. L. Boldrini, and R. C. Bassanezi, "Optimal chemotherapy: a case study with drug resistance, saturation effect, and toxicity," *Mathematical Medicine and Biology*, vol. 11, no. 1, pp. 45-59, 1994.
3. World Health Organization, "Cancer report," 2014, http://www.bmj.com/content/348/bmj.g1338/.
4. R. B. Mokhtari, T. S. Homayouni, N. Baluch et al., "Combination therapy in combating cancer," *Oncotarget*, vol. 8, no. 23, pp. 38022-38043, 2017.
5. M. V. Blagosklonny, "Overcoming limitations of natural anticancer drugs by combining with artificial agents," *Trends in Pharmacological Sciences*, vol. 26, no. 2, pp. 77-81, 2005.

<a id='b3f9afc3-75ee-40b0-ae1a-a2330eb93277'></a>

[6] E. Kelly and S. J. Russell, "History of oncolytic viruses: genesis to genetic engineering," Molecular Therapy, vol. 15, no. 4, pp. 651-659, 2007.
[7] S. J. Russel, K. W. Pengl, and J. C. Bell, "Oncolytic virotherapy," Nature Biotechnology, vol. 30, no. 7, pp. 658-670, 2012.
[8] D. Wodarz, "Viruses as antitumor weapons: defining conditions for tumor remission," Cancer Research, vol. 61, no. 8, pp. 3501-3507, 2001.
[9] T. C. Liau, E. Galanis, and D. Kirn, "Clinical trial results with oncolytic virotherapy: a century of promise, a decade of progress," Nature Clinical Practice Oncology, vol. 4, no. 2, pp. 101-117, 2007.
[10] J. Tian, "The replicability of oncolytic virus: defining conditions in tumor virotherapy," Mathematical Biosciences and Engineering, vol. 8, no. 3, pp. 841-860, 2011.
[11] J. Malinzi, P. Sibanda, and H. Mambili-Mamboundou, "Analysis of virotherapy in solid tumor invasion," Mathematical Biosciences, vol. 263, pp. 102-110, 2015.
[12] A. Nguyen, L. Ho, and Y. Wan, "Chemotherapy and oncolytic virotherapy: advanced tactics in the war against cancer," Frontiers in Oncology, vol. 4, pp. 1-10, 2014.
[13] P. K. Ottolino, J. S. Diallo, B. D. Lichty, J. C. Bell, and J. A. McCart, "Intelligent design: combination therapy with oncolytic viruses," Molecular Therapy, vol. 18, no. 2, pp. 251-263, 2010.
[14] M. J. Bartkowski, S. Bridges, P. E. Came et al., Chemotherapy of Viral Infections, P. E. Came and L. A. Caliguiri, Eds., Vol. 61, Springer Science & Business Media, Berlin, Germany, 2012.
[15] G. R. Simpson, K. Relph, K. Harrington, A. Melcher, and H. Pandha, "Cancer immunotherapy via combining oncolytic virotherapy with chemotherapy: recent advances," Oncolytic Virotherapy, vol. 5, pp. 1-13, 2016.
[16] G. Ungerechts, M. E. Frenzke, K.-C. Yaiw, T. Miest, P. B. Johnston, and R. Cattaneo, "Mantle cell lymphoma salvage regimen: synergy between a reprogrammed oncolytic virus and two chemotherapeutics," Gene Therapy, vol. 17, no. 12, pp. 1506-1516, 2010.
[17] I. V. Ulasov, A. M. Sonabend, S. Nandi, A. Khramtsov, Y. Han, and M. S. Lesniak, "Combination of adenoviral virotherapy and temozolomide chemotherapy eradicates malignant glioma through autophagic and apoptotic cell death in vivo," British Journal of Cancer, vol. 100, no. 7, pp. 1154-1164, 2009.
[18] M. M. Alonso, C. Gomez-Manzano, H. Jiang et al., "Combination of the oncolytic adenovirus ICOVIR-5 with chemotherapy provides enhanced anti-glioma effect in vivo," Cancer Gene Therapy, vol. 14, no. 8, pp. 756-761, 2007.
[19] J. Malinzi, A. Eladdadi, and P. Sibanda, "Modelling the spatiotemporal dynamics of chemovirotherapy cancer treatment," Journal of Biological Dynamics, vol. 11, no. 1, pp. 244-274, 2017.
[20] J. Malinzi, R. Ouifki, D. F. M. Torres et al., "Enhancement of chemotherapy using oncolytic virotherapy: mathematical and optimal control analysis," Mathematical Biosciences & Engineering, vol. 15, no. 6, pp. 1435-1463, 2018.
[21] M. G. Gopisankar and A. Surendiran, "Oncolytic virotherapy-a novel strategy for cancer therapy," Egyptian Journal of Medical Human Genetics, vol. 19, no. 3, pp. 165-169, 2018.
[22] L. Aurelian, "Oncolytic virotherapy: the questions and the promise," Oncolytic Virotherapy, vol. 2, pp. 19-29, 2013.
[23] S. T. R. Pinho, D. S. Rodrigues, and P. F. A. Mancera, "A mathematical model of chemotherapy response to tumor

<!-- PAGE BREAK -->

<a id='85c0c426-9d42-4c75-ba49-f6bfed046ecb'></a>

16

<a id='3e6ace79-6d9e-49be-8c0b-56875c59c6cd'></a>

Computational and Mathematical Methods in Medicine

<a id='c035ba65-21d7-4d03-8445-da7724b975f4'></a>

growth," Canadian Applied Mathematics Quarterly, vol. 4,
no. 19, pp. 369–384, 2011.
[24] Y. Wang, J. P. Tian, and J. Wei, "Lytic cycle: a defining process
in oncolytic virotherapy," Applied Mathematical Modelling,
vol. 37, no. 8, pp. 5962–5978, 2013.
[25] A. S. Novozhilov, F. S. Berezovskaya, E. V. Koonin, and
G. P. Karev, "Mathematical modelling of tumor therapy with
oncolytic viruses: regimes with complete tumor elimination
within the framework of deterministic models," Biology Di-
rect, vol. 1, no. 1, p. 6, 2006.
[26] M. Agarwal and A. S. Bhadauria, "Mathematical modeling
and analysis of tumor therapy with oncolytic virus," Applied
Mathematics, vol. 2, no. 1, pp. 131–140, 2011.
[27] L. de Pillis, K. R. Fister, W. Gu et al., "Mathematical model
creation for cancer chemo-immunotherapy," Computational
and Mathematical Methods in Medicine, vol. 10, no. 3,
pp. 165–184, 2009.
[28] W. Liu and H. I. Freedman, "A mathematical model of
vascular tumor treatment by chemotherapy," Mathematical
and Computer Modelling, vol. 42, no. 9–10, pp. 1089–1112,
2005.
[29] S. T. R. Pinho, H. I. Freedman, and F. Nani, "A chemotherapy
model for the treatment of cancer with metastasis," Mathe-
matical and Computer Modelling, vol. 36, no. 7–8, pp. 773–
803, 2002.
[30] J. R. Ursher, "Some mathematical models for cancer che-
motherapy," Computers & Mathematics with Applications,
vol. 28, no. 9, pp. 73–80, 1994.
[31] R. W. Carlson and B. I. Sikic, "Continuous infusion or bolus
injection in cancer chemotherapy," Annals of Internal Med-
icine, vol. 99, no. 6, pp. 823–833, 1983.
[32] M. Yoshimori, H. Ookura, Y. Shimada et al., "Continuous
infusion of anti-cancer drug with balloon infusor," Cancer
and Chemotherapy, vol. 15, no. 11, pp. 3121–3125, 1988.
[33] G. J. Bostol and S. Patil, "Carboplatin in clinical stage I
seminoma: too much and too little at the same time," Clinical
Oncology, vol. 29, no. 8, pp. 949–952, 2011.
[34] R. T. D. Oliver, G. M. Mead, G. J. S. Rustin et al., "Randomized
trial of carboplatin versus radiotherapy for stage I seminoma:
mature results on relapse and contralateral testis cancer rates
in MRC TE19/EORTC 30982 study (ISRCTN27163214),"
Journal of Clinical Oncology, vol. 29, no. 8, pp. 957–962, 2011.
[35] M. Bertau, E. Mosekilde, and H. V. Westerhoff, Biosimulation
in Drug Development, John Wiley & Sons, Hoboken, NJ, USA,
2008.
[36] S. D. Undevia, G. Gomez-Abuin, and M. J. Ratain, "Phar-
macokinetic variability of anticancer agents," Nature Reviews
Cancer, vol. 5, no. 6, pp. 447–458, 2005.
[37] B. L. Carey, M. Ahmed, S. Puckett, and D. S. Lyles, "Early steps
of the virus replication cycle are inhibited in prostate cancer
cells resistant to oncolytic vesicular stomatitis virus," Journal
of Virology, vol. 82, no. 24, pp. 12104–12115, 2008.
[38] B. J. Martin, P. R. Twentyman, and S. S. Zamvil, "Response to
the RIF-1 tumor in vitro and in C3H/Km mice to X-radiation
(cell survival, regrowth delay, and tumor control), chemo-
therapeutic agents, and activated macrophages," Journal of the
National Cancer Institute, vol. 64, no. 3, pp. 605–611, 1980.
[39] R. Seiler, "Delayed response to brain tumor chemotherapy,"
Surgical Neurology, vol. 11, no. 2, pp. 97–100, 1979.
[40] S. Wiggins, Introduction to Non-Linear Dynamical Systems
and Chaos, Springer Science & Business Media, New York,
NY, USA, 2003.
[41] Ž. Bajzer, T. Carr, K. Josić, S. J. Russell, and D. Dingli,
"Modeling of cancer virotherapy with recombinant measles

<a id='7e4b12e3-df94-4678-90fd-fc9394084e30'></a>

viruses," *Journal of Theoretical Biology*, vol. 252, no. 1, pp. 109-122, 2008.
[42] T. D. Brock, "The emergence of bacterial genetics," in *Cold Spring Harbor*, Cold Spring Harbor Laboratory Press, New York, NY, USA, 1990.
[43] S. Pam, "Breast cancer treatment and recovery times based on diagnosis," 2015, http://breastcancer.about.com/od/whattoexpect/a/Breast-Cancer-Treatment-Recovery-Times_2.htm.
[44] D. Wodarz and V. A. A. Jansen, "A dynamical perspective of CTL cross-priming and regulation: implications for cancer immunology," *Immunology Letters*, vol. 86, no. 3, pp. 213-227, 2003.
[45] B. J. Schroers, *Ordinary Differential Equations: A Practical Guide*, Cambridge University Press, Cambridge, UK, 2011.
PROCEEDINGS B <!-- text, from page 0 (l=0.063,t=0.044,r=0.326,b=0.075), with ID aca06709-1a54-460c-aed3-77b72fedc70c -->

royalsocietypublishing.org/journal/rspb <!-- text, from page 0 (l=0.066,t=0.094,r=0.321,b=0.117), with ID 424c0664-7bf9-4e09-b9ae-d7e9f74c1821 -->

Research

logo: open access

logo: Check for updates

Cite this article: Kimmel GJ, Locke FL, Altrock PM. 2021 The roles of T cell competition and stochastic extinction events in chimeric antigen receptor T cell therapy. Proc. R. Soc. B 288: 20210229.
https://doi.org/10.1098/rspb.2021.0229 <!-- text, from page 0 (l=0.065,t=0.149,r=0.324,b=0.305), with ID d048f472-a049-457b-a2cc-5ef8f9152a00 -->

Received: 28 January 2021  
Accepted: 2 March 2021 <!-- text, from page 0 (l=0.067,t=0.343,r=0.217,b=0.381), with ID e702b390-9d96-4b33-aa6e-f18ffb0ec8ef -->

Subject Category:
Ecology <!-- text, from page 0 (l=0.067,t=0.426,r=0.179,b=0.462), with ID 4525ce1a-17ca-4924-91fa-2f97222307c3 -->

Subject Areas:
theoretical biology, ecology, immunology <!-- text, from page 0 (l=0.068,t=0.475,r=0.293,b=0.511), with ID a281f278-fbcb-4435-ba4d-8eec8d46f268 -->

Keywords:
cellular immunotherapy, predator–prey dynamics, CAR T cells, stochastic process <!-- text, from page 0 (l=0.068,t=0.523,r=0.291,b=0.575), with ID 9942d138-32f0-4f29-b3c8-88eb23684eb7 -->

Authors for correspondence:
Frederick L. Locke
e-mail: frederick.locke@moffitt.org
Philipp M. Altrock
e-mail: philipp.altrock@gmail.com <!-- text, from page 0 (l=0.067,t=0.608,r=0.255,b=0.693), with ID 5143df19-eeef-44bf-b16c-9a1308297729 -->

†These authors contributed equally to the
study. <!-- text, from page 0 (l=0.068,t=0.808,r=0.298,b=0.844), with ID cfedc051-b191-4fa8-9b8a-cf8cf79ee11a -->

Electronic supplementary material is available  
online at https://doi.org/10.6084/m9.figshare.  
c.5345003. <!-- text, from page 0 (l=0.068,t=0.859,r=0.317,b=0.910), with ID afcd19d7-d386-4df4-beeb-ac4a6565e07c -->

THE ROYAL SOCIETY  
PUBLISHING <!-- marginalia, from page 0 (l=0.067,t=0.926,r=0.319,b=0.958), with ID d46613c0-7c9a-4922-9b80-8915716d0a6c -->

The roles of T cell competition and stochastic extinction events in chimeric antigen receptor T cell therapy <!-- text, from page 0 (l=0.400,t=0.045,r=0.907,b=0.144), with ID 1d5022de-e475-4870-a6d1-774135c22170 -->

Gregory J. Kimmel¹, Frederick L. Locke²,† and Philipp M. Altrock¹,²,³,† <!-- text, from page 0 (l=0.404,t=0.156,r=0.888,b=0.179), with ID 27aa7425-d689-4fef-8b6f-c33fcc01bc53 -->

¹Department of Integrated Mathematical Oncology, ²Department of Blood and Marrow Transplant and Cellular Immunotherapy, and ³Department of Malignant Hematology, H. Lee Moffitt Cancer Center and Research Institute, Tampa, FL, USA <!-- text, from page 0 (l=0.402,t=0.186,r=0.931,b=0.228), with ID 661d60fb-57ff-4876-8991-6ff08331a1a6 -->

logo: ORCID

GJK, 0000-0001-9766-5399; PMA, 0000-0001-7731-3345 <!-- text, from page 0 (l=0.402,t=0.231,r=0.697,b=0.250), with ID 7105b387-4497-43c6-a553-7e4228e070a2 -->

Chimeric antigen receptor (CAR) T cell therapy is a remarkably effective
immunotherapy that relies on in vivo expansion of engineered CAR T cells,
after lymphodepletion (LD) by chemotherapy. The quantitative laws under-
lying this expansion and subsequent tumour eradication remain unknown.
We develop a mathematical model of T cell–tumour cell interactions and
demonstrate that expansion can be explained by immune reconstitution
dynamics after LD and competition among T cells. CAR T cells rapidly
grow and engage tumour cells but experience an emerging growth rate dis-
advantage compared to normal T cells. Since tumour eradication is
deterministically unstable in our model, we define cure as a stochastic event,
which, even when likely, can occur at variable times. However, we show
that variability in timing is largely determined by patient variability. While
cure events impacted by these fluctuations occur early and are narrowly dis-
tributed, progression events occur late and are more widely distributed in
time. We parameterized our model using population-level CAR T cell and
tumour data over time and compare our predictions with progression-free sur-
vival rates. We find that therapy could be improved by optimizing the tumour-
killing rate and the CAR T cells’ ability to adapt, as quantified by their carrying
capacity. Our tumour extinction model can be leveraged to examine why
therapy works in some patients but not others, and to better understand the
interplay of deterministic and stochastic effects on outcomes. For example,
our model implies that LD before a second CAR T injection is necessary. <!-- text, from page 0 (l=0.407,t=0.259,r=0.929,b=0.580), with ID 9c9556d2-b2db-4ac3-9089-8c9c7ff2180f -->

1. Introduction  
In 2017, non-Hodgkin lymphoma was the most common haematologic malignancy in the US with 72 000 new cases (4.3% of all cancer) and 20 000 deaths (3.4% of all cancer deaths) [1]. Large B cell lymphoma (LBCL) is the most common subtype of non-Hodgkin lymphoma. LBCL arises in the B cell lineage for which the transmembrane protein CD19 is a specific marker. Historically, LBCL patients that did not respond to chemotherapy have a median overall survival of under seven months [2]. These patients could benefit from autologous chimeric antigen receptor (CAR) T cell therapy that uses genetically engineered T cells specifically re-targeted to CD19 [3]. A pivotal, multi-centre, phase 1–2 trial of the CAR T cell drug axicabtagene ciloleucel (axi-cel; n = 101 patients treated) was ZUMA-1 [4,5]. Overall response rate and complete response rate in ZUMA-1 were 82% and 54%. The respective responses to standard chemotherapy are 26% and 7% [2]. While many LBCL patients treated with this cellular therapy have seen a temporary reduction in tumour burden, about 60% eventually progress. A complete understanding of why these patients progress is lacking. <!-- text, from page 0 (l=0.402,t=0.623,r=0.932,b=0.858), with ID d2f7eb88-2cfd-4ea0-8978-ce59d4044354 -->

Cellular immunotherapies, such as CAR T cell therapy, encompass a new
frontier for predictive mathematical biological modelling [6–9]. One of the <!-- text, from page 0 (l=0.403,t=0.860,r=0.932,b=0.890), with ID 093a1395-a61a-4b2d-81e3-e68a9dada1ea -->

© 2021 The Authors. Published by the Royal Society under the terms of the Creative Commons Attribution License http://creativecommons.org/licenses/by/4.0/, which permits unrestricted use, provided the original author and source are credited. <!-- text, from page 0 (l=0.405,t=0.908,r=0.929,b=0.954), with ID 50695ed2-7042-4363-b798-c66ed76380ab -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.000,t=0.296,r=0.030,b=0.701), with ID 0aa8da89-ee04-40e8-8489-a6d21642754a -->

first goals of this new field is to describe and predict CAR T
cell expansion and decay after administration. Recent works
used an empirical time-dependent modelling approach and
compartment modelling [6] to describe the complicated tem-
poral kinetics of the CAR T cell drug tisagenlecleucel [10].
Others sought to quantify ecological dynamics of CAR T
cells to explain expansion and exhaustion [8], and signal-
ling-induced cell state variability [9], both using in vitro
data. Current modelling has not considered interactions
between CAR and normal T cells, nor paid much attention
to feedback between tumour and CAR T cells [11-13]. <!-- text, from page 0 (l=0.065,t=0.044,r=0.483,b=0.203), with ID 7c672a3f-39f6-4557-9845-40a6f3f0ba32 -->

Here, we seek to better understand T and CAR T cell
dynamics, and the resulting tumour cell dynamics in vivo
using mathematical modelling. We bin the potentially differ-
ent CAR T cell phenotypes together [14,15], and model
selection in the T cell homeostatic niche by including
normal T cells. Tumour dynamics can be stochastic due to
low cell counts. Our framework explains the overall CAR kin-
etics and reveals that stochastic dynamics in small tumours
match clinical progression. <!-- text, from page 0 (l=0.066,t=0.204,r=0.482,b=0.334), with ID ec1e891d-1609-49ec-bd9e-3e0f698e6666 -->

## 2. Methods
We model dynamics and interactions among normal T cells, CAR T cells and tumour cells. The model considers three cell populations in the form of continuous-time birth and death stochastic processes and their deterministic mean-field equations: normal T cells, *N*, CAR T cells, *C*, both given in cells μl⁻¹, and antigen-presenting tumour cells, *B*, given in ml. These measurements can be converted to cell counts. A more detailed overview of the methods can be found in the electronic supplementary material, sections 1 and 2. <!-- text, from page 0 (l=0.067,t=0.359,r=0.481,b=0.501), with ID 64992745-c167-4e3a-95ab-1793a4514af0 -->

We define the following two scenarios. Complete response
(CR) is achieved when the tumour is eradicated. Progressive
disease (PD) is counted when the tumour has reached 120% of
its initial size. Note that the clinical definition of progression
typically is less quantitatively tractable [16], as clinical pro-
gression can occur whenever the disease worsens in relation to
its nadir size, which could be markedly less than the value at
baseline [17]. <!-- text, from page 0 (l=0.067,t=0.501,r=0.480,b=0.605), with ID 84fb8052-8099-4cc3-b0ac-33d5fb9b8a3a -->

We consider the case of lymphodepleting chemotherapy
prior to infusion of autologous CAR T cells. We set time to 0 at
the time of CAR infusion. Normal and CAR T cell populations
then grow towards their respective carrying capacities but influ-
ence each other. This mutual influence gives rise to selection. <!-- text, from page 0 (l=0.068,t=0.605,r=0.480,b=0.670), with ID c7c809c0-f95b-43a8-8f80-b426440a9e7a -->

We exclude possible influences by other sources of CD19, such as normal B cells, based on the following observations. Patients have effectively zero normal B cells following lympho-depleting chemotherapy and prior/concurrent to CAR T cell infusion. Furthermore, the reconstitution of normal B cells is extremely slow, such that only 50% of patients have recovered any normal B cells by 1 year after therapy. While it is possible that normal B cells activate CD19 directed CAR T cells, at this scale the dynamics of CAR T are probably not impacted by normal B cells. Thus, in the patient population we are interested in, normal sources of CD19 do not seem to play a significant role. Meanwhile, the tumour cell population $B$ grows autonomously at a net growth rate $r_B$ and experiences tumour killing at rate $\gamma_{B}$, proportional to the number of CAR T cells. <!-- text, from page 0 (l=0.068,t=0.670,r=0.479,b=0.852), with ID 96fbd9da-f9db-4f23-a17c-4b1d9040748b -->

These biological mechanisms could manifest themselves in
multiple ways in a mathematical model. A carrying capacity
for T cells could emerge due to predation, resource or spatial
limitations, birth and death rate balance through exogeneous
effects (e.g. paracrine signalling [18]), or any combination of
the above. We investigated different functional forms (a general-
ized logistic, Gompertz, and an explicit interaction model, <!-- text, from page 0 (l=0.068,t=0.853,r=0.479,b=0.946), with ID 3dfe90da-6d82-4ad9-b5a5-e31a8a741e75 -->

discussed in the electronic supplementary material, section 3).
Using an information criterion, we elected to use a Gompertz
model approach. The corresponding dynamical system in the
mean-field limit is <!-- text, from page 0 (l=0.521,t=0.046,r=0.931,b=0.101), with ID bb4030f8-1a00-49a9-8a5e-79a0b31cac87 -->

$
\frac{\mathrm{d}N}{\mathrm{d}t} = -r_N\, N \ln \left[ \frac{N + C}{K_N} \right], \tag{2.1}
$

$
\frac{\mathrm{d}C}{\mathrm{d}t} = -r_C(T)\, C \ln \left[ \frac{N + C}{K_C} \right] \tag{2.2}
$

$
\text{and} \qquad \frac{\mathrm{d}B}{\mathrm{d}t} = r_B B - \gamma_B\, B \frac{C}{k_B + C}. \tag{2.3}
$ <!-- text, from page 0 (l=0.522,t=0.106,r=0.931,b=0.192), with ID 508c647a-b126-4d08-8e4a-b81760fdb396 -->

Here $T = N + C$ is the total lymphocyte count, and $r_C(T) = \rho_C + b(T - K_N)^2 / (a / (T^2 + (T - K_N)^2))$, where $\rho_C$ is a background expansion rate and the second term reflects that growth can be muted when the overall (largely normal) T cell population reaches capacity, modulated by the two parameters $a$ and $b$. We introduced feedback of total lymphocyte count on CAR expansion because the CAR T cell population expands at a faster rate initially and contracts slower after peak, which has been a challenge in several of the recent quantitative modelling approaches [6,11]. A generalized logistic or Gompertz form cannot alone capture this behaviour. Thus, we chose to include additional feedback into the intrinsic growth rate function $\rho_C$, which becomes a function of the total T cell count $T$, the tumour mass $B$, or both (see electronic supplementary material, section 3). For a deeper discussion on the assumptions and details of the system of equations (2.1)-(2.3), which can be based on a stochastic birth and death process, see the electronic supplementary material, section 3, where we also present a linear stability analysis. Figure 1a shows a schematic of the dynamical system. Figure 1b shows the associated cellular events, which can be interpreted deterministically or stochastically. The deterministic system’s *qualitative* behaviour aligns with clinical observations (figure 1d–f). <!-- text, from page 0 (l=0.521,t=0.202,r=0.932,b=0.489), with ID 26153a58-3ab8-4958-8a27-d7aee1db431d -->

Tumour killing by CAR T cells is modelled as a result of contact, thus is proportional to $B \times C$ and includes a saturation factor, motivated by the assumption that there exists an upper limit at which CAR T cells can interact and kill the tumour cells. <!-- text, from page 0 (l=0.523,t=0.490,r=0.931,b=0.541), with ID 01d1392c-d53e-4517-9f92-b85b23d612e4 -->

Altogether, these assumptions lead to seven parameters to be
fitted by optimization, based on 11 data points from clinical
observations—five for CAR T and five for absolute lymphocyte
count (ALC), excluding the initial conditions, and one measure-
ment for the tumour state at day 30 (for further details see
electronic supplementary material, section 4). <!-- text, from page 0 (l=0.522,t=0.542,r=0.932,b=0.620), with ID 1b317730-168b-4f30-8536-3369b646832d -->

3. Results  
We calibrated the deterministic model using clinical data (figure 2a,b; electronic supplementary material, sections 2 and 4), which led to the parameters in table 1. To recapitulate and predict progression-free survival over time, we employed the corresponding stochastic formulation (electronic supplementary material, section 5), which is able to capture dynamics of small tumour populations near extinction. <!-- text, from page 0 (l=0.521,t=0.653,r=0.931,b=0.776), with ID 95e707bc-d809-4895-8b07-d52cd8304543 -->

(a) Parameter sensitivity and identifiability  
We conducted a local sensitivity and identifiability analysis  
[21–23] of the fitted parameters. The resulting ranking of  
parameters highlights that the carrying capacities of the CAR  
and normal T cells, respectively, and the maximal tumour-  
killing rate were most sensitive (figure 2c). Note here that low  
sensitivity of a parameter does not imply that the model is  
not sensitive to these parameters. We performed an identifi-  
ability analysis, with a threshold value of 0.9, to indicate  
non-identifiability between parameters pairs. Strong Pearson <!-- text, from page 0 (l=0.522,t=0.799,r=0.931,b=0.945), with ID d0525937-de6b-4cb3-a49c-067252d20f11 -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.001,t=0.299,r=0.030,b=0.700), with ID df814898-9b26-416b-97d3-a177356899f0 -->

2 <!-- marginalia, from page 0 (l=0.940,t=0.047,r=0.975,b=0.067), with ID e145281e-76dd-4103-bff5-8eaee72b1182 -->

royalsocietypublishing.org/journal/rspb

Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.946,t=0.077,r=0.976,b=0.375), with ID 0a52740d-f3d0-4b01-896c-dc77e81ae920 -->

Summary : This figure presents a mechanistic mathematical model of T cell, CAR T cell, and tumor cell dynamics, integrating experimental and clinical data to simulate and predict different response scenarios to CAR T cell therapy in cancer.

flowchart and multi-panel schematic:
# (a) Schematic of the Model :
  • Depicts three main cell populations: normal T cells (N, green), CAR T cells (C, blue), and CD19+ tumor cells (B, pink).
  • Arrows indicate interactions: normal T cell expansion, CAR T cell expansion, competition between T and CAR T cells, tumor killing by CAR T cells, and net tumor growth.

# (b) Individual Cellular Processes :
  • Lists four key processes with associated rates:
    – Normal T cell expansion: R_N(N, C)
    – CAR T cell expansion: R_C(N, C, B)
    – Tumor killing by CAR T cells: γ_B
    – Tumor growth: r_B
  • Visual icons represent each process (green, blue, and pink circles).

# (c) Data and Model Integration :
  • Flowchart showing integration of data and modeling:
    – Green box: T cell kinetics over time (lymphocyte counts, Moffitt patients with CAR T).
    – Blue box: CAR T cell kinetics (ZUMA-1, peripheral CAR at days 5, 14, 28, 90, 180).
    – Red box: Tumor size estimates (MTV, CR, PD).
    – Arrows lead to "mechanistic model formulation" and "model calibration," then to "simulate stochastic outcomes."

# (d–f) Model Kinetics: Simulated Response Scenarios :
  • Three line plots (d, e, f) show cell population size vs. time for three cell types:
    – Tumor cells (red line)
    – CAR T cells (blue line)
    – Normal T cells (green dashed line)
  • (d) No response: Tumor cells increase, CAR T cells decline, normal T cells plateau.
  • (e) Transient response: Tumor cells initially decrease, then regrow; CAR T cells peak then decline; normal T cells plateau.
  • (f) Long-term response: Tumor cells decrease and remain low; CAR T cells decline after initial peak; normal T cells plateau.

# Design Encodings :
  • Distinct colors for each cell type: green (normal T), blue (CAR T), red (tumor).
  • Solid and dashed lines differentiate cell types.
  • Schematic arrows and flowchart boxes use color-coding matching cell types.

# Analysis :
  • The model integrates experimental and clinical data to simulate T cell and tumor dynamics.
  • Three kinetic scenarios illustrate possible patient responses to CAR T therapy: no response, transient response, and long-term response.
  • The model highlights the importance of CAR T cell expansion and persistence for durable tumor control, and the competitive dynamics between normal and CAR T cells.
  • The flowchart demonstrates a systematic approach to model calibration and simulation using real patient data. <!-- figure, from page 0 (l=0.090,t=0.044,r=0.904,b=0.440), with ID 9f9604d3-bb82-446b-8e5c-dde1212b0d82 -->

Figure 1. Overview of cellular interactions, kinetics, data integration and qualitative dynamics. (a) Model schematic of three cell compartments: CAR T cells, $C$, proliferate and interact with resident (normal) lymphocytes, $N$ (depleted by lymphodepleting chemotherapy). CAR T cells also engage in killing CD19+ tumour and other $B$ cells. (b) The system can be described by four cellular kinetic reactions, with density-dependent feedback (differences in carrying capacities) in the net expansion rates: $R_X = r_X \ln(K_X/(N + C))$, where $X$ stands for $N$ or $C$. The deterministic, large population size limit of these dynamics is given by equations (2.1)–(2.3). (c) Schematic of data integration to parametrize the mathematical model; we used longitudinal data of peripheral absolute lymphocyte count (ALC), peripheral CAR+ cell counts per $\mu$L, and the tumour volume-changes as estimated from patients of the ZUMA-1 trial with complete response (CR) or progressive disease (PD). We assumed that, at days 30, 60 or 90, CRs had no detectable tumour mass, and that PDs had 1.2 times their initial tumour size. Median initial tumour mass was 94.86 ml. The qualitative dynamics of the system, given by equations (2.1)–(2.3): no response to CAR therapy (d), transient response followed by progression/relapse (e) and long-term response (tumour appears to be eradicated) (f). These illustrative examples are not to scale. <!-- text, from page 0 (l=0.067,t=0.441,r=0.932,b=0.574), with ID 756922ed-22e8-4046-942b-a0159b99fd9c -->

correlations between $k_B$ and $r_B$ (0.94), and between $k_B$ and $\gamma_B$ (–0.96) were observed (figure 2d inset), which suggests that these pairs are not identifiable. All other pairs were below the threshold and can be considered identifiable. The sensitivity ranking suggests that the most promising avenues to improve CAR T cell therapy should focus on improving adaptability (carrying capacity) and efficacy (tumour-killing rate) of the engineered CAR T cell product. <!-- text, from page 0 (l=0.067,t=0.607,r=0.480,b=0.723), with ID c06cc0f9-f949-4340-9370-5f31f97c4726 -->

(b) Immune reconstitution and return to homeostasis  
during chimeric antigen receptor T cell therapy  
follows a Gompertz growth law

We initially hypothesized that immune reconstitution follows a generalized logistic growth equation of the form $x'(t) = rx(1 - (x/k)^c)$ [24]. This approach contains the standard logistic model ($c = 1$) and leads to Gompertz growth in the limits $c \to 0$, $r \to \infty$. Our nonlinear optimization routine for data fitting (see electronic supplementary material, section 3) selected Gompertz as the best approach for immune reconstitution dynamics (figure 2a). The optimizer was selecting $r$ at the edge of the upper boundary of its optimization region, while selecting $c$ at the lowest possible (positive) value. We <!-- text, from page 0 (l=0.067,t=0.739,r=0.480,b=0.947), with ID 9778f4d8-dc03-413d-8fc9-ed96435243a2 -->

$x'(t) = -rx\ln[x/k]$ <!-- text, from page 0 (l=0.519,t=0.606,r=0.931,b=0.638), with ID cf34c6f8-652b-4512-99b1-3b79beb7066c -->

(c) Chimeric antigen receptor T cell kinetics can be explained by increased growth rate and lower carrying capacity

We hypothesized that CAR T cells become maladapted during the manufacturing process, lowering their carrying capacity. After lymphodepletion, a complex signalling cascade occurs that results in immune reconstitution towards homeostatic levels [19], driven by stem and progenitor cells [25,26]. Both normal T cells (figure 2a) and CAR T cells (figure 2b) use the changing environment to proliferate and expand, but only normal cells can be reconstituted from stem cells. Although we do not model these signals explicitly, the system’s behaviour can be observed through the interplay of the normal and CAR T cells. As a result, CAR T cells are outcompeted by normal T cells [27] in the long term, resulting in lower carrying capacity. An alternative hypothesis that could explain the kinetics would be predation of CAR T cells by normal T cells. We examined and ultimately discarded this alternative hypothesis <!-- text, from page 0 (l=0.520,t=0.669,r=0.932,b=0.945), with ID b1d1c7b9-e9ee-44a4-9db8-f0893345ca79 -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.001,t=0.299,r=0.029,b=0.701), with ID 79f5049b-6898-47fd-96b2-a1c6f66a3de3 -->

3 <!-- marginalia, from page 0 (l=0.939,t=0.047,r=0.976,b=0.068), with ID 4983d7cb-314c-4e2f-a9ba-e63eef3bb65d -->

royalsocietypublishing.org/journal/rspb  
Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.946,t=0.076,r=0.975,b=0.376), with ID 695c9058-1d78-4c1f-a3ef-ff15e957fc8f -->

Summary : This figure presents two panels: (a) a time-course plot of normal T cell dynamics in patients, comparing model fit to empirical data, and (c) a parameter sensitivity and correlation analysis for the model parameters.

line and scatter plots with heatmap inset:
# (a) Normal T cell dynamics
Title & Axes :
  • Title: "normal T cell dynamics"
  • X-axis: "time (days)", tick labels: 0, 50, 100, 150, 200
  • Y-axis: "normal T cell ml⁻¹", tick labels: 0, 100, 200, 300, 400, 500
Data Points :
  • Data (grey circles): (0, 0), (10, ~200), (20, ~350), (40, ~450), (100, ~500), (200, ~500)
  • Model fit (green solid line): rises steeply from (0, 0) to plateau near (50, 500)
  • Model equation: 𝑁̇ = r_N N ln [K_N / (N + C)]
Design Encodings :
  • Grey filled circles for data points
  • Green solid line for model fit
  • Legend: "model fit" (green line), "data" (grey circle)
  • Inset text: "medians from 55 patients; calculated from ALC, subtracting CAR"
Distribution & Trends :
  • Rapid initial increase in T cell count, plateauing near 500 normal T cells/ml after ~50 days

# (c) Parameter sensitivity and correlation
Title & Axes :
  • Title: "parameter sensitivity and correlation"
  • X-axis: "model parameter", labels: K_C, K_N, γ_B, r_N, k_B, ρ_C, a, r_B, b
  • Y-axis: "relative sensitivity", log scale, tick labels: 0.005, 0.010, 0.050, 0.100, 0.500, 1
Data Points :
  • Blue circles for each parameter, showing relative sensitivity values (exact y-values not specified)
Design Encodings :
  • Blue filled circles for sensitivity values
  • Logarithmic y-axis
  • Inset: heatmap matrix of parameter correlations, with green (positive), red (negative), and white (near zero) cells, values ranging from -0.14 to 0.14
  • Correlation matrix labels: r_N, ρ_C, k_C, K_N, k_B, γ_B, a, b, r_B
Distribution & Trends :
  • Sensitivity decreases from left (K_C) to right (b)
  • Correlation matrix shows most values near zero, with a few moderate positive/negative correlations

Analysis :
  • The model accurately fits the empirical T cell data, capturing the rapid rise and plateau in cell counts.
  • Parameter sensitivity analysis reveals that K_C and K_N are the most sensitive parameters, while b and r_B are least sensitive.
  • The parameter correlation matrix indicates generally low correlations, suggesting parameter identifiability, with a few moderate correlations (both positive and negative) between specific pairs. <!-- figure, from page 0 (l=0.099,t=0.043,r=0.886,b=0.241), with ID dd50134a-5bf0-44f9-9921-d16c0c40fc46 -->

Summary : This figure presents the dynamics of CAR T cell concentrations in blood over time, comparing a mathematical model fit to median patient data.

line plot:
Title & Axes :
  • Title: “CAR T cell dynamics” (panel label: (b)).
  • X-axis: “time (days)”, range: 0 to 200.
  • Y-axis: “CAR+ T cell ml⁻¹”, range: 0 to 40.
  • Tick marks: X-axis at 0, 50, 100, 150, 200; Y-axis at 0, 10, 20, 30, 40.

Data Points :
  • Data (grey circles): Median CAR+ T cell concentrations at approximately (0, 0.36), (5, ~35), (20, ~5), (50, ~2), (100, ~1), (200, ~0.5) cells ml⁻¹.
  • Model fit (blue line): Smooth curve peaking sharply near day 5, then declining rapidly and flattening toward zero by day 200.

Design Encodings :
  • Model fit: solid blue line.
  • Data: large grey filled circles.
  • Legend: “model fit” (blue line), “data” (grey circle).
  • Mathematical model equations shown on plot:
    - \(\hat{C} = r_C(N, C)C \ln\left[\frac{K_C}{N + C}\right]\)
    - \(r_C(N, C) = \rho_C + \frac{b(N + C - K_N)^2}{a(N + C)^2 + (N + C - K_N)^2}\)
  • Text box: “medians from 101 patients [5]; initial condition: 0.36 cells ml⁻¹ at t = 0”.

Distribution & Trends :
  • The CAR+ T cell count rises sharply to a peak near day 5, then declines rapidly, approaching a low steady value by day 200.
  • Data points closely follow the model fit.

Analysis :
  • The model accurately captures the rapid expansion and subsequent contraction of CAR+ T cells post-infusion, as observed in patient medians.
  • The initial condition and model equations are explicitly provided, supporting reproducibility.
  • The data show a pronounced early peak followed by a long, low plateau, indicating a transient expansion phase. <!-- figure, from page 0 (l=0.098,t=0.249,r=0.500,b=0.429), with ID 4fb60093-b2fb-4ce1-9314-c0002bcbad36 -->

Summary : This figure shows two possible outcomes (cure vs. progression) of CD19+ tumour cell counts over time after CAR infusion, using the same model parameters but different stochastic realizations.

line plot:
Title & Axes :
  • Title: "tumour dynamics: same parameters, different outcomes"
  • X-axis: "days post CAR infusion" (range: 0 to 180, ticks at 0, 30, 60, 90, 120, 150, 180)
  • Y-axis: "CD19+ tumour cell" (log scale, range: 10^0 to 10^12, ticks at 10^0, 10^2, 10^4, 10^6, 10^8, 10^10, 10^12)

Data Points :
  • Series 1 (solid red line, labeled "cure"): Tumour cell count decreases steeply from ~10^10 at day 0 to below 10^2 by day 60, then remains low.
  • Series 2 (dotted red line, labeled "progression"): Tumour cell count decreases similarly at first, but after ~day 60, begins to rise again, reaching above 10^4 by day 180.

Design Encodings :
  • Solid red line for "cure", dotted red line for "progression".
  • Logarithmic Y-axis.
  • Dashed horizontal line at y = 10^2.
  • Equation inset: Ẋ = r_B - γ_B B (C / (k_B + C)), indicating the model for tumour cell dynamics.
  • Legend: "cure" (solid), "progression" (dotted).
  • Caption box: "two realizations of the same stochastic process".

Distribution & Trends :
  • Both series show a rapid initial decline in tumour cell count.
  • "Cure" series remains low after initial decline.
  • "Progression" series rebounds after initial decline, showing tumour regrowth.

Analysis :
  • The figure demonstrates that, even with identical parameters, stochastic effects can lead to divergent outcomes: either sustained tumour clearance (cure) or tumour regrowth (progression).
  • The initial response to CAR infusion is similar in both cases, but long-term fate diverges after ~60 days.
  • The log scale highlights the dramatic changes in tumour cell numbers and the difference in long-term outcomes. <!-- figure, from page 0 (l=0.503,t=0.251,r=0.900,b=0.429), with ID 1a023cf4-be07-4394-81de-6d8f3b2edcd7 -->

Figure 2. Comparison of model fits and data in the T cell compartments, stochastic dynamics in the tumour cell compartment. (a) ALC was used to parameterize normal T cell dynamics, equation (2.1), using ALC-CAR from peripheral blood to estimate normal T cell counts N. (b) CAR positive T cell dynamics, equation (2.2), were parameterized using ZUMA-1 trial data of median peripheral CAR counts, to fit peak and decay of CAR. Nonlinear optimization for data fitting explained in the electronic supplementary material, section 4. (c) Parameters ranked by local relative sensitivity measure (electronic supplementary material, section 4. Inset: parameter correlation matrix (Pearson correlation, see electronic supplementary material). (d) Two example trajectories of tumour burden over time, using identical parameters and initial conditions for the hybrid deterministic-stochastic process in the tumour compartment. Both examples enter the stochastic region (less than 100 tumour cells), but one escapes leading to progression. All parameter values and initial conditions used are given in table 1. Hybrid model simulation procedure described in the electronic supplementary material, section 5. (Online version in colour.) <!-- text, from page 0 (l=0.066,t=0.432,r=0.933,b=0.550), with ID 32f2f374-a7a1-4daa-9f23-4aa4e6f45725 -->

Table 1. Parameter and initial condition values as identified by our machine learning procedure and from the literature (also see electronic supplementary material, section 4). The CAR T cell growth rate function is $r_G$, which depends on parameters $\rho_C$, a, b. <!-- text, from page 0 (l=0.066,t=0.571,r=0.932,b=0.604), with ID 30a69608-b9ee-422f-a9cd-018ee391a328 -->

<table><thead><tr><th>biological parameter</th><th>symbol</th><th>fitted value</th><th>quartile range</th><th>ref.</th></tr></thead><tbody><tr><td>normal T cell carrying capacity</td><td>K<sub>N</sub></td><td>2.50 × 10<sup>11</sup> cells</td><td>n/a</td><td>[19]</td></tr><tr><td>CAR T cell carrying capacity</td><td>K<sub>C</sub></td><td>6.96 × 10<sup>10</sup> cells</td><td>[6.15, 9.65] × 10<sup>10</sup> cells</td><td>this work</td></tr><tr><td>normal T cell net growth rate</td><td>r<sub>N</sub></td><td>1.70 × 10<sup>−1</sup> day<sup>−1</sup></td><td>[1.65, 1.70] × 10<sup>−1</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>baseline CAR T net growth rate</td><td>ρ<sub>C</sub></td><td>2.51 × 10<sup>−2</sup> day<sup>−1</sup></td><td>[2.08, 3.54] × 10<sup>−2</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>signalling inefficiency factor in r<sub>C</sub></td><td>a</td><td>4.23 × 10<sup>−1</sup></td><td>[1.00, 3.02] × 10<sup>−1</sup></td><td>this work</td></tr><tr><td>immune reconstitution impact in r<sub>C</sub></td><td>b</td><td>5.25 × 10<sup>−1</sup> day<sup>−1</sup></td><td>[4.67, 5.22] × 10<sup>−1</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>tumour net growth rate</td><td>r<sub>B</sub></td><td>(1 − 50) × 10<sup>−2</sup> day<sup>−1</sup></td><td>n/a</td><td>[20]</td></tr><tr><td>tumour-killing rate (by effector CAR)</td><td>γ<sub>B</sub></td><td>1.15 × 10<sup>0</sup> day<sup>−1</sup></td><td>[0.64, 1.35] × 10<sup>0</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>killing rate saturation parameter</td><td>k<sub>B</sub></td><td>2.024 × 10<sup>9</sup> cells</td><td>[1.40, 3.125] × 10<sup>9</sup> cells</td><td>this work</td></tr><tr><td>initial median normal T cell number</td><td>N(t = 0)</td><td>3.00 × 10<sup>9</sup> cells</td><td>n/a</td><td>[5]</td></tr><tr><td>initial CAR T cell number</td><td>C(0)</td><td>1.80 × 10<sup>8</sup> cells</td><td>n/a</td><td>[5]</td></tr><tr><td>initial median tumour cell number</td><td>B(0)</td><td>9.486 × 10<sup>10</sup> cells</td><td>n/a</td><td>[5]</td></tr></tbody></table> <!-- table, from page 0 (l=0.068,t=0.614,r=0.931,b=0.861), with ID 3423fd0e-e8b1-46c5-ab36-3c1b40ff760b -->

after statistical examination (see electronic supplementary
material, section 3).
  CAR T cell persistence, at least for some time, could result
from CAR T effector memory cells [6]. Currently, it is unclear <!-- text, from page 0 (l=0.067,t=0.888,r=0.480,b=0.947), with ID 09e04339-6d8e-459b-8530-5c583a85b679 -->

whether CAR T persistence plays a role in LBCL treatment
[4]; remarkably, cure is possible without CART cell persistence.
The decline over time of CART cells may occur on a time frame
longer than the expected survival time, even in patients <!-- text, from page 0 (l=0.521,t=0.889,r=0.932,b=0.947), with ID 69a15016-e112-4418-b828-01a2e9fc8042 -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.000,t=0.297,r=0.031,b=0.703), with ID 794e735c-4696-4ab4-bef6-ca63267354de -->

4 <!-- marginalia, from page 0 (l=0.939,t=0.048,r=0.976,b=0.067), with ID 85967ed4-fa45-469e-b519-6bd210075257 -->

royalsocietypublishing.org/journal/rspb
Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.947,t=0.077,r=0.976,b=0.376), with ID 8fcde566-e0e7-46e4-84bc-6eadd69f5397 -->

with tumour extinction. Therefore, the clinical definition of
(temporal) CAR T persistence may be captured by our model.

    CAR T expansion occurs rapidly within the first two weeks.
By contrast, CAR T cells decay on a much slower time scale. For
instance, the median patient still retains levels comparable to
their value at infusion by day 90. Hence, other functional
dependencies need to be placed on the CAR T cell growth
rate (equation (2.2)). The baseline rate ρ_C sets the time scale at
which birth and death events occur on average in the CAR T
cell population. These birth and death rates depend on signals
provided by all T cells, which change during therapy as the
immune system returns to homeostatic levels. Hence, we
expect the overall CAR T cell turnover rate to change during
the course of reconstitution. The dependence on the total lym-
phocyte count T describes these nonlinear dynamics as the
total T cell count approaches a carrying capacity, $T \rightarrow K_N$. <!-- text, from page 0 (l=0.064,t=0.044,r=0.483,b=0.279), with ID e3dc5b4a-c939-4ed4-a6d9-d7ec4198248d -->

(d) Stochastic tumour extinction  
As a consequence of CAR T cell impairment in renewal capacity, tumour eradication is deterministically unstable and not a long-term outcome (see electronic supplementary material, section 3). However, tumour mass often shrinks at least for some time during treatment and can temporarily be brought down to very low levels [4], leading to possible stochastic extinction (figure 2d). We predict that if cure occurs, it does so via a stochastic event in which the malignant B cells are driven to extinction [28]. This stochastic approach leads to the question of whether parameter variability (e.g. patient variability), or stochasticity of the underlying process, or both, are responsible for the broad distributions of the times to cure or progression and probability of cure. Of those ZUMA-1 patients that were treated at Moffitt, we assessed the variability in CAR T cell kinetics, although not all patients had all time points available (figure 3a). The Moffitt ZUMA-1 patient cohort’s (overall n = 23 patients) variability in CAR T count (cells μl–1) were 27.5 (IQR: 16.5,57.5; n = 19), 9.1 (IQR: 3.8,31.1; n = 23), 2.1 (IQR: 0.6,6.1; n = 22) and 0.1 (IQR: 0.01,0.4; n = 22) at days 7, 14, 28 and 90, respectively. <!-- text, from page 0 (l=0.065,t=0.297,r=0.483,b=0.607), with ID c21ff52f-0b37-408a-bcd1-716b9897b273 -->

(e) Probability and time to progression  
To evaluate our model parameterization, we compared the overall progression-free survival (PFS) curve for all patients in the ZUMA-1 [5] trial to a virtual cohort of 1000 simulated patients with varying tumour growth rates (figure 3b). Although we had not used progression-free survival as a goal function to find suitable model parameters (Methods, electronic supplementary material, section 4), our stochastic model recapitulates PFS of the ZUMA-1 trial for reasonable tumour growth rate values, using a hybrid deterministic–stochastic numerical approach (electronic supplementary material, section 5) in which the system is simulated deterministically if the tumour is above a threshold value, and the tumour is simulated stochastically once below this threshold (the outcomes were very weakly impacted by choice of threshold; see electronic supplementary material). As a result, a probability of tumour extinction can be calculated numerically as a function of specific model parameters for a fixed point in time or overall. Treatment success (probability of tumour extinction) critically depends on the ability of the CAR T to survive (figure 3c), and on the effectiveness of lymphodepletion that reduce absolute lymphocyte counts (figure 3d). <!-- text, from page 0 (l=0.065,t=0.625,r=0.484,b=0.947), with ID 4f382062-ad05-421f-9cce-70895fce76bb -->

(f) Variability in outcomes  
A natural question involves whether overall variability in timing to cure or progression is shaped by patient variability (implemented using a hyperparameter that perturbs the parameters, see electronic supplementary material, section 5.3) in contrast with model stochastic effects. We performed additional stochastic simulations of tumour extinction (electronic supplementary material, section 5.4) under controlled parameter variation. We found that the probability of cure changes with overall parameter variability (figure 3e). Similarly, the time to cure distribution for a specific set of parameters widens with increasing parameter variability (figure 3f). Thus, variation in patient-specific conditions and parameter values could be the main determinant of observed variability in timing of cure or progression. <!-- text, from page 0 (l=0.519,t=0.046,r=0.933,b=0.264), with ID 85fe72bf-a6b6-4950-abcd-81689356f122 -->

Most stochastic simulations resulted in cure between days
20 and 80. We rarely found late cure events up to day 140
(figure 4a). Meanwhile, progression times were distributed
over a broader range. Typical progression times, as defined
in our model as 120% of initial tumour burden, occur any-
where between days 200 and 500 (figure 4b). These large
differences in time scales occur because cure, as a stochastic
tumour extinction event, is much more likely to occur
before CAR T cells begin to decline, typically after day 14. <!-- text, from page 0 (l=0.520,t=0.266,r=0.934,b=0.396), with ID 8fe0ef85-6a0c-4a33-90c3-46efaf5c2647 -->

(g) Necessity of lymphodepletion  
In the context of timing of events, our model can be useful to test new treatment strategies in silico, to inform clinical trial design. For example, we used our model to inform the timing of a second infusion, with or without additional lymphodepletion (electronic supplementary material, section 6) [11]. To improve outcomes with a second infusion, lymphodepletion that resets the T cells is necessary. This suggests that a second, lower dose lymphodepletion alone might be sufficient, provided it does not kill all CAR T cell but lowers overall T cell density sufficiently. The temporal suppression of normal lymphocytes is a key driver of CAR expansion, which, together with transient tumour burden data, could be leveraged to further evaluate the benefit of second interventions. <!-- text, from page 0 (l=0.519,t=0.414,r=0.934,b=0.620), with ID 3c191868-ba33-4c6b-be84-1aced6f9ccdf -->

4. Discussion  
Here, we propose a modelling framework for the analysis and prediction of cellular kinetics during CAR T cell therapy. We focus on normal T cells, CAR T cells and tumour cells and find that CAR expansion and decay can be explained via competitive growth in the context of immune reconstitution, which is a consequence of the lymphodepletion prior to therapy. A ramification of the model is that cure must be a stochastic event. However, the likelihood of cure is largely determined by specific parameters and tumour fluctuations play a minor role in the variability of clinical outcomes. These insights can be leveraged to better understand why therapy works for some but not all, and how it can be improved. <!-- text, from page 0 (l=0.519,t=0.651,r=0.934,b=0.859), with ID 6d189a87-e5bd-4fb9-a217-58cd3023564b -->

We posited four potential drivers of patient outcomes: the
effects of normal T cell dynamics on CAR T cells, CAR T cell
expansion (peak), CAR T cell durability (slow decay) and
tumour-killing rate. To better understand these processes, we
developed a cell population-ecological framework that describes
the kinetics of normal T, CAR T and tumour cells. We performed <!-- text, from page 0 (l=0.521,t=0.860,r=0.933,b=0.946), with ID ab512b56-0f4c-4593-bfd1-16c93b14cf7c -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.000,t=0.296,r=0.032,b=0.704), with ID 855393bc-963a-4d84-b91f-45ce7a786580 -->

5 <!-- marginalia, from page 0 (l=0.939,t=0.047,r=0.976,b=0.068), with ID 6a6eb33c-1b52-4651-9369-b35441f160d4 -->

royalsocietypublishing.org/journal/rspb

Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.946,t=0.077,r=0.977,b=0.376), with ID 57053f10-913a-4345-888f-82fdd255b5d9 -->

Summary : This multi-panel figure presents mathematical modeling and simulation results for CAR T cell therapy in cancer, including CAR T cell kinetics, progression-free survival, and the impact of biological and patient variability on cure probability and time to cure.

line and scatter plots with violin plots:
# (a) CAR T kinetics (ZUMA-1 Moffitt patients) :
  • Title: "CAR T kinetics (ZUMA-1 Moffitt patients)"
  • X-axis: "time (days)", range: 0 to ~175.
  • Y-axis: "CAR T cells μl⁻¹", log scale, range: 10⁻² to 10³.
  • Data: Individual patient trajectories (grey lines and points), fitted model (thick blue line).
  • Design: Grey lines for individual patients, blue line for model fit, log-scaled y-axis.

# (b) Progression-free survival (PFS): simulations versus clinical trial :
  • Title: "progression-free survival (PFS): simulations versus clinical trial"
  • X-axis: "days post CAR infusion", range: 0 to 400.
  • Y-axis: "PFS", range: 0 to 1.
  • Data: Four lines—slow (orange dashed), medium (red dashed), fast growing tumour (yellow dashed), ZUMA-1 (all patients, solid black).
  • Design: Different dashed and solid lines for each group.

# (c) Impact of CAR T adaptation :
  • Title: "impact of CAR T adaptation"
  • X-axis: "CAR T carrying capacity", range: 100 to 200.
  • Y-axis: "probability of cure", range: 0 to 1.
  • Data: Three series (blue, green, yellow dots) for min, median, max initial tumour.
  • Design: Dots, three colours for different initial tumour sizes.

# (d) Impact of normal T cell count after lymphodepletion :
  • Title: "impact of normal T cell count after lymphodepletion"
  • X-axis: "normal T cells μl⁻¹ at infusion", range: 2 to 12.
  • Y-axis: "probability of cure", log scale, range: 10⁻⁴ to 1.
  • Data: Three series (blue, green, yellow dots) for min, median, max initial tumour.
  • Design: Dots, three colours, log-scaled y-axis.

# (e) Impact of parameter variability on probability of cure :
  • Title: "impact of parameter variability on probability of cure"
  • X-axis: "patient std. deviation σ", values: 0.001, 0.01, 0.05, 0.10, 0.15, 0.20, 0.25.
  • Y-axis: "probability of cure", range: 0 to 1.
  • Data: Black dots for each σ value.

# (f) Impact of parameter variability on time to cure :
  • Title: "impact of parameter variability on time to cure"
  • X-axis: "patient std. deviation σ", values: 0.001, 0.01, 0.05, 0.10, 0.15, 0.20, 0.25.
  • Y-axis: "time to cure", range: 0 to 150.
  • Data: Violin plots for each σ value, coloured from red (low σ) to yellow (high σ).

# Design Encodings :
  • Multiple panels (a–f), each with distinct axes and data.
  • Use of log scales in panels (a) and (d).
  • Colour coding for tumour growth rates and initial tumour sizes.
  • Violin plots in panel (f) to show distribution.

# Analysis :
  • Panel (a): CAR T cell counts peak early and decline over time; model fits median trend.
  • Panel (b): Simulated PFS curves for different tumour growth rates closely match clinical trial data; slower tumours have better PFS.
  • Panel (c): Probability of cure increases with higher CAR T carrying capacity, especially for smaller initial tumours.
  • Panel (d): Higher normal T cell counts at infusion reduce probability of cure, especially for larger initial tumours.
  • Panel (e): Increasing patient parameter variability (σ) reduces probability of cure.
  • Panel (f): Greater parameter variability increases both the spread and median of time to cure. <!-- figure, from page 0 (l=0.086,t=0.046,r=0.911,b=0.536), with ID 64d236f5-b9da-4d38-ba67-c03004006f8a -->

Figure 3. Using stochastic simulations to describe progression-free survival and probability of cure (tumour extinction). (a) Individual CAR T kinetics for a subset of patients treated on the ZUMA-1 trial ($n = 21$). (b) Progression-free survival (PFS) during ZUMA-1 (grey line, $n = 101$), and our stochastic simulations that recapitulates this PFS curve. We recorded progression when 1.2 times the initial tumour mass was reached to avoid bias against cases that briefly increased in tumour mass but responded well eventually. Intrinsic tumour growth rates: 0.105/day (slow), 0.19/day (medium) and 0.265/day (fast). (c) Increasing the adaptability of CAR T cells (carrying capacity) improves probability of cure. (d) Initial reduction of normal T cells at CAR administration due to lymphodepletion is crucial; increasing this number decreases probability of cure. Tumour sizes for (c), (d) min $= 2.3 \times 10^9$, median $= 9.5 \times 10^{10}$, max $= 1.3 \times 10^{12}$. All probabilities estimated using 1000 stochastic simulations with the same initial conditions, all other parameters drawn from a normal distribution with a variance of 5% of mean values (table 1). (e) Without patient variability (described in the electronic supplementary material, section 5), our set of parameters (table 1) is most likely to lead to cure. As parameter variability increases, cure probability drops and saturates. (f) The distribution of time to cure (tumour extinction) without patient variability is narrow. Increases in patient variability then drastically increase the range of possible times to cure. The results in (e) and (f) were obtained using 100 independent stochastic simulations of the simplified stochastic process described in electronic supplementary material, section 5.4. (Online version in colour.) <!-- text, from page 0 (l=0.065,t=0.538,r=0.936,b=0.701), with ID dcd86d6e-3c20-48d8-85b2-c3e5955e6946 -->

parameter sensitivity and correlation analyses, and calculated
probability of cure and PFS from stochastic simulations. <!-- text, from page 0 (l=0.066,t=0.717,r=0.481,b=0.746), with ID b7095ced-cb48-4025-aef5-cde86125bc7c -->

We do not make patient-specific, personalized predictions, for which a more comprehensive dataset would be needed [29], matching multiple longitudinal data from the same patient. Instead, we give proof-of-principle that the integration of longitudinal lymphocyte counts with CAR T cell counts and changes in tumour burden can be very useful to predictively model the cell population dynamics that likely determine clinical outcomes. <!-- text, from page 0 (l=0.068,t=0.745,r=0.480,b=0.859), with ID 92e18c0e-8ecb-4626-ae1d-8a117420740b -->

Our model confirms the hypothesis that sufficient
lymphodepletion is an important factor in determining
durable response. Improving the adaptation of CAR T cells
to expand more and survive longer in vivo could result
in increased likelihood and duration of response. Future
modelling should investigate other available signals, such <!-- text, from page 0 (l=0.068,t=0.860,r=0.480,b=0.946), with ID ee18cc04-c99f-4faa-af68-1f58750995be -->

as the dynamics and upregulation of homeostatic and
inflammatory cytokines. <!-- text, from page 0 (l=0.520,t=0.718,r=0.932,b=0.746), with ID 7fd2d34a-744e-4849-839d-a7d37babb813 -->

The emergence of Gompertz growth of T cells is an interesting result of our analysis. A possible explanation can be found in recent work [30], which employed techniques from statistical mechanics to explain the emergence of well-known tumour growth laws. In particular, Gompertz emerged via a reduction in available microstates (e.g. cellular phenotypes), causing a characteristic slowdown of the overall population expansion. Our results suggest that this phenomenon could play a role during immune reconstitution. After rapid expansion, the immune compartment engages in negative selection to keep a flexible adaptive immune system ready to engage pathogens. Therefore, by analogy to the reduction of available microstates, the T cell population approaches a carrying capacity via Gompertz-like growth. <!-- text, from page 0 (l=0.520,t=0.747,r=0.932,b=0.946), with ID 09feada8-d393-4178-9463-a60e74a9315a -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.000,t=0.298,r=0.031,b=0.702), with ID 69dba57b-1bf1-4cc5-a8e8-e37f00d10dc3 -->

6 <!-- marginalia, from page 0 (l=0.939,t=0.048,r=0.977,b=0.067), with ID 526c9a4f-a50a-4c21-9ac6-2554ab42df85 -->

royalsocietypublishing.org/journal/rspb  
Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.946,t=0.076,r=0.975,b=0.377), with ID 0fb43ce4-9ee9-4eba-b4ce-2527c1b796b2 -->

Summary : This figure presents the statistics of cure and progression times following CAR infusion, using stochastic simulations. It compares the distributions of time to cure and time to progression, and examines how these times vary with initial tumour size.

bar chart and violin plots:

# (a) Time to Cure Distribution

## Title & Axes :
  • Subpanel (a)(i) title: "time to cure distribution"
  • X-axis: "days post CAR infusion" (range: 20 to 140)
  • Y-axis: "probability" (range: 0 to 0.35, ticks at 0.05 intervals)

## Data Points :
  • Histogram bars show probability distribution of cure times for the median parameters.
  • Most probability mass between 30 and 80 days.

## Design Encodings :
  • Light green bars, semi-transparent.
  • Histogram style.

## Distribution & Trends :
  • Right-skewed distribution with a peak between 40 and 60 days.
  • Most patients cured before day 100.

# (a)(ii) Time to Cure vs. Initial Tumour Size

## Title & Axes :
  • No explicit title, but violin plot for "time to cure" vs. "initial tumour size (min, max, percentiles)".
  • X-axis: "initial tumour size (min, max, percentiles)" (categories: min, 25th, 50th, 75th, max)
  • Y-axis: "time to cure" (range: 20 to 140)

## Data Points :
  • Five violin plots, shades of green from dark (min) to light (max).
  • Each violin shows distribution of cure times for a given initial tumour size percentile.

## Design Encodings :
  • Colour gradient from dark to light green.
  • Violin plot shape indicates distribution width and central tendency.

## Distribution & Trends :
  • Cure times cluster between 30 and 60 days for all tumour sizes.
  • Slight increase in spread for larger initial tumour sizes.

# (b) Time to Progression Distribution

## Title & Axes :
  • Subpanel (b)(i) title: "time to progression distribution (defined as 120% of initial tumour)"
  • X-axis: "days post CAR infusion" (range: 0 to 700)
  • Y-axis: "probability" (range: 0 to 0.16, ticks at 0.02 intervals)

## Data Points :
  • Histogram bars show probability distribution of progression times for the median parameters.
  • Most probability mass between 300 and 500 days.

## Design Encodings :
  • Light red bars, semi-transparent.
  • Histogram style.

## Distribution & Trends :
  • Symmetric, bell-shaped distribution peaking around 400 days.
  • Most simulations progress between days 300 and 500.

# (b)(ii) Time to Progression vs. Initial Tumour Size

## Title & Axes :
  • No explicit title, but violin plot for "time to progression" vs. "initial tumour size (min, max, percentiles)".
  • X-axis: "initial tumour size (min, max, percentiles)" (categories: min, 25th, 50th, 75th, max)
  • Y-axis: "time to progression" (range: 200 to 600)

## Data Points :
  • Five violin plots, shades of red from light (min) to dark (max).
  • Each violin shows distribution of progression times for a given initial tumour size percentile.

## Design Encodings :
  • Colour gradient from light to dark red.
  • Violin plot shape indicates distribution width and central tendency.

## Distribution & Trends :
  • Progression times cluster between 300 and 500 days for all tumour sizes.
  • Spread increases with larger initial tumour sizes.

# Analysis :
  • Time to cure is generally much shorter than time to progression, with most cures occurring before day 100 and most progressions between days 300 and 500.
  • Both cure and progression times show some dependence on initial tumour size, with larger tumours exhibiting slightly more spread in outcomes.
  • Cure time distributions are right-skewed, while progression times are more symmetric.
  • Colour gradients in violin plots visually encode increasing initial tumour size.
  • All data are based on 1000 stochastic simulations per condition. <!-- figure, from page 0 (l=0.066,t=0.044,r=0.926,b=0.451), with ID a805d071-d362-4ec8-baa0-9fa81e591517 -->

We made several assumptions to approach the broader
biological context of CAR T cell therapy. First, we assumed
that immune reconstitution varies minimally across patients.
The interplay between normal and CAR T competition in
individual patients should be addressed in future studies
that track both simultaneously, which could also reveal
whether the slope of ALC is predictive of CAR expansion
and efficacy. <!-- text, from page 0 (l=0.066,t=0.473,r=0.481,b=0.589), with ID 35295899-ee7c-4896-9d15-bca744431914 -->

Second, our model assumes that tumour cell proliferation
is independent of tumour burden. However, the tumour
growth rate might decrease with tumour burden. In this
context, one could explore other sources of tumour burden
variability that originate from a logistic dependence of pro-
liferation on tumour volume, called proliferation-saturation
[31,32], which points to the need for higher temporal
resolution of tumour data. <!-- text, from page 0 (l=0.067,t=0.590,r=0.480,b=0.702), with ID 63a6c2d4-2d48-4fea-a703-22b66c34609c -->

Third, our probabilistic measure of PFS did not include
the evolution of resistance to CAR T cell therapy by immuno-
logic, genetic or epigenetic escape [33], which would add an
additional probabilistic modelling layer. <!-- text, from page 0 (l=0.068,t=0.703,r=0.479,b=0.760), with ID 7500cd2b-247b-4110-827c-bab20ada5d72 -->

Fourth, normal CD19+ B cells are at negligible levels in
the weeks following lymphodepletion. These levels are low
until 4–6 months post infusion, implying that their presence
is minimal, although they are potential sources of target anti-
gen. Further, the detection of normal CD19+ B cells in
circulation long after CAR T is evidence that functional
CAR T cells no longer persist in the host. It is unclear whether
B cells themselves could be responsible for continued CAR T
persistence. Thus, we assume that non-tumour sources of
CD19 do not play a role during the activity of CAR T cells. <!-- text, from page 0 (l=0.069,t=0.760,r=0.479,b=0.902), with ID d31101c1-fea5-412d-b60a-7ea145b339a4 -->

Fifth, the functional form for the tumour-killing rate was
justified in preliminary analysis and by considering the fact
that there should be an upper limit on the number of CAR <!-- text, from page 0 (l=0.069,t=0.903,r=0.479,b=0.945), with ID 746b78de-be60-4751-b1ac-44d1ca76204b -->

T cells that can surround a given tumour cell. We expect an
upper limit on the rate of killing. However, an analogous
argument could be made for tumour influence, leading
to the following alternative forms of the killing term:
$\gamma_B B\, C/(k_B + \phi B + C)$ or $\gamma_B (B/k_B + B)(C/k_C + C)$. Given the
lack of temporal data (especially for the tumour), we elected
the simpler form in equation (2.3). <!-- text, from page 0 (l=0.521,t=0.476,r=0.932,b=0.574), with ID fe7d6c37-4d90-4729-a568-fd782ead7c93 -->

We focused on the treatment of LBCL, but our approach could also be applied to CAR T cell treatment of chronic lymphocytic leukaemia (CLL) [34,35] (investigational), or acute lymphocytic leukaemia (ALL) [36] and mantle cell lymphoma [37], the other approved indications for CAR T cell therapy. Quantitative systems pharmacological (QSP) modelling of CAR T cell kinetics to treat ALL has been conducted recently to describe kinetics independently of tumour or normal T cell dynamics [6,38], to study the effects of additional prophylactic interventions [6], or to include cytokine kinetics [38]. Our model can be interpreted such that long-term CAR T cell survival, possibly necessary to cure ALL, would require a significant slowdown of CAR T cell turnover, or an additional memory compartment. There is not enough longitudinal data in LBCL at this point to model additional CAR T compartments. As such, our model has markedly fewer parameters (two from the literature, seven fitted) than several of the recently developed QSP approaches (around 20 parameters) [11]. <!-- text, from page 0 (l=0.522,t=0.576,r=0.932,b=0.844), with ID ded38165-a2d3-4c3a-baa9-d42f5e48910f -->

Our definition of progression predicts progression events
later than those observed in some patients per clinical defi-
nition [4,17]. This discrepancy indicates that there is
additional, unresolved patient heterogeneity, potentially in
the form of differences in naive and memory cells in the
CAR T cell product at day 0, further highlighting the need
for high-resolution longitudinal data. <!-- text, from page 0 (l=0.523,t=0.847,r=0.931,b=0.945), with ID 114166df-8a95-494f-bfa7-86a45e7267fd -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025. <!-- marginalia, from page 0 (l=0.000,t=0.299,r=0.029,b=0.700), with ID 5d5310be-5dc0-45a4-be92-1dc21c6c41ba -->

7 <!-- marginalia, from page 0 (l=0.940,t=0.047,r=0.976,b=0.067), with ID b4ee96bd-3be7-4a55-b55f-4f62f1c759e6 -->

royalsocietypublishing.org/journal/rspb  
Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.947,t=0.077,r=0.974,b=0.375), with ID f8558074-e157-4afa-acf1-a1ff99d64309 -->

Our results point to the importance of the immune system’s
influence on CAR T cell kinetics, and the impact of those kin-
etics on potentially stochastic tumour dynamics. We hope
that our model can be consolidated with descriptions of
short-term changes in inflammatory cytokines [19,39–41],
because these are accessible alternative biomarkers for the
immune system’s impact [11]. On the other hand, engineering
a CAR T product with fewer cell divisions, improving its ‘stem-
ness’ or increasing metabolic capacity of CAR T cells should
lead to a higher carrying capacity. Such changes would lead
to a higher peak and a higher total volume of CAR T cells
during treatment. Stem-ness, support by secreted molecules
(e.g. IL-2, IL-12) [42] or CAR T cell exhaustion as additional
mechanisms should be subject to future modelling. <!-- text, from page 0 (l=0.065,t=0.045,r=0.482,b=0.247), with ID df9d509b-ae5b-4b85-ad67-94551e88bf74 -->

Finally, models of treatment–tumour interactions do not
require that tumour extinction is a stable steady state.
Tumour extinction (cure) can be a stochastic event, since
cure becomes an absorbing state in a stochastic framework.
Our results indicate that the effects of CAR T cell therapy
are transient and should be optimized to maximize initial
impact and rapidly drive tumours into this stochastic <!-- text, from page 0 (l=0.066,t=0.247,r=0.482,b=0.349), with ID e9a59496-6c0d-47a9-871b-4b8d26a18bb1 -->

regime. The dynamics of our model are most sensitive to
the ability of CAR T to kill tumours and to the CAR T cell
expansion capacity. Future translational work to improve
these parameters may ultimately improve efficacy of therapy. <!-- text, from page 0 (l=0.520,t=0.046,r=0.932,b=0.107), with ID 747ad53e-ff70-4577-9805-f4b1f5e3e33d -->

Data accessibility. All code and data used in this manuscript can be found at https://github.com/MathOnco/CARTEcology.

Authors’ contributions. G.J.K., F.L.L. and P.M.A. conceived of the model and designed the study. G.J.K. carried out the mathematical modelling. G.J.K. and P.M.A. carried out computational modelling and statistical data analysis. F.L.L. and P.M.A. coordinated and supervised the study. G.J.K., F.L.L. and P.M.A. wrote the manuscript. All authors gave final approval for publication and agree to be held accountable for the work performed therein.

Competing interests. G.J.K. and P.M.A. declare no potential conflict of interest. F.L.L. is scientific adviser to Kite, Novartis, and Gamma-Delta T cell Therapeutics, and consultant to CBMG.

Funding. This study was supported by the Richard O. Jacobson Foundation, Moffitt Cancer Center Evolutionary Therapy Center, William G. ‘Bill’ Bankhead Jr and David Coley Cancer Research Program (20B06), National Cancer Institute (P30-CA076292 and U54-CA193489) and USAMRAA (KC180036). <!-- text, from page 0 (l=0.519,t=0.135,r=0.933,b=0.347), with ID 62be88ec-cbb2-41a2-b8bc-09012dda6cdb -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.000,t=0.295,r=0.032,b=0.706), with ID 52ad595b-de4e-4262-9979-ba39d86364ab -->

10. Maude SL et al. 2018 Tisagenlecleucel in children
    and young adults with B-cell lymphoblastic
    leukemia. N Engl. J. Med. 378, 439–448. (doi:10.
    1056/NEJMoa1709866)
11. Chaudhury A et al. 2020 Chimeric antigen receptor
    T cell therapies: a review of cellular kinetic-
    pharmacodynamic modeling approaches. J. Clin.
    Pharmacol. 60(Suppl 1), S147–S559.
12. Kimmel GJ, Locke LL, Altrock PM. 2020 Response to
    CAR T cell therapy can be explained by ecological
    cell dynamics and stochastic extinction events.
    bioRxiv. 717074. (doi:10.1101/717074)
13. Wang E, Cesano A, Butterfield LH, Marincola F. 2020
    Improving the therapeutic index in adoptive cell
    therapy: key factors that impact efficacy.
    J. Immunother. Cancer 8, e001619. (doi:10.1136/
    jitc-2020-001619)
14. Henning AN, Klebanoff CA, Restifo NP.
    2018 Silencing stemness in T cell differentiation.
    Science 359, 163–164. (doi:10.1126/science.
    aar5541)
15. Pace L, Goudot C, Zueva E, Gueguen P, Burgdorf N,
    Waterfall JJ, Quivy J-P, Almouzni G, Amigorena S.
    2018 The epigenetic control of stemness in CD8+ T
    cell fate commitment. Science 359, 177–186.
    (doi:10.1126/science.aah6499)
16. Oxnard GR, Morris MJ, Hodi FS, Baker LH, Kris MG,
    Venook AP, Schwartz LH. 2012 When progressive
    disease does not mean treatment failure:
    reconsidering the criteria for progression. J. Natl.
    Cancer Inst. 104, 1534–1541. (doi:10.1093/jnci/
    djs353)
17. NCI. 2019 Time to progression. In Dictionary of
    cancer terms, 1908D. Bethesda, MD: National Cancer
    Institute.
18. Hart Y, Reich-Zeliger S, Antebi YE, Zaretsky I, Mayo
    A, Alon U, Friedman N. 2014 Paradoxical signaling <!-- text, from page 0 (l=0.365,t=0.407,r=0.639,b=0.939), with ID cebc48e1-f1d4-4502-9ba1-e3134bec4e49 -->

19. Turtle CJ et al. 2016 CD19 CAR–T cells of defined CD4+: CD8+ composition in adult B cell ALL patients. _J. Clin. Invest._ **126**, 2123–2138. (doi:10.1172/JCI85309)
20. Roesch K, Hasenclever D, Scholz M. 2014 Modelling lymphoma therapy and outcome. _Bull. Math. Biol._ **76**, 401–430. (doi:10.1007/s11538-013-9925-3)
21. Olufsen MS, Ottesen JT. 2013 A practical approach to parameter estimation applied to model predicting heart rate regulation. _J. Math. Biol._ **67**, 39–68. (doi:10.1007/s00285-012-0535-8)
22. Miao H, Xia X, Perelson AS, Wu H. 2011 On identifiability of nonlinear ODE models and applications in viral dynamics. _SIAM Rev. Soc. Ind. Appl. Math._ **53**, 3–39.
23. Brady-Nicholls R, Nagy JD, Gerke TA, Zhang T, Wang AZ, Zhang J, Gatenby RA, Enderling H. 2020 Prostate-specific antigen dynamics predict individual responses to intermittent androgen deprivation. _Nat. Commun._ **11**, 1750. (doi:10.1038/s41467-020-15424-4)
24. Richards FJ. 1959 A flexible growth function for empirical use. _J. Exp. Bot._ **10**, 290–300. (doi:10.1093/jxb/10.2.290)
25. Muranski P, Boni A, Wrzesinski C, Citrin DE, Rosenberg SA, Childs R, Restifo NP. 2006 Increased intensity lymphodepletion and adoptive immunotherapy—how far can we go? _Nat. Clin. Pract. Oncol._ **3**, 668–681. (doi:10.1038/ncponc0666)
26. Williams KM, Hakim FT, Gress RE. 2007 T cell immune reconstitution following lymphodepletion. _Semin. Immunol._ **19**, 318–330. (doi:10.1016/j.smim.2007.10.004) <!-- text, from page 0 (l=0.656,t=0.411,r=0.934,b=0.938), with ID 22755cb0-daf5-49da-b99c-b7da5a4dc11c -->

8 <!-- marginalia, from page 0 (l=0.940,t=0.048,r=0.975,b=0.067), with ID 3ef3ead2-e946-4934-9be0-7fdb25a608ea -->

royalsocietypublishing.org/journal/rspb

Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.945,t=0.076,r=0.977,b=0.377), with ID c86c5a7c-a202-4f9c-8929-d772ff5eef44 -->

downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=-0.003,t=0.251,r=0.034,b=0.692), with ID 63b6c7bb-a9fa-45f9-ac8a-662977c84c14 -->

27. Wu L, Wei Q, Brzostek J, Gascoigne NRJ. 2020
Signaling from T cell receptors (TCRs) and chimeric
antigen receptors (CARs) on T cells. _Cell. Mol.
Immunol._ **17**, 600–612. (doi:10.1038/s41423-020-
0470-3)
28. Gilpin ME. 1986 Minimal viable populations: processes
of species extinction. In _Conservation biology: the
science of scarcity and diversity_ (ed ME Soulé).
Sunderland, MA: Sinauer Associates.
29. Brady R, Enderling H. 2019 Mathematical models of
cancer: when to predict novel therapies, and when not
to. _Bull. Math. Biol._ **81**, 3722–3731. (doi:10.
1007/s11538-019-00640-x)
30. West J, Newton PK. 2019 Cellular interactions
constrain tumor growth. _Proc. Natl Acad. Sci. USA_
**116**, 1918–1923. (doi:10.1073/pnas.1804150116)
31. Prokopiou S et al. 2015 A proliferation saturation
index to predict radiation response and personalize
radiotherapy fractionation. _Radiat. Oncol._ **10**, 159.
(doi:10.1186/s13014-015-0465-x)
32. Poleszczuk J, Walker R, Moros E, Latifi K, Caudell J,
Enderling H. 2017 Predicting patient-specific
radiotherapy protocols based on mathematical
model choice for Proliferation Saturation Index. _Bull._ <!-- text, from page 0 (l=0.066,t=0.043,r=0.349,b=0.393), with ID 02cf1aa8-88f4-4aeb-8857-0e89be3061cf -->

Math. Biol. 80, 1195–1206. (doi:10.1007/s11538-017-0279-0)
33. Altrock PM, Liu LL, Michor F. 2015 The mathematics of cancer: integrating quantitative models. Nat. Rev. Cancer. 15, 730–745. (doi:10.1038/nrc4029)
34. Davila ML, Bouhassira DC, Park JH, Curran KJ, Smith EL, Pegram HJ, Brentjens R. 2014 Chimeric antigen receptors for the adoptive T cell therapy of hematologic malignancies. Int. J. Hematol. 99, 361–371. (doi:10.1007/s12185-013-1479-5)
35. Fraietta JA et al. 2018 Determinants of response and resistance to CD19 chimeric antigen receptor (CAR) T cell therapy of chronic lymphocytic leukemia. Nat. Med. 24, 563–571. (doi:10.1038/s41591-018-0010-1)
36. Mueller KT et al. 2018 Clinical pharmacology of tisagenlecleucel in B-cell acute lymphoblastic leukemia. Clin. Cancer Res. 24, 6175–6184. (doi:10.1158/1078-0432.CCR-18-0758)
37. Wang M et al. 2020 KTE-X19 CAR T-cell therapy in relapsed or refractory mantle-cell lymphoma. N Engl. J. Med. 382, 1331–1342. (doi:10.1056/NEJMoa1914347) <!-- text, from page 0 (l=0.365,t=0.045,r=0.638,b=0.391), with ID 94d75139-2676-409d-b2c9-122a26946157 -->

38. Hardiansyah D, Ng CM. 2019 Quantitative systems pharmacology model of chimeric antigen receptor T-cell therapy. _Clin. Transl. Sci._ **12**, 343–349. (doi:10.1111/cts.12636)
39. Park JH _et al._ 2018 Long-term follow-up of CD19 CAR therapy in acute lymphoblastic leukemia. _N Engl. J. Med._ **378**, 449–459. (doi:10.1056/NEJMoa1709919)
40. Dholaria BR, Bachmeier CA, Locke F. 2019 Mechanisms and management of chimeric antigen receptor T-cell therapy-related toxicities. _BioDrugs_ **33**, 45–60. (doi:10.1007/s40259-018-0324-z)
41. Jacobson CA. 2019 CD19 chimeric antigen receptor therapy for refractory aggressive B-cell lymphoma. _J. Clin. Oncol._ **37**, 328–335. (doi:10.1200/JCO.18.01457)
42. Pegram HJ, Lee JC, Hayman EG, Imperato GH, Tedder TF, Sadelain M, Brentjens RJ. 2012 Tumor-targeted T cells modified to secrete IL-12 eradicate systemic tumors **without** need for prior conditioning. _Blood_ **119**, 4133–4141. (doi:10.1182/blood-2011-12-400044) <!-- text, from page 0 (l=0.656,t=0.046,r=0.930,b=0.390), with ID a1e9d4d3-3698-42fc-8c6e-848d50f40077 -->

9 <!-- marginalia, from page 0 (l=0.939,t=0.047,r=0.976,b=0.067), with ID 075220e6-42c6-4e26-a905-59bd20b3fe23 -->

royalsocietypublishing.org/journal/rspb  
Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.948,t=0.074,r=0.974,b=0.376), with ID 7a384939-5269-482f-acfc-1cac722a2eeb -->
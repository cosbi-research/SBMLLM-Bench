<a id='98fb0dbc-a359-4a06-a61b-396cb93c96fc'></a>

Bulletin of Mathematical Biology (2008) 70: 1272–1296
DOI 10.1007/s11538-008-9299-0

<a id='e6bb0d37-6616-47cf-a171-4a917d065973'></a>

ORIGINAL ARTICLE

<a id='23ca31db-27b5-4e30-9872-dda7f4046b66'></a>

Determining Important Parameters in the Spread of Malaria
Through the Sensitivity Analysis of a Mathematical Model

<a id='291458e2-388c-4ee2-86e6-9b1d5166781f'></a>

Nakul Chitnis$^{a,b,c,*}$, James M. Hyman$^{b,d}$, Jim M. Cushing$^{c,d}$

$^{a}$Department of Public Health and Epidemiology, Swiss Tropical Institute, Socinstrasse 57,
Postfach, 4002, Basel, Switzerland
$^{b}$Mathematical Modeling and Analysis, Los Alamos National Laboratory, Los Alamos,
NM 87545, USA
$^{c}$Program in Applied Mathematics, University of Arizona, Tucson, AZ 85721, USA
$^{d}$Department of Mathematics, University of Arizona, Tucson, AZ 85721, USA

<a id='5a0687cb-1244-4571-a881-40f0cad7c485'></a>

Received: 3 August 2007 / Accepted: 20 November 2007 / Published online: 22 February 2008
© Society for Mathematical Biology 2008

<a id='bd6dfd5f-d848-4992-82d2-56709d240629'></a>

**Abstract** We perform sensitivity analyses on a mathematical model of malaria transmission to determine the relative importance of model parameters to disease transmission and prevalence. We compile two sets of baseline parameter values: one for areas of high transmission and one for low transmission. We compute sensitivity indices of the reproductive number (which measures initial disease transmission) and the endemic equilibrium point (which measures disease prevalence) to the parameters at the baseline values. We find that in areas of low transmission, the reproductive number and the equilibrium proportion of infectious humans are most sensitive to the mosquito biting rate. In areas of high transmission, the reproductive number is again most sensitive to the mosquito biting rate, but the equilibrium proportion of infectious humans is most sensitive to the human recovery rate. This suggests strategies that target the mosquito biting rate (such as the use of insecticide-treated bed nets and indoor residual spraying) and those that target the human recovery rate (such as the prompt diagnosis and treatment of infectious individuals) can be successful in controlling malaria.

<a id='3244bbda-52ab-482a-bc79-66a8075aa318'></a>

**Keywords** Malaria  Epidemic model  Sensitivity analysis  Reproductive number  Endemic equilibria

<a id='4a3a3cc5-8616-4ade-8ada-382474a5027f'></a>

1. Introduction

Malaria is an infectious disease caused by the *Plasmodium* parasite and transmitted between humans through bites of female *Anopheles* mosquitoes. There are about 300–500 million annual cases of malaria worldwide with 1–3 million deaths (Roll Back Malaria

<a id='836182ef-cae8-4d7f-925e-c6e5e90d8b32'></a>

*Corresponding author.
*E-mail address:* nakul.chitnis@unibas.ch (Nakul Chitnis).

<!-- PAGE BREAK -->

<a id='d699789a-45fe-4808-ae7a-65a258dd27ea'></a>

Determining Important Parameters in the Spread of Malaria

<a id='3b9ba19d-37c4-4d51-9deb-c96db6809cbc'></a>

1273

<a id='9ce3ddc1-8932-44e8-bba7-05e4062170bb'></a>

Partnership, 2005). About 40% of the world's population live in malaria endemic areas. Although the incidence of malaria had been rising in the last few decades due to in- creasing parasite drug-resistance and mosquito insecticide-resistance, recently significant resources have been made available to malaria control programs worldwide to reduce malaria incidence and prevalence. Comparative knowledge of the effectiveness and effi- cacy of different control strategies is necessary to design useful and cost-effective malaria control programs. Mathematical modeling of malaria can play a unique role in comparing the effects of control strategies, used individually or in packages. We begin such a compar- ison by determining the relative importance of model parameters in malaria transmission and prevalence levels.

<a id='f5356144-b791-4b5e-96d2-c2df890af425'></a>

The mathematical modeling of malaria transmission has a long history, beginning with Ross (1911) and MacDonald (1957), and continuing through Anderson and May (1991). In a Ph.D. dissertation, Chitnis (2005) described a compartmental model for malaria trans-mission, based on a model by Ngwa and Shu (2000); defined a reproductive number, R₀, for the expected number of secondary cases that one infected individual would cause through the duration of the infectious period; and showed the existence and stability of disease-free equilibrium points, xdfe, and endemic equilibrium points, xee. He also com-puted the sensitivity indices for R₀ and xee to the parameters in the model. Chitnis et al. (2006) presented a similar bifurcation analysis of an extension to the model in Chitnis (2005), defining R₀ and showing the existence and stability of xdfe and xee.

<a id='9e61fdd9-5034-4138-a461-d7647f14ff77'></a>

Here we extend the model in Chitnis et al. (2006) and evaluate the sensitivity indices of R0 and xee. This model is different from previous models in that it generalizes the mos-quito biting rate, and includes immigration in a logistic model for the human population with disease-induced mortality. Previous models assumed that mosquitoes have a fixed number of bites per unit time. This model allows the number of mosquito bites on hu-mans to depend on both, the mosquito and human, population sizes. This allows a more realistic modeling of situations where there is a high ratio of mosquitoes to humans, and where human availability to mosquitoes is reduced through vector control interventions. Human migration is common in most parts of the malaria-endemic world and plays an important role in malaria epidemiology. As in Ngwa and Shu (2000), this model also al-lows humans to be temporarily immune to the disease, while still transmitting malaria to mosquitoes.

<a id='71ad0127-641a-427b-897a-98ce658b6dbb'></a>

We compile two reasonable sets of baseline values for the parameters in the model: one for areas of high transmission, and one for areas of low transmission. For some parameters, we use values published in available literature, while for others, we use realistically feasible values. We then compute the sensitivity indices of R0 and xee to both sets of baseline parameter values. As R0 is related to initial disease transmission and xee represents equilibrium disease prevalence, an evaluation of these sensitivity indices allows us to determine the relative importance of different parameters in malaria transmission and prevalence. We thus look at the relative importance of the parameters in four different situations:

<a id='f82d9e11-bfd8-4f88-acff-ecd1413f432a'></a>

- The initial rate of disease transmission in areas of low transmission
- The equilibrium disease prevalence in areas of low transmission
- The initial rate of disease transmission in areas of high transmission
- The equilibrium disease prevalence in areas of high transmission

<!-- PAGE BREAK -->

<a id='83e5a7f6-1d9c-4c70-8117-e97fb338993e'></a>

1274

<a id='95d7b9bf-063b-4aaa-b986-bce61e3593c9'></a>

Chitnis, Hyman, and Cushing

<a id='e1cd863d-683b-4a54-b374-735f972db4ea'></a>

A knowledge of the relative importance of parameters can help guide in developing effi-cient intervention strategies in malaria-endemic areas where resources are scarce.
We first summarize the model and analysis from Chitnis et al. (2006). We then present the baseline parameter values, the sensitivity indices of R0 and xee for these baseline val-ues, and their interpretation. Appendix A contains data from literature and our reasons for choosing the baseline parameter values. The second Appendix describes the methodology of the sensitivity analysis.

<a id='627baeb3-8566-4292-8b43-f6749aee4e6f'></a>

## 2. Mathematical model and analysis
The malaria model (Fig. 1) (Chitnis et al., 2006) and the state variables (Table 1) with parameters in Table 2 satisfy,

<a id='52d4a28c-864f-463a-9fad-f93c51310bed'></a>

dSh/dt = Λh + ψhNh + ρhRh - λh(t)Sh - fh(Nh)Sh (1a)
dEh/dt = λh(t)Sh - νhEh - fh(Nh)Eh (1b)
dIh/dt = νhEh - γhIh - fh(Nh)Ih - δhIh (1c)
dRh/dt = γhIh - ρhRh - fh(Nh)Rh (1d)
dSv/dt = ψvNv - λv(t)Sv - fv(Nv)Sv (1e)
dEv/dt = λv(t)Sv - νvEv - fv(Nv)Ev (1f)
dIv/dt = νvEv - fv(Nv)Iv (1g)

<a id='217269bf-cd21-4d73-88c1-b9fbc1bd99cc'></a>

where, Nh = Sh + Eh + Ih + Rh, Nv = Sv + Ev + Iv, and,

fh(Nh) = μ1h + μ2h Nh,

fv(Nv) = μ1v + μ2v Nv,

λh = (σv Nv σh / (σv Nv + σh Nh)) · βhv · (Iv / Nv),

λv = (σv σh Nh / (σv Nv + σh Nh)) · (βvh · (Ih / Nh) + β̃vh · (Rh / Nh)).

<a id='9c393439-93fa-4514-99cd-e76c5962884e'></a>

All parameters are strictly positive with the exception of the disease-induced death rate, $\delta_h$, which is nonnegative. The mosquito birth rate is greater than the density-independent mosquito death rate: $\psi_v > \mu_{1v}$, ensuring that there is a stable positive mosquito population.

<a id='90d08a4c-def7-4b5c-b4ad-403945cd701a'></a>

We scale the population sizes in each class by the total population sizes to derive,

$\frac{de_h}{dt} = \left(\frac{\sigma_v \sigma_h N_v \beta_h i_v}{\sigma_v N_v + \sigma_h N_h}\right)(1 - e_h - i_h - r_h) - \left(v_h + \psi_h + \frac{\Lambda_h}{N_h}\right)e_h + \delta_h i_h e_h$, (2a)

<!-- PAGE BREAK -->

<a id='6e182998-2675-44b7-8231-f4c1ee26cfd0'></a>

Determining Important Parameters in the Spread of Malaria

<a id='e5c0fa42-5415-48e1-8422-0d45976f410e'></a>

1275

<a id='1b51d789-b0e3-4e1a-a265-84455dff6722'></a>

<::A diagram showing two interconnected compartmental models, one for Humans and one for Mosquitoes. Both are enclosed in dashed boxes.

**Humans Compartment:**
- Boxes (from left to right): S_h, E_h, I_h, R_h
- Solid arrows indicate transitions: S_h -> E_h, E_h -> I_h, I_h -> R_h
- A curved solid arrow from R_h loops back to S_h.

**Mosquitoes Compartment:**
- Boxes (from left to right): S_v, E_v, I_v
- Solid arrows indicate transitions: S_v -> E_v, E_v -> I_v

**Interactions between Humans and Mosquitoes:**
- Dotted arrows indicate interactions:
  - From I_h (Humans) to S_v (Mosquitoes)
  - From I_h (Humans) to E_v (Mosquitoes)
  - From I_v (Mosquitoes) to S_h (Humans)
  - From I_v (Mosquitoes) to E_h (Humans)
: diagram::>

<a id='922d7f59-4b04-4ee1-9ede-57bb1955292a'></a>

Fig. 1 Susceptible humans, Sh, can be infected when they are bitten by infectious mosquitoes. They then progress through the exposed, Eh, infectious, Ih, and recovered, Rh, classes, before reentering the susceptible class. Susceptible mosquitoes, Sv, can become infected when they bite infectious or recovered humans. The infected mosquitoes then move through the exposed, Ev, and infectious, Iv, classes. Both species follow a logistic population model, with humans having additional immigration and disease-induced death. Birth, death, and migration into and out of the population are not shown in the figure.

<a id='77744dc0-eb74-4b8f-9066-19a188428daa'></a>

Table 1 The state variables for the original malaria model (1) and for the malaria model with scaled population sizes (2)

<a id='29794b70-7cad-49e2-a2e6-446f5db7b0d9'></a>

---Sh: Number of susceptible humans
Eh: Number of exposed humans
Ih: Number of infectious humans
Rh: Number of recovered (immune and asymptomatic, but slightly infectious) humans
Sv: Number of susceptible mosquitoes
Ev: Number of exposed mosquitoes
Iv: Number of infectious mosquitoes

<a id='daca67d6-876a-4034-b633-46637544f33c'></a>

e_h: Proportion of exposed humans
i_h: Proportion of infectious humans
r_h: Proportion of recovered (immune and asymptomatic, but slightly infectious) humans
N_h: Total human population
e_v: Proportion of exposed mosquitoes
i_v: Number of infectious mosquitoes
N_v: Total mosquito population

<a id='623e65cc-9c58-4a99-87ca-1c37afe19e97'></a>

$$\frac{d i_h}{d t} = \nu_h e_h - \left( \gamma_h + \delta_h + \psi_h + \frac{\Lambda_h}{N_h} \right) i_h + \delta_h i_h^2 \tag{2b}$$ 

$$\frac{d r_h}{d t} = \gamma_h i_h - \left( \rho_h + \psi_h + \frac{\Lambda_h}{N_h} \right) r_h + \delta_h i_h r_h \tag{2c}$$

<a id='def8d4a9-6914-48c7-81fa-84608aec30c3'></a>

$\frac{d N_h}{d t} = \Lambda_h + \psi_h N_h - (\mu_{1h} + \mu_{2h} N_h) N_h - \delta_h i_h N_h, \quad (2d)$

<a id='0fa159d4-df3d-4a02-9aa0-6b77cbbb5ea5'></a>

de_v / dt = (sigma_v sigma_h N_h / (sigma_v N_v + sigma_h N_h)) (beta_vh i_h + ~beta_vh r_h)(1 - e_v - i_v) - (nu_v + psi_v)e_v, (2e)

<!-- PAGE BREAK -->

<a id='9e01de5d-eeed-47bd-a545-d13346899fd9'></a>

1276

<a id='f6cad0db-d554-4459-8a44-d8d2873e3f43'></a>

Chitnis, Hyman, and Cushing

<a id='51c91456-3092-4723-9220-2556b13dc4fc'></a>

Table 2 The parameters for the malaria model (2) and their dimensions (Chitnis et al., 2006)

Λh: Immigration rate of humans. Humans × Time-1
ψη: Per capita birth rate of humans. Time-1
ψv: Per capita birth rate of mosquitoes. Time-1
σv: Number of times one mosquito would want to bite humans per unit time, if humans were freely available. This is a function of the mosquito's gonotrophic cycle (the amount of time a mosquito requires to produce eggs) and its anthropophilic rate (its preference for human blood). Time-1
ση: The maximum number of mosquito bites a human can have per unit time. This is a function of the human's exposed surface area and any vector control interventions used by the human to reduce exposure to mosquitoes. Time-1
βhv: Probability of transmission of infection from an infectious mosquito to a susceptible human given that a contact between the two occurs. Dimensionless
βvh: Probability of transmission of infection from an infectious human to a susceptible mosquito given that a contact between the two occurs. Dimensionless
β̃vh: Probability of transmission of infection from a recovered (asymptomatic carrier) human to a susceptible mosquito given that a contact between the two occurs. Dimensionless
vh: Per capita rate of progression of humans from the exposed state to the infectious state. 1/vh is the average duration of the latent period. Time-1
vv: Per capita rate of progression of mosquitoes from the exposed state to the infectious state. 1/vv is the average duration of the latent period. Time-1
γh: Per capita recovery rate for humans from the infectious state to the recovered state. 1/γh is the average duration of the infectious period. Time-1
δh: Per capita disease-induced death rate for humans. Time-1
ρh: Per capita rate of loss of immunity for humans. 1/ρh is the average duration of the immune period. Time-1
μ1h: Density independent part of the death (and emigration) rate for humans. Time-1
μ2h: Density dependent part of the death (and emigration) rate for humans. Humans−1 × Time−1
μ1v: Density independent part of the death rate for mosquitoes. Time-1
μ2v: Density dependent part of the death rate for mosquitoes. Mosquitoes−1 × Time−1

<a id='8019fbe3-67f8-4960-ad48-73eb2ed72d27'></a>

$$\frac{di_v}{dt} = \nu_v e_v - \psi_v i_v, \quad (2f)$$

$$\frac{dN_v}{dt} = \psi_v N_v - (\mu_{1v} + \mu_{2v} N_v) N_v, \quad (2g)$$

<a id='3e6abbbc-3021-4e98-b709-84401d7155bc'></a>

where the new state variables are also described in Table 1.

In this model, $\sigma_v$ is the rate at which a mosquito would like to bite a human, and $\sigma_h$ is the maximum number of bites that a human can have per unit time. Then $\sigma_v N_v$ is the total number of bites that the mosquitoes would like to achieve in unit time and $\sigma_h N_h$ is the availability of humans. The total number of mosquito-human contacts is half the harmonic mean of $\sigma_v N_v$ and $\sigma_h N_h$. The exposed classes, $e_h$ and $e_v$, model the delay before infected humans and mosquitoes become infectious. While in humans, this period is short and its effect on transmission may be ignored, in mosquitoes, this delay is important because it is on the same order as their expected life span. Thus, many infected mosquitoes die before they become infectious.

<a id='9ad179e4-5f75-433b-8bd0-8e5f3e696ee7'></a>

The model also includes an immigration term into the susceptible class (that is, inde-
pendent of the total population size). This ignores the immigration of exposed, infectious,
and recovered humans. While the exposed period is short and there would, therefore, be

<!-- PAGE BREAK -->

<a id='3e50a46f-cc5c-4c78-9032-de7d4241ea41'></a>

Determining Important Parameters in the Spread of Malaria

<a id='acc908db-fdc5-4d39-b0a2-fcfe519f53fd'></a>

1277

<a id='f49d4718-9c75-41df-b7bf-234ac43d0bb7'></a>

few exposed humans, and sick infectious humans are less likely to travel; the exclusion of immigrating recovered humans is a simplifying assumption.

<a id='ff6a90fa-1049-485e-8d9e-2d449b2ac1c3'></a>

The recovered class captures the difference between infection and disease in malaria. In hyperendemic areas, most adults are immune in the sense that while they have the malaria parasite in their blood stream and are infectious to mosquitoes, they do not suffer from clinical malaria. In the model, infectious humans move to the recovered class at a constant per capita rate, where they are still infective to mosquitoes (but less infective than infectious humans) and do not suffer from additional disease-induced mortality. The model assumes that the recovered humans move back to the susceptible class at a constant per capita rate. This is a simplifying assumption because immunity in malaria is dependent on the inoculation rate. However, in the case where transmission levels are relatively stable, the inoculation rate would approach a constant value and, therefore, the rate of loss of immunity would also approach a constant value. As we conduct our sensitivity analyses around equilibrium points, this assumption is reasonable.

<a id='06e70674-280d-4f98-a800-5e0e264ab69b'></a>

The model (2) is epidemiologically and mathematically well posed in the domain,

<a id='f26720bf-0a4a-480b-acc6-9a8457ca639a'></a>

```
D = \left\{
  \begin{pmatrix}
    e_h \\
    i_h \\
    r_h \\
    N_h \\
    e_v \\
    i_v \\
    N_v
  \end{pmatrix}
  \in \mathbb{R}^7
  \middle|
  \begin{aligned}
    & e_h \ge 0, \\
    & i_h \ge 0, \\
    & r_h \ge 0, \\
    & e_h + i_h + r_h \le 1, \\
    & N_h > 0, \\
    & e_v \ge 0, \\
    & i_v \ge 0, \\
    & e_v + i_v \le 1, \\
    & N_v > 0
  \end{aligned}
\right\}
```
(3)

<a id='53489df0-031f-4b17-ac80-78ae13ee47f5'></a>

We denote points in D by x = (eh, ih, rh, Nh, ev, iv, Nv). This domain is valid epidemiologically as the scaled populations, eh, ih, rh, ev, and iv are all nonnegative and have sums over their species type that are less than or equal to 1. The human and mosquito populations, Nh and Nv, are positive. For initial conditions in D, the model (2) has a unique solution that exists and remains in D for all time t ≥ 0 (Chitnis et al., 2006, Theorem 2.1).

<a id='1f573f02-e64e-41aa-9f79-009ce45f5c50'></a>

Disease-free equilibrium points are steady state solutions where there is no disease.
We define the "*diseased*" classes as the human or mosquito populations that are either
exposed, infectious or recovered; that is, $e_h$, $i_h$, $r_h$, $e_v$, and $i_v$. The positive equilibrium
human and mosquito population sizes, in the absence of disease, for (2) are

<a id='5bda655c-ebae-4440-87df-edaed5d36574'></a>

N*h = \frac{(\psi_h - \mu_{1h}) + \sqrt{(\psi_h - \mu_{1h})^2 + 4\mu_{2h} \Lambda_h}}{2\mu_{2h}} \text{ and } N*_v = \frac{\psi_v - \mu_{1v}}{\mu_{2v}} \text{ (4)}

<a id='4be0a6b0-4072-4bfa-9ed7-ce1aa4140347'></a>

The model (2) has exactly one equilibrium point, $x_{dfe}$ = (0, 0, 0, $N_h^*$, 0, 0, $N_v^*$), with no disease in the population (in the intersection of $\mathcal{D}$ and the boundary of the positive orthant in $\mathbb{R}^7$) (Chitnis et al., **2006**, Theorem 3.1).

<a id='5cc7c73c-b869-4819-94f5-57836cd55ff3'></a>

The reproductive number, R₀, is the expected number of secondary infections that one infectious individual (human or mosquito) would create over the duration of the infectious period provided that all other members of both populations are susceptible,

<a id='d5b68109-cbf4-4d36-ba27-616fa11df079'></a>

$$R_0 = \sqrt{K_{vh}K_{hv}}$$ (5)

<!-- PAGE BREAK -->

<a id='9cc1c0fb-7025-497a-a230-9c88b5309b3d'></a>

1278

<a id='0e1f7123-cd60-40f4-a587-7df2fee65fff'></a>

Chitnis, Hyman, and Cushing

<a id='6d3440b9-3948-4645-8c08-b747cf4ae293'></a>

with,

$K_{hv} = \left(\frac{\nu_v}{\nu_v + \mu_{1v} + \mu_{2v}N_v^*}\right) \cdot \left(\frac{\sigma_v\sigma_h N_h^*}{\sigma_v N_v^* + \sigma_h N_h^*}\right) \cdot \beta_{hv} \cdot \left(\frac{1}{\mu_{1v} + \mu_{2v}N_v^*}\right)$ (6a)

$K_{vh} = \left(\frac{\nu_h}{\nu_h + \mu_{1h} + \mu_{2h}N_h^*}\right) \cdot \left(\frac{\sigma_v N_v^* \sigma_h}{\sigma_v N_v^* + \sigma_h N_h^*}\right) \cdot \left(\frac{1}{\gamma_h + \delta_h + \mu_{1h} + \mu_{2h}N_h^*}\right)$
$\times \left[\beta_{vh} + \tilde{\beta}_{vh} \left(\frac{\gamma_h}{\rho_h + \mu_{1h} + \mu_{2h}N_h^*}\right)\right]$ (6b)

<a id='a1c70b75-b6f3-4c43-bb8c-aac615c079e2'></a>

The disease-free equilibrium point, xdfe, is locally asymptotically stable if R₀ < 1 and unstable if R₀ > 1 (Chitnis et al., 2006), Theorem 3.3. Note that the number of new infections in humans that one human causes through his/her infectious period is R₀², not R₀. Because this definition of R₀ (5) is based on the next generation operator approach (Diekmann et al., 1990), it counts the number of new infections from one generation to the next. That is, the number of new infections in mosquitoes counts as one generation.

<a id='b9289a4f-63a9-4266-852c-df3e046df6d6'></a>

Endemic equilibrium points are steady state solutions where the disease persists in the population (all state variables are positive). Theorems 4.1 and 4.2 in Chitnis et al. (2006) state that there is a transcritical bifurcation at $R_0 = 1$, and there exists at least one endemic equilibrium point for all values of $R_0 > 1$. Typically in epidemiological models, bifurcations at $R_0 = 1$ tend to be supercritical (i.e., positive endemic equilibria exist for $R_0 > 1$ near the bifurcation point). Theorem 4.3 in Chitnis et al. (2006) states that in the absence of disease-induced death ($\delta_h = 0$), the transcritical bifurcation at $R_0 = 1$ is supercritical (forward). However, this model (2) can exhibit a subcritical bifurcation (i.e., positive endemic equilibria exist for $R_0 < 1$ near the bifurcation point) for some positive values of $\delta_h$.

<a id='f16f6166-4f83-4ff6-85ed-c13a5f06a4fc'></a>

3. Baseline parameter values

We show baseline values and ranges in Table 3 for the parameters described in Table 2. We include two sets of baseline values: one for areas of high transmission and one for low transmission (as measured by R₀). In Appendix A, we describe our reasons for using these values and give references where available. We estimate some parameter values from published studies and country-wide data. For location specific parameters, such as migration rates, we pick realistically feasible values. For parameters concerning human populations, we pick values representing villages, small towns, or small regions. We assume high transmission occurs in parts of Africa and low transmission occurs in Asia and the Americas. We use two significant figure accuracy for all the parameters.

<a id='4055c415-aa65-4888-8b87-95303cee7279'></a>

3.1. Low transmission

For the baseline parameters at low malaria transmission in Table 3, R₀ = 1.1 (corresponding to 1.3 new infections in humans from one infected human through the duration of the infectious (and recovered) period). There is only one locally asymptotically stable endemic equilibrium point in D,

<a id='90722047-ab5a-4f6c-859b-b19d995b904d'></a>

x_ee = (0.0029, 0.080, 0.10, 578, 0.024, 0.016, 2425).

(7)

<a id='d0ece930-8795-40e3-9133-c37045d46f2e'></a>

Figure 2 shows graphs of a typical solution of the model (1) in the original variables.

<!-- PAGE BREAK -->

<a id='b63cda19-13e3-4f69-b358-27d3998cd1ad'></a>

Determining Important Parameters in the Spread of Malaria

<a id='f19a5d74-99bf-4134-9f1a-5cd5dc12b44f'></a>

1279

<a id='ff2e8741-80ea-4ca9-83f6-0ba97d21490f'></a>

Table 3 Baseline values and ranges for parameters for the malaria model (2). Descriptions of the parameters are in Table 2 and explanations for the values are in Appendix A

<a id='9a7713a9-14c3-43f2-b6c0-cf154ad9a965'></a>

<table id="7-1">
<tr><td id="7-2"></td><td id="7-3">Dimension</td><td id="7-4">Baseline high</td><td id="7-5">Baseline low</td><td id="7-6">Range</td></tr>
<tr><td id="7-7">A</td><td id="7-8">Humans × Days-1</td><td id="7-9">0.033</td><td id="7-a">0.041</td><td id="7-b">0.0027-0.27</td></tr>
<tr><td id="7-c">ψh</td><td id="7-d">Days-1</td><td id="7-e">1.1 × 10-4</td><td id="7-f">5.5 × 10-5</td><td id="7-g">2.7 × 10-5-1.4 × 10-4</td></tr>
<tr><td id="7-h">ψv</td><td id="7-i">Days</td><td id="7-j">0.13</td><td id="7-k">0.13</td><td id="7-l">0.020-0.27</td></tr>
<tr><td id="7-m">συ</td><td id="7-n">Days</td><td id="7-o">0.50</td><td id="7-p">0.33</td><td id="7-q">0.10-1.0</td></tr>
<tr><td id="7-r">σh</td><td id="7-s">Days-1</td><td id="7-t">19</td><td id="7-u">4.3</td><td id="7-v">0.10-50</td></tr>
<tr><td id="7-w">βhv</td><td id="7-x">1</td><td id="7-y">0.022</td><td id="7-z">0.022</td><td id="7-A">0.010-0.27</td></tr>
<tr><td id="7-B">βvh</td><td id="7-C">1</td><td id="7-D">0.48</td><td id="7-E">0.24</td><td id="7-F">0.072-0.64</td></tr>
<tr><td id="7-G">βvh</td><td id="7-H">1</td><td id="7-I">0.048</td><td id="7-J">0.024</td><td id="7-K">0.0072-0.64</td></tr>
<tr><td id="7-L">vh</td><td id="7-M">Days-1</td><td id="7-N">0.10</td><td id="7-O">0.10</td><td id="7-P">0.067-0.20</td></tr>
<tr><td id="7-Q">̈̈v</td><td id="7-R">Days⁻¹</td><td id="7-S">0.091</td><td id="7-T">0.083</td><td id="7-U">0.029–0.33</td></tr>
<tr><td id="7-V">̈̈̈̈̈h</td><td id="7-W">Days⁻¹</td><td id="7-X">0.0035</td><td id="7-Y">0.0035</td><td id="7-Z">0.0014–0.017</td></tr>
<tr><td id="7-10">̈̈̈h</td><td id="7-11">Days⁻¹</td><td id="7-12">9.0 × 10⁻⁵</td><td id="7-13">1.8 × 10⁻⁵</td><td id="7-14">0–4.1 × 10⁻⁴</td></tr>
<tr><td id="7-15">̈̈h</td><td id="7-16">Days⁻¹</td><td id="7-17">5.5 × 10⁻⁴</td><td id="7-18">2.7 × 10⁻³</td><td id="7-19">1.1 × 10⁻²–5.5 × 10⁻⁵</td></tr>
<tr><td id="7-1a">̈̈̈h</td><td id="7-1b">Days⁻¹</td><td id="7-1c">1.6 × 10⁻⁵</td><td id="7-1d">8.8 × 10⁻⁶</td><td id="7-1e">1.0 × 10⁻⁶–1.0 × 10⁻³</td></tr>
<tr><td id="7-1f">μ2h</td><td id="7-1g">Humans⁻¹ x Days⁻¹</td><td id="7-1h">3.0 x 10⁻⁷</td><td id="7-1i">2.0 x 10⁻⁷</td><td id="7-1j">1.0 x 10⁻⁸-1.0 x 10⁻⁶</td></tr>
<tr><td id="7-1k">μ1v</td><td id="7-1l">Days⁻¹</td><td id="7-1m">0.033</td><td id="7-1n">0.033</td><td id="7-1o">0.0010-0.10</td></tr>
<tr><td id="7-1p">μ2v</td><td id="7-1q">Mosquitoes⁻¹ × Days⁻¹</td><td id="7-1r">2.0 x 10⁻⁵</td><td id="7-1s">4.0 x 10⁻⁵</td><td id="7-1t">1.0 x 10⁻⁶-1.0 x 10⁻³</td></tr>
</table>

<a id='f9435035-ced1-4480-b1da-949c24445a54'></a>

3.2. _High transmission_

For the baseline parameters at high malaria transmission in Table 3, R₀ = 4.4 (corresponding to 20 new infections in humans from one infected human through the duration of the infectious (and recovered) period). There is only one locally asymptotically stable endemic equilibrium point in D,

<a id='5470eed7-404b-435f-a3af-3accacb76c68'></a>

x_ee = (0.0059, 0.16, 0.77, 490, 0.15, 0.11, 4850). (8)
Figure 3 shows graphs of a typical solution of the model (1) in the original variables.

<a id='84a51ef9-c7b6-4f24-91b7-86e04f3f816a'></a>

## 4. Sensitivity analysis

In determining how best to reduce human mortality and morbidity due to malaria, it is necessary to know the relative importance of the different factors responsible for its transmission and prevalence. Initial disease transmission is directly related to R₀, and disease prevalence is directly related to the endemic equilibrium point, specifically to the magnitudes of eₕ, iₕ, rₕ, eᵥ, and iᵥ. These variables are relevant to the individuals (humans and mosquitoes) who have some life stage of Plasmodium in their bodies. The proportion of infectious humans, iₕ, is especially important because it represents the people who may be clinically ill, and is directly related to the total number of malarial deaths. We calculate the sensitivity indices of the reproductive number, R₀, and the endemic equilibrium point, xₑₑ, to the parameters in the model. These indices tell us how crucial each parameter is to disease transmission and prevalence. Sensitivity analysis is commonly used to determine the robustness of model predictions to parameter values (since there are usually errors in data collection and presumed parameter values). Here we use it to discover parameters that have a high impact on R₀ and xₑₑ, and should be targeted by intervention strategies.

<!-- PAGE BREAK -->

<a id='ab6efc43-b53d-41c5-a300-5d36de518f6e'></a>

1280

<a id='6f061068-0450-4c0c-911d-1a94ed54d05f'></a>

Chitnis, Hyman, and Cushing

<a id='79ea0ee8-a150-4640-8a79-376b07628c4e'></a>

<::chart: Four plots showing population dynamics over time. The plots are arranged in a 2x2 grid.::>Plot of human population against time:The top-left plot shows the number of people (Y-axis, from 0 to 60) against time in days (X-axis, from 0 to 10000). It includes three lines: Exposed humans (red dashed line, stays near 0), Infectious humans (blue solid line, rises to about 45), and Recovered humans (black dashed line, rises to about 55).Plot of human population against time:The top-right plot shows the number of people (Y-axis, from 480 to 600) against time in days (X-axis, from 0 to 10000). It shows one line: Susceptible humans (blue solid line, decreases from 600 to about 485).Plot of mosquito population against time:The bottom-left plot shows the number of mosquitoes (Y-axis, from 0 to 60) against time in days (X-axis, from 0 to 10000). It includes two lines: Exposed mosquitoes (red dashed line, rises to about 58) and Infectious mosquitoes (blue solid line, rises to about 37).Plot of mosquito population against time:The bottom-right plot shows the number of mosquitoes (Y-axis, from 2330 to 2410) against time in days (X-axis, from 0 to 10000). It shows one line: Susceptible mosquitoes (blue solid line, decreases from 2400 to about 2330).Fig. 2 Solution of the malaria model (1) with baseline parameter values defined in Table 3 for areas of low transmission. These parameters correspond to R0 = 1.1. The initial condition is Sh = 600, Eh = 20, Ih = 3, Rh = 0, Sv = 2400, Ev = 30, and Iv = 5. The system approaches the endemic equilibrium point (7).

<a id='070f03ce-050a-4024-91ee-d226e1bdb96c'></a>

### 4.1. Description of sensitivity analysis

Sensitivity indices allow us to measure the relative change in a state variable when a parameter changes. The normalized forward sensitivity index of a variable to a parameter is the ratio of the relative change in the variable to the relative change in the parameter. When the variable is a differentiable function of the parameter, the sensitivity index may be alternatively defined using partial derivatives.

<a id='753c4d0e-08bb-4f7c-b8a3-31d8d6b956d4'></a>

**Definition.** The normalized forward sensitivity index of a variable, *u*, that depends differentiably on a parameter, *p*, is defined as:

<a id='a8a4558e-21c7-4062-b4ae-848acd32ec32'></a>

$$\gamma_p^u := \frac{\partial u}{\partial p} \times \frac{p}{u} \quad (9)$$

<!-- PAGE BREAK -->

<a id='b03c747b-a860-4f80-a014-f85ed647eee7'></a>

Determining Important Parameters in the Spread of Malaria

<a id='daaf5246-cb92-48c9-aeaa-cd7aa295e925'></a>

1281

<a id='7730cd7b-1ce8-461b-b00d-922efd5e805b'></a>

<::chart::> Plot of human population against time. The x-axis represents Time (days), ranging from 0 to 1200. The y-axis represents Number of humans, ranging from 0 to 500. Four lines are plotted: a solid blue line for Susceptible humans, a dotted red line for Exposed humans, a dashed black line for Infectious humans, and a dash-dot magenta line for Recovered humans. The Susceptible human population starts at 500 and decreases rapidly before stabilizing at a low number. The Exposed human population starts near 0, peaks early, and then declines to near 0. The Infectious human population starts near 0, peaks around 200 days, and then slowly decreases. The Recovered human population starts at 0 and steadily increases, eventually leveling off around 400. Plot of mosquito population against time. The x-axis represents Time (days), ranging from 0 to 1200. The y-axis represents Number of mosquitoes, ranging from 0 to 5000. Three lines are plotted: a solid blue line for Susceptible mosquitoes, a dotted red line for Exposed mosquitoes, and a dashed black line for Infectious mosquitoes. The Susceptible mosquito population starts around 4000, decreases to a minimum around 200-300 days, and then slowly increases. The Exposed mosquito population starts near 0, peaks around 200-300 days, and then slowly decreases. The Infectious mosquito population starts near 0, peaks around 200-300 days, and then slowly decreases. Fig. 3 Solution of the malaria model (1) with baseline parameter values defined in Table 3 for areas of high transmission. These parameters correspond to R₀ = 4.4. The initial condition is Sₕ = 500, Eₕ = 10, Iₕ = 30, Rₕ = 0, Sᵥ = 4000, Eᵥ = 100, and Iᵥ = 50. The system approaches the endemic equilibrium point (8). <::/chart::>

<a id='8bcea87d-9341-4830-b199-08468c3001d3'></a>

We show a detailed example of evaluating these sensitivity indices in Appendix B.1.

<a id='025a64c7-05d4-44d4-88f4-a9cf8fe95927'></a>

4.2. *Sensitivity indices of R₀*

As we have an explicit formula for R₀ (5), we derive an analytical expression for the sensitivity of R₀, $Y^{R₀}_p = \partial R₀/\partial p \times p/R₀$, to each of the seventeen different parameters described in Table 2. For example, the sensitivity index of R₀ with respect to $β_{hv}$,

<a id='475461ca-fedf-4344-bf93-aa8751baef8a'></a>

$$\gamma_{\beta_{vh}}^{R_0} = \frac{\partial R_0}{\partial \beta_{vh}} \times \frac{\beta_{vh}}{R_0} = \frac{1}{2},$$

<a id='0c6c4438-a090-44a1-907a-53b0e74ab872'></a>

does not depend on any parameter values. Two important indices that also have an obvious structure are:

$\gamma_{\sigma_v}^{R_0} = \frac{\sigma_h N_h^*}{\sigma_v N_v^* + \sigma_h N_h^*}$ and $\gamma_{\sigma_h}^{R_0} = \frac{\sigma_v N_v^*}{\sigma_v N_v^* + \sigma_h N_h^*}$ (10)

<!-- PAGE BREAK -->

<a id='c28c42c2-241d-47c7-a705-747b5bd83a80'></a>

1282

<a id='721531e5-29ad-4836-9553-1e3b88153081'></a>

Chitnis, Hyman, and Cushing

<a id='fcdb85b3-84ce-4e2b-8c88-cbfd3b294924'></a>

Table 4 Sensitivity indices of R₀ (5) to parameters for the malaria model, evaluated at the baseline parameter values given in Table 3. The parameters are ordered from most sensitive to least. In both cases, of high and low transmission, the most sensitive parameter is the mosquito biting rate, σₗ, and the least sensitive parameter is the human rate of progression from the latent period, vₕ

<a id='268d1009-b235-4cde-95a8-89b18a16f032'></a>

<table id="10-1">
<tr><td id="10-2" colspan="3">Low transmission</td><td id="10-3" colspan="3">High transmission</td></tr>
<tr><td id="10-4"></td><td id="10-5">Parameter</td><td id="10-6">Sensitivity index</td><td id="10-7"></td><td id="10-8">Parameter</td><td id="10-9">Sensitivity index</td></tr>
<tr><td id="10-a">1</td><td id="10-b">σv</td><td id="10-c">+0.76</td><td id="10-d">1</td><td id="10-e">σv</td><td id="10-f">+0.80</td></tr>
<tr><td id="10-g">2</td><td id="10-h">βhv</td><td id="10-i">+0.50</td><td id="10-j">2</td><td id="10-k">βhv</td><td id="10-l">+0.50</td></tr>
<tr><td id="10-m">3</td><td id="10-n">ψv</td><td id="10-o">-0.46</td><td id="10-p">3</td><td id="10-q">ψv</td><td id="10-r">-0.39</td></tr>
<tr><td id="10-s">4</td><td id="10-t">Buh</td><td id="10-u">+0.44</td><td id="10-v">4</td><td id="10-w">Buh</td><td id="10-x">+0.34</td></tr>
<tr><td id="10-y">5</td><td id="10-z">Yh</td><td id="10-A">-0.43</td><td id="10-B">5</td><td id="10-C">μου</td><td id="10-D">-0.30</td></tr>
<tr><td id="10-E">6</td><td id="10-F">Vu</td><td id="10-G">+0.31</td><td id="10-H">6</td><td id="10-I">Yh</td><td id="10-J">-0.30</td></tr>
<tr><td id="10-K">7</td><td id="10-L">μευ</td><td id="10-M">-0.26</td><td id="10-N">7</td><td id="10-O">Vu</td><td id="10-P">+0.29</td></tr>
<tr><td id="10-Q">8</td><td id="10-R">ση</td><td id="10-S">+0.24</td><td id="10-T">8</td><td id="10-U">H2h</td><td id="10-V">+0.20</td></tr>
<tr><td id="10-W">9</td><td id="10-X">μ₂h</td><td id="10-Y">+0.15</td><td id="10-Z">9</td><td id="10-10">σh</td><td id="10-11">+0.20</td></tr>
<tr><td id="10-12">10</td><td id="10-13">Λh</td><td id="10-14">-0.10</td><td id="10-15">10</td><td id="10-16">ψh</td><td id="10-17">-0.18</td></tr>
<tr><td id="10-18">11</td><td id="10-19">μ₁v</td><td id="10-1a">-0.088</td><td id="10-1b">11</td><td id="10-1c">βvh</td><td id="10-1d">+0.16</td></tr>
<tr><td id="10-1e">12</td><td id="10-1f">ψh</td><td id="10-1g">-0.081</td><td id="10-1h">12</td><td id="10-1i">ρh</td><td id="10-1j">-0.12</td></tr>
<tr><td id="10-1k">13</td><td id="10-1l">βvh</td><td id="10-1m">+0.055</td><td id="10-1n">13</td><td id="10-1o">Λh</td><td id="10-1p">-0.10</td></tr>
<tr><td id="10-1q">14</td><td id="10-1r">ρh</td><td id="10-1s">-0.053</td><td id="10-1t">14</td><td id="10-1u">μ1v</td><td id="10-1v">-0.10</td></tr>
<tr><td id="10-1w">15</td><td id="10-1x">μ1h</td><td id="10-1y">+0.012</td><td id="10-1z">15</td><td id="10-1A">μ1h</td><td id="10-1B">+0.020</td></tr>
<tr><td id="10-1C">16</td><td id="10-1D">δh</td><td id="10-1E">-0.0025</td><td id="10-1F">16</td><td id="10-1G">δh</td><td id="10-1H">-0.012</td></tr>
<tr><td id="10-1I">17</td><td id="10-1J">vh</td><td id="10-1K">+0.00063</td><td id="10-1L">17</td><td id="10-1M">vh</td><td id="10-1N">+0.00086</td></tr>
</table>

<a id='4a1e6e3c-80ee-4f40-93ee-75718e2739a7'></a>

However, most of the expressions for the sensitivity indices are complex with little ob-
vious structure. We, therefore, evaluate the sensitivity indices at the baseline parameter
values given in Table 3. The resulting sensitivity indices of R0 to the seventeen different
parameters in the model for areas of high and low transmission are shown in Table 4.
We replace σv and σh by the parameters,

<a id='1de9483c-9d53-42b3-b59a-4e794ae4f791'></a>

$\zeta = \frac{\sigma_v \sigma_h}{\sigma_v N_v^* + \sigma_h N_h^*}$ and $\theta = \frac{\sigma_h}{\sigma_v}$. (11)

<a id='8a8840f1-7904-4c83-abe5-bcd5da88a9d0'></a>

The parameter ξ is an intrinsic measure of the number of mosquito bites on humans. By definition, it is the number of mosquito bites on humans, per human, per mosquito, at the disease-free equilibrium population sizes, per unit time. We can measure the sensitivity of R₀ with respect to ζ, keeping θ fixed, that is, allowing both σᵥ and σₕ to vary while keeping the ratio between them fixed. We find

<a id='97c0bfec-3163-4e12-8309-3698c0a35859'></a>

$$\gamma_{\zeta}^{R_0} = \gamma_{\sigma_v}^{R_0} + \gamma_{\sigma_h}^{R_0} = 1. \quad (12)$$

<a id='60ee17f9-c5c5-48e9-b596-c5039d1baefc'></a>

In both cases of high and low transmission, the most sensitive parameter is the mosquito biting rate, $\sigma_v$. Other important parameters include the probability of disease transmission from infectious mosquitoes to susceptible humans, $\beta_{hv}$, the mosquito birth rate, $\psi_v$, and the human to mosquito disease transmission probability, $\beta_{vh}$. Since $\Upsilon_{\sigma_v}^{R_0} = +0.76$ in areas of low transmission, decreasing (or increasing) $\sigma_v$ by 10% decreases (or increases) $R_0$ by 7.6%. Similarly, in either high or low transmission, as $\Upsilon_{\beta_{hv}}^{R_0} = +0.5$, increasing (or decreasing) $\beta_{hv}$ by 10% increases (or decreases) $R_0$ by 5%.

<a id='5fb532c1-1391-492a-8a1a-9a11e2d8993f'></a>

We see from (10) that both, $\gamma_{\sigma_v}^{\kappa_0}$ and $\gamma_{\sigma_h}^{\kappa_0}$ depend on the human and mosquito demographic parameters. Changing the equilibrium population size of either humans or

<!-- PAGE BREAK -->

<a id='9b78e637-689b-4796-a4f4-367b3b97ae07'></a>

Determining Important Parameters in the Spread of Malaria

<a id='782b9a3f-d377-4494-b49b-280697bef60f'></a>

1283

<a id='23dcdafe-96e1-454b-806d-c9454100c3cf'></a>

mosquitoes would affect the sensitivity indices for the human and mosquito biting rates. Thus, to estimate the importance of the human or mosquito biting rates, we would need good knowledge of the population demographic parameters. However, Y_ζ^{R_0} does not depend on the equilibrium population sizes and provides a good estimate of the impact of the mosquito-human biting rates. When ζ is considered as a parameter (with θ constant), Y_ζ^{R_0} is the largest sensitivity index. Thus, reducing the number of contacts between humans and mosquitoes, through a reduction in either or both, the frequency of mosquito blood meals, and the number of bites that a human will tolerate would have the largest effect on disease transmission.¹

<a id='defc349b-f700-4d13-9d5f-bad3c4bd9c6c'></a>

For almost all parameters, the sign of the sensitivity indices of R₀ (i.e., whether R₀ increases or decreases when a parameter increases) agrees with an intuitive expectation. The only possible exception is the mosquito birth rate, ψᵥ. For both, high and low transmission, the reproductive number decreases substantially as the mosquito birth rate increases. We would expect R₀ to increase because increasing ψᵥ increases the number of mosquitoes. Our explanation for this counterintuitive result is as follows. The mosquito death rate is assumed to be density dependent. As the birth rate increases and the number of mosquitoes increases, the death rate also increases because the environment can only support a certain number of mosquitoes (given food restrictions and so on). Therefore, the average lifespan of the mosquito also decreases. Mathematically, at equilibrium population size, the per capita birth rate, ψᵥ, is equal to the per capita death rate, μ₁ᵥ + μ₂ᵥN*. Thus, at equilibrium, ψᵥ is also the per capita death rate, and with an exponential distribution for the death rate, 1/ψᵥ is the expected lifespan of the mosquitoes. As the latent period of Plasmodium in mosquitoes is about the same as the lifespan of the mosquitoes, shortening the lifespan of the mosquito reduces the reproductive number because more infected mosquitoes die before they become infectious.

<a id='e3d9bb6f-5eaf-4293-b16c-eacdbcebdfa9'></a>

In summary, we see that any changes in $\psi_v$ have two opposite effects. On the one hand, increasing $\psi_v$ increases the number of mosquitoes which tends to increase $R_0$. On the other hand, increasing $\psi_v$ also decreases the mosquito lifespan which tends to reduce $R_0$. The values of the other parameters help determine which of these two effects is stronger. In both lists of baseline parameters that we use, the effect of the reduction of the mosquito lifespan is stronger and $R_0$ decreases for an increase in $\psi_v$.

<a id='0c3e3609-0cca-47c9-8a65-41c7a503fd50'></a>

Also, as the equilibrium mosquito population size changes, the total number of mosquito bites on humans changes. Whether this change increases or decreases R0 depends on the values of the mosquito and human equilibrium population sizes, and σv and σh.

<a id='1936b496-59ee-410f-8b2a-5404abd3f0ff'></a>

We should expect, however, that for other parameter values, it is possible for R₀ to increase when ψᵥ increases. For one such example, we evaluate the sensitivity indices for R₀ with parameter values exactly as in Table 3 for low transmission, except for μ₁ᵥ = 0.123 (instead of μ₁ᵥ = 0.033). The equilibrium mosquito population for these parameters is N* = 175 and the most sensitive parameters are: γᴿ⁰μ₁ᵥ = -8.4, γᴿ⁰ψᵥ = +8.1, and γᴿ⁰δᵥ = +0.98. Thus, when there are few mosquitoes, R₀ increases when ψᵥ increases. Note that in models where the mosquito death rate is assumed to be constant, any decrease in the emergence of mosquitoes would tend to reduce R₀.

<a id='d603fa7c-85e0-4fc6-babe-493090580926'></a>

--- 

¹ Although it is not feasible to directly impact the mosquito's gonotrophic cycle, control strategies that reduce the human-biting rate, \u03c3h, would also reduce the mosquito's chances of feeding successfully, forcing it to search for another blood meal, thereby reducing the mosquito-biting rate, \u03c3v.

<!-- PAGE BREAK -->

<a id='7c5fccad-567f-4c0d-8672-f770eea950a0'></a>

1284

<a id='3efaf02b-3dcc-4c9e-8503-9f4bedfa3217'></a>

Chitnis, Hyman, and Cushing

<a id='5b418881-f8ba-4272-9026-1b9e101bb856'></a>

4.3. Sensitivity indices of $x_{ee}$

Since we do not have an explicit expression for the endemic equilibrium, $x_{ee}$, we cannot derive analytical expressions for the sensitivity indices. However, we numerically calculate the sensitivity indices at the parameter values given in Table 3 as shown in Appendix B. In a similar manner, we also calculate the sensitivity indices of $x_{ee}$ with respect to $\zeta$ (11) while keeping $\theta$ constant. We show the resulting sensitivity indices of the state variables at the endemic equilibrium point, $x_{ee}$, to the parameters for areas of low and high transmission in Tables 5 and 6, respectively. All sensitivity indices, except for some for $N_v$, are shown to two significant figures because that was the accuracy of the parameters. The sensitivity indices for $N_v$ can be calculated analytically as we have an explicit expression for the equilibrium value of the number of mosquitoes. We show an example in Appendix B.1.

<a id='ccf37543-52d5-4a9e-9b70-864788076887'></a>

In interpreting the sensitivity indices, we first note that keeping all other factors fixed, increasing disease prevalence will lead to a decrease in the equilibrium human population size. This is because of disease-induced death in infectious humans. Similarly, reducing the disease prevalence will lead to an increase in the equilibrium human population size.

<a id='6511ce41-fb1b-4c85-a52b-cc69aa73b295'></a>

In areas of low transmission, the order of the relative sensitivity of the different parameters for the equilibrium value of i_h is largely similar to that for R_0. As the reproductive number is based on a linearization around the disease-free equilibrium, x_dfe, and the endemic equilibrium in areas of low transmission is close to x_dfe (because R_0 is close to 1), the sensitivity indices are similar to those for R_0. The most sensitive parameter is the mosquito biting rate, σ_v, followed by the mosquito to human disease transmission probability, β_hv, and the human recovery rate, γ_h. Other important parameters include the

<a id='42687dda-e3b0-4f0c-8b80-8cae5410a10b'></a>

Table 5 The sensitivity indices, $\gamma^{x_i}_{p_j} = (\partial x_i / \partial p_j) \times (p_j / x_i)$, of the state variables at the endemic equi-librium, $x_i$, to the parameters, $p_j$, for baseline parameter values for areas of low transmission given in Table 3, measure the relative change in the solution to changes in the parameters
<table id="12-1">
<tr><td id="12-2"></td><td id="12-3">eh</td><td id="12-4">ih</td><td id="12-5">rh</td><td id="12-6">Nh</td><td id="12-7">eᵥ</td><td id="12-8">iᵥ</td><td id="12-9">Nᵥ</td></tr>
<tr><td id="12-a">Λh</td><td id="12-b">-0.80</td><td id="12-c">-0.81</td><td id="12-d">-0.83</td><td id="12-e">+0.39</td><td id="12-f">-0.69</td><td id="12-g">-0.69</td><td id="12-h">0</td></tr>
<tr><td id="12-i">ψh</td><td id="12-j">-0.62</td><td id="12-k">-0.63</td><td id="12-l">-0.64</td><td id="12-m">+0.30</td><td id="12-n">-0.54</td><td id="12-o">-0.54</td><td id="12-p">0</td></tr>
<tr><td id="12-q">ψv</td><td id="12-r">-3.4</td><td id="12-s">-3.4</td><td id="12-t">-3.4</td><td id="12-u">+0.026</td><td id="12-v">-4.1</td><td id="12-w">-5.1</td><td id="12-x">+1.3</td></tr>
<tr><td id="12-y">σv</td><td id="12-z">+5.7</td><td id="12-A">+5.7</td><td id="12-B">+5.7</td><td id="12-C">-0.044</td><td id="12-D">+6.2</td><td id="12-E">+6.2</td><td id="12-F">0</td></tr>
<tr><td id="12-G">σh</td><td id="12-H">+1.8</td><td id="12-I">+1.8</td><td id="12-J">+1.8</td><td id="12-K">-0.014</td><td id="12-L">+2.0</td><td id="12-M">+2.0</td><td id="12-N">0</td></tr>
<tr><td id="12-O">βhv</td><td id="12-P">+3.9</td><td id="12-Q">+3.9</td><td id="12-R">+3.9</td><td id="12-S">-0.030</td><td id="12-T">+3.7</td><td id="12-U">+3.7</td><td id="12-V">0</td></tr>
<tr><td id="12-W">βvh</td><td id="12-X">+3.3</td><td id="12-Y">+3.3</td><td id="12-Z">+3.3</td><td id="12-10">-0.026</td><td id="12-11">+4.0</td><td id="12-12">+4.0</td><td id="12-13">0</td></tr>
<tr><td id="12-14">βvh</td><td id="12-15">+0.41</td><td id="12-16">+0.41</td><td id="12-17">+0.41</td><td id="12-18">-0.0032</td><td id="12-19">+0.50</td><td id="12-1a">+0.50</td><td id="12-1b">0</td></tr>
<tr><td id="12-1c">vh</td><td id="12-1d">-0.98</td><td id="12-1e">+0.019</td><td id="12-1f">+0.019</td><td id="12-1g">-0.00014</td><td id="12-1h">+0.018</td><td id="12-1i">+0.018</td><td id="12-1j">0</td></tr>
<tr><td id="12-1k">νυ</td><td id="12-1l">+2.4</td><td id="12-1m">+2.4</td><td id="12-1n">+2.4</td><td id="12-1o">-0.018</td><td id="12-1p">+1.9</td><td id="12-1q">+2.9</td><td id="12-1r">0</td></tr>
<tr><td id="12-1s">Yh</td><td id="12-1t">-2.8</td><td id="12-1u">-3.8</td><td id="12-1v">-2.8</td><td id="12-1w">+0.029</td><td id="12-1x">-3.5</td><td id="12-1y">-3.5</td><td id="12-1z">0</td></tr>
<tr><td id="12-1A">δη</td><td id="12-1B">+0.0022</td><td id="12-1C">-0.0025</td><td id="12-1D">-0.0022</td><td id="12-1E">-0.0077</td><td id="12-1F">-0.0042</td><td id="12-1G">-0.0042</td><td id="12-1H">0</td></tr>
<tr><td id="12-1I">Ph</td><td id="12-1J">+0.059</td><td id="12-1K">+0.059</td><td id="12-1L">-0.90</td><td id="12-1M">-0.00046</td><td id="12-1N">-0.045</td><td id="12-1O">-0.045</td><td id="12-1P">0</td></tr>
<tr><td id="12-1Q">μ1h</td><td id="12-1R">+0.092</td><td id="12-1S">+0.091</td><td id="12-1T">+0.090</td><td id="12-1U">-0.048</td><td id="12-1V">+0.076</td><td id="12-1W">+0.076</td><td id="12-1X">0</td></tr>
<tr><td id="12-1Y">2h</td><td id="12-1Z">+1.2</td><td id="12-20">+1.2</td><td id="12-21">+1.2</td><td id="12-22">-0.63</td><td id="12-23">+1.0</td><td id="12-24">+1.0</td><td id="12-25">0</td></tr>
<tr><td id="12-26">1v</td><td id="12-27">-0.69</td><td id="12-28">-0.69</td><td id="12-29">-0.69</td><td id="12-2a">+0.0053</td><td id="12-2b">-0.58</td><td id="12-2c">-0.58</td><td id="12-2d">-0.34</td></tr>
<tr><td id="12-2e">2v</td><td id="12-2f">-2.0</td><td id="12-2g">-2.0</td><td id="12-2h">-2.0</td><td id="12-2i">+0.016</td><td id="12-2j">-1.7</td><td id="12-2k">-1.7</td><td id="12-2l">-1</td></tr>
<tr><td id="12-2m">ζ</td><td id="12-2n">+7.6</td><td id="12-2o">+7.6</td><td id="12-2p">+7.6</td><td id="12-2q">-0.059</td><td id="12-2r">+8.2</td><td id="12-2s">+8.2</td><td id="12-2t">0</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='7a46bc6c-a3b8-4fcc-9210-8d04c17b63be'></a>

Determining Important Parameters in the Spread of Malaria

<a id='30bb28b3-91c0-46e1-a07c-94249ed4f7bf'></a>

1285

<a id='29512a29-2f4c-42e4-b142-e4422f7f4d73'></a>

**Table 6** The sensitivity indices, $\Gamma^{x_i}_{p_j} = (\partial x_i/\partial p_j) \times (p_j/x_i)$, of the state variables at the endemic equilibrium, $x_i$, to the parameters, $p_j$, for baseline parameter values for areas of high transmission given in Table 3, measure the relative change in the solution to changes in the parameters

<a id='0bbf76de-1f7e-4436-ae5e-7418837e7966'></a>

<table id="13-1">
<tr><td id="13-2"></td><td id="13-3">eh</td><td id="13-4">ih</td><td id="13-5">rh</td><td id="13-6">Nh</td><td id="13-7">e_v</td><td id="13-8">i_v</td><td id="13-9">N_v</td></tr>
<tr><td id="13-a">Λh</td><td id="13-b">+0.049</td><td id="13-c">+0.036</td><td id="13-d">-0.028</td><td id="13-e">+0.31</td><td id="13-f">+0.059</td><td id="13-g">+0.059</td><td id="13-h">0</td></tr>
<tr><td id="13-i">ψh</td><td id="13-j">+0.080</td><td id="13-k">+0.060</td><td id="13-l">-0.045</td><td id="13-m">+0.51</td><td id="13-n">+0.097</td><td id="13-o">+0.097</td><td id="13-p">0</td></tr>
<tr><td id="13-q">ψv</td><td id="13-r">-0.032</td><td id="13-s">-0.032</td><td id="13-t">-0.033</td><td id="13-u">+0.0021</td><td id="13-v">-0.56</td><td id="13-w">-1.6</td><td id="13-x">+1.3</td></tr>
<tr><td id="13-y">σv</td><td id="13-z">+0.094</td><td id="13-A">+0.094</td><td id="13-B">+0.095</td><td id="13-C">-0.0062</td><td id="13-D">+0.66</td><td id="13-E">+0.66</td><td id="13-F">0</td></tr>
<tr><td id="13-G">σh</td><td id="13-H">+0.024</td><td id="13-I">+0.024</td><td id="13-J">+0.025</td><td id="13-K">-0.0016</td><td id="13-L">+0.17</td><td id="13-M">+0.17</td><td id="13-N">0</td></tr>
<tr><td id="13-O">βhv</td><td id="13-P">+0.068</td><td id="13-Q">+0.068</td><td id="13-R">+0.069</td><td id="13-S">-0.0045</td><td id="13-T">+0.050</td><td id="13-U">+0.050</td><td id="13-V">0</td></tr>
<tr><td id="13-W">βvh</td><td id="13-X">+0.034</td><td id="13-Y">+0.034</td><td id="13-Z">+0.034</td><td id="13-10">-0.0022</td><td id="13-11">+0.52</td><td id="13-12">+0.52</td><td id="13-13">0</td></tr>
<tr><td id="13-14">β̃vh</td><td id="13-15">+0.017</td><td id="13-16">+0.017</td><td id="13-17">+0.017</td><td id="13-18">-0.0011</td><td id="13-19">+0.26</td><td id="13-1a">+0.26</td><td id="13-1b">0</td></tr>
<tr><td id="13-1c">vh</td><td id="13-1d">-0.99</td><td id="13-1e">+0.0063</td><td id="13-1f">+0.0064</td><td id="13-1g">-0.00041</td><td id="13-1h">+0.0046</td><td id="13-1i">+0.0046</td><td id="13-1j">0</td></tr>
<tr><td id="13-1k">νυ</td><td id="13-1l">+0.040</td><td id="13-1m">+0.040</td><td id="13-1n">+0.040</td><td id="13-1o">-0.0026</td><td id="13-1p">-0.38</td><td id="13-1q">+0.62</td><td id="13-1r">0</td></tr>
<tr><td id="13-1s">Yh</td><td id="13-1t">+0.078</td><td id="13-1u">-0.86</td><td id="13-1v">+0.13</td><td id="13-1w">+0.057</td><td id="13-1x">-0.39</td><td id="13-1y">-0.39</td><td id="13-1z">0</td></tr>
<tr><td id="13-1A">δη</td><td id="13-1B">+0.012</td><td id="13-1C">-0.0094</td><td id="13-1D">+0.0040</td><td id="13-1E">-0.065</td><td id="13-1F">-0.014</td><td id="13-1G">-0.014</td><td id="13-1H">0</td></tr>
<tr><td id="13-1I">Ph</td><td id="13-1J">+0.61</td><td id="13-1K">+0.61</td><td id="13-1L">-0.16</td><td id="13-1M">-0.040</td><td id="13-1N">+0.26</td><td id="13-1O">+0.26</td><td id="13-1P">0</td></tr>
<tr><td id="13-1Q">μι</td><td id="13-1R">+0.010</td><td id="13-1S">+0.0087</td><td id="13-1T">+0.0018</td><td id="13-1U">-0.075</td><td id="13-1V">-0.0068</td><td id="13-1W">-0.0068</td><td id="13-1X">0</td></tr>
<tr><td id="13-1Y"≯₂h</td><td id="13-1Z">+0.092</td><td id="13-20">+0.080</td><td id="13-21">+0.016</td><td id="13-22">-0.69</td><td id="13-23">-0.062</td><td id="13-24">-0.062</td><td id="13-25">0</td></tr>
<tr><td id="13-26"≯₁v</td><td id="13-27">-0.015</td><td id="13-28">-0.015</td><td id="13-29">-0.015</td><td id="13-2a">+0.00098</td><td id="13-2b">+0.041</td><td id="13-2c">+0.041</td><td id="13-2d">-0.34</td></tr>
<tr><td id="13-2e"≯₂v</td><td id="13-2f">-0.043</td><td id="13-2g">-0.043</td><td id="13-2h">-0.044</td><td id="13-2i">+0.0029</td><td id="13-2j">+0.12</td><td id="13-2k">+0.12</td><td id="13-2l">-1</td></tr>
<tr><td id="13-2m"≯</td><td id="13-2n">+0.12</td><td id="13-2o">+0.12</td><td id="13-2p">+0.12</td><td id="13-2q">-0.0078</td><td id="13-2r">+0.83</td><td id="13-2s">+0.83</td><td id="13-2t">0</td></tr>
</table>

<a id='9e888451-71db-41af-843a-f07d05bf6e67'></a>

mosquito birth rate, $\psi_v$, the human to mosquito disease transmission probability, $\beta_{vh}$, and the mosquito rate of progression from the latent state, $\nu_v$.

<a id='aea2964d-872c-44a1-afe5-7b1678c7dd93'></a>

Similar to the case for R₀, the magnitude of the sensitivity index of x_ee to ζ, γ^x_ee_ζ,
is larger than that for all other parameters. Thus, reducing the mosquito-human contacts
would have a large effect on disease prevalence at low transmission. Reducing ζ by 1%
would approximately reduce i_h by 7.6%.

<a id='de89725a-8b38-4955-a19f-0c0c47b1ec43'></a>

The sign of the sensitivity indices of the endemic equilibrium with respect to most of the parameters, for areas of low transmission, agrees with an intuitive expectation. The results that perhaps require some explanation are those for the mosquito birth rate, ψ_v, and the rate of loss of immunity, ρ_h. As explained in the section on the reproductive number, increasing the mosquito birth rate, given a density-dependent mosquito death rate, shortens the lifespan of the mosquito and results in a net decrease in the equilibrium proportion of infectious humans, i_h. Increasing ψ_v also affects the total number of mosquito bites on humans, which could further reduce i_h. As ρ_h increases, r_h decreases, which would tend to reduce disease prevalence. However, as a substantial fraction of people are in the recovered class, reducing the number of recovered people results in a redistribution of the population that increases the proportion of people in the exposed and infectious classes.

<a id='d4fce44e-1659-4466-bfa7-9d34818eca12'></a>

In areas of high transmission, the sensitivity of the endemic equilibrium to the parame-
ters is different from the sensitivity of R0 to the parameters. Since R0 is large, the endemic
equilibrium is far from the disease-free equilibrium. The magnitude of the sensitivity in-
dices for the endemic equilibrium in high transmission is also much lower than in low
transmission, because as R0 increases, disease prevalence moves closer to 100% and even
for large changes in the parameter values, there are only small changes in the endemic
equilibrium.

<!-- PAGE BREAK -->

<a id='52f3304a-0848-45f6-b92b-b510c2c79b5d'></a>

1286

<a id='d73c00ba-a46f-49e1-9984-671e48711924'></a>

Chitnis, Hyman, and Cushing

<a id='7cb685d0-0a98-431a-aa14-b9d17beaa5c3'></a>

The most sensitive parameter for $i_h$ is $\gamma_h$ followed by $\rho_h$. As the infectious and recovered periods are long and about 94% of the people are in the diseased classes, any changes in the recovery rate or rate of loss of immunity will have a relatively large effect on the fraction of infectious humans. The rate of loss of immunity has a large effect on $i_h$ because as 77% of the people are in the recovered class, any increase will remove a large number of people from the recovered class. Since infection rates are high, most of these people will be absorbed into the other classes, especially the infectious class. (This effect is similar to and more pronounced than that seen in areas of low transmission. In areas of high transmission, the increase in $i_h$ is also strong enough to increase disease prevalence in mosquitoes.)

<a id='899a7754-4eb3-41a2-ab58-ed3f4a51f96f'></a>

Increases in the human demographic parameters, ψh, Λh, μ1h, and μ2h, change the equilibrium human population size which in turn changes the total number of mosquito bites on humans, resulting in substantial changes in ih. Increasing the death rates, μ1h and μ2h, decreases the human population, which leads to an increase in the number of mosquito bites per human, which increases ih. Similarly, increasing Λh and ψh increases the equilibrium human population which would tend to decrease ih. However, as the incoming population is in the susceptible class and the inoculation rate is high, most of these people will get infected and move through the exposed and infectious classes to the recovered class. The net result of increasing the number of humans entering the population is the reduction of the fraction of recovered humans and an increase in the proportion of humans in the other classes. Increasing ih also increases disease prevalence in mosquitoes. This effect is stronger than the decrease in mosquito disease prevalence due to a reduction in rh and an increase in Nh.

<a id='114e8e5d-1cfb-43b1-bc1b-98c91205a8e0'></a>

Other important parameters for $i_h$ in high transmission, are the mosquito biting rate,
${\sigma}_v$, followed by the mosquito to human disease transmission probability, ${\beta}_{hv}$, the rate of
progression from the exposed state for mosquitoes, ${\nu}_v$, and the density-dependent mos-
quito death rate, ${\mu}_{2v}$. These are also most important parameters for $R_0$ and for the endemic
equilibrium in areas of low transmission. Again, when $\xi$ is considered as a parameter, it
has a large effect on the equilibrium value of $i_h$.

<a id='a18877ad-3817-49e2-8f93-20c15dbd809b'></a>

For both sets of parameter values, we find that $\Gamma_{\zeta}^{xee} = \Gamma_{\sigma_v}^{xee} + \Gamma_{\sigma_h}^{xee}$, although we cannot prove this relationship in general.

<a id='a51514e0-dab5-4a6e-a6a1-e34adbfb5c10'></a>

## 5. Discussion and conclusion

We analyzed a malaria model (Chitnis et al., 2006) by evaluating the sensitivity indices of the reproductive number, R₀, and the endemic equilibrium, xₑₑ, to model parameters. We did this for two sets of baseline values: one representing areas of high transmission and one representing areas of low transmission. Since R₀ is a measure of initial disease transmission, and xₑₑ represents disease prevalence, these sensitivity indices allow us to determine the relative importance of different parameters in malaria transmission and prevalence.

<a id='8d06b00e-9bb4-4f78-ad33-7c73a69b57d9'></a>

In areas of low transmission, the most important parameter for initial disease trans-
mission is the mosquito biting rate, $\sigma_v$. Other important parameters are the mosquito-to-
human disease transmission probability, $\beta_{hv}$, the mosquito birth rate, $\psi_v$, the human-to-
mosquito disease transmission probability, $\beta_{vh}$, and the human rate of recovery, $\gamma_h$. These
five parameters are also the most important parameters for equilibrium disease prevalence,

<!-- PAGE BREAK -->

<a id='43fe7ece-1af1-4854-a226-b3707762b857'></a>

Determining Important Parameters in the Spread of Malaria

<a id='d9efe908-3d1e-447e-ba9e-0e1904c1f4f8'></a>

1287

<a id='f6362025-c004-429c-b4c5-01984a27cd97'></a>

although $\gamma_h$ is in this case more important than $\psi_v$ and $\beta_{vh}$. If we consider $\xi$ as a parameter (with $\theta$ fixed), it would be the most important parameter for both initial disease transmission and equilibrium disease prevalence.

<a id='1b5f7607-277d-4372-86db-53cd1ac8b8d4'></a>

In areas of high transmission, the most important parameter for initial disease transmission is the mosquito biting rate, $\sigma_v$. Other important parameters are the mosquito-to-human disease transmission probability, $\beta_{hv}$, the mosquito birth rate, $\psi_v$, the human-to-mosquito disease transmission probability, $\beta_{vh}$, the density-dependent mosquito death rate, $\mu_{2v}$, and the human rate of recovery, $\gamma_h$. The most important parameter for equilibrium disease prevalence is the human rate of recovery, $\gamma_h$. Other important parameters are the human rate of loss of immunity, $\rho_h$, the mosquito biting rate, $\sigma_v$, the human density-dependent death and emigration rate, $\mu_{2h}$, and the mosquito-to-human disease transmission probability, $\beta_{hv}$. If we consider $\zeta$ as a parameter, it is the most important parameter in initial disease transmission and the third most important parameter in equilibrium disease prevalence.

<a id='1032f4c4-1c29-49e7-8d66-a731bb34d1d7'></a>

Although intervention strategies cannot target σ_v directly, they can target ξ through lowering mosquito-human contacts. According to our model, for the set of parameters representing areas of low transmission, strategies that affect ξ would be the most effective at reducing initial malaria transmission and equilibrium disease prevalence. Strategies that reduce mosquito-human contacts, such as the use of insecticide-treated bed nets (ITN's) and indoor residual spraying (IRS) have been shown to be effective in field studies (Hawley et al., 2003; Sharma et al., 2005). These strategies would also be the most effective in reducing initial transmission in areas of high transmission.

<a id='455c06ad-1e71-4f61-ba7b-3ad2acccec0c'></a>

Our analysis also shows that intervention strategies that affect the human recovery rate, $\gamma_h$, would be the most effective in reducing equilibrium disease prevalence for the set of parameters representing areas of high transmission. The parameter $\gamma_h$ can be reduced through prompt and effective case management (PECM) which emphasizes quick and accurate diagnosis and consequent treatment of malaria. Our model shows these strategies to also be effective in reducing equilibrium disease prevalence in areas of low transmission and initial disease transmission in both low and high transmission areas.

<a id='2abe2a0c-f5f0-4296-91b1-2e14c434b77b'></a>

The second most important parameter for initial disease transmission and equilibrium disease prevalence in areas of low transmission and initial disease transmission in areas of high transmission is the probability of disease transmission from infectious mosquitoes to susceptible humans, β_hv. This parameter can be reduced through strategies such as intermittent preventive treatment (IPT) which has been shown to be effective in Tanzania (Massaga et al., 2003; Schellenberg et al., 2001).

<a id='bf6cc553-7176-4b20-a395-a491c3f19707'></a>

The second most important parameter for equilibrium disease prevalence in areas of high transmission is the human rate of loss of immunity, ph. This parameter cannot easily be targeted by current intervention strategies and represents a simplification of our model. The rate of loss of immunity is not well understood (Anderson and May, 1991) and is generally thought of as dependent on the prevailing incidence rate. However, where the incidence rate is constant over time (as it is in our model at equilibrium), the rate of loss of immunity may be assumed to be constant and we use reasonable estimates of this constant rate in high and low transmission. However, ph, representing a nonlinear process, remains difficult to directly control through an intervention strategy.

<a id='9745867a-f975-4a3b-8b3b-145057e27ea4'></a>

The mosquito birth rate, $\psi_v$, has a substantial effect on initial disease transmission in both high and low transmission areas and on equilibrium disease prevalence in low transmission areas. However, for the parameter values used in the model, this effect is

<!-- PAGE BREAK -->

<a id='83b4b9f8-3521-4807-a113-0017bb8be9ef'></a>

1288

<a id='0c68468b-d220-4d51-b3ee-19636555165b'></a>

Chitnis, Hyman, and Cushing

<a id='45980096-bc47-417b-bb5b-531aca0a9202'></a>

detrimental and contrary to common practice, such as the destruction of breeding sites. This detrimental effect depends on the assumption that the mosquito death rate is density- dependent, as decreasing the birth rate then leads to a longer life span for each mosquito.

<a id='d8b4fd29-aee0-4bfa-953f-66846809ac43'></a>

Another important parameter in initial disease transmission in high and low transmis-
sion areas and equilibrium disease prevalence in low transmission areas is the probability
of disease transmission from infectious humans to susceptible mosquitoes, ̘vh. This pa-
rameter can be reduced through current intervention strategies such as the use of gameto-
cytocidal drugs, or possible future strategies, such as the use of a transmission-blocking
vaccine or the release of transgenetically modified mosquitoes.

<a id='32f5dec5-a793-40d5-9be7-a3f0d4064679'></a>

The particular values of the sensitivity indices of the endemic equilibrium point, Xee,
and the reproductive number, R0, to the different parameters depend on the parameter
values that we have chosen, and on the assumptions upon which this model is based. To
effectively guide public policy and public health decision making, the model and para-
meter values would need to be tested against data from malaria-endemic field sites. The
current analysis, however, remains an important first step toward comparing the effective-
ness of different control strategies.

<a id='beda044c-45b4-4085-95b3-5962fca7e427'></a>

To compare control strategies with more certainty, there are numerous additions that we would like to make to our model. We want to include the effects of the incidence rate on the period of immunity, and age and spatial structure, both of which are important in the spread of malaria. We would also like to improve our entomological submodel by the addition of juvenile mosquito stages. We could then include the effects of seasonality and the environment on the number and life span of mosquitoes, and on the development of the parasite in the mosquito. An increase in ambient temperature, with high relative humidity and rainfall, increases the emergence rate of mosquitoes, lengthens the life span of adult mosquitoes, and reduces the latency period in mosquitoes; resulting in a multi-faceted increase in malaria transmission levels. Environmental effects and changes play an important role in malaria transmission (Zhou et al., 2004) and need to be taken into account.

<a id='04c90ab5-7cae-4a4c-afa3-6a654498c4ee'></a>

Finally, we would like to quantify the relationship between the parameters in our model and the intervention strategies used to control malaria. A quantitative relationship would then allow us to directly relate the cost of each strategy to the reduction in disease burden and allow for the definite comparison of the efficiency and cost-effectiveness of different intervention strategies on reducing malaria morbidity and mortality.

<a id='7d2f2d7a-e9e7-4fec-8b2b-bbcef38c4551'></a>

## Acknowledgements
The authors thank the United States National Science Foundation for the following grants: NSF DMS-0414212 and NSF DMS-0210474. This research has also been supported under the Department of Energy contract W-7405-ENG-36. The authors thank Leon Arriola, Alain Goriely, Joceline Lega, and Jia Li for their valuable discussions and comments; and an anonymous referee for many helpful suggestions.

<a id='6471eb09-8c72-4047-9003-0b5c59925c46'></a>

**Appendix A: Data for baseline parameter value**

This Appendix shows the tables of data and explanations for the baseline parameter values of the model (2) including references.

<!-- PAGE BREAK -->

<a id='944371eb-7f70-4500-bd82-7ed9cd8b3062'></a>

Determining Important Parameters in the Spread of Malaria

<a id='abedc8fc-7d5e-424d-a0e1-3208e2015a7f'></a>

1289

<a id='4c92a058-0a8b-4995-946e-8708700a28bf'></a>

Table A.1 Demographic data for countries with areas of high levels of malaria transmission. The unit for life expectancy is years and the unit for the birth rate is total births per 1,000 people per year. This table is current as of December 7, 2007

<a id='7e545319-a4ca-4807-a31c-dc31afaf3e30'></a>

<table id="17-1">
<tr><td id="17-2">Country</td><td id="17-3">Life expectancy</td><td id="17-4">Birth rate</td><td id="17-5"></td></tr>
<tr><td id="17-6">Botswana</td><td id="17-7">50.58</td><td id="17-8">23.17</td><td id="17-9">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-a">Congo, DR</td><td id="17-b">57.20</td><td id="17-c">42.96</td><td id="17-d">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-e">Kenya</td><td id="17-f">55.31</td><td id="17-g">38.94</td><td id="17-h">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-i">Malawi</td><td id="17-j">42.98</td><td id="17-k">42.09</td><td id="17-l">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-m">Zambia</td><td id="17-n">38.44</td><td id="17-o">40.78</td><td id="17-p">Central Intelligence Agency (2007)</td></tr>
</table>

<a id='08735853-8e3e-4b7f-867f-5a4461279b0f'></a>

Table A.2 Demographic data for countries with areas of low levels of malaria transmission. The unit for
life expectancy is years and the unit for the birth rate is total births per 1,000 people per year. This table is
current as of December 7, 2007
<table id="17-q">
<tr><td id="17-r">Country</td><td id="17-s">Life expectancy</td><td id="17-t">Birth rate</td><td id="17-u"></td></tr>
<tr><td id="17-v">Brazil</td><td id="17-w">72.24</td><td id="17-x">16.30</td><td id="17-y">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-z">India</td><td id="17-A">68.59</td><td id="17-B">22.69</td><td id="17-C">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-D">Indonesia</td><td id="17-E">70.16</td><td id="17-F">19.65</td><td id="17-G">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-H">Mexico</td><td id="17-I">75.63</td><td id="17-J">20.36</td><td id="17-K">Central Intelligence Agency (2007)</td></tr>
<tr><td id="17-L">Saudi Arabia</td><td id="17-M">75.88</td><td id="17-N">29.10</td><td id="17-O">Central Intelligence Agency (2007)</td></tr>
</table>

<a id='40134000-4b47-40b7-99ee-6104fecada62'></a>

Population data for humans: Table A.1 shows the life expectancy and birth rate estimates for the year 2007 for some African countries with areas of high malaria transmission. Using this data, we assume a birth rate of 40 births per year per 1,000 people so ψη = 40/365.25/1,000. We also assume an immigration rate of 12 people per year. We set values of µ₁h = 1.6 × 10⁻⁵ and µ2h = 3.0 × 10⁻⁷. These correspond to, in the absence of malaria, a life expectancy of 48 years and 4.2% of the population emigrating every year. The stable population size for these parameter values, in the absence of malaria is 523.

<a id='7d1d1ae1-cdac-49ea-a137-365572d3a936'></a>

Table A.2 shows the life expectancy and birth rate estimates for the year 2007 for some Asian and American countries with areas of low malaria transmission. Using this data, we assume a birth rate of 20 births per year per 1,000 people so ψh = 20/365.25/1, 000. We also assume an immigration rate of 15 people per year. We set values of μ1h = 8.8 × 10−6 and μ2h = 2.0 × 10−7. These correspond to, in the absence of malaria, a life expectancy of 70 years and 3.2% of the population emigrating every year. The stable population size for these parameter values, in the absence of malaria is 583.

<a id='c66c2143-9d58-47bf-b156-b45396aeea37'></a>

To determine the range of these parameters, we allow the immigration rate, A_h, to vary from 1 migrant per year to 100 migrants per year. This is a location specific parameter so it has a large range of values. We allow the birth rate to vary from 10 births per 1,000 people per year to 50 births per 1,000 people per year. We allow _1h and _2h to vary so that the minimum removal rate corresponds to a life expectancy of 80 years and no emigration, and the maximum removal rate corresponds to a life expectancy of 30 years and 33% annual emigration. The exact values of _1h and _2h, for a given life expectancy and emigration rate, would depend on the values of the immigration rate and the birth rate.

<a id='0a8a1b4c-443f-4f25-9af1-b21570b8c485'></a>

Population data for mosquitoes: We use the results for the mosquito birth rate calculated by Bri&#235;t (2002, Fig. 2) for An. gambiae to give us a rate of 130 new adult female

<!-- PAGE BREAK -->

<a id='e9c2cd16-c66e-424d-9cd1-861524521628'></a>

1290

<a id='c8b151b4-0677-4521-82fe-5f4da841a73c'></a>

Chitnis, Hyman, and Cushing

<a id='0ed8b7d6-b91c-4692-b43e-8b8a4c5f692b'></a>

Table A.3 Mosquito life expectancy data
<table id="18-1">
<tr><td id="18-2">Lifespan (days)</td><td id="18-3">Mosquito</td><td id="18-4"></td></tr>
<tr><td id="18-5">20</td><td id="18-6">An. balabacensis</td><td id="18-7">Slooff and Verdrager (1972)</td></tr>
<tr><td id="18-8">8.5</td><td id="18-9">An. coustani</td><td id="18-a">Garrett-Jones and Grab (1964)</td></tr>
<tr><td id="18-b">5.6</td><td id="18-c">An. funestus</td><td id="18-d">Krafsur and Garrett-Jones (1977)</td></tr>
<tr><td id="18-e">5.89</td><td id="18-f">An. funestus</td><td id="18-g">Gillies and Wilkes (1963)</td></tr>
<tr><td id="18-h">10.2</td><td id="18-i">An. funestus</td><td id="18-j">Garrett-Jones and Grab (1964)</td></tr>
<tr><td id="18-k">11.26</td><td id="18-l">An. gambiae</td><td id="18-m">Gilles and Wilkes (1965)</td></tr>
<tr><td id="18-n">15.4</td><td id="18-o">An. gambiae</td><td id="18-p">Garrett-Jones and Shidrawi (1969)</td></tr>
<tr><td id="18-q">8.0</td><td id="18-r">An. gambiae</td><td id="18-s">Garrett-Jones and Grab (1964)</td></tr>
<tr><td id="18-t">9</td><td id="18-u">An. gambiae</td><td id="18-v">Molineaux et al. (1979)</td></tr>
<tr><td id="18-w">3.6</td><td id="18-x">An. gambiae</td><td id="18-y">Zahar (1974)</td></tr>
<tr><td id="18-z">9</td><td id="18-A">An. minimus</td><td id="18-B">Khan and Talibi (1972)</td></tr>
<tr><td id="18-C">5.8</td><td id="18-D">An. nili</td><td id="18-E">Garrett-Jones and Grab (1964)</td></tr>
<tr><td id="18-F">7.1</td><td id="18-G">An. punctulatus</td><td id="18-H">Peters and Standfast (1960)</td></tr>
</table>

<a id='cf2c2e5c-aeea-478a-bbdb-d23aa2b8eb42'></a>

mosquitoes per day per 1,000 female mosquitoes. The stable equilibrium value of the mosquito population, N_v, varies depending on the location. For areas of high transmission, we use estimates derived from quarterly data for the average number of An. gambiae and An. funestus mosquitoes in a region of Western Kenya (Asembo) from Gimnig et al. (2003b). From this data, we use an estimate of 2 An. gambiae and 0.8 An. funestus mosquitoes per house. We also assume that there are 1.5 people per house (Gimnig et al. (2003a) state that in Asembo there are 17,000 people living in approximately 2,500 family compounds with about 3–5 houses per compound) and there are a total of about 5 times as many mosquitoes as are found in the houses. Given the size of the human population in the model and the mosquito birth rate, we set μ_1v = 0.033 and μ_2v = 2.0 × 10⁻⁵ so that there is a stable equilibrium value of 4,850 mosquitoes.

<a id='5c8f501b-222f-4c10-b1ae-6404ac411728'></a>

For areas with low transmission, we use the same mosquito birth rate and mosquito (density independent) death rate, as that for areas of high transmission, but a higher den- sity dependent death rate, μ2v = 4.0 × 10⁻⁵, to provide a stable equilibrium value of about 2,425 mosquitoes (half as many as in areas of high transmission).
Table A.3 shows different estimates for mosquito life expectancy.

<a id='306505ab-22ca-4571-87e9-fe7327781c50'></a>

Data for mosquito-human biting rates: The number of times a mosquito bites a human per day depends on the relative sizes of the mosquito and human populations, the mosquito's gonotrophic cycle (the number of days a mosquito requires to produce eggs before it searches for a blood meal again), the mosquito's anthropophilic rate (the mosquito's innate preference for human blood), and the number of bites that a human will tolerate per day (depending on the human's exposed surface area and any preventive measures the human takes to avoid being bitten).

<a id='00d485af-9a70-472e-ae80-b7d12ae0bdb5'></a>

The parameter, σv, models the mosquito's gonotrophic cycle and its anthropophilic rate. As we do not have data to differentiate between the effects of the anthropophilic rate and the relative sizes of the human and mosquito populations, we assign values to σv based on only the gonotrophic cycle. From Bloland et al. (2002), we use estimates of a gonotrophic cycle length of 3 days in areas of low transmission and 2 days in areas of high transmission (with the assumption that areas of high transmission have higher temperatures and humidity).

<a id='2341dc03-2431-46f6-8edc-df98c46f18f5'></a>

From Table A.4, which shows estimates from field studies for the average number of bites on humans per mosquito per day, we use an estimate of 0.40 bites on humans per

<!-- PAGE BREAK -->

<a id='d9a7dc64-a912-4d07-9962-a356a546282f'></a>

Determining Important Parameters in the Spread of Malaria

<a id='1e336ca1-adcc-42e0-9216-fda37c9f8e0b'></a>

1291

<a id='ac586bcc-d8db-49be-ba7e-7e1bacbc0815'></a>

Table A.4 Mosquito daily biting rate data.
<table id="19-1">
<tr><td id="19-2">Human bites per mosquito</td><td id="19-3">Mosquito</td><td id="19-4">Year(s)</td><td id="19-5">Location</td><td id="19-6"></td></tr>
<tr><td id="19-7">0.25</td><td id="19-8">An. balabacensis</td><td id="19-9">1964</td><td id="19-a">Khmer</td><td id="19-b">Slooff and Verdrager (1972)</td></tr>
<tr><td id="19-c">0.25</td><td id="19-d">An. gambiae</td><td id="19-e">1967</td><td id="19-f">Kankiya, Nigeria</td><td id="19-g">Garrett-Jones and Shidrawi (1969)</td></tr>
<tr><td id="19-h">0.13</td><td id="19-i">An. gambiae</td><td id="19-j">1967</td><td id="19-k">Khashm El Girba, Sudan</td><td id="19-l">Zahar (1974)</td></tr>
<tr><td id="19-m">0.44</td><td id="19-n">An. gambiae</td><td id="19-o">1972</td><td id="19-p">Garki, Nigeria</td><td id="19-q">Molineaux et al. (1979)</td></tr>
<tr><td id="19-r">0.47</td><td id="19-s">An. minimus</td><td id="19-t">1966-1967</td><td id="19-u">Bangladesh</td><td id="19-v">Khan and Talibi (1972)</td></tr>
<tr><td id="19-w">0.40</td><td id="19-x">An. punctulatus</td><td id="19-y">1957-1958</td><td id="19-z">Maprik, New Guinea</td><td id="19-A">Peters and Standfast (1960)</td></tr>
</table>

<a id='68196d92-56a1-4ea5-af92-e16c44ebc87f'></a>

Table A.5 Data for probability of transmission of infection from mosquitoes to humans
<table id="19-B">
<tr><td id="19-C">Probability of transmission</td><td id="19-D">Comments</td><td id="19-E"></td></tr>
<tr><td id="19-F">0.0223±0.0028</td><td id="19-G">Calculations from data from (Pull and Grab, 1974)</td><td id="19-H">Nedelman (1985)</td></tr>
<tr><td id="19-I">0.01</td><td id="19-J"></td><td id="19-K">Davidson and Draper (1953)</td></tr>
<tr><td id="19-L">0.015-0.026</td><td id="19-M"></td><td id="19-N">Pull and Grab (1974)</td></tr>
<tr><td id="19-O">0.06-0.27</td><td id="19-P">Children</td><td id="19-Q">Krafsur and Armstrong (1978)</td></tr>
<tr><td id="19-R">0.05-0.13</td><td id="19-S">Adults</td><td id="19-T">Krafsur and Armstrong (1978)</td></tr>
<tr><td id="19-U">0.012</td><td id="19-V">Village with relative highest mosquito density</td><td id="19-W">Nedelman (1984)</td></tr>
<tr><td id="19-X">0.086</td><td id="19-Y">Village with relative lowest mosquito density</td><td id="19-Z">Nedelman (1984)</td></tr>
</table>

<a id='826ade82-522d-479c-91a3-71d4527214be'></a>

mosquito per day in areas of high transmission and 0.25 bites on humans per mosquito per day in areas of low transmission, at the disease-free equilibrium population sizes. Based on these estimates and the values of σv, Nv*, and Nh*, we calculate σh to be 19 in areas of high transmission and 4.3 in areas of low transmission. These values are reasonable given the assumption that in areas of low transmission people suffer from fewer mosquito bites.

<a id='bdff0f67-f381-42a6-bcdb-025109c6a433'></a>

Data for βhv: Table A.5 shows the probability of transmission of infection from an infectious mosquito to a susceptible human given that a contact between the two occurs.
We use an estimate of βhv = 0.022 for both, areas of high and low transmission.

<a id='e882bb16-4abb-4d19-a3df-b7d86ed1492b'></a>

Data for βvh and β̃vh: Table A.6 shows the probability of transmission of infection from infectious humans to susceptible mosquitoes given that a contact between the two occurs. We use an estimate of βvh = 0.48 for areas of high transmission and βvh = 0.24 for areas of low transmission. We assume that the probability of transmission from recovered humans to susceptible mosquitoes is one tenth the probability of transmission from infectious humans (Ngwa and Shu, 2000), so β̃vh = 0.048 for areas of high transmission and β̃vh = 0.024 for areas of low transmission.

<a id='df7f225a-3847-4dc5-a487-1c6d940d2244'></a>

Data for $v_h$: We assume a latent period in humans of 10 days, for both baseline cases, from the data shown in Table A.7.

<a id='01816d6d-d6d1-463c-b426-cd8bf2755a69'></a>

Data for _v_v: We assume the latent period in mosquitoes to be 11 days in areas of high transmission and 12 days in areas of low transmission. Table A.8 shows some estimates for the latent period in mosquitoes.

<!-- PAGE BREAK -->

<a id='f4d0e0c1-2fc4-4bd4-89a2-b60eedce0ef5'></a>

1292

<a id='ca126956-b3ae-4efb-bc37-3049054c33ef'></a>

Chitnis, Hyman, and Cushing

<a id='daf045c3-2e3b-4bd7-bc6e-56c7f15e4f6d'></a>

Table A.6 Data for probability of transmission of infection from humans to mosquitoes
<table id="20-1">
<tr><td id="20-2">Probability of transmission</td><td id="20-3">Comments</td><td id="20-4"></td></tr>
<tr><td id="20-5">0.24</td><td id="20-6">P. falciparum to An. gambiae</td><td id="20-7">Muirhead-Thomson (1957)</td></tr>
<tr><td id="20-8">0.48</td><td id="20-9">P. falciparum</td><td id="20-a">Boyd (1949)</td></tr>
<tr><td id="20-b">0.51</td><td id="20-c">P. falciparum</td><td id="20-d">Draper (1953)</td></tr>
<tr><td id="20-e">0.47</td><td id="20-f">P. falciparum</td><td id="20-g">Draper (1953)</td></tr>
<tr><td id="20-h">0.09</td><td id="20-i">P. falciparum</td><td id="20-j">Draper (1953)</td></tr>
<tr><td id="20-k">0.64</td><td id="20-l">P. falciparum after 1-4 days of gametocytemia</td><td id="20-m">Smalley and Sinden (1977)</td></tr>
<tr><td id="20-n">0.072</td><td id="20-o">P. falciparum after 11-12 days of gametocytemia</td><td id="20-p">Smalley and Sinden (1977)</td></tr>
<tr><td id="20-q">0.48</td><td id="20-r">From a differential equation model</td><td id="20-s">Nedelman (1984)</td></tr>
<tr><td id="20-t">0.38</td><td id="20-u">From a vectorial capacity approximation</td><td id="20-v">Nedelman (1984)</td></tr>
</table>

<a id='c38d883b-02bd-4e8f-b5f4-7606045a6d67'></a>

Table A.7 Data for the latent period in humans measured in days
<table id="20-w">
<tr><td id="20-x">Latent period</td><td id="20-y">Plasmodium</td><td id="20-z"></td></tr>
<tr><td id="20-A">10-14</td><td id="20-B">P. ovale</td><td id="20-C">Molineaux and Gramiccia (1980)</td></tr>
<tr><td id="20-D">15-16</td><td id="20-E">P. malariae</td><td id="20-F">Molineaux and Gramiccia (1980)</td></tr>
<tr><td id="20-G">9-10</td><td id="20-H">P. falciparum</td><td id="20-I">Molineaux and Gramiccia (1980)</td></tr>
<tr><td id="20-J">5-15</td><td id="20-K"></td><td id="20-L">Oaks et al. (1991)</td></tr>
</table>

<a id='925ded6f-7858-4469-9e58-284ea75c6f11'></a>

Table A.8 Data for the latent period in mosquitoes measured in days
<table id="20-M">
<tr><td id="20-N">Latent period</td><td id="20-O">Plasmodium</td><td id="20-P">Mosquito</td><td id="20-Q">Temperature (°C)</td><td id="20-R"></td></tr>
<tr><td id="20-S">9</td><td id="20-T">P. vivax</td><td id="20-U">–</td><td id="20-V">25–27</td><td id="20-W">Anderson and May (1991)</td></tr>
<tr><td id="20-X">12</td><td id="20-Y">P. falciparum</td><td id="20-Z">–</td><td id="20-10">25–27</td><td id="20-11">Anderson and May (1991)</td></tr>
<tr><td id="20-12">11</td><td id="20-13">P. falciparum</td><td id="20-14">An. gambiae</td><td id="20-15">24</td><td id="20-16">Baker (1966)</td></tr>
<tr><td id="20-17">3-35</td><td id="20-18">P. vivax</td><td id="20-19">–</td><td id="20-1a">17–31</td><td id="20-1b">Macdonald (1957)</td></tr>
<tr><td id="20-1c">5-35</td><td id="20-1d">P. falciparum</td><td id="20-1e">--</td><td id="20-1f">20-33</td><td id="20-1g">Macdonald (1957)</td></tr>
</table>

<a id='7285e590-f4b1-4f90-ac77-b10be388deea'></a>

Table A.9 Data for the duration of the infectious period for humans in months
<table id="20-1h">
<tr><td id="20-1i">Infectious period</td><td id="20-1j">Plasmodium</td><td id="20-1k">Comments</td><td id="20-1l"></td></tr>
<tr><td id="20-1m">2</td><td id="20-1n">P. ovale</td><td id="20-1o"></td><td id="20-1p">Molineaux and Gramiccia (1980)</td></tr>
<tr><td id="20-1q">4</td><td id="20-1r">P. malariae</td><td id="20-1s"></td><td id="20-1t">Molineaux and Gramiccia (1980)</td></tr>
<tr><td id="20-1u">9.5</td><td id="20-1v">P. falciparum</td><td id="20-1w"></td><td id="20-1x">Molineaux and Gramiccia (1980)</td></tr>
<tr><td id="20-1y">12-24</td><td id="20-1z">P. falciparum</td><td id="20-1A">No treatment</td><td id="20-1B">Bloland and Williams (2002)</td></tr>
<tr><td id="20-1C">18-60</td><td id="20-1D">P.vivax</td><td id="20-1E">No treatment</td><td id="20-1F">Bloland and Williams (2002)</td></tr>
<tr><td id="20-1G">18-60</td><td id="20-1H">P. ovale</td><td id="20-1I">No treatment</td><td id="20-1J">Bloland and Williams (2002)</td></tr>
<tr><td id="20-1K">36-600</td><td id="20-1L">P. malariae</td><td id="20-1M">No treatment</td><td id="20-1N">Bloland and Williams (2002)</td></tr>
</table>

<a id='f7ee6f04-fe22-447b-9518-7faf4e570265'></a>

Data for $\gamma_h$: We use an estimated recovery period of 9.5 months in both areas of high and low transmission. Table A.9 shows some estimates of the duration of the infectious period in humans.

<a id='d5208f47-0272-4410-aba2-f7bad337b460'></a>

Data for $\delta_h$: The value of the disease-induced death rate varies across different regions, depending on the availability and quality of treatment facilities. Arudo et al. (2003) give the malaria mortality rate for all children under 5 years old in Asembo (a region in western

<!-- PAGE BREAK -->

<a id='fb2b9ff9-f427-4212-94e7-22e063c7beb0'></a>

Determining Important Parameters in the Spread of Malaria

<a id='ec119151-da81-4a34-a262-6db8962d15b5'></a>

1293

<a id='d4dcd617-9296-4088-82cf-579d676f5ae8'></a>

Kenya) as 32.9 deaths per year per 1,000 children. Although the data in Arudo et al. (2003) is sampled only from children under the age of five (as opposed to the general population) and includes all children (as opposed to only those that are infectious), we use it as an estimate for the per capita disease-induced death rate of infectious humans in the entire population. This assumption is reasonable because in areas of high malaria transmission like Asembo, almost all children are infectious ($I_h$) and most adults are immune ($R_h$). For areas of low transmission, we assume improved availability and quality of treatment facilities, so that the per capita disease-induced death rate is a fifth that of Asembo. We assume that the range of $\delta_h$ can vary from no disease-induced deaths to 150 deaths per year per 1,000 infectious humans.

<a id='d6e0d0ed-2897-44d1-8995-c1ff7a4642a3'></a>

Data for ρ_h: Immunity to malaria in humans is a complicated mechanism that is not completely understood. While it is generally believed that immunity is short-lived and requires repeated reinfection to sustain itself (Aron, 1988; Dietz et al., 1974), in an epidemic in Madagascar, after two malaria-free decades, older adults still had some protection to malaria when compared to younger adults with no previous malaria exposure (Deloron and Chougnet, 1992). The model (1) is based on the assumption that infected humans eventually lose their immunity to malaria and return to the susceptible class. This rate of loss of immunity is a nonlinear process that depends on the transmission rate. However, for ease of analysis, we make the simplifying assumption that immunity is lost at a constant rate. We allow the rate to be higher in areas of low transmission so that humans with less exposure are immune for shorter periods of time. The assumption of a constant rate of loss of immunity is reasonable if the level of malaria does not change significantly over time in the modeled area.

<a id='c379c313-adbb-4b5a-9da5-26e6af1ac31c'></a>

For areas of high transmission, we assume that the period of immunity lasts for 5 years, while in areas of low transmission, we assume that the period lasts for 1 year. We also assume that the range can vary from 3 months to 50 years.

<a id='0bf13054-199c-4ce0-94b1-17729e78abfe'></a>

## Appendix B: Calculation of sensitivity indices
In this Appendix, we describe the methods used to determine the sensitivity indices of the endemic equilibrium to the parameters. To calculate the indices, we first need to evaluate the partial derivatives of the state variables at the endemic equilibrium with respect to the parameters.

<a id='d1b02079-0639-4918-b6c9-99ee3ed5c087'></a>

For ease of notation, we label the seven state variables at the endemic equilibrium point ($e_h, i_h, ..., N_v$) by $x_1, x_2, ..., x_7$; the seventeen parameters ($\Lambda_h, \psi_h, ..., \mu_{2v}$) by $p_1, p_2, ..., p_{17}$; and the seven equilibrium equations of (2) by

<a id='7af1d4f5-e1ff-4c33-9e1f-cc8abd071465'></a>

g1(x1,..., x7; p1,..., p17) = 0,
:
g7(x1,..., x7; p1,..., p17) = 0.                                (B.1)

<a id='7908e765-c48c-4a9e-b2d7-006fcc2ddf2e'></a>

We want to evaluate ∂xi/∂pj, for 1 ≤ i ≤ 7 and 1 ≤ j ≤ 17 for both sets of parameter values in Table 3 (with the corresponding endemic equilibrium points given by (7) and (8)).

<!-- PAGE BREAK -->

<a id='94a7af8e-4042-4351-aabb-8df4b6f0eedf'></a>

1294

<a id='5c28c79d-47ee-4905-bf7d-e81ddf178c3a'></a>

Chitnis, Hyman, and Cushing

<a id='c19446bb-6cfe-4f8d-b7f3-03da5f66ea9f'></a>

Taking full derivatives of the seven equilibrium equations (B.1) with respect to the seventeen parameters, p_j, gives us 119 equations of the form,

<a id='e2cf3ab2-d1b6-44a0-986a-27c55ce0e612'></a>

$$\frac{dg_k}{dp_j} = \sum_{i=1}^{7} \left( \frac{\partial g_k}{\partial x_i} \frac{\partial x_i}{\partial p_j} \right) + \sum_{l=1}^{17} \left( \frac{\partial g_k}{\partial p_l} \frac{\partial p_l}{\partial p_j} \right) = 0 \quad (B.2)$$

<a id='dfba6965-cfda-4dba-b3d9-5dfb7b9ab577'></a>

for 1 ≤ k ≤ 7 and 1 ≤ j ≤ 17. However, ∂pₗ/∂pⱼ = 0 if l ≠ j so each equation in (B.2) reduces to

<a id='f337efaa-dae9-4b66-bb5d-466a4fd4f06f'></a>

$$\sum_{i=1}^{7} \frac{\partial g_k}{\partial x_i} \frac{\partial x_i}{\partial p_j} = -\frac{\partial g_k}{\partial p_j}. \quad (B.3)$$

<a id='0c1390dd-a5e0-4082-956f-95a975a4fd2b'></a>

These equations are decoupled in terms of the parameters, p_j, but are coupled in terms
of the function, g_k. Equations (B.3) are thus seventeen linear systems of seven coupled
equations. They may be written as

<a id='1e721c1b-9909-41a5-aec0-603efd4adb5c'></a>

Az^{(j)} = b^{(j)},                                                                     (B.4)

<a id='6b9133f3-43e1-45cc-b58c-325fec8e6b5e'></a>

where A is the (7 × 7) Jacobian of the malaria model (2) with A_ki = \partial g_k / \partial x_i; z^(j) is the unknown (7 × 1) vector with the i^th term of z^(j) given by \partial x_i / \partial p_j; and b^(j) is a (7 × 1) vector with the k^th term given by -\partial g_k / \partial p_j. The matrix A is known because we can evaluate the Jacobian of (2) for the given parameter values and the corresponding endemic equilibrium point. Similarly, we can directly evaluate b^(j) by calculating the derivative, -\partial g_k / \partial p_j, at the given parameter values.

<a id='7229995e-efd3-487b-875a-2377fd9202b2'></a>

Solving these seventeen linear systems of (B.4) for z$^{(j)}$ gives us what we want: $\partial x_i / \partial p_j$
for $1 \le i \le 7$ and $1 \le j \le 17$. Finally, we multiply $\partial x_i / \partial p_j$ by $p_j / x_i$, as in the definition
of the sensitivity index (9), to find the sensitivity of each state variable in the endemic
equilibrium point, $x_i$, to the parameter, $p_j$.

<a id='f0772d4a-b3f3-4759-952f-36fa1f09d753'></a>

B.1 _Sensitivity analysis of the equilibrium mosquito population_

<a id='1fee82f9-090b-4f57-af08-748478b82683'></a>

As we have an explicit expression for the equilibrium value of Nᵤ, we can analytically evaluate the sensitivity of Nᵤ, to the parameters. At equilibrium,

<a id='630f6057-2835-401b-98ed-0eb1b386990a'></a>

N_v = (psi_v - mu_1v) / mu_2v. (B.5)

<a id='c3b50136-45e9-4ddc-9e78-059a3865768e'></a>

As $N_v$ depends on only three parameters, the sensitivity indices of $N_v$ to all other parameters is 0. For example, the sensitivity index for $N_v$ to $\psi_v$ is

<a id='1a1c7742-2bb5-4d1c-9471-902a0f3bea80'></a>

\gamma^{\text{Nv}}_{\psi\text{v}} = \frac{\partial \text{Nv}}{\partial \psi\text{v}} \cdot \frac{\psi\text{v}}{\text{Nv}} = \frac{\psi\text{v}}{\psi\text{v} - \mu_{1\text{v}}}.

<a id='1b246576-9dfc-4563-81f8-6039f6dc80bb'></a>

For the baseline parameter values given in Table 3, for areas of high and low transmission, $\gamma^N_{\psi v} = +1.3$.

<!-- PAGE BREAK -->

<a id='7e82885a-8e7e-4cef-aa9c-84d81a038044'></a>

Determining Important Parameters in the Spread of Malaria

<a id='8f042f9d-cb28-4493-a42a-2689ecb1073f'></a>

1295

<a id='b44a25a6-349f-4124-b9d2-884a27cac7d1'></a>

References
Anderson, R.M., May, R.M., 1991. Infectious Diseases of Humans: Dynamics and Control. Oxford University Press, London.
Aron, J.L., 1988. Mathematical modeling of immunity to malaria. Math. Biosci. 90, 385-396.
Arudo, J., Gimnig, J.E., ter Kuile, F.O., Kachur, S.P., Slutsker, L., Kolczak, M.S., Hawley, W.A., Orago, A.S.S., Nahlen, B.L., Phillips-Howard, P.A., 2003. Comparison of government statistics and demographic surveillance to monitor mortality in children less than five years old in rural western Kenya. Am. J. Trop. Med. Hyg. 68 (Suppl. 4), 30-37.
Baker, J.R., 1966. Parasitic Protozoa. Hutchinson.
Bloland, P.B., Williams, H.A., Roundtable on the Demography of Forced Migration, and Joseph L. Mailman School of Public Health. Program on Forced Migration and Health 2002 Malaria Control During Mass Population Movements and Natural Disasters. National Academies Press.
Boyd, M.F., 1949. Epidemiology: Factors related to the definitive host. In: Boyd, M.F. (Ed.), Malariology, vol. 1, pp. 608-697. Saunders, Philadelphia.
Briët, O.J.T., 2002. A simple method for calculating mosquito mortality rates, correcting for seasonal variations in recruitment. Med. Vet. Entomol. 16, 22-27.
Central Intelligence Agency, CIA—The World Factbook, 2007. https://www.cia.gov/library/publications/the-world-factbook/index.html.
Chitnis, N., 2005. Using mathematical models in controlling the spread of malaria. Ph.D. thesis, University of Arizona, Tucson, Arizona, USA.
Chitnis, N., Cushing, J.M., Hyman, J.M., 2006. Bifurcation analysis of a mathematical model for malaria transmission. SIAM J. Appl. Math. 67, 24-45.
Davidson, G., Draper, C.C., 1953. Field study of some of the basic factors concerned in the transmission of malaria. Trans. Roy. Soc. Trop. Med. Hyg. 47, 522-535.
Deloron, P., Chougnet, C., 1992. Is immunity to malaria really short-lived? Parasitol. Today 8, 375-378.
Diekmann, O., Heesterbeek, J.A.P., Metz, J.A.J., 1990. On the definition and the computation of the basic reproduction ratio R0 in models for infectious diseases in heterogeneous populations. J. Math. Biol. 28, 365-382.
Dietz, K., Molineaux, L., Thomas, A., 1974. A malaria model tested in the African Savannah. Bull. World Health Organ. 50, 347-357.
Draper, C.C., 1953. Observations on the infectiousness of gametocytes in hyperendemic malaria. Trans. Roy. Soc. Trop. Med. Hyg. 47, 160-165.
Garrett-Jones, C., Grab, B., 1964. The assessment of insecticidal impact on the malaria mosquito's vectorial capacity, from data on the population of parous females. Bull. World Health Organ. 31, 71-86.
Garrett-Jones, C., Shidrawi, G.R., 1969. Malaria vectorial capacity of a population of Anopheles gambiae. Bull. World Health Organ. 40, 531-545.
Gillies, M.T., Wilkes, T.J., 1963. Observations on nulliparous and parous rates in a population of A. funestus in East Africa. Ann. Trop. Med. Parasitol. 57, 204-213.
Gillies, M.T., Wilkes, T.J., 1965. A study of the age composition of populations of Anopheles gambiae Giles and A. funestus Giles in north-eastern Tanzania. Bull. Entomol. Res. 56, 237-262.
Gimnig, J.E., Kolczak, M.S., Hightower, A.W., Vulule, J.M., Schoute, E., Kamau, L., Phillips-Howard, P.A., ter Kuile, F.O., Nahlen, B.L., Hawley, W.A., 2003a. Effect of permethrin-treated bed nets on the spatial distribution of malaria vectors in western Kenya. Am. J. Trop. Med. Hyg. 68 (Suppl. 4), 115-120.
Gimnig, J.E., et al., 2003b. Impact of permethrin-treated bed nets on entomologic indices in an area of intense year-round malaria transmission. Am. J. Trop. Med. Hyg. 68 (Suppl. 4), 16-22.
Hawley, W.A., et al., 2003. Implications of the western Kenya permethrin-treated bed net study for policy, program implementation, and future research. Am. J. Trop. Med. Hyg. 68 (Suppl. 4), 168-173.
Khan, A.Q., Talibi, S.A., 1972. Epidemiological assessment of malaria transmission in an endemic area of East Pakistan and the significance of congenital immunity. Bull. World Health Organ. 46, 783-792.
Krafsur, E.S., Armstrong, J.C., 1978. An integrated view of entomological and parasitological observations on falciparum malaria in Gambela, Western Ethiopian Lowlands. Trans. Roy. Soc. Trop. Med. Hyg. 72, 348-356.
Krafsur, E.S., Garrett-Jones, C., 1977. The survival of Wuchereria infected Anopheles funestus Giles in north-eastern Tanzania. Trans. Roy. Soc. Trop. Med. Hyg. 71, 155-160.
Macdonald, G., 1957. The Epidemiology and Control of Malaria. Oxford University Press, London.

<!-- PAGE BREAK -->

<a id='cf62dcb2-7d0d-40ed-bd43-03078111442e'></a>

1296

<a id='b5088a4d-0ed8-4fef-9752-f458b11a0df0'></a>

Chitnis, Hyman, and Cushing

<a id='820b8f31-ac1f-4501-9491-28864166b0cd'></a>

Massaga, J.J., Kitua, A.Y., Lemnge, M.M., Akida, J.A., Malle, L.N., Rønn, A.M., Theander, T.G., Bygb-jerg, I.C., 2003. Effect of intermittent treatment with amodiaquine on anaemia and malarial fevers in infants in Tanzania: a randomized placebo-controlled trial. Lancet 361, 1853–1860.
Molineaux, L., Gramiccia, G., 1980. The Garki Project. World Health Organization.
Molineaux, L., Shidrawi, G.R., Clarke, J.L., Boulzaguet, J.R., Ashkar, T.S., 1979. Assessment of insec-ticidal impact on the malaria mosquito's vectorial capacity, from data on the man-biting rate and age-composition. Bull. World Health Organ. 57, 265–274.
Muirhead-Thomson, R.C., 1957. The malarial infectivity of an African village population to mosquitoes (Anopheles gambiae): A random xenodiagnostic survey. Am. J. Trop. Med. Hyg. 6, 971–979.
Nedelman, J., 1984. Inoculation and recovery rates in the malaria model of Dietz, Molineaux and Thomas. Math. Biosci. 69, 209–233.
Nedelman, J., 1985. Introductory review: Some new thoughts about some old malaria models. Math. Biosci. 73, 159–182.
Ngwa, G.A., Shu, W.S., 2000. A mathematical model for endemic malaria with variable human and mos-quito populations. Math. Comput. Model. 32, 747–763.
Oaks Jr., S.C., Mitchell, V.S., Pearson, G.W., Carpenter, C.C.J. (eds.) 1991. Malaria: Obstacles and Op-portunities. National Academy Press.
Peters, W., Standfast, H.A., 1960. Studies on the epidemiology of malaria in New Guinea. II. Holoendemic malaria, the entomological picture. Trans. Roy. Soc. Trop. Med. Hyg. 54, 249–260.
Pull, J.H., Grab, B., 1974. A simple epidemiological model for evaluating the malaria inoculation rate and the risk of infection in infants. Bull. World Health Organ. 51, 507–516.
Roll Back Malaria Partnership, 2005. RBM World Malaria Report 2005. http://rbm.who.int/wmr2005/index.html.
Ross, R., 1911. The Prevention of Malaria, 2 edn. Murray, London.
Schellenberg, D., Menendez, C., Kahigwa, E., Aponte, J., Vidal, J., Tanner, M., Mshinda, H., Alonso, P., 2001. Intermittent treatment for malaria and anaemia control at time of routine vaccinations in Tanzanian infants: a randomized, placebo-controlled trial. Lancet 357, 1471–1477.
Sharma, S.N., Shukla, R.P., Raghavendra, K., Subbarao, S.K., 2005. Impact of DDT spraying on malaria transmission in Bareilly District, Uttar Pradesh, India. J. Vector Borne Dis. 42, 54–60.
Slooff, R., Verdrager, J., 1972. Anopheles balabacensis Baisas 1936 and malaria transmission in south-eastern areas of Asia. WHO/MAL/72.765.
Smalley, M.E., Sinden, R.E., 1977. Plasmodium falciparum gametocytes: Their longevity and infectivity. Parasitology 74, 1–8.
Zahar, A.R., 1974. Review of the ecology of malaria vectors in the WHO Eastern 4Mediterranean region. Bull. World Health Organ. 50, 427–440.
Zhou, G., Minakawa, N., Githeko, A.K., Yan, G., 2004. Association between climate variability and malaria epidemics in the East African highlands. Proc. Nat. Acad. Sci. USA 101, 2375–2380.
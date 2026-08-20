<a id='37e420b3-a22f-4c27-b768-f4a087bb4172'></a>

NATIONAL
INSTITUTES
OF HEALTH

NIH Public Access
Author Manuscript
J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='ae983545-62a7-4c3d-86e6-ec9dd8df76c8'></a>

Published in final edited form as:
_J Biol Dyn._ 2013; 7(1): 11–40. doi:10.1080/17513758.2012.733427.

<a id='f174fd7f-33d4-4eee-b673-adef069e570b'></a>

**Modelling vertical transmission in vector-borne diseases with applications to Rift Valley fever**

<a id='7cd6667a-ff25-4141-96dc-c0daa9ee6a9c'></a>

Nakul Chitnisa,b,*, James M. Hymanc, and Carrie A. Manorec

<a id='c86349d7-d382-4bc9-a038-ddf6b79fceae'></a>

aDepartment of Epidemiology and Public Health, Swiss Tropical and Public Health Institute, 4002 Basel, Switzerland
bUniversity of Basel, 4003 Basel, Switzerland
cDepartment of Mathematics, Tulane University, New Orleans, LA 70118, USA

<a id='7512994b-b6b6-4d1b-ae54-75c85cd00564'></a>

# Abstract
We present two ordinary differential equation models for Rift Valley fever (RVF) transmission in cattle and mosquitoes. We extend existing models for vector-borne diseases to include an asymptomatic host class and vertical transmission in vectors. We define the basic reproductive number, Ro, and analyse the existence and stability of equilibrium points. We compute sensitivity indices of Ro and a reactivity index (that measures epidemicity) to parameters for baseline wet and dry season values. Ro is most sensitive to the mosquito biting and death rates. The reactivity index is most sensitive to the mosquito biting rate and the infectivity of hosts to vectors. Numerical simulations show that even with low equilibrium prevalence, increases in mosquito densities through higher rainfall, in the presence of vertical transmission, can result in large epidemics. This suggests that vertical transmission is an important factor in the size and persistence of RVF epidemics.

<a id='29e43f42-a5ee-4e0b-b736-8cdfad831cb0'></a>

Keywords
vertical transmission; vector-borne disease; Rift Valley fever; mathematical model sensitivity
analysis; bifurcation analysis

<a id='8e724e2d-8ceb-48d0-aeed-9b9d113a8789'></a>

# 1. Introduction
Rift Valley fever (RVF) is an infectious disease caused by the RVF virus of the genus _Phlebovirus_ and family _Bunyaviridae_ and transmitted between animals species, including cattle, sheep, goats, and camels, primarily through the bite of the female mosquito, usually _Aedes_ or _Culex_. RVF causes high abortion rates in pregnant animals and very high death rates in newborn animals but is often mild or inapparent in adult animals [32]. The virus is zoonotic and can be transmitted to humans either through direct contact with infected tissue or through bites from infectious mosquitoes. An RVF outbreak can thus cause sickness and

<a id='de9ca1d0-8b9c-43c9-9006-ed66b9abd8b9'></a>

© 2013 N. Chitnis
“Corresponding author. nakul.chitnis@unibas.ch.
This paper is based on an invited talk given at the 3rd International Conference on Math Modeling & Analysis, San Antonio, USA,
October 2011.

<a id='c2714744-8413-4087-82f8-46ff7cdc38ef'></a>

NIH-PA Author Manuscript

<a id='c9dc2aaa-b59a-4d5b-abdd-fe10ce343a62'></a>

NIH-PA Author Manuscript

<a id='c85ed735-a969-430d-9fd9-d757cd56bba1'></a>

NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='567817cf-031e-4c2c-9c52-03bf8e6e0775'></a>

Chitnis et al.

<a id='4a3e99d5-5e5e-42e7-8def-8e14503a9e74'></a>

Page 2

<a id='71196b28-55af-45f5-a420-61e908aec5a8'></a>

death in humans as well as severe economic losses for the livestock industry. Most humans exhibit mild or no symptoms, but the virus can induce haemorrhagic fever that has a 10– 20% mortality rate in humans. There is no treatment for RVF other than supportive care [7]. The geographic domain of RVF has been expanding due to factors including increased irrigation and dams, climate change, and movement of livestock between countries [32]. Most sub-Saharan and North African countries have had RVF outbreaks in the past century and epidemics have recently spread to areas in the Middle East [6] and Madagascar [2]. There is a growing need to understand the critical parameters in the transmission and persistence of the disease and to develop effective strategies for its prevention and control. Mathematical modelling of RVF can play a unique role in comparing the effects of control strategies. We begin such a comparison by determining the relative importance of model parameters in RVF transmission and prevalence levels.

<a id='907a5589-728d-4137-8ef9-d2fb603db5f7'></a>

There are over 30 species of mosquitoes that are vectors for RVF, though they can be represented by two types: _Aedes_, or floodwater, mosquitoes and _Culex_ mosquitoes [7]. An important factor in the spread and persistence of RVF may be vertical transmission from _Aedes_ adult mosquitoes to eggs [25]. _Aedes_ eggs need be dry for several days before they can mature. After maturing, they hatch during the next flooding event large enough to cover them with water [5,32]. The eggs have high desiccation resistance and can survive dry conditions in a dormant form for months to years. At the beginning of the rainy season, _Aedes_ mosquitoes quickly grow to large numbers before declining due to the need for dry conditions for egg maturation. There can be a second peak in mosquito densities at the end of the rainy season if there is a gap in rainfall for several days [5]. _Culex_ mosquitoes, on the other hand, do not transmit vertically and prefer water that has been standing for some time and has acquired 'green matter'. Their eggs require water to mature and hatch and the mosquitoes survive the dry season in adult form. During the rainy season, the population of _Culex_ mosquitoes reaches a maximum towards the end of the season. Thus, the emergence of adult _Aedes_ mosquitoes from infected eggs can reintroduce RVF in livestock at the beginning of the rainy season, before _Culex_ mosquitoes amplify it further [5].

<a id='3d1c00f7-a73f-4a06-a598-8805c7f7e50a'></a>

Mosquito populations depend on rainfall and temperature, among other environmental factors. Rainfall increases the number and sizes of breeding sites, leading to an increase in the survival of juvenile stages of mosquitoes, a corresponding increase in the emergence rate of new adults, and a higher egg-laying rate and host-seeking behaviour in adults [20,36]. Higher temperatures decrease the incubation period of the virus in mosquitoes [5,37], while very high or very low temperatures increase the mortality rate of mosquitoes [13,24].

<a id='f55d110a-9bd8-49b0-a187-4cff5cb7e826'></a>

RVF epidemics usually occur every 5-15 years, though there is evidence that the disease remains endemic at a low level between epidemics [25]. Furthermore, there are differences in the patterns of RVF outbreaks in West Africa from those in East Africa [41]. In East Africa, the onset of high rainfall after periods of drought produces the largest epidemics. However, in Senegal, epidemics have occurred during drought and normal rainy seasons. Ndione et al. [30] attribute epidemics in WestAfrica to human-induced movement of livestock and trade and the loss of herd immunity over time. There is a 5-7-year inter-epidemic period in Senegal that corresponds closely to the time it takes for the renewal of a domestic herd of ruminants, with epidemics occurring when pasture and water availability

<a id='04f14e8d-fd6a-4ad8-8266-3c58eaf607aa'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='915e54b5-766f-4d68-8791-dca09bd809c2'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='582baf3b-568a-4e1f-9c29-1eac0d35bdb2'></a>

Chitnis et al.

<a id='fb3f32bd-6308-4bef-a465-d4ee6b97c3e2'></a>

Page 3

<a id='b4b4a606-b53d-4d6e-a29e-175cb9b12288'></a>

bring susceptible herds in contact with infectious vectors. Ndione _et al._ [30] also note that a dam on the Senegal river may negate the effects of interannual differences in rainfall by controlling river flow during heavy rains and maintaining river flow during drought.

<a id='011a40ce-8915-41a3-bcae-3ab84ef53e5f'></a>

Many recent papers modelling RVF transmission have concentrated on prediction of risk based on meteorological data that affect mosquito populations [2,3,27]. These models do not explicitly include livestock or human populations in their prediction of risk. Although meteorological data can sometimes be a good predictor [3], our goal is to understand the underlying dynamics of RVF and determine the importance of vertical transmission in the persistence of RVF between epidemics.

<a id='aa6197e4-033b-4b78-987b-27911a094564'></a>

Favier et al. [15] use a discrete model for individual ponds on a grid in which Aedes mosquitoes lay their (infected) eggs which hatch based on mosquito population dynamics and rainfall. If the number of mosquitoes and local susceptible animals are above a certain threshold, an epidemic occurs. Favier et al. [15] model the mosquito habitat in detail and limit detail about livestock populations and contact/biting rates between mosquitoes and animals. Gaff et al. [16] proposed an ordinary differential equation (ODE) compartmental model for the spread of RVF with a susceptible–exposed–infectious–recovered pattern for animals (cattle or sheep) and susceptible–exposed–infectious for Culex and Aedes mosquitoes, including vertical transmission for Aedes mosquitoes. The model combines frequency incidence of disease transmission between vectors and hosts with vital dynamics of livestock and mosquitoes. Xue et al. [42] consider a network model with ordinary differential equations at the nodes including both Culex and Aedes mosquitoes while focusing on the role of spatial heterogeneity in the spread of a single outbreak. Recently, Gaff et al. [17] extended the ODE model of Gaff et al. [16] to include mitigation strategies. Chitnis et al. [9,10] analysed a similar model for malaria transmission.

<a id='0c0d25e8-3ec8-4944-99f5-d9b904e519b3'></a>

We adapt Chitnis et al.'s [9] model to RVF, adding vertical transmission for Aedes mosquitoes as in [16,17] and an asymptomatic class for livestock. We include an asymptomatic class for hosts because for many species of livestock, RVF virus infections are frequently subclinical [12,18]. The asymptomatic animals have no ill effects but can still infect mosquitoes. We also include the population dynamics of both livestock and Aedes mosquitoes. Since we are interested in the importance of vertical transmission and inter-epidemic persistence, we exclude the dynamics of _Culex_ mosquitoes. We allow for a carrying capacity of the mosquito population in order to analyse the effects of seasonal variations in mosquito population size on model outputs. We preserve the definition of contact rates outlined in [9] that depend on both host and mosquito densities. This is especially important since we vary mosquito densities over seasons and would like to capture the effects of control interventions. Additionally, we extend the model to explicitly include an aquatic juvenile stag and compare versions of the model with and without this juvenile class to determine importance of this addition.

<a id='b30e00ec-c9d6-4cd5-b3e6-b287c8968ae8'></a>

We first describe the mathematical model, including the definition of a domain where the model is mathematically and epidemiologically well-posed. Next, we prove the existence and stability of a disease-free equilibrium point, define the reproductive number, R₀, and the reactivity index, ε₀, and show the existence of an endemic equilibrium point, xₑₑ. We then

<a id='58d49d3f-1531-484b-8e01-2ce0b0896d6c'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='ff49903f-4594-4b06-8123-2b8a3c244e79'></a>

NIH-PA Author ManuscriptNIH-PA Author ManuscriptNIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='a0a7d142-da66-4852-86f0-17964a345c30'></a>

Chitnis et al.

<a id='8ff54e28-51a6-4d13-918b-875ef1208078'></a>

Page 4

<a id='5998bd1a-9bda-424b-8c61-3862170826f3'></a>

present two sets of baseline parameter values to represent a dry and a wet season. We calculate the sensitivity indices of R0 and E0 for these baseline values and describe their interpretation for models with and without a juvenile class. We simulate the system to describe its reactivity: the ability for epidemics to occur given a perturbation. Finally, we quantify the effects of vertical transmission and seasonality on long-term persistence of RVF using numerical simulations.

<a id='44dc48f1-4a92-4448-abc0-9b8a83c36a86'></a>

## 2. Description of RVF model
The adapted model (Figure 1) divides the cattle population into four classes: susceptible, S_h, asymptomatic, A_h, infectious, I_h, and recovered (immune), R_h. Cattle enter the susceptible class through birth (at a constant rate). Birth rates are important because after an outbreak, herd immunity can reach 80% and the proportion of susceptible cattle must be renewed through birth or movement before another outbreak can occur [8]. We assume the migration of mosquitoes is negligible and may be ignored. If we assume that all cattle migrating into the simulation region are susceptible, then our assumption that the cattle migration is negligible is easily relaxed by expanding the definition of the birth and death terms in the model to include migration. However, if we assume that some of the cattle migrating into the region are infected, then the conclusions in this paper will need to be re-analysed for this situation.

<a id='00c3e781-ea6c-4b5e-b28d-1306106d6753'></a>

When an infectious mosquito bites a susceptible cow, there is a finite probability that the cow becomes infected. Since the duration of the latent period in cattle is small relative to their life span, we do not model the exposed stage. There is a substantial difference between the immune response of an infant and an adult cow. Young cows have a much higher probability of dying from RVF (10–70%) than adults (5–10%) [7,24]. Similarly, 90–100% of goat and sheep infants die from RVF, while 10–30% of adults die from the virus [7]. Since many adult cattle do not exhibit clinical signs apart from abortion of foetuses [12,18,32], we include an asymptomatic class for infectious animals that transmit the virus at a lower rate than those with acute clinical signs. In our model, after successfully infected by an infectious mosquito, cattle move from the susceptible class Sh to either the infectious Ih or asymptomatic Ah class. After some time, the infectious and asymptomatic cattle recover and move to the recovered class, Rh. The recovered cattle have immunity to the disease for life. Cattle leave the population through a per capita natural death rate and through a per capita disease-induced death rate.

<a id='e9aaddfc-ccc5-41a8-802d-9f9d8d052426'></a>

There is evidence that RVF is transmitted horizontally by livestock through contact with blood and aborted material [32]. However, because it is not thought that this plays a role in long-term persistence of RVF, especially over a dry season, we do not include this mode of transmission in our model. If one were interested in predicting total consequence of a particular outbreak, the low levels of horizontal transmission may need to be included.

<a id='bbb32a6d-4442-4ee0-a850-8ebf89cd46dd'></a>

We divide the *Aedes* mosquito population into three classes: susceptible, $S_v$, exposed, $E_v$, and infectious, $I_v$. Female mosquitoes (we do not include male mosquitoes in our model because only female mosquitoes bite animals for blood meals) enter the susceptible class through birth. The birth term for mosquitoes accounts for and is proportional to the egg-

<a id='3a82b118-c343-45f5-8fe5-35a8b26e6187'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='f92921a5-c9d6-44c8-af2f-582f70280ded'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='1e05e81a-713e-4227-8938-cf615bb7d866'></a>

Chitnis et al.

<a id='fd56ad84-dd05-4ca9-a396-15a871cda783'></a>

Page 5

<a id='81d41f52-0131-4789-b1b0-8dcba0edd735'></a>

laying rate of adult female mosquitoes; survival and hatching rate of eggs; and survival of larvae. If any of these are increased or decreased, the birth rate is affected accordingly. Since most density-dependent survival of mosquitoes occurs in the larval stage, we assume a constant emergence rate that is not affected by the number of eggs laid; that is, all emergence of new adult mosquitoes is limited by the availability of breeding sites.

<a id='da56aa14-1b77-423c-b5b3-fa0e0575b1bf'></a>

The virus enters a susceptible mosquito, S_v, with finite probability, when the mosquito bites an infectious animal and the mosquito moves from to the exposed class, E_v. After some period of time, depending on the ambient temperature and humidity [37], the mosquito moves from the exposed class to the infectious class, I_v. The mosquito remains infectious for life. Mosquitoes leave the population through a per capita natural death rate. We consider an additional model with susceptible, S_e, and infectious, I_e, juvenile classes to explore the effects of including an aquatic stage. This will facilitate a future inclusion of seasonality and mitigation strategies and allow us to compare our model with that of Adams and Boots' [1] for dengue fever.

<a id='8d718fa9-6026-494e-bfaf-304f7374b1af'></a>

We ignore the feeding of mosquitoes on humans to keep the model simple and focus on livestock vector transmission. Although there is evidence that _Aedes_ and _Culex_ mosquitoes of the type typically spreading RVF have a preference for cattle and livestock as opposed to humans [28], we will include feeding on humans in the future because it is important to understand the effects of RVF morbidity in humans. Mpeshe _et al._ [26] present an RVF model that focuses on the human hosts. Also, although there is some evidence that mosquitoes preferentially feed on infected hosts [35], the evidence is sparse and we make the simplifying assumption that mosquitoes feed on all hosts equally.

<a id='84d57a23-c954-4b88-b8f3-b61a69d7f934'></a>

Our adaptation of Chitnis *et al.*'s [9,10] and Gaff *et al.*'s [16,17] models includes vertical transmission in mosquitoes with and without explicitly including the juvenile stage, generalizes the mosquito biting rate so that it applies to wider ranges of population sizes, and includes asymptomatic infections in cattle. In [16], the total number of mosquito bites on cattle depends on the number of mosquitoes, while in our model, the total number of bites varies with both the cattle and mosquito population sizes. This allows a more realistic modelling of situations where there is a high ratio of mosquitoes to cattle, and where cattle availability to mosquitoes is reduced through control interventions.

<a id='78f490ec-5c8a-4ddd-877e-32ca6ff3f8fa'></a>

We compile two sets of baseline values for the parameters in the model: one for high rainfall and moderate temperature (wet season) and one for lower rainfall with moderate temperatures (dry season). The dry season parameter set can also be thought of as the result of mitigation strategies that reduce vector density, lifespan, and biting rate. Unusually high rainfall is often considered to be responsible for large RVF epidemics and in East Africa these events occur once every 3-7 years on average [25,29]. We also consider a range of values for vertical transmission of the virus from mosquito mother to egg of 1% to 10% [34]. Vertical transmission is considered to be one of the main factors in inter-epidemic persistence of RVF [7,19,24,32] and has been included to various degrees in other RVF mathematical models [15-17]. An alternative hypothesis for the inter-epidemic persistence of RVF is low-level endemic transmission with an unknown vertebrate host [19]. Here, we explore only the vertical transmission hypothesis. We consider a range of parameter values

<a id='bb977a01-b301-463d-9c00-5adaecc25165'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='272ddbe7-c33d-4bbb-b87e-468e7618ff12'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='03a5464b-f12e-47e7-888d-ac7f1ccb92b6'></a>

Chitnis et al.

<a id='42a0f696-2503-4fab-94d3-bfc0ecdbee28'></a>

Page 6

<a id='7afc4a97-a142-4242-bd06-cdb7f04b5641'></a>

for incubation time in the mosquito, as incubation also depends upon climate variability. For some parameters, we use values published in the available literature, while for others, we use realistically feasible values.

<a id='a3f9fe73-8db6-44ca-9ce0-0ad626eb31e0'></a>

As R₀ is related to initial disease transmission, and ε₀ is related to epidemicity, an evaluation of these sensitivity indices allows us to determine the relative importance of different parameters in RVF transmission and the likelihood and size of outbreaks. We analyse the relative importance of the parameters for three different purposes:

*   the initial rate of disease transmission and epidemicity in areas of low rainfall;
*   the initial rate of disease transmission and epidemicity in areas of high rainfall;
*   the inter-epidemic persistence of disease with seasonal variation.

<a id='1a4a3132-3499-4cd4-953c-24624ce80c2c'></a>

A knowledge of the relative importance of parameters can help guide in developing efficient intervention strategies in RVF-endemic or epidemic areas where resources are scarce.

<a id='e8f2b3f8-99f5-424e-bb3d-bb7463c196a9'></a>

## 2.1. Mathematical model
The state variables (Table 1) and parameters (Table 2) for the RVF model (Figure 1) satisfy the equations

<a id='8a5af7bf-f511-412a-b981-c9dc148a583d'></a>

<::dSh/dt = μh C0 - λh(t)Sh - μh Sh, (1a) : equation::>

<a id='ff39145f-6529-4bb9-b4d0-0a2576a35636'></a>

dA_h / dt = θ_h λ_h(t) S_h - (μ_h + γ̃_h) A_h, (1b)

<a id='f3bfc252-37fb-4cff-a129-61ee95efe88a'></a>

$$\frac{dI_h}{dt}=(1-\theta_h)\lambda_h(t)S_h-(\mu_h+\gamma_h+\delta_h)I_h, \quad (1c)$$

<a id='0a887f8f-7206-4657-bcd1-337981d078f5'></a>

dR_h / dt = γ_h I_h + γ̃_h A_h - μ_h R_h, (1d)

<a id='e06859cc-4535-4ce7-9eb4-e175a28f02c1'></a>

$$\frac{dS_v}{dt} = \left(\frac{N_v - \varphi_v I_v}{N_v}\right) \mu_v M_0 - \lambda_v(t) S_v - \mu_v S_v \quad (1e)$$

<a id='415008f3-db11-433f-a0c4-096ce458604c'></a>

dEv/dt = λv(t)Sv - (μv + νv)Ev, (1f)

<a id='0a35e810-dfc2-458d-b660-3eb993dd405e'></a>

$\frac{dI_v}{dt} = \left(\frac{\varphi_v I_v}{N_v}\right) (\mu_v M_0 + \nu_v E_v - \mu_v I_v), \quad (1g)$

<a id='35cb0b43-79cc-4d5b-9703-d45601ae6979'></a>

where \u0010h is the per capita natural death rate for cattle. The total population sizes are Nh = Sh
+ Ah + Ih + Rh and Nv = Sv + Ev + Iv with

<a id='52460c7f-ba41-42a4-9b92-e209a8ac5dbd'></a>

*J Biol Dyn*. Author manuscript; available in PMC 2014 December 09.

<a id='49033b02-16f6-49bf-bb9c-78a76ec889b5'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='276e8063-5b2c-4528-9e34-68ac511a6fee'></a>

Chitnis et al.

<a id='7b9f0c28-f016-445f-83d9-a886fbb6d2ca'></a>

Page 7

<a id='712c95da-0d48-42b5-91a3-020912d19eaa'></a>

$$\frac{\mathrm{d}N_h}{\mathrm{d}t} = \mu_h(C_0-N_h)-\delta_h I_h, \quad (2a)$$

<a id='0f7b854a-46b1-4d2a-86e7-17c5214099d4'></a>

$\frac{dN_v}{dt} = \mu_v(M_0 - N_v)$, (2b)

<a id='d211e015-af57-4b62-8e5f-5312857fc328'></a>

and

<a id='4ec89d56-c0e6-44e2-b2a8-60298be93aae'></a>

<::λ_h = \frac{σ_v N_v σ_h}{σ_v N_v + σ_h N_h} \beta_{hv} \frac{I_v}{N_v},
λ_v = \frac{σ_v σ_h N_h}{σ_v N_v + σ_h N_h} \left( \beta_{vh} \frac{I_h}{N_h} + \tilde{\beta}_{vh} \frac{A_h}{N_h} \right).
: figure::>

<a id='97deed60-8a1a-42c8-aa82-fb79836f7d0a'></a>

All parameters are strictly positive with the exception of the mosquito vertical transmission probability, \( \phi_V \), which is non-negative.

<a id='366090f3-1781-492f-95b6-13267281ee45'></a>

In this model, following the model of Chitnis et al. [9], σ_v is the rate at which a mosquito would like to bite a cow (related to the gonotrophic cycle length), and σ_h is the maximum number of bites that a cow can support per unit time (through physical availability and any intervention measures on livestock taken by humans). Then, σ_vN_v is the total number of bites that the mosquitoes would like to achieve per unit time and σ_hN_h is the availability of cattle. The total number of mosquito–cattle contacts is half the harmonic mean of σ_vN_v and σ_hN_h,

<a id='be6bedc7-5bba-48b3-8b8a-4b329305ae65'></a>

$$b=b(N_h, N_v) = \frac{\sigma_v N_v \sigma_h N_h}{\sigma_v N_v + \sigma_h N_h} = \frac{\sigma_v \sigma_h}{\sigma_v (N_v/N_h) + \sigma_h} N_v \quad (3)$$

<a id='7d33e516-7176-4c9f-b0ab-0a5afff3eabd'></a>

In addition to having the correct limits at zero and infinity, this form also meets the necessary criteria that $b \leq \min(\sigma_v N_v, \sigma_h N_h)$ where $b$ is the total number of bites per unit time. The total number of mosquito-cattle contacts depends on the populations of both species. We define $b_h = b_h(N_h, N_v) = b(N_h, N_v)/N_h$ as the number of bites per cattle per unit time, and $b_v = b_v(N_h, N_v) = b(N_h, N_v)/N_v$ as the number of bites per mosquito per unit time.

<a id='cd028ff4-41a7-44c6-9a67-6a302867b878'></a>

We define the force of infection from mosquitoes to cattle, λ_h(t), as the product of the number of mosquito bites that one cow has per unit time, b_h, the probability of disease transmission from the mosquito to the cow, β_hv, and the probability that the mosquito is infectious, I_v/N_v. We define the force of infection from cattle to mosquitoes, λ_v(t), as the force of infection from infectious (symptomatic and asymptomatic) cattle. This is defined as the number of cattle bites one mosquito has per unit time, b_v; the probability of disease transmission from an infected (asymptomatic) cow to the mosquito, β_vh (β̃_vh); and the probability that the cow is infectious, I_h/N_h (A_h/N_h).

<a id='a42f424c-1e70-4b4d-a3b2-4a6cae206286'></a>

The exposed class models the delay before infected mosquitoes become infectious. In mosquitoes, this delay is important because it is on the same order as their expected life span. Thus, many infected mosquitoes die before they become infectious.

<a id='c736ba79-29bd-4cc5-af1b-710fc14c83df'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='919df6d8-08b8-4c47-8954-7275b3bf25f0'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='8e8a28b5-75df-4295-a224-969241db3a7d'></a>

Chitnis et al.

<a id='20cb569c-36c0-489e-a3e7-a0d4bcdfd41f'></a>

Page 8

<a id='a62c7ed2-988b-4635-a61c-0e2a356abb5f'></a>

To simplify the analysis of the model, we normalize the populations of each class of cattle and mosquitoes by their total species population size. We also assume that the mosquito population is at its stable equilibrium size, $N_v = M_0$. We let

<a id='410434cf-266e-4bae-bb72-fa41a38b0c71'></a>

a_h = A_h / N_h , i_h = I_h / N_h , r_h = R_h / N_h , e_v = E_v / M_0 , and i_v = I_v / M_0 , (4)

<a id='d538c2bf-f325-41e2-8de3-852028b43b0c'></a>

with

<a id='256a7664-0f1c-49e1-a393-e26923504692'></a>

S_h = (1 - a_h - i_h - r_h)N_h and S_v = (1 - e_v - i_v)M_0. (5)

<a id='53352f12-6e07-4e7a-9db8-f915b332821e'></a>

Differentiating the scaling Equations (4) and solving for the derivatives of the scaled variables, we obtain

<a id='ac13f626-0837-4b3e-a90b-b37bcfc678ce'></a>

$$\frac{da_h}{dt} = \frac{1}{N_h} \left[\frac{dA_h}{dt} - a_h \frac{dN_h}{dt}\right] \quad \text{and} \quad \frac{de_v}{dt} = \frac{1}{M_o} \left[\frac{dE_v}{dt}\right] , \quad (6)$$

<a id='0bc5c2b3-d75e-4d48-a433-7aaa184deb5a'></a>

and so on for the other variables. This creates a new six-dimensional system of equations,

<a id='8830f7d0-34ba-4d93-b425-6212668e875d'></a>

$$\frac{dN_h}{dt} = \mu_h (C_0 - N_h) - \delta_h i_h N_h, \quad (7a)$$

<a id='278b4ac5-721d-43ef-a609-3cef2a9e6176'></a>

$$\frac{da_h}{dt} = \left(\frac{\sigma_v M_0 \sigma_h \theta_h \beta_h i_v}{\sigma_v M_0 + \sigma_h N_h}\right) (1 - a_h - i_h - r_h) - \left(\tilde{\gamma}_h + \mu_h \frac{C_0}{N_h}\right) a_h + \delta_h i_h a_h, \quad (7b)$$

<a id='e099793a-f3f3-41b4-9ba2-3b32eb791d78'></a>

$\frac{di_h}{dt} = \left( \frac{\sigma_v M_0 \sigma_h (1-\theta_h) \beta_h i_v}{\sigma_v M_0 + \sigma_h N_h} \right) (1-a_h-i_h-r_h) - \left( \gamma_h + \delta_h + \mu_h \frac{C_0}{N_h} \right) i_h + \delta_h i_h^2, \quad (7c)$

<a id='9246c966-751f-468a-9865-757d271ed38c'></a>

$$\frac{dr_h}{dt} = \tilde{\gamma}_h a_h + \gamma_h \dot{i}_h - r_h \mu_h \frac{C_0}{N_h} + \delta_h \dot{i}_h r_h, \quad (7d)$$

<a id='baf28a37-6076-4f0f-bc5d-9d9a7219cda6'></a>

$$\frac{de_v}{dt} = \left(\frac{\sigma_v\sigma_hN_h}{\sigma_vM_0+\sigma_hN_h}\right) (\tilde{\beta}_{vh}a_h+\beta_{vh}i_h)(1-e_v-i_v)-(\nu_v+\mu_v)e_v, \quad (7e)$$

<a id='05b40af7-21d3-4834-b521-7dfc7dd02c0c'></a>

di_v / dt = nu_v e_v - (1 - phi_v) mu_v i_v. (7f)

<a id='d1fd8719-00e4-433a-94d9-914a388a4848'></a>

The model (7) is epidemiologically and mathematically well-posed in the domain,

<a id='45dbe3e0-4893-4fc3-a9c8-ffd3771b355c'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='9d037a75-80cb-48ea-a26b-ef4f07734234'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='d70e002c-1eb9-42b7-8000-77241290b307'></a>

Chitnis et al.

<a id='cd0e1b5f-7023-4620-a673-cc7b4235f541'></a>

Page 9

<a id='0a5e327d-9974-492e-b1a0-1279b7243da2'></a>

<::equation: $\mathcal{D} = \left\{ \begin{pmatrix} N_h \\ e_h \\ i_h \\ r_h \\ e_v \\ i_v \end{pmatrix} \in \mathbb{R}^6 \middle| \begin{array}{l} 0 < N_h \leq C_0, \\ a_h \geq 0, \\ i_h \geq 0, \\ r_h \geq 0, \\ a_h+i_h+r_h \leq 1, \\ e_v \geq 0, \\ i_v \geq 0, \\ e_v+i_v \leq 1 \end{array} \right\} \cdot (8)$::>This domain, $\mathcal{D}$, is valid epidemiologically as the normalized populations, $a_h, i_h, r_h, e_v$, and $i_v$, are all non-negative and have sums over their species type that are less than or equal to 1. The cattle population, $N_h$, is positive and bounded by its stable disease-free value, $C_0$. We use the notation $f'$ to denote $df/dt$. We denote points in $\mathcal{D}$ by $x = (N_h, a_h, i_h, r_h, e_v, i_v)$.

<a id='1cae7f13-c74b-4162-9c2c-ab2a44daaf1d'></a>

**Theorem 2.1:** Assuming that the initial conditions lie in D, the system of equations for the RVF model (7) has a unique solution that exists and remains in D for all time t ≥ 0.

<a id='91ed0417-6080-4311-8639-76bb44e84994'></a>

**Proof:** The right-hand side of Equation (7) is continuous with continuous partial derivatives in $\mathcal{D}$, so Equation (7) has a unique solution. We now show that $\mathcal{D}$ is forward-invariant. We can see from Equation (7) that if $a_h = 0$, then $a_h' \geq 0$; if $i_h = 0$, then $i_h' \geq 0$; if $r_h = 0$, then $r_h' \geq 0$; if $e_v = 0$, then $e_v' \geq 0$; and if $i_v = 0$, then $i_v' \geq 0$. It is also true that if $a_h + i_h + r_h = 1$ then $a_h' + i_h' + r_h' < 0$; and if $e_v + i_v = 1$ then $e_v' + i_v' < 0$. Finally, we note that if $N_h = 0$, then $N_h' > 0$; if $N_h > 0$ at time $t = 0$, then $N_h > 0$ for all $t > 0$; and if $N_h = C_0$, then $N_h' \leq 0$. Therefore, none of the orbits can leave $\mathcal{D}$ and a unique solution exists for all time.

<a id='5178db0d-3aae-46f0-a92e-4e2f4291d9a7'></a>

## 2.2. Extended vertical transmission model

Here we extend the model by adding variables for the susceptible and the infected juvenile stages. Infected eggs and larvae result from vertical transmission of RVF from an infectious mother to her eggs. We can eventually relate the hatching of eggs to environmental variables and seasonality. Where there is little delay in hatching, we show the model reduces to the simpler vertical transmission model (1). We assume that the mosquito population is at a constant carrying capacity and that the birth term thus encompasses loss of eggs, regulation at the larval stage, and predation of eggs, larvae, or pupae. In most settings, this is a reasonable assumption as breeding sites are at carrying capacity. However, the assumption breaks down if the adult population drops substantially through, for example, vector control interventions. In the future, we will include seasonality and climate effects in the juvenile stage. We model the juvenile classes as either susceptible, $S_e$, or infected, $I_e$, that are replenished at a per capita birth rate $\mu_V$. The proportion of eggs laid by an infected female mosquito that are infected is $\phi_V$, while $\gamma_e$ is the rate at which mosquitoes develop from egg to adult. The state variables (Table 1) and parameters (Table 2) for the RVF model (Figure 2) satisfy the equations

<a id='3cd09911-23e1-4857-9447-964964b06a26'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='a8167f2c-69a9-40dc-a897-5180bfad5bc7'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='7b9af4c3-0595-4722-9150-2318956f0fb3'></a>

Chitnis et al.

<a id='48a88f73-1f32-45c8-8cdf-36611cce1429'></a>

Page 10

<a id='860f5f5b-060c-4274-a0b0-d681799e42e8'></a>

dSh/dt = μh C0 - λh(t)Sh - μhSh (9a)

dAh/dt = θh λh(t)Sh - (μh + γ̃h)Ah (9b)

dIh/dt = (1 - θh)λh(t)Sh - (μh + γh + δh)Ih (9c)

dRh/dt = γhIh + γ̃hAh - μhRh (9d)

dSe/dt = μv ((Nv - φvIv) / Nv) M0 - γeSe (9e)

dIe/dt = μv ((φvIv) / Nv) M0 - γeIe (9f)

dSv/dt = γeSe - λv(t)Sv - μvSv (9g)

dEv/dt = λv(t)Sv - (μv + νv)Ev (9h)

dIv/dt = γeIe + νvEv - μvIv (9i)

<a id='f5c9d78f-6983-443c-8d60-f34925f6344a'></a>

To simplify the analysis of the model, we normalize the populations of each class of cattle and mosquitoes by their total species population size. We also assume that the mosquito population is at its stable equilibrium size, $N_v = M_0$ and $N_e = S_e + I_e = \mu_v M_0 / \gamma_e$. We normalize the variables by their respective population size,

<a id='91e733d7-3cd5-4b6b-91a4-dcd993dc73b5'></a>

$$a_h = \frac{A_h}{N_h}, i_h = \frac{I_h}{N_h}, r_h = \frac{R_h}{N_h}, i_e = \frac{I_e \gamma_e}{\mu_v M_0}, e_v = \frac{E_v}{M_0}, \text{ and } i_v = \frac{I_v}{M_0}, (10)$$

<a id='b43fc1db-1036-4a63-85b0-2ea9039d314d'></a>

with

<a id='319f40af-f2a7-4411-975d-f2de1c07044a'></a>

$$S_h = (1-a_h-i_h-r_h)N_h, \quad S_e = (1-i_e)\frac{\mu_v M_0}{\gamma_e}, \quad \text{and} \quad S_v = (1-e_v-i_v)M_0. \quad (11)$$

<a id='c18d05d8-71e7-4ce5-a7ad-e23a94ff9311'></a>

Differentiating the scaling equations (10) and solving for the derivatives of the scaled variables as before, we obtain a new seven-dimensional system of equations,

<a id='135b8316-dc2a-4a44-922c-40b57c9627e7'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='2ecb4bbb-2445-45d7-a43a-7ecfd5f57d39'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<a id='d741fc48-702d-479d-abc9-1a3b9cd5db78'></a>

d
—
c

<!-- PAGE BREAK -->

<a id='d0bb48ea-7183-49cb-865c-4551c9742e87'></a>

Chitnis et al.

<a id='e6bd2aae-d89a-4a8d-80b2-ad9d74e701a3'></a>

Page 11

<a id='6693ce8c-9fd4-462d-9a5e-a1dde8a942e2'></a>

dNh/dt = μh(C0 - Nh) - δh ih Nh, (12a)

<a id='5bd9ef27-0cf9-473d-a601-2fecf1bcfd9a'></a>

$$\frac{da_h}{dt} = \left( \frac{\sigma_v M_0 \sigma_h \theta_h \beta_{hv} i_v}{\sigma_v M_0 + \sigma_h N_h} \right) (1 - a_h - i_h - r_h) - \left( \tilde{\gamma}_h + \mu_h \frac{C_0}{N_h} \right) a_h + \delta_h i_h a_h, \quad (12b)$$

<a id='1a451b6e-b70d-4353-920b-2b991341e198'></a>

$$\frac{di_h}{dt} = \left( \frac{\sigma_v M_0 \sigma_h (1 - \theta_h) \beta_{hv} i_v}{\sigma_v M_0 + \sigma_h N_h} \right) (1 - a_h - i_h - r_h) - \left( \gamma_h + \delta_h + \mu_h \frac{C_0}{N_h} \right) i_h + \delta_h i_h^2 \quad (12c)$$

<a id='64b9a2bb-3541-4223-b608-b4bd982fc99f'></a>

$\frac{dr_h}{dt} = \tilde{\gamma}_h a_h + \gamma_h i_h - r_h \mu_h \frac{C_0}{N_h} + \delta_h i_h r_h, \quad (12d)$

<a id='d714dfcc-5d8b-4aff-b503-f16cf1af585e'></a>

$\frac{di_e}{dt} = \gamma_e \varphi i_v - \gamma_e i_e$, (12e)

<a id='c2b960ac-e906-4c01-bedd-ae68ab24a2fd'></a>

$$\frac{de_v}{dt} = \left(\frac{\sigma_v\sigma_h N_h}{\sigma_v M_0 + \sigma_h N_h}\right)(\tilde{\beta}_{vh} a_h + \tilde{\beta}_{vh} i_h)(1-e_v-i_v)-(\nu_v+\mu_v)e_v, \quad (12f)$$

<a id='620492c7-a457-429e-9694-20c27350271e'></a>

$\frac{di_v}{dt} = \mu_v i_e + \nu_v e_v - \mu_v i_v \cdot$ (12g)

<a id='146b494a-acc7-429a-aa6a-de75108384b5'></a>

The model (12) is epidemiologically and mathematically well-posed in the domain,

$$\mathcal{D}_2 = \left\{ \begin{pmatrix} N_h \\ e_h \\ i_h \\ r_h \\ i_e \\ e_v \\ i_v \end{pmatrix} \in \mathbb{R}^7 \middle| \begin{array}{l}
0 < N_h \leq C_0, \\
e_h \geq 0, \\ i_h \geq 0, \\ r_h \geq 0, \\
e_h + i_h + r_h \leq 1, \\
0 \leq i_e \leq 1, \\
e_v \geq 0, \\ i_v \geq 0, \\
e_v + i_v \leq 1
\end{array} \right\}. \quad (13)$$

<a id='6bbb90d7-2889-43b7-865d-2cfc3ce0b8bb'></a>

This domain, $\mathcal{D}_2$, is valid epidemiologically as the normalized populations, $a_h$, $i_h$, $r_h$, $i_e$, $e_v$, and $i_v$, are all non-negative and have sums over their species type that are less than or equal to 1. The cattle population, $N_h$, is positive and bounded by its stable disease-free value, $C_0$. We use the notation $f'$ to denote $df/dt$. We denote points in $\mathcal{D}_2$ by $x = (N_h, a_h, i_h, r_h, i_e, e_v, i_v)$.

<a id='e33f95c8-1d9a-45d9-bcd4-73ceb015b9a4'></a>

**Theorem 2.2:** Assuming that the initial conditions lie in _D_<sub>2</sub>, the system of equations for the RVF model (12) has a unique solution that exists and remains in _D_<sub>2</sub> for all time _t_ ≥0.

<a id='3de6842b-50f7-4049-b2c7-9e457c72b939'></a>

**Proof:** The right-hand side of Equation (12) is continuous with continuous partial derivatives in D₂ , so Equation (12) has a unique solution. We now show that D₂ is forward-

<a id='4b1a7ed1-5720-4c07-b20e-4b46c382240e'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='f147766b-7165-4d68-a026-3b2aa6b9f2b7'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='c90b1ba5-58df-4502-8446-36cf080b4d78'></a>

Chitnis et al.

<a id='73c7468e-d754-49e3-a4ab-723a397b6186'></a>

Page 12

<a id='6bff944f-9ca0-42bc-8c8e-6ccf465af960'></a>

invariant. We can see from Equation (12) that if a_h = 0, then a'_h ≥ 0; if i_h = 0, then i'_h ≥ 0; if r_h = 0, then r'_h ≥ 0; if i_e = 0, then i'_e ≥ 0; if e_v = 0, then e'_v ≥ 0; and if i_v = 0, then i'_v ≥ 0. It is also true that if a_h + i_h + r_h = 1, then a'_h + i'_h + r'_h < 0; if i_e = 1, then i'_e < 0; and if e_v + i_v = 1, then e'_v + i'_v < 0. Finally, we note that if N_h = 0, then N'_h > 0; if N_h > 0 at time t = 0, then N_h > 0 for all t > 0; and if N_h = C_0, then N'_h ≤ 0. Therefore, none of the orbits can leave D₂ and a unique solution exists for all time.

<a id='a8d1412a-cf82-42eb-ac38-9b37898691e0'></a>

### 3. Equilibrium points and basic reproductive number

#### 3.1. Disease-free equilibrium point

Disease-free equilibrium points are steady-state solutions where there is no disease. We define the 'diseased' classes as the cattle or mosquito populations that are either asymptomatic, exposed, or infectious; that is, $a_h$, $i_h$, $e_v$, and $i_v$ for model (7). We denote the positive orthant in $R^n$ by $R^n_+$ the boundary of $R^n_+$ by $∂R^n_+.$

<a id='642a0642-713a-4157-9035-7e09f7cae72b'></a>

**Theorem 3.1:** The model for RVF without a juvenile class (7) has exactly one equilibrium point,

<a id='63976462-0a5c-42cb-bf83-53ffbd694915'></a>

x_dfe=(C_0, 0, 0, 0, 0), (14)

<a id='73277ea1-cc64-4121-bd9a-0e3b2d26ff4d'></a>

with no disease in the population (on D ∩ ∂R+^6).

<a id='40c86001-dcc5-44c0-8bc3-5c3854093b93'></a>

Proof: By inserting $x_{dfe}$ in Equation (7), we see that all derivatives are equal to zero so $x_{dfe}$ is an equilibrium point of Equation (7). By setting any of $a_h$, $i_h$, $r_h$, $e_v$, or $i_v$ equal to zero, we also see that the other four variables have to be zero and $N_h = C_0$ for the system to be at equilibrium.

<a id='5c5b1bd9-9a3f-44ac-a507-e9741f3f4f90'></a>

**3.1.1. Extended model disease-free equilibrium**—We define the ‘diseased’ classes as the cattle or mosquito populations that are either asymptomatic, exposed, or infectious; that is, *a_h*, *i_h*, *i_e*, *e_v*, and *i_v* for model (12).

<a id='bb190f69-3bb2-4771-989e-fb5b854d7db7'></a>

**Theorem 3.2:** The model for RVF without a juvenile class (12) has exactly one equilibrium point,

<a id='8303cb6a-e240-48ae-abd9-72a8f0f764ba'></a>

x_dfe,2=(C_0, 0, 0, 0, 0, 0), (15)

<a id='64c22a45-2a9a-458a-955a-d8d934919d6f'></a>

with no disease in the population (on $\mathscr{D}_2 \cap \partial\mathbb{R}_+^7$).

<a id='927a8797-68a5-492c-833b-107b7290726c'></a>

**Proof:** By inserting x_{dfe,2} in Equation (12), we see that all derivatives are equal to zero so x_{dfe,2} is an equilibrium point of Equation (12). By setting any of a_{h}, i_{h}, r_{h}, i_{e}, e_{v}, or i_{v} equal to zero, we also see that the other five variables have to be zero and N_{h} = C_{0} for the system to be at equilibrium.

<a id='18a9c4d5-4999-4fad-9465-1464ad543aaf'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='addb286c-70f7-4d3a-acbc-4bf5108b8fa6'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='4ab58194-8eed-431d-a8ce-43ca89ee59d8'></a>

Chitnis et al.

<a id='fe22771b-d0e7-42ea-9611-cf9ceb92394d'></a>

Page 13

<a id='96712f6c-bc09-4bdb-9e04-bf9370b3f6ad'></a>

## 3.2. Basic reproduction number and reactivity

In a model assuming a homogeneous population and with one infectious compartment, the basic reproductive number, R₀, is defined as the expected number of secondary infections that one infectious individual would cause over the duration of the infectious period in a fully susceptible population. For our more complicated models, we use the next generation operator approach, as described by Diekmann et al. [14] and Van den Driessche and Watmough [40] to define the basic reproductive number, R₀, to describe a threshold condition for when the disease-free equilibrium points lose stability. For the model without juvenile stages, Equation (1), we let x = (aₕ, iₕ, eᵥ, iᵥ, rₕ, Nₕ) and dx/dt = 𝓕(x) - 𝓥(x), where 𝓕(x) represents the rate of new infections entering the population, and 𝓥(x) = 𝓥⁻(x) - 𝓥⁺(x) represents the rate of movement (by other means) out of, and into, each compartment, respectively. We let 𝓕₀ and 𝓥₀ be the Jacobian matrices of the first four elements of 𝓕 and 𝓥, respectively, evaluated at the disease-free equilibrium, xdᶠe. Then,

<a id='f30622d5-76b5-47d7-bffd-375cbd55b471'></a>

F₀ = 
$$
\begin{bmatrix}
0 & 0 & 0 & \theta\beta_{hv}M_0\zeta \\
0 & 0 & 0 & (1-\theta)\beta_{hv}M_0\zeta \\
\tilde{\beta}_{vh}C_0\zeta & \beta_{vh}C_0\zeta & 0 & 0 \\
0 & 0 & 0 & \mu_v\varphi_v
\end{bmatrix}
$$
(16)

<a id='f636bcf0-7068-4c28-9028-1c11018ad098'></a>

and

$V_0 = \begin{bmatrix}
\mu_h + \tilde{\gamma}_h & 0 & 0 & 0 \\
0 & \mu_h + \gamma_h + \delta_h & 0 & 0 \\
0 & 0 & \mu_v + \nu_v & 0 \\
0 & 0 & -\nu_v & \mu_v
\end{bmatrix}, (17)$

<a id='13676902-11ce-4225-8b17-1688fcf60f64'></a>

where

$$\zeta = \frac{\sigma_v\sigma_h}{\sigma_v M_0 + \sigma_h C_0} \cdot \quad (18)$$

<a id='7a7bf328-60f3-4f59-b435-7395b27c62de'></a>

The basic reproductive number is the spectral radius of the next generation matrix,
s($F_0V_0^{-1}$),

<a id='0a124db0-dbfa-44af-9681-effd48b2f46b'></a>

$$ \mathcal{R}_0 = \frac{1}{2} \left( \varphi_v + \sqrt{4 \frac{\nu_v}{\mu_v + \nu_v} \frac{\beta_{hv} \zeta^2 M_0 C_0}{\mu_v} \left( \frac{(1-\theta) \beta_{vh}}{\gamma_h + \delta_h + \mu_h} + \frac{\tilde{\theta} \tilde{\beta}_{vh}}{\tilde{\gamma}_h + \tilde{\mu}_h} \right) + \varphi_v^2} \right) \quad (19) $$

<a id='f2fdb5a3-6d1a-4642-881f-9c06ebf238b8'></a>

<::= \frac{\varphi_v}{2} + \sqrt{R_{hv}R_{vh} + \frac{\varphi_v^2}{4}}, (20)::>

<a id='bb053dd7-ed04-426a-a47f-1392c31c492b'></a>

where s(A) denotes the absolute value of the largest eigenvalue of A and where

<a id='0b3bf639-acdf-48b0-b9dc-571245ef42fb'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='95eb31af-b77c-4588-9b08-ba834a8d8290'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='bf055be9-f942-4b08-bfc6-238d0f0c822d'></a>

Chitnis et al.

<a id='57a06b1e-cc41-4c4d-beab-9eda8cf6e9e7'></a>

Page 14

<a id='558e0b22-6d52-42a6-b5f6-b7ed0219282b'></a>

<::R_{hv}=\frac{\nu_v}{\nu_v+\mu_v}\frac{\beta_{hv}\zeta C_0}{\mu_v}, (21): figure::>

<a id='70bbbc7a-f349-4bfd-a29d-abde447dee03'></a>

$$R_{vh} = \zeta M_0 \left( \frac{(1-\theta)\beta_{vh}}{\gamma_h+\delta_h+\mu_h} + \frac{\theta\tilde{\beta}_{vh}}{\tilde{\gamma}_h+\mu_h} \right) \text{ . (22)}$$

<a id='523327fb-6d62-4b3f-b28a-423579020603'></a>

**Theorem 3.3:** The disease-free equilibrium point, $x_{dfe}$ of the model for RVF without juvenile stages (7), is locally asymptotically stable when $\mathcal{R}_0$ < 1 and unstable when $\mathcal{R}_0$ > 1.

<a id='8071f2ee-93e2-45ac-b9dc-a0508d22f7b6'></a>

**Proof:** F(x), V⁻(x), and V⁺(x) satisfy assumptions (A1)–(A5) in [40] so this theorem is a straightforward application of Theorem 2 in [40].

<a id='dec03e10-ce6f-4091-a8a4-79dbaa2f5921'></a>

When there is no vertical transmission, φ_v = 0, R₀ resembles the basic reproductive number for malaria [9, (3.4)]. In that case, it is geometric mean of the number of new infections in livestock from one infected mosquito, R_hv, and the number of new infections in mosquitoes from one infected cow, R_vh, in the limiting case that both populations are fully susceptible. The number of new infections in cows from a newly infected mosquito, R_hv, is the product of the probability that the mosquito survives the exposed stage (v_v / (v_v + μ_v)), the number of bites on cows per mosquito (ζC₀), the probability of transmission per bite (β_hv), and the infectious life span of a mosquito (1/μ_v) [22]. The number of new infections in mosquitoes from one cow, R_vh, is the weighted sum of new infections resulting from asymptomatic and infectious cows. This is the product of the number of bites one cow receives (ζM₀), the probability of transmission per bite (β̃_vh for an asymptomatic cow and β_vh for an infectious cow), and the duration of the infective period (1/(γ_h + μ_h) for an asymptomatic cow and 1/(γ_h + δ_h + μ_h) for an infectious cow) weighted by the probability that a cow either becomes asymptomatic or infectious upon infection. In the presence of vertical transmission, φ_v > 0, R₀ increases because vertical transmission directly increases the number of infectious mosquitoes and indirectly increases the transmission from cows to mosquitoes and back to cows. We keep with the notation of the next generation operator methods [40] so the square root denotes the number of new infections from one infected cow to mosquitoes, or vice versa. R₀ then determines whether or not it is possible for RVF to be endemic in the population being considered.

<a id='fca72cdf-d9bc-4137-b335-3086a80c92ba'></a>

RVF is characterized by large outbreaks and periods of relative senescence so we also consider the reactivity (epidemicity) of the model, or the potential for the system to support transitory epidemics. Reactivity can be thought of as the maximum *instantaneous amplification rate* of the state variables from equilibrium following a perturbation [21]. The system is reactive when the amplification rate is positive, and not reactive when it is non-positive. For our case, reactivity is the spectral radius of the Hermitian part of the Jacobian for the system of the unscaled variables (1) evaluated at the disease-free equilibrium, $\tilde{\epsilon}_{0}=s(H(J_{0}))$, where $H(A)=(A+A^{T})/2$ is the Hermitian part of the matrix A [31].

<a id='81ce9ef9-8da5-4e41-8303-7469bac66338'></a>

Hosack et al. [21] derive a reactivity threshold, &, for the reactivity of a vector-host susceptible-infectious-recovered-type model. Near the disease-free equilibrium, for the

<a id='b92263b6-5bca-4855-b5eb-1275ec1769e6'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='d11d8fa5-9b35-4a73-a124-8e73ddb6a292'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='413d8868-e14f-42ab-9f30-11392b4167b9'></a>

Chitnis et al.

<a id='ea0519f1-ea70-4426-a2e7-fbf6674e71fc'></a>

Page 15

<a id='ff4c18ae-29c6-479a-981b-f22691939e95'></a>

system (1), ε₀ = s(H(F₀)H(V₀)⁻¹) (where F₀ and V₀ are defined in a similar manner to F₀ and V₀ except that they are evaluated for the unscaled model (1) instead of the scaled model (7)). If ε₀ > 1 then the system is reactive and an epidemic can result from a perturbation of the disease-free state. When considering the prevalence of infected individuals, one can think of the reactivity index ε₀ as being the _maximum_ number of secondary infections that could result from introducing one infectious individual into a fully susceptible population. For RVF, the most likely perturbation resulting in a transitory epidemic is the emergence of large numbers of adult mosquitoes, some of which are infected from birth via vertical transmission. As mentioned earlier, the general model (1) with its associated parameter values satisfies the assumption required for the analysis in [40] as well as in [21], including the condition that H(F₀) be non-negative and H(V₀) be non-singular with non-negative inverse. H(V₀) has a non-negative inverse when μᵥ² + νᵥμᵥ − (νᵥ/2)² > 0. For Equation (1), ε₀ does not have an easily interpreted analytic expression, so we compute it numerically for the baseline parameter values.

<a id='37ab8fc9-a264-4d85-800c-46bf32a7734e'></a>

**3.2.1. Extended model basic reproduction number and reactivity**—We use the same methods to compute the basic reproductive number and reactivity threshold for the extended model (12). Let *x* = (*a*<sub>h</sub>, *i*<sub>h</sub>, *i*<sub>e</sub>, *e*<sub>v</sub>, *i*<sub>v</sub>, *r*<sub>h</sub>, *N*<sub>h</sub>) and *dx*/*dt* = 𝓕₂(*x*) - 𝓥₂(*x*), where 𝓕₂(*x*) represents the rate of new infections entering the population, and 𝓥₂(*x*) = 𝓥₂⁻(*x*) - 𝓥₂⁺(*x*) represents the rate of movement (by other means) out of, and into, each compartment, respectively. We let *F*<sub>0,2</sub> and *V*<sub>0,2</sub> be the Jacobian matrices of the first five elements of 𝓕₂ and 𝓥₂, respectively, evaluated at the disease-free equilibrium, *x*<sub>dfe,2</sub>. Then, for the model with an explicit juvenile stage (12),

<a id='1b77a9f9-3eb7-4604-b074-ee8bafdab708'></a>

F_0,2 = \begin{bmatrix}
0 & 0 & 0 & 0 & \theta \beta_{hv} M_0 \zeta \\
0 & 0 & 0 & 0 & (1-\theta) \beta_{hv} M_0 \zeta \\
0 & 0 & 0 & 0 & \mu_v \varphi_v \\
\tilde{\beta}_{vh} C_0 \zeta & \beta_{vh} C_0 \zeta & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix} (23)

<a id='2e31fcb0-45df-4d53-a6c2-d6b49ae59d54'></a>

V_{0,2}=

<::transcription of the content
: $\begin{bmatrix}
\mu_h+\tilde{\gamma}_h & 0 & 0 & 0 & 0 \\
0 & \mu_h+\gamma_h+\delta_h & 0 & 0 & 0 \\
0 & 0 & \gamma_e & 0 & 0 \\
0 & 0 & 0 & \mu_v+\gamma_v & 0 \\
0 & 0 & -\gamma_e & -\nu_v & \mu_v
\end{bmatrix}$. (24)::>

<a id='5f57218b-88c7-464a-803a-ea0d38d32b48'></a>

The basic reproductive number is the spectral radius of the next generation matrix,
$(F_{0,2}V_{0,2}^{-1})$

<a id='d85b87d1-3689-4859-b99e-d84026a41caa'></a>

$$R_{0,2} = \frac{1}{2} \left( \varphi_v + \sqrt{4 \left( \frac{\nu_v}{\mu_v+\nu_v} \right) \left( \frac{\beta_{hv}\zeta^2 C_0 M_0}{\mu_v} \right) \left( \frac{(1-\theta)\beta_{vh}}{\gamma_h+\delta_h+\mu_h} + \frac{\theta\tilde{\beta}_{vh}}{\tilde{\gamma}_h+\tilde{\mu}_h} \right) + \varphi_v^2} \right) \quad (25)$$

<a id='3ba6743d-a9a7-4a17-a19e-20468e8abe2c'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='68c8d20b-62f2-4f69-8583-818c65833e0f'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<a id='b38eec36-6588-4ec1-b1db-6f1523646067'></a>

and

<!-- PAGE BREAK -->

<a id='0083476a-0786-4f45-96bd-a81d0e938ca2'></a>

Chitnis et al.

<a id='08c0e788-d996-46af-8dea-6f85be43034b'></a>

Page 16

<a id='7e8c72d0-1254-4cad-be9b-3d10a5aa4345'></a>

**Theorem 3.4:** The disease-free equilibrium point, $x_{dfe,2}$ of the model for RVF with explicit juvenile stages (12), is locally asymptotically stable when $R_{0,2} < 1$ and unstable when $R_{0,2} > 1$.

<a id='03d9055e-8791-42f6-adf7-0404bc390872'></a>

Proof: F₂(x), V₂⁻(x), and V₂⁺(x) satisfy assumptions (A1)–(A5) in [40] so this theorem is a straightforward application of Theorem 2 in [40].

<a id='ca7b0ed3-cb20-470e-9bc6-ca8a5737a30c'></a>

We note that $\mathcal{R}_0 = \mathcal{R}_{0,2}$, so explicitly including the juvenile stages in a manner similar to that used in [1] does not change the value of the basic reproductive number.

<a id='8785db0b-3df9-4c8f-b310-07e072a14c5b'></a>

The reactivity threshold of the unscaled model (9) around the disease-free equilibrium for the extended model is ε₀,₂ = s(H(F̂₀,₂)H(V̂₀,₂)⁻¹) (where F̂₀,₂ and V̂₀,₂ are defined in a similar manner to F₀,₂ and V₀,₂ except that they are evaluated for the unscaled model (9) instead of the scaled model (12)). Unlike the basic reproductive number, the reactivity index for the model with juvenile stages (9) is different from that of the original model (1). The effect of the larval stage cancels out for R₀ but remains a factor in the Hermitian parts of the next generation matrices and the Jacobian. It is important to note here that for some parameter values the condition that H(V̂₀) have a non-negative inverse is not met. The condition is met

<a id='ce8ed4de-5cfb-4952-b54e-6d18e94cddc7'></a>

when $\mu_v^2+\nu_v\mu_v-(\nu_v/2)^2>0$ and when $\mu_v - \gamma_e/4 > 0$. If it is not met, then we must instead use the original definition of reactivity $\mathcal{E}_{0,2} = s(H(J_{0,2}))$, where $J_{0,2}$ is the Jacobian of the unscaled RVF model with juvenile stages (9) evaluated at the disease-free equilibrium $x_{dfe,2}$, to determine whether our system is reactive.

<a id='a7d0163f-7a04-444d-8d49-0a6879f76fae'></a>

### 3.3. Endemic equilibrium points

Endemic equilibrium points are steady-state solutions where disease pers sts in the i population. While it is possible to explicitly solve for the endemic equilibrium point using symbolic software package such as *Mathematica*, the results are too complex to extract insight from. We therefore use a theorem by Rabinowitz [33] in a similar manner to that used in [9] to show the existence of an endemic equilibrium for all values of R₀ > 1.

<a id='17d0531c-6834-427f-af50-a085f42d8aca'></a>

We first rewrite the equilibrium equations of Equation (7) for $u = (a_h, i_h, e_v)$ as a nonlinear
eigenvalue problem in a Banach space,

<a id='33a6a123-1608-4291-81f5-4ed97796f484'></a>

u=G(ζ, u)=(ζLu+h(ζ,u), (26)

<a id='caba122b-2ed7-43ca-96df-1b19e82571a5'></a>

where u ∈ R³, with Euclidean norm, ||.||; ζ ∈ R (Equation (18)) is the bifurcation parameter;
L is a compact linear map on R³; and h(ζ, u) is O(||u||2) uniformly on bounded ζ intervals.
We also define Ω = R × R³ so that the pair (ζ, u) ∈ Ω.

<a id='c402585e-6e52-4656-9cf8-a6a2219c44af'></a>

A theorem by Rabinowitz [33, Theorem 1.3] states that if ζ₀ is a characteristic value (reciprocal of a real non-zero eigenvalue) of L of odd multiplicity, then there exists a continuum of non-trivial solution pairs, (ζ, u) of Equation (26) that intersects the trivial solution (i.e. (ζ, 0) for any ζ) at (ζ₀, 0) and either meets infinity in Ω (is unbounded) or meets (ζ̂₀, 0) where ζ₀ ≠ ζ̂₀ is also a characteristic value of L of odd multiplicity. We use this theorem to show that such a continuum of solution pairs (ζ, u) ∈ Ω exists for the eigenvalue equation (26) that meets infinity in Ω. We then show that to each of these solution pairs,

<a id='8a2c8239-0b46-4e2d-8aea-2e19f0ae68df'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='c939fb20-489f-4c01-8286-996df50ee43c'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='6930a925-78b7-46df-ba61-8eed00549e5a'></a>

Chitnis et al.

<a id='9571640a-8021-44d2-b354-a0a6e4570772'></a>

Page 17

<a id='74149b0f-b5c2-406b-88cb-94cff5e68bda'></a>

there corresponds an equilibrium pair (ζ, xee). We define the equilibrium pair, (ζ, xee) ∈ R × R^6, as the collection of a parameter value, ζ, and the corresponding equilibrium point, xee, for that parameter value, of the RVF model (7). We finally show that the range of ζ where this equilibrium pair exists corresponds to R_0 > 1.

<a id='3dd49751-d425-4770-8728-1bbdccfaed91'></a>

For the rest of this subsection, we use the variables, $a_h$, $i_h$, $r_h$, $N_h$, $e_v$, and $i_v$ to represent the equilibrium values of the state variables and not the values at any time $t$. We replace $\sigma_h$ and $\sigma_v$ with $\zeta$ and $\kappa = \sigma_h/\sigma_v$ to rewrite the equilibrium equations as

<a id='347be6df-7142-4d49-a2c3-3af1105ae682'></a>

\mu_h(C_0-N_h)-\delta_h i_h N_h=0, (27a)

<a id='96e729a0-24ad-421d-949e-89968c007b61'></a>

$$\zeta\left(\frac{M_0+\kappa C_0}{M_0+\kappa N_h}\right) M_0\theta_h\beta_h i_v(1-a_h-i_h-r_h) - \left(\tilde{\gamma}_h+\mu_h\frac{C_0}{N_h}\right) a_h+\delta_h i_h a_h=0, \quad (27b)$$

<a id='2fc9745a-5067-4eb4-86a1-3af33bf40e80'></a>

$\zeta\left(\frac{M_0+\kappa C_0}{M_0+\kappa N_h}\right)M_0(1-\theta_h)\beta_{hv}i_v(1-a_h-i_h-r_h)-\left(\gamma_h+\delta_h+\mu_h\frac{C_0}{N_h}\right)i_h+\delta_h i_h^2=0,\quad (27c)$

<a id='d7d4fd2c-a672-4c57-92b3-d3f756f4de49'></a>

$\tilde{\gamma}_h a_h + \gamma_h \dot{i}_h - r_h \mu_h \frac{C_0}{N_h} + \delta_h \dot{i}_h r_h = 0$, (27d)

<a id='3829fdac-89da-489c-a084-efaa6a65e985'></a>

\zeta\left(\frac{M_0+\kappa C_0}{M_0+\kappa N_h}\right)N_h(\tilde{\beta}_{vh}a_h+\beta_{vh}i_h)(1-e_v-i_v)-(\nu_v+\mu_v)e_v=0, (27e)

<a id='58822d43-4bc1-407a-854f-dcb765902006'></a>

νv ev − (1 − φv)μv iv = 0. (27f)

<a id='f38c7720-77da-473e-a407-839e638d4c7d'></a>

We solve Equations (27a), (27d), and (27f) for $N_h$, $r_h$, and $i_v$ in terms of $a_h$, $i_h$, and $e_v$,

<a id='9f2dd478-2318-42db-9f60-8d561593ac22'></a>

Nh = μh C0 / (μh + δh ih) (28a)

rh = (γ̃h ah + γh ih) / μh (28b)

iv = νv ev / ((1 - φv) μv) (28c)

<a id='40d1bcb5-afff-45dd-b05c-7af5a34345db'></a>

Substituting Equation (28) in, and taking the Taylor polynomial expansions of, the left-hand sides of Equations (27b), (27c), and (27e) with respect to a_h, i_h, and e_v around (0, 0, 0), we can rewrite Equations (27b), (27c), and (27e) in the form of Equation (26) with

<a id='4b5ea353-aad4-4735-8f8f-e87bbae0a6ab'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='a754e99e-e646-47c0-bb43-7dc9f1335d64'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='a66d9472-40fb-4bb2-b10e-6ebd88834bd2'></a>

Chitnis et al.

<a id='f1b007c2-1274-4e9f-a930-4d47f1502081'></a>

Page 18

<a id='3450b6c8-826f-4de1-a84e-547b2eac7727'></a>

u = (ah ih ev) and L = (0 0 L13, 0 0 L23, L31 L32 0) with

<a id='50e9a23c-9f59-46aa-b0ef-3cf9d213184f'></a>

L_13 = \frac{M_0 \beta_{hv} \theta_h \nu_v}{(\tilde{\gamma}_h + \mu_h) \mu_v (1-\psi_v)}, (29a)

<a id='7116b499-1258-4ea0-bde6-f8990ac68a5f'></a>

<::transcription of the content
: L23=M0βhv(1-θh)νv/(γh+δh+μh)μv(1-ψv) (29b)::>

<a id='15318bea-7c82-4a48-817d-a29c49860fe9'></a>

L31 = C0$\tilde{\beta}$vh / ($\mu$v + $\nu$v), (29c)

<a id='cdbb5cab-0740-4d10-8635-c6e26be931bb'></a>

L32 = C0βvh / (μv + νv) (29d)

<a id='2f129004-394f-4ab6-a359-d6cd99284885'></a>

The matrix $L$ has three eigenvalues: $-\sqrt{L_{13}L_{31}+L_{23}L_{32}}$, $0$, and, $\sqrt{L_{13}L_{31}+L_{23}L_{32}}$.
Therefore, the two characteristic values of $L$ are

<a id='814b9d61-ecc8-4414-9831-fc9ac908b8f8'></a>

$$\xi_1 = \frac{1}{\sqrt{L_{13}L_{31}+L_{23}L_{32}}} \sqrt{\frac{(\gamma_h+\delta_h+\mu_h)(\tilde{\gamma}_h+\mu_h)\mu_v(1-\psi_v)(\mu_v+\nu_v)}{M_0C_0\beta_{hv}\beta_{vh}\theta_h\nu_v(\gamma_h+\delta_h+\mu_h)+M_0C_0\beta_{hv}\beta_{vh}(1-\theta_h)\nu_v(\tilde{\gamma}_h+\mu_h)}} \quad (30a)$$

<a id='33a0feda-792f-4650-8ee8-698f64cedeff'></a>

$\xi_2 = - \sqrt{\frac{1}{L_{13}L_{31} + L_{23}L_{32}} \frac{(\gamma_h + \delta_h + \mu_h)(\tilde{\gamma}_h + \mu_h)\mu_v(1 - \psi_v)(\mu_v + \nu_v)}{M_0C_0\beta_{hv}\beta_{vh}\theta_h\nu_v(\gamma_h + \delta_h + \mu_h) + M_0C_0\beta_{hv}\beta_{vh}(1 - \theta_h)\nu_v(\tilde{\gamma}_h + \mu_h)}}$ (30b)

<a id='be91bf36-2180-4521-b747-c89d04d4fcba'></a>

The right eigenvectors corresponding to ξ₁ and ξ₂ are

$v_1=\frac{1}{\sqrt{L_{13}L_{31}+L_{23}L_{32}}} \left( \begin{array}{c}
L_{13}\\
L_{23}\\
\frac{L_{13}}{\sqrt{L_{13}L_{31}+L_{23}L_{32}}}
\end{array} \right)$

<a id='e5ecce23-1425-4c49-a621-2a6d71c632ad'></a>

and

<a id='2bac4e1c-f342-462c-a6f3-fe8ab5d6baa9'></a>

$$v_2 = \frac{1}{\sqrt{L_{13}L_{31}+L_{23}L_{32}}} \left( \begin{array}{c} -L_{13} \\ -L_{23} \\ \frac{-L_{23}}{\sqrt{L_{13}L_{31}+L_{23}L_{32}}} \end{array} \right),$$

<a id='2f23f802-9760-4719-8615-c7cfc928c4d4'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='6454a5b8-7c65-465c-8c55-90280ce25aed'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='82071404-f7e9-4bc3-ad6f-53b1978daa56'></a>

Chitnis et al.

<a id='aee384f9-5d48-4e93-b4a1-c6e918dbb648'></a>

Page 19

<a id='33840c25-6707-4d91-9e3a-5d7c6460dd29'></a>

respectively.

From Theorem 1.3 of Rabinowitz [33], we know that there is a continuum of solution pairs
(ζ, u) ∈ Ω, whose closure contains the point (ξ₁, 0), that either meets infinity (is unbounded)
or the point (ξ₂, 0). We denote the closure of a set *S* by *S̄* and denote the continuum of
solution pairs emanating from (ξ₁, 0) by 𝒞₁, where 𝒞₁ ⊂ Ω; and from (ξ₂, 0) by 𝒞₂, where 𝒞₂
⊂ Ω. We introduce the sets

<a id='14d2d3bd-b751-4db9-84a2-dee014bf1915'></a>

Z₁={ζ ∈ ℝ|∃u such that (ζ, u) ∈ 𝒞₁}, (31a)

U₁={u ∈ ℝ³|∃ζ such that (ζ, u) ∈ 𝒞₁}, (31b)

Z₂={ζ ∈ ℝ|∃u such that (ζ, u) ∈ 𝒞₂}, (31c)

U₂={u ∈ ℝ²|∃ζ such that (ζ, u) ∈ 𝒞₂}. (31d)

<a id='ddd6d4ae-1755-4b3f-8693-0594fb9eab99'></a>

**Lemma 3.5:** The initial direction of the branch of equilibrium points, near the bifurcation point ($\xi_1$, 0) (or ($\xi_2$, 0)), is equal to the right eigenvector of _L_ corresponding to the characteristic value $\xi_1$ (or $\xi_2$).

<a id='c2dee89e-0a33-496b-abd7-0df112f381ba'></a>

**Proof:** We use Lyapunov-Schmidt expansion, as described by Cushing [11], to determine the initial direction of the continua of solution pairs, ψ₁ and ψ₂. We expand the terms of the nonlinear eigenvalue equation (26) about the bifurcation point, (ξ₁, 0). The expanded variables are

<a id='1200141c-cd6d-4d98-b925-41d2ac703d52'></a>

u=0+εu^(1)+ε^2u^(2)+..., (32a)

<a id='560dc8ab-e0dd-4a50-8aa5-690f58aca0cd'></a>

\u03b6=\u03be\u2081+\u03b5\u03be\u2081+\u03b5\u00b2\u03b6\u2082+… , (32b)

<a id='8854f42a-6b26-4393-bd74-f7c6fda98cc1'></a>

h(ζ, u) = h(ξ_1 + εζ_1 + ε^2ζ_2 + ..., εu^(1) + ε^2u^(2) + ...)
= ε^2h_2(ξ_1, u^(1)) + ... (32c)

<a id='e3db6c9c-b49a-446a-b39b-c7037e4f5adb'></a>

Evaluating the substitution of the expansions (32) into the eigenvalue equation (26) at O(ε^1),
we obtain u^(1) = ξ₁Lu^(1). This implies that u^(1) is the right eigenvector of L corresponding to
the eigenvalue 1/ξ₁, v₁. Thus, close to the bifurcation point, the equilibrium point can be
approximated by a_h=εL₁₃/√(L₁₃L₃₁+L₂₃L₃₂), i_h=εL₂₃/√(L₁₃L₃₁+L₂₃L₃₂), and e_v = ε.

<a id='4299912a-a33c-431e-b44e-6c72d04cdd60'></a>

A similar expansion around the bifurcation point (ξ2, 0) would show that the initial direction of the branch of equilibrium points in the direction of the right eigenvector L corresponding to the eigenvalue 1/ξ2.

<a id='a2574664-11b4-4809-8fca-b611bee072a9'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='0de1d97a-211e-4d20-a09c-d46f25a7b3af'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='5d12ee12-2540-48db-8c59-5e23849a1f63'></a>

Chitnis et al.

<a id='b3d2abe9-b0ca-49e1-b63f-b6d7cb1603b0'></a>

Page 20

<a id='a55b7298-d9c4-431e-8838-25eda0d90c0d'></a>

__<ins>Lemma 3.6</ins>__: For all u ∈ U₁, aₕ > 0, iₕ > 0, and eₗ > 0.

<a id='432d63ec-b08b-42f5-bbff-ab6d9f7d4b0b'></a>

**Proof:** By Theorem 3.1, there are no equilibrium points on ∂R³₊ other than aₕ = iₕ = eᵥ = 0, so Ū₁ ∩ ∂R³₊ = 0. We know from Lemma 3.5 that close to the bifurcation point, (ξ₁, 0), the direction of U₁ is equal to v₁, the right eigenvector corresponding to the characteristic value, ξ₁. As v₁ contains only positive terms, U₁ is entirely contained in R³₊. Thus, for all u ∈ U₁, aₕ > 0, iₕ > 0, and eᵥ > 0.

<a id='8b64ee58-1327-4823-aa44-dc090ea66815'></a>

**Lemma 3.7:** The point u = 0 ∈ R³ corresponds to xdfe ∈ R⁶ (on ∂R⁶₊). For every solution pair (ζ, u) ∈ 𝒰₁, there corresponds one equilibrium pair (ζ, x*) ∈ R × R⁶, where x* is in the positive orthant of R⁶.

<a id='bff45560-57e7-4137-909b-3e942437bf04'></a>

**Proof:** We first show that _u_ = 0 corresponds to _x_dfe. As _a_h = _i_h = _e_v = 0, by Theorem 3.1 we know that the only possible equilibrium point is _x_dfe. We now show that for every \zeta \in Z_1 there exists an _x_* in the positive orthant of \mathbb{R}^6 for the corresponding _u_ \in _U_1. By Lemma 3.6, we know that _a_h > 0, _i_h > 0, and _e_v > 0. From Equation (28), we see that for every positive _a_h, _i_h, and _e_v, there exist corresponding positive _r_h, _N_h, and _i_v.

<a id='f8952405-7175-45c3-9344-6c0efa08e8ad'></a>

**Lemma 3.8**: The set Z₁ is unbounded.

<a id='80470ba9-0e7b-4570-9702-eb21da49b6b5'></a>

**Proof:** As shown in Lemma 3.6, U₁ ∩ ∂R³₊ = 0 and U₁ is entirely contained in R³₊. We can similarly show that U₂ is entirely outside of R³₊ because v₂ contains negative terms.

<a id='772a9c83-51b6-4905-8dec-7d5bb42bee6b'></a>

Therefore, C1 and C2 do not intersect and by Theorem 1.3 of Rabinowitz [33], C1 meets infinity. From Theorem 2.1, we know that the equilibrium points are bounded so U₁ does not meet infinity. Therefore, Z₁ must be unbounded.

<a id='89473916-ebac-4155-b482-7fe2a49462f1'></a>

**Theorem 3.9:** The transcritical bifurcation point at ζ = ζ_1 corresponds to R_0 = 1, and there exists at least one endemic equilibrium point of the RVF model (7) for all R_0 > 1.

<a id='ee1e5f51-743a-4924-80a4-0f222064da06'></a>

**Proof:** From Lemmas 3.7 and 3.8, we know that there exists a continuum of equilibrium pairs (ζ, x*) ∈ R × R⁶ that exists for all values of ζ > ξ₁.

<a id='0b82de79-b714-4a1b-835a-bab0af523158'></a>

Some algebraic manipulations after substituting $\zeta = \xi_1$ (Equation (30a)) into the definition of
$\mathcal{R}_0$ (Equation (20)) lead to $\mathcal{R}_0 = 1$. For any $\mathcal{R}_0 > 1$, Equation (20) defines a corresponding $\zeta >$
$\xi_1$, and therefore there exists a corresponding equilibrium point. It is possible, though not
necessary, for the continuum of equilibrium pairs to include values of $\zeta < \xi_1$ ($\mathcal{R}_0 < 1$).

<a id='f7c7fa37-38ee-45ba-9f2e-2740cc4af829'></a>

Thus, when R₀ > 1, the model (7) is guaranteed to have at least one endemic equilibrium point. Although we do not show its stability, we conjecture that this endemic equilibrium point is locally asymptotically stable for R₀ > 1.

<a id='33411ee6-a17e-4aa7-a992-89fb2f239a7f'></a>

### 3.3.1. Extended model endemic equilibrium points—For the RVF model with juvenile stages, we can show the existence of at least one endemic equilibrium point for all values of $\mathcal{R}_0$ > 1 in a similar manner to that for the model without juvenile stages. Compared

<a id='eb162286-1d80-4fe7-9030-3a97936ee0e2'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='170eef69-6613-4d37-bf51-31fd85f5d8ce'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='3cf58801-68b1-4670-b275-2511cb6dcc64'></a>

Chitnis et al.

<a id='9fd2cb7a-6ab5-4698-86e0-3815e282bea0'></a>

Page 21

<a id='d5cce828-29ec-4d8f-aeb2-91a8686f5bbd'></a>

to Equation (7), for Equation (12), the equilibrium point is in R^7 instead of R^6, there is an additional equilibrium equation,

<a id='883bbfec-62a6-4c70-a037-77ec3045dcd9'></a>

$\gamma_e\varphi_v i_v - \gamma_e i_e = 0, \quad (33a)$

<a id='7558d66b-5573-4d6a-8130-d5b87d2409b4'></a>

and the equilibrium equation (27f) is replaced by

<a id='b3a3bc42-06df-4a0b-8a9c-6b0394d7059d'></a>

μv̇ie + νvev - μvi̇v = 0. (33b)

<a id='b75a7267-267a-47d9-abc5-ce42dca1ac91'></a>

**Theorem 3.10:** The transcritical bifurcation point at ζ = ζ1 corresponds to R0 = 1, and there exists at least one endemic equilibrium point of the RVF model with juvenile stages (12) for all R0 > 1.

<a id='62a9e3c5-796f-4151-b4d6-24780ef64f93'></a>

**Proof:** Solving Equation (33a) for $i_e$ provides $i_e = \phi_i i_v$. Substituting $i_e$ in Equation (33b) provides $i_v = \nu_e i_v / (\mu_v(1 - \phi_v))$ as in Equation (28b). The rest of the proof follows as for the proof of Theorem 3.9 with the endemic equilibrium in $\mathbb{R}^7$.

<a id='961215b5-ccf5-4494-b8be-9e5462d32ec3'></a>

Again, while we do not show the stability of the endemic equilibrium point for the RVF
model with juvenile stages, we conjecture that it is locally asymptotically stable for $\mathcal{R}_0$ > 1.

<a id='4b323e71-f365-467c-88d6-6311dfdcd305'></a>

# 4. Sensitivity analysis

In determining how best to reduce cattle mortality and morbidity due to RVF, it is necessary to know the relative importance of the different factors responsible for its transmission and prevalence. Initial disease transmission and endemicity is directly related to R₀ and the potential size of outbreaks is directly related to ε₀. We calculate the sensitivity indices of the reproductive number R₀ and the reactivity index ε to the parameters in the model at baseline values described in Tables 3 and 4. These indices tell us how crucial each parameter is to disease transmission, epidemicity, and prevalence. Sensitivity analysis is commonly used to determine the robustness of model predictions to parameter values. Here we use it to discover parameters that have a high impact on R₀ and ε₀ and should be targeted by intervention strategies.

<a id='95ff3b72-8c2c-4d8d-8616-02ba8517ceb7'></a>

4.1. Description of sensitivity analysis
Local sensitivity indices allow us to measure the relative change in a state variable when a parameter changes. In computing the sensitivity analysis, we use methods described by Arriola [4]. The normalized forward sensitivity index of a variable to a parameter is the ratio of the relative change in the variable to the relative change in the parameter. When the variable is a differentiable function of the parameter, the sensitivity index may be alternatively defined using partial derivatives.

<a id='e073f365-6577-4219-94d8-4c3c97c4b559'></a>

**Definition 4.1:** The normalized forward sensitivity index of a variable, _u_, that depends differentiably on a parameter, _p_, is defined as

<a id='d7b93e3c-8370-4a65-8e50-d0ba26b2ca99'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='3003c058-58d8-418a-8774-0c341bc4c059'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='afdb161a-be30-435a-a570-5f5a8d6dc655'></a>

Chitnis et al.

<a id='8e1b9655-7aa4-4993-bfaf-68d247fd6996'></a>

Page 22

<a id='a1c4c8ec-6fb5-4ddc-a0c6-6713771b9daa'></a>

<::transcription of the content
: $\Gamma^u_p := \frac{\partial u}{\partial p} \times \frac{p}{u}$. (34)::>

<a id='f5e46101-e33c-4002-8445-625b3db84390'></a>

There is a detailed example of evaluating these sensitivity indices in [10].

<a id='4fd17d9e-026c-4145-b6f6-c52dcba395bf'></a>

## 4.2. Sensitivity indices of R₀

Since we have an explicit formula for R₀, we compute the sensitivity indices analytically at the baseline parameter values. R₀ is the same for the models with and without juvenile stages, hence the sensitivity indices are the same for both models. The indices Yₚᴿ⁰, or the local sensitivity of R₀ to a parameter p, are recorded in Table 5 for both the dry season and wet season. A simulation for an epidemic with wet season parameters and with R₀ = 2.28, with a fully susceptible host population and one infectious mosquito are shown in Figure 3. A similar simulation with dry season parameters with R₀ = 0.798 is shown in Figure 4.

<a id='35f71365-9f34-48e2-a62c-7608dcb7e3c2'></a>

For both seasons, R₀ is most sensitive to the mosquito biting rate σᵥ, so decreasing the mosquito biting rate by 10% would decrease R₀ by 7.3% for the dry season and 8.9% for the wet season. R₀ is also sensitive to the mosquito birth/death rate μᵥ, and the transmission rate from infected mosquito to cow βₕᵥ for both seasons. If μᵥ increases by 10% (so the lifespan of mosquitoes is decreased), then R₀ decreases by about 7% and if βₕᵥ increases by 10% then R₀ increases by about 4.7% for both wet and dry seasons (however, it would be difficult to

<a id='a48dc731-e26d-48a4-9710-2bbe2e29051d'></a>

decrease βhv in the field). Also, note that γ_C_0^(ℛ₀) = -γ_M_0^(ℛ₀). This is because the vector-to-host ratio is important in the initial spread of RVF for the parameter space being considered. Therefore, increasing the number of hosts while leaving the number of mosquitoes constant would decrease ℛ₀, while increasing the number of vectors and leaving the number of hosts constant would increase ℛ₀.

<a id='9bdb5239-dc71-4902-b4f2-1ac39c0e7be4'></a>

After the first three most sensitive parameters, the wet season and dry season sensitivity indices diverge. For the wet season, the next three parameters to which R₀ is most sensitive are the transmission from infected cow to mosquito β_vh, the number of bites a host can sustain σ_h, and the rate of recovery for infectious cows γ_h. The dry season is sensitive next to the carrying capacities of the mosquitoes and cows, M₀ and C₀, respectively, and to transmission from infected cow to mosquito β_vh. So we see that during the dry season when the number of mosquitoes is low, R₀ depends more on the vector-to-host ratio via M₀ and C₀. If C₀ is increased by 10% then R₀ decreases by 4.2% and if M₀ is decreased by 10% then R₀ will decrease by 4.2%. Finally, R₀ is not particularly sensitive to the vertical transmission rate Φ_v, although it is more important in the dry season with mosquito populations low. This indicates that as control measures for R₀ drive R₀ lower, vertical transmission may become more important.

<a id='f5a9c2a0-6926-4519-a6f9-204968d7e8f7'></a>

### 4.3. Sensitivity indices of ε₀
The reactivity index of the unscaled RVF model without juvenile stages in the wet season is ε₀ = 10.57. We show a simulation of the unscaled RVF model (1) for wet season parameters in Figure 5 with the effects of the changing population size through disease-induced mortality. Normally, the herd immunity is reached when the proportion of immune are

<a id='d3ab4589-cafd-43e6-b758-44067cefcb7a'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='638ac84b-9081-4c99-b872-8ed12578a1d8'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='0224ce62-a2e3-4208-8583-e6afcd6f0ee0'></a>

Chitnis et al.

<a id='accf9e8b-19d3-4d78-ba25-3055bad2a1c1'></a>

Page 23

<a id='d555e8a5-7777-4137-9eb8-96c36ab0a97e'></a>

above $1-1/\mathcal{R}_0^2$. However, in this simulation, pathogen transmission continues to occur at immune proportion values greater than $1-1/\mathcal{R}_0^2$ though still less than $1 - 1/\epsilon_0$. Though less so than the wet season, the dry season is also reactive, $\epsilon_0 = 1.84$, so given a strong enough perturbation an epidemic can still occur as shown in Figure 6.

<a id='94b20975-fc2c-4037-8b87-60f8991b2ef8'></a>

We summarize the numerical estimation of these indices in Table 6. The top five parameters to which E₀ is most sensitive are the same for both the wet season and the dry season, although the order changes between seasons. E₀ is most sensitive to the mosquito biting rate σv, the mosquito and cow carrying capacities M₀ and C₀, the transmission rate from infectious cow to mosquito βvh, and the death rate of mosquitoes μv. If σv increases by 10% then E₀ increases by 9.4% for wet and 7.4% for dry season; if βvh increases by 10% then E₀ increases by 7.9% for wet and 7.6% for dry season; if C₀ decreases by 10% or if M₀ increases by 10% then E₀ increases by 7.3% for wet and 9.1% for dry season.

<a id='c0a939f4-a731-4196-9067-17361baae339'></a>

Initial disease transmission $\mathcal{R}_0$ and epidemicity (or reactivity) $\mathcal{E}_0$ are more sensitive to different parameters, so control efforts must consider this. Different parameters will have more effect on endemicity and initial disease transmission than on the probability of a transient epidemic given a perturbation. For example, both $\mathcal{R}_0$ and $\mathcal{E}_0$ are sensitive to the mosquito biting rate $\sigma_v$ and the mosquito death rate $\mu_v$ for both seasons. However, changes in the vector-to-host ratio via the host and vector carrying capacities $C_0$ and $M_0$ will have a large effect on $\mathcal{E}_0$ in the wet season while not much of an effect on $\mathcal{R}_0$. $\mathcal{E}_0$ is also highly sensitive to $\beta_{vh}$ for both wet and dry seasons, while $\mathcal{R}_0$ is much less sensitive to the transmission from host to vector. It is possible for $\mathcal{R}_0$ to be low while reactivity is high, so that a large transient epidemic can occur (Figure 6). Therefore, controlling $\mathcal{E}_0$ may be important even when the basic reproductive ratio is below 1.

<a id='c0213b10-1a8b-4a0f-ae74-9e352952ebe8'></a>

## 4.4. Sensitivity of reactivity for the Juvenile model

For the model with juvenile stages with wet season parameter values, we cannot use the reactivity index ε₀,₂ since conditions for existence are not met for perturbations of wet season parameters, so instead we will consider sensitivity of the reactivity rate, ε, to the parameters. For the wet season, the reactivity rate ε₀,₂ is most sensitive (in order of importance) to the transmission rate from host to vector, βvh; the biting rate of the mosquitoes, σv; the host and vector carrying capacities, C₀ and M₀; the number of bites a host can sustain, σh; and the transmission from asymptomatic hosts to the vector, β̃vh. The dry season parameter values allow sensitivity analysis of the reactivity index, ε₀,₂. The reactivity index is most sensitive (in order of importance) to the vector biting rate σv; the host and vector carrying capacities, C₀ and M₀; the transmission rate from host to vector, βvh; the recovery rate of hosts, γh; and the transmission rate from asymptomatic host to vector, β̃vh.

<a id='08e36979-51c4-4c2a-ba17-bc547efb4f79'></a>

As with the original model, reactivity is insensitive to vertical transmission; however, it is more sensitive to vertical transmission for the dry season parameter set than for the wet season parameters. The extended model is also not sensitive at all to the larvae hatching rate during the wet season; it is slightly more sensitive to the hatching rate during the dry season. The sensitivity indices are summarized in Table 7. In conclusion, the extended juvenile

<a id='e0a904fb-ec5a-401a-8299-16a5c5c34f49'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='7285f3d4-8db5-44bc-b8cc-4d098a54238b'></a>

NIH-PA Author ManuscriptNIH-PA Author ManuscriptNIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='19efbeeb-541a-4050-b87e-ad98a1539d32'></a>

Chitnis et al.

<a id='e76e5052-feed-4018-a56f-a49cbbee2cc0'></a>

Page 24

<a id='9d09039a-6792-496a-b4a3-9b72b2481cf2'></a>

model for our parameter space is sensitive to the same major parameters that the original model is sensitive to.

<a id='3d7751fc-eccf-4ad8-855c-f09ff9f1755f'></a>

## 4.5. Global sensitivity analysis

In addition to the local sensitivity analysis, we performed global sensitivity analysis on R₀ and ε₀, showing the effects of variance in R₀ and ε₀ due to each parameter alone, as well as the influence of higher order effects. For the global analysis, we varied the parameters along the entire dry season and wet season range. We also varied the vertical transmission rate from 0 to 1 since the actual vertical transmission rate is not known. The global analysis confirms the local sensitivity results. Across the whole range, R₀ is most sensitive to the transmission probability from vector to host, vector death rate, vector biting rate, host recovery rate, carrying capacity of vectors, and the number of bites a host can sustain. Sensitivity to each of these parameters varies depending on whether we are considering the wet or dry season parameters. Vertical transmission can be important to R₀ if it ranges from 0 to 1. Across the whole range, ε₀ is most sensitive to host and vector carrying capacities, the vector death and biting rates, the probability of transmission from host to vector, and the number of bites a host can sustain. Global sensitivity analysis also indicates that higher order effects can be important. The effect of changing βhv on R₀ can vary depending on the values of the other parameters. This is especially true for the dry season parameter range, implying that for future studies a closer analysis of higher order interactions may be useful.

<a id='b217bbb7-cb41-4d54-9125-8010d36fb6a5'></a>

## 5. Numerical results with seasonality

We consider the introduction of RVF in a naive population in order to understand how it persists as it expands into new regions and to understand the history of its expansion over the past decades. The low-level endemic equilibrium for the wet/high season parameters is only reached after the disease effectively dies out following the first large epidemic (Figure 3). This is due to the high level of herd immunity reached in the hosts after the first epidemic in which many are infected. So in reality, even with wet season conditions all year, an endemic equilibrium would not be reached without some mode of inter-epidemic persistence such as long-lasting infected eggs or an introduced infected host. This suggests that seasonality combined with mosquito vertical transmission and/or introduction of new infected individuals after immunity wanes is necessary for the survival of RVF. Without these mechanisms, it is likely to die out within a year or two.

<a id='2bc9e241-a723-44f4-b7e2-4605406868ae'></a>

In order to explore inter-epidemic persistence, we consider a simple seasonal version of the model. To implement seasons, we run the simulations for the wet season for 182 days and the dry season for 183.25 days. Every wet season is followed by a dry season.
Compartments with less than one individual at the end of a season are set equal to zero. The simulation is run for 20 years. We assume that the eggs *Aedes* mosquitoes lay during the last 4 weeks of the wet season will overwinter and about 2/3 of them will survive and hatch in the next wet season [15]. Under these assumptions, RVF persists and eventually settles to endemic yearly cycles (Figure 7). However, under our assumptions, inter-epidemic persistence is very sensitive to the probability of vertical transmission: when *φ*v < 0.015, RVF dies out, and when *φ*v > 0.015, the disease persists on the scale we consider.
Alternatively, if an infected host were to be introduced at the opportune time, RVF could

<a id='50579adb-804e-4103-8946-0f8fa77edac6'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='4f08a7b0-030e-4a65-b184-ee9d6c4a99c3'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='1218e54a-00a6-44aa-a760-509dfe27f17c'></a>

Chitnis et al.

<a id='0094e3a6-6933-4d03-9961-560e9d79aa1c'></a>

Page 25

<a id='becefec6-63f4-4dc4-a8ab-d9ab2c52a912'></a>

reach the endemic yearly cycles observed in the simulations (Figure 7). Since both vertical transmission and the introduction of infected hosts at the right time are relatively rare events, we expect that both play a role in the persistence of RVF. Our simulations suggest that even low rates of vertical transmission can contribute significantly to inter-epidemic persistence. We do not include eggs that hatch several years after laid, an aspect of the system that could decrease the level of vertical transmission needed for persistence.

<a id='6fd7c248-d856-416b-93e7-416060b4c5a9'></a>

Next, we vary the rainfall via different mosquito wet season carrying capacities ($M_0$). As expected, more sporadic epidemics occur that look qualitatively similar to what is observed in the field (Figure 8). For varying rainfall, vertical transmission rates must be higher for persistence than with regular rainfall: for $\varphi_v < 0.03$ RVF dies out, while for $\varphi_v > 0.03$, it persists over the 20 years of the simulation. Again, vertical transmission with egg survival can explain persistence over the time frame of several years, but seems unlikely to account for decades-long persistence in a closed system. We would guess that low-level transmission in an alternate host or the introduction of infected individuals from outside the system would work along with vertical transmission to explain persistence of RVF.

<a id='76313fac-20f9-4b17-85ec-1408fb705c0f'></a>

For varied rainfall, we observe that particularly high rainfall (as in year 3) does not always result in an outbreak. However, the following year, which had normal wet season rainfall, saw a large epidemic. This hints at the importance of host–vector dynamics in addition to weather in explaining RVF outbreaks. Although unusually high rainfall is a good predictor for Kenya and East Africa, epidemics in West and South Africa do not always coincide well with abnormal weather events. This confirms the need for models that include disease, host, and vector dynamics in addition to weather data.

<a id='72f102b7-6aa8-41ba-b64c-bc9c90255495'></a>

# 5.1. Juvenile model
Numerical simulations of the juvenile class extension produce results quite similar to the original model with parameters describing the wet season alone or the dry season alone. Although the basic reproductive number, R₀, is the same for both the original and juvenile model, the reactivity index is slightly larger for the juvenile case than the original model, ε₀.₂ > ε₀.

<a id='b6810091-9bc8-404f-b9a8-dd8c75e3e800'></a>

For the seasonal case, if we reduce the hatching rate to zero during the dry season so that infectious eggs from the end of the wet season are stored, the results are similar to those of the original model with seasonality. As before, a threshold of vertical transmission probability of 0.015 is needed for persistence. For varying annual levels of rainfall, higher levels of vertical transmission are needed for persistence (vertical transmission probability of about 0.03). Figure 9 shows the infected eggs that survive the dry season and hatch at the beginning of the next wet season. The juvenile model confirms our results that vertical transmission can play an important role in RVF dynamics, especially in the presence of marked seasonality.

<a id='d5b4fc29-ab16-4655-9744-2c514e54ebbe'></a>

## 6. Discussion and conclusion

We extended Chitnis et al.'s [9] model to be applicable to RVF by including vertical transmission for *Aedes* mosquitoes and an asymptomatic class for livestock. The extended

<a id='9481dfe7-71ed-417f-823d-9d337ab53279'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='e7efd071-411d-4feb-b2f3-4161157a2b3b'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='66505e13-b2b6-465c-81ce-d2ae98932288'></a>

Chitnis et al.

<a id='cd9650cc-69e8-4f5f-8b68-12694dee2cc2'></a>

Page 26

<a id='09f0a0c4-13c6-44f7-a905-cd23abcf6376'></a>

model accounts for the population dynamics of both livestock and _Aedes_ mosquitoes and seasonal changes in weather that affects the mosquito population size. Mosquito densities vary greatly over seasons, and the contact rates vary dynamically based upon both the host and mosquito densities [9]. We also extended the model to include an aquatic juvenile stage and investigated the sensitivity of our predictions to including this juvenile class. We proved that both models are mathematically and epidemiologically well-posed, analysed the existence and the stability of disease-free equilibrium points, and proved the existence of endemic equilibrium points.

<a id='81593e9d-dd33-42a6-bcda-9e057ec48680'></a>

We derived an explicit formula for the basic reproductive number, R_0, and the reactivity index, ε_0. We compiled two baseline parameter ranges: one representing a wet season and one representing a dry season or a mitigated wet season. We then used local sensitivity analysis to define the sensitivity indices of R_0 and ε_0 and determined which parameters are most important to disease persistence and epidemicity in either the dry or the wet season. We found that including the aquatic stage does not significantly change the qualitative behaviour of the model, or the values of computed indices. However, if more complicated juvenile behaviour such as predation and larval competition were included, the aquatic stage may become more important. We also observed that the relative importance of the parameters in the extended juvenile model was about the same as the original model.

<a id='c01e9075-25a3-4a2f-a97f-9f3fb7ecca8f'></a>

The potential for large outbreaks, or epidemicity, of the system (for RVF parameters) is sensitive to the vector-to-host ratio as well as the mosquito biting rate and the probability of transmission from hosts to vectors. The basic reproductive number, on the other hand, was most sensitive to the mosquito biting rate, the mosquito death rate, and the probability of transmission from vector to host. Neither the basic reproductive number nor the reactivity index were sensitive to vertical transmission in mosquitoes. Adams and Boots [1] also found that the basic reproductive number for their dengue model was not sensitive to vertical transmission in mosquitoes.

<a id='f782bb3c-61c2-4763-9e08-ba171e88aea9'></a>

The sensitivity analysis suggests that control methods may vary depending on the season and on whether or not the goal is to reduce initial spread and endemicity, or epidemicity (reactivity). We found that R₀ is most sensitive to the mosquito biting rate, the lifetime of a mosquito, and the probability of transmission from vectors to hosts. After these three key parameters, the relative importance of the other model parameters depended upon the choice of wet season or dry season parameters. In the wet season, the next three most important parameters were the probability of transmission from hosts to vectors, the number of bites a host can sustain, and the rate of recovery for infectious hosts. In the dry season, the next most important parameters were the carrying capacities of the mosquitoes and cows, and the probability of transmission from hosts to vectors. These differences can help guide different mitigation strategies in wet and dry seasons.

<a id='0c169fc1-7d56-48d9-a4d8-5b3e5eb87523'></a>

Controlling the lifespan and biting rate of the mosquitoes will help control both the initial spread of disease and ongoing epidemics. However, if policymakers wish to decrease the probability of a large transient epidemic, reducing the overall numbers of vectors (or the vector-to-host ratio) and the probability of transmission from the host to the vector will be effective. If they wish to reduce the basic reproductive number, it would be better to focus

<a id='88610257-29c2-45f2-9ad6-53bf190fb8e4'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='555e4fc8-3e6b-4b4d-a1d6-8a8331b64430'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='ff59a448-1e55-45bd-bcca-0ac66a7b2c23'></a>

Chitnis et al.

<a id='b32ecdbc-3c7a-4f64-b8b8-3b30f28c3a70'></a>

Page 27

<a id='c4ae0ba2-ad41-4f3b-8106-8b643f794ffd'></a>

on the probability of transmission from vectors to hosts and on the number of bites a host will sustain.

<a id='ba80612d-c40f-4e3f-8587-4faa5a9299d6'></a>

If the basic reproductive number is less than 1 (as in the dry season case), we showed that the unique disease-free equilibrium is stable. However, the system is still reactive, so transient epidemics are possible even when R₀ < 1. If the basic reproductive number is greater than 1 (as in the wet season case), we proved that at least one endemic equilibrium exists. Our numerical simulations suggest that, if introduced to a naive population with wet season parameters, RVF will oscillate between transient large epidemics for several years before settling at a low endemic state. In fact, after the first large epidemic, the number of infected vectors and hosts falls well below 1 for over 2 years due to the large level of herd immunity reached. This indicates that RVF would probably die out after the first big outbreak. In order for RVF to persist between outbreaks, either an infected mosquito or infected host must be introduced to the system at the correct time. It is thought that *Aedes* mosquito eggs can survive from months to years before hatching at the next flood event. Thus, in regions where there are transient large epidemics, vertical transmission resulting in the hatching of infected mosquitoes could be playing a large role in the inter-epidemic persistence of RVF even if wet season conditions existed year round.

<a id='aab4b3cb-dc20-480f-baff-f569d31d91a4'></a>

Many RVF epidemics appear to be driven by seasonality. We explored a simple seasonal model to verify that long-term persistence of RVF with marked seasonality requires vertical transmission or introduction from outside the system of an infected host. In fact, if the system is closed, long-term persistence is sensitive to vertical transmission probability, requiring for our scenario a vertical transmission probability of 0.015–0.03 for persistence. These conditions may be relaxed if we expanded the model to include survival of eggs over multiple dry seasons rather than survival over only one dry season. We also considered varying rainfall over wet seasons, which is more realistic for many areas where RVF is endemic or invading. Again, vertical transmission is required for inter-epidemic persistence.

<a id='a3337f64-9bd4-44b3-9465-b091c4ec14b7'></a>

Vertical transmission in mosquitoes is often ignored in models for mosquito-borne pathogens. However, when mosquito populations follow seasonal patterns with large amplitudes, vertical transmission could play a significant role in long-term persistence of a pathogen. These results indicate that further exploration of vertical transmission rates and egg survival from both experimental and modelling perspectives is needed. More in-depth analysis of a seasonal version of the model is also warranted. In the future, we would like to adapt this model to include mitigation strategies and more complex mosquito dynamics, especially as better experimental and field data become available. In conclusion, although vertical transmission does not appear to affect epidemic dynamics significantly, the inter-epidemic persistence of mosquito-borne pathogens can be highly sensitive to vertical transmission rates.

<a id='3b739391-2158-4051-a687-b62d9b72e742'></a>

## Acknowledgments
This research (C.M. and J.H.) was partially supported by an NIH/NIGMS grant in the Models of Infectious Disease Agent Study (MIDAS) programme, 1U01GM097661-01 and an NSF/MPS/DMS grant DMS-1122666. We thank Kyle S. Hickmann for help with the global sensitivity analysis, and Ling Xue and an anonymous reviewer for valuable comments.

<a id='e55df750-7820-4a33-9229-ebc2e1c3e842'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='036843b4-07fe-4b47-a153-590cfac3b632'></a>

NIH-PA Author ManuscriptNIH-PA Author ManuscriptNIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='0450a624-cabc-42ec-b994-c76c9c8ec74e'></a>

Chitnis et al.

<a id='d8775024-e97c-43ef-b41b-bfd300ff293c'></a>

Page 28

<a id='71cb30d1-d8b1-4131-9844-95bb94676402'></a>

References

<a id='d7750158-bf00-4cd1-af72-88c8642e28d4'></a>

1. Adams B, Boots M. How important is vertical transmission in mosquitoes for the persistence of dengue? Insights from a mathematical model. Epidemics. 2010; 2(1):1-10. [PubMed: 21352772]
2. Andriamandimby SF, Randrianarivo-Solofoniaina AE, Jeanmaire EM, Ravololomanana L, Razafi- manantsoa LT, Rakotojoelinandrasana T, Razainirina J, Hoffmann J, Ravalohery JP, Rafisandratantsoa JT, Rollin PE, Reynes JM. Rift Valley fever during rainy seasons, Madagascar, 2008 and 2009. Emerg Infect Dis. 2010; 16(6):963-970. [PubMed: 20507747]
3. Anyamba A, Chretien JP, Small J, Tucker CJ, Formenty PB, Richardson JH, Britch SC, Schnabel DC, Erickson RL, Linthicum KJ. Prediction of a Rift Valley fever outbreak. Proc Natl Acad Sci. 2009; 106(3):955-959. [PubMed: 19144928]
4. Arriola, L. Sensitivity analysis for quantifying uncertainty in mathematical models. In: Chowell, G.; Hyman, JM.; Bettencourt, LMA.; Castillo-Chavez, C., editors. Mathematical and Statistical Estimation Approaches in Epidemiology. Springer; New York: 2009. p. 195-248.
5. Ba Y, Diallo D, Kebe CMF, Dia I, Diallo M. Aspects of bioecology of two Rift Valley fever virus vectors in Senegal (West Africa): Aedes vexans and Culex poicilipes (Diptera: Culicidae). J Med Entomol. 2005; 42(5):739-750. [PubMed: 16363157]
6. Balkhy HH, Memish ZA. Rift Valley fever: An uninvited zoonosis in the Arabian peninsula. Int J Antimicrob Agents. 2003; 21(2):153-157. [PubMed: 12615379]
7. Bird BH, Ksiazek TG, Nichol ST, MacLachlan NJ. Rift Valley fever virus. J Am Vet Med Assoc. 2009; 234(7):883-893. [PubMed: 19335238]
8. Chevalier V, Rocque S, Baldet T, Vial L, Roger F. Epidemiological processes involved in the emergence of vector-borne diseases: West Nile fever, Rift Valley fever, Japanese encephalitis and Crimean-Congo haemorrhagic fever. Rev Sci Tech - Office International des Epizooties. 2004; 23(2):535-556.
9. Chitnis N, Cushing JM, Hyman JM. Bifurcation analysis of a mathematical model for malaria transmission. SIAM J Appl Math. 2006; 67(1):24-45.
10. Chitnis N, Hyman JM, Cushing JM. Determining important parameters in the spread of malaria through the sensitivity analysis of a mathematical model. Bull Math Biol. 2008; 70(5):1272-1296. [PubMed: 18293044]
11. Cushing, JM. CBMS-NSF Regional Conference Series in Applied Mathematics. Vol. 71. SIAM; Philadelphia, PA: 1998. An Introduction to Structured Population Dynamics.
12. Davies, FG.; Martin, V. Recognizing Rift Valley Fever. FAO; Rome: 2003.
13. Depinay JMO, Mbogo CM, Killeen G, Knols B, Beier J, Carlson J, Dushoff J, Billingsley P, Mwambi H, Githure J, Toure AM, McKenzie FE. A simulation model of African Anopheles ecology and population dynamics for the analysis of malaria transmission. Malar J. 2004; 3(1):29. [PubMed: 15285781]
14. Diekmann O, Heesterbeek JAP, Metz JAJ. On the definition and the computation of the basic reproduction ratio R 0 in models for infectious diseases in heterogeneous populations. J Math Biol. 1990; 28(4):365-382. [PubMed: 2117040]
15. Favier C, Chalvet-Monfray K, Sabatier P, Lancelot R, Fontenille D, Dubois MA. Rift Valley fever in West Africa: The role of space in endemicity. Trop Med Int Health. 2006; 11(12):1878-1888. [PubMed: 17176353]
16. Gaff HD, Hartley DM, Leahy NP. An epidemiological model of Rift Valley fever. Electron J Differ Equ. 2007; 2007(115):1-12.
17. Gaff H, Burgess C, Jackson J, Niu T, Papelis Y, Hartley D. Mathematical model to assess the relative effectiveness of Rift Valley fever countermeasures. Int J Artif Life Res. 2011; 2(2):1-18.
18. Geering, WA.; Davies, FG.; Martin, V. Preparation of Rift Valley Fever Contingency Plans. Food & Agriculture Organization of the UN (FAO); Rome: 2002.
19. Gerdes GH. Rift Valley fever. Rev Sci Tech (International Office of Epizootics). 2004; 23(2):613-623.
20. Gong, H.; DeGaetano, A.; Harrington, LC. A climate based mosquito population model. Proceedings of the World Congress on Engineering and Computer Science 2007, WCECS 2007; San Francisco, CA. 24-26 October 2007;

<a id='097a437d-4b08-4ec9-b82f-f9dce37d61bc'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='71b40b95-97a2-4b25-a0be-d7143a2af96e'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='eda69513-06b7-426a-8ffc-30a09b1012ec'></a>

Chitnis et al.

<a id='b3646d8a-5c4c-468a-92bb-60f5bf208164'></a>

Page 29

<a id='2f202dbc-d817-4bf6-97a3-11a6557e5cae'></a>

21. Hosack GR, Rossignol PA, Van Den Driessche P. The control of vector-borne disease epidemics. J Theor Biol. 2008; 255(1):16-25. [PubMed: 18706917]
22. Hyman JM, Li J. An intuitive formulation for the reproductive number for the spread of diseases in heterogeneous populations. Math Biosci. 2000; 167(1):65–86. [PubMed: 10942787]
23. Jupp PG, Kemp A, Grobbelaar A, Leman P, Burt FJ, Alahmed AM, Mujalli D, Khamees M, Swanepoel R. The 2000 epidemic of Rift Valley fever in Saudi Arabia: Mosquito vector studies. Med Vet Entomol. 2002; 16(3):245-252. [PubMed: 12243225]
24. Kasari TR, Carr DA, Lynn TV, Weaver JT. Evaluation of pathways for release of Rift Valley fever virus into domestic ruminant livestock, ruminant wildlife, and human populations in the continental United States. J Am Vet Med Assoc. 2008; 232(4):514-529. [PubMed: 18279085]
25. Martin V, Chevalier V, Ceccato P, Anyamba A, De Simone L, Lubroth J, de La Rocque S, Domenech J. The impact of climate change on the epidemiology and control of Rift Valley fever. Rev Sci Tech - Office International des Epizooties. 2008; 27:413-426.
26. Mpeshe SC, Haario H, Tchuenche JM. A mathematical model of Rift Valley fever with human host. Acta Biotheor. 2011; 59(3-4):231-250. [PubMed: 21611886]
27. Murithi RM, Munyua P, Ithondeka PM, Macharia JM, Hightower A, Luman ET, Breiman RF, Njenga MK. Rift Valley fever in Kenya: History of epizootics and identification of vulnerable districts. Epidemiol Infect. 2011; 139(3):372-380. [PubMed: 20478084]
28. Muturi EJ, Muriu S, Shililu J, Mwangangi JM, Jacob BG, Mbogo C, Githure J, Novak RJ. Blood-feeding patterns of Culex quinquefasciatus and other culicines and implications for disease transmission in Mwea rice scheme, Kenya. Parasitol Res. 2008; 102(6):1329-1335. [PubMed: 18297310]
29. Ndiaye PI, Bicout DJ, Mondet B, Sabatier P. Rainfall triggered dynamics of Aedes mosquito aggressiveness. J Theor Biol. 2006; 243(2):222-229. [PubMed: 16876201]
30. Ndione PI, Besancenot JP, Lacaux JP, Sabatier P. Environnement et épidémiologie de la fièvre de la vallée du Rift (FVR) dans le bassin inférieur du fleuve Sénégal. Environnement, Risques & Santé. 2003; 2(3):176-182.
31. Neubert MG, Caswell H. Alternatives to resilience for measuring the responses of ecological systems to perturbations. Ecology. 1997; 78(3):653-665.
32. Pépin M, Bouloy M, Bird BH, Kemp A, Paweska J. Rift Valley fever virus (Bunyaviridae: Phlebovirus): An update on pathogenesis, molecular epidemiology, vectors, diagnostics and prevention. Vet Res. 2010; 41:61. [PubMed: 21188836]
33. Rabinowitz PH. Some global results for nonlinear eigenvalue problems. J Funct Anal. 1971; 7:487-513.
34. Romoser WS, Oviedo MN, Lerdthusnee K, Patrican LA, Turell MJ, Dohm DJ, Linthicum KJ, Bailey CL. Rift Valley fever virus-infected mosquito ova and associated pathology: Possible implications for endemic maintenance. Res Rep Trop Med. 2011; 2:121-127.
35. Rossignol PA, Ribeiro JM, Jungery M, Turell MJ, Spielman A, Bailey CL. Enhanced mosquito blood-finding success on parasitemic hosts: Evidence for vector-parasite mutualism. Proc Natl Acad Sci USA. 1985; 82(22):7725-7727. [PubMed: 3865192]
36. Shaman J, Day JF. Reproductive phase locking of mosquito populations in response to rainfall frequency. PloS One. 2007; 2(3):e331. [PubMed: 17396162]
37. Turell MJ, Rossi CA, Bailey CL. Effect of extrinsic incubation temperature on the ability of Aedes taeniorhynchus and Culex pipiens to transmit Rift Valley fever virus. Am J Trop Med Hyg. 1985; 34(6):1211-1218. [PubMed: 3834803]
38. Turell MJ, Presley SM, Gad AM, Cope SE, Dohm DJ, Morrill JC, Arthur RR. Vector competence of Egyptian mosquitoes for Rift Valley fever virus. Am J Trop Med Hyg. 1996; 54(2):136-139. [PubMed: 8619436]
39. Turell MJ, Linthicum KJ, Patrican LA, Davies FG, Kairo A, Bailey CL. Vector competence of selected African mosquito (diptera: Culicidae) species for Rift Valley fever virus. J Med Entomol. 2008; 45(1):102-108. [PubMed: 18283949]
40. Van den Driessche P, Watmough J. Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission. Math Biosci. 2002; 180(1):29-48. [PubMed: 12387915]

<a id='8d621dbc-fbcc-4990-bb36-dcc26d7ce953'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='81d38fc7-1b4f-4d09-92ce-c010f11dd5a1'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='5c7d51a7-110b-405c-8a02-5687aac35dae'></a>

Chitnis et al.

<a id='116b2b7e-b53b-4170-9e38-0497553ab1ac'></a>

Page 30

<a id='d75354b6-6a91-41d6-beb3-1cfc030edac9'></a>

41. Vignolles C, Lacaux JP, Tourre YM, Bigeard G, Ndione JA, Lafaye M. Rift Valley fever in a zone potentially occupied by Aedes vexans in Senegal: Dynamics and risk mapping. Geospatial Health. 2009; 3(2):211-220. [PubMed: 19440963]
42. Xue L, Scott HM, Cohnstaedt LW, Scoglio C. A network-based meta-population approach to model Rift Valley fever epidemics. J Theor Biol. 2012; 306:129-144. [PubMed: 22564391]

<a id='d8382bd7-b1c0-4a0d-ae67-a3a532124e9a'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='0f6e67e3-6433-4450-8c86-7e8406ec4dfd'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='0d223527-64d7-4b79-bbd0-49929d295853'></a>

Chitnis et al.

<a id='e3c0bb47-9310-4254-bcc7-2bd6bcc80b17'></a>

Page 31

<a id='29948f92-b868-4666-952c-4285e0f20926'></a>

<::Flowchart depicting a disease transmission model between Cattle and Mosquitoes.: flowchart::>

The model is divided into two main populations:

**Cattle (Host Population)**
Represented by an upper dashed box. This population includes:
*   **S_h (Susceptible Host):**
    *   Receives inflow `μ_h C_0` (birth/recruitment).
    *   Transitions to `I_h` with rate `(1-θ_h)λ_h`.
    *   Transitions to `A_h` with rate `θ_h λ_h`.
    *   Receives inflow from `I_v` (Infectious Mosquitoes) via an orange arrow.
    *   Exits the system (death/removal) with rate `μ_h`.
*   **I_h (Infected Host):**
    *   Transitions to `R_h` with rate `γ_h`.
    *   Transmits to `S_v` (Susceptible Mosquitoes) via an orange arrow.
    *   Exits the system (death/removal) with rate `μ_h`.
*   **A_h (Asymptomatic Host):**
    *   Transitions to `R_h` with rate `γ̃_h`.
    *   Transmits to `S_v` (Susceptible Mosquitoes) via an orange arrow.
    *   Exits the system (death/removal) with rate `μ_h`.
*   **R_h (Recovered Host):**
    *   Exits the system (death/removal) with rate `μ_h`.

**Mosquitoes (Vector Population)**
Represented by a lower dashed box. This population includes:
*   **S_v (Susceptible Vector):**
    *   Receives inflow `μ_v M_0` (birth/recruitment).
    *   Receives inflow from `I_v` (Infectious Mosquitoes) with rate `(1-φ_v)μ_v M_0`.
    *   Receives inflow from `I_h` (Infected Host) via an orange arrow.
    *   Receives inflow from `A_h` (Asymptomatic Host) via an orange arrow.
    *   Transitions to `E_v` with rate `λ_v`.
    *   Exits the system (death/removal) with rate `μ_v`.
*   **E_v (Exposed Vector):**
    *   Transitions to `I_v` with rate `ν_v`.
    *   Exits the system (death/removal) with rate `μ_v`.
*   **I_v (Infectious Vector):**
    *   Transitions to `S_v` with rate `(1-φ_v)μ_v M_0`.
    *   Has a self-loop (inflow) with rate `φ_v μ_v M_0` (green arrow).
    *   Transmits to `S_h` (Susceptible Host) via an orange arrow.
    *   Exits the system (death/removal) with rate `μ_v`.

<a id='9e2e321e-0777-48ab-96f2-79ca1550154f'></a>

Figure 1.
Susceptible cattle hosts, S_h, can be infected when they are bitten by infectious mosquitoes. Infected cattle either become infectious and sick, I_h, or asymptomatic carriers A_h (with a lower infectivity to mosquitoes). They then recover with a constant per capita recovery rate to enter the recovered, R_h, class. Susceptible mosquito vectors, S_v, can become infected when they bite infectious cattle. The infected mosquitoes then move through the exposed, E_v, and infectious, I_v, classes. Birth and death of the population are shown in the figure as well.

<a id='55647fd6-0a5d-4c6a-92b3-732371456d30'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='a3d25322-7656-4525-9302-79bdc9d1c19d'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='d0e03df4-b774-488c-bd52-c4f17825e4f6'></a>

Chitnis et al.

<a id='7651939c-069b-425f-821e-c08db6b249bf'></a>

Page 32

<a id='6ac5302b-a393-478d-993c-57853786f3f1'></a>

<::Compartmental model diagram: The diagram is divided into two main sections: 'Cattle' (top) and 'Mosquitoes' (bottom), each enclosed in a dashed rectangle. The compartments are represented by square boxes, and flows between them are indicated by arrows with associated rates or parameters. Cattle section: - Compartments: Sh (Susceptible Host), Ih (Infected Host), Ah (Asymptomatic Host), Rh (Recovered Host). - Flows:   - μhC0 into Sh (representing birth/recruitment).   - A self-loop on Sh labeled μhC0.   - Sh to Ih via (1-θh)λh.   - Sh to Ah via θhλh.   - Ih to Rh via γh.   - Ah to Rh via γ̃h.   - An outgoing arrow from the bracket encompassing Ih, Ah, Rh labeled μh (representing mortality). Mosquitoes section: - Compartments: Sv (Susceptible Vector), Ev (Exposed Vector), Iv (Infectious Vector). Additionally, two dark blue boxes represent Se (Susceptible Egg/Larvae) and Ie (Infected Egg/Larvae), grouped under 'Aquatic Stage'. - Flows:   - Sv to Ev via λv.   - Ev to Iv via νv.   - An outgoing arrow from the bracket encompassing Sv, Ev, Iv labeled μv (representing mortality).   - From Iv, two arrows originate:     - To Se via μvM0(1-φv).     - To Ie via μvM0φv.   - From Sv, an arrow points to Se via μvM0.   - Se to Sv via γe (emergence).   - Ie to Iv via γe (emergence). Inter-section flows (orange arrows): - From Ih to Sv. - From Ah to Sv.::>

<a id='8403fd8b-d2fe-41e1-9f92-63469e3d7479'></a>

Figure 2.
Susceptible cattle, S_h, can be infected when they are bitten by infectious mosquitoes.
Infected cattle either become infectious and sick, I_h, or asymptomatic carriers A_h (with a
lower infectivity to mosquitoes). They then recover with a constant per capita recovery rate
to enter the recovered, R_h, class. Susceptible mosquitoes, S_v, can become infected when they
bite infectious cattle. The infected mosquitoes then move through the exposed, E_v, and
infectious, I_v, classes. Birth and death of the population are shown in the figure as well. The
aquatic stage of mosquitoes is included explicitly, where some eggs laid by infectious
mosquitoes, I_v, are infected, I_e, and all other eggs are susceptible, S_e.

<a id='95642b74-12d8-4951-aea1-3dd1eb2f0cde'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='dad919fe-1e16-4e80-ad99-1f5b847de7d6'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='b8a918b0-0b01-447d-9a67-2a28ca98ef6b'></a>

Chitnis et al.

<a id='dbae92d5-f713-4438-b9a0-45b6adc74e86'></a>

Page 33

<a id='d2b12364-026a-40f9-9cde-68cdbeb76b70'></a>

<::chart: The figure displays two plots, (a) and (b), illustrating the solution of the RVF model (1) for wet season parameters with R₀ = 2.28. The initial conditions are S_h = 1000, A_h = I_h = R_h = 0, S_v = 19999, E_v = 0, and I_v = 1. The y-axis is on a log scale since the initial epizootic is much larger than subsequent outbreaks. (a) Hosts and (b) vectors. 

(a) Plot of host population against time. The x-axis is 'Time (years)' ranging from 0 to 10. The y-axis is 'Number of hosts' on a log scale, ranging from 10⁻² to 10². The plot shows three curves: 'Infectious' (solid blue line), 'Asymptomatic' (dashed red line), and 'Total Infected' (dotted gray line). All three curves start near 10² at time 0, peak sharply, then decrease, and show damped oscillations over time, converging to a lower value. The 'Total Infected' curve consistently stays above the 'Infectious' and 'Asymptomatic' curves, which largely overlap.

(b) Plot of exposed/infectious vectors against time. The x-axis is 'Time (years)' ranging from 0 to 10. The y-axis is 'Number of vectors' on a log scale, ranging from 10⁻¹ to 10⁴. The plot shows two curves: 'Exposed' (solid blue line) and 'Infectious' (dashed red line). Both curves start near 10³ at time 0, peak sharply, then decrease. The 'Exposed' curve shows a peak around 10³ at time 0, drops below 10⁰, then rises again, showing damped oscillations. The 'Infectious' curve shows a similar pattern but generally stays above the 'Exposed' curve after the initial peak, showing a peak around 10² between 2 and 3 years, and then another smaller peak around 10² between 5 and 6 years.::>

<a id='beb73fe2-7bb7-4235-b2ae-f87c5d5f889a'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='7f134778-51d0-445f-aaaa-86c57a6c2811'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='284308d2-b9d6-436b-9bc4-1c8e0231dd86'></a>

Chitnis et al.

<a id='13deb827-80df-4f44-b6cd-2893f3bcd2dd'></a>

Page 34

<a id='3b463bfc-1293-4776-9701-1ae85d7db621'></a>

<::chart: This figure, labeled (a) and (b), presents two plots related to the RVF model. (a) is a plot of host population against time, with 'Time (years)' on the x-axis (ranging from 0 to 2 in increments of 0.2) and 'Number of hosts' on the y-axis (ranging from 0 to 0.12 in increments of 0.02). The plot shows three curves: 'Infectious' (solid blue line), 'Asymptomatic' (dashed red line), and 'Total Infected' (dotted blue line). All three curves start low, rise to a peak (around 0.04-0.06 for 'Infectious' and 'Asymptomatic', and slightly higher for 'Total Infected') within the first 0.1-0.2 years, and then decay rapidly towards zero by approximately 0.8 to 1 year. The 'Infectious' and 'Asymptomatic' curves are very close, almost overlapping. (b) is a plot of exposed/infectious vectors against time, with 'Time (years)' on the x-axis (ranging from 0 to 2 in increments of 0.2) and 'Number of vectors' on the y-axis (ranging from 0 to 1 in increments of 0.1). This plot shows two curves: 'Exposed' (solid blue line) and 'Infectious' (dashed red line). The 'Infectious' curve starts at 1 and decreases rapidly, approaching zero by about 0.8 years. The 'Exposed' curve starts at 0, rises to a peak of approximately 0.3 around 0.1 years, and then decreases, approaching zero by about 0.8 years.::>Figure 4. Solution of the RVF model (1) for the dry season (or mitigated wet season) parameters with $\mathcal{R}_0 = 0.80$. The initial conditions are $S_h = 1000, A_h = I_h = R_h = 0, S_v = 3999, E_v = 0$, and $I_v =$ 1. (a) Hosts and (b) vectors.

<a id='26de7fef-af36-4cae-93cf-24bce4251042'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='d982d136-0cbe-4600-84ce-6d56396eb97c'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='c8d17683-970b-4da3-a352-4dd009d8e71f'></a>

Chitnis et al.

<a id='2e0a68ab-490f-4cbc-95a5-06a5222702a4'></a>

Page 35

<a id='90cbf1ee-7758-4401-b742-72bc35cbd270'></a>

<::chart: The image displays a line graph titled "Plot of host population against time". The x-axis is labeled "Time (years)" and ranges from 0 to 13. The y-axis is labeled "Number of hosts" and ranges from 0 to 1000. The graph shows five lines, as described in the legend: A magenta solid line represents the "Total" host population. A green solid line represents the "Recovered" host population. A purple dotted line represents "Nh*(1-1/R0)". A blue dashed line represents "Nh*(1-1/E0)". An aqua dotted line represents "Nh*(1-1/(R0)^2)".::>Figure 5. Solution of the RVF model (1) for the wet season parameters with $\mathcal{R}_0 = 2.28$ where the magenta line is total cattle and the green line is recovered cattle. The blue dashed line is $N_h(1 - 1/\epsilon_0)$, the purple dotted line is $N_h(1 - 1/\mathcal{R}_0)$, and the aqua dotted line is $N_h(1-1/\mathcal{R}_0^2)$. The initial conditions are $S_h = 1000$, $A_h = I_h = R_h = 0$, $S_v = 19999$, $E_v = 0$, and $I_v = 1$.

<a id='61b5d1ed-f390-4286-9975-000f828f6b37'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='a8e8e31e-03d3-41f1-9148-5c34ff8398fb'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='0a287c63-5caa-4776-85d3-d46ff292b55c'></a>

Chitnis et al.

<a id='4f5e2025-96b9-4ce5-a5b8-019c952a25fa'></a>

Page 36

<a id='9442a381-fa00-4441-a89d-82a872654fc9'></a>

<::Figure 6: A two-panel plot showing the solution of the RVF model. (a) Plot of host population against time. The y-axis is 'Number of hosts' (0 to 25) and the x-axis is 'Time (years)' (0 to 0.6). Three lines are plotted: 'Infectious' (solid blue line, peaking around 10 hosts), 'Asymptomatic' (dashed red line, peaking slightly below 10 hosts), and 'Total Infected' (dotted blue line, peaking around 20 hosts). All lines show an initial increase followed by a decline over time. The x-axis is labeled 'Hosts'. (b) Plot of exposed/infectious vectors against time. The y-axis is 'Number of vectors' (0 to 200) and the x-axis is 'Time (years)' (0 to 0.6). Two lines are plotted: 'Exposed' (solid blue line, starting at 0, rising to approximately 150 vectors, then declining) and 'Infectious' (dashed red line, starting at 200 vectors, declining, then rising slightly before declining again). The x-axis is labeled 'Vectors'. Figure 6. Solution of the RVF model (1) for the dry season parameters with initial conditions perturbed to wet season mosquito population levels and hatching infectious eggs. The initial conditions are Sh = 1000, Ah = Ih = Rh = 0, Sv = 19999, Ev = 0, and Iv = 200. The final number of cows infected is 300. (a) Hosts and (b) vectors.: chart::>

<a id='e83074db-2dd0-4cfa-9d2a-b818258643f7'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='fbbbdb4e-54ec-4f2b-96e3-cc404d705513'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='9d83f823-0f8f-4fab-b1e1-f80e6a2b961c'></a>

Chitnis et al.

<a id='ad4212ab-31c9-4bec-82de-ef25f127617b'></a>

Page 37

<a id='545f755f-ccf4-4a36-8a1d-dd5b20b1929b'></a>

<::chart:Figure 7. This figure displays four plots related to the solution of an RVF model with seasonality. The y-axis of subfigures (a) and (b) are on a log scale. A description of each subfigure is as follows: (a) Vectors First 5 Years. This plot shows the number of exposed and infectious vectors against time (years) for the first 5 years. The x-axis ranges from 0 to 5 years. The y-axis, labeled "Number of vectors", ranges from 10^0 to 10^3. The legend indicates "Exposed" with a solid blue line and "Infectious" with a dashed red line. The plot shows several peaks, with a large initial epizootic for infectious vectors in the first year, followed by smaller, distinct outbreaks in subsequent years. (b) Vectors. This plot shows the number of exposed and infectious vectors against time (years) for 15 years. The x-axis ranges from 0 to 15 years. The y-axis, labeled "Number of vectors", ranges from 10^-1 to 10^3. The legend indicates "Exposed" with a solid blue line and "Infectious" with a dashed red line. The plot shows yearly outbreaks of both exposed and infectious vectors, stabilizing after the first few years. (c) Recovered Hosts. This plot shows the host population against time (years) for 20 years. The x-axis ranges from 0 to 20 years. The y-axis, labeled "Number of hosts", ranges from 0 to 1000. The legend indicates "Recovered" with a dashed green line and "Total" with a solid magenta line. The total host population remains relatively stable, while the recovered host population increases and then fluctuates around a stable level. (d) Mosquitoes. This plot shows the number of vectors against time (years) for 15 years. The x-axis ranges from 0 to 15 years. The y-axis, labeled "Number of vectors", ranges from 0 to 2.5 x 10^4. The legend indicates "Total vectors" with a solid blue line. The plot shows a clear annual cycle where the total vector population sharply increases and then drops to near zero. The overall figure describes the solution of the RVF model (9) with seasonality, setting infected populations below 1 at the end of each season to 0. It is assumed the last 4 weeks of wet season adults contribute to the eggs that will hatch in the following wet season with a dry season survival rate of 2/3. Wet season parameters are used for 4 months, followed by dry season parameters with vector carrying capacity M₀ = 100. Subfigure (a) shows a large epizootic in the first year followed by many infectious mosquitoes hatching in year 2, and negligible infection in year 3 due to high levels of herd immunity. The exposed and infectious mosquito trajectories stabilize to yearly outbreaks after the first 5 or 6 years (subfigure (b)).::>

<a id='786b6623-ebd9-4734-8e04-d7dfbaa8dbf2'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='0ffba7a2-c325-4d39-bb3d-42e9de0d6830'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='59bf1aa1-88a6-4430-8c2a-2e9ca89b92fd'></a>

Chitnis et al.

<a id='08a51e3c-2321-494f-b08f-9ca53ff668a9'></a>

Page 38

<a id='537c2f3a-c80d-492d-a3f5-bd863c255de3'></a>

<::Figure: Four plots showing vector and host population dynamics over time.

(a) Plot of exposed/infectious vectors against time:
- X-axis: Time (years) from 0 to 6.
- Y-axis: Number of vectors, on a logarithmic scale from 10^0 to 10^3.
- Legend: Exposed (blue solid line), Infectious (red dashed line).
- Description: Shows oscillating patterns for both exposed and infectious vectors, with peaks around 0.5, 3.5, and 5 years, indicating periods of increased vector activity.

(b) Plot of infectious vectors against time:
- X-axis: Time (years) from 0 to 19.
- Y-axis: Number of vectors from 0 to 1400.
- Legend: Infectious (red solid line).
- Description: Displays fluctuating numbers of infectious vectors over a longer period, with significant spikes occurring around 0, 1, 17, and 18 years.

(c) Plot of host population against time:
- X-axis: Time (years) from 0 to 20.
- Y-axis: Number of hosts from 0 to 1000.
- Legend: Recovered (green dashed line), Total (purple solid line).
- Description: The total host population remains relatively stable, fluctuating between 800 and 900. The recovered host population shows an oscillating trend, generally increasing over time with periodic dips.

(d) Plot of vectors against time:
- X-axis: Time (years) from 0 to 19.
- Y-axis: Number of vectors, scaled by 10^4, ranging from 0 to 4.
- Legend: Total vectors (blue solid line).
- Description: Illustrates the total vector population over time, characterized by pronounced oscillations and major peaks around 0, 3, 10, and 18 years.::>

<a id='a55cfa0b-167c-4d04-8f57-acf3927937d7'></a>

Figure 8.
Solution of the RVF model (9) with seasonality and varying rainfall via changing wet season mosquito carrying capacity, setting infected populations below one at the end of each season to zero. It is assumed the last four weeks of wet season adults contribute to the eggs that will hatch in the following wet season with a dry season survival rate of 2/3. Subfigure (a) shows the first 6 years of epizootics on a log scale. Herd immunity, rainfall (via mosquito carrying capacity), and hatched infectious eggs from the previous year affect the timing and magnitude of outbreaks. Subfigure (b) shows infectious mosquitoes over a 19 year period.
(a) Hosts; (b) Vectors; (c) Recovered Hosts; (d) Mosquitoes.

<a id='df2254ba-5913-4631-9971-d939aa278d76'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='7306ee4b-faa5-416a-9eb5-6a466163be46'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='7210dae1-cd78-4b77-a858-16d71292f810'></a>

Chitnis et al.

<a id='527e5cd3-680d-4566-aae4-5e24587ca010'></a>

Page 39

<a id='1c77838c-d06e-4dbc-ae16-6e4035def633'></a>

<::Figure: The image displays Figure 9, which consists of two plots, (a) and (b), both titled "Plot of hatched infectious eggs". The y-axis for both plots is labeled "Number of infectious eggs" and is on a logarithmic scale from 10^0 to 10^2. The legend for both plots indicates "Total eggs" represented by a green line/bars.

Plot (a), subtitled "Uniform Seasons", shows the number of infectious eggs over "Time (years)" from 0 to 15. It features an initial peak around 0.5 years, followed by a decrease, and then a series of discrete vertical bars representing annual data points from year 2 to year 15, generally ranging between 10^1 and 10^2.

Plot (b), subtitled "Varying Seasons", also shows the number of infectious eggs over "Time (years)" from 0 to 19. Similar to plot (a), it has an initial peak and decrease, followed by annual discrete vertical bars from year 2 to year 19. The heights of these bars show more variability compared to plot (a), fluctuating significantly between 10^0 and 10^2.::>
Figure 9.

<a id='5d5334b4-4af3-49b5-9bd1-605b65029e47'></a>

Infected eggs that survive the dry season and hatch at the beginning of the next wet season for the RVF juvenile extension model (9) on a log scale with seasonality. Dry season hatch rate is very low ($\gamma_e = 0.005$) so that essentially no mosquitoes will hatch during the dry season. Subfigure (a) shows infectious eggs settling to yearly periodic levels, while varying rainfall results in varying numbers of infectious eggs hatching in subfigure (b). Years with large outbreaks result in infectious eggs hatching at significant levels during the wet season as well. (a) Uniform seasons; (b) Varying seasons.

<a id='6d7a9318-5530-4774-a857-dc812d4ad400'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='531d294a-13a8-4d83-a9b7-6f8a6f19d484'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='2002f961-592b-4514-810f-ca941ef2eb3b'></a>

Chitnis et al.

<a id='b0b6c11c-d6b4-4c76-85fd-2a7b9966325a'></a>

Page 40

<a id='2e093bf3-cb74-4fca-9827-c57fe60b218d'></a>

Table 1
The state variables for the RVF model (1).
<table><thead><tr><th>Variable</th><th>Description</th></tr></thead><tbody><tr><td>S<sub>h</sub></td><td>The number of susceptible cattle</td></tr><tr><td>A<sub>h</sub></td><td>The number of asymptomatic cattle</td></tr><tr><td>I<sub>h</sub></td><td>The number of infectious cattle</td></tr><tr><td>R<sub>h</sub></td><td>The number of recovered cattle</td></tr><tr><td>S<sub>v</sub></td><td>The number of susceptible <i>Aedes</i> mosquitoes</td></tr><tr><td>E<sub>v</sub></td><td>The number of exposed <i>Aedes</i> mosquitoes</td></tr><tr><td>I<sub>v</sub></td><td>The number of infectious <i>Aedes</i> mosquitoes</td></tr><tr><td>N<sub>h</sub></td><td>Total cattle population</td></tr><tr><td>N<sub>v</sub></td><td>Total <i>Aedes</i> mosquito population</td></tr><tr><td>S<sub>e</sub></td><td>The number of susceptible juvenile <i>Aedes</i> mosquitoes</td></tr><tr><td>I<sub>e</sub></td><td>The number of infected juvenile <i>Aedes</i> mosquitoes</td></tr><tr><td>N<sub>e</sub></td><td>Total <i>Aedes</i> juvenile population</td></tr></tbody></table>

<a id='26f6eed4-585c-4c01-b49a-23b9eadb49b2'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='c8f2d611-4323-41da-83e0-4523ae722be8'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='637abca1-c739-4436-bd5d-a99e529a821e'></a>

Chitnis et al.

<a id='bab6259f-ec54-453c-9af8-2017f6f7a239'></a>

Page 41

<a id='16585bfd-308f-48b8-be40-618307a82b57'></a>

Table 2
The parameters for the RVF model (1) and their dimensions.
<table><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>μh</td><td>Per capita birth/death rate of cattle, Time⁻¹</td></tr><tr><td>μv</td><td>Per capita birth/death rate of _Aedes_ mosquito species, Time⁻¹</td></tr><tr><td>φv</td><td>Probability of vertical transmission from an infectious _Aedes_ mosquito mother to its eggs, dimensionless</td></tr><tr><td>θh</td><td>Probability of an infected cow moving to the asymptomatic stage. (1 − θh) is the probability of an infected host moving to the infectious stage, dimensionless</td></tr><tr><td>σv</td><td>Number of times one mosquito would want to bite a cow per unit time, if cattle were freely available. This is a function of the mosquito's gonotrophic cycle (the amount of time a mosquito requires to produce eggs) and its preference for cattle blood, Time⁻¹</td></tr><tr><td>σh</td><td>The maximum number of mosquito bites a cow can sustain per unit time. This is a function of the cow's exposed surface area, the efforts it takes to prevent mosquito bites (such as switching its tail), and any vector control interventions in place to kill mosquitoes encountering cows or prevent bites, Time⁻¹</td></tr><tr><td>βhv</td><td>Probability of transmission of infection from an infectious mosquito to a susceptible cow given that a contact between the two occurs, dimensionless</td></tr><tr><td>βvh</td><td>Probability of transmission of infection from an infectious cow to a susceptible mosquito given that a contact between the two occurs, dimensionless</td></tr><tr><td>βvh˜</td><td>Probability of transmission of infection from an asymptomatic cow to a susceptible mosquito given that a contact between the two occurs, dimensionless</td></tr><tr><td>νv</td><td>Per capita rate of progression of mosquitoes from the exposed state to the infectious state. 1/νv is the average duration of the latent period, Time⁻¹</td></tr><tr><td>γh</td><td>Per capita recovery rate for cattle from the infectious state to the recovered state. 1/γh is the average duration of the infectious period, Time⁻¹</td></tr><tr><td>γh˜</td><td>Per capita recovery rate for cattle from the asymptomatic state to the recovered state. 1/γh˜ is the average duration of the infectious asymptomatic period, Time⁻¹</td></tr><tr><td>δh</td><td>Per capita disease-induced death rate for cattle, Time⁻¹</td></tr><tr><td>C0</td><td>Stable cattle population in the absence of disease, animals</td></tr><tr><td>M0</td><td>Stable mosquito population, animals</td></tr><tr><td>γe</td><td>Per capita rate of progression from egg to adult, Time⁻¹</td></tr></tbody></table>

<a id='4095d184-703e-4f96-8531-208c87bf6720'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='78b40515-5202-4add-9198-f31a379f74c8'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='047a62b0-f28e-42d4-aec7-05c99d1b59ae'></a>

Chitnis et al.

<a id='65d8f231-3e8a-4f29-aa27-85cee04e1791'></a>

Page 42

<a id='5a3900fb-2f00-4c8d-bf6d-17b225d29102'></a>

Table 3
The parameters for the RVF model for high rainfall and moderate temperatures (wet season) for Equation (1) with values, range, and references.

<a id='46133d9d-ebf8-40b6-8632-097627518420'></a>

<table id="41-1">
<tr><td id="41-2">Parameter</td><td id="41-3">Baseline</td><td id="41-4">Range</td><td id="41-5">Reference</td></tr>
<tr><td id="41-6">1/μh</td><td id="41-7">2190</td><td id="41-8">1825–2555</td><td id="41-9">[16,30]</td></tr>
<tr><td id="41-a">1/μv</td><td id="41-b">20</td><td id="41-c">10–30</td><td id="41-d">[13,16,24]</td></tr>
<tr><td id="41-e">φv</td><td id="41-f">0.1</td><td id="41-g">0–1</td><td id="41-h">[34]</td></tr>
<tr><td id="41-i">θh</td><td id="41-j">0.4</td><td id="41-k">0.3–0.6</td><td id="41-l">[7,32]</td></tr>
<tr><td id="41-m">σv</td><td id="41-n">0.33</td><td id="41-o">0.1-0.5</td><td id="41-p">[5,10]</td></tr>
<tr><td id="41-q">σh</td><td id="41-r">19</td><td id="41-s">0.1-50</td><td id="41-t">[10]</td></tr>
<tr><td id="41-u">βhv</td><td id="41-v">0.21</td><td id="41-w">0.001-0.54</td><td id="41-x">[23,32,37]</td></tr>
<tr><td id="41-y">βvh</td><td id="41-z">0.7</td><td id="41-A">0.3-0.9</td><td id="41-B">[23,32,37-39]</td></tr>
<tr><td id="41-C">β̃vh</td><td id="41-D">0.3</td><td id="41-E">0.1-0.5</td><td id="41-F">[10,32]</td></tr>
<tr><td id="41-G">1/v</td><td id="41-H">14</td><td id="41-I">7–20</td><td id="41-J">[5,23,37]</td></tr>
<tr><td id="41-K">1/γh</td><td id="41-L">4</td><td id="41-M">1–7</td><td id="41-N">[5,7,17,24]</td></tr>
<tr><td id="41-O">1/γh~</td><td id="41-P">4</td><td id="41-Q">1–7</td><td id="41-R">[7,24]</td></tr>
<tr><td id="41-S">δh</td><td id="41-T">0.10</td><td id="41-U">0.05–0.30</td><td id="41-V">[7,24]</td></tr>
<tr><td id="41-W">γe</td><td id="41-X">0.20</td><td id="41-Y">0.1–0.3</td><td id="41-Z"></td></tr>
<tr><td id="41-10">M0</td><td id="41-11">20,000</td><td id="41-12">15,000–25,000</td><td id="41-13">[17]</td></tr>
<tr><td id="41-14">C0</td><td id="41-15">1000</td><td id="41-16">500–2000</td><td id="41-17">[17]</td></tr>
</table>
Note: Time is in days.

<a id='7e24ec59-557a-47bd-ba23-084fa85401f5'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='639f2c63-be95-429a-8b91-11dbe2b5aa5c'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='2fbc40f0-dbc8-4f82-bda2-68255c82892f'></a>

Chitnis et al.

<a id='a6c6347a-128e-4d5c-b9ab-7e14b80a37de'></a>

Page 43

<a id='7f3002dc-3614-4d17-bc80-9c88568339bd'></a>

Table 4
The parameters for the RVF model for low moisture and moderate temperatures (dry season or wet season
with mitigation) for Equation (1) with values, range, and references.
<table id="42-1">
<tr><td id="42-2">Parameter</td><td id="42-3">Baseline</td><td id="42-4">Range</td><td id="42-5">Reference</td></tr>
<tr><td id="42-6">1/μh</td><td id="42-7">2190</td><td id="42-8">1825–2555</td><td id="42-9">[17,30]</td></tr>
<tr><td id="42-a">1/μv</td><td id="42-b">14</td><td id="42-c">7–20</td><td id="42-d">[13,24]</td></tr>
<tr><td id="42-e">φv</td><td id="42-f">0.1</td><td id="42-g">0–1</td><td id="42-h">[34]</td></tr>
<tr><td id="42-i">θh</td><td id="42-j">0.4</td><td id="42-k">0.3–0.6</td><td id="42-l">[7,32]</td></tr>
<tr><td id="42-m">σv</td><td id="42-n">0.25</td><td id="42-o">0.1–0.5</td><td id="42-p">[5,10]</td></tr>
<tr><td id="42-q">σh</td><td id="42-r">19</td><td id="42-s">0.1–50</td><td id="42-t">[10]</td></tr>
<tr><td id="42-u">βhv</td><td id="42-v">0.21</td><td id="42-w">0.001–0.54</td><td id="42-x">[23,32,37]</td></tr>
<tr><td id="42-y">βvh</td><td id="42-z">0.7</td><td id="42-A">0.3–0.9</td><td id="42-B">[23,32,37–39]</td></tr>
<tr><td id="42-C">β~vh</td><td id="42-D">0.3</td><td id="42-E">0.1–0.5</td><td id="42-F">[10,32]</td></tr>
<tr><td id="42-G">1/v</td><td id="42-H">14</td><td id="42-I">7–20</td><td id="42-J">[5,23,37]</td></tr>
<tr><td id="42-K">1/\gamma_h</td><td id="42-L">4</td><td id="42-M">1–7</td><td id="42-N">[5,7,24]</td></tr>
<tr><td id="42-O">1/\gamma_h^{-}</td><td id="42-P">4</td><td id="42-Q">1–7</td><td id="42-R">[7,24]</td></tr>
<tr><td id="42-S">\delta_h</td><td id="42-T">0.10</td><td id="42-U">0.05–0.30</td><td id="42-V">[7,24]</td></tr>
<tr><td id="42-W">\gamma_e</td><td id="42-X">0.10</td><td id="42-Y">0.05–0.2</td><td id="42-Z"></td></tr>
<tr><td id="42-10">M0</td><td id="42-11">4000</td><td id="42-12">3000-5000</td><td id="42-13">[17]</td></tr>
<tr><td id="42-14">C0</td><td id="42-15">1000</td><td id="42-16">500-2000</td><td id="42-17">[17]</td></tr>
</table>
Note: Time is in days.

<a id='7012891d-cbdc-4ed1-8f65-5754ce0a4138'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='ab764b06-6503-46ee-a6b8-049def9fadc0'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='83f76866-c0da-4db3-b3d3-9dec02d9ea8c'></a>

Chitnis et al.

<a id='16a6e6b1-bd35-460c-aa5d-7edeacf995c8'></a>

Page 44

<a id='2cd483dd-868a-4f4d-8953-6c860af147ab'></a>

Table 5
Sensitivity indices of R₀ (Equation (20)) to parameters for the RVF model, evaluated at the baseline parameter
values given in Tables 3 and 4.

<a id='4e1948e0-e999-4ffe-bd06-346e282c6963'></a>

<table id="43-1">
<tr><td id="43-2"></td><td id="43-3" colspan="2">Dry season</td><td id="43-4" colspan="2">Wet season</td></tr>
<tr><td id="43-5"></td><td id="43-6">Parameter</td><td id="43-7">Sensitivity index</td><td id="43-8">Parameter</td><td id="43-9">Sensitivity index</td></tr>
<tr><td id="43-a">1.</td><td id="43-b">σv</td><td id="43-c">+0.89</td><td id="43-d">σv</td><td id="43-e">+0.73</td></tr>
<tr><td id="43-f">2.</td><td id="43-g">μv</td><td id="43-h">-0.70</td><td id="43-i">μv</td><td id="43-j">-0.69</td></tr>
<tr><td id="43-k">3.</td><td id="43-l">βhv</td><td id="43-m">+0.47</td><td id="43-n">βhv</td><td id="43-o">+0.49</td></tr>
<tr><td id="43-p">4.</td><td id="43-q">C₀</td><td id="43-r">-0.42</td><td id="43-s">βvh</td><td id="43-t">+0.35</td></tr>
<tr><td id="43-u">5.</td><td id="43-v">M₀</td><td id="43-w">+0.42</td><td id="43-x">σh</td><td id="43-y">+0.25</td></tr>
<tr><td id="43-z">6.</td><td id="43-A">βvh</td><td id="43-B">+0.33</td><td id="43-C">γh</td><td id="43-D">-0.25</td></tr>
<tr><td id="43-E">7.</td><td id="43-F">γh</td><td id="43-G">-0.24</td><td id="43-H">C₀</td><td id="43-I">-0.24</td></tr>
<tr><td id="43-J">8.</td><td id="43-K">vᵥ</td><td id="43-L">+0.23</td><td id="43-M">M₀</td><td id="43-N">+0.24</td></tr>
<tr><td id="43-O">9.</td><td id="43-P">β̃h</td><td id="43-Q">+0.13</td><td id="43-R">vv</td><td id="43-S">+0.20</td></tr>
<tr><td id="43-T">10.</td><td id="43-U">γ̃h</td><td id="43-V">-0.13</td><td id="43-W">β̃vh</td><td id="43-X">+0.14</td></tr>
<tr><td id="43-Y">11.</td><td id="43-Z">δh</td><td id="43-10">-0.095</td><td id="43-11">γ̃h</td><td id="43-12">-0.14</td></tr>
<tr><td id="43-13">12.</td><td id="43-14">θh</td><td id="43-15">-0.089</td><td id="43-16">δh</td><td id="43-17">-0.10</td></tr>
<tr><td id="43-18">13.</td><td id="43-19">φv</td><td id="43-1a">+0.067</td><td id="43-1b">θh</td><td id="43-1c">-0.09</td></tr>
<tr><td id="43-1d">14.</td><td id="43-1e">σh</td><td id="43-1f">-0.047</td><td id="43-1g">φv</td><td id="43-1h">+0.022</td></tr>
<tr><td id="43-1i">15.</td><td id="43-1j">μh</td><td id="43-1k">-0.0007</td><td id="43-1l">μh</td><td id="43-1m">-0.0007</td></tr>
</table>

<a id='efd02ffb-4d90-44ea-81e3-7ec297224fc8'></a>

Notes: The parameters are ordered from most sensitive to least. For both wet and dry seasons, the most sensitive parameter is the mosquito biting rate, σv, and the least sensitive parameter is the cow death rate, μh. A negative sensitivity index indicates if the parameter increases, R₀ decreases, while a positive sensitivity index means that R₀ increases as the parameter increases.

<a id='bab7aa56-663a-4029-ae0a-0c2d2ca30343'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='b845a9d8-80b8-4f67-b192-e43294c832ff'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='34767160-3f4e-4b29-bfe2-8e8da2d7501f'></a>

Chitnis et al.

<a id='f71cdc22-3a2d-493f-b7c6-084b305fe169'></a>

Page 45

<a id='edfbc531-f7f6-4b19-8b50-b88d6c488bd9'></a>

Table 6
Sensitivity indices of &o to parameters for the RVF model (1), evaluated at the baseline parameter values given
in Tables 3 and 4.

<a id='f8c15c42-224f-490c-baad-37181c99c2de'></a>

<table id="44-1">
<tr><td id="44-2"></td><td id="44-3" colspan="2">Dry season</td><td id="44-4" colspan="2">Wet season</td></tr>
<tr><td id="44-5"></td><td id="44-6">Parameter</td><td id="44-7">Sensitivity index</td><td id="44-8">Parameter</td><td id="44-9">Sensitivity index</td></tr>
<tr><td id="44-a">1.</td><td id="44-b">σ</td><td id="44-c">+0.94</td><td id="44-d">βvh</td><td id="44-e">+0.79</td></tr>
<tr><td id="44-f">2.</td><td id="44-g">C₀</td><td id="44-h">-0.91</td><td id="44-i">σv</td><td id="44-j">+0.74</td></tr>
<tr><td id="44-k">3.</td><td id="44-l">M₀</td><td id="44-m">+0.91</td><td id="44-n">C₀</td><td id="44-o">-0.73</td></tr>
<tr><td id="44-p">4.</td><td id="44-q">Bvh</td><td id="44-r">+0.76</td><td id="44-s">Mo</td><td id="44-t">+0.73</td></tr>
<tr><td id="44-u">5.</td><td id="44-v">μν</td><td id="44-w">-0.39</td><td id="44-x">μν</td><td id="44-y">-0.40</td></tr>
<tr><td id="44-z">6.</td><td id="44-A">Yh</td><td id="44-B">-0.28</td><td id="44-C">Yh</td><td id="44-D">-0.28</td></tr>
<tr><td id="44-E">7.</td><td id="44-F">Boh</td><td id="44-G">+0.20</td><td id="44-H">ση</td><td id="44-I">+0.26</td></tr>
<tr><td id="44-J">8.</td><td id="44-K">δη</td><td id="44-L">-0.11</td><td id="44-M">Bvh</td><td id="44-N">+0.20</td></tr>
<tr><td id="44-O">9.</td><td id="44-P">vᵥ</td><td id="44-Q">-0.11</td><td id="44-R">δh</td><td id="44-S">-0.11</td></tr>
<tr><td id="44-T">10.</td><td id="44-U">γh</td><td id="44-V">-0.10</td><td id="44-W">γh</td><td id="44-X">-0.10</td></tr>
<tr><td id="44-Y">11.</td><td id="44-Z">σh</td><td id="44-10">+0.050</td><td id="44-11">vᵥ</td><td id="44-12">-0.10</td></tr>
<tr><td id="44-13">12.</td><td id="44-14">βhv</td><td id="44-15">+0.030</td><td id="44-16">βhv</td><td id="44-17">+0.0074</td></tr>
<tr><td id="44-18">13.</td><td id="44-19">φᵥ</td><td id="44-1a">+0.059</td><td id="44-1b">θh</td><td id="44-1c">-0.0014</td></tr>
<tr><td id="44-1d">14.</td><td id="44-1e">Θ₁</td><td id="44-1f">-0.056</td><td id="44-1g">φₛ</td><td id="44-1h">+0.0014</td></tr>
<tr><td id="44-1i">15.</td><td id="44-1j">µ₁</td><td id="44-1k">-0.0007</td><td id="44-1l">µ₁</td><td id="44-1m">-0.0007</td></tr>
</table>

<a id='1646fc47-22b4-4fee-a555-606abd4e899f'></a>

Notes: The parameters are ordered from most sensitive to least. For both wet and dry seasons, the least sensitive parameter is the cow death rate,
μh.

<a id='a76902ac-912b-4874-8de9-7f8fc6b7e262'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='4f06a91b-7873-49ee-94bb-ee7b68cf8e66'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='b951afe4-21db-4850-ab30-e5b8b817cc72'></a>

Chitnis et al.

<a id='9f999ee9-5c22-47ec-99ea-c3adef1e418b'></a>

Page 46

<a id='5a4ba8ff-eafc-42dd-a2b2-91c5b5a5b205'></a>

Table 7
Sensitivity indices of $\epsilon_{0.2}$ for the dry season and $\hat{\epsilon}_{0.2}$ for the wet season to parameters for the RVF model with juvenile stages (9), evaluated at the baseline parameter values given in Tables 3 and 4.

<a id='a51fd8fb-5d01-46a0-962e-d1850cb646d2'></a>

<table id="45-1">
<tr><td id="45-2"></td><td id="45-3" colspan="2">Dry season ( ε0,2)</td><td id="45-4" colspan="2">Wet season ( \vec{\epsilon}_{0.2})</td></tr>
<tr><td id="45-5"></td><td id="45-6">Parameter</td><td id="45-7">Sensitivity index</td><td id="45-8">Parameter</td><td id="45-9">Sensitivity index</td></tr>
<tr><td id="45-a">1.</td><td id="45-b">σv</td><td id="45-c">+0.94</td><td id="45-d">βvh</td><td id="45-e">+0.95</td></tr>
<tr><td id="45-f">2.</td><td id="45-g">C0</td><td id="45-h">-0.90</td><td id="45-i">σv</td><td id="45-j">+0.84</td></tr>
<tr><td id="45-k">3.</td><td id="45-l">M0</td><td id="45-m">+0.90</td><td id="45-n">C0</td><td id="45-o">-0.84</td></tr>
<tr><td id="45-p">4.</td><td id="45-q">Bvh</td><td id="45-r">+0.75</td><td id="45-s">Mo</td><td id="45-t">+0.84</td></tr>
<tr><td id="45-u">5.</td><td id="45-v">μν</td><td id="45-w">-0.57</td><td id="45-x">Oh</td><td id="45-y">+0.29</td></tr>
<tr><td id="45-z">6.</td><td id="45-A">Yh</td><td id="45-B">-0.28</td><td id="45-C">Bh</td><td id="45-D">+0.18</td></tr>
<tr><td id="45-E">7.</td><td id="45-F">Bh</td><td id="45-G">+0.20</td><td id="45-H">Yh</td><td id="45-I">-0.06</td></tr>
<tr><td id="45-J">8.</td><td id="45-K">δη</td><td id="45-L">-0.11</td><td id="45-M">δη</td><td id="45-N">-0.02</td></tr>
<tr><td id="45-O">9.</td><td id="45-P">γ̃h</td><td id="45-Q">-0.10</td><td id="45-R">νv</td><td id="45-S">-0.02</td></tr>
<tr><td id="45-T">10.</td><td id="45-U">γe</td><td id="45-V">+0.09</td><td id="45-W">μv</td><td id="45-X">-0.02</td></tr>
<tr><td id="45-Y">11.</td><td id="45-Z">σh</td><td id="45-10">+0.05</td><td id="45-11">γ̃h</td><td id="45-12">-0.01</td></tr>
<tr><td id="45-13">12.</td><td id="45-14">βhv</td><td id="45-15">+0.04</td><td id="45-16">βhv</td><td id="45-17">-0.0003</td></tr>
<tr><td id="45-18">13.</td><td id="45-19">νv</td><td id="45-1a">-0.02</td><td id="45-1b">θh</td><td id="45-1c">-0.0001</td></tr>
<tr><td id="45-1d">14.</td><td id="45-1e">θh</td><td id="45-1f">-0.008</td><td id="45-1g">μh</td><td id="45-1h">-0.0001</td></tr>
<tr><td id="45-1i">15.</td><td id="45-1j">ϕv</td><td id="45-1k">+0.007</td><td id="45-1l">γe</td><td id="45-1m">0</td></tr>
<tr><td id="45-1n">16.</td><td id="45-1o">μh</td><td id="45-1p">-0.0007</td><td id="45-1q">ϕv</td><td id="45-1r">0</td></tr>
</table>
Note: The parameters are ordered from most sensitive to least.

<a id='8c89fae8-ff0b-4fa8-bd60-0eb62b569303'></a>

J Biol Dyn. Author manuscript; available in PMC 2014 December 09.

<a id='ff071ff6-ec03-40b2-83a8-d237a56f0aac'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript
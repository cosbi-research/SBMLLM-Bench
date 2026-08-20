<a id='162b3e31-f96c-49a6-8223-1beea7ce78d3'></a>

<::logo: IEEE
IEEE
The logo features the letters "IEEE" in a bold, sans-serif font, accompanied by a stylized diamond-shaped symbol to its left, all in black on a white background.::>

<a id='dda7ca90-126f-42e5-bfc9-6f86e3671d15'></a>

Proceedings of the IEEE SoutheastCon 2015, April 9 - 12, 2015 - Fort Lauderdale, Florida

<a id='01f3f230-b5ef-41f0-8c75-4ce8c44ff828'></a>

A Comprehensive Model of Spread of Malaria in
Humans and Mosquitos

<a id='f4210e30-5bce-4483-bb35-52ae7e361de1'></a>

Amy Turner, Chanok Jung, Pan Tan, Srinivas Gotika, Vijay Mago*
Department of Computer Science, Troy University, Troy, AL - 36082
*Corresponding author: vmago@troy.edu

<a id='f2620c25-27f5-483f-a4be-8be8057c0681'></a>

Abstract—Mathematical models have the capability to incor-porate statistical data so that infectious diseases can be studied in-depth. In this article, we use mathematical modeling to study malaria through a combination of the Susceptible, Exposed, Infectious and Recovered (SEIR) Model for humans; Susceptible, Exposed and Infectious (SEI) Model for mosquitos; and the Four Stage Life Cycle Model of the mosquito. Due to the fact that malaria is spread to humans through the bite of a female mosquito that has been infected by the plasmodium parasite, the impacts of mosquitos are also studied in this paper using the SEI Model. Finally, the growth of the mosquito population is directly related to the spread of malaria, the Four Stage Life Cycle is incorporated to model the effects of climate change and interspecies competition within the mosquito life cycle stages of Egg, Larvae, and Pupae. The combination of these models are used to show the growth and spread of malaria.

<a id='12ccdfcb-31a7-4588-831e-a2f8b636c3f6'></a>

I. INTRODUCTION

Scientists have studied malaria transmission for over 100 years in hopes of finding a method of eradication. Malaria is still wide spread with the possibility of becoming a major source of death in certain areas [1]. According to the latest estimates, globally there are 198 million cases of malaria in 2013 and the disease has led to approximately 584,000 deaths in Africa [2]. Poverty, environment, and climate play major roles in the spread of the disease. The cause of malaria stems from the parasite *plasmodium falciparum*. This parasite inhabits female mosquitoes who then infect humans through biting. The disease is not communicable from human to human; however, if an infected human is bitten by a non-infected, susceptible mosquito, that mosquito may then become infected.

<a id='646b045f-6fdf-4616-81e9-a5c966c92a67'></a>

The study of malaria began with Sir Ronald Ross Ross[1]. In 1911, he developed the Ross Model (a very basic version of the current SEIR Model) whose parameters are shown in Table I. Later models, such as the Anderson and May model added the parameters of per capita rate of human mortality, latency, and immunity to the parameters developed by Ross[1].

<a id='e5ae44ab-4d57-4d52-9616-82216bb59ddb'></a>

TABLE I. Ross MODEL PARAMETERS
<table id="0-1">
<tr><td id="0-2">Symbol</td><td id="0-3">Parameter Description</td></tr>
<tr><td id="0-4">a</td><td id="0-5">Man biting rate</td></tr>
<tr><td id="0-6">b</td><td id="0-7">Prop of bites that produce infection in human</td></tr>
<tr><td id="0-8">c</td><td id="0-9">Prop of bites by which a susceptible mosquito become infected</td></tr>
<tr><td id="0-a">m</td><td id="0-b">Ratio of number of female mosquitos to that of humans</td></tr>
<tr><td id="0-c">r</td><td id="0-d">Average recovery rate of human</td></tr>
<tr><td id="0-e">μ1</td><td id="0-f">Per capita rate of human mortality</td></tr>
<tr><td id="0-g">μ2</td><td id="0-h">Per capita rate of mosquito mortality</td></tr>
<tr><td id="0-i">τm</td><td id="0-j">Latent period of mosquito</td></tr>
<tr><td id="0-k">τh i</td><td id="0-l">Latent period of human Immunity</td></tr>
</table>

<a id='2aea061f-7024-4fe8-b6a5-b1787363a974'></a>

Even with the numerous models and studies already in place, it is very difficult to have a thorough knowledge of all parameters that cause the spread of malaria. "Such understanding can only be reached by synthesizing the many factors controlling transmission, integrating detailed biological information into one coherent picture [3]." To address this issue, we have developed a more comprehensive model which includes spread of malaria in humans, mosquitos and how mosquito population impacts spread of malaria.

<a id='efc06d9f-6950-46a1-a3b2-96abf56b601f'></a>

In summary, we first look at the related works and the studies that have been conducted in this field. Then, we discuss our methodology which includes: the SEIR Model, SEI Model, and the Four Stage Life Cycle of the Mosquito and the parameters used in these models. Next, the experiments are discussed in context to various models by using already established values for different parameters. Finally, this paper shows the results obtained from our model and discusses topics for future research in the study of malaria.

<a id='0b2e2cad-a71c-4e23-84c8-6232f3e8a946'></a>

## II. RELATED WORKS

To model malaria properly, accurate statistics are necessary. In [4], the importance of diagnosing malaria in humans is shown. Malaria diagnosis is usually done in a passive way - only those patients exhibiting malaria symptoms are tested. For malaria to be modeled effectively, any patient with a possible exposure to malaria needs to be tested, so that accurate statistics can be documented and, so that, treatment can begin while still in the early stages of the disease.

<a id='ae47777d-42b4-46fb-9a6f-443d908e0171'></a>

While injections play a key role in the management of malaria, the injections are costly [5] and over time become ineffective against the disease. Other forms of prevention include insecticides and nets. Insecticides also become ineffective over time as malaria evolves to withstand the combatants. Mosquito nets appear to be the best and longest lasting form of prevention, and also does not cause a mutation in the disease. However, the prevention doesn't help us gain insight on how malaria spread from mosquitos to humans and among mosquitos.

<a id='050ee873-4e41-4967-98c1-de3fcc2cf5d9'></a>

When prevention methods such as injections, insecticides, or larvacides [6] are used, there is a following period called **interruption of transmission**. "Because interruption of transmission is a stochastic event, its occurrence depends on population size, as well as on R_e"(where R_e is the reproduction number)[7]. When the interruption in transmission occurs an immediate decrease in immunity follows, and in turn this causes an eventually increase in those infected by the disease. The state of disease requires close monitoring, so that in the

<a id='b50808c8-8e3a-46fb-9cbe-188c2e4d8197'></a>

978-1At72zzallarsbassented. UNIVERSITA TRENTO. Downloaded on December 22,2025 at 13:32:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE BREAK -->

<a id='af877402-a672-47fb-ac09-219274c66d4d'></a>

<::IEEE logo::>

<a id='45cb4b71-dc7d-448c-a254-916f7983a68b'></a>

Proceedings of the IEEE SoutheastCon 2015, April 9 - 12, 2015 - Fort Lauderdale, Florida

<a id='759ccfa2-e3fb-48e5-b598-caa05c72b45c'></a>

event of an interruption in transmission occurs a population's immunity can be artificially increased. This study highlighted the importance of stochastic events but fails to design a comprehensive model.

<a id='b3f307f6-58db-4b08-8af1-e2bae574aada'></a>

The main objective of some studies of malaria is dis-ease management and control. The authors of [8] show that mathematical models give large amounts of significant data to not only provide information on the disease itself, but also give insight and predictions into the outcomes of alternative courses of action. While the ability to study current prevention methods and their outcomes is necessary; it is important to go further and predict what effects new methods might have on the disease. For example, if insecticides are used to rid of an area of mosquitos, over time, humans in that area would lose the resistance they had built up while the mosquitos were present and biting. This loss of resistance and the methods by which the resistance is lost needs to be documented and studied to prevent future outbreaks in the event that the insecticide is no longer working.

<a id='cd299921-5864-4a3b-b9e0-87d61eeedd53'></a>

While most papers agree on the basic parameters necessary for the modeling of malaria growth and immunity, the authors of [9], state that the most important parameter for initial disease transmission is the mosquito biting rate. This rate is determined by multiple other parameters, including: mosquito birth rate, density-dependent mosquito death rate, and human rate of recovery. The second most important parameter for equilibrium disease prevalence in areas of high transmission is stated as the human rate of loss of immunity. While all other parameters remain consistent, loss of immunity evolves with the measures taken to combat it and it is this variable that determines the growth and spread of malaria. They also determined that the knowledge gained from the research of malaria is used in other areas of study, including determining the cost-effectiveness and usefulness of combatants being used in the prevention of malaria.

<a id='30817174-b0a7-4b26-ac84-023bebfed208'></a>

In [10], the authors focus on _Recovered_ individuals who return to the _Susceptible_ stage and the length of immunity they experience. Their paper is devoted to the basic idea that, relapse rate must be decreased for a prolonged period to increase the recovery rate. The main parameters used include relapse rate and recovery rate. Yet, in working with recovery, another study [11] shows the importance of vaccinations which has not been mentioned in this article. Since, no one vaccine can cure malaria, the vaccines must be geared toward creating longer immunity intervals and be modeled in the system.

<a id='280d5def-5832-4f2d-b03e-612c4ab0681f'></a>

Another area of study in the eradication of malaria is directly associated with mosquito re-population. Mosquitos are genetically altered in labs, then released into areas where malaria is prevalent. These genetically modified mosquitos will be the descendants of mosquitos that have been developed to have a natural immunity to the disease and are incapable of carrying or spreading the disease. When these mosquitos reproduce in the wild, their offspring will also have the same characteristics [12].

<a id='0041e723-b291-4608-8a17-789fc04eee99'></a>

In [13], the importance of modeling the life stages of the mosquito are noted. Not merely the susceptibility of the mosquito to malaria is necessary, but the life cycle and the factors that aid or prevent the growth of the mosquito population are also important. In this work, the mosquito life

<a id='d818868a-22ac-4ee0-a884-4ef8f2f5bc8a'></a>

cycle is divided into two classes - larvae and adult. The class
of larvae consists of three subclasses, which include: eggs,
larva, and pupa. Parameters involved in the development of
the larvae class include rainfall and intra-specific competition.
This study is used within this paper to develop the _ELP Model_.

<a id='f058a776-a98c-45a6-850d-c83cfb3d5ea4'></a>

The authors who used dynamical analysis of SEIR of an epidemic model [14] tried the perturbation method to get an analytical solution of the SEIR model. They then uses the statistics obtained from the model to compare the exact solution and the analytical solution. But in our paper, we focus on the dynamical analysis rather than the perturbation method. The perturbation method involves using nonlinear problems to develop numerous linear sub-problems and ending with the solutions to give approximate solutions.

<a id='4955c913-4aa4-4efd-af14-84120e116ef7'></a>

### III. METHODOLOGY

Using compartmental modeling [15] represented as a set of differential equations, the dynamics of malaria are modeled. The SEIR model is the first one we have defined and implemented. This model simulates the effect of the disease on humans. The SEI model is then designed to simulate the spread of malaria on mosquitoes. Finally, the Four Stage Life Cycle Model is used to add the importance the growth of the mosquito population has on malaria.

<a id='6f1067ea-490f-4038-8ac4-2560b152753b'></a>

A. Model 1: The SEIR model of humans
The SEIR Model can only be representative of humans due to the final compartment _Recovered_ or _R_. Once an individual recovers from malaria, they can become susceptible, again. Immunity to the strain of malaria from which they recovered will last, but the variations in the strains may cause the infection to be reproduced. The human SEIR model suggested by [16] is shown in Figure 1.

<a id='f943e5f7-572d-4c3a-a114-3bd45485b102'></a>

<::flowchart: Input Λh + ψhNh flows into Sh (Susceptible). From Sh, λh flows into Eh (Exposed). From Eh, νh flows into Ih (Infected). From Eh, fh(Nh) represents an outgoing rate. From Ih, γh flows into Rh (Recovered). From Ih, δIh represents an outgoing rate. From Ih, ρh flows back into Sh. From Rh, ρh flows back into Sh. Fig. 1. Human Model of SEIR [16]::>

<a id='a431bdee-64ea-4282-8952-28116d660b86'></a>

This model shows that given the immigration rate of humans (Λh) and adding birth rate, as well as the current total population, *Susceptible* population is calculated. From the *Susceptible* state, the per capita density-dependent death and emigration rate for humans is taken out(f_h(N_h)); and λ_h (infection rate for humans) is used to compute the size of population in the *Exposed* state. From there, the per capita rate of progression of humans exposed (ν_h) to the malaria is used to compute the size of population in the *Infectious* state; and the per capita disease-induced death rate(δ) for humans is taken out of the model. Finally, the per capita recovery rate (γ_h) is used to compute the number of people in the final stage of *Recovered*. At the *Recovered* stage, then per capita rate of loss of immunity (ρ) for humans is computed sending some *Recovered* back to the *Susceptible* stage. The model can be represented as a set of differential equations.

<a id='a340e9cd-e112-4ed2-ad30-b937b4bf5938'></a>

Authorized licensed use limited to: UNIVERSITA TRENTO. Downloaded on December 22,2025 at 13:32:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE BREAK -->

<a id='9f70d919-346b-4eba-bb8f-b7d3287a6ca6'></a>

<::logo: IEEE
IEEE
The logo features the letters "IEEE" in a bold, sans-serif font, accompanied by a stylized diamond-shaped symbol to its left, all in black on a white background.::>

<a id='e57b6462-7a4b-4fa4-b9b7-2ae66ea7cf9c'></a>

Proceedings of the IEEE SoutheastCon 2015, April 9-12, 2015 - Fort Lauderdale, Florida

<a id='1c1c21c6-0097-4586-9587-3c0d2cc3c57f'></a>

<::transcription of the content
$$\frac{dS_h}{dt} = \Lambda_h + \psi_h N_h + \rho_h R_h - \lambda_h(t) S_h - f_h(N_h) S_h$$

$$\frac{dE_h(t)}{dt} = \lambda_h(t) S_h - \nu_h E_h - f_h(N_h) E_h$$

$$\frac{dI_h}{dt} = \nu_h E_h - \gamma_h I_h - f_h(N_h) I_h - \delta_h I_h$$

$$\frac{dR_h}{dt} = \gamma_h I_h - \rho_h R_h - f_h(N_h) R_h$$
: figure::>

<a id='24acf45f-fe9c-4220-9e06-8c196251bfc4'></a>

where:
$N_h = S_h + E_h + I_h + R_h$

$f_h(N_h) = \mu_{1h} + \mu_{2h} N_h$

$\lambda_h = b_h(N_h, N_v)\beta_{hv} \frac{I_v}{N_v}$

$b_h(N_h, N_v) = \frac{\sigma_v N_v \sigma_h}{\sigma_h N_h + \sigma_h N_h}$

<a id='c587e0a9-ac8e-488e-bb70-58b45fe1bb7c'></a>

Parameters of this model are listed in the Table II

<a id='1f7d1c46-f36f-4063-8d60-4676d91728f3'></a>

TABLE II. PARAMETERS OF SEIR MODEL

<a id='c7fba55f-268f-4c6c-aa69-e7ec9708d4fe'></a>

<table><thead><tr><th>Symbol</th><th>Parameter Description</th></tr></thead><tbody><tr><td>Λ<sub>h</sub></td><td>Immigration rate</td></tr><tr><td>λ<sub>h</sub></td><td>P/capita infection rate</td></tr><tr><td>ψ<sub>h</sub></td><td>p/capita birth rate</td></tr><tr><td>σ<sub>h</sub></td><td>Max no. of mosquito bites p/unit of time</td></tr><tr><td>β<sub>hv</sub></td><td>Probability of transmission from M to H</td></tr><tr><td>ν<sub>h</sub></td><td>p/capita rate of progression from Exp to Inf</td></tr><tr><td>γ<sub>h</sub></td><td>p/capita recovery rate</td></tr><tr><td>δ<sub>h</sub></td><td>p/capita disease-induced death rate</td></tr><tr><td>ρ<sub>h</sub></td><td>p/capita rate of loss of immunity</td></tr><tr><td>μ<sub>1h</sub></td><td>density IND part of death/emigration rate</td></tr><tr><td>μ<sub>2h</sub></td><td>density dep. part of death/emigration rate</td></tr><tr><td>σ<sub>v</sub></td><td>Times 1 mosquito would bite a human p/unit of time</td></tr><tr><td>b<sub>h</sub></td><td>per capita birth rate of human</td></tr></tbody></table>

<a id='a3b1dede-f666-4912-8ee0-76372b1bf8cf'></a>

B. *Model 2: The SEI model of mosquitos*
Using the same strategy of developing compartments, the model for mosquitos has been designed. The compartments are: Susceptible - Exposed - Infected (SEI). Since, the mosquitos can't be treated of malaria, so we assume that all the infected mosquitos eventually die and this assumption is coherent with other studies [17]. Figure 2 shows the model.

<a id='591bb31e-7d4c-4470-8d1f-ab1f8c7a8fed'></a>

<::Flowchart: A diagram showing a process. An arrow points from `ψ_v N_v` to a shaded box labeled `S_v`. From `S_v`, an arrow labeled `λ_v` points to a shaded box labeled `E_v`. From `E_v`, an arrow labeled `ν_v` points to a shaded box labeled `I_v`. Downward arrows point from `S_v`, `E_v`, and `I_v` to a common label `f_v(N_v)`.::>

<a id='04c80e54-bc4f-49b5-9cea-f32defba5be7'></a>

Fig. 2. Mosquito Model of SEI[16]

<a id='2db8850a-f499-4cd2-9a2f-da2247e214a2'></a>

NOTE: An avid reader can see that the above presented model is
quite similar to the previous one, but the an exception that the X_v is
used to represent the mosquito.

<a id='308c71a4-e61a-406b-9259-72b8f4d68002'></a>

The set of differential equations representing the SEI model are shown below:

$$\frac{dS_v}{dt} = \psi_v N_v - \lambda_v(t)S_v - f_v(N_v)S_v$$

$$\frac{dE_v}{dt} = \lambda_v(t)S_v - \nu_v E_v - f_v(N_v)E_v$$

<a id='a49288e1-c432-46e5-9974-90c47b650287'></a>

$$\frac{dI_\nu}{dt} = \nu_\nu E_\nu - f_\nu(N_\nu)I_\nu$$

<a id='297a6ffa-a810-4a49-9ae9-b2a40c45386f'></a>

where:

*N*<sub>*v*</sub> = *S*<sub>*v*</sub> + *E*<sub>*v*</sub> + *I*<sub>*v*</sub>

*f*<sub>*v*</sub>(*N*<sub>*v*</sub>) = *μ*<sub>1*v*</sub> + *μ*<sub>2*v*</sub>*N*<sub>*v*</sub>

*λ*<sub>*v*</sub> = *b*<sub>*v*</sub>(*N*<sub>*h*</sub>, *N*<sub>*v*</sub>)(*β*<sub>*vh*</sub> *I*<sub>*h*</sub>/*N*<sub>*h*</sub> + *β̃*<sub>*vh*</sub> *R*<sub>*h*</sub>/*N*<sub>*h*</sub>)

*b*<sub>*v*</sub>(*N*<sub>*h*</sub>, *N*<sub>*v*</sub>) = (*σ*<sub>*v*</sub>*N*<sub>*h*</sub>*σ*<sub>*h*</sub>) / (*σ*<sub>*v*</sub>*N*<sub>*v*</sub> + *σ*<sub>*h*</sub>*N*<sub>*h*</sub>)

<a id='7a83ca53-bf73-472a-a104-f74130bc94cb'></a>

Description of the parameters of this model is given in Table III

<a id='c512c956-c3d8-4a1c-b9e2-41c333f40cdf'></a>

TABLE III. PARAMETERS OF SEI MODEL
<table id="2-1">
<tr><td id="2-2">Symbol</td><td id="2-3">Parameter Description</td></tr>
<tr><td id="2-4">λv</td><td id="2-5">P/capita infection rate of mosquito</td></tr>
<tr><td id="2-6">ψv</td><td id="2-7">Per capita birth rate</td></tr>
<tr><td id="2-8">σv</td><td id="2-9">Times 1 mosquito would a human p/unit of time</td></tr>
<tr><td id="2-a">βvh</td><td id="2-b">Probability of transmission from infected human to susceptible mosquito</td></tr>
<tr><td id="2-c">βvh</td><td id="2-d">Probability of transmission from recovered human to susceptible mosquito</td></tr>
<tr><td id="2-e">νv</td><td id="2-f">p/capita rate of progression from Exposed to Infected</td></tr>
<tr><td id="2-g">μ1v</td><td id="2-h">density independent part of death rate</td></tr>
<tr><td id="2-i">μ2v</td><td id="2-j">density dependent part of death rate</td></tr>
<tr><td id="2-k">bv</td><td id="2-l">per capita birth rate of mosquito</td></tr>
<tr><td id="2-m">σ_h</td><td id="2-n">Max no. of mosquito bites p/unit of time</td></tr>
</table>

<a id='574fd5fc-58aa-440e-873f-41b25ce65284'></a>

C. Model 3: The ELP model of mosquitos

The final piece of model design in this paper involves the connection of the mosquito life cycle stages to the growth and spread of malaria. The mosquito life cycle is broken down into four stages: Eggs (E), Larvae (L), Pupae (P), and Adult. The model is represented as follows:

`dE/dt = A r_e p - E(T_e + M_e)`

`dL/dt = E T_e - L(T_l + M_l) - K_0 L^2`

`dP/dt = L T_l - P(T_p + M_p)`

<a id='aa6d9264-aae0-4777-91d6-d06eb560c91b'></a>

where Ar is the reproducing adult mosquitos, ep is the number of eggs per oviposition, Te is the time taken for an egg to develop, Me is the egg mortality rate, Ko is the carrying capacity term, Ti is the larval development time, Tp is the pupal development time, Mp is the pupal mortality, and Mi is the larval mortality. Further details of the parameters can be found in [18]. The parameters involved infer that geo-climate and interspecies competition determine the growth rate of the mosquito population which, in turn, determines the rate at which malaria spreads. We implemented this model prior to the implementation of SEIR and SEI models in order to show the importance of the mosquito population on malaria.

<a id='b6887c35-2191-44f7-8caa-d0d0ba1fcfad'></a>

IV. EXPERIMENTATION

There are three models and these models interact with each other. We implemented the ELP model first because we assume that the output of this model provides us the input, i.e., the mosquito population of the SEI model. We used the $R_h$ from the SEIR model to the compute transmission rate $\lambda_v$ of mosquitos in the SEI model. So, we will introduce the experimentation related to ELP first, then SEI and finally the SEIR. Also, the initial parameter values for this comprehensive models are listed in Table IV.

<a id='b84706bb-a88a-4411-8237-90dd7c03a756'></a>

Authorized licensed use limited to: UNIVERSITA TRENTO. Downloaded on December 22,2025 at 13:32:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE BREAK -->

<a id='55913027-6e4e-42e3-aa97-ee459fdc378f'></a>

<::logo: IEEE
IEEE
This logo features a stylized diamond shape with a smaller diamond inside, followed by the text "IEEE" in a bold, sans-serif font.::>

<a id='212468db-2ee0-43f5-8234-3f8ddb7a38bf'></a>

Proceedings of the IEEE SoutheastCon 2015, April 9 - 12, 2015 - Fort Lauderdale, Florida

<a id='00d2acd6-ac02-403d-a04c-bb2224c3015d'></a>

TABLE IV. GENERIC PARAMETER VALUES
<table id="3-1">
<tr><td id="3-2">Parameter</td><td id="3-3">Parameter Value</td></tr>
<tr><td id="3-4">TimeSEIR</td><td id="3-5">0-1000</td></tr>
<tr><td id="3-6">TimeELP</td><td id="3-7">0-50</td></tr>
<tr><td id="3-8">TimesEI</td><td id="3-9">0-100</td></tr>
<tr><td id="3-a">POPH</td><td id="3-b">560</td></tr>
<tr><td id="3-c">POPM</td><td id="3-d">2500</td></tr>
<tr><td id="3-e">POPELP</td><td id="3-f">18000</td></tr>
<tr><td id="3-g">[E-L-P]</td><td id="3-h">[10000-5000-3000]</td></tr>
<tr><td id="3-i">[S-E-I]</td><td id="3-j">[P*0.8-S*0.02-E*0.0001]</td></tr>
<tr><td id="3-k">[S-E-I-R]</td><td id="3-l">[500-50-10-5]</td></tr>
</table>

<a id='3c5620db-0965-4694-8e21-c6d272adb24d'></a>

TABLE V. ELP PARAMETERS [18]
<table id="3-m">
<tr><td id="3-n">Symbol</td><td id="3-o">Parameter Description</td><td id="3-p">Values</td></tr>
<tr><td id="3-q">A r</td><td id="3-r">Reproducing adults</td><td id="3-s">20</td></tr>
<tr><td id="3-t">e p</td><td id="3-u">Eggs per oviposition</td><td id="3-v">30</td></tr>
<tr><td id="3-w">T e</td><td id="3-x">Egg development time</td><td id="3-y">0.361</td></tr>
<tr><td id="3-z">M e</td><td id="3-A">Egg mortality</td><td id="3-B">0.05</td></tr>
<tr><td id="3-C">K₀</td><td id="3-D">Carrying capacity term</td><td id="3-E">2 * 10⁻⁴</td></tr>
<tr><td id="3-F">Tₗ</td><td id="3-G">Larval development time</td><td id="3-H">0.134</td></tr>
<tr><td id="3-I">Tₚ</td><td id="3-J">Pupal development time</td><td id="3-K">0.342</td></tr>
<tr><td id="3-L">Mₚ</td><td id="3-M">Pupal mortality</td><td id="3-N">0.0025</td></tr>
<tr><td id="3-O">Mₗ</td><td id="3-P">Larval mortality</td><td id="3-Q">0.0501</td></tr>
</table>

<a id='9577dcff-ae98-430a-a5aa-11f0730d7d53'></a>

Fig. 3. Egg Stage<::chart::>ELP Population-Egg. The chart displays two lines over time. The Y-axis is labeled "ELP - Mosquito Population" ranging from 0 to 18000. The X-axis is labeled "Time (days)" ranging from 0 to 50. A blue solid line represents "Egg" population, starting around 10000 and decreasing over time to below 2000. A dotted line represents "Total Population", remaining constant at approximately 18000.<::>A. Model 1: The EPL model of mosquitos

<a id='7cc3a11e-a107-4d6b-80c6-288131fde410'></a>

In this model, we use various parameter values as suggested in [18] for the ELP Model. These are listed in Table V.

<a id='c7d138d6-1456-46b6-8bef-4a0cb6b4b9f2'></a>

Figure 3 represents the Egg stage of the mosquito life cycle. In this representation not all eggs will survive to the next stage of Larvae, that is why, we see a drop in the number of eggs as the time progresses. Figure 4, represents the Larvae and Pupae stages. These stages will also lose population due to various factors including interspecies competition and rainfall. Figure 5, represents the ELP stages as a whole.

<a id='8acd61c4-45d1-4fcb-bf89-5870a768faec'></a>

Fig. 4. Larvae and Pupae Stages
<::This is a line chart titled "ELP Larvae-Pupae". The y-axis is labeled "ELP - Mosquito Population" and ranges from 0 to 5000. The x-axis is labeled "Time(days)" and ranges from 0 to 50. The chart displays two lines: one red line representing "Larvae" and one cyan line representing "Pupae". Both lines start at high values and decrease over time, eventually leveling off. The Larvae population starts near 5000 and stabilizes around 1200, while the Pupae population starts near 3000 and stabilizes around 400.: chart::>

<a id='1d7af795-da8a-47e4-8839-7269a8cf5d74'></a>

Fig. 5. ELP Model Output
<::chart: The chart is titled "Eggs-Larvae-Pupae". The x-axis is labeled "Time(days)" and ranges from 0 to 50. The y-axis is labeled "ELP - Mosquito Population" and ranges from 0 to 10000. The chart displays three lines:
- "Egg" (blue line): Starts around 9500 and decreases rapidly, stabilizing around 1200 after approximately 15 days.
- "Larvae" (orange line): Starts around 5000 and decreases rapidly, stabilizing around 1000 after approximately 15 days.
- "Pupae" (yellow line): Starts around 3000 and decreases rapidly, stabilizing around 500 after approximately 15 days.
All three lines show an initial sharp decline followed by a plateau.
::>

B. Model 2: The SEI model of mosquitos
In this model, we use various parameters suggested in [16] for
the SEI Model. These are listed in Table VI.

<a id='c73763e2-e235-475c-b314-fcb51a9af07d'></a>

TABLE VI. PARAMETERS OF SEI MODEL
<table id="3-R">
<tr><td id="3-S">Symbol</td><td id="3-T">Parameter Description</td><td id="3-U">Values</td></tr>
<tr><td id="3-V">λv ψv</td><td id="3-W">P/capita infection rate of mosquito Per capita birth rate</td><td id="3-X">See Model 2 80</td></tr>
<tr><td id="3-Y">σv</td><td id="3-Z">Times 1 mosquito would a human p/unit of time</td><td id="3-10">0.6000</td></tr>
<tr><td id="3-11">bhv</td><td id="3-12">Probability of transmission from M to H</td><td id="3-13">2.000 x 10⁻²</td></tr>
<tr><td id="3-14">bvh</td><td id="3-15">Probability of transmission from H to M</td><td id="3-16">0.8333</td></tr>
<tr><td id="3-17">v_v</td><td id="3-18">p/capita rate of progression from Exp to Inf</td><td id="3-19">0.1000</td></tr>
<tr><td id="3-1a">μ_1v</td><td id="3-1b">density IND part of death rate</td><td id="3-1c">0.1429</td></tr>
<tr><td id="3-1d">μ_2v</td><td id="3-1e">density dep. part of death rate</td><td id="3-1f">2.279 x 10⁻⁶</td></tr>
<tr><td id="3-1g">b_v</td><td id="3-1h">per capita birth rate of mosquito</td><td id="3-1i">See Model 2</td></tr>
</table>

<a id='4f0cdaed-9a60-4d40-8367-686396a6a212'></a>

Fig. 6. Susceptible Stage<::A line graph titled "Mosquito Population-Susceptible" plots "Mosquitos Population" on the y-axis (ranging from 0 to 2500) against "Time(days)" on the x-axis (ranging from 0 to 100). The legend indicates two series: "Susceptible" (blue line) and "Total Population" (green dots). The "Total Population" remains constant at 2500 throughout the 100 days. The "Susceptible" population starts at 2500, sharply declines to near 0 within the first 10-20 days, and then stays at approximately 0 for the remainder of the 100 days.: chart::>Figure 6, represents the Susceptible stage of the population. In this experimentation, we used a total population count of 2500 to begin the process. The number of Susceptible mosquitoes was calculated by multiplying the total population by the per capita birth rate.

<a id='fc3e32b4-6b91-4989-9124-2d4703d4f691'></a>

Fig. 7. Exposed and Infected Stages<::line chart::>The chart is titled "Mosquito Exposed-Infected". The x-axis is labeled "Time(days)" and ranges from 0 to 100. The y-axis is labeled "Mosquitos Population" and ranges from 0 to 2.5 x 10^5. The chart displays two lines representing population changes over time: The "Exposed" population (red line) starts at 0, increases sharply to a peak of approximately 2.25 x 10^5 around day 5, then decreases and stabilizes around 0.75 x 10^5 after about 30 days. The "Infected" population (magenta line) also starts at 0, increases to a peak of approximately 0.8 x 10^5 around day 10, then decreases and stabilizes around 0.5 x 10^5 after about 30 days. Figure 7, represents the increase in Exposed and Infected for mosquitos. The Exposed group is calculated by multiplying the Susceptible population by the infection rate (λv) over a given period of time, subtracting the per capita rate of progression from Exposed::>

<a id='f05fae32-6ed9-4d96-b15e-704a622471dd'></a>

Authorized licensed use limited to: UNIVERSITA TRENTO. Downloaded on December 22,2025 at 13:32:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE BREAK -->

<a id='9675462a-c4bd-44f9-966f-ee919b9304af'></a>

<::transcription of the content
: IEEE logo::>

<a id='058efa2a-5a57-4855-a203-bcd0a1cf084e'></a>

Proceedings of the IEEE SoutheastCon 2015, April 9 - 12, 2015 - Fort Lauderdale, Florida

<a id='05ff15cf-a6a1-41bd-a383-104b1bd4b0fc'></a>

to *Infected*, and subtracting the expected death rate ($f_v(N_v)$) of the total population.

<a id='481f892c-e894-4ba4-9273-2da18ca26a8e'></a>

The *Infected* population is calculated by subtracting the death rate
($f_v$) of from those included in the per capita progression rate ($v_v$) of
the *Exposed* stage.

<a id='2cde7c19-4cb1-4916-928e-e13ff3f69a0f'></a>

C. Model 3: The SEIR model of humans
In this model, we use various parameter suggested in [16] for the SEIR Model. These are listed in Table VII.

<a id='c337c8cb-f815-498d-9145-b886c6c86a2a'></a>

TABLE VII. PARAMETERS OF SEIR MODEL
<table id="4-1">
<tr><td id="4-2">Symbol</td><td id="4-3">Parameter Description</td><td id="4-4">Values</td></tr>
<tr><td id="4-5">λh</td><td id="4-6">Immigration rate</td><td id="4-7">See Model 1</td></tr>
<tr><td id="4-8">λh</td><td id="4-9">P/capita infection rate</td><td id="4-a">3.285 x 10⁻²</td></tr>
<tr><td id="4-b">ψh</td><td id="4-c">p/capita birth rate</td><td id="4-d">7.666 x 10⁻⁵</td></tr>
<tr><td id="4-e">σh</td><td id="4-f">Max no. of mosquito bites p/unit of time</td><td id="4-g">18</td></tr>
<tr><td id="4-h">b_{hv}</td><td id="4-i">Probability of transmission from M to H</td><td id="4-j">2.000 x 10^{-2}</td></tr>
<tr><td id="4-k">b_{vh}</td><td id="4-l">Probability of transmission from H to M</td><td id="4-m">0.8333</td></tr>
<tr><td id="4-n">\nu_h</td><td id="4-o">p/capita rate of progression from Exp to Inf</td><td id="4-p">8.333 x 10^{-2}</td></tr>
<tr><td id="4-q">\gamma_h</td><td id="4-r">p/capita recovery rate</td><td id="4-s">3.704 x 10^{-3}</td></tr>
<tr><td id="4-t">\delta_h</td><td id="4-u">p/capita disease-induced death rate</td><td id="4-v">3.454 x 10^{-4}</td></tr>
<tr><td id="4-w">ρh</td><td id="4-x">p/capita rate of loss of immunity</td><td id="4-y">1.460 x 10⁻²</td></tr>
<tr><td id="4-z">μ1h</td><td id="4-A">density independent part of death/emigration rate</td><td id="4-B">1.6 x 10⁻⁵</td></tr>
<tr><td id="4-C">μ2h</td><td id="4-D">density dep. part of death/emigration rate</td><td id="4-E">3.0 x 10⁻⁷</td></tr>
<tr><td id="4-F">bh</td><td id="4-G">per capita birth rate of human</td><td id="4-H">See Model 1</td></tr>
</table>

<a id='71910ea0-c71c-4d38-8145-530f8c1d686f'></a>

Fig. 8. Susceptible Stage <::A line graph titled "Humans Population-Susceptible" with "Time (days)" on the x-axis (ranging from 0 to 1000) and "Human Population" on the y-axis (ranging from 440 to 560). The graph shows two lines: a solid blue line labeled "Susceptible" which starts around 500 and steadily decreases over time to approximately 430-440 at 1000 days, and a dotted orange line labeled "Total Population" which remains constant at 560. : chart::> Figure 8, represents the Susceptible stage of humans, which shows that, over time, the Suseptibles decrease. The calculation for those Susceptible is the addition of immigration rate (Λh) to the total population multiplied by the per capita birth rate (ψh Nh) subtracted by the per capita rate of infection (λh) of the Susceptible group and the death rate (fh) of the Susceptible population. 

<a id='a6767d22-fdd5-480d-9037-e1d2d202cb0e'></a>

Fig. 9. Exposed, Infected, and Recovered Stages<::chart: A line graph titled "Humans Exposed-Infected-Recovered" displays Human Population on the y-axis (ranging from 0 to 60) against Time (days) on the x-axis (ranging from 0 to 1000). The graph shows three distinct lines representing different stages: Exposed, Infected, and Recovered. The legend indicates: - Exposed: Red line - Infected: Cyan line - Recovered: Magenta line The "Exposed" population (red line) starts at a high value (around 50) and rapidly decreases, approaching zero after about 100 days. The "Infected" population (cyan line) starts near zero, rises sharply to a peak of approximately 57 around 50 days, and then gradually declines to about 40 by 1000 days. The "Recovered" population (magenta line) starts at zero, gradually increases, and then stabilizes around 12-13 from about 200 days onwards. Figure 9, represents the Exposed, Infected and Recovered stages. From the figure Exposed decreases, Infected Increases and Recovered increases at a smaller rate. The Exposed population is the product of the per capita infection rate (λh) of the Susceptibles over a given period of time subtracted by the per capita rate of progression (νν) of the Exposed population and the death rate (fh).::>

<a id='ee0d3d59-aae9-4856-ae71-ea62bc51d5bc'></a>

The *Infected* population was determined by the subtraction of the per capita recovery rate ($\gamma$), death rate ($f_h$), and per capita disease-induced death rate ($\delta_h$) from those in the per capita rate of progression

<a id='6c434852-87dd-486b-a5ca-926c46197ec2'></a>

($\nu_v$) the from *Exposed* population. The final piece of Figure 9, the *Recovered* population is calculated by subtracting the per capita rate of loss of immunity ($\rho_h$) and the death rate ($f_h$) from the per capita recovery rate ($\gamma_h$) of the *Infected* stage. Figure 10, represents the combine SEIR as a whole$^1$.

<a id='4f4b7281-7a46-4645-9cfd-f96630817a36'></a>

Fig. 10. SEIR Model Output
<::chart: A line chart titled "Humans Susceptible-Exposed-Infectious-Recovered" shows the change in human population over time for different states in an SEIR model. The y-axis is labeled "Human Population" and ranges from 0 to 500. The x-axis is labeled "Time(days)" and ranges from 0 to 1000.
The chart contains four lines representing different populations:
- Susceptible (blue line): Starts at approximately 500 and gradually decreases to around 420.
- Exposed (orange line): Starts near 0, rises to a peak of about 50-60 around 50-100 days, and then decreases back towards 0.
- Infected (yellow line): Starts near 0, rises to a peak of about 60 around 100-200 days, and then stabilizes at approximately 40.
- Recovered (purple line): Starts near 0 and gradually increases to about 30-40 by 1000 days.::>

<a id='59299835-1197-4fb6-b296-17fc4b294569'></a>

## V. FUTURE WORK
Future work will include modeling the effects of immunizations on the evolution of the disease. The disease evolves in response to medicine; therefore, immunizations become ineffective over time and new immunizations will need to be developed continually to combat new strains of the disease. Currently, there is no complete cure for malaria in vaccination form - largely due to the numerous factors that aid the spread of the disease [19].

<a id='a7969cb3-5f81-4e5f-81cf-103e997e5adf'></a>

VI. CONCLUSION

In conclusion, malaria's spread and growth rate can be based on the current mosquito population, human response to mosquito bite and also how mosquito's birth progression. The SEIR model representing human and SEI model representing mosquito are implemented and, given current statistics, the human and mosquito population stages of malaria are modeled effectively. Forming a connection between the ELP Model and the SEI Model, adds an additional layer to the outputs. The ELP model is used to approximate the total mosquito population and, from there, the SEI model can be based on that population. Bringing all of these parameters and models together, it is possible to show how humans are effected currently, as well as, future approximations given different inputs.

<a id='fc552816-4b74-4e2b-b380-655ee39e0324'></a>

## VII. AUTHORS CONTRIBUTION
AT and PT developed the manuscript; CJ and SG implemented the models; PT lead the brainstorming sessions and provided the idea of comprehensive model of malaria. VM supervised all aspects of the project and provided insight into modeling of diseases using PDEs.

<a id='0d45764c-a37a-4d2a-8677-59460ee831cd'></a>

## REFERENCES

1. S. Mandal, R. R. Sarkar, and S. Sinha, "Mathematical models of malaria-a review," Malar J, vol. 10, no. 1, p. 202, 2011.
2. World Health Organization, World Malaria Report 2014.
3. J. C. Koella, "On the use of mathematical models of malaria transmission," Acta tropica, vol. 49, no. 1, pp. 1-25, 1991.
4. C. Macauley, "Aggressive active case detection: a malaria control strategy based on the brazilian model," Social science & medicine, vol. 60, no. 3, pp. 563-573, 2005.
5. K. O. Okosun, R. Ouifki, and N. Marcus, "Optimal control analysis of a malaria disease transmission model that includes treatment and vaccination with waning immunity," BioSystems, vol. 106, no. 2, pp. 136-145, 2011.

¹The interested readers can contact the corresponding author for MATLAB code.

<a id='3fea1c06-d635-4547-bead-7c40199d8225'></a>

Authorized licensed use limited to: UNIVERSITA TRENTO. Downloaded on December 22,2025 at 13:32:50 UTC from IEEE Xplore. Restrictions apply.

<!-- PAGE BREAK -->

<a id='5cce72a9-70c2-4aca-a041-b286fc538aeb'></a>

<::logo: IEEE
IEEE
This logo features a stylized diamond shape with a smaller diamond inside, followed by the text "IEEE" in a bold, sans-serif font.::>

<a id='cee0c50f-829f-4f9e-996b-397a10cad825'></a>

Proceedings of the IEEE SoutheastCon 2015, April 9 - 12, 2015 - Fort Lauderdale, Florida

<a id='6907b7b0-c627-474b-882c-c12c9808677f'></a>

[6] R. Liu and S. A. Gourley, "Resistance to larvicides in mosquito populations and how it could benefit malaria control," European Journal of Applied Mathematics, vol. 24, no. 03, pp. 415-436, 2013.
[7] T. Smith and A. Schapira, "Reproduction numbers in malaria and their implications," Trends in parasitology, vol. 28, no. 1, pp. 3-8, 2012.
[8] H. J. Wearing, P. Rohani, and M. J. Keeling, "Appropriate models for the management of infectious diseases," PLoS medicine, vol. 2, no. 7, p. e174, 2005.
[9] N. Chitnis, J. M. Hyman, and J. M. Cushing, "Determining important parameters in the spread of malaria through the sensitivity analysis of a mathematical model," Bulletin of mathematical biology, vol. 70, no. 5, pp. 1272-1296, 2008.
[10] H.-F. Huo and G.-M. Qiu, "Stability of a mathematical model of malaria transmission with relapse," in Abstract and Applied Analysis, vol. 2014. Hindawi Publishing Corporation, 2014.
[11] malERA Consultative Group on Vaccines et al., "A research agenda for malaria eradication: vaccines," PLoS medicine, vol. 8, no. 1, p. e1000398, 2011.
[12] J. Li, "Modelling of transgenic mosquitoes and impact on malaria transmission," Journal of Biological Dynamics, vol. 5, no. 5, pp. 474-494, 2011.
[13] S. Ai, J. Li, and J. Lu, "Mosquito-stage-structured malaria models and their global dynamics," SIAM Journal on Applied Mathematics, vol. 72, no. 4, pp. 1213-1237, 2012.
[14] X. Wang, L. Wei, and J. Zhang, "Dynamical analysis and perturbation solution of an seir epidemic model," Applied Mathematics and Computation, vol. 232, pp. 479-486, 2014.
[15] V. Dabbaghian, V. K. Mago, T. Wu, C. Fritz, and A. Alimadad, "Social interactions of eating behaviour among high school students: a cellular automata approach," BMC medical research methodology, vol. 12, no. 1, p. 155, 2012.
[16] P. Johansson and J. Leander, "Mathematical modeling of malaria," Ph.D. dissertation, Chalmers University of Technology, 2010.
[17] M. P. Griffin, "Modeling the effects of malaria preventative measures," Ph.D. dissertation, Wofford College, 2012.
[18] R. A. Erickson, S. M. Presley, L. J. Allen, K. R. Long, and S. B. Cox, "A stage-structured Aedes albopictus population model," Ecological Modelling, vol. 221, no. 9, pp. 1273-1282, 2010.
[19] T. Smith, G. F. Killeen, N. Maire, A. Ross, L. Molineaux, F. Tediosi, G. Hutton, J. Utzinger, K. Dietz, and M. Tanner, "Mathematical modeling of the impact of malaria vaccines on the clinical epidemiology and natural history of plasmodium falciparum malaria: Overview," The Am an journal of tropical medicine and hygiene, vol. 75, no. 2 suppl, pp. 1-10, 2006.

<a id='ba35c995-c577-4cff-b658-a21b8041fa73'></a>

Authorized licensed use limited to: UNIVERSITA TRENTO. Downloaded on December 22,2025 at 13:32:50 UTC from IEEE Xplore. Restrictions apply.
<a id='a3993378-7695-4476-897e-df4672361586'></a>

Journal of Biological Systems, Vol. 16, No. 1 (2008) 51–80
© World Scientific Publishing Company

<a id='6d0beb97-0754-46f6-99cc-5be5400a5765'></a>

<::logo: World Scientific
World Scientific
www.worldscientific.com
It features a stylized "WS" monogram in black next to the company name and website in black text.::>

<a id='aa2636ed-03aa-4a3e-a939-27092317b35e'></a>

OPTIMAL CONTROL OF MIXED IMMUNOTHERAPY
AND CHEMOTHERAPY OF TUMORS

<a id='7f3acfd4-9ba4-45f2-8087-5faee8af1d30'></a>

L. G. DE PILLIS, *,§ K. R. FISTER,‡ W. GU,* TIFFANY HEAD,*
KENNY MAPLES,* TODD NEAL,‡ ANAND MURUGAN†
and KENJI KOZAI*

*Department of Mathematics, Harvey Mudd College
Claremont, CA 91711, USA

†Department of Mathematics, Pomona College
Claremont, CA 91711, USA

‡Department of Mathematics, Murray State University
Murray, KY 42071, USA

§depillis@hmc.edu

Received 28 January 2007
Revised 16 November 2007

<a id='c2c7997c-6d44-470d-a5e0-504aa95c2ad5'></a>

We investigate a mathematical population model of tumor-immune interactions. The populations involved are tumor cells, specific and non-specific immune cells, and concentrations of therapeutic treatments. We establish the existence of an optimal control for this model and provide necessary conditions for the optimal control triple for simultaneous application of chemotherapy, tumor infiltrating lymphocyte (TIL) therapy, and interleukin-2 (IL-2) treatment. We discuss numerical results for the combination of the chemo-immunotherapy regimens. We find that the qualitative nature of our results indicates that chemotherapy is the dominant intervention with TIL interacting in a complementary fashion with the chemotherapy. However, within the optimal control context, the interleukin-2 treatment does not become activated for the estimated parameter ranges.

<a id='96d43f46-91d3-440d-8498-3c36a8bdc39c'></a>

Keywords: Mixed-Immuno-Chemotherapy; Immunotherapy; Chemotherapy; Quadratic Optimal Control.

<a id='43e91004-ffbf-49ef-84da-704a9a039805'></a>

# 1. Introduction and Background
Recent developments in tumor immunology and immunotherapy have led to the question of how most effectively to combine cancer immunotherapy and chemother- apy. Immunotherapy used in combination with chemotherapy can be important in at least two ways: protecting the patient from opportunistic infection, as well as com- bating the cancer itself. Chemotherapy depletes a patient's immune system, making the patient prone to dangerous infections. For this reason alone, it is desirable to strengthen the immune system after an immune-depleting course of chemotherapy. Additionally, however, the ability to enlist the body's own defenses to fight the cancer can be a powerful treatment strategy. Maintaining a strong immune system, even during chemotherapy, may be essential to successfully fighting the cancer. The

<a id='d8e0def8-69c6-41d1-b2eb-b72fc1fce449'></a>

51

<a id='a950d9ed-bd64-4dd8-970b-b190ed4edb2b'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='00af5518-ee58-4c75-bc08-a7673f9760fa'></a>

52 de Pillis et al.

<a id='b8c78e96-aff7-4872-983d-309e522ad6e2'></a>

development of cancer vaccines, a special type of immunotherapy to treat certain forms of cancer, is a relatively recent focus in cancer research. 1-6 For more literature on the subject, please see the citations included in de Pillis et al. 7,8 Most vaccine therapy clinical trials are still in early phase studies. In some preliminary studies, vaccine therapy has been found to be most effective when administered together with chemotherapy, cf. http://www.cancerresearch.org9 and Yu et al. 10 However, it is still unknown whether concurrent administration of chemo-immunotherapy is superior to sequential administration, or whether there are as yet untried combina- tion therapy protocols that could render even greater benefit to the patient.

<a id='3b530062-37ae-4846-93b9-c632808a690e'></a>

The goal of this paper is to model mathematically, analyze and explore compu-
tationally potentially optimal ways to combine chemotherapy and immunotherapy
treatment strategies that can minimize a tumor while maximizing the strength
of the immune system, with minimal toxicity to the patient. The mathematical
model, as a reflection of the biology, has been built in order to allow us to explore
the behavior, interaction and potential synergy of three types of treatment, all
of which have been used in clinical trials with patients: cytotoxic chemotherapy,
tumor infiltrating lymphocyte (TIL) therapy, and interleukin-2 (IL-2) therapy. It
is known211,212 that IL-2 is both produced by T-cells and stimulates T-cell activity.
The use of IL-2 in combination with cytotoxic chemotherapy to treat certain forms
of cancer in humans has met with some success in certain cases (see e.g. Rosenberg
et al.21,213). In these studies, it was demonstrated that IL-2 in cancer patients as an
immunological manipulation was capable of mediating the regression of established
growing cancers in humans. The use of TIL has also been explored (see e.g. Osada
et al.214 and Dudley et al.215) with some success. Because of the promise shown by
these two types of immunotherapies, we include them in the current model, along
with chemotherapy. We note that the model of de Pillis et al.27 includes IL-2 and
TIL, but with no endogenous IL-2 production and with no optimal control. In the
current model, we incorporate the naturally occurring cytokine IL-2, allowing for
endogenous production as well as exogenous application. We also allow for TIL
injections.

<a id='a0211ff1-6439-4fc8-8b68-a0df7f0394c4'></a>

The model we have developed tracks four cell populations (tumor cells, specific effector immune cells such as CD8+T cells, innate effectors such as NK cells, and circulating lymphocytes) and three potential treatments (chemotherapy, TIL therapy and IL-2 therapy). Like the model presented in this paper, the model of de Pillis et al.7 is a population model tracking four types of cells and three types of treatment. However, the focus of the work of de Pillis et al.7 is mainly on the study of the dynamics of the model. Additionally, the current model employs somewhat different dynamics, and contains mathematical updates in response to the results presented in de Pillis et al.7 Further details on current model development can be found in Sec. 2. The model of de Pillis et al.8 is a three-cell model (tumor cells, effector immune cells, and circulating lymphocytes) with one-treatment (cytotoxic chemotherapy). In de Pillis et al.8 we successfully employed the method of optimal control and numerical techniques to reveal pathways to new chemotherapy protocols. In the current paper, we focus on the examination of the application of optimal

<a id='4f86ebe8-c6f9-47f9-a7b5-4b7f0831354a'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com
by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='c0af9b3d-4136-4fa1-aace-89f769b90302'></a>

Optimal Control of Mixed Immunotherapy

<a id='a8f61449-bbeb-403a-b270-6a172bb9d989'></a>

53

<a id='855fee7c-6aa1-4a43-9846-7a96282b725e'></a>

control to a three-treatment environment in the context of our extended four-cell
model.

<a id='55d50505-7bf1-4254-9e1c-49b68df85e50'></a>

For combination therapy, there exist many mathematical constructs that could be employed to investigate beneficial drug treatment strategies. For this manuscript, optimal control theory is used to explore the connections among the different cell mechanisms and chemo-immunotherapies. Burden et al. 16 investigate optimal treatment to minimize the tumor burden and the amount of immunotherapy given. The results proved that the immunotherapy treatment with IL-2 could improve the situation for the patient, but the IL-2 treatments alone were not enough to disrupt the cyclic re-occurrence of the tumor. Recent work by Castiglione and Piccoli³ investigates optimal control methods applied to dendritic cell transplantation. Their work shows that the tumor can be reduced within a six-month window of therapy. Yet they find a definite dependence on the last vaccine injection given in the treatment schedule. As stated, in this work we pursue combination strategies within the mathematical context of optimal control to further study the intricate trade-offs among three therapies (TIL, IL-2, and chemotherapies) and between the different tumor and immune cell populations to increase the probability of reducing the tumor while limiting the toxicities of each treatment. We use quadratic control on the coupled system of ordinary differential equations presented in Sec. 2. It is known that quadratic controls are generally more theoretically tractable. The existence of the optimal control with a quadratic objective functional is proved using results from Fleming and Rishel.17 We use Pontryagin's Minimum Principle 18 to provide first order necessary conditions for a control to be optimal.

<a id='93c946ba-309e-467f-915a-eed133094961'></a>

The outline of this paper is as follows. After this introduction, we develop the model in Sec. 2 and discuss parameter choices in Sec. 3. We next explore the dynam- ics of the model in Sec. 4. In the dynamics section, we identify example equilibrium points by first analytically reducing the problem of solving six equations with six variables to a problem of solving one equation with one variable. We find for a particular parameter set the existence of both a small and a large tumor equilib- rium, with the small equilibrium unstable, the large stable. In Sec. 5, we provide necessary conditions for an optimal control related to drug therapy, and in Sec. 6, we discuss numerical results of the optimal strategies. For the numerics, we employ the optimal control software Miser319 running in Matlab and analyze the perfor- mance of the objective functional by numerical simulations. To conclude, in Sec. 7, we interpret the biological implications of our results.

<a id='86c1c2cf-9c67-4a6f-ab92-fd7c17e6423c'></a>

## 2. Four-Cell Two-Chemical Model
### 2.1. Model development
Our goal in the creation of a mathematical model is to allow for sufficient complexity so that the model will qualitatively generate clinically observed *in vivo* tumor growth patterns, while it simultaneously maintains sufficient simplicity to admit analysis. The model we present is a system of ordinary differential equations whose

<a id='721d7aad-dfff-4c9f-a660-d17c8ded1532'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='f61f37c7-5b50-4cda-9a56-9b87e52ec7aa'></a>

54 de Pillis et al.

<a id='771a9cc6-e1bc-4367-b7ce-3d73956565be'></a>

state variables are populations of tumor cells, specific and non-specific immune cells, and concentrations of therapeutic interventions.

<a id='cdaf9a43-aa71-493e-bee5-94cb9e66744f'></a>

The model we propose herein shares features with both the model presented in de Pillis et al.<sup>8</sup> and the model given in de Pillis et al.<sup>7</sup> The model of de Pillis et al.<sup>8</sup> tracks a tumor cell population, a general effector cell population, a population of circulating lymphocytes, and a cytotoxic chemotherapy drug concentration. With this three-cell one-drug model, the authors are able to explore a comparison between quadratic and linear optimal controls applied to a single type of therapy. The model of de Pillis et al.<sup>7</sup> incorporates two important refinements: the authors distinguish between and track the populations and actions of specific (such as CD8+T) and non-specific (such as NK) effector cells, and allow for the incorporation of additional immunotherapies in the form of interleukin-2 (IL-2) and tumor-infiltrating lymphocyte (TIL) injections. The addition of the two types of immunotherapy is intended to allow the authors to explore the potential of combined chemo-immunotherapy treatment regimens. The current model tracks the same four-cell populations as the model of de Pillis et al.<sup>7</sup>, but there are some differences in how we have chosen to model the dynamics of the cell populations, the specifics of which are discussed below. Additionally, unlike the model of de Pillis et al.<sup>7</sup>, we allow for endogenous IL-2 production. We incorporate the biological perspective that not only is IL-2 produced by T-cells, but also that IL-2 in turn stimulates T-cell activity, cf. Abbas et al.<sup>11</sup> and Janeway et al.<sup>12</sup> As in de Pillis et al.<sup>7</sup>, we also explore the potential of combined therapies, but unlike de Pillis et al.<sup>7</sup>, we systematize this exploration through the application of optimal control.

<a id='2a221b85-e382-4722-9c92-8940c03c732e'></a>

Since we wish to explore the development of combination therapy treatment protocols, we include the following mathematical model components that represent tumor response to medical interventions.

1. System response to chemotherapy (direct cytotoxic effects on tumor and immune cell populations).
2. System response to immunotherapy in the form of the naturally occurring cytokine IL-2.
3. System response to immunotherapy in the form of tumor infiltrating lympho-cyte (TIL) injections.

<a id='47725114-b2f8-4a10-b990-64d44e99db22'></a>

The assumptions that were used to determine the model equations are outlined below, followed by a discussion of the model equations themselves.

<a id='5f69c00c-d2f1-4db2-b394-ecd0559c7a4f'></a>

## 2.2. Model assumptions
We should note that there is no universal agreement as to the underlying dynamics or precise cascade of events that takes place in the immune response process. Our assumptions, therefore, are based on published statements and conjectures as well as what we consider to be reasonable suppositions.

<a id='abcd01b5-2d12-4fc0-abad-687378858d98'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='28887ac0-8805-4605-b0b2-887cea62daa8'></a>

Optimal Control of Mixed Immunotherapy

<a id='6bab8d65-e012-4216-b0e2-76a7272aa09f'></a>

55

<a id='f90488a2-207c-4b0d-8035-f8824c0344d1'></a>

• A tumor grows logistically in the absence of an immune response. This is one accepted growth model for tumors, 20 and is also based on fittings of the data in Diefenbach et al.21
• Both NK (natural killer, non-specific effectors) and CD8+T (cytotoxic T-lymphocytes, specific effectors) cells are capable of killing tumor cells. (See e.g. Diefenbach et al., 21 Kawarda et al., 22 and Germain.23)
• Both NK and CD8+T cells respond to tumor cells by expanding and increasing cytolytic activity. (See e.g. Osada et al.14 and Kieper et al.24)
• NK cells are normally present in the body, even when no tumor cells are present, since they are part of the innate immune response. (See e.g. Roitt et al.25)
• As part of the specific immune response, active tumor-specific CD8+T cells are only present in large numbers when tumor cells are present. (See e.g. Roitt et al. 25 and Kirschner and Panetta. 26) We assume this activation and priming of effector cells takes place as a result of a fraction of the circulating lymphocyte population encountering tumor cells.
• NK and CD8+T cells become inactive after some number of encounters with tumor cells. (See e.g. Adam and Bellomo.27)

<a id='46145200-787b-4b11-963a-cb9e7b8b3696'></a>

The following additional assumptions are used in the development of therapeutic terms.

* Circulating lymphocyte levels can be used as a measure of patient health (see e.g. Mustafa et al.,  Melichar et al.,  and Glas et al. ). Encounters between circulating lymphocytes and tumor cells boost the effector cell population.
* The fraction of the tumor population killed by chemotherapy depends on the amount of drug in the system. The fraction killed has a maximum less than one, since only tumor cells in certain stages of development can be killed by chemotherapy.
* A fraction of NK cells, CD8+T cells, and circulating lymphocytes are also killed by chemotherapy, according to a similar fractional kill curve.
* T-cells are components of the process of stimulation and elimination of activated effector cells, a model simplification meant to reflect the self-regulatory nature of the immune system (see e.g. Dudley et al., Germain, and Jiang and Chess).

<a id='a5f8f3cc-e4ec-420e-a5de-9a909172ece1'></a>

## 2.3. ODE model: general form of equations
The model describes the kinetics of four populations (tumor cells and three types of immune cells), as well as two drug concentrations in the bloodstream, using a series of coupled ordinary differential equations.
* T(t), tumor cell population
* L(t), tumor-specific CD8+T cell population
* N(t), non-specific effector-immune cell population
* C(t), circulating lymphocyte population

<a id='b3b8a5c0-3dd4-46da-9dbd-18474d1ceb74'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='dd960a3b-fa68-4281-9603-b9fd4f5ae507'></a>

56 de Pillis et al.

<a id='9e085e7d-3121-4338-a572-b47467642cee'></a>

<ul><li>I(t), IL-2 concentration (IU per liter)</li><li>M(t), chemotherapy drug concentration (mg per liter).</li></ul>

<a id='17aad7ed-f597-4106-ae77-2d47542c43c1'></a>

The equations governing the population kinetics must take into account a net growth term for each population, the fractional cell kill, per cell recruitment, cell inactivation and external intervention with medication. We attempt to use the simplest expressions for each term that still qualitatively reflect experimental data and recognize population interactions.

<a id='1298e028-f16a-43a5-9789-59c9e2491220'></a>

In our model, we consider the population levels of NK and CD8+T cells actually to represent immune cell "effectiveness" in the sense that an increase in the total population count in the mathematical model may be evidenced biologically either as a greater number of total cells, or as each individual immune cell becoming more efficient at killing the target tumor cells.

<a id='1c32b34c-6303-4330-9adb-196b52728027'></a>

Our system of equations describing the growth, death, and interactions of these populations with treatments is:

<a id='66990cb9-1838-4dd6-90a7-0d0ba57f3277'></a>

$\frac{dT}{dt} = aT(1 - bT) - c_1NT - DT - K_T MT$ (1)

$\frac{dL}{dt} = -mL - qLT - uL^2 + r_2CT + \frac{p_I LI}{g_I + I} + V_L(t) - K_L ML$ (2)

$\frac{dN}{dt} = \alpha_1 - fN + g \frac{T^\eta}{h + T^\eta}N - pNT - K_N MN$ (3)

$\frac{dC}{dt} = \alpha_2 - \beta C - K_C MC$ (4)

$\frac{dI}{dt} = \frac{p_T T}{g_T + T}L + wLI - \mu_1 I + V_I(t)$ (5)

$\frac{dM}{dt} = -\gamma M + V_M(t)$ (6)

<a id='4af96cf9-4a86-4d29-9adc-9a23281ba48c'></a>

where $D = d\frac{(L/T)^l}{s+(L/T)^l}$. These equations have the general initial conditions $T(0) = T_0$, $L(0) = L_0$, $N(0) = N_0$, $C(0) = C_0$, $I(0) = I_0$ and $M(0) = M_0$, where each initial value is positive.

<a id='69f9cb24-7005-42c9-834a-9a90f8b8e24d'></a>

The functional forms that we choose for each cell-interaction term are discussed below. We have chosen to represent parameters by lower case letters, always assumed to be positive, and state variables or functions of state variables by upper case letters.

<a id='f1dbcde1-4eb6-4470-af82-4235ff357559'></a>

2.3.1. _dT/dt: Tumor cells_
We adapt the growth terms for tumor and CD8+T cells from de Pillis _et al._$^{34}$
In Eq. (1) tumor growth is assumed to be logistic, based on data gathered from
immunodeficient mice,$^{21}$ and is represented by _aT_ (1 - _bT_).

<a id='58886ee1-b32a-4d60-8c31-2c64c590a9a4'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='dceac832-79f0-4a9a-bee7-76ac2b9bbe27'></a>

Optimal Control of Mixed Immunotherapy

<a id='6f95fa1d-b4f7-4f84-9989-be9bb5ae1920'></a>

57

<a id='a4d73caf-9c2a-4a80-8ef6-92fc721c5c54'></a>

The fractional cell kill terms of tumor cells by tumor-specific effectors, L, and non-specific effectors, N, are of the same form as those described in de Pillis et al.34 These fractional cell kill terms represent negative interactions between two populations. They can represent competition for space and nutrients as well as regulatory action and direct cell population interaction. The interaction between tumor and NK cells is represented by a mass-action term -CNT. Tumor lysis by CD8+T cells, on the other hand, has the form:

<a id='13346db9-6690-424b-bf29-4507fad1ab86'></a>

d $\frac{(L/T)^l}{s+(L/T)^l}T$.

<a id='57f0f4f3-e904-41c6-bf20-eb0a26653002'></a>

As described in de Pillis et al., 34 the mathematical form of this term, which reflects the bounded nature of the effector cell population's ability to lyse tumor cells, was determined through fitting to published data from laboratory mice. Letting
$D(T, L) = d \frac{(L/T)^l}{s+(L/T)^l}$, we represent T-cell kill of tumor cells by the term $DT$.

<a id='b57f975f-3489-47c1-bc99-f4cb44de529e'></a>

The model includes a treatment kill term in each of the cell population equations. For simplicity, we assume mass-action kinetics in which the amount of the cell population killed by treatment is proportional to the interactions of the cells with the medicine. We recognize that it is the case that certain chemotherapeutic drugs, such as doxorubicin, are only effective during certain phases of the cell cycle, and pharmacokinetics also indicate that the effectiveness of chemotherapy is bounded. An alternate cell-kill term, then, could reasonably represent the nonlinear bounded nature of the response. However, for simplicity, we have chosen to incorporate the linear mass-action form in this version of the model. We therefore represent the effect of chemotherapy on each cell population by a term of the form $K_\phi\phi$, for $\phi = T, N, L, C$. In the case of the tumor cell population, then, the chemotherapy kill term is $-K_TMT$.

<a id='1dfeddd4-4887-44a3-9311-4afe805f80ea'></a>

### 2.3.2. dL/dt: Tumor-specific effector cells, T-cells
Cell growth for CD8+T cells consists only of natural death rates, since no CD8+T cells are assumed to be present in the absence of tumor cells. The T-cell death rate is assumed to be proportional to the population of T-cells and is represented by −mL in Eq. (2).

<a id='37348363-1d89-4d1c-b81f-e5bb7df5ecb1'></a>

Inactivation of cytolytic potential occurs when an effector cell (NK or CD8+T cell) has interacted with tumor cells several times and ceases to be effective. We use the inactivation term proposed by de Pillis et al., 34 -qLT. The parameter q in the inactivation term represents a mean inactivation rate.

<a id='d60cce7f-6dee-4983-919a-64d1654c8892'></a>

The term $-uL^2$ describes self-regulation and suppression of CD8+T cell activ-
ity, which occurs when there are very high levels of activated CD8+T cells with-
out responsiveness to cytokines present in the system (see e.g. Gett et al.$^{35}$ and
Gilbertson et al.$^{36}$). Unlike the model of de Pillis et al.,$^{7}$ we assume that self-
regulation takes place through T-lymphocyte activity, and does not involve NK
cells. This term comes into play when the amount of CD8+T cells in the body is

<a id='c755789d-38d4-4edd-888d-5846091d5878'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='6bb4a350-1147-498d-a073-a1fe2744edca'></a>

58 de Pillis et al.

<a id='8c6bfb6a-be23-481f-8db6-028ecfb019f7'></a>

high. Experimental data document that these cells can become rapidly inactivated even with a tumor present. ¹³

<a id='76a03781-f602-44ff-a408-00ada0c62ef7'></a>

The immune system is also stimulated by the presence of tumor cells to pro-duce more CD8+T cells. We assume recognition of the presence of the tumor is proportional to the average number of encounters between circulating lymphocytes and the tumor: r₂CT. We do not include the indirect stimulation of these lym-phocytes through tumor debris, as is done in the model of de Pillis et al.⁷ The evidence for the effect of tumor debris may be considered still under debate, cf. Diefenbach et al.²¹

<a id='99f9900a-d503-4c28-bce2-55f10224c236'></a>

We include CD8$^+$T activation by interleukin-2 (IL-2) immunotherapy. This
“drug” is actually a naturally occurring cytokine in the human body, and its effect
on the immune system’s efficacy is described mathematically with a Michaelis-
Menten interaction term in the equation for L. The presence of IL-2 stimulates
the production of CD8$^+$T cells, which we represent with the term $\frac{p_1LI}{g_1+I}$. This term
has the same form as the activation term developed in the Kirschner and Panetta
tumor-immune model.$^{26}$

<a id='86e06c0d-39af-469e-a43a-26b937cc1e4f'></a>

The chemotherapy kill term for this effector cell population is represented by $K_LML$. The tumor infiltration lymphocyte (TIL) drug intervention term, $V_L(t)$, for the CD8+T cell population, represents an immunotherapy in which the immune cell levels are boosted by the direct addition of antigen-specific cytolytic immune cells.

<a id='9bd81036-c8d2-4b20-90ce-398e951ee993'></a>

### 2.3.3. dN/dt: Non-specific effector cells, NK cells

As in the model of de Pillis et al., 34 we assume a constant NK cell production rate, and a population-proportional death rate, represented by a₁ – fN in Eq. (3). We note that the assumption of a constant NK production rate differs from the model of de Pillis et al., 7 in which NK production rate is linked to the populations of circulating lymphocytes. In this case, the assumption of constant NK production is also in line with the model of Kuznetsov et al., 37 in which a proposed parameter value is also provided.

<a id='4988c854-a073-4310-b9d0-dad8411a538c'></a>

The recruitment of NK cells is represented by a modified Michaelis-Menten
interaction in which the presence of tumor cells stimulates the production and
recruitment of additional non-specific effector cells. Hence the NK cell recruitment
term is

<a id='e8438729-5c52-438e-8c74-88611d91ea2e'></a>

g (T^eta / (h + T^eta))^N.
et al^7,34

<a id='d12e8056-eec4-47e0-85ff-aa33d79f3cdd'></a>

This form is also used in de Pillis et al.<sup>7,34</sup>

As was done for the tumor-specific lymphocytes, for the non-specific lymphocytes, we incorporate a term representing their inactivation after some encounters with tumor cells, and use the form proposed in de Pillis et al.,<sup>34</sup> -pNT.
The chemotherapy kill term for the non-specific cell population is represented by
-K<sub>N</sub>MN.

<a id='5fc2c816-b31b-412d-b0b2-05add6cf3632'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='9c8406e5-df5a-455a-b6b3-dbe75c0f74b6'></a>

Optimal Control of Mixed Immunotherapy

<a id='0a7cb4da-f8ed-4fa7-9316-d08460424546'></a>

59

<a id='e1ff9320-4476-42c9-9934-a6383cafadc0'></a>

2.3.4. dC/dt: Circulating lymphocytes

<a id='e3380790-bdd2-4a1f-a7d7-7b41fea87e38'></a>

For Eq. (4), we assume that circulating lymphocytes are generated at a constant rate, and that each cell has a natural lifespan. Growth and death are represented by α_2 - βC. The chemotherapy kill term for the circulating lymphocyte cell population is represented by -K_CMC.

<a id='94b5c6bb-1cdf-4221-bfde-19ed9112de57'></a>

### 2.3.5. dI/dt: IL-2

The cytokine interleukin-2 (IL-2) is known to stimulate CD8+T cell recruitment and proliferation (see e.g. Roitt et al.<sup>25</sup>). IL-2 is produced naturally by the body, and is also administered therapeutically to boost immune system function. IL-2 has been used in clinical trials on its own, in combination with chemotherapy, and in conjunction with TIL (tumor infiltrating lymphocyte) injections, in which a large number of highly activated CD8+T cells are injected into the system.<sup>13,38-40</sup> In Eq. (5), we include terms representing endogenous production of interleukin-2 (IL-2) in addition to allowing for exogenous application of IL-2 as a treatment. The first term in Eq. (5), $$\frac{p_T T}{g_T+T}L$$, is similar to that of Kirschner and Panetta<sup>26</sup> representing the understanding that the interaction of tumor-specific T-cells with tumor cells stimulates IL-2 production. The Michaelis-Menten form of the term accounts for the self-limiting nature of this production. In Abbas and Lichtman<sup>11</sup> it is noted that all types of T-cells produce IL-2. We represent this by the linear interaction term $wLI$. IL-2 concentration is assumed to decay exponentially, represented by $-\mu_I I$. Finally, direct exogenous application of IL-2 is represented by the time-dependent term $V_I(t)$.

<a id='7c4f0da5-1593-4de1-95e5-d19f459b7886'></a>

2.3.6. $dM/dt$: Chemotherapy drug
After administration of chemotherapy, we assume the drug will be eliminated from the body over time at a rate proportional to its concentration. This is represented by an exponential decay term, $-\gamma M$, in Eq. (6). Direct application of chemotherapy is included through the term $V_M(t)$.

<a id='acdd3875-8174-48f2-8036-cf48faade237'></a>

## 3. Parameter Choices

While a general model with non-specific parameters is useful in studying the qualitative dynamics of cancer growth, it can also be enlightening to run numerical simulations to observe example outcomes. Numerics require the assignment of specific parameter values. Although there is not an enormous amount of tumor-immune interaction data that are directly usable for the purposes of this model, our parameter choices are guided by the published data that are available. The paucity of relevant available data requires that we glean values from multiple data sets. In this work, we use the data made available from both the murine experimental studies of Diefenbach et al.21 and the human clinical trials of Dudley et al.15 When necessary,

<a id='5ccbc417-dfe7-42a6-bc9b-fa9dd6453aa3'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='0bbdd41b-f3ef-4ab5-919d-be39e5b74abb'></a>

60 de Pillis et al.

<a id='84dcdd3b-2138-48cb-be72-2942b1c44270'></a>

we also use parameters of earlier models that have been fitted to experimental curves. 7,34,37,41,42 In cases for which no parameter information was available, we chose parameter values that allowed for reasonable simulation outcomes.

<a id='7a87d5f7-9c65-4109-9a04-98a084063220'></a>

In this section, we present the set of example parameters that are used in Secs. 4
and 6 to generate the numerical stability analysis of this particular system, and to
produce numerical optimal control experiments.

<a id='a5b8f25c-74af-4d69-a2f1-11a5a369c41c'></a>

Chemotherapy strength was assumed to be one log-kill, as described in Perry, 43
and the values of the kill parameters K_T, K_L, K_N, K_C were chosen accord-
ingly. Certain chemotherapy drugs, such as doxorubicin, kill cells by disrupt-
ing the process of division and growth. Rapidly dividing cells, like those of the
hair, the stomach lining, and the bone marrow where immune cells are pro-
duced, are preferentially damaged by chemotherapy (see e.g. Holland et al. 44 and
http://www.nci.nih.gov/cancertopics/chemotherapy-and-you/page2). High doses of
drug can also damage other tissues in the body. 44 Ideally, chemotherapy should
more effectively kill tumor cells than immune cells. Therefore, K_L, K_N, and K_C
are assumed to be smaller than K_T, but of the same order of magnitude.

<a id='d4f3183f-5bd6-4827-8b35-8f4322e7d4d8'></a>

The drug decay rate, γ, was calculated from the drug half-life and the relation
γ = ln 2 / t_1/2 . The drug half-life, t_1/2, was estimated to be about 18 hours, based on
experimental data for the chemotherapeutic drug doxorubicin.⁴⁶

<a id='25c395c2-787c-4097-9919-42f4b18f4920'></a>

The parameters $p_I, g_I, p_T, g_T$, and $w$ have been estimated. The choice of the first four parameters was based on the analogous parameter values presented in Kirschner and Panetta, $^{26}$ but the values have been slightly altered to fit the current mathematical model, which differs from the Kirschner model. The effector cell half-life, $\frac{ln(2)}{\mu_I}$ is a biological value taken from Kirschner's model.$^{26}$ The values of $r_2$ and $u$ are estimated only. We noticed that since $L$, the tumor-specific CD8+T cell population, produces $I$, the IL-2 population, and $I$ produces $L$, there is a feedback loop that leads to a resonance effect, such that if it is not kept in check, $I$ grows uncontrollably. We therefore had to pick parameter values that would yield responses in $I$ and $L$ in the presence of tumor that could keep the IL-2 population bounded. The term $w$ represents the fractional production of IL-2 from T-cells, and has been chosen to have a fairly small value. This small numerical value of $w$ helps to avoid the initiation of the resonance effect, and IL-2 quantities stay at reasonable levels.

<a id='f3c05f36-aa0a-4f28-8c87-25f568009794'></a>

4. Numerical Equilibrium Examples

In order to understand the dynamics of the system, we need to identify the equi-
librium points and determine their stability characteristics. Unfortunately, since
the ODE system representing the model is a fairly large system of interdependent
nonlinear equations, it is not possible to solve the equilibrium points analytically
in terms of parameters. However, through analytically reducing the problem of
solving six equations with six variables to a problem of solving one equation with
one variable (the variable T representing the tumor cell population), we are able

<a id='c6f76cec-b9fe-4844-ad98-9d84439c0ecd'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='c5dda47f-3a99-4c38-bffb-1d6921a25f3e'></a>

Optimal Control of Mixed Immunotherapy

<a id='6666b0f9-3f7e-461b-8131-b3fc3a147dd9'></a>

61

<a id='e6730451-3e80-4c2c-a207-c134e84e7380'></a>

Table 1. Estimated parameter values.

<a id='f30ecece-315c-4d2d-97db-3d7db84ef2ae'></a>

<table id="10-1">
<tr><td id="10-2">Parameter</td><td id="10-3">Units</td><td id="10-4">Description</td><td id="10-5">Estimated value</td><td id="10-6">Source</td></tr>
<tr><td id="10-7">a</td><td id="10-8">day-1</td><td id="10-9">Tumor growth rate.</td><td id="10-a">2.00 x 10-3</td><td id="10-b">Estimated</td></tr>
<tr><td id="10-c">b</td><td id="10-d">cells-1</td><td id="10-e">1/b is tumor carrying capacity.</td><td id="10-f">1.02 x 10-9</td><td id="10-g">Ref. 34, estimated using tumor growth data in Ref. 21.</td></tr>
<tr><td id="10-h">c1</td><td id="10-i">(cells day)-1</td><td id="10-j">Fractional tumor cell kill by effector cells.</td><td id="10-k">3.23 x 10-7</td><td id="10-l">Ref. 34, estimated using chromium release assay data in Refs. 15 and 21.</td></tr>
<tr><td id="10-m">d</td><td id="10-n">day-1</td><td id="10-o">Saturation level of fractional tumor cell kill by CD8+T cells. Primed with ligand-transduced cells, challenged with ligand-transduced cells.</td><td id="10-p">5.00</td><td id="10-q">Ref. 34, estimated from data in Ref. 15.</td></tr>
<tr><td id="10-r">f</td><td id="10-s">day-1</td><td id="10-t">Death rate of effector cells.</td><td id="10-u">4.12 x 10-2</td><td id="10-v">Ref. 37.</td></tr>
<tr><td id="10-w">g</td><td id="10-x">day-1</td><td id="10-y">Maximum effector cell recruitment rate by tumor cells.</td><td id="10-z">2.50 x 10-2</td><td id="10-A">Ref. 34, estimated from data in Refs. 15 and 21.</td></tr>
<tr><td id="10-B">gI</td><td id="10-C">IU (liter)-1</td><td id="10-D">Steepness of CD8+T-cell recruitment curve by IL-2.</td><td id="10-E">2.00 x 107</td><td id="10-F">Ref. 26.</td></tr>
<tr><td id="10-G">gT</td><td id="10-H">cells</td><td id="10-I">Steepness of IL-2 recruitment curve from tumor-effector cell interactions.</td><td id="10-J">1.00 x 105</td><td id="10-K">Estimated.</td></tr>
<tr><td id="10-L">h</td><td id="10-M">cellsη</td><td id="10-N">Steepness coefficient of the effector cell recruitment curve.</td><td id="10-O">6.00 × 102</td><td id="10-P">Estimated.</td></tr>
<tr><td id="10-Q">K_C, K_L, K_N</td><td id="10-R">liter * (mg * day)^-1</td><td id="10-S">Fractional lymphocyte kill by chemotherapy.</td><td id="10-T">6.00 x 10^-1</td><td id="10-U">Ref. 43.</td></tr>
<tr><td id="10-V">K_T</td><td id="10-W">liter * (mg * day)^-1</td><td id="10-X">Fractional tumor cell kill by chemotherapy.</td><td id="10-Y">8.00 x 10^-1</td><td id="10-Z">Ref. 43.</td></tr>
<tr><td id="10-10">l</td><td id="10-11">none</td><td id="10-12">Exponent of fractional tumor cell kill by effector cells.</td><td id="10-13">2/3</td><td id="10-14">Estimated.</td></tr>
<tr><td id="10-15">m</td><td id="10-16">day^-1</td><td id="10-17">Death rate of CD8+T cells.</td><td id="10-18">2.00 x 10^-2</td><td id="10-19">Ref. 47.</td></tr>
<tr><td id="10-1a">p</td><td id="10-1b">(cells * day)^-1</td><td id="10-1c">Effector cell inactivation rate by tumor cells.</td><td id="10-1d">1.00 x 10^-7</td><td id="10-1e">Ref. 34, estimated from data in Ref. 21.</td></tr>
<tr><td id="10-1f">P_I</td><td id="10-1g">day^{-1}</td><td id="10-1h">Maximum CD8^{+}T-cell recruitment rate by IL-2</td><td id="10-1i">1.25 \times 10^{-1}</td><td id="10-1j">Same order of magnitude as in Ref. 26.</td></tr>
<tr><td id="10-1k">P_T</td><td id="10-1l">IU\cdot(liter\cdot cells\cdot day)^{-1}</td><td id="10-1m">Maximum IL-2 recruitment rate from tumor-effector cell interactions.</td><td id="10-1n">6.00 \times 10^{-1}</td><td id="10-1o">Estimated.</td></tr>
<tr><td id="10-1p">q</td><td id="10-1q">(cells\cdot day)^{-1}</td><td id="10-1r">CD8^{+}T cell inactivation rate by tumor cells.</td><td id="10-1s">3.42 \times 10^{-10}</td><td id="10-1t">Ref. 37.</td></tr>
</table>

<a id='8c1cdbf6-afea-4e51-b32e-9a83b383ee96'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='97a96c08-af8a-4d62-b490-9fb97f99454d'></a>

62 de Pillis et al.

<a id='e7029010-cd6e-4105-9f31-0ea5d16c6205'></a>

Table 1. (_Continued_)
<table id="11-1">
<tr><td id="11-2">Parameter</td><td id="11-3">Units</td><td id="11-4">Description</td><td id="11-5">Estimated value</td><td id="11-6">Source</td></tr>
<tr><td id="11-7">r2</td><td id="11-8">(cellsday)⁻¹</td><td id="11-9">Rate at which CD8+T cells are stimulated to be produced as a result of tumor cells interacting with circulating lymphocytes.</td><td id="11-a">3.00 × 10⁻¹¹</td><td id="11-b">No data found.</td></tr>
<tr><td id="11-c">s</td><td id="11-d">none</td><td id="11-e">Steepness coefficient of the tumor-(CD8+T cell) lysis term D. Smaller s ⇒ steeper curve.</td><td id="11-f">3.00 × 10⁻¹</td><td id="11-g">Ref. 34, estimated from data in Ref. 21.</td></tr>
<tr><td id="11-h">u</td><td id="11-i">(cellsday)⁻¹</td><td id="11-j">Scaling of self-regulation of T-cells.</td><td id="11-k">3.00</td><td id="11-l">No data found.</td></tr>
<tr><td id="11-m">w</td><td id="11-n">(cellsday)⁻¹</td><td id="11-o">Fractional production of IL-2 by T-cells.</td><td id="11-p">2.00 × 10⁻⁴</td><td id="11-q">Estimated.</td></tr>
<tr><td id="11-r">α1</td><td id="11-s">(cells·day)-1</td><td id="11-t">Constant source of effector cells.</td><td id="11-u">1.30 x 104</td><td id="11-v">Ref. 37.</td></tr>
<tr><td id="11-w">α2</td><td id="11-x">(cells·day)-1</td><td id="11-y">Constant source of circulating lymphocytes.</td><td id="11-z">5.00 × 108</td><td id="11-A">Estimated.</td></tr>
<tr><td id="11-B">β</td><td id="11-C">day-1</td><td id="11-D">Death rate of circulating lymphocytes.</td><td id="11-E">1.20 x 10-2</td><td id="11-F">Refs. 48 and 49.</td></tr>
<tr><td id="11-G">γ</td><td id="11-H">day-1</td><td id="11-I">Rate of chemotherapy drug decay.</td><td id="11-J">9.00 × 10-1</td><td id="11-K">Ref. 46.</td></tr>
<tr><td id="11-L">η</td><td id="11-M">none</td><td id="11-N">Exponent of fractional NK cell recruitment.</td><td id="11-O">1.00</td><td id="11-P">Estimated.</td></tr>
<tr><td id="11-Q">μI</td><td id="11-R">day⁻¹</td><td id="11-S">Rate of IL-2 drug decay.</td><td id="11-T">1.00 × 10¹</td><td id="11-U">Ref. 26, from average half-life of IL-2 between 30 and 120 minutes according to Ref. 13</td></tr>
</table>

<a id='15c292fe-cfc3-4f0d-adf4-7a8a37b30e5a'></a>

to gain insight into certain dynamic features such as the possible number of equi-
librium points in the system. All the analysis we perform is independent of the
specific choices of parameter values. The final equation in T involves potentially
non-integer powers of T (see Appendix A). Analytical rootfinding techniques do
not apply. However, numerical rootfinding can be employed. In order to search for
numerical solutions, the parameter values presented in Sec. 3 are used, and we are
able to find example numerical values for T. We note that even though we obtained
T values in this final step by using specific parameter values, the solutions depend
continuously on the parameter values. Thus, our numerical results are reasonable
representatives of our model. Moreover, small perturbations of parameters will give
small perturbations of the matrix entries used in finding eigenvalues for determining
the stability of each equilibrium point. Standard matrix theory tells us the eigenval-
ues continuously depend on the entries of the matrix. Thus, the stability results in

<a id='0bd375dc-8f12-4d05-8dc0-c63ffecf5fa0'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='e3a4b0e3-3e91-4856-bf58-83e9256e9871'></a>

Optimal Control of Mixed Immunotherapy

<a id='ae4a59cc-af8f-4849-b4ff-1517addf3b24'></a>

63

<a id='76670913-a9ed-4a5a-8591-8dc58a2d20fa'></a>

our numerical example case are biologically reasonable, and represent a qualitative outcome that is possible for a range of parameter values. We find three equilibrium points in our example case: zero, small tumor, and larger tumor points. We find that both the zero and the small tumor equilibrium points are locally semi-stable while the large tumor equilibrium point is locally stable, using the parameters presented in the previous section. Thus, in our example case, certain untreated tumor populations have the potential to grow until the large tumor equilibrium is achieved. Treatment interventions would be needed to shrink this tumor. The details of our analysis and results are found in Appendix A.

<a id='da4394a6-3af1-4595-acb9-5ea789ce2757'></a>

5. Optimal Control
In this section, we find the necessary conditions for an optimal control to minimize tumor size over time, while also minimizing the quantities of drugs administered. We minimize drug doses because we assume that toxic side-effects are a concern, and that the smaller the dose, the better. We minimize an objective functional of a form that reflects the trade-off we require in minimizing both tumor-size and drug-doses:

<a id='9f0081f5-4157-4d51-b2d6-a1a616dbe003'></a>

$$J(V_L, V_I, V_M) = \int_0^{t_f} \left( T(t) + \frac{\epsilon_L}{2} V_L^2(t) + \frac{\epsilon_I}{2} V_I^2(t) + \frac{\epsilon_M}{2} V_M^2(t) \right) dt. \quad (7)$$

<a id='e9361acf-9dc6-446d-a69c-8395835870d6'></a>

J, which involves a "quadratic control" because it is quadratic in the treatment terms, must be minimized subject to Eqs. (1)-(6). An important question we must address is whether, in light of the intrinsic tumor-to-therapy trade-off, an optimal control even exists. In this case, we are able to show that one does indeed exist. The proof of the existence of an optimal control is presented in Appendix B. The proof requires that we perform an analysis of the super-solutions (upper bounds on solutions) of the system (1)-(6), which is also found in Appendix B.

<a id='5f6ec4fd-4ce9-4d7d-ade4-3866d8e67306'></a>

Once we have shown we have a bounded system, we are able to establish the existence of an optimal control triple using a result from Fleming and Rishel¹⁷ (Corollary 4.1, p. 68). For convenience, we let $\vec{V}(t) = (V_L(t), V_I(t), V_M(t))$. For the statement of the existence theorem and its proof, please once again see Appendix B.

<a id='84c15364-748c-4b8b-aa8a-118ced704bb6'></a>

## 5.1. Necessary conditions for optimality

With the existence of the quadratic optimal control established, we now ask what form that control might take. In other words, we use Pontryagin's Maximum Principle<sup>18</sup> to find necessary conditions for our optimal control. We need the definition of the Lagrangian for the theorem that follows below. For this particular case, the Lagrangian is

<a id='5f0dfe75-bcf9-4939-af02-1976ef61fa92'></a>

L = H + W_1(t)V_L(t) - W_2(t)(1 - V_L(t)) - W_3(t)V_M(t) - W_4(t)(1 - V_M(t))
- W_5(t)V_I(t) - W_6(t)(1 - V_I(t))

<a id='35867754-0407-4c65-af44-dad2e02cd54c'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='d6458007-d54d-4303-a683-9ba63b75cda2'></a>

64 de Pillis et al.

<a id='45662a73-c579-43ea-99ad-f858929c3011'></a>

where H is the Hamiltonian given by

<a id='6bc77c82-301e-402c-a634-fef99a38296d'></a>

$$H = T + \frac{\epsilon_L}{2}V_L(t)^2 + \frac{\epsilon_I}{2}V_I(t)^2 + \frac{\epsilon_M}{2}V_M(t)^2$$
$$+ \lambda_1(aT(1-bT) - c_1NT - DT - K_TMT)$$
$$+ \lambda_2\left(\alpha_1 - fN + \frac{gT^\eta N}{h+T^\eta} - pNT - K_NMN\right)$$
$$+ \lambda_3\left(-mL - qLT - uL^2 + r_2CT + \frac{p_IIL}{g_I+I} - K_LML + V_L(t)\right)$$
$$+ \lambda_4\left(\frac{p_TTL}{g_T+T} + wLI - \mu_II + V_I(t)\right) + \lambda_5(\alpha_2 - \beta C - K_CMC)$$
$$+ \lambda_6(-\gamma M + V_M(t))$$

<a id='b65022df-94bd-49f3-9e47-c69b3fd837b0'></a>

and $W_i(t) \ge 0$ are penalty multipliers such that

<a id='47e271d6-6771-4c2e-9733-8f29d7b274d7'></a>

W_1(t)V_L(t) = 0
W_2(t)(1 - V_L(t)) = 0
at V_L^*(t)

W_3(t)V_M(t) = 0
W_4(t)(1 - V_M(t)) = 0
at V_M^*(t)

W_5(t)V_I(t) = 0
W_6(t)(1 - V_I(t)) = 0
at V_I^*(t).

<a id='22263e82-bfe7-4129-bec5-d801f5976d8a'></a>

**Theorem 5.1.** Given an optimal control triple, $\tilde{V}$ = ($V_L^*(t)$, $V_I^*(t)$, $V_M^*(t)$), and solutions of the corresponding state system, there exist adjoint variables $\lambda_i$ for $i$ = 1,2,...,6 satisfying the following:

<a id='c78374a5-52ca-4bf4-9b5f-49e197fad013'></a>

$$\frac{d\lambda_1}{dt} = -\frac{\partial\mathcal{L}}{\partial T} = -1 - \lambda_1\left(a - 2abT - c_1N - D + \frac{sdl\left(\frac{L}{T}\right)^1}{\left[s + \left(\frac{L}{T}\right)^1\right]^2} - K_TM\right)$$

<a id='c0771cf8-7fca-451d-985f-165863030f92'></a>

$$-\lambda_2 \left(g \frac{h\eta T^{\eta-1}}{(h+T^\eta)^2} N - pN\right) - \lambda_3 (-qL + r_2 C)$$

<a id='2e5b4e4f-e660-4d8f-8f68-1636a432afb8'></a>

-λ_4 ( (p_T g_T) / (g_T + T)^2 ) L

<a id='85cae204-1ddb-4cd3-a8ff-5e41106d3abe'></a>

$$\frac{d\lambda_2}{dt} = -\frac{\partial\mathcal{L}}{\partial N} = \lambda_1 c_1 T - \lambda_2 \left(-f + g \frac{T^\eta}{h + T^\eta} - pT - K_N M\right)$$

<a id='33c98628-21df-426b-a8bc-73d58924018b'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='75cb85b9-4238-4ff4-bc28-ae7f307f03f9'></a>

Optimal Control of Mixed Immunotherapy

<a id='8a52e99d-395e-4950-bb60-5ca82b24de93'></a>

65

<a id='702a09c0-056c-455e-b2c8-635d96c3f356'></a>

$$\frac{d\lambda_3}{dt} = -\frac{\partial\mathcal{L}}{\partial L} = \lambda_1 \frac{sdl\left(\frac{L}{T}\right)^{l-1}}{\left[s+\left(\frac{L}{T}\right)\right]^2} - \lambda_3\left(-m-qT-2uL+\frac{p_I I}{g_I+I}-K_L M\right) - \lambda_4\left(\frac{p_T T}{g_T+T}+wI\right)$$

<a id='e93414ea-7d62-46b4-b855-470a30e90004'></a>

$\frac{d\lambda_4}{dt} = -\frac{\partial L}{\partial I} = -\lambda_3 \left( \frac{p_I g_I}{(g_I+I)^2} \right) L - \lambda_4(wL - \mu_I)$

$\frac{d\lambda_5}{dt} = -\frac{\partial L}{\partial C} = -\lambda_3 r_2 T - \lambda_5(-\beta - K_C M)$

$\frac{d\lambda_6}{dt} = -\frac{\partial L}{\partial M} = \lambda_1 K_T T + \lambda_2 K_N N + \lambda_3 K_L L + \lambda_5 K_C C + \gamma \lambda_6 \quad (8)$

<a id='8ab30a3f-31f3-487e-9094-70e752eb6df5'></a>

where λ_i(t_f) = 0 for i = 1, 2, ..., 6. Furthermore, V_L*(t), V_M*(t), and V_I*(t) can be represented by

<a id='6867d166-1be2-487b-9836-78e9239e432f'></a>

$$V_L^* = \min\left(1, \left(\frac{-\lambda_3}{\epsilon_L}\right)^+\right)$$

$$V_M^* = \min\left(1, \left(\frac{-\lambda_6}{\epsilon_M}\right)^+\right)$$

$$V_I^* = \min\left(1, \left(\frac{-\lambda_4}{\epsilon_I}\right)^+\right)$$

<a id='0117d341-3008-4c11-8857-c5b39cf9341a'></a>

where the notation is

<a id='dcbcaac8-be28-4382-835e-2a37778b0663'></a>

r+ = {
r if r ≥ 0
0 if r < 0.

<a id='dbac4c09-f4d2-4e59-ac86-4976307c3c5d'></a>

The details of the proof are found in Appendix B.

We note that it is not possible to get a closed form solution to the formulation of the optimal control triple since each representation depends on a given adjoint variable which, in turn, depends on the other adjoints and the state variables due to the coupled nature of the system. However, this representation does reveal what those interdependencies are, and highlights the necessity of a numerical solution approach. For example, the form of control $V_M^*$ shows that a candidate for an optimal course of chemotherapy is far more complicated than the current standard treatment regimens that are given in the clinic. These standard regimens tend to follow a pattern of some days on, then some days off, depending on how much medication the patient can tolerate, and whether a weekend will interrupt treatment. However, an optimal regimen, according to our analysis, would not be only time dependent, but would additionally be modified as a function of current strength and activity of all four cell populations in the model.

<a id='4d437d7d-7244-4ef9-b3f5-928e884e2a30'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='2ca6899f-a249-47ec-8a9e-8eb1b6416ea7'></a>

66 de Pillis et al.

<a id='85b3b079-3890-4a22-b1eb-945257cacd37'></a>

## 6. Numerical Results of Quadratic Control Application

In this section, we develop graphical displays using Miser319 to visualize approximations to the optimal control for the objective functional (7) subject to (1)-(6). We note that we have used the first order necessary conditions for optimality subject to our specific objective functional. Since Miser3 calculates second order conditions, our computed solutions have the potential to lead to optimal results. However, the choice of initial conditions usually gives only locally optimal solutions. We simulate two types of scenarios: the first in which the initial tumor cell count is likely to be clinically imperceptible (T = 100, referred to as "small") and the second in which the tumor cell count is at the cusp of detection, (T = 1 × 107, referred to as "detectable").

<a id='2037f8a0-138d-4d74-9c35-ea5ba3a9bacc'></a>

In all numerical simulations, the two sets of initial conditions tested, "small"
and "detectable" are as follows. Small initial conditions are

<a id='1a8014e7-6cf4-4ffb-8a68-8cc9a0b9af36'></a>

T = 100, N = 3 \times 10^4, L = 30, I = 5 \times 10^2, C = 5 \times 10^6, M = 0.

<a id='1f333280-e037-4f61-b7fe-212281e514ad'></a>

With no control, this "small" set of initial conditions causes the tumor to be drawn into a semi-stable zero equilibrium.

<a id='1ee063ba-426a-4a55-944b-02056676d283'></a>

Detectable initial conditions are
$T = 1 \times 10^7$, $N = 5 \times 10^5$, $L = 2 \times 10^3$, $I = 2 \times 10^3$, $C = 4.17 \times 10^{10}$, $M = 0$.

<a id='1bdc0c47-df62-4a64-a457-da9a51c85de2'></a>

"Detectable" tumors cannot be controlled in our simulations by an immune system with the lymphocyte levels as specified, and if untreated, grow until the tumor size reaches the carrying capacity.

<a id='38b8ed97-f18e-463b-9e0c-643c4069ebbc'></a>

In each case, the form of the objective functional was that given in Eq. (7), with the \epsilon weights specified as follows: for the simulations of Figs. 1 and 2, \epsilon_I = 1 \times 10^7, \epsilon_L = 0 and \epsilon_M = 1 \times 10^7. For the simulations of Figs. 3 and 4, \epsilon_I = 0, \epsilon_L = 1 \times 10^7 and \epsilon_M = 1 \times 10^7. For the simulations of Figs. 5 and 6, \epsilon_I = 1 \times 10^5, \epsilon_L = 1 \times 10^5 and \epsilon_M = 1 \times 10^7. In all cases, treatment controls were given fairly heavy weights in the objective functional, which leads to minimizing treatment doses. Smaller weightings were also tested, which allowed for higher chemotherapy doses in particular, but did not result in tumor reduction any more significant than those shown in these simulations.

<a id='68d41cd9-8400-4670-9547-b119a1bd6127'></a>

In Figs. 1 to 4 and 6, the number of days of treatment has been limited to five. Figure 5 is allowed to run for ten days, so we can see the TIL therapy V<sub>L</sub> get turned on and off. We discuss this more below. These short term tests represent the first phase of a multiple treatment program. Work by Santana et al.<sup>50</sup> and Panetta et al.<sup>51</sup> emphasize that treatments for neuroblastoma and high-grade gliomas have incorporated such strategies. Arguments can be made that this may not be the optimal way to deliver treatment, but it is the reality that individuals receive treatment on Monday through Friday with a rest period of two days on the weekend.

<a id='c7b2195a-e939-4003-97db-5dc0c3c15ce0'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='1195fa7c-9756-4d5e-ac71-1de6bd219eab'></a>

Optimal Control of Mixed Immunotherapy

<a id='b4947b4f-3c32-487a-af2b-f708d657bf93'></a>

67

<a id='5548721c-ede4-4a9c-b677-44309f048291'></a>

<::chart: The figure displays two plots illustrating quadratic control for VL (IL-2 treatment) and VM (chemotherapy treatment) with detectable initial conditions. The overall title of the figure is "Two Quadratic Controls: VL, VM. Detectable 10^7 Initial Tumor". The x-axis for both plots is "Time (days)", ranging from 0 to 5. The caption for the figure is: "Fig. 1. Results of quadratic control for VL (IL-2 treatment) and VM (chemotherapy treatment), with 'detectable' initial conditions. Chemotherapy VM is the dominant treatment in this case. IL-2 treatment VL is so small in value that it is barely visible in the graph." The figure is composed of two subplots: Plot 1 (Top): States (Log Scale) vs. Time (days). The y-axis, labeled "States (Log Scale)", ranges from 10^0 to 10^15. The plot shows five lines: - Tumor: A red solid line, starting around 10^7 and slightly decreasing over time. - Natural Killers: A green dashed line, starting around 10^5 and slightly decreasing. - CD8+T: A cyan line marked with asterisks, starting around 10^4 and slightly decreasing. - IL-2: A magenta line marked with triangles, starting around 10^4 and slightly decreasing. - Circulating Lymphocytes: A dark blue dash-dot line, starting around 10^10 and remaining relatively constant. Plot 2 (Bottom): Control (normalized) vs. Time (days). The y-axis, labeled "Control (normalized)", ranges from -0.5 to 1.5. The plot shows two lines: - VL: A cyan line marked with asterisks, starting at 0 and remaining very close to 0 throughout the 5 days. - VM: A black solid line, starting at approximately 1.4 and decreasing to about 0.1 by day 5.::>

<a id='b1b53a22-446d-4592-b42e-f24533f6a238'></a>

Two Quadratic Controls: V₁, V_M. Small 10² Initial Tumor<::chart: The figure contains two line charts. The top chart shows "States (Log Scale)" on the y-axis (from 10⁻¹⁰ to 10¹⁰) versus "Time (days)" on the x-axis (from 0 to 5). It displays five lines: a red solid line for "Tumor", a green dashed line for "Natural Killers", a light blue line with asterisks for "CD8⁺T", a cyan line with squares for "IL-2", and a dark blue dash-dot line for "Circulating Lymphocytes". The bottom chart shows "Control (normalized)" on the y-axis (from 0 to 2.5 x 10⁻⁶) versus "Time (days)" on the x-axis (from 0 to 5). It displays two lines: a magenta line with triangles for "V₁" and a black solid line for "V_M".::>Fig. 2. Results of quadratic control for V₁ (IL-2 treatment) and V_M (chemotherapy treatment), with "small" initial conditions. As in the case with detectable initial tumor size, chemotherapy V_M is the dominant treatment, and IL-2 treatment V₁ is so small in value that it is barely visible in the graph.

<a id='fcacc901-2a8b-45ee-95df-d71235efe4f8'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='01c071fc-9ba1-4374-a52d-47186e95b400'></a>

68 de Pillis et al.

<a id='0767ee92-3367-4763-bf0b-56393c0bdcd7'></a>

<::chart: Two Quadratic Controls: V_L, V_M. Detectable 10^7 Initial Tumor

**Top Plot: States (Log Scale) vs. Time (days)**
This line chart shows the log scale of different states over 5 days.
- **Y-axis:** States (Log Scale), ranging from 10^0 to 10^15.
- **X-axis:** Time (days), ranging from 0 to 5.
- **Legend:**
  - **Tumor:** Red solid line. Starts around 2x10^6 and slightly decreases over 5 days.
  - **Natural Killers:** Green dashed line. Starts around 2x10^5 and decreases to around 1x10^5.
  - **CD8+T:** Cyan line with asterisks. Starts around 2x10^3 and slightly decreases.
  - **IL-2:** Magenta dashed line with plus signs. Starts around 2x10^3 and slightly decreases.
  - **Circulating Lymphocytes:** Dark blue dash-dot line. Starts around 1x10^11 and remains relatively constant.

**Bottom Plot: Control (normalized) vs. Time (days)**
This line chart shows normalized control values over 5 days.
- **Y-axis:** Control (normalized), ranging from -0.5 to 1.5.
- **X-axis:** Time (days), ranging from 0 to 5.
- **Legend:**
  - **V_L:** Cyan line with asterisks. Remains at approximately 0 throughout the 5 days.
  - **V_M:** Black solid line. Starts at approximately 1.4 and decreases smoothly to around 0.1 over 5 days.

Fig. 3. Results of quadratic control for V_L (TIL treatment) and V_M (chemotherapy treatment), with "detectable" initial conditions. Chemotherapy, V_M, is the dominant treatment. TIL therapy, V_L, is so small in value it may be considered practically zero.::>

<a id='1bf9ee30-a265-40b7-9b7a-3d84053a7065'></a>

For Figs. 1 and 2, combination therapy with IL-2 and chemotherapy is investigated. Similarly, Figs. 3 and 4, TIL therapy and chemotherapy are studied. One interesting concept to note is for the small or detectable initial tumor values the tumor and immune cells follow the same dynamics for IL-2 and chemotherapy and for TIL and chemotherapy. Yet, for the IL-2 and chemotherapy combination, the IL-2 is never activated. The chemotherapy protocol is the one that is found to be the best candidate to optimize the cancer problem. For the TIL and chemotherapy situation in Figs. 3 and 4, the treatments differ from each other. For the detectable initial tumor, our scenario suggests giving doses of chemotherapy in a continuously constant and decreasing manner, whereas for Fig. 4 with the small initial tumor population, TIL therapy dominates chemotherapy, but both are in small amounts. We see an initial increase in both TIL and chemotherapy over the first 12 hours of treatment, after which both therapies are steadily reduced until zero levels are reached by the end of day 5.

<a id='eb0acc29-f308-4abe-8f06-b2384a2edfa7'></a>

For a small initial tumor size, the immune system boosted by TIL can
fight the tumor so that it reduces to almost zero. This can have a positive

<a id='21eb1a47-ef8c-4343-ac56-8868931263a3'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='023d385c-c661-4b0d-9aff-54258a538165'></a>

Optimal Control of Mixed Immunotherapy

<a id='e2864397-5f35-4e73-bce0-586390ad8449'></a>

69

<a id='7836185c-06a7-4289-92f0-d0db19319bab'></a>

<::figure: Two line charts. The top chart is titled "Two Quadratic Controls: V_L, V_M. Small 10^2 Initial Tumor". The y-axis is "States (Log Scale)" ranging from 10^-10 to 10^10. The x-axis is "Time (days)" ranging from 0 to 5. The legend shows five lines: "Tumor" (red solid line), "Natural Killers" (green dashed line), "CD8+T" (cyan line with asterisks), "IL-2" (magenta line with triangles), and "Circulating Lymphocytes" (dark blue dash-dot line). The Tumor line starts around 10^2 and slightly decreases. Natural Killers and Circulating Lymphocytes remain high and relatively stable. CD8+T starts low, rises, and then slowly declines. IL-2 starts low and sharply decreases.The bottom chart's y-axis is "Control (normalized)" scaled by x 10^-5, ranging from 0 to 1. The x-axis is "Time (days)" ranging from 0 to 5. The legend shows two lines: "V_L" (cyan line with asterisks) and "V_M" (black solid line). The V_L line starts around 0.2, peaks around 0.85 at 0.5-1 day, and then gradually decreases to near 0 by 5 days. The V_M line starts around 0.15, peaks around 0.25 at 0.5 day, and then gradually decreases to near 0 by 5 days.Fig. 4. Results of quadratic control V_L (TIL treatment) and V_M (chemotherapy treatment), with "small" initial conditions. In this case, both TIL treatment, V_L, and chemotherapy treatment, V_M, are of the same order of magnitude, and both are low in value.::>

<a id='cf9e7060-a218-4b89-b5f0-43fb4939e2b7'></a>

effect for the patient because the volume of chemotherapy given is drastically reduced from the scenarios depicted by the immuno-chemotherapy combination in Fig. 2.

<a id='c63cfc08-70c3-41e2-96ec-50538467113f'></a>

In Fig. 5, all three treatment types are incorporated into the differential equa-tions system, and two back-to-back treatment periods of five days each are investi-gated. In our simulations, a five-day course alone did not turn on TIL treatment at all, whereas the ten-day course did. The tumor cells are only decreased marginally within this period. With a detectable initial tumor size, the expectation is that longer treatment schedules are needed. The treatment with three controls is very dif-ferent from those with only two controls. We note that in Fig. 5, no measurable IL-2 therapy is turned on, yet chemotherapy and TIL therapy strategies have changed. The chemotherapy is introduced at the maximum level with steadily decreasing doses given over the course of the ten-day period. The TIL therapy increases until about day 6 and then it decreases steadily over the remaining days. At the end of the treatment, no chemotherapy is given, but TIL is still given at a very low level.

<a id='b686a98c-a5b0-4eff-b64b-8377f5745e07'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='b8ac18ec-529f-4025-8b3e-bc4617401be4'></a>

70 de Pillis et al.<::chart: The figure contains two plots stacked vertically. The top plot is titled "Three Quadratic Controls: V_I, V_L, V_M. Detectable 10^7 Initial Tumor". The y-axis is labeled "States (Log Scale)" and ranges from 10^0 to 10^15. The x-axis is labeled "Time (days)" and ranges from 0 to 10. The plot shows five lines representing different states: a red solid line for Tumor, a green dashed line for Natural Killers, a cyan line with asterisks for CD8+T, a magenta line with upward triangles for IL-2, and a dark blue dashed-dot line for Circulating Lymphocytes. The bottom plot shows "Control (normalized)" on the y-axis, ranging from -0.5 to 1.5, against "Time (days)" on the x-axis, ranging from 0 to 10. This plot shows three lines representing treatment types: a cyan line with asterisks for V_L, a black solid line for V_M, and a magenta line with upward triangles for V_I. Fig. 5. Results of quadratic control for all three treatment types: V_I (IL-2 therapy), V_L (TIL therapy) and V_M (chemotherapy) with “detectable” initial conditions. Here, chemotherapy V_M dominates the treatment for the first half of the treatment interval, after which TIL V_L therapy becomes the dominant treatment. IL-2 V_I therapy is not switched on during this period.::>

<a id='e97c5f93-aa1d-4d31-9cbd-2360155ffa19'></a>

In Fig. 6, all three immune and chemotherapy treatments are again incorporated into the differential equation system, but for small initial tumor size. The tumor is reduced to zero in the five days of the treatment. Therefore, we do not consider any treatment past these five days. As in Figs. 2 and 4, the circulating lymphocytes exhibit an initial increase and then stabilize to approximately 10⁹ cells. The interleukin-2 cells decrease rather quickly which corresponds to an increased rate of decay in Eq. (5). Here, chemotherapy does not even get turned on. The TIL therapy is stepped up to a relatively high level on day 1, then decreased gradually to zero over the five remaining days. We note that the non-continuous nature of this graphical solution is an artifact of the MISER software settings, and that this image should be interpreted as an approximation only to the continuous solution. This immunotherapy administration can have a potentially positive effect with respect to tumor control without the negative side effects of the chemotherapy. Although care must be taken in relation to toxicity issues of TIL therapy, this is not a primary concern for a single five-day treatment period.

<a id='6f6304af-2645-4e57-b4e4-a84423fdf4ef'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='95ac0b91-d142-4901-9af0-1660a6807129'></a>

Optimal Control of Mixed Immunotherapy

<a id='0bb019c2-0c07-457c-a575-349f8945f10d'></a>

71

<a id='8f0fc7f6-fa62-4057-9a8b-245baee26654'></a>

Three Quadratic Controls: V_I, V_L, V_M. Small 10^2 Initial Tumor
<::chart: The figure displays two stacked line plots over a shared x-axis, "Time (days)", ranging from 0 to 5. The overall title for the figure is "Three Quadratic Controls: V_I, V_L, V_M. Small 10^2 Initial Tumor".

**Top Plot: States (Log Scale)**
- **Y-axis:** "States (Log Scale)"
- **Data Series:**
  - **Tumor:** Red solid line, starts high and decreases over time.
  - **Natural Killers:** Dark blue dashed line, remains relatively high and stable.
  - **CD8^+T:** Green dashed line, remains relatively high and stable.
  - **IL-2:** Light blue line with asterisks, starts high, decreases slightly, then stabilizes.
  - **Circulating Lymphocytes:** Dark blue dotted line, remains very high and stable.

**Bottom Plot: Control (normalized)**
- **Y-axis:** "Control (normalized)"
- **Data Series:**
  - **V_L:** Light blue line with asterisks, starts around 1, rises to a peak near 2.4 between 0.5 and 1 day, then gradually decreases back towards zero by 5 days.
  - **V_M:** Black solid line, remains at or very close to zero throughout the duration.
  - **V_I:** Pink solid line with triangles, remains at zero throughout the duration.

Fig. 6. Results of quadratic control for all three treatment types: V_I (IL-2 therapy), V_L (TIL therapy) and V_M (chemotherapy) with "small" initial conditions. In this case, TIL V_L is the dominant therapy. Chemotherapy is turned on initially for about 12 hours, but at such low levels it is not visible on the graph. IL-2 therapy, V_I, is not turned on. Our computed solution is theoretically continuous in this case. The non-continuous nature of the image is an artifact of the MISER software, and the image should be interpreted as an approximation only to a locally optimal solution.::>

<a id='90a0b7a0-5127-4afe-a6d9-537519374169'></a>

## 7. Conclusion

We have examined a model incorporating interacting tumor and immune cell pop-ulations and their responses to chemotherapy and immunotherapy treatments. The dynamics of the system without treatment reveal three equilibrium points for a spe-cific parameter case: one semi-stable zero equilibrium, one semi-stable small tumor equilibrium, and one stable large tumor equilibrium. Explicit studies on a lym-phocyte and cancer model by Lin⁵² depict a detailed analysis of similar scenarios with specific criteria for tumor extinction. Lin's work suggests that the addition of immunotherapy will shift the tumor population to a trajectory on which the tumor can be reduced to undetectable levels. Such an inclusion of immunotherapy via an optimal control analysis has been investigated. An optimal control study for chemotherapy and immunotherapy treatments for the square integrable case gives

<a id='d6f048e7-d5b2-4a0c-b636-cbed6c79afca'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='a6e42d4b-4fba-4ea8-901c-522975933763'></a>

72 de Pillis et al.

<a id='6051fdc7-7c95-4f28-82a9-104d5a5781a8'></a>

a representation of an optimal control triple that has the potential to minimize the tumor cell population. Similar work 16,53,54 provides comparisons of optimal control strategies for immunotherapy and chemotherapy, but these authors do not study the interaction among the therapies.

<a id='9c8c3f2a-a6df-45d5-b2bd-52855fab4ac9'></a>

The interaction among the three therapies (chemotherapy, TIL, and IL-2) is examined numerically. For small tumors, TIL therapy emerges as the dominant treatment for our given objective functional when all three treatment modalities are included, while for detectable tumors, chemotherapy is the course suggested by the numerical analysis. For larger tumors, there is an interplay between TIL and chemotherapy treatment with marginal reduction of the tumor cells for small time. We do note that the therapies are relatively constant for several hours or even days, but there are varying patterns of interacting therapies relative to tumor size. It is interesting to note that IL-2 therapy is non-existent for these scenarios. Forthcoming work will delve into the parameter estimates and will further investigate the IL-2 activation.

<a id='4fad1dee-8bfa-49a5-b6b0-274b5cb302e7'></a>

## Acknowledgments
This work was supported by the National Science Foundation under grant NSF-DMS-041-4011.

<a id='d7024e79-7d68-48fb-a81d-aa2257275a8c'></a>

# References

1. Rosenberg SA, Yang JC, Schwartzentruber DJ, Hwu P, Marincola FM, Topalian SL, Seipp CA, Einhorn JH, White DE, Steinberg SM, Prospective randomized trial of the treatment of patients with metastatic melanoma using chemotherapy with cisplatin, dacarbazine, and tamoxifen alone or in combination with interleukin-2 and interferon alfa-2b, *J Clin Oncol* **17**(3):968-975, 1999.
2. Huncharek M, Caubet JF, McGarry R, Single-agent DTIC versus combination chemotherapy with or without immunotherapy in metastatic melanoma: a meta-analysis of 3273 patients from 20 randomized trials, *Melanoma Res* **11**(1):75-81, 2001.
3. Castiglione F, Piccoli B, Optimal control in a model of dendritic cell transfection cancer immunotherapy, *Bull Math Biol* **68**(2):255-274, 2006.
4. Zhang XX, Black KL, Ong JM, Bogler O, Zhai Y, Wheeler CJ, T cell activity in glioma chemoresponsiveness and genetics, *Gene Ther Mol Biol* **9**:401-416, 2005.
5. Wheeler CJ, Black K, Dendritic cell vaccines and obstacles to beneficial immunity in glioma patients, *Curr Opin Mol Ther* **7**:35-47, 2005.
6. Wheeler CJ, Das A, Liu G, Yu JS, Black K, Clinical responsiveness of glioblastoma multiforme to chemotherapy after vaccination, *Clin Cancer Res* **10**:5316-5326, 2004.
7. de Pillis LG, Gu W, Radunskaya AE, Mixed immunotherapy and chemother-apy of tumors: modeling, applications and biological interpretations, *J Theor Biol* **238**(4):841-862, 2006.
8. de Pillis LG, Fister KR, Gu W, Maples K, Head T, Neal T, Yoshida K, Murugan A, Chemotherapy for tumors: an analysis of the dynamics and a study of quadratic and linear optimal controls, *Math Biosci* **209**:292-315, 2007.
9. CRI, Cancer and the Immune System: *The Vital Connection*, webpage publication of the Cancer Research Institute, 2000 (http://www.cancerresearch.org).

<a id='63ac13aa-0ace-48a8-a0c5-0fed7e62c93e'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='99d75c32-4bb7-4c70-aab9-65c802131d5a'></a>

Optimal Control of Mixed Immunotherapy

<a id='5a0ac125-9c5b-4766-9b56-a49d1a4f079f'></a>

73

<a id='336ee07d-7813-4c19-8209-2b2b2f52f671'></a>

10. Yu B, Kusmartsev S, Cheng F, Paolini M, Nefedova Y, Sotomayor E, Gabrilovich D,
Effective combination of chemotherapy and dendritic cell administration for the treatment of advanced-stage experimental breast cancer, Clin Cancer Res 9(1):285-294,
2003.
11. Abbas AK, Lichtman AH, Cellular and Molecular Immunology, 5th ed., Elsevier Saunders, 2005.
12. Janeway CA, Travers P, Walport M, Shlomchik M, Immunobiology, Garland Science, 2001.
13. Rosenberg SA, Lotze MT, Cancer immunotherapy using interleukin-2 and interleukin-2-activated lymphocytes, Annu Rev Immunol 4:681-709, 1986.
14. Osada T, Nagawa H, Shibata Y, Tumor-infiltrating effector cells of α-galactosylceramide-induced antitumor immunity in metastatic liver tumor, J Immune Based Ther Vaccines 2(7):1-9, 2004.
15. Dudley ME, Wunderlich JR, Robbins PF, Yang JC, Hwu P, Schwartzentruber DJ, Topalian SL, Sherry R, Restifo NP, Hubicki AM, Robinson MR, Raffeld M, Duray P, Seipp CA, Rogers Freezer L, Morton KE, Mavroukakis SA, White DE, Rosenberg SA, Cancer regression and autoimmunity in patients after clonal repopulation with antitumor lymphocytes, Science 298(5594):850-854, 2002.
16. Burden T, Ernstberger J, Fister KR, Optimal control applied to immunotherapy, Disc Cont Dyn Syst Ser B 4(1):135-146, 2004.
17. Fleming WH, Rishel RW, Deterministic and Stochastic Optimal Control, Springer-Verlag, 1975.
18. Pontryagin LS, Boltyanskii VG, Gamkrelidze RV, Mishchenko EF, The Mathematical Theory of Optimal Processes, Gordon and Breach, 1962.
19. Jennings LS, Fisher ME, Teo KL, Goh CJ, MISER3 Optimal Control Software: Theory and User Manual, Department of Mathematics, The University of Western Australia, Nedlands, WA 6907, Australia, 2004, Version 3 (available at http://www.cado.uwa.edu.au/miser/).
20. Britton NF, Essential Mathematical Biology, Springer Verlag, 2003.
21. Diefenbach A, Jensen ER, Jamieson AM, Raulet D, Rael and H60 ligands of the NKG2D receptor stimulate tumor immunity, Nature 413:165-171, 2001.
22. Kawarada Y, Ganss R, Garbi N, Sacher B, ad Arnold T, Hammerling G, NK- and CD8+T cell-mediate eradication of established tumors by peritumoral injection of CpG-containing oligodeoxynucleotides, J Immunol 167(1):5247-5253, 2001.
23. Germain RN, An innately interesting decade of research in immunology, Nat Med 10(12):1307-1320, 2004.
24. Kieper WC, Prlic M, Schmidt CS, Mescher MF, Jameson SC, Il-12 enhances CD8 T cell homeostatic expansion, J Immunol 166:5515-5521, 2001.
25. Roitt IM, Brostoff J, Male DK, Immunology, Mosby, St. Louis, 1993.
26. Kirschner D, Panetta JC, Modeling immunotherapy of the tumor-immune interaction, J Math Biol 37(3):235-252, 1998.
27. Adam JA, Bellomo N (eds.), Basic models of tumor-immune system interactions — Identification, analysis and predictions, in A Survey of Models for Tumor-Immune System Dynamics, Birkhauser, 1997.
28. Mustafa MM, Buchanan GR, Winick NJ, McCracken GH, Tkaczewski I, Lipscomb M, Ansari Q, Agopian MS, Immune recovery in children with malignancy after cessation of chemotherapy, J Pediatr Hematol Oncol 20(5):451-457, 1998.
29. Melichar B, Dvorak J, Jandik P, Touskova M, Solichova D, Megancova J, Voboril Z, Intraarterial chemotherapy of malignant melanoma metastatic to the liver, Hepatogastroenterology 48(42):1711-1715, 2001.

<a id='807c0261-a4f8-4baf-8ade-c841e3e86811'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='3152ed5c-9367-4a34-ab8b-c2d41d02ff9f'></a>

74 de Pillis et al.

<a id='1bf64d68-8847-4049-b01c-c7f1702349be'></a>

30. Glas R, Franksson L, Une C, Eloranta M, Ohlen C, Orn A, Karre K, Recruitment and activation of natural killer (NK) cells in vivo determined by the target cell phenotype: an adaptive component of NK cell-mediated responses, J Exp Med 191(1):129-138, 2000.
31. Pazdur R, Hoskins W, Wagman L, Coia L (eds.), Principles of chemotherapy, Can- cer Management: A Multidisciplinary Approach, 8th ed., in Oncology Publishing Group of CMP Healthcare Media, 2004 (available at http://www.cancernetwork.com/ handbook/contents.htm), accessed May 2005.
32. Gardner SN, A mechanistic, predictive model of dose-response curves for cell cycle phase-specific and nonspecific drugs, Cancer Res 60:1417-1425, 2000.
33. Jiang H, Chess L, An integrated view of supporessor T cell subsets in immunoregu- lation, J Clin Invest 114(9):1198-1208, 2004.
34. de Pillis LG, Radunskaya AE, Wiseman CL, A validated mathematical model of cell- mediated immune response to tumor growth, Cancer Res 61(17):7950-2958, 2005.
35. Gett A, Sallusto F, Lanzavecchia A, Geginat J, T cell fitness determined by signal strength, Nat Immunol 4(4):355-360, 2003.
36. Gilbertson SM, Shah PD, Rowley DA, NK cells suppress the generation of Lyt-2+ cytolytic T cells by suppressing or eliminating dendritic cells, J Immunol 136(10):3567-3571, 1986.
37. Kuznetsov V, Makalkin I, Taylor M, Perelson A, Nonlinear dynamics of immuno- genic tumors: parameter estimation and global bifurcation analysis, Bull Math Biol 56(2):295-321, 1994.
38. Curti B, Ochoa A, Urba W, Alvord G, Kopp W, Powers G, Hawk C, Creekmore S, Gause B, Janik J, Holmlund J, Kremers P, Fenton R, Miller L, Sznol M, Smith II J, Sharfman W, Longo D, Influence of interleukin-2 regimens on circulating populations of lymphocytes after adoptive transfer of anti-CD3-stimulated T cells: results from a phase I trial in cancer patients, J Immunother Emphasis Tumor Immunol 19(4):296- 308, 1996.
39. Hara I, Hotta H, Sato N, Eto H, Arakawa S, Kamidono S, Rejection of mouse renal cell carcinoma elicited by local secretion of interleukin-2, Jpn J Cancer Res 87(7):724-729, 1996.
40. Lumsden A, Codde J, Van Der Meide P, Gray B, Immunohistochemical character- isation of immunological changes at the tumour site after chemo-immunotherapy with doxorubicin, interleukin-2 and interferon-y, Anticancer Res 167(7):1145-1154, 1996.
41. de Pillis LG, Radunskaya A, The dynamics of an optimally controlled tumor model: a case study, Math Comput Model 37:1221-1244, 2003.
42. de Pillis LG, Radunskaya AE, Immune response to tumor invasion, in Bathe KJ (ed.), Computational Fluid and Solid Mechanics, Vol. 2, M.I.T., pp. 1661-1668, 2003.
43. Perry MC (ed.), The Chemotherapy Source Book, 3rd ed., Lippincott Williams & Wilkins, 2001.
44. Holland JF, Emil III F (eds.), Cancer Medicine, Lea and Febiger, Chapter II-3, XII, XV, 1973.
45. National Cancer Institute, Understanding Chemotherapy (available at http://www. nci.nih.gov/cancertopics/chemotherapy-and-you/page2), accessed May 2005.
46. Calabresi P, Schein PS (eds.), Medical Oncology: Basic Principles and Clinical Man- agement of Cancer, 2nd ed., McGraw-Hill, New York, 1993.
47. Yates A, Callard R, Cell death and the maintenance of immunological memory, Disc Cont Dyn Syst Ser B 1(1):43-59, 2002.
48. Bannock L, Nutrition (available at http://www.doctorbannock.com/nutrition).html.

<a id='a05e33d3-9773-4f7d-8115-6d2f6020188d'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='15428d9c-504d-445f-b461-687ae34e9f97'></a>

Optimal Control of Mixed Immunotherapy

<a id='4d2ae946-e9af-4146-8718-89d429ff843e'></a>

75

<a id='403c42cd-bf62-45d0-a415-6fa13e7befb8'></a>

49. Hauser B, *Blood Tests*, technical report, International Waldenstrom's Macroglobuline-mia Foundation, January 2001 (available at http://www.iwmf.com/Blood_Tests.pdf), accessed May 2005.
50. Santana V, Furman W, Billups C, Hoffer F, Davidoff A, Houghton P, Stewart C, Improved response in high-risk neuroblastoma with protracted topotecan administa- tion using a pharmacokinetically guided dosing approach, *J Clin Oncol* **23**(18):4039- 4047, 2005.
51. Panetta J, Kirstein M, Gajjar AJ, Nair G, Fouladi M, Stewart C, A mechanistic mathematical model of temozolomide myelosuppression in children with high-grade gliomas, *Math Biosci* **186**:29-41, 2003.
52. Lin A, A model of tumor and lymphocyte interactions, *Disc Cont Dyn Syst Ser B* **4**(1):241-266, 2004.
53. Ledzewicz U, Schättler H, Optimal control for a class of compartmental models in cancer chemotherapy, *Int J Appl Math Comput Sci* **13**(3):357-368, 2003.
54. Ledzewicz U, Schättler H, Comparison of optimal controls for a model in cancer chemotherapy with *l*₁ and *l*₂ type objectives, *Optim Methods Softw* **19**(3-4):339-350, 2004.
55. Ermentrout B, *Simulating, Analyzing, and Animating Dynamical Systems: A Guide to XPPAUT for Researchers and Students*, SIAM, 2002.
56. Lukes DL, *Differential Equations: Classical to Controlled*, Vol. 162, Academic Press, 1982.

<a id='f88f9340-9cd6-4fc8-bf42-03929f27e61c'></a>

## Appendix A

In this appendix, we numerically analyze the specific equilibria that correspond to the parameter values that have been used in this manuscript. We find the fixed points by setting all the derivatives in (1)–(6) to equal zero when no treatment is given ($V_L = V_I = V_M = 0$).

First, we note that

<a id='0639dc93-fdc8-4959-b888-6dc709ba96b0'></a>

dM/dt = -γM = 0,

<a id='8ef8cbde-1409-4c10-be9d-a7e9b815c234'></a>

so $M = 0$. It follows from (4) that $C = \frac{\alpha_2}{\beta}$.
Next, we consider

$\frac{dT}{dt} = aT(1 - bT) - c_1NT - DT - K_TMT$

<a id='05cd996a-a931-4e11-bc2a-0065e0f5a89d'></a>

= T(a - abT - c₁N - D - K₄T M) = 0.

<a id='ed40ed52-4f19-4d7d-8052-6a020838a8da'></a>

Thus, $T = 0$ or $a - abT - c_1N - D - K_TM = 0$. We will first examine the case $T = 0$.

<a id='8bbdfe64-314f-46e6-8c1b-52d6272c5859'></a>

Then,

<a id='0bc49896-eb13-4411-a29a-0f9c13dc056a'></a>

dN/dt = α1 - fN = 0
⇒ N = α1 / f.

<a id='a1cf12fe-5ae7-4976-812d-ce6746246232'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='b316d1d6-c9a3-4daa-b136-2fedd5802ce4'></a>

76 de Pillis et al.

<a id='1447a987-49b7-4b9d-8d1e-46d5b85b9aec'></a>

Also,

$\frac{dL}{dt} = -mL - uL^2 + \frac{p_I LI}{g_I + I} = -L \left[m + uL - \frac{p_I I}{g_I + I}\right].$

<a id='b46ff488-7458-4543-835a-54ff91a3ccc9'></a>

For this condition to be satisfied, either L = 0 or m + uL - p_I I / g_I + I = 0.
If L = 0, then, it follows from (5), I = 0. Otherwise,

<a id='373f1831-6c35-445f-9b10-d7960ad01767'></a>

L = ( (p_1I) / (g_1+I) - m ) / u .
(9)

<a id='6938495c-4206-40b1-8c80-f9715dcf697f'></a>

Additionally,

<a id='874032fe-df3b-42ba-bac8-c7beb9ba4d25'></a>

$$\frac{dI}{dt} = wLI - \mu_I I = I(wL - \mu_I).$$

<a id='e5117060-7d50-4c0d-ac15-3718996495c2'></a>

If I = 0, (9) suggests that $L = -\frac{m}{u}$, which is not biologically relevant, since then,
$L < 0$.

<a id='45c8c27b-cedd-4aaa-acf8-689ccf2eb04b'></a>

If I ≠ 0, L = μI / w, which when substituted into (9), leads to

<a id='dd350da2-ebe3-4a7b-8053-3f7e88d01b92'></a>

I = \frac{\mu_I ug_I + wmg_I}{wp_I - wm - \mu_I u}
Now we consider the case where T ≠ 0 and T satisfies

<a id='638ea24a-d07c-4d19-bf0c-6f2382d71179'></a>

a - abT - c_1N - D - K_TM = 0.

<a id='01ecf841-7d97-4b7a-beba-9453ad60ddc2'></a>

Solving for D (with M = 0 at equilibrium) yields

<a id='39061f7d-716f-4f86-acec-5c09bbfc5b33'></a>

<::D = a - abT - c₁N.
: equation::>

<a id='e76b5adb-8dfe-48df-8a4b-52523fced8da'></a>

Substituting the definition for D gives us the result that

$L = T\sqrt{\frac{s(a - abT - c_1N)}{d + abT + c_1N - a}}$ (10)

<a id='f0ee3bdd-3a0d-47cd-a6d4-75c5d8866445'></a>

To find N in terms of T, we examine the condition $\frac{dN}{dt} = 0$.

$\frac{dN}{dt} = \alpha_1 - N \left(f - g \frac{T^\eta}{h + T^\eta} + pT\right).

<a id='32ae78eb-9b3f-4fa8-aaaf-bb6550665a77'></a>

This implies

$$N = \frac{\alpha_1}{f - g^{\frac{T_\eta}{h + T_\eta}} + pT} \quad (11)$$

<a id='17a6c048-71e6-435f-8c88-9603c64ba65e'></a>

Substituting (11) into (10) now gives _L_ in terms of _T_.
Finally, solving for $\frac{dI}{dt}$ = 0 results in

<a id='a1001708-e8a6-406b-85e6-fee9598ac1d4'></a>

$$I = \frac{p_T TL}{(g_T + T)(\mu_I - wL)} \quad (12)$$

<a id='2ded58e1-2747-4df2-80bc-f882f96949c1'></a>

We now take the right sides in the expressions from (10), (11), and (12)
and define them as functions $f_L, f_N, f_I$ respectively. We have $L = f_L(T, N)$,

<a id='74353996-c5ca-4995-8a17-44923ae7d49b'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='af46b514-777b-4ece-b3c3-e1b2649be953'></a>

Optimal Control of Mixed Immunotherapy

<a id='fa69ca5c-f00f-46e6-9efb-b82a6ffc4718'></a>

77

<a id='58429160-4b4a-4dbe-8c3e-eb9771c81af8'></a>

N = fN(T), and I = fI(T, L). We can then solve for L, N and I at equilib-rium in terms of T. Thus, L = FL(T) = fL(T, fN(T)), N = FN(T) = fN(T), and I = FI(T) = fI(T, fL(T, fN(T))).

<a id='c57cb787-27c1-47f4-9a2d-57336e4e846a'></a>

By substituting these functions into the expression for $\frac{dL}{dt} = 0$, we can now find the equilibrium points by using a numerical root finder to solve for $T$ at equilibrium (call it $T^*$). Once we know $T^*$, we can evaluate $F_L(T)$, $F_N(T)$, $F_I(T)$ to find $L^*$, $N^*$, $I^*$. We know from our earlier analysis that $M^* = 0$ and $C^* = \frac{\alpha}{\beta}$, therefore, we can find the equilibria for the system (1)-(6) numerically using these equations.

<a id='d26a8cf9-2673-4db6-86ae-816198a7110d'></a>

The analysis is sufficiently general to use any value of l and η. For the purposes of simulation, we have chosen l = 2/3 and η = 1, as shown in the parameter table.

<a id='d473b638-d6e3-426f-b999-59fd00d24146'></a>

To find the values of the state variables at the $T = 0$ equilibrium points, two cases must be considered. First, if $L = 0$, we then know $I = 0$ and therefore the values of the other state equations are calculated as $T = 0$, $N \approx 2.5391 \times 10^5$, $C \approx 1.0083 \times 10^7$, and $L, I, M = 0$.

<a id='91a11407-9d64-40f1-be85-5c14440202b5'></a>

The eigenvalues of the Jacobian associated with this fixed point above are e_1 = -0.0200, e_2 = -0.0412, e_3 = 0.4320, e_4 = -10, e_5 = -0.0120, and e_6 = -0.9.

<a id='977d1235-3920-4d6e-98d1-c97bafdf8eac'></a>

This fixed point has five negative real eigenvalues and one positive real eigen-value, and is therefore semi-stable. Biologically, means that a small tumor cell population has the potential either to be drawn down to the zero equilibrium, or to be pushed away from zero, depending on the initial state of the system. If the T = 0 fixed point were locally stable, then a tumor with only one cell would be attracted back to the T = 0 point and no tumor would ever grow.

<a id='db326ad3-066a-4ce2-80d6-63f86aa2c94a'></a>

In the case when L ≠ 0, we then have T = 0, N = 2.5391 × 10⁵,
C = 1.0083 × 10⁷, L = 5 × 10⁴, I = −5 × 10⁴, and M = 0.
However, because in this case I < 0, we can see that with the current parameters,
this fixed point has no physically relevant meaning.

<a id='bbd13128-a028-438c-a411-6c04b9af9fa1'></a>

The $T \ne 0$ fixed points were found numerically using the method described previously by finding roots of $\frac{dL}{dt} = 0$ in terms of $T^*$, then substituting $T = T^*$ in the functions $F_L(T)$, $F_N(T)$, and $F_I(T)$ to find the other state variables at the fixed point.

<a id='0b8164fa-9c58-4f17-be92-5941b1af3523'></a>

Preliminary analysis used this function plotted in Matlab and showed two phys-ically meaningful roots: one at a small tumor size and the other at a much larger tumor size.

<a id='013852b8-14eb-43c3-8c10-586ee6260d74'></a>

To find the exact values of the state equations at these equilibrium points numerically, we used XPP, 55 software for analyzing dynamical systems. XPP uses a Newton method solver to find the fixed points of the system. The Newton solver tolerance for this analysis was set to 0.01, the Jacobian epsilon was set to 0.001, and the maximum number of iterations allowed by the solver to find the root was 1\times10^{6}.

<a id='2591f022-91d7-4613-a152-172f6b5f1b4f'></a>

The small tumor size fixed point was found to be approximately at the val-ues $T = 5.695 \times 10^5$, $N = 1.777 \times 10^5$, $C = 4.17 \times 10^{10}$, $L = 487.13$, and $I = 25.11$ with the associated eigenvalues $e_1 = -2924.209828$, $e_2 = 0.069246$, $e_3 = -0.096113$, $e_4 = 9.485163$, $e_5 = -0.9$, and $e_6 = -0.012$.

<a id='5bc298a1-4376-456d-8cb8-7dd316a7096f'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='6833a84c-db9c-4aea-b593-716f892017ea'></a>

78 de Pillis et al.

<a id='69eca6b6-e1c8-4346-8f9f-fbb4024df9d0'></a>

The location of the large tumor size fixed point was approximately at
T = 9.20 \times 10^8, N = 141.3, C = 4.17 \times 10^{10}, L = 19577, I = 1930, and M = 0 with
eigenvalues e_1 = -117518.189526, e_2 = -0.183657, e_3 = -91.994417, e_5 = -0.9,
and e_6 = -0.012.

<a id='8a3b265f-9c8a-4c3d-93f5-e9759472cb6e'></a>

With the parameters as stated, the small tumor equilibrium is semi-stable while the large tumor equilibrium is stable. For the small tumor equilibrium point, we see that instability and semi-stability make biological sense. If there were an attracting or stable fixed point at a small tumor size, then any tumor that started in the basin of attraction of a stable small tumor equilibrium point would be attracted to that point and never grow any larger. However we know that tumors do surpass this small tumor size, therefore we expect an unstable or semi-stable equilibrium point. For the large tumor equilibrium point, the stability also makes sense since this allows the tumor to grow to the maximal volume that the host can sustain.

<a id='5c5d8c97-c6f1-4731-a132-6bb9549c61e0'></a>

## Appendix B: Analysis of Supersolutions
We determine solutions that are upper bounds (super-solutions) of _T_, _L_, _N_, _C_, _I_ and _M_ in (1)–(6). The sub-solutions are zero. We first consider the right hand side of (4), the circulating lymphocyte population. With _C_max as an upper bound solution associated with _C_ and with _M_(_t_) ≥ 0 and _C_(_t_) ≥ 0, then _C_max = _α_2_t_f + _C_0. Similarly if _T_m is the upper bound on the solution for Eq. (1), then _T_m = _T_0_e_^_αtf_.

<a id='43280c81-22c0-4dfc-ae18-20319ad8306f'></a>

If we have that Lm is the upper bound on the solution for Eq. (2),
then dLm/dt - pILm = C2 where C2 depends on Cm and Tm. Furthermore,
Lm(t) = [-C2/pI (e^-prt - 1) + L0] e^pIt and Lm ≤ (C2/pI + L0) e^pItf.

<a id='6a5f0d34-d5af-4639-b884-ef7fb449511d'></a>

By using the bounds $C_m, T_m, L_{max}$ we can form a set of upper bound solutions for system (1)-(6). If we let these be denoted by $\overline{T}, \overline{L}, \overline{N}, \overline{C}, \overline{I}$, and $\overline{M}$, we have the system

<a id='4356f1c3-ad25-4b3f-993e-1318b0a380a2'></a>

$$\frac{d\bar{T}}{dt} = a\bar{T},$$ 

$$\frac{d\bar{N}}{dt} = \alpha_1 + g\bar{N},$$

$$\frac{d\bar{I}}{dt} = p_t\bar{L} + wL_m\bar{I} + v_I,$$ 

$$\frac{d\bar{L}}{dt} = p_I\bar{L} + v_L + r_2C_mT_m$$

$$\frac{d\bar{C}}{dt} = \alpha_2$$

$$\frac{d\bar{M}}{dt} = v_M$$
(13)

<a id='97f1e07b-b6a9-46e1-8256-46dfa470708b'></a>

that is bounded on a finite time interval. We can use a comparison result to obtain that our original system is bounded. We use this work in proving that an optimal control exists for our problem. We define \f as the class of ($X_0$, $\vec{V}$) such that $\vec{V}$ is a measurable function on $[0, T]$ with values in $U$ and the solution of (1)-(6) satisfies the initial conditions for a given $\vec{V}$.

<a id='ec2b90a0-6be5-4b5a-8063-3fdec1e2ee78'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='18d35892-d5e9-4c5e-af81-4ae436fe8db0'></a>

Optimal Control of Mixed Immunotherapy

<a id='d9c3c82a-cbb9-46b6-9b13-690ac2b9a5c5'></a>

79

<a id='402271ec-e9b1-4aa8-83e0-9d95916559df'></a>

Theorem B.1. Given the objective functional in (7), where

$U = \{ \vec{V}(t), \text{Lebesgue measurable} \mid 0 \leq \vec{V}(t) \leq 1 \forall t \in [0,t] \}$

<a id='3a52ef8b-6c35-4f5b-b9d1-5fb0b1d0d4e4'></a>

subject to system (1)-(6) with $T(0) = T_0$, $L(0) = L_0$, $N(0) = N_0$, $C(0) = C_0$, $I(0) = I_0$, $M(0) = M_0$ or $\vec{X}_0$, then there exists an optimal control $\vec{V}^*$ such that $\min_{\vec{V}^*(t)\in[0,1]} J(\vec{V}) = J(\vec{V}^*)$ if the following conditions are met:

<a id='708aa547-01cb-4fdd-8ee7-02b72144514d'></a>

(1) $\mathcal{F}$ is not empty.
(2) The admissible control set $U$ is closed and convex.
(3) Each right hand side of the state system is continuous, is bounded above by the sum of the bounded control and the state, and can be written as a linear function of $\vec{V}$ with coefficients depending on time and the state.
(4) The integrand of $J(\vec{V})$ is convex on $U$ and is bounded below by $-c_2+c_1\vec{V}^2$ with $c_1 > 0$.

<a id='5d5758ca-27f0-4526-9dde-7abbd95d09b1'></a>

**Proof.** Since the system (1)-(6) has bounded coefficients and the solutions are bounded on the finite time interval, we can use a result from Lukes,56 (Theorem 9.2.1, p. 182), to obtain the existence of the solution of the system (1)-(6). Secondly, we note that U is closed and convex by definition. For the third condition, the right hand side of system (1)-(6) must be continuous. The right hand side is continuous since the denominators of all fractions from the right hand side of this system consist solely of positive entities.

<a id='fbb54181-4e7e-4ef0-a7ad-8231f634145f'></a>

We let $\vec{a}(t, \vec{X})$ be the right hand side of system (1)–(6) except for the terms of
$\vec{V}$ and define

<a id='28a186d4-7f13-44ff-bc7a-bf94df857b12'></a>

$$\vec{f}(t, \vec{X}, \vec{V}) = \vec{a}(t, \vec{X}) + \begin{pmatrix} 0 \\ V_L \\ 0 \\ 0 \\ V_I \\ V_M \end{pmatrix}, \text{ with } \vec{X} = \begin{pmatrix} T \\ L \\ N \\ C \\ I \\ M \end{pmatrix}.$$

<a id='88aad23c-8bd4-47df-8251-c1b9fce1b01d'></a>

Using the boundedness of the solutions, we see that

$\left|\vec{f}(t, \vec{X}, v_M)\right| \le \begin{pmatrix}
a & 0 & 0 & 0 & 0 & 0 \\
0 & p_I & 0 & r_2 T_m & 0 & 0 \\
0 & 0 & g & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & p_t & 0 & 0 & w L_{\max} & 0 \\
0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix} \begin{pmatrix}
T \\
L \\
N \\
C \\
I \\
M
\end{pmatrix} + \begin{pmatrix}
0 \\
V_L \\
\alpha_1 \\
\alpha_2 \\
V_I \\
V_M
\end{pmatrix}$

$\le C_1 \left(|\vec{X}| + |\vec{v}|\right)$

<a id='3a64474b-3c2f-4105-b01e-6a2027cef458'></a>

where $C_1$ depends on the coefficients of the system.

<a id='79e40948-55ed-48f0-b4b3-02b80dedb0b7'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='b4b94015-efe7-4b20-b765-897204c781b3'></a>

80 de Pillis et al.

<a id='e5164701-d670-4fc1-98df-7a7fbd071702'></a>

For the fourth condition, the convexity follows since the integrand involves squared terms. The boundedness condition therefore follows. □

<a id='1998388f-286d-439c-bdca-60095fd9d91f'></a>

Since we have the existence of an optimal control triple, we next determine the
necessary conditions associated with it via Pontryagin's Maximum Principle. The
statement of Theorem 5.1 is in Sec. 5, Optimal Control.

<a id='2eb1a8f8-1770-4ac3-9dd6-857085ae0927'></a>

**Proof.** The form of the adjoint equations and the transversality conditions are standard results from Pontryagin's Maximum Principle.18 To find the representation for $\vec{V}^*(t)$, we analyze the necessary condition for optimality $\frac{\partial \mathcal{L}}{\partial V_L} = 0$, $\frac{\partial \mathcal{L}}{\partial V_I} = 0$, and $\frac{\partial \mathcal{L}}{\partial V_M} = 0$, respectively. For example,

<a id='954cde00-91da-4186-838e-7c2d627adf58'></a>

∂L
-- = 
∂VL
∂H
-- - W₁ + W₂ = 0
∂VL
⇒ εLVL + λ₃ - W₁ + W₂ = 0.

<a id='6443ded9-1dee-4a1a-8f78-3571c697d5f1'></a>

Using standard optimality results, we can find necessary conditions for the optimal control for $V_L(t)$ as

<a id='5ff99303-3507-4bd9-8d99-05d8a8b7a71c'></a>

$$V_L^* = \min\left(1, \left(\frac{-\lambda_3}{\epsilon_L}\right)^+\right). \quad (14)$$. 

<a id='37266684-7ee9-4c42-8fb6-eeb1145a65b5'></a>

Similarly, we can show that

<a id='d4b29f4b-8880-45b6-b0b8-c24fc8d12697'></a>

V_M^* = \min \left(1, \left(\frac{-\lambda_6}{\epsilon_M}\right)^+\right) and (15)
V_I^* = \min \left(1, \left(\frac{-\lambda_4}{\epsilon_I}\right)^+\right). (16)

\square

<a id='3d9f8566-df90-45eb-8e79-44323be569d4'></a>

J. Biol. Syst. 2008.16:51-80. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/22/25. Re-use and distribution is strictly not permitted, except for Open Access articles.
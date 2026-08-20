<a id='5187b5db-f05e-4c23-8318-286ca151dd1d'></a>

NATIONAL INSTITUTES OF HEALTH

NIH Public Access
**Author Manuscript**
Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='08eb860d-1eca-4667-b7dd-5fc1a04951ca'></a>

Published in final edited form as:
_Math Biosci_. 2007 September ; 209(1): 14–29. doi:10.1016/j.mbs.2007.01.007.

<a id='8d55abc5-9e8f-49ea-9dc5-622782f020a9'></a>

**Infection dynamics in HIV-specific CD4 T cells: does a CD4 T cell boost benefit the host or the virus?**

**Dominik Wodarz** ,* and **Dean H. Hamer**

1 Department of Ecology and Evolutionary Biology, 321 Steinhaus Hall, University of California, Irvine, CA 92697, USA

2 Laboratory of Biochemistry, NCI/DDR, 37 Convent Drive, Building 37, Room 6002, MSC 4255, Bethesda, MD, USA

<a id='1ee29db5-0710-4412-9965-7ab633a07a86'></a>

# Abstract
Recent experimental data have shown that HIV specific CD4 T cells provide a very important target for HIV replication. We use mathematical models to explore the effect of specific CD4 T cell infection on the dynamics of virus spread and immune responses. Infected CD4 T cells can provide antigen for their own stimulation. We show that such auto-catalytic cell division can significantly enhance virus spread, and can also provide an additional reservoir for virus persistence during anti-viral drug therapy. In addition, the initial number of HIV-specific CD4 T cells is an important determinant of acute infection dynamics. A high initial number of HIV-specific CD4 T cells can lead to a sudden and fast drop of the population of HIV-specific CD4 T cells which results quickly in their extinction. On the other hand, a low initial number of HIV-specific CD4 T cells can lead to a prolonged persistence of HIV specific CD4 T cell help at higher levels. The model suggests that boosting the population of HIV-specific CD4 T cells can increase the amount of virus-induced immune impairment, lead to less efficient anti-viral effector responses, and thus speed up disease progression, especially if effector responses such as CTL have not been sufficiently boosted at the same time.

<a id='c9e16ca3-bfd9-4a95-82f9-d0cebfea3435'></a>

# 1. Introduction
CD4 T helper cells are a major target for the replication of human immunodeficiency virus (HIV). On the other hand, CD4 T cells are also a central component which orchestrates the generation of specific immune responses through the delivery of help. Recent studies have shown that a significant proportion of HIV-specific CD4 T cells are infected by the virus, and that this specific population of T cells might be preferentially infected [1]. This has important implications for understanding the dynamics between HIV and immune responses. Infection of HIV-specific CD4 T cells can have several consequences for the dynamics between the virus and the immune system. For example, it enables the virus to spread via the

<a id='858ed879-8f7b-457d-9796-3e8b89265f30'></a>

* corresponding author: email: dwodarz@uci.edu, phone: 949-824-2531, Fax: 949-824-2181.
**Publisher's Disclaimer:** This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

<a id='68c5ffb1-ccca-4681-a6e6-88836ff9c17a'></a>

NIH-PA Author Manuscript

<a id='31f7d297-8f0a-4a03-82f1-f462a64ffafd'></a>

NIH-PA Author Manuscript

<a id='abd5fed7-108c-4f88-9f80-41f24ee30709'></a>

NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='2c11c6d4-7211-4e27-b2c9-8933537df458'></a>

Wodarz and Hamer

<a id='88a71555-4316-45f2-9a03-e4c753286173'></a>

Page 2

<a id='b12b35ae-d48d-4e03-9a3a-7d6559369d26'></a>

division of infected T cells. Moreover, this spread can be considered autocatalytic, since T cells proliferate in response to antigenic stimulation. (The higher the virus load, the more efficient the rate of mitotic spread). Infection of HIV-specific CD4 T cells can also result in efficient impairment of effector responses, such as cytotoxic T lymphocytes (CTL) or antibodies, because the ability to deliver help may be subverted [2-4].

<a id='932caff7-5234-4de2-818a-72712664f1d6'></a>

Mathematical models have provided important insights into the dynamics between HIV replication and immune responses [5-7]. While some models have analyzed the effect of specific helper cell infection and immune impairment [8], the detailed dynamics of virus spread in HIV-specific CD4 T cells has so far not been taken into account explicitly. Here, we construct mathematical models which describe the infection dynamics in HIV-specific CD4 T cells in detail, and ask how this affects the dynamics between virus spread and effector responses. We start by examining the dynamics of autocatalytic virus spread via the division of infected CD4 T cells. We then expand the model to include infectious spread of the virus and alternative target cells which do not react against HIV (T cells with other specificities or antigen presenting cells). We ask how a change in the initial number of HIV-specific CD4 T cells can influence the outcome of the dynamics during the initial stages of the infection. Further, we explore how infection of HIV-specific CD4 T cells influences virus dynamics during drug treatment.

<a id='57279266-2c28-49f2-87aa-f60132cd3e1e'></a>

The general approach to the article is as follows. We start from very a very simple model that forms the core for understanding the effect of autocatalytic virus spread. Although this very simple model lacks much of HIV biology, it allows us to obtain some basic analytical insights into the properties of autocatalytic virus spread. Once we have analyzed and understood this system, we will subsequently include more biological reality and complexity. That is, several models are discussed, ranging from simple to complex. The models are investigated analytically and by numerical simulations. The aim is to demonstrate potential consequences of autocatalytic virus spread and the dual role of CD4 T cells in HIV infection. At this stage, not enough parameter values are known, and not enough details are known about the biological processes underlying the model assumptions for quantitative predictions to be possible. However, a general analysis of the dynamics is a first step for a better understanding, and can provide valuable information for the design of vaccines. Also, please note that the models presented here are specifically tailored to investigate the questions posed here, and thus do not take into account aspects of HIV dynamics that are not directly relevant to these questions (e.g. immune escape and antigenic variation, or aspects of long term progression of the disease).

<a id='261ce619-27ea-402c-a292-fa49edd76c7c'></a>

## 2. Basic dynamics of autocatalytic virus spread

We start by looking at the simplest model of autocatalytic virus spread. We assume the existence of infected HIV specific CD4 T cells which can produce new virions, and ask under which circumstances this population of cells will grow and expand. The model is given by the following differential equations which describe the development of the cells over time.

<a id='641ef114-7780-46ff-9eff-0d7507eddd7f'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='c49170d4-9fe0-43c5-a4c2-011b223e87b9'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='7dbb40ab-98c2-46b0-8d8e-34b43bb6c428'></a>

Wodarz and Hamer

<a id='5a798c12-828f-4ccc-b9a3-3a91e8afe125'></a>

Page 3

<a id='06bc49a9-8dfb-4f51-9687-20473772ae85'></a>

dy/dt = ryv (1 - y/k) - ay
dv/dt = ηy - uv
(1)

<a id='0c411e4f-627c-413b-b80b-342c5179a56c'></a>

The infected HIV-specific CD4 T cells are denoted by y, and free virus particles are denoted by v. The CD4 T cells are assumed to proliferate at a rate proportional to the amount of virus recognized (ryv). This proliferation is density dependent, limited by the so called carrying capacity, k. This means that as the number of infected CD4 T cells increases, the proliferation rate slows down. This is because we assume that the number of specific CD4 T cells cannot grow beyond a level given by k, determined by homeostatic mechanisms. Density dependence is modeled in a phenomenological way, and this could also be modeled with other mathematical expressions. Numerical simulations, however, indicate that the results discussed here do not depend on the exact mathematical formulation of density dependence. The infected CD4 T cells die at a rate ay. The infected cells produce free virus at a rate ny and free virus decays at a rate uv. For now, we do not include spread of these virus particles to uninfected cells because we ask under which circumstances autocatalyitc growth alone can drive virus spread.

<a id='af1f27bc-6847-4dd2-941c-cda9af8da2c6'></a>

The model is characterized by two outcomes: (EQ1) The infected CD4 T cells fail to expand where y=v=0. (EQ2) The infected CD4 T cells do expand and grow towards an equilibrium

which is described by y = (r'k + √(r'^2 k^2 - 4r'ak)) / (2r') and v=ηy/u, where r'=ηrη/u. The stability properties have been determined by standard techniques and are described as follows. Outcome EQ1 describing failure to expand is always stable. If the basic rate of T cell proliferation lies above a threshold such that r'> 4a/k, the outcome describing T cell expansion is also stable. Thus, if this condition is fulfilled, both outcomes are possible. Which outcome is observed depends on the initial conditions. If the initial abundance of the infected CD4 T cells lies above a threshold, the CD4 T cells expand. If the initial abundance of infected CD4 T cells lies below a threshold, the T cells fail to expand. This threshold

<a id='24d13648-5b05-4f5c-a368-dfcc65ee46ce'></a>

abundance of infected CD4 T cells is given by $y_{thr} = \frac{r'k - \sqrt{r'^2k^2 - 4r'ak}}{2r'}$. The reason for this dependence on the initial number of T cells is that the cells need to receive sufficient antigenic stimulation so that the rate of proliferation is greater than the death rate. This can only be achieved if the number of infected T cells lies above a threshold. Therefore, autocatalytic virus growth via antigen-induced division of infected T cells is inefficient at low virus loads, but can contribute significantly to virus spread at higher virus loads.

<a id='9a511963-c1ab-425e-ad98-6787fcb14834'></a>

### 3. Infectious and autocatalytic virus spread in T cells
In the previous section, we examined virus spread by the division of HIV-specific CD4 T cells. We ignored virus transmission to susceptible and uninfected HIV-specific CD4 T cells. We now expand the model to include this. We assume that uninfected CD4 T cells proliferate in response to antigenic stimulation at a rate rx, die at a rate dx, and become infected at a rate βxv. The rate of infection is thus proportional to the amount of virus present. Note that the proliferation rate of the T cells is density dependent and slows down

<a id='006cc849-c92b-4b65-8432-1f9f23d67fac'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='961f4902-1916-4372-9109-5efe92893c51'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='8ef88f14-ec3a-4811-8915-cd0671297107'></a>

Wodarz and Hamer

<a id='2b33d65b-63f2-4ca6-96d1-bf341044068a'></a>

Page 4

<a id='55174e43-78cc-4e99-a099-ff69a8f0a252'></a>

as the total number of T cells (infected + uninfected) reaches a homeostatic set-point described by the parameter k. Virus is produced from infected cells at a rate η and decays at a rate u. The model is based on previous work which investigated virus spread via the mitotic division of T cells [9,10] and is given by the following set of differential equations.

<a id='3bd0b127-ca8f-4ef8-bf8a-0f849822b421'></a>

dx/dt = rxv (1 - (x+y)/k) - dx - βxv
dy/dt = βxv + ryv (1 - (x+y)/k) - ay (2)
dv/dt = ηy - uv

<a id='fa96f100-70b7-451f-9cfe-4a9219f8d7a7'></a>

The dynamics may converge to two different stable equilibria. (i) The CD4 T cell response, and thus virus replication in specific T cells, does not become established. That is, x=y=v=0. (ii) The response and thus the infection does become established. We do not, however, observe the presence of uninfected CD4 T cells. The entire population of HIV-specific CD4 T cells carries the virus. This is described the by the following equilibrium expressions. x=0;

<a id='a9fc71c5-3d83-4274-8e60-09414141745d'></a>

y = r'k + √(r'^2 k^2 - 4r'ak) / 2r'
Note, that the system is characterized by a third equilibrium that describes the coexistence of infected and uninfected cells. The equilibrium, however, is always unstable.

<a id='06449857-dcee-4ad2-ab75-a05a00243ada'></a>

Which outcomes are observed depends both on the parameters of the model and the initial conditions (Figure 1). The stability properties of the equilibria are as follows. The outcome describing the absence of the response and the failure of infection in HIV-specific CD4 T cells is always stable. The equilibrium describing the establishment of infection is stable if r'

<a id='6244dfd2-02ed-4886-9f53-8a1e672d2aba'></a>

> 4a/k and β > 2r'(a-d) / r'k √(r'2k2 – 4r'ak. In words, the division rate of the CD4 T cells, as well as the rate of infection need to lie above a threshold. Therefore, if these two conditions are fulfilled, the dynamics may result in either failure of infection, or the establishment of infection in specific T cells. Which outcome is achieved depends on the initial conditions (Figure 1). Establishment of infection is promoted by a high initial number of uninfected CD4 T cells, as well as a high initial number of infected CD4 T cells.

<a id='db1a1ccf-5e56-4263-b34f-622dfebb5595'></a>

A high initial number of infected T cells provides high degrees of antigenic stimulation for expansion. A high initial number of uninfected T cells provides targets for the virus which accelerates virus growth and the generation of antigenic drive. If, on the other hand, the initial number of infected T cells is low, and there are only few susceptible T cells to infect, then the initial level of antigenic stimulation is not sufficient for the response and the infection to be initiated.

<a id='90775797-4bfe-464a-95a1-5bb7bffd7e94'></a>

These requirements for establishment of infection are different from those derived from the
basic reproductive ratio of the virus, R₀, in standard virus dynamics models. This quantity
denotes the number of newly infected cells that arise from any one infected cell when almost
all cells are uninfected [11]. If R₀ < 1, then one infected cell gives rise on average to less
than one newly infected cell and the virus population cannot spread. If R₀ > 1, then one
infected cell gives rise on average to more than one newly infected cell and the virus

<a id='9b1b3742-2c1d-455e-9ed1-3cdc96d89dfa'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='9978c7b2-4dfc-4e53-a15b-4290b7461792'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='f2b83e49-d781-44c4-98c0-a9053f27152a'></a>

Wodarz and Hamer

<a id='6dc07a44-8492-4793-a01d-579bbdfee2b5'></a>

Page 5

<a id='26f8f01b-187e-49f2-95b5-4b23462e4cb4'></a>

population grows. The basic reproductive ratio of the virus cannot be clearly defined in the model describing virus replication in HIV-specific T cells because initial virus growth depends on the initial amounts of antigenic stimulation.

<a id='4d33cb80-9363-4ed8-92ce-782d4f62fea8'></a>

As noted above, if virus replication in HIV-specific CD4 T cells is established, the model suggests that all CD4 T cells are infected with HIV (100% prevalence). The reason is that both susceptible and infected T cells proliferate, but that infectious spread of the virus reduces the number of susceptible T cells, and increases the number of infected T cells. Data suggest that uninfected T cells may coexist with infected cells. This can be caused by additional factors which are discussed below, such as the existence of target cells which do not specifically react to HIV, or the presence of immune effector responses. This result does, however, highlight the ability of HIV to quickly impair T cell responses against itself via the infection of its own specificities.

<a id='8eeafb1f-7c8b-41e7-8c81-8b4b07f0934e'></a>

## 4. Virus replication in HIV-specific and non-specific cells
Here, we include the specific T cell infection model into a larger mathematical framework which takes into account virus replication in cells which do not react against HIV. These are T cells which are not specific to HIV, or antigen presenting cells such as macrophages and dendritic cells. We will refer to them as non-specific target cells.

<a id='c5392fba-6540-45d6-aebc-4e1cde4883a9'></a>

We denote susceptible non-specific target cells as T, and infected non-specific target cells as I. As before we denote susceptible HIV-specific CD4 T cells as x, infected specific T cells as y, and free virus as v. We assume that susceptible non-specific target cells are produced at a constant rate λ, die at a rate δ, and become infected by virus at a rate γ. Infected non-specific cells die at a rate α. The dynamics of virus infection in HIV-specific T cells remains the same as in the last section. Finally, free virus is produced by both types of infected cells (specific and non-specific) at a rate η and decays at a rate υ. The model is given by the following set of differential equations.

<a id='b7386186-30cd-47c7-8749-6a33c95453c2'></a>

<::transcription of the content
dT/dt = \lambda - \delta T - \gamma Tv
dI/dt = \gamma Tv - \alpha I
dx/dt = rxv (1 - (x+y)/k) - dx - \beta xv (3)
dy/dt = \beta xv + ryv (1 - (x+y)/k) - ay
dv/dt = \eta(y+I) - uv
: equations::>

<a id='7135ba60-63b3-4151-ae1d-bbb8a54b1d9e'></a>

A similar model was published by [8] in the context of studying the strength of the CD4 cell
response in relation to the clonality of the immune response and the ability of the immune
system to control HIV. This model, however, did not take into account autocatalytic virus
spread of HIV, and thus did not separately consider populations of infected HIV-specific T
cells and infected alternative target cells.

<a id='f9adc134-ee05-4f3f-b2bd-8526d422f2e4'></a>

Due to its complexity, this model was studied mostly by numerical simulations. In contrast to specific T cell infection, establishment of viral replication in non-specific target cells does not depend on the initial conditions and occurs if the basic reproductive ratio of the virus, R₀, is greater than one. The basic reproductive ratio in the non-specific target cells is given

<a id='cc3cccda-de0c-4721-8fe8-96133ec6a3f4'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='74cc69f8-93fa-4120-8859-9cb1997ef5bf'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='938fe005-3f7b-4ed4-ae36-e3571e341eb8'></a>

Wodarz and Hamer

<a id='3a59dc39-6174-43cd-9ce2-77bfd48e3d13'></a>

Page 6

<a id='dda7c4b5-78a6-47db-8bb6-fe7f2d28ebd3'></a>

by R₀ = γηλ/δau. If the virus can establish infection in the population of non-specific target cells, we can observe three different outcomes regarding the dynamics of the specific CD4 T cells. (i) If virus load in the non-specific target cells lies below a threshold and is not sufficient to trigger a CD4 T cell response, the dynamics of the specific CD4 T cell response behave in the same way as those in the model which only includes the population of specific CD4 T cells studied in the previous section. This scenario will not be considered further. (ii) Virus load in the non-specific target cells is sufficiently high to trigger CD4 cell expansion, and we observe the coexistence between susceptible and infected HIV-specific CD4 T cells. This occurs if the infection rate of specific T cells lies below a threshold and the rate of virus-induced cell death of specific T cells lies above a threshold. Under these circumstances virus replication in specific T cells is not efficient enough for the virus to achieve 100% prevalence in the specific CD4 cell population. (iii) Virus load in the non-specific target cells is sufficiently high to trigger specific CD4 cell expansion, and we observe 100% prevalence of HIV in the specific T cells (that is all HIV-specific T cells are infected). This is observed if the infection rate of specific T cells lies above a threshold and the rate of virus-induced death of specific T cells lies below a threshold. Now, virus replication in specific CD4 T cells is efficient enough so that the virus can reach 100% prevalence in this cell population. This is an interesting result in the context of data that indicate preferential infection of HIV-specific CD4 T cells [1], and highlights the efficiency with which HIV infection can result in the impairment of immune responses against itself.

<a id='813322f1-090d-4062-8b68-4dfdafeced6b'></a>

## 5. Initial numbers of specific CD4 T cells and impairment of help

Here we use the above model to explore how the initial number of HIV-specific CD4 T cells can influence initial virus growth and the impairment of CD4 T cell help. We assume that uninfected CD4 T cells can deliver help, but that infection impairs helper function. For now, we consider the number of HIV-specific CD4 T cells as a general measure of immunity, because CD4 T cell are needed to activate effector responses such as antibodies and CTL. In Section 6, CD4 T cell help will be considered specifically in the context of CTL responses against HIV. The effect of the initial number of HIV-specific CD4 T cells on virus growth and the kinetics of functional helper cells is shown in Figure 2. Consider the virus growth kinetics first. The initial rate of virus growth is the same regardless of the number of specific T cells (Figure 2). This is because virus growth is initiated by replication in non-specific target cells. The slope of this initial growth reflects the intrinsic growth rate of the virus in the non-specific T cells and therefore the basic reproductive ratio, R₀. The subsequent growth kinetics depend on the initial number of specific CD4 T cells (Figure 2). The higher the initial number of specific T cells, the faster this phase of virus growth. These growth kinetics have important implications for measuring the basic reproductive ratio of HIV from the virus dynamics during initial stages of the infection [12, 13]. The phase of virus growth which reflects the basic reproductive ratio of the virus might occur only at relatively low virus loads, possibly below the level of detection. As virus load increases, the kinetics of virus growth change and are not described by the standard infection models used to estimate R₀.

<a id='187ecf0d-5d8d-43ea-be01-f0e816815548'></a>

Next, we consider the kinetics of functional helper cells (Figure 2). We distinguish between
two scenarios. First we assume that the virus can spread efficiently enough in specific T

<a id='01ed26f5-e82e-42ad-b460-f293035bbefb'></a>

_Math Biosci._ Author manuscript; available in PMC 2014 June 15.

<a id='2295080b-e2bf-4ef8-aa45-ea54339a9c38'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='8d9e82c8-4f05-47f1-93ab-7000e932f22f'></a>

Wodarz and Hamer

<a id='6170c69b-3b92-4d8f-a464-dcc4cbfa05ab'></a>

Page 7

<a id='cce04b0e-15b0-4440-91c5-fece938e7339'></a>

cells to eventually achieve 100% prevalence. That is, the eventual outcome is complete
impairment of help. We then investigate the more benign scenario where not all HIV-
specific CD4 T cells are infected.

<a id='04f7b620-451d-444e-9a2a-4170402206bc'></a>

i. Assume that the virus can achieve 100% prevalence in the specific helper cell population once the dynamics have reached a steady state. The dynamics before this steady state is reached are as follows. The dynamics of the uninfected specific T cells can strongly depend on the initial number of these cells (Figure 2). Of course, the higher the initial number of specific T cells, the more help is available as the virus enters the host. As the virus starts to grow, however, the uninfected helper cells decline (Figure 2). Interestingly, the higher the initial number of specific T cells, the faster the decline of functional helpers. On the other hand, if we start with a lower initial number of specific T cells, a higher number of functional helpers remains present for a longer period of time (Figure 2). If we start from a sufficiently low initial number of T cells, we can even observe a significant temporary increase in the number of functional helpers before they decline and the infection achieves 100% prevalence (Figure 2). In summary, while at the time of infection, a higher initial number of specific T cells provides more help, elevated numbers of functional helpers are retained for longer if the initial number of specific T cells is lower. This observation does, however, depend on the parameter values. In particular it depends on the parameters that determine the extent to which the virus impairs its specific immune responses, i.e. the parameters that describe the rate of virus spread in the HIV-specific CD4 T cells. Of particular importance is the infection rate of HIV specific T cells, β. As the value of β is reduced, the virus infects the HIV specific T cells less efficiently, and thus the degree of immune impairment is less strong. Therefore, the difference in the timing of HIV-specific CD4 T cell elimination becomes less pronounced. If the value of β is even lower and crosses a threshold, then virus-induced immune impairment is so weak that the specific CD4 T cells do not go extinct, and this is described in section (ii) below. Also, note that the above described observation can disappear if the viral rate of spread in non-specific target cells is very fast compared to the rate of spread in HIV-specific CD4 T cells. In this case, the virus immediately attains high prevalence in the non-specific target cells, and this leads to instant infection and killing of the HIV specific CD4 T cells. This is not likely to be a realistic scenario.

ii. Now, consider the more benign scenario where the virus population cannot achieve 100% prevalence in the specific CD4 T cell population. That is, when steady state is reached, we observe the persistence of uninfected and functional HIV-specific helper cells. If the number of persisting functional helpers is relatively low, the dynamics are similar to the scenario described above. The lower the initial number of specific T cells, the longer the duration during which the number of functional helper cells remains at elevated levels before declining to relatively low numbers. As the infectivity of specific T cells is decreased and the virus-induced death rate of specific T cells is increased, the spread of the virus in the specific T cell population becomes less efficient, and more functional helpers remain at steady state. In this case, the initial number of specific T cells does not significantly alter

<a id='960749d5-dd43-4460-a3b2-e3aeb3463203'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='c5527d3b-9251-4143-a7e4-158f2b56a0c8'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='07be4a67-c7ce-4fd0-873d-aa828c23722e'></a>

Wodarz and Hamer

<a id='0379171d-2764-4e2d-a0e0-899241dff626'></a>

Page 8

<a id='1f96828f-01f0-4f11-9d21-30e893eed00c'></a>

the availability of help. As steady state is reached, the same relatively high number
of functional helpers is maintained. This scenario corresponds to only limited
amounts of virus-induced immune impairment and might not apply to typical HIV
infection.

<a id='01b9579f-64fb-40ee-a574-98ca8bd74185'></a>

# 6. Generation of effector responses
The generation of sustained effector responses can depend on the availability of help [14–16]. This applies both to antibody and to cytotoxic T lymphocyte (CTL) responses. As an example, we consider a CTL response which kills infected cells. CTL dynamics are modeled as follows. We assume that upon antigenic stimulation, naïve CTL undergo a phase of programmed proliferation which results in the differentiation into effector and memory cells [17,18]. We start with a (small) population of naïve specific CTL which have been activated by antigen. They are denoted by m₀. These CTL undergo n rounds of proliferation, and this is independent of antigenic stimulation. Proliferation occurs with a rate 2ρmᵢ, where mᵢ denotes CTL which have undergone i divisions (i=1..n-1). The nᵗʰ division gives rise to effector cells, denoted by w. They can kill infected cells. Effectors die at a rate φw and differentiate into memory cells at a rate ξw. These processes are described by the following set of differential equations (This approach is described in detail by [19,20]):

<a id='46e68ff6-e516-4cc9-ba29-648e98972896'></a>

$$\frac{dw}{dt} = 2\rho m_{n-1} - \xi w - \phi w$$
$$\frac{dm_{n-1}}{dt} = 2\rho m_{n-2} - \rho m_{n-1}$$
$$...$$
$$\frac{dm_1}{dt} = 2\rho m_0 - \rho m_1$$
$$\frac{dm_0}{dt} = -\rho m_0$$ (4)

<a id='1a277c18-28a9-42b2-8c6b-216c436878c2'></a>

Other mathematical models of programmed CTL proliferation have also been considered by
[21,22].

<a id='4995e87c-e5ba-467e-a7e7-a76328427a39'></a>

In accord with experimental data we assume that effectors differentiate into effector memory cells [23], and that in HIV infection central memory cells are not created at normal levels [24]. Instead, the effector memory cells continuously become activated by antigen and give rise to new effectors which again differentiate into effector memory cells. This cycle is continuously repeated during the course of infection. We assume that activation of the memory cells requires not only antigen, but also CD4 T cell help [25-27]. Because not much is known about the CTL proliferation kinetics (involving effector memory and central memory cells) during chronic infection, we take a simplified approach. We can capture the populations of effector and effector memory cells during chronic infection in a single variable, denoted by z. Based on previous models [28], these dynamics are described by the following differential equation:

<a id='f0c47bbe-33e2-4012-9c26-a608fdcc2bc2'></a>

dz/dt = ξw + cx(y+I)z/(εx+1) - bz (5)

<a id='08271abd-204a-48d7-9d6c-240565a7464f'></a>

Effector memory cells are generated during acute infection with a rate §. In addition, they become reactivated, expand and develop effector activity. This requires antigen, derived from both infected HIV specific and alternative cells (y+I), and CD4 T cell help, x. It occurs

<a id='e5ecca3e-7985-476f-a258-66ae0f064c84'></a>

_Math Biosci._ Author manuscript; available in PMC 2014 June 15.

<a id='c2361429-57f2-4232-a230-aa18fda6f205'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='8b358ad7-3bf4-4821-9e06-912bea01d25f'></a>

Wodarz and Hamer

<a id='8ddef41b-057d-4616-af6f-5367deaa96e0'></a>

Page 9

<a id='7ae10710-1246-4e7e-8a78-c67f2dbfe1ad'></a>

with a rate $cx(y+I)z/(\varepsilon x+1)$. The dependence on help saturates at high numbers of helper cells. The CTL die during chronic infection with a rate $bz$. CTL-mediated lysis is described in the model by adding the death terms $-py(z+w)$ and $-pl(z+w)$ to the equation for the respective infected cell dynamics.

<a id='b9953067-652f-4c5a-8fa1-d3c181fb1ab3'></a>

This model was studied by numerical simulations, assuming that the virus can successfully establish an infection. If HIV significantly reduces the number of functional helper cells, or even drives them extinct, we find that the outcome of the CTL dynamics can depend on the initial conditions (Figure 3). The CTL response may either become established and control the infection; or the CTL response is impaired and does not become fully established. Which outcome is attained can crucially depend on the initial number of specific helper cells. We distinguish between two scenarios. (i) Assume that CTL effectors are generated with a fast rate when the virus infects the host (Figure 3i). In the model this corresponds to a high value of p. This is unlikely to apply to a naïve host. It may correspond to the existence of CTL memory, for example induced by boosting CD8 T cell responses. In this case, establishment of a CTL response is promoted by a higher initial number of specific helper cells (Figure 3i). This is because at the time of infection, a higher initial number of specific helper cells results in more availability of help for the CTL. (ii) Next assume that there is a certain delay in the induction of the CTL effectors (Figure 3ii). This is likely to apply to naïve hosts because the process of antigenic stimulation, programmed proliferation, and migration of the cells to the site of infection takes time (low value of p). Now, we find the opposite result. A lower initial number of specific helper cells promotes the establishment of a sustained CTL response (Figure 3ii). This is because with a lower initial number of specific helper cells, elevated numbers of functional helpers remain present for a longer period of time before declining to low levels or extinction. Since we assume a naïve host which needs time to activate CTL and to mount a response, the prolonged availability of help is crucial for the maintenance of the response once it has been induced. Note that this effect also depends on viral parameters, in particular those that determine the degree of virus-induced immune impairment. These are parameters that describe the rate of viral spread in HIV-specific T cells, such as the rate of infection or the life-span of infected specific T cells. For example, if the infection rate of HIV-specific CD4 T cells, ß, is reduced, the difference in the timing of T cell decline gets smaller. In other words, the difference in outcome between low and high initial numbers of specific CD4 T cells becomes less pronounced. If the infection rate of specific CD4 T cells falls below a threshold, then the specific CD4 T cell population does not go extinct anymore. This corresponds to minimal immune impairment, a scenario that is not typical of HIV infection. In this case, the initial number of specific CD4 T cells has no effect in the outcome of the dynamics.

<a id='5d46a6e1-b764-4f19-a675-b8c1f572cfe2'></a>

Therefore, the dependency of the dynamics on the initial number of specific helper cells can be complex and can depend on the viral replication kinetics and on the exact CTL kinetics. If the CTL give rise to effectors immediately upon infection, boosting the specific CD4 T cells is beneficial for the host. This may occur if in addition to the helper cell response, the CD8 cell response has also been boosted by vaccination. Whether CD8 cell vaccination can lead to this outcome may, however, also depend on the details of the vaccination [29]. If vaccination maintains active effector responses by providing continuous antigenic

<a id='e63e7421-fdc6-4664-947c-b4f7b7f74850'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='b7efde19-ebe4-47ae-b63c-48a304c64ae2'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='5b515d41-3218-4f25-a2ce-5089c7d63679'></a>

Wodarz and Hamer

<a id='4793fe19-a316-4cdd-9a8b-1f5eb3fdd116'></a>

Page 10

<a id='296cb648-07b9-441e-b930-e9e79f0ea4c9'></a>

stimulation, this argument would certainly apply. If, on the other hand, vaccination just boosts the number of resting memory CTL, effectors might not be generated sufficiently fast for this argument to apply. If there is a significant delay between the time of infection and the generation of CTL effectors, boosting the specific CD4 T cells is beneficial for the virus and can potentially accelerate disease progression. This may correspond to the scenario where only helper cells, but not CD8 T cells have been boosted by vaccination; or if the boosted CTL response persists in the form of resting CTL which require a certain amount of time to differentiate into effectors. It has been documented that specific vaccination approaches which increased the number of SIV-specific CD4 T cells can accelerate disease progression rather than prolong or prevent it [30].

<a id='506df40a-7560-4ce2-8bd8-4500cc174298'></a>

## 7. Specific CD4 T cell dynamics during drug therapy

Here we investigate the dynamics of the HIV-specific T cells during a phase of drug therapy. Antiviral drugs essentially block viral replication. In terms of the model, this can be expressed as a reduction in the parameters y and β; in words [31], a reduction in the infectivity of non-specific target cells and specific T cells. As expected, drug therapy in the model results in a reduction of virus load in the non-specific target cells (Figure 4). The dynamics of virus replication during drug therapy in the specific T cell population is more complicated. This is because the virus can also spread by antigen-driven division of infected T cells, and this is not inhibited by drug therapy. We distinguish between two scenarios. In the first case, we assume that before therapy, the virus is 100% prevalent in the specific T cell population. Then we consider the case where both infected and uninfected specific T cells co-exist before the start of treatment.

<a id='be4b0344-3506-467d-8d3a-f08f696c3401'></a>

Consider the scenario where the virus has attained 100% prevalence in the specific T cell
population before the start of treatment. We further assume that during drug therapy, new
susceptible specific T cells are not produced. In this case, the population of infected specific
T cells can keep cycling during drug therapy and can be maintained at a steady state (Figure
4). This steady state may be small and below the level of detection. Thus, while drug
treatment can significantly reduce virus load, continued antigen-driven proliferation of
infected T cells can provide a reservoir of mitotic virus spread which is not affected by
therapy and which hinders further elimination of the infection (Figure 4). This is a separate
and additional barrier to treatment from latently infected cells which are known to persist
during therapy [32].

<a id='4a43b31c-dc39-49de-9bc9-fe11fc85b029'></a>

Now, assume that the virus has not attained 100% prevalence in the specific T cell
population, and that uninfected specific T cells are observed before the start of treatment.
That is, virus spread is slower than above, and virus-induced helper cell impairment is
weaker. In this case, the dynamics of specific T cells are different. Therapy reduces the
infection rate of susceptible T cells and thus the degree of impairment. Consequently,
functional (uninfected) CD4 T helper cells temporarily expand upon treatment, and infected
T cells decline. This is because before the virus has declined to low levels, the T cells
receive antigenic stimulation without being infected at a significant rate. While the infected
T cells also receive antigenic stimulation, they are killed by the virus and therefore decline
relative to the number of uninfected cells. If virus load is reduced to sufficiently low levels

<a id='1e5034b2-b310-429f-87f0-dd518e50806a'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='05425090-e8b6-4696-bc3b-dd0d795a7cd5'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='ae8213c5-b7b4-4ecc-bc17-766df5deea75'></a>

Wodarz and Hamer

<a id='5425d164-9aca-4aea-a703-55050288eaba'></a>

Page 11

<a id='da6eabf2-c18d-46e5-b812-d25b2e02e509'></a>

during therapy, the specific CD4 T cells are expected to eventually vanish during treatment.
On the other hand, if sufficient amounts of antigenic stimulation remains during therapy due
to elevated residual replication in non-specific target cells, this can maintain elevated levels
of specific T cells which are active and divide during treatment. Both infected and
uninfected cells persists. The higher the amount of antigenic stimulation during treatment,
the higher the number of infected relative to uninfected specific cells which persist during
the phase of therapy.

<a id='4858e831-675e-4159-9159-bfa30e36cf43'></a>

## 8. Conclusion

This paper has used mathematical models to show that the ability of HIV to infect and perhaps preferentially infect HIV-specific CD4 T cells has important consequences for the dynamics of the infection. The auto-catalytic spread of infected HIV-specific CD4 T cells contributes significantly to the rate of virus spread at higher virus loads, and also provides an additional reservoir which prevents elimination of infected cells during drug therapy. Because the ability of HIV-specific CD4 T cells to divide is not hindered by anti-viral drugs, the cells can stimulate themselves during therapy, and thus persist at a certain steady state rather than declining. The ability of HIV to infect its specific CD4 T cells also has important implications for vaccination approaches. Especially if CD8 T cells are not boosted at the same time, an elevation of the initial numbers of CD4 T cells can be advantageous for the virus and not for the host, and such vaccination approaches are likely to speed up disease progression rather than to prevent it, as found in a case study with SIV-infected macaques [30]

<a id='e5d37e9d-f787-4e0b-ada5-2b89fc9b1774'></a>

References

<a id='9b2b3f6b-4675-4687-8685-55b37f85ac90'></a>

1. Douek DC, Brenchley JM, Betts MR, Ambrozak DR, Hill BJ, et al. HIV preferentially infects HIV-specific CD4+ T cells. Nature. 2002; 417:95-98. [PubMed: 11986671]
2. Rosenberg ES, Billingsley JM, Caliendo AM, Boswell SL, Sax PE, et al. Vigorous HIV-1-specific CD4+ T cell responses associated with control of viremia [see comments]. Science. 1997; 278:1447-1450. [PubMed: 9367954]
3. Rosenberg ES, Walker BD. HIV type 1-specific helper T cells: a critical host defense. AIDS Res Hum Retroviruses. 1998; 14(Suppl 2):S143-147. [PubMed: 9672231]
4. Rosenberg ES, LaRosa L, Flynn T, Robbins G, Walker BD. Characterization of HIV-1-specific T-helper cells in acute and chronic infection. Immunol Lett. 1999; 66:89-93. [PubMed: 10203039]
5. Wodarz D, Nowak MA. Mathematical models of HIV pathogenesis and treatment. Bioessays. 2002; 24:1178-1187. [PubMed: 12447982]
6. Perelson AS. Modelling viral and immune system dynamics. Nature Rev Immunol. 2002; 2:28-36. [PubMed: 11905835]
7. Nowak, MA.; May, RM. Mathematical principles of immunology and virology. Oxford University Press; 2000. Virus dynamics.
8. Korthals Altes H, Ribeiro RM, de Boer RJ. The race between initial T-helper expansion and virus growth upon HIV infection influences polyclonality of the response and viral set-point. Proc Biol Sci. 2003; 270:1349-1358. [PubMed: 12965025]
9. Wodarz D, Bangham CRM. Evolutionary dynamics of HTLV-1. J Mol Evol. 1999 submitted.
10. Wodarz D, Nowak MA, Bangham CRM. The dynamics of HTLV-1 and the CTL response. Immunology Today. 1999; 20:220-227. [PubMed: 10322301]
11. Anderson, RM.; May, RM. Infectious diseases of humans. Oxofrd, England: Oxfors University Press; 1991.

<a id='eb7b823b-6b0e-4f22-829b-76343a7f26ad'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='1f78e2c0-661a-4fd2-94b1-01ced3743f34'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='5da33298-a4a2-447f-8f76-011993b6c14b'></a>

Wodarz and Hamer

<a id='a9da5d64-1150-4811-800a-04e5b0ec4b44'></a>

Page 12

<a id='c2f81441-c45e-4ebb-8a4b-2f75363768fc'></a>

12. Nowak MA, Lloyd AL, Vasquez GM, Wiltrout TA, Wahl LM, et al. Viral dynamics of primary viremia and antiretroviral therapy in simian immunodeficiency virus infection. J Virol. 1997; 71:7518–7525. [PubMed: 9311831]
13. Little SJ, McLean AR, Spina CA, Richman DD, Havlir DV. Viral dynamics of acute HIV-1 infection. J Exp Med. 1999; 190:841–850. [PubMed: 10499922]
14. Kalams SA, Walker BD. The critical need for CD4 help in maintaining effective cytotoxic T lymphocyte responses [comment]. J Exp Med. 1998; 188:2199–2204. [PubMed: 9858506]
15. Kalams SA, Goulder PJ, Shea AK, Jones NG, Trocha AK, et al. Levels of Human Immunodeficiency Virus Type 1-Specific Cytotoxic T- Lymphocyte Effector and Memory Responses Decline after Suppression of Viremia with Highly Active Antiretroviral Therapy. J Virol. 1999; 73:6721–6728. [PubMed: 10400770]
16. Kalams SA, Buchbinder SP, Rosenberg ES, Billingsley JM, Colbert DS, et al. Association between Virus-Specific Cytotoxic T-Lymphocyte and Helper Responses in Human Immunodeficiency Virus Type 1 Infection. J Virol. 1999; 73:6715–6720. [PubMed: 10400769]
17. van Stipdonk MJ, Lemmens EE, Schoenberger SP. Naive CTLs require a single brief period of antigenic stimulation for clonal expansion and differentiation. Nat Immunol. 2001; 2:423–429. [PubMed: 11323696]
18. Kaech SM, Ahmed R. Memory CD8+ T cell differentiation: initial antigen encounter triggers a developmental program in naive cells. Nat Immunol. 2001; 2:415–422. [PubMed: 11323695]
19. Wodarz D, Thomsen AR. Effect of the CTL proliferation program on virus dynamics. Int Immunol. 2005; 17:1269–1276. [PubMed: 16103027]
20. Wodarz D, Thomsen AR. Does programmed CTL proliferation optimize virus control? Trends Immunol. 2005; 26:305–310. [PubMed: 15922946]
21. Antia R, Bergstrom CT, Pilyugin SS, Kaech SM, Ahmed R. Models of CD8+ responses: 1. What is the antigen-independent proliferation program. J Theor Biol. 2003; 221:585–598. [PubMed: 12713942]
22. Antia R, Ganusov VV, Ahmed R. The role of models in understanding CD8+ T-cell memory. Nat Rev Immunol. 2005; 5:101–111. [PubMed: 15662368]
23. Wherry EJ, Teichgraber V, Becker TC, Masopust D, Kaech SM, et al. Lineage relationship and protective immunity of memory CD8 T cell subsets. Nat Immunol. 2003; 4:225–234. [PubMed: 12563257]
24. Sallusto F, Geginat J, Lanzavecchia A. Central memory and effector memory T cell subsets: function, generation, and maintenance. Annu Rev Immunol. 2004; 22:745–763. [PubMed: 15032595]
25. Sun JC, Williams MA, Bevan MJ. CD4+ T cells are required for the maintenance, not programming, of memory CD8+ T cells after acute infection. Nat Immunol. 2004; 5:927–933. [PubMed: 15300249]
26. Sun JC, Bevan MJ. Defective CD8 T cell memory following acute infection without CD4 T cell help. Science. 2003; 300:339–342. [PubMed: 12690202]
27. Shedlock DJ, Shen H. Requirement for CD4 T cell help in generating functional CD8 T cell memory. Science. 2003; 300:337–339. [PubMed: 12690201]
28. Wodarz D, Jansen VA. The role of t cell help for anti-viral ctl responses. J Theor Biol. 2001; 211:419–432. [PubMed: 11476625]
29. Jansen VAA, Korthals Altes H, Funk GA, Wodarz D. Contrasting B cell and T cell based protective vaccines. Journal of Theoretical Biology. 2005 in press.
30. Staprans SI, Barry AP, Silvestri G, Safrit JT, Kozyr N, et al. Enhanced SIV replication and accelerated progression to AIDS in macaques primed to mount a CD4 T cell response to the SIV envelope protein. Proc Natl Acad Sci U S A. 2004; 101:13026–13031. [PubMed: 15326293]
31. Bonhoeffer S, May RM, Shaw GM, Nowak MA. Virus dynamics and drug therapy. Proceedings of the National Academy of Sciences of the United States of America. 1997; 94:6971–6976. [PubMed: 9192676]
32. Chun TW, Stuyver L, Mizell SB, Ehler LA, Mican JA, et al. Presence of an inducible HIV-1 latent reservoir during highly active antiretroviral therapy. Proc Natl Acad Sci U S A. 1997; 94:13193–13197. [PubMed: 9371822]

<a id='1b9bd26c-abf9-414a-84a3-a529621db2fa'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='5d1b308d-42c9-48c3-9b42-8c1e4e3654a8'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='177e5b57-cf62-44ac-a912-cfbc9e5926cf'></a>

Wodarz and Hamer

<a id='4e1b0508-7836-4db0-ab7d-9acab5452abc'></a>

Page 13

<a id='5628b138-5d71-4dae-9d2f-5f483063007f'></a>

<::Figure: Two line graphs showing the number of specific CD4 T cells over time for different initial virus loads. The legend indicates that a solid line represents "Uninfected, functional" cells and a dashed line represents "Infected, impaired" cells.  (i) Low initial virus load: The y-axis represents the Number of specific CD4 T cells, ranging from 0 to 0.12. The x-axis represents Time (arbitrary units), ranging from 0 to 20. The solid line starts around 0.1 and gradually decreases to approximately 0.015 by time 20. The dashed line stays very low, near 0, throughout the period. (ii) High initial virus load: The y-axis represents the Number of specific CD4 T cells, ranging from 0 to 10. The x-axis represents Time (arbitrary units), ranging from 0 to 20. The solid line starts near 0, peaks at approximately 2.5 around time 12.5, and then decreases to near 0 by time 15. The dashed line starts near 0, shows a slow increase, then a rapid increase from time 10 to 14, and then plateaus at 10.::>

<a id='f8f24f8a-b5dc-411a-8c03-f4f61f8f8311'></a>

Figure 1.
Basic dynamics of HIV in specific CD4 T cells. The figure is based on model (2). It shows the outcome of infection depending on the initial conditions. (i) If the initial virus load is low, there is not enough antigenic stimulation to establish a CD4 T cell response. Consequently, infection in the specific CD4 T cell population also goes extinct. (ii) If the initial virus load is high, there is enough antigenic stimulation to establish the CD4 T cell response. Consequently, the infection is also established. The virus spreads through the entire population of HIV-specific CD4 T cells and attains 100% prevalence in this population (that is, all specific T cells are infected). Parameters were chosen as follows. r=1, d=0.1, k=10, β=0.2, a = 0.2, η=1, u=0.5. Initial conditions were as follows: xo=0.1, yo=0; for (i) vo=0.1; for (2) vo=1.

<a id='433f4a65-37f2-4936-aa14-0b674f13e594'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='dc4a48a3-7834-4efd-a196-715df285fc7b'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='5a3fbd18-b22b-450a-ace7-15f2dca2473e'></a>

Wodarz and Hamer

<a id='11c27dd8-f97b-4913-bb44-bc9022ae2657'></a>

Page 14

<a id='4a218e51-3ba9-4fd5-8aa6-dbfbe165e40c'></a>

<::
Solid line: Low initial number of specific CD4 cells
Dotted line: High initial number of specific CD4 cells
: figure::>

<a id='9e1112fe-05f7-4e0a-acc4-305a406ad6c6'></a>

<::Line graph showing Virus load on the y-axis (logarithmic scale) versus an unlabeled x-axis ranging from 0 to 80. The y-axis ranges from 0.0001 to 100. There are two lines plotted: a dashed line and a solid line. The dashed line starts at 0.0001 at x=0, rises sharply to a peak of approximately 50-60 between x=20 and x=25, then gradually declines and stabilizes around 10-15 after x=40. The solid line also starts at 0.0001 at x=0, rises slowly at first, then increases more rapidly from x=30. It crosses the dashed line around x=45-50 (at a virus load of about 10-15) and then stabilizes around 10-15 after x=50.: chart::>

<a id='e83e9d5f-59b9-4a4e-8c99-ab382265695c'></a>

# specific CD4 T cells<::A line graph titled "# specific CD4 T cells" with a logarithmic y-axis ranging from 0.01 to 10 (labeled 0.01, 0.1, 1, 10) and an x-axis labeled "Time (arbitrary units)" ranging from 0 to 80 in increments of 10. The graph shows two lines: a solid line and a dashed line. The solid line starts at y=0.1 at x=0, stays constant until approximately x=20, then rises to a peak around y=2 at x=42, and subsequently drops sharply to y=0.01. The dashed line starts at y=10 at x=0, stays constant until approximately x=12, then drops sharply to y=0.01 around x=17, and remains constant thereafter.: chart::>Time (arbitrary units)

<a id='a62cb80c-aebf-41dd-bb5d-e53afd16f170'></a>

Figure 2.
Virus growth and the impairment of help as a function of the initial number of specific CD4 T cells. The figure is based on model (3) which contains both specific and non-specific target cells. (i) Virus growth: The very first phase of virus growth is the same, regardless of the initial number of specific CD4 T cells. This is because the infection is initiated in the non-specific target cells and it is assumed that specific T cells only become infected after a certain time threshold, because it will take some time for virus to meet the majority of HIV-specific T cells (the virus enters through mucosal surfaces and then makes its way to the blood where the majority of T cells are located). Subsequently, the rate of virus growth depends on the initial number of specific CD4 T cells. The higher the initial number of CD4 T cells, the faster the rate of virus growth. Both time series eventually converge to the same equilibrium. The reason is that this model does not contain any immune effector responses.
(ii) Dynamics of functional specific CD4 T cells. We define this population as uninfected T cells. This assumes that infected T cells are impaired. A high initial number of specific CD4

<a id='b043c563-22c0-4e89-b3b1-8776ed625de1'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='51706b63-29b3-4764-b26c-fe3a82e1a26a'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='0261f241-ba8d-4829-86b9-48a2dc3e2ca3'></a>

Wodarz and Hamer

<a id='eb22e339-fcd2-4223-bd43-de5b76cfcf18'></a>

Page 15

<a id='9a2ca6be-5355-4835-a3fd-1af2d0f1aa28'></a>

T cells results in a fast decline of functional helper cells. If the initial number of specific CD4 T cells is lower, functional helper cells remain at higher levels for a longer period of time. In the simulation shown here, the population of specific CD4 T cells actually expands before declining to low levels. Parameters were chosen as follows. λ=1, r=1, δ=0.01, α=0.2, γ=0.005, β=0.3, d=0.001, a=0.2, k=10, η=1, u=1. Initial conditions were as follows: T₀=λ/d, I₀=0.0001, x₀=0.1 or x₀=10, y₀=0, v₀=ηI₀/u.

<a id='68f6988f-b348-43ba-9730-44b5db90f09d'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='020aa44e-9ad8-4347-bc87-6a2b4d15c6a3'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='05aa8d4e-89ea-4aa9-8efc-1f23c9aab15d'></a>

Wodarz and Hamer

<a id='9cbfec0a-a6ab-469b-97f6-9717fcae3bd6'></a>

Page 16

<a id='05704e32-87dd-45ea-bdc2-bc24b1173a9e'></a>

(i) Fast generation of effectors

<a id='18e57c10-213b-472b-88cb-0e806f3a252a'></a>

(ii) Slow generation of effectors

<a id='8b99c562-1834-443a-b566-57472b882806'></a>

Low initial number of specific CD4 cells<::chart: A line graph with a y-axis ranging from 0 to 50, marked at intervals of 10, and an x-axis ranging from 0 to 300, marked at intervals of 50. The graph displays two peaks. The first peak is prominent, starting near x=0, rising sharply to a value close to 40 on the y-axis, and then dropping sharply back to near 0 by x=20. The second peak is much smaller and wider, starting around x=60, peaking slightly above 0 on the y-axis around x=75, and returning to 0 by x=90.::>High initial number of specific CD4 cells

<a id='cc59cf2f-e672-4f3e-80af-2d2c190ae1b0'></a>

<::A line graph with an x-axis ranging from 0 to 300 and a y-axis ranging from 0 to 30. A thick black line starts near the origin, rises sharply to a peak of approximately 30 at x=25, then decreases and oscillates with decreasing amplitude, eventually stabilizing around y=5 as x approaches 300.
: chart::>

<a id='ee1f037e-9b6b-4431-96ea-355c84579b20'></a>

High initial number of specific CD4 cells<:: Two line charts. The first chart (left) shows a line starting at approximately 42 on the y-axis, then sharply decreasing, followed by damped oscillations around a value slightly above 5. The y-axis ranges from 0 to 50, with major ticks at 10-unit intervals. The x-axis ranges from 0 to 300, with major ticks at 50-unit intervals. The second chart (right) shows a line starting at 0 on the y-axis, rising sharply to a peak of approximately 30 at x=~40, and then sharply decreasing back to 0 and remaining flat. The y-axis ranges from 0 to 30, with major ticks at 5-unit intervals. The x-axis ranges from 0 to 300, with major ticks at 50-unit intervals. X-axis label for both charts: Time (arbitrary units).: chart::>

<a id='74bd8294-4b85-45c8-83eb-25474d185076'></a>

Figure 3.
CTL dynamics as a function of the initial number of specific CD4 T cells. The figure is based on models (4,5). We distinguish between two scenarios. (i) Effectors are generated at a relatively fast rate. In this case, a high initial number of specific CD4 T cells is beneficial for the immune response. (ii) Effectors are generated with a slower rate. In this case, a low initial number of specific CD4 T cells is beneficial for immunity. Parameters were chosen as follows. (i) λ=1, r=1, δ=0.01, α=0.2, γ=0.01, β=0.3, d=0.001, a=0.2, p=45, c=1, b=0.1, k=10, η=1, u=1, φ=1.5, ξ=0.01, ε=1, n=10. For (i) ρ=1 and for (ii) ρ=0.3. Initial conditions were as follows: T₀=λ/d, I₀=0.0001, x₀=0.1 or x₀=10, y₀=0, v₀=ηI₀/u, m₀=0.1, mi₀=0, w₀=0, z₀=0.

<a id='3055e6b6-41bd-4414-b57e-4586ec8165e7'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='e75a95da-6039-4952-9012-18c71d3bb5af'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<a id='31c76258-76fe-4664-a3d0-73381b651e51'></a>

Number of CTL

<!-- PAGE BREAK -->

<a id='7ef4d5c4-0359-4eed-927f-5828e09c1a43'></a>

Wodarz and Hamer

<a id='fc529549-459e-4eb3-bb79-d0b33e201569'></a>

Page 17

<a id='861ec780-b13f-44ae-9987-9d752890cf71'></a>

<::chart: A line graph with "Total virus load" on the Y-axis and an unlabeled X-axis. The Y-axis is on a logarithmic scale, showing values 0.1, 1, 10, 100, and 1000. The X-axis shows values 200, 250, 300, 350, 400, 450, and 500. A thick black line is plotted, starting at a high value (approximately 500) from X=200 to X=300. From X=300, the line sharply decreases to a low value (approximately 0.7-0.8) by X=330, and then remains constant at this low value until X=500. The background from X=300 to X=500 is shaded gray.
::>

<a id='9bff8cfe-3f3b-428b-b288-197058556b6a'></a>

<::Graph showing the Number of non-specific infected T cells on the y-axis (logarithmic scale) against an unlabeled x-axis. The y-axis ranges from 10^-10 to 10^4, with major ticks at 10^4, 100, 1, 0.01, 0.0001, 10^-6, 10^-8, and 10^-10. The x-axis ranges from 200 to 500, with major ticks at 200, 250, 300, 350, 400, 450, and 500. A black line represents the data: it is horizontal at y=100 from x=200 to x=300, and then slopes downwards from (x=300, y=100) to approximately (x=395, y=10^-10). A light gray shaded area covers the region from x=300 to x=500 across the full y-axis range.: chart::>

<a id='a6780db5-125f-4772-a492-6d6c98f7b196'></a>

<::line graph::>The line graph shows the 'Number of specific infected T cells' on the y-axis and 'Time (arbitrary units)' on the x-axis. The y-axis ranges from 0.5 to 1, with major ticks at 0.5, 0.6, 0.7, 0.8, 0.9, and 1. The x-axis ranges from 200 to 500, with major ticks at 200, 250, 300, 350, 400, 450, and 500. The line starts at a value of 1 on the y-axis and remains constant until approximately x=300. From x=300 to around x=330, the line sharply decreases to a value of approximately 0.72. After this drop, the line remains constant at about 0.72 until x=500. A gray shaded region covers the area from approximately x=300 to x=500.<::>

<a id='b5ec3a81-3c79-4ada-bb96-f55cd49ecb14'></a>

**Figure 4.**
Virus dynamics during drug therapy. Phase of drug therapy is indicated by shading. This figure is based on model (3), and does not include immune effectors for simplicity. We make the extreme assumption that there are no latently infected cells and that therapy can eradicate HIV from the non-specific target cells. We do this in order to demonstrate that the auto-catalytic virus spread via antigen driven division of specific CD4 T cells can present a separate reservoir which can prevent eradication of HIV from the host. Upon treatment, virus load is significantly reduced in the simulation, but settles at a persistent equilibrium. This happens, although the number of infected non-specific target cells is eradicated, and no

<a id='77f4da09-8a38-4bdb-9687-6ffaaf7605c3'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='a56a3ba8-cac9-4462-be70-1b049f72fcc2'></a>

NIH-PA Author ManuscriptNIH-PA Author ManuscriptNIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='6e993a14-b42d-44b9-8a83-2657f2e3f01b'></a>

Wodarz and Hamer

<a id='8d13fc53-e230-4a99-be7d-335656512c48'></a>

Page 18

<a id='6917aedf-b637-446b-a316-6f8d956fa9e2'></a>

latency is assumed. The key lies in the dynamics of the infected specific CD4 T cells. Because drug therapy reduces infectious spread of HIV, the amount of antigenic stimulation is reduced. Consequently, the number of infected specific helper cells declines. However, this population of infected specific helper cells provides enough antigenic stimulation itself to keep these cells dividing. Because drug therapy does not inhibit the mitotic spread of the infection, the virus persists. Parameters were chosen as follows. λ=100, r=1.5, δ=0.01, α=0.3, γ=0.01, β=0.3, d=0.01, a=0.3, k=1, η=1, u=1. During treatment, γ=β=0. Regarding initial conditions upon start of therapy, the system was run until all populations equilibrated, and then treatment was initiated in the model.

<a id='174520f2-fe98-4d1f-9989-302ffd8f1a81'></a>

Math Biosci. Author manuscript; available in PMC 2014 June 15.

<a id='534dfa0a-d16b-4d19-87ca-09f4ba1bc8e1'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript
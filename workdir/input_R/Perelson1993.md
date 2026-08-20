<a id='1f6c72d5-5420-47ce-ab2c-59020cf39aa5'></a>

**Dynamics of HIV Infection of CD4+ T cells**

ALAN S. PERELSON
*Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico*

<a id='d80cf9cd-bd18-4596-b3ef-001b974cf12c'></a>

**DENISE E. KIRSCHNER**
*Department of Mathematics, Vanderbilt University, Nashville, Tennessee*

<a id='995ab890-383e-4c65-aa00-86260ad5a561'></a>

AND
**ROB DE BOER***
*Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico*
*Received 22 January 1992; revised 21 July 1992*

<a id='45d1957e-4a25-4bd2-ac55-dc72595767d0'></a>

ABSTRACT

We examine a model for the interaction of HIV with CD4+ T cells that considers four populations: uninfected T cells, latently infected T cells, actively infected T cells, and free virus. Using this model we show that many of the puzzling quantitative features of HIV infection can be explained simply. We also consider effects of AZT on viral growth and T-cell population dynamics.

<a id='6176516d-cf9b-4c4b-99dd-e5bc85859159'></a>

The model exhibits two steady states, an uninfected state in which no virus is present and an endemically infected state, in which virus and infected T cells are present. We show that if N, the number of infectious virions produced per actively infected T cell, is less a critical value, N_{crit}, then the uninfected state is the only steady state in the nonnegative orthant, and this state is stable. For N > N_{crit}, the uninfected state is unstable, and the endemically infected state can be either stable, or unstable and surrounded by a stable limit cycle. Using numerical bifurcation techniques we map out the parameter regimes of these various behaviors. Oscillatory behavior seems to lie outside the region of biologically realistic parameter values. When the endemically infected state is stable, it is characterized by a reduced number of T cells compared with the uninfected state. Thus T-cell depletion occurs through the establishment of a new steady state. The dynamics of the establishment of this new steady state are examined both numerically and via the quasi-steady-state approximation. We develop approximations for the dynamics at early times in which the free virus rapidly binds to T cells, during an intermediate time scale in which the virus grows exponentially, and a third time scale on which viral growth slows and the endemically infected steady state is approached. Using the quasi-steady-state approx-

<a id='c4a8c134-bdb8-4694-a1b6-b619d30ef9dc'></a>

*Present address: Bioinformatics Group, University of Utrecht, Padualaan 8, 3584 CH Utrecht, The Netherlands.

<a id='458762fd-2e13-437c-ab33-1c08189fb332'></a>

MATHEMATICAL BIOSCIENCES 114:81-125 (1993)

81

©Elsevier Science Publishing Co., Inc., 1993
0025-5564/93/$6.00
655 Avenue of the Americas, New York, NY 10010

<!-- PAGE BREAK -->

<a id='f740c8af-f57d-4aa6-b41a-0904c6def1ec'></a>

82

ALAN S. PERELSON ET AL.

imation the model can be simplified to two ordinary differential equations the
summarize much of the dynamical behavior. We compute the level of T cells in the
endemically infected state and show how that level varies with the parameters in the
model. The model predicts that different viral strains, characterized by generating
differing numbers of infective virions within infected T cells, can cause different
amounts of T-cell depletion and generate depletion at different rates.

<a id='94e627b4-087e-47de-9685-35e17c396e10'></a>

Two versions of the model are studied. In one the source of T cells from precursors is constant, whereas in the other the source of T cells decreases with viral load, mimicking the infection and killing of T-cell precursors. The latter gives more realistic predictions than the model with a constant source.

<a id='da5f200b-36c6-4296-a107-57a74d665729'></a>

## 1. INTRODUCTION

One of the consequences of infection by the human immunodefi-ciency virus (HIV) is the selective depletion of CD4+ T cells, the cells commonly known as helper T cells or T4 cells. Because of the central role of CD4+ T cells in immune regulation, their depletion can have widespread deleterious effects on the functioning of the immune system as a whole. In fact, the decline in the number of CD4+ T cells in peripheral blood and the peripheral blood ratio of CD4+/CD8+ T cells are both used in a clinical setting as indicators of the disease stage [20, 50, 53, 58]. In this paper we present and analyze a simple model for the population dynamics of CD4+ T cells in the presence and absence of HIV. We feel it is important that any model that purports to quantita-tively characterize the effects of HIV infection be able to make realistic predictions about the status of the immune system in the absence of HIV infection. To focus the model on the effects of HIV on T-cell population dynamics, we do not deal with the dynamics of the immune response to HIV. Such a response is generally present, and one could assume that there is a constant level of immune defense that influences parameters in the model. Here we are interested in the question of whether HIV infection by itself can account for T-cell depletion in seropositive patients, and hence we not pursue the potential effects of immune defenses.

<a id='c36c9093-2f75-46c4-be14-0e3c27992547'></a>

Over the past decade, a number of models have been developed to describe the immune system and its interaction with HIV. Both stochastic and deterministic models have been developed. Stochastic models, such as the ones presented by Merrill [42, 43], can be used to account for the early events in the disease when there are few infected cells and a small number of viruses, or in situations where the variability among individuals is of interest. The model of Nowak and coworkers [47, 48] looks at the effects of variability among viral strains. Deterministic models, such as the ones developed by Cooper [7], Intrator et al. [30], McLean [38], McLean and Kirkwood [39], Reibnegger et al. [54], Doležal

<!-- PAGE BREAK -->

<a id='39eee997-97e9-4d7c-991b-8198c1f1e780'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='01e4e267-a6f1-4398-9420-96b69fdc577a'></a>

83

<a id='375d2328-c7b8-4167-a837-5e43f260515e'></a>

and Hraba [10, 28], Hraba et al. [29], Fletcher et al. [16], Anderson and May [4], and Perelson [49], examine the changes in mean cell numbers and are more applicable to later stages of the process in which population sizes are large. These models typically consider the dynamics of the CD4+ helper and virus populations. In some of these models, other immune system populations such as B cells or CD8+ cells have been included.

<a id='14529278-2004-465c-83f0-5ab229a1f17e'></a>

The model explored here is aimed at explaining a number of quanti-tative features of HIV infection that are unusual and, in the absence of a model, perplexing. As we shall show, our basic model can account for the long latency between infection and the onset of clinical AIDS as well as the low concentration of free virus observed in the blood. The model exhibits substantial CD4+ T-cell depletion but in its current form is unable to obtain the very low CD4+ cell counts seen during the late stages of the disease, particularly if the frequency of latently infected CD4+ T cells is kept at realistically low levels and the long latency period is maintained. The depletion of CD4+ cells has been particularly puzzling, since only 1 in 104-105 cells in the peripheral blood of infected HIV individuals expresses viral proteins or mRNA [14, 24] and only 1 in 102-103 T cells harbors viral DNA [55, 56]. In view of the natural turnover of CD4+ T cells in the body, it would seem that the T-cell pool should be able to compensate for such a low rate of T-cell infection [14]. Our work partially supports this observation, in that extreme reduction of CD4+ cells occurs only in the version, of our model with a constant source of T cells if the population of latently infected cells is larger than that observed. Realistic population levels of latently and actively infected cells, as well as long latency and low blood viremia, are obtained in a second version of the model in which T-cell precursors can be infected, thus reducing the supply of new T cells to the periphery. Thus the natural turnover and replenishment of T cells may be important processes in determining the CD4+ T cell count in AIDS patients.

<a id='912b5dc8-e5a2-43b3-b68d-797b953d4b55'></a>

The model developed here is not meant to be a comprehensive model of HIV's interaction with the immune system. It is aimed at examining the kinetics and degree of T-cell depletion that can be caused by viral cytopathicity and thus does not deal with the immune response to HIV. However, there have been a number of observations of viral strains that appear not to induce an effective immune response; these strains have been called escape mutants. Such strains are observed to be of the slow/low type [2]; that is, they replicate slowly and have low expression in CD4$^{+}$ T cells. Genrally, virus isolated during the latent period is of the slow/low type, while rapid/high strains are characteristically isolated during the period of active AIDS. Rapid/high

<!-- PAGE BREAK -->

<a id='c004350f-32c4-41f6-8279-af635e86e4ce'></a>

84

<a id='aec36607-de54-4bd0-b6d8-39c18f08a5bc'></a>

ALAN S. PERELSON ET AL.

<a id='3977bda1-6d95-4713-a916-52d365c7862d'></a>

strains have also been isolated during a period of initial HIV viremia,
which often follows infection [60]. It has been suggested that the
anti-HIV immune response that seems to occur during or following the
initial viremia is able to suppress rapid/high strains, whereas the
slow/low strains are able to avoid the immune response.

<a id='2a22efe5-efec-414d-af73-e2a5b3985088'></a>

Nelson and Perelson [46] presented a model that shows how some viral variants may be able to escape generating an effective immune response. In that model, consistent with observations, the escape mutants are of the slow/low type. The model presented in this paper deals with viral strains that, though not identical in their activity to the escape mutants considered in [46], still have the property of slow replication in CD4+ T cells. Thus, our model, which ignores an immune response, may in fact be relevant to the population dynamics of slow/low escape mutants. We also use our model to show that if slow/low strains are replaced by rapid/high strains in end-stage disease, then significant T-cell depletion, approaching that seen in patients, can be obtained in the model.

<a id='859d1b18-53d0-450c-9c10-87d8743ffb3e'></a>

## 2. MODEL
To generate a realistic model of T-cell infection by HIV, we first need to consider the population dynamics of T cells in the absence of HIV. T cells, like other lymphocytes, are produced in the bone marrow. Immature cells migrate to the thymus, where they undergo further differentiation and maturation into immunocompetent T cells. The thymus is subject to involution, a decrease in weight and volume associated with microscopic evidence of degeneration. In humans, the thymus reaches its greatest weight at about the time of puberty and then begins to gradually involute [61]. Removal of the thymus from an adult usually has minimal effects, although the adult thymus is functional and some of its lymphocytes serve as T-cell precursors and immunocompetent T cells [12]. Within healthy individuals the number of T cells in the blood is maintained relatively constant, with CD4+ T cells comprising about 1000 cells/mm³ [34]. The model discussed here focuses on CD4+ T cells. Thus we shall use the term T cell to mean CD4+ T cell throughout the remainder of this paper.

<a id='51d8f949-e607-4e2f-93a2-66859bce8c0e'></a>

2.1. _T-CELL GROWTH IN AN UNINFECTED INDIVIDUAL_
As a model of T-cell dynamics we propose

<a id='dd93aa16-cc76-4ac8-ba76-432b4a61fd94'></a>

$$\frac{dT}{dt} = s + rT\left(1 - \frac{T}{T_{\text{max}}}\right) - \mu_T T,$$ (1)

<!-- PAGE BREAK -->

<a id='9cee8928-7964-4081-9cbe-d9fd8b913a4d'></a>

85

<a id='667c7b5a-3d03-46e8-a237-096deafd3d30'></a>

HIV INFECTION OF CD4+ T CELLS
85
where _T_ is the number of CD4⁺ T cells, as measured in the blood, say.
The three terms in the equation represent the rates of production and
destruction of T cells, _s_ being the rate of supply of immunocompetent T
cells from precursors in the thymus. T cells, like all cells in the body,
have a finite lifetime. The lifetime may vary among T cells, with
memory T cells thought to have a longer life span than virgin T cells.
Here we do not distinguish between these classes of T cells, and thus μ_T
in Equation (1) represents the average per capita death rate of T cells.
T cells, when stimulated by antigen or mitogen, can divide and increase
in population. We assume that the growth of T cells is governed by a
logistic equation, where _r_ is the average specific T-cell growth rate
obtained in the absence of population limitation. As will be discussed in
more detail in the next section, _r_ depends on the average degree of
antigen or idiotypic network stimulation of T-cell proliferation. How-
ever, even when highly stimulated, the total number of T cells in the
body remains bounded. The term in parentheses shuts off T-cell growth
as the population level _T_max is approached from below.

<a id='1b98a4a0-6da9-4e1f-a96a-1a02249b42be'></a>

Let $T_0$ denote the normal steady-state T-cell population size found
by solving

<a id='e449922d-4ff5-4b7c-ac27-f1624e627799'></a>

$$f(T) = s + rT\left(1 - \frac{T}{T_{\max}}\right) - \mu_T T = 0, \quad (2)$$

<a id='9fdb4642-6553-4312-bce3-953fe4182c27'></a>

that is,

<a id='1ee5f7a3-ec03-40d5-8ee9-449df3954041'></a>

$\text{T}_0 = \frac{\text{T}_{max}}{2\text{r}} \left\{ \text{r} - \mu_{\text{T}} + \left[ (\text{r} - \mu_{\text{T}})^2 + \frac{4\text{sr}}{\text{T}_{max}} \right]^{1/2} \right\}.\quad(3)$

<a id='fa23e1a9-27ca-46ce-af79-6074cdfab1f7'></a>

The other root of Equation (2) is negative, and thus Equation (3)
represents the only physically possible steady state of the system.

<a id='88f58f6a-90eb-4514-80fc-150edfab14a1'></a>

There are certain parameter restrictions that we shall impose to ensure that this model gives realistic population dynamics. Even after thymic involution, the thymus remains functional [12]. Thus we shall assume s > 0. The steady-state population size T₀ should be less than Tmax, so that the T-cell population will expand when stimulated, as occurs, say, during infection. Further, if the population ever reaches Tmax it should decrease. Thus, we choose

<a id='3708e0ed-27f8-4443-b62d-0a1ac3b9c4a6'></a>

μ_T T_max > s,                                                     (4)

<!-- PAGE BREAK -->

<a id='8f2ae278-2cba-4bd3-ae87-8a2e6622f18c'></a>

86

<a id='d91d9960-8c54-4377-962f-ac9ae3850779'></a>

ALAN S. PERELSON ET AL.

<a id='c32b328b-fa2d-4066-87ee-2f1acf98f0fc'></a>

so that the death rate at Tmax is greater than the supply rate. If this were not the case, then the population could increase past Tmax.
Further, Equations (3) and (4) and the condition s>0 imply that T₀ < Tmax as we desire. To see this, note that f(0) = s > 0 and f(Tmax) = s - μT Tmax < 0. Thus, all solutions to Equation (1) that begin with an initial number of T cells, T(0), in the interval I = [0, Tmax] will remain bounded and stay in the open interval 0 < T(t) < Tmax for all t. Because T₀ is the only fixed point in I, T₀ is stable and globally attracting in I.

<a id='112bffd3-9393-4e41-bf7f-57366ae6faa0'></a>

Besides controlling the T-cell population level, Equation (1) has the nice property that the death of T cells can be balanced by the supply of new T cells, the division of T cells in the periphery, or both. Consequently, the net T-cell proliferation rate p = r - µ_T need not be positive. In the absence of environmental antigen and with little idiotypic network stimulation, one might imagine that r is small or even zero and p < 0 but that the total T-cell population is maintained at a positive value through the creation of new T cells. One might also expect that before thymic involution the source s is more important than division in the periphery, so that small or negative values of p could still give positive steady states. After thymic involution, which causes s to decrease, or following adult thymectomy, which causes s to equal zero, one might assume that humoral or growth-factor-regulated control mechanisms ensure that p > 0 so as to give a positive steady-state T-cell population size. Thus, the parameter s and possibly the parameter r may vary with age and antigenic experience. These parameter variations could be important in explaining the observed differences in the dynamics of T-cell depletion due to HIV infection in people of different ages [49].

<a id='5bebab80-f805-4ea2-a49c-d97f6ee0b795'></a>

## 2.2. HIV INFECTION

To model the influence of HIV on T-cell growth, we need to take into consideration a number of features of the life history of the virus [13]. HIV is an RNA virus. However, when it infects a cell, the enzyme reverse transcriptase, which it carries, makes a DNA copy of its RNA genome. This DNA copy is then integrated into the DNA of the infected cell. The viral DNA, called the provirus, is then duplicated with the cell's DNA every time the cell divides. Thus, once infected, a cell remains infected for life. Within a T cell the provirus can remain latent, giving no sign of its presence for months or years [26]. Stimulation of the T cell by antigen or a mitogen can lead to the production of new virus particles that bud from the surface of the infected cell. The budding can take place slowly, sparing the host cell, or it can take place very rapidly, possibly leading to lysis of the T cell [37].

<!-- PAGE BREAK -->

<a id='cfb6b139-98a9-48d8-87a4-c89e63e0082b'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='9a8a0e4e-85d0-4d76-9b96-abf89c99c9c1'></a>

87

<a id='e0fbc862-f1e5-4c83-a202-05dd71de14e5'></a>

To model these events, we consider T cells that are uninfected, T cells that are latently infected (i.e., that contain the provirus but are not producing it), and T cells that are actively infected (i.e., that are producing virus). We also consider the population of free infectious viral particles. To describe the dynamics of these populations we formulate an ordinary differential equation model. Thus spatial dependence is ignored, and the various interactions are imagined to occur in a well-mixed compartment such as the bloodstream. To correctly account for interactions in the tissues, more complex models involving multiple compartments and/or partial differential equations may be needed.
Also, because the model is deterministic, it does not correctly account for the very early stages of the infection nor can it totally account for the variability seen among infected individuals. Some variability can be ascribed to different parameter values being characteristic of different viral strains or different patients.

<a id='5048ec29-7967-48f7-b377-46e86dbc62f2'></a>

Let *T* denote the concentration of uninfected CD4$^+$ T cells, and let *T*** and *T*** denote the concentrations of latently infected and actively infected CD4$^+$ T cells. The concentration of free infectious virus particles is *V*. We will not be concerned with noninfectious viral particles. Definitions of the parameters can be found in Table 1. We assume that the dynamics of the various populations are given by

<a id='8f3858eb-b905-4aed-ab66-1ae0dacae513'></a>

$$\frac{dT}{dt} = s - \mu_T T + rT\left(1 - \frac{T + T^* + T^{**}}{T_{\max}}\right) - k_1 VT, \quad (5a)$$

<a id='1b8c35b7-11af-4c73-9f08-9bd79c6b422c'></a>

$$\frac{dT^*}{dt} = k_1VT - \mu_T T^* - k_2T^* \qquad (5b)$$

<a id='3cc22158-f6a7-45d9-bfb8-9bf2c1041030'></a>

dT** / dt = k2T* - ̲̲bT**, (5c)

<a id='a7ae0a32-e227-46af-8284-b2041e94c749'></a>

$$\frac{dV}{dt} = N\mu_b T^{**} - k_1 VT - \mu_V V. \quad (5d)$$

<a id='13569ca2-dadc-4de8-b110-8ababf3d7c62'></a>

Equation (5a) is a modified form of (1). Again s is a source term and
represents the rate of generation of new (presumably uninfected) CD4+
T cells from precursors in the bone marrow and thymus. HIV can infect
precursor cells and may have the effect of decreasing the supply of new
cells [11]. Thus, in more refined models one may need to consider s as a
decreasing function of v. This case is considered in Section 7, in
Perelson [49], and in a version of the model of Nowak et al. [48].
Uninfected T cells have a finite life span and are assumed to die at the

<!-- PAGE BREAK -->

<a id='5bcf5c53-8ae7-4c1c-82d6-84a5ef7930da'></a>

88

<a id='3c18ceb3-e01d-4adc-b832-6cd407e4e60b'></a>

ALAN S. PERELSON ET AL.

<a id='e9bbbc8d-af20-41f3-a61f-45cb1331528b'></a>

TABLE 1
Variables and Parameters

<a id='30141c74-cf84-4e22-b438-3a098cc8296e'></a>

<table><thead><tr><th>Dependent variables</th><th>Initial or default values</th></tr></thead><tbody><tr><td>T Uninfected CD4<sup>+</sup> cell population size</td><td>1000 mm<sup>-3</sup></td></tr><tr><td>T* Latently infected CD4<sup>+</sup> helper cell population size</td><td>0</td></tr><tr><td>T** Actively infected CD4<sup>+</sup> helper cell population size</td><td>0</td></tr><tr><td>V HIV population size</td><td>10<sup>-3</sup> mm<sup>-3</sup></td></tr></tbody></table>

<a id='ce32b215-db28-4d79-a7bd-ce73d58c72aa'></a>

Parameters and constants

$s$ Rate of supply of CD4$^{+}$ T cells from precursors 10 day$^{-1}$ mm$^{-3}$

$r$ Rate of growth for the CD4$^{+}$ cell population 0.03 day$^{-1}$

$T_{max}$ Maximum CD4$^{+}$ cell population level 1500 mm$^{-3}$

$\mu_T$ Death rate of uninfected and latently infected
CD4$^{+}$ cells 0.02 day$^{-1}$

$\mu_b$ Death rate of actively infected CD4$^{+}$
cell population 0.24 day$^{-1}$

$\mu_V$ Death rate of free virus 2.4 day$^{-1}$

$k_1$ Rate constant for CD4$^{+}$ cells becoming
infected by free virus 2.4$\times$10$^{-5}$ mm$^{3}$ day$^{-1}$

$k_2$ Rate latently infected cells convert to actively
infected 3$\times$10$^{-3}$ day$^{-1}$

$N$ Number of free virus produced by lysing a CD4$^{+}$ cell Varies

$\theta$ Viral concentration needed to decrease $s$ to $s$/2 1 mm$^{-3}$

<a id='ef7ea178-1f0a-4e81-a312-029d9430a1ed'></a>

Derived quantities
<table>
  <tbody>
    <tr>
      <td>_T_<sub>0</sub></td>
      <td>Steady-state level of CD4<sup>+</sup> cells in uninfected<br>individuals</td>
      <td>1000 mm<sup>-3</sup></td>
    </tr>
    <tr>
      <td>_N_<sub>crit</sub></td>
      <td>Critical number of viral progeny needed for<br>endemic infection</td>
      <td>774</td>
    </tr>
    <tr>
      <td>_k_<sub>3</sub></td>
      <td>= _k_<sub>2</sub> + μ<sub>_T_</sub></td>
      <td>0.023 day<sup>-1</sup></td>
    </tr>
    <tr>
      <td>_k_<sub>4</sub></td>
      <td>= _k_<sub>1</sub>_T_<sub>0</sub> + μ<sub>_V_</sub></td>
      <td>2.424 day<sup>-1</sup></td>
    </tr>
    <tr>
      <td>_k_̂<sub>4</sub></td>
      <td>= _k_<sub>1</sub>_T_̄ + μ<sub>_V_</sub></td>
      <td></td>
    </tr>
    <tr>
      <td>γ</td>
      <td>= _r_/_T_<sub>max</sub></td>
      <td>2×10<sup>-5</sup> day<sup>-1</sup></td>
    </tr>
    <tr>
      <td>_p_</td>
      <td>= _r_ - μ<sub>_T_</sub></td>
      <td>0.01 day<sup>-1</sup></td>
    </tr>
  </tbody>
</table>

<a id='c5906037-ee4c-4ac7-8f49-28a135481d18'></a>

same rate per cell, ̗̗̗T, as in uninfected individuals. In Equation (5b),
latently infected T cells are also assumed to have precisely the same
natural life span (~1/̗̗̗T), although other factors can augment the
natural death rate.

<a id='eddaecf7-f788-42af-9605-ddb898e5557f'></a>

If a _T_ cell encounters the antigen for which it is specific, it may be
stimulated to grow. T-cell stimulation is a complex matter. Here we are
dealing with _T_ cells of all specificities, and thus we simply assume that a
constant fraction of _T_ cells are stimulated to grow. In the mouse,

<!-- PAGE BREAK -->

<a id='f822eaf8-d531-40e8-837e-cca5c66b1fac'></a>

89

<a id='7650bcf1-4ae8-4c56-b6bd-140cfa91b92f'></a>

HIV INFECTION OF CD4+ T CELLS 89

Freitas et al. [18] find that about 10% of peripheral T cells are activated large cells. In humans the situation may be different. Analyzing peripheral blood lymphocytes (PBLs) of a healthy individual, one typically finds that on the order of 1% of the cells are activated, using the criterion of IL-2 receptor expression (K. Smith, personal communication). Since many of the PBLs with IL-2 receptors may be natural killer cells, fewer than 1% of CD4+ T cells may be activated. In a more complex model one can make the fraction of cells stimulated, _f_s, a variable in the model and let it be a function of the antigen concentration and possibly other factors such as lymphokines and antigen presentation by macrophages. As the HIV infection progresses, the fraction of cells stimulated may change, so this enhancement may be quite interesting. Here we assume that _f_s is a constant and that the parameter _r_ in Equations (1) and (5a) is given by _r_ = ^_r_ _f_s, where ^_r_ is the average antigen- or idiotypic network-induced per capita T-cell growth rate in the absence of population density limitation.

<a id='cd28c121-eea6-44f5-bde6-81110ede2df2'></a>

The other terms in Equations (5a) and (5b) deal with the effects of HIV. The term k₁VT models the rate at which free virus infects a CD4⁴ T cell. A simple mass-action type of term has been used with rate constant k₁. Once a T cell has been infected, it becomes a latently infected or T* cell; thus k₁VT is subtracted from (5a) and added to (5b).

<a id='b0700993-8989-4c06-b933-bbe047c56fc8'></a>

Equation (5c) models the population dynamics of actively infected T
cells. Actively infected cells are presumed to be generated from latently
infected cells with rate constant k₂. This activation event probably
involves the latently infected cell being stimulated to divide. In vitro, a
variety of stimuli including antigens and mitogens have been shown to
induce HIV expression [17, 41]. Thus k₂, like r, should be a function of
antigen concentration and the fraction of cells stimulated by antigen.
However, it also includes the probability that stimulation leads to viral
production. Active viral replication and budding from these cells is
assumed to lead to lysis at rate μb [37]. Although actively infected cells
may divide once or twice and generate a few daughter cells [37], we feel
that this expansion is sufficiently minor that it can be ignored. The
major factor that needs to be modeled correctly is the total number of
infectious virus particles produced by one infected cell during its life-
time, including any of its daughter cells. We call this quantity N. In this
model we treat both μb and N as parameters characteristic of a
particular viral species. Both parameters, however, may be related to
the viral replication rate. One would expect that viral strains with high
replication rates would have high values of N. However, the lytic rate
μb may also depend on the replication rate—viruses with low replica-
tion rate may kill poorly, if at all, while those with high replication rates
may kill rapidly, say by membrane disruption during viral budding. A

<!-- PAGE BREAK -->

<a id='a5441c9e-9f9a-4f1a-a6dc-4ba3c56f6bf7'></a>

90 ALAN S. PERELSON ET AL.
detailed model of these relationships will be presented elsewhere. Here
we treat _N_, _μb_, and other parameters as constants. If slow/low strains
are replaced by rapid/high variants, then various parameters, such as
_N_, could be slowly varying (see Section 10).

<a id='138360f5-e223-47d7-b06d-b2dc8b7bd1a4'></a>

Equation (5d) models the free infectious virus population. As stated above, we assume that an actively infected CD4+ T cell produces N virus particles. For simplicity, we take the rate of virus production equal to N times the death rate of the cell. For example, this would be the case if the viruses were released upon cell death. Free virus is lost by binding to uninfected CD4+ T cells at rate k₁VT. Binding might also occur to latently infected cells and cause superinfection. Here we neglect this possibility in order to keep the model as simple as possible. Recent measurements using the polymerase chain reaction [55] indicate that in patients with AIDS approximately 1 in 100 cells are latently infected, while in HIV—seropositive patients who are asymptomatic, <1/10,000–1/1000 CD4+ T cells are infected [56]. Thus, neglecting binding to latently infected cells should not introduce much error. Actively infected cells tend to lose their CD4 [27], and hence viral binding to actively infected cells can also be justifiably neglected. The last term in (5d), – µV, accounts for loss of viral infectivity, viral death, and/or clearance from the body.

<a id='f571d1fc-6aff-40ee-b88c-dad3cd277e9b'></a>

In the absence of virus, the T-cell population has the steady-state value T₀. Thus reasonable initial conditions for this system of equations are T(0) = T₀, T*(0) = 0, T**(0) = 0, and V(0) = V₀ for infection by free virus, or T(0) = T₀, T*(0) = T*₀, T**(0) = T**₀, V(0) = V₀ for infection by both infected cells and virus.

<a id='2a3000b0-fd29-445a-870b-43925b51a129'></a>

3. ANALYSIS

We first remark that the model is reasonable in the sense that no population goes negative and no population grows unbounded. The nonnegative orthant $R^4_+$ = {$x \in R^4|x \ge 0$} is called a positively invariant region if a trajectory that starts in the nonnegative orthant remains there forever. What is needed for this is to show that on each hyperplane bounding the nonnegative orthant the vector field points into $R^4_+$. From Equations (5) we find precisely this; that is,

<a id='8b47d752-8464-46b0-9aec-f919c12a3610'></a>

$$\frac{dT}{dt}\Big|_{T=0} = s \ge 0,$$$$\frac{dT^*}{dt}\Big|_{T^*=0} = k_1VT \ge 0,$$$$\frac{dT^{**}}{dt}\Big|_{T^{**}=0} = k_2T^* \ge 0,$$$$\frac{dV}{dt}\Big|_{V=0} = N\mu_b T^{**} \ge 0.$$

<a id='cdc83bca-23ca-4572-bc85-52dcf03a888f'></a>

One of the properties of the logistic equation for T-cell growth, Equation (1), is that if T(0) < Tmax, then T(t) < Tmax for all t. Since the

<!-- PAGE BREAK -->

<a id='d912c815-fef6-4e9d-b56d-c2239a8eb506'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='85f6a34c-e6f7-46e2-850b-7bf703bd9dc6'></a>

91

<a id='938c451a-40eb-40a2-a9ee-865a644e9a78'></a>

presence of HIV only decreases the T-cell population, this property should remain true for $T_{tot} = T + T^* + T^{**}$. To prove this we show that $(dT_{tot}/dt)|_{T_{tot}=T_{max}} < 0$. From Equations (5a)-(5c) we see that

<a id='7e677fae-a3ad-4758-af29-f562e145b2f4'></a>

$$\frac{dT_{tot}}{dt} = \dot{s} - \mu_T T + rT\left(1 - \frac{T_{tot}}{T_{max}}\right) - \mu_T T^* - \mu_b T^{**}.$$

<a id='0d04841d-8611-4325-9c68-f35e684e7eb8'></a>

Death by viral cytopathicity occurs faster than death by natural means;
that is, μb > μτ. Therefore,

<a id='9ac6c3b5-1ba4-43ef-b75d-1e905f9f906a'></a>

dT_tot / dt < s - mu_T T_tot + rT (1 - T_tot / T_max).

<a id='d08d9df4-e1b4-4b04-9383-26643d3c7b9c'></a>

Hence at $T_{tot} = T_{max}$,

$$\frac{dT}{dt}\Bigg|_{T_{tot}=T_{max}} < s - \mu_T T_{max} < 0.$$

<a id='aef10589-f724-4d84-9145-7329dc2efcbc'></a>

The last inequality follows from Equation (4). Thus, in the case of HIV infection, the total T-cell population, $T_{tot}$, and hence the various sub-populations, $T(t)$, $T^*(t)$, and $T^{**}$, are all bounded by $T_{max}$.

<a id='4e5e4d5e-9a9e-40cb-afa6-245f2923cbbb'></a>

We now show that within the nonnegative orthant there are two possible steady states, one with no virus present, an _uninfected steady_ state, and another with a constant level of virus, an _endemically infected_ steady state. Setting the left-hand sides of Equations (5b) and (5c) to zero yields

<a id='f51b36c5-85f2-4f4d-8f9f-3af9ed212fa0'></a>

T* = k₁VT / (k₂ + μ₁) (6)

T** = k₂T* / μₘ = k₂k₁VT / (μₘ(k₂ + μ₁)) (7)

<a id='36378b63-95fe-40ac-870a-d506124e6d86'></a>

Substituting Equations (6) and (7) into (5d), one finds

dV/dt = [[ (Nk₂ / (k₂ + μ_T)) - 1 ] k₁T - μ_V ]V.

(8)

<a id='97043118-4cce-4f8d-b784-88cfd7648349'></a>

The equation $dV/dt = 0$ has two possible solutions, $V = 0$ and $T = \mu_V/\alpha$, where

$\alpha = k_1\left(\frac{Nk_2}{k_2 + \mu_T} - 1\right)$. (9)

<a id='30297dc1-01d8-44cc-8bcb-432fd5a07503'></a>

If _V_ = 0, then from (6) and (7), _T_* = _T_** = 0. Substituting into (5a),
we find quite obviously that there exists one steady state in which the

<!-- PAGE BREAK -->

<a id='a97bc903-57f0-4f7f-8d20-f7dc7dac1b4d'></a>

92                                            ALAN S. PERELSON ET AL.
virus is totally absent. We call this the *uninfected* state. It is given by

<a id='582aecba-c20f-4a25-adfa-6506c737f1b2'></a>

$\bar{T} = T_0, \quad \bar{T}^* = \bar{T}^{**} = \bar{V} = 0, \quad (10)$

<a id='01aab3d4-f4db-42be-8705-5edf21e5132a'></a>

where an overbar denotes a steady-state value and T₀ is given by Equation (3). Introducing the parameters
p = r - μ_T and γ = r / T_max,
(11a,b)

<a id='02a51dc3-a5c3-4d64-92e8-3eb2b7944bb1'></a>

we can rewrite (3) in a form that will be useful later:

$T_0 = \frac{p + \sqrt{p^2 + 4sy}}{2\gamma}$ (12)

<a id='d0ad7869-03df-4b2a-88d7-0517d398dd9f'></a>

If V≠ 0, then substituting T = μν/α and Equations (6) and (7) into
Equation (5a) leads to a second steady state, which we call the endemi-
cally infected state. In this state,

<a id='158f7d58-297c-4598-87ae-27a70434a489'></a>

T̄ = μ_v / α = μ_v k_3 / k_1 (N k_2 - k_3) , (13a)
T̄* = k_1 μ_v V̄ / α k_3 = μ_v V̄ / N k_2 - k_3 , (13b)
T̄** = k_2 k_1 μ_v V̄ / μ_b α k_3 = k_2 μ_v V̄ / μ_b (N k_2 - k_3) , (13c)
V̄ = s α^2 + ρ α μ_v - γ μ_v^2 / k_1 μ_v (α + β μ_v) , (13d)

<a id='2f53a351-d2da-429d-aa0d-97895753a333'></a>

where

k_3 = k_2 + \mu_T, \quad \beta = \frac{\gamma}{k_3} \left(1 + \frac{k_2}{\mu_b}\right).
(14)

<a id='46a59991-c0a3-4e53-9dc3-846807911151'></a>

3.1. *STABILITY OF THE UNINFECTED STATE*
For the uninfected steady state to be asymptotically stable we require that after the introduction of a small amount of virus, dV/dt < 0. Setting T = T_0 and examining (8), we find dV/dt < 0 if and only if N < N_crit, where

<a id='83544c0b-5972-4387-acb4-d3eb666834a5'></a>

$$N_{crit} = \frac{k_3(\mu_V + k_1T_0)}{k_2k_1T_0}. \quad (15)$$

<a id='0fbaf2d8-b8a2-494c-b045-ba426dc39faa'></a>

Thus, a reasonable conjecture is that the uninfected steady state is stable if and only if N < N_crit. This is formally proved below.

<!-- PAGE BREAK -->

<a id='56f26703-bc3a-4f9d-a2c1-ae84d50dd1ff'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='af6c50c9-87af-44fe-a918-4e8f908dcced'></a>

93

<a id='741f2eff-2502-464f-8254-4542a50fec51'></a>

The Jacobian matrix A for system (5) evaluated at the uninfected steady state is given by

<a id='dd85bf98-b0ec-40a8-8353-dd434e68f05d'></a>

A = 

(  
-a     -γT₀   -γT₀   -k₁T₀
0      -k₃    0      k₁T₀
0      k₂     -μ_b   0
0      0      Nμ_b   -k₄
)
, (16)

<a id='fbdec922-5deb-4705-b6f5-fdc8cc7b990a'></a>

where

<a id='da1c11d3-0520-41a4-b160-066eb7183f73'></a>

k_4 = k_1 T_0 + \mu_v, a = -p + 2T_0 \gamma. (17)

<a id='8eaeff4b-4ecd-43f8-a8fb-758f065868d7'></a>

Substituting the value of T_0 from Equation (12), one sees that a
= sqrt(p^2 + 4sγ) > 0..
The uninfected steady state is asymptotically stable if and only if all
of the eigenvalues of the Jacobian matrix A have negative real parts.
The eigenvalues can be determined by solving the characteristic equa-
tion det(A – λI) = 0. For A given by Equation (16), this becomes

<a id='cbdf8d71-54bf-4da2-a384-8a3c4746e91b'></a>

(λ + a)[(λ + μb)(λ + k3)(λ + k4) - k1k2T0Nμb] = 0, (18)

<a id='018ef179-aa36-4d62-ab99-cb074aa9a746'></a>

and hence one eigenvalue is $\lambda = - a < 0$. Dividing Equation (18) by $\lambda + a$, we obtain the reduced equation

<a id='bda40a4b-47ac-46f6-a862-bfdf8b9bd132'></a>

$\lambda^3 + A\lambda^2 + B\lambda + C = 0,\quad(19)$

<a id='44292b06-d842-4c7a-bb05-412230ae806c'></a>

where the coefficients

A = μ_b + k_3 + k_4 > 0, (20a)
B = k_3 k_4 + μ_b (k_3 + k_4) > 0, (20b)
C = μ_b (k_3 k_4 - k_1 k_2 T N). (20c)

<a id='cbf9dedc-81c3-4b21-aede-f3e42ba9ed85'></a>

Using the definition of N_crit, we can rewrite Equation (20c) as

C = μ_b k_1 k_2 T_0 (N_crit - N). (20d)

<a id='75aed534-8531-4878-b74c-ec8d87545e9d'></a>

By the Routh-Hurwitz criteria [63], the three roots of the characteris-
tic equation (19) will have negative real parts if and only if

<a id='0e558f29-aeba-42a9-9426-c7048890eaf3'></a>

A, C > 0 and AB - C > 0.

<a id='49be82f7-b7df-409a-83d1-72c4591bae4d'></a>

The coefficient _A_ is the sum of positive terms and is positive. Under
the condition _N_ < _N_crit, we have _C_ > 0 and

<a id='4c12a402-32f7-4d6c-9b29-17de3d122439'></a>

AB – C = μ_b²(k₃ + k₄) + μ_b(k₃² + k₄² + 2k₃k₄ + k₁k₂T₀N) + k₃k₄(k₃ + k₄) > 0.

<!-- PAGE BREAK -->

<a id='30d12cb4-68ba-4a07-9d01-0fe2deb7744f'></a>

94

<a id='15546a4e-319e-453e-a831-4afb1c036f60'></a>

ALAN S. PERELSON ET AL.

<a id='e230c240-2a7b-4646-b840-2d95d8ccc5e3'></a>

Thus, if $N < N_{crit}$, the uninfected state is asymptotically stable.

If $N = N_{crit}$, $C = 0$, and (19) then implies that one eigenvalue must be zero. Applying the Routh-Horowitz condition to the reduced characteristic polynomial $\lambda^2 + A\lambda + B$, it is easy to see that the remaining two eigenvalues have negative real part. Thus, if $N=N_{crit}$, the uninfected state is neutrally stable.

<a id='c284a838-4f0e-4cfd-9d7f-616173c1dbe7'></a>

If N > N_crit, then by (20d) C < 0, and thus at least one eigenvalue will have positive real part. When C < 0 there is one sign change in (19). Hence by Descartes' rule of signs [44] we can conclude that there is exactly one positive eigenvalue when N > N_crit. Thus, the uninfected state is unstable if N > N_crit.

<a id='85f30bd2-a803-412d-b306-9aeaa35e0b96'></a>

These results imply that for the uninfected steady state, N is a bifurcation parameter and that the stability of the state is lost as N increases past N<sub>crit</sub> (Figure 1).

<a id='f920ffe7-38e0-4a4d-b017-d4b2efe6a1ad'></a>

So far, we have dealt with only the local stability of the uninfected steady state. For N < N_crit there is only one steady state in the nonnegative orthant, and we conjecture that it is globally stable. For 0 ≤ N < (k_2 + μ_T)/k_2 < N_crit, it is easy to show that this conjecture is true. Consider the function L(t) = T* + NT** + V, which as we shall see is a

<a id='27afa1de-55a4-41ac-a9ab-85ccd1ae0f5a'></a>

<::chart: A 2D plot showing a transcritical bifurcation. The y-axis is labeled 'T' and ranges from 0 to 2000, with a major tick at 1000. The x-axis is labeled 'N' and ranges from 0 to 2000, with major ticks at 500, 1000, 1500, and 2000. There are two curves plotted. One is a horizontal line at T=1000. This line is thick and dark for N values from 0 up to approximately 774, and then becomes thin and light for N values greater than approximately 774. The second curve starts at a high T value (above 2000) for small N, decreases, and intersects the T=1000 line at approximately N=774. For N values less than approximately 774, this curve is thin and light. For N values greater than approximately 774, this curve becomes thick and dark and continues to decrease. The caption for this figure is: FIG. 1. Transcritical bifurcation. The steady-state values of T are plotted versus N. Stable steady states are indicated by dark heavy lines, unstable steady states by light lines. Parameter values are given in Table 1. For N < Ncrit = 774, the uninfected steady state with T = 1000 is stable. At N = Ncrit this state loses its stability, and the endemically infected state with T a decreasing function of N becomes stable.::>

<!-- PAGE BREAK -->

<a id='89727660-ada0-40ee-b78c-df33d1225b2a'></a>

HIV INFECTION OF CD4+ T CELLS 95

<a id='c6f6b2db-e959-44bb-9de9-9e2dbdd3f29b'></a>

Lyapunov function. In the nonnegative orthant, L(t) ≥ 0. From Equa-
tions (5),

<a id='542848c5-bb96-4906-b733-5348f7b92131'></a>

<::dL/dt = [(N-1) k_2 - μ_T]T* - μ_V V.: figure::>

<a id='7141aec3-1128-4356-b7b7-99750d080834'></a>

For N < (k₂ + μᵣ)/k₂, the term in brackets is negative, and hence dL/dt < 0. Thus, as t→∞, L(t)→0. Hence T*, T**, and V all approach 0, and T → T₀.

<a id='172b1350-b106-4357-8961-32b6010919c3'></a>

3.2. ENDEMICALLY INFECTED STEADY STATE

At $N = N_{crit}$, $\alpha = \mu_\nu / T_0$ and $\bar{V} = 0$. This can be seen by substituting (15) into (9) and then substituting $\mu_\nu / T_0$ for $\alpha$ in (13d). Thus, at $N = N_{crit}$, the endemically infected state and the uninfected state coincide. At $N = N_{crit}$, there is a transcritical bifurcation, and the endemically infected state emerges for $N > N_{crit}$ as a new steady state in $R^4_+$. For $N < N_{crit}$, the infected steady state does not lie in $R^4_+$, because $\bar{V}, \bar{T}^*, \bar{T}^{**} < 0$, and hence it is unphysical. Further, since $R^4_+$ is positively invariant, this unphysical steady state is not reachable from initial conditions in $R^4_+$. Thus, we need only study the stability of the endemically infected state for $N > N_{crit}$.

<a id='3d8cbb40-aee6-485b-92ea-3de9ca2006c9'></a>

Linearizing Equations (5) around the endemically infected state, we obtain the Jacobian matrix A,

<a id='a6df2c4e-c658-41e2-83df-d3ab2b516e67'></a>

A =
$$\begin{pmatrix}
-a & -\gamma\bar{T} & -\gamma\bar{T} & -k_1\bar{T} \\
k_1\bar{V} & -k_3 & 0 & k_1\bar{T} \\
0 & k_2 & -\mu_b & 0 \\
-k_1\bar{V} & 0 & N\mu_b & -\hat{k}_4
\end{pmatrix}$$
(21)

<a id='32305bef-2059-42c3-9d6d-61293a41d202'></a>

where

<a id='89426963-8bbe-4b43-8f10-633c3e4743bf'></a>

k_3 = k_2 + \mu_T, (22a)

\hat{k}_4 = k_1\bar{T} + \mu_V, (22b)

a = -p + \gamma(2\bar{T} + \bar{T}^* + \bar{T}^{**}) + k_1\bar{V}, (22c)

<a id='db61193c-dc31-443e-82b5-db048b1f7bbb'></a>

and $\overline{T}$, $\overline{T}^*$, $\overline{T}^{**}$, and $\overline{V}$ are given by Equations (13). Using the steady state form of (5a),

<a id='96da3c26-dc0e-4014-8fad-0ba8bef3292c'></a>

0 = s + p\bar{T} - \gamma\bar{T}(\bar{T} + \bar{T}^* + \bar{T}^{**}) - k_1\bar{V}\bar{T},

<a id='44ec589c-f6ae-4506-b680-03a3234cd1c6'></a>

one easily sees $a\bar{T} = s + \gamma\bar{T}^2$, and hence

<a id='b01ef0f8-fa71-4f85-ab76-cae7d861af8e'></a>

a = γT̅ + s/T̅ > 0. (23)

<!-- PAGE BREAK -->

<a id='8d1c5d6f-67d2-42b8-a7a2-09131b2c1650'></a>

96
ALAN S. PERELSON ET AL.
Examining the characteristic polynomial, det(A – λI), we find it has
the form λ⁴ + bλ³ + cλ² + dλ + e, where the coefficients are

<a id='ee83d8a7-7cab-4df8-acfb-dd03265bf5d4'></a>

b = a + k_3 + \hat{k}_4 + \mu_b > 0, (24a)
c = a(k_3 + \hat{k}_4 + \mu_b) + \mu_b(k_3 + \hat{k}_4) + k_3\hat{k}_4 + k_1\sqrt{T}V(\gamma - k_1), (24b)
d = a[k_3\hat{k}_4 + \mu_b(k_3 + \hat{k}_4)] + k_1\sqrt{T}V[\gamma(\mu_v + k_2 + \mu_b) - k_1(k_3 + \mu_b)], (24c)
e = k_1\sqrt{T}V[k_1\mu_b(Nk_2 - k_3) + \gamma\mu_v(k_2 + \mu_b)]. (24d)

<a id='10399d9f-ba99-4a4e-8060-b053aec9c52e'></a>

In calculating the coefficients of the characteristic polynomial we
have eliminated a term proportional to $k_3\hat{k}_4 - k_1k_2NT$ from both $d$
and $e$, because substituting the definitions of $\hat{k}_4$ and $\overline{T}$ shows that this
term is zero.

<a id='db2bd241-5fc4-45e8-ae74-916f7613a27a'></a>

Analyzing the characteristic polynomial, it is obvious that b is positive. For N > Ncrit, Nk2 > k3. Thus e is positive as well.

<a id='22791689-0c11-4385-b28a-e610b3c5c8a6'></a>

To establish the stability of this steady state, it is also necessary to show that both c and d are positive and that $(bc-d)/d/b^2 > e$. For the parameters given in Table 1, all three conditions are met; however, for some parameter regimes, this steady state is unstable (Table 2).

<a id='e89e2825-88cf-4fa1-a7ff-8fae21dcb194'></a>

4. T-CELL DEPLETION

In the endemically infected state, normal T cell population regula- tion is disturbed by the presence of HIV. In this new steady state the

<a id='d6f221d0-a307-4ca5-8c12-9ad2659d85da'></a>

TABLE 2
Parameters for Oscillations
<table id="15-1">
<tr><td id="15-2"></td><td id="15-3">Parameters and constants</td><td id="15-4">Initial or default value</td></tr>
<tr><td id="15-5">s</td><td id="15-6">Rate of supply of CD4+ T cells from precursors</td><td id="15-7">10 day-1 mm-3</td></tr>
<tr><td id="15-8">r</td><td id="15-9">Rate of growth for the CD4+ cell population</td><td id="15-a">12 day-1</td></tr>
<tr><td id="15-b">Tmax</td><td id="15-c">Maximum CD4+ cell population level</td><td id="15-d">1500 mm-3</td></tr>
<tr><td id="15-e">μT</td><td id="15-f">Death rate of uninfected and latently infected CD4+ cells</td><td id="15-g">0.06 day-1</td></tr>
<tr><td id="15-h">μb</td><td id="15-i">Death rate of actively infected CD4+ cell population</td><td id="15-j">0.24 day-1</td></tr>
<tr><td id="15-k">μv</td><td id="15-l">Death rate of free virus</td><td id="15-m">5 day-1</td></tr>
<tr><td id="15-n">k1</td><td id="15-o">Rate constant for CD4+ cells becoming infected by free virus</td><td id="15-p">2.4 mm³ day-1</td></tr>
<tr><td id="15-q">k2</td><td id="15-r">Rate latently infected cells convert to actively infected</td><td id="15-s">1.2×10-4 day-1</td></tr>
<tr><td id="15-t">N</td><td id="15-u">Number of free virus produced by lysing a CD4+ cell</td><td id="15-v">1200</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='19a21199-e57c-469e-bb49-1ab449312ca8'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='2742f356-f6d6-43d3-afc9-8f00618934c5'></a>

97

<a id='530940d5-6628-4b2a-9bfb-e433bdb9a89d'></a>

T-cell level can be considerably lower than in the uninfected steady
state. Thus, one of the main conclusions of this model is that HIV
infection itself may be sufficient to account for a substantial amount of
the T-cell depletion seen in AIDS. To establish under what conditions
this is the case, we examine Equation (11) in some detail.

<a id='70656531-4946-4bf8-a476-d0277ec511c6'></a>

As a simplifying approximation let us assume that with appropriate
parameter choices the model can mimic the population distribution in
vivo in which, say, 1 in 100 cells are latently infected and 1 in 10,000 to 1
in 100,000 are actively infected. In this case, T-cell depletion must occur
predominantly in the uninfected pool. According to (13a), at steady
state the uninfected T-cell population size is

<a id='d3022212-c910-4a13-adb9-3842e84476c5'></a>

T = μv / k1(Nk2 / k3 - 1),

<a id='d14d9b09-0880-4ae2-9140-a16f0304eedf'></a>

where k₃ = k₂ + μτ. Since N > N<sub>crit</sub>, let N = N<sub>crit</sub> + n. Then, substituting the value of N<sub>crit</sub> from Equations (15), one can write

<a id='5c8f3f73-a003-428b-ab87-3f430d841f44'></a>

$$\frac{\bar{T}}{T_0} = \frac{1}{1+\delta},$$ (25)

<a id='abd10689-ae94-4b83-bb1d-ef0ddc98befe'></a>

where

$\delta = \frac{k_1 n T_0}{\mu_V (\mu_T / k_2 + 1)}$. (26)

<a id='bd5fe34d-30aa-4272-b3f9-d35d584dca3b'></a>

Since δ>0, T <T₀, and there is depletion of uninfected cells at the endemically infected steady state. As a useful measure of the degree of depletion of uninfected cells, we introduce

D=1−(T/T₀) = δ/(1+δ).
(27)

<a id='7cdf0c5d-5055-47ce-8741-87fcbb8a5c1f'></a>

Thus, D = 0 implies no depletion and D = 1 means total depletion. The larger δ, the larger the depletion. Consequently, there is increased depletion of uninfected T cells

(1) If the virus lives longer (i.e., if μv is decreased).
(2) If there is a higher rate of viral infection (i.e., if k1 is increased).
(3) If a larger number of viruses are produced per T cell (i.e., if n is increased).

<a id='2df4b7bc-5014-4331-8985-a0bbbf0de685'></a>

Further, if μ_τ / k_2 ≫ 1, then there is also increased depletion

<a id='ac623cf9-7e52-496e-aaa6-b43a048f38f8'></a>

(1) If there is more rapid conversion from the latent to the actively infected state (i.e., if k₂ is increased), or
(2) If T cells live longer (i.e., if μT is decreased).

<!-- PAGE BREAK -->

<a id='f4ff4235-7943-4a8a-a37e-ff8ead3f7c29'></a>

98

<a id='9334b92d-e926-486d-bd80-2549de21633b'></a>

ALAN S. PERELSON ET AL.

<a id='184ed565-5836-4942-ba53-0972063412ee'></a>

We also note that the depletion of uninfected cells is independent of μb, the death rate of actively infected cells, and s, the rate of supply of uninfected cells. However, increasing μb will have a small effect on the total T-cell population because it will decrease T**. Also, increasing s will increase V and thus, from (13b) and (13c), increase T* and T**. Thus, as one would expect, increasing s will decrease the total depletion. To see this explicitly, we compute the steady-state level of infected cells. From Equations (13b–13d) and (14) we find

<a id='0b378e44-0941-4f98-a201-6f27be01fc26'></a>

$$\bar{T}^* + \bar{T}^{**} = \frac{\beta[s\alpha^2 + \rho\alpha\mu_v - \gamma\mu_v^2]}{\gamma\alpha(\alpha + \beta\mu_v)} \quad (28)$$

<a id='c6552978-78ee-4947-842f-ea68116288a3'></a>

where \u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u0301\u0300\u0304\u0311\u0304\u0312\u0303\u0310\u0306\u0305\u0302\u0308\u0307\u0309\u030

<a id='7af8887a-6edf-4050-9717-68ec4b41d5bd'></a>

5. PARAMETER VALUES
Choosing parameter values characteristic of the in vivo situation is difficult; many of the parameters in our model have not been measured, or, if measurements have been attempted, they may not be as accurate as we need for quantitative predictions. Thus one role of modeling is to point out where further quantitative measurements can improve our understanding of the AIDS disease process.

<a id='74f66f7f-77bc-4cf2-bba7-b4fe9cca1a4d'></a>

The number of CD4⁺ T cells in the peripheral blood is approxi-
mately 1000/mm³, although it fluctuates both diurnally and with the
total lymphocyte count [33, 34, 40]. We shall choose 10³ as the “stan-
dard” number of CD4⁺ T cells (per mm³) in a healthy individual and
use this value as an initial condition, T₀ = T(0) = 10³. As is common in
the clinical literature, we shall report all T-cell numbers per cubic
milliliter. The T-cell number in the blood fluctuates and can easily
increase by 50% or so [1]. Thus we choose Tmax = 1.5×10³, which is
higher than typically reported T4 counts in healthy individuals but lower
than the maximum that can be obtained in severe infection. Under
conditions of infection, different lymphokines are secreted and different
control mechanisms presumably come into play. Under such conditions
our model of T-cell population dynamics would have to be modified.
Our assumption of a noninfectious situation is consistent with the
modeling approach taken here in which the immune response to HIV
and other antigens is being neglected.

<a id='057ffd62-5102-4d53-9e00-9d299cda6bae'></a>

We assume that activated T cells divide every 12-18 h. Therefore the
growth rate of an activated cell is approximately 1 day⁻¹. This growth
rate must be multiplied by the fraction of T cells that are dividing. This
is probably on the order of 1%. To this is added a death rate, so that r

<!-- PAGE BREAK -->

<a id='11b576c1-6273-40fe-ae2e-1293dfea1151'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='7e2971fa-0426-4f8b-ac93-e188f53b4ea5'></a>

99

<a id='d0268da2-1358-46a6-acd7-fbec7bc0e190'></a>

represents the net rate of increase in the population when cell death is taken into account. In the simulations reported here, we let r = 0.03 day⁻¹, μ_T = 0.02 day⁻¹ (see below), and hence the net proliferation rate p = 0.01 day⁻¹. Smaller growth and death rates would also be reasonable.

<a id='8cddba87-5ee8-4484-8779-9650a8bd0f3f'></a>

The lifetime of unactivated T cell is variable. Memory cells may live a long time, whereas precursor cells and non-memory T cells may live a short time. Freitas et al. [18] report that 50–60% of peripheral mature T lymphocytes of the mouse are replaced every 2–3 days. In this model, where we have not distinguished subpopulations of T cells, the death rate μT represents an average over all subpopulations. Thus, although some human T cells may live for years, it is clear that many T cells have much shorter lifetimes. Recent work of Gray [22] and Gray and Leanderson [23] indicates that memory T cells may live 2–6 weeks in the absence of antigen-stimulated replication. This we feel is reasonable as an average. Thus we take μT = 0.02 day⁻¹, which corresponds to a half-life of 36 days.

<a id='91469e59-a5eb-400f-ae4a-ee60ac0cd4de'></a>

The supply of new T cells from precursors populations must be less than the number required to maintain the T-cell population constant.
Thus s ≤ μT T₀. With T₀ = 10³ mm⁻³ and μT as above, s ≤ 20 day⁻¹ mm⁻³. If we take s = 10 day⁻¹ mm⁻³, with r as given above, half of the T-cell replenishment is by proliferation in the periphery and half from the supply term. The parameters r, s, and μT have been chosen so that, in the absence of virus, the population of CD4⁺ T cells is maintained at its initial value T₀ = 10³ mm⁻³. Other choices of these parameters, of course, can also maintain this steady-state population level.

<a id='e34f19f4-eafc-4456-9fd7-8bdaad22aa79'></a>

Estimating the rate k_1 at which virus infects T cells is difficult. Because k_1 is a bimolecular rate constant, it has the dimensions of 1 over cell concentration per unit time. A useful scaling is therefore to consider k_1 T_0, which has the units of time^-1. In order for a virus to infect a cell, it must encounter the cell, bind CD4 or some other receptor, and then enter the cell. Thus infection cannot be any faster than the rate of transport to the cell surface. We can thus use Smoluchowski's formula for the diffusion-limited rate constant to provide an upper bound on k_1. For interaction between two spherical particles of radii r_T and r_V and diffusion coefficients D_T and D_V, k_1 ≤ 4π(r_T + r_V)(D_T + D_V). Using r_V = 5×10^-6 cm, r_T = 4×10^-4 cm, D_V = 2×10^-8 cm^2 s^-1, and D_T = 2.5×10^-10 cm^2 s^-1 as given in Layne et al. [36], k_1 ≤ 10^-10 cm^3 s^-1 = 0.6 × 10^-3 mm^3 h^-1. Hence k_1 T_0 ≤ 0.36 h^-1. For particles the size or HIV, convective transport would not be able to increase this rate [52]. Once a virus particle encounters a cell, it need not infect it. The CD4 level will vary among T cells. Cells with low levels of CD4 may resist infection. Further, the state of activation of the

<!-- PAGE BREAK -->

<a id='2b9d8892-f8e3-4e46-8bfb-2ffab1947d18'></a>

100

<a id='7f8077da-9ad9-47af-a5b9-0faf67881414'></a>

ALAN S. PERELSON ET AL.

<a id='593cc4a5-f97b-4cc2-a42b-64cc3ba91c51'></a>

cell may be important. Some work has suggested that only activated T cells can be successfully infected [21, 65]. Kiernan et al. [31], using an in vitro system, found that although 40% of input virus attached to cells, only 2–3% of cells became actively infected. Thus, it seems reasonable to suppose that only a fraction of the encounters between HIV and T cells will lead to infection. As an initial guess, we assume that k_1 T_0 = 10^{-3} h^{-1} = 2.4 \times 10^{-2} days^{-1}. Since different viral strains have different tropisms and different degrees of virulence, one might safely assume that k_1 is a strain-dependent parameter that can vary greatly.

<a id='7cb9a846-0423-436d-b8a0-a2ad779e90f6'></a>

Latently infected cells behave the same as normal T cells and thus should have the same death rate. However, we assume that when they interact with antigen, rather than dividing they become actively infected. The time for death of an actively infected cell is probably a few days to a week. Somasundaran and Robinson [57] found that in cells of the T-cell line C8166, a 3–4-day lag occurred between expression of viral proteins and cell death in actively infected cells. Kiernan et al. [31] found that HIV-infected MT-2 cells remain viable up to 62 h postinfection, after which viability rapidly decreases. Thus we shall choose μ_b = 0.24 day^-1.

<a id='3021c148-5a1a-409e-894a-045a349b6ea9'></a>

The number of infectious viruses released, N, is not known precisely. Merrill [42] suggests that N is between 50 and 1000. Layne et al. [36] estimate N > 300 from data on the minimum concentration of soluble CD4 needed to block HIV infectivity in an in vitro assay. Somasundaran and Robinson [57] find that the standard laboratory strain of HIV, IIIB, selected to grow well in culture, can produce between 300,000 and 2.5 million copies of viral RNA in actively infected cells. The number of these viral RNAs that are packaged into viral particles and released was not measured, but such high levels of expression indicate that values of N well above 10³ are possible. Viral isolates exhibit great variability; some replicate fast and are highly cytopathic, while others replicate slowly [6, 15]. In order to study the differences in disease course with different viral strains we will vary N in our studies. However, we keep N in the low range of permissible values because this model is applicable only to strains of HIV that do not stimulate an immune response. As argued elsewhere, we believe that such strains should be low viral producers [46].

<a id='039421d0-e4c2-49a1-aedf-490cedc124fa'></a>

Free virus loses its infectivity over time, probably due to the shedding
of gp120 [19]. For example, in a viral infectivity assay, HIV-1 strains
IIIB and RFII lost half of their infectivity in 4–6 h at 37°C [36]. Thus we
take μν = 2.4 day⁻¹.

<a id='ced0d946-3238-459f-8cf3-1f5f711e8a92'></a>

The rate of conversion of a latently infected cell to an actively
infected cell is k2. We assume that only those latently infected T cells
that recognize and respond to the antigen activate HIV replication.

<!-- PAGE BREAK -->

<a id='3813a7b9-7724-4f37-9b8f-dbe9b816d04a'></a>

HIV INFECTION OF CD4⁺ T CELLS

<a id='6d427575-f652-4197-bb38-206479ef3451'></a>

101

<a id='e5f57dab-ca92-4589-848f-dbafd87df4ff'></a>

Thus, as in the calculation of the average T-cell growth rate r, k₂ has
embedded in it a factor proportional to the average fraction of T cells
stimulated by environmental antigen. Because the process of activating
HIV replication requires cell division, we expect k₂ ≤ r. Further, the
conversion process may not be 100% efficient; that is, some latently
infected cells that are activated by antigen may not produce virus or
may produce defective virus. Thus, k₂ may be considerably smaller than
r. Here we choose k₂ = 0.1r = 3×10⁻³ day⁻¹, where the value of r is
our default value for healthy individuals responding to normal environ-
mental antigens. If one focuses on times of infection by disease-causing
agents other than HIV, the parameters r and hence k₂ could change.
Models by Cooper [7], Intrator et al. [30], Reibnegger et al. [54],
McLean [41], McLean and Kirkwood [39], Anderson [3], and Anderson
and May [4] all consider the effects of secondary infection. Here we are
modeling the course of HIV on a long time scale, and the specific
effects of one infection or another are not explicitly considered. Rather
the net effect of all such antigen encounters is used to estimate the
value of r.

<a id='693ec7f3-d326-481b-b19e-4c7a9630da6b'></a>

A summary of the parameter values used in this paper is given in Table 1. However, other sets of parameters can be used that give similar behavior. If we require that T-cell dynamics in the absence of virus give a steady-state value of 1000 T cells/mm³, then only certain combina-tions of r, s, Tmax, and μT are permissible. Once these parameters are established, there is a restricted set of viral parameters that give rise to the long incubation period characteristic of HIV infection. In Perelson [49] the parameters used were quite different (s = 36 day⁻¹ mm⁻³, r = 0.108 day⁻¹, μT = 0.072 day⁻¹, Tmax = 1500 mm⁻³, k₁ = 2.4×10⁻² mm³ day⁻¹, k₂ = 1.2×10⁻⁴ day⁻¹, μv = 2.4 day⁻¹, and μb = 1.2 day⁻¹), yet gave similar dynamical behavior.

<a id='c01d1c1b-8151-4ab2-a401-a736614f09a0'></a>

6. NUMERICAL SOLUTIONS
To study the time course of the infection, we numerically integrated Equations (5). In Figure 2 we illustrate typical solutions for three values of N all greater than N_{crit}, using the parameters given in Table 1. We choose initial conditions characteristic of an uninfected individual; T(0) = T_0, T*(0) = T**(0) = 0, infected with free virus, V(0) = V_0. Here we considered the case of exposure to one infectious virion per milliliter, which corresponds to V_0 = 10^{-3} mm^{-3}. For the parameters in Table 1, N_{crit} = 774. For the three values of N displayed, we see from the upper right panel that the disease is characterized by a lag phase in which there is no discernible T-cell depletion, followed by a phase in which the CD4+ T cells decline (Figure 3). In the case N = 1000, the lag is about

<!-- PAGE BREAK -->

<a id='9bf3eb13-7886-4296-bcb9-75274c41d0f6'></a>

102 ALAN S. PERELSON ET AL. <::chart: The figure presents four line graphs arranged in a 2x2 grid, all depicting dynamics over "YEARS" on the x-axis, ranging from 0 to 10. Each graph shows three distinct curves, representing different values of N: N = 1000 (*), N = 1200 (□), and N = 1400 (○). Top-left graph: Titled "FREE VIRUS" with a logarithmic y-axis from 10^-5 to 10^3. All three curves start at 10^-5 and increase, eventually plateauing at 10^3. The curve for N = 1000 (*) rises most slowly, followed by N = 1200 (□), and N = 1400 (○) rises most rapidly. Top-right graph: Titled "UNINFECTED T4 CELLS" with a linear y-axis from 500 to 1000. All three curves start at 1000 and decrease. The curve for N = 1400 (○) drops fastest to approximately 550. The curve for N = 1200 (□) drops to approximately 650. The curve for N = 1000 (*) drops slowest to approximately 750. All curves then flatten out. Bottom-left graph: Titled "LATENTLY INFECTED T4 CELLS" with a logarithmic y-axis from 10^-5 to 10^3. Similar to the top-left graph, all three curves start at 10^-5 and increase, plateauing at 10^3. The curve for N = 1000 (*) rises most slowly, followed by N = 1200 (□), and N = 1400 (○) rises most rapidly. Bottom-right graph: Titled "ACTIVELY INFECTED T4 CELLS" with a logarithmic y-axis from 10^-7 to 10^1. All three curves start at 10^-7, increase to a peak, and then level off at 10^1. The curve for N = 1000 (*) rises most slowly and peaks latest, followed by N = 1200 (□), and N = 1400 (○) rises most rapidly and peaks earliest. FIG. 2. Dynamics of HIV infection. Solutions of Equations (5a)–(5d). Parameters are given in Table 1. In each graph the three curves correspond to different values of N, the number of infectious virus particles produced per actively infected cell. Here N_crit = 774 and N = 1000 (*), N = 1200 (□), and N = 1400 (○).::>

<a id='5f44930c-8bb4-4038-bf80-31d06ae4868b'></a>

6 years, with the T-cell decline occurring between years 6 and 8. For larger values of N, the decline in both uninfected and total CD4⁺ cells is more substantial but the lag is shorter. The two lower panels in Figure 2 indicate the changes in the latently infected T* and actively infected T** populations. The curves are essentially identical, up to a scale factor, as might be expected from the establishment of a quasi-steady state in which dT**/dt = 0. In a quasi-steady state, Equation (5c) predicts that T** = k₂T* / μb. Figure 2 shows that such a quasi-steady state is established, because k₂/μb = 1.25×10⁻² is the ratio of T** to T* seen at long times. The number of actively infected cells remains less than 10⁻¹ mm⁻³ for 2–5 years depending on N. At this level of expression, less than 1 in 10⁴ T cells would be actively infected, as has been observed. Late in the infection process, however, one can

<!-- PAGE BREAK -->

<a id='c33009a1-d228-42d2-93e0-d5b1b2c33a94'></a>

103

<a id='2bb3b275-d914-4d13-8a3a-f266d9bb42a9'></a>

HIV INFECTION OF CD4$^+$ T CELLS
103
<::chart: A line graph titled "HIV INFECTION OF CD4$^+$ T CELLS" shows the total CD4$^+$ T-cell population versus time after infection. The y-axis is labeled "TOTAL T4 CELLS" and ranges from 820 to 1000. The x-axis is labeled "YEARS" and ranges from 0 to 10. Three curves are plotted:
- One curve, marked with asterisks (*), starts at 1000 and gradually decreases, reaching approximately 925 at year 10.
- A second curve, marked with squares (□), starts at 1000, drops sharply between year 3 and year 4, and then levels off at approximately 880 from year 5 to year 10.
- A third curve, marked with circles (○), starts at 1000, drops sharply between year 2 and year 3, and then levels off at approximately 825 from year 4 to year 10.

FIG. 3. The total CD4$^+$ T-cell population given by $T+T^*+T^{**}$ versus time after infection. The three curves correspond to different values of $N$, the number of infectious virus particles produced per actively infected cell, $N = 1000 (*)$, $N = 1200$ (□), $N=1400 (igcirc)$.
:chart::>


<a id='dadf264a-8109-4c30-bf5d-b5b1838f746a'></a>

obtain ratios closer to 1 in 100. The number of latently infected cells remains small but increases over time during the initial phase of infection, consistent with measurements of the increasing viral burden in asymptomatic HIV-seropositive patients [56]. The number of latently infected cells ultimately grows to approximately 102 mm⁻3, which is about tenfold larger than the 1 in 100 infected T4 cells observed by Schnittman et al. [55] in patients with AIDS.

<a id='567d96a7-2e54-4831-aff0-b1dd786323b7'></a>

The upper left panel in Figure 2 shows the changes in the HIV population. For all three values of N, after a fast initial decline due to cellular binding, the viral population grows exponentially, slowing as its steady-state value of a few hundred virions per cubic millimeter is approached. Comparing the dynamics of viral growth with that of the latently infected and actively infected T-cell populations shows that V(t) follows essentially the same dynamics as the infected T cells. Thus, a quasi-steady-state approximation could again be used with benefit. We return to this point later. Figure 4 shows the change in the free virus population as N is decreased further. If N < Ncrit, then after the initial binding V(t) decreases exponentially indicating that the infection will not cause disease and that the uninfected state is being approached. With N > Ncrit, the virus grows after the initial decline, whereas with N = Ncrit the virus rapidly attains a constant level and no T-cell depletion is seen (not shown).

<!-- PAGE BREAK -->

<a id='58fc8535-9f02-4f36-99aa-4adce3002f5c'></a>

104

<a id='b167b56f-b295-4a9d-b291-405a9e3b2e75'></a>

ALAN S. PERELSON ET AL.

<a id='8564a059-2a29-4680-a708-2f36102a1642'></a>

<::chart: A semilog line graph titled "FREE VIRUS" versus "YEARS". The x-axis, labeled "YEARS", ranges from 0 to 10. The y-axis, labeled "FREE VIRUS", is on a logarithmic scale from 10^-7 to 10^3. Three distinct curves are plotted:
1. A curve marked with circles (O) starts at approximately 10^-5 at year 0 and increases steadily to approximately 10^2 at year 10.
2. A curve marked with squares (□) remains constant at approximately 10^-5 across the entire 0-10 year range.
3. A curve marked with asterisks (*) starts at approximately 10^-5 at year 0 and decreases exponentially, falling below 10^-7 by approximately year 2.5.

FIG. 4. The change in free virus population for different values of N. Parameters are given in Table 1. For $N < N_{crit} = 774$, that is, $N = 600 (*)$, the virus decays and the system returns to the uninfected state. For $N > N_{crit}$, that is, $N = 1000 (O)$, the virus grows, whereas at $N = N_{crit} (□)$ the virus remains constant.::>

<a id='6e9a09ca-f66e-42ba-9397-89e8f8f57123'></a>

Changing the parameters in the model changes the details of the
dynamics. For example, increasing N gives rise to larger amounts of
T-cell depletion, which is more characteristic of AIDS, but also speeds
up the depletion, which is less characteristic (Figure 5). Earlier, we
predicted that increased depletion would also occur if µy were de-
creased, that is, if infective virus lived longer. This is what we see in
Figure 6. Changing the initial conditions affects the time from infection
to depletion. As shown in Figure 7, depletion is noticeable once V(t)
reaches a level of about 50 mm⁻³. Thus, as expected, increasing V₀
decreases the time to depletion. Similar effects are seen if infected cells
are used as initial conditions rather than free virus.

<a id='e6356963-c357-4e89-953c-2512bebc6e3a'></a>

6.1. OSCILLATIONS
When the infected steady state is in the positive orthant, that is, for N > Ncrit, it is also stable for most parameter values of biological interest. In parameter regimes where the infected state is unstable, the system undergoes sustained oscillations around the infected state. We studied the behavior of the system in these regimes by numerical integration, using GRIND [8], and by numerical bifurcation, using AUTO [9]. The parameter regime for oscillations is necessarily different from that in Table 1. Table 2 gives the default parameters used in our study of oscillations. Figure 8 illustrates the dynamics of the system

<!-- PAGE BREAK -->

<a id='4a83bbc2-101f-4f8a-8f47-263d35a09476'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='ad053014-f1d1-4d31-9093-c33e03ab4839'></a>

105

<a id='a1254028-4c53-4790-83ea-e2b553653e45'></a>

<::line chart: The chart plots 'TOTAL T4 CELLS' on the y-axis against 'YEARS' on the x-axis. The y-axis ranges from 650 to 1000. The x-axis ranges from 0 to 10. Three lines are depicted: one marked with asterisks (*) for N = 1500, one with squares (□) for N = 2000, and one with circles (○) for N = 3000. All lines start at 1000 T4 cells. The line for N = 3000 (circles) shows the earliest and steepest drop, stabilizing around 660 T4 cells. The line for N = 2000 (squares) drops later and stabilizes around 740 T4 cells. The line for N = 1500 (asterisks) drops latest and stabilizes around 810 T4 cells. FIG. 5. The degree of T-cell depletion depends upon N. Parameters are given in Table 1. N = 1500 (*), N = 2000 (□), and N = 3000 (○) are shown. As N increases, the depletion increases but the time until depletion decreases.::>

<a id='7a8f97da-2165-42f1-b5ce-09ad03631d56'></a>

<::chart: A line graph titled "The influence of the viral death rate μv on T-cell depletion." The y-axis is labeled "TOTAL T4 CELLS" and ranges from 400 to 1000. The x-axis is labeled "YEARS" and ranges from 0 to 10. Three data series are plotted:
- A line marked with asterisks (*), representing μv = 2.4 day⁻¹, starts at 1000 T4 cells, drops around year 3-4 to approximately 825 T4 cells, and then stabilizes.
- A line marked with squares (□), representing μv = 1.2 day⁻¹, starts at 1000 T4 cells, drops around year 1 to approximately 675 T4 cells, and then stabilizes.
- A line marked with circles (○), representing μv = 0.24 day⁻¹, starts at 1000 T4 cells, drops around year 0.5 to approximately 500 T4 cells, and then stabilizes.
FIG. 6. The influence of the viral death rate μv on T-cell depletion. Parameters are given in Table 1; N = 1400, μv = 2.4 day⁻¹ (*), 1.2 day⁻¹ (□), and 0.24 day⁻¹ (○).::>

<!-- PAGE BREAK -->

<a id='999d32c9-17b1-46ee-8948-77732603f6df'></a>

106 ALAN S. PERELSON ET AL. <::chart: FIG. 7. The effect of changing the initial viral load. Parameters are given in Table 1; N = 1400, V₀ = 10⁻⁶ (*), 10⁻⁴ (□), and 10⁻² (O) mm⁻³. The figure contains four plots arranged in a 2x2 grid, all sharing the x-axis label "YEARS" (ranging from 0 to 6). The legend for all plots is V₀ = 10⁻⁶ (asterisk), 10⁻⁴ (square), and 10⁻² (circle). Top-left plot: - Y-axis: FREE VIRUS (log scale, from 10⁻⁵ to 10³) - Three curves show the free virus concentration over time. The curve for V₀ = 10⁻⁶ (asterisk) rises slowest, followed by V₀ = 10⁻⁴ (square), and V₀ = 10⁻² (circle) rises fastest, all eventually plateauing at a high level (around 10³). Top-right plot: - Y-axis: UNINFECTED T4 CELLS (linear scale, from 500 to 1000) - Three curves show the number of uninfected T4 cells over time. The curve for V₀ = 10⁻⁶ (asterisk) drops slowest, followed by V₀ = 10⁻⁴ (square), and V₀ = 10⁻² (circle) drops fastest, all eventually plateauing at a low level (around 500). Bottom-left plot: - Y-axis: LATENTLY INFECTED T4 CELLS (log scale, from 10⁻⁵ to 10³) - Three curves show the latently infected T4 cells over time. The curve for V₀ = 10⁻⁶ (asterisk) rises slowest, followed by V₀ = 10⁻⁴ (square), and V₀ = 10⁻² (circle) rises fastest, all eventually plateauing at a high level (around 10³). Bottom-right plot: - Y-axis: ACTIVELY INFECTED T4 CELLS (log scale, from 10⁻⁷ to 10¹) - Three curves show the actively infected T4 cells over time. The curve for V₀ = 10⁻⁶ (asterisk) rises slowest, followed by V₀ = 10⁻⁴ (square), and V₀ = 10⁻² (circle) rises fastest, all eventually plateauing at a high level (around 10¹).::>

<a id='e79841c5-5e1d-4cd0-ba0e-48d22869ba83'></a>

using the parameters in Table 2. The effects of changing the parameters
r, k₁, and μr, which are all quite different than in Table 1, were studied
using AUTO. All parameters were set at the default vaues given in
Table 2 except N. Examining Figure 9 for the transcritical bifurcation
[62] obtained with these parameters, one notes that the endemically
infected state that became stable at N = N_crit = 502 loses its stability at
a slightly larger value of N and then regains its stability at N ≈ 1229.
Oscillations arise via a Hopf bifurcation when the endemically infected
state becomes unstable (light curve in Figure 9). In order to determine
the boundary in parameter space for oscillations, we trace one of the
two Hopf bifurcations (the upper one at N = 1229.34), varying r and μ_T
simultaneously in Figure 10a. The region in which oscillations are found
is indicated. At the boundaries of the region, the endemically infected
steady state changes stability via a Hopf bifurcation. Thus, for example,
for μ_T = 0.1 day⁻¹ at r = 1.04, there is a Hopf bifurcation giving birth to

<!-- PAGE BREAK -->

<a id='82caeca5-6201-4845-817e-59bdba12b8bb'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='213f457e-8ecf-48c6-a138-206c4575a6df'></a>

107

<a id='fb302e07-1bbd-4f2a-8537-dae217198639'></a>

<::chart: The figure displays four plots illustrating the dynamics of a system. All plots share the x-axis labeled "YEARS" ranging from 0 to 3.0. The top-left plot shows "FREE VIRUS" on a logarithmic y-axis (from 10^-8 to 10^2), starting low, increasing, and then exhibiting sustained oscillations. The top-right plot shows "UNINFECTED T4 CELLS" on a linear y-axis (from 0 to 1600), starting high, decreasing sharply, and then showing sustained oscillations with sharp drops. The bottom-left plot shows "LATENTLY INFECTED T4 CELLS" on a logarithmic y-axis (from 10^-11 to 10^4), starting low, increasing, and then displaying sustained oscillations. The bottom-right plot shows "ACTIVELY INFECTED T4 CELLS" on a logarithmic y-axis (from 10^-11 to 10^1), starting low, increasing, and then exhibiting sustained oscillations.::>FIG. 8. Dynamics of the system with parameters set in the oscillatory region given in Table 2.

<a id='994d0289-71a0-4292-ac85-8e50d64c501a'></a>

a stable limit cycle. For smaller values of _r_ the infected steady state is stable. If one fixes _r_, say, at _r_ = 10 day⁻¹, and varies μ_τ_, one finds that for small values of μ_τ_ the infected state is stable; it then loses stability by a Hopf bifurcation at μ_τ_ ≈ 6.1×10⁻² and then goes stable again via a second Hopf bifurcation at μ_τ_ ≈ 0.146. Thus, there are two stable regions for the infected steady state, and in between lies a region of oscillatory behavior.

<a id='e9de4fb6-012c-42a3-bb91-d9c21796febe'></a>

Because k₁ is also important in determining the stability of the endemically infected state, we trace the Hopf bifurcations, varying k₁ and μτ simultaneously (Figure 10b), and k₁ and r simultaneously (Figure 10c). As in Figure 10a, the curves in these diagrams delimit the region where we find oscillatory behavior from the region where the infected state is stable. We have also studied the size of the region with oscillatory behavior as a function of the other parameters. First, if parameters that are part of N_crit are changed such that N_crit is increased

<!-- PAGE BREAK -->

<a id='99c4ba58-d8fb-4d7e-82a4-9182c43ce152'></a>

108

<a id='f7cfc3be-b06e-4c97-aa12-3edcc7a410a2'></a>

ALAN S. PERELSON ET AL.

<a id='c5252c5f-9a89-41ee-83eb-1d7c3f063ddb'></a>

<::A 2D line graph with N on the x-axis and T on the y-axis. The x-axis ranges from 0 to 1500, with major ticks at 500, 1000, and 1500. The y-axis ranges from 0 to 2500, with major ticks at 1000 and 2000. The plotted line shows a constant value of T approximately 1400 from N=0 up to N approximately 500. At N approximately 500, the line drops sharply to T approximately 0, and then remains at T approximately 0 for N values up to 1500. There are also faint vertical and horizontal grid lines at N approximately 500 and T approximately 1400 respectively.: chart::>

<a id='e00798c0-c905-458d-88e8-41c1fd47191a'></a>

FIG. 9. Transcritical bifurcation. The steady-state values of T are plotted versus N. Stable steady states are indicated by dark heavy lines, unstable steady states by light lines. Parameter values are given in Table 2. For N < N_crit = 502, the uninfected steady state with T = 1000 is stable. At N = N_crit, this state loses its stability and the endemically infected state with T a decreasing function of N becomes stable. This state quickly loses its stability at a Hopf bifurcation and then regains stability at a second Hopf bifurcation at N = 1229.34.

<a id='b1bb62e4-7877-41a5-8a9b-2b11834f6219'></a>

to the point N< N_crit, the uninfected state will become stable via the
transcritical bifurcation and oscillations will cease. This is, for instance,
the case for large values of μ_v and μ_τ. Second, changing parameters
may increase or decrease the size of the region with oscillatory behav-
ior. Since this region may shrink and disappear entirely as a function of
the other parameters, they are as important as k₁, r, and μ_τ in
determining whether or not oscillatory behavior occurs. In no case have
we found oscillations in a region of parameter space that we consider
biologically realistic. The existence of oscillations in a model of this type
is not novel. Anderson and May [4] also find oscillatory or chaotic
fluctuations in a dynamical model of the interaction of HIV with the
immune system. However, they do not discuss the biological implica-
tions of the parameters needed to obtain oscillations nor do they map
out the regime in parameter space where oscillations ensue.

<a id='beeb47fe-ed09-4c5f-90b5-67c1526f184f'></a>

7. VIRAL INFECTION OF T-CELL PRECURSORS
HIV may be able to infect cells in the thymus and bone marrow and
thus lead to a reduced production of new immunocompetent T cells. In

<!-- PAGE BREAK -->

<a id='250abd31-5401-4b2a-8a10-6c3749d334ba'></a>

109

<a id='e7dc4676-fb08-4a3b-821d-6290c2b4f85e'></a>

HIV INFECTION OF CD4⁺ T CELLS
<::chart: (a) A 2D plot with μ_T on the y-axis (ranging from 0.00 to 0.20) and r on the x-axis (ranging from 0 to 50). A region labeled "Oscillations" is shown, bounded by a horizontal line at μ_T = 0.15 and a curve that starts at μ_T ≈ 0.15 at r=0 and decreases as r increases, reaching approximately μ_T ≈ 0.04 at r=50.::>
<::chart: (b) A 2D plot with μ_T on the y-axis (ranging from 0.00 to 0.15) and k₁ on the x-axis (ranging from 0.0 to 10.0). A region labeled "Oscillations" is shown, bounded by a horizontal line at μ_T = 0.15 and a complex curve below it. This lower boundary curve starts at μ_T ≈ 0.04 at k₁=0, rises sharply to μ_T ≈ 0.15 at a very small k₁ value, then drops sharply to μ_T ≈ 0.03, and subsequently gradually rises to approximately μ_T ≈ 0.08 at k₁=10.0.::>

<a id='27d80699-1c52-4998-aa57-560dd589d7be'></a>

FIG. 10. Mapping the region of oscillatory behavior in parameter space. The solid curve indicates the boundary of stability for the infected steady state. As parameters are varied, the state goes unstable and then regains its stability via Hopf bifurcations. In the unstable region, the infected steady state is surrounded by a stable limit cycle. Region of oscillation in the (a) μ₁r plane; (b) μ_r k₁ plane; (c) k₁r plane. Parameters not varied are given in Table 2, except N = 1229.34.

<!-- PAGE BREAK -->

<a id='1b18b9e5-0d0b-493f-a4e8-4597034dccb9'></a>

110

<a id='68197101-9184-4564-b194-f3df68f1e8cb'></a>

ALAN S. PERELSON ET AL.

<a id='a6aa1590-fe02-42ba-b1d9-873d782e37df'></a>

<::log-log plot: The x-axis is labeled 'r' and ranges from 10^-1 to 10^1. The y-axis is labeled 'k1' and ranges from 10^-2 to 10^2. A closed curve defines a region in the center labeled 'Oscillations'. (c) FIG. 10 (Continued)::>

<a id='faf75e59-c4f8-43e4-beb8-30ea276c6c14'></a>

the mouse, CD4 has been shown to be expressed on the earliest thymic
T-precursor cells [64]. Whether this is the case in humans has only been
speculated about. We examine the consequences of precursor T-cell
infection by assuming that the source, s, in Equation (5a) is a decreas-
ing function of the viral load. Perelson [49] assumed s(v) = se^(-̑̑̑v), where
̑ is a constant. Here, to avoid solving transcendental equations to find
the steady state, we shall assume that

<a id='eac3d3f1-eb85-48d2-a1e4-41a29fac85c6'></a>

s(v) = θs/(θ + v). (29)

<a id='4e5ac315-c823-40c8-9671-52ba46f76638'></a>

If _v_ = 0, then _s_ is a constant as in Equation (1). However, if the viral load increases to the point that _v_ = 0, then _s_ is decreased to half its normal value.

<a id='db24b8e8-5736-47a4-a2d2-61c8d31eaf38'></a>

Replacing _s_ by _s_(_v_), Equations (5) still have two steady states—an uninfected state and an endemically infected state. In the endemically infected state, _T_, _T_*, and _T_** are still given by Equations (13a)–(13c). However, V is now given by the one positive solution of

<a id='64d1b5d1-f9a3-491e-8a25-9602a2be7381'></a>

V^2[k_1 μ_ν(α + βμ_ν)] + V[θk_1 μ_ν(α + βμ_ν) – ραμ_ν + γμ_ν^2]
– θ[sα^2 + ραμ_ν – γμ_ν^2] = 0. (30)

<a id='d9bbab45-24f8-4a1b-b188-7c16ee3968d2'></a>

To see that there is only one positive solution, note that in the limit of

<!-- PAGE BREAK -->

<a id='35032c2b-d7da-4a95-9e36-30783cb0e807'></a>

HIV INFECTION OF CD4⁺ T CELLS 111
large θ we can ignore the terms not proportional to θ in Equation (30).
Thus,

<a id='542f52fc-e2e9-45e3-8186-8925e568ba73'></a>

$\bar{V} = \frac{s\alpha^2 + \rho\alpha\mu_v - \gamma\mu_v^2}{k_1 \mu_v (\alpha + \beta\mu_v)}$ (31)

<a id='0f8f2eb8-4e40-44d1-b362-e7187a7a3796'></a>

This is the result that we obtained previously, when s was constant [see
Eq. (13d)]. Further, as we showed previously, if N > Ncrit, then V in (31)
is positive. Thus, for N > Ncrit, the last term in (30) is negative. The first
term is positive. Thus, regardless of whether the middle term is positive
or negative, Equation (30) always has one sign change. Consequently, by
Descartes' rule of signs, there will be only one positive root. Thus the
effect of replacing s by s(v) will be quantitative, not qualitative.
However, as we show below, our model with infection of T-cell precur-
sors gives more realistic predictions for the time course of T-cell
depletion.

<a id='c10074bb-9ec5-40be-92ab-862bc9429522'></a>

Figure 11 shows a numerical solution of Equations (5) with s replaced by s(v), using the standard parameters (Table 1) with \u03b8 = 1 mm\u207b\u00b3. The depletion of uninfected cells is now more gradual than in Figures 2, 3, and 5\u20137. With N = 1000, depletion takes about 4 years. Further, the fraction of latently infected cells now remains on the order of 1% or less, as is seen in AIDS patients [51, 55], and the fraction of actively infected cells is less than 2\u00d710\u207b\u2074, consistent with the observations of Harper et al. [24]. Thus this version of the model makes predictions that are consistent with a number of quantitative observations. The one feature that it does not match is the ultimate degree of T-cell depletion, which in AIDS patients commonly decreases below 200 mm\u207b\u00b3. Further modifications of the model that might correct this deficiency are presented in Section 10.

<a id='96afd321-9053-4d21-8f46-b9e4e0900a07'></a>

8. EFFECTS OF AZT

One of the most successful treatments for AIDS involves the admin-
istration of drugs, such as azidothymidine (AZT), that can block viral
replication. The effects of such a drug can easily be understood within
the context of our model.

<a id='0c35cb52-9788-4ce5-8e3b-01c9c46c3a99'></a>

The effects of AZT are both dosage-dependent and HIV strain-de-
pendent [35]. Assume that at some time τ AZT is administered and
causes a block of viral replication. If viral replication is completely
blocked, then for times t > τ, N = 0. However, because AZT becomes
cytotoxic at high doses, partial blockage is the more likely outcome of
AZT treatment. Thus, we assume that for times t > τ, N = N', where
N' < N. If, before drug administration, N < N_crit, then the virus would

<!-- PAGE BREAK -->

<a id='651e44fb-7124-48c5-8e3f-fa6a32ca4400'></a>

112 ALAN S. PERELSON ET AL. <::chart: The figure displays four line graphs arranged in a 2x2 grid, illustrating viral infection of T-cell precursors. The x-axis for all graphs is "YEARS" from 0 to 10. There are three data series in each graph, representing different values of N: N=1000 (*), N=1200 (□), and N=1400 (○).

**Top Left Plot: FREE VIRUS**
- The y-axis is logarithmic, ranging from 10⁻⁵ to 10². 
- All three curves show an initial rise, then plateau. The N=1000 curve plateaus at the lowest level, followed by N=1200, and N=1400 at the highest level (around 10¹).

**Top Right Plot: UNINFECTED T4 CELLS**
- The y-axis is linear, ranging from 500 to 1000.
- All three curves start at 1000 and decrease over time. The N=1000 curve shows the steepest decline to the lowest plateau (around 550). The N=1200 curve declines to an intermediate plateau (around 650), and the N=1400 curve declines to the highest plateau (around 750).

**Bottom Left Plot: LATENTLY INFECTED T4 CELLS**
- The y-axis is logarithmic, ranging from 10⁻⁵ to 10¹.
- All three curves show an initial rise, then plateau. The N=1000 curve plateaus at the lowest level, followed by N=1200, and N=1400 at the highest level (around 10⁰).

**Bottom Right Plot: ACTIVELY INFECTED T4 CELLS**
- The y-axis is logarithmic, ranging from 10⁻⁷ to 10⁻¹.
- All three curves show an initial rise, then plateau. The N=1000 curve plateaus at the lowest level, followed by N=1200, and N=1400 at the highest level (around 10⁻²).

FIG. 11. Viral infection of T-cell precursors. The same model as in Figure 4 is illustrated, except here the source term s decreases with the viral load according to Equation (29) with θ=1 mm⁻³. Parameters are as in Table 1; N_crit = 774 and N=1000 (*), 1200 (□), 1400 (○).::>


<a id='bbbeb328-06aa-4680-b172-bcf247935108'></a>

be declining ($dV/dt < 0$) and the drug would simply hasten its elimina-
tion. In such cases the drug may not be needed. However, if $N > N_{crit}$
before treatment, the virus would have been growing, as would the
populations of infected T cells. After drug treatment, if $N' < N_{crit}$, then
$V, T^*$, and $T^{**}$ would all decline and, assuming that the virus had not
affected the thymus or T-cell precursors, $T$ would eventually recover to
its initial value $T_0$. This is illustrated in the upper right panel of Figure
12 (curves marked with circles). If AZT is given in low doses, then even
after treatment $N$ may be larger than $N_{crit}$, so that only partial recovery
of the T-cell population occurs (curves with open squares in Figure 12).
Partial recovery may also occur if thymic or bone marrow infection
occurred or if AZT affected the stem cells responsible for the genera-
tion of new T cells. Under such circumstances the source of new cells, $s,$

<!-- PAGE BREAK -->

<a id='bdb1ad01-4481-4de1-8cc6-0031dacdb211'></a>

113

<a id='a4b02303-8d39-495a-8dff-5e76b09e4df8'></a>

HIV INFECTION OF CD4$^+$ T CELLS
<::A line graph titled "HIV INFECTION OF CD4$^+$ T CELLS" displays three curves representing free virus concentration over time. The y-axis is labeled "FREE VIRUS" on a logarithmic scale from 10^-5 to 10^2. The x-axis is labeled "YEARS" from 0 to 10.
- The first curve, marked with solid circles/asterisks, shows free virus concentration rising from below 10^-3 at year 0 to approximately 10^1 by year 3, then stabilizing at that level until year 10.
- The second curve, marked with open squares, also rises from below 10^-3 at year 0 to approximately 10^1 by year 3, but then decreases to a stable level around 10^0 from year 4 to year 10.
- The third curve, marked with open circles, shows an initial rise from below 10^-3 at year 0 to approximately 10^1 by year 3, followed by a sharp decline to below 10^-5 by year 6.
: chart::>

<a id='12a4054f-8ff4-4cb7-a5a8-c6980165c5ea'></a>

<::Line graph showing the number of uninfected T4 cells over time in years. The Y-axis is labeled "UNINFECTED T4 CELLS" and ranges from 500 to 1000. The X-axis is labeled "YEARS" and ranges from 0 to 10. There are three distinct lines on the graph: A line with circle markers starts at 1000 T4 cells at year 0, drops to approximately 600 T4 cells around year 3, then sharply rises back to 1000 T4 cells by year 4 and remains at that level. A line with square markers starts at 1000 T4 cells at year 0, drops to approximately 840 T4 cells around year 2, then rises to approximately 730 T4 cells by year 5 and remains constant. A line with asterisk/dot markers starts at approximately 600 T4 cells around year 3, drops slightly to approximately 550 T4 cells by year 5, and remains constant.::>

<a id='71858ced-317e-45a8-bbe2-50055fc718ae'></a>

<::chart: The figure displays two line graphs side-by-side, both showing cell counts over time in years. Both graphs have 'YEARS' on the x-axis, ranging from 0 to 10, and a logarithmic y-axis. The graphs illustrate the effects of AZT treatment. At time τ = 3 years, N is reduced from N = 1400 (*) to N = 1050 (□), that is, 75% of its original value, or to N = 350 (○), that is, 25% of its original value, to mimic the effects of AZT treatment. Here N_crit = 774, so N = 1050 is above N_crit, while N = 350 is well below N_crit. Parameters are as in Table 1.

Left Graph:
- Y-axis label: LATENTLY INFECTED T4 CELLS
- Y-axis range: 10^-5 to 10^2
- Three data series are plotted: one with '*' markers, one with '□' markers, and one with '○' markers.

Right Graph:
- Y-axis label: ACTIVELY INFECTED T4 CELLS
- Y-axis range: 10^-7 to 10^0
- Three data series are plotted: one with '*' markers, one with '□' markers, and one with '○' markers.::>

<a id='3508fff2-2aad-4e6a-8f6a-b98d9a4999ef'></a>

could be diminished, so that even after treatment and viral elimination
the T-cell population would establish a new steady state consistent with
a decreased value of _s_, as is typically the case after adult thymectomy.

<a id='7a3699b4-6125-45f7-9f1d-b86c0dac8422'></a>

## 9. QUASI-STEADY-STATE APPROXIMATION TO THE DYNAMICS

The total dynamical picture seems to naturally break up into three distinct time domains. In the first, virus rapidly binds to T cells. This corresponds to the rapid initial decay in the free virus population seen in Figure 4. Next, virus and infected T cells increase exponentially, and uninfected T cells maintain a population level close to To. In the last region, uninfected T cells decline in number, the virus and infected T-cell population growth slows, and steady state is established. In this

<!-- PAGE BREAK -->

<a id='51a85258-9d33-499b-a127-df799fc49b69'></a>

114

ALAN S. PERELSON ET AL.
section we approximate the dynamics in these regions and estimate the time intervals for each type of behavior. We also show how one can use a quasi-steady-state approximation to obtain either a one- or two- dimensional reduced description of the long-time behavior of the system.

<a id='02630a69-0107-441d-9596-a3163db9c831'></a>

9.1. EARLY TIME BEHAVIOR
Assume that the initial conditions are V(0) = V₀, T(0) = T₀, T*(0) = 0,
and T**(0) = 0, that is, that infection is by free virus. The earliest event
is the binding of virus to uninfected T cells. As can be seen in Figure 4,
this causes a rapid decrease in the concentration of free virus. We
estimate the depletion of free virus as follows.
Initially, and at early times, T(t)≈T₀ and T**(t)≈0. We use a
method of successive approximation to refine these estimates. Thus,
first assume that T = T₀ = constant, and T**(t) = 0. Equation (5d) then
becomes

<a id='1c0c58b9-4ea0-44ba-8672-627604e38607'></a>

$$\frac{dV}{dt} = -k_4V,$$

<a id='5c3e40c1-d979-47e9-9f08-ca278802af1d'></a>

where

k_4 = k_1 T_0 + \mu_V.

(32)

<a id='6578e750-a94f-417d-a2f0-eff2878ceea7'></a>

Hence virus decays exponentially according to

V(t) = V₀e⁻ᵏ⁴ᵗ.

(33a)

<a id='c59fccaf-14b6-42f3-b4c4-db66cac1e445'></a>

During this initial period some infection of T cells occurs. From
Equation (5a), with T = T₀,

dT/dt = s - μ_T T₀ + rT₀(1 - T₀) - k₁T₀V₀e^(-k₄t)
= -k₁T₀V₀e^(-k₄t)

<a id='2a1715bd-b0f3-485f-8d83-441ebd6ba8e0'></a>

with solution

$T(t) = T_0\left[1 - \frac{k_1 V_0}{k_4}(1 - e^{-k_4 t})\right].$ (33b)

<a id='afc47814-eb98-4d8a-9703-2f0ceea53ac4'></a>

If k₁V₀ << k₄, T(t) ≈ T₀. For the parameters used to generate Figure 4,
k₁V₀/k₄ ≈ 10⁻⁶, and hence there is no observable depletion of T cells.
From Equation (5b),

<a id='212e76d9-b21d-4dc8-af0d-d89c9966ed5a'></a>

dT*/dt = k1T0V0e^(-k4t) - k3T*,

<!-- PAGE BREAK -->

<a id='4437f698-b0e5-4f12-a6b9-5cb93a41999c'></a>

HIV INFECTION OF CD4$^{+}$ T CELLS 115

and thus

<a id='41a92b59-e8a7-4e68-b9f1-8ae2de96efbb'></a>

T*(t) = (k₁T₀V₀ / (k₄ - k₃)) (e^(-k₃t) - e^(-k₄t)). (33c)

<a id='df3c8fa7-edde-447b-8120-b6e56b192c39'></a>

From (5c) these latently infected cells can create actively infected cells. Substituting (33c) into (5c) and solving yields

<a id='c88f5214-42e2-4cfe-8840-592c15424974'></a>

T**(t) = (k₂k₁T₀V₀)/(k₄ - k₃) * (
  (e^(-k₄t))/(k₄ - μb) +
  (e^(-k₃t))/(μb - k₃) +
  ((k₄ - k₃)e^(-μbt))/((k₄ - μb)(μb - k₃))
)
(33d)

<a id='ad7648a5-a88a-40fc-a064-e185b9f63738'></a>

Substituting (33a) into (5d) for V(t), we find

<a id='e6aec122-0184-449d-829b-8ad814b9fc24'></a>

$$\frac{dV}{dt} = N\mu_b T^{**} - k_4 V_0 e^{-k_4 t}, \quad (34)$$

<a id='5c6ab724-88bd-40d8-8e69-74de908e8491'></a>

where T**(t) is given by (33d). Although this equation can be used to generate the next-order approximation to V(t), we shall use it to estimate the time at which V stops decreasing, that is, when dV/dt = 0. From Equation (34), this occurs at t = tmin, where tmin is the solution of the transcendental equation

<a id='8ae89a99-960f-4684-8e33-c753091dba32'></a>

(n\mu_b k_2 k_1 T_0 / (\mu_b - k_3)) * ((e^(-k_3 t) / (k_4 - k_3)) - (e^(- \mu_b t) / (k_4 - \mu_b)))

<a id='56802e1d-64e1-4683-b398-83b3d0d932e5'></a>

$$-\left(k_4 - \frac{N\mu_b k_2 k_1 T_0}{(k_4 - k_3)(k_4 - \mu_b)}\right)e^{-k_4 t} = 0. \quad (35)$$

<a id='a219547f-df8c-43b8-976a-e84ab6645579'></a>

Further, at $t_{min}$,

<a id='232b9173-a3e3-4cee-9595-cb65baa98461'></a>

V = V_min = V_0e^-k_4t_min . (36)

<a id='374b58e8-9b15-4ab8-8a17-3011b5ca395d'></a>

Evaluating $t_{min}$ and $V_{min}$ for the parameters used to generate Figure 4,
we find that with $N = 1000$, $t_{min} = 2.3$ days and $V_{min} = 4.2\times10^{-6}$. Solving the full system (5) numerically for the same parameters gives
$t_{min} = 2$ days and $V_{min} = 3\times10^{-5}$. These approximations are sufficiently
accurate for our purposes and show that the initial decrease in $V$ due to
the binding and infection of T cells is quite rapid.

<a id='f679f141-de79-4897-8e42-28b378afa3a9'></a>

9.2. MIDTERM AND LONGTERM BEHAVIOR

In Figure 2, one immediately obvious feature is that the T**(t),
T*(t), and V(t) curves all look similar. This motivates us to use a

<!-- PAGE BREAK -->

<a id='97a9d80d-ee46-42af-b38c-6c45cfe94932'></a>

116
ALAN S. PERELSON ET AL.

quasi-steady-state analysis to simplify the system. Due to rapid absorp-
tion by CD4$^+$ cells, we expect that after a fast transient, the level of
free virus will be well approximated by its quasi-steady-state level.
Similarly, actively infected cells equilibrate rapidly with latently infected
cells. Assuming that on a long time scale $dT^{**}/dt = dV/dt = 0$ leads
to the algebraic equations

<a id='a2388df4-d5e2-45cd-a832-9f3a12b2aee5'></a>

T** = k2T* / b (37)

<a id='d6e18448-7757-4af2-a660-cf3b73f189ee'></a>

and

<a id='3da18e79-3147-44b7-9dd7-de47db759258'></a>

V = Nk₂T* / (k₁T + μv).                                    (38)

<a id='0c23a4b7-f8e8-4260-8f86-278fbcb556fe'></a>

Substituting into Equations (5a) and (5b) leads to

<a id='c428548a-cdc3-476a-be12-941ac18dd310'></a>

$\frac{dT}{dt} = s + pT - \gamma T^2 - \left(k_3\beta + \frac{Nk_1k_2}{k_1T + \mu_v}\right)TT^*$, (39a)

$\frac{dT^*}{dt} = \frac{Nk_1k_2}{k_1T + \mu_v}TT^* - k_3T^*$. (39b)

<a id='6ed640fd-3483-4e91-9d1e-1777899369ea'></a>

The solution of this two-differential-equation model is shown in Figure 13. As initial conditions we used T(0) = T₀ and computed T*(0) from Equation (33c) evaluated at t = tmin. Comparing with Figures 2 and 3, one notices that the solutions are very similar to the solutions of the full system of equations, (5a)-(5d), although there is a detectable difference in the time needed to reach steady state.

<a id='a86182ff-b114-4c76-b8e9-9d1aceccecdb'></a>

The two-equation model can be studied by the usual methods of phase-plane analysis. Figure 14 shows the nullclines of Equations (39a) and (39b) for N=600 and N=1400. When dT*/dt = 0, T* = 0 or T = constant = k3 μv/(Nk1k2 - k3k1). These nullclines are indicated by the straight heavy lines in Figure 14. The lighter curved line is the locus of points along which dT/dt = 0. Notice that for N < Ncrit, Figure 14a the two nullclines only intersect at T = 1000, T* = 0, the uninfected state. When N> Ncrit, in addition to this uninfected state, there is a second intersection that corresponds to the endemically infected state. Thus, this phase plane summarizes the general features of the full four-equation model.

<a id='b6c6c5d8-b903-4082-9d6e-7efe26251bab'></a>

During the initial and middle phases of the infection, a good approxi-
mation to _T_ is _T_₀. Thus, during this period we can substitute _T_ = _T_₀
into (39b) and obtain

<a id='fb9bec59-c7d2-41f1-85b7-9eec2dbbc72d'></a>

dT*
d-- = \u03b7T*,
dt

(40)

<!-- PAGE BREAK -->

<a id='fda854f1-23cf-43b8-aa7a-afe3a07cae1f'></a>

HIV INFECTION OF CD4+ T CELLS<::Line graph titled "HIV INFECTION OF CD4+ T CELLS". The y-axis is labeled "FREE VIRUS" and uses a logarithmic scale from 10^-5 to 10^3. The x-axis is labeled "YEARS" and ranges from 0 to 10. Three distinct lines are plotted: 1. A line marked with circles starts at approximately 10^-5 at year 0, rises sharply, and plateaus around 10^3 by year 2-3. 2. A line marked with squares starts at approximately 10^-5 at year 0, rises sharply, and plateaus around 10^3 by year 4-5. 3. A line marked with solid circles starts at approximately 10^-5 at year 0, rises more gradually than the other two lines, and plateaus around 10^2-10^3 by year 7-8.: chart::>

<a id='447739b6-3fa4-42a1-8293-04d9808c058f'></a>

117
<::Line chart showing Uninfected T4 Cells over Years.
The Y-axis is labeled "UNINFECTED T4 CELLS" and ranges from 500 to 1000.
The X-axis is labeled "YEARS" and ranges from 0 to 10.
There are three distinct curves:
- The first curve, marked with circles, starts at 1000 cells, drops sharply between year 2 and 3, and stabilizes at approximately 550 cells from year 3 onwards.
- The second curve, marked with squares, starts at 1000 cells, drops sharply between year 3 and 4, and stabilizes at approximately 650 cells from year 4 onwards.
- The third curve, marked with filled circles, starts at 1000 cells, drops more gradually between year 5 and 7, and stabilizes at approximately 780 cells from year 7 onwards.
: chart::>

<a id='1534d579-da11-43d5-90a3-1d0ab6dfceda'></a>

<::chart: Two line graphs displayed side-by-side. Both graphs share the same x-axis labeled "YEARS", ranging from 0 to 10. The legend for the curves applies to both graphs: N = 1000 (*), 1200 (◻), 1400 (○). The curves represent solutions of Equations (39) for T and T*, with T(0) = 1000 and T*(0) given by (33c) with t = tmin. The algebraic equations (37) and (38) were used to determine T** and V. Parameters are as in Table 1. Left Graph: Y-axis is labeled "LATENTLY INFECTED T4 CELLS" on a logarithmic scale from 10^-5 to 10^3. Three curves are shown, each starting near 10^-5 and increasing over time to plateau around 10^2. The curve for N = 1400 (○) rises fastest, followed by N = 1200 (◻), and then N = 1000 (*), which rises slowest. Right Graph: Y-axis is labeled "ACTIVELY INFECTED T4 CELLS" on a logarithmic scale from 10^-7 to 10^1. Three curves are shown, each starting near 10^-7 and increasing over time to plateau around 10^0. Similar to the left graph, the curve for N = 1400 (○) rises fastest, followed by N = 1200 (◻), and then N = 1000 (*), which rises slowest.::>FIG. 13. The quasi-steady-state approximation. Illustrated is the solution of Equations (39) for T and T*, with T(0) = 1000 and T*(0) given by (33c) with t = tmin. The algebraic equations (37) and (38) were used to determine T** and V. Parameters are as in Table 1; N = 1000 (*), 1200 (◻), 1400 (○).

<a id='a7eddd94-b1c3-422e-9fce-9e92c7a21460'></a>

where

η = (Nk1k2T0 / (k1T0 + μv)) - k3 = k3(N - Ncrit) / Ncrit . (41)

From this we predict

T*(t) = T0*e^ηt, (42)

<a id='025215ba-3f2a-429a-b6c6-5e32ecba804b'></a>

where T₀* is determined by matching with a fast-time solution. The time scale 1/η depends on the difference between N and N_crit. Thus, as seen in the simulations, the infection is slow when N is near N_crit and becomes fast as N increases. Substituting (42) into (38) with T = T₀

<!-- PAGE BREAK -->

<a id='80209a06-fb1f-4193-b451-d7ff486027e4'></a>

ALAN S. PERELSON ET AL.

<a id='7b851661-5f35-4b81-894a-6a0d95f04d92'></a>

118

<::A line graph titled (a). The y-axis is labeled T* and ranges from 0 to 250, with major ticks at 0, 125, and 250. The x-axis is labeled T and ranges from 0 to 150, with major ticks at 0, 750, and 150. A curve starts from the top left corner (T*=250) and decreases, approaching the x-axis around T=750. There is also a thick vertical line at the right edge of the plot area and a thick horizontal line at the bottom edge of the plot area.
: line graph::>

<a id='9b0b1d9b-0c91-4bf7-833e-0e4081549a06'></a>

<::A 2D plot labeled (b). The y-axis is labeled T* and ranges from 0 to 250. The x-axis ranges from 0 to 1500. A curve starts near T*=250 at x=0 and decreases exponentially towards T*=0 as x increases. A thick vertical line is drawn at approximately x=650, and a thick horizontal line is at y=0. The plot is enclosed in a square frame.: chart::>

<a id='eaefa8db-a7ee-4382-b331-3e28ef1d05ba'></a>

FIG. 14. Nullclines of the reduced two-equation model (39a) and (39b) for (a) N = 600 and (b) N = 1400. Other parameters are as in Table 1. The light curved line is the $dT/dt = 0$ nullcline, while the two heavy straight lines are the $dT*/dt = 0$ nullclines. Note that for $N < N_{crit}$, (a), the nullclines intersect only at the uninfected state $T = 1000$, $T* = 0$, while for $N > N_{crit}$, (b), there is a second intersection corresponding to the endemically infected state.

<a id='74f49577-71e1-4abe-b16e-a204c1d5d9fa'></a>

yields

<a id='c065a0a0-aed2-47ce-851b-33023beefe0b'></a>

V(t) = V₀ⁱ e⁴⁵, (43)

<a id='e1188b09-6c22-470e-820d-40490ecdc98c'></a>

where $V_0^+ = Nk_2T_0^*/k_4$. Rather than using a formal matching procedure to find $T_0^*$, we can simply take $V_{min}$ as an approximation to $V_0^+$. 

<a id='4c16c07d-648c-4b46-9f49-45bfda0a26db'></a>

## 10. DISCUSSION
Starting from a description of T-cell population dynamics in a healthy individual, we have developed a dynamical model for T-cell depletion due to HIV infection. While our model is overly simple in that it does not account for the immune response to HIV infection or mechanisms of cell death other than direct HIV-mediated killing, it does demonstrate that HIV by itself can cause partial CD4$^{+}$ T-cell depletion in the face of normal T-cell replenishment. Further, the model demonstrates that the loss of T cells can take place on a time scale of years, as is characteristic of the disease process in most HIV-infected individuals.

<a id='5232f4d8-2e1e-4981-b1a5-9d08f63dea16'></a>

We considered two forms of the model. In the first, s, the rate of T-cell production from precursors, is constant. In this case we find that T-cell depletion begins between 3 and 6 years after infection and occurs over a period of 1-3 years depending on the value of N, the number of

<!-- PAGE BREAK -->

<a id='19ee820b-389f-4886-8e21-0afa476f31a8'></a>

119

<a id='b51b4b4f-f030-44dc-9a30-3453ad7321a1'></a>

HIV INFECTION OF CD4⁺ T CELLS 119
new virions produced by an infected CD4⁺ T cell (Figures 2 and 3). However, the number of latently infected cells grows to unrealistically high levels, where over 10% of the T cells are infected. Partially because the number of latently infected cells is so large, the depletion of total CD4⁺ T cells is not as dramatic as is seen in patients. The total number of T cells decreases from 1000 mm⁻³ to 830 mm⁻³ when _N_ = 1400 (Figure 3). Modifying the model so that _s_ decreases with increasing viral burden, mimicking the effects of infection of T-cell precursors, we obtain dynamics more reminiscent of clinical data. The onset of T-cell depletion is again delayed a few years from initial infection, but the depletion is now more gradual, taking between 3 and 5 years depending on the value of _N_ (Figure 11). Further, the depletion drives the T-cell count substantially lower, with _N_ diminishing from 1400 to approximately 550 mm⁻³ (Figure 11). More important, this depletion is accomplished with between 1 in a 100 and 1 in 1000 T cells latently infected and 1 in 10⁴ cells actively infected, precisely the numbers seen in AIDS patients [55]. Thus, with infection of CD4⁺ T cells as well as precursors, using what we consider to be reasonable parameter values, we obtain realistic kinetics and realistic levels of T-cell infection. However, we find that the T-cell level can be depleted only to a count of approximately 500 mm⁻³, not to the <200 mm⁻³ level seen in many AIDS patients.

<a id='2b53ac34-a29d-44d4-acae-455d709aee8d'></a>

Modifications of the model that include more realistic assumptions about the biology of HIV may correct this deficiency. By increasing N (Figure 5) or k₁ (not shown), more depletion can be obtained, but the rate of depletion becomes unrealistically rapid. This suggests, for exam-ple, that if N increases with time, rather than being constant, one may be able to attain more realistic levels of depletion on the correct time scale. Preliminary simulations (not shown) confirm this. A switch from slowly to rapidly replicating strains of virus, which is observed as HIV-infected patients progress from latent to active AIDS, would correspond to an increase in N with time. (Also, a decline in the potential to generate an immune response to HIV as the disease progresses would in some respects correspond to an increase in the effective value of N.) An increase in k₁ with time would correspond to the establishment of a more infectious mutant strain.

<a id='8511fed7-5a99-4b8f-b833-d772278bbdb5'></a>

One of the interesting predictions of our model is that N, the number of infectious viral particles produced per actively infected T cell, needs to be above some critical level, N_crit, for successful HIV infection. If N < N_crit, then the level of free virus will monotonically decrease and ultimately be eliminated. This decrease is due to the fact that virus binds and infects cells. If infected cells die without producing a sufficient number of viral progeny, the infection will not be sustained.

<!-- PAGE BREAK -->

<a id='aea5be1a-b56a-45d3-9b3a-42203e284266'></a>

120

<a id='6348d229-fa9f-449d-b5ad-b10e78084e8a'></a>

ALAN S. PERELSON ET AL.

<a id='7f6c49fe-60eb-43e8-ac8e-576f5b1e79d0'></a>

In this respect our model is similar to a classical epidemiological model in which infected individuals must infect at least a critical number of other individuals for an epidemic to occur [25]. As in epidemiological models, such as the Lajmanovich and Yorke [32] model for gonorrhea, we find that our model has two steady states, an uninfected steady state in which there is no virus present and no infected T cells, and an endemically infected steady state in which both virus and infected T cells are stably maintained. Because there is depletion in both the number of uninfected T cells and total number of T cells, we expect that immune function would be compromised in the endemically infected state and clinical symptoms of AIDS would appear. This is in agreement with the Walter Reed classification scheme for determining the stage of disease based on the CD4+ T cell cell count in the blood.

<a id='de461a70-c58b-4078-9ca2-3b6929b9c864'></a>

Experimental evidence supports our prediction of a critical value for N. Virus isolated from patients has been characterized as being "rapid/high" or "slow/low" [15, 45], where rapid/high indicates that the virus replicates rapidly in culture and shows a high level of reverse transcriptase activity. Slow/low virus exhibit low levels of reverse transcriptase activity and grows slowly. Fenyö et al. [15] find that some slow/low viruses could not be grown in activated peripheral blood mononuclear cells of normal donors. This lack of successful transmission did not seem to be dependent on the amount of virus introduced into the culture, as increasing the amount of infectious virus in the initial inoculum 50-fold had no effect. This lack of successful growth and the phenomenon's independence from the initial viral population size, V0, is precisely what our model predicts for viral strains with N<Ncrit. Further, as one would predict from our model, there is a correlation between the replication potential of a virus and the clinical condition of the patient from whom the virus originated. Thus, viruses isolated from patients with severe immunodeficiency tend to be rapid/high, whereas virus isolated from HIV-infected individuals with no or mild clinical symptoms tend to be slow/low [5, 6, 15]. In general agreement with these results, Tersmette et al. [59] found a significant correlation between the mean replication rate of viral isolates obtained from an individual and the rate of CD4+ cell decrease observed in this individual. In individuals with low-replicating strains, no significant CD4+ cell loss was observed, whereas recovery of high-replicating isolates was associated with rapid decline in CD4+ cell numbers and development of ARC or AIDS. Our current model considers only a single virus population. Clearly, to do a better job of modeling the differences between slow/low and rapid/high strains and the possible transitions between phenotype by mutation requires a model with

<!-- PAGE BREAK -->

<a id='605d7cc7-3ab4-46b3-9e9c-32b6b17d01bb'></a>

HIV INFECTION OF CD4+ T CELLS

<a id='54fc5822-6e42-4c59-8e3f-dd2728b11398'></a>

121

<a id='067b4fe5-2d6b-483a-b7e1-39183ae8bdc1'></a>

multiple HIV populations. Recent work by Nowak et al. [48] and Nowak
and May [47] points in this direction.

<a id='f5fe9731-2096-43a3-9405-52f3125b5303'></a>

From the model presented in this paper we conclude that HIV cytopathicity is a major factor in producing many of the quantitative features of HIV infection. Our model shows that HIV cytopathicity of both peripheral CD4+ T cells and their precursors gives rise to T-cell depletion, that it can account for the long latency from infection to symptomatic disease, and that it can account for the low levels of infected T cells seen in seropositive patients. However, infection and direct T-cell killing by a _single_ viral strain, as depicted in our model, is probably not the only factor involved in T-cell depletion. Changes in cytopathicity (i.e., increases in N or k₁ or a decrease in µy) due to the rapid mutation of HIV probably also contribute to the observed phenomenology. Further, the killing of uninfected T cells by other mechanisms, such as syncytium formation or autoimmune reactions, is not ruled out by our model. However, our results show that such mechanisms need not play a major role to get the observed quantitative phenomenology.

<a id='ad5a063d-0414-49de-b163-b609a28881ff'></a>

We thank George Nelson, Stephen J. Merrill, and James M. Hyman for critical comments and suggestions. We also thank George Nelson for technical assistance. This work was performed under the auspices of the U.S. Department of Energy and supported by the Center for Nonlinear Studies, Los Alamos National Laboratory, and the Santa Fe Institute through their Theoretical Immunology Program, as well as by grants from the University of California Universitywide Task Force on AIDS (R89LANL003) and the National Institutes of Health (AI28433 and RR06555).

<a id='8870e46b-6910-468c-8513-90be8b0c48d6'></a>

## REFERENCES

1.  T. Abo, T. Kawate, K. Itoh, and K. Kumagai, Studies on the bioperiodicity of the immune response. I. Circadian rhythms of human T, B, and K cell traffic in the peripheral blood, *J. Immunol.* 126:1360-1363 (1981).
2.  J. Albert, B. Abrahamsson, K. Nagy, E. Aurelius, H. Gaines, G. Nyström, and E. M. Fenyö, Rapid development of isolate-specific neutralizing antibodies and consequent emergence of virus variants which resist neutralization by autologous sera, *AIDS* 4:107-112 (1990).
3.  R. M. Anderson, Mathematical and statistical studies of the epidemiology of HIV, *AIDS* 3:333-346 (1989).
4.  R. M. Anderson and R. M. May, Complex dynamical behavior in the interaction between HIV and the immune system, in *Cell to Cell Signalling: From Experiments to Theoretical Models*, A. Goldbeter, Ed., Academic, New York, 1989, pp. 335-349.

<!-- PAGE BREAK -->

<a id='dd6da439-193c-459b-ae24-19533e854a09'></a>

122
ALAN S. PERELSON ET AL.
5 B. Åsjö, L. Morfeldt-Månson, J. Albert, G. Biberfeld, A. Karlsson, K. Lidman,
and E. M. Fenyö, Replicative capacity of human immunodeficiency virus from
patients with varying severity of infection, _Lancet_ ii: 660-662 (1986).
6 C. Cheng-Mayer, D. Seto, M. Tateno, and J. A. Levy, Biologic features of HIV-1
that correlate with virulence in the host, _Science_ 240:80-82 (1988).
7 L. N. Cooper, Theory of an immune system retrovirus, _Proc. Natl. Acad. Sci._
_U.S.A._ 83:9159-9163 (1986).
8 R. J. De Boer, _GRIND: Great Integrator of Differential Equations_, Bioinformatics
Group, Univ. Utrecht, The Netherlands, 1983.
9 E. J. Doedel, _AUTO: a program for the bifurcation analysis of autonomous_
systems, _Cong. Num._ 30:265-285 (1981).
10 J. Doležal and T. Hraba, Application of the mathematical model of immunologi-
cal tolerance to HIV infection, _Folio Biol. (Praha)_ 34:336-341 (1988).
11 A. S. Edelman, and S. Zolla-Pazner, AIDS: a syndrome of immune dysregula-
tion, dysfunction, and deficiency, _FASEB J._ 3:22-30 (1989).
12 H. N. Eisen, _Immunology_, 2nd ed., Harper and Row, Hagerstown, Md., 1980.
13 A. S. Fauci, Current issues in developing a strategy for dealing with the acquired
immunodeficiency syndrome, _Proc. Natl. Acad. Sci U.S.A._ 83:9278-9283 (1986).
14 A. S. Fauci, The human immunodeficiency virus: infectivity and mechanisms of
pathogenesis, _Science_ 239:617-622 (1988).
15 E. M. Fenyö, L. Morfeldt-Månson, F. Chiodi, B. Lind, A. v Grerfelt, J. Albert,
E. Olausson, and B. Åsjö, Distinct replicative and cytopathic characteristics of
human immunodeficiency virus isolates, _J. Virol._ 62:4414-4419 (1988).
16 J. E. Fletcher, R. I. Shrager, and J. J. Bailey, A kinetic model of T-lymphocyte
interactions with HIV, Preprint, 1988.
17 T. Folks, J. Kelly, S. Benn, A. Kinter, J. Justement, J. Gold, R. Redfield, K. W.
Sell, and A. S. Fauci, Susceptibility of normal human lymphocytes to infection
with HTLV-III/LAV, _J. Immunol._ 136:4049-4053 (1986).
18 A. A. Freitas, B. Rocha, and A. A. Coutinho, Lymphocyte population kinetics in
the mouse, _Immunol. Rev._ 91:5-37 (1986).
19 H. R. Gelderblom, E. H. S. Hausmann, M. Özel, G. Pauli, and M. A. Koch, Fine
structure of human immunodeficiency virus (HIV) and immunolocalization of
structural proteins, _Virology_ 156:171-176 (1987).
20 J. J. Goedert, R. J. Biggar, M. Melbye, D. L. Mann, S. Wilson, M. H. Gail, R. J.
Grossman, R. A. DiGioia, W. C. Sanchez, S. H. Weiss, and W. A. Blattner,
Effect of T4 count and cofactors on the incidence of AIDS in homosexual men
infected with human immunodeficiency virus, _JAMA_ 257:331-334 (1987).
21 S. D. Gowda, B. S. Stein, N. Mohagheghpour, C. J. Benike, and E. G. Engleman,
Evidence that T cell activation is required for HIV-1 entry in CD4+ lympho-
cytes, _J. Immunol._ 142:773-780 (1989).
22 D. Gray, T cell and B cell memory are short lived in the absence of antigen, _J._
_Cell. Biochem. Suppl._ 13A: C010 (1989).
23 D. Gray and T. Leanderson, Expansion, selection and maintenance of memory
B cell clones, _Curr. Topics Microbiol. Immunol._ 159:1-17 (1990).
24 M. E. Harper, L. M. Marselle, R. C. Gallo, and F. Wong-Stall, Detection of
lymphocytes expressing human T-lymphotropic virus type III in lymph nodes
and peripheral blood from infected individuals by in situ hybridization, _Proc._
_Natl. Acad. Sci U.S.A._ 83:772-776 (1986).

<!-- PAGE BREAK -->

<a id='aeb24d25-1dea-49cc-8e2b-a2a0df0ed37d'></a>

HIV INFECTION OF CD4+ T CELLS
123

25 H. W. Hethcote and J. A. Yorke, _Gonerrhea Transmission Dynamics and Control_ (Lect. Notes Biomath. Vol. 56), Springer-Verlag, New York, 1984.
26 D. D. Ho, R. J. Pomerantz, and J. C. Kaplan, Pathogenesis of infection with human immunodeficiency virus, _N. Engl. J. Med._ 317:278 (1987).
27 J. A. Hoxie, J. D. Alpers, J. L. Rackowski, K. Huebner, B. S. Haggarty, A. J. Cedarbaum, and J. C. Reed, Alterations in T4 (CD4) protein and mRNA synthesis in cells infected with HIV, _Science_ 234:1123–1127 (1986).
28 T. Hraba and J. Doležal, Mathematical model of CD4+ lymphocyte depletion in HIV infection, _Folio Biol. (Praha)_ 35:156–163 (1989).
29 T. Hraba, J. Doležal, and S. Čelikovsky, Model-based analysis of CD4+ lymphocyte dynamics in HIV infected individuals, _Immunibology_ 181:108–118 (1990).
30 N. Intrator, G. P. Deocampo, and L. N. Cooper, Analysis of immune system retrovirus equations, in _Theoretical Immunology, Part 2_, A. S. Perelson, Ed., Addison-Wesley, Redwood City, Calif., 1988, pp. 85–100.
31 R. Kiernan, J. Marshall, R. Bowers, R. Doherty, and D. McPhee, Kinetics of HIV-1 replication and intracellular accumulation of particles in HTLV-1 transformed cells, _AIDS Res. Hum. Retrovirus_ 6:743–752 (1990).
32 A. Lajmanovich and J. A. Yorke, A deterministic model for gonorrhea in a nonhomogeneous population, _Math. Biosci._ 28:221–236 (1976).
33 H. C. Lane and A. S. Fauci, Immunologic abnormalities in the acquired immunodeficiency syndrome, _Ann. Rev. Immunol._ 3:477–500 (1985).
34 H. C. Lane and A. S. Fauci, Infectious complications of AIDS, in _AIDS: Modern Concepts and Therapeutic Challenges_, S. Broder, Ed., Marcel Dekker, New York, 1987, pp. 185–203.
35 B. A. Larder, G. Darby, and D. D. Richman, HIV with reduced sensitivity to zidovudine (AZT) isolated during prolonged therapy, _Science_ 243:1731–1734 (1989).
36 S. P. Layne, J. L. Spouge, and M. Dembo, Quantifying the infectivity of HIV, _Proc. Natl. Acad. Sci. U.S.A._ 86:4644–4648 (1989).
37 R. Leonard, D. Zagury, I. Desportes, J. Bernard, J.-F. Zagury, and R. C. Gallo, Cytopathic effect of human immunodeficiency virus in T4 cells is linked to the last stage of virus infection, _Proc. Natl. Acad. Sci. U.S.A._ 85:3570–3574 (1988).
38 A. McLean, HIV infection from an ecological viewpoint, in _Theoretical Immunology, Part 2_, A. S. Perelson, Ed., Addison-Wesley, Redwood City, Calif., 1988, pp. 77–84.
39 A. R. McLean and T. B. L. Kirkwood, A model of human immunodeficiency virus infection in T helper cell clones, _J. Theor. Biol._ 147:177–203 (1990).
40 J. L. Malone, T. E. Simms, G. C. Gray, K. F. Wagner, J. R. Burge, and D. S. Burke, Sources of variability in repeated T-helper lymphocyte counts from human immunodeficiency virus type 1-infected patients: total lymphocyte count fluctuations and diurnal cycle are important, _J. AIDS_ 3:144–151 (1990).
41 J. B. Margolick, D. J. Volkman, T. M. Folks, and A. S. Fauci, Amplification of HTLV-III/LAV infection by antigen-induced activation of T cells and direct suppression by virus of lymphocyte blastogenic responses, _J. Immunol._ 138:1719–1723 (1987).
42 S. Merrill, AIDS: background and the dynamics of the decline of immunocompetence, in _Theoretical Immunology, Part 2_, A. S. Perelson, Ed., Addison-Wesley,

<a id='b9165f97-639a-4f9a-83fc-e4b7803eea64'></a>

petence, in Theoretical Immunology, Part
Redwood City, Calif., 1987, pp. 59-75.

<!-- PAGE BREAK -->

<a id='f4691084-c033-476e-80a5-2b9699e812f3'></a>

124                                                        ALAN S. PERELSON ET AL

<a id='6d984625-877a-4f0c-adf4-929cbf2dd4b0'></a>

43 S. Merrill, Modeling the interaction of HIV with cells of the immune response, in Mathematical and Statistical Approaches to AIDS Epidemiology (Lect. Notes Biomath., Vol. 83), C. Castillo-Chavez, Ed., Springer-Verlag, New York, 1989, pp. 371-385.
44 J. D. Murray, Mathematical Biology, Springer-Verlag, New York, 1989.
45 P. L. Nara, L. Smit, N. Dunlop, W. Hatch, M. Merges, D. Waters, J. Kelliher, R. C. Gallo, P. J. Fischinger, and J. Goudsmit, Emergence of viruses resistant to neutralization by V3-specific antibodies in experimental human immunodeficiency virus type 1 IIIB infection of chimpanzees, J. Virol. 64:3779-3791 (1990).
46 G. W. Nelson and A. S. Perelson, A mechanism of immune escape by slow-replicating HIV strains, J. AIDS 5:82-93 (1992).
47 M. A. Nowak and R. M. May, Mathematical biology of HIV infections: antigenic variation and diversity threshold, Math. Biosci. 106:1-21 (1991).
48 M. A. Nowak, R. M. May, and R. M. Anderson, The evolutionary dynamics of HIV-1 quasispecies and the development of immunodeficiency disease, AIDS 4:1095-1103 (1990).
49 A. S. Perelson, Modeling the interaction of the immune system with HIV, in Mathematical and Statistical Approaches to AIDS Epidemiology (Lect. Notes Biomath., Vol. 83), C. Castillo-Chavez, Ed., Springer-Verlag, New York, 1989, pp. 350-370.
50 A. Phillips, C. A. Lee, J. Elford, G. Janossy, M. Bofill, A. Timms, and P. B. A. Kernoff, Prediction of progression to AIDS by analysis of CD4 lymphocyte counts in a haemophilic cohort, AIDS 3:737-741 (1989).
51 M. C. Psallidopoulos, S. M. Schnittman, L. M. Thompson, M. Baseler, A. S. Fauci, H. C. Lane, and N. P. Salzman, Integrated proviral human immunodeficiency virus type 1 is present in CD4+ peripheral blood lymphocytes in healthy seropositive individuals, J. Virol. 63:4626-4631 (1989).
52 E. M. Purcell, Life at low Reynolds number, Am. J. Phys. 45:3-11 (1977).
53 R. R. Redfield, D. C. Wright, and E. C. Tramont, The Walter Reed staging classification for HTLV-III/LAV infection, N. Engl. J. Med. 314:131-132 (1986).
54 G. Reibnegger, D. Fuchs, A. Hausen, E. R. Werner, M. P. Dierich, and H. Wachter, Theoretical implications of cellular immune reactions against helper lymphocytes infected by an immune system retrovirus, Proc. Natl. Acad. Sci. U.S.A. 84:7270-7274 (1987).
55 S. M. Schnittman, M. C. Psallidopoulos, H. C. Lane, L. Thompson, M. Baseler, F. Massari, C. H. Fox, N. P. Salzman, and A. S. Fauci, The reservoir for HIV-1 in human peripheral blood is a T cell that maintains expression of CD4, Science 245:305-308 (1989).
56 S. M. Schnittman, J. J. Greenhouse, M. C. Psallidopoulos, M. Baseler, N. P. Salzman, and A. S. Fauci, Increasing viral burden in CD4+ T cells from patients with human immunodeficiency virus (HIV) infection reflects rapidly progressive immunosuppression and clinical disease, Ann. Int. Med. 113:438-443 (1990).
57 M. Somasundaran and H. L. Robinson, Unexpectedly high levels of HIV-1 RNA and protein synthesis in a cytocidal infection, Science 242:1554-1557 (1988).
58 J. M. G. Taylor, J. L. Fahey, R. Detels, and J. V. Giorgi, CD4 percentage, CD4 number and CD4:CD8 ratio in HIV infection: which to choose and how to use, J. AIDS 2:114-124 (1989).

<!-- PAGE BREAK -->

<a id='1a895c79-ad74-4e8f-a12f-bdd021a2c1a3'></a>

HIV INFECTION OF CD4+ T CELLS 125

59 M. Tersmette, R. A. Gruters, F. de Wolf, R. E. Y. de Goede, J. M. A. Lange, P. T. A. Schellekens, J. Goudsmit, H. G. Huisman, and F. Miedema, Evidence for a role of virulent human immunodeficiency virus (HIV) variants in the pathogenesis of acquired immunodeficiency syndrome: studies on sequential HIV isolates, _J. Virol._ 63:2118–2125 (1989).
60 G. Tindall and D. A. Cooper, Primary HIV infection, _AIDS_ 5:1–14 (1991).
61 L. Weiss, _The Cells and Tissues of the Immune System_, Prentice-Hall, Englewood Cliffs, N.J., 1972.
62 S. Wiggins, _Introduction to Applied Nonlinear Dynamic Systems and Chaos_, Springer-Verlag, New York, 1990.
63 J. L. Willems, _Stability Theory od Dynamical Systems_, Wiley, New York, 1970.
64 L. Wu, R. Scollay, M. Egerton, M. Pearse, G. J. Spangrude, and K. Shortman, CD4 expressed on earliest T-lineage precursor cells in adult murine thymus, _Nature_ 349:71–74 (1991).
65 J. A. Zack, S. J. Arrigo, S. R. Weitsman, A. S. Go, A. Haislip, and I. S. Y. Chen, HIV-1 entry into quiescent primary lymphocytes: molecular analysis reveals a labile, latent viral structure, _Cell_ 61:213–222 (1990).
<a id='20618cd0-ec11-4e99-9a23-39677be1915c'></a>

<::logo: Elsevier
NON SOLUS
ELZEVIER
This logo features a tree with two figures beneath it, and the text "NON SOLUS" on a banner, all rendered in black and white line art, with "ELSEVIER" in a serif font below.::>

<a id='2e7a418a-fee9-4a09-af5f-a111e997b986'></a>

Available online at www.sciencedirect.com

SCIENCE @ DIRECT

<a id='5ab25d7c-4d2c-4e8e-ab39-682fd4ef785f'></a>

===
Journal of
Theoretical
Biology
===
www.elsevier.com/locate/jtbi

<a id='cb3e30e5-d144-417d-93d4-ccb6f0a149bf'></a>

Journal of Theoretical Biology 227 (2004) 513–523

<a id='c8dbc350-b591-4e3e-8679-6ead3dc143bb'></a>

A mathematical model for chronic myelogenous leukemia (CML) and
T cell interaction

<a id='98e7de3a-2023-4e02-b093-9b5d8d2cb429'></a>

Helen Mooreª,*,¹, Natasha K. Liᵇ

ª *American Institute of Mathematics, 360 Portage Avenue, Palo Alto, CA 94306, USA*
ᵇ *Stanford University, Stanford, CA 94305, USA*

Received 19 February 2003; received in revised form 17 November 2003; accepted 18 November 2003

<a id='1f77c9f0-b551-4a57-ad91-a086954d2060'></a>

## Abstract

In this paper, we propose and analyse a mathematical model for chronic myelogenous leukemia (CML), a cancer of the blood. We model the interaction between naive T cells, effector T cells, and CML cancer cells in the body, using a system of ordinary differential equations which gives rates of change of the three cell populations. One of the difficulties in modeling CML is the scarcity of experimental data which can be used to estimate parameters values. To compensate for the resulting uncertainties, we use Latin hypercube sampling (LHS) on large ranges of possible parameter values in our analysis. A major goal of this work is the determination of parameters which play a critical role in remission or clearance of the cancer in the model. Our analysis examines 12 parameters, and identifies two of these, the growth and death rates of CML, as critical to the outcome of the system. Our results indicate that the most promising research avenues for treatments of CML should be those that affect these two significant parameters (CML growth and death rates), while altering the other parameters should have little effect on the outcome.

© 2003 Published by Elsevier Ltd.

<a id='532bb12a-ebae-498e-8925-f77bbdb63a00'></a>

Keywords: Cancer; Chronic myelogenous leukemia (CML); Differential equations; Dynamics; Latin hypercube sampling (LHS); Mathematical modeling; T cells

<a id='c2fb63bd-736f-49df-b3aa-896e1771f154'></a>

1.  **Introduction**

Chronic myelogenous leukemia (CML) is a a cancer that affects cells circulating in the blood system. The disease occurs in more than 1 out of 100 000 people per year, and makes up approximately 15% of all leukemias in adults (Faderl, et al., 1999, p. 164). The immune system is known to play an important role in the dynamics of CML (Sawyers, 1999), which is motivation for the work in this paper.

<a id='0adb2756-37b5-4c39-8cc9-e1adc520e077'></a>

In this paper, we propose a mathematical model for the human immune system's response to CML in a hypothetical patient. One major goal of this work is to identify promising directions for experimental research on treatments for patients with CML. Our model

<a id='8e9dbe72-5fb5-4e5e-b8bc-927cae975156'></a>

*Corresponding author. Tel.: 650-845-2072.
E-mail address: moore@aimath.org (H. Moore).

1Supported by National Science Foundation DMS Grant 0096135.

Abbreviations: AICD, activation-induced cell death; APC, antigen-presenting cell(s); CML, chronic myelogenous leukemia; HIV, human immunodeficiency virus; LHS, Latin hypercube sampling; MHC, major histocompatibility complex; 1 microliter (µl) = 10-61 = 1 cubic millimeter (mm³).

<a id='ff479949-1f73-49a7-a62a-a24499b631b0'></a>

0022-5193/$- see front matter  2003 Published by Elsevier Ltd.
doi:10.1016/j.jtbi.2003.11.024

<a id='49fe0962-481a-4c13-a340-4b5d5e98629c'></a>

consists of a system of three nonlinear ordinary differential equations. We consider rates of change for naive and effector T cell populations, as well as the CML cancer cell population. Parameter values are obtained from available experimental data and esti- mates, and the system is analysed for sensitivity to changes in the parameters. Our analysis reveals that changes in most parameters (such as naive and effector T cell death rates) have little effect on the long-term outcome of the system, whereas changes in two parameters, the CML cancer cell growth rate and natural death rate, result in significantly different outcomes of the system. See Section 8 below for the full set of conclusions.

<a id='96b47603-eac2-4b38-b2d4-e870832037a1'></a>

There is an extensive body of work which develops models of this type for the interaction of T cells with human immunodeficiency virus (HIV). Perelson and Nelson (1999) and Nowak and May (2000) have written detailed surveys of the main ideas developed through such models. Several other diseases with similar patho-gen–immune system interaction dynamics have been modeled in this way as well. These include tuberculosis (cf. Wigginton and Kirschner, 2001) and hepatitis B

<!-- PAGE BREAK -->

<a id='3ed4e79e-d844-41bc-9cd6-b07d3ace1054'></a>

514

<a id='756d4a03-3a7c-4faa-bfb5-898fd2215d1e'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513–523

<a id='e5d09dc5-db5b-42b0-8244-7de6a41f7ddc'></a>

(cf. Nowak et al., 1996). Early modeling of CML includes models of T cell precursors in the bone marrow (cf. Cronkite and Vincent, 1969; Rubinow, 1969; Rubinow and Lebowitz, 1975). A later mathematical model for CML created by Fokas et al. (1991) refined these models, and focused on the maturation and proliferation of the T cell precursors.

<a id='2bbb4d88-79f5-4476-b43e-11cd709ca0a9'></a>

## 2. Background and assumptions for the model

The two T cell populations included in our model are defined as follows: naive T cells, which, if specific to CML, could become activated; and effector T cells specific to CML, which are fully armed and capable of immediate action. Naive T cells are activated in the lymph tissues. If a a naive T cell is CML-specific, then it can bind to a peptide-MHC (major histocompatibility complex) pair on a professional antigen-presenting cell (APC). If costimulators are also present, the T cell will be retained, activated, and will proliferate. After up to 1 week of proliferation, the progeny differentiate into armed effector cells. These are then released into the blood and are capable of mounting an immune attack upon encountering CML antigen (without the need for costimulation).

<a id='7d828ef8-834c-4446-9545-67718cbdba56'></a>

These two categories (naive and effector) represent the major distinct types of behavior of T cells that we wish to capture in our model. In order to keep this model tractable, we do not consider other parts of the immune system's response, such as the populations of B lymphocyte cells or the levels of production of cytokines. Our working assumption is that these other responses correlate positively with the responses we do examine, although we do not hypothesize exactly what the correlation functions might be. Furthermore, in Kirschner and Webb's (1996, p. 370, footnote) model for T cell responses to HIV, they find no qualitative difference in outcome between a model with CD4+ and CD8+ T cells considered separately, and a model in which only the total population of T cells was considered. Therefore, we do not consider these populations separately in our model.

<a id='b6f5317e-f471-42a5-b3c7-fe9b8fea52c8'></a>

Our model is based in the circulatory blood system, since we wish to tie it as closely as possible to available data from blood samples. We include a source term for new T cells entering the circulatory blood from other compartments (such as the bone marrow, lymph nodes, and thymus). We also include the input of CML cells from outside the blood, in the growth term for CML. However, we assume that pre-existing cells entering and exiting the blood due to diffusion give net changes that are approximately zero. We also assume that the concentration of T cells in the circulatory blood is proportional to the concentration of T cells in other compartments. These are standard assumptions for a

<a id='9893f7d0-b011-4a95-9851-ede78ad593fa'></a>

system at or near equilibrium, and experimental support in the case of HIV appears in Haase et al. (1996) and Perelson et al. (1997).

<a id='b8cf0070-6cb4-40a3-b707-39b86ff69efb'></a>

In this model, the naive T cells come into contact with the APC in the lymph tissues. We assume that APC with antigen from CML cells are present in proportion to the number of CML cancer cells themselves. Therefore, in our model we use the populations of CML cells with a proportionality constant to represent the numbers of APC presenting CML antigen. The encounters of naive T cells with the APC are represented by a Michaelis-Menten saturation term, the third term on the right-hand side of Eq. (1). We use a saturating growth term to take into account the limitations of the immune response, due to the large numbers of APC presenting CML antigen which saturate the lymph, but the relatively few CML specific naive T cells (Janeway et al., 2001, pp. 295–318). Similar ideas were used in Perelson et al. (1993) and Kirschner and Panetta (1998).
We assume the effector T cells come into contact with CML cancer cells in the blood in a random fashion. Because the encounters take place in the blood, we use the “law of mass action”. which savs that the total

<a id='a2f6eb2e-b713-47af-adbf-da2df96acab6'></a>

Because the encounters take place in the blood, we use the "law of mass action", which says that the total number of encounters between members of the two populations is proportional to the product of the sizes of the two populations. See Edelstein-Keshet (1988) for more discussion of the law of mass action.

<a id='d17c8b2a-b6a0-4603-8c9c-2305ebcf82f2'></a>

Note that the use of deterministic equations means that our model is not expected to be accurate when the populations are relatively small (Freedman, 1980, pp. 3-4). Specifically, the model will not be very accurate in its predictions if the populations are so small (e.g., on the order of single cells) that the continuous rates are not good approximations for gain or loss terms.

<a id='bcf6b290-ea6e-4040-86f1-59678b930b70'></a>

The disease CML has three distinct phases: chronic,
accelerated, and blast. The chronic phase lasts the
longest, averaging 3–5 years in length. During this time,
cell counts grow steadily. The accelerated and blast
phases can last just a few months each, and are
characterized by more rapid increases in cell counts,
followed by death of the patient. Our model is intended
for the chronic phase, as the rapid changes in cell counts
during the accelerated and blast phases are not as well
quantified by data in the later phases, and treatments for
CML focus on the chronic phase. Also, the cancer cell
population is large enough during the chronic phase that
the law of mass action is valid for cell interactions in the
blood, and yet not so large that crowding of CML in the
bone marrow decreases the source rate of the naive T
cells (Stryckmans et al., 1977).

<a id='6de9ace2-6943-47c9-8d5a-405155248195'></a>

### 3. Details and explanation of the model

Let *t* represent time, measured in days. We consider the following populations of cells in the circulating

<!-- PAGE BREAK -->

<a id='ddf8c40d-5da9-408f-a7a7-02131834ef8e'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513–523

<a id='05fd0df2-3e6a-4bfd-b628-6a5e92a1ed36'></a>

515

<a id='1fbf1947-1ad2-4e4b-b5fa-9b73a69aa85f'></a>

blood system, measured as concentrations of cells per µl:
$T_n$ = naive T cells,
$T_e$ = effector T cells specific to CML,
$C$ = chronic myelogenous leukemia (CML) cancer cells.

<a id='5679b1d9-0944-4601-81e7-14a3d19a83fe'></a>

Each of the three cell populations is a function of time, _t_.
The naive T cell population consists of all naive T cells, both specific and non-specific for CML. The naive T cells either have not yet been exposed to professional APC presenting CML antigen, or else are not CML-specific. The effector T cells have differentiated from naive T cells upon activation by a professional APC peptide-MHC complex and costimulators.

<a id='5bce727e-fbf9-477b-ad3c-00cde527a5ef'></a>

The system of differential equations is given below,
followed by explanations of the terms:

dT_n / dt = s_n - d_nT_n - k_nT_n (C / (C + η)) (1)

dT_e / dt = α_n k_nT_n (C / (C + η)) + α_e T_e (C / (C + η))
- d_eT_e - γ_eCT_e, (2)

dC / dt = r_cC ln (C_max / C) - d_cC - γ_cCT_e. (3)

<a id='a3eeb53c-5778-47c5-8fff-4138c9948103'></a>

Each equation represents the rate of change, with
respect to time, of one of the cell populations. The
lowercase coefficients, or parameters (e.g., $s_n$, $\alpha_n$, and $r_c$)
are all taken to be constants. Later in this paper we vary
the parameter values, and examine the resulting changes
in the system.

<a id='9a7003b9-d035-4401-bf6d-952643f07a37'></a>

Fig. 1 below shows the cell population diagram for system (1)-(3).

<a id='3d71c5a6-e983-4d09-b858-41608011b07b'></a>

We assume the changes in populations due to
diffusion are approximately zero. That is, we assume
the numbers of pre-existing cells of each population that
diffuse into and out of the blood are approximately
equal. Thus, there are no terms in the equations for
diffusion of already-existing, mature cells into or out of
the blood.

<a id='6ac4c3ca-cb97-476b-8ce3-8f049c5ef64e'></a>

The first term on the right-hand side of Eq. (1) is a source term for _new T cells_ entering the blood system. We approximate this as a constant, _s_n, which is a reasonable approximation except during the last stages of CML, when crowding in the bone marrow could decrease the production of naive T cells. The second term is due to the natural attrition of _T_n cells in the absence of CML. The factor _d_n is the naive T cell death rate constant, which is equal to the reciprocal of the average lifespan of a _T_n cell, and can be thought of as roughly approximating the fraction of the _T_n population that is expected to die naturally in 1 day. The third term is a Michaelis-Menten term, and represents the change in the _T_n population due to encounters with CML antigen in the lymph. We use a Michaelis-Menten term to take into account the saturation effect of CML cells

<a id='5fd1fde6-786d-40dd-82b0-0bc15b45d11b'></a>

<::transcription of the content: diagram::>Fig. 1. Cell population diagram. The diagram illustrates the interactions between three cell populations: naive T cells (T_n), effector T cells (T_e), and cancer cells (C).  

**Naive T cells (T_n):**
- Receive input from "source s_n" (solid arrow).  
- Experience "natural death d_n T_n" (dashed arrow leading out).  
- Activate into effector T cells via "activation k_n T_n (C/(C+η))" (dashed arrow pointing to effector T cells).  

**Effector T cells (T_e):**
- Are recruited from an external source via "recruitment α_e CT_e" (solid arrow pointing in).  
- Undergo "growth α_e CT_e" (solid self-loop arrow).  
- Experience "natural death d_e T_e" (dashed arrow leading out).  
- Interact with cancer cells:  
  - Cause "death of T_e by C contact γ_e CT_e" (dashed arrow leading out from T_e, associated with interaction with C).  
  - Cause "death of C by T_e contact γ_c CT_e" (dashed arrow leading out from C, associated with interaction with T_e).  
- Interact with cancer cells via a dotted line without arrows, signifying 

<a id='7df4f737-8ff4-4404-b14a-228511b9d844'></a>

in the lymph nodes, as described earlier in Section 2. We assume CML antigen is present in proportion to the number of CML cells. The constant η is the standard half-saturation concentration in a Michaelis-Menten term. The constant k_n is the rate constant which makes k_n T_n C/(C + η) equal to the instantaneous rate of T_n loss due to encounters between naive T cells and CML antigen. While CML-specific T_n cells can become activated upon encountering CML peptides and costimulators on APC, they can also become anergic if they encounter CML antigen without costimulators. The state of anergy essentially inactivates these naive T cells, preventing later activation, even if they subsequently encounter APC with CML antigen and costimulators. Hence, we consider both activation and anergy as contributors to the loss term.

<a id='fe6a02a3-9002-4cb6-b60d-3682ae85a7e1'></a>

We now examine Eq. (2), which describes the rate of change for those effector T cells in the blood compart- ment which are specific to CML. The first term on the right-hand side is due to activation encounters between T_n and professional APC (presenting peptides from CML antigen), and comes from the naive T cells lost in Eq. (2). When a naive T cell becomes activated, it is retained in the lymph tissues and proliferates for several days. The newly-formed T cells then differentiate into

<!-- PAGE BREAK -->

<a id='70e1e491-3ed4-4c43-990f-11fb94da7a43'></a>

516

<a id='d31be142-2af3-42fa-9bb5-883fb6a8f740'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513-523

<a id='4f6943ac-2ea3-4540-8bc3-31cfc4a17637'></a>

Table 1
Parameter information
<table id="3-1">
<tr><td id="3-2">Param.</td><td id="3-3">Description</td><td id="3-4">Value</td><td id="3-5">Sampled range</td><td id="3-6">Units</td><td id="3-7">Reference</td></tr>
<tr><td id="3-8">Sn</td><td id="3-9">T source term</td><td id="3-a">0.073</td><td id="3-b">(0, 0.5)</td><td id="3-c">cells/µl day</td><td id="3-d">Mohri et al. (2001)</td></tr>
<tr><td id="3-e">d</td><td id="3-f">T₁ death rate</td><td id="3-g">0.040</td><td id="3-h">(0, 0.5)</td><td id="3-i">day-1</td><td id="3-j">Mohri et al. (2001)</td></tr>
<tr><td id="3-k">de</td><td id="3-l">Te death rate</td><td id="3-m">0.06</td><td id="3-n">(0, 0.5)</td><td id="3-o">day</td><td id="3-p">Kuznetsov et al. (1994)</td></tr>
<tr><td id="3-q">de</td><td id="3-r">C death rate</td><td id="3-s">0.2</td><td id="3-t">(0, 0.8)</td><td id="3-u">day</td><td id="3-v">Duvall and Perry (1968)</td></tr>
<tr><td id="3-w">kₙ</td><td id="3-x">Tₙ differentiation</td><td id="3-y">0.001</td><td id="3-z">(0, 0.1)</td><td id="3-A">day⁻¹</td><td id="3-B">Essunger and Perelson (1994)</td></tr>
<tr><td id="3-C">η</td><td id="3-D">Michaelis-Menten</td><td id="3-E">100</td><td id="3-F">(0, 1000)</td><td id="3-G">cells/µl</td><td id="3-H">Estimated</td></tr>
<tr><td id="3-I">αₙ</td><td id="3-J">Tₑ proliferation</td><td id="3-K">0.41</td><td id="3-L">(0, 1)</td><td id="3-M"></td><td id="3-N">Janeway et al. (2001)</td></tr>
<tr><td id="3-O">αc</td><td id="3-P">Tₑ recruitment</td><td id="3-Q">0.2</td><td id="3-R">(0, 1)</td><td id="3-S">day⁻¹</td><td id="3-T">Estimated</td></tr>
<tr><td id="3-U">Cmax</td><td id="3-V">maximum C</td><td id="3-W">3 x 10⁵</td><td id="3-X">(1.5 × 10⁵, 4 × 10⁵)</td><td id="3-Y">cells/µl</td><td id="3-Z">Estimated</td></tr>
<tr><td id="3-10">$r_c$</td><td id="3-11">C growth</td><td id="3-12">0.03</td><td id="3-13">(0, 0.5)</td><td id="3-14">day$^{-1}$</td><td id="3-15">Afenya and Calderón (2000)</td></tr>
<tr><td id="3-16">$r_e$</td><td id="3-17">$T_e$ loss (due to C)</td><td id="3-18">0.005</td><td id="3-19">(0, 0.1)</td><td id="3-1a">day$^{-1}$ (cells/μl)</td><td id="3-1b">Estimated</td></tr>
<tr><td id="3-1c">$r_c$</td><td id="3-1d">C loss (due to $T_e$)</td><td id="3-1e">0.005</td><td id="3-1f">(0, 0.1)</td><td id="3-1g">day$^{-1}$ (cells/μl)</td><td id="3-1h">Essunger and Perelson (1994)</td></tr>
</table>

<a id='2db398ff-9f6c-409f-ad6e-b04d245b76ac'></a>

effector T cells, and are released into the blood (Janeway
et al., 2001). Thus, the coefficient αn incorporates the
rate at which such encounters lead to activation (as
opposed to anergy) of Tn, as well as the rates of
proliferation and differentiation into Te.

<a id='73ecb029-0ee3-4987-a902-a4b49db7bca5'></a>

The second term is a recruitment term, which we again represent as Michaelis–Menten. We assume that a proportion of effector T cells will recruit other immune cells to aid in killing CML cells. In order to represent this increase in killer cells, we effectively boost the effector T cell population by a compensatory amount. The rate constant $\alpha_e$ incorporates this recruitment. The third term represents the loss due to the natural lifespan of $T_e$ cells, with $d_e$ the death rate constant for $T_e$. The fourth term is a law of mass action term, due to encounters between $T_e$ and CML cancer cells. Since these encounters occur in the blood, there is no saturation effect as occurs in the lymph. Some encounters result in a loss of $T_e$, due to direct effect by the CML cell or due to activation-induced cell death (AICD) from excess stimulation. The coefficient $\gamma_e$ is the rate constant for loss of $T_e$ due to these encounters.

<a id='70b4131c-f132-4eb6-8bf7-52d6a40e4a87'></a>

In Eq. (3), the first term on the right-hand side gives the contribution due to growth of C, in the form of a Gompertz law. This law is well-established as the best fit for cancerous tumors. (See, e.g., Xu and Ling, 1988; Bassukas and Maurer-Schultze, 1988; Steel, 1977.) Afenya and Calderón (2000) show that the Gompertz curve also provides a significantly better fit for leukemic cancer data than logistic, exponential, or polynomial curves. The Gompertz curve incorporates the almost exponential growth of cancers at first, as well as the later slowing of the growth. The constant Cmax is the estimate of the maximum possible concentration of CML. The second term in Eq. (2) represents the loss

<a id='1e7b34ad-0529-49de-8358-35192159128a'></a>

of CML cells which die a natural death, where d_c is their death rate constant. The third term, with coefficient &gamma;_c, represents the loss of C due to encounters with T_e.

<a id='4e6c7668-6063-4c6c-b1bf-e5bb383f41fe'></a>

The constants used in the system of differential equations (1)-(3), appear in Table 1. The table gives a brief description of the constants, the values used as initial estimates for the constants, the ranges that are used for sampling later in the paper, and the units and references for the constants.

<a id='141d729c-5624-41fb-9a44-9e33f325b628'></a>

We use the following initial values for the three populations, where t = 0 is the starting time for the model:

$T_n(0) = 1510 \text{ cells/µl,}$
$T_e(0) = 20 \text{ cells/µl,}$
$C(0) = 10,000 \text{ cells/µl.}$

<a id='dcd85ea7-25a6-477b-91fe-995677a0c126'></a>

## 4. Discussion of parameter estimates and initial population values

The value we use for s_n, the source term for the T_n cell population, is calculated using data from Mohri et al. (2001). In the data collected from healthy subjects, the average contributions from a source were found to be 0.033 CD4+ cells/µl/day, and 0.040 CD8+ cells/µl/day. This gives a net contribution of 0.073 cells/µl/day, which we use as the source term for our naive T cell population, T_n. In the same paper, the average number of cell deaths in healthy subjects, both for CD4+ and CD8+ lymphocytes, was found to be 0.040/day. (This cell death number actually takes into account the very small amount of proliferation measured for the

<!-- PAGE BREAK -->

<a id='65553999-f2de-4152-a805-054a2a65b1e3'></a>

*H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513–523*

<a id='6aeb27a1-914e-41a0-ab28-cf7a48ef7d92'></a>

517

<a id='f84dd27b-c708-4ca8-8e8b-f7a64dfdbd57'></a>

T cells, and so should more accurately be termed the
"net loss".)

<a id='c7513542-4e68-4f99-a40c-d4ed3dbed1cd'></a>

The value for $d_e$, the rate constant for natural $T_e$
death, is estimated to be close to the calculated value in
Kuznetsov et al. (1994, p. 303). It is expected that $d_e >$
$d_n$, although the two numbers should not be drastically
different, so we choose $d_e$ to be of the same order of
magnitude as $d_n$. The value for $d_c$, the rate constant for
natural $C$ death, is taken from Duvall and Perry (1968).
They report an average leukocyte half-life of 83.1 h, or
roughly 3.5 days, which we use to calculate $d_c$. The value
for $k_n$ is based on estimates of the probability of anergy
and activation of antigen-specific $T_n$ in Janeway et al.
(2001), and on the very rough estimates of encounter
rates incorporated into other T cell-pathogen models,
such as that of Essunger and Perelson (1994). The value
for $\alpha_n$, the production factor for $T_e$ from activated $T_n$, is
estimated using proliferation rates in Janeway et al.
(2001). Janeway et al. state that an activated T cell
proliferates for close to 7 days, producing a total of
approximately 1000 daughter cells. The value for $\alpha_e$, the
recruitment constant for $T_e$ due to encounters with $C$, is
approximated at 0.2, because it should be lower than the
rate of activation, but is not expected to be an entire
order of magnitude lower. The value for $r_c$, the growth
rate of $C$, is taken from Afenya and Calderón (2000). To
get an estimate for $\gamma_c$, the loss rate for $C$ due to
encounters between $T_e$ and $C$, we again use encounter
rates that are incorporated into other T cell-pathogen
models (e.g., Essunger and Perelson, 1994). Based on
our $\gamma_c$, we were able to estimate the value for $\gamma_e$.

<a id='f7bd1102-ec0c-49ef-8399-37ef224be174'></a>

In Mohri et al. (2001), the average concentration of CD4+ T cells in healthy individuals was found to be approximately 1080 cells/µl of blood in the steady state. The average concentration of CD8+ measured in healthy individuals was approximately 600 cells/µl of blood, giving a total of 1680 T cells/µl of blood, which we use for our estimate of the initial concentration of naive T cells in the blood. We decrease this by roughly 10% with the assumption that at this stage of CML, there would have been a small decrease of the usual levels of naive T cells due to activation. Thus we take T_n(0) = 1510. Correspondingly, we assume that the initial concentration of effector T cells, T_e(0), is approximately 20 cells/µl of blood. This represents the proliferation that occurs when naive T cells receive the signal to become activated and undergo cell division, minus a small loss of T_e due to interactions with C. Small changes in these numbers were investigated numerically in the model, with no significant change observed in the outcome of the system.

<a id='d1ab3716-ad52-4668-a3f3-047b0c01e329'></a>

The estimate of 10 000 cells/µl of blood is used as an initial guess for C(0); the maximum concentration of CML cells in the blood observed in living patients is reported to be approximately 300 000 cells/µl (Lee, 2001).

<a id='caa562c0-e9fb-4b4b-bcb9-5abb985c4202'></a>

## 5. Analytic results

To study the behavior of the system of differential equations, we find the equilibrium solutions, and linearize about these to examine their stability. To ease the calculations, we first simplify the model by rescaling the variables.

<a id='72a32b6f-6254-4d8a-84df-524a81ce49a9'></a>

5.1. Simplification of the model

Using standard rescaling techniques (non-dimensionalization), we reduce the number of parameters from twelve to eight. The populations and time are rescaled as follows: Tn is rescaled by multiplying by a factor of dn/sn, Te is rescaled by a factor of γe/dn, C is rescaled by γe/dn, and t is rescaled by a factor of dn.
The resulting system is the following:

<a id='219f6399-b2d0-457e-b89d-acab91a0c89b'></a>

$$\frac{dT_n}{dt} = 1 - T_n - \zeta_1 T_n \left(\frac{C}{C + \zeta_2}\right) \quad (4)$$

<a id='f043d117-0bea-4d9d-b9cc-440861c28efc'></a>

$$\frac{dT_e}{dt} = \xi_3 T_n \left(\frac{C}{C + \xi_2}\right) + \xi_4 T_e \left(\frac{C}{C + \xi_2}\right) - \xi_5 T_e - CT_e, \quad (5)$$

<a id='7a03e6b1-ffa1-4aa5-be36-5b189b14a1ce'></a>

$\frac{dC}{dt} = \xi_6 C \ln\left(\frac{\xi_7}{C}\right) - \xi_8 C - CT_e$. (6)

<a id='c8ed3b4a-0b38-4cfb-9cde-8290c57117e9'></a>

The new coefficients are defined as follows: ζ₁ = kₙ/dₙ, ζ₂ = γₑη/dₙ, ζ₃ = αₙkₙsₙγ_c/dₙ³, ζ₄ = αₑ/dₙ, ζ₅ = dₑ/dₙ, ζ₆ = r_c/dₙ, ζ₇ = γₑC_max/dₙ, and ζ₈ = d_c/dₙ.

<a id='584a71a6-b000-4d6c-a26c-30e7b709c237'></a>

5.2. *Equilibrium solutions*

We now set each of the three simplified differential equations equal to zero, and solve for T~n~, T~e~, and C. This gives the equilibrium solutions; i.e., it gives values of T~n~, T~e~, and C for which the system will no longer change (since all of the derivatives, or rates of change, will be zero).

<a id='a71f3309-2a58-4f54-8578-41689ceab6e3'></a>

We first consider the equilibrium solution(s) for which C = 0. In this case, Eq. (4) implies that T_n = 1, and Eq. (5) implies that T_e = 0, and there are no other equilibria for which C = 0. We let P_1 = (1,0,0) represent this trivial (healthy) equilibrium solution.

<a id='fb235d2f-d7ce-4f9d-923d-ba0a59f7259a'></a>

Any other equilibrium values of *C* are given by the solution to the following equation obtained from all three Eqs. (4)-(6):

<a id='97e90a78-fe6e-462a-8066-a8ccebcb989d'></a>

0 = \zeta_8 - \zeta_6 \ln(\zeta_7) + \zeta_6 \ln(C)
+ \frac{\zeta_3 C (C + \zeta_2)}{(C + \zeta_2 + \zeta_1 C) [(C + \zeta_2)(C + \zeta_5) - \zeta_4]}
(7)

<a id='f8eab6bb-f6c3-43dd-aa00-908c38752b2d'></a>

The third term on the right-hand side of Eq. (7) is logarithmic in C, and hence increases as C increases. For the factors of the fourth term to be zero, C must be negative (for the clinically feasible ranges of parameters in Table 1, Section 3). Thus, this fourth term is a

<!-- PAGE BREAK -->

<a id='2f85c674-8e19-48a5-9c94-b6d899598e16'></a>

518

<a id='73d14985-a14b-4018-b164-ad480e2bf85b'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513-523

<a id='04411f37-6b89-4c35-88c6-5e4172052e9e'></a>

rational function which decreases as C increases (when C is positive), and so there is at most one value of C which makes the right-hand side of Eq. (7) equal to zero.
This means there is at most one other equilibrium solution, which we will denote by P2 = (T̃n, T̃e, C̃). This equilibrium solution occurs when ζ8 < ζ6 ln(ζ7), or when dc/rc < ln(γe Cmax/dn).

<a id='81c2a072-496c-48e5-aa0e-98abc8defd4b'></a>

In order for this equilibrium to be physically meaningful, all three populations must be nonnegative. The resulting conditions on Eqs. (4)-(6) are satisfied trivially, so the equilibrium is a realistic one, and there is no new information obtained from the conditions.

<a id='36319d82-16c1-4ff7-8c53-3e3e32a8bd12'></a>

## 5.3. Linearization of the system

To determine the behavior of the cell populations near each of the equilibrium solutions, we need to compute the linearization of the system, which is obtained from the Jacobian matrix of the system. See, e.g., Borrelli and Coleman (1998, p.446) for more information about such calculations. For the system of Eqs. (4)-(6), the Jacobian is the following:

<a id='2681308d-697b-413f-8420-a31d6d7c310c'></a>

5.3.2. Equilibrium 2
Here we examine the equilibrium solution P₂ = (T̃n, T̃e, C̃), when it exists. In this case, analytic techniques fail to yield information about the eigenvalues, due to the complexity of the system. Conditions such as the Routh test (Borrelli and Coleman, 1998, p. 415), for example, give transcendental equations which cannot be solved analytically. As an alternative, we calculate the eigenvalues for a wide variety of possible parameter values, by systematically sampling through the ranges listed in Table 1. To ensure representative sampling, we use a technique called Latin hypercube sampling (LHS), which is discussed in detail in Section 6, to randomly select values from the specified ranges. For the equilibrium populations, we sample from the interval (0, 5000) for T̃n and T̃e, and we sample from the interval (1, 400 000) for C̃. In our 3000 LHS runs, all of the eigenvalues were either negative real or were imaginary with all of the real parts bounded above by -1.000076.

<a id='882659e5-5c0d-4158-a01b-27b1cbbacab9'></a>

The large ranges of $\tilde{T}_n$, $\tilde{T}_e$, and $\tilde{C}$ used to calculate the eigenvalue estimates give reasonable confidence that the

<a id='89969f19-1088-411d-8ae4-622ec0d0dba5'></a>

A = 
$$ \begin{pmatrix}
-1 - \zeta_1 \left(\frac{C}{C+\zeta_2}\right) & 0 & -\zeta_1 T_n \left(\frac{\zeta_2}{(C+\zeta_2)^2}\right) \\
\zeta_3 \left(\frac{C}{C+\zeta_2}\right) & \zeta_4 \left(\frac{C}{C+\zeta_2}\right) - \zeta_5 - C & \zeta_3 T_n \left(\frac{\zeta_2}{(C+\zeta_2)^2}\right) + \zeta_4 T_e \left(\frac{\zeta_2}{(C+\zeta_2)^2}\right) - T_e \\
0 & C & \zeta_6 \ln\left(\frac{\zeta_7}{C}\right) - \zeta_6 - \zeta_8 - T_e
\end{pmatrix} \quad (8) $$


<a id='08951c6b-09aa-4e04-bb23-c6605ee0686f'></a>

If we substitute a set of equilibrium values for T_n, T_e, and C in the matrix A, then the matrix A will represent the linearization of the system of differential equations about that equilibrium solution. By the Hartman-Grobman theorem (see, Othmer et al., 1997), the behavior of the original (nonlinear) system will be approximated by the behavior of the linearized system near that equilibrium solution, as long as the equilibrium solution is hyperbolic (i.e., the real parts of the eigenvalues of the matrix are not equal to zero). We will now examine the two equilibrium solutions separately.

<a id='1f100324-30cb-4044-bf0a-b1a4c0c28146'></a>

5.3.1. Equilibrium 1
Evaluating A at the trivial solution P₁ = (1,0,0) gives

A(P₁)
=

```
⎡ -1   0   -ζ₁/ζ₂   ⎤
⎢  0  -ζ₅   ζ₃/ζ₂   ⎥
⎣  0   0  -ζ₆ - ζ₈  ⎦
```
(9)

<a id='edcb5011-bb3d-4cea-bc25-af97be038288'></a>

The eigenvalues of this matrix are λ₁ = −1, λ₂ = −ζ₅, and λ₃ = −ζ₆ − ζ₈, which are all real numbers. The equilibrium solution P₁ is asymptotically stable, since λ₁, λ₂, and λ₃ are all negative.

<a id='7baa0d7c-0dc1-4223-a594-d6d9e07448c3'></a>

eigenvalues indeed have negative real parts for this
equilibrium solution. Hence we assume the equilibrium
solution considered here is asymptotically stable, and we
proceed with numerical analysis of the system.

<a id='e5e63109-3db8-4348-9ce8-f3d8e0896a5a'></a>

5.3.3. Summary of stability
If $d_c/r_c < \ln(\gamma_e C_{max}/d_n)$ (which is the case for the initial parameter estimates), then the system of Eqs. (4)–(6) has two asymptotically stable equilibria, $P_1$ and $P_2$. Otherwise, the system has only one equilibrium, the trivial (healthy) state $P_1$, and this equilibrium is asymptotically stable.

<a id='009b100a-4fa8-4df3-8893-a3108db1535b'></a>

6. Numerical analysis: relationships between parameters and C

In this section, we examine the relationship between C and the model parameters. We numerically solve Eqs. (4)-(6) for a variety of choices of parameter values, using the ranges listed in Table 1. For all of the numerical analysis that follows, we use code we wrote for Mathematica™ 4.2. Each time we numerically solve the system of differential equations we use a time span

<!-- PAGE BREAK -->

<a id='c13ba421-404a-4081-bbed-2d590a5ef141'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513–523

<a id='c04bab1d-58dd-4b83-b2d5-0e0ce864f2ac'></a>

519

<a id='0d2e772c-771a-440b-852c-e11ecd42ef70'></a>

of 750 days. We use the largest concentration of CML
cells during the 750 days as a marker for disease
progression in these solutions. Other time periods (both
much larger and much smaller) yield the same qualita-
tive results in determining critical parameters in the
outcome of the disease.

<a id='cc7e9836-a2cc-4e13-9220-899d1811ebc6'></a>

We look for significance of the relationships between choices of particular parameter values and outcomes for CML by keeping track of whether or not C exceeds a set threshold value at any time during the 750 day period. We use a threshold of 22 500 cells/µl to represent a stage at which the patient is no longer in full remission, although we also obtained the same results when larger and smaller values for the threshold were used. Partial remission is evidenced by a white blood cell count in the range of approximately 15 000–30 000 cells/µl, but it is unclear what fraction of the total count are CML cells (Athens et al., 1965; Lee et al., 1999). Stryckmans et al. (1977) show kinetic data where the fraction of white blood cells that are leukemic increases as the disease progresses, and this fraction varies greatly between patients. However, it is likely that the number of total healthy white blood cells stays around the normal range (7500–10 000) (Gordon et al., 1999). Thus, in partial remission we expect there are fewer than 22 500 CML cells/µl, and perhaps many fewer.

<a id='f0418d17-9275-499b-8914-170ed9ea9d98'></a>

Because of the uncertainty in the initial parameter estimates, we perform Latin hypercube sampling (LHS) on all of the parameters in all of the simulations below. LHS is a well-established method for investigating systems which are too complex to be tractable analytically, and for which there is possibly large uncertainty in the parameter values used in the equations (see Blower and Dowlatabadi, 1994). The technique involves numerically solving the equations multiple times, using randomly sampled values for all of the parameters in the system. Although the standard Monte Carlo sampling varies all parameters at once, LHS differs in that it ensures that the combinations of parameter choices are well distributed. The ranges of values from which samples are chosen are specified ahead of time, and are chosen here to ensure that all clinically feasible parameter values are included. Each range is divided into a specified number of equi-probable intervals, which are then put into a random order. On any given run, a random value is selected for each parameter, from the appropriate interval. This ensures the mixing of the intervals from which the random values are chosen, and provides higher confidence in the qualitative behavior of the solutions, despite the uncertainty in the parameter values.

<a id='2f8b8e08-1994-4068-9ed3-1485ed051811'></a>

6.1. *Graphical results of parameters vs. C*

First, we examine the plots of individual parameter
values versus C, where the other parameters are sampled

<a id='3ba7cc95-e3b3-49e6-8f49-dd3fd62bdf80'></a>

using LHS. We reduce the dependence of the outcome on the particular choice of other parameters by varying them simultaneously. We run LHS to give 500 sets of parameter choices. For each of the 500 sets, we determine C̃, defined to be the largest value of C over the 750 day time interval. We use C̃ to examine dependence on the parameters, since this decreases the dependence of our results on the choice of the correct time interval. For each parameter, we then create a graph showing the 500 values for that parameter, plotted against C̃. In our analysis of all 12 parameters in this manner, we find that the values of the parameters d_c and r_c appear to strongly correlate with C̃, with r_c appearing to have a somewhat stronger correlation. A statistical analysis of these plots appears in the following section.

<a id='e7f7da01-a377-46ef-bfa8-b99f3bf8f32d'></a>

In the plot of d_c vs. C̃ (Fig. 2), the dependence of C̃ on d_c can be clearly seen. However, even for extremely large values of d_c, there are many combinations of other parameter values which cause C̃ to be 50 000 cells/µl or more. This contrasts with the case of r_c, whose sampled values are plotted vs. C̃ in Fig. 3.

<a id='9054db66-d882-4d80-ac28-d4afd4940a99'></a>

In Fig. 3, there are still a few combinations of parameter values which cause C̃ to be large, even for

<a id='68b1d398-30dd-44c4-8b56-3d29bf43d3be'></a>

<::transcription of the content
: Scatter plot with y-axis labeled "C (cells/µl)" ranging from 0 to 350000, and x-axis labeled "d_c (day⁻¹)" ranging from 0 to 0.8. The plot shows 500 data points scattered across the graph, generally concentrated towards lower C values.: chart::>

Fig. 2. A plot of 500 points with d_c vs. C, the maximum value of C over a 750 day time period. All other parameters are varied simultaneously, using LHS.

<a id='452d30d2-a737-4dac-a95f-c53cded05122'></a>

<::A scatter plot showing data points with x-axis 'r_c (day⁻¹)' ranging from 0 to 0.5, and y-axis 'Ĉ (cells/µl)' ranging from 0 to 350000.: chart::>

Fig. 3. A plot of 500 points with r_c vs. C̃, the maximum value of C over a 750 day time period. All other parameters are varied simultaneously, using LHS.

<!-- PAGE BREAK -->

<a id='c00f5683-c51c-4e13-81fc-0251a8027047'></a>

520

<a id='b1e80f62-ac06-41dd-b8d2-f192a08f5167'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513–523

<a id='5a741bfa-6961-4bb8-8c59-410ead99d1bc'></a>

extremely small values of $r_c$. However, the large majority
of the outcomes for $\tilde{C}$ are indistinguishable from
0 cells/µl when $r_c$ is sufficiently small (around
0.06 cells/µl/day), regardless of the values of other
parameters.

<a id='0ce8a677-cdf0-45b6-8e5b-41007298189e'></a>

## 6.2. Analysis of numerical results

In order to distinguish individual parameters that significantly affect the long-term behavior of _C_ in the model, we record and analyse the parameter values randomly chosen during the LHS where we vary all parameters simultaneously for each of the 500 runs. The maximum value of _C_ over the 750 day time period, _C_̃, is recorded for each run. We associate a value of 1 to a particular _C_̃ if _C_̃ is above the threshold value of 22 500 cells/µl discussed previously. Otherwise, we associate a value of 0 to the particular value of _C_̃.

<a id='119f1a33-b0f0-471c-8743-f84b8db24ad1'></a>

We use the statistical package R to fit a logistic
regression to the 500 different values of a given
parameter, and the associated 1's and 0's. We then
perform an analysis of deviance on the regression model
and a chi-squared test to determine whether or not the
parameter is statistically significant. The results appear
in Table 2:

<a id='77ea880b-a4d4-4a96-b85e-b0fe1b42790b'></a>

Using a significance level of 0.05, there are two parameters which are clearly significant: r_c, the growth rate of CML, and d_c, the death rate of CML. It is important to note the statistical analysis is done on data which is not stochastic. Furthermore, by performing a logistic regression we must make the assumption that by focusing on a single parameter at a time, the effects of all the other parameters introduce enough noise that they can be considered "random" in some sense. These limitations occur because presently there are not better tools for exploring the behavior of complex high-dimensional differential equation models.

<a id='a76075c7-b840-4342-ac39-9384b1550a5f'></a>

6.3. Additional graphical evidence examining significance

For this analysis, we look at all possible pairs of the
12 parameters. This gives 66 ("12 choose 2") pairs to
examine. For each of these pairs, we make a graph of
plotted points of one parameter versus the other, with
the coordinates of the points in the graph given by
the sampled values for those parameters from the LHS.
The points in the plot are colored light gray if the

<a id='b45acb17-8a7a-4fa3-af8a-e0b7d7a057ad'></a>

Table 2
Statistical results
<table id="7-1">
<tr><td id="7-2">Parameter</td><td id="7-3">P&gt;|X|</td><td id="7-4">Parameter</td><td id="7-5">P&gt;|X|</td><td id="7-6">Parameter</td><td id="7-7">P &gt; |χ|</td></tr>
<tr><td id="7-8">Sn</td><td id="7-9">0.22</td><td id="7-a">kn</td><td id="7-b">0.67</td><td id="7-c">Cmax</td><td id="7-d">0.65</td></tr>
<tr><td id="7-e">dn</td><td id="7-f">0.40</td><td id="7-g">η</td><td id="7-h">0.09</td><td id="7-i">re</td><td id="7-j">&lt;0.001</td></tr>
<tr><td id="7-k">de</td><td id="7-l">0.61</td><td id="7-m">An</td><td id="7-n">0.39</td><td id="7-o">Ve</td><td id="7-p">0.58</td></tr>
<tr><td id="7-q">de</td><td id="7-r">&lt;0.001</td><td id="7-s">de</td><td id="7-t">0.06</td><td id="7-u">Ve</td><td id="7-v">0.12</td></tr>
</table>

<a id='630ee392-1389-48f4-a44a-9021ef45cdf7'></a>

<::Plot: scatter plot with x-axis labeled "s_n (cells/µl/day)" ranging from 0 to 0.5, and y-axis labeled "r_c (day⁻¹)" ranging from 0 to 0.5. The plot contains numerous square data points. Some points are light pink, and others are dark blue. The light pink squares are predominantly in the upper region of the plot, while the dark blue squares are mostly in the lower region, with some overlap. Figure caption: Fig. 4. Plot of the LHS sampled values for s_n vs. r_c. The light gray squares (shown as light pink in the plot) are values which caused C to go above the given threshold value of 22 500 cells/µl, and the dark gray squares (shown as dark blue in the plot) are values for which C remained below the threshold. All other parameters are varied simultaneously.::>

<a id='3b2b5fff-1d54-4a51-a071-a77ebfdf29e2'></a>

corresponding solution for C goes above our chosen threshold of 22 500 cells/µl, and dark gray if it does not.

<a id='58b3b0ca-59f6-4d7c-8af0-ce26607ed78b'></a>

In the majority of the graphs (all except for _r_c and _d_c),
there are no apparent regions of exclusion of points for
which _C_ is above the threshold value of 22 500 cells/µl
or below. However, in all of the graphs that include _r_c
(the effective growth rate of _C_), the coordinates of dark
gray points are restricted to values of _r_c below
approximately 0.35 cells/µl/day. The percentage of
points which are dark gray increases as the values of
_r_c decreases below this. This indicates that no matter
what the values of the other 11 parameters, the value of
_r_c determines the outcome of the system in the majority
of cases. See the plot of _s_n versus _r_c given in Fig. 4.

<a id='b8748723-35e0-4a16-86bb-3a342797c887'></a>

In the graphs that include d_c (the natural per capita death rate of C) few of the dark gray points occur for values of d_c below approximately 0.2/day. The percentage of points which are dark gray increases as d_c increases, but do not achieve the percentages achieved in the case of r_c. This indicates that having d_c ≥ 0.2 makes it more likely that C can be controlled, but that condition alone is likely not sufficient; the outcome also depends on the values of other parameters to a large degree. See the plot of s_n versus d_c given in Fig. 5.

<a id='413c9310-6d00-4be4-b4a1-408f2d675fc9'></a>

7. Discussion of results of numerical analysis

In addition to the computational results shown above, in the many simulations run using this model, we observe a variety of behaviors for C for different choices of parameter values. The observed outcomes correlate with some of the disease characteristics typically found in patients with CML, while undergoing treatment or not responding to treatment. These outcomes include: high CML cell counts (Fig. 7); remission and relapse or rebound of CML (Fig. 8); and control of CML (Fig. 6).

<!-- PAGE BREAK -->

<a id='a0c48e00-1731-4276-97ed-c5545d4f58ad'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513-523

<a id='3eff497d-5855-4573-8752-6cdc6bcfe8f0'></a>

521

<a id='dad50982-8184-423f-818c-d9615c72f479'></a>

<::chart: A scatter plot titled "Fig. 5. Plot of LHS sampled values for $s_n$ vs. $d_c$" shows points plotted on an x-axis labeled "$s_n$ (cells/µl/day)" ranging from 0 to 0.5, and a y-axis labeled "$d_c$ (day$^{-1}$)" ranging from 0 to 0.8. The plot contains numerous small square data points. Some points are light pink, and others are dark blue. The light pink squares represent values which caused $C$ to go above the given threshold value of 22 500 cells/µl, and the dark blue squares are values for which $C$ remained below the threshold. All other parameters are varied simultaneously.::>

<a id='54554ae8-6cda-4bb5-ac4e-e2c900600fe6'></a>

<::
Fig. 6. An example graph of CML versus time, where CML decreases over a 2-year period.

Line graph showing CML (cells/μl) on the y-axis versus time (days) on the x-axis. The y-axis ranges from 4000 to 10000, with major ticks at 1000-unit intervals. The x-axis ranges from 0 to 700, with major ticks at 100-day intervals. The curve starts at approximately 10000 cells/μl at time 0 and decreases exponentially, reaching approximately 3500 cells/μl by 700 days.
: chart::>

<a id='6ba5538c-086c-4e5b-a255-48dd096d5460'></a>

<::line graph: The x-axis is labeled "time (days)" and ranges from 0 to 700, with major tick marks at 100, 200, 300, 400, 500, 600, and 700. The y-axis is labeled "CML (cells/µl)" and ranges from 0 to 50000, with major tick marks at 20000, 30000, 40000, and 50000. A single line starts near the origin, increases sharply, and then gradually flattens out, approaching 50000 CML (cells/µl) as time approaches 500 days and beyond.Fig. 7. An example graph of CML versus time, where CML increases over a 2-year period.: chart::>

<a id='e14559e0-3698-47f7-b316-d0adea8f0139'></a>

We mention this evidence as support for the biological
relevance of our model. We show some examples of
these graphs below. Table 3 gives the approximate
parameter values for the graphs.

<a id='59304a11-28db-4f54-a245-4de8a3f6c64f'></a>

The results of the numerical analysis in the previous sections give strong evidence themselves for the validity

<a id='e31f032d-f1b2-4bd3-8309-eadeaa42ed63'></a>

<::transcription of the content: chart::>
### CML versus Time Graph
**Y-axis:** CML (cells/µl), ranging from 8800 to 9600.
**X-axis:** time (days), ranging from 0 to 100.
**Plot:** A line graph shows CML cell counts starting near 9600, sharply decreasing to a minimum of approximately 8750 around day 12, then gradually increasing and plateauing at approximately 9375 from around day 60 to day 100.

Fig. 8. An example graph of CML versus time, where CML cell counts initially decrease, but later rebound.
<::>


<a id='1aec82d3-6107-448e-9cce-fc2ded208861'></a>

of the model presented here. Another measure of the model's accuracy is given by a comparison of known treatments and their effectiveness, to the predictions of the model. The current main treatments for CML are radiation, chemotherapy, bone marrow transplant, and the drug Gleevec (imatinib). (For a review on CML treatments, see Schiffer et al., 2003.)

<a id='70180c6e-d8b5-4e82-96fe-056c08c6369b'></a>

Radiation and chemotherapy increase the death rates of the CML cells, but they are non-specific treatments, and also increase the death rates of the naive and effector T cells. For the majority of patients, these treatments alone are not effective in eradicating CML (Schiffer et al., 2003). In light of this, in some cases bone marrow transplant is used in conjunction with chemotherapy, either with or without radiation therapy. This combination treatment resets the CML count to zero or very low levels, and increases the death rates of all three cell populations. The combination treatment of bone marrow transplant, radiation, and chemotherapy is the only treatment that can lead to complete permanent cure, however it does not always lead to a cure (Schiffer et al., 2003). These treatment outcomes agree with our numerical results that changing d_c can be significant. Because these treatments also increase d_n and d_e, we do not expect that the treatments would necessarily be sufficient to control CML.

<a id='58002911-eb0f-45d9-948e-e7f6b7bf7307'></a>

Gleevec was approved in 2001 as a treatment for CML, and completely controls C in 95% of all CML patients for long periods of treatment (Kantarjian et al., 2002). However, CML mutations that cause Gleevec to lose its effectiveness can occur after one or more years, and patients return to disease progression (Kreuzer et al., 2003). Gleevec works by blocking one of the pathways that CML uses to reproduce at an excessive rate (Kreuzer et al., 2003). In our model, this rate is represented by r_c. The LHS results predict that adequately controlling r_c should control CML, which is exactly what is observed in patients treated with Gleevec, until CML mutates around the drug and Gleevec no longer is able to affect the CML growth rate.

<!-- PAGE BREAK -->

<a id='4f9b0e83-4042-4142-bd0e-2bf4e4f4ff8d'></a>

522

<a id='2f225aec-3477-4923-9d78-4824d108f2d9'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513-523

<a id='f15756b1-a3cf-4081-bddb-6a03d8509fa9'></a>

Table 3
Parameter values used in graphs
<table id="9-1">
<tr><td id="9-2">Graph</td><td id="9-3">s_n</td><td id="9-4">d_n</td><td id="9-5">d_e</td><td id="9-6">d_c</td><td id="9-7">k_n</td><td id="9-8">η</td><td id="9-9">α_n</td><td id="9-a">α_e</td><td id="9-b">C_max</td><td id="9-c">r_c</td><td id="9-d">γ_e</td><td id="9-e">γ_c</td></tr>
<tr><td id="9-f">Fig. 6</td><td id="9-g">0.37</td><td id="9-h">0.23</td><td id="9-i">0.30</td><td id="9-j">0.024</td><td id="9-k">0.062</td><td id="9-l">720</td><td id="9-m">0.14</td><td id="9-n">0.98</td><td id="9-o">230 000</td><td id="9-p">0.0057</td><td id="9-q">0.057</td><td id="9-r">0.0034</td></tr>
<tr><td id="9-s">Fig. 7</td><td id="9-t">0.29</td><td id="9-u">0.35</td><td id="9-v">0.40</td><td id="9-w">0.012</td><td id="9-x">0.066</td><td id="9-y">140</td><td id="9-z">0.39</td><td id="9-A">0.65</td><td id="9-B">160 000</td><td id="9-C">0.011</td><td id="9-D">0.079</td><td id="9-E">0.058</td></tr>
<tr><td id="9-F">Fig. 8</td><td id="9-G">0.071</td><td id="9-H">0.050</td><td id="9-I">0.12</td><td id="9-J">0.68</td><td id="9-K">0.063</td><td id="9-L">43</td><td id="9-M">0.56</td><td id="9-N">0.53</td><td id="9-O">190 000</td><td id="9-P">0.23</td><td id="9-Q">0.0077</td><td id="9-R">0.047</td></tr>
</table>

<a id='d48d0352-f3f4-4118-a7a1-34a592f810fb'></a>

# 8. Conclusions

The results above suggest several clinically relevant conclusions for treatment of CML. The most striking observation is that the growth rate of CML, r_c, and the natural death rate, d_c, are the most important parameters in the control of CML in this model. The importance of r_c suggests that Gleevec and other drugs which attempt to block excessive growth rates of CML are likely to be successful treatments for CML, for the duration of their effectiveness. Our results also give some indication that increasing d_c may not be sufficient in all cases in controlling CML, which matches observations of current treatments, and which we hope will be investigated more closely by other researchers. Another reason why controlling CML using d_c is likely to be insufficient, is the difficulty of producing a drug which increases d_c without increasing d_n or d_e, the natural death rates of the T cells.

<a id='b2160c2a-da9e-434d-b03d-54836551c75c'></a>

Thus, researchers investigating treatments for CML
patients may wish to focus on treatments that can affect
the parameter r_c. Our model suggests that treatments
that attempt to change the other parameters are less
likely to achieve reduction or eradication of CML.
Because of the high risk involved in bone marrow
transplantation, the resistance that CML develops to
Gleevec, and the lack of response of some patients to
any of the treatments mentioned here, there is still a
pressing need for other treatments or treatment proto-
cols for patients with CML.

<a id='e889ca6b-ac87-4da2-b559-2d56797b54f2'></a>

Another outcome of our analysis is validation of the
model itself. This new model can now be used and
refined to include other aspects of the immune-CML
interaction. One example would be the incorporation of
the effects of immune system-boosting treatments in
patients with CML. Another use we hope to see is the
development of a more detailed model, with experiments
designed to obtain more precision in parameter values.

<a id='baf7086a-4342-4d49-a6cc-39d2c7f60824'></a>

Having this model allows us to solve the optimal drug
dosing problem for drugs such as Gleevec, which we
hope to complete in the near future. Given an estimate
of the mutation rates of CML, the most effective dosing
levels over time can be predicted for Gleevec, or for
other drugs or combinations of drugs. Optimal dosing
can substantially increase the period in which a patient
remains healthy, which is especially important for
treatments to which diseases eventually develop resis-
tance or which are expensive. Gleevec currently costs

<a id='ce0e8002-539f-4e86-a88c-a81ceb0fdd58'></a>

approximately $2500 per month, which means that a constrained optimal dosing solution, for limited resource scenarios, would be valuable as well. Further work predicting optimal combinations of chemotherapy, radiation, and drugs such as Gleevec would also be of great benefit in the treatment of CML.

<a id='d2256835-13f9-42a5-b16a-d34272593321'></a>

## Acknowledgements

Thanks to Peter Lee, MD and Michelle Green, Ph.D.,
of Stanford University, Denise Kirschner, Ph.D., of the
University of Michigan, Alan Perelson, Ph.D., of Los
Alamos National Laboratory, and Johnny Lam, statis-
tician, of Palo Alto, CA, for helpful discussions during
the development and analysis of this model.

<a id='1e7bf496-e307-4b18-a988-113723144f90'></a>

# References
Afenya, E., Calderón, C., 2000. Diverse ideas on the growth kinetics of disseminated cancer cells. Bull. Math. Biol. 62, 527–542.
Athens, J.W., Raab, S.O., Haab, O.P., Boggs, D.R., Ashenbruker, H., Cartwright, G.E., Wintrobe, M.M., 1965. Leukokinetic studies. X. Blood granulocyte kinetics in chronic myelocytic leukemia. Leukemia 44 (5), 765–777.
Bassukas, I.D., Maurer-Schultze, B., 1988. The recursion formula of the Gompertz function: a simple method for the estimation and comparison of tumor growth curves. Growth Develop. Aging 52, 113–122.
Blower, S., Dowlatabadi, H., 1994. Sensitivity and uncertainty analysis of complex models of disease transmission: an HIV model, as an example. Int. Stat. Rev. 2, 229–243.
Borrelli, R., Coleman, C., 1998. Differential Equations: A Modeling Perspective. Wiley, New York.
Cronkite, E.P., Vincent, P.C., 1969. Granulocytopoiesis. Ser. Haematol. 2, 3–43.
Duvall, C.P., Perry, S., 1968. The use of 51-chromium in the study of leukocyte kinetics in chronic myelocytic leukemia. J. Lab. Clin. Med. 71, 614–628.
Edelstein-Keshet, L., 1988. Mathematical Models in Biology. Random House, New York.
Essunger, P., Perelson, A.S., 1994. Modeling HIV infection of CD4+ T-cell subpopulations. J. Theor. Biol. 170, 367–391.
Faderl, S., Talpaz, M., Estrov, Z., O’Brien, S., Kurzrock, R., Kantarjian, H., 1999. The biology of chronic myeloid leukemia. New Engl. J. Med. 341 (3), 164–172.
Fokas, A.S., Keller, J.B., Clarkson, B.D., 1991. A mathematical model of granulocytopoiesis and chronic myelogenous leukemia. Cancer Res. 51 (8), 2084–2091.
Freedman, H., 1980. Deterministic Mathematical Models in Population Ecology. Marcel Dekker, New York.

<!-- PAGE BREAK -->

<a id='c29f650f-949a-4528-b8bf-7cb68cfb11f4'></a>

H. Moore, N.K. Li / Journal of Theoretical Biology 227 (2004) 513–523

<a id='4a3b7588-c553-4ee5-8dfd-65cf1a8fd8fc'></a>

523

<a id='7324d6e7-0d16-43ce-8bab-cbf904a84ab2'></a>

Gordon, M.Y., Dazzi, F., Marley, S.B., Lewis, J.L., Nguyen, D.,
Grand, F.H., Davidson, R.J., Goldman, J.M., 1999. Cell biology of
CML cells. Leukemia. Apr;13 Suppl 1:S65-71.

Haase, A.T., Henry, K., Zupancic, M., Sedgewick, G., Faust, R.A.,
Melroe, H., Cavert, W., Gebhard, K., Staskus, K., Zhang, Z.Q.,
Dailey, P.J., Balfour Jr., H.H., Erice, A., Perelson, A.S., 1996.
Quantitative image analysis of HIV-1 infection in lymphoid tissue.
Science 274, 985-989.

<a id='5ed09788-6564-4299-9ed3-e33d5d52fd07'></a>

Janeway, C.A., Travers, P., Walport, M., Shlomchik, M., 2001.
Immunobiology: The Immune System in Health and Disease.
Garland Publishing, New York.

<a id='ed8b7a68-251e-4b4f-a6af-4a76bdeb0cdf'></a>

Kantarjian, H., Sawyers, C., Hochhaus, A., Guilhot, F., Schiffer, C.,
Gambacorti-Passerini, C., Niederwieser, D., Resta, D., Capdeville,
R., Zoellner, U., Talpaz, M., Druker, B., Goldman, J., O'Brien,
S.G., Russell, N., Fischer, T., Ottmann, O., Cony-Makhoul, P.,
Facon, T., Stone, R., Miller, C., Tallman, M., Brown, R., Schuster,
M., Loughran, T., Gratwohl, A., Mandelli, F., Saglio, G.,
Lazzarino, M., Russo, D., Baccarani, M., Morra, E., International
ST1571 CML Study Group, 2002. Hematologic and cytogenetic
responses in patients with accelerated phase chronic myeloid
leukemia: results of a phase 2 study. New Engl. J. Med. 346,
645-652.

<a id='4d43e5e5-0c48-4135-8467-68cc3f69a4fd'></a>

Kirschner, D., Panetta, J.C., 1998. Modeling immunotherapy of the
tumor-immune interaction. J. Math. Biol. 37, 235-252.
Kirschner, D., Webb, G.F., 1996. A model for treatment strategy in
the chemotherapy of AIDS. Bull. Math. Biol. 58 (2), 367-390.

<a id='0fe46027-d550-44cf-b051-de5645efb72f'></a>

Kreuzer, K.A., Le Coutre, P., Landt, O., Na, I.K., Schwartz, M.,
Schultheis, K., Hochhaus, A., Dorken, B., 2003. Preexistence and
evolution of imatinib mesylate-resistant clones in chronic myelo-
genous leukemia detected by PNA-based PCR clamping technique.
Ann. Hematol. 82 (5), 284–289.

<a id='9370cf46-7600-46e3-9f44-b0bc4c11a160'></a>

Kuznetsov, V., Makalkin, I., Taylor, M., Perelson, A., 1994.
Nonlinear dynamics of immunogenic tumors: parameter estimation
and global bifurcation analysis. Bull. Math. Biol. 56 (2), 295–321.

<a id='f070018e-5762-49d8-b392-3518fb4977bb'></a>

Lee, G.R., Foerster, J., Lukens, J., Paraskevas, F., Greer, J.P.,
Rodgers, G., Wintrobe, M.M. (Eds.), 1999. Wintrobe's Clinical
Hematology. Lippincott, Williams & Wilkins, Philadelphia, PA.
Lee, P., 2001. Pers. comm.

<a id='fc1aefa2-7b0b-457d-87cb-69cffb4706fa'></a>

Mohri, H., Perelson, A., Tung, K., Ribeiro, R., Ramratnam, B.,
Markowitz, M., Kost, R., Hurley, A., Weinberger, L., Cesar, D.,

<a id='1db738a3-f1f5-4cfe-9a8a-73492d95f25f'></a>

Hellerstein, M., Ho, D., 2001. Increased turnover of T lymphocytes in HIV-1 infection and its reduction by antiretroviral therapy. J. Exp. Med. 194 (9) (November 5), 1277–1287.
Nowak, M.A., Bonhoeffer, S., Hill, A.M., Boehme, R., Thomas, H.C., McDade, H., 1996. Viral dynamics in hepatitis B virus infection. Proc. Natl. Acad. Sci. USA 93, 4398–4402.
Nowak, M.A., May, R.M., 2000. Virus Dynamics: Mathematical Principles of Immunology and Virology. Oxford University Press, Oxford, UK.
Othmer, H.G., Adler, F.R., Lewis, M.A., Dallon, J.C., 1997. Case Studies in Mathematical Modeling Ecology, Physiology, and Cell Biology. Englewood Cliffs, Prentice-Hall, NJ.
Perelson, A.S., Nelson, P.W., 1999. Mathematical analysis of HIV-I dynamics in vivo. SIAM Rev. 41 (1), 3–44.
Perelson, A.S., Essunger, P., Cao, Y., Vesanen, M., Hurley, A., Saksela, K., Markowitz, M., Ho, D.D., 1997. Decay characteristics of HIV-1-infected compartments during combination therapy. Nature 387, 188–191.
Perelson, A.S., Kirschner, D., De Boer, R., 1993. Dynamics of HIV infection of CD4+ T cells. Math. Biosci. 114, 81–125.
Rubinow, S.I., 1969. A simple model of steady state differentiating cell system. J. Cell Biol. 43, 32–39.
Rubinow, S.I., Lebowitz, J.L., 1975. A mathematical model of neutrophil production and control in normal man. J. Math. Biol. 1, 187–225.
Sawyers, C.L., 1999. Chronic myeloid leukemia. New Engl. J. Med. 340 (17), 1330–1340.
Schiffer, C.A., Hehlmann, R., Larson, R., 2003. Perspectives on the treatment of chronic phase and advanced phase CML and Philadelphia chromosome positive ALL. Leukemia 17, 691–699.
Steel, G.G., 1977. Growth of Kinetic Tumors. Oxford University Press, Oxford, UK.
Stryckmans, P.A., Debusscher, L., Collard, E., 1977. Cell kinetics in chronic granuclotyci leukaemia (CGL). Clin. Haematol. 6 (1), 21–40.
Wigginton, J.E., Kirschner, D., 2001. A model to predict cell-mediated immune regulatory mechanisms for human infection with Mycobacterium tuberculosis. J. Immunol. 166 (3), 1951–1967.
Xu, X.L., Ling, Y.B., 1988. A study on the expectational model for tumor growth. Int. J. Biomed. Comput. 22 (2), 135–141.
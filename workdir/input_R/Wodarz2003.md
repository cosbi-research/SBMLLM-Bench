<a id='4fee8ee3-49b2-4d20-9433-13db07867a76'></a>

<::logo: Elsevier
NON SOLLUS
A detailed illustration of a tree with a figure standing next to it, with the company name "ELSEVIER" below the image.::>

<a id='1b6d69cf-293a-4a50-b444-96756012dc39'></a>

Available online at www.sciencedirect.com

SCIENCE @ DIRECT®

<a id='131f682a-af11-4fe4-973a-c8f50c60f384'></a>

<::Stylized 'i' followed by 'Immunology Letters' text, framed by two double horizontal lines::>
www.elsevier.com/locate/

<a id='e37a1b3d-4d12-4367-812f-f089a43f294d'></a>

Immunology Letters 86 (2003) 213–227

<a id='87362ab2-91e8-4852-92ee-1b8cc6af38f9'></a>

A dynamical perspective of CTL cross-priming and regulation:
implications for cancer immunology

<a id='322ccb3a-a025-403b-951c-48a2d1c0c385'></a>

Dominik Wodarz<sup>a,*</sup>, Vincent A.A. Jansen<sup>b</sup>

<sup>a</sup> Fred Hutchinson Cancer Research Center, 1100 Fairview Avenue North, MP-665 Seattle, WA 98109, USA
<sup>b</sup> School of Biological Sciences, Royal Holloway, University of London, Egham, Surrey TW20 0EX, UK

Received 6 September 2002; accepted 27 January 2003

<a id='285ed0fe-406b-4b30-90c5-d159f638d36c'></a>

## Abstract
Cytotoxic T lymphocytes (CTL) responses are required to fight many diseases such as viral infections and tumors. At the same time, they can cause disease when induced inappropriately. Which factors regulate CTL and decide whether they should remain silent or react is open to debate. The phenomenon called cross-priming has received attention in this respect. That is, CTL expansion occurs if antigen is recognized on the surface of professional antigen presenting cells (APCs). This is in contrast to direct presentation where antigen is seen on the surface of the target cells (e.g. infected cells or tumor cells). Here we introduce a mathematical model, which takes the phenomenon of cross-priming into account. We propose a new mechanism of regulation which is implicit in the dynamics of the CTL: According to the model, the ability of a CTL response to become established depends on the ratio of cross-presentation to direct presentation of the antigen. If this ratio is relatively high, CTL responses are likely to become established. If this ratio is relatively low, tolerance is the likely outcome. The behavior of the model includes a parameter region where the outcome depends on the initial conditions. We discuss our results with respect to the idea of self/non-self discrimination and the danger signal hypothesis. We apply the model to study the role of CTL in cancer initiation, cancer evolution/progression, and therapeutic vaccination against cancers.

© 2003 Elsevier Science B.V. All rights reserved.

<a id='425b864d-7f20-44a7-9629-04c2da375976'></a>

Keywords: CTL; Cross-Priming; Cancer; Immunology; APC; Tolerance; Self/non-self; Danger

<a id='2ac5d6e0-f933-4f20-990b-01a8d1ee3b57'></a>

1. Introduction

Cytotoxic T lymphocyte (CTL) responses are a major branch of the immune system which can remove infected cells and tumor cells and can inhibit viral replication by non-lytic means. Yet, the exact mechanism by which CTL become induced is still not clear. Recently, the phenomenon of cross-priming and cross-presentation has received attention [1–8]. This means that antigen presenting cells (APCs) such as dendritic cells take up antigen and display it on their surface. The antigen bound to the APCs is then recognized by CTL and this leads to their activation. This process of cross-presenta-

<a id='22bf111c-94fb-434c-98c5-fc9be77ece66'></a>

* Corresponding author. Tel.: +1-206-667-7700; fax: +1-206-667-7004.
E-mail address: wodarz@fhcrc.org (D. Wodarz).

<a id='65b78d7e-4d81-45d9-bbf1-4a61be42bccd'></a>

tion is in contrast to direct presentation. With direct presentation, CTL recognize antigen on the target cell (infected cell or tumor cell) itself.

<a id='ba262196-4906-4ad8-8081-fb217dcbced0'></a>

The exact events occurring in response to cross- and direct presentation are unclear. Cross-presentation is thought to play a role in the regulation of the response. That is, in deciding whether the CTL should expand and react, or whether they should enter a state of tolerance. Different activation states of dendritic cells could result in different responses by CTL upon presentation [2,6,9-11]. Related to this, the presence or absence of danger signals is thought to play an important role in deciding whether CTL react against a given antigen or not [12-15]. A better knowledge of these mechanisms is crucial for understanding important immunological questions: why CTL generally do not successfully remove tumors; how peripheral tolerance is maintained; and why CTL efficiently resolve some viral infections but not others.

<a id='276441d4-e168-432e-98a1-7586d3a49f86'></a>

0165-2478/03/$ - see front matter  2003 Elsevier Science B.V. All rights reserved.
doi:10.1016/S0165-2478(03)00023-3

<!-- PAGE BREAK -->

<a id='22012a9e-d736-4905-b10f-27d87db11286'></a>

214

<a id='2f64b5bf-1cb7-4e8e-a3f0-670fca7c062f'></a>

D. Wodarz, V.A.A. Jansen / *Immunology Letters* 86 (2003) 213–227

<a id='9d4b8e7f-268e-4e3c-bc4d-d0c67570cde0'></a>

This study uses a mathematical model to propose a new mechanism in which a dynamical interplay between cross-presentation and direct presentation regulates CTL responses. It is assumed that cross-presentation by APCs results in activation and expansion of the specific CTL. The CTL are then assumed to be exposed to direct presentation on the target cells. This results in lysis. In addition, it is assumed that exposure to high amounts of antigen by direct presentation can lead to death of the CTL. This might occur by antigen-induced cell death [16-18]. Alternatively, exposure to antigen by direct presentation might drive further differentiation of CTL precursors (CTLp) into effectors (CTLe) which die at a relatively fast rate [19].

<a id='25097585-b273-401e-995c-fd94fd18a831'></a>

Here we show that under these assumptions, the ratio of cross-presentation to direct presentation can be a deciding factor which determines whether exposure to antigen results in an immune response or in tolerance. The higher this ratio, the more likely the CTL will expand and react. The lower this ratio, the more likely it is that tolerance is achieved. We discuss our results in relation to the concept of "self/non-self" discrimination, viral infections and tumors.

<a id='7d7b808f-ba6e-400b-a760-049a7b8d93a3'></a>

## 2. The model

We describe a model containing four variables: cells directly displaying antigen such as infected cells or tumor cells, T; we will refer to these cells as "target cells"; non-activated APCs which do not present the antigen, A; loaded and activated APCs which have taken up antigen and display it, A*; CTL, C. The model is given by the following system of differential equations which describe the development of these populations over time.

<a id='207d66b7-5a94-4e74-b24e-7ae1106b4059'></a>

$\frac{dT}{dt} = rT\left(1 - \frac{T}{k}\right) - dT - \gamma TC$

$\frac{dA}{dt} = \lambda - \delta_1 A - \alpha AT$

$\frac{dA^*}{dt} = \alpha AT - \delta_2 A^*$

$\frac{dC}{dt} = \frac{\eta A^* C}{\varepsilon C + 1} - qTC - \mu C$

<a id='fa19938b-e967-4cb1-9aaa-ead8d83dca76'></a>

The infected or tumor cells grow at a density dependent
rate rT(1-T/k). In case of virus infections, this
represents viral replication, where virus load is limited
by the availability of susceptible cells, captured in the
parameter k. In case of tumors, this corresponds to
division of the tumor cells and the parameter k denotes
the maximum size the tumor can achieve, limited for
example by spatial constraints. The cells die at a rate dT,

<a id='13941134-7af3-4509-8508-cafbaac11b3d'></a>

and are in addition lysed by CTL at a rate γTC. APCs,
A, are produced at a constant rate λ and die at a rate
δ₁A. They take up antigen and become activated at a
rate αAT. The parameter α summarizes several pro-
cesses: the rate at which antigen is released from the
cells, T, and the rate at which this antigen is taken up by
APCs and processed for display and cross-presentation.
Loaded APCs, A*, are lost at a rate δ₂A*. This
corresponds either to death of the loaded APC, or to
loss of the antigen–MHC complexes on the APC. Upon
cross-presentation, CTL expand at a rate ηA*C/(εC+
1). The saturation term, εC+1, has been included to
account for the limited expansion of CTL in the
presence of strong cross-stimulation [20]. The activated
and expanding population of CTL can lyse the infected
cells upon direct presentation. In addition, it is assumed
that direct presentation can result in removal of CTL at
a rate qTC. This can be brought about, for example, by
antigen-induced cell death, or over-differentiation into
effectors followed by death. Finally, CTL die at a rate
µC. Please note that this model is a simplification of
reality. APCs can have a variety of other effects on CTL
besides cross presentation. For example, they can secrete
cytokines which can have an effect on CTL proliferation
as well as migration. These functions are not included in
the model. The reason is that—while important—these
aspects of APC function go beyond the scope of the
present paper, since we concentrate on exploring the
effect of cross-stimulation on CTL dynamics. The model
will be analyzed by a combination of analytical and
numerical methods.¹

<a id='62b04b1b-3f8f-4a01-8c03-018e9f962c95'></a>

Thus a central assumption of the model is that cross-
presentation can induce CTL expansion, while direct
presentation does not have that effect; instead it can
result in the decline of the CTL population. This
assumption is a hypothesis we would like to explore,
and experimental tests will be proposed below. This
assumption implies that the magnitude of cross-presen-
tation relative to direct presentation could be a decisive
factor which determines the outcome of a CTL re-
sponse: activation or tolerance. In the model, the ratio
of cross-presentation to direct presentation is given by
cA*/qT.

<a id='9e908b1e-12cc-471d-a15b-0d5ec7f493bc'></a>

We assume that $r > a$. That is, the rate of increase of the target cells, $T$, is greater than their death rate. This

<a id='0e27b976-2ea1-4ebb-bb28-f3cfe9136ecf'></a>

1 For illustrative purposes, specific values have to be assigned to parameters in order to plot figures. Most of the parameter values in the model are, however, not known. Since the paper presents a mathematical understanding of the model behavior, knowledge of specific parameter values is not required to understand the dynamics on a qualitative level. While the parameter values of the model are somewhat arbitrary, their relative orders of magnitude make biological sense. For example, the death rate of activated and loaded APCs is assumed to be an order of magnitude higher than that of non-activated APCs.

<!-- PAGE BREAK -->

<a id='d521c42c-2525-4740-8651-5f2e47cbda90'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227

<a id='4797f692-9334-4ffc-884d-d6f626faa738'></a>

215

<a id='dc551732-a0f3-4db2-867f-711896dcd13d'></a>

<::A multi-panel chart titled "Fig. 1. Different outcomes of the model shown as time series." The figure consists of three vertically stacked time series plots, each showing a solid line and a dashed line, representing different outcomes of a model.

Panel (i) (Top Chart): This plot shows the 'Tolerance; CTL go extinct' outcome. The x-axis ranges from 0 to 50. The left y-axis ranges from 0 to 7. The right y-axis ranges from 0 to 0.1. The solid line starts low, increases, and then plateaus around 6. The dashed line (representing CTL) peaks around x=15, then decreases to 0.

Panel (ii) (Middle Chart): This plot shows the 'Tolerance outcome where CTL do not go extinct but are maintained at very low levels'. The x-axis ranges from 0 to 50. The left y-axis is labeled "Number of target cells" and ranges from 0 to 10. The right y-axis is labeled "CTL" and ranges from 0 to 3.5. The solid line starts high, dips slightly, and then plateaus around 9. The dashed line (CTL) starts high, dips, and then plateaus at a very low level, around 0.5.

Panel (iii) (Bottom Chart): This plot shows the 'Immunity outcome'. The x-axis ranges from 0 to 400. The left y-axis ranges from 0 to 1.2. The right y-axis ranges from 0 to 1. The solid line oscillates significantly, then settles at a low level around 0.2. The dashed line oscillates, then settles at a higher level around 0.4.

Parameters used for the model were chosen as follows: r = 0.5; k = 10; d = 0.1; γ = 1; λ = 1; δ₁ = 0.1; δ₂ = 1.5; η = 2; ε = 1; q = 0.5; μ = 0.1. α = 0.2 for (i) and α = 0.1 for (ii). For (iii) α = 0.05; r = 10; η = 10.
: chart::>

<a id='26dc3311-a57c-4889-90f5-f2cfc9011ea4'></a>

ensures that this population of cells can grow and
remain present. If this is fulfilled, the system can
converge to a number of different equilibria (Fig. 1).

<a id='97b95aa5-eaaa-43a2-9eeb-00cd913b2d91'></a>

The expressions for the equilibria will not be written out here since most of them involve complicated expressions.

<!-- PAGE BREAK -->

<a id='eac0786e-35ae-43a2-b477-89792e8943be'></a>

216

<a id='988f84b3-bee0-4eac-8290-c196c6cd6f5e'></a>

D. Wodarz, V.A.A. Jansen / _Immunology Letters_ 86 (2003) 213–227

<a id='dd25176c-914f-41fa-b43b-6cc39b23c95b'></a>

i) The CTL response fails to expand, i.e. C = 0. The population of target cells grows to a high equilibrium level, unchecked by the CTL. The populations of unloaded and loaded APCs, A and A*, also equilibrate.
ii) The CTL response expands, i.e. C > 0. In this case, the system can converge to one of two different outcomes. (a) The number of CTL is low and the number of target cells is high. This outcome is qualitatively similar to (i), because the CTL population does not fully expand, and the population of target cells remains high. (b) The number of CTL is high and the number of target cells is low. This can be considered the immune control equilibrium. If the population of infected cells is reduced to very low levels, this can be considered equivalent to extinction (number of cells below one).

<a id='20d40faa-4af0-4b9e-b504-69698c625e20'></a>

The following sections will examine which outcomes are achieved under which circumstances.

<a id='b7366e00-4922-4832-82e8-b171c3e916da'></a>

### 3. Analysis of the model

The two most important parameters in the present context are the rate of antigen uptake by APCs, α, and the growth rate of the target cells, r. This is because variation in these parameters can significantly influence the ratio of cross-presentation to direct presentation which is the subject of investigation. Hence, in the following sections we will examine the behavior of the model in dependence of these two parameters.

<a id='40ab7bc6-600c-4e0a-9524-355fb8d6d2eb'></a>

3.1. The rate of antigen uptake by APCs

The rate of antigen uptake by APCs comprises two processes: (i) the degree to which the antigen is made available for uptake; this can be determined for example by the amount of antigen released from the target cell, or the amount of apoptosis going on [5]. (ii) The rate at which the APCs take up the available antigen and process it for presentation. As the rate of antigen uptake by APCs, α, decreases, the ratio of cross-presentation to direct presentation decreases (Fig. 2i). When the value of α is high, the outcome is immunity. If the value of α is decreased and crosses a threshold, we enter a region of bistability (Fig. 2i): both the immunity and the tolerance equilibria are stable. Which outcome is achieved depends on the initial conditions. If the value of α is further decreased and crosses another threshold, the immune control equilibrium loses stability. The only stable outcome is tolerance (Fig. 2i).

<a id='b053adcd-bb4f-499a-b427-34886f667f4d'></a>

In the region of bistability, the dependence on initial conditions is as follows. Convergence to the immune control equilibrium is promoted by low initial numbers of target cells, high initial numbers of presenting APCs,

<a id='8140461f-ad75-470c-b857-84a23b8ff546'></a>

and high initial numbers of CTL. This is because under
these initial conditions, the dynamics start out with a
high ratio of cross-presentation to direct presentation
and this promotes the expansion of the CTL. On the
other hand, if the initial number of target cells is high
and the initial numbers of presenting APCs and CTL is
low, then the initial ratio of cross-presentation to direct
presentation is low and this promotes tolerance.

<a id='ea314cea-c53e-4e39-b477-330ac33fd158'></a>

This is the general pattern of how the outcome of the dynamics is influenced by the rate of antigen uptake by APCs, α. There are variations on this pattern depending on the value of parameters describing the strength of the CTL. An example is the CTL responsiveness following cross-stimulation, η. If the value of η is low the overall responsiveness of the CTL is still relatively low even if the rate of antigen uptake by APCs is very high. In this case, there is no parameter region in which only the immune control outcome is stable. On the other hand, if the CTL responsiveness is very high (high value of η), the bistable parameter region, where both immunity and tolerance are possible, disappears. Note, however, that in this case, the parameter region of tolerance is narrow because the CTL responsiveness is strong. In general, the higher the CTL responsiveness, η, the lower the rate of antigen uptake by APCs, α, below which tolerance becomes stable.

<a id='41a1be58-29ca-4c05-8f87-dbae86cb7732'></a>

A similar pattern is observed if the rate of loss of antigen presentation, δ2, is low. This is because longer-lived MHC-antigen complexes correlate with stronger stimulation of the CTL. In addition, this introduces unstable behavior into the model because there is a delay between the clearance of target cells bearing the antigen, and the loss of presentation of that antigen. Hence, the immunity outcome becomes characterized by limit cycles (this corresponds to the observation of sustained cycles in the population of cells; it will be explored further below when discussing Fig. 3).

<a id='3796b211-a550-465c-a600-cf5ee815734d'></a>

In summary, as the rate of antigen uptake by APCs is
decreased, the ratio of cross-presentation to direct
presentation decreases, and this shifts the dynamics of
the CTL response in the direction of tolerance. This can
include a parameter region in which both the tolerance
and the immunity outcome are stable, depending on the
initial conditions. If the CTL responsiveness to cross-
presentation is very strong, tolerance becomes an
unlikely outcome.

<a id='9555afa2-0041-46ea-97ca-6c332ecb6bb5'></a>

3.2. The growth rate of target cells

An increase in the growth rate of target cells, r, results in a decrease in the ratio of cross-presentation to direct presentation in the model. Hence an increase in the growth rate of target cells shifts the dynamics of the CTL from a responsive state towards tolerance. The dependence of the dynamics on the parameter r is shown in Fig. 2ii. The growth rate of target cells needs to

<!-- PAGE BREAK -->

<a id='d8076e58-32aa-4644-8aab-13afd53cf026'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227

<a id='b7a121db-9b73-4c2c-80c2-456413fbf732'></a>

217

<a id='93441dea-5e92-4285-a381-829d75819f18'></a>

<::chart::>Fig. 2. Bifurcation diagram showing the outcome of the model as a function of (i) the rate of antigen presentation by APCs, α, and (ii) the growth rate of target cells, r. Virus load and the ratio of cross-presentation to direct presentation at equilibrium are shown. The figure consists of four subplots arranged in a 2x2 grid. The x-axis for the left column of plots is 'Rate of antigen presentation by APCs, α', labeled as (i). The x-axis for the right column of plots is 'Growth rate of target cells, r', labeled as (ii). The y-axis for the top row of plots is '# target cells at equilibrium'. The y-axis for the bottom row of plots is 'Ratio of cross presentation to direct presentation at equilibrium'. All axes are on a logarithmic scale. The plots illustrate regions of 'tolerance equilibrium' and 'immune control equilibrium', and bistable regions where both outcomes are stable. (i) For high values of α, only the immune control outcome is stable. If the value of α is reduced, we enter a bistable parameter region where both the immunity and the tolerance outcomes are stable. If the value of α is still lower, only the tolerance outcome becomes stable. (ii) For small values or r, only the immunity outcome is stable. For higher values of r, we enter the bistable parameter region where both the immunity and the tolerance outcomes are stable. If the value of r lies above a threshold, only the tolerance outcome is stable. Parameters were chosen as follows. r = 0.5; k = 10; d = 0.1; γ = 1; λ = 1; δ₁ = 0.1; α = 0.5; δ₂ = 1.5; η = 2; ε = 1; q = 0.5; μ = 0.1.::>

<a id='779f3fa9-d4ba-4026-8914-3b758a99ad78'></a>

lie above a threshold to enable the CTL to potentially react. This is because for very low values of r, the number of target cells is very low, not sufficient to trigger immunity. If the growth rate of target cells is sufficiently high to potentially induce immunity, we observe the following behavior (Fig. 2ii). If the value of r lies below a threshold, the only stable outcome is immunity. If the value of r is increased and crosses a threshold, we enter a region of bistability. That is, both the immunity and the tolerance outcomes are possible, depending on the initial conditions. The dependence on the initial conditions is the same as explained in the last section. If the value of r is further increased and crosses another threshold, the immunity equilibrium loses stability and the only possible outcome is tolerance.

<a id='ca4872cb-7d24-4800-b035-1bbeec3a25ea'></a>

Again, there are variations of this basic pattern
depending on parameters describing the overall strength
of the CTL response. Consider the responsiveness of the
CTL to cross-stimulation, η. As the value of η is
increased, the immunity outcome can be characterized

<a id='70d0a814-857a-4a33-a578-d0859ce9ede6'></a>

by limit cycles; in addition the growth rate of target cells at which tolerance becomes the only stable outcome becomes higher. Thus, the higher the CTL responsive- ness, the less likely it is that fast target cell growth can result in tolerance. If the CTL responsiveness, η, lies above a threshold, the dynamics are slightly different when the tolerance outcome becomes stable at high growth rates of target cells, r. Now, tolerance is not described by the equilibrium where the number of CTL is zero. Instead, it is described by the equilibrium where a very weak CTL response develops which fails to reduce the number of target cells significantly. This outcome is, however, qualitatively very similar to the state of tolerance where the number of CTL is zero. The reason for this behavior is that for a very high CTL responsiveness (high values of η), the CTL cannot be driven extinct by fast target cell growth if the ratio of cross-presentation to direct presentation is small; in- stead, they are maintained at low and ineffective levels. This is, however, of limited biological importance, since

<!-- PAGE BREAK -->

<a id='07e528a7-8686-4090-a789-b569fefcb322'></a>

218

<a id='8c1d4fc3-3ec3-4fe8-96b5-ccc5692e7689'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227

<a id='aca38a1b-a129-4d01-bf8b-7a5b9c28d661'></a>

<::chart: line graph::>Fig. 3. Simulation of virus-induced autoimmunity. The graph plots the level of the immune response against time. The x-axis is labeled "Time (arbitrary units)" and ranges from 0 to 1000. The y-axis is labeled "Number of CTL against self antigen" and ranges from 0 to 2.5. A gray shaded region extends from approximately x=200 to x=300, representing the duration of a virus infection. The line graph shows the following: From x=0 to x=200, the "Number of CTL against self antigen" remains near 0. From x=200 to x=300 (within the shaded region), the number of CTLs oscillates rapidly, reaching peaks of about 2.2 and troughs near 0.2. After x=300, the oscillations continue, with peaks gradually decreasing from about 2.2 to 1.8-1.9 by x=1000, while troughs remain low (around 0.2-0.3). The simulation assumes that the degree of cross-presentation of self-antigen is relatively weak, and that we are in the parameter region in which both the immunity and the tolerance outcomes are both stable. Initially, the equilibrium outcome is tolerance. Shading indicates the duration of a virus infection. This is modeled phenomenologically by increasing the parameter α (infection increases the rate of uptake of self antigen by APCs because the antigen is more readily available following virus-induced death of host cells). The infection induces an immune response, and the response is continued after the infection has terminated. This is because infection has shifted the dynamics into a space where all trajectories lead to the immunity equilibrium. In this simulation, the immune response cycles over time and this could correspond to periods of flare-ups of the auto-immune disease, followed by periods of remission. Parameters were chosen as follows. r = 0.7; k = 10; d = 0.1; γ = 1; λ = 1; δ₁ = 0.01; α = 0.05; δ₂ = 1.5; η = 5; ε = 1; q = 0.5; μ = 0.1. During the phase of virus infection, a = 0.5.<::>

<a id='1c8eeee5-355c-4ceb-8bb3-377d2c50f216'></a>

this state of tolerance only occurs at unrealistically high
growth rates of target cells. Again, similar patterns are
observed if the rate of loss of antigen presentation, $\delta_2$, is
low because this results in overall stronger stimulation
of the CTL. In addition, the region of bistability can be
lost and the immunity outcome can be characterized by
the occurrence of limit cycles.

<a id='493e5ede-25ee-476c-aac1-e10152012564'></a>

In summary, an increase in the growth rate of target cells has a similar effect as a decrease in the rate of antigen uptake by APCs: the ratio of cross-presentation to direct presentation becomes smaller, and the outcome of the dynamics is driven from immunity towards tolerance. Again, this includes a parameter region where both the immunity and tolerance outcomes are stable and where the outcome depends on the initial condi-tions. The higher the overall responsiveness of the CTL to cross-stimulation, the less likely it is that a high growth rate of target cells can induce tolerance.

<a id='2051cb6a-78ee-41c2-a065-0e91f0afbd7f'></a>

## 4. Immunity versus tolerance

### 4.1. CTL regulation and the self/non-self debate

The question of CTL regulation and of tolerance versus immunity is part of a more general debate about which factors determine whether immune responses should react or remain silent. A traditional idea is that

<a id='a7e8eded-6e3f-4cdb-86af-a750b5fbe5c0'></a>

the immune system can distinguish self antigens from non-self [21–24]. Hence they only react against appropriate antigens and autoimmunity is avoided. An alternative idea is the danger signal hypothesis [12–15]. According to this theory, the major factor determining whether immunity develops is not self versus non-self. Instead, the immune system can detect the presence of danger via signals received by antigen-presenting cells, mainly dendritic cells. Danger signals activate the dendritic cells which in turn induce the expansion of specific responses. If danger signals are missing, the immunity does not become stimulated even if the antigen is foreign. While some substances have been suggested as danger signals, a definite identification of danger signals remains elusive.

<a id='40613d52-c065-4f34-a7ed-23b7c581a58d'></a>

Here, we have investigated this topic from a dynamical point of view in the context of CTL responses. We show that the immune system can switch between two states: tolerance and activation. Which state is reached need not depend on the presence or absence of signals, but on the relative magnitude of cross-presentation to direct presentation. This shows that regulation can be accomplished without signals but in response to a continuously varying parameter. Thus, the regulation of CTL responses could be implicit in the dynamics. This relies on the assumption that there is a difference in the effect of cross-presentation and direct presentation. The mathematical model assumes that while cross-

<!-- PAGE BREAK -->

<a id='7d234524-4832-4051-85d0-d6f2aabae8e0'></a>

_D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227_

<a id='3b08b8fd-61da-4dd6-91b4-854f003cc96c'></a>

219

<a id='b1062d35-35ac-4061-a66f-44ea0d40bcb6'></a>

presentation results in CTL expansion, direct presenta-
tion results in lysis followed by removal of the CTL.
While this assumption remains open to investigation,
some mechanisms described in the literature support this
notion. The simplest mechanism resulting in CTL
removal could be antigen-induced cell death [16–18].
That is, exposure to large amounts of antigen can trigger
apoptosis in the T cells. Another mechanisms could be
that exposure to direct presentation of antigen on the
target cells induce further differentiation from CTLp
into CTLe [19]. Since CTLe have anti-viral activity and
are thought to be short-lived and non-proliferating,
exposure to large amounts of direct presentation can
result in over-differentiation and an overall loss of CTL.
The exact effect of cross-presentation and direct pre-
sentation on the dynamics of CTL remains to be tested
by in vitro experiments: CTL should be exposed to a
given antigen displayed both on dendritic cells, and
directly on target cells. The effect of these two modes of
presentation on the dynamics of CTL should be
measured at various stages of CTL differentiation.

<a id='3b71ce8d-709a-4fbd-9439-f04a256a5227'></a>

With the assumptions explained above, we find a very simple rule that determines whether CTL responses expand and react, or whether they remain silent and tolerant. CTL expansion and immunity is promoted if the ratio of cross-presentation to direct presentation is relatively high. This is because the amount of CTL expansion upon cross-presentation outweighs the degree of CTL loss upon direct presentation. On the other hand, tolerance is promoted if the ratio cross-presentation to direct presentation is relatively low. This is because the amount of CTL loss upon direct presentation outweighs the amount of CTL expansion upon cross-presentation. Note that this type of regulation is implicit in the dynamics of CTL. If a given CTL specificity is created and the antigen is encountered, the CTL will always try to expand. However, if the ratio of cross-presentation to direct presentation is relatively low, this attempt to expand will result in deletion of the response. While some effectors might be created, the response will be muted before damage can be done.

<a id='60e82654-a57e-4b6e-8b4b-86bcd490e1f3'></a>

For self antigen displayed on cells of the body, the
ratio of cross-presentation to direct presentation is
normally low. This is because these cells do not die at
a high enough rate or release the antigen at a high
enough rate in order for the amount of cross presenta-
tion to be strong. On the other hand, large amounts of
this antigen can be available on the surface of the cells
expressing them (direct presentation). In terms of our
model, this situation can best be described by a low
value of a. Hence, in our model, CTL responses are not
predicted to become established against self antigens.
Instead, the outcome is tolerance. In addition, the initial
conditions favor tolerance in this scenario. When
immune cells with specificity for self are created and
try to react, the number of these immune cells is very

<a id='96664e2e-1640-43e1-9c52-cfe54b090e81'></a>

low and the number of target cells (tissue) is relatively
high. This promotes failure of the CTL response to
expand and to become established.

<a id='2d37145d-d73a-43a9-b8a7-fc707d581830'></a>

In the following sections we will discuss the dynamics of CTL responses to antigens that can be considered non-self. That is, antigens derived from tumors and intracellular pathogens.

<a id='a7eaacbd-a2e8-4af9-8bb4-de16538a254b'></a>

## 4.2. Tumors

Tumors and cancers are thought to arise through the generation of a series of mutations that result in the transformation of the cells. Compared to healthy cells, tumor cells escape growth control and in most cases also show an elevated mutation rate (mutator phenotype or genetic instability [25]). Hence, a tumor is characterized by an increasing number of mutated genes. The products of these mutations will be displayed on the surface of the tumor cells in conjunction with MHC. These tumor-specific antigens should thus induce CTL responses. Yet, they usually do not. On the other hand, some vaccination protocols have resulted in the induction of tumor-specific immune responses and reduction of tumors [26,27].

<a id='481eba70-54f5-4715-a264-d4248f31d2c6'></a>

According to the danger signal hypothesis, tumors are not perceived by the immune system as dangerous because tumor cells are long lived and do not elicit the production of danger signals. According to our model, tumors fail to induce CTL responses because tumor antigens are largely displayed on the surface of the tumor cells, but relatively little tumor antigen is made available for uptake by dendritic cells and hence for cross-presentation. Thus, the ratio of cross-presentation to direct presentation is low. Further, the model suggests that the ability of the host to mount a CTL response can depend on the size of the tumor. This will be pursued in more detail later in a section discussing tumor evolution and CTL responses.

<a id='d689c864-3ae8-4986-92e7-7fd0c82eda1d'></a>

4.3. *Viruses*

Many virus infections readily induce CTL responses. This is in accordance with our model. Infected cells can release many virus particles and/or induce relatively high levels of cell death. This results in the uptake of large amounts of antigen by dendritic cells and in high amounts of cross-presentation. Thus, the ratio of cross-presentation to direct presentation is relatively high, resulting in the induction of CTL responses. According to the danger signal hypothesis, the damage induced by the virus is sensed by the dendritic cells which in turn activate the CTL. Some viruses, such as lymphocytic choriomeningitis virus, do not, however, cause any damage [28]. In the absence of immune responses, LCMV can replicate at high levels without harming the host at all. While LCMV might not be

<!-- PAGE BREAK -->

<a id='a2f4c15c-8d58-4c39-80ee-1351c8f70440'></a>

220

<a id='cdd67a2b-c772-4fbf-b867-a12d58a5541e'></a>

_D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227_

<a id='9eeba161-e67b-42da-9d21-7af89505abaf'></a>

dangerous, it induces potent CTL responses [29]. This is
in accordance with our model: Since large amounts of
virus particles are produced and released from infected
cells, ready to be taken up by dendritic cells, the ratio of
cross-presentation to direct presentation will be high. In
addition, LCMV can infect dendritic cells. This can
make presentation via these APCs even more efficient.

<a id='a96da66f-4d96-41e5-bb9e-6a60601047eb'></a>

Some viruses impair specific immunity. A prominent example is human immunodeficiency virus (HIV) which impairs the virus-specific CD4 helper cell responses [30]. A similar absence of CD4 helper cell responses has been observed with hepatitis C virus (HCV) infection [31]. A major role of CD4 T cells is to activate dendritic cells which in turn is required for cross-presentation and CTL induction. Thus, CD4 helper cell impairment can result in the reduction of cross-presentation relative to direct presentation because dendritic cells fail to become activated. In this way, the virus can shift the dynamics away from efficient immunity towards tolerance.

<a id='7fb3ae63-4ebb-4f7c-a2ab-8c98bed686ff'></a>

## 4.4. Viruses and tumors
There are interesting connections between viruses and tumors. Some viruses can cause tumors. Other viruses can be used as therapeutic agents against certain tumor cells. They can kill the cells directly and/or induce immune responses [32,33]. According to the danger signal hypothesis, the presence of viruses in tumor cells should promote the induction of immune responses against tumors, because virus replication can result in the presence of danger signals in the tumor tissue.

According to our model, the relationship between viruses, tumors and CTL responses depends on the exact life-cycle of the virus. We distinguish between two scenarios: (i) The virus replicates by cell to cell spread or by inducing division of infected cells; little or no free virus is released. This is likely to result in reduced levels of cross-presentation relative to direct presentation. Interestingly, this is a characteristic of viruses that can cause tumors. An example is human T cell leukemia virus or HTLV-1 [34]. Most infected patients are healthy carriers. A small fraction of patients develops a neurological disease called HAM/TSP. Another small fraction of patients develops leukemia. A major route of virus spread in vivo occurs by Tax-induced division of infected T cells. Another route of virus growth in vivo is cell to cell spread. While it has been thought that HTLV-1 does not replicate and is mostly latent, recent experimental data indicate that this is not the case, and that virus replication does occur [35]. No free virus is, however, released from the infected cells. In this case, the virus antigen behaves similarly to tumor antigens. A lot of antigen is produced on the infected cell and is available for direct presentation. Little virus is released and taken up by dendritic cells for cross-presentation. Hence, CTL responses are likely to fail to control the

<a id='914db9b8-d691-4460-9b2f-97fabe6c0518'></a>

infection. If tumors are induced, CTL will also fail to control the tumor cells despite the presence of ongoing viral replication and the generation of viral antigen on tumor cells. Many tumor inducing viruses, such as Epstein Barr virus (EBV) or human papiloma virus (HPV), share these characteristics. (ii) The virus replicates by releasing virus particles from the infected cell. Now the virus antigen will not only be displayed on the infected tumor cells, but large amounts of antigen will also be available for uptake by dendritic cells for cross-presentation. Thus, the ratio of cross-presentation to direct presentation is relatively large, and CTL responses against the viral antigen are likely to be induced. This can lead to CTL-mediated reduction of the tumor. In addition, virus-mediated lysis of tumor cells can result in the release of tumor-specific antigens available for uptake and cross-presentation by APCs. Hence, a tumor-specific CTL response could also be induced. Several viruses, especially adenoviruses, have been investigated as potential therapeutic agents against cancers. A particular example is ONYX-015, an adenovirus that has entered clinical trials in the context of head and neck cancer [32,33]. It infects and replicates in p53 negative cells resulting in their death. Death can be caused either by the virus itself, or by CTL. The virus spreads by releasing many virus particles resulting in the burst and death of the infected cell.

<a id='1e92642c-ccd4-4346-9ce9-df54993c7b2b'></a>

## 4.5. Viruses and autoimmunity

Autoimmunity occurs if T cell or antibody responses react against host cells, resulting in damaging lesions or metabolic dysfunctions. Viruses have been implicated often as the cause of autoimmune diseases, although conclusive evidence is still missing. Various mechanisms have been suggested which could explain the role of viruses in the induction of such diseases [36,37]. A popular mechanism is called molecular mimicry. This means that pathology is caused by cross-reactivity between an infecting virus and autoreactive T cells in the host. Other hypotheses suggest that viruses cause autoimmunity following the induction of non-specific or inflammatory events resulting from infection of the tissue. A similar mechanism is suggested by our model: through the death of infected cells, a virus infection can make self antigens available for uptake and cross-presentation by APCs. This can increase the ratio of cross-presentation to direct presentation of self-antigens, and shift the dynamics away from tolerance towards reactivity. This is demonstrated with a computer simulation in Fig. 3. We assume that the degree of cross-presentation of self-antigens is relatively weak and that we are in the parameter region where both the tolerance and the immunity outcomes are stable. When immune cells specific for self-antigens are generated, the result is likely to be tolerance. When the system is

<!-- PAGE BREAK -->

<a id='bf5fb606-fc8c-4998-a94a-a106a2366cc8'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227

<a id='58dadcd8-8fb8-42c5-be61-3766b89c3dd3'></a>

221

<a id='813e10e2-be3b-4075-bdb6-08ef65554f58'></a>

disturbed however, by a viral infection, lysis of host cells increases the amount of self-antigen, which is cross-presented, and an inappropriate CTL response is induced. In the simulation, the virus infection is assumed to be only temporary. Note, however, that after the infection has terminated, the immune response against self continues. This is because the infection has shifted the dynamics into a domain of attraction which leads to immunity and not to tolerance. Also note, that the immune response dynamics can be cycling. This could correspond to repeated flare-ups of autoimmune diseases followed by periods of remission. Such patterns can be observed for example with multiple sclerosis. (Note that the immune response dynamics do not necessarily have to be oscillatory. A stable maintenance of the immune response is observed if the rate of CTL expansion upon antigenic stimulation is lower, which corresponds to a lower value of \eta).

<a id='e3f24b75-83a8-4893-8fb3-c962d05f3fc0'></a>

## 5. Case study: CTL and cancer progression

Tumors provide an interesting case study. While tumor cells bear many mutated antigens, they do not induce significant CTL responses. As explained above, this is consistent with our theoretical framework presented here, since the ratio of cross-presentation to direct presentation is expected to be low. This ratio, however, is influenced by parameters such as the growth rate of the target cells, and we observe a parameter region where the outcome of the CTL dynamics can depend on the initial conditions. Since cancer cells continuously evolve towards less inhibited growth, these results have implications for the role of CTL in tumor progression and cancer therapy. This is explored in the following sections.

<a id='20d01f48-f5c5-4428-87b5-2aabe5133a3a'></a>

5.1. Cancer initiation
A tumor cell is characterized by mutations which enable it to escape growth control mechanisms which keep healthy cells in check. According to the model, the generation of a tumor cell can lead to three different scenarios (Fig. 4): (i) A CTL response is induced which clears the cancer. (ii) A CTL response develops which is weaker; it controls the cancer at low levels, but does not eradicate it. (iii) A CTL response fails to develop; tolerance is achieved and the cancer can grow uncontrolled. Which outcome is attained depends on the characteristics of the cancer cells. In particular it depends on how fast the cancer cells can grow (r in the model), and how resistant they are against death and apoptosis. Cell death, and in particular apoptosis, is thought to increase the amount of cross-presentation [5]. Resistance to apoptosis thus corresponds to a reduction in the parameter \(\alpha\) in the model. Three parameter

<a id='7646253f-f737-4afc-82c1-02cc4b5617c2'></a>

regions can be distinguished. (i) If the cancer cells replicate slowly and/or still retain the ability to undergo apoptosis, the cancer will be cleared, because strong CTL responses are induced. If the cancer cells replicate faster and/or the degree of apoptosis is weaker, the ratio of cross-presentation to direct presentation is reduced. This can shift the dynamics into the bistable parameter region. That is, the outcome depends on the initial conditions. If the initial size of the tumor is small, it is more likely that CTL responses will be induced which can control the tumor cells at low levels. Since the host is naïve, however, the initial number of specific CTL is low, and this could promote tolerance. In general, the larger the size of the tumor, the more likely it is that the outcome is tolerance. (iii) If the growth rate of the tumor cell is still higher and/or the degree of apoptosis is still lower, then the ratio of cross-presentation to direct presentation falls below a threshold; now the only possible outcome is tolerance and uncontrolled tumor growth.

<a id='cfe2753a-90a7-4b73-9804-981e090adf1b'></a>

## 5.2. Tumor dormancy, evolution, and progression

Here, we investigate in more detail the scenario where the growth rate of the tumor is intermediate, and both the tolerance and the CTL control outcomes are possible, depending on the initial conditions. Assume the CTL control equilibrium is attained because the initial tumor size is small. The number of tumor cells is kept at low levels, but the tumor is unlikely to be cleared because in this bistable parameter region the ratio of cross-presentation to direct presentation is already reduced. If the tumor persists at low levels, the cells can keep evolving over time. They can evolve, through selection and accumulation of mutations, either towards a higher growth rate, r, or towards a reduced rate of apoptosis which leads to reduced levels of antigen uptake by dendritic cells, α. Both cases result in similar evolutionary dynamics. This is illustrated in Fig. 5 assuming that the cancer cells evolve towards faster growth rates (higher values of r). An increase in the growth rate of tumor cells does not lead to a significant increase in tumor load. At the same time, it results in an increase in the number of tumor-specific CTL. The reason is that a faster growth rate of tumor cells stimulates more CTL, which counter this growth and keep the number of tumor cells at low levels. When the growth rate of the tumor cells evolves beyond a threshold, the equilibrium describing CTL-mediated control of the cancer becomes unstable. Consequently, the CTL response collapses and the tumor can grow to high levels.

<a id='345fa29b-96e7-4c9f-93d1-b8329d7d3c2a'></a>

The dynamics of tumor growth and progression can include a phase called "dormancy". During this phase the tumor size remains steady at a low level over a prolonged period of time before breaking out of

<!-- PAGE BREAK -->

<a id='04927744-09b6-40d6-b827-ec840f236389'></a>

222

<a id='5aa5f5d2-6cd3-46c0-b63d-8eb5d6a4f7c5'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213-227
(a)
<::chart: A line graph with an x-axis ranging from 0 to 100. There are two y-axes. The left y-axis ranges from 0 to 0.15, with tick marks at 0, 0.05, 0.1, 0.15. The right y-axis ranges from 0 to 0.35, with tick marks at 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35. Two lines are plotted: a solid line that starts around 0.1, rises to a peak around 0.15 at x=20-25, and then declines to near 0 by x=40-50; and a dashed line that starts near 0, rises to a peak around 0.3 at x=30-35, and then declines towards 0 by x=100.::>
(b)
<::chart: A line graph with an x-axis ranging from 0 to 300, labeled at 0, 50, 100, 150, 200, 250, 300. There are two y-axes. The left y-axis is labeled "Number of target cells" and ranges from 0 to 0.2, with tick marks at 0, 0.05, 0.1, 0.15, 0.2. The right y-axis is labeled "CTL" and ranges from 0 to 1.4, with tick marks at 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4. Two oscillating lines are plotted: a solid line that starts near 0, peaks around 0.18, and then oscillates with decreasing amplitude, settling around 0.05; and a dashed line that starts around 0.1, peaks around 0.18, and then oscillates with decreasing amplitude, settling around 0.13.::> 

<a id='5801d9ed-47dc-426e-b331-8337ecb44e6a'></a>

(c)<::A line graph with an x-axis labeled "Time (arbitrary scale)" ranging from 0 to 50. There are two y-axes. The left y-axis ranges from 0 to 10. The right y-axis ranges from 0 to 0.4. Two curves are plotted: a dashed curve that peaks around x=6-7 and then decreases, and a solid curve that starts near 0, increases with an S-shape, and then plateaus at approximately 9 on the left y-axis and 0.35 on the right y-axis.: chart::>

<a id='7f5eee75-7a8e-48f6-aac2-26522681c7c7'></a>

Fig. 4. Time series plots showing the different possible outcomes when a tumor is generated. (i) Clearance is likely to occur in the parameter region where only the immunity outcome is stable. (ii). Immune control but failure to clear the target cells. This is likely to occur in the bistable parameter region: the immunity outcome is still stable, but immunity is weaker. (iii). Tolerance. Immunity does not become established and the number of target cells grows to high levels. Parameters were chosen as follows. k = 10; d = 0.1; γ = 1; λ = 1; δ₁ = 0.1; α = 0.5; δ₂ = 1.5; η = 2; ε = 1; q = 0.5; μ = 0.1. (i) r = 0.13. (ii, iii) r = 1. The difference between graphs (ii) and (iii) lies in the initial number of CTL, z.

<!-- PAGE BREAK -->

<a id='08efe0e2-eaf3-4cc3-a85a-8e55a797ee81'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227

<a id='eace3e48-d967-40e1-bb87-c9364e07724c'></a>

223

<a id='b6659a42-01f6-400f-8260-a9cc04a9e352'></a>

<::chart: The figure contains two plots, (a) and (b), both showing values as a function of the 'Growth rate of the tumor, r' on the x-axis, ranging from 0.5 to 3.0.

(a) The y-axis is 'Equilibrium # of target cells', on a logarithmic scale from 0.01 to 10. The plot shows a curve that starts around 0.03 at r=0.5, gradually increases to about 0.15 at r=2.4, and then sharply rises to 10 at r=2.5.

(b) The y-axis is 'Equilibrium level of CTL', on a linear scale from 0 to 2.5. The plot shows a straight line that starts around 0.4 at r=0.5, linearly increases to about 2.3 at r=2.4, and then sharply drops to 0 at r=2.5.

Fig. 5. Equilibrium tumor load (i) and the number of tumor specific CTL (ii) as a function of the growth rate of tumor cells, r. This graph can by interpreted to show the effect of tumor evolution towards faster growth rates over time. As evolution increase the value of r over time, the tumor population and the CTL attain a new equilibrium. As long as the value of r lies below a threshold, the tumor size does not increase significantly, while the number of CTL clearly rises. When the value of r crosses a threshold, the CTL response collapses and the tumor can grow to high levels. Parameters were chosen as follows. r = 0.5; k = 10; d = 0.1; γ = 1; λ = 1; δ₁ = 0.1; α = 0.5; δ₂ = 1.5; η = 2; ε = 1; q = 0.5; μ = 0.1.::>

<a id='ff0c5e88-d603-48de-891b-cd9f830ad996'></a>

dormancy and progressing further. Several mechanisms
could account for this phenomenon. The limitation of
blood supply, or inhibition of angiogenesis, can prevent
a tumor from growing above a certain size threshold
[38]. When angiogenic tumor cell lines evolve, the cancer
can progress further. Other mechanisms that have been
suggested to account for dormancy are immune

<a id='6ca99d9b-f10b-4879-9c09-082b73f669bc'></a>

mediated, although a precise nature of this regulation remains elusive [39]. As shown in this section, the model presented here can account for a dormancy phase in tumor progression. If the overall growth rate of the cancer cells evolves beyond a threshold, dormancy is broken: the CTL response collapses and the tumor progresses.

<!-- PAGE BREAK -->

<a id='35014460-827b-4899-83bf-d061bac44cc1'></a>

224

<a id='24d4d08d-ca08-4c46-9e70-a8a19227a82d'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227

<a id='534edd5d-3882-4669-b5f3-037932935bd4'></a>

## 5.3. Immunotherapy against cancers

Assuming that the CTL response has failed and the cancer can grow unchecked, we investigate how immunotherapy can be used to restore CTL mediated control or to eradicate the tumor. In the context of the model, the aim of immunotherapy should be to increase the ratio of cross-presentation to direct presentation. The most straightforward way to do this is dendritic cell vaccination. In the model, this corresponds to an increase in the number of activated and presenting dendritic cells, *A*<sup>*</sup>. We have to distinguish between two scenarios: (i) The tumor cells have evolved sufficiently so that the CTL control equilibrium is not stable anymore, and the only stable outcome is tolerance. (ii)

<a id='f332bacc-fd92-4830-aade-bc6ecf8d5ad3'></a>

The tumor has evolved and progressed less; the equili-
brium describing CTL mediated control is still stable.

<a id='5edec9e9-0eab-4656-ae57-dcdfe2dd6000'></a>

First we consider the situation where the tumor has progressed far enough so that the CTL control equilibrium is not stable anymore. Upon dendritic cell vaccination, tolerance is temporarily broken (Fig. 6). That is, the CTL expand and reduce the tumor cell population. This CTL expansion is, however, not sustained and tumor growth relapses (Fig. 6). The reason is as follows. Upon dendritic cell vaccination, the ratio of cross-presentation to direct presentation is increased sufficiently, enabling the CTL to expand. However, this boost in the level of cross-presentation subsequently declines, allowing the tumor to get the upper hand and re-grow. The model suggests, however,

<a id='9daf408a-73a1-447b-aba8-08aef85c42e8'></a>

<::chart: The image displays three stacked line graphs, all sharing a common x-axis labeled "Time (arbitrary units)" ranging from 0 to 28. Each graph depicts changes over time for different cell populations.  Graph (i) is composed of three sub-charts.  The labels (i) are also present at the bottom left and right of the overall figure.  The x-axis for all three charts is labeled "Time (arbitrary units)" ranging from 0 to 28.  First Chart (Top):  - Y-axis (left): "# of target cells", scaled from 0 to 10.  - Y-axis (right): Scaled from 0.01 to 10 (logarithmic scale).  - Data: A line shows a rapid increase from 0 to 10, then plateaus around 10, with a slight dip around time 10-12 before returning to the plateau.  Second Chart (Middle):  - Y-axis (left): "# of CTL", scaled from 0 to 0.7.  - Y-axis (right): Scaled from 0 to 10.  - Data: A line shows a small peak around time 1-2, then drops to 0, followed by a larger, sharp peak around time 10-11, then drops back to 0.  Third Chart (Bottom):  - Y-axis (left): "# loaded dendritic cells", scaled from 0 to 35.  - Y-axis (right): Scaled from 0 to 30.  - Data: A line shows a small peak around time 2-3, then drops to 0, followed by a larger, sharp peak around time 10-11, then drops back to 0.::>

<a id='b35d6f9b-3cac-432b-92c4-566cef3fc7d6'></a>

<::Figure (ii): Three line graphs stacked vertically. The x-axis for all graphs is labeled "Time (arbitrary units)" and ranges from 0 to 28 with major ticks at 4-unit intervals.  Graph 1 (Top): Y-axis is logarithmic, labeled 0.01, 0.1, 1, 10. The line starts low, rises sharply to a plateau around 10 from x=4 to x=20 with minor oscillations, then drops sharply to near zero around x=23. Graph 2 (Middle): Y-axis is linear, labeled 0, 2, 4, 6, 8, 10. The line stays near zero until x=8, then shows increasing oscillations from x=8 to x=22, followed by a sharp rise to a peak around 8.5 at x=23, then gradually decreases. Graph 3 (Bottom): Y-axis is linear, labeled 0, 5, 10, 15, 20, 25, 30. The line shows a small peak around (2, 4) then drops to zero by x=8. From x=10 to x=22, it displays a series of six sharp, tall peaks reaching approximately 30, each followed by a rapid drop to zero. After x=22, the line remains at zero.: chart::>

<a id='76738d90-bff0-48af-9bbc-125c19d3ba59'></a>

Fig. 6. Effect of dendritic cell vaccination on tumor dynamics assuming that the growth rate of the tumor has evolved to high values, where only the tolerance outcome is stable. (i) A single vaccination event induces a temporary reduction in tumor load, followed by a relapse. (ii) Repeated vaccination events can drive the tumor load below a threshold which corresponds to extinction in practical terms. Parameters were chosen as follows. r = 1.5; k = 10; d = 0.1; γ = 1; λ = 1; δ₁ = 0.01; α = 0.5; δ₂ = 1.5; η = 0.5; ε= 1; q = 0.5; μ = 0.1.

<!-- PAGE BREAK -->

<a id='78b37ed8-4a55-4e97-88ee-7c8e596055b3'></a>

D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227<::A multi-panel line chart showing the time-course dynamics of three different cell populations. All three panels share a common x-axis labeled "Time (arbitrary units)" ranging from 0 to 400.The top panel shows "# of target cells" on a logarithmic y-axis (0.01, 0.1, 1, 10). The line starts around 0.5, increases to almost 10, then sharply drops to about 0.2, and gradually declines to a very low level near 0.01.The middle panel shows "# of CTL" on a linear y-axis (0 to 1.2). The line starts at 0, rises to about 0.2, drops to 0, then at approximately x=60, it sharply peaks at 1.2, then quickly drops and oscillates, eventually settling around 0.2.The bottom panel shows "# loaded dendritic cells" on a linear y-axis (0 to 30). The line starts at 0, shows a small initial peak around 1-2, then at approximately x=60, it sharply peaks at 30, and then quickly drops to near 0 and remains at that level.: chart::> 

<a id='e5b5d5c2-7a7b-4393-a355-21ef4a68b405'></a>

Fig. 7. Effect of dendritic cell vaccination on tumor dynamics assuming that the growth rate has not yet progressed beyond a threshold, so that we are in the bistable parameter region of the model. A single vaccination event can induce immunity which can control the tumor at low levels. Parameters were chosen as follows. r = 0.3; k = 10; d = 0.1; y = 1; λ = 1; δ₁ = 0.01; α = 0.5; δ₂ = 1.5; η = 0.5; ε = 1; q = 0.5; μ = 0.1.

<a id='37524d92-5678-4fb1-9845-e91b4d06f0ee'></a>

225

<!-- PAGE BREAK -->

<a id='1f72abd0-4b47-497e-9e0d-134f53fefbe3'></a>

226

<a id='b4a81f80-1406-4391-95d9-89794e93b737'></a>

_D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227_

<a id='2a9a4162-dd2c-4ca0-90ed-b4d04e4e51ee'></a>

that the tumor can be eradicated if the level of cross-
presentation is continuously maintained at high levels.
This can be achieved by repeated vaccination events
(Fig. 6). The next vaccination event has to occur before
the level of cross-presentation has significantly declined.
This will drive tumor load below a threshold level which
practically corresponds to extinction (Fig. 6).

<a id='3f0d8060-7523-450c-bbc3-6252dde1c23d'></a>

Next, we consider the more benign scenario in which the tumor has not progressed that far and the CTL control equilibrium is still stable. Now a single vaccina- tion event can shift the dynamics from the tolerance outcome to the CTL control outcome (Fig. 7). The reason is that an elevation in the number of presenting dendritic cells shifts the system into a space where the trajectories lead to CTL control and not to tolerance. This is likely to be achieved if the size of the tumor is not very large. The larger the size of the tumor, the stronger the vaccination has to be (higher A*) in order to achieve success. If the tumor size is very large, then an elevated level of dendritic cells cannot shift the ratio of cross- presentation to direct presentation sufficiently to induce sustained immunity. A combination of vaccination and chemotherapy can, however, result in success. This is because chemotherapy reduces the size of the tumor and also induces death of tumor cells. Both factors con- tribute to a higher ratio of cross-presentation to direct presentation and to induction of immunity. Once a sustained CTL response has been induced, tumor cells are kept at low levels. However, the cancer is unlikely to be eradicated. Consequently, it can evolve over time. Thus, induction of CTL mediated control in the model is likely to result in a temporary phase of tumor dormancy. This phase is again broken after the overall growth rate of the tumor has evolved beyond the threshold at which the CTL control outcome becomes unstable.

<a id='dc34ce30-f943-45af-9e9d-54451af8e046'></a>

These considerations result in the following sugges-
tions. Dendritic cell vaccination should be administered
repeatedly until the last tumor cell has been eradicated.
If the tumor has already progressed relatively far, this is
the only way to prevent immediate relapse of the cancer.
If the tumor is less progressed, temporary tumor
dormancy can be achieved by a single vaccination event.
Tumor persistence and evolution will, however, break
this dormancy phase, resulting in renewed cancer
growth. Thus, in this case, repeated vaccination is also
advisable in order to keep the level of cross-presentation
above a threshold and to avoid tumor persistence. In all
cases, the model suggests that a combination of im-
munotherapy with conventional therapy is beneficial
because conventional therapy can reduce the growth
rate of the tumor. If conventional therapy increases the
chances of developing immunological control of the
tumor, conventional therapy would have to be applied
only temporarily which would have significant clinical
benefits.

<a id='adc378da-2a0a-484b-b3b5-ea4d945ef8d5'></a>

## 6. Conclusion

In this paper we have described a model of CTL dynamics which takes into account cross-presentation by APCs. We assumed that cross-presentation results in the expansion of the CTL population, while direct presentation can result in a decline of the CTL. This can occur either by antigen-induced cell death, or by differentiation of CTLp into short-lived CTLe. While these assumptions remain open to experimental testing, they give rise to interesting dynamics and a new mechanism for the regulation of CTL responses: a high ratio of cross-presentation to direct presentation results in CTL reactivity; a low ratio of cross-presentation to direct presentation gives rise to tolerance. The dynamics can include a parameter region where the outcome can depend on the initial conditions.

<a id='cebac63d-7924-4d80-acb7-f1d02313cf80'></a>

Our theory is different from the self/non-self framework, and more similar to the danger signal hypothesis. This is because the decision about whether to react or whether to stay tolerant is not based on whether the antigen is self or foreign. Instead it is based on conditions indicative of the presence of an intruder. However, the danger signal hypothesis suffers from the fact that a clear definition of danger is missing. In our model, the regulation of CTL reactivity does not rely on external signals received by the APCs. Instead, the regulatory mechanism is intrinsic in the dynamics and is thus the most parsimonious explanation. We do not, however, argue against the existence of immunoregulatory signals which can influence the function of APCs and thus regulate CTL responses. Further experiments have to be performed to test the assumptions underlying our model, and to investigate factors which influence the function of APCs such as dendritic cells.

<a id='89bb882b-cf25-44fc-a31c-411705f4c1d1'></a>

## Acknowledgements

We would like to thank an anonymous referee for very helpful suggestions which improved the quality of the paper.

<a id='91fc3b37-1f0b-4663-bc32-11c3194faac2'></a>

# References

1.  W.R. Heath, F.R. Carbone, Nat. Rev. Immunol. 1 (2001) 126-
    134.
2.  W.R. Heath, F.R. Carbone, Annu. Rev. Immunol. 19 (2001) 47-
    64.
3.  G.T. Belz, D. Vremec, M. Febbraio, L. Corcoran, K. Shortman,
    F.R. Carbone, W.R. Heath, J. Immunol. 168 (2002) 6066-6070.
4.  T. Blankenstein, T. Schuler, Trends Immunol. 23 (2002) 171-173.
5.  M.L. Albert, B. Sauter, N. Bhardwaj, Nature 392 (1998) 86-89.
6.  M.L. Albert, M. Jegathesan, R.B. Darnell, Nat. Immunol. 2
    (2001) 1010-1017.
7.  J.M. den Haan, S.M. Lehar, M.J. Bevan, J. Exp. Med. 192 (2000)
    1685-1696.

<!-- PAGE BREAK -->

<a id='2f150a1c-c6cc-47b9-8861-e4cf637e3a01'></a>

_D. Wodarz, V.A.A. Jansen / Immunology Letters 86 (2003) 213–227_

<a id='b24605cb-7716-4855-a0b2-507cbf8342d2'></a>

227

<a id='4ba017d7-36ce-4901-9d52-01fd3b6961fe'></a>

[8] J.M. den Haan, M.J. Bevan, Curr. Opin. Immunol. 13 (2001) 437–441.
[9] J. Banchereau, R.M. Steinman, Nature 392 (1998) 245–252.
[10] M.V. Dhodapkar, R.M. Steinman, M. Sapp, H. Desai, C. Fossella, J. Krasovsky, S.M. Donahoe, P.R. Dunbar, V. Cerundolo, D.F. Nixon, N. Bhardwaj, J. Clin. Invest. 104 (1999) 173–180.
[11] M.V. Dhodapkar, J. Krasovsky, R.M. Steinman, N. Bhardwaj, J. Clin. Invest. 105 (2000) R9–R14.
[12] P. Matzinger, Semin. Immunol. 10 (1998) 399–415.
[13] P. Matzinger, Science 296 (2002) 301–305.
[14] S. Gallucci, P. Matzinger, Curr. Opin. Immunol. 13 (2001) 114–119.
[15] E.J. Fuchs, P. Matzinger, Semin. Immunol. 8 (1996) 271–280.
[16] S. Baumann, A. Krueger, S. Kirchhoff, P.H. Krammer, Curr. Mol. Med. 2 (2002) 257–272.
[17] D.A. Hildeman, Y. Zhu, T.C. Mitchell, J. Kappler, P. Marrack, Curr. Opin. Immunol. 14 (2002) 354–359.
[18] R.C. Budd, Curr. Opin. Immunol. 13 (2001) 356–362.
[19] Y. Guilloux, X.F. Bai, X. Liu, P. Zheng, Y. Liu, Cancer Res. 61 (2001) 1107–1112.
[20] R.J. De Boer, A.S. Perelson, J. Theor. Biol. 175 (1995) 567–576.
[21] C.A. Janeway, Jr., Annu. Rev. Immunol. 20 (2002) 1–28.
[22] C.A. Janeway, Jr., C.C. Goodnow, R. Medzhitov, Curr. Biol. 6 (1996) 519–522.
[23] C.A. Janeway, Jr., Immunol. Res. 19 (1999) 107–118.
[24] R. Medzhitov, C.A. Janeway, Jr., Semin. Immunol. 12 (2000) 185–188 (discussion 257–344).

<a id='83b41c44-fada-40bf-b2f3-c1130ea53d93'></a>

25. L.A. Loeb, Cancer Res. 61 (2001) 3230-3239.
26. E. Wang, G.Q. Phan, F.M. Marincola, Expert Opin. Biol. Ther. 1 (2001) 277-290.
27. Y. Zhou, M.L. Bosch, M.L. Salgaller, J. Immunother. 25 (2002) 289-303.
28. F. Lehmann-Grube, Virol. Monogr. 10 (1971) 1-173.
29. A.R. Thomsen, A. Nansen, S.O. Andreasen, D. Wodarz, J.P. Christensen, Philos. Trans. R. Soc. London Ser. B 355 (2000) 1031-1041.
30. E.S. Rosenberg, M. Altfeld, S.H. Poon, M.N. Phillips, B.M. Wilkes, R.L. Eldridge, G.K. Robbins, R.T. D'Aquila, P.J. Goulder, B.D. Walker, Nature 407 (2000) 523-526.
31. F. Lechner, D.K. Wong, P.R. Dunbar, R. Chapman, R.T. Chung, P. Dohrenwend, G. Robbins, R. Phillips, P. Klenerman, B.D. Walker, J. Exp. Med. 191 (2000) 1499-1512.
32. D.H. Kirn, F. McCormick, Mol. Med. Today 2 (1996) 519-527.
33. K. Raj, P. Ogston, P. Beard, Nature 412 (2001) 914-917.
34. C.R.M. Bangham, S.E. Hall, K.J.M Jeffrey, A.M. Vine, A. Witkover, M.A. Nowak, D. Wodarz, K. Usuku, M. Osame, Philos. Trans. R. Soc. London Ser. B 354 (1999) 691-700.
35. D. Wodarz, M.A. Nowak, C.R.M. Bangham, Immunol. Today 20 (1999) 220-227.
36. R.S. Fujinami, Trends Microbiol. 9 (2001) 377-381.
37. B.T. Rouse, S. Deshpande, Rev. Med. Virol. 12 (2002) 107-113.
38. J. Folkman, Mol. Med. 1 (1995) 120-122.
39. J.W. Uhr, R. Marches, Semin. Cancer Biol. 11 (2001) 277-283.
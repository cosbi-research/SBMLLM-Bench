<a id='d142f04f-4616-4242-8543-76d7a1437314'></a>

Journal of Theoretical Biology 265 (2010) 336-345

<a id='6e5cf054-120f-4cb1-a18d-475f9259ad96'></a>

<::logo: Elsevier
NON SOLLUS
A detailed illustration of a tree with a figure tending to it, accompanied by the text "ELSEVIER" in orange below.::>

<a id='d6c3a2df-d420-45aa-a3e3-42208cada246'></a>

Contents lists available at ScienceDirect

# Journal of Theoretical Biology

journal homepage: www.elsevier.com/locate/yjtbi

<a id='098e0f97-8a3b-4e7d-babb-6dd33a717cb7'></a>

<::A journal cover with a marbled green and white background. At the top left, there's a small emblem. The title "Journal of Theoretical Biology" is prominently displayed in red serif font, with "Journal of" in a smaller size above "Theoretical Biology".
: cover::>

<a id='b48abc51-5f05-472a-944d-257e9c59ebf2'></a>

Tumour suppression by immune system through stochastic oscillations
Giulio Caravagna a,*,1, Alberto d'Onofrio b,1, Paolo Milazzo a, Roberto Barbuti a

a Dipartimento di Informatica, Università di Pisa, Largo Pontecorvo 3, 56127 Pisa, Italy
b Department of Experimental Oncology, European Institute of Oncology, Via Ripamonti 435, 20141 Milano, Italy

<a id='d54ed263-4f27-4a2a-b526-c5bae3a3ff51'></a>

## ARTICLE INFO

_Article history:_
Received 26 November 2009
Received in revised form
5 May 2010
Accepted 8 May 2010
Available online 16 May 2010

_Keywords:_
Tumour
Immune system
Immune surveillance
Immunotherapy
Stochastic Hybrid model

<a id='71497d04-2494-4f57-b2e9-4a362543b64f'></a>

ABSTRACT
The well-known Kirschner-Panetta model for tumour-immune System interplay [Kirschner, D., Panetta, J.C., 1998. Modelling immunotherapy of the tumour-immune interaction. J. Math. Biol. 37 (3), 235–252] reproduces a number of features of this essential interaction, but it excludes the possibility of tumour suppression by the immune system in the absence of therapy. Here we present a hybrid-stochastic version of that model. In this new framework, we show that in reality the model is also able to reproduce the suppression, through stochastic extinction after the first spike of an oscillation.
© 2010 Elsevier Ltd. All rights reserved.

<a id='e83436da-e0f9-4c4a-bcf1-a46bc62b6bde'></a>

1.  **Introduction**

The tumour–immune system interaction takes place because tumour cells are characterised by a vast number of genetic and epigenetic events leading to the appearance of specific antigens, called neoantigens, that trigger antitumoural actions by the immune system (Pardoll, 2003). These observations provided a theoretical basis (Burnet, 1957) to the empirical hypothesis of immune surveillance, i.e. that the immune system may act to control and also, in some case, to eliminate tumours (Ehrlich, 1909). Only in recent years has the study of cancer immunobiol-ogy accumulated a sufficient amount of evidence to show that tumours may be suppressed by immune system effectors. This has been made possible by the application of new molecular techniques and by performing a large number of epidemiological studies (Dunn et al., 2004).

<a id='1c02fc3e-7f9a-422a-b9a3-75c54e2e80e2'></a>

The competitive interaction between tumour cells and the immune system involves a considerable number of events and molecules in an extremely complex way. As a consequence, the immune system is not able to eliminate a neoplasm in all cases, since it may escape from its control. Of course, a dynamic equilibrium may also be established, such that the tumour may survive in a microscopic steady state, which is undetectable by diagnostic equipment (d'Onofrio, 2007). However, let us consider

<a id='01f5444c-81dd-47ba-80bc-11638d6bb583'></a>

--- 
* Corresponding author.
_E-mail addresses_: caravagn@di.unipi.it (G. Caravagna),
alberto.donofrio@ifom-ieo-campus.it (A. d'Onofrio), milazzo@di.unipi.it
(P. Milazzo), barbuti@di.unipi.it (R. Barbuti).
1 Equal contributors.

<a id='7b65cf64-4c8d-421e-9861-aa3498f069cf'></a>

0022-5193/$- see front matter  2010 Elsevier Ltd. All rights reserved.
doi:10.1016/j.jtbi.2010.05.013

<a id='aa33a056-e4e4-4cb2-95ec-f9fa0c96d1a9'></a>

a tumour which is constrained by the immune system in a microscopic steady state. On the one hand, the presence of a small colony of tumour cells may result in metastases. On the other hand, over a long period of time, a significant fraction of the mean human life span, according to Dunn et al. (2004), the neoplasm may develop multiple strategies to circumvent the action of the immune system (Whiteside, 2002; Pardoll, 2003; Dunn et al., 2004; Vicari et al., 2002). This, in the long term, may allow it to evade immune surveillance and to re-commence growing to its carrying capacity. The tumour has itself adapted to survive in a hostile environment, in which the antitumour immune response is activated (d'Onofrio, 2007; Cattani et al., 2010).

<a id='99999ab5-f87b-4130-abb0-697b7c4699d3'></a>

However, the tumour-immune system interaction may also show attractors that are different from a constant equilibrium, namely oscillations. In fact, one may observe both 'short term-small amplitude' oscillations (Kennedy, 1970; Vodopick et al., 1972; Gatti and et al., 1973; Mehta and Agarwal, 1980) and patterns of remission-recurrence such as alternation of long phases of dormancy (where a fallacious apparent immune surveillance seems reached) followed by phases where the tumour seems to escape (Tsao et al., 1997; Blumberg et al., 1990; Sohrabi et al., 1980). Finally, the study of the tumour-immune system interaction led to the proposal and implementation of an interesting therapeutic approach: immunotherapy (De Vita et al., 2008), consisting in stimulating the immune system in order to better fight, and hopefully eradicate, a cancer. The basic idea of immunotherapy is simple and promising, but the results obtained in medical investigations are globally controversial (Agarwala, 2003; Bleumer et al., 2003; Kaminski et al., 2004).

<!-- PAGE BREAK -->

<a id='aecd7c9e-de90-4b8b-a1e3-59ea1842da94'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='557e5bee-6831-4735-9486-af122b0bf0fa'></a>

337

<a id='d1bfd33b-a7b9-4c9e-a506-aa64271800b9'></a>

Regarding the mathematical modelling of the above interac-tions, many papers have appeared using either a finite dimensional approach (De Lisi and Rescigno, 1977; Kirschner and Panetta, 1998; Stepanova, 1980; Kuznetsov et al., 1994; Kuznetsov and Knott, 2001; Galach, 2003; Szymanska, 2003; De Vladar and Gonzalez, 2004; Nani and Freedman (2000); De Pillis et al., 2005; d'Onofrio, 2005, 2007; Cappuccio et al., 2006; Kronik et al., 2008; Kirschner and Tsygvintsev, 2009) or the theory of kinetic active particles (Bellomo and Delitala, 2008; Bellomo et al., 2008).

<a id='7f6e329c-7c3a-4ba7-a047-969a992ccd8c'></a>

Some of the above works focus on sustained oscillations that are related to delays in the process of detecting the presence of the tumour by the immune system (Galach, 2003; Szymanska, 2003; d'Onofrio et al., 2010), whereas others show that oscillations are also possible in the case of absence of such delays (d'Onofrio, 2006; Kirschner and Panetta, 1998). For example, in d'Onofrio (2006) an analytical study is conducted and conditions are stated for the existence and uniqueness of a limit cycle for a large class of models.

<a id='53db1f02-1c1f-49e4-81a8-7149ea37b29c'></a>

In Kirschner and Panetta (1998), proposed a largely influential tridimensional deterministic model, whose variables are tumour cells, effector cells and the concentration of interleukins. This model is able to explain both the above type of tumour size oscillations, as well as, of course, constant equilibria, both macroscopic and microscopic. The global behaviour of the model was recently investigated in Kirschner and Tsygvintsev (2009). Although a vast array of behaviours is mimicked by the solutions of the Kirschner–Panetta model, the tumour-free equilibrium is unstable for all biologically meaningful values of the parameters of the model.

<a id='b091586c-39c4-4ba2-a64f-f6c33e5ee05c'></a>

However, we noticed that in the transitory oscillations before reaching a stable equilibrium, and also in sustained stable large oscillations, very small values of the tumour size are predicted by this deterministic model. These values could be considered well below the level of detection but they cannot be considered as eradication. Thus, we propose here a stochastic version of the Kirschner–Panetta model, which may better describe the dynamics of the tumour–immune system interplay in the case of low levels of both tumour and immune cells. In the bio–mathematical literature it has been stressed how deterministic models may exhibit oscillating solutions having no counterpart in their corresponding stochastic version, where population extinction is, instead, predicted (Nasell, 2002).

<a id='7c7ffbae-5634-4e07-9d98-19ed8affc329'></a>

In order to assess whether this also happens in the Kirschner-
Panetta model, we propose here an extended model where the
dynamics of tumour cells and immune effectors are described by a
suitable stochastic process, whereas the dynamics of the con-
centration of interleukins is modelled by an ordinary differential
equation. Since the stochastic processes are interlinked with the
dynamics of the interleukins (and vice versa), the main features of
this model are that it contains time-dependent propensity
functions and combines both the features of deterministic and
stochastic models.

<a id='ed12af67-4df7-4b5f-a926-71314cd065ec'></a>

This provides a useful tool through which we aim to offer a theoretical contribution towards a better understanding of the dynamical aspects of a key phenomenon: the suppression of a tumour by the immune system. In particular, we focused on: (i) assessing the role of antigenicity of tumour cells (Kirschner and Panetta, 1998) in shaping those dynamics; (ii) investigating the interplay between the so-called intrinsic noise and the macroscopic tendency of tumour-immune system interplay to oscillate (d'Onofrio, 2006; Kirschner and Panetta, 1998).

<a id='520674e9-6fef-4eff-919b-c656bf1438e5'></a>

The present work is organised as follows: in Section 2 we
present the Kirschner–Panetta model and we summarise its main
features, with particular regard to those linked to the onset of
sustained oscillations. In Section 3 we propose a hybrid stochastic

<a id='aea17fb6-7f1f-4fa5-bd09-a494a3d4f2f7'></a>

version of the model. In Section 4.1 we use the stochastic
Kirschner-Panetta model to investigate the role of stochasticity in
tumour suppression. The work ends with some concluding
remarks.

<a id='556a71da-ec1a-4b6c-bd1a-724e314eb0b5'></a>

## 2. Overview of the Kirschner-Panetta model

In Kirschner and Panetta (1998) the following model of the dynamics of tumour-immune system interaction was proposed

$T'_* = rT_*(1-bT_*) - \frac{aT_*}{g_2+T_*}E_*$

$E'_* = \frac{p_1I}{g_1+I}E_* - \mu_2E_* + cT_* + s_1$

$I' = \frac{p_2T_*E_*}{g_3+T_*} - \mu_3I + s_2 \quad (1)$

<a id='79cbe9c8-7bd4-43ed-9998-3f1acea6d9d9'></a>

where T*(*t*), E*(*t*) and *I*(*t*) denote, respectively, the densities of tumour cells, effectors of the immune system and interleukins. The tumour induces the recruitment of the effectors at a linear rate *cT*, thus, the parameter *c* may be seen as a measure of the immunogenicity of the tumour, i.e. 'a measure of how different the tumour is from self (Kirschner and Panetta, 1998). The proliferation of effectors is stimulated by the interleukins. A continuous infusion immunotherapy is delivered; in the general case, both effectors and interleukins are injected at rates *s*₁ ≥ 0 and *s*₂ ≥ 0. The source of interleukin is modelled as linearly depending on effectors, and it also depends on the tumour burden. Finally, the average lifespan of effectors is *μ*₂⁻¹ and the average degradation time for interleukin is *μ*₃⁻¹.

<a id='c09e5ea6-21bf-4a76-a55c-85465a02a260'></a>

In the absence of therapy (s1 = s2 = 0), the main results obtained in Kirschner and Panetta (1998) are the following: the unique tumour suppression equilibrium point (0,0,0) is always unstable, there is a value 0 < c0 ≪ 1 such that for 0 < c < c0 there are three equilibria of which two are unstable and one is locally stable. As it is intuitive, the antigenicity of the tumour being very small, this locally stable equilibrium is very close to the carrying capacity in the absence of immune response. Furthermore, there is a value cmax > 0 such that if c ∈ (c0, cmax) there is a unique periodic solution; the period and amplitude of the limit cycle decreases as far as c approaches cmax. Finally, when c > cmax there is a unique globally stable equilibrium, which is reached through damped oscillations. Again, this equilibrium is a decreasing function of c, and its size is small due to the high immunogenicity of the tumour. The presence of a very small equilibrium state that is not detectable might seem to be a sub- optimal outcome, so that one may consider it as practically equivalent to tumour suppression. However, it must be remem- bered that, as we mentioned in the introduction, the Volterrian interaction between tumour cells and the immune system is also evolutionary: tumour cells evolve their ability to evade the control (Dunn et al., 2004; d'Onofrio, 2007) and, as a consequence, no microscopic steady state may be considered permanent and safe for the patient (d'Onofrio, 2007).

<a id='3bf2f64d-183a-4ca0-b08f-0778a7b4d51f'></a>

Thus, we note that this model explicitly precludes the possibility of tumour suppression, which follows from the absence of a baseline influx of effectors. We remark that this holds in the absence of therapy, and that is the case which we will consider in the rest of the paper. In the presence of therapies, the behaviour of the system becomes more complex, but in all the possible combinations of the parameters it is possible to find regions where globally stable limit cycles exist, as well as regions where there is cancer suppression. Moreover, there is a threshold value such that, for the injection rate of the interleukins greater

<!-- PAGE BREAK -->

<a id='4b00714b-3eef-4c7a-8ab4-c60bcabd21ed'></a>

338

<a id='9a736fcf-071a-4a19-b106-3cbd915e6895'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='191bfaeb-f2ca-4112-850c-a31f7d3e86a1'></a>

than such a value, there is an unbounded growth of effectors,
leading to capillary leak syndrome.

<a id='ff8c90c8-4b1c-4ad3-aada-bc0f93518bf1'></a>

### 3. A hybrid stochastic version of the Kirschner–Panetta model

In this section we define a hybrid stochastic version of the model (1). In principle, indeed, before defining a stochastic equivalent of the model (1), we should switch from variables representing densities to variables representing the total number of cells. Thus, we would obtain an ODE model from which it would be straightforward to obtain a three dimensional stochastic process. However, since the molecular weight of interleukins is 15,000 Da, the average number of proteins is huge. As a consequence, we may assume that the dynamics of I(t) is well approximated by a linear differential equation with randomly varying coefficients, which, however, in the intervals between two consecutive stochastic events are evidently constant.

<a id='35517a8d-ec27-4305-90b5-2c36b69478c5'></a>

As a consequence, we introduce as a new parameter the
volume V of interest (e.g. the blood and bone marrow volumes for
leukaemia) and we define

<a id='3c8fc38b-1199-413e-91b5-d457c382427b'></a>

$$T_* = \frac{T}{V}, \quad E_* = \frac{E}{V}$$ (2)
thus obtaining
$$T' = rT\left(1 - \frac{b}{V}T\right) - \frac{aT}{g_2V+T}E$$

<a id='03756f73-6b25-4b81-85f3-f98cd484a2f4'></a>

E' = \frac{p_1I}{g_1+I} E - \mu_2E + cT + Vs_1

I' = \frac{p_2}{V} \frac{TE}{g_3V+T} - \mu_3I + s_2 (3)

<a id='4d83937d-08de-44bd-bf0f-6554defc022c'></a>

From the above model, we define a hybrid stochastic process, where a bi-dimensional stochastic process is linked to a scalar differential equation ruling the dynamics of the concentration of interleukins. Namely, in the interval between the _n_-th event (at time denoted as _t_n) and the (_n_+1)-th event, the above mentioned ODE is

<a id='b73dafc6-c884-42bc-bac2-09821b73e0a6'></a>

I' = \frac{p_2}{V} \frac{T(t_n)E(t_n)}{g_3V+T(t_n)} + s_2-\mu_3I (4)

<a id='54a70623-aef8-4090-aab7-4aff98329fab'></a>

which, since in ($t_n$,$t_{n+1}$) the other two state variables are constant,
is a linear ordinary differential equation with constant input and
constant coefficients. Thus, the solution of (4) in ($t_n$,$t_{n+1}$) has the
following analytical form:

<a id='0837e6da-8042-4c39-8580-1428c15c1cdb'></a>

I(t) = B_n + (I_n - B_n)Exp(-\mu_3(t - t_n))

(5)

<a id='deaa6ecd-f336-4597-bb93-c8f3ef302261'></a>

where Bn, for the sake of notation simplicity, is the following function of (Tn,En):

<a id='9eaeb6e9-3f78-4e5f-bfdf-0cd347714de5'></a>

Bn := 1/μ3 ( p2 T(tn)E(tn) / (V g3V+T(tn)) + s2 ) .
(6)

<a id='b90e997e-04fe-4cfe-9e6d-94ab47b83b86'></a>

The stochastic model of the evolution of the tumour cells and the effector cells is defined by the following events and the corresponding propensity functions:

(R1) T ⟼ T+1          a1 = r2T
(R2) T ⟼ T−1          a2 = r2bV−1T2
(R3) T ⟼ T−1          a3 = (aTE)/(g2V+T)
(R4) E ⟼ E+1          a4(t) = p1E(I(t)/(g1+I(t)))
(R5) E ⟼ E−1          a5 = μ2E
(R6) E ⟼ E+1          a6 = cT
(R7) E ⟼ E+1          a7 = Vs1

<a id='97c6ffff-2090-4917-8162-577e31db0f6f'></a>

Notice that all the propensity functions except for a₄(t) are time-constant. In order to analyse this model, we need to define an

<a id='28b969e4-1635-4008-947c-396a60e4b39d'></a>

algorithm for computing its time evolution. Although in the literature algorithms for simulating hybrid systems have been presented (Salis and Kaznessis, 2005; Alfonsi et al., 2004), in this model we combine the hybrid approach with time-dependent propensity functions (Lecca, 2006; Anderson, 2007). Consequently, we define, based on the main ideas of Gillespie's algorithm (Gillespie, 1976, 1977), a stochastic evolution algorithm for this hybrid model.

<a id='d30ada2f-cc96-4edc-bd8b-c53f2b4ab3f3'></a>

The event-induced changes in the values of T and E can be represented by the following seven-dimensional vectors
v_T = (1,-1,-1,0,0,0,0)^Tr
and
v_E = (0,0,0,1,-1,1,1)^Tr.

<a id='3db391c2-e34a-466a-8b1f-d901bb23e96c'></a>

Namely, $v_T[i]$ and $v_E[i]$ denote how the event $R_i$ affects the population $T$ and $E$, respectively. Furthermore, we denote with $S$ the set of time-constant propensity functions, namely the set {$a_1, a_2, a_3, a_5, a_6, a_7$}.

<a id='92e025bd-cfcd-46b1-9e53-8e9070c84640'></a>

The unique time varying propensity is given by the formula

$a_4(t) = E_n \frac{p_1 I(t)}{g_1 + I(t)}$

<a id='521f72c0-ff8c-4f40-8de6-3da308d0a640'></a>

We define the function

$A(\tau) = \int_{t_n}^{t_n + \tau} a_4(t) dt.$

<a id='617be9fc-e296-4f34-8484-6858751eaf3b'></a>

Given the analytical form of I(t) in formula (5), A(τ) reads as follows:

$A(\tau) = \frac{p_2 E_n}{(B_n + g_1)\mu_3} \left(\tau \mu_3 (B_n + g_1) + g_1 \text{Ln} \left(\frac{g_1 + I_n}{-B_n + e^{\tau \mu_3 (B_n + g_1)} + I_n}\right)\right).$ (7)

<a id='2b79b399-1b0e-4d3e-a5cf-d721846fd82f'></a>

The exact simulation algorithm for the hybrid system under study
can consequently be defined as follows:

1. Input the initial state: $(T_0, E_0, I_0)$ and the maximum simulation
time $\Theta_M$.
2. Initialise the time $t=t_0$ and the system state $(T,E,I)=(T_0,E_0,I_0)$.
3. If $t\ge\Theta_M$ end the simulation, else
4. Evaluate all the $a_j$ with $j\in S$ and their sum $a_0=\sum_{j\in S}a_j$.
5. The putative time for the next reaction $\tau$ is determined by
solving the following transcendental equation:

$A(\tau)+a_0\tau=\chi$,

where $\chi$ is a random number with distribution $Exp(1)$. For the
numerical solution of this equation we used Newton-Raphson
method.
6. Given a random number $r$ uniformly distributed in the interval
$[0,1]$, the next event is determined in accordance with

$\sum_{i=1}^{j-1}a_i<r\cdot a_0\le\sum_{i=1}^{j}a_i$

7. Update the system state to $(T+v_T[j],E+v_E[j],I(t+\tau))$ and the
clock to $t+\tau$.
8. Go to step 3.

<a id='efd89e9f-4d7d-405b-a901-7fb610c025c2'></a>

Finally, in order to perform the simulations of both the
deterministic and stochastic model, we have to define numerical
values for the parameters.

<a id='089168f8-459c-4e6d-b57a-8a59a649371a'></a>

Concerning the parameters, we used the values and ranges given in Refs. Kirschner and Panetta (1998) and Kirschner et al. (2004) as listed in Table 1. Note that those values pertain to mice, since they were taken from the influential papers (DeBoer et al., 1985; Kuznetsov et al., 1994), where accurate fitting of real data concerning laboratory animals were performed.

<!-- PAGE BREAK -->

<a id='8cc53246-18e4-43da-abb3-6ca55f6d6b58'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='aa9c8627-74d2-4c46-b017-b60fcbe3c6a2'></a>

339

<a id='9eb1dc1e-7f5a-4b07-a843-1ee80bd9e3fe'></a>

Table 1
Parameters used in most of the simulations of the model.
<table id="3-1">
<tr><td id="3-2">Parameter</td><td id="3-3">Value</td><td id="3-4">Measure unit</td><td id="3-5">Description</td></tr>
<tr><td id="3-6">r₂</td><td id="3-7">0.18</td><td id="3-8">days⁻¹</td><td id="3-9">Baseline growth rate of the tumour</td></tr>
<tr><td id="3-a">b</td><td id="3-b">10⁻⁹</td><td id="3-c">ml⁻¹</td><td id="3-d">Carrying capacity of the tumour</td></tr>
<tr><td id="3-e">a</td><td id="3-f">1</td><td id="3-g">ml × days⁻¹</td><td id="3-h">Baseline strength of the killing rate by immune effectors</td></tr>
<tr><td id="3-i">g₂</td><td id="3-j">10⁵</td><td id="3-k">ml⁻¹</td><td id="3-l">50% Reduction factor of the killing rate by immune effectors</td></tr>
<tr><td id="3-m">P1</td><td id="3-n">0.1245</td><td id="3-o">ml × days⁻¹</td><td id="3-p">Baseline strength of the interleukin-stimulated growth rate of effectors</td></tr>
<tr><td id="3-q">g1</td><td id="3-r">2 × 101</td><td id="3-s">ml⁻¹</td><td id="3-t">50% Reduction factor of interleukin-stimulated growth rate of effectors</td></tr>
<tr><td id="3-u">μ2</td><td id="3-v">0.03</td><td id="3-w">days⁻¹</td><td id="3-x">Inverse of average lifespan of effectors</td></tr>
<tr><td id="3-y">C</td><td id="3-z"></td><td id="3-A">time⁻¹</td><td id="3-B">Tumour antigenicity</td></tr>
<tr><td id="3-C">P2</td><td id="3-D">5</td><td id="3-E">ml × days⁻¹</td><td id="3-F">Baseline strength of production rate of interleukins</td></tr>
<tr><td id="3-G">g3</td><td id="3-H">103</td><td id="3-I">ml⁻¹</td><td id="3-J">50% Reduction factor of production rate of interleukins</td></tr>
<tr><td id="3-K">μ3</td><td id="3-L">10</td><td id="3-M">time⁻¹</td><td id="3-N">Loss/degradation rate of IL2</td></tr>
<tr><td id="3-O">V</td><td id="3-P">3.2</td><td id="3-Q">ml</td><td id="3-R">Blood and bone marrow volumes for leukaemia</td></tr>
<tr><td id="3-S">S1</td><td id="3-T">0.0</td><td id="3-U">ml⁻¹ x days⁻¹</td><td id="3-V">Injection rate of effectors for adoptive cellular immunotherapy</td></tr>
<tr><td id="3-W">S2</td><td id="3-X">0.0</td><td id="3-Y">ml⁻¹ × days⁻¹</td><td id="3-Z">injection rate of interleukins for immunotherapy</td></tr>
</table>
Tumour santigenicity c is the only variable parameter that is reported in the description of each simulation.

<a id='9d9b9628-770b-4022-9fad-874f6d8e5d91'></a>

As far as parameter V is concerned, by taking into account that in a chimeric mouse the body weight ranges from 20 g for female mouse up to 40 g, and that their blood volume ranges from 5.8 ml per 100 g up to 8 ml per 100 g, it follows that a reasonable range for V is from 1.16 ml up to 3.2 ml, in our simulations we assumed:
V=3.2 ml.

<a id='6290117f-f5bf-4fe7-a1a3-a6bb677666fa'></a>

In our simulations we focused on two key parameters: c, which reflects the antigenic potential of the tumour, and s₁ which represents the injection rate of effectors for adoptive cellular immunotherapy.

<a id='5b9d1e5e-5073-434e-a98f-fed4608213d3'></a>

**4. Stochastic behaviour**

*4.1. Stochastic suppression of tumour in absence of immunotherapy*

<a id='e168d4c0-7a49-4f51-aad1-bb20a8c108a9'></a>

In Kirschner and Panetta (1998) it has been shown that the antigenicity parameter _c_ is a key parameter for model (1) since, for very low values of _c_, the tumour burden reaches values near its carrying capacity, for large values of _c_ the tumour reaches a small steady state, whereas, for intermediate values, lying in a quite narrow range $\mathcal{R} = (C_{min}, C_{max})$, there is the onset of oscillations through Hopf bifurcations at $C=C_{min}$ and at $C=C_{max}$. This is biologically sound since, of course, the immunogenicity of a tumour is an essential factor so that the immune system may attack the tumour with some effectiveness.

<a id='42449c27-2f9f-4c0a-86cc-5e76c4803ee1'></a>

However, simulating (3) we noticed that, although for c
slightly higher than Cmin the maximum value attained during
the oscillations may be of the order of the carrying capacity, the
minima of T(t) seem very small. Indeed, if we plot time courses of
tumour size in a Log 10 scale, as in Fig. 1, we may easily see that
there are temporal ranges where the deterministic setting
predicts that T(t) < 1 cell.

<a id='57f0fd37-8e87-4fa0-9898-7b1b5ab7d1b4'></a>

This suggested to us that a range Ω ⊂ R might exist where, by using the stochastic version of the Kirschner–Panetta model, the oscillating interplay tumour–effectors–interleukins might lead to the eradication of the disease.

<a id='f23411e3-d8ed-4813-96a6-c5772e1269be'></a>

This hypothesis was confirmed by the stochastic simulations. All the simulations of the hybrid model were done by using a Java implementation of this model and of the algorithm presented in Section 3. The Java source code of the implementation is freely available at the URL: http://www.di.unipi.it/msvbio.

<a id='db4ecca3-3fac-4901-b64f-5b7b5e1f5a6a'></a>

We present, in Fig. 2, two realisations (for c=0.01 and for c=0.02) of the stochastic process corresponding to the deterministic time-courses shown in Fig. 1. We set the worst

<a id='11bb7d6a-be62-4cbe-affe-a478098e057a'></a>

possible initial conditions for effectors and interleukins, i.e.
E(0)=0, I(0)=0.

<a id='886eb3af-afd8-4383-8df5-cc2c904fe0a4'></a>

It is immediately noticeable that the stochastic behaviour is
deeply different from that predicted by the deterministic model
since, in the stochastic simulation, only the first spike of the
oscillation is achieved and then the tumour eradication is reached.
In particular, with c=0.01 eradication is observed around day 160
and with c=0.02 around day 120.

<a id='4bc5e503-defe-4fac-91a8-cf5b89b086ee'></a>

Thus, denoting as _t_er the random variable time of occurrence of the eradication we calculated the associated empirical probability density Q(_t_er; _c_) with _c_=0.02. The result is shown in Fig. 3. Such a density, computed over 103 stochastic runs of the model, has a peak at around day 130; all the simulations have shown eradication with a simulation time bounded to 200 days.
Note that the stochastic simulations for some values of _c_ become computationally intractable for sample hundreds of runs. For example, at _c_=0.01 a single stochastic run took almost 70 h on a Apple MAC2.

<a id='c5941559-dac2-47ce-a290-400b7f9128e6'></a>

Consequently, we decided to perform a deeper analysis on the deterministic model, which is much less computationally expensive, considering as eradication the first time instant in which T(t) < 1. We calculated, for the values of Log10(c) in [-4;-1] the average eradication time <ter>(c) in function of c, as reported in Fig. 4. We note that for c approaching Cmin the putative eradication time becomes very large. However, notice that in reality the patient dies before that the carrying capacity is reached. Moreover, after decreasing for nearly all the range Ω, the curve has a minimum and the eradication time restarts growing. Notice that for c=0.02 (~Log10(c) = -2.6) the analysis of the deterministic model gives roughly similar predictions of the stochastic behaviour observed in Fig. 3.

<a id='e0141415-a4ef-4c96-a754-11ce55d4091a'></a>

In order to assess the influence of non-null initial value for effectors, in Fig. 5, we show the effect of increasing E₀ on the empirical probability density of t_er with c=0.02 in the stochastic model. These densities are computed over 10² stochastic runs. All the initial configurations we considered are of the form (T₀,E₀,I₀)=(1,10ⁱ,0) with i=1,...,5 In particular, for i=1,2,3 the densities have the peaks in the interval [120; 140] while, for i=4,5 the densities become bimodal with peaks in the intervals [120; 140] and [0;10]. For the particular initial configurations, which are not shown in the figure, having 10⁶ or

<a id='aa315cf2-5ce8-4f91-b8f6-095ed1b333c6'></a>

2 Apple Macbook 2.4 GHz Intel Core 2 Duo, 4 GB 1067 MHz running Mac OS X

<a id='a4c16c4b-5bdc-4217-b0a5-880ba1c39e7d'></a>

10.5.8.

<!-- PAGE BREAK -->

<a id='3685669c-0f5b-476f-8c27-bd9bb56236c6'></a>

340

<a id='41bef16a-995a-4f59-8f96-4543dbebdc4c'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='0e98a8f1-7c36-46ae-87a6-4301bf0182ab'></a>

<::chart: The figure displays four plots arranged in a 2x2 grid, illustrating the deterministic dynamics of T(t) over time (days). The upper two panels correspond to c=0.01, and the lower two panels correspond to c=0.02. The left panels show T in a natural scale, while the right panels show Log10(T). All x-axes are labeled 'time (days)'.

-   **Top-left panel (c=0.01, natural scale)**: The y-axis is labeled 'T' and ranges from 0 to 4x10^8. The x-axis ranges from 0 to 2500 days. The plot shows two distinct, sharp peaks, one around 200 days and another around 1900 days, both reaching approximately 4.5x10^8. Between and after these peaks, T remains near zero.
-   **Top-right panel (c=0.01, Log10 scale)**: The y-axis is labeled 'Log10 (T)' and ranges from -5 to 5. The x-axis ranges from 0 to 175 days. The curve starts near Log10(T)=0, increases smoothly to a peak of about 6 at approximately 150 days, then sharply drops to a value below -5, where it fluctuates around -7.
-   **Bottom-left panel (c=0.02, natural scale)**: The y-axis is labeled 'T' and ranges from 0 to 1.2x10^6. The x-axis ranges from 0 to 1000 days. The plot shows four distinct, sharp, periodic peaks, each reaching approximately 1.2x10^6. These peaks occur around 100, 350, 600, and 850 days, with T remaining near zero between peaks.
-   **Bottom-right panel (c=0.02, Log10 scale)**: The y-axis is labeled 'Log10 (T)' and ranges from -2 to 6. The x-axis ranges from 0 to 175 days. The curve starts near Log10(T)=0, increases smoothly to a peak of about 6 at approximately 100 days, and then decreases smoothly to a value below -2 by 175 days.

Fig. 1. Deterministic dynamics of T(t) for c=0.01 (upper panels), and c=0.02 (lower panels). In left panels the curves are plotted in natural scale, whereas in right panels the plot is in Log 10 scale. The other parameters are as in Table 1.::>

<a id='bef90802-f11b-4277-9899-7be5056a258a'></a>

<::Figure 2: Two line graphs, side-by-side, depicting the stochastic dynamics of T(t). Both graphs share the same x-axis labeled "time (days)" ranging from 0 to 200, with major ticks every 20 days. The y-axis for both is labeled "T".The left panel, for c=0.01, shows a line graph where T starts at 0, rises sharply to a peak of approximately 4.5e+08 between 140 and 150 days, and then rapidly declines back to 0. The y-axis ranges from 0 to 4.5e+08.The right panel, for c=0.02, shows a line graph where T starts at 0, rises sharply to a peak of approximately 1.2e+06 between 90 and 100 days, and then rapidly declines back to 0. The y-axis ranges from 0 to 1.4e+06.Fig. 2. Stochastic dynamics of T(t) for c=0.01 (left panel), and c=0.02 (right panel). The other parameters are as in Table 1. In both cases there is tumour suppression, and further spikes of the original oscillations disappear.: chart::>

<a id='8ec2d056-c98b-4434-9ae3-ef71bed944cd'></a>

more initial effectors, all the eradications are observed almost instantaneously.

<a id='cf9dabc9-fb59-4abc-a5e6-4b8200087824'></a>

The same kind of analysis was performed by varying the initial
numbers of interleukins. In particular, in Fig. 6, we show the effect

<a id='3eb36712-31cd-41ce-851b-510c2e8fe635'></a>

of increasing $I_0$ on the empirical probability density of $t_{er}$ with $c=0.02$ in the stochastic model. Also these densities are computed over $10^2$ stochastic runs. All the initial configurations we considered are of the form $(T_0, E_0, I_0)=(1,0, 10^i)$ with $i=1,2,4,6$.

<!-- PAGE BREAK -->

<a id='52b60232-7a31-4326-8888-f0043a6d319e'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='47f43dfc-a8b3-4a63-9158-d86bf623bcf8'></a>

341

<a id='7f64a281-e555-43b4-be9a-0511889e7970'></a>

<::line chart: A probability density plot. The y-axis is labeled "density" and ranges from 0 to 0.08. The x-axis is labeled "eradication time" and ranges from 110 to 160. A bell-shaped curve shows the empirical probability density, peaking at approximately 0.052 around an eradication time of 127-128, and decreasing towards both ends of the x-axis.::>Fig. 3. Empirical probability density of t_er with c=0.02 computed over 10^3 stochastic runs. The other parameters are as in Table 1.

<a id='c12e84df-cbae-4d57-817c-5615502df764'></a>

In this case, unlike the previous ones, we observed single modal probability densities with peaks in the interval [110; 135].

<a id='a56ea336-5837-4cd7-a24c-b5e77ebb89d4'></a>

## 4.2. Stochastic oscillations in absence of immunotherapy
The stochastic version of the Kirschner–Panetta model exhibits stochastic oscillations for a small range of values of the antigenicity 0.03 ≈ < c < ≈ 0.032,

<a id='df8e7b97-03d2-434e-906a-499d98362b5c'></a>

whereas for higher values damped oscillations appears (i.e. with c=0.033 the system reaches an equilibrium with around 60,000 tumour cells). In Fig. 7 we show two examples of oscillations; for c=0.03 and for c=0.032. Note that in Fig. 7 we also plotted the minimum after the first spike of the oscillation.

<a id='1a4b57c4-7570-44bc-b6c7-c871065334ef'></a>

4.3. *Tumour suppression in the case of large c*

If the value of *c* is further increased the average value of the stochastic oscillations of tumour cells progressively reduces. The reduction is such that the suppression of the tumour gradually

<a id='8c767199-1ecc-4963-9e98-11a5d483ed45'></a>

<::chart: Two line plots are displayed side-by-side. Both plots share the y-axis label 'Eradication Time' and the x-axis label 'Log₁₀ [C]'. The left plot shows 'Eradication Time' on the y-axis ranging from approximately 0 to 1800, with major tick marks at 500, 1000, and 1500. The x-axis 'Log₁₀ [C]' ranges from -4.0 to -1.5, with major tick marks at -4.0, -3.5, -3.0, -2.5, and -2.0. The curve starts high on the left, decreases sharply, then gradually flattens before showing a slight dip and rise at the far right. The right plot is a zoomed-in view of the final part of the left plot. Its y-axis 'Eradication Time' ranges from 120 to 180, with major tick marks at 120, 130, 140, 150, 160, 170, and 180. The x-axis 'Log₁₀ [C]' ranges from -3.0 to -1.6, with major tick marks at -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, and -1.6. The curve in the right plot shows a decreasing trend, a flat section around 150, a sharp drop to around 120, and then a rise.::>Fig. 4. Eradication time vs. Log₁₀(c) for the deterministic model. The other parameters are as in Table 1. Left panel: complete plot, right panel: zoom to final part. 

<a id='ea8553b8-4f87-4e6e-ad9d-983e58375f46'></a>

<::chart: Two plots showing empirical probability density. The left plot shows density (y-axis, from 0.01 to 0.09) versus eradication time (x-axis, from 0 to 180) for c=0.02 and initial effector sizes E(0)=10^i with i=1 (solid line), i=2 (dashed line), and i=3 (semi-dashed line). The right plot shows density (y-axis, from 0 to 0.2) versus eradication time (x-axis, from 0 to 200) for c=0.02 and initial effector sizes E(0)=10^i with i=4 (solid line) and i=5 (dashed line). For each configuration, the density has been computed over 10^2 stochastic runs. The other parameters are as in Table 1.::>

<!-- PAGE BREAK -->

<a id='659f2c0c-0176-4626-aebe-2708d2c2ad6a'></a>

342

<a id='0be45c0b-19d1-4552-ae04-e1bfd0f0d7b8'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='f1a14eb4-1adf-4b84-bac3-3f428de0882e'></a>

reappears. For example, we performed a series of simulations by varying c (2000 simulations 2000 days long for each value of c), and we observed that at least one observed eradication occurred for c greater than a threshold value 13, the value for which two eradications over 2000 simulations of the stochastic process were observed. At c=30 tumour eradication was observed in 20% of simulations, and for c= 50 almost half of the simulations had the tumour eradication as outcome (956 out of 2000).

<a id='7b543619-7a7b-4cc3-b91d-f6b829e2ce07'></a>

In Fig. 8 one simulation of the stochastic process for c=71.1 is shown, whereas in Fig. 9 (left) we plotted the percentage of observed eradications in function of c. As far as the times when the first eradication is observed, we note that in many cases, the minimal eradication time is very small. Thus, we plotted in Fig. 9 (right) the modal value of t_erad for c∈ (13,71.5), i.e. the value of t_er for which the maximum number of eradications was observed.

<a id='2e37f757-5787-4f2e-a959-47002a13521f'></a>

4.4. Immunotherapy Although, as we stressed in the introduction, here we are essentially interested in investigating the effect of stochasticity in the unperturbed time course of a tumour, for the sake of <::chart: A 2D line plot titled "Fig. 6. Empirical probability density of t_er_ with c=0.02 and variable initial size of interleukins: _IL_(0)=10^i^ with i=1 (solid line), i=2 (dashed line), i=4 (semi-dashed line) and i=6 (dotted line). For each configuration the density has been computed over 10^2^ stochastic runs. The other parameters are as in Table 1.". The x-axis is labeled "eradication time" and ranges from 110 to 180. The y-axis is labeled "density" and ranges from 0.01 to 0.09. Four lines are plotted, representing the empirical probability density for different initial sizes of interleukins: the solid line (i=1) peaks around 0.067 at approximately 127; the dashed line (i=2) peaks around 0.058 at approximately 122; the semi-dashed line (i=4) peaks around 0.058 at approximately 120; and the dotted line (i=6) peaks around 0.055 at approximately 120. All lines show a similar bell-like shape, starting low, rising to a peak, and then gradually decreasing towards the x-axis, extending to eradication times beyond 150.::>

<a id='58f4c635-a796-45c6-9881-904c47434875'></a>

<::Line chart with an inset chart. The main chart displays 'T' versus 'time (days)'. The x-axis, labeled 'time (days)', ranges from 0 to 10000 in increments of 1000. The y-axis, labeled 'T', ranges from 0 to 450000 in increments of 50000. The plot shows a series of vertical oscillations, starting with a peak around 350000 at time 0, and then rapidly decreasing in peak amplitude before settling into a more stable oscillatory pattern with peaks around 225000-250000 and troughs near 0, extending across the full time range. The inset chart, located in the upper right, shows a zoomed-in or related plot. Its x-axis ranges from 128 to 142 in increments of 2. Its y-axis ranges from 160 to 210 in increments of 10. The inset plot is a line graph showing variations in value, starting around 205, dropping to about 185, rising to about 195, dropping significantly to around 160 near x-value 136, and then rising again to about 190 by x-value 142.: chart::>

<a id='0bd7086f-8df2-473e-9a32-b2ef55be4915'></a>

completeness, we briefly report some simulations of an adoptive cellular immunotherapy ($s_1 > 0$).

<a id='55d34d37-83b7-437e-8d83-1151f4337ef8'></a>

The deterministic setting is quite pessimistic since a therapy only eradicates for t→∞, so that after a therapy having a realistic finite time span the tumour restarts growing. Thus the maximum beneficial effect of an immunotherapy would be moving the state of tumour from the region of convergence of a macroscopic equilibrium (not compatible with the life of the host organism) to the basin of attraction of a small steady state.

<a id='22ed7c53-d1f6-4dbf-869f-e7dcf30cbabd'></a>

The stochastic simulations, instead, suggests that an immunotherapy may eradicate the disease in a finite time, as shown, for the case of an adoptive cellular immunotherapy (Fig. 10).

<a id='e6a01940-f920-448a-ab5c-43de6a40d62f'></a>

We focused on the antigenicity value c=10⁴ which is, for both the deterministic and stochastic models, a value such that no eradication is observed in the absence of therapy. Regarding the therapy, we modelled an adoptive cellular immunotherapy from day 70 to day 130 of simulation. We used s₁=0.0 for the first 70 days of simulation and, for the following days, we used s₁ = 10s ₁ₓ₅ where s ₁ₓ₅ is the threshold value for the local stability of the suppression in the deterministic setting (Kirschner and Panetta, 1998).

<a id='1a80cb94-4277-4868-978b-65de454d6c8a'></a>

<::chart: A line graph titled "Stochastic suppression for c=1.1 c*". The x-axis is labeled "time (days)" and ranges from 0 to 600. The y-axis is labeled "T" and ranges from 0 to 90. The graph shows a fluctuating line that starts near 0, sharply rises to a peak around 88 at approximately 20 days, then drops to around 5-10 by 50 days. It then shows several smaller peaks, reaching another peak around 50 at approximately 160 days, before gradually decreasing to near 0 by about 250 days and remaining near 0 until 600 days.::>

**Fig. 8.** Stochastic suppression for *c*=1.1 *c*<sup>\*</sup>. The other parameters are as in Table 1. 

<a id='a0bb9290-7726-4d98-a8cd-26b37997c2c1'></a>

<::A line graph with an inset graph. The main graph shows a value on the y-axis ranging from 0 to 400,000, plotted against "time (days)" on the x-axis, ranging from 0 to 10,000. The line starts around 300,000 at time 0, rapidly decreases with strong oscillations, then the oscillations' amplitude gradually diminishes, and the overall value hovers around 100,000 with smaller oscillations towards the end of the time period. The inset graph, located in the upper central part of the main graph, shows a value on its y-axis ranging from 200 to 400, plotted against an x-axis ranging from 130 to 155. The line in the inset graph starts around 400 at x=130, decreases to a minimum around 220-230 near x=140, and then increases to about 360-370 at x=155. This inset appears to be showing a detailed view of one of the oscillation cycles or a related dynamic.: chart::>

<a id='01543b03-9851-4743-bdeb-11d82a335d9d'></a>

Fig. 7. Stochastic oscillations for c=0.03 (left) and c=0.032 (right). The other parameters are as in Table 1. In both subfigures an insert is plotted zooming in on the minimal values reached at the end of the first spike of the oscillation.

<!-- PAGE BREAK -->

<a id='a85c331c-10f5-4f09-92a6-a684558502c4'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='05647694-3982-4c77-ae75-13a4e38afdd6'></a>

343

<a id='ed6de1cf-4922-4979-ac81-4b400bf352ec'></a>

<::chart: Two plots are presented side-by-side. The left plot is a 2D line graph with 'antigenicity' on the x-axis, ranging from 0 to 70, and 'probability' on the y-axis, ranging from 0 to 1. A curve starts near (0, 0) and increases, reaching approximately 0.9 at x=70. The right plot is also a 2D line graph with 'antigenicity' on the x-axis, ranging from 0 to 70, and 'day with max eradications' on the y-axis, ranging from 0 to 100. A curve starts around (0, 10), increases to a peak of approximately 82 around x=55, then slightly decreases before rising again towards 85 at x=70.::>

**Fig. 9.** In the left panel, the percentage of eradication obtained in function of the parameter c. In the right panel, the modal value of t$_{erad}$ in function of the antigenicity parameter c for c $\in$ (13,71.5). The other parameters are as in Table 1.

<a id='08b0b1b6-2f63-4162-96f5-9d6d15431134'></a>

<::Figure 10: Two plots illustrating deterministic vs. stochastic models of adoptive cellular immunotherapy.
The left plot shows Log10 (T) on the y-axis (ranging from 0 to 9) against time (days) on the x-axis (ranging from 0 to 300). The curve starts near Log10(T)=0, rises slightly, then decreases to a minimum around 80-90 days, and subsequently increases steadily, leveling off near Log10(T)=9 by 250 days.
The right plot shows T on the y-axis (ranging from 0 to 20000) against time (days) on the x-axis (ranging from 0 to 140). The curve starts at T=0, rises sharply from approximately 50 days, peaks at around T=19000 near 75 days, and then sharply declines back to T=0 by 90-100 days.
Fig. 10. Deterministic vs. stochastic models of adoptive cellular immunotherapy with c=10⁻⁴ and s₁ = 5400 delivered for 60 days after day 70. The other parameter are as in Table 1.
: chart::>

<a id='2fabc6c7-45f2-4736-ae21-3d99f96dc6b8'></a>

## 5. Concluding remarks

In order to investigate the phenomenon of spontaneous onco-suppression by the immune system and at the same time to assess whether the Kirschener-Panetta approach may reproduce this important phenomenon, we proposed here a hybrid model that extends the Kirschner-Panetta model. In our extended model the dynamics of tumour cells and immune effectors are described by a suitable stochastic process, whereas the dynamics of the concentration of interleukins are modelled by an ordinary differential equation. Since the stochastic processes are interlinked with the dynamics of the interleukins (and vice versa), the main features of this model are that it contains time-dependent propensity functions and combines both the features of deterministic and stochastic models.

<a id='9af810ed-5f67-41f3-b907-ffcaa4eb10e4'></a>

In order to simulate the model, it was necessary to define a proper stochastic simulation algorithm. Indeed, although in the literature we find algorithms for simulating time-dependent propensity functions (Lecca, 2006; Anderson, 2007) as well as algorithms for simulating hybrid models (Salis and Kaznessis, 2005; Alfonsi et al., 2004), the combination of both is missing. Consequently, for the sake of analysing this model we defined an

<a id='bf4015f8-9fab-4175-a9c3-e8f2780b8cec'></a>

ad-hoc algorithm based on the ideas of Gillespie's stochastic
simulation algorithm (Gillespie, 1976, 1977) which permits an
efficient implementation.

<a id='9e3c8aa2-39e6-4af5-86d1-dd9d253cc4db'></a>

We would point out that the model we present is not a completely new one, but is a stochastic model built on top of a well-known and biologically backgrounded model. The simulations and their biological interpretation, instead, are new.

<a id='3f64f275-1c42-4fc2-8f32-8389a41a7d11'></a>

Our hybrid stochastic version of the Kirschner-Panetta model suggests that, at least in some cases, complete immune surveillance with suppression of the neoplasm might be reached thanks to the conjunction of the intrinsic tendency of the tumour-immune system to oscillate, which is significantly evidenced by the deterministic model, with the stochastic dynamics. We note that this may empirically be inferred by the deterministic Kirschner-Panetta model by considering the tumour eradicated whenever T(t) <1. In fact, from a quantitative analysis of the models, we observe significant differences in the tumour eradication times. Moreover, by following the stochastic approach we have been able to give a probability distribution of the eradication time, and the discussion of Section 4.1 regarding the different behaviours of the system by varying its initial conditions would not have been possible by considering only the

<!-- PAGE BREAK -->

<a id='cc36990a-89be-461f-9eab-1dbb81b31fbc'></a>

344

<a id='abfffba2-cf58-4575-b9af-a08c3daf950f'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='cc636b7b-46b9-4ca1-ad25-d883880fc886'></a>

average eradication time provided by the deterministic model. The relevant role of oscillations showed an intriguing role for the immunogenicity of the disease, which is represented by the parameter c in the model. Indeed, the deterministic immuno- genicity path can be summarised as follows: for low values of c the tumour size is large and the oscillations have very large periods, for intermediate values of c we observe intermediate oscillating tumour size. Finally, for large values of c we observe small tumour size reached after damped oscillations.

<a id='3db60de8-8501-4b59-9b5e-1bfc3e6fecff'></a>

Conversely, the stochastic path forecasts immune suppression for intermediate c, as well as, of course, for quite large c. This is quite a surprising result which deserves further biological investigations and which may have interesting implications for some immunotherapies, since for intermediate c the suppression range is small.

<a id='31c7f309-b63f-4abb-ba2a-df56093a26b9'></a>

Moreover, since for many cases of tumour suppression in the case of low c tumour sizes do reach very large values, we must stress that in these cases the eradication is only theoretical since the host unfortunately dies. However, for larger values of c the tumour size is large but compatible with life, so that the model may contribute to a better understanding some sporadic cases of spontaneous permanent regression of macroscopic tumours (Krikorian, 1980). Of course for large values of c the probability of having a remission is large (e.g. for c=50 we observed that the suppression is reached in 50% of the simulated paths). Finally, we observe that also stochastic sustained oscillations are possible.

<a id='1cfcd557-d5a4-40e9-85b0-3d663116ebee'></a>

When considering adoptive cellular immunotherapies, our simulations suggest that a stochastic model may qualitatively be used in tuning the average length of the therapies, as briefly illustrated in Fig. 10.

<a id='7e6850e3-61ff-46d7-9ee7-fca97184c0ce'></a>

In summary, our work shows that the Kirschner and Panetta
model is even more powerful than it seems, since our stochastic
version of it may also describe the most important phenomenon
of the tumour-immune system interplay, namely the total
suppression of the tumour by the immune system in the absence
of human intervention.

<a id='8ed1c3f8-ccc6-40d9-8460-4c8341bf2b23'></a>

Finally, as far as the phenomena of late recurrence of tumours are concerned, since they did not appear in our stochastic simulations, we think that they may have their main root in the phenomenon of immunoediting (Dunn et al., 2004; d'Onofrio, 2007) and we intend to study them, following the approach used in d'Onofrio (2007), by allowing, in the stochastic model, a slow decrease of some key parameters.

<a id='8e74279f-2ea3-4675-ace6-47052520a80b'></a>

## Acknowledgements
The work of A. d'Onofrio was conducted within the framework of the EU Integrated Project "Advancing Clinico-Genomic Trials on Cancer—ACGT". The ACGT project is partly funded by the EU and the authors are grateful for this support. This work was conducted within the framework of the official agreement on "Computational Medicine" between the European Institute of Oncology and the University of Pisa. We wish to thank the anonymous referees for their suggestions that contributed to significantly improving the paper.

<a id='e14fbeab-f395-4126-aa08-70b7e2b9434c'></a>

# References
Agarwala, S.A., 2003. New applications of cancer immunotherapy, Agarwala, S.A. (Ed.), Seminars in Oncology, Special Issue 29-3 (Suppl. 7).

Alfonsi, A., Cances, E., Turinici, G., Di Ventura, B., Huisiga, W., 2004. Exact simulation of hybrid stochastic and deterministic models for biochemical systems. INRIA Technical Report 5435.

Anderson, D.F., 2007. A modified next reaction method for simulating chemical systems with time dependent propensities and delays. J. Chem. Phys. 127, 214107.

<a id='e7993f16-a3f1-498c-8705-eb24b2581eba'></a>

Bellomo, N., Delitala, M., 2008. From the mathematical kinetic, and stochastic game theory to modelling mutations, onset, progression and immune competition of cancer cells. Phys. Life Rev. 5, 183-206.
Bellomo, N., Li, N.K., Maini, P.K., 2008. On the foundations of cancer modelling: selected topics, speculations, and perspectives. Math. Models Methods Appl. Sci. 18, 593-646.
Bleumer, I., Oosterwijk, E., de Mulder, P., Mulders, P.F., 2003. Immunotherapy for renal cell carcinoma. European Urology 44, 65-75.
Blumberg, N., Chuang-Stein, C., Heal, J.M., 1990. The relationship of blook trans- fusion, tumor staging, and cancer recurrence. Transfusion 30 (4), 291-294.
Burnet, F.M., 1957. Cancer-a biological approach. Br. Med. J. 1, 841-847.
Cappuccio, A., Elishmereni, M., Agur, Z., 2006. Cancer immunotherapy by interleukin-21 treatment strategies evaluated in a mathematical model. Cancer Res. 66, 7293-7300.
Cattani, C., Ciancio, A., d'Onofrio, A. 2010. Metamodeling the learning-hiding competition between tumours and the immune system: a kinematic approach. Math. Comput. Modelling 52, 62-69.
DeBoer, R.J., Hogeweg, P., Hub, F., Dullens, J., DeWeger, R.A., DenOtter, W., 1985. Macrophage T Lymphocyte interactions in the anti-tumor immune response: a mathematical model. J. Immunol. 134, 2748-2758.
De Lisi, C., Rescigno, A., 1977. Immune surveillance and neoplasia: a minimal mathematical model. Bull. Math. Biol. 39 (2), 201-221.
De Pillis, L.G., Radunskaya, A.E., Wiseman, C.L., 2005. A validated mathematical model of cell-mediated immune response to tumour growth. Cancer Res. 65, 7950-7958.
De Vita Jr.V.T., Hellman, S., Rosenberg, S.A., 2008. Cancer: principles and practice of oncology, eight ed. Lippincott Williams & Wilkins.
De Vladar, H.P., Gonzalez, J.A., 2004. Dynamic response of cancer under the influence of immunological activity and therapy. J. Theor. Biol. 227, 335-348.
d'Onofrio, A., Gatti, F., Cerrai, P., 2010. Delay-induced oscillatory dynamics of tumour-immune system interaction. Math. Comput. Modelling 51, 572-591.
d'Onofrio, A., 2007. Tumour evasion from immune system control: strategies of a MISS to become a MASS. Chaos Solitons Fractals 31, 261-268.
d'Onofrio, A., 2005. A general framework for modeling tumour-immune system competition and immunotherapy: mathematical analysis and biomedical inferences. Phys. D 208, 220-235.
d'Onofrio, A., 2006. Tumour-immune system interaction: modeling the tumour- stimulated proliferation of effectors and immunotherapy. Math. Models Methods Appl. Sci. 16, 1375-1401.
Dunn, G.P., Old, L.J., Schreiber, R.D., 2004. The three ES of cancer immunoediting. Ann. Rev. Immunol. 22, 322-360.
Ehrlich, P., 1909. Ueber den jetzigen Stand der Karzinomforschung. Ned. Tijdschr. Geneeskd. 5, 273-290.
Galach, M., 2003. Dynamics of the tumour-immune system competition: the effect of time delay. Int. J. Appl. Math. Comput. Sci. 13, 395-406.
Gatti, R., et al., 1973. Cyclic leukocytosis in chronic myelogenous leukemia: new perspectives on pathogenesis and therapy. Blood 41, 771-783.
Gillespie, D., 1977. Exact stochastic simulation of coupled chemical reactions. J. Phys. Chem. 81, 2340-2361.
Gillespie, D., 1976. A general method for numerically simulating the stochastic time evolution of coupled chemical reactions. J. Comput. Phys. 22 (4), 403-434.
Kaminski, J.M., Summers, J.B., Ward, M.B., Huber, M.R., Minev, B., 2004. Immunotherapy and prostate cancer. Cancer Treat. Rev. 29, 199-209.
Kennedy, B.J., 1970. Cyclic leukocyte oscillations in chronic myelogenous leukemia during hydroxyurea therapy. Blood 35, 751-760.
Kirschner, D., Panetta, J.C., 1998. Modeling immunotherapy of the tumour-immune interaction. J. Math. Biol. 37, 235-252.
Kirschner, D., Arciero, J.C., Jackson, T.L., 2004. A mathematical model of tumor- immune evasion and siRNA treatment. Discr. Cont. Dyn. Syst. 4, 39-58.
Kirschner, D., Tsygvintsev, A., 2009. On the global dynamics of a model for tumor immunotherapy. Math. Biosci. Eng. 6 (3), 573-583.
Krikorian, J.G., 1980. Spontaneous regression of non/hodgkin lymphoma: a report of nine cases. Cancer 46, 2093-2099.
Kronik, N., Kogan, Y., Vainstein, V., Agur, Z., 2008. Improving alloreactive CTL immunotherapy for malignant gliomas using a simulation model of their interactive dynamics. Cancer Immunol. Immunother. 57, 425-439.
Kuznetsov, K.A., Knott, G.D., 2001. Modeling tumour regrowth and immunother- apy. Math. Comput. Modelling 33, 1275-1287.
Kuznetsov, V.A., Makalkin, I.A., Taylor, M.A., Perelson, A.S., 1994. Nonlinear dynamics of immunogenic tumours: parameter estimation and global bifurcation analysis. Bull. Math. Biol. 56, 295-321.
Lecca, P., 2006. A time-dependent extension of Gillespie algorithm for biochemical stochastic π- calculus. In: Proceedings of the 2006 ACM symposium on Applied Computing, pp. 137-144.
Mehta, B.C., Agarwal, M.B., 1980. Cyclic oscillations in leukocyte count in chronic myeloid leukemia. Acta Hematologica 63, 68-70.
Nani, F., Freedman, H.I., 2000. A mathematical model of cancer treatment by immunotherapy. Math. Biosci. 163, 159-199.
Nasell, I., 2002. Measles Outbreaks are not Chaotic. In: Carlos-Castillo, C. (Ed.), Mathematical Approaches for Emerging and Reemerging Infectious Diseases: Models, Methods, and Theory, The IMA Volumes in Mathematics and its Applications, vol. 126. Springer-Verlag, New York, pp. 85-114.
Pardoll, D., 2003. Does the immune system see tumours as foreign or self? Ann. Rev. Immunol. 21, 807-839.

<!-- PAGE BREAK -->

<a id='f685da03-b33e-413d-9b96-493f3efc8224'></a>

G. Caravagna et al. / Journal of Theoretical Biology 265 (2010) 336-345

<a id='b9766a0e-622e-4be1-a3e6-d245c8930575'></a>

345

<a id='62443ec0-8e06-47a1-a2c9-0daf25cdf2ab'></a>

Salis, H., Kaznessis, Y., 2005. Accurate hybrid stochastic simulation of a system of coupled chemical or biochemical reactions. J. Chem. Phys. 122, 054103.
Sohrabi, A., Sandoz, J., Spratt, J.S., Polk, H.C., 1980. Recurrence of breast cancer: obesity, tumor size, and axillary lymph node metastases. J. Am. Med. Assoc. 244 (3), 264-265.
Stepanova, N.V., 1980. Course of the immune reaction during the development of a malignant tumour. Biophysics 24, 917-923.
Szymanska, S., 2003. Analysis of the immunotherapy models in the context of cancer dynamics. Int. J. Appl. Math. Comput. Sci. 13, 407-418.

<a id='6e090d75-9fe8-4fbc-8c23-d93087e9841f'></a>

Tsao, H., Cosimi, A.B., Sober, A.J., 1997. Ultra-late recurrence (15 years or longer) of
cutaneous melanoma. Cancer 79 (12), 2361-2370.
Vicari, A.P., Caux, G., Trinchieri, G., 2002. Tumour escape from immune
surveillance through dendritic cell inactivation. Semin. Cancer Biol. 12, 33-42.
Vodopick, H., Rupp, E.M., Edwards, C.L., Goswitz, F.A., Beauchamp, J.J., 1972.
Spontaneous cyclic leukocytosis and thrombocytosis in chronic granulocytic
leukemia. New Engl. J. Med. 286, 284-290.
Whiteside, T.L., 2002. Tumour-induced death of immune cells: its mechanisms and
consequences. Semin. Cancer Biol. 12, 43-50.
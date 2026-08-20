<a id='be68437c-c0b1-4697-8d76-78d28aa4d1b6'></a>

<::logo: [Viruses]virusesA dark red square with a light pink virus icon on the left, and the word "viruses" in dark red, italicized text to its right::>

<a id='ea098adb-2de1-4e4f-a99d-7832f4225320'></a>

<::logo: MDPI
MDPI
The logo features the text "MDPI" encased within a stylized hexagonal shape, outlined in dark blue.::>

<a id='a8113ae2-1698-47ba-ab39-1085df54480c'></a>

Article

A New Model for the Dynamics of Hepatitis C
Infection: Derivation, Analysis and Implications

<a id='51328232-530f-4082-9146-a052cae2ca6c'></a>

Philip J. Aston

Department of Mathematics, University of Surrey, Guildford, Surrey GU2 7XH, UK; P.Aston@surrey.ac.uk

Received: 25 January 2018; Accepted: 10 April 2018; Published: 13 April 2018
check for
updates

<a id='eb69e879-11c9-4bb9-8c8b-29d34d693e73'></a>

**Abstract:** We review various existing models of hepatitis C virus (HCV) infection and show that there are inconsistencies between the models and known behaviour of the infection. A new model for HCV infection is proposed, based on various dynamical processes that occur during the infection that are described in the literature. This new model is analysed, and three steady state branches of solutions are found when there is no stem cell generation of hepatocytes. Unusually, the branch of infected solutions that connects the uninfected branch and the pure infection branch can be found analytically and always includes a limit point, subject to a few conditions on the parameters. When the action of stem cells is included, the bifurcation between the pure infection and infected branches unfolds, leaving a single branch of infected solutions. It is shown that this model can generate various viral load profiles that have been described in the literature, which is confirmed by fitting the model to four viral load datasets. Suggestions for possible changes in treatment are made based on the model.

<a id='2aae83fb-8166-42bc-aa77-b6976876da34'></a>

Keywords: HCV infection; mathematical model; steady state solutions; bifurcations

<a id='f10c40bd-51aa-4c40-9976-4a3297bc63c5'></a>

## 1. Introduction

Viral diseases are major causes of human morbidity and mortality worldwide. Hepatitis C virus (HCV) infection is one of the major contributors in this regard. The WHO recently published a Global Hepatitis Report [1], which provides global estimates regarding various aspects of HCV infection. They report that in 2015:

* Globally, an estimated 71 million people were living with chronic HCV infection;
* An estimated 1.75 million new HCV infections occurred worldwide, while 399,000 people died from end-stage HCV infection and 843,000 were cured;
* 20% of HCV-infected persons (14 million) have been diagnosed, and of these, 7.4% (1.1 million) had started treatment;
* HCV infection affects all regions with the highest reported prevalence in the Eastern Mediterranean and European Regions.

<a id='38bea1b5-332b-4eb8-b7bc-09af7f4c3090'></a>

The report also noted that incidence of HCV infection in the USA doubled between 2010 and 2014.
Thus, HCV infection is still an issue of major importance for global public health.

<a id='53cb022b-aea5-49cf-908b-79b2108ff988'></a>

In May 2016, the World Health Assembly adopted the Global Health Sector Strategy, which committed to a 65% reduction in mortality and a 90% reduction in incidence by 2030 [1]. Clearly, given the above statistics, there is much work to do in order to achieve these targets. A good understanding of the disease mechanism is vital in designing new drugs for treatment of the infection. This understanding is somewhat hampered by the fact that data can only be easily collected for the viral load, and so, other quantities, such as the concentration of healthy and infected hepatocytes, cannot be determined from patient data.

<a id='de9ab25b-058a-4eb1-b0e5-70820baf1d11'></a>

Viruses 2018, 10, 195; doi:10.3390/v10040195

<a id='4fb73514-b7c3-4fb9-b5fc-1c46e5b72df5'></a>

www.mdpi.com/journal/viruses

<!-- PAGE BREAK -->

<a id='5f8b592a-d372-48e8-93db-cf89d9c62cb5'></a>

Viruses 2018, 10, 195

<a id='2cd56bfa-eec2-4f7e-8cae-95595e0370bb'></a>

2 of 41

<a id='e6f379b9-8d60-483d-b509-f8696bf1afa5'></a>

Mathematical modelling allows the inclusion of all the relevant variables and can help to give insight into disease progression and the effect of treatment. Many different mathematical models have been proposed for HCV infection (as well as for many other viral infections), and we add our own new model to this collection. One of the early HCV models by Neumann et al. [2] was adapted from similar models of HBV and HIV infections. Other models have since been proposed, many of which are variations on this original model. However, these models are not consistent with some of the known facts about HCV infection. Thus, we review some of the information about HCV infection that is available in the biological literature and propose a new model that is consistent with this information.

<a id='18543f34-d204-44f9-977a-3f271d4ae892'></a>

Having derived a new model, we then analyse the steady state solutions and, unusually for a nonlinear model, we are able to give an analytic solution for the infected steady state solutions in a special case. There are many different viral load profiles described in the literature, and we describe how each of these can be achieved with our model as well as fitting the model to four different viral load profiles. We also make some suggestions for changes in treatment of HCV infection, based on our model predictions.

<a id='15720e01-14a2-4693-aba2-472bc068f510'></a>

## 2. A Review of Existing Models of HCV Infection
A number of different mathematical models has been proposed for modelling the dynamics of HCV infection. We first review some of the existing models, before proposing one of our own.

<a id='26064882-66b5-4982-99f7-86c82c25e3b6'></a>

2.1. The Neumann Model Neumann et al. [2] adapted models of HIV and HBV infections to HCV and derived the equations: $$ \dot{T} = s - dT - (1 - \eta)\beta VT \quad (1) $$ $$ \dot{I} = (1 - \eta)\beta VT - \delta I \quad (2) $$ $$ \dot{V} = (1 - \epsilon)pI - cV \quad (3) $$

<a id='c5d86dae-1b9e-40b6-a597-5f2342d8d302'></a>

where _T_ is the concentration of healthy hepatocytes, _I_ is the concentration of infected hepatocytes, _V_ is the concentration of virions and the dot represents the derivative with respect to time. The treatment parameters _η_ and _ε_ correspond to a reduction in the rate of production of infected cells and virions, respectively.

<a id='daa32033-30ca-45df-ba24-21f624140a70'></a>

These equations have an uninfected steady state:

<a id='8d7a408a-008e-46e2-98da-fab3a6e5b025'></a>

Tu = s/d', Iu = Vu = 0 (4)

<a id='ca728bf7-5705-4c29-be49-b34bf65a5cd6'></a>

which exists for all \(\eta\) and \(\epsilon\), together with an infected steady state:

<::
$$T_i = \frac{\delta c}{\beta p(1 - \eta)(1 - \epsilon)}$$
$$I_i = \frac{s}{\delta} - \frac{cd}{\beta p(1 - \eta)(1 - \epsilon)}$$
$$V_i = \frac{sp(1 - \epsilon)}{\delta c} - \frac{d}{\beta(1 - \eta)}$$
: figure::>

<a id='844f7ca7-0d60-44b9-a58a-7bb15ba00d78'></a>

The two branches intersect at a bifurcation point at:

(1 - η)(1 - ε) = δcd / βsp (5)

<a id='26d927e4-271a-4745-8fe1-dbc9db296eb2'></a>

## 2.2. The First Dahari Model

Dahari et al. [3] analysed the Neumann model and showed that the solutions could exhibit biphasic decline of the viral load under treatment, with an initial rapid decline followed by a slower

<!-- PAGE BREAK -->

<a id='cdb7cdd1-f8ef-41b0-9833-9fd7679a0e3d'></a>

Viruses 2018, 10, 195

<a id='bcade2e9-3e97-4d38-bc24-74a39bfff93b'></a>

3 of 41

<a id='ab44d7d3-f099-47ce-aa7c-768bc64bff91'></a>

decline, but that it could not show triphasic behaviour of the viral load, where a plateau exists between the rapid and slow declines. They therefore developed an extended model by adapting the Neumann model, including extra terms for the replication of the healthy and infected hepatocytes. Their model equations are given by:

<a id='23f36335-2655-46d5-bca9-8804e0183b39'></a>

$\dot{T} = s - dT + rT \left(1 - \frac{T + I}{T_{max}}\right) - (1 - \eta)\beta VT$ (6)

$\dot{I} = (1 - \eta)\beta VT + rI \left(1 - \frac{T + I}{T_{max}}\right) - \delta I$ (7)

$\dot{V} = (1 - \epsilon)pI - cV$ (8)

<a id='51c2e5dc-d3c7-4742-86c6-8dd0d0900ad8'></a>

These equations also have an uninfected steady state with $I_u = V_u = 0$ and $T_u$ found as the positive solution of the quadratic equation:

$rT^2 - T_{\text{max}}(r - d)T - sT_{\text{max}} = 0$ (9)

<a id='348b9259-daee-498f-9ad9-5e804936d7f5'></a>

We note that this quadratic equation has one positive and one negative solution, and clearly, the positive solution is the one of interest. Substituting T = T_max + δT into (9) gives the quadratic equation:
rδT^2 + T_max(r + d)δT + T_max(T_max d - s) = 0 (10)

<a id='ee91477e-1091-4e52-82fb-cf046a091583'></a>

The number of positive or negative solutions of this equation depends on the sign of Tmaxd – s.
If this term is positive, then both the solutions are negative, and so, the two solutions of (9) will
both lie below Tmax. However, if this term is negative, then (10) will have one positive and one
negative solution. Clearly, the negative solution will correspond to the negative solution of (9), and so,
the positive solution must correspond to T > Tmax. Now, Tmax is supposed to be the maximum value
for the healthy hepatocytes, and so, we maintain this upper bound provided that the condition:

<a id='6b8d7f06-65d7-4a4f-9d0d-12d3575de8b2'></a>

Tmax > s/d

<a id='aa4ea64e-fe73-4f20-aab4-7ba066ad18b7'></a>

is satisfied.

<a id='af5ac286-621a-4586-b83d-560059025c55'></a>

Equations (6)–(8) also have an infected steady state given by:

$I_i = \frac{c(T_{\text{max}}(s + (r-d)T_i) - rT_i)}{T_{\text{max}}(s + (r-d)T_i) + rT_i}$

<a id='c64b8e3e-c554-4e11-9a4e-188a1b950ed1'></a>

V_i = \frac{\varepsilon p(T_{max}(s + (r - d)T_i) - rT_i^2)}{T_i(rc + (1 - \eta)(1 - \varepsilon)p\beta T_{max})}

<a id='cf1dc80d-8f81-48b8-8d91-a199d345a6a6'></a>

where T_i is the positive solution of the quadratic equation:

(1 – η)²(1 – ε)²β²p²TmaxT² + c((1 – η)(1 – ε)βpTmax(r – δ) – cr(δ – d))T – rsc² = 0 (11)

<a id='f0f89768-a5fb-420e-9044-87be0cc5fe14'></a>

which also has one positive and one negative solution. Clearly, the positive solution is the only solution of interest. The two branches again intersect at a bifurcation point, which occurs at:

<a id='9d08007e-9b64-4cfa-a37e-bb802a8f2d00'></a>

(1 - η)(1 - ε) = \frac{c(rT_i - T_{\text{max}}(r - δ))}{pβT_{\text{max}}T_i}

<a id='5375eda6-61c0-4dbe-bde6-8abe755e8c04'></a>

Note, however, that $T_i$ also depends on $\eta$ and $\epsilon$.

<!-- PAGE BREAK -->

<a id='089824d9-eae4-4cfe-a988-fe9211705daf'></a>

Viruses 2018, 10, 195

<a id='6e5216cb-6c50-46c8-8f8a-9a3f20e37a68'></a>

4 of 41

<a id='37fed777-6730-4026-b99b-57efd0dbeb82'></a>

_2.3. The Second Dahari Model_

If ribavirin is included as part of the treatment, then it causes some of the virions to be non-infectious. Dahari et al. [4] modelled this by separating the virions into two groups, namely infectious (V_I) and non-infectious (V_NI). The equations that they derived are given by:

<a id='b7ca82eb-7d09-4fe4-92ef-5660435862a7'></a>

$$\dot{T} = s - dT + r_T T \left(1 - \frac{T + I}{T_{max}}\right) - (1 - \eta)\beta V_I T \quad (12)$$

$$\dot{I} = (1 - \eta)\beta V_I T + r_I I \left(1 - \frac{T + I}{T_{max}}\right) - \delta I \quad (13)$$

$$\dot{V_I} = (1 - \rho(t))(1 - \epsilon)pI - cV_I \quad (14)$$

$$\dot{V_{NI}} = \rho(t)(1 - \epsilon)pI - cV_{NI} \quad (15)$$

<a id='061f0b38-fa63-450a-8c24-5433b1ca1e86'></a>

where \rho(t) is the fraction of virions that are rendered non-infectious due to the effect of ribavirin. Snoeck et al. [5] simplified these equations by taking r_T = r_I and by making \rho a constant rather than a time-dependent function. We now review the solutions of these simplified equations.

<a id='feb72643-70fb-4b0e-98ca-e1dd0f9cc3f8'></a>

The first three Equations (12)-(14) involve only the three variables T, I and V_I, and so, these equations decouple from the fourth. These equations are essentially the same as Equations (6)-(8), except that V is replaced by V_I and p is replaced by (1 - \rho)p. Thus, the uninfected steady state is the same as for the first Dahari equations, together with V_NI = 0. The infected steady state is readily obtained from the first Dahari steady state by replacing p with (1 - \rho)p in the above equations together with:

<a id='6adab233-1ab6-435a-b712-54ec23a37f00'></a>

<::transcription of the content
: equation
V_NI,i = (ρ(1 - ε)p_i) / c * I_i
::>

<a id='0e67a29a-8b13-405e-b860-e730726e96cb'></a>

Similarly, the bifurcation point at which the two branches intersect occurs at:

<a id='fadebc78-0a37-46fa-a01a-f6383b6ec386'></a>

(1 - η)(1 - ε)(1 - ρ) = {}c(rT₋ - Tₘₐₓ(r - δ))}{}pβTₘₐₓT₋}}

<a id='ad713a21-9df0-4510-a89a-80c73a2df0c3'></a>

where T_i is the positive solution of (11).

<a id='17d3b7ca-adbe-4dc2-b2ae-f7a4e73d9a55'></a>

2.4. *Other Models*

There are also a number of variants of the above models in the literature. Herrman et al. [6] used Equations (2) and (3) from the Neumann model, but used a different equation for the healthy hepatocytes, given by:

$\dot{T} = \gamma(T(0) + I(0) - T - I)$

<a id='b1f12031-f497-4098-80ab-f87205333bd5'></a>

We note that this equation does not include the term -BVT associated with the virus infecting the healthy cells. Furthermore, the rate of production of the healthy cells depends on the difference between the maximum value T(0) + I(0) and the total hepatocyte population T + I. After an initial time period, they change δ in (2) to Mδ for some M > 1 to represent an inflated loss of infected cells after an initial delay.

<a id='af79e83a-83a1-426d-ac9b-54f44e8b6e20'></a>

Song and Neumann [7] also use Equations (2) and (3) from the Neumann model and supplement this with the equation for _T_ given by:

<a id='a28246c1-3a4e-4df4-82c7-b450955af6f6'></a>

$\dot{T} = s - dT + aT(1 - T/T_{\text{max}}) - \beta VT$

<a id='8ac87b69-b6fd-4ed9-b2b0-68881fb983a7'></a>

In this case, the proliferation is modelled by a logistic function, but the reason for this choice is not given. They also adapt this model by including a saturation term for the generation of infected cells where they replace the $\beta VT$ term by $\beta VT/(1+aV)$.

<a id='50b6ee1d-ae02-4c75-926e-45e5f8bce103'></a>

An earlier model by Dahari et al. [8] is very similar to the first Dahari model described above,
but with a time-dependent component for the death rate of infected cells and a time-dependent

<!-- PAGE BREAK -->

<a id='ad6eb8cf-d902-4435-ae87-f2c7238cb317'></a>

Viruses 2018, 10, 195

<a id='164f2d4a-69a2-477c-98d8-bb4c9833b36e'></a>

5 of 41

<a id='3a2d4d62-f7a0-4584-aa75-d01b806f131e'></a>

treatment parameter e(t), as well as an extra equation for the dynamics of ALT (alanine aminotransferase). There is also a term q(t)I, which is added to the T equation and subtracted from the I equation, which represents non-cytolytic clearance of the virus from infected cells. These extra terms were dropped in the later models by Dahari et al. This early model was analysed in more detail by Reluga et al. [9], but with q constant, which is then described as a spontaneous cure term.

<a id='daac4eb0-9c84-4c83-980a-5f5050aa77e0'></a>

### 3. A New Model of HCV Infection

Clearly, there are many mathematical models of HCV infection, which are generally similar in nature, but with a variety of different terms occurring in the equations, which represent different biological processes. We now add to this collection of models by developing our own model. We consider the available literature concerning the various dynamical processes that occur during HCV infection and treatment and include those that we consider to be the most important in the model.

<a id='f7276da3-40bb-4ec8-b9af-2e8c05437f54'></a>

### 3.1. Cell Regeneration
The liver is unique among the organs of the body in that it can regenerate itself if part of the liver mass is removed [10]. We therefore begin by considering the dynamics of healthy hepatocytes in an uninfected liver. All of the models described in Section 2 include the terms:

<a id='bef0ab16-1a4c-4f8c-8b51-9c21962b8fbe'></a>

$\dot{T} = s - dT$ (16)

<a id='1275fcd7-2eef-498f-8a93-fcbded730d9c'></a>

The standard interpretation of this equation is that new hepatocytes are formed at a constant rate s and that a certain fraction d of them die. However, hepatocyte turnover is low in a normal liver with more than 99% in the quiescent phase of the cell cycle. But if part of the liver is removed in a partial hepatectomy, then the liver mass is replaced within seven days by replication of the mature hepatocytes [11]. Thus, if the concentration T is measured relative to the original volume of the liver, then we model this cell division process by:

<a id='06f4ba37-a5e9-4633-8c8b-41b6b6749339'></a>

Ṫ = r(Tmax - T)

<a id='fe9a1656-0bc1-4318-8022-cdaa661a7f37'></a>

so that the concentration is reduced when part of the liver is removed and the division process stops
completely when _T_ reaches _T_max. Including the term for cell death gives the equation:

<a id='41993c7c-dc78-4668-be7c-9db854226b57'></a>

$\dot{T} = r(T_{\text{max}} - T) - dT = rT_{\text{max}} - (r + d)T$ (17)

<a id='a4da9160-e5f7-49b5-ad3d-41c48e50466c'></a>

where $d$ must be small to ensure slow turnover in a healthy liver. This equation has steady state $T_s = rT_{max}/(r + d)$. We note that this equation is essentially the same as (16) with $s = rT_{max}$ and $d$ replaced by $r + d$. Thus, this equation seems reasonable, but the interpretation of the parameters requires care.

<a id='79264194-7940-41be-8959-3a8526ae1016'></a>

It has been found that the liver regenerates itself after surgery with approximately exponential convergence to a steady state [12], as can be seen in Figure 1 (although the regeneration in the first seven days seems to occur more rapidly than predicted by the fitted curve). The solution of Equation (17) also consists of exponential convergence to the steady state. However, care must be exercised in linking these as the plots in Figure 1 are for liver volume, whereas T is a concentration of hepatocytes. However, T/Ts is the ratio of the reduced number of hepatocytes to the number of hepatocytes in the liver before surgery, which is the same as the ratio of liver volume after surgery to volume before surgery. Dividing (17) by Ts gives:

<a id='21360f0a-f5a6-4309-839a-ca27d124928e'></a>

$$\frac{\dot{T}}{T_s} = \frac{rT_{\text{max}}}{T_s} - (r+d)\frac{T}{T_s} = (r+d)\left(1-\frac{T}{T_s}\right)$$

<!-- PAGE BREAK -->

<a id='7a1e7043-e0a5-40cf-a157-65410e633530'></a>

Viruses 2018, 10, 195

<a id='a06ce1da-2917-46d5-b3dd-92ecaa31cc61'></a>

6 of 41

<a id='09732806-39ec-4710-9344-37d6fda5942f'></a>

The solution of this equation is:

<a id='681ce51e-1d79-420b-9225-88661da181fd'></a>

T/Ts = 1 - Ae^-(r+d)t

<a id='53ff41f3-703a-43e6-a979-08d5bd784552'></a>

where the constant A is determined from the initial condition. This solution can be multiplied by 100 to give a percentage figure, which does not affect the exponential term. Of course, the data shown in Figure 1 indicate that the liver does not completely regain its previous volume, and so, we cannot match this solution precisely to the data. However, we assume that the exponential rate of convergence is the same, which implies that the coefficient of the exponential of the percentage of original liver volume is r + d.

<a id='a4cfec10-e2aa-421d-9739-cac2d4ffed45'></a>

Fitting a function of the form $y = a - be^{ct}$ to the data shown in Figure 1 gives the curves shown. The corresponding parameter values are $a = 79.8889$, $b = 23.8424$, $c = 0.0153121$ for the female data and $a = 86.0996$, $b = 29.1096$, $c = 0.0111078$ for the male data. Thus, we have $r + d = 1.53 \times 10^{-2}$ day$^{-1}$ for the female data and the slightly lower value of $r + d = 1.11 \times 10^{-2}$ day$^{-1}$ for the male data.

<a id='758bb270-c166-4261-bd77-a93ac35c19a6'></a>

<::chart: Two line charts, side-by-side, depicting liver regeneration over time. (a) Female liver regeneration: The x-axis is labeled 'time (days)' from 0 to 400. The y-axis is labeled '% of original liver volume' from 45 to 90. Data points, marked with 'x', show an increasing trend in liver volume percentage over time, fitted with a smooth curve. Approximate data points are (0, 50), (25, 60), (75, 69), (125, 73), (180, 78), and (350, 79.5). (b) Male liver regeneration: The x-axis is labeled 'time (days)' from 0 to 400. The y-axis is labeled '% of original liver volume' from 40 to 90. Data points, marked with 'x', also show an increasing trend in liver volume percentage over time, fitted with a smooth curve. Approximate data points are (0, 49), (25, 56), (75, 71), (125, 76), (180, 82), and (350, 85).::>Figure 1. Data for female and male liver regeneration from [12] fitted with a curve of the form $y = a - be^{-ct}$, which is the form of the solution of (17).

<a id='7844d0dd-667d-43f1-b2e1-ea6544317e8b'></a>

For an HCV-infected liver, it is assumed in Dahari et al. [8] that the regeneration of the liver occurs through "blind homeostasis" in, which the infected cells regenerate in the same way as the healthy cells. We make this assumption here, but will revisit this issue later. Thus, if we define H = T + I, to be the total concentration of hepatocytes, then the equation for H should be the same as our previous Equation (17), but with T replaced by H, which is therefore given by:

<a id='2a191205-1ffc-4f37-a989-a2684a31259c'></a>

$\dot{H} = rT_{\text{max}} - (r+d)H \quad (18)$

<a id='ed2d4ebe-2487-4702-ac4c-cb062c4cb8b3'></a>

We note that considering only the regeneration terms in the first Dahari model [8] and the variant of the second Dahari model by Snoeck et al. [5], the regeneration terms in the equations for _T_ and _I_ are:

<a id='c9bfb07c-4aec-4ec2-9ddf-43870427321d'></a>

<::
$\\dot{T} = rT \left(1 - \frac{T+I}{T_{\text{max}}}\right)$

$\\dot{I} = rI \left(1 - \frac{T+I}{T_{\text{max}}}\right)$
: figure::>

<a id='e4769126-7cf1-4cdc-a934-2bc8a18b83be'></a>

Adding these equations gives:

Ḣ = rH (1 - H / Tmax)

<!-- PAGE BREAK -->

<a id='ebd0675c-7850-4fcb-8fc7-fc96ab3b00e2'></a>

Viruses 2018, 10, 195

<a id='23610f92-b01e-452a-a34f-2229804a7095'></a>

7 of 41

<a id='42810221-3787-4de9-88aa-6952ed4450ea'></a>

which is a logistic equation for the growth of hepatocytes. The dynamics of the logistic equation ends with exponential convergence to a steady state, but has slower growth at an earlier stage, particularly for initial conditions that are not close to the stable steady state. This does not agree with the above results that show exponential convergence to the steady state, but with more rapid initial growth.

<a id='afb12611-9bdf-4c25-b4b2-46b1fb122c75'></a>

Thus, we allocate the growth of H, given by r(Tmax − H), to the two pools T and I in relative proportion to the size of the pools, noting that the size of the pools is not constant over time. We therefore have the equations:

<a id='2434dcdc-92ff-4a4e-993e-38f21c70d165'></a>

<::Ṫ = r (T / (T + I)) (Tmax - (T + I))
İ = r (I / (T + I)) (Tmax - (T + I))
: equation::>

<a id='5627bacf-58dc-498f-bb6f-f32131b25d16'></a>

Adding these equations gives the regeneration term in (18) as we required.
It is generally assumed that the death rates of the healthy and infected cells are different, as the immune system tries to get rid of the infected hepatocytes, resulting in a higher death rate. Thus, adding in the death terms gives the equations:

<a id='dafb399f-b609-4811-964a-508a0719ca85'></a>

Ṫ = r (T / (T + I)) (Tmax - (T + I)) - dT
  = rTmax T / (T + I) - (r + d)T

İ = r (I / (T + I)) (Tmax - (T + I)) - δI
  = rTmax I / (T + I) - (r + δ)I

<a id='cbc3fbf9-0363-4934-9b63-97b5130d7ade'></a>

Setting δ = d and adding these equations then gives (18). However, since the death rate for infected cells is higher than for healthy cells, we assume that δ > d.

<a id='8d60e5a4-b35a-40b6-ac8c-30a9b0e39763'></a>

We made the assumption above that the healthy and infected cells regenerate in the same way, which implies that the total number of hepatocytes H is not changed by progression of the infection (except for the increased death rate of the infected cells). However, it is known that "the vast majority of liver diseases are characterized by various levels of damage, loss, and impaired regeneration of mature hepatocytes" [13]. Hepatocyte loss due to disease has been classed as mild (<30%), moderate (30–50%) or severe (>50%) [14], and so, it is clear that infection does result in quite significant loss of hepatocytes. As noted above, the infection also impairs the regeneration of mature hepatocytes, and so, this should be included in the model. We do this by assuming that the regeneration rates of healthy and infected hepatocytes are different (as is done in DebRoy et al. [15]), and so, our equations now become:

<a id='40f86d14-02aa-469e-99f4-412b2d336655'></a>

$$\dot{T} = r_T \frac{T}{T+I}(T_{\text{max}} - (T+I)) - dT$$ $$\quad = \frac{r_T T_{\text{max}} T}{T+I} - (r_T + d)T$$ $$\dot{I} = r_I \frac{I}{T+I}(T_{\text{max}} - (T+I)) - \delta I$$ $$\quad = \frac{r_I T_{\text{max}} I}{T+I} - (r_I + \delta)I$$

<a id='4f503416-1046-47cc-afe6-496eea34376b'></a>

where the two constants $r_T$ and $r_I$ determine the rate of proliferation of the healthy and infected hepatocytes respectively. DebRoy et al. [15] assume that $r_I > r_T$ so that the proliferation of infected cells is greater than that for uninfected cells. It has been noted that chronic HCV infection results in increased expression of proliferation markers [11], which suggests an increase in the proliferation rate due to infection. However, it has also been found that progression to the S phase of the cell

<!-- PAGE BREAK -->

<a id='a20b40cd-7705-4f82-8599-bd6aff55e5be'></a>

Viruses 2018, 10, 195

<a id='13dcadf1-149b-47b6-8ff7-17a2598b8575'></a>

8 of 41

<a id='cb28fe92-8098-4a4d-9bc6-34e3bb7751f3'></a>

cycle is blocked, so that there is overall a reduction in the number of cells that complete the cell cycle. This is related to the virus in the cells since "cell cycle progression (is) blocked by individual viral proteins" [11]. We therefore assume that r₁ < rT so that proliferation of infected cells is reduced. This is also the assumption made by Dahari et al. [4]. A combination of healthy cells becoming infected, a lower rate of regeneration for infected cells and a higher rate of cell death for infected cells is likely to result in a large decrease in the total number of hepatocytes as the infection progresses, as has been observed.

<a id='1c5927e6-9c1e-4f29-84d7-55944a88d38d'></a>

## 3.2. Stem Cells

Thus far, we have considered hepatocyte production only as a result of cell division. However, liver stem cells can also generate hepatocytes, and so, there are two mechanisms for hepatocyte production [10,13,16]. In a healthy liver, which has undergone a partial hepatectomy (where part of the liver has been removed), the healthy hepatocytes self-replicate to restore liver mass, and the contribution of liver stem cells to regeneration "seems to be minimal if any" [10]. However, if there is liver injury, which affects this mechanism of regeneration, such as due to chronic viral hepatitis, then the stem cells become more active as an alternative mechanism of hepatocyte production [10,13,16]. Moreover, "a 50% loss of hepatocytes, together with a significant decrease in proliferation of the remaining mature hepatocytes, is required for an extensive activation of hepatic progenitors" [13]. Thus, it seems that the activation of stem cells is proportional to the degree of infection, with no effect in a healthy liver and an extensive effect in a severely-infected liver. We model this by adding a term *sI* to the equation for *T*, giving the model equations, which include these two mechanisms of hepatocyte production together with cell death as:

<a id='1dffffae-bd99-465a-8766-144f37c47849'></a>

T = sI + (r_T T_max T) / (T + I) - (r_T + d)T

i = (r_I T_max I) / (T + I) - (r_I + \delta)I

<a id='53d1be67-7333-4f44-a200-32c1bed6ca9e'></a>

3.3. Infection

Infected hepatocytes are formed when virions enter healthy hepatocytes. The principle of mass action implies that the infection rate is proportional to the product of the concentrations of virions and healthy cells. Adding the infection terms into our earlier equations now gives:

<a id='8454542c-ea7a-47d2-9a95-e04cc04dc7e0'></a>

$$\dot{T} = sI + \frac{r_T T_{\max} T}{T+I} - (r_T + d)T - \beta VT$$
$$\dot{I} = \frac{r_I T_{\max} I}{T+I} - (r_I + \delta)I + \beta VT$$
$$\dot{V} = -cV - \beta VT$$

<a id='7ebc217e-7982-4268-8bde-d45b212fe866'></a>

where we have also included an elimination term in the V equation. We note that all of the models discussed above omit the infection term in the V equation. In Dahari et al. [4], they point out that if T is assumed to be constant, then -cV - βVT = -(c + βT)V = -cV, and so, the infection term can be considered to be included in the elimination term -cV. However, as the models all include a differential equation for T, it is clearly not constant. Moreover, in the case of severe infection, the concentration of healthy hepatocytes may be very low, and so, the assumption that T is approximately constant is not valid. Thus, the infection term should also be included in the V equation. We note that models for HIV infection are very similar to these models, and in this case, the infection term is also included in all three Equations [17].

<!-- PAGE BREAK -->

<a id='8c3c80a3-d863-4fc7-bde1-76e7e7af235c'></a>

Viruses 2018, 10, 195

<a id='623e3b42-c26b-4e1f-a9d2-a8f7d5e2b1e0'></a>

9 of 41

<a id='f3273659-2c83-4644-9272-1f2d47644326'></a>

3.4. The Revised Model

Finally, assuming that infected cells produce virions at a constant rate p, we add an extra term into the V equation. Treatment with interferon alpha is assumed to both reduce the rate of new infection (η) and to reduce the rate of production of virions (ϵ). Adding in these treatment parameters, we obtain our revised model equations:

$\dot{T} = sI + \frac{r_T T_{max} T}{T+I} - (r_T + d)T - (1 - \eta)\beta VT$ (19)

$\dot{I} = \frac{r_I T_{max} I}{T+I} - (r_I + \delta)I + (1 - \eta)\beta VT$ (20)

$\dot{V} = (1 - \epsilon)pI - cV - (1 - \eta)\beta VT$ (21)

<a id='8c7250ba-0936-48f7-96b4-654360019d41'></a>

If the effect of ribavirin is included, which causes some of the virions to be non-infectious, then the model becomes:

Ṫ = sI + (r_T T_max T) / (T+I) - (r_T + d)T - (1 - η)βV_I T (22)

İ = (r_I T_max I) / (T+I) - (r_I + δ)I + (1 - η)βV_I T (23)

V̇_I = (1 - ρ)(1 - ε)pI - cV_I - (1 - η)βV_I T (24)

V̇_NI = ρ(1 - ε)pI - cV_NI (25)

<a id='d3a558ab-5bd0-4467-b34c-d08d0096b7d3'></a>

Again, the last equation decouples from the other three, and so, the dynamics of the system is determined by Equations (22)-(24), which are essentially the same as Equations (19)-(21) with V₁ replaced by V. Thus, we only consider Equations (19)-(21) in detail.

<a id='756d8d63-21bc-4c5d-a05b-5b47e9358aab'></a>

3.5. Spontaneous Clearance

It has been reported that "about 15-30% of asymptomatic patients and more than 50% of symptomatic patients with acute hepatitis C spontaneously clear the virus during the early phase of infection" [8]. A more recent estimate is that "15-45% of [HCV] infected persons spontaneously clear the virus within 6 months of infection without any treatment" [18]. For infected patients who are cured by treatment, it is also likely that the treatment does not completely eliminate all infected hepatocytes and virions, but that the body is able to clear a small remnant once treatment has stopped. Both of these situations can occur in the equations by ensuring that the uninfected steady state is stable when there is no treatment (ε = η = 0) for initial conditions sufficiently close to the steady state. However, the Neumann model and the two Dahari models described above do not allow for this possibility as the model equations with the treatment parameters ε and η set to zero all have the uninfected steady state as unstable.

<a id='63cc67f5-1316-4855-aa72-2a80f11eeed9'></a>

The model described in Dahari et al. [8] includes terms (qI) for non-cytolytic clearance of the virus from infected cells. These terms are described in Reluga et al. [9] as being associated with spontaneous cure. In [9], a quasi-steady state approximation is used to reduce the three equations to two. The eigenvalues of the Jacobian evaluated at the uninfected steady state are λ1 < 0 and λ2(q) = λ2(0) – q, where λ2(0) is the difference of positive terms and so could be positive or negative. Therefore, clearly, the addition of the parameter q ensures that a larger region of the parameter space corresponds to spontaneous cure since it moves the eigenvalue λ2 to the left on the real line. However, this term was dropped in later models used by this group [3,4].

<a id='92d747c2-6c19-41f9-80c9-f7c7f8442f0e'></a>

Spontaneous clearance and clearance of infection after cessation of treatment can both be realised in a model by ensuring that the uninfected steady state is stable with no treatment, but with another nearby steady state also existing, which has one unstable and two stable eigenvalues. The two-dimensional stable manifold would then act as a surface that separates out trajectories that converge to the uninfected steady state or move away from this region to a stable infected steady

<!-- PAGE BREAK -->

<a id='7e9cfd42-dcaf-4b95-afe4-948b337aa6cb'></a>

Viruses 2018, 10, 195

<a id='77a1b492-4e22-41ac-8944-ce72b240e946'></a>

10 of 41

<a id='101b1bf4-9bfa-495d-b06f-cb3d59561e60'></a>

state. Chronic infection would then occur if either the initial conditions at the start of infection lie above this two-dimensional stable manifold, or if, for particular parameter values, the uninfected steady state had become unstable, in which case a complete cure with treatment would also be impossible.

<a id='0f58c75c-5b8f-4c58-8639-b92466902737'></a>

All the models have an uninfected steady state with I = V = 0 and T > 0. One way in which the scenario just described could occur is if the bifurcation from the uninfected steady state to an infected steady state occurs close to € = 0. If the bifurcation point occurs for € < 0, at an unphysical parameter value, with the bifurcating branch occurring to the right of the bifurcation point, then there would be two steady state solutions at € = 0 with the uninfected steady state being stable and the infected steady state being unstable (see Figure 2a). This situation allows for spontaneous cure or chronic infection, depending on the initial conditions, and for complete cure for a patient once the treatment has reduced the infected hepatocytes and virus levels to a sufficiently low level. However, only a small change in parameter values could move this bifurcation point so that it occurs for a positive value of € (see Figure 2c), which makes the uninfected steady state without treatment unstable. In this case, spontaneous clearance of the infection is not possible, and there will always be relapse of the infection on cessation of treatment, as is observed in some cases [5]. Clearly, only a small change in parameters is required to switch between these cases, which could be due to the variability between patients and would also explain the variability in outcomes for different patients. Various different scenarios will be considered in more detail in Section 8.

<a id='c0b53753-c586-4c7a-8e7e-e91bf6fab838'></a>

<::Bifurcation diagrams showing the bifurcation from the uninfected steady state. Each plot has an x-axis labeled 'ε' and a y-axis labeled 'V'. All lines shown are dashed, indicating unstable steady states. (a) For ε < 0, there is a dashed horizontal line along V=0 for ε < 0, and a dashed line originating from the origin (0,0) with a positive slope. (b) For ε = 0, there is a dashed horizontal line along V=0 for ε < 0, and a dashed line originating from the origin (0,0) with a positive slope. (c) For ε > 0, there is a dashed horizontal line along V=0 for ε < 0, and a dashed line originating from a positive ε value on the x-axis with a positive slope. Figure 2. The bifurcation from the uninfected steady state. The bifurcation point occurs for (a) ε < 0, (b) ε = 0, (c) ε > 0. Stable steady states are indicated by solid lines and unstable steady states by dashed lines.::>

<a id='96e5d16a-8fe7-4da5-b691-584521149efc'></a>

3.6. *Non-Dimensionalisation*

Before considering the properties of our new model in detail, we non-dimensionalize it in order to reduce the number of parameters. We non-dimensionalize Equations (19)-(21) by rescaling the variables by the uninfected steady state value of T, which is $T_u = r_T T_{max}/(r_T + d)$ (note that $T_u < T_{max}$). We therefore define the new non-dimensional variables:

<a id='b0461732-77ae-41fb-b664-26a5aa4e49b2'></a>

$$x = \frac{(r_T + d)T}{r_T T_{\text{max}}}, \quad y = \frac{(r_T + d)I}{r_T T_{\text{max}}}, \quad z = \frac{(r_T + d)V}{r_T T_{\text{max}}} \quad (26)$$

<a id='b8725284-5154-4816-92c2-33ef93001f1a'></a>

together with a new non-dimensional time variable:

                                                  τ = (r_T + d)t

<a id='eee4cd50-9a22-4fbb-b416-21b1e48c32d9'></a>

Equations (19)-(21) involve two treatment parameters \( \epsilon \) and \( \eta \). Interferon therapy is assumed to partially block viral production (\( \epsilon \)) and to reduce the rate of production of infected cells (\( \eta \)) [19], which implies that both of the treatment parameters are non-zero. For a bifurcation analysis, it is more convenient to have a single bifurcation parameter, and so, we also make the assumption that:

<a id='63285dbe-9e44-40a4-9b6f-bb8345307e90'></a>

η = αε (27)

<!-- PAGE BREAK -->

<a id='0d835ddd-263d-4e72-9a18-642d20dec7fd'></a>

Viruses 2018, 10, 195

<a id='71cdebfe-db31-4274-972d-c44c2a0acc26'></a>

11 of 41

<a id='2da7f2fe-8f9c-4dee-983a-ffddbd722232'></a>

for some $\alpha$ > 0. It has been shown that the major effect of interferon is to block production or release of virions from an infected cell [2], and this implies that:

<a id='6d266c8b-9dbe-4276-b070-d72b6e510f83'></a>

α < 1                                                                       (28)

<a id='f2ca62a7-d568-47cc-b23e-9093f3207403'></a>

The equations in terms of all these new variables are then given by:

x' = Sy + x/(x+y) - x - (1 - αε)Bxz (29)

y' = 1/(1+R) (y/(x+y) - y) - Dy + (1 - αε)Bxz (30)

z' = (1-ε)Py - Cz - (1 - αε)Bxz (31)

<a id='5a1548f4-0490-4318-b09d-46a596f973ad'></a>

where the prime denotes derivatives with respect to τ, and the non-dimensional parameters are given by:

<a id='ce7616d0-cf33-47f4-adb2-295419f93105'></a>

S = \frac{s}{r_T + d'}
B = \frac{\beta r_T T_{max}}{(r_T + d)^2}
R = \frac{r_T}{r_I} - 1
D = \frac{r_T \delta - r_I d}{r_T(r_T + d)}
P = \frac{p}{r_T + d'}
C = \frac{c}{r_T + d}
(32)

<a id='7991f8ee-b4c1-49e5-8e57-0ea3317a5390'></a>

We note that our previous assumptions that $r_I < r_T$ and $d < \delta$ imply that $D > 0$. We also explain our choice of the parameter $R$. The coefficient multiplying the first term in (30) is $r_I/r_T$, and this satisfies $0 < r_I/r_T < 1$. We generally define parameters so that they are positive, but in this case, we have two conditions to satisfy. However, we note that these two conditions are equivalent to the single condition $r_T/r_I > 1$, since it is implicitly assumed that the ratio is finite. Thus, we define $R = r_T/r_I - 1$ and note that $R \to \infty$ as $r_I/r_T \to 0$ and $R = 0$ when $r_I/r_T = 1$. Thus, the single condition $R > 0$ ensures that both conditions on the ratio $r_I/r_T$ are satisfied. We note therefore that all of these non-dimensional parameters must be positive.

<a id='a72d7cff-65fc-40b3-a022-4af682443cee'></a>

We also require that \(\epsilon \in [0,1)\), which ensures that the treatment factor \(1 - \epsilon\) is positive, which then also implies that \(1 - a\epsilon\) is positive using (28).

<a id='394d1255-4133-46ae-b20d-5305f7ce823f'></a>

## 4. Validation of the New HCV Model

In order to validate our new HCV model, we need to check some fundamental mathematical and biological properties of the model. From a mathematical perspective, we need to ensure that the equations are well-posed (a solution exists, is unique and depends continuously on the initial conditions). From a biological perspective, we must show that the solutions are non-negative for all time and are bounded.

<a id='6a1c0436-a6b5-4544-aca2-a7c6557d9836'></a>

All of our variables must be non-negative as they are related to physical quantities, and so,
we first show that the non-dimensional Equations (29)-(31) have an invariant region within the octant
x, y, z ≥ 0. Using polar coordinates defined by x = r cos θ, y = r sinθ, we see that:

<a id='a2a58997-9eea-4026-a599-4eb7e34fe2af'></a>

$$\frac{x}{x + y} = \frac{\cos \theta}{\cos \theta + \sin \theta'}$$ $$\frac{y}{x + y} = \frac{\sin \theta}{\cos \theta + \sin \theta}$$

<a id='9170280a-55cd-482d-8ff3-38f9bcabf5e2'></a>

and so, the quotients that occur in Equations (29) and (30) are well defined in the limit r → 0 along rays with fixed θ for 0 ≤ θ < π/2. However, this also implies that the vector field is not uniquely defined along the z axis, and so, we exclude a neighbourhood of this axis. In a modelling context, the z axis (x = y = 0) corresponds to there being no healthy or infected hepatocytes, which is unrealistic.

<a id='38bfb5c5-36b5-46b5-95df-0fc35cba5bc4'></a>

Theorem 1. We define the octant O = {(x,y,z) ∈ R³ : x,y,z ≥ 0} and a cylinder around the z axis C = {(x,y,z) ∈ R³ : x² + y² < r²₀,z ≥ 0}. The region R = O\C is invariant under the flow of Equations (29)–(31) for sufficiently small r₀ > 0. Moreover, the line y = z = 0, x ≥ r₀ is an invariant line,

<!-- PAGE BREAK -->

<a id='d9fdaa70-0b24-4ffa-bd8b-c6a290b44ac9'></a>

Viruses 2018, 10, 195

<a id='79dbbd99-148b-4253-98e7-50203d0972b1'></a>

12 of 41

<a id='d7dac8e2-1073-4671-aa35-99d90ab157bc'></a>

corresponding to the dynamics of a healthy liver, on which x converges exponentially to the steady state x = 1 for all x(0) \u2265 r0.

<a id='9241a719-57ba-4c9a-9143-aa85dadcc21c'></a>

**Proof.** We first consider the line given by y = z = 0, x ≥ r₀. On this line, we have y' = z' = 0, and so, it is invariant for all time; and the flow is given by:

<a id='bea8a11d-5a97-4846-8366-ce46248241c5'></a>

x' = 1 - x

<a id='6ff48684-79ea-4c66-9362-9139c0734283'></a>

The solution of this equation consists of exponential convergence to the steady state x = 1 for all
x(0) \ge r_0.

<a id='34ad4e70-3a53-4b8f-8946-0e6ac300ee71'></a>

The region $R$ is bounded by the planes $P_1$ ($x = 0$, $y \ge r_0$, $z \ge 0$), $P_2$ ($x \ge r_0$, $y = 0$, $z \ge 0$) and $P_3$ ($x^2 + y^2 \ge r_0^2$, $z = 0$) together with the surface $S = \{(x,y,z) \in R^3 : x^2 + y^2 = r_0^2\} \cap O$. We will show that the vector field given by Equations (29)-(31) on these surfaces is directed inside the region $R$ except for the invariant line.

<a id='0d34d13c-f662-4658-9f13-95b09227a6e2'></a>

Taking the inner product of the vector field with the inward pointing normal on the plane $\mathcal{P}_1$, we see from (29) that:

$x'|_{\mathcal{P}_1} = Sy$

<a id='d1aaf017-cc14-482f-86dc-8a2edf87f524'></a>

and so, $x'|_{P_1} > 0$ on this plane since $y \ge r_0 > 0$. Thus, the vector field is directed inside $\mathcal{R}$ on this plane.
Similarly, from (30), we have:

$y'|_{P_2} = (1 - \alpha\epsilon)Bxz$

<a id='95304d2e-3581-44f5-8250-7c2f237ddc46'></a>

and so, $y'|_{P_2} > 0$ for $z > 0$ (since $1 - \alpha\epsilon > 0$ as $\alpha, \epsilon < 1$) and $y'|_{P_2} = 0$ for $z = 0$, which is the invariant line. Thus, the vector field is directed inside $\mathcal{R}$ on this plane, except for the invariant line.

From (31), we also have:

$z'|_{P_3} = (1 - \epsilon) Py$

<a id='9b905008-1c53-4f0f-8394-874d6018fd73'></a>

and so, $z'|_{P_3}$ is positive everywhere except on the invariant line, since $1 - \epsilon > 0$ (as $\epsilon < 1$).
Finally, we consider the surface $S$. The normal to this surface points in the $r$ direction when $x = r\cos\theta$, $y = r\sin\theta$. Differentiating the equation $x^2 + y^2 = r^2$ with respect to $\tau$ and using (29),
(30) gives:

$r' = \frac{1 + R \cos^2 \theta}{(1 + R)(\cos\theta + \sin\theta)} + O(r)$

<a id='c7fa1893-2693-4fef-8ff9-8f5be59c9609'></a>

Therefore, r' |r=0 > 0, since 0 is in the first quadrant, and this implies that r' |r=r0 > 0 for sufficiently small r0, 0 ≤ 0 < π/2, z ≥ 0. Thus, the vector field points inside R also on this surface.
Thus, we conclude that any trajectory with (x(0),y(0), z(0)) ∈ R = O\C must satisfy (x(t),y(t),z(t)) ∈ R for all t > 0, and so, R is invariant. □

<a id='599531af-8b77-425b-a554-b6c7ab5eb213'></a>

We now show that our model equations are well-posed on the region $\mathcal{R}$.

<a id='d8d2ba68-6185-4e7e-8495-8e38be9860a8'></a>

**Theorem 2.** _The model Equations (29)-(31) are well-posed on the region R defined in Theorem 1._

<a id='627a0e64-9305-4911-95fa-2496ab3e2614'></a>

**Proof.** The well-posed condition requires the local existence and uniqueness of solutions of the model equations. For the system of differential equations given by u' = f(u,t), u(t₀) = u₀ with u ∈ Rⁿ, if the function f is continuous and satisfies a Lipschitz condition in u on a region |t - t₀| ≤ α, ||u - u₀|| ≤ β, then it is well-posed [20], and there is then a unique solution on an interval |t - t₀| ≤ δ for some δ ≤ α.

<a id='e7f10f99-a22f-42be-9d67-673949cacb52'></a>

For our model equations given by (29)–(31), the continuity and Lipschitz conditions are satisfied for any such bounded region in the positive octant if the terms x/(x + y) in (29) and y/(x + y) in (30) are excluded. Once the cylinder C in the positive octant is excluded, then these nonlinear terms also satisfy a Lipschitz condition on any bounded region since x + y is bounded below by r0. Therefore, our model equations are well-posed. □

<!-- PAGE BREAK -->

<a id='aea4f3b3-7aaa-4c4a-8fb6-9d394abd7670'></a>

Viruses 2018, 10, 195

<a id='128534f3-9b8c-44fa-9a2f-202bf803f8b1'></a>

13 of 41

<a id='93dd023e-359a-42f0-b1f2-4d2df20732bc'></a>

It remains to show that the solutions are bounded for all time, which we can do provided that a condition on the parameters holds, and this will also imply the global existence of solutions.

<a id='0a40d294-ddac-43c8-beb5-6cfbfb73ebbf'></a>

Theorem 3. If:

$\min(S, (1 - \epsilon)P)(1 + R) - (1 + D(1 + R)) < 0$
(33)

<a id='f524a9e5-c57d-4db1-aaa5-6e81f600888c'></a>

then there is a bounded invariant region contained in the region $\mathcal{R}$ (defined in Theorem 1). In this case,
the solution of Equations (29)–(31) exists and is bounded for all $t \geq 0$ for any finite initial conditions.

<a id='5c8689d2-acaa-4e86-bae6-72484ff08786'></a>

We note that this theorem gives a sufficient condition for bounded solutions. If this condition is not satisfied, it may still be the case that the solutions are bounded. We note that the condition (33), when divided by (1 + R), requires that the coefficient of the linear decay term in y in (30) must exceed one of the coefficients of the linear growth terms in y in Equation (29) or (31).

<a id='da056f03-3d31-4d77-bff6-1618a0982dce'></a>

**Proof.** We show that the region $\mathcal{R}$ defined in Theorem **1** (the positive octant with a cylinder around the z axis removed) together with the additional restriction that:

<a id='f5a699d8-255e-416c-8274-c1e1afd61d64'></a>

wx + y + (1 - w)z ≤ k

<a id='d17da0ce-f9ca-403e-8298-94e376079aa7'></a>

is a bounded invariant region for $k > 0$ sufficiently large and for all $w \in (0, 1)$ provided that a condition on the parameters is satisfied. We note that this region is not bounded for $w = 0$ and $w = 1$, which is why we require that $w \in (0,1)$. This region is shown in Figure 3.

<a id='31fd1055-54b3-46a8-aa9f-d741e9ec0dad'></a>

<::A 3D plot showing a blue conical shape originating from the origin, a teal cylindrical shape along the z-axis, and a green curved surface on top of the cylinder. The x-axis is labeled "x" and has the expression "k/w" along it. The y-axis is labeled "y" and has the expression "k" along it. The z-axis is labeled "z" and has the expression "k/(1-w)" near its top.
: 3D plot::>

<a id='8b6f7aca-dcf3-4342-a1e8-b6150391d909'></a>

Figure 3. The invariant region in the positive octant bounded by the cylinder C (see Theorem 1) and the plane (34).

<a id='961f0f03-4f27-4165-9c03-5ade55567987'></a>

Since we have already shown that the region R is invariant, it remains to show that the vector
field is directed inside the bounded region on the plane:

<a id='c11d261b-0d20-44b7-830d-d8f1885aed71'></a>

wx + y + (1 - w)z = k (34)

<a id='b0fd5f4e-fe90-467b-9567-a25a66bfe5b4'></a>

when the condition (33) holds.
Using the model Equations (29)-(31), we see that:

$wx' + y' + (1 - w)z' = -wx + \left(wS - \frac{1}{1+R} - D + (1-w)(1-\epsilon)P\right)y - (1-w)Cz$
$+ \frac{wx}{x+y} + \left(\frac{1}{1+R}\right)\left(\frac{y}{x+y}\right)$

<!-- PAGE BREAK -->

<a id='d41bca9f-8cf5-4901-ba7c-7543d0d058fb'></a>

Viruses 2018, 10, 195

<a id='4ce234ca-e796-4ab6-af20-6ffd9f2df6d9'></a>

14 of 41

<a id='3888beee-0e9b-4117-98ca-16c1dea22918'></a>

and substituting for z using (34) gives:

$wx' + y' + (1 - w)z' = (C-1)wx + \left(wS - \frac{1}{1+R} - D + (1 - w)(1 - \epsilon)P + C\right)y - Ck \\ \qquad\qquad\qquad\qquad\qquad\qquad + \frac{wx}{x+y} + \left(\frac{1}{1+R}\right)\left(\frac{y}{x+y}\right)$ (35)

<a id='f0cdc8d2-0c66-4fb5-b967-4a8bdeb6b7fe'></a>

We first omit the nonlinear terms and so consider the function:

$f(x,y) = (C-1)wx + \left(wS - \frac{1}{1+R} - D + (1 - w)(1 - \epsilon)P + C\right)y - Ck$

<a id='c08f3061-9739-43c5-9d69-3f1b604e350d'></a>

which is a linear function of x and y. We first show that this function is negative at the three corner points of the triangle where the plane (34) intersects the positive octant O, ignoring the excluded cylinder C at this stage. The function evaluated at these corner points is given by:

<a id='c3c20d99-b0a5-4f9a-931c-552a01c3f89f'></a>

f(0,0) = -Ck
f(0,k) = (wS - 1/(1+R) - D + (1-w)(1-ε)P)k
f(k/w,0) = -k

<a id='ee9d11c1-e77f-4494-8411-a0149ef4df0b'></a>

If we assume that:
wS - 1/(1+R) - D + (1 - w)(1 - \epsilon)P < 0                               (36)

<a id='f214b59b-3e97-4116-b32d-6e78787bf993'></a>

then f(x, y) is negative at all three of the corner points for all k > 0. Since it is a linear function of x and y, this implies that it must also be negative on the boundary and the interior of the triangular region generated by these three points.

<a id='43bbde4f-3d34-4613-9223-c66dc7c264a2'></a>

We have so far ignored the two nonlinear terms in (35), which are both positive. We note that:

<a id='544cd9b7-b1d0-4562-ab7b-0df43ab6f452'></a>

0 ≤ x/(x+y) ≤ 1 for all (x,y) ∈ R

<a id='30659780-81c0-46ae-843c-d899f67f495c'></a>

and so:

$0 \le \frac{wx}{x+y} \le w$ for all $(x,y) \in \mathcal{R}$

<a id='60d8deab-a404-4e5c-9cea-b1289cb1c592'></a>

Similarly,

$0 \le \left(\frac{1}{1+R}\right)\left(\frac{y}{x+y}\right) \le \left(\frac{1}{1+R}\right)$ for all $(x,y) \in \mathcal{R}$

<a id='03b3aee1-7610-4b86-9823-fed97c43a8d8'></a>

Thus, these two nonlinear terms are uniformly bounded above. Now, the corner points of the linear function f(x, y) scale with k, and so, f(x, y) will scale with k for all x and y. Hence, when adding the bounded nonlinear terms to f(x, y), the resulting function will be negative over the whole of the triangular region for sufficiently large k. Hence, the vector field points inside the invariant region over the whole of the plane (34) intersected with the positive octant provided that (36) holds and k is chosen sufficiently large, and the bounded region (which excludes the cylinder C) is then invariant. For any given initial conditions, k must also be chosen sufficiently large so that the initial conditions are contained within the invariant region. The solution must therefore be bounded for all time.

<a id='a4f59c86-10cc-452b-830c-03ade6b62d2c'></a>

We next consider the condition (36) in more detail. Suppose that (1 - ε)P < S. Then, when w ∈ (0,1), we have that: wS + (1 – w)(1 – ε)P ∈ ((1 – ε)P, S)

<a id='4627c2b5-8099-4842-b5d3-ecbab30b1da4'></a>

Thus, if $(1-\epsilon)P - 1/(1 + R) - D < 0$ $(w = 0)$, then by the intermediate value theorem, there exists a small $w > 0$ such that (36) holds also. A similar argument holds if $(1 - \epsilon)P > S$ with the condition $S - 1/(1 + R) - D < 0$. Thus, the optimum value of $wS + (1 - w)(1 - \epsilon)P$ to choose to be as small as possible is $S$ if $S < (1 - \epsilon)P$ or $(1 - \epsilon)P$ if $S > (1 - \epsilon)P$, which is equivalent to

<!-- PAGE BREAK -->

<a id='51dd6c35-2e8f-40df-ac86-a12841ef10a3'></a>

Viruses 2018, 10, 195

<a id='2f616d39-0118-4fcb-85ba-0c841dfbe181'></a>

15 of 41

<a id='6c554bf0-918c-4952-a258-d6a0881a0974'></a>

min(S, (1 – є)P), and this gives the condition (33) in the statement of the theorem after multiplying through by (1 + R).

<a id='aa43ab8c-81e5-4113-b2cb-02ce4d346378'></a>

It is a standard result in ode theory that if the function is continuous and satisfies a Lipschitz condition for all t ≥ 0 and on a given domain, then solutions either exist for all time or blow up in finite time [20]. On the bounded domain described above, Equations (29)–(31) satisfy these conditions, using the same argument as in the proof of Theorem 2, and since, we have shown that the solutions are bounded, if (33) holds, then this implies that the solution exists for all t ≥ 0. ◻

<a id='72af21e6-b47b-4b56-afdd-9851dc23e433'></a>

## 5. Analysis of the New HCV Model

We now consider the steady states and their bifurcations of the new HCV model given by
Equations (19)-(21), together with the dynamical properties of the model.

<a id='32839999-c454-4019-b91d-4d33ab478d31'></a>

## 5.1. Assumptions

In our analysis, we make a number of assumptions on the parameters. Rather than having them scattered throughout the text, we now state our main assumptions together for later reference. The key assumptions that we make on the parameters are as follows:

&alpha; &isin; (0,1)                                                                 (37)
&epsilon; &isin; [0,1)                                                                 (38)
(B + C)(B - CR) > BCP(1 + R)                                                (39)
D = BP / (B + C)                                                            (40)

<a id='2443ba47-492a-4112-816e-6fa12fc782c0'></a>

The justification for the first two of these conditions was given in Section 3.6, and we assume that these always hold. When we require Assumptions (39) and (40), this will be stated.
Note that if (39) holds, then:

B > CR (41)

must also hold. Moreover, if (39) holds, then:

<a id='f60f7c4f-b4ba-431f-9cf3-4efe80d6dbeb'></a>

<::B + C > CP (B(1 + R) / (B - CR))
: equation::>

<a id='6014222f-7eda-4467-9e78-bc62111d48b9'></a>

We note that B(1+R) > B > B - CR, and so, B(1+R)/(B - CR) > 1. It then follows that:

B > C(P-1) (42)

<a id='60ade5b8-7fbe-4a85-b8eb-a8f586239fe5'></a>

5.2. *Steady States* (S = 0)
We first consider the steady states of our revised model (29)–(31) in the special case when S = 0.
In Section 5.4, we will show how these states are perturbed when S > 0.
When S = 0, there is a branch of uninfected steady states given by:

<a id='faa7065a-b8e2-4ce7-981f-0d56a10f6703'></a>

x_u = 1, y_u = z_u = 0 (43)

<a id='37880f88-242d-4257-b2cd-c755722eec67'></a>

for all ∈ [0, 1).

<a id='853a7f53-07fa-4b19-9420-1439068334a1'></a>

Due to the absence of the S term, there is also a state of pure infection given by:

<a id='e9ff7621-9e60-4579-9ea0-f1bde91b1e6f'></a>

xp = 0, yp = 1 / (1 + D(1 + R)), zp(ε) = (1 - ε)P / (C(1 + D(1 + R))) (44)

<!-- PAGE BREAK -->

<a id='a17c8bdf-c9be-475f-bc49-8b157e54049b'></a>

Viruses 2018, 10, 195

<a id='3c4f3482-af57-4aa5-8474-67a80372d725'></a>

16 of 41

<a id='2cc5f27c-18b8-4259-9134-4e679f1cd941'></a>

since, if the only mechanism for cell regeneration is by division and there are no healthy hepatocytes (x = 0), then that state will persist as there are no healthy cells to divide. We note that x_p and y_p are constant, but that z_p depends on e.

<a id='e794d76a-cfd2-491b-b071-2777c0a43630'></a>

There is also a branch of infected steady states given by:

x_i(\epsilon) = C(1 + D(1 + R))z_i(\epsilon) - (1 - \epsilon)P / f(z_i(\epsilon),\epsilon)

y_i(\epsilon) = z_i(\epsilon)[BCR(1 - \alpha\epsilon)z_i(\epsilon) - (B(1 - \alpha\epsilon) + C)] / f(z_i(\epsilon),\epsilon)

<a id='7e7634b1-66ca-4b28-9d73-57114147ceeb'></a>

where:

f($z_i(\epsilon)$, $\epsilon$) = B(1 - $\alpha\epsilon$)[(1 - $\epsilon$)PR - 1 - D(1+R)]$z_i(\epsilon$) - (1 - $\epsilon$)P (45)

and $z_i(\epsilon$) is a solution of the quadratic equation:

<a id='9e6b3097-b989-4f8b-9e56-b5b3c63ff253'></a>

B^2 CR(1 - αε)^2 z^2 + B(1 - αε)(C(R + D(1 + R))) - B(1 - αε))z

<a id='d7ce9d19-45ed-4f80-912c-571b2c982027'></a>

+ (1 + R)[B(1 - αε)(D - (1 - ε)P) + CD] = 0 (46)

<a id='d40a5294-6161-4a57-ae3d-1d15dd10883b'></a>

These solutions will only be valid provided that $f(z_i(\epsilon), \epsilon) \neq 0$ for all $\epsilon \in [0, 1)$. We note that $f(z, \epsilon)$ is quadratic in $\epsilon$ and that for all $z > 0$:

$f(z, 1) = -B(1-\alpha)[1 + D(1 + R)]z < 0$

$f(z, \frac{1}{\alpha}) = \frac{(1-\alpha)P}{\alpha} > 0$

<a id='8d242c61-6d10-46e6-9e2e-bf4100a0dd29'></a>

since α < 1 (see (37)). Thus, there exists a function ε̃(z) such that f(z, ε̃(z)) = 0 with 1 < ε̃(z) < 1/α for all z > 0, which is clearly outside our range of interest.
The coefficient of ε² in f(z, ε) is αBPRz, which is positive for all z > 0, and this implies that the second value of ε that gives f(z, ε) = 0 must occur for ε < 1. In order to avoid the infected steady state branch blowing up in our range of interest, we require that this second root occur for ε < 0, and this will be the case provided that f(z, 0) < 0 for all z > 0. Now:

f(z,0) = B(PR − 1 − D(1 + R))z − P

<a id='f3fd71e6-f485-4eea-a488-9c97d70ab1ba'></a>

The sign of the z coefficient in this expression is not clear. However, we assume that (40) holds, and so, substituting for D gives:

$$f(z,0) = -\frac{B(P(B - CR) + B + C)}{B + C} z - P$$

<a id='b03b2b75-9f59-4a9e-b4de-c643412c43ae'></a>

which must be negative for all z > 0 using (41). Therefore, assuming that (40) and (41) hold, then f(z, ε) ≠ 0 for all ε ∈ [0, 1), and so, the infected branch of solutions does not blow up in our region of interest.

<a id='b7e3324d-7267-4561-8bbf-c971efd9dd0c'></a>

5.3. Bifurcations (S = 0)

We now consider bifurcations that occur in our equations with S = 0. In particular, there are bifurcations occurring when the branch of infected steady states intersects the uninfected branch and when it intersects the pure infection branch.

<!-- PAGE BREAK -->

<a id='729d111d-b619-4fae-8578-e6536b01862c'></a>

Viruses 2018, 10, 195

<a id='4dedc17a-8407-42c4-9e22-2f65a1fbf9e7'></a>

17 of 41

<a id='bbf4f626-d255-485e-be9c-e564bc212038'></a>

5.3.1. Bifurcation on the Uninfected Branch

**Lemma 1.** *With S = 0, there are two bifurcation points that occur on the uninfected branch of steady state solutions (43) that each give rise to a bifurcating branch of infected steady state solutions. One bifurcation occurs for ε > 1/α > 1, and so is out of our range of interest. The other bifurcation point occurs at ε = ε₀ < 1 where:*

<a id='216340e6-0d4f-4a6b-8603-bb6b0c5cecef'></a>

$\epsilon_0 \begin{cases} <0 & \text{if } BP < D(B+C) \\ =0 & \text{if } BP = D(B+C) \\ >0 & \text{if } BP > D(B+C) \end{cases}$

<a id='2dea1984-ad78-4e04-838e-00b204ab6d35'></a>

The uninfected branch is stable for ε0 < ε < 1 and unstable for ε < ε0.

<a id='8ecac335-6cd0-4f9c-b03e-9c623291dd39'></a>

Proof. The Jacobian matrix J(x, y, z) of Equations (29)-(31) (with S = 0) evaluated at the uninfected steady state is given by:

J(1,0,0) = 

```
⎡ -1          -1          -(1 - αε)B  ⎤
⎢  0          -D           (1 - αε)B  ⎥
⎣  0       (1-ε)P       -C - (1 - αε)B ⎦
```
(47)

<a id='ea0efc7c-802e-4db6-a979-343db03fbe78'></a>

Clearly, one eigenvalue of this matrix is -1. We note that the remaining two eigenvalues must be real since, if they were complex, then y would oscillate around the steady state value y = 0 and similarly for z. However, by our invariance result (Theorem 1), this is not possible.
A bifurcation point on the branch of uninfected steady states occurs when det J(1,0,0) = 0,

<a id='344def87-1766-4052-abf9-f6ef99ee772e'></a>

which gives:

$\alpha BP\epsilon^2 + (\alpha D - (1+\alpha)P)B\epsilon + BP - D(B + C) = 0$ (48)

<a id='c7f9d956-7298-4256-8e2c-f91460679368'></a>

If ϵ = 1 + μ, then (48) expressed in terms of μ is given by:

<a id='f065e790-f7fa-40b6-aa7d-027606edb083'></a>

αBPμ² + (αD – (1 − α)P)Bμ – D(B(1 − α) + C) = 0 (49)

<a id='56beb84e-a8f9-433b-98a4-c24f8303001a'></a>

We note that the constant term is negative (using (37)), and the μ² coefficient is positive; so the quadratic equation (49) has one positive and one negative solution. This implies that the two solutions of (48) must lie on opposite sides of ϵ = 1, and so, one bifurcation point occurs for ϵ = ϵ₁ > 1 and the other for ϵ = ϵ₀ < 1.
A similar analysis with ϵ = 1/α + μ also shows that the two solutions in μ must have opposite signs, and this implies that ϵ₁ > 1/α > 1.
Since ϵ₁ is always positive, the sign of the other solution ϵ₀ must match the sign of the constant coefficient of (48) since the coefficient of ϵ² is positive, as stated.
To determine the stability of the uninfected branch, we need to know the signs of the three eigenvalues of J(1,0,0). We have already noted that one eigenvalue is −1, and the remaining two eigenvalues are found from the lower 2 × 2 block in the Jacobian matrix, which we denote by J₁. We note that:

<a id='9cd380bc-f00b-4f83-b9bf-77c72ec7b67e'></a>

tr(J1) = -C - D - (1 - αε)B < 0
since αε < 1 (using (37), (38)) and:
det(J1) = -αBPε² - (αD - (1 + α)P)Bε - BP + D(B+C)

<a id='569407ff-8136-4c16-a84c-454978cc1389'></a>

The determinant is negative for ε < ε₀ since the coefficient of ε² is negative. A negative determinant implies that the eigenvalues have the opposite sign, and so, there is one positive and one negative eigenvalue, which implies that the uninfected branch is unstable for ε < ε₀.

<a id='2f920db2-48ed-40e8-a150-e211bf819f4c'></a>

At the bifurcation point $\epsilon = \epsilon_0$, there is one zero eigenvalue. We note that a double zero eigenvalue is not possible since the other bifurcation point occurs at $\epsilon = \epsilon_1 > 1/\alpha$. Thus, the determinant changes

<!-- PAGE BREAK -->

<a id='c22b7cd8-652d-43fa-88cc-9937b2ebbfd9'></a>

Viruses 2018, 10, 195

<a id='85bba608-4bf6-4f03-ba51-7eb1cf96dc3d'></a>

18 of 41

<a id='366b9852-8e1e-4d78-b98b-b869ce012ef1'></a>

sign at ε = ε0 and so is positive for ε0 < ε < 1. A positive determinant and negative trace implies that both of the eigenvalues are negative, and so, the uninfected branch is stable in this range. □

<a id='14cd35b6-d98b-44d5-ac91-4926682bd417'></a>

Following our discussion regarding spontaneous clearance in Section 3.5, we note that the stability of the uninfected branch for our model agrees with that shown in Figure 2. We initially assume that the bifurcation occurs precisely at $\epsilon$ = 0 (Figure 2b), as this is the point between the two cases discussed. By Lemma 1, this occurs when $BP = D(B+C)$, and solving this for $D$ gives the relation (40).

We now consider the bifurcating branch of infected solutions that arises from the bifurcation point at $\epsilon$ = 0.

<a id='9672af8a-44fb-4570-9752-f29e7019693a'></a>

Lemma 2. When (40) holds, there is a transcritical bifurcation at \u20ac = 0 on the uninfected branch of solutions.
The bifurcating branch of infected solutions is given by:

x = 1 - c(BP + B + C)\u20ac + O(\u20ac^2)
y = c(B + C)\u20ac + O(\u20ac^2)
z = cP\u20ac + O(\u20ac^2)

<a id='c45717ea-8d15-40d8-94d6-764710814f20'></a>

where:

c = \frac{(1+R)(B+(1+\alpha)C)}{(B+C)(B-CR)-BCP(1+R)}\tag{50}

<a id='929c92cc-504c-4deb-89c4-3fc3c9a5c394'></a>

*This branch is unstable for ε > 0 and stable for ε < 0.*

<a id='10f913f2-b132-49e4-919d-d6bf6a325f83'></a>

**Proof.** To find the bifurcation equation, we solve (29)+(1+R)(30) and (31) for x and y in terms of z and ε, which gives:

x = 1 - \left(\frac{BP+B+C}{P}\right) z + zO(z, \epsilon) (51)
y = \left(\frac{B+C}{P}\right) z + zO(z, \epsilon) (52)

<a id='a621fc9a-726f-4214-b7cb-4c5df517cddf'></a>

Substituting these into (29) gives the bifurcation equation:

c₁zε + c₂z² + zO((z,ε)²) = 0 (53)

<a id='170ef9c4-7c5f-466b-9002-36f5e27c4d78'></a>

where:
c_1 = -BP^2(1+R)(B + (1 + α)C)
c_2 = BP[(B+C)(B-CR) - BCP(1 + R)]

<a id='174110b8-06c4-4a6c-8100-7d7ea4e4889a'></a>

The two quadratic terms are required for the normal form of a transcritical bifurcation [21].
The trivial solution z = 0 of (53) corresponds to the uninfected branch. The non-trivial solution gives a
low order solution of the bifurcating infected branch, which is given by:

<a id='958e1282-bd8e-4ebb-8d82-101a92b5c532'></a>

z = -\frac{c_1}{c_2}\epsilon + O(\epsilon^2) = cP\epsilon + O(\epsilon^2)

<a id='47059f38-19fe-4534-afba-2c4d31f2f569'></a>

Substituting this back into (51) and (52) gives the stated expansions for x and y in terms of e. With a transcritical bifurcation, the stability of the bifurcating branches is the opposite of the trivial solution, and so, since the uninfected branch is stable for e > 0 (see Lemma 1), the bifurcating branch must be unstable for € > 0 and stable for € < 0. □

<a id='26326106-2483-4877-9dc7-53731b7f6e0d'></a>

Clearly, Lemma 2 can be generalised to the case of a bifurcation point occurring at ε = ε₀ when (40) does not hold.

<!-- PAGE BREAK -->

<a id='efad3582-cac8-45cc-87c1-c5ff38b35ee9'></a>

Viruses 2018, 10, 195

<a id='ab33cb30-8140-4d08-b167-1ce6dba9b443'></a>

19 of 41

<a id='dea4f73b-56b1-4a44-8256-ed44be7a293b'></a>

We note that only one half of the bifurcating branch of infected solutions lies within our invariant region R, and this is the half for which ce > 0, since then, y, z ≥ 0. In this case, we also have x ≤ 1, as we would expect. Referring back to Figure 2, we would like the valid half of the bifurcating branch to occur for e > 0, and this occurs provided that c > 0. Clearly the numerator of c is positive, and Assumption (39) ensures that the denominator is also positive so that c > 0. We then have precisely the situation sketched in Figure 2b.

<a id='8548e493-cb78-4a4f-abfc-a747dbf54b9e'></a>

Now, if condition (40) is perturbed slightly, then the bifurcation point will occur for ϵ either positive or negative. If it occurs for ϵ < 0, then the uninfected steady state with no treatment (ϵ = 0) is stable, but with a nearby unstable steady state (Figure 2a). Conversely, if the bifurcation point occurs with ϵ > 0, then the uninfected steady state with no treatment is unstable (Figure 2c).

<a id='3d8dd68c-5cef-4774-b4ac-4f34c6ac9637'></a>

### 5.3.2. Bifurcation on the Pure Infection Branch
In addition to the bifurcation involving the uninfected and infected branches of solutions, there is also a second bifurcation where the infected branch intersects the pure infection branch.

<a id='b3a0cd56-d27d-425f-b35c-30abddaf36c1'></a>

Lemma 3. With S = 0, there are two bifurcation points that occur on the pure infection branch of steady state solutions (44) that each give rise to a bifurcating branch of infected steady state solutions. One bifurcation occurs for € > 1/α > 1 and so is out of our range of interest. The other bifurcation point occurs at € = €2 < 1 where:

€2 {
< 0 if BP < CD(1+R)(1+D(1+R))
= 0 if BP = CD(1+R)(1+D(1+R))
> 0 if BP > CD(1+R)(1+D(1+R))


<a id='b83d9a9d-af1b-48bb-a1c4-bd39f624a4bd'></a>

The pure infection branch is stable for ε < ε₂ and unstable for ε₂ < ε < 1.

<a id='a906ce1e-8ffd-485d-b5a5-d2e3c0d2bb32'></a>

**Proof.** The bifurcation points can be found by considering the Jacobian matrix derived from Equations (29)-(31) evaluated at the pure infection steady state. This matrix is lower triangular with diagonal entries given by:

<a id='3c82e000-2441-4bf2-81e7-f1bf9f7171fb'></a>

J(x_p, y_p, z_p(ε))_{1,1} = \frac{1}{y_p} - (1 - αε)Bz_p(ε) - 1
J(x_p, y_p, z_p(ε))_{2,2} = - \frac{1}{(1 + R)y_p}
J(x_p, y_p, z_p(ε))_{3,3} = -C (54)

<a id='f654a078-e09a-47f8-a50d-e050f60a6ed6'></a>

Since the matrix is lower triangular, these diagonal entries are the eigenvalues. Clearly, the second and third eigenvalues are negative. The bifurcation points therefore occur when $J(x_p, y_p, z_p(\epsilon))_{1,1} = 0$ Substituting for $y_p$ and $z_p(\epsilon)$ from (44) gives the quadratic equation in $\epsilon$:

<a id='2ddf2bf6-c9bf-4b86-bb65-a2631b93a10b'></a>

p(̘) = -BPα̘² + BP(1 + α)̘ + CD(1 + R)(1 + D(1 + R)) – BP = 0 (55)

<a id='74cf8958-ca32-400e-83a6-ae59f72f6fd4'></a>

If ε = 1 + μ, then (55) expressed in terms of μ is given by:

<a id='0f77d330-a125-4d8b-bd37-41e24b956a05'></a>

p(1 + μ) = -BPαμ² + BP(1 - α)μ + CD(1 + R)(1 + D(1 + R)) = 0

<a id='28b43ed5-527b-4f45-8bac-af87dcc18c18'></a>

Since the constant term is positive and the μ² coefficient is negative, this quadratic equation has solutions of opposite sign, which implies that the two solutions of (55) lie on opposite sides of € = 1. Clearly, the bifurcation point € = €3 > 1 is out of our range of interest, and so, we now consider the other bifurcation point at € = €2 < 1.

<a id='080449dc-4b74-4130-8553-064c4aef4642'></a>

A similar analysis with ε = 1/α + μ also shows that the two solutions in μ must have opposite signs, and this implies that ε_3 > 1/α > 1.

<!-- PAGE BREAK -->

<a id='904c38e6-1919-4fb6-b2d4-2d98c71ed239'></a>

Viruses 2018, 10, 195

<a id='97de2058-609a-4665-9267-20736b3c0ff4'></a>

20 of 41

<a id='0ebbcca6-46f6-4394-900b-26ff7de2f393'></a>

Since $\epsilon_3$ is always positive, the sign of $\epsilon_2$ will be the opposite of the sign of the constant coefficient in (55), since the $\epsilon^2$ coefficient is negative.
The stability of the pure infection steady state is determined by the sign of $J(x_p, y_p, z_p(\epsilon))_{1,1}$ since the other two eigenvalues of $J(x_p, y_p, z_p(\epsilon))$ are negative. Combining the two terms in (54) gives a rational function with a positive denominator. The sign is therefore determined by the numerator, which is the expression on the left-hand side of (55). Since $\epsilon_2 < 1 < \epsilon_3$ and the coefficient of $\epsilon^2$ is negative, then clearly, $J(x_p, y_p, z_p(\epsilon))_{1,1} < 0$ for $\epsilon < \epsilon_2$, and so, the pure infection steady state is stable in this range. There is no possibility of a double root occurring as the two roots lie on opposite sides of $\epsilon = 1$, and so, this quadratic must change sign at the bifurcation point. Therefore, the pure infection solution is unstable for $\epsilon_2 < \epsilon < 1$ as claimed. \square

<a id='a170e335-4add-423b-b544-dfcc18c8f979'></a>

It is natural to assume that the pure infection state is stable when there is no treatment ($\epsilon = 0$),
and from Lemma 3, we see that this occurs provided that:

$BP - CD(1 + R)(1 + D(1 + R)) > 0$ (56)

<a id='06078410-c2ba-4b3e-87e1-893d5300ee7b'></a>

which implies that $\epsilon_2 > 0$. However, we will show in Section 5.4.4 that this is in fact not required for our later analysis of the model. We also note that with the assumption (40), the inequality (56) becomes:

$(B+C)(B-CR) - BCP(1+R)^2 > 0$}```शनल```json{

<a id='45a8fc9b-24ee-4345-b2ac-e0e163c607c1'></a>

Clearly, this is very similar to the inequality in (39), but the fact that the last term is squared implies that the sign of this expression cannot be determined using (39) and so could be positive or negative.

<a id='bc94b677-5809-40bc-8d33-25a177e4b565'></a>

We now consider the bifurcating branch of infected solutions that arises from the bifurcation point
at \u20ac = \u20ac2.

<a id='fe8b066f-cb3b-4756-a74b-ab09cb9d92cf'></a>

Lemma 4. The bifurcating branch of infected solutions arising from the transcritical bifurcation on the pure infection branch at € = €2 is given by:

x = -$\frac{c_3}{c_4}$ (€ - €2) + O((€ - €2)^2)
y = y_p + c_5(€ - €2) + O((€ - €2)^2)
z = z_p(€2) + ($c_6 - \frac{P}{C}y_p$) (€ - €2) + O((€ - €2)^2)
  = z_p(€) + c_6(€ - €2) + O((€ - €2)^2) (57)

<a id='f927e3a7-77e3-45c0-bfe1-5c9f0b49beb1'></a>

_where:_


<a id='409b11ff-f317-46e2-954d-fc348601f46d'></a>

$$c_3 = B\left((1 - \alpha\epsilon_2)\frac{Py_p}{C} + \alpha z_p(\epsilon_2)\right)$$
$$c_4 = (1 - \alpha\epsilon_2)Bz_p(\epsilon_2) \left((1 - \alpha\epsilon_2)B\left(\frac{1}{C} - (1 + R)z_p(\epsilon_2)\right) - \frac{R}{y_p}\right)$$
$$c_5 = -\left((1 - \alpha\epsilon_2)B(1 + R)y_pz_p(\epsilon_2) - 1\right)\frac{c_3}{c_4}$$
$$c_6 = z_p(\epsilon_2) \left((1 - \alpha\epsilon_2)B\left(\frac{1}{C} - (1 + R)z_p(\epsilon_2)\right) + \frac{1}{y_p}\frac{c_3}{c_4}\right)$$

<a id='ccbb6133-592e-4dd5-93ed-684c26021ac5'></a>

This branch is stable for ϵ > ϵ₂ and unstable for ϵ < ϵ₂.

<!-- PAGE BREAK -->

<a id='58519e95-57c8-4e43-950d-f139ca4fd165'></a>

Viruses 2018, 10, 195

<a id='5b0ffd73-b9df-4e0c-a696-b5917636232b'></a>

21 of 41

<a id='166c937c-778d-4bf2-bee4-ab55c1c19816'></a>

**Proof.** Since the pure infection steady state has x = 0, we will derive the bifurcation equation in terms of x and ε - ε₂. To do this, we solve Equations (30) and (31) for y and z in terms of x and ε - ε₂, which gives:

<a id='2352e296-5bee-46d0-81f8-9e056c661e72'></a>

y = yp + ((1 - αε2)B(1+R)ypzp(ε2) - 1)x + xO(x, (ε - ε2)) (58)
z = zp(ε2) + zp(ε2) ((1 - αε2)B ((1+R)zp(ε2) - 1/C) - 1/yv)x

<a id='e0c38918-803a-4337-9803-34223dfcbe4b'></a>

- (P/C) y_p(ε - ε_2) + O(((x, (ε - ε_2))^2)) (59)

<a id='f9cf8d8f-04d1-40fe-83fc-38af1d5a472e'></a>

Substituting these into (29) gives the bifurcation equation:

$c_3x(\epsilon - \epsilon_2) + c_4x^2 + xO((x, (\epsilon - \epsilon_2))^2)$ (60)

<a id='a08d501d-2253-4011-a469-f15ba4472324'></a>

where:

$$
c_3 = B\left(\left(1 - \alpha\epsilon_2\right)\frac{P y_p}{C} + \alpha z_p(\epsilon_2)\right)
$$

$$
c_4 = \left(1 - \alpha\epsilon_2\right)B z_p(\epsilon_2)\left(\left(1 - \alpha\epsilon_2\right)B\left(\frac{1}{C} - (1 + R)z_p(\epsilon_2)\right) - \frac{R}{y_p}\right)
$$

<a id='b5bebe81-3d83-4940-8377-a6bbc03bc4f7'></a>

The two quadratic terms are required for the normal form of a transcritical bifurcation [21]. The trivial solution x = 0 of (60) corresponds to the pure infection branch. The non-trivial solution gives a low order solution of the bifurcating infected branch, which is given by (57). Substituting for x back into (58) and (59) gives the stated expansions for y and z in terms of (e – €2). We also note from the pure infection steady states (44) that:

<a id='5cfc6176-77a6-4a38-921e-667815b3cfe1'></a>

<:: $z_p(\epsilon_2) - \frac{P}{C}y_p(\epsilon - \epsilon_2) = z_p(\epsilon)$ : figure::>

<a id='97d26986-cf5d-4928-b5dd-80213f933f45'></a>

and this is used to derive the stated second form of z.
The stability of the bifurcating branches at a transcritical bifurcation is the opposite of the trivial
solution, and so, since the pure infection branch is stable for ε < ε2 (see Lemma 3), the bifurcating
branch must be unstable for ε < ε2 and stable for ε > ε2. □

<a id='5067831f-e3c1-4282-856b-d5400da7e4ad'></a>

We note that c3 > 0 using (37) and the fact that €2 < 1 (see Lemma 3). However, c4 could be positive or negative depending on the values of the parameters in the model. Since x cannot be negative, we see from (57) that:

* if c4 < 0, then x(€) has a positive slope, and valid solutions exist locally only for € ≥ €2;
* if c4 > 0, then x(€) has a negative slope, and valid solutions exist locally only for € ≤ €2.

<a id='dd716edb-c89e-499d-91fd-36c8cb20119b'></a>

Furthermore, if $c_4 > 0$, then:

$(1 - \alpha\epsilon_2)B \left(\frac{1}{C} - (1 + R)z_p(\epsilon_2)\right) > \frac{R}{y_p}$

<a id='917e4608-65bc-43a9-adb3-d083eba012f9'></a>

and this implies that:

c_6 > \frac{z_p(\epsilon_2)(1 + R)c_3}{c_4y_p}

<a id='2daa5420-f1ec-4cd4-9d6e-936b8b342af3'></a>

and so, c6 > 0 also. However, if c4 < 0, then c6 could be positive or negative.
The solutions of Equations (29)–(31) near the bifurcation point are sketched in Figure 4 for the three possible cases associated with different signs of c4 and c6.

<!-- PAGE BREAK -->

<a id='d08fd78f-02cd-4d16-9c89-2e920b6083ca'></a>

Viruses 2018, 10, 195

<a id='cd0fa5a7-6b33-442e-93c0-065d079220dd'></a>

22 of 41

<a id='0c4ed729-eb80-4dcb-a141-37d4089fbd8d'></a>

<::chart: Figure 4 shows six plots arranged in a 3x2 grid, illustrating solutions near a bifurcation. The plots involve an infected branch (red lines) and a pure infection branch (blue lines). Solid lines represent stable solutions, while dashed lines represent unstable solutions. Each column shares a y-axis label: the left column plots X, and the right column plots Z. All plots share an x-axis labeled ϵ, with a specific point ϵ₂ marked. The rows correspond to different parameter conditions: Top row (c₄ > 0), Middle row (c₄ < 0, c₆ < 0), and Bottom row (c₄ < 0, c₆ > 0). Top row, left plot (X vs ϵ, c₄ > 0): A solid blue line is at X=0 for ϵ from 0 to ϵ₂, then a dashed blue line at X=0 for ϵ > ϵ₂. A dashed red line originates from ϵ₂ and extends upwards and to the left. Top row, right plot (Z vs ϵ, c₄ > 0): A solid blue line decreases from the left, becoming a dashed blue line that continues to decrease to the right of ϵ₂. A dashed red line originates from ϵ₂ and extends upwards and to the left. Middle row, left plot (X vs ϵ, c₄ < 0, c₆ < 0): A solid blue line is at X=0 for ϵ from 0 to ϵ₂, then a dashed blue line at X=0 for ϵ > ϵ₂. A solid red line originates from ϵ₂ and extends upwards and to the right. Middle row, right plot (Z vs ϵ, c₄ < 0, c₆ < 0): A solid blue line decreases from the left, becoming a dashed blue line that continues to decrease to the right of ϵ₂. A solid red line originates from ϵ₂ and extends downwards and to the right. Bottom row, left plot (X vs ϵ, c₄ < 0, c₆ > 0): A solid blue line is at X=0 for ϵ from 0 to ϵ₂, then a dashed blue line at X=0 for ϵ > ϵ₂. A solid red line originates from ϵ₂ and extends upwards and to the right, then transitions to a dashed red line continuing upwards and to the right. Bottom row, right plot (Z vs ϵ, c₄ < 0, c₆ > 0): A solid blue line decreases from the left, becoming a dashed blue line that continues to decrease to the right of ϵ₂. A solid red line originates from ϵ₂ and extends upwards and to the right, then transitions to a dashed red line continuing upwards and to the right.::>

<a id='9a74f40a-6de4-40f1-99d6-6b8daf6e4e1f'></a>

5.3.3. The Infected Steady State Branch (S = 0)
We have found that the infected steady state branch intersects both the uninfected and the pure infection branches of steady states at transcritical bifurcation points. We next consider what happens to the infected branch in between these two bifurcations.

<a id='5795e73a-79f1-4935-90f8-7d5a48bee1f8'></a>

Theorem 4. We assume that (39) and (40) hold and that:

<a id='968696f4-6b0e-41c4-981c-51ce49fe84cc'></a>

R > (sqrt(2) - 1) / 2                                            (61)

<!-- PAGE BREAK -->

<a id='ca8429d1-ca38-4bd7-8671-c34b0c80c080'></a>

Viruses 2018, 10, 195

<a id='ed69c312-875e-4b0f-bf92-6e264eb4c882'></a>

23 of 41

<a id='c8d45e1d-8617-4b94-a379-522c6ac97213'></a>

Then, the bifurcation point at \(\epsilon = 0\) on the uninfected branch of solutions and the bifurcation point at \(\epsilon = \epsilon_2\) on the pure infection branch of solutions are connected by a continuous branch of infected steady state solutions. There is a single limit point on this branch of infected solutions, which occurs between the two bifurcations when \(c_4 < 0\) or after the bifurcation on the pure infection branch when \(c_4 > 0\). The limit point occurs at \(\epsilon = \epsilon_4\) where \(\epsilon_2 < \epsilon_4 < 1/\alpha\). The three possible cases, associated with different signs of the coefficients \(c_4\) and \(c_6\), are shown in Figure 5.

<a id='8dd5f1e5-e400-407f-b349-a3baaf5cf041'></a>

**Remark 1.** *We conjecture that Theorem 4 holds for all R > 0, so that condition (61) is unnecessary. However, we have been unable to prove this. Some evidence to support this conjecture is included in the proof. Condition (61) is not overly restrictive though, as it implies that r₁/r₄ < 2/(√2 + 1) = 0.8284.*

<a id='355adb62-92c9-4b56-bf7b-fe7080537791'></a>

<::A 2D plot showing curves on an epsilon (x-axis) versus z (y-axis) coordinate system. The x-axis ranges from 0 and increases to the right. The y-axis is labeled 'z'. There are three curves: a solid blue line decreasing from the top left to the bottom right, a solid red curve starting from the origin (0,0) and increasing before curving back towards the right, and a dashed red curve that starts from the top left and curves downwards, connecting with the solid red curve at a point where it also intersects the blue line. (a) The infected branch for $c_4 > 0$.: chart::>

<a id='a144df79-356f-4f7d-9c9f-6176e1d6ceec'></a>

<::chart: Two plots arranged side-by-side. Both plots share the x-axis label 'ϵ' and the y-axis label 'Z'. Each plot displays a blue line, a solid red curve, and a dashed-dotted red curve. The red curves originate from the point (0,0).

(b) The infected branch for c_4 < 0, c_6 < 0. In this plot, the blue line starts high on the left and slopes downwards to the right. The solid red curve forms a 'C' shape opening to the left, starting from the origin and extending upwards and then curving back down. The dashed-dotted red curve is above the solid red curve, following a similar 'C' shape but extending further to the left at its peak. Both red curves intersect the blue line.

(c) The infected branch for c_4 < 0, c_6 > 0. In this plot, the blue line also starts high on the left and slopes downwards to the right. The solid red curve forms a 'C' shape opening to the left, starting from the origin. The dashed-dotted red curve is below the solid red curve, following a similar 'C' shape but extending less far to the left at its peak. Both red curves intersect the blue line.

Figure 5. The pure infection (blue) and infected (red) steady state branches. Note that the dashed-dotted lines indicate invalid solutions.::>

<a id='94d502f0-40f4-4ee4-bf76-4240a086f7bf'></a>

Proof. Substituting for D using (40) into (46), we obtain an equation involving z and ε to be solved for the infected branch of solutions given by:

g(z,ε) = BCR(B + C)(1 – αε)²z² + (BCP(1 + R) + (B + C)(CR – B(1 – αε)))(1 – αε)z

+ εP(1 + R)((B + C)(1 – αε) + αC) = 0 (62)

<!-- PAGE BREAK -->

<a id='39f8dd2b-62f8-434f-965c-d13f2c3fd384'></a>

Viruses 2018, 10, 195

<a id='8fef449f-e8ff-4b01-b93c-f2645698bca9'></a>

24 of 41

<a id='10a3dd25-cda9-41ae-8349-00418cf2b8a3'></a>

To find limit points on the infected steady state branch [21], we must solve the two equations:
g(z,€) = gz(z,€) = 0

<a id='a371e4e2-b0a8-4067-bd19-c13568c88460'></a>

and check the non-degeneracy conditions:

$g_{zz}(z,\epsilon) \neq 0, g_{\epsilon}(z,\epsilon) \neq 0 \quad (63)$

<a id='bf70ed77-ffc1-436b-a045-6f49064d51ce'></a>

Since g(z, \epsilon) is quadratic in z, then clearly, g_z(z, \epsilon) is linear in z, and the z coefficient is strictly positive. Thus, the second equation can be solved for z and substituted back into the first equation, which gives the quadratic equation in \epsilon:

A_1\epsilon^2 + B_1\epsilon + C_1 = 0 (64)

<a id='50a5f6c8-6f10-4ba9-8aa9-87132aae6aad'></a>

where:

A₁ = -αB(B + C)²(4CPR(1 + R) + αB)
B₁ = CP(1 + R)(2R(B + (1 + α)C) - αB) + α(B + C)(B - CR)
C₁ = -((B + C)(B - CR) - BCP(1 + R))²

<a id='c86ae654-3c3b-4490-97df-c491ac18fcaa'></a>

The discriminant of the quadratic is given by:

Δ = 16BC²PR(1 + R)(B + C)²Δ₁Δ₂ (65)

<a id='d1933f41-9a02-4c91-a405-6c3d36cbfd64'></a>

where:
Δ₁ = BP(1 + R) + α(B – CR) (66)
Δ₂ = (B + C)(αB + R(B + C)) – αBCP(1 + R) (67)

<a id='0230a484-45c3-472f-b1e4-ddc9332fde03'></a>

We have assumed that (39) holds, and this implies (41) also; this gives Δ1 > 0. We also note that
Δ2 can be expressed as:

<a id='9a327329-ef2c-4c7c-9c3e-b02911886e06'></a>

$$\Delta_2 = ((B + C)^2 - \alpha BCP)R + \alpha B(B + C - CP)$$

<a id='dc5205c3-9e1e-4019-916e-3bc26d59d627'></a>

Assumption (39) implies that (42) holds, which implies that the second term is positive. Moreover,

$(B+C)^2 - \alpha BCP > (B+C)CP - \alpha BCP \text{ using (42)}$

$= CP(B(1-\alpha) + C)$

$> 0$

<a id='97a76e5d-8323-4524-ab00-676152c0800a'></a>

using (37), and this implies that Δ₂ > 0 also. Therefore, Δ > 0, and so, the quadratic Equation (64)
will have two distinct solutions. We therefore expect to have two limit points on the infected
solution branch(es). Now, gzz (z,ε) = 2BCR(B + C)(1 – αε)² > 0 using (37), (38), and so,
the first non-degeneracy condition in (63) is satisfied. However, it is not easy to verify the second
non-degeneracy condition. We now use a different approach to get further information regarding the
infected solution branches, which will also confirm the existence of two limit points.
To get a more complete picture of the solutions, we substitute:

<a id='1372ce06-fccd-4467-875e-f60863c0a713'></a>

z = z0 + z1 + δz / ε1 + δε'           ε = ε0 + ε1 + δε                                      (68)

<!-- PAGE BREAK -->

<a id='1d80515c-a301-46c4-b9af-4f85c5aacf09'></a>

Viruses 2018, 10, 195

<a id='87f11f5b-20b2-4e78-a742-788cb8cdc9d6'></a>

25 of 41

<a id='853217c6-e54f-4f74-9704-5b988ed5a502'></a>

into (62). The parameters $z_0$, $z_1$, $\tilde{\epsilon}_0$ and $\tilde{\epsilon}_1$ can be solved for in terms of the parameters so that our equation reduces to:

$\frac{h_1 \delta \epsilon^2}{h_0} - \frac{h_2 \delta z^2}{h_0} = 1$ (69)

<a id='9d8ca167-e75c-42c2-abe8-8e12cec65906'></a>

where:

z₀ = 1 / (2CR')

z₁ = (BP(1 + R) + R(B + C)) / (2αBR(B + C))

ε₀ = 1 / α

ε₁ = - C[αR(B + C) + P(1 + R)(2R(B + C(1 - α)) + αB)] / (α(B + C)(αB + 4CPR(1 + R)))

h₀ = (P(1 + R)Δ₁Δ₂) / (4BRh₁)

h₁ = (α(B + C)(αB + 4CPR(1 + R))) / (4CR)

h₂ = α²BCR(B + C)

<a id='63953003-7b75-42b9-8ebb-e61e47a31bb3'></a>

Clearly, $h_1, h_2 > 0$, and we showed above that $\Delta_1, \Delta_2 > 0$; so, $h_0 > 0$ also. Thus, (69) is the equation of a hyperbola, and the two solution branches are given in parametric form by:

$\delta z(\beta) = \sqrt{\frac{h_0}{h_2}} \sinh \beta, \quad \delta \epsilon(\beta) = \pm \sqrt{\frac{h_0}{h_1}} \cosh \beta$

<a id='8e13c4a5-3b67-4cf0-a165-13589e842427'></a>

These solutions exist for all $\delta z$ and for $|\delta \epsilon| \ge \sqrt{h_0/h_1}$. This gives rise to parametric solutions of (62) given by:

$z(\beta) = z_0 + \frac{z_1 + \delta z(\beta)}{\tilde{\epsilon}_1 + \delta \epsilon(\beta)}$

$\epsilon(\beta) = \tilde{\epsilon}_0 + \tilde{\epsilon}_1 + \delta \epsilon(\beta)$ (70)

<a id='3cbdc762-aaa5-4517-a1bb-fea07b01d73b'></a>

Limit points on these branches occur when:

$$\frac{d\epsilon}{dz} = \frac{d\epsilon/d\beta}{dz/d\beta} = 0$$

<a id='81f3470c-d729-4240-aca9-93e206938fdf'></a>

Now, β = 0 is the unique solution of the equation dε/dβ = 0 and:

$$\frac{dz}{d\beta}\Big|_{\beta=0} = \frac{\sqrt{h_0/h_2}}{\tilde{\epsilon}_1 \pm \sqrt{h_0/h_1}}$$

<a id='98206dbe-9fd1-46d5-b873-2b82598a705f'></a>

For this derivative to be finite, we clearly require ε₁ ± √(h₀/h₁) ≠ 0. Now, ε₁ < 0, and so,
ε₁ - √(h₀/h₁) < 0; however, it is possible that ε₁ + √(h₀/h₁) = 0. However, we will show later that the
right-hand (+) branch is outside our range of interest, and so, it does not matter whether this quantity
is zero or non-zero. Thus, on the left-hand (-) branch, we have:

dz
---
dβ | β=0 = √(h₀/h₂)

---

ε₁ - √(h₀/h₁) ≠ 0

<a id='db9db8fc-2be8-4902-befd-84ec8726d76a'></a>

and so, dε/dz = 0 when β = 0. This point will be a quadratic limit point provided that the non-degeneracy condition d²ε/dz²|β=0 ≠ 0 is satisfied. It is a matter of calculation to show that for the left-hand branch:

$\frac{d^2\epsilon}{dz^2}|_{\beta=0} = \frac{d^2\epsilon/d\beta^2}{(dz/d\beta)^2}|_{\beta=0} = -\sqrt{\frac{h_2}{h_0h_1}}(\tilde{\epsilon}_1 - \sqrt{h_0/h_1})^2 \neq 0$

<a id='dff9b40b-166d-4da4-b5b5-06ee2177a150'></a>

again using the fact that $\tilde{e}_1 - \sqrt{h_0/h_1} < 0$, and so, we do indeed have a quadratic limit point when $\beta = 0$. Thus, the limit point on the left-hand branch of solutions occurs at:

<a id='37cb4290-49de-461a-933a-9f3d9139ec6f'></a>

z(0) = z_0 + \frac{z_1}{\tilde{\epsilon}_1 - \sqrt{h_0/h_1}},

\epsilon(0) = \tilde{\epsilon}_0 + \tilde{\epsilon}_1 - \sqrt{h_0/h_1}

<!-- PAGE BREAK -->

<a id='72cecf83-704f-411a-a6e4-5ec54ba99fd3'></a>

Viruses 2018, 10, 195

<a id='9d603099-e01a-4b8c-8cde-67b69e00ad30'></a>

26 of 41

<a id='5e978c6c-8812-411d-a86a-8679b1138d0b'></a>

and two solutions exist for each ε < (0), which is also confirmed by the negative second derivative.
We note that there are no solutions of (69) when δε = 0, and this corresponds to ε = ε₀ + ε₁.
We now show that ε₂ < ε₀ + ε₁ < 1/α. The right-hand inequality is clearly satisfied since ε̃₀ = 1/α
and ε₁ < 0. To verify the left-hand inequality, we consider the quadratic equation (55). We have already
shown in the proof of Lemma 3 that the two solutions ε₂ and ε₃ of this equation satisfy ε₂ < 1 < ε₃.
Since the coefficient of ε² is negative, this implies that the quadratic function p(ε) is positive if and only
if ε₂ < ε < ε₃. If p(ε̃₀ + ε₁) > 0, then this implies that ε₂ < ε₀ + ε₁ as required. It can be shown that:

<a id='112ffeed-d0e6-4786-a918-57582583c8c3'></a>

p(ẽ₀ + ẽ₁) = BPC(a₃P³ + a₂P² + a₁P + a₀) / (α(B+C)²(αB + 4CPR(1+R))²) (71)

<a id='501cc3eb-61c8-4275-87c2-e68f0387007f'></a>

where $a_0, a_1, a_3 > 0$, using (37) and (41). The remaining coefficient, $a_2$, is given by:

$a_2 = C(1+R)^2(b_2B^2 + b_1B+b_0)$

<a id='50efcfb4-4888-404c-80b5-8bbaabbc2d4d'></a>

where b~0~, b~1~ > 0 and:
b~2~ = (8α^2 - 8α + 4)R^2 + 4α^2R - α^2

<a id='6639fb5c-ede0-42b9-9cb2-00c7d46103ed'></a>

Now, b₂ is negative for a > 0 and sufficiently small R. Substituting R = (√2-1)/2 + Ř into b₂ gives:

<a id='3fc8b585-bb3e-4aa2-85f4-fe197e86ca95'></a>

b₂ = (8α² - 8α + 4) R̃² + \frac{4(2√2 - 1)}{7} (7α² + (2√2 - 6)α + 3 - √2) R̃ + (3 - 2√2)(1 - α)²

<a id='2f76f2cf-1746-4d8e-8dae-6b5fc05e0228'></a>

The first and second order coefficients of R̃ are positive, and the constant coefficient is non-negative for all α ∈ [0, 1]. Thus, b2 > 0 for R̃ > 0 and for all α ∈ [0, 1], or equivalently, for all R > (√2 − 1)/2. In this case, a2 > 0 also, which then implies that p(ẽ0 + ẽ1) > 0, as required.

<a id='be04a186-d29a-47e4-b70b-f31e1a95d144'></a>

Thus, we have proved that $p(\tilde{e}_0 + \tilde{e}_1) > 0$ using Condition (61). However, even if $b_2 < 0$, there are still many other positive terms in $p(\tilde{e}_0 + \tilde{e}_1)$, and so, it may be the case that Condition (61) is not necessary. We note that the minimum of $b_2$ in the region $R \ge 0$, $\alpha \in [0,1]$ occurs at $R = 0$, $\alpha = 1$. Substituting $R = 0$, $\alpha = 1$ into the cubic polynomial in $P$ in (71) gives:

<a id='451a5050-83da-415f-81ec-31f82eea88bb'></a>

(a₃P³ + a₂P² + a₁P + a₀)|R=0,α=1 = B²(1 + P)(B + C - CP)

<a id='eb363cbc-4125-4541-9b88-094b4da6d244'></a>

Using assumption (42), this is positive. Moreover, expanding the cubic polynomial in a Taylor series about the point (R,a) = (0,1), we find that the first order terms are positive, and so, for sufficiently small R > 0 and a < 1, the cubic polynomial in P will be positive. However, this does not guarantee that it is positive for all R > 0 and a ∈ [0, 1], although we conjecture that this is in fact the case.

<a id='f2694e32-ad56-4db4-91dc-1d9645b4175f'></a>

Now, the two branches of solutions (70) occur on either side of the gap in ẽ, and so, one branch exists for ẽ < ẽ₀ + ẽ₁ and the other for ẽ > ẽ₀ + ẽ₁. The left-hand branch is therefore the only branch of infected solutions for ẽ < ẽ₀ + ẽ₁, and so, the two bifurcating branches of infected solutions arising from the two bifurcations described above must be part of this single branch.

<a id='dcdea629-783a-49c9-b9a7-4c4f3a07df20'></a>

Thus, there is a single branch of infected solutions that connects the two bifurcation points, as claimed. There must also be a limit point on this branch, which occurs for \(\epsilon > \epsilon_2\).

<a id='675ba3e7-b9af-4278-b2d5-e0748844e73d'></a>

The only steady state solutions with x = 0 are the uninfected or pure infection solutions. Thus, all other solutions, in particular the infected solutions, have x ≠ 0. In the case of c4 > 0 (Figure 4 (top)), the only way that the valid infected branches arising from the two bifurcations can connect on a curve with a single limit point is for the limit point to occur on the invalid solutions after the bifurcation on the pure infection branch, as shown in Figure 5a. When c4 < 0 (Figure 4 (middle, bottom)), the valid infected solution emanates from the pure infection branch to the right of the bifurcation point, and the only way that this can connect to the bifurcation on the uninfected branch at e = 0 is for there to be a limit point in between the two bifurcations.

<!-- PAGE BREAK -->

<a id='d03331b1-9031-4877-b4d7-605858decd0f'></a>

Viruses 2018, 10, 195

<a id='537e0b6f-2a4c-4aa1-8161-cb572fd101d5'></a>

27 of 41

<a id='f1caea10-1dea-4c65-9fe9-758e982adaa7'></a>

We note that the left branch of (69) exists for all δz, but does not exist for all z. As δɛ → −∞
(β → ±∞), the left branch of the hyperbola asymptotes to the straight lines δz = ±√h₁/h₂ δɛ.
Substituting these into z(β) given by (70), we see that z converges to the constant values:

<a id='e82a162f-6ba7-46c9-8e0f-c347415e8d3f'></a>

<::z = z₀ ± √(h₁/h₂) = (1 / 2CR) * (1 ± √(1 + 4CPR(1 + R) / (αB)))
: equation::>

<a id='1ec3d0d4-dca6-4a37-9f5d-3cb4a9e7791a'></a>

as e → -∞. Clearly one of these asymptotes is negative and the other positive, as we would expect. ☐

<a id='a40606bd-d6b8-49fb-a23a-d3db0a60a82d'></a>

Finally, we recall the assumption we made in Theorem 4 that D is defined by (40). If this is not the case, then the same method described above can be used to derive Equation (69), and z0, ε0, h1 and h2 are unchanged. However, the other coefficients now involve the parameter D. In this case, it is not possible to determine the sign of the coefficient h0 in (69). As long as h0 remains positive, the same picture as described above will hold qualitatively. However, if h0 changes sign and becomes negative, then the structure of the solutions of (69) changes, so that there are no limit points occurring. Therefore, if (40) does not hold, then there is an extra condition h0 > 0 that is required to give the same solution structure.

<a id='fd6a2cb4-4d21-4622-ad97-880c33201bba'></a>

**5.4. Steady States (S > 0)** We have studied in detail the solutions of our model in the special case when S = 0, which is when there is no production of hepatocytes from stem cells. When S is small and positive, this will result in a small perturbation of these solutions, and we now consider this case.

<a id='164280ff-6db6-40b1-aff0-62b1542b21f1'></a>

5.4.1. Bifurcation on the Uninfected Branch

When S > 0, the uninfected steady state (43) and the bifurcation point that is found by solving (48) between the uninfected and infected steady state branches both remain the same. Therefore, the condition (40) again ensures that this bifurcation point occurs at ε = 0.

<a id='0b7872e7-3050-4ecc-8461-5528b8143b36'></a>

5.4.2. Bifurcation on the Pure Infection Branch

When S > 0, the state of pure infection no longer exists since there is a second mechanism for generating healthy hepatocytes due to stem cell production. Thus, for small values of S, the bifurcation involving the infected and pure infection branches will unfold. There are two possible ways that a transcritical bifurcation can unfold, depending on the sign of the perturbation term.
When S > 0, the bifurcation equation (60) in x simply gains an extra term Sy where y is given by (58) and so is given by:

<a id='44e6579a-8acc-4002-a536-053a8fe7ad0d'></a>

h(x, δε) = S(y_p + O(x, x², xδε)) + c_3xδε + c_4x² + xO(x, δε) (72)

<a id='5df43f37-8dc3-490b-b26d-25eaaeccc714'></a>

where $\delta\epsilon = \epsilon - \epsilon_2$. The constant term is the only term needed to determine the unfolding of a transcritical bifurcation [21]. Limit points for this equation are found by solving $h(x, \delta\epsilon) = h_x(x, \delta\epsilon) = 0$ and are then given by:

$x^2 = \frac{Sy_p}{c_4} + O(S^2)$

<a id='642b9212-9642-4441-99c9-dca7022f1503'></a>

Since S > 0, we see that for sufficiently small S:

<!-- PAGE BREAK -->

<a id='29bd3258-2587-42df-b790-2c58f76892fd'></a>

Viruses 2018, 10, 195

<a id='33ffeb11-1242-42e5-8ba8-dcc187c5a895'></a>

28 of 41

<a id='f3077fde-546c-4c13-ada4-3d727d317eed'></a>

if c4 < 0, then no limit points exist;
if c4 > 0, then there are two limit points at x =  \u221a Syp/c4.

<a id='90bc68f9-5fce-4da4-b241-14c670870045'></a>

We recall that c3 > 0, and so, the sign of c4 also determines the slope of the bifurcating branch (see Figure 4). The unfolding of the bifurcation in these two cases is shown in Figure 6. We note that when S > 0, in both cases, one of the branches locally has x < 0, and one has x > 0; so, there is only one valid branch of solutions.

<a id='da824700-c585-4847-81a4-58dec98ef2de'></a>

When 𝜀₂ > 0, the unfolding of the solutions in Figure 5 is shown in Figure 7. <::chart: The figure presents four bifurcation diagrams arranged in a 2x2 grid, illustrating the unfolding of a transcritical bifurcation. The top row corresponds to 𝑐₄ > 0, and the bottom row corresponds to 𝑐₄ < 0. In the top-left plot (S = 0, for 𝑐₄ > 0), a straight horizontal line intersects a straight diagonal line. In the top-right plot (S > 0, for 𝑐₄ > 0), two curved lines, resembling an unfolding pitchfork or cusp, are shown, where solutions appear to emerge from a turning point. In the bottom-left plot (S = 0, for 𝑐₄ < 0), a straight horizontal line intersects a straight diagonal line, similar to the top-left. In the bottom-right plot (S > 0, for 𝑐₄ < 0), two curved lines, resembling an unfolding saddle-node bifurcation, are shown, diverging from a central region. Figure 6. Unfolding of the transcritical bifurcation given by (72) in the (𝜀,𝑥) plane for 𝑐₄ > 0 (top) and 𝑐₄ < 0 (bottom).::>

<a id='bbb55806-3221-40e3-8e81-7a12b6f63ba4'></a>

5.4.3. Infected Branch of Solutions

For the infected solution branch away from the bifurcation points, the implicit function theorem implies that a small perturbation in the equations due to S > 0 results in an O(S) perturbation in the infected solutions, and so, there is only a small perturbation in this branch of solutions. Thus, we see that in all cases, the form of the infected steady states is qualitatively similar since the branch of infected states emanates from the trivial solution at the bifurcation point at e = 0 and increases with e, goes round a limit point and then decreases, as shown in Figure 7. Moreover, this is the only valid branch of infected steady state solutions.

<!-- PAGE BREAK -->

<a id='66eeb76e-214f-4c9f-b402-ca1e97706de4'></a>

Viruses 2018, 10, 195

<a id='d1d29d96-8751-4ed0-be21-86686c932e14'></a>

29 of 41

<a id='b273bca4-c4c5-4d37-bbb3-de6a973c7b79'></a>

<::chart: The chart shows a 2D plot with 'Z' on the y-axis and 'ε' on the x-axis, starting from 0. There are two curves plotted in blue. One curve is a solid line, starting near (0,0), increasing in Z, then bending back towards lower ε values before turning and increasing in Z again. The other curve is a dashed line, starting at a higher Z value on the left, decreasing as ε increases, and interacting with the solid curve. The solid and dashed lines appear to merge or connect at certain points, forming a characteristic S-shaped or C-shaped bifurcation diagram. (a) Steady state solutions for c₄ > 0.::>

<a id='a6256a8d-27a1-481d-8cf2-89dee00345ad'></a>

<::figure: Two plots are displayed side-by-side. Both plots show steady state solutions with 'Z' on the y-axis and 'ε' on the x-axis, starting from 0 at the origin.

(b) Steady state solutions for c₄ < 0, c₆ < 0. The left plot features a solid blue curve that originates from (0,0), rises, then curves back towards the right, forming a C-like shape. A dashed blue curve starts higher on the left, descends, intersects the solid curve, and continues downwards to the right.

(c) Steady state solutions for c₄ < 0, c₆ > 0. The right plot also features a solid blue curve that originates from (0,0), rises, then curves significantly back towards the left and then right, creating an S-like shape that crosses the dashed curve. A dashed blue curve starts higher on the left, descends, intersects the solid curve, and continues downwards to the right.::>

<a id='a317d4a8-6388-4b2f-accb-c236d188ffd5'></a>

Figure 7. Steady state solutions where the bifurcation between the infected and pure infection branches has been unfolded as S > 0, assuming that $\epsilon_2 > 0$. The dashed-dotted lines are invalid solutions as $x < 0$.

<a id='a1714f2c-1e15-4510-9816-7ba58c134949'></a>

5.4.4. The Case of €2 < 0

Finally, we consider one more situation, namely when condition (56) does not hold. Thus, we now assume that:

BP-CD(1+R)(1+D(1+R)) < 0 (73)

<a id='e30c104d-9f26-4bf1-801b-6ac089bf8115'></a>

This implies that ε₂ < 0 by Lemma 3. and so, the bifurcation point on the pure infection branch with _S_ = 0 occurs for negative ε. The infected branch of solutions still has a limit point in this case, but there is no connection between these two branches in our range of interest given by ε ∈ [0,1). Moreover, the pure infection steady state with no treatment (ε = 0) is unstable, since Condition (56) was required to ensure stability. In this case, the unfolding of the bifurcation when _S_ > 0 occurs in the same way, but outside our range of interest, and the pure infection branch becomes invalid. The solutions in this case are shown in Figure 8. We note that the valid solution branch is similar in this case as in the previous cases considered, with a single limit point occurring.

<!-- PAGE BREAK -->

<a id='1a38dc31-e549-47ee-acb4-a1bec13aa072'></a>

Viruses 2018, 10, 195

<a id='93269b66-ba64-40cc-a817-5cbde3c6544a'></a>

30 of 41

<a id='31c6438b-19c9-4628-9acc-f90c4292a9e5'></a>

<::chart: A 2D plot with epsilon (ϵ) on the x-axis and Z on the y-axis. The origin is marked as 0. There are two curves plotted: a solid blue curve that starts at the origin, curves upwards and then downwards, resembling a parabola opening to the right; and a dashed-dotted blue line that starts at a higher Z value on the left and slopes downwards linearly to the right. The dashed-dotted line intersects the solid blue curve. Figure 8. The steady state solutions when (73) holds and S > 0. The dashed-dotted line consists of invalid solutions as *x* < 0.::>

<a id='d2af2ab5-7791-4d38-8656-88d5b11070f5'></a>

## 6. Stability

All the cases considered above, with Assumptions (39) and (40), give rise, when S > 0, to an uninfected steady state branch x = 1, y = z = 0 together with a branch of infected steady state solutions that bifurcates from \u03f5 = 0 and has a single limit point. We have also seen that the uninfected branch of solutions is stable for \u03f5 \u2208 (0,1), and this implies that the bifurcating branch of infected solutions initially has one unstable eigenvalue together with two stable eigenvalues. The only way that the infected branch can become stable again is if the unstable eigenvalue passes back through zero, which would correspond to a limit point. We have also ascertained that there is precisely one limit point on the branch of infected solutions (for sufficiently small S). Since the solutions past the limit point are stable when S = 0, they will still be stable for small S > 0, and so, the one unstable eigenvalue must pass through zero at the limit point to give a stable branch of solutions. Thus, the bifurcation diagram for S > 0 (and sufficiently small) is as shown in Figure 9a.

<a id='292134ef-d0c0-4730-a08d-88637c4a274f'></a>

<:: Two bifurcation diagrams are presented side-by-side. Both diagrams show a curve with solid blue lines indicating stable solutions and dashed blue lines indicating unstable solutions. The x-axis for both plots is labeled "ε" and includes a point labeled "ε_LP".

(a) The left diagram has a vertical axis labeled "Z". The curve starts near the origin, with a solid line extending upwards and to the right, then turning back downwards. A dashed line branches off from the upper part of this curve, extending further upwards and to the right. There is also a solid horizontal line near the bottom of the plot.

(b) The right diagram has a vertical axis labeled "log₁₀ Z". The curve's shape is similar to (a), but with the logarithmic y-axis. A solid line extends upwards and to the right, then turns back downwards. A dashed line branches off from the upper part of this curve, extending further upwards and to the right.

Figure 9. The bifurcation diagram, where solid lines indicate stable solutions and dashed lines indicate unstable solutions. Note that the vertical scale is either (a) z or (b) log₁₀ z.
: chart::>

<a id='5b7895fb-83ff-49b5-853b-10b9c61c3735'></a>

The other possibility is that the two stable eigenvalues along the unstable section of the infected branch could collide and become complex and then cross the imaginary axis in a Hopf bifurcation. They would then have to cross back again in a reverse Hopf bifurcation before the limit point in order for the solution to stabilise after going round the limit point. However, to determine whether or not

<!-- PAGE BREAK -->

<a id='84aef6ac-c15c-4a6d-8b0b-dd58f9771504'></a>

Viruses 2018, 10, 195

<a id='56f5d241-ad42-4c98-bd8b-210d6ebf4b99'></a>

31 of 41

<a id='8feb3b12-8dac-432f-8d27-71867fce7cda'></a>

such Hopf bifurcations occur analytically from the model is a very challenging problem. It is also of little interest, since any bifurcating periodic orbits would be unstable.

<a id='c4aa8bf9-52da-421e-a308-681d27b6577a'></a>

7. Comparison with the Neumann/Dahari Models
We now compare the predictions from our new model of HCV infection with those of the Neumann and Dahari models that we reviewed in Section 2. Our model is similar to previous models in that it involves the three variables T, I and V. However, the steady state solutions, and therefore the dynamics, of the new model are quite different from previous models in several ways. These differences result in different predictions for the dynamics of the infection during treatment and suggest possible different treatment regimes.

<a id='1ea3189a-8583-4557-9950-0bc137c3efc6'></a>

A typical bifurcation diagram for the Neumann/Dahari models is shown in Figure 10a, which we compare with the bifurcation diagram for our model, as shown in Figure 9a. We also note that experimental data are plotted with log10 V on the vertical axis rather than V, and so, we also show the bifurcation diagrams plotted for log10 z in Figures 9b and 10b. We also note from (26) that log10 V = log10 z + k where k = log10(rTTmax/(rT + d)), and so, the non-dimensionalisation only results in a shift on the vertical axis.

<a id='6efb3682-f379-4df7-9f34-8ae29186dcb3'></a>

<::chart: The image displays a bifurcation diagram with two subplots, (a) and (b). Both subplots share an x-axis labeled 'ϵ' starting from 0. Plot (a) shows 'z' on the y-axis. A solid blue line represents stable solutions, starting from a high value of z, decreasing, and then becoming horizontal at z=0. A dashed blue line represents unstable solutions, running along z=0 for a range of ϵ values before the solid line flattens. Plot (b) shows 'log₁₀ z' on the y-axis. A single solid blue curve is shown, starting from a high value, decreasing, and then sharply dropping vertically at a certain value of ϵ.::>

Figure 10. A typical bifurcation diagram for the Neumann/Dahari models, where solid lines indicate stable solutions and dashed lines indicate unstable solutions. Note that the vertical scale is either (a) z or (b) log₁₀ z.

<a id='0f0ad0cc-b733-41c2-bcdc-21532b123494'></a>

We now make a number of comparisons between these models.

* For the Neumann/Dahari models, treatment will only be effective once the treatment factor e exceeds a critical value determined by the bifurcation point, regardless of the viral load when treatment commences. For our model, if the viral load is close to the infected steady state before treatment starts, then similarly, the treatment factor e must exceed the critical value eLP determined by the limit point for the treatment to be effective. However, if the infection is caught and treated in the early stages, while the viral load is still relatively low, then our model predicts that a lower drug dose, with a corresponding smaller value of the treatment parameter e, will be effective.
* As mentioned previously, once treatment is stopped, the prediction of the Neumann/Dahari models is that the infection will take hold again unless the infected hepatocytes and virus have been completed eliminated during treatment. The prediction from our model, if the bifurcation point on the uninfected solution branch occurs at a negative value of e (e0 < 0), is that the body will be able to eliminate a small amount of infected hepatocytes and virus cells without further

<!-- PAGE BREAK -->

<a id='cf3da0fe-18ce-4a96-8ce3-9e4864f30fbe'></a>

Viruses 2018, 10, 195

<a id='3fb2f60d-2583-414a-9a7a-adaf2399c904'></a>

32 of 41

<a id='b88be25b-7f01-43fd-8bc3-ec7d37304a97'></a>

treatment once their levels have been reduced sufficiently. On the other hand, if the bifurcation point on the uninfected branch occurs at a positive value of € (€0 > 0), then our model predicts in this case that the infection will take hold again on cessation of treatment unless the infected hepatocytes and virus cells have been completely eliminated during treatment. However, our model also predicts that continuing with a low level of drug treatment, corresponding to a small value of €, will stop the infection recurring in this case.

<a id='3f91231b-4320-4fe6-ab83-5ab8c1c70529'></a>

* The Neumann/Dahari models suggest that treatment will only be effective if the treatment parameter \u03f5 is greater than the critical value during the whole period of treatment, which is the way that patients are generally treated in practice. Our model suggests that the drug dose could be reduced as treatment progresses and that this will still be effective, provided that it is not reduced too far too quickly. If this is indeed the case, it could save some of the costs of treatment, and a lower drug dosage may also mean a reduction in side effects, which would benefit the patient.

<a id='d2005727-47d7-499e-a521-db91c48e4431'></a>

## 8. Description of Observed Viral Load Profiles
The usual approach with a new model is to fit it to data in order to show that there are values of the model parameters that give a good fit to these data. This is a useful approach, but does not give any insight into the mechanisms involved in the different cases. Thus, we now consider many of the observed behaviours of the viral load under treatment that are reported in the literature and show how our model can explain these observations. This also helps to explain the possible mechanism associated with the observations in some cases. In the next section, we then fit our model to four datasets to show that this can also be done in practice.

<a id='a18df2dc-6153-4d50-8037-9871ee7f81e4'></a>

A number of different viral load profiles were reported in [5], and we first consider these. However,
we also consider various other observations in the literature. In this section, we define e* ∈ (0, 1) to be
the value of the treatment parameter in the model, which may of course vary for different patients.

<a id='adba2365-5d8d-4246-9b03-93dc579ff394'></a>

## 8.1. Sustained Virologic Response

Sustained virologic response is where the viral load rapidly decreases and is undetectable at the completion of treatment at 24 weeks [5]. For our model, this is easily realised by having εLP < ε* so that the trajectory in our model converges to the only available uninfected steady state, which is stable provided that ε0 < ε*. To see this rapid one phase decline, it is likely that treatment commenced not too long after infection, since a delay in treatment is often associated with biphasic or triphasic decline of the viral load (see Section 8.6). Once treatment is stopped, the viral load remains undetectable, and this will be the case provided that ε0 < 0, or equivalently BP < D(B+C) (see Lemma 1 and the discussion in Section 3.5).

<a id='61492093-775c-4254-8fe5-a9603494889d'></a>

8.2. Relapse

Relapse is similar to sustained virological response (SVR) during treatment, in that there is a rapid decline in viral load. However, once treatment stops, the patient relapses as the viral load increases back to pre-treatment levels. This relapse occurs if €0 > 0 as discussed in Section 3.5. In this case, continuing with a lower drug dose may be sufficient to keep the viral load under control.

<a id='d62f23ed-a7c8-473c-82e9-ae66feee4634'></a>

8.3. Partial Virologic Response

There is a partial virologic response (PVR) if an initial decrease in viral load is followed by an increase during treatment. This could be explained by our model if e* < ̈_LP and with the viral load quite high before the start of treatment. In this case, the trajectory of the model would converge to the infected steady state at e*, and it is quite possible that it could initially overshoot this steady state and then return back to it.

<!-- PAGE BREAK -->

<a id='aab81033-a034-4f67-9720-f2169c2fba87'></a>

Viruses 2018, 10, 195

<a id='fd5e889d-25d1-4d46-bd05-7fd36637cc30'></a>

33 of 41

<a id='c8fd9279-8d2c-46c8-bcb8-3febfef10a83'></a>

## 8.4. Breakthrough

Breakthrough is similar to PVR, except that at some point during treatment, the viral load is undetectable before increasing again during treatment. Thus, the mechanism would be similar to that described for PVR, but with the infected steady state occurring at a lower viral load, so that there is a larger initial drop in the viral load, below the level of detection, before increasing again back up to the infected steady state.

<a id='ba06d7f0-30d9-4dac-9e6d-b41ae9caad52'></a>

## 8.5. Null Response
Some patients show no significant reduction in viral load under treatment. This could occur when ε* < ε_LP and where the infected steady state at ε* is similar to that at ε = 0. This could occur when c_4 < 0 and c_6 > 0, as shown in Figure 7c.

<a id='ee4c0422-2d45-45db-b22b-a45de7e38c2c'></a>

## 8.6. Biphasic and Triphasic Decline
A common observation of the viral load during treatment is that there is biphasic decline [3], although triphasic decline, with a flat region between two declining phases, has also been observed [3,4]. We now show that both of these patterns of decline in the viral load under treatment can occur in our model.

<a id='d92508d8-3036-4845-be0e-fd84f8cdef29'></a>

We assume that S, the parameter associated with the generation of hepatocytes due to stem cells, is small (and positive). When there is no treatment (• = 0), the infected steady state is then given by:

<a id='9bc96f89-aef0-4470-8e38-9a175ec7c7d8'></a>

x = \frac{C}{BP - CD(1+R)(1+D(1+R))}^S + O(S^2)
y = y_p + O(S)
z = z_p(0) + O(S)

<a id='c9dffb3c-731c-407a-a392-8febf00a82d5'></a>

where $y_p$ and $z_p(0)$ are the pure infection steady states given by (44). We assume that (56) holds so that this solution is both valid (as $x > 0$) and stable.

<a id='302c4ca0-43b7-46c9-8ed4-c5eb277cf603'></a>

If we assume that a patient has been infected for a long time before treatment, then this implies that at the start of treatment, x(0), y(0) and z(0) will be close to these steady state values. We therefore now assume that x = O(S), and so, we set x = S\u0169. Substituting for x in (29)–(31) and taking only the leading order terms in S gives the reduced equations:

<a id='f160ffd3-5908-48ec-86d8-f59315c374fe'></a>

x̃' = y + x̃/y - x̃ - (1 - αε)B x̃z (74)
y' = 1/(1 + R)(1 - y) - Dy (75)
z' = (1 - ε)Py - Cz (76)

<a id='88c60477-1d3b-4426-9d38-a158ca783e76'></a>

We note that equation (75) is a linear equation in y with stable steady state y = yp. Since we are assuming that y(0) is close to this steady state, dynamically, y will continue to converge towards the steady state and is not influenced by either x or z.

<a id='46c5d795-5080-4091-8ce8-4d108f15d8fb'></a>

Equation (76) has the stable steady state z = z_p(\epsilon). Once treatment starts with \epsilon = \epsilon^*, this steady state drops from z_p(0) to z_p(\epsilon^*) = (1 - \epsilon^*)z_p(0). Since y is approximately constant, this implies at the start of treatment that z will decay exponentially towards the new steady state value. If we assume that y = y_p, then the solution of (76) is:

<a id='3a14d149-d991-4604-b1bc-43dc29646efc'></a>

z = z_p(ε*) + (z(0) - z_p(ε*))e^{-Ct}                                                                           (77)

<!-- PAGE BREAK -->

<a id='8ab7d017-3343-4994-bcf2-da13f5999d3b'></a>

Viruses 2018, 10, 195

<a id='eca8e79e-2d26-41c2-80de-eb7873e736bf'></a>

34 of 41

<a id='8df0d87c-c0fc-43a0-91ce-dce8509850ba'></a>

This is the observed first phase of rapid decline in the viral load. We note that Equation (74) can be written as:

x' = y + (x̃ / y) - x̃ - Bx̃z + (αBx̃z)ε

<a id='5560c429-dcd3-45a1-94f0-26b356881282'></a>

Thus, the effect of increasing \(\epsilon\) at the start of treatment is to increase \(\tilde{x}'\), and this will result in \(\tilde{x}\) increasing also.

<a id='3b1df131-5ab0-4c4d-8446-d3ac3787bfca'></a>

Once z has dropped to close to the steady state z_p( \epsilon^* ), and assuming that y is also close to y_p, then y' = O(S) and z' = O(S), and so, y and z evolve on a slow time scale. Thus, they will remain approximately constant for a time of O(1/S). This is the flat middle phase in the triphasic decline.

<a id='2a5ee51d-4040-49b0-bad3-16e9a0c14511'></a>

Eventually, the O(S) terms in the y and z equations will result in y and z being displaced from their leading order steady states, and the third phase decline towards the uninfected steady state will start. This rate of decline is determined by the eigenvalue of the Jacobian matrix evaluated at the uninfected steady state given in (47) that is closest to zero. Clearly, one eigenvalue is \lambda_1 = -1, and this is unlikely to be the closest to zero. The other two eigenvalues are found from the lower 2 \times 2 matrix. The characteristic equation, which has to be solved for these eigenvalues, is given by:

<a id='1dcc60ea-3fb0-475d-9887-a0db69e2964a'></a>

p(λ) = λ² + ((1 - αε)B + C + D)λ - BP(1 - ε)(1 - αε) + D((1 - αε)B + C) = 0 (78)

<a id='fddf8fac-987a-441b-bd00-f63e435ea282'></a>

Assuming that $\epsilon^{*}>\epsilon_{0}$ then the uninfected steady state is stable, and so, the two solutions of this characteristic equation are both negative. Suppose that these solutions are $-\lambda_{1}$ and $-\lambda_{0}$ with $-\lambda_{1}<-\lambda_{0}<0$. In this case, the rate of decline to the uninfected steady state is determined by the eigenvalue closest to zero, which is $-\lambda_{0}$. The third phase decline is generally observed to be slower than the first phase, and this will be the case if $C>\lambda_{0}$. Now, $p(\lambda)<0$ if and only if $-\lambda_{1}<\lambda<-\lambda_{0}$. Thus, if $p(-C)<0$, then this implies that $-C<-\lambda_{0}$ as required. Now:

<a id='b703e26c-9fea-4074-9310-629803dd1b59'></a>

p(-C) = -(1 - αε*)B(C + (1 - ε*)P - D)

<a id='65324959-91b8-40d7-9d41-d1488315e75a'></a>

Clearly, this is negative if C + (1 - \(\epsilon\))P > D, and so, this is the condition that ensures that the third phase decline is slower than the first phase.

<a id='c7ef1bd4-50d5-424e-8b4e-e0a4318f2ad6'></a>

Thus, we have shown that our new model can exhibit triphasic decline of the viral load, as is seen in the data. This analysis also suggests that this pattern of decline is associated with late commencement of treatment so that the initial conditions for the model are close to the infected steady state. This is also the conclusion reached by Dahari et al. [3].

<a id='77725bcb-a8d5-48d7-8f48-add608f19033'></a>

Biphasic decline is similar to triphasic decline, but where the middle flat phase is very short.
The first order term in S in Equations (75) and (76) is S(1 – αε*) Bîz, and so, anything that increases the magnitude of this term will reduce the length of the middle phase. This includes a larger value of S or B or a larger value of zp (€*). We note that an increase in B will also result in a more rapid increase in x, which will also help to shorten this phase. Thus, our model can also exhibit biphasic decline of the viral load.

<a id='e65fafd5-b547-4d3b-a211-88eb0d8c5d24'></a>

8.7. _Initial Increase in Viral Load_

Hsu et al. [22] reported that in some patients, there is an initial increase in viral load when treatment is started and that this initial increase is associated with a higher likelihood of achieving SVR. They used different models to investigate this behaviour and concluded that a modification of the Neumann model gave the best fit provided that c = δ and η = 1, which implies that the treatment always provides a complete block on de novo infection. Guedj et al. [23] questioned these unrealistic assumptions and the analysis in [22] and suggested that the initial increase in viral load was due to the infected steady state not having been reached so that viral loads were increasing before the start of therapy. They also suggested that the correlation between the initial increases and SVR was an indication of the effectiveness of the therapy. Rong and Perelson [24] also considered this effect in their multiscale model for direct acting antiviral agents. Their model always showed a small initial increase

<!-- PAGE BREAK -->

<a id='3565c0f0-964d-40d1-952c-61b23ec9fc07'></a>

Viruses 2018, 10, 195

<a id='f6c1b6a9-6445-4f38-a430-23d6ede7b0b5'></a>

35 of 41

<a id='80b09874-73bf-4ced-84a1-37dd0f7438cb'></a>

in viral load, even when starting from steady state. Of course, this result cannot be directly compared with the experimental results of Hsu et al. [22] since these results were obtained for patients treated with interferon (IFN) and ribavirin (RBV) only.
To understand this effect from our model, we express (31) as:

z' = Py - Cz - Bxz - ε(Py - αBxz) (79)

<a id='32dc10bc-13ea-4abd-8d15-5128c1cd9fd1'></a>

Without treatment (\epsilon=0), we expect z to be increasing towards the infected steady state, and so z'>0, which implies that:

Py-Cz-Bxz>0 (80)

We note that:

Py-\alpha Bxz=(Py-Cz-Bxz)+(Cz+(1-\alpha)Bxz)>0

<a id='5c44c671-4ce6-4c3d-b457-4f1f33171971'></a>

assuming that (80) holds and using (37).
If we assume that the infected steady state ($x_i, y_i, z_i$) has been reached before the start of treatment,
then at $t = 0$, we have:

$z'(0) = -\epsilon^*(Py_i - \alpha Bx_i z_i) = -\epsilon(Cz_i + (1-\alpha)Bxz)$

<a id='d2b0c917-0139-48e0-9922-297ed8a6e734'></a>

which is negative, and so, we have an immediate decline in viral load. However, if the steady state has not been reached before treatment commences, then with $(x, y, z) = (x(0), y(0), z(0))$ at the start of treatment, we have:

$z'(0) = Py(0) - Cz(0) - Bx(0)z(0) - \epsilon^*(Py(0) - aBx(0)z(0))$

<a id='d119d663-c300-483d-9d58-53399d3e7ce4'></a>

which is the difference of two positive terms, and so could be negative or positive. Larger values of e*
are more likely to give z' (0) < 0, and so, the effectiveness of treatment does not explain the correlation
between the initial increase and SVR, as suggested in [23]. We propose an alternative explanation for
this correlation.

<a id='7b782a81-e1e6-4550-a02c-cf95dbafece9'></a>

Soon after infection, the viral load will be increasing rapidly while y and z are both quite small, and so, the effect of the treatment will be small also, so that z'(0) > 0, thus giving an initial increase in viral load. However, if the start of treatment is delayed and the system is getting towards the infected steady state, then z'(0) will be quite small before treatment commences. However, near the steady state, Py(0) will be relatively large, so that the net effect gives z'(0) < 0 once treatment starts. Thus, according to this model, an initial increase in viral load is associated with early initiation of treatment, which is likely to correlate with a higher rate of SVR, as reported in [22].

<a id='0670819f-5373-4f48-9391-00eb0ac3861c'></a>

8.8. Direct Acting Antiviral Agents

Recently, new direct acting antiviral (DAA) agents have become available, which are more effective than treatment with IFN and RBV alone. If DAAs are used as a monotherapy, then it is found that drug-resistant virus cells quickly form, rendering the treatment ineffective; so, they are used in combination with IFN and RBV, and this combination is found to be highly effective [25]. More complex models for the action of DAAs have been proposed [26]. It has been found that treatment that includes DAAs has notable differences compared to treatment with only IFN and RBV, which include (i) a more rapid and longer first phase decline and (ii) a more rapid second phase decline [25].

<a id='7516ab87-7d0b-479a-ac9c-61b980e8bef5'></a>

We note that the action of a DAA is essentially to further block viral replication, although by different mechanisms than the older drugs [27]. The simplest way that this can be modelled is to increase the parameter ε in (31). If it is also assumed that the DAAs do not have any additional effect in reducing the rate of production of infected cells (parameter η in Equations (19)–(21)), then an increase in ε must be accompanied by a corresponding reduction in the parameter α given in (27), in order to

<!-- PAGE BREAK -->

<a id='1fdc9652-9ac4-46fe-97b3-570c44793257'></a>

Viruses 2018, 10, 195

<a id='666e200b-3361-4502-8fca-90475b772ff1'></a>

36 of 41

<a id='d2fa1ece-d38d-44e8-b44c-c13cb4aecd51'></a>

keep η = 1 – αε > 0 constant. We claim that this simple change is sufficient to explain both of the
above observed effects, which we now justify.

<a id='de144e25-0fac-43b5-bdbe-0af407625498'></a>

(i) It has been noted that the first phase decline when treating with DAAs is both longer and faster than when using IFN and RBV. Since the rate of the first phase decline is essentially given by the parameter C (or c for the original equations), it has been suggested that both e and c should be increased in the models for treatment with DAAs [25]. However, we claim that an increase in e alone is sufficient to produce a longer and faster first phase. To see this, we consider the decline in viral load during the first phase that is given in (77). For this solution, we find that the initial rate of decline is:

<a id='96bc9918-a555-4b25-b659-340abae9b9d8'></a>

d(log₁₀ z) / dτ |_(τ=0) = - (1 - z_p(ε*) / z_p(0)) C log₁₀ e
= -ε* C log₁₀ e

<a id='d96bfe5a-c689-4218-a404-386d3748eac3'></a>

since zp(e*) = (1 - e*)zp(0), and so, the initial slope increases as the treatment factor e* increases, with maximum slope only being achieved when e* = 1 (which corresponds to zp(e*) = 0). Clearly, the steady state zp(e*) is also reduced as e* is increased. These two effects result in an increase in the length of the decline in the viral load together with a more rapid decline. This is illustrated in Figure 11.

<a id='03ac82b0-d311-46fc-841e-a2c805293166'></a>

<::chart: line graph::>  Figure 11. The decline in viral load given by (77) with z_p(0) = 1, C = 1 and z_p(ε*) = 0.5 (blue) or z_p(ε*) = 0.2 (red). The x-axis is labeled 'τ' and ranges from 0 to 10. The y-axis is labeled 'log₁₀z' and ranges from -0.8 to 0. Two lines are plotted: a blue line starting at 0 and decreasing to approximately -0.3, representing z_p(ε*) = 0.5; and a red line starting at 0 and decreasing more steeply to approximately -0.7, representing z_p(ε*) = 0.2. Both lines show an initial decline followed by a plateau. <::/chart::>

<a id='a3baa14f-6d9d-4b0c-8c56-a5ffdacf9e1e'></a>

(ii) The second observation made for DAAs is that the second phase is also faster than that for treatment with IFN and RBV. We have seen in Section 8.6 that for our model, the rate of decay in the second phase is proportional to e<sup>-λ<sub>0</sub>t</sup> where -λ<sub>0</sub> < 0 is the solution of the characteristic equation (78) that is closest to zero. With our assumption that η = 1 - αε is constant, (78) becomes:
p(λ(ε)) = λ(ε)² + (ηB + C + D)λ(ε) - ηBP(1 - ε) + D(ηB + C) = 0 (81)

<a id='fdde7205-8920-4db3-bc68-334ab677e446'></a>

Differentiating this equation with respect to ε and solving for λ'(ε) gives:

λ'(ε) = -ηBP
        ──────────────
        (ηB + C + D + 2λ(ε))

and evaluating at ε = ε* gives:

λ'(ε*) = -ηBP
         ───────────────                                                                  (82)
         (ηB + C + D - 2λ₀)

<!-- PAGE BREAK -->

<a id='b67bc424-a41a-4ec8-8121-f19affcd9d72'></a>

Viruses 2018, 10, 195

<a id='2be0d3c6-cac1-44c4-9bd8-dafe5753a42f'></a>

37 of 41

<a id='84a8795b-9193-4024-a481-fcf061b55dc6'></a>

for λ(ε*) = -λ₀. The sign of the denominator is not clear. However, substituting λ = -(ηB + C+D)/2 into p(λ) given by (81) gives:
p \left( -\frac{1}{2}(\eta B+C+D) \right) = - \left( (1-\epsilon)\eta BP + \frac{1}{4}(\eta B + C - D)^2 \right) < 0

<a id='de1e6c67-8eed-4d95-9d03-00817860112e'></a>

using (38) and the assumption that η > 0. The quadratic coefficient of λ(ε) in (81) is positive, and so, p(λ(ε)) is only negative between the two roots −λ_1 and −λ_0, which implies that:

<a id='acca9c6c-7e9e-432a-a479-2619daa2da20'></a>

-λ₁ < -½(ηB + C + D) < -λ₀

<a id='01f7b36f-e126-4f8b-a321-252f5b38bb14'></a>

It follows from this that the denominator of (82) is positive, and so, λ'(e*) < 0. Hence, if e is increased from e*, then the eigenvalue –λ₀ will decrease to first order, thereby increasing the rate of the second phase decline.

<a id='822ac159-236f-4795-a2a5-3c2616a2f608'></a>

Thus, the observed effects of direct acting antiviral agents, in association with IFN and RBV, can be included in our model by simply keeping 1 - αε constant and reducing ε.

<a id='af3cccaa-a2df-48ed-94d4-ce5e451e851c'></a>

### 9. Data Fitting
We claimed in Section 8 that our new model is capable of generating many of the observed profiles of viral load under treatment. We now fit our model to some data in order to demonstrate that this is indeed the case.

<a id='996a6031-034c-45d3-9c34-0bff513b8cc6'></a>

For this data fitting, we use the model equations in dimensional form given by (19)–(21). We first note that it is not possible to fit all of the parameters in the model. In particular, the parameters η and β always occur in the combination (1 – η)β, and so, during treatment, we can only hope to determine this single quantity from the data. Similarly, ε and p occur in the combination (1 - ε)p, and so again, we can only determine this single quantity during treatment.

<a id='73ef3727-415c-4c27-83a2-8921ec1eb8de'></a>

We also observe that the five parameters $r_T$, $r_I$, $T_{max}$, $d$ and $\delta$ occur only in the four groups $r_T T_{max}$, $r_I T_{max}$, $r_T + d$, $r_I + \delta$, and so, it will not be possible to identify all five of these parameters from the data. Instead of using these four parameter groups, we use $r_T T_{max}$, $r_T + d$, $R$ and $D$, where $R$ and $D$ are non-dimensional parameters defined in (32). We write Equations (19)-(21) in terms of these parameters as:

<a id='effb26d0-0a79-4d2f-962b-e763a8715940'></a>

Ṫ = sI + r_T T_{max}T / (T+I) - (r_T + d)T - β*VT (83)
İ = 1 / (1+R) (r_T T_{max}I / (T+I) - (r_T + d)I) - D(r_T + d)I + β*VT (84)
V̇ = p*I - cV - β*VT (85)

<a id='0aed2401-a725-4999-a946-acf307904f79'></a>

where:

$\beta^* = (1 - \eta)\beta$, $p^* = (1 - \epsilon)p$

<a id='ca1b05d0-9241-4887-9241-9e746b54965c'></a>

Values of the parameter groups rTmax and rT + d will be found by fitting the model to data.
We note that by including the non-dimensional parameter R, and requiring it to be positive, ensures
that the conditions 0 < rI/rT < 1 are satisfied. Moreover, requiring D > 0 is consistent with the
conditions rI < rT and d < δ, but does not guarantee that they hold. We also note that it is not possible
to determine whether Condition (39) holds since the parameter β cannot be determined. The sign of
ε0, the value of ε at which the bifurcation on the uninfected branch occurs (see Lemma 1), cannot be
determined either since β and p cannot be determined.

<a id='903cc0df-7d01-4759-b1e2-92d3eb1b9a19'></a>

The initial value V(0) will be taken from the data and the other initial values, T(0) and I(0), will be regarded as unknown parameters. Thus, there is a total of 10 parameters and initial values to be found by fitting the model Equations (83)-(85) to the data, all of which are required to be positive.

<!-- PAGE BREAK -->

<a id='eb10628d-fd40-4429-9c6a-31ff7442e11c'></a>

Viruses 2018, 10, 195

<a id='061b19c3-2de3-4735-a6f6-4cef72cd1899'></a>

38 of 41

<a id='61eca59a-cd73-4bf5-94b3-28b80b376221'></a>

These parameters are found using the method of least squares in which the sum of the squares of the differences between the log of the viral load data points and the log of the viral load predicted by the model at the given time points is minimised. This task was performed using MATLAB with the differential equations described in terms of the log of each of the variables.

<a id='280b91e2-6df7-417f-be67-4455f584f377'></a>

We considered various datasets that show partial virologic response (PVR), breakthrough, null response and triphasic behaviour. The first three datasets are taken from [5], while the last one is taken from [6]. We fitted our model to the data during treatment only. The data together with the fitted curve V(t) and the predicted curves T(t) and I(t) from the model for each case are shown in Figure 12. The parameter values used are given in Table 1. These should not be regarded as definitive parameter values since very similar fits to the viral load data can be found using quite different sets of parameter values.

<a id='68a68f5d-dd09-47d0-ad73-331cc90b67aa'></a>

We did not consider data that shows sustained virologic response (SVR) since these datasets typically contain only two data points before the viral load goes below the lower limit of quantification (see [5]), and there will be many parameter combinations that will fit the two data points. The model can of course show this behaviour for appropriate parameter values.

<a id='978fd887-1bcc-413c-a818-3794f0857b93'></a>

For the breakthrough data, we note that the three lowest data points are recorded as 50 IU/mL, which is the lower limit of quantification, and so, the actual values of the viral load will be lower than this. However, we do not know the correct values of the viral load, and so, for the data fitting, we kept the outer two of these values, but ignored the middle value.

<a id='59edcfb1-4bd1-4fe5-b497-3362c93d3a30'></a>

Figure 12. <::chart: Four plots showing Concentrations (log10 IU/mL) versus Time (days). Each plot displays three lines representing viral load V (blue solid line with 'x' markers), healthy hepatocytes T (green dashed line), and infected hepatocytes I (red dashed line). All legends are consistent across the plots: "log10 T" (green dashed line), "log10 I" (red dashed line), and "log10 V" (blue solid line). The x-axis is labeled "Time (days)" and the y-axis is labeled "Concentrations (log10 IU/mL)". (a) Partial virologic response (PVR) plot: The viral load V starts high, decreases, then increases again. Healthy hepatocytes T increase. Infected hepatocytes I decrease then increase. The time axis ranges from 0 to 250 days. (b) Breakthrough plot: The viral load V starts high, decreases significantly, then increases again. Healthy hepatocytes T increase to a plateau. Infected hepatocytes I decrease then increase. The time axis ranges from 0 to 350 days. (c) Null response plot: The viral load V starts around 5.5, slightly decreases, then stabilizes around 5. Healthy hepatocytes T increase slightly to a plateau around 7. Infected hepatocytes I increase slightly to a plateau around 7. The time axis ranges from 0 to 350 days. (d) Triphasic plot: The viral load V starts high, decreases rapidly, then decreases more slowly. Healthy hepatocytes T start low and increase. Infected hepatocytes I start around 2.5 and decrease. The time axis ranges from 0 to 60 days.::> Plots of the viral load V (blue), healthy hepatocytes T (green) and infected hepatocytes I (red) against time fitted to the viral load datasets for (a) partial virologic response (PVR), (b) breakthrough, (c) null response, (d) triphasic.

<!-- PAGE BREAK -->

<a id='960b538e-77ac-47aa-b899-9076aa228da0'></a>

Viruses 2018, 10, 195

<a id='0c651d9e-9d8e-4467-aa18-5037abad6c11'></a>

39 of 41

<a id='24f027c4-952e-43f3-ac40-87116d7d316c'></a>

We now make a number of observations regarding these results.

* In the PVR, breakthrough and triphasic cases, we have I(t) < V(t) for all t, but in the null response case, I(t) is significantly higher than V(t).
* The initial viral load is highest in the PVR case, and we predicted in Section 8.3 that PVR would be associated with a high initial viral load.
* In the null response case, it is interesting to observe that the fitted viral load V and infected hepatocyte concentration I both reduce towards zero, but very slowly. The start of the decline in these variables can be observed from around 300 days in Figure 12c. At 1000 days after the start of treatment, the predicted values are log₁₀ I (1000) = 5.1202 and log₁₀ V(1000) = 2.8515.
* In Section 8.6, we stated that triphasic decline might be expected when the patient has been infected for a long time before treatment, which means that the viral load will be high while the healthy hepatocyte concentration will be very low. This is precisely the situation observed in Figure 12d.
* In Section 8.7, we showed that an initial increase in viral load at the start of treatment is possible, and we see this in the null response case.
* We saw in Section 3.1 that the regeneration rate for a healthy liver is 1.15 × 10⁻² day⁻¹ for females and 1.11 × 10⁻² day⁻¹ for males. This is effectively the parameter rₒ + d in our new model. The value of this parameter when fitted to data is a little lower than this for the PVR and breakthrough cases and is slightly higher in the null response and triphasic cases.
* The condition (33) for the solution to be bounded for all t ≥ 0 in terms of the parameters we are using here is given by:

<a id='b904a8c5-46f5-4339-bc7f-21d4d41ccafa'></a>

min(s, p*)(1+R) - (rT + d)(1 + D(1 + R)) < 0

<a id='f4de67ae-004e-4cb0-8ca6-c510c042bfbe'></a>

The term on the LHS for each of the fits to the data is given by: PVR: -0.1790; breakthrough: -2003; null response: -0.1753; triphasic: -0.2500. All of these values are negative, which ensures that each of the solutions exists and is bounded for all time by Theorem 3.

<a id='78e36a3d-ac90-4751-bae0-38fbe1e76d99'></a>

Table 1. Parameter values for fitting the model to the data.
<table id="38-1">
<tr><td id="38-2"></td><td id="38-3">PVR</td><td id="38-4">Breakthrough</td><td id="38-5">Null Response</td><td id="38-6">Triphasic</td></tr>
<tr><td id="38-7">s (day⁻¹)</td><td id="38-8">1.1178 × 10⁻¹</td><td id="38-9">1.5104 × 10⁻⁴</td><td id="38-a">4.6260 × 10⁻³</td><td id="38-b">3.1259 × 10⁻³</td></tr>
<tr><td id="38-c">rT Tmax (IU/ml/day)</td><td id="38-d">1.0645 × 10⁴</td><td id="38-e">2.8556 × 10⁴</td><td id="38-f">1.2920 × 10⁶</td><td id="38-g">1.1149 × 10²</td></tr>
<tr><td id="38-h">rT + d (day⁻¹)</td><td id="38-i">1.9927 × 10⁻³</td><td id="38-j">2.9890 × 10⁻³</td><td id="38-k">3.8518 × 10⁻²</td><td id="38-l">1.7882 × 10⁻²</td></tr>
<tr><td id="38-m">R</td><td id="38-n">3.0078 × 10¹</td><td id="38-o">1.1686 × 10³</td><td id="38-p">2.6011</td><td id="38-q">2.0350 × 10⁻¹</td></tr>
<tr><td id="38-r">D</td><td id="38-s">5.8954 × 101</td><td id="38-t">5.7302 × 102</td><td id="38-u">1.1064</td><td id="38-v">1.0962 × 101</td></tr>
<tr><td id="38-w">β* (ml/IU/day)</td><td id="38-x">8.3376 x 10-9</td><td id="38-y">7.1149 × 10-9</td><td id="38-z">1.9493 x 10-7</td><td id="38-A">3.3281 x 10-8</td></tr>
<tr><td id="38-B">p* (day -1)</td><td id="38-C">2.0396 × 102</td><td id="38-D">9.4025 × 10</td><td id="38-E">3.4868 x 10-2</td><td id="38-F">1.1646 × 103</td></tr>
<tr><td id="38-G">c (day -1)</td><td id="38-H">1.7908 × 101</td><td id="38-I">3.3659</td><td id="38-J">2.7784 × 10-4</td><td id="38-K">1.4294</td></tr>
<tr><td id="38-L">T(0) (IU/ml)</td><td id="38-M">3.3246</td><td id="38-N">8.2935 × 106</td><td id="38-O">1.7755 × 104</td><td id="38-P">1.9948</td></tr>
<tr><td id="38-Q">I(0) (IU/ml)</td><td id="38-R">4.1752 × 10⁵</td><td id="38-S">9.5880 × 10³</td><td id="38-T">1.4523 x 10⁶</td><td id="38-U">1.0355 x 10²</td></tr>
</table>

<a id='f0520623-bb06-4c42-9a09-f62eb4064ad1'></a>

10. Conclusions

We have proposed a new mathematical model of HCV infection, which involves the same three variables (concentrations of healthy and infected hepatocytes and of virions) as the earlier models of Neumann and Dahari, but which has a significantly different structure to the steady state solutions. The typical bifurcation diagram for our model is shown in Figure 9 and consists of an uninfected steady state branch with a bifurcating branch of infected steady state solutions on which there is a single limit point. Allowing the bifurcation point to occur at positive or negative values of the treatment parameter means that the model can include spontaneous clearance, as well as relapse at the end of

<!-- PAGE BREAK -->

<a id='252bc233-a67c-45a3-87e5-9ab091985d9b'></a>

Viruses 2018, 10, 195

<a id='899aec07-1a22-47bb-9c54-b2ab51624383'></a>

40 of 41

<a id='b8339398-e68a-4ba4-afc0-15a876929877'></a>

treatment. In the case S = 0 (no generation of hepatocytes from stem cells), we showed that there is a pure infection branch of solutions, and an infected steady state branch was found analytically that connects the uninfected and pure infection branches. When S > 0, the bifurcation between the pure infected and infected branches unfolds, generating a single valid branch of infected solutions on which there is a limit point (see Figure 7). We have been able to describe these solutions of the model using only the assumption (39) and the requirement that the quantity BP - D(B+C) is close to zero.

<a id='612a058e-c0df-45d1-a7f8-5faff8c9a716'></a>

We have shown in Section 8 that our model is able to show the many profiles of viral load reported in the literature, and the model has been fitted to four datasets in Section 9. Moreover, based on the bifurcation diagram shown in Figure 9 for our model, we also made some predictions regarding treatment (see Section 7), which we summarise as follows:

* If the infection is caught and treated in the early stages, then our model predicts that a lower drug dose may be effective in eliminating the infection.
* If the viral load relapses on cessation of treatment, then continuing with a low level of drug treatment may keep the viral load low.
* The infected branch from the bifurcation on the uninfected branch to the limit point has a positive slope, and this suggests that the drug dose could be reduced as treatment progresses, which could save some of the costs of treatment and give a reduction in side effects for the patient.

<a id='0b147d10-7ee0-4f56-b105-2eca1d9b318d'></a>

The Neumann HCV model was obtained by modifying earlier models for HBV and HIV infections.
It would now be interesting to see whether this process could be reversed by adapting this new model
for HCV infection for other viral infections.

<a id='ea77772c-ecde-4ce2-ad1a-42a73c2d36be'></a>

Another avenue of interest would be to fit this model to viral load data while a patient is on treatment in order to make patient-specific recommendations from the model regarding the future treatment plan. An important step in this process would be to determine the feasibility of estimating each of the parameters in the model, as has been done for other HCV models [28].

<a id='608c07df-5661-4ca6-ae14-50afaffceefb'></a>

**Acknowledgments:** I am grateful to many colleagues for helpful conversations regarding mathematical modelling of HCV infection, including Piet van der Graaf, Mark Ransley, Edwin Rwemigabo, Hien Tran, Tom Banks, Joseph Arthur, Aluisio Seguardo, Cássia Mendes Corrêa, João Renato Rebello Pinho and Bernadette Moore.

<a id='a1f0d9b9-00c4-4e49-9f8f-342f12096c4b'></a>

**Conflicts of Interest:** The author declares no conflict of interest.

<a id='816d4f8b-5f35-44bc-9567-6915377bc450'></a>

## References
1. World Health Organization. *Global Hepatitis Report 2017*; World Health Organization: Geneva, Switzerland, 2017. [CrossRef]
2. Neumann, A.U.; Lam, N.P.; Dahari, H.; Gretch, D.R.; Wiley, T.E.; Layden, T.J.; Perelson, A.S. Hepatitis C viral dynamics in vivo and the antiviral efficacy of interferon-α therapy. *Science 1998*, 282, 103–107. [CrossRef]
3. Dahari, H.; Lo, A.; Ribeiro, R.M.; Perelson, A.S. Modelling hepatitis C virus dynamics: Liver regeneration and critical drug efficacy. *J. Theor. Biol. 2007*, 247, 371–381. [CrossRef]
4. Dahari, H.; Ribeiro, R.M.; Perelson, A.S. Triphasic decline of hepatitis C virus RNA during antiviral therapy. *Hepatology 2007*, 46, 16–21. [CrossRef]
5. Snoeck, E.; Chanu, P.; Lavielle, M.; Jacqmin, P.; Jonsson, E.N.; Jorga, K.; Goggin, T.; Grippo, J.; Jumbe, N.L.; Frey, N. A comprehensive hepatitis C viral kinetic model explaining cure. *Clin. Pharm. Therapeut. 2010*, 87, 706–713. [CrossRef]
6. Herrmann, E.; Lee, J.H.; Marinos, G.; Modi, M.; Zeuzem, S. Effect of ribavirin on hepatitis C viral kinetics in patients treated with pegylated interferon. *Hepatology 2003*, 37, 1351–1358. [CrossRef]
7. Song, X.; Neumann, A.U. Global stability and periodic solution of the viral dynamics. *J. Math. Anal. Appl. 2007*, 329, 281–297. [CrossRef]
8. Dahari, H.; Major, M.; Zhang, X.; Mihalik, K.; Rice, C.M.; Perelson, A.S.; Feinstone, S.M.; Neumann, A.U. Mathematical modeling of primary hepatitis C infection: Noncytolytic clearance and early blockage of virion production. *Gastroenterology 2005*, 128, 1056–1066. [CrossRef]

<!-- PAGE BREAK -->

<a id='9152f8fc-4d49-4a71-b1a1-767da12468bd'></a>

Viruses 2018, 10, 195

<a id='ee8a169e-bfa2-4542-9ab8-2e12e7488ede'></a>

41 of 41

<a id='806501c9-6391-48b1-a664-007dbbbc700d'></a>

9. Reluga, T.C.; Dahari, H.; Perelson, A.S. Analysis of hepatitis C virus infection models with hepatocyte
homeostasis. SIAM J. Appl. Math. 2009, 69, 999-1023. [CrossRef]

10. Tanaka, M.; Itoh, T.; Tanimizu, N.; Miyajima, A. Liver stem/progenitor cells: Their characteristics and
regulatory mechanisms. J. Biochem. 2011, 149, 231-239. [CrossRef]

11. Marshall, A.; Rushbrook, S.; Davies, S.E.; Morris, L.S.; Scott, I.S.; Vowler, S.L.; Coleman, N.; Alexander, G.
Relation between hepatocyte G1 arrest, impaired hepatic regeneration, and fibrosis in chronic hepatitis C
virus infection. Gastroenterology 2005, 128, 33-42. [CrossRef]

12. Pomfret, E.A.; Pomposelli, J.J.; Gordon, F.D.; Erbay, N.; Price, L.L.; Lewis, W.D.; Jenkins, R.L. Liver
regeneration and surgical outcome in donors of right lobe liver grafts. Transplantation 2003, 76, 5-10.

13. Darwiche, H.; Petersen, B.E. Biology of the adult hepatic progenitor cell: "Ghosts in the machine". Prog. Mol.
Biol. Transl. Sci. 2010, 97, 229-249. [CrossRef]

14. Katoonizadeh, A.; Nevens, F.; Verslype, C.; Pirenne, J.; Roskams, T. Liver regeneration in acute severe liver
impairment: A clinicopathological correlation study. Liver Int. 2006, 26 1225-1233. [CrossRef]

15. DebRoy, S.; Bolkerzand, B.M.; Martcheva, M. Bistability and long-term cure in a within-host model of
hepatitis C. J. Biol. Sys. 2011, 19, 533-550. [CrossRef]

16. Turner, R.; Lozoya, O.; Wang, Y.; Cardinale, V.; Gaudio, E.; Alpini, G.; Mendel, G.; Wauthier, E.; Barbier, C.;
Alvaro, D.; et al. Human hepatic stem cell and maturational liver lineage biology. Hepatology 2011, 53,
1035-1045. [CrossRef]

17. Adams, B.M.; Banks, H.T.; Davidian, M.; Kwon, H.D.; Tran, H.T.; Wynne, S.N.; Rosenberg, E.S. HIV dynamics:
Modeling, data analysis, and optimal treatment protocols. J. Comp. Appl. Math. 2005, 184, 10–49.

18. Hepatitis C Fact Sheet. World Health Organization, 2017. Available online: http://www.who.int/
mediacentre/factsheets/fs164/en/ (accessed on 11 April 2018). [CrossRef]

19. Rong, L.; Perelson, A.S. Treatment of hepatitis C virus infection with interferon and small molecule direct
antivirals: Viral kinetics and modeling. Crit. Rev. Immunol. 2010, 30, 131-148.

20. Grimshaw, R. Nonlinear Ordinary Differential Equations; Blackwell: Oxford, UK, 1990.

21. Wiggins, S. Introduction to Applied Nonlinear Dynamical Systems and Chaos, 2nd ed.; Texts in Applied
Mathematics; Springer: New York, NY, USA, 2003, Volume 2. [CrossRef]

22. Hsu, C.S.; Hsu, S.J.; Chen, H.C.; Tseng, T.C.; Liu, C.H.; Niu, W.F.; Jeng, J.; Liu, C.J.; Lai, M.Y.; Chen, P.J.; et al.
Associate of IL28B gene variations with mathematical modeling of viral kinetics in chronic hepatitis C
patients with IFN plus ribavirin therapy. Proc. Natl. Acad. Sci. USA 2011, 108, 3719-3724. [CrossRef]

23. Guedj, J.; Dahari, H.; Perelson, A.S. Understanding the nature of early HCV RNA blips and the use of
mathematical modeling of viral kinetics during IFN-based therapy. Proc. Natl. Acad. Sci. USA 2011, 108, E302.
[CrossRef]

24. Rong, L.; Perelson, A.S. Mathematical analysis of multiscale models for hepatitis C virus dynamics under
therapy with direct-acting antiviral agents. Math. Biosci. 2013, 245, 22-30. [CrossRef]

25. Dahari, H.; Guedj, J.; Perelson, A.S.; Layden, T.J. Hepatitis C viral kinetics in the era of direct acting antiviral
agents and IL28B. Curr. Hepat. Rep. 2011, 10, 214-227. [CrossRef]

26. Rong, L.; Guedj, J.; Dahari, H.; Coffield, D.J., Jr.; Levi, M.; Smith, P.; Perelson, A.S. Analysis of hepatitis C virus
decline during treatment with the protease inhibitor danoprevir using a multiscale model. PLOS Comp. Biol.
2013, 9, e1002959.

27. TenCate, V.; Sainz, B., Jr.; Cotler, S.J.; Uprichard, S.L. Potential treatment options and future research to
increase hepatitis C virus treatment response rate. Hepat. Med. 2010, 2, 125-145. [CrossRef]

28. Arthur, J.G.; Tran, H.T.; Aston, P.J. Feasibility of parameter estimation in hepatitis C viral dynamics models.
J. Inverse Ill-Posed Probl. 2017, 25, 69-80.

<a id='91fb1b43-e991-40f1-ba67-62259a8be3f9'></a>

CC
BY
© 2018 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).
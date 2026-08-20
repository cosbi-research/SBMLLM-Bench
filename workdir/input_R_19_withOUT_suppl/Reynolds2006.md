<a id='3ba440cf-0798-4830-bb31-83a220384814'></a>

<::logo: Elsevier
ELSEVIER
The logo features a detailed illustration of a tree with two figures beneath it, and the brand name "ELSEVIER" in a serif font below the illustration.::>

<a id='50ea72a7-527d-4216-9d52-90d38d46bc9f'></a>

Available online at www.sciencedirect.com
SCIENCE @ DIRECT®

<a id='b0cd3c64-cab0-43b6-97ff-676617d414aa'></a>

Journal of Theoretical Biology 242 (2006) 220–236

<a id='93e3a8ed-8795-4ba2-82eb-786df153a1c2'></a>

Journal of
Theoretical
Biology

<a id='535bb0dc-af13-49d4-aa67-ab137caacbb1'></a>

www.elsevier.com/locate/yjtbi

<a id='56e25341-d312-4d94-9f70-454700fb3a9f'></a>

A reduced mathematical model of the acute inflammatory response:
I. Derivation of model and analysis of anti-inflammation

<a id='5722ded6-e74f-4cf6-a1d9-c0d248171107'></a>

Angela Reynoldsa, Jonathan Rubina*, Gilles Clermontb,c,d, Judy Daya,
Yoram Vodovotzb,c,e, G. Bard Ermentrouta

<a id='3e847e8f-a7c0-496d-bd41-6ca880dd86c4'></a>

aDepartment of Mathematics, 301 Thackeray, University of Pittsburgh, Pittsburgh, PA 15260, USA
bCIRM (Center for Inflammation and Regenerative Modeling), 100 Technology Drive Suite 200, Pittsburgh, PA 15219-3110, USA
cCRISMA Laboratory, University of Pittsburgh, Pittsburgh, PA 15261, USA
dDepartment of Critical Care Medicine, 3550 Terrace St., University of Pittsburgh Medical Center, Pittsburgh, PA 15261, USA
eDepartment of Surgery, University of Pittsburgh Medical Center, W1542 Biomedical Sciences Tower, 200 Lothrop St., Pittsburgh, PA 15213, USA
Received 24 October 2005; received in revised form 18 February 2006; accepted 22 February 2006
Available online 3 April 2006

<a id='cd3bf556-30c0-42cd-8b68-93cb56dd2848'></a>

Abstract

The acute inflammatory response, triggered by a variety of biological or physical stresses on an organism, is a delicate system of checks and balances that, although aimed at promoting healing and restoring homeostasis, can result in undesired and occasionally lethal physiological responses. In this work, we derive a reduced conceptual model for the acute inflammatory response to infection, built up from consideration of direct interactions of fundamental effectors. We harness this model to explore the importance of dynamic anti-inflammation in promoting resolution of infection and homeostasis. Further, we offer a clinical correlation between model predictions and potential therapeutic interventions based on modulation of immunity by anti-inflammatory agents.

© 2006 Elsevier Ltd. All rights reserved.

<a id='79e6ca7e-88db-487d-bb22-9cb613a0afa4'></a>

*Keywords*: Immunology; Mathematical modeling; Anti-inflammatory cytokines; Sepsis; Bifurcation analysis

<a id='f85c920a-ed3d-4c28-b53d-e88688c06ff1'></a>

## 1. Introduction
Acute biological stress, such as severe infection or trauma, leads to the development of an acute inflammatory response. The goal of this response is to promote adaptation of the organism to stress, eliminate threats to survival such as pathogens, and promote tissue repair and healing. However, an excessive or inappropriate inflam- matory response will lead to collateral tissue damage, organ dysfunction, a prolonged healing phase, or possibly death. This state of excessive inflammation is particularly common in association with extensive physiological organ support as provided in modern intensive care units (Goris et al., 1985; Takala et al., 1999). Organisms have developed regulatory mechanisms to contain the molecular and cellular cascades initiated by excessive inflammation. In general, pro-inflammatory elements that are key to ridding

<a id='85885289-ffb7-47c8-be5a-0b798c3d9eb6'></a>

--- 
*Corresponding author. Tel.: +1412 624 6157; fax: +14126248397.
*E-mail address:* rubin@math.pitt.edu (J. Rubin).

<a id='b0b71d62-d34a-432f-a182-24c866ff028f'></a>

0022-5193/$ - see front matter © 2006 Elsevier Ltd. All rights reserved.
doi:10.1016/j.jtbi.2006.02.016

<a id='b079dafe-591d-4bd0-9136-ca8eeaaf7692'></a>

organisms of large numbers of pathogens also mobilize a
negative feedback, or anti-inflammatory response, which
downregulates the initial inflammatory wave (Fig. 1).
Specific details of pro- and anti-inflammatory responses
may be sculpted by the nature and magnitude of the
initiating insults, as well as by genetic predispositions.

<a id='2606c270-d741-4d10-88aa-c980cc9cc873'></a>

In prior work, we constructed a reduced mathematical
model of the pro-inflammatory response (Kumar et al., 2004)
consisting of a response instigator (pathogen) and early and
late pro-inflammatory mediators. While that model captured
a variety of clinically relevant scenarios associated with the
inflammatory response to infection, the goal of the present
work is to gain insight into the presumed advantage and
robustness instilled by the presence of a time-dependent anti-
inflammatory response. While anti-inflammation inhibits the
subsequent build-up of pro-inflammation and the damage to
tissue that may be caused by pro-inflammation, it also
mitigates the subsequent production of anti-inflammatory
mediators. Thus, the overall effects of anti-inflammation on
the outcome following pathogenic infection, and how these

<!-- PAGE BREAK -->

<a id='f3ade6a6-4cad-44cf-8792-2337d5bf97e0'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='28a1c2c3-9904-4a62-bb64-6667e1b19f1e'></a>

221

<a id='e0aa5020-dcc6-4e3b-9861-1e297c80acff'></a>

<::flowchart: A diagram illustrating the interactions within a four-variable model of the acute immune response. The diagram features four main components: 'Initiating event (P)', 'Inflammation (N*)', 'Damage (D)', and 'Anti-inflammation (C_A)'. 'Inflammation' is represented by a flame icon, and 'Anti-inflammation' by a snowflake icon. Arrows indicate upregulation or stimulation, and bars (T-shaped lines) indicate inhibition. Specific interactions are as follows: Initiating event (P) upregulates Inflammation (N*) and inhibits Anti-inflammation (C_A). Inflammation (N*) upregulates Damage (D) and Anti-inflammation (C_A). Damage (D) upregulates Inflammation (N*) and inhibits Anti-inflammation (C_A). Anti-inflammation (C_A) inhibits Inflammation (N*). There is also a self-inhibitory loop for Inflammation (N*) and a direct inhibitory connection from Anti-inflammation (C_A) to Inflammation (N*). The bar between anti-inflammation and inflammation corresponds to the inhibition of both the production of inflammation and the ability of inflammation to interact with all other involved species. Fig. 1. Interactions included in our four-variable model of the acute immune response. Arrows and bars represent upregulation and inhibition, respectively. The bar between anti-inflammation and inflammation corresponds to the inhibition of both the production of inflammation and the ability of inflammation to interact with all other involved species.::>

<a id='1629b501-723f-4592-985f-527670e0ded6'></a>

effects depend on parameters such as pathogen growth rate
and the anti-inflammatory response rate itself, may be
difficult to predict by intuition alone but are well suited for
dynamical systems analysis.

<a id='55862bab-b8e3-4cc9-a0e9-5f133cdf4405'></a>

As the first step in performing this mathematical analysis, we derive a reduced model of the acute immune response that incorporates pro- and anti-inflammation. This model does not include components of the adaptive immune response, such as T-cells and specific antibodies. Therefore, this model describes the generic response to pathogenic insult (Janeway and Medzhitov, 2002). Our derivation proceeds through several stages, based on calibration of subsystems to generally accepted features of the interactions of particular immune system components, as observed in previous experimental studies. We construct a reduced model of inflammation from these subsystems, where the impact of dynamic anti-inflammation is evaluated through simulations and bifurcation studies. Our results illustrate the health advantage conferred by a dynamic anti-inflammatory response and suggest that the rates of this response may be well tuned to yield optimal outcomes following pathogenic infection. Our findings also point to risks associated with manipulation of the levels of the anti-inflammatory mediator present, either before an initial infection or following an initial infection that is on its way to, but has not yet reached, a healthy resolution. We conclude with a discussion in which we elaborate on these and other possible therapeutic implications of our results.

<a id='9b364f9c-2ef2-484d-b6d5-3379d542739a'></a>

## 2. Methods

Our reduced model of the acute inflammatory response
consists of a system of four differential equations in which

<a id='dc3eb5e0-bf7e-4f2d-845d-87c817bfe875'></a>

the dependent variables represent the levels of pathogen (P), activated phagocytes (N*) such as activated neutrophils, tissue damage (D), and anti-inflammatory mediators (CA) such as cortisol and interleukin-10. This model describes the interactions depicted in Fig. 1. We develop this model by first considering the two-variable subsystems N*/P and N*/D, treating CA as a parameter, then combining these subsystems to form a three-variable subsystem, and finally incorporating the dynamics of the anti-inflammatory mediator to create the reduced model. We adopted a subsystem approach to ensure that the interactions of the model variables are consistent with biological observations.

<a id='c492a7d1-8a66-41a6-b506-e4f7b10bfa7b'></a>

Baseline parameter values for both the subsystems and the reduced model are provided in Table 1 and are selected to remain within the given ranges and constraints found in the experimental literature. This baseline parameter set is used for all simulations except where noted in the text. Parameters that could not be documented from existing data were estimated such that the subsystems behave in a biologically appropriate manner for plausible levels of the anti-inflammatory mediators. Furthermore, when the pathogenic insult is replaced by endotoxin as an initiating event, as presented in Day et al. (2006), the resulting model qualitatively reproduces the responses of immune mediators measured experimentally during repeated endotoxin administrations. Further details on the derivation of parameter ranges, constraints and estimated values, are presented in the Supplementary Materials. Units for the model variables and many of the associated parameters cannot be determined, since the variables represent various types of cells, signaling proteins such as cytokines, and/or other mediators concurrently. More precisely, these variables quantify the response of the immune function they represent rather than, for example, an exact cell count. Therefore, units of most parameters related to these variables are not in conventional form, but rather in terms of the associated variable.

<a id='65831e29-7d22-49a1-aa69-dd93ea00cf66'></a>

Throughout the analysis of the reduced model and its
subsystems, we will be tracking the existence and values of
fixed points, determining the parameter regimes in which
particular fixed points are stable, and locating bifurcations.
A fixed point is a point where the derivatives of all
variables in the system are zero, also known as a critical
point or equilibrium point. This occurs where the
nullclines¹ of the system intersect. We will refer to a fixed
point as stable if the real part of each eigenvalue associated
with the linearized system at that fixed point is negative. In
the systems that we consider, it is exactly the stable fixed
points that represent possible asymptotic steady states
attained by open sets of initial conditions. A bifurcation

<a id='30ab039b-77aa-45ec-97bf-80ba0c5f8969'></a>

¹For a system of the form dx/dt = f(x, y); dy/dt = g(x, y), the x-nullcline (y-nullcline) is the set of points in the (x,y) plane that satisfy f=0 (g = 0). Intersections of nullclines are fixed points, since at an intersection both dx/dt and dy/dt are zero. These ideas generalize directly to systems with more than two equations.

<!-- PAGE BREAK -->

<a id='07bead61-ebb5-45dd-98ae-e6c12a34c067'></a>

<table id="2-1">
<tr><td id="2-2">Parameter</td><td id="2-3">Range</td><td id="2-4">Value</td><td id="2-5">Description</td><td id="2-6">Comments</td><td id="2-7">Sources</td></tr>
<tr><td id="2-8">pm</td><td id="2-9">Estimated</td><td id="2-a">0.6/M-units/h</td><td id="2-b">Rate at which the non-specific local response (M) eliminates pathogen</td><td id="2-c">Estimated to be considerably less efficient than a phagocyte-driven response, and therefore can be overwhelmed with modest to large inocula of pathogen</td><td id="2-d"></td></tr>
<tr><td id="2-e">mp</td><td id="2-f">Estimated</td><td id="2-g">0.01/P-units/h</td><td id="2-h">Rate at which the non-specific local response is exhausted by pathogen (P)</td><td id="2-i"></td><td id="2-j"></td></tr>
<tr><td id="2-k">m</td><td id="2-l">Estimated</td><td id="2-m">0.005 M-units/h</td><td id="2-n">Source of non-specific local response</td><td id="2-o">Chosen to balance known natural half-life of non-specific antibodies (see below)</td><td id="2-p"></td></tr>
<tr><td id="2-q">Pm</td><td id="2-r">0.0013-0.0048/h</td><td id="2-s">0.002/h</td><td id="2-t">Decay rate for the non-specific local response</td><td id="2-u">Range based on the reported half-lives of immunoglobulins G and A, non-specific antibodies probably key in the non-specific local immune response</td><td id="2-v">Janeway et al., 2001; Zouali, 2001</td></tr>
<tr><td id="2-w">pg</td><td id="2-x">0.021-2.44/h Estimated</td><td id="2-y">Various 20 x 10^6/cc</td><td id="2-z">The growth rate of pathogen Maximum pathogen population</td><td id="2-A">Estimated from a lethal model of E. coli rat peritonitis</td><td id="2-B">Spector, 1956; Todar, 2002 Vodovotz, Y. pers. comm.</td></tr>
<tr><td id="2-C">pn</td><td id="2-D">Maximum 2.5/N*-units/h</td><td id="2-E">1.8/N*-units/h</td><td id="2-F">Rate at which activated phagocytes (N*) consume pathogen</td><td id="2-G">Based on observed mean rate of phagocytosis by macrophages in the presence of unlimited supply of targets</td><td id="2-H">Branwood et al., 1992</td></tr>
<tr><td id="2-I">np</td><td id="2-J">Estimated</td><td id="2-K">0.1/P-units/h</td><td id="2-L">Activation of resting phagocytes (NR) by pathogen</td><td id="2-M"></td><td id="2-N"></td></tr>
<tr><td id="2-O">nn</td><td id="2-P">Estimated</td><td id="2-Q">0.01/N*-units/h</td><td id="2-R">Activation of resting phagocytes by previously activated phagocytes and</td><td id="2-S"></td><td id="2-T"></td></tr>
</table>
Table 1
Parameters

<a id='c282987c-f701-4794-9119-ea6be2aa8cc5'></a>

Decay rate of resting phagocytes
Decay rate of activated phagocytes
Activation of resting phagocytes by
tissue damage (D)

<a id='3862e78d-8283-4347-b6b7-1e273782fbbf'></a>

Coxon et al., 1999
Coxon et al., 1999
Andersson et al., 2000

<a id='77bbacbc-8d0a-46fb-a224-fd65fa7506ff'></a>

222

<a id='7d59c6b0-a85c-4e33-83f0-2af88c82b50b'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220-236

<a id='d0819fff-7916-4a26-a7e4-6d62b0d717d2'></a>

<table><thead><tr><th></th><th>Estimated</th></tr></thead><tbody><tr><td>s_nr</td><td>0.08 N_R-units/h</td></tr><tr><td>μ_nr</td><td>0.069-0.12/h</td></tr><tr><td>μ_n</td><td>Less than μ_nr<br>0.12/h<br>0.05/h</td></tr><tr><td>k_nd</td><td>Less than k_np<br>0.02/D-units/h</td></tr></tbody></table>

<a id='61175cd0-0875-48fa-b999-3344e18f46dd'></a>

previously activated phagocytes
their cytokines
Source of resting phagocytes

<a id='82afd293-d8f0-4eef-bcf4-af20e7d005c2'></a>

This parameter was chosen to ensure a stable concentration of resting phagocytes in the absence of any perturbation on the system
We used half-life of 6 h
Activated cells have prolonged half-lives due to delayed apoptosis
Peak of the activated phagocyte response elicited from pathogen (k_np) is greater than that triggered by damage (k_nd)

<!-- PAGE BREAK -->

<a id='34a2235f-db0f-4c9a-896a-ba69423af2f6'></a>

<table id="3-1">
<tr><td id="3-2">kdn</td><td id="3-3">Estimated</td><td id="3-4">0.35 D-units/h</td></tr>
<tr><td id="3-5">xdn</td><td id="3-6">Estimated</td><td id="3-7">0.06 N*-units</td></tr>
<tr><td id="3-8">μd</td><td id="3-9">0.017 minimum</td><td id="3-a">0.02/h</td></tr>
<tr><td id="3-b">c∞</td><td id="3-c">Estimated</td><td id="3-d">0.28 CA-units</td></tr>
<tr><td id="3-e">Sc</td><td id="3-f">Estimated</td><td id="3-g">0.0125 CA-units/h</td></tr>
<tr><td id="3-h">kcn</td><td id="3-i">Estimated</td><td id="3-j">0.04 CA-units/h</td></tr>
<tr><td id="3-k">kcnd</td><td id="3-l">Estimated</td><td id="3-m">48 N*-units/D-units</td></tr>
<tr><td id="3-n">μc</td><td id="3-o">0.15-2.19/h</td><td id="3-p">0.1/h</td></tr>
</table>

<a id='e2337913-cf75-4e2d-ac60-b2e75167491d'></a>

Maximum rate of damage produced
by activated phagocytes (and/or
associated cytokines and free radicals)
Determines level of activated
phagocytes needed to bring damage
production up to half its maximum
Decay rate of damage; a combination
of repair, resolution, and regeneration
of tissue

<a id='6b571fc9-1d81-4d23-825e-efdfa7eee83d'></a>

Controls the strength of the anti-inflammatory mediator (C_A)

<a id='abdab7ab-d1db-457a-abd5-4d3b8ce07d6c'></a>

Source of the anti-inflammatory mediator

<a id='29ea474a-c929-4b11-8f9a-0425caba8272'></a>

Maximum production rate of the anti-inflammatory mediator
Relative effectiveness of activated phagocytes and damaged tissue in inducing production of the anti-inflammatory mediator
Decay rate of the anti-inflammatory mediator

<a id='1cd53dcf-064b-4f75-a797-4bfdaf81590e'></a>

We calculated the parameter from data of the half-life of HMG-1, a histone tethering protein leaked by damaged cells as a surrogate for the many danger molecules that perpetuate the inflammatory signal

<a id='335b1245-975c-4b3c-8be3-00c3ed99c0d7'></a>

Set such that f(x) = x/(1+(C_A/c_∞)²)
corresponds to ≈75% inhibition when C_A
reaches maximum value in response to an insult.
Organisms have constitutive levels of anti-
inflammatory effectors. The source parameter
was chosen to balance their documented half-
life

<a id='1ebd0a54-43fd-4579-8987-d73aa614f694'></a>

Wang et al., 1999

<a id='ae71ce84-660f-4074-adae-4b355b4bc72e'></a>

Isler et al., 1999

<a id='44c6623c-6ede-4449-958d-2dab0659f5df'></a>

Tsukaguchi et al., 1999

<a id='77c0aabb-70f9-4713-892c-3a3438847dd8'></a>

Anti-inflammatory signals have downstream cellular effects not explicitly modeled herein, lasting longer than the effector cytokine or molecule producing it. Therefore, our parameter value was set below the lower limit of reported half-lives of anti-inflammatory effectors. This still probably is a higher bound for this parameter

<a id='c753b17d-02f0-4fd0-afae-6d23141c6dac'></a>

Bacon et al., 1973; Bocci,
1991; Fuchs et al., 1996;
Huhn et al., 1997

<a id='93792e63-e23b-412f-b16f-89d85ac0a73b'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220-236

<a id='f4e19cdf-0401-49fb-a750-7714efd79f45'></a>

223

<!-- PAGE BREAK -->

<a id='d1a84e95-1cc6-4c0b-a69e-375487821fa2'></a>

224

<a id='298bc003-a1b4-4da8-b9a0-e9fd1ba0c356'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='e80e5adc-9f9e-4e49-b2ca-701f9a48f701'></a>

occurs when a change in a parameter alters the number of
fixed points and/or their stability, and thus changes the
number and nature of the asymptotic steady states of the
system (Strogatz, 1994).

<a id='fc5a5d60-5555-4ade-a1c8-9aa5875a2d1a'></a>

The reduced model displays three physiologically relevant equilibrium points, which correspond to biological states of health, aseptic death, and septic death, respectively. The health state is a fixed point with P = 0, N* = 0, D = 0, and CA = sc/μc, which, when stable, is the desirable asymptotic behavior. The aseptic death state, which corresponds to an outcome where pathogen has been eliminated but with high and persistent immune activation and damage, is a fixed point where P = 0, N*>0, D>0 and CA>0. The third possible equilibrium is septic death, where all variables are non-zero, which corresponds to a state in which there is insufficient immune activation to clear pathogen. Note that a healthy outcome viewed as a return to an equilibrium point is an idealized construct. In fact, the complex biological systems we are considering are out of equilibrium and a return to mediator levels within the basin of attraction² of the health state is a desirable outcome. However, in the reduced model, solutions with initial conditions in the basin of attraction of health asymptotically approach health. Thus, for simplicity we refer to the fixed point, (0,0,0,sc/μc) as the health state.

<a id='5a266927-4af7-44d3-9653-211c0d24c44b'></a>

2.1. The non-specific local immune response: the M/P subsystem

A normal individual in a healthy state has a baseline capacity to respond and resolve local infections. This resides in the presence of cells, such as tissue macrophages as well as other non-specific physical and biological defenses, such as defensins and non-specific antibodies (Ochsenbein and Zinkernagel, 2000; Paulsen et al., 2002; Raj and Dentino, 2002). This local response is rapid and effective, but can be overwhelmed with large inocula or rapidly dividing pathogens. To account for this non-specific local removal of pathogen, we assume the reactions in Table 2, with the non-specific local response and pathogen levels represented by the variables M and P, respectively.

<a id='faaf641e-3ec2-4720-98b3-289c5494eae6'></a>

From the reactions in Table 2, based on mass action kinetics, we derive the following preliminary equations:

<a id='99684bd6-f759-4e9c-900b-0ca39b975aea'></a>

dM/dt = sm - mM - kmpMP,

<a id='7b04b611-0b86-4661-bb54-a92651e7aaeb'></a>

<::dP/dt = -k_pm MP.:figure::>

<a id='f9b2be89-b90a-48e2-abd2-74277fd87d8e'></a>

For simplicity, we assume that the local response reaches
quasi-steady state and substitute M = S_m/(µ_m + k_mpP) into
the pathogen equation. Further, to incorporate the
dynamics of the pathogen population into our model, we

<a id='0add2f0e-2e1d-4c37-8d3c-e112d0c6ebbb'></a>

---  
2The basin of attraction of a stable fixed point, x*, of a dynamical system is the set of all initial conditions that dynamically evolve to x* (Strogatz, 1994).

<a id='d4b624a2-cb2c-4105-b1f0-2ac84eddadc4'></a>

Table 2 Reactions involving the local immune response (M) and pathogen (P)
<table><thead><tr><th>Col 1</th><th>Col 2</th></tr></thead><tbody><tr><td>M + P <sup>kpm</sup> &rarr; M</td><td>P is destroyed at the rate k<sub>pm</sub> when it encounters M</td></tr><tr><td>M + P <sup>kmp</sup> &rarr; P</td><td>M is consumed at the rate k<sub>mp</sub> when it encounters P</td></tr><tr><td>* <sup>sm</sup> &rarr; M</td><td>Source of M</td></tr><tr><td>M &rarr; <sup>&mu;m</sup></td><td>Death of M</td></tr></tbody></table>

<a id='1c948b46-d043-4482-9f08-bd54bc267683'></a>

used a logistic growth term, $k_{pg}P(1 - P/p_{\infty})$. Therefore, we obtain the pathogen equation:

$\frac{dP}{dt} = k_{pg}P\left(1 - \frac{P}{p_{\infty}}\right) - \frac{k_{pm}s_mP}{\mu_m + k_{mp}P}.$ (1)

<a id='4a3d2aba-ee3a-41fb-b600-070ab1b52f6e'></a>

Here, the pathogen growth rate and the carrying capacity of the pathogen population are represented by $k_{pg}$ and $p_\infty$, respectively. The units for $k_{pg}$ are per hour while $p_\infty$ has the same units as P, $10^6$/cc. P = 0 is always a fixed point of Eq. (1). We find that a saddle-node bifurcation gives rise to two additional fixed points, say $p_1 < p_2$, which exist for $k_{pg} > 4k_{mp}k_{pm}s_m p_\infty / (p_\infty k_{mp} + \mu_m)^2$, or equivalently for $k_{pg} > 0.059$ with the parameters in [Table 1](Table 1). When they first arise, $p_1$ and $p_2$ are positive. Direct linearization and algebraic manipulation show that P = 0 is stable for $k_{pg} < k_{pm}s_m / \mu_m = 1.5$, where it loses stability in a transcritical bifurcation with $p_1$, and that the largest fixed point is stable whenever it exists. Thus for $0.059 < k_{pg} < 1.5$, this subsystem is bistable.

<a id='47f6b7db-b27c-41f3-8854-43dd3ec99e10'></a>

## 2.2. The N*/P subsystem

A key component of the acute immune response is the removal of the pathogen by phagocytic immune cells, such as activated neutrophils and macrophages. Resting phagocytes are activated by pathogen and by previously activated phagocytes via the binding of endotoxin and pro-inflammatory cytokines (Janeway and Medzhitov, 2002). Once activated, a phagocyte becomes efficient at eliminating pathogens. When the growth rate of the pathogen is low, activated phagocytes are capable of clearing the pathogen in normal individuals. However, if the growth rate is high, then a sufficiently large inoculum of pathogen can induce a persistent infection despite the attack by activated phagocytes. This dependence on kpg and the interaction between resting and activated phagocytes are essential in developing the N*/P subsystem, which consists of the following:

<a id='a3d4edaf-f7f7-41f2-93a8-3f0d0c9aa25e'></a>

dP/dt = k_pg * P * (1 - P/P_infinity) - (k_pm * s_m * P) / (mu_m + k_mp * P) - k_pn * N* * P (2)

<a id='80746ec7-ab49-452f-a93d-1ed98153382c'></a>

$\frac{dN^{*}}{dt} = \frac{s_{nr} R_{1}}{\mu_{nr} + R_{1}} - \mu_{n}N^{*}$, (3)
where $R_{1} = k_{nn}N^{*} + k_{np}P$.

<a id='07fa723c-465a-4d4a-a1b4-768a7572ee0b'></a>

To derive Eqs. (2) and (3) we first take into account the activation of the resting phagocytes ($N_R$). In particular, from the system of reactions given in Table 3, we derive the

<!-- PAGE BREAK -->

<a id='5a4abb0c-b45a-4cc5-99e7-81a86be720f4'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220-236

<a id='a94352b7-cf8d-4c8b-b456-a85760212d53'></a>

225

<a id='d2b985ed-59e1-486c-87e2-27561bc2301c'></a>

Table 3
Reaction involving resting and activated phagocytes

<table><thead><tr><th>Col 1</th><th>Col 2</th></tr></thead><tbody><tr><td>N<sub>R</sub> <span style="font-size: 0.8em;">k<sub>np</sub>P+k<sub>nn</sub>N*</span><br>→ N*</td><td>Activation of the resting phagocytes (N<sub>R</sub>) is induced by the presence of pathogen (P) and by positive feedback from the activated phagocytes (N*) via pro-inflammatory cytokines</td></tr><tr><td>* <span style="font-size: 0.8em;">s<sub>nr</sub></span><br>→ N<sub>R</sub></td><td>Source of N<sub>R</sub></td></tr><tr><td>N<sub>R</sub> <span style="font-size: 0.8em;">μ<sub>nr</sub></span><br>→</td><td>Death of N<sub>R</sub></td></tr><tr><td>N* <span style="font-size: 0.8em;">μ<sub>n</sub></span><br>→</td><td>Death of N*</td></tr></tbody></table>

<a id='6c98c642-6749-4be2-9eab-ed22b326d10e'></a>

following equations:

$\frac{dN_R}{dt} = s_{nr} - \mu_{nr} N_R - R_1 N_R,$

<a id='7bf53d2c-a619-4d48-bfe7-811cc63d93cc'></a>

$\frac{dN^*}{dt} = R_1 N_R - \mu_n N^*,$

<a id='dc4e4d97-3d20-4041-8f15-9a517b31a3e0'></a>

where $R_1 = k_{nn}N^* + k_{np}P$.
When a resting phagocyte encounters an agent capable of activating it, however, the activation process is rapid. Thus, we assume that the variable $N_R$ is in quasi-steady state, reducing the $N_R/N^*$ system to a single equation (3). When this equation is combined with the pathogen equation (1) derived above, and an additional term is included to encode the direct consumption of pathogen by activated phagocytes, we obtain systems (2) and (3).

<a id='d6780a3d-8be2-4593-afd6-2f8f767a410b'></a>

Linearization of Eqs. (2) and (3) about the health fixed point (P,N*) = (0,0) yields real eigenvalues that are negative for kpg <kpmSm/µm and µη > Snrknn/µηr. Since the second of these inequalities holds for the parameters in Table 1, the condition kpg<kpmSm/µm is once again the criterion for the stability of health, as in the M/P subsystem.

<a id='2254af25-d2e8-4bea-b50b-c51404b46ad1'></a>

We provide a further analysis of the fixed points of Eqs. (2) and (3) below, but first, to more accurately model the immune response, we introduce the anti-inflammatory mediator in this subsystem. At this point, we simply encode anti-inflammatory effects in a parameter $C_A$. By treating the anti-inflammatory mediator as a parameter, we can manually manipulate it to verify that sustained variations in its level induce biologically appropriate alterations in the $N^*/P$ dynamics, such that this subsystem will behave appropriately once dynamic anti-inflammatory mediators are incorporated.

<a id='9925ccc2-768b-4e6a-bdfb-ed5a4dfbd863'></a>

In normal individuals, the anti-inflammatory mediator inhibits the activation of phagocytes and reduce the ability of activated phagocytes to attack pathogen (Tsukaguchi et al., 1999). We incorporate this inhibition into the N*/P subsystem by replacing R₁ with f(R₁) and N* with f(N*) in Eq. (2), for f(V) = V/(1 + (C_A/c_∞)²). The parameter c_∞ is set such that when the anti-inflammatory mediators reach their maximum level in response to an infection, their inhibitory effects are roughly equivalent to a 75% reduction in the inhibited element, as seen in Isler et al. (1999). While it would have been reasonable to consider different levels of inhibition by the anti-inflammatory

<a id='00cdd4d0-7289-4c62-a5e3-1fff22c3cdd5'></a>

mediator for each interaction, we consider uniform inhibition for simplicity.

<a id='582b8fc2-d053-438e-a0b4-4af94b92bbd3'></a>

For low pathogen growth rate (kpg), the resulting N*/P subsystem has only the stable health state, whose existence is independent of CA. There is a saddle-node bifurcation at kpg = 0.8829 for the parameters in Table 1 with CA fixed to 0.2. The corresponding bifurcation diagram is displayed in Fig. 2(a), which was created, as were all other figures in this paper, using XPPAUT (Ermentrout, 2002). Of the pair of fixed points born in the saddle-node bifurcation, the lower (with respect to N*) is a saddle separatrix, while the upper, corresponding to septic death (P>0, N*>0), is initially unstable. As kpg increases further, there is a Hopf bifurcation at kpg = 1.187, which stabilizes septic death. Finally, health loses stability through a transcritical bifurcation at kpg = 1.5. The stable branch that is created corresponds to negative levels of pathogen and activated phagocytes and is therefore not included in the bifurcation figure. In summary, for 1.187<kpg<1.5 and CA = 0.2, this subsystem features bistability between health and septic death.

<a id='3c2ec5c3-73a1-45aa-b82e-89c8668816a8'></a>

This bifurcation structure remains qualitatively similar for nearby values of C_A, while for sufficiently elevated C_A levels, septic death is stable as soon as it appears and we no longer observe a Hopf bifurcation. We examined the criteria for existence of stable septic death in a two-parameter bifurcation k_pg-C_A plane. A curve divides the plane in two regions (solid curve in Fig. 2(b)). For parameter values on the left of the curve, stable septic death does not exist, while on the right, it does. Also in Fig. 2(b), at k_pg = 1.5, there is a dashed vertical line that denotes where the health state loses stability. This line further divides the plane, creating a total of four regions: health, health/septic death, septic death, and a shaded region. The first three regions are labeled by the stable states that corresponding parameter values support. In the shaded region, septic death does not exist, and health is unstable. Therefore, there is no stable fixed point and trajectories oscillate. This does not represent a biologically observed state; however, once we combine subsystems below, oscillations will no longer occur.

<a id='982b998c-745d-4c62-80ad-b31355e64957'></a>

In Fig. 2(c), we see the effect of C_A on the level of activated phagocytes (N*) in the septic death state when it first becomes stable. From Fig. 2(b), we know that as C_A increases, the k_pg value at which the stable septic death state appears decreases. Biologically, this corresponds to a prediction that holding C_A at a larger constant level

<!-- PAGE BREAK -->

<a id='1b09852b-20dc-4320-8638-96a8ff242194'></a>

226

<a id='23468a2e-93e6-4a67-aa51-c34f9acf48b9'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='4670d353-0eb0-4f93-9733-d6747f46f7b9'></a>

induces a greater inhibition of the immune response,
allowing a less virulent pathogen to induce a septic death
outcome. In theory, this inhibition of N* could allow an
initial enhancement of the build-up of P, which would
subsequently evoke a large rise in N*, leading to a high N*
septic death state; alternatively, the combination of higher
C_A and low k_pg could suppress the level of N* seen in septic
death. Fig. 2(c) shows that in fact the latter possibility
occurs, such that the activated phagocyte levels reached in

<a id='ec9d9ecc-2cda-46e4-b3c0-fbf4886eb3b7'></a>

septic death decrease, along with the pathogen growth rate,
as the anti-inflammatory response increases.

<a id='d2cfe065-c086-4e1a-a5c6-d4b5b74a4566'></a>

For parameters corresponding to the region of septic
death/health in Fig. 2(b), the N*/P subsystem is bistable.
As noted above, a saddle separatrix, specifically the stable
manifold of a saddle fixed point, separates the two stable
states, as we see Fig. 2(d) and (e) for C_A = 0.2. Notice the
boxed region in Fig. 2(d). Zooming in on this region, as in
Fig. 2(e), we see that the P nullcline and the stable manifold

<a id='05b434d0-5e0c-45f9-a539-3053e16aef42'></a>

<::Figure (a): Bifurcation diagram showing Activated Phagocytes (N*) on the y-axis and Growth Rate of Pathogen (kpg) on the x-axis. The curve illustrates different bifurcation points: a Hopf bifurcation at kpg = 1.187, a saddle-node bifurcation at kpg = 0.8829, and a transcritical bifurcation at kpg = 1.5.: chart::>
(a)
<::Figure (c): Plot of Activated Phagocytes (N*) on the y-axis versus Growth Rate of Pathogen (kpg) on the x-axis. The curve represents the C_A = 0 nullcline, with an arrow indicating the direction of increasing C_A.: chart::>
(c)
<::Figure (b): Phase diagram showing Anti-inflammatory Mediator (CA) on the y-axis and Growth Rate of Pathogen (kpg) on the x-axis. The plot is divided into regions labeled 'Health', 'Septic Death/Health', and 'Septic Death', separated by a curve and a dashed vertical line. A shaded region in the bottom right corner indicates 'Septic Death'.: chart::>
(b)
<::Figure (d): Phase portrait showing Activated Phagocytes (N*) on the y-axis versus Pathogen (P) on the x-axis. The plot includes: Pathogen Nullcline (black line), Activated Phagocytes Nullcline (red line), Stable Manifold of the Saddle Point (blue line), Unstable Manifold of the Saddle Point (blue line), a Saddle Point (triangle), and a Stable Fixed Point (dot). The trajectories illustrate the system's dynamics around these points.: chart::>
(d)
<::Figure (e): Zoomed-in phase portrait showing Activated Phagocytes (N*) on the y-axis versus Pathogen (P) on the x-axis, focusing on the region near the origin. The plot includes: Pathogen Nullcline (black line), Activated Phagocytes Nullcline (red line), Stable Manifold of the Saddle Point (blue line), Unstable Manifold of the Saddle Point (blue line), a Saddle Point (triangle), and a Stable Fixed Point (dot).: chart::>
(e)

<!-- PAGE BREAK -->

<a id='84aa8047-2677-4c3b-8c69-f79429c3ec04'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='a7bbab21-319f-4fee-9e5c-0d52bff2a4fb'></a>

227

<a id='99332ca9-5f3c-4471-8ffe-809928f6ad22'></a>

of the saddle point divide the P-axis into three regions. Suppose an initial pathogen load, P_0, is introduced to the system, which had previously been in the health state. When P_0 falls in the first region, to the left of the P nullcline, the non-specific local response is able to eliminate the pathogen without any transient pathogen growth. If P_0 falls in the middle region, between the P nullcline and the stable manifold, then the pathogen is able to overcome the local response and initially grow before the activated phagocytes respond and clear the infection. If P_0 is in the final region, to the right of the stable manifold, then the immune response is unable to heal the individual. When the subsystems are combined, and the anti-inflammatory mediator is allowed to evolve dynamically, we shall see that these regions persist, with qualitatively similar properties. Thus, this analysis of the N*/P system with a constant anti-inflammatory mediator is helpful in understanding the role of the activated phagocytes in the pro-inflammatory response to pathogen.

<a id='2c60ff23-87f7-4ff9-8750-e098c2e23ff7'></a>

## 2.3. The N*/D subsystem

When activated phagocytes respond to an infection, their presence in the tissue not only kills pathogens, but may also lead to collateral tissue damage (Goris et al., 1985; Takala et al., 1999). Damaged tissue releases pro-inflammatory cytokines, which causes further phagocyte activation. This positive feedback interaction between phagocytes and damage also exists in the absence of pathogen and can be triggered by other stimuli, such as tissue trauma. Therefore, the N*/D system should be bistable between health and aseptic death over a range of the anti-inflammatory mediator. Modeling the interactions between activated phagocytes and damage, we developed the N*/D subsystem, which consists of the following:

<a id='01f28eb5-3908-4750-b91d-d2f011a5448b'></a>

dN*/dt = s_nr R_2 / (μ_nr + R_2) - μ_n N*, (4)

<a id='a7caec1d-d973-48b1-8867-0a319a88a861'></a>

dD/dt = k_dn f_s(N*) - \mu_d D, (5)
where R_2 = k_nn N* + k_nd D and the saturation function is phenomenologically defined as f_s(V) = V^6/(x_dn^6 + V^6).

<a id='a8aabb60-f3c1-49f5-91f0-478b7e4d475b'></a>

As in the N*/P systems (2) and (3), the activated phagocyte equation in the N*/D system is derived by first considering a system of equations that includes the resting phagocytes and subsequently assuming that the resting phagocytes are in quasi-steady state. The only difference between the N* equations (3) and (4) appears in the activation of resting phagocytes, which we now take to be affected by D rather than P. Correspondingly, R1 from Eq. (3) is replaced by R2 = knnN* + kndD in Eq. (4).

<a id='32c675ce-99db-408c-8a8f-ea2fc0f00e42'></a>

At low counts, activated phagocytes do not cause significant damage. However, as they accumulate in response to an infection, the activated phagocytes will cause tissue damage to accrue. Finally, once levels of activated phagocytes are sufficiently high, damage saturates, such that the activation of additional phagocytes has little impact on damage creation. We model this non-linearity in the induction of damage by activated phagocytes via the Hill-type function, f_s, in Eq. (5). The coefficient in f_s must be chosen to be sufficiently large to produce a reasonable basin of attraction for health in the N*/D system (see Supplementary Materials for further explanation). We subtract the term _dD in Eq. (5) to represent tissue repair, resolution, and regeneration. Linear stability analysis of the health state, (N*, D) = (0,0), shows that the eigenvalues are negative for _n > s_nrk_nn/_nr, which is the same condition that arose for the N*/P subsystem and always holds for our baseline parameter set.

<a id='ae07e65b-cd98-453d-a197-f2dc1dad7dfc'></a>

As in the N*/P subsystem, we introduce the anti-
inflammatory mediator (C_A) into the N*/D subsystem as
a parameter to ensure that our other parameter choices
give the desired bistability for all physiological levels of C_A.
As in the previous subsystem, the inclusion of the anti-
inflammatory mediator leads to inhibition of activated
phagocytes by two means. Specifically, the activation
process itself is inhibited, which we model by replacing
R_2 with f(R_2) in Eq. (4), where f is the same saturating
function defined for inhibition in the N*/P subsystem. The
ability of activated phagocytes to cause damage is also
inhibited by the anti-inflammatory mediator, which we
model by replacing N* with f(N*) in Eq. (5).

<a id='91e8d8ec-ac37-42ab-a9d9-d745f5741429'></a>

As in the N*/P subsystem, the nullclines of the modified
N*/D subsystem intersect such that there are two stable
fixed points separated by a saddle node for appropriate

<a id='51fa2025-5438-4f29-92b6-a7000ee30034'></a>

Fig. 2. Bifurcation diagrams and nullclines for the N*/P subsystem. (a) Bifurcation diagram generated for C_A = 0.2 with bifurcation parameter k_pg. There is a saddle-node bifurcation at k_pg = 0.8829, Hopf bifurcation at k_pg = 1.187, where the system becomes bistable between septic death and health, and a transcritical bifurcation at k_pg = 1.5, where health loses stability. The stable branch emerging from the transcritical point corresponds to negative pathogen and activated phagocytes, a non-physiological situation not displayed. The number of bold curves a vertical line intersects corresponds to the number of stable outcomes possible for the parameter value represented by this line. Which asymptotic outcome is reached depends on the initial conditions of the system. For example, a vertical line at k_pg = 1.3 would intersect two bold curves; therefore, at this parameter value there are two stable outcomes, health and septic death. (b) Two-parameter bifurcation diagram. We follow the existence of stable septic death (the bold line) and the transcritical (dashed line) from (a), with C_A as the second parameter. This divides the k_pg-C_A plane into regions labeled by the set of stable outcomes that exist. In the shaded region there are no stable fixed points and the system oscillates. The diamond represents the point where the bifurcation giving rise to stable septic death changes from a Hopf (below the diamond) to a saddle-node bifurcation (above the diamond). (c) Plot of the solid curve from (b) in (N*, k_pg) space shows the level of activated phagocytes reached at the onset of stable septic death as a function of k_pg. Both N* and k_pg decrease as C_A increases and again a diamond marks the change from a Hopf bifurcation (above the diamond) to a saddle-node bifurcation (below the diamond). (d), (e) Plots of the nullclines for this subsystem with C_A = 0.2 and k_pg = 1.25. The system is bistable between the health and septic death fixed points with a saddle point separating them. The unstable and stable manifolds of the saddle point are included in (d) and by zooming in on the boxed region, we see in (e) that the P-axis is divided into three regions by the P-nullcline and the stable manifold of the saddle point.

<!-- PAGE BREAK -->

<a id='0a7bbe8a-a1a4-4460-b661-b6efe3e1a590'></a>

228

<a id='c8c77dec-bf7e-4154-83f5-0a052295e63d'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='c5b9ec45-75a4-4e06-b6ad-b161c35342bd'></a>

values of C_A. Similar to Fig. 2(d) and (e), Fig. 3(a) shows the nullclines and invariant sets of the N*/D subsystem with C_A = 0.2. The stable manifold of the saddle point defines the threshold between health and aseptic death. The parameters and the Hill coefficient are chosen so that this threshold allows activated phagocytes to adequately respond to an inoculum of pathogen without triggering aseptic death.

<a id='09af6e3b-97bc-487a-8e16-90a29abc820e'></a>

In the bifurcation diagram for the anti-inflammatory
mediator in Fig. 3(b), we see that the N*/D subsystem
displays bistability between health and aseptic death for
C_A<0.626. Note that as the level of C_A increases, the level

<a id='664beb42-57a2-4b55-8c11-369c52d840a1'></a>

of activated phagocytes reached at aseptic death is decreased. This trend makes sense, since the anti-inflam- matory mediator inhibits the activation of phagocytes. Eventually, this inhibition prevents the system from equilibrating at a state where N* remains elevated; specifically, as C_A increases, the nullclines pull apart and eventually do not intersect. This occurs at the saddle node C_A = 0.626 and causes this subsystem to lose bistability. We note that this value lies above the physiological relevant range for C_A and also is consistent with the intuition that high C_A levels prevent the explosion of N* needed for aseptic death.

<a id='29aa1ab2-756a-4fe4-89fa-fdfe6ab74e05'></a>

<::Figure (a) is a phase plane plot showing Tissue Damage (D) on the y-axis and Activated Phagocytes (N*) on the x-axis. The plot displays several curves and points with the following legend: Activated Phagocytes Nullcline (red line), Tissue Damage Nullcline (thick black line), Stable Manifold of the Saddle Point (blue line), Unstable Manifold of the Saddle Point (thin black line), Saddle Point (black triangle), and Stable Fixed Point (red dot). The x-axis ranges from 0.0 to 1.2, and the y-axis ranges from 0 to 15.::> (a) <::Figure (b) is a bifurcation diagram showing Activated Phagocytes (N*) on the y-axis versus The Anti-Inflammatory Mediator (CA) on the x-axis. The plot shows a curve with a saddle-node bifurcation occurring at CA = 0.6264, indicated by a blue square and text label. The x-axis ranges from 0.0 to approximately 0.7, and the y-axis ranges from 0.0 to 1.2.::> (b)

<a id='8f309f6f-cec6-4b33-84d9-e40129ca5c8f'></a>

Fig. 3. Nullclines and bifurcation diagrams for the N*/D subsystem. (a) Plot of the nullclines shows that the stable health and aseptic death fixed points are separated by a saddle point. The stable and unstable manifolds of the saddle point also are included. (b) Bifurcation diagram with bifurcation parameter C_A, showing bistability between health and aseptic death that is lost through a saddle-node bifurcation as C_A increases through 0.6264.

<!-- PAGE BREAK -->

<a id='0f0013f5-47ca-4a96-99aa-8777025a976e'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220-236

<a id='1b86e286-8662-4ef0-90b3-baf169427891'></a>

229

<a id='97e23952-6092-4c18-8317-4cafce47d227'></a>

2.4. The three-variable subsystem

We combine the above two systems by including effects of both pathogen and damage on the rate at which the resting phagocytes are activated. To do this, we let R3 = knnN* + knpP + kndD and again assume that the resting phagocytes are in quasi-steady state to obtain the system of equations:

<a id='2ea21235-fb8e-4a48-a759-2e0ba034a350'></a>

dP/dt = k_pg P (1 - P/P_∞) - k_pm s_m P / (μ_m + k_mp P) - k_pn N* P, (6)

dN*/dt = s_nr R_3 / (μ_nr + R_3) - μ_n N*, (7)

dD/dt = k_dn f_s(N*) - μ_d D, (8)
where
R_3 = k_nn N* + k_np P + k_nd D
and
f_s(V) = V^6 / (x_dn^6 + V^6)

<a id='e7163b7e-41a8-476c-b0ad-8e4e917f3800'></a>

Models (6)-(8) exhibit the combined dynamics of the previous two subsystems. The conditions for stable health are unchanged from the N*/P subsystem, since D = 0 at the health fixed point. In particular, health is stable for low pathogen growth rate (kpg), but loses stability at a transcritical bifurcation at kpg = 1.5 as kpg is increased. Since this instability is induced by the pathogen dynamics, it follows that even after this stability loss, the healthy state retains a two-dimensional stable manifold, such that small perturbations in the non-pathogen components lead to healthy resolutions. For low or moderate growth rate, the system inherits the existence of stable aseptic death from the bistability of the N*/D subsystem. Consequently, for low pathogen growth rate, the physiological outcomes after pathogenic infection are health, achieved when the initial pathogen level is low, and aseptic death, arising when the initial inoculum of pathogen is large enough that the resulting phagocytic response results in large tissue damage.

<a id='22b4ac59-0514-446d-ac1b-54b54f60901a'></a>

As in the N*/P subsystem, increasing pathogen growth rate leads to a bifurcation that introduces the possibility of septic death. Fig. 4(a) shows a bifurcation diagram with C_A = 0.2, in which we see that this bifurcation is a Hopf at k_pg = 1.707. This diagram also shows the transcritical bifurcation that destabilizes the health state at k_pg = 1.5; the second branch of equilibria participating in this bifurcation is not shown, since it corresponds to a non-physiological state with negative pathogen and activated phagocytes. Since health is already unstable for k_pg < 1.707, there are only two possible stable outcomes, aseptic death and septic death, until k_pg = 2.769, when aseptic death loses stability through a second transcritical bifurcation. Aseptic death loses stability when k_pg becomes so large that

<a id='357c4005-ef46-44a5-b4ce-c32913c9f65d'></a>

the immune system cannot clear the pathogen, preventing
stability of a state with a non-zero pathogen level and
leaving septic death as the only stable state for the system.

<a id='0c6b3cee-c18b-418d-87c4-463e0503ef68'></a>

Despite the bistability between aseptic and septic death for 1.707 < k_pg < 2.769, initial conditions with only pathogen elevated, and all other variables at healthy levels, always lead to septic death for fixed C_A. The aseptic death outcome is attainable if tissue trauma (D_0 > 0) occurs in the absence of pathogen or if the initial level of activated phagocytes (N*_0 > 0) is elevated (with or without pathogen). A pre-activated immune system allows the infection to be cleared, avoiding septic death. However, activated phagocytes continue to be elevated in response to the pathogen, and this triggers aseptic death.

<a id='457fbdf4-fe8e-4b7d-be5a-a8567582c4e5'></a>

Next, we follow the bifurcation points in a two-parameter bifurcation diagram in the $k_{pg}-C_A$ plane (Fig. 4(a) and (b)). The existence of septic death is represented by the solid curve. For a combination of parameters on the right of this curve, this system enters septic death (given a sufficient inocula for pathogen), while on the left, septic death does not exist. The transcritical bifurcation where health loses stability is represented by the vertical dashed line at $k_{pg} = 1.5$. To the right of this line the health state is unstable. The transcritical threshold corresponding to the loss of stability of aseptic death is represented by a blue dashed curve. Also, for $C_A$ levels above the horizontal, dashed line, aseptic death does not exist due to the same saddle-node bifurcation we showed in the $N^*/D$ subsystem. Therefore, aseptic death is not a possible outcome above the horizontal, dashed line or to the right of the blue dashed curve. Combining these bifurcation structures we are able to label each region, as we did in Fig. 2(b), by the stable states they support.

<a id='74ed1571-b068-4b75-baa0-13ccdfb78cee'></a>

From the two-parameter bifurcation diagram in Fig. 4(b), we observe that for C_A>0.234, the bifurcation giving rise to the existence of septic death occurs at a k_pg <1.5. Therefore, if 0.234<C_A<0.626 (indicated by the horizontal, dashed line in Fig. 4(b)), there is a range of k_pg for which all three outcomes are stable. As in the case with C_A = 0.2 and bistability between aseptic and septic death, the path to aseptic death is sensitive to initial conditions and there is a propensity to enter septic death when only pathogen is initially introduced.

<a id='3719d031-47a1-48f3-b6b1-4228e6a6a80e'></a>

2.5. The four-variable model

We complete the model derivation by introducing time dependence to the anti-inflammatory mediator C_A, thereby obtaining our four-variable reduced model of the acute immune response. The production of the anti-inflammatory mediator is associated with the presence of activated phagocytes (de Waal et al., 1991) and elevated markers of tissue damage (Stvrtinova et al., 1995). As discussed in the development of the various subsystems considered above, the anti-inflammatory mediator (C_A) regulates the immune response by inhibiting the production and effects of activated phagocytes and damage. More specifically, the

<!-- PAGE BREAK -->

<a id='5e9f8acb-1230-4446-8f58-c3c07a05cfb2'></a>

230

<a id='729f82d7-2d3b-4289-8512-df8ce0471351'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236<::chart: (a) Bifurcation diagram showing Activated Phagocytes (N*) on the y-axis and Growth Rate of Pathogen (kpg) on the x-axis. The y-axis ranges from 0.0 to 1.4, with a break between 0.2 and 1.0. The x-axis ranges from 0 to 4. A horizontal line at N* = 0.0 shows a transcritical bifurcation point at kpg = 1.5. A horizontal line at N* = 1.0 shows a saddle-node bifurcation point at kpg = 1.702 and a transcritical bifurcation point at kpg = 2.769. A curve emerges from the saddle-node point, extends upwards, and then curves back down to meet the horizontal line at the transcritical point (kpg = 2.769). A Hopf bifurcation point is indicated on the upper part of this curve at kpg = 1.707.::><::chart: (b) Phase diagram showing Anti-inflammatory Mediator (CA) on the y-axis and Growth Rate of Pathogen (kpg) on the x-axis. The y-axis ranges from 0.0 to 1.0, and the x-axis ranges from 0 to 4. The plot is divided into several regions by solid black curves, a dashed red horizontal line, a dashed vertical black line at kpg approx 1.6, and a dashed blue curve. The regions are labeled as follows: 'Health' (top-left corner, bounded by a black curve and red dashed line), 'Health & Septic Death' (above the black curve and left of the dashed vertical line), 'Health, Aseptic & Septic Death' (between two black curves and left of the dashed vertical line), 'Health & Aseptic Death' (below the black curve and left of the dashed vertical line), 'Aseptic & Septic Death' (between the dashed blue curve and the lower black curve, right of the dashed vertical line), 'Aseptic Death' (below the lower black curve, right of the dashed vertical line), and 'Septic Death' (above the dashed blue curve, right of the dashed vertical line).::>

<a id='fc7a783e-f4d5-4236-a024-8e8f3244f0cb'></a>

Fig. 4. Bifurcation diagrams for the three-variable subsystem. (a) Bifurcation diagram for kpg with CA = 0.2. Health and aseptic death both lose stability through transcritical bifurcations, at kpg = 1.5 and 2.769, respectively. The emerging stable states correspond to non-physiological states and are not shown. At kpg = 1.702 there is a saddle-node bifurcation giving rise to two additional fixed points that are both initially unstable. However, at kpg = 1.707, a Hopf bifurcation creates a stable state, which corresponds to septic death. Therefore, when kpg <1.5, there is bistability between health and aseptic death; for 1.5<kpg<1.707, aseptic death is the only stable state; there is bistability between aseptic and septic death for 1.707<kpg<2.769; and septic death is the only stable state for kpg>2.769. (b) Two-parameter bifurcation diagram generated by following the Hopf, saddle node, and transcritical bifurcations from (a). The black solid curve represents the onset of stable septic death. The diamond again represents the switch from a Hopf (below) to a saddle node (above) bifurcation. Each region is labeled by the possible stable outcomes in the corresponding parameter regime. Transcritical bifurcations are represented by dashed curves; the vertical is the loss of stable health and the blue the loss of stable aseptic death. The red, dashed, horizontal line corresponds to where the aseptic death state loses existence due to a saddle-node bifurcation as CA is increased, which is related to the saddle point seen in Fig. 3(b) from the N*/D subsystem.

<a id='fc2e5be6-4c93-4d24-ba44-8cf843ae70cd'></a>

presence of C_A decreases the ability of activated phagocytes to react to other cell types, reducing their effectiveness against the pathogen, their induction of damage, and their production of additional C_A (de Waal et al., 1991). The recruitment of C_A by tissue damage (D) is similarly

<a id='96435f2e-6a5a-4546-8881-ffd69973b073'></a>

inhibited. Further, C_A compromises all means of activation of resting phagocytes.

<a id='d5c69232-1b6d-4964-92c4-db3712d05fc7'></a>

As in the various subsystems, inhibition of activated
phagocytes by the anti-inflammatory mediator ($C_A$) is
incorporated in the model by replacing $N^*$ with $f(N^*) =$

<!-- PAGE BREAK -->

<a id='8cfd5bf1-122f-414e-be85-72fc7864ae01'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='f395842c-e469-43c6-84b9-21a6187ac074'></a>

231

<a id='ab051bd8-5cf8-4089-82bc-e4f955a23bdb'></a>

<::The image displays three sets of line graphs, labeled (a), (b), and (c), each illustrating the progression of four different biological quantities over time (Time (hours)). Each set consists of a 2x2 grid of plots. The x-axis for all plots is "Time (hours)" ranging from 0 to 200. The y-axis labels are consistent across the sets:

**Set (a):**
*   **Top-left: Pathogen (P)**
    *   Y-axis: 0.0 to 1.0
    *   The curve starts at 1.0, rapidly decreases to near 0 by approximately 50 hours, and remains near 0 thereafter.
*   **Top-right: Activated Phagocytes (N*)**
    *   Y-axis: 0.00 to 0.20
    *   The curve starts at 0.00, rises to a peak of about 0.19 at around 30 hours, then gradually declines to approximately 0.02 by 200 hours.
*   **Bottom-left: Tissue Damage (D)**
    *   Y-axis: 0 to 3.5
    *   The curve starts at 0, increases to a peak of about 3.5 at around 30-40 hours, then gradually decreases to near 0 by 200 hours.
*   **Bottom-right: Anti-Inflammatory Mediator (C_A)**
    *   Y-axis: 0.0 to 0.5
    *   The curve starts at 0.0, rapidly increases to about 0.5 by 30-40 hours, then slightly decreases to approximately 0.45 by 200 hours.

**Set (b):**
*   **Top-left: Pathogen (P)**
    *   Y-axis: 0.0 to 1.8
    *   The curve starts at approximately 1.6, rapidly decreases to near 0 by around 50 hours, and stays near 0.
*   **Top-right: Activated Phagocytes (N*)**
    *   Y-axis: 0.0 to 0.6
    *   The curve starts at 0.0, increases to about 0.3 by 50 hours, then continues to slowly increase to approximately 0.6 by 200 hours.
*   **Bottom-left: Tissue Damage (D)**
    *   Y-axis: 0 to 18
    *   The curve starts at 0, continuously increases with a decreasing slope, reaching about 17 by 200 hours.
*   **Bottom-right: Anti-Inflammatory Mediator (C_A)**
    *   Y-axis: 0.0 to 0.5
    *   The curve starts at 0.0, rapidly increases to about 0.5 by 30-40 hours, then plateaus at approximately 0.5.

**Set (c):**
*   **Top-left: Pathogen (P)**
    *   Y-axis: 0 to 8
    *   The curve starts at 1.0, rapidly increases to a peak of about 7.8 at around 15 hours, then slowly decreases and plateaus around 5.0 by 200 hours.
*   **Top-right: Activated Phagocytes (N*)**
    *   Y-axis: 0.0 to 1.0
    *   The curve starts at 0.0, rapidly increases to about 0.95 by 50 hours, then plateaus at approximately 0.98.
*   **Bottom-left: Tissue Damage (D)**
    *   Y-axis: 0 to 18
    *   The curve starts at 0, continuously increases with a decreasing slope, reaching about 17.5 by 200 hours.
*   **Bottom-right: Anti-Inflammatory Mediator (C_A)**
    *   Y-axis: 0.0 to 0.5
    *   The curve starts at 0.0, rapidly increases to about 0.5 by 30-40 hours, then plateaus at approximately 0.5.
: chart::>

<a id='fbcb79db-0014-432f-a962-35718d066682'></a>

Fig. 5. Transients from the evolution of the reduced model. (a) Healthy outcome, with kpg = 0.3/h and initial conditions P = 1, N* = 0, D = 0, and CA=0.125. (b) Aseptic death, with kpg = 0.3 and initial conditions P = 1.5, N* = 0, D = 0, and CA = 0.125. (c) Septic death, with kpg = 0.6, such that septic death is a possible outcome, and initial conditions P = 1, N* = 0, D = 0, and CA = 0.125.

<!-- PAGE BREAK -->

<a id='4b3df897-a24e-4036-8aa0-6787a1853303'></a>

232

<a id='86c1062f-9e6b-45da-84e2-7c70a1e53e4e'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220-236

<a id='79c45fba-5381-4f04-a7f0-c5ffa5fbb76a'></a>

N*/(1+(CA/C)²) in Eqs. (6) and (8). The inhibition of the activation of resting phagocytes is modeled by replacing R3 with R = f(R3) = f(knnN* + knpP+kndD).
Note that f limits to zero as CA approaches infinity, and therefore if CA levels are manipulated to be sufficiently high (above the maximum reached in response to an infection), then they will correspond to nearly complete inhibition of immune activation, which is experimentally observed (D'Andrea et al., 1993).

<a id='10308b80-ee5d-4b28-926c-a4a324ab384a'></a>

The C_A equation contains a source of C_A, denoted s_c,
and a term modeling the production of anti-inflammatory
mediator from damage and activated phagocytes, which
takes the form k_cn(N* + k_cndD)/(1 + N* + k_cndD), before
inhibition is incorporated. This expression is a Michae-
lis–Menten-type term, in which k_cnd controls the effective-
ness of damage, relative to activated phagocytes, in
producing C_A. Including inhibition in this term, we obtain
k_cnf(N*+k_cndD)/(1+f(N* + k_cndD)).

<a id='891edc13-bb32-41db-8444-ad8bd5117dbf'></a>

Finally, incorporating these changes and additions into
our three-variable model, Eqs. (6)-(8) result in our four-
variable model, which consists of the following:

<a id='f69dd113-a50a-4308-8043-cb9d570ac0c9'></a>

dP/dt = k_pg P (1 - P/P_∞) - k_pm s_m P / (μ_m + k_mp P) - k_pn f(N*)P, (9)
dN*/dt = s_nr R / (μ_nr + R) - μ_n N*, (10)
dD/dt = k_dn f_s(f(N*)) - μ_d D, (11)
dC_A/dt = s_c + k_cn f(N* + k_cnd D) / (1 + f(N* + k_cnd D)) - μ_c C_A, (12)
where
R = f(k_nn N* + k_np P + k_nd D),
f(V) = V/(1 + (C_A/c_∞)²),
and
f_s(V) = V⁶/(x_dn⁶ + V⁶).

<a id='2a9ab442-ed47-49a7-8ac6-f21a81a7510c'></a>

We shall refer to Eqs. (9)-(12) as the _reduced model_,
because it describes a highly abstracted representation of
the complexity of the acute immune response. The
XPPAUT code for the reduced model and all subsystems
is included with the Supplementary Materials.

<a id='0107b365-8687-40e3-8c18-61b63e9b7950'></a>

## 3. Results

The reduced model, Eqs. (9)–(12), exhibits the same physiological fixed points as discussed above for the three- variable model. The health state is a fixed point with P = 0, N* = 0, D = 0, and CA = sc/μc. The anti-inflammatory mediator is non-zero in this state, corresponding to the background level of these cytokines that exists in healthy individuals. In aseptic death, P = 0, but N*, D, and CA are non-zero. All variables are non-zero in septic death. Model dynamics for initial conditions leading to health, or aseptic

<a id='bc696343-8f47-4466-a05b-7ead9ad3e968'></a>

and septic death are depicted in Fig. 5(a), (b), and (c),
respectively. The qualitative dependence of the existence of
stable states on the pathogen growth rate kpg is maintained
as in the three-variable model. As kpg is increased, the
septic death state comes into existence via a Saddle-node
bifurcation at kpg = 0.5137 and the aseptic death state loses
stability at kpg = 1.755, as can be seen in the bifurcation
graph presented in Fig. 6. As in the subsystems, health
loses stability at a transcritical bifurcation at kpg = 1.5. The
second branch of equilibria involved in this transcritical
bifurcation corresponds to a non-physiological state and is
not included in Fig. 6.

<a id='3b88885a-d68a-4f0f-94f1-b37e05b89546'></a>

Utilizing both the three-variable subsystem, with the anti-inflammatory mediator treated as a parameter, and the reduced model, we explore several aspects of the role of C$_A$: (1) we investigate the effects of allowing C$_A$ to dynamically depend on other model variables, which we compare to results found by holding the anti-inflammatory response at various constant levels, (2) we vary parameters that govern the speed of the anti-inflammatory response, (3) we analyse the effects resulting from the presence of initially elevated or depleted C$_A$ levels when an infection is introduced, and (4) we consider the effects of reducing or elevating (resetting) C$_A$ after an infection has progressed for multiple hours and then allowing the full model to evolve, a manipulation that simulates a therapeutic intervention with an anti-inflammatory mediator.

<a id='4fd91f6c-7c0a-4b10-9f37-d4e8e992965a'></a>

We first ask whether the dynamics of the anti-inflam-
matory response are important, or whether a similar
protection against runaway inflammation is achieved by
the inclusion of a constant presence of the anti-inflamma-
tory mediator in the model. In Fig. 7, we compare the

<a id='56b75c97-e1f3-4ef5-8904-d3f7dfffaeba'></a>

<::chart: Bifurcation diagram. The x-axis is "Growth Rate of Pathogen (k_pg)" ranging from 0.0 to 3.0. The y-axis is "Activated Phagocytes (N*)" ranging from 0.0 to 1.4. The graph shows a horizontal black line around N* = 0.65, and a curve that starts around (0.5, 0.8), goes up to a peak, then turns back and merges with the horizontal line. Key points are marked: a "Saddle-node (k_pg = 0.5137)" with a blue dot around (0.5137, 0.83), and two "Transcritical" points with red dots on the horizontal line at (k_pg = 1.5) and (k_pg = 1.755). Fig. 6. Bifurcation diagram for the four-variable reduced model. Septic death comes into existence via a saddle-node bifurcation at k_pg = 0.5137/ h. Health and aseptic death lose stability by transcritical bifurcations at k_pg = 1.5 and 1.755, respectively. As in the subsystems, the emerging stable states are not shown, since they are non-physiological. For k_pg<0.5137, the model is bistable between health and aseptic death. The model has all three states stable for 0.5137<k_pg<1.5. There is bistability between aseptic and septic death for 1.5<k_pg<1.755. Finally, above k_pg = 1.755, the only stable state is septic death.::>


<!-- PAGE BREAK -->

<a id='686a6fce-c3f0-4b81-86db-1a06f70bb875'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='c0375785-57e5-403b-bda3-c090cfde862f'></a>

233

<a id='031b30be-ddd2-46a9-a896-2f8d95f18031'></a>

<::chart: The chart shows Initial Pathogen (P_0) on the y-axis ranging from 0.0 to 1.0, and Growth Rate of Pathogen (k_pg) on the x-axis ranging from 0.0 to 1.0. Several curves are plotted, representing different C_A levels: a red solid line labeled "Dynamic" with black dots, a blue solid line labeled "C_A = 0.4" with black dots, a green solid line labeled "C_A = 0.3" with black dots, a black solid line labeled "C_A = 0.7" which has a dotted portion at higher k_pg values, a red dashed line labeled "C_A = 0.125", and a black dashed line labeled "C_A = 0". The curves generally decrease as k_pg increases. Fig. 7. The basin of attraction for the health state depends on C_A. For each constant C_A level shown, the three-variable subsystem was used to determine the level of initial pathogen (P_0) that is the threshold between health and death (aseptic or septic), over a range of k_pg. Using the reduced model, with initial conditions N* = 0, D = 0, and C_A = 0.125 and with dynamic C_A, the same was done, giving rise to the curve labeled "Dynamic". The dotted portion of the C_A = 0.7 curve (black) represents a range of k_pg where health is the only stable outcome.::>

<a id='96163c2b-b8ae-43a5-874e-1876eddd5cdf'></a>

outcomes associated with a dynamic C_A response with those found with a variety of constant levels of C_A. At different k_pg values, we determine the level of initial pathogen that is the threshold between health and death (aseptic or septic). The curve associated with C_A = 0 lies below all other curves; the presence of the anti-inflamma- tory mediator, whether dynamic or constant, allows a larger initial pathogen load or growth rate to be tolerated over all physiological (>0) values of the pathogen growth rate, k_pg. An interesting result arising from simulation of the reduced model is that a dynamic anti-inflammatory mediator is almost always more effective than constant levels of the anti-inflammatory mediator at producing a healthy outcome following infection. Indeed, the curve associated with dynamic C_A in Fig. 7 is above all other curves for most k_pg levels. The only exception is that at low growth rate (k_pg <0.307), the curve for C_A = 0.7 (very high C_A) ends and is continued by a dotted line, which crosses above the curve for dynamic C_A. In this region, with C_A=0.7, the only outcome is health, and hence the threshold between health and death is no longer defined. For infections of such low virulence, even large anti- inflammatory levels will not thwart inflammation to a degree that allows runaway infection and death. Tele- ologically, our model demonstrates that a dynamic anti- inflammatory response increases the robustness of the immune response to infection, allowing the body to recover over a broad range of pathogen growth rate, yet in a way that minimizes life-threatening tissue damage.

<a id='df88e3ee-6eae-4a78-915a-80a5fcfdb1cf'></a>

Given that a dynamic anti-inflammatory response is
advantageous, we now consider how the rate of this
response affects the overall outcome following infection.

<a id='928a4f6a-6ae7-44cb-b260-425ed912a7bf'></a>

Considering a trajectory that is in the basin of attraction of health but close to the threshold between health and death, we altered the time-scale of C_A by modifying the rate constants reflecting the production (k_cn) and decay rate (μ_c) of the anti-inflammatory mediator simultaneously. A slight increase in these rates helped the system to restore health sooner, but larger increases favored septic death. On the other hand, slowing down the anti-inflammatory dynamics causes the trajectory to proceed to aseptic death. Similar results are obtained over a broad range of pathogen growth rates.

<a id='7492be16-e26c-420b-8f8c-988ce07b86ea'></a>

Next, we use the reduced model to explore the impact of baseline anti-inflammatory mediator levels on response to infection. First, we vary the initial level of $C_A$ ($C_{A0}$) for a given initial level of pathogen ($P_0$) and determine the threshold between health and death at this $P_0$. This was repeated for multiple values of $P_0$ at fixed $k_{pg}$ values. As depicted in Fig. 8, this process defines, for each $k_{pg}$ value, a boundary between health and death illustrated by the corresponding curve. Because the local non-specific immune response in our model is not inhibited by $C_A$, the threshold between health and death cannot fall below the level of pathogen that the local response is capable of clearing, regardless of the initial levels $C_A$. Thus, a vertical asymptote, close to the $k_{pg}$ = 1 curve, is reached for large $k_{pg}$. The dotted line in Fig. 8 indicates the level of $C_{A0}$ found in the healthy state (background), call it $C_{A0}^*$. From Fig. 8, we see that the effect of $C_{A0}$ is generally stronger at lower $k_{pg}$. For such $k_{pg}$, a reduction in $C_{A0}$ from $C_{A0}^*$ moves the threshold for death to lower $P_0$. Conversely, increasing $C_{A0}$ allows the system to handle higher $P_0$. However, the changes that occur for higher $k_{pg}$, while milder, are opposite to these. Moreover, even for low $k_{pg}$, the

<a id='d3cc0fce-86a9-4a12-a70e-835e0bd0d9c9'></a>

<::chart: A 2D line plot titled "The threshold between health and death depends on the initial anti-inflammatory mediator and pathogen levels in the reduced model." The x-axis is labeled "Initial Pathogen (P₀)" and ranges from 0.0 to 2.0. The y-axis is labeled "Initial Anti-Inflammatory Mediator (C_A₀)" and ranges from 0.0 to 0.8. Six colored curves are plotted, each representing a different k_pg value: black for k_pg=1, purple for k_pg=0.6, red for k_pg=0.5, blue for k_pg=0.4, green for k_pg=0.3, and black again for k_pg=0.2. A blue dashed horizontal line is present at C_A₀ = 0.15, labeled "Background Level C_A₀". The caption states: "Fig. 8. The threshold between health and death depends on the initial anti-inflammatory mediator and pathogen levels in the reduced model. At each k_pg value indicated we find the initial C_A level that is the threshold between health and death outcomes, given that N* and D are initially at their baseline (zero) levels. Initial conditions to the left of each curve lead to health while those to the right give rise to either septic or aseptic death. The baseline level of C_A, corresponding to health in the reduced model, is indicated by the blue dashed line." :chart::>

<!-- PAGE BREAK -->

<a id='7d779e12-f94b-4cff-924f-1030c5009d6f'></a>

234

<a id='6e4af26a-b626-42d3-bb26-d8ace85b18b8'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='03ade32e-5c37-4c1d-b4ee-e25b8b88dd3e'></a>

threshold for death shifts back to lower P₀ when C_A0 is
made sufficiently large. Indeed, it appears that the back-
ground C_A level, C*_{A0}, is fairly optimally situated to allow
for maximal or near-maximal threshold P₀ for a fairly
broad range of high pathogen growth rates values, without
undue compromise of protection at lower k_pg. Interestingly,
however, this background level is not globally optimal.

<a id='f7f8e743-9ab8-4afc-ab2e-1957ac3bf31d'></a>

For solutions to the reduced model with initial condi-
tions in the basin of attraction of the health state, C_A
returns to baseline significantly later than all other
variables (Fig. 5(a)). Therefore, after an infection is
cleared, there is a period of time when only C_A is elevated,
a window of relative immune suppression. Fig. 8 allows us
to consider the effects of introducing a second infection
during this window. Although for high k_pg, the baseline
level of C_A leads to a larger basin of attraction for health
than does elevated C_A, the elevated levels of C_A found
immediately after an infection are only mildly detrimental.
At these levels, C_A offers significant protection against a
subsequent infection of a low or moderate k_pg (see also Day
et al., 2006).

<a id='d22c4521-6b49-475e-be5a-44ed64bf1da1'></a>

Multiple clinical trials have been conducted in which an anti-inflammatory mediator is administered as treatment to individuals with severe clinical sepsis (i.e. typically a highly inflamed state), where death is a frequent outcome (Annane, 2001; Marshall, 2000). To mimic treatment aimed at modulating the anti-inflammatory mediator after an initial infection, we devised an in silico experiment where an initial pathogen is injected into the reduced model, Eqs. (9)-(12). The infection is allowed to evolve for several hours at which point we instantly decrease or increase the level of C_A, to simulate a therapeutic intervention aimed at depleting or raising the availability of C_A. The simulation then proceeds according to Eqs. (9)-(12). Initially, we ran simulations where the intervention was performed at 8, 10, and 12h after pathogen injection. The results depicted in Fig. 9, obtained for the 10-h intervention, are representative of the case with moderate pathogen growth rate, where the simulation still results in health restoration, yet the solution lies near the threshold between health and aseptic death. In Fig. 9, a sufficiently small depletion of C_A (e.g. C_A = 0.24) still yields a healthy outcome, but resolution to health takes longer. More substantial depletion of C_A (e.g. C_A = 0-0.2) pushes the system to aseptic death; activated phagocytes clear the infection successfully yet are insufficiently inhibited, such that persistent collateral tissue damage results. If instead C_A values are instantly raised beyond 0.35, the simulation leads to septic death due to an excessive inhibition of activated phagocytes, which cannot mount a substantial attack on the pathogen. Therefore, over the time window explored, a modest increase in the anti-inflammatory mediator may indeed be slightly beneficial (e.g. C_A = 0.32 in Fig. 9), but it is important to prevent an overly large increase. This finding could be particularly crucial in clinical circumstances where the body cannot mount a sufficient anti-inflammatory response

<a id='52b5c1c9-4f52-40c3-a5fb-6c1e7ea05688'></a>

<::transcription of the content: chart::>The chart titled "Activated Phagocytes (N*)" on the y-axis versus "Time (Hours)" on the x-axis displays multiple curves representing the levels of activated phagocytes over time under different anti-inflammatory mediator (CA) levels. The y-axis ranges from 0.0 to 1.0, and the x-axis ranges from 0 to 140 hours. There are eight distinct curves shown, some solid and some dashed, each labeled with a CA value or "NORMAL". The caption states that after 10 hours, the anti-inflammatory mediator (CA) is either increased (dashed lines) or decreased (solid lines) without altering pathogen, activated phagocytes, and damage levels. The "NORMAL" curve (black solid line) represents the time course without manipulation of the CA level from its normal level of 0.303. Other curves are labeled by their adjusted CA levels as introduced at 10 hours. The curves are:
- NORMAL (black solid line)
- CA=0.32 (red dashed line, starting around 0.18 at 10h and decreasing to near 0.0 at 140h)
- CA=0 (black solid line, starting around 0.18 at 10h and increasing to around 0.5 at 140h)
- CA=0.12 (red solid line, starting around 0.18 at 10h and increasing to around 0.6 at 140h)
- CA=0.2 (green solid line, starting around 0.18 at 10h and increasing to around 0.48 at 140h)
- CA=0.24 (blue solid line, starting around 0.18 at 10h and decreasing to around 0.05 at 140h)
- CA=0.36 (blue dashed line, starting around 0.18 at 10h and increasing sharply to 1.0 by 70h)
- CA=0.8 (green dashed line, starting around 0.18 at 10h and increasing sharply to 1.0 by 50h)

Fig. 9. Altering the anti-inflammatory mediator levels after an infection has progressed can dramatically alter outcome. In this example, we allow an infection, triggered by an initial pathogen injection of 0.36 with kpg = 0.6/h, to progress for 10 h. After this, the anti-inflammatory mediator (CA) is increased (dashed lines) or decreased (solid lines) without altering pathogen, activated phagocytes, and damage levels. The curve labeled “NORMAL” is the time course obtained without manipulation of the CA level from its normal level of 0.303, and all other curves are labeled by their adjusted CA levels, as introduced at 10 h.<::>

<a id='a1dc0084-ea9a-4997-b3dd-f28b341e5db0'></a>

(Annane, 2001; Annane et al., 2002). In such situations, a modest transient increase in anti-inflammation mediator would change the outcome from aseptic death to health, but larger increases would be problematic.

<a id='6d759f3f-ea82-4eca-97fe-885271cbf3cd'></a>

Finally, we explored the sensitivity of these results to pathogen growth rate and timing of intervention. For larger kpg, the thresholds between health, aseptic death, and septic death are quite close together. As we raise kpg from the example in Fig. 9, we find that interventions featuring significant increases in CA continue to promote septic death, while significant decreases favor aseptic death. However, for sufficiently large kpg, aseptic death becomes less of a threat, while there is a propensity for a pathogenic explosion leading to septic death. In these cases, the removal of most or all of the CA present at the time of intervention is optimal for yielding a return to health. We note that if the delay before intervention is increased for moderate kpg, then a greater CA input is needed to avoid aseptic death, since N* builds up during the time before intervention. In cases of high kpg, excessive delays before removal of CA can eliminate their ameliorative effects by prolonging the period of insufficiently restrained pathogen growth. These results highlight further that the outcome of anti-inflammatory therapy will be highly sensitive to the nature of the infection being treated and the details of the therapeutic protocol.

<a id='507a2ae4-e224-4e68-82c4-098202501cec'></a>

## 4. Discussion

We have derived a reduced model of the acute inflammatory response to infection that includes an anti-inflammatory mediator. Simulation and bifurcation

<!-- PAGE BREAK -->

<a id='3ead9e8e-8362-4968-901c-c86faea55989'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='bd3db609-8613-4b47-afad-a816d8c4f27d'></a>

235

<a id='62e61b26-3a8c-489a-a3eb-5fc8e0d99701'></a>

analysis of this model suggest that anti-inflammation plays several important roles in the restoration of health. First, anti-inflammation expands the basin of attraction of health compared to that present in models lacking anti-inflamma- tion (Kumar et al., 2004), which is a desirable feature, given that we expect health to be a robust state. Second, we demonstrate an advantage, in terms of healthy resolution of infection, conferred by the dynamic nature of the anti- inflammatory response, in comparison to a tonic response. This advantage holds in all situations except for the mildest of infections, which, in any case, do not present a vital threat. This is illustrated in current clinical practice, where distressing symptoms associated with mild infections are alleviated by the co-administration of antibiotics and anti- inflammatory mediators. The reduced model also under- lines the importance of the different response rates of substances promoting inflammation, represented in the model by N*, and of the anti-inflammatory mediator that limit this response. Specifically, our results suggest that these rates are fairly well tuned to optimize healthy outcomes to pathogenic infection. Further, we have used simulations of our model to explore how variations in levels of the anti-inflammatory mediator present initially or at some time after initial infection affect the restoration of health following an inflammatory response.

<a id='22b32ba8-d381-454c-b961-3b1d16df2bba'></a>

We followed a systematic, modular approach to model development, building our reduced model from subsystems, each one with biologically plausible dynamics. Indeed, by building up this model through modules, we gain a clear understanding of how each element and interaction in the system contributes to the overall network dynamics. We also ensure that the final model behaves in a way that is consistent with situations in which particular features are absent, such as tissue damage without pathogen exposure, or are experimentally manipulated.

<a id='d54594fa-5140-4477-90a5-3a38c35cb28a'></a>

Our results illustrate the point that administration of an anti-inflammatory mediator during the response to an infection may compromise outcome (Fig. 9). The administration of pharmacological doses of steroids, which are potent natural anti-inflammatory mediators, in severely septic patients, has clearly resulted in worse survival (Schumer, 1976; Sprung et al., 1984). This situation corresponds in our model to either the maintenance of tonic elevated levels of the anti-inflammatory mediator or the transient administration of the anti-inflammatory mediator, in patients who would otherwise survive or evolve to aseptic death, causing septic death (Fig. 9). The association between significant immune suppression and infectious complications is clearly an ongoing concern for several groups of patients. Fortunately, the anti-inflammatory mediator, in addition to being conducive to the healing phase of injury, also plays a role in the acute phase of infection as well. A significant body of recent evidence suggests that low-dose immunosuppression with an anti-inflammatory mediator may in fact improve outcome in patients with severe infection, particularly in patients with an insufficient anti-inflammatory response (Annane, 2001;

<a id='c98458bf-064b-4fb0-962d-f13317d51884'></a>

Annane et al., 2002). Our simulations highlight the dependence of the outcomes of such interventions on pathogen virulence (Fig. 8) and timing of intervention, as discussed in the previous section. Therefore, studies such as those we have performed may be useful for subsequent investigations of anti-inflammatory therapeutic agents. For example, the only approved therapeutic agent for patients with severe sepsis, recombinant human activated Protein C, has anti-inflammatory properties (Bernard et al., 2001; Joyce and Grinnell, 2002; Nick et al., 2004) and the proper degree of modulation with this agent, alone or in combination with others, remains a very active focus of clinical research (Cross and Opal, 2003; Marshall, 2003). How the various features of the inflammatory response interact to govern the outcome following multiple insults, including pathogen, trauma, endotoxin, or other stimuli, also warrants intensive computational exploration (Day et al., 2006).

<a id='3ebeeda8-2e5a-4f19-a145-129e98974338'></a>

The biological relevance of our analysis and conclusions are limited by the significant oversimplification present in our reduced model and the difficulty in translating functions such as "pro-inflammation", "anti-inflamma- tion" and "damage" into measurable quantities. We are also involved with the development of a much larger model that directly addresses this limitation, where predictions are compared to prospectively collected experimental data (Chow et al., 2005). Such large-scale models, however, do not allow for detailed analysis, where emergent behaviors and drivers of such behavior are clearly identified and characterized. Future directions for study include a more detailed biological characterization of anti-inflammatory substances, since they differ widely in the time-scale and specificity of their activity, and a detailed mathematical analysis of the use of anti-inflammatory mediators as "therapeutic" agents, depending on time-scale as well as time and intensity of intervention. The experimental and clinical relevance of these efforts will continue to grow as methods are developed to better link reduced models and more complex models, both from top-down and bottom-up approaches.

<a id='23c3612d-608f-44f5-a14d-20014621e5cc'></a>

### Acknowledgments

This work was partial supported by NIH Award R01-GM67240.

<a id='5cf453fd-8c2c-456b-b3fc-20b8729bc856'></a>

## Appendix A. Supplementary materials

Supplementary information associated with this article can be found in the online version at [doi:10.1016/j.jtbi.2006.02.016](https://doi.org/10.1016/j.jtbi.2006.02.016).

<a id='08529d70-6ecb-442f-86c4-dbed7831ef0d'></a>

References
Andersson, U., Wang, H., Palmblad, K., Aveberger, A.C., Bloom, O.,
Erlandsson-Harris, H., Janson, A., Kokkola, R., Zhang, M., Yang,

<!-- PAGE BREAK -->

<a id='a250c6b6-6d9d-45c9-85eb-d6e93dd52cfd'></a>

236

<a id='e6dd8ec1-8a5c-4c9f-ae5f-5726b3741edc'></a>

A. Reynolds et al. / Journal of Theoretical Biology 242 (2006) 220–236

<a id='cf9ef4d8-c2b7-466a-ac01-ea85c5f64be3'></a>

H., Tracey, K.J., 2000. High mobility group 1 protein (HMG-1) stimulates proinflammatory cytokine synthesis in human monocytes. J. Exp. Med. 192, 565–570.
Annane, D., 2001. Corticosteroids for septic shock. Crit. Care Med. 29, 117–120.
Annane, D., Sebille, V., Charpentier, C., Bollaert, P.E., Francois, B., Korach, J.M., Capellier, G., Cohen, Y., Azoulay, E., Troche, G., Chaumet-Riffaut, P., Bellissant, E., 2002. Effect of treatment with low doses of hydrocortisone and fludrocortisone on mortality in patients with septic shock. JAMA 288, 862–871.
Bacon, G.E., Kenny, F.M., Murdaugh, H.V., Richards, C., 1973. Prolonged serum half-life of cortisol in renal failure. Johns Hopkins Med. J. 132, 127–131.
Bernard, G.R., Vincent, J.L., Laterre, P.F., LaRosa, S.P., Dhainaut, J.F., Lopez-Rodriguez, A., Steingrub, J.S., Garber, G.E., Helterbrand, J.D., Ely, E.W., Fisher Jr., C.J., 2001. Efficacy and safety of recombinant human activated protein C for severe sepsis. N. Engl. J. Med. 344, 699–709.
Bocci, V., 1991. Interleukins. Clinical pharmacokinetics and practical implications. Clin. Pharmacokinet. 21, 274–284.
Branwood, A., Noble, K., Schindhelm, K., 1992. Phagocytosis of carbon particles by macrophages in vitro. Biomaterials 19, 646–648.
Chow, C.C., Clermont, G., Kumar, R., Lagoa, C., Tawadrous, Z., Gallo, D., Betten, B., Bartels, J., Constantine, G., Fink, M.P., Billiar, T.R., Vodovotz, Y., 2005. The acute inflammatory response in diverse shock states. Shock 24, 74–84.
Coxon, A., Tang, T., Mayadas, T.N., 1999. Cytokine-activated endothelial cells delay neutrophil apoptosis in vitro and in vivo. A role for granulocyte/macrophage colony-stimulating factor. J. Exp. Med. 190, 923–934.
Cross, A.S., Opal, S.M., 2003. A new paradigm for the treatment of sepsis: is it time to consider combination therapy? Ann. Intern. Med. 138, 502–505.
D'Andrea, A., ste-Amezaga, M., Valiante, N.M., Ma, X., Kubin, M., Trinchieri, G., 1993. Interleukin 10 (IL-10) inhibits human lymphocyte interferon gamma-production by suppressing natural killer cell stimulatory factor/IL-12 synthesis in accessory cells. J. Exp. Med. 178, 1041–1048.
Day, J., Rubin, J., Vodovotz, Y., Chow, C.C., Reynolds, A., Clermont, G., 2006. A reduced mathematical model of the acute inflammatory response II. Capturing scenarios of repeated endotoxin administration. J. Theor. Biol., in press.
de Waal, M.R., Abrams, J., Bennett, B., Figdor, C.G., de Vries, J.E., 1991. Interleukin 10(IL-10) inhibits cytokine synthesis by human monocytes: an autoregulatory role of IL-10 produced by monocytes. J. Exp. Med. 174, 1209–1220.
Ermentrout, G.B., 2002. Simulating, Analyzing, and Animating Dynamical Systems: A Guide to XPPAUT for Researchers and Students, first ed. Society for Industrial & Applied Mathematics, Philadelphia.
Fuchs, A.C., Granowitz, E.V., Shapiro, L., Vannier, E., Lonnemann, G., Angel, J.B., Kennedy, J.S., Rabson, A.R., Radwanski, E., Affrime, M.B., Cutler, D.L., Grint, P.C., Dinarello, C.A., 1996. Clinical, hematologic, and immunologic effects of interleukin-10 in humans. J. Clin. Immunol. 16, 291–303.
Goris, R.J., te Boekhorst, T.P., Nuytinck, J.K., Gimbrere, J.S., 1985. Multiple-organ failure. Generalized autodestructive inflammation? Arch. Surg. 120, 1109–1115.
Huhn, R.D., Radwanski, E., Gallo, J., Affrime, M.B., Sabo, R., Gonyo, G., Monge, A., Cutler, D.L., 1997. Pharmacodynamics of subcutaneous recombinant human interleukin-10 in healthy volunteers. Clin. Pharmacol. Ther. 62, 171–180.
Isler, P., de Rochemonteix, B.G., Songeon, F., Boehringer, N., Nicod, L.P., 1999. Interleukin-12 production by human alveolar macrophages

<a id='79aecc2a-a422-472f-bf96-1579a1a3a710'></a>

is controlled by the autocrine production of interleukin-10. Am. J. Respir. Cell Mol. Biol. 20, 270–278.
Janeway Jr., C.A., Medzhitov, R., 2002. Innate immune recognition. Annu. Rev. Immunol. 20, 197–216.
Janeway Jr., C.A., Travers, P., Walport, M., Shlomchik, M., 2001. Immunobiology: The Immune System in Health and Disease, fifth ed. Garland Publishing, New York.
Joyce, D.E., Grinnell, B.W., 2002. Recombinant human activated protein C attenuates the inflammatory response in endothelium and monocytes by modulating nuclear factor-kappaB. Crit. Care Med. 30, S288–S293.
Kumar, R., Clermont, G., Vodovotz, Y., Chow, C.C., 2004. The dynamics of acute inflammation. J. Theor. Biol. 230, 145–155.
Marshall, J.C., 2000. Clinical trials of mediator-directed therapy in sepsis: what have we learned? Intensive Care Med. 26 (Suppl. 1), 75–83.
Marshall, J.C., 2003. Such stuff as dreams are made on: mediator-directed therapy in sepsis. Nat. Rev. Drug Discov. 2, 391–405.
Nick, J.A., Coldren, C.D., Geraci, M.W., Poch, K.R., Fouty, B.W., O'Brien, J., Gruber, M., Zarini, S., Murphy, R.C., Kuhn, K., Richter, D., Kast, K.R., Abraham, E., 2004. Recombinant human activated protein C reduces human endotoxin-induced pulmonary inflammation via inhibition of neutrophil chemotaxis. Blood 104 (13), 3878–3885.
Ochsenbein, A.F., Zinkernagel, R.M., 2000. Natural antibodies and complement link innate and acquired immunity. Immunol. Today, 21, 624–630.
Paulsen, F., Pufe, T., Conradi, L., Varoga, D., Tsokos, M., Papendieck, J., Petersen, W., 2002. Antimicrobial peptides are expressed and produced in healthy and inflamed human synovial membranes. J. Pathol. 198, 369–377.
Raj, P.A., Dentino, A.R., 2002. Current status of defensins and their role in innate and adaptive immunity. FEMS Microbiol. Lett. 206, 9–18.
Schumer, W., 1976. Steroids in the treatment of clinical septic shock. Ann. Surg. 184, 333–341.
Spector, W.S. (Ed.), 1956. Handbook of Biological Data. W.B. Saunders Company, London.
Sprung, C.L., Caralis, P.V., Marcial, E.H., Pierce, M., Gelbard, M.A., Long, W.M., Duncan, R.C., Tendler, M.D., Karpf, M., 1984. The effects of high-dose corticosteroids in patients with septic shock. A prospective, controlled study. N. Engl. J. Med. 311, 1137–1143.
Strogatz, S.H., 1994. Nonlinear Dynamics and Chaos: With Application to Physics, Biology, Chemistry, and Engineering. Westview Press, Cambridge.
Stvrtinova, V., Jakubovsky, J., Hulin, I., 1995. The acute phase reactants. Inflammation and Fever. Academic Electronic Press.
Takala, A., Jousela, I., Jansson, S.E., Olkkola, K.T., Takkunen, O., Orpana, A., Karonen, S.L., Repo, H., 1999. Markers of systemic inflammation predicting organ failure in community-acquired septic shock. Clin. Sci. (London) 97, 529–538.
Todar, K., 2002. Growth of bacterial populations. In: Todar's Online Textbook of Bacteriology. Date Accessed: 10-21-2005. http://www.textbookofbacteriology.net.
Tsukaguchi, K., de, L.B., Boom, W.H., 1999. Differential regulation of IFN-gamma, TNF-alpha, and IL-10 production by CD4(+) alphabetaTCR + T cells and vdelta2(+) gammadelta T cells in response to monocytes infected with Mycobacterium tuberculosis-H37Ra. Cell Immunol. 194, 12–20.
Wang, H., Bloom, O., Zhang, M., Vishnubhakat, J.M., Ombrellino, M., Che, J., Frazier, A., Yang, H., Ivanova, S., Borovikova, L., Manogue, K.R., Faist, E., Abraham, E., Andersson, J., Andersson, U., Molina, P.E., Abumrad, N.N., Sama, A., Tracey, K.J., 1999. HMG-1 as a late mediator of endotoxin lethality in mice. Science 285, 248–251.
Zouali, M., 2001. Antibodies. In: Encyclopedia of Life Science. Nature Publishing Group. Date Accessed: 8-18-2005. www.els.net.
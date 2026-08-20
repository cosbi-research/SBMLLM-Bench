<a id='7b2dd188-9722-4db4-bb41-35ab50526dee'></a>

Biomedical Signal Processing and Control 3 (2008) 212-219

<a id='0b6d4248-bae7-406f-a5cb-c71537c0845b'></a>

<::logo: Elsevier
NON SOLUS
The logo features an orange-colored tree with a person standing under it, and the brand name "ELSEVIER" in orange below the image.::>

<a id='0bc90093-9296-4c76-a8e9-bf8edc380b88'></a>

Contents lists available at ScienceDirect

<a id='f89e5829-dc01-481d-abe2-eae63d893a62'></a>

Biomedical Signal Processing and Control

<a id='8911d704-3bae-4ab1-95ce-4d1b08c4467e'></a>

journal homepage: www.elsevier.com/locate/bspc

<a id='60cb3d1d-df74-4613-b150-7fceb2c88925'></a>

<::logo: [Elsevier] Biomedical Signal Processing and Control. A red square with white text and a white signal waveform pattern.::>

<a id='0411eb10-757b-40ee-95b5-1b4d70b0ec85'></a>

An insight into tumor dormancy equilibrium via the analysis of its domain of attraction

<a id='e0f27490-5d97-4626-8152-f3c0cef4749d'></a>

A. Merola, C. Cosentino *, F. Amato
School of Computer and Biomedical Engineering, Università degli Studi Magna Græcia di Catanzaro, Campus "Salvatore Venuta", 88100 Catanzaro, Italy

<a id='85c7d3eb-cc84-4a11-b61a-29494f577fae'></a>

ARTICLE INFO

Article history:
Received 12 October 2007
Received in revised form 11 January 2008
Accepted 18 February 2008
Available online 14 April 2008

---

Keywords:
Domain of attraction
Linear matrix inequalities
Quadratic systems
Tumor-immune system competition
dynamics

<a id='ee57fb7a-17d9-44ad-b1c9-d3ea84620927'></a>

ABSTRACT

The trajectories of the dynamic system which regulates the competition between the populations of malignant cells and immune cells may tend to an asymptotically stable equilibrium in which the sizes of these populations do not vary, which is called tumor dormancy. Especially for lower steady-state sizes of the population of malignant cells, this equilibrium represents a desirable clinical condition since the tumor growth is blocked. In this context, it is of mandatory importance to analyze the robustness of this clinical favorable state of health in the face of perturbations. To this end, the paper presents an optimization technique to determine whether an assigned rectangular region, which surrounds an asymptotically stable equilibrium point of a quadratic systems, is included into the domain of attraction of the equilibrium itself. The biological relevance of the application of this technique to the analysis of tumor growth dynamics is shown on the basis of a recent quadratic model of the tumor-immune system competition dynamics. Indeed the application of the proposed methodology allows to ensure that a given safety region, determined on the basis of clinical considerations, belongs to the domain of attraction of the tumor blocked equilibrium; therefore for the set of perturbed initial conditions which belong to such region, the convergence to the healthy steady state is guaranteed. The proposed methodology can also provide an optimal strategy for cancer treatment.

3000 PTF A 111

<a id='c3519662-30c2-4456-a67b-c410d18e5d54'></a>

&#169; 2008 Elsevier Ltd. All rights reserved.

<a id='905dee58-8414-447a-9f0b-74c97e6fa53f'></a>

# 1. Introduction

In the last 20 years many papers have dealt with the problem of devising reliable dynamical models of tumor development. The works [1,2] provide a comprehensive overview of the different approaches used in the modelling of the tumor-immune system interaction dynamics. Several papers (see for example [3-11]) make use of Lotka-Volterra terms and Verhulst (logistic) terms for describing the interactions between malignant and normal (immune) cells. In particular, the work [6] analyzes the different types of models of tumor growth (both empirical and functional) in their attitude to retrieve some biologically relevant information from experimental data sets of multicell tumor spheroid. Moreover, it is demonstrated that the functional models of competing populations (like as Lotka-Volterra-based models), in which tumor growth dynamics is explained in terms of competition between malignant and normal cells, allow to reveal the role of the cell-cell interactions in growth regulation of tumors and then in tumor remission. In spite of their simple formulation, Lotka-Volterra models of tumor growth can describe the different dynamics of the cancer development, such

<a id='c9eb4a06-6469-4ea0-bccf-c767fb80d019'></a>

*Corresponding author. Tel.: +39 0961 369 4196; fax: +39 0961 369 4090.
E-mail address: merola@unicz.it (A. Merola), carlo.cosentino@unicz.it
(C. Cosentino), amato@unicz.it (F. Amato).

<a id='e1c27d81-05b5-4a6e-8bd1-398f74423a39'></a>

1746-8094/$ – see front matter © 2008 Elsevier Ltd. All rights reserved.
doi:10.1016/j.bspc.2008.02.001

<a id='ce17c1f0-a6aa-4644-9b32-3d133f2fcadb'></a>

as: (a) unbounded growth which leads to an uncontrolled tumor; (b)
steady-state condition in which the populations of normal and
malignant cells coexist and their sizes do not vary (said tumor
dormancy); (c) cyclic profiles of the size of the tumor cells population
(tumor recurrence); (d) steady state of tumor eradication due to the
action of the immune response (tumor remission). The cases (b) and
(d) represent desirable clinical conditions since in these equilibria
the population size of tumor cells can be constrained to low or null
values. Lotka-Volterra formulation allows to describe the growth
dynamics of homogeneous tumors, as well as that of heterogenous
tumors [12-15]. The work [16] shows that Lotka-Volterra models
also provide a good fitting of the decelerating pattern of tumor
growth detected in clinical data.

<a id='127bb412-298e-4e41-b45b-53405c590184'></a>

In the literature about the modeling of tumor growth dynamics, the analysis of the equilibrium points, the bifurcation diagrams and the inspection of the phase plane represent the more assessed tools used for the prediction of the outcome of the disease. In particular, the papers [3,4,17,18] analyze how the phase plane changes for different values of the model parameters. The phase plane inspection allows to identify some conditions on the parameters which are critical for tumor growth. For example, in [18], it is shown that, by modifying the values of some model parameters, the domain of attraction (DA) of the tumor-free equilibrium can be enlarged. The determined DA represents a safety region since, for any initial

<!-- PAGE BREAK -->

<a id='8ff54db8-f72f-4655-af1b-c0931b0ba008'></a>

A. Merola et al./Biomedical Signal Processing and Control 3 (2008) 212–219

<a id='782f59ed-9d00-4fca-aa18-0d28fb0cfb22'></a>

213

<a id='ecdc1c56-41c3-49b8-875e-f51ed0850f28'></a>

condition included in such region, the tumor is annihilated by the immune response. In [17], the phase plane inspection helps to evaluate the effectiveness of a chemotherapeutic treatment.

<a id='28b8fee0-eaf4-40bf-b0ee-44a0a5870898'></a>

In this paper we focus on the dynamical model of tumor growth provided in the recent paper [10], where the impact that random fluctuations, due to high temperature, radiation, etc., have on the nature of the equilibrium point is investigated. The model proposed in [10] has three equilibrium points, two unstable (say E₁ and E₂) and one asymptotically stable (say E₃). E₁ and E₂ corresponds to an unbounded tumor growth, while E₃ corresponds to a fixed (steady-state) density of malignant cells which can be considered safe for the patient. Roughly speaking, the main result of the paper shows that, under the influence of sufficiently strong stochastic fluctuations, E₃ may become unstable.

<a id='f06ddad4-49eb-4d04-bb83-14566fb7ba3b'></a>

In our paper, rather than focusing on such kind of 'stochastic robustness' of E3, we are interested in studying the robustness of E3 directly in terms of state perturbations. Indeed it is important from a clinical point of view to determine whether, under a given perturbation of the state variables, the system trajectories go back to E3. In particular, our goal is to determine whether a given neighborhood of E3 belongs to its DA.

<a id='af3cf0da-537e-4d9e-a4f3-21e56ba43249'></a>

The model considered in [10] turns out to be quadratic in the state variables. The literature on quadratic systems is fairly vast, since they provide an appropriate tool for modeling phenomena in a wide range of applications, either in engineering (electrical power systems, chemical reactors, robots), or in other areas such as ecology and economics. In particular, quadratic models are widely used for describing the behavior of biological systems, where the quadratic terms naturally arise when considering, for example, biochemical phenomena (e.g. from the law of mass action) or prey-predator-like interactions between multispecies populations. Population ecology theory applied to modeling of tumor growth dynamics yields ordinary differential equations (ODE) quadratic systems, since these models generally make use of Lotka-Volterra terms which are quadratic [4-6,13-15,19]. Some quadratic models of tumor dynamics are also obtained within the framework of other theories. For example, a kinetic modeling approach is used in [18,20]. When dealing with such systems it is of primary interest to determine what happens when a (voluntary or undesired) perturbation is injected in the system, moving the trajectory away from an equilibrium point.

<a id='1c09f5cf-c403-4077-94c7-b21ebb5a3649'></a>

Over the years, several papers have focused on the estimation of the DA of the zero equilibrium point of nonlinear (quadratic, cubic and, more in general, polynomial) autonomous systems. In [21] a Lyapunov-based procedure is proposed to compute an ellipsoidal estimate of the DA of a second order nonlinear system containing either linear and quadratic or linear and cubic terms. For general n th order systems, some gridding techniques have been employed in [22-24]; however, since these methods are computationally heavy, this kind of approach is practically applicable only to low order systems. An alternative way to obtain an estimate of the DA, based on topological considerations, is provided in [25,26]. More recently, the problem of determining the DA of polynomial systems has been solved by recasting it as a linear matrix inequalities (LMIs) feasibility problem [27-30].

<a id='0d67bc91-8f60-4bd0-bd1c-eea0c07463c9'></a>

In the above cited papers, the problem is tackled by means of a two-steps procedure: (i) choice of a quadratic Lyapunov function, which proves local asymptotic stability of the equilibrium; (ii) computation of the estimate of the DA associated to that particular Lyapunov function. However, the choice of the optimal Lyapunov function is not a trivial task and may severely affect the conservatism of the estimate. In particular, in [23] it is shown that the computation of the quadratic Lyapunov function which maximizes the volume of the estimate of the DA requires solving a double non-convex optimization problem; a sub-optimal procedure, based on the solution of a semi-convex problem, is proposed in [31].

<a id='d0b9280b-3dea-498c-9efb-5502855272ec'></a>

The exact determination of the whole DA of the zero equilibrium point of a quadratic system is a difficult or even impossible task (except for very simple cases); moreover it is not the primary interest in the context of the problem we deal with in this paper. Therefore we propose an approach to solve the more practical problem of determining whether an assigned box, determined on the basis of clinical considerations, belongs to the DA of the equilibrium E3 of the model developed in [10].

<a id='1f1321c5-d1c8-402e-aa5e-f1d880be6b61'></a>

Our approach improves the existing literature in many ways. First of all it can be exploited regardless of the system order, while most of the previous papers dealing with the analysis of tumor growth dynamics (see for example [3,4,17,18]) were based on phase plane methodologies which are limited to second order systems. Another fundamental point is that our methodology optimizes over the whole set of quadratic Lyapunov functions, thus reducing the conservatism of the previous approaches which, as said, worked with a fixed Lyapunov function. The proposed technique requires the solution of a generalized eigenvalue problem (GEVP) [32], for which efficient numerical optimization routines exist [33]. Finally, our approach can also be used to design an optimal strategy for cancer therapy in order to _guarantee_ that a given rectangular region of the state space belongs to the DA of E3.

<a id='9c12b266-9a83-45f8-bb6f-ce9abbefed7d'></a>

The paper is organized as follows: In Section 2, the model describing the tumor development provided in [10] is presented; in Section 3, a general methodology for testing whether an assigned box surrounding the equilibrium point of a quadratic system belongs to the DA of the equilibrium itself is illustrated; in Section 4, the proposed methodology is applied to study the properties of the asymptotically stable equilibrium point corre- sponding to a blocked-growth tumor behavior. Finally some concluding remarks are given in Section 5.

<a id='0400fff4-2a21-4354-b24a-1fdf059b0102'></a>

## 2. A prey–predator model for cancer development

In this section, we introduce the quadratic model of the tumor growth developed in [10] and state precisely the problem we deal with in the paper. In such model, the tumor progression is described by means of a prey–predator system. Malignant cells are modelled as a prey-population which competes against the predator-population of healthy cells within the environment of the organic tissues.

<a id='c3097a69-f775-4f76-b4f6-427c2ed6fe9e'></a>

The population of predators consists of the cells which perform the immune response against the tumor, such as T-lymphocytes, macrophages and natural killer cells; these cells engulf and neutralize malignant cells. T-lymphocytes are divided into two categories: regulatory and cytotoxic. In the regulatory form, said *helper*, T-lymphocytes organize the attack against the tumor cells, despite they do not actively participate to the elimination of the malignant cells. In particular, they are able to stimulate the growth of the population of several types of predator cells (e.g. macrophages and cytotoxic T-lymphocytes). Moreover, predator cells are present in the body in two forms: hunting and resting. For example, the cytotoxic T-lymphocytes in the resting form can become active predators (cytotoxic cells) when a helper T-cell sends the activation signal.

<a id='86749ce6-79b6-4925-bf1c-d19e513aa0d8'></a>

Thereby, the cited model contains three state variables: the
density of tumor cells M, the density of hunting predator cells N,
and the density of resting predator cells Z. The system model is

<a id='14d13d60-e19e-41e8-b62d-b954343b29a7'></a>

{Ṁ = q + rM (1 - M/k₁) - αMN,
Ṅ = βNZ - d₁N,
Ż = sZ (1 - Z/k₂) - βNZ - d₂Z,
(1)

<a id='09c7c16b-df28-4cac-be13-70dda8d82f62'></a>

where r is the growth rate of the tumor cells, q is the rate of
conversion of the normal cells to the malignant ones, ̑ is the rate of

<!-- PAGE BREAK -->

<a id='46c23108-6d8a-4cd7-8476-7ced0fccca08'></a>

214

<a id='8e0a1831-60c7-44ee-9d89-e57bd8b12d91'></a>

A. Merola et al. / Biomedical Signal Processing and Control 3 (2008) 212-219

<a id='b79c07f4-701c-409f-815c-01a50a584d71'></a>

predation of the tumor cells by the hunting cells, β is the rate of conversion of the resting cells to the hunting cells, d₁ is the natural death of the hunting cells, s is the growth rate of the resting predator cells, d₂ is the natural death of the resting cells, k₁ is the maximum carrying or packing capacity of the tumor cells, k₂ is the maximum carrying capacity of the resting cells. All these parameters are positive. In particular, for each population, k₁ and k₂ (k₁ > k₂) represent the maximum number of cells that the environment could carry in absence of competition between these populations.

<a id='09ed3f02-96d3-40dc-9502-80020e1f0dee'></a>

Note that in (1) the dynamics of the tumor-immune system interactions are described using a quadratic formulation. Indeed, for tumor cells and resting predator cells, the growth is modelled by adopting both the Lotka–Volterra and logistic terms [34]. In general, the logistic growth factor is defined as

<a id='7f304778-f30a-4dd2-ae92-eae219488951'></a>

R(x) = r(1 - x/f), (2)

<a id='0dfaf298-228d-4d9f-84fd-9d760c0190cd'></a>

where x is the number of individuals of the population, r and f are positive constants. For a given population, r is the intrinsic growth factor and f is the maximum number of individuals that can cohabit in the same environment such that each individual finds the necessary quantity of resources for surviving. From (2), note that the increase of the growth factor is thwarted by the rise of individuals for population. Also other works in the literature, as [3-11], present ordinary differential equations models in which the tumor growth is described using logistic terms. Indeed, several clinical tests on measurable tumors confirm that, at higher tumor density, the growth increases more slowly.

<a id='aca25831-b198-478e-abcc-da62b55300ba'></a>

2.1. Stability properties of the equilibrium points

System (1) has three equilibrium points:

$E_1 = [\frac{k_1}{2} (1 + \sqrt{1 + \frac{4q}{rk_1}}), 0, 0]$, (3a)

$E_2 = [\frac{k_1}{2} (1 + \sqrt{1 + \frac{4q}{rk_1}}), 0, k_2(1 - \frac{d_2}{s})]$, (3b)

$E_3 = [M^*, \frac{s}{\beta} (1 - \frac{d_1}{\beta k_2}) - \frac{d_2}{\beta}, \frac{d_1}{\beta}]$, (3c)

<a id='2dfafbf1-18a2-48ab-ba50-276d11aa1e7d'></a>

where
M* = -[((αs/β)(1 - (d₁/βk₂)) - (αd₂/β) - r)] + √[((αs/β)(1 - (d₁/βk₂)) - (αd₂/β) - r)² + (4rq/k₁)] / 2(r/k₁)

(4)

<a id='ac2b54e2-4442-4de3-a2dd-e818398a6da4'></a>

These equilibrium points are biologically admissible if they belong to the positive orthant. From (3a), we note that in correspondence of the equilibrium E₁ only malignant cells are present. This equilibrium point always belongs to the positive orthant since the system parameters are positive. Both malignant cells and resting predator cells are present in the organism in correspondence of the equilibrium point E₂. Finally, when the system trajectories are around the equilibrium E₃, the three species of cells are all present. To guarantee biological admissibility of the equilibria E₂ and E₃, it is needed that s > d₂ in (3b) and

<a id='730e082f-79ab-4c4c-b98d-3ae44a39608d'></a>

β > sd₁ / k₂(s - d₂)                                (5)
in (3c), respectively.

<a id='ccd31e4d-f0b1-499c-8782-b5b1d6a20f41'></a>

Concerning the stability properties of these equilibrium points, as shown in [10] the first equilibrium point is always unstable because the values of the system parameters are all positive. If the equilibria E₁ and E₂ belong to the positive orthant and E₃ does not, E₂ is an asymptotically stable equilibrium point. Finally, if also E₃ belongs to the positive orthant, E₂ is unstable and E₃ is asymptotically stable.

<a id='8875ea9e-0696-415b-a29e-a961e127a9ed'></a>

An asymptotically stable equilibrium point corresponds to a favorable condition from the clinical point of view, since it represents a blocked-growth tumor in which the density of malignant cells does not vary.

<a id='18bae25b-2e40-4e65-832f-d1b922d82738'></a>

Moreover, when E3 belongs to the positive orthant, it is possible to decrease the steady-state density of the malignant cells by varying the rate of destruction of the tumor cells by the hunting cells (system parameter α). In addition, by comparing the density of the malignant cells in the equilibrium points E3 and E2, it is possible to verify that, if

<a id='d08d848e-05ec-474d-b740-edca590dc7c7'></a>

$$\alpha < \frac{2r\beta}{s(1 - (d_1 / \beta k_2)) - d_2}, \quad (6)$$

<a id='0b503974-b72e-467e-a2be-c47f6034b141'></a>

the density of malignant cells in E3 is lower than in E2.
There is a biological interpretation for the equilibrium points E2
and E3 lying in the positive orthant. In particular, if only E2 belongs
to the positive orthant, a mechanism able to convert resting
predator cells to hunting predator cells does not exist. Conversely,
when E3 belongs to the positive orthant it is possible to control the
steady-state density of the tumor by varying a.

<a id='a501e23e-68eb-4240-88cb-5c82bcc41a9e'></a>

In the light of the properties of the equilibrium E3, it is desirable to compute a safety region around E3 such that, for the set of perturbed initial conditions starting from this region, the state trajectory tends to the favorable clinical condition, that is the steady-state E3.

<a id='f9aa92d9-4bf2-498d-9624-6bb1ad2ebc3e'></a>

To this aim the optimization procedure presented here allows
to determine whether an assigned rectangular region in the state
space, defined on the basis of clinical considerations, is included
into the DA of E3.

<a id='193ece11-a332-4fea-a3a6-3cfaeaac75f6'></a>

In general, the goal of a therapy should be that of leading the system evolution from a given range of initial cells concentrations into the DA of an asymptotically stable equilibrium in which the tumor cells concentration is null (tumor remission) or, at least, low as in the case of E3. Indeed, for the considered model, the proposed approach also allows to devise an optimal strategy for cancer therapy such that a given range of concentrations belongs to the DA of E3.

<a id='7fc67487-c9ec-4f63-90e7-4de986adeb85'></a>

In [11,35], it has been shown that the new protocols for cancer treatment, which make use of vaccines and immunotherapy, are able to control (or block) the tumor growth by modifying some critical parameters of the dynamical system that regulates the interactions between tumor cells and immune cells. Immunotherapy consists of the administration of therapeutic antibodies as drugs which can render immune cells stronger and therefore able to kill more tumor cells.

<a id='fbfc316e-a275-47ec-906a-5c31a526c82c'></a>

Therefore, in the following, we shall assume to be able to regulate the immunotherapeutical action in the model (1), by varying the value of the parameter \alpha. For purposes of cancer therapy planning, an optimal value of \alpha will be determined which is able to ensure a safe rectangular region, as defined, around E3.

<a id='9d47f2f0-1503-4219-ad95-d4bc2b43e0ad'></a>

3. **A procedure to check whether an assigned box belongs to the domain of attraction of the equilibrium**

In this paper we consider a quadratic system, that is a nonlinear system in the form

_x_ = _Ax_ + _B_(_x_), (7)

<!-- PAGE BREAK -->

<a id='5eda986e-4f25-4ad2-b9c2-2871d8923061'></a>

A. Merola et al./Biomedical Signal Processing and Control 3 (2008) 212–219

<a id='7f5afa99-629d-4fb5-a2b0-4edaa51bf526'></a>

215

<a id='9664974c-ec01-47cb-b245-417752661e55'></a>

where x ∈ Rⁿ is the system state and

<a id='53f719f2-3de7-4756-a932-878319742b5e'></a>

$$B(x) = \begin{pmatrix} x^T B_1 x \\ x^T B_2 x \\ \vdots \\ x^T B_n x \end{pmatrix} \quad (8)$$with $B_i \in \mathbb{R}^{n \times n}$, $i = 1,...,n.$

<a id='10b57bf0-446e-45a5-9315-5b3f1caf6e5a'></a>

First note that the study of the stability properties of a nonzero equilibrium point of system (7) can be always reduced to the study of the corresponding properties of the origin of the state space of another quadratic system by applying a suitable change of variable. Indeed assume that xₑ ≠ 0 is an equilibrium point for system (7), then

<a id='c0e64fb1-f8fa-41cb-b9f6-2ba53d52d20c'></a>

Axe + B(xe) = 0.

<a id='b15511e3-b863-4efe-807b-37f685c92500'></a>

Now let

<a id='0827c96f-4679-4450-b4e8-72f6a7dc35ba'></a>

Z = X - X_e;

<a id='a026dd82-c501-45d9-a6dd-504e4d8b2dc9'></a>

it is readily seen that, from (9),

$ \dot{z} = \left( A+2 \begin{pmatrix} x_e^T B_1 \\ x_e^T B_2 \\ \vdots \\ x_e^T B_n \end{pmatrix} \right) z+B(z) + Ax_e + B(x_e) $

$ = \left( A+2 \begin{pmatrix} x_e^T B_1 \\ x_e^T B_2 \\ \vdots \\ x_e^T B_n \end{pmatrix} \right) z+B(z) \quad (11) $

<a id='3eea6311-b0e3-425a-8575-be46dfcc9561'></a>

which is a quadratic system in the form (7). Moreover, the equilibrium z = 0 of system (11) corresponds to the equilibrium x = x<sub>e</sub> of system (7).

<a id='fb7a2b63-f41b-4ebb-b8bf-ec8adaab83bd'></a>

On the basis of this observation, without loss of generality,
we shall focus on the stability properties of the zero equilibrium
point of system (7). Also, with slight abuse of terminology, we
shall refer to the "stability properties" of system (7), in place of
the "stability properties of the zero equilibrium point" of system
(7).

<a id='36163c4b-0afb-4c5d-99f7-3d2a20c00776'></a>

Checking local asymptotic stability of system (7) is rather simple, since it amounts to evaluating the eigenvalues of the linearized system x = Ax. In the context of our work, however, establishing the local asymptotic stability is not enough, since it is required to check whether a given box belongs to the DA of the equilibrium.

<a id='fb931436-2b98-4323-b634-6c9913652460'></a>

In order to precisely define the problem we deal with in this
paper, recall that a box $\mathcal{R} \subset \mathbb{R}^n$ can be described as follows:

$\mathcal{R} = \text{conv}\{x_{(1)}, x_{(2)}, \ldots, x_{(p)}\}
(12a)

<a id='c3c5664d-d971-4c0d-b627-32d57320517a'></a>

= {x ∈ R^n : a_k^T x ≤ 1, k = 1, 2, ..., q},

(12b)

<a id='5b163549-0554-4c46-8fed-bee5f60cec96'></a>

where p and q are suitable integer values, x(i) denotes the ith vertex of R and conv{.} denotes the operation of taking the convex hull of the argument.

<a id='d4c06570-610b-45cf-907e-878883923e82'></a>

For example the box in R^2
R := [-1,2] × [-1,3]

<a id='436b0a8f-8a8d-4a97-abbd-8379df632143'></a>

can be described both in the form (12a) with
x_(1) = (2 - 1)^T, x_(2) = (2 3)^T, x_(3) = (-1 3)^T,
x_(4) = (-1 - 1)^T,

<a id='86eac265-4613-4838-90a6-38e01c542ccf'></a>

and in the form (12b) with

$a_1^T = \left(\frac{1}{2} \ 0\right)$, $a_2^T = (-1 \ 0)$, $a_3^T = \left(0 \ \frac{1}{3}\right)$, $a_4^T = (0 \ -1)$.

<a id='0c2a2522-b19f-483f-b68f-2b42ca456277'></a>

In the next section we will try to solve the following problem.

<a id='6e0b5179-5755-4d45-a9d2-dc4457e59205'></a>

**Problem 1.** Assume that the matrix A in (7) is Hurwitz; then, given the box R defined in (12), such that 0 is an interior point of R, establish whether R belongs to the DA of system (7).

<a id='4915a5c9-732e-4be3-9cdc-eea362e7ad20'></a>

## *3.1. Machinery*
Let us first recall the following classical result from Lyapunov stability theory.

<a id='c773af48-4d17-48d3-a335-30e66ce3bdde'></a>

**Theorem 1** ([36]).
A given closed set E ⊆ Rⁿ, such that 0 is an interior point of E, is an
estimate of the DA of system (7) if

<a id='e141e9eb-258b-44fb-bd1c-dd9e438d8f12'></a>

(i) *E* is an invariant set for system (7);
(ii) there exists a Lyapunov function *v(x)* such that
(a) *v(x)* is positive definite on *E*;
(b) *v̇(x)* is negative definite on *E*.

<a id='55826def-0506-45d5-9484-11b6e1add3d8'></a>

**Remark 1.** Recall that, given an asymptotically stable system, the DA is defined as the largest connected set Ω containing the origin and such that every solution starting in Ω converges to zero. Any closed region E, such that 0 is an interior point of E, contained in Ω is an estimate of the DA. Note that, in order to ensure that a given set E is an estimate of the DA, it is not sufficient to find a positive definite Lyapunov function with negative definite derivative on E. Indeed, as stated in Theorem 1, we also need to ensure that E is an invariant set, i.e. that every solution of (7) starting in E remains in E for all t.

<a id='8191dd1e-a5ff-43df-b60a-14e92fef3766'></a>

In this paper, as usual, we consider quadratic Lyapunov functions
in the form v(x) = xᵀPx with P symmetric positive definite, so as to
satisfy condition (ii-a) in Theorem 1.

<a id='97dbb681-15b4-4f99-832b-ff122019e1af'></a>

Now let us consider the derivative of v(x) along the trajectories of system (7); we have
v̇(x) = xᵀPx + xᵀPẋ

= xᵀ { [Aᵀ + (B₁ᵀx B₂ᵀx ... Bₙᵀx)]P + P [A +

    ⎛
    ⎜ xᵀB₁
    ⎜ xᵀB₂
    ⎜
    ⎜ ⋮
    ⎜
    ⎝ xᵀBₙ

    ⎞
    ⎟
    ⎟
    ⎟
    ⎟
    ⎟
    ⎠

] } x < 0.

(13)

<a id='b4f43d94-2677-436a-994b-a76cbe35585e'></a>

Note that the bracketed expression is an affine function of the state
variables x1,..., xn, therefore it is negative definite on R if it is
negative definite on the vertices of R (see [37], Chapter 3).
Therefore we can conclude that v(x) satisfies the hypothesis (ii)
of Theorem 1 on R if the symmetric matrix function

<a id='64f98064-7c36-4b7d-986e-f32be122e017'></a>

A^T P + PA + P \begin{pmatrix} x^T B_1 \\ x^T B_2 \\ \vdots \\ x^T B_n \end{pmatrix} + (B_1^T x B_2^T x \dots B_n^T x)P (14)

<a id='dc11f7b7-27e5-44fa-b6c8-943f82fe7f6a'></a>

is negative definite on the vertices of the box *R*.
In order to satisfy also condition (i) in **Theorem 1**, the idea is that
of enclosing *R* into an invariant set which belongs to the DA,
namely the region bounded by a suitable level curve of the
Lyapunov function.

<a id='b7681281-1b4b-48e9-87dd-6398b89d1f89'></a>

More precisely, let us consider a box $\mathcal{R}' \supset \mathcal{R}$ and a positive definite quadratic function $v(x) = x^T P x$ such that the matrix functional in (14) is negative definite on $\mathcal{R}'$. Then, given $c > 0$, any ellipsoidal region

<a id='3c43a362-f37d-4016-919b-edce64f43fb0'></a>

E_c := {x \in R^n : x^T Px \le c} \subset R' (15)

<a id='362ec093-cb95-4c38-9170-5ec1634b5c54'></a>

belongs to the DA.

<a id='773fcfa6-d519-4990-bc4d-c01ad42eb09c'></a>

(9)

<a id='3ee95501-59df-46d7-8772-62067eb1d426'></a>

(10)

<!-- PAGE BREAK -->

<a id='acdd8176-59ba-4afa-91f3-d7997547a84c'></a>

216

<a id='930420a7-c58c-4cb1-b2aa-d36b0f2ef3f8'></a>

A. Merola et al. / Biomedical Signal Processing and Control 3 (2008) 212–219

<a id='b17965cb-2f94-406c-b1d6-990bdb89eabb'></a>

Clearly, if it is possible to prove that E_c ⊃ R for some positive scalar c, a solution to Problem 1 has been found.
In the following we shall show that the double constraint

R' ⊃ E_c ⊃ R                                                        (16)

<a id='5908d7ef-bbc5-4492-85fd-30b95f67d388'></a>

can be translated into LMI conditions, therefore Problem 1 can be translated (with some conservatism) into a feasibility problem involving LMI constraints [32] and solved via available software [33].

<a id='8f6a3a2d-284e-4c43-bed0-edea1406c35b'></a>

Let us refine this idea; let $\mathcal{R}' := \rho\mathcal{R}$, $\rho > 1$, as the set obtained by multiplying by $\rho$ the dimensions of $\mathcal{R}$. Roughly speaking the set $\mathcal{R}'$ has the same shape of the set $\mathcal{R}$, but its vertices are amplified by a factor $\rho$. In the following we are interested in finding a positive definite quadratic Lyapunov function $v(x) = x^T Px$, a corresponding ellipsoidal region $\mathcal{E}_c$ containing the set $\mathcal{R}$ and a factor $\rho > 1$ such that:
(a) the matrix functional in (14) is negative definite on the set $\mathcal{R}'$; (b) $\mathcal{R}'$ contains $\mathcal{E}_c$. Everything should be translated into LMI conditions.

<a id='47b2d763-1682-484a-aef9-75d856b4ade5'></a>

First we focus on the condition $\mathcal{E}_c \supset \mathcal{R}$. Since the matrix $P$ defining the quadratic Lyapunov function will be an optimization variable in the final formulation of the problem, without loss of generality we can assume $c = 1$; indeed $c \neq 1$ is equivalent to rescaling $P$. Looking to (15) and (12a) we have that the condition

$\mathcal{E} := \mathcal{E}_1 \supset \mathcal{R}$
(17)

<a id='b85b2e6d-750c-4f7b-8fde-da77ba30a14f'></a>

is equivalent to (see [32], p. 69)

$x_{(i)}^T Px_{(i)} \le 1, \quad i = 1,2,...,2^n$

(18)

<a id='9d5bffec-6f6f-4239-a3cd-fad78206faab'></a>

which is a set of 2" LMIs in the matrix variable P.
Now note that the set R' can be equivalently described as

<a id='51c7f958-010e-4708-a177-e308035e6658'></a>

R' = {x ∈ Rⁿ : aᵏᵀx ≤ ρ, k = 1, 2, ..., 2n}
= {x ∈ Rⁿ : (aᵏᵀ/ρ)x ≤ 1, k = 1, 2, ..., 2n} (19)

<a id='83cff251-83e3-4b8c-8dec-3f1908a08530'></a>

Therefore, according to [32], p. 70, we have that the condition

$R' \supset E$ (20)

<a id='03a0814e-d41f-48b9-ab02-e86a5d6f9ed5'></a>

can be equivalently rewritten

$\frac{a_k^T}{\rho} P^{-1} \frac{a_k}{\rho} \leq 1, \quad k = 1,2,...,2n$ (21)

<a id='b995e6bd-4466-4bba-8de6-2bf6d6306fc2'></a>

which, using Schur complements, is equivalent to

<a id='8442f12b-9e58-49c6-9493-9de034234e5b'></a>

$$\begin{pmatrix} 1 & a_k^T / \rho \\ a_k / \rho & P \end{pmatrix} \geq 0, \quad k = 1, 2, \dots, 2n. \quad (22)$$

<a id='1921101a-1cc4-4319-a0df-3ede935a9bf2'></a>

On the basis of the above discussion, Problem 1 is solvable if the following generalized eigenvalue problem (GEVP) ([32], p. 10) admits a feasible solution.

<a id='307dcf85-b4a8-438b-969c-308a67e9dadd'></a>

**Problem 2.** Find a scalar \gamma and a symmetric matrix \textit{P} such that

<a id='983b183b-2e2d-4467-96e1-62a192a57d17'></a>

<::chart: Line graph titled "Population dynamics of the tumor-immune system competition". The x-axis is labeled "time [days]" and ranges from 0 to 250. The y-axis is labeled "Cells [number]" and ranges from 0 to 6. The graph shows three lines: a blue dashed line representing "M Tumor cells", a green solid line representing "N Hunting cells", and a red dash-dot line representing "Z Resting cells". The "M Tumor cells" line starts at approximately 3.2, decreases slightly, and then stabilizes around 2.6. The "N Hunting cells" line starts at approximately 1.5, increases sharply to about 5.4, and then stabilizes. The "Z Resting cells" line starts at approximately 0.5, decreases rapidly to near 0.2, and then remains low. Fig. 1. State response of system (1) from a perturbed initial condition.::>

<a id='9c3f9960-e872-4a74-9e00-a2a88edc7bed'></a>

**Remark 2.** Note that, depending on the system structure, the ellipsoid $\mathcal{E}$ may result a set much more large than the original box $\mathcal{R}$. Indeed such ellipsoid has to contain _all_ the trajectories starting from the points of $\mathcal{R}$; conversely, such trajectories are not constrained to stay confined within $\mathcal{R}$ for all time, since, as said, $\mathcal{R}$ is not an invariant set. This is particularly true if the trajectories exhibit a strong overshoot (see also Section 4.2).

<a id='61fd0edc-50bd-4316-9e15-adcc8f5378a4'></a>

## 4. Analysis of the tumor dormancy equilibrium

### 4.1. Validation of the proposed technique

In [10], the state response of system (1) is determined for the initial condition X₀ = [2.5 1.5 0.5]ᵀ and parameters q = 10, r = 0.9, α = 0.3, k₁ = 0.8, β = 0.1, d₁ = 0.02, s = 0.8, k₂ = 0.7, d₂ = 0.03. As shown in Fig. 1, starting from this initial condition, the system trajectory converges to the asymptotically stable equilibrium E₃ = [2.67 5.41 0.2]ᵀ.

In order to validate our technique, we have solved Problem 1 for system (1) with the same values of the parameters given in [10]. To this aim, we define the box R = [2,3.5] × [1,6] × [0.1, 0.7] containing the equilibrium point E₃ and the cited initial condition.

Since E₃ is a nonzero equilibrium point, we apply the change of variable (10) and study the properties of the zero state of the corresponding quadratic system in the form (11) with

<a id='afd136ac-5d89-4bde-aadb-a227e8aa0147'></a>

A = \begin{pmatrix} r & 0 & 0 \\ 0 & -d_1 & 0 \\ 0 & 0 & s-d_2 \end{pmatrix}, B_1 = \begin{pmatrix} -\frac{r}{k_1} & -\frac{\alpha}{2} & 0 \\ -\frac{\alpha}{2} & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, (23)

B_2 = \begin{pmatrix} 0 & 0 & \frac{\beta}{2} \\ 0 & 0 & \frac{\beta}{2} \\ 0 & \frac{\beta}{2} & 0 \end{pmatrix}, B_3 = \begin{pmatrix} 0 & 0 & -\frac{\beta}{2} \\ 0 & 0 & -\frac{s}{k_2} \\ 0 & -\frac{\beta}{2} & 0 \end{pmatrix}.

<a id='7c6c50df-4b4a-4f70-a597-4fd7ce28cabb'></a>

0 < γ < 1, P > 0, \begin{pmatrix} 1 & \gamma a_k^T \\ \gamma a_k & P \end{pmatrix} \geq 0,
k = 1,2,..., 2n, x_{(i)}^TPx_{(i)} \leq 1, i = 1,2,..., 2^n,
\gamma(A^TP + PA) + P \begin{pmatrix} x_{(i)}^TB_1 \\ x_{(i)}^TB_2 \\ \vdots \\ x_{(i)}^TB_n \end{pmatrix} + (B_1^Tx_{(i)} \ B_2^Tx_{(i)} \ ... \ B_n^Tx_{(i)})P < 0, i = 1,2,..., 2^n.

<!-- PAGE BREAK -->

<a id='47f8de2e-2e8c-486d-817b-a59b72eec206'></a>

A. Merola et al./Biomedical Signal Processing and Control 3 (2008) 212–219

<a id='4602508e-e5c5-45cb-b02c-79d7ff1f4bf7'></a>

217

<a id='d01d58a3-9fb1-42ba-9da6-06fd04132dc2'></a>

Then we determine the vectors $a_k$ for $k = 1,..., 6$, the vertices $z_{(i)}$, for $i = 1,..., 8$, and the expression of the box $\mathcal{R}$ translated to the origin. The solution of the feasibility Problem 2 has been obtained by means of the Matlab LMI Toolbox [33]. An admissible solution is

$\gamma = 0.0774, P = \begin{pmatrix}
0.0221 & 0.0060 & -0.0690 \\
0.0060 & 0.0092 & -0.0154 \\
-0.0690 & -0.0154 & 1.1850
\end{pmatrix}$

<a id='36e3864e-9a80-4d86-bf18-99b8b7970b40'></a>

We can conclude that the box $\mathcal{R}$ belongs to the DA of $E_3$. This implies that every trajectory starting from an initial condition included in $\mathcal{R}$ converges to $E_3$. Since the initial condition $x_0$ belongs to the box $\mathcal{R}$, our methodology confirms the asymptotic behavior of the state response of system (1) computed in [10].

<a id='3e59224c-21d2-4e1c-8c5e-e2a293e4bad6'></a>

## 4.2. Optimization of the domain of attraction of E3

Changes of the hemodynamic perfusion of the tumor, radiation or chemotherapy may induce stochastic perturbations of the state variables around the equilibrium point E3, thus leading the system away from the steady-state condition. If the amount of these perturbations brings the system out of the domain of attraction of the equilibrium point E3, the state trajectories diverge. Instability is an undesirable clinical circumstance since it causes the unbounded growth of the tumor.

<a id='084aebbc-599f-4d5c-b1f6-63c5ff8e6cc6'></a>

The results presented in this paper are potentially useful not only for the analysis of the tumor development, but also to devising an effective therapeutic strategy: given a certain operative range, a suitable strategy could be that of enforcing the system trajectories to tend to the asymptotically stable equilibrium E3 (tumor growth blocked). This problem can be translated in mathematical terms to that of computing the value of certain parameters such that the DA of E3 contains the given operative range.

<a id='144266b0-f267-4fac-af5d-3fdbf620719b'></a>

By using the results presented in Section 3, it is possible to optimize the value of α, which depends on the amount of immunotherapeutic drug injected into the patient, in order to guarantee a safety region (i.e. included in the DA) around the equilibrium point E3. It means that the box R is assigned in terms of an admissible variation interval of each state variable around the equilibrium point. The sizes of such intervals have to be chosen on the basis of the clinical knowledge about the admissible perturbations acting on the system.

<a id='70723e1a-e694-4d0a-b6ee-53b9e99b0472'></a>

In order to exemplify this strategy, we shall apply the proposed methodology to the quadratic model (1) using the same parameter values given in [10], except for α which will be optimized as described below. First of all, note that the first component of the equilibrium E3 depends on α, while the other components do not:

<a id='b99bcfcd-8c29-4cd8-8692-4372d4a209fa'></a>

E₃(α) = (x(α) 5.41 0.2)ᵀ (24)

<a id='9bc37d45-b37a-4de3-b8cd-08b2179ca561'></a>

where $x(\alpha)$ is given by (4) when all parameters, except $\alpha$, assume the values given in [10].

<a id='fd9e2845-8a4d-42f1-95ab-1aa1b4daa208'></a>

In Fig. 2 the first component of E3 is plotted versus α, for α between 0 (absence of drug) and 0.3 (maximum value of α compatible with (6)). In [10] the maximum allowable α is considered to simulate the system behavior. Here our goal is that of using the proposed approach for guaranteeing a reasonable robustness region around E3 and, at the same time, lowering the value of α and therefore the amount of drug delivered to the patient.

<a id='a1ecf9aa-cc4d-4deb-adb6-75914d96c4d0'></a>

Remember that _M_(_t_) represents the density of tumor cells, while _N_(_t_) and _Z_(_t_) the density of hunting and resting predator cells. For a given _α_, it is reasonable to define a safety interval around _E_3 which allows a 50% variation of the state variables around the equilibrium point (this safety box captures, for example, an increase up to 50% of the malignant cells and/or a decrease up to 50% of the predator cells with respect to the values at the equilibrium); in this way we define a

<a id='4d85bea1-7613-41a4-90f9-61b9f10133f8'></a>

<::line graph
: The graph shows the behavior of a function E₃(α). The x-axis is labeled "α" and ranges from 0 to 0.3, with major ticks at 0, 0.05, 0.1, 0.15, 0.2, 0.25, and 0.3. The y-axis is labeled "E₃(α)" and ranges from 2.6 to 3.5, with major ticks at 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, and 3.5. A single blue line decreases linearly from approximately (0, 3.4) to (0.3, 2.68).
: Fig. 2. Behavior of x(a).
::>

<a id='b69d7850-bf65-468d-bf74-5ccb1e19edf9'></a>

box (for a given $\alpha$) as follows:

$\mathcal{R}(\alpha) := [x(\alpha) - 0.5 \cdot x(\alpha), x(\alpha) + 0.5 \cdot x(\alpha)] \times [2.7, 8.12] \times [0.1, 0.3].$ (25)

<a id='3b2ad421-e4c8-47bf-9a47-fdf89b86c7a4'></a>

Now, for a given value of $\alpha$:
1. Compute the corresponding equilibrium point $E_3(\alpha)$ by using (24).
2. Compute the box $\mathcal{R}(\alpha)$ around $E_3(\alpha)$ by using (25).
3. Determine whether $\mathcal{R}(\alpha)$ belongs to the DA of $E_3(\alpha)$ by using the approach of Section 3.

<a id='c13aa471-8857-4c91-9494-a34844e11d29'></a>

By a dichotomous search it is possible to find the minimum value of α satisfying this test. In our case the result is α_opt = 0.06, with E₃(α_opt) = [3.25 5.41 0.2]ᵀ and R(α_opt) := [1.53, 4.59] × [2.7, 8.12] × [0.1, 0.3]. Indeed it is possible to verify that, with the values given above,

<a id='ce37fd9d-3b35-4120-95f4-8b2e35940247'></a>

α_opt = 0.06, γ = 0.2154,

P = 
  ⎛ 0.0243    0.0016   -0.2022 ⎞
  ⎜ 0.0016    0.0065   -0.0241 ⎟ ,
  ⎝ -0.2022   -0.0241    6.3640 ⎠
(26)

<a id='be1ad607-4ae7-4ba5-a9bf-ad2df0e15706'></a>

is an admissible solution to Problem 2.
In Fig. 3 the box R(α_opt), the ellipsoid bounded by the level curve
of the Lyapunov function x^T Px, with P given in (26), and the

<::transcription of the content
: 3D plot showing an ellipsoid, a red box labeled E3, and a trajectory starting from x0. The axes are labeled Z (vertical, from -0.3 to 0.7), N (horizontal, from 0 to 20), and M (horizontal, from -10 to 12).::>

Fig. 3. The box R(α_opt), the level curve of x^T Px which contains the ellipsoid
surrounding R(α_opt) and the trajectory starting from x0.

<!-- PAGE BREAK -->

<a id='7f872b6f-ad84-4df7-9bac-ceec1ed47273'></a>

218

<a id='5a068816-e272-425a-846f-2f2b97bd38f8'></a>

A. Merola et al./Biomedical Signal Processing and Control 3 (2008) 212–219

<a id='7ccc7946-419b-40a6-aff9-00a23867e0a9'></a>

trajectory starting from the initial condition x0 = (4.87 2.7 0.1)T (maximum density of malignant cells, and minimum density of predator cells) is depicted. As expected, the trajectory, starting by this very unfavorable state which is included into the safety box, converges to the tumor dormancy equilibrium.

<a id='46eee108-2353-4119-b1d8-af425e92c478'></a>

It is interesting to note that the trajectory exits the box (see
Remark 2), exhibits an overshoot, which extends well outside the
box, and eventually reaches the equilibrium. The fact that the
initial condition belongs to the DA, indeed, does not guarantee that
the number of malignant cells is bounded during the transient, but
it ensures that, after a possible overshoot, it will return to the
dormancy level. On the other hand, the proposed analysis method
also provides a bound to the admissible system trajectories, which
is given by the ellipsoidal region surrounding the box.

<a id='48a29a3c-2bf0-4eae-a2cf-14bc80e2f596'></a>

Understanding this dynamical behavior can have interesting
implications in the therapeutic strategy: a quantitative analysis of
tumor growth over a time interval, coupled with an effective model,
could help to determine whether the current therapy is effective and
the growth is just a transient dynamic, or the system has left the
safety region and a different therapeutic action is needed.

<a id='db500de3-5fbd-4cf2-870b-c19b2b92a008'></a>

Also note that the optimal value of α is very small. Under the assumption that the parameter α is influenced by the dose of drug administered to the patient, the slight value of α is an alluring result, because it suggests that, by exploiting the proposed technique, it is possible not only to devise a robust therapeutic strategy but also to minimize, at the same time, the amount of drug delivered to the patient. A major remaining challenge in immunotherapy, in fact, consists of improving antitumor activity without inducing unmanageable toxicity to normal tissues [38]. Therefore, a primary goal consists of determining the minimum dose of drug capable of producing the desired effective therapeutic action, with limited side-effects of drug on normal tissues.

<a id='3c332076-862c-4022-9d10-cc28defc2b50'></a>

## 5. Conclusions
An optimization technique has been proposed which, given a nonlinear dynamical quadratic system, is aimed at determining whether an assigned region of the state space, containing an asymptotically stable equilibrium point, belongs to the DA of that point. This problem is reduced to the solution of a LMI-based optimization problem, which can be dealt with by means of efficient numerical algorithms. The proposed technique has been exploited in the context of a dynamical model, which describes the tumor-immune system competition, originally presented in [10]. Such model, which is quadratic in the state variables, focuses on the interaction of different cell populations, providing an empirical description of the phenomenon, based on classical mathematical biology arguments (i.e. Lotka–Volterra-like and logistic terms).

<a id='e34ff380-00e2-4b5b-84c4-06a43135cee2'></a>

By applying the devised results, it is possible to analyze the robustness of the desired operative condition against perturba-tions moving the state trajectory away from an asymptotically stable equilibrium point, which represents a clinical favorable condition, i.e. tumor dormancy. It is appropriate to remark that a detailed description of tumor dynamics would require taking into account also other effects, like diffusion of compounds through biological tissues, or changes in the vascularization of the tumoral mass, which could possibly result in non-quadratic models. However, if the dynamics of the quadratic model provide a sufficiently accurate description of the biological behavior, one could also assume that the effects of the mathematical mismatch-ing between such model and the 'real' one do not drive the state trajectory outside the domain of attraction of the tumor dormancy equilibrium point. Certainly, a definitive answer to this question can be provided only by in vitro/in vivo experimental tests, which will likely be the object of future investigations.

<a id='903d79b1-8cd9-4421-b2e9-206a43bf4e68'></a>

Finally, it has been shown that the proposed technique can be exploited to optimize the therapeutic strategy. For the analyzed model, in accordance with the working principles of immunother-apy (see [10]), we have assumed that the value of the parameter a (the killing rate of tumor cells by hunting cells) can be modified by means of drug administration. Under this working hypothesis, at least in principle, it is possible to maximize the value of a, in order to eradicate the tumor, by delivering high doses of drugs to the patient; in practice this is not viable, because high doses of immunotherapeutic drugs cause toxic side-effects to normal tissues. From these considerations it is clear that the value of a has to be optimized, by acting on the doses of drugs delivered to the patient, in order to achieve both a favorable tumor dormancy condition, robust against perturbations of the level of malignant cells, and a low level of toxicity for healthy tissues.

<a id='efcd7052-ec9e-4cc0-a0b7-099ce5db6738'></a>

With reference to the modeling framework adopted in the paper, the analysis technique has been also exploited to find an optimal value of the parameter \u03b1, through an iterative procedure. It is important to note that the actual translation of such procedure into an effective therapeutical strategy would require the definition of a precise relationship between the doses of drugs delivered to the patient and the rate of killing of tumor cells, which could possibly be determined through biological experiments.

<a id='232c5b7e-4325-424b-90c0-db6e4331483d'></a>

# References

1.  J. Adam, N. Bellomo, A Survey of Models on Tumor Immune Systems Dynamics, Birkhauser, Boston, 1996.
2.  L. Preziosi, From population dynamics to modelling the competition between tumors and immune system, Math. Comput. Model. 23 (6) (2003) 132-152.
3.  V.A. Kuznetsov, I.A. Makalkin, M.A. Taylor, A.S. Perelson, Nonlinear dynamics of immunogenic tumors: parameter estimation and global bifurcation analysis, Bull. Math. Biol. 56 (2) (1994) 295-321.
4.  R.A. Gatenby, Models of tumor host interaction as Competing populations: implications for tumor biology and treatment, J. Theor. Biol. 176 (1995) 447-455.
5.  S. Michelson, J.T. Leith, A theoretical explanation of concomitant resistance, Bull. Math. Biol. 57 (5) (1995) 747-773.
6.  Z. Bajzer, M. Marusic, S. Vuk-Pavlovic, Conceptual frameworks for mathematical modeling of tumor growth dynamics, Math. Comput. Model. 23 (6) (1996) 31-46.
7.  D. Kirschner, J.C. Panetta, Modeling immunotherapy of the tumor-immune interaction, J. Math. Biol. 37 (1998) 235-252.
8.  L.G. de Pillis, A.E. Radunskaya, A mathematical tumor model with immune resistance and drug therapy: an optimal control approach, J. Theor. Med. 3 (2001) 79-100.
9.  L.G. de Pillis, A.E. Radunskaya, C.L. Wiseman, A validated mathematical model of cell-mediated immune response to tumor growth, Cancer Res. 65 (17) (2005) 7950-7958.
10. R.R. Sarkar, S. Banerjee, Cancer self remission and tumor stability—a stochastic approach, Math. Biosci. 196 (1) (2005) 65-81.
11. L.G. de Pillis, W. Gu, A.E. Radunskaya, Mixed immunotherapy and chemotherapy of tumors: modeling applications and biological interpretations, J. Theor. Biol. 238 (4) (2006) 841-862.
12. S. Michelson, J.T. Leith, Autocrine and paracrine growth factors in tumor growth: a mathematical model, Bull. Math. Biol. 53 (4) (1991) 639-656.
13. S. Michelson, J.T. Leith, Growth factors and growth control of heterogeneous cell populations, Bull. Math. Biol. 55 (5) (1993) 993-1011.
14. S. Michelson, J.T. Leith, Dormancy, regression, and recurrence: towards a unifying theory of tumor growth control, J. Theor. Biol. 169 (4) (1994) 327-338.
15. S. Michelson, J.T. Leith, Positive feedback and angiogenesis in tumor growth control, Bull. Math. Biol. 59 (2) (1997) 235-254.
16. J.A. Spratt, D. von Fournier, J.S. Spratt, E.E. Weber, Decelerating growth and human breast cancer, Cancer 71 (1992) 2013-2019.
17. J.C. Panetta, A mathematical model of periodically pulsed therapy: tumor recurrence and metastasis in a competitive environment, Bull. Math. Biol. 58 (3) (1996) 427-447.
18. M. Iori, G. Nespi, G. Spiga, Analysis of a kinetic cellular model for tumor-immune system interaction, Math. Comput. Modell. 29 (1999) 117-129.
19. S. Michelson, J.T. Leith, Interlocking triads of growth control in tumors, Bull. Math. Biol. 57 (2) (1995) 345-366.
20. N.D. Evans, et al., A mathematical model for the in vitro kinetics of the anti-cancer agent topotecan, Math. Biosci. 189 (2004) 185-217.
21. R. Genesio, A. Vicino, Some results on the asymptotic stability of second-order nonlinear systems, IEEE Trans. Automat. Contr. 29 (1984) 857-861.
22. E. Davidson, E. Kurak, A computational method for determining quadratic Lyapunov functions for nonlinear systems, Automatica 7 (1971) 627-636.

<!-- PAGE BREAK -->

<a id='5efb9fff-0b6b-42a9-8ca3-cac0c827ae44'></a>

A. Merola et al. / Biomedical Signal Processing and Control 3 (2008) 212-219

<a id='d240e191-6947-4360-ac65-29bb3f46f60e'></a>

219

<a id='a76dafb7-2ebb-44f9-af20-e4baf9bb194c'></a>

[23] A.N. Michel, N.R. Sarabudla, R.K. Miller, Stability analysis of complex dynamical systems. Some computational methods, Circ. Syst. Signal Process. 1 (1982) 561-573.
[24] H. Chiang, J. Thorp, Stability regions of nonlinear dynamical systems: a constructive methodology, IEEE Trans. Automat. Contr. 34 (1989) 1229-1241.
[25] R. Genesio, M. Tartaglia, A. Vicino, On the estimation of asymptotic stability regions: state of the art and new proposals, IEEE Trans. Automat. Contr. 30 (1985) 747-755.
[26] H. Chiang, M. Hirsch, F. Wu, Stability regions of nonlinear autonomous dynamical systems, IEEE Trans. Automat. Contr. 33 (1988) 16-27.
[27] A. Tesi, F. Villoresi, R. Genesio, On the stability domain estimation via a quadratic Lyapunov function: convexity and optimality properties for polynomial systems, IEEE Trans. Automat. Contr. 41 (1996) 1650-1657.
[28] G. Chesi, Estimating the domain of attraction: a light LMI technique for a class of polynomial systems, in: Proceedings of the 42nd IEEE International Conference on Decision and Control, Maui, Hawaii, 2003.
[29] B. Tibken, Estimation of the domain of attraction for polynomials systems via LMI's, in: Proceedings of the 39th IEEE International Conference on Decision and Control, Sidney, Australia, 2000.

<a id='bef4635d-a90a-4a41-944b-9cbb2a75c4b6'></a>

[30] G. Chesi, A. Garulli, A. Tesi, A. Vicino, LMI-based computation of optimal quadratic Lyapunov functions for odd polynomial systems, Int. J. Nonlinear Robust Contr. 15 (1) (2005) 35–49.
[31] G. Chesi, A. Tesi, A. Vicino, Computing optimal quadratic Lyapunov function for polynomial nonlinear systems via LMIs, in: Proceedings of the 15th IFAC World Congress, Barcelona, 2002.
[32] S. Boyd, L.E. Ghaoui, E. Feron, V. Balakrishnan, Linear Matrix Inequalities in System and Control Theory, SIAM Press, 1994.
[33] P. Gahinet, A. Nemirovski, A.J. Laub, M. Chilali, LMI Control Toolbox, The Math-works Inc., Natick, MA, 1995.
[34] J. Murray, Mathematical Biology, Springer, New York, 2002.
[35] R.A. Gatenby, T.L. Vincent, Application of quantitative models from population biology and evolutionary game theory to tumor therapeutic strategies, Mol. Cancer Ther. 2 (2) (2003) 919–927.
[36] H.K. Khalil, Nonlinear Systems, MacMillan, 1992.
[37] F. Amato, Robust Control of Linear Systems Subject to Uncertain Time-Varying Parameters, Springer Verlag, Berlin, 2006.
[38] J.N. Blattman, P.D. Greenberg, Cancer immunotherapy: a treatment for the masses, Science 305 (2004) 200–205.
<a id='149f1234-8465-47d6-9343-b4fe978348f0'></a>

MATHEMATICAL BIOSCIENCES
AND ENGINEERING
Volume **10**, Number **3**, June **2013**

<a id='4b6f5628-de0b-44ae-bd50-fa5eeaaf6b18'></a>

doi:10.3934/mbe.2013.10.787

pp. **787–802**

<a id='2d636736-d6a9-455f-93e9-86fa933a62c1'></a>

ON OPTIMAL CHEMOTHERAPY WITH A STRONGLY
TARGETED AGENT FOR A MODEL OF TUMOR-IMMUNE
SYSTEM INTERACTIONS WITH GENERALIZED
LOGISTIC GROWTH

<a id='92f57667-e096-458c-add5-27ebd7f2f4ac'></a>

URSZULA LEDZEWICZ AND OMEIZA OLUMOYE
Dept. of Mathematics and Statistics
Southern Illinois University Edwardsville
Edwardsville, Illinois, 62026-1653, USA

<a id='36576acd-08df-4087-a4be-62c7534f6316'></a>

HEINZ SCHÄTTLER
Dept. of Electrical and Systems Engineering
Washington University
St. Louis, Missouri, 63130-4899, USA

<a id='30d4a7cc-5fd3-4a46-b376-a6064abdfbce'></a>

ABSTRACT. In this paper, a mathematical model for chemotherapy that takes tumor immune-system interactions into account is considered for a strongly targeted agent. We use a classical model originally formulated by Stepanova, but replace exponential tumor growth with a generalised logistic growth model function depending on a parameter _v_. This growth function interpolates between a Gompertzian model (in the limit _v_ → 0) and an exponential model (in the limit _v_ → ∞). The dynamics is multi-stable and equilibria and their stability will be investigated depending on the parameter _v_. Except for small values of _v_, the system has both an asymptotically stable microscopic (benign) equilibrium point and an asymptotically stable macroscopic (malignant) equilibrium point. The corresponding regions of attraction are separated by the stable manifold of a saddle. The optimal control problem of moving an initial condition that lies in the malignant region into the benign region is formulated and the structure of optimal singular controls is determined.

<a id='6dfbe9e7-887c-47b7-9b9d-dc31dd663831'></a>

1. **Introduction.** A tumor's microenvironment or stroma is comprised of several components that also include various cells of our immune system with both beneficial and detrimental effects. This reflects just one of many aspects of cancer as a "multifaceted disease" [7]. The purpose of the immune system is to protect the organism from disease. In order to fulfill this function, it needs to be able to detect a wide variety of agents, from viruses to parasites, but also must be able to distinguish these from the organism's own healthy tissue in order not to harm the organism. Tremendous progress in understanding the workings of the immune system has been made in connection with research on HIV and this new knowledge also finds its application in cancer research. Since the immune system's first response to its environment is on the basis of a discrimination between "own" and "foreign" objects, many types of tumor cells are more or less tolerated by the patient's own

<a id='d168d170-aab3-44dd-a5dd-50e5fb02939e'></a>

2010 Mathematics Subject Classification. Primary: 49K15, 92C50; Secondary: 93C95.
Key words and phrases. Optimal control, targeted chemotherapy, tumor immune system interactions, generalized logistic growth.

<a id='b9a8c02e-fc5d-4ad3-8fdc-2fb3d7a4f73a'></a>

787

<!-- PAGE BREAK -->

<a id='188d94f1-a8ee-405a-a1f1-f9c91a8a6ddb'></a>

788 URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER

<a id='9b2eb828-8894-424d-95af-2850e1a2a0e3'></a>

immune system since, essentially, they are classified as "own" cells [26]. However, tumor cells also exhibit a large number of abnormalities (such as mutated proteins, under- or over-expressed normal proteins and many more) that lead to the appear- ance of specific antigens some of which will be classified as "foreign" and thus do trigger reactions by both the innate and adaptive immune system [10, 33]. In fact, the empirical hypothesis of immune surveillance, i.e., that the immune system may act to eliminate tumors, which is well-established in the medical community, has recently been confirmed experimentally and epidemiologically [6].

<a id='d6600284-d8bc-4b4d-b4eb-2f9c6de54806'></a>

The competitive interaction between tumor cells and the immune system is complex and involves a large number of events with the kinetics highly nonlinear. The possible outcome of this interplay is not only constituted by either tumor suppression or cancer outbreak, but there exist many intermediate scenarios. For example, it has been hypothesized that in case of a fully developed and metastatic tumor, upregulation of the immune system may be responsible for controlling small metastases. There exist theoretical immuno-oncologic studies, largely inferred from clinical data, that come to the conclusion that in some cases the immune system may be able to keep the tumor in a dynamic equilibrium that corresponds to a microscopic (undetectable) dormant state [18, 19, 21], so-called tumor dormancy.
But it is quite intuitive, that this equilibrium can be disrupted by sudden events affecting the immune system. Mathematically, this simply is related to the size of the region of attraction of this equilibrium: if this region is small, even minor events may bring up the disease while the immune system is well able to control the disease if this region is large. While there exist good reasons to believe that the immune system may be able to control tumors initially, over a long period of time, the neoplasm will develop various strategies to circumvent the action of the immune system which allows the tumor to recommence growing [6, 21] into clinically apparent tumors [12] and eventually reach its carrying capacity [21]. Outside effects such as immuno-suppressive treatments or immuno-editing may move the current state of the system (comprising cancer and immune cells) across the boundary from a benign state (in the region of attraction of a microscopic equilibrium) into a malignant state (in a region of uncontrolled growth or region of a attraction of a malignant equilibrium). Overall, tumor-immune system interactions exhibit a multitude of dynamic properties that include multi-stability, i.e., persistence of both benign and malignant scenarios.

<a id='b5db5cde-6f96-40ee-9524-c0803a728a3a'></a>

There exists a substantial literature on the mathematical description of tumor and immune system interaction that has seen a strong resurgence due to our in-creased understanding of the mechanisms of the immune system in connection with AIDS (acquired immune deficiency syndrome) research, e.g., [2, 3, 11, 22, 29], to mention just a small sample of more recent publications on this topic. Historically, one of the earliest references on this topic is the 1980 paper by Stepanova [32] where two ordinary differential equations are proposed that model the interactions between tumor cell growth and the activities of the immune system during the development of cancer. In this model, the main features of tumor-immune interactions are ag-gregated into two principal variables, the tumor volume and immunocompetent cell densities relating to the activities of various kind of T-cells. Precisely because of its simplicity---a few parameters incorporate many medically important features--- the underlying equations have been widely accepted as a basic model. There exist numerous extensions and generalizations of this model, most notably the one by Kuznetsov, Makalkin, Taylor and Perelson who in [13] employ a logistic model for

<!-- PAGE BREAK -->

<a id='6817e186-bd46-41dc-8414-d500557adbe8'></a>

CHEMOTHERAPY WITH GENERALIZED LOGISTIC GROWTH

<a id='91fbca87-0bea-41f5-a26f-03dee38e0a62'></a>

789

<a id='ae45608d-6a59-4bfc-b6f9-6bdecdb1a84e'></a>

cancer growth and estimate parameters based on in vivo data of B-lymphoma BCL1
in the spleen of mice. In a paper by de Vladar and González [34], logistic growth
on cancer cells is replaced with a Gompertzian model. In all cases, the models ex-
hibit both stable microscopic (benign) and macroscopic (malignant) equilibria and
a comprehensive analysis of the dynamic behavior of the underlying systems and
its bifurcations is carried out in the respective papers. More recently, d'Onofrio
formulated and investigated a general class of models [19, 20] that incorporates all
these dynamical models. The analysis of these mathematical models all confirm the
following medical findings: while the immune system can be effective in the control
of small cancer volumes, for large volumes the cancer dynamics generally suppresses
the immune dynamics.

<a id='a7bd5d38-685b-4e9c-ae40-bc8e78fe8c86'></a>

In this paper, we consider Stepanova's model when a generalised logistic growth
model,

<a id='32798778-9abd-45b6-af67-f51317c839f4'></a>

F(x) = \xi \left(1 - \left(\frac{x}{x_\infty}\right)^\nu\right), \quad \nu > 0,

<a id='d8ed1809-72b9-4494-bc5b-7ba30edc5265'></a>

with finite carrying capacity $x_\infty$ is employed to describe the growth of the tumor volume $p$ as $\dot{p} = pF(p)$. The parameter $\nu$ in this model allows to differentiate the rate of tumor growth: for small values of $\nu$, the term $\left(\frac{x}{x_\infty}\right)^\nu$ will be close to 1 and the model reflects a slowly growing tumor while tumor growth accelerates with increasing values of $\nu$ reaching unrestricted exponential growth in the limit $\nu \to \infty$. In the other extreme, if the limit $\nu \to 0$ is taken with the growth coefficient $\xi$ made to depend on the parameter $\nu$ in the order of $\xi = O(\frac{1}{\nu})$, a Gompertzian model is obtained. The generalised logistic rate function $F$ thus interpolates between Gompertzian and exponential growth models with the parameter $\nu$ determining the rate of tumor growth. For models of the tumor-vasculature dynamics it has been argued by d'Onofrio, Gandolfi and Rocca [25] that models with $\nu < 1$ more realistically reflect a slowing down process of tumor proliferation as a response to its changing environment. This also agrees with a mechanistic model for non-immunogenic tumors as discussed by d'Onofrio in [23]. In the context of tumor immune system interactions, which play a major role at the onset of the disease, it would seem that all values of $\nu$ would appear reasonable, simply modeling different rates of tumor growth lying between the extremes of Gompertzian and exponential growth models.

<a id='4e0d32ca-c0ef-4d19-898a-cb2e9df10ffe'></a>

For most of these models the dynamics is multi-stable and, except for small values of $v$, the system has both an asymptotically stable microscopic (benign) and an asymptotically stable macroscopic (malignant) equilibrium point. Their corresponding regions of attraction are separated by the stable manifold of a saddle. We shall see that the coefficient $v$ (and thus ultimately the tumor growth rate) directly relates to the size of the region of attraction of these equilibria. Indeed, for small enough $v$, there only exists one globally asymptotically stable equilibrium which corresponds to a microscopic and thus benign equilibrium point. In this sense, for very slow growing tumors, in the model the immune system is able to control the disease. However, as $v$ increases, an unstable and a stable macroscopic (malignant) equilibrium are born in a saddle-node bifurcation and the corresponding malignant region of attraction increases in size with increasing tumor growth rate converging to the region of attraction for the model with exponential growth in the limit $v \to \infty$. From a practical point of view, the question of curing cancer then is related to the mathematical problem of how to move an initial condition

<!-- PAGE BREAK -->

<a id='c635c991-091d-4f07-adea-96931f9f83d6'></a>

790 URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER

<a id='9b45040c-e244-459d-9c4b-919372be20e9'></a>

that lies in the malignant region into the benign region. This requires therapy and can naturally be formulated and analyzed as an optimal control problem. In this paper, we analyze the structure of singular controls and their optimality depending on the parameter $\nu$. It will be seen that the regions where singular controls can be optimal shrink with increasing values $\nu$ and in the limit $\nu \to \infty$ they no longer are candidates for optimality for the exponential model.

<a id='dfbc322c-5bc9-4ab5-8517-43ef39c31a8a'></a>

2. **Benign and malignant regions for Stepanova's model with generalized logistic growth.** We retain Stepanova's model for tumor immune system inter-actions, but replace exponential growth for the tumor with a generalized logistic growth model. Stepanova's model has the advantage of being minimally parame-terized while, nevertheless, rather accurately reflecting the main qualitative aspects of tumor-immune interactions. Let *x* denote the tumor volume and suppose there exists a fixed carrying capacity *x*∞ < ∞. Furthermore, let *y* denote the immuno-competent cell densities, a non-dimensional, order of magnitude quantity related to various types of immune cells (T-cells) activated during the immune reaction. Stepanova's model then takes the form

<a id='afdf7819-9b8a-411a-a44b-4a5cdfd6fa2e'></a>

ẋ = μ_C x (1 - (x / x_∞)^ν) - γxy (1)
ẏ = μ_I (1 - βx) xy - δy + α (2)

<a id='5d4a24f9-4cf3-45ea-ad83-ac065cbb5878'></a>

with $\nu > 0$ a parameter. The model is classical and we therefore only briefly review its rationale and refer the reader to [16, 32] for a more detailed discussion. Equation (2) summarizes the main features of the immune system's reaction to cancer. The coefficient $\alpha$ models a constant rate of influx of T-cells generated through the primary organs and $\delta$ is simply the rate of natural death of T-cells. The first term in this equation models the proliferation of lymphocytes. The fact that small tumors stimulate the immune system while large tumors suppress it, is expressed in the model through the inclusion of the factor $(1 - \beta x)$ at the term $\mu_Ixy$ describing the effects of tumor immune interactions on the immune system. The constant $1/\beta$ thus corresponds to a threshold beyond which the immunological system becomes depressed by the growing tumor. Together, the coefficients $\mu_I$ and $\beta$ are used to calibrate these interactions. Similarly, in the first equation, (1), the term $\gamma xy$ describes the elimination effects of the tumor-immune interactions on the cancer volume. The difference between this model and the formulations used by Kuznetsov et al. [13] and de Vladar and Gonzalez [34] is that we employ a generalised logistic model for tumor growth.

<a id='e8a4475b-1f6c-4502-951d-ccd4383d2a37'></a>

In this section, we illustrate the changes in the equilibria and the associated regions of attractions of the existing stable equilibria. We recall that for a dynamical system $\dot{z} = f(z)$ with a locally asymptotically stable equilibrium point $x_*$, its region of attraction is defined as the set of all initial conditions $z_0$ for which the corresponding solution $z(t; x_0)$ of the initial value problem $\dot{z} = f(z)$, $z(0) = z_0$, exists for all times $t \geq 0$ and converges to $z_*$ as $t \to \infty$. This set is always an open and connected subset of the state space. By solving the equation $\dot{x} = 0$ for $y$ and substituting into the relation $\dot{y} = 0$, equilibria are solutions of the nonlinear equation

<a id='f8180bfc-12d5-4e02-aec9-f946e51e94e5'></a>

\mu_C \left(1 - \left(\frac{x}{x_\infty}\right)^\nu\right) (\mu_I (x - \beta x^2) - \delta) + \alpha \gamma = 0.

<!-- PAGE BREAK -->

<a id='57ff4196-885f-4bee-8cda-40d556313372'></a>

CHEMOTHERAPY WITH GENERALIZED LOGISTIC GROWTH

<a id='39e8b932-d4f5-4f0f-a923-1647932b4890'></a>

791

<a id='ed1a51b3-cb38-44ce-b41f-a5a2336200fe'></a>

Clearly, the analysis of solutions depends on the parameter values and in this paper we only analyze this equation for the parameter values given in Table 1. These values are non-dimensional on an order of magnitude scale. The values for α through δ are taken from the paper by Kuznetsov et al. [13] and μI and μC were adjusted to account for the different growth function. The tumor volume x is expressed in terms of multiples of 10^6 cells and y is a dimensionless quantity that describes the immuno-competent cell density as an order of magnitude relative to base value 1.

<a id='826af4e8-51fa-4f00-b07a-a58565303f02'></a>

<table id="4-1">
<tr><td id="4-2">variable/parameters</td><td id="4-3">interpretation</td><td id="4-4">numerical value</td><td id="4-5">Ref.</td></tr>
<tr><td id="4-6">x</td><td id="4-7">tumor volume</td><td id="4-8"></td><td id="4-9">[32]</td></tr>
<tr><td id="4-a">x₀</td><td id="4-b">initial value for x</td><td id="4-c">600</td><td id="4-d"></td></tr>
<tr><td id="4-e">y</td><td id="4-f">immuno-competent cell density</td><td id="4-g"></td><td id="4-h">[32]</td></tr>
<tr><td id="4-i">y₀</td><td id="4-j">initial value for y</td><td id="4-k">0.10</td><td id="4-l"></td></tr>
<tr><td id="4-m">α</td><td id="4-n">rate of influx</td><td id="4-o">0.1181</td><td id="4-p">[13]</td></tr>
<tr><td id="4-q">β</td><td id="4-r">inverse threshold for tumor suppression</td><td id="4-s">0.00264</td><td id="4-t">[13]</td></tr>
<tr><td id="4-u">γ</td><td id="4-v">interaction rate</td><td id="4-w">1</td><td id="4-x">[13]</td></tr>
<tr><td id="4-y">δ</td><td id="4-z">death rate</td><td id="4-A">0.37451</td><td id="4-B">[13]</td></tr>
<tr><td id="4-C">μC</td><td id="4-D">tumor growth parameter</td><td id="4-E">0.5599</td><td id="4-F"></td></tr>
<tr><td id="4-G">μI</td><td id="4-H">tumor stimulated proliferation rate</td><td id="4-I">0.00484</td><td id="4-J"></td></tr>
<tr><td id="4-K">x∞</td><td id="4-L">fixed carrying capacity</td><td id="4-M">780</td><td id="4-N"></td></tr>
<tr><td id="4-O">κ</td><td id="4-P">chemotherapeutic killing parameter</td><td id="4-Q">1</td><td id="4-R"></td></tr>
</table>
TABLE 1. Numerical values for the variables and parameters used
in computations.

<a id='558a3250-68f3-46c0-8b78-43b935a6c21f'></a>

Figure 1 shows the values of the equilibria as function of ͵. The system undergoes a saddle-node bifurcation for ͵\* = 0.40355. For ͵ < ͵\*, there exists a unique globally asymptotically stable equilibrium that corresponds to a microscopic (benign) state. Medically this reflects a situation where the tumor growth is very small and the reaction of the immune system is able to control the tumor. For ͵ > ͵\* the system is multi-stable. In this case, there always exist three equilibria, a locally asymptotically stable focus (_x_b, _y_b) whose values are represented by the green curves in Fig. 1, a saddle point (_x_s, _y_s) whose values are represented by the blue curves in Fig. 1, and a locally asymptotically stable node (_x_m, _y_m) whose values are represented by the red curves in Fig. 1. For example, for classical logistic growth (͵ = 1) these values are given by (_x_b, _y_b) = (35.158, 0.537), (_x_s, _y_s) = (387.527, 0.283) and (_x_m, _y_m) = (736.102, 0.032).

<a id='2553748a-8580-4659-9253-e91ddb3a49c8'></a>

The focus ($x_b, y_b$) represents a benign equilibrium and we call its region of attraction the benign region while ($x_m, y_m$) represents a malignant equilibrium and we call its region of attraction the malignant region. The benign and malignant regions are separated by the stable manifold of the saddle ($x_s, y_s$) that forms the common boundary of these regions (separatrix). These regions are illustrated for the values $\nu = \frac{1}{2}$, 1, 2, and 4 in Fig. 2. In each of the figures, the separatrix is shown as a red curve and Fig. 3 gives the curve of saddle points for $\nu \in [\frac{1}{2}, 4]$ with a stable

<!-- PAGE BREAK -->

<a id='449b740b-5853-400a-887a-d5370cae7560'></a>

792

<a id='cb4a026f-ec8f-488e-82f3-fd3b049bd508'></a>

URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER<::chart: The figure displays two plots, one above the other, illustrating the values of equilibria for an uncontrolled system as a function of parameter v.The top plot shows "cancer volume, x" on the y-axis (ranging from 0 to 800) against "parameter, v" on the x-axis (ranging from 0 to 4). It features three curves: a green curve (benign equilibrium) that remains low and slightly increasing, a blue curve (saddle) that starts around x=600 for v around 0.4 and then decreases and flattens around x=350, and a red curve (malignant equilibrium) that starts around x=600 for v around 0.4 and then increases and flattens around x=750. A black dot is present where the blue and red curves diverge at approximately v=0.4.The bottom plot shows "immunocompetent density, y" on the y-axis (ranging from 0 to 0.7) against "parameter, v" on the x-axis (ranging from 0 to 4). It also features three curves: a green curve (benign equilibrium) that increases from y=0.3 to y=0.55, a blue curve (saddle) that increases from y=0.05 to y=0.55, and a red curve (malignant equilibrium) that remains very low, starting around y=0.05 and decreasing slightly to y=0.03.FIGURE 1. Values of the equilibria of the uncontrolled system (1) and (2) as a function of v with the x-values shown on the top and the y-values shown on the bottom. The values for the benign equilibrium point are shown as the green curve, for the saddle as the blue curve and for the malignant equilibrium point as the red curve.::>

<a id='ea3e00af-7f0e-43cf-b7fd-bd84d3688f11'></a>

eigenvector indicated in the diagram for specific values. The phase portraits shown
in Fig. 2 show the decrease of the benign region at the expense of the malignant
regions as the parameter $\nu$ increases reflecting the fact that the immune system
becomes increasingly overwhelmed by a fast growing tumor.

<a id='fb601fda-4e3b-403e-939d-2533cd0e5bcf'></a>

3. Optimal chemotherapy with tumor-immune interactions. We now consider the dynamics (1) and (2) under the action of a chemotherapeutic agent. Following standard cell-kinetic principles, the so-called *log-kill hypothesis*, we use a linear pharmacodynamic model to describe the tumor loss, i.e., assume that the elimination of tumor cells is proportional to the tumor volume *x* and the concentration of the chemotherapeutic agent which we denote by *u*. We do not include a cytotoxic effect of the chemotherapeutic agent on the immune system here. Clearly, it exists, but the interactions are complex. They might be included as a separate log-kill type term in the equation for *y*, but could also be modeled through a factor that reduces the constant influx *α* of T-cells. This term depends on the bone marrow which is one of the main recipients of the negative side effects of chemotherapeutic drugs. Essentially, in the model here we are assuming that these effects are small

<!-- PAGE BREAK -->

<a id='643f54c7-2e9e-4072-811f-7ab5f431bd5e'></a>

CHEMOTHERAPY WITH GENERALIZED LOGISTIC GROWTH 793<::A figure containing four phase portraits, labeled (a), (b), (c), and (d). Each subplot shows "cancer volume, x" on the x-axis, ranging from 0 to 800, and "immunocompetent density, y" on the y-axis, ranging from 0 to 1.5. Multiple blue lines represent trajectories. A thick black line represents a specific trajectory that starts at a high y-value, decreases in x and y, then increases in x. A red line represents another specific trajectory that generally increases. A green star is located near the origin, and a red star is located at a higher x-value and lower y-value. The positions and shapes of these elements vary slightly across the subplots based on the parameter $\nu$. Specifically:
(a) Phase portrait for $\nu = \frac{1}{2}$. The green star is around (25, 0.5) and the red star is around (650, 0.2).
(b) Phase portrait for $\nu = 1$. The green star is around (25, 0.5) and the red star is around (750, 0.2).
(c) Phase portrait for $\nu = 2$. The green star is around (25, 0.5) and the red star is around (750, 0.2).
(d) Phase portrait for $\nu = 4$. The green star is around (25, 0.5) and the red star is around (750, 0.2).

FIGURE 2. Phase portrait of the uncontrolled system (1) and (2) for the values (a) $\nu = \frac{1}{2}$, (b) $\nu = 1$, (c) $\nu = 2$, and (d) $\nu = 4$.
: chart::>

<a id='68aaad48-0dc6-4135-9f58-8efc5931442b'></a>

<::plot: chart
Caption: FIGURE 3. The curve of saddle points with a stable eigenvector indicated for values $\frac{1}{2} \leq \nu \leq 4$.
The plot shows a curve in a 2D coordinate system. The x-axis is labeled "x(v)" and ranges from approximately 300 to 600. The y-axis is labeled "y(v)" and ranges from 0 to 0.8.
A blue curve descends from left to right. Several points are marked on the curve with circles, each associated with a value of 'v' and an arrow representing a stable eigenvector.
- At approximately (340, 0.53), a point is labeled "v = 4". An arrow points upwards and to the right from this point.
- At approximately (360, 0.45), a point is labeled "v = 2". An arrow points upwards and to the right from this point.
- At approximately (390, 0.29), a point is labeled "v = 1". An arrow points upwards and to the right from this point.
- At approximately (470, 0.09), a point is labeled "v = 1/2". An arrow points upwards and to the right from this point.
::>


<!-- PAGE BREAK -->

<a id='b6305742-d287-4e1d-9af8-85ba792bb9b2'></a>

794

<a id='675e13a1-9958-434c-93f0-16d0bbc6ad72'></a>

URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER

<a id='f8036449-f59c-4840-af54-e8f001f38d85'></a>

and, in a first step, have neglected them. This can be considered a reasonable as-sumption for strongly targeted chemotherapeutic drugs. For simplicity, we also do not include a pharmacokinetic model and identify dose rates with concentrations. In other papers, e.g., [14, 17], we have investigated the relationships of optimal controls under augmentations of the system with standard linear pharmacokinetic models and generally the changes in the optimal controls are minor so that we here consider this simpler modeling approach. We normalize the maximum of the control values to 1 and subsume all the coefficients describing the effectiveness of treatment and accounting for possible heterogeneities in the composition of tumor cells (consisting of sensitive and more resistant cells) in the coefficient κ in the pharmacodynamic model. Thus, overall the controlled equations with treatment take the form

<a id='9f58033a-4b20-4ace-81bd-44db978ec60e'></a>

ẋ = µ_C x (1 - (x / x_∞)^ν) - γxy - κxu, (3)
ẏ = µ_I (x - βx²) y - δy + α. (4)

<a id='8f2e7c77-3520-47be-9765-dd36d7b9525e'></a>

Throughout the paper, we only consider M = {(x,y) : 0 < x < x∞, y > 0}, the region of interest for the problem.

<a id='24c5bf1c-920b-471f-b832-e07f26885d25'></a>

Proposition 1. The region M is positively invariant for the control system, i.e., given an arbitrary Lebesgue measurable function u : [0,T] → [0,1] defined over the interval [0,T], T≤∞, the solution to the dynamics (3) and (4) exists on [0,T] and the corresponding trajectory x lies in M..

<a id='b48a6d0d-eb01-47bd-92bd-fec7a537bd97'></a>

Proof. Since $\dot{y}|_{y=0} = \alpha > 0$, it follows that the y-components of solutions cannot cross $y = 0$ from positive to negative values. Since the initial condition $y_0$ is positive, the y-component of the solution is always positive. Furthermore, for any control $u$, $x = 0$ is an equilibrium solution to equation (3) and $\dot{x}|_{x=x_{\infty}} < 0$. Thus the x-component of the solution cannot leave the open interval $(0, x_{\infty})$. In particular, by a standard argument of ODEs, this implies that solutions exist on all of $[0, T]$. □

<a id='9ff92dd1-b941-45f2-9368-38eb278badf0'></a>

In principle, it is possible to eliminate the cancer through indefinite adminis-tration of cytotoxic agents. Obviously, side effects of the drugs need to be taken into account and this invalidates such a simplistic reasoning. This model does not include a separate compartment of healthy cells to describe the side effects of treat-ment and these are only indirectly measured through the total amounts of cytotoxic drugs given. Essentially, under a log-kill hypothesis, the drugs kill healthy cells at a proportional rate and thus the total amount of drugs given, ∫₀ᵀ u(t)dt, is used to represent the side effects of treatment. The practical aim of therapy thus becomes to move an initial state (x₀, y₀) of the system that lies in the malignant region of the uncontrolled system into the region of attraction of the stable, benign equilibrium point while keeping side effects tolerable. In an optimal control formulation, the aim is to achieve this goal in an efficient and effective way.

<a id='9ce691a4-3397-4dce-bbb0-95ae712940cd'></a>

Intuitively, such a transfer requires to minimize the cancer cells $x$ while not depleting the T-cell density $y$ too strongly. The uncontrolled system is Morse-Smale [8] and the separatrix between the benign and malignant regions is the stable manifold of the saddle point. It generally is difficult to give explicit analytic expressions for this manifold, but its tangent space is spanned by the stable eigenvector of the saddle point and thus is easily computed and can serve as a reasonable approximation. This motivates us to include in the objective a term of the form $Ax(T) - By(T)$ where $A$ and $B$ are positive coefficients determined by the stable eigenvector $\mathbf{v}$ of the saddle point $(x_s, y_s)$, $\mathbf{v} = (B, A)^T$. Minimizing this quantity, whose level sets

<!-- PAGE BREAK -->

<a id='367a5169-6d50-48c7-802c-0d927a66bfe0'></a>

CHEMOTHERAPY WITH GENERALIZED LOGISTIC GROWTH

<a id='3a5015bd-36b1-45fc-89c6-edc4f48e96c3'></a>

795

<a id='156b7bb3-cc29-4aa7-99f2-da2621f144e6'></a>

are lines parallel to the tangent space of the stable manifold of the saddle, creates an incentive for the system to move across the separatrix into the benign region. Furthermore, we keep the terminal time T in our problem formulation free and in order to avoid trajectories that use zero controls over very long time horizons, we also add a small penalty on the terminal time. It has been shown in [16] that the existence of the asymptotically stable, benign equilibrium point generates controlled trajectories that improve the value Ax(T) - By(T) of the objective along the trivial controls u = 0. These trajectories provide a "free pass" and, by taking a very long time horizon, no minimum may exist in this case. The infimum arises as the control switches to follow u = 0 when the controlled trajectory intersects the separatrix (the red curves in the phaseportraits in Fig. 2), then follows the separatrix for an infinite time to the saddle and then again leaves this saddle point along the unstable manifold, once more taking an infinite time. This indeed would be the "optimal" solution for this problem formulation, but it is not an admissible trajectory in our system. For this reason, we include a penalty term on the final time as well. This creates a well-posed mathematical problem for which the existence of solutions follows from standard theory. From a biological point of view, the addition of this term induces optimal solutions to enter the benign region rather than taking an infinite time with a smaller amount of agents. Clearly, it is not desirable for the system to evolve along the boundary between benign and malignant tumor behavior and it is the penalty term on the terminal time T that forces the system into the benign region. In view of imprecise and mathematically unmodelled dynamics and other random perturbations, from a system theoretic perspective, the addition of this term provides desired robustness and stability properties for the underlying real system.

<a id='0768ae7d-f99b-4ec3-b4f2-92a93cbaa8fb'></a>

Summarizing, we therefore consider the following optimal control problem in
Bolza form:
[OC]: for a free terminal time T, minimize the objective

<a id='ab1308ad-de23-4cda-aa4e-6cbf3fa85d64'></a>

J(u) = Ax(T) − By(T) + C ∫₀ᵀ u(t)dt + ST, (5)

<a id='e7f6d0af-b3e2-4459-889a-6b513a8c04e4'></a>

over all Lebesgue measurable functions u : [0,T] → [0, 1] subject to the dy-
namics (3) and (4),

<a id='98508e2e-2b97-48f4-9fa7-7f58c326bb46'></a>

$\dot{x} = \mu_C x \left(1 - \left(\frac{x}{x_\infty}\right)^\nu\right) - \gamma xy - \kappa xu, \quad x(0) = x_0,$
$\dot{y} = \mu_I (x - \beta x^2) y - \delta y + \alpha, \quad y(0) = y_0.$

<a id='b884aee4-205c-41f3-9684-6e82dd3e49e5'></a>

We emphasize that the coefficients in the objective (5) are variables of choice and typically will be calibrated to tailor the response of the system. The choice of the weights aims at striking a balance between the benefit at the terminal time T, Ax(T) - By(T), and the overall side effects measured by the total amount of drugs given, while it guarantees the existence of an optimal solution by also penalizing the free terminal time T. The integrals of the dose rates model the side effects of the therapies on the healthy tissue and clinical data as to the severity of the drugs should be reflected in the choice for C. Naturally, the specific type of tumor, and even the stage of cancer the patient has will enter into the choice and calibration of these coefficients. In a more advanced stage, higher side effects need to be tolerated and thus smaller values of C would need to be taken. Overall, the coefficients A,

<!-- PAGE BREAK -->

<a id='7d2a8eae-4ad5-4f3d-90aa-87e684f55624'></a>

796 URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER

<a id='5474a156-eda4-4c24-800f-06b983102258'></a>

B, C and S are variables of choice that can be fine tuned to calibrate the system's optimal response.

<a id='caedaf55-08cb-4843-836c-ebe40354cf24'></a>

Writing $z = (x, y)^T$ for the state of the system, we can express the dynamics in
the vector field form

$\dot{z} = f(z) + ug(z)$
(6)

<a id='6858686e-721d-486e-9328-4b40538ce745'></a>

where

$f(z) = \begin{pmatrix} \mu_C x \left(1 - \left(\frac{x}{x_\infty}\right)^\nu\right) - \gamma xy \\ \mu_I (x - \beta x^2) y - \delta y + \alpha \end{pmatrix}$ and $g(z) = \begin{pmatrix} -\kappa x \\ 0 \end{pmatrix}$ (7)

<a id='667e12a8-6b32-47c6-a657-c48874d9f862'></a>

are the drift and control vector field, respectively. First-order necessary conditions for optimality of a control _u_ are given by the _Pontryagin maximum principle_ ([30], for some recent texts, see [4, 5, 31]): for _λ₀_ ∈ ℝ and a 2-dimensional row-vector _λ_ = (_λ₁_, _λ₂_), define the Hamiltonian _H_ = _H_(_λ₀_, _λ_, _x_, _y_, _u_) as

<a id='7166b744-5cbf-4c98-9436-ff966ed63fa1'></a>

H = \lambda_0 (Cu+S) + \lambda_1 \left( \mu_C x \left(1-\left(\frac{x}{x_\infty}\right)^\nu\right) - \gamma xy - \kappa xu \right)
+ \lambda_2 \left( \mu_I (x - \beta x^2) y - \delta y + \alpha \right),
(8)

<a id='dfef9b95-38e3-4880-9c48-36f35cf4c03a'></a>

or, equivalently, in terms of the vector fields f and g, as

H = λ0S + ⟨λ, f(z)⟩ + u (λ0C + ⟨λ, g(z)⟩). (9)

<a id='657902d1-51ce-4820-902d-26de9e0aeaea'></a>

If $u_*$ is an optimal control defined over an interval $[0, T]$ with corresponding trajec-tory $z_* = (x_*, y_*)^T$, then there exist a constant $\lambda_0 \ge 0$ and an absolutely continuous covector $\lambda = (\lambda_1, \lambda_2)$, also defined on $[0, T]$, such that the following conditions hold:
(a) $\lambda_0$ and $\lambda(t) = (\lambda_1(t), \lambda_2(t))$ do not vanish simultaneously, (b) $\lambda_1$ and $\lambda_2$ satisfy the adjoint equations

<a id='65d25253-e9c4-4bfe-b7a1-7093a63868bd'></a>

$$\dot{\lambda_1} = -\frac{\partial H}{\partial x} = \lambda_1 \left( \mu_C \left( -1 + (\nu+1)\left(\frac{x}{x_\infty}\right)^\nu \right) + \gamma y + u\kappa \right) - \lambda_2 \mu_I (1 - 2\beta x) y,$$ (10)

<a id='b1a4b629-0437-488c-8f2a-58c1c56c6eb9'></a>

λ̇₂ = -∂H/∂y = λ₁γx - λ₂ (μ_I (x - βx²) - δ), (11)

<a id='35c262e1-37f2-4f46-a8e1-5294862079fb'></a>

with terminal conditions \lambda_1(T) = \lambda_0A and \lambda_2(T) = -\lambda_0B, and (c) for almost every time t \in [0,T], the optimal control u_*(t) minimizes the Hamiltonian H along (\lambda_0, \lambda(t), x_*(t), y_*(t)) over the control set [0, 1] with minimum value given by 0.

<a id='c76f8552-6dbc-4489-88f4-03c30d50ab77'></a>

Since the Lagrangian, the integral term in the objective, does not depend on the state variables $x$ and $y$, the adjoint equations can be succinctly expressed in the form

<a id='93894e29-3652-4ab5-93c0-29c3a54a6310'></a>

λ̇(t) = -λ(t) (Df(z*(t)) + u*(t)Dg(z*(t))) (12)

<a id='931fa5a5-baff-44b9-959c-998d9d565eba'></a>

where $Df$ and $Dg$ denote the matrices of the partial derivatives of the vector fields $f$ and $g$, respectively.

<a id='7bceb799-dc5c-4304-bc1f-f14faffe67e6'></a>

A controlled trajectory $((x, y), u)$, consisting of an admissible control $u$ and corresponding solution $(x, y)$ of the initial value problem (3) and (4), for which there exist multipliers $\lambda_0$ and $\lambda$ such that the conditions of the maximum principle are satisfied is called an extremal (pair) and the triple $((x, y), u, (\lambda_0, \lambda))$ is an extremal lift (to the cotangent bundle). If the multiplier $\lambda_0 = 0$, the extremal is called abnormal while it is called normal if $\lambda_0 > 0$. In this case, by dividing by $\lambda_0$, it is always possible to normalize $\lambda_0 = 1$. For our problem, it is easily seen that all extremals are normal. For, if $\lambda_0 = 0$, then the terminal conditions for the adjoint equation are given by $\lambda_1(T) = \lambda_2(T) = 0$ and thus, as solutions of the homogeneous

<!-- PAGE BREAK -->

<a id='a9e3eecd-a6ba-4dd7-8213-d517fc0dbc18'></a>

CHEMOTHERAPY WITH GENERALIZED LOGISTIC GROWTH 797

<a id='faf477aa-4a33-4459-838c-8062ac00b4ef'></a>

linear differential equations (10) and (11), λ₁(t) and λ₂(t) vanish identically. But this contradicts condition (a), the nontriviality of the multipliers. Thus extremals are normal and henceforth we take λ₀ = 1.

<a id='31884c28-7338-4381-90f4-d2acc76f5ac1'></a>

By condition (c), an optimal control $u_*(t)$ minimizes the Hamiltonian $H$ along the extremal $(\lambda(t), x_*(t), y_*(t))$ over the control set $[0, 1]$ a.e. on $[0,T]$. Since $H$ is linear in the controls and the control set is an interval, this minimization is easily carried out. Defining the *switching function* $\Phi$ for the control as

<a id='b281cd59-96e8-469d-93aa-a9b00b419776'></a>

$\Phi(t) = C + \langle\lambda(t), g(z_*(t))\rangle = C - \lambda_1(t)\kappa x_*(t), \quad (13)$

<a id='9fdd83d4-ba45-4a35-9350-83c665b73e19'></a>

it follows that

u*(t) = 
{
0 if Φ(t) > 0,
1 if Φ(t) < 0.

(14)

<a id='f9f93742-5b9b-4c20-9613-5ec6f912902f'></a>

We refer to the constant controls given by the values 0 and 1 as the *bang* controls. The minimum condition itself does not determine the control at times τ when the switching function vanishes, Φ(τ) = 0, but if the time-derivative Φ̇(τ) does not vanish, then the control switches at τ between its extreme values 0 and 1 with the order depending on the sign of Φ̇(τ). Thus also the name of bang-bang controls. In the other extreme, if Φ(t) ≡ 0 on an open interval *I*, then all derivatives of Φ(t) must vanish as well and typically this does allow to compute the control. Controls of the second kind are called *singular* [4, 31]. Corresponding trajectories are called singular arcs. Overall, optimal controls need to be synthesized from these classes of candidates.

<a id='36a6369a-9205-4d50-b364-a1a6aba691bb'></a>

We analyze singular controls. The proposition below, which is verified with a direct computation, provides a simple and efficient formalism for the computation of these derivatives.

<a id='933e22b2-96a6-4718-9654-89de7f48cb1e'></a>

**Proposition 2.** Let z(.) be a solution of the dynamics (6) for the control u and
let λ be a solution of the corresponding adjoint equation (12). For a continuously
differentiable vector field h, let

<a id='6dd13ad7-37b9-4478-8aaf-e3361328d208'></a>

Ψ(t) = ⟨λ(t), h(z(t))⟩. (15)

<a id='356d43cc-0c07-4d18-b2f2-fdece25d3738'></a>

Then the derivative of Ψ is then given by

<a id='1ba4fbf9-b123-48a7-bc86-f8f0940d089c'></a>

Ψ̇(t) = ⟨λ(t), [f + ug, h](z(t))⟩,

(16)

<a id='d88d9efe-e426-4bce-a244-18f7f556e269'></a>

where $[k, h](z) = Dh(z)k(z) - Dk(z)h(z)$ denotes the Lie bracket of the vector fields k and h.

<a id='f091e9fb-5b71-4b8b-af32-ff285f474cb8'></a>

For example, since $[k, k] \equiv 0$ for any vector field $k$, the first two derivatives of the switching functions $\Phi$ are given by

<a id='196772e7-17a6-42f1-bc6b-77bc29894b6c'></a>

$$\dot{\Phi}(t) = \langle\lambda(t), [f, g](z_*(t))\rangle \tag{17}$$

<a id='2a7d49b0-33fb-47b5-b326-a58d7892a270'></a>

and

$\ddot{\Phi}(t) = \langle \lambda(t), [f + u_*(t)g, [f, g]](z_*(t))\rangle$.
(18)

<a id='4a832ab3-6133-440c-968b-55a6271ee80a'></a>

A singular control is said to be of order 1 over an interval I if the quantity
⟨λ(t), [g, [f, g]](z*(t))⟩ does vanish on I. In this case, we can formally solve for
the singular control u_sing as

<a id='f9916532-7492-4cec-ab0a-ea891293f108'></a>

$$u_{\text{sing}}(t) = -\frac{\langle\lambda(t), [f, [f, g]](z_{*}(t))\rangle}{\langle\lambda(t), [g, [f, g]](z_{*}(t))\rangle} \quad (19)$$

<!-- PAGE BREAK -->

<a id='738ddf7e-1c62-4e45-88aa-1263fc4357d9'></a>

798 URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER

<a id='a73d9459-c844-44cf-b2d7-b40974aa678e'></a>

and it is a high-order necessary condition for optimality, the so-called Legendre-
Clebsch condition, that

<a id='21a0c294-ffbf-4167-8e71-c0fb97d738fa'></a>

$$\langle\lambda(t), [g, [f, g]](z_*(t))\rangle < 0 \quad \text{for all} \quad t \in I. \quad (20)$$

Direct computations verify that

$$[f,g](z) = \kappa \begin{pmatrix} -\mu_C \left(\frac{x}{x_\infty}\right)^\nu vx \\ \mu_I (x - 2\beta x^2) y \end{pmatrix} \quad \text{and} \quad [g, [f,g]](z) = \kappa^2 \begin{pmatrix} \mu_C \left(\frac{x}{x_\infty}\right)^\nu v^2x \\ \mu_I (4\beta x^2 - x) y \end{pmatrix}.$$

Analyzing these conditions, we obtain the following result:

<a id='56b237a9-1fdd-4050-bd69-f7c749cf8313'></a>

**Proposition 3.** For the problem [OC], singular controls are of order 1 and the Legendre-Clebsch condition is satisfied if and only if

$$\nu<\frac{1-4\beta x_{*}(t)}{1-2\beta x_{*}(t)}. \qquad (21)$$

<a id='372c8d6f-f8b4-4bc5-b25d-4c9a821418b1'></a>

Proof. Suppose the control u* is singular over an open interval I. Then we have Φ(t) \equiv 0 on I, i.e., λ₁(t)κx*(t) = C > 0 and thus λ₁ is positive along a singular arc. Therefore the condition that Φ̇(t) \equiv 0 on I implies that

<a id='8f2a219f-07f3-4aeb-a922-710c9b74dcc6'></a>

$\lambda_2(t)\mu_I (1 - 2\beta x_*(t)) y_*(t) \equiv \lambda_1(t)\mu_C \left(\frac{x_*(t)}{x_\infty}\right)^\nu \quad \nu > 0.$

<a id='e927d5f8-52b4-4afd-aba5-c9ef80690070'></a>

Evaluating the Legendre-Clebsch condition, and using this relation to eliminate the multiplier λ2, we therefore obtain that

<a id='bf2ce4a8-81c7-4192-8237-1e28775f6d3f'></a>

$$\langle\lambda(t), [g, [f, g]] (z_*(t))\rangle$$
$$= \kappa^2 \left\{\lambda_1(t)\mu_C \left(\frac{x_*(t)}{x_\infty}\right)^\nu \nu^2 x_*(t) + \lambda_2(t)\mu_I \left(4\beta x_*(t)^2 - x_*(t)\right) y_*(t)\right\}$$
$$= \kappa^2 \lambda_1(t)x_*(t) \left\{\mu_C \left(\frac{x_*(t)}{x_\infty}\right)^\nu \nu^2 + \frac{\mu_C \left(\frac{x_*(t)}{x_\infty}\right)^\nu \nu}{1 - 2\beta x_*(t)} \left(4\beta x_*(t) - 1\right)\right\}$$
$$= \kappa^2 \lambda_1(t)\mu_C \left(\frac{x_*(t)}{x_\infty}\right)^\nu \nu x_*(t) \left\{\nu - \frac{1 - 4\beta x_*(t)}{1 - 2\beta x_*(t)}\right\} \quad (22)$$

<a id='2edc68f0-0bb4-43d7-80b4-b1e5ca2aa2e2'></a>

Since λ₁(t) is positive along a singular arc, this implies that equation (20) holds if and only if (21) is satisfied. □
This determines the following intervals along which an optimal control can be singular dependent on the parameter ν.

<a id='7c2a1cdc-1655-4eb7-b1e6-42617f2b07f1'></a>

**Corollary 1.** _Suppose an optimal control_ $u_*$ _is singular at time t. Then, we have that_

1.  _if_ $0 < \nu < 1$, _we have either_ $0 \le \beta x_*(t) < \frac{1-\nu}{2-\nu} < \frac{1}{4}$ _or_ $\frac{1}{2} < \beta x_*(t)$,
2.  _if_ $1 \le \nu \le 2$, _then_ $\frac{1}{2} < \beta x_*(t)$ _and_
3.  _if_ $\nu > 2$, _then_ $\frac{1}{2} < \beta x_*(t) < \frac{1-\nu}{2-\nu}$.

<a id='4cdb0140-79de-487d-9991-f343e862b26f'></a>

These relations readily follow from condition (21) and are illustrated in Figure 4. In the limiting case $\nu \to 0$ we obtain that the Legendre-Clebsch condition is satisfied on the intervals $[0,\frac{1}{4}) \cup (\frac{1}{2},\infty)$ and this agrees with the result obtained in [16] for a Gompertzian growth function. As $\nu$ increases, these intervals continuously shrink until, in the limit $\nu \to \infty$, for exponential growth singular controls no longer are optimal.

<!-- PAGE BREAK -->

<a id='3b44ca4a-2aaa-42c6-9862-a9bab583316d'></a>

CHEMOTHERAPY WITH GENERALIZED LOGISTIC GROWTH 799<::chart: The chart shows a 2D plot with 'v' on the y-axis (ranging from 0 to 6) and 'βx' on the x-axis (ranging from 0 to 3). A vertical line is present at approximately x = 0.5. A curve starts from the bottom left, goes up to the vertical line, and then another curve starts from the top of the vertical line and decreases towards the right. Horizontal dashed-dot lines are present at y = 1 and y = 2. Several horizontal gray lines are also visible, particularly between y = 1 and y = 2, and above y = 2, extending to the right of the vertical line. The region bounded by the vertical line at x=0.5, the decreasing curve, and the horizontal lines between y=1 and y=2 appears to be highlighted by the gray lines. FIGURE 4. The highlighted region represents the intervals (horizontally, for fixed value of ν and scaled as βx) on which the Legendre-Clebsch condition for minimality of singular arcs is satisfied::>

<a id='3f148940-6074-4f90-88e8-8669f94f3cb3'></a>

We now compute the singular control and singular arcs. Along a singular control we have that $\Phi = C + \langle\lambda, g(z_*)\rangle \equiv 0$, $\dot{\Phi} = \langle\lambda, [f,g](z_*)\rangle \equiv 0$ and also $H = S + \langle\lambda, f(z_*)\rangle + u\Phi \equiv 0$. It thus follows that the multiplier $\lambda(t)$ vanishes against both the vector fields $Sg - Cf$ and $[f,g]$ along a singular arc. Since $\lambda$ is nonzero (as nontrivial solution to a homogeneous linear ODE), it follows that singular arcs can only lie in the set $S$ where $Sg - Cf$ and $[f,g]$ are linearly dependent,

<a id='8e568567-3adb-420a-b236-30e2908a738d'></a>

$$ \mathcal{S} = \{z \in \mathbb{M} : \det (Cf(z) - Sg(z), [f, g](z)) = 0\} . \qquad (23) $$

<a id='20ecf6d2-f588-44bf-81e4-96520084e650'></a>

This leads to the relation

<a id='d1acdba5-ba15-4d2f-88da-2775f2bbfa91'></a>

det (
  C [μ_C (1 - (x/x_∞)^ν) - γy] + S_κ   -μ_C (x/x_∞)^ν
  C [μ_I (x - βx²) y - δy + α]        μ_I (x - 2βx²) y
) = 0

<a id='04b62a5c-9959-4c63-b5ee-d927b23cade6'></a>

which takes the form
$Q(x, y) = a_0(x) + a_1(x)y + a_2(x)y^2 = 0$

<a id='8b31cd7b-4f6f-4554-8309-2cee0bd30b13'></a>

where
a₀(x) = CμCαν (x/x∞)^ν > 0 and a₂(x) = CμIγ (2βx - 1)x.

<a id='a4d57d89-edee-4ac0-81ee-04ff25ff5882'></a>

In the region where βx > ½, the coefficient a₂(x) is positive and thus, for a given value of x, there exist 0, 1 or 2 solutions y = y_sing(x) that define possible singular arcs. On the other hand, a₂(x) is negative for βx < ¼ and in this case there always exists a unique solution y = y_sing(x) for the singular arc. Generally, singular arcs are defined through this relation as function of x. The associated singular control is the defined in equation (19) and it is admissible if its values lie in the interval [0, 1].

<!-- PAGE BREAK -->

<a id='234c3eb1-cd76-4030-92df-7c7d71784db5'></a>

800 URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER

<a id='c20377f2-0a20-4494-92e3-119ebbc878d7'></a>

## 4. Conclusion and discussion. Following the approach introduced in [15] and [16], in this paper we analyzed tumor-immune interactions under chemotherapy with a targeted agent for Stepanova's model with a generalized logistic rate function F(x) = μ_C (1 - (x/x_∞)^ν), ν > 0. The parameter ν in the model allows to differentiate the tumor growth rate with Gompertzian and exponential models forming the limiting cases. For a specific set of parameters, we analyzed the multi-stability of the underlying system leading to both benign and malignant regions of dynamic behavior and then, for the general model, investigated the optimal control problem of transferring an initial condition that lies in the malignant region into the benign region under chemotherapy. Our results about optimal singular controls for the generalized logistic growth provide a natural interpolation between the Gompertzian and exponential models and, together with our previous results in [16], suggest that singular controls, which administer agents at less than maximum dose, may play an essential part of optimal solutions in phases when the tumor is growing slowly, but will be replaced with bang-bang structures which correspond to the traditional maximum tolerated dose (MTD) approaches it tumor growth is fast.

<a id='dab75cb3-4495-4714-af12-f423fba1929f'></a>

From a practical side, this indicates the use of partial lower doses, maybe even a metronomic scheduling, for slowly growing tumors. In such a treatment approach, chemotherapy essentially is given at low concentrations over prolonged periods with- out any major interruptions. As more aspects of the tumor microenvironment are taken into account, antiangiogenic and/or immunostimulatory effects that such schedules exhibit (e.g., see [27, 35]) have been suggested as possible mechanisms that would explain the effectiveness of such therapy schedules in some cases (e.g., [28]). In the context of angiogenic signaling, theoretical evidence also points to the optimality of such schedules [9] as well as to a metronomic scheduling of antiangio- genic agents [25]. Generally, because of the ubiquity of immunoediting, it would be important to also consider the evolution of the tumor-immune system dynam- ics over time [1, 24], but this requires further modeling efforts. In this paper, a stationary point of view (represented by the coefficient v) was taken.

<a id='c0fe31fb-407d-490e-90e4-03ef4d43d8c4'></a>

**Acknowledgments.** This material is based upon research supported by the National Science Foundation under collaborative research grants DMS 1008209 and 1008221. We also would like to thank an anonymous referee for most valuable comments.

<a id='7f5a318f-c2d0-4c98-9e54-fab2370bc7f3'></a>

## REFERENCES
[1] M. M. Al-Tameemi, M. A. J. Chaplain and A. d'Onofrio, *Evasion of tumours from the control of the immune system: Consequences of brief encounters*, Biology Direct, **7** (2012), 31.
[2] N. Bellomo and N. Delitala, From the mathematical kinetic, and stochastic game theory for active particles to modelling mutations, onset, progression and immune competition of cancer cells, Physics of Life Reviews, **5** (2008), 183-206.
[3] N. Bellomo and L. Preziosi, *Modelling and mathematical problems related to tumor evolution and its interaction with the immune system*, Mathematical and Computational Modelling, **32** (2000), 413-452.
[4] B. Bonnard and M. Chyba, "Singular Trajectories and their Role in Control Theory," Springer Verlag, Series: Mathematics and Applications, **40** (2003).
[5] A. Bressan and B. Piccoli, "Introduction to the Mathematical Theory of Control," American Institute of Mathematical Sciences, 2007.
[6] G. P. Dunn, L. J. Old and R. D. Schreiber, *The three ES of cancer immunoediting*, Annual Review of Immunology, **22** (2004), 322-360.

<!-- PAGE BREAK -->

<a id='4b499702-7827-4447-b04e-50c32b4061d3'></a>

CHEMOTHERAPY WITH GENERALIZED LOGISTIC GROWTH

<a id='382819de-edfd-4ba2-a5cf-55982fd47f65'></a>

801

<a id='665959a1-8ffc-424a-a400-0a736677a03e'></a>

[7] A. Friedman, Cancer as multifaceted disease, Mathematical Modelling of Natural Phenomena, 7 (2012), 1-26. [8] J. Guckenheimer and P. Holmes, "Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields," Springer Verlag, New York, 1983. [9] P. Hahnfeldt, J. Folkman and L. Hlatky, Minimizing long-term burden: the logic for metronomic chemotherapeutic dosing and its angiogenic basis, J. of Theoretical Biology, 220 (2003), 545-554. [10] T. J. Kindt, B. A. Osborne and R. A. Goldsby, "Kuby Immunology," W. H. Freeman, 2006. [11] D. Kirschner and J. C. Panetta, Modeling immunotherapy of the tumor-immune interaction, J. of Mathematical Biology, 37 (1998), 235-252. [12] C. M. Koebel, W. Vermi, J. B. Swann, N. Zerafa, S. J. Rodig, L. J. Old, M. J. Smyth and R. D. Schreiber, Adaptive immunity maintains occult cancer in an equilibrium state, Nature, 450 (2007), 903-905. [13] V. A. Kuznetsov, I. A. Makalkin, M. A. Taylor and A. S. Perelson, Nonlinear dynamics of immunogenic tumors: Parameter estimation and global bifurcation analysis, Bulletin of Mathematical Biology, 56 (1994), 295-321. [14] U. Ledzewicz, M. Faraji and H. Schättler, On optimal protocols for combinations of chemo- and immunotherapy, Proceedings of the 51st IEEE Proceedings on Decision and Control, Maui, Hawaii, (2012), 7492-7497. [15] U. Ledzewicz, M. Naghnaeian and H. Schättler, Dynamics of tumor-immune interactions under treatment as an optimal control problem, Proceedings of the 8th AIMS Conference, Dresden, Germany, (2010), 971-980. [16] U. Ledzewicz, M. Naghnaeian and H. Schättler, Optimal response to chemotherapy for a mathematical model of tumor-immune dynamics, J. of Mathematical Biology, 64 (2012), 557-577. [17] U. Ledzewicz and H. Schättler, The influence of PK/PD on the structure of optimal control in cancer chemotherapy models, Mathematical Biosciences and Engineering (MBE), 2 (2005), 561-578. [18] A. Matzavinos, M. Chaplain and V. A. Kuznetsov, Mathematical modelling of the spatio- temporal response of cytotoxic T-lymphocytes to a solid tumour, Mathematical Medicine and Biology, 21 (2004), 1-34. [19] A. d'Onofrio, A general framework for modeling tumor-immune system competition and immunotherapy: mathematical analysis and biomedical inferences, Physica D, 208 (2005), 220-235. [20] A. d'Onofrio, Tumor-immune system interaction: Modeling the tumor-stimulated proliferation of effectors and immunotherapy, Mathematical Models and Methods in Applied Sciences, 16 (2006), 1375-1401. [21] A. d'Onofrio, Tumor evasion from immune control: Strategies of a MISS to become a MASS, Chaos, Solitons and Fractals, 31 (2007), 261-268. [22] A. d'Onofrio, Metamodeling tumor-immune system interaction, tumor evasion and immunotherapy, Mathematical and Computational Modelling, 47 (2008), 614-637. [23] A. d'Onofrio, Cellular growth: Linking the mechanistic to the phenomenological modeling and vice-versa, Chaos, Solitons and Fractals, 41 (2009), 875-880. [24] A. d'Onofrio and A. Ciancio, Simple biophysical model of tumor evasion from immune system control, Physical Review E, 84 (2011). [25] A. d'Onofrio, A. Gandolfi and A. Rocca, The cooperative and nonlinear dynamics of tumor- vasculature interaction suggests low-dose, time-dense antiangiogenic schedulings, Cell Proliferation, 42 (2009), 317-329. [26] D. Pardoll, Does the immune system see tumors as foreign or self?, Annual Reviews of Immunology, 21 (2003), 807-839. [27] E. Pasquier, M. Kavallaris and N. André, Metronomic chemotherapy: new rationale for new directions, Nature Reviews Clinical Oncology, 7 (2010), 455-465. [28] K. Pietras and D. Hanahan, A multitargeted, metronomic, and maximum-tolerated dose "chemo-switch" regimen is antiangiogenic, producing objective responses and survival benefit in a mouse model of cancer, J. of Clinical Oncology, 23, (2005), 939-952. [29] L. G. de Pillis, A. Radunskaya and C. L. Wiseman, A validated mathematical model of cell- mediated immune response to tumor growth, Cancer Research, 65 (2005), 7950-7958. [30] L. S. Pontryagin, V. G. Boltyanskii, R. V. Gamkrelidze and E. F. Mishchenko, "The Mathematical Theory of Optimal Processes," MacMillan, New York, 1964.

<!-- PAGE BREAK -->

<a id='3eb666b0-8945-4fa5-8f63-671b990eccb6'></a>

802 URSZULA LEDZEWICZ, OMEIZA OLUMOYE AND HEINZ SCHÄTTLER

<a id='a91d6970-aa0d-4269-9c1b-09acdc12bb23'></a>

[31] H. Schättler and U. Ledzewicz, "Geometric Optimal Control: Theory, Methods and Examples," Springer Verlag, 2012.
[32] N. V. Stepanova, Course of the immune reaction during the development of a malignant tumour, Biophysics, 24 (1980), 917-923.
[33] J. B. Swann and M. J. Smyth, *Immune surveillance of tumors*, J. of Clinical Investigations, 117 (2007), 1137-1146.
[34] H. P. de Vladar and J. A. González, *Dynamic response of cancer under the influence of immunological activity and therapy*, J. of Theoretical Biology, 227 (2004), 335-348.
[35] S. D. Weitman, E. Glatstein and B. A. Kamen, *Back to the basics: the importance of concentration x time in oncology*, J. of Clinical Oncology, 11 (1993), 820-821.

<a id='f09ee864-f963-4446-b46f-cc0d4c19cab9'></a>

Received September 21, 2012; Accepted January 30, 2013.

E-mail address: uledzew@siue.edu
E-mail address: oolumoy@siue.edu
E-mail address: hms@wustl.edu
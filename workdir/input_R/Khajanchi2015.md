<a id='f5d61129-6cec-42f6-bd4c-135207a14cba'></a>

Applied Mathematics and Computation 271 (2015) 375–388

<a id='74c0c364-9958-4352-b1a0-0930c4207641'></a>

<::logo: Elsevier
NON SOLLVS
A detailed black and white illustration of a tree with a figure next to it, above the orange text "ELSEVIER"::>

<a id='d9ddaf78-7c4e-41c2-b66f-7a83864f28be'></a>

Contents lists available at ScienceDirect

Applied Mathematics and Computation

journal homepage: www.elsevier.com/locate/amc

<a id='7c262287-ae83-4d14-bed4-821d82062391'></a>

ELSEVIER

ISSN 0096-3003

APPLIED
MATHEMATICS
AND
COMPUTATION

<a id='e040143e-9db3-43e1-922a-6f60567325df'></a>

The combined effects of optimal control in cancer remission

<a id='8f7d5155-9085-449f-a464-aacbccee2183'></a>

<::logo: CrossMark
CrossMark
A red bookmark-like symbol is centered within a blue and grey circular icon.::>

<a id='a70343e5-bfd8-42fd-a4d0-f299d998d6be'></a>

Subhas Khajanchi a,b, Dibakar Ghosh C,*
a Department of Mathematics, Indian Institute of Technology Roorkee, Uttaranchal - 247667, India
b Department of Mathematics, Bankura University, Bankura - 722146, India
c Physics and Applied Mathematics Unit, Indian Statistical Institute, Kolkata - 700108, India

<a id='e3b9608d-d794-4e6b-83a6-75d176ba743c'></a>

ARTICLE INFO

Keywords:
Optimal Control
Adoptive Cellular Immunotherapy (ACI)
Pontryagin's Maximum Principle
Immune Effector cells

<a id='de64bd9f-dde6-48b8-ad3f-80ad2c82eb1b'></a>

ABSTRACT

We investigate a mathematical model depicting the nonlinear dynamics of immunogenic tumors as envisioned by Kuznetsov et al. [1]. To understand the dynamics under what circumstances the cancer cells can be eliminated, we implement the theory of optimal control. We design two types of external treatment strategies, one is Adoptive Cellular Immunotherapy and another is interleukin-2. Our aim is to establish the treatment regimens that maximize the effector cell count and minimize the tumor cell burden and the deleterious effects of the total amount of drugs. We derive the existence of an optimal control by using the boundedness of solutions. We characterize the optimality system, in which the state system is coupled with co-states. The uniqueness of an optimal control of our problem is also analyzed. Finally, we demonstrate the numerical illustrations that the optimal regimens reduce the tumor burden under different scenarios.

<a id='7ff40d70-2a39-483e-942f-63df9b82390a'></a>

© 2015 Elsevier Inc. All rights reserved.

<a id='55e93aba-2806-44b5-b9ef-a73869a9ebef'></a>

# 1. Introduction
Cancer is a worldwide problem caused by the proliferation of tumor cells which destroy the surrounding tissues of our body. But, it is still an enigma about its proliferation, destruction and its mechanism of establishment. When the tumor cells can grow, it is necessary for them to take treatment depend upon their devastating nature, malignancy and their sequestered locations. In most of the cases surgery, chemotherapy, hormone therapy and radiation therapy failed to eliminate the cancerous cells. Despite the advances of clinicians, there are so much challenges remain to diagnosis and the treatment of cancers. So our aim is not only prevent the measure of cancer, but also investigate the successful treatment strategies through cancer immune reactions or immunotherapeutic approach to eliminate cancer.

<a id='0999bd12-5c7d-4ef6-bc79-e3d01dca5239'></a>

The immunotherapy naturally stimulate our immune system to work harder against foreign organisms such as cancers. The immunological therapy can refer to as the antigen and non-antigen specific agents such as cytokine usually along with Adoptive Cellular Immunotherapy (ACI) [15-19]. Cytokines are protein hormones that mediate cell growth and activate our immune system response. Cytokines can provide the immune system a boost or given with different immunotherapies they can be used as adjuvants [38]. Interleukin-2 (IL-2) is the main cytokine (approved by Food and the Drug Administration (FDA) in 1992) responsible for the activation of T-cells (Lymphocytes) growth and differentiation. It is produced by Helper-T (CD4 + T) cells and CD8 + T cells (Cytotoxic-T-Lymhocytes or CTLs). IL-2 acts on the same cells and produce them and alter the near by T-Lymphocytes. Therefore, we can infer to as an autocrine growth factor and an paracrine growth factor. IL-2 also used as a chemotherapeutic drug and has generic name Aldesleukin (http://chemocare.com/chemotherapy/drug-info/il-2.asp). IL-2 has been accepted for the

<a id='f253184a-8292-4e5a-9e77-3d885e5915a6'></a>

* Corresponding author. Tel.: +03325753024.
E-mail address: dibakar@isical.ac.in (D. Ghosh).

<a id='e27c6fcb-c81e-470b-9a3c-b0ecde94cad6'></a>

http://dx.doi.org/10.1016/j.amc.2015.09.012
0096-3003/© 2015 Elsevier Inc. All rights reserved.

<!-- PAGE BREAK -->

<a id='d47f6bff-e69e-4e54-8b94-849681677aa0'></a>

376

<a id='83f91ad4-eaba-4998-baa5-9e310caf8a37'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375-388

<a id='7d51f528-48f8-4fc1-8e6f-0690a9fea3e1'></a>

treatment of cancer with high dosage regimen [14]. IL-2 is a paramount cytokine that mediate the proliferation of cells, enhance the production of several cytokine and stimulate CTLs activity at different stages [17,19] and also promote the functions of Natural Killer (NK) cells.

<a id='b9869f37-c443-4cd8-afc7-e369ba08fbb4'></a>

Adoptive Cellular Immunotherapy is refers to as the boosting and expansion of the immune system externally in the cultured of immune cells. In the tumor bearing host, ACI has an anti-tumor activity which can be achieved in conjunction with high dosage human recombinant interleukin-2. This can happen in two distinct ways: (a) Lymphokine - activated - killer (LAK) cell therapy and (b) Tumor Infiltrating Lymphocyte (TIL) therapy. In [20], Kirschner and Panetta discussed in detail the activity of LAK and TIL therapy.

<a id='2a33848c-0d0b-4968-9da7-6370b4ed3023'></a>

To understand the dynamics of tumor cells and their environment from the context of mathematical modeling have been studied by numerous researchers [1,3,4,20-22,24-26,28,29]. The delay introduced to the biological system may cause the arising of phenomena such as existence of stability switches of the steady state [31], appearance of Hopf-bifurcation and periodic solu- tions or chaos [8,27,30]. But, our aim of this paper is to study the dynamic behavior of tumor-immune interaction through the application of optimal control technique. There is a large body of literature that addresses on the applications of optimal control strategy for immunotherapy in cancer dynamics [11,13,14,23,32-38]. Fister and Donnelly [38] implement the optimal control theory to obtain under what situations the cancer cells can be eliminated. They showed that the bang-bang control exists for two linear optimal control problem and cancer cells have cyclic nature during therapy. Chakrabarty and Banerjee [14] studied a mathematical model of cancer remission that include two external treatments of ACI and IL-2 therapy based on numerical simulations. Castiglione and Piccoli [32] presented a mathematical model of the competition between tumor cells and their en- vironment, and after that they applied the optimal control theory to obtain when and in which extent the immune system can be stimulated by immunotherapeutic treatment regimens during the treatment period in the finite time horizon. Fister and Panetta [33] developed an optimal treatment strategies for the chemotherapeutic treatment administered by using optimal control the- ory. They studied the qualitative behavior of three distinct cell-kill models, both analytically and numerically. They also observed that the distinct treatment policies which depend on the distinct cost functions. De Pillis et al. [34] explored a magnificent math- ematical model to understand the dynamics of cancer and immune system reactions in addition to chemotherapy. The authors developed the existence of optimal control theory and solved in both the quadratic and linear optimal control. They compared optimal treatment strategies, in quadratic control, linear control and state-constraint. In the article [34], the authors showed by graphical representations that the regions on which the singular control is optimal. Burden et al. [35] considered a mathemati- cal model of cancer dynamics that include immune-effector cells and interleukin-2 (IL-2). The authors used the optimal control theory to obtain the optimal treatment strategy by external injections of adoptive cellular immunotherapy against tumor cells. Swan [37] studied the optimal control theory and established feedback treatment control and the characterization of drugs for tumor models under the hypothesis of quadratic control performance criteria. Murray [36] studied a mathematical model of tumor cells and the normal cells under the conjectures of logistic growth fashion and Gompertzian growth fashion, whereby the rate of administration of therapies is controlled. At the end of the treatment, the tumor cell burden is minimized, in different implementation, the level of toxicity, interpreted as the area under the concentration curve. De Pillis and Radunskaya [23] stud- ied and improved a more pragmatic mathematical model of tumor cells, normal cells and immune cells with drug therapy and achieved a new treatment strategy which shows that the total amount of tumor mass being small at the end of the treatment period. To the best of our knowledge, the combined effects of drug therapies has not been explored so far in cancer dynamics by analytically and numerically. But, the effects of a single drug in cancer dynamics using optimal controls are done analytically by Fister and Donnelly [38], Fister and Panetta [33], De Pillis [23,34].

<a id='12c6c5e1-3a35-48e2-8360-b53b4b95e659'></a>

In this paper, we use the deterministic optimal control theory to obtain the effectiveness of an optimal treatment strategies for the two therapies ACI and IL-2. Also, we minimize the total number of tumor burden and the deleterious effect of drugs and maximize the total amount of effector cells. The subsequent part of this paper is as follows: we briefly describe the system of nonlinear differential equations which address the cancer-immune system interaction model in Section 2. By keeping the biomedical aim in our mind, we formulate the optimal control problem in Section 3. In Section 4, we investigate the existence of an optimal control pair. In the same section, we characterize the optimal control problem by using the Pontryagin's Maximum Principle. We then analyze the uniqueness of the optimality system, in which the state system coupled with co-states in Section 5. We perform numerical simulations for our problem in Section 6. The paper ends with a conclusion in Section 7.

<a id='507b4f0a-f12c-4f0c-b140-45c7539fc1fe'></a>

2. Mathematical model

In this section, we will study the model of cancer dynamics originally represented by Kuznetsov et al. [1]. The mathematical model is akin to a prey-predator system which comprises a system of two nonlinear ordinary differential equation's (ODEs) namely, the activated immune - effector cells (ECs) and tumor cells (TCs) in a single tumor-site compartment model. The system of coupled nonlinear ODEs is defined as follows:

<a id='d1d2a187-64c9-4972-871f-a75869cf3334'></a>

$$\frac{dE}{dt} = s\epsilon_1(t) + \frac{pET}{g+T} - mET - dE,$$$$\frac{dT}{dt} = aT(1-bT) - nET - \epsilon_2(t)T,\quad(1)$$

<a id='4eab0d88-3b6e-4f96-aea9-3b0f7ba9e905'></a>

satisfying the initial conditions E(0) = E₀ and T(0) = T₀ are known. ε₁(t) and ε₂(t) are the time dependent drug efficacies. The cancer dynamics model system (1) without treatment [1] can be obtained by setting ε₁(t) = 1 and ε₂(t) = 0. All the parameter

<!-- PAGE BREAK -->

<a id='21a0cc1e-764d-4d8d-ae7b-e82543ef33b7'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375-388

<a id='8d666224-698c-4594-93d9-3e73e9fb24d6'></a>

377

<a id='860caa44-7f10-43ee-8fb6-ee77225d20bb'></a>

values are assumed to be positive and the Eq. (1) ensure positive solutions for the state equations E(t) and T(t) [4]. The first equation depicting the rate of change of effector cell population at any time t. The first term of RHS represents the strength of treatment, s and e₁(t) is the control which regarded as an external source of immune-effector cells. The second term is the recruitment of tumor-specific effector cells which follow the Michaelis-Menten factor to specify the saturated effect of immune response, whereby the effector cells are recruited by tumor cells. At the same time, the effector cells are being eliminated by tumor cells which follow the law of mass action at a proportional rate m. The final term of the first equation represents the natural death of effector cells at a rate d. Our second equation designates the rate of change of tumor population which exhibit logistic growth where a is the intrinsic growth rate and 1/b is the biotic capacity. The second term represents the degradation of tumor cells due to interaction with tumor-specific effector cells at a rate n which follow the law of mass action. The final term designates tumor cells killed by an external injection of Adoptive Cellular Immunotherapy (ACI) €2 = €2(t). The ACI refers to the injection of cultured immune cells which have an anti-tumor activity into tumor bearing host. The external injection of ACI is depicted by the control function €2(t) which slows the cancer production and directly tumor cells in the tumor site.

<a id='9697037e-9740-4442-9a20-d1b13d1b4484'></a>

### 3. The control problem
This section is dedicated to the study of our model system (1), when we administered a treatment policy over a fixed time window. For that we design an objective functional by considering the biomedical goal in our mind. The aim is to study the consequences of the controlled treatment (ACI ($ε_2(t)$)) and IL-2 therapy ($ε_1(t)$))) on the dynamics of the mathematical model. Therefore, the objective functional (which is to be maximized) is defined as:

<a id='2dbbe8bd-9286-4bbe-a1db-eb50da485bd4'></a>

J(ε₁, ε₂) = ∫₀ᵗᶠ [E(t) - T(t) - ½(B₁ε₁²(t) + B₂ε₂²(t))]dt.

<a id='b592b623-f123-4a51-9726-16530cd594ab'></a>

Here, we maximize the advantage based on the amount of immune-effector cells (ECs) and minimize the tumor cell burden and the systemic cost of the control or deleterious effects of the therapy. The constants B_1 and B_2 represent the cost of drugs which are known as the weight factors on control and they include a measure of toxicity of the drugs of our body. B_1, B_2 also play a pivotal role of balancing the size of the terms and ε_1^2, ε_2^2 demonstrates the severity of the side effects of therapy. When drugs such as ACI and IL-2 are administered, they exhibit high toxicity for our body, which is the rationale behind the quadratic terms in the objective functional against linear control. Also, we need a finite time horizon t_f, since the treatment period is finite. Now our motto is to acquire an optimal control pair (ε_1^*, ε_2^*) as

J(ε_1^*, ε_2^*) = max{J(ε_1, ε_2) : ε_i ∈ S, for i = 1, 2}

<a id='869dd538-8b19-46d0-a3c3-bc04321e8c3b'></a>

where $S$ is the admissible control class defined on $[0, t_f]$, with initial conditions $0 \leq a_i \leq \epsilon_i(t) \leq b_i \leq 1$ i.e.
$S = \{(\epsilon_1, \epsilon_2): \epsilon_i \text{ is Lebesgue-measurable, } a_i \leq \epsilon_i \leq b_i, t \in [0, t_f], \text{ for } i = 1, 2\}.

<a id='cd22b6e8-5baf-4021-8797-155a930d9b8b'></a>

4. The necessary and sufficient condition of optimal control
In this section, we will study the sufficient condition for the existence of an optimal control pair of our problem from classical results [2,5,6]. After that, we utilize the calculus of variation to attain the optimal control system. At the same time, by using classical Pontryagin's Maximum Principle [6,7], we derive necessary conditions for our control problem.

<a id='e955235f-9973-4e04-b55b-2d50ecce24aa'></a>

4.1. The existence of optimal control

In this subsection, we will discuss the existence of an optimal control of our system of ODEs (1). To establish the existence of an optimal control and the proof of the uniqueness of the optimality system we need to prove the solutions of the system (1) are bounded for a finite time horizon. Now we will establish the existence of optimal control using the result developed by Fleming and Rishel [5], (Corollary 4.1, page 68–69).
This can be calculated by using the property of upper bounds (super-solutions) E, T of

$\frac{dE}{dt} = s + p\overline{E}$,

$\frac{d\overline{T}}{dt} = a\overline{T}$, (2)

<a id='14bf3d19-8b2e-41b6-9c60-9f1c24163746'></a>

are bounded on a finite time horizon. We can write in the vector form:

$$ 
\begin{pmatrix} E \\ T \end{pmatrix}' = \begin{pmatrix} p & 0 \\ 0 & a \end{pmatrix} \begin{pmatrix} E \\ T \end{pmatrix} + \begin{pmatrix} s \\ 0 \end{pmatrix} 
$$

<a id='252bc1d2-e11b-4539-8db7-1fba9c60c93e'></a>

Since this is a linear system with bounded coefficients and the time interval is finite, then we conclude that the super-solutions
$\bar{E}$ and $\bar{T}$ are uniformly bounded. Using the boundedness of the solutions to each state variables, we are now in position to proof
the existence of optimal control:

<!-- PAGE BREAK -->

<a id='e6a3b06f-b779-4c94-9e51-3eff893766a5'></a>

378

<a id='c7b9a1aa-c212-41be-bbab-cdea9d1f3ba8'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375–388

<a id='ffb447a1-e310-4b5f-b0e7-9e786011f235'></a>

## Theorem 1. Given the objective functional

$J(\epsilon_1, \epsilon_2) = \int_0^{t_f} \left[ E(t) - T(t) - \frac{1}{2} (B_1 \epsilon_1^2(t) + B_2 \epsilon_2^2(t)) \right] dt,$

<a id='ad9dc5ab-c2af-48dd-9a92-5c7871fde3b7'></a>

where the admissible control class:

<a id='6f5f91eb-726a-4d6e-840e-d549cb0dd8c9'></a>

S = {(\epsilon_1, \epsilon_2): \epsilon_i is piecewise continuous, a_i \le \epsilon_i \le b_i, t \in [0, t_f], for i = 1, 2},

<a id='e579effd-9c23-4eb0-8bd9-72ec8e7ea4ec'></a>

subject to the state system (1) with initial conditions E(0) = E₀, T(0) = T₀, then ∃ an optimal control pair \epsilon^* = (\epsilon_1^*(t), \epsilon_2^*(t)) which maximizes the functional J (\epsilon_1, \epsilon_2), that is

<a id='00cfc8d2-1d21-4da1-b3b2-25e643480436'></a>

max J(ε_1, ε_2) = J(ε_1^*, ε_2^*),
ε_i ∈ S, i=1:2

<a id='04d380ec-9965-4a2c-a5e3-33a97a399a60'></a>

provided that the conditions must be satisfied:

1. The admissible control class and the corresponding state equations with initial conditions are non-empty.
2. The admissible control class S is convex and bounded.
3. The right hand side (RHS) of the state equations is continuous and bounded above by a linear function in the state variables and control.
4. The integrand of cost functional J (€1, €2) is convex on S and bounded above.
5. There exists positive constants d1, d2 > 0 and y > 1 satisfying the integrand J (€1, €2) of the cost functional such that,

<a id='2421c1d4-1ab7-4bd6-8ad1-28608714a16e'></a>

$$J(\epsilon_1, \epsilon_2) \le d_2 - d_1 (|\epsilon_1|^2 + |\epsilon_2|^2)^{\gamma/2}.$$

<a id='a8855d1f-6902-4264-8876-2bad1968cff3'></a>

Proof.

1.  Since, the system (1) has bounded coefficients and the solutions are bounded on a finite time window, we can utilize the result developed by Lukes [9] (Theorem 9.2.1, page 182) to find the existence of the solution of the state Eq. (1).
2.  By the definition of control set S leads to the control set is closed and bounded.
3.  For the third condition, the RHS of the state Eq. (1) must be continuous. It may happen only the RHS of $\frac{dE}{dt}$ has a chance of being discontinuous of the term $\frac{pET}{g+T}$. Since both g and T are positive so $g + T$ is also positive, this eliminates the possibility of $\frac{pET}{g+T}$ being undefined. So, the complete system of the equation is continuous. Of note, the system (1) is bilinear in control and can be written in the vector form:

    $\vec{h}(t, \vec{Y}, \vec{\epsilon}) = \vec{\beta}(t, \vec{Y}) + \vec{\epsilon}s,$

    where $\vec{Y} = [E(t), T(t)]^T$, $\vec{\epsilon} = [\epsilon_1(t), \epsilon_2(t)]^T$ and $\vec{\beta}$ is a constant vector valued function of $\vec{Y}$.
    Using the boundedness of the solutions, we can write that

    $|\vec{h}(t, \vec{Y}, \vec{\epsilon})| \leq \begin{vmatrix} p & 0 \\ 0 & a \end{vmatrix} \begin{vmatrix} \vec{E} \\ \vec{T} \end{vmatrix} + \begin{vmatrix} \epsilon_1s \\ 0 \end{vmatrix} \leq A_1|\vec{Y}| + |\epsilon_1s|,$ 

    where $A_1$ depends on the coefficients of the system.
4.  In order to show the concavity (for the case of maximization) of the integrand in the objective functional $\mathcal{N}(t, \mathbf{Y}, \mathbf{u})$ we have to prove that,

    $(1-q)\mathcal{N}(t, \mathbf{Y}, \mathbf{u}) + q\mathcal{N}(t, \mathbf{Y}, \mathbf{v}) \leq \mathcal{N}(t, \mathbf{Y}, (1-q)\mathbf{u} + q\mathbf{v}),$

    where, $\mathcal{N}(t, \mathbf{Y}, \mathbf{u}) = E - T - \frac{1}{2}(B_1u_1^2 + B_2u_2^2) = E - T - \frac{1}{2}\sum_{i=1}^2 B_iu_i^2$; $\mathbf{u}, \mathbf{v}$ are two control vectors and $q \in (0, 1)$. Now,

    $(1-q)\mathcal{N}(t, \mathbf{Y}, \mathbf{u}) + q\mathcal{N}(t, \mathbf{Y}, \mathbf{v})$

    $= E - T - \frac{1}{2}(B_1u_1^2 + B_2u_2^2) + \frac{q}{2}(B_1u_1^2 + B_2u_2^2) - \frac{1}{2}(B_1v_1^2 + B_2v_2^2)$

    $= E - T - \frac{1}{2}(1-q)\sum_{i=1}^2 B_iu_i^2 - \frac{q}{2}\sum_{i=1}^2 B_iv_i^2,$

    and

    $\mathcal{N}(t, \mathbf{Y}, (1-q)\mathbf{u} + q\mathbf{v})$

    $= E - T - \frac{1}{2}(B_1u_1^2 + B_2u_2^2) - \frac{1}{2}B_1\{ (q^2 - 2q)u_1^2 + q^2v_1^2 + 2q(1-q)u_1v_1 \}$

    $- \frac{1}{2}B_2\{ (q^2 - 2q)u_2^2 + q^2v_2^2 + 2q(1-q)u_2v_2 \}$.

<!-- PAGE BREAK -->

<a id='d4115e9f-106e-41ad-8c9c-4d1090d19c69'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375–388

<a id='643b1e87-efe7-4242-a182-b58e4b7126cc'></a>

379

<a id='dc830c93-02e7-43e5-976a-8f54dec40d5a'></a>

Finally,

$[(1-q)N(t, Y, u) + qN(t, Y, v)] - [N(t, Y, (1 - q)u + qv)]$

$= -\frac{1}{2}B_1 [\sqrt{q(1-q)}u_1 - \sqrt{q(1-q)}v_1]^2 - \frac{1}{2}B_2 [\sqrt{q(1-q)}u_2 - \sqrt{q(1-q)}v_2]^2 < 0$

$= -\sum_{i=1}^2 \frac{B_i}{2} [\sqrt{q(1-q)}u_i - \sqrt{q(1-q)}v_i]^2 < 0.$

<a id='eccc8c2e-13a5-4bfb-b488-bc1f54e239a5'></a>

Hence, $\mathcal{N}(t, \mathbf{Y}, \mathbf{u})$ is concave.
5. Finally, $E(t) - T(t) - \frac{1}{2}(B_1\epsilon_1^2 + B_2\epsilon_2^2) \le E(t) - \frac{1}{2}(B_1\epsilon_1^2 + B_2\epsilon_2^2) \le d_2 - d_1 (\vert\epsilon_1\vert^2 + \vert\epsilon_2\vert^2)$ where $d_2$ depends on the upper bound on $E(t)$ and $d_1 = \min\{B_1, B_2\}$.
Hence, we conclude that there exists an optimal control pair $\vec{\epsilon}^* = (\epsilon_1^*, \epsilon_2^*)$ such that $\mathcal{J}(\epsilon_1, \epsilon_2)$ is maximized. \square

<a id='9d2d4d52-47bc-4361-b77e-3dd35f27acf4'></a>

4.2. *Characterization of optimal control*

In the previous section, we established the existence of an optimal control pair for maximization problem, now we derive the necessary conditions for optimal control by using Pontryagin's Maximum Principle [7]. In order to characterize the optimal control pair ($\epsilon_1^*$, $\epsilon_2^*$) we prove the following theorem.

<a id='261de338-a0ca-4b1d-b444-edd428e6a0b0'></a>

Theorem 2. Given an optimal control pair $(\epsilon_1^*, \epsilon_2^*)$ with corresponding state variables $E^*(t)$, $T^*(t)$ then there exist co-states or adjoint variables $\eta_1, \eta_2$ satisfying the following system:

$\eta_1' = -\left[1 + \eta_1\left\{\frac{pT}{g+T} - mT - d\right\} - \eta_2nT\right].$

$\eta_2' = -\left[-1 + \eta_1\left\{\frac{gpE}{(g+T)^2} - mE\right\} + \eta_2(a(1 - 2bT) - nE - \epsilon_2)\right] \quad (3)$

<a id='9160a809-aefc-4c90-ae3c-4dc6a7d26cd7'></a>

with n₁(tf) = 0, i = 1, 2 are the terminal conditions or transversality conditions. Moreover, the control pair (∈₁, ∈₂) is represented by,

<a id='46696fa3-f3fa-4fa3-8741-f4c98f17aec7'></a>

$$\epsilon_1^*(t) = \min \left\{ \max \left\{ a_1, \frac{1}{B_1} \eta_1 s \right\}, b_1 \right\},$$ $$\epsilon_2^*(t) = \min \left\{ \max \left\{ a_2, - \frac{1}{B_2} T^*(t) \eta_2 \right\}, b_2 \right\}.$$

<a id='e0191f22-4b7d-4c48-a908-485c7ec223b1'></a>

**Proof.** For the objective functional, the Hamiltonian is given by,

<a id='15068329-e75c-4f4e-b854-254fc9fcdc1d'></a>

H(E, T, ε₁, ε₂, η₁, η₂) = [E(t) - T(t) - ½(B₁ε₁²(t) + B₂ε₂²(t))] + η₁[sε₁(t) + pE(t)T(t) / (g + T(t)) - mE(t)T(t) - dE(t)] + η₂[aT(t)(1 - bT(t)) - nE(t)T(t) - ε₂(t)T(t)].

<a id='5dda3485-f6e7-4edc-b220-ceff61a8beff'></a>

Since, our control is bounded, we defined the Lagrangian as follows:

$\mathcal{L} = \mathcal{H} + m_{11}(t)(b_1 - \epsilon_1) + m_{12}(t)(\epsilon_1 - a_1) + m_{21}(t)(b_2 - \epsilon_2) + m_{22}(t)(\epsilon_2 - a_2)$,

<a id='43b045bf-55a3-4b1c-92f5-ee4ba2db51a7'></a>

where $m_{11}(t)$, $m_{12}(t)$, $m_{21}(t)$, $m_{22}(t) \geq 0$ are the Lagrangian multipliers satisfying the conditions:
$m_{11}(t)(b_1 - \epsilon_1) = 0$, $m_{12}(t)(\epsilon_1 - a_1) = 0$ at $\epsilon_1^*$

<a id='dd7373df-0253-473b-9a9a-87d850224a48'></a>

and

m₂₁(t)(b₂ − ε₂) = 0, m₂₂(t)(ε₂ − a₂) = 0 at ε₂*.

<a id='28968133-a135-4f82-b55b-69baf0d69e13'></a>

In order to form the co-states and transversality conditions we use the classical results in optimal control theory [10]. We differentiate the Lagrangian $\mathcal{L}$, with respect to the state variables $E$ and $T$ respectively and then the co-states or adjoint system can be expressed as:
$\dot{\eta_1} = -\frac{\partial \mathcal{L}}{\partial E}$, $\dot{\eta_2} = -\frac{\partial \mathcal{L}}{\partial T}$.

<a id='44cd8d34-7a5d-4907-957d-32b657a9bc72'></a>

To characterize the optimal control ε*1, ε*2 we take the variation with respect to controls (ε1, ε2) and set it equal to zero. Then, we obtain

∂L/∂ε1 = -B1ε1(t) + η1s - m11(t) + m12(t) = 0 at ε*1,

∂L/∂ε2 = -B2ε2(t) - η2T*(t) - m21(t) + m22(t) = 0 at ε*2,

<!-- PAGE BREAK -->

<a id='bb13b457-85ab-45a4-9e74-89a7167b7a73'></a>

380

<a id='206a0f40-4f89-4727-bdc7-55b0ebac8230'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375-388

<a id='d05d6969-8858-4cd8-9fb3-66f8ee4da327'></a>

Solving for optimal control pair, we get

$$\epsilon_1^*(t) = \frac{1}{B_1}[\eta_1(t)s - m_{11}(t) + m_{12}(t)],$$

$$\epsilon_2^*(t) = \frac{1}{B_2}[-\eta_2(t)T^*(t) - m_{21}(t) + m_{22}(t)].$$

<a id='fe76087d-ffb0-4b6b-80bc-519fd166c3b3'></a>

By classical control arguments and using the bounds on the controls, we have

$$\epsilon_1^* = \begin{cases}
\frac{\eta_1 S}{B_1} & \text{if } a_1 < \frac{1}{B_1}\eta_1 S < b_1; \\
a_1 & \text{if } \frac{1}{B_1}\eta_1 S \le a_1; \\
b_1 & \text{if } \frac{1}{B_1}\eta_1 S \ge b_1.
\end{cases}$$

<a id='18357459-d01a-43e7-b834-787b64f68a14'></a>

In similar way,

$\epsilon_2^* = \begin{cases}
-\frac{\eta_2 T^*(t)}{B_2} & \text{if } a_2 < -\frac{1}{B_2}\eta_2 T^*(t) < b_2; \\
a_2 & \text{if } -\frac{1}{B_2}\eta_2 T^*(t) \leq a_2; \\
b_2 & \text{if } -\frac{1}{B_2}\eta_2 T^*(t) \geq b_2.
\end{cases}$

<a id='28f2c540-8418-432d-8b73-e5510b8700c1'></a>

Of note, the optimality system encompasses of the coupled of state variables, co-states or adjoint variables, with their initial conditions and transversality conditions, along with the characterization of the control pair,

<a id='b668ec26-9094-4de4-ba55-999934dec533'></a>

$\varepsilon_1^*(t) = \min \left\{ \max \left\{ a_1, \frac{1}{B_1}\eta_1 s \right\}, b_1 \right\}$
(4)

$\varepsilon_2^*(t) = \min \left\{ \max \left\{ a_2, -\frac{1}{B_1}\eta_2 T^*(t) \right\}, b_2 \right\}$
(5)

<a id='80974327-5051-46a5-8df0-c9664f47268a'></a>

By using the above optimal control pair, we obtain the subsequent optimality system:

$\frac{dE(t)}{dt} = \min \left\{ \max \left\{ a_1, \frac{1}{B_1}\eta_1 s \right\}, b_1 \right\} + \frac{pE(t)T(t)}{g+T(t)} - mT(t)E(t) - dE(t),$

$\frac{dT(t)}{dt} = aT(t)(1 - bT(t)) - nE(t)T(t) - \min \left\{ \max \left\{ a_2, -\frac{1}{B_1}\eta_2 T(t) \right\}, b_2 \right\} T(t),$

$\eta'_1 = -1 - \eta_1 \left[ \frac{pT(t)}{g+T(t)} - mT(t) - d \right] + \eta_2 nT(t),$

$\eta'_2 = 1 - \eta_1 \left[ \frac{gpE(t)}{(g+T(t))^2} - mE(t) \right] - \eta_2 (a(1 - 2bT(t)) - nE(t)) + \eta_2 \min \left\{ \max \left\{ a_2, -\frac{1}{B_1}\eta_2 T(t) \right\}, b_2 \right\}. (6)$

<a id='8572bbca-024e-4461-a93b-03c734c3dd3c'></a>

with η1(tf) = η2(tf) = 0 and E(0) = E0, T(0) = T0. Of note, the second variation of the Lagrangian with reference to the control pair (ε1, ε2) is negative, designating a maximum of both the controls. □

<a id='04c0b5b6-8578-4041-b3f9-ae6a9eccf950'></a>

5. Uniqueness of optimal control

By using the boundedness for the state system, the co-states has bounded coefficients which is linear in each of the adjoint variables. Therefore, solutions of the co-states are bounded. Now, we are in position to proof the uniqueness of the optimality system. We will use the proposition (without proof) which is indispensable for the proof of the uniqueness of the optimality system for the smaller time window.

<a id='586316d1-c533-45a5-bf9d-9ab545ddc384'></a>

Proposition 5.1. The function \u20ac*(m) = min{max{m, a}, b} which is Lipschitz continuous in m, with a < b for some fixed nonnegative constants.

<a id='5a1cea2f-fa5e-4c31-a2c9-d68a22975235'></a>

**Theorem 3.** *The bounded solutions of the optimality system is unique, for sufficiently small time horizon t₃.*

<a id='c60a1834-dcc4-4180-94be-8888f6b7e202'></a>

**Proof.** Let us assume that (E, T, η₁, η₂) and (Ē, Ī, ħ₁, ħ₂) are two non-identical solutions to the optimal system (6). Suppose,
E = eⁿᵗh, T = eⁿᵗq, η₁ = e⁻ⁿᵗu, η₂ = e⁻ⁿᵗv and Ē = eⁿᵗħ, Ī = eⁿᵗǣ, ħ₁ = e⁻ⁿᵗū, ħ₂ = e⁻ⁿᵗŵ, with positive η i.e. η > 0. Moreover,
we assume that,

<!-- PAGE BREAK -->

<a id='a652706e-9f31-4043-8a69-5be8ea83815a'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375–388

<a id='16794e76-bc12-414b-b382-4bbd98e48719'></a>

381

<a id='f7b84273-3533-4f3a-b2b1-ebc0dfd953aa'></a>

$\epsilon_1^*(t) = \min \left\{ \max \left\{ a_1, \frac{e^{-\eta t} us}{B_1} \right\}, b_1 \right\},$

$\epsilon_2^*(t) = \min \left\{ \max \left\{ a_2, \frac{-vq}{B_2} \right\}, b_2 \right\},$ 

<a id='f100aa54-a451-4f5b-b9d5-a3bc74683c28'></a>

and

$\bar{\epsilon}_1^*(t) = \min \left\{ \max \left\{ a_1, \frac{e^{-\eta t \bar{u}s}}{B_1} \right\}, b_1 \right\}$

$\bar{\epsilon}_2^*(t) = \min \left\{ \max \left\{ a_2, -\frac{\bar{v}q}{B_2} \right\}, b_2 \right\}$

<a id='7ea7408b-3775-4cc5-ac21-a9bdd12e7dd4'></a>

Substituting E = e^ηt h into the first ODE of (6) we have,h' + ηh = min { max { a₁, (e^(-ηt)us) / B₁ }, b₁ }.se^(-ηt) + (phqe^(ηt)) / (g + qe^(ηt)) - mhqe^(ηt) - dh.

<a id='39a96086-9949-4904-8e87-ebf03cfcf816'></a>

In a similar way, by putting $T = e^{nt}q$, $\eta_1 = e^{-nt}u$, $\eta_2 = e^{-nt}v$, we have,

$q' + \eta q = aq(1 - be^{nt}q) - nhqe^{nt} - \min \left\{ \max \left\{ a_2, -\frac{vq}{B_2} \right\}, b_2 \right\}q$,

$-u' + \eta u = e^{nt} + u\left[ \frac{pqe^{nt}}{g + e^{nt}q} - mqe^{nt} - d \right] - nvqe^{nt}$,

$-v' + \eta v = -e^{nt} + u\left[ \frac{gph e^{nt}}{(g + e^{nt}q)^2} - mhe^{nt} \right] + v[a(1 - 2be^{nt}q) - nhe^{nt}] - \min \left\{ \max \left\{ a_2, -\frac{vq}{B_2} \right\}, b_2 \right\}v.$

<a id='d216d41e-6d96-4fa7-89c6-be293feaa7c0'></a>

Using the Proposition (5.1), we can write that

$$|\epsilon_1^*(t) - \bar{\epsilon}_1^*(t)| \le \frac{1}{B_1}|e^{\eta t}s(u - \bar{u})|$$

$$|\epsilon_2^*(t) - \bar{\epsilon}_2^*(t)| \le \frac{1}{B_2}|v q - \bar{v}\bar{q}|$$

<a id='c4816aaa-5e3d-4129-9b47-c0f0ae1d5d6d'></a>

Now, we subtract the equations for the state variables $E$ and $\bar{E}$, $T$ and $\bar{T}$, as well as the co-states $\eta_1$ and $\bar{\eta}_1$, $\eta_2$ and $\bar{\eta}_2$. Then, each of the resulting equation is multiplied by an appropriate difference of functions and integrate from 0 to $t_f$. After that, we will add the four equations and estimates them to get the results are employed.
Some of the integral equations are listed below for example:

<a id='99b98e22-44af-4e24-96cd-ce0c8c661fde'></a>

$\frac{1}{2}[h(t_f) - \bar{h}(t_f)]^2 + (\eta + d)\int_0^{t_f} (h - \bar{h})^2 dt$

$= \int_0^{t_f} se^{-\eta t}(\epsilon_1(t) - \bar{\epsilon}_1(t))(h - \bar{h})dt - \int_0^{t_f} me^{\eta t}(hq - \bar{h}\bar{q})(h - \bar{h})dt + \int_0^{t_f} pe^{\eta t}\left(\frac{hq}{g + e^{\eta t}q} - \frac{\bar{h}\bar{q}}{g + e^{\eta t}\bar{q}}\right)(h - \bar{h})dt.$

<a id='106c1e3b-40f9-4344-94b5-b0e7c1a7f249'></a>

Now, our interest is to obtain the bounds on the right hand side of the above integration terms. Since $q, \bar{q} \ge 0$, we can estimate the denominator of the fractional part as follows:

<a id='7bcd827c-0efd-44ed-ad3c-3259966677b2'></a>

g + e^ηt q ≥ g, g + e^ηt q̄ ≥ g.

<a id='5df75f81-8172-4b1e-9682-5e73400b0dc4'></a>

Therefore, the above integral equation takes the form as:

<a id='75182a94-3521-4895-a66c-37afa87ea051'></a>

$$\frac{1}{2}[h(t_f) - \bar{h}(t_f)]^2 + (\eta + d) \int_0^{t_f} (h - \bar{h})^2 dt \\ \le \bar{C} \int_0^{t_f} (u - \bar{u})(h - \bar{h})dt + \frac{pe^{\eta t_f}}{g} \int_0^{t_f} (hq - \bar{h}\bar{q})(h - \bar{h})dt \\ + \frac{pe^{2\eta t_f}}{g^2} \int_0^{t_f} \bar{q}q(h - \bar{h})^2 dt + me^{\eta t_f} \int_0^{t_f} (hq - \bar{h}\bar{q})(h - \bar{h})dt. \quad (7)$$

<a id='2434d62f-245f-4b21-9f7d-f5f605393a53'></a>

Now, we want to analyze the term $\int_{0}^{t_f} (hq - \overline{hq})(h - \overline{h})dt$ to obtain the specific estimate, we employ the Cauchy - Schwarz inequality to disjoint the linear product forms into quadratic terms. Then, we can write

<a id='5368bca1-faea-49c2-b7a1-8a896b712904'></a>

$$\int_{0}^{t_f} (hq - \bar{h}\bar{q})(h - \bar{h})dt \leq \int_{0}^{t_f} q(h - \bar{h})^2dt + \int_{0}^{t_f} \bar{h}(q - \bar{q})(h - \bar{h})dt$$ $$\leq \frac{2A_2 + A_1}{2} \int_{0}^{t_f} (h - \bar{h})^2dt + \frac{A_1}{2} \int_{0}^{t_f} (q - \bar{q})^2dt,$$

<!-- PAGE BREAK -->

<a id='d00a76b5-bc30-4b8c-95e5-b484541d2543'></a>

382

<a id='da0611a5-8c9d-4f62-a71d-7e7260c1c682'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375–388

<a id='8311efe9-80da-4469-b273-d9663c3fd24f'></a>

where A₁, A₂ are the upper bounds of $\bar{h}$, $\bar{q}$ respectively. Now, we can write the Eq. (7) as,

$$\frac{1}{2}[h(t_f) - \bar{h}(t_f)]^2 + (\eta + d) \int_0^{t_f} (h - \bar{h})^2 dt$$

$$\leq \tilde{C}_1 \int_0^{t_f} (u - \bar{u})^2 + (h - \bar{h})^2 dt + C_{11}e^{\eta t_f} \int_0^{t_f} ((h - \bar{h})^2 + (q - \bar{q})^2)dt + C_{12}e^{2\eta t_f} \int_0^{t_f} ((h - \bar{h})^2 + (q - \bar{q})^2)dt.$$

<a id='a2686a3e-2031-42d5-8e7e-b20662186819'></a>

The constants C̃₁, C₁₁ and C₁₂ depends on the bounds of the state variables and co-states.
Also it can be noticed that,

<a id='0e1de87e-da2a-4171-bf60-3b59057e49c9'></a>

\frac{1}{2}[\nu(0) - \bar{\nu}(0)]^2 + (\eta - \alpha) \int_0^{t_f} (v - \bar{v})^2 dt\n\n\leq gp \int_0^{t_f} e^{\eta t} (v - \bar{v}) \left[\frac{g^2 (uh - \bar{u}\bar{h})}{(g+qe^{\eta t})^2 (g+\bar{q}e^{\eta t})^2}\right] dt + 2g^2 p \int_0^{t_f} e^{\eta t} (v - \bar{v}) \left[\frac{e^{\eta t} (\bar{q}uh - \bar{u}hq)}{(g+qe^{\eta t})^2 (g+\bar{q}e^{\eta t})^2}\right] dt\n\n+gp \int_0^{t_f} e^{\eta t} (v - \bar{v}) \left[\frac{e^{2\eta t} (q^2uh - \bar{q}^2\bar{u}\bar{h})}{(g+qe^{\eta t})^2 (g+\bar{q}e^{\eta t})^2}\right] dt + m \int_0^{t_f} e^{\eta t} (uh - \bar{u}\bar{h}) (v - \bar{v})dt\n\n+2b \int_0^{t_f} e^{\eta t} (vq - \bar{v}\bar{q}) (v - \bar{v})dt + n \int_0^{t_f} e^{\eta t} (vh - \bar{v}\bar{h}) (v - \bar{v})dt + \int_0^{t_f} (v\epsilon_2 - \bar{v}\bar{\epsilon}_2) (v - \bar{v})dt.

<a id='09b68fb8-f32c-4c35-b91d-4d4367d98763'></a>

To find the bounds on RHS of the integrals, we estimate the denominator as $(g+qe^{nt})^2 \ge g^2$; $(g+\bar{q}e^{nt})^2 \ge g^2$ as $q, \bar{q} \ge 0$. Then we can write that,

<a id='04564519-a381-404b-953e-1401884b327e'></a>

1/2 [v(0) - v_bar(0)]^2 + (η - α) ∫_0^(t_f) (v - v_bar)^2 dt
≤ (pe^(ηt_f) / g) ∫_0^(t_f) (uh - u_bar h)(v - v_bar)dt + (2pe^(2ηt_f) / g^2) ∫_0^(t_f) (q_bar uh - u_bar hq)(v - v_bar)dt
+ (pe^(3ηt_f) / g^3) ∫_0^(t_f) (q^2 uh - q^2 u_bar h)(v - v_bar)dt + me^(ηt_f) ∫_0^(t_f) (uh - u_bar h)(v - v_bar)dt
+ 2be^(ηt_f) ∫_0^(t_f) (vq - v_bar q)(v - v_bar)dt + ne^(ηt_f) ∫_0^(t_f) (vh - v_bar h)(v - v_bar)dt + ∫_0^(t_f) (vε_2 - v_bar ε_2)(v - v_bar)dt.

<a id='e2b10893-a6ec-4e3a-a02d-5b4d21e7e80a'></a>

Now, we want to find the specific form of $\int_0^{t_f} (\bar{q}^2 uh - q^2 \bar{u}\bar{h})(v - \bar{v})dt$, by using Cauchy - Schwarz inequality:

$\int_0^{t_f} (\bar{q}^2 uh - q^2 \bar{u}\bar{h})(v - \bar{v})dt$

$\le \int_0^{t_f} \bar{q}^2 (v - \bar{v})(uh - \bar{u}\bar{h})dt + \int_0^{t_f} \bar{u}\bar{h}(v - \bar{v})(q^2 - \bar{q}^2)dt$

$\le A_2^2 \int_0^{t_f} (v - \bar{v})(uh - \bar{u}\bar{h})dt + 2A_1 A_2 A_4 \int_0^{t_f} (v - \bar{v})(q - \bar{q})dt$

$\le \frac{A_2^2 A_1}{2} \int_0^{t_f} (u - \bar{u})^2 dt + \frac{A_4 A_2^2}{2} \int_0^{t_f} (h - \bar{h})^2 dt + A_1 A_2 A_4 \int_0^{t_f} (q - \bar{q})^2 dt + \frac{A_1 A_2^2 + 2A_1 A_2 A_4 + A_2^2 A_4}{2} \int_0^{t_f} (v - \bar{v})^2 dt,$

<a id='14cf3900-101c-4f2f-a767-b49e30d2517e'></a>

where A1, A2, and A4 are the upper bounds of $\bar{h}$, $\bar{q}$, $\bar{u}$ respectively.
Now to prove the uniqueness of the optimality system, the integral representations of $(h - \bar{h})$, $(q - \bar{q})$, $(u - \bar{u})$ and $(v - \bar{v})$ are combined together, we have,

<a id='06ed5a75-f4ac-47b2-8e4b-65da912a1557'></a>

1/2[h(t_f) - h̄(t_f)]^2 + 1/2[q(t_f) - q̄(t_f)]^2 + 1/2[u(t_f) - ū(t_f)]^2 + 1/2[v(t_f) - v̄(t_f)]^2
+ (η+d) ∫_0^(t_f) (h-h̄)^2dt + (η-a) ∫_0^(t_f) (q-q̄)^2dt + (η+d) ∫_0^(t_f) (u-ū)^2dt + (η-a) ∫_0^(t_f) (v-v̄)^2dt
≤ C̄e^(3ηt_f) ∫_0^(t_f) [(h-h̄)^2 + (q-q̄)^2 + (u-ū)^2 + (v-v̄)^2]dt.

<a id='a94e20d3-ae31-4e9d-9575-99bda795eb81'></a>

Using the conditions for non-negativity of the variables and evaluated at the initial time and the final time and then simplifying,
the above inequality can be stated as:

<a id='0572d252-bc87-4549-bc1f-787b394b6093'></a>

$(\eta - B - \bar{C}e^{3nt_f}) \int_{0}^{t_f} [(h - \bar{h})^2 + (q - \bar{q})^2 + (u - \bar{u})^2 + (v - \bar{v})^2]dt \le 0,$

<a id='9c0a9760-ddad-4794-98d3-224f789a8aa1'></a>

where $\bar{B}$, $\bar{C}$ depends on the coefficients and bounds on all the solution variables.
We choose, $\eta$ in such a manner that $\eta > \bar{B} + \bar{C}$ and thus $\eta > \bar{B} + \bar{C}e^{3\eta t_f}$, then $h = \bar{h}$, $q = \bar{q}$, $u = \bar{u}$ and $v = \bar{v}$. Also, we are aware
that the natural logarithm is a non-decreasing function, then $\ln (\frac{\eta - \bar{B}}{\bar{C}}) > 3\eta t_f$. Which implies that, $t_f < \frac{1}{3\eta} \ln (\frac{\eta - \bar{B}}{\bar{C}})$. Based on the

<!-- PAGE BREAK -->

<a id='b792742a-71c6-4e61-b49c-f1f5326b2268'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375-388

<a id='08bd02c1-17b5-4967-85a2-ed4107b7acfb'></a>

383

<a id='716e5d13-5233-46ef-ba9a-deed2067fac9'></a>

Table 1
List parameter values used for model simulations.
<table id="8-1">
<tr><td id="8-2">Parameter</td><td id="8-3">Description</td><td id="8-4">Units</td><td id="8-5">Values</td></tr>
<tr><td id="8-6">s</td><td id="8-7">The constant source rate of effector cells</td><td id="8-8">cells day⁻¹</td><td id="8-9">1.3 × 10⁴</td></tr>
<tr><td id="8-a">p</td><td id="8-b">Maximum rate of effector cell proliferation</td><td id="8-c">day⁻¹</td><td id="8-d">0.1245</td></tr>
<tr><td id="8-e">g</td><td id="8-f">Half saturation constant</td><td id="8-g">cell</td><td id="8-h">2.019 × 10⁷</td></tr>
<tr><td id="8-i">m</td><td id="8-j">Effector cells inactivation rate by tumor cells</td><td id="8-k">cell⁻¹day⁻¹</td><td id="8-l">3.422 × 10⁻¹⁰</td></tr>
<tr><td id="8-m">d</td><td id="8-n">The natural death rate of effector cells</td><td id="8-o">day⁻¹</td><td id="8-p">0.0412</td></tr>
<tr><td id="8-q">a</td><td id="8-r">The maximal growth rate of tumor cells</td><td id="8-s">day⁻¹</td><td id="8-t">0.18</td></tr>
<tr><td id="8-u">b</td><td id="8-v">is the maximal carrying capacity</td><td id="8-w">cell⁻¹</td><td id="8-x">2.0 × 10⁻⁹</td></tr>
<tr><td id="8-y">n</td><td id="8-z">Inactivation of tumor cells due to effector cells</td><td id="8-A">cell⁻¹day⁻¹</td><td id="8-B">1.101 × 10⁻⁷</td></tr>
</table>

<a id='7ced0a60-1fac-46db-92f4-d016c000ad13'></a>

above analysis of the uniqueness of the optimal control system, the optimal control pair is unique. So, the control is characterized in terms of \eta2.

<a id='725683e8-0632-43d5-9934-b93415a845d1'></a>

From the mathematical background, the uniqueness of the solution of an optimality system holds for a small time window in such a highly nonlinear boundary value (two point) problems with reverse time orientations; where the initial conditions for state variables and terminal time conditions for adjoint variables. The optimal control pair will provide us an optimal treatment policy to the cancer patients. \u25a1

<a id='ac15d1e4-6e5e-4d7d-98a9-029a7750c8f9'></a>

## 6. Numerical simulations

Now we will study the numerical aspect of our optimal control problem to validate our analytical results in the foregoing sections. To illustrate our numerical simulations we have taken the set of parameter values from the article by Kuznetsov et al. [1] and also we put the data in Table 1. Of note, the optimality system is a boundary ('two point') value problem where we use the forward in time to solve the state Eq. (1) with initial conditions and backward in time to solve the co-state or adjoint system (3) with terminal or transversality conditions. Indeed, the state system moves forward with time and the co-states move backward with time and we coupled both situation in addition to controls which is a quite challenging problem. We solved the optimality system numerically by using an iterative process with the fourth order Runge–Kutta scheme. The algorithm for our problem as follows:

Step 1: We choose an initial guess for the control pair $\epsilon_1^*$, $\epsilon_2^*$.

Step 2: We solved the state system (1) by using a forward sweep loop with initial conditions using an initial guess of the control pair.

Step 3: After obtaining the solution for the state system, we use backward loop to solve the co-states or adjoints system using transversality or terminal conditions.

Step 4: We update the control pair $\epsilon_1^*$, $\epsilon_2^*$ in each iteration by using the values of the optimality system obtained in the previous iterations.

Step 5: The procedure is continued iteratively till the convergence is achieved.

<a id='eaa0a4e0-083d-47eb-bfec-e80f75118814'></a>

One could espouse an easier version of the multiple shooting method by Hackbusch [12] identifies as being one-shot, which were designed for partial differential equations (PDEs). We will however espouse a two-shot procedure, similar to the one developed by Chakrabarty and Hanson [11]. The algorithm for treatment strategy is simulated for 200 days. In order to obtain the entire procedure of what actually is occurring, we observe the following scenarios.

<a id='6e87795a-ed71-4ca1-8c14-cddf35a4891c'></a>

### First scenario: without treatment
At first, we look for the case where both of the treatment regimens are absent. May be this will provide us an intuition what would happen without treatment and from that we can obtain an idea about the designing of different optimal control policies. Fig. 1, depicts the dynamics where the no treatment administered. The effector cells goes up and down and achieve its steady state as one would presume for such a small time frame. Also the cancerous cell burden goes up and down, respectively and attains its equilibrium point. From that it is clear that, there is no such manifestation of the remission of cancer without any treatment strategy such as Adoptive Cellular Immunotherapy(ACI), Interleukin-2(IL-2) or any prescribed therapy.

<a id='77ebb435-aabc-4cb5-8069-b3823a548ebb'></a>

**Second scenario: role of interleukin-2 (IL-2)**
Now we will study the dynamics of our system when single external IL-2 was injected, but ACI was not administered. For the case of cancerous cells, a moderate attainment of the equilibrium point is observed. If we look carefully, then the size of tumor burden is decreased by administered of single IL-2 therapy ε₁ (the second figure of Fig. 2 compared to the second figure of Fig. 1, without treatment). Also the magnitude of effector cells is decreased (the first figure of the Fig. 2) due to side-effects of the drugs. It can also be noticed that, control ε₁ is deliberately depends on the first adjoint or co-state η₁. When the value of (η₁) is increased approximately zero to 50 days, the control variable ε₁ is also increased within zero to 50 days (approximately) and when the value of η₁ is decreased from 51 days to 100 days then the control variable ε₁ is also decreased from 50 days to 100 days (approximately) and so on.

<!-- PAGE BREAK -->

<a id='b6d978d2-1e20-4477-a582-f40b42921002'></a>

384

<a id='218b7e5e-091d-48f7-895c-2e15bc3b48b7'></a>

384 S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375–388<::chart: This figure contains two line graphs side-by-side. Both graphs share the same x-axis, labeled "Days", ranging from 0 to 200. The first graph (left) shows the number of "Effector cells" (y-axis labeled "Effector cells x 10⁶"). The curve starts at approximately 1.72 x 10⁶, decreases to a minimum of about 1.53 x 10⁶ around day 50, rises to a peak of about 1.67 x 10⁶ around day 100, then decreases to about 1.57 x 10⁶ around day 150, and finally rises to approximately 1.66 x 10⁶ by day 200, exhibiting an oscillatory pattern. The second graph (right) shows the number of "Tumor cells" (y-axis labeled "Tumor cells x 10⁷"). The curve starts at approximately 0.8 x 10⁷, increases to a peak of about 1.58 x 10⁷ around day 50, decreases to a minimum of about 0.87 x 10⁷ around day 100, then rises to about 1.48 x 10⁷ around day 150, and finally decreases to approximately 0.9 x 10⁷ by day 200, also showing an oscillatory pattern. Fig. 1. The figure shows the solution of the state system (1) without treatment strategies. The initial conditions used are E₀ = 1.70811 × 10⁶, T₀ = 8.28638 × 10⁶. Parameters for this simulations are described in the Table 1.::>

<a id='f103efe0-20d1-413e-afea-9b57ebf6a588'></a>

<::chart: The figure presents four subplots arranged in a 2x2 grid, all sharing a common x-axis labeled "Days" ranging from 0 to 200. The top-left subplot shows "Effector cells" (scaled by x 10^6) on the y-axis, with the curve oscillating between approximately 1.4 and 1.8. The top-right subplot shows "Tumor cells" (scaled by x 10^6) on the y-axis, with the curve oscillating between approximately 5.5 and 8.5. The bottom-left subplot shows "Optimal control ($\epsilon_1$)" on the y-axis, with the curve oscillating between 0 and approximately 0.4. The bottom-right subplot shows "Adjoint ($\eta_1$)" on the y-axis, with the curve oscillating between 0 and approximately 550. Fig. 2. The figure shows the solution of the objective functional $J(\epsilon_1)$ subject to the state system (1) when the single therapy IL-2 is administered. The initial conditions used are $E_0 = 1.60811 \times 10^6$, $T_0 = 8.28638 \times 10^6$. $B_1 = 10^7$. Parameters for this simulations are described in Table 1.::>

<a id='2fca5bb2-471b-4cfd-8b0e-f82c6d457a9a'></a>

**Third scenario: role of Adoptive Cellular Immunotherapy(ACI)**
Now we will observe the upshot for a singular drug ACI (IL-2 therapy is not administered). The administration of ACI shows a significant reduction of tumor cell burden as compared to without treatment case (see second figure of Fig. 1) also in the case of second scenario (when the single therapy IL-2 administered) (see second figure of Fig. 2). Due to external input of ACI in conjunction with effector cells, the tumor cells decreases sharply (see the second figure of the top panel of Fig. 3). It can also be observed that the effector cells decreases due to the toxicity of the drug. Next, we focused on the consequence of the optimal control ε₂ which solely depends on the adjoint variable η₂. When the adjoint variable η₂ is non-positive the optimal control variable ε₂ is sharply decreased (see the bottom panel of the Fig. 3).

<a id='c820f91d-59af-40d8-a230-227d6db00fbc'></a>

From the previous scenarios (first scenario, second scenario), we can say that, single therapy ACI can reduce the tumor burden significantly but IL-2 therapy can reduce the tumor burden slightly.

<a id='e630e739-d922-4619-b7ff-0bf9d0946096'></a>

Fourth scenario: Role of combined therapy
Figs. 4 and 5 depict the dynamics of optimal control treatment strategy, when both the therapies (ACI and IL-2) are administered. The tumor cells decrease sharply and flattens out as compared to singular therapy (ACI or IL-2). This is the consistent with our daydream that the combined effects of drugs reduce the tumor cells burden remarkably. The application of combined therapy is showing 'tumor dormancy' situation(see the second figure of the top panel of Fig. 4). The bottom panel of Fig. 4 indicates the cost of the optimal control effectiveness for the combined therapy. Also, the bottom panel of Fig. 4 reflects the decline the level of dosages during the treatment period. Fig. 5 designates both the co-state or adjoint variables η₁ and n₂, respectively. The

<!-- PAGE BREAK -->

<a id='29f219fa-b24f-4b6b-a463-22ee86499b5d'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375-388

<a id='183be76c-c94e-4d77-a7f2-88b8e4b10d24'></a>

385

<a id='fbac1521-cf8c-4d53-9c04-b7a2931a6ffd'></a>

<::A figure composed of four line charts arranged in a 2x2 grid. The x-axis for all charts is 'Days', ranging from 0 to 200.::>

<::chart: The top-left chart, titled "Effector cells", shows a line decreasing from approximately 1.6 x 10^6 at 0 days to around 0.3 x 10^6 at 200 days. The y-axis ranges from 0 to 2 x 10^6.::>

<::chart: The top-right chart, titled "Tumor cells", shows a line decreasing from approximately 8.5 x 10^6 at 0 days to nearly 0 at 200 days. The y-axis ranges from 0 to 10 x 10^6.::>

<::chart: The bottom-left chart, titled "Optimal control(ε₂)", shows a line starting at 0.6, sharply decreasing to near 0.1 around 50 days, and remaining at 0.1 until 200 days. The y-axis ranges from 0.1 to 0.6.::>

<::chart: The bottom-right chart, titled "Adjoint (η₂)", shows a line starting near 0, decreasing to approximately -13 around 100 days, and then increasing sharply to 5 at 200 days. The y-axis ranges from -15 to 5.::>

**Fig. 3.** The figure shows the solution of the objective functional $\mathcal{J}(\epsilon_2)$ subject to the state system (1) when the single drug ACI is administered. The initial conditions used are $E_0 = 1.60811 \times 10^6$, $T_0 = 8.28638 \times 10^6$. $B_2 = 10^7$. Parameters for this simulation are described in Table 1.

<a id='5fe8ca5f-9e83-4b34-9fe5-3cafc089eb42'></a>

<::transcription of the content: chart::>Fig. 4. The figure shows the solution of the objective functional $\mathcal{J}(\varepsilon_1, \varepsilon_2)$ subject to the state system (1) when the combined drugs are administered. The initial conditions used are $E_0 = 1.60811 \times 10^6$, $T_0 = 8.28638 \times 10^6$. $B_1 = 10^7$, $B_2 = 10^7$. Parameters for this simulation are described in Table 1.

The figure consists of four line plots arranged in a 2x2 grid.

Top-left plot:
- Y-axis: "Effector cells" (scaled by $x 10^6$)
- X-axis: "Days"
- A blue line starts around 1.6 $x 10^6$ and decreases rapidly, then levels off near 0.

Top-right plot:
- Y-axis: "Tumor cells" (scaled by $x 10^6$)
- X-axis: "Days"
- A blue line starts around 8.5 $x 10^6$ and decreases rapidly, then levels off near 0.

Bottom-left plot:
- Y-axis: "Optimal control ($\varepsilon_1$)"
- X-axis: "Days"
- A blue line starts around 0.09, decreases to about 0.065, then slightly increases towards 0.07, and finally drops to about 0.055 at the end.

Bottom-right plot:
- Y-axis: "Optimal control ($\varepsilon_2$)"
- X-axis: "Days"
- A blue line starts around 0.55, stays constant for a short period, then decreases rapidly to about 0.1, and slowly decreases further towards 0.05.
<::>

<a id='3bb8efcf-ce1e-4480-8021-ca1191a8e94b'></a>

<::The figure consists of two line charts displayed side-by-side. The left chart shows 'Adjoint (η₁)' on the y-axis, ranging from 0 to 60, and 'Days' on the x-axis, ranging from 0 to 200. The blue line starts near 50 at Day 0, decreases sharply, then gradually declines, reaching close to 0 at Day 200. The right chart shows 'Adjoint (η₂)' on the y-axis, ranging from -40 to 0, and 'Days' on the x-axis, ranging from 0 to 200. The blue line starts near -5 at Day 0, decreases to a minimum around -35 at approximately Day 100, and then increases, reaching close to 0 at Day 200. Fig. 5. The figure shows the solution of the adjoint system (3) when the combined drugs are administered. The initial conditions and parameters are same in Fig. 4.: chart::>

<!-- PAGE BREAK -->

<a id='64811970-f6b3-4585-98c0-3e6e598f4f9c'></a>

386

<a id='cb87d9d4-70b0-49e5-99d5-716b2e649c76'></a>

386 S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375–388<::chart: A 2x2 grid of line plots showing the solution of the objective functional J(ε₁, ε₂) subject to the state system (1) when combined drugs are administered.The x-axis for all plots is "Days", ranging from 0 to 200.Top-left plot: "Effector cells" (y-axis, scaled by x 10^5). The curve starts around 7.5 x 10^5, peaks at approximately 14 x 10^5 around 30 days, and then decreases towards 0 by 200 days.Top-right plot: "Tumor cells" (y-axis, scaled by x 10^8). The curve starts at 3 x 10^8, rapidly decreases to near 0 by around 50 days, and remains close to 0 thereafter.Bottom-left plot: "Optimal control (ε₁)" (y-axis). The curve starts around 0.23, decreases to about 0.12 around 50 days, then gradually increases to about 0.15 around 150 days, and finally decreases to about 0.05 by 200 days.Bottom-right plot: "Optimal control (ε₂)" (y-axis). The curve starts around 0.57, drops to about 0.1 around 25 days, stays at 0.1 until about 40 days, then jumps back to 0.57 and stays there until about 180 days, finally dropping to about 0.1 by 200 days.Fig. 6. The figure shows the solution of the objective functional J(€1, €2) subject to the state system (1) when the combined drugs are administered. The initial conditions used are E0 = 758509, T0 = 2.86023 × 10^8. B1 = 10^8, B2 = 10^8. Parameters for this simulation are described in Table 1.::>

<a id='47cbe326-29db-48bd-99b3-a65b5f9f6538'></a>

<::chart: The figure contains two line plots side-by-side, representing the solution of the adjoint system. The x-axis for both plots is labeled 'Days' and ranges from 0 to 200. The left plot shows 'Adjoint (η₁)' on the y-axis, ranging from 0 to 3000. The curve starts around 2500, drops to about 1000, rises slightly to around 1300-1400, and then sharply declines to near 0 by 200 days. The right plot shows 'Adjoint (η₂)' on the y-axis, ranging from -500 to 100. The curve starts near 0, dips to a minimum of approximately -450 around 80-90 days, and then rises back towards 0 by 200 days.::>Fig. 7. The figure shows the solution of the adjoint system (3) when the combined drugs are administered. The initial conditions and parameters are same in Fig. 6.

<a id='827413b9-256e-4733-9fe8-c6d6c3877735'></a>

first control ε₁ is heavily depends on the adjoint variable η₁ which shows a triphasic decline of control ε₁ as well as the adjoint variable η₁. Also, the second control ε₂ is solely depends on the second adjoint η₂.

<a id='8bdb0571-48bb-406d-9cb8-c67658f38fb7'></a>

Fifth scenario: an special interest
We have a special fascinate for the Fig. 6. If we watch carefully the second figure of the top panel of Fig. 6, then the tumor cells reduce sharply (approximately zero to 45 days) and flattens out or is in 'dormant stage' from 46 days to 145 days. But important observation is that after 145 days tumor calls can rebound. So, we definitely need a long term study for the dynamics of cancer growth after the administered of therapy. We can elucidate the effects of combined drugs for the case of effector cells. Initially, effector cells has a growth zero to 45 days (approximately) before the sharp decline in their levels. The biological significance is that it takes some time for the side effects of external therapy. From the bottom panel of Fig. 6, it can be noticed that the control pair €1, €2 are entirely depends upon the co-states η₁, η₂ respectively (Fig. 7).

<a id='aa7d95fe-da1e-4cf2-b4a8-30a217fd0a26'></a>

## 7. Conclusions and future directions

We studied a simple mathematical model for competing cells presented by Kuznetsov et al. [1] namely the immune effector cells and malignant tumor cells. The goal of this paper is to understand the biological dynamics of the interaction between two populations and their environment. In order to do this, we applied the optimal treatment strategy by introducing two external therapies, namely ACI, IL-2. The main contribution of this article is that we were accomplished to use the deterministic optimal control theory to obtain the combination of optimal treatment policies. At first, we established the objective functional by remembering the fundamental biomedical goals in our mind. Theoretically, we proved the existence of optimal control by using the uniformly boundedness of the super-solutions. We studied the characterization of optimal control and the uniqueness

<!-- PAGE BREAK -->

<a id='e250cc7e-a357-4f02-a731-b0acff03a895'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375–388

<a id='f1626b5b-e43e-467f-9a80-c6f9a0d28f1e'></a>

387

<a id='5f2acbd6-b1ec-473d-86bb-879f09a6d174'></a>

of optimal control. We also studied the biologically validation of the quadratic optimal control [13]. The proof of the uniqueness of the optimal control system, assure that the optimal control is unique in the depictions. Also, we proved the validation of the maximization of our control pair $\epsilon^\dagger$, $\epsilon^*$ by taking the second variation of Lagrangian functions.

<a id='9202bc4c-f01a-4eb2-a982-8fe553752789'></a>

Numerically, we studied the dynamics of our system by considering four different scenarios, namely no treatment, singular treatment policy either ACI or IL-2 and the role of combined therapy. Fig. 4, depicting the role of combined therapy which shows the more effectiveness to reduce the tumor cells burden. From Fig. 2, we can infer that the single therapy (IL-2) is unable to reduce the tumor mass. From both of the singular therapies, it can be observed that only ACI may be acceptable to reduce the tumor burden in compared to IL-2 [14]. Our special interest about the Fig. 6, shows that the tumor can resurgence at the end of our time window. To the best of our perception, we believe that the effect of two external drugs on this particular mathematical model has not been done previously and for the first time we analytically address the proof of the uniqueness of two controls in cancer dynamics. We got the worthy numerical results as our expectations. From the biomedical viewpoint, the obtained outcomes will provide a good assessment for treatment strategies. We have applied two different therapies in cancer dynamics and solved it both numerically and analytically. We hope that our results in this paper will be helpful for the clinicians and the future researchers who are working in the same field.
Some of the future works are:

<a id='173b3c90-dcd6-4278-a65c-15b9ee3b27f6'></a>

1. Implementation of the state constraint for the tumor cells which may be decline the tumor burden within the small time horizon.
2. Incorporating the time delay for the drug resistance into this mathematical model which may be contribute us a better assessment for designing cancer dynamics.
3. The model can be extended by introducing the dynamics of cytokines (with proper biological justification) and then we can study the combined effects of chemotherapy and immunotherapy.

<a id='6a6f54ee-b1f2-451c-b3d1-b208274fa296'></a>

References

1.  V.A. Kuznetsov, I.A. Makalin, M.A. Taylor, A.S. Perelson, Nonlinear dynamics of immunogenic tumors: parameter estimation and global bifurcation analysis, Bull. Math. Biol. 56 (2) (1994) 295–321.
2.  S. Nandi, S. Khajanchi, A.N. Chatterjee, P.K. Roy, Insight of viral infection of jatropha curcas plant (future fuel): a control based mathematical Study, Acta Analysis Functionalis Applicata 13 (4) (2011) 366–374.
3.  S. Banerjee, S. Khajanchi, S. Chaudhuri, A mathematical model to elucidate brain tumor abrogation by immunotherapy with T11 target structure, PLoS ONE 10 (5) (2015) e0123611, doi: 10.1371/journal.pone.0123611.
4.  S. Khajanchi, S. Banerjee, Stability and bifurcation analysis of delay induced tumor immune interaction model, Appl. Math. Comput. 248 (2014) 652–671.
5.  W.H. Fleming, R.W. Rishel, Deterministic and Stochastic Optimal Control, Sringer-Verlag, New York, 1975.
6.  S. Lenhart, J.T. Workman, Optimal Control Applied to Biological Models, Chapman and Hall/CRC, 2007.
7.  L.S. Pontryagin, V.G. Boltyanskii, R.V. Gamkrelidze, E.F. Mishchenko, The Mathematical Theory of Otimal Process, Wiley, New Jersey, 1962.
8.  S. Khajanchi, Dynamic behavior of a Beddington–DeAngelis type stage structured predator–prey model, Appl. Math. Comput. 244 (2014) 344–360.
9.  D.L. Lukes, Differential Equations: Classical to Controlled, Mathematics in Science and Engineering, Academic Press, New York, 1982.
10. M.I. Kamien, N.L. Schwartz, Dynamic Optimization: The Calculus of Variations and Optimal Control in Economics and Management, North-Holland, Amsterdam, 1991.
11. S.P. Chakrabarty, F.B. Hanson, Optimal control of drug delivery to brain tumors for a distributed parameters model, in: Proceeding of the American Control Conference, 2005, pp. 973–978.
12. W.K. Hackbusch, A numerical method for solving parabolic equations with opposite orientations, Computing 20 (1978) 229–240.
13. G.W. Swan, General applications of optimal control theory in cancer chemotherapy, IMA J. Math. Appl. Med. Biol. 5 (4) (1988) 303–316.
14. S.P. Chakrabarty, S. Banerjee, A control theory approach to cancer remission aided by an optimal therapy, J. Biol. Syst. 18 (1) (2010) 75–91.
15. B.L. Gause, M. Sznol, W.C. Kopp, J.E. Janik, J.W.II Smith, R.G. Steis, W.J. Urba, W. Sharfman, R.G. Fenton, S.P. Creekmore, J. Holmlund, K.C. Conlon, L.A. Vander-Molen, D.L. Longo, Phase I study of subcutaneously administered interleukin-2 in combination with interferon alfa-2a in patients with advanced cancer, J. Clin. Oncol. 14 (8) (1996) 2234–2241.
16. I. Hara, H. Hotta, N. Sato, H. Eto, S. Arakawa, S.S. Kamidono, Rejection of mouse renal cell carcinoma elicited by local secretion of interleukin-2, J. Clin. Oncol. 87 (7) (1996) 724–729.
17. S.A. Rosenberg, M.T. Lotze, Cancer immunotherapy using interleukin-2 and interleukin-2-activated lymphocytes, Annu. Rev. Immunol. 4 (1) (1986) 681–709.
18. R. Kaempfer, L. Gerez, H. Farbstein, L. Madar, O. Hirschman, R. Nussinovich, A. Shapiro, Prediction of response to treatment in superficial bladder carcinoma through pattern of interleukin-2 gene expression, J. Clin. Oncol. 14 (6) (1996) 1778–1786.
19. D.J. Schwartzentruber, In vitro predictors of clinical response in patients receiving interleukin-2 based immunotherapy, Curr. Opin. Oncol. 5 (6) (1993) 1055–1058.
20. D.E. Kirschner, J.C. Panetta, Modeling immunotherapy of the tumor-immune interaction, J. Math. Biol. 37 (3) (1998) 235–252.
21. L.G. de Pillis, W. Gu, A.E. Radunskaya, Mixed immunotherapy and chemotherapy of tumors: modeling, applications and biological interpretations, J. Theor. Biol. 238 (4) (2006) 841–862.
22. N. Bellomo, L. Preziosi, Modelling and mathematical problems related to tumor evolution and its interaction with the immune system, Math. Comput. Model. 32 (2000) 413–452.
23. L.G. de Pillis, A.E. Radunskaya, A mathematical tumor model with immune resistance and drug therapy: an optimal control approach, J. Theor. Med. 3 (2001) 79–100.
24. A. Matzavinos, M.A.J. Chaplain, V.A. Kuznetsov, Mathematical modelling of the spatio-temporal response of cytotoxic T-lymphocytes to a solid tumour, Math. Med. Biol. 21 (1) (2004) 1–34.
25. J. Adam, N. Bellomo, A Survey Models for Tumor-Immune System Dyamics, Birkhuser, Boston (MA), 1997.
26. R.P. Araujo, D.L.S. McElwain, A history of the study of solid tomour growth: the contribution of mathematical modelling, Bull. Math. Biol. 66 (2004) 1039–1091.
27. M. Marhl, M. Perc, Determining the flexibility of regular and chaotic attractors, Chaos, Solitons Fractals 28 (2006) 822–833.
28. S. Khajanchi, Bifurcation analysis of a delayed mathematical model for tumor growth, Chaos, Solitons Fractals 77 (2015) 264–276.
29. M. Bodnar, U. Forys', Periodic dynamics in the model of immune system, Int. J. Appl. Math. Comput. Sc. 10 (1) (2000) 113–126.
30. M. Perc, M. Marhl, Detecting and controlling unstable periodic orbits that are not part of a chaotic attractor, Phys. Rev. E 70 (2004) 016204.
31. Q. Wang, Z. Duan, M. Perc, G. Chen, Synchronization transitions on small-world neuronal networks: Effects of information transmission delay and rewiring probability, Chaos 24 (2014) 023101.
32. F. Castiglione, P. Piccoli, Cancer immunotherapy, mathematical modeling and optimal control, J. Theor. Biol. 247 (4) (2007) 723–732.

<!-- PAGE BREAK -->

<a id='9def2e56-c32f-4275-8be7-95db32e6e73d'></a>

388

<a id='f9bc487f-08e5-432a-9c00-e3d059d8d701'></a>

S. Khajanchi, D. Ghosh/Applied Mathematics and Computation 271 (2015) 375-388

<a id='6eaad212-1be7-4ec1-af67-99e8cfe05080'></a>

[33] K.R. Fister, J.C. Panetta, Optimal control applied to competing chemotherapeutic cell-kill strategies, SIAM J. Appl. Math. 2003 63 (6) (2003) 1954-1971.
[34] L.G. de Pillis, W. Gu, K.R. Fister, T. Head, K. Maples, A. Murugan, T. Neal, K. Yoshida, Chemotherapy for tumors: an analysis of the dynamics and a study of quadratic and linear optimal controls, Math. Biosc. 209 (1) (2007) 292-315.
[35] T. Burden, J. Ernstberger, K.R. Fister, Optimal control applied to immunotherapy, Dis. Cont. Dyn. B 4 (1) (2004) 135-146.
[36] J.M. Murray, Optimal control for a Cancer chemotherapy problem with general growth and loss functions, Math. Biosc. 98 (2) (1990) 273-287.
[37] G.W. Swan, Role of optimal control theory in Cancer chemotherapy, Math. Biosc. 101 (2) (1990) 237-284.
[38] K.R. Fister, J.H. Donnelly, Immunotherapy: an optimal control theory apprach, Math. Biosc. Engg. 2 (3) (2005) 499-510.
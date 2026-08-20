<a id='59fa7492-966b-406e-847f-71a4655d6d35'></a>

Theory in Biosciences (2018) 137:67–78
https://doi.org/10.1007/s12064-018-0261-x

<a id='0c199acb-7390-43a6-a05b-78ce95e482af'></a>

ORIGINAL ARTICLE

<a id='039220f6-9b1a-404a-9632-cd07c04f500b'></a>

<::logo: CrossMark
CrossMark
A red bookmark icon is enclosed within a blue and silver circular emblem.::>

<a id='be4dfd4d-9c65-4493-af04-8fc4e5f5c8f7'></a>

Mathematical modeling of cancer-immune system, considering the role of antibodies

<a id='9f92bfb8-2e90-4961-b684-a50d609d94ec'></a>

Sumana Ghosh¹. Sandip Banerjee¹

Received: 7 February 2017 / Accepted: 9 March 2018 / Published online: 23 March 2018
© Springer-Verlag GmbH Germany, part of Springer Nature 2018

<a id='6a8aba92-6060-4cbd-a2ff-03090150c86c'></a>

**Abstract**
A mathematical model for the quantitative analysis of cancer-immune interaction, considering the role of antibodies has been proposed in this paper. The model is based on the clinical evidence, which states that antibodies can directly kill cancerous cells (Ivano et al. in J Clin Investig 119(8):2143-2159, 2009). The existence of transcritical bifurcation, which has been proved using *Sotomayor theorem*, provides strong biological implications. Through numerical simulations, it has been illustrated that under certain therapy (like monoclonal antibody therapy), which is capable of altering the parameters of the system, cancer-free state can be obtained.

<a id='2c7fd9b1-a542-46d5-8636-b7d32c1761f2'></a>

**Keywords** Cancer cells  B cells  Plasma cells  Antibodies  Global stability  Transcritical bifurcation

<a id='2ca1fee6-4ceb-4e68-b1fb-a7a10587e3a9'></a>

# Introduction

Cancer is a leading cause of death worldwide. Unfortunately,
it is predicted to remain so, for years to come. It is a disease
which is caused by the abnormal function of our own cells.
Cancer is not a single disease; it comprises more than 200
diseases (Gabriel 2007; Schulz 2007), which share common
characteristics, that is, they are abnormal cells, where the
normal processes which regulate normal cell proliferation,
differentiation and death (cell apoptosis) are interrupted,
modified or bypassed. The causes of cancer are the changes
that cause normal cells to acquire abnormal functions. These
causes may be the result of inherited mutation or environ-
mental factors such as tobacco products, ultraviolet radia-
tion, X-rays, chemicals, etc (Schulz 2007). A normal cell can
be transformed into a cancerous cell when certain genes are
activated or inactivated because of mutation and environ-
mental factors. In cancerous cells, the normal control system
that prevents abnormal cell growth and differentiation and
the invasion of other tissues and organs is disabled.

<a id='a3a31996-13db-4769-85c9-86e90c2e5212'></a>

---Sandip Banerjee
sandofma@iitr.ac.in

Sumana Ghosh
sumanaghosh.math@gmail.com

1 Department of Mathematics, Indian Institute of Technology
Roorkee, Roorkee, Uttaranchal 247667, India

<a id='d23412cd-2ffe-4eb1-862b-ab7040940ea8'></a>

The theoretical study of cancer–immune dynamics, which has a long history, has been done by many authors (Adam and Bellomo 1997; Banerjee and Sarkar 2008; Banerjee et al. 2015; Banerjee and Tsygvintsev 2015; Bodnar and Foryś 2000; Chaplain and Matzavinos 2006; Foryś 2002; Kirschner and Panetta 1998; Kirschner and Tsygvintsev 2009; Kolev 2003a, b; Kuznetsov et al. 1994; Khajanchi and Banerjee 2014; Mallet and de Pillis 2006; Preziosi 1996; Sarkar and Banerjee 2005; Szymanska 2003; Tsygvintsev and Banerjee 2014). We first look through some of the existing mathemat-ical models of the cancer–immune system interactions. In Kuznetsov et al. (1994), the authors presented a mathemati-cal model of the cytotoxic T-lymphocyte and its responses to the growth of an immunogenic tumor. They studied the immune stimulation of tumor growth, “sneaking through” of the tumor and the formation of a tumor dormant state. Through mathematical modeling, Kirschner and Panetta (1998) have illustrated the dynamics between tumor cells, immune effecter cells and interleukin-2 (IL-2). Their efforts explain both short -term tumor oscillations in tumor size as well as long-term tumor relapses. Bodnar and Foryś (2000) studied the periodic dynamics in the mathematical model of the immune system. In Marchuk's model of immune system dynamics, Foryś (2002) presented the model of a general immune system reaction. The qualitative behavior of the solution to the model (and its application), along with many illustrations of the recovery process, oscillations or lethal outcomes of the disease have been discussed. In Sarkar and

<a id='2777ca49-8f5a-4bd1-8706-e59bbfec8c70'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol next to the word "Springer" in black text.::>

<!-- PAGE BREAK -->

<a id='9aec638e-1ccb-4a32-a75a-5912f865e953'></a>

68

<a id='f7a9d001-de95-4b04-9121-00b914577d70'></a>

Theory in Biosciences (2018) 137:67–78

<a id='35b3d2bc-4e9f-4dcb-9e8c-df6bb8e2d5ab'></a>

Banerjee (2005), the authors expressed the spontaneous regression and progression of a malignant tumor as a prey-predator like system, where the tumor (cancerous cells) is treated as prey and the cytotoxic T-lymphocytes as predator. The deterministic model is extended to a stochastic one, allowing random fluctuations around the positive interior equilibrium point. The stochastic stability properties of the model are investigated both analytically and numerically. Mallet and de Pillis (2006) have presented a hybrid cellular automaton partial differential equation model of moderate complexity, to describe the interaction between tumor and the immune system of the host. Chaplain and Matzavinos (2006) have explained the effect of time and space in tumor immunology using a mathematical model, that is, the spatiotemporal phenomena. The role of interleukin-2 (IL-2) in tumor dynamics is illustrated through mathematical modeling (a modified version of the Kirschner–Panetta model) in Tsygvintsev and Banerjee (2014), where the authors have shown that interleukin-2 alone can cause the tumor cell population to regress. In Kirschner and Tsygvintsev (2009), the global dynamics of the Kirschner–Panetta model was explored and the conditions under which tumor clearance can be achieved, were obtained.

<a id='079bf15e-7e61-49f2-9310-a12efe598502'></a>

However, not much work has been done on the role of antibodies to eradicate cancer cells through mathematical modeling. This may be due to the fact that until recently no clinical evidence was available to support the fact that anti- bodies are actually capable of killing cancer cells directly. The motivation for this work comes from the investigations by researchers at the University of Manchester along with their collaborators at the University of Southampton. They have shown in their latest study that antibodies can kill can- cer cells directly (Ivanov et al. 2009).

<a id='fb22c6f1-9c65-46b1-b17e-5ba77856d5c2'></a>

In the second section, we formulate the mathematical
model. Linear stability analysis, global stability analysis and
bifurcation analysis of the system are shown in the third sec-
tion. Sensitivity analysis, subset selection and estimation of the
system parameters are discussed in fourth section. Fifth section
deals with the numerical results and their biological implica-
tions. The paper ends with a conclusion in the sixth section.

<a id='2e8207ee-1c4b-4ac0-9af9-5016a84a23bc'></a>

# Model formulation

Let _B_, _P_, _A_ and _T_ be the number of large B cells, plasma cells, antibodies and the cancer cells, respectively, at any time _t_. We assume that the large B cells grow logistically.
The large B cells proliferate with constant intrinsic growth rate _a_ and increase the large B cell population. They can undergo further differentiation into plasma cells at a constant rate _b_. We assume _a_ > _b_ to insure that there can be a net growth in the large B cells population. Thus, the governing equation for the large B cells and the plasma cells is given by

<a id='722da203-ecfa-4fe9-ba35-96e1cc6871f1'></a>

dB/dt = auB(1 - B/k_1) - b(1 - u)B (1)

<a id='96f0cb9f-3d90-4985-bb60-a4d7d90d4ba6'></a>

dP/dt = b(1 - u)B - μ₁P, (2)

<a id='7e4e921c-f304-4e43-bd49-4ef7a1f605ae'></a>

where u (0 < u < 1) is the fraction of the large B cells which
remains as the proliferating large B cells and (1 – u) is the
fraction that differentiates into plasma cells, k₁ is the car-
rying capacity of the large B-cell population, and ₁ is the
natural death rate of the plasma cells.

<a id='f4fecf7b-0699-48c2-a1cd-48dc899a76e2'></a>

The governing equation for the antibody is given by

<a id='07f2a2a7-c7b7-4ddc-9811-c848b7d1083a'></a>

$\frac{dA}{dt} = r_1B + r_2P - \mu_2A \quad (r_1 < r_2),$ (3)

<a id='5216825e-eeb4-4de7-a340-33c2be07deed'></a>

where r₁ and r₂ are the rates at which the large B cells and
the plasma cells secrete antibodies, respectively, 2 is the
decay rate of antibodies. From biological point of view, can-
cerous cells cannot kill antibodies as they are a kind of pro-
tein and hence non living. So, there is no loss of antibodies
due to its interaction with cancerous cells.

<a id='7d136d30-1489-4b5b-b9b3-fd6430ffd6e5'></a>

We assume that the cancerous cells grow logistically
in the absence of the antibodies and the antibodies kill the
cancerous cells directly. Thus, for the cancerous cells, the
governing equation is

<a id='7b10120f-c4e0-4f5e-b25c-35e8ea82ec78'></a>

$$\frac{dT}{dt} = rT\left(1 - \frac{T}{k_2}\right) - \beta_1AT, \quad (4)$$

<a id='989c717e-ed45-43f6-87ab-7cf75dacdce2'></a>

where r is the intrinsic growth rate, k₂ is the carrying capacity of the cancer cells, and β₁ is the rate at which the antibodies kill the cancer cells by direct interaction.

<a id='a9694646-4e72-4712-b8e5-f76432dcaf64'></a>

The initial conditions for systems (1-4) are B(0) = B₀ > 0;
P(0) = P₀ > 0; A(0) = A₀ > 0 and T(0) = T₀ > 0
respectively.

<a id='8654853f-c585-4b90-8065-fbae820118ef'></a>

## Analysis of the system

### Positivity and boundedness of solution

Throughout the paper, we denote $q_0 = au - b(1 - u)$ and assume that it is positive.

<a id='0ae10d17-d6a6-4f9f-ba1a-43d2f66db517'></a>

**Theorem 1** *Let the initial conditions of system (1-4) be positive, then the solutions (B (t), P (t), A (t), T (t)) of the system are nonnegative for all t > 0.*

<a id='1b6e47f0-9d8b-427c-8c18-10488c29a7d9'></a>

**Proof** Consider the system of Eq. (1–4) in vector form as

<a id='41ffd36f-aaae-488b-bc30-c9fe271f10f3'></a>

X(t) = col(B(t), P(t), A(t), T(t)) ∈ R_+^4

<a id='c54e6ee6-d88c-4e0b-b03f-82e30d9d47aa'></a>

and

<a id='1e95ef82-c561-4e2c-ab82-29c3e8a0045f'></a>

<::logo: Springer
Springer
The logo features a stylized black chess knight icon next to the word "Springer".::>

<!-- PAGE BREAK -->

<a id='95e42b2c-971d-473c-ace6-d4c27755cfc7'></a>

Theory in Biosciences (2018) 137:67–78

<a id='b9bdbb75-ec3a-414c-a26f-4aed83ef2c7b'></a>

69

<a id='48007790-2031-4cfe-862a-299e3a462193'></a>

$$\mathcal{H} = \begin{pmatrix} \mathcal{H}_1(X(t)) \\ \mathcal{H}_2(X(t)) \\ \mathcal{H}_3(X(t)) \\ \mathcal{H}_4(X(t)) \end{pmatrix} = \begin{pmatrix} auB\left(1-\frac{B}{k_1}\right) - b(1-u)B \\ b(1-u)B - \mu_1 P \\ r_1B + r_2P - \mu_2A \\ rT\left(1-\frac{T}{k_2}\right) - \beta_1AT \end{pmatrix}. $$

<a id='48a410fc-3d08-4831-8d25-396065772352'></a>

This can be written as

<a id='85eb3746-fe04-457a-9120-68ed0d4557d9'></a>

$\dot{X} = \mathcal{H}(X(t))$, (5)

where $\cdot \equiv \frac{d}{dt}$ with initial conditions
$X(t) = col(B(0), P(0), A(0), T(0)) \in \mathbb{R}^4_+$. Consider the map-
ping $\mathcal{H} : \mathbb{R}^4_+ \rightarrow \mathbb{R}^4$ and $\mathcal{H} \in C^\infty(\mathbb{R}^4)$. It is easy to verify
that $\mathcal{H}(X)|_{x_i=0} = \mathcal{H}_i(0) \ge 0, \forall i = 1, 2, 3, 4$. Due to the well
known theorem by Nagumo (1942), the solution of (1-4)
with initial conditions $X_0 \in \mathbb{R}^4_+$, is such that $X(t) \in \mathbb{R}^4_+$,
for all $t > 0$, that is it remains nonnegative throughout the
region $\mathbb{R}^4_+$, $\forall t > 0$.
□

<a id='588cf1ed-cd6e-40c3-ba1d-5ee08cc9f8b7'></a>

**Theorem 2** *The solutions of system (1–4) with positive initial conditions are bounded.*

<a id='1c729639-0a7e-4387-bc25-b7eb8745817b'></a>

Proof From Eqs. (1) and (2), we have
$\frac{d}{dt}(B+P)=auB(1-\frac{B}{k_{1}})-\mu_{1}P$

<a id='63be6fee-1e7c-42c6-9720-2cf2f8993c9c'></a>

= k₁(μ₁ + au)² / 4au - μ₁(B + P)
- au / k₁ (B - k₁(μ₁ + au) / 2au)²
≤ k₁(μ₁ + au)² / 4au - μ₁(B + P).

<a id='3918dcb9-3d95-425c-9d9c-d95e83432f17'></a>

Hence, using standard differential inequalities, we have

B + P ≤ k₁(μ₁ + au)²
           ———————————————————
           4aμ₁

<a id='f8b2d71a-b5da-4ce8-a67d-65a91a628f35'></a>

Similarly, from Eq. (3) and (4), since B(t) + P(t) is bounded (say, by r₀), we have

<a id='07e4196a-0f03-4751-8cdb-5efcf7678992'></a>

d/dt (A + T) = r_1 B + r_2 P - μ_2 A + rT (1 - T/k_2)

<a id='a8bde5e8-fae1-4fe9-9a0a-7f6364f541b4'></a>

- β₁AT
≤ r₂(B + P) - μ₂(A + T)

<a id='98e2eb76-363c-44bf-910b-eae2ca03a607'></a>

- \frac{r}{k_2} \left(T - \frac{k_2(r + \mu_2)^2}{2r}\right) + \frac{k_2(r + \mu_2)^2}{4r}

<a id='d311eb28-715f-4b65-9e62-a7acba3ba815'></a>

$$\leq r_2r_0 + \frac{k_2(r + \mu_2)^2}{4r} - \mu_2(A + T).$$

<a id='b9ee9130-acb2-49bc-9b32-53ef14f8ab11'></a>

Hence, $A + T \le \frac{rr_0}{\mu_2} + \frac{k_2(r+\mu_2)^2}{4r\mu_2}$. Therefore, the solutions of system (1–4) are bounded. \u25a1

<a id='1fbad6f3-9b8a-41a3-a8a9-c06dc1c66eb8'></a>

## Local stability analysis

The equilibrium points of the system are the trivial equilibrium point $E_0 = (0,0,0,0)$, boundary equilibrium point $E_1 = (0,0,0, k_2)$, the cancer-free equilibrium point $E_2 = (\bar{B}, \bar{P}, \bar{A}, 0)$ and the positive interior equilibrium point $E^* = (\bar{B}, \bar{P}, \bar{A}, T^*)$, where

<a id='b3c52e68-9e98-4102-b64d-879212c01ec3'></a>

\bar{B} = \frac{k_1(au - b(1-u))}{au}

\bar{P} = \frac{b(1-u)\bar{B}}{\mu_1}

\bar{A} = \frac{r_1\bar{B} + r_2\bar{P}}{\mu_2}

T^* = \frac{k_2}{r}(r - \beta_1\bar{A}) (r > \beta_1\bar{A})

<a id='b2236868-7036-4b23-b691-577c11623e09'></a>

The Jacobian matrix $J_{E_2}$ at the cancer-free equilibrium point $E_2$ is given by

$J_{E_2}=\begin{pmatrix}-(au-b(1-u))&0&0&0\\ b(1-u)&-\mu_1&0&0\\ r_1&r_2&-\mu_2&0\\ 0&0&0&r-\beta_1\bar{A}\end{pmatrix}$

<a id='b603f97f-3879-474f-a17b-3f6d019b7279'></a>

and the corresponding characteristic equation is

$(\lambda + au - b(1 - u))(\lambda + \mu_1)(\lambda + \mu_2)(\lambda - (r - \beta_1\bar{A})) = 0$.

Therefore, the equilibrium point $E_2$ is locally asymptotically stable if

$r - \beta_1\bar{A} < 0$

$\Rightarrow \beta_1 > \frac{au\mu_1\mu_2r}{k_1[\mu_1r_1 + br_2(1 - u)][au - b(1 - u)]}$ (6)

<a id='a97dcfc5-081b-4068-97be-6059fbf18542'></a>

The Jacobian matrix J_E* at the interior equilibrium point E* is given by

J_E* = 
| -(au - b(1-u))   0           0          0        |
| b(1-u)           -μ₁         0          0        |
| r₁               r₂          -μ₂        0        |
| 0                0           -β₁T*      -r/k₂ T* |

<a id='dcd4ae90-4fae-4688-a7d5-b2e6bc576835'></a>

and the corresponding characteristic equation is

<a id='e06cdebe-d39b-42bd-81f8-a59129aa3ad7'></a>

(λ + au – b(1 – u))(λ + μ₁)(λ + μ₂)(λ + r/k₂ T*) = 0,

<a id='39aa9a7b-f606-4857-9d0b-02d99d341e7f'></a>

implying that all the eigenvalues are negative (since,
T* > 0). Therefore, the interior equilibrium point E* (if it
exists) is locally asymptotically stable.

<a id='bf59115f-efa1-4fb4-8bea-e30a05fc77d7'></a>

Springer

<!-- PAGE BREAK -->

<a id='ebdc9444-3beb-40a9-b141-e05324505db0'></a>

70

<a id='7b0820d2-e880-4b51-a903-46e9d984656a'></a>

Theory in Biosciences (2018) 137:67–78

<a id='5f0584e6-e17f-4abd-9e30-bde3fabacc64'></a>

Note If q0 = au - b(1-u) < 0, the cancerous-free equilibrium E2 and the positive interior equilibrium point E* of the system will not exist. But, from the linear stability analysis, one can show that the trivial equilibrium point E0 is always unstable and the boundary equilibrium point E1 is locally asymptotically stable. Hence, the stability of the boundary equilibrium point E1 implies the nonexistence of cancer-free and the positive interior equilibrium points.

<a id='078c409e-8527-4411-879d-69fcfb335e3e'></a>

**Global stability analysis**

We now study the global stability of the cancer-free equi-
librium point E₂ and the interior equilibrium point E*.

<a id='c9668f24-0b6b-4fa3-9a4e-b2f0ea35845a'></a>

**Theorem 3** *The locally stable cancer-free equilibrium point E₂ is globally asymptotically stable, provided* β₁ > auμ₁μ₂r / k₁[μ₁r₁ + br₂(1 − u)][au − b(1 − u)].

<a id='d2d9dce9-9e44-4ec6-b86f-7b116493ea1a'></a>

**Proof** The condition β₁ > auμ₁μ₂r / [μ₁r₁ + br₂(1-u)][au - b(1-u)] implies that r - β₁Ā < 0. Hence, the cancer-free equilibrium point E₂ is locally asymptotically stable. From the first equation of the system, we have

<a id='fe312ac0-41fc-4335-b5c7-43cea896c793'></a>

B(t) = q_0 / ( (au/k_1) * (1 - e^(-q_0 t)) + (q_0/B_0) * e^(-q_0 t) )

<a id='42f299c8-15df-4bfd-8215-6c0cff3c4978'></a>

Hence, $\lim_{t\to+\infty} B(t) = \frac{k_1(au-b(1-u))}{au} = \bar{B}$ and for all $t \ge 0$, we have $B(t) < \bar{B}$; assuming that the initial condition $B(0) < \bar{B}$.
Since $B$ is increasing functions for $t \ge 0$, for arbitrary small $\epsilon_1 > 0$, there exists $T_{\epsilon_1} > 0$ such that $B(t) \ge \bar{B} - \epsilon_1$ for all $t \ge T_{\epsilon_1}$. Thus, one has $\bar{B} - \epsilon_1 \le B(t) < \bar{B}$, $\forall t \ge T_{\epsilon_1}$. From the second equation of the system we get, for $t \ge T_{\epsilon_1}$

<a id='6defd2d2-a9b9-4c07-9e66-1a01466be2e3'></a>

$$b(1 - u)(\bar{B} - \epsilon_1) - \mu_1 P \leq \frac{dP}{dt} \leq b(1 - u)\bar{B} - \mu_1 P,$$

<a id='a817760b-aa5d-4a1c-b51f-0bdc588fcda6'></a>

which can be written as

<a id='1520c22a-eea3-46a5-a1de-c99b91d5bd67'></a>

b(1-u)(B - ε1)e^μ1t ≤ (e^μ1t P)'(t) ≤ b(1-u)Be^μ1t

<a id='58e15457-692f-4496-beef-c2d118df5e7e'></a>

Integrating the last inequality in the interval [$T_{\epsilon_1}, t$], one obtains

<a id='655894f3-3eff-4891-813a-798cc7b0f327'></a>

η(B̄ - ε₁) / μ₁ (e^(μ₁t) - e^(μ₁T_ε₁)) ≤ e^(μ₁t) P(t) - e^(μ₁T_ε₁) P(T_ε₁) ≤ ηB̄ / μ₁ (e^(μ₁t) - e^(μ₁T_ε₁))

<a id='e502d618-1b2e-4804-acd3-c4884e44f5a6'></a>

or, after division by eμ1t

<a id='f8ca1f11-231c-49bd-bb86-b1c4cc99d57f'></a>

\frac{\eta(\overline{B} - \epsilon_1)}{\mu_1}(1 - e^{\mu_1(T_{\epsilon_1} - t)}) \le P(t) - e^{\mu_1(T_{\epsilon_1} - t)}P(T_{\epsilon_1}) \le \frac{\eta\overline{B}}{\mu_1}(1 - e^{\mu_1(T_{\epsilon_1} - t)})

<a id='41c08aef-c6a4-4fc2-98a5-d2e44d2d6df2'></a>

where we put $\eta = b(1 - u)$.
If $t \to +\infty$, according to the last inequality and since
$\epsilon_1 > 0$ is arbitrary, we obtain

<a id='5a4f9da2-6263-4593-b495-28cac6871d41'></a>

<::$$\lim_{t \to +\infty} P(t) = \frac{B_1}{\mu_1} = \frac{b(1-u)\bar{B}}{\mu_1} = \bar{P}.$$::>

<a id='d2883c02-06fa-4d01-ba14-3ea15d2f379a'></a>

Now, using the definition of limit superior and limit inferior
of a function we have, for any $\epsilon_2 > 0$, $\exists$ a large $T_{\epsilon_2}$, such that

<a id='befe8358-0504-4241-ac05-d6b6a7954512'></a>

r₁(B - ϵ₂) + r₂(P - ϵ₂) ≤ (dA/dt) + μ₂A ≤ r₁(B + ϵ₂) + r₂(P + ϵ₂), ∀t ≥ Tϵ₂

<a id='90d987fe-d447-41e5-b2e4-e19e5679a7f0'></a>

which can be written as

<a id='3ac03af6-086f-48b4-8f15-ce0aa06eac83'></a>

$r_1(\bar{B} - \epsilon_2) + r_2(\bar{P} - \epsilon_2)e^{\mu_2 t} \leq (e^{\mu_2 t}A)'(t) \leq r_1(\bar{B} + \epsilon_2) + r_2(\bar{P} + \epsilon_2)e^{\mu_2 t}$

<a id='5b18f757-08e7-4970-96d0-8f8162127139'></a>

Integrating the last inequality in the interval [Tε₂, t], one
obtains

<a id='4f5e0f24-49a7-4e75-9846-ca2b1647d510'></a>

$$\frac{r_1(\bar{B} - \epsilon_2) + r_2(\bar{P} - \epsilon_2)}{\mu_2}(e^{\mu_2 t} - e^{\mu_2 T_{\epsilon_2}})$$

$$\le e^{\mu_2 t} A(t) - e^{\mu_2 T_{\epsilon_2}} A(T_{\epsilon_2})$$

$$\le \frac{r_1(\bar{B} + \epsilon_2) + r_2(\bar{P} + \epsilon_2)}{\mu_2}(e^{\mu_2 t} - e^{\mu_2 T_{\epsilon_2}})$$

<a id='c11e9909-86f6-43d3-b816-d1a01cd2badf'></a>

or, after division by e^μ₂t,

r₁(B - €₂) + r₂(P - €₂)
---------------------- (1 - e^μ₂(Tε₂-t))
          μ₂

≤ A(t) - e^μ₂(Tε₂-t)A(Tε₂)

≤ r₁(B + €₂) + r₂(P + €₂)
---------------------- (1 - e^μ₂(Tε₂-t)).
          μ₂

<a id='9351791b-28ca-4181-87e7-1153c05d1337'></a>

If t → +∞, according to the last inequality and since €₂ > 0 is arbitrary, we obtain

$$\lim_{t \to +\infty} A(t) = \frac{r_1 \bar{B} + r_2 \bar{P}}{\mu_2} = \bar{A}.$$

<a id='76db0451-a421-4959-b48c-f99d88d17276'></a>

In the similar manner, using the definition of limit superior and limit inferior of a function in case of A(t) we have, for any $\epsilon_3 > 0$, $\exists$ a large $T_{\epsilon_3}$ such that

<a id='6d776899-a3f3-4e00-873d-966853878256'></a>

$r - \beta_1(\bar{A} + \epsilon_3) \leq \frac{1}{T}\frac{dT}{dt} + \frac{rT}{k_2} \leq r - \beta_1(\bar{A} - \epsilon_3) \forall t \geq T_{\epsilon_3}$

<a id='b4d64738-339f-41dd-a27b-e48818ebb468'></a>

Integrating $\frac{1}{T}\frac{dT}{dt} + \frac{rT}{k_2} \leq r - \beta_1(\bar{A} - \epsilon_3)$ in the interval $[T_{\epsilon_3}, t]$
we get,

<a id='fbcdb1d3-93d2-41ef-8629-a2c7b6607e03'></a>

<::logo: Springer
Springer
The logo features a stylized black chess knight icon next to the word "Springer".::>

<!-- PAGE BREAK -->

<a id='d7596837-ea19-4942-baaa-0ad789288cf2'></a>

Theory in Biosciences (2018) 137:67–78

<a id='605cb24f-4c95-46d0-b868-5a9a0cb92d0e'></a>

71

<a id='3881e403-1cf3-45b8-96d8-af77c7f02c9b'></a>

T(t) ≤ ( (r - β₁(Ā - ε₃))e^((r - β₁(Ā - ε₃))(t - Tε₃)) ) / ( ( (r - β₁(Ā - ε₃)) - (r/k₂)T(Tε₃) ) / T(Tε₃) + (r/k₂)e^((r - β₁(Ā - ε₃))(t - Tε₃)) ) (7)

<a id='103af80c-d85d-4250-8a05-441544e07816'></a>

Similarly, integrating $\frac{1}{T}\frac{dT}{dt} + \frac{rT}{k_2} \ge r - \beta_1(\bar{A} + \epsilon)$ in the interval $[T_{\epsilon_3}, t]$ we get,

<a id='78da4643-991f-47c7-a635-1e5a177c2809'></a>

T(t) ≥ \frac{(r - \beta_1(\bar{A} + \epsilon_3))e^{((r - \beta_1(\bar{A} + \epsilon_3))(t - T_{\epsilon_3}))}}{\frac{(r - \beta_1(\bar{A} - \epsilon_3))}{T(T_{\epsilon_3})} + \frac{r}{k_2}e^{((r - \beta_1(\bar{A} + \epsilon_3))(t - T_{\epsilon_3}))}} (8)

<a id='00d30b4b-3cf5-4d8f-872d-8320b2e68a59'></a>

Now, combining (7) and (8) and taking $t \to +\infty$, if $r - \beta_1 \bar{A} < 0$ and since $\epsilon_3 > 0$ is arbitrary, we obtain

<a id='a2585b88-130d-42a8-9623-1a19aa71215d'></a>

lim_{t→+∞} T(t) = 0.

Therefore, for $r - \beta_1\bar{A} < 0$, that is,
$\beta_1 > \frac{au\mu_1\mu_2r}{k_1[\mu_1r_1+br_2(1-u)][au-b(1-u)]}$, the cancer-free equilibrium
point $E_2 = (\bar{B}, \bar{P}, \bar{A}, 0)$ is globally asymptotically stable. —

<a id='0ddf5380-1f1e-456e-91be-bd817157985d'></a>

**Theorem 4** _The locally asymptotically stable positive interior equilibrium point E* is globally asymptotically stable,_ _if_ $\beta_1 < \frac{\alpha\upsilon\mu_1\mu_2r}{k_1[\mu_1r_1+br_2(1-u)][\alpha u-b(1-u)]}$

<a id='57c0b870-e528-44be-a483-d8760d910d0d'></a>

**_Proof_** For 0 < β₁ < r/Ā, the equilibrium point E* is locally asymptotically stable. From Theorem 3, we have

<a id='1a07d581-98af-4dcd-9e97-1dfcb77b9198'></a>

lim B(t) = B, lim P(t) = P, lim A(t) = A
t->+∞       t->+∞       t->+∞
Rewriting (7) and (8) we get,

<a id='3587559e-bf22-4120-9b56-9c52be831492'></a>

$$T(t) \le \frac{r - \beta_1(\bar{A} - \epsilon_3)}{\left(\frac{r - \beta_1(\bar{A} - \epsilon_3) - \frac{r}{k_2}T(T_{\epsilon_3})}{T(T_{\epsilon_3})}\right) e^{-(r - \beta_1(\bar{A} - \epsilon_3))(t - T_{\epsilon_3})} + \frac{r}{k_2}}$$ \n \n $$T(t) \ge \frac{r - \beta_1(\bar{A} + \epsilon_3)}{\left(\frac{r - \beta_1(\bar{A} + \epsilon_3) - \frac{r}{k_2}T(T_{\epsilon_3})}{T(T_{\epsilon_3})}\right) e^{-(r - \beta_1(\bar{A} + \epsilon_3))(t - T_{\epsilon_3})} + \frac{r}{k_2}}$$

<a id='557ff7ea-3be6-442d-ac99-20ebaed2e2b6'></a>

Now, considering these two expressions and taking $t \rightarrow +\infty$
($r - \beta_1\bar{A} > 0$), we obtain (since $\epsilon_3 > 0$ is arbitrary)

<a id='5ab0da8d-a628-4a7a-a6de-203fc0802916'></a>

$\lim_{t \to +\infty} T(t) = \frac{k_2}{r}(r - \beta_1 \bar{A}) = T^*$.

$\implies \lim_{t \to +\infty} (B(t), P(t), A(t), T(t)) = (\bar{B}, \bar{P}, \bar{A}, T^*).$

<a id='74f5d732-e097-4ad0-8f2b-c196f90879f5'></a>

Hence, the positive interior equilibrium point
E* = (B, P, Ā, T*) is globally asymptotically stable if

β₁ < \frac{a u \mu_1 \mu_2 r}{k_1[\mu_1 r_1 + b r_2 (1-u)][a u - b(1-u)]} □

<a id='936748e2-a7dc-4810-9a45-44c540f3da3c'></a>

## Bifurcation analysis

In this section, we explore the critical parameter values where the qualitative behavior of the system changes. By using the Dulac-Bendixson theorem, one can show that system (1–4) has no closed orbit for positive solutions. Equations (1) and (2) can be solved analytically to give

<a id='e9e46276-6b13-451d-9c0c-0da10e209924'></a>

B(t) = q_0 / ( (au/k_1)(1 - ce^(-q_0t)) ), where c = 1 - (k_1q_0 / (auB_0))

P(t) = P_0e^(-μ_1t) + b(1 - u) ∫_0^t e^(μ_1(s-t))B(s)ds,

<a id='a2ff055e-8a15-48db-9fcc-8b6e774288f3'></a>

which are not closed orbits. To show that the other solutions are also not a closed orbit, we consider the function $m(T, A) = \frac{1}{TA}$. Then

<a id='5bfb6379-1234-424a-a4e7-f105b9a9c793'></a>

L = ∂/∂A (m(T,A) dA/dt) + ∂/∂T (m(T,A) dT/dt)
= ∂/∂A (1/(TA) (r₁B + r₂P - μ₂A))
+ ∂/∂T (1/(TA) (rT (1 - T/k₂) - β₁AT))
= -1/A ( (r₁x + r₂y)/(TA) + r/k₂ ).

<a id='6daf3907-5e7d-4128-8a70-3cc96d3abb06'></a>

Since all the parameter values are positive, L < 0 over
the domain of interest, and hence, the system satisfies the
Dulac–Bendixson theorem. Therefore, there are no limit
cycles or homoclinic connections for the system. Similarly,
from the values of the eigenvalues of the corresponding
Jacobian matrix, there is no Hopf bifurcation.

<a id='0ea35fd5-c4e4-47d0-bfdc-ec43fb9c3ce7'></a>

The system has different steady states depending on the
values of the system parameters. The equilibrium points
E₀ = (0, 0, 0, 0) and E₁ = (0, 0, 0, k₂) exist for all parameter
values. The cancer-free steady state E₂ = (B̄, P̄, Ā, 0) exists
if au - b(1 - u) > 0. The positive steady state E* exists if
r - β₁Ā > 0

<a id='0a499cdc-5be1-4dc6-ab21-7d21341b692c'></a>

The stability of the cancer-free equilibrium point E₂
changes as the value of the parameter β₁ passes through the
critical value β* = r / A = auμ₁μ₂r / (k₁[μ₁r₁ + br₂(1-u)][au-b(1-u)]). Hence, β₁,

<a id='db4b1a34-2952-4651-9361-734a044e4f45'></a>

which represents the effectiveness of the antibodies to
destroy the cancer cells, is a bifurcation parameter for the
system. The Jacobian matrix J at E2 and its transpose have
a simple eigenvalue \u03bb = 0 with corresponding eigenvectors

<a id='82486f74-b830-4322-bf35-fb1b3cad9f31'></a>

<::logo: Springer
Springer
The logo features a stylized black knight chess piece next to the word "Springer".::>

<!-- PAGE BREAK -->

<a id='b512677d-6061-48ed-91d3-46e19ac339c8'></a>

72

<a id='778caa15-745b-4ec0-935f-aaba0f7c08e8'></a>

Theory in Biosciences (2018) 137:67–78

<a id='71f4f8ce-9873-47a7-acc0-fb2e18d72e8d'></a>

vᵀ = (0, 0, 0, 1) and wᵀ = (0, 0, 0, 1), respectively, at the
bifurcation parameter value β₁ = r/Ā. If f_β₁ denotes the
vector of partial derivatives of the components of the
right-hand side of system (1–4) with respect to the scalar
β₁ and Df(E₂, β₁)v is the directional derivative of f in the
direction of v at the equilibrium point E₂, then

<a id='e76b349e-df35-4d2f-a659-c96f5fc3e85f'></a>

w^T f_{\beta_1} (E_2) = 0,
w^T [D f_{\beta_1} (E_2, \beta^*)v] = -\bar{A} = -\frac{r}{\beta^*},
w^T [D^2 f(E_2, \beta^*)(v, v)] = \frac{2r}{k_2},

<a id='b334563d-fdc7-41ad-8b8d-936ef5654a84'></a>

Therefore, all three properties (see "Appendix") for the existence of transcritical bifurcation hold and we conclude by Sotomayor's theorem, the system experiences a transcritical bifurcation at the cancer-free equilibrium point E₂ = (B̄, P̄, Ā, 0), as the parameter β₁ passes through the bifurcation parameter value β₁ = β* = r/Ā.

<a id='13f89bbc-b1e4-46a9-a085-4da4bea10a00'></a>

## Sensitivity analysis, subset selection and parameter estimation

Sensitivity analysis determines influence of changes in parameters of model output. Following in the line of Fink et al. (2008), we obtain sensitivity graph using the code myAD, developed by Fink (2006) (see Fig. 1a). To quantify the sensitivities from the figures, we calculate the sensitivity coefficient by non-dimensionalizing the sensitivity functions and computing L₂ norm of the resulting functions, given by

<a id='9e272a81-f2a7-4a17-8c99-9f9ddbae37a3'></a>

$$C_{ij} = \left\| \frac{\partial x_i}{\partial q_j} \frac{q_j}{\text{maxx}_i} \right\|_2^2 = \int_{t_0}^{t_f} \left| \frac{\partial x_i}{\partial q_j} \frac{q_j}{\text{maxx}_i} \right|^2 dt \quad (9)$$

<a id='3cae0dd2-fd44-47a4-befe-68e960d04fc9'></a>

After comparing and ranking the sensitivity function,
we sort the most sensitive parameters (in descending
order) to the least ones (see Fig. 1B), which shows that
the parameters k₂ and β₁ are the most sensitive parameters,
along with µ₂, r and r₂.

<a id='4ccb0598-f948-4d7f-8b4f-999ea2959d36'></a>

A parameter is said to be practically identifiable if a unique estimate can be obtained from different initial values using the available data. After computing the normalized sensitivity function matrix S using automatic differentiation (Fink 2006), we define Fisher's information matrix F = Sⁿ S. It follows that the m parameters are locally identifiable if and only if the column rank of the matrix S is equal to m, or equivalently det(Sⁿ S) ≠ 0. We next use the QR factorization technique with the column pivoting, which is implemented in the MATLAB routine qr, [Q, R, P] = qr(F). This method determines a permutation matrix P such that FP = QR (QR being the factorization of FP). The indices in the first k columns of P identify the k parameters that are most estimable. In our case, ̒₁, ̗₁, b, r, a, ̗₂ are the system parameters that are most estimable from the synthetic data.

<a id='06ba53d8-6f5e-4abe-86d7-f736f51e8788'></a>

The parameters $a, b, \mu_1, k_1, u, r_1, r_2, r, k_2$ are obtained from literature, and their values are given in tabular form in Table 1. The interaction term between antibodies and cancerous cells, namely $\beta_1$ and the decay rate of antibodies, that is, $\mu_2$ are estimated using synthetic data.

<a id='841fdea5-68ca-4d49-9a07-da2f4e370eb8'></a>

To generate synthetic data, we consider the research arti-cle by de Pillis et al. (2006). We first generate a figure (see Fig. 2a) taking human data, patient 9, as given in Table 2 of de Pillis et al. (2006). This figure (see Fig. 2a) reflects the behavior of the model by de Pillis et al. (2006), who have used parameters taken from experimental results of patient from study of Rosenberg et al. (2004) on metastatic melanoma. In the generated figure, they have investigated a tumor comprising 106 cells, a size that in silico, the innate immune system cannot control on its own. The figure shows the effect of immunotherapy alone against the tumor, namely

<a id='487ce49d-92b2-489c-9fd8-d0cece667a3e'></a>

Table 1 Parameter values
<table><thead><tr><th>Parameter</th><th>Parameter values and units</th></tr></thead><tbody><tr><td><i>a</i> (growth rate of large B cells)</td><td>0.1 day<sup>-1</sup> Perelson et al. (1976)</td></tr><tr><td><i>b</i> (conversion rate of large B cells into plasma cells)</td><td>0.01 day<sup>-1</sup> Perelson et al. (1976)</td></tr><tr><td><i>μ</i><sub>1</sub> (natural death rate of plasma cells)</td><td>0.01 day<sup>-1</sup> Perelson et al. (1976)</td></tr><tr><td><i>K</i><sub>1</sub> (carrying capacity of large B cells)</td><td>10<sup>6</sup> cells Perelson et al. (1976)</td></tr><tr><td><i>u</i> (the fraction of daughter cells which remain as large B cells)</td><td>0.1 Perelson et al. (1976)</td></tr><tr><td><i>r</i><sub>1</sub> (rate at which large B cells secrete antibodies)</td><td>100 Ab cell<sup>-1</sup> day<sup>-1</sup> Nossal and Makela (1962)</td></tr><tr><td><i>r</i><sub>2</sub> (rate at which plasma cells secrete antibodies)</td><td>1000 Ab cell<sup>-1</sup> day<sup>-1</sup> Nossal and Makela (1962)</td></tr><tr><td><i>μ</i><sub>2</sub> (decay rate of antibodies)</td><td>6.8840 day<sup>-1</sup> (estimated)</td></tr><tr><td><i>r</i> (intrinsic growth rate of cancer cells)</td><td>0.431 day<sup>-1</sup> de Pillis et al. (2006)</td></tr><tr><td><i>K</i><sub>2</sub> (carrying capacity of cancer cells)</td><td>9.8 × 10<sup>8</sup> cells de Pillis et al. (2006)</td></tr><tr><td><i>β</i><sub>1</sub> (death rate of cancer cells due to interaction with antibodies)</td><td>3.0218 × 10<sup>7</sup> Ab<sup>-1</sup> day<sup>-1</sup> (estimated)</td></tr></tbody></table>

<a id='ab76fb63-0460-4779-8e65-b0f931a88db3'></a>

<::logo: Springer
Springer
The logo features a stylized black chess knight icon next to the word "Springer".::>

<!-- PAGE BREAK -->

<a id='66bf7923-4c79-486f-a767-807ffb602537'></a>

Theory in Biosciences (2018) 137:67–78

<a id='0d20a735-8512-4efc-801e-97239e259174'></a>

73

<a id='2a0a24ca-a799-4f73-91be-6515de906bcf'></a>

<::Eleven line charts arranged in 4 rows and 3 columns, all sharing a common x-axis labeled "Time" ranging from 0 to 100. The y-axis label "Cancer cells" is positioned vertically on the left side of the first column of charts.: chart::>

<::chart::>
**Chart a:**
Y-axis: x 10^8
Trend: The line starts near 0, decreases to a minimum of approximately -10 x 10^8 around x=60, and then increases back to 0 by x=80.

**Chart u:**
Y-axis: x 10^8
Trend: The line starts near 0, decreases to a minimum of approximately -5 x 10^8 around x=60, and then increases back to 0 by x=80.

**Chart K_1:**
Y-axis: Values from 0 to -30
Trend: The line starts at 0, decreases to a minimum of approximately -30 around x=60, and then increases back to 0 by x=80.

**Chart b:**
Y-axis: x 10^8
Trend: The line starts near 0, increases to a maximum of approximately 4 x 10^8 around x=60, and then decreases back to 0 by x=80.

**Chart μ_1:**
Y-axis: x 10^9
Trend: The line starts at 0, increases to a maximum of approximately 1.5 x 10^9 around x=60, and then decreases back to 0 by x=80.

**Chart r_1:**
Y-axis: x 10^4
Trend: The line starts near 0, decreases to a minimum of approximately -5 x 10^4 around x=60, and then increases back to 0 by x=80.

**Chart r_2:**
Y-axis: x 10^4
Trend: The line starts near 0, decreases to a minimum of approximately -10 x 10^4 around x=50, and then increases back to 0 by x=80.

**Chart μ_2:**
Y-axis: x 10^7
Trend: The line starts at 0, peaks around x=5 at approximately 5 x 10^7, dips, then rises to another peak of approximately 5 x 10^7 around x=60, and then decreases back to 0 by x=80.

**Chart r:**
Y-axis: x 10^7
Trend: The line starts at 0, peaks around x=5 at approximately 10 x 10^7, dips, then rises to another peak of approximately 7 x 10^7 around x=60, and then decreases back to 0 by x=80.

**Chart K_2:**
Y-axis: Values from 0 to 1
Trend: The line starts at 0, increases to a maximum of approximately 0.8 around x=10, and then gradually decreases back to 0 by x=80.

**Chart β_1:**
Y-axis: x 10^16
Trend: The line starts near 0, decreases to a minimum of approximately -2.5 x 10^16 around x=10, rises to near 0 around x=40, dips to approximately -2 x 10^16 around x=65, and then increases back to 0 by x=80.::>

<a id='c86db7d9-a5ae-4e23-b22d-dd1f652b55e1'></a>

<::A scatter plot titled "Relative sensitivities of the parameters using automatic differentiation and the corresponding L₂ norm". The x-axis is labeled "Parameters" and ranges from 0 to 11. The y-axis is labeled "L₂ norm" and ranges from 0 to 9. The plot shows several points. The top-left corner is labeled 'b'. Key points with labels are: a point at approximately (1, 8) labeled 'k₂', a point at approximately (2.5, 7.2) labeled 'β₁', a point at approximately (3.5, 5.8) labeled 'μ₂', a point at approximately (4.2, 5.1) labeled 'r', and a point at approximately (5, 1.2) labeled 'r₂'. Other points are clustered near y=0 for x values 6 through 11. The caption states: "Fig. 1 Relative sensitivities of the parameters using automatic differentiation and the corresponding L₂ norm. a Sensitivity of a parameter is identified by the maximum deviation of the state variable (along y axis). It also identifies the time intervals wl sensitive to such changes. b Sensitivity quant sensitivity coefficient through L₂ norm": graph::>

<a id='050d9ca6-b9bb-4a9d-8e9c-2670d85819fa'></a>

y axis). It also identifies the time intervals when the system is most sensitive to such changes. b Sensitivity quantification by calculating sensitivity coefficient through L₂ norm

<a id='b5b06486-47e0-426c-893a-03ed18b14363'></a>

Springer

<!-- PAGE BREAK -->

<a id='cc628d8d-6e3c-471b-9808-3cb7f3e932ea'></a>

74

<a id='2d7dc1ad-946a-4ce0-8d2c-ebc9c97f2ddf'></a>

Theory in Biosciences (2018) 137:67–78

<a id='8942200a-7351-4bef-986e-12214350d006'></a>

<::Figure: The figure consists of two plots, labeled 'a' and 'b'. Both plots share the y-axis label 'Number of Cancer Cells' (scaled by 10⁵) and the x-axis label 'Time (Days)'. Plot 'a' is a line graph showing a smooth, exponentially decaying curve, starting around 10 x 10⁵ and approaching zero by approximately 3 days. Plot 'b' is also a line graph, showing a similar decaying trend, but with discrete red circular markers indicating data points at 0, 0.5, 1, 1.5, 2, 4, 6, and 8 days. The blue line represents the curve of best fit passing through these points. Fig. 2 The figures show how synthetic data have been generated and used to estimate the system parameters μ₂ and β₁. a Generated by taking the model and parameter values from human data, patient 9 as given in Table 2 of de Pillis et al. (2006). b Shows the curve of best fit for the estimation of the parameters μ₂ and β₁. Using least square method, the estimated values of μ₂ and β₁ are, respectively, μ₂ = 6.8840 day⁻¹ and β₁ = 3.0218 × 10⁻⁷ Ab⁻¹ day⁻¹::>


<a id='7d273429-e48e-481a-9655-19439a80f345'></a>

a TIL (tumor infiltrating lymphocyte) injection, followed by short doses of IL-2. Using DataThief (www.datathief.org), the data for cancer cells decay are extracted (say, for 20 time points) and some noise is added to the data, which we name as observed values, $T_{obs}$ (say). To start the estimation process, we initially choose (within meaningful biological range) the values of the parameters to be estimated, namely $\beta_1$ and $\mu_2$ arbitrarily. Next, we solve equations (1–4) numerically with these initial values of the parameters and obtain the solution of the model at those time points, where the observed values have been obtained, which we name as calculated values, $T_{cal}$ (say). We now use the least squares method to minimize the sum of the residuals, namely $\sum_{i=1}^{20} (T^{(i)}_{cal} – T^{(i)}_{obs})^2$ to obtain the estimated values of the system parameters, namely $\beta_1$ and $\mu_2$. In practice, a MATLAB code has been developed to carry out the above process and the estimated values of the parameters are obtained as $\beta_1 = 3.0218 \times 10^{-7}$ and $\mu_2 = 6.8840$. Figure 2b shows the best fit estimate for the model parameters.

<a id='1dc69d95-658f-4183-92b5-6ba160c954a3'></a>

## Numerical results

In this section, we present the numerical results of the system
(1–4) for the parameter values given in Table 1. The steady
state E₀ = (0, 0, 0, 0) and E₁ = (0, 0, 0, k₂) exist for the param-
eter values given in Table 1. The cancer-free equilibrium point
E₂ = (B̄, P̄, Ā, 0) exists for the system parameters provided that

<a id='03965b3f-5531-4d4e-8516-1b6b290158b4'></a>

au > b(1 - u), which holds true for the parameter values given
in Table 1. The positive interior equilibrium point
E* = (B̄, P̄, Ā, T*) exists if β₁ < (auμ₁μ₂r) / ([μ₁r₁ + br₂(1-u)][au - b(1-u)]), that is,

<a id='89731f63-4e44-4743-87f5-e85403343055'></a>

if β < 2.967 × 10⁻⁸, keeping the other parameter values fixed,
as shown in Table 1.

<a id='26f5ebde-3557-4f64-b22a-5693a600e90f'></a>

By linearizing the system about the steady states, the stability of the equilibrium points are determined, which is important from biological point of view. From the linear stability analysis we observe that, the equilibrium points E₀ = (0,0,0,0) and E₁ = (0,0,0, K₂) are unstable for $au-b(1-u) > 0$. The cancer-free equilibrium point E₂ is stable if $\beta_1 > \frac{au\mu_1\mu_2r}{[\mu_1r_1+br_2(1-u)][au-b(1-u)]} = \beta^*(= 2.967 \times 10^{-8})$

<a id='013543d9-55ab-451b-99bc-1581103dc9de'></a>

and it also attains global stability in that region (Fig. 3a, b).
The endemic equilibrium point E* exists and is globally stable
if β₁ < β*(= 2.967 × 10⁻⁸) (Fig. 3c). However, in that region,
the cancer-free equilibrium point also exists, but it is a saddle
point (unstable). Thus, as β₁ passes through the critical value
β* = 2.967 × 10⁻⁸, the stability of E₂ changes from unstable
to a stable one and the system has a transcritical bifurcation at
this point (verified by Sotomayor's theorem and the software
Matcont, Fig. 3d).

<a id='1eec6801-5cd2-4f56-a24d-b2f9eb295b1e'></a>

Figure 4 shows the dynamics of the cancer cells with varying β₁, the killing rate of cancer cells by antibodies. When β₁ < β*(= 2.967 × 10⁻⁸), the cancer cells grow and reach to a steady state (Fig. 4a). However, in Fig. 4b, c, the cancer cells first reduce significantly but fail to maintain that state and grow to a high cancer steady state. This may be due to the existence of both cancer free and endemic equilibria in the region β₁ < β*. The endemic equilibrium is globally stable, and hence, the cancer burden reaches the nonzero steady state (Fig. 4a–c). But when β₁ < β*, the cancer-free equilibrium point is a saddle (unstable), as we know that in case of a saddle point, two paths approach and enter the point and two paths move away from the point, which may be the reason for initial decrease of the cancer cells but ultimately fail to sustain due to the unstable nature (Fig. 4b, c). When β₁ > β*, the interior equilibrium does not exist and the cancer-free steady state is globally stable. Hence, the cancer cells are eradicated due to antibody attack (Fig. 4d).

<a id='ed45c6bb-3f1f-4988-a26c-fc8af41ee939'></a>

Figure 5 shows the overall dynamics of all the state varia-bles, namely B cells, plasma cells, antibodies and cancer cells. For β₁ = 3.0218×10⁻⁷ Ab⁻¹day⁻¹, the cancer cells decay to zero at a much faster rate. The B cells, plasma cells and antibodies reach their respective steady state, and we obtain a cancer-free system.

<a id='48c33b4e-db4a-4b03-a35e-f0854fc7bdbc'></a>

# Conclusion

In this paper, we have formulated a system of nonlinear ordinary differential equations that describes the stimulatory effect of cancerous cells on immune cells in conjunction

<a id='caa9269a-add3-4289-b537-fbb689b5cfef'></a>

<::logo: Springer
Springer
The logo features a black outline of a knight chess piece next to the word "Springer".::>

<!-- PAGE BREAK -->

<a id='b0e85761-59a9-40a6-b2d2-cd2a9f87f906'></a>

Theory in Biosciences (2018) 137:67–78

<a id='b2eeb840-4067-4c76-a1f5-33dbab600ae5'></a>

75

<a id='c1f1375d-7a7e-4cc5-ba34-775cb44f8044'></a>

<::chart: Plot a: Number of Cancer cells (x 10^8) vs. Time. Curves representing different initial conditions (T₀) for cancer cell population decreasing over time. Legend: Green: T₀ = 0.5 x 10^8, Pink: T₀ = 10^8, Cyan: T₀ = 3 x 10^8, Red: T₀ = 6 x 10^8, Blue: T₀ = 9 x 10^8.::><::chart: Plot b: Number of Cancer cells (x 10^6) vs. Time. Curves representing different initial conditions (T₀) for cancer cell population decreasing over time. Legend: Green: T₀ = 10^5, Pink: T₀ = 10^6, Cyan: T₀ = 2 x 10^6, Red: T₀ = 5 x 10^6, Blue: T₀ = 10^7.::><::chart: Plot c: Number of Cancer cells (x 10^8) vs. Time. Curves representing different initial conditions (T₀) for cancer cell population increasing and then stabilizing over time. Legend: Orange: T₀ = 0.01, Green: T₀ = 0.1, Pink: T₀ = 1, Cyan: T₀ = 10, Red: T₀ = 100, Blue: T₀ = 1000.::><::chart: Plot d: Number of Cancer cells vs. β₁. A horizontal line at y=0 with a point labeled "H BP" at approximately β₁ = 2.9 x 10^-8. An arrow points from "H BP" to a box containing "2.967 x 10^-8".::>Fig. 3 The figures show the global stability of the cancer-free and interior equilibrium points. The cancer-free equilibrium is globally stable for β₁ > β* = 2.967 × 10⁻⁸. The value of β₁ for a, b is 3.5 × 10⁻⁸ and for c is 1.0135 × 10⁹. d Shows transcritical bifurcation with respect to the parameter β₁, given by BP (branching point), the point H is called a neutral saddle, which is biologically not meaningful

<a id='af5edcd2-7e60-4c69-8c47-49c80bb9b5ca'></a>

with antibodies. The model we have proposed is simple and
more of general type. The major difference of our model
from that of the existing literature in this area is that the
immune system we considered here is antibody mediated
(T-cell independent) immune response. In this model, a sig-
nificant role is played by β₁, the effectiveness of the antibod-
ies to kill the cancer cells directly.

<a id='751d96f8-b9fc-4e9f-ac2a-983b563db70d'></a>

From our study we observe that for certain values of ̘₁,
one can control the unlimited growth of the cancer cells.
From the analysis of our model, we determine some criterion
for the existence of the equilibrium points of the system and
the stability conditions. The interior equilibrium point E*
is globally stable whenever it exists. This implies that the
cancer cells will escape immune surveillance unless each
and every cancer cells are killed, that is, the system will
ineluctably return to the high cancer state if the treatment
is stopped. Thus, in order to realistically effect a cure when
the cancer-free equilibrium point is unstable, a therapy or
treatment must ensure that not only the cancer burden must
be reduced, but the therapy itself is capable of changing the
parameter values of the system. In this context, monoclo-
nal antibody therapy of cancer (Adams and Weiner 2005) is

<a id='d7ee8585-a3d2-4e82-80bb-e390e42cf036'></a>

suggested as treatment, which may be capable of changing
the system parameters. Monoclonal antibodies can be used
to target a number of cancer associated targets, including
tumor associated blood vessels, vascular growth factors,
diffuse malignant cells like leukemia, cancer cells within
a solid tumor and tumor associated stroma like fibroblasts.

<a id='8aed84b5-7323-4334-a7ad-a6f69b60dbed'></a>

As the value of β₁ crosses certain critical value, the cancer cells always decays to zero, no matter what the initial size is. As stated earlier, the effect of monoclonal therapy, which is capable of changing the system parameter, is evidently visible in this region, that is, when β₁ > β*. In this therapy, a monoclonal antibody can be directed to attach to certain cancer cells. Cetuximab (Erbitux), a monoclonal antibody approved to treat colon cancer and head and neck cancers, attaches to receptors on cancer cells that accept a certain growth signal (epidermal growth factor). Cancer cells and some healthy cells rely on this signal to tell them to divide and multiply. Blocking this signal from reaching its target, may slow or stop the cancer cells from growing. There are a number of monoclonal antibody drugs that are available to treat various types of cancer by (a) making the cancer cells more visible to the immune system (b) delivering radiation

<a id='eecd86ad-6f74-4a77-b82c-9f1d9055c711'></a>

<::logo: Springer
Springer
The logo features a black silhouette of a chess knight, symbolizing knowledge and strategy, placed to the left of the brand name "Springer".::>

<!-- PAGE BREAK -->

<a id='6877587b-9315-4897-9011-2f151babdcf3'></a>

76

<a id='9517ffc7-2e29-482e-ba39-7ad450c67b91'></a>

Theory in Biosciences (2018) 137:67–78

<a id='ec67b09f-6cc6-481f-b1f8-8f40eac6e11f'></a>

<::chart: The image displays two line graphs, labeled (a) and (c), illustrating the dynamics of cancer cells over time. Both graphs have 'Time (Days)' on the x-axis, ranging from 0 to 500, and 'Number of Cancer Cells' on the y-axis, ranging from 0 to 10 (scaled by x 10⁸). Plot (a): The curve, labeled with β₁ = 1.0 x 10⁻⁹, starts at approximately 1 x 10⁸ cells, increases rapidly to about 7 x 10⁸ cells by 50 days, and then gradually approaches a steady state around 9 x 10⁸ cells by 300 days. Plot (c): The curve, labeled with β₁ = 4.5 x 10⁻⁹, starts at approximately 1 x 10⁸ cells, decreases to near 0 cells by 50 days, remains low until about 100 days, then rapidly increases to about 7 x 10⁸ cells by 200 days, and gradually approaches a steady state around 9 x 10⁸ cells by 400 days.::>Fig. 4 The figures show dynamics of cancer cells for different kill rates (β₁) of antibodies, when they are interacting with cancer cells. When β₁ < β*(= 2.967 × 10⁻⁸), the cancer cells grow and reach a steady state (a). However, in figures b and c, the cancer cells first

<a id='09b033d7-08c2-4796-bf0d-a33cf2a8bdd4'></a>

<::chart: Two line graphs, labeled (b) and (d), illustrating the number of cancer cells over time. Plot (b) shows the number of cancer cells (y-axis, x 10^8) versus time (x-axis, Days) for β₁ = 4.0 x 10^-9. The blue line starts at approximately 1 x 10^8, dips slightly, then increases significantly from day 75 to day 200, reaching around 7.5 x 10^8, and then levels off to about 8 x 10^8 by day 500. Plot (d) shows the number of cancer cells (y-axis, x 10^7) versus time (x-axis, Days) for β₁ = 3.5 x 10^-8. The blue line starts at 10 x 10^7 (10^8), decreases rapidly over the first 1.5 days, approaching zero, and remains at zero from approximately day 2 to day 5. These plots illustrate how cancer cells reduce significantly but fail to maintain that state and grow to a high cancer state in (b). When β₁ > β*, as shown in (d), the cancer cells delay to zero due to antibody attack.::>

<a id='4b5a4865-bf64-43c4-a5b0-7bc0f5005b18'></a>

<::chart: The figure contains two line graphs. The top graph, labeled 'a', shows the 'Number of B Cells' (scaled by x 10^4) on the y-axis against 'Time (Days)' on the x-axis. The curve starts at approximately 9 x 10^4 B cells at Time 0 and increases to around 9.8 x 10^4 B cells at 2500 days. The bottom graph, labeled 'c', shows the 'Number of Antibodies' (scaled by x 10^7) on the y-axis against 'Time (Days)' on the x-axis. The curve starts at approximately 15 x 10^7 Antibodies at Time 0 and decreases rapidly, then gradually, towards a low value by 1000 days.::>Fig. 5 The figures show the overall dynamics of all the state variables, namely B cells, plasma cells, antibodies and cancer cells. For $\beta_1 = 3.0218 \times 10^{-7}$ Ab$^{-1}$ day$^{-1}$, the cancer cells decay to zero at a 

<a id='4a3f87ab-592a-41a8-a249-ce5fca92d576'></a>

<::Figure: Two line graphs showing cell counts over time.The top graph, labeled 'b', displays the "Number of Plasma Cells" (x 10^5) versus "Time (Days)". The curve starts at approximately 10 x 10^5 plasma cells and decreases rapidly, then gradually approaches zero by around 400 days, stabilizing at a very low number by 1000 days.The bottom graph, labeled 'd', displays the "Number of Cancer Cells" (x 10^7) versus "Time (Days)". The curve starts at approximately 10 x 10^7 cancer cells and decreases very rapidly, reaching near zero within approximately 0.2 days and remaining at zero until 2 days.: figure::>much faster rate. The B cells, plasma cells and antibodies reach their respective steady state, and we obtain a cancer-free system

<a id='11d842f3-2fd4-4b99-9c4d-b3395a0d9d61'></a>

<::logo: Springer
Springer
The logo features a black outline of a knight chess piece next to the word "Springer".::>

<!-- PAGE BREAK -->

<a id='ec80f3eb-08e2-4d31-a085-47232948821d'></a>

Theory in Biosciences (2018) 137:67–78

<a id='366b140f-eb26-4bfb-88c6-10cbe607998f'></a>

77

<a id='355d39bf-2774-4466-bdfb-cb8a4f8283d8'></a>

to cancer cells (c) slipping powerful drugs into cancer cells.
Recent clinical investigations show that they are capable of
killing cancer cells directly (Ivanov et al. 2009). However,
more clinical trials are necessary before such treatment may
be applied in a clinical setting.

<a id='e577a0e2-7d5b-4e28-8ca1-c0c79e246859'></a>

**Acknowledgements** We are grateful to the anonymous reviewers for their comments and useful suggestions to improve the quality of the paper. This study was supported by the Indo-French Centre for Applied Mathematics (IFCAM) (Grant No. MA/IFCAM/13/120) and the Ministry of Human Resource Development (MHRD) (Grant No. MHR02-41-113-429).

<a id='80a3df1d-cb63-4879-afb1-afd4516aa349'></a>

## Appendix: Sotomayor theorem (Perko 1991)

Consider the system of ordinary differential equations

$\frac{dx}{dt} = f(x, \eta). x \in \mathbb{R}^n,$
(10)

<a id='ce9ed513-de63-41e0-8cee-fd5efdc9312a'></a>

where η ∈ R is a system parameter. It is assumed that the function f is sufficiently differentiable so that all the derivatives appearing in that theorem are continuous on Rⁿ × R. We denote the matrix of partial derivatives of the components of the vector field f with respect to the components of x by Df and the vector of partial derivatives of the components of f with respect to parameter η denoted by fη.

<a id='2f728396-4305-40fb-84f8-38811e79b67d'></a>

**Theorem 5** (Perko 1991) (Sotomayor):*Suppose that f(x₀, η₀) and that n × n matrix B ≡ Df(x₀, η₀) has a simple eigenvalue λ = 0 with eigen vector v and that Bᵀ has an eigen vector u corresponding to the eigenvalue λ = 0. Furthermore, suppose that B has k eigenvalues with negative real parts and (n − k − 1) eigenvalues with positive real parts.*

<a id='5a5c166e-d184-4384-9aa4-13e7d342b742'></a>

(i) If the following conditions are satisfied

uᵀ fη(x₀, η₀) ≠ 0, uᵀ [D²f(x₀, η₀)(v, v)] ≠ 0 (11)

Then there is a smooth curve of equilibrium point
of (10) in Rⁿ × R passing through (x₀, η₀) and tangent
to the hyperplane Rⁿ × η₀. Depending on the signs of
the expressions in (11), there are no equilibrium points
of (10) near x₀ when η < η₀ (or η > η₀) and there are
two equilibrium points of (10) near x₀ when η > η₀
(or η < η₀). The two equilibrium points of (10)
near x₀ are hyperbolic and have stable manifolds of
dimension k and k + 1, respectively, that is, the sys-
tem (10) experiences a saddle-node bifurcation at the
equilibrium point x₀ as the parameter η passes through

<a id='3ebddc9d-5218-4d46-a0d9-62bdede66bde'></a>

the bifurcation value η = n₀. The set of C^∞ -vector fields satisfying the above conditions is an open, dense subset in the Banach space of all C^∞, one parameter vector fields with an equilibrium point at x₀ having a simple zero eigenvalue. (ii)If the following conditions are satisfied

<a id='fa24b172-a143-4890-9327-166fe0d06175'></a>

u^T f_{\eta}(x_0, \eta_0) = 0,
u
uu^T [Df(x_0, \eta_0)v \neq 0
u
uu^T [D^2f(x_0, \eta_0)(v, v)] \neq 0

(12)

<a id='d9cd00f0-ec9f-4357-8dc9-c5bff03461de'></a>

the system (10) experiences a transcritical bifurcation
at the equilibrium point (x₀, η₀) as the parameter η varies through the bifurcation value η = η₀.

<a id='f7b7a50e-dae6-4e29-bfef-88a66999cb11'></a>

# References
Adam J, Bellomo N (1997) A survey of models for tumor immune dynamics. Birkhauser, Boston, MA
Adams GP, Weiner LM (2005) Monoclonal antibodies therapy of cancer. Nat Biotechnol 23(9):1147-1157
Banerjee S, Sarkar RR (2008) Delay Induced-model for tumor-immune interaction and control of malignant tumor growth. Bio Syst 91:268-288
Banerjee S, Khajanchi S, Chowdhuri S (2015) Mathematical model to elucidate brain tumor abrogation by immunotherapy with T11 target structure. PLoS ONE 10(5):1-21
Banerjee S, Tsygvintsev A (2015) Stability and bifurcations of equilibria in a delayed Kirschner–Panetta model. Appl Math Lett 40:65-71
Bodnar M, Foryś U (2000) Periodic dynamics in the model of immune system. Int J Appl Math Comput Sci 10(1):1201-1209
Chaplain MAJ, Matzavinos A (2006) Mathematical modeling of spatiotemporal phenomena in tumor immunology. Springer, Berlin
de Pillis LG, Gu W, Radunskaya AE (2006) Mixed immunotherapy and chemotherapy of tumors: modeling, applications and biological interpretation. J Theor Biol 238:841-862
Foryś U (2002) Marchuk's Model of Immune System Dynamics with Application to Tumor Growth. J Theor Med 4(1):85-93
Fink M (2006) myAD: fast automatic differentiation code in Matlab. http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?objectId=15235. Accessed 28 Oct 2016
Fink M, Batzel JJ, Tran H (2008) A respiratory system model: parameter estimation and sensitivity analysis. Cardiovasc Eng 8:120-134
Gabriel JA (2007) The biology of cancer, 2nd edn. Wiley, Boca Raton
Ivanov A, Beers SA, Walshe CA, Honeychurch J, Alduaij W, Cox KL, Potter KN, Murray S, Chan CHT, Klymenko T, Erenpreisa J, Martin GJ, Illidge Tim M, Cragg MS (2009) Monoclonal antibodies directed to CD20 and HLA-DR can elicit homotypic adhesion followed by lysosome-mediated cell death in human lymphoma and leukemia cells. J Clin Investig 119(8):2143-2159
Khajanchi S, Banerjee S (2014) Stability and bifurcation analysis of delay induced tumor immune interaction model. Appl Math Comput 248:652-671
Kirschner D, Panetta JC (1998) Modeling the immunotherapy of tumor–immune interaction. J Math Biol 37(3):235-252
Kirschner D, Tsygvintsev A (2009) On global dynamics of a model for tumor immunotherapy. Math Biosci Eng 6(3):579-583

<a id='7fb88d7a-2e43-44f6-a91f-231a799fb71e'></a>

Springer

<!-- PAGE BREAK -->

<a id='f39895cc-723c-4605-98ec-1ba72f363590'></a>

78

<a id='28019c92-a0f9-4a6f-99ec-8fe5e7ea3030'></a>

Theory in Biosciences (2018) 137:67–78

<a id='6417430b-cda7-4152-abd5-164caf56f466'></a>

Kolev M (2003a) Mathematical modeling of the competition
between acquired immunity and cancer. Appl Math Comput Sci
13(3):289-296
Kolev M (2003b) Mathematical modeling of the competition between
tumors and the immune systems considering the role of antibod-
ies. J Math Comput Model 37:1143-1152
Kuznetsov VA, Makalkin IA, Taylor MA, Perelson AS (1994) Non-
linear Dynamics of immunogenic tumors: parameter estimation
and global bifurcation analysis. Bull Math Biol 56(2):295-321
Mallet DG, de Pillis LG (2006) A cellular automata model of tumor-
immune system interactions. J Theor Biol 239:334-350
Nagumo N (1942) Uber die Lage der Integralkurven gewonlicher Dif-
ferantialgleichungen. Proc Phys Math Soc Jpn 24:551-567
Nossal GJV, Makela O (1962) Elaboration of antibodies by single cell.
Ann Rev Microbiol 16:53-74
Perelson AS, Mimirani M, Oster GF (1976) Optimal strategies in
immunology, B-cell differentiation and proliferation. J Math Biol
3:325-367

<a id='192196f5-3336-4358-a3b8-0bfa6b48b185'></a>

Perko L (1991) Differential equations and dynamical systems, 2nd edn.
Springer, New York

Preziosi L (1996) From population dynamics to modeling the com-
petition between tumor and immune system. Math Model
23(6):135–152

Rosenberg S, Yang J, Restifo N (2004) Cancer immunotherapy: moving
beyond current vaccines. Nat Med 10:909915

Sarkar RR, Banerjee S (2005) Cancer self remission and tumor stabil-
ity—a stochastic approach. J Math Biosci 196:65–81

Schulz WA (2007) Molecular biology of human cancer. Springer,
Berlin

Szymanska Z (2003) Analysis of immunotherapy models in the context
of cancer dynamics. Int J Appl Math Comput Sci 13(3):407–418

Tsygvintsev A, Banerjee S (2014) Bounded immune response in immu-
notherapy described by delay Kirschner–Panetta model. Appl
Math Lett 35:90–94

<a id='2050d74d-d90b-4236-bc39-b6e5243aac6c'></a>

Springer
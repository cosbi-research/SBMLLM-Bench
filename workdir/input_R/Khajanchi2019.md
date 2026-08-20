<a id='61f2d15d-acff-427b-b59c-ad31addc71aa'></a>

DE GRUYTER

<a id='cb7c5378-ffa3-4f14-809b-6211b7923077'></a>

IJNSNS 2019; 20(3-4): 269–285

<a id='15bc657c-1556-4983-9043-8dad2e36aa92'></a>

Subhas Khajanchi*

Stability Analysis of a Mathematical Model for
Glioma-Immune Interaction under Optimal
Therapy

<a id='87113023-af0c-4eb0-b2cc-cfc3ffb2492f'></a>

https://doi.org/10.1515/ijnsns-2017-0206
Received September 20, 2017; accepted February 20, 2019

<a id='4ab8ca61-d7b8-4718-8ed7-6b771b45901d'></a>

Abstract: We investigate a mathematical model using a system of coupled ordinary differential equations, which describes the interplay of malignant glioma cells, macrophages, glioma specific CD8+T cells and the immunotherapeutic drug Adoptive Cellular Immunotherapy (ACI).
To better understand under what circumstances the glioma cells can be eliminated, we employ the theory of optimal control. We investigate the dynamics of the system by observing biologically feasible equilibrium points and their stability analysis before administration of the external therapy ACI. We solve an optimal control problem with an objective functional which minimizes the glioma cell burden as well as the side effects of the treatment. We characterize our optimal control in terms of the solutions to the optimality system, in which the state system coupled with the adjoint system. Our model simulation demonstrates that the strength of treatment u₁(t) plays an important role to eliminate the glioma cells. Finally, we derive an optimal treatment strategy and then solve it numerically.

<a id='51c6ec7c-7c07-4854-bb3f-3f0801ae60cd'></a>

**Keywords:** malignant gliomas, stability analysis, optimal control, adoptive cellular immunotherapy

<a id='3898f20d-b360-4294-b38e-634286770812'></a>

PACS® (2010). 49J15, 92B05, 92C50, 93C10, 93C15, 93D20

<a id='c609ecfd-5413-4912-a0c5-9b622c322310'></a>

# 1 Introduction

Gliomas are highly diffusive and aggressive brain tumors with the nefarious ability to recur despite extensive medical advances and surgical resection. Gliomas are generally originated from brain resident glial cells or their precursors and accounting for about 50% brain tumors caused by the malignancy of gliomas, and it has life expectancies 6th to 12th months [1]. It is not surprising

<a id='a3703a8a-a814-428b-bdc2-7ba00433dfb5'></a>

*Corresponding author: Subhas Khajanchi, Department of Mathematics, Presidency University, Kolkata 700073, India, E-mail: subhaskhajanchi@gmail.com

<a id='1c880684-9ca9-4f3a-9643-423f103d5cae'></a>

that the researchers around the entire world have been trying to successfully model the malignancy of gliomas. Mathematical modeling is a powerful tool provide realistic and quantitative representations of complicated biological phenomena [2–9], and biological interpretation of their results could provide better insight to make realistic predictions of the state of gliomas under different scenarios [10].

<a id='757da586-a5a0-4567-b29b-39c6466c3948'></a>

According to the World Health Organization (WHO),
the gliomas can be classified into four grades: WHO
grade I-IV. Among them Glioblastoma multiforme (GBM)
WHO grade IV is the most frequent glioma and accounts
for about one half of all primary brain tumors. Due to
their genomic instability, heterogeneity, and infiltrative
behavior in their sequestered location beyond the blood
brain barrier (BBB), malignant gliomas are difficult to
conventional treatments, including gene therapy, immun-
otherapy, chemotherapy, radiation therapy, etc. The most
important thing is this, how our immune system responds
to the progression and development of malignant glioma
cells, which is still an enigma in terms of its establishment
and destruction [11].

<a id='ad2c0be2-7a3a-4948-bf41-40e762647b05'></a>

Glioblastomas use different ways to invade the sur-
rounding normal tissues. One of them is a dramatic
reduction in the expression of major histocompatibility
complex (MHC) molecules on their surface, which weak-
ens their detection by cytotoxic-T-lymphocytes. Glioma
secrete various immunosuppressive factors, like trans-
forming growth factor-ẞ (TGF-β), prostaglandin E2 (PGE2),
interleukin (IL)-10, which can deactivate T-helper cells
(CD4+T), and stimulate the activity of regulatory-T cells
(Tregs) [12]. In the central nervous system (CNS), glioma-
immune system cellular interactions are affected due
to the presence of the selective BBB. Only activated
cytotoxic-T-lymphocytes (CD8+T cells) cross the BBB and
enter into the brain tumor cells [12]. Microglial cells are
the brain resident macrophages, which occupy 15% of the
brain, which can protect our brain from the foreign anti-
gen and eliminate the foreign antibody by phagocytosis
process [2, 9].

<a id='c5b19fb6-cfc1-4d9c-9d22-6c7ccc0a5ee7'></a>

A series of work has been developed to study the
tumor-immune interaction through mathematical model

<!-- PAGE BREAK -->

<a id='f4d382f3-448f-4414-8c06-84e2c4ca4f56'></a>

270

<a id='ef88109d-ce1d-4adc-aef8-c701a5896190'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='dd9ed329-1420-4f6f-8b61-ca5124d40650'></a>

DE GRUYTER

<a id='e150a65f-ef8d-4119-b571-27c0a9a13db8'></a>

[11, 13-23], but few scientists/researchers has been worked on mathematical models to study the prolifer-ation and development and control of malignant glio-blastomas [1, 3-5, 9, 10, 24-27]. In [24], Chakrabarty and Hanson developed a mathematical model for the growth and control of malignant gliomas and applied the theory of optimal control techniques to minimize the cell count of malignant gliomas and reduce the detrimental effects of the drug by using Galerkin finite element method. Kronik et al. [5] considered the interactive dynamics of high grade gliomas and their environment through a sys-tem of coupled nonlinear ordinary differential equations by exogenous administration of immune cells or immun-oregulatory factor alloreactive cytotoxic-T-lymphocytes (aCTL) and they used computer simulations for model verification and retrieving putative treatment scenarios.

<a id='55ee787b-2dec-4306-bd9b-173aa3ea6bc2'></a>

The administration of membrane glycoprotein T11 target structure as a therapeutic agent has been shown to reverse the immune-suppressed state of malignant gliomas by boosting the functional status of immune cells including macrophages and activated CD8+T cells in animals. Modeling this treatment computationally can predict that treatment with T11 target structure can allow effect or cells of the immune system to overcome BBB impermeability and lead to enhanced phagocytic activity and diminishing of malignant gliomas [9]. Iarosz et al. [25] constructed a biologically based mathematical model of brain tumor in which they introduce the interaction between glial cells and neurons using heaviside step function. In their model they used chemotherapeutic treatment to inhibit the proliferation of malignant glioma cells. In [4], Gerlee and Nelander developed a biologically based mathematical model to analyze how the phenotypic switching between proliferative and migratory states of individual cells affect the macroscopic growth of the malignant gliomas. From their model they derive a continuum approximation in the form of two coupled partial differential equations, which demonstrate traveling wave solutions whose speed of invasion depends on the system parameters.

<a id='129a22d4-8fff-44a2-a190-7609bf1b6762'></a>

The main aim of this paper is to investigate the dynamics of glioma-immune interaction through the application of control theory. Several articles have addressed on the applications of control theory for immunotherapy in tumor-immune dynamics [16, 20, 28-36] and glioma-immune dynamics [24]. Fister and Donnelly [36], applied the optimal control theory to obtain under what situations the tumor cells can be eliminated. They investigate that the bang-bang control exists for the linear optimal control problem. In [33], Castiglione and Piccoli developed a mathematical model of the interplay

<a id='89e26a4d-a842-49c0-82ce-190077654b80'></a>

between tumor and their micro-environment, and then they applied the theory of optimal control to obtain when and in which extent the immune system can be stimu- lated by an immunotherapeutic drug during the treatment period in a small time window. In [35], Fister and Panetta used an optimal treatment strategies for the chemothera- peutic treatment administered by using optimal control theory. They investigated the qualitative behavior of three different cell-kill models, both analytically and numeric- ally. In [34], De Pillis et al. studied a mathematical model to understand the dynamics of tumor-immune competit- ive system and applied to chemotherapy to minimize the tumor cells and the cost of the chemotherapeutic drug. The showed the existence of an optimal control theory and solved both the quadratic and linear optimal control. Also, the authors find the region by graphical representations on which the singular control will be optimal. Burden et al. [32] used the theory of optimal control to investig- ate the optimal treatment strategy by external injections of adoptive cellular immunotherapy (ACI) against tumor cell populations. Swan [30] investigated the optimal con- trol theory and established feedback treatment control and the characterization of drugs for tumor models under the hypothesis of quadratic control performance criteria. J. M. Murray [28] considered a mathematical model for normal and tumor cells under the conjectures of logistic growth and Gompertzian growth function, in which the rate of administration of therapies has been controlled. At the end of the treatment, he showed that the tumor bur- den is minimized, in different implementation, the level of toxicity, interpreted as the area under the concentra- tion curve. Khajanchi and Ghosh [16] used optimal control technique with combined effects of the drugs in a tumor- immune interaction model which is originally developed by Kuznetsov et al. [17]. They characterized the optimal- ity system and investigate the uniqueness of the optimal controls.

<a id='4871ff71-ece6-4951-9c40-4120b8a8c471'></a>

In this article, we propose a biologically based math-
ematical model using a system of coupled nonlinear
ordinary differential equations for the growth and control
of malignant glioma cells, where the glioma cells attack
the macrophages [9, 25]. In our model, we consider inter-
action among malignant glioma cells, macrophages and
the glioma specific CD8+T cells. The main thrust of this
paper is to introduce the dynamic relationship between
glioma cells and macrophages. The special attention is
paid to the local asymptotic stability of the total annihila-
tion of the glioma cells, as well as the case of interior equi-
librium point under which the tumor cannot be elimin-
ated. This will provide a clearer idea to design better treat-
ment strategies or improve existing policies to eradicate

<!-- PAGE BREAK -->

<a id='d9541b3b-7691-4110-a6a1-755dcf7319ea'></a>

DE GRUYTER

<a id='ccbafc48-c8b6-48d1-b623-95573ad5fd80'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='7d9ed722-0893-4ade-9a53-cd970bd65240'></a>

271

<a id='72213d1f-f446-4afd-b64b-30e30e4332da'></a>

the brain tumor or at least to improve the patients' quality
of life which is the main goal of this paper.

<a id='18f422ee-73f0-4896-a615-4dd5aa9c70ff'></a>

The outline of this paper is as follows. After this introduction, Section 2 dwells on the formulation of the mathematical model and its non-dimensional form. Section 3 is devoted to the basic properties of the mathematical model including positivity and boundedness of the model. In the same section, we provide the biologically feasible singular points and their stability analysis. The optimal control problem is proposed in Section 4. We seek to minimize the glioma cell burden and the cost of effectiveness. We characterize the optimal control using Pontryagin's maximum principle. In the same section, we solve the resulting optimality system. The system thus obtained, being highly nonlinear in nature is then solved by numerical simulations, which has been discussed with proper biological justifications in Section 5. Finally, our paper ends with a brief discussion with clinical implications.

<a id='97596f12-70d4-4794-a978-3486562f5678'></a>

## 2 The mathematical model

The main aim of this mathematical model is to allow suffi-cient complexity so that the model will qualitatively gen-erate clinically observed gliomas growth pattern, while it simultaneously maintains sufficient simplicity to admit the model analysis. By singling out the vital forces in the system and deliberately ignoring secondary effects, the analytical power of the model is importantly sharpened. Our mathematical model focuses on the main interplay among the malignant glioma cells, macrophages and glioma-specific CD8+T cells. The mathematical expres-sions we have chosen for describing the model conform with standards of mathematical immunology set by works such as references [5, 9, 17, 25]. Our mathematical model describing the proliferation, decay, and interactions of these cells is:

<a id='25171928-24c1-41e7-bf87-cd43939668fc'></a>

dG(t) / dt = r₁G(t) (1 - G(t) / G₁)

- (ā₁M(t) + ā₂T₈(t))G(t) / (G(t) + k₁)

dM(t) / dt = r₂M(t) (1 - M(t) / M₁) - α₃ G(t)M(t) / (G(t) + k₂)

dT₈(t) / dt = γ₁G(t)T₈(t) / (k₃ + G(t)) - μ₁T₈(t) - α₄ G(t)T₈(t) / (G(t) + k₄) (1)

where G(t) represents the density of malignant glioma
cells, M(t) represents the density of macrophages and
T₈(t) designates the density of the glioma specific CD8+T

<a id='0cf3d376-b6f2-44b5-add2-22a5a1a00334'></a>

cells at time $t$. The first term on the right-hand side of the first equation of (1) designates the proliferation of glioma cells. We assume that the glioma cells can grow logistically without any immune intervention, where $G_1$ designates the maximum carrying capacity and $r_1$ is the intrinsic growth rate. The second term represents the elimination of glioma cells due to interaction with glioma specific CD8+T cells $T_8(t)$ and macrophages $M(t)$, with saturation for large $G(t)$. The saturation is represented by a linear denominator with the parameter $\bar{k}_1$ standing for the accessibility of the glioma cell population. The rates $\bar{a}_1$ and $\bar{a}_2$ designates the elimination of malignant gliomas by macrophages and glioma specific CD8+T cells, respectively.

<a id='4b88463a-aab6-4656-bf4f-95535d83482e'></a>

The term dM(t)/dt in eq. (1) represents the rate of change of macrophages at any time t. The first term represents the proliferation of macrophages. We assume that macrophages can grow logistically with intrinsic growth rate r₂ and M₁ is the maximum carrying capacity. The second term corresponds to the deactivation of macrophages, which is represented by Michaelis–Menten saturation dynamics to indicate the limited interaction between gliomas and macrophages. α₃ represents the rate at which the macrophages are eliminated by glioma cells.

<a id='75a18d88-d83d-44a4-9aa0-bf2a1abcc001'></a>

The third equation of the system eq. (1) represents the rate of change for glioma specific cytotoxic-T-lymphocytes. The activated glioma specific CD8+T cells recruited by malignant glioma cells. The term $\frac{\gamma_1 G(t)T_8(t)}{k_3+G(t)}$ is of Michaelis-Menten form to represent the saturated effects of glioma specific CD8+T cells, where $\gamma_1$ is the recruitment rate and $\bar{k}_3$ represents the half saturation constant. $\mu_1$ is the natural death rate of glioma specific CD8+T cells due to inflammatory reaction in the brain. The term $\alpha_4 \frac{G(t)T_8(t)}{G(t)+\bar{k}_4}$ corresponds to the elimination of glioma specific cytotoxic-T-lymphocytes by malignant glioma cells at the rate $\alpha_4$, $\bar{k}_4$ being the Michaelis-Menten constant.

<a id='f4a761fb-98cb-40a4-be9d-bb4dc552d268'></a>

To non-dimensionalize the model system eq. (1), we introduce new variables as follows:

<a id='7868b164-0eef-4467-ab27-c4f55efa3d2e'></a>

u(t) = G(t) / G₁,
v(t) = M(t) / M₁,
w(t) = T₈(t) / k₃

<a id='0743c3b7-1149-492b-a028-860516d4a3f9'></a>

then the model system (1) leads to the following form:

$\frac{du(t)}{dt} = r_1 u(t)(1 - u(t)) - \frac{(\alpha_1 v(t) + \alpha_2 w(t))}{u(t) + k_1} u(t),$

$\frac{dv(t)}{dt} = r_2 v(t)(1 - v(t)) - \alpha_3 \frac{u(t)v(t)}{u(t) + k_2},$

$\frac{dw(t)}{dt} = \frac{\gamma_1 u(t)w(t)}{k_3 + u(t)} - \mu_1 w(t) - \alpha_4 \frac{u(t)w(t)}{u(t) + k_4} \quad (2)$

<!-- PAGE BREAK -->

<a id='f894dc57-530b-40b6-8142-8085a063756d'></a>

272

<a id='1fc3e7a5-648d-479b-8fd5-d01df19fa3ef'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='a687eaec-9115-475f-aa13-29e94ea9d15e'></a>

DE GRUYTER

<a id='d81d8083-8de4-436f-bd3b-126d5a8041ac'></a>

where

$\alpha_1 = \frac{\bar{a}_1M_1}{G_1}$, $\alpha_2 = \frac{\bar{a}_2k_3}{G_1}$, $k_1 = \frac{k_1}{G_1}$,

$k_2 = \frac{\bar{k}_2}{G_1}$, $k_3 = \frac{\bar{k}_3}{G_1}$, $k_4 = \frac{\bar{k}_4}{G_1}$,

with the positive initial conditions:

$u(0) \geq 0$, $v(0) \geq 0$, $w(0) \geq 0$. (3)

<a id='06e264e6-dba5-4663-bb01-364080df54da'></a>

## 3 Basic properties of the model

In this section, we shall investigate the important proper-
ties (positivity and boundedness of the system (2)) of the
solutions to the model system (2) with nonnegative initial
values (3).

<a id='e8d3f26e-110c-47d8-85a6-4729bca7fb82'></a>

**Theorem 3.1.** _All the solutions for the system (2) with positive initial values remain positive._

<a id='8a6ef56b-27bc-4de7-bf4b-8c20ec34ddd4'></a>

Proof. The right hand side of the first equation of (2) is a continuous functions of dependent variables, we obtain after the integration

$u(t) = u(0) \exp\left(\int_{0}^{t} \left[r_{1}(1-u(s)) - \frac{(\alpha_{1}v(s) + \alpha_{2}w(s))}{k_{1} + u(s)}\right]ds\right).$

<a id='360dfa78-ab7d-4fde-913f-4d892c8a19b1'></a>

In similar way, we obtain from the second and third
equations of (2), we get

$v(t) = v(0) \exp \left( \int_0^t \left[ r_2(1-v(s)) - \frac{\alpha_3 u(s)}{k_2 + u(s)} \right] ds \right)$

and

<a id='409026b9-071d-4cd5-994c-89086cbc32db'></a>

<::transcription of the content
: $w(t) = w(0) \exp\left(\int_0^t \left[\frac{\gamma_1 u(s)}{k_3 + u(s)} - \mu_1 - \frac{\alpha_4 u(s)}{k_4 + u(s)}\right] ds\right).$::>

<a id='71d9442f-6b32-4261-8241-02a1dd0f3cfc'></a>

Therefore, it is clear from the above expressions that u(t),
v(t) and w(t) remain positive for all t > 0, if they initiate
from an interior point of:

<a id='7d370249-666e-409c-a17c-c80f8f53c035'></a>

R³₊ = {u(t), v(t), w(t) : u(t) > 0, v(t) > 0, w(t) > 0}.

<a id='e4182e7f-3bb2-4f26-86f7-a237c3250464'></a>

Thus, **R**³ is positively invariant for the model system (2). □

<a id='eda4b700-ed3e-4e9a-afdc-2b2e360af109'></a>

By using the positivity of the system (2), we now prove that our system is dissipative, that is, there exists a compact region in the positive quadrant **R** such that all the solutions initiating in **R** remain within **R**, and all solutions initiating outside **R** in the positive quadrant enter it in for all future time.

<a id='66139603-0388-4d83-9397-c0a864401317'></a>

**Theorem 3.2.** *The model system (2) is dissipative.*

**Proof.** Using the nonnegativity of state variables, we obtain from the first and second equations of (2):

du(t)
--- = r₁u(t)(1 - u(t)),
dt
dv(t)
--- = r₂v(t)(1 - v(t)).
dt

<a id='98ec8af3-3e6f-4eb9-a2a2-d3a21076ac3e'></a>

Using the standard comparison theory for differential inequalities, it follows that:

$\bar{u}(t) = \limsup_{t\to+\infty} u(t) \leq 1$,

$\bar{v}(t) = \limsup_{t\to+\infty} v(t) \leq 1$.

<a id='e7dc7622-3b56-46d2-84d1-fee903f7e813'></a>

Since μ₁ > 0, from the third equation of (2), it follows that
dw(t)
---
 dt ≤ γ₁ū(t)w(t) - μ₁w(t),

<a id='ec1f4c58-519b-47dc-a60f-73e97d67ce24'></a>

which implies that

w̄(t) = lim sup w(t) ≤ 0, if γ₁ū(t) < μ₁.
       t→+∞

<a id='25f49e61-6c1f-444a-a72d-2977d514758a'></a>

Therefore, the region

**R** = {(u(t), v(t), w(t)) ∈ **R**³₊
: 0 ≤ u(t) ≤ 1, 0 ≤ v(t) ≤ 1, w(t) ≥ 0},

<a id='78ac84fc-8dc4-45a4-9faa-513a436c6417'></a>

is an attracting region, showing the property.
option : [ ]

<a id='4ddb43c1-5612-45c2-b8b1-c0629f2c739e'></a>

## 3.1 Existence of singular points and local stability analysis

Our interest of this section is to find the biologically feasible singular points and their stability of the system of eq. (2). The study of local stability analysis is too important to verify if the suppression of glioma cells is stable asymptotically or not, or to understand whether a less important singular point is stable asymptotically or not.

<!-- PAGE BREAK -->

<a id='ce9bf73f-0916-4947-87a5-50c7b822d214'></a>

DE GRUYTER

<a id='3529e5d8-2132-4921-a6b1-a2ff1d851ee4'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='2c1f5c55-3d5a-4f2a-bde9-1a5342e650f9'></a>

273

<a id='d6cd993e-46da-419a-9564-6edaf6d7068d'></a>

**3.1.1 Equilibria and their local stability analysis**
The local stability of the system (2) around each of the singular points is determined by the eigenvalues λᵢ (i = 1, 2, 3) of the variational matrix:

<a id='2cbdfeab-9893-49ff-a492-786df81b5462'></a>

```
J_E = 
	[
		A_11				-a_1u / (k_1+u)			-a_2u / (k_1+u)
		a_3k_2v / (k_2+u)^2		A_22					0
		gamma_1k_3w / (k_3+u)^2 - a_4k_4w / (k_4+u)^2	0					A_33
	]
```

<a id='8dad6043-be7a-404e-bcea-0bc5a4edb70c'></a>

where
A11 = r1(1 - u) - (α1v + α2W) / (k1 + u) - r1u + (α1v + α2)u / (k1 + u)^2 ,
A22 = r2(1 - v) - α3u / (k2 + u) - r2v,
A33 = γ1u / (k3 + u) - μ1 - α4u / (k4 + u) .

<a id='f9112a02-bc4e-4519-9f09-23c2624b50f6'></a>

The conditions for the existence of equilibrium points
and their stability analysis are discussed below.

(i) For any set of parameters, the system (2) has an
"extinct" equilibrium point E₀(0, 0, 0), in which all
the three cell populations are extincted. The cor-
responding eigenvalues associated with this equi-
librium point E₀ are λ₁ = r₁ > 0, λ₂ = r₂ > 0
and λ₃ = -μ₁ < 0. Therefore, E₀ is a saddle point
with a one-dimensional stable manifold along u-axis
and two-dimensional unstable manifold in the u - v
plane. Thus, there is no initial values exterior the
first quadrant which can converge to E₀.

(ii) The singular point E₁(1, 0, 0) is a point of the sys-
tem (2) where only glioma (tumor) cells present.
This equilibrium point E₁ is located in the posit-
ive quadrant. The eigenvalues associated with this
equilibrium point E₁ are

<a id='74a3ead2-9e0a-41ed-9b00-0deb9ea829c1'></a>

$$\begin{cases}\lambda_1 = -r_1 < 0,\\ \lambda_2 = r_2 - \frac{\alpha_3}{k_{2+1}},\\ \lambda_3 = \frac{\gamma_1}{k_{3+1}} - \mu_1 - \frac{\alpha_4}{k_{4+1}}.\end{cases}$$

<a id='6f6ce098-3f1e-4ec3-a70f-671055efc674'></a>

The singular point $E_1$ is locally asymptotically stable if the following condition holds:

<a id='979f87ca-66aa-46f3-b818-69941b45bd42'></a>

<::
$$
\begin{cases}
r_2 < \frac{\alpha_3}{k_2+1}, \\
\gamma_1 < (k_3 + 1) \left[\mu_1 + \frac{\alpha_4}{k_4+1}\right].
\end{cases}
$$
: figure::>

<a id='f094c897-9259-437a-90f6-72397b019fbb'></a>

The equilibrium point E₁ has a deleterious effect for the patient since only glioma cells present in the

<a id='ea305d3b-7604-4c38-a580-330943ced5c8'></a>

corresponding site. The singular point E₁ is a stable node when the above two conditions are satisfied.
The first one implies that the proliferation rate of macrophages r₂ must be less than the deactivation rates of macrophages by glioma cells in presence of half saturation constant k2. The second one is related to the immune system and can be regarded as a condition for gliomas immune evasion [37].
The glioma free singular point E₂(0, 1, 0) is a point of the system (2) where only macrophages present. This singular point E₂ is located in the positive quadrant.
The eigenvalues associated with this singular point Es are as follows

<a id='9f296f2d-fbf9-4c19-aacf-9709c9a87471'></a>

<::
λ₁ = r₁ - α₁/k₁,
λ₂ = -r₂ < 0,
λ₃ = -μ₁ < 0.
: equation::>

<a id='575f3747-368f-47fc-b21c-c53fca177881'></a>

The glioma free singular point $E_2$ is locally asymptotically stable if $r_1 < \frac{\alpha_1}{k_1}$, otherwise the equilibrium point is a saddle point. The condition implies that the proliferation rate of gliomas $r_1$ must be less than the deactivation rate of glioma cells by macrophages in presence of half saturation constant $k_1$. Note that, when the parameter values are such as the glioma-free equilibrium is a point attractor, there no longer exists a possibility of a sustained glioma growth, the microenvironment is not conducive to the growth of glioma cells.

<a id='30fa49ec-954f-4094-9f2c-4aaeadb2ba04'></a>

(iv) The singular point Ẽ(ũ, ṽ, 0) corresponds to a scen-
ario where glioma cells and macrophages coexist.
The CD8+T cells free singular point Ẽ whose coordin-
ates are

<a id='30e5c801-556d-4759-bdfc-7ce82de9a4a8'></a>

| v = r_1/a_1 (1 - ũ)(k_1 + ũ),
ũ = 0,

<a id='5ac9b6a9-276c-4de4-b3a5-a587e1a57a3e'></a>

where the glioma cells \(\tilde{u}\) is obtained by the solution
of the cubic equation

\(f(u) = q_0\tilde{u}^3 + q_1\tilde{u}^2 + q_2\tilde{u} + q_3, \quad (4)\)

<a id='ed5b7ba1-8129-4bc0-9090-9122ae375c63'></a>

with

<a id='9da541c2-eb1c-45e8-9be4-40f1484c8f22'></a>

q_0 = r_1 r_2 > 0,
q_1 = (k_1 + k_2 - 1)r_1 r_2,
q_2 = r_1 r_2 k_1 k_2 + \alpha_1 r_2 - r_1 r_2 k_1 - r_1 r_2 k_2 - \alpha_1 \alpha_3,
q_3 = r_2 k_2 (\alpha_1 - r_1 k_1).

<a id='857447c9-65b9-47f6-988b-c3bb3c62e04b'></a>

(iii)

<!-- PAGE BREAK -->

<a id='9dda891a-cd74-429b-a128-e5f25489d266'></a>

274

<a id='2af63671-745b-49cd-bddb-6325b15efd79'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='d9710e96-9193-4801-9d9c-d23c661a199b'></a>

DE GRUYTER

<a id='92434bbb-09ca-417a-be80-beb6a7ece7d3'></a>

It can be observed from Figure 1 that the cubic eq. (4)
has exactly one positive root of ũ. Thus, the glioma-
macrophages singular point Ẽ has a unique positive
root. The eigenvalues associated with this singular
point Ẽ are

<a id='62b9e84b-31bc-4f67-ad76-64c725d559fc'></a>

\lambda_1 = \frac{\gamma_1\tilde{u}}{k_3 + \tilde{u}} - \mu_1 - \frac{\alpha_4\tilde{u}}{k_4 + \tilde{u}}

<a id='d09eedd4-7ee7-4665-9491-7c94a5d2fc6b'></a>

and the two other eigenvalues (λ₂, λ₃) are the roots of
the following characteristic equation

<a id='e9b19890-3820-49d9-aed8-7a2aa0ae13ca'></a>

λ² + ρ₁₁λ + ρ₁₂ = 0,

<a id='c47e08b8-ae45-4b40-b143-b9ab68f94f7e'></a>

where

$$\begin{cases}
\rho_{11} = r_1\tilde{u} + r_2\tilde{v} - \frac{\alpha_1\tilde{u}\tilde{v}}{(k_1+\tilde{u})^2}, \\
\rho_{12} = r_2\tilde{u}\tilde{v} \left[r_1 - \frac{\alpha_1\tilde{v}}{(k_1+\tilde{u})^2}\right] - \frac{\alpha_1\alpha_3k_2\tilde{u}\tilde{v}}{(k_1+\tilde{u})(k_2+\tilde{u})^2}
\end{cases}$$

<a id='850b823e-0297-44c2-8c55-a9dc5d640cb7'></a>

The solutions of the above characteristic equation are real negative or complex conjugate with negative real parts if ρ₁₁ > 0 and ρ₁₂ > 0. This could corresponds to a situation according which the immune response remains efficient against malignant gliomas. If not, there is a glioma immune evasion. The singular point Ẽ is locally asymptotically stable if the following conditions hold

<a id='453e3e33-300a-4b1d-9393-d23103e35f89'></a>

γ₁ < (k₃/ū + 1) [μ₁ + α₄ū / (k₃+ū)],

α₁ < (r₁/v + r₂/ū) (k₁ + ū)²,

α₃ < r₂(k₁+ū)(k₂+ū)² / (α₁k₃) [r₁ - α₁v / (k₁+ū)²].

<a id='959f1340-25c8-428a-8275-3b439c1723b9'></a>

The equilibrium point Ẽ is thus stable if the above conditions hold. From the biological point of view, the undesirable singular point Ẽ has limited interest to the clinicians as the gliomas are always survive in this singular point.

<a id='92c5e7d3-1393-40da-8c24-81e2b747d53a'></a>

<::2D line plot::>A 2D line plot showing a cubic polynomial function f(u). The x-axis ranges from approximately -0.5 to 1.2, with major tick marks at -0.5, 0.5, and 1.0. The y-axis ranges from approximately -0.06 to 0.12, with major tick marks at -0.05, 0.05, and 0.10. The curve starts at y > 0 for x = -0.5, decreases, crosses the x-axis around x = 0.05, reaches a local minimum around x = 0.75, then increases sharply, crossing the x-axis again around x = 0.9 and continuing to increase. The function is labeled 'f(u)' in the upper right quadrant. Figure 1: Nonnegative root(s) of the cubic polynomial (4). The parameter values are specified in Table 1.<::

<a id='da348cc4-cb22-475f-8f75-686bcd4f884a'></a>

(v) The singular point $\overline{E}(\overline{u}, 0, \overline{w})$

$$\overline{E} = \begin{cases}
\overline{u}, \\
0, \\
\overline{w} = \frac{r_1}{\alpha_2}(1 - \overline{u})(k_1 + \overline{u}),
\end{cases}$$

<a id='86efcfea-262e-46b4-9e18-002cb05c5efb'></a>

is such that the glioma cells coexist with activated
CD8+T cells. The first coordinate ū is the nonnegative
root(s) of the quadratic equation

<a id='0e8b75af-d47d-4eea-9551-9b336cf9aa61'></a>

h(u) = ū² (μ₁ + α₄ – γ₁) + ū(k₄μ₁ + k₃μ₁
+ α₄k₃ – γ₁k₄) + k₃k₄μ₁,
(5)

<a id='2cff0c21-1ace-4c95-930e-ae9cb18006ea'></a>

which can be written as

$\bar{u} = \frac{1}{2(\mu_1 + \alpha_4 - \gamma_1)} [-\Theta \pm \sqrt{\Theta^2 - 4(\mu_1 + \alpha_4 - \gamma_1)k_3k_4\mu_1}],$

where $\Theta = k_4\mu_1 + k_3\mu_1 + \alpha_4k_3 - \gamma_1k_4.$

<a id='141302a8-2bae-4800-9441-54414bf07b8e'></a>

Now, for the existence of positive roots of ū we
consider the following cases:

<a id='4ce3b1a9-c65e-4ced-8326-38ace28761ac'></a>

Case 1. If

<a id='7ad839a4-d44b-4321-958d-634df7bf914f'></a>

$\gamma_1 > \mu_1 + \alpha_4,$

<a id='b142cac0-4b8c-4458-9f5a-1fc61b584679'></a>

then the quadratic eq. (5) has a unique positive root.

<a id='16f3b512-f795-4c9c-9b7c-e8f1f743636b'></a>

**Case 2.** The necessary and sufficient conditions for eq. (5) to have two positive roots are

<a id='45657278-da63-43e7-b73d-5b3e52454769'></a>

γ₁ > μ₁ + k₃(μ₁ + α₄) / k₄,
γ₁ < (μ₁ + α₄) < (k₄μ₁ + k₃μ₁ + α₄k₃ - γ₁k₄)² / (4k₃k₄μ₁).

<a id='f517cd91-9328-41b7-8ef3-696caaecaded'></a>

For the above two cases the quadratic eq. (5) will
have positive root(s) when the glioma cells and activ-
ated CD8+T cells coexists. This singular point E is
located in the positive quadrant. It can be noticed
from Figure 2, that the quadratic polynomial eq. (5)
has exactly one positive root of u. The eigenvalues
associated with this equilibrium point E are

<a id='269fe7df-acb9-43a0-9398-bcfb1752327c'></a>

\lambda_1 = r_2 - \frac{\alpha_3\bar{u}}{k_2 + \bar{u}}

<a id='61ff3d46-9e87-4c17-88a6-5558dd3a88a1'></a>

the two other eigenvalues ($\\lambda_2$, $\\lambda_3$) being the solutions
of the quadratic equation

$\\lambda^2 + \\rho_{11}\\lambda + \\rho_{12} = 0,$

<!-- PAGE BREAK -->

<a id='e7367e5c-4e17-41a5-9c52-e52b7201a53e'></a>

DE GRUYTER

<a id='71b8106d-8652-4293-9879-c825a7da413e'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='315bce28-e44a-402e-bc9a-eb80b6caaf3d'></a>

275

<a id='653fcf31-b17b-4e9d-b23e-812e42f4b64c'></a>

<::line graph: The graph shows a blue curve representing h(u) as a function of u. The x-axis (u) ranges from approximately -0.4 to 0.7, with major ticks at -0.4, -0.2, 0.2, 0.4, and 0.6. The y-axis (h(u)) ranges from approximately -0.022 to 0.012, with major ticks at -0.020, -0.015, -0.010, -0.005, 0.005, and 0.010. The curve starts below the x-axis, crosses the x-axis around u = -0.2, reaches a peak around u = 0.15 with a value slightly below 0.010, crosses the x-axis again around u = 0.45, and then decreases below the x-axis. The label "h (u)" is placed near the peak of the curve. Figure 2: Nonnegative root(s) of the biquadratic polynomial (5). The parameter values are specified in Table 1.::>

<a id='ecc34fa3-5b52-4ade-a3c3-ea9f3a6b7359'></a>

where

{
ρ₁₁ = r₁ū - α₂uw̄ / (k₁+ū)² ,
ρ₁₂ = α₂ū / (k₁+ū) [ γ₁k₃w̄ / (k₃+ū)² - α₄k₄w̄ / (k₄+ū)² ] .


<a id='e8da9ef5-5eb6-4394-b3e1-3b38ac335e8d'></a>

Solutions of the above equation are real negative or complex conjugate with negative real parts if ρ11 > 0 and ρ12 > 0. This could corresponds to a situation according which the immune response remains efficient against malignant gliomas. If not, there is a glioma immune evasion. The singular point Ē is locally asymptotically stable if the following conditions hold

<a id='a4fd99d6-3b96-4bd9-ae5f-a4ca6d3b5ce8'></a>

$\alpha_3 > r_2(1 + \frac{k_2}{u})$

$\quad r_1 > \frac{\alpha_2\bar{w}}{(k_1 + \bar{u})^2}$

$\quad \gamma_1 > \frac{\alpha_4k_4}{k_3} (\frac{k_3 + \bar{u}}{k_4 + \bar{u}})^2$

<a id='8cc80987-6e74-48c6-bc30-975cfd21b0bd'></a>

The equilibrium point $\bar{E}$ is thus stable when (i) the macrophage tissue provides strong barrier against malignant gliomas progression (first condition), (ii) a deleterious effect for the patient since the immune system is not very efficient against gliomas (second condition) and (iii) the proliferation of activated CD8+T cells $\gamma_1$ must be greater than the fraction of the glioma cells in presence of the others nonnegat- ive parameters.

<a id='9256e414-7eef-46fc-aac8-216a890f0975'></a>

(vi) The singular point E*(u*, v*, w*)

E* =
  u*,
  v* = r2(k2+u*)-a3u* / r2(k2+u*),
  w* = r1r2(1-u*)(k1+u*)(k2+u*)-a1r2(k2+u*)+a1a3u* / r2a2(k2+u*)

<a id='8892c538-6cfb-488b-a108-11ef1b2d8b40'></a>

corresponds to a state where all the three cells, namely glioma cells, macrophages and activated CD8+T cells coexist. The first coordinate u* is the nonnegative root(s) of the quadratic eq. (5). We recover three conditions for the existence of other two singular points v*, w*, which can be expressed as

<a id='ae15a4ef-b796-45f6-ab8e-ede36225e336'></a>

| $r_2 > \frac{\alpha_3 u^*}{k_2+u^*}$,
| $u^* < 1$,
| $\frac{r_1(1-u^*)(k_1+u^*)}{\alpha_1} + \frac{\alpha_3 u^*}{r_2(k_2+u^*)} > 1$

<a id='322006e2-1d97-469b-845b-9dacc1669fb7'></a>

which implies, macrophages tissue of the gliomas
micro-environment presenting sufficiently strong
barrier against gliomas progression (first condition),
the tumor mass always less than a unity (second con-
dition), and the sum of the fraction of glioma cells
with other nonnegative parameter values are greater
than a unity (third condition). The variational matrix
calculated at the interior singular point E* is given
by

<a id='0d533a00-5c34-4138-9059-97cdef572733'></a>

JE* = (
  -r₁u* + (a₁v*+a₂w*)u* / (k₁+u*)² - a₁u* / k₁+u* - a₂u* / k₁+u*   -r₂v*   0
  -a₃k₂v* / (k₂+u*)²                                                    0
  γ₁k₃w* / (k₃+u*)² - a₄k₄w* / (k₄+u*)²                                   0       0
)

<a id='8b19ba5d-9d09-486b-9b43-de0a40c5eb07'></a>

The characteristic equation for the interior sin-gular point E* can be expressed as

<a id='eb708b70-0774-4903-82ee-0ecf2b2d5dd7'></a>

λ³ + χ₁₁λ² + χ₁₂λ + χ₁₃ = 0, (6)

<a id='9d970eed-2b9f-4bba-9d98-a56e06786bb9'></a>

where
X₁₁ = r₁u* + r₂v* - (α₁v* + α₂w*)u* / (k₁ + u*)²
X₁₂ = r₁r₂u*v* + α₂u*w* / (k₁ + u*) [ γ₁k₃ / (k₃ + u*)² - α₄k₄ / (k₄ + u*)² ] - u*v* / (k₁ + u*) [ α₁α₃k₂ / (k₂ + u*)² + r₂(α₁v* + α₂w*) / (k₁ + u*) ] ,
X₁₃ = r₂α₂u*v*w* / (k₁ + u*) [ γ₁k₃ / (k₃ + u*)² - α₄k₄ / (k₄ + u*)² ] .

<a id='bc71d60a-ead3-42e9-b02d-c1f415a20fd6'></a>

The roots of the characteristics eq. (6) are either real negative or have negative real parts if it satisfies the well known Routh-Hurwitz criterion χ₁₁ > 0, χ₁₃ > 0 and χ₁₁χ₁₂ - χ₁₃ > 0, where

<!-- PAGE BREAK -->

<a id='0663b624-d256-42e6-9f8f-e24047604eb0'></a>

276

<a id='c53d42ca-c38c-4df7-af46-e94eee92edaf'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='9d29eaad-93a7-4f9e-8616-d64791d6697e'></a>

DE GRUYTER

<a id='f6df2d7c-3ab4-4db8-af08-72874969e0c5'></a>

\chi_{11}\chi_{12} - \chi_{13}\n= (r_1 u^* + r_2 v^*)r_1 r_2 u^* v^* - \frac{(r_1 u^* + r_2 v^*)u^* v^*}{k_1 + u^*}\n\times \left[ \frac{\alpha_1 \alpha_3 k_2}{(k_2 + u^*)^2} + \frac{r_2 (\alpha_1 v^* + \alpha_2 w^*)}{k_1 + u^*} \right]\n+ \frac{r_1 \alpha_2 w^* u^{*2}}{k_1 + u^*} \left[ \frac{\gamma_1 k_3}{(k_3 + u^*)^2} - \frac{\alpha_4 k_4}{(k_4 + u^*)^2} \right]\n- \frac{(\alpha_1 v^* + \alpha_2 w^*)u^{*2}}{(k_1 + u^*)^2} \left[ r_1 r_2 v^* \right]\n+ \frac{1}{k_1 + u^*} \left\{ \frac{\alpha_2 \gamma_1 k_3 w^*}{(k_3 + u^*)^2} - \frac{\alpha_1 \alpha_3 k_2 v^*}{(k_2 + u^*)^2}\n- \frac{\alpha_2 \alpha_4 k_4 w^*}{(k_4 + u^*)^2} - \frac{r_2 (\alpha_1 v^* + \alpha_2 w^*)v^*}{(k_1 + u^*)^2} \right\}.

<a id='c1cac316-07a1-421a-8489-30a5ae113c6f'></a>

The singular point E*(u*, v*, w*) is thus locally asymptotically stable if

<a id='2f1ae6ac-acb7-45cd-b877-2d911987ce3e'></a>

$\begin{cases}
\alpha_1v^* + \alpha_2w^* < (r_1 + r_2\frac{v^*}{u^*}) (k_1 + u^*)^2,\\
\frac{\gamma_1}{\alpha_4} > \frac{k_4}{k_3} (\frac{k_3+u^*}{k_4+u^*})^2,\\
\chi_{11}\chi_{12} - \chi_{13} > 0.
\end{cases}$

<a id='0713c7a0-a3a9-4f90-8fd0-c275cbdb782e'></a>

From an analytical expression of the conditions for a stability of interior equilibrium point is too difficult to be investigated here. We will thus perform them through numerical simulations using the parameter values specified in Table 1.

<a id='956eb25d-54ec-4f93-b573-8f18aebccb14'></a>

# 4 The optimal control problem

In this section, we introduce optimal control problem for the model system (2) by keeping biomedical goals in our mind. The main goal is to study and analyze the effects of a controlled treatment (considering adoptive cellular immunotherapy (ACI) (u₁(t))) on the dynamics for the model. I would like to maximize the number of macrophages and tumor-specific CD8+T cells and minimize the number of glioma cells and the cost of the control. Our control is a function u₁(t) representing the percentage of immunotherapeutic drug ACI. The control u₁(t) is a class of piecewise continuous functions defined for all t > 0 in such a way that 0 ≤ u₁(t) ≤ 1 where u₁(t) = 1 indicates the totally effective immunotherapy whereas u₁(t) = 0 describes no treatment. We describe the class of admissible control as

<a id='07a95e26-8e36-45af-8b7c-c6814bbd2100'></a>

Table 1: Parameters for glioma-immune model: their description
and sources.
<table id="7-1">
<tr><td id="7-2">Parameter</td><td id="7-3">Description</td><td id="7-4">Value</td><td id="7-5">Source</td></tr>
<tr><td id="7-6">r₁</td><td id="7-7">proliferation rate of glioma cells</td><td id="7-8">0.4822</td><td id="7-9">[18, 40]</td></tr>
<tr><td id="7-a">α₁</td><td id="7-b">decay rate of gliomas due to macrophages</td><td id="7-c">0.069943</td><td id="7-d">[9]</td></tr>
<tr><td id="7-e">α₂</td><td id="7-f">decay rate of gliomas due to CD8+T cells</td><td id="7-g">2.74492</td><td id="7-h">[9]</td></tr>
<tr><td id="7-i">k₁</td><td id="7-j">steepness coefficient of glioma cells</td><td id="7-k">0.90305</td><td id="7-l">[5]</td></tr>
<tr><td id="7-m">r₂</td><td id="7-n">growth rate of macrophages</td><td id="7-o">0.3307</td><td id="7-p">[9]</td></tr>
<tr><td id="7-q">α₃</td><td id="7-r">loss of macrophages due to malignant gliomas</td><td id="7-s">0.0194</td><td id="7-t">[9]</td></tr>
<tr><td id="7-u">k₂</td><td id="7-v">steepness coefficient of macrophages</td><td id="7-w">0.030584</td><td id="7-x">[5]</td></tr>
<tr><td id="7-y">γ₁</td><td id="7-z">recruitment of activated CD8+T cells by glioma cells</td><td id="7-A">0.1245</td><td id="7-B">[17]</td></tr>
<tr><td id="7-C">k₃</td><td id="7-D">maximum recruitment of CD8+T cells by glioma cells</td><td id="7-E">2.8743</td><td id="7-F">[17]</td></tr>
<tr><td id="7-G">μ1</td><td id="7-H">natural death rate of CD8+T cells</td><td id="7-I">0.0074</td><td id="7-J">[9]</td></tr>
<tr><td id="7-K">α4</td><td id="7-L">deactivation rate of CD8+T cells by glioma cells</td><td id="7-M">0.01694</td><td id="7-N">[5]</td></tr>
<tr><td id="7-O">K4</td><td id="7-P">Michaelis-Menten constant</td><td id="7-Q">0.378918</td><td id="7-R">[5]</td></tr>
</table>

<a id='21b08dc2-cd0b-46ca-b2e2-f51f0ff3cbdb'></a>

C = {u₁(t) piecewise continuous function :
0 \u2264 u₁(t) \u2264 1, \u2200 t\u2208 [0, T]}.

<a id='0eccecec-6b83-4991-9cb9-4e8c22a36d04'></a>

We define the objective functional as

<a id='d069ab83-5877-4b76-9185-f4680997b97a'></a>

$$J[u_1] = \int_0^T \left[ v(t) + w(t) - u(t) - \frac{1}{2} D_g u_1^2(t) \right] dt, \quad (7)$$

<a id='3d8a3c10-fc94-4b50-ac65-ed90d476d065'></a>

subject to the state system

_du(t)_ = r₁u(t)(1 - u(t)) - (_α₁v(t) + α₂w(t)_)u(t),
_dt_                                       u(t) + k₁

_dv(t)_ = r₂v(t)(1 - v(t)) - α₃ _u(t)v(t)_,
_dt_                                     u(t) + k₂

_dw(t)_ = _γ₁u(t)w(t)_ - μ₁w(t) - α₄ _u(t)w(t)_ + s₁u₁(t). (8)
_dt_      k₃ + u(t)                        u(t) + k₄

<a id='91c5293c-a13b-427c-843c-8ea84faaaec5'></a>

The term s₁ represents the strength of the treatment, and the function control u₁(t) describes an external source of glioma-specific CD8+T cells. The term s₁ is the threshold parameter which determine the stability properties of the glioma-specific CD8+T cells and tumor cells. In our control problem, we maximize the number of CD8+T cells and macrophages and minimize the number of glioma cells and the cost of the control. The positive constant Dg is the weight factor which indicates the patients' level for

<!-- PAGE BREAK -->

<a id='fcc508d1-a3ae-43bd-9883-f8c7f6f734b1'></a>

DE GRUYTER

<a id='d2357270-d05e-45ed-8f5a-cbd0665ecb4f'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy — 277

<a id='6e8af951-966c-4a41-be81-4423c8f90f18'></a>

the acceptance of the treatment. When the drug is admin-
istered in the patients' body, they produce high toxicity
for the patients', for that we consider quadratic control
term as against linear control. If we consider the objective
functional as a control function of u₁(t), it can be observed
that J is concave. Thus, we obtained a maximum value.
The aim is to characterize the optimal control u₁*, such that

<a id='1f9f2811-6857-4aa8-a8a1-db9b9fe1040c'></a>

max J[u₁] = J[u₁*].
0≤u₁(t)≤1

<a id='0d66eb11-4838-489d-8e2b-4de964c7b80a'></a>

## 4.1 Characterization of an optimal control

To determine the precise formula for the optimal control function u₁*, we employ the well-known Pontryagin's Maximum principle [38, 39]. To do this, we define the Lagrangian as follows

<a id='373978e8-db29-40de-962c-35049db0b977'></a>

$$L(u(t), v(t), w(t), \xi_1, \xi_2, \xi_3)$$
$$= v(t) + w(t) - u(t) - \frac{1}{2} D_g u_1^2(t)$$
$$+ \xi_1 \left[ r_1 u(t)(1 - u(t)) - \frac{(\alpha_1 v(t) + \alpha_2 w(t))}{u(t) + k_1} u(t) \right]$$
$$+ \xi_2 \left[ r_2 v(t)(1 - v(t)) - \alpha_3 \frac{u(t) v(t)}{u(t) + k_2} \right]$$
$$+ \xi_3 \left[ \frac{\gamma_1 u(t) w(t)}{k_3 + u(t)} - \mu_1 w(t) - \alpha_4 \frac{u(t) w(t)}{u(t) + k_4} + s_1 u_1(t) \right]$$
$$+ v_1(t) u_1(t) + v_2(t)(1 - u_1(t)),$$

<a id='2ef2e144-7826-4265-8940-5e2de98a959b'></a>

where v₁(t) ≥ 0 and v₂(t) ≥ 0 represents the penalty mul-
tipliers ensuring that the control function u₁(t) remains
bounded between 0 and 1. Also, satisfying

v₁(t)u₁(t) = 0,
v₂(t)(1 - u₁(t)) = 0,

<a id='34d90419-1aa8-4fa8-b5f6-e3838223147e'></a>

at the optimal $u_1^*(t)$.
Here, $\xi_j(t)$, for $j = 1, 2, 3$, are the co-states or adjoint variables, which determine the adjoint system, together with the state variables, indicates the optimality for the system (8).

<a id='55474467-7a9d-4d8a-9db2-93f824238daf'></a>

Now, we shall investigate all the possible values for
the optimal control u₁, including the boundary values
u₁(t) = 0 and u₁(t) = 1. To investigate the interior
maximum for the Lagrangian, we use the Pontryagin's
Maximum Principle such that the unconstrained optimal
control u₁*(t) satisfies

<a id='2306d77d-c395-48d6-a183-f536fd6faa93'></a>

$$\frac{\partial L}{\partial u_1} = 0, \text{ at } u_1 = u_1^*.$$

<a id='4f4d0d08-b514-4861-bcb3-fb71ca2b71a7'></a>

After some algebraic manipulations, we have

$u_1^* = \frac{\xi_3 S_1 + v_1(t) - v_2(t)}{D_g}$ (9)

<a id='bef51c79-840e-4245-9f3d-8d9564d92302'></a>

Now, we consider the following cases:

<a id='d73edc56-1e68-4293-ab6b-6b3eefcb343c'></a>

**Case I.** For the set {t: 0 < u*i(t) < 1} with v1(t) = v2(t) = 0.
From eq. (9), our optimal control can be characterized as

<a id='80b44b12-d061-4aa7-9149-c80b01cdd679'></a>

<::transcription of the content
: $u_1^* = \frac{\xi_3 s_1}{D_g}$.
: equation::>

<a id='dda91f06-a150-4048-adb3-555897782681'></a>

Case II. For the set {t : u₁*(t) = 1} with v₁(t) = 0. From eq. (9), we can write that

1 = u₁* = ξ₃s₁ - v₂(t)
Dg

or, 1 + v₂(t)
Dg
= ξ₃s₁
Dg
.

<a id='549723e5-42e6-42a8-b8f1-d369acd67860'></a>

Since $v_2(t) \ge 0$, then $1 + \frac{v_2(t)}{D_g} \ge 1$. Thus, we obtain that
$1 = u_1^* \le \frac{\xi_3 s_1}{D_g}$.

<a id='8c0b722f-a86c-4316-a9b8-e189ac5c83e8'></a>

**Case III.** For the set {$t : u_1^*(t) = 0$} with $v_2(t) = 0$. From eq. (9), we obtain that

$0 = u_1^* = \frac{\xi_3 S_1 + v_1(t)}{D_g}$

<a id='fbb01b0e-b743-430e-9f03-e113ee5140e0'></a>

Since v₁(t) ≥ 0, then ξ3S1 / Dg ≤ 0. Now, to establish that u₁* is not negative, we use the notation as follows

0 = u₁* = (ξ3S1 / Dg)⁺.

<a id='3d04c556-01cc-46c6-bd1d-9242387c8e9c'></a>

Combining all the three cases in a compact form, we have

$u_1^* = \min \left(1, \left(\frac{\xi_3 s_1}{D_g}\right)^+\right)$.

<a id='bf3ad67a-4b0c-402b-a774-8284ea62a28a'></a>

The above results can be summarized in the following
theorem.

<a id='11efdbf0-d893-4f6d-8fdd-2aa2c3ea5c0d'></a>

**Theorem 4.1.** *The optimal control $u_1^*$ for the control problem (8) can be characterized as*

$u_1^* = \min \left(1, \left(\frac{\xi_3 s_1}{D_g}\right)^+\right)$.

<a id='5b73dc9d-ee4a-49eb-b5ba-166c4ea7fcf6'></a>

## 4.2 Derivation of the optimality system

The most important part of this optimal control problem (8) is to derivation of the optimality system. From

<!-- PAGE BREAK -->

<a id='0cbbd82b-d61b-4014-99f6-2dc7aa1bb990'></a>

278

<a id='319ba1f4-f3cd-41a5-b780-04ff40587030'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='e25d0bc2-b7a0-4923-b721-6c4663be223c'></a>

DE GRUYTER

<a id='ddc6ff27-fe7e-4d73-a822-1d1941f29d86'></a>

the mathematical perspective it describes how the control
problem (8) behaves under the application of an optimal
control. Thus, we may obtain how the different cell pop-
ulations, namely glioma cells, macrophages and glioma-
specific CD8+T cells grow or decay when the patient is
treated with optimal therapy which characterized in the
previous subsection.

<a id='2abf66c4-4dab-4b20-ade7-ff1d941dfff1'></a>

The optimality system is defined as the co-states or
adjoint equations coupled with state variables and the ini-
tial and transversality or final conditions with the optimal
control $u_i^*$. The adjoint equations or co-state system is
given by

<a id='b85c25b9-c1cb-40ce-9c77-d08503bb1065'></a>

dξ₁ / dt = - ∂L / ∂u'
dξ₂ / dt = - ∂L / ∂v'
dξ₃ / dt = - ∂L / ∂w'

<a id='0f52ea32-d5cb-46e6-b6a2-3e8dcc7a17b7'></a>

The set of transversality conditions is known as the final
component for the optimality system, which in this case
reduce to final conditions on the adjoint variables. The
results can be obtained from the book by Lenhart and
Workman [38].

<a id='2b6146bb-1132-4d96-8af1-810862d6b8b4'></a>

For the given maximization problem max $\mathcal{J}[u_1] = \mathcal{H}(u(T)) + \int_0^T h_0(u, u_1)dt$, subject to the state system $\frac{du}{dt} = h(t, u, u_1)$, we obtain the following terminal or transversality conditions for the co-states

<a id='d87e926d-c4a1-4200-8f67-7fece9d194e2'></a>

$$\xi_i(T) = \nabla H(u(T)) + \sum_{i=1}^{n} \alpha_i h_i(u(T))$$

<a id='c400d08f-b2e1-4e7e-a4e4-264ac23773f3'></a>

where the function H represents the terminal cost.
In case of our problem, no terminal cost exists, that
is, H(u(T)) = 0. The problem under consideration, do not
have the target set for our state variables - we have a
desired end result, of course, but the final state is in fact
free, so the summation term will also zero.

<a id='962ee2fc-27f0-4c6c-bfe6-88ee6a99ed36'></a>

Thus, the terminal or transversality conditions for the co-states or adjoint variables are

<a id='b674e24e-df91-401d-a193-572e380305a3'></a>

ξi(T) = 0, for i = 1, 2, 3.

<a id='61891560-864d-4a68-b907-072746a5c86f'></a>

Thus, incorporating the representation of an optimal treatment control $u_t^*$, we obtain the state system coupled with the adjoint system, and the transversality or terminal conditions, we have the following optimality system:

<a id='df2ac734-9b84-464c-8712-3954d96c7f53'></a>

du(t) / dt = r₁u(t)(1 – u(t)) – (α₁v(t) + α₂w(t)) / (u(t) + k₁) u(t),
dv(t) / dt = r₂v(t)(1 - v(t)) - α₃ u(t)v(t) / (u(t) + k₂),
dw(t) / dt = γ₁u(t)w(t) / (k₃ + u(t)) – μ₁w(t) – α₄ u(t)w(t) / (u(t) + k₄) + s₁u₁(t),

<a id='2a685bc2-8e46-4923-9789-5575cc3783f9'></a>

dξ₁/dt = -[ -1 + ξ₁{r₁(1 - 2u(t)) - (k₁(α₁v(t) + α₂w(t)))/(k₁ + u(t))²} - (ξ₂α₃k₂v(t))/(u(t) + k₂)²
+ ξ₃{(γ₁k₃w(t))/(u(t) + k₃)² - (α₄k₄w(t))/(u(t) + k₄)²}] (10)

dξ₂/dt = -[1 - (ξ₁α₁u(t))/(u(t) + k₁) + ξ₂{r₂(1 - 2v(t)) - (α₃u(t))/(u(t) + k₂)}]

dξ₃/dt = -[1 - (ξ₁α₂u(t))/(k₁ + u(t)) + ξ₃{(γ₁u(t))/(k₃ + u(t)) - μ₁} - (α₄u(t))/(k₄ + u(t))]

u₁* = min (1, (ξ₃s₁/Dg)⁺)

<a id='d8883fbb-05ba-48a6-a809-96176ce89a3a'></a>

$\xi_i(T) = 0$, for $i = 1, 2, 3$.

<a id='a8ba42d6-b1fa-4819-a26b-46dd90063f01'></a>

# 5 Numerical simulations

In order to understand the dynamics of glioma-immune interaction, we performed some numerical simulations using MATLAB function and Mathematica by choosing the parameter values presented in Table 1 with positive initial conditions x(0) = 0.12, y(0) = 0.50 and z(0) = 0.20. Our study is not only provide the equilibrium points and their stability characteristics for the system (2) but also represents the feasibility of different complex behavior. For the parameter values in Table 1, we obtained six biologically feasible singular points, namely, trivial singular point E₀(0, 0, 0), gliomas singular point E₁(1, 0, 0), gliomas or tumor free singular point E₁(0, 1, 0), gliomas–macrophages singular point Ẽ(0.925166, 0.943214, 0), gliomas–glioma specific CD8+T cells free singular point E̅(0.438843, 0, 0.132283) and the co-existing singular point E*(0.438843, 0.945159, 0.108199).

<a id='5b58a914-43c3-4dd5-8dd0-75fc6981b19a'></a>

From the clinical point of view, the trivial singular
point E₀ has limited interest and it is always unstable
in the 2-dimensional manifold as the eigenvalues of E₀

<!-- PAGE BREAK -->

<a id='7d06592e-6f2b-4f0b-8fe7-8b1493a29af8'></a>

DE GRUYTER

<a id='4e774665-fc37-4669-8910-69f8ab20dc8a'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='5e8dc749-adf7-4edb-8d77-8014f2d37012'></a>

279

<a id='fcf84dda-3ad4-4e76-b9fb-2bdbe44a0496'></a>

<::3D plot: The plot shows the local asymptotic stability of a co-existing equilibrium point E* (0.438843, 0.945159, 0.108199) with different initial values. The plot has three axes: 'CD8+T cells' (y-axis), 'Macrophages' (x-axis, ranging from 0.4 to 1), and 'Tumor cells' (z-axis, ranging from 0 to 0.6). Multiple colored trajectories (black, magenta, green, blue, yellow, red, and another blue) are depicted, originating from different initial points and converging towards a central point. The initial points are labeled as: (0.02, 0.98, 0.2), (0.6, 0.6, 0.22), (0.6, 0.5, 0.2), (0.1, 0.96, 0.13), (0.25, 0.9, 0.1), (0.55, 0.5, 0.12), (0.2, 0.7, 0.09), and (0.35, 0.5, 0.1).
Figure 3: Local asymptotic stability of the co-existing equilibrium point E* (0.438843, 0.945159, 0.108199) with different initial values. Other parameters are specified in Table 1.
::>

<a id='c7b66e43-0b36-4849-982a-d055da045a69'></a>

are 0.4822, 0.3307, -0.0074. Also, E₁ is unstable in the 2-dimensional manifold as the eigenvalues of E₁ are 0.0124498, 0.311876, -0.4822 and it has also limited interest from the clinical view point. The eigenvalues for the glioma free singular point E₂ are 0.404749, -0.3307, -0.0074, which is unstable in 1-dimensional manifold and stable in 2-dimensional manifold. From the clinical view point E₂ is important as the clinicians can predicts under what situations the patients' will be free from gliomas (brain tumor) and design the better treatment strategy according to the patients' outcome. The eigenvalues for gliomas-macrophages singular point Ẽ are 0.0108977, -0.311734, -0.428041, which is stable in the 2-dimensional manifold and unstable in the 1-dimensional manifold. Biologically, the undesirable singular point Ẽ is saddle type. The eigenvalues of gliomas- CD8+T cells singular point Ẽ are 0.310464, -0.0940901, -0.02903, which is stable in the 2-dimensional manifold and unstable in the 1-dimensional manifold. Form the biological view point, the undesirable singular point Ẽ is saddle type. The co-existing equilibrium point E* in which all the three cells (gliomas, macrophages and tumor specific CD8+T cells) coexist, whose eigenvalues are -0.31286, -0.100647, -0.022180 all are real and negative, which indicates that E* is locally asymptotically stable. The time series plot demonstrates that all the three cell populations reach their equilibrium points and become stable in absence of the immunotherapeutic drug ACI (u₁(t)) = 0, which has been plotted in the Figure 4. Figure 4 represents the fact that the glioma-specific CD8+T cells, mediated by macrophages, is not capable of controlling the progression and development of malignant gliomas [2]. There is no indications of any sort of remission. This can be illustrated in light of the fact that due to absence

<a id='e70a81ee-dc8d-4bad-8c32-86ed2bcf3467'></a>

<::chart: The figure contains three subplots, all sharing a common x-axis labeled "Time" ranging from 0 to 300. Each subplot shows a line graph.

Top subplot:
- Y-axis: "Glioma cells" (ranging from 0 to 0.6)
- The line starts near 0.1, decreases to almost 0 around x=50, then rapidly increases to a peak around 0.6 at x=75, and then gradually decreases and stabilizes around 0.45.

Middle subplot:
- Y-axis: "Macrophages" (ranging from 0.6 to 1)
- The line starts near 0.6, rapidly increases to 1 around x=25, stays at 1 until x=50, then slightly decreases and stabilizes around 0.95.

Bottom subplot:
- Y-axis: "CD8+T cells" (ranging from 0.05 to 0.2)
- The line starts near 0.2, decreases to a minimum around 0.08 at x=75, then gradually increases and stabilizes around 0.11.

Figure 4: Solutions of the system (8) without optimal treatment strategy with initial values $u(0) = 0.1$, $v(0) = 0.55$ and $w(0) = 0.20$. Parameters for this simulations are presented in Table 1.::>

<a id='38e78693-1aed-44d7-adcb-1b7f2bc16d20'></a>

of external drug, the level of macrophages and tumor-specific CD8+T cells go up and down respectively before attaining a equilibrium level. From Figure 4, it can also be observed that the glioma specific CD8+T cells are continually declining as we considered that they are only present when the glioma cells are present, thus they have a negative proliferation rate.

<a id='b61f42f3-7941-4575-9da5-8bf6442b473a'></a>

Figure 3 represents the 3-dimensional phase por-
trait diagram of three cells (gliomas, macrophages and

<!-- PAGE BREAK -->

<a id='da8d9cb9-0c56-4023-a2cc-0e984e71045d'></a>

280

<a id='fb0a0eeb-7730-42ff-9dff-fccefe141e97'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='1c6a0618-faa3-4649-af66-c2a7d7c28cb2'></a>

DE GRUYTER

<a id='82902bc3-4b1d-4b9c-ac93-c48cdc43b93f'></a>

<::chart: The image displays three stacked line charts, all sharing a common x-axis labeled "Time" ranging from 0 to 300. Each chart represents the solution of a state system.

**Top Chart: Glioma cells**
- Y-axis: "Glioma cells", ranging from 0 to 1.
- The line starts near 0, rapidly increases to a peak around 0.9 at approximately Time 25, then gradually decreases to about 0.5 at Time 300.

**Middle Chart: Macrophages**
- Y-axis: "Macrophages", ranging from 0.6 to 1.
- The line starts around 0.6, rapidly increases to a plateau near 0.95 at approximately Time 25, and remains relatively constant until Time 300.

**Bottom Chart: CD8+T cells**
- Y-axis: "CD8+T cells", ranging from 0 to 0.1.
- The line starts around 0.01 and gradually increases, reaching approximately 0.08 at Time 300.

Figure 5: Solutions of the state system (8) when the immunotherapeutic drug ACI is administered with Dg = 100.::>

<a id='e1bf6d50-b3fd-42df-99e2-1233075f7537'></a>

glioma-specific CD8+T cells). From Figure 3, it can be noticed that all the trajectories initiating into the region of attraction approach towards the interior singular point E*, in which all three three cells exist together. For different choices initial size of glioma cells u(0), macrophages v(0) and glioma-specific CD8+T cells w(0), we draw a three dimensional phase diagram (see Figure 3) for the model system (2) as [u(0), v(0), w(0)] are [0.6, 0.5, 0.2], [0.35, 0.5, 0.1], [0.25, 0.9, 0.1],
[0.55, 0.5, 0.12], [0.2, 0.7, 0.09], [0.02, 0.98, 0.2],
[0.6, 0.6, 0.22] and [0.1, 0.96, 0.13]. The 3-dimensional phase plane diagram (Figure 3) indicates that the disease will always present in the patients' body in absence of the drug ACI and from which the oncologists can get an idea how to chalk out the optimal treatment strategy.

<a id='5efd3493-e14c-4e26-b1a3-161149834a14'></a>

Now, we shall investigate the dynamics of glioma-
immune interaction for the model system (8) after the
administration of immunotherapeutic drug ACI. We ran
the numerical simulation for a small time period 300 days.
From the mathematical point of view, the uniqueness of
the solution for optimal system holds for a small time win-
dow. In Figure 5, we demonstrate that the results for the
case where the treatment regimens were employed. It can
be observed that the glioma burden goes up and attains a
equilibrium state as one can expect for such a shorter time
window. From Figure 5, it can be observed that the levels
of both macrophages and CD8+T cells more or less remain

<a id='eba2a884-9d38-4bd3-a92b-6d2a9e6ff68c'></a>

unchanged. In case of the glioma cells, however, there is
a gradual attainment of an equilibrium state.

<a id='0e85864c-3464-4baa-931d-1776b96b3f5b'></a>

Now we focused on the outcome after administration
of the immunotherapeutic drug ACI ($D_g$ = 1.0). From
Figure 6 it can be noticed that the cell count of both macro-
phages and glioma specific CD8+T cells increases because
of the external administration of ACI, in conjunction with
natural activation of glioma specific CD8+T cells. Both
these acts contributed to the activation of macrophages
and activated CD8+T cells, which in turn caused some
reduction of the glioma cells burden (first figure of Figure
6) as compared to the without treatment case (first figure
of Figure 4) and as compared to the case for $D_g$ = 100 (first
figure of Figure 5).

<a id='491d188f-2faa-4f01-bf59-499ea31cf74c'></a>

From the model simulations, as presented in Figure
7, indicate that the model system (8), with biologically
meaningful parameter assumptions and values used, is
capable of controlling the glioma cells by our immune
component macrophages in a biologically realistic time
window after administration of immunotherapeutic drug
ACI (D_g = 0.1). After administration of the drug ACI, our
immune system is capable of recognizing and eliminat-
ing the glioma cells, though some glioma cells escape
from immune surveillance [37]. From Figure 7, it can be
observed that the cell count of macrophages and glioma
specific CD8+T cells increases. This is happen due to
external injection of the immunotherapeutic drug ACI. As

<!-- PAGE BREAK -->

<a id='3b44562e-d2a8-4da1-b9b3-b8d5c73e2316'></a>

DE GRUYTER

<a id='730a6454-505e-46bc-93d4-880f52866ef2'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='51775f2c-b30e-4db4-b556-67c8890e13f0'></a>

281

<a id='06d05100-651f-49c8-bab4-a528d61ba38d'></a>

<::Three line plots stacked vertically, sharing a common x-axis labeled "Time" ranging from 0 to 300. The plots illustrate the solutions of a state system when an immunotherapeutic drug is administered. The top plot shows "Glioma cells" on the y-axis, ranging from 0 to 1. The curve starts at 0, rises to a peak around 0.8 at approximately x=25, and then gradually decreases to stabilize around 0.35. The middle plot shows "Macrophages" on the y-axis, ranging from 0.6 to 1. The curve starts around 0.6, rapidly increases to a peak around 0.95 at approximately x=25, and then stabilizes at that level. The bottom plot shows "CD8+T cells" on the y-axis, ranging from 0 to 0.15. The curve starts at 0, gradually increases, and stabilizes around 0.12 from approximately x=150 onwards. Figure 6: Solutions of the state system (8) when the immunotherapeutic drug ACI is administered with D_g = 1.0.::>

<a id='f12a78dc-9628-4a77-8393-3bd1ea4d6ca5'></a>

one would expect that there is a slight increase of glioma cells before a sharp decline in the level of gliomas. This reflects the clinical/biological fact that it takes some time for the external therapy to act on the gliomas. In any case the development or progression of glioma size over time is always less than the corresponding gliomas density in the other three cases. Also, similar kind of dynamics can be observed after the administration of the external therapy ACI (D_g = 0.001) which has been shown in Figure 8. If we reduce the effective cost of the drug ACI, then the gliomas burden also reduces. It is also showing that the glioma burden decreases sharply after a slight growth of glioma cells. This indicates that the external immunotherapeutic drug ACI takes some time to eliminate or destroy the glioma cells.

<a id='c4c901c8-566e-4f7f-8b36-2111350f1095'></a>

Figure 9 represents the co-states or adjoint variables
ξ1, ξ2 and ξ3 respectively. The optimal effectiveness of the
treatment strategies has been shown in the Figure 9. Of
particular interest is to notice that ξ3 (third adjoint/co-
state). Since our control function u1(t) depends heavily
upon the value of the ξ3, the value of the control function
u1(t) become one when ξ3 is positive (see Figure 10). The

<a id='5142542e-41bb-44c0-940e-79a9c55c89bd'></a>

control vanishes between 250 days and 300 days due to the fact that our adjoint goes to zero (for the case D_g = 0.1). Since the co-state is directly related to the density of the glioma specific CD8+T cells, this effects them and the glioma dynamics due to the coupled nature of the system of equations. When the size of glioma increases, the third adjoint causes the control (drug) to adjust and effectively lowers the glioma cells from 200 days to 300 days. It can be observed that there is a delayed reaction between the administration in immunotherapeutic drug ACI and the reduction of the glioma cells. Eventually the glioma cells grows again because of the unstable dynamics. All these were done while keeping the side effects of the external treatment to the minimal.

<a id='7d763987-e72e-43c4-9c86-41c113efe045'></a>

## 6 Discussion
In this article we studied a mathematical model to study the dynamics of the glioma-immune interaction in conjunction with an immunotherapeutic drug ACI. We take into account the glioma cells (brain tumor),

<!-- PAGE BREAK -->

<a id='1b7b3ed2-b325-41f4-93e4-f65345e52447'></a>

282

<a id='80e0c915-2a33-4d7b-8940-c46ca3295f54'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='d392dd6f-5c8e-41f7-a00c-03e8ab51724a'></a>

DE GRUYTER

<a id='59e1acaa-e498-4044-8d9d-cddebaba0e5b'></a>

<::chart: The figure displays three line graphs stacked vertically, all sharing a common x-axis labeled 'Time' ranging from 0 to 300. Each graph represents the solution of an objective functional.  The top graph shows 'Glioma cells' on the y-axis, ranging from 0 to 1. The curve starts at 0, rises to a peak around 0.75 at approximately x=25, and then decreases, approaching 0 by x=200. The middle graph shows 'Macrophages' on the y-axis, ranging from 0.6 to 1. The curve starts at 0.6, rises sharply to nearly 1 by x=50, and then gradually increases, plateauing at 1. The bottom graph shows 'CD8+T cells' on the y-axis, ranging from 0 to 0.15. The curve starts at 0, rises to approximately 0.14 by x=150, and then levels off. Figure 7: Solutions of the objective functional $\mathcal{J}[u_1]$ associated with the state system (8) when the immunotherapeutic drug ACI is administered with $D_g = 0.1$.::>

<a id='b3d03359-23b4-4601-be0e-8280c04091e6'></a>

macrophages, glioma specific CD8+T cells and the immunotherapeutic drug Adoptive Cellular Immunotherapy (ACI). The main difficulties in the treatment of brain tumors are the sequestered location beyond the BBB and the infiltrative nature of gliomas. We investigate some aspects of the dynamics of the proliferation of malignant gliomas, as well as, we investigate its suppression and elimination by varying the system parameters. The dynamics of the system (2) without treatment strategy reveal six biologically feasible singular points. We performed positivity and boundedness of the system, which indicates that none of the populations cannot grow unboundedly. For the parameter set in Table 1, we investigate that our system is locally asymptotically stable, which has been shown in the time series solution (see Figure 4), as well as in the 3-dimensional phase diagram (see Figure 3).

<a id='d9cb1b6e-b5c6-4560-872c-2e62b392e764'></a>

The most important contribution of this work is the
fact that we are able to use deterministic control theory
to find an optimal treatment strategy. In this work, we
identify that the weight factor Dg plays an important role

<a id='64be0ed4-894d-4a1e-929c-0b29669438b3'></a>

to eradicate the glioma cells, as well as the immune sys-tem can be depleted by glioma cells. The goal was to betterunderstand the biological dynamics of the three interact-ing cell population. We take into account the different val-ues of the optimal treatment effectiveness Dg. For our pur-pose we examined the external immunotherapeutic agentACI. We formulated an objective functional J[u₁], keep-ing the biomedical goals in our mind and investigatedthe dynamics without therapy (see Figure 4), with therapy(see Figures 5-8) with a total four possible scenarios.

<a id='cc39b8d3-ddc2-43b1-9a51-5d472a330a3e'></a>

We observed that the strength of the treatment Dg is the most effective in reducing glioma cell burden. For the lower threshold value of Dg = 0.001, the glioma cells can be eliminated and the cell count of macrophages and activated CD8+T cells increases. From Figures 7 and 8 it can be noticed that there is a slight increase of glioma cells before a sharp fall in glioma cells. This indicates the fact that it takes some time for the external immunotherapeutic agent ACI to act on the gliomas. In this work, we also presented a comparison between the four different scenarios, which form a biomedical perspective gives a

<!-- PAGE BREAK -->

<a id='7a517de5-db29-4fa3-9948-8a113f621f2b'></a>

DE GRUYTER

<a id='effb2953-e5b3-477a-a768-f262e3e48135'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='f402ecc9-8a83-48ec-bbfc-346b43f3753b'></a>

283

<a id='0355b754-7454-4bcb-a2f7-9ecc6155ba68'></a>

<::chart: The image displays three stacked line charts, all sharing a common x-axis labeled "Time" ranging from 0 to 300. The y-axis labels and ranges vary for each chart.

**Top Chart:**
- Y-axis label: "Glioma cells"
- Y-axis range: 0 to 1
- Data: A blue line starts near 0, rises to a peak of approximately 0.75 around Time = 25-30, then gradually decreases, approaching 0 by Time = 200 and remaining near 0 until Time = 300.

**Middle Chart:**
- Y-axis label: "Macrophages"
- Y-axis range: 0.6 to 1
- Data: A blue line starts at 0.6, rapidly increases to approximately 0.9 by Time = 25, then slowly continues to rise, approaching 1 by Time = 200-250 and staying at that level.

**Bottom Chart:**
- Y-axis label: "CD8+T cells"
- Y-axis range: 0 to 0.15
- Data: A blue line starts near 0, steadily increases, reaching a peak of approximately 0.14-0.15 around Time = 150, and then levels off, remaining constant until Time = 300.

Figure 8: Solutions of the state system (8) when the immunotherapeutic drug ACI is administered with $D_g = 0.001$.::>

<a id='b2303f88-2510-48aa-ac66-eae6bdc252aa'></a>

<::chart: The visual displays three line graphs stacked vertically, all sharing a common x-axis labeled 'Time' ranging from 0 to 300. Each graph shows the solution of an adjoint equation.

Top Graph:
- Y-axis: 'Adjoint (ξ₁)' ranging from -200 to 100.
- The blue line starts near 0, slightly increases to a peak around 0-20 before time 100, then gradually decreases, reaching approximately -150 at time 300.

Middle Graph:
- Y-axis: 'Adjoint (ξ₂)' ranging from 2 to 6.
- The blue line starts near 6, decreases sharply to a local minimum around 2.5 at approximately time 100, then increases to a local maximum around 4 at approximately time 150, and subsequently decreases towards approximately 3 at time 300.

Bottom Graph:
- Y-axis: 'Adjoint (ξ₃)' ranging from 0 to 1000.
- The blue line starts near 900, decreases to a local minimum around 500 at approximately time 75, then increases to a local maximum around 900 at approximately time 150, and finally decreases sharply to approximately 200 at time 300.

Figure 9: Solutions of adjoint equations for the state system (8) when the immunotherapeutic drug ACI is administered with Dg = 0.1.::>

<!-- PAGE BREAK -->

<a id='5047a78f-a995-434b-b30b-4362005c35e0'></a>

284

<a id='cbc1edc9-aa03-4e5f-b557-0ceb53c5e521'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='db4d2231-a63c-4c52-a0d2-8bf4404a8db1'></a>

DE GRUYTER

<a id='e25b1a95-4bfd-4dfc-b23c-4ea70c66676d'></a>

<::chart: The image displays four line graphs arranged in a 2x2 grid, all sharing a common y-axis label "Optimal treatment strategy u₁" and a common x-axis label "Time (arbitrary units)". Each graph illustrates the optimal treatment strategy over time for different values of D_g. The y-axis for the top-left graph ranges from 0 to 0.05, while for the other three graphs, it ranges from 0 to 1. The x-axis for all graphs ranges from 0 to 300. The four graphs are:

1.  **Top Left (D_g = 100):** The line starts at approximately 0.04, decreases gradually to 0.01 around Time = 150, and then remains constant at 0.01 until Time = 300.
2.  **Top Right (D_g = 1.0):** The line starts at 1, decreases to about 0.4 around Time = 150, then further decreases, reaching 0 at Time = 300.
3.  **Bottom Left (D_g = 0.1):** The line remains at 1 for most of the duration, then sharply drops to 0 starting around Time = 270 and reaching 0 at Time = 300.
4.  **Bottom Right (D_g = 0.001):** The line remains at 1 for almost the entire duration, then sharply drops to 0 starting around Time = 290 and reaching 0 at Time = 300.

Figure 10: Solutions of the objective functional $\mathcal{J}[u_1]$ when the immunotherapeutic drug ACI is administered with different values for $D_g$.::>

<a id='c4edb3ae-306c-4d72-a765-601ee3cef60c'></a>

better assessment of the treatment options. An optimal control study for the immunotherapeutic treatment for the square integrable case gives a representation of a single optimal control that has the potential to minimize the glioma cell burden and the effectiveness of the cost. Figure 8 represents the fact that the glioma burden in the objective functional is minimized, the glioma cells reduced but may not be totally eliminated from the patient's body.

<a id='141e9446-dbd7-4588-97e3-535f81fa14ca'></a>

We hope that the mathematical model, which con-
sider the interplay between glioma cells and the immune
system, constitutes an important step towards develop-
ing strategies for the treatment of malignant gliomas.
The understanding of glioma proliferation and develop-
ment may help in the treatment of diseases. In future
works, we plan to investigate this biological process con-
sidering nonlinear time and space models to describe the
spatiotemporal evolution patterns of gliomas.

<a id='be93202b-f127-4622-80cd-616728338280'></a>

**Acknowledgment:** I am thankful to the reviewer and the editor for their careful reading of this manuscript, the questions they posed and suggestions they offered. As a result, this paper is significantly improved. This study was supported by the Science & Engineering Research Board (SERB), Govt. of India, File No.: ECR/2017/000234.

<a id='3daa8d6c-7b7d-4008-ac57-4f1be40d1b65'></a>

## References

[1] L.M. DeAngelis, Brain tumors, N. Engl. J. Med. **344** (2001),
114–123.

<a id='e41f0412-9dd7-4aed-9e5a-fef0016dbc34'></a>

2. G.P. Dunn, L.J. Old and R.D. Schreiber, The three Es of cancer immunoediting, Annu. Rev. Immunol. 22 (2004), 329-360.
3. S. Khajanchi, Bifurcation analysis of a delayed mathematical model for tumor growth, Chaos Solitons Fractals. 77 (2015), 264-276.
4. P. Gerlee and S. Nelander, The impact of phenotypic switching on glioblastoma growth and invasion, PLoS ONE Comput. Biol. 8(6) (2012), e1002556.
5. N. Kronik, Y. Kogan, V. Vainstein and Z. Agur, Improving alloreactive CTL immunotherapy for malignant gliomas using a simulation model of their interactive dynamics, Cancer Immunol. Immunother. 57(3) (2008), 425-439.
6. S. Nandi, S. Khajanchi, A.N. Chatterjee and P.K. Roy, Insight of viral infection of Jatropha Curcas plant (future fuel): a control based mathematical study, Acta Anal. Funct. Appl. 13(4) (2011), 366-374.
7. S. Khajanchi, Modeling the dynamics of glioma-immune surveillance, Choas Solitons Fractals. 114 (2018), 108-118.
8. M. Gosak, R. Markovic, J. Dolensek, M.S. Rupnik, M. Marhl, A. Stozer and M. Perc, Network science of biological systems at different scales: a review, Phys. Life Rev. 24 (2018), 118-135.
9. S. Banerjee, S. Khajanchi and S. Chaudhury, A mathematical model to elucidate brain tumor abrogration by immunotherapy with T11 target struncture, PLoS ONE 10(5) (2015), e0123611.
10. K.R. Swanson, C. Bridge, J.D. Murray and E.C. Alvord Jr, Virtual and real brain tumors: Using mathematical modeling to quantify glioma growth invasion, J. Neurol. Sci. 216(1) (2003), 1-10.
11. R.D. Schreiber, L.J. Old and M.J. Smyth, Cancer immunoediting: integrating immunity's roles in cancer suppression and promotion, Science 331 (2011), 1565-1570.
12. W.F. Hickey, Basic principles of immunological surveillance of the normal central nervous system, Glia 36 (2001), 118-124.
13. S. Khajanchi and S. Banerjee, Stability and bifurcation analysis of delay induced tumor immune interaction model, Appl. Math. Comput. 248 (2014), 652-671.

<!-- PAGE BREAK -->

<a id='b0a1d415-9769-453c-98d2-2c92577a3488'></a>

DE GRUYTER

<a id='ac7b23b5-2ed1-4427-9c4d-4313de2faaae'></a>

S. Khajanchi: Glioma-Immune Interaction Model under Optimal Therapy

<a id='c702c6ef-6924-41b0-bafd-d1a9e4421c6a'></a>

285

<a id='30accb55-7812-45a7-baf8-f3354fbe03c7'></a>

[14] S. Khajanchi and J.J. Nieto, Mathematical modeling of tumor-immune competitive system, considering the role of time delay, Appl. Math. Comput. **340** (2019), 180–205.
[15] D. Ghosh, S. Khajanchi, S. Mangiarotti, F. Denis, S.K. Dana and C. Letellier, How tumor growth can be influenced by delayed interactions between cancer cells and the microenvironment?, BioSystems. **158** (2017), 17–30.
[16] S. Khajanchi and D. Ghosh, The combined effects of optimal control in cancer remission, Appl. Math. Comput. **271** (2015), 375–388.
[17] V.A. Kuznetsov, I.A. Makalkin, M.A. Taylor and A.S. Perelson, Non-linear dynamics of immunogenic tumors: parameter estimation and global bifurcation analysis, Bull. Math. Biol. **56(2)** (1994), 295–321.
[18] S. Bunimovich-Mendrazitsky, J.C. Gluckman and J. Chaskalovic, A mathematical model of combined bacillus Calmette-Guerin (BCG) and interleukin (IL)-2 immunotherapy of superficial bladder cancer, J. Theor. Biol. **277** (2011), 27–40.
[19] S. Bunimovich-Mendrazitsky, H. Byrne and L. Stone, Mathematical model of pulsed immunotherapy for superficial bladder cancer, Bull. Math. Biol. **70(7)** (2008), 2055–2276.
[20] X. Lai and A. Friedman, Mathematical modeling in scheduling cancer treatment with combination of VEGF inhibitor and chemotherapy drugs, J. Theor. Biol. **462** (2019), 490–498.
[21] S. Khajanchi, M. Perc and D. Ghosh, The influence of time delay in a chaotic cancer model, Chaos. **28** (2018), 103101.
[22] S. Khajanchi and S. Banerjee, Quantifying the role of immunotherapeutic drug T11 target structure in progression of malignant gliomas: mathematical modeling and dynamical perspective, Math. Biosci. **289** (2017), 69–77.
[23] S. Khajanchi, Bifurcations and oscillatory dynamics in a tumor immune interaction model, BIOMAT 2015. (2016), 241–259. doi.org/10.1142/9789813141919_0016
[24] S.P. Chakrabarty and F.B. Hanson, Distributed parameters deterministic model for treatment of brain tumors using Galerkin finite element method, Math. Biosci. **219** (2009), 129–141.
[25] K.C. Iarosz, F.S. Borges, A.M. Batista, M.S. Baptista, R.A.N. Siqueira, R.L. Viana and S.R. Lopes, Mathematical model of brain tumour with glia–neuron interactions and chemotherapy treatment, J. Theor. Biol. **368** (2015), 113–121.
[26] S. Khajanchi and S. Banerjee, Influence of multiple delays in brain tumor and immune system interaction with T11 target

<a id='559050d3-f75b-441b-8524-f99a0c3cba5b'></a>

structure as a potent stimulator, Math. Biosci. **302** (2018), 116–130.

[27] S. Khajanchi, Uniform persistence and global stability for a brain tumor and immune system interaction, Biophys. Rev. Lett. **12(4)** (2017), 187–208.

[28] J.M. Murray, Optimal control for a Cancer chemotherapy problem with general growth and loss functions, Math. Biosci. **98(2)** (1990), 273–287.

[29] G.W. Swan, General applications of optimal control theory in cancer chemotherapy, IMA J. Math. Appl. Med. Biol. **5(4)** (1988), 303–316.

[30] G.W. Swan, Role of optimal control theory in Cancer chemotherapy, Math. Biosci. **101(2)** (1990), 237–284.

[31] Z. Wang, C.T. Bauch, S. Bhattacharyya, A. d'Onofrio, P. Manfredi, M. Perc, N. Perra, M. Salathe and D. Zhao, Statistical physics of vaccination, Phys. Rep. **664** (2016), 1–113.

[32] T. Burden, J. Ernstberger and K.R. Fister, Optimal control applied to immunotherapy, Discrete Cont. Dyn. B **4(1)** (2004), 135–146.

[33] F. Castiglione and P. Piccoli, Cancer immunotherapy, mathematical modeling and optimal control, J. Theor. Biol. **247(4)** (2007), 723–732.

[34] L.G. de Pillis, W. Gu, K.R. Fister, T. Head, K. Maples, A. Murugan, T. Neal and K. Yoshida, Chemotherapy for tumors: an analysis of the dynamics and a study of quadratic and linear optimal controls, Math. Biosci. **209(1)** (2007), 292–315.

[35] K.R. Fister and J.C. Panetta, Optimal control applied to competing chemotherapeutic cell-kill strategies, SIAM J. Appl. Math. **63(6)** (2003), 1954–1971.

[36] K.R. Fister and J.H. Donnelly, Immunotherapy: An optimal control theory apprach, Math. Biosci. Eng. **2(3)** (2005), 499–510.

[37] F.H. Igney and P.H. Krammer, Immune escape of tumors: Apoptosis resistance and tumor counterattack, J. Leukoc. Biol. **71(6)** (2002), 907–920.

[38] S. Lenhart and J.T. Workman, Optimal control applied to biological models, Chapman and Hall/CRC, 2007.

[39] L.S. Pontryagin, V.G. Boltyanskii, R.V. Gamkrelidze and E.F. Mishchenko, The mathematical theory of optimal process, Wiley, New Jersey, 1962.

[40] J.S. Spratt and J.A. Meyer, Rates of growth of human neoplasms: Part II, J. Surg. Oncol. **61** (1996), 68–83.
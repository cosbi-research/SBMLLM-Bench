<a id='301a5e3c-2450-4c70-9073-27ec13b40dc2'></a>

Research Article

<a id='03e05f59-05cc-4a09-8587-acf40f1f6ef8'></a>

Mathematical
Methods in the
Applied Sciences

<a id='ca121bd9-837f-4b70-b9db-a8a3fc75f557'></a>

Received 26 March 2014

<a id='235ac0ab-1970-4054-93f5-2381636766af'></a>

Published online 29 December 2014 in Wiley Online Library

<a id='49d97216-4e3f-46a0-acef-2b29e779ee53'></a>

(wileyonlinelibrary.com) DOI: 10.1002/mma.3370
MOS subject classification: 92B05; 92D25

<a id='647bc52e-d0fb-4cc7-ab7b-a12ec7cbfa5b'></a>

Qualitative behavior of systems of tumor-CD4+-cytokine interactions with treatments

<a id='b24d7498-ec12-4344-8a1f-5610dbbac349'></a>

Luke Anderson⁰, Sophia Jang⁰*† and Jui-Ling Yuⁱ,⁲

<a id='91d80098-30bc-4b88-9715-c08137b8bba0'></a>

**Communicated by Y. Xu**
Immunotherapies are important methods for controlling and curing malignant tumors. Based on recent observations that many tumors have been immuno-selected to evade recognition by the traditional cytotoxic T lymphocytes, we propose mathematical models of tumor–CD4+-cytokine interactions to investigate the role of CD4+ on tumor regression. Treatments of either CD4+ or cytokine are applied to study their effectiveness. It is found that doses of treatments are critical in determining the fate of the tumor, and tumor cells can be eliminated completely if doses of cytokine are large. Bistability is observed in models with either of the treatment strategies, which signifies that a careful planning of the treatment strategy is necessary for achieving a satisfactory outcome. Copyright © 2014 John Wiley & Sons, Ltd.

<a id='f1ab5ca4-1873-44b7-b471-b4b488c17af6'></a>

Keywords: tumor; cytokine; ordinary differential equations; global stability; bistability

<a id='8dfe6631-ccdb-4cbb-b45f-0954b7ca0c25'></a>

# 1. Introduction
Cancer is a broad group of diseases, all involved with unregulated cell growth. In cancer, cells divide and grow uncontrollably, forming malignant tumors and invading even distant parts of the body [1]. Many tumors express antigens that can be recognized by the adaptive immune system and therefore can be used to induce an antitumor immune response. The Tumor Immuno-Surveillance Hypothesis formulated in 1957 suggests that the immune system is capable of inhibiting the growth of very small tumors and eliminating them before they become clinically evident [2].

<a id='ad9ea27b-740b-4f3e-a29f-e2849992e3e9'></a>

Cancer immunotherapies have focused much on the antitumor activities of white blood cells, especially T cells (usually CD8+ T cells), natural killer (NK) cells, and macrophages. Experiments have shown that these immune cells can lyse tumor cells very effectively [3, 4]. The interactions between tumor cells and other components of the tumor microenvironment, however, are very complex and continuously changing. Consequently, devising cancer immunotherapies to treat or to cure cancer has proven a very challenging task. Mathematical modeling provides a useful tool to understand the interactions among the many components of the tumor microenvironment [5–8].

<a id='d103327a-ac13-4026-b46d-8820c1a48200'></a>

Most cancer immunotherapies are based on the generation of cytotoxic T lymphocyte (CTL) such as CD8+ T cells that recognize tumor antigens in association with major histocompatibility complex class I molecules on tumor cells [9]. However, strong evidence has shown that many tumors have been immuno-selected to evade recognition by CTLs [9]. Traditionally, CD4+ T cells have been assumed to have only a helper role by activating CD8+ T cells to kill cancer cells. Recent experiments, however, have shown that CD4+ T cells actually play a more direct role in killing the cancer cells [9-11]. Indeed, these CD4+ T cells appear to have an effector role through the cytokines and chemokines that they produce [9, 11]. Consequently, CD4+ T cells can kill cancer cells even in the absence of CD8+ T cells and NK cells. In these cases, tumor eradication may be mediated by tumoricidal myeloid cells recruited into the tumors or by anti-angiogenic cytokine, such as IL-4 secreted by CD4+ T cells [9, 11].

<a id='5a8d0947-276c-44bf-8856-34d7fe32f6e5'></a>

In this work, we propose mathematical models of tumor cells, CD4+T cells, and cytokine interactions to investigate possible effects of CD4+ on tumor regression and dormancy. In fact, CD4+ T cells cannot kill the tumor cells directly but can secrete and use cytokines to suppress tumor growth. There are many mathematical models of tumor-immune interactions in the literature. For example, Forys et al. [12], Kuznetsov et al. [13], Michelson et al. [14], and de Vladar and Gonzalez [15] propose models of ordinary differential equations to

<a id='208894f9-c8e8-495d-a1d7-ca5540ca9d4a'></a>

a Department of Mathematics and Statistics, Texas Tech University, Lubbock, TX 79409-1042, USA
b Department of Financial and Computational Mathematics, Providence University, Taichung 43301, Taiwan
c Physics Division, National Center for Theoretical Sciences, Taiwan
* Correspondence to: Sophia Jang, Department of Mathematics and Statistics, Texas Tech University, Lubbock, TX 79409-1042, USA.
† E-mail: sophia.jang@ttu.edu

<a id='a29ee0de-1582-4e7b-801e-647da43ba68b'></a>

4330

<a id='5db344ba-0547-4a65-89fd-86fe6851cec8'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='1d706581-1260-4889-9189-0284ef497797'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<!-- PAGE BREAK -->

<a id='4930b89e-27a1-4dd0-91b6-30353361b911'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='594790ab-a9ba-4054-886d-94d9a9b5e180'></a>

Mathematical Methods in the Applied Sciences

<a id='1659893c-52cb-453d-8263-29438e6f62dc'></a>

study the interactions between tumor and effector cells. Kirschner and Panetta [16] have investigated the dynamics between cytokine and CTL cells in the 1990s, where the CTL cells are directly killing cancer cells. The article by Eftimie et al. [2] provides a very thorough review of the research in this area. More recently, Eftimie et al. [17] propose models of tumor, CD4+, and cytokine interactions to study the role of CD4+ cells on skin tumor rejection, where CD4+ cells are separated into Th1 and Th2 cells. The system in [17] is complicated and consists of either six or seven ordinary differential equations depending on whether granulocytes are included or not. It is concluded from simulations that the feedback between Th2 cells and eosinophils can promote tumor rejection [17].

<a id='4f883913-6be3-487d-aceb-cd6f808d5674'></a>

The present model in this investigation is different from that of Eftimie et al. [17] and others. Specifically, CD4+ T cells are grouped as one type of cells and only tumor suppressing cytokine such as IL-4 is considered. There is no direct interactions between CD4+ cells and tumor cells. Moreover, adoptive immunotherapy of either CD4+ T cells or cytokine is applied. Our goal is to determine whether the immunotherapy is sufficient to kill tumor cells completely when CD4+ T cells are considered in the tumor-suppressing process without CTLs. When there is no treatment, linear stability analysis indicates that tumor cells cannot be eliminated completely even if the tumor is small. With the treatment of CD4+, the tumor cannot grow to its carrying capacity, and the model can exhibit bi-stability. When the treatment of cytokine is implemented, it is possible to kill all the cancer cells if doses of treatment are large. However, tumor cells may grow to the carrying capacity if doses of treatment are small. We numerically simulate the model and compare different treatment strategies. We conclude that it is better to adopt CD4+ T cells as the immunotherapy than using the cytokines when doses are small. Both strategies are able to suppress the tumor into low volume if doses are large. Moreover, large doses of treatment by cytokine can wipe out the tumor cells completely.

<a id='b66f9404-5175-461c-8777-66d1a405c4ec'></a>

In the following section, a simple mathematical model consisting of three ordinary differential equations is presented, and analysis is carried out on the model of no treatment. Section 3 analyzes models with treatments. Specifically, treatments by CD4+T cells are considered in Section 3.1, and Section 3.2 deals with the model of treatment by cytokine. Numerical simulations are performed in Section 4, and the final section provides a brief summary and discussion.

<a id='82fb203a-f296-464f-b5fe-656f4df39082'></a>

## 2. Models of tumor cells, CD4+ T cells, and cytokine interactions

In this section, we introduce models of tumor, CD4$^+$, and cytokine interactions and provide analysis for the model with no treatment.
Let x, y, and z denote the tumor cells, CD4$^+$ T cells, and the cytokine (IL-4 or more broadly any cytokine produced by Th2), respectively.
The proposed model is given by

<a id='666c67c6-867e-4401-a5f2-2705125eb612'></a>

$$\begin{cases}x' = xf(x) - d(x, z)\\y' = g_y(x,y) - a_y(y) + l_1(t)\\z' = g_z(x, y, z) - a_z(z) + l_2(t),\end{cases}\quad(1)$$

<a id='7851e424-f97f-4076-a5f1-849cf60f0706'></a>

where f(x) is the per capita growth rate of the tumor cells, d(x, z) denotes the loss of tumor cells caused by cytokine, gy(x, y) is the proliferation of the CD4⁺ T cells through interactions with the tumor cells, and g₂(x, y, z) denotes productions of cytokine secreted by CD4⁺ T cells. Expression aᵧ(y) is the apoptosis (natural death) of the T cells, a₂(z) denotes the loss of cytokine, and I₁(t) and I₂(t) are the immunotherapy treatments, which may be time-dependent.

<a id='155efe14-7493-454f-bdd1-d07312d26d29'></a>

2.1. The model and preliminary analysis

We use a logistic growth equation for the tumor cells and a Michaelis-Menten for all the functional forms with different half saturation constants. Consequently, it is assumed that the tumor's growth is limited and the productions of CD4$^+$ and cytokine due to the tumor cells are also limited. With this consideration, the model is given by

<a id='5318d5c3-6382-445c-9764-2dd1d49057ba'></a>

```latex
x' = rx(1 - x/K) - \frac{\delta xz}{m + x}
y' = \frac{\beta xy}{k + x} - ay + I_1
z' = \frac{\alpha xy}{b + x} - \mu z + I_2
```
(2)

<a id='17811395-18d8-4f8b-84fe-cfbd7dc5f84f'></a>

where all the parameters r, K, m, δ, β, k, a, a, b, and μ are positive constants and I₁ ≥ 0 and I₂ ≥ 0 denote constant treatments of CD4⁺ and cytokine per unit time, respectively. The parameters and their biological interpretations are summarized in Table I.

<a id='97ff79e3-d0e9-4de0-a34a-753e0269179c'></a>

Proposition 2.1
_Solutions of (2) exist and remain nonnegative for t > 0._

<a id='9e7dca53-6848-441e-b743-da36ebd88b02'></a>

Proof
Because $x'|_{x=0} = 0$, $y'|_{y=0} = I_1 \ge 0$, and $z'|_{z=0,x,y\ge 0} \ge I_2 \ge 0$, solutions of (2) remain nonnegative on the time interval for which they are defined [18]. Let $(x(0),y(0), z(0))$ be given. We may assume $x(0)y(0)z(0) > 0$. Notice $x' \le rx(1-x/K)$, and consider $w' = rw(1-w/K)$ with $w(0) = x(0)$. Then, $x(t) \le w(t)$ for all $t > 0$, where $\lim_{t\to\infty} w(t) = K$. Moreover, $x'|_{x\ge K} < 0$ implies $x(t) < K$ for all

<a id='09c60ddc-c5d6-4145-a229-205dc71420f6'></a>

Copyright  2014 John Wiley & Sons, Ltd.

<a id='ca87ae93-1f4a-4159-ad50-4f289da11352'></a>

_Math. Meth. Appl. Sci._ **2015**, 38 4330–4344

<a id='d948a442-4280-4e83-a43f-707ff42d5b0a'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable crefiles31cense

<!-- PAGE BREAK -->

<a id='e7a0e056-c438-4a4d-8c98-57344368cbc2'></a>

Mathematical Methods in the Applied Sciences

<a id='f371d215-2fd0-489a-a66a-53169cb537fb'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='65175202-89fe-4b62-84cd-d827f80826de'></a>

<table><thead><tr><th>Parameter</th><th>Biological meaning</th></tr></thead><tbody><tr><td>r</td><td>Intrinsic growth rate of the tumor</td></tr><tr><td>K</td><td>Carrying capacity of the tumor</td></tr><tr><td>δ</td><td>Maximum tumor killing rate by cytokine</td></tr><tr><td>m</td><td>Half saturation constant of the tumor killing rate</td></tr><tr><td>β</td><td>Maximum CD4<sup>+</sup> production rate (antigenicity of the tumor)</td></tr><tr><td>k</td><td>Half saturation constant of the CD4<sup>+</sup> production rate</td></tr><tr><td>a</td><td>Death rate of the CD4<sup>+</sup> cells</td></tr><tr><td>α</td><td>Maximum production rate of cytokine</td></tr><tr><td>b</td><td>Half saturation constant of the cytokine production rate</td></tr><tr><td>μ</td><td>Cytokine loss rate</td></tr><tr><td>I₁</td><td>Treatment by CD4<sup>+</sup></td></tr><tr><td>I₂</td><td>Treatment by cytokine</td></tr></tbody></table>

<a id='960db3bb-ac1b-46c3-a235-77a4b7150bc9'></a>

t large, and we may assume x(t) < K for all t ≥ 0. Let a0 = min {a, µ} > 0, and let T = y + z. Then, T' ≤ (A − a0)T + I1 + I2, where
A = βK/k+K + αK/b+K. Consider now W' = (A − a0)W + I1 + I2 with W(0) = T(0). Because W(t) is defined and bounded on any interval
[0, t0], 0 < t0 < ∞, and T(t) ≤ W(t), we conclude that y(t), z(t) are defined for all t > 0, and hence, the solution is defined and remain
nonnegative for t > 0.
■

<a id='3ab8dcbc-b320-4404-9a95-d63155f33297'></a>

## 2.2. The model without treatment
In this subsection, we assume that there are no treatments and investigate the dynamics of the tumor, CD4$^+$, and cytokine interactions. That is, we first consider the following system:

$$\begin{cases}x' = rx(1 - x/K) - \frac{\delta xz}{m + x} \\ y' = \frac{\beta xy}{k + x} - ay \\ z' = \frac{\alpha xy}{b + x} - \mu z,\end{cases}\quad(3)$$

<a id='4c4b56b5-5787-4388-b385-2a2d2513aeee'></a>

with nonnegative initial conditions. Clearly, solutions of (3) exist for all t > 0 and remain nonnegative by Proposition 2.1. Model (3)
has two boundary steady states E₀ = (0,0,0) and E₁ = (K, 0, 0), which exist for all parameter values. Their local stability can be easily
determined by the Jacobian matrix J of (3) evaluated at the steady state, given respectively by

<a id='832ff1ef-cb6c-4925-8318-291110688423'></a>

J(E_0) = 
```
⎛ r  0  0 ⎞
⎜ 0 -a  0 ⎟
⎝ 0  0 -μ ⎠
```

<a id='a3415e7d-9ce9-4199-913c-3d6b50c79feb'></a>

<::J(E1) = 
$$\begin{pmatrix}
-r & 0 & -\frac{\delta K}{m+K} \\
0 & \frac{\beta K}{k+K} - a & 0 \\
0 & \frac{\alpha K}{b+K} & -\mu
\end{pmatrix}$$
: equation::>

<a id='bee1a846-9bc3-4caa-95bf-b424a20b50bc'></a>

Therefore, E₀ = (0, 0, 0) is a saddle point with stable manifold lying on the nonnegative yz-plane. This indicates that the tumor may not be eliminated completely without any treatment even if it is very small. Steady state E₁ = (K, 0, 0) is locally asymptotically stable if

β < a(k + K) / K and unstable if β > a(k + K) / K. Denote

βc := a(k + K) / K (4)

<a id='dcdd269e-aaa7-4368-a1c8-a47ba97df9b2'></a>

The following theorem shows that the tumor will grow to its maximum size K if β is below the critical value βc.

<a id='8c1a5cf3-7162-4fb5-8d20-e7ea1008c25f'></a>

Theorem 2.2
System (3) has two boundary steady states E_0 = (0,0,0) and E_1 = (K, 0, 0), where E_0 is a saddle point and E_1 is asymptotically stable if β < β_c and a saddle point if β > β_c. Moreover, E_1 is globally asymptotically stable in {(x, y, z) ∈ R^3_+ : x > 0} if β < β_c.

<a id='df2e0879-432f-4344-b41f-5d2c22eba4fe'></a>

4332

<a id='b0ec7919-1091-4b8b-a166-7733ad6671cc'></a>

--- Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='64fccf6a-027b-4dab-ba55-ce364baba085'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<a id='c573310b-1999-4cd3-9003-f1291590f9db'></a>

and

<a id='0bed4ebe-2a0b-4d0b-9aea-0ec392f48572'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<!-- PAGE BREAK -->

<a id='992a5968-98aa-4e15-9861-7edc09624984'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='20646edb-a673-4632-9e89-6af89d4a97d3'></a>

Mathematical
Methods in the
Applied Sciences

<a id='643595fa-ede7-4121-b684-26287d03eb3f'></a>

Proof
We only need to prove the last statement. Let β < βc. Observe that E₁ is locally asymptotically stable and the x-component of solutions of (3) satisfies lim sup x(t) ≤ K. Therefore, for any ε > 0, there exists t₀ > 0 such that x(t) < K + ε for all t ≥ t₀. By the assumption
t→∞
β < βc, we can choose ε > 0 so that β(K + ε) / (k + K + ε) < a. It follows from the second equation of (3) that y'(t) < (β(K + ε) / (k + K + ε) - a)y for
t ≥ t₀, and hence, limt→∞ y(t) = 0. Therefore, limt→∞ z(t) = 0, limt→∞ x(t) = K if x(0) > 0, and E₁ is globally asymptotically stable in {(x,y,z) ∈ ℝ³: x > 0}.
□

<a id='2794ac46-3350-4cb4-b120-4fc1b86e89df'></a>

If y(0) = 0, then y(t) = 0, and hence, limt→∞ z(t) = 0 and limt→∞ x(t) = K. Therefore, the stable manifold of E₁ is the nonnegative xz-coordinate plane when β > βc, where βc depends on the CD4+'s death rate a, half saturation constant k of the CD4+ production, and the tumor's carrying capacity K. If either a or k is small, then βc is small, and it is more likely for β to exceed βc. Because K is the tumor's maximum size, one would wish E₁ to be unstable. Therefore, a smaller parameter value of a or k or both would be beneficial to the individual carrying the tumor.

<a id='b8460a83-be6f-4044-9cf1-ec38dba43507'></a>

Assume now β > βc. An interior steady state (x*, y*, z*) of (3) can be solved explicitly via

x* = ak / (β-a),
z* = r/δ (m + x*) (1 - x*/K),
y* = μz* (b + x*) / (αx*).
(5)

<a id='4c37fc7c-9243-4fd0-b71d-10c02b3b86be'></a>

Because β > βc implies β > a, and so, x* > 0. Moreover, z* > 0 is equivalent to β > βc by a direct computation. Therefore, system (3) has a unique interior steady state E* = (x*, y*, z*) if and only if β > βc, where x* < K. The tumor size in the interior steady state is always smaller than its carrying capacity.
Suppressing the stars in the components of the interior steady state, the Jacobian matrix of (3) at E* is given by

<a id='70f9223b-7ae4-47f0-800e-1c714668d412'></a>

$$J(E^*) = \begin{pmatrix} j_{11} & 0 & j_{13} \\ j_{21} & 0 & 0 \\ j_{31} & j_{32} & -\mu \end{pmatrix}, \quad (6)$$

<a id='528ff80c-f0b1-4ecd-88ea-323eb8c5aea2'></a>

with

$j_{11} = r\left(1 - \frac{2x}{K}\right) - \frac{\delta mz}{(m + x)^2}$, $j_{13} = -\frac{\delta x}{m + x}$, $j_{21} = \frac{\beta ky}{(k + x)^2}$

$j_{31} = \frac{\alpha by}{(b + x)^2}$, $j_{32} = \frac{\alpha x}{b + x}$

<a id='d50caa61-be06-4082-93ef-faf30bae69a6'></a>

After some computations, the characteristic polynomial is
P(λ) = λ³ + a₁λ² + a₂λ + a₃,

<a id='6019b5c8-2045-4ca8-b7ff-c9c3e89af94f'></a>

where
$a_1 = \mu - j_{11}$, $a_2 = - (\mu j_{11} + j_{13}j_{31})$, $a_3 = -j_{21}j_{13}j_{32}$. (7)

<a id='8d6d35cc-2f79-4d0c-b380-38f2ad9a16a3'></a>

Because j13 < 0 and j21, j32 > 0, the coefficient a3 > 0. Observe that when β > βc and β is close to βc, x* < K and x* is close to K.
Therefore,

<a id='a6f6362a-fa8e-4667-9633-dd563092aac7'></a>

$$j_{11} < r\left(1 - \frac{2x^*}{K}\right) \approx -r < 0,$$

<a id='719f1e67-bf4f-4d91-9395-4bb0b9742306'></a>

and thus all the other coefficients $a_1$ and $a_2$ are positive. Moreover,

<a id='af4cc82b-cd8c-4dd7-90c3-920aba8754c5'></a>

$P(0) = a_3 > 0, \lim_{\lambda\to\infty} P(\lambda) = \infty, \lim_{\lambda\to-\infty} P(\lambda) = -\infty.$

<a id='a7022937-1db5-48cf-a59d-654c21320e43'></a>

It follows that P(λ) = 0 has at least one negative real root. Because all the coefficients of P(λ) are positive, Descartes' rule of signs [19] implies that P(λ) = 0 has no positive real roots. On the other hand, P(−λ) = −λ³ + a₁λ² – a₂λ + a₃, and so, P(λ) = 0 has either one or three negative real roots by the Descartes' rule of signs [19]. If there are three negative real roots, then E* is locally asymptotically stable. If there is only one negative real root, then the other two roots are complex numbers. In the following, we show that E* is locally asymptotically stable when β > βc and β is close to βc.

<a id='49452aef-33b3-4e26-b750-9004a4e647fd'></a>

Because a₁ > 0 and a₃ > 0, the Routh-Hurwitz criteria [19] imply that E* is locally asymptotically stable if a₁a₂ > a₃ holds or equivalently

<a id='6686a1f4-4295-4018-9ac5-2d50cf717d02'></a>

(rx(K - m - 2x) - μK(m + x)) (x(K - m - 2x)(b + x) - b(K - x)(m + x)) > βkx(K - x)(m + x)²(b + x)(k + x)².

<a id='fe1e95da-3812-463c-a112-08f29f7ea2a4'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='ff8dc01c-7fa1-4e95-aea1-303cc48855b9'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='685568fc-550d-43b4-bba2-95dace011b81'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable cregies 33
cense

<!-- PAGE BREAK -->

<a id='93282db2-f65c-460f-b4fb-306a8b68cb07'></a>

Mathematical
Methods in the
Applied Sciences

<a id='bd652834-0825-4b1a-a8e1-b23a0bc1f2b5'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='f45529c6-ccc9-43aa-8e3b-a0aad710ddfd'></a>

<::chart: The image contains three plots. Plot (a) is a line graph titled "The maximum real parts of the eigenvalues of J(E*) for system (3)". The x-axis is labeled "β" and ranges from 0 to 0.8. The y-axis is labeled "maximum of Re(λ)" and ranges from -5 x 10^-3 to 5 x 10^-3. A red curve is plotted, starting near 0, rising to a peak around β=0.2, and then decreasing. A green horizontal line is at y=0. Plot (b) is a line graph showing "time evolutions of the tumor with initial condition (0.5, 1.0, 0) for system (3)". The x-axis is labeled "days" and ranges from 0 to 3000. The y-axis ranges from 0 to 1000. There are three curves: a dashed blue line for β=0.12, a dashed red line for β=0.15, and a dotted gray line for β=0.2. These curves show initial growth followed by oscillations, with different frequencies and amplitudes. Plot (c) is a line graph showing "plots R(x) and L(x) given in Equation (10) when m + b - k < 0 for system (8)". The x-axis is labeled "x" and ranges from 0 to 400. The y-axis ranges from 0 to 1.5. A dashed blue line represents R(x), starting high and decreasing exponentially. A solid red line represents L(x), starting high and decreasing linearly.::>

<a id='eb7bbb81-6b0d-488b-abec-201295086640'></a>

After multiplying both sides by (k + x), the right hand side of the previous inequality is close to 0 because x* is close to K but the left hand side is approximately K(m + K)(r + )(b + K)(k + K) > (r + )K > 0. Therefore, a1a2 > a3 holds and E* is locally asymptotically stable when  > c and  is close to c. Let o > c denote the  value for which E* is stable when  (c, o) and unstable if  > o. We denote o =  if E* is stable for all  > c. If o < , then it is expected that a Hopf bifurcation [20] occurs at  = o and system (3) has positive periodic solutions.
Figure 1(a) plots the maximum real parts of the eigenvalues of J(E*) by varying  with

<a id='7644e0fe-74c7-4e0d-8ebf-31fdc4602b15'></a>

α = 0.01, a = 0.03, b = 10², δ = 0.1, k = 10³, μ = 50, m = 10², K = 10³, r = 0.01.

<a id='11a2bf07-8d99-4cce-8770-02646c858f9c'></a>

In this example, βc = 0.06 and β ranges from 0.065 to 0.95 in Figure 1(a). We see that E* is stable when β is close to βc, which conforms with our analytical finding. We calculate β0 numerically with β0 = 0.113. The interior steady state is unstable when β > β0, and it becomes stable again as β is increased further as shown in Figure 1(a). We denote the β value for which E* is stable after passing β0 by β1. In this numerical example, β1 is approximately 0.248. Because x* is a decreasing function of β by (5), the tumor can be stabilized in a small size if β is large.

<a id='8009ba5f-d9fe-4ca9-ba6b-e88cf3844836'></a>

Parameter β can be interpreted as the antigenicity of the tumor. If this parameter is less than βc, then the tumor will grow to its carrying capacity over time when there is no treatment. Because βc is an increasing function of a and k, it is desirable to have a smaller a or k so that β can easily exceed βc and the tumor may be oscillating with a smaller maximum size as illustrated in Figure 1(b) where β ε (β0, β1).

<a id='f3e98558-02c1-4452-bc2c-8f3308021091'></a>

### 3. Models with treatment and analysis
In this section, we adopt immunotherapy to study its effects on the tumor regression. In Section 3.1, the treatment by CD4+ is considered. The treatment by cytokine is discussed in Section 3.2.

<a id='803199f2-b608-484a-b3fa-10466c4b6af1'></a>

3.1. _The model with treatment of CD4+_
The interaction between tumor, CD4+, and cytokine with treatment of CD4+ T cells based on model (3) is given by the following system:

<a id='d68ab742-d4db-4646-afc3-dfd98e88b4d5'></a>

x' = rx(1 - x/K) - δxz / (m + x)
y' = βxy / (k + x) - ay + l₁
z' = αxy / (b + x) - μz
(8)

<a id='953c4981-3876-4a69-85f2-0ee6090ea200'></a>

4334

<a id='92ca3da4-bc57-4d16-92bb-8aed59426ede'></a>

--- 
Copyright  2014 John Wiley & Sons, Ltd.

<a id='e01643fe-0658-4fa4-ba00-397faf56e0e9'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='262e16ad-bb97-42e7-84bb-b08fe3f189f9'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='71147541-0b53-47b2-b240-93dc90f2d817'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='12fa6c0a-d499-46a4-b286-e3de2929979e'></a>

Mathematical
Methods in the
Applied Sciences

<a id='182dd233-1ff2-47b3-9c23-971d48fae9d2'></a>

with nonnegative initial conditions, where I₁ > 0 denotes the immunotherapy by adopting constant volume I₁ of CD4⁺ T cells into the tumor site of the patient per unit time.
Clearly solutions of (8) exist for all t > 0 and remain nonnegative by Proposition 2.1. Because x' ≤ rx(1 − x/K) and y' ≥ −ay + I₁,
solutions of (8) satisfy

<a id='1cbf4e73-f498-4ef5-9ef2-979bf8e6425f'></a>

lim sup x(t) ≤ K and lim inf y(t) ≥ l₁
t→∞                     t→∞       a

(9)

<a id='2b049544-b728-48c8-a6d9-313ef428cc17'></a>

There exists only one boundary steady state $E_2 = \left(0, \frac{l_1}{a}, 0\right)$ and its stability depends on the Jacobian matrix evaluated at $E_2$,

$J(E_2) = \begin{pmatrix}
r & 0 & 0 \\
* & -a & 0 \\
0 & 0 & -\mu
\end{pmatrix}$

<a id='578e2147-c3fb-4c30-ab8f-9b5e500151c5'></a>

where * is an unimportant term. It follows that E₂ is always a saddle point. Notice if x(0) = 0, then x(t) = 0 for t > 0, lim_{t→∞} z(t) = 0 and lim_{t→∞} y(t) = I₁/a, that is, the stable manifold of E₂ lies on the nonnegative yz-coordinate plane. This indicates that the tumor may not be eliminated completely even with the immunotherapy by adopting CD4⁺ T cells to boost the immune response. However, the steady state (K, 0, 0) where the tumor is at its carrying capacity is not present in this model. Therefore, the tumor can never grow to its maximum size with the treatment of CD4⁺ T cells.

<a id='41c6570a-76e8-4985-a3a8-3e9ae518976f'></a>

To determine the existence of an interior steady state (x, y, z), we set x' = y' = z' = 0 and assume x, y, z > 0. Then, the x component satisfies

<a id='e45336f5-10e5-4091-b850-37bb513dc7b6'></a>

$\mu r(1 - \frac{x}{K}) ((a - \beta)x + ak) = \frac{\alpha\delta l_1 x(k + x)}{(m + x)(b + x)}$ (10)

<a id='8994abc3-4fa8-4eab-b0da-3a5692ca05ed'></a>

and the y and z components are given in terms of x via

<a id='962835ea-ad81-4ab7-ba24-3cf38d915ff9'></a>

y = \frac{I_1(k + x)}{(a - \beta)x + ak}, z = \frac{\alpha I_1x(k + x)}{\mu(b + x)((a - \beta)x + ak)} (11)

<a id='5342b5d9-7fa5-4790-a193-444d88caca77'></a>

It is clear that any positive solution x of (10) will result in an interior steady state if x < K and (a - ̘)x + ak > 0. Let the left hand side and the right hand side of (10) be denoted by L(x) and R(x) respectively. Then,

<a id='433843eb-ba8d-4c54-99bd-65e467b0fd96'></a>

R'(x) = αδI₁ \frac{(m + b - k)x² + 2mbx + mbk}{(m + x)²(b + x)²}, R(0) = 0, \lim_{x→∞} R(x) = αδI₁.

<a id='7b4e3993-4345-44d0-92ab-8a69915fbe39'></a>

On the other hand, L(x) is either a concave up or a concave down parabola depending on whether a < β or a > β respectively and it
is a line if a = β. Moreover,
L(K) = 0 and L(0) = rakμ > 0.

<a id='a9480e84-1308-4975-b2ea-897fad30c751'></a>

Therefore, (10) has at least one positive solution x that is less than K and satisfying (a - β)x + ak > 0. It follows that system (8) has at least one interior steady state. Because R(x) is strictly increasing if m + b - k ≥ 0, we can conclude that system (8) has a unique interior steady state if in addition a ≥ β. If m + b - k ≥ 0 and a < β, then (10) has two positive solutions but only one of them is less than K. Therefore, (8) has a unique interior steady state whenever m + b - k ≥ 0. If m + b - k < 0, then R'(x) = 0 has only one positive root x+, where

<a id='1d9abb76-c397-4df4-a11b-e90de74c643a'></a>

x+ = 2mb + √4m²b² - 4mbk(m + b - k) / 2(k - m - b) (12)

<a id='d2d6c3da-6a38-4b3b-a551-87995e43eacc'></a>

It can be shown that system (8) either has one, two, or three interior steady states depending on the parameter regimes. We summarize the previous discussion.

<a id='8515d098-0a59-40e1-a1f5-9c4d5a7d66a4'></a>

Proposition 3.1

System (8) has a unique boundary steady state E2 = $(0, \frac{l}{a}, 0)$, which is always a saddle point. System (8) has a unique interior steady state if $m + b - k \geq 0$. If $m + b - k < 0$, then (8) has either one, two or three interior steady states.

<a id='ec41a1a9-ff2a-42d7-8332-c662afb06a04'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='a431ade1-8773-424c-88cb-ac32e7767919'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='352ae8bb-7d19-4dbb-9f21-6738bdaecc27'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Crea
s License

<!-- PAGE BREAK -->

<a id='f9fc1972-3914-4423-b8b0-f2e5ce185ba7'></a>

Mathematical
Methods in the
Applied Sciences

<a id='cc72bb2c-6d77-4bba-a357-2a12d62e771f'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='10010cc4-2850-41c0-bc6e-f1e0775159c8'></a>

We provide a graph to illustrate existence of three interior steady states for system (8). Let

<a id='ad1ddd25-a7de-457e-bada-d58e4106af0b'></a>

I_1 = 267, α = 0.01, a = 0.03, b = 1, δ = 0.01, k = 10^3, μ = 50, m = 10, K = 10^3, r = 0.001, β = 0.1.

<a id='a1123ddc-7fd8-4ea3-87f7-60b89ae36312'></a>

Then, a < β and m + b - k < 0. Figure 1(c) plots the two curves y = R(x) and y = L(x) given in (10). There are three positive intersections and each of which is less than K with (a - β)x + ak > 0 so that there are three interior steady states for model (8). The tumor size is small for the first two interior steady states.

<a id='261f97e3-8a9d-47da-8852-27b2fbc56912'></a>

As the model may have up to three interior steady states and the number of the interior steady states with respect to the model parameters is not easy to determine analytically, we will study the model numerically in Section 4. Let E* = (x, y, z) be an interior steady state of system (8). The Jacobian matrix of (8) is the same as the Jacobian matrix of (3), however, the Jacobian matrix evaluated at an interior steady state is different. Indeed, the Jacobian matrix of (8) evaluated at E* has the following form

<a id='047504d8-7fec-4b3c-bd5b-f2281d5e09aa'></a>

J(E*) = 

$$\begin{pmatrix} j_{11} & 0 & j_{13} \\ j_{21} & j_{22} & 0 \\ j_{31} & j_{32} & -\mu \end{pmatrix}, \quad (13)$$

<a id='a3d2ff26-1277-4c77-817d-4ddd03df133b'></a>

where

j₁₁ = r(1 - 2x/K) - δmz/(m + x)², j₁₃ = -δx/(m + x), j₂₁ = βky/(k + x)²

<a id='b605a46f-fd07-4ca2-8321-1d4ee6f0a586'></a>

j22 = βx / (k + x) - a, j31 = αby / (b + x)², j32 = αx / (b + x).

<a id='73f566d9-0869-42cb-8b2e-856798b3fb75'></a>

Because j₂₂ can be rewritten as j₂₂ = -\frac{(a - \beta)x + ak}{k + x}, we have j₂₂ < 0. The characteristic polynomial of J(E*) is Q(\lambda) = \lambda³ + a₁\lambda² + a₂\lambda + a₃, where

<a id='e10a3d23-da67-4800-891a-ee0baf81567f'></a>

a1 = -(j11 + j22 - μ), a2 = -(j13j31 + μj22 + μj11 - j11j22),

<a id='5a533290-f60f-4eab-a1a7-4ecad14ff75e'></a>

a_3 = -j_{32}j_{21}j_{13} + j_{31}j_{11}j_{22} + \mu j_{11}j_{22}.

<a id='422d62a4-7e2e-4c28-a501-59a6021acdd8'></a>

If $j_{11} < 0$, then $a_i > 0$ for $i = 1, 2, 3$. Applying the Routh-Hurwitz criteria [19], the interior steady state is locally asymptotically stable if $a_1a_2 - a_3 > 0$, where

<a id='c8c4337e-ef48-4790-9ad8-ead92b2e05a0'></a>

a₁a₂ - a₃ = -µj₃₁j₁₃ - µ²j₁₁ + µj₂₂j₁₁ - j₂₂²j₁₁ + j₁₁j₁₃j₃₁ + µj₁₁² - j₂₂²j₁₁ + j₃₂j₂₁j₁₃.

<a id='378cb298-e3cf-42ac-8bdf-13db0bc858d1'></a>

Notice under the assumption j₁₁ < 0 that every term in the expression of a₁a₂ − a₃ is positive except the last term, where j₃₂j₂₁j₁₃ can be shown to be

<a id='bfb6ef65-1a54-4693-81c4-a69f70a8d660'></a>

j32j21j13 = - βkrx(1 - x/K) / μ(k + x)² < 0.

<a id='fe331f68-d807-4394-8314-61a19cd38f4b'></a>

However, if x is close to K, then j11 < 0 and j32j21j13 ≈ 0 and such an interior steady state is therefore locally asymptotically stable. As a consequence, the interior steady state (x, y, z) with x sufficiently close to K is always asymptotically stable.
It is expected that when system (8) has two interior steady states, then the two curves y = R(x) and y = L(x) are tangent at one of the two intersections and the resulting steady state is non-hyperbolic. If (8) has three interior steady states, then it is very likely that two of them are locally asymptotically stable and the other is a saddle point so that the model exhibits bi-stability. In such a case, the tumor can stabilize at two different levels depending on initial conditions. The two locally asymptotically stable interior steady states may loss their stability, and then, the model has periodic solutions.

<a id='705850ea-fdd1-4fdb-9068-2b1eb672e196'></a>

3.2. _Treatment with cytokine_

If treatment by cytokine is adopted, then the interaction is described by the following system:

$$\begin{cases}
x' = rx(1 - x/K) - \frac{\delta xz}{m + x} \\
y' = \frac{\beta xy}{k + x} - ay \\
z' = \frac{\alpha xy}{b + x} - \mu z + I_2
\end{cases} \quad (14)$$

<a id='e0a61735-5b20-4a11-b1d2-d5b30c2ea2aa'></a>

4336

<a id='505761d5-86ec-463d-a42c-6972f7e45058'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='9a997a13-1e0c-462e-981a-4a1189b955e2'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='6d2d8a69-e719-4064-b519-6f5ae0f147e2'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<a id='bc96ad5e-4a47-464a-816e-a4a176925095'></a>

and

<!-- PAGE BREAK -->

<a id='7986aa5e-c9a6-446e-b2d2-3b0a0098a98b'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='9858f5d5-7f70-4035-93a0-b7f14efe0825'></a>

Mathematical Methods in the Applied Sciences

<a id='0054c1a4-79c6-4eac-9764-728f1fee41f4'></a>

where I₂ > 0 denotes the immunotherapy by adopting constant I₂ volume of cytokine into the tumor site of the patient per unit time. It is clear that solutions of (14) exist for t > 0 and remain nonnegative by Proposition 2.1. Moreover, as x' ≤ rx(1 − x/K) and z' ≥ −μz + I₂, the x and z components of any solution of (14) satisfy

<a id='6107f431-be1a-4ddd-bb80-8dec445eaaf7'></a>

$\lim_{t\to\infty} \sup x(t) \le K \text{ and } \lim_{t\to\infty} \inf z(t) \ge \frac{l_2}{\mu}.$ (15)

<a id='7bbce04a-553c-42b1-ae3e-25f4197ba25e'></a>

Noticing $\frac{\beta K}{k+K} < a$ is equivalent to $\beta < \beta_c$, where $\beta_c = \frac{a(k+K)}{K} > a$ is defined in (4). If $\beta < \beta_c$, then by (15) one can prove that solutions $(x(t), y(t), z(t))$ satisfy $\lim_{t\to\infty} y(t) = 0$. Therefore, we assume $\beta > \beta_c$ and consequently $\beta > a$ in the following discussion.

<a id='ca609b02-f01a-4116-86b9-fca3bb981af5'></a>

There exists a trivial steady state E₃ = $(0, 0, \frac{b}{\mu})$, where the tumor is extinct. Its stability depends on the following Jacobian matrix evaluated at E₃,

<a id='f9996333-9dff-4fa6-b98c-48f9c9121edb'></a>

$$J(E_3) = \begin{pmatrix} r - \frac{\delta I_2}{m\mu} & 0 & 0 \\ 0 & -a & 0 \\ 0 & 0 & -\mu \end{pmatrix}\text{ (16)}$$

<a id='5a9af1de-a13f-4e08-8e34-92bca1ea442f'></a>

We conclude that E3 is locally asymptotically stable if rmu < δI2 and unstable when rmu > δI2. As a result, if the treatment I2 is large or if the tumor's intrinsic growth rate r is small, then the tumor can be eliminated completely when its size is very small.
If y(0) = 0, then y(t) = 0 for all t > 0, and (14) is asymptotic to the following xz-subsystem:

<a id='a664d188-7680-45d2-8cc1-1acd9826324b'></a>

{ x' = rx(1 - x/K) - δxz / (m + x)
z' = -μz + I₂.
(17)

<a id='4a95057d-90f9-4bc8-aaeb-246f2c72c013'></a>

The z component of the solutions of (17) satisfies $lim_{t→∞} z(t) = \frac{l_2}{\mu}$, and thus (17) reduces to the scalar equation

<a id='f381c1c4-9b1a-4c54-9b40-0395887d4dba'></a>

x' = rx(1 - x/K) - \frac{\delta xl_2}{\mu(m + x)}

(18)

<a id='61f103b1-05f6-4caf-a5b3-920e7d1195c2'></a>

Clearly 0 is a steady state of (18) and a positive steady state x satisfies

<a id='c3607264-3aad-45bf-b5f5-faf1f8cfa6b8'></a>

1/(m+x) (-r/K x^2 + r/K (K-m)x + rm - δI_2/μ) = 0, (19)

<a id='43a00455-3b0a-405b-8400-1654e9d2ca6d'></a>

which has the following two solutions

$x^{\pm} = \frac{(K-m) \pm \sqrt{(K-m)^2 + \frac{4K}{r}\left(rm - \frac{\delta I_2}{\mu}\right)}}{2}$ (20)

<a id='01b0355c-5c97-42b8-bdfa-30866201ceeb'></a>

Denote
$I_2^c = \frac{\mu r}{\delta} \left( \frac{(K-m)^2}{4K} + m \right)$ (21)

<a id='2c0b8c4d-5b57-4af5-9ba3-a3a90fcb2c00'></a>

and observe that $l_2 > \frac{\mu rm}{\delta}$. Then, $x^{\pm}$ are complex numbers and thus are not biologically feasible if $l_2 > l_5$ and consequently 0 is the only steady state for (18). The number of steady states of (18) depends on parameter regimes. Because $l_2$ is the parameter for treatment, it is very unlikely that $l_2 = \frac{rm\mu}{\delta}$ occurs, and therefore, we do not discuss this case. We summarize the existence and stability of the steady states for (18) in the following table, where LAS denotes local asymptotic stability. Because the proof is straightforward, it is omitted.

<a id='c8478d15-dd08-41d1-9199-4ea0a15ea719'></a>

It is omitted.
In addition to E3 = (0, 0, I2/μ), Table II implies that system (14) may have other boundary steady states of the form E⁻ = (x⁻, 0, I2/μ)

<a id='c4a5b5d5-1ab9-43f9-b33b-f9de5510226d'></a>

and $E^+ = (x^+, 0, \frac{l^2}{\mu})$ depending on the parameter regimes. Furthermore, stability of $E^-$ and $E^+$ is determined by the Jacobian matrix

<a id='f8111303-81ec-4e2b-a3f7-2e4fdf2cfd5f'></a>

<::transcription of the content
: $\begin{pmatrix} j_{11} & 0 & j_{13} \\ 0 & j_{22} & 0 \\ 0 & j_{32} & -\mu \end{pmatrix}$,
::>

<a id='9f08644c-97dd-4aea-8ee2-81fbce4aa206'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='3d03fd2e-39b1-4e07-bd87-68077bb8bbc6'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='a440b86f-75f4-4671-8bd3-ccbc49cfac6d'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Cro 433

<a id='4cf7dd9d-c510-4f99-8196-b29b714b086b'></a>

Creative Commons License
4337

<!-- PAGE BREAK -->

<a id='9ed62c31-51db-4fc9-a2df-a7af2c93d2d0'></a>

Mathematical Methods in the Applied Sciences

<a id='6ad30fe3-4e53-4cca-8fb8-955e65b3b04e'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='a1f0d2c7-452c-4a9a-88ee-dba1358735c3'></a>

<table id="8-1">
<tr><td id="8-2" colspan="3">Table II. Existence and stability of steady states of (18).</td></tr>
<tr><td id="8-3">Parameter regime</td><td id="8-4">Steady state</td><td id="8-5">Stability</td></tr>
<tr><td id="8-6">l₂ &lt; ᵐ⁄₈</td><td id="8-7">0, x⁺</td><td id="8-8">0 unstable, x⁺ LAS</td></tr>
<tr><td id="8-9">l₂ &gt; ᵐ⁄₈, K ≤ m</td><td id="8-a">0</td><td id="8-b">LAS</td></tr>
<tr><td id="8-c">l₂ &gt; ᵐ⁄₈, K &gt; m, l₂ &lt; l₂ᶜ</td><td id="8-d">0, x⁻, x⁺</td><td id="8-e">0 LAS, x⁺ LAS, x⁻ unstable</td></tr>
<tr><td id="8-f">l₂ &gt; l₂</td><td id="8-g">0</td><td id="8-h">O LAS</td></tr>
</table>

<a id='156e3202-5ec0-4614-87c4-f63447bd1445'></a>

where all the nonzero entries are evaluated at the steady state. In particular, j22 = βx / (k+x) - a and using r (1 - x/K) = δl2 / μ(m+x) at the steady state, we have

j11 = r(1 - 2x/K) - δml2 / μ(m+x)² = rx(K - m - 2x) / K(m + x)

<a id='d4ca92c6-ddd0-4da8-bf1f-109a7e2f98d6'></a>

Therefore, $j_{11} > 0$ at $E^-$ and $j_{11} < 0$ at $E^+$ by (20) whenever they exist. It follows that $(x^-, \frac{l_2}{\mu})$ is a saddle point and $(x^+, \frac{l_2}{\mu})$ is locally asymptotically stable for (17).

<a id='d8deaf76-7425-4c96-ab1d-4f9f45b7b4eb'></a>

Because cytokine has a deleterious effect on the tumor's growth rate as modeled in the first equation of (14), it is possible to eliminate the tumor completely if the dose I₂ of treatment by cytokine is large as shown subsequently.

<a id='b6c7ed46-e42c-47b7-96fb-b574c2f5bd29'></a>

Theorem 3.2
Steady state $E_3 = (0, 0, \frac{I_2}{\mu})$ is globally asymptotically stable in $\mathbb{R}^3_+$ for system (14) if either (a) $rm\mu < \delta I_2$ and $K \le m$, or (b) $I_2 > I_2^c$ holds.

<a id='4e0ab364-7e18-426e-96a7-ffe800478cc8'></a>

Proof
By (15), given any ε > 0, there exists t₀ > 0 such that z(t) > $\frac{l_2 - \epsilon}{\mu}$ for t ≥ t₀. We can choose ε > 0 sufficiently small so that rmμ < δ(l₂ - ε) for the proof of (a) and l₂ - ε > $l_2^c$ for the proof of (b). Observe that by (19)

<a id='410b8e5e-124f-4fce-89fa-58b81b868c7d'></a>

x'(t) < \frac{x}{m+x} \left( -\frac{r}{K}x^2 + r\left(1 - \frac{m}{K}\right)x + rm - \frac{\delta(l_2 - \epsilon)}{\mu} \right) = xh(x) \quad (22)

<a id='7d520498-b176-4628-8e50-263cb14fba83'></a>

for t ≥ t₀. To prove (a), notice that h(x) < 0 for x ≥ 0 and in particular,

<a id='f8587e15-bbd5-42b3-98b0-684547825951'></a>

x'(t) ≤ (x / (m+x)) * (rm - (δ(l₂ - ε)) / μ) for t ≥ t₀.

<a id='fe4b1c75-b635-40c1-85b5-78fdd8d8ef36'></a>

Therefore, lim$_{t\to\infty}$ x(t) = 0, and hence, lim$_{t\to\infty}$ y(t) = 0 and lim$_{t\to\infty}$ z(t) = l$_{2}$/\u, that is, E$_{3}$ is globally attracting in R$^{3}_{+}$. It follows that E$_{3}$ is globally asymptotically stable because it is locally asymptotically stable by (16).

<a id='55cd398f-bc87-430f-9cc3-2262fc7dd5c7'></a>

The proof of (b) is trivial by (a) if K ≤ m. If K > m, we rewrite (22) as x'(t) < xh(x) = •̂ / (m + x²) g(x), where g(x) is a concave down

<a id='9256e58f-8db4-4cfe-85f4-db5392315cc1'></a>

parabola with vertex at $\frac{K-m}{2}$ and

$g\left(\frac{K-m}{2}\right) = \frac{r(K-m)^2}{4K} + rm - \frac{\delta(l_2 - \epsilon)}{\mu} < 0.$

<a id='1cce077c-5d5c-4ba7-8a1f-b15cc683d293'></a>

As a result,
x'(t) < x / (m + x) g ( (K - m) / 2 ) < 0 for t >= t₀,

<a id='e9b6792f-2fcc-4053-8f20-933bea28fcf0'></a>

and hence, lim<sub>t→∞</sub> x(t) = 0. Therefore, lim<sub>t→∞</sub> y(t) = 0 and lim<sub>t→∞</sub> z(t) = l<sub>2</sub>/μ, and E<sub>3</sub> is globally asymptotically stable in R<sup>3</sup><sub>+</sub>
by (16). □

<a id='e60fbcd2-305a-4d86-9451-46048f74d3ba'></a>

An interior steady state E = (x*, y*, z*) satisfies

<a id='803e461d-a2bb-44f5-905c-744be47ba34e'></a>

x* = ka / (β - a), y* = (b + x*) / (αx*) (μz* - l₂),
z* = r(1 - x*/K)(m + x*)/δ.
(23)

<a id='f1f56622-c082-45cc-a614-497c29db5288'></a>

<::4338
: figure::>

<a id='3d9e350d-b6eb-43ec-bbd0-1dfa785c84cf'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='dfc066b7-6182-4bff-8bcc-a4d406ddc046'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='7d883dd3-213d-4d03-8d2d-a1a7c56d64c5'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='499857f0-5771-451f-9bcd-622b54c59e25'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='71655b9b-71f2-43c1-a560-755908416a97'></a>

Mathematical Methods in the Applied Sciences

<a id='3de13db1-707b-4e92-8a64-d6feecc1a666'></a>

Thus an interior steady state exists if β > a (which is already assumed), x* = ka / (β - a) < K and μz* > I2. Notice that x* < K is equivalent to β > βc, and hence, it holds trivially. Also, μz* > I2 can be shown to be equivalent to

<a id='1b49119a-3694-4ae0-ab84-c25ed1083ec7'></a>

(μr (Km(β – a)² + (β – a)ka(K – m) – k²a²)) / (δK(β – a)²) > I₂.

<a id='a21f8537-89e8-4799-987a-a6b3590a26d3'></a>

Define
l_2^0 = \frac{\mu r (Km(\beta - \alpha)^2 + k\alpha(\beta - \alpha)(K - m) - k^2\alpha^2)}{\delta K(\beta - \alpha)^2}
(24)

<a id='79ddaa98-f667-48f2-a727-5b74ab47c36d'></a>

Because β > βc is assumed, we have l₂⁰ > 0, and it is straightforward to verify that
l₂⁰ < l₂ᶜ.

<a id='ef93c369-a422-4a3d-a359-31df10d6f525'></a>

We conclude that (14) has an interior steady state if and only if $I_2 < I'_2$, and the interior steady state is unique when it exists.
Stability of boundary steady states is summarized subsequently along with the condition for the existence of an interior steady state.

<a id='a3993589-9aeb-40ca-bc25-af6cfdf0e1ab'></a>

Proposition 3.3
System (14) always has the boundary steady state E3 = (0,0, l2/μ), which is locally asymptotically stable if δI2 > rmμ and is a saddle point if

<a id='b6af626c-c9c9-4c55-b953-3afbe7307236'></a>

δl_2 < rmμ. System (14) may have two other boundary steady states E^± = (x^±, 0, l_2/μ), where E^− is a saddle point. The stable manifold W^S

<a id='f4d924df-0846-4d6b-a696-ef2005173bb7'></a>

of E⁻ is two-dimensional if βx⁻ < a(k + x⁻) and is one-dimensional if βx⁻ > a(k + x⁻). Steady state E⁺ is locally asymptotically stable if βx⁺ < a(k + x⁺) and is a saddle point with a one-dimensional stable manifold Wˢ if βx⁺ > a(k + x⁺). Moreover, (14) has a unique interior steady state if and only if I₂ < I₂⁰.

<a id='bbefb744-56bc-4465-92e6-46fba5bd4f3b'></a>

Recall that I₂ > μrm/δ. Because I₂⁰ can be rewritten as

I₂⁰ = μr/δ (m + (ka(β-a)(K-m) - k²a²)/(K(β-a)²))

<a id='b94aff3c-2472-48f0-b27d-5a92a36b2b8d'></a>

we see that $I_2 > \frac{\mu rm}{\delta}$ if and only if $K-m > \frac{ka}{\beta-a} = x^*$. Consequently if $x^* < K-m$ and $I_2 \in (I_2^0, I_2^0)$, then system (14) has no interior steady state but it has boundary steady states $E_3$ and $E^{\pm}$ by Table II as $K > m$. Moreover, it can be verified that

<a id='ddb7086a-0bbb-4184-9a5a-8afb98c08225'></a>

βx+
k + x+
< a if and only if I₂ > I₂⁰.
(25)

<a id='84ea3025-0c81-4c08-a2ee-24b019f94328'></a>

Therefore, E⁺ is locally asymptotically stable and E⁻ is a saddle point with a two-dimensional manifold. We have the following global dynamics.

<a id='c59c4120-42db-4c07-8434-5cd84db48f77'></a>

Theorem 3.4
If x* < K - m and I₂ ∈ (I₂⁰, I₂ᴷ), then except on a set of initial conditions of Lebesgue 0, solutions of (14) either converge to E₃ = (0, 0, I₂/μ) or
to E⁺ = (x⁺, 0, I₂/μ).

<a id='c234d1e7-927b-4310-a6da-69eb728897a7'></a>

Proof
Because x* < K - m, we have K > m and l₂² > μrm / 𝛿. As l₂ ∈ (l₂⁰, l₂¹), the scalar equation (18) has three steady states 0, x±, and hence, (14) has boundary steady states E₃ and E±. Moreover, solutions of (18) satisfy lim(t→∞) x(t) = 0 if x(0) < x⁻ and lim(t→∞) x(t) = x⁺ if x(0) > x⁻. Thus solutions of (14) satisfy lim sup(t→∞) x(t) ≤ x⁺, where βx⁺ / (k + x⁺) < a by (25). Therefore, for any ε > 0, there exists t₀ > 0 such that x(t) < x⁺ + ε for t ≥ t₀. We can choose ε > 0 such that β(x⁺ + ε) / (k + x⁺ + ε) < a. It follows from the second equation of (14) that

<a id='d5649eb3-fb0a-4d66-a8b1-187ec3b7c69a'></a>

y'(t) < ( β(x⁺ + ε) / (k + x⁺ + ε) - a ) y for t ≥ t₀.

<a id='26761008-25c6-4078-85d0-9c22c7f32ed0'></a>

As a result, lim_{t→∞} y(t) = 0 and solutions of (14) are asymptotic to the solutions of (17). Consequently, except those on the two-dimensional stable manifold W_s of E^−, solutions either converge to E_3 or to E^+. □

<a id='28e67ec0-c871-4690-8b5a-fc959d52bbf5'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='75a1c1f6-1383-4027-abab-95eecc9e8508'></a>

Math. Meth. Appl. Sci. **2015**, 38 4330–4344

<a id='d1f32a69-0ea6-49e3-b66c-5e7ce7196e8a'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Cre339 cense

<!-- PAGE BREAK -->

<a id='8a53c5cd-fa4b-4803-8211-24988e6afd23'></a>

Mathematical
Methods in the
Applied Sciences

<a id='aff7ddda-3c4e-4a0e-8824-6a3ba2a52974'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='f430aea4-b58f-4238-bdba-7b56e63a48d8'></a>

We remark that if x* < K − m and l₂ ∈ ( (μrm) / δ , l₂ ), then (14) has a unique interior steady state and three boundary steady states E₃ and E±, where E₃ is locally asymptotically stable and E± are saddle points. If x* < K − m and l₂ ∈ ( 0, (μrm) / δ ), then the unique interior steady state exists and there are two boundary steady states E₃ and E⁺, where both of the boundary steady states are saddle points.
---
---

<a id='d2c47d77-90b7-4110-987b-c11696b5e7bd'></a>

If $K - m < x^*$, then $I_2^0 < \frac{\mu rm}{\delta}$. If $I_2 \in (\frac{\mu rm}{\delta}, I_2)$, then (14) has no interior steady state. If in addition $K > m$, then (14) has the same dynamical behavior as described in Theorem 3.3. If in addition $K \le m$, then $E_3$ is GAS by Theorem 3.2. If $I_2 \in (I_2^0, \frac{\mu rm}{\delta})$, then (14) has only two boundary steady states $E_3$ and $E^+$, where $E_3$ is unstable. Because $I_2 > I_2^0$, $E^+$ is locally asymptotically stable by (25). Moreover,

<a id='95902adf-af8d-4f63-be5c-ae16a61d08a9'></a>

limₜ→∞ y(t) = 0 and thus E⁺ is globally asymptotically stable in _int_ (R³₊). We now summarize.

<a id='937e7711-20bb-4c2f-bb24-eea227f0fac8'></a>

Theorem 3.5
Let x* > K - m. Then, $l_2^0 < \frac{\mu rm}{\delta}$ and the following statements hold.

<a id='f9aedc9c-49a8-4b34-aba8-5fbfbdd55c5b'></a>

(a) If I₂ \(\in\) \( ( \frac{\mu rm}{8}, I_2 ) \) and K > m, then except on a set of initial conditions of Lebesgue 0, solutions of (14) either converge to E₃ \(= (0,0, \frac{I_2}{\mu}) \)

<a id='6ca89749-ad24-4090-812b-84a38d58b7f3'></a>

or to $E^+ = (x^+, 0, \frac{l_2}{\mu})$.


<a id='f1967895-eb33-43a6-8685-863e4409460c'></a>

(b) If I₂ ∈ (μrm/δ, I₂⁰) and K ≤ m, then E₃ is globally asymptotically stable in ℝ³⁺.
(c) If I₂ ∈ (I₂⁰, μrm/δ), then E⁺ is globally asymptotically stable in int (ℝ³⁺).

<a id='118a1840-89d3-4296-8927-748063498ad3'></a>

If x* > K - m and I₂ ∈ (0,I₂⁰), then (14) has a unique interior steady state and two boundary steady states E₃ and E⁺, where both boundary steady states are saddle points. The following proposition complements Theorems 3.2, 3.4 and 3.5.

<a id='02d4fef9-e9f6-4888-a4f9-7aa44e86b5b7'></a>

Proposition 3.6
If x* < K - m, then (14) has a unique interior steady state E₃* and two boundary steady states E₀ and E⁺ if I₂ ∈ (0, μrm / δ) and has a unique

<a id='f9fcba0c-fe16-4c84-8336-542b6a42da72'></a>

interior steady state E₃* and three boundary steady states E₀ and E± if l₂ ∈ (μrm/δ, l₂⁰). If x* > K − m and l₂ ∈ (0, l₂⁰), then (14) has a unique interior steady state E₃* and two boundary steady states E₀ and E⁺.

<a id='3a0c6b87-e2c7-4b68-b0cf-bfb1c9c3e01f'></a>

When the unique interior steady state E* exists, then the Jacobian matrix of (14) evaluated at E* has the form of (6) and similarly we can verify that E* is LAS if β > βc and β is close to βc. It is expected that a Hopf bifurcation occurs when E* loses its stability. Therefore, when the treatment I2 is not large, then the size of the tumor may be oscillating over time. In addition to have a smaller amplitude, one would also hope that the tumor can be dormant for a longer period of time. We shall use numerical simulations to investigate the scenario.

<a id='ed80ef9b-2515-4444-9fe1-0f4673194700'></a>

## 4. Numerical simulations
Numerical investigations using MATLAB (Mathworks Inc., Natick, MA, USA) are employed in this section to study dynamical behavior of the tumor, CD4$^+$, and cytokine interactions. The time unit is a day and all populations have the unit of volume. The carrying capacity K of the tumor using the data from Kronik et al. [8] is 10³cm³. The intrinsic growth rate r of the tumor is calculated from its doubling

<a id='8de4469f-77cf-4fce-bddd-59a75c2b9ff7'></a>

<table id="10-1">
<tr><td id="10-2" colspan="3">Table III. Default parameter values.</td></tr>
<tr><td id="10-3">Parameter</td><td id="10-4">Default value</td><td id="10-5">Unit</td></tr>
<tr><td id="10-6">r</td><td id="10-7">(0.006, 0.03)</td><td id="10-8">day⁻¹</td></tr>
<tr><td id="10-9">K</td><td id="10-a">10³</td><td id="10-b">cm³</td></tr>
<tr><td id="10-c">δ</td><td id="10-d">0.1</td><td id="10-e">day⁻¹</td></tr>
<tr><td id="10-f">m</td><td id="10-g">1</td><td id="10-h">cm³</td></tr>
<tr><td id="10-i">β</td><td id="10-j">*</td><td id="10-k">day⁻¹</td></tr>
<tr><td id="10-l">k</td><td id="10-m">10</td><td id="10-n">cm³</td></tr>
<tr><td id="10-o">a</td><td id="10-p">(0.01, 0.18)</td><td id="10-q">day⁻¹</td></tr>
<tr><td id="10-r">α</td><td id="10-s">0.1</td><td id="10-t">day⁻¹</td></tr>
<tr><td id="10-u">b</td><td id="10-v">0.1</td><td id="10-w">cm³</td></tr>
<tr><td id="10-x">μ</td><td id="10-y">(47,77)</td><td id="10-z">day⁻¹</td></tr>
<tr><td id="10-A">l₁</td><td id="10-B">*</td><td id="10-C">cm³ day⁻¹</td></tr>
<tr><td id="10-D">l₂</td><td id="10-E">* </td><td id="10-F">cm³ day⁻¹</td></tr>
</table>
'*' denotes varied parameter.

<a id='18b6a15a-3cf7-45dd-9c7d-17bb980c7285'></a>

<::logo: [Unknown Brand]
4340
A vertical blue rectangle with white numbers "4340" oriented sideways.::>

<a id='2282f337-9c2c-4297-8a9a-d1d2dbaf0b0a'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='ea1cfc1b-a573-4cdb-9000-dcf02d638725'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='9819a78b-c528-4755-a668-45a105a7ab2f'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='8d767810-f3c2-4aa2-bc96-12b9d4f92308'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='53e0b820-8c3b-4cdb-89a7-b8936896955c'></a>

Mathematical
Methods in the
Applied Sciences

<a id='4d28d919-51cb-4d3f-80ab-86a03b869162'></a>

<::Figure: Four plots showing time-evolutions of tumor and CD4+ T cells. Each plot has 'days' on the x-axis. The legend in all plots indicates 'tumor' (blue dotted line with circles) and 'CD4+' (green dotted line). The initial condition for all plots is (0.5, 0.01, 0) with β = 0.02. Figure 2. Time-evolutions of tumor and CD4⁺ T cells for system (8) on the left column and for system (14) on the right column. Initial condition is (0.5, 0.01, 0) for all plots with β = 0.02.

(a) Plot titled 'β=0.02, I₁=10, I₂=0'. The left y-axis ranges from 0 to 1, and the right y-axis from 0 to 1000. The tumor population starts at 0.5, peaks around 0.75, then declines to near 0 by 200 days and remains low. The CD4+ population starts near 0, increases to about 500 by 100 days, and then stabilizes.

(b) Plot titled 'β=0.02, I₁=50, I₂=0'. The left y-axis ranges from 0 to 1, and the right y-axis from 0 to 4000. The tumor population starts at 0.5 and rapidly decreases to near 0 within 100 days. The CD4+ population starts near 0, increases to about 2000 by 100 days, and then stabilizes.

(c) Plot titled 'β=0.02, I₁=0, I₂=10'. The left y-axis ranges from 0 to 1000, and the right y-axis from 0 to 0.01. The tumor population starts near 0, increases steadily to about 1000 by 400 days, and then stabilizes. The CD4+ population starts at about 0.01 and rapidly decreases to near 0 within 100 days.

(d) Plot titled 'β=0.02, I₁=0, I₂=50'. The left y-axis ranges from -0.2 to 0.8, and the right y-axis from 0 to 0.01. The tumor population starts at 0.5 and rapidly decreases to near 0 within 100 days, then slightly goes below 0 and stabilizes around 0. The CD4+ population starts at about 0.01 and rapidly decreases to near 0 within 100 days.::>

<a id='709a5424-8818-431f-9a00-d7e188c62d9e'></a>

time and it ranges from 0.00737, 0.021064 in Kronik et al. [8] to 0.02888 in Plesnicar et al. [21]. We therefore use r ∈ (0.006, 0.03). The IL-4's loss rate μ is estimated from its half-life, which is 19 ± 2 min in Conlon et al. [22] and less than 15 min in Perez-Diez et al. [10]. Converting to days, μ is in the range of (47.5301, 76.779). The apoptosis a of CD4⁺ ranges from 0.01 to 0.18 by considering various references [8, 16, 23]. The other parameter values are not easy to determine from the available literature. In the following simulations, we use the values given in Table III with μ = 50, r = 0.027 and a = 0.02.

<a id='592c2a89-8c67-4178-986b-cca12d2fa2ab'></a>

When adopting CD4+ T cells as treatment, we convert the number of cells to volume. According to [24], a single CD4+ cell is approximately 10 µm in diameter, which is 5 × 10⁻⁴cm in radius, and hence, a single CD4+ cell is about 5.3 × 10⁻¹⁰cm³ in volume. In [25, 26], treatments of CTL range from 2 × 10⁹–9.5 × 10¹⁰ and 2.3 × 10¹⁰–13.7 × 10¹⁰ number of cells per infusion, respectively, which are 1.06 cm³ to 72.61 cm³ per infusion.

<a id='bd96f809-1714-4025-9237-d99e38a4fd47'></a>

The critical ̘ value calculated from (4) is about ̘c = 0.0202. Figure 2 provides time evolutions of the tumor cells and CD4+ T cells with ̘ = 0.02 < ̘c = 0.0202. The initial condition for these simulations is (0.5, 0.01, 0). The upper panel uses treatments of CD4+ and the bottom panel uses cytokines. Two different doses of 10 and 50 are considered for both strategies. If dose is small, then it can be seen from Figure 2(a) and (c) that adopting CD4+ T cells to treat the disease is better than using cytokines. If large doses are used, then either treatment is able to suppress the tumor to a low volume as shown in Figure 2(b) and 2(d). The tumor is stabilized as we simulate the model for time up to 5000 days. We only provide the simulation results for the first 500 days. Notice that the tumor may grow to its carrying capacity if small doses of cytokine are applied.

<a id='0fc29bf6-43d0-444c-83e5-3011cd0b5356'></a>

The previous simulations use β that is smaller than βc. We next consider the situation when β = 0.1 > βc = 0.0202 with the same initial condition. If doses of treatments are small, then adopting CD4+ T cells for treatment is also better than using cytokines as shown in Figure 3(a) and (c). The tumor is stabilized again at a very low level when CD4+ T cells are used while the tumor cells grow to a large volume and may be oscillating over time if cytokines are adopted. When the dose of treatment is large, then both immunotherapies are able to suppress the tumor in about 50 days. Comparing Figures 2 and 3, we see that a larger β has a better effect in controlling the tumor.

<a id='d44bde01-a350-4219-a693-acde54147d1c'></a>

Copyright  2014 John Wiley & Sons, Ltd.

<a id='cff0b6ed-dae6-4016-9eed-59111a100f66'></a>

Math. Meth. Appl. Sci. **2015**, 38 4330–4344

<a id='d6e52239-aa81-480c-ac9c-c630354baab1'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Cregions License

<!-- PAGE BREAK -->

<a id='14ef0726-aa08-4467-86fb-f95520cb32f6'></a>

Mathematical
Methods in the
Applied Sciences

<a id='df9ab8ab-64d3-4f7f-9278-17ce28f703a3'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='61590308-eb5b-444a-8b14-09ca00ac0fa4'></a>

<::chart: A 2x2 grid of four line plots, labeled (a), (b), (c), and (d), showing the time evolution of tumor cells and CD4+ T cells. Each plot has 'days' on the x-axis and two y-axes with different scales for 'tumor' (blue dotted line) and 'CD4+' (green dotted line). The legend for each plot indicates '---tumor' and '---CD4+'.

**Plot (a):** Titled "β=0.1, I₁=10, I₂=0". The x-axis ranges from 0 to 500 days. The left y-axis implicitly ranges from 0 to 1 for tumor cells, and the right y-axis implicitly ranges from 0 to 1000 for CD4+ cells. The tumor cell count starts around 0.5, peaks around 0.8 at approximately 50 days, and then decreases to near 0 by 200 days. The CD4+ T cell count starts low, increases to about 500 by 100 days, and then stabilizes.

**Plot (b):** Titled "β=0.1, I₁=50, I₂=0". The x-axis ranges from 0 to 500 days. The left y-axis implicitly ranges from 0 to 1 for tumor cells, and the right y-axis implicitly ranges from 0 to 4000 for CD4+ cells. The tumor cell count starts around 0.5, peaks around 0.6 at approximately 20 days, and then decreases to near 0 by 100 days. The CD4+ T cell count starts low, increases rapidly to about 2500-3000 by 100 days, and then stabilizes.

**Plot (c):** Titled "β=0.1, I₁=0, I₂=10". The x-axis ranges from 0 to 3000 days. The left y-axis implicitly ranges from 0 to 1000 for tumor cells, and the right y-axis implicitly ranges from 0 to 5 x 10⁵ for CD4+ cells. Both tumor and CD4+ T cell counts show oscillatory behavior. Tumor cell count peaks around 700-900 at approximately 400 days and 2300 days. CD4+ T cell count peaks around 4-5 x 10⁵ at similar times, showing an increasing amplitude over time.

**Plot (d):** Titled "β=0.1, I₁=0, I₂=50". The x-axis ranges from 0 to 500 days. The left y-axis implicitly ranges from -0.2 to 0.8 for tumor cells, and the right y-axis implicitly ranges from -0.002 to 0.01 for CD4+ cells. The tumor cell count starts around 0.5, decreases rapidly to near 0 by 100 days, and then stabilizes. The CD4+ T cell count starts around 0.008, decreases rapidly to near 0.002 by 100 days, and then stabilizes.

Figure 3. Time evolutions of tumor and CD4+ T cells for system (8) on the left column and for system (14) on the right column. Initial condition is (0.5, 0.01,0) for all plots with β = 0.1.::>

<a id='90244217-2d97-4160-a39d-6110224b6008'></a>

In these simulations, CD4+ T cells take about 100 days to reach their peaks with the exception in Figure 3(c), where relapse occurs after a long period of dormancy when small treatments of cytokine are used. In general, if we reduce the parameter _k_ to a smaller value, then the time that it takes for CD4+ T cells to reach a maximum volume is shorter. Parameter _k_ is the half saturation constant for the CD4+ production rate. The smaller _k_ the faster proliferation of the CD4+ through interaction with the tumor cells.

<a id='b88d7163-fdf1-4764-a4b7-23ad71803446'></a>

## 5. Summary and conclusions

Cancer is a leading cause of death worldwide. There are clinical methods such as surgery and/or chemotherapies and radiotherapies to treat the disease. Immunotherapy refers to the treatment of disease by inducing, enhancing, or suppressing an immune response. It uses cytokines usually together with adoptive cellular transfer to boost the immune system. Currently, most cancer immunotherapies involve the generation of CD8$^+$ CTLs to kill cancer cells. As many tumors have been able to evade recognition by CTLs, the need of other immunotherapies is urgent [9–11]. Several recent experiments suggest that CD4$^+$ T cells can recognize tumor antigen that is CTL resistant and may be even more efficient than the CTLs [9–11]. In this work, we propose mathematical models of tumor, CD4$^+$ T cells, and cytokine interactions to explore tumor dynamics and to investigate possible mechanisms of tumor regression and dormancy.

<a id='3ab98e66-b513-49d6-a0a9-82de5ad36ce1'></a>

The maximum production rate β of CD4+, or the antigenicity of the tumor, plays a critical role in the tumor-immune interactions. If β is small, β < βc, then the tumor will grow to its carrying capacity when there is no treatment (cf. Proposition 2.2). If β is larger, the system has limit cycles because of the Hopf bifurcation and the tumor will be oscillating over time. Although clinical evidence for oscillatory dynamics of tumors is not thoroughly established, there are indications of such oscillating behavior for diseases such as leukemia [27–29] observed in patients. The periodicity of the limit cycle in the model depends on the tumor antigenicity β as shown in Figure 1(b). The larger β the smaller the amplitude of the limit cycle and the longer dormant period for the tumor are observed. If β is increased further, then the tumor can be stabilized at a smaller size but the tumor cannot be eliminated completely when there is no treatment.

<a id='2e5d4168-e2b5-449c-9c07-5e34548cabd6'></a>

<::transcription of the content: figure::>
4342

<a id='14741954-93bb-4136-a3b8-54979214ef9f'></a>

--- 
Copyright  2014 John Wiley & Sons, Ltd.

<a id='7fed3462-6312-482c-b4fd-a1ada8e85e1a'></a>

--- Math. Meth. Appl. Sci. **2015**, 38 4330–4344

<a id='7cfc7d77-65e3-478b-82e8-fe51c9e2c7bd'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='de0a98b3-2868-47d4-9462-bad22634198b'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='50d07c74-9113-43f8-8e05-3bbe6b125dd8'></a>

Mathematical
Methods in the
Applied Sciences

<a id='d50d63a0-8e27-4648-b8ef-a3c07c8d6c3d'></a>

With the constant treatment of CD4$^+$ T cells, it is certain that the tumor can never grow to its carrying capacity. However, the tumor may not be eliminated even if its size is small (cf. Proposition 3.1). The interaction may support up to three interior steady states, and therefore, the model may exhibit bistability. This indicates that the long term fate of the tumor with treatment of CD4$^+$ depends on the size when it is detected. Consequently, if the tumor can be detected early, then the tumor cells will be reduced and controlled with the treatment of CD4$^+$.

<a id='e22f2717-2bdb-4d60-ae7c-9be380e362a3'></a>

When the treatment of cytokine is adopted, then it is possible to eliminate the tumor completely when the tumor size is small (cf. (16)). The treatment can also kill all the tumor cells independently of the tumor size if the treatment doses are large enough (cf. Theorem 3.2). If the treatment dose is in the middle range and the tumor's antigenicity ̒ is large, then the tumor can also be eliminated depending on its size and parameter regimes (cf. Theorem 3.4, Theorem 3.5(a)). In these cases, the model exhibits bistability and the stable manifold of the saddle point separates those tumor sizes that can be eliminated from those that cannot.

<a id='0dfe19a9-7c86-465f-8439-87b7ed114084'></a>

We prove theoretically that treatments by cytokine is more effective than transferring CD4+ T cells because treatments by cytokine can clear the tumor cells completely as demonstrated in Theorems 3.2, 3.4 and 3.5. In practice, however, it may not be necessary to kill all the tumor cells but it may be enough to keep the tumor dormant for a long period of time with small size. Our simulations with small tumor size indicate that if doses of treatment are small, then adopting CD4+ T cells as an immunotherapy is better than transferring cytokine when tumor's antigenicity is small; the tumor may grow to its carrying capacity if small doses of cytokine are implemented. If the tumor's antigenicity is large, then small doses of cytokine may keep the tumor dormant for a long period of time before relapsing with large sizes. Both immunotherapies are adequate to control the tumor if doses of treatment are large.

<a id='fc9478d4-94d9-41f7-a426-6244d7c9446c'></a>

The tumor microenvironment is very complex. In this work, we use simple mathematical models of tumor, CD4$^+$, and cytokine to explore effectiveness of immunotherapies. We conclude that transferring either CD4$^+$ T cells or cytokine is effective in controlling the tumor if doses of treatment are large. Because bistability is observed in both modes of immunotherapy, it signifies that a careful planning of the treatments is necessary to achieve a satisfactory outcome.

<a id='90ef87bb-2c44-47cd-8ccf-32519ccad660'></a>

## Acknowledgements

We thank Professor Jonathan Dushoff for his valuable discussion on developing the mathematical models presented in this manuscript.
The authors thank the referee for helpful comments and suggestions that improved the original paper. L. Anderson and S. Jang were
partly supported by the National Science Foundation Grant DMS-1035096.

<a id='7e5b6bbb-4e45-4daf-87fa-2434f10908a5'></a>

References
1. Weienberg RA. The Biology of Cancer second edition. Garland Science: London, UK, 2013.
2. Eftimie R et al. Interaction between the immune system and cancer: a brief review of non-spatial mathematical models. Bulletin of Mathematical Biology 2011; 73:2-32.
3. Quesnel B. Dormant tumor cells as therapeutic target. Cancer Letters 2008; 267:10-17.
4. Rosenberg SA, et al. Use of tumor-infiltrating lymphocytes and interleukin-2 in the immunotherapy of patients with metastatic melanoma. The New England Journal of Medicine 1988; 319(25):1676-1680.
5. de Pillis L, et al. A validated mathematical model of cell-mediated immune response to tumor growth. Cancer Research 2005; 65(17):7950-7958.
6. Goldstein B, Faeder J, Hlavacek W. Mathematical and computational models of immune-receptor signaling. Nature Reviews Immunology 2004; 4(6):445-456.
7. Kronik N, et al. Improving alloreactive CTL immunotherapy for malignant gliomas using a simulation model of their interactive dynamics. Cancer Immunology, Immunotherapy 2008; 57:425-439.
8. Kronik N, et al. Improving T-cell immunotherapy for melanoma through a mathematically motivated strategy: efficacy in numbers? The Journal of Immunology 2012; 35:116-124.
9. Mattes J, et al. Immunotherapy of cytotoxic T cell?resistant tumors by T helper 2 cells: an eotaxin and STAT6-dependent process. The Journal of Experimental Medicine 2003; 197:387-393.
10. Perez-Diez A, et al. CD4 cells can be more efficient at tumor rejection than CD8 cells. Blood 2007; 109:5346-5354.
11. Zhang S. CD4 T-cell-mediated anti-tumor immunity can be uncoupled from autoimmunity via the STAT4/STAT6 signaling axis. European Journal of Immunology 2009; 39:1252-1259.
12. Forys U, et al. Anti-tumor immunity and tumor anti-immunity in a mathematical model of tumor immunotherapy. Journal of Biological Systems 2006; 14(1):13-30.
13. Kuznetsov V, et al. Nonlinear dynamics of immunogenic tumors: parameter estimation and global bifurcation analysis. Bulletin of Mathematical Biology 1994; 2(56):295-321.
14. Michelson S, et al. Tumor micro-ecology and competitive interactions. Journal of Theoretical Biology 1987; 128:233-246.
15. de Vladar H, Gonzlez J. Dynamic response of cancer under the influence of immunological activity and therapy. Journal of Theoretical Biology 2004; 227:335-348.
16. Kirschner D, Panetta JC. Modeling immunotherapy of the tumor-immune interaction. Journal of Mathematical Biology 1998; 37:235-252.
17. Eftimie R, et al. Anti-tumour Th1 and Th2 immunity in the rejection of melanoma. Journal of Theoretical Biology 2010; 265:467-480.
18. Thieme HR. Mathematics in Population Biology. Princeton University Press: New Jersey, 2003.
19. Allen L. An Introduction to Mathematical Biology. Prentice-Hall: New Jersey, 2006.
20. Wiggins S. Introduction to Applied Nonlinear Dynamical Systems and Chaos. Springer: New York, 2003.
21. Plesnicar S, et al. Actual doubling time values of pulmonary metastases from malignant melanoma. ANZ Journal of Surgery 1978; 48(1):23-25.
22. Conlon PJ, et al. Interleukin-4 (B-cell stimulatory factor-1) augments the in vivo generation of cytotoxic cells in immunosuppressed animals. Biotechnology Theory 1989; 1:31-41.

<a id='17641216-2317-4121-b374-08f312072861'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='0a2326d1-eb35-4468-9b2a-e16501f641d8'></a>

Math. Meth. Appl. Sci. 2015, 38 4330–4344

<a id='7816eb5d-c3ac-4420-84a1-4f6a265d2ec0'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Cre434g cense

<!-- PAGE BREAK -->

<a id='1b13e735-422f-46f7-822c-63cab9cf314c'></a>

Mathematical
Methods in the
Applied Sciences

<a id='12f151c5-5969-4fda-889f-8e3d95b3d8c7'></a>

L. ANDERSON, S. JANG AND J.-L. YU

<a id='66b03c65-1099-446e-9ded-cff913900c33'></a>

23. Yee C, et al. Adoptive T cell therapy using antigen-specific CD8+ T cell clones for the treatment of patients with metastatic melanoma: in vivo persistence, migration, and antitumor effect of transferred T cells. Proceedings of the National academy of Sciences of the United States of America 2002; **99**(25):16168–16173.
24. http://en.wikipedia.org/wiki/White—blood—cell.
25. Dudley ME, et al. Cancer regression and autoimmunity in patients after clonal repopulation with antitumor lymphocytes. Science 2002; **298**:850–854.
26. Plautz GE, et al. T-cell adoptive immunotherapy of metastatic renal cell carcinoma. Adult Urology 1999; **54**:617–623.
27. Mehta B, Agarwal M. Cyclic oscillations in leukocyte count in chronic myeloid leukemia. Acta Haematologica 1980; **63**:68–70.
28. Kennedy B. Cyclic leukocyte oscillations in chronic myelogenous leukemia during hydroxyurea therapy. Blood 1970; **35**:751–760.
29. Vodopick H, et al. Spontaneous cyclic leukocytosis and thrombocytosis in chronic granulocytic leukemia. The New England Journal of Medicine 1972; **286**:284–290.

<a id='62cd90a5-78cc-4844-9ced-5f3940056ad4'></a>

<::4344: figure::>

<a id='f95a65ba-1a06-43e7-9374-0859cacd9bb4'></a>

Copyright © 2014 John Wiley & Sons, Ltd.

<a id='a9a53330-0fc9-43c2-9f87-a0617e5f89cb'></a>

Math. Meth. Appl. Sci. 2015, 38 4330-4344

<a id='06e49119-e725-4301-8ad4-2305be87640e'></a>

10991476, 2015, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mma.3370 by Universita Di Trento, Wiley Online Library on [09/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
<a id='6b1a1ed2-e595-4af0-918c-819c65b9612a'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207
DOI 10.1007/s11538-005-9022-3

<a id='c1014401-87ad-4c4b-806f-4824f9586735'></a>

ORIGINAL ARTICLE

<a id='4a8fb007-f099-4e78-bd00-01422d956d7b'></a>

Macrophage Dynamics in Diabetic Wound Healing

<a id='602b2627-4952-4d47-bdb6-8c8b684319fb'></a>

Helen V. Waugh*, Jonathan A. Sherratt

<a id='91594f8d-63f4-4824-bf84-a70a42d7185c'></a>

School of Mathematics and Computing, Heriot-Watt University, Riccarton,
Edinburgh EH14 4AS, UK

<a id='073cbebc-93c5-4f03-87bc-6333a1ba5875'></a>

Received: 17 August 2004 / Accepted: 15 March 2005 / Published online: 22 February 2006
© Society for Mathematical Biology 2006

<a id='ce84be29-5e76-4598-8a5f-cee00fb41dfc'></a>

**Abstract** Wound healing in diabetes is a complex process, characterised by a chronic inflammation phase. The exact mechanism by which this occurs is not fully understood, and whilst several treatments for healing diabetic wounds exist, very little research has been conducted towards the causes of the extended inflammation phase. We describe a mathematical model which offers a possible explanation for diabetic wound healing in terms of the distribution of macrophage phenotypes being altered in the diabetic patient compared to normal wound repair. As a consequence of this, we put forward a suggestion for treatment based on rectifying the macrophage phenotype imbalance.

<a id='676f6987-bbc9-4ded-bb06-38267a1244c3'></a>

**Keywords** Macrophages  Wound healing  Diabetes

<a id='38248e9b-9795-4471-83ed-46c2243433b6'></a>

# 1. Introduction

It has been known for many years that wounds in diabetic patients can take longer to heal than similar wounds in non-diabetics (Mulder et al., 1998). Typically healing takes several months, and many wounds do not heal for 12–18 months or more. The normal wound healing mechanism is obviously disrupted in some way, although despite intensive research a comprehensive understanding of this disruption, or its extent, has not yet been realised. There are, however, pieces of this complex jigsaw which have been identified and by combining these pieces together it becomes possible to present an initial mathematical model of the wound healing process as affected by diabetes mellitus.

<a id='2c028bda-d673-497b-a0a0-3f7b7f6dd8a6'></a>

The first stage of the wound healing process is the inflammation stage (Robson et al., 2001), and macrophages are among the first cells to arrive at the wound site in response to chemical signals (growth factors) released by platelets (Singer and Clark, 1999). Growth factors stimulate the chemotaxis and mitosis of both endothelial cells and fibroblasts, and are thus vital for the second stage of wound

<a id='aed211cd-e574-4a8b-a6bd-0b3c73507938'></a>

*Corresponding author.
E-mail address: hwaugh@ma.hw.ac.uk (Helen V. Waugh).

<!-- PAGE BREAK -->

<a id='57d0fd1b-6422-4601-b20d-5c0d960d6cd1'></a>

198

<a id='6006d467-e2ae-4ca0-9d72-453e355a6cfd'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='316c7507-1697-4fba-9c8f-4d324a0ea48b'></a>

repair, the proliferative stage. In diabetic patients, macrophages are known to per-
sist past the inflammatory stage in chronic non-healing wounds, and data from
Loots et al. (1998) shows that significant numbers of these cells have been mea-
sured on day 28 of healing, long after macrophages are no longer seen in similar
wounds in the control (non-diabetic) subjects.

<a id='4b706c3f-02b9-4ff2-af8a-4c65ef304013'></a>

Macrophages themselves are differentiated monocytes, and result from mono-cytes responding to certain chemical stimuli. There are known to be three types of macrophage important to the wound environment-cytocidal, inflam-matory and repair macrophages (Riches, 1996). Monocytes become inflamma-tory macrophages in the presence of 1,3-β-glucan, and differentiate into re-pair macrophages in the presence of hyaluronan. Cytocidal macrophages are formed in response to polyinosinate-polycytidylate and are 'killer' cells that re-move bacteria and other debris from the wound site. Since we are not con-sidering the effects of a bacterial load on the wound site or debris removal in the model, this macrophage phenotype will not be discussed further in this paper.

<a id='9ddf18c3-f696-445d-b8b0-80a59ec355fb'></a>

Each type of macrophage produces different growth factors and cytokines. Inflammatory macrophages produce platelet-derived growth factor (PDGF), transforming growth factor-β (TGF-β) and basic fibroblast growth factor (Singer and Clark, 1999; Robson et al., 2001), which attract fibroblasts and endothelial cells to the wound site and encourage them to proliferate. Repair macrophages, which help remodel the extracellular matrix of the wound, produce insulin-like growth factor 1 and also PDGF (Singer and Clark, 1999; Robson et al., 2001).

<a id='857f0b3b-c5ee-4cd8-8679-2096b100885d'></a>

It is the balance between the inflammatory and repair macrophage popula-
tions (Zykova et al., 2000) that appears to be crucial for successful wound healing.
Since monocytes become repair macrophages in the presence of hyaluronan, and
hyaluronan is produced by fibroblasts, it follows that if the balance between the
macrophage populations is disturbed, as suspected in diabetic wounds, then the
hypothesis is that there could be an insufficient amount of hyaluronan being pro-
duced by fibroblasts, resulting in the repair macrophage population being too low
for healing to be completed.

<a id='57f6ad94-bf71-44c8-b1b3-e558600c0e8a'></a>

The effects of diabetes on the wound healing process are the impairment of cellular proliferation for most cell types (Sank et al., 1994; Hehenberger et al., 1998; Lerman et al., 2003), increased apoptosis of endothelial cells (Lorenzi et al., 1985; Baumgartner-Parzer et al., 1995; Darby et al., 1997), increased average blood glucose level (Williams and Pickup, 2001), impairment of blood vessel re-growth (Loots et al., 1998; Singer and Clark, 1999), inadequate flow through blood vessels (Singer and Clark, 1999; Greenhalgh, 2003) and decreased collagen depo-sition at the wound site (Black et al., 2003). Furthermore, it is likely that growth factor expression is altered (Shukla et al., 1998; Wetzler et al., 2000; Robson et al., 2001; Greenhalgh, 2003), and nitric oxide secretion (Bulgrin et al., 1995; Schaeffer et al., 1996; Schaeffer et al., 1997; Zykova et al., 2000) and macrophage removal to the lymph nodes may also be impaired (Bellingan et al., 1996).

<a id='84ad807d-cee1-45c0-8979-68cd829d0094'></a>

Mathematical models of wound repair and healing have thus far been directed towards the proliferation and repair stages of the wound healing process, but it is evident that for diabetic wounds, the inflammatory phase should be modelled in the first instance, as this is when macrophages are most involved.

<!-- PAGE BREAK -->

<a id='7399a9c2-420a-4f6e-b220-a6fc6bb98f4f'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='89e05951-0dae-41cd-ad07-86995e0a7f2a'></a>

199

<a id='f71e0105-48b1-4191-9135-cc2e5044fadc'></a>

The aim of this paper is to investigate the inflammatory stage of the wound heal-ing process, in both diabetic and normal patients, in terms of the macrophage population behaviour. In the next section, we will derive a basic mathematical model capturing the main features of the inflammatory stage, concentrating on the behaviour of macrophages. In Section 3 we proceed to numerically simulate our model, which leads to a fuller analysis of the steady states in Section 4. This enables us to identify the number of steady-states and their nature, and whether these states can be correlated with the diabetic and normal wound healing states seen in patients. Finally, in Section 5, we discuss our results with reference to avail-able biological data and suggest possible suitable treatment strategies.

<a id='ecc9ae99-1832-4bd4-ac4a-afc8a6c71bb0'></a>

## 2. A basic mathematical model
Very little work has been done in this context from a mathematical viewpoint. Our mathematical model is deliberately simple and concentrates on the involvement of inflammatory and repair macrophages in the inflammatory stage of the wound healing process. The model consists of three variables, considered on a timescale starting approximately 1 day post-wounding. In comparison to other models (Pettet et al., 1996; Cobbold and Sherratt, 2000) we examine the inflammatory stage, and how events at this stage may have a knock-on effect on the latter stages of the wound healing process. By looking only at this stage we are able to ignore the effects of fibroblasts and endothelial cells (Singer and Clark, 1999), and concentrate on the macrophage dynamics. Also, as we are not investigating bacterial cell populations we can ignore the behaviour of cyctocidal (killer) macrophages. In our model, we choose the inflammatory macrophage density $\phi_1(t)$ (cells mm⁻³) and the repair macrophage density $\phi_R(t)$ (cells mm⁻³) as variables, as they are the key cell populations during the inflammatory stage (Singer and Clark, 1999); $t$ denotes the time in days. Furthermore, we include the TGF-β concentration $T(t)$ (pg mm⁻³) as this growth factor is released by platelets upon wounding, and macrophage precursors (monocytes) migrate to the wound in response to the TGF-β concentration (Riches, 1996; Robson et al., 2001).

<a id='ff2256fe-a2f8-4488-8460-01b0c391d037'></a>

## 2.1. Inflammatory macrophages

In modelling the inflammatory macrophage population, we represent the migration of monocytes to the wound site in response to TGF-β concentration by a function K, with α being the proportion of the monocytes that become inflammatory macrophages in response to chemical stimuli at the wound site. Mitotic division of the cells is represented by a logistic growth term, although the macrophage population mainly increases due to migration: there is still a significant amount of mitosis (Miyasaki, 2002). There is also a crowding term representing the effect of the repair macrophage population. Finally, we have a linear decay term representing the removal of the macrophages from the wound site. Note that macrophages do not actually die at the wound site, but travel to the lymph node system, the spleen or the liver (Bellingan et al., 1996). Combining these terms gives the following

<!-- PAGE BREAK -->

<a id='4ad8e04c-1b0f-4a36-8a42-26354ccd916b'></a>

200

<a id='32745108-429b-4b70-847d-d77279f5ee51'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='f8e3b6e2-7e9d-4cf1-81c0-881bbb4b9917'></a>

ordinary differential equation representing the rate of change of the inflammatory
macrophage cell density:

<a id='4c2cb1e0-e4b5-4396-977c-fa4de59664be'></a>

dφI/dt = αK(T) + k1 k2 φI (1 - k3(φI + φR)) - d1 φI (1)

<a id='7a9d7bfd-9c18-446a-b324-45c4bb5a563f'></a>

In this equation, k₁ represents the proportion of macrophages undergoing mitotic division at any one time and k₂ is the macrophage growth rate. In the model k₁ and k₂ only appear as a product but we include them both explicitly to facilitate comparison with other mathematical models, in which k₁ = 1, and so is not included as a separate parameter. In our context, a typical value of k₁ is 0.05 because the number of macrophages undergoing mitotic division is low (Miyasaki, 2002).

<a id='7e217bc3-5729-49f9-87d5-1e76283a86fb'></a>

2.2. *Repair macrophages*

We assume that repair macrophages exhibit the same characteristics as inflam-matory macrophages regarding cell migration, mitosis and removal; there is very little data available about this. As α is the fraction of monocytes that become in-flammatory macrophages then it follows that (1 - α) is the monocyte fraction that becomes repair macrophages, as both macrophage phenotypes originate from the same pool of available cells. Thus, the ordinary differential equation representing the rate of change of the repair macrophage cell density is:

<a id='d89ca4ff-a88b-4018-8dff-4c1ca23f98dd'></a>

dφR / dt = (1 - α) K(T) + k1 k2 φR (1 - k3 (φI + φR)) - d1 φR (2)

<a id='6851c97e-f034-421e-8f46-964fc6525b19'></a>

2.3. Transforming growth factor-β, TGF-β
TGF-β is only produced by inflammatory macrophages (Singer and Clark, 1999), and again the production of TGF-β by these cells may be considered as constant. The decay rate may also be considered as linear, and therefore the ordinary differential equation representing the rate of change of TGF-β concentration is:

<a id='0dd4ca60-ffbf-4b4e-a5b1-7e59bee14842'></a>

dT/dt = k4φ1 - d2T (3)

<a id='af3632e2-607a-4069-9e51-ecf45451c995'></a>

### 3. Numerical solution of equations
Numerical solutions of our model (Eqs. (1)-(3)) were carried out using ode15s, a stiff ODE solver in Matlab. While investigating the model we were able to obtain simulations of both diabetic and normal wound healing. To simulate normal wound healing, we assume that α = 0.5 (i.e. that there are equal numbers of inflammatory and repair macrophages formed), and we take α = 0.8 in a diabetic wound (i.e. that there are more inflammatory macrophages formed than repair

<!-- PAGE BREAK -->

<a id='414300d0-cf5c-443c-a03e-039cd6f923fb'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='90f7f92f-dc0f-489a-9ce1-7dec89a0e4a3'></a>

201

<a id='3e1d6762-03be-4386-9095-369442462b90'></a>

<::chart: The main chart, labeled Fig. 1, displays Monocyte migration (Y-axis, from 0 to 400) as a function of TGF-Beta concentration (X-axis, from 0 to 10). A curve, representing the cubic function K(T), starts slightly above zero, increases to a peak around TGF-Beta concentration of 6, and then decreases, crossing the X-axis near 9.5. An inset chart provides an enlargement of the curve for TGF-Beta concentration from 0 to 1, with Monocyte migration from 0 to 30. This inset shows the initial segment of the curve, labeled with the text "Enlargement shows that the intercept of cubic is positive". The caption reads: "Fig. 1 A qualitative form of K(T) representing monocyte migration, based on the data available in Wahl et al. (1987). Note that when T = 0, the macrophage migration is small but positive. The curve plotted in the figure is the cubic K(T) = τ₁ T³ + τ₂T² + τ₃T + τ₄ with τ₁ = -2.47, τ₂ = 21.94, τ₃ = 6.41 and τ₄ = 1.75. Note that a cubic is the simplest mathematical form for K(T) giving the appropriate behaviour. In particular, a quadratic form for K(T) does not give the two distinct behaviours shown in Fig. 2." ::>

<a id='4e8847ff-c986-4268-ac0e-fff93f502f42'></a>

macrophages). Unfortunately, there is currently no quantitative data on which the value of _a_ for diabetic wounds can be based.

<a id='3e4b1483-ff2e-4c3b-b14b-f61f27efe4c8'></a>

There is also little actual data available to construct a suitable function of _K_(_T_)
but Wahl et al. (1987) presents data on the migration of monocytes in vivo in re-
sponse to TGF-̒. Figure 1 shows a qualitative form of _K_(_T_) constructed using this
data. When the TGF-̒ concentration _T_ is zero, there is a low background level of
macrophage migration. As _T_ increases, the migration increases initially, reaching
a maximum at about _T_ = 6.0 pg mm⁻³, and then decreasing again.

<a id='70ec5291-d903-4534-a5f7-e0c005c045eb'></a>

Figure 2 shows typical macrophage and TGF-̸ profiles obtained for both normal and diabetic wounds by numerical solution of the model (Eqs. (1)-(3)). The numerical results suggest that there are two stable steady states for our system of equations—one that is near zero, and one that is away from zero. In a normal wound the macrophage population decreases to the near zero steady state, but in a diabetic wound the macrophage population continues to increase as the macrophages persist in the wound environment, and the other steady state is reached. This suggests a detailed study of the nature of these steady states to see if these correlate with behaviour observed for normal and diabetic wounds.

<a id='bab7483e-bc07-4300-85fe-100400968fa7'></a>

## 4. Steady state and stability analysis
When solving for steady states, it is convenient to keep the form of K(T) general and to express solutions in terms of T. This shows that the steady states satisfy

<!-- PAGE BREAK -->

<a id='2b1124f7-1a70-42a8-9b39-1ac7ee735df0'></a>

202

<a id='81b41d0f-5a39-46bb-94eb-96572f00720f'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='6be2a390-4ef1-47a6-9404-0bc447566977'></a>

<::chart: A figure titled "Fig. 2 Numerical simulation of our model (Eqs. (1)–(3)) illustrating normal and diabetic wound healing." The figure consists of six line graphs arranged in a 3x2 grid, comparing "Normal Wound" (left column) and "Diabetic Wound" (right column) simulations over 40 days. The diabetic wound simulation shows that macrophages persist in the wound environment far longer than they do in the normal wound simulation, and that the level of TGF-β is far higher than in the normal wound. The initial conditions are φ_I (0) = φ_R (0) = 200 cells mm⁻³, T(0) = 6 pg mm⁻³. The parameters are k₁ = 0.05 (5%), k₂ = 0.693 day⁻¹, k₃ = 0.002 (cells mm⁻³)⁻¹, k₄ = 0.07 pg cells⁻¹ day⁻¹, d₁ = 0.2 day⁻¹, d₂ = 9.1 day⁻¹. The function K(T) used in the simulation is the same as illustrated in Fig. 1. The subplots are described as follows:||||Normal Wound Column:||Top-left graph: Shows φ_I (cells/cubic mm) decreasing from 200 to near 0 over 40 days.||Middle-left graph: Shows φ_R (cells/cubic mm) decreasing from 200 to near 0 over 40 days.||Bottom-left graph: Shows TGF-β (pg/cubic mm) decreasing from 6 to near 0 over 40 days.||||Diabetic Wound Column:||Top-right graph: Shows φ_I (cells/cubic mm) increasing from 200 to plateau around 950-1000 by day 20.||Middle-right graph: Shows φ_R (cells/cubic mm) starting at 200, dipping to around 150, then increasing to plateau around 250-275 by day 20.||Bottom-right graph: Shows TGF-β (pg/cubic mm) starting at 6, dipping slightly, then increasing to plateau around 7.5-8 by day 20.::>

<a id='feaae864-76bd-4ba3-9ae8-58ffc821e5f6'></a>

either:

(i)

$\phi_I = \frac{d_2 T}{k_4}, \phi_R = \frac{k_1 k_2 - d_1}{k_1 k_2 k_3} - \frac{d_2 T}{k_4}$

$K(T) = 0$

<!-- PAGE BREAK -->

<a id='19a94d23-7d7f-4b9a-9cc2-7eadbd0a5ed6'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='85038d44-9f1a-4ec6-bd6c-55380bca1259'></a>

203

<a id='95772b1c-98e1-4a9d-a402-1768d486ba7a'></a>

<::chart: The chart is a 2D plot with 'q' on the x-axis, ranging from -10 to 90, and 'r' on the y-axis, ranging from -50 to 50. The plot shows two curves representing the variation of 'q' and 'r' as 'α' and 'β' are varied. The axes are labeled 'q' and 'r'. A horizontal line is at r=0 and a vertical line is at q=0. The region where q > 0 is indicated at the top left, and r > 0 is indicated at the middle right. A 'plain solid line' curve starts near (20, 15), curves downwards to (30, -50), and then continues curving outwards to the right. A 'line with crosses' curve starts near (0, 0), goes up to (25, 2), and then continues upwards and to the right, reaching approximately (90, 20). An arrow along this curve indicates 'increasing α'. Several regions are labeled: - '1 steady state (stable)' is in the top right quadrant. - 'normal wound α = 0.5' points to a segment of the 'line with crosses' curve around (30, 5). - 'diabetic wound α = 0.8' points to a segment of the 'line with crosses' curve around (60, 10). - '1 steady state (stable)' is in the bottom left quadrant. - '3 steady states (2 stable, 1 unstable)' is in the bottom right quadrant. Fig. 3 Plots of q and r as α and β are varied. The plain solid line is a plot of (10) while the line with crosses shows (7). This figure shows that a small imbalance in the inflammatory and repair macrophage populations can result in wound healing being severely disrupted. All other parameter values are as in Figs. 1 and 2.::>

<a id='bcb85937-b118-4824-9db6-4b69111f3c1e'></a>

(ii)
$\phi_I = \frac{d_2 T}{k_4}$, $\phi_R = \frac{d_2 T(1 - \alpha)}{k_4 \alpha}$
$K(T) = \frac{k_1 k_2 k_3 d_2 T^2}{k_4^2 \alpha^2} + \frac{(d_1 - k_1 k_2) d_2 T}{k_4 \alpha}$ (4)

<a id='f5e3a60b-3d4b-47d6-a013-f9fe691c7333'></a>

Solution set (i) implies that there is no migration of monocytes to the wound site, and since we know this not to be true even in diabetic wounds we disregard this solution set and instead concentrate on solution set (ii).

<a id='5fd11f01-0ac0-4713-9725-e5211a241de8'></a>

As α increases from 0 to 1, the number of solutions of (4) varies from one to three. Numerical stability analysis (not included) of the steady states shows that when there is only one steady state, it is stable, and when there are three intersections, the sequence is stable-unstable-stable. This is commonly seen in biological problems, and we use a method adapted from the study of spruce budworm population dynamics (Murray, 2002) to investigate the changes in steady state number.

<a id='7033bef6-4237-4f32-b06d-cadfc9266f56'></a>

4.1. *Bifurcation location*
The simplest mathematical form for *K*(*T*) having the appropriate qualitative form
(see Fig. 1) is a cubic

<!-- PAGE BREAK -->

<a id='676a0cd8-0f5e-43b9-9d00-db5497bafbd7'></a>

204

<a id='096735e1-edd4-41fa-b7e7-0feb6b9fade6'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='e7ef06e8-6339-4693-abb2-53504ac41b0c'></a>

K(T) = τ₁T³ + τ₂T² + τ₃T + τ₄ (5)

<a id='4838fb10-de85-4722-9ae5-743e8f64fe3c'></a>

with τ₁ < 0 and τ₂,τ₃,τ₄ > 0. (Note that a quadratic form for K(T) does not give the required asymmetry and would not allow for the possibility of three solutions to (4)). At the steady states we know that this cubic form of K(T) will satisfy (4), so that

τ₁ T³ + τ₂ T² + τ₃ T + τ₄ = rT² + qT (6)

<a id='bbb4a308-cdd6-415b-aa36-55d87fe43e0e'></a>

where for our model:

$r = \frac{k_1 k_2 k_3 d_2^2}{k_4^2 \alpha^2}$

$q = \frac{(d_1 - k_1 k_2) d_2}{k_4 \alpha}$
(7)

<a id='f0dc5b01-fe1f-4d75-b314-a3967640dafe'></a>

Rearranging Eq. (6) gives:

$T^3 + \left(\frac{\tau_2 - r}{\tau_1}\right) T^2 + \left(\frac{\tau_3 - q}{\tau_1}\right) T + \frac{\tau_4}{\tau_1} = 0.$ (8)

<a id='1e16b24c-5eec-4a1a-b395-438b06752c97'></a>

At the transition between one and three real roots, Eq. (8) will have a dou-ble root. A relation between _q_ and _r_ at this transition can thus be obtained by comparing (8) with the general form of a cubic equation with a double root, namely

$(T - \beta)^2(T - \gamma) \equiv T^3 - (2\beta + \gamma)T^2 + (\beta^2 + 2\gamma\beta)T - \beta^2\gamma = 0$ (9)

<a id='6f33b217-bacb-4748-b063-4569b5ba85ee'></a>

where β and γ are steady state values of T. If we then use this equation to deter-
mine r and q as functions of β alone we obtain:

$r = \tau_2 + 2\tau_1\beta - \frac{\tau_4}{\beta^2}$;

$q = \tau_3 + 2\frac{\tau_4}{\beta} - \tau_1\beta^2$. (10)

<a id='59402496-004a-43b2-bfd8-9bf990bef726'></a>

Figure 3 shows the relationship between _r_ and _q_ given by (10), treating \beta as a parameter linking _r_ and _q_. At the cusp,

<a id='65846b63-d383-4a8a-b631-c8ce202da24b'></a>

dr/d̸ = dq/d̸ = 0

<a id='ce078a86-bd84-424f-b20f-a07f1ad9f238'></a>

which implies that

<a id='01874cf5-fca1-4d97-a199-6500825aa75d'></a>

$\beta = \sqrt[3]{\frac{-\tau_4}{\tau_1}}$.

<a id='a1d03e60-6c71-43f5-aa6a-96ac645537f6'></a>

For our parameters, this gives β = 0.89, i.e. T = 0.89 pg mm⁻³. In Fig. 3 we also plot the relationship between r and q implied by (7). Here α has been allowed to vary with the other model parameters fixed. This shows that as α is increased, there is a bifurcation at α = 0.54, at which the number of steady states changes from one

<!-- PAGE BREAK -->

<a id='2b455fb4-e66f-45bd-88f6-ccba9b84133b'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='5ecc8b76-ea40-4182-826f-279aa724425e'></a>

205

<a id='53e37ff5-50a6-4499-ac30-0ded50151d34'></a>

to three. Crucially, the value of \$\alpha = 0.5\$ corresponding to normal wound healing is
below this threshold, while the value of \$\alpha = 0.8\$ corresponding to diabetic healing
is above it. Our model predicts that this is the key factor underlying the difference
in repair of normal and diabetic wounds.

<a id='153140ca-d138-481c-9236-5b6868b99f38'></a>

## 5. Discussion
Although the model we utilised is a simple one, both the numerical solution and the steady state analysis indicate that this model can provide insights into wound healing in normal and diabetic patients. However, this model has only investigated the behaviour of macrophages and TGF-β and there are many more cell populations and growth factors present during the wound healing process. Therefore, our model cannot claim to give a definitive answer to the problems encountered in the healing of diabetic wounds.

<a id='e1625b95-015b-46dd-9ced-5de81398a3e1'></a>

## 5.1. Macrophage dynamics

Figure 1 shows that the model captures the key qualitative features of wound re-pair in the two cases of normal and diabetic wound healing; in particular, that the macrophage population decreases to almost zero in normal wound healing, whilst the macrophages persist in the diabetic case. Moreover, our analysis shows the two different wound healing responses seen clinically, and demonstrates that there is a sudden shift between the two healing states, as the balance between inflamma-tory and repair macrophages changes. The critical value of α for which the system changes from having one to three steady states is 0.54 which occurs when T = 3.55 pg mm⁻³. This is less than values typically reported in diabetic wounds, and pro-vides a possible explanation for why diabetic wounds do not heal. There is an ex-cess of TGF-β in the wound environment, which in turn attracts more monocytes to the wound site, leading to a higher level of inflammatory macrophages. These cells produce more TGF-β, perpetuating this vicious circle of events.

<a id='4e8d9c0b-8a05-4fcc-a4a3-8ec946867a00'></a>

## 5.2. Treatment suggestions

Our model predicts that there is an imbalance between the inflammatory and repair macrophage populations in the diabetic wound environment. Therefore, one course of action to aid healing would be to address this imbalance, and return it to that which is found in normal patients. This requires a reduction of \u03b1. In principle, this could be done in one of two ways, either by decreasing the amount of 1,3-\u03b2-glucan in the wound environment or by increasing the amount of hyaluronan available.

<a id='073d9b82-f2ce-428c-9c27-2fae26eb814d'></a>

Figure 4 demonstrates a hypothetical treatment applied to a diabetic wound 10 days after formation. This treatment reduces a to 0.2 and returns the diabetic wound to a healed state, compared to a diabetic wound which was left untreated. Of course, this treatment may not work in practice because the resultant effect on other cell populations, such as fibroblasts, has not been considered in our model, and any alterations at the inflammation stage may well alter the latter stages of wound healing.

<!-- PAGE BREAK -->

<a id='4eb55dc7-a8a1-462e-9184-65c46437c3dc'></a>

206

<a id='7b01c9a9-5a47-4a94-bee8-5ccee4548539'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='f03f58de-41f0-40fc-912b-7166a9828076'></a>

<::chart: line graph::>Fig. 4 Comparison of a diabetic wound left untreated and one to which a therapy reducing α to 0.2 is applied at Day 10. In the diabetic wound the macrophage population persists, but in the treated wound the macrophage population decreases in accordance with behaviour seen in healing wounds. All other parameters as before. The graph shows total macrophage density (cells/cubic mm) on the y-axis versus time (days) on the x-axis, ranging from 0 to 40 days. The y-axis ranges from 0 to 1400. A dashed line, labeled "untreated diabetic wound", shows macrophage density rising from approximately 500 at day 0, peaking around 1200 at day 10, and then leveling off at approximately 1200 for the remainder of the 40 days. A solid line, labeled "diabetic wound after treatment applied to wound on day 10", follows the same path as the untreated wound until day 10, reaching approximately 1200 cells/cubic mm. After day 10, the density continues to rise slightly to a peak of around 1300 cells/cubic mm at day 13-14, then sharply decreases, dropping to below 200 cells/cubic mm by day 30 and approaching 0 by day 40.<::>

<a id='05ab6bd7-3b51-4763-9a24-da8dd7703ed9'></a>

## 6. Conclusion
The results of our modelling are consistent with the hypothesis that the balance of macrophage phenotypes is disrupted in diabetic wound healing. Possible extensions of the model could be to include equations for other cell populations, such as fibroblasts and keratinocytes, to enable the modelling of current treatments for diabetic wound management. In conclusion, our work highlights the importance of macrophages in diabetic wound healing, and supports the hypothesis that diabetic wounds appear to be 'stuck' in the inflammation stage and can be 'jump-started' into healing by the application of an appropriate treatment.

<a id='a5909de5-7a73-44a5-966b-f343b67aeedc'></a>

## Acknowledgement
HVW was supported by a doctoral training account from the Engineering and Physical Sciences Research Council. JAS was supported in part by an Advanced Research Fellowship, also from EPSRC.

<a id='be903b9b-b081-47ab-9394-2642aec01fc0'></a>

## References
Baumgartner-Parzer, S.M., 1995. High-glucose triggered apoptosis in cultured endothelial cells. Diabetes 44(11), 1323–1327.
Bellingan, G.J., 1996. In vivo fate of the inflammatory macrophage during resolution of inflammation: Inflammatory macrophages do not die locally, but emigrate to the draining lymph nodes. J. Immunol. 157(6), 2577–2585.

<!-- PAGE BREAK -->

<a id='fe65ae6f-f2eb-4f59-9f5f-b89d1e4abae6'></a>

Bulletin of Mathematical Biology (2006) 68: 197–207

<a id='b38e4e9e-df11-47fb-aa8c-b3a43e657d56'></a>

207

<a id='9af0f868-bd68-4a75-8fac-50f73faa3b81'></a>

Black, E., 2003. Decrease of collagen deposition in wound repair in type 1 diabetes independent of glycemic control. Arch. Surg. 138(1), 34-40.
Bulgrin, J.P., 1995. Nitric oxide synthesis is suppressed in steroid-impaired and diabetic wounds. Wounds 7, 48-57.
Cobbold, C.A., Sherratt, J.A., 2000. Mathematical modelling of nitric oxide activity in wound healing can explain keloid and hypertrophic scarring. J. Theor. Biol. 204(2), 257-288.
Darby, I.A., 1997. Apoptosis is increased in a model of diabetes-impaired wound healing in genetically diabetic mice. Int. J. Biochem. Cell Biol. 29(1), 191-200.
Greenhalgh, D., 2003. Wound healing and diabetes mellitus. Clin. Plast. Surg. 30(1), 37-45.
Hehenberger, K., 1998. Inhibited proliferation of fibroblasts derived from chronic diabetic wounds and normal fibroblasts treated with high glucose is associated with increased formation of 1-lactate. Wound Repair Regen. 6(2), 135-141.
Lerman, O., 2003. Cellular dysfunction in the diabetic fibroblast: Impairment in migration, vascular endothelial growth factor production, and response to hypoxia. Am. J. Pathol. 162(1), 303-312.
Loots, M.A., 1998. Differences in cellular infiltrate and extracellular matrix of chronic diabetic and venous ulcers versus acute wounds. J. Invest. Dermatol. 111(5), 850-857.
Lorenzi, M., Cagliero, E., Toledo, S., 1985. Glucose toxicity for human endothelial cells in culture: Delayed replication, disturbed cell cycle, and accelerated death. Diabetes 34(7), 621-627.
Miyasaki, K., 2002. Chap. 5—Monocytes. In: Basic Immunology Course Notes (Web Document), UCLA.
Mulder, G.D., 1998. Clinician's Pocket Guide to Chronic Wound Repair. In: Wound Care Communications Network, 4th edn. Springhouse Corp., Springhouse, PA, pp. 58-67.
Murray, J.D., 2002. Mathematical Biology. Vol. 1: An Introduction, 3rd edn. In: Interdiscliplinary Applied Mathematics Series. Springer-Verlag, Berlin, pp. 7-10, 40-41.
Pettet, G., 1996. On the role of angiogenesis in wound healing. Proc. R. Soc. Lond. Part B 263(1376), 1487-1493.
Riches, D.W.H., 1996. Macrophage involvement in wound repair, modelling and fibrosis. In: Clark, R.A.F. (Ed.), The Molecular and Cellular Biology of Wound Repair, 2nd edn., pp. 95-142.
Robson, M.C., Steed, D.L., Franz, M.G., 2001. Wound Healing: Biologic features and approaches to maximize healing trajectories. Curr. Probl. Surg. 38(2), 65-140.
Sank, A., 1994. Human endothelial cells are defective in diabetic vascular research. J. Surg. Res. 57(6), 647-653.
Schaeffer, M.R., 1996. Nitric oxide regulates wound healing. J. Surg. Res. 63(1), 237-240.
Schaeffer, M.R., 1997. Diabetes-impaired healing and reduced wound nitric oxide synthesis: A possible pathophysiologic correlation. Surgery 121(5), 513-519.
Shukla, A., 1998. Differential expression of proteins during healing of cutaneous wounds in normal and chronic models. Biochem. Biophys. Res. Commun. 244(2), 434-439.
Singer, A.J., Clark, R.A.F., 1999. Cutaneous wound healing. N. Engl. J. Med. 341(10), 738-746.
Wahl, S.M., 1987. Transforming growth factor beta induces monocyte chemotaxis and growth factor production. Proc. Natl. Acad. Sci. U.S.A. 84(16), 5788-5792.
Wetzler, C., 2000. Large and sustained induction of chemokines during impaired wound healing in the genetically diabetic mouse: Prolonged persistence of neutrophils and macrophages during the late phase of repair. J. Invest. Dermatol. 115(2), 245-253.
Williams, G., Pickup, J.C., 2001. Handbook of Diabetes, 2nd edn. Blackwell Science, Oxford, 69p.
Zykova, S.N., 2000. Altered cytokine and nitric oxide secretion in vitro by macrophages from diabetic type II-like db/db mice. Diabetes 49(9), 1451-1458.
<a id='3f3b0727-6c00-4882-9d2b-767a7ba0d210'></a>

<::logo: Elsevier
NON SOLUS
Black and white illustration of a tree with two figures beneath it, and the word "ELSEVIER" below.::>

<a id='cb975980-566a-4639-80bc-76120b0ea97c'></a>

BioSystems 59 (2001) 15–25

<a id='6125bf1a-caad-416e-a597-3033e90cf357'></a>

<::logo: Bio Systems
Bio Systems
The logo features a black square with a grid pattern, positioned above the text "Bio Systems", all enclosed within a thin rectangular border and two horizontal lines at the top.::>

<a id='b880e085-6de4-4101-b056-df4f92738eca'></a>

www.elsevier.com/locate/biosystems

<a id='23a994e4-1b79-48bc-859a-2d2e0048a114'></a>

Modeling insulin kinetics: responses to a single oral glucose
administration or ambulatory-fed conditions

<a id='5f0dd211-4236-4922-9754-82b6d24b4a0d'></a>

Yongwimon Lenbury *, Sitipong Ruktamatakul, Somkid Amornsamarnkul
*Department of Mathematics, Faculty of Science, Mahidol University, Rama 6 Rd., Bangkok 10400, Thailand*
*Received 24 August 2000; accepted 28 August 2000*

<a id='78909ea6-d255-4005-ac4b-4509dd631a8a'></a>

# Abstract

This paper presents a nonlinear mathematical model of the glucose–insulin feedback system, which has been extended to incorporate the ẞ-cells' function on maintaining and regulating plasma insulin level in man. Initially, a gastrointestinal absorption term for glucose is utilized to effect the glucose absorption by the intestine and the subsequent release of glucose into the bloodstream, taking place at a given initial rate and falling off exponentially with time. An analysis of the model is carried out by the singular perturbation technique in order to derive boundary conditions on the system parameters which identify, in particular, the existence of limit cycles in our model system consistent with the oscillatory patterns often observed in clinical data. We then utilize a sinusoidal term to incorporate the temporal absorption of glucose in order to study the responses in the patients under ambulatory-fed conditions. A numerical investigation is carried out in this case to construct a bifurcation diagram to identify the ranges of parametric values for which chaotic behavior can be expected, leading to interesting biological interpretations.
© 2001 Elsevier Science Ireland Ltd. All rights reserved.

<a id='acecbf6b-64ee-4f0d-ab7d-3078ce9e6781'></a>

Keywords: Insulin kinetics; Mathematical model; Periodicity; Chaotic dynamics

<a id='001e7b2e-42ec-472b-bade-807def709407'></a>

# 1. Introduction

It has been established (Bajaj and Rao, 1987) that the secretion of insulin and its biological effectiveness in response to a glucose load is deter- mined mostly by the number and function of -cells in the pancreas, and the peripheral resis- tance to insulin action. Diabetes can arise from insulin deficiency or insulin resistance and several studies have been carried out to determine their

<a id='72189b0a-fb61-431a-9386-317fe64e090e'></a>

* Corresponding author.
E-mail address: scylb@mahidol.ac.th (Y. Lenbury).

<a id='7cfb97b1-465c-429d-9f64-0a2bccce4ac5'></a>

relative contributions toward a patient's hyperglycemia (Turner et al., 1979). A number of mathematical models have been proposed (Ackerman et al., 1964; Geevan et al., 1990) to explain the relationships between the concentrations of glucose and insulin in plasma in response to a glucose load.

<a id='83c54563-6553-429e-927e-1a3199f70718'></a>

These models are usually too complex to be
fitted to the small amount of clinical data avail-
able. Moreover, the data is generally of glucose
concentrations only and has been collected over a
time scale of an experiment, which is too short for
the model's verification (Bajaj and Rao, 1987).

<a id='676c6e72-9d1b-4fb7-b0d4-72c04e170598'></a>

0303-2647/01/$ - see front matter © 2001 Elsevier Science Ireland Ltd. All rights reserved.
PII: S0303-2647(00)00136-2

<!-- PAGE BREAK -->

<a id='6e4e0033-bcc4-4e37-a9b1-1295905b347c'></a>

16

<a id='55472015-d201-44f6-b71d-057bd21a5f22'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='f3bf15e7-da48-476a-a947-8796228e7334'></a>

More importantly, most models prove not to be consistent enough with known physiological data.
On comparing mathematical models, it is no longer sufficient to match numerical simulations to experimental data and choose the best fitting model. We are in a better position if the model can be shown to admit the same dynamic behavior exhibited by real data. Specifically, if sustained oscillatory patterns are observed in the system under study, a model which does not admit such a qualitative behavior must be discarded. As Ackerman et al. (1964) have observed, body or natural rhythms range from very fast ones, such as those of the electro-encephalogram, to very slow ones, such as seasonal variations. Some of these rhythms are induced by the external environment, while others are characteristic of the living organisms. Apart from the oscillations of long periodicity such as those of about 24 h, several physiological variables also show shorter rhythms, which are often regarded as a complication that somehow must be avoided or compensated for in the design of experiments in biology and medicine. Instead, these rhythms should be studied and used as qualitative parameters of the biological system. It was proposed by Ackerman et al. (1964) that the analysis of cyclic variations and periodicity in a system could prove to be a useful tool to help distinguish health from disease.

<a id='2296632c-e7a1-4a64-8c1f-328e3f5a4eee'></a>

A recent model for insulin kinetics, studied by Geevan et al. (1990), involves four variables, incorporating β-cell kinetics, a glucose–insulin feedback system and a gastrointestinal absorption term. Analysis of the model (Bajaj and Rao, 1987) showed that only damped oscillations were admitted in response to an instantaneous oral glucose administration. Several studies have, however, reported persistent cyclic patterns in the plasma glucose and insulin concentrations in man and monkeys (Turner et al., 1979; Tasaka et al., 1994). In another study by Molnar et al. (1972), where immunoreactive insulin measurements were made from ambulatory-fed subjects, plasma insulin and glucose patterns in diabetics showed chaotic behavior during the 48-h observation period.

<a id='fe2e5c2c-ec5c-4b22-b7c0-3a5df3ed0535'></a>

We, therefore, extend the above mentioned
model to take into account the role of the number
of ̒-cells in the regulation of plasma insulin level,

<a id='872c25d8-a927-4e50-8973-521188af61ad'></a>

following the results presented by Turner et al.
(1979) in which the β-cells function in the negative
feedback loop appears to have a predominant role
in regulating both the basal plasma glucose and
insulin concentrations.

<a id='de6dabb8-d8a8-478d-9758-509581e2cf84'></a>

We show, by a singular perturbation analysis,
that the model will admit sustained oscillations
for certain ranges of the system parameters.
Moreover, when a term is incorporated to simu-
late the responses to an ambulatory-fed condition,
we discover that chaotic behavior can be expected
in the system for certain ranges of the system
parameters, yielding irregular patterns consistent
with the physiological data reported by Molnar et
al. (1972).

<a id='66b6f9a4-c1d1-4e20-b7f1-c10198dca17b'></a>

## 2. Model development

Here, we derive an extended model by making the following assumptions. If *x* and *y* represent the differences in the plasma insulin and glucose concentrations from their respective fasting (basal) concentrations, and *z* represents the density of the pancreatic ̒-cells in the proliferative phase, then the rate of change of *x* satisfies the following rate equation.

<a id='1e146cdb-4b7c-4b94-9649-312fb105a4cb'></a>

dx/dt = R_1y - R_2x + C_1 (1)

<a id='08f73ba7-06df-40aa-a86c-a5d1fa3a580b'></a>

where the first term describes the increase in the insulin concentration due to the increase in the plasma glucose concentration; the second term describes the reduction in x due to its access amount, while C₁, is the rate of increase in x in the absence of y and x.

<a id='7471b5d7-b482-4aaf-addc-053389f5bb1e'></a>

Since β-cells function in a negative feedback
loop has been established to take a predominant
role in regulating both the basal plasma glucose
and insulin concentrations (Bajaj and Rao, 1987;
Lenbury et al., 1996), it is reasonable to assume
that the rates R₁ , R₂ and C₁ in Eq. (1) should
depend on the density of β-cells in the prolifera-
tive phase z. Eq. (1) thus becomes

<a id='5a038c84-83ca-4dd6-b359-7d5a16db2e6a'></a>

dx/dt = r_1zy - r_2zx + c_1z (2)

<!-- PAGE BREAK -->

<a id='10c43299-23a4-443d-9e78-85604ad47455'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='b788c24c-c581-4a42-890e-871cf4aae45c'></a>

17

<a id='c1411d4c-cb4b-46df-9c43-c1b43a7996ed'></a>

where linear dependence on z is assumed while r₁, r₂ and c₁ are positive constants. The system is thus considered to be a self-regulative one in a normal subject, where basal plasma glucose level is pre-dominantly determined by insulin secretion from normal β-cells. A decreased number of cells would maintain a normal basal plasma insulin concen-tration by operating at an increased secretory rate per cell. This is reflected by the second term in Eq. (2), which becomes smaller in magnitude as z decreases so that x will be reduced at a slower rate in the event that the number of cells becomes smaller.

<a id='ed2e1477-e0d7-4485-bf30-5bf1d34c0471'></a>

As for the plasma glucose level y, if there is a decrease in insulin secretion due to a reduction to 1/N of the normal number, n, of β-cells, the basal plasma glucose will increase until nearly normal basal insulin levels are obtained (Bajaj and Rao, 1987). Thus, the plasma glucose level is a function of the β-cell capacity, N/n. Therefore, plasma glucose is assumed to satisfy the following rate equation.

<a id='39718fd1-c431-4f95-949d-cb4c5e52d9d7'></a>

dy/dt = R3N / z - R4x + C2 + w(t) (3)

<a id='9ddbcea4-4c28-4ac5-9f57-71dbd0823695'></a>

where the first term accounts for the hyperbolic increase in y due to a reduction in the number of β-cells, supported by the study of Turner et al., (1979) mentioned previously. The second term accounts for the reduction in y due to the regula- tive effect of plasma insulin, while C₂ accounts for the change in y in the absence of x and z. The last term in Eq. (3) corresponds to the variation in the gastrointestinal absorption with time, accounting for the absorption by the intestine and the subse- quent release of glucose into the bloodstream.

<a id='55313b64-3daa-4c8a-8501-47b7ca23e51d'></a>

Finally, the density of pancreatic ̓-cells in the proliferative phase satisfies the following equation used in the work of Rao et al. (1990):

<a id='e80d2719-5aaf-4e40-ae64-681860d13f0b'></a>

dz/dt = R₅(y - ŷ)(T - z) + R₆z(T - z) - R₇z (4)

<a id='eabba53d-5824-4c42-a52c-fd7d7a8920f7'></a>

where ŷ is the difference between the normal
glucose level and its basal concentration, T is the
total density of dividing and non-dividing β-cells,
while R₅, R₆, and R₇ are rate constants. The first
term accounts for the increase in z due to the
interaction between the plasma glucose above the

<a id='1683ac75-fa2a-40b8-a12b-2b84ab569fee'></a>

basal level and the non-dividing ̖-cells, while the
second term represents the increase in the dividing
̖-cells from the interaction between the dividing
and non-dividing cells. The last term is the rate of
reduction in the cells density, proportional to its
current level with a rate constant R₇.

<a id='bd3d96ef-5a45-4a9f-a102-f3885e5172cd'></a>

Thus, our reference model consists of Eqs. (2)–(4).

<a id='d8ce487e-f754-447f-963c-143e1ee44988'></a>

### 3. Single oral glucose administration
When a single oral glucose administration is utilized, a gastrointestinal absorption term $w(t)$ is assumed to have the form

$w(t) = \frac{1}{p + e^{xt}}$ (5)

which means that the absorption by the intestine and the subsequent release of glucose into the bloodstream takes place at an initial rate

$w_0 = \frac{1}{p + 1}$ (6)

<a id='15add076-3e44-4ed7-80a0-86a0bece9dd0'></a>

and then falls off exponentially with time (Rao et al., 1990).
On substituting Eq. (5) into Eq. (3) and differentiating w(t), we can eliminate the time dependence of the term w(t) by considering instead the following system of four autonomous differential equations

$\frac{dx}{dt} = z(r_1y - r_2x + c_1)$, $x(0) = x_0$ (7)

$\frac{dy}{dt} = \frac{R_3N}{z} - R_4x + C_2 + w$, $y(0) = y_0$ (8)

$\frac{dx}{dt} = R_5(y - \hat{y})(T-z) + R_6z(T-z) - R_7z$,
$z(0) = z_0$ (9)

$\frac{dw}{dt} = - \alpha w + \alpha pw^2$ $w(0) = w_0$ (10)

<a id='d8d01958-51e5-4d99-a4bb-c93c112b49dd'></a>

### 4. Singular perturbation analysis
At this point, we first observe that, the con-stants $\alpha$ and $p$ determine the rapidity of glucose

<!-- PAGE BREAK -->

<a id='26dee761-894e-427e-bab4-00de788a96bc'></a>

18

<a id='ef4fbddd-f15f-4e13-8f5c-25ae74f39a55'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='3011b9df-9d46-4179-a9f7-d5241939d2aa'></a>

absorption. Thus, if a is high, the gastrointestinal
absorption process equilibrates very quickly to the
steady state w=0 of Eq. (10), which is stable.
This means that as time passes w becomes infi-
nitesimally small and the system model reduces to
Eqs. (7)-(9) with w = 0.

<a id='9914ddd6-5005-4bbc-8720-4ba9098ed1ee'></a>

In order to analyze the resulting model equations (Eqs. (7)–(9)) with w = 0 by a singular perturbation technique, we scale the dynamics of the three remaining hierarchical components of the system, namely x, y and z, by means of two small dimensionless positive parameters ε and δ.

<a id='9bc26a6e-4eae-4835-acd4-57fa19e87fa7'></a>

Letting ẑ = T, r₃ = R₃N/ε, r₄ = R₄/ε, r₅ = R₅/εδ, r₆ = R₆/εδ, r₇ = R₇/εδ, and c₂ = C₂/ε, we are led to the following system of differential equations.

<a id='0fa96b89-edff-49ab-85eb-c23ae25299d2'></a>

dx/dt = z(r₁y - r₂x + c₁) ≡ f(x, y, z) (11)

<a id='64a4b424-ca3f-4fc7-a389-a0dc016a4422'></a>

dy/dt = ε[r_3 / z - r_4 x + c_2] ≡ εg(x, y, z) (12)

<a id='a10838a5-ce81-4114-bc80-f3c07b612de9'></a>

$$\frac{dz}{dt} = r_5(y - \hat{y})(\hat{z} - z) + r_6z(\hat{z} - z) - r_7z$$ 
$$\equiv \varepsilon\delta h(x, y, z) \quad (13)$$

<a id='aaf4190d-60f3-4b25-a0e4-28084595e060'></a>

which means that during transitions, when the
right sides of Eqs. (11)-(13) are finite but differ-
ent from zero, |ẏ| is of the order ε, and |ż| is of
order εδ. Thus, we have assumed that insulin
formation has faster time response than that of
plasma glucose, and the β-cells proliferation pos-
sesses the slowest dynamics.

<a id='f2ab808d-059b-4890-aed6-1649927744ea'></a>

It is well known (Muratori, 1991; Muratori and Rinaldi, 1992; Lenbury et al., 1996) that the system (Eqs. (11)-(13)), when \(\varepsilon\) and \(\delta\) are small, can be analyzed with the singular perturbation method which, under suitable regularity conditions, allows approximation of the solution of the system by a sequence of simple dynamic transitions occurring at different speeds. The resulting curve, composed of these transitions, approximates the actual solution in the sense that the real trajectory is contained in a tube around the curve, and that the radius of the tube goes to zero with \(\varepsilon\), and \(\delta\).

<a id='039d9c4d-d9d2-4a68-98e4-595e2fec2f00'></a>

4.1. On the manifold f = 0

<a id='9b49fc72-02c0-4731-816a-d777ab100ef5'></a>

This consists of the trivial manifold z = 0 and
the nontrivial one given by the equation

<a id='a0880e2a-8d31-47d8-9eb1-87ac9a880514'></a>

$$x = \frac{r_1}{r_2}y + \frac{c_1}{r_2}\quad(14)$$

<a id='54954a44-22ce-490a-ba2d-1016e65dd1bf'></a>

The above equation describes a plane in the (x,
y, z)-space which is parallel to the z-axis. It
intersects the (x, z)-plane along the line

<a id='91ddf3c8-55ea-42f5-b2c5-86a96bee5dd5'></a>

x = c_1 / r_2 = x_1 (15)

<a id='1f4d36fe-90bd-413c-bbd6-e954224a94c1'></a>

as shown in Fig. 1.

<a id='d9f81c86-8586-4d69-a6aa-4cef9e48a5b3'></a>

4.2. On the manifold h = 0

This is the surface

<a id='c94dcb9d-f48c-4526-b7dd-62bae6565f2d'></a>

y = \pi(z) \equiv \hat{y} - \frac{r_6 Z}{r_5} + \frac{r_7 Z}{r_5(\hat{z} - z)} \quad (16)

<a id='7f8d8aac-d8f3-4274-abe7-3ff09d906a10'></a>

for which

<a id='a1644183-2be4-4b73-a06c-205cef2907d7'></a>

$\pi'(z) = -\frac{r_6}{r_5} + \frac{r_7 \hat{z}}{r_5 (\hat{z} - z)^2}$ (17)

<a id='04167905-6a50-4559-b447-03f223dd6e0a'></a>

<::A 3D diagram illustrating the shapes and relative positions of equilibrium manifolds in a system exhibiting a limit cycle. The coordinate system consists of x, y, and z axes. Various surfaces and planes are shown, including those labeled f=0, g=0, h=0, f=h=0, and f=g=0. A trajectory is depicted on these manifolds, passing through points labeled A, B, C, D, E, F, G, P, S. Arrows along the trajectory indicate transition speeds: three arrows signify fast transitions (e.g., from P to E, from D to S, from G to C, from A to B), two arrows signify transitions at intermediate speed (e.g., from E to S, from C to G), and a single arrow signifies slow transitions (e.g., from S to D, from B to C). The diagram also marks coordinate values x1, x2, x3 on the x-axis, y1 on the y-axis, and z1 on the z-axis, with the origin at O. Dashed lines represent projections or hidden parts of the geometry.: diagram::>

Fig. 1. Shapes and relative positions of the equilibrium manifolds in the case where a limit cycle exists. Here, three arrows indicate fast transitions, two arrows indicate transitions at intermediate speed, and a single arrow indicates slow transitions.

<!-- PAGE BREAK -->

<a id='a8601397-8d70-45c8-b430-179c4c2f5b2a'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='8cbb245a-3b44-4650-85d4-5e2554687310'></a>

19

<a id='81e65abf-00e2-4ed4-9ae7-66ffea98ce41'></a>

Setting π'(z) = 0, one obtains

z = ẑ ± √(
r₇ẑ
---
r₆
)

<a id='42011289-ee16-4646-8b3b-5f5b66f6b2b7'></a>

Since it is necessary that $z \leq \hat{z}$, we consider only the critical point where

<a id='0a784069-10a8-4392-aa3c-5e6926ae03b8'></a>

z = ẑ - √( r₇ẑ / r₆ ) ≡ z₁ ≤ ẑ (18)

<a id='a4555e31-8247-41bf-a3b6-440eee339429'></a>

Moreover, since

$\pi"(z) = \frac{2r_7\hat{z}}{r_5(\hat{z} - z)^3}$ (19)

<a id='19830a7b-0bdb-42f1-ae90-3f3f7fe0de97'></a>

we have

<a id='66be108d-31f7-4c00-b0ff-1caa128817e9'></a>

\pi''(z_1) = \frac{2r_6}{r_5}\sqrt{\frac{r_6}{r_7\hat{z}^2}} > 0

<a id='4d9abe28-798f-418f-a0ca-690fec9c6886'></a>

for positive parametric values. Thus, z is a mini-
mum at the point z = z₁, on this surface. Substi-
tuting z₁ into Eq. (16), one obtains

<a id='8578350a-4cab-47f0-ba46-08ab97dea629'></a>

\pi(z_1) = \hat{y} - \frac{1}{\sqrt{r_5}}(\sqrt{r_7} - \sqrt{r_6}\hat{z})^2 \equiv y_1 (20)

<a id='f3f49843-e8fd-4a0e-967c-5ccd161f5fac'></a>

Also, if z = 0 on this surface, then
z = ź

<a id='49c889d2-dcc1-45ed-be9c-4914b85a1fad'></a>

which is where the manifold intersects the (x,
y)-plane, as shown in Fig. 1.

<a id='83846feb-500e-4923-b734-fb8e58943cca'></a>

We observe further that the slow manifold given by Eq. (16) is parallel to the x-axis and intersects the (y, z)-plane along a curve on which y becomes a minimum at the point where z = z1.

<a id='e03198a7-58e0-42e8-a446-8a67aeb32b93'></a>

Moreover, the manifold $h = 0$ intersects the
plane of the manifold $f=0$ along the parabolic
curve given by the equation

<a id='9f5a6327-ca55-4820-8a42-eae722434ebb'></a>

x = ̓(y, z)

<a id='9cdca4d0-ab72-460d-869c-c12e7619aca0'></a>

≡ (1/r₂) [r₁y + c₁ + r₇z - r₅(y - ŷ)(ŵ - z)
- r₆z(ŵ - z)]
(21)

<a id='72d55730-163f-464f-b6a0-b19b1fb73eba'></a>

Substituting y₁ and z₁, in the above equation,
we obtain
x = (1/r₂) [ r₁ŷ - (r₁r₇ / r₅) + (2r₁ / r₅)√(r₆r₇ẑ - r₁r₆ẑ / r₅) + c₁ ] ≡ x₂
(22)

<a id='6fbdcc7f-ac03-4d2d-89eb-2387c38d49e1'></a>

also shown in Fig. 1.
On the other hand, on substituting y = ŷ and
z = 0 in Eq. (21), we obtain

<a id='0827034a-c2fb-408b-8e0d-f2d9d9fc7c2d'></a>

x = \frac{1}{r_2}[r_1\hat{y} + c_1] \equiv x_3 (23)

<a id='371d7d07-88ac-4aa6-8f94-0fece929a7ee'></a>

However, on considering Eqs. (22) and (23), we
find that x3 > x2 for all positive parametric values.

<a id='52b45f88-5dd6-407e-aca4-27daa71350e8'></a>

Now, for a constant y, ψ is a decreasing function of z on the interval (0, z₁), that is, x decreases along the curve given by Eq. (21) from the point (x, y, z) = (x₃, ŷ, 0), or point P in Fig. 1, to the point (x, y, z) = (x₂, y₁, z₁), or point D, along the curve PD in Fig. 1.

<a id='c884848a-2597-40ce-bd7d-41473f5e1c40'></a>

4.3. On the manifold g = 0

<a id='641951a0-2c01-4caa-a959-bc8cb13acd53'></a>

This is the cylindrical surface given by

<a id='667fb342-a83e-4a68-9ddc-8fa486b8ef12'></a>

x = \phi(z) \equiv \frac{r_3}{r_4z} + \frac{c_2}{r_4}
(24)

<a id='ac9a36e3-1401-4789-88da-8fed79b191a2'></a>

which is parallel to the y-axis and intersects the
(x, z)-plane along a hyperbola. As z tends toward
infinity along this surface, x tends toward the
value c2/r4.

<a id='c815b356-bb31-4475-a8ed-f1dfab8943e9'></a>

Since φ(z) is a monotonically decreasing func-
tion of z, if z₁ > 0 then x is decreasing for z in the
interval (0, z₁). Substituting z = z₁ into Eq. (24),
we obtain

<a id='fc5ff884-bb90-42d6-b1df-70410959c0bc'></a>

x = \frac{r_3}{r_4 z_1} + \frac{c_2}{r_4} \equiv x_4 (25)

<a id='2d34f284-48f0-4dd5-ad7a-3f9a9837c881'></a>

Thus, by requiring that

<a id='8ff1fab2-78ff-490f-b20d-67e9ff82f631'></a>

0 < (r_3 + c_2 z_1) / (r_4 z_1)

<a id='c9727485-efa6-447a-b4e4-4f6f9d51b549'></a>

$$ < \frac{r_1r_5\hat{y} - r_1r_7 + 2r_1\sqrt{r_6r_7\hat{z} - r_1r_6\hat{z}} + c_1r_5}{r_2r_5} \quad (26) $$

<a id='2c85f6c4-c7c9-4c84-8cb9-3e935f6d6b16'></a>

we are assured that $0 < x_4 < x_2$ and the surface $f = g = 0$ intersects the curve $f = h = 0$ at the point S which is located on the unstable portion PD of the curve. In other words, the manifold $g = 0$ separates the two stable submanifolds $z = 0$ and $f = h = 0$, on the former of which $g > 0$ while $g < 0$ on the latter. The stability of the manifolds is determined by the signs of $f$, $g$, and $h$. If we further require that

<a id='aad4376d-9292-4706-bcea-b9fb381391b5'></a>

$\hat{y} > \frac{(\sqrt{r_7} - \sqrt{r_6 \hat{z}})^2}{\sqrt{r_5}}$ (27)

<a id='08012f3d-8e78-42a8-b548-c4566fa3c7ee'></a>

and

<!-- PAGE BREAK -->

<a id='6b93b2bd-598b-45e0-b53d-04c36cd405df'></a>

20

<a id='1ea91eb0-65ac-4b86-90d7-11809b8e1280'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='fda372ed-0d3a-4193-acfa-f5a2aa60f210'></a>

$\hat{z} > \frac{r_7}{r_6}$

<a id='10dea83d-7ecd-4e96-958a-34fe369dc381'></a>

(28)

<a id='ce76207c-d4a1-4563-af0b-ef9a29dbc01c'></a>

then, on considering Eqs. (18) and (20), we are
assured that y₁ > 0 and z₁ > 0.

<a id='60acd00d-c19d-40c2-b06a-479841d99d65'></a>

Under these conditions, the shapes and relative
positions of the equilibrium manifolds f= 0, g =
0, and h = 0 will be as depicted in Fig. 1, where
three arrows indicate fast transitions, two arrows
indicate intermediate ones, while a single arrow
indicates slow ones.

<a id='83f0e33f-cef1-4f76-8f9e-175555fded08'></a>

Thus, a system initially at a generic point, say
point A of Fig. 1, will make a quick transition to
the plane given by Eq. (14) on the fast manifold
f= 0 (point B in Fig. 1), since the signs of f assure
us that this part of the manifold f = 0 is stable. As
the plane where f = 0 is approached, y has slowly
become active. A transition at an intermediate
speed is made along f= 0 in the direction of
decreasing y, since g <0 here, to the point C on a
stable part of the curve f= h = 0. From the point
C, a slow transition is then made along this curve
in the direction of decreasing y, since g is still
negative here.

<a id='af9e9e66-39e0-47ad-af66-62a9e63f26a1'></a>

Once the point D is reached, the stability of the manifold is lost, a catastrophic transition brings the system to point E on the manifold z = 0 where it intersects the plane given by Eq. (14). Consequently, the system will slowly develop along this line in the direction of increasing y, since g is now positive.

<a id='bbd00009-da75-495d-9fe5-4f81ae33750f'></a>

At a point F on the plane z = 0, the stability will again be lost and a quick transition will bring the system back to the point G on the stable branch of the curve f= h = 0, before repeating the same previously described path, thereby forming a closed cycle GDEFG. Thus, the existence of a limit cycle in the system for ɛ and δ sufficiently small is assured. The exact solution trajectory of the system will be contained in a tube about this closed curve, the radius of which tends to zero with ɛ and δ.

<a id='1fccdaf0-cbb4-4aa8-aab5-0e5c48628b8c'></a>

The above arguments can be summarized by
the following theorem.

<a id='54397752-8eee-4d09-9653-6178e1d5d151'></a>

**Theorem 1.** *If inequalities (Eqs. (26)–(28)) hold, and ɛ and δ are sufficiently small, then the system of Eqs. (11)–(13) has a global attractor, in the positive octant of the phase space, which is a limit*

<a id='924411c5-5c73-45ec-8332-cffe54891979'></a>

_cycle composed of a concatenation of catastrophic transitions occurring at different speeds._

<a id='338e6f60-ea81-484d-9cd8-d3f37dc2044b'></a>

A computer simulation of Eqs. (11)-(13) is presented in Fig. 2a, with parametric values chosen to satisfy inequalities (Eqs. (26)-(28)) identified in the above theorem. The solution trajectory, projected onto the (y, x)-plane, is seen here to tend towards a limit cycle as theoretically predicted. The corresponding time series of insulin (x) and glucose (y) are shown in Fig. 2b.

<a id='4162f682-43af-4d25-84cf-9da3b57746c7'></a>

### 5. Ambulatory-fed conditions and chaotic behavior

We now extend our model to incorporate temporal glucose absorption in order to model the responses of a subject under ambulatory-fed conditions. The term w(t) in Eq. (3) is then taken in this case to assume the sinusoidal form

`w(t) ≡ k sin ωt`

(29)

<a id='0fa3bd0a-e415-49ba-8e15-10f70569d656'></a>

We then remove the explicit dependence on
time of the above oscillatory term by letting
$u = \cos \omega t$

<a id='6677fdf1-177d-485f-bf50-5ebc16be5a66'></a>

and

v = sin ωt

which transforms the model equations into the following five-dimensional system of autonomous differential equations.

ẋ = z[r₁y − r₂x + c₁] (30)
ẏ = ε[r₃/z − r₄x + c₂ + c₃u] (31)
ż = εδ[r₅(y − ŷ)(ẑ − z) + r₆z(ẑ − z) − r₇z] (32)
u̇ = −ωv (33)
v̇ = ωu (34)

<a id='e29ce98e-565c-4b7f-ad49-5d5d4f008539'></a>

and
c₃ = k / ε

<a id='57df86cb-aa6a-4fc5-b6b3-b901535688fd'></a>

We now carry out a numerical investigation to
determine the ranges of parametric values where
chaotic dynamics were likely. Since it has been

<!-- PAGE BREAK -->

<a id='d5f1d5dc-0bde-44c1-a0e5-538730aa89ff'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='8c1559a2-ce4b-4740-bceb-07cf00162c99'></a>

21

<a id='835d9e99-3e79-4771-98da-62520d5becb6'></a>

<::Figure: chart::>Fig. 2. A computer simulation of the model system of Eqs. (11)–(13) with parametric values chosen to satisfy the conditions identified in the text for which periodic solutions exist. The solution trajectory, projected onto the (y, x)-plane, is seen in Fig. 2a to tend toward a stable limit cycle as theoretically predicted. The corresponding time series of plasma insulin (x) and glucose (y) are shown in Fig. 2b. Here, ε = 0.1; δ = 0.01; r₁ = 0.2; r₂ = 0.1; r₃ = 0.1; r₄ = 0.1; r₅ = 0.1; r₆ = 0.1; r₇ = 0.05; c₁ = 0.1; c₂ = 0.1; ŷ = 1.24; ź = 2.0; and N = 0.1.

Fig. 2a shows a phase portrait with 'x' on the y-axis (ranging from 1 to 5) and 'y' on the x-axis (ranging from 0.0 to 2.0). A trajectory starts from the bottom left and spirals inward, eventually forming a stable limit cycle at the top left.

Fig. 2b shows two time series plots. The left plot has 'x' on the y-axis (ranging from 4.200 to 4.700) and 't' on the x-axis (ranging from 25000 to 33000). The plot displays a periodic oscillation for 'x'. The right plot has 'y' on the y-axis (ranging from 0.000 to 2.500) and 't' on the x-axis (ranging from 25000 to 33000). This plot also displays a periodic oscillation for 'y'.<::/Figure::>

<a id='a651deb2-f78b-4cb6-9189-560115a1b044'></a>

discovered by some researchers (Hastings and Powell, 1991; Lenbury et al., 1999) that one may be able to generate chaos in a nonlinear system which already exhibits limit cycle behavior, we choose parametric values that would lead to cycling in the x, y and z components, guided by our work in the previous section.

<a id='9c03ac8b-02bb-4b17-a0e6-fa6644235d65'></a>

We then let the system run for 10^5 time steps, and examining only the last 8 × 10^4 time steps to eliminate transient behavior. Using the values of ẑ between 0.985 and 1.038, and changing ẑ in steps of 10^-5, the relative maximum values x_max of x are collected during the last 8 × 10^4 time steps. They are then plotted as a function of ẑ as shown in Fig. 3. We discover in this bifurcation diagram the appearance of a period doubling route to chaos, which resembles the dynamics of one-dimensional difference equations such as the logistic population model. Thus, the system of Eqs. (30)–(34) appears to exhibit chaotic dynamics for values of ẑ between 1.000 and 1.038.

<a id='290c0cfa-72d8-454b-91be-744e48ba2ac7'></a>

A computer simulation of the model system (Eqs. (30)–(34)), with parametric values chosen under the above mentioned guidelines and ẑ = 1.01 in the chaotic range, is presented in Fig. 4a, showing the strange attractor projected onto the (y, z)-plane, and the corresponding chaotic time courses of plasma insulin (x) and glucose (y) are presented in Fig. 4b.

<a id='4d973250-70a2-4c0a-ad3b-7509f61bcc2b'></a>

## 6. Discussion and conclusion

In a situation where chaotic dynamics are observed, a small change in the initial conditions may lead to drastically different dynamic behavior. Thus, even a slight perturbation in the insulin concentration may lead to unpredictable results through time.

<a id='68f6ccb1-5e13-4f97-8f99-815ccc3a3dcf'></a>

In some diabetic patients, it can be difficult to
establish appropriate schedules for insulin admin-
istrations. In these patients, programmed insulin

<!-- PAGE BREAK -->

<a id='b3c958c7-8fc6-4c31-a487-73d904d6562f'></a>

22

<a id='15d2e2d7-bff6-4a58-8195-51c20c142a8d'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='8b065b17-b146-421d-9c5d-0f72608ab8d9'></a>

administration combined with regular eating and
exercise schedules is ineffective in maintaining
blood glucose within normal limits. Rather, there
can be apparently irregular fluctuations (Molnar
et al., 1972), for example, in blood glucose moni-
tored upon rising. The unpredictability of glucose
or insulin patterns could generate many control
problems. A low insulin concentration can result
in polyuria and circulatory shocks. Conversely, a
high insulin concentration indicates possibility of
convulsion, sympathetic over-activity and loss of
consciousness.

<a id='57db3495-6dd7-4fbc-9613-cf66bdf02514'></a>

On the other hand, a reduction in blood glucose levels below 45–55 mg/100 ml for a continued interval of time will lead to an impairment of brain function, tremors, and convulsions due to activation of the sympathetic nervous system and, ultimately, death (Norman and Litwack, 1997). Hence, it is necessary to develop protocols for insulin administration based on a knowledge of ambient blood-sugar levels and an understanding of the dynamics of the glucose control system.

<a id='4d486851-5b74-45ce-9eff-f0952336b828'></a>

In the paper by Tasaka et al. (1994), clinical
data was reported where irregular patterns were
observed in the time courses of plasma insulin
levels. Earlier, Molnar et al. reported immunore-
active-insulin (IRI) measurements made during
studies in ambulatory-fed subjects. It was pointed

<a id='ae7da5b7-7115-4fd8-a87d-2401c4854b98'></a>

out that in normal subjects, an IRI increase oc-
curred after every increased blood glucose (BG).
In an unstable diabetics, however, there were
fewer IRI increases and these increases bore a less
regular relationship in time to the BG increases
which followed the meals. We observe that the
reported IRI and BG patterns, shown in Fig. 5,
appear more irregular in an unstable diabetics
than in a normal subject.

<a id='2d7d3bb6-598f-4c0f-b1a0-a39e5df47ab6'></a>

We have been able to discover in our model the possibility of chaotic behavior with the appearance of a strange attractor for the values of ẑ in the approximate range 1.000 < ẑ < 1.038. On the other hand, periodic oscillations in the three components of our system are observed if 0.98 < ẑ < 1.0, and other parametric values are as in the bifurcation diagram shown in Fig. 3. We have thus found that the bifurcation parameter, which delineates various dynamic behaviors in our system is the total density ẑ of β-cells.

<a id='94d85a7e-75d9-420e-a05a-78c8a95c65b7'></a>

In comparison, it was discovered in our earlier
study (Lenbury et al., 1996) that the critical
parameter which differentiates the various dynam-
ical behaviors clinically observed in the electrical
activities in the ̖-cells is, in fact, that which is
related to cell shape and volume, among other
channel conductance related parameters. It has
been well established that such electrical activities

<a id='1cd83abd-6252-4b59-a545-ecdc95ebba3b'></a>

<::Bifurcation diagram chart:The chart shows x_max on the y-axis, ranging from 4.50 to 5.50, and ẑ on the x-axis, ranging from 0.9750 to 1.0375. The plot illustrates a bifurcation diagram. Initially, there are distinct branches of x_max values, which undergo period-doubling bifurcations as ẑ increases, leading to a complex, seemingly chaotic region with many dense points at higher ẑ values. The diagram shows multiple splits from single branches into two, then four, and eventually into a broad band of values. Fig. 3. Bifurcation diagram for the model system of Eqs. (11)-(13) with ε= 0.1, δ = 0.01, r₁ = 0.15, r₂ = 0.12, r₃ = 0.05, r₄ = 0.03, r₅ = 0.09, r₆ = 0.1, r₇ = 0.05, c₁ = 0.1, c₂ = 0.1, ŷ = 1.08, N = 0.1, c₃ = 0.005, ω = 0.05, and 0.985 < ẑ < 1.037. Plots are of x_max vs. ẑ.::>

<!-- PAGE BREAK -->

<a id='383db236-5eae-44d5-9b97-a32dccca2890'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='57e99b2d-0963-4139-8f37-f3a99dd1383a'></a>

23

<a id='b7146a26-8ffb-4108-abca-188a9b55a3ad'></a>

<::chart: Fig. 4a is a 2D plot showing a strange attractor. The y-axis is labeled 'x' and ranges from 2 to 6. The x-axis is labeled 'y' and ranges from -5.0 to 7.5. Fig. 4b consists of two time series plots. The left plot shows the time series of plasma insulin (x), with the y-axis labeled 'x' ranging from 2 to 6, and the x-axis labeled 't' ranging from 40000 to 55000. The right plot shows the time series of glucose (y), with the y-axis labeled 'y' ranging from -5.0 to 7.5, and the x-axis labeled 't' ranging from 40000 to 50000.::>Fig. 4. A computer simulation of the model system of Eqs. (11)–(13) with parametric values of Fig. 3 and ž = 1.01 in the chaotic range, showing a strange attractor projected onto the (y, z)-plane in Fig. 4a. The corresponding time series of plasma insulin (x) and glucose (y) are shown in Fig. 4b.

<a id='14281312-81f2-4a12-833e-f23bb18d5046'></a>

are closely related to insulin secretion and the regulation of plasma glucose. Chaotic behavior in the potential difference component, which will result when the critical parameter falls within certain ranges can be indicative of irregularities in the underlying mechanisms of the system under study.

<a id='00894025-66d7-40e3-a6b4-adbe53058e04'></a>

To summarize, we have demonstrated in this
paper that our system model consisting of Eqs.
(7)-(9) can exhibit sustained oscillations after an
initial dose of glucose. It can also exhibit chaotic
dynamics under ambulatory-fed conditions, con-

<a id='99004a6f-40e4-4714-9cc1-ea54762721b2'></a>

sistent with the reported clinical data. Our investigation demonstrates how the frequency of IRI increases is interfered with by the added frequency of meals being fed. When synchrony is disturbed further in a patient with impaired glucose-insulin regulation system, a period doubling route to chaotic dynamics may be observed.

<a id='dfa51f28-a81d-4b10-a41c-e230f047034c'></a>

We further note that, in the clinical data re-
ported by Molnar et al. (1972), blood glucose
levels oscillate over wider ranges and the averaged
plasma insulin is higher in the diabetic patients
than in the normal subjects. In Fig. 5a, the glu-

<!-- PAGE BREAK -->

<a id='ef44d7f8-25b5-452d-be81-00b4e7990241'></a>

24

<a id='de36c0ef-f27b-43b6-8c01-ffc9d968562d'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='c60b1579-fd25-48c3-8fdd-94a3f95b56aa'></a>

<::chart: Two line graphs, labeled (a) and (b), showing variations in IRI and BG over 48 hours. Both graphs share a common x-axis labeled "CLOCK TIME" ranging from 07 to 19, repeated over two 24-hour cycles. The y-axis on the left shows "IRI" (Insulin Reactivity Index) with values from 0 to 80 (for graph a) and 0 to 100 (for graph b). Below the IRI axis, there's a second y-axis for "BG" (Blood Glucose) with values from 0 to 200 (for graph a) and 0 to 300 (for graph b). Above each graph, meal times are indicated by letters: B (breakfast), L (lunch), K (snack), D (dinner), U (supper), occurring approximately every 6 hours.  Graph (a) depicts data for normal subjects, showing IRI fluctuating between 0 and about 70, and BG fluctuating between 0 and about 150. Graph (b) depicts data for diabetics, showing IRI fluctuating between 20 and about 100, and BG fluctuating between 100 and about 250, generally at higher levels than in graph (a). Both IRI and BG levels show fluctuations around meal times. Fig. 5. Variations in IRI (in mg/100 ml) and BG (in µU/ml) during 48 h continuous monitoring. Clocktime is shown in hours and major meals were taken at 6-h intervals. B, breakfast; L, lunch; K, snack; D, dinner; U, supper; normal subjects in (a); diabetics in (b). Data is taken from Molnar et al. (1972).::>

<a id='8c87d9b1-ac91-46a3-a646-437cd81bbd01'></a>

cose pattern of a normal subject shows very low peaks, while the insulin level oscillates between zero and maximum levels of no more than 80 U/ml. The diabetic patient's data in Fig. 5b, on the other hand, shows higher glucose peaks, and the plasma insulin oscillates between 20 and 100 U/ml. On comparing our simulation results in Fig. 2, for the periodic case, and Fig. 4, for the chaotic case, we see that our model exhibits the same qualitative difference, which has been observed clinically in the corresponding cases of normal subjects and diabetic patients.

<a id='cac0903f-a7f8-45ab-b93d-f6ed7f68882e'></a>

Thus, this study shows how such insights gained from our analysis can have clinical utility in distinguishing health from disease. More in-depth studies and sufficient amounts of additional data should allow us to establish a stronger linkage between the dynamic behavior of the model and the clinically observed patterns, and lead us in the right direction towards our being eventually in the position to make certain reliable predictions regarding the control strategies and effective therapy of diabetes mellitus.

<a id='50846cf0-7349-48f1-b836-86878dfd3941'></a>

Acknowledgements

The authors would like to extend their deepest
appreciation to the Thailand Research Fund for
supporting this research project (contract number
RTA/02/2542).

<a id='78f78afd-124c-4770-a300-86f362a32425'></a>

# References

Ackerman, E., Rosevear, J.W., McGuckin, W.F., 1964. A mathematical model for glucose-tolerance test. Phys. Med. Biol. 9 (2), 203-213.

Bajaj, J.S., Rao, G.S., 1987. A mathematical model for insulin kinetics and its application to protein-deficient (malnutrition-related) diabetes mellitus (PDDM). J. Theor. Biol. 129, 491-503.

Geevan, C.P., Rao, S., Rao, G.S., Bajaj, J.S., 1990. A mathematical model for insulin kinetics III. Sensitivity analysis of the model. J. Theor. Biol. 147, 255-263.

Hastings, A., Powell, T., 1991. Chaos in a three-species food chain. Ecology 72 (3), 896-903.

Lenbury, Y., Kumnungkit, K., Novaprateep, B., 1996. Detection of slow-fast cycles in a model for electrical activity in the pancreatic ̒-cell. IMA J. Math. Appl. Med. Biol. 13, 1-21.

Lenbury, Y., Rattanamongkonkul, S., Tumrasvin, N., Amornsamarnkul, S., 1999. Predator prey interaction coupled by parasitic infection: limit cycles and chaotic behavior. Math. Comp. Model. 30, 131-146.

Molnar, G.D., Taylor, W.F., Langworthy, A.L., 1972. Plasma immunoreactive insulin patterns in insulin-treated diabetics: studies during continuous blood glucose monitoring. Mayo Clin. Proc. 47, 709-719.

Muratori, S., 1991. An application of the separation principle for detecting slow-fast limit cycles in a three-dimensional system. Appl. Math. Comput. 43, 1-18.

Muratori, S., Rinaldi, S., 1992. Low- and high-frequency oscillations in three-dimensional food chain systems. 52, 1688-1706.

Norman, A.W., Litwack, G., 1997. Hormones, second ed. Academic Press, California.

Rao, G.S., Bajaj, J.S., Rao, J.S., 1990. A mathematical model for insulin kinetics II. Extension of the model to include response to oral glucose administration and application to insulin-dependent diabetes mellitus (IDDM). J. Theor. Biol. 142, 473-483.

<!-- PAGE BREAK -->

<a id='d5ad7ea8-b364-47c4-9236-df78d4e249f3'></a>

Y. Lenbury et al. / BioSystems 59 (2001) 15–25

<a id='ec96eca3-599b-4a2d-a9ac-117dc3f2bd87'></a>

25

<a id='4c29a14e-58b3-43e7-bcd0-1b19aac9c414'></a>

Tasaka, Y., Nakaya, F., Matsumoto, H., Omori, Y., 1994.
Effect of aminoguanidine on insulin release from pancreatic
islet. Endocr. J. 41 (3), 309–313.
Turner, R.C., Holman, R.R., Mattthews, D.R., Hockaday,

<a id='66dffbdf-acaa-46b0-8f03-92690251502e'></a>

D.R., Peto, J., 1979. Insulin deficiency and insulin resistance
interaction in diabetes: estimation of their relative contribu-
tion by feedback analysis from basal plasma insulin and
glucose concentrations. Metabolism 28 (11), 1086-1096.
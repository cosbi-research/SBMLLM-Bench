<a id='5962fb03-83b9-41ca-b443-fee67a68f7af'></a>

<::logo: Elsevier
ELSEVIER
This logo features a detailed black and white illustration of a tree with two figures beneath it, and a snake wrapped around the tree, with the company name in black capital letters below the illustration::>

<a id='9af6c308-746b-4b76-81cd-ff65a6be41fa'></a>

Available online at www.sciencedirect.com
SCIENCE @ DIRECT®

<a id='4915b143-4c5d-49e8-8269-364d93e717ad'></a>

<::logo: Mathematical Biosciences
Mathematical Biosciences
The logo features the words "Mathematical Biosciences" in bold, italicized black font on a white background.::>

<a id='4f0de884-2ba7-47a0-bc3e-ea1b44cce05c'></a>

Mathematical Biosciences 189 (2004) 185–217

<a id='cabdf42d-5604-422c-8fc5-cf6f71204fcf'></a>

www.elsevier.com/locate/mbs

<a id='85648bbf-725a-44bc-b5dd-52b8107db48f'></a>

A mathematical model for the in vitro kinetics
of the anti-cancer agent topotecan

<a id='ba6c6a7a-a5d7-4a3a-8edf-ead798b738e9'></a>

Neil D. Evans a, Rachel J. Errington b, Michael Shelley c, Graham P. Feeney d,
Michael J. Chapman e, Keith R. Godfrey a,*, Paul J. Smith d,
Michael J. Chappell a

<a id='57b24e6f-4b18-413f-b07e-a9e7dffc43f4'></a>

a School of Engineering, University of Warwick, Coventry CV4 7AL, UK
b Department of Medical Biochemistry, University of Wales College of Medicine, Cardiff CF14 4XN, UK
c Cancer Research Wales Laboratories, Velindre NHS Trust, Cardiff CF14 2TL, UK
d Department of Pathology, University of Wales College of Medicine, Cardiff CF14 4XN, UK
e School of MIS-Mathematics, Coventry University, Coventry CV1 5FB, UK
Received 21 October 2002; received in revised form 18 June 2003; accepted 22 January 2004

<a id='fce6ead9-5deb-4958-8f99-864a167c34d2'></a>

## Abstract

In this paper a compartmental modelling approach is applied to provide a mathematical description of the activity of the anti-cancer agent topotecan, and delivery to its nuclear DNA target following administration. The activity of topotecan in defined buffers is first modelled using a linear two compartment model that then forms the basis of a cell based model for drug activity in live cell experiments. An identifiability analysis is performed before parameter estimation to ensure that the model output (i.e., continuous, perfect and noise-free data) uniquely determines the parameters. Parameter estimation is performed using experimental data which offers concentrations of active and inactive forms of topotecan from high performance liquid chromatography methods.
© 2004 Elsevier Inc. All rights reserved.

<a id='79d52ee3-9ad9-4e59-92d4-f6ceb6b6cf52'></a>

Keywords: Compartmental models; Identifiability; Topotecan; Drug kinetics

<a id='ae963e32-6a03-49d9-8fba-a9934ea61eca'></a>

## 1. Introduction
The compartmental modelling [1,2] of the kinetics of a drug can be used to provide a mathematical description of the stability of the drug and delivery to a specified target. This description

<a id='191b4642-4265-401e-94b3-188a93bb2e15'></a>

* Corresponding author. Tel.: +44-2476 523 144; fax: +44-2476 418 922.
E-mail address: k.godfrey@warwick.ac.uk (K.R. Godfrey).

<a id='578f49d4-140a-497e-a183-d2e0b01b904f'></a>

0025-5564/$ - see front matter  2004 Elsevier Inc. All rights reserved.
doi:10.1016/j.mbs.2004.01.007

<!-- PAGE BREAK -->

<a id='e8dba6ed-c63c-4a42-8447-c2a5b205b9f1'></a>

186

<a id='c33d323f-6efb-4d15-94e0-c8acaaaa86fe'></a>

_N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217_

<a id='86d30d66-1f6d-483a-a220-4cec38f5f5a0'></a>

can be analysed to explore the interplay between drug stability and delivery to target. For this purpose we propose a compartmental model for the anti-cancer agent topotecan (TPT), which is based on underlying biological assumptions, and the model parameters estimated using high performance liquid chromatography (HPLC) data.

<a id='420b5cc4-226b-47d2-ab1a-8dd8a764cef8'></a>

Camptothecin (CPT), an extract from the Chinese tree, Camptotheca acuminata [3,4], is an anti-cancer agent that acts as a specific and reversible poison of topoisomerase I [5]. Topotecan, a water-soluble derivative [3,4,6], has been approved for clinical use against ovarian and small cell lung carcinomas with continuous infusion schedules providing reduced toxicity. Both in vitro [7] and clinical studies [8] show elements of schedule dependency for TPT action. The molecular target for TPT is DNA topoisomerase I [9], a cellular enzyme that acts to resolve topological distortions in DNA through a process involving the cleavage and re-ligation of one strand of the double-stranded DNA (dsDNA) [3,4,9,10]. Topotecan acts to trap topoisomerase I in a covalently bound intermediate and reversible complex with DNA. It has been proposed that genotoxic stress occurs when the DNA replication machinery collides with this complex, resulting in dsDNA breaks due to strand discontinuity within the stalled replicon [5,6,10]. Maintenance of the complex requires the presence of the active form of TPT and also this molecule is capable of DNA binding [11,12] thus describing nuclear location of active agent as a vital parameter in the cytotoxic action of TPT [3].

<a id='6fc553ad-8170-485e-9fe2-204e6b1b900f'></a>

In aqueous media, the active form of TPT is not stable at physiological pH and undergoes reversible hydrolysis from a closed ring parent lactone form (TPT-L) to an open-ringed hydroxy acid form (TPT-H). This conversion is pH-dependent, with the lactone form predominating at low pH (<4), and the hydroxy acid form at high pH (>10). Additionally, stabilisation of the active form has been suggested when bound to DNA [11]. It is therefore critical to be able to characterise the time dependent conversion of the active form, not only in solution or medium, but also in live cells.

<a id='48d8ec97-8137-4416-8de9-757071ef2122'></a>

HPLC provides a means by which the levels of the lactone form can be quantified from medium and cellular extracts. Applying HPLC to TPT in buffers at different pH enables measured values for the concentrations of TPT-L and TPT-H to be obtained. Data collected from in vitro cell experiments using HPLC further provides information about the respective concentrations of TPT-L and TPT-H in the medium and cellular pools. These data can then be used to estimate parameters in corresponding compartmental models.

<a id='c40f6e9d-df96-44a7-9b32-f949be968b67'></a>

The reversible hydrolysis of TPT-L can be modelled by a simple linear two compartment model. In order to characterise the pH dependency of the conversion between active and inactive forms the model parameters are estimated from HPLC data collected from buffers at different pH. In the live cell experiments differential hydrolysis of TPT-L occurs in the medium compared to the cellular pools. This occurs by virtue of the difference between extracellular and intracellular pH levels as well as due to less well-defined properties of the drug in the cell. Combining compartmental models for each pool, by including cellular influx and efflux terms, a partial description of the stability of TPT-L in solutions containing live cells can be obtained. A final compartment is added to represent the cellular target (active drug bound to nuclear DNA) and appropriate association (non-linear) and dissociation pathways included to complete the mathematical description of the activity of TPT and its delivery to target.

<a id='533ab417-f491-429e-a24a-f999fed92f70'></a>

In applying this knowledge-based approach to compartmental modelling, biological informa-
tion and minimal assumptions are used to determine the structure of the compartmental model.

<!-- PAGE BREAK -->

<a id='0a70fe81-0615-4db1-aabe-0be5c552ad13'></a>

_N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217_

<a id='5005b3ab-9d4d-4237-9c08-8f2c6e5801f6'></a>

187

<a id='9cfe0d41-1082-454c-8cf4-40753a2d158e'></a>

This enables a greater understanding of the underlying drug kinetics and re-evaluation of the biological assumptions. After estimating the model parameters using experimental (HPLC) data it is then possible to explore, via simulation, the delivery of active TPT to DNA. HPLC provides drug activity data from the medium and intracellular milieu, and in both cases the measurements represent an average of each pool, local gradients and heterogeneity are not taken into account. Additionally, it is not possible to differentiate the nuclear and cytosolic concentrations of TPT-L. Therefore the model provides a means for inferring, quantitatively, the delivery of TPT-L to target. Hence the mathematical model leads to a comprehensive characterisation of the kinetics of the TPT forms in the medium, cytoplasm and provides a significant tool for predicting the amount of active drug bound to target sites in the nucleus. In this paper different model conditions are implemented to allow consideration of the consequences of various drug schedule designs as well as the dose dependent effect on delivery of drug to target.

<a id='9f372b5d-551a-4d40-84a0-2de66f8fdb4f'></a>

A critical model component that affects drug delivery to the nuclear target sites is the cellular efflux rate constant. In essence this parameter represents the ability of the cell to clear the drug from the cellular pool to the medium. Several resistance mechanisms have been described in cancer cells able to reduce cytotoxic drug accumulation by up-regulating plasma-membrane-located ATP-dependent efflux pumps [13]. TPT P-glycoprotein (P-gp)-mediated resistance has been reported in hamster ovarian cells [14] while further evidence suggests the existence of unidentified transporters in TPT-resistant cells [7]. BCRP (BCRP1/MXR/ABCP) is a plasma-membrane-located ATP-binding cassette 'half-transporter' drug efflux pump thought to have a substrate spectrum different from those of P-gp and MRP1 [15]. BCRP renders tumour cells resistant to many anticancer agents and is associated with cross-resistance to CPT derivatives including TPT [16].

<a id='078005d7-a098-41dc-9398-525ac82aa35b'></a>

An important prerequisite to experiment design and parameter estimation is the question of structural identifiability [17]. Each proposed experiment to collect data for the purposes of parameter estimation determines model outputs, which are the functions of the model variables that are to be directly measured. For example, using HPLC it is possible to directly measure the concentration of TPT-L in the medium, which is one of the variables in the mathematical model and so this variable constitutes one of the model outputs. The structural identifiability problem, for a given experiment, is then whether the corresponding model outputs uniquely determine all of the unknown parameters. This is a question relating to the structure of the mathematical model and is independent of the actual experimental data collected. Should the parameters not be uniquely determined then any subsequent parameter estimation should be viewed with less confidence [2].

<a id='b247e8e8-f748-4a87-a2b2-875fe8b21691'></a>

The general method that is applied to perform the structural identifiability analyses for the models derived in this paper is outlined in Section 2. In Section 3 a simple two compartment model is proposed to describe the reversible hydrolysis of TPT in buffers. After an identifiability analysis is performed using the approach of Section 2, the model parameters are estimated from HPLC data for buffers at different pH. The full cell based model is described in Section 4 with an identifiability analysis of this model (using the method outlined in Section 2) summarised in Section 5. The details of the identifiability analysis are presented in Appendix A. Section 6 deals with the estimation of the parameters of the full cell model from HPLC data. The results of simulations to assess the effects of changes in the dose, or in the method of administration of the dose, on the binding of TPT-L to nuclear DNA are presented in Section 7. Also presented in this

<!-- PAGE BREAK -->

<a id='4630bc85-0690-44b2-b54b-8be29eb24a4b'></a>

188

<a id='b127a22e-ed8a-4263-8092-f1dfda0e86a9'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='33a9854e-8908-4ccf-b9ee-2a984b416c15'></a>

section are the results of simulations assessing the effects of changes in the cellular efflux of TPT on the binding of TPT-L to DNA, reflecting the effects of variation in the expression of a drug resistance pathway.

<a id='659f2a63-a79d-4b75-baf4-896e47dc90a4'></a>

## 2. Structural identifiability

To formally define structural identifiability, it is first necessary to introduce a general class of parametric models for which the compartmental models derived in this paper are particular examples. Consider a postulated parametric model given by

x(t,p) = f(x(t,p),p), (1)
x(0,p) = x0(p), (2)
y(t,p) = C(p)x(t,p) (3)

<a id='9fe324f2-b9f7-4183-94e7-041346503546'></a>

where **p** = (p₁, ..., p_q)^T is a vector comprising the unknown model parameters and lies in some open set Ω of feasible values; **x**(*t*,**p**) = (*x*₁(*t*,**p**), ..., *x*ₙ(*t*,**p**))^T is the state vector and represents the information required by the system to evolve in time; **y**(*t*,**p**) = (*y*₁(*t*,**p**), ..., *y*ᵣ(*t*,**p**))^T comprises the model outputs and corresponds to the functions of the state that are measured in the experiments. Solutions to Eq. (1) are assumed to lie in *M*(**p**), a connected open subset of Rⁿ (i.e., all *n* components are real numbers), that is **x**(*t*,**p**) ∈ *M*(**p**) for all *t* ≥ 0. It is assumed that *f*(·,**p**) is analytic on *M*(**p**), and **C**(**p**) is an *r* × *n* real matrix.

<a id='eaf47344-a01a-4c1a-8af7-9b91ec31dcc8'></a>

The experimental input consists of a single impulse (injection of drug into the system) and so is included in the initial conditions x_0(p). There are assumed to be no other external inputs to the model and so no further input terms are included in Eq. (1).

<a id='e657a3a3-b93a-48b8-a4a8-e52c0018aaf3'></a>

Given a parameter vector p, then p̄ ∈ Ω is said to indistinguishable from p if they give rise to identical model outputs, i.e.,

<a id='cd254ffc-8c4d-4fbb-9f3b-09dc12e53880'></a>

y(t,p) = y(t,p) for all t≥ 0.

<a id='37c8f3fb-bcb0-4b57-94e1-a3bf59048dff'></a>

A model of the form of Eqs. (1)-(3) is *globally identifiable* at **p** ∈ Ω if the only parameter vector indistinguishable from **p**, is **p** itself. The model is said to be *structurally globally identifiable* if it is *globally identifiable* at **p**, for generic **p**.

<a id='7a2323d6-e1d9-400e-9b8e-73b37c99e5ce'></a>

For linear models there are many well-established techniques for analysing structural identi-fiability (see the tutorial paper [18] for details). Among the most commonly used are those based on the uniqueness properties of the Laplace transform of the output (or outputs) [1,2,19] or on the existence of a similarity transformation [2,19]. However, for non-linear models there are relatively few techniques available, with the most common being the Taylor series approach [20] and the similarity transformation approach [21,22]. The former can be applied to models of systems where the drug is administered via a bolus injection and performed by expanding the output as a Taylor series around t = 0 [20]. The coefficients in the resulting expansion are unique for a given input so the approach reduces to equating coefficients for y(t,p) and y(t,p) where p is indistinguishable from p. However, the analysis using this method can sometimes become intractable (see, for example, the identifiability analysis for Model B in Section 9.4.3 of [1]). In order to apply the

<!-- PAGE BREAK -->

<a id='666bb7db-cb93-40bf-a039-66ebe740cd6c'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='6cb78f54-6c8d-4f16-aa00-5662d43667c1'></a>

189

<a id='e025fc22-5534-4423-bc86-ebede0725ef8'></a>

similarity transformation approach, it is first necessary to check observability and controllability
criteria [2], the latter of which is not in general satisfied (for non-linear systems) when adminis-
tration is via a bolus injection. Since administration of TPT in the HPLC experiments is via a
bolus injection, and to avoid possible computational problems, a new method [23,24] is applied to
perform the structural identifiability analysis. This method uses similar ideas to the similarity
transformation approach in that a mapping is constructed that connects the states corresponding
to indistinguishable parameter vectors, i.e., x(t,p) and x(t,p̄). However, to apply it does not
require a controllability criterion to be satisfied, only an observability one.

<a id='50a8c773-ac06-4792-af81-f888fc78fc4e'></a>

A simplified test for the observability criterion is as follows (for more details of the general form of the observability criterion see the papers by Evans et al. [23,24], and for observability of general input–output systems see the paper by Hermann and Krener [25]): Define r smooth real-valued functions (where r is the number of model outputs) by

<a id='6c07d232-5ac0-4108-9846-9dea86f5801f'></a>

<::$\mu_i(\mathbf{x}, \mathbf{p}) = c_i(\mathbf{p})\mathbf{x},$
: figure::>

<a id='0d8f8988-ac18-4e5a-a78f-bb39aa885593'></a>

where $c_i(p)$ is the $i^{th}$ row of the output matrix $C(p)$. Using these, an infinite list of functions can be defined by setting

$\phi_i(\mathbf{x}, \mathbf{p}) = \left( \frac{\partial\mu_i}{\partial x_1}(\mathbf{x}, \mathbf{p}), \dots, \frac{\partial\mu_i}{\partial x_n}(\mathbf{x}, \mathbf{p}) \right) f(\mathbf{x}, \mathbf{p})$

<a id='b166976b-8cd6-47c2-a712-5246525b0459'></a>

for $i = 1,\ldots,r$, and then recursively setting

$\phi_i(\mathbf{x},\mathbf{p}) = \left( \frac{\partial\phi_{i-r}(\mathbf{x},\mathbf{p})}{\partial x_1}, \ldots, \frac{\partial\phi_{i-r}(\mathbf{x},\mathbf{p})}{\partial x_n} \right) f(\mathbf{x},\mathbf{p})$

<a id='3d7d6c1d-945d-4a61-8dc5-94e995e82851'></a>

for i > r. From the infinite list φ₁, φ₂, ..., we can choose n - r functions φm₁, ..., φm_{n-r} and form a matrix **J** by

<a id='c89aa6f0-8118-4f10-844b-d1650501959f'></a>

<::J = 
\begin{pmatrix}
\frac{\partial \mu_1}{\partial x_1} (\mathbf{x}_0(\mathbf{p}),\mathbf{p}) & \cdots & \frac{\partial \mu_1}{\partial x_n} (\mathbf{x}_0(\mathbf{p}),\mathbf{p}) \\
\vdots & & \vdots \\
\frac{\partial \mu_r}{\partial x_1} (\mathbf{x}_0(\mathbf{p}),\mathbf{p}) & \cdots & \frac{\partial \mu_r}{\partial x_n} (\mathbf{x}_0(\mathbf{p}),\mathbf{p}) \\
\frac{\partial \phi_{m_1}}{\partial x_1} (\mathbf{x}_0(\mathbf{p}),\mathbf{p}) & \cdots & \frac{\partial \phi_{m_1}}{\partial x_n} (\mathbf{x}_0(\mathbf{p}),\mathbf{p}) \\
\vdots & & \vdots \\
\frac{\partial \phi_{m_{n-r}}}{\partial x_1} (\mathbf{x}_0(\mathbf{p}),\mathbf{p}) & \cdots & \frac{\partial \phi_{m_{n-r}}}{\partial x_n} (\mathbf{x}_0(\mathbf{p}),\mathbf{p})
\end{pmatrix}
: math::>

<a id='b88c10c1-81c1-497b-a8fb-4c7869ba28c6'></a>

The model satisfies the observability criterion if there exist $n - r$ such functions $\phi_{m_1}, \ldots, \phi_{m_{n-r}}$ for which det $\mathbf{J} \neq 0$. In this case $n - r$ functions are defined by $\mu_{r+i}(\mathbf{x}, \mathbf{p}) = \phi_{m_i}(\mathbf{x}, \mathbf{p})$ ($i = 1, \ldots, n - r$).

<a id='12350efd-0617-482b-b671-b16c0996dabf'></a>

To minimise the computation involved in checking the observability condition, candidates should be considered in order of increasing complexity. It is also desirable that only the candidate functions be calculated, with further functions calculated only if necessary.

<a id='8b0e6575-393a-4430-b8e5-31ffc8245500'></a>

The following, which summarises results from Evans et al. [23], is used to perform the structural identifiability analyses for the mathematical models proposed in this paper. To test the identifi- ability of a model at a parameter vector *p*:

<!-- PAGE BREAK -->

<a id='8c1ab1d3-bee5-4811-9d1c-7f151c8be5ae'></a>

190

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='0a568707-2003-43f7-a197-fb18d6bcde48'></a>

Step 1 Rewrite the model and outputs in the general form of Eqs. (1)-(3).
Step 2 Check whether the observability criterion is satisfied:
* If satisfied then _n_ (the number of states in the model) smooth functions
	_μ_1,···, _μ_r, _μ_r+1,..., _μ_n are obtained;
* Otherwise it might be possible to redesign the experiments, and therefore the output
	structure of the model, such that the resulting model does satisfy the observability
	criterion;
* If it is not possible to redesign the experiments such that the observability criterion is
	satisfied, then a different approach must be applied.

<a id='9a4c9ea4-7277-4a2c-9c8f-c750fff94fc6'></a>

Step 3 Let $\bar{p}$ be an arbitrary parameter vector. Construct a smooth function $\lambda$, defined on a suitable neighbourhood of $x_0(\bar{p})$, by solving the following
$\mu_i(\lambda(x), \bar{p}) = \mu_i(x, \bar{p}), \quad i = 1, \ldots, n$
(4)

<a id='b00368d9-b836-4fb6-87ef-d4a662c85939'></a>

and obtaining expressions for the components of λ(x) in terms of the components of **p** and
**p̄**. Note that, in general this means that λ(x) can depend on **p** and **p̄**.
Step 4 Determine the set 𝒮(**p**) of all **p̄** ∈ Ω such that for some τ > 0

λ(x₀(**p̄**)) = x₀(**p**), (5)

<a id='3daba946-54e2-4088-9913-fbfe9682bf87'></a>

$\large f(\lambda(x(t,\bar{p})), \bar{p}) = \frac{\partial \lambda}{\partial x}(x(t,\bar{p}))f(x(t,\bar{p}), \bar{p}) \quad (6)$

<a id='b747b527-0a64-47cd-a9f3-60602e3b27d9'></a>

for all t ∈ [0, τ).

<a id='c6fc8c6b-5988-4f0f-9905-dbd7a0fa13bb'></a>

The set *S*(*p*) consists of precisely those parameter vectors *p̄* that are indistinguishable from *p*.
The model is globally identifiable at *p* if *S*(*p*) = {*p*}. If the analysis performed for an arbitrary, but fixed, *p* ∈ *Ω* remains valid for generic parameter vectors then the results are structural. Thus if *S*(*p*) = {*p*} for generic *p* then the model is structurally globally identifiable.

<a id='d1022ca1-49e8-4530-9922-bd60d7b7b308'></a>

### 3. TPT persistence in buffers
The inactivation of TPT-L and subsequent activation of TPT-H is an important aspect of the kinetics of TPT and forms the basic building block for the full cell model presented in this paper. This reversible hydrolysis of TPT-L can be modelled using a simple two compartment model.

<a id='16e503fe-b25e-4454-baca-723fb4518b11'></a>

3.1. Compartmental model
Let L(t) denote the concentration of the active form of the drug (TPT-L) in solution at time t after an initial dose of TPT-L; and H(t) the corresponding concentration of the inactive form of the drug (TPT-H). It is assumed that the inactivation (ring opening) of TPT-L occurs with a first order rate constant ko to give TPT-H; TPT-H becomes activated (ring closing) to give TPT-L with a first order rate constant ke. The following coupled linear differential equations then describe the dynamics of the concentrations of TPT-L and TPT-H:

<a id='4955894c-233b-4e33-b589-ff5c46a0f4fb'></a>

d/dt L(t) = -k_o L(t) + k_c H(t), (7)

<!-- PAGE BREAK -->

<a id='2365fa0e-323b-4035-aaf6-95a72e916be6'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217 191

<a id='b7e1e893-ea35-48d6-ac24-b0f4550b01c8'></a>

d/dt H(t) = k_o L(t) - k_c H(t). (8)

<a id='1398d4a4-ed9f-4008-a942-e2e40ae4e32f'></a>

In all of the experiments considered in this paper, TPT is administered as a single bolus input of active (lactone form) drug to give a concentration of D. Since the drug concentrations are zero before administration, which is deemed to occur at t = 0, the associated initial conditions for the differential equations, Eqs. (7) and (8), are given by

L(0) = D and H(0) = 0.
(9)

<a id='f801ebd5-11d2-4a2c-903c-2088ad61259a'></a>

The values for the constants (model parameters) ko and kc are estimated from high performance liquid chromatography (HPLC) data collected at Cancer Research Wales Laboratories (Velindre NHS Trust, Cardiff) for different values of pH consistent with physiological conditions (pH 6.8–8.0). Since the experiment to collect the data allows the separate sampling of the concentrations of TPT-L and TPT-H, there are two model outputs, namely L(t) and H(t). Before estimating the parameters from the data, an identifiability analysis for the model is performed.

<a id='5cdfe375-e911-4fd9-951d-a6fb1ef9ecdd'></a>

## 3.2. Identifiability analysis
The general method presented in Section 2 will be applied to perform the structural identifiability analysis for the two compartment hydrolysis model. Although the analysis is relatively simple for the hydrolysis model, it illustrates the general method that is used in the more complicated analysis for the full cell model in Section 5.

<a id='bed55398-4091-4d52-a168-3120b2d79c64'></a>

Step 1

The dose D is assumed to be known and is therefore not included in the parameter vector **p**,
which is given by **p** = (_k_0, _k_c)<sup>T</sup>. Since the parameters must be real and positive the set of feasible
vectors is taken to be Ω = {(_p_1, _p_2)<sup>T</sup> : _p_1 > 0 and real}.

The state **x**(_t_,**p**) (_n_ = 2) and output **y**(_t_,**p**) (_r_ = 2) for the model are the same and given by

<a id='3e018d46-ed91-4454-bc02-f7183c171419'></a>

y(t,p) = x(t,p) = (
L(t,p)
H(t,p)
).

<a id='2ae94898-37f0-4c51-8967-dc0654651203'></a>

The state takes values in the set M(p) which is taken to be R² (i.e., the set of all 2-vectors, x = (L, H)ᵀ, such that both components, L and H, are real). The initial state x(0,p) is given by x₀(p) = (D, 0)ᵀ. In this example the initial state is actually independent of the vector of unknown parameters p.

<a id='29863a23-0350-4550-8b36-05c751e7acc3'></a>

To complete the model description, in terms of the general formulation of Eqs. (1)-(3), we define the following

<a id='695500ef-6fe6-4650-95b7-9d53caad7f83'></a>

f(x,p) = (
-k_oL + k_cH
k_oL - k_cH
),

<a id='1a385b73-4652-47e3-8662-a55a7ffdb441'></a>

where **x** = (*L*, *H*)^T is an arbitrary vector in *M*(*p*), and the output matrix

<a id='02b8c3bb-e607-4fe0-b62f-f3236e4735ed'></a>

C(p) = ( 1 0 )
       ( 0 1 )

<a id='f7aa34f2-e0f3-4d5d-b95b-517e9fab641a'></a>

is independent of the parameter vector _p_.

<!-- PAGE BREAK -->

<a id='bc5abd2e-2ae2-4096-aba9-2437dcece3ba'></a>

192 N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='e0ea83b6-be7f-4278-b9ba-c13219746af4'></a>

Step 2
Let μ₁(x,p) = L and μ₂(x,p) = H (again, where x = (L,H)ᵀ). Note that both μ₁ and μ₂ are independent of the parameter vector p. For this example r=n = 2 and so we construct J immediately:

J = (∂μ₁/∂L (x₀(p),p) ∂μ₁/∂H (x₀(p),p) 
∂μ₂/∂L (x₀(p),p) ∂μ₂/∂H (x₀(p),p)) = (1 0 
0 1)

<a id='2bfd4e70-7dec-49ed-a4d7-892337959308'></a>

which has non-zero determinant. Therefore the observability criterion is satisfied.

Step 3
Let $\bar{p} = (k_o, \bar{k}_c)^T$. Then solving Eq. (4) for $i = 1$ it is seen that $\mu_1(\lambda(\mathbf{x}), \bar{p}) = \lambda_1(\mathbf{x})$, the first component of $\lambda(\mathbf{x})$, by definition of $\mu_1$. Therefore
$\lambda_1(\mathbf{x}) = \mu_1(\lambda(\mathbf{x}), \bar{p}) = \mu_1(\mathbf{x}, \bar{p}) = L$

<a id='046aa481-6658-4d4d-855e-2a9fdeacc702'></a>

Similarly, solving Eq. (4) for _i_ = 2 gives

<a id='e7ebd4a6-4906-4669-a870-c72da6861b49'></a>

λ2(x) = μ₂(λ(x),p) = μ2(x,p) = H

<a id='6e9ef7c8-d45f-45a0-b8d9-d903f89314ea'></a>

and so λ(x) = x, i.e., λ is the identity.
Step 4

<a id='92814eca-6731-4942-8f92-eb5a5af69c00'></a>

Now it only remains to determine the set $\mathcal{S}(\mathbf{p})$ of all solutions $\bar{\mathbf{p}}$ to Eqs. (5) and (6). Since $\lambda$ is the identity Eq. (5) is automatically satisfied and Eq. (6) is given by

<a id='ce2d345b-f229-403f-ab3f-f1618d3a04d7'></a>

-k_o L(t, \bar{p}) + k_c H(t, \bar{p}) = -\bar{k}_o L(t, \bar{p}) + \bar{k}_c H(t, \bar{p}), (10)

<a id='f86bf7ff-d439-4615-ba11-1b27525ca4f5'></a>

k_o L(t,\boldsymbol{p}) - k_c H(t,\boldsymbol{p}) = \bar{k}_o L(t,\boldsymbol{p}) - \bar{k}_c H(t,\boldsymbol{p}).

(11)

<a id='f9a17fb7-4d2c-410d-a73e-0470107f4b70'></a>

By setting $t = 0$ in either of these equations and noting that $D \neq 0$ shows that $\bar{k}_o = k_o$. Therefore, from Eq. (10) it is seen that

<a id='b13ecaf4-2895-4f02-8dc6-9d7a4f84e440'></a>

$$(k_c - \bar{k}_c)H(t,\bar{p}) = 0$$

<a id='748f47cf-4194-4934-ab07-371373694cc6'></a>

on an interval of the form [0, τ), for some τ. Since _H_(_t_,_p̅_) is not identically zero (because _k_o > 0) this means that the only solution for _k_c is _k_c = _k_c. Therefore _S_(_p_) = {_p_} and because the analysis remains valid for all parameter vectors _p_, the model is structurally globally identifiable.

<a id='5dd8af8e-d164-4389-8aec-ce704194774e'></a>

### 3.3. Parameter estimates
The parameter fitting was performed using the computer package Facsimile (MCPA Software, UK) for HPLC data (for details concerning the HPLC methods used see Section 6) consisting of values for the concentrations of TPT-L and TPT-H at $t$ = 1, 2, 5, 10, 15, 30, 45, 60, and 120 min after the drug was added. Phosphate buffered saline (PBS) solutions made to the required pH (6.8, 7.0, 7.2, 7.4, 7.6, 7.8, and 8.0) were used for the experiments, which were performed in duplicate.
The parameter values obtained are presented in Table 1.

<a id='93c92fc0-6f49-4cae-9bd4-0c8c3829d4ed'></a>

Facsimile works in terms of internal parameters that are natural logarithms of the model parameters, and so the SDLN value in Table 1 corresponds to the estimated standard deviation of

<!-- PAGE BREAK -->

<a id='75f6f38c-11ef-441e-a050-6f3bcbea8078'></a>

*N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217*

<a id='b0c05dd1-ad79-48a3-917c-aef3b22ce67e'></a>

193

<a id='8588a67a-1f30-405a-b017-1afd42755ce2'></a>

Table 1
The parameter values for the model Eqs. (7) and (8) obtained from HPLC data
<table id="8-1">
<tr><td id="8-2">pH</td><td id="8-3" colspan="4">k_o</td></tr>
<tr><td id="8-4"></td><td id="8-5">Value</td><td id="8-6">SDLN</td><td id="8-7">5%</td><td id="8-8">95%</td></tr>
<tr><td id="8-9">6.8</td><td id="8-a">5.4960×10-3 min-1</td><td id="8-b">0.0640</td><td id="8-c">4.9466×10-3 min-1</td><td id="8-d">6.1064×10-3 min-1</td></tr>
<tr><td id="8-e">7.0</td><td id="8-f">7.7480×10-3 min-1</td><td id="8-g">0.0467</td><td id="8-h">7.1754×10-3 min1</td><td id="8-i">8.3663×10-3 min-1</td></tr>
<tr><td id="8-j">7.2</td><td id="8-k">9.3594×10-3 min</td><td id="8-l">0.0432</td><td id="8-m">8.7176×10-3 min¹</td><td id="8-n">1.0048×10-2 min-1</td></tr>
<tr><td id="8-o">7.4</td><td id="8-p">1.1669×10-2 min-1</td><td id="8-q">0.0408</td><td id="8-r">1.0912×10-2 min-1</td><td id="8-s">1.2478×10-2 min-1</td></tr>
<tr><td id="8-t">7.6</td><td id="8-u">1.3973×10-2 min-¹</td><td id="8-v">0.0383</td><td id="8-w">1.3119×10-2 min-1</td><td id="8-x">1.4882×10-2 min-1</td></tr>
<tr><td id="8-y">7.8</td><td id="8-z">1.5332×10-2 min-1</td><td id="8-A">0.0394</td><td id="8-B">1.4370×10-2 min-1</td><td id="8-C">1.6359×10-2 min</td></tr>
<tr><td id="8-D">8.0</td><td id="8-E">1.7234×10-2 min</td><td id="8-F">0.0423</td><td id="8-G">1.6075×10-2 min-1</td><td id="8-H">1.8477×10-2 min</td></tr>
<tr><td id="8-I"></td><td id="8-J" colspan="4">k_c</td></tr>
<tr><td id="8-K">6.8</td><td id="8-L">1.7710×10-2 min-1</td><td id="8-M">0.1181</td><td id="8-N">1.4582×10-2 min-1</td><td id="8-O">2.1509×10-2 min-1</td></tr>
<tr><td id="8-P">7.0</td><td id="8-Q">1.8947×10-2 min</td><td id="8-R">0.0837</td><td id="8-S">1.6510×10-2 min-1</td><td id="8-T">2.1744×10-2 min</td></tr>
<tr><td id="8-U">7.2</td><td id="8-V">1.7732×10-2 min-1</td><td id="8-W">0.0802</td><td id="8-X">1.5546×10-2 min-1</td><td id="8-Y">2.0237×10-2 min-1</td></tr>
<tr><td id="8-Z">7.4</td><td id="8-10">1.8537×10-2 min-1</td><td id="8-11">0.0743</td><td id="8-12">1.6404×10-2 min-1</td><td id="8-13">2.0947×10-2 min-1</td></tr>
<tr><td id="8-14">7.6</td><td id="8-15">1.2878×10-2 min-1</td><td id="8-16">0.0850</td><td id="8-17">1.1197×10-2 min</td><td id="8-18">1.4811×10-2 min1</td></tr>
<tr><td id="8-19">7.8</td><td id="8-1a">1.2852×10⁻² min⁻¹</td><td id="8-1b">0.0878</td><td id="8-1c">1.1123×10⁻² min⁻¹</td><td id="8-1d">1.4850×10⁻² min⁻¹</td></tr>
<tr><td id="8-1e">8.0</td><td id="8-1f">8.2328×10⁻³ min⁻¹</td><td id="8-1g">0.1257</td><td id="8-1h">6.6954×10⁻³ min⁻¹</td><td id="8-1i">1.0123×10⁻² min⁻¹</td></tr>
</table>

<a id='bdec9302-e700-4d60-8a25-63b2b2fa07ab'></a>

the logarithm of each parameter. The SDLN therefore provides an approximation of the coeffi-cient of variation of the parameter estimate. Under an assumption that the logarithms of the parameters are normally distributed, the SDLN is used to obtain 5% and 95% confidence limits, which are values such that the probability of the true parameter being smaller is 5% and 95% respectively [26]. In Fig. 1 the output of the model, given by Eqs. (7)-(9), is plotted together with the data.

<a id='39db9569-b837-49d9-849a-4dea744bfc35'></a>

From these plots, it is seen that there is good correspondence between the (simulated) output of the model and the collected data.

<a id='e3875236-693e-49d5-b89f-03650cbe6437'></a>

The correlation coefficients for the two parameters in each of the experiments are, respectively, 0.913, 0.909, 0.902, 0.897, 0.868, 0.863 and 0.824, showing high linear covariation between the estimates for ln(k_o) and ln(k_c). This means that it is really only a linear combination of ln(k_o) and ln(k_c) that is well estimated [27].

<a id='f450246e-640a-4477-bdb7-ddb380eb37af'></a>

It is seen from the graphs in Fig. 1 that as pH increases, the initial slope of the TPT-L time curve becomes steeper and the long term value decreases. This indicates that for higher pH the initial dose of TPT-L more rapidly undergoes hydrolysis to TPT-H and that the equilibrium concentration of TPT-L decreases. Conversely, TPT-H is formed more rapidly at higher pH, with a larger concentration at equilibrium. This indicates, as expected, that TPT-L is more stable at lower pH. For pH greater than 7.6 TPT-H predominates at equilibrium, while for values less than 7.6 TPT-L does. As pH increases above 7.6, the first time at which more hydrolysed form than lactone is present decreases rapidly. In Fig. 2, the fitted values for each parameter are plotted against pH.

<a id='6f7f8363-e9f7-4d54-a8fe-f303814aa965'></a>

The values for parameter k_o appear to vary linearly with pH, while it is not possible to readily determine a relationship between the values for k_c and pH.

<!-- PAGE BREAK -->

<a id='5b308f17-3221-4185-b127-8d7ff5933feb'></a>

194

<a id='cfa31c63-8c0a-48d6-9cb2-df11eef748cd'></a>

194 N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217 <::Seven line graphs depicting concentration (µM) versus time (mins) for TPT-L and TPT-H at different pH environments. Each graph's y-axis is labeled "Concentration (µM)" (0 to 10) and x-axis is labeled "Time (mins)" (0 to 120). The model output (lines) for TPT-L is represented by a solid line, and for TPT-H by a dashed line. HPLC data points are shown as circles for TPT-L and squares for TPT-H. Graph 1: pH 6.8. TPT-L decreases from approximately 9.5 µM to 8 µM. TPT-H increases from 0 µM to approximately 2.5 µM. Graph 2: pH 7.0. TPT-L decreases from approximately 9.5 µM to 7 µM. TPT-H increases from 0 µM to approximately 3 µM. Graph 3: pH 7.2. TPT-L decreases from approximately 9.5 µM to 6.5 µM. TPT-H increases from 0 µM to approximately 3.5 µM. Graph 4: pH 7.4. TPT-L decreases from approximately 9.5 µM to 6 µM. TPT-H increases from 0 µM to approximately 4 µM. Graph 5: pH 7.6. TPT-L decreases from approximately 9.5 µM to 5 µM. TPT-H increases from 0 µM to approximately 5 µM. Graph 6: pH 7.8. TPT-L decreases from approximately 9.5 µM to 4.5 µM. TPT-H increases from 0 µM to approximately 5.5 µM. Graph 7: pH 8.0. TPT-L decreases from approximately 9.5 µM to 4 µM. TPT-H increases from 0 µM to approximately 6 µM, then slightly decreases to 5.5 µM. Fig. 1. The plots represent the model output (lines) for TPT-L (solid) and TPT-H (dashed) fitted to the HPLC data (circles and squares, respectively) collected for the different pH environments.::>

<a id='4af901c1-224e-4087-87f2-8b2970af68ca'></a>

Fig. 1. The plots represent the model output (lines) for TPT-L (solid) and TPT-H (dashed) fitted to the HPLC data (circles and squares, respectively), collected for the different pH environments.

<!-- PAGE BREAK -->

<a id='446f6240-4e0a-4978-b676-f40cc857548d'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='913eea45-e6f5-40df-ba14-a58a980e4ebc'></a>

195

<a id='69c5a80e-8228-4bce-84bb-ec58546f849f'></a>

<::chart: The figure displays two plots side-by-side, showing the variation of fitted parameter values with pH. Both plots use a pH range of 6.8 to 8.0 on their x-axes. The vertical bars represent the 90% confidence limits for each estimated parameter value.  The y-axis for both plots is scaled by ×10^-3.  The left plot is titled "k_o (min^-1)". Its y-axis ranges from 5.0 to 18.5, with tick marks at 5.0, 7.7, 10.4, 13.1, 15.8, and 18.5. Data points with error bars are shown for pH values:  - pH 6.8: ~5.0  - pH 7.0: ~7.0  - pH 7.2: ~8.8  - pH 7.4: ~11.0  - pH 7.6: ~13.5  - pH 7.8: ~15.0  - pH 8.0: ~16.5.  The right plot is titled "k_c (min^-1)". Its y-axis ranges from 6.70 to 22.00, with tick marks at 6.70, 9.76, 12.82, 15.88, 18.94, and 22.00. Data points with error bars are shown for pH values:  - pH 6.8: ~17.0  - pH 7.0: ~19.0  - pH 7.2: ~17.5  - pH 7.4: ~18.0  - pH 7.6: ~12.5  - pH 7.8: ~12.5  - pH 8.0: ~8.0.  Fig. 2. Variation of the fitted parameter values with pH in the range 6.8–8.0. The vertical bars show the 90% confidence limits for each estimated parameter value.::>

<a id='5ae29ce9-8664-4254-a10b-d4f1136602b7'></a>

**4. Cell based model**
The simple compartmental model for the reversible hydrolysis of lactone form TPT in solution is used to construct a model based on the kinetics of TPT in live cell experiments. This model yields quantitative predictions of the concentrations of TPT-L and TPT-H in the various experimental pools.

<a id='f4698b37-f47b-4150-ab92-6b87dfbf1b3d'></a>

The two basic experimental pools are the medium, in which the cells grow, and a cellular pool comprising all of the individual cells. Therefore, in the model, the individual cells are lumped together and treated as a single homogeneous mixture. Assumptions about the kinetics of TPT on a single cell basis are then used, with the principle of mass balance, to derive the model. As a result of this, there is no differentiation between cells to allow for heterogeneity in intra-cellular pH or drug kinetics. In the model, which is shown schematically in Fig. 3, there are three pools corre-sponding to the extracellular medium (denoted by subscript m), the cytoplasm (denoted by sub-script c), and the nucleus (denoted by subscript n).

<a id='42fb43c7-1348-46c9-a94a-54528a621b24'></a>

In the medium and cytoplasm, TPT undergoes reversible hydrolysis, as considered in the previous section, which can be modelled by a simple two compartment model. It is assumed that all TPT present in the nucleus is bound, and that only TPT-L binds to DNA. The latter assumption is supported by current knowledge from studies on DNA in free solution (see Introduction), while the former is a simplifying assumption that requires further experimental investigation. Therefore, in the model, there is no direct pathway for TPT-H to enter the nucleus. The rate at which TPT-L binds to DNA is assumed to be proportional to the product of the concentrations of available binding sites, B_F, and cytosolic TPT-L, L_c. If B_T is used to denote the total concentration of sites to which TPT-L can bind and L_n denotes the concentration of bound TPT-L then, using the appropriate conservation law [28], this product can be rewritten as (B_T - L_n)L_c. Bound TPT-L dissociates from DNA as cytosolic TPT-L, at a first order rate k_d L_n.

<!-- PAGE BREAK -->

<a id='ea736cca-806e-4d5a-a186-4212dd84d5ac'></a>

196
N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='94a551c7-73ae-46f8-b4ad-45a2090fafc3'></a>

<::schematic diagram::>The diagram illustrates a multi-compartment model. On the left, outside a larger compartment labeled "Cytoplasm", are two circles: `Lm` (TPT-L) at the top and `Hm` (TPT-H) at the bottom. Inside the "Cytoplasm" compartment, there are two circles: `Lc` (TPT-L) at the top and `Hc` (TPT-H) at the bottom. The "Cytoplasm" compartment also encloses a smaller rounded rectangle labeled "Nucleus", which contains one circle: `Ln` (TPT-L). Arrows indicate transitions between compartments with associated rate constants:
- `Lm` and `Lc` are connected by bidirectional arrows with rate constants `ki` (from `Lm` to `Lc`) and `ke` (from `Lc` to `Lm`).
- `Lm` and `Hm` are connected by bidirectional arrows with rate constants `kc,m` (from `Lm` to `Hm`) and `ko,m` (from `Hm` to `Lm`).
- `Lc` and `Hc` are connected by bidirectional arrows with rate constants `kc,c` (from `Lc` to `Hc`) and `ko,c` (from `Hc` to `Lc`).
- `Lc` transitions to `Ln` with rate `kbBF(t)`.
- `Ln` transitions to `Lc` with rate `kd`.
An equation `[BF(t) = BT - Ln(t)]` is positioned near `Lc` and `Ln`.

Fig. 3. Schematic of the mathematical model used to investigate the effect on TPT of injecting a dose (system concentration 10 µM) of the active form of the drug into a culture medium containing human lymphoma cells (SU-DHL-4 cell line) in suspension.<::>

<a id='59f80b18-0135-4bf9-9b43-4e85dd45e9a5'></a>

Only extracellular TPT-L flows into the cell, and this inflow is taken to be a first order process with rate constant kᵢ. Similarly, only TPT-L flows out of the cell, and the (first order) rate constant for this efflux is denoted by kₑ. These assumptions are supported by previous observations and the physical properties of the hydroxy acid form with respect to lipid bilayer traverse [29].

<a id='13091e65-3c3d-4467-95d0-11a59d7c9e51'></a>

The concentrations of TPT-L and TPT-H are denoted by L and H, respectively, so that: the instantaneous concentrations, at time t after the initial dose, of TPT-L in the medium, cytoplasm, and nucleus are Lm(t), Lc(t), and Ln(t), respectively; the corresponding concentrations for TPT-H are denoted by Hm(t) and Hc(t), respectively. The mathematical model thus consists of the following system of five ordinary differential equations:

<a id='08df1d76-f5c5-4c3b-b742-19a614d7fdda'></a>

d/dt Lm(t) = -(k_o,m + k_i)Lm(t) + k_c,m Hm(t) + (k_e/v_1)Lc(t), (12)
d/dt Hm(t) = k_o,m Lm(t) - k_c,m Hm(t), (13)
d/dt Lc(t) = (k_i v_1)Lm(t) - (k_e + k_o,c)Lc(t) + k_c,c Hc(t) - k_b(B_T - Ln(t))Lc(t) + v_2 k_d Ln(t), (14)
d/dt Hc(t) = k_o,c Lc(t) - k_c,c Hc(t), (15)
d/dt Ln(t) = (k_b/v_2)(B_T - Ln(t))Lc(t) - k_d Ln(t), (16)

<a id='0abf5c84-d16d-43a2-adb0-ea33903c52e8'></a>

where v₁ = Vm/Vc, and v₂ = Vn/Vc, are the ratios, respectively, of the volumes of the medium (Vm) to cytoplasm (Vc), and nucleus (Vn) to cytoplasm. Since the drug is added to the medium at t = 0, with dose D, and comprises TPT-L only, the initial conditions for the model are given by
Lm(0) = D and Hm(0) = Lc(0) = Hc(0) = Ln(0) = 0. (17)

<!-- PAGE BREAK -->

<a id='25f50615-4c60-409d-a6f7-ec0a26d48e4a'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='9db87879-171f-4e97-8354-34d3c6a346e5'></a>

197

<a id='7bf51cd4-d42b-46a6-8620-c81bdeb6f9f1'></a>

In all of the experiments considered in this paper, concentrations are measured in µM, time in minutes and the initial dose _D_ is 10 µM. The eleven parameters in the model are:

*   _k_o,m and _k_c,m, units: min⁻¹ (per minute). Rate constants for deactivation/activation of active/ inactive form of TPT in medium;
*   _k_i and _k_e, units: min⁻¹. Rate constants for flow of the active form of TPT into and out of the cell;
*   _k_o,c and _k_c,c, units: min⁻¹. Rate constants for deactivation/activation of active/inactive form of TPT in cells (cytoplasm);
*   _k_b and _k_d, units: (µM min)⁻¹ and min⁻¹. Rate constants for binding/dissociation of TPT to/from DNA;
*   _B_T, units: µM. Concentration of DNA sites available for TPT (active form) to bind to;
*   _v_1 and _v_2. The ratios, respectively, of the volumes of medium (_V_m) to cytoplasm (_V_c), and nucleus (_V_n) to cytoplasm.

<a id='ccb1dc46-86fb-4526-9606-56a7966dabbf'></a>

All of these parameters are unknown and need to be estimated from experimental data. Using HPLC it is possible to directly measure the concentrations of TPT-L and TPT-H in the extra-cellular medium, and the concentrations of TPT-L and TPT-H in the cellular pool. Before attempting to estimate the parameters from the experimental data, it is first necessary to test whether the parameters are uniquely determined by the model output.

<a id='b56bafb3-1c9d-4a17-86a7-af3d7b3eb159'></a>

5. **Identifiability of cell based model**

In this section, the general theory of Section 2 is applied to the model described by Eqs. (12)–(17). For simplicity, only the results of each step are summarised here, with the full details given in Appendix A.

_Step 1_
The vector **p**, comprising the unknown parameters, is given by

**p** = (k_o,m, k_c,m, k_i, k_e, k_o,c, k_c,c, k_b, k_d, B_T, v_1, v_2)^T.

<a id='d2bebcb3-4fc4-4888-9248-6ab2fb745d97'></a>

The model parameters represent flow rate constants (between locations or forms of drug), or a concentration, or volume ratios, and are therefore positive. This means that the set of admissible parameter vectors, Ω, consists of those vectors $(p_1,...,p_{11})^T$ such that $p_i > 0, 1 \le i \le 11$. The state vector $x(t,p)$ is given by

$x(t,p) = (L_m(t,p), H_m(t,p), L_c(t,p), H_c(t,p), L_n(t,p))^T$

<a id='58e325a0-d371-463f-915d-0960e7164472'></a>

and the set M(_p_) is taken to be

<a id='5efed1ac-ea7b-4ba1-be15-48fef6525c8a'></a>

M(p) = R^5 = {x = (Lm, Hm, Lc, Hc, Ln)^T : Lm, Hm, Lc, Hc, Ln all real}.

<a id='c419ac2e-37aa-44c1-bae5-da00736af2a9'></a>

The output function is given by
$y(\mathbf{t},\mathbf{p}) = (L_m(\mathbf{t},\mathbf{p}), H_m(\mathbf{t},\mathbf{p}), L_i(\mathbf{t}, \mathbf{p}), H_i(\mathbf{t},\mathbf{p}))^T$ (18)

<!-- PAGE BREAK -->

<a id='2e813939-c320-409a-99b2-9394f6a82022'></a>

198                                             N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='980eae87-632d-4807-bf74-ca27de063e6f'></a>

where the subscript _i_ denotes intra-cellular concentrations. By assumption, TPT-H is only present in the cytoplasm and so
$$
H_i(t) = \frac{V_c H_c(t)}{V_c + V_n} = \frac{H_c(t)}{1 + v_2}, \quad \text{where } v_2 = \frac{V_n}{V_c}.
$$

<a id='e2d60105-8533-47f3-b149-60704e535e36'></a>

Since TPT-L is present in both the cytoplasm and nucleus, it is seen that
$L_i(t) = \frac{V_c L_c(t) + V_n L_n(t)}{V_c + V_n} = \frac{L_c(t) + v_2 L_n(t)}{1 + v_2}$

<a id='dce62ab2-8e5b-4689-b64e-001d4a215bac'></a>

In terms of the general mathematical formulation of Eq. (3), the output matrix $C(p)$ is therefore given by

<::
$C(p) = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1/(1+v_2) & 0 & v_2/(1+v_2) \\
0 & 0 & 0 & 1/(1+v_2) & 0
\end{pmatrix}$
: figure::>

<a id='568c37d8-2556-4a15-b646-03c34e978718'></a>

To complete the model description in the general form of Eqs. (1)-(3) we define

<::
$$f(\mathbf{x},\mathbf{p}) = \begin{pmatrix}
-(k_{o,m} + k_i)L_m + k_{c,m}H_m + \left(\frac{k_e}{v_1}\right)L_c \\
(k_i v_1)L_m - (k_e + k_{o,c})L_c + k_{c,c}H_c - k_b(B_T - L_n)L_c + v_2 k_d L_n \\
k_{o,c}L_c - k_{c,c}H_c - \left(\frac{k_b}{v_2}\right)(B_T - L_n)L_c - k_d L_n
\end{pmatrix}
$$
: figure::>

<a id='698e8c89-682d-4ebb-a93d-a66dfb676cf1'></a>

where **x** = ($L_m$, $H_m$, $L_c$, $H_c$, $L_n$)$^T$ is a general vector in $M(\boldsymbol{p})$, and
**x**$_0(\boldsymbol{p})$ = ($D$, 0, 0, 0, 0)$^T$,

<a id='a096e208-10c2-4b6a-9d8a-d102a10be453'></a>

where *D* is the known dose. Again, the initial condition x₀(*p*) is independent of the parameter vector *p* (since *D* is known).

<a id='b4c6349c-e6c9-412e-8b0f-e046e90c33a6'></a>

Step 2
The model satisfies the observability criterion (see Appendix A.1) with the functions given by
$\mu_1(\mathbf{x}, \mathbf{p}) = c_1(\mathbf{p})\mathbf{x} = L_m$ (independent of $\mathbf{p}$),

<a id='11f612f9-1ab8-4f5c-b2df-0026166fc9a3'></a>

μ₂(**x**,**p**) = c₂(**p**)**x** = _H_m (independent of **p**),

<a id='3b93bbbc-625f-4fee-b46e-3f0e125ddcdc'></a>

$\mu_3(\mathbf{x},\mathbf{p}) = c_3(\mathbf{p})\mathbf{x} = \frac{L_c + v_2L_n}{1 + v_2}$,

<a id='4040f89c-fa3d-4ae2-8c4f-e40d242ae4c4'></a>

μ₄(x,p) = c₄(p)x = H_c / (1 + v₂)

<a id='e8c488bc-da66-47f1-9e26-83a1a70ca852'></a>

and
$\mu_5(\mathbf{x}, \mathbf{p}) = \left(\frac{\partial \mu_1}{\partial L_m}(\mathbf{x}, \mathbf{p}), \ldots, \frac{\partial \mu_1}{\partial L_n}(\mathbf{x}, \mathbf{p})\right)f(\mathbf{x}, \mathbf{p}) = -(k_{o,m} + k_i)L_m + k_{c,m}H_m + \frac{k_eL_c}{v_1}$

<!-- PAGE BREAK -->

<a id='aa59902f-c62d-4c1d-85b7-949b51910d68'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217 199

<a id='79b25e14-fc2e-4145-84d7-0067d5854cce'></a>

## Step 3
Let $\bar{p}$ denote an arbitrary parameter vector:

$\bar{p} = (\bar{k}_{o,m}, \bar{k}_{c,m}, \bar{k}_i, \bar{k}_e, \bar{k}_{o,c}, \bar{k}_{c,c}, \bar{k}_b, \bar{k}_d, \bar{B}_T, \bar{v}_1, \bar{v}_2)^T$

By solving Eq. (4) (see Appendix A.2 for details) the following function, $\lambda$, is obtained:

$\lambda(\mathbf{x}) = \lambda(L_m, H_m, L_c, H_c, L_n) = \left(L_m, H_m, \lambda_3(\mathbf{x}), \frac{1+v_2}{1+\bar{v}_2}H_c, \lambda_5(\mathbf{x})\right)^T\quad(19)$

<a id='83c0759d-fb90-40df-803e-08670f255c19'></a>

where

λ₃(x) = v₁/kₑ ( [(kₒ,ₘ + kᵢ) - (k̄ₒ,ₘ + k̄ᵢ)]Lₘ + (k꜀,ₘ - k̄꜀,ₘ)Hₘ + k̄ₑL꜀/v₁ )

(20)

<a id='e5d21342-d21d-4cf8-8d64-a598a372cf73'></a>

and

$\lambda_5(\mathbf{x}) = \frac{1}{v_2} \left( \frac{1+v_2}{1+\bar{v}_2} (L_c + \bar{v}_2 L_n) - \lambda_3(\mathbf{x}) \right)$ (21)

<a id='bc7d1c06-0adc-4780-8e50-c1fdeab82ee6'></a>

Step 4
The final step in the identifiability analysis is to determine the set $\mathcal{S}(\boldsymbol{p})$, comprising those parameter vectors $\boldsymbol{p}$ for which $\lambda$ satisfies Eqs. (5) and (6). In Appendix A.3 it is shown that $\mathcal{S}(\boldsymbol{p})$ comprises all parameter vectors $\boldsymbol{p} \in \Omega$ that satisfy the following relations:

<a id='93ff8a21-8970-4929-a663-d6771f2f48e7'></a>

$\bar{k}_{o,m} = k_{o,m}$, $\bar{k}_{c,m} = k_{c,m}$, $\bar{k}_i = k_i$, $\bar{k}_e = k_e$, $\bar{k}_{o,c} = k_{o,c}$, $\bar{k}_{c,c} = k_{c,c}$, $\bar{k}_d = k_d$,
$\frac{\bar{v}_1}{1+\bar{v}_2} = \frac{v_1}{1+v_2}$, $\bar{k}_b B_T = k_b B_T$, $\frac{\bar{k}_b \bar{v}_1}{\bar{v}_2} = \frac{k_b v_1}{v_2}$. (22)

<a id='dfbec0fe-6274-4543-970e-f8361d60ef0b'></a>

The function λ, which gives the relationship between state trajectories corresponding to indistinguishable parameter vectors, satisfies

λ(x) = λ(Lm, Hm, Lc, Hc, Ln) = (Lm, Hm, v1/v̄1 Lc, v̄1v̄2 / (v1v2) Hc, Ln)^T.

<a id='f7a17ab8-41e2-4e51-b56e-c255d0ef1ade'></a>

Summary of analysis
The seven individual parameters k_o,m, k_c,m, k_i, k_e, k_o,c, k_c.c, and k_d are uniquely determined by the model output. Similarly, the parameter combinations v_1/(1 + v_2), k_bB_T, and (k_bv_1)/v_2 are uniquely determined by the model output. However, the parameters k_b, B_T, v_1, and v_2 are not uniquely determined, and so can take any (positive) value (provided that the above combinations remain fixed) without changing the model output.

<a id='32ad4545-a99d-4751-9731-8510626a1c98'></a>

If either (or both) of the volume ratios v₁ and v₂ can be estimated from other data so that they can be assumed known, prior to the experiment, then v̄₁ = v₁ and v̄₂ = v₂. Substituting these into Eq. (22) shows that, in this case, S(p) = {p} and the model is globally identifiable. In fact, since the analysis remains valid for generic p ∈ Ω the model is structurally globally identifiable.

<a id='65628b51-b546-4d22-bb39-5514db56d314'></a>

If neither v₁ or v₂ is estimated from other experimental data then performing subsequent parameter estimation for the cell based model can yield only partially meaningful values. This is because an infinite number of different combinations of values for the parameters k_b, B_T, v₁, and v₂

<!-- PAGE BREAK -->

<a id='dff26935-6f71-44e8-abad-ce87c73a4e5b'></a>

200

<a id='94a66112-e76b-4b9b-8d73-601ac6f68565'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='2af7c19a-9a61-409f-9dd9-2a56f3a2d1bf'></a>

can give rise to identical model outputs and hence as good fits. This is a particularly bad situation for the cell based model because one of these parameters is B_T, the total concentration of nuclear binding sites for TPT-L. As a result of the identifiability analysis it is seen that an arbitrary value can be assigned to B_T, which generates values for k_b, v₁ and v₂ using the expressions in Eq. (22), and an equally good fit obtained for each value.

<a id='807073e5-5c7f-4174-8886-11cb08ad75fc'></a>

## 6. Parameter estimation

Estimation of the model parameters from experimental data is performed using the computer package Facsimile which uses a robust (implicit) numerical integrator. The parameter fitting consists of an optimisation problem in which the parameters that minimise a weighted least-squares criterion are sought. If y_i(t_j) denotes the jth model output at the jth sampling time (t_j), and d_i(j) the corresponding data point, then Facsimile seeks to minimise the residual sum of squares (RSS) given by

<a id='09153773-6537-4068-b54e-c1b211dbe033'></a>

<::RSS = \sum_{i=1}^{m} \sum_{j=1}^{N} \frac{(d_i(j) - y_i(t_j))^2}{\sigma_i^2},:figure::>

<a id='cfe4a2be-a51d-465f-94ce-69f16b718a5b'></a>

where σᵢ is the standard error for data curve dᵢ. In the absence of estimates for the standard errors, Facsimile uses the product σᵢ = erᵢ, where e is an estimate of the overall accuracy of the data, and rᵢ is the range for data curve dᵢ [30]. Upon completion of the parameter fitting the standard deviations, σ̃ᵢ (i = 1,...,m), of the corresponding (unweighted) residuals (dᵢ(j) – yᵢ(tⱼ)), j = 1,...,N, are calculated. These values are then used as estimates for the standard errors in a subsequent round of parameter fitting by setting σᵢ = σ̃ᵢ, i = 1,...,m. This process is continued iteratively.

<a id='6d68596e-1e75-49b7-92c5-d668da2ba586'></a>

During the fitting procedure, Facsimile performs a statistical analysis to detect parameters that are not well determined by the data (NWD). The values for these parameters are then fixed before continuing the parameter fitting procedure, and treated as unknown in subsequent statistical tests. Let P^0 denote the vector comprising the logarithms of the fitted parameter values. An approximation for the variance-covariance matrix of P - P^0 is then calculated and an estimate for the standard deviation (SDLN) of the logarithm of each parameter value obtained [30]. Assuming that the logarithms of the parameters are normally distributed, the 5% and 95% confidence limits are estimated for the logarithm of each well-determined parameter.

<a id='8e55803a-b68f-4566-ad28-4efb050f7a97'></a>

It is worth noting that, if the sampling errors are normally distributed, then the least squares parameter estimate P⁰ is a maximum-likelihood estimate [27]. Maximum-likelihood estimators are often unbiased, and when they are unbiased, they have minimum variance among all unbiased estimators [2].

<a id='164df9d0-96d3-48de-9d8d-34c5406dc76c'></a>

High performance liquid chromatography (HPLC) was used for quantitating the intracellular and extracellular TPT species, based on the method of [31]. All chemicals and solvents were of HPLC grade and obtained from Sigma Chemical Co., UK. The column used was a Hypersil C18 BDS 100×3 mm (Hypersil, Runcorn, UK) maintained at a constant temperature of 30 °C. The mobile phase was 10 mM KH2PO4, 25% methanol, 0.2% triethylamine adjusted to pH 6.0 and run at a flow rate of 0.6 ml/min. Fluorescence detection of TPT was used at 381 nm excitation and 524

<!-- PAGE BREAK -->

<a id='81915616-a738-4cf3-b6a4-b68a12ca8e06'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='770434e4-e811-499c-9107-b1c3fc2f7a98'></a>

201

<a id='ccc47bc7-5be8-480b-8e5c-dad1b1d2d576'></a>

nm emission. Standards of TPT (kindly donated by SmithKline Beecham) were made up fresh; the lactone form of TPT was generated by acidifying the TPT with 0.1 M HCL and the open ring hydroxy-acid form was made by increasing pH with 0.1 M NaOH.

<a id='0b7a9fe8-f849-43a3-b06a-228c3d9bb906'></a>

Frozen cell medium was thawed and 100 µl immediately diluted with 900 µl ice-cold phosphate buffered saline (PBS), and injected directly onto the HPLC column. Cell aliquots were thawed and 100 µl of cold methanol (-30 °C) added immediately, followed by 900 µl of ice-cold PBS and centrifugation at 13000 rpm for 2 min. Twenty microlitres of the supernatant were injected onto the HPLC column and analysed for TPT. Samples were analysed in triplicate. Standards were used to calculate total TPT (ng) in the cell extract.

<a id='78559e3b-f287-483f-b03d-cc72b02086df'></a>

The cells were seeded at a density of 10⁵ per flask in RPMI (Roswell Park Memorial Institute)
plus 10% fetal calf serum, incubated at 37 C and spiked with TPT (lactone). Samples of cells and
medium were taken at specified times, snap frozen to -70 C and kept at this temperature until
analysed.

<a id='0959cb59-20fd-4d21-96a5-a0599c362dad'></a>

Two HPLC data sets are used in the parameter estimation. These sets each provide the mean (together with standard deviation) of three separate experiments. In each experiment, the values for the extracellular concentrations of TPT-L and TPT-H, and the total intra-cellular concen- trations of TPT-L and TPT-H (four measurements in total), are recorded at sampling times of t = 5, 10, 15, and 20 min after drug administration.

<a id='2094c7a3-8cca-4307-b727-f71580810d7c'></a>

It is known from the previous section that the model is unidentifiable in the sense that, for generic parameter vectors **p**, there are an (uncountably) infinite number of other parameter vectors **p̄** for which the model has identical output to that with **p**. At this stage, we would have little confidence in estimates for the parameters derived from collected HPLC data. Moreover, there are eleven parameters to estimate from only 32 data points, if both data series are used. To ensure that the model is globally identifiable and to reduce the number of parameters to be estimated, the volume ratios v₁ and v₂ are estimated by optical sectioning using a confocal microscope. Measurements are made of 14 cells to obtain the following mean values: Vc = 829 µm³ (SD 232) and Vn = 326 µm³ (SD 85.5). The culture medium has a volume of 2 ml (2×10¹² µm³) and the cells are set at a fixed density, using Coulter Counter estimation, of 2×10⁵ cells per ml (giving 4×10⁵ cells in total). The volume ratios are therefore given by v₁ = Vm/Vc = (2 × 10¹²)/ (829 × (4 × 10⁵)) = 6.0314 × 10³, and v₂ = Vn/Vc = 326/829 = 3.9324 × 10⁻¹. It should be noted that actual cellular volume, as estimated here, may not reflect the apparent volume of distribution. Factors such as intracellular protein binding may greatly affect this.

<a id='90fbb991-af65-4227-bfd5-868425f6190e'></a>

The fitted parameter values are presented in Table 2, where it is seen that three of the nine parameters are not well-determined by the data.

<a id='6ed75fdb-b9d8-4113-b913-a6f7d4a24314'></a>

This means that small changes in the values of the parameters k_c,m, k_b, and B_T will not affect the goodness of fit, as measured by the least squares criterion. It can also be seen that the values for the hydrolysis rate constants k_o,m and k_c,m are outside of the range of values determined from the pH buffer experiments. There is a level of ill-conditioning in the problem of defining the region of the medium from which drug may flow into the cells, since the extracellular compartments are, by definition, assumed to be homogeneous and well-mixed. If cellular TPT-L influx were from a smaller region of the medium, that is not well-mixed with the remainder, then the TPT-L to TPT-H ratio in this region might seem more favoured to TPT-H than expected from the pH buffer experiments. The model can be extended to consider such a situation by splitting the medium into a region from which drug can flow into the cells, and one from which it does not. Such an

<!-- PAGE BREAK -->

<a id='c77075d4-cc87-4faa-bef1-c82402b133c4'></a>

202

<a id='0b4757e3-3334-451f-8160-e234c3e27956'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='c2a7c229-b470-47ef-b776-cb893a5b5b41'></a>

Table 2
The parameter values for the model (12)-(16) estimated from HPLC data
<table id="17-1">
<tr><td id="17-2">Parameter</td><td id="17-3">Value</td><td id="17-4">SDLN</td><td id="17-5">5%</td><td id="17-6">95%</td></tr>
<tr><td id="17-7">k_o,m (min⁻¹)</td><td id="17-8">2.8900×10⁻²</td><td id="17-9">0.0452</td><td id="17-a">2.6831×10⁻²</td><td id="17-b">3.1128×10⁻²</td></tr>
<tr><td id="17-c">k_i (min⁻¹)</td><td id="17-d">3.0900×10⁻⁴</td><td id="17-e">0.7098</td><td id="17-f">9.6125×10⁻⁵</td><td id="17-g">9.9330×10⁻⁴</td></tr>
<tr><td id="17-h">k_e (min⁻¹)</td><td id="17-i">1.0140</td><td id="17-j">0.6662</td><td id="17-k">3.3890×10⁻¹</td><td id="17-l">3.0339</td></tr>
<tr><td id="17-m">k_o,c (min⁻¹)</td><td id="17-n">2.6553×10⁻²</td><td id="17-o">0.3243</td><td id="17-p">1.5575×10⁻²</td><td id="17-q">4.5268×10⁻²</td></tr>
<tr><td id="17-r">k_{c,e} (min^{-1})</td><td id="17-s">1.8637×10^{-1}</td><td id="17-t">0.4099</td><td id="17-u">9.4952×10^{-2}</td><td id="17-v">3.6580×10^{-1}</td></tr>
<tr><td id="17-w">k_d (min^{-1})</td><td id="17-x">4.4489</td><td id="17-y">0.6914</td><td id="17-z">1.4267</td><td id="17-A">1.3873×10^{1}</td></tr>
<tr><td id="17-B">k_{c,m} (min^{-1})</td><td id="17-C">1.0600×10^{-4}</td><td id="17-D">NWD</td><td id="17-E"></td><td id="17-F"></td></tr>
<tr><td id="17-G">k_b (µM min)^{-1}</td><td id="17-H">8.5341×10^{-4}</td><td id="17-I">NWD</td><td id="17-J"></td><td id="17-K"></td></tr>
<tr><td id="17-L">B_T (μΜ)</td><td id="17-M">2.8900×10^{1}</td><td id="17-N">NWD</td><td id="17-O"></td><td id="17-P"></td></tr>
</table>

<a id='55de54a1-272e-4618-b1de-2114fec341ae'></a>

extension would incorporate an element of mixing into the model as flows between the extra- cellular regions. However, extending the model in this fashion would involve additional para- meters, including the ratio of the volumes of the regions, that would also need to be estimated from the data.

<a id='96b2004d-8df2-4a5f-9f2e-c52f835a118d'></a>

In Fig. 4, the simulated output of the model, with the parameters taking the values in Table 2, is plotted together with the experimental data.

<a id='3564466a-9a40-41fd-bf84-1ad60b9e87c2'></a>

The limited number of sampling time points and variation in the two data series results in less well-determined parameter values since different model responses can give similar least-squares errors. Increasing the number of sampling time points should narrow the class of possible model responses, and thereby result in better determined fitted parameter values.

<a id='782d54a5-1394-4f10-8467-b0b31e4705ce'></a>

The estimated correlation matrix for the well-determined parameters is given in Table 3. From this table it is seen that the highest correlation is between the rate constants for the flow of (active) TPT into and out of the cells ($k_i$ and $k_e$). As in the free solution pH experiments, the (intra- cellular) inactivation/activation rate constants are highly correlated.

<a id='ade2fa2c-b60e-49c1-b0f5-367c07c16794'></a>

<::chart: The figure displays two plots side-by-side, labeled 'Extracellular' and 'Intracellular', showing concentration (Conc (µM)) versus time (Time (mins)). Both plots include simulated output from a full model (lines) for TPT-L (solid lines) and TPT-H (dashed lines), fitted to experimental data (circles for TPT-L and squares for TPT-H), with vertical bars indicating standard deviation. 

(i) Extracellular pool: The left plot, titled 'Extracellular', shows Conc (µM) on the y-axis (0 to 10) and Time (mins) on the x-axis (0 to 20). The solid line and corresponding circular data points (TPT-L) show a decreasing concentration from approximately 10 µM at 0 mins to about 5 µM at 20 mins. The dashed line and corresponding square data points (TPT-H) show an increasing concentration from 0 µM at 0 mins to about 4.5 µM at 20 mins.

(ii) Cellular pool: The right plot, titled 'Intracellular', shows Conc (µM) on the y-axis (0 to 16) and Time (mins) on the x-axis (0 to 20). The solid line and corresponding circular data points (TPT-L) show a concentration that increases from 0 µM, peaks around 11.5 µM between 5 and 10 mins, and then decreases to about 8 µM at 20 mins. The dashed line and corresponding square data points (TPT-H) show a slowly increasing concentration from 0 µM at 0 mins to approximately 1.5 µM at 20 mins. Some standard deviation bars are too small to be visible.::>

Fig. 4. The plots represent the simulated output of the full model (lines) for TPT-L (solid) and TPT-H (dashed) fitted to the data (circles and squares, respectively), with vertical bars denoting (±) standard deviation (note that some bars are too small to be visible in the plots). 

<!-- PAGE BREAK -->

<a id='a1e65895-fbe1-480a-b4a0-13df3584c54a'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='82b0637d-0c3d-458f-9869-0fd59ab63406'></a>

203

<a id='0ba320c6-2095-4924-bf5b-799011118c92'></a>

Table 3
The estimated correlation matrix for the well-determined parameters in the full model
<table id="18-1">
<tr><td id="18-2"></td><td id="18-3">k_{o,m}</td><td id="18-4">k_d</td><td id="18-5">k_i</td><td id="18-6">k_e</td><td id="18-7">k₀,c</td><td id="18-8">kc,c</td></tr>
<tr><td id="18-9">k_{o,m}</td><td id="18-a">1.000</td><td id="18-b">-0.009</td><td id="18-c">0.009</td><td id="18-d">-0.009</td><td id="18-e">-0.057</td><td id="18-f">-0.060</td></tr>
<tr><td id="18-g">k_d</td><td id="18-h">-0.009</td><td id="18-i">1.000</td><td id="18-j">-0.440</td><td id="18-k">-0.444</td><td id="18-l">-0.091</td><td id="18-m">-0.270</td></tr>
<tr><td id="18-n">k_i</td><td id="18-o">0.009</td><td id="18-p">-0.440</td><td id="18-q">1.000</td><td id="18-r">0.983</td><td id="18-s">-0.189</td><td id="18-t">0.418</td></tr>
<tr><td id="18-u">k_e</td><td id="18-v">-0.009</td><td id="18-w">-0.444</td><td id="18-x">0.983</td><td id="18-y">1.000</td><td id="18-z">-0.117</td><td id="18-A">0.428</td></tr>
<tr><td id="18-B">K o,c</td><td id="18-C">-0.057</td><td id="18-D">-0.091</td><td id="18-E">-0.189</td><td id="18-F">-0.117</td><td id="18-G">1.000</td><td id="18-H">0.742</td></tr>
<tr><td id="18-I">K c,c</td><td id="18-J">-0.060</td><td id="18-K">-0.270</td><td id="18-L">0.418</td><td id="18-M">0.428</td><td id="18-N">0.742</td><td id="18-O">1.000</td></tr>
</table>

<a id='d8069365-7763-4ccf-b25d-aa192e2290de'></a>

To see whether the (weighted) residuals, the (weighted) errors between the data points and the simulated output of the model, are normally distributed, we consider a normal probability plot in Fig. 5 [32].

<a id='c0cf53a1-04f0-4d5c-9d9b-034dd678b604'></a>

To do this the residuals are ranked in ascending numerical order to give a list R1 < R2 < ... < R32. Setting zᵢ = (i – 0.5)/32, for i = 1, ..., 32, a list Z1,..., Z32 is obtained where Zᵢ is the point in the normal cumulative distribution with probability zᵢ. The Zᵢ are then plotted against the Rᵢ (horizontal direction), and if the residuals are normally distributed, then the plot should be linear. Fig. 5 shows an approximately linear relation between the Zᵢ and Rᵢ, giving some justification to an assumption of normally distributed errors.

<a id='5f7afff9-7dd5-44b6-9e0d-d08fa5b62b76'></a>

In Fig. 6 the effects of variation in the fixed values for the volume ratios v₁ and v₂, on the intracellular simulation time curves is shown.

<a id='428d8143-48d1-4da3-b29f-ad09ec6a9b25'></a>

If the values for the volumes V_c and V_n vary within two standard deviations, and allowing for a ±1% error in the value used for the number of cells, the volume ratios v_1 and v_2 can vary in the ranges 3.79×10^3–1.40×10^4, and 0.12–1.36, respectively. Variation in the value of v_1 has the largest effect on the intracellular time curves. The qualitative behaviour of the curves is not affected by variation in the volume ratios. There is a negligible effect on the extracellular time curves

<a id='ef39ae7d-1613-4ad7-bf67-4afb5ca7c57a'></a>

<::chart: Normal probability plot. The x-axis is labeled "Ordered residuals" and ranges from -4 to 4. The y-axis ranges from -3 to 3. A series of black data points are plotted, showing a curved distribution.::>

Fig. 5. A normal probability plot for the residuals in the non-linear least-squares fit of the full model to HPLC data. The residuals are plotted in ascending numerical order on the horizontal axis, against cumulative probabilities in N(0, 1) transformed to a linear scale.

<!-- PAGE BREAK -->

<a id='48bfd4bd-bf78-4da3-8200-e9105ff4f8b0'></a>

204

<a id='6b2175bb-f30b-496a-ae35-846a090c22bf'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='390b8e27-a1b5-441f-9bb9-49b283ec7da9'></a>

<::chart:(i) Effects of variations in v₁ on Lᵢ. Line chart with Time (mins) on the x-axis (0 to 20) and Conc (µM) on the y-axis (0 to 30). Seven curves (labeled a-g) show the concentration over time. Curve 'd' is dashed. The curves show an initial rise followed by a decline. Curve 'a' has the lowest peak, and curve 'g' has the highest peak. (ii) Effects of variations in v₁ on Hᵢ. Line chart with Time (mins) on the x-axis (0 to 20) and Conc (µM) on the y-axis (0 to 3.5). Seven curves (labeled a-g) show the concentration over time. Curve 'd' is dashed. The curves show an initial rise followed by a plateau or slow decline. Curve 'a' has the lowest concentration, and curve 'g' has the highest concentration. (iii) Effects of variations in v₂ on Lᵢ. Line chart with Time (mins) on the x-axis (0 to 20) and Conc (µM) on the y-axis (0 to 16). Seven curves (labeled a-g) show the concentration over time. Curve 'd' is dashed. The curves show an initial rise followed by a decline. Curve 'g' has the lowest peak, and curve 'a' has the highest peak. (iv) Effects of variations in v₂ on Hᵢ. Line chart with Time (mins) on the x-axis (0 to 20) and Conc (µM) on the y-axis (0 to 1.8). Seven curves (labeled a-g) show the concentration over time. Curve 'd' is dashed. The curves show an initial rise followed by a plateau or slow decline. Curve 'g' has the lowest concentration, and curve 'a' has the highest concentration.::>Fig. 6. Effects of variation in the volume ratios v₁ and v₂ on the intracellular time curves (Lᵢ and Hᵢ). In figures (i) and (ii) v₁ takes the values (a) 3.0×10³, (b) 4.0×10³, (c) 5.0×10³, (d, fixed value) 6.0314×10³, (e) 8.6×10³, (f) 1.12×10⁴, (g) 1.38×10⁴. In figures (iii) and (iv) v₂ takes the values (a) 0.1, (b) 0.2, (c) 0.3, (d, fixed value) 0.3932, (e) 0.72, (f) 1.04, (g) 1.36.

<a id='894813a9-0691-4432-b7c3-b579583e95a2'></a>

varying the volume ratios in the ranges above. This shows that there must be other factors
involved in causing the differences between the two experimental data sets (see Fig. 4).

<a id='88055bd4-7aa7-4db6-9f77-8a7377e4077d'></a>

7. Simulation results

In this section, the mathematical model is used to make predictions concerning the effects of changes in dose or cellular drug efflux on the concentration of active drug binding to DNA. These predictions provide essential information for designing future experimental regimes which optimise delivery to target sites. The total accumulation of bound active drug, over the first hour after dose addition, can be regarded as the 'hit-on-target' since it is this bound (active) drug that causes the cellular stress responses. Hit-on-target corresponds to the area under the curve (AUC) for the plot of the bound TPT-L (L(t)) time course, and has units µM mins. Direct measurements by others [10] show the rapid induction of DNA damage by the camptothecins and the rapid reversal

<!-- PAGE BREAK -->

<a id='f968a0c3-e4a4-4ecc-844c-401ae2431d36'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='2d6a7180-d193-4cb5-98ed-1b6c19930a6f'></a>

205

<a id='7fbc0046-9ae8-4863-9980-a6b35c99dd2e'></a>

of that damage following drug removal. This suggests that the cell “experience” of active drug
(given here as an exposure times dose calculation of AUC) will effectively determine the known
dose and schedule dependency of the drug.

<a id='41a9e636-3586-47fb-bdf6-4858be8a25d7'></a>

## 7.1. Dose dependence

To assess the effects of different doses on the concentration of active drug binding to DNA, and the subsequent hit-on-target, the mathematical model (12)-(17), with parameters taking the values in Table 2, is simulated with the initial dose D taking values from 0.2 to 20 \u00b5M. The simulated output of L_n(t) over the first hour following each dose is shown in Fig. 7(i) and (ii).

<a id='49e363ec-0b11-4bb9-a3ba-38808ccd8b8d'></a>

The corresponding area under the curve (AUC) of L_n(t) for each is shown in Table 4. These values are plotted against dose in Fig. 7(v) (solid line) where it is seen that there is a linear relationship between dose and hit-on-target.

<a id='83ffb913-e075-448b-a842-4c8fffc99aef'></a>

A comparison between the effects of a bolus injection of drug and a continuous infusion can
also be made. To allow for a continuous infusion of active drug the initial conditions for the
model, Eqs. (12)-(16), with parameters taking the values in Table 2, are set as

<a id='c97cc0e3-679f-4daa-ab89-4beac8b45c44'></a>

L_m(0) = H_m(0) = L_c(0) = H_c(0) = L_n(0) = 0

<a id='8e8999c5-33e1-43c9-b3e8-f5b0156cf73c'></a>

and Eq. (12) is replaced by the following

<a id='3e146511-9d4c-4a7e-ae73-ba00296c2706'></a>

$\frac{d}{dt} L_m(t) = \frac{D_{inf}}{T_{inf}} u(t) - (k_{o,m} + k_i) L_m(t) + k_{c,m} H_m(t) + \left(\frac{k_e}{v_1}\right) L_c(t), \quad (23)$

<a id='7e034191-aa13-4979-a1df-2cc38181f83a'></a>

where $D_{inf}$ is the dose, $T_{inf}$ the length of infusion and $u$ a unit step function:

$u(t) = \begin{cases}
1 & 0 \leq t < T_{inf},\\
0 & t \geq T_{inf}.
\end{cases}$

<a id='7666bb90-28e8-4e78-b3bd-6180a247c53b'></a>

Repeating the previous experiment to assess the effect of changes in the dose on the hit-on-target,
with a constant infusion over the first 30 min (Tinf = 30 mins), gives rise to the simulated output
given in Fig. 7(iii) and (iv). The corresponding AUC of L_n(t) for each is shown in Table 4. These
values are plotted against dose in Fig. 7(v) (dotted line) where it is seen that there is a linear
relationship between dose and hit-on-target.

<a id='939df1ac-b9d6-4f9b-970a-a372df251783'></a>

It can also be seen from Fig. 7 that the model predicts that the peak concentration of bound (active) drug in the nucleus is higher (approximately 35% higher in each case) for the bolus injection when compared with a constant infusion of the same total dose. The total accumulation of bound drug (AUC) is also higher for each bolus dose compared with a constant infusion of the same total dose. Suppose that one is interested in keeping the concentration of bound (active) drug (L_n(t)) above a certain threshold for a given period. This could be critical to the pharmacodynamic action of TPT since it is selectively toxic to cells undergoing DNA replication. The maintenance of minimally active drug concentrations will be required so that TPT can act on cells as they enter the DNA replicative phase (S phase) as a consequence of cell cycle traverse (SU-DHL-4 cells having a 21 h doubling period) and hence act to recruit cells to the cytotoxic pathway. For a total dose of 2 µM (Plot (g) in Fig. 7) it is seen that L_n(t) exceeds a threshold of 0.03 µM for at least 18.5 min for a bolus dose, and 10 min for a constant infusion. However, a

<!-- PAGE BREAK -->

<a id='27a0383c-c4df-4192-a647-cd5296db7276'></a>

206

<a id='830ca44b-5ad6-4f0a-845b-116081032fe8'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='73cc7675-b77b-40be-b6f4-56f79675ab20'></a>

<::figure: This figure contains five plots related to drug concentration and dose. (i) Bolus doses (a)-(g) is a line graph showing Concentration (µM) on the y-axis (from 0 to 0.05) versus Time (mins) on the x-axis (from 0 to 60). It displays seven curves labeled 'a' through 'g', where 'a' is the lowest and 'g' is the highest. (ii) Bolus doses (g)-(p) is a line graph showing Concentration (µM) on the y-axis (from 0 to 0.5) versus Time (mins) on the x-axis (from 0 to 60). It displays ten curves labeled 'g' through 'p', where 'g' is the lowest and 'p' is the highest. (iii) Infusion doses (a)-(g) is a line graph showing Concentration (µM) on the y-axis (from 0 to 0.035) versus Time (mins) on the x-axis (from 0 to 60). It displays seven curves labeled 'a' through 'g', where 'a' is the lowest and 'g' is the highest. (iv) Infusion doses (g)-(p) is a line graph showing Concentration (µM) on the y-axis (from 0 to 0.35) versus Time (mins) on the x-axis (from 0 to 60). It displays ten curves labeled 'g' through 'p', where 'g' is the lowest and 'p' is the highest. (v) hit-on-target vs dose is a line graph showing hit-on-target (µM mins) on the y-axis (from 0 to 15) versus Dose (µM) on the x-axis (from 0 to 20). It contains a legend with four entries: 'bolus' (solid line), 'Tinf=15' (dotted line), 'Tinf=30' (dashed line), and 'Tinf=45' (dash-dot line), each represented by a line on the plot. The 'bolus' line is the highest, followed by Tinf=15, Tinf=30, and Tinf=45, which is the lowest.::>

<a id='9315c810-92a0-4d5d-8e3a-6778b5869b43'></a>

Fig. 7. The effect on L_n(t), over the first hour, of different doses: (a) 0.2 μM, (b) 0.4 μM, (c) 0.6 μM, (d) 0.8 μM, (e) 1 μM, (f) 1.5 μM, (g) 2 μM, (k) 4 μM, (l) 6 μM, (m) 8 μM, (n) 10 μM, (o) 15 μM and (p) 20 μM; where the dose is given as a bolus injection or a constant infusion. Also shown is a plot of hit-on-target against dose.

<a id='d8d90797-e4d1-4201-b120-2fca01c6df74'></a>

threshold of 0.02 µM is exceeded by L_n(t) for at least 33 min for a bolus dose and 34.5 min for a constant infusion.

<a id='d7a07fe3-435f-4a44-bcff-7edcaa89c461'></a>

Also shown in Table 4 is the hit-on-target for constant infusions of 15 and 45 min, respectively. It is shown from this table that the hit-on-target decreases as the length of the infusion increases.

<!-- PAGE BREAK -->

<a id='859c4d30-f1ca-43de-9152-fcf12cceb2b0'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='e9038c86-95c3-46f2-b90f-89a7952d0c55'></a>

207

<a id='2beb8ba8-b193-45a2-ab23-1c712fb728db'></a>

Table 4
The dose dependence of the hit-on-target (in µM mins) following a bolus injection of drug, or a constant infusion lasting
$T_{inf}$ minutes
<table id="22-1">
<tr><td id="22-2">Tinf (min)</td><td id="22-3" colspan="7">Total dose D (µM)</td></tr>
<tr><td id="22-4"></td><td id="22-5">0.2</td><td id="22-6">0.4</td><td id="22-7">0.6</td><td id="22-8">0.8</td><td id="22-9">1.0</td><td id="22-a">1.5</td><td id="22-b">2.0</td></tr>
<tr><td id="22-c">15</td><td id="22-d">0.1382</td><td id="22-e">0.2764</td><td id="22-f">0.4145</td><td id="22-g">0.5526</td><td id="22-h">0.6907</td><td id="22-i">1.0359</td><td id="22-j">1.3808</td></tr>
<tr><td id="22-k">30</td><td id="22-l">0.1269</td><td id="22-m">0.2539</td><td id="22-n">0.3808</td><td id="22-o">0.5077</td><td id="22-p">0.6345</td><td id="22-q">0.9516</td><td id="22-r">1.2685</td></tr>
<tr><td id="22-s">45</td><td id="22-t">0.1117</td><td id="22-u">0.2233</td><td id="22-v">0.3350</td><td id="22-w">0.4466</td><td id="22-x">0.5582</td><td id="22-y">0.8371</td><td id="22-z">1.1159</td></tr>
<tr><td id="22-A">bolus</td><td id="22-B">0.1466</td><td id="22-C">0.2931</td><td id="22-D">0.4396</td><td id="22-E">0.5860</td><td id="22-F">0.7325</td><td id="22-G">1.0984</td><td id="22-H">1.4642</td></tr>
<tr><td id="22-I"></td><td id="22-J">2.0</td><td id="22-K">4.0</td><td id="22-L">6.0</td><td id="22-M">8.0</td><td id="22-N">10.0</td><td id="22-O">15.0</td><td id="22-P">20.0</td></tr>
<tr><td id="22-Q">15</td><td id="22-R">1.3808</td><td id="22-S">2.7591</td><td id="22-T">4.1347</td><td id="22-U">5.5077</td><td id="22-V">6.8782</td><td id="22-W">10.2932</td><td id="22-X">13.6921</td></tr>
<tr><td id="22-Y">30</td><td id="22-Z">1.2685</td><td id="22-10">2.5349</td><td id="22-11">3.7991</td><td id="22-12">5.0611</td><td id="22-13">6.3210</td><td id="22-14">9.4613</td><td id="22-15">12.5884</td></tr>
<tr><td id="22-16">45</td><td id="22-17">1.1159</td><td id="22-18">2.2302</td><td id="22-19">3.3427</td><td id="22-1a">4.4536</td><td id="22-1b">5.5627</td><td id="22-1c">8.3281</td><td id="22-1d">11.0830</td></tr>
<tr><td id="22-1e">bolus</td><td id="22-1f">1.4642</td><td id="22-1g">2.9254</td><td id="22-1h">4.3837</td><td id="22-1i">5.8390</td><td id="22-1j">7.2913</td><td id="22-1k">10.9093</td><td id="22-1l">14.5090</td></tr>
</table>

<a id='bbf86f5c-9928-4a7f-839b-e17bd61d16b6'></a>

The relationship between dose and hit-on-target though still remains linear. The peak concen-
tration of bound active drug, for each dose, is 13% and 59%, respectively, higher for the bolus
dose compared with constant infusions over 15 and 45 min.

<a id='6697d321-6bf2-44e7-8d9a-ec63d232e7ba'></a>

7.2. Drug resistance

We consider the impact of drug resistance pathways on the concentration of active drug binding to DNA by simulating the effects of changes in the cellular efflux rate constant k_e. As before, a period of 1 h following a bolus injection of 10 \u00b5M is considered. The fitted value for k_e is 1.0140 (per minute). The simulated output of L_n(t) over the first 60 min is shown in Fig. 8, with k_e taking values from 0 min\u207b\u00b9 to 10 min\u207b\u00b9.

<a id='f0786db2-30a0-4646-8822-73a4ad0b00a5'></a>

The corresponding hit-on-target for each is shown in Table 5. The non-linearity of the system is clearly demonstrated by plotting hit-on-target against the constrained efflux value ($k_e$) (Fig. 8(iv)).

<a id='c7dd132a-423f-4b85-b6d6-da6568256849'></a>

Changes in the value of the efflux rate constant k_e cause a corresponding non-linear change in the peak concentration of L_n(t) and the AUC. Increasing the value of k_e, which corresponds to a faster rate of drug clearance from the cytoplasm, decreases the peak value for target engagement L_n(t). At the maximum imposed efflux of 10 min⁻¹ approximately 0.03 µM peak target sites become engaged, while completely blocking drug efflux leads to a maximum engagement of target sites at a concentration of 5.5 µM. As expected at the faster rate of clearance of TPT-L from the cytoplasm, less drug is available to bind to DNA and topoisomerase I. It is interesting to note from Fig. 8(iv) that increases in the efflux rate constant (k_e) above the fitted value (1.0140 per minute), result in small decreases in the corresponding hit-on-target. Conversely, decreases in this value result in large increases in the hit-on-target. This is advantageous from the point of view of maximising the hit-on-target for a given dose, but also indicate how small changes in efflux may have severely limiting effects on drug efficacy.

<!-- PAGE BREAK -->

<a id='b9814872-b16b-4622-9637-219c1bbd7dfd'></a>

208                               N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='f2d4d550-9079-4463-9dca-fd2180cdeb09'></a>

<::Figure 8: A composite figure showing four plots. The figure caption is: Fig. 8. The effect on L_n(t), over the first hour, of different values for parameter k_e: (a) 0 min⁻¹, (b) 0.01 min⁻¹, (c) 0.05 min⁻¹, (d) 0.1 min⁻¹, (e) 0.5 min⁻¹, (f) 0.75 min⁻¹, (g) 1 min⁻¹, (k) 1.25 min⁻¹, (l) 1.5 min⁻¹, (m) 2 min⁻¹, (n) 3 min⁻¹, (o) 5 min⁻¹ and (p) 10 min⁻¹. Also shown is a plot of hit-on-target against the value of k_e. The plots are arranged in a 2x2 grid. 

(i) Top-left plot, titled "Values (a)-(e)", is a line chart with 'Time (mins)' on the x-axis (0 to 60) and 'Concentration (µM)' on the y-axis (0 to 6). It displays five increasing curves labeled 'a' through 'e', where 'a' has the highest concentration at 60 mins and 'e' has the lowest.

(ii) Top-right plot, titled "Values (e)-(l)", is a line chart with 'Time (mins)' on the x-axis (0 to 60) and 'Concentration (µM)' on the y-axis (0 to 0.45). It displays five curves labeled 'e', 'f', 'g', 'k', 'l', each rising to a peak and then decreasing. Curve 'e' shows the highest peak concentration, and 'l' shows the lowest peak concentration among these curves.

(iii) Bottom-left plot, titled "Values (l)-(p)", is a line chart with 'Time (mins)' on the x-axis (0 to 60) and 'Concentration (µM)' on the y-axis (0 to 0.16). It displays five curves labeled 'l', 'm', 'n', 'o', 'p', similar in shape to the previous plot, rising to a peak and then decreasing. Curve 'l' shows the highest peak concentration, and 'p' shows the lowest peak concentration among these curves.

(iv) Bottom-right plot, titled "hit-on-target vs k_e", is a line chart with 'k_e (min⁻¹)' on the x-axis (0 to 10) and 'hit-on-target (µM mins)' on the y-axis (0 to 250). It shows a single curve that starts at a very high value on the y-axis, sharply decreases as k_e increases from 0 to about 2, and then levels off at a low value for higher k_e values.::>

<a id='2c6892fe-50ad-4712-807d-7a2a8c640ff7'></a>

Table 5
The effects of changes in the cellular efflux parameter, $k_e$, on the hit-on-target of a bolus injection of 10 µM
<table id="23-1">
<tr><td id="23-2">kₑ (min⁻¹)</td><td id="23-3">0</td><td id="23-4">0.01</td><td id="23-5">0.05</td><td id="23-6">0.10</td><td id="23-7">0.50</td><td id="23-8">0.75</td><td id="23-9">1.00</td></tr>
<tr><td id="23-a">HoT (µM min)</td><td id="23-b">214.943</td><td id="23-c">182.597</td><td id="23-d">104.890</td><td id="23-e">64.162</td><td id="23-f">14.589</td><td id="23-g">9.813</td><td id="23-h">7.392</td></tr>
<tr><td id="23-i">kₑ (min⁻¹)</td><td id="23-j">1.00</td><td id="23-k">1.25</td><td id="23-l">1.50</td><td id="23-m">2.00</td><td id="23-n">3.00</td><td id="23-o">5.00</td><td id="23-p">10.00</td></tr>
<tr><td id="23-q">HoT (µM min)</td><td id="23-r">7.392</td><td id="23-s">5.929</td><td id="23-t">4.949</td><td id="23-u">3.719</td><td id="23-v">2.484</td><td id="23-w">1.493</td><td id="23-x">0.747</td></tr>
</table>

<a id='6fedf9d9-ab61-4c4e-846e-59e1207887c3'></a>

## 8. Conclusion

In this paper a mathematical model of the in vitro kinetics of the anti-cancer agent topotecan has been derived and fitted to HPLC data. The approach taken was a knowledge-based one in which the form of the mathematical model is based on prior biological information or assumptions. The consequences of these assumptions can then be investigated using the model.

<!-- PAGE BREAK -->

<a id='7586fa9e-d4b3-4f4c-adce-d16cfc3b8434'></a>

*N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217*

<a id='0096001b-ceab-4a66-929f-327ca95cd299'></a>

209

<a id='5ece0300-af17-43af-850f-63c9936d4cf1'></a>

In the fitting process, a large number of parameters (nine in total) were fitted to relatively little data (32 data points). As a result of the large variation between the two HPLC data sets, and more importantly, the small number of sampling times (or measurement times), some of the parameters were not well determined by the data. This was due to different model responses giving similar least-squares errors. By increasing the number of sampling (measurement) times, the class of possible model responses should be reduced, as should the set of potential parameter values. However, prior knowledge concerning the qualitative forms of the concentration time courses for each form of drug in each location, could be used to reject some of the possible model responses.

<a id='8f8e49cf-7fc9-4197-aecc-3c5935bd51c6'></a>

The model derived in this paper does not address inter-cellular heterogeneity; this is because the HPLC data only provide concentration measurements for the entire population of cells. The model with fitted parameter values therefore represents the average of a heterogeneous popula- tion. However, together with the predictive modelling resulting from constraining the cellular efflux rate constant ($k_e$) it is quite clear that even small decreases in $k_e$ will have severe conse- quences on the hit-on-target. Hence the natural variation in efflux capabilities within a population should demonstrate a range of drug delivery to the nucleus. Therefore the next stage is to apply the same techniques used in this paper to derive models based on single cell measurements and these models can be combined to more accurately represent a heterogeneous population (such as found in tumours) and validation sought using single cell analytical methods.

<a id='7219ef4e-b496-45aa-9fda-6353f14d4263'></a>

At present it is assumed that all of the drug in the nucleus is TPT-L and bound to DNA. This is a simplification of the real situation that results in a degree of error in the volume ratios although current evidence from cell-free systems partially supports this assumption. Further experimental work is required to explore this issue and to quantify possible errors in these parameters. It may prove necessary to redefine the intra-cellular compartments as bound and unbound drug, rather than cytosolic and nuclear. This, however, requires additional data concerning the volume of DNA binding sites within the cell nucleus. Current work is directed towards using advanced high spatial and temporal resolution imaging methods to address these issues.

<a id='30f03371-d88d-41f9-b60f-a13ef88164fc'></a>

A crucial step in the modelling process is the analysis of the (structural) identifiability of the postulated mathematical model with respect to the proposed experiment to acquire data for parameter fitting. A globally identifiable model is one for which the model output, that is, the variables or combination of variables that are to be directly measured, uniquely determines all of the unknown parameters. In this paper a new approach [23] for performing an identifiability analysis has been applied. This approach is valid for models with a single external input that is analytic or impulsive (e.g., bolus injection). The model was initially found to be unidentifiable, unless at least one of the volume ratios (v1 and v2) was assumed known (these ratios were estimated from additional experimental data). This demonstrates the importance of an identifiability analysis since parameter estimates for unidentifiable parameters are almost meaningless.

<a id='7eda57a6-f216-4718-aba3-868c429aa43d'></a>

Using HPLC it is possible to measure the total concentrations of active and inactive drug in the medium and cells. However, it is not possible to distinguish between cytosolic and nuclear con-centrations, and any physico-chemical fractionation studies would not easily prevent redistribu-tion and compartmental loss of TPT. An important variable in the mathematical model, therefore, is L_n(t), the concentration of nuclear TPT-L. In particular, predictions of peak con-centration or hit-on-target can be readily obtained using the model. Therefore the modelling allows insights into the stability of the drug and predictions to be made concerning quantities that cannot be directly measured, such as the concentration of TPT-L bound to DNA. This enables

<!-- PAGE BREAK -->

<a id='b68a47e3-ee15-4f0e-b5f8-f008ffd62655'></a>

210 N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='010e9947-330d-4b0d-b5e2-5f5fdffb1058'></a>

experimentalists to explore, and predict, the delivery of active drug to the nuclear target. Model predictions show that the bolus delivery is far more effective at engaging an accumulated number of binding sites over time at high doses (>5 µM). However at lower doses the infusion and bolus methods become more equivalent. The linking of this pharmacokinetic prediction to the pharmacodynamic elucidation of critical doses for cell cycle related stress responses has implications for the comprehensive understanding of the anti-cancer action of the camptothecins. This leads to a rationale for modelling the effects of different drug efflux pathways in the basal drug resistant situation of the lead cell model system, such as the human breast tumour (MCF-7) cell line in which verification studies using established drug resistant sublines [33] would be pursued. Importantly, the modelling approach developed here will permit the study of cell-to-cell heterogeneity, a feature accessible to single cell verification studies. It is suggested that such modelling approaches will be informative in the design of therapeutic regimens and provide insights into the development of drug resistance reversing agents.

<a id='e400a56c-d0c3-497a-b3a7-e36bbb801df4'></a>

## Acknowledgements
The authors gratefully acknowledge the support of the Engineering and Physical Sciences Research Council of the UK under grants GR/M11943 and GR/R70354, and the Association for International Cancer Research (AICR) for grant support (G.P.F. and P.J.S.).

<a id='9d676ebc-9070-4b75-8d4a-c2a228a88d1f'></a>

# Appendix A. Identifiability analysis

## A.1. Step 2

There are four model outputs so r = 4, and we can define the following smooth functions:

μ₁(x,p) = c₁(p)x = Lm,

μ₂(x,p) = c₂(p)x = Hm,

μ₃(x,p) = c₃(p)x = Lc + v₂Ln / 1 + v₂,

μ₄(x,p) = c₄(p)x = Hc / 1 + v₂.

<a id='6943fffe-438e-40a6-940e-a9cef711674c'></a>

Since $n = 5$ (number of state variables) only a single further function is needed. Rather than calculating all four functions $\phi_1, \dots, \phi_4$ we try the simplest candidate. The simplest function is $\phi_2$, but this fails the observability test since it is a function of $L_m$ and $H_m$ only, so its derivative will be dependent on the derivatives of $\mu_1$ and $\mu_2$. The next (expected) simplest function is

<a id='30a77142-e289-4270-9b7e-8014bf9dd5f8'></a>

$\phi_1(\mathbf{x}, \mathbf{p}) = \left(\frac{\partial \mu_1}{\partial L_m}(\mathbf{x}, \mathbf{p}), \dots, \frac{\partial \mu_1}{\partial L_n}(\mathbf{x}, \mathbf{p})\right)f(\mathbf{x}, \mathbf{p}) = -(k_{o,m} + k_i)L_m + k_{c,m}H_m + \frac{k_e L_c}{v_1}$

<a id='bad0ddcc-35f4-4df6-90c7-c7b9a0128418'></a>

which is used in the construction of a matrix **J** as follows:

<!-- PAGE BREAK -->

<a id='2e7ad6d1-bc4b-407f-9fa4-f1a431ac25a9'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='18e11d77-ef8f-4589-b187-e7603a90e2b7'></a>

211

<a id='4de3fee3-4e2f-476a-89ff-cf6d2c5daf6c'></a>

J =

$$\begin{pmatrix}
\frac{\partial \mu_1}{\partial L_m}(\mathbf{x}_0(\mathbf{p}),\mathbf{p}) & \cdots & \frac{\partial \mu_1}{\partial L_n}(\mathbf{x}_0(\mathbf{p}),\mathbf{p}) \\
\vdots & \ddots & \vdots \\
\frac{\partial \mu_4}{\partial L_m}(\mathbf{x}_0(\mathbf{p}),\mathbf{p}) & \cdots & \frac{\partial \mu_4}{\partial L_n}(\mathbf{x}_0(\mathbf{p}),\mathbf{p}) \\
\frac{\partial \phi_1}{\partial L_m}(\mathbf{x}_0(\mathbf{p}),\mathbf{p}) & \cdots & \frac{\partial \phi_1}{\partial L_n}(\mathbf{x}_0(\mathbf{p}),\mathbf{p})
\end{pmatrix}$$

<a id='3f310cac-3a14-4c54-a681-80cc173cab98'></a>

This matrix has non-zero determinant and so the model satisfies the observability criterion. We set
$\mu_5(\mathbf{x}, \mathbf{p}) = \phi_1(\mathbf{x}, \mathbf{p}).$

<a id='7345f03c-ede0-4efe-9b7b-3c5007be7a54'></a>

A.2. Step 3

<a id='7ea5fbc2-9e22-4b5e-baf9-db355b4ee886'></a>

For the next step in the identifiability analysis Eq. (4) is used to construct the function λ. It is seen that

λ₁(x) = Lm (A.1)

λ₂(x) = Hm (A.2)

λ₃(x) + v₂λ₅(x)
---
1 + v₂
= Lc + v₂Ln
---
1 + v₂ (A.3)

<a id='2feeaf2f-31da-4398-bf22-b6544489f8e5'></a>

$\frac{\lambda_4(\mathbf{x})}{1 + v_2} = \frac{H_c}{1 + \bar{v}_2}$ (A.4)

<a id='e21360cd-b70f-4c63-830b-02be799b1352'></a>

$$-(k_{o,m} + k_i)\lambda_1(\mathbf{x}) + k_{c,m}\lambda_2(\mathbf{x}) + \frac{k_e\lambda_3(\mathbf{x})}{v_1} = -(\bar{k}_{o,m} + \bar{k}_i)L_m + \bar{k}_{c,m}H_m + \frac{\bar{k}_e L_c}{\bar{v}_1}. \quad (A.5)$$

<a id='c3bee077-b13c-43a5-a16f-003a8dfa1c0a'></a>

Substituting Eqs. (A.1) and (A.2) into Eq. (A.5) gives, on rearranging,

$\lambda_3(\mathbf{x}) = \frac{v_1}{k_e} \left( \left[ (k_{o,m} + k_i) - (\bar{k}_{o,m} + \bar{k}_i) \right] L_m + (\bar{k}_{c,m} - k_{c,m}) H_m + \frac{\bar{k}_e L_c}{v_1} \right)$.

<a id='abaed06d-ba11-4471-9aed-a418d805281c'></a>

Rearranging Eq. (A.3) gives

$\lambda_5 (\mathbf{x}) = \frac{1}{v_2} \left( \left( \frac{1 + v_2}{1 + \bar{v}_2} \right) (L_c + \bar{v}_2 L_n) - \lambda_3 (\mathbf{x}) \right)$.

A.3. Step 4

<a id='32ebf066-e53a-466b-9bef-7dbcba2da3b0'></a>

The final step in the identifiability analysis is to determine the set _S_(_p_), comprising those parameter vectors _p_ for which _λ_ satisfies Eqs. (5) and (6). For Eq. (5) to be satisfied, it is necessary that

<!-- PAGE BREAK -->

<a id='da35e296-24e5-407e-97e2-b860c7efc99c'></a>

212

<a id='ef4086e1-1ec7-49a7-9276-6f64cee7233e'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='4fa2e9ee-c4ec-42d0-9cf8-05c89ae70393'></a>

\(\lambda(\mathbf{x}_0(\mathbf{p})) = \begin{pmatrix} D \\ 0 \\ \frac{v_1}{k_e} \left[ (k_{o,m} + k_i) - (\bar{k}_{o,m} + \bar{k}_i) \right] D \\ 0 \\ -\frac{v_1}{v_2 k_e} \left[ (k_{o,m} + k_i) - (\bar{k}_{o,m} + \bar{k}_i) \right] D \end{pmatrix} = \mathbf{x}_0(\mathbf{p}) = \begin{pmatrix} D \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}.\)

<a id='141ee382-e4f7-48b7-ae5b-f8233202d017'></a>

Therefore, since D ≠ 0,

$\bar{k}_{o,m} + \bar{k}_i = k_{o,m} + k_i$ (A.6)

<a id='e538c379-9797-4ddb-8341-f93c67439ec2'></a>

It now only remains to consider Eq. (6) with λ defined by Eqs. (19)–(21). The components of Eq.
(6) will be considered separately.

<a id='c94eb879-54fa-46e5-a046-b6389af270a0'></a>

In the analysis of the third, fourth and fifth components of Eq. (6) it is necessary to solve equations involving the components of x(t,p). This is done by repeatedly differentiating the equation with respect to t and making use of the known initial condition (by setting t = 0 in the resulting equations). In order to greatly simplify this procedure, the following observations are made:

$L_m(0,\bar{p}) = D_r H_m(0,\bar{p}) = L_c(0,\bar{p}) = H_c(0,\bar{p}) = L_n(0,\bar{p}) = 0.$ (A.7)

<a id='26d0ea18-41a5-42d4-85a4-994ae248f4b5'></a>

Setting $t = 0$ in Eqs. (12)-(16) and using the above conditions (and Eq. (A.6)) gives

<a id='b64d35cc-f465-48a7-ba2a-616f89478bb2'></a>

$\dot{L}_m(0, \bar{p}) = -(k_{o,m} + k_i)D, \quad \dot{H}_m(0, \bar{p}) = \bar{k}_{o,m}D, \quad \dot{L}_c(0, \bar{p}) = (\bar{k}_i \bar{v}_1)D, \quad (A.8)$ 
$\dot{H}_c(0, \bar{p}) = \dot{L}_n(0, \bar{p}) = 0.$

<a id='6f973347-62e7-46cf-8265-87716389c546'></a>

A.3.1. First component of Eq. (6)
The first component follows directly from Eq. (4), with $i = 5$, since
$f_1(\lambda(\mathbf{x}(t,\bar{\mathbf{p}})),\mathbf{p}) = \mu_5(\lambda(\mathbf{x}(t,\bar{\mathbf{p}})),\mathbf{p})$

<a id='31f66a22-22e0-4dc8-8940-00b9dc8658d8'></a>

and

$\frac{\partial\lambda_1}{\partial\mathbf{x}}(\mathbf{x}(t,\bar{\mathbf{p}}),\bar{\mathbf{p}})\mathbf{f}(\mathbf{x}(t,\bar{\mathbf{p}}),\bar{\mathbf{p}}) = \mathbf{f}_1(\mathbf{x}(t,\bar{\mathbf{p}}),\bar{\mathbf{p}}) = \mu_5(\mathbf{x}(t,\bar{\mathbf{p}}),\bar{\mathbf{p}}).$

<a id='19bc1470-b11f-4c61-a8d5-86b02ccdf15a'></a>

A.3.2. Second component of Eq. (6)
For the second component to be satisfied, it is necessary and sufficient that
$k_{o,m}L_m(t,\bar{p}) - k_{c,m}H_m(t,\bar{p}) = \bar{k}_{o,m}L_m(t,\bar{p}) - \bar{k}_{c,m}H_m(t,\bar{p})$

<a id='765084c4-f6bb-4a75-a939-ddb835697ea4'></a>

for all $t \geq 0$. Setting $t = 0$ it is seen that $\overline{k_{o,m}} = k_{o,m}$ and so

<a id='c0c13817-0db9-4cde-b6fc-1beab11d1493'></a>

$$(\bar{k}_{c,m} - k_{c,m})H_m(t, \bar{p}) = 0$$

<a id='19b55121-f69c-40de-af13-6fc3b401c1ad'></a>

for all $t \geq 0$. Since $H_m(t, \bar{p})$ is not identically zero, it must be true that $\bar{k}_{c,m} = k_{c,m}$. From these expressions and Eq. (A.6), it is seen that, for a parameter vector $\bar{p}$ to be in the set $\mathcal{S}(\mathbf{p})$, it is necessary that

<a id='f460bbd8-a16a-4810-acf0-514d167d4362'></a>

$$\bar{k}_{o,m} = k_{o,m}, \quad \bar{k}_{c,m} = k_{c,m}, \quad \bar{k}_{i} = k_{i}. \quad \quad (A.9)$$

<!-- PAGE BREAK -->

<a id='9ca32fb2-7fa2-42fa-bfa1-95ef3cd07d46'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217                                                                                                        213

<a id='49f83bfe-4d98-47d8-ac87-118842e94aa7'></a>

Substituting these conditions into Eqs. (20) and (21) it is seen that λ satisfies

$\lambda(x) = \left( L_m, H_m, \frac{v_1 \bar{k}_e}{\bar{v}_1 k_e} L_c, \frac{1+v_2}{1+\bar{v}_2} H_c, \frac{1}{v_2} \left[ \frac{1+v_2}{1+\bar{v}_2} (L_c + \bar{v}_2 L_n) - \frac{v_1 \bar{k}_e}{\bar{v}_1 k_e} L_c \right] \right)^T$.
(A.10)

<a id='22f912fd-70f3-48c5-bd91-db02007a83ae'></a>

A.3.3. Fourth component of Eq. (6)
The fourth component appears to be simplest in form of the remaining three components and so is treated first. Comparing the fourth components of both sides of Eq. (6), it is seen that

$k_{o,c}\left(\frac{v_1\bar{k}_e}{\bar{v}_1k_e}\right)L_c(t,\bar{p}) - k_{c,c}\left(\frac{1+v_2}{1+\bar{v}_2}\right)H_c(t,\bar{p}) = \left(0,0,0,\frac{1+v_2}{1+\bar{v}_2},0\right)f(\mathbf{x}(t),\bar{p})$

$= \frac{1+v_2}{1+\bar{v}_2}\left(\bar{k}_{o,c}L_c(t,\bar{p}) - \bar{k}_{c,c}H_c(t,\bar{p})\right).$

<a id='d59a9efc-cc4c-4b0b-b711-c9a18799dbe0'></a>

Rearranging and collecting terms together results in the following equation

$\left(k_{o,c}\left(\frac{v_1 \bar{k}_e}{\bar{v}_1 k_e}\right)(1+\bar{v}_2) - \bar{k}_{o,c}(1+v_2)\right)L_c(t,\bar{p}) + (1+v_2)(\bar{k}_{c,c} - k_{c,c})H_c(t,\bar{p}) = 0. \quad (A.11)$

<a id='105a0a43-cbdb-421c-80c8-44aef55aecfb'></a>

Differentiating this equation with respect to t and then setting t = 0, it is seen (using Eq. (A.8))
that

<a id='11ddd26f-0a3a-4dcf-9ce9-fb661f622dbe'></a>

$$\left(k_{o,c}\left(\frac{v_1\bar{k}_e}{\bar{v}_1k_e}\right)(1+\bar{v}_2) - \bar{k}_{o,c}(1+v_2)\right)(\bar{k}_i\bar{v}_1)D = 0.$$

<a id='b4218c6d-c273-431d-8a37-d529a92a6a89'></a>

Therefore

<a id='b92d4cc8-48d2-4fa9-bc52-88475e096260'></a>

$$\bar{k}_{o,c} = k_{o,c} \left( \frac{v_1 \bar{k}_e (1 + \bar{v}_2)}{v_1 k_e (1 + v_2)} \right) \quad (A.12)$$

<a id='7a25faec-31a6-4f16-8c2c-c5232bd38384'></a>

and so Eq. (A.11) reduces to

$(1 + v_2)(\bar{k}_{c,c} - k_{c,c})H_c(t,\bar{p}) = 0.$

<a id='c8d04036-c2eb-40d3-80cc-30111e0eb9ca'></a>

Since $H_c(t, \mathbf{p})$ is not identically zero, it must be the case that

$\bar{k}_{c,c} = k_{c,c}$

(A.13)

<a id='2dfff189-f0e9-4679-ac00-215af6951e0f'></a>

Substituting the conditions given in Eqs. (A.12) and (A.13) into Eq. (A.11) shows that these conditions are sufficient for λ to satisfy the fourth component of Eq. (6).

<a id='6902fbf9-776f-4ba3-83ab-8086ee2bc7ed'></a>

From Eqs. (A.9), (A.12) and (A.13), it is seen that, for a parameter vector p to be in the set S(p), it is necessary that

<a id='2b7b84ce-7c9e-4399-8aff-f5717b2f77d8'></a>

$$\bar{k}_{o,m} = k_{o,m}, \quad \bar{k}_{c,m} = k_{c,m}, \quad \bar{k}_i = k_i, \quad \bar{k}_{c,c} = k_{c,c}, \quad \frac{k_{o,c}\bar{v}_1}{k_e(1+\bar{v}_2)} = \frac{k_{o,c}v_1}{k_e(1+v_2)}. \quad (A.14)$$

<a id='ab5c66be-2355-4b8b-b2e3-335b0fc844ea'></a>

The form of the function $\lambda$ reduces to

$\lambda(x) = \left(L_m, H_m, \frac{v_1\bar{k}_e}{\bar{v}_1\bar{k}_e}L_c, \frac{1+v_2}{1+\bar{v}_2}H_c, \alpha\left(\left(1-\frac{\bar{k}_{o,c}}{k_{o,c}}\right)L_c + \bar{v}_2L_n\right)\right)^T$ (A.15)

where $\alpha = (1 + v_2)/(\bar{v}_2(1+\bar{v}_2))$.

<!-- PAGE BREAK -->

<a id='c32125a7-8242-4b82-87ae-4c8184f9e445'></a>

214 N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='4207194c-abe2-48ae-93da-2f191b2378bf'></a>

A.3.4. *Fifth component of Eq. (6)*
The fifth component appears to be the next simplest of the remaining two components and so is treated next. To simplify subsequent analysis, it is helpful to set *t* = 0 in the fifth component of Eq. (6). By doing so, it is seen that

<a id='cf6cc140-0712-471e-b477-01b55acbbaa4'></a>

```latex
0 = \left(0, 0, \alpha\left(1 - \frac{\bar{k}_{o,c}}{k_{o,c}}\right), 0, \alpha\bar{v}_2\right) \begin{pmatrix} -(k_{o,m} + k_i)D \\ k_{o,m}D \\ k_i\bar{v}_1D \\ 0 \\ 0 \end{pmatrix} = \alpha\left(1 - \frac{\bar{k}_{o,c}}{k_{o,c}}\right)k_i\bar{v}_1D
```

<a id='56bc5d4b-f29c-47d0-b076-669b6504cf36'></a>

and so

$\bar{k}_{o,c} = k_{o,c}.$ (A.16)

<a id='365f3362-403d-4791-bea0-7e61822943f0'></a>

This implies that the fifth component of λ(x) is given by λ₅(x) = ᾱv₂L_n. Now, comparing the fifth components of both sides of Eq. (6), it is seen, using Eqs. (A.14) and (A.16), that

<a id='8a619def-80e3-4e59-b2c0-53fa3ca96ccb'></a>

$$\left(\frac{k_b}{v_2}\right) \left(B_T - \alpha\bar{v}_2 L_n(t, \bar{p})\right) \frac{v_1\bar{k}_e}{\bar{v}_1 k_e} L_c(t, \bar{p}) - k_d\alpha\bar{v}_2 L_n(t, \bar{p})$$
$$= \alpha\bar{v}_2 \left( \left( \frac{\bar{k}_b}{\bar{v}_2} \right) (\bar{B}_T - L_n(t, \bar{p})) L_c(t, \bar{p}) - \bar{k}_d L_n(t, \bar{p}) \right).$$

<a id='c8beed5d-36c1-469a-bbb7-a31bf698d009'></a>

Note that (v₁k̄ₑ)/(v̄₁kₑ) = αv₂ and α ≠ 0. Therefore, both sides of the equation can be divided through by α. Rearranging and collecting terms together results in the following equation

<a id='17ed6984-e3b2-4d69-a1b6-c25fe4a50dbf'></a>

$$(k_b B_T - \bar{k_b} \bar{B_T}) L_c(t, \bar{p}) + (\bar{k_b} - k_b \alpha \bar{v_2}) L_c(t, \bar{p}) L_n(t, \bar{p}) + \bar{v_2} (\bar{k_d} - k_d) L_n(t, \bar{p}) = 0. \quad (A.17)$$

<a id='6f158572-4ee6-403c-854f-545bfcb1b8ca'></a>

Differentiating this equation with respect to _t_ and then setting _t_ = 0, it is seen (using Eqs. (A.7)
and (A.8)) that

<a id='6faf52de-9746-4c03-bf5e-fa11ddf5d03b'></a>

(k_b B_T - \overline{k_b B_T})k_i \overline{v_1} D = 0

<a id='070d463f-f140-47ce-9803-a290b5792be2'></a>

and so

$\bar{k}_b\bar{B}_T = k_bB_T$.

(A.18)

<a id='81867c66-8bae-478a-8350-a1d8241840f5'></a>

Therefore, Eq. (A.17) reduces to

$[(k̄_b - k_b\alpha v̄_2)L_c(t,p̄) + v̄_2(k̄_d - k_d)]L_n(t,p̄) = 0.$

<a id='d6057bbb-7a07-4b10-8302-b611f7bf7563'></a>

Since $L_n(t, \bar{p})$ is not identically zero, this means that

$(\bar{k}_b - k_b \alpha \bar{v}_2) L_c(t, \bar{p}) + \bar{v}_2 (\bar{k}_d - k_a) = 0$

<a id='1868fbcf-322a-438a-b48a-3b8720bcb68e'></a>

on some interval for $t$. Similarly, $L_c(t,\bar{p})$ is not constant (i.e., $\dot{L}_c(t,\bar{p})$ is non-zero) and so

$(k_b - k_b\alpha\bar{v}_2) = \bar{v}_2(\bar{k}_d - k_d) = 0.

<!-- PAGE BREAK -->

<a id='daab6d98-2ebe-43f4-94aa-fc5da75597f3'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217                                                                                   215

<a id='dbe6e0ac-341f-4ca0-b59d-8297acea44b1'></a>

This equation implies that

$\bar{k}_d = k_d$

(A.19)

<a id='96d593d6-29c6-4b91-8bf6-b83c75691b8f'></a>

and
$\frac{\bar{k}_b}{\bar{v}_2} = k_b\chi = \frac{k_b\bar{k}_e v_1}{v_2 k_e v_1}$. (A.20)

<a id='3608e982-4bae-448e-8e44-1b4ffc00f1bb'></a>

Conditions Eqs. (A.16), (A.18), (A.19), (A.20) are required for the fifth component of Eq. (6) to be satisfied. Putting these conditions together with those in Eq. (A.14) shows that, for a parameter vector **p** to be in the set $\mathcal{S}(\mathbf{p})$, it is necessary that

<a id='7f32334b-2e6d-4ba7-842e-985cd5630b79'></a>

$$\bar{k}_{o,m} = k_{o,m},\quad \bar{k}_{c,m} = k_{c,m},\quad \bar{k}_i = k_i,\quad \bar{k}_{o,c} = k_{o,c},\quad \bar{k}_{c,c} = k_{c,c},\quad \bar{k}_d = k_d,$$ 
$$\frac{\bar{v}_1}{\bar{k}_e(1 + \bar{v}_2)} = \frac{v_1}{k_e(1 + v_2)},\quad \bar{k}_b B_T = k_b B_T,\quad \frac{\bar{k}_b \bar{v}_1}{\bar{v}_2 \bar{k}_e} = \frac{k_b v_1}{v_2 k_e}. \quad (A.21)$$

<a id='d63ad078-c7ff-4b4b-984c-b11beaccabc1'></a>

The function $\lambda$ further reduces in form to
$\lambda(\mathbf{x}) = (L_m, H_m, (\alpha\bar{v}_2)L_c, (\alpha\bar{v}_2)H_c, (\alpha\bar{v}_2)L_n)^T$,
where $\alpha = (1 + \bar{v}_2)/(v_2(1 + \bar{v}_2)) = v_1\bar{k}_e/(v_2k_e\bar{v}_1)$.

(A.22)

<a id='6bcc9790-8ea3-4e91-8cd3-2cd2d72f6a24'></a>

A.3.5. Third component of Eq. (6)
All that remains is to consider the third component. To simplify subsequent analysis, it is helpful to set $t = 0$ in the third component of Eq. (6). By doing so, it is seen that

$k_i v_1 D = (0, 0, \alpha v_2, 0, 0) \begin{pmatrix} -(k_{o,m} + k_i)D \\ k_{o,m}D \\ k_i \bar{v}_1 D \\ 0 \\ 0 \end{pmatrix} = \alpha v_2 k_i \bar{v}_1 D.$

<a id='392fe669-a868-42ab-9b3d-8782de63bd9d'></a>

Therefore,

$\bar{v}_1 = \frac{v_1}{\alpha v_2} = \frac{\bar{v}_1 k_e}{k_e}$ (A.23)

and thus

$\bar{k}_e = k_e.$ (A.24)

<a id='edfaa24f-86a6-43f2-815a-8a3c5712b6c0'></a>

Comparing the third components of both sides of Eq. (6) and using the above conditions, it is seen that

<a id='212b8f23-9928-4278-83a5-7fd38c2cfe9c'></a>

(k_i v_1)L_m(t, \mathbf{p}) - (k_e + k_{o,c})(\alpha v_2)L_c(t, \mathbf{p}) + k_{c,c}(\alpha v_2)H_c(t, \mathbf{p}) - k_b(B_T - (\alpha \bar{v}_2)L_n(t, \mathbf{p}))(\alpha v_2)L_c(t, \mathbf{p})
+ v_2 k_d(\alpha \bar{v}_2)L_n(t, \mathbf{p})
= \alpha v_2(((k_i \bar{v}_1)L_m(t, \mathbf{p}) - (k_e + k_{o,c})L_c(t, \mathbf{p}) + k_{c,c}H_c(t, \mathbf{p}) - k_b(B_T - L_n(t, \mathbf{p}))L_c(t, \mathbf{p})
+ \bar{v}_2 k_d L_n(t, \mathbf{p}))).

<a id='82d227b3-f48b-4076-a300-d58e362d8b32'></a>

Rearranging and collecting terms results in the following equation (using Eq. (A.23))

$(k_b \alpha \bar{v}_2 - \bar{k}_b)L_c(t, \bar{p})L_n(t, \bar{p}) = 0.$ (A.25)

<!-- PAGE BREAK -->

<a id='44e1b987-1316-41d0-9ca6-1b5af540a66c'></a>

216

<a id='94831dc5-10d9-4034-bd35-1c9deacdc754'></a>

N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217

<a id='a7c33e3d-81d4-4a80-8e1e-da1e2ef2e148'></a>

From Eq. (A.20), it is seen that this equation is automatically satisfied so the third component of Eq. (6), is satisfied.

<a id='d246a7cd-44da-41db-9ca0-7da9baf2dc5a'></a>

Therefore conditions Eqs. (A.23) and (A.24) are required for the third component of Eq. (6) to be satisfied. Putting these conditions together with those in Eq. (A.14) shows that a parameter vector p in the set S(p) satisfies

<a id='2b09364b-ad70-4bd3-acf7-ad260b706e78'></a>

k̄_o,m = k_o,m, k̄_c,m = k_c,m, k̄_i = k_i, k̄_e = k_e, k̄_o,c = k_o,c, k̄_c,c = k_c,c, k̄_d = k_d,
v̄_1 / (1 + v̄_2) = v_1 / (1 + v_2), k̄_b B̄_T = k_b B_T, k̄_b v̄_1 / v̄_2 = k_b v_1 / v_2.

<a id='888fdebe-4e74-41ae-b1d0-1ec0c3db5773'></a>

The function $\lambda$ satisfies

$\lambda(x) = \left( L_m, H_m, \frac{v_1}{v_1}L_c, \frac{v_1}{v_1}H_c, \frac{v_1 \bar{v}_2}{\bar{v}_1 v_2}L_n \right)^{\text{T}}$

(A.26)

<a id='667f257e-77a3-42a2-aa58-53636fa1bbbc'></a>

# References

1. K.R. Godfrey, Compartmental Models and their Application, Academic Press, London, 1983.
2. J.A. Jacquez, Compartmental Analysis in Biology and Medicine, 3rd Ed., BioMedware, Ann Arbor, MI, 1996.
3. C. Bailly, Topoisomerase I poisons and suppressors as anticancer drugs, Curr. Medic. Chem. 7 (2000) 39.
4. J. O'Leary, F.M. Muggia, Camptothecins: a review of their development and schedules of administration, Europ. J. Cancer 34 (10) (1998) 1500.
5. Y.H. Hsiang, L.F. Lui, Identification of mammalian DNA topoisomerase-I as an intracellular target of the anticancer drug camptothecin, Cancer Res. 48 (7) (1988) 1722.
6. R. Garcia-Carbonero, J.G. Supko, Current perspectives on the clinical experience, pharmacology and continued development of the camptothecins, Clinic. Cancer Res. 8 (3) (2002) 641.
7. E. Jonsson, H. Fridborg, K. Csoka, S. Dhar, C. Sundstrom, P. Nygren, R. Larsson, Cytotoxic activity of topotecan in human tumour cell lines and primary cultures of human tumour cells from patients, Br. J. Cancer 76 (2) (1997) 211.
8. D. Ormrod, C.M. Spencer, Topotecan: a review of its efficacy in small cell lung cancer, Drugs 58 (3) (1999) 533.
9. J.C. Wang, DNA topoisomerases, Ann. Rev. Biochem. 65 (1996) 635.
10. K.W. Kohn, R.G. Shao, Y. Pommier, How do drug-induced topoisomerase I-DNA lesions signal to the molecular interaction network that regulates cell cycle checkpoints, DNA replication, and DNA repair?, Cell Biochem. Biophys. 33 (2) (2000) 175.
11. I. Gryczynski, Z. Gryczynski, J.R. Lakowicz, D.Z. Yang, T.G. Burke, Fluorescence spectral properties of the anticancer drug topotecan by steady-state and frequency domain fluorometry with one-photon and multi-photon excitation, Photochem. Photobiol. 69 (4) (1999) 421.
12. S. Yao, D. Murali, P. Seetharamulu, K. Haridas, P.N.V. Petluru, D.G. Reddy, F.H. Hausheer, Topotecan lactone selectively binds to double- and single-stranded DNA in the absence of topoisomerase I, Cancer Res. 58 (17) (1998) 3782.
13. B. Tan, D. Piwnica-Worms, L. Ratner, Multidrug resistance transporters and modulation, Curr. Opinion Oncol. 12 (5) (2000) 450.
14. C.B. Hendricks, E.K. Rowinsky, L.B. Grochow, R.C. Donehower, S.H. Kaufmann, Effect of P-glycoprotein expression on the accumulation and cytotoxicity of topotecan (SK&F 104864), a new camptothecin analog, Cancer Res. 52 (8) (1992) 2268.
15. E. Rocchi, A. Khodjakov, E.L. Volk, C.H. Yang, T. Litman, S.E. Bates, E. Schneider, The product of the ABC half-transporter gene ABCG2 (BCRP/MXR/ABCP) is expressed in the plasma membrane, Biochem. Biophys. Res. Comm. 271 (1) (2000) 42.

<!-- PAGE BREAK -->

<a id='42c3764a-a994-47ae-96d2-c7de59e81ca9'></a>

*N.D. Evans et al. / Mathematical Biosciences 189 (2004) 185–217*

<a id='6b3d11c4-59e1-4ed1-93b1-2ce245cc6aa2'></a>

217

<a id='e91a7289-c3d1-49a8-98c6-9ca1340d27da'></a>

[16] T. Litman, M. Brangi, E. Hudson, P. Fetsch, A. Abati, D.D. Ross, K. Miyake, J.H. Resau, S.E. Bates, The multidrug-resistant phenotype associated with overexpression of the new ABC half-transporter, MXR (ABCG2), J. Cell Sci. 113 (11) (2000) 2011.
[17] R. Bellman, K.J. Aström, On structural identifiability, Math. Biosci. 7 (1970) 329.
[18] K.R. Godfrey, J.J. DiStefano III, Identifiability of model parameters, in: E. Walter (Ed.), Identifiability of Parametric Models, Pergamon, Oxford, 1987, p. 1 (Chapter 1).
[19] E. Walter, Identifiability of State Space Models, Springer, Berlin, 1982.
[20] H. Pohjanpalo, System identifiability based on the power series expansion of the solution, Math. Biosci. 41 (1978) 21.
[21] E.T. Tunali, T.J. Tarn, New results for identifiability of nonlinear systems, IEEE Trans. Automat. Control 32 (1987) 146.
[22] S. Vajda, K.R. Godfrey, H. Rabitz, Similarity transformation approach to identifiability analysis of non-linear compartmental models, Math. Biosci. 93 (1989) 217.
[23] N.D. Evans, M.J. Chapman, M.J. Chappell, K.R. Godfrey, Identifiability of uncontrolled nonlinear rational systems, Automatica 38 (2002) 1799.
[24] N.D. Evans, M.J. Chappell, M.J. Chapman, K.R. Godfrey, The structural identifiability of a general epidemic (SIR) model with seasonal forcing, In: Proceedings of the Fifteenth IFAC World Congress, Barcelona, Spain, 21-26 July 2002. Paper T-Mo-A20.2.
[25] R. Hermann, A.J. Krener, Nonlinear controllability and observability, IEEE Trans. Automat. Control AC-22 (3) (1977) 728.
[26] AEA Technology. Facsimile (Version 4.0) User Guide. Harwell Laboratory, Didcot, Oxfordshire, UK, 1995.
[27] J.A. Jacquez, Modeling With Compartments, BioMedware, Ann Arbor, MI, 1999.
[28] M.J. Chappell, G.D. Thomas, K.R. Godfrey, A.R. Bradwell, Optimal tumor targeting by antibodies: Development of a mathematical model, J. Pharmacokin. Biopharm. 19 (1991) 227.
[29] I. Chourpa, J.M. Millot, G.D. Sockalingum, J.F. Riou, M. Manfait, Kinetics of lactone hydrolysis in antitumor drugs of camptothecin series as studied by fluorescence spectroscopy, Biochim. Biophys. Acta 1379 (3) (1998) 353.
[30] AEA Technology. Facsimile (Version 4.0) Technical Reference. Harwell Laboratory, Didcot, Oxfordshire, UK, 1995.
[31] W.J. Loos, G. Stoter, J. Verweij, J.H.M. Schellens, Sensitive high-performance liquid chromatographic fluorescence assay for the quantitation of topotecan (SKF 104864-a) and its lactone ring-opened product (hydroxy acid) in human plasma and urine, J. Chromatogr. B 678 (1996) 309.
[32] G.M. Clarke, D. Cooke, A Basic Course in Statistics, 4th Ed., Arnold, London, 1998.
[33] M. Brangi, T. Litman, M. Ciotti, K. Nishiyama, G. Kohlhagen, C. Takimoto, R. Robey, Y. Pommier, T. Fojo, S.E. Bates, Camptothecin resistance: Role of the ATP-binding cassette (ABC), mitoxantrone-resistance half-transporter (MXR), and potential for glucuronidation in MXR-expressing cells, Cancer Res. 59 (23) (1999) 5938.
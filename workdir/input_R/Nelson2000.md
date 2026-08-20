<a id='c2277d27-5ab5-493f-9f9a-bbfee16d2b7e'></a>

<::logo: Elsevier
ELSEVIER
The logo features a tree with a figure on each side, and a serpent wrapped around the tree.
::>

<a id='60dac55b-e4b6-46f3-b42e-0efa1faddd38'></a>

<::logo: Mathematical Biosciences
Mathematical Biosciences
The logo features the words "Mathematical Biosciences" in bold, italicized black text, centered between a double line above and a single line below.::>

<a id='a2d1bff3-9601-46cf-a412-fdc863becac6'></a>

Mathematical Biosciences 163 (2000) 201–215

<a id='11125d02-9724-42ac-bef1-7a279dade8cc'></a>

www.elsevier.com/locate/mbs

<a id='d12ed66a-e51c-49f7-8f90-acdca05e658b'></a>

A model of HIV-1 pathogenesis that includes an intracellular delay

<a id='727a17b2-7ced-4cac-a08e-880c9a576932'></a>

Patrick W. Nelson a,b, James D. Murray c, Alan S. Perelson b,*
a Department of Mathematics, Duke University, Durham, NC 27708, USA
b Theoretical Biology and Biophysics Group, Los Alamos National Laboratory, Mail Stop K710, Los Alamos, NM 87545, USA
c Department of Applied Mathematics, University of Washington, Seattle, WA 98195, USA
Received 20 July 1999; received in revised form 14 October 1999; accepted 18 October 1999

<a id='cda52703-9a8b-48ba-811a-0f072188ae10'></a>

## Abstract
Mathematical modeling combined with experimental measurements have yielded important insights into HIV-1 pathogenesis. For example, data from experiments in which HIV-infected patients are given potent antiretroviral drugs that perturb the infection process have been used to estimate kinetic parameters underlying HIV infection. Many of the models used to analyze data have assumed drug treatments to be completely efficacious and that upon infection a cell instantly begins producing virus. We consider a model that allows for less then perfect drug effects and which includes a delay in the initiation of virus production. We present detailed analysis of this delay differential equation model and compare the results to a model without delay. Our analysis shows that when drug efficacy is less than 100%, as may be the case in vivo, the predicted rate of decline in plasma virus concentration depends on three factors: the death rate of virus producing cells, the efficacy of therapy, and the length of the delay. Thus, previous estimates of infected cell loss rates can be improved upon by considering more realistic models of viral infection. © 2000 Elsevier Science Inc. All rights reserved.

<a id='d7e1e379-f5c8-4bcd-a038-41ca1d380674'></a>

Keywords: HIV; Delay; Viral life cycle; T-cells

<a id='96c4fb59-deba-4058-aa66-74ea9057d105'></a>

1. Introduction

In recent years, clinical research combined with mathematical modeling has enhanced progress in the understanding of HIV-1 infection. The introduction of a new class of drugs, protease

<a id='845903cd-fcac-44e3-bc8a-d1ee6b39a279'></a>

* Corresponding author. Tel.: +1-505 667 6829; fax: +1-505 665 3493.
E-mail address: asp@receptor.lanl.gov (A.S. Perelson).

<a id='17714719-4aee-4edb-bc69-d3ae6587fab5'></a>

0025-5564/00/$ - see front matter  2000 Elsevier Science Inc. All rights reserved.
PII: S0025-5564(99)00055-3

<!-- PAGE BREAK -->

<a id='56f0b48e-5fdf-4e9f-af85-5f97325dbb5f'></a>

202

<a id='e4ca33b3-28cb-43ca-a7a4-95d765b78313'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='963e07ff-80c5-4ada-be49-bbf9afbe3a2b'></a>

inhibitors, used in combination with previously approved drugs such as zidovudine (AZT) and lamivudine (3TC) has shown much promise in reducing the detectable levels of viral RNA in the plasma. The introduction of these potent antiviral agents has opened the door to defining kinetic parameters associated with HIV-1 dynamics in infected individuals. Using mathematical models to interpret clinical data from HIV-1 infected patients treated with these potent antiviral agents has led to an estimate of the half-life of productively infected cells of 1.6 days or less and of the clearance rate of free virions from the plasma of six hours or less [1-3]. These initial estimates were claimed to be minimal estimates because the models used to analyze the patient data assumed the drug was completely effective. Refining these estimates will improve our quantitative description of viral dynamics and our understanding of the speed at which drug resistance emerges. Also, the dynamics of the models assumed that cells upon infection instantly begin producing virus. Both the assumption of 100% drug efficacy and of instantaneous production of virus upon infection are relaxed in this paper.

<a id='6fbf1617-61fb-46a1-a404-5e17bed36cc1'></a>

Ho et al. [4] and Wei et al. [3] developed models that were applied to data from an experiment where patients received an antiretroviral drug. Before drug therapy was initiated the patients were determined to have a quasi steady state concentration of virus in their plasma, suggesting that the rate of viral production equaled the rate of virus clearance. After administration of the drug, blood samples were taken for several days and plasma viral RNA levels were measured. The results showed that when virus production was interfered with by drugs the virus declined approximately exponentially. The data, when analyzed in the context of the model, allowed an estimate to be made of the quasi-steady state rate of viral production. The estimated production level was much higher then previously thought and provided an explanation for the ease by which HIV could mutate and escape therapy when only a single drug was used. Extensions of this work showed that after drug is applied there is a delay before virus begins to decline [1]. This delay is due to pharmacological events, the mechanism of protease inhibitor action that allows pre-existing virus particles to continue infecting cells and delays in the process of producing virus particles [1,5,6]. The viral decline is at first very rapid and then after about two weeks slows [2]. Thus there is a rapid first phase followed by a slower second phase of viral decline. Analysis of the data in the context of models showed that the viral decline during the first, rapid, phase could be used to estimate both c, the virus clearance rate constant and δ, the decay rate of productively infected T-cells [1]. In the model, the asymptotic rate of the exponential decline of virus concentration is e<sup>-δt</sup>. In order to get this result, it was assumed the drug was completely effective and that the virus clearance rate constant, c, was much larger than δ, and therefore associated with processes that decayed more quickly and consequently could be ignored after a brief initial period. It was later shown [7] that if the drug or combination of drugs was less then perfect, the exponential decline of the first phase could be represented by e<sup>-δnct</sup> where n<sub>c</sub> is the effectiveness of the drug combination with a value of one for complete efficacy and zero for no effect. In this paper we study the changes in these approximations when a constant delay is introduced in the model and the drug, a protease inhibitor, is assumed to have variable efficacy. Four models have been developed that attempt to generalize the early models by Wei et al. [3] and Perelson et al. [1] by including delays [5,6,8,9]. Grossman et al. [8] assume that infected cells die after a delay, given by a gamma distribution, and allow drugs to be partially effective. Tam [9] assumes that infected cells produce virus after a fixed delay and shows that including this delay does not affect the stability properties of infected steady state of the model for reasonable parameter values. The

<!-- PAGE BREAK -->

<a id='e3106ff5-066a-4f15-ac34-11f289ba4f7c'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='c2882ac4-5a82-4906-8050-528711b2a0c8'></a>

203

<a id='746e7378-3ae6-4047-9e41-234d9640b9f4'></a>

effects of drug therapy are not studied. Herz et al. [5] examined the effect of including a constant delay in the source term for productively infected T-cells but their analysis was limited to the case where the drug treatment was assumed completely effective. Mittler et al. [6] also assumed that there was a delay between initial infection and the start of virus production, a period that virologists call the *eclipse phase* of the viral life cycle, but rather than using a fixed delay they assumed that the delay varied between cells according to a gamma distribution. They used this model to examine if the parameters that characterize viral dynamics could be identified from biological data and then compared the parameter estimates obtained in a previous model without delay and those obtained with their delay model [10]. These works extended the ability of models to describe the relevant biological processes and addressed the implications of ignoring the intracellular delays that are part of the viral life cycle. In the models of Herz et al. [5] and Mittler et al. [6], the drug was assumed to completely block viral production. This assumption, we will show, cancels out the effect the intracellular delay has on the decay rate of virus producing T-cells. Hence, while noticing a change in viral dynamics during the eclipse phase, it was assumed the delay had no effect during the first phase's exponential decline. This paper's main focus is to examine the change in dynamics when a delay of discrete type is considered and the drug, a protease inhibitor, is assumed less then perfect. We have already shown [6,11] that when fitting a model to experimental data there are significant changes in the values of the infected T-cell loss rate and the viral clearance rate constant if the model includes a delay. Here, we derive a new approximation, $e^{-\delta n_p C(\tau, n_p, \delta)t}$, for the asymptotic first-phase viral decay when a constant intracellular delay $\tau$ is considered and protease inhibitor treatment is applied. Here the new factor is $C(\tau, n_p, \delta) = [1 + (1 - n_p)\delta\tau]^{-1}$, where $n_p$ is the effectiveness of the protease inhibitor. We provide a detailed analytical study of the model equations and examine the effects of adding a delay on the stability of solutions, something that was neglected in the analysis of previous delay models (see Table 1).

<a id='e20b4d32-18df-4ee4-8c0e-6947fb5050dd'></a>

Table 1
List of variables and parametersª
<table id="2-1">
<tr><td id="2-2"></td><td id="2-3">Definition</td><td id="2-4">Mean/Initial value</td><td id="2-5">Source</td></tr>
<tr><td id="2-6">Variable</td><td id="2-7"></td><td id="2-8"></td><td id="2-9"></td></tr>
<tr><td id="2-a">T(t)</td><td id="2-b">Uninfected T-cells</td><td id="2-c">180 cells/mm³</td><td id="2-d">[4]</td></tr>
<tr><td id="2-e">T*(t)</td><td id="2-f">Productively infected T-cells</td><td id="2-g">~ 2 % T-cells</td><td id="2-h">[4]</td></tr>
<tr><td id="2-i">V₁(t)</td><td id="2-j">Infectious virus</td><td id="2-k">134 × 10³ virions/ml</td><td id="2-l">[4]</td></tr>
<tr><td id="2-m">V_{NI}(t)</td><td id="2-n">Non-infectious virus</td><td id="2-o">0 virions/ml</td><td id="2-p">[4]</td></tr>
<tr><td id="2-q">n_p(t)</td><td id="2-r">Protease inhibitor efficacy</td><td id="2-s">(0,1)</td><td id="2-t">Variable</td></tr>
<tr><td id="2-u">Parameter</td><td id="2-v"></td><td id="2-w"></td><td id="2-x"></td></tr>
<tr><td id="2-y">λ</td><td id="2-z">T-cell source term</td><td id="2-A">0 – 10 cells/mm³</td><td id="2-B">[30]</td></tr>
<tr><td id="2-C">δ_I</td><td id="2-D">Death rate of target T-cells</td><td id="2-E">0.03/day</td><td id="2-F">[31]</td></tr>
<tr><td id="2-G">k</td><td id="2-H">Viral infectivity rate</td><td id="2-I">3.43 × 10⁻⁵ ml/virions/day</td><td id="2-J">[4]</td></tr>
<tr><td id="2-K">δ</td><td id="2-L">Death rate of an infected T-cell</td><td id="2-M">0.5/day</td><td id="2-N">[1]</td></tr>
<tr><td id="2-O">N</td><td id="2-P">Bursting term for viral production after lysis</td><td id="2-Q">480 virions/cell</td><td id="2-R">[1]</td></tr>
<tr><td id="2-S">c</td><td id="2-T">Clearance rate of virus</td><td id="2-U">3/day</td><td id="2-V">[1]</td></tr>
</table>

<a id='7a8761fe-4c1e-46da-9774-16d7e021e865'></a>

ª The parameter values used in generating the figures shown later in the paper are given and the references from which they were derived. The values for c and δ are the published estimates obtained from applying non-delay models to data from drug perturbation experiments.

<!-- PAGE BREAK -->

<a id='be5f3ca2-ab2f-4d26-8ded-bfba1ce220b2'></a>

204

<a id='2b326fb8-4ad0-425e-928e-b2a707130873'></a>

P.W. Nelson et al. / *Mathematical Biosciences* 163 (2000) 201–215

<a id='44b9d675-2e67-4d37-8084-3bc0d0209ec0'></a>

## 2. General model
The models in this paper only deal with dynamics occurring after drug treatment. The models are not designed to examine the progression from time of infection until drug initiation [12,13]. The study of HIV-1 dynamics has focused on the use of a general set of model equations that keep track of different cell populations and virus. In one case the model has been linear [4], while in most cases the model includes non-linear effects [14-17]. In most cases the models, while trivial mathematically, have provided important results when fitted to experimental data [3,4]. Models have distinguished between infected and non-infected T-cells [1], included other populations of immune cells, such as macrophages [2], looked at variability in certain crucial parameters, such as the infectivity rate, _k_ [18], viral burst size, _N_, and included drug treatments [7,19,20]. The general form of the non-delay model includes compartments for the densities of uninfected T-cells, _T_, infected T-cells that are producing virus, _T_*, infectious virus, _V_I, and non-infectious virus (produced by the action of a protease inhibitor), _V_NI, and is written as

<a id='f5a0cd8d-6778-41ab-b0d1-52efb511f517'></a>

$\frac{dT}{dt} = \lambda - \delta_1 T - kV_I T$,

$\frac{dT^*}{dt} = kV_I T - \delta T^*$,

$\frac{dV_I}{dt} = (1 - n_p)N\delta T^* - cV_I$,

$\frac{dV_{NI}}{dt} = n_p N\delta T^* - cV_{NI}$,

(1)

<a id='a1b6dc66-c5a4-43df-803f-85ff6d725aa8'></a>

where T, T*, V_I and V_NI ∈ R⁺ and all the parameters are in R⁺. δ is the decay rate of virus producing T-cells, c is the viral clearance rate constant, and n_p represents the drug efficacy of a protease inhibitor. The system (1) models the dynamics of virus levels in the plasma during drug treatment. The term (1 – n_p) represents the level of leakiness of a protease inhibitor, a drug that inhibits the cleaving of viral polyproteins and renders newly produced virions non-infectious. Thus, if n_p = 1, the protease inhibitor is 100% effective and no infectious virus particles are produced. Analysis of (1) has shown that allowing T to vary dynamically has not yielded significantly different behavior in the total viral output, V = V_I + V_NI, over a period of a week or so [21,22]. Because of this, we will analyze a model in which T is held constant at the value T_0.

<a id='02133577-db06-43ca-8c20-38755be35f63'></a>

2.1. Approximation to dominant eigenvalue

The eigenvalues of (1) determine the rate of viral decline, after therapy is initiated. Assuming that the system is in steady state before therapy is initiated so that c = NkTo and that T = To, then the eigenvalues of the final three equations of (1) can be expressed as [22]

<a id='eb4f067b-6746-445b-b412-0fd34574ea5c'></a>

$\lambda_{1,2} = -\frac{\delta+c}{2} \pm \frac{1}{2}\sqrt{(\delta+c)^2 - 4n_p\delta c}, \lambda_3 = -c.$ (2)

<a id='b95951ec-1cc3-49c5-a170-bc6257a6e811'></a>

If one assumes that the viral clearance rate constant, c, is significantly larger then the decay rate of productively infected T-cells, δ, then the eigenvalue with the largest real part related can be estimated to first order by [7,22]

<!-- PAGE BREAK -->

<a id='563d089b-3923-4658-a976-c2b33bd9e4f6'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='ea389ee7-7210-4c74-a676-67d9aa6e4419'></a>

205

(3)

<a id='812c49c9-38dc-4a8e-a4c2-1442c54c6798'></a>

\u03bb\u2081 ~ -\u03b4n\u209a.

<a id='975936f3-d19e-472a-b34a-a9ed248005ff'></a>

This shows when therapy is less then perfect the first phase slope of viral decline is not simply the death rate, δ, of productively infected T-cells. Previously, the value of δ has been estimated from experimental data, assuming a completely effective drug [3,4]. Relaxing this assumption of a perfect drug will change the estimate of δ. However, as we show below, when the drug efficacy is not 100%, delays between the time of cell infection and viral production will also influence the estimate of δ because λ₁ now becomes λ₁ ~ -δnₚC(τ, nₚ, δ) where C(τ, nₚ, δ) is a new factor introduced by the delay.

<a id='4b7aed11-f907-4847-a75d-235f29d46b60'></a>

### 3. Intracellular delay model

In HIV-1 infection, the virus life cycle plays a crucial role in disease progression. The binding of a viral particle to a receptor on a target cell initiates a cascade of events that can ultimately lead to the target cell becoming productively infected, i.e. producing new virus. The previous model (1) assumed this process to occur instantaneously. In other words, it is assumed that as soon as virus contacts a target cell the cell begins producing virus. However, in reality there is a time delay between initial viral entry into a cell and subsequent viral production. Previous work has shown that this delay needs to be taken into account to accurately determine the half life of free virus from drug perturbation experiments, but if the drug is assumed to be completely efficacious, the delay does not affect the estimated rate of decay of viral producing T-cells [5,6,10]. Here we show that the delay does affect the estimated value for the infected T-cell loss rate when one assumes the drug is not completely effective.

<a id='f170d455-c792-432b-8d4d-467404decc2e'></a>

We incorporate the intracellular delay in the model given by (1) by assuming that the gener-
ation of virus producing cells at time t is due the infection of target cells at time t – τ, where τ is a
constant. As before, we assume uninfected T-cells remain constant, i.e., T = T₀. The equations
describing this model are then

<a id='4e86a9b8-cdca-4313-8048-b8bbe5d8e942'></a>

$$\frac{dT^*}{dt} = k T_0 V_I(t - \tau)e^{-m\tau} - \delta T^*$$

$$\frac{dV_I}{dt} = (1 - n_p)N \delta T^* - c V_I$$

$$\frac{dV_{NI}}{dt} = n_p N \delta T^* - c V_{NI} \quad (4)$$

<a id='04b27ca6-c262-4860-889f-e69a9049646d'></a>

where the term V_I(t - τ) allows for the time delay between contact and virus production and e^(-mτ)
allows for death of an infected T-cells before it becomes productively infected. The rate constant
for infection, k is assumed constant because the drug we are modeling, a protease inhibitor, does
not affect k. If a reverse transcriptase inhibitor were being used then the appropriate model would
have k in the dT*/dt equation replaced by k(t - τ). Notice the equation for V_NI(t) can be easily
solved once the solution for the first two equations is known. Analysis of a more general form of
this delay model, which included uninfected T-cells and non-linearities can be found in [21]. The
following sections will examine the model's characteristic equation. Our main focus is to provide
an expression for the dominant eigenvalue, i.e., the eigenvalue with the largest real part.

<!-- PAGE BREAK -->

<a id='0fec0867-03b2-42dd-99de-e95520715b07'></a>

206 P. W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='fa008556-459e-4dbe-aa94-34cadd1de652'></a>

3.1. Analysis of delay model

The model (4) in vector-matrix notation is

$\frac{dy(t)}{dt} = B_0y(t - \tau) + C_0y(t),$ (5)

<a id='53f7b7c8-6c6c-4af4-9cdf-70dc6a693640'></a>

where $\tau$ is a constant, $B_0$ and $C_0$ are $n \times n$ matrices defined as

$B_0 = \begin{pmatrix}
0 & kT_0e^{-m\tau} & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}$, $C_0 = \begin{pmatrix}
-\delta & 0 & 0 \\
(1-n_p)N\delta & -c & 0 \\
n_pN\delta & 0 & -c
\end{pmatrix}$

<a id='72a7d79b-0612-4624-ad20-2112760e4752'></a>

and

y(t) = 

<::transcription of the content
: figure::>

<p style="text-align: center;">
  <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
    <mi mathvariant="bold">y</mi>
    <mo stretchy="false">(</mo>
    <mi>t</mi>
    <mo stretchy="false">)</mo>
    <mo>=</mo>
    <mrow data-mjx-texclass="INNER" close=")" open="(">
      <mtable columnspacing="1em" rowspacing="4pt">
        <mtr>
          <mtd>
            <msup>
              <mi>T</mi>
              <mo>*</mo>
            </msup>
            <mo stretchy="false">(</mo>
            <mi>t</mi>
            <mo stretchy="false">)</mo>
          </mtd>
        </mtr>
        <mtr>
          <mtd>
            <msub>
              <mi>V</mi>
              <mi>I</mi>
            </msub>
            <mo stretchy="false">(</mo>
            <mi>t</mi>
            <mo stretchy="false">)</mo>
          </mtd>
        </mtr>
        <mtr>
          <mtd>
            <msub>
              <mi>V</mi>
              <mrow data-mjx-texclass="ORD">
                <mi>N</mi>
                <mi>I</mi>
              </mrow>
            </msub>
            <mo stretchy="false">(</mo>
            <mi>t</mi>
            <mo stretchy="false">)</mo>
          </mtd>
        </mtr>
      </mtable>
    </mrow>
    <mo>.</mo>
  </math>
</p>



<a id='aa7b0709-a219-4d43-a48e-322bdabdeeeb'></a>

The initial conditions, on the interval 0 ≤ t ≤ τ are defined as
y(t) = g(t),
                                                                        (6)

<a id='87d6cb99-4167-4d15-a910-4c31bfede7e2'></a>

where

$\mathbf{g}(t) = \begin{pmatrix} T_{ss} \\ V_{ss} \\ 0 \end{pmatrix}.$

<a id='70c3c20f-3d7d-47e2-8244-d823477ac509'></a>

Using the results in [23] it is easy to show that a system of the form (5), with initial conditions (6), has a unique solution which is continuous for t ≥ 0 and which satisfies (5) for t > τ.

<a id='54850534-b04c-44a3-8a3c-ef57b61b1038'></a>

3.1.1. Characteristic equation
Time delays when used in population dynamic models have been shown to create fluctuations in population size due to the generation of instabilities [24,25]. Here, we will show that the eigenvalues of the delay model remain in the left half plane for all values of the delay. With this being the case the dominant eigenvalue will then be the negative eigenvalue whose real part is closest to zero.

<a id='6a79365f-cc19-48b2-94a8-503c5c972485'></a>

Introducing a delay of discrete type in a system of differential equations changes the structure of the solution as determined by the characteristic equation. In the case when no delay is present a linear system of N differential equations will have N solutions and a characteristic polynomial of degree N. When a delay is included the characteristic equation is no longer a polynomial but rather takes the form (see [26])

<a id='c0db04ba-adcc-4f26-8514-d3773b42c003'></a>

H(̴) = G(̴) + K(̴)e^{-̴τ} = 0, (7)

<a id='31c95e46-c96c-45cb-a1fa-df001e7302c2'></a>

where G(λ) and K(λ) are polynomials and
P(λ) = G(λ) + K(λ) = 0,
(8)

<a id='af80ffae-20ce-4793-901f-3485a366fea1'></a>

is the corresponding characteristic equation for the system with no delay. Since the model we
consider is of retarded and not neutral type, G(λ) is of higher order than K(λ). This ensures (see

<!-- PAGE BREAK -->

<a id='711205e8-a531-403e-bd12-7d52686fc2e4'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='3742a8dd-dd9d-4ed5-b804-1db174eb81a7'></a>

207

<a id='04b0e266-476c-4294-a807-ac4664890bc9'></a>

[27]) that as τ→ 0, n of the roots of (7) tend towards the roots of P(λ) = 0, while the remainder of the roots have real parts tending to large negative values. Hence as τ→ 0 the stability properties of the equilibrium points in the non-delay model (1) are recovered.
The characteristic function of (4), determined from the Laplace transform [23], is
H₁(λ, τ) = (λ² + (δ + c)λ + δc – ηe⁻λτ) (λ + c),
(9)
where η = (1 – nₚ)δNkTo e⁻mτ. Further, if we assume that the system is in quasi-steady state before drug therapy, i.e., c = NkTo, and that the death during transition from infected to productively infected is negligible, i.e., m ≪ 1, we can then simplify η to
η = (1 – nₚ)δc.
(10)
From (9) one eigenvalue is equal to –c and hence always negative. In what follows we determine the other eigenvalues from the solutions of
H(λ, τ) = λ² + (δ + c)λ + δc – ηe⁻λτ = 0.
(11)
The following results show that the eigenvalues will remain in the left half plane and show the location of the largest eigenvalue. Set λ = μ + iν where μ, ν ∈ ℝ and substitute into (11) to get
H(μ, ν, τ) = [μ² – ν² + (δ + c)μ + δc – ηe⁻μτ cos ντ] + i[2μν + ν(δ + c) + ηe⁻μτ sin ντ],
(12)
where H(μ, 0, τ) ≡ H(μ) = μ² + (δ + c)μ + δc – ηe⁻μτ.

<a id='633dac77-303a-4b06-a5d8-5bfb22f07c5c'></a>

**Lemma 1.** If H(μ) > 0 then there is no v ∈ R such that H(μ + iv) = 0. Moreover, if H(μ) = 0 then H(μ + iv) = 0 if and only if v = 0.

**Proof** (by contradiction). Assume that H(μ + iv) = 0. Then H(μ + iv) can be rewritten in terms of its real and imaginary parts as
μ² – v² + μ(δ + c) + δc = ηe^(-μτ) cos vτ and 2μv + v(δ + c) = -ηe^(-μτ) sin vτ.
Taking the squares of the absolute values of both equations and adding together gives
[v² + (μ + c)²][v² + (μ + δ)²] = η²e^(-2μτ)
which implies that
(μ + c)² (μ + δ)² – η²e^(-2μτ) = -v⁴ - v²[(μ + c)² + (μ + δ)²].

<a id='2dc85879-514a-4cc3-8da7-fb5024a99d60'></a>

The left-hand side of this equation equals
$H(\mu)[(\mu + c)(\mu + \delta) + \eta e^{-\mu\tau}] = H(\mu)[H(\mu) + 2\eta e^{-\mu\tau}]$

<a id='202d201c-737b-442d-b3c8-bdf745570bd4'></a>

which is always positive given H(μ) > 0. The right-hand side is always negative leading to a contradiction. Therefore, H(μ + iv) ≠ 0 given H(μ) > 0. The second part of the proof is easily seen. □

<a id='dede7d64-d13a-4345-8d7f-4b8bb0331178'></a>

Note that $H(\mu)$ can be rewritten as $H(\mu) = \mu^2 + (\delta + c)\mu + \delta c(1 - (1-n_p)e^{-\tau})$. Since $\delta > 0$, $c > 0$, and $0 \le n_p \le 1$, $H(\mu) > 0$ for $\mu > 0$. Therefore by Lemma 1 there are no eigenvalues with non-negative real part. Moreover, a special case of the above lemma shows that if $H(0) > 0$, then there is no $v \in \mathbb{R}$ such that $H(iv) = 0$. Hence there are no purely imaginary roots.

<!-- PAGE BREAK -->

<a id='1e9a85d1-396f-4eb3-9f70-e5e3b8007ec6'></a>

208

<a id='0bd9a0c4-2120-469b-aaf0-3822ce477e4c'></a>

208 P. W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215 <::This visual content is a figure composed of four graphs arranged in a 2x2 grid. Each graph plots H(λ,τ) on the y-axis against λ₁ on the x-axis. The y-axis ranges from -0.5 to 0.5, and the x-axis ranges from -0.65 to -0.4. A dashed horizontal line is present at H(λ,τ) = 0 in all graphs. Each graph contains multiple upward-sloping, roughly parallel lines, representing different values of τ (delay), varying from τ = 0 to τ = 1.5. The lines are labeled for τ = 0 and τ = 1.5. The four graphs correspond to different values of nₚ (drug efficacy):

1.  **Top-Left Graph:** nₚ = 0.8
2.  **Top-Right Graph:** nₚ = 0.85
3.  **Bottom-Left Graph:** nₚ = 0.9
4.  **Bottom-Right Graph:** nₚ = 0.95

Fig. 1. Each graph represents the solution (largest real eigenvalue) of (11) for the given values of $n_p$ with $\delta = 0.7$, $c = 3$, and $\tau$ varying in increments of 0.25. Notice as the drug efficacy gets larger, the value of the largest eigenvalue is less dependent on the value of the delay, $\tau$. If we set $n_p = 1$, the graphs combine into one curve with the largest root at $-\delta n_p = -0.7$ and the delay would have no effect on this value.
: chart::>

<a id='816b6c80-3940-4d1b-985a-95a3063ea54d'></a>

In the remainder of this section we will show that there exists one real eigenvalue, called `û`, on the interval `[-c, 0)` (see Fig. 1) and that for certain parameter values all other eigenvalues, either real or complex, have real parts at least an order of magnitude smaller then `û`. (This is similar to showing the approximation of `λ₁ ~ -δn_p` was valid given `c ≫ δ`.)

<a id='6acba6aa-5bda-4525-a840-cddb786c1e2a'></a>

**Theorem 1.** For each τ ≥ 0 there is exactly one û(τ) ∈ [min(−c, −δ), ∞) such that H(û) = 0. Moreover, when H(μ) > 0 for μ > û then û is the unique eigenvalue with the largest real part.

<a id='58c614f8-f29e-42d4-97a7-81b1f74b2e1b'></a>

Proof.

$H(\mu) = \mu^2 + (\delta + c)\mu + \delta c - \eta e^{-\mu\tau}$ and $H'(\mu) = 2\mu + (\delta + c) + \eta\tau e^{-\mu\tau}$.

<a id='b3f9fe66-d569-4495-b0a6-1f343595f41c'></a>

For $\mu \in [-c, -\delta]$, $H(\mu) < 0$ and for $\mu \ge - (c + \delta)/2$, $H'(\mu) > 0$. Hence $H(\mu)$ is a monotonic increasing function on the interval $[-\frac{(c+\delta)}{2}, \infty)$. Therefore, there exists exactly one unique $\hat{\mu}$ such that $H(\hat{\mu}) = 0$ for $\hat{\mu} \in [\min(-c, -\delta), \infty)$. Now for $\mu > \hat{\mu}$, $H(\mu) > 0$ and by Lemma 1 cannot be the real part of any eigenvalue. Thus, $\hat{\mu}$ is the largest real eigenvalue. \u25a1

<a id='6b7465e3-9329-41de-9f2e-87e192a03c00'></a>

Moreover, by direct computation, H(0) = n_pδc > 0. Thus, by Lemma 1, μ̂ < 0. In other words, μ̂(τ) ∈ [min(-c, -δ), 0), and further assuming c ≫ δ, μ̂(τ) ∈ [-c, 0). Thus, there is only one real root in the interval, [-c, 0). To complete this analysis we must show that this interval contains no complex eigenvalues. If there exists complex eigenvalues in [-c, 0) then we would be unable to claim that the real eigenvalue, μ̂, is the slowest varying, or dominant, eigenvalue since the complex eigenvalues would have real parts of the same order of magnitude as μ̂. Hence we would be unable to isolate a single dominant term.

<!-- PAGE BREAK -->

<a id='9b5c981f-7641-4562-83c6-a169acde44a4'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='31d13b4c-8a1a-4857-8b6e-a4c44d27242b'></a>

209

<a id='49c16931-8343-4d68-a647-c9cba851ccb6'></a>

## 3.2. Numerical analysis of location of complex roots

By definition if there exists a pair of complex eigenvalues in $[-c,0)$ then given $\mu \in [-c, 0)$, $H(\mu + i\nu) = 0$ for some $\nu \in \mathbb{R}$. We can write the eigenvalue equation $H(\lambda)$ in terms of two real equations defined as

$\mu^2 + (\delta + c)\mu + \delta c - \nu^2 = \eta e^{-\mu\tau} \cos \nu\tau$, (13a)

$2\mu\nu + \nu(\delta + c) = -\eta e^{-\mu\tau} \sin \nu\tau$. (13b)

<a id='aa8ade0b-9a8e-4697-b0cf-108be63e28c4'></a>

We can rewrite (13a) as

H(μ) – ν² = ηε-μτ cos ντ,

(14)

where H = μ² + (c + δ)μ + δc. It is easily seen that on the interval μ∈ [−c, −δ], H(μ) ≤ 0. We can also define some constraints to validate numerical results.

<a id='b6f56271-f709-41a5-9f94-98f920a08b59'></a>

### 3.2.1. Constraint I
Given μ∈ [-c, -δ], the left-hand side of (14) is always less then or equal to zero. For 0 < ντ < π/2 the right-hand side of (14) is positive and hence there can be no solution to the equation. Subsequently, for 0 < ντ < π/2 and μ∈ [-δ,0), (13b) cannot be satisfied. In general, for (13a) and (13b) to have complex roots, the following has to hold:

<a id='ee7a44f3-6d45-48ce-8530-e593adc21505'></a>

$\max(\bar{H} - v^2) \geq \min(\eta e^{-\mu\tau} \cos v\tau).$

<a id='f20f7187-fb91-4da9-9bbe-09598d878b90'></a>

For μ ∈ [-c, -δ], min(ηe^(-μτ) cos vτ) = -ηe^(cτ) and max(H - v²) = -v². Thus, (15) implies that for a root to exist, v² ≤ ηe^(cτ). Since there is no solution if 0 < vτ < π/2, π/(2τ) < v < √ηe^(cτ) is a necessary condition for a non-zero root. Hence, if √ηe^(cτ) < π/(2τ) there can be no non-zero solution. Rearranging, we find that if

0 < τ√e^(cτ) < π / (2√η)

<a id='2375f4ea-f235-4dd1-81f4-cfcc8fe742cd'></a>

then (13a) and (13b) has no solution for v≠ 0.

<a id='38f90bf5-0f34-4b18-ba46-eee6d534ffe1'></a>

3.2.2. Constraint II

As pointed out to us by D. Calloway, Cornell University, the derivative of (13a) with respect to μ is 1/v times the left-hand side of (13b). Therefore,

$$\frac{\partial}{\partial\mu} (\eta e^{-\mu\tau} \cos v\tau) = -\frac{1}{v} \eta e^{-\mu\tau} \sin v\tau$$

<a id='9b287df9-7172-41f2-8bc7-2b55a2934bb5'></a>

and hence a condition for the system (13a) and (13b) to have a solution is

ντ = tan ντ. (16)

<a id='5755112b-004a-4412-bb61-4905eeb86ddd'></a>

This result gives an infinite number of solutions due to the periodicity of the tangent function. Solving this equation numerically, we find ντ = 0, ~ 4.4934, ~ 7.7235, . . . But, from (14), we can write

v² < ηeᶜᵗ + H(μ) ≤ ηeᶜᵗ,
(17)

<a id='cccf4678-449e-4ee1-887e-27f75a800ab5'></a>

(15)

<!-- PAGE BREAK -->

<a id='5e4ee6eb-fb7b-40a3-a2ae-6b8df712dcac'></a>

210

<a id='00c7bfb9-614c-4879-8a28-6249d59ccba6'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='b1af0e66-8a74-41d4-ab80-31e99f7bf196'></a>

which gives a bound on v necessary for (13a) and (13b) to have a solution. For example, with
δ = 0.5, c = 3 and a drug efficacy n_p = 0.7, η = 0.45. Hence for τ < 1.5, v < 6.36 and hence the
solutions with ντ ≥ 7.7235 can be excluded. Thus the constraints provide a finite range of v in
which to search for solutions, simplifying the following numerical calculations.

<a id='9f5650a5-5105-4250-a161-10f8d04b3c83'></a>

### 3.2.3. Numerical calculations
Using the above results, we examine the possible existence of complex eigenvalues numerically. We restrict our attention to the case $c = 3$. Discretizing $\mu$, $\nu$, $\tau$, and $n_p$ with step sizes of $0.01$ and using Matlab we find for $\mu \in [-3,0)$, and $n_p \in (0.7,0.9)$ there exists no solution of (13a) and (13b) with $\nu \neq 0$ for determined ranges of $\tau$. As an example, with $\delta = 0.5$, $c = 3$ and $n_p = 0.8$, numerically we find no solutions of (13a) and (13b) when $\tau < 0.825$. This agrees surprisingly well with constraint I, which implies no solutions given $\tau < 0.828$. If we use a higher efficacy of drug treatment, say $n_p = 0.95$ then numerically we can show there are no solutions with $\tau < 1.18$ and using constraint I, we find no solutions for $\tau < 1.105$. Varying $\delta$ between $(0.25, 0.75)$ adjusts the upper bound on $\tau$. For example, with $\delta = 0.35$, $c = 3$ and $n_p = 0.95$, (13a) and (13b) is not satisfied with $\mu > -3$ given $\tau < 1.15$. These numerical results compared with the above constraints for $\tau$ and $\nu$ provide sufficient evidence to support the conclusion that there exists only one unique root which is real and dominant while also providing sufficient reasoning for neglecting, to first approximation, all eigenvalues of the delay model except the unique real eigenvalue.

<a id='ff620d62-a7d6-4abd-9097-0a157a4aee2e'></a>

The value of _c_ may be higher than _c_ = 3 [10,28,29]. If this is so, then a high drug efficacy is required to guarantee that there will not be any complex eigenvalues. For example, if _c_ = 5 and _τ_ = 1 then only with a drug efficacy of 0.92 or higher, will there be one unique real eigenvalue. If _c_ is much higher, then our results show the existence of complex eigenvalues but the order of magnitude of their real parts is still dominated by the single negative and real eigenvalue. Therefore, it should still be possible to describe the viral decline seen in patients after drug treatment to a good approximation by a single exponential but the shoulder region no longer depends on _c_ alone but a combination of _c_ and the complex eigenvalues.

<a id='a802662f-462e-48c4-9e65-631bab2dc1a0'></a>

4. Delay effects on dominant eigenvalue
With the results of the previous section we can now present the main finding of this work: an asymptotic representation for the dominant eigenvalue and how the delay effects its value (see Fig. 1). Since we have shown that for μ ∈ (-3,0) there are no complex roots for a defined τ, we can let μ̂ be the unique root of H(μ, 0, τ) = H(μ, τ) = μ² + (δ + c)μ̂ + δc – ηe⁻μ̂τ = 0 with the largest real part. Expanding e⁻μ̂τ in a Taylor series gives

<a id='9f6f6913-8a4d-48e0-b3c1-47a47d0a5dc5'></a>

e^{-\mu\tau} \sim 1 - \hat{\mu}\tau + \frac{\hat{\mu}^2\tau^2}{2} + O(\hat{\mu}^3\tau^3),
(18)

<a id='69de7c2d-09f0-434d-8d16-7aea97b70a96'></a>

provided that |ûτ| is sufficiently small. From our previous results, we have shown that û varies between [-0.5,0) depending on the parameters used. Also, it has been suggested experimentally that a realistic value of the time delay is on the order of 1 day. Hence, the expansion for the exponential term is reasonably accurate and the accuracy improves as the value of û → 0. Also,

<!-- PAGE BREAK -->

<a id='b4d5ff0c-9ec3-47ce-88db-7f780a84b5fd'></a>

P.W. Nelson et al. | Mathematical Biosciences 163 (2000) 201–215                                                                    211

<a id='e2d3de9c-6c33-4814-a6f4-fcf6b5958017'></a>

notice from (22), that as τ increases, μ̂ decreases, hence |μ̂τ| remains sufficiently small. Substituting this expansion into (11) yields

μ̂² + μ̂(δ + c) + δc − η(1 − μ̂τ + (μ̂τ)²/2 + 0(μ̂³τ³)) = 0 (19)

<a id='10ae218a-a6b1-4b00-a2d2-b5d20d67c701'></a>

and solving for μ̂ gives

μ̂ = rac{1}{2(1 - \eta\tau^2/2)} \left[ -(\delta + c + \eta\tau) \pm (\delta + c + \eta\tau) \sqrt{1 - \frac{4(\delta c - \eta)(1 - c\eta\tau^2/2)}{(\delta + c + \eta\tau)^2}} \right]. (20)

<a id='d7a4af06-a0bd-47e3-bbf8-0f5776ddd153'></a>

The square root term can be approximated by the first two terms of its binomial expansion, since
for the parameter values of interest

<a id='5c15befe-7071-48c5-a036-ca91fb2acfa3'></a>

<::|\frac{4(\delta c - \eta)(1 - \frac{\eta\tau^2}{2})}{(\delta + c + \eta\tau)^2}| < 1.: equation::>

<a id='193a52c0-b788-46f2-9858-02cc2787f8bd'></a>

Using this and taking the positive term we get

$\hat{\mu} \sim - \frac{\delta c - \eta}{\delta + c + \eta \tau}$ (21)

<a id='554160bd-81fb-4026-a49b-dc0ef6203244'></a>

Assuming c \gg \delta [2,10,29], and using the definition of \eta (10), we find

$$\hat{\mu} \sim -\frac{\delta n_p}{1 + (1 - n_p)\delta\tau} = -\delta n_p C(\tau, n_p, \delta) \tag{22}$$

<a id='c6a9c906-72b2-4f06-a36f-248d9a64f872'></a>

where

C(τ, n_p, δ) = 1 / (1 + (1 - n_p)δτ) < 1

<a id='cf76a3b7-67a3-452f-a208-a3cadfae932b'></a>

is the correction introduced by incorporating a delay. Notice the rate of decay, û, is proportional to the product of the rate constant for death of virus producing T-cells, δ, and the efficacy of the protease inhibitor, np, but now this product is reduced by the delay since as τ gets bigger the value of û gets smaller.

<a id='71041afd-5228-4a43-ba5e-99a97140be65'></a>

We illustrate the effects of delay in Figs. 2 and 3. When n_p ≠ 1, the delay reduces the long term rate of decline of the viral load and hence any estimate of δ that is made which does not take the delay into account will be flawed. The effect, however, is not large. For example, if τ = 1 day, a typical value, and n_p = 0.8 then the correction due to the delay

<a id='08a94024-ebe1-4bfe-a317-6aead8eefdd9'></a>

<::C(\tau, n_p, \delta) = \frac{1}{1 + 0.2\delta}
: figure::>

<a id='35fce2c2-69a1-48c9-a6ca-ae66d718c083'></a>

For $\delta = 0.5$ day$^{-1}$ [1], $C = 0.91$. If the drug is only 50% efficacious, which would be remarkably low, then $C = 0.8$. Hence if the intracellular delay is approximately constant, as assumed here, and if the effects of drug efficacy are properly taken into account, then including the delay will change the estimate of $\delta$ from slope/$n_p$ to slope/$n_p C$, which for the cases considered above yields at most a 25% increase in $\delta$.

<!-- PAGE BREAK -->

<a id='31488043-8b2b-4e16-b77d-e2037f5799de'></a>

212
P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201-215
<::A figure containing three line plots. The top plot shows HIV RNA/ml on the logarithmic y-axis (from 10^2 to 10^6) versus days on the x-axis (from 0 to 14). It contains two decaying curves, one solid line labeled "τ = 0" and one dashed-dot line labeled "τ = 1". The two curves are parallel. The bottom section contains two side-by-side line plots. The left plot shows HIV RNA/ml on the logarithmic y-axis (from 10^2 to 10^6) versus days on the x-axis (from 0 to 10). It also contains two decaying curves, one solid line labeled "τ = 0" and one dashed-dot line labeled "τ = 1". The right plot shows HIV RNA/ml on the logarithmic y-axis (from 10^2 to 10^6) versus days on the x-axis (from 0 to 10). It similarly contains two decaying curves, one solid line labeled "τ = 0" and one dashed-dot line labeled "τ = 1". In both bottom plots, the slopes of the curves diverge.: figure::>
Fig. 2. The top plot shows the numerical solution for viral decay when a perfect drug is used. Notice the slopes of the decay with and without a delay are parallel. The bottom two graphs compare the viral decay with and without a delay assuming a less then perfect drug; with np = 0.8 in the left panel and np = 0.5 in the right panel. Both cases show the change in the slope is affected by the delay. The model parameters, besides the ones noted, are given in Table 1.

<a id='17d8bd78-0621-49e6-80b7-69d39517ed77'></a>

<::chart: The chart titled "HIV RNA/ml" on the y-axis (log scale from 10^2 to 10^6) and "days" on the x-axis (0 to 14) displays viral decay curves. There are four curves, representing different values of τ (delay). The solid line corresponds to τ = 0 days. The three dashed lines correspond to τ = 0.5, 1, and 1.5 days, with the topmost dashed line explicitly labeled as τ = 1.5 days. The caption below the figure states: "Fig. 3. The viral decay for τ = 0, 0.5, 1, and 1.5 days when the drug efficacy n_p = 0.8. The slopes of the curves generated with different delays differ. Also, the shoulder region on the curve increases as τ increases, an effect noticed previously [5,6,10]." ::>

<!-- PAGE BREAK -->

<a id='0576a582-fbcd-41f6-aeff-cfd66f3e4417'></a>

*P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215*

<a id='32ade2de-2209-4048-8743-40305a5cf275'></a>

213

<a id='13e0bef4-5865-425a-88e8-bc22481438c5'></a>

# 5. Conclusions
The main goal of this paper was to show that the viral decay seen in HIV-1 infected patients put under antiretroviral therapy depends not only on the lifespan of viral producing cells, δ, but also the efficacy of the therapy, np and the length of the intracellular delay, τ, that measures the time between viral infection of a cell and the time the cell begins releasing virus. Here we have focused on the effects of protease inhibitor therapy because detailed data have been published about the kinetics of viral load decline and used to estimate both c and δ [1]. In [1] a model with no delay and np = 1 was used to estimate c and δ, and the claim was made that the estimates of both of these parameters were minimal estimates. Our results support the claim that the estimate of δ was minimal since the inclusion of drug efficacy and delay both reduce the slope of the viral decay curve. Hence estimates of δ made by examining the slope, as was in essence done in [1], under- estimate the true value of δ. Recent work by Mittler et al. [6,10] using a model with delay argue that the published estimates of c were also minimal as claimed. Previous work of Herz et al. [5] and Mittler et al. [6] have shown that an intracellular delay can effect the length of the 'shoulder region' observed in Fig. 3, i.e., the time between initiation of therapy and the observed decay in plasma virus. But in both of these theoretical models, no changes were predicted during the ex- ponential decline of the viral load. We have shown that this is due to assuming the protease in- hibitor to be completely effective. When the efficacy, np = 1, the effects of the delay cancel out. The above results imply that the inclusion of a constant delay and allowing the protease inhibitor to be less then perfect changes the estimates for the productively infected T-cell loss rate, δ, and the viral decay rate, c.

<a id='2e1d0432-6d5f-4b4f-902d-124cd0197310'></a>

Including a delay also changes the estimated lifespan of a productively infected cell. In previous work without delays the average lifespan of a productively infected cell was calculated as 1/δ. Here we have taken into consideration that there are two phases in the life of cell from time of infection to death. First, there is an eclipse phase in which the virus enters the cell, uses reverse transcriptase to copy its RNA genome into DNA, and proceeds through a number of steps in its life cycle before new virus particles are produced. The length of the eclipse phase is represented by the delay τ. Following the eclipse phase, the cell produces virus. In the current model the average lifespan of a virus producing cell is 1/δ. Thus the total average lifespan of cell from infection to death is τ + 1/δ. The precise value of τ is not known but current estimates suggest values of 1–1.5 days [1,6,10]. Thus, to a first approximation T-cells infected with HIV-1 might live an average of 2–3 days rather than the average of 1–2 days previously reported [1,3,4]. Currently, work is in progress examining delays in drug activation and modeling the efficacy of the drug as a dynamically varying parameter. Also, there is a need to explore the effects of different types of delays such as distributed delays or multiple discrete delays; some of which is already in progress. The length of the delay is not directly measurable in vivo. Thus, additional in vitro data would prove valuable in expanding our knowledge of the delay characteristics.

<a id='87bf04bd-3169-43e6-8081-7065d57abba5'></a>

## Acknowledgements

The authors thank John Mittler and Hans Weinberger for their help and Duncan Calloway for critically reading and commenting on the manuscript. Portions of this work were performed under

<!-- PAGE BREAK -->

<a id='f23290cb-2918-4eae-8eef-6d6ed4e787df'></a>

214

<a id='bc0191b8-64a0-45f4-bab5-ab2cd2498613'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='cc49b360-0ab1-44b6-bab0-296019285b0f'></a>

the auspices of the US Department of Energy and supported by NIH grant RR06555 (ASP) and an Institute for Mathematics and Its Applications Postdoctoral Fellowship (PWN) with funds provided by the National Science Foundation.

<a id='82ff27a0-b09e-41f7-bf04-e546fff91fdd'></a>

References

1. A.S. Perelson, A.U. Neumann, M. Markowitz, J.M. Leonard, D.D. Ho, HIV-1 dynamics in vivo: Virion clearancerate infected cell life-span and viral generation time, Science 271 (1996) 1582.
2. A.S. Perelson, P. Essunger, Y. Cao, M. Vesanen, A. Hurley, K. Saksela, M. Markowitz, D.D. Ho, Decay characteristics of HIV-1-infected compartments during combination therapy, Nature 387 (1997) 188.
3. X. Wei, S.K. Ghosh, M.E. Taylor, V.A. Johnson, E.A. Emini, P. Deutsch, J.D. Lifson, S. Bonhoeffer, M.A. Nowak, B.H. Hahn, S.S. Saag, G.M. Shaw, Viral dynamics in human immunodeficiency virus type 1 infection, Nature 373 (1995) 117.
4. D.D. Ho, A.U. Neumann, A.S. Perelson, W. Chen, J.M. Leonard, M. Markowitz, Rapid turnover of plasma virions and CD4 lymphocytesin HIV-1 infection, Nature 373 (1995) 123.
5. V.M. Herz, S. Bonhoeffer, R.M. Anderson, R.M. May, M.A. Nowak, Viral dynamics in vivo: Limitations onestimations on intracellular delay and virus decay, Proc. Nat. Acad. Sci. USA 93 (1996) 7247.
6. J.E. Mittler, B. Sulzer, A.U. Neumann, A.S. Perelson, Influence of delayed virus production on viral dynamics in HIV-1 infected patients, Math. Biosci. 152 (1998) 143.
7. L.M. Wein, R.M. D'Amato, A.S. Perelson, Mathematical considerations of antiretroviral therapy aimed at HIV-1 eradication or maintenance of low viral loads, J. Theoret. Biol. 192 (1998) 81.
8. Z. Grossman, M. Feinberg, V. Kuznetsov, D. Dimitrov, W. Paul, HIV infection: how effective is drug combinationtreatment? Immunol. Today 19 (1988) 528.
9. J. Tam, Delay effect in a model for virus replication, IMA J. Math. Appl. Med. Biol. 16 (1999) 29.
10. J.E. Mittler, M. Markowitz, D.D. Ho, A.S. Perelson, Refined estimates for HIV-1 clearance rate and intracellular delay, AIDS 13 (1999) 1415.
11. P.W. Nelson, J. Mittler, A.S. Perelson, Effect of the eclipse phase of the viral life cycle on estimation of HIV viral dynamic parameters, submitted.
12. H.J. Bremermann, Mechanism of HIV persistence: implications for vaccines and therapy, J. AIDS 9 (1995) 459.
13. N.I. Stilianakis, C.A.B. Boucher, M.D. DeJong, R. VanLeeuwen, R. Schuurman, R.J. DeBoer, Clinical data sets on human immunodeficiency virus type 1 reverse transcriptase resistant mutants explained by a mathematical model, J. Virol. 71 (1997) 161.
14. S. Bonhoeffer, R.M. May, G.M. Shaw, M.A. Nowak, Virus dynamics and drug therapy, Proc. Nat. Acad. Sci. USA 94 (1997) 6971.
15. P. Essunger, A.S. Perelson, Modeling HIV infection of CD4+ T-Cell subpopulations, J. Theoret. Biol. 170 (1994) 367.
16. D.E. Kirschner, R. Mehr, A.S. Pereson, The role of the thymus in pediatric HIV-1 infection, J. AIDS 18 (1998) 95.
17. M.A. Nowak, R.M. Anderson, M.C. Boerlijist, S. Bonhoeffer, R.M. May, A.J. McMichael, HIV-1 evolution and disease progression, Science 274 (1996) 1008.
18. N.I. Stilianakis, K. Dietz, D. Schenzle, Analysis of a model for the pathogenesis of AIDS, Math. Biosci. 145 (1997) 27.
19. M.A. Nowak, S. Bonhoeffer, G.M. Shaw, R.M. May, Anti-viral drug treatment: dynamics of resistance in free virus and infected cell populations, J. Theoret. Biol. 184 (1997) 205.
20. D.E. Kirschner, G.F. Webb, Understanding drug resistance for monotherapy treatment of HIV infection, Bull. Math. Biol. 59 (1997) 763.
21. P.W. Nelson, Mathematical models of HIV pathogenesis and immunology, PhD thesis, University of Washington, pp. 1-150, 1998.
22. A.S. Perelson, P.W. Nelson, Mathematical models of HIV dynamics in vivo, SIAM Review 41 (1999) 3.
23. R. Bellman, K.L. Cooke, Differential-Difference Equations, Academic Press, New York, 1963.

<!-- PAGE BREAK -->

<a id='a921f8da-3888-4ab1-a800-2f8e2bee1774'></a>

P.W. Nelson et al. / Mathematical Biosciences 163 (2000) 201–215

<a id='5516e70e-3670-47ab-a2b6-49c9dfd1708d'></a>

215

<a id='15f0a11b-053c-445c-8363-511562b81c24'></a>

[24] D.M. Pratt, Analysis of population development in Daphnia at different temperatures, Biol. Bull. 85 (1943) 116.
[25] C.E. Taylor, R.R. Sokal, Oscillations in housefly population sizes due to time lags, Ecology 57 (1976) 1060.
[26] N. MacDonald, Time Lags in Biological Models, Springer, Berlin, 1970.
[27] L.E. El'sgol'ts, S.B. Norkin, An Introduction to the Theory and Application of Differential Equations with Deviating Arguments, Academic Press, New York, 1973.
[28] T. Igarashi, C. Brown, A. Azadegan, N. Haigwood, D. Dimitrov, M.A. Martin, R. Shibata, Human immunodeficiency virus type 1 neutralizing antibodies accelerate clearance of cell-free virions from blood plasma, Nature Med. 5 (1999) 211.
[29] B. Ramratnam, S. Bonhoeffer, J. Binley, A. Hurley, L. Zhang, J.E. Mittler, M. Markowitz, J.M. Moore, A.S. Perelson, D.D. Ho, Rapid production and clearance of HIV-1 and hepatitis C virus assessed by large volume plasma apheresis, Lancet 354 (1999) 1782.
[30] D.E. Kirschner, G.F. Webb, A model for treatment strategy in the chemotherapy of AIDS, Bull. Math. Biol. 58 (1996) 367.
[31] A.R. McLean, C.A. Michie, In vivo estimates of division and death rates of human lymphocytes, Proc. Nat. Acad. Sci. USA 92 (1995) 3707.
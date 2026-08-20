<a id='d03c3504-cee7-46ea-992d-777d06401d0e'></a>

J. Math. Biol. (2016) 72:1337-1368
DOI 10.1007/s00285-015-0905-0

<a id='b4a3c67e-5c90-4567-959c-15e0b5976947'></a>

Mathematical Biology

<a id='6753a3cd-da83-475c-8288-995ca3152ad6'></a>

<::logo: CrossMark
CrossMark
The logo features a red bookmark icon within a blue and grey circle, accompanied by the text "CrossMark".::>

<a id='9921e009-16a4-4318-a92e-36bc4e41b71b'></a>

Geometric analysis of the Goldbeter minimal model for the embryonic cell cycle

<a id='4e0292c6-a4aa-45d4-a113-63f6272223fc'></a>

Ilona Kosiuk¹ · Peter Szmolyan²

<a id='83edd11b-057c-4926-9d7a-e360500be7c7'></a>

Received: 13 February 2015 / Revised: 11 May 2015 / Published online: 23 June 2015
© Springer-Verlag Berlin Heidelberg 2015

<a id='0534d385-d69c-4a7b-99c8-2051f4f4203d'></a>

**Abstract** A minimal model describing the embryonic cell division cycle at the molecular level in eukaryotes is analyzed mathematically. It is known from numerical simulations that the corresponding three-dimensional system of ODEs has periodic solutions in certain parameter regimes. We prove the existence of a stable limit cycle and provide a detailed description on how the limit cycle is generated. The limit cycle corresponds to a relaxation oscillation of an auxiliary system, which is singularly perturbed and has the same orbits as the original model. The singular perturbation character of the auxiliary problem is caused by the occurrence of small Michaelis constants in the model. Essential pieces of the limit cycle of the auxiliary problem consist of segments of slow motion close to several branches of a two dimensional critical manifold which are connected by fast jumps. In addition, a new phenomenon of exchange of stability occurs at lines, where the branches of the two-dimensional critical manifold intersect. This novel type of relaxation oscillations is studied by combining standard results from geometric singular perturbation with several suitable blow-up transformations.

<a id='d16a0a70-a644-4657-9c72-ff6db6405c97'></a>

**Keywords** Cell cycle · Mitotic oscillator · Enzyme kinetics · Geometric singular perturbation theory · Relaxation oscillations · Blow-up method

<a id='b6dafd1e-a9bc-4424-8bb2-91d52a53182c'></a>

--- 

✉ Ilona Kosiuk
ilona.kosiuk@mis.mpg.de

Peter Szmolyan
szmolyan@tuwien.ac.at

1 Max Planck Institute for Mathematics in the Sciences, Inselstraße 22, 04103 Leipzig, Germany
2 Institute for Analysis and Scientific Computing, Technische Universität Wien,
Wiedner Hauptstraße 8-10, 1040 Vienna, Austria

<a id='043ef5a0-87ed-48a4-abea-d1904a8c51dd'></a>

Springer

<!-- PAGE BREAK -->

<a id='260aa544-fdff-48bf-916c-5e71d26dcc5e'></a>

1338

<a id='b1e3e3ba-00bf-4853-a1ba-589deff0adb9'></a>

I. Kosiuk, P. Szmolyan

<a id='ef4264b5-6e5d-4c4d-9185-758d93a827e1'></a>

Mathematics Subject Classification 34C20 · 34C26 · 34E13 · 92C37 · 92C40 · 92C45

<a id='b2945660-1f8d-4272-b566-7c61aa2a7df1'></a>

# 1 Introduction

Understanding the process of cell division is a central issue in cell biology (Alberts et al. 2014). The cell division cycle is classically described as a sequence of several phases, G1, S, G2, and M, a cell must go through for the division to be completed. The gap phase G1 leads to the S phase of DNA replication, while the gap phase G2, separates the S phase from mitosis (the M phase), during which the cell divides into two daughter cells. The cell cycle involves a large variety of proteins and regulatory interactions, and many different processes have to take place correctly for a proper cell division. The control of cell division plays a crucial role in development and differentiation, e.g., the uncontrolled process can give rise to a cancer-like state. The key regulators of the cell cycle control system are two classes of proteins, cyclins and cyclin dependent kinases (cdks), which are responsible for the ordering and timing of the cell cycle transitions (Hunt 2001; Nurse 2000).

<a id='b96504e7-0c53-4dc0-9534-ccae2ff3e771'></a>

Due to the fact that in dividing cells mitosis recurs in regular intervals, cell divi-sion has been discussed in terms of a chemical oscillatory process. In particular, it has been hypothesized since the 1970s that the onset of mitosis in eukaryotic cells is controlled by a biochemical oscillator of the limit cycle type. Experimental studies support the existence of a continuous oscillator driving the cell division. In the sim-plest situation the cell cycle consists in the periodic alternation of interphase (with no discernible gap phases) and mitosis. The interphase is characterized by accumu-lation of cyclin. As cyclin passes a certain threshold mitosis promoting factor (MPF) in the form of activated cdk is produced. Activation and deactivation of cdk proceeds through phosphorylation-dephosphorylation cycles. A sufficient amount of MPF trig-gers mitosis and subsequent degradation of cyclin. As cyclin drops below another threshold MPF decreases, i.e., the corresponding cdk is deactivated. Thus, cyclin syn-thesis is both necessary and sufficient for entry into mitosis, while cyclin degradation is required for exit from mitosis. For more biological background we refer to (Alberts et al. 2014; Morgan 2007).

<a id='02a3082b-7a68-4c5f-9313-17d8e6c45b54'></a>

Due to the complexity of the process, mathematical modelling and simulation are commonly used to gain better understanding of the functioning and dynamics of the cell cycle. Typical models are systems of ODEs describing the time evolution of the biochemical species involved. Mathematical models of the cell cycle of varying complexity based on mass-action kinetics or Michaelis-Menten type kinetics have been developed (Battogtokh and Tyson 2004; Chen et al. 2000; Gérard and Goldbeter 2011, 2012; Goldbeter 1991; Sveiczer et al. 2004; Novak and Tyson 1995, 1997; Novak et al. 1998; Tyson 1991; Tyson et al. 2001). By now most of the regulatory mechanisms of these systems are being understood as positive or negative feedback loops. For introductions to mathematical models of the cell cycle we refer to (Aguda and Friedman 2008; Goldbeter 1996; Keener and Sneyd 1998). The analysis of these models is mostly based on direct numerical simulations and numerical bifurcation

<a id='0e635d58-2629-4f91-97dd-390bae00a443'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol in black, positioned to the left of the company name "Springer" written in a simple, sans-serif font.::>

<!-- PAGE BREAK -->

<a id='1b935377-1b24-4374-815a-e6103b76a21b'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='5c64b3ed-71ca-4ccb-a381-5dd59d61a049'></a>

1339

<a id='11b32da7-6d29-427a-972c-1ac37fff5517'></a>

analysis of equilibria or periodic orbits. Analytical arguments are typically used only for planar systems.

<a id='1af81a65-8520-4ff0-be72-ec63aa78b252'></a>

## 1.1 A minimal model for the mitotic oscillator

In this paper we study a minimal model for the cell cycle based on an enzymatic cascade of two phosphorylation-dephosphorylation cycles developed by Goldbeter (1991). The model is based on a negative feedback loop. Although the model is kept simple, i.e., the formation of a complex between cyclin and cdc2 kinase is not taken into account, it successfully captures the key features of the cell cycle as described above. Cyclin periodically activates and deactivates an enzyme cascade. More precisely, in the first cycle cyclin triggers the transformation of inactive (M+) into active (M) cdc2 kinase, whereas in the second cycle a transition from inactive (X+) into active (X) cyclin protease occurs, which in turn degrades cyclin, see Fig. 1. For a more detailed explanation of the model, see (Goldbeter 1991). The reactions involved in the two phosphorylation-dephosphorylation cycles are modelled by Michaelis-Menten type kinetics. This leads to the following three-dimensional system of ordinary differential equations for the cyclin concentration C, the fraction of active cdc2 kinase M, and the fraction of active cyclin protease X

<a id='b7c7ec6c-1dc8-4bf2-b464-306e74be39ec'></a>

dC / dτ = v_i - v_d X (C / (K_d + C)) - k_d C,
dM / dτ = V_1(C) ((1 - M) / (k_1 + 1 - M)) - V_2 (M / (k_2 + M)),
dX / dτ = V_3(M) ((1 - X) / (k_3 + 1 - X)) - V_4 (X / (k_4 + X))
(1)

<a id='ddfc6669-9c47-4ee6-80b8-4978152a9f11'></a>

with the effective maximum rates V₁(C) and V₃(M) given by
V₁(C) = V₁C / (K₉ + C),
V₃(M) = V₃M.

<a id='ac4a4dc3-c99b-47d1-b791-09468ff28c60'></a>

Since _X_ and _M_ represent fractions of active cyclin protease and _cdc2_ kinase, their values are restricted to [0, 1]. The fractions of inactive _cdc2_ kinase and cyclin protease are given by (1 - _M_) and (1 - _X_), respectively.

<a id='d10647f1-1a30-4e60-940f-8388e1253fc5'></a>

The parameter $v_d$ denotes the maximum rate of cyclin degradation by protease X, $v_i$ is the constant rate of cyclin synthesis. $K_d$ and $K_c$ denote the Michaelis constants for cyclin degradation and for cyclin activation of the $cdc25$ phosphatase acting on the phosphorylated form of the $cdc2$ kinase, respectively. The first-order reaction with a reaction rate constant $k_d$ represents a non-specific degradation of cyclin. The functions (parameters) $V_i$ and the parameters $k_i$ denote the effective maximum rates and the Michaelis constants, respectively, for the enzymes $E_i, i = 1,...,4$ involved in the two cycles of phosphorylation-dephosphorylation. A key assumption in the mitotic oscillator model is that both cyclic enzymatic reactions possess the property of zeroth-order ultrasensitivity, which requires that the Michaelis constants

<a id='fc05aea5-7089-4978-9109-dcc5b0d62a9a'></a>

<::Springer logo with a knight chess piece icon: figure::>

<!-- PAGE BREAK -->

<a id='23cfac92-1b7e-49a0-9c92-74b212efd60d'></a>

1340

<a id='d598ad38-7800-4b20-b592-58402d82c0d1'></a>

I. Kosiuk, P. Szmolyan

<a id='44d3290b-b5fa-4731-b146-f369c2d3d399'></a>

<::reaction diagram: A diagram illustrating Goldbeter's minimal model for the mitotic oscillator. It shows a series of reactions and conversions involving 'Cyclin', 'M', and 'X' species. An incoming flux 'v_i' leads to 'Cyclin'. 'Cyclin' undergoes degradation via 'v_d'. A dotted arrow indicates that 'Cyclin' influences the conversion between 'M+' and 'M'. Specifically, 'M+' converts to 'M' with rate 'V1' and enzyme 'E1', while 'M' converts to 'M+' with rate 'V2' and enzyme 'E2'. Another dotted arrow indicates that 'M' influences the conversion between 'X+' and 'X'. 'X+' converts to 'X' with rate 'V3' and enzyme 'E3', while 'X' converts to 'X+' with rate 'V4' and enzyme 'E4'. A dotted arrow from 'X' points towards 'v_d', indicating an influence on the degradation rate. Fig. 1 Goldbeter's minimal model for the mitotic oscillator::>

<a id='5adb87c8-1ead-4a3f-a8b2-400624f93895'></a>

<::A line chart plots 'Cdc2 kinase, M' on the y-axis against 'Cyclin, C' on the x-axis. The y-axis ranges from 0 to 1 in increments of 0.2. The x-axis ranges from 0 to 1 in increments of 0.2. The curve shows a low value of Cdc2 kinase for low Cyclin concentrations, then sharply increases around Cyclin C = 0.4 to 0.5, reaching a high, saturated value near 1 for Cyclin C values greater than approximately 0.6.
: chart::>

**Fig. 2** Steady response of *cdc2* kinase *M* as a function of cyclin *C* for the parameter values given below

<a id='41da891b-fbd7-4b3a-b716-5cd3a49bb72b'></a>

k~j~, j = 1,..., 4 are small (Goldbeter and Koshland 1981). The basic feature of this phenomenon is illustrated in Fig. 2, i.e., the existence of sharp threshold in the triggering by cyclin of cdc2 kinase activation through dephosphorylation. Goldbeter observed numerically that for the parameter values k~d~ = 0.25, v~i~ = 0.25, K~c~ = 0.5, K~d~ = 0, V~M1~ = 3, V~2~ = 1.5, V~M3~ = 1, V~4~ = 0.7, v~d~ = 0.25, k~j~ = 10^-3^, j = 1,..., 4, system (1) has an attracting periodic solution, which qualitatively captures key features of the cell-cycle.

<a id='48e1e1cb-47bd-47a5-8fc7-04b75b40b448'></a>

For simplicity we set k_j = ε << 1, j = 1, ..., 4 in the following. More generally,
we could use k_j = εκ_j, j = 1,..., 4 with ε << 1 and k_j = O(1) and obtain similar
results. With these choices system (1) takes the form

<a id='0875a2a4-8d46-4144-9327-01049555c72a'></a>

dC / dτ = (1 / 4)(1 - X - C),

dM / dτ = (6C / (1 + 2C)) (1 - M / (ε + 1 - M)) - (3M / (2ε + M)),

dX / dτ = M (1 - X / (ε + 1 - X)) - (7X / (10ε + X))
(2)

<a id='16c72d5d-1025-4113-b6d9-3529d854e94f'></a>

Springer

<!-- PAGE BREAK -->

<a id='e8687be1-a9de-4123-9041-1625865b6ae2'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='f2b242ef-e529-4585-b940-1acb0032252b'></a>

1341

<a id='d64fd86a-0899-4ad9-a703-0409f3af32f9'></a>

Fig. 3 Numerically computed periodic solution of system (2) for ε = 10⁻³

<::1.0
0.8
0.6
0.4
0.2
0.0
0 10 20 30 40
Variables
— C
— M
- - X
: chart::>

Fig. 4 Numerically computed limit cycle (shown in red) of system (2) for ε = 10⁻³ and two orbits converging to the limit cycle (shown in brown)

<::M 0.7
1
C
0.5
0
0
0 1
X
: chart::>

<a id='d309b05e-c741-4d51-9e4c-55f78783ae0d'></a>

Provided &lt;&lt; 1 the following switching behavior emerges, see Fig. 3. Starting with a low cyclin concentration C and values of X, M close to zero, the variable C increases, while M and X stay close to zero. Once the variable C passes the activation threshold value C* := 0.5, the variable M increases sharply (up to 1). As soon as M exceeds the threshold M* := 0.7, X is activated and also increases sharply (up to 1). This in turn triggers the degradation of cyclin C, as C falls below the threshold value C* the variable M decreases and once it drops below the threshold M*, cyclin protease X is inactivated. Consequently, both M and X return to low values, while the level of C starts to rise again. This proceeds in a periodic manner and results in the generation of the limit cycle type oscillations, see Figs. 3 and 4, where a numerically computed solution of (2) and the corresponding limit cycle in phase space are shown, respectively.

<a id='67dfcb69-2c75-425b-b0b7-285ed14d4285'></a>

<::logo: Springer
Springer
The logo features a stylized knight chess piece next to the word "Springer" in black text.::>

<!-- PAGE BREAK -->

<a id='b2e92691-3aa5-4244-b56f-abdaf66b58b2'></a>

1342

<a id='adb46d67-e810-4964-bc77-357ab184c390'></a>

I. Kosiuk, P. Szmolyan

<a id='8dd8007c-68c7-4036-b781-be2615b7d951'></a>

Remark 1 Goldbeter's model for the mitotic oscillator is discussed in (Tyson et al. 2003) as one of the main modules of molecular regulatory networks under the name negative-feedback oscillator.

<a id='581dcc5c-6642-48c0-8fc4-0e15c89f7373'></a>

Despite the numerical evidence of periodic dynamics, a mathematical analysis of the mechanisms generating this dynamics is needed and can provide additional information. In (Erneux and Goldbeter 2006) the model (1) was studied by means of bifurcation theory and formal asymptotic methods. It was shown that small amplitude oscillations can be generated in a Hopf bifurcation. By applying a variant of the quasi-steady state approximation, a two-dimensional system was derived, which exhibits periodic oscillations. However, it seems that these results are not relevant for the parameter values given above and do not explain the dynamics. In fact, our analysis shows that the dynamics is truly three-dimensional and cannot be described by a (single) two-dimensional approximating system.

<a id='18f68c0b-0e8f-4511-8603-bd01be0aef3f'></a>

Remark 2 The analysis in this paper is carried out for the specific parameter values described above. The dynamics for other choices of the parameters could be analyzed similarly provided that ε is sufficiently small, see e.g., the case corresponding to Fig. 10.6 in (Goldbeter 1996), where M and X are more pulse-like, i.e., they do not reach the plateaus M = 1 and X = 1.

<a id='759642d9-4f02-4699-8c62-6bcd61caf534'></a>

## 1.2 Singular perturbation approach and results

To understand the nature of the observed oscillations, we analyze the dynamics of the system (2) in the limit of small ε. The limiting behaviour of the system (2) for ε → 0 is very different depending on whether (X, M) is O(ε)-close to the boundary of the square [0, 1]² or not. One possibility to resolve this singular behaviour is to consider the following auxiliary system

<a id='346e9a5b-b955-490a-9b3d-07c445b186a0'></a>

dX/dτ = [M(1 - X)(ε + X) - (7/10)X(ε + 1 - X)]F_ε(M),
dM/dτ = [(6C)/(1 + 2C)(1 - M)(ε + M) - (3/2)M(ε + 1 - M)]F_ε(X), (3)
dC/dτ = (1/4)(1 - X - C)F_ε(X, M),

<a id='42bb5906-fe49-4dd2-8096-cbc0e3b2e142'></a>

which is obtained by multiplying each component of the right hand side of the sys-
tem (2) by the factor F_&epsilon;(X, M) given by

<a id='e08001ef-675a-4738-af0f-566074f10b9b'></a>

F_ε(X, M) := F_ε(X)F_ε(M),
F_ε(X) := (ε + 1 – X)(ε + X), (4)
F_ε(M) := (ε + 1 – M)(ε + M).

<a id='d36a0eeb-8014-4535-baa8-57c606fcb789'></a>

We also changed the order of the variables to (X, M, C) since this leads to improved three-dimensional pictures, e.g., Fig. 4. Mathematically, the multiplication by the

<a id='e799953d-c604-478e-a955-b29ccc6fcd26'></a>

<::Springer logo with a knight chess piece icon
: figure::>

<!-- PAGE BREAK -->

<a id='7706a6f2-da6c-48d9-81a2-5a81cd79b469'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='6e250efc-cfb8-448c-9b32-4a767a06f9aa'></a>

1343

<a id='83b80eb5-b8cf-4a42-8858-bac6ee5dd166'></a>

factor Fε(X, M) amounts to a reparametrization of time, which depends on the position in phase space and does not change the phase portrait as long as Fε(X, M) is positive (Chicone 2006). This clearly holds for ε > 0 in the relevant part of phase space given by X ∈ [0, 1] and M ∈ [0, 1]. The derivative in (3) is with respect to the resulting reparametrized time variable, which we still denote by τ. The main reason for bringing the system into this form is that the auxiliary system (3) turns out to be a singular perturbation problem, which can be analyzed by geometric methods. A further advantage is that the auxiliary system (3) is polynomial. This approach has been successfully used in the analysis of a two-parameter singular perturbation problem describing glycolytic oscillations (Kosiuk and Szmolyan 2011).

<a id='1ab61115-5375-49e2-aa58-b74e1021729b'></a>

Remark 3 We would like to emphasize that the two systems (2) and (3) have the same phase portraits as long as $F_\varepsilon(X, M)$ is positive. The time dependence of the solutions of the mitotic oscillator (2) and the auxiliary system (3) is, however, very different, i.e., the dynamics of system (2) occurs essentially on a single time scale, whereas solutions of system (3) evolve on several fast and slow time scales. This is also apparent in Fig. 3 where the only hint of some singular dependence of the solutions on $\varepsilon$ are the sharp corners in the $X$ and $M$ components close to $M = 0$, $X = 0$, $M = 1$, and $X = 1$.

<a id='9c345f2d-bdee-4d61-9c51-8db4a949b590'></a>

Singular perturbations and the associated slow-fast dynamics are abundant in ODE-models of biological and bio-chemical processes, e.g., in enzyme kinetics, neuroscience, and population dynamics. In these problems often the main interest is to study the existence and bifurcation of special solutions, e.g., periodic, heteroclinic, and homoclinic orbits. A particular interesting type of periodic solutions are relaxation oscillations (Grasman 1987; Mishchenko and Kh 1980; Szmolyan and Wechselberger 2004). These highly non-linear oscillations characterized by repeated switching of slow and fast motions appear frequently in applications of biological nature. A prototypical system where they occur is the van der Pol equation of a triode circuit. Relaxation oscillations arise in many biological problems, e.g., heartbeat and neuronal activity, see e.g., (Izhikevich 2007; Keener and Sneyd 1998) and references therein.

<a id='077a3980-78b2-4132-97e5-381d9c103b94'></a>

Often the underlying equations arise in the standard form

<a id='99257f67-57d5-462a-a104-a5bf0ded16b2'></a>

εẋ = f(x, y, ε),
ẏ = g(x, y, ε)

(5)

<a id='d04e4fba-4f89-4263-819f-1611b28cb0f7'></a>

with (x, y) ∈ Rⁿ x Rᵐ, smooth functions f and g, and a small parameter ε > 0. The derivative in system (5) is with respect to the slow time scale t. On the fast time scale τ = t/ε the governing equations are

<a id='0f3bca54-4d1e-4623-b520-41677b666304'></a>

x' = f(x, y, ε),
y' = εg(x, y, ε).
(6)

<a id='3ce6e0db-e79f-4e53-a1f1-7b9c6093e31a'></a>

For a simple example of the form (5) we refer to system (26), which plays an important role in our analysis.

<a id='d5e3123b-4230-4e52-bfe0-3c32cac169bb'></a>

Traditionally, slow-fast systems and the related oscillatory phenomena have been studied by the method of matched asymptotic expansions, see e.g., (Grasman 1987;

<a id='d4efee05-3494-4a2e-adaa-540a90ee3e81'></a>

<::logo: Springer
Springer
The logo features a stylized knight chess piece next to the word "Springer" in black text.::>

<!-- PAGE BREAK -->

<a id='dd853c0c-f541-4b4d-8b7f-a6740fc91dfd'></a>

1344

<a id='d805b5fc-b02c-4930-a3bb-ae65b3bfa325'></a>

I. Kosiuk, P. Szmolyan

<a id='a5b54ab8-88b6-4ecc-b25b-ebe9a3b411d3'></a>

Mishchenko and Kh 1980). In addition, a very successful more qualitative approach based on the methods from dynamical systems theory known as *geometric singular perturbation theory* has been developed. Its foundation goes back to Fenichel (Fenichel 1979). For an introduction and survey material we refer to (Hek 2010; Jones 1995; Szmolyan 1991).

<a id='c6d9b2da-d164-4b75-aba5-df89be91db9d'></a>

The basic reasoning is the following. The dynamics of system (5) for ε > 0, or
of the equivalent fast system (6), is studied by analyzing and suitably combining the
dynamics of the reduced problem

<a id='2f961818-7585-4067-b0b2-b5d7b5b12460'></a>

0 = f(x, y, 0),

ẏ = g(x, y, 0),

(7)

<a id='a92ab570-83a3-4904-9bc6-156612487d8e'></a>

and the dynamics of the layer problem

<a id='12de5353-9d4d-472e-ba2b-42cca711fa61'></a>

x' = f (x, y, 0),
y' = 0,
(8)

<a id='9c759e8a-910d-40a2-a46e-eea04a625a96'></a>

which are the \epsilon = 0 limiting problems on the slow and fast time scale, respectively. The equation $f(x, y, 0) = 0$ defines the critical manifold $S$ on which the reduced problem (7) acts as a dynamical system. On the other hand, the critical manifold $S$ is a manifold of equilibria of the layer problem (8). A point $(x_0, y_0) \in S$ is normally hyperbolic if the Jacobian $\frac{\partial f}{\partial x} (x_0, y_0, 0)$ has no eigenvalues on the imaginary axis. Due to results by Fenichel (1979), normally hyperbolic pieces of critical manifolds perturb smoothly to locally invariant slow manifolds $S_\epsilon$ for $\epsilon$ sufficiently small. The flow on the slow manifold $S_\epsilon$ is a smooth perturbation of the reduced problem on $S$. Moreover, the slow manifold has stable and unstable manifolds, which have a smooth invariant foliation by fibers, which are a smooth perturbation of stable and unstable manifolds of $S$ for the layer problem (8). The essence of the geometric approach is that Fenichel theory allows to obtain (under suitable assumptions) orbits of a singularly perturbed system (5) as perturbations of singular orbits consisting of pieces of orbits of the reduced problem (7) and of the layer problem (8). For more details and examples we refer to the literature cited above.

<a id='c4307f86-7c7d-4b23-88a9-a737790e3506'></a>

Interesting dynamics may occur when the critical manifold S has a non-trivial geometry, e.g., a folded structure, where attracting and repelling parts of the critical manifold are separated by folds. Such folded structures of critical manifolds give rise to a jumping behavior of solutions, i.e., after reaching a fold point solutions jump to another attracting part of the critical manifold by following approximately orbits of the layer problem (8). By repeating this process a closed loop may be formed leading to a relaxation oscillation as e.g., in the classical van der Pol oscillator. A substantial difficulty in the analysis of system (5) are fold points of the critical manifold and other points, where normal hyperbolicity of the critical manifold is lost. At these points Fenichel theory fails, i.e., the existence of slow manifolds under ε-perturbations is not guaranteed. More recently, it has become clear how to extend geometric singular perturbation theory beyond non-hyperbolic points. The answer came with the pioneering work by Dumortier and Roussarie (Dumortier and Roussarie 1996) in which the blow-

<a id='3fd3300c-e8ef-4498-a8f1-a9498c2b7baf'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol in black, positioned to the left of the company name "Springer" written in a simple, sans-serif font.::>

<!-- PAGE BREAK -->

<a id='9b9e7d64-e65a-44b8-a231-1e4366194a58'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='3906d459-d575-4b57-affc-b517128249e6'></a>

1345

<a id='0a28a2dc-03f6-4761-a158-86c3b709ba21'></a>

up method has been introduced. The blow-up method has proven to be an effective tool in the geometric analysis of singularly perturbed equations near non-hyperbolic points (Krupa and Szmolyan 2001). For an introduction to the blow-up method and references to a large number of its applications we refer to (Kuehn 2015).

<a id='ee771bca-20a8-45ff-8680-969e8f710dfa'></a>

In the system (5) there exists a clear separation into slow and fast variables, i.e., y and x. However, singular perturbation problems without such a separation into slow and fast variables arise frequently in applications. Mathematically such problems are governed by a differential equation

<a id='c9cfbf38-cb47-46ad-8752-0e0c3ab9ab5a'></a>

u' = F(u, ε), u ∈ R^(n+m), (9)

<a id='cb6ef5d7-3749-48b2-816e-426e88b08920'></a>

which for ̣ = 0 has an _m_-dimensional manifold _S_ of equilibria. The corresponding
layer problem is given by

<a id='32aec5d8-4156-4ae1-bc2e-c432cb6e4ab9'></a>

u' = F(u, 0), u \in R^{n+m},                                                                   (10)

<a id='aa53d000-dda9-4dea-92c0-72011a913180'></a>

with the critical manifold S, i.e., in general all variables are fast away from the critical manifold. Under the assumption of normal hyperbolicity of S, all the results from the standard case carry over, i.e., a reduced problem on S can be defined, S perturbs smoothly to a slow manifold Sε, and the slow manifold has stable and unstable manifolds, which have a smooth invariant foliation by fibers, which are a smooth perturbation of stable and unstable manifolds of S for the layer problem (10). A point p ∈ S is normally hyperbolic, if ∂F/∂u (p, 0) has n eigenvalues off the imaginary axis in addition to an eigenvalue zero with multiplicity m, corresponding to the tangent space of S. Such problems are discussed in (Gucwa and Szmolyan 2009; Kosiuk and Szmolyan 2011), where it is shown that suitable rescalings combined with the blow-up method and Fenichel theory allow a detailed analysis.

<a id='73f12b3c-a766-4245-b3ed-095b8f95ba85'></a>

We will show that the auxiliary system (3) is a singular perturbation problem of this more general type where the singular perturbation parameter is the parameter ε corresponding to the small Michaelis constants. We will demonstrate that the slow-fast nature of the auxiliary system allows a complete analysis of the dynamics. It turns out that the critical manifold $S$ consists of four planes $S^1$, $S^2$, $S^3$, and $S^4$ corresponding to $M = 0$, $X = 0$, $M = 1$, and $X = 1$, respectively. Each of these planes changes its stability at a non-hyperbolic line $l_C$, $l_M$, $l^C$, and $l^M$ given by $C = C^*$, $M = M^*$, $C = C^*$, and $M = M^*$, respectively; see Fig. 5. In addition, the planes, which build up the critical manifold $S$, intersect along four non-hyperbolic lines called edges. The edges $l_e := S^1 \cap S^2$ and $l^e := S^3 \cap S^4$ will be particularly important.

<a id='722533e9-259a-42d0-8d4a-b689fa1be9d4'></a>

Such self-intersections of critical manifolds are another common phenomenon in slow-fast systems corresponding to transcritical or pitchfork singularities of the critical manifold. In these situations the critical manifold consists of two intersecting branches and a change of stability along the branches of S considered as steady states of the layer problem occurs at the intersection. Hence, singular perturbation problems of this type are often referred to as problems with exchange of stability. Intuitively, one would expect a transition from slow motion along one attracting branch of the corresponding slow manifolds to slow motion along another attracting branch to occur.

<a id='39039078-4745-4d2d-818e-29f22d8007d9'></a>

<::logo: Springer
Springer
The logo features a stylized knight chess piece next to the word "Springer" in black text.::>

<!-- PAGE BREAK -->

<a id='07cefd23-1caa-4642-8d36-cf4ac97ed525'></a>

1346

<a id='5b0cb439-d405-437c-a09b-5193cc4a182b'></a>

I. Kosiuk, P. Szmolyan

<a id='173edf87-4602-489e-b810-e13cd22e8768'></a>

However, more complicated dynamics is also possible, e.g., connections between attracting branches of the slow manifolds might not exist, or canard solutions following for a while a repelling branch of the slow manifold might occur. These phenomena have been analyzed in some detail by different approaches (Krupa and Szmolyan 2001; Lebovitz and Schaar 1975).

<a id='f9b1938e-fcbb-4486-8681-a8a9c0979330'></a>

It turns out that in the auxiliary system (3) a direct transition between the attracting parts of the critical manifold is not possible. Instead, we are able to identify a singular cycle, see Fig. 9, the half of which consists of
1. slow motion in the attracting part of S¹ towards the (non-hyperbolic) edge lₑ,
2. very slow drift along the edge lₑ,
3. slow motion in the attracting part of S² to a point p_f on the non-hyperbolic line l_M
4. and a fast jump from p_f to the attracting part of the plane S³.

<a id='7e019739-def6-48f8-b863-dcfb3862e37a'></a>

The second half of the cycle is generated in a similar manner.
In the following we refer to this new phenomenon of slow drift along the edge $l_e$
as "delayed exchange of stability". We will prove that this generates relaxation oscil-
lations of a new type for $\varepsilon$ small. The analysis of the dynamics close to the edges is
based on the blow-up method. A blow-up transformation is a sophisticated coordinate
transformation on the extended $(X, M, C, \varepsilon)$ phase space, which can be compared
to a magnifying glass. In the original coordinates some properties of the dynam-
ics of the system may be invisible (or degenerate) for $\varepsilon = 0$ but become visible
(or regular) when the system is transformed to a new space called the blown-up
space.

<a id='50ab271b-c3ab-45dd-b1b2-efd7c3b52f15'></a>

In the auxiliary system of the mitotic oscillator problem the nonhyperbolic edges $l_e \times \{0\}$ and $l^e \times \{0\}$, and the degenerate lines $l_M \times \{0\}$ and $l^M \times \{0\}$ are blown-up to cylinders by rewriting the original $(X, M, C, \varepsilon)$ variables in suitable cylindrical variables. Next the dynamics in the blown-up space is analyzed. The geometry and the dynamics in the blow-up of the edge $l_e \times \{0\}$ is shown schematically in Fig. 15. Note that this figure is a three-dimensional caricature of a four-dimensional manifold.

<a id='8aa12359-9341-4a10-8c5a-c8d73418251f'></a>

The planes shown in blue correspond to the two-dimensional critical manifolds X = 0 and M = 0 on which the reduced flow is defined. The edge $l_e$ has been blown-up to the cylinder shown in orange. Within this cylinder we find a (previously invisible) one-dimensional attracting critical manifold $N^0$ shown in purple. The reduced flow on $N^0$ is upwards corresponding to the accumulation of cyclin C. At the threshold value $C^*$ the critical manifold $N^0$ connects to the plane X = 0 and the variable M begins to increase by following the reduced flow. This corresponds to crossing the threshold for activation of cdc2 kinase M. This singular limit, i.e., $\varepsilon$ = 0 dynamics, is sufficiently nondegenerate to carry out a perturbation analysis for 0 < $\varepsilon$ << 1 and to prove the existence of an attracting limit cycle of the auxiliary system (3) close to the singular cycle.

<a id='f8e60bcf-e5a2-4dec-a017-00b6e3135b2e'></a>

Recall that the mitotic oscillator (2) and the auxiliary system (3) have the same orbits. Thus, the existence of the limit cycle of the mitotic oscillator (2) follows.

<a id='6b9f56ca-282b-448a-929a-5f9d0b6fd7f9'></a>

**Main result:** For ε sufficiently small there exists a locally unique strongly attracting limit cycle of the mitotic oscillator (2). The geometry and structure of the cycle is in excellent

<a id='3c07b5b5-72a5-406e-a671-251f614461d1'></a>

<::logo: Springer
Springer
The logo features a stylized knight chess piece next to the word "Springer" in black text.::>

<!-- PAGE BREAK -->

<a id='7910eebd-1396-41a9-b145-adf47213effd'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='fda5e838-1da2-4813-8343-04bc0ce6b213'></a>

1347

<a id='c46020f0-80a8-4f99-9e52-91f0c1513521'></a>

agreement with the results obtained by numerical simulations, see Figs. 3 and 4. The novel mathematical mechanisms generating the limit cycle and the switching behaviour described in the paragraph following the equations (2) are revealed and fully understood by the geometric and asymptotic analysis.

<a id='d1fd6787-185c-4d24-9f7e-8216e4ce5e71'></a>

_Remark 4_ Our analysis and numerical simulations strongly indicate that the limit cycle is the only periodic solution of the system, which attracts all the solutions except the unique unstable equilibrium.

<a id='9336e34a-e17c-429c-afd6-8c1675fb5873'></a>

In addition, our approach leads to the following results and conclusions:

1. The existence of a mathematically novel type of oscillations in the mitotic oscillator model (2) corresponding to a novel type of relaxation oscillations in the auxiliary system (3).
2. Better understanding of dynamical effects related to ultrasensitivity in phosphorylation-dephosphorylation cycles by utilizing their hidden multiple-time structure.
3. Identifying problem-adapted slow-fast decompositions and the understanding of several simpler limiting problems leads to good approximations of the full system, which already capture the essential dynamics.
4. Fenichel theory and geometric desingularization based on the blow-up method are well-suited for the rigorous analysis of this and related problems.
5. Equation (1) and similar systems have been widely utilized as modules in cell cycle models (Gérard and Goldbeter 2011, 2012; Tyson 1991; Tyson et al. 2001).

Therefore, we feel that the tools used and developed in this work will be useful in the on-going and planned mathematical analysis of such systems.

<a id='134fa8ef-4dc8-4406-8e84-9a99db11bcab'></a>

## 1.3 Outline of the paper
This paper is organized as follows. In Sect. 2 we give a slow-fast analysis of the auxiliary system (3) and identify the mechanisms leading to the oscillatory behaviour. In particular, we discuss in detail the dynamics in the \u03b5 = 0 singular limit. The proof of the main result, i.e., the existence of an attracting periodic orbit, is given in Sect. 2.4. In Sect. 3 we carry out the blow-up analysis of the non-hyperbolic edge l\u208a \u00d7 {0} needed for the proof. We conclude in Sect. 4 with a discussion and outlook.

<a id='2aac17da-dfbc-43d8-9bd6-6e49d35f0d8a'></a>

# 2 Geometric singular perturbation analysis
In this section we analyze the slow-fast structure of the auxiliary system (3) and identify the singular cycle for ε = 0, which persists as the limit cycle for ε small.

<a id='24a26be7-f3b1-4f15-b930-e65f439440a7'></a>

## 2.1 Layer problem and critical manifold
Setting ̣ = 0 in (3) gives the layer problem

<a id='2db6a181-5288-44fb-8d5b-ad9e4b9ef726'></a>

<::logo: Springer
Springer
The logo features a stylized knight chess piece in black next to the company name.::>

<!-- PAGE BREAK -->

<a id='88a369d8-3701-4670-858d-1cadfe906110'></a>

1348

<a id='55ca81a3-6711-4091-9461-95148d37fc7b'></a>

I. Kosiuk, P. Szmolyan

<a id='bca63a79-b149-43ba-9003-6596225c57ff'></a>

$$\frac{dX}{d\tau} = \left(M - \frac{7}{10}\right) F_0(X, M),$$
$$\frac{dM}{d\tau} = \left(\frac{6C}{1 + 2C} - \frac{3}{2}\right) F_0(X, M),$$
$$\frac{dC}{d\tau} = \frac{1}{4}(1 - X - C) F_0(X, M) \quad (11)$$

<a id='f5bd8d4b-b5c0-454f-966a-a52503955ffe'></a>

with

<a id='05d2d502-173c-4509-8c77-dda0df8edd60'></a>

F0(X, M) = (1 - M)(1 - X)MX.

<a id='50f3ba8a-6a1a-47db-b596-58c3cbcb06ea'></a>

The critical manifold defined as the set of equilibria of the layer problem consists of four planes, defined by _M_ = 0, _X_ = 0, _M_ = 1, _X_ = 1, which we denote by S¹, S², S³, S⁴, respectively, and the isolated equilibrium point (_X_, _M_, _C_) = (½, ⁷⁄₁₀, ½) denoted by _P_, see Fig. 5.

<a id='0336a4ba-a9c4-4aa0-9129-88130ba623eb'></a>

Remark 5 The equilibrium point _P_ plays no role in the analysis; however, we include it for completeness.

<a id='4c48df57-91d7-4199-9274-b8ea843dfcc8'></a>

We summarize the stability properties of points in S in the following lemma. Recall that for the parameter values considered the threshold values of C and M are C* = 0.5 and M* = 0.7.

<a id='5b602370-09e6-4b97-9475-9abb43e9b89b'></a>

Lemma 1 The critical manifold S of the layer problem (11) has the following prop-erties: S¹ is attracting for C < C* and repelling for C > C*; S² is attracting for<::3D diagram illustrating the critical manifold S. The diagram shows a cube with axes labeled C, M, and X. The C-axis ranges from 0 to 1, with an additional point C*. The M-axis ranges from 0 to 1, with an additional point M*. The X-axis ranges from 0 to 1. The cube is divided into several regions and surfaces. Surfaces are labeled S¹, S², S³, S⁴. Various lines are highlighted in orange and labeled: l_M, l_C, l^C, l^M, l_e, l^e. These lines and surfaces delineate different regions within the 3D space.Fig. 5 Critical manifold S = S¹ ∪ S² ∪ S³ ∪ S⁴, non-hyperbolic lines l_C, l_M, l^C, l^M, and edges l_e, l^e: diagram::>

<a id='d4b5a8ce-f388-45a1-997b-4a8a2376a262'></a>

<::Springer logo with a knight chess piece icon
: figure::>

<!-- PAGE BREAK -->

<a id='af21dab1-03e2-42ee-b3d4-c9092625ecf1'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='e56975ed-58d9-45d8-8d5a-0e94f5ce71f9'></a>

1349

<a id='f36cf2ef-a20b-44dd-b26b-8194c7df6038'></a>

M < M* and repelling for M > M*; S³ is attracting for C > C* and repelling for C < C*; S⁴ is attracting for M > M* and repelling for M < M*; The lines $l_C \in S^1$, $l_M \in S^2$, $l^M \in S^3$, and $l^C \in S^4$, given by C = C*, M = M*, C = C*, M = M*, respectively, and the four edges, in particular, $l_e := S^1 \cap S^2$ and $l^e := S^3 \cap S^4$, are non-hyperbolic; Equilibrium P is of saddle-focus type.

<a id='48c24240-01d5-453c-bc58-4619a310931a'></a>

*Proof* Computations, e.g., the eigenvalues of the linearization of system (11) at points in S  9, i.e., for M = 0, are given by

<a id='2dd3bad2-90cb-457f-8d95-ebb9da0d62f1'></a>

λ₁ = 0, λ₂ = (6C)/(1 + 2C) - (3)/(2), λ₃ = 0.

<a id='f0e7dc5e-d565-4efc-af21-ad820a0f5ed4'></a>

Hence, λ₂ changes its sign at C = C* and S¹ is attracting for C < C* and repelling for C > C*.

<a id='5c65be09-c3b8-4bc4-82b3-57072be95fa4'></a>

We denote the attracting (repelling) part of $S^i$ by $S_a^i$ ($S_r^i$) for $i = 1,..., 4$.
Away from the critical manifold $S$ all variables evolve on the fast time scale $\tau$ and the orbits of the layer problem are identical with the orbits of the system

<a id='64b7cf85-cdbc-41cd-91b1-ca4e10ef6b8e'></a>

dX/dτ = (M - 7/10)

dM/dτ = (6C / (1 + 2C) - 3/2)

dC/dτ = 1/4 (1 - X - C)                                                (12)

<a id='db45db92-96ab-4244-a414-a1d7baae370c'></a>

obtained by dropping the non-zero factor $F_0(X, M)$.

<a id='b2f1680b-e2d4-43eb-ae20-272995fa5879'></a>

_Remark 6_ Note that the system (12) is the limit of the mitotic oscillator (2) as ε → 0 for (_X_, _M_) ∈ (0, 1)².

<a id='647f932e-25f6-4261-ae52-7984b687a541'></a>

## 2.2 Reduced problem, slow manifolds, and slow dynamics

Any compact subset of the critical manifold $S$ that does not contain the non-hyperbolic lines is normally hyperbolic. To such normally hyperbolic parts of $S$ (away from the edges and away from the non-hyperbolic lines $l_C$, $l_M$, $l^C$, $l^M$, respectively), Fenichel theory applies. In particular, the theory implies that these parts perturb to slow manifolds, which lie within $O(\varepsilon)$ of $S$ and can be described as graphs over $S$.

<a id='b4c38491-769f-4faa-b9eb-d546567b702c'></a>

Remark 7 In the following we compute the slow manifolds and analyze the reduced flows in the planes _M_ = 0 and _X_ = 0. Note that for our purposes it is sufficient to concentrate on the attracting parts of the critical manifold _S_. Similar results hold for the planes _M_ = 1 and _X_ = 1, see (Kosiuk 2012) for details.

<a id='7a97d25e-bbd2-4b62-ba89-eb36815c7443'></a>

Lemma 2 For small δ > 0 there exist ε₀ > 0 and a smooth function h¹_ε(X, C) defined on I_a := [δ, 1 − δ] × [δ, ½ − δ] such that the graph

<a id='265425d0-cc65-40db-be8b-58d52c4158ae'></a>

S^1_{a,\varepsilon} = \{(X, M, C) : M = h^1_{\varepsilon}(X, C), (X, C) \in I_a\}

<a id='d8b8a624-a500-4df5-9d9f-fed0fc6e06b5'></a>

<::Springer logo with a knight chess piece
: figure::>

<!-- PAGE BREAK -->

<a id='2c732930-88eb-43ed-be2d-f7c307c89404'></a>

1350

<a id='0cc61442-6e6f-4261-a7c4-4f61478560fc'></a>

I. Kosiuk, P. Szmolyan

<a id='1a67adc0-ea7f-40cd-ae68-50cd7cbdc194'></a>

is a locally invariant attracting slow manifold of system (3) for ε ∈ (0, ε₀]. The function h^1_ε has the expansion

<a id='d26a0d2a-c5a5-4bd3-8dc1-8bbae7e534f0'></a>

h^1_ε(X, C) = \frac{-4C}{2C - 1} ε + O(ε^2).

<a id='5feff924-50a4-40d5-911d-feed7f6d47bf'></a>

Proof The existence of $S_{a,\varepsilon}^1$ as a graph over $I_a$ follows from Fenichel theory. Since the function $h_\varepsilon^1(X, C)$ is smooth it has an expansion

<a id='87e8b586-986e-4309-a17c-e9839dc1ecf0'></a>

h^1_{ε}(X, C) = εη(X, C) + O(ε^2).

<a id='06595c14-c03f-4674-831b-549f92df8b44'></a>

By inserting this expansion into (3), the invariance of the slow manifold S^1_{a,ε} implies

<a id='ba156c3c-e555-4566-9fd5-8725b536a77a'></a>

$$\varepsilon \left( \frac{\partial \eta}{\partial X} \frac{dX}{d\tau} + \frac{\partial \eta}{\partial C} \frac{dC}{d\tau} \right) + O(\varepsilon^2) = \varepsilon \left( \frac{6C}{1+2C}(1+\eta) - \frac{3}{2}\eta \right) (1-X)X + O(\varepsilon^2). $$

<a id='45f3e613-b103-496d-8d60-ec69d0f95313'></a>

Since $\frac{dX}{d\tau}|_{M=\eta(X,C)} = O(\varepsilon)$ and $\frac{dC}{d\tau}|_{M=\eta(X,C)} = O(\varepsilon)$, comparing coefficients of powers of $\varepsilon$ implies

$0 = \left(\frac{6C}{1+2C}(1+\eta(X, C)) - \frac{3}{2}\eta(X, C)\right)(1-X)X,$

<a id='be74c3b3-8d93-409e-b8f7-435d5510f162'></a>

which yields η(X, C) as given in the lemma.

<a id='45da80bb-69b6-46e5-8c57-378d49ebf46d'></a>

For the plane X = 0 we obtain a similar result.

<a id='77d16efd-662e-49a7-ae3c-685677ce37e2'></a>

**Lemma 3** For small δ > 0 there exist ε₀ > 0 and a smooth function h²_ε(M, C) defined on J_a := [δ, 0.7 – δ] × [δ, 1 – δ] such that the graph

<a id='93128f82-9997-43d5-9dfe-aae2a9acf287'></a>

S²_a,ε = {(X, M, C) : X = h²_ε(M, C), (M, C) ∈ J_a}

<a id='d29e0161-a8d2-4bb8-b290-754d26329ac0'></a>

is a locally invariant attracting slow manifold of system (3) for ε ∈ (0, ε0]. The function has the expansion
h_ε^2(M, C) = \frac{M}{0.7 - M}\varepsilon + O(\varepsilon^2).

<a id='425662a1-94b7-4a8a-880f-698084cfa93a'></a>

Remark 8

(i) The necessity to restrict the domains of definition of the slow manifolds described in the above theorems is also apparent from the singularity of the functions $h_\varepsilon^1$ and $h_\varepsilon^2$ at $C = C^*$ and $M = M^*$, respectively.

(ii) The repelling slow manifolds close to $S_\varepsilon^1$ and $S_\varepsilon^2$ are described by the same formulas as their attracting counterparts but lie in the non-physical parts of phase space $M < 0$ and $X < 0$, respectively.

<a id='2398c6a8-305c-4bfd-8a84-0decdb3a051b'></a>

We now turn to the analysis of the reduced flows in the planes $M = 0$ and $X = 0$.
By inserting the function $h^1_\varepsilon$ into system (3) written on the fast time scale $\tau$, we obtain

<a id='3ecb4ad8-b44e-488e-b0c9-c7673795d629'></a>

<::Springer logo with a knight chess piece icon and the word "Springer": figure::>

<!-- PAGE BREAK -->

<a id='8cdd1c4c-90a1-4f2c-9c63-75e0ccb7e61a'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='37938fc6-a605-4d9c-917c-4e6668437c0c'></a>

1351

<a id='23c0436e-add4-492a-bdd5-5d6e17e80cd9'></a>

<::plot: A 2D plot showing the flow of a reduced system on a critical manifold. The x-axis is labeled 'X' and ranges from 0 to 1, with intermediate labels 'x2' and 'x1'. The y-axis is labeled 'C' and ranges from 0 to 1, with an intermediate label 'C*'. A horizontal red line is present at C*. Multiple blue curves with arrows indicate the flow direction. Some arrows point right, and some point left. Two vertical cyan lines are also shown. Fig. 6 Flow of the reduced system (15) on the critical manifold S¹::>
$$X' = \varepsilon \frac{7X(1-X)(6C + 3)}{10(6C - 3)} + O(\varepsilon^{2}),$$
$$C' = \varepsilon \frac{(1 - X - C)(X - 1)X(6C + 3)}{4(6C - 3)} + O(\varepsilon^{2}), \tag{13}$$

<a id='c671cc3e-b436-4a24-a3ad-2eb53965ae11'></a>

The equations governing the slow dynamics on the slow manifold S¹_{a,ε} are computed by dividing out a factor of ε, which corresponds to switching to the slow time variable t = ετ. Hence, the slow flow on S¹_{a,ε} is governed by

<a id='2daf5c69-e965-4bb5-b109-fc7c3ee3220f'></a>

$$\dot{X} = \frac{7X(1-X)(6C + 3)}{10(6C - 3)} + O(\varepsilon)$$

$$\dot{C} = \frac{(1 - X - C)(X - 1)X(6C + 3)}{4(6C - 3)} + O(\varepsilon) \quad (14)$$

<a id='fe9c3bc3-997f-41c3-bb95-1cab3fd52ca5'></a>

where · denotes differentiation with respect to the slow variable t. By setting ε = 0
we obtain the reduced flow on $S_a^1$, which is governed by

<a id='376aa3be-6060-4816-b3fe-272e5ee2002f'></a>

Ẋ = 7X(1 - X)(6C + 3)
---––––––––––––––––––––––––––
10(6C - 3)

Ċ = (1 - X - C)(X - 1)X(6C + 3) (15)
---––––––––––––––––––––––––––
4(6C - 3)

<a id='9ffb4fca-1b38-41eb-8229-5ecfb984d0e7'></a>

System (15) is singular at the line C = C*, i.e., the flow is not defined there. The lines X = 0 and X = 1, shown in blue in Fig. 6, are lines of equilibria. The line X = 0 is attracting for C < C* and repelling for C > C*, whereas the line X = 1 is repelling for C < C* and attracting for C > C*, see Fig. 6.

<a id='b540f1ed-4e9b-4abe-8b83-8ad3ac082009'></a>

Remark 9 Note that the lines X = 0 and X = 1 of equilibria of system (15) do not correspond to equilibria of system (2). In some sense they are an artefact of the multiplication transforming system (2) into (3).

<a id='93e7430d-22c8-429a-b339-c8b8aa9c85db'></a>

<::Springer logo with a knight chess piece icon: figure::>

<!-- PAGE BREAK -->

<a id='a293ecfe-ffdf-4670-8523-1984988cd71a'></a>

1352

<a id='087f6091-35b7-42fc-b5b8-f89d25018c29'></a>

I. Kosiuk, P. Szmolyan

<a id='3966620e-090b-4b5c-b95b-f195f0930273'></a>

The orbits of the reduced flow can be obtained from the desingularized system

<a id='44d69607-3736-4ce6-9921-21e090f5d3a0'></a>

Ẋ = -7/10
Ċ = 1/4(1 - X - C) (16)

<a id='91035e22-77b4-4aa7-a151-e23ba15397ff'></a>

which is obtained from (15) by dividing out the factor X (X - 1)^((6C+3)/(6C-3)). The resulting equations (16) can be integrated explicitly.

<a id='02b2c6d9-9536-4e7e-86f1-adff236c2eda'></a>

For X ∈ (0, 1) systems (15) and (16) have the same phase portraits on the lower part of the plane M = 0, i.e., for C < C*. On the upper part, for C > C*, the direction of time has to be reversed in the phase portrait of system (16) in order to obtain the phase portrait of the reduced system (15). For our purposes it suffices to study the flow of system (15) in the lower part of the M = 0 plane, away from the line lC, and away from the lines of equilibria, which are non-hyperbolic for the layer problem (11).

<a id='36bf3c99-f90e-4b82-9506-ba63a812fa66'></a>

Lemma 4 The reduced flow (15) on $S_a^1$ and the slow flow (14) on $S_{a,\epsilon}^1$, respectively, are contracting in C, i.e., the induced map between sections $X = x_1$ and $X = x_2$ with $0 < x_2 < x_1 < 1$ contracts the variable C.

<a id='7e331ba3-30a2-4b1a-9640-482a66809d35'></a>

Proof For the reduced flow the lemma follows from a direct computation based on
(16). Clearly, the claimed contraction property persists for the slow flow for \u03b5 small.

<a id='45617dd4-8f52-4abf-940d-fae889aed086'></a>

Analogously, by inserting the function $h_\varepsilon^2$ into (3) and dividing out a factor of $\varepsilon$, which corresponds to switching to the slow time scale $t = \varepsilon\tau$, we obtain the equations governing the slow flow on $S_{a,\varepsilon}^2$. By setting $\varepsilon = 0$ we obtain the reduced flow on the critical manifold $S_a^2$, i.e., in the plane $X = 0$. Namely,

<a id='760fdc16-b143-4c7b-bd0e-485bd15ef167'></a>

Ṁ = (6C - 3)M(1 - M) / [2(2C + 1)(0.7 - M)]
Ċ = (1 - C)(1 - M)M / [4(0.7 - M)]

(17)

<a id='daf211b7-bc51-4c31-a289-01e9844d77be'></a>

System (17) has two lines of equilibria, i.e., M = 0 and M = 1, and is singular at M = M*. To analyze the dynamics of the reduced system (17), we divide out the factor $\frac{M(M-1)}{M-0.7}$ in system (17), and obtain

<a id='b7cc7f6f-d4a9-4c14-98db-5d8590c51498'></a>

M = (6C - 3) / 2(2C + 1)
C = (1/4)(1 - C)
(18)

<a id='147e8c9e-c1d3-44b5-b2b0-1f9ad517acf3'></a>

These equations can be solved explicitly. For $M \in (0, 1)$ systems (17) and (18) have the same phase portraits for $M < M^*$. The phase portrait of the reduced system (17) on $S_r^2$ is obtained by changing the direction of the flow in system (18) for $M > M^*$, see Fig. 7. It turns out it is sufficient to consider the reduced flow on $S_a^2$ for $C > C^*$.

<a id='c621c847-ea49-4868-aaac-0abfb439e29d'></a>

Lemma 5 For C > C* the reduced flow (17) on S_a^2 has the following properties:

<a id='8ce04234-a898-4ce9-a8b1-a4d68d357392'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol in black, positioned to the left of the company name "Springer" written in a simple, sans-serif font.::>

<!-- PAGE BREAK -->

<a id='e07c9f88-c0e4-474b-9a19-bbf86698954d'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='71c7447f-1aae-4bf9-aaae-7ed4b5606594'></a>

1353

<a id='44975821-2959-4222-b002-b4bd19d0af94'></a>

<::Phase portrait showing reduced flow on a critical manifold. The x-axis is labeled 'M' and ranges from 0 to 1, with intermediate tick marks at 'm1', 'm2', and 'M*'. The y-axis is labeled 'C' and ranges from 0 to 1, with an intermediate tick mark at 'C*'. Blue curved lines with arrows indicate the flow direction. There are thick blue vertical boundary lines at M=0 and M=1, and a thick red vertical line at M=M*. Two cyan vertical line segments are present, one above m1 and one above m2. The flow generally moves from left to right, with some trajectories curving up and others curving down.: diagram::>
7 Reduced flow on the critical manifold S² and non-hyperbolic line lM

<a id='bc35a978-11b8-4ae5-8216-fd4b513487ae'></a>

1. The reduced flow on S² is directed towards the line M = M* and solutions of the reduced flow on S_a² and S_r² reach the line l_M in finite forward time.
2. The reduced flow (17) on S_a² and the corresponding slow flow on S_a,ε² are contracting in C, i.e., the induced map between sections M = m_1 and M = m_2 with 0 < m_1 < m_2 < M* contracts the variable C.

<a id='db9cba43-a230-40bd-83cc-5c7b0acf1863'></a>

Remark 10 The behaviour of system (3) close to the line $l_M$ for C > C* is very similar to the behaviour of standard slow-fast systems with two slow variables and one fast variable near a generic fold line (Grasman 1987; Mishchenko and Kh 1980; Szmolyan and Wechselberger 2004). In the standard situation the reduced flow on the attracting part of a folded critical manifold reaches the fold line in finite time. There a jump along a straight unstable fiber of the corresponding layer problem occurs. A detailed description of the dynamics near fold lines for $\varepsilon$ > 0 small based on the blow-up method has been given in (Szmolyan and Wechselberger 2004).

<a id='8b61945c-f43b-42a6-9b5f-8a40f28e6ada'></a>

The critical manifold S of system (3), see Fig. 7, can be viewed as such a standard folded critical manifold which has been straightened out by a suitable diffeomorphism. This clearly leads to the curved fibers of the layer problem (11), see Fig. 9. Hence, the results of (Szmolyan and Wechselberger 2004) can be applied there.

<a id='31003466-d06c-474d-be07-b1dda2f2b3a0'></a>

## 2.3 Singular cycle

One goal of the analysis of system (3) in the singular limit \$\varepsilon = 0\$ is to identify a singular cycle, i.e., a closed curve consisting of alternating segments of the critical manifold \$S\$ and orbits of the layer problem. Note, however, that just from inspection of the layer problem and the reduced problems, it is not clear how to define a singular cycle, which would be a good candidate to obtain relaxation oscillations. The reason for this is that at the moment we have no valid description of the dynamics close to the edges \$l_e\$ nor \$l^e\$. Moreover, we need to understand better the dynamics of system (3) in a neighbourhood of the non-hyperbolic lines \$l_M\$ and \$l^M\$.

<a id='052bd486-c9d1-420c-92bb-351cf79032dc'></a>

<::A logo with a knight chess piece icon followed by the word "Springer".
: figure::>

<a id='d5fadcfa-997b-4b80-9033-cacf5b2f16b1'></a>

Fig.

<!-- PAGE BREAK -->

<a id='b8fffbb3-334f-41a4-95b4-4f3af8833c70'></a>

1354

<a id='c30a97c6-5798-4b14-a072-a09f4e38571f'></a>

I. Kosiuk, P. Szmolyan

<a id='a37467eb-5329-4539-ad8e-2aed286a2f13'></a>

<::diagram: Upper picture of Fig. 8 showing reduced flows and singular cycle Γ₀. This diagram illustrates the planes M = 0 and X = 0 intersecting along the edge lₑ. The horizontal axis is X, ranging from 1 to 0, and the vertical axis is M, ranging from 0 to 1, with a mark at M*. The diagram shows regions S¹ᵣ, S¹ₐ, S²ₐ. Blue arrows indicate reduced flows on S¹ and S². Orbits of the layer problem are shown in green. The components of the singular cycle Γ₀ are drawn as thick curves: ω₁ (blue, starting from pᵣ), ω₈ (blue, connecting qₑ to pₑ), ω₇ (blue, connecting pₑ to p₁), and ω₆ (blue, forming a loop around p₁). Points p₁, pₑ, qₑ, and pᵣ are marked. Double green arrows indicate hyperbolic behaviour of the layer problem. Lines lₑ (vertical at X=0), lᶜ (horizontal at C*), and lᴹ (vertical at M*) are shown.::>

<::diagram: Lower picture of Fig. 8 showing reduced flows and singular cycle Γ₀. This diagram illustrates the planes M = 1 and X = 1 intersecting along the edge lₑ. The horizontal axis is X, ranging from 0 to 1, and the vertical axis is M, ranging from 1 to 0, with a mark at M*. The diagram shows regions S³ₐ, S⁴ₐ, S³ᵣ, S⁴ᵣ. Blue arrows indicate reduced flows on S³ and S⁴. Orbits of the layer problem are shown in green. The components of the singular cycle Γ₀ are drawn as thick curves: ω₂ (blue, starting from p₃), ω₃ (blue, connecting p₃ to pₑ), ω₄ (blue, connecting pₑ to qₑ), ω₅ (blue, connecting qₑ to pᶠ), and ω₆ (blue, forming a loop around pᶠ). Points p₃, pₑ, qₑ, and pᶠ are marked. Double green arrows indicate hyperbolic behaviour of the layer problem, while non-hyperbolic behaviour is indicated by a single green arrow (near ω₂). Lines lᶜ (horizontal at C*), lₑ (vertical at X=1), and lᴹ (vertical at M*) are shown.::>

Fig. 8 Reduced flows and singular cycle Γ₀ := ω₁ ∪ ω₂ ∪ ω₃ ∪ ω₄ ∪ ω₅ ∪ ω₆ ∪ ω₇ ∪ ω₈.

<a id='0e482510-66d4-4fd8-b759-4af56741f534'></a>

A full description of the dynamics is obtained by carrying out the blow-up analysis in Sect. 3. Anticipating this we define the singular cycle Γ₀ of system (3) for ε = 0, half of which consists of
1. slow motion in the attracting part of S¹ (the plane M = 0) towards the (non-hyperbolic) edge lₑ,
2. very slow drift along the edge lₑ,
3. slow motion in the attracting part of S² (the plane X = 0) to a point p_f on the non-hyperbolic line l_M,
4. a fast jump from p_f to the attracting part of S³ (the plane M = 1).

<a id='2363fd54-f8af-47dd-be7b-cb47e78d019e'></a>

We will show that for small values of ε this leads to a phenomenon of delayed
exchange of stability mentioned in the introduction. More precisely, the construction
of the singular cycle Γ0 starts at the point qe = (0, 0, 1/2) ∈ le, see Figs. 8 and 9. At

<a id='c5486aca-9234-48a7-beaa-86f69705785f'></a>

<::Springer logo with a knight chess piece icon and the word "Springer": figure::>

<!-- PAGE BREAK -->

<a id='fa7dc78a-3fde-4b72-82be-826f9c31a5fb'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='3f956112-b804-46f5-be1b-1b1ff0c7ccdd'></a>

1355

<a id='4265c810-590d-4e90-a85a-28f48aa44541'></a>

<::figure: A 3D cube is depicted, representing a phase space with axes marked 0 and 1. The cube has labels 'M', 'C', and 'X' on its visible faces/edges. Inside and on the surfaces of the cube, a singular cycle Γ₀ is illustrated as a series of connected paths (orbits) labeled ω₁ through ω₈. Specific points along these paths are marked as p_f, p_l, p_3, p_e, q_e, p^e, q^e, and p^f. Two vertical lines, lᴹ and l′ᴹ, are shown in orange. The orbits ω₁, ω₃, ω₅, and ω₇ are colored blue and represent orbits of the reduced flows. The orbits ω₂ and ω₆ are colored green and represent orbits of the layer problem. The orbits ω₄ and ω₈ are colored purple and indicate very slow motion along non-hyperbolic edges. The non-hyperbolic lines lᴹ and l′ᴹ are colored orange. This visual represents a Singular cycle Γ₀ := ω₁ ∪ ω₂ ∪ ω₃ ∪ ω₄ ∪ ω₅ ∪ ω₆ ∪ ω₇ ∪ ω₈ in ℝ³.:>

**Fig. 9** Singular cycle Γ₀ := ω₁ ∪ ω₂ ∪ ω₃ ∪ ω₄ ∪ ω₅ ∪ ω₆ ∪ ω₇ ∪ ω₈ in ℝ³. Orbits of the reduced flows ω₁, ω₃, ω₅, ω₇ are shown in *blue*, orbits of the layer problem ω₂, ω₆ are shown in *green*. Very slow motion ω₄, ω₈ along the non-hyperbolic edges are shown in *purple*. Non-hyperbolic lines lᴹ and l′ᴹ are shown in *orange*.

<a id='4415f765-3e05-491b-9a10-33253dfe1b88'></a>

this stage the choice of $q_e$ is motivated by the fact that this is the unique point on the edge $l_e$ where a transition from the critical manifold $S_a^1$ to the critical manifold $S_a^2$ seems to be possible, see the top picture in Fig. 8. Next we define points $p_f \in l_M$, $p_3 \in S_a^3$, $p^e \in l^e$, $q^e = (1, 1, \frac{1}{2}) \in l_e$, $p^f \in l_M$, $p_1 \in S_a^1$, and $p_e \in l_e$ in the following way: $p_f$ is the point where the orbit $\omega_1$ of the reduced problem on $S_a^2$ starting at $q_e$ intersects the line $l_M$, $p_f$ is connected to $p_3$ by a heteroclinic orbit $\omega_2$ of the layer problem (11), $p^e$ is the point where the orbit $\omega_3$ of the reduced problem on $S_a^3$ starting at $p_3$ intersects the edge $l^e$, $p^e$ is connected to $q^e$ by a segment $\omega_4$ of the edge $l^e$. Similarly, $\omega_5$ is a solution segment of the reduced flow on $S_a^4$ from $q^e$ to $p^f$, $\omega_6$ is the heteroclinic orbit of the layer problem (11) from $p^f$ to $p_1$, $\omega_7$ is a solution segment of the reduced problem on $S_a^1$ from $p_1$ to $p_e$; finally, $\omega_8$ is a segment of $l_e$ from $p_e$ to $q_e$. We define the singular cycle $\Gamma_0$ of system (3) for $\varepsilon = 0$ as

<a id='b626b33a-d157-4404-b5ba-89a3df1e41fa'></a>

Γ₀ := ω₁ ∪ ω₂ ∪ ω₃ ∪ ω₄ ∪ ω₅ ∪ ω₆ ∪ ω₇ ∪ ω₈. (19)

<a id='b0b13d7b-03f6-466e-a020-e63258695bda'></a>

This construction and the definition of the limit cycle Γ₀ is based on the following assumption that the orbit ω₂ limits in a point in S³ₐ, which is denoted by p₃, and the orbit ω₆ limits in a point in S¹ₐ, which is denoted by p₁. In Fig. 4 the orbits ω₂ and ω₆ are computed numerically, while the other orbits ωⱼ, j ≠ 2, 6 are known analytically. Since computing ω₂ and ω₆ is based on finite time calculations for the system (12), the validity of this assumption can be considered as being established.

<a id='0c7c88bb-8fc1-4d68-a1f5-889c79883ae7'></a>

Remark 11 A mathematically novel feature of the singular cycle $\Gamma_0$ is the slow drift along the edges $l_e$ and $l^e$ shown in purple. At this stage of the analysis the pieces $\omega_4$ and $\omega_8$ of the singular cycle $\Gamma_0$ do not carry any dynamics. Only the blow-up analysis in

<a id='7116be14-e108-4ebf-a42d-98bea37a7082'></a>

<::logo: Springer
Springer
The logo features a stylized black chess knight icon next to the word "Springer".::>

<!-- PAGE BREAK -->

<a id='df745832-b977-49b5-897b-c4c83501b137'></a>

1356

<a id='a4240d81-3314-4c75-ba9d-5e20580c6b63'></a>

I. Kosiuk, P. Szmolyan

<a id='fbb79069-ad0e-4bbc-99b5-f02e58a76f33'></a>

<::A 3D diagram shows a cube representing a phase space with axes labeled M, C, and X, each ranging from 0 to 1. Inside the cube, a singular cycle Γ₀ is depicted, consisting of blue and green curved paths with directional arrows. Several sections for the Poincaré map are shown as turquoise rectangular planes (Δ₁, Δ₂, Δ_in, Δ_out) intersecting the cycle. Vertical orange lines labeled M* are visible on two faces of the cube. Specific segments of the cycle are labeled ω₁ through ω₈, and a point on the cycle is labeled C*.::>Fig. 10 Singular cycle Γ₀ and sections for the Poincaré map

<a id='b97c9970-774d-4322-90a9-c866abf1dbaf'></a>

Sect. 3 will reveal that $\omega_8$ is associated with a very slow upward motion along the edge $l_e$; similarly, $\omega_4$ is associated with a very slow downward motion along the edge $l^e$.

<a id='2bfbf98b-e80e-4e56-aa19-7e7ebb27303f'></a>

## 2.4 Proof of the main result

Our main result follows by showing that the singular cycle $\Gamma_0$ persists as a relaxation cycle of the auxiliary system (3) for small values of $\varepsilon$.

<a id='0237a594-2c3f-4adc-93d7-a131ce58d7bd'></a>

**Theorem 1** Let Γ₀ be the singular cycle described above. Then there exists a locally unique attracting periodic orbit Γε of system (3) for ε sufficiently small, which tends to the singular cycle Γ₀ for ε → 0.

<a id='09dc4f0f-c578-4688-bc20-d2332d297e9e'></a>

The proof will be based on the construction of a suitable Poincaré map Π for the system (3) defined in a neighbourhood of Γ₀, whose fixed point gives the limit cycle for ε small. The Poincaré map Π is obtained as the composition of three different types of intermediate maps. The first type of maps describes contraction onto and transport along the attracting slow manifold S¹_a,ε (S³_a,ε). A second type of maps describes the dynamics close to the edge l_e (lᵉ) and is constructed for a system obtained by blowing-up this edge. The third type describes slow motion close to S²_a (S⁴_a), passage of the line l_M (lᴹ), and the fast jump to S³_a (S¹_a), and involves a blow-up of these lines. Based on the properties of the three types of maps we prove that for ε small the Poincaré map is a strong contraction and has an attracting fixed point corresponding to the limit cycle.

<a id='f13d9b6f-049e-4b91-8b94-6f839d835612'></a>

We start to prove Theorem 1 by choosing four sections Δ₁, Δin, Δout, and Δ₂,
as shown in Fig. 10, i.e., Δ₁ is transversal to ω₆, Δin is transversal to ω₇ ⊂ S¹ and
close to the edge *lₑ*, Δout is transversal to ω₁ ⊂ S² and close to the edge *lₑ*, Δ₂ is
transversal to ω₂. We denote the coordinates of the points *p₁* and *p₃* as (*X₁*, 0, *C₁*)

<a id='bd7a5f4e-5ecf-43b9-9ba7-3ff987314278'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol in black, positioned to the left of the company name "Springer" written in a simple, sans-serif font.::>

<!-- PAGE BREAK -->

<a id='08cff750-0456-45d6-8659-73c2acc94979'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='5911836d-f40f-48ff-b99a-c12afd4b6809'></a>

1357

<a id='59d3f10f-bf0c-4121-810c-da8e6553bd12'></a>

and ($X_3$, 1, $C_3$), respectively. We define the sections more precisely as

$\Delta_1 := \{(\delta_1, M, C) : (M, C) \in L_1\}$

$\Delta_{in} := \{(\delta, M, C) : (M, C) \in L_{in}\}$

$\Delta_{out} := \{(X, \delta, C) : (X, C) \in L_{out}\}$

$\Delta_2 := \{(\delta_2, M, C) : (M, C) \in L_2\}$

<a id='766f804d-f630-4d9d-bdc0-a6c392bc5403'></a>

where X₁ < δ₁ < 1, 0 < δ₂ < X₃, and δ > 0 is small, and L₁, Lᵢₙ, Lₒᵤₜ, and L₂ are suitable small rectangles, see Fig. 10. These sections are transversal to the singular cycle Γ₀ independently of ε and can be made arbitrary small. Since they are needed later, we define the following points: q₁ := Δ₁ ∩ ω₆, q₂ := Δᵢₙ ∩ ω₇, and q₃ := Δₒᵤₜ ∩ ω₁. The first half of the Poincaré map is defined as the composition of three maps:

πₐ : Δ₁ → Δᵢₙ (describing contraction onto and slow flow along the manifold S¹a,ε),
πₑ : Δᵢₙ → Δₒᵤₜ (describing passage of the edge lₑ),
π𝒻 : Δₒᵤₜ → Δ₂ (describing flow along S²a,ε and fast jump close to the line lₘ).

<a id='85561c5b-9dae-4d21-9fb7-078ef9ea6dd6'></a>

The properties of these maps are summarized in the following lemmas.

<a id='90441472-e57b-448f-a95c-ab4f91a04c28'></a>

Lemma 6 Fix \delta_1 > 0. If the section \Delta_1 is chosen small enough, there exists \varepsilon_0 such that the map

<a id='e722c8a1-dec8-4dae-a193-644c7db7b64e'></a>

$\pi_a : \Delta_1 \to \Delta_{in}, (M, C) \mapsto (\pi_a^M (M, C, \varepsilon), \pi_a^C (M, C, \varepsilon))$

<a id='bbda27d5-b34f-4777-9cf7-f8c3660e314e'></a>

is well defined and smooth for $\varepsilon \in [0, \varepsilon_0]$. Furthermore, the linearization $\frac{\partial\pi_a}{\partial(M,C)}(q_1)$ is uniformly bounded.

<a id='31d936f8-0a8a-496f-be96-416bbc136473'></a>

Proof The lemma is proven by treating the map $\pi_a$ as a perturbation of a corresponding map $\pi_{a,0}$ defined for $\varepsilon = 0$. The map $\pi_{a,0}$ is defined by projecting the section $\Delta_1$ onto $S_a^1$ along the orbits (stable fibers) of the layer problem and then following the reduced flow till the section $\Delta_{in}$. The map $\pi_{a,0}$ is smooth and its $M$-component vanishes identically. If $\Delta_1$ is small, $\pi_{a,0}(\Delta_1)$ is a small vertical segment in $\Delta_{in} \cap S_a^1$ containing the point $q_2$. Fenichel theory implies that $\pi_a$ is a smooth $O(\varepsilon)$-perturbation of the map $\pi_{a,0}$.

<a id='18ded6a8-186a-4cf0-81e8-67e650e401e1'></a>

**Lemma 7** *Fix \u03b4 > 0 small. If the section \u0394\u208bin is chosen small enough, there exists \u03b5\u2080 > 0 such that the map*

<a id='c59cdd9e-7023-49c8-9e29-d86c863c48d7'></a>

$\pi_e : \Delta_{in} \rightarrow \Delta_{out}, \quad (M, C) \mapsto (\pi_e^X(M, C, \varepsilon), \pi_e^C(M, C, \varepsilon))$

<a id='1d959326-b61f-45cc-9d6a-5b400711e1ca'></a>

is well defined and smooth for ε ∈ [0, ε₀]. The map π_ε is a strong contraction with a contraction rate e^(-K/ε) with K > 0. The image of Δ_in is a two-dimensional domain of exponentially small size, which converges to the point q₃ := Δ_out ∩ ω₁ as ε → 0.

<a id='a42f0b2f-80b2-46c3-b05d-2372be282524'></a>

<::Springer logo with a knight chess piece
: figure::>

<!-- PAGE BREAK -->

<a id='3e64afc3-6925-4edf-bdce-d9144d7526b8'></a>

1358

<a id='b0bc4208-81f8-48a1-9041-5aff00827599'></a>

I. Kosiuk, P. Szmolyan

<a id='3b9cef67-f9e5-4401-b55c-0b9efcaa290f'></a>

The full proof of the lemma is based on the blow-up analysis of the edge $l_e$ carried out in Sect. 3. Fenichel theory holds along $w_7$ and $ω_1$ away from the non-hyperbolic edge $l_e$, but does not give a valid description of the dynamics on the edge $l_e$. As already stated in Remark 11 we still have to give arguments why the edge $l_e$ should be associated with a very slow upward motion.

<a id='90d04d3e-e84a-411a-ac7f-590b6ffd8541'></a>

Lemma 8 Fix δ > 0 small. If the section Δout is chosen small enough, there exists ε0 such that the map
πf : Δout → Δ2,
(X, C) ↦ (πfM (X, C, ε), πaC (X, C, ε))

<a id='bc0627c2-ae05-4146-b5ce-5c7b537f386a'></a>

is well defined and smooth for ɛ ∈ [0, ɛ₀]. Furthermore, the linearization $\frac{\partial\pi_f}{\partial(X,C)}$ (q₂) is uniformly bounded.

<a id='219fa33c-1c2f-4df4-badc-8e8868dc3967'></a>

_Proof_ The basic idea of the proof is very similar to the proof of Lemma 6, since the dominant contribution to the map $\pi_f$ comes from the slow flow along the slow manifold $S^2_\varepsilon$ combined with the exponential contraction towards the slow manifold. The jump behaviour at the non-hyperbolic line $l_M$ causes additional difficulties. Fortunately, as described in Remark 10 the map $\pi_f$ is smoothly equivalent to a transition map for the standard singularly perturbed two-dimensional fold (Szmolyan and Wechselberger 2004). Theorem 1 in (Szmolyan and Wechselberger 2004) implies that the good properties of the flow along the attracting slow manifold $S^2_{a,\varepsilon}$ are not affected during the passage of "the fold line" $l_M$. See also Theorem 7 in (Broer et al. 2013). Hence, the statements of the lemma follow.

<a id='523c1dee-f45a-423f-8452-b9101f8c63e0'></a>

Remark 12 Fenichel theory implies that the linearization of πₐ at q₁ (πf at q₂) has one exponentially small eigenvalue λ₁ and one uniformly bounded eigenvalue λ₂ with a well-conditioned eigenbasis. Lemma 4 (Lemma 5) combined with numerical simulations of the flow of the layer problem indicate that in fact that λ₂ < 1 holds, which would imply that the map πₐ (πf) is a contraction.

<a id='5ba991ba-e550-40e0-aee2-ff73064b4b35'></a>

We now turn to the proof of Theorem 1.

Proof of Theorem 1 We combine the maps $\pi_a, \pi_e, \pi_f$ described in Lemmas 6, 7, and 8 to a map $\Pi_1 : \Delta_1 \rightarrow \Delta_2$. If $\Delta_1$ is chosen small enough, there exists $\epsilon_0 > 0$ such that the map $\Pi_1$ is well defined and smooth for $\epsilon \in [0, \epsilon_0]$. The Lemmas 6, 7, and 8 imply that $\Pi_1$ is a contraction with a contraction rate $e^{-K/\epsilon}$ with $K > 0$, since the map $\pi_e$ is contracting with this rate and the maps $\pi_a$ and $\pi_f$ have bounded derivatives.

<a id='8814d27b-d3b2-41e1-924f-576353232e21'></a>

In a completely analogous way, we can define a smooth map $\Pi_2 : \tilde{\Delta} \subset \Delta_2 \rightarrow \Delta_1$,
which is a contraction with a contraction rate $e^{-K/\varepsilon}$ with $K > 0$. For $\varepsilon$ sufficiently
small $\Pi(\Delta_1) \subset \tilde{\Delta}$, hence we can define the Poincaré map $\Pi$ as

<a id='a79f9d3f-07cb-4f1e-a7d1-72542ce32ca0'></a>

Π := Π₂ ∘ Π₁ : Δ₁ → Δ₁.

<a id='79f3d62e-337e-406d-a71f-9f278aaf9658'></a>

The smooth map Π is a contraction with a contraction rate e^(-K/ε) with K > 0 and the existence of a unique fixed point of Π follows for sufficiently small ε. This fixed point corresponds to a periodic orbit of system (3), which tends to the singular cycle Γ₀ as ε → 0, because of the third assertion in Lemma 7.

<a id='f9a7a8b5-ae49-4732-a80b-110ed5784153'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol in black, positioned to the left of the company name "Springer" written in a simple, sans-serif font.::>

<!-- PAGE BREAK -->

<a id='93d5d9aa-267e-4e06-903e-f1d824088865'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='0ed07514-3e6d-4b12-8d8f-a354692ba044'></a>

1359

<a id='8ea48c9d-13d9-480b-af05-1acbea74816a'></a>

### 3 Blow-up analysis of the non-hyperbolic edge $l_e$

In this section we analyze the dynamics of the system (3) close to the edge $l_e$, and give the proof of Lemma 7 describing the properties of the map $\pi_e$. Here the blow-up method plays a crucial role. Although the paper is essentially self-contained, we refer to (Krupa and Szmolyan 2001), (Gucwa and Szmolyan 2009), (Kuehn 2015) for basic examples and more background.

<a id='c728a674-b532-40ef-bda6-de8c76825d2d'></a>

For the blow-up method it is important to introduce the extended system

$\frac{dX}{d\tau} = \left[M(1 - X)(\varepsilon + X) - \frac{7}{10}X(\varepsilon + 1 - X)\right] F_{\varepsilon}(M),$

$\frac{dM}{d\tau} = \left[\frac{6C}{1 + 2C}(1 - M)(\varepsilon + M) - \frac{3}{2}M(\varepsilon + 1 - M)\right] F_{\varepsilon}(X),\quad (20)$

$\frac{dC}{d\tau} = \frac{1}{4}(1 - X - C) F_{\varepsilon}(X, M),$

$\frac{d\varepsilon}{d\tau} = 0,$

<a id='b279367f-7969-41cb-93ab-01fd044b5295'></a>

obtained from the auxiliary system (3) by adding & as a trivial dynamic variable.
For the extended system (20) the line le × {0} is a set of equilibria, at which the
linearization of the system has a quadruple zero eigenvalue, hence the extended system
is very degenerate there. To overcome these degeneracies, we define the blow-up
transformation of the non-hyperbolic line of steady states le × {0} by

<a id='3e2e7dcc-1db6-41df-bcc5-ad858379b2f9'></a>

X = rX̄,
M = rM̄,
ɛ = rɛ̄,
C = C̄

(21)

<a id='930caf7d-42b8-4f20-84bc-01a3a90d1c01'></a>

with (X̄, M̄, ε̄, r, Č) ∈ S² × R × R. More precisely, we consider the blow-up transformation (21) as a mapping

<a id='bbdaef6d-f780-4de4-ba54-31c4b7e3be09'></a>

$\Phi : S^2 \times \mathbb{R}^2 \rightarrow \mathbb{R}^4,$

<a id='b60c59c1-59bc-484e-baa4-5ee6f4ce2af9'></a>

which for $r > 0$ is a diffeomorphism. However, the manifold $Z := S^2 \times \{0\} \times \mathbb{R}$
is mapped onto the edge $l_e \times \{0\}$. The word blow-up refers to the inverse process,
i.e., the edge $l_e \times \{0\}$ is blown-up to its inverse image $Z$ under the transformation
$\Phi$. Similarly, for $C$ fixed each point $(0, 0, C) \in l_e$ is blown-up to a sphere. We use
the following notation: any object $P$ of the extended system (20) is denoted as $\bar{P}$ for
the blown-up problem, see Fig. 11. The extended vector field (20) induces a vector
field on the blown-up space $S^2 \times \mathbb{R}^2$, which vanishes on $Z$. Therefore, the blown-up
vector field can be desingularized on $Z$ by dividing out a common factor $\bar{r}$ to obtain a
less-degenerate non-trivial flow on $Z$. The rationale behind this is that the properties
of the desingularized blown-up system may give results about the degenerate original
problem.

<a id='4135f3f8-80e6-4360-95ee-833bc36f55b4'></a>

<::A logo with a knight chess piece icon followed by the word "Springer".
: figure::>

<!-- PAGE BREAK -->

<a id='bcfa40f7-0a8e-4753-96d8-709ada94c38c'></a>

1360

<a id='1e8c75b9-501f-4dff-931d-712760d2d8ad'></a>

I. Kosiuk, P. Szmolyan

<a id='1443e80f-4b8e-48de-9176-54e9373385dc'></a>

<::Figure: The figure displays a 3D visualization of a blow-up operation. The top-left panel shows a 3D coordinate system with axes labeled C, X, and M. A blue rectangular volume is intersected by two blue planes. A red line segment, labeled `l_e`, represents the non-hyperbolic edge, running along the intersection of these planes. An arrow points from this panel to the top-right panel. The top-right panel shows an orange hemisphere with grid lines, representing a sphere. It has axes labeled C̄, ϵ, M̄, and X̄. Another arrow points from the top-left panel to the bottom-center panel. The bottom-center panel shows a similar 3D setup with the blue rectangular volume and intersecting planes, but the red line `l_e` is replaced by an orange cylinder with grid lines, indicating the blow-up of the edge into a cylinder. This panel also has axes labeled C̄, X̄, and M̄. Fig. 11 Visualization of the blow-up of the non-hyperbolic edge `l_e`. For C fixed each point (0, 0, C) ∈ `l_e` is blown-up to a sphere::>

<a id='84cbbeda-cef3-4ce3-b726-23d9b5ecda96'></a>

Remark 13 Note that our illustrations concerning the blown-up system are three-dimensional sketches of four-dimensional situations showing important parts of the geometry. For instance, in the lower part of Fig. 11 we show the whole (X, M, C)-space, and in addition, the blown-up edge where the individual spheres corresponding to $r = 0$ are drawn as the discs obtained by projecting the spheres into the $\bar{\epsilon} = 0$ plane.

<a id='730f97cf-e848-446f-bc2a-5f4d146b8cd3'></a>

Clearly, the critical manifolds S¹ and S² correspond to M = 0, X = 0, and ε = 0 in the blown-up space. For r > 0 their stability and the reduced flows on the critical manifolds are as described in Sect. 2, see Fig. 12, where also the sections Δin and Δout defined in Sect. 2.4 are shown.

<a id='8b40dffd-9662-47db-a403-ccaa4adaef20'></a>

Since the blow-up analysis is fairly involved, we first summarize the key ideas. Our main goal is to analyze how solutions starting in $\overline{\Delta}_{in}:={}\Phi^{-1}(\Delta_{in}\times\{[0,\epsilon_{0}]	ext{ }	ext{ }	ext{ }	ext{ }\})$ approach Z, are transported upwards along the cylinder until they exit the cylinder close to $C=C^*$ and finally pass through $\overline{\Delta}_{out}:={}\Phi^{-1}(\Delta_{out}\times\{[0,\epsilon_{0}]	ext{ }	ext{ }	ext{ }	ext{ }\})$ see the right part of Fig. 12. This fairly complicated passage is analyzed in local charts $K_1$, $K_2$, and $K_3$, which cover the relevant parts of the manifold Z corresponding to $\overline{X}\ge0$, $\overline{\epsilon}\ge0$ and $\overline{M}\ge0$, respectively, see Figs. 11 and 13. In chart $K_1$ we are able to construct the continuation of the attracting slow manifold $S_{a,\epsilon}^{1}$ (described by Lemma 2) as it enters the neigh-bourhood of Z. Chart $K_2$ allows us to track the continuation of the slow manifold $S_{a,\epsilon}^{1}$ as it moves across the cylinder. We will see that this transition in chart $K_2$ is controlled by a one-dimensional attracting slow manifold. Finally, chart $K_3$ is used to analyze how the extension of the slow manifold exits the cylinder and continues along $S_{a,\epsilon}^{2}$.

<a id='91e38aba-ad4a-486d-a044-4ccbd1a16448'></a>

After having the main strategy explained, we specify the blow-up transformation in the individual charts. The coordinates of the charts K1, K2, and K3 are denoted by

<a id='62bf5c8b-a810-40b9-bef2-b40f01e37bde'></a>

<::logo: Springer
Springer
The logo features a stylized knight chess piece next to the word "Springer" in black text.::>

<!-- PAGE BREAK -->

<a id='65439f41-457a-4b76-ac65-d0c0ff90d78f'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='29ecf23e-ae1a-4a9e-a182-e07dada88def'></a>

1361

<a id='4ef50c8b-cd33-4dac-9d4a-01ff913dc5de'></a>

<::A diagram showing a blow-up process. The left panel shows a 3D representation of a system with axes labeled C, M, and X. A vertical orange line segment is labeled l_e, with a point q_e on it. Blue flow lines with arrows indicate movement around l_e. Two light blue rectangular planes are labeled Δ_out and Δ_in, respectively, in the upper and lower right sections. Green flow lines with arrows originate near Δ_in. An arrow points from this panel to the right panel. The right panel shows a transformed 3D representation, where the line segment l_e has been replaced by an orange cylinder. An orange elliptical cross-section is visible inside the cylinder. The axes are now labeled C̄, M̄, and X̄. Blue flow lines wrap around the cylinder, and two light blue rectangular planes are labeled Δ̄_out and Δ̄_in. Green flow lines with arrows originate near Δ̄_in.: chart::>Fig. 12 Blow-up of the non-hyperbolic edge $l_e$, critical manifolds and reduced flows for $\varepsilon = 0$ and $\bar{\varepsilon} = 0$

<a id='90428a2e-914b-4c66-b274-4b29f392352a'></a>

Understanding the Global Supply Chain

Key Components

The global supply chain is a complex network of organizations, people, activities,
information, and resources involved in moving a product or service from supplier to
customer. It encompasses everything from raw material sourcing to final product
delivery.

• Sourcing & Procurement: Identifying and acquiring raw materials and components.
• Manufacturing: Transforming raw materials into finished goods.
• Logistics & Distribution: Managing the movement, storage, and flow of goods.
• Sales & Marketing: Promoting and selling products to customers.
• Customer Service: Providing support and ensuring customer satisfaction.
• Technology & Data: Leveraging tools for optimization and visibility.

<::diagram
A 3D coordinate system with axes labeled X̄, M̄, and ε̄. An orange, irregularly shaped 3D region is shown in the center. Three light blue planar regions are also depicted:
- K₁ is a rectangular plane in the X̄-M̄ quadrant, partially overlapping the orange region.
- K₂ is a rectangular plane parallel to the X̄-M̄ plane, positioned above the orange region along the ε̄ axis.
- K₃ is a rectangular plane parallel to the X̄-ε̄ plane, positioned to the right of the orange region along the M̄ axis.
::>

Challenges and Solutions

Navigating the global supply chain involves overcoming various obstacles, from
geopolitical risks to technological integration. Effective management requires
adaptability and strategic foresight.

• Risk Management: Developing strategies to mitigate disruptions.
• Sustainability: Implementing eco-friendly practices throughout the chain.
• Digital Transformation: Adopting new technologies for efficiency.
• Collaboration: Fostering strong partnerships with suppliers and distributors.

The future of the global supply chain hinges on innovation and resilience.

<a id='e9198830-b674-42f0-8dad-4bee63faecda'></a>

Fig. 13 Local charts covering the sphere for C fixed. Chart K₁ covers the region corresponding to X ≥ 0, chart K2 covers the upper part of the sphere corresponding to § > 0, and chart K3 the region corresponding to M ≥ 0

<a id='c0255111-1733-4e94-a1bf-069ef0a6472a'></a>

(r_1, M_1, ε_1, C_1), (X_2, M_2, r_2, C_2), and (X_3, r_3, ε_3, C_3), respectively. In these coordinates the blow-up transformation (21) takes the form

<a id='18a74b1e-61d7-4368-bc5b-c632f176f333'></a>

X = r_1,       M = r_1 M_1,       ε = r_1 ε_1,       C = C_1,   (22)
X = ε X_2,     M = ε M_2,         ε = r_2,           C = C_2,   (23)
X = r_3 X_3,   M = r_3,           ε = r_3 ε_3,       C = C_3.   (24)

<a id='d6334021-d7c4-47dd-a4ca-687e8ca08067'></a>

If needed, we will use the following notation: any object _P_ of the extended system
(20) is denoted as _P_i in chart _K_i, _i_ = 1, 2, 3.

<a id='a582b017-7512-482f-8be5-85dfd41de2ce'></a>

Although the transition process has to be analyzed as a process starting in K1,
passing through K2, and ending in K3, we focus on the analysis of the dynamics in
chart K2, since it describes the most important part of the transition along the edge le.
We do not give all the details of the analysis of the dynamics in K₁ and K3, because
it would make the paper prohibitively long. Furthermore, in the proof of our main
result dynamical effects in charts K₁ and K3 play a minor, but very technical role. Full
details can be found in (Kosiuk 2012).

<a id='a634fcc4-039d-4238-b28e-a3de11220dfc'></a>

<::A logo with a knight chess piece icon followed by the word "Springer".
: figure::>

<!-- PAGE BREAK -->

<a id='d59d5a77-2e53-4663-8828-d2946989bcf6'></a>

1362

<a id='515656bc-ea58-4962-97a3-f8b5a6e7b640'></a>

I. Kosiuk, P. Szmolyan

<a id='8c84791f-c3bf-4f54-a940-f344a147928a'></a>

The equations governing the dynamics in $K_2$ are obtained by inserting the trans-
formation (23) into the extended system (20) and by dividing out a common factor $r_2$
in all equations. This gives

<a id='34762038-02e6-42b5-9752-4ff9d6552127'></a>

X'_2 = -7/10 X_2(1 + M_2) + O(ε),
M'_2 = [6C_2 / (2C_2 + 1) (1 + M_2) - 3/2 M_2] (1 + X_2) + O(ε), (25)
C'_2 = ε (1/4 (1 - C_2)(1 + M_2)(1 + X_2)) + O(ε^2).

<a id='4ec3043f-21c0-4053-aef6-fe1e7f8821a0'></a>

Here we have used ε = r_2 and kept the original ε. System (25) is a family of vector fields with parameter ε (since r'_2 = ε' = 0), i.e., the blow-up transformation (21) in these coordinates is just a rescaling of variables. Therefore, the chart K_2 is often referred to as the rescaling chart.

<a id='5c16c068-7fed-4a73-b3be-6f8124ac26a6'></a>

Remark 14 In all applications of the blow-up method the rescaling chart K2 is of crucial importance, since it describes the essential dynamics hidden in the degenerate object, which is blown-up. Actually, the specific form of the blow-up used is typically found by finding a suitable scaling first. Perturbation arguments are valid on compact domains of the rescaling chart. In the original variables these domains correspond to a neighbourhood of the degenerate object of "size" ε. The more complicated related blow-up transformation allows to connect this inner dynamics with the dynamics in an O(1)-distance from the degenerate object. The associated matching is carried out in other charts, here K1 and K3.

<a id='f4552863-a399-40fb-ac59-ad4852653cec'></a>

It is important to observe that system (25) is again singularly perturbed with respect to ε, however, now in standard form of slow-fast systems, i.e., C₂ is the slow variable, X₂ and M₂ are the fast variables, and ' denotes differentiation with respect to a fast time variable τ₂. By transforming to the slow time variable t₂ = ετ₂, we obtain the equivalent slow system

<a id='a6c370ed-ec9a-4581-953c-2428c3364ebd'></a>

$\varepsilon \dot{X}_2 = -\frac{7}{10}X_2(1 + M_2) + O(\varepsilon),$

$\varepsilon \dot{M}_2 = \left[\frac{6C_2}{2C_2 + 1}(1 + M_2) - \frac{3}{2}M_2\right](1 + X_2) + O(\varepsilon),\quad(26)$

$\dot{C}_2 = \frac{1}{4}(1 - C_2)(1 + M_2)(1 + X_2) + O(\varepsilon).

<a id='a86641eb-7245-4c5e-a5b6-8be03d1298d3'></a>

The derivative in (26) is now with respect to t2.
Setting ̣ = 0 in (25) gives the corresponding layer problem

<a id='e9a4a024-4633-4f53-9cd9-40f772f9cf4c'></a>

X'_2 = -7/10 X_2(1 + M_2),
M'_2 = [ (6C_2 / (2C_2 + 1)) (1 + M_2) - 3/2 M_2 ] (1 + X_2),
C'_2 = 0.
(27)

<a id='fbb2b5e0-a5ee-4655-bc81-159101f73fa8'></a>

<::A logo featuring a stylized knight chess piece icon next to the word "Springer".: figure::>

<!-- PAGE BREAK -->

<a id='3993c25f-5a68-424c-88ee-6ec7a961d911'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='b18df262-008b-482b-a8d6-dd872c85f0db'></a>

1363

<a id='4c15f916-2b3c-4df4-a75b-735cf3e6bfa8'></a>

<::Figure 4: A 3D plot illustrating an attracting critical manifold N₂⁰. The coordinate system has axes labeled C₂ (vertical), M₂ (horizontal, extending right), and X₂ (diagonal, extending forward-left). A thick magenta curve, labeled N₂⁰, starts near the C₂-X₂ plane and curves towards higher M₂ values. Orange lines with arrows depict the dynamics, showing trajectories converging towards the magenta manifold. Most arrows are horizontal, pointing towards N₂⁰ from the right. Some arrows also originate from the C₂-X₂ plane, curving towards N₂⁰. On the C₂ axis, there are two marked points: C* (with a dashed horizontal line extending from it) and c̃. The figure represents fast and reduced dynamics in chart K₂.::>

<a id='0a05d5fb-3cef-4edc-b22c-a6df9d5b4805'></a>

The associated critical manifold denoted by $\mathcal{M}_2^0$ is the curve of equilibria $X_2 =$
0, $M_2 = -\frac{4C_2}{2C_2-1}$ of the layer problem (27), shown in purple in Fig. 14. The critical
manifold $\mathcal{M}_2^0$ is normally hyperbolic and the reduced flow on it is upwards. More
precisely, we have

<a id='09999838-6d92-465e-83a3-bfca0d363e24'></a>

Lemma 9 Define $I_2 := [0, \check{c}]$, $\check{c} < C^*$. Then the critical manifold

$N_2^0 := \left\{(0, -\frac{4C_2}{2C_2 - 1}, C_2), C_2 \in I_2\right\}$

<a id='6fa1d326-23f3-41db-a8b3-bd97e785a965'></a>

is fully attracting. There exists ε₀ such that for ε ∈ (0, ε₀] there exists a smooth locally invariant attracting one-dimensional slow manifold N₂^ε , which is O(ε)- close to N₂^0.
The slow flow on N₂^ε is given by

<a id='04f38bc3-66a7-45d0-9e0b-e0f6e90a5422'></a>

$$\dot{C}_2 = \frac{1}{4}(C_2 - 1)\left(\frac{2C_2 + 1}{2C_2 - 1}\right) + O(\varepsilon). \quad (28)$$

<a id='cdc27832-398b-4a6f-8605-8fdba9f7a72c'></a>

Proof For fixed $C_2$ the point $q_2^a = (0, -\frac{4C_2}{2C_2-1})$ is a stable node for the first two equations in (27). The equation governing the reduced problem on the critical manifold $\mathcal{N}_2^0$ is obtained by substituting $M_2 = -\frac{4C_2}{2C_2-1}$ and $X_2 = 0$ into the third equation of system (26) and setting $\varepsilon = 0$. This gives the equation (28) with $\varepsilon = 0$. Hence, the lemma follows from standard Fenichel theory (Fenichel 1979).

<a id='99adc207-5bc4-4360-946a-d54de7e00d6b'></a>

Hence, $C_2$ increases under the slow flow on $\mathcal{N}_2^0$, as shown in Fig. 14. In fact, the solution of the reduced problem reaches the singularity $C_2 = C^*$ in finite time and $M_2$ becomes unbounded. The associated loss of normal hyperbolicity is the reason why we had to restrict $C_2$ to the interval $I_2$. To see what happens as $C_2$ approaches $C^*$, one must switch to chart $K_3$, see Figs. 14 and 15.

<a id='d59cac5e-8e48-472c-a93d-535ac0a79cd6'></a>

Remark 15 The dynamics in chart K2 corresponds to accumulation of cyclin C for M and X close to zero. Approaching and crossing the threshold value C = C* corresponding to the activation of cdc2 kinase M must be analyzed in chart K3.

<a id='57a3d6b6-8502-472d-8818-270157a19b97'></a>

<::Springer logo with a knight chess piece icon: figure::>

<a id='9944c491-d891-47b1-9127-98cd6c88c948'></a>

Fig. 1

<!-- PAGE BREAK -->

<a id='88b238b8-f170-4ca5-8b22-81b611ab3b6d'></a>

1364

<a id='5e689068-47fd-4d8a-b9ce-441e55dcd7ee'></a>

I. Kosiuk, P. Szmolyan

<a id='68c09f82-9856-4710-bdc0-25493fd002a8'></a>

<::diagram: The diagram illustrates the geometry of a blown-up space and a singular cycle Γ_0. A central orange cylinder is shown, intersected by several blue planes. The cylinder has multiple circular cross-sections indicated by dotted orange lines, each with small black dots and arrows suggesting a flow or direction. A vertical axis labeled "C" passes through the center of the cylinder. A horizontal plane is labeled "M" on the right and "X" on the left. Another plane is labeled with "N^0". A value "C*=0.5" is indicated to the left of the cylinder. Several curves with arrows are drawn, some in blue, some in magenta, and some in green. A prominent magenta curve traverses the interior of the cylinder, connecting points labeled "p_e" and "q_e". Blue curves labeled "ω_1" and "ω_7" are shown interacting with the cylindrical structure. The overall representation shows complex interactions between geometric surfaces and paths. Fig. 15 Geometry of the blown-up space and singular cycle Γ_0::>

<a id='0560a501-00dc-4355-9d50-419b5a1107da'></a>

Now we are ready to state the main result of this section.

**Theorem 2** For fixed δ small there exists ε₀ > 0 such that system (3) has the following properties for fixed ε ∈ [0, ε₀]:

1. The transition map π_ε : Δ_in → Δ_out is well defined and smooth.
2. The image of Δ_in is a two-dimensional domain of exponentially small size lying exponentially close to a point (X(ε), δ, C(ε)), which lies exponentially close to S²_{a,ε} and converges to the point q₃ := Δ_out ∩ ω₁ as ε → 0.
3. The transition map π_ε is an exponential contraction with a rate O(e^(-K/ε)), where K is a positive constant.

<a id='c37b2747-3ef8-4b67-8d22-698b0d53ae01'></a>

The proof is carried out by studying the corresponding transition map $\bar{\pi}_\varepsilon: \bar{\Delta}_{in} \to \bar{\Delta}_{out}$ in the blown-up space and interpreting the results for fixed $\varepsilon \in [0, \varepsilon_0]$. We start by stating and explaining the relevant properties of the blown-up vector field shown in Fig. 15. Recall that the critical manifolds $X = 0$ and $\bar{M} = 0$ intersect along the non-hyperbolic line $l_\varepsilon$, which due to the blow-up has been replaced by the cylinder shown in orange. The flows shown in blue correspond to the reduced flows on $\bar{M} = 0$ and $\bar{X} = 0$, respectively. Here, the orbits $\bar{\omega}_7$ and $\bar{\omega}_1$ correspond to the orbits $\omega_7$ and $\omega_1$, respectively, compare Figs. 8 and 15. The point where $\bar{\omega}_7$ ends on $Z$ is denoted

<a id='72c247a2-b0e0-4fa1-970f-49ce77fb434c'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol in black, positioned to the left of the company name "Springer" written in a simple, sans-serif font.::>

<!-- PAGE BREAK -->

<a id='d07733da-da00-4d78-b7f0-687eedc54d33'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='28de0b1c-e2a5-4c11-9903-026025553390'></a>

1365

<a id='6966a1dc-2d2f-438d-abaa-47e501d49edf'></a>

by $\overline{p}_{e}$ Similarly, the point where $\overline{\omega}_{1}$ starts on Z is denoted by $\overline{q}_{e}$. A computation in chart $K_{1}$ proves that at the point $\overline{p}_{e}$ there exists a three-dimensional attracting center manifold, which is in fact the continuation of the family (indexed by $\varepsilon$) of slow attracting manifolds $S_{a,\epsilon}^{1}$. This allows to continue the family $S_{a,\epsilon}^{1}$ into chart $K_{2}$, which covers the interior of the cylinder. There all orbits are exponentially attracted by the one-dimensional slow manifold $\mathcal{N}_{2}^{\varepsilon}$ described in Lemma 9. Transforming the unbounded part of the critical manifold $\mathcal{N}_{2}^{0}$ to chart $K_{3}$ proves that it limits in a point $q_{e,3}$, which is precisely the point $\overline{q}_{e}$ written in chart $K_{3}$. The point $q_{e,3}$ is a degenerate equilibrium of the blown-up vector field. The linearization at $q_{e,3}$ has one stable eigenvalue and a triple zero eigenvalue. This allows to construct a three-dimensional center manifold at $q_{e,3}$, which controls the local dynamics. Carefully tracking the family $\mathcal{N}_{2}^{\varepsilon}$ along this center manifold proves that the continuation of $\mathcal{N}_{2}^{\varepsilon}$ intersects the section $\Delta_{out}$ in a point $(X(\varepsilon),\delta,C(\varepsilon))\in\Delta_{out}$ exponentially close to the slow manifold $S_{a,\epsilon}^{2}$. Furthermore, the point $(X(\varepsilon),\delta,C(\varepsilon))$ converges to the point $q_{3}:=\Delta_{out}\cap\omega_{1}$ as $\varepsilon$ tends to zero.

<a id='8aa48a50-2dd5-45b3-91df-31ad53cbbc8e'></a>

All orbits starting in $\Delta_{in}$ are exponentially attracted onto the continuation of the slow manifold $S^1_{a,\varepsilon}$. Hence, these orbits enter chart $K_2$ and are exponentially attracted onto the one-dimensional slow manifold $\mathcal{N}^{\varepsilon}_2$, follow it through $K_2$ and $K_3$, and intersect $\Delta_{out}$ exponentially close to the point $(X (\varepsilon), \delta, C(\varepsilon))$.

<a id='b521cfd9-8020-43ca-8346-42d2953b36d4'></a>

The transition map πe is a strong contraction, since all orbits starting in Δin spend an O(1)-time on the time scale t2 of system (26) in chart K2. This contraction is not lost during the passage near the exit point q3 in K3, since a locally defined transition map corresponding to this passage can be shown to be at most algebraically expanding.

<a id='8c6ee3f4-10d9-4b00-ba18-799bacf572ed'></a>

Remark 16 In our blow-up analysis the singular cycle $\Gamma_0$ (19) is replaced by the more complicated singular cycle $\bar{\Gamma}_0$, which is obtained by replacing the segment $\omega_8 \subset l_e$ with the connection between the points $\bar{p}_e$ and $\bar{q}_e$, which consists of two pieces: the thick orange orbit and the slow motion along $\mathcal{N}^0$ shown in purple, see Fig. 15. Close to the point $\bar{p}_e$, i.e., in chart $K_1$ this thick orange orbit is the unique one-dimensional center manifold of $\bar{p}_e$ on $\mathbb{S}^2 \times \{0\} \times \{C_e\}$, where $C_e$ is the $C$-coordinate of the point $p_e$. As it approaches $\mathcal{N}^0$ in the plane $C_2 = C_e$ in chart $K_2$ this orbit corresponds to an orbit of the layer problem (27). In retrospective this justifies the definition of the singular cycle $\Gamma_0$ containing the segment $\omega_8$, compare Remark 11.

<a id='f7586762-6f23-44a8-bdea-1ad8e6e57352'></a>

Clearly, Theorem 2 implies Lemma 7.

<a id='737c14e0-5522-492c-b0ef-feff284b0953'></a>

## 4 Discussion

Very detailed molecular descriptions of the basic mechanisms of the cell cycle have been defined through experimental and theoretical studies over the past three decades. The cell cycle network is fairly well mapped out, however, a satisfying understanding of its dynamics requires more than a description of its components and the interactions between them.

<a id='3cb9551a-a80d-4e6d-a5dd-6acf9d1e3a55'></a>

To fully comprehend the dynamics of the cell cycle, ODE models of varying complexity have been used. Many of the early models aimed at understanding in simpler terms the cell cycle regulation, while the recent more complicated models test the

<a id='7ebaf76a-44c6-475f-88a8-c9aa1a844682'></a>

<::Springer logo with a knight chess piece icon: figure::>

<!-- PAGE BREAK -->

<a id='f8666665-b815-4ad6-8460-59330d98acfb'></a>

1366

<a id='02ec72ee-71db-469a-b43a-fa74f6298e6d'></a>

I. Kosiuk, P. Szmolyan

<a id='066de06d-3c5f-4dbd-8d39-a0c88aef6f1a'></a>

existing knowledge on the specific details of the cell cycle network regulated by a
variety of negative and positive feedback loops. Often such feedback loops involve
one or more sigmoidal response functions. At the molecular level the sigmoidal depen-
dence can originate from the phenomenon of zero-order ultrasensitivity in which two
enzymes catalyzing opposite covalent modification reactions (e.g., phosphorylation-
dephosphorylation) are saturated by their protein substrate.

<a id='f6f89c4c-348e-48e7-bff2-940eca3005e6'></a>

In this paper we studied a model for the oscillatory activity of several enzymes working in a covalent modification cascade developed by Goldbeter. The minimal model for the mitotic oscillator involving cyclin, cdc2 kinase, and a cyclin protease is given by a system of three nonlinear ordinary differential equations (2). For certain parameter values and Michaelis constants small the model exhibits interesting oscilla- tory behaviour: the progressive rise of cyclin beyond a threshold activates cdc2 kinase, which increases sharply; as soon as cdc2 kinase exceeds a threshold, cyclin protease is activated (by reversible phosphorylation) and also increases rapidly, which in turn elicits cyclin degradation; consequently, this switches off the activation of cdc2 kinase and cyclin protease, both return to low values resetting the system for a new mitotic cycle, see Fig. 3.

<a id='47c609f4-b62a-4b2d-b2b2-8cab6f1bd3b9'></a>

We have analyzed the dynamics of the mitotic oscillator (2) in the limit of small Michaelis constants and proved analytically that for ε sufficiently small there exists a unique strongly attracting limit cycle of the mitotic oscillator. Our proof is based on a detailed geometric analysis of the auxiliary system (3), which is a polynomial version of the mitotic oscillator (2). The auxiliary system (3) turned out to be a singular perturbation problem of general type, i.e., without a global separation into slow and fast variables, and with exchange of stability, i.e, for ε = 0 the problem has a self-intersecting two-dimensional critical manifold S of equilibria. The singular perturbation character of the problem with respect to small Michaelis constant ε allowed to study the auxiliary system in the spirit of geometric singular perturbation theory by analyzing various lower-dimensional limiting problems. To obtain a full description of the dynamics – in particular, close to the self-intersections of S, where the normal hyperbolicity of S is lost – we have applied the blow-up method.
From the mathematical point of view our main findings are

<a id='e36b45bd-76a1-4f7e-8573-4607b6fc4ac1'></a>

1. discovery of a new phenomenon of slow drift along the edge l_e called "delayed exchange of stability",
2. the identification of the singular cycle Γ_0, which persists as a new type relaxation cycle of the auxiliary system (3) for small values of ε.

<a id='30fa4dc9-d31f-4410-941c-96430d12fa3b'></a>

Our geometric analysis provides the explanation and full understanding of the mathematical mechanisms leading to the oscillatory behaviour of cyclin, cdc2 kinase, and cyclin protease. More precisely, in the Goldbeter model cyclin accumulation in the mitotic oscillator (2) corresponds to slow drift along the edge l_e, the activation of cdc2 kinase corresponds to the transition from slow motion along the edge l_e to slow motion along the slow manifold S_a^2, which occurs close to C* = 0.5. The activation of cyclin protease takes place at jump points at the non-hyperbolic line l_M with M close to M* = 0.7. Cyclin degradation corresponds to the slow drift along the edge l^e. Finally, the inactivation of cdc2 kinase and cyclin protease correspond to the transition from slow motion along the edge l^e to slow motion along S_a^3, and jumps at

<a id='db3e9195-d426-4023-af4c-dd1498f15abb'></a>

<::logo: Springer
Springer
The logo features a stylized chess knight symbol in black, positioned to the left of the company name "Springer" written in a simple, sans-serif font.::>

<!-- PAGE BREAK -->

<a id='d3dd7c6f-4b9e-47a4-a8cf-5beb5bd3389d'></a>

Geometric analysis of the Goldbeter minimal model...

<a id='1cb0815d-8148-48b5-bb8a-644daed6df52'></a>

1367

<a id='ba90f2ef-f824-4fff-bb22-2869d63a417c'></a>

the non-hyperbolic line $l^M$, respectively. These mechanisms generate a novel type of oscillations, which in the auxiliary system (3) are of relaxation type.

<a id='6a9b5136-c605-4552-965c-f1756f4d1f71'></a>

Since equations (1) and similar systems are widely utilized as modules in cell cycle models, we believe that our approach based on concepts from geometric singular perturbation theory and geometric desingularization by blow-ups will be useful in the mathematical analysis of such systems.

<a id='06835ddc-698d-4c01-b5fd-41120d4db3ce'></a>

Acknowledgments I. Kosiuk thanks the Max Planck Institute for Mathematics in the Sciences in Leipzig for providing a post-doctoral scholarship funding this research. I. Kosiuk and P. Szmolyan thank the Max Planck Institute for Mathematics in the Sciences in Leipzig and Technische Universität Wien for support and hospitality during several mutual visits. We are also grateful for financial support from the Vienna Science and Technology Fund (WWTF) through Project MA14-049.

<a id='a1ff99ed-cee6-4162-81a3-7dfc616920e8'></a>

# References
Aguda BD, Friedman A (2008) Models of cellular regulation, Oxford Graduate Texts. Oxford University Press, Oxford
Alberts B, Johnson A, Lewis J, Morgan D, Raff M, Roberts K, Walter P (2014) Molecular Biology of the cell. Garland Science, New York
Battogtokh D, Tyson JJ (2004) Bifurcation analysis of a model of the budding yeast cell cycle. Chaos 14:653–661
Broer HW, Kaper TJ, Krupa M (2013) Geometric desingularization of a cusp singularity in slow-fast systems with applications to Zeeman's examples. J Dyn Differ Equ 25:925–958
Chen KC, Csikasz-Nagy A, Gyorffy B, Val J, Novak B, Tyson JJ (2000) Kinetic analysis of a molecular model of the budding yeast cell cycle. Mol Biol Cell 11:369–391
Chicone C (2006) Ordinary differential equations with applications. Springer Science+Business Media Inc, New York
Dumortier F, Roussarie R (1996) Canard cycles and center manifolds. Mem Am Math Soc 577
Erneux T, Goldbeter A (2006) Rescue of the quasi-steady state approximation in a model for oscillations in an enzymatic cascade. SIAM J Appl Math 67:305–320
Fenichel N (1979) Geometric singular perturbation theory. J Differ Equ 31:53–98
Gérard C, Goldbeter A (2011) A skeleton model for the network of cyclin-dependent kinases driving the mammalian cell cycle. R Soc J Interface Focus 1:24–35
Gérard C, Goldbeter A (2012) The cell cycle is a limit cycle. Math Models Nat Phenom 7:126–166
Goldbeter A, Koshland DE Jr (1981) Ultrasensitivity in biochemical systems controlled by covalent modification. Interplay between zero-order and multistep effects. J Biol Chem 259:14441–14447
Goldbeter A (1991) A minimal cascade model for the mitotic oscillator involving cyclin and cdc2 kinase. Proc Natl Acad Sci USA 88:9107–9111
Goldbeter A (1996) Biochemical oscillations and cellular rhythms: the molecular bases of periodic and chaotic behaviour. Cambridge University Press, Cambridge
Grasman J (1987) Asymptotic methods for relaxation oscillations and applications. Springer, New York
Gucwa I, Szmolyan P (2009) Geometric singular perturbation analysis of an autocatalotor model. Discrete Contin Dyn Syst Ser S 2:783–806
Hek G (2010) Geometric singular perturbation theory in biological practice. J Math Biol 60:347–386
Hunt T (2001) Protein synthesis, proteolysis, and cell cycle transitions, Nobel lecture. http://www.nobelprize.org/nobel_prizes/medicine/laureates/2001/hunt-lecture
Izhikevich EM (2007) Dynamical systems in neuroscience: the geometry of excitability and bursting. The MIT Press, Massachusetts
Jones CKRT (1995) Geometric singular perturbation theory. Springer Lect Notes Math Berlin 1609:44–120
Keener JP, Sneyd J (1998) Mathematical physiology. Springer, New York
Kosiuk I (2012) Relaxation oscillations in slow-fast systems beyond the standard form, PhD thesis, University of Leipzig
Kosiuk I, Szmolyan P (2011) Scaling in singular perturbation problems: blowing up a relaxation oscillator. SIAM J Appl Dyn Syst 10:1307–1343

<a id='3ef23ae0-8dc6-48cc-bad7-a25a025d8d7a'></a>

<::logo: Springer
Springer
The logo features a stylized knight chess piece next to the word "Springer" in black text.::>

<!-- PAGE BREAK -->

<a id='98e4be2c-ee5e-4d05-a353-6290cb90d706'></a>

1368

<a id='22c72519-1456-4173-97d6-03fdf05b1f27'></a>

I. Kosiuk, P. Szmolyan

<a id='91c5223b-7a69-4ed6-b4fe-7f914bd26b79'></a>

Krupa M, Szmolyan P (2001) Extending geometric singular perturbation theory to non-hyperbolic points-fold and canard points in two dimensions. SIAM J Math Anal 33:286–314
Krupa M, Szmolyan P (2001) Extending slow manifolds near transcritical and pitchfork singularities. Nonlinearity 14:1473–1491
Kuehn Ch (2015) Multiple time scale dynamical systems. Springer, Berlin. doi:10.1007/978-3-319-12316-5
Lebovitz NR, Schaar JR (1975) Exchange of stabilities in autonomous systems. Studies Appl Math 54:229–260
Mishchenko EF, Kh Rozov N (1980) Differential equations with small parameters and relaxation oscillations. Plenum Press, New York
Morgan DO (2007) The cell cycle: principles of control. New Science Press, Oxford University Press, Sinauer Associates/London, Corby, Sunderland
Novak B, Tyson JJ (1995) Quantitative analysis of a molecular model of mitotic control in fission yeast. J Theor Biol 173:283–305
Novak B, Tyson JJ (1997) Modeling the control of DNA replication in fission yeast. Proc Natl Acad Sci USA 94:9147–9152
Novak B, Csikasz-Nagy A, Gyorffy B, Chen K, Tyson JJ (1998) Mathematical model of the fission yeast cell cycle with checkpoint controls at the G1/S, G2/M and metaphase/anaphase transitions. Biophys Chem 72:185–200
Nurse P (2000) A long twentieth century of the cell cycle and beyond. Cell 100:71–78
Sveiczer A, Tyson JJ, Novak B (2004) Modelling the fission yeast cell cycle. Brief Funct Genomic Proteomic 2:298–307
Szmolyan P (1991) Transversal heteroclinic and homoclinic orbits in singular perturbation problems. J Differ Equ 92:252–281
Szmolyan P, Wechselberger M (2004) Relaxation oscillations in R³. J Differ Equ 200:69–104
Tyson JJ, Chen K, Novak B (2003) Sniffers, buzzers, toggles and blinkers: dynamics of regulatory and signaling pathways in the cell
Tyson JJ (1991) Modeling the cell division cycle: cdc2 and cyclin interactions. Proc Natl Acad Sci USA 88:7328–7332
Tyson JJ, Chen K, Novak B (2001) Network dynamics and cell physiology. Nat Rev Mol Cell Biol 2:908–916

<a id='f1a8328b-2d6c-4661-b4ed-1849a160cb86'></a>

Springer
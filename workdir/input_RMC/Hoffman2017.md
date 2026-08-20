<a id='c0fa8aab-8513-467c-a9d6-8b1c7ae35cb0'></a>

Journal of Theoretical Biology 436 (2018) 39–50

<a id='d188229b-ce9e-4f83-9a25-e1e8bf259932'></a>

<::logo: Elsevier
NON SOLLUS
A detailed illustration of a tree with two figures, one picking fruit, above the orange text "ELSEVIER"::>

<a id='0f2884d7-5259-4e2c-8ecc-52596276d9b6'></a>

Contents lists available at ScienceDirect

<a id='ce697a52-ff35-4b45-9963-4d655fc5b1ac'></a>

Journal of Theoretical Biology

<a id='3785d031-55ca-42ac-ae9b-aa7569f1843a'></a>

journal homepage: www.elsevier.com/locate/jtbi

<a id='0b412cfd-8bf5-46b0-a173-68be3f3cbf14'></a>

<::Cover of the "Journal of Theoretical Biology". The title "Journal of Theoretical Biology" is prominently displayed in red text. In the top left corner, there is a small emblem or logo. In the top right corner, "VOLUME 220" is written. The background of the cover has a marbled texture in shades of green, white, and light brown.: cover image::>

<a id='14c47fef-5ce6-4895-aec5-ad8d88f10125'></a>

A mathematical model of antibody-dependent cellular cytotoxicity (ADCC)

<a id='cdab99bf-581c-4548-82bb-d1215759f7d5'></a>

<::CrossMark logo with a red bookmark icon : figure::>

<a id='0edf8225-2deb-45b0-9854-2df0772d19f8'></a>

F. Hoffmana, ¹, D. Gavaghana, J. Osborne a,b,¹, I.P. Barrettc, T. You d,e,¹, H. Ghadiallyf,
R. Sainson f,¹, R.W. Wilkinsonf, H.M. Byrnea,g,*

<a id='de871cbb-d012-491b-a9ff-715db21482db'></a>

a Department of Computer Science, University of Oxford, Oxford, UK
b School of Mathematics and Statistics, University of Melbourne, AUS
c Quantitative Biology, Astrazeneca Ltd., Cambridge, UK
d Computational Biology, Astrazeneca Ltd., Alderley Edge, UK
e Beyond Consulting Ltd., BioHub, Alderley Park, Cheshire SK12 4TG, UK
f Medimmune Ltd., Cambridge, UK
g Mathematical Institute, University of Oxford, Oxford, UK

<a id='6e2de726-a31e-471e-a1f3-e277e7e6d4f5'></a>

A R T I C L E I N F O
---
Article history:
Received 21 October 2016
Revised 26 September 2017
Accepted 28 September 2017
Available online 29 September 2017
---
Keywords:
Immunotherapy
Antibody-dependent cellular cytotoxicity
Ordinary differential equations
Asymptotic analysis

<a id='c36cbd7b-9c48-4160-a456-ae3e831d9706'></a>

ABSTRACT
Immunotherapies exploit the immune system to target and kill cancer cells, while sparing healthy tissue. Antibody therapies, an important class of immunotherapies, involve the binding to specific antigens on the surface of the tumour cells of antibodies that activate natural killer (NK) cells to kill the tumour cells. Preclinical assessment of molecules that may cause antibody-dependent cellular cytotoxicity (ADCC) involves co-culturing cancer cells, NK cells and antibody in vitro for several hours and measuring subsequent levels of tumour cell lysis. Here we develop a mathematical model of such an in vitro ADCC assay, formulated as a system of time-dependent ordinary differential equations and in which NK cells kill cancer cells at a rate which depends on the amount of antibody bound to each cancer cell. Numerical simulations generated using experimentally-based parameter estimates reveal that the system evolves on two timescales: a fast timescale on which antibodies bind to receptors on the surface of the tumour cells, and NK cells form complexes with the cancer cells, and a longer time-scale on which the NK cells kill the cancer cells. We construct approximate model solutions on each timescale, and show that they are in good agreement with numerical simulations of the full system. Our results show how the processes involved in ADCC change as the initial concentration of antibody and NK-cancer cell ratio are varied. We use these results to explain what information about the tumour cell kill rate can be extracted from the cytotoxicity assays.

<a id='eee7e42e-1ef9-447a-b877-09b904e9447f'></a>

© 2017 Elsevier Ltd. All rights reserved.

<a id='fd03ada5-29a1-4154-b92e-6036bcc416ad'></a>

1. Introduction
The immune system plays a key role in cancer progression
(Bachireddy, 2012), with evasion of the immune system now recog-
nised as one of the hallmarks of cancer (Hanahan and Wein-
berg, 2011). The design of drugs that manipulate the immune
system has the potential to revolutionise treatments for cancer
(Hodi et al., 2010). Antibody-based treatments represent an impor-
tant class of cancer immunotherapies. Of interest here are antibod-
ies, that induce cancer cell death by binding to specific cell-surface
molecules on cancer cells (tumour associated antigens), which in-
terfere with cell signalling and/or flag cells for removal by the im-

<a id='375e465f-ea34-42ed-95cc-b7b0aa0657f4'></a>

* Corresponding author.
E-mail address: helen.byrne@maths.ox.ac.uk (H.M. Byrne).
1 Indicates formerly.

<a id='40dce30d-bb80-4f0d-a9db-768efa029aee'></a>

https://doi.org/10.1016/j.jtbi.2017.09.031
0022-5193/© 2017 Elsevier Ltd. All rights reserved.

<a id='048d4368-985b-4fdc-aa96-7e3e83b2bc3b'></a>

mune cells, including natural killer (NK) cells (Seidel et al., 2013).
NK cells establish dynamic contacts with potential target cells and
survey their surface for molecules such as antibodies, using recep-
tors with binding specificity for a part of the antibody known as
the Fc region. When an NK cell's Fc receptors (FcRs) detect a crit-
ical level of antibody, it lyses the cell by the targeted delivery of
cytotoxic proteins: this process is termed antibody dependent cel-
lular cytotoxicity (ADCC). It enables individual NK cells sequentially
to kill multiple target cells (Deguine et al., 2010), while sparing
healthy cells that do not express the relevant antigens.

<a id='1a8d9fb1-f08f-49bc-981c-c9a6277317a0'></a>

ADCC is known to contribute to the clinical efficacy of anti-cancer antibodies (Iida et al., 2009) and it is anticipated that antibodies that enhance ADCC will play a prominent role in the development of future treatments for cancer patients. Experimentalists investigate the capacity of an antibody to induce ADCC by performing in vitro cytotoxicity assays, that measure target cell lysis as an-

<!-- PAGE BREAK -->

<a id='1978ba0b-c624-4df6-9827-d6dcd4d9e998'></a>

40

<a id='b0602688-01e4-405e-9246-b6f077485b54'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='f90b9b12-f4eb-4ad0-8325-27c114872bc6'></a>

<::chart: Line chart showing the percentage of cell kill against antibody concentration. The x-axis is "antibody(µg/ml)" with a logarithmic scale from 10⁻⁵ to 10, and an initial point at 0. The y-axis is "%kill" ranging from -20 to 120. There are five data series, each representing a different initial NK-tumour cell ratio, indicated by labels on the right side of the chart: 20:1, 10:1, 5:1, 2.5:1, and 1.25:1. Each series is plotted with red triangles for the mean percentage kill, and a transparent red shaded field representing the maximum and minimum of triplicate measures. The lines generally show an increase in %kill with increasing antibody concentration, with higher NK-tumour cell ratios leading to higher %kill. The 20:1 ratio shows the highest kill percentage, reaching close to 100%, while the 1.25:1 ratio shows the lowest, staying below 20%.::>Fig. 1. Data from a series of cytotoxicity assays in which HER2/neu positive, SkBr3 breast cancer cells (Fogh et al., 1977) were co-cultured with NK cells in the presence of the antibody Trastuzumab (Hudis, 2007). The percentage of cell kill after 4 h of co-culture was measured for different initial NK-tumour cell ratios (20:1, 10:1, 5:1, 2:1, 1.25:1) and for a range of initial antibody levels (10⁻⁶ µg/ml–10 µg/ml). The percentage tumour cell kill associated with an initial antibody level (and an initial NK-tumour cell ratio) was measured as described in Appendix A, all values being measured at the end of the experiment (t = 4 h). Key: mean percentage kill (red triangles); maximum and minimum of triplicate measures for a particular experiment (transparent red fields). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

<a id='681c522a-264b-476b-8163-f2f26cbdb802'></a>

tibody concentrations and NK-cancer cell ratios are varied. In these assays, cancer cells, antibodies and NK cells are co-cultured in a micro-well and levels of tumour cell lysis are then measured 2-4 h later. In a typical assay NK cells and cancer cells are co-cultured at ratios that range from 1:1 to 20:1, while antibody concentrations vary between 10-6 µg/mL and 10 µg/mL (for more details, see, for example, Ogbomo et al., 2006; Stewart et al., 2011).

<a id='a69a6fdc-6555-4b20-ad4c-9c22df8cff53'></a>

In Fig. 1 we present results from specific cytotoxicity assays in which HER2/neu positive, SkBr3 breast cancer cells (Fogh et al., 1977) were co-cultured with NK cells in the presence of the anti-body trastuzumab (Hudis, 2007). Briefly, different ratios of effector cells (NK cells) and tumour cells (target cells) were mixed with a range of concentrations of an antibody that binds to a receptor on the surface of the tumour cells (initial NK-tumour cell ratios were 20:1, 10:1, 5:1, 2:1, 1.25:1; antibody levels ranges from 10-6 µg/ml to 10 µg/ml which corresponds to 6.67 x10-8 mol/l–6.67 x10-14 mol/l). Binding of antibody to tumour cell receptors in turn enables an NK cell to bind and kill the antibody-bound tumour cell, and that cell killing process is measured after four hours of co-culture using a marker of cell lysis (release of an enzyme, GAPDH, into the culture medium). In this way, the percentage of tumour cells killed for a range of different effector/target cell ratios and antibody concentrations can be measured. (Full details of the experimental procedure used to generate the data presented in Fig. 1 are provided in Appendix A) Fig. 1 shows that the percentage kill increases with the initial antibody level and the initial NK-cancer cell ratio. We note also that the cytotoxicity assays provide information about percentage tumour cell kill at a single time-point only (t = 4 h).

<a id='f016ad90-1446-4e5e-b680-a3a2b1efe834'></a>

Mathematical models represent a natural framework within which to study the processes involved in the cytotoxicity assays and the timescales on which they act. To date, two main approaches have been used to model immune cell killing in cytotoxicity assays: deterministic models, formulated as systems of time-dependent, ordinary differential equations (ODEs) (Callewaert et al., 1978; Thorn and Henney, 1976; 1977; Zeijlemaker et al.,

<a id='459fda92-c55e-4491-ac88-1fcb1f9194b3'></a>

1977), and stochastic models, typically involving Poisson processes (Chu, 1978; Miller and Dunkley, 1974). The ODE models can be viewed as mean-field approximations of the stochastic models (Gardner, 2009) and are typically more analytically and computa- tionally tractable than their stochastic counterparts. Therefore, in this paper, we use an ODE approach to develop a dynamic, math- ematical model of in vitro ADCC. Where existing models of cancer cell killing by immune cells assume a constant kill rate and neglect the role of antibodies in modulating the cell kill rate (Callewaert et al., 1978; Thorn and Henney, 1976; 1977; Zeijlemaker et al., 1977), our model assumes that the rate at which NK cells kill can- cer cells depends upon the number of antibodies bound to the tar- get/cancer cells. For completeness, we note that other authors have modelled the relationship between binding parameters and cyto- toxicity in ADCC using non-ODE based approaches (see Douglass et al., 2013; Garcia-Penarrubia et al., 2002 for further details).

<a id='ddd92c58-02df-4edc-8663-8aa057685d3d'></a>

We use the experimental literature to estimate parameter val- ues and then nondimensionalise the model equations, before in- vestigating them with a combination of numerical simulations and analytical techniques. Throughout this study, our main aim is to es- tablish what information can be obtained about the way in which ADCC modulates the rate at which NK cells kill tumour cells. Our analysis reveals how data from the different cytotoxicity assays may be aggregated to provide valuable information about the rate at which NK cell killing of cancer cells is enhanced by ADCC.

<a id='571300cd-d4ba-4a8b-9d2d-8d1b863fd8bd'></a>

The remainder of the paper is structured as follows. In Section 2 we introduce our mathematical model, nondimension-alise the governing equations and then introduce a change of vari-ables in order to simplify the subsequent analysis. We also use the experimental literature to estimate model parameters and identify a range of parameter scalings relevant to antibody-based cancer therapy. In Section 3 we perform numerical simulations to illus-trate how the system dynamics change as the experimental condi-tions vary. In Section 4 we exploit the parameter scalings identified in Section 2 by using perturbation methods to construct approx-imate model solutions. The paper concludes in Section 5 with a discussion of our results and suggestions for future work.

<a id='d91faf07-4fb7-4de1-90e9-3c5b210af1b9'></a>

## 2. A mathematical model of ADCC

In this section we develop a new mathematical model of an ADCC cytotoxicity assay in which cancer cells, antibodies and NK cells are incubated in a micro-well for four hours and then the number of dead target cells is measured (see Fig. 1). The model is formulated as a system of six time-dependent ODEs and accounts for processes that occur on the subcellular and cellular scales. At the subcellular scale, the dependent variables represent the concentration of antibodies, A(t) (moles per litre), the concentration of unbound target receptors, T<sub>u</sub>(t) (moles per litre), and the concentration of antibody-target receptor complexes, T<sub>b</sub>(t) (moles per litre).

<a id='e42f80e0-5dae-4b27-b8c9-6aa36a0a0266'></a>

At the cellular scale, the dependent variables represent the con-centration of NK cells, N(t), the concentration of cancer cells, T(t), and the concentration of NK-cancer cell complexes, C(t), all vari-ables having units of cells per cubic metre. Our model accounts for the binding of antibodies to target receptors on cancer cells, NK cell binding to cancer cells, and NK cell killing of cancer cells in response to antibody-bound targets. A schematic of the model is presented in Fig. 2.

<a id='4eb123c6-cc08-4d4e-a522-0b7d2f7b6285'></a>

As the time-scale of experiments (4 h) is much shorter than typical cell cycle times of NK cells (Lutz et al., 2011) and cancer cells (Nakagawa et al., 2003), we neglect processes such as cell division and natural cell death, which operate on longer time-scales. We assume further that the cells and antibody are well-mixed so that spatial effects may be neglected. While direct evidence to justify a well-mixed model is currently lacking, our assumption is

<!-- PAGE BREAK -->

<a id='a8533396-b503-496f-b24a-ae3525bd388d'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='450322a6-ac1e-43e8-8baa-b17f0bbdc15d'></a>

41

<a id='4584d1c4-5aad-4d27-b101-c5651d29efab'></a>

<::Schematic diagram: flowchart
Cellular Molecular

Left side (Main Model):
Molecular section:
- Circle A
- Circle T_u
- Circle T_b
- Double-headed arrow between A and T_b
- Arrow from T_u to T_b
- Arrow from T_b to T_u

Cellular section:
- Circle N
- Circle T
- Circle C
- Double-headed arrow between N and C
- Arrow from T to C
- Arrow from C to T

Right side (Cell Kill - enclosed in a dashed box):
Molecular part of Cell Kill:
- Circle T_u with an arrow to Ø
- Circle T_b with an arrow to Ø

Cellular part of Cell Kill:
- Circle C with an arrow to N

Connections:
- Line from T_b (left) to T_b (right)
- Line from T (left) to T_u (right)
- Line from C (left) to C (right)

Fig. 2. Schematic of the model illustrating the cellular and molecular components. When cells are killed, C→ N and target receptors and the associated receptor complexes are eliminated, thereby reducing both T_u and T_b.
:chart::>


<a id='7f45bd03-a041-4b50-9f69-ac051d67cc8b'></a>

based on: (a) the volumes used are small and so diffusion should not be limiting during the timescales of the experiments, (b) we are not adding any further components (e.g. lipid particles) that may plausibly sequester the species considered and (c) no obvious precipitation is observed visually. Future studies are needed to verify these assumptions.

<a id='215029e7-b8bc-4922-9832-7c3fcfd51603'></a>

By applying the principle of mass balance to each dependent variable and appealing to the Law of mass action, we arrive at the following system of ODEs:

dA/dt = -k_on T_u A + k_off T_b (1)
Ab. target assoc. Ab. target dissoc.

dT_u/dt = -k_on T_u A + k_off T_b - f(T_b/(T+C)) (T_u/(T+C)) C (2)
target removal

dT_b/dt = k_on T_u A - k_off T_b - f(T_b/(T+C)) (T_b/(T+C)) C (3)
Ab./target complex removal

dN/dt = -β_on NT + β_off C + f(T_b/(T+C)) C (4)
NK/T assoc. NK/T dissoc. NK dissoc. after kill

<a id='750d4d03-4893-4391-98e1-548be0d89ffa'></a>

$$\frac{dT}{dt} = -\beta_{on}NT + \beta_{off}C, \qquad (5)$$

$$\frac{dC}{dt} = \beta_{on}NT - \beta_{off}C - f\left(\frac{T_b}{T+C}\right)C. \qquad (6)$$
$$\underbrace{\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad}_{\text{NK/T killing}}$$

<a id='9c734dca-e7a9-484c-9225-e26107c4f44c'></a>

Eqs. (1)–(3) define the subcellular dynamics. Antibodies, A, are as-
sumed to bind reversibly to unbound tumour receptors, T_u, at rate
k_on, forming bound tumour receptors, T_b, from which they disso-
ciate at rate k_off. We assume antibody is removed from the sys-
tem upon tumour cell death, via local release of proteolytic en-

<a id='88695c26-4239-4fcd-8bce-b0b0741b280d'></a>

zymes from the dying cell. We have no direct evidence under-pinning this assumption, but we feel it is reasonable as estab-lished protein preparation protocols routinely employ proteolytic enzyme inhibitors to avoid degradation of protein from lysed cells. Eqs. (4)-(6) define the cellular dynamics. NK cells, *N*, are assumed to bind reversibly to cancer cells, *T*, at rate β<sub>on</sub> forming cellu-lar conjugates, *C*, from which they dissociate at rate β<sub>off</sub>. While Deguine et al. (2012) report that antibody recognition by NK cells increases contact stability with cancer cells, for simplicity, we as-sume that the rates of NK-cancer cell association and dissociation are independent of bound antibodies (*T*<sub>b</sub>). We postpone to future work a comparison of this case with one in which β<sub>on</sub> and β<sub>off</sub> de-pend on *T*<sub>b</sub>/(*T*+*C*), the number of antibody-target receptor com-plexes per cancer cell.

<a id='ce3aa42f-6813-4bf3-b554-07f2e9049722'></a>

The subcellular and cellular dynamics are coupled by NK cell-mediated killing of the tumour cells. We suppose that NK cells bound to cancer cells kill the cancer cells at a rate, $f\left(\frac{T_b}{T+C}\right)$, which

<a id='458fd9d1-fd52-4716-a93d-6c17a0ad6d7a'></a>

is a monotonically increasing, saturating function of $\frac{T_b}{T+C}$, the number of antibody-target receptor complexes per cancer cell. We assume further that $f(0) = 0$ so that no killing occurs in the absence of bound antibody. As an illustrative example, we will use the following functional form for $f$,

<a id='e81cce1e-5e81-4419-8374-3b927b012eae'></a>

f(R) = f*_K R / (R + R_K) (7)

where f*_K represents the maximum rate of killing and R_K is the value of R = T_b / (T+C) at which the rate of killing is half-maximal. However, since much of the analysis presented in the remainder of the paper holds for more general choices for f (with f(0) = 0), where appropriate we will use the general form.

<a id='75371d94-94cf-40f9-852a-bc4c7e4d1a3d'></a>

After a tumour cell has been killed, NK cells can detach from their target and then move on to another target cell (see: Bhat and Watzl, 2007). We model this effect by supposing that when a tumour cell has been killed, the NK cell dissociates, giving rise to a source term in Eq. (4). Cancer cell killing is also accompanied by a reduction in unbound and antibody bound receptors. For simplicity, we assume that all cancer cells have the same number of receptors, which we denote by ρT, and, hence, that cancer cell death will reduce receptor numbers at a rate proportional to the cell death rate. Since the numbers of unbound and bound receptors per cancer cell are $\frac{T_u}{T+C}$ and $\frac{T_b}{T+C}$ respectively, we assume that unbound and bound receptors are removed from the system at rates $f(\frac{T_b}{T+C})\frac{T_u}{T+C}C$ and $f(\frac{T_b}{T+C})\frac{T_b}{T+C}C$, respectively (see Eqs. (2) and (3)).

We close Eqs. (1)-(6) by imposing suitable initial conditions. At the start of the experiment, antibodies, NK cells and cancer cells are added separately to a micro-well. Therefore we assume that at $t = 0$ no antibodies are bound to targets ($T_b(0) = 0$) and no NK cells are bound to cancer cells ($C(0) = 0$). We denote by $A_0$, $N_0$ and $T_0$ the initial concentrations of antibodies, cancer cells and NK cells so that $A(0) = A_0$, $N(0) = N_0$ and $T(0) = T_0$ and assume that initially all target receptors are unbound, so that $T_u(0) = ρ_T T_0$. To summarise, the initial conditions that close Eqs. (1)-(6) are

$A(0) = A_0, T_u(0) = ρ_T T_0, T_b(0) = 0, N(0) = N_0, T(0) = T_0$ and $C(0) = 0$. (8)

<a id='4845b4bb-bdba-4030-bbf6-12fd10c295bf'></a>

2.1. Model reduction, nondimensionalisation and variable transformation

<a id='75f43824-7876-45b5-9288-c23f5ac1ecdb'></a>

Inspection of Eqs. (1)-(6) reveals two conserved quantities which we may exploit to reduce our model from six equations to four. Firstly, adding Eqs. (4) and (6) and integrating subject to Eq. (8) supplies

$N + C = N_{0}.$
(9)

<!-- PAGE BREAK -->

<a id='1749ddda-78aa-44c0-8199-5bdd8b9512cd'></a>

42

<a id='a7c03af3-f631-4199-b907-6ef62b89c33e'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='fb914f7e-2649-4d99-846d-2bf386dea3dd'></a>

Eq. (9) states that the total concentration of NK cells (bound and unbound) remains constant during the experiment. Secondly, combining Eqs. (2), (3), (5) and (6) and exploiting Eq. (8) gives

$T_u + T_b = \rho_T (T + C)$, (10)

<a id='a4471776-f40a-45cf-b34e-017594f9d6d3'></a>

reflecting the fact that, at any given time, the total concentration of
target receptors (free and bound) is proportional to the total con-
centration of cancer cells (free and in complex), with constant of
proportionality \rho_{T}. We exploit these conservation laws to eliminate
N and T_{u} from Eqs. (1)-(8), which reduce to give,

<a id='760278f2-e32e-49ba-a50e-e5a81a0beb32'></a>

$\frac{dA}{dt} = -k_{on} (\rho_T (T+C) - T_b)A + k_{off} T_b,\quad(11)$

<a id='3043fbf2-559f-4058-aa90-911625dc7817'></a>

$$\frac{dT_b}{dt} = k_{on} (\rho_T (T + C) - T_b)A - k_{off}T_b - f\left(\frac{T_b}{T + C}\right) \frac{T_b}{T + C} C \quad (12)$$

<a id='76d13f7a-1c0f-4a39-8d15-0fed625ff9a2'></a>

dT/dt = -β_on (N_0 - C)T + β_off C, (13)

<a id='95bad47a-479c-4ee9-90a8-5a329525a5fd'></a>

$$\frac{dC}{dt} = \beta_{on} (N_0 - C)T - \beta_{off}C - f\left(\frac{T_b}{T+C}\right)C \quad (14)$$

<a id='cd7ce78c-df7f-4c79-bcba-dd5a3e9724c4'></a>

with A(0) = A₀, T♭ (0) = 0, T(0) = T₀ and C(0) = 0. (15)

<a id='e84ac2a2-5d74-40fb-ac48-61583adb5f89'></a>

To simplify the analysis that follows we replace $T_b(t)$ and $T(t)$ by two related dependent variables

$R(t) = \frac{T_b}{T+C}$ and $S(t) = T + C$.

(16)

<a id='e3ba9eb3-cd0c-42ca-a158-358b08bedaf9'></a>

Here R(t) is the number of antibody-receptor complexes per cancer cell and S(t) is the total concentration of cancer cells (free and bound to NK cells). Under this change of variables, Eqs. (11)–(15) become

<a id='f0af71f5-ba48-477f-be33-1f3f43e6edfe'></a>

dA/dt = -k_on (ρ_T S - RS)A + k_off RS, (17)

<a id='62bc7f90-2eac-489d-8cce-a2846d40a614'></a>

dR/dt = k_on (ρ_T - R)A - k_off R, (18)

<a id='6f3fb26f-979b-4ed1-9447-dc24472d3baf'></a>

dS/dt = -f(R)C, (19)

<a id='ee38248e-c152-46c2-b86a-5f54e0745be1'></a>

$$\frac{dC}{dt} = \beta_{on} (N_0 - C) (S - C) - \beta_{off}C - f(R)C \quad (20)$$

<a id='79070147-17e9-4c25-a7b8-5a52b0e3f18f'></a>

with $A(0) = A_0$, $R(0) = 0$, $S(0) = T_0$ and $C(0) = 0$.
(21)
In what follows it will be convenient to recast Eqs. (17)-(21) in
dimensionless form using the following rescaling

<a id='0a36f4c8-4b65-4834-a2e6-16536e297f54'></a>

A = A₀A*, R = ρTR*, S = T₀S*, C = T₀C*, t = t₀t*, (22)

<a id='d441fc9b-c946-4b27-8ba4-6114724ed56c'></a>

where $t_0$ is the timescale of the cytotoxicity assay. Under this transformation, Eqs. (17)-(21) become (on dropping the asterisks),

<a id='7e8df4f9-82c0-4a0e-a7c6-d39b7d41cf14'></a>

$\frac{dA}{dt} = -\alpha_1 (1 - R)AS + \alpha_2\gamma RS, \quad (23)$

<a id='2910f23e-9d01-4e5a-b565-b6745a8ce1df'></a>

dR / dt = α1 / γ (1 - R)A - α2R,
(24)

<a id='d3ebe44b-6947-4f31-b368-81a20cc9f0f9'></a>

$$\frac{dS}{dt} = -\hat{f}(R)C, \quad (25)$$

<a id='a827cbf5-bfb4-416a-a4ce-2b2f0c63e92e'></a>

dC/dt = v₁(μ – C)(S – C) – v₂C – ƒ(R)C. (26)

<a id='aa5d15ee-6856-4e61-8ca3-407a180a8091'></a>

In Eqs. (23)-(26) we have introduced the following dimensionless
parameter groupings and functions

<a id='95c38907-8bff-4c69-b76b-4deae43fd0ed'></a>

$\alpha_1 = k_{on}t_0\rho_T T_0$, $\alpha_2 = k_{off}t_0$, $\gamma = \frac{\rho_T T_0}{A_0}$, $\nu_1 = \beta_{on}t_0 T_0$,
$\nu_2 = \beta_{off}t_0$, $\mu = \frac{N_0}{T_0}$
(27)

<a id='3f93f814-55c2-49e1-8273-e0857dba93a2'></a>

and $\hat{f}(R) = t_0f(\rho_TR)$. (28)

<a id='195b619a-52ab-43f0-ad43-768ec800cdaf'></a>

2.2. Parameter estimation

<a id='fd94348c-6ec8-4d7d-8f01-57e9f6b61132'></a>

Dimensional and dimensionless estimates of the model param-
eters are presented in Tables 1 and 2 respectively. The latter are
obtained from the former using Eq. (27). Details of how these esti-
mates were obtained are presented in Appendix B.

<a id='cfd937cd-c68c-46b0-903d-ff0378fdb7fa'></a>

We note from Table 2 that two parameters are typically much smaller than the others: α₁ = O(10⁻⁶)–O(10²) and γ = O(10⁻⁹)–O(10²). For ADCC, α₁ and γ are fundamental quantities: α₁ is the product of the antibody association rate and the total number of target receptors initially present in the system while γ is the ratio of the number of target receptors to the number of antibodies initially present in the assay. In Table 3 we state order of magnitude estimates of α₁ and γ for three values of ρT and kon that span the range found in the literature (Bostrom et al., 2011; Ernst et al., 2005; Kute et al., 2012; Ward et al., 2011). In each case, the range of values of γ reflects the range of values of A₀ used in cytotoxicity assays.

<a id='a8301706-7c26-4eb0-9709-703e27066961'></a>

Of the antibody:cancer cell combinations represented in Table 3, the first row corresponds to the anti-CD20 antibody rituximab and CD20 expression in B cell cancers (Ernst et al., 2005; Ward et al., 2011). For rituximab, k_on = O(10³) M⁻¹s⁻¹, while target receptor levels in B cell cancers range from O(10³) to O(10⁷) receptors per cell. The parameter values in row 2 (columns 2 and 3) apply to the anti-HER2/neu antibody trastuzumab which is used to target HER2/neu expression in breast cancer (Bostrom et al., 2011; Kute et al., 2012). Trastuzumab has k_on = O(10⁵) M⁻¹s⁻¹ and is only prescribed for breast cancers with high HER2/neu expression (ρ_T > 10⁶ receptors per cell). Table 3 reveals that the dimensionless parameter α₁ may range in value from small to O(1) or larger, and that γ may also range from very small to large. We note, however, that for most of the parameter ranges recorded in Table 2, α₁ ≪ 1 and γ ≤ O(1). Therefore, in what follows we fix α₁ = ε ≪ 1 and investigate separately the cases γ = O(1), O(ε) and O(ε²).

<a id='1e9e2211-4fbf-4da4-be12-e423bb8ed798'></a>

Based on Table 2 we note that the (dimensionless) rate at which NK cells bind to cancer cells is large (${\nu}_{1}=O({\epsilon}^{-1})$). We will exploit this scaling in the asymptotic analysis presented in Section 4. First, to illustrate the relevance of the scalings to cytotoxicity assays, we fix $\epsilon=10^{-3}$, ${\rho}_{T}=10^{5}$ and indicate on Fig. 3 which cytotoxicity experiments correspond to each of the scalings for the dimensionless parameter $\gamma$ (${\gamma}=O(1)$ $O(\epsilon)$, and $O({\epsilon}^{2})$).

<a id='150ad2a7-4896-4fb5-a6a5-e285927ba4f3'></a>

## 3. Model dynamics

Before analysing our model, we present numerical results obtained by integrating Eqs. (23)–(26), using MATLAB’s inbuilt routine ODE15s (Mathworks, 2013). ODE15s uses a variable order method based on numerical differentiation formulae and is designed to solve stiff ODEs (Shampine and Reichelt, 1997). For illustrative purposes, we use the dimensionless form of the kill rate function given by Eq. (7)

f^(R) = f_K R / (R + R_K), (29)

<!-- PAGE BREAK -->

<a id='017cc007-6de6-4efb-875e-23716028946a'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='fe39804a-bcd4-4a8b-84a3-6d924aae1437'></a>

43

<a id='34f725f0-1fd6-40db-a27e-ed36ab43486e'></a>

Table 1
Summary of the parameters associated with Eqs. (11)-(15), together with estimates of their dimensional values.
<table id="4-1">
<tr><td id="4-2">Parameter</td><td id="4-3">Definition</td><td id="4-4">Estimated Value (units)</td><td id="4-5">Source</td></tr>
<tr><td id="4-6">ρT</td><td id="4-7">Number of receptors per cell</td><td id="4-8">10³ – 10⁷ (molecule cell⁻¹)</td><td id="4-9">Ward et al. (2011), Kute et al. (2012)</td></tr>
<tr><td id="4-a">kon</td><td id="4-b">Antibody binding rate</td><td id="4-c">10³ – 10⁷ (M⁻¹s⁻¹)</td><td id="4-d">Bostrom et al. (2011), Ernst et al. (2005)</td></tr>
<tr><td id="4-e">koff</td><td id="4-f">Antibody dissociation rate</td><td id="4-g">10⁻⁴ (s⁻¹)</td><td id="4-h">Bostrom et al. (2011), Ernst et al. (2005)</td></tr>
<tr><td id="4-i">βon</td><td id="4-j">Cell binding rate</td><td id="4-k">2 x 10³ (M⁻¹ s⁻¹)</td><td id="4-l">Almeida et al. (2011)</td></tr>
<tr><td id="4-m">βoff</td><td id="4-n">Cell dissociation rate</td><td id="4-o">10⁻³ (s⁻¹)</td><td id="4-p">Almeida et al. (2011)</td></tr>
<tr><td id="4-q">f(T/T+C)</td><td id="4-r">Cell kill function</td><td id="4-s">0 - 1.6 × 10⁻³ (s⁻¹)</td><td id="4-t">Vanherberghen et al. (2013)</td></tr>
<tr><td id="4-u">A0</td><td id="4-v">Initial antibody concentration</td><td id="4-w">6.67 × 10⁻¹² – 10⁻⁵ (M)</td><td id="4-x"></td></tr>
<tr><td id="4-y">N0</td><td id="4-z">Initial NK cell concentration</td><td id="4-A">4.15 × 10⁻¹⁶ – 8.30 × 10⁻¹⁵ (M)</td><td id="4-B"></td></tr>
<tr><td id="4-C">T0</td><td id="4-D">Initial tumour cell concentration</td><td id="4-E">4.15 × 10⁻¹⁶ (M)</td><td id="4-F">Ogbomo et al. (2006), Stewart et al. (2011)</td></tr>
<tr><td id="4-G">t₀</td><td id="4-H">Time-scale of experiment</td><td id="4-I">1.44 x 10⁴ (s)</td><td id="4-J">Ogbomo et al. (2006), Stewart et al. (2011)</td></tr>
</table>

<a id='e9baa4cb-8c13-4aa4-bcfc-e2e118522898'></a>

Table 2
Summary of the dimensionless parameters associated with Eqs. (23)-(26), together with estimates of their values
(see also Eq. (27)).

<table id="4-K">
<tr><td id="4-L">Parameter</td><td id="4-M">Definition</td><td id="4-N">Description</td><td id="4-O">Estimated value</td></tr>
<tr><td id="4-P">α1</td><td id="4-Q">kontρT0</td><td id="4-R">Dimensionless antibody binding rate</td><td id="4-S">5.8 x 10^-6 - 5.8 x 10^2</td></tr>
<tr><td id="4-T">α2</td><td id="4-U">kofft0</td><td id="4-V">Dimensionless antibody dissociation rate</td><td id="4-W">1.44</td></tr>
<tr><td id="4-X">γ</td><td id="4-Y">ρT0/A0</td><td id="4-Z">Initial ratio of total number of receptors to antibody</td><td id="4-10">6.22 x 10^-9 - 6.22 x 10^2</td></tr>
<tr><td id="4-11">ν1</td><td id="4-12">βont0T0</td><td id="4-13">Dimensionless cell binding rate</td><td id="4-14">1.2 x 10^2</td></tr>
<tr><td id="4-15">V2</td><td id="4-16">βofft0</td><td id="4-17">Dimensionless cell dissociation rate</td><td id="4-18">14.4</td></tr>
<tr><td id="4-19">μ</td><td id="4-1a">N0/T0</td><td id="4-1b">Initial ratio of NK cells to tumour cells</td><td id="4-1c">1-20</td></tr>
<tr><td id="4-1d">f(R) (image: f(R) with hat)</td><td id="4-1e">t0f((ρrT0)/(C+S))</td><td id="4-1f">Dimensionless cell kill rate</td><td id="4-1g">0 to 22.4</td></tr>
</table>

<a id='77e86cd7-69e9-47d5-b8c0-0a4f11177a3a'></a>

Table 3
Table showing how the dimensionless parameters $\alpha_1 = k_{on}t_0\rho_T T_0$ and $\gamma = \frac{\rho_T T_0}{A_0}$ (see
Eq. (27) and Table 2) vary with $\rho_T$ and $k_{on}$. Since $\gamma$ is inversely related to $A_0$ via Eq. (27),
the range of values of $\gamma$ stated for each value of $k_{on}$ and $\rho_T$ is due to the range of values
of $A_0$ stated in Table 1 where $A_0 \in [6.67 \times 10^{-12}, 6.67 \times 10^{-5}]$M.

<table id="4-1h">
<tr><td id="4-1i"></td><td id="4-1j">ρ_T = 10^3</td><td id="4-1k">ρ_T = 10^5</td><td id="4-1l">ρ_T = 10^7</td></tr>
<tr><td id="4-1m">k_on = 10^3</td><td id="4-1n">α_1 = O(10^-6),</td><td id="4-1o">α_1 = O(10^-4)</td><td id="4-1p">α_1 = O(10^-2),</td></tr>
<tr><td id="4-1q"></td><td id="4-1r">γ = O(10^-9) - O(10^-2),</td><td id="4-1s">γ = O(10^-7) - O(1)</td><td id="4-1t">γ = O(10^-5) - O(10^2)</td></tr>
<tr><td id="4-1u">k_on = 10^5</td><td id="4-1v">α_1 = O(10^-4),</td><td id="4-1w">α_1 = O(10^-2),</td><td id="4-1x">α_1 = O(1),</td></tr>
<tr><td id="4-1y"></td><td id="4-1z">γ = O(10^-9) - O(10^-2)</td><td id="4-1A">γ = O(10^-7) - O(1)</td><td id="4-1B">γ = O(10^-5) - O(10^2)</td></tr>
<tr><td id="4-1C">kon = 107</td><td id="4-1D">α₁ = 0(10-2),</td><td id="4-1E">α₁ = 0(1),</td><td id="4-1F">α₁ = 0(102),</td></tr>
<tr><td id="4-1G"></td><td id="4-1H">γ = 0(10-9)-0(10-2)</td><td id="4-1I">γ = 0(10-7)-0(1)</td><td id="4-1J">γ = 0(10-5)-0(102)</td></tr>
</table>

<a id='4509a741-d075-4b63-8377-e3103a757913'></a>

<::Figure: Line chart with shaded areas::>
<::Chart::>
Chart title: Cytotoxicity data from Fig. 1
Y-axis label: %kill
Y-axis range: -20 to 120
X-axis label: antibody(µg/ml)
X-axis range: 0 to 10

The chart displays multiple red lines with triangular markers, grouped into several series, some with shaded red regions. There is a gray vertical bar on the left side of the plot, obscuring part of the y-axis.

Three blue dashed rectangles highlight different regions of the chart:
- A rectangle on the left, covering the range from approximately 0 to 10^-5 on the x-axis, is labeled "γ=1".
- A rectangle in the middle, covering the range from approximately 10^-3 to 10^-2 on the x-axis, is labeled "γ=ε".
- A rectangle on the right, covering the range from approximately 1 to 10 on the x-axis, is labeled "γ=ε²".

On the right side of the chart, next to the data lines, are labels: 20:1, 10:1, 5:1, 2.5:1, and 1.25:1.

Fig. 3. Cytotoxicity data from Fig. 1, with the blue rectangles indicating which data corresponds to the three asymptotic cases of interest (γ = O(1), O(ε) and O(ε²)). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
<::/Chart::>
<::/Figure::>

<a id='15de6759-f686-4353-b3e2-d599a73e68d4'></a>

where f_K represents the maximum rate of killing (dimensionless)
and R_K is the value of R at which the rate of killing is half-
maximal. In what follows, we fix f̂_K = 1 and R_K = 0.5. We suppose

<a id='e9d92c34-878e-49b2-9a95-6cb2e95ca64a'></a>

that α₁ = € = 10⁻³ and that the initial ratio of NK cells to cancer
cells is 20:1. With the exception of γ, all other parameters are as-
signed values as per Table 2. The numerical results presented in
Fig. 4 show how the system dynamics change as γ varies. We plot
the time evolution of R(t), S(t) and C(t) (see Eqs. (23)-(26)). The
dynamics of A(t) are omitted since, for this choice of parameters,
A(t)≈1 for the timescale of interest (0≤t≤1).

<a id='b7031a15-b121-4aae-b49a-81490f385709'></a>

For all values of γ, at early times (when 0 < t < 10^-3), the total number of cancer cells, S(t) = T(t) + C(t), remains constant (S(t)≈1), and cell killing is negligible. During this time, cancer cells form complexes with NK cells (C(t) increases from zero to a maximum value which decreases in magnitude as γ decreases). On a longer time-scale, R(t), the number of receptors per cancer cell bound by antibodies, increases at a rate which increases as γ decreases (i.e., as antibody levels increase). When γ = ε^2, antibody is plentiful and rapidly binds to all available receptor so that R(t)≈1 for t ≈ 10^-2. In this case, receptor saturation is sustained for the remainder of the simulation, because the ratio of antibody to target receptors is large. The increase in R(t) stimulates the killing of cancer cells by bound NK cells, so S(t) and C(t) decline over a similar time-scale. This effect is more pronounced for smaller values of γ. Indeed, for smaller values of γ the dynamics associated with R(t), S(t) and C(t) merge (see Fig. 4(C)). By contrast, when γ = O(1), the simulations needs to be continued for longer times in order to see a significant reduction in the number of cancer cells (see Fig. 4(A)).

<a id='1feab1f5-cda1-499c-88d7-80b7c116161e'></a>

We emphasise that the main aim of Fig. 4 is to show how the
dynamic behaviour of the model changes as the dimensionless pa-
rameter y varies. Since the experimental data were collected at

<!-- PAGE BREAK -->

<a id='ff0fe152-78f6-4d25-b8b8-37cae7189f1e'></a>

44

<a id='347286e6-ec5d-4626-8119-f677ad402211'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='0582e338-f1fe-404f-b976-568573a62779'></a>

<::chart: Fig. 4. Series of numerical results, obtained by solving the dimensionless Eqs. (23)–(26) with $\hat{f}(R)=\frac{f_{K}R}{R+R_{K}}$. The simulation results show how the time evolution of the number of antibody-receptor complexes per cancer cell, $R(t)=\frac{T_{b}}{T+C}$ (solid line), the total concentration of cancer cells, $S(t)=T+C$ (dotted line), and the concentration of cancer cells bound to NK cells, $C(t)$ (dashed line), change as we vary $\gamma$, the ratio of the initial number of target receptors to the initial number of antibodies. Each panel shows the y-axis ranging from 0 to 1 and the x-axis as log(t) ranging from -7 to 0. A legend in Panel A indicates the solid line as R(t), the dashed line as C(t), and the dotted line as S(t). Panel (A) corresponds to low antibody levels ($\gamma=1$). In this panel, R(t) (solid line) starts at 0, rises sharply, and then plateaus near 1. C(t) (dashed line) follows a similar trajectory, rising sharply and then leveling off near 1. S(t) (dotted line) remains constant at 1. Panel (B) is for intermediate levels of antibody ($\gamma=\epsilon$). Here, R(t) (solid line) rises to a lower peak (around 0.15) and then plateaus. C(t) (dashed line) rises sharply to near 1, then decreases sharply. S(t) (dotted line) remains at 1 for most of the duration, with a slight dip towards the end. Panel (C) is for high levels of antibody ($\gamma=\epsilon^{2}$). In this panel, R(t) (solid line) rises sharply to 1 and then plateaus. C(t) (dashed line) rises sharply to near 1, then decreases sharply to near 0. S(t) (dotted line) remains at 1 for most of the duration, then decreases sharply to near 0. Parameter values: as per Table 2, with $\hat{f}_{k}=1, R_{K}=0.5, \alpha_{1}=\epsilon=10^{-3}, \mu=1$.::>

<a id='1805c221-6d22-4336-bf7d-f8416e0de6f3'></a>

a single time-point, it is not possible to compare these numer- ical results to the experimental data. Rather, the numerical re- sults highlight the additional insight that is afforded by develop- ing a dynamic model of ADCC. We note also that the duration of the numerical simulations matches that of the experiments (4 h in dimensional terms). It is not appropriate to extend the simu- lations beyond this timescale because processes which have been neglected, such as cell proliferation and natural cell death, become important.

<a id='46232c67-9aba-4a46-858a-15008aaf308c'></a>

To summarise, the numerical simulations presented in
Fig. 4 show that the system dynamics act on two different
timescales. On the short timescale, tumour cell killing is neg-
ligible, NK- cancer conjugation approaches equilibrium and, if

<a id='ed6ca90c-545f-42f7-b4c1-eb407994ff86'></a>

antibody levels are high enough, the binding of antibodies to target receptors increases towards an equilibrium. On a longer time-scale the number of antibodies bound to target receptors becomes large enough to induce NK cells to kill cancer cells.

<a id='f30a3b38-98d0-48a1-95d6-90e7277274cf'></a>

## 4. Perturbation analysis

In this section we focus on the parameter scalings introduced
in Section 2.2 and use perturbation methods to construct approx-
imate solutions on the short and long timescales. We recall from
Tables 2 and 3, that v₁, the rate at which NK cells bind to can-
cer cells, is large while α₁, the product of the antibody association
rate and the total number of target receptors initially present in
the system, is typically small. Accordingly, fixing α₁ = ∈ ≪ 1 and

<!-- PAGE BREAK -->

<a id='62672fbe-961f-4c86-b159-b9a358ce1592'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='8c3152fd-9fbb-42df-9eb6-bb8effbf7557'></a>

45

<a id='77a1893c-2c9d-40b9-a362-71f47e787419'></a>

v₁ = v̂₁/ϵ, Eqs. (23)-(26) supply

dA/dt = -[ϵ(1 - R)A - α₂γR]S, (30)

dR/dt = 1/γ [ϵ(1 - R)A - α₂γR], (31)

dS/dt = -f̂(R)C, (32)

dC/dt = v̂₁/ϵ (μ - C)(S - C) - v₂C - f̂(R)C, (33)

with A(0) = 1, R(0) = 0, S(0) = 1 and C(0) = 0. (34)

<a id='076239e5-6092-4a9e-a067-bf31a28b37b4'></a>

Eqs. (30)-(34) define a singular perturbation problem which we analyse on two timescales. We construct an *inner* solution on a short timescale for which $t = O(\epsilon)$ and match this to an *outer* solution which evolves on a longer timescale, for which $t = O(1)$. From Fig. 4 it is clear that details of the solutions change as $\gamma$ varies. For example, when $0 < \gamma \ll 1$ the two timescales merge. While details of the solutions change as $\gamma$ varies, the approach is similar and, therefore, we focus our analysis on the case $\gamma = O(1)$.

<a id='d94656e4-1207-41e0-beb6-c2da5463eebe'></a>

4.1. Analysis for γ = O(1)

For the inner solution, we rescale time so that t = ετ and de-fine
a(τ) = A(t), r(τ) = R(t), s(τ) = S(t), c(τ) = C(t).
Then Eqs. (30)-(34) transform to give

$\frac{da}{dτ} = -ε[ε(1 - r)a - α_2γr]s,\qquad (35)$

$\frac{dr}{dτ} = \frac{ε}{γ}[ε(1 - r)a - α_2γr],\qquad (36)$

$\frac{ds}{dτ} = -ε\hat{f}(r)c,\qquad (37)$

$\frac{dc}{dτ} = \hat{v}_1(μ - c)(s - c) - εv_2c - ε\hat{f}(r)c,\qquad (38)$

<a id='94707999-e7f6-4500-b8f3-b2ed8b02d190'></a>

with $a(0) = 1$, $r(0) = 0$, $s(0) = 1$ and $c(0) = 0$. (39)
We seek trial solutions of the form
$a(\tau) = a_0(\tau) + \epsilon a_1(\tau) + \epsilon^2 a_2(\tau) + O(\epsilon^3)$, (40)
with similar expansions for $r(\tau)$, $s(\tau)$ and $c(\tau)$. Substituting these
trial solutions in Eqs. (35)-(39) and equating to zero coefficients of
$O(1)$, $O(\epsilon)$ and $O(\epsilon^2)$ yields the following approximate solutions for
$a$, $r$, $s$ and $c$:
$a(\tau) = 1 - \epsilon^2 \tau + O(\epsilon^3)$, (41)
$r(\tau) = \frac{\epsilon^2 \tau}{\gamma} + O(\epsilon^3)$, (42)
$s(\tau) = 1 + O(\epsilon^3)$, (43)
$c(\tau) = \mu \frac{(1 - e^{-\hat{v}_1 (\mu-1)\tau})}{(\mu - e^{-\hat{v}_1 (\mu-1)\tau})} + O(\epsilon)$. (44)

<a id='862b8d02-57b1-4681-b4b9-ae0c6410792f'></a>

Thus, on the short timescale, _s_ remains constant (to O(ε³)), while _a_ decreases, and _r_ increases, linearly with time, these effects being small (O(ε²)). The dominant effect is an increase in _c_ from _c_ = 0 to _c_ = 1. Thus, we conclude that, at early times, the system dynamics are dominated by binding of NK cells to cancer cells, until all cancer cells are complexed with NK cells (_s_ ≈ _c_ ≈ 1). In particular, at leading order, the cell dynamics are independent of the choice of the cell kill function, _f_(.). Now, the long-time limit (τ → ∞) of the short timescale solutions should match the short time behaviour of the system on the long timescale. Thus we deduce that the initial conditions for _A_, _R_ and _S_ on the longer timescale are identical to Eq. (34) whereas _C_(0) = 1.

<a id='eea06501-42e1-4eb3-8e43-fba2dbbfb254'></a>

We now construct approximate solutions on the longer
timescale, $t = O(1)$. Matching to the inner solution leads us to im-
pose the following initial conditions:

<a id='96a5946e-abd4-4181-a61e-670f0b946584'></a>

A(0) = 1, R(0) = 0, S(0) = 1 and C(0) = 1. (45)

<a id='10d5a04b-4ad1-439f-ad39-8ad54f6b7bff'></a>

We assume regular power series expansions for A(t) of the form

<a id='24d82f9d-fe67-4356-971e-a6eb82a7457c'></a>

A(t) = A₀(t) + εA₁(t) + O(ε²),

(46)

<a id='ab26ed43-9059-4ea5-aa9d-7431a37b41b4'></a>

with similar expressions for R(t), S(t) and C(t). Substituting these
trial solutions in Eqs. (30)-(33) and equating to zero coefficients of
O(1) and O(\epsilon), it is straightforward to obtain the following expres-
sions for the dependent variables

<a id='4731d8e4-1f37-4f83-b9bb-1343fcb5f9c0'></a>

A(t) = 1 - \frac{\epsilon}{\alpha_2} (1 - e^{-\alpha_2 t}) + O(\epsilon^2), (47)

<a id='dc278e17-1a8b-4425-99d8-46f5f1f4eb0e'></a>

R(t) = \frac{\epsilon}{\alpha_2\gamma}(1 - e^{-\alpha_2 t}) + O(\epsilon^2), (48)

<a id='edf53938-5fd2-4b33-a751-9c2ba9118dda'></a>

S(t) = 1 - \frac{\epsilon \hat{f}'(0)}{\alpha_2 \gamma} \left(t - \frac{1}{\alpha_2}(1 - e^{-\alpha_2 t})\right) + O(\epsilon^2),\quad(49)

<a id='0c68edb8-6418-4d00-8167-ae5d3fd9a18e'></a>

C(t) = 1 - \frac{\epsilon\hat{f}'(0)}{\alpha_2\gamma} \left(t - \frac{1}{\alpha_2}(1 - e^{-\alpha_2 t})\right) - \frac{\epsilon v_2}{v_1(\mu - 1)} + O(\epsilon^2).

(50)

<a id='e71c7d50-1b88-4101-aca0-e728eb9940f3'></a>

As expected from the numerical results presented in Fig. 3(a),
when γ = O(1) and antibody levels are low, tumour cell killing
is negligible during the timecourse of the experiments (t = O(1)).
Eqs. (47)–(50) reveal how the system dynamics depend on the
model parameters and, in particular, on f'(0), the slope of the kill
rate function at R = 0. For example, A(t) decays exponentially at
rate α2. As such, these expressions reveal how time-resolved ex-
perimental data might be used to estimate the model parameters.
Using Eqs. (47)–(50) it is possible to derive the following approx-
imate expression for the percentage of tumour cells killed during
the experiment.

<a id='85478504-5e41-4b04-8114-07458740ede6'></a>

(Percentage of tumour
cells killed at t = 1)
= 1 - S(t=1)/S(t=0) ≈ (εf'(0))/(α₂γ) (1 - (1/α₂) (1 - e^(-α₂))) (51)

<a id='5cbdb883-1e3b-4645-bc95-a6ea81a5a8b8'></a>

Eq. (51) reveals that, when antibody levels are low, the percentage cell kill depends only on the slope of the cell kill rate function at the origin, f'(0). As a particular example, we note that, when γ = O(1) and the cell kill rate is defined by Eq. (7), the percentage kill during the lysis experiment depends on f'(0) = fK/RK. Given values of the parameters α2, γ and ε, we can use this expression to estimate f'(0), the slope of the cell kill rate function at the origin.

<!-- PAGE BREAK -->

<a id='62004cd3-d03c-4ef3-b2b3-4e220e6f7aed'></a>

46

<a id='b5b1f733-2308-4836-bea4-9cdb44b5a035'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='3239eb69-8a99-4c02-8cca-9be150e2e464'></a>

4.2. Analysis for ̵ = O(̈)

<a id='bd0b90f1-4c7d-443f-a409-2255d81b3dcd'></a>

It is straightforward to adapt the above analysis for the case
γ = O(ε): we seek trial solutions of the form in Eqs. (40) and
(46) on the short and long timescales respectively. Behaviour on
the short timescale t = ετ is similar to that for γ = O(1): binding
of NK cells to tumour cells dominates the system dynamics, with
changes in A, R and S being negligible while C increases rapidly
until all tumour cells are bound to NK cells (results not presented).
As a result, we deduce that the initial conditions that apply on the
long timescale are given by Eq. (45). For t = O(1) and γ = εỹ, sub-
stituting with trial solutions of the form in Eq. (46) in Eqs. (30)-
(33) we deduce that, at leading order,

<a id='b395db71-f0b6-40c4-a3c7-28c4a7dfc664'></a>

A(t) = 1 + O(€), (52)

<a id='511c25f8-6bc4-42d9-a87f-88820c8ffc89'></a>

R(t) = 1 / (1 + α₂ỹ) (1 - e^(-θt/ỹ)) + O(ε),

(53)

<a id='21252522-5b9a-4484-a508-a6304538d7fd'></a>

S(t) = 1 - ∫₀ᵗ f̂(R₀)dt + O(ε), (54)

<a id='c2197c18-871b-4937-9713-35c7b0a6075a'></a>

C(t) = 1 - \int_{0}^{t} \hat{f}(R_0)dt + O(\epsilon), (55)

<a id='f0d44c30-3d3a-4e33-a319-94d2e327af3b'></a>

where θ = (1 + α₂ỹ)/ỹ.
Eqs. (52)-(55) hold for a general cell kill rate function, ƒ(.). As
an illustrative example, we note that, with γ = εỹ, ƒ(R) defined
by Eq. (7), and R(t) defined by Eq. (53), the expression for S(t) be-
comes:

<a id='85a78761-aa2f-4f87-b5a3-75fbf3ad14e1'></a>

S(t) \approx 1 - f_K \left\{ t - \frac{R^*_K}{1 + R^*_K} \frac{1}{\theta} \log \left( \frac{(1 + R^*_K)e^{\theta t} - 1}{R^*_K} \right) \right\}.

<a id='18645611-6ede-42fa-aed0-7d5dfe5c579b'></a>

Using Eq. (51), we deduce further that when f̂(R) is defined by
Eq. (7) the percentage of tumour cells killed during the lysis assay
can be written as:

<a id='f5850fc9-75c8-4035-b746-b9a143064a3f'></a>

(Percentage of tumour cells killed at t = 1) = 1 - S(t = 1) / S(t = 0) = ∫_0^1 f̂(R_0)dt

<a id='79feb1d9-c869-4ffa-ba58-54ad24e082b4'></a>

$$ = \int_0^1 \frac{f_k R_0(t)}{R_0(t) + R_K} dt \quad (56) $$

<a id='faea8793-7f1e-4ac9-8609-b027f7a72e79'></a>

= f_K { 1 - R_K^* / (1 + R_K^*) * (1 / \theta) * log ( ((1 + R_K^*)e^\theta - 1) / R_K^* ) } . (57)

<a id='e322793b-4950-44a0-96cf-4b1743ac4688'></a>

where $R_K^* = R_K (1 + \alpha_2 \tilde{\gamma})$. Comparison of Eqs. (51) and (57) highlights the way in which the percentage of tumour cells killed at the end of the cytotoxicity assay (t = 1), particularly the nature of its dependence on the cell kill rate function $\hat{f}$, changes as $\gamma$ decreases from $\gamma = O(1)$ to $\gamma = O(\epsilon)$.

<a id='273f9ef1-c5a4-48e5-ab78-edd842618aee'></a>

4.3. Analysis for \u03b3 = O(\u03f5\u00b2)

<a id='0786b4ff-ba08-4265-8af1-6cc58d21c303'></a>

When γ = ε^2ŷ, we again seek trial solutions of the form given
in Eqs. (40) and (46) on the short and long timescales respectively.
In this way it is possible to derive the following leading order solutions for the dependent variables on the short timescale t = ετ:
a(τ) = 1 + O(ε^2),
(58)

<a id='a42d6e53-77f5-47e6-9555-fb98a35729f9'></a>

r(τ) = 1 - e^{-τ/ŷ} + O(ϵ),
(59)

<a id='723d7729-261c-4b2e-b916-5cf438fca6d6'></a>

s(τ) = 1 + O(ϵ), (60)

<a id='c41a3326-07b8-4d8e-b39a-d4541bf75da8'></a>

c(τ) = μ * ( (1 - e^(-ν̂_1 (μ-1)τ)) / (μ - e^(-ν̂_1 (μ-1)τ)) ) + O(ε),

(61)

<a id='62503fa9-c151-46f9-a0d9-1308bdf1796f'></a>

We note that the dynamics for _a_, _s_ and _c_ associated with the cases $\gamma=O(1)$ and $\gamma=O(\epsilon)$ are identical (see Eqs. (41)–(44) for example). However, since initial antibody levels are now much greater than the initial number of receptors on the tumour cells, the receptors become saturated with antibody on the same short timescale as that on which the NK cells bind to the tumour cells. Matching from the short to the long timescale requires that the following initial conditions be used to determine the solutions on the long timescale:
A(0) = 1, R(0) = 1, S(0) and C(0) = 1.

<a id='6fc516ec-4b8d-4638-a094-fa3ec0326509'></a>

Substituting with trial solutions of the form shown in Eq. (46) in
Eqs. (30)-(33) and equating to zero coefficients of O(1) yields the
following leading order expressions for the dependent variables:

A(t) = 1 + O(€²)
(62)

<a id='d40c8a8d-71ee-437e-9591-43be01a8053d'></a>

R(t) = 1 - εα₂ŷ + O(ε²), (63)

<a id='4b68e557-00bd-4b69-afc6-206969bc2a2c'></a>

S(t) = e⁻ᶠ̂⁽¹⁾ᵗ + O(ε), (64)

<a id='f97af5ee-610b-4a7e-8c07-2e909bbeea83'></a>

C(t) = e^{-\hat{f}(1)t} + O(\epsilon).
(65)

<a id='9256756d-6331-4296-b746-27249c70b4f7'></a>

Using Eq. (51) we deduce further that the percentage of tumour cells that have undergone lysis at t = 1 is given by

<a id='0db651bb-cfb0-4bb2-ad75-70846ef37c66'></a>

(Percentage of tumour cells killed at t = 1) = 1 - S(t = 1) / S(t = 0) = 1 - e^(-f^(1))

= 1 - exp(-f_K / (1 + R_K)) (66)

<a id='dc1fb7ce-72a4-473f-a03f-b2b7be418c8d'></a>

Eq. (66) reveals that when γ = O(ε^2) the percentage tumour cell
kill at the end of cytotoxicity assay can be estimated by evaluating
the cell kill rate function f̂(R) at R = 1. Comparison of Eqs. (51),
(57) and (66) shows further how when f̂(R) = f_KR/(R+R_K) the
different assays provide complementary information about the pa-
rameters associated with the cell kill rate function. Combining
these together gives

<a id='251a96c9-1864-455b-8a6b-fcfcde1cb25c'></a>

(Percentage of tumour cells killed at t = 1)

$$\approx \begin{cases}
\frac{\epsilon f_K}{\alpha_2\gamma} \left(1 - \frac{1}{\alpha_2} (1 - e^{-\alpha_2})\right) & \text{for } \gamma = O(1), \\
f_K \left\{1 - \frac{R_K^*}{1+R_K^*} \frac{1}{\theta} \log\left(\frac{(1+R_K^*)e^\theta - 1}{R_K^*}\right)\right\} & \text{for } \gamma = O(\epsilon), \quad (67) \\
1 - \exp\left(-\frac{f_K}{1+R_K}\right) & \text{for } \gamma = O(\epsilon^2).
\end{cases}$$

<a id='2a933459-be6d-4aa9-a895-2d39f875a554'></a>

where R*K = RK(1 + α2γ̃).

<a id='7bf0fa1e-9896-4a52-bf25-b1a86889fce0'></a>

4.4. Comparison with numerics

In Fig. 5 we compare the short and long time solutions for R(t) and C(t) to numerical solutions of the full model (Eqs. (30) - (34)). For clarity we omit the variables A(t) and S(t). We observe good agreement between the approximate solutions and solutions of the full model for the three cases of interest (γ=O(1), O(ϵ) and O(ϵ^2)).

<!-- PAGE BREAK -->

<a id='5f221153-b923-4b4a-853d-11f0da3ba0d8'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='08b565ed-b5e7-4cae-b91c-35a438b8b2c2'></a>

47

<a id='7127bb1a-7432-403c-a775-a9cc52d2e954'></a>

A) <::chart: Panel A, titled "γ = 1", shows a plot with y-axis ranging from 0 to 1 and x-axis labeled "log(τ)" ranging from -7 to 0. The plot displays six curves: R(τ) (black solid line), C(τ) (black dashed line), R_0(τ), inner (blue solid line), C_0(τ), inner (blue dashed line), R_0(τ), outer (red solid line), and C_0(τ), outer (red dashed line). The blue dashed line (C_0(τ), inner) rises sharply from 0 to 1 between log(τ) = -5 and -3. The black solid line (R(τ)) and blue solid line (R_0(τ), inner) overlap, rising from 0 to 1 and then plateauing. The red solid line (R_0(τ), outer) and red dashed line (C_0(τ), outer) also overlap, staying at approximately 1 across the x-axis range. B) Panel B, titled "γ = ε", shows a plot with y-axis ranging from 0 to 1 and x-axis labeled "log(τ)" ranging from -7 to 0. The blue dashed line (C_0(τ), inner) rises sharply from 0 to 1 between log(τ) = -5 and -3, then falls sharply to near 0 between log(τ) = -2 and -1, before rising slightly. The red dashed line (C_0(τ), outer) starts near 1, drops, and then rises to a value around 0.2 at log(τ) = 0. The black solid line (R(τ)) and blue solid line (R_0(τ), inner) overlap, rising from 0 to 1 and then plateauing. The red solid line (R_0(τ), outer) also rises from 0 to 1 and plateaus. C) Panel C, titled "γ = ε^2", shows a plot with y-axis ranging from 0 to 1 and x-axis labeled "log(τ)" ranging from -7 to 0. The blue dashed line (C_0(τ), inner) rises sharply from 0 to 1 between log(τ) = -4 and -2, then falls sharply to near 0 between log(τ) = -2 and -1. The red dashed line (C_0(τ), outer) starts near 1, drops, and then rises to a value around 0.4 at log(τ) = 0. The black solid line (R(τ)) and blue solid line (R_0(τ), inner) overlap, rising from 0 to 1 and then plateauing. The red solid line (R_0(τ), outer) also rises from 0 to 1 and plateaus. Fig. 5. Series of plots showing good agreement between the approximate solutions derived in Section 4 on the short (blue curves) and long (red curves) timescales and numerical solutions of the full model (see Eqs. (23)-(26)) when f(R) = f_R R/(R+R_K) and as we vary γ, the ratio of the initial number of target receptors to the initial number of antibodies. As in Fig. 4, Panel (A) corresponds to low antibody levels (γ = 1), Panel (B) to intermediate levels (γ = ε) and Panel (C) to high levels (γ = ε^2). In each sub-Panel, we present profiles for the number of antibody-receptor complexes per cancer cell, R(t) = T/(T+R_K) (solid lines) and the concentration of cancer cells bound to NK cells, C(t) (dashed lines). Parameter values: as per Fig. 4, with (A) γ = 1; (B) γ = ε = 10^-3; (C) γ = ε^2 = 10^-6. Key: numerical solutions of the full model for R(t) (black solid line) and C(t) (black dashed line); leading order inner solutions for R(t) (blue solid line) and C(t) (blue dashed line) on the short timescale t = O(ε); leading solutions for R(t) (red solid line) and C(t) (red dashed line) on the long timescale, t = O(1). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)::> 

<a id='c48e8320-3a25-42cf-9cd7-6d54301246bd'></a>

## 5. Discussion

Antibody-based cancer therapy is now one of the most successful and important strategies for treating patients with cancer (Scott et al., 2012). ADCC, antibody directed killing of tumour cells by natural killer cells is one of the main mechanisms of action of many clinically successful therapies (Vacchelli et al., 2015). _In vitro_ cytotoxicity assays have been instrumental in developing ADCC mediating antibodies for clinical use.

<a id='f6392574-c8fd-477d-9be9-cecec532d910'></a>

Previous mathematical models of cytotoxicity assays, formu-
lated as systems of time-dependent ordinary differential equations
(ODEs), focussed on antibody-independent killing mechanisms and,
therefore, assumed a constant kill rate (Callewaert et al., 1978;
Thorn and Henney, 1976; 1977; Zeijlemaker et al., 1977). In this
paper we have relaxed these assumptions to develop a new model
in which tumour cell kill rates depend on how much antibody is
bound to target receptors on the cancer cells. By applying pertur-
bation methods we were able to show how information about the

<!-- PAGE BREAK -->

<a id='b6c49a5b-e22f-4851-a829-45f2e29f01a7'></a>

48

<a id='b0b516aa-6a20-413b-81b6-9e9186bf5849'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='93512f44-abe0-4a77-b9cc-7f3d8b21cdbe'></a>

rate at which NK cells kill tumour cells can be extracted from in vitro cytotoxicity data.

<a id='3a411ef8-0058-4f27-8715-d164247d3741'></a>

In more detail, we used the experimental literature to estimate the model parameters and, in this way, identified two dimension-less parameters which take extremal values and a third which can vary over several orders of magnitude. In particular, the param-eter 0 < α₁ << 1 is the product of the association rate of an anti-body for its target (k_on), and the concentration of target receptors. The parameter v₁ >> 1 is the product of the NK-cancer cell bind-ing rate and the initial concentration of cancer cells. Finally, the parameter γ is the ratio of the concentration of target receptors to antibodies, and may take values across several orders of magni-tude. We introduced the small parameter 0 < ε << 1 and fixed α = ε and v₁ = O(ε⁻¹). We exploited the extremal values of α₁ and v₁ to simplify the model equations, and investigated separately three cases characterised by different values of γ: γ = O(1), O(ε) and O(ε²), these values of γ reflecting the range of values of the ini-tial ratio of antibody numbers to target receptors that are typically used in ADCC cytotoxicity assays (see Fig. 3). In all cases, the sys-tem dynamics evolved on two time-scales, one fast (t = O(ε)) and one slow (t = O(1)). We used perturbation methods to derive ap-proximate expressions for the dependent variables on each time-scale and showed that these were in good agreement with numer-ical solutions of the full model.

<a id='6b62d167-a887-43c9-86a3-66212cc3a43d'></a>

The approximate solutions enabled us to relate the rate at which NK cells kill in response to binding antibody to the percentage of cancer cells killed at the end of a cytotoxicity assay and to determine how different initial antibody levels yield different information about the functional form of the kill rate function. This has implications for the information that can be gained about the efficacy of antibodies from cytotoxicity assays. In particular, when γ = O(1), the concentration of antibodies is the same order of magnitude as targets, killing is negligible and proportional to *f'*(0), the slope of the cell kill rate function at the origin. At intermediate antibody levels, γ = O(ϵ), the kill rate depends on the integral of the kill rate function. Finally, when γ = O(ϵ²), antibody levels greatly exceed target levels, targets are saturated on a fast time-scale and killing proceeds at its maximum rate, *f*(1). Thus, in this case, information about the maximum rate of NK-cancer cell killing can be inferred.

<a id='dbafddbc-52c8-492c-9c9c-a90b285321a9'></a>

To summarise, our asymptotic analysis reveals how measurements of lysis rates, extracted from experiments for which the ratio of initial antibody numbers to target receptors is small, could be integrated with similar data from experiments for which these ratios are intermediate and large in order to estimate the tumour cell kill rate function $\hat{f}(R)$ for a particular combination of NK cells, tumour cells and antibody. Further, numerical simulations of the full model reveal how the dynamics of the dependent variables change over time. Additional, experimental data, collected at multiple time-points, is now needed first to validate our model and then to estimate specific values of its parameters.

<a id='32ae8bac-af0d-44a1-ac9b-b2d7e0e47f55'></a>

There is considerable scope for extending the work presented in this paper. First, we recall that in our model we assume, for simplicity, that NK cells associate and dissociate from cancer cells at constant rates, βon and βoff, although Deguine et al. (2012) report that antibody recognition by NK cells increases contact stability with cancer cells. It would be interesting to establish whether the qualitative behaviour of our model changes if we relax the assumption that the association and dissociation rates are constant and suppose instead that they depend on T♭/(T+C), the number of antibody-target receptor complexes per cancer cell. Additionally, we could consider different functional forms of the kill rate function, _f_, and a broader range of parameter regimes (see Table 3).
The model could also be validated against lysis data from cytotoxicity assays performed to assess the efficacy of candidate antibodies for ADCC. More generally, the model could be applied to

<a id='2836c547-1d07-40fc-bd56-b4403ea2313b'></a>

data for other forms of antibody dependent cell based killing such as antibody dependent cellular phagocytotosis (ADCP) involving macrophages (Matlawska-Wasowska et al., 2013). The long-term aim of our model is to improve the ability of pharmacologists to use cytotoxicity assays to optimise antibody therapies, discriminate between experimental antibodies and design more informative experiments.

<a id='fbf43d21-8524-4394-a93c-53207072f1d1'></a>

As mentioned in Sections 2 and 3, the current model is valid for the relatively short timescales associated with the cytotoxicity as-say, during which processes such as cell proliferation and apoptosis can be neglected. By relaxing these assumptions, the model could be extended to describe longer time-scales on which cancer cells and NK cells proliferate as they do in vivo. The model could also be extended to capture in vivo features of tumour growth such as an-tibody clearance and NK cell trafficking to the cancer site, as well as the effect of other mechanisms of immune attack, angiogene-sis and vascular remodelling, and other cancer treatments such as chemotherapy.

<a id='e4094ecb-7279-42c0-9a23-c1e2358fd512'></a>

Another possible direction for further research relates to side-effects caused by the antibodies. In more detail, increasing the amount of antibodies used in the clinic has substantial draw-backs. Firstly, antibodies are typically given intravenously and are formulated at a prescribed, standard concentration, so increasing the dose means increasing the volume of antibody solution that needs to be infused. This substantially extends the time required to administer the drugs (infusion of larger volumes of drugs can take several hours) and can be extremely unpleasant to patients. Administering higher doses than strictly necessary also increases the risks of eliciting so called _infusion reactions_ which can involve the patients immune system reacting to the foreign protein and can in extreme cases lead to anaphylaxis. For a discussion of infusion reactions, see Vogel (2010). Additionally, monoclonal antibody drugs are generally very expensive so increasing the amount administered unnecessarily increases the price of the therapy substantially.

<a id='14c03390-3684-4aa9-bc3d-d99b12ec5b7e'></a>

Drug discovery is a time-consuming process which involves op-
timising many parameters of a pharmaceutical agent. The approach
presented in this paper and the suggestions for further work illus-
trate some of the ways in which mathematical modelling can be
used to increase the information we gain from particular experi-
ments.

<a id='0462bce6-ac62-4bf5-8b6e-142e19309cbf'></a>

## Acknowledgements
FH gratefully acknowledges funding from the ESPRC, MRC, Astrazeneca and Medimmune. We thank Professor Kevin Burrage (Queensland University of Technology), Dr Mark Penney (Medimmune, Cambridge), Professor Mark Coles (University of Leeds) and Dr Alex Phipps (Roche, UK) for helpful discussions.

<a id='26de8d14-f7b2-4512-bad6-e654ef8a4a4f'></a>

Appendix A. Experimental protocol

In this appendix, we explain how the experimental data pre-sented in Fig. 1 were collected. ADCC experiments with the anti-body Trastuzumab/Herceptin (Roche, Basel, Switzerland) were per-formed as described in Stewart et al. (2011). In this system, Natu-ral Killer (NK) cells were used as effector cells (E) and SkBr3 cells (a breast cancer cell line) acts as target cells (T). SkBr3 cells ex-press high levels of the receptor protein HER2/neu on the cell sur-face to which Trastuzumab binds with high affinity. Briefly, periph-eral blood mononuclear cells (PBMCs), a complex mixture of cells which contain NK cells, were recovered from human blood by lay-ering over Ficoll-paque (GE Healthcare, Bucks, UK) and centrifug-ing at 400 x g for 40 min. PBMCs were washed twice in phos-phate buffered saline (PBS) and NK cells were purified by nega-tive selection using Robosep and the human NK cell enrichment kit

<!-- PAGE BREAK -->

<a id='7923818b-8ec5-432a-aea8-beb6167710f6'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='11464b1c-5823-4b41-918e-be9307bf00cb'></a>

49

<a id='5726549f-68cc-4a9d-85bc-6dc12632c65d'></a>

(Stem Cell Technologies Inc., Vancouver, Canada) as per the manu-
facturer's instructions and counted with a haemocytometer.

<a id='4434f26b-bf63-4f2f-9acd-baf5e96680f8'></a>

SkBr3 cells were obtained from the American Type Culture Col-lection (ATCC). Cells were counted with a haemocytometer and 5 x 103 cells/well incubated at 37 °C for 4 h, together with antibody and NK effector cells at the effector to target (E:T) ratios indicated, in RPMI 1640 Glutamax I growth medium (Invitrogen, Paisley, UK) supplemented with 10% foetal bovine serum having low levels of endogenous IgG and 1% penicillin/streptomycin in a total volume of 2001. Serving as maximum lysis control, some wells contained target cells alone and were lysed completely by the addition of 10 µl of lysis agent (Cell Technology Inc., Mountain View, CA, USA) 15 min before the end of incubation and the resulting values were set as 100% lysis. Supernatant (100 µl) was transferred to a 96-well Optiplate (PerkinElmer, Montreal, QC, Canada) and assayed for the presence of glyceraldehyde 3-phosphate dehydrogenase (GAPDH) levels using the aCella-Tox kit (Cell Technology Inc.) as per the manufacturer's instructions. GAPDH is an enzyme involved in gly-colysis and present in all cells. It is released into the supernatants only upon lysis of cells, thus acting as a surrogate for cell killing and loss of structural integrity. All wells were corrected for back-ground contributions from the medium by measuring wells that contained media only. Spontaneous release of GAPDH from target as well as NK cells was determined by measuring supernatants from wells containing only target cells and NK cells, respectively.

<a id='fe8dddcf-141b-49cd-b6a9-3fe15c97cb36'></a>

Percentage killing was calculated using the following formula in which each term refers to the amount of GAPDH released from a specific experiment:

<a id='92e4fafd-1f1b-4de7-88bf-99a7763e934a'></a>

Percentage Killing = Sample - Target_cont - NK_cont - Media only / 100% Lysis - Media only

<a id='ef803dbc-5377-4d97-8e88-27993c0687c7'></a>

where Target_cont = (Target cells only) – (Media only),

<a id='85383377-1dad-4991-b5cc-05fbfcf28dd7'></a>

and NK_cont = (NK cells only) - (Media only).

<a id='24c9d8d3-b712-42a6-97c1-f0e94e5ebc80'></a>

Based on this formula, we remark that if the values for release from (target cells only) and (NK cells only) are close to those for media only then this equation can produce values that are just below zero, especially if there is some variation in the experimental values, as is almost inevitable in a biological system. This is generally not considered to be a problem as long as it is within the limits of about 5% tolerance. Many researchers would simply set these values at zero but, for reasons of scientific accuracy, we chose instead accurately to reflect the variability inherent in this assay. Finally, we note that, in Fig. 1, data points are mean values of triplicate measures within the representative experiment.

<a id='7025e5c9-9d5c-49db-a8b2-eb601ba6b566'></a>

### Appendix B. Parameter estimation

In this appendix we detail how the parameters used in the model were derived.

<a id='6139a073-2e6b-4ba3-9e96-8ac1670032e3'></a>

The number of target receptors per cancer cell, ρ_T. In Ward et al. (2011), Ward et al. measured the expression levels of two receptors, CD19 and CD20, which are targets of the therapeutic antibodies MEDI551 and rituximab respectively, when treating Chronic Lymphocytic Leukaemia. In a panel of patient cell lines expression levels of the two targets were in the range O(10³) – O(10⁴) molecules cell⁻¹. In Kute et al. (2012), Kute et al. measured expression levels of HER2/neu, the target for trastuzumab when treating breast cancer. Across a panel of experimental cell lines, expression levels of HER2/neu were in the range O(10⁴) – O(10⁷) molecules cell⁻¹. Following Ward et al. (2011) and Kute et al. (2012), we estimate the number of target receptors per cancer cell to be in the range 10³ – 10⁷ molecules cell⁻¹.

<a id='1ca7355f-595a-4fdf-b24e-934af2c171e9'></a>

The *antibody binding rates*, **k_on** and **k_off**. In Bostrom et al. (2011) Bostrom et al. estimated the association and dissociation rates of trastuzumab, and its variants, to HER2/neu and VEGF, target receptors relevant for treating breast cancer. They found that **k_on** takes values in the range O(10^4) – O(10^6) M^-1s^-1, while **k_off** was O(10^-4) s^-1. In Ernst et al. (2005), Ernst et al. estimated the association and dissociation rates of rituximab and its variants, for CD20, target receptors relevant for treating B cell cancers. The parameters **k_on** and **k_off** varied in the ranges O(10^3) – O(10^4) M^-1s^-1 and O(10^-4) – O(10^-3) s^-1 respectively. Based on these studies, we estimate **k_on** lies in the range O(10^3) – O(10^7) M^-1s^-1 and fix **k_off** = 10^-4 s^-1. We assume a fixed value for **k_off** for simplicity and to reduce the number of parameters that need to be considered when performing perturbation analysis (see Section 4).

<a id='cff0100b-60c2-478a-9d90-1133a3a45b16'></a>

NK: tumour cell association and dissociation rates, β_on and β_off. In Almeida et al. (2011), Almeida et al. estimated β_on and β_off from in vitro conjugation assays in which approximately 200 NK cells and 200 cancer cells were co-cultured in a micro-well and the number of NK-cancer cell conjugates counted at times t = 5, 10, 15, 20 and 30 min using flow cytometry. An ODE model was fit to these data to estimate the rates of conjugation and dissociation under the assumption that cell killing is negligible on this timescale. Based on this study, we fix β_on = 2 x 10^13 M^-1 s^-1 and β_off = 10^-3 s^-1.

<a id='b2123017-0597-4e88-958c-d4883f7af8d0'></a>

The kill-rate function, $f\left(\frac{T_b}{T+C}\right)$. We estimate typical values of $f\left(\frac{T_b}{T+C}\right)$ from experimental data generated by Vanherberghen et al. (2013). Using microchip-based, time-lapse imaging, they found that, once an NK:cancer cell complex forms, the time to tumour cell death was approximately 10 min. Thus, we estimate that $f\left(\frac{T_b}{T+C}\right)$ takes values in the range $0 - 1.6 \times 10^{-3}\text{ s}^{-1}$.

<a id='1fc54448-ecff-4652-9175-24f0106d0256'></a>

References
Almeida, C., Ashkenazi, A., Shahaf, G., Kaplan, D., Davis, D.M., Mehr, R., 2011.
Human NK cells differ more in their KIR2DL1-dependent thresholds for
HLA-cw6-mediated inhibition than in their maximal killing capacity. PLoS One
6 (9). E24927.
Bachireddy, P., 2012. Immunology in the clinic review series; focus on cancer: mul-
tiple roles for the immune system in oncogene addiction. Clin. Exp. Immunol.
167 (2), 188-194.
Bhat, R., Watzl, C., 2007. Serial killing of tumor cells by human natural killer cell-
s-enhancement by therapeutic antibodies. PLoS One 2. E326.
Bostrom, J., Haber, L., Koenig, P., Kelley, R.F., Fuh, G., 2011. High affinity antigen
recognition of the dual specific variants of herceptin is entropy-driven in spite
of structural plasticity. PLoS One 6. E17887.
Callewaert, D.M., Johnson, D.F., Kearney, J., 1978. Spontaneous cytotoxicity of cul-
tured human cell lines mediated by normal peripheral blood lymphocytes. III.
Kinetic parameters. J. Immunol. 121, 710-717.
Chu, G., 1978. The kinetics of target cell lysis by cytotoxic t lymphocytes: a descrip-
tion by poisson statistics.. J. Immunol. 120, 1261-1267.
Deguine, J., Breart, B., Lematre, F., Bousso, P., 2012. Cutting edge: tumor targeting
antibodies enhance NKG2d mediated NK cell cytotoxicity by stabilizing NK cell
tumor cell interactions. J. Immunol. 189, 5493-5497.
Deguine, J., Breart, B., Lematre, F., Santo, J.P.D., Bousso, P., 2010. Intravital imaging
reveals distinct dynamics for natural killer and CD8+ t cells during tumor re-
gression. Immunity 33, 632-644.
Douglass, E.F., Miller, C.J., Sparer, G., Shapiro, H., Spiegel, D.A., 2013. A comprehen-
sive mathematical model for three-body binding equilibria. J. Am. Chem. Soc.
135 (16), 6092-6099.
Ernst, J.A., Li, H., Kim, H.S., Nakamura, G.R., Yansura, D.G., Vandlen, R.L., 2005.
Isolation and characterization of the b-cell marker CD20.. Biochemistry 44,
15150-15158.
Fogh, J., Fogh, J.M., Orfeo, T., 1977. One hundred and twenty-seven cultured human
tumor cell lines producing tumors in nude mice.. J. Nat. Cancer Inst. 59 (1),
221-226.
Garcia-Penarrubia, P., Lorenzo, N., Galvez, J., Campos, A., Ferez, X., Rubio, G., 2002.
Study of the physical meaning of the binding parameters involvedin effectortar-
get conjugation using monoclonal antibodies against adhesion molecules and
cholera toxin.. Cell. Immunol. 215 (2), 141-150.
Gardner, C., 2009. Stochastic methods: a handbook for the natural and social sci-
ences.. Springer.
Hanahan, D., Weinberg, R.A., 2011. Hallmarks of cancer: the next generation. Cell
144 (5), 646-674.

<!-- PAGE BREAK -->

<a id='d1914060-f1f8-47a1-b05d-1fee920b28a3'></a>

50

<a id='c1765fb5-69cf-4a67-989c-60db445d9aa1'></a>

F. Hoffman et al./Journal of Theoretical Biology 436 (2018) 39–50

<a id='8203a5ff-0b3e-4998-92c8-99bd5cd6dd92'></a>

Hodi, F.S., O'Day, S.J., McDermott, D.F., Weber, R.W., Sosman, J.A., Haanen, J.B., Gonzalez, R., Robert, C., Schadendorf, D., Hassel, J.C., Akerley, W., van den Eertwegh, A.J., Lutzky, J., Lorigan, P., Vaubel, J.M., Linette, G.P., Hogg, D., Ottens-meier, C.H., Lebb, C., Peschel, C., Quirt, I., Clark, J.I., Wolchok, J.D., Weber, J.S., Tian, J., Yellin, M.J., Nichol, G.M., Hoos, A., Urba, W.J., 2010. Improved survival with ipilimumab in patients with metastatic melanoma. N. Eng. J. Med. 363 (711).
Hudis, C.A., 2007. Trastuzumab–mechanism of action and use in clinical practice. N. Eng. J. Med. 357 (1), 39–51.
Iida, S., Kuni-Kamochi, R., Mori, K., Misaka, H., Inoue, M., Okazaki, A., Shitara, K., Satoh, M., 2009. Two mechanisms of the enhanced antibody-dependent cellular cytotoxicity (ADCC) efficacy of non-fucosylated therapeutic antibodies in human blood.. BMC Cancer 9 (58).
Kute, T., Stehle Jr, J.R., Ornelles, D., Walker, N., Delbono, O., Vaughn, J.P., 2012. Understanding key assay parameters that affect measurements of trastuzumab-mediated ADCC against her2 positive breast cancer cells. Oncolmmunology 1 (6), 810–821.
Lutz, C.T., Karapetyan, A., Al-Attar, A., Shelton, B.J., Holt, K.J., Tucker, J.H., Presnell, S.R., 2011. Human NK cells proliferate and die in vivo more rapidly than t cells in healthy young and elderly adults. J. Immunol. 186 (8), 4590–4598.
Mathworks, (2013). Matlab 2013a. http://www.mathworks.co.uk.
Matlawska-Wasowska, K., Ward, E., Stevens, S., Wang, Y., Herbst, R., Winter, S.S., Wilson, B.S., 2013. Macrophage and NK-mediated killing of precursor-b acute lymphoblastic leukemia cells targeted with a-fucosylated anti-CD19 humanized antibodies. Leukemia 27 (6), 1263–1274.
Miller, R.G., Dunkley, M., 1974. Quantitative analysis of the 51cr release cytotoxicity assay for cytotoxic lymphocytes. Cell Immunol. 14, 284–302.
Nakagawa, S., Fujii, T., Yokoyama, G., Kazanietz, M.G., Yamana, H., Shirouzu, K., 2003. Cell growth inhibition by all-trans retinoic acid in SKBR-3 breast cancer cells: Involvement of protein kinase ca and extracellular signal-regulated kinase mitogen-activated protein kinase. Mol. Carcinogenesis 38 (3), 106–116.
Ogbomo, H., Hahn, A., Geiler, J., Michaelis, M., Doerr, H.W., Cinatl Jr, J., 2006. NK sensitivity of neuroblastoma cells determined by a highly sensitive coupled luminescent method. Biochem. Biophys. Res. Comm. 339 (1), 375–379.

<a id='2e9a7b2e-8e3d-4f7c-b5d9-36c9365fa2db'></a>

Scott, A.M., Wolchok, J.D., Old, L.J., 2012. Antibody therapy of cancer. Nat. Rev. Cancer 12, 278-287.

Seidel, U.J.E., Schlegel, P., Lang, P., 2013. Natural killer cell mediated antibody-dependent cellular cytotoxicity in tumor immunotherapy with therapeutic antibodies. Front Immunol. 4. 76.

Shampine, L.F., Reichelt, M.W., 1997. The MATLAB ODE suite. SIAM J. Sci. Comput. 18, 1-22.

Stewart, R., Thom, G., Levens, M., Guler-Gane, G., Holgate, R., Rudd, P.M., Webster, C., Jermutus, L., Lund, J., 2011. A variant human igg1-fc mediates improved ADCC. Protein Eng. Des. Sel. 24 (9), 671-678.

Thorn, R.M., Henney, C.S., 1976. Kinetic analysis of target cell destruction by effector t cells. i. Delineation of parameters related to the frequency and lytic efficiency of killer cells. J. Immunol. 117, 2213-2219.

Thorn, R.M., Henney, C.S., 1977. Kinetic analysis of target cell destruction by effector t cells. II. Changes in killer cell avidity as a function of time and antigen dose. J Immunol 119, 1973-1978.

Vacchelli, E., Pol, J., Bloy, N., Eggermont, A., Cremer, I., Fridman, W.H., Galon, J., Marabelle, A., Kohrt, H., Zitvogel, L., Kroemer, G., Galluzzi, L., 2015. Trial watch: tumour-targetting monoclonal antibodies for oncological indications.. Oncoimmunology 4. E985940.

Vanherberghen, B., Olofsson, P.E., Forslund, E., Sternberg-Simon, M., Khorshidi, M.A., Pacouret, S., Guldevall, K., Enqvist, M., Malmberg, K.J., Mehr, R., nfelt, B., 2013. Classification of human natural killer cells based on migration behavior and cytotoxic response. Blood 121 (8), 1326-1334.

Vogel, W.H., 2010. Infusion reactions: diagnosis, assessment, and management. Clin. J. Oncol. Nurs. 14, E10-21.

Ward, E., Mittereder, N., Kuta, E., Sims, G.P., Bowen, M.A., Dall'Acqua, W., Tedder, T., Kiener, P., Coyle, A.J., Wu, H., Jallal, B., Herbst, R., 2011. A glycoengineered anti-CD19 antibody with potent antibody-dependent cellular cytotoxicity activity in vitro and lymphoma growth inhibition in vivo. Br J Haem 155 (4), 426-437.

Zeijlemaker, W.P., Oers, R.H.J.V., De Goede, R.E., Schellekens, P.T., 1977. Cytotoxic activity of human lymphocytes: quantitative analysis of t cell and k cell cytotoxicity, revealing enzyme-like kinetics. J. Immunol. 119, 1507-1514.
<a id='748a06b2-eb33-4b4f-ad74-afa4b822c986'></a>

<::logo: Elsevier
ELSEVIER
The logo features a detailed illustration of a tree with two figures beneath it, rendered in black and white.:%>

<a id='bbb45f59-d7a1-4e64-b729-408d6b727e59'></a>

<::logo: ScienceDirect
Available online at www.sciencedirect.com
Grey dots forming a curved, cloud-like shape::>

<a id='d60d4c8d-d668-4889-bf7c-ca50693b9433'></a>

Journal of Theoretical Biology 246 (2007) 70–86

<a id='fe4e02c6-6e66-477f-a5e6-983d08afa43d'></a>

===

Journal of
Theoretical
Biology

===

www.elsevier.com/locate/yjtbi

<a id='8c298dd2-8df3-404b-9ce5-c5bad1b5320c'></a>

A dynamical model of human immune response
to influenza A virus infection

<a id='30650f7d-4fa7-4388-bd2b-8dcde65ecea2'></a>

Baris Hancioglu, David Swigona,b,c, Gilles Clermontb,c,d,*
aDepartment of Mathematics, 301 Thackeray, University of Pittsburgh, Pittsburgh, PA 15260, USA
bCIRM (Center for Inflammation and Regenerative Modeling), 100 Technology Drive Suite 200, Pittsburgh, PA 15219-3110, USA
cCRISMA Laboratory, University of Pittsburgh, Pittsburgh, PA 15261, USA
dDepartment of Critical Care Medicine, 3550 Terrace St, University of Pittsburgh Medical Center, Pittsburgh, PA 15261, USA

Received 11 May 2006; received in revised form 8 November 2006; accepted 11 December 2006
Available online 19 December 2006

<a id='dc1e7696-fec0-4e46-9c4c-cf1e146ceb4c'></a>

Abstract

We present a simplified dynamical model of immune response to uncomplicated influenza A virus (IAV) infection, which focuses on the control of the infection by the innate and adaptive immunity. Innate immunity is represented by interferon-induced resistance to infection of respiratory epithelial cells and by removal of infected cells by effector cells (cytotoxic T-cells and natural killer cells). Adaptive immunity is represented by virus-specific antibodies. Similar in spirit to the recent model of Bocharov and Romanyukha [1994. Mathematical model of antiviral immune response. III. Influenza A virus infection. J. Theor. Biol. 167, 323-360], the model is constructed as a system of 10 ordinary differential equations with 27 parameters characterizing the rates of various processes contributing to the course of disease. The parameters are derived from published experimental data or estimated so as to reproduce available data about the time course of IAV infection in a naïve host. We explore the effect of initial viral load on the severity and duration of the disease, construct a phase diagram that sheds insight into the dynamics of the disease, and perform sensitivity analysis on the model parameters to explore which ones influence the most the onset, duration and severity of infection. To account for the variability and speed of adaptation of the adaptive response to a particular virus strain, we introduce a variable that quantifies the antigenic compatibility between the virus and the antibodies currently produced by the organism. We find that for small initial viral load the disease progresses through an asymptomatic course, for intermediate value it takes a typical course with constant duration and severity of infection but variable onset, and for large initial viral load the disease becomes severe. This behavior is robust to a wide range of parameter values. The absence of antibody response leads to recurrence of disease and appearance of a chronic state with nontrivial constant viral load.
© 2007 Elsevier Ltd. All rights reserved.

<a id='d48b5b33-0703-4955-bb22-882f6278bb56'></a>

Keywords: Immunology; Mathematical modeling; Human immune response; Influenza; Antigenic distance

<a id='5ed094d2-3f49-4de6-a015-ce6e84254718'></a>

## 1. Introduction

Influenza is a highly cytopathic, contagious, acute respiratory disease caused by an influenza virus infection (Mohler et al., 2005; Nicholson et al., 1998; Tamura and Kurata, 2004). Transmission is caused by direct contact such as hand shake or by airborne virus (Mohler et al., 2005). The virus is an enveloped virus with seven internal

<a id='9d88bd03-4e52-41e5-8893-417903ccf4e5'></a>

--- 
*Corresponding author. Department of Critical Care Medicine,
University of Pittsburgh, Scaife 606B, 3550 Terrace, Pittsburgh, PA
15260, USA. Tel.: +1 412 647 7980; fax: +1 412 647 3791.
*E-mail address:* cler@pitt.edu (G. Clermont).

<a id='220d3233-a913-4f86-beac-b8d4b58444c9'></a>

0022-5193/$ - see front matter © 2007 Elsevier Ltd. All rights reserved.
doi:10.1016/j.jtbi.2006.12.015

<a id='76498470-1b7d-476b-8b1c-e84eea3b68e9'></a>

proteins (nucleoprotein (NP), three polymerase proteins (PA, PB1, and PB2), two matrix proteins (M1 and M2), and nonstructural proteins (NS2)) and two external glycoproteins, hemagglutinin (HA) and neuraminidase (NA) (Tamura et al., 2005). It is divided into types A, B, and C, according to the antigenic differences between NP and matrix protein (M) (Tamura et al., 2005). Influenza A viruses are subdivided into subtypes such as H1N1, H16N9, etc. based on the antigenic signatures of the major surface proteins HA (16 subtypes differ by 30%) and NA (Webster et al., 2006). The viruses in each subtype regularly undergo gradual changes in genetic makeup through point mutations in the HA and NA molecules (antigenic drift)

<!-- PAGE BREAK -->

<a id='6a95feb1-d688-4072-b062-bb38437ab80b'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='b639f854-8c2a-4bdc-b744-00d95f9f8b46'></a>

71

<a id='749ee9be-97ff-4dc1-8de9-7bb9d7cc2d79'></a>

which cause local outbreaks of influenza and small size epidemics. Occasionally, a major change in the HA and NA proteins can arise from the exchange of genetic material (reassortment) between the avian influenza gene pool and human influenza genes during co-infection (Tamura and Kurata, 2004) or adaptive mutation. Such a change is termed as "antigenic shift" and since the population has typically limited or no immunity against the modified virus, a global pandemic may result.

<a id='dab7b91a-a49b-4d9d-a4ad-d680986bf928'></a>

In the 20th century, three global pandemics occurred. The "Spanish flu" of 1918–19, which was of the subtype H1N1, infected approximately one third of the entire human population (Taubenberger and Morens, 2006). More than a half million people died in the US and about 50 million people died worldwide (Taubenberger and Morens, 2006). In 1957–58, "Asian flu" of the subtype H2N2 caused about 70,000 deaths in the US. In 1968–69, "Hong Kong flu" of the subtype H3N2 caused about 34,000 deaths in the US. Many scientists believe that it is only a matter of time until the next pandemics occurs. In the absence of proper preparation, a pandemic could cause 89,000–207,000 deaths, 314,000–734,000 hospitalizations, 18–42 million outpatient visits, and another 20–47 million people being sick in the US (Meltzer et al., 1999). The economic impact could range between $71.3 and $166.5 billion and between 15% and 35% of the US population could be affected from the infection (Meltzer et al., 1999). Currently, there is a big concern about the pandemic potential of the avian flu of subtype H5N1 which has already caused considerable damage, mainly to birds: more than 140 million domestic birds have been killed by the virus or culled to stem its spread till now and more than 130 people have been infected in various countries in Asia (Webster et al., 2006). Almost half of the infected people died. These numbers show the potential danger of IAV infection for human population and the importance of understanding virus–immune system interactions which helps for taking necessary control measures (vaccination or antiviral drugs).

<a id='4cce48f9-f9d3-4d9a-9b66-961926ba98ea'></a>

Mathematical modeling has proven to be a valuable tool
in the understanding of immune response to infectious
diseases (Perelson, 2002) which helps in clarifying and
testing hypotheses, finding the smallest number of factors
sufficient to explain the biological phenomena and analyz-
ing the experimental results (Asquith and Bangham, 2003).
Modeling has a substantial impact on research at the
molecular level (Nowak and May, 2000). Recently,
important results have been obtained in the mathematical
modeling of virus dynamics for the HIV (Nowak and
Bangham, 1996; Perelson et al., 1993, 1996), hepatitis B
(Marchuk et al., 1991), hepatitis C (Neumann et al.,
1998) and influenza (Bocharov and Romanyukha, 1994)
infections.

<a id='ba7ab567-72eb-43a6-bd99-adb4cb8949bf'></a>

In this paper we construct a simplified, biologically justified, mathematical model of the dynamics of IAV infection and the human immune response to such infection. We do not strive to obtain a detailed model

<a id='00b67de8-f497-42e1-8327-d9a878211d1f'></a>

accounting for all known components of the immune system and their interactions. Rather, we focus on three important components of the immune response: the interferon and cellular components of innate immunity and the adaptive immunity, all of which have the same goal of limiting the concentration of the virus and the damage to the system, but which achieve this goal using different strategies: interferon immunity by removing the "substrate" that virus needs for reproduction (i.e., the healthy cells), cellular immunity by removing the source of new viruses (i.e., the infected cells), and adaptive immunity by lowering the effective concentration of the virus.

<a id='a569d7a2-1e63-483a-bc2d-5c9621c3ee1c'></a>

Our main goal is to uncover the relative roles played by each immune strategy during the course of the disease to have a better understanding of what drives the intensity of symptoms, infectivity of the virus and the host, and duration of the disease. In subsequent research, the model will serve as a tool for predicting the effect of therapeutic interventions on the course of the disease, as well as a model for understanding of basic processes of immune response to multiple infections. Our second goal is to develop a model of the immune response of individuals that can be used as a practical basis for multi-scale population susceptible-infected-recovered (SIR) models that are used to describe geographic disease spread and evaluate the impact of containment strategies. As such, this biological model should account for individual character-istics of the human host and the virulence of a specific virus subtype or strain and should yield predictions about the onset, severity and infectivity of the IAV infection in an individual as a function of the initial viral load and existing immunity (Clermont et al., 2004). Yet, the model should be sufficiently simple to allow fast computation of individual immune responses as part of multi-scale simulations.

<a id='9165965a-175a-4f03-bab1-d5de9f638dc6'></a>

## 2. Methods

### 2.1. Biology of influenza

Influenza A virus (IAV) attacks the host respiratory tract mucosa, interacts with healthy epithelial cells and infects them by binding to cell surface receptors via one of the major surface glycoproteins, HA (Tamura and Kurata, 2004). The virus replicates in infected cells and several hours after cellular infection, newly synthesized virus particles are released by the action of another major glycoprotein, NA (Tamura et al., 2005). The response of the host to IAV infection involves a cascade of events mediated by several effector cells and molecules (Ada and Jones, 1986; Tamura and Kurata, 2004) that neutralize free virus, kill infected cells and limit the spread of viral particles by increasing healthy cell resistance to infection.

<a id='959b85b2-05a0-47f2-ab0b-59ec2a6a5fb9'></a>

Antigen presenting cells (APC) are essential in the induction and amplification of the human immune response (Akira et al., 2001). Exogenous viral antigens, which comprise inactive viral particles, intact viruses and apoptotic, infected cells, are taken up by APC through

<!-- PAGE BREAK -->

<a id='780aa28c-7fef-43b8-8f04-90881c95ac65'></a>

72

<a id='9defb9d5-f564-480a-bdf1-c7cf81b58c7d'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70-86

<a id='604a5a8f-7e06-4a5b-957e-0fd7a9457c91'></a>

endocytosis and provide a potential source of peptides that
could bind to MHC class I or II molecules in the APC
(Nguyen et al., 1998; Tamura and Kurata, 2004; Tulp
et al., 1994). The role of the APC is to stimulate both
innate and adaptive immunity.

<a id='351714c5-37b3-46d4-ac78-00192803387e'></a>

As the first line of defense, APC and infected cells stimulate the innate immunity by secreting interferon α and β (IFN) molecules (Julkunen et al., 2000; Lamb, 1996; Ronni et al., 1995; Sareneva et al., 1998; Stark et al., 1998) which interact with healthy cells and convert them to an infection resistant state, thereby preventing the virus from spreading efficiently and allowing the adaptive immune response enough time to develop and eliminate the virus (Price et al., 2000). Another role of IFN is to stimulate symptoms such as fever which occurs in the early stages of infection. IFN levels rise rapidly after infection and correlate directly with the degree of viral replication in ferrets, mice and humans (Tamura and Kurata, 2004; Wyde et al., 1982). Magnitude of the fever correlates strongly with the level of virus shedding in humans and animals (Tamura and Kurata, 2004).

<a id='349e3723-eaf1-4a18-9ae5-a613920800a6'></a>

As a second line of defense, APC stimulate the cellular component of innate immunity which consists of effector cells (cytotoxic T cells (CTL) or natural killer cells (NK)) that destroy infected cells before they can release a mature virus. Activated T cells produce various factors which are extremely important for the kinetics of the IAV infection: helper T cells secrete IL-2 and other lymphocytes and CTL produce IFN-γ, which increases the expression of MHC antigens acting to enhance virus-infected cell destruction. The peptide-class I MHC complexes presented on the infected cells are recognized by class-I MHC-restricted CD8+ memory T cells (Th1 cells), which destroy the infected cells (Tamura et al., 2005). The specificity of memory T cells is directed against viral internal proteins; NP is the strongest of these antigens (Yewdell et al., 1985). Since structure of these antigens is conserved within the type of virus, Th1 cells against these antigens are cross-reactive within the type of influenza (Tamura et al., 2005).

<a id='7a8f67bd-1f9a-4968-804e-a4f00dc8c328'></a>

Finally, APC stimulate adaptive immunity by activating the proliferation of virus-specific plasma cells which produce antibodies (Abs) that bind with IAV and render it ineffective. HA and NA are taken up in an endocytic vesicle pathway of the APC and are degraded; the peptides of these antigens are loaded on class-II MHC molecules and then expressed on the APC (Tulp et al., 1994). The peptide class II MHC complexes are recognized by class-II MHC-restricted CD4+ T cells (Th2 cells). Th2 cell stimulation by antigen recognition results in the produc- tion of specific Abs to HA and NA molecules. Anti-HA Abs neutralize the infectivity of the virus, whereas anti-NA Abs prevent the release of viruses from infected cells (Johansson et al., 1989). Thus, anti-HA Abs are primarily responsible for preventing infection, while anti-NA Abs and CTL specific for viral core proteins are responsible for reducing viral spread and thereby for accelerating the recovery from influenza (Tamura et al., 2005).

<a id='c24d9507-92a6-436b-9060-ef317adeb7ca'></a>

The respiratory tract mucosa is not only the site of infection by influenza viruses but also the site of defense against viral infection in the host (Tamura and Kurata, 2004). The recovery process after primary infection involves two phases: an early phase (days 5-7), character- ized by a rapid decrease in virus titer via killing of the virus- infected epithelial cells by MHC class I restricted CD8+ CTLs, which appear with a peak at day 7 is cellular response dependent, while a late phase (day 7 onwards), characterized by a more protracted decrease that ultimately results in clearance, depends on the adaptive response (Tamura and Kurata, 2004). Since flu symptoms emerge within a few days of inoculation, acquired immunity appearing after the first week of infection cannot prevent the onset of respiratory symptoms. Therefore, effective immunity must be induced in advance by natural infection or vaccination in order to prevent disease.

<a id='7b9c1e27-f2a9-4865-9f9c-febe4fd9d51e'></a>

## 2.2. Model development

The model of human immune response against IAV infection we consider is a simplified model of population-dynamics type which consists of the following interactions (see Fig. 1). The epithelial cells of the respiratory tract are assumed to be in one of four possible states: healthy (_H_), infected (_I_), dead (_D_), or resistant (_R_) to infection. The total number of epithelial cells (i.e., _H_ + _I_ + _D_ + _R_) is assumed constant. The virus particles (_V_) interact with healthy cells and infect them. Infected cells release new virus particles upon their death. Proliferation of healthy cells causes regeneration and decrease in the proportion of dead cells. Dead cells stimulate the activation of APC (_M_).

<a id='eee30b0a-7dc7-4207-9a5c-440b1a729e40'></a>

<::schematic diagram: The diagram shows a network of interacting components. The influenza virus (IAV) is represented by a red hexagon labeled "IAV V". Four different cell types are shown in cyan ovals: "Resistant cells R", "Healthy cells H", "Infected cells I", and "Dead cells D".

Components of adaptive immunity are shown in orange. These include "Plasma cells P" (oval) and "Antibody A" (rectangle). Also part of adaptive immunity are "Effector cells E" (purple oval). Components of innate immunity are shown in purple, but here Effector cells are colored purple. The interferon component is shown in green: "Interferon F" (rectangle).

Other components include "Antigen presenting cells M" (blue rounded rectangle) and "Antigenic compatibility S" (white rectangle).

Interactions:
- Upregulation (lines terminated with arrows):
  - Interferon F upregulates Resistant cells R.
  - Healthy cells H can become Infected cells I.
  - Infected cells I can become Dead cells D.
  - IAV V infects Healthy cells H, turning them into Infected cells I.
  - Infected cells I stimulate Antigen presenting cells M.
  - Antigen presenting cells M stimulate Plasma cells P and Effector cells E.
  - Antigen presenting cells M also stimulate Th2 and Th1 (dashed ovals).
  - Th2 and Bcells (dashed ovals) stimulate Plasma cells P.
  - Plasma cells P produce Antibody A.
  - Antigenic compatibility S upregulates Plasma cells P.

- Inhibition (lines terminated with bars):
  - IAV V is inhibited by Antibody A.
  - IAV V is inhibited by Antigenic compatibility S.

- Inter-conversion of cell types (cyan) is indicated by dashed arrows:
  - Healthy cells H can become Resistant cells R and vice versa (double-headed dashed arrow).
  - Infected cells I can become Healthy cells H (dashed arrow).
  - Dead cells D can become Healthy cells H (dashed arrow).

- Homeostatic maintenance of effector and plasma cell populations are indicated by self-regulating loops:
  - Plasma cells P have a self-regulating loop.
  - Effector cells E have a self-regulating loop.

- Dashed ovals represent details of the mechanism ignored in this model: Th2, Th1, Bcells.

Fig. 1. Schematic representation of interactions included in the model. The influenza virus (IAV) is shown as red hexagon, the four different cell types are shown in cyan. Components of adaptive immunity are shown in orange, cellular component of innate immunity in purple, and interferon component in green. Upregulation is represented by lines terminated with arrows and inhibition by lines terminated with bars. The inter-conversion of cell types (cyan) is indicated by dashed arrows. Dashed ovals represent details of the mechanism ignored in this model. Homeostatic maintenance of effector and plasma cell populations are indicated by self-regulating loops.::>

<!-- PAGE BREAK -->

<a id='8ad6c66c-6c4b-472f-867f-f5a843bf9083'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70-86

<a id='1ba65206-b539-400f-8d25-5add6147bb84'></a>

73

<a id='4ffb3b6d-6327-4cf0-a83c-cee0592a3cf5'></a>

Table 1
Model variables and scaling factors
<table id="3-1">
<tr><td id="3-2">Variable</td><td id="3-3">Decription</td><td id="3-4">Scaling factor</td></tr>
<tr><td id="3-5">V</td><td id="3-6">Viral load per epithelial cell*</td><td id="3-7">H* = 1.7 x 10⁻¹¹M</td></tr>
<tr><td id="3-8">H</td><td id="3-9">Proportion of healthy cells</td><td id="3-a">H* = 1.7 x 10⁻¹¹M</td></tr>
<tr><td id="3-b">I</td><td id="3-c">Proportion of infected cells</td><td id="3-d">H* = 1.7 x 10⁻¹¹M</td></tr>
<tr><td id="3-e">M</td><td id="3-f">Activated antigen presenting cells per homeostatic level</td><td id="3-g">M* = 10⁻¹⁵M</td></tr>
<tr><td id="3-h">F</td><td id="3-i">Interferons per homeostatic level of macrophages</td><td id="3-j">M* = 10⁻¹⁵ M</td></tr>
<tr><td id="3-k">R</td><td id="3-l">Proportion of resistant cells</td><td id="3-m">H* = 1.7 x 10⁻¹¹ M</td></tr>
<tr><td id="3-n">E</td><td id="3-o">Effector cells per homeostatic level</td><td id="3-p">E* = 10⁻¹⁶ M</td></tr>
<tr><td id="3-q">P</td><td id="3-r">Plasma cells per homeostatic level</td><td id="3-s">P* = 1.8139 x 10⁻²⁰ M</td></tr>
<tr><td id="3-t">A</td><td id="3-u">Antibodies per homeostatic level</td><td id="3-v">A* = 7.2 x 10⁻¹¹ M</td></tr>
<tr><td id="3-w">β</td><td id="3-x">Antigenic distance</td><td id="3-y"></td></tr>
</table>
*V = 1 corresponds to 10^10 particles/ml respiratory epithelial cells.

<a id='b795bbe9-ca95-4b88-93cb-db72285e0782'></a>

APC stimulate the production of interferon α and β (F) that interact with healthy cells and convert them to a resistant state. APC also stimulate the proliferation of effector cells (E) that destroy infected cells. Finally, they stimulate the production of plasma cells (P) which, in turn, produce antibodies (A) that neutralize virus. This neutralization is modulated by the antigenic compatibility (S) between virus and antibodies currently produced by the organism. S quantifies the affinity between antibodies and virus.

<a id='923ccaf8-f675-4d88-bb14-61d2770e15ec'></a>

These interactions were used in the construction of a system of 10 ordinary differential equations describing the dynamics of the main variables, listed in Table 1, which correspond to the components of the immune response shown in Fig. 1:

<a id='6adb0e2e-f284-456a-b278-b538158fb21b'></a>

$$\frac{dV}{dt} = \gamma_V I - \gamma_{VA} SAV - \gamma_{VH} HV - \alpha_V V - \frac{a_{V1} V}{1 + a_{V2} V} \quad (1)$$

<a id='79f73e21-1ff3-48d2-b92b-34083a73eca4'></a>

dH/dt = b_HD D(H + R) + a_R R - \gamma_{HV} VH - b_{HF} FH, (2)

dI/dt = \gamma_{HV} VH - b_{IE} EI - a_I I, (3)

dM/dt = (b_{MD}D + b_{MV} V)(1 - M) - a_M M, (4)

dF/dt = b_{FM} M + c_F I - b_{FH} HF - a_F F, (5)

dR/dt = b_{HF} FH - a_R R, (6)

dE/dt = b_{EM} ME - b_{EI} IE + a_E(1 - E), (7)

dP/dt = b_{PM} MP + a_P(1 - P), (8)

dA/dt = b_{AP} P - \gamma_{AV} SAV - a_A A, (9)

<a id='ce61e80e-d240-40d2-9585-d891199d57c4'></a>

$$\frac{dS}{dt} = rP(1 - S). \qquad (10)$$

<a id='8cedb6f8-488c-432e-a4ff-b44914fd47de'></a>

No differential equation is needed for the proportion of dead cells (D) which is given by

$D = 1 - H - R - I.$

(11)

<a id='bc89aa5f-9a94-4970-87d2-ce84ac547955'></a>

The variable D serves as a marker for tissue damage (Hayden et al., 1998) and an indicator of the severity of disease. All variables have been rescaled by their constant homeostatic values (see Table 1) and hence the system (1)-(11) is dimensionless.

<a id='83e662c6-95a1-40f8-a876-ebf1a0f0faf1'></a>

The interactions are based on clonal selection theory, mass-action kinetics, characteristics of interactions and the birth-death balances of populations of cells and molecules: Eq. (1) of the system describes the rate of change of virus concentration V. It expresses the production rate of a viral particle by infected cells, rate of neutralization of IAV by specific antibodies, the rate of adsorption of viral particles by healthy cells, and the natural decay of viral particles. The viral particles are also removed from the respiratory tract by nonspecific mechanisms. The nonspecific muco-ciliary removal of virions supported by cough and other mechanisms is described by the term (av₁V)/(1+av₂V), which saturates with increasing V as the available capacity of these mechanisms is exhausted. Note that the lethal damage of an infected cell by the effector cells does not cause any release of infective IAV and hence in Eq. (1) there is no term of the form EI.

<a id='7f88e209-a1c1-4708-99d0-f1a2ef1802f4'></a>

Eq. (2) determines the time rate of change of healthy cells H. During recovery, new healthy cells are generated as a result of proliferation of both healthy and resistant cells (the offspring of resistant cells lose resistance) and hence the proliferation term is proportional to (H+R), and to D (in a logistic fashion) since regeneration can only occur in the presence of damage. Resistant cells R gradually lose their resistance to infection and return into their initial sensitive state (healthy state) (Joklik, 1985), which is characterized by the term aRR. The term \u03b3HVVH is the loss of healthy cells due to infection and the term bHFFH characterizes transition of the healthy cells into resistant state.

<!-- PAGE BREAK -->

<a id='355cdebe-0dbd-4ae1-8889-ffead1e393b1'></a>

74

<a id='2fe139a1-311a-486a-9661-b9701b5bd971'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='6cd2c82a-6a94-4895-9b30-608d223f042b'></a>

Eq. (3) characterizes the time rate of change of infected cells _I_. The infection of healthy cells by virions is described in the term _γHVVH_. The term _aI_ indicates the natural death of infected cells during which new virus particles are produced. The term _bIE EI_ characterizes the destruction of infected cells by effector cells (CTL and NK) during which no new virus is produced.

<a id='67a9638c-7bd6-454b-8105-37cda91684af'></a>

Eq. (4) establishes that the time rate of increase of activated APC (_M_) is proportional to the amount of the virus and the amount of dead cells. The natural decay of activated state of APC is represented by the last term in that equation.

<a id='fe5fba3b-22a9-4553-a2bd-70e1bd989ba3'></a>

Eq. (5) describes the time rate of change of interferons α and β (F) which depends on the production rate of F by APC and by infected cells, on the rate of F binding healthy cells, as well as on the nonspecific decay of F.

<a id='9f5a81b9-fb92-4322-843a-18d80f724c7c'></a>

Eq. (6) shows that resistant cells R are induced from
healthy cells ($b_{HF}FH$) and convert back to healthy cells
($a_R R$) with finite lifetime.

<a id='5f4d1267-477a-4d7a-961d-e3198c29a38e'></a>

Eq. (7) characterizes the rate of change of effector cells E concentration and takes into account the production rate of effector cells stimulated by APC (first term) and the destruction rate of infected cells by effector cells (second term, bEIE). The terms aE(1-E) and aP(1-P) in Eqs. (7) and (8) are approximate expressions for homeostatic maintenance of the levels of active effectors and plasma cells, reflecting the observation that the healthy body tends to maintain their concentrations within narrow bounds. In a healthy state the effectors and plasma cells are naturally located in lymph nodes and blood, and migrate into the infected tissue upon activation. Both the activation and migration of those cells to the infected tissue are assumed to be much faster than their proliferation and hence are not explicitly accounted for. The first term in Eq. (8) characterizes the activation process of plasma cells stimulated by APC.

<a id='aedbd650-94c9-4e1a-b215-2cf07d0d4ade'></a>

Eq. (9) stands for the time rate of change of the concentration of antibodies A describing the production rate of A by plasma cells (first term), the neutralization rate of free viral particles by specific antibodies (second term) and the natural decay rate of A (last term).

<a id='54911cdc-96b6-4e6d-ab9d-29e28a6ab315'></a>

The variable S in our model represents the compatibility between antibodies and the virus strain in an individual and ranges from 0 (no compatibility) to 1 (maximal compatibility) and can be interpreted as a measure of binding affinity of the antibody and the virus (Smith et al., 1999). The immune memory of the host is described by the initial value S(0) of S. During the course of the disease, S increases as plasma cells produce antibodies increasingly compatible with viral antigens. The rate of increase of S is approximated by the term rP(1-S) which accounts for two natural observations: (i) the increase in S is stimulated by plasma cells and (ii) S cannot increase beyond 1. By adjusting the time evolution of S we may observe how the course of the disease depends on the evolution of antigenic distance.

<a id='d5a0c767-184a-4f8c-9617-d425f4ce33d8'></a>

It has been established that IAV boosts T cell and B cell memory (Ada and Jones, 1986). However, the majority of

<a id='2b10dbb8-8d6c-4935-add8-4b716b0affc4'></a>

IAV-induced CTL are fully cross-reactive with related strains and would provide heterotypic immunity, while antibodies (and consequently B memory cells) are protective only against reinfection by strains closely related to the stimulating IAV (Bocharov and Romanyukha, 1994). Thus a variable analogous to S for description of the antigenic distance between effectors and the virus is not necessary.

<a id='e993b18f-9929-467f-966c-24d7a383931d'></a>

We note that a number of assumptions in the model are strong simplifications of our knowledge of immune physiology. The populations of cells and virions are assumed to be uniformly distributed over the epithelial layer at all times. It is also assumed that time rate of change of any model variable is determined by the present value of all variables. Some of the variables do not have uniquely identifiable biological counterparts. For example, there is no single biological entity or marker that represents the APC in our model, which are assumed to provide both antigen presenting and IFN producing functions. We have also omitted intermediate steps in the pathways: for example, we do not account for the intermediate steps in the production of effector cells and plasma cells such as Th1 and Th2 helper cells and B-cells. We do not consider time delays in the reproduction of cellular components.

<a id='d1c9eb62-315b-435f-9b0e-f81d387d9212'></a>

Although our model is similar on that of Bocharov and Romanyukha (1994), it differs in a number of instances that reflect the latest knowledge about biology of influenza: (i) we include a new nonspecific virus removal term in Eq. (1), which results in clearing out extremely low initial virus concentrations, (ii) we make the cell regeneration rate proportional to the product of healthy cells and dead cells, as opposed to only dead cells, (iii) we include reproduction of resistant cells, (iv) we make the activation of APC proportional to the amount of both viral particles and dead cells, (v) we include a new term describing the production of interferons by infected cells and (vi) we introduce a new variable that accounts for the antigenic distance between antibodies and the virus.

<a id='0d4cbfa3-3c38-4703-b9c7-5a1705aae85c'></a>

2.3. Simulations

We use the dynamical systems analysis software XPPAUT (www.pitt.edu/~phase/) to run all simulations. The time courses of variables were obtained by numerical integration using parameters provided in Table 2. Model parameters were adjusted so that the response of the naïve host to the standard initial conditions (see below) satisfies the following criteria, extracted from available experimental and clinical data (Bocharov and Romanyukha, 1994):
(i) Virus titers V peak 4-5 days after infection with an approximately 10^4-fold increase over the initial level.
(ii) The maximum amount of activated APC M is 40%. APC become deactivated within 8-10 days.
(iii) Effector cells E peak with approximately 10^2-fold increase over the homeostatic level.
(iv) P cells peak with approximately 10^4-fold increase.
(v) S changes gradually. After 15 days, the antibodies A are 80% compatible with the virus.
(vii) Maximum level of dead cells Dmax is 36%. (ix) Interferons

<!-- PAGE BREAK -->

<a id='cd0fb353-576d-4478-96be-37225e0dce73'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70-86

<a id='8ce6176e-7de4-49ba-94e9-7dfe4f940e25'></a>

75

<a id='64de89d4-f420-4826-9469-44a9655829e1'></a>

Table 2
Model parameters used for the baseline case
<table id="5-1">
<tr><td id="5-2">Parameter</td><td id="5-3">Value</td><td id="5-4">Description</td><td id="5-5">Comments</td><td id="5-6">Sources</td></tr>
<tr><td id="5-7">γV</td><td id="5-8">510</td><td id="5-9">Rate constant of influenza A virus (IAV) particles secretion per infected epithelial cells</td><td id="5-a">About 10³-10⁴ virus particles are released from a single infected cell within a day</td><td id="5-b">Zdanov and Bukrinskaja (1969)</td></tr>
<tr><td id="5-c">γVA</td><td id="5-d">619.2</td><td id="5-e">Rate constant of neutralization of IAV by antibodies</td><td id="5-f">1-10 antibodies are sufficient to neutralize a single IAV (Wohlfart, 1988)</td><td id="5-g">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-h">γVH</td><td id="5-i">1.02</td><td id="5-j">Rate constant of adsorption of IAV by infected epithelial cells</td><td id="5-k">In vitro experiments show that a single epithelial cell can adsorb 1-10 influenza virions</td><td id="5-l">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-m">αV</td><td id="5-n">1.7</td><td id="5-o">Rate constant of nonspecific IAV removal</td><td id="5-p">Nonspecific physical removal of infective virions takes about 4-24h</td><td id="5-q">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-r">ανι</td><td id="5-s">100</td><td id="5-t">Rate constant of nonspecific IAV removal</td><td id="5-u"></td><td id="5-v"></td></tr>
<tr><td id="5-w">av2</td><td id="5-x">23000</td><td id="5-y">Rate constant of nonspecific IAV removal</td><td id="5-z"></td><td id="5-A"></td></tr>
<tr><td id="5-B">bHD</td><td id="5-C">4</td><td id="5-D">Rate constant of regeneration of epithelial cells</td><td id="5-E">The duration of a single division of an epithelial cell is about 0.3-1 day</td><td id="5-F">Keenan et al. (1982)</td></tr>
<tr><td id="5-G">aR</td><td id="5-H">1</td><td id="5-I">Rate constant of epithelial cells&#x27; virus resistance state decay</td><td id="5-J"></td><td id="5-K">Marchuk et al. (1991)</td></tr>
<tr><td id="5-L">HV</td><td id="5-M">0.34</td><td id="5-N">Rate constant of epithelial cells infected by IAV</td><td id="5-O">The difference between YV and уни is caused by the fact that more than one virion are required to infect a healthy cell</td><td id="5-P">Marchuk et al. (1991)</td></tr>
<tr><td id="5-Q">bHF</td><td id="5-R">0.01</td><td id="5-S">Rate constant of epithelial cells&#x27; virus resistant state induction</td><td id="5-T"></td><td id="5-U">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-V">bIE</td><td id="5-W">0.066</td><td id="5-X">Rate constant of infected epithelial cells that CTL damage</td><td id="5-Y">A single effector cell can deliver approximately 10 lethal hits</td><td id="5-Z">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-10">aI</td><td id="5-11">1.5</td><td id="5-12">Rate constant of infected epithelial cells damage by cytopathicity of IAV</td><td id="5-13">The life time of an infected cell is approximately 1 day</td><td id="5-14">Zdanov and Bukrinskaja (1969)</td></tr>
<tr><td id="5-15">bMD</td><td id="5-16">1</td><td id="5-17">Rate constant of stimulation of antigen presenting cells by dead cells</td><td id="5-18"></td><td id="5-19">Marchuk et al. (1991)</td></tr>
<tr><td id="5-1a">bMV</td><td id="5-1b">0.0037</td><td id="5-1c">Rate constant of stimulation of antigen presenting cells by virus particles</td><td id="5-1d"></td><td id="5-1e">Marchuk et al. (1991)</td></tr>
<tr><td id="5-1f">aM</td><td id="5-1g">1</td><td id="5-1h">Rate constant of stimulated state loss of antigen presenting cells</td><td id="5-1i"></td><td id="5-1j">Marchuk et al. (1991)</td></tr>
<tr><td id="5-1k">bF</td><td id="5-1l">250,000</td><td id="5-1m">Interferon (IFN) production rate per APC</td><td id="5-1n"></td><td id="5-1o">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-1p">cF</td><td id="5-1q">2000</td><td id="5-1r">Interferon (IFN) production rate per infected cell</td><td id="5-1s">Interferon α and β (IFN) are secreted also from infected cells (Julkunen et al., 2000)</td><td id="5-1t">Estimated</td></tr>
<tr><td id="5-1u">bFH</td><td id="5-1v">17</td><td id="5-1w">Rate constant of epithelial cells that IFN binds</td><td id="5-1x"></td><td id="5-1y">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-1z">aF</td><td id="5-1A">8</td><td id="5-1B">Rate constant of IFN&#x27;s natural decay</td><td id="5-1C"></td><td id="5-1D">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-1E">bEM</td><td id="5-1F">8.3</td><td id="5-1G">Rate constant of stimulation of effector cells</td><td id="5-1H"></td><td id="5-1I">Marchuk et al. (1991)</td></tr>
<tr><td id="5-1J">bEI</td><td id="5-1K">2.72</td><td id="5-1L">Rate constant of death of effectors by lytic interactions with infected epithelial cells</td><td id="5-1M">A single effector cell can kill about 100 infected cells</td><td id="5-1N">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-1O">aE</td><td id="5-1P">0.4</td><td id="5-1Q">Rate constant of natural death of effector cells</td><td id="5-1R"></td><td id="5-1S">Marchuk et al. (1991)</td></tr>
<tr><td id="5-1T">bPM</td><td id="5-1U">11.5</td><td id="5-1V">Rate constant of plasma cells production</td><td id="5-1W"></td><td id="5-1X">Marchuk et al. (1991)</td></tr>
<tr><td id="5-1Y">aP</td><td id="5-1Z">0.4</td><td id="5-20">Rate constant of natural death of plasma cells</td><td id="5-21"></td><td id="5-22">Marchuk et al. (1991)</td></tr>
<tr><td id="5-23">$b_A$</td><td id="5-24">0.043</td><td id="5-25">Antibody production rate per plasma cells</td><td id="5-26"></td><td id="5-27">Marchuk et al. (1991)</td></tr>
<tr><td id="5-28">$\gamma_{AV}$</td><td id="5-29">146.2</td><td id="5-2a">Rate constant of antibodies which binds to IAV</td><td id="5-2b"></td><td id="5-2c">Bocharov and Romanyukha (1994)</td></tr>
<tr><td id="5-2d">$a_A$</td><td id="5-2e">0.043</td><td id="5-2f">Rate constant of natural death of antibodies</td><td id="5-2g"></td><td id="5-2h">Marchuk et al. (1991)</td></tr>
<tr><td id="5-2i">$r$</td><td id="5-2j">3e-5</td><td id="5-2k">Rate constant for S variable</td><td id="5-2l"></td><td id="5-2m">Estimated</td></tr>
</table>

<a id='b14ed802-a13d-4283-b8d3-b62ddd67f7a9'></a>

F peak with approximately 104-fold increase. (x) Anti-bodies A peak with approximately 103-fold increase. Most of our parameters are close to those in Bocharov and Romanyukha (1994) yet rescaled to dimensionless quantities. To examine the robustness of infection dynamics to parameter values and to provide insight into inter-individual variation in disease dynamics, we conducted a full set of one-dimensional sensitivity analyses.

<a id='81cf26d1-27c2-4398-a665-52954e7bad1d'></a>

## 3. Results

### 3.1. Standard behavior

The standard behavior describes the course of infec-tion in a naïve host. We assume that initially the host has no dead, infected or resistant cells, no interferon molecules, and no activated APC (i.e., H(0) = 1,

<!-- PAGE BREAK -->

<a id='5ef4a863-fc8a-4074-9c4c-0f7e3be65854'></a>

76

<a id='39712b80-09d6-484f-9240-81ae1e71330b'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='74c046e0-5e81-4a9e-8a1a-a49a4bbae65c'></a>

I(0) = M(0) = F(0) = R(0) = 0). The initial levels of effectors, plasma cells, and antibodies are assumed to be at the homeostatic values (i.e., E(0) = P(0) = A(0) = 1) (Asquith and Bangham, 2003). The influence of antigenic compatibility S on the progression of infection is described in the subsection "Impact of Antigenic Distance" below. In a naïve host, we assume that S(0) = 0.1 which corresponds to a relatively low compatibility with the virus strain, that may have resulted from previous exposure to IAV and subsequent genetic drift. In the typical course of acute IAV infection, the initial concentration of aerosol delivered virus particles that the host receives is about 10⁸ particle per ml on day 0, corresponding to V(0) = 0.01 in our dimensionless system.

<a id='685df3e3-6052-44ac-8120-601c1ce73b85'></a>

The resulting time courses of model variables corre-sponding to naïve infection are depicted in Fig. 2. As seen in Fig. 2(a), virus level peaks (period of maximum antigen concentration) after 5 days. This relatively late onset of the disease is the result of relatively low initial viral load used in our simulation. Peak viral load is increased by 104-fold with respect to initial value staying at peak approximately 3 more days, in accord with experimental data (Tamura et al., 1998). Viral load starts to decline to inoculation level after day 8 (early stage of recovery, disappearance of IAV particles). The host is considered infectious when the virus level exceeds 1, which happens at day 4.9. The host remains infectious for 2.6 days. APC are activated after 5 days peaking after about 7 days and returning to homeostatic levels within 8–10 days.

<a id='68e444bf-637f-47b4-a978-45c5e205402b'></a>

The resulting loss of respiratory epithelial cells (dead
cells) is one major reason for several of the symptoms that
accompany infection, such as cough, depressed tracheo-
bronchial clearance, and altered pulmonary function
(Hayden et al., 1998). We consider the host "symptomatic"
if the damage level exceeds 10% of the epithelial cells
(Marchuk and Berbentsova, 1986), which occurs when the
viral load peaks at day 5. The maximum proportion of
dead cells is 36% attained at day 6.1. The host stays
symptomatic for 2.4 days after which time most of the cells
become resistant to the infection. Infected cells reach a
maximum proportion of 53% of all cells after day 5.2,
while the proportion of resistant cells peak after 9 days,
which is in accord with the experimental observation that
the expression of nucleoprotein (NP) mRNA in epithelial
cells, showing the presence of infected cells, changes in
parallel with viral titer (Fig. 2(b)) (Tamura and Kurata,
2004).

<a id='dbcd73ae-2c28-40ee-9fe6-31b91e790573'></a>

Interferon response comes into play once the virus peaks at day 5 making most of the cells resistant to infection. The interferon level is increased by 10⁴-fold peaking approximately at day 6. Plasma cells are produced after 6 days peaking at 9 days, before virus-specific antibodies are detectable, in accord with empirical observations (Ada and Jones, 1986). Antibody production by plasma cells begins at day 7. There is a 10³-fold increase in the amount of antibodies when the adaptive immune response comes into play to remove all viral particles and generate immune

<a id='348bcc42-d9e2-4205-b1ab-a2e7f2d7fd78'></a>

memory. Furthermore, antigenic compatibility is increas-
ing monotonically starting right after when the adaptive
immunity is activated (after day 8) and the antibodies are
capable of inhibiting viral particles with 80% probability
after 15 days of infection.

<a id='7e80c371-e72a-404a-9900-b9f75e9c0b33'></a>

3.2. *Impact of viral load*
We investigated the impact of initial viral load on the
onset, duration and severity of infection to understand
the immune response of a naïve host to a moderate virus
strain. It has been realized that IAV infection could result
in large spectrum of disease states, however, this spectrum
of severity has not been understood well (Yetter et al.,
1980).

<a id='a10ead1f-be3c-4543-94e0-869d9b3cad20'></a>

As seen in Fig. 3, the immune response falls into one of the three categories depending on initial viral load, V(0): asymptomatic disease, typical disease, and severe disease (Asquith and Bangham, 2003). If V(0) is less than the threshold V₁, the disease never develops. This corresponds to asymptomatic infection in which no virus shedding is observed. The host is considered not contagious in this case since the virus is eliminated from the host promptly and viral load remains very low with almost no ensuing damage. If V(0) is in the range between V₁ and V₂, the disease follows the same trajectory but the larger V(0) the sooner the onset of the disease. In other words, in this range of V(0), the maximum viral load (Vmax = 138), maximum damage (Dmax = 36%), the duration of symptoms, and length of contagious period are all *independent* of V(0). If V(0) is larger than V₂, the disease state corresponds to severe disease for which the maximum viral load and damage increase with V(0). In this case maximum damage can exceed 50% of the respiratory cell population. Such levels of damage represent serious situation in which secondary infections could develop resulting in the death of the host. For standard parameter values the thresholds are V₁ = 0.00227 and V₂ = 0.1, with V₁ producing a trajectory terminating at a saddle node (see below), and V₂ being an approximate quantity determined as the lowest value of V(0) for which the trajectory perceptibly departs from the typical behavior.

<a id='6a51afba-fbe1-42de-93f8-e52702de54fd'></a>

Fig. 3(c) shows the projection of the phase diagram onto the variables V and D. In this projection the trajectories have only a very limited tendency to cross. The trajectories for initial conditions V₁<V(0) <V₂ all coincide, in accord with the observation that the trajectories are very similar and only shifted in time. On this plot the trajectory with V(0) = V₁ terminates at the point (V, D) = (0.0015, 0.0001). Note that because the graphs are plotted on a logarithmic scale and D(0) = 0, the trajectories originate off the graph on the left.

<a id='fdc1a91b-613a-4eae-bcff-02c8c0a853c4'></a>

### 3.3. Stability analysis

As expected, the flow of the dynamical system defined by
Eqs. (1)-(11) leaves invariant the physiological region of

<!-- PAGE BREAK -->

<a id='ea2a5b7c-7c1f-4033-befb-94b673007f14'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='e94f82e8-ec0d-4f7a-9488-45bdce37e0c8'></a>

77

<a id='1cc67801-ffe4-41f6-bfc7-abde6eaebdf9'></a>

<::chart: The figure contains four vertically stacked line plots, all sharing a common x-axis labeled "Days" ranging from 0 to 15.  

**Top Plot (V - Viral Load)**:  
- Y-axis is logarithmic, from 10^-5 to 10^2.  
- The curve starts at approximately 10^-3 at Day 0, rises sharply to a peak of around 10^2 between Day 5 and 6, then rapidly declines to below 10^-5 by Day 8.  

**Second Plot (M - Proportion of Infected Cells)**:  
- Y-axis is linear, from 0.0 to 1.0.  
- The curve starts at 0, rises to a peak of about 0.35 between Day 6 and 7, and then gradually decreases back to 0 by Day 10-11.  

**Third Plot (E - Total Number of Epithelial Cells)**:  
- Y-axis is logarithmic, from 10^-2 to 10^2.  
- The curve starts at 10^0 (1) at Day 0, remains relatively constant until around Day 5, dips slightly below 10^0, then increases sharply to a peak near 10^2 by Day 9, and slowly declines thereafter.  

**Bottom Plot (D - Proportion of Resistant Cells)**:  
- Y-axis is linear, from 0.0 to 1.0.  
- The curve starts at 0, rises to a peak of about 0.35-0.4 between Day 6 and 7, and then gradually decreases back to 0 by Day 10-11.  

**Caption**:  
Fig. 2. Time-courses of the viral load, proportion of resistant cells, proportion of infected cells, and antigenic compatibility of the virus during disease. Initially, the viral load is V(0) = 0.01, all cells are at their homeostatic levels, and antigenic compatibility S(0) = 0.5. The curves show the concentration of virus (V), the proportion of infected epithelial cells (M), the total number of epithelial cells (E), and the proportion of resistant cells (D). For E, the dashed line indicates the homeostatic level of epithelial cells: at any given time, below the red curve is the proportion of susceptible epithelial cells, and blue the proportion of resistant cells, and above blue the proportion of infected epithelial cells.::>

<a id='d7792033-9fd9-4dda-baf1-54de578b9747'></a>

<::Four line graphs stacked vertically, sharing a common x-axis labeled "Days" from 0 to 15. The top graph, labeled "H" on the y-axis (0.0 to 1.0), shows a curve starting at 1.0, dropping sharply between days 4 and 6 to near 0.0, and then gradually rising again from day 9 to about 0.8 by day 15. The second graph, labeled "F" on the y-axis (logarithmic scale from 10⁻¹ to 10⁴), shows a curve starting low, increasing to a peak around day 7-8 (approximately 10⁴), and then decreasing. The third graph, labeled "P" on the y-axis (logarithmic scale from 10⁻¹ to 10⁴), shows a curve starting low, rising sharply between days 5 and 8, peaking around day 10 (approximately 10⁴), and then slowly declining. The bottom graph, labeled "S" on the y-axis (0.0 to 1.0) and also with a vertical label "Cell proportions" on the right, shows a curve starting at 0.0, rising sharply between days 5 and 10, and continuing to rise towards 0.8 by day 15. The accompanying text states that this panel displays proportions, with implied colors for dead cells (red and green) and healthy cells (blue), though these colors are not visible in the monochromatic graph.::>f respiratory epithelial cells, and the three arms of the ls are healthy, levels of APC and interferons are zero, , S(0) = 0.1.

<a id='afe3f971-154f-46db-a6c2-296caff84eda'></a>

<::Figure: Four plots showing time-course dynamics. All plots share a common x-axis labeled "Days" ranging from 0 to 15. The surrounding text describes "the immune response for a standard course of the" and mentions "effector cells, plasma cells and antibodies are at cumulative proportions of types of respiratory" and "the proportion of infected cells, between green".

Plot 1 (Top):
- Y-axis: "I", ranging from 0.0 to 1.0.
- A single black curve starts at 0, rises to a peak of approximately 0.55 around day 5, and then declines back to 0 by day 15.

Plot 2:
- Y-axis: "R", ranging from 0.0 to 1.0.
- A single black curve starts at 0, begins to rise around day 3, increases sharply from day 4 to day 7, reaching a peak near 0.9 around day 9, and then gradually declines, ending above 0 by day 15.

Plot 3:
- Y-axis: "A", on a logarithmic scale from 10^3 to 10^-5.
- A single black curve starts around 10^0, drops sharply to a minimum near 10^-4 around day 5, then rises sharply to a plateau near 10^3 by day 10, remaining high until day 15.

Plot 4 (Bottom):
- Y-axis: "Cell proportions", ranging from 0.0 to 1.0.
- Contains four labeled curves:
  - Blue curve: Labeled "healthy" at the beginning and end, and "resistant" in the middle. It starts at 1.0, drops sharply to near 0 around day 5, then rises to a plateau near 1.0 (labeled "resistant") from day 7 to day 12, and finally declines slightly before rising back to 1.0 (labeled "healthy") by day 15.
  - Green curve: Labeled "infected". It starts at 0, rises to a peak of approximately 0.7 around day 6, and then declines back to 0 by day 9.
  - Red curve: Labeled "dead". It starts at 0, rises to a peak of approximately 0.3 around day 6.5, and then declines back to 0 by day 9.::>

<a id='37eefe40-373b-48da-a170-06c2c77961ff'></a>

the phase space obeying 0≤(V, F, E, P, A), 0≤(H, I, R, D,
S, M)≤1. Within that region, for the baseline parameter
values, the system (1)-(11) with parameters as in Table 2
has 3 steady states. One is the healthy steady state xh at
which (V, H, I, M, F, R, E, P, A, S) = (0, 1, 0, 0, 0, 0, 1, 1,

<a id='12c3334a-0e97-4b2e-b55b-8880d3b88403'></a>

1, 1), the second is a threshold state $x_{th}$ for which ($V$, $H$, $I$,
$M$, $F$, $R$, $E$, $P$, $A$, $S$) = (0.0014698, 0. 9865, 0.00031472,
0.00012869, 1.3243, 0.013064, 1.0005, 1.0037, 0.16739, 1),
and the third one is a high-virulence state $x_v$ for which
($V$, $H$, $I$, $M$, $F$, $R$, $E$, $P$, $A$, $S$) = (2.9646, 0.0903, 0.056947,

<!-- PAGE BREAK -->

<a id='fb55a7f8-f521-49c0-8f60-8daa22215ee8'></a>

78

<a id='a7384779-d2c3-4055-9443-f46b9110ad39'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='61214433-c7fc-4fe1-b417-a8e2bc60be0e'></a>

<::chart: This figure presents three plots related to viral load and damage dynamics. Fig. 3. Time-courses of (a) viral load and (b) damage for various levels of the initial viral load V(0). For V(0) in the range from 0.00227 to 0.1 the dependence of V on t (and of D on t) follows the same trajectory but the larger V(0) the sooner the onset of the disease. (c) Phase diagram of the dependence on initial viral load V(0) as a plot of log V versus log D. The direction of time is indicated by arrows. The maximum viral load and maximum damage for typical disease are Vmax = 1.3 × 10¹⁰ particles/ml and Dmax = 36. The thresholds V₁ = 0.00227 for the typical disease and V₂ = 0.1 for the extreme disease are indicated and the corresponding trajectories are shown in black.  (a) A line chart showing the time-courses of viral load (V) on the y-axis (log scale from 10^-8 to 10^2) versus Days on the x-axis (0 to 15). The legend indicates different initial viral load V(0) values: 0.001 (green line, decreasing), 0.00227 (blue line, constant then decreasing), 0.01 (cyan line, peaking around 5 days), 0.1 (magenta line, peaking around 3 days), and 200 (red line, peaking early).  (b) A line chart showing the time-courses of damage (D) on the y-axis (0.0 to 1.0) versus Days on the x-axis (0 to 15). The legend indicates different initial viral load V(0) values: 0.01 (cyan line, peaking around 5 days), 0.1 (magenta line, peaking around 3 days), and 200 (red line, peaking early).  (c) A phase diagram showing log V (viral load) on the y-axis (10^-7 to 10^2) versus log D (damage) on the x-axis (10^-7 to 10^0). Arrows indicate the direction of time along the trajectories. Key labels include: Vmax and Dmax. Disease states are indicated by horizontal lines: Severe disease, Typical disease (between V₂=0.1 and V₁=0.00227), and Asymptomatic disease. Trajectories are shown for V(0) values: 200 (red, reaching Vmax/Dmax), 0.1 (black, reaching Vmax/Dmax), 0.01 (magenta, lower peak V, D), 0.00227 (black, lower peak V, D), and 0.001 (green, lowest peak V, D). The black trajectories correspond to V₁ = 0.00227 and V₂ = 0.1 as indicated in the caption.::>

<a id='1079ad86-0107-4f28-be98-9cd4473de4b0'></a>

0.034516, 916.91, 0.82797, 1.49024, 130.29, 0.012925, 1).
The threshold state corresponds to the separator for the
dynamics of influenza between the asymptomatic disease
and typical disease cases as seen in Fig. 3. The Jacobian
matrix for the linearization of system (1)-(11) about the
healthy state xh admits eigenvalues that are all real and
negative, and hence the healthy fixed point is asymptoti-
cally stable. We find that, with the exception of a small
number of cases, the healthy state remains stable under
perturbations of the parameters of the system. The
Jacobian matrix for the threshold state xth has two complex
and one positive eigenvalue and hence xth is a saddle node.
The Jacobian matrix for the high-virulence state xv has two
complex eigenvalues with positive real parts and hence xv is
an unstable spiral. As discussed below, the xv becomes
stable at fixed, extremely low values of S(0).

<a id='aaa7a080-18bc-4ec1-b244-45822e08de45'></a>

### 3.4. Sensitivity analysis

The goals of sensitivity analysis with respect to random perturbations of the model parameters are the following:

*   To show how robust the simplified uncomplicated influenza model is in relation to perturbed parameter values.

<a id='2d17506d-7099-4990-83e9-b381bdb7c127'></a>

* To explore to which parameters the system is more sensitive to understand key processes and immune system mechanisms.

<a id='abbd96cb-57c7-4f4f-b363-2dbf6b9a416a'></a>

Our approach to investigate sensitivity was based on studying the effect of changes in the parameters (in every case we increased and decreased the baseline value threefold) on the duration, onset and severity of the disease (Table 3). In clinical studies, the assessment of influenza virus pathogenicity is based on the magni- tude and duration of fever, the frequency and amount of virus shedding, and the level and persistence of the infection. Within the model framework we can generalize these clinically relevant correlates into the following characteristics: (I) the severity of the disease measured as the maximum attained proportion of dead cells Dmax = max_t>0D(t), (II) the duration of symptomatic infec- tion Atillness = t2-t1, where t₁ is the time that D exceeds 0.1 and t2 is the time that D drops below 0.1 (III) simi- larly, the value V = 1 is considered to be the threshold level for becoming contagious and the duration of infectivity will be referred to as At contagious. For typi- cal disease, we find that Atillness = 2.4 days and At contagious = 2.6 days.

<!-- PAGE BREAK -->

<a id='b30707a5-cfb9-44e0-88be-9254893192c0'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70-86

<a id='b1df4564-725a-421f-a5a9-8ba7e686f615'></a>

79

<a id='7e38d3d4-0437-499f-95c9-da64779c8daa'></a>

Table 3<br>One-way sensitivity analysis on model parameters
<table><thead><tr><th>Parameter</th><th>Baseline (range)</th><th>Model behavior</th></tr></thead><tbody><tr><td>γHV</td><td>0.34(0.1-1)</td><td><ul><li>At high virulence, disease always develops. At low virulence, asymptomatic disease is possible.</li><li>The higher the virulence, the earlier the onset of disease.</li><li>The higher the virulence, the shorter the duration of disease.</li><li>At high virulence, damage (Dmax = 68%) is at least five times larger than that of low virulence (Dmax = 12%). So, high virulence may cause death.</li><li>At peak, virus shedding is about the same for high and low virulent viruses.</li><li>The less virulent the virus, the longer the contagious period when disease is developed.</li></ul></td></tr><tr><td>γV</td><td>510(150-1500)</td><td>The model behavior is same as in case for γHV.</td></tr><tr><td>γVA</td><td>619.2(200-1800)</td><td><ul><li>For low γVA, disease always develops.</li><li>The higher the γVA, the later the onset of disease.</li><li>At high and low values of γVA, the duration of disease is about the same.</li><li>At high and low values of γVA, the damage is about the same. At peak, virus shedding is about the same for high and low γVA.</li><li>The contagious period is about the same for various values of γVA. So, γVA only affects the onset of the disease which has the same characteristics.</li></ul></td></tr><tr><td>bMD</td><td>2(0.6-6)</td><td><ul><li>Disease always develops for all bMD.</li><li>The onset of disease stays the same.</li><li>The higher bMD, the shorter the duration of disease.</li><li>The higher bMD, the lesser the damage. Very low values of bMD may cause death. At peak, virus shedding is about the same for high and low bMD.</li><li>The higher bMD the shorter the contagious period.</li><li>If bMD is very high the onset is very late, duration is short, damage is very low, contagious period is very short.</li></ul></td></tr><tr><td>bIE</td><td>0.066(0.02-0.1)</td><td><ul><li>At high bIE, asymptomatic disease is observed for standard V(0) and S(0).</li><li>The higher bIE, the later the onset of disease.</li><li>The higher bIE, the shorter the duration of disease.</li><li>At high values of bIE, the damage is lower. Changes only in bIE only cannot cause death.</li><li>At peak, virus shedding is about the same for high and low bIE.</li><li>The higher bIE, the shorter the contagious period when disease is developed.</li></ul></td></tr><tr><td>aI</td><td>1.5(0.5-4.5)</td><td><ul><li>At high aI, asymptomatic disease is observed for standard V(0) and S(0).</li><li>The higher aI, the later the onset of disease.</li><li>The higher aI, the shorter the duration of disease.</li><li>At high values of aI, the damage is lower. Changes only in bIE only cannot cause death.</li><li>Virus shedding is very sensitive to aI. When aI is higher, at the peak viruses shed less.</li><li>The higher aI, the shorter the contagious period. But the time difference is very small.</li></ul></td></tr><tr><td>bHD</td><td>4(2-8)</td><td><ul><li>Disease always develops for all bHD for standard V(0) and S(0).</li><li>Onset of disease is about the same for all bHD.</li><li>The higher bHD the shorter the duration of disease.</li><li>At high values of bHD, the damage is lower. Changes only in bHD cannot cause death.</li><li>Virus shedding is very sensitive to bHD When bHD is higher, at the peak viruses shed more.</li><li>The higher bHD, the longer the contagious period. The time difference is significant.</li></ul></td></tr><tr><td>bF</td><td>25,000(125,000-500,000)</td><td><ul><li>Disease always develops for all bF for standard V(0) and S(0).</li><li>Onset of disease is about the same for all bF.</li><li>The higher bF, the shorter the duration of disease.</li><li>At high values of bF. the damage is lower. Very low values of pG may cause death.</li><li>Virus shedding is very sensitive to bF. When bF is higher, at the peak viruses shed less.</li><li>The higher bF, the longer the contagious period. The time difference is significant.</li></ul></td></tr><tr><td>bA</td><td>0.043(0.01-0.12)</td><td><ul><li>Disease always develops for all bA for standard V(0) and S(0).</li><li>The higher the bA, the later the onset of disease.</li><li>The duration of disease is about the same for all bA.</li><li>At high values of bA, the damage is lower. Changes only in bA cannot cause death.</li><li>Virus shedding is sensitive to bA. When bA is higher, viruses shed a little at the peak less.</li><li>The higher bA, the shorter the contagious period. The time difference is small.</li></ul></td></tr><tr><td>bHF</td><td>0.02(0.005-0.03)</td><td><ul><li>At high bHF, asymptomatic disease is observed for standard V(0) and S(0).</li><li>Onset of disease is about the same for all bHF.</li><li>The higher bHF, the shorter the duration of disease.</li></ul></td></td></tr></tbody></table>

<!-- PAGE BREAK -->

<a id='fd0ca694-c004-46ad-b03e-afc0dae63aec'></a>

80
B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='344ef687-49e4-4731-8a19-37a3ae7a9a40'></a>

Table 3 (continued)
<table><thead><tr><th>Parameter</th><th>Baseline (range)</th><th>Model behavior</th></tr></thead><tbody><tr><td></td><td></td><td><ul><li>At high values of bHF, the damage is lower. Very low values of bHF may cause death.</li><li>Virus shedding is very sensitive to bHF. When bHF is higher, at the peak viruses shed significantly less.</li><li>The higher bHF, the longer the contagious period. The time difference is significant.</li></ul></td></tr><tr><td>bEM</td><td>8.3(2.5–25)</td><td><ul><li>At high bEM, asymptomatic disease is observed for standard V(0) and S(0).</li><li>Onset of disease is about the same for all bEM.</li><li>The higher the value of bEM, the shorter the duration of disease.</li><li>At low values of bEM, the damage is lower. Very high values of may cause death.</li><li>Virus shedding is not sensitive to bEM.</li><li>The higher the value of bEM, the shorter the contagious period. The time difference is not significant.</li></ul></td></tr><tr><td>bPM</td><td>11.3(3–30)</td><td><ul><li>For low values of bPM, flow goes through disease trajectory and converges to the fixed point for standard V(0) and S(0).</li><li>Onset of disease is about the same for all bPM.</li><li>The duration of disease is about the same for all bPM.</li><li>The damage is about the same for all bPM.</li><li>Virus shedding is not sensitive to bPM.</li><li>The higher the value of bPM, the shorter the contagious period. The time difference is significant.</li></ul></td></tr><tr><td>S(0)</td><td>0–1</td><td><ul><li>For S(0) = 0 disease always develop for standard V(0).</li><li>The higher the S(0), the later the onset of disease. The duration of disease is about the same for all S(0).</li><li>At high values of S(0), the damage is lower. When S(0) is higher, viruses shed less at the peak. The higher the value of S(0), the higher the contagious period during the typical disease.</li></ul></td></tr></tbody></table>

<a id='410127cb-3e1d-44fc-84d2-5bd6f1da86ed'></a>

3.5. Sensitivity to pathogen virulence

Virulence is characterized by the parameters γHV and γV, which represent the rate of infection of epithelial cells by IAV and the rate of IAV particles secretion per infected epithelial cell, respectively. When virulence is high, the viruses are able to infect the healthy cells at much higher rate and they reproduce and replicate themselves in infected cells much faster. Since the sensitivity to γHV and γV are essentially the same, we will consider only parameter γHV.

<a id='5c065f50-4d9b-49cc-a6a2-f9a860909d48'></a>

The virulence γHV affects the range of viral loads V(0)
causing typical disease. When the value of γHV is three
times more than the baseline value, then no matter what
the initial viral load is, disease always develops (see
Fig. 4(b)). When γHV is three times less than the baseline,
we observe the presence of asymptomatic, typical and
severe disease regimes depending on V(0). When V(0) is
low, the disease stays asymptomatic. The higher the
virulence, the earlier the onset of disease and the shorter
the duration of disease. The variation in maximum
damage, m_max, between the case of low γHV and the case
of high γHV is significant (we found a fivefold difference
between D_max = 68% for γHV = 1 and D_max = 12% for
γHV = 0.1). As expected, infection by virus of high
virulence causes substantial damage, while infection by a
virus of low virulence may go unnoticed. The lower the
virulence, the longer the contagious period Δt_contagious. The
duration of the disease and maximum level of virus titer at
the peak are not sensitive to the virulence. When γHV is 0.1,
the threshold value for V(0) to cause typical disease is

<a id='2bbe8799-51b8-4571-93eb-c987d07d3e51'></a>

0.00227. The phase diagram for γHV is 0.1 (not shown) is essentially the same as Fig. 3(c). The threshold point of the dynamics between the typical disease case and the asymptomatic case is due to the presence of an unstable threshold state x_th, the stable manifold of which intersects the locus of initial conditions.

<a id='4049c5ae-0ef8-4eb1-9c25-cdf726d399a2'></a>

3.6. Sensitivity to interferon response

The parameters bF and bHF characterize the interferon production rate constant and the rate constant of induction of resistant state in epithelial cells, respectively. If bF increased or lowered from its standard value, disease always develops for standard values of V(0) and S(0). However, when bHF is high, the host remains asymptomatic. The time of onset of disease does not depend on bF and bHF, but when either of these constants is higher, the duration of disease becomes shorter. Damage increases if either bF or bHF is decreased. Very low values of bF or bHF result in excessive damage (over 50%) which may presumably lead to secondary infections or death (Iwasaki and Nozima, 1977). Virus shedding is sensitive to the magnitude of bF or bHF: higher values are associated with a less virus shedding but a longer contagious period. When the interferon production rate constant is two times bigger than the baseline value (i.e., when bF = 500,000), then the host remains contagious for about 3.5 days. When this rate is two times less than the baseline (i.e., when bF = 125,000) then the contagious period is about 2.3 days. So, the difference in the length of infectious period is significant for various levels of innate immune response.

<!-- PAGE BREAK -->

<a id='f55b90f7-bdf2-4f33-9210-dc67b27b917d'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='fc3b6a4e-0f85-4787-bb41-dbdcff719d96'></a>

81

<a id='8ac5727c-aa60-4ced-8263-e75e9c8ab33c'></a>

<::figure: (a) Time-course of viral load (V) versus Days. The y-axis is logarithmic from 10^-8 to 10^2. The x-axis is linear from 0 to 15. Three curves are shown, corresponding to different values of gamma (γ): a green line for γ = 0.1, a red line for γ = 0.34, and a magenta line for γ = 1. The red curve peaks around 10^2 at approximately 2.5 days. The magenta curve peaks around 10^2 at approximately 7 days. The green curve remains at a low viral load. A legend indicates γ values: 0.1, 0.34, 1. (b) Time-course of damage (D) versus Days. The y-axis is linear from 0.0 to 1.0. The x-axis is linear from 0 to 15. Two curves are shown, corresponding to different values of gamma (γ): a red line for γ = 0.34 and a magenta line for γ = 1. The red curve peaks around 0.7 at approximately 2.5 days. The magenta curve peaks around 0.4 at approximately 7 days. A legend indicates γ values: 0.34, 1. (c) Phase diagram showing the dependence on initial viral load V(0). The x-axis is D (Damage) on a logarithmic scale from 10^-7 to 10^0. The y-axis is V (Viral load) on a logarithmic scale from 10^-7 to 10^2. Several curves with arrows indicate the direction of time. A red curve starts at V=200 (indicated by a label) and moves towards high D, then drops sharply along D=10^0 to low V. A black curve starts at V=0.1 and moves towards higher D and V, then sharply drops along D=10^0. A magenta curve starts at V=0.01 and moves towards higher D and V, then sharply drops along D=10^0. A green curve starts at V=0.001 and moves towards higher D and V, then sharply drops along D=10^0. Labels on the y-axis indicate 'Severe disease' at high V and 'Typical disease' at lower V. A horizontal line is labeled V2. Vmax and Dmax are indicated at the top right corner, corresponding to the maximum values reached by the curves. The maximum viral load and maximum damage for typical disease are Vmax = 1.1 × 10^10 particles/ml and Dmax = 68.::>
Fig. 4. Time-courses of (a) viral load and (b) damage for various values of $\gamma_{HV}$. (c) Phase diagram of the dependence on initial viral load $V(0)$ for value of $\gamma_{HV} (\gamma_{HV} = 1)$ that is threefold higher than the standard value. The direction of time for each curve is indicated by arrows. The maximum viral load and maximum damage for typical disease are $V_{max} = 1.1 \times 10^{10}$ particles/ml and $D_{max} = 68$.

<a id='65dfd89d-43aa-4987-82ad-fe692a541d1b'></a>

Even in the absence of an innate response (when b_F = 0 and b_HF = 0), the disease is eventually healed by the adaptive immune response and the organism will approach the healthy state.

<a id='0d7b5c36-cb14-4956-b0dd-f080acc97abf'></a>

3.7. Sensitivity to cellular component of innate immunity

The parameters _bEM_ and _bIE_ stand for the rate constant of production of effector cells and rate constant of removal of infected cells by effectors, respectively. For sufficiently large _bEM_ or _bIE_, the host is able to clear the disease without symptoms and typical disease conditions, given the standard initial immunity and standard initial amount of the virus. Although _bEM_ has no effect on the onset of the disease, when infected cell removal rate constant is high, the onset of infection happens later. At low values of _bEM_ or _bIE_, the symptoms last longer. When _bEM_ is high, the resulting maximum damage, _Dmax_, is large and may result in death. On the other hand, when _bIE_ is high, we observe lower damage of epithelial cells. Even under a significant decrease in _bIE_, _Dmax_ will stay under 50% and hence a decrease in _bIE_ has no effect on the mortality. Virus shedding is the same for different levels of _bEM_ or _bIE_. When there is a less vigorous cellular response, the host remains infectious for longer. But the time differences in

<a id='a7d51996-14f7-4a3f-a0c7-a2852d01d6d0'></a>

the contagious period of the host for various levels of $b_{EM}$
or $b_{IE}$ are small.

<a id='147fe3bd-c620-477b-9cec-6375d4e49f56'></a>

Even in the absence of a cellular response (when bEM = 0 and bIE = 0), virus is eventually cleared by the innate and adaptive immune responses and the organism will approach the healthy state.

<a id='ef32827c-3005-40df-a160-536e129aadca'></a>

## 3.8. Sensitivity to adaptive response

Activation of adaptive immune response is slower than activation of cellular and interferon components of innate immunity. The parameters bPM, bA and γVA stand for the plasma cell production rate constant, antibody production rate constant and the rate constant of neutralization of IAV by antibodies. For sufficiently large bPM, bA or γVA, the host is able to clear infection without symptoms after administration of a standard inoculum. Although bPM has no effect on the onset of the disease, later onset is observed with higher bA and γVA. The duration of illness does not depend on bPM, bA or γVA. Damage is lower with higher bA, while damage is insensitive to the two other rate constants. Variations in bPM, bA or γVA never result in excessive damage. Virus shedding is sensitive to bA. With higher bA, fewer viruses are shed at the peak of the disease and the contagious period is significantly shorter.

<!-- PAGE BREAK -->

<a id='aeff84a6-af8b-4f48-b471-748e856a5361'></a>

82

<a id='504dadcf-4a10-4d8c-9ba7-5284211ebee0'></a>

_B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86_

<a id='ead21735-a95f-4ae4-8a7f-2d4e81c04918'></a>

In summary, γ_VA only affects the onset of the disease,
while b_PM affects only virus shedding at the peak. The
system is much more sensitive to the b_A. We will discuss the
situation where there is no adaptive response or very weak
response in the next subsection.

<a id='79c02683-a890-4d43-a2d6-6831255a8817'></a>

3.9. _Impact of antigenic distance_

The efficiency of the existing antibodies of the organism to neutralize the virus of the strain causing the illness is represented by the variable _S_ which describes the probability of a match between the existing antibodies and the antigenic structure of the viral strain. Fig. 5(a) displays the dependence of incurred damage on _S_(0), the initial value of _S_. Previous infection with one subtype induces little or no immunity to other subtypes of the IAV (Couch and Kasel, 1983; Murphy and Clements, 1989), therefore _S_(0) for the

<a id='3a3e1dae-39eb-46a9-8f83-4b18db8aa6cf'></a>

<::chart: Fig. 5. (a) Time courses of the damage for various levels of the initial probability of the existing antibodies to neutralize IAV particles, S(0). The larger S(0) the sooner the onset of the disease. The plot shows 'D' (Damage) on the y-axis (0.0 to 1.0) versus 'Days' on the x-axis (0 to 15). A legend indicates S(0) values: '0' (red line) shows a peak around D=0.48 at Day ~2.5, and '0.1' (magenta line) shows a peak around D=0.36 at Day ~6. (b) Diagram of the dependence of the expected type of disease on V(0) and S(0). The lines correspond to the threshold values V₁ (triangles connected by green lines) and V₂ (circles connected by red lines). The regions corresponding to asymptomatic, typical and severe disease are indicated. The plot shows 'V(0)' on a logarithmic y-axis (10^-6 to 10^0) versus 'S(0)' on the x-axis (0.0 to 0.3). The green line with triangles represents V₁, and the red line with circles represents V₂. Regions are labeled: 'Asymptomatic disease' below V₁, 'Typical disease' between V₁ and V₂, and 'Severe disease' above V₂.::>

<a id='bc463339-1909-4d54-b328-97ed1e3198f9'></a>

individual facing a new subtype is very low. For the standard value of S(0), corresponding to the standard response, we chose S(0) = 0.1 which corresponds to partial match of antibodies due to the history of previous contacts of the individual with the virus, perhaps during the last season. This standard S(0) is much lower than 1 because of the antigenic drift of the virus strain. When there is no initial match at all (S(0) = 0), damage is higher (Yetter et al., 1980). When S(0) is sufficiently large, then the individual remains asymptomatic (Liew et al., 1984; Yoshikawa et al., 2004). As seen in Fig. 5(b), when S(0) = 0, disease always develops regardless of initial viral load, i.e., V₁ = −∞. The threshold for severe disease, V₂, increases with S(0). The threshold for typical disease, V₁, becomes finite when S(0) = 0.0124 and then increases with S(0). For values of S(0) above 0.2, corresponding to reasonably compatible initial immunity, the disease is asymptomatic unless V(0)>0.1. This situation corresponds to an immunized individual. The higher the S(0), the later the onset of disease. The duration of disease is about the same for all S(0). At high values of S(0), the damage is lower (Yetter et al., 1980) When S(0) is higher, less viruses are shed at the peak. The higher the value of S(0), the less the contagious period (Yetter et al., 1980).

<a id='4315284d-cddd-45e3-8871-b2acdeb9e09e'></a>

The parameter _r_ controls the rate of improvement of antigenic distance. A zero rate _r_ corresponds to the situation in which antibodies do not improve their ability to match antigens. Complete failure to develop antibodies (when _S_(0) = 0 and _r_ = 0) results in recurrence of the disease and transition to a chronic state, as seen Fig. 6(a) and (b). This state is characterized by the following values:
(_V_, _H_, _I_, _M_, _F_, _R_, _E_, _P_, _A_) = (5.26, 0.06, 0.018, 0.05, 1484, 0.89, 67.0). As the immune system produces virus-specific antibodies, the host is able to clear the disease even in the case when the production rate of compatible antibodies is quite low such as _r_ = 10⁻⁵, as seen in Fig. 6(c) and (d). A partial failure to develop antibodies occurs when _S_(0)>0 and _r_ = 0. In that case, if _S_(0) is sufficiently small (below 10⁻⁷), complete failure occurs, with recurrence of the disease and transition to a chronic state (not shown).

<a id='f4b2209d-00a3-4736-8da4-031ce5c003e6'></a>

To obtain further insight into the influence of the
variable S on the behavior of the system we considered the
reduced system of Eqs. (1)-(9) with S treated as a constant,
and studied changes in the location and stability of fixed
points of this reduced system as a function of S. The
corresponding bifurcation diagram, shown in Fig. 7(a) and
(b), reveals that when S<S* = 0.000224555, the high
virulence state x_v is stable while the healthy state is
unstable. (This is compatible with the behavior of the full
system for S = 0 and r = 0 described above.) At S = S*, a
subcritical Hopf bifurcation occurs which gives rise to a
family of unstable periodic orbits. That family continues as
a family of stable limit cycles for values S>S*. (Only a
portion of that branch is shown in Fig. 7 (a); difficulties
with numerical calculation of that branch prevent us from
determining whether the stable limit cycle persists for all
S<= 1.) The healthy steady state x_H is unstable until

<!-- PAGE BREAK -->

<a id='d9d4abb8-7445-44a3-b3ae-866bead4c0e7'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86 83<::chart: A 2x2 grid of four line graphs. The x-axis for all graphs is labeled "Days" and ranges from 0 to 25.

(a) Time-course of viral load (V) for an individual without adaptive immune response. The y-axis is labeled "V" and is on a logarithmic scale from 10⁻⁵ to 10². The curve shows an initial sharp increase in viral load, peaking around day 2, then decreasing, followed by a smaller peak around day 10, and then stabilizing at a moderate level (around 10⁰ to 10¹).

(b) Time-course of the proportion of healthy cells for an individual without adaptive immune response. The y-axis is labeled "Healthy Cells" and ranges from 0.0 to 1.0. The curve shows an initial high proportion of healthy cells, which sharply drops to near zero around day 2, then recovers slightly before dropping again and remaining at a low level (around 0.1) from approximately day 15 onwards.

(c) Time-course of viral load (V) for an individual whose existing antibodies are incompatible but improving. The y-axis is labeled "V" and is on a logarithmic scale from 10⁻⁵ to 10². The curve shows an initial sharp increase in viral load, peaking around day 2, and then rapidly decreasing to below 10⁻⁵ by around day 5, remaining at that low level.

(d) Time-course of the proportion of healthy cells for an individual whose existing antibodies are incompatible but improving. The y-axis is labeled "Healthy Cells" and ranges from 0.0 to 1.0. The curve shows an initial low proportion of healthy cells, which then rapidly increases from around day 5, reaching a high plateau (near 1.0) by approximately day 10 and remaining there.

Fig. 6. Time-courses of (a) the viral load and (b) the proportion of healthy cells for an individual with no initial and no improvement in antibody compatibility, S(0) = 0, r = 0, i.e., an individual without adaptive immune response. Failure to develop compatible antibodies results in recurrence of the disease and transition to a chronic state. Time-courses of (c) the viral load and (d) the proportion of healthy cells in an individual whose existing antibodies are incompatible but improving, i.e., S(0) = 0, r = 10⁻⁵. As virus-specific antibodies appear with the adaptive response, IAV particles are removed from the host completely.::>

<a id='3b9d9363-cce7-45f0-aeb1-66ea1ca2de1c'></a>

S reaches S# = 0.0129294, at which value XH gains stability through a transcritical bifurcation. A branch of unstable threshold steady states Xth bifurcates off of XH and exists for S>S#.

<a id='2e0e7646-4e80-4f23-9f44-a18144f79000'></a>

## 4. Discussion

We presented a simplified model of the human immune
response to the IAV infection in individual hosts which
includes innate and adaptive immunity, and analyzed its
behavior. Such a model could be used to explore in more
detail individual determinants of symptoms and behavior
of clinical relevance, especially in large-scale simulations of
disease spread and containment. Simulation and sensitivity
analysis of this model suggest that for majority of possible
parameter values and initial conditions the course of the
disease falls into one of three categories: asymptomatic
disease, typical disease, and severe disease. In special
circumstances a recurrence of infection may occur,
followed by a transition to either healthy or chronic state.
The magnitude of initial viral load V(0) determines which
of the paths will be taken, in accord with experimental
observations (Tamura and Kurata, 2004). With sufficiently
small viral inoculum, disease is asymptomatic in the sense
that the virus level decreases monotonically to 0 and
damage remains very low. With inocula within the interval
of values corresponding to typical disease, virus shedding,

<a id='eec1483f-ef66-4285-9742-15a3f7aeb1e5'></a>

duration of sickness and the severity of symptoms, as well as the duration of contagious period are independent of size of inoculum; only the time of the onset of disease changes: disease peaks earlier for larger inocula. An important epidemiological implication of this result is that from observations of a typical disease it is impossible to determine a posteriori both when the infection occurred and what was the initial virus load since these data are inter-dependent. When the inoculum is sufficiently large (more than 0.1 particles per epithelial cell in some cases), disease becomes severe with maximum viral load and maximum damage increasing proportionally to the size of the inoculum.

<a id='d08cbd68-328c-4a45-9c59-96a739f6cd69'></a>

Analysis of the adaptive immune response revealed that whenever there is sufficient antibody response with enough specificity, the dynamics will restore health, irrespective of the intensity of the innate responses and of the trajectory followed by the disease. However, if memory cells cannot produce sufficiently compatible antibodies against the IAV particles initially (very low S(0)) or cannot improve the antigenic compatibility sufficiently rapidly (S is not increasing during the disease), there is rebound of virus shedding and transition of the system to a chronic state.

<a id='daa03b89-d7bc-4bac-85af-780ad317d850'></a>

The role of antigenic compatibility in virus clearance can be viewed as a series of transitions in the bifurcation diagram of Fig. 7, once one realizes that S is slowly, but steadily, increasing during the course of the disease in

<!-- PAGE BREAK -->

<a id='3d6de56e-d9e3-490c-8bc3-0b6ef259215a'></a>

84

<a id='087082b5-f806-4e05-9566-9393e083ae3a'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='496732dd-77ad-4d48-a81f-57cd131dc75a'></a>

<::figure: Bifurcation diagram::>
### a
Graph titled 'a' with 'V' on the y-axis (log scale from 10^-4 to 10^2) and 'S' on the x-axis (log scale from 10^-5 to 1). The graph shows a bifurcation curve with stable states (solid black lines) and unstable steady states (dashed red lines). A solid black curve starts at a high V value, goes down, and then forms a loop with a red dashed curve and a red solid curve segment, then continues downwards. A horizontal dashed red line is present across the top portion.

### b
Graph titled 'b' with 'V' on the y-axis (linear scale from -10^-3 to 2x10^-3) and 'S' on the x-axis (log scale from 10^-5 to 1). The graph shows a horizontal solid black line at V=0, representing a stable state. A dashed red curve starts at V=0 and curves upwards as S increases, indicating an unstable steady state.

Fig. 7. Bifurcation diagram for a reduced system of Eqs. (1)–(9) with S treated as a bifurcation parameter. Two separate parts of the diagram are shown: (a) the high virulence steady state and connected branches and (b) the healthy state and connected branches. Stable states are shown as solid black curves, unstable steady states as dashed red curves, unstable periodic orbit as hollow red circles and stable periodic orbit as solid black circles. (The branch of limit cycles is terminated due to difficulties in its numerical calculation, but is expected to persist up to the value S = 1.)
<::/figure::>

<a id='a6955b3c-00a2-4050-9542-94012167cf55'></a>

initially naïve individuals. Near S = 0 the healthy steady state is unstable and the system initially approaches the chronic state. Eventually, S increases beyond S*, the limit of stability of the chronic state, and the system will approach the limit cycle. Eventually, S will increase beyond S#, at which instant the healthy state becomes stable and the immune system clears the infection.

<a id='621b83c5-de6d-458d-8ee8-e53e4bbb2285'></a>

The reduced model underlines the importance of
antigenic distance between the virus strain which causes
IAV infection and the existing virus-specific antibodies of
the adaptive response represented in the model by S
variable. Children who previously experienced natural
infection or who received a live virus vaccine exhibit a
marked reduction in both the amount and duration of virus
shedding when compared to subjects without prior
exposure to IAV infection (Tamura and Kurata, 2004).
Compared with adults, children can shed virus earlier
before illness begins and for longer periods once illness

<a id='95e87c88-0968-4738-b2d4-02359b61d489'></a>

starts. In children absolute levels of virus shedding may be higher than those in adults. These experimental findings confirm our model predictions (see Fig. 5) which take into account the immune memory of the individual providing not only much accurate predictions for the host but also a solid foundation as individual-based model for realistic epidemic models. Our results suggest that in the absence of initial immune memory (low S(0) or S(0) = 0) due to lack of proper vaccination or new subtype of the virus, the individual would experience severe disease which might result in death and remains contagious for a longer period of time. Therefore, such an individual has a larger probability to die and spread the disease in an epidemic.

<a id='f3ee03f1-c2cf-4953-90ad-3a45b2d56626'></a>

Our results illustrate the point that IAV infection caused by high virulent viruses may cause death due to substantial damage, while infection by a virus with low virulence may be cleared without any symptoms: a combination of viral properties and host susceptibility determines the outcome of infection (Price et al., 2000). High virulence corresponds in our model to high values of the parameters γHV and γv which characterizes the rate of infection of epithelial cells by IAV and the rate of IAV particles secretion per infected epithelial cell, respectively. In the three global pandemic of the last century, new subtypes with higher values of γHV and γv arose due to antigenic shift. Since there was no or very little immunity of human population to these new subtypes (0 or very low S(0)) combining with high virulence, they caused excessive mortality rates with large probability of death for particular individuals as our results indicated. Although the H5N1 subtype of avian flu has very limited ability to bridge the species barrier and humans to human has not been observed (Kuiken et al., 2006; Shinya et al., 2006), it might mutate into a form for which it can be transmitted from human to human. Since this new subtype (i.e. very low S(0) for individuals) of the IAV is very virulent (i.e. γHV and γv both high), it would be predicted to cause excessive damage in individuals, conditions conducive to a pandemic. Containment measures should be taken such as antiviral drugs which can neutralize the actions of NA (i.e. decreased γv) and efficient vaccination which can improve host immunity by the existence of very affine subtype-specific antibodies neutralizing the actions of HA (i.e very low S(0) and decreased γHV). Sensitivity analysis of the model suggest that innate response is an early, important line of nonspecific defense which has significant impact on lowering the duration of sickness, virus shedding and tissue damage. Contagious period of an individual which is an important measure for disease control is increased by the higher interferon response. Sensitivity analysis also suggests that higher cellular response result in lower period of symptomatic case and contagious period.

<a id='62725a23-7b78-4b1a-a654-65a3955f98f9'></a>

Although each component of innate and adaptive
immune response contributes to the recovery of IAV
infection, the simulations suggest that, in the absence of
one component of innate immunity, the remaining two
defense mechanisms are sufficient for viral clearance.

<!-- PAGE BREAK -->

<a id='d2d3fea2-22a8-475c-afe4-41fbf9b4e8ea'></a>

B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86

<a id='0310acfa-481d-4b7b-9eb0-adea03e3421f'></a>

85

<a id='1d2faccc-66e7-48b0-9b9d-d96e9a87d797'></a>

For example, when cellular component are not involved in viral clearance, antibodies (sufficient in the amount and affinity) on their own can mediate clearance of influenza (Scherle et al., 1992). The cellular response can also be sufficient to clear the IAV infection from an individual (Asquith and Bangham, 2003). In the absence of adaptive immunity, the viral load is brought down to very low levels, although not completely cleared, which is supported by experiments showing that in some circumstances antibody response is necessary to clear the infection (Iwasaki and Nozima, 1977). For example, in nude mice without antibodies the viral particles survive with chronic infection (see Fig. 6(a)) (Scherle et al., 1992). After transferring T helper cells into the infected mice that promotes antibody response, the disease is completely cleared (Iwasaki and Nozima, 1977; Scherle et al., 1992). Therefore, one can conclude that innate defense mechanisms are not capable of curing the disease on their own in the absence of antibody response, and can only reduce the disease to a chronic state (see Fig. 6(b)). Host may escape from this chronic state with sufficient adaptive response or through sufficient cellular response (Epstein et al., 1998).

<a id='f36eba3c-6235-416f-a560-791d202ac82a'></a>

The biological relevance of our analysis and conclusions are limited by the significant oversimplification present in our reduced model and the difficulty in translating functions such as "antigen presenting cells", "damage", "effector cells" into measurable quantities as we have done in more specific models (Chow et al., 2005). Our model does not permit the derivation of the number of new cases per infected cases, or R₀. Yet, inscribed in a simulation furnishing distributions of viral loads/contact and contact density, such a number could be derived. Future development of the biological model include detailed mathematical analysis of the system of equations of the model, correlating infectivity and classes of symptoms to specific components of the model such as viral load, interferon levels and proportion of unhealthy respiratory epithelial cells, and improved biological fidelity and calibration data. We wish to include the effects of age and genetic variations through realistic distributions of key model parameters. Such an extension will be used to conduct large scale simulations of clinical trials of antiviral strategies in genetically heterogeneous hosts and to construct response surfaces to be integrated in multi-scale models of IAV infection (Clermont et al., 2004). We also wish to develop a more sophisticated model of antigenic distance.

<a id='f199b9f5-69f4-4cf8-8686-7aaf7116e7c3'></a>

### Acknowledgments

This work is supported under grant NIH R01-GM67240 (Clermont). We are grateful to Dr. Ted Ross for critical comments on the manuscript.

<a id='92e39c1f-6d34-4f62-85a1-f4b874b75513'></a>

References
Ada, G.L., Jones, P.D., 1986. The immune response to influenza infection.
Curr. Top. Microbiol. Immunol. 128, 1–54.

<a id='0e063cfd-1dfd-4696-b09e-d64ad8c8c8da'></a>

Akira, S., Takeda, K., Kaisho, T., 2001. Toll-like receptors: critical proteins linking innate and acquired immunity. Nat. Immunol. 2, 675-680.
Asquith, B., Bangham, C.R., 2003. An introduction to lymphocyte and viral dynamics: the power and limitations of mathematical analysis. Proc. Biol. Sci. 270, 1651-1657.
Bocharov, G.A., Romanyukha, A.A., 1994. Mathematical model of antiviral immune response. III. Influenza A virus infection. J. Theor. Biol. 167, 323-360.
Chow, C.C., Clermont, G., Kumar, R., Lagoa, C., Tawadrous, Z., Gallo, D., Betten, B., Bartels, J., Constantine, G., Fink, M.P., Billiar, T.R., Vodovotz, Y., 2005. The acute inflammatory response in diverse shock states. Shock 24, 74-84.
Clermont, G., Bartels, J., Kumar, R., Constantine, G., Vodovotz, Y., Chow, C., 2004. In silico design of clinical trials: a method coming of age. Crit. Care Med. 32, 2061-2070.
Couch, R.B., Kasel, J.A., 1983. Immunity to influenza in man. Annu. Rev. Microbiol. 37, 529-549.
Epstein, S.L., Lo, C.Y., Misplon, J.A., Bennink, J.R., 1998. Mechanism of protective immunity against influenza virus infection in mice without antibodies. J. Immunol. 160, 322-327.
Hayden, F.G., Fritz, R., Lobo, M.C., Alvord, W., Strober, W., Straus, S.E., 1998. Local and systemic cytokine responses during experimental human influenza A virus infection. Relation to symptom formation and host defense. J. Clin. Invest. 101, 643-649.
Iwasaki, T., Nozima, T., 1977. Defense mechanisms against primary influenza virus infection in mice. I. The roles of interferon and neutralizing antibodies and thymus dependence of interferon and antibody production. J. Immunol. 118, 256-263.
Johansson, B.E., Bucher, D.J., Kilbourne, E.D., 1989. Purified influenza virus hemagglutinin and neuraminidase are equivalent in stimulation of antibody response but induce contrasting types of immunity to infection. J. Virol. 63, 1239-1246.
Joklik, W.K., 1985. Interferons. In: Fields, B.N., Knipe, R.M., Melnick, J.L., Chanok, M.S., Riozman, B., Shope, R.E. (Eds.), Virology. Raven Press, New York, pp. 281-307.
Julkunen, I., Melen, K., Nyqvist, M., Pirhonen, J., Sareneva, T., Matikainen, S., 2000. Inflammatory responses in influenza A virus infection. Vaccine 19 (Suppl. 1), S32-S37.
Keenan, K.P., Combs, J.W., McDowell, E.M., 1982. Regeneration of hamster tracheal epithelium after mechanical injury. I. Focal lesions: quantitative morphologic study of cell proliferation. Virchows Arch. B Cell Pathol. Incl. Mol. Pathol. 41, 193-214.
Kuiken, T., Holmes, E.C., McCauley, J., Rimmelzwaan, G.F., Williams, C.S., Grenfell, B.T., 2006. Host species barriers to influenza virus infections. Science 312, 394-397.
Lamb, R.K.R., 1996. Orthomyxoviridae: The Viruses and their Replica- tion. Lippincott-Raven Publishers, Philadelphia, pp. 1353-1396.
Liew, F.Y., Russell, S.M., Appleyard, G., Brand, C.M., Beale, J., 1984. Cross-protection in mice infected with influenza virus by the respiratory route is correlated with local IgA antibody rather than serum antibody or cytotoxic T cell reactivity. Eur. J. Immunol. 14, 350-356.
Marchuk, G.I., Berbentsova, E.P., 1986. [Results using a quantitative method for evaluating the severity and dynamics of acute pneumonia, chronic bronchitis and bronchial asthma]. Ter. Arkh. 58, 63-70.
Marchuk, G.I., Petrov, R.V., Romanyukha, A.A., Bocharov, G.A., 1991. Mathematical model of antiviral immune response. I. Data analysis, generalized picture construction and parameters evaluation for hepatitis B. J. Theor. Biol. 151, 1-40.
Meltzer, M.I., Cox, N.J., Fukuda, K., 1999. The economic impact of pandemic influenza in the United States: priorities for intervention. Emerg. Infect. Dis. 5, 659-671.
Mohler, L., Flockerzi, D., Sann, H., Reichl, U., 2005. Mathematical model of influenza A virus production in large-scale microcarrier culture. Biotechnol. Bioeng. 90, 46-58.
Murphy, B.R., Clements, M.L., 1989. The systemic and mucosal immune response of humans to influenza A virus. Curr. Top. Microbiol. Immunol. 146, 107-116.

<!-- PAGE BREAK -->

<a id='140220eb-33b5-4517-b90a-f5c4e0f030cd'></a>

86

<a id='fa6ee843-5ff8-4e50-9c4f-60ad80f53ba2'></a>

_B. Hancioglu et al. / Journal of Theoretical Biology 246 (2007) 70–86_

<a id='190fce93-e98b-49a4-8842-60aef96c2f6c'></a>

Neumann, A.U., Lam, N.P., Dahari, H., Gretch, D.R., Wiley, T.E., Layden, T.J., Perelson, A.S., 1998. Hepatitis C viral dynamics in vivo and the antiviral efficacy of interferon-alpha therapy. Science 282, 103-107.

Nguyen, H.H., Boyaka, P.N., Moldoveanu, Z., Novak, M.J., Kiyono, H., McGhee, J.R., Mestecky, J., 1998. Influenza virus-infected epithelial cells present viral antigens to antigen-specific CD8+ cytotoxic T lymphocytes. J. Virol. 72, 4534-4536.

Nicholson, K.G., Webster, A.G., Hay, A.J., 1998. Textbook of Influenza. Blackwell Science, Oxford.

Nowak, M.A., Bangham, C.R., 1996. Population dynamics of immune responses to persistent viruses. Science 272, 74-79.

Nowak, M.A., May, R., 2000. Virus Dynamics: The Mathematical Foundations of Immunology and Virology. Oxford University Press, Oxford.

Perelson, A.S., 2002. Modelling viral and immune system dynamics. Nat. Rev. Immunol. 2, 28-36.

Perelson, A.S., Kirschner, D.E., De, B.R., 1993. Dynamics of HIV infection of CD4+ T cells. Math. Biosci. 114, 81-125.

Perelson, A.S., Neumann, A.U., Markowitz, M., Leonard, J.M., Ho, D.D., 1996. HIV-1 dynamics in vivo: virion clearance rate, infected cell life-span, and viral generation time. Science 271, 1582-1586.

Price, G.E., Gaszewska-Mastarlarz, A., Moskophidis, D., 2000. The role of alpha/beta and gamma interferons in development of immunity to influenza A virus in mice. J. Virol. 74, 3996-4003.

Ronni, T., Sareneva, T., Pirhonen, J., Julkunen, I., 1995. Activation of IFN-alpha, IFN-gamma, MxA, and IFN regulatory factor 1 genes in influenza A virus-infected human peripheral blood mononuclear cells. J. Immunol. 154, 2764-2774.

Sareneva, T., Matikainen, S., Kurimoto, M., Julkunen, I., 1998. Influenza A virus-induced IFN-alpha/beta and IL-18 synergistically enhance IFN-gamma gene expression in human T cells. J. Immunol. 160, 6032-6038.

Scherle, P.A., Palladino, G., Gerhard, W., 1992. Mice can recover from pulmonary influenza virus infection in the absence of class I-restricted cytotoxic T cells. J. Immunol. 148, 212-217.

Shinya, K., Ebina, M., Yamada, S., Ono, M., Kasai, N., Kawaoka, Y., 2006. Avian flu: influenza virus receptors in the human airway. Nature 440, 435-436.

<a id='92e5448e-06a7-41bd-9409-912e51bd649d'></a>

Smith, D.J., Forrest, S., Ackley, D.H., Perelson, A.S., 1999. Variable efficacy of repeated annual influenza vaccination. Proc. Natl. Acad. Sci. USA 96, 14001–14006.

Stark, G.R., Kerr, I.M., Williams, B.R., Silverman, R.H., Schreiber, R.D., 1998. How cells respond to interferons. Annu. Rev. Biochem. 67, 227–264.

Tamura, S., Kurata, T., 2004. Defense mechanisms against influenza virus infection in the respiratory tract mucosa. Jpn. J. Infect. Dis. 57, 236–247.

Tamura, S., Iwasaki, T., Thompson, A.H., Asanuma, H., Chen, Z., Suzuki, Y., Aizawa, C., Kurata, T., 1998. Antibody-forming cells in the nasal-associated lymphoid tissue during primary influenza virus infection. J. Gen. Virol. 79 (Pt 2), 291–299.

Tamura, S., Tanimoto, T., Kurata, T., 2005. Mechanisms of broad cross- protection provided by influenza virus infection and their application to vaccines. Jpn. J. Infect. Dis. 58, 195–207.

Taubenberger, J.K., Morens, D.M., 2006. 1918 Influenza: the mother of all pandemics. Emerg. Infect. Dis. 12, 15–22.

Tulp, A., Verwoerd, D., Dobberstein, B., Ploegh, H.L., Pieters, J., 1994. Isolation and characterization of the intracellular MHC class II compartment. Nature 369, 120–126.

Webster, R.G., Peiris, M., Chen, H., Guan, Y., 2006. H5N1 outbreaks and enzootic influenza. Emerg. Infect. Dis. 12, 3–8.

Wohlfart, C., 1988. Neutralization of adenoviruses: kinetics, stoichiome- try, and mechanisms. J. Virol. 62, 2321–2328.

Wyde, P.R., Wilson, M.R., Cate, T.R., 1982. Interferon production by leukocytes infiltrating the lungs of mice during primary influenza virus infection. Infect. Immun. 38, 1249–1255.

Yetter, R.A., Lehrer, S., Ramphal, R., Small Jr., P.A., 1980. Outcome of influenza infection: effect of site of initial infection and heterotypic immunity. Infect. Immun. 29, 654–662.

Yewdell, J.W., Bennink, J.R., Smith, G.L., Moss, B., 1985. Influenza A virus nucleoprotein is a major target antigen for cross-reactive anti- influenza A virus cytotoxic T lymphocytes. Proc. Natl. Acad. Sci. USA 82, 1785–1789.

Yoshikawa, T., Matsuo, K., Matsuo, K., Suzuki, Y., Nomoto, A., Tamura, S., Kurata, T., Sata, T., 2004. Total viral genome copies and virus-Ig complexes after infection with influenza virus in the nasal secretions of immunized mice. J. Gen. Virol. 85, 2339–2346.

Zdanov, V.M., Bukrinskaja, A.G., 1969. Myxoviruses Reproduction. Medicina, Moscow, Russia.
<a id='9de3254f-29a1-48f0-98bc-3a32dd53052c'></a>

<::logo: Elsevier
ELSEVIER
This logo features a detailed black and white illustration of a tree with two figures beneath it, and a snake wrapped around the tree, with the company name in black capital letters below the illustration::>

<a id='645dd825-653b-457b-9fd1-a4e76bef3e88'></a>

Available online at www.sciencedirect.com

SCIENCE @ DIRECT®

<a id='dbf5febe-566f-41f7-aa94-892d5f5dad16'></a>

<::logo: [Mathematical Biosciences]
Mathematical Biosciences
The logo features the words "Mathematical Biosciences" in an italicized sans-serif font, with two horizontal lines above them.::>

<a id='f2c2f092-91d9-45fc-a6e5-bf8892cc3e50'></a>

Mathematical Biosciences 185 (2003) 191–203

<a id='cd1b65cc-90ad-4770-82b0-fa25e8a0d320'></a>

www.elsevier.com/locate/mbs

<a id='db3e429e-c81a-41df-9742-886c4182ca09'></a>

Fighting a virus with a virus: a dynamic model for HIV-1 therapy

<a id='924e4480-7795-4365-b69d-497ca2f7b482'></a>

Tomás Revilla ⁱ, Gisela García-Ramos ⁱ,*

ⁱ _Instituto de Zoología Tropical, Universidad Central de Venezuela, Apdo. Postal 47058, Caracas 1041-A, Venezuela_
ⁱ _Department of Biology, University of Kentucky, 101 Morgan Building, Lexington, KY 40506-0225, USA_

Received 26 September 2002; received in revised form 14 May 2003; accepted 18 June 2003

<a id='c05795aa-ac49-4709-a216-61d25da11a1b'></a>

Abstract
A mathematical model examined a potential therapy for controlling viral infections using genetically modified viruses. The control of the infection is an indirect effect of the selective elimination by an engineered virus of infected cells that are the source of the pathogens. Therefore, this engineered virus could greatly compensate for a dysfunctional immune system compromised by AIDS. In vitro studies using engineered viruses have been shown to decrease the HIV-1 load about 1000-fold. However, the efficacy of this potential treatment for reducing the viral load in AIDS patients is unknown. The present model studied the interactions among the HIV-1 virus, its main host cell (activated CD4+ T cells), and a therapeutic engineered virus in an in vivo context; and it examined the conditions for controlling the pathogen. This model predicted a significant drop in the HIV-1 load, but the treatment does not eradicate HIV. A basic estimation using a currently engineered virus indicated an HIV-1 load reduction of 92% and a recovery of host cells to 17% of their normal level. Greater success (98% HIV reduction, 44% host cells recovery) is expected as more competent engineered viruses are designed. These results suggest that therapy using viruses could be an alternative to extend the survival of AIDS patients.
© 2003 Elsevier Inc. All rights reserved.

<a id='45108d28-858b-49d8-b9cd-e21e27af0290'></a>

Keywords: HIV-1 therapy; Viral therapy; HIV-1 dynamics; Engineered virus; Hunter-virus

<a id='f595a6d8-7c02-4c02-b60a-c8cc5ef0c01d'></a>

1. Introduction
Current therapies for acquired immunodeficiency syndrome (AIDS) employ inhibitors of the
enzymes required for replication of human immunodeficiency virus (HIV-1) to reduce the HIV-1

<a id='34086902-e7f2-4c72-86c1-ba2398e267c4'></a>

* Corresponding author. Tel.: +1-859 257 1996; fax: +1-859 257 1717. E-mail address: ggarc0@uky.edu (G. García-Ramos).

<a id='90763c85-556b-4724-a6f6-0ae1dde01aa0'></a>

0025-5564/$ - see front matter  2003 Elsevier Inc. All rights reserved.
doi:10.1016/S0025-5564(03)00091-9

<!-- PAGE BREAK -->

<a id='2f98b7f4-1a6f-4578-a00a-caf1c791bab4'></a>

192
T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191–203

<a id='aad44ed2-9220-4705-af78-3ae41b0e78c9'></a>

load [1,2]. Genetic engineering offers an alternative approach, featuring modification of a viral genome to produce recombinants capable of controlling infections by other viruses [3,4]. This method has been used to modify rhabdoviruses, including the rabies [5] and the vesicular stomatities viruses (VSV) [6], making them capable of infecting and killing cells previously attacked by HIV-1. The engineered virus codifies the coreceptor pair CD4 and CXCR4 of the host cell membrane and bind specifically to the protein complex gp120/41 of HIV-1 expressed on the surface of infected cells [6]. The engineered virus causes a rapid cytopathic infection. This destruction of infected cells decreased by about 1000-fold HIV-1 load [6]. Since these experiments were conducted in vitro the potential effectiveness of this treatment for reducing the viral load of AIDS patients is unknown. In the present study, we modeled the interactions among HIV-1, its main host cell and an engineered virus in an in vivo context, in order to predict the dynamics of the system and evaluate the potential efficacy of this approach to treatment. Results from the present study demonstrated that this treatment could be effective in reducing individual HIV-1 load.

<a id='62f1e4dd-1c4c-45a0-b542-a1768805bf7d'></a>

## 2. Model

Viruses depend on host cells to reproduce. HIV-1 infects many types of cells such as dendritic cells and macrophages, but it preferentially replicates (>90%) in some of the lymphocytes, the activated CD4+ T cells [1,7,8]. The model considered only the main host cell for HIV-1, namely the activated CD4+ T cell. The analysis was based on a simple model of viral dynamics [9], using the following variables: the number of normal or virus-free host cells x, infected cells y, and a pathogen virus v that represents HIV-1. Normal cells are produced at a constant rate λ, and die at rate dx (Fig. 1). The infection rate is equal to βxv, and infected cells die at a rate ay, releasing pathogens at a rate ky, but pathogens are removed from the plasma at rate uv. The resulting differential equations are:

<a id='6ec4bb1f-0838-47ee-bf39-12cae620acfc'></a>

<::Figure 1: Diagram showing a model for a double viral infection. Three main states are represented by circles: X (normal cell, speckled pattern), Y (single-infected cell, speckled with a solid black circle inside), and Z (double-infected cell, speckled with two solid black circles inside). Arrows indicate transitions between states and production/consumption of viral particles.

- Normal cell (X) has an incoming arrow labeled `λ` and an outgoing arrow labeled `dx`.
- Pathogen virus (V, solid black circle) is produced from single-infected cells (Y) via an arrow labeled `ky` and infects normal cells (X) via a jagged arrow labeled `βxv` to produce single-infected cells (Y). It also has an outgoing arrow labeled `uv`.
- Single-infected cell (Y) is formed from normal cell (X) and pathogen virus (V). It has an outgoing arrow labeled `ay`.
- Recombinant virus (W, solid black circle with an 'X' or cross inside) is produced from double-infected cells (Z) via an arrow labeled `cz` and infects single-infected cells (Y) via a jagged arrow labeled `αwy` to produce double-infected cells (Z). It also has an outgoing arrow labeled `qw`.
- Double-infected cell (Z) is formed from single-infected cell (Y) and recombinant virus (W). It has an outgoing arrow labeled `bz`.

Legend:
X: normal cell
Y: single-infected cell
Z: double-infected cell
V: pathogen virus
W: recombinant virus

Fig. 1. Model for a double viral infection. Pathogen viral particles v infect normal cells x, producing single-infected cells y; these are the target of a new infection by the recombinant virus w that converts them in double-infected cells z. Double-infected cells are able to produce recombinants but no pathogens. Definitions of parameters are in Table 1.::>

<!-- PAGE BREAK -->

<a id='09e0ec74-f7b7-4a81-a75f-4d55fea0bb6a'></a>

T. Revilla, G. García-Ramos / Mathematical Biosciences 185 (2003) 191–203

193

<a id='7c990654-44f0-4b52-8c07-3df0c8436fbe'></a>

$\dot{x} = \lambda - dx - \beta xv$,
$\dot{y} = \beta xv - ay$,
$\dot{v} = ky - uv$. (1)

<a id='b7fe2fa1-67be-45dd-9e5f-cb877b447003'></a>

We then added a second virus, the recombinant (genetically modified) virus, whose density is _w_.
The recombinant infects cells previously infected by the pathogen, turning them at a rate _awy_ into
double-infected cells, whose density is _z_. Recombinants are removed at rate _qw_. The double-
infected cells die at rate _bz_ and release recombinants at rate _cz_. The equations for the full system
are:

<a id='c871b052-0d8f-4ef7-8caf-52d25fca63b8'></a>

ẋ = λ - dx - βxv,
ẏ = βxv - ay - αwy,
ż = αwy - bz,
v̇ = ky - uv,
ẇ = cz - qw.

(2)

<a id='93ff4b58-e69a-4a6b-b7db-59de0398aef6'></a>

### 3. Analytical results

The model has three steady states as shown below:

(a) Equilibrium with an absence of viruses:

$(\hat{x}_1, \hat{y}_1, \hat{z}_1, \hat{v}_1, \hat{w}_1) = (\lambda/d, 0, 0, 0, 0).$ (3)

(b) Equilibrium with the pathogen:

$(\hat{x}_2, \hat{y}_2, \hat{z}_2, \hat{v}_2, \hat{w}_2) = \left(\frac{au}{\beta k}, \frac{\lambda}{a} - \frac{du}{\beta k}, 0, \frac{\lambda k}{au} - \frac{d}{\beta}, 0\right).$ (4)

<a id='03078ecb-e818-41cc-bd67-b08d68e6822d'></a>

(c) Equilibrium with both viruses:

$\hat{x}_3 = \lambda/(d + \beta bkq/(\alpha cu))$,

$\hat{y}_3 = bq/(\alpha c)$,

$\hat{z}_3 = (q/c)\hat{w}_3$,

$\hat{v}_3 = bkq/(\alpha cu)$,

$\hat{w}_3 = (\alpha \beta \lambda ck - \beta abkq - \alpha acdu)/(\alpha(\beta bkq + \alpha cdu))$. (5)

<a id='9369b08a-c66a-4dd6-a803-d5bf57584325'></a>

The steady state with the pathogen present (Eq. (4)) is possible when the equilibrium density of the pathogen is greater than zero ($v_2$ > 0), and this leads to a condition for invasion of the pathogen: $R_v = \beta\lambda k/adu$ > 1 [9]. This describes the ratio of growth and death rates for the pathogen pathway (Fig. 1). For the third equilibrium to exist (Eq. (5)), the density of the recombinant virus must be greater than zero ($w_3$ > 0), and this leads to the condition $R_w$:

<!-- PAGE BREAK -->

<a id='af25621b-f3f8-4d22-88a3-88a56756ac82'></a>

194

<a id='44fd722e-baf8-4db8-a65c-8da58b9c9703'></a>

T. Revilla, G. García-Ramos / Mathematical Biosciences 185 (2003) 191–203

<a id='d1f9f554-786e-4acc-bf96-d323bc88c3a1'></a>

R_w = (αλc/abq)(R_v - 1)/R_v > 1.

<a id='c0a08f91-a973-42b5-9418-eb719b58f0f7'></a>

(6)

<a id='e2c0b561-9de1-4ebb-a335-1f8e29916b4e'></a>

R_w depends on the product of the growth-rates-to-death-rates ratio and the net growth of the pathogen, (R_v - 1)/R_v. Appendix A shows that R_w describes the condition for invasion of the recombinant by accounting for the number of secondary infections produced by one cell infected with the recombinant. So if R_w is larger than 1 indicates that at the start of the infection each recombinant-infected cell produces more than one newly recombinant-infected cell, resulting in an increase in this cell population.

<a id='7a7284e6-3acb-4395-92c8-c9d6cfd28c9b'></a>

Thus the infection with the pathogen progresses when R_v > 1, leading to a steady state (Eq. (4)). In this situation, the normal host cell density x decreases in favor of the infected population y, and the level of pathogens v is very high. The immune system response may decrease viral density by direct attack or through infected cells. However, this response appears some weeks to months after infection and would presumably only be temporary since the immune system is severely compromised at later stages of the disease [10], and therefore, is ignored here. This model better describes the initial and latest stage of HIV-1 infection (see [9,11] for an immune model for a

<a id='515da1a4-19c0-46f3-8ed9-214239f4aa38'></a>

Table 1<br>Interpretation and value of the parameters<br><table><thead><tr><th>Parameter</th><th>Definition</th><th>Value (day⁻¹)</th><th>Comments</th></tr></thead><tbody><tr><td>d</td><td>Death rate of host cellª</td><td>0.01</td><td>Average life span of CD4+T cell is two years, so<br>d = 0.0014 [28]. From modeling, d = 0.01 [19].</td></tr><tr><td>λ</td><td>Production rate of host cell</td><td>2 cell/mm³</td><td>Density of total CD4+ T cell in the blood in healthy<br>human is X' = 1000 cell/mm³ [12]. Assumed equi-<br>librium, their production λ' equal loss<br>λ' = X'd = 10. Assumed that a fraction τ = 0.2 of<br>new generated cells are activated λ = λ'τ = 2 [12].</td></tr><tr><td>β</td><td>Infection rate of host cell by<br>HIV-1</td><td>0.004 mm³/vir</td><td>Estimated indirectly as a small value that preserves<br>both infections. For single infection β = 0.00027<br>[12], β = 0.00065 [19], β = 0.0035 [29], upper bound<br>β = 0.007 [30].</td></tr><tr><td>a</td><td>Death rate of HIV-1 infected<br>cell</td><td>0.33</td><td>Based on life span of HIV-1 infected cells of three<br>days [12]. Other estimates: a = 0.49 [18], a = 0.39<br>[19].</td></tr><tr><td>α</td><td>Infection rate by recombinant</td><td>0.004 mm³/vir</td><td>Estimated indirectly as a small value that preserves<br>the double infection. Assumed identical to β.</td></tr><tr><td>b</td><td>Death rate of double-infected<br>cell</td><td>2</td><td>Based on observations of virus release within 8 h of<br>infection before lysis [6].</td></tr><tr><td>k</td><td>HIV-1 production rate by a<br>cell</td><td>50 vir/cell</td><td>k = n₁a. n₁ is total number of infectious HIV-1<br>produced by a cell: n₁ ~ 140 [31], n₁ = 180 [1].</td></tr><tr><td>u</td><td>Removal rate of HIV-1</td><td>2</td><td>Based on life span of 1/2 day [12]. Another value,<br>u = 3 [18,19].</td></tr><tr><td>c</td><td>Production rate of recombi-<br>nant by a double-infected cell</td><td>2000 vir/cell</td><td>c = n₂b. n₂ is total number of infectious re-combi-<br>nant produced by a double-infected cell. In vitro<br>total number of recombinants per cell is ~3333 [6].<br>Assumed n₂ = 1000.</td></tr><tr><td>q</td><td>Removal rate of recombinant</td><td>2</td><td>Assumed identical to u.</td></tr></tbody></table>ª Host cells refer to activated CD4+ T cells.

<!-- PAGE BREAK -->

<a id='33493a84-b0b0-4aaf-8b95-640e2bdc3e16'></a>

T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191-203

<a id='dd36dc45-5356-41be-af94-6eeb3087a08c'></a>

195

<a id='aa80435d-2c0d-41c8-8831-918797541a8c'></a>

single virus; Eq. (1) describes a target-cell limited model where the sharp declines in virus load following infection results by limitation in target cells and does not involve an immune response [9,12]). For the recombinant infection to succeed, it is necessary that R_w > 1, leading to the equilibrium in Eq. (5). The stability of this equilibrium is described in the following section. Notice that host cells are generated in the presence of pathogens, thus it was assumed that at the time of infection a proportion p = τ of the existing CD4+ T cells were activated [12]. It results in a host cell density at infection equal to its equilibrium value without viruses x̂_1 (Eq. (3), Table 1 for λ).

<a id='b016c385-9465-4820-bce4-a898d33b728a'></a>

## 4. Numerical results

The temporal dynamics of the model was extensively studied by numerical simulations using a routine for stiff ordinary differential equations from the software MATLAB 6. The model was evaluated for the HIV-1 and the VSV-recombinant infections; and most of the values for the parameters were based on the literature (Table 1). In the absence of data, infection and removal rates for the recombinant (a, q) were assumed identical to their equivalents in the pathogen. β was set small enough to allow for the development of both infections. The parameters b and c were set to magnitudes estimated under in vitro conditions.

<a id='771173c0-d229-452f-aefc-97d028ed7b3a'></a>

Fig. 2(a) shows the results for a single infection with the pathogen. The population of the pathogen rapidly increased showing a peak towards the end of the first week and stabilizing within four weeks after infection. Simultaneously, the host cells were severely depleted by the infection, stabilizing around two orders of magnitude lower than their initial level. These patterns are comparable to previous results [9,12]. Timing and size of pathogen peak depended on initial conditions for host cell number and pathogen load. Broad variation for initial pathogen load (10⁻⁶–10² vir/mm³) only moved by a few days the peak timing, but varying initial cell number from 200 to 10 cell/mm³ delayed by two weeks the peak and decreased 5.5-fold its size. The small value of 10 for the number of initial host cells corresponds to average values in healthy individuals [13]. The larger value follows Ref. [12] and was chosen on the basis that HIV-1 increase T cell activation. The initial condition does not change the equilibrium. Fig. 2(b) shows the full model with the double infection. In addition to the dynamics of the pathogen infection, the recombinant virus generates double-infected cells. A few days after the recombinant infection, the pathogen load decayed by 12-fold and then generated damped oscillations around the equilibrium. At the same time, the normal cells increased by one order of magnitude during the first week, and sta- bilized slowly to equilibrium. The normal cell trajectory oscillated slightly toward its equilibrium, in comparison to the major fluctuations of other elements of the system. Fig. 2(c) also shows the infection with both viruses, but it simulates a higher infection rate for the recombinant. This higher infection rate significantly increased the normal cells and decreased the pathogen, stabi- lizing the system more rapidly. The recovery of normal cells for the double infection using the default values was to 17% of the density in individuals without pathogen (x₃ = 33 cell/mm³ re- specting x₁ = 200 cell/mm³, Fig. 2(b)). However, when the recombinant infection rate exceeded that of the pathogen, such as α = 4β (Fig. 2(c)), the recovery of normal cells increased up to 44% (x₃ = 89 cell/mm³).

<!-- PAGE BREAK -->

<a id='cf72aaeb-9816-4383-a681-07a2d3f71448'></a>

196
T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191-203

<::
chart: Fig. 2. Simulations.

Three line graphs are presented, each showing Density (counts/mm³) on the y-axis (log scale from 0.1 to 1000) versus Days from infection on the x-axis (0 to 90).

(a) The single-infection system.
  - A graph with three lines:
    - "pathogen virus v" (thick solid line)
    - "single-infected cell y" (dotted line)
    - "normal cell x" (thin solid line)

(b) System with the double infection, and with equal rates of infection for both viruses (α = β).
  - A graph with five lines:
    - "recombinant virus w" (wavy solid line)
    - "normal cell x" (thick solid line)
    - "pathogen virus v" (wavy solid line, thinner than recombinant virus w)
    - "single-infected cell y" (dotted line)
    - "double-infected cell z" (dashed line)

(c) Alternative system with the double infection with c = 2000, but α = 4β.
  - A graph with five lines:
    - "recombinant virus w" (wavy solid line)
    - "normal cell x" (thick solid line)
    - "pathogen virus v" (wavy solid line, thinner than recombinant virus w)
    - "single-infected cell y" (dotted line)
    - "double-infected cell z" (dashed line)

Fig. 2. Simulations. (a) The single-infection system. A pathogen virus v infects a host cell x, generating single-infected cell y. Initial condition for the host cells was x(0) = 200, and the pathogen invaded with v(0) = 10⁻⁶ (a few hundred viruses in the whole body). Quantities corresponded to 1 mm³ in the peripheral blood. The values of the parameters were from Table 1. (b) System with the double infection, and with equal rates of infection for both viruses (α = β). In addition to the pathogen infection, a recombinant virus w infects a single-infected cell y, generating a double-infected cell z. Equilibrium densities from (a) were the initial conditions [x(0) = 3, y(0) = 6, v(0) = 149], and the recombinant invades with w(0) = 1. The production rate of recombinants was c = 2000. (c) Alternative system with the double infection with c = 2000, but α = 4β.
::>


<a id='051451f4-e908-48d6-86f6-3bbdc2716e3b'></a>

The equilibrium for the system using the default values exhibited negative eigenvalues, indicating that it was locally stable to small perturbations. These eigenvalues were obtained using the software *Mathematica*. Since we are interested in understanding global stability, we performed numerous simulations to infer the macrostability of the equilibrium. The simulations considered different initial conditions for the invasion of the recombinant ranging from w(0) = 10^-6^-100 counts/mm^3^. All initial conditions in this range converged to the same equilibrium, suggesting that it was globally stable. Further, the trajectories to the equilibrium from different initial conditions converged rapidly a few days after infection. These results suggest that all doses of the recombinant at the time of the treatment may have the same effect in controlling the pathogen.

<a id='d6239546-d6db-4500-a126-e26b99952e65'></a>

Since most parameter values can only be roughly estimated, we evaluated the model's sensi- tivity to changes in these magnitudes (Table 2, rows 1-26). Most of the new values result from multiplying and dividing the default magnitude by 2, and may represent extreme values. The equilibrium densities (Table 2, columns 3-6) were obtained from Eqs. (3)-(5). For comparison the

<!-- PAGE BREAK -->

<a id='18c6d637-0cbc-4113-9513-905813f4e474'></a>

T. Revilla, G. García-Ramos / Mathematical Biosciences 185 (2003) 191-203

<a id='6c9a8d89-af39-4417-989f-01a7cbd691ea'></a>

197

<a id='fb74ee70-a926-4071-93a5-f0c7ae9e67a8'></a>

Table 2
Effect of parameter values on the density of normal cell $x_i$ pathogen $v_i$ and on the stability of the system
<table id="6-1">
<tr><td id="6-2">Row</td><td id="6-3">Parameter values</td><td id="6-4">x₂ (%x₁)</td><td id="6-5">x₃ (%x₁)</td><td id="6-6">v₂</td><td id="6-7">v̂₃ (%v̂₂)</td><td id="6-8" colspan="2">Oscillations (t = 200)</td></tr>
<tr><td id="6-9"></td><td id="6-a"></td><td id="6-b"></td><td id="6-c"></td><td id="6-d"></td><td id="6-e"></td><td id="6-f">x₃</td><td id="6-g">v₃</td></tr>
<tr><td id="6-h">1</td><td id="6-i">Default (Table 1)</td><td id="6-j">3 (2)</td><td id="6-k">33 (17)</td><td id="6-l">149</td><td id="6-m">12 (8)</td><td id="6-n">–</td><td id="6-o">12 ± 1</td></tr>
<tr><td id="6-p">2</td><td id="6-q">λ = 1.0, d = 0.005</td><td id="6-r">3 (2)</td><td id="6-s">18 (9)</td><td id="6-t">74</td><td id="6-u">12 (17)</td><td id="6-v">15 ± 1</td><td id="6-w">23 ± 20</td></tr>
<tr><td id="6-x">3*</td><td id="6-y">λ = 4.0, d = 0.02</td><td id="6-z">3 (2)</td><td id="6-A">57 (29)</td><td id="6-B">298</td><td id="6-C">12 (4)</td><td id="6-D">–</td><td id="6-E">–</td></tr>
<tr><td id="6-F">4</td><td id="6-G">λ = 1.0</td><td id="6-H">3 (3)</td><td id="6-I">17 (17)</td><td id="6-J">73</td><td id="6-K">12 (17)</td><td id="6-L">13±1</td><td id="6-M">24±21</td></tr>
<tr><td id="6-N">5*</td><td id="6-O">λ = 4.0</td><td id="6-P">3 (1)</td><td id="6-Q">66 (17)</td><td id="6-R">300</td><td id="6-S">12 (4)</td><td id="6-T">–</td><td id="6-U">–</td></tr>
<tr><td id="6-V">6</td><td id="6-W">d = 0.005</td><td id="6-X">3 (1)</td><td id="6-Y">36 (9)</td><td id="6-Z">150</td><td id="6-10">12 (8)</td><td id="6-11">–</td><td id="6-12">12±1</td></tr>
<tr><td id="6-13">7</td><td id="6-14">d = 0.02</td><td id="6-15">3 (3)</td><td id="6-16">29 (29)</td><td id="6-17">147</td><td id="6-18">12 (9)</td><td id="6-19">28</td><td id="6-1a">12±4</td></tr>
<tr><td id="6-1b">8</td><td id="6-1c">β = 0.002, α = β</td><td id="6-1d">7 (3)</td><td id="6-1e">33 (17)</td><td id="6-1f">146</td><td id="6-1g">25 (17)</td><td id="6-1h">27±3</td><td id="6-1i">50±45</td></tr>
<tr><td id="6-1j">9</td><td id="6-1k">β = 0.008, α = β</td><td id="6-1l">2 (1)</td><td id="6-1m">33 (17)</td><td id="6-1n">150</td><td id="6-1o">6 (4)</td><td id="6-1p">–</td><td id="6-1q">–</td></tr>
<tr><td id="6-1r">10*</td><td id="6-1s">β = 0.002, α = 4β</td><td id="6-1t">7 (3)</td><td id="6-1u">89 (44)</td><td id="6-1v">150</td><td id="6-1w">6 (4)</td><td id="6-1x">–</td><td id="6-1y">–</td></tr>
<tr><td id="6-1z">11*</td><td id="6-1A">β = 0.004, α = 4β</td><td id="6-1B">3 (2)</td><td id="6-1C">88 (44)</td><td id="6-1D">149</td><td id="6-1E">3 (2)</td><td id="6-1F">–</td><td id="6-1G">–</td></tr>
<tr><td id="6-1H">12*</td><td id="6-1I">a = 0.165, k = 25</td><td id="6-1J">3 (2)</td><td id="6-1K">57 (29)</td><td id="6-1L">149</td><td id="6-1M">6 (4)</td><td id="6-1N">56</td><td id="6-1O">7 ± 2</td></tr>
<tr><td id="6-1P">13</td><td id="6-1Q">a = 0.66, k = 100</td><td id="6-1R">3 (2)</td><td id="6-1S">18 (9)</td><td id="6-1T">149</td><td id="6-1U">25 (17)</td><td id="6-1V">–</td><td id="6-1W">25 ± 1</td></tr>
<tr><td id="6-1X">14</td><td id="6-1Y">b = 1.0, c = 1000</td><td id="6-1Z">3 (2)</td><td id="6-20">33 (17)</td><td id="6-21">149</td><td id="6-22">12 (8)</td><td id="6-23">27±3</td><td id="6-24">27±25</td></tr>
<tr><td id="6-25">15</td><td id="6-26">b = 4.0, c = 4000</td><td id="6-27">3 (2)</td><td id="6-28">33 (17)</td><td id="6-29">149</td><td id="6-2a">12 (8)</td><td id="6-2b">–</td><td id="6-2c">–</td></tr>
<tr><td id="6-2d">16</td><td id="6-2e">k = 25</td><td id="6-2f">7 (3)</td><td id="6-2g">57 (29)</td><td id="6-2h">73</td><td id="6-2i">6 (9)</td><td id="6-2j">56</td><td id="6-2k">7±2</td></tr>
<tr><td id="6-2l">17</td><td id="6-2m">k = 100</td><td id="6-2n">2 (1)</td><td id="6-2o">18 (9)</td><td id="6-2p">300</td><td id="6-2q">25 (8)</td><td id="6-2r">–</td><td id="6-2s">25±1</td></tr>
<tr><td id="6-2t">18</td><td id="6-2u">c = 1000</td><td id="6-2v">3 (2)</td><td id="6-2w">18 (9)</td><td id="6-2x">149</td><td id="6-2y">25 (17)</td><td id="6-2z">15±2</td><td id="6-2A">45±39</td></tr>
<tr><td id="6-2B">19*</td><td id="6-2C">c = 4000</td><td id="6-2D">3 (2)</td><td id="6-2E">57 (29)</td><td id="6-2F">149</td><td id="6-2G">6 (4)</td><td id="6-2H">–</td><td id="6-2I">–</td></tr>
<tr><td id="6-2J">20</td><td id="6-2K">u = 1.0, q = 1.0</td><td id="6-2L">2 (1)</td><td id="6-2M">33 (17)</td><td id="6-2N">300</td><td id="6-2O">12 (4)</td><td id="6-2P">–</td><td id="6-2Q">–</td></tr>
<tr><td id="6-2R">21</td><td id="6-2S">u = 4.0, q = 4.0</td><td id="6-2T">7 (3)</td><td id="6-2U">33 (17)</td><td id="6-2V">73</td><td id="6-2W">12 (17)</td><td id="6-2X">18±8</td><td id="6-2Y">80±79</td></tr>
<tr><td id="6-2Z">22</td><td id="6-30">u = 1.0</td><td id="6-31">2 (1)</td><td id="6-32">18 (9)</td><td id="6-33">300</td><td id="6-34">25 (8)</td><td id="6-35">–</td><td id="6-36">–</td></tr>
<tr><td id="6-37">23</td><td id="6-38">u = 4.0</td><td id="6-39">7 (3)</td><td id="6-3a">57 (29)</td><td id="6-3b">73</td><td id="6-3c">6(9) 2</td><td id="6-3d">3±11</td><td id="6-3e">95±94</td></tr>
<tr><td id="6-3f">24*</td><td id="6-3g">q = 0.5</td><td id="6-3h">3 (2)</td><td id="6-3i">89 (44)</td><td id="6-3j">149</td><td id="6-3k">3 (2)</td><td id="6-3l">81±1</td><td id="6-3m">5±4</td></tr>
<tr><td id="6-3n">25*</td><td id="6-3o">q = 1.0</td><td id="6-3p">3 (2)</td><td id="6-3q">57 (29)</td><td id="6-3r">149</td><td id="6-3s">6 (4)</td><td id="6-3t">56</td><td id="6-3u">6±3</td></tr>
<tr><td id="6-3v">26</td><td id="6-3w">q = 4.0</td><td id="6-3x">3 (2)</td><td id="6-3y">18 (9)</td><td id="6-3z">149</td><td id="6-3A">25 (17)</td><td id="6-3B">–</td><td id="6-3C">25±1</td></tr>
<tr><td id="6-3D">27*</td><td id="6-3E">Advanced</td><td id="6-3F">3 (2)</td><td id="6-3G">188 (94)</td><td id="6-3H">149</td><td id="6-3I">0.16 (0.1)</td><td id="6-3J">165</td><td id="6-3K">0.16±0.06</td></tr>
</table>

<a id='e88d5a71-7856-4444-90d4-19af3940b7a7'></a>

Sub-index 1 refers to a system with no virus, the 2 with the pathogen but not the recombinant, and the 3 with both viruses. The columns 3-6 describe densities of equilibria from Eqs. (3)-(5). The density of normal cells as a percentage at the time of the pathogen infection (%x₁), and the density of the pathogen as a percentage in single-infected individuals (%v₂) are in parentheses. 'Oscillations' describes fluctuations in densities through day 200 after infection obtained from simulations. '-' means identical to equilibrium values. * indicates cases consistent with a high recuperation of normal cells, reduction of pathogen, and stability of the system. 'Advanced' considered very competent values for the recombinant parameters: α = 4β, c = 10,000 and q = 0.5.

<a id='a19e161b-31a5-4530-9677-61b8d4d6fbf0'></a>

cells and the pathogen density are also described in terms of percentage change in response to the infections. As the result of the pathogen infection, the density of normal cells declined to 1–3% of the amount in individuals without pathogen. After the addition of the recombinant, the normal cell density increased up to 8–44% of the density in an individual without pathogen, while the pathogen declined 83–98% of the density in an infected individual. In the best case considered, the pathogen was reduced to a very low density, but it was not exterminated by this therapy. Results from simulations indicated that those equilibria may be reached at different times, depending on the stability of the system, as well, that they may represent average values for low amplitude limit

<!-- PAGE BREAK -->

<a id='26c90527-048d-4afe-8797-91c62d96018d'></a>

198 T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191–203

<a id='0e1d7392-4d31-4cc9-bfe2-85d4c3dcb68e'></a>

cycles. The last two columns of Table 2 resulted from simulations and described fluctuations in density through day 200 after infection. By that time amplitudes were generally stabilized. The large oscillations were limit cycles, and their frequencies and amplitudes were determined by the parameter values, and not on the initial conditions [14]. Limit cycles were associated with low efficiency in the control of the pathogens. Table 2 (rows 1–26) indicates that a high recovery of normal cells (29–44%), elimination of pathogens (96–98%) and stability of the system are favored by large host cell and recombinant production rates (λ, c), and larger infection rate for the recombinant (α > β). The parameter values ‘Advanced’ at the bottom of Table 2 considered simultaneously competent values for several recombinant parameters. This set of values predicted a 99.9% elimination of the pathogens. This 1000-fold reduction of pathogens may represent the upper limit for the efficiency of this therapy.

<a id='e4973ecd-a19c-4456-be61-ddbdfddf73f3'></a>

The parameters production c and infection rates α of the recombinant virus could be manip-ulated genetically [15]. Appendix B illustrated the magnitude of these parameters for a recovery up to 40% of normal host cells. This level of cell recovery required that the product of the in-fection and production rates of the recombinant (αc) must be at least 133 times larger than the pathogen (αc/βk ≥ 133). Fig. 3 described in detail the positive effect of increasing only the re-combinant production rate c on the efficiency of this therapy. It showed that increasing c in-creased normal cells, decreased pathogens, and stabilized the system from limit cycles. At lower production rates (c < 2000, and default values), the system was characterized by oscillation in densities, and lower efficiencies in cell recovery and pathogen elimination. At intermediate pro-duction rates (c ~ 2000–10,000) the efficiency increases significantly with c, with cell recovery ranging from 17% to 50% and pathogen elimination from 92% to 98%. For larger production rates (extreme values), cell recovery and pathogen elimination levels progressed slowly with c.

<a id='6926dec4-82bb-45c4-81b4-53ec49642f6e'></a>

<::chart: Two plots showing the effect of recombinant production rate (c) on cell and pathogen densities. Both plots share a common x-axis labeled "Recombinant production rate c" ranging from 100 to 10000 on a logarithmic scale. The left y-axis for both plots is labeled "Density (counts/mm³)" ranging from 0 to 160. Each plot also has a right y-axis. The legend for the lines in both plots is:  -  `— β=α=ε` (thick solid line)  -  `— β=α=2ε` (thin solid line)  -  `-- β=ε, α=4ε` (dashed line).  

**Left Plot: Normal cells**  
-   Title: "Normal cells"  
-   Right y-axis: "% x̂₁" ranging from 0 to 80.  
-   The lines generally show an increasing trend with increasing 'c'. The thick solid line (`β=α=ε`) shows a steeper increase, reaching near 160 counts/mm³ (or 80% x̂₁) at c=10000. The thin solid line (`β=α=2ε`) and dashed line (`β=ε, α=4ε`) also increase but generally remain lower than the thick solid line. Some lines show bifurcated upper and lower bounds, especially at lower 'c' values. An asterisk (*) marks a point on the thick solid line around c=2000-3000.  

**Right Plot: Pathogens**  
-   Title: "Pathogens"  
-   Right y-axis: "% v̂₂" with labels 0, 27, 54, 81.  
-   The lines generally show a decreasing trend with increasing 'c'. The thick solid line (`β=α=ε`) starts high (around 160 counts/mm³) at low 'c' and drops sharply to near 0 at c around 2000. The other lines also decrease but generally start lower and drop less sharply. Bifurcated lines are also present, indicating upper and lower bounds of limit cycles. An asterisk (*) marks a point on the thick solid line around c=2000-3000.  

Fig. 3. Effect of the recombinant production rate (c), and the infection rates of pathogen and recombinant (α, β) on the densities of normal cells (x) and pathogens (v) at day 200 after infection. Bifurcated lines indicate upper and lower bounds of limit cycles found at some densities. ε = 0.004; initial conditions and other parameters not specified were as Fig. 2(b). * indicated default values. Right vertical axes describe density in terms of recovery of normal cells (%x̂₁), and remnant of pathogen percentages (%v̂₂).::>

<!-- PAGE BREAK -->

<a id='3e20b032-ebeb-47c9-a8dd-ea3da23b2f97'></a>

T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191-203

<a id='ece55d97-316b-493c-bda1-5e26a710464b'></a>

199

<a id='4aaa3111-a83a-4351-9586-b8bda9766c67'></a>

Fig. 3 also showed that when the infection rate is larger for the recombinant (α > β) these results are similar but of a larger magnitude.

<a id='a7bcce48-1b06-411b-893b-96cdce33b1ae'></a>

## 5. Discussion

A mathematical model studied a potential therapy for controlling HIV infection that uses an engineered virus to selectively eliminate infected cells. Results indicated that this viral-therapy of using genetically modified viruses can be effective in reducing the HIV-1 load in patients. The model predicted a 92% reduction of HIV load, and recovery of host cells to 17% of their normal level. This is a basic estimation that used data from a currently available engineered virus [6] and reasonable assumptions for some parameter values. The model also indicated a larger success as more competent engineered viruses are designed (98% HIV reduction and a host cells recovery to 44% of their normal level). Viral-therapy, however, may be less efficient than anti-viral drugs in reducing HIV-1 load, since anti-viral drugs may reduce the viral load to below the limit of detection (0.02-0.5 counts/mm³) [8]. Viral-therapy has a secondary effect, a high recombinant load that is considered innocuous in principle [6]. Nevertheless, viral-therapy may have several advantages over present conventional treatment, since it is expected no toxicity, no negative side effects, and no evolution of resistance (Appendix C). An additional advantage is the simplicity of treatment; in simulations and in in vitro experiments [6] the engineered virus remains in the system once introduced, indicating that only one treatment may be required. These advantages could make this viral-therapy an alternative to extend the survival of AIDS patients.

<a id='c2c29f98-43b0-4f0b-8d63-eb89c61714d1'></a>

Our results were consistent with those of Schnell et al. [6], however, in their in vitro study the drop in the HIV-1 level after the recombinant infection was larger (~0.6%) but comparable with the best cases simulated here (Table 2). Also, oscillations in HIV density after infection with the recombinant were observed experimentally [6].

<a id='c1749db6-d038-4645-a15d-384e428611e8'></a>

The present research provides a qualitative understanding of a simple model involving a hunter-virus to control a pathogen. Further research on viral-therapy may incorporate more realistic assumptions concerning the population dynamics of the entire population of CD4+ T cells; this would include the cellular cycle involving naïve, memory and activated CD4+ cells. It also may consider the impact of recovered CD4+ cells on the restoration of the immune system. Such a study may provide a more practical translation to a clinical situation. It is expected a synergistic interaction between the hunter-virus and the immune response controlling HIV-1 will occur. The engineered virus encodes only envelope human proteins and thus would not induce production of neutralizing antibodies. However, its internal proteins could induce a cytotoxic T cell response, but such responses might help in clearing HIV infection by rapidly killing cells infected with HIV-1 and the engineered virus [6]. This model does not consider the pathogen-recombinant interaction, which may generate hybrid viruses capable of attacking normal or infected cells. Such an interaction was reported as being extremely rare [6]. The simulated infections exhibited temporal dynamic behaviors varying from broad limit cycles to rapid equilibrium convergence. Large production and infection rates for the engineered virus favored equilibrium convergence and a major reduction of HIV-1 load. Thus, viral engineers may look to improve those parameter values in hunter-viruses. More quantitative predictions require detailed measuring of the therapeutic infection parameters such as rates of infectivity, production and

<!-- PAGE BREAK -->

<a id='1d139d42-903d-41ca-b144-a404995d52ac'></a>

200 T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191–203

<a id='6ef0042d-68ba-4aef-a3ef-3824bdc43750'></a>

elimination of the engineered virus. The construction of the recombinant caused an important reduction in the efficiency of budding viral particles [6]. Since genetically engineered VSV has crucial medical applications including an alive-vaccine [16] research has been conducted to determine critical modifications in the VSV membrane for virus assembly [15]. This may allow for the design of more efficient recombinants.

<a id='4252df46-62cd-4919-b8a8-1d7c6c3488e0'></a>

A comparable model used a defective interfering virus (DIV) as therapy for AIDS [17]. Similar to our recombinant virus, DIV only replicates in a host cell coinfected with HIV. The proposed DIV was assumed to obstruct HIV replication by two interfering mechanisms: slowing the as-sembly of HIV-1, and producing HIV-1 with reduced infectivity (HIV*). Therefore, the model considered two pathways for double-infected cells: (a) undergo lysis producing HIV, HIV* and DIV; or (b) stay alive 'cured' producing HIV* and DIV. In both pathways coinfected cells ex-perience large removal rates. This model predicted, however, that DIV survival on a peripheral blood HIV-1 infection is unlikely. Our mechanism is simpler because the double-infected cells are killed by the rapid cytopathic infection of the recombinant producing only recombinants. This assumption was based on the recombinant replication speed. Within 3 h after infection the recombinant would shut off cell protein synthesis and within 8 h would produce particles that bud from the cell prior to lysis [6], while the life span of a HIV-1 infected cell is 2-3 days [12,18,19].

<a id='085b3f49-2e8e-4d21-894b-b5adedbd78b5'></a>

Therapy using viruses has been employed to treat bacterial diseases [20–25], and has been found to be more efficient than antibiotics because of the continuous replication of the virus compared to the rapid decay of antibiotics [23]. Beneficial effects of a virus on viral diseases have also been reported where the hepatitis G virus that coinfects HIV patients increases their survival [26,27]. Results of the present study are important not only in relation to therapies against AIDS but also for other diseases for which these biological devices may be developed.

<a id='57623434-252b-48da-9833-f72d05147193'></a>

## Acknowledgements
We are indebted to J.J. Bull for revealing the potential application of modeling predator-prey dynamics in viruses. We thank R. May for valuable comments as well as P. Crowley, L. Brewer and D. Rodríguez for their many helpful suggestions. The manuscript benefited from comments by two anonymous reviewers. This work was supported by a grant PG 03-31-4336-1999 from the CDCH, Universidad Central de Venezuela to T.R.; and from the Center for Computational Sciences, University of Kentucky to G.G.-R.

<a id='f79c1861-5590-457f-bb5a-b4a1a455f05e'></a>

Appendix A. Condition for the recombinant invasion (basic reproductive ratio)

From Fig. 1, each double-infected cell Z produces recombinants at a rate c during a mean life 1/b, resulting in a 'net production of recombinants' c/b. These recombinants W infect pathogen-infected cells Y at an infection rate per recombinant of ay (Eq. (2)). Since the mean life time for a recombinant is 1/q the 'net number of infections per recombinant' is ay/q. Then by multiplying the net production of recombinants by the net number of infections, results in the number of secondary infections or basic reproductive ratio [32] for the recombinant:

<!-- PAGE BREAK -->

<a id='95bb12b2-fadf-4040-9894-5af188865104'></a>

T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191-203                                                                     201
R_w = \alpha yc/bq.                                                                                                                        (A.1)

<a id='5d8f5e9e-0997-42da-901d-1190653a4f8d'></a>

At the beginning of the recombinant infection the density of pathogen-infected cells y is given by Eq. (4). By replacing this density into (A.1) gives

$R_w = \frac{\alpha c}{bq} \left( \frac{\lambda}{a} - \frac{du}{\beta k} \right)$ (A.2)

<a id='0c2e31e2-e8d7-4a43-ad88-b0e57084bbd1'></a>

By taking λ/α as a common factor off the parentheses in (A.2), the basic reproductive ratio of the
recombinant becomes

$R_w = \frac{\alpha \lambda c}{abq} \left(1 - \frac{adu}{\beta \lambda k}\right)$ (A.3)

The quotient inside the parentheses of (A.3) is the reciprocal of $R_v$.

<a id='0676b973-5534-44e1-959b-e825b6971023'></a>

## Appendix B. Extent of recovery of normal host cells

An efficient therapy must also increase normal cell density allowing the recuperation of the immune system. The recovery of normal cells after the recombinant infection is determined by the ratio r = βbkq/αcu. This ratio differentiates the amount of normal cells in a system without viruses (x₁ = λ/d, Eq. (3)), from one with both viruses (x₃ = λ/(d+r), Eq. (5)), and it must be small to recover abundant cells. Successful therapy may be indicated by achieving a normal-cell level of at least 40% in a non-infected individual (assuming that activated and total CD4+ T cells vary proportionally, this percentage may represent the presymptomatic stage of AIDS [1]). A recovery of cells up to 40% is reached for r≤1.5d. By considering the default values for b, q, u, and d (Table 1), this ratio is reduced to αc/βk ≥ 133 which requires a recombinant with a product of production and infection rates 133 larger than the corresponding product for the pathogen.

<a id='88cb7f80-5577-498e-83bb-75e3e4e66ff8'></a>

# Appendix C

## *C.1. Could HIV evolve resistance to the recombinant?*

For an HIV-1 infection, the HIV-1 envelope protein gp120/41 must bind to receptors at the cell surface, and then HIV-1 fuses its envelope with the membrane of the cell. Later, the recombinant attacks HIV-1-infected cells by binding to the gp120/41 expressed on the cell surface. Consequently, a HIV-1 mutation for resistance to the recombinant infection would require the loss of HIV's ability to bind the cell receptors [6], and this loss of HIV infectivity would therefore not be selected.

<a id='f4598119-a6da-4a4d-966b-6c27b0640e5d'></a>

C.2. What toxicity and side effects has incorporating a virus into the human body?
The recombinant was derived from the VSV that causes a non-lethal disease in farm animals consisting of blister-like bumps on the hoofs and tongue. Occasionally, humans become infected

<!-- PAGE BREAK -->

<a id='3ba58401-decc-42ea-885a-553917db7a19'></a>

202

<a id='11760cef-2b02-473f-bed2-a6148e2c9749'></a>

T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191–203

<a id='1c45ee68-7a53-4005-b712-85b26262b03d'></a>

with VSV, and most individuals have no symptoms, but those who become ill usually have a mild flu-like disease [6]. Since the VSV recombinant no longer has its normal coat protein it cannot cause infection in livestock or healthy humans.

<a id='61ecb323-9b5c-40a3-9904-28083f44428a'></a>

Further, lytic bacteriophages - small viruses that are harmless for humans but lethal for their bacterial host - have been used since the early 20th century to cure human bacterial infections [20-22,24,25]. During this period, these phages have been administered extensively in Eastern Europe and the former Soviet Union to treat a broad list of individual and epidemic infections, and there are no reports of serious complications. From a clinical standpoint, the phages appear to be innocuous [25]. Viruses have further potential assisting in prevention and treatment of human infections. For example, Alive Vaccines will use viruses expressing given foreign proteins to induce specific immune responses [16]. Gene Therapy has used viral vectors to transfer genetic material to target cells [33]. Phages are expected to be commercialized in the USA to treat multidrug resistant bacterial infections.

<a id='3e3f1906-cb5b-484b-b6db-73896a9cc03f'></a>

## References

[1] A.T. Haase, Population biology of HIV-1 infection: viral and CD4+ T cell demography and dynamics in lymphatic tissues, Ann. Rev. Immunol. 17 (1999) 625.
[2] J. Levy, HIV and the Pathogenesis of AIDS, ASM, Washington, DC, 1998.
[3] G.P. Nolan, Harnessing viral devices as pharmaceuticals: fighting HIV-1s fire with fire, Cell 90 (1997) 821.
[4] E.K. Wagner, M.J. Hewlett, Basic Virology, Blackwell, New York, 1999.
[5] T. Mebatsion, S. Finke, F. Weiland, K. Conzelmann, A CXCR4/CD4 pseudotype rhabdovirus that selectively infects HIV-1 envelope protein-expressing cells, Cell 90 (1997) 841.
[6] M.J. Schnell, E. Johnson, L. Buonocore, J.K. Rose, Construction of a novel virus that targets HIV-1 infected cells and control HIV-1 infection, Cell 90 (1997) 849.
[7] Z.-Q. Zhang, T. Schuler, M. Zupancic, S. Wietgrefe, K.A. Staskus, K.A. Reimann, T.A. Reinhart, M. Rogan, W. Cavert, C.J. Miller, R.S. Veazey, D. Notermans, S. Little, S.A. Danner, D.D. Richman, D. Havlir, J. Wong, H.L. Jordan, T.W. Schacker, P. Racz, K. Tenner-Racz, N.L. Letvin, S. Wolinsky, A.T. Haase, Sexual Transmission and propagation of SIV and HIV in resting and activated CD4+ T cells, Science 286 (1999) 1353.
[8] T. Pierson, J. McArthur, R.F. Siliciano, Reservoirs for HIV-1: mechanisms for viral persistence in the presence of antiviral immune responses and antiretroviral therapy, Ann. Rev. Immunol. 18 (2000) 665.
[9] M.A. Nowak, C.R.M. Bangham, Population dynamics of immune responses to persistent viruses, Science 272 (1996) 74.
[10] S. Crowe, J. Mills, Virus infections of the immune system, in: D.P. Stites, A.L. Terr, T.E. Parslow (Eds.), Basic and Clinic Immunology, Appleton & Lange, Norwalk, CT, 1994, p. 689.
[11] M.A. Nowak, R. May, Virus Dynamics, Oxford University Press, Oxford, 2000.
[12] B.N. Phillips, Reduction of HIV concentration during acute infection: independence from a specific immune response, Science 271 (1996) 497.
[13] N. Sachsenberg, A.S. Perelson, Y. Sabine, G.A. Schock, D. Leduc, B. Hirschel, L. Perrin, Turnover of CD4+ and CD8+ T lymphocytes in HIV-1 infection as measured by Ki-67 antigen, J. Exp. Med. 187 (1998) 1295.
[14] J. Roughgarden, Theory of Populations Genetics and Evolutionary Ecology, Macmillan, New York, 1979.
[15] M.J. Schnell, L. Buonocore, E. Boritz, H.P. Ghosh, R. Chernish, J.K. Rose, Requirement for a non-specific glycoprotein cytoplasmic domain sequence to drive efficient budding of vesicular stomatitis virus, EMBO 17 (1998) 1289.
[16] N.F. Rose, P.A. Marx, A. Luckay, D.F. Nixon, W.J. Moretto, S.M. Donahoe, D. Montefiori, A. Roberts, L. Buonocore, J.K. Rose, An effective AIDS vaccine based on live attenuated vesicular stomatitis virus recombinants, Cell 106 (2001) 539.

<!-- PAGE BREAK -->

<a id='dc712ea9-1bb0-4f10-804a-6b092ea99f48'></a>

T. Revilla, G. García-Ramos | Mathematical Biosciences 185 (2003) 191-203

<a id='b5deba60-af7b-4562-ace2-c70a11ed3b42'></a>

203

<a id='2324d49a-2663-4387-bba0-ecfc59638fd7'></a>

17. G.W. Nelson, A.S. Perelson, Modelling defective interfering virus therapy for AIDS: conditions for DIV survival, Math. Biosci. 125 (1995) 127.
18. A.S. Perelson, A.U. Neumann, M. Markowitz, J.M. Leonard, D.D. Ho, HIV-1 dynamics in vivo: virion clearance rate, infected cells life-span, and viral generation time, Science 271 (1996) 1582.
19. M.A. Stafford, L. Corey, Y. Cao, E.S. Daar, D.D. Ho, A.S. Perelson, Modeling plasma virus concentration during primary HIV infection, J. Theor. Biol. 203 (2000) 285.
20. P. d'Herelle, The Bacteriophage and its Behavior, Williams & Williams, Baltimore, MD, 1926.
21. V.M. Sakandelidze, The combined use of specific phages and antibiotics in different infectious allergoses, Vrachebnoe Delo 3 (1991) 60.
22. S. Slopek, B. Wener-Dabrowska, M. Dabrowska, A. Kucharewicz-Krikowska, Results of bacteriophage treatment of supportive bacterial infections in the years 1981-1986, Arch. Immunol. Ther. Exp. 35 (1997) 569.
23. B.R. Levin, J.J. Bull, Phage therapy revisited: the population biology of a bacterial infection and its treatment with bacteriophage and antibiotics, Amer. Nat. 147 (1996) 881.
24. R.M. Carlton, Phage therapy: past history and future prospects, Arch. Immunol. Exp. 47 (1999) 267.
25. A. Sulakvelidze, Z. Alavidze, G. Morris Jr., Bacteriophage therapy, Antimicrob. Agents Chemother. 45 (2001) 649.
26. H.L. Tillmann, H. Heiken, A. Knapik-Botor, S. Heringlake, J. Ockenga, J.C. Wilber, B. Goergen, J. Detmer, M. McMorrow, M. Stoll, R.E. Schmidt, M.P. Manns, Infection with GB virus C and reduced mortality among HIV-infected patients, N. Engl. J. Med. 345 (2001) 715.
27. J. Xiang, S. Wunschmann, D.J. Diekema, D. Klinzman, K.D. Patrick, S.L. George, J.T. Stapleton, Effect of coinfection with GB virus C on the survival among patients with HIV infection, N. Engl. J. Med. 345 (2001) 707.
28. C.A. Michie, A. McLean, C. Alcock, P.C.L. Beverly, Lifespan of human lymphocyte subsets defined by CD45 isoforms, Nature 360 (1992) 264.
29. J.M. Murray, G. Kaufmann, A.D. Kelleher, D.A. Cooper, A model of primary HIV infection, Math. Biosci. 154 (1998) 57.
30. S.P. Layne, J.L. Spouge, M. Dembo, Quantifying the infectivity of human immunodeficiency virus, Proc. Nat. Acad. Sci. USA 86 (1989) 4644.
31. D.S. Dimitrov, R.L. Willey, H. Sato, L.J. Chang, R. Blumenthal, M.A. Martin, Quantitation human immunodeficiency virus type 1 infection kinetics, J. Virol. 67 (1993) 2182.
32. R.M. Anderson, R.M. May, Infectious Diseases of Humans, Oxford University, Oxford, 1991.
33. J.S. Norris, C. Westwater, D. Dolan, Prokaryotic gene therapy to combat multidrug resistant bacterial infection, Gene Therapy 7 (2000) 723.
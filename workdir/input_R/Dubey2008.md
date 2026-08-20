<a id='ac232501-1b06-4d8a-a544-12e71690c054'></a>

Journal of Biological Systems, Vol. 16, No. 3 (2008) 337-356
© World Scientific Publishing Company

<a id='6519331a-b9ed-4bf5-b5c3-bfb53f75d5c6'></a>

<::logo: World Scientific
World Scientific
www.worldscientific.com
This logo features a stylized "WS" monogram in black, with the company name and website in black text to its right.::>

<a id='c6ba831a-d8a7-4759-bf7e-2b77f39dc900'></a>

MODELING THE INTERACTION BETWEEN AVASCULAR
CANCEROUS CELLS AND ACQUIRED IMMUNE RESPONSE

<a id='5604c5c1-113d-4392-971b-dc10052a113a'></a>

B. DUBEY,*,‡ UMA S. DUBEY† and SANDIP BANERJEE*

*Mathematics Group and †Biological Science Group
Birla Institute of Technology and Science (BITS)
Pilani 333 031, India
‡bdubey@bits-pilani.ac.in

<a id='d6e75b3a-1c29-4702-b652-dace98aaa1d5'></a>

Received 25 November 2007
Accepted 25 March 2008

<a id='e8ad0f56-4fba-4688-abe0-48f723ebcb36'></a>

This paper deals with the interaction between dispersed cancer cells and the major populations of the immune system, namely, the T helper cells, T Cytotoxic cells, B cells, and antibodies produced. The system is described by a set of five ordinary differential equations. Both local and global stability of the system has been investigated. It has been observed that under appropriate conditions this interaction is capable of controlling the growth of these cancer cells. The analytical findings are supported by numerical and computational analytical methods.

<a id='7cf5a602-1d00-4b12-b8e2-03d50570d0e6'></a>

Keywords: Cancer Cells; Cytotoxic T-Lymphocytes; T-Helper Cells; B Cells; Antibodies; Cytotoxicity; Proliferation.

<a id='4bb5ce43-1135-406d-b770-c642d9be41a0'></a>

# 1. Introduction
Cancer is a leading cause of death worldwide. From a total of 58 million deaths worldwide in 2005, cancer accounts for 7.6 million (or 13%) of all deaths.¹ Deaths from cancer in the world are projected to continue rising, with an estimation of 9 million people dying from cancer in 2015 and 11.4 million dying in 2030. The Immune system not only helps in fighting against pathogenic micro-organisms but also helps preventing the occurrence, development, and recurrence of cancer within the body. Various components of the immune system interact with each other and with cancer cells to facilitate the detriment of the latter. But sometimes, cancer cells are able to overcome the limitations imposed by the immune system and are able to successfully proliferate and propagate within the body. The condition under which this happens is of clinical significance and needs to be better understood to ensure proper management and cure. Besides using experimental systems, it is also possible to understand this interaction by using mathematical models. The additional advantage of a mathematical model is that in such an approach it is possible to simultaneously alter multiple number of parameters in a wide range, a situation difficult to achieve under experimental conditions.

<a id='0249add3-a542-44bb-b3e9-e6f8d5b292ab'></a>

337

<a id='c976012a-0a6d-40f7-a832-aab9eb06cb71'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='396f81a2-0e7b-4468-a3c3-ca0bb7ed0fec'></a>

338 Dubey et al.

<a id='0edbb4dc-269c-4be5-b473-a9458f907311'></a>

There have been numerous studies on the cancer-immune dynamics. A good summary can be found in Adam and Bellomo² and Preziosi.³ A mathematical model of the cytotoxic T lymphocyte response to the growth of an immunogenic tumor is presented by Kuznetsov and Taylor,⁴ followed by Kirschner and Panetta,⁵ who have illustrated through mathematical modeling the dynamics between tumor cells, immune effector cells, and interleukin-2 (IL-2). Their efforts explain both short-term tumor oscillations in tumor sizes as well as long-term tumor relapse. They also explored the effects of adaptive cellular immunotherapy on the tumor model and described the circumstances under which the tumor can be eliminated. Kolev⁶ presented a mathematical model, showing competition between cancer and immune system, considering the role of antibodies. The model is developed with statistical methods analogous to those of the kinetic theory and is expressed in terms of a system of integro-differential equations. Arciero et al.⁷ described a mathematical model which represented growth, immune escape, and siRNA treatment of cancer. The model consists of a system of nonlinear ordinary differential equations describing cancer cells and immune effectors, as well as the immuno-stimulatory and suppressive cytokines IL-2 and TGF-β. Matzavinos and Chaplain Mart⁸ presented a travelling-wave analysis of a mathematical model describing the growth of a solid tumor in the presence of an immune system response. From a modeling perspective, attention is focused upon the attack of cancer cells by tumor infiltrating cytotoxic lymphocytes (TICLs), in a small multicellular cancer, without necrosis and at some stage prior to (cancer-induced) angiogenesis. Sarkar and Banerjee⁹ expressed the spontaneous regression and progression of cancer (malignant tumor) and its interaction with immune system as a prey-predator-like system. They extended the deterministic model (a set of ODE's) to a stochastic one allowing random fluctuations around the positive interior equilibrium and obtained thresholds which may be helpful to control the malignant tumor growth. Recently, Dubey and Dubey¹⁰ proposed a mathematical model and studied the effect of toxicant on the immune system of the body. They observed that the oscillatory behavior of the immune system of the body is least in the presence of the toxicant. It may be noted that most of the earlier studies related to mathematical modeling and cancer cells have been done for tumors (solid masses of cancers) but very few studies have been conducted on avascular cancers. A review of the same has been presented by Roose et al.¹¹

<a id='3eb077fb-13c9-4f0f-82c9-b44f79d4f762'></a>

It may be noted that all cancers (like cancerous blood cells and even malignant tumor cells in very early stage of development) are not necessarily solid. The dispersed state of such malignant cells exhibit increased interaction with the immune system. These malignant cells are in the state of so-called free cell regime, namely a physical situation in which cells move freely and homogeneously in space and cancer cells are not yet condensed in a macroscopically observed quasi-spherical tumor.12 In such a case there is an increased interaction between malignant cells and the immune system. Earlier metastasis of human cells using cell lines 13,14 has been experimentally studied by Bioluminescent imaging. In a lung colonization

<a id='01871ce0-6947-4e69-b091-b14021503072'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com
by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='39ec0a46-d40d-482e-9127-211c4ff9db93'></a>

Modeling the Interaction

<a id='ddef2092-e1d1-48b0-be6d-74129a3718ae'></a>

339

<a id='6840e465-294f-474d-abef-8400640429c5'></a>

model, A549-Luc-C8 human lung cancer cells were injected intravenously and lung
metastasis was monitored in vivo by whole animal imaging. This longitudinal study
permitted an accurate, real-time evaluation of tumor burden in the same animals
for a period of time. Although the above model is experimental rather mathemat-
ical, but single cells were used to induce metastasis (in cell-free regime). In the
present paper, this aspect is considered in modeling the system and our model may
also be applicable to cancer cells which have detached from the main body of tumor
and are in circulation during the process of metastasis.

<a id='2734e88e-ad13-4ac1-a01a-539db3d7dcd5'></a>

The paper has been divided into the following main sections, Sec. 2 briefly
describes avascular cancer cell and the major components of the immune system.
The mathematical model related to the interaction between cancer cells and vari-
ous components of acquired immune system has been formulated and described in
Sec. 3. Stability analysis of this model has been done in Sec. 4. Section 5 deals with
the numerical calculations and its interpretation. The paper ends with a discussion
in Sec. 6.

<a id='809b135d-27e7-492b-adff-b5460f54c0d8'></a>

## 2. Biology of the Cancer Cell–Immune System Interaction

Neoplastic cells are rapidly multiplying self-cells, which have undergone genetic alterations to cause uninhibited cell proliferation and malignant potential. A solid neoplasm is a tumor. Occasionally, small clusters of neoplastic cells dislodge from their original site, invade the blood or lymphatic vessels, and are carried to other tissues where they again rehabilitate (metastasis). These cells that are more aggressive, invasive, and display metastatic potential are cancer cells. Metastasis is responsible for the majority of cancer deaths. Cancer cell antigens have been shown to induce both humoral and cell mediated immune responses.<sup>15</sup> Our present study deals with cancerous cells that are in dispersed state and thus have better interaction with the cells of the immune system. Also there is no specialized vasculature (blood vessel) requirement to transfer gases nutrient and waste materials.

<a id='aceaf556-f525-4547-b961-5d32807b8651'></a>

The immune system has two main components — Innate immunity and acquired immunity. Innate immunity is the non-specific component which is naturally present, even if absence of any invading microbe or cancer. The next component is adaptive or acquired immunity. It does not come into play until there is an anti-genic challenge or development of cancer. It responds to the challenge with very high degree of specificity. The adaptive immune response requires few days to get activated, whereas the innate immune response acts just after exposure to pathogen or immediately upon development of cancer.

<a id='3eee4662-8490-4774-a390-5cb7d61b72ca'></a>

The acquired immune response is mediated primarily by lymphocytes and includes the cell mediated immune response as well as the humoral immune response. The cell mediated immune responses are mediated by the T lympho- cytes, whereas the humoral immune responses are mediated by the B cells which produce antibodies specific to antigens. Antibodies are used by the immune system to identify and neutralize targets such as bacteria, viruses, etc. but in our case the

<a id='1d655f01-8828-4fc6-b02e-14e774b5387c'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='fdc562f8-dde6-413f-a802-efe7f8ebd149'></a>

340 _Dubey et al._

cancer cells. The T lymphocytes are of two types. The T-cytotoxic cells ($T_c$) kill
the target cells in an antigen specific manner, whereas T-helper cells ($T_h$) are reg-
ulators of the cellular as well as humoral components of the cell mediated immune
response.$^{15}$

<a id='40fa3d8f-9672-4a31-ad9f-9217ad45c796'></a>

T helper cell interacts with the cancer cell it gets activated and releases cytokines like IL-2 and these cytokines promote the proliferation of not only T_c and B cells but also T_h cells itself. The T_c cells and the B cells after proliferation differentiated into effector cells. An effector T_c cell lyses the cancer cell, whereas the effector B cells secretes antibodies which act in a manner detrimental to cancer cells.

<a id='159cb6e9-d66c-4ad2-b9d1-7243a7b7d128'></a>

### 3. Mathematical Model of Adaptive Immune System–Cancer Cell Interaction

In this paper, we consider the interaction between cancer cells and the cellular components of the adaptive immune system namely, T-cytotoxic cells, T-helper cells, B-Cells, and the antibodies. The system is described with the help of five ordinary differential equations and its local as well as global stability analysis is performed. This system may also serve as a mathematical model for adaptive immunotherapy. Figure 1 gives the schematic diagram of the interactions between cancer cells and various components of immune system. This simplification allows for a complex yet

<a id='f8687133-4607-4c34-8ae7-e62037d58dc9'></a>

<::The diagram illustrates the interaction between cancer cells and the immune system. It features several components: T-Helper Cells, Cancer Cells, B Cells, Cytotoxic T lymphocytes, Destroyed Cancer Cells, Antibodies, Death, and Death/functional inactivation. Rectangular nodes represent cell types or entities, while oval nodes represent states of removal or inactivation. Arrows indicate interactions or transitions, with solid arrows generally showing activation, stimulation, or progression, and dashed/dotted arrows often indicating inhibition, death, or inactivation rates.  Specific interactions are labeled with Greek letters.

- T-Helper Cells:  
  - An arrow labeled γ2 points to B Cells.  
  - An arrow labeled β2 points to Cytotoxic T lymphocytes.  
  - A dotted arrow labeled μ10 points to Death.  
  - A curved solid arrow points to Cancer Cells.  

- Cancer Cells:  
  - A curved solid arrow points from T-Helper Cells to Cancer Cells.  
  - A curved solid arrow points from Cytotoxic T lymphocytes to Cancer Cells.  
  - A dotted arrow labeled μ11 points from Cancer Cells to T-Helper Cells.  
  - A dotted arrow labeled μ2 points from Cancer Cells to Cytotoxic T lymphocytes.  
  - An arrow labeled γ1 points to B Cells.  
  - A dotted arrow labeled μ3 points from Cancer Cells to B Cells.  
  - A dotted arrow labeled α0 points to Destroyed Cancer Cells.  
  - A thick solid arrow labeled δ1 points to Antibodies.  
  - A dotted arrow labeled μ4 points from Cancer Cells to Antibodies.  
  - A dotted curved arrow indicates a self-loop or proliferation for Cancer Cells.  
  - A dotted arrow labeled μ30 points to Death/functional inactivation.  

- Cytotoxic T lymphocytes:  
  - An arrow labeled α1 points to Destroyed Cancer Cells.  
  - A dotted arrow labeled μ20 points to Death.  

- Antibodies:  
  - An arrow labeled δ2 points to Destroyed Cancer Cells.  
  - A dotted arrow labeled μ40 points to Death/functional inactivation.
: flowchart::>

Fig. 1. The figure represents the key players in the interaction between cancer cells and immune system.

<a id='5a2626af-31c8-4afe-8f27-cc3b16df993d'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='a50ce42a-5a9c-44c4-b9bd-5e1297268bb0'></a>

_Modeling the Interaction_

<a id='ebed0f8c-b839-4a6b-bf81-5ea65b301856'></a>

341

<a id='67cd716f-f180-485c-82bd-29c26e52e578'></a>

manageable mathematical system. Predictions based on this model are similar to
biological realities, thus the complexity is matched with its realities.

<a id='eb7b300d-5eb5-41b0-a6d7-4c0aa7338951'></a>

The arrows with double lines show the negative effect of the interaction between various components on a specific concentration and the arrows with a single line show the positive effect. The dotted arrows indicate the effect of a single component and the line arrows show the interaction between two components.

<a id='e7c52188-842f-448c-a64e-2d64ff515417'></a>

Let T, Th, Tc, B, and A represent, respectively, the concentration of the cancer cells, T-Helper cells, Cytotoxic T lymphocytes, B Cells, and antibodies, respectively. Keeping in view the interactions of cancer cells with immune system as mentioned in Sec. 2 and in Fig. 1, the dynamics of the system can be governed by the following system of ordinary differential equations:

<a id='bfa976e2-fb17-45b7-8fb6-9e7c6aa8920c'></a>

$$\frac{dT}{dt} = \alpha T - \alpha_0 T^2 - \alpha_1 T T_c - \delta_2 T A$$ 

$$\frac{dT_h}{dt} = \mu_1 T - \mu_{10} T_h + \mu_{11} T T_h$$ 

$$\frac{dT_c}{dt} = \mu_2 T - \mu_{20} T_c + \beta_1 T T_c + \beta_2 T_h T_c \qquad (3.1)$$ 

$$\frac{dB}{dt} = \mu_3 T - \mu_{30} B + \gamma_1 T B + \gamma_2 T_h B$$ 

$$\frac{dA}{dt} = \mu_4 B - \mu_{40} A - \delta_1 T A$$

<a id='075f85b5-6baa-4aa8-abc1-91a3a24b2f87'></a>

T(0) ≥ 0, Th(0) ≥ 0, Tc(0) ≥ 0, B(0) ≥ 0, A(0) ≥ 0.

<a id='9e71ddf2-296c-4e8f-bd45-51455cc11e26'></a>

The proposed mathematical model implements five key players and their interpretations are as follows:

<a id='466681eb-807e-4be5-a080-c50424746d06'></a>

Cancer Cells (T)

* The cancer cell has an inherent growth characteristic represented by αT.
* Its growth is limited by competition with similar cancer cells (-α₀T²).
* The growth of cancer cells depends on its interaction with T Cytotoxic cells and the cancer specific antibodies. T cytotoxic cells decline the cancer cell number by killing them (-αTTc). Similarly, antibodies also limit the proliferation (-δ₂TA) of cancer cells.

<a id='58ca4d45-e9fa-42b6-92f9-48fe96543802'></a>

T-Helper Cells (Tₕ)
* The proliferation of cancer specific T-Helper cells is enhanced due to the antigenicity of the cancer (μ₁T) and due to its interaction with these cells (μ₁₁TTₕ).
* (-μ₁₀Tₕ) gives the natural decay of the T-Helper cells.

<a id='93616856-bbc8-4531-b62e-26fdefbfd147'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='ad521e5a-ede1-4df7-942c-bf739ea823e5'></a>

342 Dubey et al.

<a id='3b63677c-ce0f-46ff-97fd-4cbdb507f26e'></a>

Cytotoxic T lymphocytes ($T_c$)

* The number of T cytotoxic cells increase with the antigenicity ($\mu_2T$) of the cancer cell.
* The proliferation of $T_c$ cells is stimulated by its interaction with the cancer cells ($\beta_1TT_c$) and T-Helper cells ($\beta_2T_hT_c$).
* The natural decay of the T-Helper cells is represented by ($-\mu_{20}T_h$).

B-Cells

* The proliferation of B cells is enhanced due to the antigenicity of the cancer cells ($\mu_3T$).
* The antibody secreting B cells get activated by the cancer cells ($\gamma_1TB$) as well as T helper cells ($\gamma_2T_hB$).
* The natural death rate of these cells is indicated by $ -\mu_{30}B$.

<a id='94c1c072-a53b-4118-a036-ef3efa5d8d0d'></a>

Antibodies

*   Antibodies are produced by the B cells at a rate directly proportional to the number of these cells (µ4B).
*   Antibodies themselves interact with the cancer cells by attaching to its specific cell surface antigens and are consumed, resulting in decline in the process (-δ1TA).
*   The rate of natural decay of of antibodies is indicated by -µ40A.

<a id='97c5a7b9-ee49-4c6e-b4de-92a94d43cec5'></a>

In the following lemma we show that all solutions of system (1) are non-negative and bounded, which shows that the system under consideration is biologically well behaved. The proof of this lemma is easy and hence omitted.

<a id='3edf9175-cb9c-491e-bd40-437943b0dcd5'></a>

Lemma 3.1. The set Ω = {(T, Th, Tc, B, A): 0 ≤ T ≤ α/α₀, 0 ≤ Th ≤ Thk, 0 ≤ Tc ≤ Tck, 0 ≤ B ≤ Bk, 0 ≤ A ≤ Ak} is a region of attraction for all solutions initiating in the interior of the positive orthant, where

<a id='f605cc3d-98f9-4690-ac3d-057b528c5c73'></a>

$\qquad T_{hk} = \frac{\mu_1\alpha}{\mu_{10}\alpha_0 - \mu_{11}\alpha}$,\quad $T_{ck} = \frac{\mu_2\alpha}{\mu_{20}\alpha_0 - \beta_1\alpha - \beta_2 T_{hk}\alpha_0}$

<a id='e4ca837e-da18-4f97-b5e1-d29b76efceef'></a>

Bk = μ3α / (μ30α0 - γ1α - γ2Thkα0),
Ak = μ4Bk / μ40,

<a id='44e489c9-7226-4d48-9b2f-8d607ab503b5'></a>

$$\mu_{10}\alpha_0 > \mu_{11}\alpha, \quad \mu_{20}\alpha_0 > \beta_1\alpha + \beta_2T_{hk}\alpha_0, \quad \mu_{30}\alpha_0 > \gamma_1\alpha + \gamma_2T_{hk}\alpha_0.$$

<a id='5cb8ceda-adda-422d-9c96-5b566fde51b7'></a>

## 4. Stability Analysis
The model system (3.1) has two non-negative equilibria, namely, $E_0$ (0, 0, 0, 0, 0) and $E^*$ ($T^*$, $T_h^*$, $T_c^*$, $B^*$, $A^*$). The equilibrium point $E_0$ always exists, and we show the existence of the positive equilibrium as follows.

<a id='6fa7bed7-8665-4bae-8fdf-df2b0aa5583a'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com
by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='44044762-d01b-4738-9a4a-fc99d40f22a8'></a>

Modeling the Interaction 343

<a id='b4537fc9-eb32-48b8-8a93-c57e933890ba'></a>

Here, $T^*, T_h^*, T_c^*, B^*$ and $A^*$ are the positive solutions of the following algebraic equations:

$\alpha - \alpha_0 T - \alpha_1 T_c - \delta_2 A = 0,$ (4.1a)

$\mu_1 T - \mu_{10} T_h + \mu_{11} T T_h = 0,$ (4.1b)

$\mu_2 T - \mu_{20} T_c + \beta_1 T T_c + \beta_2 T_h T_c = 0,$ (4.1c)

$\mu_3 T - \mu_{30} B + \gamma_1 T B + \gamma_2 T_h B = 0,$ (4.1d)

$\mu_4 B - \mu_{40} A - \delta_1 T A = 0.$ (4.1e)

Eq. (4.1b) yields

<a id='7f067d31-fde9-4c0e-8b06-b600c26375f1'></a>

Eq. (4.1b) yields

$T_h = \frac{\mu_1 T}{\mu_{10} - \mu_{11} T}$ (4.2)

Eq. (4.1c) yields

<a id='237cf5e1-66e5-4dd8-b8d6-c9dc62d64303'></a>

Eq. (4.1e) yields

$A = \frac{\mu_4 B}{\mu_{40} + \delta_1 T}$ (4.3)

Eqs. (4.1d) and (4.2) give

<a id='f0e75417-da84-4bce-a24f-87096f230456'></a>

$$B = \frac{\mu_3 T}{\mu_{30} - \gamma_1 T - \frac{\gamma_2 \mu_1 T}{\mu_{10} - \mu_{11} T}}\quad (4.4)$$

<a id='1a5510c9-c816-4a2c-a1a0-63e16f3abc6a'></a>

Eqs. (4.1a), (4.3), and (4. 4) give

$\alpha - \alpha_0T - \alpha_1T_c - \frac{\delta_2\mu_4}{\mu_{40} + \delta_1T} \times \frac{\mu_3T}{\mu_{30} - \gamma_1T - \frac{\gamma_2\mu_1T}{\mu_{10}-\mu_{11}T}} = 0.$ (4.5)

<a id='30b1fe94-c685-4a88-b7ce-0f01d13a812d'></a>

Eqs. (4.1d) and (4.2) give

$\mu_2 T - \mu_{20} T_c + \beta_1 T T_c + \beta_2 T_c \frac{\mu_1 T}{\mu_{10} - \mu_{11} T} = 0. \quad (4.6)$

<a id='e0b2c9bd-b742-4d56-aa4e-8bb99c507ae5'></a>

We note that isoclines (4.5) and (4.6) involve only two variables $T$ and $T_c$ that we wish to solve.

<a id='78c87fe9-2f89-4732-931b-decf17b90400'></a>

From (4.5) we note the following:
When T = 0, then Tc = α/α1.
When Tc = 0, then we have

<a id='dc976676-8d2f-4076-adef-470bf91f871d'></a>

(α - α₀T)(μ₄₀ + δ₁T) [(μ₃₀ - γ₁T)(μ₁₀ - μ₁₁T) - γ₂μ₁T]
- δ₂μ₃μ₄T (μ₁₀ - μ₁₁T) = 0.

<a id='8a19dc1e-ce60-4f2d-a31b-d7e06827bc24'></a>

Let,
$F(T) = (\alpha - \alpha_0T)(\mu_{40} + \delta_1T)[(\mu_{30} - \gamma_1T)(\mu_{10} - \mu_{11}T) - \gamma_2\mu_1T] - \delta_2\mu_3\mu_4T(\mu_{10} - \mu_{11}T)$.

<a id='3c562290-39aa-4813-b0fb-d3bc34cfef13'></a>

Then we have

$F(0) = \alpha\mu_{10}\mu_{30}\mu_{40} > 0,$

$F\left(\frac{\alpha}{\alpha_0}\right) = -\delta_2\mu_3\mu_4\frac{\alpha}{\alpha_0}\left(\mu_{10} - \mu_{11}\frac{\alpha}{\alpha_0}\right),

<a id='8eb55e2e-a8e8-4e0c-bdeb-ab1b1567fc86'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='28127547-ca48-45d1-b072-2c369cc8aea2'></a>

344 Dubey et al.

<a id='4be71ce5-ea95-4603-879b-1e71c57a1c47'></a>

which is negative if

<a id='349653b6-bc7f-41b2-87a6-dbfa689dd7ba'></a>

$$\mu_{10}\alpha_0 > \mu_{11}\alpha. \quad (4.7a)$$

<a id='1ee23484-0f18-43e0-a3f0-5946d68e689e'></a>

This shows that there exists a $T = \bar{T}$ in the interval $0 < \bar{T} < \alpha/\alpha_0$ such that $F(\bar{T}) = 0$. Further, this $\bar{T}$ is unique if

<a id='762a65cf-07c5-49fe-9ee8-eb54f78cb58b'></a>

F'(T) < 0 for all T ≥ 0.                                       (4.7b)

<a id='daaa50fc-574f-444e-858c-2a414323467e'></a>

Further, from Eq. (4.5) it may be noted that

$\frac{dT_c}{dT} < 0$ if $X(\mu_{10} - 2\mu_{11}T) - T(\mu_{10} - \mu_{11}T)\frac{dX}{dT} > 0$, (4.7c)

<a id='880dd3b9-97b7-45ef-a96b-fbad299fc804'></a>

where
X = (\mu_{40} + \delta_1 T) [(\mu_{30} - \gamma_1 T)(\mu_{10} - \mu_{11} T) - \gamma_2 \mu_1 T].

<a id='0e6ab85f-e276-4c20-b2be-e3de0da07d75'></a>

Now, from Eq. (4.6) we note the following:

<a id='4988e66d-f083-45f9-bd8b-ec8e79732e16'></a>

When T = 0, then T_c = 0.
And

<a id='b5066387-4ddc-402d-9563-11af3cbb4780'></a>

$$\frac{dT_c}{dT} > 0 \text{ if } \mu_{10}\alpha_0 > 2\mu_{11}\alpha, \quad \mu_{20}\alpha_0 > \beta_1\alpha. \quad (4.8a)$$

<a id='800f9237-0216-4e9e-9f59-594e00b80b06'></a>

This shows that the isoclines (4.5) and (4.6) intersect at a unique point ($T^*, T_c^*$) under conditions (4.7a)-(4.7c) and (4.8a). Knowing the values of $T^*$ and $T_c^*$, the values of $T_h^*$, $B^*$, and $A^*$ can then be computed from (4.2), (4.4), and (4.3), respectively. It may be noted that for $T_h^*$ and $B^*$ to be positive, we must have respectively

<a id='2d9e2e72-c8e6-41a3-963c-119f0fe9b148'></a>

μ₁₀ > μ₁₁T* (4.8b)
μ₃₀ > γ₁T* + γ₂Tₕ* (4.8c)

<a id='9c66c5ef-3d24-435f-9a2e-075b2756994e'></a>

Thus, we conclude that the positive equilibrium E* exists if conditions (4.7a)-
(4.7c) and (4.8a)-(4.8c) are satisfied.

<a id='4eb8d11f-7eda-4cfc-a853-8bb5d83cdb86'></a>

**Remark.** It may be noted here that condition (4.7a) is satisfied in the region ̑ defined in Lemma 3.1.

<a id='412b9f02-172b-4bae-a0bd-02917d7d2f62'></a>

In order to study the local stability behavior of the equilibria obtained above, we compute the variational matrices corresponding to each equilibrium. From the variational matrix at the equilibrium E0, we note that E0 is a saddle point with unstable manifold locally in the T-direction and with stable manifold locally in the Th-Tc-B-A space. The local stability behavior of the equilibrium E* is not obvious from the variational matrix computed at E*. However, using Liapunov's stability theory14 we are able to find sufficient conditions for E* to be locally asymptotically stable.

<a id='bd071875-6dde-428d-8780-d6511ef11810'></a>

Theorem 4.1. Let the following inequalities hold:

(δ₂ + k₄δ₁A*)² < ½k₄α₀(μ₄₀ + δ₁T*), (4.9a)

<a id='c11dba67-6ad5-408c-85d6-4f79d0b95b4b'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='2149eeab-a904-4f0e-ac3d-d5497222d280'></a>

Modeling the Interaction 345

<a id='e848d93d-c18e-497c-b1fc-aef6fe8da4e6'></a>

k_2(\beta_2 T_c^*)^2 < \frac{2k_1 \mu_1 \mu_2 T^{*2}}{3T_h^* T_c^*}, (4.9b)

<a id='3eaa1ecf-8be5-4853-bdf7-7b00b3bdfc50'></a>

where $k_i$'s are some positive constants to be chosen such that
$k_1 < \frac{\alpha_0 \mu_1 T^*}{3T_h^*(\mu_1 + \mu_{11}T_h^*)}$, $k_2 = \frac{\alpha_1}{\mu_2 + \beta_1 T_c^*}$

<a id='a9d46bdd-2271-4f06-8c8c-9acc48a52745'></a>

k_3 < \min \left\{ \frac{\alpha_0 \mu_3 T^*}{3B^* (\mu_3 + \gamma_1 B^*)^2}, \frac{4k_1}{9(\gamma_2 B^*)^2}, \frac{\mu_1 \mu_3 T^{*2}}{T_h^* B^*} \right\}

<a id='529fd6ce-7d58-45d6-9dc6-6fa0a4e682d1'></a>

<::transcription of the content
: k_4 < \frac{2k_3\mu_3 T^*}{3\mu_4^2 B^*} (\mu_{40} + \delta_1 T^*).
::>

<a id='d90e02ab-5f4d-47a4-a37c-169c679a2191'></a>

Then E* is locally asymptotically stable (for proof see Appendix A).
Theorem 4.2. Let the following inequalities hold in the region Ω:

<a id='5186bdcd-2003-41bb-b2db-242993069090'></a>

$$(\delta_2 + m_4\delta_1 A_k)^2 < \frac{1}{2}m_4\alpha_0(\mu_{40} + \delta_1 T^*), \quad (4.10a)$$

<a id='03db6ca8-e449-4e29-abde-26965a6fc0f5'></a>

$m_2(\beta_2 T_{ck})^2 < \frac{2m_1 \mu_1 \mu_2 T^{*2}}{3T_h^* T_c^*}$, (4.10b)

<a id='719db4df-6148-4840-b986-ab11181c69bf'></a>

where $m_i$'s are some positive constants to be chosen such that

$m_1 < \frac{\alpha_0 \mu_1 T^*}{3T_h^*}$, $m_2 = \frac{\alpha_1}{\mu_2 + \beta_1 T_{ck}}$,

$m_3 < \min \left\{ \frac{\alpha_0 \mu_3 T^*}{3B^*(\mu_3 + \gamma_1 B_k)^2}, \frac{4m_1}{9(\gamma_2 B_k)^2}, \frac{\mu_1 \mu_3 T^{*2}}{T_h^* B^*} \right\}$,

$m_4 < \frac{2m_3 \mu_3 T^*}{3\mu_4^2 B^*} (\mu_{40} + \delta_1 T^*)$.

<a id='02af3896-d9b2-4e9b-bdc4-d7e789623adb'></a>

Then E* is globally asymptotically stable with respect to all solutions initiating in the interior of the positive orthant. The proof is deferred to Appendix B.

<a id='4b8834d2-67ff-457e-8ae1-0c368d8b7ebb'></a>

## 5. Numerical Simulations
In this section, we present the numerical simulations of the results obtained in the previous sections. We choose the following hypothetical set of values of parameters (other set of values of parameters may also exist) for model system (3.1):

<a id='24b963bd-ce45-4b5c-9427-9a4bbc5b9bdc'></a>

α = 0.18, α₀ = 4.6, α₁ = 0.101, δ₂ = 0.008, μ₁ = 1.5,
μ₁₀ = 0.2, μ₁₁ = 0.01, μ₂ = 1.4, μ₂₀ = 0.0412, β₁ = 0.3, (5.1)
β₂ = 0.05, μ₃ = 0.45, μ₃₀ = 0.03, γ₁ = 0.4, γ₂ = 0.3,
μ₄ = 0.35, μ₄₀ = 0.3, δ₁ = 0.5.

<a id='74527c00-bcb3-4d95-bbc5-459331c6aaf4'></a>

It may be noted that experimental values of parameters α₁, μ₂₀ are taken from Ref. 4, and α, α₀ from Ref. 16.

<a id='f2c233fb-dea2-4484-9995-310ced958bad'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='97d1478e-7f5e-49dd-8ae7-e275ccdc8df7'></a>

346 Dubey et al.

<a id='9c5eb8e5-be9a-45ae-9016-b8af331db382'></a>

For the above set of values of parameters, our computer simulation shows that the positive equilibrium E* of model (3.1) exists, and it is given by

<a id='9fd6a662-aa9c-40a1-97fc-c56eb9e7331f'></a>

T* = 0.0111056, T<sub>h</sub>* = 0.0833382, T<sub>c</sub>* = 0.46134,
B* = 8.98314, A* = 10.2899.
(5.2)

<a id='e4eaa7d1-d04f-4a13-a628-f5c536f7064c'></a>

For the set of values of parameters given in (5.1), it can be checked that conditions (4.9a) and (4.9b) in Theorem 4.1, and conditions (4.10a) and (4.10b) in Theorem 4.2 are satisfied. This shows that the positive equilibrium E* is locally as well as globally asymptotically stable in region Ω defined in Lemma 3.1.

<a id='08885822-c8ea-4d43-9d5a-6f64e8f3d356'></a>

In order to study the effects of interaction parameters (namely, α1, δ2, μ11, β1, β2, γ1, γ2, δ1) on the dynamics of the system, various graphs are plotted with the help of MATLAB. Figures 2–9 are plotted for the set of values of parameters given in (5.1).

<a id='9a8128ac-7fd4-48e7-9885-7ebe1a16264a'></a>

Figure 2 shows the effect of the interaction parameter between cancer cells and $T_c$ cells ($\alpha_1$) on the concentration of cancer cells with respect to time. This figure shows that as a result of this interaction the concentration of cancer cells decreases with respect to time $t$, and finally settles down at its steady state. It may further be noted that the concentration of these cells also decreases as the interaction $\alpha_1$ increases. An increase in the interaction between $T_c$ cells and cancer cells definitely facilitates the lysis of the later as the interaction brings about a better cell to cell

<a id='dbd26959-b679-49a8-abac-c6223d2fe219'></a>

<::The image shows a 2D line graph titled "Density of Cancer Cells vs. Time".

The x-axis is labeled "Time" and ranges from 0 to 4 in increments of 0.5.
The y-axis is labeled "Density of Cancer Cells" and ranges from -1 to 4 in increments of 0.5.

There are three lines plotted on the graph, each representing a different value of the interaction parameter α₁:
- A dotted line represents α₁ = 0.101.
- A solid line represents α₁ = 0.601.
- A dashed-dotted line represents α₁ = 1.101.

All three lines start at a high density (around 4) at Time = 0, rapidly decrease, and then flatten out, approaching 0 as Time increases. The dotted line (α₁ = 0.101) shows a slightly higher concentration of cancer cells compared to the other two lines for Time > 0. The solid line (α₁ = 0.601) is slightly below the dotted line, and the dashed-dotted line (α₁ = 1.101) is the lowest of the three, indicating a faster decrease and lower concentration of cancer cells for higher α₁ values.

Fig. 2. The figure shows the effect of the interaction parameter α₁ on the concentration of cancer cells.
: chart::>

<a id='b0e02334-32af-4e20-8751-4391e2fc5196'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='817f8bae-8aeb-4c9f-b527-3079a9c04de5'></a>

*Modeling the Interaction*

<a id='0001ca49-2654-4a3f-a69b-ca058d609614'></a>

347

<a id='a8ac330a-c38a-4653-9825-06699e765b56'></a>

contact. Moreover, the soluble factors that perforate the cancer cell (e.g., perforin)
can act with optimum efficiency only in the proximity of cancer cells. It is also
known that a single $T_c$ is capable of lysing multiple cancer cells without being
inactivated itself.

<a id='57aefd84-bc72-47eb-9e5b-99aa66fcce04'></a>

Figure 3 shows the effect of the interaction (δ₂) between antibodies and cancer cells on the cancer cell concentration and its effect is similar to that of α₁ on T as explained in Fig. 2. It has been observed that just like the T_c_ cells, the interacting antibodies too succeed in bringing down the level of cancer cells. But the mechanism of action of antibody is totally different. Antibodies do not kill or lyse a cancer cell directly but can initiate or enhance antibody mediated elimination mechanisms like opsonization (enhanced phagocytosis or cell eating), complement activation leading to pore formation in cancer cells and antibody dependent cellular cytotoxicity (ADCC) by natural killer cells. But one or more antibodies may be required for cancer cell neutralization or killing depending on the mechanism of action.

<a id='788885ec-7163-42b8-94f2-eeb1738078d7'></a>

The effect of cancer cell and T-helper cell interaction (µ11) on the T-helper cells has been shown in Fig. 4. From this figure, we note that when T-helper cells come in contact with cancer cells, then the concentration of T-helper cells increases for a short period of time subsequently it starts decreasing and finally obtains a steady state. The initial increase is due to the fact that this interaction stimulates the proliferation of helper T cell, therefore its number increases. It is worth noting that the density of tumor cells also goes down with the increase of the T helper cells

<a id='176ab333-7711-4d50-8c15-35ff75880c30'></a>

<::chart: Line chart showing Density of Cancer Cells versus Time. The x-axis is labeled "Time" and ranges from 0 to 5 in increments of 0.5. The y-axis is labeled "Density of Cancer Cells" and ranges from -1 to 9 in increments of 1. Three lines are plotted, all starting at approximately 8.5 on the y-axis at Time = 0 and rapidly decreasing to a value near 0 as Time increases. The lines then remain stable near 0 for the remainder of the chart. The legend indicates three different values for the interaction parameter δ₂:
- Dotted line: δ₂ = 0.008
- Solid line: δ₂ = 0.8
- Dash-dot line: δ₂ = 1.8
All three lines are nearly indistinguishable, suggesting that the interaction parameter δ₂ has little to no effect on the concentration of cancer cells after an initial rapid decline.
Fig. 3. The figure shows the effect of the interaction parameter δ₂ on the concentration of cancer cells.::>

<a id='15e1895f-048e-4806-9d43-4c7472942128'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com
by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='aa113a80-1495-4d91-8dfd-e98059b96bab'></a>

348 Dubey et al.<::chart: The figure contains two plots. The main plot shows the Density of T Helper cells on the y-axis against Time on the x-axis, ranging from 0 to 30. The y-axis ranges from 0 to 9. There are three curves representing different values of the interaction parameter µ₁₁:
- Dotted line: µ₁₁ = 0.01
- Solid line: µ₁₁ = 0.09
- Dash-dotted line: µ₁₁ = 0.3
All three curves start at a density of approximately 8-9 at Time=0 and decrease over time, approaching 0. The curve for µ₁₁ = 0.01 decreases the slowest, while the curve for µ₁₁ = 0.3 decreases the fastest.

An inset plot is also included, showing the Density of Cancer Cells on the y-axis against Time on the x-axis. The x-axis for the inset plot ranges from 0 to 5, and the y-axis ranges from 0 to 10. A single curve in this plot shows that the density of cancer cells starts around 2.5 at Time=0 and rapidly decreases, approaching 0 within the first unit of time and remaining near 0 thereafter.

Fig. 4. The figure shows the effect of the interaction parameter µ₁₁ on the concentration of T-helper cells. The corresponding graph for the concentration of cancer cells is also shown in the figure.::>

<a id='cd72bf4c-2a77-4eba-bdf2-8edfccb1bae7'></a>

at the same time as shown in the inbox. This is because once the helper T cell is activated it stimulates the effector T_c cells to kill cancer cells and B cells to produce antibodies which again mediated cancer cells killing by antibody dependent cellular cytotoxicity. Subsequently, the number of cancer cells would fall and thus would no longer stimulate the proliferation of helper T cells, and therefore the latter would achieve a steady state at a very low level. This portrays a situation where the immune system is able to efficiently control the cancer cell growth.

<a id='58b6c8ed-bed9-4a8a-ba16-1938b023246c'></a>

Figure 5 shows the behavior of T_c cells when they come in contact with the cancer cells with respect to time t for different values of β_1. This figure shows that when the T_c cells come in contact with the cancer cells, then the concentration of these cells initially increases for some time and then decreases, and it finally settles down at its steady state. It also shows that the number of T_c cells increase as the interaction term β_1 increases. It may be noted that the pattern of response of β_1 is similar to μ_11 but also more amplified as compared to T helper cells (refer to Fig. 4). The initial increase in concentration of T_c cells is brought about indirectly via the T helper cells and not by a direct interaction with cancer cells. The reason for the delay is that the T helper cells after activation mediate the proliferation of T_c cells by secreting cytokines like Interleukin-2 (IL-2). After being acted upon by IL-2, the T_c cells proliferate and mediate cytotoxicity of cancer cells. The amplification is an indication of the ability of a single T helper cell to activate multiple T_c as

<a id='b1c5ab8c-210c-46bc-b597-4c2481336b4f'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com
by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='a909b2b1-8a8c-471a-8e13-4c18783031c6'></a>

Modeling the Interaction 349

<a id='acafdba0-d634-46e0-9217-75294ecc6aec'></a>

<::chart: The figure displays two line graphs. The main graph shows the "Density of Cytotoxic T Lymphocytes" on the y-axis, ranging from 0 to 14, against "Time" on the x-axis, ranging from 0 to 150. Three lines represent different values of β₁: a dotted line for β₁ = 0.08, a solid line for β₁ = 0.3, and a dashed-dotted line for β₁ = 0.8. All three lines show an initial increase in density, peaking around Time = 20, and then a gradual decrease towards zero. The dashed-dotted line (β₁ = 0.8) shows the highest peak density, followed by the solid line (β₁ = 0.3), and then the dotted line (β₁ = 0.08). An inset graph is located in the upper right corner. This inset graph shows the "Density of Cancer cells" on its y-axis, ranging from 0 to 10, against "Time" on its x-axis, ranging from 0 to 5. A single solid line depicts the cancer cell density, which starts at a high value, rapidly decreases, and then levels off near zero after Time = 1. Fig. 5. The figure shows the effect of the interaction parameter β₁ on the concentration of T_c cells. The corresponding graph for the concentration of cancer cells is also shown in the figure.::>

<a id='b320cb4e-b95b-44cc-bcef-9fca58c91ef6'></a>

it secretes enough IL-2. Once the level of cancer cells has fallen down it would
no longer stimulate the T-helper cells. In absence of any activation, the T-helper
cells would not secrete IL-2 thus the T_c cells stop proliferation and their number
gradually declines with time to attain a steady state.

<a id='e21d4f1d-cc43-4c0c-a9f3-e784dbbf59ae'></a>

The effect of interaction (β2) between T-helper cells and cytotoxic T cells on the density of cytotoxic T cells is shown in Fig. 6. It may also be noted that the density of cytotoxic T cells increases for some time and then starts decreasing, and obtains its steady state. This also shows that T_c increases as β2 increases. The reason for this has already been discussed in Fig. 5. Here the effect is due to the direct effect between T_c and T_h cells unlike in Fig. 5 where it was mediated via T_h cells.

<a id='0d4a722a-bd0b-4c6f-8dcc-a611a0e3a3bb'></a>

Figure 7 shows the behavior of B cells when they interact with cancer cells with respect to time t for different values of $\gamma_1$. The effect of cancer cells on interacting with B cell is similar to their effect on $T_c$ cells ($\beta_1$) in Fig. 5. Just like $T_c$ cells the proliferation of B cells is also mediated indirectly via $T_h$ cells and thus shows a delayed time and amplification (as compared to $T_h$). The mechanism of action of B cells against cancer cells differ from $T_c$ cells in the fact that the B cells secrete antibodies into the bloodstream which counter the cancer cells (as already discussed in Sec. 1), whereas $T_c$ cells mediate cancer cell cytotoxicity directly either by cell to cell contact or by secreting paracrine molecules like perforins which act on cancer cells in the immediate vicinity. Similarly a single B cell produces multiple antibodies thus amplifying its affect.

<a id='42028bcd-ad31-47d7-ad6f-b3ba90979719'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='cabf70f0-2d83-4b76-8c88-28e596a3cee6'></a>

350 Dubey et al.
<::chart: The figure contains three plots. The top plot shows the Density of Cytotoxic T Lymphocytes on the y-axis (ranging from 0 to 14) versus Time on the x-axis (ranging from 0 to 150). It displays three curves representing different values of the interaction parameter β₂: a dotted line for β₂ = 0.04, a solid line for β₂ = 0.05, and a dash-dot line for β₂ = 0.06. All three curves show an initial increase in density followed by a decrease over time, with higher β₂ values correlating to higher peak densities. The bottom-left plot shows the Density of T Helper Cells on the y-axis (ranging from 0 to 8) versus Time on the x-axis (ranging from 0 to 30). It features a single curve showing a continuous decrease in density over time. The bottom-right plot shows the Density of Cancer cells on the y-axis (ranging from 0 to 10) versus Time on the x-axis (ranging from 0 to 5). It also features a single curve showing a rapid decrease in density over time. Fig. 6. The figure shows the effect of the interaction parameter β₂ on the concentration of T_c cells when they interact with T-helper cells. The corresponding graph for the concentration of T-helper cells and cancer cells is also shown in the figure.::>

<a id='983e12fd-2253-45e2-a901-e666d03c642d'></a>

<::chart: The main chart shows the 'Density of B Cells' (x 10^4) on the y-axis against 'Time' on the x-axis. Three curves are plotted, representing different values of the interaction parameter $\gamma_1$: a dotted line for $\gamma_1 = 0.6$, a solid line for $\gamma_1 = 0.8$, and a dash-dot line for $\gamma_1 = 1.0$. All curves show an initial increase in B cell density, reaching a peak (around 10 x 10^4 for $\gamma_1 = 0.6$, 11.5 x 10^4 for $\gamma_1 = 0.8$, and 14.5 x 10^4 for $\gamma_1 = 1.0$) before decreasing over time. The peak B cell density increases with increasing $\gamma_1$. The x-axis ranges from 0 to 150, and the y-axis from 0 to 15 x 10^4. An inset chart is present in the upper right corner, showing the 'Density of Cancer cells' on its y-axis against 'Time' on its x-axis. This inset chart displays a single curve that rapidly increases to a peak (around 8-9 units) and then quickly declines to near zero. The inset chart's x-axis ranges from 0 to 5, and its y-axis from 0 to 10. Fig. 7. The figure shows the effect of the interaction parameter $\gamma_1$ on the concentration of B cells when they interact with $T_c$ cells. The corresponding graph for the concentration of cancer cells is also shown in the figure.::>

<a id='9c093a95-7481-45d0-80c0-c2dcd3aec500'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='c6d32b20-ec6a-45b5-aa6f-ee2d740e1f22'></a>

Modeling the Interaction

<a id='56d3cf30-c152-4763-878b-c706572be972'></a>

351

<a id='c90ef3f7-3bd8-499f-8d81-4fd215e0f615'></a>

Figure 8 shows the behavior of B cells when they come in contact with T-helper cells with respect to time *t* for different values of γ₂. Figures 6 and 8 show that effects of β₂ and γ₂ are similar. In both cases the interaction with T-helper cells shows the increases in the concentration of T_c cells and B cells, respectively. The T_h cells release proliferation inducing cytokines like IL-2 to induce this increase in concentration. It may be noted that increase in the concentration of B cells is more in Fig. 6. This could be explained by the fact that the T_c acts directly whereas B cells secrete antibodies which would also have an amplifying affect. Also in Figs. 7 and 8, the concentration of B cells increases as γ₁ and γ₂ increase. Further in both cases, initially the density of B cells increases with respect to time, and then declines to obtains its steady state. But it may be noted that increase in the density of B cells is more in Fig. 7 than that of in Fig. 8. The behavior of B cells is similar to the already observed behavior of CTL. In this case too the T_h (which is activated by cancer cells) stimulates the B cells leading to two different effects. Firstly, the B cells start proliferating leading to an increase in number and secondly there is an increased secretion of antibodies by B cells. These antibodies will indirectly mediate cancer cell killing. With no cancer cell left there is a decreased immune activation and consequent deactivation of T_h, B cells, and antibody production in the same sequence. In Fig. 8 the B cell activation and decline follows a pattern similar to

<a id='b6ba0b84-410c-4169-97f3-3708b0f11cf1'></a>

<::chart: The figure contains three plots. The top plot shows the Density of B cells (x 10^4) versus Time. The x-axis ranges from 0 to 150, and the y-axis from 0 to 12 x 10^4. There are three curves representing different values of the interaction parameter γ₂: a dotted line for γ₂ = 0.28, a solid line for γ₂ = 0.29, and a dash-dot line for γ₂ = 0.30. All curves show an initial increase in B cell density, reaching a peak, and then a gradual decrease over time. The peak density increases with increasing γ₂. The bottom-left plot shows the Density of Cancer Cells versus Time. The x-axis ranges from 0 to 5, and the y-axis from 0 to 10. A single curve shows the density of cancer cells starting high and rapidly decreasing towards zero. The bottom-right plot shows the Density of T Helper Cells versus Time. The x-axis ranges from 0 to 30, and the y-axis from 0 to 8. A single curve shows the density of T Helper Cells starting high and gradually decreasing towards zero.:>
Fig. 8. The figure shows the effect of the interaction parameter γ₂ on the concentration of B cells when they interact with T-helper cells. The corresponding graph for the concentration of cancer cells as well as T-helper cells is also shown in the figure.

<a id='5dd9377b-fcfd-4f4c-8fd5-1337493e0c1e'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='b10e6d28-0973-4ba3-9798-5ae1ad1a3c20'></a>

352 Dubey et al.

<a id='9d05441e-9c5c-42ba-a83d-e2a49320edf3'></a>

Fig. 7 except that the level is lower. This decline in level can be due to indirect impact of cancer cells on B cells via Th cells. Just like earlier, the cancer cells initially stimulated Th and consequently B cells and its death leads to deactivation of both the above cells.

<a id='a490843c-3d75-42e0-a816-b1262a5b9b3d'></a>

Figure 9 shows the effect of d₁ on the concentration of antibody with respect to time t. It may also be noted that when antibody interacts with cancer cells, then the concentration of antibody increases for some time and decreases for a relatively longer period, and finally settles down at is steady state. We also note that A decreases as δ₁ increases. The level of antibody depends upon the level of B cells present in the system. The B cells (as explained earlier in Figs. 7 and 8) depend on level of T-helper cells and status of immunoactivation in presence of cancer cells. Also more the interaction between antibodies and cancer cells more will be the lysis of latter mediated by mechanisms already described. In the process the antibody is also consumed therefore its level later declines. A final steady state is achieved when all the cancer specific antibodies have been consumed and there is no specific synthesis of antibodies by B cells. This would happen when the cancer cells are no longer present to activate the helper T cells thus also the B cells.

<a id='b4fdb624-ae69-4b6f-86db-d360f5cb828e'></a>

It is a well-understood fact that many immunodeficiency diseases like AIDS are marked by an increase incidence of cancer due to inability of T cells and B cells to function and interact in the normal manner (due to viral infection of the helper

<a id='cd5080ca-a8c9-4404-a9a7-68425b186818'></a>

<::chart: A composite plot showing two graphs. The main graph displays the 'Concentration of Antibodies' (y-axis, from 0 to 14 x 10^4) versus 'Time' (x-axis, from 0 to 150). It contains three curves, each representing a different interaction parameter δ₁:
- Dotted line: δ₁ = 0.5
- Solid line: δ₁ = 50.5
- Dashed-dotted line: δ₁ = 300.5
All three curves show an initial increase, peak around Time 30-40 (with peak concentration around 12 x 10^4), and then a gradual decrease. The dashed-dotted line (δ₁ = 300.5) shows the highest peak, followed by the solid line (δ₁ = 50.5), and then the dotted line (δ₁ = 0.5).

An inset graph is located in the upper right corner, showing 'Density of Cancer Cells' (y-axis, from 0 to 10) versus 'Time' (x-axis, from 0 to 5). This curve starts at a density of approximately 2 at Time 0 and rapidly decreases to near 0 within the first unit of Time, remaining close to zero thereafter.::>

Fig. 9. The figure shows the effect of the interaction parameter δ1 on the concentration of antibodies when they interact with Tc cells. The corresponding graph for the concentration of cancer cells is also shown in the figure.

<a id='da9e8e8c-5715-4003-9380-c8164f3e3c7a'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='5be2bb38-d37a-4bc8-ac0c-1da7561b7f1b'></a>

Modeling the Interaction

<a id='7557f181-aa65-4a9c-a77a-fdc6700e9e37'></a>

353

<a id='e167346a-0d1b-414a-8aa5-9889b70af083'></a>

T cells thus faulty immunoregulatory mechanisms). Furthermore, the potency of immune system can be increased using various immunopotentiating modalities like cytokine therapy, drug tagged monoclonal antibodies (immunotoxins), anti-idiotypic antibodies, production of Lymphokine Activated Killer (LAK) cells, and Tumor Infilterating Lymphocytes (TILs). 13

<a id='20f4c367-b9d4-42fe-bd55-965c3f997da2'></a>

## 6. Conclusions

In this paper, we have considered the interaction between cancer cells and immune system, which includes T-helper cells, T-cytotoxic cells, B cells, and antibodies. Analysis of the mathematical model suitably exemplifies the biological interaction. Stability analysis reveals that the system is asymptotically stable, both locally and globally. The system is then tested numerically with hypothetical data. In the numerical section we have mainly shown the effects of the interaction parameters (namely, α₁, δ₂, μ₁₁, β₁, β₂, γ₁, γ₂, and δ₁) on the dynamics of the system. It is mathematically revealed that T cytotoxic cells and antibodies play an important role in bringing down the concentration of cancer cells. This suggests proper activation of the system parameters in the conditions obtained, namely, α₁, δ₂, which are the rates at which T_c and antibodies destroy cancer cells. A further analysis of this system would be testing the proposed model with experimental data/reallife data, which we propose as our future research work.

<a id='d4a597da-37f0-4431-9de9-5609d7a885da'></a>

Acknowledgments
The authors are grateful to the anonymous referees for their valuable comments to
improve the paper.

<a id='f30faf5a-3502-4692-b9dd-1ebb3bf1c95e'></a>

## References

1. WHO, Cancer, World Health Organization, 2006, Retrieved on 2007-06-25, http://www.who.org/.
2. Adam J, Bellomo N, *A Survey of Models for Tumor-Immune System Dynamics*, Birkhäuser, Boston, MA, 1996.
3. Preziosi L, From population dynamics to modeling the competition between tumors and immune system, *Math Comput Model* **23**(6):135-152, 1996.
4. Kuznetsov V, Taylor M, Nonlinear dynamics of immunogenic tumors: parameter estimation and global bifurcation analysis, *Bull Math Biol* **56**(2):295-321, 1994.
5. Kirschner D, Panetta J, Modeling immunotherapy of the tumor-immune interaction, *J Math Biol* **37**:235-252, 1998.
6. Kolev M, Mathematical modeling of the competition between tumors and immune system considering the role of the antibodies, *Math Comput Model* **37**:1143-1152, 2003.
7. Arciero JC, Jackson TL, Kirschner DE, A mathematical model of tumor immune evasion and siRNA treatment, *Disc Cont Dyn Syst Ser B* **4**(1):39-58, 2004.

<a id='3dac6322-1f21-4aec-a1b5-40d8b8159aff'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='987d6413-4032-47a8-b24c-871c273e1d5d'></a>

354 Dubey et al.

<a id='d60d501d-8539-4345-b39e-35feb7d55746'></a>

8. Matzavinos A, Chaplain MAJ, Travelling-wave analysis of a model of the immune response to cancer, *C R Biol* **327**:995-1008, 2004.
9. Sarkar R, Banerjee S, Cancer self remission and tumor stability --- a stochastic approach, *Math Biosci* **196**:65-81, 2005.
10. Dubey US, Dubey B, A mathematical model for the effect of toxicant on the immune system, *J Biol Syst* **15**(4):473-493, 2007.
11. Roose T, Chapman SJ, Maini KP, Mathematical models of avascular tumor growth, *SIAM Rev* **49**(2):179-208, 2007.
12. Bellomo N, Preziosi L, Forni G, On a kinetic (cellular) theory of the competition between tumors and the immune host system, *J Biol Syst* **4**(4):479-502, 1996.
13. Darlene EJ, Yoko O, Yvette SH, Shang-Fan Y, Joan D, Tony P, Pamela RC, Bio-luminescent imging (BLI) to improve and refine traditional murine models of tumor growth and metastasis, *Clin Exp Metastasis* **20**(8):733-744, 2003.
14. Hoffman R, Green fluorescent protein imaging of tumour growth angiogenesis in mouse models, *Lancet Oncol* **3**(9):546-556, 2002.
15. Goldsby RA, Kindt TJ, Osborne BA, Kuby J, *Immunology*, Freeman & Co., 2003, pp. 499-522.
16. Siu H, Vitetta ES, May RD, Uhr IW, Tumor dormancy: regression of BCL₁ tumor and induction of a dormant tumor state in mice chimeric at the major histocompatibility complex, *J Immunol* **137**:1376-1382, 1986.
17. LaSalle J, Lefschetz S, *Stability by Liapunov's Direct Method with Applications*, Academic Press, New York, London, 1961.

<a id='d323fc3d-6367-4010-a548-c08df6f61719'></a>

## Appendix A: Proof of Theorem 4.1

In order to prove Theorem 4.1, we first linearize model (3.1) by considering the following transformations:

<a id='021921b6-f2bd-4be7-9d9c-05e9f616eed5'></a>

T = T* + τ,
T_h = T_h* + τ_h,
T_c = T_c* + τ_c,
B = B* + b,
A = A* + a,

<a id='bf69cdcb-8562-4837-a456-139cf3e72889'></a>

where $\tau$, $\tau_h$, $\tau_c$, $b$, $a$ are small perturbations about $E^*$.
Now, we consider the following positive definite function:

<a id='808dd19b-9a9d-4e86-875b-a1df00cc2927'></a>

V = \frac{1}{2T*} \tau^2 + \frac{1}{2}k_1\tau_h^2 + \frac{1}{2}k_2\tau_c^2 + \frac{1}{2}k_3b^2 + \frac{1}{2}k_4a^2,

<a id='c86e3dd2-c6b8-415c-ad5c-a1f4a24a8a8b'></a>

where $k_i$'s are some positive constants as defined in Theorem 4.1.
Differentiating $V$ with respect to $t$ along the linearized version of model (3.1),
a little algebraic manipulation yields,

<a id='52611aa9-44e3-4f33-8a2f-2b722b10f258'></a>

$$\frac{dV}{dt} = -\frac{1}{2}a_{11}\tau^2 + a_{12}\tau\tau_h - \frac{1}{2}a_{22}\tau_h^2 - \frac{1}{2}a_{11}\tau^2 + a_{13}\tau\tau_c - \frac{1}{2}a_{33}\tau_c^2 \\ \quad -\frac{1}{2}a_{11}\tau^2 + a_{14}\tau b - \frac{1}{2}a_{44}b^2 - \frac{1}{2}a_{11}\tau^2 + a_{15}\tau b - \frac{1}{2}a_{55}a^2 \\ \quad -\frac{1}{2}a_{22}\tau_h^2 + a_{23}\tau_h\tau_c - \frac{1}{2}a_{33}\tau_c^2 - \frac{1}{2}a_{22}\tau_h^2 + a_{24}\tau_h b - \frac{1}{2}a_{44}b^2 \\ \quad -\frac{1}{2}a_{44}b^2 + a_{45}ba - \frac{1}{2}a_{55}a^2, \quad (A.1)$$

<a id='54198197-e170-4ee1-a8e2-83f8f0b99f43'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='0d16f3f6-d4c7-4e00-bc27-369eaa4d78dc'></a>

Modeling the Interaction 355

<a id='efb86545-943f-4749-b311-1de23f2255f5'></a>

where
$a_{11} = \frac{1}{2}\alpha_0,$
$a_{22} = \frac{2k_1\mu_1T^*}{3T_h^*},$
$a_{33} = \frac{k_2\mu_2T^*}{T_c^*},$
$a_{44} = \frac{2k_3\mu_3T^*}{3B^*}$
$a_{55} = k_4(\mu_{40} + \delta_1T^*),$
$a_{12} = k_1(\mu_1 + \mu_{11}T_h^*),$
$a_{13} = -\alpha_1 + k_2(\mu_2 + \beta_1T_c^*),$
$a_{14} = k_3(\mu_3 + \gamma_1B^*),$
$a_{15} = -\delta_2 - k_4\delta_1A^*,$
$a_{23} = k_2\beta_2T_c^*,$
$a_{24} = k_3\gamma_2B^*,$
$a_{45} = k_4\mu_4.$

<a id='15d988d8-165c-4922-9b97-00f75f228e7d'></a>

Sufficient conditions for $\frac{dV}{dt}$ to be negative definite are that the following inequalities hold:

$a_{12}^2 < a_{11}a_{22}$, (A.2a)
$a_{13}^2 < a_{11}a_{33}$, (A.2b)
$a_{14}^2 < a_{11}a_{44}$, (A.2c)
$a_{15}^2 < a_{11}a_{55}$, (A.2d)
$a_{23}^2 < a_{22}a_{33}$, (A.2e)
$a_{24}^2 < a_{22}a_{44}$, (A.2f)
$a_{45}^2 < a_{44}a_{55}$. (A.2g)

<a id='da44b197-0531-4213-b9eb-25df503a08f8'></a>

By choosing the constants k_l's suitably as defined Theorem 4.1, we note that conditions (A.2a), (A.2b), (A.2c), (A.2f), and (A.2g) are automatically satisfied. Further, (4.9a) ⇒ (A.2d), (4.9b) ⇒ (A.2e). This proves the theorem.

<a id='f1d5e860-6e0d-4c39-8d78-f4f0184aea41'></a>

Appendix B: Proof of Theorem 4.2
Consider the following positive definite function about the positive equilibrium E*,

$W(t) = T - T^* - T^* \ln \left(\frac{T}{T^*}\right) + \frac{1}{2}m_1(T_h - T_h^*)^2 + \frac{1}{2}m_2(T_c - T_c^*)^2$

$+ \frac{1}{2}m_3(B - B^*)^2 + \frac{1}{2}m_4(A - A^*)^2,$ (B.1)

<a id='292ccdf4-5f98-41f4-9363-908c2d26c0a2'></a>

where $m_i$'s are positive constants chosen suitably as in Theorem 4.2.
Differentiating $W$ with respect to time $t$ along the solutions of model (3.1) and
after some algebraic manipulations, we get

<a id='dfd01111-b2f1-4315-b24f-2143e5502741'></a>

$$\frac{dW}{dt} = -\frac{1}{2}b_{11}(T - T^*)^2 + b_{12}(T - T^*)(T_h - T_h^*) - \frac{1}{2}b_{11}(T_h - T_h^*)^2$$
$$- \frac{1}{2}b_{11}(T - T^*)^2 + b_{13}(T - T^*)(T_c - T_c^*) - \frac{1}{2}b_{33}(T_c - T_c^*)^2$$
$$- \frac{1}{2}b_{11}(T - T^*)^2 + b_{14}(T - T^*)(B - B^*) - \frac{1}{2}b_{44}(B - B^*)^2$$

<a id='3120ffd8-ee99-49c3-9d3a-ac5279bc296d'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.

<!-- PAGE BREAK -->

<a id='df88cd67-9b16-40b4-8086-91a081cad8ff'></a>

356 Dubey et al.

<a id='9f5a6175-1338-4e51-9d9a-44ef0ea7f6a9'></a>

$$-\frac{1}{2} b_{11}(T - T^*)^2 + b_{15}(T - T^*)(A - A^*) - \frac{1}{2} b_{55}(A - A^*)^2$$ $$\label{eq:1} -\frac{1}{2} b_{22}(T_h - T_h^*)^2 + b_{23}(T_h - T_h^*)(T_c - T_c^*) - \frac{1}{2} b_{33}(T_c - T_c^*)^2$$ $$\label{eq:2} -\frac{1}{2} b_{22}(T_h - T_h^*)^2 + b_{24}(T_h - T_h^*)(B - B^*) - \frac{1}{2} b_{44}(B - B^*)^2$$ $$\label{eq:3} -\frac{1}{2} b_{44}(B - B^*)^2 + b_{45}(B - B^*)(A - A^*) - \frac{1}{2} b_{55}(A - A^*)^2,$$

<a id='f60c1b9e-06a1-4ee2-b753-cc3f0aa9e996'></a>

where

<a id='f18709af-cb31-47bc-b4b7-98ba33f1744d'></a>

b11 = (1/2)α0, b22 = (2m1μ1T*)/(3T_h*), b33 = (m2μ2T*)/(T_c*), b44 = (2m3μ3T*)/(3B*),

<a id='586cbde5-abbf-4d03-92bb-28f283945134'></a>

b_55 = m_4(\mu_{40} + \delta_1 T^*), b_{12} = m_1(\mu_1 + \mu_{11}T_h), b_{13} = -\alpha_1 + m_2(\mu_2 + \beta_1 T_c),

<a id='11844e08-e245-4107-bf1a-de1bddc99dce'></a>

b₁₄ = m₃(μ₃ + γ₁B),
b₁₅ = -δ₂ - m₄δ₁A,
b₂₃ = m₂β₂Tₒ,

<a id='b1f6376b-d3e2-4820-b0c0-978e78581ec4'></a>

$$b_{24} = m_3\gamma_2B, \quad b_{45} = m_4\mu_4.$$

<a id='6ac3b657-b5e2-4a87-aef1-153fc0165a61'></a>

Sufficient conditions for dW/dt to be negative definite are that the following inequalities hold:

<a id='51e25a9d-5b83-4888-b614-24b1c926acea'></a>

b^2_{12} < b_{11}b_{22}, (B.2a)
b^2_{13} < b_{11}b_{33}, (B.2b)
b^2_{14} < b_{11}b_{44}, (B.2c)
b^2_{15} < b_{11}b_{55}, (B.2d)
b^2_{23} < b_{22}b_{33}, (B.2e)
b^2_{24} < b_{22}b_{44}, (B.2f)
b^2_{45} < b_{44}b_{55}. (B.2g)

<a id='96645836-5324-4935-a6ed-8c7031daccd5'></a>

By choosing the constants mi's suitably as defined in Theorem 4.2, we note that conditions (B.2a), (B.2b), (B.2c), (B.2f), and (B.2g) are automatically satisfied. Further, (4.10a) ⇒ (B.2d), (4.10b) ⇒ (B.2e). This shows that W is a Liapunov's function¹⁷ with respect to E* whose domain contains the region of attraction Ω, proving the theorem.

<a id='8bedc119-fdc7-4630-a507-7796749b973d'></a>

J. Biol. Syst. 2008.16:337-356. Downloaded from www.worldscientific.com by UNIVERSITY OF TRENTO on 12/30/25. Re-use and distribution is strictly not permitted, except for Open Access articles.
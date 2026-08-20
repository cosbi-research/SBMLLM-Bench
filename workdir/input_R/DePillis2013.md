<a id='93ab450f-ccbf-4dea-9d9c-f04f05a0655f'></a>

DISCRETE AND CONTINUOUS
DYNAMICAL SYSTEMS SERIES B
Volume 18, Number 4, June 2013

<a id='800ae0c0-3255-43b1-9869-3a1cd5228d8e'></a>

doi:10.3934/dcdsb.2013.18.915

<a id='983c62c5-34cb-4e3f-82b7-d084271d9407'></a>

pp. 915–943

<a id='919cdb2b-00e6-4b39-a3db-6588aff7c04f'></a>

MATHEMATICAL MODELING OF REGULATORY T CELL
EFFECTS ON RENAL CELL CARCINOMA TREATMENT

<a id='664f6f90-86eb-4603-a1a6-9c82dfb82fe6'></a>

LISETTE DE PILLIS
Department of Mathematics, Harvey Mudd College
Claremont, CA 91711 USA

TREVOR CALDWELL, ELIZABETH SARAPATA AND HEATHER WILLIAMS
Harvey Mudd College
Claremont, CA 91711, USA

<a id='69171a82-c185-46ce-95bf-482644a02588'></a>

ABSTRACT. We present a mathematical model to study the effects of the regulatory T cells (Treg) on Renal Cell Carcinoma (RCC) treatment with sunitinib. The drug sunitinib inhibits the natural self-regulation of the immune system, allowing the effector components of the immune system to function for longer periods of time. This mathematical model builds upon our non-linear ODE model by de Pillis et al. (2009) [13] to incorporate sunitinib treatment, regulatory T cell dynamics, and RCC-specific parameters. The model also elucidates the roles of certain RCC-specific parameters in determining key differences between _in silico_ patients whose immune profiles allowed them to respond well to sunitinib treatment, and those whose profiles did not.

<a id='ba369102-6f98-47d0-97bc-1fa11d771b59'></a>

Simulations from our model are able to produce results that reflect clinical outcomes to sunitinib treatment such as: (1) sunitinib treatments following standard protocols led to improved tumor control (over no treatment) in about 40% of patients; (2) sunitinib treatments at double the standard dose led to a greater response rate in about 15% the patient population; (3) simulations of patient response indicated improved responses to sunitinib treatment when the patient's immune strength scaling and the immune system strength coefficients parameters were low, allowing for a slightly stronger natural immune response.

<a id='35389067-b765-4863-ade2-2c4ac67f3bd4'></a>

1. Introduction. Immunotherapy has recently taken center-stage in the develop-ment of multi-faceted treatment approaches used to combat certain forms of cancer. One such cancer is renal cell carcinoma (RCC), which has been particularly resistant to most traditional forms of cancer treatment, such as chemotherapy and radiation therapy [51]. The resiliency of RCC has spawned the search for new treatment meth-ods that can effectively harness the natural power of the immune system. There has been limited success with some immunotherapies, such as high-dose interleukin-2 (IL-2), which is a natural cytokine (a signaling protein used by immune cells for communication) that acts as a growth factor for various immune cells [1]. Despite the promise of reproducible trials using IL-2 therapy, the overall response rates (at least a 30% decrease in tumor size, as defined by the Response Evaluation Criteria for Solid Tumors) have not been overwhelmingly positive, usually falling between 5% and 20% [53, 17]. However, sunitinib malate (SUT), a novel tyrosine kinase inhibitor, has been used to a greater degree of success, with response rates between

<a id='66823362-c513-46d6-ae86-9960131a1bce'></a>

2010 _Mathematics Subject Classification._ Primary: 92C50; Secondary: 92C37, 97M10, 97M60.
_Key words and phrases._ Renal cell carcinoma, regulatory T cells, sunitinib, immune system,
mathematical modeling.

<a id='166b2268-a837-4fce-8c65-17511ffb1c0a'></a>

915

<!-- PAGE BREAK -->

<a id='c6fce391-29cb-4ffe-bf4e-4319b55ff7e3'></a>

916

<a id='005808d2-9d0f-40c4-9d6d-bf92d42c8fcf'></a>

L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='040fb6fb-6392-454e-88cf-26c0919aabcb'></a>

30% and 40% [31, 53]. Sunitinib was designed to inhibit growth receptors im-portant for tumor growth and angiogenesis [24, 63]. However, there is now strong evidence that in addition to its antiangiogenic effects, sunitinib may directly inhibit the immunosuppressive environment through reducing the number of regulatory T cells (Treg) in patients [25, 63, 6]. Regulatory T cells (Treg cells) are responsible for the inhibition of other immune cells, such as effector CTL cells (cytotoxic T lym-phocytes). Treg function is critical to preventing autoimmune disease. However, it is also the case that Treg suppression of effector immune cell activity may be playing a role in reducing the effectiveness of some immunotherapies. In fact, according to [19], one important mechanism by which RCCs evade immune destruction is through active recruitment of immunosuppressive cells such as Tregs. Some studies have noted that RCC patients have increased numbers of Tregs in both peripheral blood and tumors. This is important, since these increased numbers of Tregs are inversely correlated to overall survival [62, 11, 30, 25]. The significance of Treg levels in the prognosis of an RCC patient is a motivator for focusing our attention on mathematically modeling the action of Tregs in an RCC system, as well as the effect that sunitinib has on suppressing Treg activity. Therefore, although the an-tiangiogenic properties of sunitinib are certainly of interest, we choose to focus our attentions on modeling the Treg suppressive effects of sunitinib alone. In particular, patient specific Treg levels in the peripheral blood are relatively easy to measure, as compared to degree of vascularization or number of growth receptors present in the tumor tissue itself. Patient trials in which patient-specific Treg data are collected may then benefit from the insights the model we present may provide.

<a id='b1334265-8346-476a-b89c-f745f314e8ef'></a>

Theoretically, the combination of sunitinib with immunotherapy should boost the efficacy of immune cells without the inhibition from T$_{reg}$ cells, maximizing the ability of the immune system to fight off a tumor. However, in order to find how to best maximize the effectiveness of the immune system, we must first understand the complex dynamics of the interactions between various immune cells and tumor cells. Our aim in this work is to gain insight into these dynamics via a mathematical model employing a system of nonlinear ordinary differential equations.

<a id='cafc718c-a8a8-4b1e-bd3f-cbc098917864'></a>

Some recent cancer modeling endeavors have incorporated a multi-scale approach in order to connect dynamics of complex biological interactions on various scales. These can include the molecular scale and gene expression (see, e.g., [56, 26]), the cellular scale that incorporates cell-cell signaling and interactions (as does the model we present in this paper), and the macroscopic scale that includes tissue models. Multiscale work that incorporates two or more of these scales within one model can be found in, for example, [5]. Some helpful reviews and overviews of the multi-scale modeling approach can be found in [64, 10, 18]. We do not take an explicitly multiscale approach in this paper, however. Our interest in this case is in gaining qualitative insight into the effect regulatory T cells have on the tumor-immune dynamic. Following the philosophy that a model should be as simple as possible while still capturing the behavior of interest, we therefore choose to focus on just the cellular scale. Relatively simple cellular scale models can be quite powerful. As was done in, for example, [42], the authors present a prostate cancer immunotherapy model that takes a cellular scale approach. This cellular scale patient specific model yields results that closely reflect clinical data and that can provide powerful predictive information on various treatment approaches. Future work may call for the addition of more scales in the model, but whether and how these are incorporated will be driven by the questions we wish to address. Although not many

<!-- PAGE BREAK -->

<a id='67cde84a-9ef1-422e-bcc9-211fb77d38d0'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 917

<a id='0bb7228b-bf51-45eb-923a-33b9ee8638f4'></a>

mathematical models of RCC have yet been developed, Leon et al. have created a non-multi-scale two-compartment general tumor-Treg interaction model [45, 46] that includes a lymph node compartment and a tumor compartment. The model populations include a general solid tumor, effector cells, regulatory T cells and anti-gen presenting cells. The authors explore the effect of a variety of parameter ranges on model dynamics, and find that their model allows for two classes of tumors: one class that induces the expansion of effector T cells that is greater than Treg expansion, and one class that induces expansion of both effector and regulatory T cells at similar rates. In both cases they find that tumor growth without treatment intervention within the parameter ranges chosen is not controlled by the effector T cells. However, in [46] they extend their model explorations to include a variety of treatment protocols, including surgery and vaccination. In contrast to an explo-ration of general tumor-Treg dynamics, our model is somewhat more focused. We have chosen model components and parameters specifically to reflect the dynamics of RCC. Our aim is to develop a mathematical model that qualitatively reflects clinical RCC observations, and that may provide some insight into patient-specific responses to treatments.

<a id='2e7f4319-5ba4-4d0b-85bb-327e9d8bba18'></a>

The model we present can be viewed as an extension and modification of the model created by de Pillis et al. [13]. As with the de Pillis et al. model, our state variables include a tumor cell population, the concentration of natural killer (NK) cells, activated cytotoxic CD8$^+$ T cells, circulating lymphocytes, and the concentration of endogenous IL-2 per liter of blood. In this work, our primary goal is to examine the effects of regulatory T cells (T$_{reg}$ cells), which mediate the immune response against a tumor by suppressing other immune cells. To this end, we extend the model of [13] to include regulatory T cell (T$_{reg}$) dynamics, sunitinib treatment, and RCC-specific parameters both for tumor growth, immune interactions, and response to RCC-specific treatment with sunitinib. To the best of our knowledge, this is the first mathematical model that attempts to study the effects of the regulatory T cells on renal cell carcinoma with sunitinib treatment. We have chosen to focus on the effects that sunitinib has on depleting the number of T$_{reg}$ cells rather than the direct inhibition of tumor growth factor receptors.

<a id='1bd2c25c-d5c0-4c9e-a02a-5539d10f3d86'></a>

In section 2, we present the full system of differential equations, along with explanations for each term in the equations. In section 3 we examine biological homeostasis values for a zero-tumor and high-tumor state. In section 4 we provide derivations and explanations of parameter values used in the model. In section 5 we present model analysis and simulation results. In particular, in sections 5.1 and 5.2 we present model validation both without and with treatment intervention through comparison with published laboratory clinical data. In section 5.3 we explore the results of hypothetical treatment strategies through model simulations. In section 5.4, we perform a sensitivity analysis on the model parameters to determine which parameters have the greatest impact on model outcomes. Finally, in sections 6 and 7 we discuss the significance of our results and suggest future directions for mathematical modeling of RCC growth and treatment.

<a id='bff33d8a-94ae-45a3-a818-b48471aa2cc1'></a>

2. The mathematical model. We present the full ODE system with a detailed derivation of the governing equations for each state variable. Our RCC model builds upon our earlier model in de Pillis et al. [13], extending it to include regulatory T cells, new treatments, and parameters adjusted to fit specifically with renal cell carcinoma.

<!-- PAGE BREAK -->

<a id='12009f99-4c66-4085-a97f-30c2a294c242'></a>

918 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='773c858c-d131-45b6-9f66-3069ef816e96'></a>

The new RCC model considers six cell populations, endogenous IL-2 and the sunitinib concentration, and is defined as follows:

* T(t): the total (cells) tumor cell population in number of cells
* N(t): the concentration (cells/L) of Natural Killer (NK) cells per liter of blood
* L(t): the concentration (cells/L) of CD8+ T cells per liter of blood
* R(t): the concentration (cells/L) of CD4+CD25+ regulatory T (Treg) cells per liter of blood
* C(t): the concentration (cells/L) of lymphocytes per liter of blood, not including NK cells, CD8+ T cells, and regulatory T (Treg) cells
* I(t): the concentration (IU/L) of IL-2 per liter of blood
* S(t): the concentration (mg/L) of sunitinib per liter of blood
* vS(t): the amount of sunitinib injected per day per liter of body volume (in mg/L per day)

<a id='b7479dba-c3f2-4fc2-bf5b-b2250a105cc3'></a>

Our model consists of the following ODEs:

<a id='90712f2e-97c5-435e-a02f-63d3721a2744'></a>

dT/dt = aT (1 - bT) - ce^(-λ_T R NT) - DT (1)
dN/dt = f ((e/f)C - N) - pNT + p_N NI / (g_N + I) (2)

<a id='1622900b-20dd-4a0e-95d2-4c6094c93601'></a>

$$\frac{dL}{dt} = -mL - qLT + (r_1N + r_2C) T + \frac{p_ILI}{g_I + I} - \frac{zL^2RI}{\kappa + I} + j\frac{T}{k+T}L \quad (3)$$

<a id='b26dbd19-79af-4991-a41a-2a1f6a5bce3f'></a>

$$\frac{dR}{dt} = u\left(\frac{w}{u}C - R\right) + \frac{p_R RI}{g_R + I} - H_R(1 - e^{-\lambda_R S})R \quad (4)$$

$$\frac{dC}{dt} = \beta\left(\frac{\alpha}{\beta} - C\right) \quad (5)$$

$$\frac{dI}{dt} = -\mu_I I + \phi C + \frac{\omega LI}{\zeta + I} \quad (6)$$

$$\frac{dS}{dt} = -\eta S + v_S(t), \quad (7)$$

<a id='0f3b6b9b-12a1-48e4-a36a-52a54db12379'></a>

where

<a id='ab91d836-06a6-49a5-9f2c-55671ea8f548'></a>

$$D = d \frac{\left(\frac{L}{T}\right)^l}{s + \left(\frac{L}{T}\right)^l} \quad (8)$$

<a id='dd9772eb-b439-4c88-bdfc-c5168ef5a776'></a>

The dynamics of the populations of tumor cells (T), natural killer cells (N),
CD8+T cells (L), circulating lymphocytes (C), and endogenous IL-2 (I), generally
follow the dynamics developed in de Pillis et al. [13]. In addition, in this RCC model
we introduce the effects of regulatory T cell dynamics and sunitinib treatment.
These effects are included through the new term $ce^{-\lambda_T R}NT$ in equation (1), the
new term $\frac{zL^2RI}{\kappa+I}$ in equation (3), and the new equations (4) and (7) representing
$T_{reg}$ and sunitinib dynamics, respectively. Table (1) provides an overview with a
brief description of each model term. We now present a detailed explanation of each
model term.

<a id='203104fd-323b-4690-9bcb-30c1b76c8fe3'></a>

In equation (1), the first term represents logistic tumor growth. Intrinsic growth laws can vary, depending on tumor type, host type, and so forth, but we have found that the use of the logistic growth law provides sufficient flexibility to achieve

<!-- PAGE BREAK -->

<a id='7228278e-4bb7-4eef-b00d-96e5c2e1a157'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 919

<a id='4e28058b-d067-4ba7-b138-72171ffbeb8d'></a>

reasonable fits to tumor growth data. The last term in this equation, $DT$, represents
CD8+T cell induced tumor death, where $D$ is defined in equation (8). This form
of term $D$ is supported by cell lysis experiments that indicate that percent lysis
is a function of the ratio of CD8+T cells to tumor cells. Further justification and
background can be found in [16] and [15].

<a id='78f02a8f-ff8e-43ce-a702-9822d5a5d592'></a>

Treg activity affects tumor cell dynamics. The Treg effect on tumor growth is included in this model through the term $ce^{-\lambda_T R}NT$, which represents the rate of NK-induced tumor death. Trzonkowski et al. [66] found that the cytotoxic effect of NK cells was suppressed when cultured with CD4$^+$CD25$^+$ regulatory T cells. However, the number of conjugates formed between NK cells and target cells did not noticeably decrease, suggesting that the effectiveness of NK-induced tumor death decreases in the presence of Treg cells. We choose an exponential term to allow NK cells to kill tumor cells at the maximal rate $c$ without any regulatory cells in the immune system and so that the kill rate stays strictly positive.

<a id='67a124db-b8df-4390-955e-2a016ace6da4'></a>

Equation (2) is similar to the equation for NK cell growth discussed in [13]. The first term, $eC$, represents baseline NK cell production from circulating lymphocytes. The second term, $-fN$, represents natural cell death. The first two terms are written with $f$ as a constant multiplier to highlight the fact that the constant $e/f$, which denotes the average baseline fraction of circulating lymphocytes that are NK cells, can be found [1]. Inactivation of cytolytic potential occurs when an NK or CD8+T cell has interacted with tumor cells several times and ceases to be effective. The mass-action term $-pNT$ represents this inactivation of NK cells by tumor cells, as presented in [16]. The final term, $\frac{pNNI}{gN+I}$, represents IL-2-induced NK cell proliferation. NK cells express the IL-2R$\beta\gamma_c$IL-2 receptor, and IL-2 binding stimulates NK cell proliferation [1]. Although the enzyme dissociation constant $k_d$ for this binding is sufficiently large that IL-2-stimulated NK cell proliferation is minimal in healthy individuals, it has been shown that additional IL-2 can more than double the NK cell population [50]. Consequently, in the presence of elevated serum IL-2, as can occur with some cancer cases, this interaction may be important [22, 54], and is therefore included in the model.

<a id='8fc0c904-681f-44d9-89e7-b7db6c0b37c1'></a>

In equation (3), the term $-mL$ represents CD8$^{+}$ cell turnover, as in de Pillis et al. [14]. There is no intrinsic growth term since activated CD8$^{+}$T cells are assumed not to be generated in the absence of tumor cells. As with the NK cell equation, the cytolytic potential of the CD8$^{+}$T cells decreases through interaction with the tumor cells, and is represented by the second term, $-qLT$. The next two terms represent T cell recruitment due to the presence of the tumor cells. CD8$^{+}$T cells may be recruited by the debris from tumor cells lysed by NK cells (see, e.g., Huang et al., [34]). This recruitment term is proportional to the number of NK-tumor interactions, $r_1NT$. The immune system is also stimulated by the presence of tumor cells to produce more CD8$^{+}$T cells. Recognition of the presence of the tumor is proportional to the average number of encounters between circulating lymphocytes and the tumor, and is therefore represented by $r_2CT$. The term $\frac{p_1LI}{g_1+I}$ represents CD8$^{+}$T cell activation by IL-2. The Michaelis-Menten form for this term was also implemented in [39].

<a id='e3e2b949-8632-456a-95f0-5f60b1009db0'></a>

Treg dynamics also affect the CTL population. These dynamics are modeled through the term, $\frac{zL^2RI}{\kappa+I}$, which represents the breakdown of surplus CD8+ T cells in the presence of IL-2 and regulatory T cells. From Abbas et al. [1], we note that the deactivation of CD8+T cells occurs through a pathway that requires IL-2 and the action of CD4+T cells (most regulatory T cells are CD4+) but not NK cells.

<!-- PAGE BREAK -->

<a id='e1d34dec-0cd6-4de6-adb6-2989251b5db8'></a>

920 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='feb3be21-444c-4534-a21d-8b3aee6d3dd6'></a>

Moreover, the breakdown occurs only at high concentrations of activated CD8+T cells. Consequently, use Michaelis-Menten dynamics in IL-2 and including factors of $L^2$ and $R$. We choose to model $T_{reg}$ suppression of CD8$^+$ cells like this rather than changing the efficacy of the kill rate in the presence of regulatory cells (as we do with NK cells) because the number of conjugates between CD8$^+$ cells and target cells decreases in the presence of $T_{reg}$ cells [66]. The final term, $j\frac{T}{k+T}L$, represents CD8+T cell stimulated accumulation of effector cells, and takes the same form as the effector cell recruitment term used in [43].

<a id='b1f045b0-6d12-4bf8-b28d-38466f7ebef9'></a>

In equation (4), we introduce new terms to model the rate of change of CD4+25+
Treg cells involved in the immune response. We use a multiplier u that comes from
the first and second terms (representing the creation and turnover of Treg cells) in
order to emphasize the fact it is possible to measure the ratio of Treg cells to other
circulating lymphocytes in the absence of IL-2 [68, 1]. We then have a Michaelis-
Menten term in IL-2, representing IL-2-induced Treg proliferation [49].

<a id='da5ecdcf-b524-45d7-84a3-2255291c403a'></a>

The kill term $H_R (1-e^{-\lambda_R S}) R$ representing the inhibition of T$_{reg}$ cells by sunitinib, is used to reverse immune suppression and enhance the efficacy of immunotherapy [55]. Making the reasonable assumption that the effectiveness of sunitinib treatment is bounded, we use the saturation term $1 - e^{-\lambda_R S}$ to represent the effect of sunitinib stimulating fractional regulatory T cell kill. Note that at relatively low concentrations of drug, the kill rate is nearly linear, while at higher drug concentration, the kill rate plateaus. The mathematical term we use reflects the doseresponse curves to chemotherapy suggested by the literature [28]. It has been found that sunitinib does not directly cause apoptosis (programmed cell death) in T$_{reg}$ cells, but rather that it appears to reduce naive T cell differentiation into T$_{reg}$ cells [31]. However, we have chosen to model the main contribution of of sunitinib, which is to reduce the total population of effective regulatory T cells.

<a id='0085478f-9b10-4165-9c85-d50f9ca7606a'></a>

In equation (5), the circulating lymphocytes are modeled by constant growth and population dependent turnover. Note that the turnover rate not only rep-resents natural death, but also the differentiation of circulating lymphocytes into other immune cells. Although T_reg cells have been observed to have a suppressive effect on CD4+ proliferation [38], we choose not to include that effect directly in this equation, but instead to model the significant result, the suppression of IL-2 production by T_reg inhibited CD4+ cells in equation (6). This allows us to keep circulating lymphocytes at a constant level, which simplifies the dynamics, as has been done in [13]. We believe that even with this simplification, the most critical suppressive effects of the regulatory T cells are captured in our model.

<a id='e92230cc-cb9e-4acd-876c-6096961a0269'></a>

Equation **(6)** is similar to the IL-2 equation used in [13]. The term $-\mu_I I$ represents natural decay. The term $\phi C$ represents a constant rate of IL-2 production from circulating lymphocytes (specifically CD4+T cells and, to a lesser extent, naive CD8+T cells). The Michaelis-Menten term $\frac{\omega LI}{\zeta+I}$ represents the production of IL-2 from activated CD8+T cells, which is inhibited in a concentration-dependent fashion by IL-2 [1]. We note that although the presence of T$_{reg}$ cells likely has some effect on IL-2 production, we have decided not to include detail on IL-2 that is more explicit than what has already been included in the model of [13]. In a future work, we plan to examine IL-2 interactions more carefully, in which exogenous as well as endogenous IL-2 effects will be explored.

<!-- PAGE BREAK -->

<a id='05522eff-0edd-457a-af39-5f3d51c0866c'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 921

<a id='f7940772-ab21-484a-ab23-054f8210d11f'></a>

In equation (7) we introduce the term $-\eta S$ to represent the natural exponential decay of the inhibitory drug sunitinib [24]. The equation also contains the time-dependent function $v_S(t)$, representing sunitinib dosing. The rate of change of sunitinib is zero when no sunitinib is supplied.

<a id='9f8018ba-da75-4160-960a-99aa9da241e0'></a>

3. **Homeostasis values.** Before determining the various unknown parameters in our model, we first seek to find reasonable homeostasis values (biological equilibrium values) for a no-tumor condition and a high-tumor condition.

3.1. **Zero tumor homeostasis values.** In the absence of the tumor, T and S are defined to be equal to zero. Abbas et al. [1] indicates that NK cells make up approximately 10% of total circulating lymphocytes in the absence of a tumor, so if we assume that the total lymphocyte count is 2.5 × 10⁹ cells per liter, as is described in de Pillis et al. [13], then we have N = (2.5 × 10⁹) × 0.10 = 2.5 × 10⁸. The value of I is the same as the no-tumor value used in de Pillis et al. [13]. I is obtained from Orditura et al. [54], who note that healthy control subjects had average serum IL-2 levels of I = 2.99 pg/ml = 48.9273 IU/l, where we have converted to IU using the assumption that we have 18 × 10⁶ IU IL-2 per 1.1 mg IL-2 [57]. The value for L also mirrors the value used in [13]. Data taken from Pittet et al. [58] and Speiser et al. [65] indicate that approximately 0.004 % of all CD8+T cells are expected to be activated and specific for a tumor-associated antigen. Combining this with the assumption that the total number of CD8+T cells is about 6 × 10⁸ [36, p.751], we arrive at a homeostasis value of L = 2.4 × 10⁴. From Jonuleit and Schmidt [37], we know that CD4+25+ Treg cells make up 5 to 10% of all peripheral CD4+ cells. Abbas et al. [1] indicate that 50 to 60% of all circulating lymphocytes are CD4+ cells, and again assuming the total number of circulating lymphocytes is 2.5 × 10⁹ cells per liter, we can find a range of possible R values. On the lower end, 2.5 × 10⁹ × 0.05 × 0.50 = 6.25 × 10⁷, and on the upper end, 2.5 × 10⁹ × 0.10 × 0.60 = 1.5 × 10⁸. An intermediate value for R can be found by choosing intermediate values of 8% and 55%. This then yields 2.5 × 10⁹ × 0.08 × 0.55 = 1.1 × 10⁸, the value we will choose for our no-tumor homeostatic value for R. Assuming now that our population C does not include N and R, since we have separated these out, then subtracting N and R from 2.5 × 10⁹ (L is essentially negligible) gives us 2.14 × 10⁹, our equilibrium value for C.
In summary, for the no-tumor homeostasis point, we have:

<a id='35fd9136-aa57-4e6b-ab19-5467522faffa'></a>

T₀ = 0, N₀ = 2.5 × 10⁸, L₀ = 2.4 × 10⁴, R₀ = 1.1 × 10⁸,
C₀ = 2.14 × 10⁹, I₀ = 48.9, S₀ = 0. (9)

<a id='b98330b5-e9ef-4693-a252-c5ee648cf403'></a>

3.2. High tumor homeostasis values. With a tumor present but no treatments administered, S remains equal to zero. We assume that the non-zero tumor home-ostasis value is the carrying capacity of the tumor (see Section 4.1). N and C remain the same as in the zero-tumor homeostasis state. L and I change due to the presence of a tumor, which induces the activation of cytokines and CD8+ cells; we use the values found by de Pillis et al. [13]. The value for I was taken from Orditura et al. [54], who measure that IL-2 serum levels were on average I = 71.69 pg/mL = 1173 IU/L in stage III non-small cell lung cancer patients. Although these measures were not for RCC patients, we are using the approximate values as a proxy in the absence of more specific RCC data. The value for was derived L using percentages of activated CD8+ T cells from Lee et al. [44] and total CD8+ T cell values from Janeway et al. [36]. The study by Lee et al. [44] focused on melanoma, but again

<!-- PAGE BREAK -->

<a id='4942b92d-b03c-403c-8639-77614a0af81b'></a>

922 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='9785db52-89e4-47d2-bacb-5617fb9dc0f5'></a>

we are using these numbers as a proxy. We derived our value for R from Cesana et
al. [7], who found that the frequency of regulatory T cells increased 3.2-fold in RCC
patients, assuming that the patients have sufficiently large tumors for this value to
be reasonable.

<a id='acfee131-48fc-4d3c-9828-c3e4bb634f3a'></a>

In summary, for the high-tumor homeostasis values we have:
T_1 = 4.662 \times 10^9, N_1 = 2.5 \times 10^8, L_1 = 5.268 \times 10^5, R_1 = 3.52 \times 10^8, (10)
C_1 = 2.14 \times 10^9 I_1 = 1173, S_1 = 0.

<a id='12248dd4-0e00-45c9-a4b9-c794e0082fdf'></a>

4. **Parameter estimates**. With the large number of parameters in this RCC model, we had to determine parameter estimates using a variety of methods. In some cases, it was possible to find numerical ranges in the biological literature. In other cases, we had to perform numerical fits to published data. In yet other cases, when there was no relevant information available, we chose our parameter values that allowed model behavior to be biologically reasonable. A summary of the parameter descriptions and their numerical values is given in tables (2) and (3) respectively. We now outline our approach to estimating numerical values for each model parameter.

<a id='00976b81-b817-418b-8bc9-739e9295cdfd'></a>

4.1. The tumor.
The tumor growth rate, a = 2.065 × 10⁻¹ day⁻¹, is found by using MATLAB's fminsearch to fit the logistic growth equation (1) to RCC tumor growth data in nude mice from Gao et al. [27] and Doehn et al. [21]. The Doehn paper data are on a larger time scale, but the Gao data have better resolution for early tumor growth, so we chose to combine the two data sets to give us a more comprehensive set of data, as shown in Figure 1. The mice were injected with smaller initial tumors in the Doehn study, so we assume a seven day delay between the two data sets. For t = 0 to 20 days, we use data from days 0 through 20 in the Gao study, and for t = 21 to 44 days, we use data from days 28 to 51 in the Doehn study. This gives us a value for the tumor growth rate that is consistent with the individual data sets.

<a id='8147687c-c370-49d0-a591-21463c4b816c'></a>

The inverse of the tumor carrying capacity, b = 2.145 × 10⁻¹⁰ cells⁻¹, is found by looking at endpoints in tumor growth data from Doehn et al. [21]. Doehn et al.[21] indicate a reasonable approximate endpoint value could be 8.5 × 10³ mm³ = 8.5 × 10¹²μm³. Assuming a spherical tumor cell diameter of approximately 15.15μm [9, 8, 3], yields a tumor cell volume of approximately 1.82 × 10³ μm³. Dividing total tumor volume by cell volume yields a total cell count of approximately 4.7 × 10⁹. Taking the inverse of the total cell count gives our value for b.

<a id='6d6fd2e9-55f3-44bc-b9c8-80995ca01f22'></a>

The maximal rate of NK-induced tumor death, $c = 8.68 \times 10^{-10}$ L cells$^{-1}$ day$^{-1}$, is found to give the best fit to known data.

<a id='d0b8ccf5-a809-4cdb-8921-0a3c0a9a02da'></a>

The T<sub>reg</sub> induced NK inhibition coefficient, \(\lambda_T = 1.590 \times 10^{-9}\) L cells\(^{-1}\), is an
ad hoc value and has been chosen to give reasonable biological outcomes. As more
data become available, it should be possible to fit this parameter to more closely
reflect the degree NK inhibition by regulatory T cells.

<a id='317bf136-72fe-433d-a0c8-b76f2f37c748'></a>

The CD8+T cell tumor kill term, D = d((l/r)^l / (s+(l/r)^l)), involves three parameters (d, l,

<a id='6c09a5ca-f2a9-423e-b567-b3660536fec5'></a>

and s), which reflect the efficacy of patient-specific immune systems. The immune system strength coefficient is d (day⁻¹), the immune strength scaling coefficient is l (unitless), and the constant s (unitless) is the value of (L/T)l necessary for half-maximal CD8⁺ T cell toxicity. In our numerical simulations, we use uniform probability distributions ranging from 1.7 to 2.2 to generate random values of d and

<!-- PAGE BREAK -->

<a id='62f0c294-a036-4e49-82b3-11c05ec6f0b1'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 923

<a id='6b4d6c85-81ec-430c-9c6f-5672d75bcfd3'></a>

<::chart: Fitting Logistic Growth Curve to Gao (2010) and Doehn (2009) Data. The x-axis is labeled "Time (days)" and ranges from 0 to 50. The y-axis is labeled "Tumor Size (cells)" and is on a logarithmic scale from 10^0 to 10^10. The chart displays two data series: red stars with error bars representing "Gao & Doehn Data", and a blue solid line representing "Logistic Growth Fit". The red stars generally follow the blue curve, which shows a growth trend that levels off over time.::>FIGURE 1. Fit to combined data from Gao *et al*. (2010) (days 0 through 20) and Doehn *et al*. (2009) (days 21 through 44) to find parameter *a*.

<a id='edc0c620-cb23-433d-9305-e8e38f0efae6'></a>

l for each individual patient. The value of $s = 3.5 \times 10^{-2}$ is kept unchanged from the de Pillis et al. [13] model.

<a id='5e60c9ff-fbb7-49a1-8662-fd5f8fda5379'></a>

4.2. The natural killer cells. The ratio of NK cell synthesis to turnover, e/f = 1.168 x 10⁻¹, is equal to the ratio N/C at equilibrium if we ignore the small effect of IL-2 on NK proliferation. Note that in this model, C measures the total number of lymphocytes that are not CD8⁺ T cells, NK cells, or Treg cells.

<a id='2902540b-1fcd-48a2-afd5-a979b19a12b7'></a>

The rate of NK turnover, $f = 1.25 \times 10^{-2}$ day$^{-1}$, is taken from de Pillis et al. [13]. They found this value for $f$ by employing metabolic scaling, noting that the average mass of an adult human male is $77kg$ [67] and $11.9kg$ for an average adult male rhesus monkey [59]. From Gillooly et al. [29], we have that the mass-specific metabolic rate $B$ scales as

<a id='6ccb5f63-e922-444b-bf95-c56e7edf1015'></a>

B/M \propto M^{-1/4},

<a id='6d3f6b04-f878-453a-a2a0-74bccc9a2453'></a>

where M is mass. The de Pillis et al. [13] team assumed that f, the turnover rate of NK cells, was proportional to the mass-specific metabolic rate. They found fmonkey = 2 × 10-2 for a rhesus monkey from De Boer et al. [12]. Thus, we have

<a id='bbf5da5e-e0f6-4855-ac7a-f2708986e38b'></a>

f = Γ(B/M) = Γ'M^{-1/4},

<a id='b7486cde-24db-4c78-a779-83da8043f87a'></a>

where Γ and Γ' are constants. Then,

<a id='acc8f86a-02ee-4fb9-a407-6daf2ffd05a0'></a>

Γ' = f_monkey / M_monkey^(-1/4) = 0.0371,

<!-- PAGE BREAK -->

<a id='ac31f2ba-d8be-41ed-ad8b-05ab898e0436'></a>

924 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='a959f92d-fab7-49c1-b305-73bcfb03c117'></a>

which then yields
f = Γ'M_human^(-1/4) = 1.25 × 10^(-2)

<a id='720e6415-c80b-436b-86cc-eac05c0cd236'></a>

for an average human.
The rate of NK cell death due to tumor interaction, $p = 6.682 \times 10^{-14}$ L cells$^{-1}$
day$^{-1}$, is obtained by considering the large tumor equilibrium in the absence of
medicine. We have

<a id='c4e7d432-1cc7-469b-9b31-43e111b034c1'></a>

0 = dN/dt = f((e/f)C - N) - pNT + p_N NI / (g_N + I).

<a id='2070de1f-da79-4299-b1cd-13860b24c404'></a>

Since we suppose that $e/f = N/C$ at equilibrium, this simplifies to

<a id='f8b75f2d-0f90-476c-9c0d-d02587adecfe'></a>

<::p = (pNI) / (T(gN + I)).
: equation::>

<a id='75353f9d-caad-4034-8f9a-6072bd1f29ec'></a>

Using the equilibrium values from the high-tumor equilibrium, we arrive at our value for $p$.

<a id='da273fdb-9057-4de9-ab8a-f99a61b4779c'></a>

The rate of IL-2 induced NK cell proliferation, pN = 6.68 x 10-2 day-1, is calculated using the same method as de Pillis et al. [13]. They used data from the study of Meropol et al. [50], that examined IL-2 induced NK cell expansion in patients. They assumed that the peak NK cell count from Meropol et al. [50] in the absence of tumor corresponds to the equilibrium value of N subject to the peak value of IL-2 (including non-negligible exogenous supplementation). Thus, we have:

<a id='2c826585-8281-408f-919d-55ee5957ffaa'></a>

$$\frac{dN}{dt} = 0 = f\left(\frac{e}{f}C - N\right) + \frac{p_N NI}{g_N + I}$$

<a id='74fd6c67-edca-4edf-9d86-4f439a718e8c'></a>

which gives

<a id='d75d2006-c47f-4316-98c5-28e95eba604d'></a>

<::p_N = \frac{f (N - \frac{e}{f}) (g_N + I)}{NI}.
: figure::>

<a id='cd0846e8-9b43-4ed0-bcb5-022b812ca9ab'></a>

Using our value of $C = 2.14\times10^9$ and the Meropol et al. [50] values for $N$ ($2.3\times10^9$) and $I$ ($5.0073 \times 10^4$), we arrive at our value for $p_N$.

<a id='3d681e41-69e0-499e-8db7-25d02d33845d'></a>

The concentration of IL-2 required for half-maximal NK cell proliferation, gN =
2.5036 × 10⁵ IU L⁻¹, is left unchanged from the value found by the de Pillis et al.
[13] team, who derived gN using IL-2 binding data from Abbas et al. [1]. From
Abbas, we see that the concentration of IL-2 required for half-maximal binding of
cells expressing the IL-2RβγC receptor complex is 10⁻⁹ mol/L. IL-2 has a molecular
mass of 15,300 Da (15,300 g/mol), and there are 18 × 10⁶ IU of IL-2 per 1.1 mg
[35]. Converting to IU/L, we have

<a id='7547e427-dfe5-4907-aeab-93a6a78af109'></a>

gN = (1 \times 10^{-9}mol / 1L) (15,300g / 1mol) (1000mg / 1g) (1.8 \times 10^7IU / 1.1mg) = 2.5036 \times 10^5IU/L.

<a id='30f409a0-843f-42ad-afa4-2ed9a909f7e8'></a>

4.3. **The CD8$^{+}$ T cells.** The rate of CD8$^{+}$ turnover, $m = 9 \times 10^{-3}$ day$^{-1}$, is left unchanged from de Pillis et al. [13], who derived their value for $m$ from Hellerstein et al. [33]. They put the half-life of CD8$^{+}$ cells at 77 days in healthy donors. Assuming exponential decay, we have $m = \frac{\ln(2)}{77\text{days}}$.

<a id='e242402b-e1d3-46d4-b5bb-137a57b28f3b'></a>

The rate of CD8$^+$ T cell death due to tumor interaction, $q = 3.422 \times 10^{-10}$ cells$^{-1}$ day$^{-1}$, is borrowed from de Pillis et al. [13]. The value of $q$ was in turn taken from Kuznetsov et al. [43], who used mouse data to model the dynamics of a general effector cell population and a tumor. Other studies suggesting alternate values for $q$, $j$, and $k$ were not found.

<!-- PAGE BREAK -->

<a id='243fd999-9a3c-4a00-bf57-b04d8cd71d28'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 925

<a id='f4698bfe-67a1-4116-ac87-7590c92b89c3'></a>

The rate of NK-lysed tumor cell debris activation of CD8+ cells, r₁ = 8.68×10⁻¹² cells⁻¹ day⁻¹, is derived using similar methods as de Pillis et al. [13]. Data directly measuring the rate of NK cell activation as a result of lysed tumor debris are not readily available. However, in order to determine a reasonable approximate rate, we followed the argument of [13], where it is assumed that each lysed tumor cell, through antigen-presenting pathways, leads to activation of CD8+T cells. Rates of activation were adapted from Avigan [4] and Ruedl [61], which indicate that a dendritic cell may stimulate between 10 and 3000 T cells over the course of its lifetime, and that an average lifetime for some DCs is about 10 days. Assuming that only a fraction of lysed tumor cells activate a single DC, we set r₁ = 0.01 × c. Here we estimate that a lysed tumor cell, through DC activation, will stimulate 1/100 of 1 T cell per day. Recall that c represents the rate of NK-induced tumor cell death.

<a id='aacdfb83-202d-4ce8-bc39-0484ef8a44a9'></a>

The rate of CD8+ T cell production from circulating lymphocytes is given by r2 = 1 \times 10^-15 cells^-1 day^-1. Since we found no data measuring the relevant kinetics of CD4+T cell activation of CD8+T cells, this value is chosen to obtain a model consistent with expectations.

<a id='e4a65abb-d91b-4d5c-958e-b7af91c42907'></a>

The rate of IL-2 induced CD8+ T cell activation, $p_I = 1.111$ day$^{-1}$, is derived using a system of equations designed to produce reasonable behavior at homeostasis levels. We set $dL/dt = 0$ and insert both sets of homeostasis values along with all parameters besides $p_I$ and $z$ to obtain a system with two equations and two unknowns. Solving these equations then yields values for $p_I$ and $z$. We note that the system of equations is ill-conditioned. However, although the values of $p_I$ and $z$ may vary based on how the solution of the system is carried out numerically, repeat calculations with varying solution strategies give rise to values of the same order of magnitude.

<a id='f25e85ee-0faf-428e-880b-1c3f897f4148'></a>

The concentration of IL-2 for half-maximal CD8+ T cell activation, $g_I = 2.5036\times$
$10^3$ IU L$^{-1}$, is left unchanged from the value found by de Pillis et al. [13], who found
their value for $g_I$ using IL-2 binding data from Abbas et al. [1]. The derivation is
the same as for $g_N$, except that the concentration for half-maximal binding is $10^{-11}$
mol/L for the IL-2R$\alpha\beta\gamma_c$ receptor on CD8+ T cells, which yields $2.5036 \times 10^3$ IU/L.

<a id='9698f6c0-dc1f-49ba-a535-f7a73acb035a'></a>

The T_reg induced CD8^+ inhibition coefficient, z = 2.3085 \times 10^{-13} L^2 cells^{-2} day^{-1}, is part of the solution of the system of equations used to calculate p_I.

<a id='18c66e30-e2f3-4f82-ae9c-55359a90f4c5'></a>

The concentration of IL-2 needed to halve the magnitude of T_reg inhibition, ̕ = 2.5036  10 IU L, is left unchanged from the value found by de Pillis et al. [13], who derived ̕ in the same way as g. Refaeli et al. [60] observe that upon removal of the a IL-2 receptor chain, CD8+T cells fail to self-regulate. This affirms that k should correspond to the disassociation constant for the IL-2R̖̗̘̙̕ receptor.

<a id='949f9a48-ff36-4939-8ac2-cffa81d580c2'></a>

The rate of CD8+ T cell lysed tumor cell debris activation of CD8+ cells, j =
1.245 x 10-1 day-¹, is left unchanged from de Pillis et al. [13], who took j from
Kuznetsov et al. [43] for lack of data in humans.

<a id='2cff7b8e-8008-4d2e-8f4c-ad57d5c2bd6f'></a>

The tumor size for half-maximal CD8+ T cell lysed debris CD8+ T cell activation,
k = 2.019 x 10^7 cells, is left unchanged from de Pillis *et al*. [13], who took *k* from
Kuznetsov *et al*. [43] for lack of data in humans.

<a id='cc656670-f5cc-4438-9611-22f5ae39d17e'></a>

4.4. **The regulatory T cells.** The ratio of T<sub>reg</sub> production to turnover, _w/u_ = 0.0122, is equal to _R/C_ at a homeostasis state with no IL-2. From Yu et al. [68], we find that somewhere between 2% and 10% of CD4<sup>+</sup> cells are regulatory T cells in the absence of IL-2. Assuming that 2% of CD4 cells are T<sub>regs</sub>, and assuming that there are 2.5 × 10<sup>9</sup> circulating lymphocytes per liter and that 55% of lymphocytes

<!-- PAGE BREAK -->

<a id='d9087516-e44f-4d17-ba84-2930e39ba5f1'></a>

926 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='5941d4c7-72a5-48d2-8e8e-4f508ab265ae'></a>

are CD4+ cells [1], we have $R = 2.75 \times 10^7$ and $C = 2.2225 \times 10^9$, which yields w/u.

<a id='be9ef301-9135-4c49-96e9-c2044e163785'></a>

The rate of T_reg turnover, _u_ = 3.851 \times 10^-2 day^-1, is found by assuming ex-ponential decay of regulatory T cells. We find that these cells had a half life of approximately 18 days [48]. Thus, we have

<a id='55818e4a-ef5a-40bf-8203-b6f8cd6bbade'></a>

u = ln(2) / 18 days.

<a id='a6169450-24a2-4ec2-9b80-49f66fa1b906'></a>

The rate of IL-2 induced regulatory T cell proliferation, $p_R = 3.598 \times 10^{-2}$ day$^{-1}$, is found by solving a system of equations designed to produce reasonable behavior at homeostasis states. We set equation (4) to zero and insert both sets of homeostasis values, along with the unknown parameters $p_R$ and $g_R$. We then have a system of two equations and two unknowns. Recall that the zero tumor and high tumor homeostasis values are given in sections 9 and 10 respectively. Using these values, we solve for $\vec{x}$ in the system $A\vec{x} = \vec{b}$ where

<a id='2ee7eaca-e3c5-41aa-b576-971cd48ed02b'></a>

A = $\begin{bmatrix} R_0I_0 & wC_0 - uR_0 \ R_1I_1 & wC_1 - uR_1 \ \end{bmatrix}$

$\vec{x} = \begin{bmatrix} p_R \ g_R \ \end{bmatrix}$

$\vec{b} = \begin{bmatrix} I_0(-wC_0 + uR_0) \ I_1(-wC_1 + uR_1) \ \end{bmatrix}$ (11)

<a id='c2f67280-06de-4b4e-b037-f623663518b4'></a>

Solving this system yields our desired parameters. In this case, the matrix A is not well conditioned, so the values of pR and gR may vary slightly depending on how the system solve is carried out, but the variance yields values of the same order of magnitude, and does not appear to affect the model outcome significantly.

<a id='8dfa44d2-f7c7-480d-bf49-ff0042bc1d21'></a>

The concentration of IL-2 necessary for half-maximal activation of T$_{reg}$ cells,
*g*$_{R}$ = 11.027 IU L$^{-1}$, is found by noting that CD4$^{+}$25$^{+}$ cells express both the
IL-2R$\beta\gamma$$_{c}$ receptor complex and the IL-2R$\alpha\beta\gamma$$_{c}$ receptor complex [1]. Since both
receptor complexes are present, we assume that we cannot simply take one of the
IL-2 binding rates, so we instead solve for *g*$_{R}$ through system (11) as described for
parameter *p*$_{R}$ above.

<a id='0fc4ae9c-a252-45bc-8356-cf8d8df94c4e'></a>

The rate of T_reg inhibition from sunitinib, H_R = 2.27×10⁻² day⁻¹, was found by running simulations with data from Finke et al. [25]. They show that the percentage of CD4⁺ cells that differentiate into T_reg cells (including both CD4⁺CD25ʰⁱ⁺ cells and CD4⁺CD25ʰⁱ⁺FoxP3⁺ cells) decrease from about 6.65% to 5.98% after 28 days of sunitinib treatment, so we numerically determine values for H_R and λ_R that give us this desired T_reg behavior.

<a id='bcd86874-6307-456c-bd4f-85ef7a51206b'></a>

The sunitinib efficacy coefficient, $\lambda_R = 50.02$ L mg$^{-1}$, was found as part of the numerical calculation of $H_R$.

<a id='7f61d120-d2ad-4821-bade-e68a7bffc53b'></a>

4.5. **The circulating lymphocytes.** The ratio of lymphocyte synthesis to turnover, α/β = 2.14 × 10⁹ cells L⁻¹, is equal to _C_ at homeostasis with no treatments present. We have taken an average value of circulating lymphocytes to be 2.5 × 10⁹ cells [1], but we factor out NK, CD8⁺, and T_reg cells, yielding our desired value.

<a id='05c0011a-b7f5-448f-94a1-6d34a0c5cbff'></a>

The rate of lymphocyte turnover, β = 6.3 × 10⁻³ day⁻¹, is taken from the de Pillis et al. [13] model. It was found by applying metabolic scaling, as was done for finding parameter f, to the 1% turnover rate of CD4⁺ cells found in rhesus monkeys [12].

<a id='e5bbcf59-51ef-4909-8b56-5a993a6108ec'></a>

4.6. The **IL-2**. The rate of IL-2 excretion and elimination, μI = ln 2/5.9 × 10⁻² = 11.7483 day⁻¹, is taken from de Pillis et al. [13]. The value was derived using the assumption of exponential decay, with a tissue elimination half-life of 85 minutes taken from Konrad et al. [41].

<!-- PAGE BREAK -->

<a id='b5c7954f-d852-4f03-bbe7-85e5e6f82e59'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 927

<a id='0d159e3d-e24b-41a1-b318-578bdb48aa0a'></a>

The rate of IL-2 production from CD8+ T cells, ω = 7.879 × 10^-2 day^-1, is calculated using a system of equations designed to produce reasonable homeostasis behavior. Setting equation (6) to zero, inserting both sets of homeostasis values, and solving for the unknown parameters φ and ω, yields the following system:

A = [[C0, L0I0 / (ζ+I0)], [C1, L1I1 / (ζ+I1)]] x = [[φ], [ω]] b = [[μI I0], [μI I1]] (12)

<a id='0bee1974-3543-4f53-a7e8-a93828b9acb0'></a>

We then solve for $\vec{x}$ in the system $A\vec{x} = \vec{b}$. Solving this system yields values for both $\omega$ and $\phi$.

<a id='bc6ff1cb-315f-4fb9-87f4-9712658347b0'></a>

The rate of IL-2 production from CD4+T cells and naive CD8+T cells is given by φ = 2.5153 × 10⁻⁷ IU cells⁻¹ day⁻¹, This value is calculated using the system of equations (12) designed to produce reasonable homeostasis behavior, as outlined in the description of the calculation for ω.

<a id='b54fb866-d761-43d9-8ecd-6f42d2b96425'></a>

The concentration of IL-2 needed for half-maximal CD8$^{+}$ T cell IL-2 production,
ζ = 2.5036 × 10³ IU L⁻¹, is left unchanged from the value found by de Pillis et al.
[13], who set ζ = g_I, since CD8$^{+}$ T cell IL-2 synthesis induced by IL-2 depends on
the IL-2Rαβγc receptor [1].

<a id='88bc0eb5-2157-4285-9bc1-01018f1dd309'></a>

4.7. The **Treg inhibitor: Sunitinib**. The rate of excretion and elimination of sunitinib, η = 0.277 day⁻¹, is taken from Faivre et al. [24]. It is derived using the assumption of exponential decay with a half-life of 60 hours (2.5 days). Faivre et al. [24] note that sunitinib has a half-life of 41 to 86 hours but do not report a mean or median, so we choose a value from that range and calculated η as ln(2) / 2.5 days.

<a id='c1400c89-7df4-4f28-b64d-6bec512ed490'></a>

The sunitinib dose function, v_S mg/L, is a function of time, and is determined as follows. The dosing schedule for sunitinib, v_S, was derived from Ko et al. [40] and Motzer et al. [52, 53], whose dosing schedule consists of 50 mg/day taken orally every day for 28 days followed by 14 days of rest; this comprises a single 6-week cycle. A study performed by Motzer et al. [52] tells us that the average number of cycles that patients typically go through is 5. Assuming the average body volume of a human male to be 59.71 L (the same assumption used by de Pillis et al. [13] in their dosage calculations), we have v_S = (50mg/day × 28days)/59.71L, which gives us

<a id='446786f7-21d8-4ca5-9ec5-ecaade083af2'></a>

vS = 23.4467mg/L
each cycle for an average of 5 cycles. The value of vS is set to zero in between dosing cycles.

<a id='171daed6-d4bb-412a-b2e5-5bc8c6d18ec4'></a>

5. **Results and analysis.** In this section, we present numerical outcomes of model simulations. We will first provide model verification by examining numerical model dynamics in the absence of treatment interventions, followed by simulations using clinically tested sunitinib dosing schedules and comparing these outcomes to clinical data. Finally, we present experimental hypothetical dosing schedules that can provide improved tumor growth control.

<a id='3b72ee5b-82fd-4c57-8cd7-11cf48c875ea'></a>

5.1. **Model validation - Simulations with no treatment.** In this section we run model simulations to determine whether model outcomes are reasonable and reflect expected clinical outcomes.

<a id='b68672f5-8916-40bc-84cf-18c5e9bc563e'></a>

We first examine the biological homeostasis values, and test whether they are
close to numerical equilibrium values. We should expect to see at least a slight
difference between the biological and the numerical values since our homeostasis

<!-- PAGE BREAK -->

<a id='8c382e86-e587-4931-90ef-bcb5f355c64d'></a>

928 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='c1e19f71-b0f9-43f1-a5d0-e4bce40ee080'></a>

values are approximations using simplifying assumptions, while the model simulations provide the outcomes incorporating full system interactions. For example, the high tumor homeostasis value is chosen to be the tumor carrying capacity, which does not account for immune control, so we would expect our simulated outcomes to evidence a slightly lower "high tumor" equilibrium because of the presence of the immune components in the system.

<a id='94f979c1-ff5b-4efb-9f98-7e1e1eac5cea'></a>

Figure 2 shows the no-tumor and the high-tumor scenarios, in which initial values of the state variables are given by the biological homeostasis values provided in section 3. The parameter values used for these simulations are provided in table 3, with d = l = 1.7. The no-tumor homeostasis values are very close to the numerical equilibrium values. Numerically, all values remain within the same order of magnitude, and visually it is difficult to detect much change in the values over time. The high tumor homeostasis values are also close to the numerical high tumor equilibrium values, but as expected, the numerical equilibrium values are slightly lower because of the interaction with the immune components. The homeostasis value for the tumor was chosen to be the carrying capacity, 4.662 \u00d7 10\u2079, while the numerical high tumor equilibrium is closer to 2.14 x 10\u2079.

<a id='031821c8-2cbb-4b1f-847c-d0aa80cd366e'></a>

Numerically, it appears that the high tumor equilibrium is stable. The natural question to ask is whether the low tumor equilibrium is also stable. In figure 3 we see that the zero tumor equilibrium is indeed numerically stable, and in fact, it appears that the bifurcation point lies at around 1.77 x 10^7. That is, when the initial tumor size is set to a value at or below 1.77 x 10^7, the tumor shrinks back down to zero, but if it is initiated at a value above, for example at 1.78 x 10^7, then the tumor grows to the high equilibrium value. In both these scenarios, all other initial states are the zero tumor homeostasis values. This model does not address the interesting question of tumorigenesis, that is, if the zero tumor state is stable, how does a tumor ever grow to carrying capacity. We hypothesize that this can be in part caused by a breakdown in immunosurveillance. In fact, if we remove all immune control in the model, then even a single tumor cell will grow to carrying capacity (figure not shown).

<a id='3b79fc84-1d9b-4f4b-b9aa-2774f5c0558c'></a>

In figure 4, we present the result of simulating tumor growth for 100 different patients over 300 days. All parameters are fixed at the values presented in table 3, except for d and l. These two parameters, which modulate the effectiveness of the CD8+T cells, can vary from 1.7 to 2.2 in our model. This range was chosen since it reflects biologically reasonable values for d and l as found in [13]. For each simulated individual, random values of d and l are chosen from a uniform distribution. Each patient starts at day 0 with an initial tumor size of 1 × 10⁸ tumor cells, which is above clinical detection levels. In this simulation, there is no treatment intervention, and in every case, the tumor grows by an order of magnitude. It is clear from this simulation that the effect of varying d and l within the specified range is not sufficient by itself to control tumor growth.

<a id='82b3737f-b35d-4a7b-8835-3fa472d3651b'></a>

We increased the d and l range of values in order to explore whether there were any parameter combinations that would allow for the immune system to control tumor growth with no treatment intervention. Allowing l and d to take on values between 0.5 and 3.0, we observed the outcome at day 300, using every (d, l) combination in increments of 0.1 (resulting in a total of 676 scenarios). As we would expect, each scenario resulted either in a complete response (CR), or progressive disease (PD). That is, the system was driven to either the zero tumor or the high

<!-- PAGE BREAK -->

<a id='0a9bdb77-ecac-4083-894e-39f631f61eda'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 929

<a id='64e281e5-757c-463a-a83b-d95542a20847'></a>

<::chart: Two line plots, stacked vertically, showing model simulations over time. Top panel: "Model Simulation: No-Tumor Homeostasis". X-axis: "Time (days)", from 0 to 300. Y-axis: "States (logarithmic scale)", from 10^0 to 10^12. Legend: Tumor Cells (black line, constant at ~10^8), Natural Killer Cells (green line, constant at ~10^8), CD8+ T Cells (blue line, constant at ~10^4), Regulatory T Cells (yellow line, constant at ~10^9), Circulating Lymphocytes (cells) (red line, constant at ~10^8), IL-2 (IU) (cyan line, constant at ~10^2), Sunitinib (mg) (red dashed line, constant at ~10^0). All lines are horizontal, indicating stable states for each component. Bottom panel: "Model Simulation: High-Tumor Homeostasis". X-axis: "Time (days)", from 0 to 300. Y-axis: "States (logarithmic scale)", from 10^0 to 10^12. Legend: Tumor Cells (black line, starts high and stabilizes around 10^9), Natural Killer Cells (green line, starts high and stabilizes around 10^8), CD8+ T Cells (blue line, starts low and stabilizes around 10^5), Regulatory T Cells (yellow line, starts high and stabilizes around 10^9), Circulating Lymphocytes (cells) (red line, starts high and stabilizes around 10^8), IL-2 (IU) (cyan line, starts low and stabilizes around 10^2), Sunitinib (mg) (red dashed line, constant at ~10^0). Lines show an initial transient phase before settling into stable states, which are different from the "No-Tumor Homeostasis" panel. FIGURE 2. Numerical equilibrium values appear to be stable. Top panel: initial conditions are tumor free. Bottom panel: initial conditions are a high-tumor state. Numerical initial condition values are given by the low-tumor and high-tumor homeostasis values provided in section 3. Parameter values are given in table 3, with $d = l = 1.7$::>

<a id='9fcd74c6-e09f-4631-9ef9-8c8e6507f9ec'></a>

tumor homeostasis value. As can be seen in figure 5, there is a range of (d, l) combinations that represent a sufficiently strong immune response. For all tested values of d, as long as l ≤ 1, the tumor was eliminated. Also, for larger values of d, the values of l could also increase slightly, and the tumor can still be controlled. Parameter l represents how the target lysis rate depends on the effector-target ratio. According to [15], this is a patient-specific parameter that can, in theory, be measured. In [15], they found that for the two patients whose data was examined, the respective values for l were greater than 1. However, it is possible that certain treatments may effectively reduce this parameter value, representing a strengthening of the immune response [15, 20].

<a id='a1c46f44-ad5e-4417-bd2c-4751c293a139'></a>

In the next section, we explore simulation outcomes with sunitinib intervention.

<!-- PAGE BREAK -->

<a id='d38efe9e-0ed9-4ef2-8289-f8e221088dd5'></a>

930 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS<::chart: Two line graphs stacked vertically, showing model simulations for tumor bifurcation. Both graphs share a y-axis labeled "States (logarithmic scale)" ranging from 10^0 to 10^12, and an x-axis labeled "Time (days)" ranging from 0 to 300. A common legend indicates the lines: Tumor Cells (black), Natural Killer Cells (green), CD8+ T Cells (blue), Regulatory T Cells (red), Circulating Lymphocytes (cells) (yellow), IL-2 (IU) (cyan), and Sunitinib (mg) (dashed red).Top Panel: Titled "Model Simulation: Tumor Bifurcation - Low". The black line (Tumor Cells) starts around 10^7 and decreases sharply to below 10^0 around 175 days, remaining at zero. The blue line (CD8+ T Cells) and red line (Regulatory T Cells) show initial stability then a slight decrease. The green line (Natural Killer Cells) and yellow line (Circulating Lymphocytes) remain relatively constant at higher values. The cyan line (IL-2) is stable at a low value. The dashed red line (Sunitinib) is stable at a high value.Bottom Panel: Titled "Model Simulation: Tumor Bifurcation - High". The black line (Tumor Cells) starts around 10^7 and increases steadily, reaching above 10^11 by 300 days. The blue line (CD8+ T Cells) shows an initial increase then a decrease, stabilizing around 10^5. The red line (Regulatory T Cells) is stable. The green line (Natural Killer Cells) and yellow line (Circulating Lymphocytes) remain relatively constant at high values. The cyan line (IL-2) shows a slight increase towards the end. The dashed red line (Sunitinib) is stable at a high value.FIGURE 3. The zero tumor equilibrium stable. Initial tumor size in the top panel is $T_0 = 1.77\times10^7$, and the tumor shrinks down to zero over time. Initial tumor size in the bottom panel is $T_0 = 1.77\times10^7$, and the tumor grows to the high tumor equilibrium value. Initial conditions of the other state variables are given by the low-tumor homeostasis values provided in section 3. Parameter values are given in table 3, with $d = l = 1.7$::>

<a id='fcd58b6b-17d1-43c3-8144-75745a0669cc'></a>

5.2. **Model validation - Simulations with sunitinib treatment.** We now examine simulated outcomes in response to sunitinib dosing. In figure 6, we present

<!-- PAGE BREAK -->

<a id='ba2fa736-857b-4acc-9876-62d0b65cdf75'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 931<::chart: Bar chart titled "Patient Responses – No Treatment". The y-axis is labeled "Percentage of Patients" and ranges from 0 to 100. The x-axis is labeled "Type of Response" and has categories "Complete Response", "Partial Response", and "No Response". There are three bars: "Complete Response" shows 0% of patients, "Partial Response" shows 0% of patients, and "No Response" shows 100% of patients (represented by a red bar). FIGURE 4. Simulation of 100 patients. Tumor growth after 300 days, no treatment. Immune strength parameters $d$ and $l$ sampled from a uniform distribution within $[1.7, 2.2]$. Initial tumor size for all patients $1 \times 10^8$. Final tumor size for all patients approaches on the order of $1 \times 10^9$.::>

<a id='d8eb3bf0-e218-4e05-8d1a-08672ff10cc8'></a>

the result of simulating tumor growth for 100 different patients over 300 days with sunitinib dosing according to standard sunitinib dosing schedules. The same dos- ing schedule was followed in, for example, the studies described in [47, 40, 52, 53]. See section 4.7 for dosing details. We classify our simulated patient responses following the patient response classification schemes of the clinical studies data we used [47, 40, 52, 53]. In each of the studies in [47, 40, 52, 53], the authors assess clinical response using the Response Evaluation Criteria in Solid Tumors (RECIST) guidelines [23, section 4.3]. According to these guidelines, a complete response (CR) means all target lesions have "disappeared". A partial response (PR) means there has been at least a 30% decrease in the sum of diameters of the target lesions. Progressive disease (PD) means there has been at least a 20% increase in the sum of the diameters of the target lesions, and stable disease (SD) means there has been neither lesion shrinkage greater than 30% nor lesion growth greater than 20%. An "objective response rate" combines both complete and partial responses. In [32], the relevance of these categorizations is questioned, particularly the distinction be- tween SD and PD. In this paper, the authors state, "Many physicians have tried to identify the clinical significance of SD and some claim that patients with initial SD after their first-line chemotherapy have poorer survival outcome and less sympto- matic benefit than those with PR." [32] Our interest is in whether the treatments lead to significant tumor shrinkage. Therefore, for the purposes of our simulations, we combine the SD and PD categories, and categorize patients as having "no re- sponse" (or no objective response) when the tumor has not decreased in size by at least 30%. The study of [40], for example, provides numbers only for PR and PD categories. In many studies, the "best overall response" is reported. The "best overall response" refers to the "best" response at any point from the start of treatment until disease progression or the end of the observation period. The time point at which the best response was achieved is rarely reported. Likewise, the time point at which the disease is considered SD or PD is almost never specified.

<!-- PAGE BREAK -->

<a id='b9e813a1-9d33-43d6-82d1-94ce30da31ea'></a>

932

<a id='2348d31e-82c6-4418-98d4-0dac1dc95d92'></a>

L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='b913324c-330a-444b-9570-c37458187770'></a>

<::chart: Patient Categories, No Drugs. Day 300. 676 Patients. This is a scatter plot showing patient outcomes (Complete Response or Progressive Disease) based on 'd values' (x-axis) and 'l values' (y-axis). The x-axis ranges from 0 to 3.5, labeled 'd values'. The y-axis ranges from 0 to 3.5, labeled 'l values'. A legend indicates that green circles represent 'CR' (Complete Response) and red triangles represent 'PD' (Progressive Disease). The plot shows a grid of points. For 'l values' approximately below 1.3, most points are green circles (CR). For 'l values' approximately above 1.3, most points are red triangles (PD). The transition from CR to PD occurs predominantly around l = 1.3, regardless of the 'd' value. The 'd' and 'l' values are presented from 0.5 to 3.0. FIGURE 5. Simulation of 676 patients. No treatment. Patients either experience complete response (CR - circles) or progressive disease (PD - triangles) by day 300. All combinations of immune strength parameters d and l presented, each taking values from 0.5 to 3.0. Initial tumor size for all patients 1 × 10⁸. Final tumor size for patients in the PD category on the order of 1 × 10⁹.::>

<a id='0389c92b-8fb1-49f0-a01e-53bdc441b948'></a>

For the purposes of our simulations, therefore, we also measure the best response within the simulation period, and we have translated the RECIST criteria to mean the following: A complete response (CR) in our simulations means that the tumor level has gone below 100 cells by day 300. Since this level is far below clinical detection levels, we have chosen this to align with the RECIST meaning of having "disappeared". As we saw earlier, with tumor levels this low, a non-compromised immune system will allow the tumor size to be driven zero over time. A partial response means that at least a 30% decrease in tumor size has been achieved, as specified by RECIST. And, as we have stated, "no response" means the response could neither be categorized as complete nor partial.

<a id='c71021cb-d7f4-4c3b-8565-3660a090c65d'></a>

As in the non-intervention case, 100 simulations are carried out to represent
100 patients of varying CD8+T cell strength as reflected by modification of the
parameters $d$ and $l$. Parameters $d$ and $l$ are randomly chosen from a uniform
distribution varying between 1.7 and 2.2. As before, each patient starts at day 0
with an initial tumor size of $1 \times 10^8$ tumor cells.

<a id='02209611-f24f-464d-bcce-11442be48ce7'></a>

Our simulations in this case show that about 60% of patients did not respond to treatment. About 35% achieved a partial response, and about 5% achieved

<!-- PAGE BREAK -->

<a id='8a268c7e-2979-49f2-86a5-a892b34853b5'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 933

<a id='bb85d266-b71b-4b0b-bdd5-70d5bf027156'></a>

a complete response. These results are in line with expected response rates to sunitinib treatment, as seen in [47, 40, 53]. For example, in [47], a total of 36 RCC patients were treated with sunitinib and followed for 15 months. In this study, 29.4% achieved partial response, and 70.6% had stable or progressive disease for at least two cycles. In [53], 248 patients received sunitinib treatment and were followed for six months. Approximately 30% achieved PR, while about 70% had no objective response, while one patient may have achieved a complete response. The study of [40], which enrolled 23 metastatic RCC patients followed over two years, reported partial response for 43% of patients.

<a id='08d2704d-8bf6-4f93-b6d3-7ffdd04830e8'></a>

The simulation results indicate that the model is able to capture qualitatively realistic responses to sunitinib treatment, even in the absence of patient-specific data. We note that our simulations did give rise a complete response in about 5% of patients, which was a fairly rare outcome in the clinical studies. It is interesting that varying only the two immune-strength parameters $d$ and $l$ from patient to patient yields simulated results that reflect clinical outcomes reasonably well. If patient-specific data were to become available, model parameters could be tuned accordingly, and simulations would likely align even more closely to clinical outcomes.

<a id='400ea374-7480-4255-b819-a5c27c56bc7f'></a>

<::bar chart
Title: Patient Responses - Normal Sunitinib Treatment
Y-axis: Percentage of Patients
X-axis: Type of Response
Data:
- Complete Response: Approximately 5%
- Partial Response: Approximately 35%
- No Response: Approximately 59%

FIGURE 6. Simulation of 100 patients. Tumor growth after 300 days with sunitinib treatment as outlined in section 4.7. Immune strength parameters $d$ and $l$ sampled from a uniform distribution within $[1.7, 2.2]$. Initial tumor size for all patients $1 \times 10^8$.
:chart::>

<a id='631bcd5d-23ea-4978-acc3-c4d5c8eb89d6'></a>

5.3. Experimental dosing schedules. Once we validated our model's correlation with clinical response data, we varied the clinical dosing schedule of sunitinib to test whether this would yield better response rates. We experimented with increasing the amount of time the drug was administered by two days and decreasing the number of days in a full treatment cycle by two days (that is, resuming treatment two days sooner than the standard), giving us four permutations of scheduling. For these new schedules, we also varied the dose of sunitinib administered between the normal dosage amount (50 mg), a half dose, and a double dose. These changes gave us 12 experimental trials. We found that doubling the dosage amount, but keeping the dosing schedule the same as in our model validation (figure 7), yielded the best

<!-- PAGE BREAK -->

<a id='bef79d56-0e4b-4c58-8ce5-ee0159ccb4c7'></a>

934

<a id='a0d70388-62d5-4fa4-8d8b-a63633d29b55'></a>

L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='b31a3428-2a6e-4f2e-9af0-64cf78b5df51'></a>

response rates. The simulation shows that about 50 % of patients achieved a partial response, which is a 15 % increase over our original response rates. It is interesting to note that although the partial response rate is increased, the number of patients who with a complete response to the drug is not changed. We present the outcomes of an individual patient in figure 8 that would benefit from the doubled dosage of sunitinib. With no treatment, this patient's tumor grows to carrying capacity, as expected. With normal sunitinib treatment, this patient achieves a partial response. Then, when we double the dose amount, the patient achieves a complete response by day 300.

<a id='a66f4744-d7ad-495b-bdb4-462cd541bf47'></a>

<::chart: Bar chart titled "Patient Responses -- Sunitinib Double Dose". The y-axis is labeled "Percentage of Patients" and ranges from 0 to 100. The x-axis is labeled "Type of Response" and shows three categories: "Complete Response", "Partial Response", and "No Response". There are three red bars representing these categories. The "Complete Response" bar reaches approximately 5%. The "Partial Response" bar reaches 50%. The "No Response" bar reaches approximately 44%.::>

FIGURE 7. Simulation of 100 patients. Tumor growth after 300 days with amount of sunitinib treatment administered daily doubled from the amount outlined in section 4.7. Immune strength parameters $d$ and $l$ sampled from a uniform distribution within [1.7, 2.2]. Initial tumor size for all patients $1 \times 10^8$.

<a id='247a3697-09be-4a3f-99a3-afab7760068f'></a>

5.4. **Parameter sensitivity.** We carried out a numerical parameter sensitivity analysis on the system of differential equations with no treatment intervention. We followed the standard approach of changing one parameter at a time by a certain percent (both increasing and decreasing) while leaving all other parameters fixed. Numerical initial condition values for all but the initial tumor size were chosen to be the no-tumor homeostasis values provided in section 3. Initial tumor size was set to 1.78 × 10^7 cells, somewhat lower than the high-tumor equilibrium values for this model. We measured the effect of varying each parameter by evaluating the resulting percent change in final tumor size on day t_final = 300. The percent change in final tumor size as a result of each parameter change can be seen in figure 9.

<a id='b6224320-9cee-4069-9ce7-c2bea5cf54ad'></a>

In figure 9 it is clear that there are three parameters that have the greatest impact on final tumor size. These are a, intrinsic tumor growth rate, c, a measure associated with NK cell effectiveness, and l, a measure associated with T cell effectiveness. It seems biologically reasonable that these three parameters should affect the system outcome significantly. It is also interesting to note that it may be possible to determine patient-specific values for these important parameters, as was highlighted in de Pillis et al. (2005) [15].

<!-- PAGE BREAK -->

<a id='fcfbfc02-13b2-44d7-a1ea-0a3505d378b1'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 935

<a id='22fa5ab8-f791-437c-a4cc-a8f7949d683b'></a>

<::chart: FIGURE 8. Individual patient dynamics. Top panel: Model Simulation: No Response, No Treatment. This line chart shows states (logarithmic scale) on the y-axis from 10^0 to 10^12 and time (days) on the x-axis from 0 to 300. The legend includes: Tumor Cells (black line), Natural Killer Cells (green line), CD8+ T Cells (blue line), Regulatory T Cells (red line), Circulating Lymphocytes (cells) (cyan line), IL-2 (IU) (yellow line), Sunitinib (mg) (dashed red line). The tumor cells show continuous growth. Middle panel: Model Simulation: Partial Response, Normal Sunitinib Treatment. This line chart shows states (logarithmic scale) on the y-axis from 10^0 to 10^12 and time (days) on the x-axis from 0 to 300. The legend includes the same elements as the top panel. The tumor cells initially decrease then resume growth. The Sunitinib line shows intermittent pulses. Bottom panel: Model Simulation: Complete Response, Double Dose. This line chart shows states (logarithmic scale) on the y-axis from 10^0 to 10^12 and time (days) on the x-axis from 0 to 300. The legend includes: Tumor Cells (black line), Natural Killer Cells (cells/L) (green line), CD8+ T Cells (cells/L) (blue line), Regulatory T Cells (cells/L) (red line), Circulating Lymphocytes (cells/L) (cyan line), IL-2 (IU/L) (yellow line), Sunitinib (mg/L) (dashed red line). The tumor cells significantly decrease to near zero. The Sunitinib line shows intermittent pulses with higher peaks than the middle panel. In our simulation, this patient had d and l values of 1.72989.::>

<a id='09b50358-f0f2-4fd2-9466-c0a61261f867'></a>

6. Discussion. The goal of the model presented in this paper was to explore the interaction between tumor growth and the activity of regulatory T cells (Treg cells), and how these might vary according to patient-specific immune strength. Tumor model parameters were chosen to reflect renal cell carcinoma. Sunitinib, a drug that can suppress the activity of regulatory T cells, was the treatment simulated. We have demonstrated that the model with the chosen parameter set can give simulated results that qualitatively and quantitatively reflect clinic study data.

<a id='95e27cd3-9dd2-45cd-a3ea-fe2ac77aa1d6'></a>

1. **Model Validation**: In a simulated sample population of 100, sunitinib treatments following standard protocols led to improved tumor control in approximately 30% to 40% of patients, which reflects the numbers seen in clinical studies.
2. **Hypothetical Dosing**: Simulations of experimental sunitinib treatments at double the standard dose led to a greater response rate in about 15% the patient population. However, about 45% of patients still had no objective response, even to the larger dose treatment.
3. **Role of Patient Specific Immune Strength**: The key in the difference between patients that responded well to sunitinib and those who did not

<!-- PAGE BREAK -->

<a id='dd538744-a80f-4fa4-972b-e6e2d8f7f817'></a>

936

<a id='1c6370d1-7be9-440a-8e3b-8aa1d669dc42'></a>

L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='0e1aa9e8-1143-488a-9c3a-246ce13d9cae'></a>

<::bar chart
Title: Parameters Changed by 0.1 percent
Y-axis: Percent Change in Final Tumor Size After 300 days (ranging from -100 to 40)
X-axis: Parameter Changed
Legend:
  - Increased (white bars)
  - Decreased (black bars)

Data:
- Parameter 'a': Increased: ~0%, Decreased: ~-100%
- Parameter 'b': Increased: ~25%, Decreased: ~0%
- Parameter 'c': Increased: ~0%, Decreased: ~25%
- Parameter 'λ_T e/f': Increased: ~15%, Decreased: ~-30%
- Parameter 'f': Increased: ~0%, Decreased: ~0%
- Parameter 'p': Increased: ~0%, Decreased: ~0%
- Parameter 'P_N': Increased: ~0%, Decreased: ~0%
- Parameter 'g_N': Increased: ~0%, Decreased: ~0%
- Parameter 'm': Increased: ~2%, Decreased: ~0%
- Parameter 'j': Increased: ~0%, Decreased: ~-2%
- Parameter 'k': Increased: ~0%, Decreased: ~0%
- Parameter 'q': Increased: ~0%, Decreased: ~0%
- Parameter 'r_1': Increased: ~5%, Decreased: ~-5%
- Parameter 'r_2': Increased: ~-5%, Decreased: ~5%
- Parameter 'z': Increased: ~0%, Decreased: ~0%
- Parameter 'κ': Increased: ~0%, Decreased: ~0%
- Parameter 'p_1': Increased: ~0%, Decreased: ~0%
- Parameter 'g_1': Increased: ~0%, Decreased: ~0%
- Parameter 'w': Increased: ~10%, Decreased: ~-5%
- Parameter 'u': Increased: ~-30%, Decreased: ~15%
- Parameter 'p': Increased: ~0%, Decreased: ~0%
- Parameter 'P_R': Increased: ~0%, Decreased: ~0%
- Parameter 'g_R': Increased: ~0%, Decreased: ~0%
- Parameter 'H_R': Increased: ~0%, Decreased: ~0%
- Parameter 'λ_R α/β': Increased: ~0%, Decreased: ~0%
- Parameter 'β': Increased: ~0%, Decreased: ~0%
- Parameter 'μ_1': Increased: ~0%, Decreased: ~0%
- Parameter 'φ': Increased: ~0%, Decreased: ~0%
- Parameter 'ω': Increased: ~10%, Decreased: ~-5%
- Parameter 'ζ': Increased: ~-5%, Decreased: ~10%
- Parameter 'η': Increased: ~0%, Decreased: ~0%
- Parameter 'd': Increased: ~25%, Decreased: ~-5%
- Parameter 'l': Increased: ~-100%, Decreased: ~5%
- Parameter 's': Increased: ~5%, Decreased: ~-5%
: bar chart::>

<a id='4cdc94f4-9676-4c67-a7a2-6cea23c58693'></a>

FIGURE 9. Parameter sensitivity. Change in final tumor size after 300 days in response to 0.1% change in parameter value. Initial tumor size is 1.78 x 10^7 cells. All other initial values are the no-tumor homeostasis values provided in section 3. Baseline values for l and d are 1.7.

<a id='aea00292-a07d-4043-8cd2-3fc779cd8b72'></a>

was the relative immune strength of each patient, reflected in the model by varying the values of the parameters d and l. These two parameters affect the strength of T cell control of a tumor. However, as can be seen from the parameter sensitivity analysis, increasing l weakens tumor control, while increasing d strengthens tumor control. In our simulations, we assigned l and d the same values, allowing these parameters to increase or decrease together. With this approach, we did not give one group of patients a clear advantage over another. This was one way of capturing possible differences in individual patient immune strengths, but other approaches are possible.

<a id='148d0693-86d3-41c5-a525-afdd193835ee'></a>

From the sensitivity analysis as well as the simulation of all possible $(d, l)$ pairs in figure 5, we see that the effect of shrinking parameter $l$ is greater than the counter-effect of increasing parameter $d$. This explains why, in our simulations, the lower the values of $l$ and $d$, the better the patient responded to treatment. It is interesting to note that with no treatment, the differences in relative immune strength, when constraining $l$ and $d$ to values within the parameter range 1.7 to 2.2, did not affect tumor growth. It was only in the presence of sunitinib treatment that innate immune differences affected patient outcomes. Tumor control without medication could be achieved for values of $l \leq 1$, but $l$-values measured in patients may tend to be larger than 1[15]. The connection between innate immune strength and patient prognosis may be very significant. When patient-specific immune parameters can be measured - and it is possible to do so in certain cases [15] - this may give clinicians

<!-- PAGE BREAK -->

<a id='f0cae6c3-bd98-47ea-9524-ceee8de2785b'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 937

<a id='0d049d3f-25c4-499c-b395-3d3a8d68fb06'></a>

the ability to predict which patients have a good chance of responding well to
certain immunotherapies, and which patients do not. It may also allow the
personalizing of treatments based on patient parameters.

<a id='b063c2da-cb8e-46c5-be29-fefd13b31528'></a>

7. Future directions. There are some modifications that may be useful to implement in future versions of this model. One possibility is to model explicitly the activity CD4+ helper T cells as a separate population, rather than including them in the circulating lymphocyte population. In the current model, circulating lymphocytes are assumed to include, and therefore act as a proxy for, the CD4+ T cell population. It is known that CD4+ T cells are the main producers of IL-2, as well as the source of Treg cells [2]. It is also known that sunitinib modulates Treg activity by decreasing CD4+ T cell differentiation into Treg cells rather than killing the Treg cells directly [31].Sunitinib is a tyrosine kinase inhibitor, meaning that it acts by blocking the receptors of numerous tumor growth factors [55]. Since one goal of our model was to test the endpoint effects that sunitinib can have through reducing the number of Treg cells in the system, we chose to keep our model simple and focus on the end result of sunitinib administration rather than the explicit pathways through which sunitinib achieves Treg down-regulation. However, determining a way to model the exact mechanism by which sunitinib decreases Treg cells may be worthwhile. Having a separate CD4+ T cell compartment could facilitate more accurately modeling IL-2, Treg, and sunitinib dynamics. More accurately modeling IL-2 activity would also allow us to include exogenous IL-2 treatments in the model, thus allowing us to explore optimizing combination IL-2 and sunitinib therapies.

<a id='05a4382b-2700-4b22-9b22-42d6b7441da2'></a>

Finally, an important model extension would be to account for drug toxicity and autoimmune reactions. It is known that high doses of both IL-2 and sunitinib have potentially toxic effects on the body. Currently, our model does not account for negative side effects when implementing experimental dosages. The additional amount of treatment needed to improve response rates could cause so much harm to the patients that it cannot be considered feasible in the clinic.

<a id='f43c7550-f670-4a37-8e09-561fa65cf26c'></a>

# REFERENCES

1.  A. K. Abbas, A. H. Lichtman and S. Pillai, "*Cellular and Molecular Immunology*," Elsevier Saunders, 6th ed. edition, 2007.
2.  Paul Andrew Antony and P. Restifo Nicholas, *CD4+CD25+ T regulatory cells, immunotherapy of cancer, and interleukin-2*, Journal of Immunotherapy, **28** (2005), 120–128.
3.  American Surgical Association, New York Surgical Society, Philadelphia Academy of Surgery, Southern Surgical Association (U.S.) and Central Surgical Association, "Annals of Surgery," Lippincott, Williams and Wilkins, 1914.
4.  D. Avigan, *Dendritic cells: development, function and potiental use for cancer immunotherapy*, Blood Reviews, **13** (1999), 51–64.
5.  Nicola Bellomo, Abdelghani Bellouquid, Juan Nieto and Juan Soler, *Multiscale biological tissue models and flux-limited chemotaxis for multicellular growing systems*, Mathematical Models and Methods in Applied Sciences, **20** (2010), 1179–1207.
6.  Anamika Bose, Jennifer L. Taylor, Sean Alber, Simon C. Watkins, Jorge A. Garcia, Brian I. Rini, Jennifer S. Ko, Peter A. Cohen, James H. Finke, and Walter J. Storkus, *Sunitinib facilitates the activation and recruitment of therapeutic anti-tumor immunity in concert with specific vaccination*, International Journal of Cancer, **129** (2011), 2158–2170.
7.  G. C. Cesana et al, *Characterization of CD4+ CD25+ regulatory T cells in patients treated with high-dose interleukin-2 for metastatic melanoma or renal cell carcinoma*, Journal of Clinical Oncology, **24** (2006), 1169–1177.
8.  Ann F. Chambers, Alan C. Groom and Ian C. MacDonald, *Metastasis: Dissemination and growth of cancer cells in metastatic sites*, Nature Reviews Cancer, **2** (2002), 563–572.

<!-- PAGE BREAK -->

<a id='230ab279-d7ce-42c0-a6a4-acbfd21f064e'></a>

938 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='12d64359-e45d-416e-ba81-f68414fe8a05'></a>

[9] Z. Z. Chen, S. Y. Zhang, Q. S. Liu, P. F. Xiao, X. Y. Guo and Z. H. Lu, Theoretical and experimental studies on filtering tumor cells from blood cell mixture with dam structure in microuidic devices, In "Engineering in Medicine and Biology 27th Annual Conference," 2005.
[10] Kristin Cobb, Modeling cancer biology, Biomedical Computation Review, (2007), 17-24.
[11] J. Dannull, Z. Su, D. Rizzieri, B. K. Yang, D. Coleman, D. Yancey, A. Zhang, P. Dahm, N. Chao, E. Gilboa and J. Vieweg, *Enhancement of vaccine-mediated antitumor immunity in cancer patients after depletion of regulatory T cells*, The Journal of Clinical Investigation, **115** (2005), 3623-3633.
[12] R. J. De Boer, H. Mohri, D. D. Ho and A. S. Perelson, Turnover rates of B cells, T cells, and NK cells in simian immunodeficiency virus-infected and uninfected rhesus macaques, Journal of Immunology, **170** (2003), 2479-2487.
[13] L. G. de Pillis, K. R. Fister, W. Gu, C. Collins, M. Daub, D. Gross, J. Moore and B. Preskill, *Mathematical model creation for cancer chemo-immunotherapy*, Computational and Mathe- matical Methods in Medicine, **10** (2009), 165-184.
[14] L. G. de Pillis, W. Gu and A. E. Radunskaya, *Mixed immunotherapy and chemotherapy of tu- mors: Modeling, applications, and biological interpretations*, Journal of Theoretical Biology, **238** (2006), 841-862.
[15] L. G. de Pillis, A. E. Radunskaya and C. L. Wiseman, A validated mathematical model of cell-mediated immune response to tumor growth, Cancer Research, **65** (2005), 7950-7958.
[16] L. G. de Pillis and A. E. Radunskaya, Immune response to tumor invasion, In K.J. Bathe, editor, Computational Fluid and Solid Mechanics, M.I.T., **2** (2003), 1661-1668.
[17] V. De Vita, Jr., S. Hellman and S. Rosenberg, "Cancer: Principles and Practice of Oncology," Lippincott Williams & Wilkins, 7th ed. edition, 2000.
[18] Thomas S. Deisboeck, Zhihui Wang, Paul Macklin and Vittorio Cristini, Multiscale cancer modeling, Annual Reviews Biomedical Engineering, **13** (2011), 127-155.
[19] I. M. Desar, J. F. M. Jacobs, C. A. Hulsbergen-vandeKaa, W. J. Oyen, P. F. Mulders, W. T. van der Graaf, G. J. Adema, C. M. van Herpen and I. J. de Vries, Sorafenib reduces the percentage of tumour infiltrating regulatory T cells in renal cell carcinoma patients, Interna- tional Journal of Cancer, **129** (2011), 507-512.
[20] A. Diefenbach, E. R. Jensen, A. M. Jamieson and D. Raulet. Rael and H60 ligands of the NKG2D receptor stimulate tumor immunity, Nature, **413** (2001), 165-171.
[21] C. Doehn et al, Mode-of-action, efficacy, and safety of a homologous multi-epitope vaccine in a murine model for adjuvant treatment of renal cell carcinoma, European Urology, **56** (2009), 123-133.
[22] J. Dunne, S. Lynch, C. O'Farrelly, S. Todryk, J. E. Hegarty, C. Feighery and D. G. Doherty, Selective expansion and partial activation of human NK cells and NK receptor-positive T cells by IL-2 and IL-15, Journal of Immunology, **167** (2001), 3129-3138.
[23] E. A. Eisenhauer, P. Therasse, J. Bogaerts, L. H. Schwartz, D. Sargent, R. Ford, J. Dancey, S. Arbuck, S. Gwyther, M. Mooney, L. Rubinstein, L. Shankar, L. Dodd, R. Kaplan, D. La- combe and J. Verweij, New response evaluation criteria in solid tumors: Revised recist guide- line (version 1.1), European Journal of Cancer, **45** (2009), 228-247.
[24] S. Faivre et al, Safety, pharmacokinetic, and antitumor activity of su11248, a novel oral multitarget tyrosine kinase inhibitor, in patients with cancer, Journal of Clinical Oncology, **24** (2006), 25-35.
[25] J. H. Finke et al, Sunitinib reverses type-1 immune suppression and decreases t-regulatory cells in renal cell carcinoma patients, Clinical Cancer Research, **14** (2008), 6674-6682.
[26] Ester Gabetta and Eugenio Regazzini, *About the gene families size distribution in a re- cent model of genome evolution*, Mathematical Models and Methods in Applied Sciences, **20** (2010), 1005-1020.
[27] P. Gao, Q. Ding, Z. Wu, H. Jiang and Z. Fang, Therapeutic potential of human mesenchymal stem cells producing IL-12 in a mouse xenograft model of renal cell carcinoma, Cancer Letters, **290** (2010), 157-166.
[28] S. N. Gardner, A mechanistic, predictive model of dose-response curves for cell cycle phase- specific and non-specific drugs, Cancer Research, **60** (2000), 1417-1425.
[29] J. F. Gillooly, J. H. Brown, G. B. West, V. M. Savage and E. L. Charnov, Effects of size and temperature on metabolic rate, Science, **293** (2001), 2248-2251.
[30] R. W. Griffiths, E. Elkord, D. E. Gilham, V. Ramani, N. Clarke, P. L. Stern and R. E. Hawkins, Frequency of regulatory T cells in renal cell carcinoma patients and investigation of correlation with survival, Cancer Immunology, Immunotherapy, **56** (2007), 1743-1753.

<!-- PAGE BREAK -->

<a id='b92be5f6-78ec-4094-b3ae-36eadc1d9b14'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 939

<a id='9a33b75d-9cb9-4a07-b4db-23b26f7e8d75'></a>

[31] Y. Gu, W. Zhao, F. Meng, B. Qu, X. Zhu, Y. Sun, Y. Shu and Q. Xu, Sunitinib impairs the proliferation and function of human peripheral T cell and prevents t-cell-mediated immune response in mice, Clinical Immunology, **135** (2010), 55-62.
[32] Lijie He, Yuee Teng, Bo Jin, Mingfang Zhao, Ping Yu, Xuejun Hu, Jingdong Zhang, Songbai Li, Yaling Gao and Yunpeng Liu, Initial partial response and stable disease according to RECIST indicate similar survival for chemotherapeutical patients with advanced non-small cell lung cancer, BMC Cancer, **10** (2010), 1-11.
[33] M. Hellerstein, M. B. Hanley, D. Cesar, S. Siler, C. Papageorgopoulos, E. Wieder, D. Schmidt, R. Hohl, R. Neese, D. Macallan, S. Deels and J. M. McCune, Directly measured kinetics of circulating t lymphocytes in normal and hiv-1-infected humans, Nature Medicine, **5** (1999), 83-89.
[34] Alex Y. C. Huang, Paul Golumbek, Mojgan Ahmadzadeh, Elizabeth Jaffee, Drew Pardoll and Hyam Levitsky, Role of bone marrow-derived cells in presenting mhc class i-restricted tumor antigens, Science, SE: New Series, **264** (1994), 961-965.
[35] RxList Inc, "Doxil Drug Description," July 2008.
[36] C. A. Janeway, Jr., P. Travers, M. Walport and M. J. Shlomchik, "Immunobiology," Garland Science Publishing, 5th ed. edition, 2005.
[37] H. Jonuleit and E. Schmitt, The regulatory T cell family: distinct subsets and their interre- lations, Journal of Immunology, **171** (2003), 6323-6327.
[38] H. Jonuleit, E. Schmitt, H. Kakirman, M. Stassen, J. Knop and A. H. Enk, Infectious toler- ance: Human CD25+4 regulatory T cells convey suppressor activity to conventional CD4+ T helper cells, Journal of Experimental Medicine, **196** (2002), 255-260.
[39] Denise Kirschner and John Carl Panetta, Modeling immunotherapy of the tumor - immune interaction, Journal of Mathematical Biology, **37** (1998), 235-252.
[40] J. S. Ko et al, Sunitinib mediates reversal of myeloid-derived suppressor cell accumulation in renal cell carcinoma patients, Clinical Cancer Research, **6** (2009), 2148-2157.
[41] M. W. Konrad, G. Hemstreet, E. M. Hersh, P. W. A. Mansell, R. Mertelsmann, J. E. Kolitz and E. C. Bradley, Pharmacokinetics of recominbant interleukin 2 in humans, Cancer Re- search, **50** (1990), 2009-2017.
[42] Natalie Kronik, Yuri Kogan, Moran Elishmereni, Karin Halevi-Tobias, Stanimir Vuk-Pavlovic and Zvia Agur, Predicting outcomes of prostate cancer immunotherapy by personalized math- ematical models, PLOS ONE, **5** (2010), 1-8.
[43] Vladimir A. Kuznetsov, Iliya A. Makalkin, Mark A. Taylor and Alan S. Perelson, Nonlinear dynamics of immunogenic tumors: Parameter estimation and global bifurcation analysis, Bulletin of Mathematical Biology, **56** (1994), 295-321.
[44] P. P. Lee, C. Yee, P. A. Savage, L. Fong, D. Brockstedt, J. S. Weber, D. Johnson, S. Swetter, J. Thompson, P. D. Greenberg, M. Roederer and M. M. Davis, Characterization of circulating T cells specific for tumor-associated antigens in melanoma patients, Nature Medicine, **5** (1999), 677-85.
[45] K. Leon, K. Garcia, J. Carneiro and A. Lage, _How regulatory CD25(+)CD4(+) T cells impinge on tumor immunobiology? On the existence of two alternative dynamical classes of tumors_, Journal of Theoretical Biology, **247** (2007), 122-137.
[46] K. Leon, K. Garcia, J. Carneiro and A. Lage, _How regulatory CD25(+)CD4(+) T cells impinge on tumor immunobiology: The differential response of tumors to therapies_, The Journal of Immunology, **179** (2007), 5659-5668.
[47] X. S. Li, X. Wu, P. J. Zhao, L. H. Huang, Y. Song, K. Gong, C. Shen, W. Yu, G. Song, Z. Zhao, Z. Zhang, Q. Zhang, G. Wang, Z. S. He, L. Q. Zhou and J. Jin, Efficacy and safety of sunitinib in the treatment of metastatic renal cell carcinoma, China Medical Journal, **124** (2011), 2920-2924.
[48] N. H. E. Mabarrack, N. L. Turner and G. Mayrhofer, Recent thymic origin, differentiation, and turnover of regulatory T cells, Journal of Leukocyte Biology, **84** (2008), 1287-1297.
[49] T. R. Malek and A. L. Bayer, Tolerance, not immunity, crucially depends on IL-2, Nature Reviews: Immunology, **4** (2004), 665-674.
[50] N. J. Meropol, G. M. Barresi, T. A. Fehniger, J. Hitt, M. Franklin and M. A. Caligiuri, Evalu- ation of natural killer cell expansion and activation in vivo with daily subcutaneous low-dose interleukin-2 plus periodic intermediate-dose pulsing, Cancer Immunology, Immunotherapy, **46** (1998), 318-326.
[51] R. J. Motzer, N. H. Bander and D. M. Nanus, Medical progress: renal-cell carcinoma, New England Journal of Medicine, **335** (1996), 865-875.

<!-- PAGE BREAK -->

<a id='c9a6e066-7e47-46b9-b83c-4262a7a9138c'></a>

940 L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='b14057a7-3127-446c-8cf3-af393b0593a6'></a>

[52] R. J. Motzer et al, Sunitinib in patients with metastatic renal cell carcinoma, Journal of the American Medical Association, 295 (2006), 2516-2524.
[53] R. J. Motzer et al, Sunitinib versus interferon alfa in metastatic renal-cell carcinoma, New England Journal of Medicine, 356 (2007), 115-124.
[54] M. Orditura, C. Romano, F. De Vita, G. Galizia, E. Lieto, S. Infusino, G. De Cataldis and G. Catalano, Behaviour of interleukin-2 serum levels in advanced non-small-cell lung cancer patients: relationship with response to therapy and survival, Cancer Immunology, Immunotherapy, 49 (2000), 530-536.
[55] J. Ozao-Choy et al, The novel role of tyrosine kinase inhibitor in the reversal of immune suppression and modulation of tumor microenvironment for immune-based cancer therapies, Cancer Research, 69 (2009), 2514-2522.
[56] Johan Paulsson, Models of stochastic gene expression, Physics of Life Reviews, 2 (2005), 157-175.
[57] Novartis Pharmaceuticals, "Proleukin (aldesleukin), Pharmacology and Indications," January 2007.
[58] M. J. Pittet et al, High frequencies of naive melan-a/MART-1-specific CD8+ T cells in a large proportion of human histocompatibility leukocyte antigen (HLA)-A2 individuals, Journal of Experimental Medicine, 190 (1999), 705-715.
[59] A. Raman, R. J. Colman, Y. Cheng, J. W. Kemnitz, S. T. Baum, R. Weindruch and D. A. Schoeller, Reference body composition in adult rhesus monkeys: Glucoregulatory and anthropometric indices, Journal of Gerontology Series A, 60 (2005), 1518-1524.
[60] Yosef Refaeli, Luk Van Parijs, Cheryl A. London, Jurg Tschopp and Abul Abbas, Biochemical mechanisms of IL-2-regulated Fas-mediated T cell apoptosis, Immunity, 8 (1998), 616-623.
[61] Christiane Ruedl, Pascale Koebel, Martin Bachmann, Michael Hess and Klaus Karjalainen, Anatomical origin of dendritic cells determines their life span in peripheral lymph nodes, Journal of Immunology, 165 (2000), 4910-4916.
[62] S. A. Siddiqui, X. Frigola, S. Bonne-Annee, M. Mercader, S. M. Kuntz, A. E. Krambeck, S. Sengupta, H. Dong, J. C. Cheville, C. M. Lohse, C. J. Krco, W. S. Webster, B. C. Leibovich, M. L. Blute, K. L. Knutson and E. D. Kwon, Tumor-infiltrating Foxp3-CD4+CD25+ T cells predict poor survival in renal cell carcinoma, Clinical Cancer Research, 13 (2007), 2075-2081.
[63] Renee N. Salas, James H. Finke and Brian I. Rini, The intersection of sunitinib with the immunosuppressive microenvironment of renal cell carcinoma: implications for future therapeutics, Targeted Oncology, 2 (2007), 225-234.
[64] Sandeep Sanga, John P Sinek, Hermann B Frieboes, Mauro Ferrari, John P Fruehauf and Vittorio Cristini, Mathematical modeling of cancer progression and response to chemotherapy, Expert Review of Anticancer Therapy, 6 (2006), 1361-1376.
[65] D. E. Speiser et al, The activatory receptor 2B4 is expressed in vivo by human CD8+ effector alpha beta T cells, Journal of Immunology, 167 (2001), 6165-6170.
[66] P. Trzonkowski, E. Szmit, J. Mysliwska, A. Dobyszuk and A. Msyliwski, CD4+CD25+ T regulatory cells inhibit cytotoxic activity of T CD8+ and NK lymphocytes in the direct cell-to-cell interaction, Clinical Immunology, 112 (2004), 258-267.
[67] D. F. Williamson, Descriptive epidemiology of body weight and body weight change in u.s. adults, Annals of Internal Medicine, 119 (1993), 646-649.
[68] A. Yu and T. R. Malek, Selective availability of IL-2 is a major determinant controlling the production of CD4+CD25+Foxp3+ T regulatory cells, Journal of Immunology, 177 (2006), 5115-5121.

<a id='11cff218-7c8f-4f3b-9b64-893787c396e5'></a>

Appendix A. **Reference tables.** The reference tables below provide a quick ref- erence for parameter values, as well as descriptions of parameters and equation terms.

<a id='3698839e-8f39-4732-b38c-3dfbccc68349'></a>

Table 1: Equation Descriptions

<a id='329ef491-af66-4a86-8873-d58b38492aee'></a>

<table id="25-1">
<tr><td id="25-2">ODE</td><td id="25-3">Term</td><td id="25-4">Description</td></tr>
<tr><td id="25-5">dT/dt</td><td id="25-6">aT(1-bT)</td><td id="25-7">Logistic tumor growth</td></tr>
<tr><td id="25-8"></td><td id="25-9">-ce^{-\lambda rR}NT</td><td id="25-a">NK-induced tumor death with T_{reg} inhibition</td></tr>
<tr><td id="25-b"></td><td id="25-c"></td><td id="25-d">Continued on next page</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='c41b8bb4-0acb-4e92-a238-a14f99ffdd02'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 941

<a id='8c312451-962e-40d8-b2b9-dfac0e465636'></a>

Table 1: Equation Descriptions

<a id='ec7df65a-ee75-4677-bc0e-89b71f7a246d'></a>

<table id="26-1">
<tr><td id="26-2">ODE</td><td id="26-3">Term</td><td id="26-4">Description</td></tr>
<tr><td id="26-5"></td><td id="26-6">-DT</td><td id="26-7">CD8+ T cell induced tumor death</td></tr>
<tr><td id="26-8">dN/dt</td><td id="26-9">eC</td><td id="26-a">Production of NK cells from circulating lympho- cytes</td></tr>
<tr><td id="26-b"></td><td id="26-c">-fN</td><td id="26-d">NK turnover</td></tr>
<tr><td id="26-e"></td><td id="26-f">-pNT</td><td id="26-g">NK death by exhaustion of tumor-killing resources</td></tr>
<tr><td id="26-h"></td><td id="26-i">(pNNI/gN+I)</td><td id="26-j">Stimulatory effect of IL-2 on NK cells</td></tr>
<tr><td id="26-k">dL/dt</td><td id="26-l">-mL</td><td id="26-m">CD8+ T cell turnover</td></tr>
<tr><td id="26-n"></td><td id="26-o">-qLT</td><td id="26-p">CD8+ T cell death by exhaustion of tumor-killing resources</td></tr>
<tr><td id="26-q"></td><td id="26-r">r1NT</td><td id="26-s">CD8+ T cell stimulation by NK-lysed tumor cell debris</td></tr>
<tr><td id="26-t"></td><td id="26-u">r2CT</td><td id="26-v">Activation of naive CD8+ T cells in general lymphocyte population</td></tr>
<tr><td id="26-w"></td><td id="26-x">(p_I LI/g_I + I)</td><td id="26-y">Stimulatory effect of IL-2 on CD8+ T cells</td></tr>
<tr><td id="26-z"></td><td id="26-A">(-zL^2RI/\kappa+I)</td><td id="26-B">Inhibition of CD8+ T cells by T_reg cells</td></tr>
<tr><td id="26-C"></td><td id="26-D">(jTL/k+T)</td><td id="26-E">CD8+ T cell stimulation by CD8+ T cell-lysed tumor cell debris</td></tr>
<tr><td id="26-F">dR/dt</td><td id="26-G">wC</td><td id="26-H">Production of T_reg cells from circulating lymphocytes</td></tr>
<tr><td id="26-I"></td><td id="26-J">-uR</td><td id="26-K">T_reg cell turnover</td></tr>
<tr><td id="26-L"></td><td id="26-M">(pRRl/gR + I)</td><td id="26-N">Stimulatory effect of IL-2 on Treg cells</td></tr>
<tr><td id="26-O"></td><td id="26-P">-HR(1-e^{-\lambda RS})R</td><td id="26-Q">Inhibition of Treg cells due to sunitinib</td></tr>
<tr><td id="26-R">dC/dt</td><td id="26-S">\alpha</td><td id="26-T">Lymphocyte synthesis in bone marrow</td></tr>
<tr><td id="26-U"></td><td id="26-V">-\beta C</td><td id="26-W">Lymphocyte turnover</td></tr>
<tr><td id="26-X">dI/dt</td><td id="26-Y">-\mu I</td><td id="26-Z">IL-2 turnover</td></tr>
<tr><td id="26-10"></td><td id="26-11">C</td><td id="26-12">Production of IL-2 due to naive CD8+ T cells and CD4+ T Cells</td></tr>
<tr><td id="26-13"></td><td id="26-14">(wLI/ζ + I)</td><td id="26-15">Production of IL-2 from activated CD8+ T cells</td></tr>
<tr><td id="26-16">dS/dt</td><td id="26-17">-ηS</td><td id="26-18">Excretion and elimination of sunitinib</td></tr>
<tr><td id="26-19"></td><td id="26-1a">vs(t)</td><td id="26-1b">Sunitinib injection</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='4ddff99b-77ed-4f1b-bf10-fab23bcb05e8'></a>

942

<a id='4b3cc192-3e36-482b-946c-8230cccdb187'></a>

L. DE PILLIS, T. CALDWELL, E. SARAPATA AND H. WILLIAMS

<a id='a69c5a22-51b0-4585-ab11-803eb90485e3'></a>

Table 2: Parameter Descriptions

<a id='7639256f-9479-4e08-a535-18d1e62726db'></a>

<table id="27-1">
<tr><td id="27-2">ODE</td><td id="27-3">Param</td><td id="27-4">Description</td></tr>
<tr><td id="27-5">dT/dt</td><td id="27-6">a</td><td id="27-7">Growth rate of tumor</td></tr>
<tr><td id="27-8"></td><td id="27-9">b</td><td id="27-a">Inverse of carrying capacity</td></tr>
<tr><td id="27-b"></td><td id="27-c">c</td><td id="27-d">Maximal rate of NK-induced tumor death</td></tr>
<tr><td id="27-e"></td><td id="27-f">λT</td><td id="27-g">Treg induced NK inhibition coefficient</td></tr>
<tr><td id="27-h"></td><td id="27-i">d</td><td id="27-j">Immune system strength coefficient</td></tr>
<tr><td id="27-k"></td><td id="27-l">l</td><td id="27-m">Immune strength scaling coefficient</td></tr>
<tr><td id="27-n"></td><td id="27-o">s</td><td id="27-p">Value of (L/T) for half-maximal CD8+ toxicity</td></tr>
<tr><td id="27-q">dN/dt</td><td id="27-r">e/f</td><td id="27-s">Ratio of NK cell synthesis rate to turnover rate</td></tr>
<tr><td id="27-t"></td><td id="27-u">f</td><td id="27-v">Rate of NK cell turnover</td></tr>
<tr><td id="27-w"></td><td id="27-x">p</td><td id="27-y">Rate of NK cell death due to tumor interaction</td></tr>
<tr><td id="27-z"></td><td id="27-A">p_N</td><td id="27-B">Rate of IL-2 induced NK cell proliferation</td></tr>
<tr><td id="27-C"></td><td id="27-D">g_N</td><td id="27-E">Concentration of IL-2 for half-maximal NK cell proliferation</td></tr>
<tr><td id="27-F">dL/dt</td><td id="27-G">m</td><td id="27-H">Rate of activated CD8+ T cell turnover</td></tr>
<tr><td id="27-I"></td><td id="27-J">q</td><td id="27-K">Rate of CD8+ T cell death due to tumor interaction</td></tr>
<tr><td id="27-L"></td><td id="27-M">r_1</td><td id="27-N">Rate of NK-lysed tumor cell debris activation CD8+ cells</td></tr>
<tr><td id="27-O"></td><td id="27-P">r_2</td><td id="27-Q">Rate of CD8+ production from circulating lymphocytes</td></tr>
<tr><td id="27-R"></td><td id="27-S">p_1</td><td id="27-T">Rate of IL-2 induced CD8+ T cell activation</td></tr>
<tr><td id="27-U"></td><td id="27-V">g_1</td><td id="27-W">Concentration of IL-2 for half-maximal CD8+ T cell activation</td></tr>
<tr><td id="27-X"></td><td id="27-Y">z</td><td id="27-Z">T_reg induced CD8+ T cell inhibition coefficient</td></tr>
<tr><td id="27-10"></td><td id="27-11">κ</td><td id="27-12">Concentration of IL-2 to halve magnitude of CD8+ inhibition</td></tr>
<tr><td id="27-13"></td><td id="27-14">j</td><td id="27-15">Rate of CD8+ T cell-lysed tumor debris activation of CD8+ T cells</td></tr>
<tr><td id="27-16"></td><td id="27-17">k</td><td id="27-18">Tumor size for half-maximal CD8+ T cell-lysed debris CD8+ T cell activation</td></tr>
<tr><td id="27-19">dR/dt</td><td id="27-1a">w/u</td><td id="27-1b">Ratio of Treg synthesis rate to turnover rate</td></tr>
<tr><td id="27-1c"></td><td id="27-1d">u</td><td id="27-1e">Rate of Treg turnover</td></tr>
<tr><td id="27-1f"></td><td id="27-1g">pR</td><td id="27-1h">Rate of IL-2 induced Treg proliferation</td></tr>
<tr><td id="27-1i"></td><td id="27-1j">gR</td><td id="27-1k">Concentration of IL-2 for half-maximal Treg activation</td></tr>
<tr><td id="27-1l"></td><td id="27-1m">HR</td><td id="27-1n">Rate of Treg inhibition from sunitinib</td></tr>
<tr><td id="27-1o"></td><td id="27-1p">λR</td><td id="27-1q">Sunitinib efficacy coefficient</td></tr>
<tr><td id="27-1r">dC/dt</td><td id="27-1s">α/β</td><td id="27-1t">Ratio of lymphocyte synthesis rate to turnover rate</td></tr>
<tr><td id="27-1u"></td><td id="27-1v">β</td><td id="27-1w">Rate of lymphocyte turnover</td></tr>
<tr><td id="27-1x">dM/dt</td><td id="27-1y">ん</td><td id="27-1z">Rate of excretion and elimination of doxorubicin</td></tr>
<tr><td id="27-1A">dI/dt</td><td id="27-1B">μι</td><td id="27-1C">Rate of excretion and elimination of IL-2</td></tr>
<tr><td id="27-1D"></td><td id="27-1E">W</td><td id="27-1F">Rate of IL-2 production from CD8+ T cells</td></tr>
<tr><td id="27-1G"></td><td id="27-1H">φ</td><td id="27-1I">Rate of IL-2 production from CD4+ T cells and naive CD8+ T cells</td></tr>
<tr><td id="27-1J"></td><td id="27-1K">ζ</td><td id="27-1L">Concentration of IL-2 for half-maximal CD8+ T cell IL-2 production</td></tr>
<tr><td id="27-1M">dS/dt</td><td id="27-1N">η</td><td id="27-1O">Rate of excretion and elimination of sunitinib</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='e18fc499-c59b-4121-abbe-04fd6c14b584'></a>

MATHEMATICAL MODEL: REGULATORY T CELL EFFECTS ON RCC TREATMENT 943

<a id='708233b6-378c-4611-9b7f-5e0b41113475'></a>

Table 3: Parameter Values

<a id='0316f57a-69f0-4420-8723-78e317203a82'></a>

<table id="28-1">
<tr><td id="28-2">ODE</td><td id="28-3">Param</td><td id="28-4">Value</td><td id="28-5">Units</td><td id="28-6">Source</td></tr>
<tr><td id="28-7">dT/dt</td><td id="28-8">a</td><td id="28-9">0.2065</td><td id="28-a">1/day</td><td id="28-b">Estimated (see section 4.1)</td></tr>
<tr><td id="28-c"></td><td id="28-d">b</td><td id="28-e">2.145 × 10⁻¹⁰</td><td id="28-f">Cells⁻¹</td><td id="28-g">Estimated (see section 4.1)</td></tr>
<tr><td id="28-h"></td><td id="28-i">c</td><td id="28-j">8.68 × 10⁻¹⁰</td><td id="28-k">L Cells⁻¹ Day⁻¹</td><td id="28-l">Estimated (see section 4.1)</td></tr>
<tr><td id="28-m"></td><td id="28-n">λT</td><td id="28-o">1.590 × 10⁻⁹</td><td id="28-p">L Cells⁻¹</td><td id="28-q">Estimated (see section 4.1)</td></tr>
<tr><td id="28-r"></td><td id="28-s">d</td><td id="28-t">1.7 [1.7-2.2]</td><td id="28-u">Day-1</td><td id="28-v">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-w"></td><td id="28-x">l</td><td id="28-y">1.7 [1.7-2.2]</td><td id="28-z"></td><td id="28-A">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-B"></td><td id="28-C">s</td><td id="28-D">3.5 × 10-2</td><td id="28-E">L-1</td><td id="28-F">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-G">dN/dt</td><td id="28-H">e/f</td><td id="28-I">0.1168</td><td id="28-J"></td><td id="28-K">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-L"></td><td id="28-M">f</td><td id="28-N">1.25 x 10-2</td><td id="28-O">Day</td><td id="28-P">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-Q"></td><td id="28-R">p</td><td id="28-S">6.682 × 10-14</td><td id="28-T">L Cells-1 Day-1</td><td id="28-U">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-V"></td><td id="28-W">pN</td><td id="28-X">6.68 × 10-2</td><td id="28-Y">Day-1</td><td id="28-Z">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-10"></td><td id="28-11">gN</td><td id="28-12">2.5036 × 105</td><td id="28-13">IU L-1</td><td id="28-14">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-15">dL/dt</td><td id="28-16">m</td><td id="28-17">9 × 10-3</td><td id="28-18">Day-1</td><td id="28-19">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1a"></td><td id="28-1b">q</td><td id="28-1c">3.422 × 10-10</td><td id="28-1d">Cells-1 Day-1</td><td id="28-1e">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1f"></td><td id="28-1g">r₁</td><td id="28-1h">6.682 × 10⁻¹²</td><td id="28-1i">Cells⁻¹ Day⁻¹</td><td id="28-1j">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1k"></td><td id="28-1l">r₂</td><td id="28-1m">1 × 10⁻¹⁵</td><td id="28-1n">Cells⁻¹ Day⁻¹</td><td id="28-1o">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1p"></td><td id="28-1q">pI</td><td id="28-1r">1.111</td><td id="28-1s">Day⁻¹</td><td id="28-1t">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1u"></td><td id="28-1v">gI</td><td id="28-1w">2.5036 × 10³</td><td id="28-1x">IU L⁻¹</td><td id="28-1y">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1z"></td><td id="28-1A">z</td><td id="28-1B">2.3085 × 10⁻¹³</td><td id="28-1C">L² Cells⁻² Day⁻¹</td><td id="28-1D">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1E"></td><td id="28-1F">κ</td><td id="28-1G">2.5036 × 10³</td><td id="28-1H">IU L⁻¹</td><td id="28-1I">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1J"></td><td id="28-1K">j</td><td id="28-1L">1.245 × 10⁻¹</td><td id="28-1M">Day⁻¹</td><td id="28-1N">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1O"></td><td id="28-1P">k</td><td id="28-1Q">2.019 × 10⁷</td><td id="28-1R">Cells</td><td id="28-1S">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-1T">dR/dt</td><td id="28-1U">w/u</td><td id="28-1V">1.22 × 10⁻²</td><td id="28-1W"></td><td id="28-1X">Estimated (see section 4.4)</td></tr>
<tr><td id="28-1Y"></td><td id="28-1Z">u</td><td id="28-20">3.851 × 10⁻²</td><td id="28-21">Day⁻¹</td><td id="28-22">Mabarrack et al. (2008) [48]</td></tr>
<tr><td id="28-23"></td><td id="28-24">p_R</td><td id="28-25">3.598 × 10⁻²</td><td id="28-26">Day⁻¹</td><td id="28-27">Method from de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-28"></td><td id="28-29">g_R</td><td id="28-2a">11.027</td><td id="28-2b">IU L⁻¹</td><td id="28-2c">Method from de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-2d"></td><td id="28-2e">H_R</td><td id="28-2f">0.227</td><td id="28-2g">Day⁻¹</td><td id="28-2h">Estimated (see section 4.4)</td></tr>
<tr><td id="28-2i"></td><td id="28-2j">λ_R</td><td id="28-2k">50.02</td><td id="28-2l">L mg⁻¹</td><td id="28-2m">Estimated (see section 4.4)</td></tr>
<tr><td id="28-2n">dC/dt</td><td id="28-2o">α/β</td><td id="28-2p">2.14 × 10⁹</td><td id="28-2q">cells L⁻¹</td><td id="28-2r">Abbas et al. (2007) [1]</td></tr>
<tr><td id="28-2s"></td><td id="28-2t">β</td><td id="28-2u">6.3 × 10^{-3}</td><td id="28-2v">Day^{-1}</td><td id="28-2w">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-2x">dI/dt</td><td id="28-2y">μ_I</td><td id="28-2z">11.7427</td><td id="28-2A">Day^{-1}</td><td id="28-2B">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-2C"></td><td id="28-2D">ω</td><td id="28-2E">5.314 × 10^{-2}</td><td id="28-2F">Day^{-1}</td><td id="28-2G">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-2H"></td><td id="28-2I">Φ</td><td id="28-2J">3.594 × 10^{-7}</td><td id="28-2K">IU Cells^{-1} Day^{-1}</td><td id="28-2L">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-2M"></td><td id="28-2N">ζ</td><td id="28-2O">2.5036 × 10^{3}</td><td id="28-2P">IU L^{-1}</td><td id="28-2Q">de Pillis et al. (2009) [13]</td></tr>
<tr><td id="28-2R">dS/dt</td><td id="28-2S">η</td><td id="28-2T">0.277</td><td id="28-2U">Day-1</td><td id="28-2V">Estimated (see section 4.7)</td></tr>
</table>

<a id='0cf25f11-19be-47d5-aee3-cbe93486a708'></a>

Received February 2012; revised August 2012.
E-mail address: depillis@hmc.edu;tcal42@uw.edu
E-mail address: esarapata@g.hmc.edu; hwilliams@hmc.edu
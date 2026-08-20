<a id='849ea327-1024-4391-8e6e-1c982ab6b71f'></a>

BioSystems 118 (2014) 51–59

<a id='dbd51e8a-a0fc-4b6e-9339-84f8453f63c5'></a>

<::logo: ELSEVIER
NON SOLUS
A detailed illustration of a tree with two figures beneath it, rendered in black and white, with the brand name "ELSEVIER" in orange text below.::>

<a id='e19b6504-09d4-4e9f-90ee-8f5b8f3a0c9a'></a>

Contents lists available at ScienceDirect

<a id='f5ff1a55-ba25-4771-823d-242c9b2e3579'></a>

BioSystems

<a id='c6d6bcfb-acf2-4670-8350-de9ffb23e32c'></a>

journal homepage: www.elsevier.com/locate/biosystems

<a id='9b948a4b-a91b-4d68-bb38-d1b5f005e5ce'></a>

<::logo: [Bio Systems]
Bio Systems
The logo features a stylized circular design with radiating lines, set against a dark blue background with a gradient effect.: রক্ষা करें ::>

<a id='7b5a6cbe-b742-4d81-a29e-c2592b07fdd3'></a>

Within-host influenza dynamics: A small-scale mathematical modeling approach

<a id='74a22b71-a239-47c4-8a53-9253828f7409'></a>

<::logo: CrossMark
CrossMark
A blue circular icon with a red bookmark symbol inside, accompanied by the text "CrossMark".::>

<a id='b0e73987-9c6c-45a3-b8f9-8a19bd1e6f5d'></a>

Himanshu Manchanda a, b, 1, Nora Seidelb, 1, Andi Krumbholz b, c, Andreas Sauerbreib,
Michaela Schmidtke b,*, Reinhard Guthke a, **

<a id='0d6cc003-ea09-4cb6-b933-c4d92affd01b'></a>

a Leibniz Institute for Natural Product Research and Infection Biology - Hans Knöll Institute, Jena, Germany
b Jena University Hospital, Department of Virology and Antiviral Therapy, Jena, Germany
c Institute for Infection Medicine, Christian-Albrecht University of Kiel and University Medical Center Schleswig-Holstein, Campus Kiel, Kiel, Germany

<a id='9550efda-4f38-402c-86e1-5de376c1f9a5'></a>

ARTICLE INFO

*Article history:*
Received 28 June 2013
Received in revised form 24 February 2014
Accepted 27 February 2014
Available online 11 March 2014

*Keywords:*
Influenza virus
Infection
Modeling
Virus replication
Immune response
Inflammation

<a id='f161e829-deff-45db-a328-b6017c6a1ac2'></a>

ABSTRACT

The emergence of new influenza viruses like the pandemic H1N1 influenza A virus in 2009 (A(H1N1)pdm09) with unpredictable difficulties in vaccine coverage and established antiviral treatment protocols emphasizes the need of new murine models to prove the activity of novel antiviral compounds _in vivo_. The aim of the present study was to develop a small-scale mathematical model based on easily attainable experimental data to explain differences in influenza kinetics induced by different virus strains in mice. To develop a three-dimensional ordinary differential equation model of influenza dynamics, the following variables were included: (i) viral pathogenicity (_P_), (ii) antiviral immune defense (_D_), and (iii) inflammation due to pro-inflammatory response (_I_). Influenza virus-induced symptoms (clinical score _S_) in mice provided the basis for calculations of _P_ and _I_. Both, mono- and biphasic course of mild to severe influenza induced by three clinical A(H1N1)pdm09 strains and one European swine H1N2 virus were comparatively and quantitatively studied by fitting the mathematical model to the experimental data. The model hypothesizes reasons for mild and severe influenza with mono- as well as biphasic course of disease.

<a id='82a70f5f-6e61-4b39-bd52-3223bdf1102c'></a>

According to modeling results, the second peak of the biphasic course of infection is caused by inflam-mation. The parameters (i) maximum primary pathogenicity, (ii) viral infection rate, and (iii) rate of activation of the immune system represent most important parameters that quantitatively characterize the different pattern of virus-specific influenza kinetics.

<a id='0edcfec0-9085-4af1-a26b-b1e09797def6'></a>

© 2014 Elsevier Ireland Ltd. All rights reserved.

<a id='44da0a5f-4110-44ae-9d75-9481ada38565'></a>

# 1. Introduction
In April 2009 a new pandemic H1N1 influenza A virus (A(H1N1)pdm09) emerged (Dawood et al., 2009; Ginsberg et al., 2009). It replaced seasonal H1N1 viruses and continued to circulate together with H3N2 and influenza B viruses causing millions of infections per year (WHO, 2013).

<a id='79d5a90c-262b-40c4-9d5e-a96e993fa9b4'></a>

A(H1N1)pdm09 virus is M2 ion channel blocker-resistant and neuraminidase (NA) inhibitor (NAI)-sensitive (Dawood et al., 2009; Gubareva et al., 2009). However, since its emergence several muta- tions were identified that resulted in reduced NAI susceptibility or even resistance (Nguyen et al., 2012). Moreover, A(H1N1)pdm09

<a id='b77ccbaf-795f-409f-addf-71e75d86512d'></a>

* Corresponding author.
** Corresponding author. Fax: +49 3641 532 0803.
E-mail address: reinhard.guthke@hki-jena.de (R. Guthke).
1 These authors contributed equally to this work.

<a id='3ce016f4-d9d4-4d71-8d2c-43affa5595f0'></a>

http://dx.doi.org/10.1016/j.biosystems.2014.02.004
0303-2647/© 2014 Elsevier Ireland Ltd. All rights reserved.

<a id='16f98ff6-7c2c-4f06-be33-8ff14223b6d6'></a>

virus lacks the 150-cavity that is typical of group 1 NA (Li et al., 2010) and presents a structurally new target for the development of new inhibitory compounds (Kirchmair et al., 2011). In addition, the virus has a natural resistance against the potential nucleoprotein inhibitor nucleozin (Kao et al., 2010). Thus, there is an urgent need for the development of new anti-influenza compounds.

<a id='27463101-4ad4-4eb4-8b30-54e64401efce'></a>

The efficacy of novel potential drug candidates for treatment of
mild as well as lethal A(H1N1)pdm09 infections has to be demon-
strated in vivo. Influenza can be modeled in a wide range of animals
like mice, ferrets, pigs, nonhuman primates, rats and cotton rats
(Barnard, 2009). Due to the moderate costs of the animals as well
as their caging and the comparability of the disease to human ill-
ness, mice represent a good compromise for anti-influenza studies.
During establishment of antiviral mouse models the dynamics of
infection of used virus strains has to be characterized quantita-
tively. Influenza dynamics depends on viral pathogenicity that can
be influenced for example by the efficiency of binding to host recep-
tors, induction of apoptosis, or the replication potential of the virus

<!-- PAGE BREAK -->

<a id='ffcf7515-620e-41c5-9d5d-09a4b746ec7b'></a>

52

<a id='52706a35-d17d-42d2-97d5-60181d3e756f'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51–59

<a id='f8245e94-faae-499a-985e-91111232c556'></a>

(Tscherne and Garcia-Sastre, 2011). In addition, the virus-induced host immune response can worsen the disease course. In particular, the pro-inflammatory immune response that comprise cytokine as well as chemokine release of infected cells and the attraction of leucocytes can affect negatively the dynamics of infection and con- tribute to a severe course of influenza (Arankalle et al., 2010; de Castro et al., 2010).

<a id='d7bad552-0fc4-44c5-bb82-5d997c01f643'></a>

Viral titers (Baccam et al., 2009) or measurements of at least one of the immunological components like interferons, macrophages, NK cells, B cell, T cells (Hancioglu et al., 2006; Handel et al., 2010; Miao et al., 2010; Lee et al., 2009; Pawelek et al., 2012; Saenz et al., 2010) were used as experimental data for modeling influenza kinetics in different hosts with the aim to identify factors explaining the course of illness (Canini and Carrat, 2011) and/or differences in pathogenicity of influenza strains (Wattrang et al., 2003; Smith et al., 2011). As reviewed by Smith and Perelson (2011), there are an increasing number of influenza kinetics models based on viral load data. However, these authors also express their doubts about using viral load as the only indicator of disease severity because immunopathology is discussed as an additional factor in severe infection (de Castro et al., 2010). For example, Kumar et al. (2004) have shown that a strong late immune response can increase the risk of persistent inflammation even after clearing the pathogen. Interestingly, Smith and Perelson (2011) suggest that assigning a symptom score throughout the infection could offer a new perspective into the characteristics of an infection. A symptom score is easily attainable and reflects how sick a host is.

<a id='f4271c89-83a0-4f5c-83ed-55339a89cd35'></a>

Both small-scale mathematical models (e.g., Saenz et al., 2010; Baccam et al., 2009) and complex models with more than 10 equations and more than 50 parameters (e.g., Hao et al., 2013; Hancioglu et al., 2006; Lee et al., 2009) have been proposed. However, complex models require an increased number and quality of experimental data to calibrate the model parameters. Small-scale models have the advantage to be applicable for quantitative comparison of a (also large) set of experiments (e.g., with different virus strains and/or therapeutic strategies) with a limited experimental effort.

<a id='3b375bac-3e1a-41e1-a18c-6a4773660377'></a>

The aim of the present study was to use the symptom score as an easily attainable data source and to develop a small-scale mathematical model of influenza dynamics. Virus pathogenicity, antiviral immune defense, and pro-inflammatory response resulting from viral pathogenicity as well as inflammation were considered as main model variables in a three differential equation model. In the present work, the dynamics of influenza induced by three different A(H1N1)pdm09 strains and one swine H1N2 strain in mice was modeled by a single model with 8 parameters on experimental data given by the symptoms score.

<a id='ad2e08e6-6fc5-40b9-8b4e-834eeb435cdd'></a>

## 2. 2 Materials and methods
### 2.1. Cells and viruses
Madin-Darby canine kidney (MDCK) cells (Friedrich-Loeffer
Institute, Riems, Germany) were maintained in Eagle's minimum
essential medium (EMEM) supplemented with 100 U/ml penicillin
and 100 U/ml streptomycin, 10% fetal bovine serum, and 2 mM L-
glutamine.

<a id='d753ee5b-e377-458f-b022-9c71090e21d5'></a>

The A(H1N1)pdm09 influenza virus strains A/Jena/5258/09 ('Jena/5258'), A/Jena/5555/09 ('Jena/5555') (Kirchmair et al., 2011; Durrwald et al., 2010), and A/Jena/2688/10 ('Jena/2688') were isolated in MDCK cells from respiratory specimen that originated from patients with clinical symptoms of influenza infection. The European swine H1N2 influenza virus A/swine/Bakum/1832/00 ('Bakum/1832') was obtained from a nasal swab of a diseased pig (Bauer et al., 2012; Schrader and Suss, 2003).

<a id='faf9e6ef-edaf-4dc2-acbb-98fa14e48b0a'></a>

Virus titers were determined by titration of 10-fold serial dilutions on confluent MDCK cells. The 50% tissue culture infectious dose (TCID50) was calculated according to Reed and Muench (1938). For isolation, titration and propagation of viruses EMEM formulated with 100 U/ml penicillin and streptomycin, 2 µg/ml trypsin, and 0.1% sodium bicarbonate was used (test medium).

<a id='840c5048-6394-4748-8d00-69e763cf3069'></a>

## 2.2. Animal experiments and data

Experiments were performed in female BALB/c mice (16–18 g; Charles River, Bad Sulzfeld, Germany). After isoflurane anesthesia, five mice were inoculated intranasally with 10⁶ TCID₅₀/20 µl of each virus in EMEM. Three mice were mock-infected for control. Body weight and clinical score were used as study parameters and monitored for 21 days after virus challenge. Mice that lost more than 25% of their initial body weight were sacrificed. A laboratory clinical score was used to assess the severity of disease. It ranged from 0 to 7: 0 – no changes, 1 – scrubby coat in the neck, 2 – scrubby coat in the neck and on the back, 3 – scrubby coat on whole body, incipient hunchbacked posture, 4 – scrubby coat, hunchbacked posture, incipient inactivity, eyes half closed, 5 – scrubby coat, hunchbacked posture, inactivity, eyes closed, 6 – scrubby coat, hunchbacked posture, completely inactive, eyes closed, 7 – mouse deceased. The mean values and standard deviation (_Std_) for the clinical score (_S_) as well as the percentage of body weight changes in comparison to day 0 were calculated.

<a id='39903310-fb1b-4109-a818-8b0538c9ae32'></a>

### 3. Theory and calculations

#### 3.1. *Model*

The mathematical model representing the within-host influenza dynamics consists of a system of three differential equations in which the dependent variables represent the virus pathogenicity (*P*), antiviral immune defense (*D*) including both the innate immune response and the adaptive immune response, and inflammation due to pro-inflammatory response (*I*). The mathematical equations of our reduced model are:

<a id='d45bc4cc-c45f-4652-bcd3-9f5ee0245792'></a>

dP/dt = α * P * (1 - P/k_p) - β * D * P / (P + 0.01) (1)
dD/dt = γ * P - θ * D (2)
dI/dt = ε * f(D) - ρ * I (3)
f(D) = 1 + tanh((D - δ) / ω) (4)
S = P + I (5)

<a id='74c503e2-3ecf-46d0-890d-3b4bedf6d4ed'></a>

The virus pathogenicity _P_ represents the virulence of the virus strains. The dynamics of change of _P_ is described by Eq. (1). It depends on viral infection and the immune response of the host. The first term is parameterized by the virus infection rate (parameterized by α) and the maximum primary pathogenicity (parameterized by _kP_). The second term of Eq. (1) represents the efficiency of the early immune response to the virus (parameterized by β). For very small values of _P_ this second term goes to zero due to the Michaelis-Menten function parameterized by a small and fixed Michaelis-Menten constant 0.01 (smaller values or other functions that go to zero if _P_ becomes zero do not change the model behavior) to avoid that _P_ becomes negative.

<a id='9743a6ac-fb03-4285-9fb0-7bb61f9b5377'></a>

The antiviral defense is modeled by the variable D including both
the innate immune response and the adaptive immune response.
Although the defense system is very complex, in the small-scale
model the change of the defense system is modeled in Eq. (2) by only

<!-- PAGE BREAK -->

<a id='70409fb3-9f96-498e-976b-d8eebcaf6689'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51–59

<a id='c7a6c51d-95cb-4ad1-a713-fa11c6ee8730'></a>

53

<a id='eefa9c71-014b-4e6b-a751-dc157e2275d8'></a>

<::flowchart: The diagram illustrates a model structure with four interconnected variables: a red circle labeled "P" representing "Virus Pathogenicity"; a blue circle labeled "D" representing "Antiviral Immune Defense"; a green circle labeled "I" representing "Inflammation"; and a gradient circle (orange to green) labeled "S" representing "Clinical Score, measure of clinical symptoms". Relationships between variables are indicated by arrows: a self-loop from P to P is labeled "α Infection rate"; an arrow from P to D is labeled "γ Immune activation"; an arrow from D to P has a minus sign and is labeled "β Efficiency of immune response"; an arrow from D to I is labeled "ε Pro-inflammatory cytokines and adverse adaptive immune response"; an unlabeled arrow connects P to I; an unlabeled arrow connects I to S; an unlabeled arrow connects P to S. Additionally, an outgoing arrow from D, not connecting to another node, is labeled "θ Immunity decay"; and an outgoing arrow from I, not connecting to another node, is labeled "ρ Inflammation decay or anti-inflammatory response". Fig. 1. Model structure. The model variables P (pathogen), D (defense), I (inflammation), and S (clinical score) as well as the relations between them according to Eqs. (1)–(5). ::>

<a id='2ab02c7f-f36f-40b2-839b-7bdc21989165'></a>

two terms. The first term represents the activation of the defense systems in response to the pathogen (parameterized by γ) and the second term represents the immunity decay (parameterized by θ), which means that once the pathogen has been cleared off from the host system, the defense system should come to rest. Both terms are modeled by first-order reactions.

<a id='f7b608f6-4632-46da-ae85-427113f28d3b'></a>

The third model variable *I* represents the inflammation due to pro-inflammatory response. Its change is described by Eq. (3).
This model formulation is derived from Kumar et al. (2004) and describes a combined effect of cytokines and chemokines, and stimulatory effects of tissue damaged and dysfunction. The first term according to Kumar et al. is a hyperbolic function of antiviral defense system of the host *D* which strength is parameterized by ε. The parameter δ in Eq. (4) represents the triggering threshold value for the chronic inflammation along with the parameter ω, which represents the strength of prolongation of the inflammation. The ratio δ/ω represents the intensity of the inflammation which can explain whether the virus triggers the chronic inflammation or the acute one. The second term in Eq. (4) represents the relaxation of the inflammation (parameterized by ρ) which could be the anti-inflammatory response by the host. This part of inflammation (denoted by *I*) does not help in removing the pathogen but leads to collateral damage to the neighboring tissue (Goris et al., 1985; Takala et al., 1999) contributing to the influenza virus-induced symptoms (clinical score *S*) as modeled by Eq. (5). Fig. 1 displays the model structure and Table 1 lists the model parameters.

<a id='a5be79d1-8d0c-4d90-8432-4159ed874492'></a>

3.2. Model simulation and parameter estimation

The model formulated by the Eqs. (1)-(5) is numerically solved using the R-package deSolve from Soetaert et al. (2010). The LSODA method of integration (Petzold, 1983) was employed using a step size of 0.01. The R-package FME from Soetaert et al. (2010) was used for the estimation of parameter values and their impact (sensitivity) on the model output S. The Levenberg-Marquardt algorithm (Moré, 1978) has been used to fit the model variable S to the respective data (observed clinical score) as implemented in the modFit function of the package FME. The modCost function from the package has been used in the fitting procedure and is the sum of the variable costs, which are scaled according to the number of observations. The variables cost itself is calculated as the sum of squared weighted residuals, where the standard deviation Std of the mean of the observed clinical score S is used as weight.

<a id='e31149d6-f355-49c1-b11d-fc5cea0cfe43'></a>

Table 1
Description of model variables and parameters.
<table id="2-1">
<tr><td id="2-2">Model variables</td><td id="2-3"></td></tr>
<tr><td id="2-4">t</td><td id="2-5">Time (d)</td></tr>
<tr><td id="2-6">P</td><td id="2-7">Virus pathogenicity</td></tr>
<tr><td id="2-8">D</td><td id="2-9">Antiviral immune defense</td></tr>
<tr><td id="2-a">I</td><td id="2-b">Inflammation due to pro-inflammatory response</td></tr>
<tr><td id="2-c">S (letter S)</td><td id="2-d">Clinical score; measure of clinical symptoms</td></tr>
</table>
<table id="2-e">
<tr><td id="2-f" colspan="2">Model parameters</td><td id="2-g">Value</td></tr>
<tr><td id="2-h">α</td><td id="2-i">Viral infection rate</td><td id="2-j">Estimated (d⁻¹)</td></tr>
<tr><td id="2-k">kP</td><td id="2-l">Maximum primary pathogenicity</td><td id="2-m">Estimated</td></tr>
<tr><td id="2-n">β&#x27;</td><td id="2-o">Efficiency of immune response</td><td id="2-p">Fixed: 1 d⁻¹ Eliminated, see text</td></tr>
<tr><td id="2-q">γ</td><td id="2-r">Rate of activation of the immune system</td><td id="2-s">Estimated (d⁻¹)</td></tr>
<tr><td id="2-t">θ</td><td id="2-u">Convalescence rate of immune system; immune decay</td><td id="2-v">Fixed: 0.01 d⁻¹ See text</td></tr>
<tr><td id="2-w">ε</td><td id="2-x">Rate at which inflammation gets activated</td><td id="2-y">Estimated (d⁻¹)</td></tr>
<tr><td id="2-z">δ</td><td id="2-A">Triggering threshold value of the defense for inflammation</td><td id="2-B">Estimated for biphasic course only</td></tr>
<tr><td id="2-C">ω</td><td id="2-D">Tolerance value of the defense for the chronic inflammation</td><td id="2-E">Estimated for biphasic course only</td></tr>
<tr><td id="2-F">ρ</td><td id="2-G">Relaxation rate of inflammation/Anti-inflammatory response</td><td id="2-H">Fixed: 1.82 d⁻¹, Canini and Carrat, 2011</td></tr>
<tr><td id="2-I">P(0)</td><td id="2-J">Virus pathogenicity, initial value</td><td id="2-K">Fixed: 0.01 Baccam et al. (2009)</td></tr>
<tr><td id="2-L">D(0)</td><td id="2-M">Antiviral immune defense, initial value</td><td id="2-N">Fixed: 0.00</td></tr>
<tr><td id="2-O">I(0)</td><td id="2-P">Inflammation due to pro-inflammatory response, initial value</td><td id="2-Q">Fixed: 0.00</td></tr>
</table>

<a id='c633862c-8d7d-4561-a3ae-38812037979f'></a>

Finally, a Markov Chain Monte Carlo (MCMC; implemented in the package FME; Soetaert and Petzoldt, 2010) simulation was used to estimate the uncertainty of the parameter estimates as resulted by the model fit. The first 500 iterations were removed which is known as burn-in so as to make sure the chain was close enough to target distribution. The parameters sets that gave the highest probability to fit the model have been chosen as the final parameter sets for the model fitting. All the parameter values and variables are positive.

<a id='70a9d5e5-962c-42cf-82e7-cef9c85121ba'></a>

3.3. Parameter sensitivity analysis

The sensitivity and identifiability analysis were done by the functions *sensFun* and *collin* outlined in the R-package FME. Briefly, this is done by estimating at each data point the derivative of the clinical score *S* with respect to the parameter values *p_j*. The sensitivities are dimensionless, as they are scaled with respect to the variables and parameter values:

$\Sigma_i = \frac{p_j}{S} \frac{\partial S}{\partial p_j}$ (6)

<a id='207c7e92-1785-45cc-8245-bdb9ae06163e'></a>

These sensitivities allow to determine which parameter is least important to the model output and these least sensitive parameters can be fixed and not used for calibration.

<a id='e809fcbe-836d-41f3-a90f-3338d46d59a8'></a>

3.4. Parameter identifiability analysis

<a id='0ec850da-f25e-42d2-8fe2-67dca39a05e4'></a>

Raue et al. (2009) distinguished between structural and practical
identifiability. A structural identifiability analysis gives insight into
which parameters can be simultaneously estimated, given noise-
free data and a model that can fit the data perfectly. A structural
non-identifiability is caused by redundant parameterization. Here,
the structural identifiability was evaluated by investigating the

<!-- PAGE BREAK -->

<a id='adefeaa2-4a03-4cf6-be91-9276a1d49687'></a>

54

<a id='35b2909d-9a4c-47b5-b178-b1286075ce51'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51-59

<a id='89094d30-084c-45ca-8964-c61a21483d33'></a>

Table 2
Model parameter values. Parameter values and their 95% confidence intervals (in brackets) identified by model fit to the observed clinical scores. The parameter values NaN
denote that they could not be identified. Units of the parameters are displayed in Table 1.

<a id='69f8b4d0-08db-4012-ab1c-51b521d4554c'></a>

<table id="3-1">
<tr><td id="3-2">Strain/parameter</td><td id="3-3" colspan="4">Infection experiments</td></tr>
<tr><td id="3-4"></td><td id="3-5">Jena/5258 (A(H1N1)pdm09)</td><td id="3-6">Jena/5555 (A(H1N1)pdm09)</td><td id="3-7">Jena/2688 (A(H1N1)pdm09)</td><td id="3-8">Bakum/1832 (swine H1N2)</td></tr>
<tr><td id="3-9">α</td><td id="3-a">3.63 [3.62, 5.78]</td><td id="3-b">3.64 [3.31, 4.16]</td><td id="3-c">2.12 [2.03, 2.29]</td><td id="3-d">2.22 [2.09, 2.40]</td></tr>
<tr><td id="3-e">kp</td><td id="3-f">3.23 [2.31, 3.29]</td><td id="3-g">5.69 [5.13, 6.17]</td><td id="3-h">3.72 [3.02, 4.54]</td><td id="3-i">4.85 [4.27, 5.36]</td></tr>
<tr><td id="3-j">γ</td><td id="3-k">0.51 (0.25, 0.64]</td><td id="3-l">0.28 [0.27, 0.31]</td><td id="3-m">0.52 [0.44, 0.65]</td><td id="3-n">0.29 [0.24, 0.32]</td></tr>
<tr><td id="3-o">θ</td><td id="3-p">0.01</td><td id="3-q">0.01</td><td id="3-r">0.01</td><td id="3-s">0.01</td></tr>
<tr><td id="3-t">ε</td><td id="3-u">6.81</td><td id="3-v">0</td><td id="3-w">0</td><td id="3-x">0</td></tr>
<tr><td id="3-y">δ</td><td id="3-z">4.27</td><td id="3-A">NaN</td><td id="3-B">NaN</td><td id="3-C">NaN</td></tr>
<tr><td id="3-D">ω&#x27;</td><td id="3-E">0.13</td><td id="3-F">NaN</td><td id="3-G">NaN</td><td id="3-H">NaN</td></tr>
<tr><td id="3-I">ρ</td><td id="3-J">1.82</td><td id="3-K">1.82</td><td id="3-L">1.82</td><td id="3-M">1.82</td></tr>
</table>

<a id='bb959514-7c69-4ee7-95ef-1ed65c859a68'></a>

pairwise linear dependence or collinearity of all possible param-
eters sets. If the 'collinearity index' calculated by the function collin
exceeds a critical values typically chosen to be 10–15, then the
parameter set is regarded as poorly identifiable (Brun et al., 2001).

<a id='f615d4e5-cab8-4254-86f3-20d8d7cc42a1'></a>

In practice, all measurements have error and the model is non-perfect and this causes the uncertainty of the parameters values characterized by confidence regions. The practical non-identifiability is characterized by an infinitely extended confidence region in increasing and/or decreasing direction. For the estimation of confidence intervals the data-dependent probability distribution of the parameters have to be derived. Raue et al. introduced the pro-file likelihood to estimate the confidence intervals. In the present work, a Bayesian method, in particular the Markov Chain Monte Carlo approach using the DRAM method (Delayed Rejection Adap-tive Metropolis) (Haario et al., 2006) as implemented in FME was applied to visualize the confidence regions by pairwise scatter plots and to estimate the confidence intervals.

<a id='6ba829a4-449d-4a93-91b7-4c035c4eca95'></a>

## 4. Results
The parameter β was eliminated by the following model transformation: β' = 1 d⁻¹, D' = D * β, γ' = β * γ, δ' = δ * β, ω' = ω * β. In the following text, the transformed parameters are used for better readability without the prime. Then, the mathematical model includes 8 parameters, four of them (α, γ, kp, ε) were virus strain specific and therefore calibrated individually by fitting to the data of the experiments with different virus strains. The two parameters δ and ω are only relevant for biphasic course of infection and, thus, estimated only for the virus Jena/5258. The remaining two parameters ρ and θ are host-related and, therefore, fixed, i.e., identical for the four virus strains. For the inflammation decay ρ we use the value 1.82 d⁻¹ published by Canini and Carrat (2011). The fixed parameter θ were calculated by model fit to all the data sets providing a rich data set of 72 data points from four different virus strains. The values of the fixed parameters are shown in Table 1.

<a id='7cc71187-34eb-4aa9-8dfe-6015522d2077'></a>

Fig. 2 displays the results of model fit to four experimental viral infections with four different virus strains. Table 2 depicts the identified values of the 8 model parameters (i.e., all but the eliminated parameter \u03b2) together with their 95% confidence intervals.

<a id='2d60744a-9072-4b06-9b47-58ae7c720a6c'></a>

The mean sensitivity values (averaged over time) of the model parameters calculated by Eq. (6) for the four virus strains are shown in Table 3. As displayed in Table 3, we used different time intervals for averaging to exclude periods with values of S close to zero as S is in the denominator in Eq. (6). The temporal profiles of the sensitivity are depicted in the Supplementary Fig. S4.

<a id='1e169864-03dd-47e0-b06c-967622d27056'></a>

For Jena/5258, the threshold parameter δ is the most sensitive model parameter. Here, the immune defense (D) exceeds the threshold parameter δ and triggers the onset of inflammation due to the fact that three parameters are high: (i) α, i.e., the viral replication and infection rate, (ii) γ, i.e. the rate of early activation of the immune system, and (iii) the parameter ε, i.e., the rate at which inflammation gets activated. For Jena/5258, the

<a id='0244a16a-5d48-49d2-8295-27457f32145f'></a>

parameter k_p called maximum primary pathogenicity is the second most sensitive parameter after the threshold parameter δ. The infection with this strain is characterized by the highest clinical score value that is caused not by a high primary pathogenicity k_p but by the inflammation ('secondary pathogenicity'). This parameter k_p has the smallest value of 3.23 for Jena/5258 and the highest value of 5.69 for Jena/5555. The confidence intervals (CI) of k_p for these two virus strains with high temporal maximum clinical score are disjunctive, i.e., without overlap. Thus, the causes of high clinical score in both infection courses are different: Jena/5555 causes the high clinical score by a high primary pathogenicity, while Jena/5258 by high inflammation.

<a id='a4a7247e-761a-4d24-9ef0-4e1d23430dbc'></a>

The parameter Α called viral infection rate is the next most sensi-
tive parameter for Jena/5258 with biphasic course of infection, but
the most sensitive parameter for the other three virus strains with
monophasic profile (Table 3). It has the highest identified values for
the H1N1 strains Jena/5258 and Jena/5555 that are characterized
by the utmost clinical score. The CI of Α for these two virus strains
are disjunctive to the respective intervals of the other two virus
strains Jena/2688 and Bakum/1832.

<a id='91cb5476-9085-4f94-b213-06f36d1d48be'></a>

For all four virus strains, the parameter γ, which quantifies the rate of activation of the immune system, is the third (fourth for Jena/5258) most sensitive parameter – after k<sub>p</sub> and α (and after δ that is only relevant for the strain Jena/5258). Parameter γ has the highest value of 0.52 for Jena/2688 where the corresponding CI is disjunctive to the respective intervals of the strains Jena/5555 and Bakum/1832 with estimated parameter values smaller than 0.3.

<a id='c1e98bcb-1fcd-42e7-99a9-d272adcac867'></a>

In Table 2, the confidence intervals are only shown for the parameters α, γ and k<sub>p</sub>. The distribution and the pairwise scatter plot of the MCMC-generated parameter values shown in Figs. 3 and 4 give a hint to the practical identifiability of these three most important model parameters.

<a id='3a3dce6e-2d38-4a0e-8a11-a6a9d739531f'></a>

The parameters ε, i.e., the rate at which inflammation gets acti-
vated, as well as ω and δ were only identified for Jena/5258 that
exhibits a biphasic course of infection. For the other three strains
the kinetics of inflammation is non-observable based on the mea-
sured clinical score S and the model Eqs. (1)-(5). Therefore, the

<a id='93be7d5d-0ce8-4c7a-b2ad-7688be7f341f'></a>

Table 3
Sensitivities of the model parameters. Mean value (averaged over time) of the sen-
sitivity with respect to the read out value S.
<table id="3-N">
<tr><td id="3-O">Strain/Parameter</td><td id="3-P" colspan="4">Infection experiments</td></tr>
<tr><td id="3-Q"></td><td id="3-R">Jena/5258</td><td id="3-S">Jena/5555</td><td id="3-T">Jena/2688</td><td id="3-U">Bakum/1832</td></tr>
<tr><td id="3-V">Time interval (d)</td><td id="3-W">[0,10]</td><td id="3-X">[0,5]</td><td id="3-Y">[0,5]</td><td id="3-Z">[0,5]</td></tr>
<tr><td id="3-10">α</td><td id="3-11">2.88</td><td id="3-12">0.99</td><td id="3-13">1.78</td><td id="3-14">1.67</td></tr>
<tr><td id="3-15">kρ</td><td id="3-16">4.57</td><td id="3-17">0.39</td><td id="3-18">0.46</td><td id="3-19">0.46</td></tr>
<tr><td id="3-1a">γ&#x27;</td><td id="3-1b">0.96</td><td id="3-1c">-0.12</td><td id="3-1d">-0.34</td><td id="3-1e">-0.16</td></tr>
<tr><td id="3-1f">θ</td><td id="3-1g">0.38</td><td id="3-1h">0.00</td><td id="3-1i">0.01</td><td id="3-1j">0.01</td></tr>
<tr><td id="3-1k">ε</td><td id="3-1l">0.20</td><td id="3-1m">0</td><td id="3-1n">0</td><td id="3-1o">0</td></tr>
<tr><td id="3-1p">δ&#x27;</td><td id="3-1q">-8.03</td><td id="3-1r">0</td><td id="3-1s">0</td><td id="3-1t">0</td></tr>
<tr><td id="3-1u">ω&#x27;</td><td id="3-1v">0.00</td><td id="3-1w">0</td><td id="3-1x">0</td><td id="3-1y">0</td></tr>
<tr><td id="3-1z">p (greek letter)</td><td id="3-1A">-0.46</td><td id="3-1B">0</td><td id="3-1C">0</td><td id="3-1D">0</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='ba0c3ca5-c7bb-48b5-a933-b21126e63664'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51-59

<a id='ccadac7e-33dd-401c-a876-3ee1dd99dabf'></a>

55

<a id='f192d4e2-d027-44fc-b517-97b47c27bab8'></a>

<::chart::>Fig. 2. Model fit to the clinical score after infection with four different virus strains. All infected with 10⁶ TCID₅₀/mice. (For interpretation of the references to color in text, the reader is referred to the web version of this article.)

**Top Row: A(H1N1)pdm09 Jena/5258**

**Left Plot: Clinical Score vs. Days after infection**
*   **Y-axis:** Clinical score (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Data:** Black circles with error bars ('Std') representing observed and averaged clinical score S.
*   **Model Fit:** Red solid line representing model kinetics S.
*   **Legend:** fitting (red line), data (black circle).
*   **Description:** The clinical score shows a peak around day 6-7, then declines. The red line (model fit) closely tracks the black circles (observed data).

**Right Plot: All Variables vs. Days after infection**
*   **Y-axis:** All Variables (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Legend:** P (blue dashed line), D (black dashed line), I (green dotted line), S (red dashed line).
*   **Description:** This plot shows the kinetics of four model variables over time. Variable P (blue dashed line) peaks early, followed by S (red dashed line) and D (black dashed line). Variable I (green dotted line) remains low throughout.

**Second Row: A(H1N1)pdm09 Jena/5555**

**Left Plot: Clinical Score vs. Days after infection**
*   **Y-axis:** Clinical score (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Data:** Black circles with error bars ('Std') representing observed and averaged clinical score S.
*   **Model Fit:** Red solid line representing model kinetics S.
*   **Legend:** fitting (red line), data (black circle).
*   **Description:** Similar to the top row, the clinical score peaks around day 6-7 and then decreases, with the model fit closely matching the observed data.

**Right Plot: All Variables vs. Days after infection**
*   **Y-axis:** All Variables (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Legend:** P (blue dashed line), D (black dashed line), I (green dotted line), S (red dashed line).
*   **Description:** Variable P (blue dashed line) peaks early and declines, while S (red dashed line) peaks later. Variable D (black dashed line) rises and plateaus. Variable I (green dotted line) remains low.

**Third Row: A(H1N1)pdm09 Jena/2688**

**Left Plot: Clinical Score vs. Days after infection**
*   **Y-axis:** Clinical score (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Data:** Black circles with error bars ('Std') representing observed and averaged clinical score S.
*   **Model Fit:** Red solid line representing model kinetics S.
*   **Legend:** fitting (red line), data (black circle).
*   **Description:** The clinical score peaks around day 6-7 and then declines, with the model fit closely matching the observed data.

**Right Plot: All Variables vs. Days after infection**
*   **Y-axis:** All Variables (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Legend:** P (blue dashed line), D (black dashed line), I (green dotted line), S (red dashed line).
*   **Description:** Variable P (blue dashed line) peaks early and declines, S (red dashed line) peaks later. Variable D (black dashed line) rises and plateaus. Variable I (green dotted line) remains low.

**Bottom Row: European swine H1N2 Bakum/1832**

**Left Plot: Clinical Score vs. Days after infection**
*   **Y-axis:** Clinical score (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Data:** Black circles with error bars ('Std') representing observed and averaged clinical score S.
*   **Model Fit:** Red solid line representing model kinetics S.
*   **Legend:** fitting (red line), data (black circle).
*   **Description:** The clinical score peaks around day 6-7 and then declines, with the model fit closely matching the observed data.

**Right Plot: All Variables vs. Days after infection**
*   **Y-axis:** All Variables (ranging from 0 to 7)
*   **X-axis:** Days after infection (ranging from 0 to 20)
*   **Legend:** P (blue dashed line), D (black dashed line), I (green dotted line), S (red dashed line).
*   **Description:** Variable P (blue dashed line) peaks early and declines, S (red dashed line) peaks later. Variable D (black dashed line) rises and plateaus. Variable I (green dotted line) remains low.

**Overall:** Each row displays a pair of plots for a specific virus strain. The left plot compares observed clinical scores with model kinetics S, showing a good fit. The right plot illustrates the dynamics of four model variables (P, D, I, S) over time.::>

<a id='799dcfdb-bd76-43d8-a87f-2212a5bddc00'></a>

parameter ε was set to zero and the parameter values ω and δ were
denoted in Table 2 as unknown for the infection experiments using
the virus strains Jena/5555, Jena/2688, and Bakum/1832.

<a id='a172dd86-d8ba-4912-9442-bedabd4d94c2'></a>

The model parameters *k<sub>p</sub>*, *\alpha*, and *\gamma* were found to be the most discriminative and identifiable parameters that quantitatively characterize the four virus strains under investigated in this study. Each of the four virus strains is characterized by a specific pattern with respect to these three parameters as displayed in Table 4.

<a id='56de1f2f-2cb9-4501-8946-bd9cdf7872a4'></a>

Table 4
Virus-specific pattern with respect to three model parameters. Labels 'low' versus
'high' represent disjunctive confidence intervals of the respective parameter values.
<table id="4-1">
<tr><td id="4-2">Strain/parameter</td><td id="4-3" colspan="2">Infection experiments</td><td id="4-4"></td><td id="4-5"></td></tr>
<tr><td id="4-6"></td><td id="4-7">Jena/5258</td><td id="4-8">Jena/5555</td><td id="4-9">Jena/2688</td><td id="4-a">Bakum/1832</td></tr>
<tr><td id="4-b">kP</td><td id="4-c">Low</td><td id="4-d">High</td><td id="4-e">(Medium)</td><td id="4-f">(Medium)</td></tr>
<tr><td id="4-g">α</td><td id="4-h">High</td><td id="4-i">High</td><td id="4-j">Low</td><td id="4-k">Low</td></tr>
<tr><td id="4-l">γ</td><td id="4-m">(Medium)</td><td id="4-n">Low</td><td id="4-o">High</td><td id="4-p">Low</td></tr>
</table>

<a id='0a326385-1129-4678-b55e-782dba04416a'></a>

To evaluate the structural identifiability of the non-fixed param-eters, the collinearity index (also known as condition number) was estimated using the function _collin_ of the R-package FME. The collinearity indices for all combinations of the 8 model parameters α, kρ, γ, θ, ε, δ, ω, and ρ are high (Supplementary Fig. S1) and, thus, demonstrate the structural non-identifiability of the whole param-eter set. The collinearity indices for the combinations of the three most important model parameters α, kρ, and γ are shown in the Supplementary Fig. S2. These values are below 5. As a rule of thumb, a collinearity index less than 10–15 estimated by the function _collin_ of the R-package FME is assumed to be structural identifiable (Brun et al., 2001). Figs. 3, 4 and S3 show the scatter-plot matrices visual-izing the model parameter values from MCMC-generated samples, the probability distribution of the model parameters values and their pair-wise correlation coefficients as calculated by the function _pairs_ of the package FME. For all four experiments the distributions of the parameters α, kρ, and γ tend to zero for both increas-ing as well as decreasing values and the correlation between the

<!-- PAGE BREAK -->

<a id='0c0c3880-ee96-4473-8cd7-4da330c07331'></a>

56

<a id='07a63291-f13d-445a-842f-98ebebc4f0a2'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51-59

<a id='f880c0bc-11f5-428e-951a-348edaa4e52a'></a>

<::Figure: Scatter-plot matrix of Markov Chain Monte Carlo (MCMC) samples for the virus strain Jena/5258.

**Structure:** 5x5 grid displaying relationships between parameters α, γ, δ, ω, and kp.

**Diagonal Panels (Histograms):**
- **alpha:** Histogram with x-axis ranging from approximately 0.3 to 0.9.
- **gamma:** Histogram with x-axis ranging from approximately 0.0 to 0.4.
- **delta:** Histogram with x-axis ranging from approximately 4 to 10.
- **omega:** Histogram with x-axis ranging from approximately 2.5 to 4.5.
- **kp:** Histogram with x-axis ranging from approximately 0.0 to 0.4.

**Upper Triangular Panels (Pair-wise Scatter Plots):**
- **alpha vs. gamma:** Scatter plot showing a strong positive correlation.
- **alpha vs. delta:** Scatter plot showing a weak positive correlation.
- **alpha vs. omega:** Scatter plot showing a weak negative correlation.
- **alpha vs. kp:** Scatter plot showing a weak negative correlation.
- **gamma vs. delta:** Scatter plot showing a weak positive correlation.
- **gamma vs. omega:** Scatter plot showing a weak negative correlation.
- **gamma vs. kp:** Scatter plot showing a weak negative correlation.
- **delta vs. omega:** Scatter plot showing a weak negative correlation.
- **delta vs. kp:** Scatter plot showing a very weak positive correlation.
- **omega vs. kp:** Scatter plot showing a very weak negative correlation.

**Lower Triangular Panels (Correlation Coefficients):**
- **gamma-alpha:** 0.85
- **delta-alpha:** 0.22
- **delta-gamma:** 0.22
- **omega-alpha:** -0.12
- **omega-gamma:** -0.13
- **omega-delta:** -0.37
- **kp-alpha:** -0.34
- **kp-gamma:** -0.12
- **kp-delta:** 0.034
- **kp-omega:** -0.024

**Outer Axes Ranges:**
- **Top x-axis:** 0.3, 0.5, 0.7, 0.9 (for alpha); 0.0, 0.1, 0.2, 0.3, 0.4 (for gamma); 4, 5, 6, 7, 8, 9, 10 (for delta); 2.5, 3.0, 3.5, 4.0, 4.5 (for omega); 0.0, 0.1, 0.2, 0.3, 0.4 (for kp).
- **Right y-axis:** 2, 3, 4, 5 (for alpha); 4, 5, 6, 7, 8, 9, 10 (for gamma); 2.5, 3.0, 3.5, 4.0, 4.5 (for delta); 0.0, 0.1, 0.2, 0.3, 0.4 (for omega); 0.0, 0.1, 0.2, 0.3, 0.4 (for kp).

Fig. 3. Scatter-plot of the Markov Chain Monte Carlo (MCMC) samples for the virus strain Jena/5258. The top right panels show the pair-wise plot of the parameters α, γ, δ, ω, and kp. For the total parameter set see Supplementary Fig. S3. The range of the parameters is shown at the outer axis; 1000 random parameter sets around the parameter set calibrated for Jena/5258. The probability distribution for each parameter is shown in the diagonal panels. The bottom panels give the correlation coefficients for each parameter pair.::>

<a id='fdf604cd-18f1-4f90-b20a-ea657ec75f04'></a>

parameter values is low, i.e., the highest absolute value of correla-
tion coefficients is 0.86. That indicates, that the confidence regions
are finite and these three parameters are obviously practically iden-
tifiable based on the measured data of all the four experiments
studied. The remaining parameters are non-identifiable at all and,
therefore, they were fixed in our study. The parameters ε, δ, and ω
were estimated as displayed in Table 2 for the infection with virus
strain Jena/5258 that shows biphasic course. The distributions of
these parameters do not show finite borders in both Figs. 3 and S3.
For the other three virus strains with a monophasic course, the
parameter ε were set to zero and the values of the parameters δ and
ω are irrelevant as inflammation does not cause a separate peak in
the profile of the clinical score S and, therefore, it is non-observable
based on these easily attainable experimental data.

<a id='a0473e5e-93e1-4c02-9ffc-90d8dd9ac4a4'></a>

The parameter ε quantifies the degree of damage caused by the adverse effect of inflammation with respect to individual virus strains. The high values of the three parameters α, γ and ε could explain the biphasic course of clinical symptoms after infection with the virus strain Jena/5258 by stronger inflammation reaction.

<a id='9f294ec6-c03e-4d5b-b47f-16714c511eb3'></a>

Fig. 5 visualizes that the body weight is negatively correlated to the clinical score S as shown in Fig. 2. This observation supports the assumption implemented in the model Eqs. (1)-(5) that the second peak of S for Jena/5258 is caused by inflammation processes (represented by the model variable I) which is responsible for damage and the loss of body weight of the infected mice.

<a id='85cf7d01-d074-4949-a47e-9ec23f568157'></a>

## 5. Discussion

The main focus of this study was to quantify the kinetics of influenza caused by different viral strains based on a single model by only few most important parameters. With this aim, a dynamic model of influenza in mice was established and fitted to experimental data representing virus-induced clinical symptoms. Three non-fixed model parameters were proven to be identifiable and to be suitable to quantitatively characterize the four different virus strains under study: (i) the viral replication and infection rate (a), (ii) the maximum primary pathogenicity ($k_p$), and (iii) the rate of early activation of the immune system ($\gamma$). However, the

<!-- PAGE BREAK -->

<a id='8722547c-59da-4701-8df7-19fa034d99da'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51-59

<a id='96ead7a7-4dd6-4d5c-9f75-2ce30a95f534'></a>

57

<a id='58d52ace-ea5d-42c5-8f3c-24facc42de57'></a>

a
<::scatter-plot matrix: Panel a, representing virus strain Jena/5555. The matrix shows pairwise relationships between 'alpha', 'gamma', and 'kp'.
- Top row:
  - Histogram for 'alpha' (x-axis: 3.0-5.5, y-axis: 0-0.35).
  - Scatter plot of 'alpha' vs 'gamma' (x-axis: 0.25-0.35, y-axis: 3.0-5.5).
  - Scatter plot of 'alpha' vs 'kp' (x-axis: 4.5-7.0, y-axis: 3.0-5.5).
- Middle row:
  - Correlation coefficient: 0.55.
  - Histogram for 'gamma' (x-axis: 0.25-0.35, y-axis: 0-0.35).
  - Scatter plot of 'gamma' vs 'kp' (x-axis: 4.5-7.0, y-axis: 0.25-0.35).
- Bottom row:
  - Correlation coefficient: -0.26.
  - Correlation coefficient: 0.12.
  - Histogram for 'kp' (x-axis: 4.5-7.0, y-axis: 0-0.35).::>
c
<::scatter-plot matrix: Panel c, representing virus strain Jena/2688. The matrix shows pairwise relationships between 'alpha', 'gamma', and 'kp'.
- Top row:
  - Histogram for 'alpha' (x-axis: 2.0-2.8, y-axis: 0-0.35).
  - Scatter plot of 'alpha' vs 'gamma' (x-axis: 0.25-0.35, y-axis: 2.0-2.8).
  - Scatter plot of 'alpha' vs 'kp' (x-axis: 4.0-6.0, y-axis: 2.0-2.8).
- Middle row:
  - Correlation coefficient: -0.36.
  - Histogram for 'gamma' (x-axis: 0.25-0.35, y-axis: 0-0.35).
  - Scatter plot of 'gamma' vs 'kp' (x-axis: 4.0-6.0, y-axis: 0.25-0.35).
- Bottom row:
  - Correlation coefficient: -0.42.
  - Correlation coefficient: 0.76.
  - Histogram for 'kp' (x-axis: 4.0-6.0, y-axis: 0-0.35).::>
b
<::scatter-plot matrix: Panel b, representing virus strain Bakum/1832. The matrix shows pairwise relationships between 'alpha', 'gamma', and 'kp'.
- Top row:
  - Histogram for 'alpha' (x-axis: 2.0-2.7, y-axis: 0-0.8).
  - Scatter plot of 'alpha' vs 'gamma' (x-axis: 0.4-0.8, y-axis: 2.0-2.7).
  - Scatter plot of 'alpha' vs 'kp' (x-axis: 2.5-5.5, y-axis: 2.0-2.7).
- Middle row:
  - Correlation coefficient: -0.36.
  - Histogram for 'gamma' (x-axis: 0.4-0.8, y-axis: 0-0.8).
  - Scatter plot of 'gamma' vs 'kp' (x-axis: 2.5-5.5, y-axis: 0.4-0.8).
- Bottom row:
  - Correlation coefficient: -0.4.
  - Correlation coefficient: 0.86.
  - Histogram for 'kp' (x-axis: 2.5-5.5, y-axis: 0-0.8).::>
Fig. 4. Scatter-plot of the Markov Chain Monte Carlo (MCMC) samples for the virus strains Jena/5555 (top), Jena/2688, and Bakum/1832 (bottom).

<a id='aace66f9-30d0-4952-b341-2fdd9a45b589'></a>

model structure is hypothetic. Follow-up experiments including molecular parameters and genome-wide transcriptome analysis are ongoing to discriminate between alternative models and to verify the hypothesis that the second peak of biphasic course of infection is caused mainly by inflammation. Thus, the models sug- gested in the present study describe the course of influenza based on virus infection and on virus-induced immune response includ- ing pro- as well as anti-inflammatory response. Finally, they link the virus pathogenicity and/or inflammation with the observable clinical symptoms.

<a id='7052ce9d-03b5-4fa8-9d84-ffe41afc60ee'></a>

The small-scale model has some interesting features: First, it is able to describe the outcome of infection with four influenza virus strains. Thus, the model can be used to quantify the virulence of different strains by a set of 8 parameters listed in Tables 1 and 2. Three

<a id='312faa73-25c4-4c3d-a78c-fb9b6faaad8f'></a>

of them (a, kp, γ) were found to be structurally as well as practically
identifiable. The remaining five parameters are non-identifiable
with the given experimental data. They were fixed, which is no
critical for four of them due to their low sensitivity. Only for the
threshold parameter δ introduced by Kumar et al. (2004), the prac-
tical non-identifiability is an issue for further studies due to its high
sensitivity for biphasic profiles of the clinical score.

<a id='fa0867ed-0e50-4d3c-a133-8381006dbbec'></a>

Second, the model is able to simulate and interpret the cause of different outcomes of disease after virus challenge in mice. At day 2 p.i. mice became ill independently from the virus strain and infection dose studied. Maximum clinical score was observed between days 3 and 6 after infection with Jena/5555, Bakum/1832, and Jena/2688; afterwards mice recovered (monophasic kinetic). Also there is only low or no persistent inflammation. Obviously, the

<!-- PAGE BREAK -->

<a id='799fc1e4-8769-4dbb-8e13-bf1250e966e4'></a>

58

<a id='f4befca6-6edc-41d0-a36c-888c6198c8ff'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51–59

<a id='8a538093-a2c6-4e53-9c8a-4131909bcfa8'></a>

<::chart: The figure displays four line graphs, each showing body weight change (%) over 21 days after infection. Each graph compares a specific virus strain (represented by solid lines with square markers) to an uninfected control group (represented by dashed lines with triangle markers). The y-axis for all graphs is 'Body weight change (%)' ranging from 70 to 130, and the x-axis for all graphs is 'Days after infection' ranging from 0 to 21. Error bars are present on the data points. Top left: A line graph titled 'Jena/5258 10^6 TCID50' shows the body weight of infected mice decreasing to a minimum of approximately 83% around day 7-8, then gradually recovering to about 107% by day 21. The uninfected control group maintains a body weight around 100-110%. Top right: A line graph titled 'Jena/5555 10^6 TCID50' shows the body weight of infected mice decreasing to a minimum of approximately 84% around day 5-6, then recovering to about 105% by day 21. The uninfected control group maintains a body weight around 100-110%. Bottom left: A line graph titled 'Jena/2688 10^6 TCID50' shows the body weight of infected mice decreasing to a minimum of approximately 82% around day 6-8, then recovering to about 108% by day 21. The uninfected control group maintains a body weight around 100-120%. Bottom right: A line graph titled 'Bakum/1832 10^6 TCID50' shows the body weight of infected mice decreasing to a minimum of approximately 75% around day 6-7, then recovering to about 105% by day 21. The uninfected control group maintains a body weight around 100-115%. Fig. 5. Body weight change after infection with four different virus strains. Top left: A(H1N1)pdm09 Jena/5258; Top right: A(H1N1)pdm09 Jena/5555; bottom left: (H1N1)pdm09 Jena/2688; bottom right: European swine H1N2 Bakum/1832 (full squares) compared with uninfected mice (triangles).::>

<a id='bcb55eb0-8a3c-4962-8a5a-3ea4f9a7d79e'></a>

respective viruses have been eliminated efficiently by the immune response. In contrast, after infection with Jena/5258, a biphasic course of clinical symptoms were observed and simulated by the mathematical model. According to the established model, persistent inflammation contributes to the biphasic course of disease. Due to the experimental design, it remains unclear whether the virus was eliminated or not at the second peak of disease. So there is still an open question, whether the second peak of the disease is solely due to the persistent inflammation or due to the existence of mutant influenza virus.

<a id='98cbe6d5-92fc-4f00-bf77-ca757924d71b'></a>

For modeling of the biphasic behavior, a dynamic model introduced and theoretically studied by Kumar et al. (2004) was used and reduced. To the best of knowledge, in the present work, the first time Kumar's model was fitted to experimental data by linking the strength of inflammation with the clinical score that monitors clinical symptoms representing influenza in mice. In addition, the course of infection of the A(H1N1)pdm09 virus as well as a European swine H1N2 influenza virus (Bakum/1832) was modeled the first time.

<a id='18329d81-5e30-4f73-b184-bd23617191e6'></a>

Based on the model presented here, it can be assumed that the dynamics of influenza depends on both the virus pathogenicity as well as the adverse adaptive immune response that includes the pro-inflammatory cytokines (Pommerenke et al., 2012; Arankalle et al., 2010). Arankalle et al. (2010) showed the absence of viremia in both critically ill patient and mild patients infected with A(H1N1)pdm09 virus suggesting that viral replication may not be the major factor for the observed differences in the course of influenza disease. Based on the determined significantly increased levels of several chemokines and pro-inflammatory cytokines that may result in massive infiltration of leucocytes, these authors suggest that excessive damage resulting from immune response may also contribute to disease severity.

<a id='99f5fe7c-c0e4-4410-81a6-bc763b739469'></a>

This supports the model predictions where a higher severity and
inflammatory reaction was seen in one of the virus strain used.
The model established in the present study is able to interpret
and quantify the biphasic course of disease by a late inflammation
phase. It allows quantifying the rate of pro- and anti-inflammatory

<a id='0b3f1296-00a7-45bf-93ec-ae87c6ab6d5e'></a>

response (ε and ρ, respectively) as well as the conditions for the
onset of inflammation (δ, ω) by a set of identified parameters.
As suggested already by Kumar et al. (2004), it was hypothesized
with Eqs. (3) and (4) that the onset of inflammation (model vari-
able I) is triggered by the immune defense (if the model variable
D goes beyond the threshold value δ). The sensitivity of the pro-
inflammatory response in dependence on the immune defense is
quantified by the parameter (1/ω). These results warranted a more
detailed biological characterization of pro-inflammatory response
that is ongoing now. As published recently for a non-lethal infec-
tion of C57BL/6J mice with A/Puerto Rico/8/34 (Pommerenke et al.,
2012), a transcriptome analysis will help to clarify the role of factors
of innate and adaptive host immune response in severe biphasic
influenza in mice.

<a id='417e2fe1-7405-4d6e-88d8-38863d7b8d44'></a>

The observed clinical score was used for the presented model fit. These data are negatively correlated with the body weight (W; Fig. 5). Thus, the body weight could be used alternatively for model fit using a linear regression model (W=W₀−a*P−b*I).

<a id='117296c7-8626-44fb-b92f-728bd00b99d1'></a>

The model introduced by Canini and Carrat (2011) was based on population analysis of viral kinetics and symptoms dynamics which is similar to our study. The major limitation with their model was that data of immune response were not included. Their model was solely dependent on the pathogenicity of virus used. They assume that natural killer cells contribute to adverse inflammation which supports the hypothesis of the small scale model of the present study. In addition, the suggestion of Smith and Perelson (2011) to use clinical score as easily attainable experimental data supports the approach used here.

<a id='d6f4c4a1-e170-4f12-9ea0-06fd510ef1b5'></a>

The established model may help to quantify the dynamics of influenza induced by different virus strains and support the search for reasons for the severe, biphasic course of influenza in mice. Including antiviral treatment, drug administration could be optimized specifically for the virus strain used in further stud- ies. The model might allow to direct antiviral studies including the mathematical analysis of the use of antiviral compounds such as oseltamivir for the treatment of pandemic influenza virus

<!-- PAGE BREAK -->

<a id='08f8514a-a609-487f-9703-9ff6dc8fe40f'></a>

H. Manchanda et al. / BioSystems 118 (2014) 51-59

<a id='c0857d8e-6534-42e7-8b04-6a2615034857'></a>

59

<a id='7cb0e20f-77d3-490d-a80f-ff8f638faefd'></a>

infections (as modeled e.g., for the therapy HIV therapy by
Pitchaimani et al. (2013)).

<a id='3656b91c-437a-401a-a2a8-299a1855ec32'></a>

# 6. Conclusion

In the current study, a small-scale mathematical model of pandemic H1N1(2009) influenza A (A(H1N1)pdm09) infection was developed with a special emphasis on the late pro-inflammatory response. Simulation analysis of this model revealed that the pro-inflammatory response plays some adverse role on the disease condition. For the first time, the dynamics of four different influenza A virus strains (three A(H1N1)pdm09 and one European swine H1N2) were modeled. The established model allows quantifying the infection process by using a few interpretable parameters. This quantification includes the pathogenicity of different viral strains and the conditions and rate of pro- and anti-inflammatory response. Thus, the model will be important for the quantitative comparison of virus strains as well as condition for different outcome of the infection process. Most importantly, the main focus was to quantify the kinetics of different viral strains based on single model. The model study shows, that the inflammatory response is specific for the virus strain and, thus, it plays a crucial role for optimization of the therapeutic profile of drug administration that should be designed specifically for the virus strain. Due to the lack of additional experimental data, viral adaptation cannot be excluded as additional risk factor for biphasic influenza. Taken together, the models can be easily used to quantify influenza disease caused by different influenza virus strains and give hints for the experimental setup to further analyze the driving factors for severe disease as well a drug susceptibility.

<a id='8da1cd3f-78f4-47bf-829c-b2cc2b65bd05'></a>

## Acknowledgments
This study was supported by grant of the German Federal Min-
istry of Education and Research (01 K1 1006J) as well as the
European Social Fund and the Thuringia Ministry of Economy, Tech-
nology, and Work (2011 FGR0137).

<a id='f3072d49-1a69-455d-aec4-bfaf2df5f269'></a>

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/j.biosystems.2014.02.004.

<a id='7af539ac-df40-4146-afbf-a5bab065a195'></a>

# References
Arankalle, V.A., Lole, K.S., Arya, R.P., Tripathy, A.S., Ramdasi, A.Y., Chadha, M.S., San-gle, S.A., Kadam, D.B., 2010. Role of host immune response and viral load in the differential outcome of pandemic H1N1 (2009) influenza virus infection in Indian patients. PLoS ONE 5 (10), e13099.
Baccam, P., Beauchemin, C., Macken, C.A., Hayden, F.G., Perelson, A.S., 2009. Kinetics of influenza A virus infection in Human. J. Virol. 80 (15), 7509-7590.
Barnard, D.L., 2009. Animal models for the study of influenza pathogenesis and therapy. Antiviral. Res. 82 (2), A110-A122.
Bauer, K., Durrwald, R., Schlegel, M., Pfarr, K., Topf, D., Wiesener, N., Dahse, H.M., Wut-zler, P., Schmidtke, M., 2012. Neuraminidase inhibitor susceptibility of swine influenza A viruses isolated in Germany between 1981 and 2008. Med. Microbiol. Immunol. 201, 61-72.
Brun, R., Reichert, P., Kunsch, H., 2001. Practical identifiability analysis of large envi-ronmental simulation models. Water Resour. Res. 37 (4), 1015-1030.
Canini, L., Carrat, F., 2011. Population modeling of influenza A/H1N1 virus kinetics and symptoms dynamics. J. Virol. 85, 2764-2770.
Dawood, F.S., Jain, S., Finelli, L., Shaw, M.W., Lindstrom, S., Garten, R.J., Gubareva, L.V., Xu, X., Bridges, C.B., Uyeki, T.M., Novel Swine-Origin Influenza A (H1N1) Virus Investigation Team, 2009. Emergence of a Novel Swine-Origin Influenza A (H1N1) virus in humans. N. Engl. J. Med. 360 (25), 2605-2615.
de Castro, I.F., Guzmán-Fulgencio, M., García-Alvarez, M., Resino, S., 2010. First evi-dence of a pro-inflammatory response to severe infection with influenza virus H1N1. Crit. Care 14, 115.
Durrwald, R., Krumbholz, A., Baumgarte, S., Schlegel, M., Vahlenkamp, T.W., Selbitz, H.J., Wutzler, P., Zell, R., 2010. Swine influenza A vaccines,

<a id='546b673e-9abf-475c-b8f0-d1d320a8adc9'></a>

pandemic (H1N1) 2009 virus, and cross-reactivity. Emerg. Infect. Dis. 16,
1029-1030.
Ginsberg, M., Hopkins, J., Maroufi, A., Dunne, G., Sunega, D.R.<ET-Al>, 2009. Swine
influenza A (H1N1) infection in two children - Southern California, March-April
2009. MMWR Morb. Mortal Wkly. Rep. 58 (15), 400-402.
Goris, R.J., te Boekhorst, T.P., Nuytinck, J.K., Gimbrere, J.S., 1985. Multiple-organ
failure: generalized autodestructive inflammation? Arch. Surg. 120, 1109-1115.
Gubareva, L., Okomo-Adhiambo, M., et al., 2009. Update: drug susceptibility of
swine-origin influenza A (H1N1) viruses, April 2009. MMWR Morb. Mortal Wkly.
Rep. 58 (16), 433-435.
Hao, L., Jiang, G., Liu, S., Ling, L., 2013. Global dynamics of SIRS epidemic model with
saturation incidence. Biosystems 114 (1), 56-63.
Hancioglu, B., Swigon, D., Clermont, G., 2006. A dynamical model of human immune
response to influenza A virus infection. J. Theor. Biol. 246 (1), 70-86.
Handel, A., Longini, I.M., Antia, R., 2010. Towards a quantitative understanding of the
within-host dynamics of influeza A infections. J. R. Soc. Interface 7 (42), 35-47.
Haario, H., Laine, M., Mira, A., Saksamn, E., 2006. DRAM: efficient adaptive MCMC.
Stat. Comput. 16, 339-354.
Kao, R.Y., Yang, D., Lau, L.S., Tsui, W.H., Hu, L., Dai, J., Chan, M.P., Chan, C.M., Wang,
P., Zheng, B.J., Sun, J., Huang, J.D., Madar, J., Chen, G., Chen, H., Guan, Y., Yuen,
K.Y., 2010. Identification of influenza A nucleoprotein as an antiviral target. Nat.
Biotechnol. 28 (6), 600-605.
Kirchmair, J., Rollinger, J.M., Liedl, K.R., Seidel, N., Krumbholz, A., Schmidtke, M.,
2011. Novel neuraminidase inhibitors: identification, biological evaluation and
investigations of the binding mode. Future Med. Chem. 3 (4), 437-450.
Kumar, R., Clermont, G., Vodovotz, Y., Chow, C.C., 2004. The dynamics of acute
inflammation. J. Theor. Biol. 230, 145-155.
Lee, H.Y., Topham, D.J., Park, S.Y., Hollenbaugh, J., Treanor, J., Mosmann, T.R., Jin, X.,
Ward, B.M., Miao, H., Holden-Wiltse, J., Perelson, A.S., Zand, M., 414 Wu, H., 2009.
Simulation and prediction of the adaptive immune response to influenza A virus
infection. J. Virol. 83, 7151-7165.
Li, Q., Qi, J., Zhang, W., Vavricka, C.J., Shi, Y., Wie, J., Feng, E., Shen, J., Chen, J., Liu, D.,
He, J., Yan, J., Liu, H., Jiang, H., Teng, M., Li, X., Gao, G.F., 2010. The 2009 pandemic
H1N1 neuraminidase N1 lacks the 150-cavity in its active site. Nat. Struct. Mol.
Biol. 17 (10), 1266-1268.
Moré, J.J., 1978. The Levenberg-Marquardt algorithm: implementation and theory.
In: Watson, G.A. (Ed.), Numerical Analysis, Dundee 1977. Lecture Notes Math.
630, 105-116.
Miao, H., Hollenbaugh, J.A., Zand, M.S., Holden-Wiltse, J., Mosmann, T.R., Perelson,
A.S., Wu, H., Topham, D.J., 2010. Quantifying the early immune response and
adaptive immune response kinetics in mice infected with influenza A virus. J.
Virol. 84 (13), 6687-6698.
Nguyen, H.T., Fry, A.M., Gubareva, L.V., 2012. Neuraminidase inhibitor resistance
in influenza viruses and laboratory testing methods. Antivir. Ther. 17 (1 Pt B),
159-173.
Pawelek, K.A., Huynh, G.T., Quinlivan, M., Cullinane, A., Rong, L., Perelson, A.S., 2012.
Modeling within-host dynamics of influenza virus infection including immune
responses. PLoS Comput. Biol. 8 (6), e1002588.
Petzold, L.R., 1983. Automatic selection of methods for solving Sti and Nonsti systems
of ordinary differential equations. SIAM J. Sci. Stat. Comput. 4, 136-148.
Pitchaimani, M., Monica, C., Divya, M., 2013. Stability analysis for HIV infection delay
model with protease inhibitor. Biosystems 114, 118-124.
Pommerenke, C., Wilk, E., Srivastava, B., Schulze, A., Novoselova, N., Geffers, R.,
Schughart, K., 2012. Global transcriptome analysis in influenza-infected mouse
lungs reveals the kinetics of innate and adaptive host immune responses. PLoS
ONE 7 (7), e41169.
Raue, A., Kreutz, C., Maiwald, T., Bachmann, J., Schilling, M., Klingmüller, U.,
Timmer, J., 2009. Structural and practical identifiability analysis of partially
observed dynamical models by exploiting the profile likelihood. Bioinformatics
25, 1923-1929.
Reed, L.J., Muench, H., 1938. A simple method of estimating fifty percent endpoints.
Am. J. Hyg. 27 (3), 493-497.
Saenz, R.A., Quinlivan, M., Elton, D., Macrae, S., Blunden, A.S., Mumford, J.A., Daly, J.M.,
Digard, P., Cullinane, A., Grenfell, B.T., McCauley, J.W., Wood, J.L., Gog, J.R., 2010.
Dynamics of influenza virus infection and pathology. J. Virol. 84 (8), 3974-3983.
Schrader, C., Suss, J., 2003. Genetic characterization of a porcine H1N2 influenza
virus strain isolated in Germany. Intervirology 46, 66-70.
Smith, A.M., Adler, F.R., McAuley, J.L., Gutenkunst, R.N., Ribeiro, R.M., McCullers,
J.A., Perelson, A.S., 2011. Effect of 1918 PB1-F2 expression on influenza A virus
infection kinetics. PLoS Comput. Biol. 7 (2), e1001081.
Smith, A.M., Perelson, A.S., 2011. Influenza A virus infection kinetics: quantitative
data and models. Syst. Biol. Med. 3, 429-445.
Soetaert, K., Petzoldt, T., Woodrow, R., Setzer, R.W., 2010. Solving differential equa-
tions in R: package deSolve. J. Stat Softw. 33 (9), 1-25.
Soetaert, K., Petzoldt, T., 2010. Inverse modeling, sensitivity and Monte Carlo analysis
in R using FME package. J. Stat. Softw. 33 (3), 1-28.
Takala, A., Jousela, I., Jansson, S.E., Olkkola, K.T., Takkunen, O., Orpana, A., Karonen,
S.L., Repo, H., 1999. Markers of systemic inflammation predicting organ failure
in community-acquired septic shock. Clin. Sci. (Lond.) 97, 529-538.
Tscherne, D.M., Garcia-Sastre, A., 2011. Virulence determinants of pandemic
influenza viruses. J. Clin. Invest. 121 (1), 6-13.
Wattrang, E., Jessett, D.M., Yates, P., Fuxler, L., Hannant, D., 2003. Experimental
infection of ponies with equine influenza A2 (H3N8) virus strains of differ-
ent pathogenicity elicits varying interferon and interleukin-6 responses. Viral
Immunol. 16 (1), 57-67.
WHO 2013 Influenza Update No. 184
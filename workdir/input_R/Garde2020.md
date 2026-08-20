<a id='f82f2057-0987-4823-ad50-23d700b2803c'></a>

ROYAL SOCIETY
OPEN SCIENCE

<a id='f8e5a81a-41cc-43d0-a8b3-ccf5b7f49548'></a>

royalsocietypublishing.org/journal/rsos

<a id='bbccadb6-4fcf-46c3-89d0-62475bcd91ba'></a>

<::logo: [Research] Research. The logo features the word "Research" in black, an open padlock symbol, and a circular icon with a red flag and the text "Check for updates".::>

<a id='716318a6-d907-412c-a5a9-d2770a8be90e'></a>

Cite this article: Garde R, Ibrahim B, Kovács ÁT,
Schuster S. 2020 Differential equation-based
minimal model describing metabolic oscillations
in Bacillus subtilis biofilms. R. Soc. open sci. 7:
190810.
http://dx.doi.org/10.1098/rsos.190810

<a id='0630a217-28d4-4fab-8505-a33b3e8f4e6e'></a>

Received: 15 May 2019
Accepted: 15 January 2020

<a id='fad20d07-f838-4366-8d44-ef40c3222c4c'></a>

Subject Category:
Mathematics

<a id='4545f1da-d854-4f3c-a779-8e25ff122e1d'></a>

Subject Areas:
systems biology/computational biology/
mathematical modelling

<a id='e68da442-d131-4db7-b253-acdcc8838273'></a>

**Keywords:**
metabolic oscillations, *Bacillus subtilis*,
minimal model, biofilm, Hopf bifurcation,
glutamate metabolism

<a id='4024b65f-4ef4-4fda-a317-bfce7ea2bceb'></a>

Author for correspondence:
Stefan Schuster
e-mail: stefan.schu@uni-jena.de

<a id='99094734-a23e-4df6-9dcb-f328dba44a5b'></a>

Electronic supplementary material is available online at https://doi.org/10.6084/m9.figshare.c.4828275.

<a id='9cc5b628-791d-4117-a8d0-c8752603d1b9'></a>

THE ROYAL SOCIETY
PUBLISHING

<a id='8bd45cf0-cb34-4ee0-bdba-6de2de7bfff9'></a>

Differential equation-based
minimal model describing
metabolic oscillations in
_Bacillus subtilis_ biofilms

<a id='61179c64-7cb0-4e80-9a0a-add7047ebdff'></a>

Ravindra Garde1,2, Bashar Ibrahim1,4,5, Ákos T. Kovács3
and Stefan Schuster1

1Department of Bioinformatics, Matthias Schleiden Institute, Friedrich Schiller University Jena, Ernst-Abbe-Platz 2, 07743 Jena, Germany
2Max Planck Institute for Chemical Ecology, Hans-Knöll-Strasse 8, 07745 Jena, Germany
3Bacterial Interactions and Evolution Group, DTU Bioengineering, Technical University of Denmark, Søltofts Plads Building 221, 2800 Kgs. Lyngby, Denmark
4Centre for Applied Mathematics and Bioinformatics, and 5Department of Mathematics and Natural Sciences, Gulf University for Science and Technology, Hawally 32093, Kuwait

ID BI, 0000-0001-7773-0122; ÁTK, 0000-0002-4465-1636;
SS, 0000-0003-2828-9355

<a id='76230a9c-53ba-4f81-84be-e58692dd2af8'></a>

Biofilms offer an excellent example of ecological interaction among bacteria. Temporal and spatial oscillations in biofilms are an emerging topic. In this paper, we describe the metabolic oscillations in *Bacillus subtilis* biofilms by applying the smallest theoretical chemical reaction system showing Hopf bifurcation proposed by Wilhelm and Heinrich in 1995. The system involves three differential equations and a single bilinear term. We specifically select parameters that are suitable for the biological scenario of biofilm oscillations. We perform computer simulations and a detailed analysis of the system including bifurcation analysis and quasi-steady-state approximation. We also discuss the feedback structure of the system and the correspondence of the simulations to biological observations. Our theoretical work suggests potential scenarios about the oscillatory behaviour of biofilms and also serves as an application of a previously described chemical oscillator to a biological system.

<a id='46bce448-b3b2-433a-aaf8-c1ae353a2954'></a>

# 1. Introduction

Development of a complex biofilm provides several benefits to bacteria, including efficient nutrient distribution, defence from chemical attacks or, in the case of a floating pellicle on the surface of liquids, better gaseous exchange [1]. Biofilms are thus complex communities of bacteria and as such, many types of

<a id='317d1682-81cc-4bd6-9b32-ee46aa8eb0d0'></a>

© 2020 The Authors. Published by the Royal Society under the terms of the Creative Commons Attribution License http://creativecommons.org/licenses/by/4.0/, which permits unrestricted use, provided the original author and source are credited.

<!-- PAGE BREAK -->

<a id='faeb5c90-f550-4515-bee4-bb5949a23e89'></a>

social dynamics come into play [2,3]. One of these is the division of labour [4,5]. The core of the biofilm growing on a solid surface shows a different metabolic state than the periphery. The periphery can freely access the nutrients from the surrounding environment. The interior, however, faces hindrance in obtaining a stable inflow of nutrients because the peripheral cells use up the nutrients that diffuse towards the interior. An experimental set-up to simulate that situation is provided by a microfluidics chamber [4].

<a id='396c021e-318b-47ed-a25f-5ce2067722f5'></a>

An example of such a nutrient gradient is the production and diffusion of ammonia in the biofilm. Every cell in the biofilm has the ability to produce ammonia [4,6]. However, this small chemical compound is highly diffusive and therefore escapes into the environment as soon as it is produced by the cells in the periphery, thus leading to waste of nitrogen. In the interior, the ammonia produced by the cells diffuses out into the periphery. Thus, the interior cells monopolize ammonia production for the entire biofilm. Ammonia being an essential component of glutamine metabolism could be used to control the growth rate of the periphery by limiting its supply. The interplay between the inner and outer cells is required for glutamine synthesis and therefore the growth of the biofilm [4,6,7].

<a id='51f506c9-8818-4156-8e40-55ba2caaafdc'></a>

To understand biofilms more closely and make predictions based on empirical data, several models have been developed [4,7–12]. Liu et al. [4] observed oscillations in the biofilm, which they explained by different metabolic roles performed by the different compartments in the biofilm. They also established a model based on six differential equations. They defined two regions: the interior and periphery. Each of the regions has a variable representing glutamate and another representing the concentration of housekeeping proteins like ribosomal proteins. Ammonia and the active form of the enzyme glutamate dehydrogenase are also variables of the model.

<a id='e01cc50f-aad9-41e0-bf3b-aea6ea66a352'></a>

Since many biological oscillators have been described by less than six variables [13,14], a simpler model could be established for biofilm oscillations as well. Our ultimate aim was to develop a minimal model to describe the metabolic oscillations happening in a biofilm. Minimal models are the simplest way to describe a certain phenomenon with the least number of parameters [15] and this is in agreement with Occam's razor. For example, minimal models were established for glycolytic oscillations by Higgins [16] and Sel'kov [17] and for calcium oscillations by Somogyi & Stucki [18].

<a id='02e52785-0028-43f3-92f6-fafeb7f23b46'></a>

Here, we employ the smallest chemical reaction system showing a Hopf bifurcation [19], which was further analysed [20,21] and used to describe p53 oscillations [22]. At a Hopf bifurcation, damped oscillations turn into undamped oscillations [15,23]. In particular, Wilhelm & Heinrich [19,20] performed a thorough stability analysis of the model. We test to what extent the terms in this model match the processes in a biofilm system. In this analysis, we focus on the Hopf bifurcation, discuss the feedback structure and point out the correspondence of the simulations to biological observations.

<a id='fe9f2476-2e79-48a8-b389-e8ca5b292829'></a>

In our model, we use three variables only: ammonia, and interior and peripheral glutamate. Besides the quest for minimality, a reason for not considering the concentrations of housekeeping proteins as variables is that they change on a longer time-scale than metabolites. A similarity to the larger Liu model [4] is that, among the various amino acids, we focus on the metabolism of glutamate since glutamate and ammonia are both involved in the production of various amino acids through _trans-amination_, which is then equated to growth.

<a id='a995ec0a-9747-4d5a-a579-d2c56fc740c0'></a>

To study the effect and possible benefit of oscillations, it is of interest to compute the average values of variables, as was done for several oscillators [24–29]. For linear differential equation systems showing oscillations (such as the system describing the harmonic pendulum), the average values equal the values at the marginally stable steady state. For nonlinear differential equation systems, the average values often differ from the values at the unstable steady state surrounded by the oscillations. However, there are some types of nonlinear systems for which equality holds, for example, Lotka–Volterra systems of any dimension [25]. The equality property has also been proved for some models of calcium oscillations [27,30] and the Higgins–Selkov oscillator [27]. Here, we probe the model employed for describing biofilm oscillations for the above-mentioned property.

<a id='371e515e-e9d0-49b0-83f9-11925feeae12'></a>

## 2. Material and methods

### 2.1. The model

Based on the scenario described by Liu et al. [4], the biofilm was separated into two compartments—the interior and the periphery. Here, we use a minimalist approach and try to model biofilm oscillations with the simplest model possible. Accordingly, we use the smallest chemical reaction system with Hopf

<a id='248a9039-5db4-4f90-a92c-33dea0386275'></a>

2

<a id='9b1bd9af-ab2d-42f4-8ed3-4aee9145e3af'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='e6e1a8ef-1f7c-4648-88d6-0617119cc6ce'></a>

<::figure: diagram::>(a) Schematic of the biofilm metabolic oscillation model. A large light blue circle labeled "environment" encloses a smaller light blue circle labeled "periphery". The "periphery" circle encloses an even smaller yellow circle labeled "interior". A light blue oval labeled "Gₑ" is outside the "environment". Inside the "periphery" (but outside "interior") is a blue rectangle labeled "Gₚ". Inside the "interior" is a red rectangle labeled "Gᵢ" and a yellow rectangle labeled "A". A black oval labeled "biomass" is located between the "periphery" and "interior" circles, slightly overlapping the "periphery" boundary. An arrow labeled "k₁" goes from Gₑ to Gₚ. An arrow labeled "k₂" goes from Gₚ to biomass. An arrow labeled "k₄" goes from Gₚ to Gᵢ. An arrow labeled "k₅" goes from Gᵢ to A. An arrow labeled "k₃" goes from A, exiting the "interior" and "periphery" circles. (b) Feedback structure of the model. Three colored rectangles are shown: blue Gₚ, red Gᵢ, and yellow A. Gₚ has two self-loops, one with a "+" sign and one with a "-" sign. Gᵢ has a self-loop with a "-" sign. A has a self-loop with a "-" sign. A dashed arrow with a "+" sign goes from Gₚ to Gᵢ. A dashed arrow with a "+" sign goes from Gᵢ to A. A dashed arrow with a "-" sign goes from A to Gₚ.Figure 1. Schematic of the biofilm metabolic oscillation model. (a) The five reactions with rate constants k₁ through k₅ between the substances Gᵢ, Gₚ, A having variable concentrations and Gₑ considered to be constant. The final result is the production of biomass. (b) Feedback structure of the model. Gₚ is self-amplifying while all three variables are self-degrading. Gₚ positively influences Gᵢ, which positively influences A which negatively influences Gₚ, thus, the overall feedback is negative.<::>

<a id='bb36ffff-84ec-4788-aab3-550ef2d9820f'></a>

bifurcation [19]. The term chemical system mathematically means that only up to bilinear terms are involved. It turns out that this model matches the biological set-up.

<a id='5ae6d0d3-e505-467f-9254-0dcfb7ff11e1'></a>

The model includes five reactions (figure 1) and three species with variable concentrations. The general variables X, Y and Z from the Wilhelm and Heinrich model can be assigned for the biofilm system to: peripheral glutamate (Gp), ammonia (A) and internal glutamate (Gᵢ), respectively. Based on mass-action kinetics, the reactions have been translated as follows into a system of ordinary differential equations (ODEs):

<a id='9caf23cd-e55d-43cb-8973-03fb574a699b'></a>

and

    dG_p  = k_1 G_E G_p - k_4 G_p - k_2 A G_p
    dt                                                      (2.1a)

    dA    = -k_3 A + k_5 G_i
    dt                                                      (2.1b)

    dG_i  = k_4 G_p - k_5 G_i
    dt                                                      (2.1c)

<a id='7a745e86-8626-4485-950f-6a66634b0e56'></a>

Model assumptions and interpretation of terms in the model:

- $k_1G_E G_p$: The uptake of glutamate from the environment ($G_E$) by the periphery of the biofilm. $G_E$ is supplied in a large excess, hence considered constant. The uptake of glutamate ($G_p$) is dependent on itself because glutamate represents the total amino acid and thus protein concentration in the biofilm periphery and can be assumed, in rough approximation, to be proportional to the concentration of various transport proteins embedded in the cell membranes. The greater the concentration of these proteins, the higher is the glutamate uptake rate. Without this self-amplification of glutamate, the system would not oscillate by construction of the minimal model.
- $k_4G_p$: Diffusion of glutamate from the periphery of the biofilm into its interior. We do not consider self-amplification by $G_i$ in the main text. We analysed the effect of self-amplification of $G_i$ using the term $k_4G_iG_p$ (electronic supplementary material, figure S4).
- $k_2AG_p$: Consumption of glutamate and ammonia to produce biomass. As a simplification, we assumed that only the interior cells produce ammonia since that produced by the peripheral cells is rapidly lost to the environment.
- $k_5G_i$: Consumption of glutamate to produce ammonia.
- $k_3A$: Diffusion of ammonia into the surroundings. The loss of ammonia due to diffusion is much larger than that taken up by the periphery to produce biomass. Therefore, the term $k_2AG_p$ does not appear in equation (2.1b).

<a id='5ddaad50-0e33-4c97-a3a1-87596b454197'></a>

3

<a id='cc72860a-dcf4-4f70-9dc3-9706fa1acfd7'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='a8175434-e454-47f2-9a8f-94b3972adbef'></a>

Table 1. List of parameters used in the model. For explanations, see text.

<a id='3676f212-9a1f-4b6d-9300-437ebde07258'></a>

4

<a id='32a27b11-4758-47ba-a7f9-f37412d00202'></a>

<table id="3-1">
<tr><td id="3-2">parameter</td><td id="3-3">symbol</td><td id="3-4">value with unit</td></tr>
<tr><td id="3-5">rate constant of glutamate diffusion from environment to biofilm</td><td id="3-6">k₁</td><td id="3-7">0.3426 (mmol l⁻¹ h)⁻¹</td></tr>
<tr><td id="3-8">biomass formation coefficient</td><td id="3-9">k₂</td><td id="3-a">5.3 (mmol l⁻¹ h)⁻¹</td></tr>
<tr><td id="3-b">rate constant of ammonia diffusion [32]</td><td id="3-c">k₃</td><td id="3-d">4 h⁻¹</td></tr>
<tr><td id="3-e">rate constant of glutamate diffusion within biofilm [33,34]</td><td id="3-f">k₄</td><td id="3-g">2 h⁻¹</td></tr>
<tr><td id="3-h">ammonia production coefficient</td><td id="3-i">k_S</td><td id="3-j">2.3 h⁻¹</td></tr>
<tr><td id="3-k">glutamate concentration in the environment [4]</td><td id="3-l">G_E</td><td id="3-m">30 mmol l⁻¹</td></tr>
<tr><td id="3-n">conversion factor for biomass production</td><td id="3-o">b</td><td id="3-p">0.1 ((mmol l⁻¹)² h)⁻¹</td></tr>
</table>

<a id='49ef83f0-a32a-4cf6-9a1d-47d700994c98'></a>

## 2.2. Simulation

For computer simulations, we used the software COPASI v. 4.16 and 4.24 [31] and its LSODA deterministic solver. The simulations were double-checked using the Matlab ode15s (MathWorks) function. The figures of the simulations were produced using COPASI, and the three-dimensional (3D) phase plot was generated using the lines3D function of R plot3D library. The biomass plot was generated using the R function ggplot.

<a id='3696f6b1-c6df-4792-858f-c896223c9bd1'></a>

Parameter values are given in table 1. They are obtained by rescaling the parameter values from the Wilhelm & Heinrich paper [19] such that the oscillation period observed in the experimental work by Liu et al. [4] is matched. The glutamate concentration in the environment was adopted from the Liu et al. paper [4]. We have chosen the rate constant of diffusion of ammonia, k3, to be twice as high as that of glutamate, k4. This is because the diffusion coefficient for ammonia [32] is about 1.6  10⁻⁵ cm² s⁻¹, while that for glutamate [33,34] is about 8  10⁻⁶ cm² s⁻¹. k₁ and k₂ had to be increased in order to obtain undamped oscillations and to match the same period. Overall, the parameters allow a good comparison to the results by Wilhelm & Heinrich [19], while also being realistic from a physico-chemical point of view.

<a id='2f486c7c-6ff9-434e-84cc-98e3ce9c4abd'></a>

The predicted doubling time was calculated by averaging the relative increase in biomass at four consecutive time points of the maxima of ammonia concentration.

<a id='efd11a65-c992-4400-8224-799b6675ac22'></a>

# 3. Results

## 3.1. Steady states

The steady states of the system can be calculated analytically. This gives a trivial steady state (TSS)

$G_p = A = G_i = 0$ (3.1)

<a id='6bd6d75b-7fbc-4ddc-8951-925623e96866'></a>

Gp = A = G₁ = 0                                       (3.1)
and a non-trivial steady state (NTSS)

<a id='763a1b07-ed80-4d96-8c23-b0b2ba76b092'></a>

Gp,ss = ( (k1GE - k4) / (k2k4) ) k3 (3.2a)
Ass = (k1GE - k4) / k2 (3.2b)

and

Gi,ss = ( (k1GE - k4) / (k2k5) ) k3. (3.2c)

<a id='4cc3d01e-0a2e-423c-8b00-4e4c3ae9f212'></a>

It is worth noting that the concentrations at the latter state are linear functions of G~E~. The TSS and NTSS are stable if k~1~G~E~ - k~4~ is negative or positive, respectively [19]. At the threshold, a transcritical bifurcation [35] occurs; that is, the two steady states interchange their stability. At a further threshold, k~1~G~E~=k~3~+k~4~+k~5~, the stable NTSS turns unstable in a Hopf bifurcation [19].

<a id='9b5fa200-0400-45a5-ac01-5918c71ced27'></a>

## 3.2. Time course shows oscillations
We run the time course calculation of the system (2.1a-c) for 25 simulation hours with 1000 steps each of size 0.025 h (1.5 min). The period for oscillations is about 126 min (2 h 6 min), which is in agreement with

<a id='56ae5614-31de-4605-9697-f93f5d5226e3'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='155a7d6e-3bc1-4876-b179-b3a9162cc53f'></a>

time course

<a id='a2cbbd8d-71b8-4acc-a607-f65f9e4c0203'></a>

<::chart: Line chart showing concentration over time. The x-axis is labeled "time (h)" and ranges from 0 to 25. The y-axis is labeled "concentration (mmol l⁻¹)" and ranges from 0 to 16. There are three lines on the chart, representing different substances: a yellow line for [A], a red line for [Gᵢ], and a blue line for [Gₚ]. All three lines exhibit a cyclical pattern of increasing and decreasing concentrations over time. The blue line (Gₚ) shows the highest peaks, followed by the red line (Gᵢ), and then the yellow line (A). The peaks of the blue line reach approximately 14-15 mmol l⁻¹, the red line peaks around 6-7 mmol l⁻¹, and the yellow line peaks around 2-3 mmol l⁻¹. The cyclical pattern repeats approximately every 2 hours. A legend at the bottom indicates: [A] (yellow), [Gᵢ] (red), and [Gₚ] (blue).::>

**Figure 2.** Time course of ammonia (yellow) and interior (red) and peripheral (blue) glutamate as computed by the minimal model.
Parameter values: refer to table 1.

<a id='a9613a86-cfe7-4195-8922-edfa05b924c2'></a>

<::chart: Six three-dimensional phase portraits arranged in a 2x3 grid. Each plot shows trajectories in a space defined by axes G_i, G_p, and A. The trajectory runs anti-clockwise in the perspective shown. Top row, from left to right: 1. Plot for G_E = 5 mmol l⁻¹: Shows a single curved trajectory approaching a stable point. 2. Plot for G_E = 8 mmol l⁻¹: Shows a single curved trajectory approaching a stable point. 3. Plot for G_E = 20 mmol l⁻¹: Shows a trajectory spiraling inwards towards a central point, indicating damped oscillations. Bottom row, from left to right: 4. Plot for G_E = 25 mmol l⁻¹: Shows a trajectory forming a closed loop (limit cycle). 5. Plot for G_E = 35 mmol l⁻¹: Shows a trajectory forming a larger, more complex limit cycle. 6. Plot for G_E = 60 mmol l⁻¹: Shows a trajectory forming an even larger and more complex limit cycle. Figure 3. Three-dimensional phase portrait of all the variables at various values of G_E. The trajectory runs anti-clockwise in the perspective shown here. Top three trajectories from left to right depict approaches towards: the TSS, the NTSS in a non-oscillatory way and the NTSS by damped oscillations. The bottom three trajectories depict the convergence towards limit cycles beyond the Hopf bifurcation (G_E = 24.41). For parameter values except G_E, see table 1.::>

<a id='dc530447-28ff-4b03-ae65-65a2b118847e'></a>

the experimental observations [4], because the parameters have been rescaled accordingly (see above).
The amplitude of oscillations is observed to be 3.0 mmol l-¹ for ammonia, 7.1 mmol l-¹ for interior
glutamate and 14.9 mmol l-¹ for peripheral glutamate (figure 2). It can be seen that the three variables
oscillate with phase shifts, i.e. asynchronously.

<a id='5ff1e593-1054-4c65-9422-e5b06e9e090f'></a>

In order to see the interdependence between the variables of our model, we plot the phase portrait of all three variables for various values of G_E (figure 3). G_E is an appropriate bifurcation parameter because

<a id='85deedf6-66d0-4c02-a883-4ac70e46301b'></a>

5

<a id='b0c1eaec-b848-47e9-bee5-7f4ebb15e1f5'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='2301a797-bbd1-4064-a9d6-30f38bd87ad0'></a>

<::line chart showing biomass (cell l^-1) on the y-axis (logarithmic scale) versus time (h) on the x-axis. The y-axis ranges from 10^10 to 2 x 10^12. The x-axis ranges from 0 to 10.0. Multiple lines are plotted, with colors indicating different values of G_p0, as shown in the legend. The legend shows a color gradient from light blue to dark blue/black, corresponding to G_p0 values of 10.0, 7.5, 5.0, and 2.5 respectively. The lines generally show an initial plateau, followed by step-like increases in biomass, with the rate and final biomass level increasing with higher G_p0 values.: chart::>

<a id='75dced5b-145f-4300-8568-3c161db3e634'></a>

Figure 4. Plot of the time course of growth as calculated from equation (3.4) for various initial values of Gp from 1 to 10 mmol l⁻¹ with a step size of 1 mmol l⁻¹ (all wavy curves). We took 10¹⁰ cells l⁻¹ as the initial value of B. On average, the curves have a doubling time of about 99 min. The black monotonic curve (initial value: 10 cells l⁻¹) indicates the growth calculated by the steady-state values.

<a id='5c23b79a-9b76-4133-909e-5a459ac8cab4'></a>

the external glutamate concentration can be changed in experiment. Wilhelm & Heinrich [19] presented a similar figure for the vicinity of the Hopf bifurcation. In our figure 3, also the non-oscillatory relaxation towards the TSS and NTSS for appropriate parameter values is shown. G_E values below 15 mmol l-1 eliminate the oscillations (even damped ones).

<a id='be716f76-e3c1-42d6-9804-19424e1d28a7'></a>

As per the assumptions of our model, $k_2AG_p$ is a proxy for the input for the synthesis of biomass from ammonia and glutamate and is thus related to the growth of the biofilm. Biomass production can be described by the following differential equation:

<a id='aba4a47a-c935-419d-a18d-e5e954aa94b6'></a>

dB / dt = bAGpB, (3.3)

<a id='53bdc3a6-9995-4747-a07c-ea083de11cce'></a>

where _b_ is a conversion factor and was tuned to 0.1 ((mmol l⁻¹)² h)⁻¹ so that the doubling time is in agreement with the experimental values [36]. The number of cells can be converted to biomass by taking the volume of a typical _B. subtilis_ cell of about 0.85 ± 0.38 µm³ [37] and the average density of 1 g ml⁻¹ which results in 8.5 ± 0.38 × 10⁻¹³ g cell⁻¹. The numerical solution of equation (3.3) for various initial values of G_p_ is shown in figure 4. It can be seen that there is periodic retardation in growth.
Figure 4 also displays the growth curve in the hypothetical case where G_p_ and _A_ subsisted at steady state (black curve).

<a id='eee025bb-9e97-4c84-9d90-2479ee9a21b2'></a>

The initial value of Gp for the growth with constant growth rate (black monotonic curve) was chosen such that biomass is comparable to that for oscillating growth in the first 10 h. If the same initial values as for the growth with varying growth rate were chosen, biomass would grow to higher values right from the beginning. Thus, the numerical calculations suggest that oscillating growth for this system is not in favour of increasing growth rate. As can be seen from electronic supplementary material, figure S5, the steady-state growth rate overtakes the oscillating growth rate at about 10.5 h.

<a id='fa206ea4-1614-4681-8765-be6c17ab0957'></a>

It is an important result that biofilm oscillations can be described by considering a few processes only, which are listed below equation (2.1). They include considerably less processes than the Liu model [4]. However, they do include the diffusion of ammonia to the surroundings, unlike that model. Thus, it is plausible to assume that these are the most relevant processes for the phenomenon of oscillations.

<a id='a0b52904-f48b-4ad5-9a04-746f54ea7515'></a>

6

<a id='f67b3604-2bc0-4c17-b3cd-ca8da5bc4bb8'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='cb557c35-086d-42da-a7a3-b15af85f0f1f'></a>

All other processes (such as the diffusion of glutamate from the interior of the biofilm to its periphery and from there to the environment) can be neglected.

<a id='7699c9a8-59eb-4475-9bcd-10ccd36b1348'></a>

3.3. Average concentrations and average growth rate
Motivated by the reasoning in the Introduction, we now compare the average concentrations with the steady-state concentrations. As the model under study is a mixture of a Lotka–Volterra equation, equation (2.1a) and two linear equations (2.1b,c), it can be assumed that the values are equal. To demonstrate this, we divide equation (2.1a) by Gp

<a id='ee5c3a2b-e86f-4c8b-9d80-b0fc1199a290'></a>

1/G_p dG_p/dt = d/dt (ln G_p) = k - k_2 A where k = k_1 G_E - k_4.

<a id='ba4ea77b-6bde-4018-8afa-a79ab6dc4e4a'></a>

We integrate over one oscillation period, T

<a id='af8e5fbf-c6b9-43ee-a97d-891d1e74e58f'></a>

$$\int_{0}^{T} \frac{d}{dt}(\ln G_p) \, dt = 0 = \int_{0}^{T} (k - k_2 A) \, dt$$ 
$$= kT - k_2 \int_{0}^{T} A \, dt,$$

<a id='ccfb8ef7-468d-41d2-a13c-0534697c1e39'></a>

where the integral is zero because Gp(T) = Gp(0)

<a id='bef81460-0a8f-4894-8af9-a2571d7ddf55'></a>

$\frac{1}{T}\int_{0}^{T} A dt = \langle A \rangle = \frac{k}{k_2} = A_{ss}$

<a id='bf72dc2b-3808-4443-b2b7-5402b9cfe94e'></a>

Now, we calculate the integral of dA/dt:

<a id='55b64e19-55ad-4dad-957e-772f813540e2'></a>

$\int_0^T \frac{dA}{dt} dt = 0 = \int_0^T (k_5G_i - k_3A)dt$

$= k_5 \int_0^T G_i dt - k_3 \int_0^T A dt$

<a id='c0ca6a3c-17e0-4995-b68b-81fe086c440a'></a>

k_5 \langle G_i \rangle = k_3 A_{ss} = \frac{k k_3}{k_2}

<a id='9ba79731-7c76-415f-98ce-cc2583ae6bde'></a>

⟨G_i⟩ = k k_3 / k_2 k_5 = G_i,ss.

<a id='28c9b334-620f-4fc8-bc7d-1f8ff4ae17b1'></a>

Now, we calculate the integral of dG_i / dt and derive, analogously

<a id='f49c36de-86d1-489e-8400-b3bc58e3bff8'></a>

<G_p> = G_{p,ss}.

<a id='babad5ad-ad8d-4ce3-b3d9-ba5145f7b451'></a>

Thus, the average concentrations are equal to the steady-state concentrations.

<a id='486bdc93-26bb-45ea-a849-e9c90f792e71'></a>

The question arises whether the oscillations have an effect on the average of the bilinear term k₂AGp.
This is not immediately clear, although figure 4 suggests that the average growth rate is slower than that
at the metabolic steady state. Note that the growth term bAGpB is trilinear.

<a id='8a7b52a6-d0d2-4d7c-86a7-daab567f953a'></a>

To check whether $\langle A G_p \rangle = A_{ss} \cdot G_{p,ss}$, we integrate $dG_p/dt$ over one period, $T$

<a id='32c1d57d-124c-4d6f-8997-2882a1c26003'></a>

$\int_{0}^{T} \frac{dG_p}{dt} dt = 0 = \int_{0}^{T} kG_p dt - \int_{0}^{T} k_2AG_p dt$

$= k\langle G_p \rangle T - k_2A G_p T.$

<a id='0ee08816-72eb-4626-98f0-6333436879e7'></a>

Since $\langle G_p \rangle = G_{p,ss}$ and $\langle A \rangle = A_{ss} = \frac{k}{k_2}$, dividing by $k_2$ and $T$ gives

$\langle A G_p \rangle = A_{ss} \cdot G_{p,ss}$.

<a id='fd0e7d6e-8b8a-4144-8e72-85dee7a80f09'></a>

Thus, the average of the bilinear term, which can be interpreted as the input to biomass, is indeed unaffected by oscillations, although the ammonia and peripheral glutamate levels oscillate asynchronously. For two-dimensional Lotka-Volterra systems, this property was shown earlier [24].

<a id='cf150be1-bebe-478a-a025-d245c3001132'></a>

### 3.4. Bifurcations
Figure 5 shows the two bifurcations: the transcritical bifurcation occurring at G_E = 5.88 mmol l⁻¹ and the Hopf bifurcation at G_E = 24.41 mmol l⁻¹, i.e. the transition from stable steady state to stable limit cycle.

<a id='68352c53-c98d-48a3-878b-7a47db5e101b'></a>

7

<a id='3ebce4fd-7036-4b01-86d4-9087c25870db'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='a04f12b1-d481-41c7-8667-e8a1411d3e2f'></a>

<::bifurcation plot
: chart
Chart title: bifurcation plot
X-axis: G_E (mmol l⁻¹)
Y-axis: G_p (mmol l⁻¹)
Legend: G_p | G_E (red square)
Description: The plot shows G_p versus G_E. Initially, G_p is low and stable. As G_E increases, a transcritical bifurcation occurs around G_E = 5.88 mmol l⁻¹, followed by a supercritical Hopf bifurcation around G_E = 24.41 mmol l⁻¹, leading to a region of oscillation where the amplitude widens with increasing G_E.
Figure 5. Bifurcation diagram of G_p versus G_E. For parameter values except G_E, see table 1. The transcritical bifurcation occurs at G_E = 5.88 mmol l⁻¹ and the supercritical Hopf bifurcation at G_E = 24.41 mmol l⁻¹. The two arms of the convex hull represent the amplitude of oscillation which widen with increasing value of G_E. It can be seen that the model is sensitive to G_E in terms of oscillation amplitude.::>

<a id='a83df96b-7d03-4b7f-ad01-ee15b8209f88'></a>

These values can also be calculated from the general formulae for the bifurcations [19]. The steady-state value of Gp is a linear function of the bifurcation parameter GE, as shown in equation (3.2a). It can be seen that the Hopf bifurcation is supercritical; that is, the amplitude grows gradually starting from zero and the limit cycle is stable right from the beginning.

<a id='b84502d4-d665-43ba-9437-04b3d16649e3'></a>

Near the Hopf bifurcation, the obtained time course curve (figure 2) is sinusoidal. For GE> 24.41 mmol l⁻¹ the oscillations get spike-like and are no longer sinusoidal. It is of interest to speculate about the physiological advantage of spike-like oscillations. This question has been discussed earlier in the context of calcium oscillations [26,38,39]. Whenever the kinetic effect of the oscillating variable (e.g. in activating a protein or in a biochemical conversion) is nonlinear and follows a convex function, the spikes contribute more than proportionately to the effect. Thus, spike-like oscillations can lead to a high average effect even at low average value of the variable. In order that oscillations really enable division of labour in the case of biofilms, it can be expected that they should not be sinusoidal. This deserves further studies. A biological explanation of the bifurcations is given in the Discussion.

<a id='2a30eeb3-a1c7-4204-9000-ccda5225d2f4'></a>

We checked the parameter sensitivity in two ways. First, we performed a bifurcation analysis for all parameters (except k₁ since it is equivalent to G_E), see figures 5 and 6 and electronic supplementary material, figures S1–S3. We see a steep increase in the oscillation amplitude with respect to G_E and k₃, a moderately steep increase for k₄, whereas the other parameters show a very gradual increase in the vicinity of the bifurcation. Second, we applied local parameter sensitivity analysis to the steady-state concentrations, which are equal to the average values. This can be done in an analytical way by differentiating the steady-state values given in equation (3.2) consecutively with respect to all parameters. The resulting unscaled sensitivities for the parameter values from table 1 are given in electronic supplementary material, table S1a. Thereafter, we computed the scaled sensitivities by multiplying by the parameter and dividing by the concentration (electronic supplementary material, table S1b). The obtained values for all sensitivities were confirmed by numerical computation using COPASI [40].

<a id='637d2576-c71d-4af6-9ef9-137437e8c306'></a>

The results show that A is not sensitive at all to k3 and k5, nor is Gp to k5. This is counterintuitive because increasing k5 corresponds to over-expression of glutamate dehydrogenase, which produces ammonia. However, in our model, increasing k5 leads to a decrease in Gi, so that the term k5Gi stays constant. It deserves further study whether a more realistic kinetics leads to non-zero sensitivity for these cases.

<a id='7b46e7a3-5484-489e-a923-9749c845f7ad'></a>

Scaled sensitivities are equal to unity if the parameter enters the formula for the steady value in a multiplicative way (that is, as a factor in the numerator) and equal to minus unity if it is a factor in the denominator. Examples are provided by the scaled sensitivities of G_i and G_p with respect to k_3 and of all concentrations with respect to k_2, respectively. The highest scaled sensitivity, 1.24, is found

<a id='63bf8b91-ed27-40bc-9f1f-566ce9ad6316'></a>

8

<a id='a2aa85fd-d614-4b50-ae41-640ecaef0eb6'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='8a78989c-2e63-4317-8478-faafebbd90fc'></a>

<::bifurcation plot: chart
Legend: Gp | k₅
Y-axis: Gp (mmol l⁻¹)
X-axis: k₅ (h⁻¹)
Description: A bifurcation plot showing Gp as a function of k₅. The plot starts with a single value of Gp for k₅ around 0.5, then widens into a range of values, suggesting chaotic or oscillatory behavior, before narrowing back to a single value around k₅ = 4.3, and then continuing as a single line for k₅ up to 5.0.
: chart::>

<a id='fe4d06ef-f356-491c-9ddf-0fc48c48d52f'></a>

Figure 6. Bifurcation diagram of Gp versus k5. For parameter values, see table 1, except for k5, which is varied between 1 and 4.6 h⁻¹. It can be seen that the model is less sensitive to k5 in terms of oscillation amplitude when compared with GE.

<a id='061bf418-93bb-4ca3-83f8-dd8660c114ab'></a>

for all concentrations with respect to k₁. That value means that a 1% increase in a parameter value leads to a 1.24% increase in the concentration.

<a id='1d1ad2c6-0449-4a07-9ce5-bfbbffd07aab'></a>

## 3.5. Quasi-steady-state approximation

To ascertain the cause of oscillations, which could be a negative feedback with a delay or a positive feedback, we can study a subsystem by eliminating a variable. This can be done by the quasi-steady-state approximation (QSSA) [15]. In our system, we see that Gp exerts a positive feedback on itself which is linear and, thus, quite weak. For example, in the Higgins-Selkov oscillator involving two variables, the feedback is quadratic [16,17]. Moreover, the above system involves a negative feedback: Gp is converted to Gᵢ, Gᵢ is converted to A and A promotes the degradation of Gp (figure 1). In the Goodwin oscillator, which also consists of three variables, a negative feedback is the cause of oscillation [41,42].

<a id='b81a5db9-ec2a-470f-91e3-7bcbf3c18182'></a>

Inspired by the observation in figure 5 that the oscillations vanish at high k5 values, we apply the QSSA for G₁. This corresponds to the special case where glutamate dehydrogenase is overexpressed. In that case, indeed quenching of oscillations was observed in experiment and also predicted by the Liu model [4]. The variable G₁ then attains a quasi-steady state

<a id='75933854-b7cc-4c89-b486-a8142e3875af'></a>

This leads to

dGi
-- = k4Gp - k5Gi = 0.
dt

(3.4)

<a id='05cf7feb-2d01-4024-ae17-bbc46e7ef2b8'></a>

G_i = \frac{k_4}{k_5} G_p.                                                                                                (3.5)

<a id='4b4b43f2-567c-4618-86e7-93143cce1a8b'></a>

Substituting this into the above model equations (2.1a-c) yields a simplified system

<a id='6d6cd8db-1401-498f-a468-45d24b6a8f92'></a>

$$\frac{dG_p}{dt} = (k_1G_E - k_4)G_p - k_2G_pA \quad (3.6a)$$

<a id='8e230673-89fa-4c45-8b35-f26c94bcea1b'></a>

$\frac{dA}{dt} = -k_3A + k_4G_p$.                                                                       (3.6b)

<a id='df475df9-bd05-4c1d-88e2-2261202105f8'></a>

It is of interest to analyse its dynamics. It follows from the general result by Hanusse [43,44] that it cannot give rise to a limit cycle because it involves two variables and only linear and bilinear terms. However, the question still remains whether it gives rise to a stable or unstable steady state, whether damped oscillations are possible, etc.

<a id='ce939cf6-417d-4c6d-8fd3-38ba208e5bde'></a>

9

<a id='5f7c84af-f98e-4086-ac5f-5b8b3683fa85'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<a id='ea9c580c-38b4-4280-b72b-aad19c7209fb'></a>

and

<!-- PAGE BREAK -->

<a id='737b1294-4267-4233-a20c-a544762d9769'></a>

System (3.6) shows two steady states

<a id='0bcf965a-d868-4338-bb06-55d1e8041215'></a>

Gp1 = A1 = 0,                                                                  (3.7a,b)

<a id='75b8d031-e79b-43e0-8c36-6aa76f27a343'></a>

which is the TSS, and

<a id='903d2978-afee-431f-a744-9af72113aef9'></a>

Gp2 = k1GE - k4 / k2k4 k3, A2 = k1GE - k4 / k2
(3.8a,b)

<a id='e57c48f0-d241-4c73-b9d8-676a681d74af'></a>

which is the NTSS (see equations (3.2a,b)). The Jacobian matrix reads
M = $\begin{pmatrix} k_1G_E - k_4 - k_2A & -k_2G_p \ k_4 & -k_3 \ \end{pmatrix}$
(3.9)

<a id='c5f3e588-2837-4236-8296-e125eeb65e99'></a>

while for the TSS, it reads

M = $\begin{pmatrix} k_1 G_E - k_4 & 0 \\ k_4 & -k_3 \end{pmatrix}$ (3.10)

<a id='7301eb13-9abd-46ec-97f7-fa0ef27b59be'></a>

For matrices with such a triangular structure, the eigenvalues are given by the diagonal elements. In our case

$\lambda_1 = k_1 G_E - k_4$, $\lambda_2 = -k_3$. (3.11)

<a id='9e02ab50-b59a-467a-a314-7ae433d51456'></a>

In any case, the eigenvalues are real, so that not even damped oscillations are possible. For $k_1 G_E < k_4$, both eigenvalues are negative, so that the TSS is a stable node. For $k_1 G_E > k_4$, one eigenvalue is negative and the other one positive. The steady state then is unstable, it is a saddle point.
For the NTSS (3.8), the Jacobian matrix becomes

<a id='90608704-055a-47fd-914f-c22f603821d6'></a>

M = \begin{pmatrix} 0 & -\frac{k_1 G_E - k_4}{k_4} k_3 \\ k_4 & -k_3 \end{pmatrix}.

(3.12)

<a id='1341d7f3-759b-49d2-8f70-4beaaeb82ae8'></a>

The characteristic equation reads

λ² + k₃λ + (k₁G_E - k₄)k₃ = 0. (3.13)

<a id='c16f13b3-4ffb-45fc-870e-26e30f34b646'></a>

This has the solutions

$\lambda_{1/2} = -\frac{k_3}{2} \pm \sqrt{\frac{k_3^2}{4} - (k_1 G_E - k_4)k_3}$ (3.14)

<a id='0e0f4d0d-7abd-4d29-b762-a670c3abb6db'></a>

Now, we distinguish three cases:

(a) For k₁GE < k₄, the term under the square root is positive, so that the root is real. Moreover, it is larger than k₃/2. Thus, one eigenvalue is negative and the other one positive. The steady state then is unstable, it is a saddle point.
(b) For 0 < k₁GE − k₄ < k₃/4, the root is again real. It is less than k₅/2, though. Both eigenvalues are negative; the steady state is a stable node.
(c) For k₁GE − k₄ > k₃/4, the root is imaginary. Both eigenvalues are complex numbers, with the same negative real part −k₃/2. The steady state is a stable focus. This state is, thus, reached by damped oscillations.

<a id='0799d669-55a9-40e7-b398-1de4a197d64f'></a>

From these calculations, the following conclusions can be drawn. At k₁Gₑ = k₄, the two steady states of the simplified system (3.6) coincide, as in the complete system (2.1). Since the TSS and NTSS interchange their stability at that point, it is a transcritical bifurcation.

<a id='6ecacb56-c0c4-4174-9ef1-51a05b088df9'></a>

There is a second transition point where the qualitative behaviour changes, at k₁GE -k₄=k₃/4. This is another point than the Hopf bifurcation in the complete system, which is at k₁GE-k₄=k₃+k₅. At this transition in the simplified system, a stable node turns into a stable focus. Such a transition must also occur in the complete system between the transcritical bifurcation, where an unstable node turns into a stable node, and the Hopf bifurcation, where a stable focus gets unstable. It is difficult to find it exactly in the three-dimensional system. Beyond this transition, the simplified system shows damped oscillations. This implies that the positive feedback of Gp on itself can be considered as a cause of oscillation, yet not as a cause of a limit cycle. The 'inflation' of the oscillation to a limit cycle in the

<a id='bdd3602c-78e6-4f3a-be72-b120adac2ab4'></a>

10

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='7f4bb710-453e-4f16-b23c-ff53f98ab012'></a>

complete system appears to be brought about by the negative feedback via G₁. The loop via G₁ can,
moreover, be interpreted as a delay.

<a id='e71051a3-179a-4d47-9401-e2dfed48d00d'></a>

In this subsection, we have considered the special case of high k5. This corresponds to a situation realized in experiments by Liu et al. where they overexpress the glutamate dehydrogenase leading to an excessive production of ammonia [4]. In that situation, indeed no oscillations were observed. We have proved analytically that the limit cycle disappears in that case. This generalizes the numerical finding shown in figure 6. Thus, to model limit cycle oscillations in biofilms by equation (2.1), we need the full three-dimensional system with values of k5 that are not too high.

<a id='6a6ae5f9-ca4e-4949-bd42-922b725bd1fa'></a>

The QSSA for the rate constant k3 is given in the electronic supplementary material.

<a id='c7bce00b-c84f-4f3a-88c9-b1ff40ae1764'></a>

## 4. Discussion

Here, we have used the smallest chemical system showing a Hopf bifurcation to model metabolic oscillations in _B. subtilis_ biofilms. That model had been used earlier to describe p53 oscillations [22]. Here, we have applied the model to describe another biological phenomenon. We have specifically selected the parameter values to describe biofilm dynamics, which makes the model more relevant in the light of the biological observation. In our system, the diffusion of ammonia is critical for biofilm oscillations. All the terms in the model are linear, except k₂AGp, which is bilinear. The model describes metabolic and diffusion processes as outlined above. As an output, the growth of the biofilm (consisting of incremental and halting phases) was also computed (figure 4).

<a id='c071c413-3410-4a74-9221-a2aa6cd27ac4'></a>

A major reason of the observed oscillations was demonstrated to be the division of labour between the central and peripheral zones of the biofilm. While the release of usable ammonia is mainly delimited to the former, the production of biomass and, thus, growth, is mainly delimited to the latter.

<a id='32dd0547-3e30-4bc2-bc2f-a267d2124715'></a>

We have presented bifurcation diagrams, which clearly show supercritical Hopf bifurcations (figure 5 and 6, electronic supplementary material, figures S1-S3). Earlier, Wilhelm & Heinrich [19,20] had analysed that bifurcation and had presented one bifurcation diagram. Here, we have added some mathematical analysis. For example, we show the maxima and minima of oscillations, the knowledge of which gives us a quantitative insight into the biofilm dynamics. Moreover, we performed a QSSA and probed for the equality property of the average values. We analysed the Hopf bifurcation by changing not only the external glutamate G_E but alternatively also all the rate constants except k_1, since changing k_1 has the same effect as changing G_E. Interestingly, a recent model [7] has shown a subcritical bifurcation in describing the behaviour of the stress levels in the biofilm periphery. However, they modelled the stress with a single delay differential equation and did not consider other molecular details, while we do not consider stress. Using a single differential equation meets the quest for minimality. However, a delay differential equation (meaning that the time derivative of a variable depends on that variable at a previous time point) is, from a mathematical point of view, very complex because it requires infinitely many initial values (from zero to the delay period, with a simplifying assumption being that they are all equal). Moreover, stability analysis is then considerably more complicated. Our model is complementary to their model. It is closer to Liu's original model [4] but much simpler because it involves only three rather than six variables, and thus only requires three initial values. We chose the parameters of the model such that they are in agreement with Liu's experimental results, namely the period and the amplitude of oscillations.

<a id='10a0ba1c-9840-453e-b169-00c840ae59b5'></a>

In our model, peripheral glutamate exerts a positive feedback on itself. Mathematically, this has the form of a bilinear term involving peripheral and external glutamate concentrations. At very low values of _G_<sub>_E_</sub>, the feedback is not strong enough to enable a positive steady state. The system then tends to the TSS. In that state, _G_<sub>_p_</sub> is zero, so that growth is impossible. Biologically, this can be interpreted that the biofilm is too small to be viable. This is in agreement with observations in the recent study from the Suel group [7]. At a certain threshold value of _G_<sub>_E_</sub> (5.88 mmol l<sup>−1</sup>), the NTSS turns stable in a transcritical bifurcation. Beyond that value, the feedback is strong enough to enable growth. At high values of _G_<sub>_E_</sub>, the feedback becomes so strong that an overshoot occurs: more glutamate is taken up than needed, so that the _G_<sub>_p_</sub> level transiently exceeds the steady-state value. Then, more peripheral glutamate is consumed for release of ammonia or for growth, so that the concentration decreases again. This leads to oscillations.

<a id='f30662dd-dc7b-4cf5-91d5-d5289e5a3496'></a>

From a functional point of view, a steady state is quite appropriate [29]. Growth of the biofilm does not require oscillations. However, in this system, oscillations help in mitigating the chemical attack that challenges the biofilm [4]. This may have interesting clinical implications in view of treatment of biofilm-forming bacteria by antibiotics. Furthermore, another study [9] indicates that oscillations in growth

<a id='e0b842f7-8625-4f08-9c69-12001e7f0757'></a>

11

<a id='51e4fc55-f5cd-49c3-86af-0ac9849bf826'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='8edcae45-475c-4f23-9050-0db4b5d09b0e'></a>

actually help in sharing the nutrients among several biofilms more efficiently. However, not all biofilms show oscillations, indicating that it is not critical for biofilms. Our numerical calculations suggest that the average growth rate is lower when compared with growth at the metabolic steady state.

<a id='37c6e1d3-894a-411f-8772-18497f4e245c'></a>

By contrast, the individual concentration variables (ammonia, peripheral glutamate etc. but not biomass) show the equality property that their average during oscillations equals the value at the unstable state, as usual for Lotka-Volterra systems [25]. Here, we have shown that the bilinear input term k₂AGₚ exhibits this equality property as well. This may come as a surprise because the ammonia and peripheral glutamate levels oscillate with a phase shift.

<a id='b127b5b5-828c-4c93-a74f-f9367a090fcc'></a>

In the paper by Liu _et al._ [4], the oscillations computed by their model have a sinusoidal shape. In our model, such a shape only occurs in the neighbourhood of the Hopf bifurcation. Further beyond it, the shape is more spike-like with the crests being sharper than the troughs.

<a id='3883f1e5-4424-4ac2-aed2-216b47dd06aa'></a>

The question arises whether the model used and analysed here is minimal. On the basis of ODE systems (without delays), at least two variables are needed to generate oscillations [13,14]. However, when only linear and bilinear terms are included, at least three variables are needed, as was proved by Hanusse by an analysis of the Jacobian matrix [43,44]. As shown by Wilhelm & Heinrich [19], such a model requires at least five reactions. Thus, the above model is minimal in terms of the number of variables (criterion with highest priority) and number of reactions, given the type of kinetics. The famous two-variable Brusselator model [45] and the Higgins-Selkov oscillator involve a term of degree three each [16,17]. If the number of reactions is granted the highest priority, the model may look different. Thus, it depends on the criteria what a minimal model is. Note that a delay differential equation [7] is, from the viewpoint of the number of initial values, of infinite dimension. While our model is not necessarily the simplest, it provides a trade-off between simplicity and adequacy to match the observed oscillation in biofilms.

<a id='fc02e3f4-8b1c-454d-9ef1-e704a10c6bfd'></a>

As for any oscillatory system, it is interesting to elucidate the feedback structure. The term k₁GEGₒ represents a positive feedback because peripheral glutamate stimulates its own uptake. This is because glutamate is a proxy for the concentration of various transport proteins embedded in the cell membranes. The higher the concentration of these proteins, the higher is the glutamate uptake rate. Since this positive feedback is the driving force for oscillations, at low values of k₁GE, we observe a steady state rather than oscillations. In glycolytic and calcium oscillations, the cause of oscillations is also a positive feedback [13,14,17,46], while in a Goodwin oscillator, it is a negative feedback [41,42].

<a id='6ba8a4d7-3212-42a4-b1ea-4b2e855e8203'></a>

In addition to the positive feedback, there is also a negative feedback loop in the system (figure 1). As seen from the differential equations, peripheral glutamate positively influences internal glutamate, which positively affects ammonia, which then negatively influences peripheral glutamate. Thus, the overall effect is inhibitory. This feedback structure of the Wilhelm-Heinrich model has been highlighted earlier [22].

<a id='58053b15-a664-47d8-8e07-2e2afafd6851'></a>

By applying the QSSA, we have proved analytically that the limit cycle disappears if glutamate is degraded very fast or ammonia diffuses very easily. As mentioned in the Results section, the former case corresponds to a situation realized in experiments by overexpressing the glutamate dehydrogenase [4]. In that situation, no oscillations were observed. By contrast, in the case where oscillations occur, a description by a simple mass-action system requires three variables. Analyses in this direction may be relevant for clinical interventions via inhibition or activation of bacterial enzymes or changing diffusivity in the biofilm.

<a id='e4040ffd-3a17-4efc-9e1d-eb38a93ecf9a'></a>

The model analysed here has several pros and cons. In view of the mathematical analysis, its simplicity is certainly an advantage. In view of an adequate description of the biological and biochemical processes involved, the model may appear oversimplified. For example, describing growth by trilinear term is quite simplistic; usually, it is described by saturation kinetics (e.g. Michaelis-Menten kinetics). In addition, the assumption that glutamate uptake by the periphery is proportional to the glutamate concentration as explained above could be refined in future studies. Moreover, diffusion processes are usually reversible. In the above model, we neglected the backward processes in diffusion, which is justified if concentration differences are high.

<a id='f83f8ebf-fbb7-4122-867a-45b27037010a'></a>

Many theoretical and experimental studies have been published on glycolytic oscillations [13,16,17,47,48]. However, these oscillations only occur under very special or even artificial conditions. In living cells, metabolic oscillations are rare, while being quite frequent in signalling systems [13,14,49,50]. The lights of a car are a helpful analogy: the headlights illuminate the street in a permanent way; there is no point in oscillations. By contrast, the side indicators (as signalling device) flash; that is, they emit oscillating light. Interestingly, in the case of biofilms, metabolic oscillations could provide advantages. While the work described here is quite theoretical, we consider it to be an appropriate basis for refined and more sophisticated models of biofilm oscillations.

<a id='ac60563b-94fd-464e-85ce-08a99bb6b634'></a>

12

<a id='9002f270-2f88-437b-bb98-1a326999611e'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='bc2f68d7-b9b8-4989-984c-05cea1b3fb7f'></a>

Data accessibility. No custom code and datasets was used within this study.
Authors' contributions. S.S. conceived the idea of applying the Wilhelm and Heinrich model to the biofilm system. R.G. performed modelling and simulation using COPASI. He and Á.T.K. interpreted the model variables, parameters and results biologically. B.I. verified the results using Matlab and also produced figures and mathematical analyses. S.S. performed QSSA and mathematical proof and mathematical interpretation of the results. R.G. and S.S. wrote the manuscript and B.I. and Á.T.K. edited and structured it. All the authors have read and approved the manuscript.
Competing interests. The authors declare no competing financial interests.
Funding. R.G. was supported by the Max Planck Society through the IMPRS 'Exploration of Ecological Interactions with Molecular and Chemical Techniques'. B.I. was supported by the DFG through the Collaborative Research Center 1127, ChemBioSys Project C07.

<a id='e1405ecd-6df8-4d7e-9f71-b47900c011bb'></a>

Acknowledgements. We acknowledge David Heckel for his valuable inputs in interpreting the biological implications of the results and Frank Hilker for drawing our attention to the paper by Goel et al. [24].

<a id='c8d1ec81-1a6e-46fe-850a-5e5ac7ab84f8'></a>

References

1. Kovacs AT, Dragos A. 2019 Evolved biofilm: review on the experimental evolution studies of _Bacillus subtilis_ pellicles. _J. Mol. Biol._ **431**, 4749–4759. (doi:10.1016/j.jmb.2019.02.005)
2. Kreft JU. 2004 Biofilms promote altruism. _Microbiology_ **150**, 2751–2760. (doi:10.1099/mic.0.26829-0)
3. Popat R, Crusz SA, Messina M, Williams P, West SA, Diggle SP. 2012 Quorum-sensing and cheating in bacterial biofilms. _Proc. R. Soc. B_ **279**, 4765–4771. (doi:10.1098/rspb.2012.1976)
4. Liu J, Prindle A, Humphries J, Gabalda-Sagarra M, Asally M, Lee DY, Ly S, Garcia-Ojalvo J, Suel GM. 2015 Metabolic co-dependence gives rise to collective oscillations within biofilms. _Nature_ **523**, 550–554. (doi:10.1038/nature14660)
5. Dragos A et al. 2018 Division of labor during biofilm matrix production. _Curr. Biol._ **28**, 1903–1913.e5. (doi:10.1016/j.cub.2018.04.046)
6. Stannek L, Thiele MJ, Ischebeck T, Gunka K, Hammer E, Volker U, Commichau FM. 2015 Evidence for synergistic control of glutamate biosynthesis by glutamate dehydrogenases and glutamate in _Bacillus subtilis_. _Environ. Microbiol._ **17**, 3379–3390. (doi:10.1111/1462-2920.12813)
7. Martinez-Corral R, Liu J, Suel GM, Garcia-Ojalvo J. 2018 Bistable emergence of oscillations in growing _Bacillus subtilis_ biofilms. _Proc. Natl Acad. Sci. USA_ **115**, E8333–E8340. (doi:10.1073/pnas.1805004115)
8. Horn H, Lackner S. 2014 Modeling of biofilm systems: a review. _Adv. Biochem. Eng. Biotechnol._ **146**, 53–76. (doi:10.1007/10_2014_275)
9. Liu J, Martinez-Corral R, Prindle A, Lee DD, Larkin J, Gabalda-Sagarra M, Garcia-Ojalvo J, Suel GM. 2017 Coupling between distant biofilms and emergence of nutrient time-sharing. _Science_ **356**, 638–642. (doi:10.1126/science.aah4204)
10. Skoneczny S. 2015 Cellular automata-based modelling and simulation of biofilm structure on multi-core computers. _Water Sci. Technol._ **72**, 2071–2081. (doi:10.2166/wst.2015.426)
11. Miller JK et al. 2014 Mathematical modelling of _Pseudomonas aeruginosa_ biofilm growth and treatment in the cystic fibrosis lung. _Math. Med. Biol._ **31**, 179–204. (doi:10.1093/imammb/dqt003)
12. Rotrattanadumrong R, Endres RG. 2017 Emergence of cooperativity in a model biofilm.

<a id='532f0f43-0442-4bb3-9d68-d873c99a4d8f'></a>

J. Phys. D: Appl. Phys. **50**, 234006. (doi:10.1088/
1361-6463/aa7097)

13. Goldbeter A, Berridge MJ. 1996 *Frontmatter. In
Biochemical oscillations and cellular rhythms: the
molecular bases of periodic and chaotic behaviour*, pp.
i–viii. Cambridge, UK: Cambridge University Press.

14. Schuster S, Marhl M, Hofer T. 2002 Modelling of
simple and complex calcium oscillations: from
single-cell responses to intercellular signalling.
*Eur. J. Biochem.* **269**, 1333–1355. (doi:10.1046/
j.0014-2956.2001.02720.x)

15. Heinrich R, Schuster S. 1996 *The regulation of
cellular systems*. New York, NY: Chapman and Hall.

16. Higgins J. 1967 The theory of oscillating
reactions—kinetics symposium. *Ind. Eng. Chem.*
**59**, 18–62. (doi:10.1021/ie50689a006)

17. Sel'kov EE. 1968 Self-oscillations in glycolysis. 1. A
simple kinetic model. *Eur. J. Biochem.* **4**, 79–86.
(doi:10.1111/j.1432-1033.1968.tb00175.x)

18. Somogyi R, Stucki JW. 1991 Hormone-induced
calcium oscillations in liver cells can be
explained by a simple one pool model. *J. Biol.*
*Chem.* **266**, 11 068–11 077.

19. Wilhelm T, Heinrich R. 1995 Smallest chemical-
reaction system with Hopf-bifurcation. *J. Math.*
*Chem.* **17**, 1–14. (doi:10.1007/Bf01165134)

20. Wilhelm T, Heinrich R. 1996 Mathematical
analysis of the smallest chemical reaction
system with Hopf bifurcation. *J. Math. Chem.*
**19**, 111–130. (doi:10.1007/Bf01165179)

21. Wilhelm T, Schuster S, Heinrich R. 1997 Kinetic and
thermodynamic analyses of the reversible version
of the smallest chemical reaction system with Hopf
bifurcation. *Nonlinear World.* **4**, 295–321.

22. Geva-Zatorsky N *et al.* 2006 Oscillations and
variability in the p53 system. *Mol. Syst. Biol.* **2**,
2006 0033. (doi:10.1038/msb4100068)

23. Strogatz SH. 2018 *Nonlinear dynamics and chaos:
with applications to physics, biology, chemistry,
and engineering*. Boca Raton, FL: CRC Press.

24. Goel NS, Maitra SC, Montroll EW. 1971 On the
Volterra and other nonlinear models of
interacting populations. *Rev. Mod. Phys.* **43**,
231–276. (doi:10.1103/RevModPhys.43.231)

25. Hofbauer J, Sigmund K. 1998 *Evolutionary
games and population dynamics*. Cambridge,
UK: Cambridge University Press.

26. Knoke B, Bodenstein C, Marhl M, Perc M,
Schuster S. 2010 Jensen's inequality as a tool
for explaining the effect of oscillations on the

<a id='0258fc7a-dbf4-4815-bf3a-43db0dda1519'></a>

average cytosolic calcium concentration. Theory
Biosci. **129**, 25–38. (doi:10.1007/s12064-010-
0080-1)

27. Knoke B, Marhl M, Perc M, Schuster S. 2008
Equality of average and steady-state levels in
some nonlinear models of biological oscillations.
Theory Biosci. **127**, 1–14. (doi:10.1007/s12064-
007-0018-4)

28. Ritter AB, Douglas JM. 1970 Frequency response
of nonlinear systems. Ind. Eng. Chem. **9**, 21–28.

29. Reimers AM, Reimers AC. 2016 The steady-state
assumption in oscillating and growing systems.
J. Theor. Biol. **406**, 176–186. (doi:10.1016/j.jtbi.
2016.06.031)

30. Dupont G. 1993 Modélisation des oscillations et
des ondes de calcium intracellulaire. Bruxelles,
Belgium: Université Libre de Bruxelles.

31. Hoops S et al. 2006 COPASI—a Complex
PAthway Simulator. Bioinformatics **22**,
3067–3074. (doi:10.1093/bioinformatics/btl485)

32. Cussler EL. 2009 Diffusion: mass transfer in fluid
systems, 2nd edn. Cambridge, UK: Cambridge
University Press.

33. Kullmann DM, Min MY, Asztely F, Rusakov DA.
1999 Extracellular glutamate diffusion
determines the occupancy of glutamate
receptors at CA1 synapses in the hippocampus.
Phil. Trans. R. Soc. Lond. B **354**, 395–402.
(doi:10.1098/rstb.1999.0392)

34. Ribeiro ACF, Rodrigo MM, Barros MCF, Verissimo
LMP, Romero C, Valente AJM, Esteso MA. 2014
Mutual diffusion coefficients of L-glutamic acid
and monosodium L-glutamate in aqueous
solutions at T = 298.15 K. J. Chem. Thermodyn.
**74**, 133–137. (doi:10.1016/j.jct.2014.01.017)

35. Strogatz S. 2000 Nonlinear dynamics and chaos:
with applications to physics, biology, chemistry,
and engineering. Cambridge, MA: Perseus Pub.

36. Burdett ID, Kirkwood TB, Whalley JB. 1986
Growth kinetics of individual Bacillus subtilis
cells and correlation with nucleoid extension.
J. Bacteriol. **167**, 219–230. (doi:10.1128/jb.167.
1.219-230.1986)

37. Maass S et al. 2011 Efficient, global-scale
quantification of absolute protein amounts by
integration of targeted mass spectrometry and
two-dimensional gel-based proteomics. Anal.
Chem. **83**, 2677–2684. (doi:10.1021/ac1031836)

38. Salazar C, Politi AZ, Hofer T. 2008 Decoding of
calcium oscillations by phosphorylation cycles:

<a id='6f990628-4fee-4d8e-bdfc-7632c53f5036'></a>

13

<a id='f0d211be-e9cb-412c-90a9-85221454f14a'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

<!-- PAGE BREAK -->

<a id='82e7e0e2-c008-4363-8306-dd6469cb1eba'></a>

analytic results. *Biophys. J.* **94**, 1203–1215. (doi:10.1529/biophysj.107.113084)
39. Bodenstein C, Knoke B, Marhl M, Perc M, Schuster S. 2010 Using Jensen's inequality to explain the role of regular calcium oscillations in protein activation. *Phys. Biol.* **7**, 036009. (doi:10.1088/1478-3975/7/3/036009)
40. Kent E, Neumann S, Kummer U, Mendes P. 2013 What can we learn from global sensitivity analysis of biochemical systems? *PLoS ONE* **8**, e79244. (doi:10.1371/journal.pone.0079244)
41. Goodwin BC. 1965 Oscillatory behavior in enzymatic control processes. *Adv. Enzyme Regul.* **3**, 425–438. (doi:10.1016/0065-2571(65)90067-1)
42. Heiland I, Bodenstein C, Hinze T, Weisheit O, Ebenhoeh O, Mittag M, Schuster S. 2012 Modeling temperature entrainment of circadian clocks using the Arrhenius equation and a reconstructed model from *Chlamydomonas*

<a id='f4da914e-1d70-4b7c-b7d8-58550759299b'></a>

reinhardtii. _J. Biol. Phys._ **38**, 449–464. (doi:10. 1007/s10867-012-9264-x)

43. Hanusse P. 1973 Étude des systèmes dissipatifs chimiques à deux et trois espèces intermédiaires. _C. R. Acad. Sci. Paris C_ **277**, 263–266.

44. Hanusse P. 1972 De l'Existence d'un Cycle Limite dans l'Evolution des Systèmes Chimiques Ouverts. _C. R. Acad. Sci. Paris, C_ **274**, 1245–1247.

45. Prigogine I, Lefever R. 1968 Symmetry breaking instabilities in dissipative systems. II. _J. Chem. Phys._ **48**, 1695–1700. (doi:10.1063/1.1668896)

46. Kummer U, Olsen LF, Dixon CJ, Green AK, Bornberg-Bauer E, Baier G. 2000 Switching from simple to complex oscillations in calcium signaling. _Biophys. J._ **79**, 1188–1195. (doi:10. 1016/S0006-3495(00)76373-9)

47. du Preez FB, van Niekerk DD, Kooi B, Rohwer JM, Snoep JL. 2012 From steady-state to

<a id='06097edd-3141-4650-8624-3121c4e3b885'></a>

synchronized yeast glycolytic oscillations
I: model construction. *FEBS J.* **279**,
2810–2822. (doi:10.1111/j.1742-4658.2012.
08665.x)

48. du Preez FB, van Niekerk DD, Snoep JL. 2012
From steady-state to synchronized yeast
glycolytic oscillations II: model validation. *FEBS
J.* **279**, 2823–2836. (doi:10.1111/j.1742-4658.
2012.08658.x)

49. Goldbeter A, Dupont G, Berridge MJ. 1990
Minimal model for signal-induced Ca²⁺
oscillations and for their frequency encoding
through protein phosphorylation. *Proc. Natl
Acad. Sci. USA* **87**, 1461–1465. (doi:10.1073/
pnas.87.4.1461)

50. Ewald J, Sieber P, Garde R, Lang SN, Schuster S,
Ibrahim B. 2019 Trends in mathematical
modeling of host–pathogen interactions. *Cell.
Mol. Life Sci.* (doi:10.1007/s00018-019-03382-0)

<a id='e3578c69-d66d-4269-a8b6-b2ad2af6da1a'></a>

14

<a id='a8b6b80c-0272-49f9-92e7-a92909805ff0'></a>

royalsocietypublishing.org/journal/rsos R. Soc. open sci. 7: 190810

# Supplementary materials

<a id='acb3eea5-e62f-41ea-90de-5f5981b936ac'></a>

SUPPLEMENT TO

<a id='30caebc3-737c-4fc6-bb36-d8bb6454fe63'></a>

Differential equation based minimal model describing metabolic oscillations in *Bacillus subtilis* biofilms

<a id='ff80a8b0-bbf2-47af-903f-d7e450359373'></a>

Ravindra Garde 1,2, Bashar Ibrahim 1,4,5, Ákos T. Kovács³, Stefan Schuster¹*

¹Dept. of Bioinformatics, Matthias Schleiden Institute, Friedrich Schiller University Jena,
Ernst-Abbe-Platz 2, 07743 Jena, Germany

²Max Planck Institute for Chemical Ecology Hans-Knöll-Str. 8, 07745, Jena, Germany

³Bacterial Interactions and Evolution Group, DTU Bioengineering, Technical University of
Denmark, Søltofts Plads Building 221, 2800 Kgs. Lyngby, Denmark

⁴Centre for Applied Mathematics and Bioinformatics, Gulf University for Science and
Technology, Hawally 32093, Kuwait

⁵Department of Mathematics and Natural Sciences, Gulf University for Science and
Technology, Hawally 32093, Kuwait

<a id='cace68a6-19aa-4201-a89d-f20324226887'></a>

*Corresponding Author

<!-- PAGE BREAK -->

<a id='1ded13d9-e924-4864-abd1-28b1eb22c5c8'></a>

Applying the quasi-steady-state approximation to ammonia

Just as in the case of the QSSA variable G, (see main text for details), we apply the same approximation to the variable A.

<a id='9fd11671-fe12-4cd8-9216-9eb36144c893'></a>

A = k_5 / k_3 G_i (S1)

<a id='e67b3e77-bb55-4b1b-85f7-cdeb6cc4e818'></a>

From Eq. (1), we derive a reduced system:

$\frac{dG_p}{dt} = k_1 G_E G_p - k_4 G_p - \frac{k_2 k_5}{k_3} G_p$ (S2)

<a id='6be557b1-32d0-453f-a2fd-2ad759cc1377'></a>

dG_i / dt = k_4 G_p - k_5 G_i (S3)

<a id='25f67039-3601-4ff1-9f12-55be128f2d8f'></a>

The system shows two steady states:

Gp1=Gi1=0                                                                     (S4a,b)

<a id='15b4d22b-b174-40fb-b064-f94779e05ffc'></a>

$G_{p2} = \frac{(k_1 G_E - k_4) k_3}{k_2 k_4}$, $G_{i2} = \frac{(k_1 G_E - k_4) k_3}{k_2 k_5}$ (S5a,b)

<a id='019f25b2-0927-4065-8da2-6acdde5afa05'></a>

(see Eqs. (3a,c)). The Jacobian matrix reads:

$M=\begin{pmatrix}
k_1 G_E - k_4 - \frac{k_2 k_5}{k_3} G_i & - \frac{k_2 k_5}{k_3} G_p \\
k_4 & -k_5
\end{pmatrix}$ (S6)

<a id='6bdcf1af-30d7-486b-9018-1faee306a4d0'></a>

For the trivial steady state (TSS, Eq. (S4)), it leads to:

$M = \begin{pmatrix} k_1 G_E - k_4 & 0 \\ k_4 & -k_5 \end{pmatrix}$

(S7)

<a id='96fe5a4e-2b4c-4a6f-b7e8-d595f30ff2c6'></a>

For matrices with such a triangular structure, the eigenvalues are given by the diagonal
elements. In our case:

$\lambda_{1}=k_{1}G_{E}-k_{4},\lambda_{2}=-k_{5}$ (S8)

<!-- PAGE BREAK -->

<a id='8feaf6ab-d17a-4c3e-937d-e076d95c735c'></a>

In any case, the eigenvalues are real, so that not even damped oscillations are possible. For k1GE < k4, both eigenvalues are negative, so that the trivial steady state is a stable node. For k1GE > k4, one eigenvalue is negative and the other one positive. The steady state then is unstable, it is a saddle point.
For the NTSS (Eq. (S5)), the Jacobian matrix becomes:

<a id='6b49a04a-dd1e-42a8-9084-e0b67e3bd441'></a>

M = 
  ( 0  - k_1 G_E - k_4 k_5 / k_4 )
  ( k_4 - k_3 )

(S9)

<a id='645f4330-79d7-41e6-9aef-a7ca6adb15a9'></a>

The characteristic equation reads:

$\lambda^2 + k_3\lambda + (k_1G_E - k_4)k_5 = 0$ (S10)

<a id='c3fbd486-6212-4179-b6fa-92dab3a1d1e7'></a>

This has the solutions

<a id='ed69c529-c65f-44a2-ac31-75bc96e8abae'></a>

\lambda_{1/2} = -\frac{k_3}{2} \pm \sqrt{\frac{k_3^2}{4} - (k_1 G_E - k_4)k_5} (S11)

<a id='983465fd-6118-4a56-823a-a722f4883085'></a>

Now, we distinguish three cases:

a) For k₁G_E < k₄, the term under the square root is positive, so that the root is real.
   Moreover, it is larger than k₃/2. Thus, one eigenvalue is negative and the other one
   positive. The steady state then is unstable, it is a saddle point.

b) For 0 < k₁G_E - k₄ < k₃²/4k₅, the root is again real. It is less than k₃/2, though. Both
   eigenvalues are negative; the steady state is a stable node.

c) For k₁G_E - k₄ > k₃²/4k₅, the root is imaginary. Both eigenvalues are complex numbers,

<a id='bf971744-c2f4-47e9-8f79-5c4ac4081319'></a>

with the same negative real part -k3/2. The steady state is a stable focus. This state is, thus, reached by damped oscillations.

<a id='dda7831f-65a2-4731-8630-539d4e618107'></a>

The transition between stable node and stable focus occurs at k₁G_E - k₄ = k₃²/4k₅. The results

<a id='261cf35e-2af7-4ea5-bc70-730ae890f066'></a>

of this approximation are similar to those in the main text section on QSSA. We can conclude that the limit-cycle oscillations vanish if ammonia diffuses very fast.

<!-- PAGE BREAK -->

<a id='ae984938-da75-49e3-827b-6b98049fd053'></a>

<::Bifurcation Plot: chart::>Bifurcation Plot. The chart displays a scatter plot with red data points. The Y-axis is labeled "[Gp] in mmol/l" and ranges from 0 to 800. The X-axis is labeled "k2 (lh/mmol)" and ranges from 0 to 12. The plot shows a wide spread of [Gp] values for small k2 values (near 0), which then rapidly narrows and decreases as k2 increases, eventually showing a more stable, lower range of [Gp] values for larger k2. A legend at the bottom indicates the data points correspond to "[Gp]|[k2]".

<a id='303629ed-6dd3-44ed-a329-4981179952d6'></a>

Figure S1: Bifurcation plot of Gp versus k2. It can be seen that the model is not very sensitive to k2 in terms of amplitude of oscillations if k2 ≥ 2 h⁻¹.

<!-- PAGE BREAK -->

<a id='a4971fa3-4898-4e69-b96c-cfde1016c6e0'></a>

<::chart: Bifurcation Plot::>Bifurcation Plot. The Y-axis is labeled "[G_p] in mmol/l" and ranges from 0 to 16. The X-axis is labeled "k_3 (h⁻¹)" and ranges from 0 to 8. The plot shows red scattered points. For k_3 values approximately less than 1, there is a single line of points. Between k_3 approximately 1 and 5.5, the points form a dense, wide region, indicating oscillations with varying amplitudes. Above k_3 approximately 5.5, the points narrow down to a single line again. There is a legend entry "[Gp]|k3".Figure S2: Bifurcation plot of G_p versus k_3. The model is sensitive to k_3 if k_3 ≥ 4 h⁻¹ in terms of amplitude of oscillations.<::

<!-- PAGE BREAK -->

<a id='43f35da4-db91-4e29-979f-18a1aa1d4408'></a>

<::Bifurcation Plot. The y-axis is labeled "[G_p] in mmol/l" with values from 0 to 50. The x-axis is labeled "k_4 (h⁻¹)" with values from 0 to 5. The plot shows red data points forming a bifurcation diagram. For k_4 values less than approximately 3.5 h⁻¹, there is a spread of [G_p] values, indicating multiple possible states or oscillatory behavior, with the spread being largest for k_4 values between 1 and 2 h⁻¹. For k_4 values greater than approximately 3.5 h⁻¹, the [G_p] values converge to a single, low value near 0. Legend: [Gp]|k4. Figure S3: Bifurcation plot of G_p versus k_4. The model is sensitive to k_4 if k_4 ≤ 3 h⁻¹ in terms of
: chart::>

<a id='1db7cf31-1984-4147-a283-0d12f4ddaade'></a>

amplitude of oscillations.

<!-- PAGE BREAK -->

<a id='9fefb6d0-6cd0-43f1-913f-87311c739935'></a>

<::line graph: Time Course showing Concentration (mmol/l) vs. Time (h). The x-axis ranges from 0 to 100 hours. The y-axis ranges from 0 to 16 mmol/l. Three lines are plotted: a yellow line labeled "[A]|Time", a red line labeled "[Gi]|Time", and a blue line labeled "[Gp]|Time". The red line ([Gi]) shows large, spike-like oscillations, peaking around 14 mmol/l. The blue line ([Gp]) shows smaller, spike-like oscillations that peak shortly before the red line's peaks, reaching about 8 mmol/l. The yellow line ([A]) remains consistently low, near 0 mmol/l, with small fluctuations. The oscillations are periodic, with peaks occurring approximately every 20 hours. Figure S4: Time course after introducing self-amplification to G, in addition to Gp. This can be obtained by changing the term k4Gp to k4G₁Gp in eq (1). The oscillations become spike-like but no dramatic difference to the results of the minimal model can be seen. In order to obtain realistic oscillations, the parameter values needed to be changed. The parameters from Table 1 were reduced to 10% while k3 was increased to 15.93 h⁻¹. In the main text, we only use self-amplification for Gp.::>

<!-- PAGE BREAK -->

<a id='f2423a89-3aa6-4ef3-8031-f376643dd0e5'></a>

<::A line chart titled "Time Course". The y-axis is labeled "mmol/l" and ranges from 0 to 2,500. The x-axis is labeled "h" and ranges from 0 to 12. The chart displays six data series:
- [B1] [Time]: Represented by a red line, showing a relatively flat concentration that slightly increases after approximately 9 hours.
- [B2] [Time]: Represented by a blue line, similar to [B1] but at a slightly higher concentration.
- [B3] [Time]: Represented by a green line, similar to [B2] but at a slightly higher concentration.
- [B4] [Time]: Represented by a cyan line, similar to [B3] but at a slightly higher concentration.
- [B5] [Time]: Represented by a magenta line, showing a more pronounced increase starting around 8-9 hours, reaching approximately 300 mmol/l by 11 hours.
- [SS] [Time]: Represented by a yellow line, which remains low until about 9.5 hours, then exhibits a sharp, exponential increase, reaching over 2,000 mmol/l by 11 hours.
: chart::>

<a id='47389907-2c74-4813-ad95-fe1a24978a31'></a>

Figure S5: Plot of the time course of growth as calculated from Eq. (4) for various initial values of Gp from 1 mmol/l - 10 mmol/l with a step size of 1 mmol/l (all wavy curves). On average the curves have a doubling time of about 99 minutes. The black monotonic curve (initial value: 10-9 mmol/l) indicates the growth calculated by the steady state values. It can be seen that the steady state growth rate overtakes the oscillating growth rate at about 10.5 hours.

<a id='ffc35794-8ed4-4b29-8790-60d1352e3901'></a>

Table S1: Sensitivity analysis for all variables at steady state with respect to all parameters.
Darker shades denote higher sensitivity. Positive sensitivity is shown in green and negative in red. White means that the variable is not sensitive to that parameter.

<a id='d52b4e1d-f48a-4173-9f7a-903fb5b6bfad'></a>

a: Values indicate unscaled derivatives at steady state.
<table id="7-1">
<tr><td id="7-2"></td><td id="7-3">K1</td><td id="7-4">K2</td><td id="7-5">K3</td><td id="7-6">K4</td><td id="7-7">k5</td></tr>
<tr><td id="7-8">[A]</td><td id="7-9">5.6604</td><td id="7-a">-0.2944</td><td id="7-b">0</td><td id="7-c">-0.1887</td><td id="7-d">0</td></tr>
<tr><td id="7-e">[G]</td><td id="7-f">9.8441</td><td id="7-g">-0.5120</td><td id="7-h">0.6790</td><td id="7-i">-0.3281</td><td id="7-j">-1.1798</td></tr>
<tr><td id="7-k">[Gp]</td><td id="7-l">11.3208</td><td id="7-m">-0.5888</td><td id="7-n">0.7809</td><td id="7-o">-1.9392</td><td id="7-p">0</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='15a960f8-36c2-418f-8260-9f4df1c8e0b6'></a>

**b**: Values indicate scaled derivatives at steady state.
<table id="8-1">
<tr><td id="8-2"></td><td id="8-3">k_1</td><td id="8-4">k_2</td><td id="8-5">k_3</td><td id="8-6">k_4</td><td id="8-7">K5</td></tr>
<tr><td id="8-8">[A]</td><td id="8-9">1.2416</td><td id="8-a">-1</td><td id="8-b">0</td><td id="8-c">-0.2416</td><td id="8-d">0</td></tr>
<tr><td id="8-e">[G]</td><td id="8-f">1.2416</td><td id="8-g">-1</td><td id="8-h">1</td><td id="8-i">-0.2416</td><td id="8-j">-1</td></tr>
<tr><td id="8-k">[G_p]</td><td id="8-l">1.2416</td><td id="8-m">-1</td><td id="8-n">1</td><td id="8-o">-1.2416</td><td id="8-p">0</td></tr>
</table>
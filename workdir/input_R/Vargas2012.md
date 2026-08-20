<a id='a8432bda-00aa-46df-ae8e-751f6dd5de62'></a>

8th IFAC Symposium on Biological and Medical Systems
The International Federation of Automatic Control
August 29-31, 2012. Budapest, Hungary

<a id='96c75bf9-54b2-464f-a2af-7c2a7abf5506'></a>

<::logo: IFAC
IFAC
This logo features the text "IFAC" above a stylized gray arrow that forms a loop, suggesting a cyclical or continuous process, with one end shaped like a double-ended arrow and the other a single arrow::>

<a id='21d34d73-5a15-4597-a7ed-6cfa89d38144'></a>

Innate Immune System Dynamics to
Influenza Virus

<a id='a1de478e-5ccd-43b6-98bc-8a8898245d05'></a>

Esteban A. Hernandez-Vargas * Michael Meyer-Hermann * ,**

* Systems Immunology Department, Helmholtz-Zentrum für
Infektionsforschung, Inhoffenstraße 7, D-38124, Braunschweig,
Germany (e-mail: abelardo_81@hotmail.com)
** Bio Center for Life Sciences, University of Technology
Braunschweig, Spielmannstr. 7, 38106 Braunschweig, Germany
(e-mail: michael.meyer-hermann@helmholtz-hzi.de)

<a id='e56566e6-aec6-4b20-bde7-7ac470b88118'></a>

**Abstract:** The understanding of how influenza virus infection activates the immune system is crucial to designing prophylactic and therapeutic strategies against the infection. Nevertheless, the immune response to influenza virus infection is complex and remains largely unknown. In this paper we focus in the innate immune response to influenza virus using a mathematical model, based on interferon-induced resistance to infection of respiratory epithelial cells and the clearance of infected cells by natural killers. Simulation results show the importance of IFN-I to prevent new infections in epithelial cells and to stop the viral explosion during the first two days after infection. Nevertheless, natural killers response might be the most relevant for the first depletion in viral load due to the elimination of infected cells. Based on the reproductive number, the innate immune response is important to control the infection, although it would not be enough to clear completely the virus. The effective coordination between innate and adaptive immune response is essential for the virus eradication.

<a id='1fbfef9e-886e-4b99-8297-fefc8ad37240'></a>

Keywords: innate immune response, influenza virus, modelling, elderly

<a id='b393d3ad-4dc9-4a98-a091-a9546da357e1'></a>

## 1. INTRODUCTION
Influenza virus can be transmitted by direct contact such as hand shake or airborne virus; this means is very likely to promote pandemics with high death tolls [World Health Organization, 2011]. For instance, annual hospitalization rates for flu have been reported to be as high as 226,000 individuals in USA [CDC, 2007].

<a id='8bce55b1-1512-4bd0-b778-ce13ecbf8803'></a>

Influenza virus causes acute respiratory disease by the infection of the epithelial cells lining the nasal mucosa, the larynx and the tracheobronchial tree. Typically the infec- tion will involve on the upper respiratory tract and the upper division of bronchi, nevertheless in fatal cases the infection can spread to lower lungs [van Riel et al., 2006]. Cell infection begins with the adsorption of the virus. The influenza virus hemagglutinin (HA) is responsible for bind- ing the sialic acid receptors on the surface of epithelial cells providing a strong bond. Neuraminidase (NA) participates in virus release from the cell. Once the virus is inside the cell, the virus kidnaps the cell and starts to replicate. While antibodies to HA are protective, antibodies to NΑ are much less effective. The incubation period, between 24-96 hours, for influenza depends in the size of initial inoculum [Potter, 2004]. The period between successful

<a id='794a8e40-565f-4feb-bd4f-43bf4e1a3972'></a>

---* This work was supported by the German Federal Ministry for Education and Research BMBF.

<a id='4b4c0d53-3a91-431a-89bc-18743042c2f7'></a>

infection and the viral production has been called "eclipse
phase" [Beauchemin and Handel, 2011]. After this phase
infected cells will quickly promote an exponential growth
of viral titer, which peaks around 2-3 days post infection
(dpi).

<a id='0ec29e12-7e28-4d3a-a177-17676469ba84'></a>

Influenza is a serious concern for elderly, mainly because elderly immune system is not as efficient as one of a young person. More than 36,000 deaths in the elderly are due to flu or its complications [CDC, 2007]. Ageing is a complex unknown process; the balance in T cell repertoire appears to be crucial for the defence against infections throughout life [Nikolich-Zugich, 2008]. The interaction of influenza virus with the immune system and how this is affected by the ageing process are still unresolved [Beauchemin and Handel, 2011]. Most of these problems require quantita- tive analysis of immune components and their respective interactions. Hence, the necessity of using alternative ap- proaches to tackle these drawbacks has motivated several researchers of different disciplines. To this end, several mathematical models have been attempting to capture the dynamics of influenza to understand the interaction of the virus with the immune system cells [Beauchemin and Handel, 2011].

<a id='11a711f2-7f8a-415f-aa9a-ebd1cdd5a86e'></a>

Much work has been focus in the basic relation host and
virus [Möhler et al., 2005], [Baccam et al., 2006] while oth-
ers have developed more complicated models that quan-

<a id='3116d56a-e1bb-401d-b90d-fe5d5ca4a400'></a>

978-3-902823-10-6/12/$20.00 © 2012 IFAC

<a id='4fff0b4a-a443-4672-a32e-3e1449f73429'></a>

260

<a id='897c3209-190d-43e1-bc77-69202b841661'></a>

10.3182/20120829-3-HU-2029.00029

<!-- PAGE BREAK -->

<a id='32c40f5c-83b6-4a01-a7d6-161096d3ad48'></a>

8th IFAC Symposium on Biological and Medical Systems August 29-31, 2012. Budapest, Hungary

<a id='f626878d-8eef-4784-976d-67a2e8baeb58'></a>

tifies the interplay between viral replication and adaptive immunity [Hancioglu et al., 2007], [Lee et al., 2009], [Saenz et al., 2010]. The adaptive immune system has received considerable attention for the mathematical community. However, the successful eradication of a pathogen depends on the coordinated action of the innate and adaptive immune systems. Moreover, influenza vaccination is effi-cacious in the young, but this offers limited protection in the elderly. Therefore, it is important to understand the primary response to influenza. The innate immune system can be divided in two parts [Hancioglu et al., 2007]. As a first line of protection, IFN-a and ̢ (IFN-I) interact with healthy cells and convert them to an infection resistant state. Then, the virus can not spread efficiently, providing enough time to the adaptive system to react and eliminate the virus [Price et al., 2000]. The second immune response is promoted by natural killers (NK) which can destroy infected cells before they can release a mature virus [Tamura et al., 2005]. At the same time, antigen presenting cells (APCs) have stimulated the adaptive immune system organizing the production of virus specific plasma cells to tackle the infection.

<a id='bd6776f5-97ad-49ba-afa1-8f84c3bcf74c'></a>

A few influenza infection models have studied the innate immune system; [Saenz et al., 2010] proposed a simple model validated with equine data in order to show the importance of interferon kinetics in influenza pathology. In similar direction, [Hancioglu et al., 2007] suggest a more complex model integrating both immune and adaptive system. However these models have not provided specific interactions in the innate response, this means between epithelium cells, interferon and natural killers. Murine studies [Beli et al., 2011] reveal that age-related defects in natural killers, specially NK cells from aged mice were reduced and had impaired function in lungs during influenza infection.

<a id='870e0f6c-7000-4898-9dfc-bc8fe012c9fe'></a>

Based on a systematic approach, the aim in this work is to understand the innate immune response to influenza infection and to unveil the foremost mechanisms involved in the innate immune system that may cause serious problems in the elderly. The paper is organized as follows: The proposed model and explanation are given in Section 2. Simulation results and model parameters values are presented in Section 3. Dynamic studies that reveal the important mechanisms for the eradication of the infection are discussed in Section 4. Conclusions finalize the paper in Section 5.

<a id='5a169fc0-8e2c-4f46-9d93-4de8911fa202'></a>

## 2. INNATE IMMUNE SYSTEM MODEL

The innate immune response is a complex system that is regulated by chemokines and cytokines produced by infected cells and APCs. The proposed mathematical model for the innate immune response to influenza virus is composed by 7 differential equations presented in (1). This is a simplified model of cell populations and cytokines as is shown in Fig 1. The place of infection by influenza virus is the airway epithelium. Therefore, we consider respiratory tract epithelial cells in one of the four possible states: healthy ($U_H$), partially infected ($U_E$), infected ($U_I$)

<a id='57e49ce2-f38e-4431-9948-f468851ecb89'></a>

and resistant to infection ($U_R$). The number of uninfected cells increases with a specific constant cell growth rate $S_H$. Natural death rate of healthy, infected, and viral resistant epithelium cells are represented by $\delta_H$, $\delta_I$ and $\delta_R$ respectively. Virus particles ($V$) interact with healthy cells and infect them with a rate $k_I$. The period between successful infection and production of virus, approximately 4-6 hours, is often called and modelled as "eclipse phase" [Möhler et al., 2005], which is considered by the term $k_E$. Once the cells are productively infected, they can release thousands of copies a day, that is expressed by the parameter $\rho_V$. The clearance of the virus is included by $\delta_V$.

<a id='a261a501-8b3f-4488-82bb-f6c502cec6dc'></a>

$$\dot{U}_H = S_H - k_I U_H V - k_R U_H [IFN] - \delta_H U_H$$
$$\dot{U}_E = k_I U_H V - k_E U_E - q_K U_E K$$
$$\dot{U}_I = k_E U_E - \delta_I U_I - q_K U_I K$$
$$\dot{U}_R = k_R U_H [IFN] - \delta_R U_R \quad (1)$$
$$\dot{V} = \rho_V U_I - \delta_V V$$
$$\dot{[IFN]} = a_I U_I - \delta_{IFN} [IFN]$$
$$\dot{K} = S_K + \Phi_K U_I - \delta_K K$$

<a id='d8319ce1-1c57-4d1d-a479-7c0e2e377023'></a>

In the first line of defence, APC and infected cells stimulate the innate immunity by secreting interferon IFN-I. Note that we consider APCs and epithelium cells as one compartment. Therefore, this compartment of cells will produce IFN-I with a ratio $a_I$. These IFN-I molecules may convert cells to an infection resistant state with a rate $k_R$. IFN is lost through degradation according to the rate $\delta_{IFN}$.

<a id='eb71fb68-134a-4c79-9a07-c96934a8254a'></a>

<::flowchart: Schematic representation of the innate immune response to influenza virus.The diagram is enclosed within a dashed box labeled "Lung Compartment".Inside the lung compartment, there are several nodes representing different cell types or molecules, and arrows indicating interactions or transformations.The nodes are:1.  UR (purple circle)2.  UH (blue circle)3.  UE (gray circle)4.  UI (blue circle)5.  V (black circle)6.  K (red circle)7.  IFN -I (blue rectangle)Outside the lung compartment, there is one node:8.  NK Reservoirs (orange rectangle)The interactions are as follows: - An arrow from UR to UH, labeled kR. - An arrow from UH to UE, labeled kI. - An arrow from UE to UI, labeled kE. - An arrow from UI to V, labeled ρV. - An arrow from UI to IFN -I, labeled aI. - A red line from IFN -I to K. - A red line from IFN -I to UI. - An arrow from UI to K, labeled qK. - An arrow from V to UI. - An arrow from V to K. - A line originating from both UI and K, merging and pointing to NK Reservoirs, labeled ΦK.Fig. 1. Schematic representation of the innate immune response to influenza virus.::>

<a id='fdba54c9-eec9-4e13-aca3-0b7cd075f60e'></a>

In the second line of protection, infected cells and APCs stimulate the cellular innate immunity which consists of natural killers ($K$) that destroy infected cells, this is modelled using the bilinear terms $q_K U_E K$ and $q_K U_I K$.

<a id='9e5f8017-df26-4bb9-8687-798be113164b'></a>

261

<!-- PAGE BREAK -->

<a id='04a9e40a-9e4d-4f23-9411-f850c7e8c410'></a>

8th IFAC Symposium on Biological and Medical Systems
August 29-31, 2012. Budapest, Hungary

<a id='e9c38aef-4c80-431e-a73a-d19bb91b009d'></a>

The number of NKs increases with a constant cell growth rate $S_K$ and die with rate $\delta_K$. Just after a few hours of inflammatory stimulation, large numbers of natural killers are recruited from the blood to the lung and become activated to secrete cytokines, particularly IFN-\gamma [Gregoire et al., 2007]. Recruitment of natural killers from the blood ($K_B$) to the lung ($K_L$) may be represented by the term $\Phi_K K_B U_I$. For simplicity we assume that the number of natural killers in blood and other compartments is large enough that the depletion of NKs, is negligible, represented by $\Phi_K U_I$.

<a id='2299feba-5928-421e-af99-cd0050d050b1'></a>

## 3. SIMULATION RESULTS

Model implementation outlined in last section is conducted using MATLAB. The set of parameters in this model is as follows;

<a id='085d8bcd-13eb-465f-a29e-b3dcf3b52d42'></a>

$\theta = \{k_I, k_R, k_E, q_K, \rho_V, a_I, \Phi_K, \delta_H, \delta_I, \delta_R, \delta_{IFN}, \delta_V, \delta_K\}$

Parameter values were based on other works as is presented in Table 1 and others were adjusted with experimental data from [Quinlivan et al., 2007]. For initial conditions there are approximately $5\times10^8$ epithelial cells in the upper respiratory tract [Baccam et al., 2006]. Infected cells and IFN molecules are initialize as zero, and initial viral concentration as $10^{-3}$ copies/ml. Based on experimental observations in [Gregoire et al., 2007], we use $8\times10^5$ natural killer cells for simulations.

<a id='88b4da7e-f5cc-41c8-9b4e-c715a617d0e9'></a>

Table 1. Parameters values for the model (1)
<table id="2-1">
<tr><td id="2-2">Parameter</td><td id="2-3">Nominal Value</td><td id="2-4">Taken from:</td></tr>
<tr><td id="2-5">kI</td><td id="2-6">3×10-3 mL/day</td><td id="2-7">Möhler et al. [2005]</td></tr>
<tr><td id="2-8">kR</td><td id="2-9">7 day-1</td><td id="2-a">Baccam et al. [2006]</td></tr>
<tr><td id="2-b">kE</td><td id="2-c">0.5 day-1</td><td id="2-d">Saenz et al. [2010]</td></tr>
<tr><td id="2-e">qK</td><td id="2-f">3 × 10-6 cels/day</td><td id="2-g">Kuznetsov et al. [1994]</td></tr>
<tr><td id="2-h">ϕK</td><td id="2-i">1 × 10-3 cells/day</td><td id="2-j">Fitted</td></tr>
<tr><td id="2-k">aI</td><td id="2-l">3 × 10-6 fold change/day</td><td id="2-m">Fitted</td></tr>
<tr><td id="2-n">pV</td><td id="2-o">1 × 10-2 TCID50/ml day</td><td id="2-p">Baccam et al. [2006]</td></tr>
<tr><td id="2-q">δH</td><td id="2-r">0.01</td><td id="2-s">Baccam et al. [2006]</td></tr>
<tr><td id="2-t">δI</td><td id="2-u">0.01</td><td id="2-v">Fitted</td></tr>
<tr><td id="2-w">δR</td><td id="2-x">0.01</td><td id="2-y">Baccam et al. [2006]</td></tr>
<tr><td id="2-z">δIFN</td><td id="2-A">4</td><td id="2-B">Saenz et al. [2010]</td></tr>
<tr><td id="2-C">δK</td><td id="2-D">0.04</td><td id="2-E">Kuznetsov et al. [1994]</td></tr>
<tr><td id="2-F">δV</td><td id="2-G">5.2</td><td id="2-H">Baccam et al. (2006</td></tr>
<tr><td id="2-I">SH</td><td id="2-J">UHOδH</td><td id="2-K">Steady state</td></tr>
<tr><td id="2-L">$S_K$</td><td id="2-M">$K_0\delta_K$</td><td id="2-N">Steady state</td></tr>
</table>

<a id='b5285da1-f3ff-4101-ae8e-f7ab5346cc5b'></a>

Notice that the proposed model is for the innate immune system, therefore simulation results correspond with ex-perimental data up to 6 days after infection [Quinlivan et al., 2007]. That means the innate immune system is the responsible for the protection against the virus until the adaptive system is ready to clear the infection and causes the final drop in the viral which is not observed in simulations, see Fig. 2.

<a id='dda26a48-6d12-43a0-85f4-cba49ba4812e'></a>

Epithelium cells experience a fast depletion in the upper
respiratory tract just a few hours after infection. Consequently cell infection cycles quickly result in an exponen-
tial growth of viral titer which which peaks around 2-3

<a id='b3feb237-5d25-4989-9fff-2538a0675364'></a>

<::line graph: The top graph, titled "Lung cells (cells)" on the y-axis (logarithmic scale from 10^0 to 10^8) and "Time (days)" on the x-axis (0 to 8), shows the time-courses of different cell populations. The legend indicates: U_H (blue line), U_R (green line), U_I (red line), and Total healthy cells (light blue dashed line). U_H starts high, decreases significantly around day 1, then gradually recovers. U_R starts low, increases rapidly, then stabilizes at a high level. U_I starts low, peaks around day 1.5, then decreases. The 'Total healthy cells' line remains constant at a high level.: chart::>
<::line graph: The middle graph, titled "Viral load (EID_50/ml)" on the y-axis (logarithmic scale from 10^0 to 10^7) and "Time (days)" on the x-axis (0 to 8), displays the time-course of viral load. The legend includes: Model (blue line) and Quinlivan 2007 (grey 'x' markers with error bars). The model shows viral load starting low, peaking around day 1.5-2, and then gradually decreasing and stabilizing. The experimental data points from Quinlivan 2007 generally follow this trend.: chart::>
<::line graph: The bottom graph, titled "IFN-I (fold change)" on the y-axis (linear scale from 0 to 14) and "Time (days)" on the x-axis (0 to 8), illustrates the time-course of IFN-I concentration. The legend specifies: Model (blue line) and Quinlivan 2007 (grey 'x' markers with error bars). The model shows IFN-I starting at zero, peaking around day 1.5, and then rapidly decreasing back to zero. The experimental data points from Quinlivan 2007 also show a peak around day 1.5-2, followed by a decline.: chart::>
Fig. 2. Time-courses of epithelial cells, viral load and IFN concentration respectively

<a id='82568609-fa04-4c3a-951b-da350d3305b7'></a>

dpi as is illustrated in Fig.2. Clinical influenza symptoms typically result from the damage of about 10% of epithelial cells. For this simulation scenario, the maximum peak of infected cells is approximately 8% and take place around 1-2 days dpi.

<a id='3ae6d82b-0266-4917-8513-336a5cf60e70'></a>

While the infection process is invading the upper respira-
tory tract, the innate immune system coordinates a fast
and effective protection using IFNs. Simulation results

<a id='79ffa656-ebed-430e-a2dd-21d21c7be252'></a>

262

<!-- PAGE BREAK -->

<a id='e8dc1e3b-d37c-4857-b488-55168fa03906'></a>

8th IFAC Symposium on Biological and Medical Systems
August 29-31, 2012. Budapest, Hungary

<a id='4a80f649-8cb8-45b3-a743-ff79019c3953'></a>

show in Fig.2 that IFN-I dynamics represent reasonably experimental data as well as clinical observations that detect high IFN titers two days after virus shedding begin and generally peak simultaneously with virus titer peak [Hayden et al., 1998] [Van Reeth, 2000]. IFN-I molecules induce an antiviral state in the cells, therefore the virus incursion to another cells is interrupted. An interesting situation takes place in the beginning of the infection; there is a running process of infection and protection, even the infection process starts first, the protection of cells by IFN-I might be much faster than the infection process. Consequently, this will block the exponential growth of viral load reported in the 1-2 dpi. This brings to the atten- tion the importance of communication processes between infected cells and their neighbours in order to coordinate an effective protection response. Notice that IFN-I is pro- duced by infected cells and other hosts as macrophages monocytes and dendritic cells [Baccam et al., 2006], nev- ertheless for simplicity, all these cells are expressed in a single compartment.

<a id='f159e0ea-27a6-477f-a40d-96e89eeee451'></a>

At the same time that IFN-I molecules are protecting cells, a second response is organized by natural killers. One of the main responsibilities of these cells is the production of cytokines and the rapid elimination of infected cells [Jost et al., 2011]. Natural killers compose 10% of resident lymphocytes in the lung [Stein-streilein et al., 1983]. The order for natural killers frequency is lung > liver > peripheral blood > spleen > bone marrow > lymph node > thymus, where natural killers are almost undetectable [Gregoire et al., 2007].

<a id='532802a7-462c-455f-8423-4bfb362949c4'></a>

<::chart: A line graph titled "Natural killer dynamics" (Fig. 3) shows the number of Natural Killers (cells) in the lung over time (days). The y-axis, labeled "Natural Killers (cells)", ranges from 8.0 x 10^5 to 8.2 x 10^5. The x-axis, labeled "Time (days)", ranges from 0 to 8. A blue line, representing "K in Lung", starts at approximately 8.0 x 10^5 cells at Time = 0. It remains low until around Time = 1 day, then rapidly increases, peaking at approximately 8.19 x 10^5 cells around Time = 3 days. After the peak, the line gradually decreases, reaching about 8.17 x 10^5 cells by Time = 8 days.::>

Fig. 3. Natural killer dynamics

<a id='4548fe3e-24bb-4389-80fd-b768cc3c6a54'></a>

Dynamic results in Fig.3 exhibit an increment in numbers
of natural killers in lungs, around 2%. This corresponds
to experimental observations of [Gazit et al., 2006], which
tracked natural killers in several organs during influenza
infection, and noted a slight reduction in percentage of NK
in the blood 2 dpi. Therefore, at the peak of the infection
2 dpi, the migration and action of natural killers might
be important to clear infected cells and cause the first and
the most predominant viral depletion during the infection.

<a id='310fcd2b-133f-4e02-a777-4e6b0552d788'></a>

## 4. DYNAMIC STUDY

In this section we study the steady-state for the proposed system (1), the respective equilibria may be obtained as follows;

<a id='2917d920-de6d-440b-afcb-35dbac1fb422'></a>

$$\bar{U}_H = \frac{s_H}{a_1\bar{U}_I + \delta_T}, \quad \bar{U}_E = \frac{a_2}{a_3\delta_H + a_5\bar{U}_I - a_1a_4\bar{U}_I^2}\bar{U}_I$$

$$\bar{U}_R = \frac{k_R S_H \delta_V a_I}{a_7\bar{U}_I - \delta_H \delta_V \delta_{IFN}}\bar{U}_I, \quad \bar{V} = \frac{\rho_V}{\delta_V}\bar{U}_I$$

$$\overline{IFN} = \frac{a_I}{\delta_{IFN}}\bar{U}_I, \quad \bar{K} = \frac{s_K}{\delta_K} + \frac{\phi}{\delta_K}\bar{U}_I$$

<a id='f8446d03-6a3e-448a-aa17-2e3325910f13'></a>

Ū_I is the solution of the polynomial:

<a id='f0812d97-7c94-4f74-9fb4-eaa89e4ddf4b'></a>

\alpha_1\bar{U}_I^4 + \alpha_2\bar{U}_I^3 + \alpha_3\bar{U}_I^2 + \alpha_4\bar{U}_I = 0 (2)

<a id='2dd8bc03-ef2d-42fa-8dcc-e03dc2bf00a9'></a>

where the new variable sets {$a_1, ..., a_7$} and {$\alpha_1, ..., \alpha_4$} are functions of $\theta$. Equation (2) has four solutions, therefore four equilibria may be obtained for the system (1); one of them is the uninfected equilibrium which is easy to obtain when $\bar{U}_I = 0$. The other three equilibrium points can not be obtained analytically, then using parameter values of Table 1 we obtain numerically the equilibria with biological meaning as presented in Table 2. For the meaningful infected equilibrium, we observe how the innate immune system is able to reduce and to keep low viral levels.

<a id='bcee71b0-d432-4167-a2d2-a2cb82bd35ca'></a>

Table 2. Equilibria for (1)

<table id="3-1">
<tr><td id="3-2">State</td><td id="3-3">Uninfected</td><td id="3-4">Infected</td></tr>
<tr><td id="3-5">ŪH</td><td id="3-6">SH
δH</td><td id="3-7">2.44 x 10^6</td></tr>
<tr><td id="3-8">UE</td><td id="3-9">0</td><td id="3-a">8.94 x 10^5</td></tr>
<tr><td id="3-b">UI</td><td id="3-c">0</td><td id="3-d">1.84 x 10^5</td></tr>
<tr><td id="3-e">UR</td><td id="3-f">0</td><td id="3-g">2.37 x 10^8</td></tr>
<tr><td id="3-h">V</td><td id="3-i">0</td><td id="3-j">354.65</td></tr>
<tr><td id="3-k">IFN</td><td id="3-l">0</td><td id="3-m">0.138</td></tr>
<tr><td id="3-n">K</td><td id="3-o">SK / δK</td><td id="3-p">804.610 × 103</td></tr>
</table>

<a id='156e7f83-4c54-4b9d-bc28-62293cf1b946'></a>

In order to understand the key processes in the innate immune system and to quantify the effect in the viral load for the infected equilibrium, we perform variations around nominal values for those parameters directly involved in the innate response, these are $k_R$, $\phi$, $q_k$ and $a_I$. Fig. 4 reveals that innate immune parameters related to IFN are robust to variations. On one hand we notice that IFN-I may minimize the viral load when the IFN-I production ($a_I$) and conversion to infection resistant state ($k_R$) are increased. On the other hand a failure in this response can produce an increment in viral load accompanied by more cell infections.

<a id='4fe10a0f-9eca-4ded-8bca-e5b8a84dab4c'></a>

Notice that in case of a complete failure of IFN-I response, there is not a very marked explosion in the viral load. This is consistent with experimental observations that influenza viruses have evolved and can circumvent the IFN response but there are other mechanisms to control the infection [Price et al., 2000]. Moreover, the resistant viral state is maintained for approximately 8 -10 days, then cells could

<a id='8a778d3e-07b2-4928-8478-2bb9a5cbf58e'></a>

263

<!-- PAGE BREAK -->

<a id='bafba2bc-8686-438f-980b-d8e5ea417bae'></a>

8th IFAC Symposium on Biological and Medical Systems
August 29-31, 2012. Budapest, Hungary

<a id='8a345829-dec0-4c0a-80af-9b4e462c447d'></a>

be infected by the virus. For this reason the relevance that the immune system has several lines of defence. <::chart: A line chart titled "Viral infected equilibrium analysis; parameter variation respect nominal values presented in Table 1". The y-axis is labeled "Viral load (EID50/ml)" and has a logarithmic scale from 10^2 to 10^4. The x-axis is labeled "Variation (%)" and ranges from -100 to 100. There are four lines plotted with a legend indicating: - q_K (blue line) - φ (red line) - k_R (black line) - a_I (dashed black line, though it appears as a thin black line in the image) The blue line (q_K) starts high at -100% variation and decreases significantly as variation increases. The red line (φ) is a horizontal line around 300 EID50/ml. The black line (k_R) starts around 600 EID50/ml at -100% variation and decreases linearly to around 200 EID50/ml at 100% variation. The dashed black line (a_I) is very close to the k_R line, starting around 700 EID50/ml at -100% variation and decreasing to around 250 EID50/ml at 100% variation. The q_K line intersects the φ line and the k_R line between 0% and 20% variation.::>

<a id='6e01e704-16d8-45ad-80ee-c1ae8f9fd8b1'></a>

Natural killers are considered to be responsible in the rapid elimination of viral infected cells [Jost et al., 2011]. We notice in Fig.4 that the clearance rate of natural killers on infected epithelium is important to tackle the infection. An appropriate response of NKs may clear the infection on the contrary an inadequate response would promote an uncontrolled explosion in the viral load. This could be relevant in the elderly, in accordance with the studies of [Beauchemin and Handel, 2011], they show that aged mice have NK dysfunctions and elevated lung virus titers during the 4 dpi.

<a id='06358dd5-8c68-44ee-96fc-6f1c78bd9a66'></a>

In silico studies for the proposed model (1) reveal that the migration of natural killers to the lung ($\phi$) might not be as important as the effectiveness of NKs to eradicate infected cells. However, this migration could be important for the production of cytokines to produce an adequate adaptive response. Experimental data [Beauchemin and Handel, 2011] and simulation results suggest that NKs are very important to promote an early and effective response to influenza infection; this is more crucial in the elderly when vaccines are not available or effective.

<a id='6a0034ac-a56c-4dd4-9ee9-77aff29dd6e6'></a>

## 4.1 Reproductive Number
The most important concerns about any infectious disease is its ability to invade a population. For this reason we analyse for the proposed model the reproductive number ($R_0$) [Diekmann et al., 1990], which is roughly defined as the expected number of secondary individuals produced by an individual in its lifetime. On one hand, if $R_0$ is less than one, each infected individual produces on average less than one infected individual, and therefore the infection will be cleared from the population. On the other hand, if $R_0$ is greater than one, the pathogen is able to invade the susceptible population [Diekmann et al., 1990]. For the case of influenza, the reproductive number has been computed for a simple influenza model in [Baccam

<a id='709365c2-30df-4a66-8c76-ee20939a1bc6'></a>

<::line chart
: The chart displays "Reproductive Number" on the y-axis (log scale, from 10^-2 to 10^3) against "Time (days)" on the x-axis (from 0 to 8). The blue line starts around 200, drops sharply to a minimum near 10^-2 at approximately 1.5 days, then rises gradually to about 2.5 at 5.5 days, and then slightly decreases to around 2 at 8 days.
Fig. 5. Reproductive number during the innate immune response::>

<a id='96ae3dff-3292-4302-8d71-10bda1c6d737'></a>

et al., 2006], where authors calculated R₀ for different patients; the mean was 11.1, with a 95% CI of 6.6 to 18.5. Thus, experimental influenza virus infection is predicted to spread rapidly through the cells in the upper respiratory tract. However, authors do not consider the influence of the immune response. To show the effect of the innate response on the influenza infection, we compute the reproductive number for the system (1) as follows:

<a id='2fc45418-0993-46f3-8817-82752330c9d8'></a>

R_o = \frac{S_H k_I k_E \rho_v}{(k_E + q_u \bar{K})(\delta_H + k_R [IFN])(\delta_I + q_u \bar{K})\delta_v} (3)

The reproductive number is obtained from the infected steady state and is presented as a function of [IFN] and \bar{K}. We can observe in Fig.5 how R_o is not affected by the innate immune response during the first hours of infection, then the virus would be able to spread through epithelium cells. During the second day of infection, the innate response brings the expanse of the infection down and keeps R_o \approx 2, that is when dynamics are close to the infected steady state. This means that the innate response is very important to stop the accelerated infection process, however it would not be enough to clear completely the infection.

<a id='11f6178b-fb81-4cd3-b600-72d36934551c'></a>

5. CONCLUSIONS
A mathematical model is proposed for the interaction of the innate immune system and influenza virus. The model reasonably describes experimental data for viral load and IFN-I concentration during the first 6 days of infection. In silico results reveal the importance of IFN-I to convert cells to a viral resistant state and interrupt the infection to other cells. Nevertheless, natural killers appears to be more important to promote the clearance of infected cells provoking the first sharp drop in viral load concentration. The reproductive number exhibits the role of the innate immune response to control the infection, although not enough to clear the infection. One could speculate that these mechanisms become more critical in the elderly when a clear immune dysfunction is presented.

<a id='951e5e3f-09a5-48be-9f47-b7a468d33264'></a>

264

<!-- PAGE BREAK -->

<a id='e9c543d2-a647-479b-88cd-02c17438b088'></a>

8th IFAC Symposium on Biological and Medical Systems
August 29-31, 2012. Budapest, Hungary

<a id='0dbebe7f-2d4d-4df8-a420-7cf455432867'></a>

REFERENCES
Prasith Baccam, Catherine Beauchemin, Catherine Macken, Frederick Hayden, and Alan Perelson. Kinetics of influenza A virus infection in humans. Journal of virology, 80(15):7590-9, August 2006.
Catherine Beauchemin and Andreas Handel. A review of mathematical models of influenza A infections within a host or cell culture: lessons learned and challenges ahead. BMC public health, 11 (Suppl 1):S7, January 2011.
Eleni Beli, Jonathan Clinthorne, David Duriancik, II-woong Hwang, Sungjin Kim, and Elizabeth Gardner. Natural killer cell function is altered during the primary response of aged mice to influenza infection. Mechanisms of Ageing and Development, 132(10):503-510, 2011.
CDC. Morbidity and Mortality Weekly Report Prevention and Control of Influenza Recommendations of the Advisory Committee. Technical report, 2007.
O Diekmann, J Heesterbeek, and J Metz. On the definition and the computation of the basic reproduction ratio R0 in models for infectious diseases in heterogeneous populations. Journal of Mathematical Biology, 28(4): 365-382, 1990.
Roi Gazit, Raizy Gruda, Moran Elboim, Tal I Arnon, Gil Katz, Hagit Achdout, Jacob Hanna, Udi Qimron, Guy Landau, Evgenia Greenbaum, Zichria Zakay-Rones, Angel Porgador, and Ofer Mandelboim. Lethal influenza infection in the absence of the natural killer cell receptor gene Ncr1. Nature immunology, 7(5):517-23, May 2006. doi: 10.1038/ni1322.
Claude Gregoire, Lionel Chasson, Luci Carmelo, Elena Tomasello, Geissmann Frederic, Eric Vivier, and Thierry Walzer. The trafficking of natural killer cells. Immunological Reviews, 220:169-182, 2007.
Baris Hancioglu, David Swigon, and Gilles Clermont. A dynamical model of human immune response to influenza A virus infection. Journal of theoretical biology, 246(1):70-86, May 2007. doi: 10.1016/j.jtbi.2006.12.015.
F Hayden, R Fritz, M Lobo, W Alvord, W Strober, and S Straus. Local and systemic cytokine responses during experimental human influenza A virus infection. Relation to symptom formation and host defense. The Journal of clinical investigation, 101(3):643-9, February 1998.
Stephanie Jost, Heloise Quillay, Jeff Reardon, Eric Peterson, Rachel Simmons, Blair Parry, Nancy Bryant, William Binder, and Marcus Altfeld. Changes in Cytokine Levels and NK Cell Activation Associated with Influenza. Plos ONE, 6(9), 2011. doi: 10.1371/journal.pone.0025060.
V.A. Kuznetsov, I.A. Makalkin, M.A. Taylor, and A.S. Perelson. Nonlinear dynamics of immunogenic tumors: Parameter estimation and global bifurcation analysis. Bulletin of Mathematical Biology, 56(2):295-321, 1994.
Ha Youn Lee, David J Topham, Sung Yong Park, Joseph Hollenbaugh, John Treanor, Tim R Mosmann, Xia Jin, Brian M Ward, Hongyu Miao, Jeanne Holden-Wiltse, Alan S Perelson, Martin Zand, and Hulin Wu. Simula-

<a id='33a3da26-a181-48f9-98d9-5cac2444d4b0'></a>

tion and prediction of the adaptive immune response to
influenza A virus infection. Journal of virology, 83(14):
7151-65, July 2009.

<a id='e93675c9-7d9c-4c69-9e32-c5a6bd46d18b'></a>

Lars Möhler, Dietrich Flockerzi, Heiner Sann, and Udo Reichl. Mathematical model of influenza A virus production in large-scale microcarrier culture. Biotechnology and bioengineering, 90(1):46-58, April 2005. doi: 10.1002/bit.20363.

<a id='6df3f343-6fa7-4d0a-b38a-9cf9a7d4e66e'></a>

Janko Nikolich-Zugich. Ageing and life-long maintenance of T-cell subsets in the face of latent persistent infections. *Nature reviews. Immunology*, 8(7):512–22, July 2008.

<a id='566910dc-6337-4bd9-9b9e-0907ebeaf86b'></a>

Christ Potter. Influenza. In *Principles and Practice of Clinical Virology*, chapter 5, pages 271–297. John Wiley & Sons, Ltd, fifth edit edition, 2004. doi: 10.1002/0470020970.

<a id='a74e7fdd-b8cc-4fcf-ac38-25e84059afa8'></a>

G. Price, A. Gaszewska-Mastarlarz, and D. Moskophidis.
The role of alpha/beta and gamma interferons in de-
velopment of immunity to influenza A virus in mice.
_Journal of virology_, 74(9):3996–4003, May 2000.
Michelle Quinlivan, Maura Nelly, Michael Prendergast,
Cormac Breathnach, David Horohov, Sean Arkins, Yu-
wei Chiang, Hsien-jue Chu, Terry Ng, and Ann Culli-
nane. Pro-inflammatory and antiviral cytokine expres-
sion in vaccinated and unvaccinated horses exposed to
equine influenza virus. _Vaccine_, 25(41):7056–64, Octo-
ber 2007.

<a id='615252f5-3f2b-4240-914f-a61245025b4b'></a>

Roberto Saenz, Michelle Quinlivan, Debra Elton, Shona Macrae, Anthony Blunden, Jennifer Mumford, Janet Daly, Paul Digard, Ann Cullinane, Bryan Grenfell, John McCauley, James Wood, and Julia Gog. Dynamics of influenza virus infection and pathology. Journal of virology, 84(8):3974–83, April 2010. doi: 10.1128/JVI.02078-09.

<a id='1c7a6a49-54b4-4225-a35b-dc50cc8f79bd'></a>

Joan Stein-streilein, Michael Bennett, Donald Mann, Vinay Kumar, and H Ni. Natural killer cells in mouse lung: surface phenotype, target preference, and response to local influenza virus infection. _The Journal of Immunology_, 131(6):0-5, 1983.

<a id='566de451-421a-413c-9132-af04c09c5c07'></a>

Shin-ichi Tamura, Takeshi Tanimoto, and Takeshi Ku-
rata. Mechanisms of Broad Cross-Protection Provided
by Influenza Virus Infection and Their Application to
Vaccines. _Jpn. J. Infect. Dis._, 58:195-207, 2005.
K Van Reeth. Cytokines in the pathogenesis of influenza.
_Veterinary microbiology_, 74(1-2):109-16, May 2000.

<a id='a2d29857-b879-45b2-8dcb-49a31ebb9605'></a>

Debby van Riel, Vincent Munster, Emmie de Wit, Guus
Rimmelzwaan, Ron a Fouchier, Ab Osterhaus, and Thijs
Kuiken. H5N1 Virus Attachment to Lower Respiratory
Tract. *Science (New York, N.Y.)*, 312(5772):399, April
2006.

<a id='e252fea0-18f4-47af-bd55-2629c0237967'></a>

World Health Organization. Manual for the laboratory
diagnosis and virological surveillance of influenza. Tech-
nical report, 2011.

<a id='2675b3ff-61bb-4e68-9bae-634ef3f04b3d'></a>

265
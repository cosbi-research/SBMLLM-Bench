<a id='3e404c0e-2e8e-4799-ad3b-5e2b99c35094'></a>

NATIONAL INSTITUTES OF HEALTH
NIH Public Access
Author Manuscript
J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='bec11d37-23bf-4737-856c-333c021af675'></a>

Published in final edited form as:
*J Theor Biol*. 2011 May 7; 276(1): 106–116. doi:10.1016/j.jtbi.2011.01.052.

<a id='f9304f67-b9e1-4ae2-8207-bf0e72081731'></a>

**Mathematical Model of a Three-Stage Innate Immune Response to a Pneumococcal Lung Infection**

**Amber M. Smith**<sup>a,*</sup>, **Jonathan A. McCullers**<sup>b</sup>, and **Frederick R. Adler**<sup>c</sup>
<sup>a</sup>Theoretical Biology and Biophysics, Los Alamos National Laboratory, Los Alamos, NM 87545, USA
<sup>b</sup>Department of Infectious Diseases, St. Jude Children's Research Hospital, Memphis, TN 38105, USA
<sup>c</sup>Departments of Mathematics and Biology, University of Utah, Salt Lake City, UT 84112, USA

<a id='0c81c993-444f-41e8-a430-106d5a9c7f78'></a>

## Abstract
Pneumococcal pneumonia is a leading cause of death and a major source of human morbidity. The initial immune response plays a central role in determining the course and outcome of pneumococcal disease. We combine bacterial titer measurements from mice infected with *Streptococcus pneumoniae* with mathematical modeling to investigate the coordination of immune responses and the effects of initial inoculum on outcome. To evaluate the contributions of individual components, we systematically build a mathematical model from three subsystems that describe the succession of defensive cells in the lung: resident alveolar macrophages, neutrophils and monocyte-derived macrophages. The alveolar macrophage response, which can be modeled by a single differential equation, can by itself rapidly clear small initial numbers of pneumococci. Extending the model to include the neutrophil response required additional equations for recruitment cytokines and host cell status and damage. With these dynamics, two outcomes can be predicted: bacterial clearance or sustained bacterial growth. Finally, a model including monocyte-derived macrophage recruitment by neutrophils suggests that sustained bacterial growth is possible even in their presence. Our model quantifies the contributions of cytotoxicity and immune-mediated damage in pneumococcal pathogenesis.

<a id='cc9cc720-da23-46b7-aa5a-642a426ade7c'></a>

## Keywords

Bacterial Dynamics Model; *Streptococcus pneumoniae* Infection; Acute Inflammation; Dose-Dependence; Immune Response Modeling

<a id='4821be29-d5b6-49c4-96a8-2aabdfe8037f'></a>

# 1. Introduction

*Streptococcus pneumoniae* (pneumococcus) is a common pathogen associated with community acquired pneumonia, bacterial meningitis, and secondary infections following influenza (World Health Organization, 2008). Furthermore, pneumococcus is the causative agent in an estimated one million deaths worldwide each year among children under 5 years

<a id='436491cc-d47f-4546-a7f1-c7480ae5596e'></a>

*Corresponding Author: Amber M. Smith Address: Theoretical Biology and Biophysics, Los Alamos National Laboratory, Los Alamos, NM 87545, USA Phone: 505-665-4662 Fax: 505-665-3493 asmith@lanl.gov.

<a id='d26fb33b-6869-49bd-b52b-50424e7e2b18'></a>

**Publisher's Disclaimer:** This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

<a id='5c256d80-f954-421e-aa45-b6aa939e09cf'></a>

NIH-PA Author Manuscript

<a id='4a49cc8c-a205-4b27-8939-4d36e363528e'></a>

NIH-PA Author Manuscript

<a id='779dcfb1-c8f1-48cd-a0b8-3f4eb7949104'></a>

NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='d0d45db8-bfde-48ae-aa79-9e04144ce422'></a>

Smith et al.

<a id='b82ee3dd-1c22-40c7-af91-13179d01f097'></a>

Page 2

<a id='6da8f8e6-8bb6-402c-a745-c74ec2f4605b'></a>

of age (World Health Organization, 2008), particularly in developing countries. Although vaccination and antibiotic use have greatly reduced incidence of disease in all persons, the emergence of resistant strains coupled with an increase in incidence during influenza outbreaks (McCullers and English, 2008) has emphasized a need for novel treatments and a deeper understanding of pneumococcal infection kinetics.

<a id='c5fc9c2e-d56b-4eeb-b5de-cbd3e745d204'></a>

Based on experimental studies in mice, this paper introduces a series of mathematical
models that address the factors associated with favorable outcomes from pulmonary
pneumococcal infections. These models track three stages of immune cell recruitment to
identify how each cell type controls bacterial dynamics and the likelihood of host survival.

<a id='891e0ec1-5379-40d6-91c5-c1ab36906d87'></a>

1.1. Innate Immune Response to S. pneumoniae

Pneumococci colonize the nasopharynx in up to 70% of young children (Giebink, 2001) and 40% of healthy adults (Austrian, 1986), and asymptomatic carriage may last up to 6 weeks in an individual (Orihuela and Tuomanen, 2006). However, pneumococci can migrate to the lungs resulting in a more serious infection. Nevertheless, only a small fraction of carriers develop pneumonia. The rarity of pneumococcal pneumonia in healthy individuals reflects the efficiency of host defenses as most disease occurs when pathogen removal systems, such as ciliated epithelium and mucin entrapment, are compromised either due to preceding viral infections or underlying respiratory conditions (Kadioglu et al., 2008). In addition to host characteristics, both the pathogen strain and inoculum size determine whether a pneumococcal population can establish within a host (Kadioglu et al., 2008).

<a id='8a55c7dc-21dd-4a62-9f09-3f55aee580ef'></a>

When host barriers are breached, three types of cells arrive sequentially and destroy pneumococci through phagocytosis: resident alveolar macrophages (AMs), neutrophils, and monocyte-derived macrophages (MDMs). Alveolar macrophages play an important role in the defense against airborne pathogens and provide the first line of cellular defense against a pneumococcal lung infection (Dockrell et al., 2003; Gwinn and Vallyathan, 2006; Taylor et al., 2005). These cells phagocytose bacteria that reach the terminal bronchioles and alveoli (Franke-Ullmann et al., 1996; Jonsson et al., 1985), and coordinate the innate immune response to infection (Kadioglu and Andrew, 2004; Knapp et al., 2003). It is thought that when the ratio of pneumococci to phagocytes does not exceed some critical, although unknown, number, AMs can successfully phagocytose and kill pneumococci (Knapp et al., 2003). However, as this ratio increases for larger initial pneumococcal inoculums, AMs are unable to eradicate all pneumococci. Alveolar macrophages also secrete proinflammatory cytokines, such as interleukin-1 (IL-1) and tumor necrosis factor alpha (TNF-a), to initiate the inflammatory response and recruit activated neutrophils into the lung (Monton and Torres, 1998; Zhang et al., 2000).

<a id='a64460f5-2196-48ce-8610-c8f489984369'></a>

With a high-dose challenge of pneumococci, neutrophils appear within 2-4 hours postinoculation (pi) and dominate the initial inflammatory immune response. A rapid reduction of neutrophil numbers follows a peak 24-48 hours pi, even when bacterial titers remain high (Bergeron et al., 1998; Duong et al., 2001; Fillion et al., 2001; Kadioglu et al., 2000). This swift decrease in neutrophils is paralleled by MDM infiltration at 48 hours pi (Fillion et al., 2001). Nevertheless, pneumococcal growth can remain unbounded causing 100% mortality in mice within 5 days at higher inocula (Bergeron et al., 1998; Duong et al., 2001; Fillion et al., 2001), indicating a limit to the phagocytic capacity of all three types of cells (Clawson and Repine, 1976; Onofrio et al., 1983) and a potential for significant inflammation to occur.

<a id='177f2e46-0096-4a45-9599-a486f7a58b52'></a>

These phenomena suggest that a three-stage phagocytic response is critical for clearance of larger inocula and that skewing of the innate response may have a profound impact on the outcome. Although it is known that effective phagocytosis is not the only factor determining

<a id='8bb40f60-d5da-47c9-9460-a183c183efc1'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='2f177b4a-c900-4c56-9c81-54f0ed6125a4'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='dfd86d85-46ab-482e-9426-9ec22c5b886a'></a>

Smith et al.

<a id='6e71c54a-144d-4e21-bf77-5a40ca18207c'></a>

Page 3

<a id='b0c96fa7-a4eb-4893-9256-e97685a58b1c'></a>

pneumococcal pathogenesis, we aim here to capture some of the complexities of the innate
immune response to pneumococcus by developing mathematical models for the three-stage
phagocytic response and testing them with data on artificially infected mice.

<a id='a7d906a8-d184-4b4b-b334-88986d76e2c7'></a>

## 1.2. Mathematical Models of Bacterial Kinetics

Previously published mathematical models of bacterial kinetics and inflammatory processes present a conceptual framework to examine two phenomena of interest here (Lauffenburger, 1985; Pilyugin and Antia, 2000; Reynolds et al., 2006; Rudnev and Romanyukha, 1995): (i) the initial dose threshold, and (ii) the observed variations in outcome (clearance vs sustained growth). These studies (described below) use systems of ordinary differential equations to describe bacterial pathogenesis and often divide phagocytic cells into a variety of different subpopulations. To address these behaviors, one study split the macrophage population into cells that are in a free state (i.e., not associated with bacteria) and cells that are engaged in active phagocytosis of bacteria (Pilyugin and Antia, 2000), and suggested that the "handling" time of bacteria limited the ability of macrophages to fully eradicate a bacterial population.

<a id='90772d48-7e59-4c13-90a7-308fc53e19fd'></a>

Other models include two separate subsets of phagocytes, neutrophils and macrophages (Lauffenburger, 1985; Rudnev and Romanyukha, 1995), and show that different behaviors are possible with various initial conditions. However, the models did not have these cells arriving sequentially, and the macrophage response included either only recruited macrophages (Rudnev and Romanyukha, 1995) or a single equation combining resident alveolar macrophages and MDMs (Lauffenburger, 1985). More commonly, however, models include only one subset of phagocytes. For example, a single type of macrophage was useful in a model that evaluated the importance of prolonged inflammation in the context of sepsis, and emphasized antiinflammatory cytokines and tissue damage as the factors influencing infection outcomes (Reynolds et al., 2006).

<a id='05746a13-db7d-4f3f-80a8-1beed9408c3d'></a>

Many of these models describe "generic" bacterial dynamics. However, differences among bacterial species render most prior formulations inappropriate for a pneumococcal lung infection. In particular, the succession of neutrophil and MDM accumulation depends on bacterial type and differs between various gram-positive bacteria and gram-negative bacteria (Schluger and Rom, 1997; Toews et al., 1979). For example, an infection with *Pseudomonas aeruginosa* (gram-negative) is similar to pneumococcus (gram-positive) in that neutrophils are the predominant phagocyte. However, neutrophils may appear simultaneously with MDMs during infections with *Klebsiella pneumoniae* (gram-negative) and *Staphylococcus aureus* (gram-positive) (Toews et al., 1979). This variation has been attributed to a distinct, but partially overlapping, set of cytokines induced by different species during bacterial colonization (Schluger and Rom, 1997).

<a id='b3b64a5d-a793-4302-bfcc-c2d6a1358f49'></a>

Few existing models have sufficient experimental data for validation and parameterization,
and no models specific to *S. pneumoniae* have been developed. We capitalize on the power
and convenience of the mouse model system to compare the kinetics of three bacterial doses
over the course of an infection and infer possible interactions between pneumococci and
host immune responses. We infected groups of BALB/cJ mice with three different inocula
of *S. pneumoniae* strain D39 and obtained bacterial measurements from the lungs of
individual mice.

<a id='bffe9b76-30e7-445e-a0bb-f56086495880'></a>

Using these data as a guideline, we develop mathematical models that describe the kinetics
of each of the three stages. We find a single equation that characterizes the alveolar
macrophage response, and use this equation to determine how an initial dose threshold
arises. We then extend the model to incorporate proinflammatory cytokine production and
the resulting neutrophil recruitment, and establish that two outcomes, clearance or sustained

<a id='da82fd0c-8dc7-4ba9-8a6b-30abb7d92818'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='9d37971a-3922-40ce-b3c4-cb36ddd46aa6'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='5da535e4-f7f3-4835-82b3-3b1c1cabf209'></a>

Smith et al.

<a id='73c0bc76-c352-437b-b33f-b3f494b72366'></a>

Page 4

<a id='1c6402d9-5d8b-42c2-b8ae-3cf5754f3a48'></a>

bacterial growth, are possible. Lastly, we examine the possibility of bacterial clearance given an influx of monocyte-derived macrophages. Through each of these models, we gain a better understanding of the extent to which AMs, neutrophils, MDMs, proinflammatory cytokines, and apoptotic cellular material ("debris") contribute to the initiation and resolution of a pneumococcal lung infection.

<a id='fdf706ff-a653-4891-919e-2caf84ccd015'></a>

## 2. Experimental Data
### 2.1. Methods and Materials

<a id='0f18bc18-bb4e-48f2-ae63-afdb0f723097'></a>

### 2.1.1. Mice
Adult (6-8 wk old) female BALB/cJ mice were obtained from Jackson Laboratories (Bar Harbor, ME). Mice were housed in groups of 4-6 mice in high-temperature 31.2 cm x 23.5 cm x 15.2 cm polycarbonate cages with isolator lids. Rooms used for housing mice were maintained on a 12:12-hour light:dark cycle at 22 ± 2° C with a humidity of 50% in the biosafety level 2 facility at St. Jude Children's Research Hospital (Memphis, TN). Prior to inclusion experiments, mice were allowed at least 7 days to acclimate to the animal facility. Laboratory Autoclavable Rodent Diet (PMI Nutrition International, St. Louis, MO) and autoclaved water were available ad libitum. All experiments were performed in accordance with the guidelines set forth by the Animal Care and Use Committee at St. Jude Children's Research Hospital.

### 2.1.2. Infectious Agents and Model
S. pneumoniae strain D39 (type 2) was transformed with the lux operon (Xenogen) (McCullers and Bartmess, 2003). For infection experiments, bacteria were diluted in sterile phosphate buffered saline (PBS) and administered at a dose of 10^4, 10^5 or 10^6 colony forming units (CFU) intranasally to groups of 6 mice lightly anesthetized with 2.5% inhaled isoflurane (Baxter, Deerfield, IL) in a total volume of 100µl (50µl per nostril). Mice were weighed at the onset of infection and each subsequent day for illness and mortality.

### 2.1.3. Lung Titers
Mice were euthanized by CO2 asphyxiation. Lungs were aseptically harvested, washed three times in PBS, and placed in 500µl sterile PBS. Lungs were mechanically homogenized using the Ultra-Turrax T8 homogenizer (IKA-werke, Staufen, Germany). Lung homogenates were pelleted at 10,000 rpm for 5 minutes and the supernatants were used to determine the bacterial titer for each set of lungs using serial dilutions on tryptic soy-agar plates supplemented with 3% (vol/vol) sheep erythrocytes.

<a id='81693fcc-2725-438c-a053-d7c8bdde394a'></a>

## 2.2. Experimental Results

Infecting mice with an initial inoculum of 10^4 CFU resulted in undetectable bacterial lung titers 4 hours pi. We found that a dose above 10^4 CFU is necessary to induce a pneumococcal lung infection with the type 2 strain D39. The groups of mice given an initial dose of 10^5 CFU had bacterial titers initially increase exponentially for 8 hours, drop briefly at 16 hours pi then reach peaks up to 5.8 x 10^7 CFU/ml lung homogenate at 24 hours pi. Bacterial lung titers then declined rapidly and, in all but one sample, became undetectable at 48 hours pi. All mice in the 72-hour group had completely cleared the infection (Figure 1).

<a id='770fbb7f-3f35-4eea-8315-b29399ee58e0'></a>

Mice inoculated with 106 CFU had bacterial titers at significantly high levels by 4 hours pi, which reached peaks as high as 2.3 × 108 CFU/ml lung homogenate by 16 hours pi. Titers began to decline thereafter; however, clearance slowed between 24 and 48 hours pi. The infection was not cleared in these mice, which showed sustained bacterial titers 72 hours pi (Figure 1). Elevated bacterial titers over several days coupled with significant weight loss (data not shown) suggested these mice had severe pneumonia. All but one mouse (72-hour group) survived the experiment.

<a id='6e914be2-a164-48d9-a39b-f14bd34ae9bd'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='8effc7c0-5d2e-4ffd-8aaf-a4278c2e76ca'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='2212193f-d5b5-4b7a-8b64-871d5c137ebe'></a>

Smith et al.

<a id='5f607dfe-0463-422d-a51a-aba7b1a1585e'></a>

Page 5

<a id='be4e7af6-734c-49a0-af96-02b77b36931d'></a>

### 3. Mathematical Model
#### 3.1. Methods and Materials
Numerical simulation of model equations was done in Matlab using the ordinary differential equation (ODE) solver _ode45_ for the alveolar macrophage model and the neutrophil model, and using the delay differential equation (DDE) solver _dde23_ for the monocyte-derived macrophage model. Parameter values used to simulate each model are given in Tables 1-3 and descriptions of the chosen values are given in the text.

<a id='46798f92-a6a2-40f3-b367-e46df6a92e99'></a>

## 3.2. Stage 1: The Alveolar Macrophage Response
Alveolar macrophages are part of the initial host defense that respiratory pathogens encounter when entering the airway. These cells are thought to tightly regulate growth of small pneumococcal populations but become insufficient with larger initial inocula. This limitation may explain the dependency of initial acquisition on inoculum size, as both we and others have found for a pulmonary pneumococcal infection (Sun and Metzger, 2008).

<a id='71debee4-c299-45ea-aaa2-b9ee1a672eef'></a>

To investigate the dosage threshold, we developed a mathematical model (Equation (2)) that depicts the interaction between a pneumococcal population (P) and the resident alveolar macrophages (M_A). Pneumococci grow logistically at a rate r per hour with a maximum tissue carrying capacity, Kp CFU/ml, and are phagocytosed at rate \gamma_{MA}f(P, M_A) per cell per hour, where

<a id='66deaf59-ec57-4625-8c40-43e3ceb82c03'></a>

f(P, M_A) = \frac{n^x M_A}{P^x + n^x M_A} (1)

<a id='872c6900-ad78-4d61-9c17-01bb28831afb'></a>

Equation (1) represents a decrease in phagocytosis with large pneumococcal population size. The shape parameter _x_ describes the rate of consumption of pneumococci (Figure 2(a)). The value of _n_ gives the ratio of bacteria to alveolar macrophages, with large values describing a higher phagocytosis rate for a given inoculum size (Figure 2(b)).

<a id='0024c114-7bba-496d-8a6f-bf1e42e7a2b6'></a>

Although alveolar macrophages were once thought to locally proliferate rather than derive from blood monocytes (Coggle and Tarling, 1982, 1984; Tarling et al., 1987), recent studies do not support this view (Murphy et al., 2008; Taut et al., 2008). We assume AMs are supplied at a constant rate of s cells per hour with a clearance rate d, for simplicity. We do not consider pneumococcal-induced death of AMs (Maus et al., 2004) as this effect would likely be minimal in the early stages of infection kinetics. Alveolar macrophage population dynamics are slow compared to bacterial clearance, so we take these cells to be in quasi-steady state such that M*~A~=s/d.

<a id='4d8f918f-1068-48f2-8d20-08419be876a2'></a>

We term this model "the alveolar macrophage model", which has dynamics described by a single equation for the pneumococcal population,

<a id='1d46c30d-17e8-41f0-b03d-8e6312363936'></a>

dP/dt = rP(1 - P/K_P) - γ_{MA} f(P, M_A^*) M_A^* P. (2)

<a id='ac774122-b79c-4d10-b843-85720073d423'></a>

### 3.2.1. Parameter Identification—We did not use a sophisticated scheme to estimate parameter values because this model is designed to capture only the initial dose threshold and would fit at most 1-2 data points. We instead use parameter values available in the literature where possible and selected others to match the data by tuning values based on biologically feasible ranges (Table 1).

<a id='d8970b8d-bc31-4deb-9de7-277966c1d523'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='d425f727-5586-42ba-9976-c092ce895cdb'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='9ff50e02-5001-4514-814a-024824a0ee15'></a>

Smith et al.

<a id='467a8938-4a55-4bba-aff9-e233ff5423ea'></a>

Page 6

<a id='52f2ec9c-1a65-46f3-9e4c-80e38823ea7a'></a>

We set the steady state value of alveolar macrophages to M*\_A\_ = 10⁶ cells, the estimated number that reside in a murine lung (van Oud Alblas and van Furth, 1979). Estimates of the turnover rate of alveolar macrophages range from 10-40 days (Coggle and Tarling, 1982; Godleski and Brain, 1972; van Oud Alblas and van Furth, 1979), although recent evidence suggests a longer life-span (Murphy et al., 2008). This corresponds to 0.001 ≤ d ≤ 0.0042 implying s = 1.0-4.2 × 10³ cells per hour. Based on the maximum bacterial titer measured in our own experiment, we fix Kp = 2.3 × 10⁸ CFU/ml.

<a id='2037cdd9-01e1-46bc-a3d7-b6df50dcf6aa'></a>

The three initial values of pneumococci (P0) were chosen as 10³, 10⁴, and 10⁵ CFU/ml. The units of these values (CFU per ml of lung homogenate) differ from the units of initial inocula (CFU) used in the experiments. We assume only a portion of bacteria reach the lungs since some bacteria could be quickly trapped in the airway and removed by mucocilliary mechanisms. These values were chosen such that the data could be reproduced and to correspond to the three doses mice were infected with, i.e., 10⁴, 10⁵, and 10⁶ CFU.

<a id='d5ef9fab-b3f1-4d45-b1fe-ab145dca800a'></a>

The doubling time of pneumococcal strain D39 is estimated to be 84 minutes when injected intravenously in a mouse model of sepsis (Benton et al., 1995). In contrast, the calculated doubling time in blood media is 20-30 minutes (Todar, 2002). Because we could not establish an exact value of the growth rate in the lung, we explored values between 20-84 minutes to determine which produced the best fit. We chose r = 11.3 \u00d7 10\u207b\u00b9 per hour, corresponding to a doubling time of approximately 37 minutes.

<a id='2bf8369d-55f7-40af-bee6-7f438e213726'></a>

The maximum number of pneumococci associated with an alveolar macrophage (_n_) was set to 5 CFU/ml per cell, based on a study that found, on average, 5 pneumococci bound to each human AM (Gordon et al., 2000) and since the lung homogenate is typically 1-1.5 ml. We fix the degree of nonlinearity (_x_) in the function _f_(_P_, _M_<sub>A</sub>) to a value of 2 based on our experimental findings that phagocytosis is decreased for initial inocula greater than 10<sup>4</sup> CFU (i.e., 10<sup>3</sup> CFU/ml). Lastly, we found that _γ_<sub>MA</sub> = 5.6 × 10<sup>-6</sup> per cell per hour (i.e., _γ_<sub>MA</sub> _M_<sub>A</sub> = 5.6 per hour) could predict the observed bacterial titers. We find this value reasonable as the estimated killing rate of _S. aureus_ by neutrophils is 6.9 per hour (Hampton et al., 1994).

<a id='f710f392-c566-4207-9819-d95d94f7fc3d'></a>

3.2.2. Results - Alveolar Macrophage Model—We solved Equation (2) numerically with the parameter values specified in Table 1. For an initial pneumococcal value of P0 = 103 CFU/ml, the number of resident alveolar macrophages is large enough that bacterial titers decline immediately (Figure 3). A dose one log higher (P0 = 104 CFU/ml) results in a short lag (~3 hours) in bacterial growth as AMs initially limit exponential bacterial replication. Shortly after, however, pneumococci overwhelm the AM response and reach a steady-state value of P(t) = Kp. This slowed initial growth phase is not evident with a higher initial value (P0 = 105 CFU/ml) where immediate bacterial growth occurs.

<a id='beaa57d1-a5a3-4f81-80c1-4e18e7868066'></a>

These results imply that a decreased ability of resident alveolar macrophages to efficiently phagocytose large densities of pneumococci can produce a dosage threshold. Our model predicts that bacterial titers would quickly reach a maximum capacity which could then result in death of the host without additional components of the immune response.

<a id='c5520843-8c4b-4f39-a082-9c80e4743cd6'></a>

3.3. Stage 2: The Neutrophil Response

Using the alveolar macrophage model, we found that resident alveolar macrophages could provide protection against a low-dose challenge of pneumococci, partial clearance of an intermediate dose, but no visible effects on a high-dose challenge (Figure 3). When AMs cannot control bacterial growth through phagocytosis, their main effect switches to modulating the inflammatory response by recruiting neutrophils to the infected lung (Jones et al., 2005; Mizgerd et al., 1996). We build upon Equation (2) to incorporate

<a id='4e00889d-ff46-4d5a-87ff-e290fc8c46f9'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='116e4e4f-8ec9-41b3-bc60-ddf1477e2a37'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='f028ff34-56a9-4f81-8f3d-14789b82a63d'></a>

Smith et al.

<a id='e8aa695d-a3b6-4bff-ae05-5ea4475167f0'></a>

Page 7

<a id='c6fbea78-1e4d-485f-83ba-9eb2cf3148d9'></a>

proinflammatory cytokine production that induces neutrophil migration and further phagocytosis of pneumococci.

<a id='61673530-f686-4b79-a6ec-20a6235758a3'></a>

### 3.3.1. Cytokine Production
Pneumococcal entry into the lung prompts the release of proinflammatory cytokines such as IL-1 and TNF- (Bergeron et al., 1998). Alveolar macrophages produce a wide array of cytokines (Monton and Torres, 1998), and alveolar epithelial cells also secrete cytokines following pneumococcal attachment and/or cytotoxic injury (Maus et al., 2004; McRitchie et al., 2000; Stadnyk, 1994). Both IL-1 and TNF-α have been shown to increase rapidly during a pneumococcal infection, peaking 12 hours pi and then declining (Bergeron et al., 1998).

<a id='c4bb58dc-2f27-4051-8e97-d100c9870d32'></a>

Although these two cytokines have slightly different kinetics (Bergeron et al., 1998), we include both as the single variable _C_ (Equation (9)). We divide the alveolar macrophage class into two subsets: _M_R, representing AMs in a resting state that are not releasing cytokines, and _M_C, representing AMs actively secreting cytokines. Alveolar macrophages in the _M_R class become activated at rate _θ_M _P_ due to interaction with bacteria and are deactivated at rate _κ_ per hour. Equations (3)-(4) are the subsystem describing this process,

<a id='476f2e07-9c80-49ca-81ae-a077d6cdf4af'></a>

$$\frac{dM_R}{dt} = s - dM_R - \theta_M PM_R + \kappa M_C$$ (3)

<a id='6adc1ba4-a830-49d7-b6ef-e3d02e3bda4e'></a>

dM_C / dt = θ_M P M_R - κM_C - dM_C. (4)

<a id='0e18bbc1-642d-4424-be3e-5a4ac31f497d'></a>

We assume that the total AM population remains constant, $M_A^* = M_R + M_C$, and that the activation process is rapid when AMs encounter pneumococci. Thus, the number of alveolar macrophages that release cytokine is

<a id='783be4ea-cc02-4450-b45e-0ae02769c4dd'></a>

M*C = (θM PM*A) / (d+κ+θM P)
(5)

<a id='cd486f87-5f5a-4044-abf7-2fa8a67d07fb'></a>

when we assume that the $M_C$ population reaches a quasi-steady state. The rate of cytokine production from these cells is v pg/ml per hour.

<a id='730c7b04-2423-47b2-a0e7-399d384b216e'></a>

To model cytokine production from tissue injury, we consider two populations of epithelial cells: target cells not associated with pneumococci ($E_U$, Equation (7)) and cells with pneumococci attached to cell surface receptors ($E_A$, Equation (8)). Following acute lung injury, little epithelial cell regeneration occurs within 3-5 days (Adamson et al., 1988; Ramphal et al., 1980), so we do not consider a source of new target cells. Pneumococci adhere to cells at a rate $\omega P$ per hour. Cells with bacteria attached are lost, either from toxic effects of the bacteria or by immune-mediated mechanisms, at a rate $d_E$ per hour. Cytokines are produced at a rate $\alpha$ pg/ml per hour from epithelial cells and are degraded at a rate $d_C$ per hour.

<a id='5164b839-88b5-4713-95a0-6373ac748af4'></a>

Antiinflammatory cytokines (e.g., IL-10) and other signaling molecules (e.g., nitric oxide (NO)) produced by alveolar macrophages and neutrophils during a pneumococcal infection aid regulation of the inflammatory process (Bergeron et al., 1998; Bingisser and Holt, 2001; Marriott et al., 2004; van der Poll et al., 1996; Thomassen et al., 1997). For simplicity, we do not explicitly include products such as IL-10 or NO in our model. Instead, we incorporate

<a id='4a901c4b-83c0-4952-be17-5a1a29947e29'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='030b2750-6418-4f40-bb50-1bdedb5c5fdd'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='189ad982-119a-41ab-8464-29a1b5802b2e'></a>

Smith et al.

<a id='73c40d5d-a72b-41f1-848b-c93c1fcf6546'></a>

Page 8

<a id='33ba704c-caa8-49c4-9648-54dc00ac9304'></a>

cytokine inhibition from neutrophil (N) effects by reducing production by a factor of 1 +
k_nN.

<a id='33082154-4712-4b83-a01a-17df61bd1892'></a>

**3.3.2. Neutrophil Recruitment**—The signaling from proinflammatory cytokines recruits neutrophils (_N_, Equation (10)) at a rate η cells per pg/ml per hour which are then cleared at a rate _d_N per hour. We do not include a limitation of the phagocytic rate (γ_N_) of neutrophils but we do set the maximum number of neutrophils present in the lung at _N_max.

<a id='f478b3af-6f5c-4110-ab7e-610da9786806'></a>

Neutrophil exposure to pneumococci results in apoptosis and, at high inocula, necrosis (Zysk et al., 2000). The effect of this process is two-fold. First, phagocyte apoptosis following bacterial colonization decreases inflammation and contributes to host recovery (DeLeo, 2004). Alveolar macrophages play an integral role in the clearance of the dead material and debris from the airway (Dockrell et al., 2001, 2003). However, when apoptotic and necrotic material is not efficiently removed, tissue damage increases and bacterial growth may be increased.

<a id='278004e7-e4ad-4e0e-bb5f-7be8e3e47525'></a>

We incorporate both the influence of pneumococcal-induced neutrophil apoptosis ($d_{NP}$) and the role of alveolar macrophages in this process. To understand the effect of cell death on pathogenesis, we introduce a state variable to account for the accumulation of debris ($D$, Equation (11)), which has arbitrary units. In our model, neutrophil death, both natural and bacterial-induced, and the death of epithelial cells translate into debris at rates $\rho_1$, $\rho_2$ and $\rho_3$ per cell, respectively. Alveolar macrophages then eliminate excess debris at a rate $d_D$ per hour. While AMs are engaged in clearing the airway of dead material, we assume their ability to phagocytose pneumococci is inhibited by a factor $1+k_dDM_A^*$

<a id='1a4d40b3-3a14-47dc-9537-dc8d3b75e580'></a>

Together, these dynamics result in "the neutrophil model" given by

<a id='ceecb132-8670-486d-8a0c-61198ceeaae2'></a>

$$\frac{dP}{dt} = rP\left(1 - \frac{P}{K_P}\right) - \frac{\gamma_{M_A} f(P, M_A^*)}{1 + k_d DM_A^*} M_A^* P - \gamma_N NP \quad (6)$$

<a id='21a4d9c0-5b6a-412f-825b-54e859c8d148'></a>

$$\frac{dE_U}{dt} = - \omega PE_U \quad (7)$$

<a id='ff9e93dc-a2aa-4908-b30d-d193070da892'></a>

dE_A / dt = ωPE_U - d_E E_A (8)

<a id='fff8ae30-0982-47f6-be66-21e0cf578f79'></a>

$\frac{dC}{dt} = \alpha \frac{E_A}{1+k_nN} + \nu \frac{\theta_M PM_A^*}{(d+\kappa+\theta_MP)(1+k_nN)} - d_cC \quad (9)$

<a id='572a0a0b-d96d-41ac-aacb-aa7aa877c4d4'></a>

$$\frac{dN}{dt} = \eta C\left(1 - \frac{N}{N_{max}}\right) - d_{NP}NP - d_N N \quad (10)$$

<a id='4de8699c-9af9-4b07-8809-6fd391a6d910'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='61e0579c-87b6-433f-8525-3d2b79220377'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='eb7ae518-d1c0-497d-8734-43b64f88209a'></a>

Smith et al.

<a id='65d1c440-843f-4964-971e-c898cc55113a'></a>

Page 9

<a id='898d4177-c0e2-4b96-b80c-c9c9724680b9'></a>

$\frac{dD}{dt}=\rho_1d_{NP}NP+\rho_2d_NN+\rho_3d_EE_A-d_DDM_A^*.$ (11)

<a id='75056c01-71a3-41f3-b85e-e4dec5a5d590'></a>

3.3.3. Results - Neutrophil Model—The large number of parameters in our model restricts our ability to fit Equations (6)–(11) to the data. Therefore, most parameter values were chosen based on searches in biologically realistic ranges that matched the data, although we fix some values (dC and dN) based on estimates reported in the literature (Gloff and Wills, 1992; Malech, 2007). The initial number of epithelial cells was set at EU(0) = 108 cells, based on a calculation of the number of cells residing in the murine lung (Stone et al., 1992), and the initial values of the remaining state variables (C, N, and D) were set to zero. All other parameter values are listed in Table 2.

<a id='bcf20778-4ae0-4997-94a0-ede82152d08d'></a>

Simulating Equations (6)-(11) with three different initial pneumococcal conditions (10³, 10⁴ and 10⁵ CFU/ml) shows three distinct outcomes (Figure 4a). A low dose, P₀ = 10³ CFU/ml, is immediately cleared by alveolar macrophages and does not result in noticeable cytokine production or neutrophil recruitment (Figure 4c,b).

<a id='ee98d616-b9b6-40c9-8820-d70adf1bcb70'></a>

At an intermediate value (_P_0 = 10^4 CFU/ml), the lag in bacterial growth initially from clearance by alveolar macrophages is reinforced by the appearance of neutrophils in the lung, which extends the delay in exponential bacterial growth from 3 hours to 6 hours (Figure 4a). Proinflammatory cytokine production is initially slow but increases rapidly thereafter and reaches a peak 24 hours pi (Figure 4c). These dynamics agree with experimental measurements of both IL-1 and TNF-α (Bergeron et al., 1998). Paralleling cytokine dynamics, neutrophils increase rapidly and peak 36 hours pi before slowly declining over several days (Figure 4b), also consistent with empirical observations (Fillion et al., 2001). The migration of neutrophils into the infection site effectively controls bacterial growth, which peaks 16 hours pi. Elimination of bacteria slows between 48-72 hours pi corresponding to a decrease in neutrophil numbers. At this time, alveolar macrophages are freed up from debris removal and return to phagocytosis of pneumococci. It is unclear whether or not this occurs biologically; however, it is possible that AMs are responsible for the completion of bacterial eradication. During the course of the infection, only a fraction (~65%) of epithelial cells are killed as a result of bacterial adherence (Figure 4e,f).

<a id='3eaa281b-137c-4e94-9e30-dbef7eae270a'></a>

The neutrophil response is not sufficient to clear a high dose inoculation. For P0 = 105 CFU/ ml, bacterial growth slows briefly within 3 hours pi in accordance with a sharp rise in both neutrophils and proinflammatory cytokine concentration (Figure 4a,b,c). However, pneumococcal-induced neutrophil apoptosis results in an equally sharp decrease of these phagocytes. At this point, 24 hours pi, bacterial titers rise quickly and reach the maximum tissue carrying capacity (Kp). In addition, a significant amount of debris results from both the cytotoxic effects on neutrophils and epithelial cells. In this case, all target cells are killed by pneumococcal attachment.

<a id='4e6fb8c4-a57f-421f-ba7a-791167ac6a39'></a>

We next simulated Equations (6)-(11) with additional values of P0 to determine the extent to which outcomes are altered with small changes in the initial condition. As illustrated in Figure 5, the alveolar macrophage response is sufficient for all initial values under P0 = 10^4 CFU/ml and bacterial titers decline rapidly. However, for initial conditions larger than P0 = 10^4 CFU/ml, bacteria grow exponentially with an evident lag phase in only a small region around this value. The length of time that bacterial growth is controlled by neutrophils decreases as P0 increases, with complete clearance possible below some critical value of P0 (3.98 x 10^4 CFU/ml, compared to 9.99 x 10^3 with AMs only). These dynamics correspond

<a id='25efebc5-c938-464d-bfd7-70f25c0cafcf'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='a8bc0088-0771-49c4-a210-983937e07dbf'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='51ad5e75-9716-4446-8c91-ba4239bbd0b6'></a>

Smith et al.

<a id='41fdc038-797f-4703-86fe-a99e7bf5a920'></a>

Page 10

<a id='9059f3cb-47f5-4515-a796-16fa28084117'></a>

to an unstable equilibrium between _P_(_t_) = 0 and _P_(_t_) = _K_p, although we were not able to find
this value analytically.

<a id='8262d348-084e-4675-8920-068e6d93acbf'></a>

### 3.4. Stage 3: The Monocyte-Derived Macrophage Response

Although neutrophils dominate the early cellular influx of leukocytes (i.e., white blood cells) into sites of pulmonary pneumococcal infections (Mizgerd et al., 1996), these cells are replaced by monocyte-derived macrophages later during inflammation (Fillion et al., 2001). The shift to MDM recruitment is thought to be triggered by the release of soluble factors from neutrophils (Doherty et al., 1988). However, other studies suggest the switch may be the result of MDM response to chemokines produced by tissue cells (Henderson et al., 2003) or regulation by the cytokine IL-6 (Kaplanski et al., 2003). The delayed appearance of MDMs also correlates with macrophage-colony protein 1 (MCP-1) production (Fillion et al., 2001), NO release (Bergeron et al., 1998), and bacterial formyl peptide production (Fillion et al., 2001), many of which are either influenced by or directly produced by neutrophils (Cassatella, 1995).

<a id='1364a135-21dd-451d-8304-3c210878db37'></a>

Rather than including the dynamics of cytokines such as IL-6, MCP-1, or NO, we assume MDM recruitment is proportional to the neutrophil population. Furthermore, we found it beneficial to assume that MDMs appear τ time units after neutrophils at a rate ζ per hour, where the number of macrophages cannot exceed Mmax (Equation (18)). Clearance of these cells occurs at a rate dm per hour. We exclude macrophage apoptosis in response to the bacterial challenge since it has been shown to be delayed (Dockrell et al., 2001; Marriott et al., 2004). We also exclude the contribution of macrophage death to debris assuming that the effect is small. Recruited macrophages phagocytose pneumococci at a rate γm per cell per hour. Combining these dynamics with Equations (6)-(10) results in “the monocyte-derived macrophage model” which describes all three stages of phagocytosis,

<a id='da345f74-1c5f-47a9-9850-b1872c7000af'></a>

$$\frac{dP}{dt} = rP\left(1 - \frac{P}{K_p}\right) - \frac{\gamma_{MA} f(P, M_A^*)}{1+k_d DM_A^*} M_A^* P - \gamma_N NP - \gamma_m MP \quad (12)$$

<a id='4f0099f9-0980-4fdf-9ba1-fc9f64e25472'></a>

$$\frac{dE_U}{dt} = - \omega PE_U$$ (13)

<a id='a41994ee-8702-4725-a983-6bddd7b673e3'></a>

dE_A = \omega PE_U - d_E E_A (14)
dt

<a id='1d5b0a92-0d4a-4382-adcc-d3ffb9fb31d2'></a>

dC/dt = α (E_A / (1 + k_n N)) + v (θ_M P M*_A / ((d + κ + θ_M P) (1 + k_n N))) - d_C C (15)

<a id='d37eac5a-3d56-40e0-b903-780502836d37'></a>

dN/dt = ηC(1 - N/Nmax) - dN N - dNP NP (16)

<a id='7e0a2f2f-a85f-4a1f-b8fb-d2732a9736ff'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='deb773da-0107-442a-9b24-7b7dd3459db9'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='c1d9d8cd-b45a-4f82-a1ae-60e674b64b2e'></a>

Smith et al.

<a id='bf93ace6-f7e3-4eef-b47f-2eedb4f92107'></a>

Page 11

<a id='eb20cdc9-1856-4be6-8005-7132bd7b026f'></a>

$$\frac{dD}{dt} = \rho_1 d_{NP} NP + \rho_2 d_N N + \rho_3 d_E E_A - d_D DM^*_A \quad (17)$$

<a id='97827168-4cba-40bb-8730-26c50e950c21'></a>

$$\frac{dM}{dt} = \xi N(t - \tau)\left(1 - \frac{M}{M_{max}}\right) - d_m M. \quad (18)$$

<a id='95e4f1b8-8744-4cf6-95ed-14c8bc6018b4'></a>

3.4.1. Results - Monocyte-Derived Macrophage Model—With parameters in Table
3, this model exhibits the observed behavior of bacterial kinetics for all three initial
conditions of pneumococci (Figure 6a). Recruited macrophages (Figure 6d) are evident
starting at 24 hours pi and peak between 72 and 96 hours pi for an intermediate initial value
of pneumococci (10⁴ CFU/ml). This is consistent with experimental findings (Fillion et al.,
2001) and corresponds to successful elimination of bacteria, which occurs 24 hours earlier
with these cells present than with neutrophils and AMs only. Furthermore, the threshold
value of P₀ such that bacterial eradication occurs is 2.5 times more when macrophages are
recruited than with neutrophils and AMs only (9.97 w 10⁴ vs 3.98 w 10⁴ CFU/ml). For high
initial numbers of pneumococci (10⁵ CFU/ml), these cells continue to increase until a peak
is reached 9 days pi (not shown in Figure 6), reducing pneumococcus numbers without
achieving complete clearance. This extended infection with the resulting prolonging of the
neutrophil response (Figure 6c) indicates significant inflammation.

<a id='09058b65-103b-46df-b181-678df7ccbaa8'></a>

The complexity of our model restricts our ability to fully investigate individual parameter values; however, perturbations in many of the model parameters may significantly influence the dynamics of each stage and reflect differences in the host and the pathogen. Performing a differential sensitivity analysis (see (Bortz and Nelson, 2004; Eslami, 1994; Frank, 1978)) highlights several important aspects of the dynamics (details in the Supplementary File).

<a id='4916e4e1-bdce-4541-8737-505f30ab2d1e'></a>

Changes in bacterial clearance can be the driving force behind a rapid and favorable resolution. As such, altering either of the two of the parameters controlling clearance, $\gamma_N$ and $\gamma_m$, influences the dynamics. The importance of neutrophils in the early stages of bacterial control is confirmed by the differences observed early in the infection with changes in the rate of bacterial clearance by neutrophils ($\gamma_N$) (Supplementary Figures S1 and S2). Furthermore, this effect is more pronounced and for high initial inocula (i.e., $P_0 = 10^5$ CFU/ml). On the other hand, changes in the rate of bacterial clearance by macrophages ($\gamma_m$) influences dynamics later in the infection and to a lesser extent (Supplementary Figures S5 and S6), with little effect when $P_0 = 10^4$ CFU/ml. In general, parameters related to recruited macrophages ($\gamma_m$, $\xi$ and $\tau$) are relatively insensitive to changes with intermediate or low initial values of pneumococci since these cells only aid bacterial clearance later in the infection when bacteria is low.

<a id='0b7c913c-445d-4029-8865-c93af935d228'></a>

Perturbing factors related to inflammation can also result in dynamical differences. One important parameter with the ability to alter infection kinetics is the rate of neutrophil apoptosis due to bacterial cytotoxicity ($d_{NP}$). However, for high initial inocula, the kinetic effect of an increase in this parameter can be balanced with an increase in the rate of neutrophil recruitment ($\eta$) (Supplementary Figure S1). Other parameters pertaining to inflammation are those which control debris ($\rho_1, \rho_2, \rho_3, d_D$ and $k_D$), but these parameters are insensitive for both intermediate (except $k_D$) and high initial initial inocula (Supplementary Figures S7 and S8).

<a id='ace478d4-2344-4d0f-af24-3efc5d800850'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='0dca6bfb-ca79-4228-95c1-16d947f89337'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='8a434e26-d28b-4dc4-9c42-680a80c950a5'></a>

Smith et al.

<a id='5ca3692b-0218-4cd0-b3e1-e038c5e7be1c'></a>

Page 12

<a id='ea07652c-cb91-4c1b-b469-e1d47c0c7c23'></a>

## 4. Discussion

<a id='b5e885c8-5794-49e3-a1c3-d0661ed28673'></a>

When a pneumococcal infection overcomes the innate immune defenses, bacterial pneumonia can result. There are many factors, including virulence of bacterial strain and host defense status, that determine the eventual outcome of a bacterial challenge to the lung. Developing a basic model of acute pulmonary bacterial infection kinetics that could then be expanded or modified to address specific bacterial pathogens would be ideal. However, establishing the appropriate simplifications to be made is challenging and no generalized model may be sufficient given the variability of immune control and modulation by different bacterial species.

<a id='87f372f1-762a-4cc7-b143-04cfc6149b26'></a>

We developed a series of models to gain a deeper understanding of how the different layers of host defense in the lower respiratory tract, including physical barriers, resident cells and recruited cells, combine to fight a pneumococcal lung infection and to address the two thresholds observed given the inoculum size: establishment and eradication. Through our experiments and models, we were able to successfully capture the qualitative behavior of the data and identify key steps.

<a id='49ef43f1-32e7-4898-a59a-83aca4190083'></a>

The initial dose threshold was evident through the use of a single equation that took into account a decrease in phagocytosis by alveolar macrophages as bacterial numbers increase, consistent with the view that these cells are sufficient to clear only small densities of pneumococci. Following the first few hours of infection, more complicated dynamics occur. With the neutrophil model, both clearance or sustained growth of bacteria are possible and are dependent on whether alveolar macrophages are engaged in phagocytosis or debris removal, which was correlated to the amount of pneumococcal-induced neutrophil apoptosis. Thus, alveolar macrophages may play a critical role in both establishment and complete eradication of a bacterial infection.

<a id='8121d368-f487-4df2-ac72-4bc49542c611'></a>

While the neutrophil response is rapid, pneumococcal-induced apoptosis of these cells could result in an equally rapid contraction phase. Normal resolution in the lung includes the apoptosis of neutrophils, but this may also be a significant source of inflammation if the debris is not efficiently cleared. Furthermore, the effects of neutrophil death can be negated with an increase in neutrophil recruitment, but these events combined may still be harmful even though bacterial numbers would not be a ected. This effect is further enhanced with the appearance of macrophages, which contribute to both bacterial clearance and respiratory tract inflammation.

<a id='b828c5eb-4610-472d-9dc6-84fe5c8fafed'></a>

Understanding the ways that damage to the respiratory tract epithelium is accrued during an infection has implications on selecting an appropriate antimicrobial for treatment. The strategy of rapid pathogen lysis by antibiotics may work against immune controls by amplifying inflammatory process leading to adverse outcomes. Cell lysis results in the release of bacterial products (e.g., cytotoxins, DNA, and cell-wall components) which are recognized by the innate immune system and trigger inflammation (McCullers and Tuomanen, 2001; Orman and English, 2000). Therefore, nonlytic antibiotics may improve the outcome possibly by exhibiting antiinflammatory activities that complement the antimicrobial actions (Ivetić Tkalčević et al., 2006). Although we did not study the implications of antibiotics or the complete feedback of damage to the cellular response, our model could be extended to find alternative treatment strategies that effectively eliminate pathogens without increasing pathogenesis.

<a id='ee386fde-4afd-4686-9056-6f560df11879'></a>

The signal triggering the macrophage influx into the lung has yet to be fully understood. Delayed macrophage recruitment following neutrophils can predict the behavior of pneumococcus in mice suggesting that an intermediate variable may be responsible. Our model generates consistent results by assuming that the signal originates from neutrophils.

<a id='f85dfaa7-e6a0-49e5-9cf5-b81ed42bc14d'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='ae3c6352-2048-4e89-b1aa-56cbd57579d0'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='191717a9-3cf7-4977-b4b1-8286df46d7bd'></a>

Smith et al.

<a id='56226313-f0bf-4a13-bcdb-67efb4a7273a'></a>

Page 13

<a id='2e770420-1a26-4dd2-89e1-2e48fb72a45b'></a>

However, this is likely an oversimplification and further experiments would be necessary to be sure.

<a id='86998b55-71f8-4adc-b467-eb8e832f2cf8'></a>

The phagocytic response is essential for successful clearance; however, other factors may contribute to pneumococcal removal. For example, a polysaccharide capsule renders this bacterium resistant to engulfment by phagocytic cells, but antibodies bound to the polysaccharide negate this effect by acting as ligands between the bacteria and the phagocyte thereby increasing phagocytic efficiency (van Dam et al., 1990). Furthermore, antibodies activate the classical complement pathway (Paterson and Mitchell, 2006), which is thought to be a key step leading to elimination of pneumococci (Kerr et al., 2005). More recent evidence suggests that IL-17-secreting CD4+ T-cells are involved in the neutrophil-mediated immune response and may also help prevent colonization (Lu et al., 2008). However, relatively little is known regarding the influence of these cells, which may have only minimal effects on an initial infection in a naive individual.

<a id='0fd1bfb4-367b-4178-af6a-f52fa4fa6fd2'></a>

Much remains to be discovered concerning the properties of bacterial rise, dissemination, and clearance within a host. Mathematical models provide a means of evaluating relative contributions of individual immune components to the processes during a bacterial infection with pneumococci. Using theoretical analyses to compare host responses in different patient populations will help determine why some individuals never get sick while others are easily colonized. Even models with moderate complexity like ours are important tools for the assessment of host responses. As more data becomes available, model formulations can become more refined and parameter values can be estimated thus facilitating an in depth understanding of the underlying biology of pneumococcal infections.

<a id='37049686-6791-40e3-a5d4-1c21560e7e67'></a>

**Supplementary Material**

Refer to Web version on PubMed Central for supplementary material.

<a id='3df8c994-a1ae-48e3-aa65-d0d4d03d2ed3'></a>

# Acknowledgments
This material is based upon work supported by the National Science Foundation under grant DMS-0354259 (AMS), NIH contract N01-AI-50020 (AMS), the 21st Century Science Initiative Grant from the James S. McDonnell Foundation (AMS, FRA), and PHS grant AI-66349 and ALSAC (JAM). Portions were done under the auspices of the US Department of Energy (AMS).

<a id='04f0c6a0-a014-4170-af50-7b3ecdd444e6'></a>

# References
Adamson I, Young L, Bowden D. Relationship of alveolar epithelial injury and repair to the induction of pulmonary fibrosis. Am. J. Pathol. 1988; 130:377–383. [PubMed: 3341452]
Austrian R. Some aspects of the pneumococcal carrier state. J. Antimicrob. Chemother. 1986; 18:35. [PubMed: 3745031]
Benton K, Everson M, Briles D. A pneumolysin-negative mutant of Streptococcus pneumoniae causes chronic bacteremia rather than acute sepsis in mice. Inf. Immun. 1995; 63:448–455.
Bergeron Y, Ouellet N, Deslauriers A, Simard M, Olivier M, Bergeron M. Cytokine kinetics and other host factors in response to pneumococcal pulmonary infection in mice. Infect. Immun. 1998; 66:912–922. [PubMed: 9488375]
Bingisser R, Holt P. Immunomodulating mechanisms in the lower respiratory tract: nitric oxide mediated interactions between alveolar macrophages, epithelial cells, and T-cells. Swiss Med. Wkly. 2001; 131:171–179. [PubMed: 11345807]
Bortz D, Nelson P. Sensitivity analysis of a nonlinear lumped parameter model of HIV infection dynamics. Bull. Math. Biol. 2004; 66:1009–1026. [PubMed: 15294416]
Cassatella M. The production of cytokines by polymorphonuclear neutrophils. Immunol. Today. 1995; 16:21–26. [PubMed: 7880385]

<a id='839e2c17-7946-4276-b47f-fba47721c568'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='cf217647-8f57-48b7-b8b2-5d1940adaec3'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='5718f464-db09-4f1e-8396-6a4cd608577f'></a>

Smith et al.

<a id='bec8d094-0b4c-4986-9f0e-67878197c3d5'></a>

Page 14

<a id='c605df5c-e526-40f5-b8ef-015427e87afc'></a>

Clawson C, Repine J. Quantitation of maximal bactericidal capability in human neutrophils. J. Lab. Clin. Med. 1976; 88:316-327. [PubMed: 956687]
Coggle J, Tarling J. Cell kinetics of pulmonary alveolar macrophages in the mouse. Cell Prolif. 1982; 15:139-143.
Coggle J, Tarling J. The proliferation kinetics of pulmonary alveolar macrophages. J. Leukoc. Biol. 1984; 35:317-327. [PubMed: 6584524]
van Dam J, Fleer A, Snippe H. Immunogenicity and immunochemistry of Streptococcus pneumoniae capsular polysaccharides. Antonie van Leeuwenhoek. 1990; 58:1-47. [PubMed: 2195989]
DeLeo F. Modulation of phagocyte apoptosis by bacterial pathogens. Apoptosis. 2004; 9:399-413. [PubMed: 15192322]
Dockrell D, Lee M, Lynch D, Read R. Immune-mediated phagocytosis and killing of Streptococcus pneumoniae are associated with direct and bystander macrophage apoptosis. J. Infect. Dis. 2001; 184:713-722. [PubMed: 11517432]
Dockrell D, Marriott H, Prince L, Ridger V, Ince P, Hellewell P, Whyte M. Alveolar macrophage apoptosis contributes to pneumococcal clearance in a resolving model of pulmonary infection. J. Immunol. 2003; 171:5380-5388. [PubMed: 14607941]
Doherty D, Downey G, Worthen G, Haslett C, Henson P. Monocyte retention and migration in pulmonary inflammation: Requirement for neutrophils. Lab. Investig. 1988; 59:200-213. [PubMed: 3404972]
Duong M, Simard M, Bergeron Y, Bergeron M. Kinetic study of the inflammatory response in Streptococcus pneumoniae experimental pneumonia treated with the ketolide HMR 3004. Antimicrob. Agents Chemother. 2001; 45:252-262. [PubMed: 11120974]
Eslami, M. Theory of Sensitivity in Dynamic Systems: An Introduction. Springer-Verlag; Berlin: 1994.
Fillion I, Ouellet N, Simard M, Bergeron Y, Sato S, Bergeron M. Role of chemokines and formyl peptides in pneumococcal pneumonia-induced monocyte/macrophage recruitment. J. Immunol. 2001; 166:7353-7361. [PubMed: 11390486]
Frank, P. Academic Press, Inc.; New York, NY: 1978. Introduction to System Sensitivity Theory..
Franke-Ullmann G, Pfortner C, Walter P, Steinmuller C, Lohmann-Matthes M, Kobzik L. Characterization of murine lung interstitial macrophages in comparison with alveolar macrophages in vitro. J. Immunol. 1996; 157:3097-3104. [PubMed: 8816420]
Giebink G. The prevention of pneumococcal disease in children. New Engl. J. Med. 2001; 345:1177-1183. [PubMed: 11642234]
Gloff, C.; Wills, R. Pharmacokinetics and Metabolism of Therapeutic Cytokines. In: Ferraiolo, B.; Mohler, M.; Gloff, C., editors. Protein Pharmacokinetics and Metabolism. New York. Plenum Press; 1992. p. 127-150.
Godleski J, Brain J. The origin of alveolar macrophages in mouse radiation chimeras. J. Exp. Med. 1972; 136:630-643. [PubMed: 4559194]
Gordon S, Irving G, Lawson R, Lee M, Read R. Intracellular trafficking and killing of Streptococcus pneumoniae by human alveolar macrophages are influenced by opsonins. Infect. Immun. 2000; 68:2286-2293. [PubMed: 10722631]
Gwinn M, Vallyathan V. Respiratory burst: Role in signal transduction in alveolar macrophages. J. Toxicol. Environ. Health B. 2006; 9:27-39.
Hampton M, Vissers M, Winterbourn C. A single assay for measuring the rates of phagocytosis and bacterial killing by neutrophils. J. Leukoc. Biol. 1994; 55:147-152. [PubMed: 8301210]
Henderson R, Hobbs J, Mathies M, Hogg N. Rapid recruitment of inflammatory monocytes is independent of neutrophil migration. Blood. 2003; 102:328-335. [PubMed: 12623845]
Ivetić Tkalčević V, Bošnjak B, Hrvačić B, Bosnar M, Marjanović N, Ferenčić Z, Šitum K, Čulić O, Parnham M, Eraković V. Anti-inflammatory activity of azithromycin attenuates the effects of lipopolysaccharide administration in mice. Eur. J. Pharmacol. 2006; 539:131-138. [PubMed: 16698012]
Jones M, Simms B, Lupa M, Kogan M, Mizgerd J. Lung NF-κB activation and neutrophil recruitment requires IL-1 and TNF receptor signaling during pneumococcal pneumonia. J. Immunol. 2005; 175:7530-7535. [PubMed: 16301661]

<a id='797e5f15-19d1-4e05-b188-572554620ca4'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='c97b2246-65b9-4539-85bf-2578120a2da8'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='6e4f8dba-d572-43ed-b161-69d47ae54a9b'></a>

Smith et al.

<a id='c8edfa35-7cc1-4b17-96e9-577889ab281a'></a>

Page 15

<a id='7edc0f23-ffa7-4fa4-b2c5-1f9568be7a15'></a>

Jonsson S, Musher D, Chapman A, Goree A, Lawrence E. Phagocytosis and killing of common
bacterial pathogens of the lung by human alveolar macrophages. J. Infect. Dis. 1985; 152:4-13.
[PubMed: 3874252]
Kadioglu A, Andrew P. The innate immune response to pneumococcal lung infection: The untold
story. Trends Immunol. 2004; 25:143-149. [PubMed: 15036042]
Kadioglu A, Gingles N, Grattan K, Kerr A, Mitchell T, Andrew P. Host cellular immune response to
pneumococcal lung infection in mice. Infect. Immun. 2000; 68:492-501. [PubMed: 10639409]
Kadioglu A, Weiser J, Paton J, Andrew P. The role of Streptococcus pneumoniae virulence factors in
host respiratory colonization and disease. Nat. Rev. Microbiol. 2008; 6:288-301. [PubMed:
18340341]
Kaplanski G, Marin V, Montero-Julian F, Mantovani A, Farnarier C. IL-6: A regulator of the transition
from neutrophil to monocyte recruitment during inflammation. Trends Immunol. 2003; 24:25-29.
[PubMed: 12495721]
Kerr A, Paterson G, Riboldi-Tunnicliffe A, Mitchell T. Innate immune defense against pneumococcal
pneumonia requires pulmonary complement component C3. Infect. Immun. 2005; 73:4245-4252.
[PubMed: 15972516]
Knapp S, Leemans J, Florquin S, Branger J, Maris N, Pater J, van Rooijen N, van der Poll T. Alveolar
macrophages have a protective antiinflammatory role during murine pneumococcal pneumonia.
Am. J. Respir. Crit. Care Med. 2003; 167:171-179. [PubMed: 12406830]
Lauffenburger, D. Mathematical analysis of the macrophage response to bacterial challenge in the
lung. In: van Furth, R., editor. Mononuclear Phagocytes: Characteristics, Physiology and Function.
Martinus Nijhoff Publishers; The Netherlands: 1985. p. 351-357.
Lu Y, Gross J, Bogaert D, Finn A, Bagrade L, Zhang Q, Kolls J, Srivastava A, Lundgren A, Forte S, et
al. Interleukin-17A mediates acquired immunity to pneumococcal colonization. PLoS Pathog.
2008; 4:e1000159. [PubMed: 18802458]
Malech, H. Role of neutrophils in the immune system. In: Quinn, M.; Deleo, F.; Bokoch, G., editors.
Neutrophil Methods and Protocols. Humana Press; 2007. p. 3-14.
Marriott H, Ali F, Read R, Mitchell T, Whyte M, Dockrell D. Nitric oxide levels regulate macrophage
commitment to apoptosis or necrosis during pneumococcal infection. FASEB J. 2004; 18:1126-
1128. [PubMed: 15132983]
Maus U, Srivastava M, Paton J, Mack M, Everhart M, Blackwell T, Christman J, Schlondorff D,
Seeger W, Lohmeyer J. Pneumolysin-induced lung injury is independent of leukocyte trafficking
into the alveolar space. J. Immunol. 2004; 173:1307-1312. [PubMed: 15240724]
McCullers J, Bartmess K. Role of neuraminidase in lethal synergism between influenza virus and
Streptococcus pneumoniae. J. Infect. Dis. 2003; 187:1000-1009. [PubMed: 12660947]
McCullers J, English B. Improving therapeutic strategies for secondary bacterial pneumonia following
influenza. Future Microbiol. 2008; 3:397-404. [PubMed: 18651811]
McCullers J, Tuomanen E. Molecular pathogenesis of pneumococcal pneumonia. Front. Biosci. 2001;
6:D877-89. [PubMed: 11502489]
McRitchie D, Isowa N, Edelson J, Xavier A, Cai L, Man H, Wang Y, Keshavjee S, Slutsky A, Liu M.
Production of tumour necrosis factor by primary cultured rat alveolar epithelial cells. Cytokine.
2000; 12:644-654. [PubMed: 10843740]
Mizgerd J, Meek B, Kutkoski G, Bullard D, Beaudet A, Doerschuk C. Selectins and neutrophil traffic:
Margination and Streptococcus pneumoniae-induced emigration in murine lungs. J. Exp. Med.
1996; 184:639-645. [PubMed: 8760817]
Monton C, Torres A. Lung inflammatory response in pneumonia. Monaldi Arch. Chest Dis. 1998;
53:56-63. [PubMed: 9632909]
Murphy J, Summer R, Wilson A, Kotton D, Fine A. The prolonged life-span of alveolar macrophages.
Am. J. Respir. Cell Mol. Biol. 2008; 38:380-385. [PubMed: 18192503]
Onofrio J, Toews G, Lipscomb M, Pierce A. Granulocyte-alveolar-macrophage interaction in the
pulmonary clearance of Staphylococcus aureus. Am. Rev. Respir. Dis. 1983; 127:335-341.
[PubMed: 6830054]

<a id='0bc0e483-a8b7-4002-a733-d573d7288c98'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='2b884223-6fd9-4622-a629-9d695d436bd0'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='73b8bc1a-dc74-47de-8b51-92f2b7ee6156'></a>

Smith et al.

<a id='40992aea-1917-4eae-be85-67eb95c7e41d'></a>

Page 16

<a id='b5e061a3-1717-4032-bf40-378bde533673'></a>

Orihuela, C.; Tuomanen, E. Streptococcus pneumoniae: Invasion and inflammation. In: Fischetti, V.; Novick, R.; Ferretti, J., editors. Gram-positive Pathogens. 2nd edition. ASM Press; Washington, DC: 2006. p. 253-267.Am. Soc. Microbiol.
Orman K, English B. Effects of antibiotic class on the macrophage inflammatory response to Streptococcus pneumoniae. J. Infect. Dis. 2000; 182:1561-1565. [PubMed: 11023483]
van Oud Alblas A, van Furth R. Origin, Kinetics, and characteristics of pulmonary macrophages in the normal steady state. J. Exp. Med. 1979; 149:1504-1518. [PubMed: 448291]
Paterson G, Mitchell T. Innate immunity and the pneumococcus. Microbiol. 2006; 152:285-293.
Pilyugin S, Antia R. Modeling immune responses with handling time. Bull. Math. Biol. 2000; 62:869–890. [PubMed: 11016088]
van der Poll T, Marchant A, Keogh C, Goldman M, Lowry S. Interleukin-10 impairs host defense in murine pneumococcal pneumonia. J. Infect. Dis. 1996; 174:994-1000. [PubMed: 8896500]
Ramphal R, Small P, Shands Jr J, Fischlschweiger W, Small Jr P. Adherence of Pseudomonas aeruginosa to tracheal cells injured by influenza infection or by endotracheal intubation. Infect. Immun. 1980; 27:614-619. [PubMed: 6769805]
Reynolds A, Rubin J, Clermont G, Day J, Vodovotz Y, Bard Ermentrout G. A reduced mathematical model of the acute inflammatory response: I. Derivation of model and analysis of anti-inflammation. J. Theor. Biol. 2006; 242:220-236. [PubMed: 16584750]
Rudnev S, Romanyukha A. Mathematical modeling of immune-inflammatory reaction in acute pneumonia. J. Biol. Sys. 1995; 3:429-439.
Schluger N, Rom W. Early responses to infection: Chemokines as mediators of inflammation. Curr. Opin. Immunol. 1997; 9:504-508. [PubMed: 9287176]
Stadnyk A. Cytokine production by epithelial cells. FASEB J. 1994; 8:1041-1047. [PubMed: 7926369]
Stone K, Mercer R, Gehr P, Stockstill B, Crapo J. Allometric relationships of cell numbers and size in the mammalian lung. Am. J. Respir. Cell Mol. Biol. 1992; 6:235. [PubMed: 1540387]
Sun K, Metzger D. Inhibition of pulmonary antibacterial defense by interferon-γ during recovery from influenza infection. Nat. Med. 2008; 14:558-564. [PubMed: 18438414]
Tarling J, Lin H, Hsu S. Self-renewal of pulmonary alveolar macrophages: Evidence from radiation chimera studies. J. Leukoc. Biol. 1987; 42:443-446. [PubMed: 3316460]
Taut K, Winter C, Briles D, Paton J, Christman J, Maus R, Baumann R, Welte T, Maus U. Macrophage turnover kinetics in the lungs of mice infected with Streptococcus pneumoniae. Am. J. Respir. Cell Mol. Biol. 2008; 38:105. [PubMed: 17690327]
Taylor P, Martinez-Pomares L, Stacey M, Lin H, Brown G, Gordon S. Macrophage receptors and immune recognition. Annu. Rev. Immunol. 2005; 23:901-944. [PubMed: 15771589]
Thomassen M, Buhrow L, Connors M, Takao Kaneko F, Erzurum S, Kavuru M. Nitric oxide inhibits inflammatory cytokine production by human alveolar macrophages. Am. J. Respir. Cell Mol. Biol. 1997; 17:279-283. [PubMed: 9308913]
Todar K. Streptococcus pneumoniae: Pneumococcal pneumonia. Todar's Online Textbook of Bacteriology . 2002
Toews G, Gross G, Pierce A. The relationship of inoculum size to lung bacterial clearance and phagocytic cell response in mice. Am. Rev. Respir. Dis. 1979; 120:559-566. [PubMed: 114074]
World Health Organization. Streptococcus pneumoniae (pneumococcus). 2008. http://www.who.int/nuvi/pneumococcus/en/
Zhang P, Summer W, Bagby G, Nelson S. Innate immunity and pulmonary host defense. Immunol. Rev. 2000; 173:39-51. [PubMed: 10719666]
Zysk G, Bejo L, Schneider-Wald B, Nau R, Heinz H. Induction of necrosis and apoptosis of neutrophil granulocytes by Streptococcus pneumoniae. Clin. Exper. Immunol. 2000; 122:61-66. [PubMed: 11012619]

<a id='092fdc88-3267-4c26-bdfa-2fc50b56d165'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='61256149-0234-4d9d-a2fb-28b26f54eeb9'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='1dee013d-c888-426f-86fa-82442ccf69fb'></a>

Smith et al.

<a id='7867c2ef-ff9a-453c-a3a9-614e56ec0dd9'></a>

Page 17

<a id='467a965d-2e51-4086-8f34-6afe2ff2a26a'></a>

<::logo: [Company/Organization/Brand Name]  
[Readable Text if any]  
[Short description of key visual elements]::>

<a id='2822209a-b96c-4dcd-bc5f-6adf94c407e9'></a>

Figure 1.
Pneumococcal lung titers (geometric means  SD) over time for groups of 6 mice inoculated with 10 (squares) or 10 (triangles) CFU. Titers for mice given 10 CFU were undetectable and are not shown. The dotted line represents a lower detection limit.

<a id='0ac70212-43c9-4055-941e-441b7bc8cee5'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='a7979a06-1f3c-49f9-aa12-417b474a166d'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='98617960-6cdb-40a4-9e53-9582ff756c8f'></a>

Smith et al.

<a id='b6409e15-28d2-402a-995c-47a89d4c4b10'></a>

Page 18

<a id='f34eaa58-ddd0-41c0-aebb-646ecfd5722c'></a>

<::logo: [No company, organization, or brand identified]
[No readable text]
[No notable visual elements]::>

<a id='262f4f4f-eb11-4609-85e2-afe0577ceaa5'></a>

Figure 2.
The function (f(P, MA)) describing the decrease in phagocytosis of pneumococcus by alveolar macrophages for various values of (a) the nonlinearity parameter x, and (b) the maximum number of pneumococci per alveolar macrophage, n. Vertical line at P(t) = 104 shows the difference in f(P, MA) given a particular value of n. MA is fixed at 106 cells.

<a id='a8d7b4a8-f2dd-4949-865d-2fb38fce247d'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='bd12fa13-7d33-42c4-baaa-fcc9451c2fcb'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='878be363-ffb2-4719-ad0a-4b0a91034691'></a>

Smith et al.

<a id='dbaecedf-19f1-4916-9139-389a30043e92'></a>

Page 19

<a id='b2e57ef9-1e86-4450-a3c6-3eff9db22dd0'></a>

<::
chart showing Bacteria (log10 CFU/ml lung homogenate) on the y-axis versus Time (hours) on the x-axis.

Legend:
- P0 = 10^5 CFU/ml
- P0 = 10^7 CFU/ml
- --- P0 = 10^5 CFU/ml
- --- P0 = 10^7 CFU/ml
- • 10^5 CFU, Mean ± SD
- ▲ 10^7 CFU, Mean ± SD
- ■ 10^5 CFU, Mean ± SD
: chart::>

<a id='ddb94e03-5a81-4b1e-9dec-b115337217a8'></a>

**Figure 3.**
Numerical simulation of the alveolar macrophage model, Equation (2), using initial
conditions P₀ = 10³ CFU/ml (dashed-dotted line), P₀ = 10⁴ CFU/ml (dashed line), and P₀ =
10⁵ CFU/ml (solid line). Pneumococcal titers (geometric means ± SD) are shown for mice
inoculated with 10⁵ (squares) or 10⁶ (triangles) CFU. Titers for mice given 10⁴ CFU were
undetectable and are not shown. The dotted line represents a lower detection limit.

<a id='9671b75e-1514-4a36-a56d-28cddae86c9e'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='231a5c53-2eff-4cca-a2a0-671bdc880582'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='07066de2-c887-4693-9c26-46851e6bea81'></a>

Smith et al.

<a id='09154f4d-d88a-4ce5-8129-3db434dc9485'></a>

Page 20

<a id='49032e07-ae0c-471a-b8c8-b0f7f9144709'></a>

<::chart: A multi-panel plot showing the numerical simulation of a neutrophil model. The legend at the top indicates line styles for different initial conditions: P₀ = 10⁵ CFU/ml (solid line), P₀ = 10⁴ CFU/ml (dashed line), P₀ = 10³ CFU/ml (dashed-dotted line). It also shows symbols for titer data: triangles - 10⁶ CFU, Mean ± SD; squares - 10⁵ CFU, Mean ± SD. All subplots share a common x-axis, "Time (hours)", ranging from 0 to 120. The y-axis labels and ranges vary for each subplot. (a) Bacteria (log₁₀ CFU/ml) against time. This subplot includes both simulated lines and experimental data points (squares and triangles with error bars). (b) Neutrophils (x 10⁴) against time. (c) Proinflammatory Cytokine (pg/ml, x 10⁵) against time. (d) Debris (x 10⁵) against time. (e) Susceptible Epithelial Cells (x 10⁷) against time. (f) Epithelial Cells With Bact. Attached (x 10⁷) against time. Figure 4. Numerical simulation of the neutrophil model, Equations (6)-(11), using initial conditions P₀ = 10³ CFU/ml (dashed-dotted line), P₀ = 10⁴ CFU/ml (dashed line), P₀ = 10⁵ CFU/ml (solid line), and parameter values in Table 2. (a) Bacteria against titer data (squares - 10⁵ CFU/mouse, triangles -10⁶ CFU/mouse), (b) neutrophils, (c) proinflammatory cytokine, (d) debris, (e) susceptible epithelial cells, and (f) epithelial cells with bacteria attached.::>

<a id='98712e18-bcfb-4f49-954b-8d040fad0ada'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='d74bdf14-d234-4b7d-869b-f68341f0fbd7'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='7da433cb-6149-48fb-a541-41ceb9920ee2'></a>

Smith et al.

<a id='0446934a-9f81-4e23-8b55-1209572b0766'></a>

Page 21

<a id='6d782245-bb7a-46ed-a283-5b8c43bd9418'></a>

<::chart: The chart displays the numerical simulation of the neutrophil model (Equations (6)-(11)) with varying initial bacterial values, along with experimental data points. The x-axis represents Time (hours) from 0 to 80. The y-axis represents Bacteria (log₁₀ CFU/ml lung homogenate) from -1 to 9. Six simulated curves are shown: P₀ = 10³ CFU/ml (dashed-dotted line), P₀ = 5.6 × 10³ CFU/ml (solid orange line), P₀ = 10⁴ CFU/ml (dashed line), P₀ = 1.8 × 10⁴ CFU/ml (solid green line), P₀ = 5.6 × 10⁴ CFU/ml (solid yellow line), and P₀ = 10⁵ CFU/ml (solid black line). Experimental data points are also plotted: light blue triangles represent 10⁶ CFU (Mean ± SD), and magenta squares represent 10⁵ CFU (Mean ± SD). The simulation uses parameter values from Table 2.::>

<a id='54bcf12b-1ac8-4bfe-9e70-f572a41c7701'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='95bbb4c0-4ce2-43bb-a8bc-ab1cdaefaea6'></a>

NIH-PA Author Manuscript

<a id='d5d2e965-0499-498f-98f6-192511bdd758'></a>

NIH-PA Author Manuscript

<a id='33c90e0c-77e2-44a3-b75a-1f728287ecd1'></a>

NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='42dafd31-e193-40b8-9a47-d3eeff921d05'></a>

Smith et al.

<a id='a5bfd4c5-5a8d-44aa-9fef-bb18969abf99'></a>

Page 22

<a id='1a6ddbf7-611f-436d-ad35-13adde17fc30'></a>

<::Six plots (a-f) arranged in two columns and three rows, showing different parameters over time. All x-axes are labeled "Time (hours)".

Legend at the top right: Solid line represents 10^2 CFU/mL, Dashed line represents 10^4 CFU/mL. There are also data points for 10^2 CFU/mL Mean \u00b1 SD (squares) and 10^4 CFU/mL Mean \u00b1 SD (circles).

Plot (a): Y-axis labeled "Bacteriology (CFU/mL)". Shows bacterial count over time.
Plot (b): Y-axis labeled "Cytokines (pg/mL)". Shows cytokine levels over time.
Plot (c): Y-axis labeled "Neutrophils". Shows neutrophil count over time.
Plot (d): Y-axis labeled "Macrophages". Shows macrophage count over time.
Plot (e): Y-axis labeled "Epithelial Cells". Shows epithelial cell count over time.
Plot (f): Y-axis labeled "Ext. Cells W/In Renal Adjunct". Shows external cells within renal adjunct over time.
: chart::>

<a id='6a54f6ba-c345-4e05-8fdf-f52f0006488e'></a>

Figure 6.
Numerical simulation of the monocyte-derived macrophage model, Equations (12)-(18),
using initial conditions P₀ = 10³ CFU/ml (dashed-dotted line), P₀ = 10⁴ CFU/ml (dashed
line), P₀ = 10⁵ CFU/ml (solid line), and parameter values in Table 3. (a) Bacteria against
titer data (squares - 10⁵ CFU/mouse, triangles -10⁶ CFU/mouse), (b) proinflammatory
cytokine, (c) neutrophils, (d) monocyte-derived macrophages, (e) debris, (f) susceptible
epithelial cells and (g) epithelial cells with bacteria attached.

<a id='2d1a45b7-7db4-4b31-a4cb-16438df3e4d9'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='4d10a487-5297-4d1f-a310-ad6d06f4f004'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='be0695cf-f183-4b8b-bcd2-9d95eeb5101a'></a>

Smith et al.

<a id='79d6705e-e346-4762-8a33-7540a25518e5'></a>

Page 23

<a id='ec8c82a5-497a-412f-be1f-ca0ca35b8a10'></a>

Table 1
The alveolar macrophage model (Stage 1) parameter definitions and values.
<table id="22-1">
<tr><td id="22-2">Parameter</td><td id="22-3">Description</td><td id="22-4">Units</td><td id="22-5">Value</td><td id="22-6">Comments</td></tr>
<tr><td id="22-7">r</td><td id="22-8">Bacterial growth rate</td><td id="22-9">hour⁻¹</td><td id="22-a">11.3 x 10⁻¹</td><td id="22-b">see text</td></tr>
<tr><td id="22-c">Kₚ</td><td id="22-d">Bacterial carrying capacity</td><td id="22-e">CFU/ml</td><td id="22-f">2.3 x 10⁸</td><td id="22-g">see text</td></tr>
<tr><td id="22-h">γMₐ</td><td id="22-i">Bacterial clearance by AMs</td><td id="22-j">cell⁻¹hour⁻¹</td><td id="22-k">5.6 x 10⁻⁶</td><td id="22-l">see text</td></tr>
<tr><td id="22-m">n</td><td id="22-n">Maximum number bacteria per AM</td><td id="22-o">(CFU/ml)cell⁻¹</td><td id="22-p">5</td><td id="22-q">(Gordon et al., 2000)</td></tr>
<tr><td id="22-r">x</td><td id="22-s">Nonlinearity in f(P, M_A)</td><td id="22-t">N/A</td><td id="22-u">2</td><td id="22-v">see text</td></tr>
<tr><td id="22-w">s</td><td id="22-x">AM constant supply</td><td id="22-y">cell^-1hour^-1</td><td id="22-z">1.0 - 4.2 x 10^3</td><td id="22-A">see text</td></tr>
<tr><td id="22-B">d</td><td id="22-C">AM death rate</td><td id="22-D">hour^-1</td><td id="22-E">1.0 - 4.2 x 10^-3</td><td id="22-F">(Coggle and Tarling, 1982; Godleski and Brain, 1972; van Oud Alblas and van Furth, 1979)</td></tr>
<tr><td id="22-G">M_A^*</td><td id="22-H">AM steady state value</td><td id="22-I">cells</td><td id="22-J">10^6</td><td id="22-K">(van Oud Alblas and van Furth, 1979)</td></tr>
<tr><td id="22-L">P_0</td><td id="22-M">Initial number of pneumococci</td><td id="22-N">CFU/ml</td><td id="22-O">10^3, 10^4, or 10^5</td><td id="22-P">see text</td></tr>
</table>

<a id='ae05dca5-4c1d-4e04-bd92-bde0026e5493'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='1d5aa967-3ad3-41c9-94c6-49492b6d9843'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='dff71103-7007-466f-b7e1-8fea040a1316'></a>

Smith et al.

<a id='33dd6f4d-f4dc-4ae3-99e4-1646e6c4d7bc'></a>

Page 24

<a id='3133f220-e1a2-4c15-893a-387bea58e754'></a>

Table 2
The neutrophil model (Stage 2) parameter definitions and values.
<table id="23-1">
<tr><td id="23-2">Parameter</td><td id="23-3">Description</td><td id="23-4">Units</td><td id="23-5">Value</td><td id="23-6">Comments</td></tr>
<tr><td id="23-7">γ N</td><td id="23-8">Bacterial clearance by neutrophils</td><td id="23-9">cell⁻¹hour⁻¹</td><td id="23-a">1.0 × 10⁻⁵</td><td id="23-b">see text</td></tr>
<tr><td id="23-c">θ M</td><td id="23-d">Activation of cytokine production</td><td id="23-e">(CFU/ml)⁻¹hour⁻¹</td><td id="23-f">4.2 × 10⁻⁸</td><td id="23-g">see text</td></tr>
<tr><td id="23-h">κ</td><td id="23-i">Deactivation of cytokine production</td><td id="23-j">hour⁻¹</td><td id="23-k">4.2 × 10⁻²</td><td id="23-l">see text</td></tr>
<tr><td id="23-m">ν</td><td id="23-n">Cytokine production by AMs</td><td id="23-o">(pg/ml)cell⁻¹hour⁻¹</td><td id="23-p">2.9 × 10⁻²</td><td id="23-q">see text</td></tr>
<tr><td id="23-r">ω</td><td id="23-s">Bacterial attachment to epithelial cells</td><td id="23-t">(CFU/ml)-¹hour-¹</td><td id="23-u">2.1 × 10⁻⁸</td><td id="23-v">see text</td></tr>
<tr><td id="23-w">dE</td><td id="23-x">Epithelial cell death</td><td id="23-y">hour-¹</td><td id="23-z">16.7 × 10⁻²</td><td id="23-A">see text</td></tr>
<tr><td id="23-B">α</td><td id="23-C">Cytokine production by epithelial cells</td><td id="23-D">(pg/ml)cell-¹hour-¹</td><td id="23-E">2.1 × 10⁻²</td><td id="23-F">see text</td></tr>
<tr><td id="23-G">kn</td><td id="23-H">Cytokine inhibition by neutrophils</td><td id="23-I">cell-¹</td><td id="23-J">1.4 × 10⁻⁵</td><td id="23-K">see text</td></tr>
<tr><td id="23-L">dc</td><td id="23-M">Cytokine degradation rate</td><td id="23-N">hour-¹</td><td id="23-O">8.3 × 10⁻¹</td><td id="23-P">(Gloff and Wills, 1992)</td></tr>
<tr><td id="23-Q">Nmax</td><td id="23-R">Maximum number neutrophils</td><td id="23-S">cells</td><td id="23-T">1.8 × 10⁵</td><td id="23-U">see text</td></tr>
<tr><td id="23-V">η</td><td id="23-W">Neutrophil recruitment rate</td><td id="23-X">cells (pg/ml)⁻¹hour⁻¹</td><td id="23-Y">13.3 × 10⁻¹</td><td id="23-Z">see text</td></tr>
<tr><td id="23-10">d_N</td><td id="23-11">Neutrophil clearance rate</td><td id="23-12">hour⁻¹</td><td id="23-13">6.3 × 10⁻²</td><td id="23-14">(Malech, 2007)</td></tr>
<tr><td id="23-15">d_NP</td><td id="23-16">Bacterial-induced death neutrophils</td><td id="23-17">(CFU/ml)⁻¹hour⁻¹</td><td id="23-18">2.5 × 10⁻⁷</td><td id="23-19">see text</td></tr>
<tr><td id="23-1a">ρ 1</td><td id="23-1b">Debris from bacterial-induced neutrophil death</td><td id="23-1c">cell⁻¹</td><td id="23-1d">1.0 × 10⁻¹</td><td id="23-1e">see text</td></tr>
<tr><td id="23-1f">P2</td><td id="23-1g">Debris from neutrophil death</td><td id="23-1h">cell-1</td><td id="23-1i">1.0 x 10-3</td><td id="23-1j">see text</td></tr>
<tr><td id="23-1k">P3</td><td id="23-1l">Debris from epithelial cell death</td><td id="23-1m">cell-1</td><td id="23-1n">1.0 x 10-5</td><td id="23-1o">see text</td></tr>
<tr><td id="23-1p">dp</td><td id="23-1q">Removal of debris by AMs</td><td id="23-1r">cell-1</td><td id="23-1s">2.5 x 10-6</td><td id="23-1t">see text</td></tr>
<tr><td id="23-1u">ka</td><td id="23-1v">Phagocytosis inhibition</td><td id="23-1w">cell-1</td><td id="23-1x">5.0 x 10-9</td><td id="23-1y">see text</td></tr>
<tr><td id="23-1z">P(0)</td><td id="23-1A">Initial number of pneumococci</td><td id="23-1B">CFU/ml</td><td id="23-1C">103, 104 or 105</td><td id="23-1D">see text</td></tr>
<tr><td id="23-1E">E(0)</td><td id="23-1F">Initial number of epithelial cells</td><td id="23-1G">cells</td><td id="23-1H">108</td><td id="23-1I">(Stone et al., 1992)</td></tr>
<tr><td id="23-1J">Ελ(0)</td><td id="23-1K">Initial number of epithelial cells with bacteria</td><td id="23-1L">cells</td><td id="23-1M">0</td><td id="23-1N">see text</td></tr>
<tr><td id="23-1O">C(0)</td><td id="23-1P">Initial concentration</td><td id="23-1Q">pg/ml</td><td id="23-1R">0</td><td id="23-1S">see text</td></tr>
<tr><td id="23-1T">N(0)</td><td id="23-1U">Initial number of neutrophils</td><td id="23-1V">cells</td><td id="23-1W">0</td><td id="23-1X">see text</td></tr>
<tr><td id="23-1Y">D(0)</td><td id="23-1Z">Initial amount of debris</td><td id="23-20">N/A</td><td id="23-21">0</td><td id="23-22">see text</td></tr>
</table>

<a id='87caea72-b583-430c-b0d3-f054d46daf9e'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='2116c284-2729-46e4-bd61-9e1421357331'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='fd362351-92e7-4e5b-9b72-d91fa0af4522'></a>

Smith et al.

<a id='b24e6a70-da99-4b73-b74d-8c8b39e9bd9f'></a>

Page 25

<a id='f17d68cb-fa41-4089-bfe6-0bd8206bce51'></a>

Table 3
The monocyte-derived macrophage model (Stage 3) parameter definitions and values.
<table id="24-1">
<tr><td id="24-2">Parameter</td><td id="24-3">Description</td><td id="24-4">Units</td><td id="24-5">Value</td></tr>
<tr><td id="24-6">γm</td><td id="24-7">Bacterial clearance by MDMs</td><td id="24-8">cell-1hour-1</td><td id="24-9">3.2 x 10-5</td></tr>
<tr><td id="24-a">Mmax</td><td id="24-b">Maximum number of MDMs</td><td id="24-c">cells</td><td id="24-d">1.8 × 105</td></tr>
<tr><td id="24-e">ζ</td><td id="24-f">MDM recruitment rate</td><td id="24-g">hour-1</td><td id="24-h">3.8 x 10-3</td></tr>
<tr><td id="24-i">dm</td><td id="24-j">MDM clearance rate</td><td id="24-k">hour-1</td><td id="24-l">1.9 x 10-3</td></tr>
<tr><td id="24-m">τ</td><td id="24-n">Time delay before MDM recruitment</td><td id="24-o">hours</td><td id="24-p">12</td></tr>
<tr><td id="24-q">M(0)</td><td id="24-r">Initial number of MDMs</td><td id="24-s">cells</td><td id="24-t">0</td></tr>
<tr><td id="24-u">N(t)</td><td id="24-v">Number of neutrophils for -r &lt; t ≤ 0</td><td id="24-w">cells</td><td id="24-x">0</td></tr>
</table>

<a id='22fa772a-dfaa-4ddf-9001-aff0dfcdf234'></a>

J Theor Biol. Author manuscript; available in PMC 2012 May 7.

<a id='26b69d2b-d4f3-4cb3-9f61-31cb46723c44'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<a id='0213ed93-6f73-483d-8a34-9249ce8d48c7'></a>

# Supplementary Materials

## Mathematical Model of a Three-Stage Innate Immune Response to a Pneumococcal Lung Infection

Amber M. Smith'*, Jonathan A. McCullers', and Frederick R. Adler'

'Theoretical Biology and Biophysics, Los Alamos National Laboratory, Los Alamos, NM 87545, USA
'Department of Infectious Diseases, St. Jude Children's Research Hospital, Memphis, TN 38105, USA
'Departments of Mathematics and Biology, University of Utah, Salt Lake City, UT 84112, USA
*Email: asmith@lanl.gov

<a id='74d3798e-ae2f-4327-a56a-2ef959c01f32'></a>

## Differential Sensitivity Analysis

To gain a better understanding of the monocyte-derived macrophage model dynamics and reveal relationships between model solutions and parameters, we analyzed the output of our model in response to changes in the parameters. The approach we use is a differential sensitivity analysis (see (Bortz and Nelson, 2004; Eslami, 1994, Frank, 1978)), which is also referred to as the direct method. See Bortz and Nelson (2004) for application of this method to models including a time delay.

<a id='c0e1fb0d-75c8-4209-9b34-5b7b939fe517'></a>

The sensitivity equations interpret how changes in parameter values influence the model solution over time and are generated by differentiating the model equations with respect to each parameter. In general, for a system of equations $\dot{\mathbf{y}} = \mathbf{g}(t, \mathbf{y}, \mathbf{y}(t - \tau), \mathbf{q})$, where $\mathbf{q}$ is the vector of parameters, the sensitivity equations are given by

<a id='b496b3a4-1196-4f32-9232-154e940431a5'></a>

dS/dt = J(t)S(t) + J^T(t)S(t - τ) + A(t), (S1)

<a id='f71834e2-b8ff-4b24-b050-16ffea3f2cbd'></a>

where $S_{i,j}(t) = \partial y_i/\partial q_j$ is the sensitivity function, $J_{i,j}(t) = \partial g_i/\partial y_j$ is the jacobian, $J^T_{i,j}(t) = \partial g_i/\partial y_j(t - \tau)$ is the delayed jacobian, and $A_{i,j}(t) = \partial g_i/\partial q_j$ is the partial derivative of the model equation with respect to the parameter in question.

More specifically for the monocyte-derived macrophage model (Eqns. (12)-(18) in the

<a id='153c1b0f-06e9-4c00-9b87-c467c8ee1458'></a>

1

<!-- PAGE BREAK -->

<a id='a41e58e9-53f6-4238-af78-94ea1a2a0da3'></a>

main text), the sensitivity functions (S) for any parameter qi are defined as

<a id='1c2ebd27-19ef-4cc2-9040-a8bc84db34cd'></a>

$$S_1: P_{q_i}(t) = \frac{\partial}{\partial q_i} P(t, \mathbf{q})$$
$$S_2: E_{U,q_i}(t) = \frac{\partial}{\partial q_i} E_U(t, \mathbf{q})$$
$$S_3: E_{A,q_i}(t) = \frac{\partial}{\partial q_i} E_A(t, \mathbf{q})$$
$$S_4: C_{q_i}(t) = \frac{\partial}{\partial q_i} C(t, \mathbf{q}) \quad (S2)$$
$$S_5: N_{q_i}(t) = \frac{\partial}{\partial q_i} N(t, \mathbf{q})$$
$$S_6: D_{q_i}(t) = \frac{\partial}{\partial q_i} D(t, \mathbf{q})$$
$$S_7: M_{q_i}(t) = \frac{\partial}{\partial q_i} M(t, \mathbf{q}),$$

<a id='7df4907b-8ee4-49f1-a7f7-1277b9db9e5d'></a>

and the corresponding sensitivity equations are

<a id='9a562754-7a9a-4d9a-94ad-7f43be126839'></a>

$$\frac{dS_1}{dt} = \left[ r\left(1 - \frac{2P}{K_P}\right) - \frac{\partial f(P, M_A^*)}{\partial P} \left(\frac{\gamma_{MA} M_A^* P}{1 + k_D D M_A^*}\right) - \frac{\gamma_{MA} f(P, M_A^*) M_A^*}{1 + k_D D M_A^*} - \gamma_N N - \gamma_m M \right] S_1$$

<a id='f82edc19-bc38-4915-813d-bcb3d700f48e'></a>

$$- \gamma_N PS_5 + \frac{\gamma_{M_A} f(P, M_A^*) k_D M_A^*}{(1 + k_D D M_A^*)^2} M_A^* PS_6 - \gamma_m PS_7 + \frac{\partial\dot{P}}{\partial q_i}$$

<a id='e1746cf2-bb0a-4643-adc3-7cc58491bc5e'></a>

$\frac{dS_2}{dt} = -\omega(E_U S_1 + P S_2) + \frac{\partial\dot{E}_U}{\partial q_i}$

<a id='0d0fc715-3a71-4fd6-b21f-3958499f1660'></a>

dS3/dt = ω(EUS1 + PS2) - DES3 + ∂EA/∂qi
dS4/dt = ν * ((θMM*A(d + κ + θMP) - θ^2M PM*A) / ((d + κ + θMP)^2(1 + kNN))) * S1 + (α / (1 + kNN)) * S3 - dcS4 (S3)

<a id='02d2c392-6226-4f4b-bbc7-23099ada84e0'></a>

$$\frac{dS_5}{dt} = -d_{NP}NS_1 + \eta\left(1 - \frac{N}{N_{max}}\right)S_4 - \left( \left(\frac{\alpha E_A k_N}{(1 + k_N N)^2} + \nu\frac{k_N\theta_M P M^*_A}{(d + \kappa + \theta_M P)(1 + k_N N)^2}\right) S_5 + \frac{\partial\dot{C}}{\partial q_i} \right) - \left( \frac{\eta C}{N_{max}} + d_N + d_{NP}P \right) S_5 + \frac{\partial\dot{N}}{\partial q_i}$$

<a id='9a42454f-388a-4079-8a09-696c216c384c'></a>

$$\frac{dS_6}{dt} = \rho_1 d_{NP} N S_1 + \rho_3 d_E S_3 + (\rho_1 d_{NP} P + \rho_2 d_N) S_5 - d_D M_A^* S_6 + \frac{\partial \dot{D}}{\partial q_i}$$

<a id='fb5cb2c4-2c1a-402f-9b4b-b7a438b612ee'></a>

dS_7 / dt = - [ (ξ N(t - τ) / M_{max}) + d_m ] S_7 + ξ (1 - M / M_{max}) S_5(t - τ) + ∂M / ∂q_i

<a id='fefe0063-cd75-4a7d-9b15-ecd2fd5f0d7e'></a>

2

<!-- PAGE BREAK -->

<a id='0b6a796a-584e-4d34-beb8-37b51a7cfe5f'></a>

Here, the last term in each equation is the derivative of the original model equations (Equations (12)-(18) in the main text) with respect to the parameter. So for each parameter of interest, a set of these 7 equations are constructed.

<a id='47172f45-b0cf-4d31-a422-ba83db364f82'></a>

The output of the sensitivity equations can be analyzed using the semirelative sensitivity solutions and the logarithmic sensitivity solutions. The semirelative sensitivity solutions are obtained by multiplying the parameter in question by the sensitivity solution (e.g., $\gamma_N P_{\gamma_N}(t)$). These results quantify how the model solution changes when a parameter is doubled, for instance, and have the same units as the model solutions. Logarithmic sensitivity solutions, on the other hand, are dimensionless and reflect the percentage change in the solution that occurs when a parameter is varied. To obtain these solutions, the sensitivity solutions are effectively normalized by dividing the semirelative sensitivity solutions by the value of the solved variable (e.g., $\gamma_N P_{\gamma_N}(t)/P(t)$). Here, we present only the results of the logarithmic sensitivity solutions.

<a id='7ba4eca5-fc48-45cb-8200-c16c8da734f9'></a>

# Logarithmic Sensitivity Solutions
The sensitivity equations (Equation (S3)) were derived for 14 model parameters (γN, dNP, η, α, ν, ω, γm, ξ, τ, ρ1, ρ2, ρ3, dD, and kD), and solved simultaneously with the model equations (Equations (12)-(18) in the main text) using dde23 in Matlab. The corresponding logarithmic sensitivity solution curves are presented in Figures S1-S8. To plot the sensitivity solution curves, model parameters have been classified into those related to neutrophils (γN, dNP and η), to cytokines (α, ν and ω), to monocyte-derived macrophages (γm, ξ and τ) and to debris (ρ1, ρ2, ρ3, dD and kD). Each set of parameters is plotted separately for the high (P0 = 10^5 CFU/ml) and the intermediate (P0 = 10^4 CFU/ml) initial inocula.

<a id='43af3e6f-8cb6-4f45-99db-9693d1ac67ff'></a>

Figures S1-S8 represent the effect that positive perturbations in the model parameters have on solutions. For example, an increase in the parameters $\gamma_N$ (rate of bacterial clearance by neutrophils) or $\eta$ (rate of neutrophil recruitment) impacts the bacterial solution negatively (Figure S1a and S2a). That is, for instance, increasing the rate of bacterial clearance by

<a id='d21b6c00-a0da-4693-8660-7a6f0b4db26b'></a>

3

<!-- PAGE BREAK -->

<a id='dcbc41a1-49fa-419d-8f4a-6f93ade8478d'></a>

neutrophils ($\gamma_N$) results in a decrease in the bacterial population, with a 100% decrease by 4 hours postinoculation when $P_0$ = 10⁵ CFU/ml (Figure S1a inset). Furthermore, the effect of both of these parameters continues to increase with time until approximately 10 hours postinoculation when $P_0$ = 10⁴ CFU/ml (Figure S2) and approximately 60 hours postinoculation when $P_0$ = 10⁵ CFU/ml (Figure S1). At this point, the effect begins to decrease before becoming negligible.

<a id='0076ebbb-41b7-4d75-bcf0-77f72cade35b'></a>

Similarly, an increase in the rate of bacterial clearance by monocyte-derived macrophages
($\gamma_m$), or equivalently an increase in the rate of macrophage recruitment ($\xi$), results in a
decrease of bacteria, although these effects occur later in the infection since macrophage
recruitment is later than neutrophil recruitment. Furthermore, the effect of perturbing $\gamma_m$
(or $\xi$) when P$_0$ = 10$^4$ CFU/ml is minimal (Figure S6), particularly compared to the higher
dose (Figure S5). Thus, as expected, the monocyte-derived macrophages play a more critical
role when the initial dose is high. On the contrary, the inhibition of bacterial clearance by
alveolar macrophages ($k_D$) is more sensitive to changes with the intermediate dose of bacteria
(Figure S8). This again highlights the importance of the trade-off between debris removal and
phagocytosis, particularly with an intermediate initial value of bacteria. The results of this
analysis also support the importance of bacterial-induced cytotoxicity ($d_{NP}$), particularly
with the intermediate initial inocula (Figure S2) since the effects can be neutralized by an
increase in $\eta$ for high initial inocula (Figure S1).

<a id='cd02afd8-e60b-49d1-b4d7-bede1482dbd9'></a>

When interpreting the results in Figures S1-S8, the dynamics of the original model (Figure 6 in the main text) must be taken into consideration. At the low initial inocula, P_0 = 10^3 CFU/ml, bacteria are immediately cleared by alveolar macrophages and the dynamics of all other populations are absent. Therefore, we do not include the results when P_0 = 10^3 CFU/ml since any changes induced by perturbations in model parameters are negligible. Similarly, the effect of parameter perturbations on the model solution are insignificant after 36-40 hours for the intermediate initial condition P_0 = 10^4 CFU/ml. For instance, changes in the bacterial population resulting from an increase in γ_m, ξ or τ do not begin until

<a id='82ea6bf2-d7be-49f8-86e7-deffc3c369d8'></a>

4

<!-- PAGE BREAK -->

<a id='560bf753-8b03-4f1d-8703-57517980b71b'></a>

approximately 30 hours (Figure S6a). Thus, altering the value of these parameters has only minimal effects on the model solution. This is not the case, however, for the neutrophil and macrophage populations. For these dynamics, we must interpret the sensitivity analysis results (i.e., Figures S2ce, S4ce, S6ce, and S8ce) for longer than 40 hours since these two cell types remain in high levels throughout the simulation (see Figure 6ce in the main text).

<a id='81caf1df-9312-4ac9-8c6f-1ebde1d6907e'></a>

On the other hand, for the high initial condition P₀ = 10⁵ CFU/ml, only two populations, cytokine and debris, reach low levels at approximately 40 hours (see Figure 6bd in the main text), and thus changes induced by parameter perturbations are insignificant after this time point. In this case, it is necessary to examine the results for all other populations (bacteria, neutrophils, macrophages, and epithelial cells) for the entire length of the simulation (i.e., Figures S1acefg, S3acefg, S5acefg, and S7acefg).

<a id='322fe82a-a5ea-4393-b1b3-71077878909a'></a>

It is also important to note the scales in Figures S1-S8. Although many of the curves have similar dynamics, their scales vary. When comparing the results for each of the initial conditions, P₀ = 10⁵ CFU/ml and P₀ = 10⁴ CFU/ml, the effects are usually more pronounced for the higher initial condition. One exception is in the sensitivity analysis for the debris parameters (Figures S7 and S8), where perturbations lead to greater changes with the intermediate initial condition than with the high initial condition. The changes in these debris parameters, however, are generally insignificant compared to parameters related to neutrophils (Figures S1 and S2), cytokines (Figures S3 and S4) and macrophages (Figures S5 and S6).

<a id='7b152525-a6fe-456e-b1a4-f85d3668e36c'></a>

5

<!-- PAGE BREAK -->

<a id='d9795eaa-08fa-44e7-a4a6-658637c4e8ed'></a>

<::A line graph titled "(a)" shows "Bacteria - qP_q/P" on the y-axis (ranging from -10 to 4, multiplied by 10^4) against "Time (hours)" on the x-axis (ranging from 0 to 120). Three lines are plotted: a green line representing q=γ_N, a black line representing q=d_NP, and an orange line representing q=η. The graph also includes an inset plot, zoomed into the initial section of the main graph. The inset plot shows the same three lines for "Time" from 0 to 15 hours and "Bacteria - qP_q/P" from -1 to 1.::>

<a id='8ac40489-3f3d-4332-b8b5-fd18845d023d'></a>

<::Line chart labeled (b) showing "Cytokine - qCq/C" (scaled by 10^4) on the y-axis versus "Time (hours)" on the x-axis. The x-axis ranges from 0 to 120 hours, and the y-axis ranges from -7 to 3. Three distinct curves are plotted: a black curve, a green curve, and an orange/yellow curve. The black curve starts near 0, rises to a peak around 2.5, then decreases, crosses 0, and rises again. The green curve starts near 0, decreases significantly to a trough around -7, then rises and crosses 0. The orange/yellow curve starts near 0, decreases slightly, then rises to a peak around 1, and then decreases. An inset chart provides a magnified view of the initial segment from 0 to 15 hours on the x-axis and -1 to 1 on the y-axis, illustrating the early behavior of the three curves.: chart::>

<a id='acbe31a5-74e7-4dbc-8799-8925e1e818fd'></a>

<::A line graph titled "(c)" shows Neutrophils - qN_q/N on the y-axis against Time (hours) on the x-axis. The x-axis ranges from 0 to 120 hours, and the y-axis ranges from -16000 to 8000. There are three distinct lines: a black line, an orange line, and a green line, all exhibiting oscillatory behavior over time. The black line starts near 0, dips to approximately -2000, rises to about 5000, then dips again to around -2000. The orange line starts near 0, rises to approximately 2000, dips to about -8000, then rises again to around 2000. The green line starts near 0, rises to approximately 6000, dips significantly to about -16000, then rises again to around 4000. An inset graph provides a zoomed-in view of the initial segment of these lines, with its x-axis ranging from 0 to 15 and its y-axis from -1 to 1. In the inset, the black line dips slightly below 0, the orange line rises above 0 to about 1, and the green line also rises above 0.::>

<a id='6c905394-7c28-474b-acc9-2b1522d29635'></a>

<::Line chart titled (d) showing "Debris - qD_q / D" on the y-axis (ranging from -5 x 10^4 to 2 x 10^4) versus "Time (hours)" on the x-axis (ranging from 0 to 120). Three distinct lines are plotted: a black line, an orange line, and a green line. The black line starts near 0, peaks around 1.5 x 10^4 at approximately 75 hours, then decreases and crosses the x-axis around 95 hours before rising slightly. The orange line starts near 0, decreases to a trough around -2 x 10^4 at approximately 80 hours, then increases to cross the x-axis around 105 hours. The green line starts near 0, decreases to a trough around -4.8 x 10^4 at approximately 75 hours, then increases to cross the x-axis around 95 hours. An inset plot provides a magnified view of the data from 0 to 15 hours on the x-axis and from -1 to 1 on the y-axis. In the inset, the black line rises to a peak around 1, the orange line rises to a peak around 0.8, and the green line decreases from 0.: chart::>

<a id='9b271e1b-bc30-4d19-a756-ab683e070c23'></a>

<::A line graph titled "Macrophages - qM_q/M" on the y-axis and "Time (hours)" on the x-axis, labeled (e). The y-axis ranges from -2000 to 2000, with major ticks at 400 unit intervals. The x-axis ranges from 0 to 120 hours, with major ticks at 20 hour intervals. Three lines are plotted: a green line, an orange line, and a black line. All three lines start near 0. The green line rises to a peak around 1700 at approximately 70 hours, then falls to about -800 at 120 hours. The orange line rises to a peak around 800 at approximately 70 hours, then falls to about -200 at 120 hours. The black line initially drops to about -600 at approximately 70 hours, then rises to about 200 at 120 hours. An inset graph is located in the bottom left, showing a zoomed-in view of the main graph for the initial 15 hours. The inset's y-axis ranges from -1 to 1, and its x-axis ranges from 0 to 15 hours. In the inset, the green, orange, and black lines are all very close to 0, with the orange line slightly positive, and the green and black lines slightly negative within this initial time frame.: chart::>

<a id='3a7d2109-6da2-4eaf-85a0-384af327075f'></a>

<::A line graph titled (f) shows "Susceptible Epithelial Cells - qE_U,q / E_U" (multiplied by 10^4) on the y-axis and "Time (hours)" on the x-axis, ranging from 0 to 120 hours. The main plot displays three lines: a green line, an orange line, and a black line. The green line starts near 0, rises to a peak of approximately 1.2 x 10^4 around 80 hours, and then slightly declines. The orange line also starts near 0, rises to a peak of approximately 0.5 x 10^4 around 80 hours, and then slightly declines. The black line starts near 0 and gradually decreases to approximately -0.4 x 10^4 by 120 hours. An inset plot provides a magnified view of the initial phase (0 to 15 hours on the x-axis, -1.6 to 1 on the y-axis), showing the same three lines: the green and orange lines rising sharply from near 0, and the black line decreasing sharply from near 0.: chart::>

<a id='f0df8158-5f1a-4c58-aa9d-846a23db90fd'></a>

<::Line graph showing the change in "Epith. Cells With Bact. Attached - qE_A,q / E_A" (multiplied by 10^4) over "Time (hours)". The x-axis ranges from 0 to 120 hours. The y-axis ranges from -7 to 2 (representing -7 x 10^4 to 2 x 10^4). Three distinct lines are plotted: a black line, a green line, and an orange line. The black line starts near 0, peaks around 70 hours at approximately 2.2 x 10^4, then drops to a trough around 90 hours at approximately -0.5 x 10^4, and returns to near 0 by 120 hours. The green line starts near 0, drops significantly to a trough around 75 hours at approximately -6.5 x 10^4, then rises to a peak around 95 hours at approximately 2.2 x 10^4, and ends near 0. The orange line starts near 0, drops to a trough around 70 hours at approximately -3 x 10^4, then rises to a peak around 95 hours at approximately 1 x 10^4, and ends near 0. A label "(g)" is present near the peak of the green line. An inset graph provides a zoomed-in view of the early time points (0 to 15 hours). In the inset, the x-axis is Time (hours) from 0 to 15, and the y-axis ranges from -1 to 1. The black line in the inset rises from 0 to about 1. The green line in the inset drops from 0 to about -1. The orange line in the inset drops from 0 to about -0.5.: figure::>

<a id='652fa4de-a717-4eae-9d37-14a30038c8c5'></a>

Figure S1: Logarithmic sensitivity solutions for $\gamma_N$ (rate of bacterial clearance by neutrophils), $d_{NP}$ (rate of bacterial-induced neutrophil death), or $\eta$ (rate of neutrophil recruitment) when the initial condition of bacteria is $P_0 = 10^5$ CFU/ml.

<a id='16273386-d033-4aba-bbc1-b52dbddd1d91'></a>

6

<!-- PAGE BREAK -->

<a id='d2d114b4-6bf9-49f7-93dd-0de75fbf20f0'></a>

<::chart: A multi-panel line chart showing logarithmic sensitivity solutions over time. All panels share a common x-axis labeled 'Time (hours)' ranging from 0 to 80. A common legend indicates three lines: a green dashed line for 'q=γN', a black dashed line for 'q=dNP', and an orange dashed line for 'q=η'. The panels are: (a) Bacteria - qP/P, with a y-axis from -60 to 60. (b) Cytokine - qC/C, with a y-axis from -50 to 10. (c) Neutrophils - qN/N, with a y-axis from -25 to 5. (d) Debris - qD/D, with a y-axis from -80 to 10. (e) Macrophages - qM/M, with a y-axis from -18 to 2. (f) Susceptible Epithelial Cells - qEU,q/EU, with a y-axis from -4 to 20. (g) Epith. Cells With Bact. Attached - qEA,q/EA, with a y-axis from -60 to 10. The lines in each panel show the sensitivity of the respective quantity to changes in γN, dNP, or η.::>Figure S2: Logarithmic sensitivity solutions for γN (rate of bacterial clearance by neutrophils), dNP (rate of bacterial-induced neutrophil death), or η (rate of neutrophil recruitment) when the initial condition of bacteria is P0 = 10^4 CFU/ml.

<a id='e4615073-0207-4417-94cc-fae63b2887d2'></a>

7

<!-- PAGE BREAK -->

<a id='09557828-74ae-4826-a97c-c8ccac12d864'></a>

<::Figure S3 consisting of 7 subplots (a) through (g) showing logarithmic sensitivity solutions. The x-axis for all subplots is 'Time (hours)', ranging from 0 to 120. Each subplot includes an inset showing a zoomed-in view of the initial part of the curves (Time 0 to 15 hours). Three lines are plotted in each subplot: cyan for q=α, magenta for q=v, and dark blue for q=ω. :chart::>
<::Subplot (a) shows 'Bacteria - qP/P' (scaled by x 10^4) on the y-axis, with values ranging from -4 to 0.5. The cyan line starts at 0, dips to about -3.5 around 50 hours, then rises to 0.5 around 90 hours, and ends near 0. The magenta line starts at 0, dips to about -1.5 around 40 hours, rises to 0.5 around 80 hours, and ends near 0. The dark blue line starts at 0, dips to about -3.5 around 50 hours, then rises to 0.5 around 90 hours, and ends near 0. :chart::>
<::Subplot (b) shows 'Cytokine - qC/C' (scaled by x 10^4) on the y-axis, with values ranging from -3 to 0.5. The cyan line starts at 0, dips to about -2.5 around 50 hours, then rises to 0.5 around 90 hours, and ends near 0. The magenta line starts at 0, dips to about -1.5 around 40 hours, rises to 0.5 around 80 hours, and ends near 0. The dark blue line starts at 0, dips to about -2.5 around 50 hours, then rises to 0.5 around 90 hours, and ends near 0. :chart::>
<::Subplot (c) shows 'Neutrophils - qN/N' on the y-axis, with values ranging from -6000 to 2000. The cyan line starts at 0, dips to about -5000 around 50 hours, then rises to 2000 around 90 hours, and ends near 1000. The magenta line starts at 0, dips to about -1000 around 40 hours, rises to 1000 around 80 hours, and ends near 500. The dark blue line starts at 0, dips to about -5000 around 50 hours, then rises to 2000 around 90 hours, and ends near 1000. :chart::>
<::Subplot (d) shows 'Debris - qD/D' on the y-axis, with values ranging from -18000 to 4000. The cyan line starts at 0, dips to about -16000 around 50 hours, then rises to 4000 around 90 hours, and ends near 2000. The magenta line starts at 0, dips to about -8000 around 40 hours, rises to 2000 around 80 hours, and ends near 1000. The dark blue line starts at 0, dips to about -16000 around 50 hours, then rises to 4000 around 90 hours, and ends near 2000. :chart::>
<::Subplot (e) shows 'Macrophages - qM/M' on the y-axis, with values ranging from -800 to 600. The cyan line starts at 0, dips to about -600 around 50 hours, then rises to 600 around 90 hours, and ends near 300. The magenta line starts at 0, dips to about -200 around 40 hours, rises to 200 around 80 hours, and ends near 100. The dark blue line starts at 0, dips to about -600 around 50 hours, then rises to 600 around 90 hours, and ends near 300. :chart::>
<::Subplot (f) shows 'Susceptible Epithelial Cells - qE_U,q/E_U' on the y-axis, with values ranging from -5000 to 5000. The cyan line starts at 0, rises to about 4000 around 100 hours, and ends near 4000. The magenta line starts at 0, rises to about 1000 around 100 hours, and ends near 1000. The dark blue line starts at 0, rises to about 4000 around 100 hours, and ends near 4000. :chart::>
<::Subplot (g) shows 'Epith. Cells With Bact. Attached - qE_A,q/E_A' (scaled by x 10^4) on the y-axis, with values ranging from -2.5 to 1. The cyan line starts at 0, dips to about -2 around 50 hours, then rises to 0.5 around 90 hours, and ends near 0. The magenta line starts at 0, dips to about -0.5 around 40 hours, rises to 0.5 around 80 hours, and ends near 0. The dark blue line starts at 0, dips to about -2 around 50 hours, then rises to 0.5 around 90 hours, and ends near 0. :chart::>
Figure S3: Logarithmic sensitivity solutions for α (rate of cytokine production from epithelial cells), ν (rate of cytokine production from alveolar macrophages), or ω (rate of bacterial attachment to epithelial cells) when the initial condition of bacteria is $P_0 = 10^5$ CFU/ml.

<a id='24af65bd-70e6-4561-9c74-b23ab391ce73'></a>

8

<!-- PAGE BREAK -->

<a id='95b84d11-11fc-4761-b3e6-e10aa380924f'></a>

<::chart: A multi-panel line chart titled "Logarithmic sensitivity solutions for α (rate of cytokine production from epithelial cells), ν (rate of cytokine production from alveolar macrophages), or ω (rate of bacterial attachment to epithelial cells) when the initial condition of bacteria is P₀ = 10⁴ CFU/ml." The chart consists of seven subplots (a-g), each showing the logarithmic sensitivity over time (hours) for different biological components. The legend for all subplots is: q=α (cyan dashed line), q=ν (magenta dashed line), q=ω (blue dashed line). All x-axes are labeled "Time (hours)" ranging from 0 to 80.  (a) Bacteria - qP/P: The magenta line shows a significant increase, peaking around 40 hours, then gradually decreasing. The cyan and blue lines show an initial decrease, then an increase, followed by a decrease, with the cyan line decreasing more sharply towards 80 hours. (b) Cytokine - qC/C: All three lines show a sharp decrease, reaching a minimum around 10-15 hours, then increasing and stabilizing, with the magenta line stabilizing at a higher value than the cyan and blue lines. (c) Neutrophils - qN/N: Similar to (b), all three lines show a sharp decrease, reaching a minimum around 10-15 hours, then increasing and stabilizing, with the magenta line stabilizing at a higher value than the cyan and blue lines. (d) Debris - qD/D: Similar to (b) and (c), all three lines show a sharp decrease, reaching a minimum around 10-15 hours, then increasing and stabilizing, with the magenta line stabilizing at a higher value than the cyan and blue lines. (e) Macrophages - qM/M: All three lines show an initial decrease, reaching a minimum around 20-25 hours, then increasing and stabilizing, with the magenta line stabilizing at a higher value than the cyan and blue lines. (f) Susceptible Epithelial Cells - qE_U,q / E_U: The cyan and blue lines show an increase and then stabilize at different positive values. The magenta line increases, then decreases, stabilizing at a lower positive value. (g) Epith. Cells With Bact. Attached - qE_A,q / E_A: All three lines show a sharp decrease, reaching a minimum around 10-15 hours, then increasing and stabilizing, with the magenta line stabilizing at a higher value than the cyan and blue lines.::>

<a id='2013c063-f0ac-42c7-930e-6f1552f9385e'></a>

9

<!-- PAGE BREAK -->

<a id='0c48d68c-063f-4688-ae24-ae168e5e67e6'></a>

<::transcription of the content: chart::>Figure S5: Logarithmic sensitivity solutions for $\gamma_m$ (rate of bacterial clearance by monocyte-derived macrophages), $\xi$ (rate of monocyte-derived macrophage recruitment), or $\tau$ (time delay before monocyte-derived macrophage recruitment) when the initial condition of bacteria is $P_0 = 10^5$ CFU/ml.The figure displays seven line graphs, labeled (a) through (g), showing logarithmic sensitivity solutions over time (hours). All graphs share the same x-axis, "Time (hours)", ranging from 0 to 120. A common legend is present in panel (a): q=$\gamma_m$ (black line), q=$\xi$ (red line), and q=$\tau$ (blue line). (a) Y-axis: Bacteria - qP_q/P. The blue line shows a large peak around 1300 at 60 hours, then drops below zero before rising again. The red and black lines remain close to zero with minor fluctuations. (b) Y-axis: Cytokine - qC_q/C. The blue line shows a large peak around 1000 at 60 hours, drops to -400, then rises. The red and black lines remain close to zero with minor fluctuations. (c) Y-axis: Neutrophils - qN_q/N. The blue line peaks around 160 at 70 hours, drops to -75, then rises. The red and black lines remain close to zero with minor fluctuations. (d) Y-axis: Debris - qD_q/D. The blue line peaks around 800 at 60 hours, drops to -300, then rises. The red and black lines remain close to zero with minor fluctuations. (e) Y-axis: Macrophages - qM_q/M. The blue line drops to -25 at 40 hours, then rises to 10. The red and black lines peak around 7 at 60 hours, then drop. (f) Y-axis: Susceptible Epithelial Cells - qE_U,q/E_U. The blue line drops to -250 at 80 hours, then rises. The red and black lines rise to 75 at 80 hours, then drop slightly. (g) Y-axis: Epith. Cells With Bact. Attached - qE_A,q/E_A. The blue line peaks around 900 at 70 hours, then drops to -300. The red and black lines remain close to zero with minor fluctuations.::>

<a id='18d03a0d-7872-479b-9e47-daa87c390518'></a>

10

<!-- PAGE BREAK -->

<a id='942517c6-4661-45ad-ab1e-268eee6d658c'></a>

<::Figure S6: Logarithmic sensitivity solutions for γm (rate of bacterial clearance by monocyte-derived macrophages), ξ (rate of monocyte-derived macrophage recruitment), or τ (time de-lay before monocyte-derived macrophage recruitment) when the initial condition of bacteria is P0 = 10^4 CFU/ml.

This figure consists of 7 subplots (a-g) showing logarithmic sensitivity solutions over time (hours). The legend indicates three lines: black dashed for q=γm, red dotted for q=ξ, and blue dashed for q=τ.

(a) Bacteria - qPq/P: Y-axis ranges from -14 to 8. The black dashed line remains near 0, then slightly increases. The red dotted line decreases from 0 to -14. The blue dashed line increases from 0 to 8.
(b) Cytokine - qC/C: Y-axis ranges from -0.04 to 0.16. The black dashed line remains near 0. The red dotted line decreases from 0 to -0.02. The blue dashed line increases from 0 to 0.14.
(c) Neutrophils - qN/N: Y-axis ranges from -0.04 to 0.06. The black dashed line remains near 0. The red dotted line fluctuates around 0, peaking at 0.01 and then decreasing to -0.01. The blue dashed line decreases to -0.03, then increases to 0.05.
(d) Debris - qD/D: Y-axis ranges from -0.04 to 0.18. The black dashed line remains near 0. The red dotted line decreases from 0 to -0.02. The blue dashed line increases from 0 to 0.17.
(e) Macrophages - qM/M: Y-axis ranges from -5 to 1. The black dashed line remains near 0. The red dotted line remains near 0. The blue dashed line decreases to -5, then increases to 0.
(f) Susceptible Epithelial Cells - qE_U,q/E_U: Y-axis ranges from -0.10 to 0.02. The black dashed line remains near 0. The red dotted line increases from 0 to 0.02. The blue dashed line decreases from 0 to -0.09.
(g) Epith. Cells With Bact. Attached - qE_A,q/E_A: Y-axis ranges from -0.04 to 0.16. The black dashed line remains near 0. The red dotted line decreases from 0 to -0.02. The blue dashed line increases from 0 to 0.15.
: chart::>

<a id='4e5d5c23-c58f-4f7e-a767-0a4ea316b717'></a>

11

<!-- PAGE BREAK -->

<a id='f2387edb-223e-4050-baff-8c1d1210271c'></a>

<::A line chart with an inset plot. The main chart's y-axis is labeled "Bacteria - qP_q/P" and ranges from -0.6 to 0.6. The x-axis is labeled "Time (hours)" and ranges from 0 to 120. Two prominent curves are displayed: a magenta line representing q=ρ_1 and a green line representing q=k_D. The chart is identified by the label (a). An inset plot is superimposed on the main chart, sharing the same x-axis range of 0 to 120. Its y-axis ranges from -0.03 to 0.02. This inset plot shows three curves: a yellow line for q=ρ_2, a black line for q=ρ_3, and a cyan line for q=d_D. A legend on the right side of the main plot provides the color-coding for all five curves: magenta for q=ρ_1, green for q=k_D, yellow for q=ρ_2, black for q=ρ_3, and cyan for q=d_D.: chart::>

<a id='b7b1e3e0-c61c-45b3-acd4-972918d5e892'></a>

<::transcription of the content: chart::>
Figure S7: Logarithmic sensitivity solutions. The figure displays three subplots, (b), (d), and (f), each showing logarithmic sensitivity solutions over time.

**(b)**
*   **Y-axis:** Cytokine - qC_q/C
*   **X-axis:** Time (hours) from 0 to 120
*   **Main Plot:** Shows green and magenta lines starting near 0, rising to a peak around 0.4 at approximately 60-70 hours, then decreasing to around 0.1 at 120 hours. There are also black, yellow, and cyan lines, which are more visible in the inset.
*   **Inset Plot:** Y-axis from -0.03 to 0.01. Shows black and yellow lines staying close to 0, while the cyan line dips to approximately -0.025 around 70 hours.

**(d)**
*   **Y-axis:** Debris - qD_q/D
*   **X-axis:** Time (hours) from 0 to 120
*   **Main Plot:** Shows a magenta line starting around 1.0, dipping slightly, then rising to approximately 1.2 at 120 hours. A green line starts near 0, rises to a peak around 0.25 at approximately 80 hours, then decreases. There are also black, yellow, and cyan lines, which are more visible in the inset.
*   **Inset Plot:** Y-axis from -3 to 1. Shows black and yellow lines staying close to 0, while the cyan line dips to approximately -2.8 around 70 hours.

**(f)**
*   **Y-axis:** Susceptible Epithelial Cells - qE_U,q/E_U
*   **X-axis:** Time (hours) from 0 to 120
*   **Main Plot:** Shows green and magenta lines starting near 0, decreasing to approximately -0.07 at around 80 hours, then rising slightly to around -0.06 at 120 hours. There are also black, yellow, and cyan lines, which are more visible in the inset.
*   **Inset Plot:** Y-axis from -2 to 3 (scaled by x 10^-3). Shows black and yellow lines staying close to 0, while the cyan line rises to approximately 3 x 10^-3 around 80 hours.

<a id='de95dab4-3669-47a0-9205-242cbbf8db73'></a>

<::A line graph titled "(c)" shows "Neutrophils - qNq/N" on the y-axis ranging from -0.16 to 0.08, and "Time (hours)" on the x-axis ranging from 0 to 120. There are two curves plotted: one in green and one in magenta. The green curve starts at 0, dips to about -0.04 around 40 hours, rises to about 0.08 around 75 hours, and then dips back towards 0. The magenta curve closely follows the green curve, overlapping for most of its length.An inset line graph is present within the main graph. Its y-axis is labeled "x 10^-3" and ranges from -6 to 2. Its x-axis implicitly corresponds to "Time (hours)" and ranges from 0 to 120. This inset graph displays three curves: one in cyan, one in black, and one in yellow. The cyan curve shows a dip around 60-80 hours, reaching approximately -6. The black curve has a peak around 70-80 hours and a dip around 40-50 hours. The yellow curve shows a peak around 90-100 hours and a dip around 60-70 hours.: chart::>

<a id='c187785a-e483-4687-bdc7-3ee45d7dd918'></a>

<::Figure (e) is a line graph showing Macrophages - qM_q/M (x 10^-3) on the y-axis against Time (hours) on the x-axis, ranging from 0 to 120. The y-axis ranges from -16 to 8. There are three lines plotted: a green line, a magenta line, and another line (initially overlapping with the green line). All lines start near 0. The green and magenta lines diverge from the initial line around 40 hours, decreasing to a minimum around 70 hours, then increasing to a peak around 100 hours, and finally decreasing again towards 120 hours. The magenta line is slightly above the green line after the peak. An inset plot is located in the bottom left, showing values (x 10^-4) on its y-axis, ranging from -6 to 4, against Time (hours) on its x-axis, ranging from 0 to 120. This inset plot contains three lines: a cyan line, a yellow line, and a black line, all showing oscillations around zero. The cyan line shows a larger oscillation, going negative, then positive, then negative again. The yellow and black lines show smaller oscillations, mostly staying between -2 and 2 (x 10^-4).: chart::>

<a id='cddc0d21-bc09-466a-b53a-f90473a9395b'></a>

<::Figure S7: Logarithmic sensitivity solutions for ρ₁ (amount debris from bacterial-induced neutrophil death), ρ₂ (amount debris from neutrophil death), ρ₃ (amount debris from epithelial cell death), d_D (rate of debris removal by alveolar macrophages) or k_D (rate of phagocytosis inhibition) when the initial condition of bacteria is P₀ = 10⁵ CFU/ml. The figure contains two plots, (f) and (g), each with an inset plot. Plot (f) shows time (hours) on the x-axis from 0 to 120. The y-axis ranges from 0 to -0.08. Two main lines, green and magenta, show varying values over time. The inset in plot (f) shows time (hours) on the x-axis from 0 to 120, and the y-axis ranges from -2 to 3, multiplied by 10^-3. Four lines, cyan, yellow, black, and green, show varying values. Plot (g) shows time (hours) on the x-axis from 0 to 120. The y-axis is labeled "Epith. Cells With Bact. Attached - qE_A,q / E_A" and ranges from 0.4 to -0.4. Two main lines, green and magenta, show varying values over time. The inset in plot (g) shows time (hours) on the x-axis from 0 to 120, and the y-axis ranges from 0.01 to -0.03. Three lines, cyan, yellow, and black, show varying values.::>

<a id='7c2cc923-2632-47ce-a61e-cd53f4971b22'></a>

-o
neut
ithel
phag

<!-- PAGE BREAK -->

<a id='b29a5437-6e5b-4dbf-aa06-04af8b05c70c'></a>

<::A line graph titled "(a)" with an inset plot. The main plot shows "Bacteria - qPq/P" on the y-axis, ranging from -6 to 12, against "Time (hours)" on the x-axis, ranging from 0 to 80. Five dashed lines are plotted: a magenta line representing q=ρ1, a yellow line representing q=ρ2, a black line representing q=ρ3, a cyan line representing q=dD, and a green line representing q=kD. The green line starts at 0, rises to a peak of about 8 around 8 hours, then decreases to -6 around 40 hours, and then rises sharply to 12 by 80 hours. The cyan line stays around 0 for the first 20 hours, then decreases to about -7 at 55 hours, and then rises back towards 0. The inset plot, located in the top middle, shares the same x-axis (Time (hours) from 0 to 80) and shows a y-axis ranging from 0 to 0.04. It displays the magenta, yellow, and black dashed lines. The magenta line in the inset peaks around 10-20 hours, the black line peaks around 50-60 hours, and the yellow line peaks around 60-70 hours. All lines in the inset show low values, mostly below 0.01, except at their peaks.: chart::>

<a id='d2f72b6f-bb73-4b81-adc3-d17a3b05a30f'></a>

<::chart: The figure displays six plots, arranged in two columns and three rows, labeled (b), (d), and (f) for the left column plots. Each plot shows the logarithmic sensitivity solutions over time (hours). The x-axis for all main plots ranges from 0 to 80 hours. Each of the left-column plots includes an inset plot showing a magnified view of certain curves. The various dashed lines (green, cyan, magenta, black, yellow) represent different sensitivity parameters.

- **Panel (b) (Top Left): Cytokine - qC/C**
  - Y-axis ranges from -1 to 7.
  - The green dashed line shows a peak around 10 hours and then decreases, while the cyan dashed line remains relatively flat near zero.
  - Inset plot: Y-axis from 0 to 0.03, showing magenta, black, and yellow dashed lines, all very close to zero after an initial rise.

- **Panel (Top Right): Neutrophils - qN/N**
  - Y-axis ranges from -0.5 to 3.5.
  - The green dashed line peaks around 10 hours and then decreases, while the cyan dashed line remains near zero.

- **Panel (d) (Middle Left): Debris - qD/D**
  - Y-axis ranges from -6 to 10.
  - The green dashed line peaks around 10 hours and then decreases, while the cyan dashed line decreases steadily.
  - Inset plot: Y-axis from 0 to 1.0, showing magenta, black, and yellow dashed lines, with magenta staying high and black/yellow decreasing.

- **Panel (Middle Right): Macrophages - qM/M**
  - Y-axis ranges from 0 to 2.5.
  - The green dashed line shows a small increase after 10 hours, while the cyan dashed line remains near zero.

- **Panel (f) (Bottom Left): Susceptible Epithelial Cells - qE_U,q/E_U**
  - Y-axis ranges from -1.8 to 0.2.
  - The green dashed line decreases significantly around 10-20 hours and then stabilizes, while the cyan dashed line remains near zero.
  - Inset plot: Y-axis from -8 x 10^-3 to 0 x 10^-3, showing magenta, black, and yellow dashed lines, with magenta showing a significant negative deflection.

- **Panel (Bottom Right): Epith. Cells With Bact. Attached - qE_A,q/E_A**
  - Y-axis ranges from -1 to 8.
  - The green dashed line peaks around 10 hours and then decreases, while the cyan dashed line remains near zero.

Figure S8: Logarithmic sensitivity solutions for ρ₁ (amount neutrophil death), ρ₂ (amount debris from neutrophil death), epithelial cell death), dD (rate of debris removal by alveolar phagocytosis inhibition) when the initial condition of bacteria::>


<a id='9590d619-be71-45ee-b6f7-54f968654e2f'></a>

<::chart: Three plots showing changes over time (hours) with insets. The x-axis for all main and inset plots is "Time (hours)".

Plot (c):
Main plot: Y-axis is "Neutrophils - qN_q/N", ranging from -0.5 to 3.5. A green dashed line shows a sharp increase to a peak around 3.5 at 10 hours, then decreases rapidly. A light blue dashed line stays close to 0.
Inset plot: Y-axis is scaled by "x 10^-3", ranging from 0 to 15. A magenta dashed line peaks around 12 x 10^-3 at 10 hours. A yellow dashed line shows a smaller peak around 10 hours. A black dashed line stays near 0.

Plot (e):
Main plot: Y-axis is "Macrophages - qM_q/M", ranging from 0 to 2.5. A green dashed line shows an increase to a peak around 2.3 at 25 hours, then decreases. A light blue dashed line stays close to 0.
Inset plot: Y-axis is scaled by "x 10^-3", ranging from 0 to 8. A magenta dashed line peaks around 8 x 10^-3 at 25 hours. A yellow dashed line shows a smaller peak around 25 hours. A black dashed line stays near 0.

Plot (g):
Main plot: Y-axis is "Epith. Cells With Bact. Attached - qE_A,q/E_A", ranging from -1 to 8. A green dashed line shows an increase to a peak around 8 at 10 hours, then decreases, going below 0. A light blue dashed line stays close to 0.
Inset plot: Y-axis ranges from 0 to 0.03. A magenta dashed line peaks around 0.03 at 10 hours. A yellow dashed line shows a smaller peak around 10 hours. A black dashed line stays near 0.
:chart::>
or ρ₁ (amount debris from bacterial-induced
trophil death), ρ₃ (amount debris from ep-
l by alveolar macrophages) or k_D (rate of
ion of bacteria is P₀ = 10⁴ CFU/ml. 
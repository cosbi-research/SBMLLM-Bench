<a id='57da1bd9-a557-445d-b081-8b7a16379e41'></a>

DEPARTMENT OF HEALTH & HUMAN SERVICES - USA

# HHS Public Access
Author manuscript
*Math Med Biol.* Author manuscript; available in PMC 2015 September 09.

<a id='3497f5cf-3002-4081-b50d-a306d7b50ffc'></a>

Published in final edited form as:
_Math Med Biol._ 2015 September; 32(3): 285–306. doi:10.1093/imammb/dqu008.

<a id='c34304db-cd79-4ed3-b650-338dd03d96e6'></a>

Modelling the interaction between the host immune response,
bacterial dynamics and inflammatory damage in comparison
with immunomodulation and vaccination experiments

<a id='7e599937-922d-4ddf-a856-f315b863cfaf'></a>

Angela M. Jarrett,
Department of Mathematics, Florida State University, 1017 Academic Way, Tallahassee, FL
32306, USA

<a id='047e8aa6-5c08-498c-a1f9-7db160ee8572'></a>

N.G. Cogan, and
Department of Mathematics, Florida State University, 1017 Academic Way, Tallahassee, FL
32306, USA

<a id='6833a74a-e14b-4804-b27a-e7c6acb16ca9'></a>

M.E. Shirtliff
Department of Microbial Pathogenesis, Dental School, University of Maryland, Baltimore, MD,
USA

<a id='14a0dbcf-4de8-40e4-bfca-c2a61abae6b5'></a>

# Abstract
The immune system is a complex system of chemical and cellular interactions that responds quickly to queues that signal infection and then reverts to a basal level once the challenge is eliminated. Here, we present a general, four-component model of the immune system's response to a *Staphylococcal aureus* (*S. aureus*) infection, using ordinary differential equations. To incorporate both the infection and the immune system, we adopt the style of compartmenting the system to include bacterial dynamics, damage and inflammation to the host, and the host response. We incorporate interactions not previously represented including cross-talk between inflammation/damage and the infection and the suppression of the anti-inflammatory pathway in response to inflammation/damage. As a result, the most relevant equilibrium of the system, representing the health state, is an all-positive basal level. The model is able to capture eight different experimental outcomes for mice challenged with intratibial osteomyelitis due to *S. aureus*, primarily involving immunomodulation and vaccine therapies. For further validation and parameter exploration, we perform a parameter sensitivity analysis which suggests that the model is very stable with respect to variations in parameters, indicates potential immunomodulation strategies and provides a possible explanation for the difference in immune potential for different mouse strains.

<a id='c3c31b9a-b38e-4e6a-b43a-7dc90ee1b1b5'></a>

## Keywords
immunology; mathematical modelling; MRSA; osteomyelitis

<a id='f8601822-0681-4885-afdc-5eab18573f1c'></a>

Corresponding author: ajarrett@math.fsu.edu.

<a id='2b2436fc-5423-4f8e-a9f3-6ccd462a2e3a'></a>

Author Manuscript

<a id='335a59ee-e9da-45b0-829f-98e2964c1fb8'></a>

Author Manuscript

<a id='589253e2-dfde-47d5-9147-8f8cf05fbc20'></a>

Author Manuscript

<a id='93129e77-49a7-45c1-9361-783c40c74c9b'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='fc6075b2-d192-4ba9-b987-53ed90d5aa0b'></a>

Jarrett et al.

<a id='11978053-028c-4509-bfda-87376d5e55c2'></a>

Page 2

<a id='918e24e6-f9d7-494a-9aee-a7ecdc5e6f68'></a>

# 1. Introduction

## 1.1 Overview

<a id='1c50e98b-4b6d-4212-a6d6-418f1ba6044e'></a>

When a pathogen enters a host, a complex sequence of responses takes place to remove the challenge and prevent any further damage. In most instances, a healthy body's immune system is successful in eliminating the foreign microbes; however, there are several possible complications that can arise. The infection may become endemic, or there may be reoccurring bouts of infection followed by periods of relative inactivity. Each of the outcomes hinge on the interplay between the immune system and the bacterial dynamics. The goal of this investigation is to determine if a simple compartmental model which incorporates the known major interactions can reflect each of the outcomes of recent experimental results for mice challenged with osteomyelitis due to *Staphylococcal aureus* (*S. aureus*). The model presented serves to develop and test treatment methods as well as a building block for more detailed biofilm models.

<a id='79ba78b8-a2ef-415b-afad-efdafe67a7c6'></a>

There are many layers to the immune system involving cellular, chemical and neural pathways. We used a simplified system of components: the pro-inflammatory response, which in regard to the experiments described later, represents the inflammatory cytokines and cells of the *Th1* and *Th17* responses (IL-2, IL-12p70, IL-6, IL-17, TNF-α, IL-1β, neutrophils) and the anti-inflammatory response for the *Th2* and *Treg* responses (IL-4, IL-10). Another component of the model is 'inflammation', which is used as a general compartment which we choose to represent higher blood flow, cellular damage and pro-inflammatory chemical signalling. Before a challenge, the immune system is maintained at a low level of activation with no active response and low levels of passive/innate response components (Delves & Roitt, 2000b). Under ideal circumstances, the interplay between the pro-inflammatory, anti-inflammatory and 'inflammation' components will bring the body back to a basal or healthy level.

<a id='eb62a1e6-ad0f-48bd-9230-fa4015c4a30e'></a>

Finding the best course of treatment for pathogens that overwhelm the immune system's response such as persistent infections due to *S. aureus*, both Methicillin Sensitive and Methicillin Resistant (MRSA) strains, and *Streptococcus spp.* is a difficult problem. One of the goals of this study is to develop a model that incorporates current observations—in particular, how different parameter regimes reflect observable outcomes regarding bacterial clearance, proper immune response and vaccine strategies. In the next section, we overview the specific biological observations that we incorporate into the model.

<a id='8a65297b-6772-437b-8703-b020ad339a18'></a>

## 1.2 Biological background
It is difficult to eliminate and prevent aggressive infections using standard treatment protocols (Shirtliff et al., 2001). Treatment is often complicated for infections caused by strains that are resistant to an array of antimicrobial agents, such as MRSA (Gould et al., 2012). This pathogen is a rising problem, not only from infections such as skin, soft tissue, pneumonia or musculoskeletal infections, but also due to the burgeoning increase in the use, and the resulting infections of, indwelling medical devices such as intravenous catheters and prosthetic implants. MRSA has a number of genetically encoded resistance mechanisms, such as efflux pumps, antibiotic-degrading/deactivating enzymes or altering the antibiotic

<a id='18027d86-34ed-4ce4-9e7b-b325229273ef'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='0867ee14-db36-422a-af7f-8438f7e71cca'></a>

Author Manuscript

<a id='2cc0257a-726f-447d-b462-a3a018b21acd'></a>

Author Manuscript

<a id='20a2bfe0-6ad5-4d3f-87f7-b602026ea214'></a>

Author Manuscript

<a id='a615a526-8e93-4ec6-8619-22e68d0e0cfd'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='a36088b1-2f84-432c-9b3e-49c3c8a25e0f'></a>

Jarrett et al.

<a id='f70898fd-7c4e-4379-93bf-8ba4f8d80f24'></a>

Page 3

<a id='12a041df-9a92-4833-9c2e-e516472f868b'></a>

target. MRSA can also tolerate high levels of antibiotics to which it is normally sensitive due to its growth as a community of microbes termed biofilm. Biofilms are formed by bacteria attaching to a surface and embedding themselves in an extracellular hydrated slime matrix derived from both the microbes themselves and the host (Shirtliff et al., 2002). This forms a source of infection that resists clearance by the host immune response and antimicrobial agents.

<a id='1edae4ac-8846-4ca5-a6e5-d662a50e9c90'></a>

Despite genetically encoded resistance mechanisms, the antibiotic tolerance enjoyed by the microbes within a biofilm is due to a variety of protective mechanisms including reduced antibiotic penetration, low metabolic rate and specialized phenotypic expression (Gilbert et al., 1990; Proctor et al., 1998; Stewart & Costerton, 2001; Thien-Fah et al., 2001; Stewart, 2003). These tolerance mechanisms enable 10²- to 10³-fold increased tolerance to antimicrobial agents compared with their free-floating, planktonic counterparts. There is also growing evidence that the biofilm mode of growth increases the spread of advantageous mutations that induce drug resistance (Cogan, 2006). Therefore, biofilm infections usually cannot be resolved using antimicrobial agents alone, and once a mature biofilm forms within the host, surgical removal of the biofilm becomes necessary to eliminate the infection, causing significantly more morbidity, mortality and complications for the patient (Prabhakara et al., 2011b).

<a id='4a7cc819-a057-46f7-8ea7-e74caafef14c'></a>

In this study, the pathogen is treated as a growing population whose growth depends explicitly on the inflammation and damage—which we generalize as our 'inflammation' component of the model. Studies have shown that biofilm infections can benefit from inflammatory responses which increase the level of nutrients to the area. One example of this is *Helicobacter pylori*, which infects a nutrient poor area of the stomach between epithelial and mucosal layers. Activation of the pro-inflammatory response makes nutrients available to these bacteria for growth (Baldari et al., 2005). In addition, there is evidence suggesting that *S. aureus* can induce pro-inflammatory cytokines (Assenmacher et al., 1998; Sinha et al., 1999; Breuer et al., 2005). In inducing a pro-inflammatory response, *S. aureus* can then lyse leucocytes and blood cells brought by increased blood flow using a variety of different toxins, and then subsequently use several types of uptake systems to collect nutrients (Dinges et al., 2000). This is in addition to the eukaryotic extracellular matrix proteins brought to the infection which the bacteria target to attach and promote colonization. The pro-inflammatory component of the immune system decreases the pathogen level as leucocytes attack the infection. Simultaneously, the bacteria increase the damage to the host. In the beginning stages of biofilm development, a flood of proteins are expressed by *S. aureus* to promote adherence and colonization. Many of these proteins cause damage to the host to harvest nutrients for colony growth. This formation of biofilm is the root of osteomyelitis, which is the focus of the biological experiments that the model reflects (Brady et al., 2006). This coupled interaction between the infection and inflammation/ damage is a distinction of the current study.

<a id='b097dbc3-4449-4831-8905-429ee19370e7'></a>

The Shirtliff group at the University of Maryland has been interested in identifying new ways to prevent these biofilm infections such as vaccines and immunomodulation. They have performed a series of experiments to identify different aspects of the immune response to osteomyelitis in mice. In these experiments, S. aureus biofilms were grown on a pin and

<a id='15f36162-a12b-4946-9280-efc1d2269da4'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='2b7d6a30-1c1f-4d33-b78b-7d1e47c3773b'></a>

Author Manuscript

<a id='32e23c57-5708-4558-9b50-dec30277ce63'></a>

Author Manuscript

<a id='3f130d31-5a03-4b29-9546-65b3480359a6'></a>

Author Manuscript

<a id='0fbd2fd2-2cfa-42bb-bc8c-756f5140bb82'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='07d34216-9d20-417f-8f44-a63772bb6f80'></a>

Jarrett et al.

<a id='3e1be82f-3dc6-4e04-aa13-d3002f80c51b'></a>

Page 4

<a id='0ae7d46e-20e4-4622-b79c-00457cb189f7'></a>

implanted into the tibia of mice. At multiple days, post-infection, samples were collected in order to determine local cytokine production, regulatory T-cell (_Treg_) frequency and neutrophil infiltration and culture of bones was done to detect the presence of infection (Brady _et al._, 2011; Prabhakara _et al._, 2011a,b; Shirtliff _et al._, 2012).

<a id='7cb898b5-007c-4567-be0e-c6fee5044289'></a>

Three different strains of mice were used in these experiments, the main two being: BALB/c and C57BL/6. These mice strains have biased immune responses where C57BL/6 mice have dominant pro-inflammatory response (Th1 and Th17 cellular responses), and BALB/c mice have stronger anti-inflammatory responses (Th2 and Treg cellular responses) (Chen et al., 2005; Prabhakara et al., 2011a). Inflammation results in increased blood flow and inflammatory cell influx into areas of infection, which can often eliminate the invading pathogens. However, if not specific or overly activated, host tissue damage can result from uncontrolled inflammation. Contrasting these responses are the anti-inflammatory responses that reduce inflammation through host immune cells, cytokines and chemokines (Delves & Roitt, 2000a).

<a id='57780e9b-d7e1-457f-937c-8ea3ba56b3e4'></a>

The first of a series of experiments compared the immune responses of BALB/c and C57BL/6 mice. The infection was less severe in BALB/c mice than the C57BL/6 mice. BALB/c mice had increased anti-inflammatory (Th2 and *Treg*) cytokine levels, while C57BL/6 mice had increased inflammatory cytokines (IL-12, IL-17, TNF-*a* and IL-*B*).

<a id='6ab25cf7-fadb-4d97-93b9-b642c05526f5'></a>

In addition, they compared the neutrophil infiltration (damage caused by neutrophils moving into the infected area) at the pin implant site of the C57BL/6 and the BALB/c mice. After staining the tibia of the infected mice, they observed significant physiological disruption to the C57BL/6 tibia, whereas the BALB/c tibia looked like the C57BL/6 tibia implanted with sterile pins.

<a id='5e1bc4e3-5b8c-4b58-af6d-8ef21265b41f'></a>

To test the hypothesis that a robust *Th2* response allows the BALB/c mice to resolve the infection, they performed the same experiment on another strain of mice, STAT6 KO BALB/c. The STAT6 gene has well-documented roles in the differentiation of *Th2* cells, expression of cell surface markers and class switching of immunoglobulins. Therefore, the knockout strain has a *Th2* defect due to lack of this important component of the *Th2* signalling pathway. The STAT6 KO BALB/c experiment resulted in chronic infection for all the mice compared with clearance in the majority of wild-type BALB/c mice. This suggests that the *Th2* is necessary to eliminate *S. aureus* biofilm infections for BALB/c mice. However, these mice had similar gross morphology and bacterial numbers in their tibia to the wild-type BALB/c mice. Evidently, either the STAT6 KO BALB/c mice have a compensatory mechanism, like higher *Treg* levels, or the intense *Th1* and *Th17* responses of the C57BL/6 mice increased the severity of their infections (Prabhakara *et al*., 2011b).

<a id='0bdcbee7-c6a8-4a43-8fad-04e15184954e'></a>

By treating the BALB/c mice with anti-CD25 antibodies, the Shirtliff group was able to test whether the _Treg_ response was also necessary for the BALB/c mice to eliminate the infection. These antibodies effectively eliminate the majority of _Treg_ cells in the mice. From this experiment, they found that most of the BALB/c mice were no longer able to clear the infection without their _Treg_ cells (Prabhakara _et al_., 2011b).

<a id='9cc37663-525c-4dac-a18f-43a07e0319e4'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='b304a3b6-8b09-4ac6-974c-f9ba8e62aa8a'></a>

Author Manuscript

<a id='1791a32b-6bb8-4d6f-81c8-47256dae7365'></a>

Author Manuscript

<a id='ef435d10-20a2-45b8-9cfa-154e1fd23107'></a>

Author Manuscript

<a id='e4335327-1133-474c-97c2-2333b8f94482'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='b6b15c2c-4aef-45cf-84c3-37c0276a97d6'></a>

Jarrett et al.

<a id='f79513cf-4a8c-4428-a3bf-79a6a2a56d67'></a>

Page 5

<a id='d400fbab-78af-445c-b78b-45bcaa679d8a'></a>

To determine if the pro-inflammatory (Th1 and Th17) responses of the C57BL/6 mice exacerbate the infection, they treated these mice with two different types of antibodies. First, they treated with antibodies against a Th17 cytokine (anti-IL-6) and then antibodies against a cytokine common to both Th1 and Th17 immune responses (anti-IL-12p40). They observed a slight reduction of infection in the mice overall for the first antibody treatment, but with the combined antibody treatment, there was a significant reduction (Prabhakara et al., 2011b).

<a id='83a5ac08-e8ab-40fd-a7c1-43eb6fb35d25'></a>

Finally, the Shirtliff group developed two different vaccines for osteomyelitis caused by MRSA. Efforts towards vaccine development for MRSA is important due to their antibiotic resistance and ability to form a biofilm. However, S. aureus presents major challenges to current vaccine strategies which are not addressed by the majority of these vaccine development efforts (including polymicrobial infection, biofilm maturation and host carrier status). For a full discussion on the development of vaccines for S. aureus, see (Harro et al., 2010). Bacterial vaccines can consist of various types (killed-whole bacteria, live-attuentuated bacteria, toxoid, protein only, polysaccharide only and protein–polysaccharide conjugate (Harro et al., 2010)); the two vaccines described here use target proteins specific to the S. aureus biofilm as antigens.

<a id='ca8c4a78-8171-4f6b-b70f-373f42c262b6'></a>

Without vaccination, it is understood that the C57BL/6 mice would not have a quick or strong enough immune response to these antigens before a protective biofilm matrix forms at the implant site. The first vaccine showed some protection against an _S. aureus_ biofilm infection. However, since the vaccine was composed of biofilm-specific antigens only, adjunctive antibiotic therapy was required in these studies to clear the free-floating, and antibiotic-sensitive, planktonic populations (Brady _et al._, 2011). These planktonic populations are often shed from the biofilm colony/structure. The second vaccine was a pentavalent (five-component) vaccine consisting of the original four components of the earlier vaccine with an additional antigen. The additional antigen is expressed by the planktonic bacteria _in vivo_ during the infection. The five-component vaccine provided complete protection and elimination of _S. aureus_ populations in the mouse model with prosthetic implant infections (Shirtliff _et al._, 2012).

<a id='c400c25a-caf1-480d-8c33-a17ab181ac5d'></a>

In the model we present below, we do not look at specific elements of the immune system but at general components. Therefore, we do not include the vaccine directly into the model, but adjust parameters that govern the affected components. The functions of host antibodies include neutralization, aiding in removal and destruction of pathogens (especially bacteria). In addition, recent evidence shows that plasma cells (activated B cells which are the source of antibodies) produce pro-inflammatory cytokines (Vettermann et al., 2011). Since our pro-inflammatory response is the only component that eliminates/prevents infection, we consider these vaccination benefits pro-inflammatory. We specify the particular parameter changes below.

<a id='99e799bd-19d0-44f5-9857-bdd78260592a'></a>

For a summary of the mouse strains and their basic biological elements, see Table A1 in the Appendix.

<a id='8d6d1b3c-7624-4baf-8e9e-ede836e8a14d'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='a31f3a5a-88be-4846-a136-09eef47d3f8f'></a>

Author Manuscript

<a id='01fa7403-2262-4b72-9659-b07efe42d2b0'></a>

Author Manuscript

<a id='e3fca13b-060a-47b5-bc39-9c1c93e36040'></a>

Author Manuscript

<a id='7f8eead7-32cd-4240-b2e9-2619dc7f9f5a'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='775dcf89-6c9b-4328-8e67-543e97bed85d'></a>

Jarrett et al.

<a id='8bdb4149-cb03-4fc4-b44f-166c5467121b'></a>

Page 6

<a id='56291f08-20a6-4386-a8b1-c6c3bd283933'></a>

## 1.3 Mathematical background
Many models have been developed to describe the immune system including the causes and affects of inflammation. Considering the number of interconnected components of the immune system, including the signalling cytokines, active cellular machinery and the transduction of the cytokine signal, detailed models require a substantial number of variables and assumptions which can be problematic since many of these immune system components are not completely characterized (Wigginton & Kirschner, 2001; Marino & Kirschner, 2004; Marino et al., 2004; Chow et al., 2005; Gammack et al., 2005). Although these models are more biologically detailed, they can be quite difficult to analyse and are not as well-suited for developing a general understanding of the main components.

<a id='08a55e3c-0023-45da-b184-10e8fd8a2a10'></a>

In an attempt to handle the complexity of the immune system, many modellers take a simplified, mechanistic approach. For example, in one study, the pro-inflammatory response was divided into two components: early and late (Kumar et al., 2004). This model was capable of describing many clinically relevant outcomes but without specific experiments/organisms implicated. In an extended model, the anti-inflammatory response was incorporated and played several important roles in the system's recovery (Day et al., 2006; Reynolds et al., 2006). In particular, the anti-inflammatory component was responsible for expanding the basin of attraction for the healthy steady state. In a similar model, the anti-inflammatory response was included to determine if the anti-inflammatory cytokines could be applied as a therapy to suppress chronic inflammation (Herald, 2010). These successful compartmental models are the groundwork for our current study.

<a id='b6c3788c-7573-474d-a058-dc55b7895ea8'></a>

In choosing the compartmental approach, we present a four-component ordinary differential equation model that includes the inflammatory immune response to an infection of S. aureus. This model incorporates an immune response consisting of three elements: the pro-inflammatory response, anti-inflammatory response and inflammation, similar to the previous work mentioned above, which first incorporated and explored the addition of the anti-inflammatory response (Day et al., 2006; Reynolds et al., 2006), but there are several notable differences.

* We use simpler kinetics to reduce the number of parameters required—specifically, we eliminate the use of Michaelis–Menten kinetics for more direct interactions.
* We also require that the model exhibit a natural basal level when there is no pathogen exposure (an all-positive equilibrium), reflecting the disease-free state. This is separate from an all-zero equilibrium which remains unstable throughout.
* An additional, and important, direct interaction between the inflammation damage and bacterial pathogen is included, where the pathogen benefits from the inflammation/damage and also causes inflammatory damage.
* Another direct interaction between the inflammation/damage and anti-inflammatory response is included where the anti-inflammatory response is hindered by the inflammation/damage.

<a id='4c76dbf9-1177-45e5-8224-40cc3ed06152'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='21a87cf2-cb6d-4a86-95ef-a7a292cb8796'></a>

Author Manuscript

<a id='5fbfe8ca-7e4b-4bd8-ad9e-540a1d7a0fe7'></a>

Author Manuscript

<a id='2cb8975a-feae-46ca-8ea8-1890513932d1'></a>

Author Manuscript

<a id='2dcd43bb-cc96-4ce3-ac04-9adf14cdab4c'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='54768744-8edb-4417-a550-67172df57068'></a>

Jarrett et al.

<a id='4410eb53-6d75-426c-a114-b3b0658bc658'></a>

Page 7

<a id='8b4e7937-fd23-44cc-9b0a-73adc8141cc2'></a>

* Finally, we consider alterations in the parameters that are motivated by a range of experiments with different mouse strains (i.e. different immune potential) and vaccine strategies.

<a id='4cdb963e-ce72-4891-b82f-02d1f9b8c445'></a>

This model is capable of capturing this range of experiments—indicating the flexibility of the model structure. In addition, the results of a parameter sensitivity analysis indicate that the model is stable with respect to variations in the parameters, and the analysis suggests an explanation for the difference in immune potential between two of the mouse strains.

<a id='efb8d32c-13ed-4118-91f7-9967354d8a00'></a>

The interactions included in this system were motivated by the experimental designs described above and recent biological evidence. We also dynamically link the decay rates of the pro- and anti-inflammatory responses with the presence of an infection to reflect the immune system's ongoing effort (Coxon et al., 1999). With these modifications, we are able to include the different mice strains and vaccine strategies needed to represent the Shirtliff experiments (Brady et al., 2011; Prabhakara et al., 2011b; Shirtliff et al., 2012).

<a id='aa8cf392-251e-49b6-8a47-5972d17eccbf'></a>

The model is simple and does not incorporate the interactions of specific cell types and chemical signalling; despite this, we found that it can predict several clinically relevant outcomes. The model includes 16 parameters, some of which can be well-estimated. For the linear stability analysis, we used Maple to determine equilibria and their eigenvalues for stability. In order to evaluate the effect of variations in the other key parameters, we performed a sensitivity analysis and found that our results are quite robust to a range of perturbations.

<a id='7b1bc239-7929-4efb-9589-1aa303ec5b48'></a>

## 2. Model

We now introduce the full model which consists of four components: pro- (P) and anti-inflammatory (A) responses, inflammation (I) and a bacterial infection (B). Inflammation represents the damage caused by an injury or a pathogen, and the pro- and anti-inflammatory responses are the components of the immune system that work to repair damage and eliminate the problem-causing issue. The bacterial component directly interacts with the pro-inflammatory response and inflammation of the immune system subsystem (Fig. 1). The full system is as follows:

<a id='19f3345a-7b6b-423e-8c61-da011ff1b91f'></a>

dP/dt = (α₁I + ρ₁B)(1 - P) - [β₁A + μ₁(1 - B/K_B)]P, (2.1)

<a id='0c5e2977-e64b-4e5e-b4d7-738aab0a79ec'></a>

$\frac{dA}{dt} = \alpha_2P - \left[ \beta_2I + \mu_2 \left(1 - \frac{B}{K_B}\right) \right] A, (2.2)$

<a id='cae95364-cb50-4081-ae10-e967d5eb2ce1'></a>

dI/dt = α₃P + ρ₂B - (β₃A + μ₃)I, (2.3)

<a id='8cd8094a-b3c0-417a-b06b-b88c6ac5efef'></a>

$$\frac{dB}{dt} = \left[g\left(1 - \frac{B}{K_B}\right) + \alpha_4 I - \beta_4 P\right] B + e^{-\gamma t}. \quad (2.4)$$

<a id='349ef4ce-ff3c-4951-85f0-26472ce6b1a7'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='1731c5e9-8688-499f-b616-acb0b96c68bf'></a>

Author Manuscript

<a id='7303696d-756b-46fb-ba70-032a1fbe76bb'></a>

Author Manuscript

<a id='ab22a8ca-5d98-4c7d-8b51-d68f9bfd4ad9'></a>

Author Manuscript

<a id='fe556ea2-4cc7-4941-91c9-6d6a7b50cf20'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='cd8b05d3-a095-4fb4-b0c7-a4e3589a2ce2'></a>

Jarrett et al.

<a id='c2ec5eb3-b54c-413e-a4dd-a3cedeff3aef'></a>

Page 8

<a id='95dc5c54-6c2f-45a0-b765-a06e0b1a29cc'></a>

The pro-inflammatory component (P) is the combined efforts of the *Th1* and *Th17* responses of mice described by the Shirtliff group. This response is recruited by inflammation with rate α₁. However, this recruitment is not exponential. Since the immune system is designed with a maximal, active capacity, it depends on the amount of the pro-inflammatory response present. This is similar to Kumar et al. (2004), but we do not make the assumption that this includes anti-inflammatory cytokines but treat the anti-inflammatory response separately.
The pro-inflammatory also depends on the bacterial presence with rate ρ₁. The pro-inflammatory response is down-regulated by the anti-inflammatory response directly with rate β₁, and it decays at a rate µ₁. In addition, we assume that the natural decay rate decreases when bacteria are present in the system, agreeing with the biological evidence that the production of granulocyte/macrophage colony-stimulating factor (GM-CSF) released by activated endothelial cells causes anti-apoptotic activity and enhanced survival in neutrophils (Coxon et al., 1999).

<a id='e1b97be7-acd8-4955-890e-023e874a4513'></a>

The anti-inflammatory component (A) represents the effort of the *Treg* cells. In the model,
the anti-inflammatory response is recruited by the pro-inflammatory response at rate *a₂*.
This is a simplification since the anti-inflammatory response is actually recruited by the
inflammation. We make this simplifying assumption because the anti-inflammatory
response should not be effective against the inflammation until macrophages (part of the
pro-inflammatory response) are activated, similar to Herald (2010). This separate activation
is the 'reprogramming' of already active macrophages by *Treg* cells. The anti-inflammatory
response is decreased by inflammation caused by platelet blockage impeding *Treg*
recruitment (Moura & Tjwa, 2010) with rate *β₂* and by its natural decay rate *µ₂*. We again
assume that the natural decay rate also depends on the magnitude of the infection since GM-
CSF affects monocytes as well and are the precursors for macrophages.

<a id='8844ca7b-bf46-4ab6-a5fe-383ad0146644'></a>

The inflammation component (I) reflects the damage caused by both the pro-inflammatory response and the bacteria. It is reduced by the anti-inflammatory response and natural decay. The coupling between the pathogen and damage has not been incorporated in previous models and plays a key role in our results. The pro-inflammatory response and infection cause the inflammation to increase with rates α3 and ρ2, respectively. The inflammation is reduced by the immune system's anti-inflammatory response with rate β3 and by its natural decay rate represented by μ3.

<a id='a7417fdf-f186-4401-b41f-0f8b70958824'></a>

The bacteria component (B) is treated as a growing population that benefits from inflammation—unlike previously mentioned models (Kumar et al., 2004; Reynolds et al., 2006; Herald, 2010) and is reduced by the pro-inflammatory response. We use logistic-type growth since we are not accounting for nutrient for the bacteria to harvest from the body where g is the growth rate. The bacteria directly benefit from the inflammation with rate α4 and are eliminated by the pro-inflammatory response with rate β4. In addition, we include a source term e^-γt representing the initial source of the biofilm infection which was incorporated to better represent the slowly decaying infection from the pin in the experiments.

<a id='70f60ed3-4a0e-4f60-b13e-6bc4676fd003'></a>

We note that the *Th2* response is represented in the combination of both pro-inflammatory and anti-inflammatory components. *Th2* recruits cells to attack the biofilm (pro-

<a id='64b67be1-cfc8-4195-afe4-87c9ae415ab5'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='4f82e8ba-1e0d-4335-96b6-c8c0f65f76db'></a>

Author Manuscript

<a id='164fe8b4-c6b6-4f29-bebc-8d1a3e71303d'></a>

Author Manuscript

<a id='446d6acc-f1d0-4548-9922-bbc3138ac1f8'></a>

Author Manuscript

<a id='998ba101-5595-4113-b45f-2a13e9f2f982'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='2837ece8-861a-48d6-a01c-b9746471999b'></a>

Jarrett et al.

<a id='a51052a0-22bb-47c7-91ca-a22602c43e33'></a>

Page 9

<a id='a106c810-efe9-4b30-9d16-aaef54e24db9'></a>

inflammation component). *Th2* also produces cytokines that reduce the *Th1* and *Th17*
responses (anti-inflammatory component).

<a id='d49e3667-b190-463b-81a6-36ace5ea129e'></a>

These variables quantify the response of each component rather than give a quantitative count. In the experiments, the data that can be collected are those of the cytokine concentration, which is less useful in understanding the interactions at a mechanistic level. Our analysis combines several of the components the Shirtliff experiments describe and gives a qualitative relationship between the model predictions and the experimental data.

<a id='42c167b8-8f07-41bc-bac2-77b4b118890a'></a>

Without an infection, the immune subsystem has five equilibria. Only two of these equilibria are biologically relevant (they do not have any negative values). One of the biologically relevant equilibria is the all-zero equilibrium which is unstable (P, Ā, I) = (0, 0, 0). The other is a stable, non-zero (all-positive) equilibrium that is considered the natural basal level (P, Ā, I) ≈ (0.82, 0.20, 2.10). This is unlike the models previously mentioned where their healthy state does not correspond to a basal level due to a zero value for one of the immune system components (Kumar et al., 2004; Reynolds et al., 2006). Depending on which component is perturbed from this healthy equilibrium, the system will follow a particular recovery pathway.

<a id='a4b45246-bf9a-415b-bcba-4c04de5922b4'></a>

If only the inflammation is initially higher than the basal level, the pro-inflammatory response increases and then the anti-inflammatory response follows. Eventually all three components return back to the basal level. If only the initial amount of pro-inflammatory response is higher than the basal level, both the inflammation and anti-inflammatory responses increase in response to the pro-inflammatory signalling, and again, everything returns to the basal level. An increase in only the anti-inflammatory response results in the anti-inflammatory response simply returning to the basal level (see Fig. 2 for examples of the immune system responding to different initial conditions).

<a id='5929f184-88a0-4d22-9651-8cee35baf06b'></a>

As key parameters are changed, the healthy steady state, which has a low level of inflammation after bacterial challenge, moves to a chronically inflamed state. Notably, chronic inflammation persists even in the absence of bacterial challenge, which is a hallmark of that disease. The model does not admit a separate equilibrium from the basal level equilibrium but rather indicates that chronic inflammation is due to particular defects in the immune system and not necessarily caused by a particular event. This interpretation of chronic inflammation can be reached by:

* decreasing the anti-inflammatory response rate, a2, representing a deficiency in the anti-inflammatory response;
* increasing the production of inflammation/damage due to the pro-inflammatory response, a3, representing an immune response more sensitive to its own cells;
* increasing the rate at which inflammation hinders the anti-inflammatory response, B2, representing blockage to anti-inflammatory cells and cytokines/chemokines;
* and decreasing the rate at which the anti-inflammatory response reduces inflammation, B3, representing an ineffectiveness of the anti-inflammatory cells (Fig. 2).

<a id='c86161e5-db70-49b7-9faa-5bccc75b6110'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='19e40a61-0b32-4df9-8b25-6508b0367acd'></a>

Author Manuscript

<a id='a559d2ed-9c1f-4ff3-868c-294fa7a435eb'></a>

Author Manuscript

<a id='61bd6af0-d6b0-4457-977e-c29031d55190'></a>

Author Manuscript

<a id='e00e7f19-f091-4e8a-b428-2bcb4af086f4'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='a4aea238-51c0-4a7b-a90f-fe5f307579b4'></a>

Jarrett et al.

<a id='fdde511f-c059-4e8e-9394-770ae21b2738'></a>

Page 10

<a id='504f3b0d-a7ef-4b5f-8a27-0edcf33acb1a'></a>

These parameter changes allow for the healthy steady state to have a significantly higher level for at least it is inflammation component. Chronic inflammation is not of particular interest for the biological or mathematical models presented here, but we provide our interpretation for comparison back to the literature.

<a id='5a4ed618-6a5d-42d3-9574-4a5050bb7bd6'></a>

After adding the bacterial dynamics, several new steady states are obtained. Note that the source term for bacteria goes to zero, so our steady state and linearization calculations neglect that contribution. There are eight total equilibria for the full system. Depending on the parameter choices, there can be two to three biologically relevant equilibria (they do not have negative or imaginary values for any of the components). The most clinically relevant represent the clearance of the infection or a return to health (or perhaps chronic inflammation) and chronic infection, similar to previous work (Kumar et al., 2004; Reynolds et al., 2006; Herald, 2010). The values for the steady states and their eigenvalues vary for the different parameter choices for experiments. These are listed in the figures for the experimental results. There is also the all-zero equilibrium which remains unstable for all of our experiments.

<a id='b4f52b57-1f17-41fb-8b42-e9889f0ecfd7'></a>

The simplest medical state the model can achieve is bacterial clearance by the immune response followed by the suppression of the inflammation. Here the equilibrium has a zero value for the bacterial component and all positive values for the immune system components at the basal level ((P, Ã, Ī, B) ≈ (0.82, 0.20, 2.10, 0) with all negative eigenvalues for the BALB/c mouse parameter set).

<a id='aea05db4-5765-4a43-8c84-3d2f921dce34'></a>

By changing clinically relevant parameters, a new stable equilibrium is introduced with all positive values while the previous steady states (all-zero equilibrium and the healthy equilibrium) persist. There is a transfer in stability between the new, infected state and the healthy state. Similar switches were found in Kumar *et al.* (2004), Day *et al.* (2006), Reynolds *et al.* (2006) and Herald (2010) where detailed phase-plane analysis was used. By decreasing the pro-inflammatory effectiveness ($\beta_4$), the bacteria can survive the immune response. Alternatively, chronic infection can occur if the recruitment rate of the anti-inflammatory response is decreased ($\alpha_2$). By decreasing the rate at which the anti-inflammatory response eliminates inflammation ($\beta_3$, such as neutralizing *Treg* cells), we see a stable, chronic infection. Finally, by increasing the amount that the inflammation component hinders the anti-inflammatory response ($\beta_2$), the infection becomes chronic. The second and third parameter changes discussed above ultimately result in too strong a pro-inflammatory response for the anti-inflammatory response to compensate, which in turn causes too much inflammation/damage as seen by the evidence of neutrophil infiltration.

<a id='a8bc437b-b49c-4da1-afa5-f78aa2e58168'></a>

The model is also capable of representing both non-aggressive and aggressive species of bacteria. For the non-aggressive species (relatively low growth rate, g), the immune response is able to clear the infection. For more aggressive growth rates, the bacteria can still be cleared if the pro-inflammatory effectiveness ($\beta_4$) is increased. This shows a threshold between health and infection dependent upon the virulence of the pathogen, previously and extensively described in the exploration of a constant versus dynamical anti-inflammatory response (Reynolds et al., 2006). This is similar to work describing the competition between pathogenic and probiotic populations in the gut where if the pathogenic

<a id='82c3c076-07b2-4170-aeda-8ec76592a044'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='6affc8d0-2fc5-4e98-97d2-5f1a7baea110'></a>

Author Manuscript

<a id='d324982c-bd9c-4668-b35c-9011ff391b59'></a>

Author Manuscript

<a id='8329e521-c3e5-41fc-91fa-e4b1ca0202da'></a>

Author Manuscript

<a id='bc9b6242-51c4-4606-9f2e-622f60aee13b'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='85db1524-cfce-4b01-8a78-91c582e79155'></a>

Jarrett et al.

<a id='ce096034-e2b8-4434-9a86-51bdb6ab6389'></a>

Page 11

<a id='aac4068c-71e6-46e1-8810-0b36c5454b8f'></a>

growth rate exceeds a certain threshold, it dominates over the probiotic bacteria (Arciero et al., 2010).

<a id='68c062d0-d63c-44fb-a6e8-ef56746a3a9d'></a>

A summary of model assumptions is as follows:

* The bacteria do not hinder the pro- or anti-inflammatory responses (there are no direct inhibitory interactions from the bacteria to the pro- and anti-inflammatory responses).
* Bacteria induce more inflammation than the pro-inflammatory response (i.e. the body is more sensitive to invaders than its own cells, $\alpha_{3} > \rho_{2}$ for normal, effective immune systems).
* Inflammation is only suppressed by the anti-inflammatory response and a natural decay.
* The presence of bacteria decreases the rate of decay of the anti-inflammatory response.
* The pro-inflammatory cells respond more quickly to signals from host signals caused by inflammation than the pathogen itself ($\alpha_{1} > \rho_{1}$, for normal, effective immune systems).

<a id='3724ed3e-a46d-47d5-ab7d-ecb90a48eddf'></a>

## 3. Comparison with experimental results

In this section, we describe the results of several experiments using immunomodulation and specific mice strains. The Shirtliff lab investigated several levels of the immune responses of different types of mice and used different antibody treatments to further characterize those elements (Brady et al., 2011; Prabhakara et al., 2011b; Shirtliff et al., 2012). In each case, alterations in the related parameters in the model yield predictions that are consistent with the experiments. We note that previous models have been able to qualitatively describe clinically relevant states (e.g. persistent infection, clearance, etc.), but to our knowledge, none are specifically designed to compare with immunotherapy, vaccination or specific knock-out animal models. Reasonable changes to parameters in the current model can predict a wide range of experimental observations, indicating that the core model is capturing the dominant biological processes involved. The key contribution of our efforts indicates that the concept of 'inflammation' is more subtle than previously assumed and that simple compartmental models are capable of representing this complex system for specific biological experiments.

<a id='35378aef-be53-4027-80c7-1c6a6a4cf202'></a>

We have found that, for each experiment, the model gives similar results to those observed in the animal model experiments. We have included a table of parameters for the BALB/c mouse as our basis set of values (Table A2). The parameter values changed for each individual experiment are identified in the captions of each experiment's figure. For each of the experiments, we have included the stable equilibrium in the figure citations as well, along with their eigenvalues. For all the simulations, the initial values for the immune components are below basal level (but not zero), the idea being that post-surgical implantation the mice would have lost fluids and some immune capability.

<a id='b530e257-8e4e-465d-b045-40f435e5dfdd'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='a0acff4a-a7f5-4d01-9fed-c58b316799f3'></a>

Author Manuscript

<a id='91037dc0-b635-4027-ad5d-c0443e992962'></a>

Author Manuscript

<a id='c746a505-fa7a-4c55-857a-8b195507b021'></a>

Author Manuscript

<a id='a8336952-68b6-4980-a584-a449f416bba7'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='c68f9bb8-d227-4bfc-962f-3092b055ed80'></a>

Jarrett et al.

<a id='854006ba-392a-4f47-a1a8-e9b028822d95'></a>

Page 12

<a id='15688f16-dca5-4b1c-bcb5-2d4764a471a4'></a>

For a summary of the mathematical results compared with the biological results for each experiment, see Table A3.

<a id='7b38c89e-21de-40b9-b6ce-71de628d405c'></a>

**Experiment 1: BALB/c**
The mice of type BALB/c, which have *Th2* biased responses, are able to clear the infection when implanted with a biofilm covered pin. We consider this as our basis experiment for the parameters in the model. Our model captures the clearance of the infection by BALB/c mice (the steady state is for zero bacteria and basal levels of the immune system unlike Reynolds *et al*. (2006), with eigenvalues that have negative real parts differing from Kumar *et al*., 2004, see Fig. 3).

<a id='0fdbcd79-79a2-4fcd-83d3-89206eaba570'></a>

## Experiment 2: C57BL/6

Recall that the C57BL/6 mice have decreased *Th2* and *Treg* cytokines than BALB/c and are unable to clear the infection. Moreover, they have higher inflammation/neutrophil damage. Since the *Th2* component has both pro- and anti-inflammatory roles, with these mice we lowered the pro-inflammatory effectiveness against the infection by lowering *β4* lowered the reduction of the pro-inflammatory response by the anti-inflammatory response by decreasing *β1* and lowered the recruitment rate of the anti-inflammatory response by decreasing *α2*. The model reflects the inability of the immune system to clear the infection.
The model also indicates higher levels of inflammation that is consistent with the observation that C57BL/6 mice had higher neutrophil infiltration than the BALB/c mice. The inflammation part of the steady state for BALB/c is *I* ≈ 2.10, whereas for C57BL/6, in this experiment, it is *I* ≈ 2.69 (see Fig. 4).

<a id='30f6262f-32ae-45db-a774-13c8a0e66ca9'></a>

## Experiment 3: STAT6 KO BALB/c
STAT6 KO BALB/c mice entirely lack the *Th2* response. The parameters match the BALB/c parameters except for the pro-inflammatory effectiveness against the infection, which was lowered (*β4*). We also lowered the reduction of the pro-inflammatory response by the anti-inflammatory response (*β1*). Just as in the experiments, the infection is not cleared. In addition, these mice were found to have lower amounts of damage than C57BL/6 mice which is also predicted by the model (the inflammation component of the steady state for C57BL/6 is *I* ≈ 2.69, whereas for STAT6 KO BALB/c, it is *I* ≈ 1.56). Although these mice remain infected, the steady state has a lower amount of inflammation (see Fig. 5).

<a id='1118f5f3-a197-4368-8330-4606cfa12a30'></a>

## Experiment 4: BALB/c treated with anti-CD25 antibodies eliminating Treg populations

Experiments indicate that _Tregs_ protect BALB/c mice from chronic infection. To test this, BALB/c mice were treated with anti-CD25 antibodies against _Tregs_. By decreasing the rate, the anti-inflammatory response reduces the pro-inflammatory response (β₁) and the rate the anti-inflammatory response reduces inflammation (β₃), the model captures the experimental results. The model shows that damage and infection amounts remain significantly high (see Fig. 6).

<a id='1acc8ac8-22dc-4631-9b99-1017dfe28953'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='960eaf7f-7bfa-4bbf-bcb6-eae47f5f3494'></a>

Author Manuscript

<a id='f73fbec4-5e37-4650-929c-6fe3eedeaf22'></a>

Author Manuscript

<a id='2b64c0a0-dee7-491e-8862-d03c079aa34e'></a>

Author Manuscript

<a id='d9a93ec8-b9e8-432f-a70e-d7ffb2f16854'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='9490d719-fe25-4c52-a012-c5083f70755d'></a>

Jarrett et al.

<a id='98668417-15ae-4114-a938-d6c73a4c0f25'></a>

Page 13

<a id='61e9feb5-e193-417f-becf-69117de54b4c'></a>

**Experiment 5: C57BL/6 mice treated with anti-IL-6 antibodies reducing Th17**

C57BL/6 mice were given anti-IL-6 antibodies decreasing the _Th17_ response and the infection load (anti-IL-6, 15% of mice were able to clear the infection). Using the same parameters as the untreated C57BL/6 mice, with the exception of a reduction in the recruitment of the pro-inflammatory response (α₁) and lowering the rate of inflammation caused by the pro-inflammatory response (α₃, since the _Th17_ response was neutralized), the model indicates a lower level of infection but not a significant amount (similar to the observations in the physical experiments; see Fig. 7).

<a id='5ab96cb6-2ea8-491d-9080-0c136d31edad'></a>

**Experiment 6: C57BL/6 mice treated with anti-IL-12p40 antibodies reducing both the Th1 and Th17 host responses**

When C57BL/6 mice are treated with antibodies against a cytokine common to both _Th1_ and _Th17_, 62.5% of the mice remained infected. We lowered the two parameters discussed in experiment 5 even more (α1, α3). If the multiplier is reduced enough, the infection is cleared. This indicates that whether the mouse is able to clear the infection or not depends on a threshold of the _Th1_ and _Th17_ response and may vary within the mice, which could explain why 62.5% of the mice remained infected (see Fig. 8).

<a id='00529772-40b6-4668-add0-5385448e99b7'></a>

### Experiment 7: C57BL/6 and four-component vaccine

For another experiment, C57BL/6 mice were treated with four-component vaccine and antibiotics. With this vaccine, the pro-inflammatory response rate for the C57BL/6 mice is increased (a1), and the effectiveness of the pro-inflammatory response against infection is also increased (β4). Without the antibiotics, the vaccine is not sufficient to prevent infection (see Fig. 9). Antibiotics alone were also insufficient to clear the infection, and our model agrees with this.

<a id='2e57b6a0-29a9-461b-8fc2-d1608991aedf'></a>

**Experiment 8: C57BL/6 and five-component vaccine**
However, when C57BL/6 mice are treated with a five-component vaccine, the infection is prevented. For the five-component vaccine, we only increased the pro-inflammatory response rate to the same level as the four-component vaccine but increased the pro-inflammatory effectiveness against infection even more. By priming the immune system with this vaccine, it prepares the cells to be able to eliminate the infection faster and stronger. The model gives clearance of the infection (see Fig. 10).

<a id='2c0e232d-722d-4d74-bca6-6a56eff74236'></a>

## 4. Parameter sensitivity

One of the most useful tools that modellers use to understand the effects of uncertainty on model predictions is sensitivity analysis. This term refers to a broad group of methods that attempts to sort the parameters by their effect variations have on the model predictions. The value of this analysis is that the effects of parameters on the system can easily be identified and ranked accordingly without extensive exploration. The ability to identify parameters that exert more control on the output of the system provides insight into the biological processes that play a pivotal role. Additionally, for most biologically motivated mathematical models, parameters are approximated which leaves a certain level of uncertainty in model results, but if the majority of parameters can be identified as having low overall effect on the system, a

<a id='429d85d2-080d-42ab-a90a-84cbbc0e18a9'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='a9646c3d-c346-4bb7-8068-38baa1f5d02f'></a>

Author Manuscript

<a id='93b250c9-051e-4a35-ba3e-92f3dae7f024'></a>

Author Manuscript

<a id='349b68a1-cb1d-4192-9b94-7689a2c9c3d9'></a>

Author Manuscript

<a id='7490e56e-b78f-4286-bced-a6b0e4a513be'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='0ff2c1a8-7c78-4c8f-8bb1-88fa861e591f'></a>

Jarrett et al.

<a id='717aca1d-c973-4380-9c7e-6b569643ea5e'></a>

Page 14

<a id='87de6491-7d5f-43de-96ab-74b4bf6e66e9'></a>

degree of confidence is added to parameter approximations. Finally, identifying parameters that may be 'frozen' reduces the parameter space to explore.

<a id='0f831d51-4d37-48a0-8a6a-814418c49bef'></a>

We performed a parameter sensitivity analysis previously used for biological models for the parameters and initial conditions (Blower & Dowlatabadi, 1994). This sensitivity analysis is based upon Latin Hypercube Sampling (LHS) and the calculation of partial rank correlation coefficients (PRCCs). Sensitivity analysis indicates how changes in the values of a parameter affect the results of the model.

<a id='ce9c810b-90ff-4492-af0f-7525472d0c39'></a>

The first step in the analysis is to form the LHS matrix that organizes the parameter values for each of the N simulations. We are not able to draw any particular forms of probability distributions for our parameters, so we chose a uniform distribution with ranges between 0.002 and 7 for the parameters while the initial conditions range between 0.003 and 1. The distributions are divided into N intervals, where N is the number of simulations. The value K is the number of parameters being tested (here, K = 20, 16 parameters and 4 initial values). For our model, we choose N = 300 (it has been previously established that N > 4/3K must be satisfied (McKay et al., 1979; Blower & Dowlatabadi, 1994)). Each of these N parameter values are paired randomly with the N values of the other parameters. The LHS table is an NxK matrix. Once the LHS table has been established, N simulations are performed using parameter values from each of the rows of the LHS table. Next we calculate the PRCC value for each parameter and initial value corresponding to each output variable. As noted by Blower & Dowlatabadi (1994), a PRCC value indicates the monotonicity of the input variables (parameters) to the particular outcome variable. The sign of the PRCC indicates the qualitative relationship and the magnitude indicates the importance of the uncertainty.

<a id='8bf25c13-3c3b-43ab-aedb-8a22db9a027c'></a>

We found that none of the parameters gave a PRCC value greater than 0.5 (values are shown in Table A4 in the Appendix). Correlation values below 0.5 are considered not significant individually. This analysis implies that the model's results are stable for reasonable parameter choices.

<a id='9a6ee095-2cfb-49b9-8415-a5b27fd825b9'></a>

More interestingly, we found that some of the parameters did stand out from the others with their PRCC values—specifically α2, β2, α3 and α4, which can be used as targets for experiments. The parameters β2 and α4, parameters added for interactions not previously incorporated into models, may be, in fact, significant to the model outcomes, which we are currently exploring mathematically and experimentally. Alternatively, α2, the recruitment of the anti-inflammatory response, possibly provides an explanation for the differences in immune potential between the two different mouse strains even though several parameters change between these experiments. The parameters α2, β2 and α3 were identified earlier as possible parameters for changing the immune stability between states. It has been suggested previously that this type of sensitivity analysis can identify bifurcation parameters (Marino et al., 2008). This sensitivity analysis narrows down interesting parameters to be explored.

<a id='7780ab76-7a78-4908-bdb5-7eba4b747cc9'></a>

## 5. Discussion

With this model, we are able to predict the outcome of a wide range of specific experiments by reasonable alterations in the parameter values. The model was motivated and analysed with the aim of reflecting particular experiments that lead to biologically and clinically

<a id='7c9af67f-d607-4108-9f2a-3436acb54c80'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='da2746eb-0b49-40a0-b73e-d06692954844'></a>

Author Manuscript

<a id='cee58b9c-7b54-4506-83d0-678380790560'></a>

Author Manuscript

<a id='2fb44e9c-252c-4728-a42c-4cc6f21aca59'></a>

Author Manuscript

<a id='b646d346-2a04-400b-b15b-2a5681a9fb3b'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='0ea2e151-cb0f-4ff9-a6a2-8e9d350c0d31'></a>

Jarrett et al.

<a id='2eec9b44-851e-4ed0-976e-87acfbe98bea'></a>

Page 15

<a id='37da8162-819b-4d2e-8fa9-26115fe620cf'></a>

relevant vaccine strategies. We have incorporated several interactions including: the positive
feedback between the infection and inflammation, the dynamic decay rates for the pro- and
anti-inflammatory response when the pathogen is present, the negative effect of the
inflammation on the anti-inflammatory response and representing a slowly decaying
bacterial load rather than a single bolus.

<a id='faf1548b-cf2b-4ddd-8ae6-0277e1741c21'></a>

We have also performed a parameter sensitivity analysis to verify the acceptability of our parameter values—the parameter space already being smaller than some of other models mentioned previously. This analysis not only indicates that our parameter choices are reasonable but also that the model is very stable with parameter changes. This gives confidence that the model fit is robust—which is not the case for all models. In addition, the sensitivity analysis also provides guidance for which components of the immune system are important, and hence, good targets for immunotherapies.

<a id='3da88a74-ce2b-4a82-81b9-418047f0adf0'></a>

It is of particular importance that the core model can capture all of the relevant experimental outcomes—including the healthy basal state represented by a non-zero equilibrium—by altering certain parameters that are comparable with different experimental designs. We also provide an alternative interpretation for the chronic inflammation state not described as a separate equilibrium. Knowing that the model is able to predict each of these experimental outcomes allows for major insights about the system interactions for successful vaccine strategies.

<a id='bee3866b-09a9-43e6-99b0-c134f90da040'></a>

Not only can it predict experiments that manipulate the immune response, but it can also represent different mouse strains as well as the results from the introductions of both aggressive and non-aggressive species of bacteria. Perhaps this suggests that, mathematically, not every detail needs to be included to investigate a complex system. There is value for the biological investigators in being able to narrow down the scope of the characterization of the full immune response to the biofilm infections even though the exact mechanism may not be identified. However, the model can easily be built upon by adding more interactions as they are discovered, changing interactions to be less direct or expanding the model for more detailed biological interests.

<a id='f62b0994-5001-4b80-84ba-1694ed7717f2'></a>

Further experiments involving specific time course data are needed to investigate the
model's predictions for the behaviours of immune response components are accurate—such
as early spikes in the model results and oscillations which can be induced by certain
parameter changes not shown here. These behaviours are interesting biologically and are
already motivating future experiments.

<a id='56259acf-35f0-4530-9352-6e36e8866f6e'></a>

# Acknowledgments

<a id='04726dd4-68cb-4fd9-a741-3204e251614b'></a>

### Funding

N.G.C. was supported by National Science Foundation DMS-1122378 M.E.S. was supported by the NIH, National Institute of Allergy and Infectious Diseases (AI069568-02 and ARRA Supplement AI069568) and the National Institute of Dental and Craniofacial Research (DE016257).

<a id='3766ecb0-5472-4cd3-aacb-b1bf7a00a67b'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='191e46a7-6fd5-4e4e-88d0-c9ba1f0778e4'></a>

Author Manuscript

<a id='26569231-6573-4f59-8484-9779e27b236a'></a>

Author Manuscript

<a id='9214bdc7-f427-4811-946f-0fc8bd238dda'></a>

Author Manuscript

<a id='af39aa5b-37cf-4966-97fc-e19047e927d1'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='b2e1326e-92a6-4d32-8234-bb9e766b4862'></a>

Jarrett et al.

<a id='1c5974ad-1147-4983-9bf1-57ed5f4219f1'></a>

Page 16

<a id='b1835b4f-43ed-485a-975b-5b6d73769c6a'></a>

# References

<a id='8866b97a-0046-4117-8645-a6ea5ba79cb2'></a>

Arciero JC, Ermentrout GB, Upperman JS, Vodovotz Y, Rubin JE. Using a mathematical model to analyze the role of probiotics and inflammation in necrotizing enterocolitis. Plos One. 2010; 5:13.
Assenmacher M, Lohning M, Scheffold A, Manz RA, Schmitz J, Radbruch A. Sequential production of il-2, ifn-gamma and il-10 by individual staphylococcal enterotoxin b-activated t helper lymphocytes. Eur J Immunol. 1998; 28:1534-1543. [PubMed: 9603458]
Baldari CT, Lanzavecchia A, Telford JL. Immune subversion by helicobacter pylori. Trends Immunol. 2005; 26:199-207. [PubMed: 15797510]
Blower SM, Dowlatabadi H. Sensitivity and uncertainty analysis of complex-models of disease transmission—an hiv model, as an example. Int Stat Rev. 1994; 62:229-243.
Brady R, Leid J, Costerton J, Shirtliff M. Osteomyelitis: clinical overview and mechanisms of infection persistence. Clin Microbiol Newsl. 2006; 28:65-72.
Brady RA, O'May GA, Leid JG, Prior ML, Costerton JW, Shirtliff ME. Resolution of staphylococcus aureus biofilm infection using vaccination and antibiotic treatment. Infect Immun. 2011; 79:1797–1803. [PubMed: 21220484]
Brandwood A, Noble KR, Schindhelm K. Phagocytosis of carbon particles by macrophages invitro. Biomaterials. 1992; 13:646-648. [PubMed: 1391413]
Breuer K, Wittmann M, Kempe K, Kapp A, Mai U, Dittrich-Breiholz O, Kracht M, Mrabet-Dahbi S, Werfel T. Alpha-toxin is produced by skin colonizing staphylococcus aureus and induces a t helper type 1 response in atopic dermatitis. Clin Exp Allergy. 2005; 35:1088-1095. [PubMed: 16120092]
Chen X, Oppenheim JJ, Howard OMZ. Balb/c mice have more cd4(+)cd25(+) t regulatory cells and show greater susceptibility to suppression of their cd4(+)cd25(-) responder t cells than c57b1/6 mice. J Leukoc Biol. 2005; 78:114-121. [PubMed: 15845645]
Chow CC, Clermont G, Kumar R, Lagoa C, Tawadrous Z, Gallo D, Betten B, Bartels J, Constantine G, Fink MP, Billiar TR, Vodovotz Y. The acute inflammatory response in diverse shock states. Shock. 2005; 24:74-84. [PubMed: 15988324]
Cogan NG. Effects of persister formation on bacterial response to dosing. J Theor Biol. 2006; 238:694-703. [PubMed: 16125727]
Coxon A, Tang T, Mayadas TN. Cytokine-activated endothelial cells delay neutrophil apoptosis in vitro and in vivo: a role for granulocyte/macrophage colony-stimulating factor. J Exp Med. 1999; 190:923-933. [PubMed: 10510082]
Day J, Rubin J, Vodovotz Y, Chow CC, Reynolds A, Clermont G. A reduced mathematical model of the acute inflammatory response II. Capturing scenarios of repeated endotoxin administration. J Theor Biol. 2006; 242:237-256. [PubMed: 16616206]
Delves PJ, Roitt IM. Advances in immunology: the immune system—first of two parts. N Engl J Med. 2000a; 343:37-49. [PubMed: 10882768]
Delves PJ, Roitt IM. Advances in immunology: the immune system—second of two parts. N Engl J Med. 2000b; 343:108-117. [PubMed: 10891520]
Dinges MM, Orwin PM, Schlievert PM. Exotoxins of staphylococcus aureus. Clin Microbiol Rev. 2000; 13:16-34. [PubMed: 10627489]
Edelson PJ, Zwiebel R, Cohn ZA. Pinocytic rate of activated macrophages. J Exp Med. 1975; 142:1150-1164. [PubMed: 53258]
Gammack D, Ganguli S, Marino S, Segovia-Juarez J, Kirschner DE. Understanding the immune response in tuberculosis using different mathematical models and biological scales. Multiscale Model Simul. 2005; 3:312-345.
Gilbert P, Collier PJ, Brown MR. Influence of growth rate on susceptibility to antimicrobial agents: biofilms, cell cycle, dormancy, and stringent response. Antimicrob Agents Chemother. 1990; 34:1865-1868. [PubMed: 2291653]
Gould IM, David MZ, Esposito S, Garau J, Lina G, Mazzei T, Peters G. New insights into meticillin-resistant staphylococcus aureus (mrsa) pathogenesis, treatment and resistance. Int J Antimicrob Agents. 2012; 39:96-104. [PubMed: 22196394]

<a id='1ae274ab-f124-477c-9eb8-31d7f9f4c45c'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='ddff7249-693b-4ebe-b73f-068e98229c2a'></a>

Author Manuscript

<a id='bece4c66-3379-4d99-92cc-1fa844c5c09e'></a>

Author Manuscript

<a id='f49e8db2-597c-42ee-b332-6793d59650e7'></a>

Author Manuscript

<a id='5f90ceeb-ab91-4306-bc6f-63695094cddd'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='cd8c221b-82ed-4310-aab5-c8ff1af67f0f'></a>

Jarrett et al.

<a id='23337cab-de66-4662-b9ff-cc53179d067a'></a>

Page 17

<a id='8688ef6b-859b-493f-9b76-9593960f2037'></a>

Harro JM, Peters BM, O'May GA, Archer N, Kerns P, Prabhakara R, Shirtliff ME. Vaccine development in staphylococcus aureus: taking the biofilm phenotype into consideration. Fems Immunol Med Microbiol. 2010; 59:306-323. [PubMed: 20602638]
Herald MC. General model of inflammation. Bull Math Biol. 2010; 72:765-779. [PubMed: 19851812]
Huhn RD, Radwanski E, Gallo J, Affrime MB, Sabo R, Gonyo G, Monge A, Cutler DL. Pharmacodynamics of subcutaneous recombinant human interleukin-10 in healthy volunteers. Clin Pharmacol Ther. 1997; 62:171-180. [PubMed: 9284853]
Kumar R, Clermont G, Vodovotz Y, Chow CC. The dynamics of acute inflammation. J Theor Biol. 2004; 230:145-155. [PubMed: 15321710]
Marino S, Hogue IB, Ray CJ, Kirschner DE. A methodology for performing global uncertainty and sensitivity analysis in systems biology. J Theor Biol. 2008; 254:178-196. [PubMed: 18572196]
Marino S, Kirschner DE. The human immune response to mycobacterium tuberculosis in lung and lymph node. J Theor Biol. 2004; 227:463-486. [PubMed: 15038983]
Marino S, Pawar S, Fuller CL, Reinhart TA, Flynn JL, Kirschner DE. Dendritic cell trafficking and antigen presentation in the human immune response to mycobacterium tuberculosis. J Immunol. 2004; 173:494-506. [PubMed: 15210810]
Matsui H, Ito T, Ohnishi SI. Phagocytosis by macrophages 3. Effects of heat-labile opsonin and poly(1-lysine). J Cell Sci. 1983; 59:133-143. [PubMed: 6306023]
McKay MD, Beckman RJ, Conover WJ. A comparison of three methods for selecting values of input variables in the analysis of output from a computer code. Technometrics. 1979; 21:239-245.
Moura R, Tjwa M. Platelets suppress t(reg) recruitment. Blood. 2010; 116:4035-4037. [PubMed: 21088138]
Prabhakara R, Harro JM, Leid JG, Harris M, Shirtliff ME. Murine immune response to a chronic staphylococcus aureus biofilm infection. Infect Immun. 2011a; 79:1789-1796. [PubMed: 21282411]
Prabhakara R, Harro JM, Leid JG, Keegan AD, Prior ML, Shirtliff ME. Suppression of the inflammatory immune response prevents the development of chronic biofilm infection due to methicillin-resistant staphylococcus aureus. Infect Immun. 2011b; 79:5010-5018. [PubMed: 21947772]
Proctor RA, Kahl B, von Eiff C, Vaudaux P, Lew DP, Peters G. Staphylococcal small colony variants have novel mechanisms for antibiotic resistance. Clin Infect Dis. 1998; 27:S68-74. ID: unige: 7527. [PubMed: 9710673]
Reynolds A, Rubin J, Clermont G, Day J, Vodovotz Y, Ermentrout GB. A reduced mathematical model of the acute inflammatory response: I. Derivation of model and analysis of anti-inflammation. J Theor Biol. 2006; 242:220-236. [PubMed: 16584750]
Shirtliff ME, Calhoun JH, Mader JT. Comparative evaluation of oral levofloxacin and parenteral nafcillin in the treatment of experimental methicillin-susceptible staphylococcus aureus osteomyelitis in rabbits. J Antimicrob Chemother. 2001; 48:253-258. [PubMed: 11481297]
Shirtliff ME, Mader JT, Camper AK. Molecular interactions in biofilms. Chem Biol. 2002; 9:859-871. [PubMed: 12204685]
Shirtliff, ME.; O'May, G.; Leid, J. Protective vaccine against staphylococcus aureus biofilms comprising cell wall-associated immunogens. United States Patent. US 08318180. 2012.
Sinha P, Ghosh AK, Das T, Sa G, Ray PK. Protein a of staphylococcus aureus evokes th1 type response in mice. Immunol Lett. 1999; 67:157-165. [PubMed: 10369122]
Spector, WS. Cell Division Frequency: Microorganisms. Saunders; Saunders, Philadelphia: 1956. p. 96-97.
Stewart PS. Diffusion in biofilms. J Bacteriol. 2003; 185:1485-1491. [PubMed: 12591863]
Stewart PS, Costerton JW. Antibiotic resistance of bacteria in biofilms. Lancet. 2001; 358:135-138. [PubMed: 11463434]
Thien-Fah Maha C, O'Toole GA. Mechanisms of biofilm resistance to antimicrobial agents. Trends Microbiol. 2001; 9:34-39. [PubMed: 11166241]

<a id='609591d4-0614-4b82-ac64-fbec612e6083'></a>

_Math Med Biol_. Author manuscript; available in PMC 2015 September 09.

<a id='031c266d-b578-4bfe-b6f8-458fbf375351'></a>

Author Manuscript

<a id='22c344b4-ef8d-48a1-9241-feef6feab81b'></a>

Author Manuscript

<a id='010252e6-7dcf-4e81-a775-4e245d20194d'></a>

Author Manuscript

<a id='779d47a5-b610-48c3-9f73-4f6dce8405b5'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='f22de8cd-9bff-4afb-aac0-d9c5a3bce060'></a>

Jarrett et al.

<a id='4d7eecf0-82b3-4361-8ea1-2fbdb159b303'></a>

Page 18

<a id='20aa4120-8406-4a71-8d26-86829afd455c'></a>

Vettermann C, Castor D, Mekker A, Gerrits B, Karas M, Jack HM. Proteome profiling suggests a pro-
inflammatory role for plasma cells through release of high-mobility group box 1 protein.
Proteomics. 2011; 11:1228–1237. [PubMed: 21319304]

<a id='8133ecc9-549a-4366-bd7b-74a36c910942'></a>

Wigginton JE, Kirschner D. A model to predict cell-mediated immune regulatory mechanisms during human infection with mycobacterium tuberculosis. J Immunol. 2001; 166:1951-1967. [PubMed: 11160244]

<a id='b3af39e9-e7d7-469b-95bb-10d1f745ec76'></a>

**Appendix**

<a id='3c86203a-3730-47be-81db-68059adbe5a8'></a>

Table A1
Comparison of mouse strains: their dominant responses, antibodies involved for testing and
list of experiments.

<a id='3792ed75-dde6-437a-9d1b-550e09222de0'></a>

<table id="17-1">
<tr><td id="17-2">Mouse strain</td><td id="17-3">Basic description</td><td id="17-4">Biological elements</td><td id="17-5">Experiments</td></tr>
<tr><td id="17-6">BALB/c</td><td id="17-7">Anti-inflammatory response dominates</td><td id="17-8">Th2, Treg dominate (Treg treated with: anti-CD25 antibodies)</td><td id="17-9">1,4</td></tr>
<tr><td id="17-a">C57BL/6</td><td id="17-b">Pro-inflammatory response dominates</td><td id="17-c">Th17, Th1 dominate (treated with: anit-IL-6, anti-IL-12p40 antibodies)</td><td id="17-d">2,5-8</td></tr>
<tr><td id="17-e">STAT6 KO BALB/c</td><td id="17-f">BALB/c mice with Th2 response removed</td><td id="17-g">Treg dominates</td><td id="17-h">3</td></tr>
</table>
Note: the Th2 response has both pro- and anti-inflammatory characteristics

<a id='aba2adee-672d-4756-8c81-f0c62d7add33'></a>

Table A2
Parameters used in the model for the BALB/c mouse. All parameters have units h⁻¹ except for the following: β₁, β₂, β₃, β₄ and α₄ have units of (amount * h)⁻¹; K_B has units of relative amount. Estimated parameters have relatively low PRCC values, indicating that variations do not significantly alter results.

<a id='f03cb3ab-c30f-43d8-b676-172b34071d4d'></a>

<table id="17-i">
<tr><td id="17-j">Parameters</td><td id="17-k">Values used</td><td id="17-l">Description</td><td id="17-m">Ref.</td></tr>
<tr><td id="17-n">a</td><td id="17-o">0.27a</td><td id="17-p">Response or recruitment rate of pro-inflammatory cells and signalling (P) to inflammatory signalling (I)</td><td id="17-q">Estimated</td></tr>
<tr><td id="17-r">P</td><td id="17-s">0.2</td><td id="17-t">Response rate of the pro-inflammatory response (P) to the infection itself (B)</td><td id="17-u">Estimated (Reynolds et al., 2006)</td></tr>
<tr><td id="17-v">B</td><td id="17-w">0.014</td><td id="17-x">Rate the anti-inflammatory cells and signalling (A) reduce/inhibit the response of the pro-inflammatory response (P)</td><td id="17-y">Estimated</td></tr>
<tr><td id="17-z">μι</td><td id="17-A">0.12</td><td id="17-B">Natural decay rate of the pro-inflammatory response (P)</td><td id="17-C">Coxon et al. (1999)</td></tr>
<tr><td id="17-D">α₂</td><td id="17-E">0.11ᵃ</td><td id="17-F">Response or recruitment rate of the anti-inflammatory response (A) to pro-inflammatory signalling (P)</td><td id="17-G">Estimated</td></tr>
<tr><td id="17-H">β₂</td><td id="17-I">0.1</td><td id="17-J">Rate at which inflammation (I) inhibits the anti-inflammatory response (A)</td><td id="17-K">Moura &amp; Tjwa (2010)</td></tr>
<tr><td id="17-L">μ₂</td><td id="17-M">0.25</td><td id="17-N">Natural decay rate of the anti-inflammatory response (A)</td><td id="17-O">Huhn et al. (1997) and Coxon et al. (1999)</td></tr>
<tr><td id="17-P">α₃</td><td id="17-Q">1.05ᵃ</td><td id="17-R">Rate of inflammation/damage (I) produced by the pro-inflammatory response (P)</td><td id="17-S">Estimated</td></tr>
<tr><td id="17-T">ρ₂</td><td id="17-U">0.45</td><td id="17-V">Rate of inflammation/damage (I) produced by the infection (B)</td><td id="17-W">Estimated</td></tr>
<tr><td id="17-X">β₃</td><td id="17-Y">2ª</td><td id="17-Z">Rate the anti-inflammatory response (A) removes inflammatory signalling and damage (I)</td><td id="17-10">Brandwood et al. (1992), Edelson et al. (1975) and Matsui et al. (1983)</td></tr>
<tr><td id="17-11">μ₃</td><td id="17-12">0.0174</td><td id="17-13">Natural decay rate of inflammation (I)</td><td id="17-14">Reynolds et al. (2006)</td></tr>
<tr><td id="17-15">g</td><td id="17-16">0.9</td><td id="17-17">Bacterial (B) growth rate</td><td id="17-18">Spector (1956)</td></tr>
</table>

<a id='3c699114-9a02-4b1b-85ed-c333cf014288'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='67819491-3730-415f-856b-d5313e1a5aa5'></a>

Author Manuscript

<a id='d2ccb5d6-bcea-49d9-832b-ebd5d49d8ea6'></a>

Author Manuscript

<a id='ee374850-16ed-4059-891b-59e67abd5734'></a>

Author Manuscript

<a id='9d60576a-286e-438d-88eb-58f45cfbdada'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='2da7854d-2f8d-4563-be1f-4aaaade328b6'></a>

Jarrett et al.

<a id='0744b637-b6ee-461d-ae3b-7cb9d37e0849'></a>

Page 19

<a id='946a0dff-9dca-4839-94eb-4b1d6b9ec80e'></a>

<table id="18-1">
<tr><td id="18-2">Parameters</td><td id="18-3">Values used</td><td id="18-4">Description</td><td id="18-5">Ref.</td></tr>
<tr><td id="18-6">K_B</td><td id="18-7">1</td><td id="18-8">Carrying capacity for infection (B)</td><td id="18-9">Assumed</td></tr>
<tr><td id="18-a">a_4</td><td id="18-b">1.5</td><td id="18-c">Rate the infection (B) benefits from inflammation and damage (I)</td><td id="18-d">Estimated</td></tr>
<tr><td id="18-e">β_4</td><td id="18-f">5^a</td><td id="18-g">Rate the pro-inflammatory response (P) kills or removes the bacteria (B)</td><td id="18-h">Brandwood et al. (1992), Edelson et al. (1975) and Matsui et al. (1983)</td></tr>
<tr><td id="18-i">γ</td><td id="18-j">0.01</td><td id="18-k">Decaying source of bacteria (B) from the implant</td><td id="18-l">Estimated</td></tr>
</table>
"Parameters changed for specific experiments. Changed values for each experiment are identified in the captions of their simulations
Table A3
Qualitative summary of the model results compared with experimental evidence (d = days)
<table id="18-m">
<tr><td id="18-n">Experiment description</td><td id="18-o">Model results</td><td id="18-p">Corresponding biological results</td></tr>
<tr><td id="18-q">1. BALB/c tibia implanted with S. aureus-coated pin</td><td id="18-r">Clearance of infection and return to basal/ healthy equilibrium</td><td id="18-s">After 21d, 41.67% of mice infected and after 49d, 25% infected—with decreasing CFU amounts; no biofilm formation; lack of neutrophil infiltration to bone (Prabhakara et al., 2011b)</td></tr>
<tr><td id="18-t">2. C57BL/6 tibia implanted with S. aureus-coated pin</td><td id="18-u">Infection persists and bacteria positive equilibrium is stable which has a higher inflammation/damage value</td><td id="18-v">At all time points 100% of mice infected; definite biofilm formation; large numbers of neutrophil infiltration to bone (Prabhakara et al., 2011b)</td></tr>
<tr><td id="18-w">3. STAT6 KO BALB/c tibia implanted with S. aureus-coated pin</td><td id="18-x">Infection persists and bacteria positive equilibrium is stable. However, it has a lower inflammation/damage value</td><td id="18-y">After 21d, 100% of mice were still infected but with CFU amounts comparable with BALB/c mice still infected at 21d (Prabhakara et al., 2011b)</td></tr>
<tr><td id="18-z">4. BALB/c tibia implanted with S. aureus-coated pin and treated with Treg antibodies</td><td id="18-A">Infection persists and bacteria positive equilibrium is stable</td><td id="18-B">After 21d, infected mice increased to 87.5% (Prabhakara et al., 2011b)</td></tr>
<tr><td id="18-C">5. C57BL/6 tibia implanted with S. aureus-coated pin and treated with Th17 antibodies</td><td id="18-D">Infection persists and bacteria positive equilibrium is stable but with a lower level of infection</td><td id="18-E">After 21d, infected mice decreased slightly to 85.7% (Prabhakara et al., 2011b)</td></tr>
<tr><td id="18-F">6. C57BL/6 tibia implanted with S. aureus-coated pin and treated with Th17 and Th1 antibodies</td><td id="18-G">Small changes in the specific parameters for experiments 5 and 6 result in either persistence of infection or clearance</td><td id="18-H">After 21d, infected mice decreased slightly to 62.5% (Prabhakara et al., 2011b)</td></tr>
<tr><td id="18-I">7. C57BL/6 tibia implanted with S. aureus coated pin and treated with quadrivalent vaccine and antibiotics</td><td id="18-J">Infection persists and bacteria positive equilibrium is stable unless antibiotic treatment is incorporated which gives stability to the healthy/basal equilibrium</td><td id="18-K">After previous vaccination, 14 d after implantation of infection 50% of mice remained infected (Shirtliff et al., 2012) and in rabbits 66% remained infected (Brady et al., 2011), but combined with antibiotics there was a 99.9% reduction in bacterial population for rabbits (Shirtliff et al., 2012)</td></tr>
<tr><td id="18-L">8. C57BL/6 tibia implanted with S. aureus coated pin and treated with pentavalent vaccine</td><td id="18-M">Clearance of infection and return to basal/ healthy equilibrium</td><td id="18-N">After 21 d, there was 100% clearance in all mice (Shirtliff et al., 2012)</td></tr>
</table>

<a id='386fe7dd-d2d9-4e01-a500-1d0d78fbf59f'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='27dbc744-b4be-497f-ae6b-c207f0ab2b18'></a>

Author Manuscript

<a id='8fe54ff2-f316-4c14-b783-42c8ffe4eae9'></a>

Author Manuscript

<a id='3d587a1f-ecc5-4c6c-a787-7a24dc2ac8bf'></a>

Author Manuscript

<a id='36e63cad-f83b-469b-b85b-79f1e0a24408'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='453e9102-3617-41e5-8b37-a4ae2462461a'></a>

Jarrett et al.

<a id='5df07900-d37c-498c-8a1a-00cc6aacbbcc'></a>

Page 20

<a id='d8e10871-8d4d-4c20-b19b-76aa9905ae44'></a>

**Table A4**
PRCC values calculated for the model. Note that positive/negative values indicate a positive/negative feedback

<a id='e979e629-5277-46a2-981a-09a15f1a59c9'></a>

<table id="19-1">
<tr><td id="19-2">Parameters</td><td id="19-3">Pro-inflammatory PRCC Value</td><td id="19-4">Anti-inflammatory PRCC Value</td><td id="19-5">Inflammation PRCC Value</td><td id="19-6">Bacteria PRCC Value</td></tr>
<tr><td id="19-7">a_{1}</td><td id="19-8">0.1318</td><td id="19-9">-0.0017</td><td id="19-a">0.0109</td><td id="19-b">-0.0140</td></tr>
<tr><td id="19-c">P</td><td id="19-d">-0.0439</td><td id="19-e">0.0505</td><td id="19-f">-0.0582</td><td id="19-g">-0.0717</td></tr>
<tr><td id="19-h">A</td><td id="19-i">0.0300</td><td id="19-j">0.0657</td><td id="19-k">0.0894</td><td id="19-l">-0.0243</td></tr>
<tr><td id="19-m">\mu_{1}</td><td id="19-n">-0.0682</td><td id="19-o">0.0877</td><td id="19-p">-0.0341</td><td id="19-q">0.1094</td></tr>
<tr><td id="19-r">a_{2}</td><td id="19-s">-0.3514</td><td id="19-t">0.1963</td><td id="19-u">-0.2471</td><td id="19-v">-0.1969</td></tr>
<tr><td id="19-w">β</td><td id="19-x">0.2675</td><td id="19-y">-0.1210</td><td id="19-z">0.2054</td><td id="19-A">0.1324</td></tr>
<tr><td id="19-B">\mu_{2}</td><td id="19-C">0.1890</td><td id="19-D">-0.2260</td><td id="19-E">0.0454</td><td id="19-F">0.0471</td></tr>
<tr><td id="19-G">аз</td><td id="19-H">0.4239</td><td id="19-I">0.0649</td><td id="19-J">0.3063</td><td id="19-K">0.1606</td></tr>
<tr><td id="19-L">2</td><td id="19-M">0.0698</td><td id="19-N">0.0339</td><td id="19-O">0.0851</td><td id="19-P">0.0264</td></tr>
<tr><td id="19-Q">β3</td><td id="19-R">-0.1345</td><td id="19-S">0.1110</td><td id="19-T">0.1185</td><td id="19-U">0.0080</td></tr>
<tr><td id="19-V">μ3</td><td id="19-W">-0.1027</td><td id="19-X">-0.0409</td><td id="19-Y">-0.2082</td><td id="19-Z">-0.1059</td></tr>
<tr><td id="19-10">g</td><td id="19-11">0.0857</td><td id="19-12">0.0031</td><td id="19-13">0.0334</td><td id="19-14">0.0028</td></tr>
<tr><td id="19-15">KB</td><td id="19-16">0.1644</td><td id="19-17">-0.1110</td><td id="19-18">0.1031</td><td id="19-19">0.1689</td></tr>
<tr><td id="19-1a">a4</td><td id="19-1b">0.2793</td><td id="19-1c">0.0335</td><td id="19-1d">0.0453</td><td id="19-1e">0.2204</td></tr>
<tr><td id="19-1f">B4</td><td id="19-1g">-0.1632</td><td id="19-1h">0.0294</td><td id="19-1i">-0.0269</td><td id="19-1j">-0.1046</td></tr>
<tr><td id="19-1k">Y</td><td id="19-1l">0.0576</td><td id="19-1m">0.0517</td><td id="19-1n">0.0357</td><td id="19-1o">0.0065</td></tr>
<tr><td id="19-1p">P_{i}</td><td id="19-1q">0.0320</td><td id="19-1r">0.0857</td><td id="19-1s">0.0109</td><td id="19-1t">0.0291</td></tr>
<tr><td id="19-1u">A_{i}</td><td id="19-1v">-0.0770</td><td id="19-1w">-0.0970</td><td id="19-1x">-0.0420</td><td id="19-1y">-0.1230</td></tr>
<tr><td id="19-1z">I_{i}</td><td id="19-1A">-0.0360</td><td id="19-1B">-0.0770</td><td id="19-1C">-0.0960</td><td id="19-1D">-0.1000</td></tr>
<tr><td id="19-1E">B_i</td><td id="19-1F">0.0682</td><td id="19-1G">0.0439</td><td id="19-1H">0.0818</td><td id="19-1I">0.1164</td></tr>
</table>

<a id='6ec2ca61-12b2-4faf-8e75-18f4cf08bab6'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='a26299e2-c1cd-4b32-a162-b7884ddf4b2d'></a>

Author Manuscript

<a id='869a7052-37f2-47e2-992e-5381e11790d0'></a>

Author Manuscript

<a id='d9445e61-5936-461f-8e91-5b47ecece4ec'></a>

Author Manuscript

<a id='90f83d51-edc5-466b-a765-26b3c59e67f6'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='27bb6fe9-92bb-4353-b8c6-f49b563f304f'></a>

Jarrett et al.

<a id='30f6e15a-dc43-44e0-931a-66df908b8fc3'></a>

Page 21

<a id='cb38886a-077f-49ec-91e3-235ac5ce51aa'></a>

<::Diagram showing a network of interactions between four entities: 'Pro-inflammatory Response', 'Anti-inflammatory Response', 'Bacteria', and 'Inflammation'. Each entity is represented by a rounded rectangular box. Arrows indicate relationships, with some arrows having a blunt end indicating inhibition, and others pointed, indicating activation or influence. The labels on the arrows are Greek letters.

**Nodes and their connections:**
*   **Pro-inflammatory Response** (light gray box, top center):
    *   Activates Anti-inflammatory Response (arrow labeled α₂).
    *   Is inhibited by Anti-inflammatory Response (blunt-ended arrow labeled β₁).
    *   Activates Bacteria (arrow labeled β₄).
    *   Is inhibited by Bacteria (blunt-ended arrow labeled ρ₁).
    *   Activates Inflammation (arrow labeled α₁).
    *   Is activated by Inflammation (arrow labeled α₃).
*   **Anti-inflammatory Response** (dark gray box, left):
    *   Inhibits Pro-inflammatory Response (blunt-ended arrow labeled β₁).
    *   Is activated by Pro-inflammatory Response (arrow labeled α₂).
    *   Activates Inflammation (arrow labeled β₃).
    *   Is inhibited by Inflammation (blunt-ended arrow labeled β₂).
*   **Bacteria** (light gray box, right):
    *   Inhibits Pro-inflammatory Response (blunt-ended arrow labeled ρ₁).
    *   Is activated by Pro-inflammatory Response (arrow labeled β₄).
    *   Activates Inflammation (arrow labeled α₄).
    *   Is inhibited by Inflammation (blunt-ended arrow labeled ρ₂).
*   **Inflammation** (dark gray box, bottom center):
    *   Inhibits Anti-inflammatory Response (blunt-ended arrow labeled β₂).
    *   Is activated by Anti-inflammatory Response (arrow labeled β₃).
    *   Activates Pro-inflammatory Response (arrow labeled α₃).
    *   Is activated by Pro-inflammatory Response (arrow labeled α₁).
    *   Inhibits Bacteria (blunt-ended arrow labeled ρ₂).
    *   Is activated by Bacteria (arrow labeled α₄).
: diagram::>

<a id='302a9dd0-e3e4-4593-b17c-0ea64bf81077'></a>

Fig. 1.
Model diagram for component interactions. Arrow-ended lines represent the up-regulation or promotion of one component by another. Flat-ended lines represent down-regulation or blockage of one component by the corresponding component. The general interactions outlined by this figure are described by the following parameters: α₁ is the response or recruitment rate of pro-inflammatory cells and signalling to inflammatory signalling; ρ₁ is the response rate of the pro-inflammatory response to the infection itself; β₁ is the rate the anti-inflammatory cells and signalling reduce/inhibit the response of the pro-inflammatory response; α₂ is the response or recruitment rate of the anti-inflammatory response to pro-inflammatory signalling; β₂ is the rate at which inflammation inhibits the anti-inflammatory response; α₃ is the rate of inflammation/damage produced by the pro-inflammatory response; ρ₂ is the rate of inflammation/damage produced by the infection; β₃ is the rate at which the anti-inflammatory response removes inflammatory signalling and damage; α₄ is the rate at which the infection benefits from inflammation and damage and β₄ is the rate at which the pro-inflammatory response kills or removes the bacteria. These descriptions as well as other parameters are listed in Table A2.

<a id='da349221-e818-4f05-aefa-692e8d0f3b04'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='ea14b316-4172-455c-9d4a-81957397265d'></a>

Author Manuscript

<a id='7db391f8-664d-42e9-a08f-ed10d7133707'></a>

Author Manuscript

<a id='e8377d55-a263-4e1a-b1c3-39dcce7756a5'></a>

Author Manuscript

<a id='cf95f657-1b8f-4a3f-86f7-2e065fa5dd5e'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='e7e5fca2-e3c6-4fa9-a503-ea84ab37e443'></a>

Jarrett et al.

<a id='0d1b5b96-8cf8-43dc-a3b8-eb66b0bfb33d'></a>

Page 22

<a id='905d5bf5-5d8b-473b-bc7a-abf7cad126e6'></a>

<::chart: The figure displays three line graphs, arranged in a 2x1 layout (two at the top, one at the bottom), all showing "Component Value" on the y-axis (ranging from 0 to 3) versus "Hours" on the x-axis (ranging from 0 to 35). Each graph contains three lines representing different immune responses: a solid line for "Pro-inflammatory", a dashed line for "Anti-inflammatory", and a dotted/dash-dotted line for "Inflammation". A legend is present in the top right of each subplot.  Top left plot: Shows initial high inflammation (dotted line starts high), and initial pro-inflammatory and anti-inflammatory responses (solid and dashed lines start around 1 and 0.5 respectively). The pro-inflammatory response stabilizes around 0.8, anti-inflammatory rises to around 2, and inflammation drops then rises to around 2.  Top right plot: Shows initial high pro-inflammatory and anti-inflammatory responses (solid and dashed lines start high) but low inflammation (dotted line starts low). The pro-inflammatory response stabilizes around 0.8, anti-inflammatory rises to around 2, and inflammation drops then rises to around 2.  Bottom plot: Shows initial high pro-inflammatory response and even higher anti-inflammatory response with low initial inflammation. The pro-inflammatory response stabilizes around 0.8, anti-inflammatory rises to around 2, and inflammation drops then rises to around 2. Fig. 2. Immune response to basal levels: the parameter set used for these particular simulations is the BALB/c mouse set listed in the parameter table. The basal level is $(P, \bar{A}, \bar{I}) \approx (0.82, 0.20, 2.10)$ with eigenvalues $\lambda \approx -0.17, -0.44, -0.95$. Top left: initial high inflammation, pro-inflammatory response and anti-inflammatory response, top right: initial high pro-inflammatory response and anti-inflammatory response, but low inflammation, bottom: initial high pro-inflammatory response and even higher anti-inflammatory response with low initial inflammation.::>

<a id='cb7520d1-627f-4bd8-a9a3-fb3ee475639b'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='91203f6a-9766-4ee3-acff-175b9b26fd01'></a>

Author Manuscript

<a id='ae38e93d-c405-43a6-88b6-85d9a0f1efc9'></a>

Author Manuscript

<a id='2de9f1eb-b172-4036-a8e0-5811dd9202f1'></a>

Author Manuscript

<a id='46c62a3b-3463-4b70-8087-7e3dd76cabf9'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='846c1747-4efc-4332-b8f3-fbb6058dc9b8'></a>

Jarrett et al.

<a id='ec5b6ea5-93be-4c52-854f-e1958be9e705'></a>

Page 23

<a id='955e19d0-3eba-4129-896c-17eeeb1c6305'></a>

<::The image contains three plots, labeled as Fig. 3. from the caption below them.The top-left plot is a line chart with 'Hours' on the x-axis (ranging from 0 to 250) and 'Component Value' on the y-axis (ranging from 0 to 3.5). It displays three lines: 'Pro-inflammatory' (solid line), 'Anti-inflammatory' (dashed line), and 'Inflammation' (dash-dot line). The 'Pro-inflammatory' line starts at approximately 0.8, peaks around 1.1 at 10 hours, then gradually decreases to about 0.9. The 'Anti-inflammatory' line starts near 0.1, rises to about 0.4 at 10 hours, then slowly decreases to approximately 0.2. The 'Inflammation' line starts near 3.5, sharply drops to about 1.5 at 10 hours, then slowly increases to around 2.1.The top-right plot is a line chart with 'Hours' on the x-axis (ranging from 0 to 250) and 'Infection' on the y-axis (ranging from 0 to 1.6). It displays one line labeled 'Bacteria'. This line starts near 0.2, sharply peaks at approximately 1.5 at around 5 hours, then rapidly decreases to about 0.5 at 25 hours, continuing to decline.The bottom plot is a scatter plot with error bars, titled 'S. Aureus implanted BALB/c CFUs over time'. The x-axis is 'Hours' (ranging from 0 to 500), and the y-axis is 'CFUs' (ranging from 0 to 9 x 10^7). It shows two data series: 'Model' (dashed line) and 'Average Experimental data' (black circular markers with error bars). The 'Model' line starts at approximately 3 x 10^7, decreases to about 1.5 x 10^7 at 200 hours, and continues to decrease towards 0. The 'Average Experimental data' points are: approximately 4.5 x 10^7 at 50 hours, 1.5 x 10^7 at 175 hours, and 0.5 x 10^7 at 350 hours. Error bars are present for the experimental data points.::>Fig. 3. 

<a id='01c12d6d-b37c-40a1-8277-60b51bf7d3f9'></a>

Experiment 1: BALB/c response results in the clearance of infection. We consider this our basis experiment to compare other experimental responses. The stable equilibrium (basal level) is (P, Ā, Ī, B) ≈ (0.82, 0.20, 2.10, 0) with eigenvalues λ ≈ −0.06, −0.17, -0.44, -0.95. **Top left**: immune system components, **top right**: bacterial component, **bottom**: we present this dimensional simulation of the model output to compare with the experimental data for this particular experiment. We scaled the model output based on the observed Colony Forming Units (CFUs) of bacteria.

<a id='f72c5a9e-7eb8-4e0e-89be-38cfaff5d60d'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='27173dee-886f-4381-814a-bbca56f54cda'></a>

Author Manuscript

<a id='363a4f96-d304-4c7d-b911-a56b65e9c6f6'></a>

Author Manuscript

<a id='986c5c4b-4902-4163-a5a8-8d9d23805c37'></a>

Author Manuscript

<a id='01438f77-2b3f-4011-ab53-cd4df949728e'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='32fb5ca0-cacd-4954-81e9-455d8bf174b8'></a>

Jarrett et al.

<a id='b8ec4c0a-71d4-4b46-9c39-35a37e75fc40'></a>

Page 24

<a id='c527919c-71e4-43cf-9da5-4a4c11ec55dc'></a>

<::chart: Two plots side-by-side, sharing a common x-axis label 'Hours'. The x-axis ranges from 0 to 250. Both plots show a transient phase followed by stabilization.

Left Panel: 'Immune system components'.
- Y-axis: 'Component Value', ranging from 0 to 4.
- Legend:
  - Pro-inflammatory (solid line): Starts high (around 3.8), quickly drops, then stabilizes at approximately 0.9.
  - Anti-inflammatory (dashed line): Starts low (around 0.2), rises slightly, then stabilizes at approximately 0.25.
  - Inflammation (dash-dotted line): Starts high (around 3.8), drops to approximately 1.8, then slowly increases to approximately 2.6.

Right Panel: 'Bacterial component'.
- Y-axis: 'Infection', ranging from 0.4 to 2.4.
- Legend:
  - Bacteria (solid line): Starts very high (around 2.3), sharply drops to approximately 0.6, then slowly decreases further to approximately 0.55.

Fig. 4. Experiment 2: C57BL/6 response. We changed specific parameters compared with the BALB/c mice (β₁ = 0.007, α₂ = 0.09, β₄ = 4.75), resulting in chronic infection. The stable equilibrium is (P, Ā, Ī, B) ≈ (0.94, 0.22, 2.69, 0.54) with eigenvalues λ ≈ −0.07 + 0.33i, −1.04 + 0.33i, −1.04 −0.33i, −0.07 −0.33i. Left panel: immune system components, right panel: bacterial component.::>

<a id='e97bc1b1-7085-481c-9533-c4d94fb53a42'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='453c7fae-744a-46c7-8d79-51864d03d741'></a>

Author Manuscript

<a id='383dc620-ad25-49f8-a609-9034a1cd98fe'></a>

Author Manuscript

<a id='b74deb70-b277-47e2-bdcf-82787718161c'></a>

Author Manuscript

<a id='1a30cc51-38cb-48b1-b5c3-44a5949f448c'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='3a4f28ca-34b6-4e96-b3c5-d08295da0913'></a>

Jarrett et al.

<a id='ca4153f4-ce06-4485-9fea-ba7ec4e877e5'></a>

Page 25

<a id='ee066c25-aae0-455c-a31f-4296c0765e8e'></a>

<::chart: The figure consists of two line charts side-by-side, illustrating Experiment 3: STAT6 KO BALB/c response (β₁ = 0.005, β₄ = 3) where the Th2 response is removed, resulting in chronic infection. The stable equilibrium is (P, Ā, Ī, B) ≈ (0.91, 0.38, 1.56, 0.57) with eigenvalues λ ≈ -0.08 + 0.39i, -0.64, -1.33, -0.08 -0.39i. The x-axis for both charts is labeled "Hours", ranging from 0 to 250. The y-axis for both charts ranges from 0 to 4. Left panel: immune system components. This chart shows three lines. The y-axis is labeled "Component Value". The legend indicates: "Pro-inflammatory" (solid line), "Anti-inflammatory" (dashed line), and "Inflammation" (dash-dot line). The Pro-inflammatory component starts around 0.5, peaks at approximately 1.1 around 10 hours, and then stabilizes around 0.9. The Anti-inflammatory component starts near 0, peaks at approximately 1.1 around 10 hours, and then decreases to stabilize around 0.5. The Inflammation component starts near 0, rapidly increases to a peak near 4, then quickly drops to about 1, and gradually increases to approximately 1.5 at 250 hours. Right panel: bacterial component. This chart shows one line. The y-axis is labeled "Infection". The legend indicates: "Bacteria" (solid line). The Bacteria component starts near 0, rapidly increases to a peak near 4, then quickly drops to about 0.7, and gradually decreases to approximately 0.55 at 250 hours.::>

<a id='ffb08e44-6788-4be9-a05d-24de648279c2'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='79c846c9-f2af-4405-8104-0c61daaa7c4f'></a>

Author Manuscript

<a id='aed16b6d-b6ef-4c3a-b2cd-f07e8aba299c'></a>

Author Manuscript

<a id='67d49ba3-3fe6-466b-afd3-dc2629446bab'></a>

Author Manuscript

<a id='055eb738-3379-412e-90e9-7724d3c5445d'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='e15b8e26-1cd1-4f98-986c-5f8c66032d97'></a>

Jarrett et al.

<a id='b2808c2d-a092-41aa-9062-02bf074c1c61'></a>

Page 26

<a id='2b61d40f-18e2-4ead-a68c-d378714a0110'></a>

Fig. 6.
<::chart: The figure displays two line charts side-by-side, depicting Experiment 4 where BALB/c mice were treated with Treg antibodies (β₁ = 0.005, β₃ = 1.5). Left panel: immune system components, right panel: bacterial component.

Left Panel - Immune System Components:
- X-axis: Hours, ranging from 0 to 250.
- Y-axis: Component Value, ranging from 0 to 4.5.
- Legend:
    - Pro-inflammatory (solid line)
    - Anti-inflammatory (dashed line)
    - Inflammation (dash-dot line)
- Data trends:
    - Pro-inflammatory component starts high, drops quickly to approximately 1.0, and then stabilizes.
    - Anti-inflammatory component starts near 0, increases to about 0.5, and then stabilizes.
    - Inflammation component starts high, drops, then gradually increases from approximately 2.0 to 3.0.

Right Panel - Bacterial Component:
- X-axis: Hours, ranging from 0 to 250.
- Y-axis: Infection, ranging from 0.8 to 2.6.
- Legend:
    - Bacteria (solid line)
- Data trend:
    - The Bacteria component starts at a high peak of approximately 2.4, sharply decreases to around 0.7, then slightly increases to about 0.8 before gradually stabilizing around 0.75.::>
Experiment 4: BALB/c treated with Treg antibodies (β₁ = 0.005, β₃ = 1.5). Again, the result is infection, indicating that the Treg component of the immune system partially protects BALB/c mice from infection. The stable equilibrium is (P, Ā, Ī, B) ≈ (0.96, 0.28, 3.03, 0.70) with eigenvalues λ ≈ -0.06 + 0.36i, -1.16 + 0.43i, -1.16 -0.43i, -0.06 -0.36i. 

<a id='6a6d45bb-b4ea-4071-8e39-5974d854705d'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='612aa67c-b9e5-4684-9a1c-e62f2eb2a867'></a>

Author Manuscript

<a id='793ab7df-c62a-4fa1-a83f-dd5b9333bda1'></a>

Author Manuscript

<a id='58ed0404-a9c0-4a8e-a62f-952c311591be'></a>

Author Manuscript

<a id='ffbc3695-674d-4735-af10-316a832f3165'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='557455bd-ca64-46fd-8663-18a9a2d81634'></a>

Jarrett et al.

<a id='e290d517-2bc4-4e01-a8e7-1a58d7d6e421'></a>

Page 27

<a id='7a410fb5-6abd-4cde-a9d8-0b9c027b616b'></a>

<::chart: Two line graphs are displayed side-by-side. The x-axis for both graphs is labeled "Hours" and ranges from 0 to 250. The y-axis for the left graph is labeled "Component Value" and ranges from 0 to 4. The y-axis for the right graph is labeled "Infection" and ranges from 0.2 to 2.0. Left Panel: Immune system components. Three lines are plotted: - Pro-inflammatory (solid line): Starts around 0.5, quickly rises to about 1.0, then gradually decreases to stabilize around 0.9. - Anti-inflammatory (dashed line): Starts near 0, quickly rises to about 0.35, then gradually decreases to stabilize around 0.25. - Inflammation (dash-dot line): Starts around 3.5, sharply drops to about 1.5, then gradually increases to stabilize around 2.1. Right Panel: Bacterial component. One line is plotted: - Bacteria (solid line): Starts near 0, sharply rises to a peak of about 1.9 around 10 hours, then rapidly decreases to about 0.55 around 50 hours, and slowly declines further to about 0.35 at 250 hours. Fig. 7. Experiment 5: C57BL/6 treated with Th17 antibodies ($\alpha_1 = 0.225$, $\beta_1 = 0.007$, $\alpha_2 = 0.09$, $\alpha_3$ = 0.875, $\beta_4 = 4.75$) results in reduced infection and damage, but does not clear the infection. The stable equilibrium is ($\bar{P}$, $\bar{A}$, $\bar{I}$, $\bar{B}$) $\approx$ (0.84, 0.18, 2.17, 0.18) with eigenvalues $\lambda \approx -0.09 +$ 0.18i, -0.62, -0.80, -0.09 -0.18i. Left panel: immune system components, right panel: bacterial component.::>

<a id='48763bed-3a28-49b4-abda-b76d477ac3b5'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='4718a07b-91f2-4ae6-81fe-750effb978bb'></a>

Author Manuscript

<a id='38a1cadb-ef3e-49d5-9054-1da08b76948e'></a>

Author Manuscript

<a id='8b603012-d20e-4538-9ee3-53f086ffc023'></a>

Author Manuscript

<a id='1f8b3bc5-b885-47f0-9ee9-1421cc80a3a7'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='fc10b4c3-6193-4129-b81c-8264deceba9f'></a>

Jarrett et al.

<a id='03652669-a350-47a2-aa32-0f0943d0d3c0'></a>

Page 28

<a id='aa593e97-bc95-4a21-9c51-4b3e4177134e'></a>

<:: Two line graphs displayed side-by-side. The left graph, titled 'immune system components', shows 'Component Value' on the y-axis (ranging from 0 to 3.5) and 'Hours' on the x-axis (ranging from 0 to 250). It contains three lines: a solid line representing 'Pro-inflammatory' which peaks around 1.1 and then stabilizes around 0.8; a dashed line representing 'Anti-inflammatory' which peaks around 0.35 and then stabilizes around 0.3; and a dash-dot line representing 'Inflammation' which peaks around 3.2 and then stabilizes around 1.4. The right graph, titled 'bacterial component', shows 'Infection' on the y-axis (ranging from 0 to 1.6) and 'Hours' on the x-axis (ranging from 0 to 250). It contains one solid line representing 'Bacteria' which starts around 1.5, peaks slightly higher, then sharply decreases to around 0.5 within the first 25 hours, and continues to gradually decrease towards 0.2 by 250 hours. Fig. 8. Experiment 6: C57BL/6 treated with Th17 and Th1 antibodies with clearance of infection (α₁ = 0.18, β₁ = 0.007, α₂ = 0.09, α₃ = 0.7, β₄ = 4.75). Here the treatment allows the mice to overcome the infection with the combined reduction of the two inflammatory responses. The stable equilibrium is (P, Ā, Ī, B) ≈ (0.68, 0.16, 1.46, 0) with eigenvalues λ ≈ -0.16, -0.19 + 0.08i, -0.72, -0.19 -0.08i. The healthy state (basal level) is lower than the healthy state of the BALB/c mice here due to the immunomodulation. Left panel: immune system components, right panel: bacterial component. :chart::>

<a id='8e4d8325-88b9-4e7e-8c3e-f875b513a8e9'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='d50faef7-4035-4345-bd84-8a8104722ffb'></a>

Author Manuscript

<a id='ef28a0b4-f208-4ada-9319-a50c6c39d8a4'></a>

Author Manuscript

<a id='c3563c13-1f27-45b7-b059-2a2e665084d9'></a>

Author Manuscript

<a id='5856dc06-4f05-4611-bc47-97bb5ed071d8'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='2b13dfd4-fa5f-4ba8-b4ca-bfff61626dbc'></a>

Jarrett et al.

<a id='f98af594-ed57-4b78-b33d-dd357f956442'></a>

Page 29

<a id='a115ddc5-be4f-49eb-8e43-2e6ab1624bea'></a>

<::chart: The figure displays two line charts side-by-side, representing Experiment 7. The x-axis for both charts is labeled "Hours", ranging from 0 to 250. Fig. 9. Experiment 7: C57BL/6 treated with four-component vaccine resulting in no clearance ($a_1 = 0.36, \beta_1 = 0.007, a_2 = 0.09, \beta_4 = 6$). The four-component vaccine is unable to prime the immune system to remove the infection entirely. The stable equilibrium is $(P, \bar{A}, \bar{I}, B) \approx (0.91, 0.15, 3.08, 0.07)$ with eigenvalues $\lambda \approx -0.07 + 0.07i, -0.78, -1.25, -0.07 -0.07i$. Left panel: immune system components, right panel: bacterial component. Left panel: This line chart shows "Component Value" on the y-axis, ranging from 0 to 4. It contains three lines: a solid line representing "Pro-inflammatory" which quickly rises to approximately 0.9 and then stabilizes; a dashed line representing "Anti-inflammatory" which quickly rises to approximately 0.25 and then stabilizes; and a dash-dot line representing "Inflammation" which peaks around 3.5, drops, and then slowly increases from approximately 2.5 to 3.0. Right panel: This line chart shows "Infection" on the y-axis, ranging from 0.2 to 1.6. It contains one solid line representing "Bacteria" which peaks at approximately 1.4, then rapidly decreases to about 0.55, and continues to slowly decrease towards 0.25 over 250 hours.::>

<a id='4be9fdd7-2a94-4e2d-948d-914412bcadba'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='286ecb36-bed0-403a-a35b-9acf1b93075b'></a>

Author Manuscript

<a id='f0105fa6-5bb3-4fc6-8d56-942ae9d52117'></a>

Author Manuscript

<a id='5af8f511-be10-4413-abf8-ecd6afef7fcf'></a>

Author Manuscript

<a id='1e7580e8-b7dc-41c4-8762-c1d48e3f88e1'></a>

Author Manuscript

<!-- PAGE BREAK -->

<a id='401842d3-48d3-4cc7-9a2d-f152e98aac89'></a>

Jarrett et al.

<a id='931ccb33-f3ef-4068-b57c-e98d67a63639'></a>

Page 30

<a id='c0269669-6568-481c-a86d-97aba5852b2a'></a>

<::chart: Two-panel plot showing immune system components and bacterial infection over 250 hours. Left panel: Immune system components. The y-axis is 'Component Value' ranging from 0 to 3.5. The x-axis is 'Hours' from 0 to 250. Three lines are plotted: 'Pro-inflammatory' (solid line) stabilizes around 0.9, 'Anti-inflammatory' (dashed line) stabilizes around 0.15, and 'Inflammation' (dash-dot line) spikes to about 3.3 and then stabilizes around 3.0. Right panel: Bacterial component. The y-axis is 'Infection' ranging from 0 to 1.4. The x-axis is 'Hours' from 0 to 250. A single solid line labeled 'Bacteria' shows the infection level, starting at about 1.4, peaking slightly, and then steadily decreasing to near 0.1 by 250 hours. Fig. 10. Experiment 8: C57BL/6 treated with a five-component vaccine ($\alpha_1 = 0.36, \beta_1 = 0.007, \alpha_2 = 0.09, \beta_4 = 7$). Here the C57BL/6 mice clear the infection. The stable equilibrium is ($P, \bar{A}, \bar{I}, \bar{B}) \approx (0.90, 0.15, 3.06, 0)$ with eigenvalues $\lambda \approx -0.82, -0.11, -0.68, -1.30$. Left panel: immune system components, right panel: bacterial component.::>

<a id='3515d57d-30c0-4c62-9a06-cb1fd71f0407'></a>

Math Med Biol. Author manuscript; available in PMC 2015 September 09.

<a id='134b2898-f35a-471b-ab30-149c556ded03'></a>

Author Manuscript

<a id='cba12de9-9880-422a-b4f8-3994ec1048d4'></a>

Author Manuscript

<a id='3514c3cc-d3b7-4951-949e-34274027e471'></a>

Author Manuscript

<a id='b6720d78-77af-453c-a3fb-557fe5f0e461'></a>

Author Manuscript
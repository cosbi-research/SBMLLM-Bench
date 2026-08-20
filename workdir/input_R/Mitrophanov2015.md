<a id='e54fe237-7ad9-4de4-86a5-0facc326f90b'></a>

Mechanistic Modeling of the Effects of Acidosis on Thrombin Generation

<a id='cc99a5f2-4d9a-4002-a5d2-c5107cdd0130'></a>

Alexander Y. Mitrophanov, PhD,*† Frits R. Rosendaal, MD, PhD,‡§ and Jaques Reifman, PhD*†

<a id='ad824598-2f30-4b30-bbfc-2300e8042230'></a>

**BACKGROUND:** Acidosis, a frequent complication of trauma and complex surgery, results from tissue hypoperfusion and IV resuscitation with acidic fluids. While acidosis is known to inhibit the function of distinct enzymatic reactions, its cumulative effect on the blood coagulation system is not fully understood. Here, we use computational modeling to test the hypothesis that acidosis delays and reduces the amount of thrombin generation in human blood plasma. Moreover, we investigate the sensitivity of different thrombin generation parameters to acidosis, both at the individual and population level.

<a id='845faf7c-45e9-4a1a-9c5c-2ccc333e5302'></a>

**METHODS:** We used a kinetic model to simulate and analyze the generation of thrombin and thrombin-antithrombin complexes (TAT), which were the end points of this study. Large groups of temporal thrombin and TAT trajectories were simulated and used to calculate quantitative parameters, such as clotting time (CT), thrombin peak time, maximum slope of the thrombin curve, thrombin peak height, area under the thrombin trajectory (AUC), and prothrombin time. The resulting samples of parameter values at different pH levels were compared to assess the acidosis-induced effects. To investigate intersubject variability, we parameterized the computational model using the data on clotting factor composition for 472 subjects from the Leiden Thrombophilia Study. To compare acidosis-induced relative parameter changes in individual ("virtual") subjects, we estimated the probabilities of relative change patterns by counting the pattern occurrences in our virtual subjects. Distribution overlaps for thrombin generation parameters at distinct pH levels were quantified using the Bhattacharyya coefficient.

<a id='b9a7e6a5-bccd-4149-934a-3c1f98239f9e'></a>

**RESULTS:** Acidosis in the range of pH 6.9 to 7.3 progressively increased CT, thrombin peak time, AUC, and prothrombin time, while decreasing maximum slope of the thrombin curve and thrombin peak height (P < 10-5). Acidosis delayed the onset and decreased the amount of TAT generation (P < 10-5). As a measure of intrasubject variability, maximum slope of the thrombin curve and CT displayed the largest and second-largest acidosis-induced relative changes, and AUC displayed the smallest relative changes among all thrombin generation parameters in our virtual subject group (1-sided 95% lower confidence limit on the fraction of subjects displaying the patterns, 0.99). As a measure of intersubject variability, the overlaps between the maximum slope of the thrombin curve distributions at acidotic pH levels with the maximum slope of the thrombin curve distribution at physiological pH level systematically exceeded analogous distribution overlaps for CT, thrombin peak time, and prothrombin time.

<a id='0c8a8405-a89c-4692-9074-505001eff6a7'></a>

**CONCLUSIONS:** Acidosis affected all quantitative parameters of thrombin and TAT generation. While maximum slope of the thrombin curve showed the highest sensitivity to acidosis at the individual-subject level, it may be outperformed by CT, thrombin peak time, and prothrombin time as an indicator of acidosis at the subject-group level. (Anesth Analg 2015;121:278–88)

<a id='b2407b4e-23db-4031-89a1-9f8a3b6574e3'></a>

From the *DoD Biotechnology High Performance Computing Software Applications Institute (BHSAI); †Telemedicine and Advanced Technology Research Center; U.S. Army Medical Research and Materiel Command, Ft. Detrick, MD; and Departments of ‡Clinical Epidemiology and §Thrombosis and Haemostasis, Leiden University Medical Center, Leiden, The Netherlands.

<a id='662e692c-5287-4856-8b91-54f89eb7b4cd'></a>

Accepted for publication December 1, 2014.
Funding: AYM and JR were supported by the Network Science Initiative of
the U.S. Army, U.S. Army Medical Research and Materiel Command, Ft. De-
trick, MD. The Leiden Thrombophilia Study, completed previously (FRR),
was funded by the Netherlands Heart Foundation (89-063).

<a id='9c8a7849-faff-41d5-951b-d1d2bd166cff'></a>

The authors declare no conflicts of interest.

<a id='db8ff205-9762-46dc-a2bd-d19bb89d58ca'></a>

Supplemental digital content is available for this article. Direct URL citations
appear in the printed text and are provided in the HTML and PDF versions of
this article on the journal's website (www.anesthesia-analgesia.org).

<a id='3bd21f76-7c22-41af-ba80-abe8f86fe482'></a>

The opinions and assertions contained herein are the private views of the
authors and are not to be construed as official or as reflecting the views of
the U.S. Army or of the U.S. Department of Defense. This paper has been
approved for public release with unlimited distribution.

<a id='7e6d9c6f-5652-4df1-bc9d-12e343a63749'></a>

Reprints will not be available from the authors.

<a id='0576cb02-3373-4573-b4c6-d429c6e1d919'></a>

Address correspondence to Jaques Reifman, PhD, DoD Biotechnology High Performance Computing Software Applications Institute (BHSAI), Telemedicine and Advanced Technology Research Center, U.S. Army Medical Research and Materiel Command, ATTN: MCMR-TT, 504 Scott St., Ft. Detrick, MD 21702. Address e-mail to jaques.reifman.civ@mail.mil.

<a id='01257ece-fc71-427e-a098-f4f86e57de67'></a>

Copyright  2015 International Anesthesia Research Society
DOI: 10.1213/ANE.0000000000000733

<a id='5367b548-a98e-41fe-9623-ecf874c956ac'></a>

Acidosis (arterial pH ≤ 7.35) is a major contributor to trauma-associated coagulopathy.9⁻3 Acidosis arises when trauma is accompanied by severe hemorrhage and shock, and the resulting hypoperfusion leads to the accumulation of lactic acid.34 Moreover, the infusion of resuscitation fluids, such as normal saline, can exacerbate acidosis.2 Similar factors can trigger acidosis in patients undergoing complex surgery.5

<a id='70434375-5fb5-41fd-90b8-dfde34b7e0d6'></a>

The molecular mechanisms by which acidosis affects thrombin formation and activity have not been definitively elucidated. Blood coagulation is a complex phenomenon comprising cell-dependent thrombin generation, fibrin formation, and fibrinolysis. While each of these stages could potentially be impaired by acidosis, its effects on the biochemistry of thrombin generation are of particular interest because of the central role of thrombin in thrombus formation.6,7 Several studies using different experimental methodologies showed that thrombus formation is considerably impaired in acidosis,8,9 and this effect can even exceed that observed from hypothermia.10 However, other reports suggest that acidosis without hypothermia has a very limited impact on blood coagulation.11,12 Direct

<a id='a2891dfa-8ef7-4d19-96ba-ba8f9afab2aa'></a>

278

<a id='32413d39-c0cb-4951-bfe6-42e7d0e83192'></a>

www.anesthesia-analgesia.org

<a id='7d4cf8bf-8f79-4613-b69f-ca417d0d9f04'></a>

August 2015 • Volume 121 • Number 2

<!-- PAGE BREAK -->

<a id='ea2ac166-4a73-42fc-b89f-85873c180d15'></a>

experimental evidence demonstrates that key coagulation enzymes are inhibited by decreasing pH,13 but the effects of acidosis on thrombin generation kinetics in human blood plasma have not been investigated. Furthermore, it is not known how intersubject variability would influence acidosis-induced effects.

<a id='9259916c-00a3-4691-bbaa-01ad496f2b8f'></a>

Computational modeling can be used to integrate the available knowledge of individual biochemical reactions and make predictions about their cumulative effect on thrombin generation kinetics.6,14 Such approaches have been applied to analyze how thrombin generation is influenced by dilution15,16 and hypothermia,17 as well as by the action of therapeutic agents, such as recombinant factor VIIa15,18 and prothrombin complex concentrates.15 These results were obtained by applying, and extending the capabilities of, the Hockin-Mann kinetic model19,20 of thrombin generation. This model is a simplified representation of thrombin generation biochemistry in human plasma in vitro and can serve as a framework for simulating complex combinations of factors affecting blood clotting.6,14,18

<a id='3476f7f9-8194-438a-a787-b373a97f8985'></a>

In this study, we extend the Hockin-Mann model to rep-resent the effects of acidic pH on thrombin generation. We hypothesize that acidosis has the ability to affect the kinet-ics of free thrombin and thrombin-antithrombin complex (TAT) by both delaying their accumulation and reducing their maximum levels. Moreover, we hypothesize that these effects will be consistent throughout a large population of subjects. Finally, we compare the sensitivity to acidosis for different quantitative parameters of thrombin generation both at the single-subject level and at the subject-group level.

<a id='4b3aa3e8-7c90-4f58-9121-74dd29fdaaf7'></a>

## METHODS
### Study Group
This work is a computational modeling study; no actual blood samples were drawn or analyzed. This study was conducted in compliance with the document defining our organization's (BHSAI) Standard Operating Procedure for acquisition, warehousing, and sharing human data, which has been approved by the U.S. Army. Because this study only used previously obtained data, it was exempt from IRB review based on these procedures. Our computational analyses were performed for a virtual subject defined based on average values of coagulation protein concentrations in human plasma.18,20 Moreover, we analyzed virtual subjects defined using the clotting factor composition data for 472 individual subjects in the Leiden Thrombophilia Study (LETS)21 control group, as described below.

<a id='a443e18d-c879-4136-aeb8-9bbe35674fe7'></a>

Model Parameters, Inputs, Outputs, and the
Basic Simulation Protocol
The Hockin-Mann model of thrombin generation is a system of 34 ordinary differential equations reflecting the mass action kinetics of essential biochemical reactions in the thrombin generation network (i.e., in the system of biochemical reactions responsible for thrombin generation).19,20 Each equation represents one of the coagulation proteins or their complexes. The model's parameters are the initial concentrations of the coagulation proteins and 44 kinetic constants that determine the rates of the constituent biochemical reactions (the reactions are listed in Table S1 in the

<a id='2e0c07f8-b7d9-423f-afbf-5fd6d03a01e4'></a>

Supplemental Digital Content, http://links.lww.com/AA/ B118). The default initial concentrations are equal to the corresponding average values in human plasma, and the default values of the kinetic constants correspond to physi- ological pH level (i.e., pH 7.4). The main input of the model is the initial concentration of tissue factor, which is a biologi- cal trigger of thrombus formation. The model's outputs are temporal curves, called "kinetic trajectories," that reflect the time dependence of the concentrations of the coagulation proteins. The 2 main outputs considered in this work corre- spond to the concentration of thrombin (primary end point) and TAT complex (secondary end point).

<a id='faa7da66-7a0e-4198-92f8-7c1224d10809'></a>

To run the model and generate output trajectories for the chosen parameter values, we used a software function that computes the trajectories spanning a preselected time interval (in our case, 0-80 minutes). The model trajectories were subjected to further numerical analyses and/or plotted against time. All computations were performed in the software suite MATLAB R2012a (MathWorks, Natick, MA). Additional details pertaining to the computational procedures are provided in the Supplemental Digital Content (http://links.lww.com/AA/B118).

<a id='80e642aa-47fe-49e5-9523-4e898aa84f68'></a>

To model thrombin and TAT generation in the individual LETS subjects, we followed our previously described approach<sup>15-17</sup> and substituted the default values of the initial coagulation protein concentrations in the model with the corresponding values determined experimentally for each of the 472 individual subjects in the LETS control subject group. The resulting 472 variants of the Hockin-Mann model can be regarded, and are henceforth referred to, as virtual LETS subjects. After this adjustment to the initial concentrations, we generated and processed output trajectories as described above.

<a id='c351a1fb-5109-4749-ad78-18cd8da89f62'></a>

**Modeling the pH Dependence of Thrombin and TAT Generation**
To represent the pH dependence of thrombin and TAT generation, the basic simulation protocol (suitable only for pH 7.4) had to be modified. Because it is known that the rates of individual enzymatic reactions depend on pH,22-24 we represented the pH-dependent modulation of the thrombin/TAT generation kinetics by adjusting the catalytic rates of the enzymatic reactions in the Hockin-Mann model. Specifically, we used the expression k(pH) = f(pH)*k(7.4), where k(pH) is the catalytic rate constant of an enzymatic reaction at a given pH level, k(7.4) is the rate constant's value for physiological pH = 7.4, and f(pH) is a pH-dependent quantity that we refer to as "pH factor." We considered the following acidotic pH levels: 6.9, 7.0, 7.1, 7.2, and 7.3.

<a id='42c38e20-2dc8-439d-9002-ea0b8624f25f'></a>

We developed and compared 2 strategies, designated "full" and "reduced," for the pH-dependence simulations; these strategies were analogous to our recently developed approach to model the effects of hypothermia on thrombin generation. 17 The full strategy involved pH factor random sampling from a pH-dependent interval (shown in Fig. 1), which accounted for the uncertainty in the pH factor values. For a given acidotic pH value, this strategy produced a large number (by default, 5000) of random pH factor sets, each of which was used to adjust the kinetic constants in the model. After the adjustments, the model was run according to the

<a id='9ba3760b-b7ac-44fe-8068-c2a417f0a308'></a>

August 2015 • Volume 121 • Number 2

<a id='7be628e7-6d66-4c67-a554-f68aa41902c1'></a>

www.anesthesia-analgesia.org

<a id='f81c6f05-9f6a-4112-ae16-06b481d2bc92'></a>

279

<!-- PAGE BREAK -->

<a id='b70f5a55-8657-448b-bbb2-c88a76251e2e'></a>

Effects of Acidosis on Thrombin Generation

<a id='8f6810a0-41c9-4269-bf71-222e065b7163'></a>

basic simulation protocol (see previous subsection) to pro-duce a group of 5000 distinct trajectories for thrombin and TAT generation. These distinct trajectories were subjected

<a id='102d4122-22e0-406c-bfb8-20e71b51c848'></a>

<::transcription of the content: chart::>The chart displays "Relative enzyme activity" on the y-axis (ranging from 0 to 1) versus "pH" on the x-axis (ranging from 6.8 to 7.4). Two solid blue lines with square markers represent experimental data. The upper solid line depicts the enzymatic activity of the extrinsic tenase coagulation factor complex, while the lower solid line shows the enzymatic activity of the prothrombinase coagulation factor complex. Two dashed blue lines are present, forming an envelope around the solid lines, which represent a 100% increase in the distance from the solid lines. Black double-headed arrows indicate intervals at pH levels 6.9, 7.1, and 7.3. Figure 1. Relative enzyme activity as a function of pH. For every considered acidotic pH level, the pH factor values (which express enzymatic activity relative to that at pH 7.4) were sampled uniformly from the interval delimited by the dashed lines at that pH level. For the pH levels of 6.9, 7.1, and 7.3, such intervals are indicated by black arrows. The dashed lines were obtained by increasing (by 100%) the distance between the solid lines, which approximate the experimental data (extracted from Figs. 2 and 3 in Meng et al.13) shown with square markers. The markers on the upper and lower solid lines correspond to the enzymatic activity of the extrinsic tenase and prothrombinase coagulation factor complexes, respectively. The solid lines were fitted to the experimental data using the MATLAB function PCHIP. See Supplemental Digital Content for further details.<::>

<a id='3a96377c-f042-42f9-b5c4-6d304af88166'></a>

Figure 2. Thrombin generation versus time under physiological and acidotic conditions. TAT = thrombin-antithrombin complex. Subplots A and B: each subplot shows 30 green and 30 red kinetic trajectories, with each trajectory corresponding to a randomly generated set of pH factors; the blue lines correspond to trajectories at the physiological pH level. Subplots C and D represent kinetic trajectories at the physiological pH level (blue) and median trajectories corresponding to the 5000-trajectory groups computed for acidotic pH levels (other colors) as described in Methods (via the full pH-dependence simulation strategy). E, Normalized thrombin-antithrombin complex (TAT) data on induced acidosis for an in vivo porcine model; the data values are designated with square markers and were extracted from Figure 5 in Martini et al.9

<a id='b4fa3f99-3ed8-4be2-8601-df887259ea52'></a>

to further analyses, such as quantitative parameter calcula-
tion, or plotted against time (Figs. 2–4). For trajectory com-
parisons and plotting, the default 80-minute time interval
was divided into 800 evenly spaced points, and the value
of each trajectory at each time point was recorded. Thus,
for each time point, we obtained a sample of 5000 trajectory
values, which were used for statistical analyses. For exam-
ple, for each sample at each time point, we calculated the
median (Fig. 2, C and D) and quartiles (Fig. 3) and plotted
them against time. Moreover, the samples for each model
output (i.e., thrombin or TAT), each acidotic pH level, and
each time point were tested for normality using the Jarque-
Bera test. 25

<a id='d6d04097-41d2-4cfa-91dd-e550d33d6472'></a>

Because the full pH-dependence simulation strategy is computationally intensive, a simpler simulation algorithm might be preferable for the LETS subject group analysis. The reduced strategy that we developed did not rely on pH factor randomization, but provided a method for direct estimation of the median and quartiles for the quantities of interest (Figs. 3 and 4). This was achieved by adjusting all the catalytic rate constants in the Hockin-Mann model using 1 appropriately selected pH factor set (see Supplemental Digital Content, http://links.lww.com/AA/B118), which was followed by running the model with these new kinetic constants according to the basic simulation protocol. Thus, in the case of the default initial concentrations, we used

<a id='c687e561-17ce-4020-a0fe-24cbaa7f9f3f'></a>

<::A figure composed of five line graphs (A, B, C, D, E) showing the concentration of Thrombin or TAT over time at different pH levels. A. Line graph titled 'Thrombin vs Time'. The y-axis is labeled '[Thrombin] (nM)' ranging from 0 to 350. The x-axis is labeled 'Time (min)' ranging from 0 to 50. Multiple lines are plotted for each pH value: blue lines for pH = 7.4, green lines for pH = 7.2, and red lines for pH = 7.0. B. Line graph titled 'TAT vs Time'. The y-axis is labeled '[TAT] (nM)' ranging from 0 to 1200. The x-axis is labeled 'Time (min)' ranging from 0 to 50. Multiple lines are plotted for each pH value: blue lines for pH = 7.4, green lines for pH = 7.2, and red lines for pH = 7.0. C. Line graph titled 'Thrombin vs Time'. The y-axis is labeled '[Thrombin] (nM)' ranging from 0 to 350. The x-axis is labeled 'Time (min)' ranging from 0 to 60. Single lines are plotted for each pH value: blue for pH = 7.4, purple for pH = 7.3, green for pH = 7.2, orange for pH = 7.1, red for pH = 7.0, and black for pH = 6.9. D. Line graph titled 'TAT vs Time'. The y-axis is labeled '[TAT] (nM)' ranging from 0 to 1200. The x-axis is labeled 'Time (min)' ranging from 0 to 60. Single lines are plotted for each pH value: blue for pH = 7.4, purple for pH = 7.3, green for pH = 7.2, orange for pH = 7.1, red for pH = 7.0, and black for pH = 6.9. E. Line graph titled 'TAT vs Time'. The y-axis is labeled '[TAT] (%)' ranging from 0 to 100. The x-axis is labeled 'Time (min)' ranging from 0 to 7. Lines with square markers are plotted for two pH values: blue for pH = 7.4 and brown for pH = 7.1.::>

<a id='8c22bd4a-7935-4592-a425-11f951a7337c'></a>

280

<a id='24080237-de92-47d7-a2a0-6c6b2ac3e075'></a>

www.anesthesia-analgesia.org

<a id='b855a171-584e-453b-980a-0433c714b857'></a>

ANESTHESIA & ANALGESIA

<!-- PAGE BREAK -->

<a id='3f3b6be6-d87a-497b-915f-cf8667e084df'></a>

<::transcription of the content: chart::>The image displays two plots in the top row and six box plots (labeled A-F) in the bottom row. The top left plot shows [Thrombin] (nM) on the y-axis (0-300 nM) versus Time (min) on the x-axis (0-40 min). It contains several curves (red, green, and dashed black) that peak between 10 and 20 minutes and then decline. The top right plot shows [TAT] (nM) on the y-axis (0-1000 nM) versus Time (min) on the x-axis (0-40 min). It displays several sigmoidal curves (red, green, and dashed black) that increase from approximately 10 minutes and plateau. The bottom row consists of six box plots, each showing a different coagulation parameter as a function of pH (ranging from 6.9 to 7.4 on the x-axis). A: CT (min) on the y-axis (0-70 min). The box plots generally show a decreasing trend in CT as pH increases. B: PT (min) on the y-axis (0-70 min). The box plots generally show a decreasing trend in PT as pH increases. C: MS (nM/min) on the y-axis (0-120 nM/min). The box plots generally show an increasing trend in MS as pH increases. D: PH (nM) on the y-axis (0-350 nM). The box plots generally show an increasing trend in PH as pH increases. E: AUC (nM x min) on the y-axis (0-1500 nM x min). The box plots show relatively stable AUC values across the pH range, with a slight decrease at higher pH. F: Prothrombin time (s) on the y-axis (0-60 s). The box plots generally show a decreasing trend in Prothrombin time as pH increases. <::>both the full and the reduced strategies, whereas in our vir-tual LETS subject analysis (Figs. 5 and 6), we only used the reduced strategy. We also anal as CT for an i default conce 

<a id='98a9478f-a601-48c2-9431-c1ec32e4a65d'></a>

**Quantitative Parameter Analysis for Kinetic
Trajectories**
For the simulated thrombin trajectories, we calculated quan-
titative parameters of thrombin generation 16,18: clotting time
(CT) (i.e., time to 10 nM thrombin), thrombin peak time,
maximum slope of the thrombin trajectory (also known as
the maximum rate of thrombin generation), thrombin peak
height, and the area under the thrombin trajectory (AUC).

<a id='125b6df2-ab91-4867-b93c-5df5d44fafe2'></a>

Figure 3. Thrombin generation ranges for acidotic pH levels. Solid green and red lines correspond to the interquartile range and median, respectively, calculated for the groups of 5000 kinetic trajectories generated via the full pH-dependence simulation strategy as described in Methods (the medians, also shown in Fig. 2, C and D, are shown here for comparison purposes). The dashed lines correspond to the acidotic-pH kinetic trajectories calculated using our reduced pH-dependence simulation strategy. For each subplot, the left and right groups of trajectories correspond to pH 7.2 and 7.0, respectively.

<a id='fdb3b4a4-6249-4a95-ae1d-3d3d18b42703'></a>

Figure 4. Box and whisker plot of the quantitative parameters of thrombin generation trajectories under physiological and acidotic pH conditions. A, Clotting time; B, Thrombin peak time; C, Maximum slope of the thrombin trajectory; D, Thrombin peak height; E, Area under the thrombin trajectory (or "curve"); F, Prothrombin time. The blue squares correspond to single values for physiological pH, whereas the box plots show thrombin generation parameter distributions corresponding to the groups of 5000 thrombin trajectories generated via the full pH-dependence simulation strategy. Dashed whiskers, green boxes, and red lines show the ranges, interquartile ranges, and medians of the parameter distributions, respectively. The red circles correspond to the estimates of the median values calculated using our reduced pH-dependence simulation strategy (see Methods). The green circles were calculated similarly to the red circles as an estimate of the interquartile ranges shown as green boxes. Acidosis-induced median fold changes in the area under the thrombin trajectory with respect to its physiological value were smaller than corresponding median fold changes for every other thrombin generation parameter (P = 0 to machine precision, Wilcoxon rank sum test; comparisons for each acidotic pH level performed independently.) For each (acidotic) thrombin trajectory and each thrombin generation parameter, fold_change = AV/NV if AV > NV and fold_change = NV/AV otherwise, where AV and NV are the (acidotic) value of the parameter for that thrombin trajectory and the parameter's physiological value, respectively.

<a id='e84f9116-b5e9-4b4e-b1ff-9c74759af6d0'></a>

We also analyzed prothrombin time, which was computed as CT for an initial tissue factor concentration of 17 nM17 (its default concentration in the model was 5 pM, a standard value for in vitro thrombin generation assays). Likewise, for the simulated TAT trajectories, we calculated the following quantitative parameters: onset time (i.e., time to 10 nM TAT), activation time (i.e., time to 50% of the TAT final level), maximum slope of the TAT trajectory, and TAT final level (i.e., the TAT level at 80 minutes).

<a id='64f1205a-f711-45d4-8142-ec9b4a9ba6c8'></a>

For each acidotic pH level, application of the full pH-
dependence simulation strategy resulted in the generation of
5000 values for each quantitative parameter (i.e., 1 parameter

<a id='abd5b73b-afab-4a2b-bc9f-da7579c031e7'></a>

August 2015 • Volume 121 • Number 2

<a id='359ddea1-80ef-43f1-88a4-7048cfba8a4e'></a>

www.anesthesia-analgesia.org

<a id='6422b151-e0eb-489f-bc0e-4fc54422d0ac'></a>

281

<!-- PAGE BREAK -->

<a id='0e91d124-6091-480e-b66b-3dbd29515e43'></a>

Effects of Acidosis on Thrombin Generation <::A series of five line plots (A-E) showing the distribution of 'Number of subjects' (y-axis) against 'Fold change' (x-axis) at different pH levels. The plots display six different parameters, color-coded and identified by a legend in plot B:
- CT (green line)
- PT (blue line)
- MS (black line)
- PH (red line)
- AUC (purple line)
- Prothrombin time (orange line)

Plot A: pH 7.3. The x-axis ranges from 1 to 1.4.
Plot B: pH 7.2. The x-axis ranges from 1 to 2.
Plot C: pH 7.1. The x-axis ranges from 1 to 3.
Plot D: pH 7.0. The x-axis ranges from 1 to 5.
Plot E: pH 6.9. The x-axis ranges from 1 to 12.

Across all plots, the y-axis 'Number of subjects' ranges from 0 to 400 (or 0 to 300 in plot E).
: chart::>

<a id='e0ca7081-e8f0-440b-a941-2b3ef9dce3f5'></a>

Figure 5. Fold change distributions in the virtual Leiden Thrombophilia Study (LETS) subject group for the 5 thrombin generation parameters and prothrombin time. For each virtual LETS subject, each parameter, and each acidotic pH level, fold_change = AV/NV if AV > NV and fold_change = NV/AV otherwise, where AV and NV are the acidotic and physiological values of the parameter in that subject, respectively. The plots show distribution histograms generated using the MATLAB function HIST with 100 bins splitting up the interval between 1 and the maximum parameter fold change value for a given pH level. CT = clotting time; PT = thrombin peak time; MS = maximum slope of the thrombin trajectory; PH = thrombin peak height; AUC = area under the thrombin trajectory (or "curve").

<a id='2b95ae4a-f486-48bc-8308-94ff3982e5a3'></a>

value for each kinetic trajectory). The samples were tested for normality using the Jarque-Bera test. To compare these parameter samples with the physiological values of the corresponding parameters, we used the Wilcoxon rank sum test.26 In our virtual LETS subject analysis (performed using the reduced pH-dependence simulation strategy), for each considered pH level and each quantitative parameter, we generated a sample of 472 values (i.e., 1 value per 1 virtual subject). Such samples were also tested for normality using the Jarque-Bera test. To test for statistically significant differences between such parameter samples for physiological and acidotic pH levels, we used the Wilcoxon signed rank test.26 The differences between the samples were illustrated by calculating their medians and interquartile ranges. The P values resulting from the Wilcoxon tests were Bonferroni-corrected to account for multiple comparisons. The denominator for the Bonferroni correction was equal to 5, which reflects comparisons between a sample for the physiological pH level and the corresponding samples for each of the considered five acidotic pH levels.

<a id='5e3f583f-c034-4b12-b6f0-ba44a6e0a271'></a>

**Intrasubject Parameter Change Analysis for the LETS Subject Group**
The magnitude of pH-induced change in different thrombin generation parameters for the same subject was assessed via intrasubject fold change comparisons. For each virtual LETS

<a id='bdb52e08-28dc-4241-ba03-98a77d1f6636'></a>

subject, each parameter, and each acidotic pH level, fold_ change = AV/NV if AV > NV and fold_change = NV/AV otherwise, where AV and NV are the acidotic and physi- ological values of the parameter, respectively. We then followed our previous work$^{15,16}$ and estimated the prob- ability of fold change patterns by calculating the fraction of virtual subjects for which the pattern of interest was detected. For example, we considered the pattern FC(AUC) < FC(X), where FC(AUC) is the fold change in the AUC and FC(X) is the fold change in any other thrombin genera- tion parameter in the same virtual subject at the same pH level. The SE of a probability estimate q was computed as SE = √(q(1-q)/N), where N = 472 is the LETS subject group size.$^{26}$ We also report a 95% confidence interval (95% CI) for q; its upper boundary point is 1.00, and its lower bound- ary point was calculated as the exact (Clopper-Pearson) 1-sided 95% lower confidence limit.$^{27}$

<a id='3358369c-da5a-42d6-8af7-ab615d98944a'></a>

**Intersubject Variability Analysis for**
**the LETS Subject Group**
We analyzed the intersubject variation of the parameter
fold changes and parameter values by visualizing the
fold-change and parameter histograms (Figs. 5 and 6) and
calculating the interquartile ranges for the parameter dis-
tributions (Tables 1 and 2). The overlap between 2 distribu-
tions (or histograms) of a thrombin generation parameter

<a id='86f7d5e8-4270-4cbf-a0ae-be56eefdf86a'></a>

282

<a id='bc3002c7-c985-4049-a59e-6a35e29f7f92'></a>

www.anesthesia-analgesia.org

<a id='361f0f20-4de2-4f75-b6b9-4bc7adc2d875'></a>

ANESTHESIA & ANALGESIA

<!-- PAGE BREAK -->

<a id='4b74a7d1-1a97-4bf9-9679-64d9fb4ed4cd'></a>

<::Figure: Six panels (A-F) displaying distributions of various thrombin generation parameters for different pH levels. Panel A: Histogram showing the distribution of CT (clotting time) in minutes. The y-axis represents the Number of subjects. The legend indicates pH = 7.4 (blue line), pH = 7.3 (purple line), pH = 7.2 (green line), pH = 7.1 (orange line), pH = 7.0 (red line), and pH = 6.9 (black line). Panel B: Histogram showing the distribution of PT (prothrombin time) in minutes. The y-axis represents the Number of subjects. Panel C: Histogram showing the distribution of MS (maximum thrombin generation rate) in nM/min. The y-axis represents the Number of subjects. Panel D: Histogram showing the distribution of PH (peak height of thrombin generation) in nM. The y-axis represents the Number of subjects. Panel E: Histogram showing the distribution of AUC (area under the curve of thrombin generation) in nM x min. The y-axis represents the Number of subjects. Panel F: Histogram showing the distribution of Prothrombin time in seconds. The y-axis represents the Number of subjects.::>

(with the 2 distributions corresponding to 2 distinct pH levels) was quantified via the Bhattacharyya coefficient ρ (Table 3) defined as follows.²⁸ Let x and y be histograms with m bins each, and let xᵢ and yᵢ be the numbers of obser- vations from x and y, respectively, falling into the ith bin. (In our analysis, the number of observations in the ith bin is the number of virtual LETS subjects whose thrombin generation parameter values fall within that bin.) The Bhattacharyya coefficient was defined by the expression

monotonically responding to A and B), which pled pH factor and each acidic prothrombin slope and peak values at pH 6.9, acidotic pH levels.

<a id='88dab242-4950-48b7-abf0-391af2b291a8'></a>

Figure 6. Thrombin generation parameter distributions (including prothrombin time) in the virtual Leiden Thrombophilia Study (LETS) subject group for different pH levels. The plots show distribution histograms generated using the MATLAB function HIST with 50 bins splitting up the interval between 0 and the maximum value for a given thrombin generation parameter. CT = clotting time; PT = thrombin peak time; MS = maximum slope of the thrombin trajectory; PH = thrombin peak height; AUC = area under the thrombin trajectory (or "curve").

<a id='5d096d0a-77c6-48fe-b1db-1cfc5c829dc3'></a>

<::transcription of the content
: figure::>
$\rho(x,y) = \sum_{i=1}^{m} \sqrt{(x_i / N)(y_i / N)}$

<a id='fc5cd243-cd7a-400f-9d4a-1bbcccf3e2f3'></a>

where N = 472. It follows that 0 \u2264 \u03c1(x,y) \u2264 1; \u03c1(x,y) = 0 when x and y do not overlap (i.e., when none of the bins contain observations from both x and y), and \u03c1(x,y)=1 when x and y coincide (i.e., when x\u2081 = y\u2081, i = 1,..., m).

<a id='7b2e1a57-6394-4a53-b025-95a22488a229'></a>

### RESULTS
pH Dependence of Thrombin Generation
Examples of distinct thrombin and TAT kinetic trajectories generated using the full pH-dependence simulation strategy are shown in Figure 2, A and B, respectively. In each 5000-trajectory group (1 group corresponded to 1 acidotic pH level), all thrombin trajectories possessed a characteristic one-peaked shape, and all TAT trajectories were

<a id='19b60219-fc59-4dbf-b588-ea3e85cf2e06'></a>

monotonically increasing. Trajectories from the groups corresponding to different pH levels often overlapped (Fig. 2, A and B), which reflects the variations in the randomly sampled pH factors. Yet, for each distinct thrombin trajectory and each acidotic pH level, the values of CT, peak time, and prothrombin time were larger, and the values of maximum slope and peak height were smaller, than the corresponding values at pH 7.4. The AUC (i.e., the area under the curve) for acidotic pH levels was larger than that for pH 7.4 in 99.54% of the trajectories. Likewise, for each distinct TAT trajectory and each acidotic pH level, the values of onset time and activation time were larger, and the values of maximum slope were smaller, than the corresponding values at pH 7.4. The TAT final level for acidotic pH levels was smaller than that for pH 7.4 in 99.49% of the trajectories.

<a id='279806e7-8264-4efc-9b1f-fe4a6fbe4d65'></a>

To elucidate major trends in the 5000-trajectory groups at each acidotic pH level, we analyzed the corresponding median trajectories. Median trajectories were used because the distributions of thrombin and TAT concentrations in each 5000-trajectory group deviated from normality (P ≤ 0.001, thrombin and TAT samples at each time point and each acidotic pH level tested independently). Acidosis progressively delayed the time of onset and reduced the amount of thrombin and TAT generation, as reflected by median trajectories (Fig. 2, C and D). These model predictions were consistent with experimental results for a porcine model of acidosis (Fig. 2E).⁹

<a id='10d1d08f-a950-4e7f-a6c6-91333a589a0b'></a>

August 2015 • Volume 121 • Number 2

<a id='4ec226f1-72a2-44df-91d9-cf8a9b790068'></a>

www.anesthesia-analgesia.org

<a id='628aec80-e667-4b62-91d9-39a54d24bde0'></a>

283

<!-- PAGE BREAK -->

<a id='87ed0c2d-fc97-4626-a953-f5f6ddfff324'></a>

Effects of Acidosis on Thrombin Generation

<a id='960e39ba-580c-47de-8283-885c191a9f63'></a>

<table id="6-1">
<tr><td id="6-2" colspan="7">Table 1. Thrombin Generation Parameters in the Virtual Leiden Thrombophilia Study (LETS) Subject Group Under pH Variation</td></tr>
<tr><td id="6-3">pH</td><td id="6-4">CT, min</td><td id="6-5">PT, min</td><td id="6-6">MS, nM/min</td><td id="6-7">PH, nM</td><td id="6-8">AUC, nM × min</td><td id="6-9">Prothrombin time, s</td></tr>
<tr><td id="6-a">7.4</td><td id="6-b">3.31 (2.99-3.73)</td><td id="6-c">7.90 (7.43-8.49)</td><td id="6-d">121.28 (98.89-145.28)</td><td id="6-e">320.34 (276.06-368.27)</td><td id="6-f">1304.27 (1153.38-1481.32)</td><td id="6-g">11.50 (10.85-12.21)</td></tr>
<tr><td id="6-h">7.3</td><td id="6-i">4.31 (3.90-4.86)</td><td id="6-j">9.64 (9.06-10.44)</td><td id="6-k">90.54 (73.30-108.57)</td><td id="6-l">281.36 (241.04-324.05)</td><td id="6-m">1315.47 (1163.29-1493.30)</td><td id="6-n">13.31 (12.53-14.12)</td></tr>
<tr><td id="6-o">7.2</td><td id="6-p">5.74 (5.17-6.48)</td><td id="6-q">12.03 (11.25-13.07)</td><td id="6-r">65.08 (52.37-78.35)</td><td id="6-s">241.12 (205.74-279.13)</td><td id="6-t">1327.91 (1174.45-1508.11)</td><td id="6-u">15.57 (14.66-16.50)</td></tr>
<tr><td id="6-v">7.1</td><td id="6-w">7.78 (6.94-8.80)</td><td id="6-x">15.29 (14.24-16.61)</td><td id="6-y">44.69 (35.68-54.55)</td><td id="6-z">201.75 (171.50-234.28)</td><td id="6-A">1342.04 (1186.81-1524.07)</td><td id="6-B">18.45 (17.34-19.60)</td></tr>
<tr><td id="6-C">7.0</td><td id="6-D">10.96 (9.76-12.46)</td><td id="6-E">20.28 (18.78-22.08)</td><td id="6-F">28.20 (22.28-35.48)</td><td id="6-G">160.96 (136.16-189.18)</td><td id="6-H">1359.89 (1201.60-1543.85)</td><td id="6-I">22.52 (21.14-23.97)</td></tr>
<tr><td id="6-J">6.9</td><td id="6-K">17.04 (15.08-19.46)</td><td id="6-L">29.45 (27.02-32.33)</td><td id="6-M">14.86 (11.41–19.06)</td><td id="6-N">116.15 (97.16-138.65)</td><td id="6-O">1383.50 (1221.99–1571.16)</td><td id="6-P">29.4 (27.52-31.43)</td></tr>
</table>
The data are shown as median (interquartile range), because the distributions of all the parameters at all considered pH levels deviated from normality (P ≤ 0.001 for each parameter at each pH level tested independently).
Statistical significance of acidosis-induced differences (for each parameter tested independently): physiological-pH parameter values versus acidotic-pH values for the same parameter (comparison of statistical samples),
P < 10⁻⁵. The P-value computations were performed as described in Mitrophanov et al.¹⁷ (Table 1).
CT = clotting time; PT = thrombin peak time; MS = maximum slope of the thrombin trajectory; PH = thrombin peak height; AUC = area under the thrombin trajectory (or “curve”).

<a id='17d86e81-2b28-40c0-928b-707af85b57f1'></a>

The interquartile distances for the simulated groups of distinct trajectories could be considerable (up to 89.00% of the maximum median value for thrombin generation and up to 64.22% of the maximum median value for TAT gen- eration; see examples in Fig. 3). One reason for this could be imprecise estimation of the median and quartile trajec- tories owing to insufficient sample size. To test this possi- bility, we repeated the computations with trajectory group size increased to 10,000 (trajectories generated using our full strategy for pH-dependence simulation, as described in Methods). The resulting median and quartile trajectories practically coincided with the corresponding trajectories for the 5000-trajectory groups (results not shown). This finding suggests that the interquartile value spread may primarily reflect the uncertainty in the pH factor values, which is cap- tured in the full pH-dependence simulation strategy. Yet, the domain shapes defined by the interquartile distances were consistent with the trends shown by the median tra- jectories (Fig. 2, C and D, and Fig. 3).

<a id='c5fcfd52-205d-441f-abe5-e676b1bd42f9'></a>

To test our reduced pH-dependence simulation strategy, we used it to approximate the median trajectories generated via the full simulation strategy. Yet, the temporal trajectories generated via the reduced strategy (see examples shown for pH 7.2 and 7.0, dashed black lines in Fig. 3) could noticeably deviate from the 5000-trajectory group medians (red lines in Fig. 3) for both thrombin and TAT, especially at pH 6.9 and 7.0 (comparison of statistical samples using Wilcoxon's rank sum test, P < 10-5 for certain time points and acidotic pH levels). This result indicates that the use of the full pH-dependence simulation strategy is preferable for accurate estimation of the thrombin and TAT time courses at acidotic pH levels.

<a id='91b8459c-7434-4d6a-9be2-47becf96d1cf'></a>

**Quantitative Parameters of Thrombin Generation**
The groups of quantitative parameter values for thrombin and TAT corresponding to each group of 5000 trajectories (generated via the full pH-dependence simulation strategy) were characterized using medians and interquartile ranges because all corresponding distributions deviated from normality (P ≤ 0.001 for each parameter at each pH level tested independently). Acidosis caused a progressive increase in median CT, thrombin peak time, the AUC, and prothrombin time, while the medians for both maximum slope of the thrombin trajectory and thrombin peak height progressively decreased (statistical sample comparisons for each parameter tested independently: physiological-pH parameter values versus acidotic values for the same parameter, P = 0 to machine precision) (Fig. 4). Interestingly, the median value of the AUC at pH 6.9 was only 1.06-fold (95% CI, 1.061–1.062, calculated using the large sample CI approximation for the median29) larger than its value at physiological pH, which is a small change compared with other parameters.

<a id='c6e38ec5-f3a9-4f63-881e-668af1a86d77'></a>

The interquartile ranges for CT, thrombin peak time, the AUC, and prothrombin time were comparatively small in relation to the median values, particularly for higher pH levels (Fig. 4). This suggests that the full simulation strat- egy can produce informative estimates of the quantitative thrombin generation parameters. Interestingly, the param- eter values calculated using the reduced pH-dependence simulation strategy nearly coincided with the correspond- ing parameter values calculated as sample medians for the

<a id='e7c5b6be-fb1e-4fa2-929d-da782fdd0079'></a>

284

<a id='aab090ed-6d30-42c5-a217-762d37c139c6'></a>

www.anesthesia-analgesia.org

<a id='c74f8b6d-7173-4d35-9910-4bdb8e27a771'></a>

ANESTHESIA & ANALGESIA

<!-- PAGE BREAK -->

<a id='c27c8ea0-832a-4841-ac5d-31c4aab9b5cf'></a>

<table id="7-1">
<tr><td id="7-2" colspan="5">Table 2. Thrombin-Antithrombin Complex (TAT) Generation Parameters in the Virtual Leiden Thrombophilia Study (LETS) Subject Group Under pH Variation</td></tr>
<tr><td id="7-3">pH</td><td id="7-4">OT, min</td><td id="7-5">AT, min</td><td id="7-6">MS_TAT, nM/min</td><td id="7-7">FL, nM</td></tr>
<tr><td id="7-8">7.4</td><td id="7-9">5.33 (5.03-5.80)</td><td id="7-a">8.27 (7.75-8.88)</td><td id="7-b">288.76 (249.67-323.14)</td><td id="7-c">999.71 (901.51-1092.40)</td></tr>
<tr><td id="7-d">7.3</td><td id="7-e">6.69 (6.27-7.30)</td><td id="7-f">10.06 (9.46-10.91)</td><td id="7-g">236.69 (204.75-265.90)</td><td id="7-h">933.41 (839.87-1028.64)</td></tr>
<tr><td id="7-i">7.2</td><td id="7-j">8.57 (7.98-9.41)</td><td id="7-k">12.57 (11.77-13.64)</td><td id="7-l">187.79 (160.26-212.51)</td><td id="7-m">859.95 (767.23-954.45)</td></tr>
<tr><td id="7-n">7.1</td><td id="7-o">11.21 (10.33-12.34)</td><td id="7-p">16.00 (14.91-17.44)</td><td id="7-q">142.43 (119.07-162.94)</td><td id="7-r">781.79 (693.56-871.77)</td></tr>
<tr><td id="7-s">7.0</td><td id="7-t">15.24 (13.96-16.91)</td><td id="7-u">21.30 (19.64-23.31)</td><td id="7-v">98.61 (81.56-116.21)</td><td id="7-w">687.70 (600.81-767.77)</td></tr>
<tr><td id="7-x">6.9</td><td id="7-y">22.76 (20.59-25.43)</td><td id="7-z">31.06 (28.40-34.24)</td><td id="7-A">58.44 (45.80-71.13)</td><td id="7-B">556.93 (484.20-635.42)</td></tr>
</table>
The data are shown as median (interquartile range), because the distributions of all the parameters at all considered pH levels deviated from normality (P ≤ 0.001
for each parameter at each pH level tested independently).
Statistical significance of acidosis-induced differences (for each parameter tested independently): physiological-pH parameter values versus acidotic-pH values
for the same parameter (comparison of statistical samples), P < 10⁻⁵. The P-value computations were performed as described in Mitrophanov et al.¹⁷ (Table 2).
OT = TAT onset time; AT = 50% activation time; MS_TAT = maximum slope of the TAT trajectory; FL = TAT final level.

<a id='32b3911c-5db0-4ab3-aad0-8aca9e5a5714'></a>

<table id="7-C">
<tr><td id="7-D" colspan="7">Table 3. Bhattacharyya Coefficients for the Thrombin Generation Parameters in the Virtual Leiden Thrombophilia Study (LETS) Subject Group</td></tr>
<tr><td id="7-E">pH</td><td id="7-F">CT, min</td><td id="7-G">PT, min</td><td id="7-H">MS, nM/min</td><td id="7-I">PH, nM</td><td id="7-J">AUC, nM x min</td><td id="7-K">Prothrombin time, s</td></tr>
<tr><td id="7-L">7.3</td><td id="7-M">0.75</td><td id="7-N">0.65</td><td id="7-O">0.86</td><td id="7-P">0.93</td><td id="7-Q">1.00</td><td id="7-R">0.74</td></tr>
<tr><td id="7-S">7.2</td><td id="7-T">0.30</td><td id="7-U">0.13</td><td id="7-V">0.55</td><td id="7-W">0.78</td><td id="7-X">0.98</td><td id="7-Y">0.26</td></tr>
<tr><td id="7-Z">7.1</td><td id="7-10">0.04</td><td id="7-11">0.01</td><td id="7-12">0.22</td><td id="7-13">0.56</td><td id="7-14">0.98</td><td id="7-15">0.05</td></tr>
<tr><td id="7-16">7.0</td><td id="7-17">0.00</td><td id="7-18">0.00</td><td id="7-19">0.04</td><td id="7-1a">0.30</td><td id="7-1b">0.97</td><td id="7-1c">0.00</td></tr>
<tr><td id="7-1d">6.9</td><td id="7-1e">0.00</td><td id="7-1f">0.00</td><td id="7-1g">0.00</td><td id="7-1h">0.09</td><td id="7-1i">0.96</td><td id="7-1j">0.00</td></tr>
</table>
The coefficients reflect the overlaps between the distributions (or histograms) for the thrombin generation parameters at pH 7.4 and the distributions for the
same parameters at the indicated acidotic pH levels.
CT = clotting time; PT = thrombin peak time; MS = maximum slope of the thrombin trajectory; PH = thrombin peak height; AUC = area under the thrombin
trajectory (or "curve").

<a id='6118e4a4-f449-4a9b-9db5-0c2e47dd8f3f'></a>

5000-trajectory groups from the full pH-dependence simula-
tion strategy (Fig. 4). Moreover, the parameter distributions'
1st and 3rd quartiles could also be approximated using the
reduced simulation strategy. These approximations were
particularly accurate for pH 7.2 and 7.3 (Fig. 4).

<a id='c72d6800-4c61-4e1e-aba1-5e52bc5993fb'></a>

For TAT, acidosis progressively increased median onset time and activation time, and progressively decreased the median maximum slope of the TAT trajectory and TAT final level (statistical sample comparisons for each parameter tested independently: physiological-pH parameter values versus acidotic values for the same parameter, P = 0 to machine precision). Accuracy of approximation of the median and quartile parameter values using our reduced pH-dependence simulation strategy was similar to the case of thrombin trajectories (Fig. 4). Taken together, these results suggest that the application of our reduced simulation strategy can be particularly effective in the analysis of individual quantitative trajectory parameters (Fig. 4), rather than whole trajectories (Fig. 3).

<a id='a9c953f3-2655-4f53-bad6-d9b6cb4609f0'></a>

**pH Effects in the Group of Virtual LETS Subjects**
Because our virtual LETS subject analysis focused only on
quantitative parameters (rather than the whole trajecto-
ries) of thrombin generation, we performed the simulations
using only the reduced pH-dependence simulation strategy.
Indeed, its use was justified by the sufficiently high accu-
racy of this approximation detected in the case of average
initial concentrations of coagulation proteins (Fig. 4). While
the calculated thrombin and TAT generation parameter val-
ues in the LETS group displayed substantial intersubject
variability (Tables 1 and 2), the general patterns character-
izing the effects of acidosis were robust and consistent with
our results for the case of average initial concentrations of
coagulation proteins. Indeed, for every virtual subject, CT,

<a id='68cc649d-7e01-4a53-b105-68c40837378d'></a>

thrombin peak time, the AUC, and prothrombin time mono-tonically increased with acidosis, whereas maximum slope of the thrombin trajectory and thrombin peak height mono-tonically decreased. Likewise, for TAT trajectories, onset time and activation time increased, while maximum slope and final level decreased.

<a id='ae78b348-182f-47a2-9e37-891657545739'></a>

For every acidotic pH level, the pattern FC(MS)
> FC(CT) > FC(X) occurred in every virtual subject.
Therefore, estimated probability of the pattern's occur-
rence in the same subject was equal to 1.00 (SE, 0.00;
95% CI, 0.99–1.00). [Here, FC(.) denotes fold change in a
thrombin generation parameter, and MS, CT, and X des-
ignate maximum slope of the thrombin trajectory, clot-
ting time, and any other thrombin generation parameter,
respectively.] This result suggests that maximum slope
and CT can be regarded as the 2 most sensitive thrombin
generation parameters in each virtual LETS subject. The
least sensitive parameter was the AUC because the pat-
tern FC(AUC) < FC(X) (with X being any other thrombin
generation parameter) occurred in every virtual subject
and, therefore, its estimated probability was equal to 1.00
(SE, 0.00; 95% CI, 0.99–1.00). Interestingly, while these
results reflect the intrasubject variability, our conclusions
regarding the most- and the least-sensitive parameters
can also be reached by visually comparing the fold change
distributions reflecting the intersubject variability in the
virtual subject group (Fig. 5).

<a id='3adbf7ed-1b62-42b1-ac91-a3023c9e3975'></a>

These findings imply that maximum slope of the thrombin trajectory could potentially be used to discriminate between physiological and acidotic thrombin generation— a question related to the problem of coagulopathy diagnostics. Specifically, would it be possible to tell whether a thrombin trajectory was generated under physiological (pH 7.4) or acidotic pH (for example, pH 7.0) conditions just by

<a id='591ed1b8-78d5-4129-923b-f6c4997b4aaf'></a>

August 2015 • Volume 121 • Number 2

<a id='40f21e84-8d71-4e93-9819-826a1fa5c439'></a>

www.anesthesia-analgesia.org

<a id='1a204c5c-278c-44d8-9d5e-a3294cc79405'></a>

285

<!-- PAGE BREAK -->

<a id='39822460-460f-4ecb-a8e0-e425fd52c7d2'></a>

Effects of Acidosis on Thrombin Generation

<a id='2d16d820-de46-48db-846b-6f4e9b8fb4bd'></a>

looking at its maximum slope value? To investigate this
possibility in the context of intersubject variability in the
LETS group, we estimated the overlaps between the param-
eter distributions for different pH values (Fig. 6) using the
Bhattacharyya coefficients (Table 3). Surprisingly, maximum
slope was inferior to other parameters in its discriminative
capacity. Indeed, the maximum slope distributions for pH
7.4 and pH 7.0 overlapped (Fig. 6C, Table 3), thereby thwart-
ing the possibility to tell whether a given maximum slope
value has arisen under a physiological (pH 7.4) or acidotic
(pH 7.0) condition. By contrast, the pH 7.4 and pH 7.0 distri-
butions for CT (Fig. 6A), thrombin peak time (Fig. 6B), and
prothrombin time (Fig. 6F) were fully separated (Table 3),
even though thrombin peak time and prothrombin time dis-
played only moderate fold change magnitudes (Fig. 5). In
fact, the overlaps between the maximum slope distributions
at acidotic pH levels with the maximum slope distribu-
tion at physiological pH level exceeded the corresponding
distribution overlaps for CT, thrombin peak time, and pro-
thrombin time for all acidotic pH levels except 6.9 (Table 3).
This effect could be understood by noticing the large spread
of the fold change distribution for maximum slope (Fig. 5),
which suggests that its high sensitivity to intersubject vari-
ability causes its distributions for different pH levels to
overlap (Fig. 6C). This sensitivity to intersubject variability
thus prevents maximum slope from being an informative
indicator of acidosis in a subject population, despite its high
sensitivity to acidosis in individual subjects.

<a id='35621d69-0a5f-4062-b7a1-ac493914b504'></a>

**DISCUSSION** It is generally known that enzymatic activity is influenced by the pH of the biochemical milieu.22-24 Therefore, it can be expected that the phases of the complex enzymatic aspects of the blood coagulation process would be significantly affected by acidosis. Our computational modeling methodology allowed us to link the pH dependence of individual reactions in the thrombin generation network with the final end points of the study. We used the LETS data in the definition of the initial concentrations for the model and incorporated the pH dependence by adjusting the values of the model's kinetic constants. We analyzed the model's ability to qualitatively predict the effects of acidosis. Our results support our hypothesis that acidosis may progressively delay, and reduce the levels of, thrombin generation. Moreover, we found this combined effect to be pronounced, despite considerable intersubject variability in the LETS subject group.

<a id='7ef3b802-5536-4e57-8ec9-b6fe1704b0b8'></a>

The assessment of thrombin generation can be divided into 2 categories: assessment of thrombus formation (CT, thrombin peak time, and maximum slope of the thrombin trajectory) and the assessment of the quantity of thrombin generated (thrombin peak height and the AUC).18 Likewise, the TAT trajectory parameters that we used in this study are an indicator of the latency of thrombus formation as measured by onset time, activation time, and maximum slope, whereas TAT final level represents a measurement of the quantity of thrombus. Our results indicate that acidosis strongly influenced all of the above parameters except the AUC. In our analysis, acidosis acted by delaying thrombin generation, as evidenced by an increase in CT, thrombin peak time, the prothrombin time, TAT onset time, and TAT

<a id='6c0526a9-e3f3-43f9-8261-fc9da6bb655a'></a>

activation time, and by reducing the maximum thrombin level, as evidenced by a decrease in thrombin peak height and TAT final level. The relative insensitivity of the area under the curve to acidosis may be explained by noticing that lower rates of thrombin accumulation and the result- ing lower levels of active thrombin lead to a decreased rate of thrombin inhibition by antithrombin. This, in turn, may result in a relatively wider thrombin trajectory, thereby compensating for the acidosis-induced reduction in the thrombin peak height.

<a id='748c3bb6-3dd3-4952-a9b6-1fb35795d321'></a>

Trauma-associated coagulopathy can have several causes, including plasma dilution and hypothermia. Our results suggest that the effect of acidosis on thrombin generation is similar to that expected from hemodilution.16 There is, however, a considerable difference. The maximum slope of the thrombin curve is the most sensitive parameter for both acidosis and hemodilution, and CT is the second most sensitive parameter for acidosis. In contrast, thrombin peak height is the second most sensitive parameter for hemodilution.16 Hypothermia is expected to considerably delay thrombin generation and increase the area under the thrombin trajectory, and to leave thrombin peak height and TAT final level practically unchanged.17 Thus, each of these 3 coagulopathy-inducing factors (i.e., hemodilution, hypothermia, and acidosis) is characterized by unique "signature" effects on thrombin generation. It can be anticipated that a combination of hypothermia and acidosis, similarly to a combination of hypothermia and dilution,17 would both strongly delay the onset and decrease the levels of thrombin generation.1,3

<a id='eb040cbb-ba4d-463f-8fa9-a066d6425285'></a>

Our results are consistent with those reported by Martini et al.,9 who showed that acidosis induced in an in vivo porcine model (by infusion of hydrochloric acid in lactated Ringer's solution) delays the onset and decreases the levels of TAT generation. Further, Darlington et al.,30,31 using a porcine model of acidosis, found that CT and prothrombin time (which, like TAT onset time, reflect the time of onset of thrombin generation) significantly increased when acidosis was induced by hydrochloric acid infusion.30,31 In contrast, when acidosis was induced by hemorrhage/hypoventilation, it resulted in a thrombin peak height decrease, with no significant effect on the prothrombin time and CT measured via the Calibrated Automated Thrombogram (Thrombinoscope BV, Maastricht, The Netherlands).30,31 These discrepancies between experimental results using different strategies to induce acidosis and different types of measurement assays suggest that these (and perhaps other) factors influence the observed effects of acidosis on the onset (and perhaps other aspects) of thrombus formation. This conclusion is supported by evidence obtained from human blood in vitro.10 Indeed, it was shown that acidosis induces delays in prothrombin time and the onset of thrombus formation determined using thromboelastography.10 Yet, other studies reported a lack of significant acidosis-induced changes in clotting initiation time measured by viscoelastic assays in whole human blood.8,12 Paradoxically, Bladbjerg and Jespersen32 reported accelerated clotting initiation upon pH reduction from 7.4 to 7.0. These disparities highlight the limits of our current knowledge about acidosis and illustrate the necessity of further experimental work.

<a id='bd99083b-b092-427c-a377-cbd1835a50d1'></a>

286

<a id='21811acf-8cfb-4dd2-825e-7fbbfece3320'></a>

www.anesthesia-analgesia.org

<a id='a94537d6-7d10-4724-afda-db2110b77b75'></a>

ANESTHESIA & ANALGESIA

<!-- PAGE BREAK -->

<a id='f214020b-82b3-4f28-8324-1c70707396a6'></a>

Thrombin generation assays have been proposed as an alternative to traditional laboratory tests, such as prothrom- bin time and partial thromboplastin time, for accurate assessment of the functional status of the blood coagulation system and diagnosis of its abnormalities.33,34 While their utility in the specific settings of trauma and complex sur- gery require further studies, in this study we investigated the concept of using numerical parameters of thrombin generation to distinguish between healthy and diseased states. It is conceivable that a high sensitivity of a thrombin generation parameter based on intrasubject comparisons (i.e., its larger acidosis-induced fold change in comparison with that of the other parameters in the same subject) may lead to better diagnostic dicrimination between healthy and diseased states, because decreasing the pH would lead to large, easily detectable shifts in the parameter distribution. However, our results demonstrate that the most sensitive parameter to lowered pH, that is, the maximum slope of the thrombin curve, is also highly sensitive to intersubject variability in clotting factor composition, which leads to increased overlaps between maximum slope distributions corresponding to different pH levels. Thus, our results sug- gest that the best discriminating parameters for determin- ing the impact of lowered pH on thrombin kinetics should demonstrate both a sufficiently high intrasubject sensitivity to acidosis and only moderate intersubject variability. This general principle can be applied to other coagulation mea- surement techniques suggested for coagulopathy diagnos- tics, such as thromboelastography.35,36

<a id='42d760ec-a235-451f-8e5d-b22d65d27ba0'></a>

There are several limitations to this study. Because our investigation strategy builds on the computational model of thrombin generation (i.e., the Hockin-Mann model),6,19,20 our approach has the conceptual limitations of the original model. First, it primarily reflects biochemical reactions in synthetic plasma; therefore, it does not represent platelet activation kinetics and only partially represents the hemostatic proteome of human blood. Second, the model reflects a static assay that cannot be used to investigate the effects of blood flow or spatial heterogeneity on blood coagulation. Third, this is a thrombin generation model that does not account for other processes that contribute to thrombus formation, such as fibrin generation, fibrin polymerization, and fibrinolysis. Yet, the Hockin-Mann model, which reflects a frequently used in vitro setup and has been extensively validated, has demonstrated its ability to yield valuable mechanistic insights and informative predictions regarding thrombin generation kinetics.6,18,20,37 Finally, our modeling strategy does not reproduce subtle but important phenomena associated with acidosis, such as the possible differences between specific acidosis-inducing agents and insufficiency of physiological pH restoration to fully reverse the negative impact of acidosis on blood clotting.30,38 These questions call for separate, focused investigations and motivate the development of computational models of blood coagulation processes beyond thrombin generation.

<a id='1a54a041-2389-4c15-a6c1-f0949ded3f2a'></a>

Computational kinetic modeling has recently been described as a "thinking tool" in blood coagulation research.39 The value of this tool lies in its capacity to establish a connection between our mechanistic understanding of thrombus formation and relevant end points that may

<a id='f05a8077-cf35-4c8c-b447-22febebdb689'></a>

reflect pathological conditions. Here, we applied this tool to obtain insights into the effects of acidosis on thrombin generation kinetics in a large group of (virtual) subjects. Our study revealed well-defined patterns that can be tested experimentally. Such experiments will facilitate evaluation of the existing understanding of acidosis and its impact on blood coagulation. The resulting knowledge will contribute to future efforts aimed at therapeutic reversal of the conse- quences of traumatic coagulopathy.

<a id='a51bb25e-0027-4333-8cd5-14056377935d'></a>

### ACKNOWLEDGMENTS
The authors are grateful to the Editor and 2 anonymous reviewers whose comments have helped to improve the paper, and to Dr. Franklin Dexter for his comments and suggestions regarding the statistical methods used in this work.

<a id='cd9e543d-f327-434f-b500-d0bc95e4370b'></a>

**DISCLOSURES**
**Name:** Alexander Y. Mitrophanov, PhD.
**Contribution:** This author designed and conducted the study, analyzed the data, and prepared the manuscript.
**Attestation:** Alexander Y. Mitrophanov approved the final manuscript, attests to the integrity of the original data and the analysis reported in this manuscript, and is the archival author.
**Name:** Frits R. Rosendaal, MD, PhD.
**Contribution:** This author contributed to data collection and analysis.

<a id='901e133f-7f5e-46f5-9f9f-de1da2719339'></a>

<::attestation: Approval and integrity attestation
Approved, attests to integrity
Attestation: Frits R. Rosendaal approved the final manuscript.
Name: Jaques Reifman, PhD.
Contribution: This author designed the study, analyzed the data, and edited the manuscript.
Attestation: Jaques Reifman approved the final manuscript, and attests to the integrity of the original data and the analysis reported in this manuscript.
This manuscript was handled by: Charles W. Hogue, Jr., MD.
Text describing approvals and contributions related to a manuscript, positioned centrally on the page.::>

<a id='6b460577-ad00-4fcf-b44d-d46915d3bd7a'></a>

REFERENCES
1. Eddy VA, Morris JA Jr, Cullinane DC. Hypothermia, coagulopathy, and acidosis. Surg Clin North Am 2000;80:845-54
2. Maani CV, DeSocio PA, Holcomb JB. Coagulopathy in trauma patients: what are the main influence factors? Curr Opin Anaesthesiol 2009;22:255-60
3. Mikhail J. The trauma triad of death: hypothermia, acidosis, and coagulopathy. AACN Clin Issues 1999;10:85-94
4. Rotondo MF, Zonies DH. The damage control sequence and underlying logic. Surg Clin North Am 1997;77:761-77
5. Waters JH, Miller LR, Clack S, Kim JV. Cause of metabolic acidosis in prolonged surgery. Crit Care Med 1999;27:2142-6
6. Brummel-Ziedins K. Models for thrombin generation and risk of disease. J Thromb Haemost 2013;11(suppl 1):212-23
7. Mann KG, Butenas S, Brummel K. The dynamics of thrombin formation. Arterioscler Thromb Vasc Biol 2003;23:17-25
8. Engström M, Schött U, Romner B, Reinstrup P. Acidosis impairs the coagulation: a thromboelastographic study. J Trauma 2006;61:624-8
9. Martini WZ, Pusateri AE, Uscilowicz JM, Delgado AV, Holcomb JB. Independent contributions of hypothermia and acidosis to coagulopathy in swine. J Trauma 2005;58:1002-9
10. Ramaker AJ, Meyer P, van der Meer J, Struys MM, Lisman T, van Oeveren W, Hendriks HG. Effects of acidosis, alkalosis, hyperthermia and hypothermia on haemostasis: results of point-of-care testing with the thromboelastography analyser. Blood Coagul Fibrinolysis 2009;20:436-9
11. D'Angelo MR, Dutton RP. Management of trauma-induced coagulopathy: trends and practices. AANA J 2010;78:35-40
12. Dirkmann D, Hanke AA, Görlinger K, Peters J. Hypothermia and acidosis synergistically impair coagulation in human whole blood. Anesth Analg 2008;106:1627-32

<a id='38624b44-46b6-41d2-8eaa-12493b43b4a8'></a>

August 2015 • Volume 121 • Number 2

<a id='6c5456b5-4919-48d9-8b29-3d7760b62a37'></a>

www.anesthesia-analgesia.org

<a id='1cb73431-819b-4689-a522-de1f0ed6f508'></a>

287

<!-- PAGE BREAK -->

<a id='ff272f64-bf81-4e09-915d-aa48605f0a49'></a>

Effects of Acidosis on Thrombin Generation

<a id='e97cd37e-bb2e-4dfc-b389-d74802f814bc'></a>

13. Meng ZH, Wolberg AS, Monroe DM 3rd, Hoffman M. The effect of temperature and pH on the activity of factor VIIa: implications for the efficacy of high-dose factor VIIa in hypothermic and acidotic patients. J Trauma 2003;55:886-91
14. Diamond SL. Systems biology of coagulation. J Thromb Haemost 2013;11(suppl 1):224-32
15. Mitrophanov AY, Rosendaal FR, Reifman J. Therapeutic correction of thrombin generation in dilution-induced coagulopathy: computational analysis based on a data set of healthy subjects. J Trauma Acute Care Surg 2012;73:S95-S102
16. Mitrophanov AY, Rosendaal FR, Reifman J. Computational analysis of intersubject variability and thrombin generation in dilutional coagulopathy. Transfusion 2012;52:2475-86
17. Mitrophanov AY, Rosendaal FR, Reifman J. Computational analysis of the effects of reduced temperature on thrombin generation: the contributions of hypothermia to coagulopathy. Anesth Analg 2013;117:565-74
18. Mitrophanov AY, Reifman J. Kinetic modeling sheds light on the mode of action of recombinant factor VIIa on thrombin generation. Thromb Res 2011;128:381-90
19. Danforth CM, Orfeo T, Mann KG, Brummel-Ziedins KE, Everse SJ. The impact of uncertainty in a blood coagulation model. Math Med Biol 2009;26:323-36
20. Hockin MF, Jones KC, Everse SJ, Mann KG. A model for the stoichiometric regulation of blood coagulation. J Biol Chem 2002;277:18322-33
21. van der Meer FJ, Koster T, Vandenbroucke JP, Briët E, Rosendaal FR. The Leiden Thrombophilia Study (LETS). Thromb Haemost 1997;78:631-5
22. Bender ML, Clement GE, Kézdy FJ, Heck H D'A. The correlation of the pH (pD) dependence and the stepwise mechanism of a-chymotrypsin-catalyzed reactions. J Am Chem Soc 1964;86:3680-90
23. Brocklehurst K, Dixon HB. PH-dependence of the steady-state rate of a two-step enzymic reaction. Biochem J 1976;155:61-70
24. Tijskens LM, Greiner R, Biekman ES, Konietzny U. Modeling the effect of temperature and pH on activity of enzymes: the case of phytases. Biotechnol Bioeng 2001;72:323-30
25. Jarque CM, Bera AK. A test for normality of observations and regression residuals. Internat Statist Rev 1987;55:163-72

<a id='1c87a16c-3de9-4fe4-961e-7ffd4d9aafa5'></a>

26. Glantz SA. Primer of Biostatistics. 6th ed. New York: McGraw-
Hill, 2005
27. Cai TT. One-sided confidence intervals in discrete distributions.
J Statist Plan Infer 2005;131:63–88
28. Kailath T. The divergence and Bhattacharyya distance mea-
sures in signal detection. IEEE Transact Comm Technol
1967;15:52–60
29. Conover WJ. Practical Nonparametric Statistics. 3rd ed. India:
Wiley, 2006
30. Darlington DN, Kheirabadi BS, Delgado AV, Scherer MR,
Martini WZ, Dubick MA. Coagulation changes to systemic
acidosis and bicarbonate correction in swine. J Trauma
2011;71:1271–7
31. Darlington DN, Kheirabadi BS, Scherer MR, Martini WZ,
Dubick MA. Acidosis and correction of acidosis does not affect
rFVIIa function in swine. Int J Burns Trauma 2012;2:145–57
32. Bladbjerg EM, Jespersen J. Activity of recombinant factor VIIa
under different conditions in vitro: effect of temperature, pH,
and haemodilution. Blood Coagul Fibrinolysis 2008;19:369–74
33. Dargaud Y, Wolberg AS, Luddington R, Regnault V, Spronk H,
Baglin T, Lecompte T, Ten Cate H, Negrier C. Evaluation of a
standardized protocol for thrombin generation measurement
using the calibrated automated thrombogram: an international
multicentre study. Thromb Res 2012;130:929–34
34. Ten Cate H. Thrombin generation in clinical conditions. Thromb
Res 2012;129:367–70
35. Aleshnick M, Orfeo T, Brummel-Ziedins K, Gissel M, Mann K.
Interchangeability of rotational elastographic instruments and
reagents. J Trauma Acute Care Surg 2014;76:107–13
36. Sankarankutty A, Nascimento B, Teodoro da Luz L, Rizoli
S. TEG® and ROTEM® in trauma: similar test but different
results? World J Emerg Surg 2012;7(suppl 1):S3
37. Brummel-Ziedins KE, Everse SJ, Mann KG, Orfeo T. Modeling
thrombin generation: plasma composition based approach.
J Thromb Thrombolysis 2014;37:32–44
38. Martini WZ, Dubick MA, Pusateri AE, Park MS, Ryan KL,
Holcomb JB. Does bicarbonate correct coagulation function
impaired by acidosis in swine? J Trauma 2006;61:99–106
39. Mann KG. Is there value in kinetic modeling of thrombin gen-
eration? Yes. J Thromb Haemost 2012;10:1463–9

<a id='d3de5637-b983-48e5-93c4-e09a352d850a'></a>

288

<a id='8745fbcb-dcb0-4e4b-a61d-2ba946e62f25'></a>

www.anesthesia-analgesia.org

<a id='bb5a4db3-1066-4d2c-b81d-fdd2d26fa9a3'></a>

ANESTHESIA & ANALGESIA

# Supplementary materials

<a id='05d1d851-35ce-4bef-a007-29974ff21961'></a>

Supplemental Digital Content

<a id='f8cac1be-5eb6-49a5-98cb-63357d42f2a1'></a>

"Mechanistic Modeling of the Effects of Acidosis on Thrombin Generation"
by Alexander Y. Mitrophanov, Frits R. Rosendaal, and Jaques Reifman

<a id='384ba26d-be67-4ac2-9ba3-bdc5e4660aa1'></a>

Supplemental Methods: Computational Modeling

<a id='d3da4761-9257-4042-b660-89b98ed15413'></a>

*General Comments*

In our simulations, we used an updated version¹ of the Hockin–Mann model² of thrombin generation implemented in the SimBiology toolbox of the MATLAB software suite. The general modeling methodology followed our previously published work; the model equations were solved using the SUNDIALS solver in SimBiology.³–⁵ Note that the quantitative parameters of thrombin and TAT generation were calculated from the raw-output trajectories (to preserve numerical accuracy), i.e., before the discretization of the 80-min simulation time interval and the raw-output trajectories into 800 evenly-spaced points for group trajectory analyses (see Methods in the main text). The discretization of the raw-output trajectories was performed using the MATLAB function SPLINE.

<a id='8a1e38fb-468e-4838-8482-ac2be3b9e0cb'></a>

*The Full pH-Dependence Simulation Strategy*

Our full pH-dependence simulation strategy relied on pH factor randomization (see Methods in the main text), because pH factors can be different for different coagulation enzymes⁶ and are unknown for the vast majority. Our pH factor randomization strategy was similar to our recently developed strategy to model the temperature dependence of thrombin generation kinetics.⁵ For each considered acidotic pH level, each pH factor value was sampled independently and uniformly from the corresponding pH-dependent interval (shown in Fig. 1).

<a id='091d2ddb-7d03-493f-a80e-7e24db4c7264'></a>

In our recently developed strategy to model temperature dependence of thrombin generation, the unknown reaction-specific, temperature-independent parameters (termed temperature coefficients) defining the rates of temperature dependence for kinetic constants were sampled randomly from the interval (2–3) (Ref. 5). This choice of sampling interval was deemed reasonable because this interval is often referred to as the typical interval for temperature coefficients characterizing biological processes and biochemical reactions. 7–9 For the pH-dependent pH factors, however, such general localization information is unavailable. This motivated our decision to estimate pH factors from the measurements for extrinsic tenase and prothrombinase reported in Meng et al. 6 [The measurements reported in that work for the enzymatic activity of free factor factor VIIa were not used because this activity is not reflected in the Hockin–Mann model.1,2]

<a id='716ff5af-3cf0-4aa0-89d4-387314e12ac7'></a>

The pH dependence data in Meng et al.⁶ were obtained at room temperature (Dr. Maureanne

<a id='77256b91-c92a-4bc4-9777-39cac33191e6'></a>

1

<!-- PAGE BREAK -->

<a id='3f8eb040-08cb-4a13-9096-7469dc7a7545'></a>

Hoffman, private communication). However, those results could still be used in our modeling (which reflects biochemical processes at body temperature, 37 °C) because catalytic rates for enzymatic reactions depend on temperature and pH in a multiplicative way. This can be expressed as follows: R(T, pH) = k₁(T)*k₂(pH), where R is a rate that depends on temperature (T) and pH, k₁(T) and k₂(pH) are the functions that define the multiplicative dependence, and k₂(pH) only weakly depends on temperature.10 Therefore, R(T, pH)/R(T, 7.4) = k₂(pH)/k₂(7.4) and this implies that pH factors, which are ratios of catalytic rates at different pH levels, are approximately independent of temperature.

<a id='84906332-4a54-4328-bdbe-c6ee6188838a'></a>

We assume that the "real" pH factors for all catalytic rates in the model lie near the values for extrinsic tenase and prothrombinase (Fig. 1). This assumption is based on the observation that all the blood coagulation enzymes belong to the class of chymotrypsin-like serine proteases, which demonstrate a considerable similarity in their catalytic center structure and catalytic mechanism.¹¹ Yet, to account for possible variability, our pH factor sampling domain was obtained by increasing by 100% the distance between the fitted curves for the extrinsic tenase and prothrombinase data (i.e., for each considered pH level, we moved the top and bottom points up and down, respectively, by 50% of the distance between them; see Fig. 1).

<a id='63ef9ff7-1918-4029-911b-f082cc3ef0ca'></a>

To reflect pH-dependent effects in our model, we performed pH factor adjustment to the kinetic constants with the following indices (see Table S1 below for the specific reactions each of those constants controls): 5, 6, 7, 10, 15, 16, 17, 22, 26, 31, 32, 43, and 44. All these kinetic constants represent catalytic rates of enzymatic reactions. Note that we randomized the catalytic rates for extrinsic tenase acting on factor X (kinetic constant index 10) and prothrombinase (kinetic constant indices 31 and 32) despite the availability of data for those enzymatic reactions (Fig. 1). This was done in order to ascertain consistent and uniform pH modulation of all catalytic rates in our simulation strategy. Indeed, the current version of our computational strategy does not take into account localization information for individual pH factor values; it only uses the information (or assumption) that they lie within the selected sampling interval.

<a id='5c5f3cb1-1b1c-442b-b5a2-5958ccc410d3'></a>

Our choice of pH factor sampling interval width (Fig. 1, dashed lines) can be justified as follows. First, for every considered pH level, we wanted to define a contiguous sampling interval that contains pH factor values for both extrinsic tenase and prothrombinase (Fig. 1, solid lines). Second, in the absence of contradicting evidence (and guided by the Maximum Entropy Principle, as in our work on modeling the effects of hypothermia⁵), we assumed that the sampling distribution should be uniform and that the pH factor of a random coagulation protease would be equally likely to fall inside or outside of the interval defined by the measurements for extrinsic tenase and prothrombinase. Our definition of pH factor sampling intervals satisfies all these requirements.

<a id='34357338-c49e-41d1-83ac-12737d9ec5dc'></a>

The Reduced pH-Dependence Simulation Strategy

<a id='087449d0-ca42-44a0-958e-92ec7b43f5dd'></a>

Our reduced pH-dependence simulation strategy relied on the use of one specified pH factor value for all the catalytic rate constants in the model and did not involve pH factor

<a id='e23e89b0-684b-4fe3-b0a3-a69590678afc'></a>

2

<!-- PAGE BREAK -->

<a id='4b0c58f9-2cd2-46ab-9bce-356e94346f1f'></a>

randomization. The specific definition of the pH factor values in this strategy depended on what type of estimation was intended. When, for a given acidotic pH level, the reduced strategy was intended to estimate the *median* value of a sample generated by pH factor randomization (such as a thrombin generation parameter sample generated using the full simulation strategy, see Fig. 4, red circles), then all pH factors were assigned the value equal to the middle of the pH factor sampling interval for that pH level (Fig. 1). Note that this middle value in fact corresponds to the median of the pH factor sampling distribution, because this distribution is uniform. When the reduced strategy was used to estimate the 1^st^ and 3^rd^ *quartiles* of a sample generated by pH factor randomization (Fig. 4, green circles), then the pH factors in the reduced strategy were assigned the values corresponding to the 1^st^ and 3^rd^ quartiles, respectively, of the pH factor sampling distribution. These latter values were equal to the value that is above the lower sampling interval boundary by 25% of the interval length and the value that is below the upper sampling interval boundary by 25% of the interval length, respectively (the pH dependence of these values is shown by solid lines in Fig. 1).

<a id='b3ebc1d7-2884-4b5a-968b-f311b0793071'></a>

3

<!-- PAGE BREAK -->

<a id='93862c24-8e4c-42a3-bf6d-9ef5e0cfbf06'></a>

Table S1. Biochemical reactions represented in the mathematical model of thrombin generation. The reacting biochemical species are blood coagulation factors and their inactive precursors. The numbers in parentheses pointed at by the arrows in the above kinetic schemes designate the kinetic constant indices for those reactions [e.g., A (x) ↔ (y) B denotes the reaction A → B with kinetic constant index y and the reverse reaction with index x]. TF = tissue factor; AT = antithrombin; TFPI = tissue factor pathway inhibitor.

<a id='65e10aed-530d-47f6-86ee-9b009999b6b2'></a>

Biochemical reactions
TF + FVII (1) ↔ (2) TF:FVII
TF + FVIIa (3) ↔ (4) TF:FVIIa
TF:FVIIa + FVII → (5) TF:FVIIa + FVIIa
FXa + FVII → (6) FXa + FVIIa
FIIa + FVII → (7) FIIa + FVIIa
TF:FVIIa + FX (8) ↔ (9) TF:FVIIa:FX → (10) TF:FVIIa:FXa
TF:FVIIa + FXa (11) ↔ (12) TF:FVIIa:FXa
TF:FVIIa + FIX (13) ↔ (14) TF:FVIIa:FIX → (15) TF:FVIIa + FIXa
FXa + FII → (16) FXa + FIIa
FIIa + FVIII → (17) FIIa + FVIIIa
FVIIIa + FIXa (18) ↔ (19) FIXa:FVIIIa
FIXa:FVIIIa + FX (20) ↔ (21) FIXa:FVIIIa:FX → (22) FIXa:FVIIIa + FXa
FVIIIa (23) ↔ (24) FVIIIa1-L + FVIIIa2
FIXa:FVIIIa:FX → (25) FVIIIa1-L + FVIIIa2 + FX + FIXa
FIXa:FVIIIa → (25) FVIIIa1-L + FVIIIa2 + FIXa
FIIa + FV → (26) FIIa + FVa
FXa + FVa (27) ↔ (28) FXa:FVa
FXa:FVa + FII (29) ↔ (30) FXa:FVa:FII → (31) FXa:FVa + mFIIa
mFIIa + FXa:FVa → (32) FIIa + FXa:FVa
FXa + TFPI (33) ↔ (34) FXa:TFPI
TF:FVIIa:FXa + TFPI (35) ↔ (36) TF:FVIIa:FXa:TFPI
TF:FVIIa + FXa:TFPI → (37) TF:FVIIa:FXa:TFPI
FXa + AT → (38) FXa:AT
mFIIa + AT → (39) mFIIa:AT
FIXa + AT → (40) FIXa:AT
FIIa + AT → (41) FIIa:AT
TF:FVIIa + AT → (42) TF:FVIIa:AT
FIXa + FX → (43) FIXa + FXa
mFIIa + FV → (44) mFIIa + FVa

<a id='21a632a0-ffa7-4b75-a256-e1573bb80f2c'></a>

4

<!-- PAGE BREAK -->

<a id='ac92ddd4-b786-472e-9f24-a6514c314db0'></a>

References

1. Danforth CM, Orfeo T, Mann KG, Brummel-Ziedins KE, Everse SJ. The impact of uncertainty in a blood coagulation model. Math Med Biol 2009; 26:323-36.
2. Hockin MF, Jones KC, Everse SJ, Mann KG. A model for the stoichiometric regulation of blood coagulation. J Biol Chem 2002; 277:18322-33.
3. Mitrophanov AY, Reifman J. Kinetic modeling sheds light on the mode of action of recombinant factor VIIa on thrombin generation. Thromb Res 2011; 128:381-90.
4. Mitrophanov AY, Rosendaal FR, Reifman J. Computational analysis of intersubject variability and thrombin generation in dilutional coagulopathy. Transfusion 2012; 52:2475-86.
5. Mitrophanov AY, Rosendaal FR, Reifman J. Computational analysis of the effects of reduced temperature on thrombin generation: the contributions of hypothermia to coagulopathy. Anesth Analg 2013; 117:565-74.
6. Meng ZH, Wolberg AS, Monroe DM, 3rd, Hoffman M. The effect of temperature and pH on the activity of factor VIIa: implications for the efficacy of high-dose factor VIIa in hypothermic and acidotic patients. J Trauma 2003; 55:886-91.
7. Ahlgren G. Temperature functions in biology and their application to algal growth constants. Oikos 1987; 49:177-90.
8. DeAngelis DL. Strategies and difficulties of applying models to aquatic populations and food webs. Ecol Modell 1988; 43:57-73.
9. Reyes BA, Pendergast JS, Yamazaki S. Mammalian peripheral circadian oscillators are temperature compensated. J Biol Rhythms 2008; 23:95-8.
10. Tijskens LM, Greiner R, Biekman ES, Konietzny U. Modeling the effect of temperature and pH on activity of enzymes: the case of phytases. Biotechnol Bioeng 2001; 72:323-30.
11. Hedstrom L. Serine protease mechanism and specificity. Chem Rev 2002; 102:4501-24.

<a id='a7149e8a-446e-4a8e-a18a-61c2c982a3c7'></a>

5
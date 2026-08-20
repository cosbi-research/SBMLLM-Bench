<a id='64bfda04-8e52-4542-b09c-08eb0b50b98b'></a>

Boada et al. BMC Systems Biology (2016) 10:27
DOI 10.1186/s12918-016-0269-0

<a id='9e97b463-c2b2-47ff-bd83-732169e3387a'></a>

BMC Systems Biology

<a id='3c51a94b-b2d5-425e-970f-1ed5b909e14e'></a>

RESEARCH ARTICLE                                        Open Access

<a id='3998d26e-3efa-4f13-a6e7-51701b8d4a81'></a>

Multi-objective optimization framework
to obtain model-based guidelines for tuning
biological synthetic devices: an adaptive
network case
CrossMark

<a id='1c32acd8-88e1-4142-8458-636fc70e37a1'></a>

Yadira Boada¹, Gilberto Reynoso-Meza², Jesús Picó¹ and Alejandro Vignoni¹,³* [ID icon]

<a id='91319001-2a66-4099-b4bb-33cee5124d14'></a>

## Abstract

**Background:** Model based design plays a fundamental role in synthetic biology. Exploiting modularity, i.e. using biological parts and interconnecting them to build new and more complex biological circuits is one of the key issues. In this context, mathematical models have been used to generate predictions of the behavior of the designed device. Designers not only want the ability to predict the circuit behavior once all its components have been determined, but also to help on the design and selection of its biological parts, i.e. to provide guidelines for the experimental implementation. This is tantamount to obtaining proper values of the model parameters, for the circuit behavior results from the interplay between model structure and parameters tuning. However, determining crisp values for parameters of the involved parts is not a realistic approach. Uncertainty is ubiquitous to biology, and the characterization of biological parts is not exempt from it. Moreover, the desired dynamical behavior for the designed circuit usually results from a trade-off among several goals to be optimized.

<a id='975fa3f9-593b-4923-94d1-72563154821b'></a>

**Results:** We propose the use of a multi-objective optimization tuning framework to get a model-based set of guidelines for the selection of the kinetic parameters required to build a biological device with desired behavior. The design criteria are encoded in the formulation of the objectives and optimization problem itself. As a result, on the one hand the designer obtains qualitative regions/intervals of values of the circuit parameters giving rise to the predefined circuit behavior; on the other hand, he obtains useful information for its guidance in the implementation process. These parameters are chosen so that they can effectively be tuned at the wet-lab, i.e. they are effective biological tuning knobs. To show the proposed approach, the methodology is applied to the design of a well known biological circuit: a genetic incoherent feed-forward circuit showing adaptive behavior.

<a id='db81a0c3-0b95-4c92-9f1a-2c213688da87'></a>

**Conclusion:** The proposed multi-objective optimization design framework is able to provide effective guidelines to tune biological parameters so as to achieve a desired circuit behavior. Moreover, it is easy to analyze the impact of the context on the synthetic device to be designed. That is, one can analyze how the presence of a downstream load influences the performance of the designed circuit, and take it into account.

<a id='9ad05466-2c35-48ce-9c64-e633302928cf'></a>

**Keywords:** Biological circuits, Dynamic behavior, Multi-objective optimization, Kinetic parameters, Biological tuning knobs

<a id='bb3802cb-5753-4cd4-b9e7-ccaf453fa117'></a>

*Correspondence: vignoni@mpi-cbg.de
1 Institut d'Automàtica i Informàtica Industrial, Universitat Politècnica de
València, Valencia, Spain
3 Present Address: Center for Systems Biology Dresden (CSBD), Max Planck
Institute of Molecular Cell Biology and Genetics, Dresden, Germany
Full list of author information is available at the end of the article

<a id='bb39c94e-c194-44eb-afbd-399349071e4e'></a>

BioMed Central
© 2016 Boada et al. Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated.

<!-- PAGE BREAK -->

<a id='0402b206-13bd-4838-8ffd-3e3373eb7c2c'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='623e7765-1f39-4347-8fc8-9af4fa0f77fa'></a>

Page 2 of 19

<a id='071a46b8-edf5-41f2-bb17-d82e0824e4a4'></a>

## Background
Synthetic Biology is defined as the engineering of biology: the deliberate (re)design and construction of novel biological and biologically based parts, devices and systems to perform new functions for useful purposes [1]. As an engineering discipline, it emphasizes engineering principles and methodology in designing, constructing and characterizing biological systems to be applied in industrial, environmental and other applications. Currently, there still is a disparity between the ability to design systems and the one to synthesize them. This disparity can partly be attributed to a lack of well-characterized parts and methods for reliably and robustly composing parts into devices [2].

<a id='c8c06e12-e0dd-496e-966a-9255e7e2aef0'></a>

From the very beginning of Synthetic Biology, efforts have been made in order to characterize standard bio-logical parts -i.e. DNA sequences encoding a function that can be assembled with other standard parts to form devices [3]. Yet, the roadmap to engineering biological systems is determined not by the biological parts but rather by how they interact [4]. Thus, both precise charac-terization and predictable part composition are essential for the efficient creation of sophisticated genetic circuits [5, 6]. In this context, developing frameworks for func-tional composition is a current challenge, the solution of which will allow biological components to be systemati-cally, reliably, and predictably assembled into a functional device or system [2].

<a id='46a50bff-f82f-4938-b48f-e1413db25209'></a>

The systematic design of complex bio-circuits from libraries of standard parts relies on mathematical models describing the circuit dynamics. In this regard, modular modeling tools facilitate the mathematical representa-tion of biological parts and their combinations, providing the description of the reactions which take place inside the different parts and the interfaces that connect them [7, 8]. Computer-aided (model based) methods and tools can be used to guide the design of synthetic biochemical pathways [9-11].

<a id='ea720f75-3121-4900-b02b-eacf6a383580'></a>

Several problems arise when building up biological devices by combining parts. First, composing different biological parts and devices together can be difficult, even if assuming a synthetic circuit structure has been properly designed to have a pre-specified dynamic behavior, because the desired input and output levels of a module are often unknown, difficult to measure quantitatively, or difficult to compare. Additionally, the ratio part/device performance may be altered due to the interaction of loads in the combined system, the so-called retroactivity [12]. Along with this, there is an ever-growing appreciation for biological complexity, which requires new circuit modeling and design principles to overcome barriers such as metabolic load, cross-talk, resource sharing, and gene expression noise [5, 13–15]. Finally, one must never forget the gap between computational (dry-lab) design,

<a id='bf80e68f-2e0a-4761-a8a8-0433b21ce062'></a>

and _wet-lab_ implementation. In practice, biological parts
are subject to uncertainty. Circuit structure design and
parameters tuning methods must cope with this uncer-
tainty in the biological parts and context to narrow the
gap.

<a id='0f478370-4ded-4f65-bce6-efe31d301944'></a>

To this end, the modular and systematic design of bio-
circuits, i.e. the systematic way of finding combinations
of components from a library of standard parts allow-
ing to optimally perform a pre-defined function, can be
formulated using an optimization framework [16-18].
Indeed, it has been argued that Synthetic Biology is less
like highly modular (or 'switch-like') electrical engineering
and computer science, and more like civil and mechani-
cal engineering in its use of models optimization of whole
system-level stresses and traffic flow [5].

<a id='b909526c-e29b-4625-92f4-3cc4012d71f6'></a>

Advanced optimization-based methods, capable of han-
dling high levels of complexity and multiple design criteria
have been proposed for the modular and systematic struc-
tural design of biocircuits [19]. These new approaches
combine the efficiency of global Mixed Integer Nonlinear
Programming solvers with multi-objective optimization
techniques [20, 21].

<a id='3fde15b1-b9df-4621-84e3-5e9dcf285595'></a>

On the other hand, a natural approach to model-based tuning of synthetic circuits consists of the analysis of the effect of key parameters that can be used as tuning knobs in the experimental implementation. In this approach, selection of biological parts is understood as choice of the range of values of key parameters of the device that yield the desired dynamical behavior. A current challenge is to devise methods to provide the set of circuit parame- ters that satisfies a specified circuit behavior in a way that can be readily used for their wet-lab implementation [22]. Thus, for instance, in [23], the authors synthesize reg- ulatory promoter libraries, characterize key parameters, and use them to guideline the construction of synthetic networks with different predicted input-output charac- teristics. Global sensitivity analysis is used in [16]. The sensitivity information is used to guide the selection of circuit components and thereby reduce the wet-lab imple- mentation effort. In [24] the authors express the desired behavior as a functional cost index of the desired circuit trajectories. Then, the inverse sensitivity of the mapping between parameters and cost index is obtained after lin- earising the functional cost index around an initial value of the model parameters. This local inverse mapping is used to map a region of specifications into a one of parameters.

<a id='7f04694d-ddc7-429b-a199-738240a6c2dd'></a>

Although the specification of the desired dynamic of the circuit is most often naturally expressed as a multi-objective global optimization problem, this approach has not been used so far. Instead, current approaches define independent thresholds set a priori for each of the functional goals characterizing the desired behavior of the circuit. Then, global Monte Carlo-like approaches are used,

<!-- PAGE BREAK -->

<a id='122d0fe5-ac1a-4d66-bba6-90984be3f8ab'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='54dc26ce-6016-40b4-870e-565f58cd1173'></a>

Page 3 of 19

<a id='5add6748-1112-4598-9124-5a6ae061ada7'></a>

sampling the parameters space and simulating the circuit
time response. The result of these simulations is used to
assess the circuit behavior, so as to profile the subset of the
parameters space that result in circuit behavior fulfilling
all thresholds. After this, some statistical post-treatment
of the results is used, like clustering or correlation anal-
ysis or global sensitivity analysis, to draw conclusions
between the distribution of the parameters, and the cir-
cuit behavior [25]. This Monte Carlo based approach has
a huge computational cost. Given a defined search space
in the parameters space, the Monte Carlo sampling does
not ensure that a solution will be found, thus requiring a
large number of samples to find solutions. This problem
increases as the thresholds defining the acceptable cir-
cuit behavior are more stringent. On the other hand, the
solution space obtained weighs, either equally or ad hoc,
all the functional goals of the circuit. Thus, besides miss-
ing many possible optimal solutions, there may be little
variability among the different solutions in the param-
eters space, making the statistical post-treatment less
sensitive.

<a id='a62f4134-3d59-47ec-b666-d8d8ec1aacf1'></a>

Feed-forward circuits have been used within this con-text as an important case-study. In [26] all three-node possible network topologies that present adaptive dynam-ical behavior are analyzed using function-topology maps based on Monte Carlo sampling in the parameters space. Using a simple enzymatic model, the authors draw design principles of adaptation circuits. They show that there are only two core solutions that achieve robust adaptation: negative feedback loops and incoherent feed-forward ones. In [27], the incoherent feed-forward adap-tive enzyme network structure derived in [26], is used as case study. A method is proposed to make inferences on the contribution of individual parameters to specific components of the system. Classes of kinetic parameters are obtained that may correspond to varying strengths of enzymatic reactions that can be measured and classified experimentally. The authors show that, for a given net-work structure, certain types of values, or motifs, also exist for kinetic parameters in order to achieve specific system dynamics. Clustering in the parameters space to detect kinetic motifs, i.e. sets of parameters yielding desired circuit dynamics, is used in [25].

<a id='79337681-78ea-4958-923a-7a9dcd23614c'></a>

In this paper, to build a given functional device with
desired dynamic behavior, we study the application of a
multi-objective optimization design (MOOD) framework
[28] to obtain a model-based set of guidelines for the
selection of its biological parts. In MOOD all objectives
are important, so all of them are optimized simultane-
ously. Thus, the solution rarely is unique, but a set of
solutions called the _Pareto Front_. In this sense all solu-
tions are Pareto-optimal and differ from each other in the
trade-off of objectives that each one represents. Then, the
design reduces to encode carefully the desired dynamics

<a id='271eb14c-75d8-4e7d-9fdc-a452abfc2dbf'></a>

into the objectives and optimization problem itself in
the MOOD [28]. As a result, the designer obtains qual-
itative regions/intervals of parameters along the Pareto
Front giving rise to the predefined behavior of the circuit.
Contrarily to the passive search for solutions of Monte
Carlo-based approaches, the multi-objective optimization
approach actively searches for all the optimal solutions as
a first step. The MOOD framework also naturally provides
a classification of the parameters along the Pareto front, by
taking into account their effect on each of the goals. More-
over, this framework makes easy to analyze the impact of
context on the synthetic devices to be designed. This can
be done by just incorporating information about the rela-
tionship between the device and the context. In general,
this means we only need to know where do we connect the
device which is being designed and how we are connecting
it. Including this information in the optimization problem,
we obtain a qualitative region of parameters taking into
account the effect of the context on the device.

<a id='c3099e56-409a-43f6-bd2e-d50c493eea4d'></a>

The remaining of the paper is organized as follows. In Methods, the general framework, and the type-1 incoherent feed-forward (I1-FFL) circuit that will be used as case study, are presented. Next, in Results, the proposed methodology is applied to the I1-FFL case study, and the main findings for the circuit are described. Two typical application scenarios of the methodology are also considered. Finally, some discussion and general conclusions, both on the methodology and its results on the I1-FFL case study are drawn in Discussion and Conclusion sections.

<a id='df100818-1fe7-4218-8885-fc7a0a5e7e30'></a>

# Methods
## Multi-objective optimization design framework
### *General workflow*
Achieving a synthetic biological circuit fulfilling some behavioral specifications requires in practice an iterative process through three main steps: choosing a circuit structure capable to perform the desired behavior after the proper tuning of its parameters, tuning the circuit parameters, and validating the circuit with the selected tuned components. The use of models to solve the first two subproblems *in silico*, before attempting the wet-lab implementation to validate the circuit, reduces the wet-lab effort and speeds-up the design process. This work focuses on the second subproblem: *in silico* tuning of the circuit model parameters, so as to achieve the desired behavioral specifications.

<a id='f3e1cbfc-86f5-4098-b550-d733194dbf8e'></a>

First, a topology for the functional module or circuit is needed, capable to perform the desired behavior after the proper tuning of its parameters. This will provide the circuit model structure. Although currently there are no *catalogues* as such for functional modules, there is a vast literature in the systems biology area on network motifs producing a variety of dynamic behaviors [29].

<!-- PAGE BREAK -->

<a id='b7ca2532-48ea-497f-a90e-28fbe4095530'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='81360a9f-8ec4-4634-9e49-e28382643947'></a>

Page 4 of 19

<a id='f068c1e5-be4d-4cef-88ba-b16a007cbbaa'></a>

Much work has also been done and is on-going on the design of circuits with various capabilities: repressilators [30], biomolecular concentration trackers [31], feedback regulation circuits [32], switchable genetic oscillators [33], etc. Many of the functional circuits that are being implemented in synthetic biology take advantage from well-established work in areas such as electronics and feedback control for the design of bistables, feedback and feedforward structures, switches, etc; see, for example, [26, 29, 34-39] and the references therein. Alternatively, one may find the potential circuit structure casting the problem as an optimization one, starting from coarse-grained models of the potential circuit structural components, and looking for the optimal circuit topology [19].

<a id='b304f1fe-f4f7-4016-b45f-c25ee4d056df'></a>

Models may have different degrees of detail. Our goal is to tune the model parameters using a degree of detail in the model amenable to serve as basis to provide guide-lines for the experimental implementation of the circuit. That is, the parameters to be tuned should correspond to biological tuning knobs that can be modified experimen-tally [40]. Mass action kinetic models obtained from the set of biochemical reactions will be used for this purpose. These models can be reduced using singular perturbation methods (the so-called _quasi-steady state approximation_, QSSA) by neglecting the dynamics associated to fast bind-ing reactions - e.g. RNA polymerase binding to DNA- and by taking into account the algebraic relationships among species resulting from conserved moieties [41]. The reduction process can be performed so that both the species in the reduced model are a subset of the original one [42, 43], and that the resulting aggregated parameters have a clear matching with experimental biological tuning knobs [44].

<a id='e082a362-a272-43b1-a59d-08d40912863b'></a>

From this starting point, we can proceed to tune the
model parameters so that eventually the circuit fulfills
the behavioral specifications. We will consider the general

<a id='911f132d-f11f-44c7-af68-9f21f66df988'></a>

case when a set of specifications is desired, thus leading to a multi-objective problem. A usual approach to face a multi-objective problem consists of building an aggre- gate function in order to assemble the design objectives in a unique index, normally by means of a weighting vector. This approach is followed for example in [25]. However, the solution obtained depends too much on the correct selection of the weighting factors, and it might not possibly reflect with enough clarity the designer's preferences in relation with the desired balance of require- ments. An alternative option is to use multi-objective optimization [45]. This is a natural choice to face this kind of problems. In multi-objective optimization all design objectives are important to the designer, so all of them are optimized simultaneously. Thus, the solution rarely is unique, but a set of solutions called the _Pareto Front_. In this sense all solutions are Pareto-optimal and differ from each other in the trade-off of objectives each one represents.

<a id='b996ce83-535c-415b-a2e5-14e07838f800'></a>

In order to successfully implement the multi-objective
optimization approach, at least three fundamental steps
are required [46], as depiced in figure depicted in Fig. 1:

1. the multi-objective problem (MOP) definition:
defining the circuit behavioral specifications in a
proper way.
2. the optimization process: tuning the parameters
using multi-objective global optimization (MOO).
3. and the multi-criteria decision making (MCDM)
stage: obtaining tuning guidelines useful for the
wet-lab implementation.

<a id='5380ec90-6ea2-45e1-8901-8c6e184bcf94'></a>

This overall multi-objective optimization design
(MOOD) procedure enables to analyze design objectives
trade-offs to implement a preferable solution [28]. Fur-
thermore, it may provide a better understanding of the
problem at hand by the so called process of _innovization_

<a id='bc756fe1-9fbd-4e79-88d0-85d950963d35'></a>

<::flowchart: Multi-objective Optimization Design (MOOD) Procedure::>
<::flowchart-step::>
<::flowchart-box: Multi-objective Problem (MOP) Definition::>
<::chart: A 2D plot with y-axis J2(θ) and x-axis J1(θ). A downward-sloping curve represents a trade-off.::>
<::flowchart-box: Defining meaningful design objectives::>
<::flowchart-connector: Circular arrow indicating flow to the next step::>
<::flowchart-step::>
<::flowchart-box: Multi-objective Optimization Process::>
<::chart: A 2D plot with y-axis J2(θ) and x-axis J1(θ). Multiple diamond-shaped points are scattered, with arrows pointing towards a downward-sloping curve, indicating optimization towards a Pareto front.::>
<::flowchart-box: Optimization with pertinency improvement::>
<::flowchart-connector: Circular arrow indicating flow to the next step::>
<::flowchart-step::>
<::flowchart-box: Multi-criteria Decision Making (MCDM) Step::>
<::chart: A 3D scatter plot with axes J3(θ), J2(θ), and J1(θ). Red points are scattered, and a subset of blue points forms a surface, representing a Pareto front.::>
<::flowchart-box: Multi-criteria analysis to develop design guidelines::>
<::caption: Fig. 1 Steps for the multi-objective optimization design procedure::>


<!-- PAGE BREAK -->

<a id='4d2cbbec-0e49-40be-8375-925da7fcb418'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='c524403d-4d86-4a8c-b117-4547b6d21b2d'></a>

Page 5 of 19

<a id='e5993e0c-ae2b-41c3-9f16-7bf686f72de1'></a>

through optimization as stated by [47]. Next we describe
each of the steps in detail.

<a id='24cf7db2-ed9d-467c-a989-88bd1e68d71b'></a>

_Defining the circuit behavioral specifications_
The starting point of the proposed methodology is the multi-objective problem definition, that is the specification of the desired dynamical behavior for the circuit to be designed. This can be done in several ways. From the designer's point of view, specifying the circuit behavior in terms of the desired output signal profile for a given input signal profile is a natural approach [48]. The input signal is chosen as the one that is going to be used in working conditions, or as simple standard probing input-signals (e.g. step-like, sinusoidal, or pulse ones). Once the desired input-output relationship is defined, the set of circuit parameters achieving it can be obtained by optimization-based system identification [20]. This approach is useful for linear dynamical systems, as their time-response to these probing signals fully characterizes the circuit dynamical behavior. This is not the case for nonlinear circuits as the ones typically encountered in synthetic biology. Thus, the particular signal to be used in working conditions should be chosen. Yet, this may be very restrictive. Indeed, usually the input signal to a circuit will have varying characteristics. In the best case, it will belong to a given class (e.g. step-like signal with varying amplitude). Therefore, the dynamical behavior, i.e. the desired circuit time-response to a given input signal, is better given as a set of input-output performance indexes to be optimized.

<a id='7aaaca42-78bb-47c7-8c99-be64290f2272'></a>

Specifying the desired circuit behavior in terms of per-
formance indexes to be optimized has many advantages.
In the general case, the indexes will take the form of func-
tionals mapping the circuit trajectories to the reals. Thus,
consider a circuit with dynamics given by the model:

<a id='5124b937-0f38-4bd0-b5ae-5954950049d0'></a>

ẋ = f(x, θ)
0 = g(x, θ)

                               (1)

<a id='2f3bfa96-131c-406c-8880-24d8f07a649d'></a>

where $x \in \mathbb{R}^n$ is the state, $\theta \in \mathbb{R}^p$ the parameters, and function $g(.)$ represents algebraic constraints in the system. The indexes can be expressed as:

<a id='4208b37b-ef87-4537-99f7-a3f8ccec72a3'></a>

J_i(\theta) = \int_{t_0}^{t_f} h(x(\tau, \theta), \tau)d\tau                                                              (2)

<a id='ea103c1a-8139-44e8-880a-805282650024'></a>

for some possibly time-dependent function _h_ (.) of the sys-
tem trajectories during a time interval of interest [_t_₀, _t_f],
being _i_ = 1..._n_i is the number of indexes. These can be
made valid for a whole class of input signals, may consider
other signals in the circuit besides the input and output
ones, robustness with respect to uncertainty in the cir-
cuit parameters can be included, etc. They will typically
consider the desired performance at steady state (preci-
sion), and some measure of the quality of the transient.
Proper definition of the optimization indexes representing

<a id='0b8b7bc2-88b0-4aff-a7e3-a4452aec6641'></a>

the desired behavior is a key point. An incorrectly speci-
fied objective, not properly representing the actual desired
behavior, will lead the optimization in a wrong direc-
tion, returning a parameter set that will give misleading
design guidelines. Moreover, for the proper interpreta-
tion of results by the designer, one must pose meaningful
design objectives.

<a id='695ef145-7ebd-4db3-a615-1797f98a8b8c'></a>

**Multi-objective parameters tuning**
As mentioned above, representing the desired behavior
will eventually lead to several objectives to be optimized.
That is, the optimization problem will be a multi-objective
one in the general case. Typically, some of the objec-
tives will be in conflict, so a trade off among solutions
is required. Ad hoc weighting of the different objectives
may be used to transform the problem into a single-
objective one [49]. Alternatively, thresholds on each of
the objectives may be set in order to run multiple times
a single-objective optimization. Instead, we address the
problem as a truly multi-objective optimization design
(MOOD) one.

<a id='b02f7d46-8808-4a90-910b-1d5ac9c37dac'></a>

The multi-objective optimization (MOO) process seeks to approximate the best parameters $\theta_p^*$ that give the best Pareto-front approximation $J_p^*$ [45]. Such search could be done through a random Monte-Carlo sampling in the decision variables space $\theta$ —the set of parameters determining our biological model—, followed by a filtering of the solutions in order to obtain the $\theta_p^*$ that defines the Pareto front approximation $J_p^*$. This could be a good option for problems with few decision variables. For problems with a large number of decision variables, as our case, it is more efficient to use an appropriate multi-objective optimization algorithm to approximate this solution.

<a id='8b4fd70b-6328-434b-a187-a67abac56d62'></a>

We obtain the Pareto-optimal front of solutions via spMODE, a multi-objective optimization algorithm based on differential evolution [50, 51] implemented in Matlab, and available at Matlab Central¹. The algorithm spMODE actively searches for all the solutions in the parameter space along the Pareto front. It:
* improves convergence by using an external file to store solutions and include them in the evolutionary process;
* improves spreading by using the spherical pruning mechanism [50];
* improves pertinency of solutions, i.e. getting interesting solutions from the designer's point of view, by means of a basic bound mechanism in the objective space, as described in [52].

<a id='b8963b01-07a7-4c63-8d00-d2be8aa0dc5d'></a>

_**Obtaining tuning guidelines for implementation**_
After the multi-objective optimization, a set of solutions
is obtained: values for the kinetic parameters that repre-
sent a trade-off between the objectives. Then, the final

<!-- PAGE BREAK -->

<a id='217a9536-9ddb-445c-8170-48440338f51a'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='be325d86-03ba-4fb2-b1e2-f373502a1227'></a>

Page 6 of 19

<a id='68043e30-9c2f-45dc-9d62-2d6a31e20664'></a>

step is to obtain tuning guidelines to select the values of the kinetic parameters of the model and correspondingly cues for the implementation of the circuit in the wet-lab. In this work we present two alternatives for this last step: a semi-automated one based on an optimized clustering of the solutions, that is, providing some guidelines; and a second one, in case the implementation needs more insight allowing to learn more about the problem, based on the visualization of the Pareto front and set using suitable tools, thus, providing a guidance with this information.

<a id='32b4bf7a-7a35-4478-9cb0-3ff37646904e'></a>

In the first alternative, qualitative instructions for the wet-lab implementation are extracted from these solu-
tions. The kind of information extracted is in the form of qualitative levels for the kinetic parameters that can be commonly modified in the wet-lab, for instance:

<a id='9a5015ee-37d9-4bc5-a016-4ab1c962daed'></a>

- Plasmid copy number. It can be tuned by selecting the appropriate replication origin of the plasmid.
- Promoter strength. It can be modified by selecting the appropriate promoter with predicted strength; for example from the Anderson Promoter library [53] available at the iGEM Parts Registry.
- Ribosome Binding Site strength. It is one of the easiest parameters to tune in the wet-lab using, for instance, RBS libraries, the RBS Calculator from Sallis Lab [54], or nucleotides repetition [55].
- Protein degradation rate. It can be tuned globally by changing the growth rate of the microorganism. It can also be tuned by adding a protein degradation tag to include the protein in an active degradation pathway.

<a id='7b135a85-2a2f-4521-b0ed-b25204cfd5b3'></a>

In order to facilitate the obtention of the guidelines, a hierarchical clustering is performed with the solutions (also using a Matlab script, see Additional files 1 and 2), including the values of the objectives and also the kinetic parameters of each solution. This process is achieved by using a cluster tree based on the Euclidean distance among the vectors containing the attained values of the objectives for all points along the Pareto front. The distance among clusters is obtained by means of the weighted center of mass distance. Then we set the number of clusters in an iterative manner from ten to two, and in each iteration we perform a Kruskal-Wallis [56] test (which is the non-parametric equivalent of the one-way analysis of variance ANOVA) to study the correlation between the kinetic parameters and the clusters. With this process the optimal number of clusters is selected by choosing the one that maximizes the number of significantly correlated parameters with the clusters. Each one of the resulting correlated parameters has different value ranges in each one of the clusters which represents a guideline for this parameter. For example it can range around low values

<a id='eb9ebd34-074a-4cdd-912b-46d3eb814091'></a>

(with respect to the initial interval for that parameter)
for some clusters and high values for other clusters.
This parameters are particular guidelines for each
cluster.

<a id='f20797e5-208e-4eef-abbd-fa372064a358'></a>

For the parameters that do not exhibit a significative correlation, its optimized range is also checked against the initial interval given to the optimizer. If the ranges are different this means the optimization process found an optimal range for the parameter, but general to all the clusters. This parameters are general guidelines for optimality.

<a id='2efa5032-1f47-4965-a20e-a870831e1e3e'></a>

For the second alternative, it is accepted that visualization techniques are valuable in order to analyze the trade-off among competing objectives. Such visualization and analysis is not a trivial task when the number of objectives is larger than three and/or the number of decision variables in the Pareto set is large, like in our case. Several tools are available, but in any case, some desirable characteristics are useful to perform such analysis. The first of them are concerned with the practical aspects of the analysis:

* It must enable design alternatives comparison (analyze different solutions).
* It must enable design concepts comparison (analyze different Pareto front approximations).

<a id='598511f9-64c9-4f4a-bba5-6591d70fa75c'></a>

Others are related to subjective aspects of the visualization:

* Completeness: all relevant information should be contained in the visualization.
* Persistence: all the relevant information should be retained in the designer's mind.
* Simplicity: the visualization should be easily understandable.

<a id='5dcfe404-8a5c-440e-ba9f-870c17c4d2d8'></a>

In this work we use the visualization tool Level Diagrams (LD) [57, 58], which has a freely available implementation for designers: LD-Tool. LD-Tool allows to correlate design objectives with decision variables. It classifies the calculated optimal parameters *θ*^*_p* with respect to each objective *J_q*(*θ*) normalized with respect to its minimum and maximum value. A graph for each objective is displayed (see Additional file 1: Figure S1), where the Y-axis is the p-norm ||*Ĵ*(*θ*)||*p* of the objectives vector, and the X-axis corresponds to the objective value or decision variable depending on the case. A second graph displays ||*Ĵ*(*θ*)||*p* with respect to each decision variable. These characteristics make it helpful in order to propagate the information from clustering between design objectives space and decision variables space. Thus, a given solution will have the same value -*y* in all graphs. As it is, LD enables the alternative and design concept comparison. In order

<!-- PAGE BREAK -->

<a id='de09eb6d-6265-4242-8a20-b64127ef321c'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='6ed47ad0-cf3b-48b7-bf3e-3f1291198d11'></a>

Page 7 of 19

<a id='3b46009b-b496-418c-94df-814a74458a1e'></a>

to also incorporate the information obtained in the clustering, the y-axis of the LD plot is modified to show the membership of a solution to a cluster, therefore, improving completeness for our problem. And this is coded also in the color of the points in all the graphs, improving persistence and simplicity. This correspondence of colors helps to evaluate general tendencies along the Pareto front and compare solutions according to the clusters they belong to. Additionally, with the aim of improving simplicity and completeness, the dynamic response of species from the model is ploted using the same color code. To sumarize, this step consists in first the clustering of the solutions and then:

<a id='351c78bc-d64a-4b89-98e2-d8e6a8a44358'></a>

*For the guidelines*
Study correlations between the parameters and the clus-
ters and obtain guidelines.
*For the guidance to help manual decision making*
Visualization of the Pareto Front and Pareto Set of the
clustered solutions to obtain more insight and learn about
the specific problem.

<a id='155673fd-8c94-47bd-a0de-27d3c31c72f0'></a>

All this step is performed in matlab scripts (see
Additional files 1 and 2 for a description and the scripts
respectively) ³.

<a id='bbe5a13c-ec64-47cb-9f43-10d3fb7f04be'></a>

Finally, it is interesting to note that the selection of the preferable solution according to designer's criteria, or equivalently the extraction of qualitative levels for the parameters, takes place in an _a-posteriori_ multi-criteria analysis of the Pareto Front approximation, and it is in general computationally cheap in comparison with the multiobjective optimization step.

<a id='76b410f4-8851-4dcc-8c79-d2e9fb2c0f07'></a>

Incoherent type 1 feed-forward loop (I1-FFL)
Adaptation is an important property of biological systems, linked to homeostasis [29], and to the generation of responses that depend on the fold-change in the input signal, and not on its absolute level [59]. It is defined as the particular ability of biological circuits to respond to a change in its input and return to the value it had prior to the stimulus, as depicted in Fig. 2. Due to its relevance, in the paper we will use a genetic circuit showing adaptation to illustrate the proposed approach. Circuit topologies giving rise to adaptive behavior have been extensively studied [29]. Different three-node topologies are possible [26]. Among them, the incoherent type 1 feed-forward loop structure (I1-FFL) is one the most common network motifs. Different implementations are possible, including enzyme reaction networks [26, 27], gene networks [34, 60] and in vitro transcriptional networks [61]. In the gene network case, a protein A acts as a transcription factor and activates expression of two downstream genes B, and C. In turn protein B represses expression of gene C. Figure 3a depicts the genetic synthetic circuit. To introduce a step-like input signal to the circuit, we consider the addition of an external chemical inducer I, that diffuse from the extracellular culture inside the cell. Most of these inducers undergo an heterodimerization, i.e. the inducer binds to one of the circuit species thus effectively providing an input to the circuit. Most of them subsequently dimerize. We have used a model that captures both phenomena. The protein A, product of gene A, bounds to the inducer I, forming a monomer A · I which in turn dimerizes. The dimer (A · I)2 is the transcription factor that activates expression of gene C directly, and represses it indirectly

<a id='290ab9d4-027c-4870-882a-2d75d4050040'></a>

<::figure: Functional module behavior diagram::>Functional module behavior

[Block Diagram]
INPUT Inductor Ie: Green rectangle containing a step function graph with two levels, Ie1 and Ie2.

-> Gene network E. coli bacterium: Pink rectangle labeled "Gene network E. coli bacterium".

-> OUTPUT Protein C with Adaptation: Blue rectangle containing a graph with y-axis labels Opeak, O1, O2, and x-axis label time. The graph shows a signal that rises to Opeak and then adapts back to O2 (which is at the same level as O1).

[Additional Diagrams and Definitions]
Sensitivity: Graph with x-axis labeled "time" and a curve showing a peak followed by a return to baseline, with the label "Precision" below the curve.

Adaptation
SENSITIVITY: value of the peak after the application of the stimulus.
PRECISION: detects if the output returns to its previous value after application of the stimulus.

Fig. 2 Input-output adaptive behavior. Adaptation is an important property of biological systems, related to homeostasis. After an input stimulus the output signal responds by first quickly reaching a peak value, after which it returns to its previous value even if the stimulus persists

<!-- PAGE BREAK -->

<a id='849968a7-f8ed-426c-854b-17ee0cf24c72'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='b5293264-158b-4c11-b598-9f185d3ed0d1'></a>

Page 8 of 19

<a id='04bd7c09-2e5f-4f39-8d74-d926e256513c'></a>

<::Fig. 3 Three-node incoherent type 1 feedforward loop. a Gene gA produces the protein A, which forms a dimer with the inducer I. The dimer activates both genes gC and gB. In turn, the product of gB represses gC. b Representation of a cell incorporating an incoherent feedforward loop synthetic circuit
: diagram::>
<::a. This diagram illustrates the gene regulatory network. A promoter PgA drives the expression of gene gA, which produces protein A. Protein A binds with an inducer I to form a complex AI, which then dimerizes to form (AI)₂. This dimer (AI)₂ activates the promoters PgB and PgC, leading to the expression of genes gB and gC, respectively. Gene gB produces protein B. Protein B, in turn, represses the promoter PgC. Gene gC produces protein C. Arrows indicate activation, and blunt-ended lines indicate repression.
: diagram::>
<::b. This diagram shows the synthetic circuit within a cell, enclosed by a cell membrane. Inducer I (green circles) enters the cell. Inside, gene gA (green arrow labeled gA with promoter PgA) produces protein A (green crescent shapes). Protein A and inducer I combine to form Monomer AI (green crescent with green circle). These monomers then form Dimer (AI)₂ (two green crescents with two green circles). This Dimer (AI)₂ activates (labeled 'activation') both the promoter PgC of gene gC (blue arrow labeled gC) and the promoter PgB of gene gB (orange arrow labeled gB). Gene gB produces protein B (orange shapes). Protein B represses (labeled 'repression') the promoter PgC. Gene gC produces protein C (blue dimeric shapes). All components are depicted within the cell, with the inducer I shown entering from outside the cell membrane.
: diagram::>

<a id='54b16a0a-65b8-4143-a36f-11084675de01'></a>

via activation of the repressor B. As a result, when a sig-
nal causes node A to assume its active conformation, C
is produced, but after some time B accumulates, even-
tually attaining the repression threshold for the gene C
promoter.

<a id='c5327eaf-de56-4c00-8f87-9a9972e31d4c'></a>

We model the designed genetic circuit using a deter-
ministic approach and taking into account the key regu-
latory interactions between the main biochemical species
present in the genetic circuit: proteins _A_, _B_, and _C_, and
inducer _I_. In our gene synthetic circuit (see Fig. 3b), the
circuit comprises a gene gC under the control of the pro-
moter _P_gC. The concentration of protein _C_ is considered
to be the circuit output signal. Expression of _C_ is activated
by the dimer (A·I)$_2$ that acts as transcription factor for the
hybrid promoter _P_gC, and it is repressed by protein _B_. The
dimer (A·I)$_2$ also acts as transcription factor activating
the promoter _P_gB. Protein _A_ is constitutively expressed,
and bounds to the inducer _I_. The inducer can passively
diffuse across the cell membrane. Though the input signal
to the circuit is the intracellular inducer concentration _I_,
the experimental input signal is the external application of
the inducer in the broth _I_e.

<a id='8e50d51e-c39f-4ecc-a411-ac7192a888da'></a>

Starting from a complete model based on mass action kinetics (See Additional file 1, 1.I1-FFL Model) we obtained the reduced deterministic model (3).

<a id='b442329e-8b6a-4840-92a2-6f5882590a98'></a>

ẋ₁ = k_mAC_gA - d_mAx₁
ẋ₂ = k_pAx₁ - d_Ax₂ - k₂x₂x₃ + k₋₂M
ẋ₃ = -k₂x₂x₃ + k₋₂M + k_d(x₉ - x₃) - d_Ix₃
ẋ₄ = k₃M² - k₋₃x₄ - d_AI₂x₄
ẋ₅ = K_mBC_gB \frac{x₄}{γ₁ + x₄} - d_mBx₅
ẋ₆ = k_pBx₅ - d_Bx₆
ẋ₇ = K_mCC_gC \frac{x₄ + β₁γ₄x₆ + β₂γ₅x₄x₆}{γ₂ + γ₃x₄ + γ₄x₆ + γ₅x₄x₆} - d_mCx₇
ẋ₈ = k_pCx₇ - d_Cx₈
ẋ₉ = K_cells k_d(-x₉ + x₃) - d_Iex₉
M = -\frac{d_AI + k₋₂}{4k₃} + \frac{1}{4k₃}\sqrt{(d_AI + k₋₂)² + 8k₃(k₂x₂x₃ + 2k₋₃x₄)}

(3)

<a id='090e7a72-0e71-4524-981f-43914290aa7b'></a>

where M is the monomer concentration, and
K_cells = (V_cell N_cells) / V_medium the volumes relationship required to
take into account the concentration outside the cells.
Note the transport term (x_3 - x_9), depends only on the
difference of the concentrations inside and outside the
cells. The K_cells constant reflects the amount that goes
out (or in, depending on the sign) from all the cells into
the extracellular volume. In the simulations we used
V_cell = 1 x 10^-15 L, which is the typical volume of an E. coli

<!-- PAGE BREAK -->

<a id='6a9fc1be-853f-41c0-9107-3f6b0f1cdbbf'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='c8060c78-34f2-453e-9d8d-2c63c2181ccb'></a>

Page 9 of 19

<a id='df6099de-2385-4b99-a184-474fa4d2fe62'></a>

cell, we considered Ncells = 2.4 × 10⁸ cells/mL * 0.18 mL which is the number of cells in a 180 µL culture with OD = 0.3 placed in a well containing Vmedium = 180μL of culture medium. Table 1 shows the species and their corresponding symbols.

<a id='a059b2e5-9d09-4d02-ab0e-f7e96e65c59c'></a>

Model (3) has nine differential equations plus one algebraic equation (M) and 26 parameters, described in Table 2. Although from the model reduction process more algebraic relations were obtained, (See Additional file 1, 1.11-FFL Model), they are simple enough to be directly replaced into the model.

<a id='86e73135-4596-41d9-8f5b-bbc4a0ba9184'></a>

An SBML implementation of this model was deposited in BioModels [62] and assigned the identifier MODEL1511290000. This implementation is not part of the multi-objective optimization design procedure, although it was included for completenes and is intended to be used separately. The implementation as matlab scripts is in the Additional file 2, and will be available in Matlab Central.

<a id='1472f7d4-0c11-472e-b925-bebc4eeb3b6d'></a>

For the simulations implemented in the next section, the values in Table 3 are selected for the kinetic parameters that are not considered decision variables.

<a id='2a6fc81b-e645-4fb8-96ac-b95c7b16b0b5'></a>

## Results
Using the presented framework we considered its application for tuning the kinetic parameters of the I1-FFL circuit to achieve adaptation behaviour. The idea is to apply the three steps of the MOOD considering the I1-FFL model presented in the previous section. This way, the implementation of the MOOD procedure will be clarified by an example. Later we will show two scenarios related with the wet-lab implementation and usability of the guidelines obtained.

<a id='7e580593-5aa0-4ea8-8f41-c0d250cb334b'></a>

**I1-FFL tuning using MOOD framework**
***Multi-objective problem (MOP) definition***
The first step of the MOOD framework is to formulate the
circuit specifications as design objectives to be optimized.
Recall the desired input-output behavior for the I1-FFL

<a id='3c01f4f8-76f3-4784-851d-7fff3fa37f51'></a>

Table 1 List of variables used in the reduced model
<table id="8-1">
<tr><td id="8-2">Variable</td><td id="8-3">Description</td><td id="8-4">Units</td><td id="8-5">Symbol</td></tr>
<tr><td id="8-6">X1</td><td id="8-7">mRNAgA</td><td id="8-8">nM</td><td id="8-9">mA</td></tr>
<tr><td id="8-a">X2</td><td id="8-b">A protein</td><td id="8-c">nM</td><td id="8-d">A</td></tr>
<tr><td id="8-e">X3</td><td id="8-f">Inducer</td><td id="8-g">nM</td><td id="8-h">I</td></tr>
<tr><td id="8-i">M</td><td id="8-j">A-l monomer</td><td id="8-k">nM</td><td id="8-l">A-I</td></tr>
<tr><td id="8-m">X4</td><td id="8-n">(A-I)2 dimer</td><td id="8-o">nM</td><td id="8-p">(A-I)2</td></tr>
<tr><td id="8-q">X5</td><td id="8-r">mRNAgB</td><td id="8-s">nM</td><td id="8-t">mB</td></tr>
<tr><td id="8-u">X6</td><td id="8-v">B protein</td><td id="8-w">nM</td><td id="8-x">B</td></tr>
<tr><td id="8-y">X7</td><td id="8-z">mRNAgc</td><td id="8-A">nM</td><td id="8-B">mC</td></tr>
<tr><td id="8-C">X8</td><td id="8-D">C protein</td><td id="8-E">nM</td><td id="8-F">C</td></tr>
<tr><td id="8-G">X9</td><td id="8-H">Extracellular inducer</td><td id="8-I">nM</td><td id="8-J">le</td></tr>
</table>

<a id='e49c1431-7166-4f6f-9846-296c6dd0f758'></a>

circuit, depicted in Fig. 2. Let \theta denote the following
subset of parameters selected for optimization from the
reduced model (3):

<a id='1c45fd56-3bff-4797-b922-659125feff9b'></a>

Two basic objectives can be considered for this circuit
[25, 26, 60, 63]:

*   **Sensitivity**: after input stimulation, a clear transient
    peak value is desired for the output. Sensitivity can be
    defined in relative terms as the relationship between
    the input and output variation during the transient.
    In our case, we define sensitivity as the ratio between
    the absolute total variation of the output signal -the
    C protein concentration x8-, and the variation of the
    input signal -the external inducer x9.
*   **Precision**: after the peak transient, the output must
    go back to its value previous to circuit stimulation.
    Thus, precision can be defined as the inverse of the
    normalized output error. The lower the steady state
    error, the higher the precision.

<a id='9b824d46-00c9-4b42-a913-c0c722e367d1'></a>

Our design objectives can be mathematically expressed
by means of the indexes:

$J_1(\theta) = \frac{2 (x_9 (t_f) - x_9 (t_0))}{\int_{t_0}^{t_f} |\frac{dx_8}{dt}| dt}$

$J_2(\theta) = \frac{x_8 (t_f) - x_8 (t_0)}{x_9 (t_f) - x_9 (t_0)}$ (4)

<a id='8d49417b-4cc5-4a31-b0fb-cfa848be4721'></a>

where $t_f$ is the time length of the experiment. The input stimulus is applied at $t_0$.

<a id='1c7bac37-3d76-475a-ae9a-d0ab152b176e'></a>

Sensitivity is the inverse of J1 (θ). Notice the total absolute variation of the C protein concentration is obtained as half the accumulated absolute value of the time derivative of x8. The lower J1 (θ) (larger output peak w.r.t. input variation), the higher the sensitivity.

<a id='7369db82-3061-48ab-b975-05104af318f2'></a>

Precision is the inverse of J2(θ), i.e. the inverse of the ratio between the variation of the C protein concentration between t0 and tf, and the variation of the external inducer concentration between t0 and tf. If the C protein concentration x8 at time tf is the same as the initial one at time t0, precision is infinite.

<a id='6e63abcf-25c5-4a62-8abf-ab860f576389'></a>

Note that both objectives are defined as the inverses of Sensitivity and Precision in order to use them in the min-imization problem as it is the standard for optimization problems [46].

<a id='634a6d3f-0712-404b-aa5e-94a448b7da32'></a>

Additionally, other objectives could be considered. For instance, fulfillment of constraints on the species. In our case, in order to obtain realistic solutions regarding the values of protein B concentration, its absolute total variation was taken into account as a constraint. This can be expressed as:

$P(\theta) = \int_{t_0}^{t_f} \left|\frac{dx_6}{dt}\right| dt,$

<!-- PAGE BREAK -->

<a id='797a9c09-926a-46b6-b7b8-4e17dbb0ad31'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='d3675652-5126-43ad-918e-079e5bd955ef'></a>

Page 10 of 19

<a id='215f5953-7a15-4f67-b95a-97bf54701eb0'></a>

Table 2 Parameters of the reduced model
<table id="9-1">
<tr><td id="9-2">Parameter</td><td id="9-3">Description</td><td id="9-4">Value</td><td id="9-5">Unit</td></tr>
<tr><td id="9-6">CgA, CgB, CgC</td><td id="9-7">gA, gB, gC copy number</td><td id="9-8"></td><td id="9-9">adim.</td></tr>
<tr><td id="9-a">kmA, kmB, kmC</td><td id="9-b">gA, gB, gC transcription rate</td><td id="9-c"></td><td id="9-d">min⁻¹</td></tr>
<tr><td id="9-e">dmA, dmB, dmC</td><td id="9-f">mA, mB, mC degradation rate</td><td id="9-g">0.3624</td><td id="9-h">min⁻¹</td></tr>
<tr><td id="9-i">kpA</td><td id="9-j">mA translation rate</td><td id="9-k">80</td><td id="9-l">min⁻¹</td></tr>
<tr><td id="9-m">kₚB, kₚC</td><td id="9-n">mB, mC translation rate</td><td id="9-o">*</td><td id="9-p">min⁻¹</td></tr>
<tr><td id="9-q">dA</td><td id="9-r">A degradation rate</td><td id="9-s">0.035</td><td id="9-t">min⁻¹</td></tr>
<tr><td id="9-u">dB, dC</td><td id="9-v">B, C degradation rate</td><td id="9-w">*</td><td id="9-x">min⁻¹</td></tr>
<tr><td id="9-y">kd</td><td id="9-z">inducer diffusion rate</td><td id="9-A">0.06</td><td id="9-B">min⁻¹</td></tr>
<tr><td id="9-C">k2, k3</td><td id="9-D">(AI) and (AI)₂ association rate</td><td id="9-E">0.1</td><td id="9-F">min⁻¹</td></tr>
<tr><td id="9-G">k_2</td><td id="9-H">(Al) dissociation rate</td><td id="9-I">20</td><td id="9-J">min⁻¹</td></tr>
<tr><td id="9-K">k_3</td><td id="9-L">(Al)₂ dissociation rate</td><td id="9-M">1</td><td id="9-N">min⁻¹</td></tr>
<tr><td id="9-O">γ1</td><td id="9-P">gB promoter Hill constant</td><td id="9-Q"></td><td id="9-R">nM</td></tr>
<tr><td id="9-S">γ2</td><td id="9-T">gC promoter coefficients</td><td id="9-U">0.2</td><td id="9-V">nM</td></tr>
<tr><td id="9-W">γ3, γ4, γ5</td><td id="9-X">gC promoter coefficients</td><td id="9-Y"></td><td id="9-Z">adim, adim, nM⁻¹</td></tr>
<tr><td id="9-10">β1, β2</td><td id="9-11">gC promoter basal expression coefficients</td><td id="9-12">0.05</td><td id="9-13">adim, nM⁻¹</td></tr>
<tr><td id="9-14">dI, dIe</td><td id="9-15">inducer degradation rate</td><td id="9-16">0.0164</td><td id="9-17">min⁻¹</td></tr>
<tr><td id="9-18">dAI, dAI2</td><td id="9-19">(AI), (AI)2 degradation rate</td><td id="9-1a">0.035</td><td id="9-1b">min⁻¹</td></tr>
</table>

<a id='7d97d98f-7e3d-4b70-808e-ef59b5ed6d2c'></a>

We considered the constraint:

1 < P(θ) < 10000 (5)

<a id='dae363ca-0e43-4555-9d9c-e67d17753b8f'></a>

To make the precision higher (that is, low output error)
the easiest option is to have very high values of protein
B concentration, which acts as repressor of protein C. To
avoid this unrealistic solution, it is possible to make the
concentration of protein B to have an upper bound. In the
case of not having this restriction, the solutions may have
higher precision at the cost of unrealistically high values of
protein B concentration. The restriction penalizes this fact
and drives the search to a different region of the parame-
ter space (going away from this undesired region, the one
corresponding to high values of protein B).

<a id='45afcbe1-3419-44a1-b681-b5fa9d287e22'></a>

Another relevant issue is the definition of limits for J_1(θ) and J_2(θ) beyond which we consider that precision and sensitivity degrade to such an extent that we cannot talk about adaptive behavior anymore [26]. This is the so-called *pertinency* range of the objectives. The limits established in this work are: J_1(θ) ∈ [1 × 10^{-3}, 200], and J_2(θ) ∈ [1 × 10^{-4}, 20].

<a id='299ed0b4-6080-486e-9a9b-3f96301b8394'></a>

Table 3 Parameters of the reduced model selected for optimization
<table><thead><tr><th>Parameter</th><th>Wet-lab implication</th></tr></thead><tbody><tr><td>k<sub>mB</sub>C<sub>gB</sub>, k<sub>mC</sub>C<sub>gC</sub></td><td>Promoter strength and Plasmid origin of replication</td></tr><tr><td>k<sub>pB</sub>, k<sub>pC</sub></td><td>RBS Strength</td></tr><tr><td>γ<sub>1</sub>, γ<sub>3</sub>, γ<sub>4</sub>, γ<sub>5</sub></td><td>Mutations in promoter sequence</td></tr><tr><td>d<sub>B</sub>, d<sub>C</sub></td><td>Degradation tag sequence</td></tr></tbody></table>

<a id='003a2fb0-b796-4a01-829f-5a4029870a7f'></a>

Finally, we look for the set of values for the 10 decision
variables θ that optimize both objectives. Yet, precision
and sensitivity are conflicting objectives. So a trade-off
must be reached. Therefore, our problem can be formu-
lated as a multi-objective problem (MOP):

<a id='68d01c96-4b9d-4c76-b415-c64b0bfa6d39'></a>

min J(θ) = [J_1(θ), J_2(θ)] ∈ R^2 Eq. (3)
θ ∈ R^10
subject to:
1 × 10^-3 < J_1(θ) < 200
1 × 10^-4 < J_2(θ) < 20
1 < P(θ) < 1 × 10^5 (6)

<a id='e83488ea-15e2-4fd0-b2e0-10c499ac0686'></a>

**Multi-objective optimization**
As a second step we carried out the dynamic optimization of (6) using the multi-objective differential evolution spMODE genetic algorithm described in Subsection Multi-objective parameters tuning. Starting from an initial random population of candidate solutions, we set 15.000 iterations as the maximum number of evaluations of the objective functions. We obtained a Pareto front containing 33 solutions that achieve adaptation, together with the Pareto set containing the kinetic model parameters corresponding to the Pareto front solutions (see Additional file 1: Table S3). These solutions show, as expected, a trade-off. Solutions range from high sensitivity (low values of J₁) and low precision (high values of J₂) ones to low sensitivity (high values of J₁) and high precision (low values of J₂) ones. Note in all cases these solutions are the optimal ones, in the sense of Pareto.

<!-- PAGE BREAK -->

<a id='4b0e5edc-2b58-4066-949b-fc5bfc15fc1e'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='063f99e5-11d7-4faa-8599-76461834062a'></a>

Page 11 of 19

<a id='a2fcd39a-e07b-44ff-bfaf-fbb0cfece70b'></a>

A Monte-Carlo sampling (MCS) and a Latin Hypercube sampling (data not shown) with the same computational cost were performed for the sake of comparison. In both cases, the solutions must be selected with a dominance filter so as to detect the ones actually fulfilling the constraints and yielding adaptive dynamics [25]. Note this functional association step is not required in our approach, as the optimal sets of parameters obtained already correspond to functional ones. From the functional solutions obtained with these sampling techniques, we approximated the corresponding Pareto front. Figure 4 shows the results obtained. The Pareto front obtained from the MCS (dominant solutions in green) covers a larger region of the objectives space, but outside of our region of interest (pertinency box), and it is far away behind the optimal one obtained with spMODE.

<a id='137905a0-ba6b-4024-8e18-b627aa1a9de4'></a>

_**Obtaining guidelines for the implementation**_
The third step is to obtain guidelines and guidance for the implementation of the circuit. To obtain the guidelines, the solutions gathered from the optimization were clustered hierarchically in an agglomerative tree (see Matlab code in Additional file 1) and the optimal number of clusters obtained with the procedure explained in the Methods section. The guidelines obtained are shown as intervals in the next Table.

<a id='abf0e242-e008-4a1e-865d-66c424a81dda'></a>

As result we can put into words the following general guidelines, which are necessary for achieving adaptation:

* d_B: Degradation rate of protein B, has to be the lowest possible in all the cases.
* Kp_B: The RBS strength of gene B has to be the lowest possible in all the cases.
* \gamma_1: The promoter strength (activation strength) has to be high in general, but it does not has an apparent effect.

<a id='4436773d-8502-4a69-9901-e182ab156f94'></a>

• y3: The hybrid promoter strength (activation strength), has to be the lowest possible in all the cases.

<a id='c41b511a-449f-4ce8-bf8c-cee84749d9c0'></a>

Depending on whether high sensitivity or high precision are chosen, specific guidelines (see Table 4) can be given for the tuning knobs to be modified in the wet-lab so as to tune the behavior of the circuit:

<a id='f00dbd14-c7e7-4db5-9f7b-276c52e795d8'></a>

High Sensitivity Strategy:

*   _KmCCgC_ and _KpC_: increasing values of the promoter strength and plasmid copy number of gene C, and the RBS Strength of gene C, lead to increasing values of sensitivity (higher peak values). These are tuning knobs for sensitivity.
*   _dC_: degradation of protein C has to be slightly lower for high sensitivity.
*   _γ4_ and _γ5_: Hybrid promoter strengths (repression, and activation - repression cross combined strength), should be kept low.
*   _KmBCgB_: Promoter strength and plasmid copy number of gene B, must have low values.

<a id='164b3689-a5f1-4b39-a7a9-3f02a395cc7b'></a>

**High Precision Strategy:**
*   *KmBCgB*: Promoter strength and plasmid copy number of gene B, is a tuning knob for Cluster 6, increasing precision proportionally to its value.
*   *γ4* and *γ5*: Increasing values of the hybrid promoter strengths lead to increasing values of precision (lower error).
*   *KmCCgC* and *KpC*: Promoter strength and plasmid copy number of gene C, and the RBS Strength of gene C, keep them low.
*   *dC*: degradation of protein C has to be high.

<a id='354dc8e3-b38f-432c-8a07-326db6d42cd9'></a>

The results show that the value of $d_C$, i.e. the degradation rate of the C protein, is a key parameter to correctly

<a id='19a91d82-1a8e-40f8-b10b-518373e181ae'></a>

<::transcription of the content: chart::>Fig. 4 Pareto Front comparison. This chart displays J2 on the y-axis (log scale from 10^-2 to 10^2) versus J1 on the x-axis (log scale from 10^-3 to 10^2). A legend indicates: 'Monte Carlo sampling' with red open circles, 'MC dominant solutions' with a green line and asterisks, 'Pareto Front (spMODE)' with a blue line and filled circles, and 'Objectives pertinency box' with dashed lines. Pareto Front representation for J₁ and J2 obtained with the spMODE algorithm for the MOO (blue line). Monte-Carlo random sampling results are colored in red and the dominant solutions are in green. The time response of the C protein concentration for three representative points are shown

<!-- PAGE BREAK -->

<a id='2728c219-0db3-4839-9b35-b5729170431d'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='a41dc40a-3f18-45e0-ab2d-c2bb82360e91'></a>

Page 12 of 19

<a id='5b0ec726-b65c-43dc-b379-cde00769e4e8'></a>

Table 4 Design guidelines. Each one of the optimized parameters is either a general guideline for all clusters, or is a trade-off control
tuning knob for a specific cluster
\
<table id="11-1">
<tr><td id="11-2">Parameter</td><td id="11-3">Initial parameter range</td><td id="11-4"></td><td id="11-5">Design guideline</td><td id="11-6"></td></tr>
<tr><td id="11-7"></td><td id="11-8"></td><td id="11-9">General guideline</td><td id="11-a">Cluster 1</td><td id="11-b">Cluster 2</td></tr>
<tr><td id="11-c">kmACgA*</td><td id="11-d">[1 200]</td><td id="11-e"></td><td id="11-f">[1 171.91]</td><td id="11-g">1</td></tr>
<tr><td id="11-h">kmBCgB</td><td id="11-i">[1 200]</td><td id="11-j"></td><td id="11-k">1</td><td id="11-l">[1 200]</td></tr>
<tr><td id="11-m">kmCCgC</td><td id="11-n">[1 200]</td><td id="11-o"></td><td id="11-p">[1 171.91]</td><td id="11-q">1</td></tr>
<tr><td id="11-r">kpB</td><td id="11-s">[1 100]</td><td id="11-t">1</td><td id="11-u">–</td><td id="11-v">–</td></tr>
<tr><td id="11-w">kpC</td><td id="11-x">[1 100]</td><td id="11-y">–</td><td id="11-z">[1 15.68]</td><td id="11-A">1</td></tr>
<tr><td id="11-B">dB</td><td id="11-C">[0.01 0.3]</td><td id="11-D">[0.01 0.0792]</td><td id="11-E">–</td><td id="11-F">–</td></tr>
<tr><td id="11-G">dc</td><td id="11-H">[0.01 0.3]</td><td id="11-I">–</td><td id="11-J">[0.2784 0.3]</td><td id="11-K">0.3</td></tr>
<tr><td id="11-L">y1</td><td id="11-M">[50 200]</td><td id="11-N">[78.93 200]</td><td id="11-O">–</td><td id="11-P">–</td></tr>
<tr><td id="11-Q">Y3</td><td id="11-R">[1e-4 0.5]</td><td id="11-S"></td><td id="11-T">[1e-4 0.013]</td><td id="11-U">[1e-4 0.0141]</td></tr>
<tr><td id="11-V">Y4</td><td id="11-W">[5e-4 5]</td><td id="11-X"></td><td id="11-Y">[5e-4 1.4424]</td><td id="11-Z">[0.0697 5]</td></tr>
<tr><td id="11-10">Y5</td><td id="11-11">[1 100]</td><td id="11-12"></td><td id="11-13">[1 9.2546]</td><td id="11-14">[12.125 100]</td></tr>
</table>
\
*kmACgA Is the same as kmCCgC as the are physically in the same plasmid

<a id='a0577af5-c308-460c-93fb-7d536c77c61f'></a>

achieve adaptation. With high values of this parameter, the concentration of the C protein will to return faster to its original level.

<a id='10752968-dc4a-45ac-aa07-4356717cb026'></a>

Some parameters γ in the hybrid promoter of protein C are also forced to take certain values for the system to attain the adaptive behavior. In particular, it is interesting to notice that the repression strength, parameter γ4 plays an important role, which is in agreement with the analysis in [34], where a mutation was performed on the hybrid promoter so as to affect the same parameter.

<a id='48884dc6-25ed-46f7-9398-7e44a4112176'></a>

In the case the designed needs more insight, we provide the tools for visualization to allow a proper decision mak-ing procedure and selection of the appropriate parameters for the design.

<a id='4c2906e2-30b1-4151-8e35-6bfb5b82a238'></a>

The Pareto front together with the time response of the C protein concentration for each point are shown in Fig. 5. Clusters range from high sensitivity and low precision (cluster 1) to low sensitivity-high precision ones (cluster 2). In Fig. 6 the Pareto set is depicted the value of each parameter and its membership to the corresponding cluster. This way is easy to directly find the implication of each parameter in the design. After the analysis of the Pareto set plot it is possible to find: on the one hand, parameters _d_B, _K_pB and γ3 have uniform (and tight) values for both clusters and γ1 has a uniform and wide range of values also for both clusters. On the other hand, we find basically two different strategies: one for high sensitivity (clusters 1, with red color, in Fig. 6) which changes parameters in gene C (_K_m_gC_gC, _k_pC and less _d_C), and another one for high precision (clusters 2, blue colors, in Fig. 6) which changes parameters in gene B and in the hybrid promoter (_K_m_BC_gB, γ4 and γ5).

<a id='b2c6fa9d-803d-4a93-9574-ee44a92c878f'></a>

In the Additional file 1: Figures S3 and S4 the original
Level Diagrams of the Pareto front and set are shown, in

<a id='3413b428-e410-4ae3-bbe6-82dcdc170f33'></a>

case the designed needs more information and insight for
the guidance of its multi-criteria decision-making.

<a id='24503458-bd66-4244-999d-fbc78cc04316'></a>

Application scenario I: selecting parameters for an implementation
As a proof of concept, and also to validate the guide-
lines obtained for the I1-FFL we proceed as we would
do in the wet-lab. Let us suppose we have two imple-
mentations obtained with the guidelines proposed in this
work: one designed with the High Sensitivity Strategy
(Case A) and another one with High Precision Strategy
(Case B).

<a id='044c7480-5f17-4786-b0c1-a24e1198e134'></a>

The Case A is a solution with low precision, but high sensitivity as it belongs to cluster number 1. It is located in the low extreme of J~1~, and in the high end of J~2~ in Fig. 5. For this design will use the High Sensitivity Strategy and we will choose, for example, kp~C~ as a tuning-knob. Changing the value of this parameter will affect the position of the solution in the Pareto front. Although, moving exactly along the Pareto front requires modifying more parameters as shown in the guidelines before, we can see (by looking at the reddish dots in see Fig. 7) how the initial chosen solution moves almost on top of the Pareto front. This shows that the obtained guidelines are robust so that we can use the selected parameter as a tuning knob in the wet-lab implementation.

<a id='bd632897-ebc0-4ea2-8046-37b70451f730'></a>

Also, starting from the high precision implementation
(Case B), we show how changing one of the tuning knobs
from our High Precision Strategy ($Km_BCgB$ for exam-
ple) one can almost move along the Pareto front and
obtain higher sensitivity solutions without losing preci-
sion, as shown by the bluish dots. In the insets of Fig. 7
is possible to see the temporal behavior of the obtained
solutions.

<!-- PAGE BREAK -->

<a id='40482fbd-eeae-4b27-a945-f842148fd255'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='4af61999-2bc5-4f25-9135-f9eed7816de8'></a>

Page 13 of 19

<a id='0d4f1a9d-5044-4d46-9aaa-406ec66b9a85'></a>

<::chart:Fig. 5 Pareto front representation in the cluster-modified LD tool. a Value of the objectives J₁ and J₂ for each solution where each cluster is identified by a different color. Clusters range from high sensitivity-low precision (red) to low sensitivity-high precision ones (blue). The figure is composed of two main panels, A and B.Panel A contains two scatter plots. The left scatter plot shows J₁ (θ) on a logarithmic x-axis ranging from 10⁻² to 10² and 'Cluster' on the y-axis, with values 1 and 2. Solutions belonging to Cluster 1 are represented by red circular markers, and solutions belonging to Cluster 2 are represented by blue circular markers. The right scatter plot shows J₂ (θ) on a logarithmic x-axis ranging from 10⁻³ to 10² and 'Cluster' on the y-axis, with values 1 and 2. Solutions belonging to Cluster 1 are represented by red circular markers, and solutions belonging to Cluster 2 are represented by blue circular markers.b Time courses of protein C concentration for the different solution in the clusters.Panel B contains two line plots. Both plots share 'Time [min]' on the x-axis, ranging from 0 to 50. The left line plot shows 'Protein C Concentration x 10⁴' on the y-axis, ranging from 0 to 5. It displays multiple red lines, each representing a time course of protein C concentration. The right line plot shows 'Protein C Concentration' on the y-axis, ranging from 0 to 80. It displays multiple blue lines, each representing a time course of protein C concentration.::>

<a id='df50760b-0e3f-4509-a97e-14932577ab21'></a>

Conversely to this, changing values of key parameters like dC completely destroy the adaptation behavior independently of the selected solution (see Figure S2 in Additional file 1).

<a id='c6a64947-a1a8-4040-aa52-c3758a401fae'></a>

**Application scenario II: output robustness analysis**
This framework is also useful to analyze the output performance of the designed functional device when connecting it to other devices.

<a id='b3e09214-171b-498a-b714-9f296a830a0f'></a>

Here we will use a simple binding reaction as a load to
demonstrate the procedure (see Fig. 8). This is one of the
most common types of load. For example, the protein C
could be a transcription factor and bind to a promoter

<a id='a68028a9-c8ab-448f-a688-2fbef7c8577c'></a>

region in the DNA. The next equations model this load
binding reaction:

ẋ₈ = kₚcχ₇ - d_cχ₈ - K₁χ₈χ₁₀ + K₂χ₁₁
ẋ₁₀ = -K₁χ₈χ₁₀ + K₂χ₁₁ (7)
ẋ₁₁ = K₁χ₈χ₁₀ - K₂χ₁₁

<a id='527e314c-3f36-4293-85ff-6b21ef79592c'></a>

where $x_{10}$ represents the empty load species (e.g. an unbound promoter or protein), and $x_{11}$ represents the complex C bound to the load species. $K_1$ and $K_2$ are the binding constants. For this case we used $K_1 = 40 \ nM^{-1}min^{-1}$, and $K_2 = 20 \ min^{-1}$, which correspond to a mildly fast binding. We chose the initial

<!-- PAGE BREAK -->

<a id='1b0bd7fc-03eb-430d-bcf2-1d08ec72e3f4'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='7ff7b88c-f95d-414c-9da0-7d0bd1b260cd'></a>

Page 14 of 19

<a id='53110cf9-c973-4b53-a20e-ba2fc33b8210'></a>

<::Figure: A grid of 10 scatter plots showing the distribution of decision variables (kinetic parameters) for two clusters, High Sensitivity Strategy (cluster 1, red dots) and High Precision Strategy (cluster 2, blue dots). Each subplot has 'Cluster' on the y-axis, with values 1 and 2, and a different kinetic parameter on the x-axis. The plots are arranged in three rows and four columns (the last row has only two plots). 

**Row 1:**
1.  **Plot 1 (Top-left):** X-axis: KmBCgB (ranging from 0 to 200). Red dots (cluster 1) are clustered between 25 and 50. Blue dots (cluster 2) are distributed from 25 to 200.
2.  **Plot 2:** X-axis: dB (ranging from 0 to 0.3). Red dots (cluster 1) are clustered around 0.05. Blue dots (cluster 2) are clustered around 0.05, 0.15, and 0.25.
3.  **Plot 3:** X-axis: kpB (ranging from 0 to 100). Red dots (cluster 1) are clustered between 15 and 20. Blue dots (cluster 2) are distributed from 15 to 100.
4.  **Plot 4 (Top-right):** X-axis: γ1 (ranging from 50 to 200). Red dots (cluster 1) are distributed between 100 and 180. Blue dots (cluster 2) are distributed between 100 and 200.

**Row 2:**
5.  **Plot 5 (Middle-left):** X-axis: γ3 (ranging from 0 to 0.4). Red dots (cluster 1) are clustered around 0.05. Blue dots (cluster 2) are clustered around 0.05.
6.  **Plot 6:** X-axis: γ4 (ranging from 0 to 5). Red dots (cluster 1) are distributed between 0.5 and 4. Blue dots (cluster 2) are distributed between 0.5 and 5.
7.  **Plot 7:** X-axis: γ5 (ranging from 0 to 100). Red dots (cluster 1) are clustered around 15-20. Blue dots (cluster 2) are distributed from 15 to 100.
8.  **Plot 8 (Middle-right):** X-axis: KmCCgC (ranging from 0 to 200). Red dots (cluster 1) are distributed between 50 and 180. Blue dots (cluster 2) are distributed between 50 and 200.

**Row 3:**
9.  **Plot 9 (Bottom-left):** X-axis: dC (ranging from 0 to 0.3). Red dots (cluster 1) are clustered around 0.05 and 0.3. Blue dots (cluster 2) are clustered around 0.05 and 0.3.
10. **Plot 10 (Bottom-right):** X-axis: kpC (ranging from 0 to 100). Red dots (cluster 1) are clustered around 15-20. Blue dots (cluster 2) are distributed between 15 and 100.

Fig. 6 Representation of the Pareto set. Cluster-modified LD representation for decision variables (kinetic parameters) in the High Sensitivity Strategy (cluster 1, red dots) and in the High Precision Strategy (cluster 2, blue dots): chart::>

<a id='30909fcb-1871-4287-abb5-63dd88961bf5'></a>

<::chart: Fig. 7 Application scenario I Pareto Front. The main plot is a log-log scatter plot showing J2 on the y-axis (ranging from 10^-3 to 10^2) versus J1 on the x-axis (ranging from 10^-3 to 10^2). A blue line connects various dots representing the Pareto Front. Dots with reddish color (labeled "Case A") are obtained when using the RBS strength of gene C as a trade-off tuning knob and represented by modifying $k p_C \in [5 \ 0.05]$ starting at the extreme solution. An arrow points from "Case A" to the reddish dots on the Pareto front. Dots with bluish color (labeled "Case B") are obtained when using the promoter strength and plasmid copy number gene B by modifying $K m_B C g_B \in [200 \ 1]$. An arrow points from "Case B" to the bluish dots on the Pareto front. An inset plot shows the time course of protein C. The inset contains two subplots. The top subplot shows Protein C concentration (y-axis, from 0 to 6 x 10^4) versus time [sec] (x-axis, from 0 to 40) with multiple reddish-colored curves. The bottom subplot shows Protein C concentration (y-axis, from 0 to 30) versus time [sec] (x-axis, from 0 to 40) with multiple bluish-colored curves. Arrows connect specific regions of the main Pareto front plot to the corresponding time course plots in the inset. Notice, that decreasing only $k p_C$ it is possible to increase the sensitivity, almost without losing optimality (without getting away from the Pareto front). As expected, sensitivity of the solution is increased, i.e. the peak of protein concentration after stimulus is higher.::>

<!-- PAGE BREAK -->

<a id='5c686df9-7cc0-4e2a-9d61-f6e48c1d73e5'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='d43a4e3c-50d5-4b9f-90c0-53468b2b92ca'></a>

Page 15 of 19

<a id='f5981cda-61c6-441b-8a04-9a0fa1db654a'></a>

<::diagram: The diagram is titled "Output robustness" and depicts a system with an input, a gene network, and a load.The input is represented by a green rectangle containing a step function that goes from an initial level labeled "I_e1" to a higher level labeled "I_e2". Below this rectangle, the text reads "INPUT Inductor I_e".An arrow points from the input rectangle to a pink rectangle labeled "Gene network E. coli bacterium".Another arrow points from the pink "Gene network" rectangle to a red rectangle labeled "LOAD".Below the main flow, there's a section titled "Load reaction". This section illustrates a biochemical reaction with "Protein C" above two bidirectional arrows. On the left of the arrows is "Load" and on the right is "C. Load".A light blue arrow connects the "Gene network" to the "Load reaction" section, specifically pointing towards the "Load" text.To the right of the "Load reaction" section, there is a small graph and a question. The graph has a horizontal x-axis labeled "time" and a vertical y-axis that is unlabeled. The curve on the graph shows an initial baseline at "O_1", then a sharp increase to a peak labeled "O_peak", followed by a decrease to a new steady state labeled "O_2". Next to the graph is a large question mark. Below the graph and question mark, the text reads "Do we still have adaptation?"::>Fig. 8 Application scenario II Depiction of the incorporation of information on the context. Connecting our module to a load

<a id='131ff193-461d-4158-b5c6-28c9aae264a1'></a>

condition $x_{10}(t_0) + x_{11}(t_0) = 800\,nM$. Since we did not consider degradation terms in (7), this initial condition represents the total amount of available load species.

<a id='47072e80-e217-4997-9a80-e78ba3a5260f'></a>

In Fig. 9, the Pareto front of the loaded device is shown in red colored diamonds, and the original Pareto front in blue circles. Notice that the analysis needs to be performed only along the Pareto front solutions. Thus, it is computationally very efficient. As we see for the I1-FFL circuit, solutions with low sensitivity are

<a id='d12484d5-aa30-4440-8a8b-6c5d97c68553'></a>

more affected by the load effect at high values of $J_1$, i.e.
lower peak values of C protein. This happens when the
concentration of C is in the order of 800 $nM$, which is
the total amount of load species concentration in this
example.

<a id='34bb94aa-b2f2-4aa7-a86a-c5303285e1ef'></a>

Finally, in the inset of Fig. 9, the loaded time courses of the protein C concentration after stimulus (red line) are shown and compared with the original ones (blue line) for values of the parameters corresponding to solutions 1,

<a id='ddc89c90-e7d4-43fb-9b3b-28610a522239'></a>

<::chart: The figure displays a Pareto front for a functional module, with inset plots showing temporal responses. The main plot is a scatter plot with a log-log scale. The x-axis is labeled "J1" and ranges from 10^-3 to 10^2. The y-axis is labeled "J2" and ranges from 10^-3 to 10^3. Two data series are shown: "Pareto Front (with Load)" represented by red diamonds, and "Pareto Front (without Load)" represented by blue circles. Several points on the Pareto front are marked with numbers 1, 2, and 3.  The figure includes three inset line graphs, each showing "Protein C concentration" on the y-axis against "time [sec]" on the x-axis (ranging from 0 to 40 sec). Each inset graph shows two lines: a red line representing responses "with load" and a blue line representing responses "without load". Inset 1 (corresponding to point 1) shows protein C concentration peaking around 3000-3500. Inset 2 (corresponding to point 2) shows protein C concentration peaking around 350-400 for the blue line and around 100 for the red line. Inset 3 (corresponding to point 3) shows protein C concentration peaking around 50 for the blue line, while the red line remains very low, close to zero.::>Fig. 9 Application scenario II Pareto front of the functional module without load (blue circles) and with load (red diamonds). Inset: temporal responses of the solutions 1, 2 and 3 with (red line) and without load (blue line)

<!-- PAGE BREAK -->

<a id='8af058ae-2a7e-4eaa-9f31-5018b68d9abb'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='0b7b5f19-fae6-40c7-af8c-e8a21e67d662'></a>

Page 16 of 19

<a id='e5e0bffb-18d9-48de-a540-19e9da8c43bb'></a>

2 and 3. As we see, solution 1 is practically not affected;
but solution 2 is affected considerably. Finally, solution 3
is way out from is location and actually looses adaptation
behavior. Consequently, it is possible to use this frame-
work to evaluate the output performance of our designed
circuit.

<a id='abb903d7-40dc-4717-aa26-b442f8f53677'></a>

**Discussion**
Computer-aided model-based methods and tools are being increasingly used in synthetic biology to guide the design of synthetic biochemical pathways so as to achieve user-defined functions and behaviors [9–11].

<a id='30f0dfe3-20fc-49fb-8a7f-7b05ca1f592f'></a>

In this work, in order to obtain a set of guidelines to aid the design of synthetic genetic networks with a predefined functionality (functional modules), we developed a framework using a multi-objective optimization design (MOOD) procedure. Compared to previous studies [25], a novel feature of our framework is that the result of the optimization is already a set of parameters that optimally achieve the desired function and dynamics, as encoded in the objective indexes. Specifying the desired circuit behavior in terms of performance indexes to be optimized has many advantages. The indexes or objectives can be made valid for a whole class of input signals, they may consider other signals in the circuit apart from input and output, the robustness with respect to uncertainty in the circuit parameters can be included, etc. The proper definition of the optimization indexes representing the desired behavior is a key point. An incorrectly specified objective, not properly representing the actual desired behavior, will lead the optimization in a wrong direction, thus returning a parameters set that will give misleading design guidelines. This is a drawback, but easier to handle than setting the thresholds defining the acceptable circuit behavior after a Monte Carlo sampling, for these do not ensure that a solution will be found [25, 27].

<a id='5113a380-9558-49f6-9db1-b0cc41558af6'></a>

The solutions obtained, i.e. the design objectives together with the respective parameter sets, may be clustered hierarchically, or post-processed with any multivariate statistical analysis tool in order to get further insight into the role of the different parameters. The importance of this, is that the spMODE and LD-tools already order the Pareto front solutions with respect to the objective functions. The LD-tool, as a matter of fact, already provides insight into the role of the different solutions. Further statistical processing is very efficient, as only a small set of data has to be processed (the solutions at the Pareto front), and this set is already ordered. This allows us to reveal and understand associations of parameters and functionality. For example, cluster 1 (red) in the Results Section has the highest sensitivity together with the lowest precision. To implement in the wet-lab a system with this functionality, the RBS in gene B has to be weak, and it should be

<a id='e6bfb2b7-5732-420c-8521-11ea7a0f1631'></a>

cloned in a low copy plasmid, as reflected by the guidelines obtained for parameters kpB and KmBCgB, respectively. On the contrary, to implement a cluster 2 (blue) system, the guidelines obtained for the same parameters tell us to put gene B also with a weak RBS and but in a high copy plasmid (Fig. 6).

<a id='095befc4-0f67-405e-aeb0-b31340186043'></a>

For a given circuit design with a desired functionality,
the guidelines for the kinetic parameters (Fig. 6, Table 4)
are very useful to decide which biological components to
use out of the ones available from a library of biologi-
cal parts, such as the MIT Registry of Standard Biological
Parts [64] by iGEM Foundation, the BIOSS Toolbox [65],
or BioFab [66]. In particular, for the I1-FFL, we showed
that important tuning knobs are:

<a id='31aebeed-fa72-44fb-8dcf-485a2fc9a676'></a>

*   _KmXCgX_. This is a lumped plasmid copy number and promoter strength, so it can be tuned by selecting the appropriate replication origin of the plasmid and the promoter; for example from the Anderson Promoter library [53] available at the iGEM Parts Registry.
*   _kpX_ represents the Ribosome Binding Site strength, and is one of the easiest parameters to tune in the wet-lab using, for instance, RBS libraries, the RBS Calculator from Sallis Lab [54], or nucleotides repetition [55].
*   _dX_ is the protein degradation rate. It also can be tuned globally by changing the growth rate of the microorganism. It also can be tuned by adding a protein degradation tag to include the protein in an active degradation pathway.

<a id='2c50e69e-db25-4650-a602-b1530c711e96'></a>

As more and more parts are deposited and character-
ized in these libraries, frameworks providing guidelines
for the design and wet-lab implementation, like the ones
presented here, will gain more applicability and the design
of synthetic genetic circuits will become more rationale-
based than intuition-based.

<a id='db2f4ea5-dbb7-46ed-b8b4-9fb5eedcbef1'></a>

The analysis performed in the Application Scenario I,
shows that it is possible to use only one parameter to
move from the Pareto front to a sub-optimal solution. For
example, starting from a solution with high precision and
low sensitivity, one can move to a solution with higher
sensitivity and lower precision; with almost no losing opti-
mality. This is very useful in the wet-lab, because it means
that once you have the system implemented in the wet-
lab, it is possible to change the output of your system
in a controlled way by performing the minimum amount
of changes to it. The methodology easily allows to check
how the initial solution will deteriorate by changing the
value of only one parameter (see Fig. 7). Of course, mov-
ing along the Pareto front solutions requires modifying
more parameters, i.e. changing the values of the param-
eters from a cluster to another one; however we showed
that the obtained guidelines are really robust and that we

<!-- PAGE BREAK -->

<a id='ad66a209-b7da-4901-88b1-fc293c437b90'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='0db2166d-8808-4219-b3d4-c62e434c8849'></a>

Page 17 of 19

<a id='d81cf709-f5f6-4005-a379-b9920ec07625'></a>

can use a particular parameter as a tuning knob in the
wet-lab implementation.

<a id='01009bdb-775d-49da-a665-fcc892fafb8f'></a>

In the Application Scenario II, we saw that it is straightforward to have an idea of how much the functionality of the system can be compromised by loading it, i.e. by connecting it to another module. The proposed methodology allows to design the system taking this into account. The analysis is computationally efficient, as it has to be performed only for the Pareto front solutions, and not for the whole objective space. Thus, we foresee that extending the approach to the analysis of interconnecting several devices will not be difficult. In a way, as advocated in [5], the approach is less like highly modular electrical engineering, and more like civil and mechanical engineering in its use of optimization of modeling of whole system-level taking into account loads and flows.

<a id='63e6e985-8036-4cfb-be1f-8cb83290ed8d'></a>

Notice that the analysis needs to be performed only along the Pareto front solutions. In this case, we are performing a robustness analysis _a posteriori_ with the Pareto optimal solutions approximated. That is, the decision making process is carried out at the end of the MOOD process using additional information, in order to select a _robust_ configuration. This is congruent with similar analysis of uncertainties and decision making [67].

<a id='0e04c8dd-85c6-456a-a76f-8b9632dbafa9'></a>

If it is required by the decision maker to seek actively for a robust set of solutions, a different approach will be required. That is, in order to get such solutions then the robustness measure analysis should be included _a priori_ within the optimisation process. This leads to different optimisation instances known as robust design optimization (RDO) and reliability based design optimisation (RBDO) [68]. The former seeks to minimize the sensitivity of a solution; the latter to provide a measure of risk failure. In any case, such optimization instances are out of the scope of this work and are proposed as future work.

<a id='6023fa38-5d23-45d9-80c9-10ea116f2c2a'></a>

The general applicability of the framework allows to use it with different functional modules and topologies, as soon as the ODEs can be obtained from reactions, although evidently difficulties will arise when dealing with larger networks. In that sense it is interesting to note the difference between the problem of expensive computation and the one of large-scale optimization. Expensive computation arises when the complexity of the system makes the evaluation of the objective function an expensive task. On the contrary, large-scale is related with the amount of decision variables and the size of the objective space. In the cases we are dealing with, this two problems will be more or less coupled. For a larger network, more kinetic parameters (decision variables) and more expensive computation of the dynamics of the system to evaluate the objectives. Nevertheless, one of the key issues will be to obtain a reasonable reduced model of the module

<a id='d8191855-2148-4302-8443-bf7f53c54a8f'></a>

to give to the optimization algorithm rather than the opti-
mization itself. Genetic algorithms like spMODE have
been used in the past with problems with sizes includ-
ing 15 objectives and hundreds of decision variables with
reasonable computational cost, and related research is a
hot topic [69, 70]. Also memory handling in the men-
tioned algorithms is very efficient, as the only informa-
tion that propagates from generation to generation is the
population.

<a id='5b086d5b-2bbd-481d-9b4e-a9b12074aefa'></a>

# Conclusion
The proposed multi-objective optimization design framework is able to provide effective guidelines to tune biological parameters so as to achieve a desired circuit behavior. Moreover, it is easy to analyze the impact of the context on the synthetic device to be designed. That is, one can analyze how the presence of a downstream load influences the performance of the designed circuit, and take it into account. Finally, our results suggest that -although system dynamics actually put constraints on the possible values of the kinetic parameters- design guidelines can be obtained to build a biological systems with a desired functionality.

<a id='3f15f6a2-9908-4e05-b9d6-55a78fa5e09f'></a>

## Availability of data and materials
All the material used in this work can be found in the following locations:

*   The spMODE, a multi-objective optimization algorithm based on differential evolution implemented in MATLAB is available at MatlabCentral, code 39215. http://www.mathworks.com/matlabcentral/fileexchange/39215
*   The LD-tool toolbox to help visualization in MATLAB is available at MatlabCentral, code 24042. http://www.mathworks.com/matlabcentral/fileexchange/24042
*   An SBML implementation of the I1-FFL model was deposited in BioModels with identifer MODEL1511290000. https://www.ebi.ac.uk/biomodels-main/ (This implementation is not part of the multi-objective optimization design procedure, although it was included for completeness and is intended to be used separately.)
*   The source code of the all the software developed for this work is available in the Additional file 2 --- matlabscripts.zip and also publicly available at http://sb2cl.ai2.upv.es/content/software, and it is explained in Additional file 1, Section 2. Matlab CODE.

<a id='0663b63b-cccf-4104-a51f-627bea07219b'></a>

## Endnotes
¹http://es.mathworks.com/matlabcentral/fileexchange/39215.

<a id='b5adb763-f1d3-4183-8e9d-90b4aa8cab6d'></a>

²Tool available at http://www.mathworks.com/
matlabcentral/fileexchange/24042.

<!-- PAGE BREAK -->

<a id='6a011d9f-9aa9-46b2-bb0a-8697edd1afb2'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='7bf6f26f-d29c-407a-ab81-349480a70506'></a>

Page 18 of 19

<a id='7cc05c38-882b-4be7-b96c-2595daefee68'></a>

3 publicly available at http://sb2cl.ai2.upv.es/content/
software.

<a id='109823e1-96f2-4d88-9731-2cfec6927f4a'></a>

# Additional files

**Additional file 1:** additional. (1) I1-FFL model, Tables S1–S2; (2) 2. Matlab CODE (3) Supplementary Tables and Figures: Figure S1 – S4 and Table S3. (PDF 978 kb)

**Additional file 2:** matlabscripts.zip. Code source of the software explained in Additional file 1 (2. Matlab CODE). (ZIP 255 kb)

<a id='e845a20d-664b-4944-9a20-775fe065e916'></a>

**Competing interests**
The authors declare that they have no competing interests.

<a id='2be491d7-d581-4bbc-a495-6cdbd85f87c9'></a>

Authors' contributions
Conceived and designed experiments: YB, GRM, JP and AV. Performed the experiments: YB, GRM and AV. Analyzed the data: YB, GRM,JP and AV. Wrote the paper YB, GRM, JP and AV. All authors read and approved the manuscript.

<a id='ab037a11-4f2e-4706-a9e6-c5ff07cc4ea3'></a>

Acknowledgements
Research in this area is partially supported by Spanish government and European Union (FEDER-CICYT DPI2011-28112-C04-01, and DPI2014-55276-C5-1-R). Yadira Boada thanks grant FPI/2013-3242 of Universitat Politècnica de València; Gilberto Reynoso-Meza gratefully acknowledges the partial support provided by the postdoctoral fellowship BJT-304804/2014-2 from the National Council of Scientific and Technologic Development of Brazil (CNPq) for the development of this work.
We are grateful to Alejandra Gonzalez-Boscá for her collaboration on this topic while doing her Bachelor thesis, and to Dr. José Luis Pitarch from Universidad de Valladolid for his advise in algorithmic implementations and for proof reading the manuscript.

<a id='8a1d1492-ce72-4555-949f-8c508efca519'></a>

**Author details**

¹Institut d'Automàtica i Informàtica Industrial, Universitat Politècnica de València, Valencia, Spain.
²Industrial and Systems Engineering Graduate Program (PPGEPS), Pontificial Catholic University of Parana (PUCPR), Curitiba, Brazil.
³Present Address: Center for Systems Biology Dresden (CSBD), Max Planck Institute of Molecular Cell Biology and Genetics, Dresden, Germany.

<a id='8606ac22-750c-44da-a567-28ccbab13225'></a>

Received: 13 October 2015 Accepted: 16 February 2016
Published online: 11 March 2016

<a id='c2f5e27d-591b-4492-b390-f803cb2028db'></a>

# References
1. ERASynBio. Next steps for european synthetic biology: a strategic vision from erasynbio. Report, ERASynBio. 2014. https://www.erasynbio.eu/lw_resource/datapool/_items/item_58/erasynbiostrategicvision.pdf.
2. Way J, Collins J, Keasling J, Silver P. Integrating biological redesign: Where synthetic biology came from and where it needs to go. Cell. 2014;157(1):151-61.
3. Canton B, Labno A, Endy D. Refinement and standardization of synthetic biological parts and devices. Nat Biotechnol. 2008;26(7):787-93.
4. De Lorenzo V, Danchin A. Synthetic biology: discovering new worlds and new words. EMBO Rep. 2008;9(9):822-7.
5. Church GM, Elowitz MB, Smolke CD, Voigt CA, Weiss R. Realizing the potential of synthetic biology. Nat Rev Mol Cell Biol. 2014;15(4):289-94.
6. Takahashi CN, Miller AW, Ekness F, Dunham MJ, Klavins E. A low cost, customizable turbidostat for use in synthetic circuit characterization. ACS Synth Biol. 2015;4(1):32-8. doi:10.1021/sb500165g.
7. Cooling MT, Rouilly V, Misirli G, Lawson J, Yu T, Hallinan J, Wipat A. Standard virtual biological parts: a repository of modular modeling components for synthetic biology. Bioinformatics. 2010;26(7):925-31.
8. Medema MH, van Raaphorst R, Takano E, Breitling R. Computational tools for the synthetic design of biochemical pathways. Nat Rev Microbiol. 2012;10(3):191-202.
9. Marchisio MA, Stelling J. Automatic design of digital synthetic gene circuits. PLoS Comput Biol. 2011;7(2):e1001083. doi:10.1371/journal.pcbi.1001083.

<a id='fd77a519-b059-4662-8978-081e939bbccb'></a>

10. Rodrigo G, Carrera J, Landrain TE, Jaramillo A. Perspectives on the automatic design of regulatory systems for synthetic biology. FEBS Lett. 2012;586(15):2037-42.
11. Crook N, Alper HS. Model-based design of synthetic, biological systems. Chem Eng Sci. 2013;103:2-11.
12. Jayanthi S, Nilgiriwala K, Del Vecchio D. Retroactivity controls the temporal dynamics of gene transcription. ACS Synth Biol. 2013;2(8): 431-41.
13. Mélykúti B, Hespanha JP, Khammash M. Equilibrium distributions of simple biochemical reaction systems for time-scale separation in stochastic reaction networks. J R Soc Interface. 2014;11(97):20140054.
14. Oyarzún DA, Lugagne JB, Stan GB. Noise propagation in synthetic gene circuits for metabolic control. ACS Synth Biol. 2015;4(2):116-25. doi:10.1021/sb400126a.
15. Picó J, Vignoni A, Picó-Marco E, Boada Y. Modelado de sistemas bioquímicos: De la ley de acción de masas a la aproximación lineal del ruido. Revista Iberoamericana de Automática e Informática Industrial RIAI. 2015;12(3):241-52.
16. Feng X-j-J, Hooshangi S, Chen D, Li G, Weiss R, Rabitz H. Optimizing genetic circuits by global sensitivity analysis. Biophys J. 2004;87(4): 2195-202.
17. Dasika MS, Maranas CD. Optcircuit: An optimization based method for computational design of genetic circuits. BMC Syst Biol. 2008;2:24.
18. Rodrigo G, Carrera J, Jaramillo A. Genetdes. Bioinformatics. 2007;23(14): 1857-8.
19. Otero-Muras I, Banga JR. Multicriteria global optimization for biocircuit design. 2014. arXiv preprint arXiv:1402.7323.
20. Banga JR. Optimization in computational systems biology. BMC Syst Biol. 2008;2:47.
21. Sendin J, Exler O, Banga JR. Multi-objective mixed integer strategy for the optimisation of biological networks. IET Syst Biol. 2010;4(3):236-48.
22. Miller M, Hafner M, Sontag E, Davidsohn N, Subramanian S, Purnick PE, Lauffenburger D, Weiss R. Modular design of artificial tissue homeostasis: robust control through synthetic cellular heterogeneity. PLoS Comput Biol. 2012;8(7):1002579.
23. Ellis T, Wang X, Collins JJ. Diversity-based, model-guided construction of synthetic gene networks with predicted functions. Nat Biotechnol. 2009;27(5):465-71.
24. Koeppl H, Hafner M, Lu J. Mapping behavioral specifications to model parameters in synthetic biology. BMC Bioinforma. 2013;14(Suppl 10):9.
25. Chiang AWT, Hwang M-JJ. A computational pipeline for identifying kinetic motifs to aid in the design and improvement of synthetic gene circuits. BMC Bioinforma. 2013;14 Suppl 16:5.
26. Ma W, Trusina A, El-Samad H, Lim WA, Tang C. Defining network topologies that can achieve biochemical adaptation. Cell. 2009;138(4): 760-73.
27. Chiang AWT, Liu W-CC, Charusanti P, Hwang M-JJ. Understanding system dynamics of an adaptive enzyme network from globally profiled kinetic parameters. BMC Syst Biol. 2014;8:4.
28. Reynoso-Meza G, Blasco X, Sanchis J, Martínez M. Controller tuning using evolutionary multi-objective optimisation: current trends and applications. Control Eng Pract. 2014;28:58-73.
29. Alon U. An Introduction To Systems Biology. Design Principles of Biological Circuits. London: Chapman & Hall/ CRC Mathematical and computational Biology Series; 2006.
30. Elowitz MB, Leibler S. A synthetic oscillatory network of transcriptional regulators. Nature. 2000;403(6767):335-8.
31. Hsiao V, de los Santos ELC, Whitaker WR, Dueber JE, Murray RM. Design and implementation of a biomolecular concentration tracker. ACS Synth Biol. 2015;4(2):150-61. doi:10.1021/sb500024b.
32. Franco E, Giordano G, Forsberg P-O, Murray RM. Negative autoregulation matches production and demand in synthetic transcriptional networks. ACS Synth Biol. 2014;3(8):589-99. doi:10.1021/sb400157z.
33. Strelkowa N, Barahona M. Switchable genetic oscillator operating in quasi-stable mode. J R Soc Interface. 2010;7(48):1071-82.
34. Basu S, Mehreja R, Thiberge S, Chen MT, Weiss R. Spatiotemporal control of gene expression with pulse-generating networks. Proc Natl Acad Sci US A. 2004;101(17):6355-60.
35. Bleris L, Xie Z, Glass D, Adadey A, Sontag E, Benenson Y. Synthetic incoherent feedforward circuits show adaptation to the amount of their genetic template. Mol Syst Biol. 2011;7(519):1-12. doi:10.1038/msb.2011.49.

<!-- PAGE BREAK -->

<a id='fbbf4d5d-b9b1-4f2f-aa9f-695a9f6800da'></a>

Boada et al. BMC Systems Biology (2016) 10:27

<a id='b7a5a6d6-b81b-4645-87f5-a0166524bf48'></a>

Page 19 of 19

<a id='fefea246-eefb-40a7-88b5-3fa764dc0b5d'></a>

36. Hart Y, Antebi YE, Mayo AE, Friedman N, Alon U. Design principles of cell circuits with paradoxical components. Proc Natl Acad Sci. 2012;109(21):8346-51.
37. Zhang Q, Bhattacharya S, Andersen ME. Ultrasensitive response motifs: basic amplifiers in molecular signalling networks. Open Biol. 2013;3(4): 130031.
38. Weber M, Buceta J, Others. Dynamics of the quorum sensing switch: stochastic and non-stationary effects. BMC Syst Biol. 2013;7(1):6.
39. Womelsdorf T, Valiante TA, Sahin NT, Miller KJ, Tiesinga P. Dynamic circuit motifs underlying rhythmic gain control, gating and integration. Nat Neurosci. 2014;17(8):1031-9.
40. Arpino JAJ, Hancock EJ, Anderson J, Barahona M, Stan G-BVB, Papachristodoulou A, Polizzi K. Tuning the dials of synthetic biology. Microbiology. 2013;159(Pt 7):1236-53.
41. Zagaris A, Kaper HGG, Kaper TJJ. Analysis of the computational singular perturbation reduction method for chemical kinetics. J Nonlinear Sci. 2004;14(1):59-91.
42. Anderson J, Chang Y-C-C, Papachristodoulou A. Model decomposition and reduction tools for large-scale networks in systems biology. Automatica. 2011;47(6):1165-74.
43. Prescott TP, Papachristodoulou A. Layered decomposition for the model order reduction of timescale separated biochemical reaction networks. J Theor Biol. 2014;356:113-22.
44. Hancock EJ, Stan GB, Arpino JAJ, Papachristodoulou A. Simplified mechanistic models of gene regulation for analysis and design. J R Soc Interface. 2015;12(108):.
45. Miettinen K, Vol. 12. Nonlinear Multiobjective Optimization. Boston: Kluwer Academic Publishers; 1999.
46. Miettinen K, Ruiz F, Wierzbicki AP. Introduction to multiobjective optimization: interactive approaches. In: Multiobjective Optimization. Berlin: Springer; 2008. p. 27-57.
47. Deb K, Bandaru S, Greiner D, Gaspar-Cunha A, Tutum CC. An integrated approach to automated innovization for discovering useful design principles: Case studies from engineering. Appl Soft Comput. 2014;15(0): 42-56.
48. Ang J, Ingalls B, McMillen D. Probing the input-output behavior of biochemical and genetic systems: System identification methods from control theory In: Johnson ML, Brand L, editors. Methods in Enzymology. Academic Press; 2011. p. 279-317. doi:10.1016/8978-0-12-381270-4. 00010-X.
49. Mattson CA, Messac A. Pareto frontier based concept selection under uncertainty, with visualization. Optim Eng. 2005;6(1):85-115.
50. Reynoso-Meza G, Sanchis J, Blasco X, Martínez M. Design of continuous controllers using a multiobjective differential evolution algorithm with spherical pruning. Appl Evol Comput. 2010;532-541.
51. Reynoso-Meza G, García-Nieto S, Sanchis J, Blasco X. Controller tuning using multiobjective optimization algorithms: a global tuning framework. IEEE Trans Control Syst Technol. 2013;21(2):445-58.
52. Reynoso-Meza G, Sanchis J, Blasco X, Herrero JM. Multiobjective evolutionary algortihms for multivariable PI controller tuning. Expert Syst Appl. 2012;39:7895-907.
53. Anderson C. Anderson promoter collection [online]. 2006. http://parts. igem.org/Promoters/Catalog/Anderson. Accesed 20 Feb 2015.
54. Salis HM, Mirsky EA, Voigt CA. Automated design of synthetic ribosome binding sites to control protein expression. Nat Biotechnol. 2009;27(10): 946-50.
55. Egbert RG, Klavins E. Fine-tuning gene networks using simple sequence repeats. PNAS. 2012;109(42):16817-22. doi:10.1073/pnas.1205693109.
56. Hair JF, Suárez MG. Análisis Multivariante vol. 491. Madrid: Prentice Hall; 1999.
57. Blasco X, Herrero JM, Sanchis J, Martínez M. A new graphical visualization of n-dimensional pareto front for decision-making in multiobjective optimization. Inf Sci. 2008;178(20):3908-24. doi:10.1016/j.ins.2008.06.010.
58. Reynoso-Meza G, Blasco X, Sanchis J, Herrero JM. Comparison of design concepts in multi-criteria decision-making using level diagrams. Inform Sci. 2013;221:124-41.
59. Goentoro L, Shoval O, Kirschner MW, Alon U. The incoherent feedforward loop can provide fold-change detection in gene regulation. Mol Cell. 2009;36(5):894-9.

<a id='33c674da-e34a-4ef4-92ad-e1e15aa640eb'></a>

60. Rodrigo G, Elena SF. Structural discrimination of robustness in transcriptional feedforward loops for pattern formation. PloS ONE. 2011;6(2):16904.
61. Kim J, Khetarpal I, Sen S, Murray RM. Synthetic circuit for exact adaptation and fold-change detection. Nucleic Acids Res. 2014;42(2): 6078-89. doi:10.1093/nar/gku233.
62. Chelliah V, Juty N, Ajmera I, Ali R, Dumousseau M, Glont M, Hucka M, Jalowicki G, Keating S, Knight-Schrijver V, et al. Biomodels: ten-year anniversary. Nucleic Acids Res. 2015;43(D1):542-8.
63. Ang J, Bagh S, Ingalls BP, McMillen DR. Considerations for using integral feedback control to construct a perfectly adapting synthetic gene network. J Theor Biol. 2010;266(4):723-38.
64. Biobrick Foundation. 2006. Part Registry [online]. http://partsregistry.org/. Accessed 20 Feb 2015.
65. BIOSS. 2006. BIOSS Toolbox [online]. http://www.bioss.uni-freiburg.de/ cms/toolbox-home.html. Accessed 20 Feb 2015.
66. BioFab. 2006. International Open Facility Advancing Biotechnology [online]. http://www.biofab.org/. Accessed 20 Feb 2015.
67. Vallerio M, Hufkens J, Van Impe J, Logist F. An interactive decision-support system for multi-objective optimization of nonlinear dynamic processes with uncertainty. Expert Syst Appl. 2015;42(21):7710-31.
68. Frangopol DM, Maute K. Life-cycle reliability-based optimization of civil and aerospace structures. Comput Struct. 2003;81(7):397-410.
69. Lozano M, Molina D, Herrera F. Editorial scalability of evolutionary algorithms and other metaheuristics for large-scale continuous optimization problems. Soft Comput. 2011;15(11):2085-7.
70. Santana-Quintero LV, Montano AA, Coello CAC. A review of techniques for handling expensive functions in evolutionary multi-objective optimization. In: Computational Intelligence in Expensive Optimization Problems. Berlin: Springer; 2010. p. 29-59.

<a id='b89fb234-ae78-4a69-81c9-1918696a6ac7'></a>

Submit your next manuscript to BioMed Central
and we will help you at every step:

*   We accept pre-submission inquiries
*   Our selector tool helps you to find the most relevant journal
*   We provide round the clock customer support
*   Convenient online submission
*   Thorough peer review
*   Inclusion in PubMed and all major indexing services
*   Maximum visibility for your research

Submit your manuscript at
www.biomedcentral.com/submit
BioMed Central

# Supplementary materials

<a id='a9cd48d5-0dd0-47a7-a36d-d92299042c5e'></a>

Additional File 1☆

<a id='39361db0-6fc3-49e3-a238-6dbb5510158a'></a>

Yadira Boadaª, Gilberto Reynoso-Mezab, Jesús Picóª, Alejandro Vignonia,1

ªInstitut d'Automàtica i Informàtica Industrial, Universitat Politècnica de València, Valencia, Spain

bIndustrial and Systems Engineering Graduate Program (PPGEPS), Pontifical Catholic University of Parana (PUCPR), Curitiba, Brasil.

<a id='b655aaf8-3b85-477a-9768-0572be43707d'></a>

## Abstract
In this file there is all the additional information including: Model reduction, explanation of the Matlab code and additional tables and figure to help support the main paper.

<a id='d6a978b5-a045-4918-91b5-30f6e766f439'></a>

1. I1-FFL model

Next, a complete biochemical model of the I1-FFL gene regularoty network is derived, and its corresponding dynamical model based on balance equations and mass action kinetics is formulated. The biochemical reactions considered can be split in two main classes: the gene expression reactions, and the induction ones. In the gene expression block, the main processes considered for each of the three proteins are the binding of the RNA polymerase to the promoter, transcription, translation, mRNA degradation and protein degradation. In the induction part, the main processes considered are binding between the protein A and the inducer to form the monomer, monomer degradation, dimer formation and its degradation, addition of external inducer, diffusion of the inducer, inducer degradation, binding of the dimer to the gB promoter, binding of the dimer to the gC promoter, and binding between the activator (or repressor) and the gC hybrid promoter. The corresponding set of variables and corresponding symbols are shown in Table 1.
The resulting set of biochemical reactions is:

<a id='38843303-6109-4845-b855-e711aab6aa0a'></a>

☆ Boada et al. Obtaining model based guidelines for the design of synthetic devices using a multi-objective optimiza-tion framework. An adaptive network case
¹Actual affiliation is Center for Systems Biology Dresden (CSBD), Max Planck Institute of Molecular Cell Biology and Genetics, Pfotenhauerstr. 108, 01307 Dresden, Germany

<!-- PAGE BREAK -->

<a id='12f0e4e7-6188-40a2-9e0a-2f1812e97af4'></a>

Table S 1. List of variables in the complete model.
<table id="1-1">
<tr><td id="1-2">Variable</td><td id="1-3">Description</td><td id="1-4">Units</td><td id="1-5">Symbol</td></tr>
<tr><td id="1-6">X1</td><td id="1-7">DNA promoter gene A</td><td id="1-8">nM</td><td id="1-9">gA</td></tr>
<tr><td id="1-a">X2</td><td id="1-b">RNA polymerase</td><td id="1-c">nM</td><td id="1-d">RNAp</td></tr>
<tr><td id="1-e">X3</td><td id="1-f">gA·RNAp complex</td><td id="1-g">nM</td><td id="1-h">gA·RNAp</td></tr>
<tr><td id="1-i">X4</td><td id="1-j">messenger RNA for gene A</td><td id="1-k">nM</td><td id="1-l">mA</td></tr>
<tr><td id="1-m">X5</td><td id="1-n">A protein</td><td id="1-o">nM</td><td id="1-p">A</td></tr>
<tr><td id="1-q">X6</td><td id="1-r">Intracellular inducer</td><td id="1-s">nM</td><td id="1-t">I</td></tr>
<tr><td id="1-u">X7</td><td id="1-v">A·I monomer</td><td id="1-w">nM</td><td id="1-x">A·I</td></tr>
<tr><td id="1-y">X8</td><td id="1-z">(A·I)2 dimer</td><td id="1-A">nM</td><td id="1-B">(A·I)2</td></tr>
<tr><td id="1-C">X9</td><td id="1-D">DNA promoter gene B</td><td id="1-E">nM</td><td id="1-F">gB</td></tr>
<tr><td id="1-G">X10</td><td id="1-H">gB(A·I)2 complex</td><td id="1-I">nM</td><td id="1-J">gB(A·I)2</td></tr>
<tr><td id="1-K">X11</td><td id="1-L">DNA promoter gene C</td><td id="1-M">nM</td><td id="1-N">gC</td></tr>
<tr><td id="1-O">X12</td><td id="1-P">gC(A·I)2 complex</td><td id="1-Q">nM</td><td id="1-R">gC(A·I)2</td></tr>
<tr><td id="1-S">X13</td><td id="1-T">gC·B complex</td><td id="1-U">nM</td><td id="1-V">gC·B</td></tr>
<tr><td id="1-W">X14</td><td id="1-X">gC·B(A·I)2 complex</td><td id="1-Y">nM</td><td id="1-Z">gC·B(A·I)2</td></tr>
<tr><td id="1-10">X15</td><td id="1-11">gB(A·I)2RNAp complex</td><td id="1-12">nM</td><td id="1-13">gB(A·I)2RNAp</td></tr>
<tr><td id="1-14">X16</td><td id="1-15">messenger RNA for gene B</td><td id="1-16">nM</td><td id="1-17">mB</td></tr>
<tr><td id="1-18">X17</td><td id="1-19">B protein</td><td id="1-1a">nM</td><td id="1-1b">B</td></tr>
<tr><td id="1-1c">X18</td><td id="1-1d">messenger RNA for gene C</td><td id="1-1e">nM</td><td id="1-1f">mC</td></tr>
<tr><td id="1-1g">X19</td><td id="1-1h">C protein</td><td id="1-1i">nM</td><td id="1-1j">C</td></tr>
<tr><td id="1-1k">X20</td><td id="1-1l">Extracellular inducer</td><td id="1-1m">nM</td><td id="1-1n">le</td></tr>
</table>

<a id='66cf45e0-ddaf-4232-9688-56a7fe0e8b43'></a>

<::
gA + RNAP <img src="/k1_k-1_equilibrium_arrow.png" alt="k1 above, k-1 below, equilibrium arrows"> gA·RNAP

gA·RNAP <img src="/kmA_arrow.png" alt="kmA above arrow"> gA + RNAP + mA

mA <img src="/kPA_arrow.png" alt="kPA above arrow"> mA + A

mA <img src="/dmA_arrow.png" alt="dmA above arrow"> Ø

A <img src="/dA_arrow.png" alt="dA above arrow"> Ø

A + I <img src="/k2_k-2_equilibrium_arrow.png" alt="k2 above, k-2 below, equilibrium arrows"> AI

Ø <img src="/ke_arrow.png" alt="ke above arrow"> Ie

Ie <img src="/kd_kd_equilibrium_arrow.png" alt="kd above, kd below, equilibrium arrows"> I

I <img src="/dI_arrow.png" alt="dI above arrow"> Ø

2(AI) <img src="/k3_k-3_equilibrium_arrow.png" alt="k3 above, k-3 below, equilibrium arrows"> (AI)2

(AI) <img src="/dAI_arrow.png" alt="dAI above arrow"> Ø

(AI)2 <img src="/dAI2_arrow.png" alt="dAI2 above arrow"> Ø
: figure::>

<a id='31174320-54db-4e01-9ebf-4aa15b20afef'></a>

gene A:

<!-- PAGE BREAK -->

<a id='e67387ed-8f34-4df2-9d7e-08d83f070673'></a>

gene B:

<::
gB + (AI)₂ <=> k₄ / k₋₄ gB·(AI)₂

gB·(AI)₂ + RNAp <=> k₇ / k₋₇ gB·(AI)₂·RNAP

gB·(AI)₂·RNAP → kmB gB·(AI)₂ + RNAp + mB

mB → kpB mB + B

mB → dmB ∅

B → dB ∅
: chart::>

<a id='06a072ca-a796-4605-89f6-36752e04264a'></a>

gene C:

<::gC + (AI)₂ \xrightarrow{k₅} gC·(AI)₂
\xleftarrow{k₋₅}

gC·B + (AI)₂ \xrightarrow{k₆} gC·B·(AI)₂
\xleftarrow{k₋₆}

gC·(AI)₂ + B \xrightarrow{k₈} gC·B·(AI)₂
\xleftarrow{k₋₈}

gC + B \xrightarrow{k₉} gC·B
\xleftarrow{k₋₉}

gC·(AI)₂ + RNAp \xrightarrow{k₁₀} gC·(AI)₂·RNAp
\xleftarrow{k₋₁₀}

gC·(AI)₂·RNAp \xrightarrow{k_{mC}} gC·(AI)₂ + RNAp + mC

mC \xrightarrow{k_{PC}} mC + C

mC \xrightarrow{d_{mC}} \emptyset

C \xrightarrow{d_C} \emptyset
: figure::>

<a id='aae5c7f7-bc80-4cc6-bd0d-9da21289ca7a'></a>

Note: the empty set Ø denotes species degradation when placed in the right hand side of a reaction.

<a id='8227937e-945c-4146-b2a8-233d97338585'></a>

Notice we assume that binding between the activating dimer and the gC hybrid promoter is always possible, even if the repressor B is already bound to the promoter, and vice versa. Yet, we consider that whenever the repressor B is bound to the promoter gC, the RNA polymerase cannot bind the promoter.

<a id='3dfa6387-384e-41a3-ac8d-31daafbf887b'></a>

Using the law of mass-action kinetics (Horn and Jackson, 1972; Chellaboina et al., 2009), the previous reactions can be used to formulate the corresponding dynamic balances of the species

<a id='446b0287-501a-4ad1-8cf3-8df3785f623e'></a>

3

<!-- PAGE BREAK -->

<a id='99feeb22-925d-466f-9850-53a9f67bcfba'></a>

concentrations:

x_1 = -k_1 x_1 x_2 + k_{-1} x_3 + k_{mA} x_3
x_2 = -k_1 x_1 x_2 + k_{-1} x_3 + k_{mA} x_3 - k_7 x_{10} x_2 + k_{-7} x_{15} + k_{mB} x_{15}
x_3 = k_1 x_1 x_2 - k_{-1} x_3 - k_{mA} x_3
x_4 = k_{mA} x_3 - d_{mA} x_4
x_5 = k_{pA} x_4 - d_A x_5 - k_2 x_5 x_6 + k_{-2} x_7
x_6 = -k_2 x_5 x_6 + k_{-2} x_7 + k_d x_{20} - k_d x_6 - d_I x_6
x_7 = k_2 x_5 x_6 - k_{-2} x_7 - 2k_3 x_7^2 + 2k_{-3} x_8 - d_{AI} x_7
x_8 = k_3 x_7^2 - k_{-3} x_8 - k_4 x_8 x_9 + k_{-4} x_{10} - k_5 x_8 x_{11} + k_{-5} x_{12} - k_6 x_8 x_{13} + k_{-6} x_{14} - d_{AI2} x_8
x_9 = -k_4 x_9 x_8 + k_{-4} x_{10}
x_{10} = k_4 x_9 x_8 - k_{-4} x_{10} - k_7 x_{10} x_2 + k_{-7} x_{15} + k_{mB} x_{15}
x_{11} = -k_9 x_{11} x_{17} + k_{-9} x_{13} - k_5 x_{11} x_8 + k_{-5} x_{12}
x_{12} = k_5 x_{11} x_8 - k_{-5} x_{12} - k_8 x_{12} x_{17} + k_{-8} x_{14}
x_{13} = k_9 x_{11} x_{17} - k_{-9} x_{13} - k_6 x_{13} x_8 + k_{-6} x_{14}
x_{14} = k_6 x_{13} x_8 - k_{-6} x_{14} + k_8 x_{12} x_{17} - k_{-8} x_{14}
x_{15} = k_7 x_{10} x_2 - k_{-7} x_{15} - k_{mB} x_{15}
x_{16} = k_{mB} x_{15} - d_{mB} x_{16}
x_{17} = k_{pB} x_{16} - d_B x_{17} - k_9 x_{11} x_{17} + k_{-9} x_{13} - k_8 x_{12} x_{17} + k_{-8} x_{14}
x_{18} = k_{mC} x_{12} - d_{mC} x_{18}
x_{19} = k_{pC} x_{18} - d_C x_{19}
x_{20} = k_d x_6 - k_d x_{20} - d_I x_{20}

<a id='385008bb-fdba-4d90-8397-563768c39fdc'></a>

Note these equations can be derived either by inspection, or using specific software to automate the process. Software packages like BioNetGen (Blinov et al., 2004) or COPASI (Mendes et al., 2009) allow to obtain the dynamic kinetic model from either the set of reactions or from SBML files encoding them.

<a id='ae5f3124-c88d-42dd-a15a-71ed85cb6759'></a>

The complete model is of large order, which implies a high computational cost for the param- eters estimation process that will be carried out later on. Moreover, the large differences in the time scales among the different species in the synthetic gene network (typically many orders of magnitude) originate huge difficulties for simulating the temporal evolution of the network and for understanding the basic principles of its operation. Therefore, the dynamical model will be reduced using time-scale separation and detection of invariant moieties.

<a id='e4081916-5942-486c-a342-31d037533e54'></a>

We apply the _Quasi Steady-State Approximation_ (QSSA) to the fast chemical species (Zagaris
et al., 2004; Mélykúti et al., 2014). In essence QSSA is a singular perturbation method that
considers the time-scale separation among the different dynamics. In particular, we will assume
that binding reactions occur very fast in comparison with those corresponding to transcription,
translation or even genuine degradation. On the other hand, monomer formation is faster that
dimerization Therefore, the differential equation corresponding to the AI complex formation
will be assumed to be at steady state.

<a id='ea86c7b8-deb5-4573-87cb-d90c53e2b3b3'></a>

Additional algebraic relationships among variables can be obtained through _system invari_-
ants. In the case of reaction networks, it can be observed that some reactions are a linear combi-

<a id='44fbd224-de65-45e7-a83a-71c1435dfc5e'></a>

4

<!-- PAGE BREAK -->

<a id='83b9d881-aa67-4b8b-a16f-adc5bfbce959'></a>

Table S 2. List of variables used in the reduced model.
<table id="4-1">
<tr><td id="4-2">Variable</td><td id="4-3">Description</td><td id="4-4">Units</td><td id="4-5">Symbol</td></tr>
<tr><td id="4-6">x₁</td><td id="4-7">mRNAgA</td><td id="4-8">nM</td><td id="4-9">mA</td></tr>
<tr><td id="4-a">x₂</td><td id="4-b">A protein</td><td id="4-c">nM</td><td id="4-d">A</td></tr>
<tr><td id="4-e">x₃</td><td id="4-f">Inducer</td><td id="4-g">nM</td><td id="4-h">I</td></tr>
<tr><td id="4-i">M</td><td id="4-j">A·I monomer</td><td id="4-k">nM</td><td id="4-l">A·I</td></tr>
<tr><td id="4-m">X4</td><td id="4-n">(A•I)2 dimer</td><td id="4-o">nM</td><td id="4-p">(A•I)2</td></tr>
<tr><td id="4-q">X5</td><td id="4-r">mRNAgB</td><td id="4-s">nM</td><td id="4-t">mB</td></tr>
<tr><td id="4-u">X6</td><td id="4-v">B protein</td><td id="4-w">nM</td><td id="4-x">B</td></tr>
<tr><td id="4-y">X7</td><td id="4-z">mRNAgC</td><td id="4-A">nM</td><td id="4-B">mC</td></tr>
<tr><td id="4-C">X8</td><td id="4-D">C protein</td><td id="4-E">nM</td><td id="4-F">C</td></tr>
<tr><td id="4-G">X9</td><td id="4-H">External I ext</td><td id="4-I">nM</td><td id="4-J">Ie</td></tr>
</table>

<a id='af6c602c-09cd-47d7-a80c-7d0ab1352325'></a>

nation of other ones. Then, the linear combination of the concentrations of the species involved will keep constant in time. These linear combinations, so called moieties, can be understood as a kind of quasi-species that keep invariant, i.e. keep constant concentration.

<a id='551f3dbd-0d06-4420-bf23-8e29cf7fa233'></a>

After the reduction, ommited here, we get a system of nine ordinary differential equations
(each one corresponding to the dynamics of one of the species) plus an algebraic equation, and
26 model parameters that will be the decision variables at the the optimization step. The resulting
model is:

<a id='7cbeaf05-a4ae-4c25-821f-dc9ac09111f3'></a>

$\dot{x}_1 = k_{mA}C_{gA} - d_{mA}x_1$ (1)
$\dot{x}_2 = k_{pA}x_1 - d_Ax_2 - k_2x_2x_3 + k_{-2}M$ (2)
$\dot{x}_3 = -k_2x_2x_3 + k_{-2}M + k_dx_9 - k_dx_3 - d_Ix_3$ (3)
$\dot{x}_4 = k_3M^2 - 2k_{-3}x_4 - d_{AI2}x_4$ (4)
$\dot{x}_5 = K_{mB}C_{gB}\frac{x_4}{\theta_1 + x_4} - d_{mB}x_5$ (5)
$\dot{x}_6 = k_{pB}x_5 - d_Bx_6$ (6)
$\dot{x}_7 = K_{mC}C_{gC}\frac{x_4 + \beta_1x_6 + \beta_2x_4x_6}{\theta_2 + \theta_3x_4 + \theta_4x_6 + \theta_5x_4x_6} - d_{mC}x_7$ (7)
$\dot{x}_8 = k_{pC}x_7 - d_Cx_8$ (8)
$\dot{x}_9 = -k_dx_9 + k_dx_3 - d_{Ie}x_9$ (9)

<a id='e05a9d52-8383-4bc7-9a61-cb258ee24b98'></a>

with $M = -\frac{d_{AI} + k_{-2}}{2k_3} + \frac{1}{2k_3} \sqrt{(d_{AI} + k_{-2})^2 + 4k_3(k_2x_2x_3 + 2k_{-3}x_4)}$.
The resulting set of biochemical reactions corresponding to the reduced model is:

<a id='8d121de3-ab40-4cd9-bacb-ca6b80b550e9'></a>

5

<!-- PAGE BREAK -->

<a id='98397395-cb3d-44ba-b1fd-2920149fab77'></a>

gene A:

<::
0 --(f_A)--> + mA
mA --(k_pA)--> mA + A
mA --(d_mA)--> 0
A --(d_A)--> 0
2A + 2I <--(k_2M)/(2k-3)--> (AI)_2
0 --(k_e)--> Ie
Ie <--(k_d)/(k_d)--> I
I --(d_I)--> 0
(AI)_2 --(d_AI2)--> 0
: figure::>

<a id='06650036-d901-42c5-b3e0-e52bdf83b6c1'></a>

gene B:

<::
0 --(fB)--> mB
mB --(kPB)--> mB + B
mB --(dmB)--> 0
B --(dB)--> 0
: figure::>

<a id='3816554d-10b3-4546-bdd7-30ec0536f5fa'></a>

gene C:

0 \xrightarrow{f_c} + mC
mC \xrightarrow{k_{pC}} mC + C
mC \xrightarrow{d_{mC}} \emptyset
C \xrightarrow{d_C} \emptyset

<a id='d33247a4-4489-4e6e-bcdb-6b843f08cfd7'></a>

Where $f_A$, $f_B$, and $f_C$ are the lumped propensities obtained from the reduction:

$f_A = K_{mA}C_{gA}$, (10)

$f_B = K_{mB}C_{gC} \frac{x_4}{\theta_1 + x_4}$, (11)

$f_C = K_{mC}C_{gC} \frac{x_4 + \beta_1x_6 + \beta_2x_4x_6}{\theta_2 + \theta_3x_4 + \theta_4x_6 + \theta_5x_4x_6}$, (12)

<!-- PAGE BREAK -->

<a id='4fe1865b-15e5-4de9-b296-494d03e21a18'></a>

## 2. Matlab CODE

A short description of the main functions integrating this code and justification of the value sets is given below. It has been divided in two groups: files related to the model computational characterization, and files used by the optimizer, which link to the first set.

Model code

*   _model_3genes.m_ is a function for the ODEs of the reduced model. Receives the value of the state vector _x_ at time _t_, the parameters, initial conditions and time point; and returns a vector with the derivatives defined in it. When used with the command ode23s in the function _objective_func.m_ one obtains the solution of the ODEs system for the given parameters.

*   _objective_func.m_ is the objective function. It receives the parameters and returns the **objectives values vector**, after calculating J₁ and J₂ for the corresponding dynamic response obtained with the given parameters.

The 14 variables are initialized, and the 10 parameters are not because the optimizer will work with a given range in its code.

The ode23s algorithm gives the variables values Y for each t, using _model_3genes.m_. This _ode_ algorithm was selected because our system model is what it is known as _stiff_, in terms of the numerical solution of ordinary differential equations, i.e. it has both slow and fast dynamics. An ordinary differential equation problem is stiff if the solution being sought is varying slowly, but there are nearby solutions that vary rapidly, so the numerical method must take small steps to obtain satisfactory results. For our integration problem we use an absolute tolerance of 1e-8, and a relative tolerance of 1e-6.

For computational simulation, we start from the equilibrium initial conditions (precomputed) and give a jump of 50nM to the concentration of x9 to simulate the induction. With respect to the simulation parameters, the simulation sampling time (Ts) was fixed to 1e-3 minutes, and a total simulation time _Tsim_ = 300 minutes was used.

*   _eval_obj_fun.m_ is the function that receive a population of parameters, evaluates the objective functions in this population, and accumulates the results in a matrix to return it. It is executed at each iteration of the sp-MODE algorithm.

<a id='3e996b29-e653-4a2a-88d2-188ada965c5d'></a>

MOO code
First, highlight that we use the script *Tutorial.m* to run all the functions used to obtain the results shown in the main paper.

<a id='03d94b78-c21f-4bc4-a696-90051e4fba3b'></a>

The first step is to run the *spMODEparam* file to build the variable 'spMODEDat' with the variables required for the optimization. Here the number of objectives are defined, also the number of decision variables and the 'Cost Function', which brings the objectives matrix after previous *ode* simulations (by means of interlinked functions mentioned above, constituting in essence the problem 'nucleus' or characterization). The field of search, and bounds to improve pertinency of solutions in the objective space so as to cut solutions with no interest to the DM, are defined here too. Also other aspects, such as maximum Pareto optimal solutions required and a bound on the number of function evaluations.

<a id='507433fb-24fb-49f9-a0f8-35adc484c905'></a>

Once the Pareto set and the Pareto front are found by the optimizer, results can be plot with optional features through the _Leveltool_. This tool provides the LD visualization for the MCDM.

<a id='b7f7ea22-c133-49e5-b6e6-86a63b9cc829'></a>

7

<!-- PAGE BREAK -->

<a id='fb44a92c-57f0-4202-97ad-7ab87b2e5e84'></a>

 * _spMODEparam.m_ generates the required parameters to run the spMODE optimization algorithm.
In this file the variables regarding the multi-objective problem are defined. The values of interest for our problem are:

1. Number of objectives.
   spMODEDat.NOBJ = 2
2. Number of decision variables.
   spMODEDat.NVAR = 10
3. Cost Function.
   spMODEDat.mop = str2func('CostFunction')
4. Problem Instance.
   spMODEDat.CostProblem = 'modelo3genes'
5. Maximum and minimum values for the parameters or decision variables are fixed in order to give a range to the optimizer to search the optimal solutions, (spMODEDat.FieldD). k_d and d_l were fixed to avoid the optimizer to modify the model input I_e, as we want an step input determined by K_e(t).
6. Bounds on objectives.
   spMODEDat.Pertinency=[ 1e-3 200; 1e-4 20]; A row for each objective, with the minimum and maximum values desired.

<a id='920d0d9c-d647-44d5-9e09-a9e92778f311'></a>

• *CostFunction.m* calls the cost function of your own multi-objective problem. In this case
*eval_obj_fun.m*. It also includes a default mechanism to improve pertinency (Objective
space bounded).

<a id='4bf8d819-80db-4325-8e60-468fa1772f52'></a>

*Clustering and Visualization*

*   **clustering.m** is a script that performs the hierarchical clustering with the solutions obtained from the **spMODE** optimization algorithm, and uses the modified **LD-tool** to plot the LD plots with the cluster number as **Y-axis**.

<a id='7315fb0f-4bda-43c0-bb4f-3af98790b8b6'></a>

_Computational cost._ Execution of our MOO using the sp-MODE algorithm (15.000 evaluations of the objective function) took around 10 hours and 25 minutes and was performed in a Intel XEON Server with 12 cores and 32 Gb of RAM Memory.

<a id='6cf17539-4f56-4fae-982b-413b22d8379d'></a>

8

<!-- PAGE BREAK -->

<a id='a216aa9e-aafd-4429-beea-2e8c7a1ef0ee'></a>

3. Supplementary Tables and Figures

<a id='9e9d2d6c-aac5-4e88-9679-df24df770468'></a>

<::chart: A figure containing three plots. The top plot shows a Pareto front with J2 (J2 Units) on the y-axis (0 to 4) and J1 (J1 Units) on the x-axis (0 to 4). Diamond-shaped points form a curve, labeled "Pareto front points". "Extreme point Y" is at (0, 4), "Extreme point X" is at (4, 0). "Point A" is approximately at (1, 1) and "Point B" is approximately at (3.2, 0.5). The bottom-left plot shows ||J(θ)||1 on the y-axis (0 to 1) and J1(θ) : [J1(θ) units] on the x-axis (0 to 4). Diamond-shaped points form a U-shaped curve. "Extreme Point X" is at (4, 1), "Extreme Point Y" is at (0, 1). "Point B" is approximately at (3.2, 0.8) and "Point A" is approximately at (1.6, 0.45). The bottom-right plot shows ||J(θ)||1 on the y-axis (0 to 1) and J2(θ) : [J2(θ) units] on the x-axis (0 to 4). Diamond-shaped points form a U-shaped curve. "Extreme Point X" is at (0, 1), "Extreme Point Y" is at (4, 1). "Point B" is approximately at (0.5, 0.8) and "Point A" is approximately at (2.2, 0.45). Figure S 1. Example of Level Diagram for a bi-objective Pareto front and set.::>

<a id='da3d0054-a726-416c-9b71-e75734b81d08'></a>

9

<!-- PAGE BREAK -->

<a id='a453d546-6fa3-47a8-a6b7-1201604cc5ed'></a>

<::A figure showing two plots. The main plot is a scatter plot with a line connecting blue circular markers. The x-axis is labeled J1 and ranges from 10^-3 to 10^2 on a logarithmic scale. The y-axis is labeled J2 and ranges from 10^-3 to 10^2 on a logarithmic scale. The line connects a series of blue dots, and there are additional scattered dots in lighter shades of blue and purple. Inset plot: A smaller plot is embedded in the top left corner of the main plot. This inset plot shows multiple decaying curves. The y-axis is labeled "Protein C concentration" and ranges from 0 to 15. The x-axis is labeled "time [min]" and ranges from 0 to 300.::>10

<a id='5d7d9c90-e56d-433f-bec1-800bf15d0175'></a>

Figure S 2. Pareto Front in blue line connected dots. Dots changing from blue to light blue are obtained by changing the degradation rate of protein C represented by $d_c \in [0.30.10.03 0.01]$ starting at the extreme solution. Notice, that decreasing $d_c$ lead to a complete lose of optimality and moreover of the adaptation behavior, as we can see in the temporal profile of the protein C concentration in the inset.

<!-- PAGE BREAK -->

<a id='a81145f2-c954-440d-9b0d-ba41974155d6'></a>

<::Two scatter plots are presented, each showing data points in blue and red. Both plots share a linear y-axis labeled "||J(θ)||₂" ranging from 0 to 1. Both plots also share a logarithmic x-axis ranging from 10⁻³ to 10².  Top Plot:  - X-axis: "J₂ (θ)".  - Blue points: Generally decrease from ||J(θ)||₂ = 1 towards 0 as J₂(θ) increases.  - Red points: Show a curve that increases from low ||J(θ)||₂ values, peaks around J₂(θ) = 10⁰, and then decreases.  Bottom Plot:  - X-axis: "J₁ (θ)".  - Blue points: Generally decrease from ||J(θ)||₂ = 1 towards 0 as J₁(θ) increases.  - Red points: Show a curve that increases from low ||J(θ)||₂ values, peaks around J₁(θ) = 10⁰, and then decreases. : chart::> 11

<a id='7a545e23-e6f8-48f0-a2e0-36a37ddea16c'></a>

Figure S 3. Pareto Front as the distance to ideal point. J₁(θ) is the sensitivity and J₂(θ) is the precision objectives. Cluster 1 is plotted in red circles and cluster 2 is plotted in blue circles.

<!-- PAGE BREAK -->

<a id='a8f9d02a-31a7-45ab-a020-89aedeafc010'></a>

<::Multiple scatter plots arranged in a 3x3 grid, showing the relationship between || J(θ) ||₂ (y-axis) and various parameters (x-axis). Each plot contains blue and red circular data points. The y-axis ranges from 0 to 1 for all plots.

Top row:
- Plot 1 (left): x-axis is γ₁ from 0 to 200.
- Plot 2 (center): x-axis is kpB from 0 to 100.
- Plot 3 (right): x-axis is KmcCgC from 0 to 200.

Middle row:
- Plot 4 (left): x-axis is dB from 0 to 0.3.
- Plot 5 (center): x-axis is γ₄ from 0 to 5.
- Plot 6 (right): x-axis is γ₅ from 0 to 100.

Bottom row:
- Plot 7 (left): x-axis is KmBCgB from 0 to 200.
- Plot 8 (center): x-axis is γ₃ from 0 to 0.4.
- Plot 9 (right): x-axis is dc from 0 to 0.3.

Note: The y-axis label || J(θ) ||₂ is shown twice at the bottom of the left and middle columns, and the x-axis label kpC from 0 to 100 is shown next to the last plot, which should be kpc. The layout suggests a 3x3 grid of plots. The x-axis labels are positioned vertically. One x-axis label, kpC, is misplaced next to the last plot, which should be dc.
: chart::>
12

<a id='d34f3929-9273-4016-8fb5-fd6a413bc29d'></a>

Figure S 4. Pareto set of decision variables. Each parameter of the model was plotted according its distance to ideal point. Red circles represent the cluster 1 and blue circles allow to the cluster 2.

<!-- PAGE BREAK -->

<a id='74b75af3-c949-40c5-8050-e64a46da793e'></a>

Table S 3. Solutions obtained from the MOO. Columns are values for the design objectives and parameters. Rows are the solutions obtained.
<table id="12-1">
<tr><td id="12-2">Solution</td><td id="12-3">J₁</td><td id="12-4">J₂</td><td id="12-5">KmCgC</td><td id="12-6">KmBgB</td><td id="12-7">d_B</td><td id="12-8">d_C</td><td id="12-9">\u03b3_1</td><td id="12-a">\u03b3_3</td><td id="12-b">\u03b3_4</td><td id="12-c">γ5</td><td id="12-d">kpB</td><td id="12-e">kpC</td></tr>
<tr><td id="12-f">1</td><td id="12-g">0.00</td><td id="12-h">12.53</td><td id="12-i">104.09</td><td id="12-j">1.00</td><td id="12-k">0.02</td><td id="12-l">0.28</td><td id="12-m">107.41</td><td id="12-n">0.01</td><td id="12-o">1.15</td><td id="12-p">8.56</td><td id="12-q">1.00</td><td id="12-r">11.43</td></tr>
<tr><td id="12-s">2</td><td id="12-t">0.00</td><td id="12-u">7.72</td><td id="12-v">84.06</td><td id="12-w">1.00</td><td id="12-x">0.02</td><td id="12-y">0.28</td><td id="12-z">193.06</td><td id="12-A">0.00</td><td id="12-B">1.44</td><td id="12-C">9.25</td><td id="12-D">1.00</td><td id="12-E">8.66</td></tr>
<tr><td id="12-F">3</td><td id="12-G">0.00</td><td id="12-H">4.04</td><td id="12-I">47.71</td><td id="12-J">1.00</td><td id="12-K">0.01</td><td id="12-L">0.30</td><td id="12-M">200.00</td><td id="12-N">0.00</td><td id="12-O">1.25</td><td id="12-P">1.00</td><td id="12-Q">1.00</td><td id="12-R">5.93</td></tr>
<tr><td id="12-S">4</td><td id="12-T">0.00</td><td id="12-U">3.76</td><td id="12-V">53.93</td><td id="12-W">1.00</td><td id="12-X">0.01</td><td id="12-Y">0.30</td><td id="12-Z">170.42</td><td id="12-10">0.00</td><td id="12-11">0.38</td><td id="12-12">1.00</td><td id="12-13">1.00</td><td id="12-14">5.08</td></tr>
<tr><td id="12-15">5</td><td id="12-16">0.00</td><td id="12-17">3.38</td><td id="12-18">41.92</td><td id="12-19">1.00</td><td id="12-1a">0.01</td><td id="12-1b">0.30</td><td id="12-1c">188.31</td><td id="12-1d">0.00</td><td id="12-1e">1.17</td><td id="12-1f">1.00</td><td id="12-1g">1.00</td><td id="12-1h">5.68</td></tr>
<tr><td id="12-1i">6</td><td id="12-1j">0.00</td><td id="12-1k">2.91</td><td id="12-1l">21.52</td><td id="12-1m">1.00</td><td id="12-1n">0.01</td><td id="12-1o">0.30</td><td id="12-1p">176.89</td><td id="12-1q">0.00</td><td id="12-1r">0.00</td><td id="12-1s">1.00</td><td id="12-1t">1.00</td><td id="12-1u">9.44</td></tr>
<tr><td id="12-1v">7</td><td id="12-1w">0.00</td><td id="12-1x">2.48</td><td id="12-1y">171.91</td><td id="12-1z">1.00</td><td id="12-1A">0.01</td><td id="12-1B">0.29</td><td id="12-1C">185.33</td><td id="12-1D">0.00</td><td id="12-1E">0.00</td><td id="12-1F">1.00</td><td id="12-1G">1.00</td><td id="12-1H">1.00</td></tr>
<tr><td id="12-1I">8</td><td id="12-1J">0.00</td><td id="12-1K">1.68</td><td id="12-1L">101.48</td><td id="12-1M">1.00</td><td id="12-1N">0.01</td><td id="12-1O">0.30</td><td id="12-1P">200.00</td><td id="12-1Q">0.00</td><td id="12-1R">0.57</td><td id="12-1S">1.00</td><td id="12-1T">1.00</td><td id="12-1U">1.15</td></tr>
<tr><td id="12-1V">9</td><td id="12-1W">0.00</td><td id="12-1X">1.41</td><td id="12-1Y">103.74</td><td id="12-1Z">1.00</td><td id="12-20">0.01</td><td id="12-21">0.30</td><td id="12-22">163.00</td><td id="12-23">0.00</td><td id="12-24">0.00</td><td id="12-25">1.00</td><td id="12-26">1.00</td><td id="12-27">1.00</td></tr>
<tr><td id="12-28">10</td><td id="12-29">0.00</td><td id="12-2a">0.98</td><td id="12-2b">77.26</td><td id="12-2c">1.00</td><td id="12-2d">0.01</td><td id="12-2e">0.30</td><td id="12-2f">120.21</td><td id="12-2g">0.00</td><td id="12-2h">0.00</td><td id="12-2i">1.00</td><td id="12-2j">1.00</td><td id="12-2k">1.00</td></tr>
<tr><td id="12-2l">11</td><td id="12-2m">0.01</td><td id="12-2n">0.64</td><td id="12-2o">47.90</td><td id="12-2p">1.00</td><td id="12-2q">0.01</td><td id="12-2r">0.30</td><td id="12-2s">149.24</td><td id="12-2t">0.00</td><td id="12-2u">0.00</td><td id="12-2v">1.00</td><td id="12-2w">1.00</td><td id="12-2x">1.00</td></tr>
<tr><td id="12-2y">12</td><td id="12-2z">0.02</td><td id="12-2A">0.24</td><td id="12-2B">1.00</td><td id="12-2C">1.00</td><td id="12-2D">0.01</td><td id="12-2E">0.30</td><td id="12-2F">191.70</td><td id="12-2G">0.00</td><td id="12-2H">0.00</td><td id="12-2I">1.00</td><td id="12-2J">1.00</td><td id="12-2K">15.68</td></tr>
<tr><td id="12-2L">13</td><td id="12-2M">0.14</td><td id="12-2N">0.03</td><td id="12-2O">1.00</td><td id="12-2P">1.00</td><td id="12-2Q">0.01</td><td id="12-2R">0.30</td><td id="12-2S">200.00</td><td id="12-2T">0.00</td><td id="12-2U">0.00</td><td id="12-2V">1.00</td><td id="12-2W">1.00</td><td id="12-2X">1.80</td></tr>
<tr><td id="12-2Y">14</td><td id="12-2Z">0.99</td><td id="12-30">0.01</td><td id="12-31">1.00</td><td id="12-32">1.17</td><td id="12-33">0.08</td><td id="12-34">0.30</td><td id="12-35">165.00</td><td id="12-36">0.00</td><td id="12-37">0.78</td><td id="12-38">12.66</td><td id="12-39">1.00</td><td id="12-3a">1.00</td></tr>
<tr><td id="12-3b">15</td><td id="12-3c">1.73</td><td id="12-3d">0.01</td><td id="12-3e">1.00</td><td id="12-3f">1.00</td><td id="12-3g">0.01</td><td id="12-3h">0.30</td><td id="12-3i">200.00</td><td id="12-3j">0.00</td><td id="12-3k">2.47</td><td id="12-3l">50.50</td><td id="12-3m">1.00</td><td id="12-3n">1.00</td></tr>
<tr><td id="12-3o">16</td><td id="12-3p">2.98</td><td id="12-3q">0.01</td><td id="12-3r">1.00</td><td id="12-3s">1.00</td><td id="12-3t">0.01</td><td id="12-3u">0.30</td><td id="12-3v">128.61</td><td id="12-3w">0.00</td><td id="12-3x">0.07</td><td id="12-3y">100.00</td><td id="12-3z">1.00</td><td id="12-3A">1.00</td></tr>
<tr><td id="12-3B">17</td><td id="12-3C">5.37</td><td id="12-3D">0.01</td><td id="12-3E">1.00</td><td id="12-3F">24.05</td><td id="12-3G">0.01</td><td id="12-3H">0.30</td><td id="12-3I">184.64</td><td id="12-3J">0.00</td><td id="12-3K">1.24</td><td id="12-3L">18.72</td><td id="12-3M">1.00</td><td id="12-3N">1.00</td></tr>
<tr><td id="12-3O">18</td><td id="12-3P">7.54</td><td id="12-3Q">0.01</td><td id="12-3R">1.00</td><td id="12-3S">49.25</td><td id="12-3T">0.01</td><td id="12-3U">0.30</td><td id="12-3V">145.35</td><td id="12-3W">0.01</td><td id="12-3X">1.21</td><td id="12-3Y">12.13</td><td id="12-3Z">1.00</td><td id="12-40">1.00</td></tr>
<tr><td id="12-41">19</td><td id="12-42">8.82</td><td id="12-43">0.01</td><td id="12-44">1.00</td><td id="12-45">12.53</td><td id="12-46">0.01</td><td id="12-47">0.30</td><td id="12-48">200.00</td><td id="12-49">0.00</td><td id="12-4a">4.30</td><td id="12-4b">100.00</td><td id="12-4c">1.00</td><td id="12-4d">1.00</td></tr>
<tr><td id="12-4e">12</td><td id="12-4f">11.73</td><td id="12-4g">0.01</td><td id="12-4h">1.00</td><td id="12-4i">68.79</td><td id="12-4j">0.01</td><td id="12-4k">0.30</td><td id="12-4l">199.76</td><td id="12-4m">0.00</td><td id="12-4n">1.02</td><td id="12-4o">33.42</td><td id="12-4p">1.00</td><td id="12-4q">1.00</td></tr>
<tr><td id="12-4r">21</td><td id="12-4s">14.52</td><td id="12-4t">0.01</td><td id="12-4u">1.00</td><td id="12-4v">73.80</td><td id="12-4w">0.01</td><td id="12-4x">0.30</td><td id="12-4y">155.42</td><td id="12-4z">0.00</td><td id="12-4A">1.10</td><td id="12-4B">36.26</td><td id="12-4C">1.00</td><td id="12-4D">1.00</td></tr>
<tr><td id="12-4E">22</td><td id="12-4F">18.25</td><td id="12-4G">0.01</td><td id="12-4H">1.00</td><td id="12-4I">100.50</td><td id="12-4J">0.01</td><td id="12-4K">0.30</td><td id="12-4L">168.85</td><td id="12-4M">0.00</td><td id="12-4N">0.66</td><td id="12-4O">46.72</td><td id="12-4P">1.00</td><td id="12-4Q">1.00</td></tr>
<tr><td id="12-4R">23</td><td id="12-4S">20.10</td><td id="12-4T">0.01</td><td id="12-4U">1.00</td><td id="12-4V">101.56</td><td id="12-4W">0.01</td><td id="12-4X">0.30</td><td id="12-4Y">162.82</td><td id="12-4Z">0.00</td><td id="12-50">1.42</td><td id="12-51">51.65</td><td id="12-52">1.00</td><td id="12-53">1.00</td></tr>
<tr><td id="12-54">24</td><td id="12-55">22.90</td><td id="12-56">0.01</td><td id="12-57">1.00</td><td id="12-58">100.50</td><td id="12-59">0.01</td><td id="12-5a">0.30</td><td id="12-5b">126.03</td><td id="12-5c">0.01</td><td id="12-5d">0.77</td><td id="12-5e">50.50</td><td id="12-5f">1.00</td><td id="12-5g">1.00</td></tr>
<tr><td id="12-5h">25</td><td id="12-5i">25.61</td><td id="12-5j">0.01</td><td id="12-5k">1.00</td><td id="12-5l">127.78</td><td id="12-5m">0.01</td><td id="12-5n">0.30</td><td id="12-5o">125.51</td><td id="12-5p">0.01</td><td id="12-5q">1.21</td><td id="12-5r">47.80</td><td id="12-5s">1.00</td><td id="12-5t">1.00</td></tr>
<tr><td id="12-5u">26</td><td id="12-5v">27.38</td><td id="12-5w">0.01</td><td id="12-5x">1.00</td><td id="12-5y">150.25</td><td id="12-5z">0.01</td><td id="12-5A">0.30</td><td id="12-5B">195.38</td><td id="12-5C">0.00</td><td id="12-5D">2.83</td><td id="12-5E">73.36</td><td id="12-5F">1.00</td><td id="12-5G">1.00</td></tr>
<tr><td id="12-5H">27</td><td id="12-5I">30.74</td><td id="12-5J">0.01</td><td id="12-5K">1.00</td><td id="12-5L">152.69</td><td id="12-5M">0.01</td><td id="12-5N">0.30</td><td id="12-5O">178.20</td><td id="12-5P">0.00</td><td id="12-5Q">2.97</td><td id="12-5R">81.41</td><td id="12-5S">1.00</td><td id="12-5T">1.00</td></tr>
<tr><td id="12-5U">28</td><td id="12-5V">33.45</td><td id="12-5W">0.01</td><td id="12-5X">1.00</td><td id="12-5Y">70.15</td><td id="12-5Z">0.01</td><td id="12-60">0.30</td><td id="12-61">78.93</td><td id="12-62">0.00</td><td id="12-63">0.35</td><td id="12-64">100.00</td><td id="12-65">1.00</td><td id="12-66">1.00</td></tr>
<tr><td id="12-67">29</td><td id="12-68">35.51</td><td id="12-69">0.01</td><td id="12-6a">1.00</td><td id="12-6b">200.00</td><td id="12-6c">0.01</td><td id="12-6d">0.30</td><td id="12-6e">200.00</td><td id="12-6f">0.00</td><td id="12-6g">0.66</td><td id="12-6h">100.00</td><td id="12-6i">1.00</td><td id="12-6j">1.00</td></tr>
<tr><td id="12-6k">30</td><td id="12-6l">38.11</td><td id="12-6m">0.01</td><td id="12-6n">1.00</td><td id="12-6o">200.00</td><td id="12-6p">0.01</td><td id="12-6q">0.30</td><td id="12-6r">200.00</td><td id="12-6s">0.00</td><td id="12-6t">5.00</td><td id="12-6u">100.00</td><td id="12-6v">1.00</td><td id="12-6w">1.00</td></tr>
<tr><td id="12-6x">31</td><td id="12-6y">40.38</td><td id="12-6z">0.01</td><td id="12-6A">1.00</td><td id="12-6B">200.00</td><td id="12-6C">0.01</td><td id="12-6D">0.30</td><td id="12-6E">185.33</td><td id="12-6F">0.00</td><td id="12-6G">5.00</td><td id="12-6H">100.00</td><td id="12-6I">1.00</td><td id="12-6J">1.00</td></tr>
<tr><td id="12-6K">32</td><td id="12-6L">44.39</td><td id="12-6M">0.01</td><td id="12-6N">1.00</td><td id="12-6O">200.00</td><td id="12-6P">0.01</td><td id="12-6Q">0.30</td><td id="12-6R">132.08</td><td id="12-6S">0.00</td><td id="12-6T">1.57</td><td id="12-6U">96.57</td><td id="12-6V">1.00</td><td id="12-6W">1.00</td></tr>
<tr><td id="12-6X">33</td><td id="12-6Y">47.29</td><td id="12-6Z">0.01</td><td id="12-70">1.00</td><td id="12-71">200.00</td><td id="12-72">0.01</td><td id="12-73">0.30</td><td id="12-74">134.69</td><td id="12-75">0.01</td><td id="12-76">2.05</td><td id="12-77">100.00</td><td id="12-78">1.00</td><td id="12-79">1.00</td></tr>
</table>

<a id='6f07d2cf-3f84-4a3b-95c7-7744ed0b2496'></a>

13

<!-- PAGE BREAK -->

<a id='8910a73a-d783-4cf3-af54-f435d1d2c91b'></a>

## 4. References

Blinov, M. L., Faeder, J. R., Goldstein, B., Hlavacek, W. S., 2004. Bionetgen: software for rule-based modeling of signal transduction based on the interactions of molecular domains. Bioinformatics 20 (17), 3289-3291.
Chellaboina, V., Bhat, S., Haddad, M., Bernstein, D. S., 2009. Modeling and analysis of mass-action kinetics. Control Systems, IEEE 29 (4), 60-78.
Horn, F., Jackson, R., 1972. General mass action kinetics. Archive for rational mechanics and analysis 47 (2), 81-116.
Mélykúti, B., Hespanha, J. P., Khammash, M., 2014. Equilibrium distributions of simple biochemical reaction systems for time-scale separation in stochastic reaction networks. Journal of The Royal Society Interface 11 (97), 20140054.
Mendes, P., Hoops, S., Sahle, S., Gauges, R., Dada, J., Kummer, U., 2009. Computational modeling of biochemical networks using copasi. In: Systems Biology. Springer, pp. 17-59.
Zagaris, A., Kaper, H. G., Kaper, T. J., 2004. Analysis of the computational singular perturbation reduction method for chemical kinetics. Journal of Nonlinear Science 14 (1), 59-91.

<a id='94013f30-1db5-4a5c-b23a-0b66930c515c'></a>

14
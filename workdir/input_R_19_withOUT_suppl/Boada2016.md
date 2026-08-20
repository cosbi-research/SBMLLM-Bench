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
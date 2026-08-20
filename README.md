# SBMLLM-Bench

## Purpose

**SBMLLM-Bench** is a validation framework designed to assess how accurately Large Language Models (LLMs) can reconstruct executable systems biology models directly from scientific publications.

For each paper, an LLM receives the publication text and is asked to reconstruct the described mathematical model in **Antimony**, a human-readable modeling language that can be converted directly to SBML. The generated model is subsequently tested for executability. When simulation errors occur, the framework can provide the model and the corresponding error message back to the LLM for up to two correction attempts.

The final generated model is compared with a manually curated reference model representing the published study. The benchmark evaluates both whether a valid model was produced and how closely its biological structure and simulated behavior agree with the expert reconstruction.

---

## Input Files

SBMLLM-Bench requires three main types of scientific input.

### 1. Scientific papers in Markdown format

Input publications are placed in:

```text
workdir/input_R/
```

Each paper must be provided as a `.md` file. Every Markdown file in this directory is automatically considered an independent benchmark case.

The Markdown documents used in the benchmark were obtained from the original scientific publications using **Landing.AI Agentic Document Extraction (ADE)**. ADE converts the publication into a machine-readable Markdown representation while retaining the textual and document information required by the LLM. The resulting Markdown document, rather than the original PDF, is provided to the model-generation prompt.

Alternative input collections are also present for experiments involving supplementary information or papers containing multiple variants of a biological model.

### 2. Expert-curated reference models

For each input publication, an expert-reconstructed Antimony model is required in:

```text
workdir/expected_output_R/
```

The corresponding reference model follows the naming convention:

```text
or<PAPER_NAME>.txt
```

These models represent the benchmark ground truth and are used to evaluate the biological structure and simulated behavior of the LLM-generated reconstruction.

### 3. Species correspondence maps

Species mapping tables are stored in:

```text
workdir/SpeciesMap/
```

with one file per publication:

```text
<PAPER_NAME>_speciesMap.csv
```

These manually curated maps associate names used in generated models with the corresponding species in the expert model. They are required because an LLM may identify the correct biological entity while using a different abbreviation or synonym.

Multiple generated names can be associated with the same reference species, allowing the evaluation to recognize biologically equivalent naming conventions rather than requiring exact textual matches.

---

## Fabric Patterns

The pipeline uses **Fabric** to provide structured instructions to the LLM. Fabric patterns are reusable Markdown-based prompts that define the role of the model, its task, constraints, and expected output.

SBMLLM-Bench requires **two conceptually different patterns**:

1. a **Converter pattern**, which reconstructs an Antimony model from the scientific paper;
2. an **Editor pattern**, which repairs an Antimony model when execution produces an error.

The current Snakefile invokes these patterns using:

```text
fabric -s -p Converter
```

and:

```text
fabric -s -p Editor
```

respectively. The pattern names can be changed, but the names specified in the Snakefile must correspond to patterns available to the local Fabric installation.

Fabric patterns are Markdown-based prompt definitions and can be installed as custom patterns in Fabric.

### Pattern 1 — Converter

The **Converter** receives one complete Landing.AI ADE Markdown publication as its input.

Its purpose is to identify the biological system described by the article and reconstruct the corresponding mechanistic model in valid Antimony syntax.

A suitable starting pattern is:

```markdown
# IDENTITY AND PURPOSE

You are an expert systems biologist and mathematical modeler.

Your task is to reconstruct the quantitative systems biology model
described in the scientific publication provided as input.

Extract the biological species, compartments, reactions, regulatory
relationships, kinetic laws, parameter values, initial conditions,
and other information necessary to reproduce the model.

Express the reconstructed model in valid Antimony syntax.

# INSTRUCTIONS

- Read the complete scientific publication before constructing the model.
- Reconstruct the model described by the authors rather than proposing
  a new model.
- Identify all modeled biological species.
- Identify reaction directions and stoichiometric coefficients.
- Extract kinetic equations whenever they are provided.
- Extract parameter values and initial conditions whenever available.
- Preserve biological compartments when they are part of the model.
- Use information from equations, tables, figure descriptions, and text.
- Do not invent biological mechanisms that are not supported by the paper.
- When a minor implementation choice is necessary, use the simplest
  interpretation consistent with the publication.
- Produce a complete Antimony model that can be loaded and simulated.

# OUTPUT INSTRUCTIONS

Return only the Antimony model.

Do not include Markdown code fences.
Do not include explanations before or after the model.
Do not provide a summary of the paper.
```

The key requirement is that the pattern produces **only an executable Antimony reconstruction**. This is important because downstream stages treat the response directly as a model rather than as explanatory prose.

The Snakefile currently notes default sampling settings of temperature `0.7` and Top-P `0.9`, while also suggesting model-specific alternatives.

---

### Pattern 2 — Editor

The **Editor** does not receive the original publication. Instead, its input consists of the current Antimony model followed by the execution error encountered during simulation.

The Snakefile constructs an input conceptually equivalent to:

```text
<CURRENT ANTIMONY MODEL>

==SIMULATION ERROR==

<SIMULATION ERROR MESSAGE>
```

and submits it to the Editor pattern.

A suitable starting pattern is:

```markdown
# IDENTITY AND PURPOSE

You are an expert systems biologist and Antimony model debugger.

Your task is to correct an Antimony model that failed to load or simulate.

The input contains the current model followed by the marker:

==SIMULATION ERROR==

Everything after this marker describes the error produced when the model
was tested.

# INSTRUCTIONS

- Examine the Antimony model and the simulation error.
- Identify the cause of the failure.
- Correct only what is necessary to make the model executable.
- Preserve the biological meaning and structure of the supplied model.
- Preserve species, reactions, kinetic laws, parameter values, and
  initial conditions whenever they are not responsible for the error.
- Correct syntax errors, undefined symbols, invalid declarations,
  malformed reactions, inconsistent expressions, or other issues that
  prevent the model from loading or simulating.
- Do not redesign or simplify the biological model unnecessarily.
- Return a complete corrected model, not a patch or list of changes.
- Ensure that the resulting output is valid Antimony.

# OUTPUT INSTRUCTIONS

Return only the corrected Antimony model.

Do not include Markdown code fences.
Do not explain the corrections.
Do not reproduce the simulation error.
```

The distinction between these two patterns is important. 

The **Converter performs scientific model reconstruction**, whereas the **Editor performs constrained model repair**. 

The pipeline can invoke the Editor twice, allowing an initially invalid reconstruction to undergo two successive correction attempts.

---

## Performance Metrics

SBMLLM-Bench evaluates LLM performance at several complementary levels. 
No single metric is intended to characterize model quality completely: some metrics measure whether the generated model can execute, 
others assess reconstruction of the reaction network, and others compare its dynamical behavior or overall size.

### Simulation success

The generated model is tested up to three times:

- **First simulation ratio** — proportion of papers for which the original LLM-generated model executes successfully.
- **Second simulation ratio** — proportion executing successfully after the first Editor correction.
- **Third simulation ratio** — proportion executing successfully after the second Editor correction.

For each stage, a value of `1` would therefore indicate that all models in the benchmark were executable at that stage.

These metrics distinguish direct model-generation capability from the LLM's ability to recover from execution feedback.

---

### Species %

**Species %** measures how much of the biological state space of the reference model was recovered.

For each reference model, the species present in the generated model are first normalized using the manually curated species map. The metric is then calculated as:

```text
number of reference species identified in the generated model
--------------------------------------------------------------
total number of species in the reference model
```

A value of:

- **1.0** indicates that all reference species were identified;
- **0.5** indicates that half were identified;
- **0.0** indicates that none were identified.

The final benchmark value is the average across papers.

Because species synonyms can be incorporated through the species maps, this metric assesses biological identification rather than requiring identical variable names.

---

### Arrow %

**Arrow %** evaluates whether the LLM reconstructed the **qualitative reaction structure** correctly.

For each reaction in the reference model, the benchmark determines whether a generated reaction contains the same:

- reactant species;
- product species;
- reaction direction.

The numerical stoichiometric coefficients are ignored at this stage.

For example, if the reference contains:

```text
2 A + B -> C
```

then a generated reaction such as:

```text
A + B -> C
```

has the correct reaction pattern for the purposes of Arrow %, even though its stoichiometry is not fully correct.

The metric is calculated as the fraction of reference reactions for which a matching reactant/product pattern can be found. A value closer to **1** indicates better recovery of the reaction-network topology.

---

### Reaction %

**Reaction %** is a stricter version of Arrow %.

A reference reaction is considered correct only when the generated model reproduces both:

- the correct reactants and products;
- the correct stoichiometric coefficients.

Thus, for:

```text
2 A + B -> C
```

a generated reaction:

```text
A + B -> C
```

can contribute to Arrow % but **not** to Reaction %.

A Reaction % of **1** means that every reference reaction has been recovered with an identical stoichiometric representation.

Consequently:

```text
Reaction % <= Arrow %
```

is generally expected, since Reaction % imposes the stricter criterion.

---

### Average Hamming Distance

The **Average Hamming Distance** measures structural disagreement between matched reference and generated reaction vectors.

Each reaction can be represented through its column in the stoichiometric matrix. After species normalization and reaction matching, the Hamming distance measures the fraction of positions in which the generated and reference reaction vectors differ. These reaction-level distances are then averaged.

Unlike Species %, Arrow %, and Reaction %, **lower values are better**:

- **0** means no stoichiometric differences for the compared reactions;
- larger values indicate increasing disagreement.

This metric is useful because it provides a graded measure of reconstruction error rather than simply classifying an entire reaction as correct or incorrect.

---

### Average RMSRE

**Average RMSRE** measures the magnitude of errors in the reconstructed **stoichiometric coefficients**.

RMSRE stands for **Root Mean Square Relative Error**. For corresponding positions in reference and generated stoichiometric reaction vectors, the benchmark calculates the relative deviation between the coefficients and aggregates these errors across the model. The implementation also handles positions with a zero reference coefficient by applying a shift that avoids division by zero.

Interpretation is again based on minimization:

- **0** indicates exact agreement;
- values increasingly above zero indicate larger stoichiometric discrepancies.

Reaction % answers the binary question *“Was the entire reaction reproduced exactly?”*, whereas RMSRE quantifies *“How large are the coefficient errors?”*

---

### AAFE reproducibility

Structural agreement does not necessarily imply that two models produce the same biological dynamics. SBMLLM-Bench therefore also compares simulated trajectories.

The benchmark uses **Absolute Average Fold Error (AAFE)** to compare time series generated by the LLM model with those generated by the corresponding reference model.

A generated model is classified as dynamically reproducible when **at least one comparable simulated time series has an AAFE below 2**.

The final **AAFE reproducibility score** is:

```text
number of generated models satisfying the AAFE criterion
--------------------------------------------------------
total number of benchmark papers
```

A score close to **1** therefore indicates that a high proportion of reconstructed models reproduce at least one reference dynamical behavior within the benchmark's accepted error threshold.

The pipeline additionally produces plots comparing simulated trajectories for generated and reference models.

---

### Model-size ratios

SBMLLM-Bench also compares the overall composition of the generated model with the expert reconstruction.

Four quantities are counted independently for the generated and reference models:

- total number of species;
- number of reactions;
- number of compartments;
- number of global parameters.

For each paper, the pipeline calculates:

```text
generated model count
---------------------
reference model count
```

and then averages these ratios across papers.

Interpretation is centered around **1**:

| Ratio | Interpretation |
|---|---|
| `1.0` | Generated and reference models contain the same number of elements |
| `< 1.0` | The generated model contains fewer elements than the reference |
| `> 1.0` | The generated model contains more elements than the reference |

These ratios are reported separately for species, reactions, compartments, and global parameters.

They should be interpreted as **model-composition indicators rather than accuracy metrics**. For example, a species ratio of `1.0` means that the two models contain the same number of species, but does not guarantee that they contain the *same biological species*. Species % addresses that separate question.

---

## Final Benchmark Output

The benchmark-level results are consolidated in:

```text
workdir/test_table.csv
```

The table contains the LLM identifier together with:

- number of evaluated papers;
- first simulation success ratio;
- second simulation success ratio;
- third simulation success ratio;
- AAFE reproducibility score;
- Arrow %;
- Reaction %;
- Average Hamming Distance;
- Average RMSRE;
- Species %;
- generated/reference species-count ratio;
- generated/reference reaction-count ratio;
- generated/reference compartment-count ratio;
- generated/reference global-parameter-count ratio.

Together, these metrics characterize **executability, reaction-network reconstruction, stoichiometric accuracy, biological-species recovery, dynamical reproducibility, and overall model composition**.
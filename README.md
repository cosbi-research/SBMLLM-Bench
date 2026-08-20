# SBMLLM-Bench

**SBMLLM-Bench** is a validation framework for testing how accurately Large Language Models (LLMs) can reconstruct executable systems biology models from scientific publications.

The benchmark provides a curated collection of scientific papers, expert-reconstructed reference models, and quantitative evaluation metrics. You can use it to benchmark a new LLM, compare prompting strategies, or investigate where automated reconstruction of mechanistic biological models succeeds or fails.

## Index

- [Purpose](#purpose)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [1. Clone the repository](#1-clone-the-repository)
  - [2. Create the Mamba environment](#2-create-the-mamba-environment)
  - [3. Install and configure Fabric](#3-install-and-configure-fabric)
  - [4. Add the required Fabric patterns](#4-add-the-required-fabric-patterns)
  - [5. Check your benchmark inputs](#5-check-your-benchmark-inputs)
  - [6. Run the benchmark](#6-run-the-benchmark)
- [Input Files](#input-files)
- [Fabric Patterns](#fabric-patterns)
  - [Converter](#pattern-1--converter)
  - [Editor](#pattern-2--editor)
- [Performance Metrics](#performance-metrics)
- [Benchmark Output](#benchmark-output)

---

## Purpose

SBMLLM-Bench is designed to assess whether an LLM can recover a quantitative systems biology model from the information reported in a scientific publication.

For each benchmark paper, the LLM receives the publication as Markdown and is asked to reconstruct the model in **Antimony**, a human-readable modeling language that maps directly to SBML. The generated model is tested for executability. If the model cannot be loaded or simulated, its simulation error is returned to the LLM, which receives up to two opportunities to repair the model.

The final generated model is then compared with an expert-curated reconstruction of the published model. Evaluation covers several complementary aspects of performance, including successful simulation, recovery of biological species and reactions, stoichiometric accuracy, similarity of simulated dynamics, and overall model composition.

If you are developing or evaluating an LLM for scientific model reconstruction, you can use SBMLLM-Bench as a reproducible starting point and replace the model, Fabric patterns, or benchmark paper collection according to your experiment.

---

# Getting Started

## Requirements

The repository is currently configured for **Windows** execution.

In particular, the `Snakefile` explicitly uses:

```python
shell.executable("powershell.exe")
```

so the commands launched by Snakemake are written for PowerShell.

You will need:

- Git;
- Windows PowerShell;
- Mamba;
- Fabric;
- access to an LLM provider supported by Fabric;
- the repository's Python environment defined in `env.yml`.

The supplied `env.yml` uses the `bioconda` and `conda-forge` channels and installs Snakemake together with the modeling and simulation libraries required by the benchmark, including Antimony, libRoadRunner, Tellurium, libSBML, SciPy, and plotting dependencies.

If you do not already use Mamba, see the official Mamba documentation:

[Mamba documentation](https://mamba.readthedocs.io/?utm_source=chatgpt.com)

---

## 1. Clone the repository

Start by cloning SBMLLM-Bench and moving into the repository:

```powershell
git clone https://github.com/cosbi-research/SBMLLM-Bench.git
cd SBMLLM-Bench
```

The repository contains the main `Snakefile`, the reproducible environment specification in `env.yml`, evaluation scripts under `scripts/`, and benchmark data under `workdir/`.

---

## 2. Create the Mamba environment

Create a dedicated environment from the supplied `env.yml`:

```powershell
mamba env create -n sbmllm-bench -f env.yml
```

Activate it:

```powershell
mamba activate sbmllm-bench
```

You can confirm that Snakemake is available with:

```powershell
snakemake --version
```

The environment file already contains the Python and systems-biology packages used by the evaluation scripts, so you should normally not need to install these dependencies manually.

If you later update `env.yml`, synchronize the existing environment with:

```powershell
mamba env update -n sbmllm-bench -f env.yml
```

---

## 3. Install and configure Fabric

SBMLLM-Bench uses **Fabric** to send the paper and model-repair prompts to an LLM.

Fabric is an open-source framework for applying reusable prompt templates, called **patterns**, to text through different LLM providers.

Useful Fabric resources:

[Fabric repository and documentation](https://github.com/danielmiessler/fabric/blob/main/README.md?utm_source=chatgpt.com)

[Fabric custom-pattern documentation](https://github.com/danielmiessler/fabric/blob/main/README.md?utm_source=chatgpt.com)

On Windows, Fabric currently documents installation through package managers such as Winget. For example:

```powershell
winget install danielmiessler.Fabric
```

After installation, initialize Fabric:

```powershell
fabric --setup
```

Use the setup interface to configure the LLM provider and credentials that you want to benchmark. Fabric supports explicit model selection with its `--model`/`-m` option, while SBMLLM-Bench's current commands call the configured Fabric setup through named patterns.

Confirm that Fabric works:

```powershell
fabric --version
```

and inspect the available models and patterns if needed:

```powershell
fabric --listmodels
fabric --listpatterns
```

Before launching a complete benchmark, it is useful to verify that a simple Fabric request reaches your selected provider successfully.

---

## 4. Add the required Fabric patterns

SBMLLM-Bench requires two custom Fabric patterns:

```text
Converter
Editor
```

The `Snakefile` calls them directly as:

```powershell
fabric -s -p Converter
```

and:

```powershell
fabric -s -p Editor
```

where `-s` enables streamed output and `-p` selects the Fabric pattern.

Current Fabric versions support a dedicated custom-pattern directory that can be configured through:

```powershell
fabric --setup
```

A pattern is stored in its own directory and normally contains a `system.md` file. For example:

```text
<YOUR_CUSTOM_PATTERN_DIRECTORY>/
├── Converter/
│   └── system.md
└── Editor/
    └── system.md
```

Fabric's current custom-pattern mechanism keeps personal patterns separate from built-in patterns and makes them available through `fabric --pattern <NAME>`.

After adding the patterns, verify that Fabric can see them:

```powershell
fabric --listpatterns
```

You should find both:

```text
Converter
Editor
```

in the resulting list.

The exact prompts can be adapted to your experimental question. Two usable starting templates are provided in the [Fabric Patterns](#fabric-patterns) section below.

---

## 5. Check your benchmark inputs

Before running Snakemake, make sure that each benchmark case has the required files.

For a paper named:

```text
example.md
```

the corresponding files should be:

```text
workdir/input_R/example.md
workdir/expected_output_R/orexample.txt
workdir/SpeciesMap/example_speciesMap.csv
```

The `Snakefile` automatically discovers benchmark cases from the `.md` files present in:

```text
workdir/input_R/
```

so adding or removing papers from this directory changes which cases are evaluated in a run.

You can therefore use the supplied dataset directly or prepare your own benchmark collection following the same naming convention.

---

## 6. Run the benchmark

With the Mamba environment activated and Fabric configured, first perform a Snakemake dry run:

```powershell
snakemake -n
```

This shows the jobs Snakemake plans to execute without launching the LLM requests or simulations.

To run the complete benchmark, a conservative starting command is:

```powershell
snakemake --cores 1
```

Using one core keeps LLM requests sequential, which is useful when first testing a provider configuration or working with API rate limits.

Once the setup has been validated, you can choose a different number of cores according to your computing environment and LLM-provider constraints:

```powershell
snakemake --cores <N>
```

The benchmark runs over every Markdown file detected in `workdir/input_R/` and ultimately generates:

```text
workdir/test_table.csv
```

together with per-paper simulation outputs, structural evaluations, and simulation-comparison plots.

If you want to benchmark a different LLM, configure that model in Fabric and run the workflow again. For reproducible comparisons, keep the input collection and pattern definitions fixed across models.

---

# Input Files

SBMLLM-Bench requires three main types of scientific input.

## 1. Scientific papers in Markdown format

Input publications are stored in:

```text
workdir/input_R/
```

Each `.md` file is treated as an independent benchmark case. The `Snakefile` discovers these files automatically.

The Markdown documents provided with SBMLLM-Bench were obtained from the original scientific publications using **Landing.AI Agentic Document Extraction (ADE)**.

Landing.AI ADE converts document content into a machine-readable representation suitable for downstream LLM processing. In SBMLLM-Bench, the resulting Markdown document—not the original PDF—is supplied to the Converter pattern. This is explicitly documented in the pipeline itself.

The repository also identifies alternative paper collections for experiments involving supplementary material and papers describing multiple model variants:

```text
input_R_19_with_suppl
input_R_19_withOUT_suppl
input_R_multimodel
```



---

## 2. Expert-curated reference models

For every input paper, the benchmark requires a manually reconstructed reference model under:

```text
workdir/expected_output_R/
```

The expected naming convention is:

```text
or<PAPER_NAME>.txt
```

For example:

```text
workdir/input_R/example.md
```

corresponds to:

```text
workdir/expected_output_R/orexample.txt
```

These Antimony models represent the expert reconstruction against which the LLM-generated model is evaluated.

---

## 3. Species correspondence maps

Species maps are stored under:

```text
workdir/SpeciesMap/
```

using the naming convention:

```text
<PAPER_NAME>_speciesMap.csv
```

These manually curated tables connect species names produced by the LLM with their corresponding entities in the expert model.

This allows the benchmark to distinguish a genuinely missing biological species from a species that was reconstructed correctly but assigned a different abbreviation or synonym.

The maps can be extended with additional accepted synonyms when required.

---

# Fabric Patterns

Fabric patterns are reusable Markdown-based prompts that specify what the LLM should do with its input. Fabric's own patterns typically place the main instructions in a `system.md` file, and custom patterns can be made available to the CLI under a chosen pattern name.

SBMLLM-Bench needs two different kinds of reasoning:

1. **scientific reconstruction**, performed by `Converter`;
2. **model repair**, performed by `Editor`.

You are encouraged to adapt these patterns when evaluating different prompting strategies, provided that their outputs remain compatible with the pipeline.

## Pattern 1 — Converter

`Converter` receives the complete Markdown representation of one scientific publication.

Its job is to reconstruct the quantitative biological model described by the authors and return it as executable Antimony.

The `Snakefile` passes each paper to Fabric using:

```powershell
Type {input} | fabric -s -p Converter
```



A useful starting `Converter/system.md` is:

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

The final constraint is important: downstream rules process the LLM response as a model, so additional explanatory text can interfere with execution.

The `Snakefile` notes default creativity settings of temperature `0.7` and Top-P `0.9`, and includes commented examples of alternative parameter choices for GPT- and Claude-family models.

If you want to evaluate specific sampling parameters, edit the Fabric command in the `conversion` rule and keep the settings fixed across benchmark runs.

---

## Pattern 2 — Editor

`Editor` is used after an attempted simulation.

Instead of receiving the original paper, it receives:

```text
<CURRENT ANTIMONY MODEL>
==SIMULATION ERROR==
<SIMULATION ERROR MESSAGE>
```

The `Snakefile` constructs this input automatically and sends it to:

```powershell
fabric -s -p Editor
```

The same repair process can be applied twice.

A useful starting `Editor/system.md` is:

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

The two patterns deliberately solve different problems: `Converter` asks whether the LLM can recover scientific knowledge from a paper, while `Editor` asks whether it can use execution feedback to repair the resulting formal model.

This separation also makes it easy to experiment. For example, you can keep the Converter fixed while testing several Editor prompts, or vice versa.

---

# Performance Metrics

SBMLLM-Bench evaluates model reconstruction from several complementary perspectives.

A model may be executable without faithfully representing the published biology, while a structurally similar model may still fail to reproduce the expected dynamics. For this reason, the benchmark reports multiple metrics rather than reducing performance to a single score.

## Simulation success

Each generated model can be tested at three stages:

1. immediately after generation;
2. after the first Editor correction;
3. after the second Editor correction.

The benchmark therefore reports:

- **First simulation ratio** — fraction of initially generated models that can be executed successfully;
- **Second simulation ratio** — fraction that can execute after one correction attempt;
- **Third simulation ratio** — fraction that can execute after two correction attempts.

A value of `1.0` indicates successful simulation for every benchmark case at that stage.

These scores make it possible to distinguish **zero-shot model executability** from the LLM's capacity for **error-guided repair**.

---

## Species %

**Species %** measures how many of the biological species in the reference model were successfully recovered.

Conceptually:

```text
reference species identified in generated model
------------------------------------------------
total species in reference model
```

The comparison uses the manually curated species maps before scoring. Consequently, an LLM does not need to reproduce the expert model's exact variable names to receive credit for identifying the same biological entity.

Interpretation:

- `1.0` — all reference species were identified;
- `0.5` — half were identified;
- `0.0` — none were identified.

**Higher is better.**

---

## Arrow %

**Arrow %** evaluates recovery of the qualitative reaction network.

A reaction receives credit when the generated model contains the correct reactants and products. Stoichiometric coefficient values are not required to match for this metric.

For example, if the reference contains:

```text
2 A + B -> C
```

and the generated model contains:

```text
A + B -> C
```

the reaction has the correct qualitative structure and can therefore match under Arrow %, even though the coefficient of `A` is wrong.

Arrow % therefore asks:

> Did the LLM identify who reacts with whom, and in which direction?

**Higher is better.**

---

## Reaction %

**Reaction %** applies a stricter criterion.

A reaction is counted as correct only when the generated model reproduces:

- the reactants;
- the products;
- the stoichiometric coefficients.

Thus:

```text
Reference:  2 A + B -> C
Generated:    A + B -> C
```

can match for Arrow % but not for Reaction %.

Reaction % therefore asks:

> Did the LLM reconstruct the complete stoichiometric reaction correctly?

**Higher is better.**

---

## Average Hamming Distance

The **Average Hamming Distance** provides a graded measure of structural disagreement between generated and reference reaction representations.

After species correspondence has been established, reactions can be represented through their stoichiometric vectors. The Hamming-distance calculation measures how many corresponding positions differ.

Interpretation:

- `0` indicates no differences in the compared representation;
- increasing values indicate increasing disagreement.

Unlike Species %, Arrow %, and Reaction %, **lower is better**.

This metric complements the exact reaction score because it can distinguish a nearly correct reaction from one whose structure differs substantially.

---

## Average RMSRE

**RMSRE** stands for **Root Mean Square Relative Error**.

In SBMLLM-Bench, it quantifies the magnitude of differences between reference and LLM-generated stoichiometric coefficients. The individual errors are combined to provide an average measure across the model.

Interpretation:

- `0` represents exact coefficient agreement;
- larger values represent larger stoichiometric discrepancies.

**Lower is better.**

Reaction % asks whether an entire reaction is exactly correct, whereas RMSRE captures **how large the numerical stoichiometric errors are** when differences occur. The `Snakefile` explicitly defines this metric as the root mean square relative deviation between correct and generated stoichiometric coefficients.

---

## AAFE reproducibility

Structural similarity alone does not establish that two models reproduce the same biological behavior.

SBMLLM-Bench therefore simulates the generated and expert models and compares their time-dependent trajectories using **Absolute Average Fold Error (AAFE)**.

A generated model satisfies the benchmark's reproducibility criterion when **at least one simulated time series has an AAFE below 2**.

The benchmark-level AAFE reproducibility score is conceptually:

```text
models satisfying the AAFE criterion
------------------------------------
total benchmark models
```

A value closer to `1` means that a larger proportion of generated models recover at least one sufficiently similar dynamical trajectory.

**Higher is better.**

The workflow also produces per-model plots comparing generated and reference simulations:

```text
workdir/Sim_plots/
```



---

## Model-size ratios

The benchmark additionally compares the overall composition of each generated model with its reference model.

It counts:

- species;
- reactions;
- compartments;
- global parameters.

For each category, the comparison is:

```text
generated count
---------------
reference count
```

Interpretation is centered on `1`:

| Ratio | Interpretation |
|---|---|
| `1.0` | Generated and reference models contain the same number of elements |
| `< 1.0` | Generated model contains fewer elements |
| `> 1.0` | Generated model contains more elements |

These values are **composition indicators**, not identity scores.

For example, a species-count ratio of `1.0` only means that the generated and reference models contain the same *number* of species. It does not imply that they contain the same biological species; that question is addressed by Species %.

---

# Benchmark Output

A complete run produces the summary table:

```text
workdir/test_table.csv
```

The final Snakemake rule combines simulation, structural, dynamical, and model-composition results into this table.

The reported benchmark information includes:

- number of evaluated papers;
- first simulation success ratio;
- second simulation success ratio;
- third simulation success ratio;
- AAFE reproducibility;
- Arrow %;
- Reaction %;
- Average Hamming Distance;
- Average RMSRE;
- Species %;
- generated/reference species ratio;
- generated/reference reaction ratio;
- generated/reference compartment ratio;
- generated/reference global-parameter ratio.

If you want to evaluate a new LLM, the simplest workflow is therefore:

```text
configure the model in Fabric
        ↓
install or adapt Converter and Editor
        ↓
activate the Mamba environment
        ↓
run Snakemake
        ↓
inspect workdir/test_table.csv
```

You can then repeat the same run with another LLM or prompt configuration while keeping the benchmark dataset fixed, making SBMLLM-Bench suitable for systematic comparison of model-generation approaches.
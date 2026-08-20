# SBMLLM-Bench

Benchmark LLMs on their ability to reconstruct executable systems-biology models from scientific papers.

Each paper is converted to Markdown with **Landing.AI Agentic Document Extraction (ADE)**, passed to an LLM through **Fabric**, converted into an Antimony model, tested for simulation, optionally repaired, and compared with an expert-curated reference model.

## Index

- [Quick Start](#quick-start)
- [Inputs](#inputs)
- [Fabric Patterns](#fabric-patterns)
- [Run the Benchmark](#run-the-benchmark)
- [Performance Metrics](#performance-metrics)
- [Output](#output)

---

## Quick Start

### 1. Clone the repository

```powershell
git clone https://github.com/cosbi-research/SBMLLM-Bench.git
cd SBMLLM-Bench
```

### 2. Create the environment with Mamba

```powershell
mamba env create -n sbmllm-bench -f env.yml
mamba activate sbmllm-bench
```

Check Snakemake:

```powershell
snakemake --version
```

The current `Snakefile` is configured to use **PowerShell on Windows**.

### 3. Install and configure Fabric

Fabric is used to send prompts to the LLM.

- [Fabric documentation](https://github.com/danielmiessler/fabric/)

Install Fabric, then configure your model provider:

```powershell
fabric --setup
```

Check that Fabric is available:

```powershell
fabric --version
fabric --listmodels
```

### 4. Add the required Fabric patterns

SBMLLM-Bench expects two patterns:

```text
Converter
Editor
```

Verify that Fabric can see them:

```powershell
fabric --listpatterns
```

### 5. Test the workflow

First run a dry run:

```powershell
snakemake -n
```

Then execute the benchmark:

```powershell
snakemake --cores 1
```

Use more cores only if your LLM provider and API limits allow parallel requests.

---

## Inputs

Each benchmark paper requires three files.

### Scientific paper

```text
workdir/input_R/<paper>.md
```

The benchmark Markdown files were obtained from the original publications using **Landing.AI ADE**.

The `.md` files in `workdir/input_R/` determine which papers are included in a run.

### Expert reference model

```text
workdir/expected_output_R/or<paper>.txt
```

This is the manually reconstructed Antimony model used as ground truth.

### Species map

```text
workdir/SpeciesMap/<paper>_speciesMap.csv
```

This file maps equivalent species names between generated and reference models.

Example:

```text
workdir/input_R/example.md
workdir/expected_output_R/orexample.txt
workdir/SpeciesMap/example_speciesMap.csv
```

---

## Fabric Patterns

### `Converter`

The `Converter` pattern receives the complete Markdown paper and should return **only a valid Antimony model**.

Minimal example:

```markdown
# IDENTITY AND PURPOSE

You are an expert systems biologist.

Reconstruct the mathematical model described in the supplied scientific paper.

# INSTRUCTIONS

- Identify species, reactions, compartments, parameters and initial conditions.
- Recover kinetic laws and stoichiometry where available.
- Reconstruct the model described by the authors.
- Do not invent unsupported mechanisms.
- Produce valid executable Antimony.

# OUTPUT INSTRUCTIONS

Return only the Antimony model.
Do not include explanations or Markdown code fences.
```

The pipeline calls it with:

```powershell
fabric -s -p Converter
```

### `Editor`

The `Editor` pattern receives the current Antimony model followed by:

```text
==SIMULATION ERROR==
```

and the corresponding error message.

Its role is to repair the model while preserving its biological meaning.

Minimal example:

```markdown
# IDENTITY AND PURPOSE

You are an expert Antimony model debugger.

Correct the supplied model using the simulation error.

# INSTRUCTIONS

- Fix syntax, undefined symbols, malformed reactions or other execution errors.
- Preserve the biological structure whenever possible.
- Return the complete corrected model.

# OUTPUT INSTRUCTIONS

Return only valid Antimony.
Do not include explanations or Markdown code fences.
```

The pipeline calls it with:

```powershell
fabric -s -p Editor
```

The Editor can be invoked twice, giving the LLM up to two repair attempts.

---

## Run the Benchmark

With the environment activated and Fabric configured:

```powershell
mamba activate sbmllm-bench
snakemake --cores 1
```

To benchmark another LLM:

1. select/configure the model in Fabric;
2. keep the benchmark inputs fixed;
3. keep or modify the `Converter` and `Editor` patterns;
4. rerun Snakemake;
5. compare the resulting metrics.

---

## Performance Metrics

| Metric | Meaning | Better |
|---|---|---:|
| **First simulation ratio** | Models executable immediately after generation | Higher |
| **Second simulation ratio** | Models executable after one repair | Higher |
| **Third simulation ratio** | Models executable after two repairs | Higher |
| **Species %** | Fraction of reference species recovered | Higher |
| **Arrow %** | Fraction of reference reactions with correct reactants, products and direction | Higher |
| **Reaction %** | Fraction of reactions also having correct stoichiometric coefficients | Higher |
| **Average Hamming Distance** | Structural disagreement between generated and reference reactions | Lower |
| **Average RMSRE** | Relative error in stoichiometric coefficients | Lower |
| **AAFE reproducibility** | Fraction of models reproducing at least one reference trajectory with AAFE < 2 | Higher |

The benchmark also reports generated/reference ratios for:

- number of species;
- number of reactions;
- number of compartments;
- number of global parameters.

A ratio near **1** means the generated model has a similar overall size to the reference model.

---

## Output

The main benchmark summary is:

```text
workdir/test_table.csv
```

It contains the simulation, structural, dynamical, and model-size metrics for the evaluated LLM.

For a first run, the shortest path is:

```text
clone repository
→ create Mamba environment
→ configure Fabric
→ add Converter and Editor
→ run snakemake --cores 1
→ inspect workdir/test_table.csv
```
###
# SBMLLM-Bench
#
# SBMLLM-Bench is a validation framework to assess the agreement between LLM-generated systems biology models and reproducible published results.
# It is composed of a) formal performance metrics b) a dataset of manually curated papers and corresponding systems biology model.
#
# Requirements: python3, snakemake, and fabric to execute prompts.
# other requirements in env.yaml (mamba-compatible)
###
import os
import pandas as pd
from pathlib import Path
from snakemake.shell import shell

# meant to be run under windows
shell.executable("powershell.exe")
#shell.executable("C:/Program Files/PowerShell/7/pwsh.exe")

# info to provide on each test:
onstart:
    print("In rule 'evaluation table' remind to log:\nLLM utilized=\nday/time-slot where this LLM has been used so far=\nnumber of input papers=\n")

# Reads from input_R the list of manually reproducible papers
# alternative folders for evaluating performances on papers with supplementary information outside main text are available in `input_R_19_with_suppl` (with supplementary)
# and `input_R_19_withOUT_suppl` (without supplementary)
# and `input_R_multimodel` (papers that describe multiple variants of the same model)
Papers = glob_wildcards("workdir/input_R/{text}.md").text

# the final output is in `workdir/test_table.csv` that will contain all the metrics for the current run.
# each run evaluate once the pipeline on all the papers, and compute the evaluation metrics.
# the evaluation metrics are as follows:
# Species %: Percentage of species correctly identified.
# Arrow %: Percentage of reactions for which reactants and products are correctly identified.
# Reaction %: Percentage of reactions for which reactants, products, and stoichiometric coefficients are all correct
# Coefficients RMSRE: Root mean square relative deviation between the correct and LLM-generated stoichiometric coefficients for a reaction.
# AAFE %: Reproducibility score is the percentage of LLM-generated models where at least one simulated time series Absolute Average Fold Error (AAFE) is < 2
rule all:
    input:
        expand("workdir/fabric_output/{sample}.txt", sample=Papers), 
        expand("workdir/expected_output_R/or{sample}.txt", sample=Papers),
        #expand("workdir/csv_output/{sample}_result.csv", sample=Papers),
        expand("workdir/final_models/{sample}_tested.txt", sample=Papers),
        "workdir/all_simulations.csv",
        "workdir/all_semantic_comparison.csv",
        "workdir/test_table.csv"

# the pipeline consists of two prompts.
# the converter, applied by this rule, takes as input the paper converted in markdown using Landing.AI Agentic Document Extraction (ADE)
# and produces a first draft of systems biology model in Antimony format (that can be mapped 1-1 to SBML)
# Creativity parameters can be set here through `-t` (temperature) and `-T` (Top-P)
# Default: temperature 0.7, Top-P 0.9
rule conversion:
    input:
        "workdir/input_R/{sample}.md"

    output:
        "workdir/fabric_output/{sample}.txt"

    shell:
        "Type {input} | fabric -s -p Converter > {output}; Start-Sleep -Seconds 1.5"
        
# PS command for GPT models (like gpt-5) : Type {input} | fabric -t 1 -T 1 -p Antimony_Converter > {output}; Start-Sleep -Seconds 1.5
# PS command for claude models (like claude-sonnet-4.*) : Type {input} | fabric -t 0.2 -p Antimony_Converter > {output}; Start-Sleep -Seconds 1.5

rule first_decode:
    input:
        "workdir/fabric_output/{sample}.txt"  
    output:
        "workdir/decoded/{sample}_1dec.txt"
    run:
        with open(input[0], 'rb') as source_file:
            with open(output[0], 'w+b') as dest_file:
                contents = source_file.read()
                dest_file.write(contents.decode('utf-16').encode('utf-8'))
          

rule first_simulation:
    input:
        "workdir/decoded/{sample}_1dec.txt" 

    output: 
        "workdir/Error/{sample}_1er.txt",
        "workdir/simulated/{sample}_1S.txt"
    
    script:
        "scripts/check_simulation.py"

rule first_Evaluation:
    input:
        "workdir/Error/{sample}_1er.txt"
    
    output:
        "workdir/Evaluation/first/{sample}_1eval.csv"
    
    script:
        "scripts/Error_Evaluation_1.py"

rule first_aggregation:
    input:
        expand("workdir/Evaluation/first/{sample}_1eval.csv", sample=Papers)
    output:
        "workdir/CSV/first_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

# the pipeline consists of two prompts.
# the editor, applied by this rule, takes as input the antimony model draft and the (eventual) simulation error,
# and try to fix it.
# Creativity parameters can be set here through `-t` (temperature) and `-T` (Top-P)
# Default: temperature 0.7, Top-P 0.9
rule first_correction:
    input:
        model = "workdir/simulated/{sample}_1S.txt",
        error = "workdir/Error/{sample}_1er.txt"

    output:
        corrected_model = "workdir/corrected/{sample}_1C.txt"

    shell:
        "(Type {input.model}) + '==SIMULATION ERROR==' + (Type {input.error}) | fabric -s -p Editor > {output.corrected_model}; Start-Sleep -Seconds 1.5" 

# PS command for GPT models (like gpt-5) : (Type {input.model}) + '==SIMULATION ERROR==' + (Type {input.error}) | fabric -t 1 -T 1 -p Antimony_Editor > {output.corrected_model}; Start-Sleep -Seconds 1.5
# PS command for claude models (like claude-sonnet-4.*) : (Type {input.model}) + '==SIMULATION ERROR==' + (Type {input.error}) | fabric -t 0.2 -p Antimony_Editor > {output.corrected_model}; Start-Sleep -Seconds 1.5

rule second_decode:
   input:
        "workdir/corrected/{sample}_1C.txt"  
   output:
        "workdir/decoded/{sample}_2dec.txt"
   run:
        with open(input[0], 'rb') as source_file:
            with open(output[0], 'w+b') as dest_file:
                contents = source_file.read()
                dest_file.write(contents.decode('utf-16').encode('utf-8'))

rule second_simulation:
    input:
        "workdir/decoded/{sample}_2dec.txt" 

    output: 
        "workdir/Error/{sample}_2er.txt",
        "workdir/simulated/{sample}_2S.txt"
    
    script:
        "scripts/check_simulation.py"


rule second_Evaluation:
    input:
        "workdir/Error/{sample}_2er.txt"
    
    output:
        "workdir/Evaluation/second/{sample}_2eval.csv"
    
    script:
        "scripts/Error_Evaluation_2.py"

rule second_aggregation:
    input:
        expand("workdir/Evaluation/second/{sample}_2eval.csv",sample=Papers)
    output:
        "workdir/CSV/second_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

# the pipeline consists of two prompts.
# the editor, applied by this rule, takes as input the antimony model draft and the (eventual) simulation error,
# and try to fix it, for the second time.
# Creativity parameters can be set here through `-t` (temperature) and `-T` (Top-P)
# Default: temperature 0.7, Top-P 0.9
rule second_correction:
    input:
        model = "workdir/simulated/{sample}_2S.txt",
        error = "workdir/Error/{sample}_2er.txt"

    output:
        corrected_model = "workdir/corrected/{sample}_2C.txt"

    shell:
        "(Type {input.model}) + '==SIMULATION ERROR==' + (Type {input.error}) | fabric -s -p Editor > {output.corrected_model}; Start-Sleep -Seconds 1.5" 

# PS command for GPT models (like gpt-5) : (Type {input.model}) + '==SIMULATION ERROR==' + (Type {input.error}) | fabric -t 1 -T 1 -p Antimony_Editor > {output.corrected_model}; Start-Sleep -Seconds 1.5
# PS command for claude models (like claude-sonnet-4.*) : (Type {input.model}) + '==SIMULATION ERROR==' + (Type {input.error}) | fabric -t 0.2 -p Antimony_Editor > {output.corrected_model}; Start-Sleep -Seconds 1.5 

rule third_decode:
    input:
        "workdir/corrected/{sample}_2C.txt"  
    output:
        "workdir/decoded/{sample}_3dec.txt"
    run:
        with open(input[0], 'rb') as source_file:
            with open(output[0], 'w+b') as dest_file:
                contents = source_file.read()
                dest_file.write(contents.decode('utf-16').encode('utf-8'))

# third Simulation: the models coming from second correction will be copied in the ./final_model repository: it contains all tested model (corrected or not). In the end we are going to generate a final csv file with some info about each 
# model simulation (% of compiled and simulated model from first simulation without correction until the last one after the second correction).

rule third_simulation:
    input:
        "workdir/decoded/{sample}_3dec.txt" 

    output: 
        "workdir/Error/{sample}_3er.txt",
        "workdir/final_models/{sample}_tested.txt"
    
    script:
        "scripts/check_simulation.py"


rule third_Evaluation:
    input:
        "workdir/Error/{sample}_3er.txt"
    
    output:
        "workdir/Evaluation/third/{sample}_3eval.csv"
    
    script:
        "scripts/Error_Evaluation_3.py"

rule third_aggregation:
    input:
        expand("workdir/Evaluation/third/{sample}_3eval.csv",sample=Papers)
    output:
        "workdir/CSV/third_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

# compute AAFE%
rule AAFE_Evaluation:
    input:
        "workdir/final_models/{sample}_tested.txt",
        "workdir/expected_output_R/or{sample}.txt"
    output:
        "workdir/Evaluation/AAFE/gen{sample}_vs_or{sample}_aafe_eval.csv",
        "workdir/Sim_plots/gen{sample}_vs_or{sample}.png"
    script:
        "scripts/AAFE_&_plots.py"

rule fourth_aggregation:
    input:
        expand("workdir/Evaluation/AAFE/gen{sample}_vs_or{sample}_aafe_eval.csv",sample=Papers)
    output:
        "workdir/CSV/AAFE_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

# Compute the Evaluation metrics.
# Species %: Percentage of species correctly identified.
# Arrow %: Percentage of reactions for which reactants and products are correctly identified.
# Reaction %: Percentage of reactions for which reactants, products, and stoichiometric coefficients are all correct
# Coefficients RMSRE: Root mean square relative deviation between the correct and LLM-generated stoichiometric coefficients for a reaction.
# AAFE %: Reproducibility score is the percentage of LLM-generated models where at least one simulated time series Absolute Average Fold Error (AAFE) is < 2
#
# in particular Species% is based on `workdir/SpeciesMap` that map every generated species name, 
# to it's counterpart in the original model manually coded by a domain expert.
# SpeciesMaps can be edited to add further synonyms.
rule Hamming_distance_Evaluation:
    input:
        "workdir/final_models/{sample}_tested.txt",
        "workdir/expected_output_R/or{sample}.txt",
        "workdir/SpeciesMap/{sample}_speciesMap.csv"
    output:
        "workdir/Evaluation/Arrow%/gen{sample}_vs_or{sample}_Arrow_eval.csv",
        "workdir/Evaluation/Reaction%/gen{sample}_vs_or{sample}_Reaction_eval.csv",
        "workdir/Evaluation/Av_Hamming_Distance/gen{sample}_vs_or{sample}_Hamming_eval.csv",
        "workdir/Evaluation/Av_RMSRE/gen{sample}_vs_or{sample}_RMSRE_eval.csv",
        "workdir/Evaluation/different_species/{sample}_different_species.txt",
        "workdir/Evaluation/missing_species/{sample}_missing_species.txt",
        "workdir/Evaluation/Correct_species%/gen{sample}_vs_or{sample}_Correct_species_eval.csv"

    script:
        "scripts/ComputeMetrics.py"

# aggregate Arrow%
rule fifth_aggregation:
    input:
        expand("workdir/Evaluation/Arrow%/gen{sample}_vs_or{sample}_Arrow_eval.csv",sample=Papers)
    output:
        "workdir/CSV/Arrow%_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

# aggregate Reaction%
rule sixth_aggregation:
    input:
        expand("workdir/Evaluation/Reaction%/gen{sample}_vs_or{sample}_Reaction_eval.csv",sample=Papers)
    output:
        "workdir/CSV/Reaction%_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

rule seventh_aggregation:
    input:
        expand("workdir/Evaluation/Av_Hamming_Distance/gen{sample}_vs_or{sample}_Hamming_eval.csv",sample=Papers)
    output:
        "workdir/CSV/AvHammingDist_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

# aggregate Average RMSRE between generated and original stoichiometric coefficients
rule eighth_aggregation:
    input:
        expand("workdir/Evaluation/Av_RMSRE/gen{sample}_vs_or{sample}_RMSRE_eval.csv",sample=Papers)
    output:
        "workdir/CSV/AvRMSRE_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)

# aggregate Species %
rule ninth_aggregation:
    input:
        expand("workdir/Evaluation/Correct_species%/gen{sample}_vs_or{sample}_Correct_species_eval.csv",sample=Papers)
    output:
        "workdir/CSV/CorrectSpecies_evaluation.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(output[0], index=False)


rule aggregate_all:
    input:
        expand("workdir/CSV/{metric}_evaluation.csv", metric=["first","second","third","AAFE","Arrow%","Reaction%","AvHammingDist","AvRMSRE","CorrectSpecies"])

    output:
        "workdir/all_simulations.csv"

    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=False, axis=1)
        df.to_csv(output[0], index=False)

rule semantic_evaluation_generated:
    input:
        "workdir/final_models/{sample}_tested.txt"
    
    output:
        "workdir/semantic_evaluation/generated/{sample}_G_semantic.csv"
    
    script:
        "scripts/semantic_evaluation.py"

rule semantic_evaluation_originals:
    input:
        "workdir/expected_output_R/or{sample}.txt"
    
    output:
        "workdir/semantic_evaluation/original/{sample}_O_semantic.csv"
    
    script:
        "scripts/semantic_evaluation.py"

rule merge_generated:
    input:
        expand("workdir/semantic_evaluation/generated/{sample}_G_semantic.csv",sample=Papers)
    output:
        "workdir/semantic_evaluation/Semantic_Outputs_generated.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=False, axis=0)
        df.to_csv(output[0], index=False)

rule merge_originals:
    input:
        expand("workdir/semantic_evaluation/original/{sample}_O_semantic.csv", sample=Papers)
    output:
        "workdir/semantic_evaluation/Semantic_Outputs_original.csv"
    run:
        import pandas as pd
        
        dfs = [pd.read_csv(file) for file in input]
        df = pd.concat(dfs, ignore_index=False, axis=0)
        df.to_csv(output[0], index=False)

rule parameter_comparison:
    input:
        "workdir/semantic_evaluation/Semantic_Outputs_generated.csv",
        "workdir/semantic_evaluation/Semantic_Outputs_original.csv"
    
    output:
        "workdir/all_semantic_comparison.csv"
    
    script:
        "scripts/final_comparison.py"


rule evaluation_table:
    input:
        "workdir/all_simulations.csv",
        "workdir/all_semantic_comparison.csv"
    
    output:
        "workdir/test_table.csv"
    
    script:
        "scripts/test_table.py"
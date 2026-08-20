from scipy.spatial import distance
import pandas as pd
import numpy as np
import tellurium as te
from collections import OrderedDict

# Snakemake inputs & output

generated_model = snakemake.input[0]
original_model = snakemake.input[1]
species_map = snakemake.input[2]
Arrow_evaluation = snakemake.output[0]
Reaction_evaluation = snakemake.output[1]
Av_Hamming_Dist_evaluation = snakemake.output[2]
Av_RMSRE_evaluation = snakemake.output[3]
different = snakemake.output[4]
missing = snakemake.output[5]
Correct_species_evaluation = snakemake.output[6]


# Loading the models and extract the stechiometric matrices

def checking_simulation(gen_file, orig_file):
    
    simulation_gen = True

    try:
        with open(gen_file, "r") as f1:
            gen = f1.read()
            
            gen_antimony = te.loadAntimonyModel(gen)
            
    
    except Exception:

        simulation_gen = False

    # decision based on simulation_output

    if simulation_gen:

        # compute Hamming distance for each pair of column vector of generated_model matrix and original_model matrix 
        # and extract the percentage of non-similar vectors (reactions differentiation)

        gen_matrix, orig_matrix = getStechiometricMatrices(gen_file, orig_file)

        if gen_matrix is None or orig_matrix is None:
            arrow = np.nan
            Reaction = np.nan
            average_hamming_distance = np.nan
            average_RMSRE = np.nan
            species_identification_rate = np.nan

            # save empty spurious/different species txt
            with open(different, "w") as f_5:
                f_5.write("Species in generated Stoichiometric matrix NOT found in original:\n")
                f_5.write("\nNo matrices, No information") 

            # save empty missing species txt
            with open(missing, "w") as f_6:
                f_6.write("Species in original Stoichiometric matrix NOT found in generated:\n")
                f_6.write("\nNo matrices, No information")

        else:
            gen_norm_matrix_mapped, species_identification_rate = normalization(gen_matrix,orig_matrix,csv_path=species_map)

            gen_ordered_matrix = Ordering_by_original_rownames(gen_norm_matrix_mapped, orig_matrix)

            arrow, Reaction, average_hamming_distance, average_RMSRE = order_matrices_by_original_columns(gen_ordered_matrix, orig_matrix)
       

    else:
        arrow = np.nan
        Reaction = np.nan
        average_hamming_distance = np.nan
        average_RMSRE = np.nan
        species_identification_rate = np.nan

        # generated model doesn't executable, empty txt files

        with open(different, "w") as f_5:
                f_5.write("Species in generated Stoichiometric matrix NOT found in original:\n")
                f_5.write("\nGenerated model not executable, No information") 

        with open(missing, "w") as f_6:
                f_6.write("Species in original Stoichiometric matrix NOT found in generated:\n")
                f_6.write("\nGenerated model not executable, No information")

        # write the ratios on a CSV:
    with open(Arrow_evaluation, "w") as f_1:
        csv_out_1=pd.DataFrame({"Arrow%":[arrow]})
        csv_out_1.to_csv(Arrow_evaluation, index=False)
    with open(Reaction_evaluation, "w") as f_2:
        csv_out_2= pd.DataFrame({"Reaction%": [Reaction]})
        csv_out_2.to_csv(Reaction_evaluation, index=False)
    with open(Av_Hamming_Dist_evaluation, "w") as f_3:
        csv_out_3 = pd.DataFrame({"Average_Hamming_Distance": [average_hamming_distance]})
        csv_out_3.to_csv(Av_Hamming_Dist_evaluation, index=False)
    with open(Av_RMSRE_evaluation, "w") as f_4:
        csv_out_4 = pd.DataFrame({"Average_RMSRE": [average_RMSRE]})
        csv_out_4.to_csv(Av_RMSRE_evaluation, index=False)
    with open(Correct_species_evaluation, "w") as f_7:
        csv_out_5 = pd.DataFrame({"Average_Correct_species":[species_identification_rate]})
        csv_out_5.to_csv(Correct_species_evaluation, index=False)
   
# Function Extraction_matrix: load the models if simulation goes fine and extract the stechiomatric matrix of both (generated vs original)

def getStechiometricMatrices(gen_file, orig_file):

    # Loading the generated model and extracting its stechiometric matrix 
    
    try:
        with open(gen_file, "r") as file1:
        
            generated = file1.read()
        
            gen_model = te.loadAntimonyModel(generated)

            depen_gen_sp = gen_model.getFloatingSpeciesIds()
            
            gen_matrix = gen_model.getFullStoichiometryMatrix()

            gen_df = pd.DataFrame(gen_matrix, index=depen_gen_sp)

            gen_df = gen_df.loc[:,(gen_df != 0).any(axis=0)]

    # Loading the original model and extracting its stechiometric matrix
        
        with open(orig_file, "r") as file2:
            
            original = file2.read()
            
            orig_model = te.loadAntimonyModel(original)

            depen_or_sp = orig_model.getFloatingSpeciesIds()
            
            orig_matrix = orig_model.getFullStoichiometryMatrix()

            orig_df = pd.DataFrame(orig_matrix, index=depen_or_sp)

            orig_df = orig_df.loc[:,(orig_df != 0).any(axis=0)]

        return gen_df, orig_df
    
    except Exception:

        return None, None

def normalization(generated_dataframe, original_dataframe, csv_path):
    
    #generated_dataframe.index = [s.replace("_", "") for s in generated_dataframe.index]

    #original_dataframe.index = [s.replace("_", "") for s in original_dataframe.index]

    # extraction of unmatched species after normalization
    orig_species = set(original_dataframe.index)
    gen_species = set(generated_dataframe.index)

    # Case 1: species in generated but NOT in original (spurious/different species)
    unmatched_gen_species = gen_species - orig_species

    # Case 2: species in original but NOT in generated (missing species)
    unmatched_orig_species = orig_species - gen_species

    # save spurious/different species to txt
    with open(different, "w") as f_5:
        f_5.write("Species in generated Stoichiometric matrix NOT found in original:\n")
        for species in sorted(unmatched_gen_species):
            f_5.write(f"{species}\n") 
    
    # save missing species to txt
    with open(missing, "w") as f_6:
        f_6.write("Species in original Stoichiometric matrix NOT found in generated:\n")
        for species in sorted(unmatched_orig_species):
            f_6.write(f"{species}\n")

    # step 2: load and build the mapping dict
    mapping_dict = dict()

    with open(csv_path, "r") as f:
        lines = f.readlines()

        if len(lines) > 1:
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",",maxsplit=1)
                if len(parts) != 2:
                    continue

                generated_block, original = parts[0].strip(), parts[1].strip()

                generated_names = [
                    name.strip().replace("//","")
                    for name in generated_block.split("//")
                    if name.strip()
                ]

                for name in generated_names:
                    mapping_dict[name] = original
    
    # step 3: rename generated species names to original ones (if mapping exists)
    if mapping_dict:
        generated_dataframe = generated_dataframe.rename(index=mapping_dict)

    # compute % of correctly identified species after mapping

    gen_species_after_mapping = set(generated_dataframe.index)
    correctly_identified = orig_species.intersection(gen_species_after_mapping)
    percent_correct_species = len(correctly_identified) / len(orig_species)

    return generated_dataframe, percent_correct_species


def Ordering_by_original_rownames(df1,df2):

    gen_reordered = df1.reindex(df2.index)

    missing_rows = gen_reordered[gen_reordered.isna().all(axis=1)].index

    for row in missing_rows:
        gen_reordered.loc[row] = np.zeros(df1.shape[1])


    return gen_reordered

def percentage_matching_rownames(data_1, data_2):

    original = te.loada(data_2)

    generated = te.loada(data_1)

    original_sp = original.getFloatingSpeciesIds()

    generated_sp = generated.getFloatingSpeciesIds()

    orig_species = set(original_sp)
    
    gen_species = set(generated_sp)

    common = orig_species.intersection(gen_species)

    average_common_names = len(common) / len(orig_species)


    return average_common_names

def order_matrices_by_original_columns(gen_df, orig_df):

    ordered_generated_cols = []
    original2generated = OrderedDict()
    
    correct_pattern = 0
    correct_coeff = 0
    
    errors = []
    hamming_dist = []

    for orig_col in orig_df.columns:

        orig_vec = orig_df[orig_col].values

        sources = orig_vec < 0
        targets = orig_vec > 0

        original2generated[orig_col] = []
        
        for gen_col in gen_df.columns:
            
            gen_vec = gen_df[gen_col].values
            g_sources = gen_vec < 0
            g_targets = gen_vec > 0
        
            if np.array_equal(sources,g_sources) and np.array_equal(targets,g_targets):
                
                original2generated[orig_col].append(gen_col)        

        if len(original2generated[orig_col]) > 0:
            correct_pattern += 1 

        # set of available generated columns

    available_gen_cols = set(gen_df.columns)  
    
    # selection of the closest candidates

    for i, (orig_col, gcandidates) in enumerate(original2generated.items()):

        o_vector = orig_df[orig_col].values
        epsilon = 1

        # filter candidates to only those still available
        
        available_candidates = [c for c in gcandidates if c in available_gen_cols]

        if len(available_candidates) == 0:

            zero_vec = pd.Series(
                np.zeros(orig_df.shape[0]),
                index=orig_df.index
            )
            ordered_generated_cols.append(zero_vec)
            best_vec = zero_vec.values
        
        else:
            distances = []

            for candidate in available_candidates:
                g_vector = gen_df[candidate].values
                dist = np.linalg.norm(o_vector - g_vector)
                distances.append(dist)
        
            best_idx = np.argmin(distances)
            best_gen_col = available_candidates[best_idx]

            best_vec = gen_df[best_gen_col].values

            ordered_generated_cols.append(gen_df[best_gen_col])

            # remove assigned column from available set --> 1:1 mapping enforced

            available_gen_cols.remove(best_gen_col)
        
        if np.array_equal(o_vector,best_vec):

            correct_coeff += 1
            hamming_dist.append(0)
            errors.append(np.zeros_like(o_vector, dtype=float))

        else:
            
            error_vec = np.zeros_like(o_vector, dtype=float)

            # Case 1: o != 0 --> Standard RMSRE
            mask_nonzero_orig = (o_vector != 0) 
            den = np.abs(o_vector[mask_nonzero_orig])
            error_vec[mask_nonzero_orig] = ((o_vector[mask_nonzero_orig] - best_vec[mask_nonzero_orig]) / den) **2
            #error_vec = (o_vector != best_vec).astype(float)


            # Case 2: o == 0 - shift both by epsilon(1) to avoid zero-div
            mask_zero_orig = ~mask_nonzero_orig
            o_shifted = o_vector[mask_zero_orig] + epsilon
            g_shifted = best_vec[mask_zero_orig] + epsilon
            error_vec[mask_zero_orig] = ((o_shifted - g_shifted) / np.abs(o_shifted)) **2


            errors.append(error_vec)
            hamming_dist.append(distance.hamming(o_vector, best_vec))

    # RMSRE aggregation
    total = len(orig_df.columns)
    arrow_percent = correct_pattern/total
    reaction_percent = correct_coeff/total

    rmsre_avg = 0
    hamming_avg = 0

    if len(errors) > 0:
        errors = np.array(errors)
        #print(f"errors:\n{errors}")
        row_sums = np.sum(errors, axis=1)
        rmsre_avg = np.sqrt(np.mean(row_sums))

    if len(hamming_dist) > 0:
        hamming_dist = np.array(hamming_dist)
        hamming_avg = np.mean(hamming_dist)

    return arrow_percent, reaction_percent, hamming_avg, rmsre_avg


# Run

checking_simulation(generated_model, original_model)
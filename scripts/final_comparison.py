
import pandas as pd
import numpy as np

##Snakemake inputs and Outputs##

in_csv_fabric = snakemake.input[0]
in_csv_original= snakemake.input[1]
out_csv = snakemake.output[0]

file1= pd.read_csv(in_csv_fabric, index_col=0)

file2= pd.read_csv(in_csv_original, index_col=0)

df1 = pd.DataFrame(file1)

df2 = pd.DataFrame(file2)


df_fabric = df1.copy()
df_original = df2.copy()

#df_fabric = df_fabric.drop("N° Glob.Parameters", axis=1)
#df_original= df_original.drop("N° Glob.Parameters", axis=1)


df_ratio = pd.DataFrame(columns=df_fabric.columns, index=df_fabric.index)

for col in df_fabric.columns:
    df_ratio[col] = df_fabric[col] / df_original[col].values

df_ratio = df_ratio.replace([np.inf], np.nan)

df_ratio.index = [idx.replace("_generated", "_ratio") for idx in df_fabric.index]

#print(df_ratio)

mean_values = df_ratio.mean()

final_df = pd.DataFrame([mean_values], columns=df_fabric.columns)

# Output CSV

final_df.to_csv(out_csv, index=False)


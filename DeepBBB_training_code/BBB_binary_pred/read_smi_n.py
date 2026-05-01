
from rdkit import Chem
import glob
import pandas as pd
import sys
input_f=sys.argv[1]



#Test=pd.read_csv("Test_"+num+".csv", header=0, sep=",")
Test=pd.read_csv(input_f+".tsv", header=0, sep="\t")

#TAID,Name,IUPAC Name,PubChem CID,Canonical SMILES,InChIKey,Toxicity Value

#dict_smi={}
#dict_name={}
#dict_t_valu={}

dict_smi_n_v={}
for index, row in Test.iterrows():

    smi=row['SMILES']
    print (smi)
    InChI=row['Inchi']
    if str(smi) != 'nan' and str(InChI) != 'nan':
       mol = Chem.MolFromSmiles(smi)
       #InChI=row['Inchi']
       Name=row['compound_name']
       print (Name)
       T_value=row['BBB+/BBB-']
       if T_value=='BBB+':
             T_value_n=1
       elif  T_value=='BBB-':
             T_value_n=0
       if mol is not None:
          dict_smi_n_v[InChI] = [smi,Name,T_value_n]
          #dict_name[InChIKey]= Name

# 读取 CSV 文件
approved_df = pd.read_csv('drugbank_approved_structure_links.csv')
experimental_df = pd.read_csv('drugbank_experimental_structure_links.csv')
investigational_df = pd.read_csv('drugbank_investigational_structure_links.csv')

# 合并所有 DataFrame
combined_df = pd.concat([approved_df, experimental_df, investigational_df], ignore_index=True)

for index, row in  combined_df.iterrows():
    
    smi=row['SMILES']
    print (smi)
    InChI=row['InChI']
    if str(smi) != 'nan' and str(InChI) != 'nan':
       mol = Chem.MolFromSmiles(smi)
       #InChI=row['Inchi']
       Name=row['Name']
       print (Name)
       T_value_n=0
       if mol is not None  and InChI not in dict_smi_n_v.keys():
          dict_smi_n_v[InChI] = [smi,Name,T_value_n]





import numpy as np

np.save(input_f+'_dict_comb.npy',dict_smi_n_v)
new_dic=np.load(input_f+'_dict_comb.npy', allow_pickle='TRUE').item()

print (new_dic)
import json
with open(input_f+'_dict_comb.json', 'w') as f:
    json.dump(dict_smi_n_v, f)



'''
import json

with open('my_dict.json', 'r') as f:
    my_dict = json.load(f)

print(my_dict)
'''

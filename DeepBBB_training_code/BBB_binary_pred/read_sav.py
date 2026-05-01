import pandas as pd

import sys

input_f=sys.argv[1]

data = pd.read_csv(input_f, delimiter=' ', header=None)

data.columns = ['id_old', 'smiles']

data['id'] = input_f.replace('.txt','_').replace('generated_','') + data.index.astype(str)

new_data = data[['id', 'smiles']]
new_data.to_csv(input_f.replace('.txt','')+'_n.csv', index=False)

output_f = input_f.replace('.txt', '_n.smi')
data[['smiles', 'id']].to_csv(output_f, sep='\t', index=False)


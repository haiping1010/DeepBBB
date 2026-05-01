import pandas as pd

# 定义文件路径
input_file = 'Enamine_REAL_350-3_lead-like_cxsmiles.cxsmiles'
output_prefix = 'temT_'

# 定义需要保留的列
columns_to_keep = ['smiles', 'id']

# 使用 pandas 读取大文件，只加载需要的列
chunk_size = 200000  # 每个小文件的行数
out_count = 0

# 使用 chunksize 分块读取文件
for chunk in pd.read_csv(input_file, sep='\t', usecols=columns_to_keep, chunksize=chunk_size):
    out_count += 1
    output_file = f'{output_prefix}{out_count}.cxsmiles'
    
    # 将每个块保存为单独的文件，只保留需要的列
    chunk.to_csv(output_file, sep='\t', index=False)

print(f'文件已拆分为 {out_count} 个小文件，仅保留 smiles 和 id 列。')

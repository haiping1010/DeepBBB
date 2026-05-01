
name=$1

base=${name%.cxsmiles}

python  read_smi_protein_nnn.py  $name  > 'out_'$base'.log' 


python  training_nn3_BBB_load_name.py  $base > $base'_predict.log'

rm -rf data1/processed/$base'.pt'




#conda activate py3
for name in   *.json

do

base=${name%.json}
#python  read_smi_protein_nnn.py  $name
nohup python  read_smi_protein_nnn.py  $base  > 'out_'$base'.log' 2>&1&
sleep 4s
done

#conda activate py3
for name in   *.json

do

base=${name%.json}
nohup python  read_smi_protein_nnn.py  $name  > 'out_'$base'.log' 2>&1&
sleep 4s
done

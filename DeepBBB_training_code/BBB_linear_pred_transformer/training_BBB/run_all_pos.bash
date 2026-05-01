#conda activate py3
for name in   all_data/temT_*.txt

do

	id=${name:14:-4}
	echo $id
nohup python  read_smi_protein_nnn.py  $id  > 'outT_'$id'.log' 2>&1&
sleep 15s
done

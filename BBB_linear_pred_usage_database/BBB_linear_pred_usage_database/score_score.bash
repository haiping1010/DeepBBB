

for name in output_temT_*_n_n.txt  
do

base=${name%.txt}

sort -t ','  -g -rk 2,2  $name  > $base'_tem.sort'

awk -F ',' ' $2 >= 0.5 ' $base'_tem.sort'  >  $base'_select_RG.sort'

rm -rf $base'_tem.sort'


done

cat  output_temT_*'_select_RG.sort'   > all_out_select.sort





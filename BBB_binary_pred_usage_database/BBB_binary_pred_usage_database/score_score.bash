

for name in output_temT_*_n.txt  
do

base=${name%.txt}

sort -t ','  -g -rk 2,2  $name  > $base'_tem.sort'

awk -F ',' ' $2 >= 0.99 ' $base'_tem.sort'  >  $base'_select.sort'

rm -rf $base'_tem.sort'


done

cat  output_temT_*'_select.sort'   > all_out_select.sort





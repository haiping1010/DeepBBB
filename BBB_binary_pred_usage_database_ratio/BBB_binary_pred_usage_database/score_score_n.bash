


cat  output_temT_*_sel_n_f_n.txt  > all_output.txt
sort -t ','  -g -rk 2,2   all_output.txt  >   all_output.sort

awk -F ',' ' $2 >= 0.9 ' all_output.sort  >  all_output_select.sort









for name in   ../../select_all/final/temT_*_sel_n_f.cxsmiles
do
#../../select_all/final/
base=${name:23}

echo $base
nohup bash run_all_part.bash  $base &

sleep 3s


done

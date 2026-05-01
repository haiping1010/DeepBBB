for name in   ../../select_all/temT_*_sel_n.cxsmiles
do

base=${name:17}

echo $base
nohup bash run_all_part.bash  $base &

sleep 3s


done

for name in   ../../database/temT_8756.cxsmiles
do

base=${name:15}

echo $base
nohup bash run_all_part.bash  $base &

sleep 60s


done

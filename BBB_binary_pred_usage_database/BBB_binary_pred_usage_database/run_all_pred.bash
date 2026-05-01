for name in   ../../database/temT_{4353..4999}.cxsmiles
do

base=${name:15}

echo $base
nohup bash run_all_part.bash  $base &

sleep 60s


done

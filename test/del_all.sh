test_task=$(ls -l |grep ^d |awk '{print$9}')

for task in ${test_task};do
    cd ${task}
    rm ${task} run -r
    cd ../
done


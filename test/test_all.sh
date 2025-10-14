test_task=$(ls -l |grep ^d |awk '{print$9}')

#Preprocessing 
for task in ${test_task};do
    python ../main.py -d ${task} -i run.in.EXAMPLE1 system.data system.in.init system.in.settings -o temp -t ${task} -p pre
done


#Running
for task in ${test_task};do
    python ../main.py -d ${task} -i temp -o temp -t ${task} -p run
done


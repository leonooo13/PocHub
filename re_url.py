import re
pattern = r'https?://\S+|www\.\S+'
with open("text.txt","r",encoding="utf-8") as f:
    text=f.read()
urls=re.findall(pattern,text)
for url in urls:
    print(url)
import requests

r = requests.get(
    'https://sh.58.com/job/pn2/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&key=&pid=428659423751503872&PGTID=0d302408-0000-23f0-1512-0f8696de4c20&ClickID=3')
print(r.text)

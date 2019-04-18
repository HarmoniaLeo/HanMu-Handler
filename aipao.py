import urllib.request
import ssl
import random
 
imeilist={"bc1a4f7ea85044db891bdde5ff970563","db6aa97501104012b057aa1742e435db"}
ssl._create_default_https_context = ssl._create_unverified_context
for i in imeilist:
    res=urllib.request.urlopen("https://client4.aipao.me/api/token/QM_Users/LoginSchool?IMEICode="+i)
    pack=res.read().decode("utf-8")
    tok=pack[pack.find("Token")+9:pack.find("Token")+41]
    res=urllib.request.urlopen(url="https://client4.aipao.me/api/"+tok+"/QM_Runs/SRS?S1=30.534743&S2=114.367236&S3=2000")
    pack=res.read().decode("utf-8")
    RunId=pack[pack.find("RunId")+9:pack.find("RunId")+41]
    time=random.randrange(540,660)
    urllib.request.urlopen(url="https://client4.aipao.me/api/"+tok+"/QM_Runs/ES?S1="+RunId+"&S2=2000&S3=2000&S4="+str(time)+"&S5=2000&S6=&S7=1&S8=0123456789&S9=1000")
    print("success")
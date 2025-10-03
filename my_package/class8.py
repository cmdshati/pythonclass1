## module ...
## python e ekekta file e hocce module.. 
# ekta file er vhetor j variable ba list tuple jake nm dhore daka jai. segula onno module b afile e acces kora jai ..tobe age import kore nite hobe..

import class7, my_module
print(class7.string)


def foo(a,b):
    return a+b

m=class7.m
n=class7.n

# print(foo(class7.m, class7.n))
print(foo(m,n))
print(class7.my_func(2,7)+10)

print(class7.i)

print(class7.name)
print(my_module.name)

##default module ..
#date and time..

import datetime
a= datetime.datetime.now()
print(a.strftime("%H"))  ##  24 hour e dekai... like 21 ta
print(a.strftime("%a"))  ##  day  short form e dekay..like thu..
print(a.strftime("%A"))  ##  day fuul form e dekay.. thursday..
print(a.strftime("%d"))  ## month er kon tarik like 2 tarik..
print(a.strftime("%I"))  ## 12 hour e time dekay..like 9 ta ..
print(a.strftime("%h"))  ## kon month seta short form e dekay..like Oct..
print(a.strftime("%B"))  ## kon month seta full form e dekabe..like October..
print(a.strftime("%Y"))  ## kon year seta full form e dekabe..like 2025..
print(a.strftime("%y"))  ##  kon yer eta shortly dekabe.. like 25..
print(a.strftime("%p"))  ## am nki pm seta  dekabe..
print(a.strftime("%H : %M : %S %p"))  #hour minute second sb dekabe..
print(a.strftime("%I:%M:%S %p"))  #hour minute second sb dekabe..
print(a.strftime("%j"))  ## bochorer koto tomo day seta ber kora jbe..


## finding timezone..
from zoneinfo import ZoneInfo
from datetime import datetime

## kintu ekhane first time error show hoice karon amr amr timezine data install kora nei..
## tai termine e commnad likhe timezone data install korte hbe..
## command ti hocce...pip install tzdata


dhaka = datetime.now(ZoneInfo("Asia/Dhaka"))
print(dhaka)

Kolkata = datetime.now(ZoneInfo("Asia/Kolkata"))
print(Kolkata)

##jegulate duit aword ache..sgulo Underscore diye likte hobe.. like New_York , Los_Angles 
america = datetime.now(ZoneInfo("America/New_York"))
print(america)

singapore = datetime.now(ZoneInfo("Asia/Singapore"))
print(singapore)

# folder create and delete kora using import os 

import os 

#new folder create kora..
# os .mkdir("New")
# folder ta delete kotra..
# os.rmdir("New")  # folder delete korar jonno rmdir remove directory..

# ar file delete korar jonno  os .remove 
# os.remove("my_file.txt")

#working  directory ber kora..(cwd)
x= os. getcwd()
print(x)
y= os.listdir(x)
print(y)


##pip --python package  installer ..
#PyPI - python Package Index.. -- python er package er  online repository...
#mne developer ra packge create kore online repository te upload kore ... ar je keu tr projone pip install  diye ter end e install korte pre..and project e use korte pre..

import requests as r 
respone = r.get("http://google.com")
print(respone.status_code)

import requests 
respone = requests.get("http://google.com")
print(respone.status_code)


import requests 
respone = requests.post("http://google.com")
print(respone.status_code)












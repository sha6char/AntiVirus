import requests
import os
url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': "3365946f439ad2763ff7ce6d9feb360608091af7cab2663a04e1cddef875d452"}

def results(resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report' 
    params = {'apikey': "3365946f439ad2763ff7ce6d9feb360608091af7cab2663a04e1cddef875d452" ,'resource': resource}
    response = requests.get(url, params=params)
    res = str(response.json())
    result = res.split(",")
    result = str(result[-3])
    result = result[-1:]
    if result == '0':
        print ("no virus detected")
    else:
        print (result+"  viruses was detected")

def p1(fole,list):
    if  fole > len(list)-1 :
        print ("finished")
    else:
        print(list[fole])
        files = {'file': (list[fole], 'rb')}
        response = requests.post(url, files=files, params=params)
        dic= str(response.json())
        resource = dic.split(",")
        resource = str(resource[2][14:-1])
        print (resource)
        results(resource)
        p1 (fole+1,list)
list = os.listdir("C:/Users/sha6c/OneDrive/שולחן העבודה/לימודים - ט/תנך")
p1(0,list)

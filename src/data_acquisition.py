import os
import time
import requests
import sys

def retrieve_html():
    
'''
    Collect San Francisco weather data.
    Example: https://en.tutiempo.net/climate/mm-yyyy/ws-724940.html
'''

    for yyyy in range(2010,2021):
        for mm in range(1,13):
            # if mm < 10, there are two digits with leading 0 otherwise no leading zero.
            if(mm<10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-725300.html'.format(mm, yyyy)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-725300.html'.format(mm, yyyy)        
            
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            
            if not os.path.exists("../data/html_data/{}".format(yyyy)):
                os.makedirs("../data/html_data/{}".format(yyyy))
            with open("../data/html_data/{}/{}.html".format(yyyy,mm),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush() 
        
if __name__=="__main__":
    start = time.time()
    retrieve_html()
    stop = time.time()
    print("Time taken {}".format(stop - start))
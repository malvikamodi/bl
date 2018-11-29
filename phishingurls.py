from gglsbl import SafeBrowsingList
#import pandas
import time
import csv
#data = pandas.read_csv('verified_online.csv')
#urls = data.url.tolist()


def find_blacklisted_domains(urls):
    total_count=0
    count=0
    start_time = time.time()

    sbl = SafeBrowsingList('AIzaSyBHPCVVk-tbM0iC93uvulfEFTyBfmKecVA')
    #sbl = SafeBrowsingList('AIzaSyCj6PXcG8IuHW3cpVB5dZHVWHb2QnALWSU')
    for url in urls:
        threat_list = sbl.lookup_url(url)
        if threat_list:
            count+=1
            with open(r'blacklist.txt', 'a') as f:
               f.write(url)
        
        total_count+=1

    elapsed_time = time.time() - start_time
    print("Number of URLS:"+str(total_count))
    print("Phishing URLS:"+str(count))
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    fields=[str(total_count),str(count)]
    with open(r'results.csv', 'a') as f:
       writer = csv.writer(f)
       writer.writerow(fields)
    

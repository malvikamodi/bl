from gglsbl import SafeBrowsingList
import pandas
import time

# your script
sbl = SafeBrowsingList('AIzaSyCj6PXcG8IuHW3cpVB5dZHVWHb2QnALWSU')
#sbl = SafeBrowsingList('AIzaSyBHPCVVk-tbM0iC93uvulfEFTyBfmKecVA')
data = pandas.read_csv('verified_online.csv')
urls = data.url.tolist()

total_count=0
count=0
start_time = time.time()

for url in urls:
	threat_list = sbl.lookup_url(url)
	if threat_list == None:
		print("no threat")

	else:
		#print('threats: ' + str(threat_list))
		count+=1

	total_count+=1


elapsed_time = time.time() - start_time
print("Number of URLS:"+str(total_count))
print("Phishing URLS:"+str(count))
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))




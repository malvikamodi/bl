from  elasticsearch import Elasticsearch
from phishingurls import find_blacklisted_domains
import json
import time

host = "192.168.0.15"
port = 9200
domains=[]
es = Elasticsearch(
    [
        {
            'host': host,
            'port': port
        }
    ],
    timeout=1000
) 

page = es.search(
  index = 'dns-data',
  scroll = '2m',
  size = 1000,
  body = { "_source": "domain_name", "query": {"bool": {"must": [{"match": {"is_registered": "true"}}]}} })
    
sid = page['_scroll_id'] 
scroll_size = page['hits']['total']
  
def process_hits(hits):
    for item in hits:
        #obj = json.dumps(item, indent=2)
        domains.append(item["_source"]["domain_name"])
    
    if len(domains)>200000:
        find_blacklisted_domains(domains)
        domains.clear()

start_time = time.time()
  # Start scrolling
while (scroll_size > 0):
    #print ("Scrolling...")
    page = es.scroll(scroll_id = sid, scroll = '2m')
    # Update the scroll ID
    sid = page['_scroll_id']
    # Get the number of results that we returned in the last scroll
    scroll_size = len(page['hits']['hits'])
    print ("scroll size: " + str(scroll_size))
    # Do something with the obtained pagee
    process_hits(page['hits']['hits'])
    
elapsed_time = time.time() - start_time
print("Time Taken: "+time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

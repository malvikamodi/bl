from  elasticsearch import Elasticsearch
from phishingurls import find_blacklisted_domains
import json
import time
import datetime
from update_body import *

batch_size = 200000
host = "192.168.0.15"
port = 9200
domains=[]
info = {}
listnames = ["safebrowsing"]

es = Elasticsearch(
    [
        {
            'host': host,
            'port': port
        }
    ],
    timeout=1000
)

info = {}
listnames = ["safebrowsing","phishtank"]

def isBlacklisted(domain,value):
	return value

def find_blacklisted_domains(info):
	add = []
	remove = []

	for name in listnames:
		for record in info:
			result = isBlacklisted(record, False)

			if(info[record][name]["is_blacklisted"]==False and result==True):
				add.append((record,name))

			if(info[record][name]["is_blacklisted"]==True and result==False):
				remove.append((record,name))
	


	print("ADD:",add)
	print("REMOVE:",remove)
	return add, remove

def process_hits(hits):

	for item in hits:
		domain_name = item["_source"]["domain_name"]
		info[domain_name] = {}
		info[domain_name]["id"] = item["_id"]
		info[domain_name]["route"] = item["_routing"]

		for name in listnames:
			info[domain_name][name] = {}
			info[domain_name][name]["is_blacklisted"] = False

			if "blacklists" in item["_source"]:
				if name in item["_source"]["blacklists"]:
					info[domain_name][name]["is_blacklisted"] = item["_source"]["blacklists"][name]["is_blacklisted"]


	if len(info)>0:
		add, remove = find_blacklisted_domains(info)

		for record in add:
			domain_name, name = record
			uid = info[domain_name]["id"]
			route = info[domain_name]["route"]

			if(name=="safebrowsing"):
				body = body_sb_add

			elif(name=="phishtank"):
				body = body_phishtank_add

			#print(record, body)
			doc = es.update(index='dns-data-local', doc_type='RECORD',routing=route, id=uid, body=body)

		for record in remove:
			domain_name, name = record
			uid = info[domain_name]["id"]
			route = info[domain_name]["route"]

			if(name=="safebrowsing"):
				body = body_sb_remove

			elif(name=="phishtank"):
				body = body_phishtank_remove
			
			doc = es.update(index='dns-data-local', doc_type='RECORD',routing=route, id=uid, body=body)

        #Add is the list of all domains where we need to append to add history and set isBlacklisted as True
        #Remove is the list of all domains where we need to append to delete history and set isBlacklisted as False  


page = es.search(
  index = 'dns-data-local',
  scroll = '2m',
  size = 1000,
  body = { "query": {"bool": {"must": [{"match": {"is_registered": "true"}}]}} })

process_hits(page['hits']['hits'])



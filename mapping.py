from  elasticsearch import Elasticsearch

host = "192.168.0.15"
port = 9200

es = Elasticsearch(
    [
        {
            'host': host,
            'port': port
        }
    ],
    timeout=1000
)

mapping_update = {
		"RECORD":{
        "properties": {
        "blacklists":{
		"type": "nested",
		"properties":{
		"safebrowsing" : {"type": "nested",
						 "properties":{
						 		"blacklist_add_history": {"type": "date"},
						 		"blacklist_remove_history": {"type": "date"},
						 		"is_blacklisted":{"type":"boolean", "store":True}

						 	 }},

		"phishtank" : {"type": "nested",
						 "properties":{
						 		"blacklist_add_history": {"type": "date"},
						 		"blacklist_remove_history": {"type": "date"},
						 		"is_blacklisted":{"type":"boolean", "store":True}

						 	 }}
		}
	}#BLACKLISTS
	}#PROPERTIES
	}#RECORD

}#MAPPING_UPDATE

es.indices.put_mapping(index = 'dns-data', doc_type = "RECORD", body = mapping_update)

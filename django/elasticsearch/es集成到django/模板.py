# search app
import pdb

import elasticsearch


articlemapping = {
    "mappings" : {
		"article" : {
            "_all": {
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "term_vector": "no",
                    "store": "false"
                    },
            "properties" : {
                    "title" : {
                                "type" : "string",
                                "analyzer": "ik_max_word",
                                "search_analyzer": "ik_max_word",
                                "include_in_all": "true",
                                "boost": 8
                                },
                    "body" : {
                                "type" : "string",
                                "analyzer": "ik_max_word",
                                "search_analyzer": "ik_max_word",
                                "include_in_all": "true",
                                "boost": 8
                                },
                    "status" : {
                                "type" : "integer",
                                "analyzer": "ik_max_word",
                                "search_analyzer": "ik_max_word",
                                "include_in_all": "true",
                                "boost": 8
                                },
                    "article_type" : {
                                "type" : "integer",
                                "analyzer": "ik_max_word",
                                "search_analyzer": "ik_max_word",
                                "include_in_all": "true",
                                "boost": 8
                                },
                    "category" : {
                                "type" : "string",
                                "analyzer": "ik_max_word",
                                "search_analyzer": "ik_max_word",
                                "include_in_all": "true",
                                "boost": 8
                                },
                    "tags" : {
                                "type" : "string",
                                "analyzer": "ik_max_word",
                                "search_analyzer": "ik_max_word",
                                "include_in_all": "true",
                                "boost": 8
                                },
                    }
            }
        }
    }

class ES(object):
    def __init__(self,mapping,index_name,doc_type):
       self.mapping = mapping
       self.index_name = index_name
       self.doc_type = doc_type
    
	@classmethod
    def connect_host(cls):

        host  =  ["http://127.0.0.1:9200"]
        es = elasticsearch.Elasticsearch(
             host,
             #sniff_on_start=True,
             #sniff_on_connection_fail=True,
             #sniffer_timeout=600
        )
        return es
	
    def sync_es(self,data,id_num):
        #pdb.set_trace()
        #`es_mapping = self.mapping
        es = self.connect_host()
        if not es.indices.exists(self.index_name):
           es.indices.create(index=self.index_name,ignore=True)
        return es.index(index=self.index_name,doc_type=self.doc_type,body=data,id=id_num) 


if __name__ == "__main__":
	es_data  = {'body': 'hello word', 'status': 0, 'author': 'bskFLldf', 'title': 'hello', 'article_type': 1, 'category': "", 'tags': []}
	es1 = ES(mapping=articlemapping,index_name="article",doc_type="article")
	es1.sync_es(es_data,1)
import sys
from elasticsearch import Elasticsearch

sys.path.append('.')

def test_connect():
    # es = Elasticsearch(f"https://{host}:{port}", basic_auth=(username, password), verify_certs=verify_certs)
    es = Elasticsearch(["https://localhost:9200"],
                       basic_auth=('elastic', '_98dKU-=2J_pkreMXew6'),
                       verify_certs=False, 		# no verify SSL certificates
                       )
    print(es.info())
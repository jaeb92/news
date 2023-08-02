import yaml
import typing as t
from datetime import datetime
from elasticsearch import Elasticsearch
from elastic_transport import ObjectApiResponse

class ElasticSearch:
    
    def __init__(self) -> None:
        """_summary_

        Raises:
            ConnectionError: _description_
        """
        
        with open('es_config.yaml', 'r') as f:
            es_config = yaml.load(f, Loader=yaml.FullLoader)
            hostname = es_config['host']
            port = es_config['port']
            username = es_config['username']
            password = es_config['password']
            verify_certs = es_config['verify_certs']
            
        self.es = Elasticsearch(f"https://{hostname}:{port}", basic_auth=(username, password), verify_certs=verify_certs)
        if not self.es.info():
            raise ConnectionError
    

    def __str__(self) -> str:
        """
        print elasticsearch information

        Returns:
            str: information of elasticsearch
        """
        return f"{self.es.info()}"
    
    
    def get_all_indexes(self) -> None:
        """
        get list of all indexes 

        Returns:
            list: list of all indexes
        """
        return sorted(self.es.indices.get_alias(index="*"))
    
    
    def create_index(self, index: str, index_body: dict) -> ObjectApiResponse[t.Any]:
        """
        create index 

        Args:
            index_name (str): name of index
            index_body (dict): mappings and settings of index

        Returns:
            ObjectApiResponse: result of creating index
        """
        
        response = self.es.indices.create(index=index, body=index_body)
        
        return response

    
    def delete_index(self, index: str):
        """
        delete index

        Args:
            index (str): name of index

        Returns:
            _type_: _description_
        """
        delstr = input(f"delete {index}, are you sure? (y/n)")
        if delstr.lower() == 'y':
            self.es.indices.delete(index=index, ignore=[400, 404])
        else:
            return ""

    
    
    def search_all(self, index: str) -> dict:
        """
        search all documents from index

        Args:
            index (str): name of index

        Returns:
            dict: list all of documents from index
        """
        return [doc for doc in self.es.search(index=index, query={"match_all":{}})['hits']['hits']]
        
    
    def search_by_id(self, index: str, id: int) -> dict:
        """
        search document by id

        Args:
            index (str): name of index
            id (int): id of document

        Returns:
            dict: document
        """
        return self.es.search(index=index, body={"query": {"match": {"id": id}}})['hits']
    
    def insert(self, index: str, document: dict) -> ObjectApiResponse:
        """
        insert document 

        Args:
            index (str): name of index
            document (dict): document which is inserted to index

        Returns:
            ObjectApiResponse: result of insert document
        """
        try:
            res = self.es.index(index=index, document=document)
        except Exception as e:
            res = None
            print(e)
            
        return res
    
    
    def insert_bulk(self, index: str, document: list) -> ObjectApiResponse:
        """
        insert document for bulk

        Args:
            index (str): name of index
            document (list): list of documents

        Returns:
            ObjectApiResponse: result of bulk inserting
        """
        
        try:
            res = self.es.bulk(index, document)
        except Exception as e:
            res = None
            
        return res    

    
    def update(self, id: str, doc: dict) -> ObjectApiResponse:
        """
        update document by document d

        Args:
            id (str): document id
            doc (dict): {'field1': 'value', 'field2': 'value', ... }

        Returns:
            ObjectApiResponse: result of bulk inserting
        """
        try:
            res = self.es.update(index='인덱스명', id = id, body = {"doc": doc})
        except Exception as e:
            res = None
            
        return res
    
    
    def delete(self, index: str, id: str) -> ObjectApiResponse:
        """
        
        delete document by id

        Args:
            index (str): name of index
            id (str): document id

        Returns:
            ObjectApiResponse: result of deleting document
        """
        
        try:
            res = self.es.delete_by_query(index=index, doc_type="_doc", id=id)
        except Exception as e:
            res = None

        return res
    
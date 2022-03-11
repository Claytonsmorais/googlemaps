from neo4j import GraphDatabase
import os

class Database():
    def __init__(self):
        uri = os.environ['NEO4J_URI']
        driver = GraphDatabase.driver(uri,
                                      auth=(os.environ['NEO4J_USER'], os.environ['NEO4J_PASSWORD'])
                                      )
        self.driver = driver

    def close(self):
        self.driver.close()

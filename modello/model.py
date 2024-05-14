import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self.grafo = nx.Graph()
        self.paesi = DAO.getAllCountries()
        # Costruisco un dizionario per avere associato ad ogni codice un oggetto "Paese"
        self.idMap = {}
        for p in self.paesi:
            self.idMap[p.CCode] = p

    def buildGraph(self):
        self.grafo.add_nodes_from(self.paesi)

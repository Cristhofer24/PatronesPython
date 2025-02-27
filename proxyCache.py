from abc import ABC, abstractmethod
import time
class DataFechert(ABC):
    @abstractmethod
    def fetch_data(self,query:str)-> str:
        pass
    
class RealDataFetcher(DataFechert):
    def fetch_data(self,query:str)-> str:
        print(f"consultando Datos para '{query}'.....(esto puede tardar unos segundos)")
        time.sleep(3)
        return f"Informacion para {query}"
class CacheProxy(DataFechert):
    def __init__(self):
        self.real_fetcher = RealDataFetcher()
        self.cache = {}

    def fetch_data(self, query: str) -> str:
        if query in self.cache:
            print(f"Usando caché para '{query}'")
            return self.cache[query]
        
        data = self.real_fetcher.fetch_data(query)
        self.cache[query] = data  
        return data
    
if __name__ == "__main__":
    proxy = CacheProxy()
    print(proxy.fetch_data("Datos empresariales"))
    
    print(proxy.fetch_data("Datos empresariales"))
    
    
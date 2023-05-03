from email.policy import HTTP
import random
from typing import List
from models.proxy_model import ProxyModel
import aiohttp
from aiohttp import ClientTimeout
from requests.auth import HTTPProxyAuth
from settings import settings

class ProxyManager():
    proxies: ProxyModel =[]
    
    def loadProxies(self, new_proxies: List[ProxyModel]):
        try:
            for p in new_proxies:
                self.proxies.append(p)
        except:
            raise Exception("Error loading proxies!")
    
    def getProxy(self):
        try:
            r = random.randint(0, len(self.proxies) - 1)
            return self.proxies[r]
        except:
            raise Exception("Error looking for another proxy!")
    
    async def fetch(self,url, headers, *args):
        proxy = self.getProxy()
        proxy_request = proxy.request_proxy()
        try:
            async with aiohttp.ClientSession(timeout=ClientTimeout(600)) as session:
                response = await session.get(url, proxy=proxy_request, headers=headers)
                response = await response.text()
        except:
            raise Exception("Could not fetch url!")
        else:
            proxy.success()
        finally:
            proxy.fail()

        return response


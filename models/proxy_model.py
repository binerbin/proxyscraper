from tokenize import String


class ProxyModel():
    _proxies = set()

    @property
    def proxy(self):
        return self._proxy

    def __init__(self, proxy: String, username: String, password: String):
        # Unique Proxies only
        self._proxy = proxy
        self.username = username
        self.password = password
        self.used = 0
        self.failed = 0

    def request_proxy(self):
        format = f'http://{self.username}:{self.password}@{self.proxy}'
        return format

    def success(self):
        self.used+= 1
    
    # Return True if it the fail has not hit its max fail attempts before being removed.
    def fail(self):
        self.failed += 1

        if self.failed > 5:
            return False
        
        return True
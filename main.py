import requests


class TradeOgre:
    # Unauthenticated instantiation
    def __init__(self):
        self.uri = "https://tradeogre.com/api/v1"

    # Authenticated instantiation
    def __init__(self, apikey, public, private):
        self.uri = "https://tradeogre.com/api/v1"
        self.apiKey = apikey
        self.publicKey = public
        self.privateKey = private

    # Methods not requiring authentication
    def list_markets(self):
        r = requests.get(self.uri + "/markets")
        return r.json()

    def get_order_book(self, market: str):
        r = requests.get(self.uri + "/orders/" + market)
        return r.json()

    def get_ticker(self, market: str):
        r = requests.get(self.uri + "/ticker/" + market)
        return r.json()

    def get_trade_history(self, market: str):
        r = requests.get(self.uri + "/history/" + market)
        return r.json()

    # Methods requiring authentication
    def get_balances(self):
        if(self.checkifauthenticated):
            r = requests.get(self.uri + "/account/balances")
            return r.json()

    # Helper functions
    def checkifauthenticated(self):
        if self.apiKey is None or self.publicKey is None or self.privateKey is None:
            return False
        else:
            return True

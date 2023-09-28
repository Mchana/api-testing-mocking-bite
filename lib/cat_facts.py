class CatFacts:

    def __init__(self, requester,response):
        self.requester = requester
        self.response = response

    def provide(self):
        return f"Cat fact: {self.requester._get_cat_fact().json()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.requester.get("'https://catfact.ninja/fact'")
        return response.json()
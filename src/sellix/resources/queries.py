def get_queries(self):
    return self.handle_response(
        self.request("/queries"),
        "queries"
    )


def get_query(self, uniqid):
    return self.handle_response(
        self.request(f"/queries/{uniqid}"),
        "query"
    )


def reply_query(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/queries/reply/{uniqid}", "POST", kwargs)
    )


def close_query(self, uniqid):
    return self.handle_response(
        self.request(f"/queries/close/{uniqid}", "POST", [])
    )


def reopen_query(self, uniqid):
    return self.handle_response(
        self.request(f"/queries/reopen/{uniqid}", "POST", [])
    )

def get_blacklists(self):
    return self.handle_response(
        self.request("/blacklists"),
        "blacklists"
    )


def create_blacklist(self, **kwargs):
    return self.handle_response(
        self.request("/blacklists", "POST", kwargs),
        "uniqid"
    )


def get_blacklist(self, uniqid):
    return self.handle_response(
        self.request(f"/blacklists/{uniqid}"),
        "blacklist"
    )


def update_blacklist(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/blacklists/{uniqid}", "PUT", kwargs)
    )


def delete_blacklist(self, uniqid):
    return self.handle_response(
        self.request(f"/blacklists/{uniqid}", "DELETE")
    )

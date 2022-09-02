def get_whitelists(self):
    return self.handle_response(
        self.request("/whitelists"),
        "whitelists"
    )


def create_whitelist(self, **kwargs):
    return self.handle_response(
        self.request("/whitelists", "POST", kwargs),
        "uniqid"
    )


def get_whitelist(self, uniqid):
    return self.handle_response(
        self.request(f"/whitelists/{uniqid}"),
        "whitelist"
    )


def update_whitelist(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/whitelists/{uniqid}", "PUT", kwargs)
    )


def delete_whitelist(self, uniqid):
    return self.handle_response(
        self.request(f"/whitelists/{uniqid}", "DELETE")
    )

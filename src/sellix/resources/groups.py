def get_groups(self):
    return self.handle_response(
        self.request("/groups"),
        "groups"
    )


def create_group(self, **kwargs):
    return self.handle_response(
        self.request("/groups", "POST", kwargs),
        "uniqid"
    )


def get_group(self, uniqid):
    return self.handle_response(
        self.request(f"/groups/{uniqid}"),
        "group"
    )


def update_group(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/groups/{uniqid}", "PUT", kwargs)
    )


def delete_group(self, uniqid):
    return self.handle_response(
        self.request(f"/groups/{uniqid}", "DELETE")
    )

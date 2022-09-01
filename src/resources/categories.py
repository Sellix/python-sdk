def get_categories(self):
    return self.handle_response(
        self.request("/categories"),
        "categories"
    )


def create_category(self, **kwargs):
    return self.handle_response(
        self.request("/categories", "POST", kwargs),
        "uniqid"
    )


def get_category(self, uniqid):
    return self.handle_response(
        self.request(f"/categories/{uniqid}"),
        "category"
    )


def update_category(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/categories/{uniqid}", "PUT", kwargs)
    )


def delete_category(self, uniqid):
    return self.handle_response(
        self.request(f"/categories/{uniqid}", "DELETE")
    )

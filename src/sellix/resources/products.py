def get_products(self):
    return self.handle_response(
        self.request("/products"),
        "products"
    )


def create_product(self, **kwargs):
    return self.handle_response(
        self.request("/products", "POST", kwargs),
        "uniqid"
    )


def get_product(self, uniqid):
    return self.handle_response(
        self.request(f"/products/{uniqid}"),
        "product"
    )


def update_product(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/products/{uniqid}", "PUT", kwargs)
    )


def delete_product(self, uniqid):
    return self.handle_response(
        self.request(f"/products/{uniqid}", "DELETE")
    )

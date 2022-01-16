def get_customers(self):
    return self.handle_response(
        self.request("/customers"),
        "customers"
    )


def create_customer(self, **kwargs):
    return self.handle_response(
        self.request("/customers", "POST", kwargs),
        "customer_id"
    )


def get_customer(self, id):
    return self.handle_response(
        self.request(f"/customers/{id}"),
        "customer"
    )


def update_customer(self, id, **kwargs):
    return self.handle_response(
        self.request(f"/customers/{id}", "PUT", kwargs)
    )

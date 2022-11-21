def get_orders(self):
    return self.handle_response(
        self.request("/orders"),
        "orders"
    )


def get_order(self, uniqid):
    return self.handle_response(
        self.request(f"/orders/{uniqid}"),
        "order"
    )

def update_order(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/orders/update/{uniqid}", "PUT", kwargs)
    )

def issue_order_replacement(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/orders/replacement/{uniqid}", "POST", kwargs)
    )
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

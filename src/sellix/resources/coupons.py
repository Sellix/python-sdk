def get_coupons(self):
    return self.handle_response(
        self.request("/coupons"),
        "coupons"
    )


def create_coupon(self, **kwargs):
    return self.handle_response(
        self.request("/coupons", "POST", kwargs),
        "uniqid"
    )


def get_coupon(self, uniqid):
    return self.handle_response(
        self.request(f"/coupons/{uniqid}"),
        "coupon"
    )


def update_coupon(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/coupons/{uniqid}", "PUT", kwargs)
    )


def delete_coupon(self, uniqid):
    return self.handle_response(
        self.request(f"/coupons/{uniqid}", "DELETE")
    )

def create_payment(self, **kwargs):
    return self.handle_response(
        self.request("/payments", "POST", kwargs),
        {
            "oneOf": [
                "url,uniqid",
                "invoice"
            ],
        }
    )


def delete_payment(self, uniqid):
    return self.handle_response(
        self.request(f"/payments/{uniqid}", "DELETE")
    )

def get_subscriptions(self):
    return self.handle_response(
        self.request("/subscriptions"),
        "subscriptions"
    )


def create_subscription(self, **kwargs):
    return self.handle_response(
        self.request("/subscriptions", "POST", kwargs),
        {
            "oneOf": [
                "url,uniqid",
                "subscription_id"
            ],
        }
    )


def get_subscription(self, id):
    return self.handle_response(
        self.request(f"/subscriptions/{id}"),
        "subscription"
    )


def delete_subscription(self, id):
    return self.handle_response(
        self.request(f"/subscriptions/{id}", "DELETE")
    )

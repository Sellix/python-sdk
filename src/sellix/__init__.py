import requests


class Sellix:
    from .resources.blacklist import get_blacklists, create_blacklist, get_blacklist, update_blacklist, delete_blacklist
    from .resources.categories import get_categories, create_category, get_category, update_category, delete_category
    from .resources.coupons import get_coupons, create_coupon, get_coupon, update_coupon, delete_coupon
    from .resources.feedback import get_feedback, reply_feedback
    from .resources.orders import get_orders, get_order
    from .resources.payments import create_payment, delete_payment
    from .resources.products import get_products, create_product, get_product, update_product, delete_product
    from .resources.queries import get_queries, get_query, reply_query, close_query, reopen_query
    from .resources.whitelists import get_whitelists, create_whitelist, get_whitelist, update_whitelist, delete_whitelist
    from .resources.customers import get_customers, create_customer, get_customer, update_customer
    from .resources.subscriptions import get_subscriptions, create_subscription, get_subscription, delete_subscription
    from .test import sellix_test_sdk

    class SellixException(Exception):
        def __init__(self, message, code):
            super().__init__(self, message, code)

    def __init__(self, api_key, merchant=""):
        self.api_key = api_key
        self.merchant = merchant
        self.api_endpoint = 'https://dev.sellix.io/v1'

    def handle_response(self, response, key=None):
        if response["status"] != 200:
            raise self.SellixException(response["error"], response["status"])

        if not key:
            return None

        if isinstance(key, dict) and "oneOf" in key:
            new_response = {}
            for one_key in key["oneOf"]:
                if "," in one_key:
                    one_key = one_key.split(',')
                    for k in one_key:
                        if k in response["data"]:
                            new_response[k] = response["data"][k]
                elif one_key in response["data"]:
                    return response["data"][one_key]
            return new_response
        elif key in response["data"]:
            return response["data"][key]

    def request(self, component, action="get", payload={}):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        if self.merchant:
            headers["X-Sellix-Merchant"] = self.merchant

        action = getattr(requests, action.lower(), None)
        if action:
            return action(headers=headers,
                          url=f"{self.api_endpoint}{component}",
                          json=payload).json()

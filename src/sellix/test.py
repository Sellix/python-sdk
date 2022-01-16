def sellix_test_sdk(self, components=[]):
    if not components:
        return
    try:
        if "blacklists" in components:
            print("Testing blacklists")
            blacklist_uniqid = self.create_blacklist(
                type="EMAIL", data="sample@gmail.com", note="demo")
            print("Create blacklist passed ✓")
            self.get_blacklist(blacklist_uniqid)
            print("  Get blacklist passed ✓")
            self.get_blacklists()
            print("  Get blacklists passed ✓")
            self.update_blacklist(blacklist_uniqid, type="EMAIL",
                                  data="sample@gmail.com", note="demo")
            print("  Update blacklist passed ✓")
            self.delete_blacklist(blacklist_uniqid)
            print("  Delete blacklist passed ✓")

        if "whitelists" in components:
            print("Testing whitelists")
            whitelist_uniqid = self.create_whitelist(
                type="EMAIL", data="sample@gmail.com", note="demo")
            print("  Create whitelist passed ✓")
            self.get_whitelist(whitelist_uniqid)
            print("  Get whitelist passed ✓")
            self.get_whitelists()
            print("  Get whitelists passed ✓")
            self.update_whitelist(whitelist_uniqid, type="EMAIL",
                                  data="sample@gmail.com", note="demo")
            print("  Update whitelist passed ✓\n")
            self.delete_whitelist(whitelist_uniqid)
            print("  Delete whitelist passed ✓")

        if "categories" in components:
            print("Testing categories")
            category_uniqid = self.create_category(title="Software",
                                                   unlisted=False,
                                                   products_bound=[],
                                                   sort_priority=0)
            print("  Create category passed ✓")
            self.get_category(category_uniqid)
            print("  Get category passed ✓")
            self.get_categories()
            print("  Get categories passed ✓")
            self.update_category(category_uniqid, title="Software",
                                 unlisted=False, products_bound=[], sort_priority=0)
            print("  Update category passed ✓")
            self.delete_category(category_uniqid)
            print("  Delete category passed ✓")

        if "coupons" in components:
            print("Testing coupons")
            coupon_uniqid = self.create_coupon(code="TESTING_COUPON",        discount_value=35,
                                               max_uses=50,
                                               products_bound=[],
                                               discount_type="PERCENTAGE",
                                               disabled_with_volume_discounts=True)
            print("  Create coupon passed ✓")
            self.get_coupon(coupon_uniqid)
            print("  Get coupon passed ✓")
            self.get_coupons()
            print("  Get coupons passed ✓")
            self.update_coupon(coupon_uniqid, code="TESTING_COUPON",        discount_value=35,
                               max_uses=50,
                               products_bound=[],
                               discount_type="PERCENTAGE",
                               disabled_with_volume_discounts=True)
            print("  Update coupon passed ✓")
            self.delete_coupon(coupon_uniqid)
            print("  Delete coupon passed ✓")

        if "feedback" in components:
            print("Testing feedback")
            feedback_list = self.get_feedback()
            print("  List feedback passed ✓")
            if feedback_list:
                feedback_uniqid = feedback_list[0]["uniqid"]
                self.get_feedback(feedback_uniqid)
                print("  Get feedback passed ✓")
                self.reply_feedback(feedback_uniqid, reply="Testing Reply")
                print("  Reply feedback passed ✓")

        if "orders" in components:
            print("Testing orders")
            orders = self.get_orders()
            print("  Get orders passed ✓")
            if orders:
                self.get_order(orders[0]["uniqid"])
                print("  Get order passed ✓")

        if "products" in components:
            print("Testing products")
            product_uniqid = self.create_product(title="Software Activation Keys",
                                                 price=12.5,
                                                 description="Product description example.",
                                                 currency="EUR",
                                                 gateways=[
                                                     "PAYPAL", "STRIPE", "BITCOIN"],
                                                 type="SERIALS",
                                                 serials=[
                                                     "activation-key-#1"
                                                 ])
            print("  Create product passed ✓")
            self.get_product(product_uniqid)
            print("  Get product passed ✓")
            self.get_products()
            print("  Get products passed ✓")
            self.update_product(product_uniqid, title="Software Activation Keys",
                                price=12.5,
                                description="Product description example.",
                                currency="EUR",
                                gateways=["PAYPAL", "STRIPE", "BITCOIN"],
                                type="SERIALS",
                                serials=[
                                    "activation-key-#1"
                                ])
            print("  Update product passed ✓")
            self.delete_product(product_uniqid)
            print("  Delete product passed ✓")

        if "queries" in components:
            print("Testing queries")
            queries = self.get_queries()
            print("  Get queries passed ✓")
            if queries:
                self.get_query(queries[0]["uniqid"])
                print("  Get query passed ✓")
                self.reply_query(queries[0]["uniqid"],
                                 reply="this is a demo reply"
                                 )
                print("  Reply query passed ✓")
                self.close_query(queries[0]["uniqid"])
                print("  Close query passed ✓")
                self.reopen_query(queries[0]["uniqid"])
                print("  Reopen query passed ✓\n")

        if "payments" in components:
            print("Testing payments")

            payment_no_white_label = self.create_payment(title="Sellix Payment",
                                                         value=1.5,
                                                         currency="EUR",
                                                         quantity=5,
                                                         email="no-reply@sellix.io",
                                                         white_label=False,
                                                         return_url="https://sample.sellix.io/return")
            print("  Create payment no white label passed ✓")
            payment_white_label = self.create_payment(title="Sellix Payment",
                                                      value=1.5,
                                                      currency="EUR",
                                                      quantity=5,
                                                      email="no-reply@sellix.io",
                                                      white_label=True,
                                                      return_url="https://sample.sellix.io/return")
            print("  Create payment white label passed ✓")
            self. delete_payment(payment_no_white_label["uniqid"])
            print("  Delete payment no white label passed ✓")
            self.delete_payment(payment_white_label["uniqid"])
            print("  Delete payment white label passed ✓")

        if "customers" in components:
            print("Testing customers")
            customer_id = self.create_customer(
                email="sample@gmail.com",
                name="James",
                surname="Smith",
                phone="3287261000",
                phone_country_code="IT",
                country_code="IT",
                street_address="St. Rome 404",
                additional_address_info=None,
                city="Rome",
                postal_code="0",
                state="Italy"
            )
            print(customer_id)
            print("  Create customer passed ✓")
            self.get_customer(customer_id)
            print("  Get customer passed ✓")
            self.get_customers()
            print("  Get customers passed ✓")
            self.update_customer(customer_id,
                                 email="sample@gmail.com",
                                 name="James",
                                 surname="Smith",
                                 phone="3287261000",
                                 phone_country_code="IT",
                                 country_code="IT",
                                 street_address="St. Rome 404",
                                 additional_address_info=None,
                                 city="Rome",
                                 postal_code="0",
                                 state="Italy"
                                 )
            print("  Update customer passed ✓")

        if "subscriptions" in components:
            print("Testing subscriptions")
            self.create_subscription(
                product_id="61a8de6277597",
                coupon_code=None,
                custom_fields={
                    "user_id": "demo"
                },
                customer_id="cst_4a30a219a9d7663fdd35",
                gateway=None
            )
            print("  Create subscription passed ✓")
            self.get_subscriptions()
            print("  Get subscriptons passed ✓")
    except self.SellixException as e:
        print(e)

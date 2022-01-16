from sellix import Sellix

# pass <MERCHANT_NAME> only if you need to be authenticated as an additional store

client = Sellix("<MERCHANT_API_KEY>", "<MERCHANT_NAME>")

client.sellix_test_sdk([
    "subscriptions",
])

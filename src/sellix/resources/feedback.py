def get_feedback(self, uniqid=""):
    endpoint = "/feedback"
    if uniqid:
        endpoint += f"/{uniqid}"

    return self.handle_response(
        self.request("/feedback"),
        "feedback"
    )


def reply_feedback(self, uniqid, **kwargs):
    return self.handle_response(
        self.request(f"/feedback/reply/{uniqid}", "POST", kwargs)
    )

class Request:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_headers(self):
        return self.headers

    def set_headers(self, value):
        self.headers = value

    def get_body(self):
        return self.body

    def set_body(self, value):
        self.body = value
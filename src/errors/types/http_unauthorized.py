class HttpUnauthorizedError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.name = "Unauthorized"
        self.status_code = 401
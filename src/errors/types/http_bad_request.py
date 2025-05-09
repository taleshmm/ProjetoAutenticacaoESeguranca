class HttpBadRequestError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.name = "BadRequest"
        self.status_code = 400
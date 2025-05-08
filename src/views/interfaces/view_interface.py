from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HtppResponse

class ViewInterface(ABC):
    
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HtppResponse:
        pass
from abc import ABC, abstractmethod

class LoginCreatorInterface(ABC):
    
    @abstractmethod
    def create(self, usarname: str, password: str) -> dict:
       pass
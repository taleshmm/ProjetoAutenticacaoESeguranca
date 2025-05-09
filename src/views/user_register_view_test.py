from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView
import pytest

class MockController:
    def registry(self, username, password) -> dict:
        return {"test_test": "something"}

def test_handle_user_register():
    body = {
       "username": "test_user",
       "password": "test_password"
    }
    request = HttpRequest(body=body)
    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)
    
    response = user_register_view.handle(request)
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == {"data": {"test_test": "something"}}
    
def test_handle_user_register_invalid_inputs():
    body = {
       "username": "",
       "password": ""
    }
    request = HttpRequest(body=body)
    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)
    
    with pytest.raises(Exception):
        user_register_view.handle(request)
   
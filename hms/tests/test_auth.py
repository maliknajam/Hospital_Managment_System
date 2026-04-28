import unittest
from unittest.mock import patch, MagicMock
from hms.services.auth_service import AuthService
from hms.models.user import User

class TestAuthService(unittest.TestCase):
    
    @patch('hms.services.auth_service.execute_query')
    def test_login_success(self, mock_execute_query):
        # Arrange
        mock_execute_query.return_value = [{
            'id': 1,
            'username': 'admin',
            'password': 'password123',
            'role': 'admin',
            'created_at': '2023-10-01 10:00:00'
        }]
        
        # Act
        user = AuthService.login('admin', 'password123')
        
        # Assert
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.role, 'admin')
        mock_execute_query.assert_called_once()

    @patch('hms.services.auth_service.execute_query')
    def test_login_failure(self, mock_execute_query):
        # Arrange
        mock_execute_query.return_value = []
        
        # Act
        user = AuthService.login('admin', 'wrongpassword')
        
        # Assert
        self.assertIsNone(user)
        mock_execute_query.assert_called_once()

if __name__ == '__main__':
    unittest.main()

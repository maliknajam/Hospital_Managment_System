from hms.utils.db import execute_query
from hms.models.user import User

class AuthService:
    @staticmethod
    def login(username, password):
        """
        Validates user credentials against the database.
        Returns a User object if successful, None otherwise.
        """
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        # Note: In a real application, passwords should be hashed (e.g., using bcrypt).
        # We are using plaintext here for simplicity as requested for a beginner-friendly project.
        result = execute_query(query, (username, password), fetch=True)
        
        if result:
            user_data = result[0]
            return User(
                id=user_data['id'],
                username=user_data['username'],
                password=user_data['password'],
                role=user_data['role'],
                created_at=user_data['created_at']
            )
        return None

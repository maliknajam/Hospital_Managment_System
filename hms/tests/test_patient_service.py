import unittest
from unittest.mock import patch
from hms.services.patient_service import PatientService
from hms.models.patient import Patient

class TestPatientService(unittest.TestCase):

    @patch('hms.services.patient_service.execute_query')
    def test_get_all_patients(self, mock_execute_query):
        # Arrange
        mock_execute_query.return_value = [
            {'id': 1, 'name': 'John Doe', 'age': 30, 'gender': 'Male', 'contact_number': '1234567890', 'address': '123 Main St', 'created_at': None}
        ]
        
        # Act
        patients = PatientService.get_all_patients()
        
        # Assert
        self.assertEqual(len(patients), 1)
        self.assertIsInstance(patients[0], Patient)
        self.assertEqual(patients[0].name, 'John Doe')
        mock_execute_query.assert_called_once()

    @patch('hms.services.patient_service.execute_query')
    def test_add_patient(self, mock_execute_query):
        # Arrange
        mock_execute_query.return_value = 1 # Return last row id
        
        # Act
        result_id = PatientService.add_patient('Jane Doe', 25, 'Female', '0987654321', '456 Elm St')
        
        # Assert
        self.assertEqual(result_id, 1)
        mock_execute_query.assert_called_once()

if __name__ == '__main__':
    unittest.main()

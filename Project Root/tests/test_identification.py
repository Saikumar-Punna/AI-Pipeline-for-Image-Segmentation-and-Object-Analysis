import unittest
from models.identification_model import IdentificationModel

class TestIdentificationModel(unittest.TestCase):
    def setUp(self):
        self.model = IdentificationModel()
    
    def test_identify(self):
        description = self.model.identify("data/segmented_objects/object1.jpg")
        self.assertIsNotNone(description, "No description was generated")

if __name__ == "__main__":
    unittest.main()

import unittest
from models.text_extraction_model import TextExtractionModel

class TestTextExtractionModel(unittest.TestCase):
    def setUp(self):
        self.model = TextExtractionModel()
    
    def test_extract_text(self):
        text = self.model.extract_text("data/segmented_objects/object1.jpg")
        self.assertIsNotNone(text, "No text was extracted")

if __name__ == "__main__":
    unittest.main()

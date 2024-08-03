import unittest
from models.summarization_model import SummarizationModel

class TestSummarizationModel(unittest.TestCase):
    def setUp(self):
        self.model = SummarizationModel()
    
    def test_summarize(self):
        summary = self.model.summarize("Sample text for testing summarization.")
        self.assertIsNotNone(summary, "No summary was generated")

if __name__ == "__main__":
    unittest.main()

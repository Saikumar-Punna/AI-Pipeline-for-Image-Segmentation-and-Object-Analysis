import unittest
from models.segmentation_model import SegmentationModel

class TestSegmentationModel(unittest.TestCase):
    def setUp(self):
        self.model = SegmentationModel()
    
    def test_segment(self):
        masks = self.model.segment("data/input_images/sample.jpg")
        self.assertGreater(len(masks), 0, "No masks were generated")

if __name__ == "__main__":
    unittest.main()

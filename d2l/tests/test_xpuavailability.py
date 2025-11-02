import unittest
import torch

class TestAvailability(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(torch.xpu.is_available(), True, "Should be True")


if __name__ == "__main__":
    unittest.main()
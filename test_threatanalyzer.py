# test_threatanalyzer.py
"""
Tests for ThreatAnalyzer module.
"""

import unittest
from threatanalyzer import ThreatAnalyzer

class TestThreatAnalyzer(unittest.TestCase):
    """Test cases for ThreatAnalyzer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThreatAnalyzer()
        self.assertIsInstance(instance, ThreatAnalyzer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThreatAnalyzer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

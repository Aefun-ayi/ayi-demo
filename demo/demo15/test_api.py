import pytest

"""
   Pytest运行demo
"""

class TestPytest():
    """测试Pytest类"""

    def test_001(self):
        """test_001"""
        print("test_001")
        assert 1 == 1

    def test_002(self):
        """test_002"""
        print("test_002")
        assert 1 < 2

    def test_003(self):
        """test_003"""
        print("test_003")
        assert 1 != 2

    def test_004(self):
        """test_004"""
        print("test_004")
        assert 1 == 0

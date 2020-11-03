import pytest
import yaml

class TestData:
    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./yml.yaml")))
    def test_param(self, a, b):
        print(a+b)
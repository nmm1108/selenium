import pytest
class TestDemo():
    def test_one(self):
        print("开始执行 test_one 方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two 方法")

    def test_three(self):
        print("开始执行 test_three 方法")
        # x = 'this'
        # assert 'h' in x
class  TestDemo1():
    def test_a(self):
        print("开始执行 test_a 方法")
        x = 'this'
        assert 'h' in x
    def test_b(self):
        print("开始执行 test_b 方法")


    def test_c(self):
        print("开始执行 test_c 方法")
        #x = 'this'
        #assert 'h' in x

if __name__ == '__main__':
    #pytest.main("-v -x TestDemo")
    pytest.main(['-v','-s','TestDemo'])




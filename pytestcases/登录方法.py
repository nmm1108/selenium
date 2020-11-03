import pytest

@pytest.fixture()
def login():
    print("这是个需要登录的方法")

def test_case1(login):
    print("test_case1,要登录")


def test_case2():
    print("test_case2,不要登录")


def test_case3(login):
    print("test_case3,要登录")

if __name__ == '__main__':
    pytest.main()

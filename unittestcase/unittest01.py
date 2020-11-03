import unittest
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")
    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(1, 1,"判断是否相等")
        self.assertIn('h','this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1, 2, "判断是否相等")

    @unittest.skipIf(1+1==2,"跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3, 1, "判断是否相等")

class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1_case0")

    def test_demo1_case1(self):
        print("test_demo1_case1")

class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo1_case0")

    def test_demo2_case1(self):
        print("test_demo1_case1")


if __name__ == '__main__':
    #执行指定类下面的某些函数
    # unittest.main()
    # suite= unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo1_case0"))

    # unittest.TextTestRunner().run(suite)

    # 执行指定类的全部测试用例
    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(suiteall)

    #匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    discover = unittest.defaultTestLoader.discover('./ ', 'test*.py')
    unittest.TextTestRunner().run(discover)

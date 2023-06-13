import pytest


class Test_py_003():
    def test_sum(self):
        a=9
        b=9
        sum=a+b
        print("sum---->"+str(sum))
        if sum==18:
            assert True
        else:
            assert False
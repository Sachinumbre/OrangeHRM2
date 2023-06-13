import pytest

from selenium.webdriver.chrome import webdriver
from selenium import webdriver


# driver=webdriver.Chrome()

class Test_py:
    def test_sum_001(self):
        a = 10
        b = 20
        sum = a + b
        print("str-->" + str(sum))
        if sum == 30:
            assert True
        else:
            assert False

    def test_mul_002(self):
        a = 30
        b = 20
        mul = a * b
        print("Mul---->" + str(mul))
        if mul == 600:
            assert True
        else:
            assert False

    def test_sub_003(self):
        c = 100
        d = 20
        sub = c - d
        print("sub--->" + str(sub))
        if sub == 80:
            assert True
        else:
            assert False

    def test_credenceUrl_004(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        print(driver.title)
        if driver.title == "Credence":
            print("Your are at credence site")
            assert True
        else:
            print("Your are at wrong site")
            assert False

    def test_goole_005(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

        # driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        print(driver.title)
        if driver.title == "Google":
            print("You are in google site")
        else:
            print("You are in Wrong site")
    #










    def test_credence_006(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://credence.in/")
        print(driver.title)
        if driver.title == "Credence":
            print("You are in Credence site")
            assert True
        else:
            print("You are in wrong site")
            assert False


    def test_add_007(self):
        e=200
        f=400
        add = e+f
        print("add---->"+str(add))
        if add == 600:
            print("the test case is pass")
            assert True
        else:
            print("test case is fail")
            assert False



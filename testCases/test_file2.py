import time
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Test_py_002():
    def test_sum_008(self):
        R = 20
        j = 40
        sum = R + j
        print("sum--->"+str(sum))
        if sum==60:
            assert True
        else:
            assert False

    def test_credence_009(self):
        from selenium import webdriver
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver=webdriver.Chrome(options=chrome_options)
        # driver=webdriver.Chrome()
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()

        l = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p/a"))
        time.sleep(2)
        list =[]

        for r in range(1,l+1):
            Mobile_number=driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p/a ["+str(r)+"]").text
            list.append(Mobile_number)
        print(list)

        if "+91 7385318590" in list:
            print("Mobile number is present in a list")
            print(list.index("+91 8237916162"))
            assert True

        else:
            print("mobile number is not present")
            assert False

        driver.quit()



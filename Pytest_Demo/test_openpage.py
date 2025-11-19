
def test_openpage(driver,base_url):
    print("Inside test open page")
    driver.get(base_url)
    print(driver.title)
    #assert "Face" in driver.title
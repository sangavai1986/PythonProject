
def test_openpage(driver,base_url):
    print(base_url)
    driver.get(base_url)
    print(driver.title)
    #assert "Face" in driver.title
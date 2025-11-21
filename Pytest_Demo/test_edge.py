import os

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService, Service


def test_edge_browser():
    #service = EdgeService(EdgeChromiumDriverManager(version="142.0.3595.99").install())
    #driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    service = Service(r"C:\Users\eksri\PycharmProjects\pythonProject\Pytest_Demo\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    #driver = webdriver.Edge()

    '''
    driver = webdriver.Edge()
    options = Options()
    options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver_path = os.path.join(os.path.dirname(__file__), "msedgedriver.exe")
    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service,options=options)
    '''
    driver.get("https://saucedemo.com")

test_edge_browser()
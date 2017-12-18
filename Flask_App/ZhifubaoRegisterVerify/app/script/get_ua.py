from selenium import webdriver


# driver = webdriver.PhantomJS(executable_path=r'E:\Program Files\Phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get(r"C:\Users\YongHu\Desktop\TMP\tt.html")

print(driver.page_source)
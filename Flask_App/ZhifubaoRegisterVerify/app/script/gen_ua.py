from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

content = open('gen_ua.html', 'r', encoding='utf-8').read()
script = "document.write(\'\'\'%s\'\'\')" % content
print(script)


driver.execute_script(script)
print(driver.page_source)
driver.close()
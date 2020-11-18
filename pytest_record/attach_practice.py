import allure
#添加一个文本
def test_attach_txt():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)
#添加一个html代码块
def test_attach_html():
    allure.attach("<body>这是一个htmlbody块</body>","html代码块",attachment_type=allure.attachment_type.HTML)
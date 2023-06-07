# pip install zenrows
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient

client = ZenRowsClient("4b0ff4bdf6c636643e34485c15890af74e1fe2cf")
url = "https://admin-demo.nopcommerce.com"
params = {"antibot": "true", "device": "mobile"}

response = client.get(url, params=params)
soup = BeautifulSoup(response.text, "html.parser")
form = soup.findAll('form')
print(form)
# with open("./data/home.html", 'a') as file:
#     for line in response.text:
#         file.write(line)

# print(response.text)
# import time
#
# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     context = p.chromium.launch_persistent_context(
#         user_data_dir="",
#         headless=False,
#         executable_path="C:\\TOOLS\\chrome-win\\chrome.exe")
#     page = context.new_page()
#     page.goto("https://admin-demo.nopcommerce.com/")
#     time.sleep(10)
#     print(page.url)

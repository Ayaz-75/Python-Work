from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import smtplib

my_email = "hisherhim2022@gmail.com"
my_pass = "fqhbljpavieykgoz"

chrome_driver_path = "C:\Development\chromedriver.exe"
item_link = "https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=pd_rhf_ee_s_pd_crcd_sccl_1_1/143-2082044-3248110?pd_rd_w=Uta6R&content-id=amzn1.sym.cee83ff1-8fc1-4533-a3f5-bf3d998f4558&pf_rd_p=cee83ff1-8fc1-4533-a3f5-bf3d998f4558&pf_rd_r=A3H3HR98B4AAKJNXXFQ5&pd_rd_wg=7ewac&pd_rd_r=07b06b59-756c-4bec-b24d-c9e06db99627&pd_rd_i=1491957662&psc=1"


s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
driver.get(item_link)

price_tag = driver.find_element(by=By.ID, value="newBuyBoxPrice")
price_string = price_tag.text.replace("$", "")
price_int = float(price_string)


# print(type(price_tag))
# print(price_tag)

print(price_int)
if price_int < 35:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs="lakho75@yahoo.com",
                            msg="Price has become in your budget go buy that item on Amazon")


driver.close()

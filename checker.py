import time
import requests
import smtplib

from bs4 import BeautifulSoup


URL = "https://www.amazon.com/dp/1936781921/?coliid=I3PC4YITMMDPR3&colid=1G3LTO0VGID97&psc=1&ref_=lv_ov_lig_dp_it"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.72'}

def checkprice():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(class_='a-size-medium a-color-price offer-price a-text-normal').get_text()
    converted_price = float(price[1:])
    if converted_price < 20:
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alex.sgrpg@gmail.com', 'mypassword')
    subject = 'Price fell down!'
    body = 'Product link ' + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('alex.sgrpg@gmail.com','lex_signori@hotmail.com', msg)
    print('Email has been sent')
    server.quit()


while True:
    checkprice()
    time.sleep(86400)
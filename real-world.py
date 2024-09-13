from bs4 import BeautifulSoup
import requests
import sys

bitget_coin_price_url = requests.get(
    "https://www.bitget.com/price").text
okx_coin_price_url = requests.get(
    "https://www.okx.com/markets/prices"
).text


class OkxClass:
    def __init__(self, title="", abb="", price=0.0):
        self.title = title,
        self.abb = abb,
        self.price = price


try:
    bitget_soup = BeautifulSoup(bitget_coin_price_url, 'lxml')
    okx_soup = BeautifulSoup(okx_coin_price_url, 'lxml')
except Exception:
    e = sys.exc_info()[1]
    print(e.args[0])


# ? ---- for Biget wallet -------
index = 0
coin_title_index = 0

bitget_title_html_tag = "a"
bitget_abb_html_tag = "span"
bitget_price_html_tag = "span"

bitget_title_class_name = "text-fs18 text-primaryText break -words pointer-events-none"
bitget_abb_class_name = "text-fs12 text-thirdText"
bitget_price_class_name = "text-fs16 text-primaryText"


coin_title_list_biget = bitget_soup.findAll(
    bitget_title_html_tag, class_=bitget_title_class_name)

coin_abb_list_biget = bitget_soup.findAll(
    bitget_abb_html_tag,
    class_=bitget_abb_class_name
)

price_list_biget = bitget_soup.findAll(
    bitget_price_html_tag, class_=bitget_price_class_name)

for price in price_list_biget:
    if (index % 5 == 0):
        # print(coin_abb_list_biget[coin_title_index].text + " - " + price.text)
        coin_title_index = coin_title_index+1

    index = index + 1


# ? ---- for Okx wallet -------
okx_result = []
okx_index = 0

okx_title_html_tag = "span"
okx_abb_html_tag = "span"
okx_price_html_tag = "td"

okx_title_class_name = "full-name"
okx_abb_class_name = "short-name"
okx_price_class_name = "last-price"

okx_price_list = okx_soup.findAll(okx_price_html_tag, okx_price_class_name)
okx_abb_list = okx_soup.findAll(okx_abb_html_tag, okx_abb_class_name)
okx_title_list = okx_soup.findAll(okx_title_html_tag, okx_title_class_name)


def create_okx_instances(okx_price_list, okx_abb_list, okx_title_list):
    okx_result = []

    for okx_price in (okx_price_list):
        okx_instance = OkxClass(price=okx_price.text)
        okx_result.append(okx_instance)

    if (len(okx_abb_list) > 0):
        for i, okx_abb in enumerate(okx_abb_list):
            okx_result[i].abb = okx_abb.text

    if (len(okx_title_list) > 0):
        for i, okx_title in enumerate(okx_title_list):
            okx_result[i].title = okx_title.text

    return okx_result


def print_okx_instance(okx_result):
    for instance in okx_result:
        print(instance.title)
        print(instance.price)
        print(instance.abb)


okx_list = create_okx_instances(okx_price_list, okx_abb_list, okx_title_list)

print_okx_instance(okx_list)

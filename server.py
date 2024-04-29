import requests
import json
import time
import os
from dotenv import load_dotenv
import grpc
import grpc_pb2_grpc
import grpc_pb2
from concurrent import futures

class Item:
    def __init__(self, name, characteristics, link, images, rating, price):
        self.name = name
        self.characteristics = characteristics
        self.link = link
        self.images = images        
        self.rating = rating
        self.price = price

class Characteristic:
    def __init__(self, name, value):
        self.name = name
        self.value = value


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print("env is not initialized")

class ProductServiceServicer(grpc_pb2_grpc.ProductServiceServicer):
    def Product(self, request, context):

        product_ids = get_products_ids()
        products = get_products_data(product_ids)
        prods = []
        for i in products:
            prod = grpc_pb2.ItemProduct()
            prod.link = i.link
            prod.name = i.name
            for characteristic in i.characteristics:
                p = grpc_pb2.Characteristics(
                    name=characteristic.name,
                    value=characteristic.value
                )
                prod.characteristics.append(p)
            for image in i.images:
                prod.images.append(image)
            prod.rating = i.rating
            prod.price = int(i.price)
            prods.append(prod)

        return grpc_pb2.ClientResponse(prod=prods)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_ProductServiceServicer_to_server(ProductServiceServicer(), server)

    insecure_port = str(os.environ.get("INSECURE_PORT"))

    port = f"[::]:{insecure_port}"
    server.add_insecure_port(port)
    server.start()
    print("server is started")
    server.wait_for_termination()

cookies = {
    'MVID_CITY_ID': 'CityCZ_975',
    'MVID_REGION_ID': '1',
    'MVID_REGION_SHOP': 'S002',
    'MVID_TIMEZONE_OFFSET': '3',
    'bIPs': '1949759381',
    'JSESSIONID': 'j4G6mn6JHQ650yl9qNL0JDhnfGSJQ9WlyhXhBH2GLwwgfZ6kJ6vd!58526892',
    'MVID_GUEST_ID': '23746744586'
}

login = str(os.environ.get("PROXY_LOGIN"))
password = str(os.environ.get("PROXY_PASSWORD"))
addr = str(os.environ.get("PROXY_ADDR"))

proxies = {
    'http': f'socks5://{login}:{password}@{addr}',
    'https': f'socks5://{login}:{password}@{addr}',
    'no_proxy': 'localhost,172.0.0.1'
}

def main():
    product_ids = get_products_ids()
    get_products_data(product_ids)

ids_categories = [
    "205",
    "118",
    "101",
    "4107",
    "65"
]

def get_products_ids():
    amount = 24
    products_ids = []

    for id_category in ids_categories:
        step = 0
        while True:
            # заглушка
            # if step == 3:
            #     break

            offset = step*amount

            response = requests.get(f"https://www.mvideo.ru/bff/products/listing?categoryId={id_category}&offset={offset}&limit=24", cookies=cookies, proxies=proxies)
            json_data = json.loads(response.text)
            # print(response.text)

            if json_data["body"]["products"] != []: 
                products_ids += json_data["body"]["products"]
                step += 1

                time.sleep(2)
            else: break
    
    return products_ids
        
def divide_chunks(list, n): 
    for i in range(0, len(list), n):  
        yield list[i:i + n] 

def get_products_data(products_ids):
    headers = {
        'cookie': 'MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ACCESSORIES_PDP_BY_RANK=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CHAT_VERSION=6.6.0; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_DISPLAY_ACCRUED_BR=true; MVID_DISPLAY_PERS_DISCOUNT=true; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_NEW_CHAT_PDP=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_PODELI_PDP=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICE_AVLB=true; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; mindboxDeviceUUID=b8b1dd90-b23c-472a-9f33-b5e44c9a34d2; directCrm-session=%7B%22deviceGuid%22%3A%22b8b1dd90-b23c-472a-9f33-b5e44c9a34d2%22%7D; _ym_uid=1713373650747649541; _ym_d=1713373650; _ga=GA1.1.96952222.1713373651; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=6255af39-0178-42f4-a142-0204472c28c2; tmr_lvid=0634bcaad7fc0264f076708beabe61af; tmr_lvidTS=1713373653647; uxs_uid=fb842450-fcdc-11ee-831b-35e5e458bff8; flocktory-uuid=eb42992d-9a55-4db3-b3bd-8f5626f0bba8-9; afUserId=7e7bc3cf-bcd4-4695-b638-5bca302b0df3-p; MVID_GEOLOCATION_NEEDED=false; adid=171377373307705; MVID_GUEST_ID=23746744586; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=1; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; __lhash_=b1d2b6c9b73983db3253d1bde6f15954; MVID_FAVORIT_NEW=true; customer_email=null; AF_SYNC=1714043191009; __hash_=3fdadf9488b77945c77232548fb03308; MVID_CART_MDENGY=1; MVID_DIGINETICA_ENABLED=true; MVID_ENVCLOUD=prod2; _userGUID=0:lvjhcjit:mvLci23OMOx1LaIBb3G6aLg0w5gI_Dxi; _sp_ses.d61c=*; _ym_isad=2; dSesn=144b8332-1ff2-ce43-55d2-5117bf7d8725; _dvs=0:lvjhcjit:agnV1hi6dOsrw0INGlImJXLefQ0gSq_Q; _ym_visorc=w; SMSError=; authError=; advcake_track_id=cc8986b4-6708-2bcd-9d99-2f93b8936ad4; advcake_session_id=ed177e5f-fe0d-7777-e499-b1c24b87a01c; domain_sid=GCg4AAEc1tcqSLSZxoLk-%3A1714305698159; JSESSIONID=j4G6mn6JHQ650yl9qNL0JDhnfGSJQ9WlyhXhBH2GLwwgfZ6kJ6vd!58526892; flacktory=no; BIGipServeratg-ps-prod_tcp80=2416237578.20480.0000; bIPs=1949759381; CACHE_INDICATOR=true; MVID_GTM_BROWSER_THEME=1; adrdel=1; adrcid=A6ZlKqPGbNu8WR7aHS_ndfw; advcake_track_url=%3D202404222Gv5eTpKP6gOnLPOIPEbWh32VCvEJ2oYZBP6IQoPYqxCjuRxLg8Ut5P%2FTyZu%2FK5w7Ch6uQs24y6oBvFdqg9sLeasJIvRCynwlHrZNZ2RmwdydDhZ%2FZIuBBxV3IYw%2B4abfFIJU5Uy%2Bo%2BdmUoA7LJXaXiUC16KVUpIH4rPavnLINw27AfDkDAzegDbmBWjbX3r8m6B69KxyYe5l7eDoOEoVL0%2FxHFQfLsdkuE%2B46ZWh2dXlZICkykmLnnb7zINPv3uzH5OKAvwNSXkCanuGHlcKSet2EV9Fplae3QKCf476wYw6ZsAFbT%2F9elxQFdexGkFF3V5bKZRoqKvYDwPlR6FcsarCaP%2FTBtTqfv%2Btq9Gepp3D1WV6sNkvgjHqrfw7RCnvLRepmHJ4IGFuhOTy7eBSD2%2BXbr0BjPrt5ZNNaBePyD%2Fk3qFeKWqhQwzaAt4D7J9wsqlToRKVbMYkxH53a1oLBMPfEWPZg3kmtg%2Fl4pQnXVZkUfjiGi7j48xcfvjwbTUy8sp5avO8MJFkv7NJp%2FyZqvAqc%2BGWLD522%2FFhPHrMMFOILXie6urGKcayqWLidoV0842rlHXMnyyzEofmGptEuwq2DyXmJCmS1JZKN6tca%2FsABu%2Fr6k7qBFF2cqjd9ji10FflJbrp50UrTNSzlNhD4OdHpRirJiNQzyVtFMhXJAWBZxQibgDstQ%3D; tmr_detect=0%7C1714305775478; gsscgib-w-mvideo=liFVdETfxbfAufgAuR7eB8wfr0z1kwy2y9E2bbdqs6P94INym/CX6231ygKqCFva4DYBQ7U3Btm2a2bV7O3A0gaIUxilhcO4bsPlGLTcvEi3ssHO1C3kIcoGmiS6kEJj4hxxDuE8NR2B7ew6YMQz/zgjQTW4GU3CL0iwRI0h3y3rt2Y8PJplsPmSY0YV7qDol/pwyzoquHPmfFVARSI2SW59bbRXrobXV4hO1DhHvZFtDIfaEUsRBJdAr5hIlMcW6Q==; gsscgib-w-mvideo=liFVdETfxbfAufgAuR7eB8wfr0z1kwy2y9E2bbdqs6P94INym/CX6231ygKqCFva4DYBQ7U3Btm2a2bV7O3A0gaIUxilhcO4bsPlGLTcvEi3ssHO1C3kIcoGmiS6kEJj4hxxDuE8NR2B7ew6YMQz/zgjQTW4GU3CL0iwRI0h3y3rt2Y8PJplsPmSY0YV7qDol/pwyzoquHPmfFVARSI2SW59bbRXrobXV4hO1DhHvZFtDIfaEUsRBJdAr5hIlMcW6Q==; _sp_id.d61c=94b72935-5a5d-4c12-a65d-cddfb4fd83a5.1713373650.7.1714307405.1714047721.fad7636c-1f70-47c6-be44-86b4591e2b8a.fae5fca2-b22c-4577-b7e5-2692069299de.48266f70-7152-41dd-a93e-315b6196552d.1714305694568.134; fgsscgib-w-mvideo=rxf4523c3f9967bc431c065cd9b1c5e52c9fdd8a; fgsscgib-w-mvideo=rxf4523c3f9967bc431c065cd9b1c5e52c9fdd8a; gsscgib-w-mvideo=kM/eWult9Qp9QEhpViWEYt8vWIINYTtBS5134xL3teevC730Wfp4pxBkX9LNeAmoQCL2nvSknXOX1bErUtezApuyqn5sFHakC3B0R25LsQfhJOpUuhwMLqyin1LPOWx9e5OfZSpuSKlaojSPAHKPLTKjrwsrJZpzvgkYquqDs8Tsd4UcYhmAMtPgevLC2RaVVxkDzHN1/o3mhXuKFXJxLJnSLgb/JO7znnEUOwOB4mrybo3Uurfbo0wIzmaUf9ALhA==; cfidsgib-w-mvideo=LcJx3FVubbbY5i/Z0GjDVyxUymQiCn4TnpYTu4qLPHyAtzOauBHqJrI3dZOkem6koIa5N+sZxY1YWnZpXQDtxA5+EsanNzXnplFoJ0HZ1wWY/dODlSRnsBGazpA41b5TsLG3CXoGQU4ggBBtbpuIFqTytcTVCuF6aNNfo8I=; _ga_CFMZTSS5FM=GS1.1.1714305694.8.1.1714307407.0.0.0; _ga_BNX5WPP3YK=GS1.1.1714305694.8.1.1714307407.60.0.0',
        'authority': "www.mvideo.ru",
        'accept': "application/json",
        'accept-language': "ru,en;q=0.9,zh;q=0.8,ko;q=0.7",
        'content-type': "application/json",
        'origin': "https://www.mvideo.ru",
        'referer': "https://www.mvideo.ru/",
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "YaBrowser";v="24.4", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36"
        }

    lists = list(divide_chunks(products_ids, 24)) 
    items = []

    for _list in lists:
        payload = {
            'productIds': _list,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }
       

        # получение данных о ценах на товары

        ids_string = ""
        for id in _list:
            ids_string += f"{id},"

        response = requests.get(f"https://www.mvideo.ru/bff/products/prices?productIds={ids_string}", cookies=cookies, proxies=proxies)
        price_data = json.loads(response.text)

        # получение данных о товарах

        response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=payload, proxies=proxies)
        json_data = json.loads(response.text)
        
        for product in json_data["body"]["products"]:
            characteristics = []

            for property in product["propertiesPortion"]:
                characteristic = Characteristic(
                    name=property["name"],
                    value=property["value"]
                )
                characteristics.append(characteristic)

            images = []
            for image in product["images"]:
                image = f"https://img.mvideo.ru/{image}"
                images.append(image)

            price = 0
            for el in price_data["body"]["materialPrices"]:
                if el["productId"] == product["productId"]:
                    price = el["price"]["salePrice"]
 
            rating = ""
            if str(product["rating"]["star"]) == "None":
                rating = "Отсутствует"
            else:
                rating = str(round(product["rating"]["star"], 1))

            item = Item(
                name=product["name"],
                link=f"https://www.mvideo.ru/products/{product["nameTranslit"]}-{product["productId"]}",
                rating=rating,
                characteristics=characteristics,
                images=images,
                price=price
            )
            
    # for item in items:
    #     print("--------------------")
    #     print(item.name)
    #     print(item.link)
    #     for i in item.characteristics:
    #         print(i.name)
    #         print(i.value)
    #     for image in item.images:
    #         print(image)
    #     print(item.rating)
    #     print(item.price)
    return items
        
serve()
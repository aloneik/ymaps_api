import requests
from lxml import etree


URL = 'https://geocode-maps.yandex.ru/1.x/'
nsmap = {
    "ymps": "http://maps.yandex.ru/ymaps/1.x",
    "gml": "http://www.opengis.net/gml",
    "geo": "http://maps.yandex.ru/geocoder/1.x"
}

latitude = input("Input latitude: ")
longitude = input("Input longtitude: ")

payload = {
    "geocode": latitude + "," + longitude,
    "lang": "en_RU"
}
response = requests.get(URL, params=payload)
if response.status_code == 200:
    document = etree.fromstring(response.text.encode("utf-8"))
    print(document.xpath(
        "//ymps:GeoObjectCollection/gml:featureMember[1]/ymps:GeoObject/"
        "gml: metaDataProperty/geo: GeocoderMetaData/geo: text/text()",
        namespaces=nsmap
    )[0])

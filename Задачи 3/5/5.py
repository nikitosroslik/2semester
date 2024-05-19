import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
dic={}
for product in root.findall('product'):
    price = product.find('price').text
    name = product.get('name')
    dic[name]=price
while True:
    print("выбери категорию")
    print("1) сортировка по цене")
    print("2) корзина")
    print("3) выход")
    prod=input()
    if prod=='1' or prod=="сортировка по цене":
        sorted_product = sorted(dic.items(), key=lambda item: item[1])
        for i in sorted_product:
            print(i[0],i[1])
    elif prod == '2' or prod == "корзина":
        summ = 0
        while True:
            print("выбери товар")
            prodi=input()
            try:
                summ+=int(dic[prodi])
            except:
                print("нет такого товара")
            print("хватит?")
            a=input()
            if a=="да":
                print(summ)
                break
    elif prod == '3' or prod == "выход":
        break

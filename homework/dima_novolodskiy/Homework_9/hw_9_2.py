PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
list_price = PRICE_LIST.split()
dict_price_list = {list_price[x]: int(list_price[x + 1].rstrip('р')) for x in range(len(list_price)) if x % 2 == 0}
print(dict_price_list)

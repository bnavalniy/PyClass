# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
input_amount = int(input("Which amount?"))
list_of_goods = []
count_id = 1
while input_amount != 0:
    n = input("название:")
    pr = float(input("цена:"))
    q = int(input("количество:"))
    e = input("eд:")
    buffer_dict = dict(name=n, price=pr, quantity=q, ed=e)
    buffer_tuple = tuple((count_id, buffer_dict))
    list_of_goods.append(buffer_tuple)
    input_amount -= 1
    count_id += 1
print(list_of_goods)
# Analytics
names = []
prices = []
quantities = []
eds = []
for el in list_of_goods:
    names.append(el[1].get("name"))
    prices.append(el[1].get("price"))
    quantities.append(el[1].get("quantity"))
    eds.append(el[1].get("ed"))
analytic_dict = dict(names=names, prices=prices, quantities=quantities, ed=eds)
print(analytic_dict, end='')

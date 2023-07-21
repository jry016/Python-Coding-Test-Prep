# KATTIS
# Bacon, Eggs, and Spam
# https://open.kattis.com/problems/baconeggsandspam

while True:
    n = int(input())
    if n == 0: 
        break
    orders = []
    for i in range(n):
        item = [order for order in input().split()]
        orders.append(item)
    #print(orders)
    
    menus = {}
    for menu in orders:
        person = menu[0]
        menu = menu[1:]
        for i in range(len(menu)):
            if menu[i] not in menus:
                menus[menu[i]] = []
            menus[menu[i]].append(person)
    
    # Sort Dictionary by keys and then by values which is a list
    sorted_menu = {key: sorted(value) for key, value in sorted(menus.items())}
    
    for food, person in sorted_menu.items():
        print(f"{food} {' '.join(person)}")
        
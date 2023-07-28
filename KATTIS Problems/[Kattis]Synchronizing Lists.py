# KATTIS
# Synchronizing Lists
# https://open.kattis.com/problems/synchronizinglists

synced_lsts = []
while True:
    n = int(input())
    if n == 0:
        break
    lst = []
    for i in range(n*2):
        user_input = int(input())
        lst.append(user_input)
        
    # Split the Lists
    syn_lst1, syn_lst2 = lst[:n], lst[n:]

    order_dict = {syn_lst1[i]: i for i in range(0, n)}
    
    syn_lst1.sort()
    syn_lst2.sort()
    
    # 0:0, 1:2, 2:3, 3:1
    # need index of the sorted list
    order = []
    sort_dict = {syn_lst1[i]: i for i in range(0, n)}
    
    for key in order_dict.keys():
        order.append(sort_dict[key])
    
    for i in range(n):
        synced_lsts.append(syn_lst2[order[i]])
    
    synced_lsts.append('\n')
        
for lst in synced_lsts:
    print(lst)
        
    
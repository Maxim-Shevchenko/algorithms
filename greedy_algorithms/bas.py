list_all_orders =[ (150,1000),(400,2000),(350,1500),(150,300), (200, 500) ]
sorted_list_all_orders = sorted(list_all_orders ,reverse = True)
print(sorted_list_all_orders)
carrying = 4000
list_out= list()
i = 0
while carrying >= sorted_list_all_orders[i][1]:
  
    list_out.append(sorted_list_all_orders[i])    
    carrying -=sorted_list_all_orders[i][1]
    i+=1
total_value = 0
total_weight = 0
counter_box=0 
for value,weight in list_out:
    counter_box+=1
    total_value += value
    total_weight += weight
  
      
print(f" Взяли коробок {counter_box}, общая стоимость {total_value}, общий вес {total_weight}, еще можно взять {carrying } кг")

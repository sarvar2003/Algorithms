# Fractional Knapsack problem
import math
from typing import List

class Item:
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value
        self.ratio = value / weight
    
def knapsack(items: List[Item], capacity: int) -> int:
    items.sort(key=lambda x:x.ratio, reverse=True)

    currCapacity = capacity
    totalValue = 0

    for i in items:
        if currCapacity == 0:
            break

        if i.weight <= currCapacity:
            currCapacity -= i.weight
            totalValue += i.value
        else:
            totalValue += currCapacity * i.ratio
            currCapacity = 0
        
    return totalValue

item1 = Item(20, 150)
item2 = Item(30, 200)
item3 = Item(10, 120)

items = [item1, item2, item3]

print(knapsack(items, 50))

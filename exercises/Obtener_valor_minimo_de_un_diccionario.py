prices = {
   'A': 89.77,
   'B': 12.65,
   'C': 85.55,
   'D': 7.25,
   'F': 198.75
}

def min_dic(dic):
    return min(dic, key=lambda key: dic[key])

print(min_dic(prices))

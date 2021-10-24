car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

list1 = [1,2,3,1,2,3,4,5]

list1= list(dict.fromkeys(list1))
print(list1)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


for key,value in car.items():
    print(key,value)
# Boolean expressions
print(5 > 1)
print(12 == 4)
print(7 < 3)

x = 320
y = 150
if y > x:
  print("y is greater than x")
else:
  print("y is not greater than x")

# Boolean values
print(bool("Hello"))
print(bool(21))

a = "Hello"
b = 42

print(bool(a))
print(bool(b))

bool("uvw")
bool(234)
bool(["carrot", "beet", "cucumber"])


class CustomClass():
  def __len__(self):
    return 0

custom_obj = CustomClass()
print(bool(custom_obj))

def sampleFunction():
  return False

if sampleFunction():
  print("ACCURATE!")
else:
  print("INCORRECT!")

z = 910
print(isinstance(z, str))

# Operators
print(4 + 3)
print(21 + 5 * 6)
print(10 + 6 - 3 + 8)

# Lists
vehicles = ["toyota", "ford", "mazda"]
print(vehicles)

list1 = ["banana", "peach", "pear"]
list2 = [6, 3, 1, 4, 9]
list3 = [True, True, False]

# Tuples
tupleA = ("rose", "tulip", "daisy")
print(tupleA)

k = ("cherry", "blueberry", "pomegranate")
m = list(k)
m[1] = "raspberry"
k = tuple(m)

print(k)

tupleM = ("u", "v", "w")
tupleN = (4, 5, 6)

tupleP = tupleM + tupleN
print(tupleP)

# Sets
fruitCollection = {"peach", "pear", "orange"}
print(fruitCollection)

setA = {"grapefruit", "watermelon", "avocado"}
setB = {2, 5, 9, 11, 14}
setC = {True, True, False}

fruitCollection = {"cherry", "pineapple", "apricot"}

for item in fruitCollection:
  print(item)

# Dictionaries
devices = {
  "brand": "Apple",
  "model": "MacBook Air",
  "year": 2023
}

gadget = {
"brand": "Samsung",
"model": "Galaxy S21",
"year": 2022
}
k = gadget.keys()

print(k) # before modification

gadget["color"] = "green"
print(k) # after modification

# If ... Else 
M = 200
N = 450
if N > M:
  print("N is greater than M")

M = 88
N = 88
if N > M:
  print("N is greater than M")
elif M == N:
  print("M and N are equal")

# While Loops
j = 3
while j < 8:
  print(j)
  j += 1

j = 4
while j < 9:
  print(j)
  if j == 6:
    break
  j += 1

j = 2
while j < 7:
  j += 1
  if j == 5:
    continue
  print(j)
  
# For Loops

device_types = ["monitor", "keyboard", "mouse"]
for x in device_types:
  print(x)

for x in range(2, 30, 3):
  print(x)

meals = ["sandwich", "pizza", "tacos"]
for x in meals:
  print(x)
  if x == "pizza":
    break

for x in range(6):
  print(x)
else:
  print("Task completed!")

shapes = ["circle", "triangle", "square"]
materials = ["wood", "metal", "plastic"]

for x in shapes:
  for y in materials:
    print(x, y)
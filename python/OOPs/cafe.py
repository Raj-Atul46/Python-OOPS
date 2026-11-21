# class Coffee:
#     colour = "Brown"
    
#     def __init__(self, name, roast, grind, top_layer, shot):
#         self.name = name
#         self.roast = roast
#         self.grind = grind
#         self.top_layer = top_layer
#         self.shot = shot

#     def order(self):
#         print(f"You ordered the {self.name}")
#     def check_description(self):
#         print(f"Your drink is {self.name} which is {self.roast} roast, grinded {self.grind} having {self.top_layer} as top layer with a {self.shot} shot of espresso.")


l1 = [2, 4, 3]
l2 = [5, 6, 4]
l3 = []
num1 = 0
num2 = 0
for n1 in l1:
    num1 = num1*10 + n1
print(num1)

for n2 in l2:
    num2 = num2*10 + n2
print(num2)

sum = num1 + num2
print(sum)

result1 = [int(x) for x in str(sum)[::-1]]

print(result1)


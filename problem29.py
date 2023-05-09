import random
for i in range(10, 150):
    random.randint = i 
    if i % 5 == 0 and i % 7 == 0:
        print(i)

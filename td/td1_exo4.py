def index(a, li):
    for i in range(len(li)):
        if a == li[i]:
            return i
        

li = [2, 8, 4]
print(index(8, li))





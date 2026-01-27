numbers = [10,25,20,30,45,50]
target = 30
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print("element found at index: ",i)
        found=True
        break
    else:
        print("Element not found!!!")
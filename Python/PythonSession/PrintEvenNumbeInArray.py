# myFirstList =[4,5,True,78,"Abhi",{4,5,6,7,8},78]

# for i in range(len(myFirstList)):
#     if i % 2 == 0:
#         print(myFirstList[i])22

def evenNumber(inputValue):
    numList = inputValue.split()
    newNumList =[]
    for i in range(len(numList)):
        num = int(numList[i])
        if num % 2 == 0:
            newNumList.append(num)
    
    return newNumList

inputValue = input("Enter The Values")



print(evenNumber(inputValue))
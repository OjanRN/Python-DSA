#Bubble sort algorithm by OjanRN
#Github: github.com/ojanrn

import time

def mainApp():
    start = time.time()
    inputList = [85,32,42,12,95,20,40]
    order = 0
    while True:
        if order+1 == len(inputList):
            order = 0
        if inputList[order] > inputList[order + 1]:
            inputList[order + 1], inputList[order] = inputList[order], inputList[order + 1]
        order+= 1
        print(inputList)
        if inputList == sorted(inputList):
            end = time.time()
            break

mainApp()
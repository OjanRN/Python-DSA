#Bubble sort algorithm by OjanRN
#Github: github.com/ojanrn

def mainapp():
    inputlist = [85,32,42,12,95,20,40]
    order = 0
    while True:
        if order+1 == len(inputlist):
            order = 0
        if inputlist[order] > inputlist[order + 1]:
            inputlist[order + 1], inputlist[order] = inputlist[order], inputlist[order + 1]
            print(inputlist[order], inputlist[order + 1])
        order+= 1
        print(inputlist)
        if inputlist == sorted(inputlist):
            break
mainapp()

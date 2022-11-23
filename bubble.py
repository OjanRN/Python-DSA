#Bubble sort algorithm by OjanRN
#Github: github.com/ojanrn

def mainapp():
    inputlist = [3,5,2,23,15,63,100]
    order = 0
    print(inputlist)
    while True:
        if order+1 == len(inputlist):
            order = 0
        if inputlist[order] > inputlist[order + 1]:
            inputlist[order + 1], inputlist[order] = inputlist[order], inputlist[order + 1]
        order+= 1
        if inputlist == sorted(inputlist):
            print(inputlist)
            break
mainapp()

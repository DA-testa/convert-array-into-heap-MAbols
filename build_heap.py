# python3
from math import floor
import numpy as np

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    array=np.array(data)
    
    for i in range(len(array)):
        i=len(array)-1-i
        while True:

            if array[i]<array[floor(i/2)]:
                temp=array[floor(i/2)]
                array[floor(i/2)]=array[i]
                array[i]=temp
                swaps.append([floor(i/2)-1,i-1])
                i=floor(i/2)
                continue
            else:
                break

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text=input()

    # input from keyboard
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

        # checks if lenght of data is the same as the said lenght
        assert len(data) == n

        # calls function to assess the data 
        # and give back all swaps
        data.insert(0,0)
        swaps = build_heap(data)
    elif "F" in text:
        faila_nosaukums=input()
        if "a" in faila_nosaukums:
            print("error")
            
        else:
            
            fails=open("./test/"+faila_nosaukums)
            n=fails.readline()
            n=int(n)
            data=list(map(int,fails.readline().split()))
            assert len(data) == n

            # calls function to assess the data 
            # and give back all swaps
            swaps = build_heap(data)


    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

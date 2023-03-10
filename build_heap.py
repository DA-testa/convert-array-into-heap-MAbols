# python3
from math import floor
#import numpy as np

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
   # data=np.array(data)
    #i=1
    # for i in range(1,len(data)+1):
    #     i=len(data)-i
    #     while True:
    #         p=floor(i/2)
    #         if data[i]<data[p]:
    #             temp=data[p]
    #             data[p]=data[i]
    #             data[i]=temp
    #             swaps.append([p-1,i-1])
    #             i=p
    #         else:
    #             #f=abs((floor(i/2))-1)
    #             break
    # i=1
    # for i in range(len(data)):
    #     i=len(data)-1-i
    #     while True:
    #         p=floor(i/2)
    #         if array[i]<array[p]:
    #             temp=array[p]
    #             array[p]=array[i]
    #             array[i]=temp
    #             swaps.append([p-1,i-1])
    #             i=p
    #         else:
    #             #f=abs((floor(i/2))-1)
    #             break
    i=1
    check=True
    
    while check:
        i=len(data)-i
        lc=i*2
        rc=(i*2)+1
        if (2*i)+1<=len(data)-1:
            for i in range(1,len(data)):
                if data[rc]<data[i] or data[lc]<data[i]:
                    for i in range(1,len(data)):
                        i=len(data)-i
                        lc=i*2
                        rc=(i*2)+1
                        if (2*i)+1<=len(data)-1:
                            if data[rc]<data[i] or data[lc]<data[i]:
                                if data[rc]<data[lc]:
                                    temp=data[i]
                                    data[i]=data[rc]
                                    data[rc]=temp
                                    swaps.append([i-1,rc-1])
                                    i=floor(i/2)
                                else:
                                    temp=data[i]
                                    data[i]=data[lc]
                                    data[lc]=temp
                                    swaps.append([i-1,lc-1])
                                    i=floor(i/2)
                            else:
                                break
                                #continue
                        else:
                            continue
                else:
                     check=False
                    # i=len(data)-1
                    #break
        elif (2*i)+2<=len(data)-1:
            
            if data[lc]<data[i] or data[rc]<data[i]:
                for i in range(len(data)):
                    i=len(data)-i
                    lc=i*2
                    rc=(i*2)+1
                    if data[lc]<data[rc]:
                        temp=data[i]
                        data[i]=data[lc]
                        data[lc]=temp
                        swaps.append(i-1,lc-1)
                        i=floor(i/2)
                    else:
                        temp=data[i]
                        data[i]=data[rc]
                        data[rc]=temp
                        swaps.append([i-1,rc-1])
                        i=floor(i/2)
            else:
                check=False
                continue
           
        else:
            i-=1
            
               
        
                    
    
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
            
            fails=open("./tests/"+faila_nosaukums)
            n=fails.readline()
            n=int(n)
            data=list(map(int,fails.readline().split()))
            assert len(data) == n

            # calls function to assess the data 
            # and give back all swaps
            data.insert(0,0)
            swaps = build_heap(data)


    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    print(len(swaps))

if __name__ == "__main__":
    main()

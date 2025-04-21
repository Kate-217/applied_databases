def main():
    #empty array:
    empty_array = []
    
    #array:
    array = [1,3,2,5,6]

    for num in array:
        new_num = double(num)
        empty_array.append(new_num)
    
    print("This is doubled array:",empty_array)
    

def double(n):
    doubled_num = 2 * n
    return doubled_num
          
    





if __name__=="__main__":
    main()
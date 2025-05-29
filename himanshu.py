# a = ["Himanshu", 15, 9, 19]  
# print(a[0])  
# a[0]="Himani"
# print(a)

# a=[1,2,3]
# a.append(4)
# print(a) add 4 to the string

# a=[3,5,6,7,4]
# a.sort()
# print(a)

# print(a)
# print(a)


a = int(input("Enter a number from 1 to 7: "))

match a:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")    
    case 3:
        print("Tuesday")
    case 4:
        print("Wenesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
            print("Saturday")
    case _:
                print("Invalid day")  # This will be executed if the input is not 1,
        
    

# Main function
import numpy 

def main():
	# Initialise array
	array = []

	display_menu()
	
	while True:
		choice = input("Enter choice: ")
		
		if (choice == "1"):
			array = fill_array()
			display_menu()
		elif (choice == "2"):
			print(array)
			display_menu()
		elif (choice == "3"):
			find_gt_in_array(array)
			display_menu()
		elif (choice == "4"):
			break;
		else:
			display_menu()
			

# Write the necessary code to fill the array.
# -1 should not be part of the array			
def fill_array():
    array = []
    while True:
        try:
            num = int(input("Please, insert a number. To stop insert '-1': "))
            if num == -1:
                break
            array.append(num)
        except ValueError:
            print("Invalid input, Please enter a nubber")
    return array
     
	

# Write the necessary code to get a number from the user
# and print out all numbers in the array that are greater
# than this number
def find_gt_in_array(array):
	new_list = []
	num = int(input("Please, insert a number: "))
	for n in array:
		if n > num:
			new_list.append(n)
	print(new_list)



def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Fill Array")
    print("2 - Print Array")
    print("3 - Find > in Array")
    print("4 - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()

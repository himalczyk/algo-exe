'''
Create list in range 0-100
When, User inputs random number, the program check if the number is included in the list by first slicing half of the list.
If the number is found in the first half, it will eliminate the other one and vice versa.
The search continues until the program finds the number input of the user or the subarray size becomes 0.
This would mean that the number is not in the list itself. Range: 0-100. So user cannot provide something else, rule.


'''

list_range_100 = list(range(100))

ask_for_number_range_100 = int(input("Please provide a number between 0 and 99\n"))
found = False

if ask_for_number_range_100 in list_range_100:
    while found == False:
        lenght = len(list_range_100)
        middle_index = lenght//2
        first_half = list_range_100[:middle_index]
        second_half = list_range_100[middle_index:]
        
        for number in first_half:
            if ask_for_number_range_100 in first_half:
                print("first half")
                found = True
                break
        for number in second_half:
            if ask_for_number_range_100 in second_half:
                print("second half")
                found = True
                break
else:
    print("Number not in range from 0-99")
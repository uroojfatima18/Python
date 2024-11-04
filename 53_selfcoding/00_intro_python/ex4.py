# ex .4:

#  Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

# solution :
def main():
    # Introduction of the program
    print(" Program to solve age-realated riddle!")
    anton=21
    beth=anton+6             # Beth is 6 years older than Anton
    chen=beth+20             # Chen is 20 years older than Beth
    drew=chen+anton          # Drew is as old as Chen plus Anton
    ethan=chen               # Ethan is the same age as Chen

    # Responding with the user's input
    print("Anton is", anton, "years old.")    
    print("Beth is",beth ,"years old.")
    print("Chen is", chen, "years old.")
    print('Ethan is' ,chen, 'years old.')
    print('Drew is ', drew ,'years old.')


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
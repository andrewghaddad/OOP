# marbles
"""
Assume that you have a jar that contains 5 marbles
The jar has a capacity of 10 marbles.
Continually ask the user if they want to add or remove a marble
    - 'a' -> add a marble
    - 'r' -> remove a marble
    Make sure the user enters either 'a' or 'r'
If they add a marble, then you should increase the number of marbles in the jar
If they remove a marble, then you should decrease the number of marbles in the jar
Print out how many marbles there are after each update
If the jar becomes full or empty, you should terminate your program.
"""

jar = 5
while not (jar == 10 or jar == 0):
    choice = ""
    while choice != 'a' and choice != 'r':
        choice = input("Please enter 'a' to add to a marble or 'r' to remove a marble: ")
        if not(choice == 'a' or choice == 'r'):
            print("Invalid choice!")
        
    if choice == 'a':
        jar += 1
    elif choice == 'r':
        jar -= 1

    print("There are", jar, "marbles in jar.")

"""
1. Write code to complete a task once
2. Place that code into a loop
3. Write a condition to exit the loop
4. Double check your work
    a) before the loop
    b) during the loop
    c) after the loop
"""
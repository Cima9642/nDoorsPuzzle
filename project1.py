# Carlos Martinez
# fxv013
# CS-3343-001
# Project1
# This project solves the N Doors Puzzle using the various aspects of
# algorithmic thinking and Python programming discussed in class.

def n_doors(n):
    #initializer for all the doors as closed (False)

    doors = [False] * (n+1)

    #loop for the n passes, change boolean for every run
    for i in range(1, n+1):
        #check every n-ith door
        for j in range(i,n+1,i):
            #toggle doors (open/close)
            doors[j]= not doors[j]
            #print results
            print(f"i: {i}; j:{j}; step size: {i}. Toggling door number {j}.")
    #show the user the algorithm has finished
    print("\nAlgorithm has finished.\n")

    #PRINT DOORS STATUS

    #store the status as a list
    o_doors = []
    c_doors = []

    for i in range(1,n+1):
        #Is the door open?
        if doors[i]:
            o_doors.append(i)
            print(f"Door number {i} remains open.")
        else:
            c_doors.append(i)

    for i in c_doors:
        print(f"Door number {i} remains closed.")


    #BONUS

    #FizzBuzz Bonus results
    print("\nN Doors Puzzle's Fizz Buzz implementation: ")
    bonus_result = []

    for i in o_doors:
        #check if it's divisible by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            bonus_result.append("FizzBuzz")
        #check if it's divisible by 3
        elif i % 3 == 0:
            bonus_result.append("Fizz")
        #check if it's divisble by 5
        elif i % 5 == 0:
            bonus_result.append("Buzz")
        else:
            bonus_result.append(i)

    #print the results
    print(bonus_result)

#MAIN
if __name__ == "__main__":
    #error handling and user input
    try:
        #User input for the amount of doors
        N = int(input("Enter the number of Doors (N): "))
        if N <= 0:
            raise ValueError("Please enter a positive integer")
        n_doors(N)
    except ValueError as e:
        print(f"OOOOOPS invalid input: {e}")







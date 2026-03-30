def triangle(n):
    # n is passed as an argument, so no need to redefine it as a string
    k = n - 1
    
    # The loops must be INSIDE the function
    for i in range(0, n):
        # Print leading spaces
        for j in range(0, k):
            print(end=" ")
        
        # Decrement k for the next row
        k = k - 1
        
        # Print stars
        for j in range(0, i + 1):
            print("* ", end="")
            
        # Move to the next line after each row
        print("\r")

# Call the function with an integer
triangle(5)
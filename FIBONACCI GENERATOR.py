# Function to generate Fibonacci series up to 'n' terms
def generate_fibonacci(n):
    # Starting the series with the first two numbers: 0 and 1
    fibonacci_sequence = [0, 1]
    
    # Loop to generate the next numbers in the series until 'n' terms are reached
    for i in range(2, n):
        # Calculate the next number by summing the last two numbers in the sequence
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)
    
    # Return the series truncated to the requested number of terms (in case n < 2)
    return fibonacci_sequence[:n]

# Taking input from the user for the number of terms
try:
    terms = int(input("Enter the number of terms for the Fibonacci series: "))
    if terms <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        # Calling the function and printing the generated Fibonacci series
        print(f"Fibonacci series with {terms} terms: {generate_fibonacci(terms)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

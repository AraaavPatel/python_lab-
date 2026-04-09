# Sum all numbers from user input
def sum_of_numbers():
    numbers = input("Enter numbers separated by space: ")
    num_list = numbers.split()
    total_sum = sum(map(float, num_list))
    print(f"The sum of the numbers is: {total_sum}")        
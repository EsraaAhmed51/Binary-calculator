# Esraa Ahmed Kamal Hassan, 20230051
# Rawda Mohammed Abdelreheem, 20230562
# Aya Farahat Hassan Ali, 20230549

# menus
def menu1():
    print("** Binary Calculator **")
    print("A) Insert new numbers")
    print("B) Exit")


def menu2():
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) Addition")
    print("D) Subtraction")


# validation
binary_nums = {'0', '1'}


# operations
def addition(binary_num1, binary_num2):
    # Make the lengths of both numbers equal by padding with zeros
    max_len = max(len(binary_num1), len(binary_num2))
    binary_num1 = binary_num1.zfill(max_len)
    binary_num2 = binary_num2.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        bit_sum = int(binary_num1[i]) + int(binary_num2[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2

    # If there's a carry left, add it to the leftmost side of the result
    if carry:
        result = '1' + result

    return result
"""
input1 = "1101"
input2 = "100"
output(addition) = "10001"
"""

# subtraction
def subtract_binary(larger_bin, smaller_bin):
    # Make the lengths of both numbers equal by padding with zeros
    max_len = max(len(larger_bin), len(smaller_bin))
    larger_bin = larger_bin.zfill(max_len)
    smaller_bin = smaller_bin.zfill(max_len)

    result = ''
    borrow = 0

    # Iterate over the binary digits from right to left
    for i in range(max_len - 1, -1, -1):
        bit_diff = int(larger_bin[i]) - int(smaller_bin[i]) - borrow

        if bit_diff < 0:
            bit_diff += 2  # Borrow 1 from the next higher bit
            borrow = 1
        else:
            borrow = 0

        result = str(bit_diff) + result

    return result
"""
input1 = "1101"
input2 = "100"
output(subtraction) = "1001"
"""
# ones_complement
def compute_ones_complement(number):
    ones_complement = ''
    for bit in number:
        if bit == '0':
            ones_complement += '1'
        else:
            ones_complement += '0'

    return ones_complement
"""
input = "1100"
output(one's complement) = "0011"
"""

# twos_complement
def compute_twos_complement(number):
    # Calculate one's complement
    ones_complement = ''
    for bit in number:
        if bit == '0':
            ones_complement += '1'
        else:
            ones_complement += '0'

    # Add 1 to one's complement
    twos_complement = ''
    carry = 1
    for bit in ones_complement[::-1]:
        if bit == '1' and carry == 1:
            twos_complement = '0' + twos_complement
        elif bit == '0' and carry == 1:
            twos_complement = '1' + twos_complement
            carry = 0
        else:
            twos_complement = bit + twos_complement

    return twos_complement
"""
input = "1010"
output(two's complement) = "0110"
"""
# running the program
while True:
    menu1()
    choice1 = str(input("Enter your choice (A/B): ").upper())

    if choice1 == "A":
        num1 = input("Insert a binary number: ")

        # Validate the input
        if set(num1) <= binary_nums:
            menu2()
            choice2 = str(input("Enter your choice (A/B/C/D): ").upper())
            result = ""

            if choice2 in ["A", "B", "C", "D"]:
                if choice2 == "A":
                    result = compute_ones_complement(num1)
                elif choice2 == "B":
                    result = compute_twos_complement(num1)
                elif choice2 == "C":
                    num2 = input("Please enter a second number: ")

                    # Validate the second input
                    if set(num2) <= binary_nums:
                        result = addition(num1, num2)
                    else:
                        print("Please enter a valid binary number")
                        continue

                elif choice2 == "D":
                    num2 = input("Please enter a second number: ")

                    # Validate the second input
                    if set(num2) <= binary_nums:
                        if int(num2, 2) > int(num1, 2):
                            print(f"Please enter a smaller number than {num1}.")
                            continue
                        else:
                            result = subtract_binary(num1, num2)
                    else:
                        print("Please enter a valid binary number")
                        continue
            else:
                print("Please enter a valid choice (A/B/C/D):")
                continue

            print("The answer is :", result)
        else:
            print("Please enter a valid binary number")
    elif choice1 == "B":
        print("Exiting Program")
        break
    else:
        print("Please enter a valid choice (A/B)")

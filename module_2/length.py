def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count


str1 = input("Enter a string: ")
print("Length of the string is: ", string_length(str1))
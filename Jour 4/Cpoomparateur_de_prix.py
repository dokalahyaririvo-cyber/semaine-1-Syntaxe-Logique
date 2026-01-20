def min (a, b) :
    if a < b :
        return a
    else :
        return b

first_value = int(input("Enter the first value: "))
second_value = int(input("Enter the second value: "))
min_value = min(first_value, second_value)
print("The minimum value is :", min_value)
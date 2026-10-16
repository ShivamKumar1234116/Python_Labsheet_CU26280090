# ==============================================================================
# Lab Sheet-05: Python Programming Lab – Tuples Operations
# MCA I Semester (Session 2026-2027)
# COER University, Roorkee
# ==============================================================================


# ==============================================================================
# Q1: Write a Python program to create and display a tuple.
# ==============================================================================
# Q1_tuple_creation.py

user_input = input("Enter elements separated by space: ").strip()

# Create a tuple from user input
elements_tuple = tuple(user_input.split())

print("Created Tuple:", elements_tuple)
print("Type:", type(elements_tuple))
print("Number of elements in tuple:", len(elements_tuple))


# ==============================================================================
# Q2: Write a program to create a tuple with different data types.
# ==============================================================================
# Q2_tuple_mixed_data_types.py

int_val = int(input("Enter an integer value: "))
float_val = float(input("Enter a floating-point value: "))
str_val = input("Enter a string value: ").strip()
bool_val = input("Enter a boolean value (True/False): ").strip().lower() == "true"

# Construct a tuple with mixed data types
mixed_tuple = (int_val, float_val, str_val, bool_val)

print("\nMixed Data Type Tuple:", mixed_tuple)
print("Element Data Types:")
for index, item in enumerate(mixed_tuple):
    print(f"Index {index} -> Value: {item} | Type: {type(item).__name__}")


# ==============================================================================
# Q3: Write a program to find the length of a tuple.
# ==============================================================================
# Q3_tuple_length.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

# Calculate length manually using a loop without built-in len()
count = 0
for _ in tup:
    count += 1

print("Tuple:", tup)
print("Length of the tuple (calculated manually):", count)


# ==============================================================================
# Q4: Write a program to access tuple elements using indexing.
# ==============================================================================
# Q4_tuple_indexing.py

user_input = input("Enter elements separated by space: ").strip()

if not user_input:
    print("Tuple is empty.")
else:
    tup = tuple(user_input.split())
    print("Tuple:", tup)
    idx = int(input(f"Enter an index to access (0 to {len(tup) - 1}): "))

    if -len(tup) <= idx < len(tup):
        print(f"Element at index {idx}: {tup[idx]}")
        print(f"First element (index 0): {tup[0]}")
        print(f"Last element (index -1): {tup[-1]}")
    else:
        print("Index out of range.")


# ==============================================================================
# Q5: Write a program to access tuple elements using slicing.
# ==============================================================================
# Q5_tuple_slicing.py

user_input = input("Enter elements separated by space: ").strip()

if not user_input:
    print("Tuple is empty.")
else:
    tup = tuple(user_input.split())
    print("Original Tuple:", tup)

    start = int(input("Enter start index for slicing: "))
    end = int(input("Enter end index for slicing: "))

    print(f"Slice tup[{start}:{end}]:", tup[start:end])
    print("First 3 elements tup[:3]:", tup[:3])
    print("Elements from index 2 to end tup[2:]:", tup[2:])
    print("Tuple reversed using slicing tup[::-1]:", tup[::-1])


# ==============================================================================
# Q6: Write a program to check if an element exists in a tuple.
# ==============================================================================
# Q6_check_element_exists.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

target = input("Enter the element to search: ").strip()

# Check existence manually using a loop
exists = False
for item in tup:
    if item == target:
        exists = True
        break

if exists:
    print(f"Element '{target}' exists in the tuple.")
else:
    print(f"Element '{target}' does NOT exist in the tuple.")


# ==============================================================================
# Q7: Write a program to count the occurrences of an element in a tuple.
# ==============================================================================
# Q7_count_occurrences.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

target = input("Enter the element to count: ").strip()

# Count occurrences manually using a loop
frequency = 0
for item in tup:
    if item == target:
        frequency += 1

print("Tuple:", tup)
print(f"The element '{target}' occurs {frequency} time(s) in the tuple.")


# ==============================================================================
# Q8: Write a program to find the index of an element in a tuple.
# ==============================================================================
# Q8_find_element_index.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

target = input("Enter the element whose index you want to find: ").strip()

# Find the first index manually using a loop
found_index = -1
for i in range(len(tup)):
    if tup[i] == target:
        found_index = i
        break

if found_index != -1:
    print(f"The first occurrence of '{target}' is at index {found_index}.")
else:
    print(f"Element '{target}' was not found in the tuple.")


# ==============================================================================
# Q9: Write a program to concatenate two tuples.
# ==============================================================================
# Q9_concatenate_tuples.py

input1 = input("Enter elements for Tuple 1 separated by space: ").strip()
input2 = input("Enter elements for Tuple 2 separated by space: ").strip()

tuple1 = tuple(input1.split()) if input1 else ()
tuple2 = tuple(input2.split()) if input2 else ()

# Concatenate tuples using + operator
concatenated_tuple = tuple1 + tuple2

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Concatenated Tuple:", concatenated_tuple)


# ==============================================================================
# Q10: Write a program to repeat a tuple n times.
# ==============================================================================
# Q10_repeat_tuple.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

n = int(input("Enter number of repetitions (n): "))

# Repeat tuple using * operator
repeated_tuple = tup * n

print("Original Tuple:", tup)
print(f"Tuple repeated {n} times:", repeated_tuple)


# ==============================================================================
# Q11: Write a program to convert a list into a tuple.
# ==============================================================================
# Q11_list_to_tuple.py

user_input = input("Enter list elements separated by space: ").strip()
input_list = user_input.split() if user_input else []

# Convert list to tuple
converted_tuple = tuple(input_list)

print("Original List:", input_list, "| Type:", type(input_list))
print("Converted Tuple:", converted_tuple, "| Type:", type(converted_tuple))


# ==============================================================================
# Q12: Write a program to convert a tuple into a string.
# ==============================================================================
# Q12_tuple_to_string.py

user_input = input("Enter tuple elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

# Convert tuple to string manually without using join()
result_str = ""
for item in tup:
    result_str += str(item)

# Also create space-separated string manually
spaced_str = ""
for i in range(len(tup)):
    spaced_str += str(tup[i])
    if i < len(tup) - 1:
        spaced_str += " "

print("Tuple:", tup)
print("Converted to string (concatenated):", result_str)
print("Converted to string (with spaces):", spaced_str)


# ==============================================================================
# Q13: Write a program to find the maximum and minimum values in a tuple.
# ==============================================================================
# Q13_max_min_in_tuple.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("Tuple is empty.")
else:
    numbers_tuple = tuple(float(x) for x in user_input.split())

    # Find max and min manually without using max() or min()
    max_val = numbers_tuple[0]
    min_val = numbers_tuple[0]

    for val in numbers_tuple:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val

    print("Numbers Tuple:", numbers_tuple)
    print("Maximum Value:", max_val)
    print("Minimum Value:", min_val)


# ==============================================================================
# Q14: Write a program to calculate the sum of numeric elements in a tuple.
# ==============================================================================
# Q14_sum_of_tuple_elements.py

user_input = input("Enter numeric values separated by space: ").strip()

if not user_input:
    print("Tuple is empty.")
else:
    numbers_tuple = tuple(float(x) for x in user_input.split())

    # Calculate sum manually using a loop without built-in sum()
    total_sum = 0
    for num in numbers_tuple:
        total_sum += num

    print("Numbers Tuple:", numbers_tuple)
    print("Sum of elements:", total_sum)


# ==============================================================================
# Q15: Write a program to sort a tuple of numbers in ascending order.
# ==============================================================================
# Q15_sort_tuple_numbers.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("Tuple is empty.")
else:
    numbers_tuple = tuple(float(x) for x in user_input.split())

    # Pure tuple selection sort without converting to list
    temp_tup = numbers_tuple
    sorted_tuple = ()

    while temp_tup:
        # Find minimum element and its index
        min_val = temp_tup[0]
        min_idx = 0
        for i in range(1, len(temp_tup)):
            if temp_tup[i] < min_val:
                min_val = temp_tup[i]
                min_idx = i

        # Concatenate minimum value to sorted_tuple
        sorted_tuple += (min_val,)
        # Remove minimum value from temp_tup using slicing
        temp_tup = temp_tup[:min_idx] + temp_tup[min_idx + 1:]

    print("Original Tuple:", numbers_tuple)
    print("Sorted Tuple (ascending):", sorted_tuple)


# ==============================================================================
# Q16: Write a program to sort a tuple of strings alphabetically.
# ==============================================================================
# Q16_sort_tuple_strings.py

user_input = input("Enter strings/words separated by space: ").strip()

if not user_input:
    print("Tuple is empty.")
else:
    strings_tuple = tuple(user_input.split())

    # Pure tuple selection sort alphabetically without converting to list
    temp_tup = strings_tuple
    sorted_tuple = ()

    while temp_tup:
        min_val = temp_tup[0]
        min_idx = 0
        for i in range(1, len(temp_tup)):
            if temp_tup[i].lower() < min_val.lower():
                min_val = temp_tup[i]
                min_idx = i

        sorted_tuple += (min_val,)
        temp_tup = temp_tup[:min_idx] + temp_tup[min_idx + 1:]

    print("Original Tuple:", strings_tuple)
    print("Alphabetically Sorted Tuple:", sorted_tuple)


# ==============================================================================
# Q17: Write a program to reverse a tuple.
# ==============================================================================
# Q17_reverse_tuple.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

# Reverse using pure tuple concatenation in reverse order
reversed_tuple = ()
for i in range(len(tup) - 1, -1, -1):
    reversed_tuple += (tup[i],)

print("Original Tuple:", tup)
print("Reversed Tuple:", reversed_tuple)


# ==============================================================================
# Q18: Write a program to check if two tuples are equal.
# ==============================================================================
# Q18_check_tuples_equal.py

input1 = input("Enter elements for Tuple 1 separated by space: ").strip()
input2 = input("Enter elements for Tuple 2 separated by space: ").strip()

tuple1 = tuple(input1.split()) if input1 else ()
tuple2 = tuple(input2.split()) if input2 else ()

# Check equality manually without using == shortcut
are_equal = True

if len(tuple1) != len(tuple2):
    are_equal = False
else:
    for i in range(len(tuple1)):
        if tuple1[i] != tuple2[i]:
            are_equal = False
            break

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

if are_equal:
    print("The two tuples are equal.")
else:
    print("The two tuples are NOT equal.")


# ==============================================================================
# Q19: Write a program to remove duplicate elements from a tuple.
# ==============================================================================
# Q19_remove_duplicates_tuple.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

# Remove duplicates maintaining order using pure tuple concatenation
unique_tuple = ()
for item in tup:
    if item not in unique_tuple:
        unique_tuple += (item,)

print("Original Tuple:", tup)
print("Tuple after removing duplicates:", unique_tuple)


# ==============================================================================
# Q20: Write a program to find the length of the longest word in a tuple.
# ==============================================================================
# Q20_longest_word_in_tuple.py

user_input = input("Enter words separated by space: ").strip()

if not user_input:
    print("Tuple is empty.")
else:
    words_tuple = tuple(user_input.split())

    longest_word = ""
    max_len = 0

    for word in words_tuple:
        # Measure length manually
        current_len = 0
        for _ in word:
            current_len += 1

        if current_len > max_len:
            max_len = current_len
            longest_word = word

    print("Words Tuple:", words_tuple)
    print(f"Longest word: '{longest_word}' with length: {max_len}")


# ==============================================================================
# Q21: Write a program to create a nested tuple and access its elements.
# ==============================================================================
# Q21_nested_tuple.py

num_records = int(input("Enter number of inner tuples to create: "))
nested_tuple = ()

for i in range(num_records):
    print(f"Enter details for record {i + 1}:")
    roll = input("  Enter Roll No: ").strip()
    name = input("  Enter Name: ").strip()
    marks = input("  Enter Marks: ").strip()
    nested_tuple += ((roll, name, marks),)

print("\nNested Tuple:", nested_tuple)
print("\nAccessing Elements using indexing [i][j]:")
for i in range(len(nested_tuple)):
    print(f"Record {i + 1} (Tuple index {i}): {nested_tuple[i]}")
    print(f"  Roll: {nested_tuple[i][0]} | Name: {nested_tuple[i][1]} | Marks: {nested_tuple[i][2]}")


# ==============================================================================
# Q22: Write a program to flatten a nested tuple.
# ==============================================================================
# Q22_flatten_nested_tuple.py

def flatten_tuple(nested):
    flat = ()
    for item in nested:
        if isinstance(item, tuple):
            flat += flatten_tuple(item)
        else:
            flat += (item,)
    return flat

user_input = input("Enter nested tuple (e.g. (1, (2, 3), (4, (5, 6)), 7)): ").strip()

try:
    nested = eval(user_input)
    if not isinstance(nested, tuple):
        print("Input is not a tuple.")
    else:
        flattened = flatten_tuple(nested)
        print("Flattened Tuple:", flattened)
except Exception as e:
    print("Invalid tuple input format:", e)


# ==============================================================================
# Q23: Write a program to swap two tuples.
# ==============================================================================
# Q23_swap_tuples.py

input1 = input("Enter elements for Tuple 1 separated by space: ").strip()
input2 = input("Enter elements for Tuple 2 separated by space: ").strip()

tuple1 = tuple(input1.split()) if input1 else ()
tuple2 = tuple(input2.split()) if input2 else ()

print("\n--- Before Swapping ---")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Swap tuples using tuple unpacking
tuple1, tuple2 = tuple2, tuple1

print("\n--- After Swapping ---")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)


# ==============================================================================
# Q24: Write a program to find common elements between two tuples.
# ==============================================================================
# Q24_common_elements_tuples.py

input1 = input("Enter elements for Tuple 1 separated by space: ").strip()
input2 = input("Enter elements for Tuple 2 separated by space: ").strip()

tuple1 = tuple(input1.split()) if input1 else ()
tuple2 = tuple(input2.split()) if input2 else ()

common_tuple = ()

# Find common elements without using set()
for item in tuple1:
    if item in tuple2 and item not in common_tuple:
        common_tuple += (item,)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Common elements tuple:", common_tuple)


# ==============================================================================
# Q25: Write a program to find the difference between two tuples.
# ==============================================================================
# Q25_difference_tuples.py

input1 = input("Enter elements for Tuple 1 separated by space: ").strip()
input2 = input("Enter elements for Tuple 2 separated by space: ").strip()

tuple1 = tuple(input1.split()) if input1 else ()
tuple2 = tuple(input2.split()) if input2 else ()

# Elements in tuple1 that are NOT in tuple2
diff_tuple = ()

for item in tuple1:
    if item not in tuple2 and item not in diff_tuple:
        diff_tuple += (item,)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Difference (Tuple 1 - Tuple 2):", diff_tuple)


# ==============================================================================
# Q26: Write a program to convert a tuple of tuples into a dictionary.
# ==============================================================================
# Q26_tuple_of_tuples_to_dict.py

n = int(input("Enter number of key-value pairs: "))
pairs_tuple = ()

for i in range(n):
    key = input(f"Enter key for pair {i + 1}: ").strip()
    val = input(f"Enter value for pair {i + 1}: ").strip()
    pairs_tuple += ((key, val),)

# Convert tuple of tuples to dictionary
result_dict = {}
for pair in pairs_tuple:
    k, v = pair
    result_dict[k] = v

print("\nTuple of Tuples:", pairs_tuple)
print("Converted Dictionary:", result_dict)


# ==============================================================================
# Q27: Write a program to unzip a list of tuples into individual lists.
# ==============================================================================
# Q27_unzip_tuples_to_lists.py

n = int(input("Enter number of tuples in list: "))
list_of_tuples = []

for i in range(n):
    entry = input(f"Enter elements of tuple {i + 1} separated by space: ").strip().split()
    list_of_tuples.append(tuple(entry))

if not list_of_tuples:
    print("List is empty.")
else:
    num_cols = len(list_of_tuples[0])
    unzipped_lists = [[] for _ in range(num_cols)]

    # Unzip into separate lists
    for tup in list_of_tuples:
        for col_idx in range(min(len(tup), num_cols)):
            unzipped_lists[col_idx].append(tup[col_idx])

    print("\nOriginal List of Tuples:", list_of_tuples)
    print("Unzipped Individual Lists:")
    for idx, lst in enumerate(unzipped_lists):
        print(f"List {idx + 1}: {lst}")


# ==============================================================================
# Q28: Write a program to find repeated items in a tuple.
# ==============================================================================
# Q28_find_repeated_items.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

repeated_items = ()

# Identify elements occurring more than once without using set()
for i in range(len(tup)):
    count = 0
    for j in range(len(tup)):
        if tup[i] == tup[j]:
            count += 1
    if count > 1 and tup[i] not in repeated_items:
        repeated_items += (tup[i],)

print("Original Tuple:", tup)
if repeated_items:
    print("Repeated items in tuple:", repeated_items)
else:
    print("No repeated items found in the tuple.")


# ==============================================================================
# Q29: Write a program to check if all elements in a tuple are the same.
# ==============================================================================
# Q29_check_all_elements_same.py

user_input = input("Enter elements separated by space: ").strip()
tup = tuple(user_input.split()) if user_input else ()

if len(tup) <= 1:
    all_same = True
else:
    first_item = tup[0]
    all_same = True
    for item in tup:
        if item != first_item:
            all_same = False
            break

print("Tuple:", tup)
if all_same:
    print("All elements in the tuple are the same.")
else:
    print("Elements in the tuple are NOT all the same.")


# ==============================================================================
# Q30: Write a program to find the element-wise sum of two tuples.
# ==============================================================================
# Q30_element_wise_sum_tuples.py

input1 = input("Enter numbers for Tuple 1 separated by space: ").strip()
input2 = input("Enter numbers for Tuple 2 separated by space: ").strip()

tuple1 = tuple(float(x) for x in input1.split()) if input1 else ()
tuple2 = tuple(float(x) for x in input2.split()) if input2 else ()

if len(tuple1) != len(tuple2):
    print("Error: Both tuples must have the same number of elements for element-wise sum.")
else:
    element_wise_sum = ()
    for i in range(len(tuple1)):
        element_wise_sum += (tuple1[i] + tuple2[i],)

    print("Tuple 1:", tuple1)
    print("Tuple 2:", tuple2)
    print("Element-wise Sum Tuple:", element_wise_sum)

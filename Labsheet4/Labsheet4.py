# ==============================================================================
# Lab Sheet-04: Python Programming Lab – List and Dictionary Operations
# MCA I Semester (Session 2026-2027)
# COER University, Roorkee
# ==============================================================================


# ==============================================================================
# Q1: Find the sum and average of elements in a list.
# ==============================================================================
# Q1_sum_and_average.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("The list is empty. Cannot compute sum and average.")
else:
    numbers = [float(x) for x in user_input.split()]
    total_sum = 0
    count = 0

    # Calculate sum and count manually without using built-in sum() or len()
    for num in numbers:
        total_sum += num
        count += 1

    average = total_sum / count

    print("Sum of elements:", total_sum)
    print("Average of elements:", average)


# ==============================================================================
# Q2: Rotate a list by n positions.
# ==============================================================================
# Q2_rotate_list.py

user_input = input("Enter list elements separated by space: ").strip()

if not user_input:
    print("The list is empty.")
else:
    elements = user_input.split()
    n = int(input("Enter number of positions to rotate (right shift): "))
    length = len(elements)

    # Normalize n in case n is larger than length
    n = n % length

    # Rotate list manually using loops
    rotated = []
    # Append the last n elements
    for i in range(length - n, length):
        rotated.append(elements[i])
    # Append the remaining elements from the beginning
    for i in range(length - n):
        rotated.append(elements[i])

    print("Original list:", elements)
    print(f"List rotated by {n} positions:", rotated)


# ==============================================================================
# Q3: Remove all negative numbers from a list.
# ==============================================================================
# Q3_remove_negative_numbers.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("The list is empty.")
else:
    numbers = [float(x) for x in user_input.split()]
    positive_numbers = []

    # Filter out negative numbers using a loop
    for num in numbers:
        if num >= 0:
            positive_numbers.append(num)

    print("Original list:", numbers)
    print("List after removing negative numbers:", positive_numbers)


# ==============================================================================
# Q4: Find the product of all elements in a list.
# ==============================================================================
# Q4_product_of_elements.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("The list is empty.")
else:
    numbers = [float(x) for x in user_input.split()]
    product = 1

    # Compute product manually
    for num in numbers:
        product *= num

    print("Product of all elements:", product)


# ==============================================================================
# Q5: Create a list of squares of numbers from 1 to n.
# ==============================================================================
# Q5_list_of_squares.py

n = int(input("Enter positive integer n: "))

if n < 1:
    print("Please enter a number greater than or equal to 1.")
else:
    squares = []
    for i in range(1, n + 1):
        squares.append(i * i)

    print(f"List of squares from 1 to {n}:", squares)


# ==============================================================================
# Q6: Split a list into two halves.
# ==============================================================================
# Q6_split_list_two_halves.py

user_input = input("Enter elements separated by space: ").strip()

if not user_input:
    print("The list is empty.")
else:
    elements = user_input.split()
    total_length = len(elements)
    midpoint = total_length // 2

    first_half = []
    second_half = []

    for i in range(total_length):
        if i < midpoint:
            first_half.append(elements[i])
        else:
            second_half.append(elements[i])

    print("Original list:", elements)
    print("First half:", first_half)
    print("Second half:", second_half)


# ==============================================================================
# Q7: Check if a list is sorted or not.
# ==============================================================================
# Q7_check_sorted.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("The list is empty.")
else:
    numbers = [float(x) for x in user_input.split()]
    is_sorted_asc = True
    is_sorted_desc = True

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            is_sorted_asc = False
        if numbers[i] < numbers[i + 1]:
            is_sorted_desc = False

    if is_sorted_asc:
        print("The list is sorted in ascending order.")
    elif is_sorted_desc:
        print("The list is sorted in descending order.")
    else:
        print("The list is not sorted.")


# ==============================================================================
# Q8: Find pairs of numbers in a list whose sum is equal to a given number.
# ==============================================================================
# Q8_find_pairs_with_sum.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("The list is empty.")
else:
    numbers = [int(x) for x in user_input.split()]
    target_sum = int(input("Enter the target sum: "))

    pairs = []
    # Find all unique pairs without using set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                pair = (numbers[i], numbers[j])
                already_exists = False
                for p in pairs:
                    if (p[0] == pair[0] and p[1] == pair[1]) or (p[0] == pair[1] and p[1] == pair[0]):
                        already_exists = True
                        break
                if not already_exists:
                    pairs.append(pair)

    if len(pairs) == 0:
        print(f"No pairs found with sum equal to {target_sum}.")
    else:
        print(f"Pairs with sum {target_sum}:", pairs)


# ==============================================================================
# Q9: Flatten a nested list.
# ==============================================================================
# Q9_flatten_nested_list.py

def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            for sub_item in flatten_list(item):
                flat.append(sub_item)
        else:
            flat.append(item)
    return flat

user_input = input("Enter a nested list (e.g. [1, [2, 3], [4, [5, 6]], 7]): ").strip()

try:
    nested_list = eval(user_input)
    if not isinstance(nested_list, list):
        print("Input is not a list.")
    else:
        flattened = flatten_list(nested_list)
        print("Flattened list:", flattened)
except Exception as e:
    print("Invalid list format:", e)


# ==============================================================================
# Q10: Convert a list into a string without using join().
# ==============================================================================
# Q10_list_to_string_without_join.py

user_input = input("Enter elements separated by space: ").strip()

if not user_input:
    print("The list is empty.")
else:
    elements = user_input.split()
    
    # Concatenate directly without separator
    result = ""
    for item in elements:
        result += str(item)

    # Concatenate with space separator manually
    spaced_result = ""
    for i in range(len(elements)):
        spaced_result += str(elements[i])
        if i < len(elements) - 1:
            spaced_result += " "

    print("Concatenated string (without spaces):", result)
    print("Concatenated string (with spaces):", spaced_result)


# ==============================================================================
# Q11: Create a dictionary of student names and marks and display it.
# ==============================================================================
# Q11_student_marks.py

num_students = int(input("Enter the number of students: "))
student_records = {}

for i in range(num_students):
    name = input(f"Enter name of student {i + 1}: ").strip()
    marks = float(input(f"Enter marks for {name}: "))
    student_records[name] = marks

print("\n--- Student Details ---")
for name, marks in student_records.items():
    print(f"Student: {name} | Marks: {marks}")


# ==============================================================================
# Q12: Find the maximum and minimum marks from a dictionary.
# ==============================================================================
# Q12_max_min_marks.py

num_students = int(input("Enter the number of students: "))

if num_students <= 0:
    print("No students to evaluate.")
else:
    students = {}
    for i in range(num_students):
        name = input(f"Enter student name {i + 1}: ").strip()
        marks = float(input(f"Enter marks for {name}: "))
        students[name] = marks

    # Find max and min without using built-in max() or min()
    max_marks = None
    min_marks = None
    top_student = ""
    lowest_student = ""

    for name, marks in students.items():
        if max_marks is None or marks > max_marks:
            max_marks = marks
            top_student = name
        if min_marks is None or marks < min_marks:
            min_marks = marks
            lowest_student = name

    print(f"Maximum Marks: {max_marks} (Scored by: {top_student})")
    print(f"Minimum Marks: {min_marks} (Scored by: {lowest_student})")


# ==============================================================================
# Q13: Count the frequency of characters in a string using a dictionary.
# ==============================================================================
# Q13_character_frequency_dict.py

text = input("Enter a string: ")

char_frequency = {}

for ch in text:
    if ch in char_frequency:
        char_frequency[ch] += 1
    else:
        char_frequency[ch] = 1

print("\n--- Character Frequencies ---")
for ch, freq in char_frequency.items():
    print(f"'{ch}': {freq}")


# ==============================================================================
# Q14: Merge two dictionaries into one.
# ==============================================================================
# Q14_merge_dictionaries.py

n1 = int(input("Enter number of entries for Dictionary 1: "))
dict1 = {}
for _ in range(n1):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    dict1[k] = v

n2 = int(input("Enter number of entries for Dictionary 2: "))
dict2 = {}
for _ in range(n2):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    dict2[k] = v

merged_dict = {}

# Copy all key-value pairs from dict1
for key, value in dict1.items():
    merged_dict[key] = value

# Copy/update key-value pairs from dict2
for key, value in dict2.items():
    merged_dict[key] = value

print("\nDictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)


# ==============================================================================
# Q15: Sort a dictionary by keys.
# ==============================================================================
# Q15_sort_dict_by_keys.py

n = int(input("Enter number of entries in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    d[k] = v

keys_list = list(d.keys())

# Bubble sort on keys without using built-in sorted()
for i in range(len(keys_list)):
    for j in range(0, len(keys_list) - i - 1):
        if keys_list[j] > keys_list[j + 1]:
            keys_list[j], keys_list[j + 1] = keys_list[j + 1], keys_list[j]

sorted_by_keys = {}
for key in keys_list:
    sorted_by_keys[key] = d[key]

print("Dictionary sorted by keys:", sorted_by_keys)


# ==============================================================================
# Q16: Sort a dictionary by values.
# ==============================================================================
# Q16_sort_dict_by_values.py

n = int(input("Enter number of entries in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter key: ").strip()
    v = float(input(f"Enter numeric value for '{k}': "))
    d[k] = v

items_list = list(d.items())

# Bubble sort by value without using built-in sorted() or lambda
for i in range(len(items_list)):
    for j in range(0, len(items_list) - i - 1):
        if items_list[j][1] > items_list[j + 1][1]:
            items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]

sorted_by_values = {}
for k, v in items_list:
    sorted_by_values[k] = v

print("Dictionary sorted by values:", sorted_by_values)


# ==============================================================================
# Q17: Update the value of a key in a dictionary.
# ==============================================================================
# Q17_update_key_value.py

n = int(input("Enter number of entries in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    d[k] = v

print("Current dictionary:", d)
search_key = input("Enter key to update: ").strip()

if search_key in d:
    new_value = input(f"Enter new value for key '{search_key}': ").strip()
    d[search_key] = new_value
    print("Updated successfully!")
    print("Updated dictionary:", d)
else:
    print(f"Key '{search_key}' does not exist in the dictionary.")


# ==============================================================================
# Q18: Remove a key from a dictionary.
# ==============================================================================
# Q18_remove_key.py

n = int(input("Enter number of entries in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    d[k] = v

print("Current dictionary:", d)
key_to_remove = input("Enter key to remove: ").strip()

if key_to_remove in d:
    del d[key_to_remove]
    print(f"Key '{key_to_remove}' removed successfully.")
    print("Updated dictionary:", d)
else:
    print(f"Key '{key_to_remove}' does not exist in the dictionary.")


# ==============================================================================
# Q19: Check if a key exists in a dictionary.
# ==============================================================================
# Q19_check_key_exists.py

n = int(input("Enter number of entries in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    d[k] = v

key_to_check = input("Enter key to check: ").strip()

# Check key existence manually
exists = False
for k in d:
    if k == key_to_check:
        exists = True
        break

if exists:
    print(f"Key '{key_to_check}' exists in dictionary with value: '{d[key_to_check]}'")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")


# ==============================================================================
# Q20: Find the sum of all values in a dictionary.
# ==============================================================================
# Q20_sum_of_values.py

n = int(input("Enter number of items in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter item name/key: ").strip()
    v = float(input(f"Enter numeric value for '{k}': "))
    d[k] = v

# Calculate sum manually without built-in sum()
total_sum = 0
for value in d.values():
    total_sum += value

print("Dictionary:", d)
print("Sum of all values:", total_sum)


# ==============================================================================
# Q21: Find the key with the maximum value in a dictionary.
# ==============================================================================
# Q21_key_with_max_value.py

n = int(input("Enter number of items in dictionary: "))

if n <= 0:
    print("Dictionary is empty.")
else:
    d = {}
    for _ in range(n):
        k = input("Enter key: ").strip()
        v = float(input(f"Enter numeric value for '{k}': "))
        d[k] = v

    # Find max key without built-in max()
    max_key = None
    max_value = None

    for k, v in d.items():
        if max_value is None or v > max_value:
            max_value = v
            max_key = k

    print("Dictionary:", d)
    print(f"The key with maximum value is '{max_key}' with value {max_value}")


# ==============================================================================
# Q22: Create a dictionary with numbers as keys and their squares as values.
# ==============================================================================
# Q22_numbers_and_squares_dict.py

n = int(input("Enter positive integer n: "))

if n < 1:
    print("Please enter a number greater than or equal to 1.")
else:
    squares_dict = {}
    for i in range(1, n + 1):
        squares_dict[i] = i * i

    print(f"Dictionary of numbers 1 to {n} and their squares:")
    print(squares_dict)


# ==============================================================================
# Q23: Convert two lists into a dictionary.
# ==============================================================================
# Q23_two_lists_to_dict.py

keys_input = input("Enter keys separated by space: ").strip().split()
values_input = input("Enter values separated by space: ").strip().split()

min_length = len(keys_input) if len(keys_input) < len(values_input) else len(values_input)

result_dict = {}
# Associate keys and values without using zip()
for i in range(min_length):
    result_dict[keys_input[i]] = values_input[i]

print("Keys list:", keys_input)
print("Values list:", values_input)
print("Resulting dictionary:", result_dict)


# ==============================================================================
# Q24: Invert a dictionary (keys become values and values become keys).
# ==============================================================================
# Q24_invert_dictionary.py

n = int(input("Enter number of entries in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    d[k] = v

inverted_dict = {}
for k, v in d.items():
    inverted_dict[v] = k

print("Original dictionary:", d)
print("Inverted dictionary:", inverted_dict)


# ==============================================================================
# Q25: Count word frequency in a given paragraph using a dictionary.
# ==============================================================================
# Q25_word_frequency_paragraph.py

paragraph = input("Enter a paragraph: ").strip()

# List of punctuation characters to clean
punctuation = ".,!?;:'\"()[]{}-_/\t\n"

words = paragraph.split()
word_frequency = {}

for word in words:
    # Clean the word by stripping punctuation
    cleaned_word = ""
    for ch in word:
        if ch not in punctuation:
            cleaned_word += ch
    
    cleaned_word = cleaned_word.lower()

    if cleaned_word != "":
        if cleaned_word in word_frequency:
            word_frequency[cleaned_word] += 1
        else:
            word_frequency[cleaned_word] = 1

print("\n--- Word Frequencies ---")
for word, freq in word_frequency.items():
    print(f"'{word}': {freq}")


# ==============================================================================
# Q26: Check if two dictionaries are equal.
# ==============================================================================
# Q26_check_dictionaries_equal.py

n1 = int(input("Enter number of entries in Dictionary 1: "))
dict1 = {}
for _ in range(n1):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    dict1[k] = v

n2 = int(input("Enter number of entries in Dictionary 2: "))
dict2 = {}
for _ in range(n2):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    dict2[k] = v

# Check equality manually without using == shortcut
are_equal = True

if len(dict1) != len(dict2):
    are_equal = False
else:
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            are_equal = False
            break

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

if are_equal:
    print("Both dictionaries are equal.")
else:
    print("Dictionaries are not equal.")


# ==============================================================================
# Q27: Remove duplicate values from a dictionary.
# ==============================================================================
# Q27_remove_duplicate_values.py

n = int(input("Enter number of entries in dictionary: "))
d = {}
for _ in range(n):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    d[k] = v

unique_value_dict = {}
seen_values = []

# Retain only the first key associated with each unique value (without set())
for k, v in d.items():
    if v not in seen_values:
        seen_values.append(v)
        unique_value_dict[k] = v

print("Original dictionary:", d)
print("Dictionary after removing duplicate values:", unique_value_dict)


# ==============================================================================
# Q28: Create a nested dictionary for student details (Name, Roll, Marks).
# ==============================================================================
# Q28_nested_student_details.py

num_students = int(input("Enter the number of students: "))
student_database = {}

for i in range(num_students):
    print(f"\nEnter details for Student {i + 1}:")
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Name: ").strip()
    marks = float(input("Enter Marks: "))

    student_database[roll] = {
        "Name": name,
        "Roll": roll,
        "Marks": marks
    }

print("\n--- Student Database (Nested Dictionary) ---")
for roll, info in student_database.items():
    print(f"Roll: {roll} -> Name: {info['Name']}, Marks: {info['Marks']}")


# ==============================================================================
# Q29: Find common keys between two dictionaries.
# ==============================================================================
# Q29_common_keys.py

n1 = int(input("Enter number of entries in Dictionary 1: "))
dict1 = {}
for _ in range(n1):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    dict1[k] = v

n2 = int(input("Enter number of entries in Dictionary 2: "))
dict2 = {}
for _ in range(n2):
    k = input("Enter key: ").strip()
    v = input("Enter value: ").strip()
    dict2[k] = v

common_keys = []

# Find common keys without using set() intersection
for k in dict1:
    if k in dict2:
        common_keys.append(k)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Common keys:", common_keys)


# ==============================================================================
# Q30: Create a dictionary from a string with characters as keys and frequency as values.
# ==============================================================================
# Q30_char_freq_from_string.py

input_string = input("Enter a string: ")

char_dict = {}

for ch in input_string:
    if ch in char_dict:
        char_dict[ch] += 1
    else:
        char_dict[ch] = 1

print("Generated dictionary of characters and frequencies:")
print(char_dict)

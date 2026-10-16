# ==============================================================================
# Lab Sheet-06: Python Programming Lab – Set Operations
# MCA I Semester (Session 2026-2027)
# COER University, Roorkee
# ==============================================================================


# ==============================================================================
# Q1: Write a Python program to create and display a set.
# ==============================================================================
# Q1_set_creation.py

user_input = input("Enter elements separated by space: ").strip()

# Create a set from user input (automatically removes duplicate entries)
created_set = set(user_input.split()) if user_input else set()

print("Created Set:", created_set)
print("Type:", type(created_set))
print("Number of unique elements in set:", len(created_set))


# ==============================================================================
# Q2: Write a program to create a set with different data types.
# ==============================================================================
# Q2_set_different_data_types.py

# Note: Set elements must be immutable (hashable) data types like int, float, str, bool, tuple
int_val = int(input("Enter an integer: "))
float_val = float(input("Enter a float: "))
str_val = input("Enter a string: ").strip()
bool_val = input("Enter a boolean (True/False): ").strip().lower() == "true"
tuple_val = (101, "immutable_element")

mixed_set = {int_val, float_val, str_val, bool_val, tuple_val}

print("\nMixed Data Type Set:", mixed_set)
print("Elements and their respective types:")
for item in mixed_set:
    print(f"Value: {item} | Type: {type(item).__name__}")


# ==============================================================================
# Q3: Write a program to add a single element to a set.
# ==============================================================================
# Q3_add_single_element.py

user_input = input("Enter initial set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

print("Initial set:", s)
new_element = input("Enter a single element to add: ").strip()

# Add element using add() method
s.add(new_element)

print("Set after adding element:", s)


# ==============================================================================
# Q4: Write a program to add multiple elements to a set.
# ==============================================================================
# Q4_add_multiple_elements.py

user_input = input("Enter initial set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

print("Initial set:", s)
multi_elements = input("Enter multiple elements to add (separated by space): ").strip().split()

# Add multiple elements using update()
s.update(multi_elements)

print("Set after adding multiple elements:", s)


# ==============================================================================
# Q5: Write a program to remove an element from a set using remove().
# ==============================================================================
# Q5_remove_element.py

user_input = input("Enter set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

print("Current set:", s)
element_to_remove = input("Enter element to remove using remove(): ").strip()

# remove() raises KeyError if element does not exist
try:
    s.remove(element_to_remove)
    print(f"Element '{element_to_remove}' removed successfully.")
    print("Updated set:", s)
except KeyError:
    print(f"KeyError: Element '{element_to_remove}' not found in the set.")


# ==============================================================================
# Q6: Write a program to remove an element from a set using discard().
# ==============================================================================
# Q6_discard_element.py

user_input = input("Enter set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

print("Current set:", s)
element_to_discard = input("Enter element to discard using discard(): ").strip()

# discard() does NOT raise an error if the element is not found
s.discard(element_to_discard)

print(f"Attempted to discard '{element_to_discard}'.")
print("Updated set:", s)


# ==============================================================================
# Q7: Write a program to clear all elements from a set.
# ==============================================================================
# Q7_clear_set.py

user_input = input("Enter set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

print("Set before clear():", s)

# Clear all elements using clear()
s.clear()

print("Set after clear():", s)


# ==============================================================================
# Q8: Write a program to check if an element exists in a set.
# ==============================================================================
# Q8_check_element_exists.py

user_input = input("Enter set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

target = input("Enter element to search in set: ").strip()

# Membership testing using 'in' operator
if target in s:
    print(f"Yes, '{target}' exists in the set.")
else:
    print(f"No, '{target}' does NOT exist in the set.")


# ==============================================================================
# Q9: Write a program to find the length of a set.
# ==============================================================================
# Q9_set_length.py

user_input = input("Enter set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

# Calculate length manually using a loop without built-in len()
count = 0
for _ in s:
    count += 1

print("Set:", s)
print("Length of the set (calculated manually):", count)


# ==============================================================================
# Q10: Write a program to iterate through a set and print its elements.
# ==============================================================================
# Q10_iterate_set.py

user_input = input("Enter set elements separated by space: ").strip()
s = set(user_input.split()) if user_input else set()

print("Iterating through set elements:")
for index, item in enumerate(s, start=1):
    print(f"Element {index}: {item}")


# ==============================================================================
# Q11: Write a program to find the union of two sets.
# ==============================================================================
# Q11_set_union.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Union using | operator and union() method
union_set = set_a | set_b

print("Set A:", set_a)
print("Set B:", set_b)
print("Union (A | B):", union_set)


# ==============================================================================
# Q12: Write a program to find the intersection of two sets.
# ==============================================================================
# Q12_set_intersection.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Intersection using & operator
intersection_set = set_a & set_b

print("Set A:", set_a)
print("Set B:", set_b)
print("Intersection (A & B):", intersection_set)


# ==============================================================================
# Q13: Write a program to find the difference of two sets.
# ==============================================================================
# Q13_set_difference.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Difference: Elements in A that are not in B
diff_a_b = set_a - set_b
diff_b_a = set_b - set_a

print("Set A:", set_a)
print("Set B:", set_b)
print("Difference (A - B):", diff_a_b)
print("Difference (B - A):", diff_b_a)


# ==============================================================================
# Q14: Write a program to find the symmetric difference of two sets.
# ==============================================================================
# Q14_symmetric_difference.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Symmetric difference: Elements in either A or B, but not in both
sym_diff = set_a ^ set_b

print("Set A:", set_a)
print("Set B:", set_b)
print("Symmetric Difference (A ^ B):", sym_diff)


# ==============================================================================
# Q15: Write a program to check if a set is a subset of another set.
# ==============================================================================
# Q15_check_subset.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Check subset condition manually and with issubset()
is_subset = set_a.issubset(set_b)

print("Set A:", set_a)
print("Set B:", set_b)

if is_subset:
    print("Set A is a subset of Set B (A <= B).")
else:
    print("Set A is NOT a subset of Set B.")


# ==============================================================================
# Q16: Write a program to check if a set is a superset of another set.
# ==============================================================================
# Q16_check_superset.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Check superset condition using issuperset()
is_superset = set_a.issuperset(set_b)

print("Set A:", set_a)
print("Set B:", set_b)

if is_superset:
    print("Set A is a superset of Set B (A >= B).")
else:
    print("Set A is NOT a superset of Set B.")


# ==============================================================================
# Q17: Write a program to check if two sets are disjoint.
# ==============================================================================
# Q17_check_disjoint.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Disjoint sets have no elements in common
if set_a.isdisjoint(set_b):
    print("Set A and Set B are disjoint (no common elements).")
else:
    print("Set A and Set B are NOT disjoint (they share elements):", set_a & set_b)


# ==============================================================================
# Q18: Write a program to remove all elements of one set from another set.
# ==============================================================================
# Q18_remove_elements_of_one_set.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

print("Set A before removal:", set_a)
print("Set B (elements to remove):", set_b)

# In-place removal of elements of Set B from Set A
set_a.difference_update(set_b)

print("Set A after removing all elements of Set B:", set_a)


# ==============================================================================
# Q19: Write a program to create the power set of a given set.
# ==============================================================================
# Q19_power_set.py

user_input = input("Enter elements for set separated by space (keep small, e.g. 1 2 3): ").strip()
s = set(user_input.split()) if user_input else set()

# Power set: set of all subsets
power_set = [set()]

for element in s:
    new_subsets = [subset | {element} for subset in power_set]
    power_set.extend(new_subsets)

print("Original Set:", s)
print(f"Total number of subsets in Power Set (2^n): {len(power_set)}")
print("Power Set:")
for subset in power_set:
    print(subset)


# ==============================================================================
# Q20: Write a program to find the Cartesian product of two sets.
# ==============================================================================
# Q20_cartesian_product.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

# Cartesian Product A x B = {(a, b) for a in A, b in B}
cartesian_product = {(a, b) for a in set_a for b in set_b}

print("Set A:", set_a)
print("Set B:", set_b)
print(f"Cartesian Product (A x B) with {len(cartesian_product)} ordered pairs:")
print(cartesian_product)


# ==============================================================================
# Q21: Write a program to count distinct elements from a list using a set.
# ==============================================================================
# Q21_count_distinct_elements.py

user_input = input("Enter list elements separated by space (duplicates allowed): ").strip()
input_list = user_input.split() if user_input else []

# Distinct elements represented by a set
distinct_elements_set = set(input_list)
distinct_count = len(distinct_elements_set)

print("Original List:", input_list)
print("Distinct Elements Set:", distinct_elements_set)
print("Total number of distinct elements:", distinct_count)


# ==============================================================================
# Q22: Write a program to find duplicate elements in a list using a set.
# ==============================================================================
# Q22_find_duplicate_elements.py

user_input = input("Enter list elements separated by space: ").strip()
input_list = user_input.split() if user_input else []

seen = set()
duplicates = set()

# Detect duplicate elements using set membership
for item in input_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Original List:", input_list)
if duplicates:
    print("Duplicate elements found in list:", duplicates)
else:
    print("No duplicate elements found.")


# ==============================================================================
# Q23: Write a program to remove duplicates from a list using a set.
# ==============================================================================
# Q23_remove_duplicates_list.py

user_input = input("Enter list elements separated by space: ").strip()
input_list = user_input.split() if user_input else []

# Removing duplicates using set conversion
unique_list = list(set(input_list))

print("Original List (with duplicates):", input_list)
print("List after removing duplicates:", unique_list)


# ==============================================================================
# Q24: Write a program to convert a string into a set of characters.
# ==============================================================================
# Q24_string_to_char_set.py

user_string = input("Enter a string: ")

# Convert string into a set of unique characters
char_set = set(user_string)

print("Original String:", user_string)
print("Set of characters:", char_set)
print("Number of unique characters:", len(char_set))


# ==============================================================================
# Q25: Write a program to find common letters in two strings using sets.
# ==============================================================================
# Q25_common_letters_strings.py

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Exclude spaces and convert to sets
set1 = set(str1.replace(" ", "").lower())
set2 = set(str2.replace(" ", "").lower())

# Intersection gives common letters
common_letters = set1 & set2

print("Letters in String 1:", set1)
print("Letters in String 2:", set2)
print("Common letters:", common_letters)


# ==============================================================================
# Q26: Write a program to find unique words in a sentence using a set.
# ==============================================================================
# Q26_unique_words_sentence.py

sentence = input("Enter a sentence: ").strip()

punctuation = ".,!?;:'\"()[]{}"
words = sentence.split()

# Strip punctuation and convert to lowercase unique words
unique_words = set()
for word in words:
    cleaned = word.strip(punctuation).lower()
    if cleaned:
        unique_words.add(cleaned)

print("Original Sentence:", sentence)
print("Unique words set:", unique_words)
print("Total number of unique words:", len(unique_words))


# ==============================================================================
# Q27: Write a program to check if two strings are anagrams using sets.
# ==============================================================================
# Q27_anagram_check_using_sets.py

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Clean strings: remove spaces and convert to lowercase
s1_clean = str1.replace(" ", "").lower()
s2_clean = str2.replace(" ", "").lower()

# Check 1: Unique characters universe must be identical
set1 = set(s1_clean)
set2 = set(s2_clean)

# Check 2: Lengths and individual character frequencies must match
if set1 != set2 or len(s1_clean) != len(s2_clean):
    print("Result: The strings are NOT anagrams.")
else:
    is_anagram = True
    for ch in set1:
        if s1_clean.count(ch) != s2_clean.count(ch):
            is_anagram = False
            break

    if is_anagram:
        print(f"Result: '{str1}' and '{str2}' are anagrams!")
    else:
        print("Result: The strings are NOT anagrams.")


# ==============================================================================
# Q28: Write a program to create a frozen set and demonstrate its properties.
# ==============================================================================
# Q28_frozenset_properties.py

user_input = input("Enter elements for frozenset separated by space: ").strip()
fs = frozenset(user_input.split()) if user_input else frozenset()

print("Created FrozenSet:", fs)
print("Type:", type(fs))

# Property 1: Immutability (Attempting to add or remove raises an AttributeError)
try:
    fs.add("test_element")
except AttributeError as e:
    print("Property 1 (Immutability): frozenset cannot be modified ->", e)

# Property 2: Hashability (Can be used as a key in a dictionary or element of another set)
dict_with_frozenset_key = {fs: "Allowed because frozenset is hashable"}
print("Property 2 (Hashability): Used as dictionary key successfully:")
print(dict_with_frozenset_key)

# Property 3: Read-only set operations
other_set = {"a", "b", "c"}
print("Union with other set:", fs | other_set)


# ==============================================================================
# Q29: Write a program to find maximum and minimum values in a set.
# ==============================================================================
# Q29_max_min_in_set.py

user_input = input("Enter numbers separated by space: ").strip()

if not user_input:
    print("Set is empty.")
else:
    num_set = {float(x) for x in user_input.split()}
    print("Numbers Set:", num_set)

    # Find max and min manually without using built-in max() or min()
    iterator = iter(num_set)
    first_val = next(iterator)
    max_val = first_val
    min_val = first_val

    for val in iterator:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val

    print("Maximum Value in Set:", max_val)
    print("Minimum Value in Set:", min_val)


# ==============================================================================
# Q30: Write a program to perform all basic set operations (union, intersection, difference, symmetric difference) in one program.
# ==============================================================================
# Q30_all_basic_set_operations.py

input1 = input("Enter elements for Set A separated by space: ").strip()
input2 = input("Enter elements for Set B separated by space: ").strip()

set_a = set(input1.split()) if input1 else set()
set_b = set(input2.split()) if input2 else set()

print("\n================== SET OPERATIONS SUMMARY ==================")
print("Set A:", set_a)
print("Set B:", set_b)
print("------------------------------------------------------------")
print("1. Union (A | B)                 :", set_a | set_b)
print("2. Intersection (A & B)          :", set_a & set_b)
print("3. Difference (A - B)            :", set_a - set_b)
print("4. Difference (B - A)            :", set_b - set_a)
print("5. Symmetric Difference (A ^ B)  :", set_a ^ set_b)
print("6. Is A Subset of B? (A <= B)    :", set_a.issubset(set_b))
print("7. Is A Superset of B? (A >= B)  :", set_a.issuperset(set_b))
print("8. Are A and B Disjoint?         :", set_a.isdisjoint(set_b))
print("============================================================")

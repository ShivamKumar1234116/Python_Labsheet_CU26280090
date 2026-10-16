# Q1_palindrome.py

s = input("Enter a string: ")

reverse = ""

# Reverse the string without slicing
for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]

if s == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Q2_vowels_consonants.py

s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

# Q3_replace_spaces.py

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == " ":
        result += "_"
    else:
        result += ch

print("Result:", result)


# Q4_uppercase.py

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isupper():
        result += ch

print("Uppercase characters:", result)


# Q5_remove_duplicates.py

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)


# Q6_character_frequency.py

s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:")

for ch in frequency:
    print(ch, ":", frequency[ch])

# Q7_reverse_string.py

s = input("Enter a string: ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

print("Reversed string:", reverse)


# Q8_title_case.py

s = input("Enter a string: ")

result = ""
new_word = True

for ch in s:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            result += ch.upper()
            new_word = False
        else:
            result += ch.lower()

print("Title case:", result)


# Q9_count_words.py

s = input("Enter a string: ")

count = 0
inside_word = False

for ch in s:
    if ch != " " and not inside_word:
        count += 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Number of words:", count)

# Q9_count_words.py

s = input("Enter a string: ")

count = 0
inside_word = False

for ch in s:
    if ch != " " and not inside_word:
        count += 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Number of words:", count)


# Q10_longest_word.py

s = input("Enter a sentence: ")

words = s.split()

if len(words) == 0:
    print("No words found.")
else:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)


# Q11_anagram.py

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Strings are not anagrams.")
else:
    frequency = {}
    
    for ch in s1:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    is_anagram = True

    for ch in s2:
        if ch not in frequency:
            is_anagram = False
            break
        frequency[ch] -= 1

        if frequency[ch] < 0:
            is_anagram = False
            break

    if is_anagram:
        print("Strings are anagrams.")
    else:
        print("Strings are not anagrams.")


# Q12_substring.py

s = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub in s:
    print("Substring exists in the string.")
else:
    print("Substring does not exist.")


# Q13_vowels_uppercase.py

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            result += ch.upper()
        else:
            result += ch.lower()
    else:
        result += ch

print("Result:", result)


# Q14_remove_punctuation.py

s = input("Enter a string: ")

punctuation = ".,!?;:'\"-()[]{}<>/@#$%^&*_+=|\\"

result = ""

for ch in s:
    if ch not in punctuation:
        result += ch

print("After removing punctuation:", result)


# Q15_first_non_repeated.py

s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

found = False

for ch in s:
    if frequency[ch] == 1:
        print("First non-repeated character:", ch)
        found = True
        break

if not found:
    print("No non-repeated character found.")



# Q16_count_characters.py

s = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special characters:", special)


# Q17_substrings.py

s = input("Enter a string: ")

print("All substrings:")

for i in range(len(s)):
    substring = ""

    for j in range(i, len(s)):
        substring += s[j]
        print(substring)

# Q18_sort_characters.py

s = input("Enter a string: ")

characters = []

for ch in s:
    characters.append(ch)

# Bubble sort
for i in range(len(characters)):
    for j in range(0, len(characters) - i - 1):
        if characters[j] > characters[j + 1]:
            temp = characters[j]
            characters[j] = characters[j + 1]
            characters[j + 1] = temp

result = ""

for ch in characters:
    result += ch

print("Sorted string:", result)


# Q19_most_repeated_word.py

s = input("Enter a sentence: ")

words = s.split()
frequency = {}

for word in words:
    word = word.lower()

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

if len(frequency) == 0:
    print("No words found.")
else:
    most_repeated = ""
    max_count = 0

    for word in frequency:
        if frequency[word] > max_count:
            max_count = frequency[word]
            most_repeated = word

    print("Most repeated word:", most_repeated)
    print("Frequency:", max_count)

# Q20_string_rotation.py

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Strings are not rotations.")
else:
    combined = s1 + s1

    if s2 in combined:
        print("Strings are rotations of each other.")
    else:
        print("Strings are not rotations.")

# Q21_largest_smallest.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty.")
else:
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    print("Largest element:", largest)
    print("Smallest element:", smallest)


# Q22_sort_list.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Ascending order using bubble sort
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Ascending order:", numbers)

# Descending order
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Descending order:", numbers)


# Q23_remove_duplicates.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)


# Q24_reverse_list.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

left = 0
right = len(numbers) - 1

while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

    left += 1
    right -= 1

print("Reversed list:", numbers)

# Q25_list_frequency.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of each element:")

for num in frequency:
    print(num, ":", frequency[num])


# Q26_merge_lists.py

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged = []

for num in list1:
    merged.append(num)

for num in list2:
    merged.append(num)

print("Merged list:", merged)

# Q27_second_largest.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = None
second_largest = None

for num in numbers:

    if largest is None or num > largest:
        second_largest = largest
        largest = num

    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

if second_largest is None:
    print("Second largest element does not exist.")
else:
    print("Second largest element:", second_largest)


# Q28_common_elements.py

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)


# Q29_list_difference.py

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

difference = []

for num in list1:
    if num not in list2:
        difference.append(num)

print("Difference between lists:", difference)


# Q30_even_odd.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)
# ==============================================================================
# Lab Sheet-07: Python Programming Lab – File Handling – Read and Write Operations Using Python Programming
# MCA I Semester (Session 2026-2027)
# COER University, Roorkee
# ==============================================================================

import csv
import os
import string


# ==============================================================================
# Q1: Write a Python program to create and write text into a file.
# ==============================================================================
# Q1_create_and_write_file.py

filename = input("Enter file name to create (press Enter for 'sample.txt'): ").strip() or "sample.txt"
default_text = (
    "Python is a high-level, interpreted programming language.\n"
    "It emphasizes code readability with clean and expressive syntax.\n"
    "File handling in Python allows creating, reading, updating, and deleting files.\n"
    "Working with files is a fundamental skill in software development.\n"
    "COER University MCA Python Programming Lab Session 2026-2027."
)

prompt_msg = f"Enter text to write into '{filename}' (press Enter for default text): "
text_to_write = input(prompt_msg).strip() or default_text

try:
    # Open the file in write mode ('w') which creates the file or overwrites if existing
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text_to_write)
    print(f"Success: File '{filename}' created and written successfully.")
    print(f"Total characters written: {len(text_to_write)}")
except IOError as err:
    print(f"IOError: An error occurred while writing to file '{filename}': {err}")


# ==============================================================================
# Q2: Write a program to read the entire content of a text file.
# ==============================================================================
# Q2_read_entire_file.py

filename = input("\nEnter file name to read (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    # Open the file in read mode ('r') using 'with' statement for automatic closing
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(f"\n--- Entire Content of '{filename}' ---")
    print(content)
    print("---------------------------------------")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as err:
    print(f"IOError: Could not read file '{filename}': {err}")


# ==============================================================================
# Q3: Write a program to read a file line by line.
# ==============================================================================
# Q3_read_file_line_by_line.py

filename = input("\nEnter file name to read line-by-line (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    # Iterating directly over the file object reads lazily and memory-efficiently
    with open(filename, "r", encoding="utf-8") as file:
        print(f"\n--- Reading '{filename}' Line by Line ---")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.rstrip()}")
            line_number += 1
    print(f"Total lines read: {line_number - 1}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as err:
    print(f"IOError: Could not read file '{filename}': {err}")


# ==============================================================================
# Q4: Write a program to count the number of words in a text file.
# ==============================================================================
# Q4_count_words_in_file.py

filename = input("\nEnter file name to count words (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        # split() splits the content by any whitespace (spaces, tabs, newlines)
        words = content.split()
        word_count = len(words)
    print(f"File '{filename}' contains {word_count} word(s).")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as err:
    print(f"IOError: Could not read file '{filename}': {err}")


# ==============================================================================
# Q5: Write a program to count the number of lines and characters in a file.
# ==============================================================================
# Q5_count_lines_and_characters.py

filename = input("\nEnter file name to count lines and characters (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)
    # Characters including whitespaces and newlines
    total_chars = sum(len(line) for line in lines)
    # Characters excluding whitespace
    non_space_chars = sum(len(char) for line in lines for char in line if not char.isspace())

    print(f"--- File Statistics for '{filename}' ---")
    print(f"Number of Lines              : {line_count}")
    print(f"Total Characters (with spaces): {total_chars}")
    print(f"Characters (without spaces)  : {non_space_chars}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as err:
    print(f"IOError: Could not read file '{filename}': {err}")


# ==============================================================================
# Q6: Write a program to display only even-numbered lines from a file.
# ==============================================================================
# Q6_display_even_numbered_lines.py

filename = input("\nEnter file name to display even lines (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        print(f"\n--- Even-Numbered Lines from '{filename}' ---")
        even_found = False
        # enumerate starting at 1 for 1-based line indexing
        for line_num, line in enumerate(file, start=1):
            if line_num % 2 == 0:
                print(f"[Line {line_num}]: {line.rstrip()}")
                even_found = True
        if not even_found:
            print("No even-numbered lines found.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as err:
    print(f"IOError: Could not read file '{filename}': {err}")


# ==============================================================================
# Q7: Write a program to write multiple lines of input from the user into a file.
# ==============================================================================
# Q7_write_multiple_lines.py

filename = input("\nEnter file name to save multiple lines (press Enter for 'multiline_sample.txt'): ").strip() or "multiline_sample.txt"
num_lines_input = input("Enter number of lines to write (press Enter for 3 sample lines): ").strip()

lines_to_write = []
if not num_lines_input:
    lines_to_write = [
        "First line: MCA First Semester at COER University.\n",
        "Second line: Mastering File Operations in Python.\n",
        "Third line: Python provides robust I/O capabilities.\n",
    ]
else:
    try:
        count = int(num_lines_input)
        print(f"Please enter {count} line(s) below:")
        for idx in range(1, count + 1):
            line = input(f"Line {idx}: ")
            lines_to_write.append(line + "\n")
    except ValueError:
        print("Invalid number entered; using default sample lines instead.")
        lines_to_write = [
            "Default line 1: Automated multiline record.\n",
            "Default line 2: Python file input output.\n"
        ]

try:
    with open(filename, "w", encoding="utf-8") as file:
        # writelines writes an iterable of strings to the file
        file.writelines(lines_to_write)
    print(f"Success: Wrote {len(lines_to_write)} line(s) to '{filename}'.")
except IOError as err:
    print(f"IOError: Could not write multiple lines to '{filename}': {err}")


# ==============================================================================
# Q8: Write a program to append new content to an existing file.
# ==============================================================================
# Q8_append_content_to_file.py

filename = input("\nEnter file name to append to (press Enter for 'sample.txt'): ").strip() or "sample.txt"
default_append = "Appended Line: Python file handling allows easy appending using mode 'a'."
text_to_append = input(f"Enter text to append (press Enter for default): ").strip() or default_append

try:
    # Open in 'a' mode: cursor moves to the end of file without truncating
    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n" + text_to_append)
    print(f"Success: Content appended successfully to '{filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as err:
    print(f"IOError: Could not append to file '{filename}': {err}")


# ==============================================================================
# Q9: Write a program to copy the contents of one file into another.
# ==============================================================================
# Q9_copy_file_contents.py

src_file = input("\nEnter source file to copy (press Enter for 'sample.txt'): ").strip() or "sample.txt"
dest_file = input("Enter destination file name (press Enter for 'sample_copy.txt'): ").strip() or "sample_copy.txt"

try:
    with open(src_file, "r", encoding="utf-8") as source:
        content = source.read()

    with open(dest_file, "w", encoding="utf-8") as destination:
        destination.write(content)

    print(f"Success: Contents of '{src_file}' copied to '{dest_file}'.")
    print(f"Total characters copied: {len(content)}")
except FileNotFoundError:
    print(f"Error: Source file '{src_file}' does not exist.")
except IOError as err:
    print(f"IOError: Could not copy file: {err}")


# ==============================================================================
# Q10: Write a program to read a file and convert its content to uppercase.
# ==============================================================================
# Q10_convert_file_content_to_uppercase.py

filename = input("\nEnter file name to convert to uppercase (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    upper_content = content.upper()

    print(f"\n--- Content of '{filename}' in Uppercase ---")
    print(upper_content)
    print("---------------------------------------------")

    # Optionally write to uppercase file
    upper_filename = "sample_uppercase.txt"
    with open(upper_filename, "w", encoding="utf-8") as upper_file:
        upper_file.write(upper_content)
    print(f"Saved uppercase content to '{upper_filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as err:
    print(f"IOError: Could not read/write file: {err}")


# ==============================================================================
# Q11: Write a program to search for a particular word in a file.
# ==============================================================================
# Q11_search_word_in_file.py

filename = input("\nEnter file name to search in (press Enter for 'sample.txt'): ").strip() or "sample.txt"
search_word = input("Enter the word to search for (press Enter for 'Python'): ").strip() or "Python"

try:
    with open(filename, "r", encoding="utf-8") as file:
        matching_lines = []
        for line_num, line in enumerate(file, start=1):
            # Check case-insensitively
            if search_word.lower() in line.lower():
                matching_lines.append((line_num, line.strip()))

    if matching_lines:
        print(f"Found '{search_word}' in {len(matching_lines)} line(s):")
        for num, text in matching_lines:
            print(f"  Line {num}: {text}")
    else:
        print(f"Word '{search_word}' was not found in '{filename}'.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q12: Write a program to count the occurrence of a specific word in a file.
# ==============================================================================
# Q12_count_word_occurrence.py

filename = input("\nEnter file name (press Enter for 'sample.txt'): ").strip() or "sample.txt"
target_word = input("Enter word to count occurrences of (press Enter for 'Python'): ").strip() or "Python"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        # Clean punctuation to ensure accurate word tokenization
        translator = str.maketrans("", "", string.punctuation)
        cleaned_words = [w.translate(translator).lower() for w in content.split()]
        count = cleaned_words.count(target_word.lower())

    print(f"The word '{target_word}' occurs {count} time(s) in '{filename}'.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q13: Write a program to read numbers from a file and display their sum and average.
# ==============================================================================
# Q13_read_numbers_sum_average.py

num_filename = input("\nEnter numbers file name (press Enter for 'numbers.txt'): ").strip() or "numbers.txt"

# If the file does not exist, create it with sample numbers
if not os.path.exists(num_filename):
    with open(num_filename, "w", encoding="utf-8") as nf:
        nf.write("10 25.5 34 40.5 50 65 75 80\n")
    print(f"Created sample numbers file '{num_filename}' with initial values.")

try:
    with open(num_filename, "r", encoding="utf-8") as file:
        content = file.read()
        tokens = content.replace(",", " ").split()
        numbers = [float(x) for x in tokens]

    if numbers:
        total_sum = sum(numbers)
        avg = total_sum / len(numbers)
        print(f"Numbers read: {numbers}")
        print(f"Total count : {len(numbers)}")
        print(f"Sum         : {total_sum:.2f}")
        print(f"Average     : {avg:.2f}")
    else:
        print(f"File '{num_filename}' contains no numbers.")
except FileNotFoundError:
    print(f"Error: File '{num_filename}' not found.")
except ValueError as err:
    print(f"ValueError: Could not parse non-numeric token as number: {err}")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q14: Write a program to display the longest line in a file.
# ==============================================================================
# Q14_longest_line_in_file.py

filename = input("\nEnter file name to find longest line (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print(f"File '{filename}' is empty.")
    else:
        # Strip trailing newlines when evaluating length
        longest_index = 0
        max_length = -1
        for idx, line in enumerate(lines):
            clean_line = line.rstrip("\r\n")
            if len(clean_line) > max_length:
                max_length = len(clean_line)
                longest_index = idx

        print(f"\n--- Longest Line in '{filename}' ---")
        print(f"Line Number : {longest_index + 1}")
        print(f"Length      : {max_length} characters")
        print(f"Content     : {lines[longest_index].rstrip()}")
        print("---------------------------------------")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q15: Write a program to replace a word in a file with another word.
# ==============================================================================
# Q15_replace_word_in_file.py

filename = input("\nEnter file name (press Enter for 'sample.txt'): ").strip() or "sample.txt"
old_word = input("Enter word to replace (press Enter for 'Python'): ").strip() or "Python"
new_word = input(f"Enter replacement for '{old_word}' (press Enter for 'Python 3'): ").strip() or "Python 3"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    occurrences = content.count(old_word)
    if occurrences == 0:
        print(f"Word '{old_word}' was not found in '{filename}'. No replacements made.")
    else:
        updated_content = content.replace(old_word, new_word)
        out_filename = "sample_replaced.txt"
        with open(out_filename, "w", encoding="utf-8") as out_file:
            out_file.write(updated_content)
        print(f"Success: Replaced {occurrences} occurrence(s) of '{old_word}' with '{new_word}'.")
        print(f"Saved modified content to '{out_filename}'.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q16: Write a program to display the first and last lines of a file.
# ==============================================================================
# Q16_first_and_last_lines.py

filename = input("\nEnter file name (press Enter for 'sample.txt'): ").strip() or "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print(f"File '{filename}' is empty.")
    else:
        first_line = lines[0].rstrip("\r\n")
        last_line = lines[-1].rstrip("\r\n")
        print(f"\n--- First and Last Lines of '{filename}' ---")
        print(f"First Line (Line 1)         : {first_line}")
        print(f"Last Line  (Line {len(lines)})        : {last_line}")
        print("---------------------------------------------")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q17: Write a program to remove blank lines from a file.
# ==============================================================================
# Q17_remove_blank_lines.py

filename = input("\nEnter file name (press Enter for 'sample.txt'): ").strip() or "sample.txt"
clean_filename = "sample_no_blank_lines.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Filter out empty or whitespace-only lines
    non_blank_lines = [line for line in lines if line.strip() != ""]
    removed_count = len(lines) - len(non_blank_lines)

    with open(clean_filename, "w", encoding="utf-8") as file:
        file.writelines(non_blank_lines)

    print(f"Success: Removed {removed_count} blank line(s).")
    print(f"Kept {len(non_blank_lines)} non-blank line(s) in '{clean_filename}'.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q18: Write a program to read a file and store only unique words into another file.
# ==============================================================================
# Q18_store_unique_words.py

src_filename = input("\nEnter source file name (press Enter for 'sample.txt'): ").strip() or "sample.txt"
dest_filename = "unique_words.txt"

try:
    with open(src_filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Clean punctuation and normalize to lowercase
    translator = str.maketrans("", "", string.punctuation)
    words = [w.translate(translator).lower() for w in content.split()]
    unique_words = sorted(set(w for w in words if w))

    with open(dest_filename, "w", encoding="utf-8") as file:
        for word in unique_words:
            file.write(word + "\n")

    print(f"Success: Stored {len(unique_words)} unique word(s) into '{dest_filename}'.")
    print("Sample unique words:", unique_words[:10])
except FileNotFoundError:
    print(f"Error: File '{src_filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q19: Write a program to sort all words in a file alphabetically and save to a new file.
# ==============================================================================
# Q19_sort_words_alphabetically.py

src_filename = input("\nEnter source file name (press Enter for 'sample.txt'): ").strip() or "sample.txt"
dest_filename = "sorted_words.txt"

try:
    with open(src_filename, "r", encoding="utf-8") as file:
        content = file.read()

    translator = str.maketrans("", "", string.punctuation)
    words = [w.translate(translator) for w in content.split() if w.translate(translator)]
    # Sort alphabetically in a case-insensitive manner
    sorted_words = sorted(words, key=str.casefold)

    with open(dest_filename, "w", encoding="utf-8") as file:
        for word in sorted_words:
            file.write(word + "\n")

    print(f"Success: Saved {len(sorted_words)} sorted word(s) into '{dest_filename}'.")
    print("First 10 sorted words:", sorted_words[:10])
except FileNotFoundError:
    print(f"Error: File '{src_filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q20: Write a program to merge two text files into a third file.
# ==============================================================================
# Q20_merge_two_files.py

file1_name = "file1.txt"
file2_name = "file2.txt"
merged_name = "merged.txt"

# Ensure both sample files exist
if not os.path.exists(file1_name):
    with open(file1_name, "w", encoding="utf-8") as f1:
        f1.write("=== Part 1: COER University ===\nMaster of Computer Applications (MCA) Program.\n")
if not os.path.exists(file2_name):
    with open(file2_name, "w", encoding="utf-8") as f2:
        f2.write("=== Part 2: Python Lab ===\nFile Handling - Read and Write Operations.\n")

try:
    with open(file1_name, "r", encoding="utf-8") as f1, open(file2_name, "r", encoding="utf-8") as f2:
        data1 = f1.read()
        data2 = f2.read()

    with open(merged_name, "w", encoding="utf-8") as out:
        out.write(data1.rstrip() + "\n\n" + data2)

    print(f"Success: Merged '{file1_name}' and '{file2_name}' into '{merged_name}'.")
    with open(merged_name, "r", encoding="utf-8") as mf:
        print(f"\n--- Contents of '{merged_name}' ---")
        print(mf.read())
        print("-----------------------------------")
except IOError as err:
    print(f"IOError: Could not merge files: {err}")


# ==============================================================================
# Q21: Write a Python program to create and write data into a CSV file.
# ==============================================================================
# Q21_create_and_write_csv.py

csv_filename = input("\nEnter CSV file name (press Enter for 'students.csv'): ").strip() or "students.csv"

# Sample student dataset
student_records = [
    ["Roll_No", "Name", "Department", "Marks"],
    [101, "Shivam Kumar", "MCA", 88.5],
    [102, "Aarav Sharma", "MCA", 92.0],
    [103, "Priya Singh", "MCA", 85.0],
    [104, "Rohan Verma", "MCA", 78.5],
    [105, "Neha Patel", "MCA", 95.5]
]

try:
    # newline='' prevents extra blank rows across different operating systems
    with open(csv_filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(student_records)
    print(f"Success: CSV file '{csv_filename}' created with {len(student_records)-1} student record(s).")
except IOError as err:
    print(f"IOError: Could not write CSV file '{csv_filename}': {err}")


# ==============================================================================
# Q22: Write a program to read data from a CSV file and display it.
# ==============================================================================
# Q22_read_and_display_csv.py

csv_filename = input("\nEnter CSV file name to read (press Enter for 'students.csv'): ").strip() or "students.csv"

try:
    with open(csv_filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        print(f"\n--- Data from '{csv_filename}' ---")
        for row in reader:
            # Print each row formatted nicely
            print(f"{row[0]:<10} {row[1]:<18} {row[2]:<12} {row[3]:<8}")
        print("---------------------------------------------")
except FileNotFoundError:
    print(f"Error: CSV file '{csv_filename}' not found.")
except IOError as err:
    print(f"IOError: Could not read CSV file: {err}")


# ==============================================================================
# Q23: Write a program to read a CSV file and calculate the average of numeric columns.
# ==============================================================================
# Q23_csv_numeric_column_average.py

csv_filename = input("\nEnter CSV file name (press Enter for 'students.csv'): ").strip() or "students.csv"

try:
    with open(csv_filename, "r", newline="", encoding="utf-8") as file:
        dict_reader = csv.DictReader(file)
        marks_list = []
        for row in dict_reader:
            try:
                marks_list.append(float(row["Marks"]))
            except (ValueError, KeyError):
                continue

    if marks_list:
        avg_marks = sum(marks_list) / len(marks_list)
        print(f"Marks Column Analysis for '{csv_filename}':")
        print(f"  Count   : {len(marks_list)}")
        print(f"  Total   : {sum(marks_list):.2f}")
        print(f"  Average : {avg_marks:.2f}")
    else:
        print(f"No numeric marks data found in '{csv_filename}'.")
except FileNotFoundError:
    print(f"Error: CSV file '{csv_filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q24: Write a program to count the number of rows and columns in a CSV file.
# ==============================================================================
# Q24_count_rows_and_columns_csv.py

csv_filename = input("\nEnter CSV file name (press Enter for 'students.csv'): ").strip() or "students.csv"

try:
    with open(csv_filename, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    total_rows = len(rows)
    data_rows = max(0, total_rows - 1)  # Excluding header row
    col_count = len(rows[0]) if total_rows > 0 else 0

    print(f"--- Dimension of CSV File '{csv_filename}' ---")
    print(f"Total Rows (including header): {total_rows}")
    print(f"Data Rows  (excluding header): {data_rows}")
    print(f"Total Columns                : {col_count}")
except FileNotFoundError:
    print(f"Error: CSV file '{csv_filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q25: Write a program to append a new record to an existing CSV file.
# ==============================================================================
# Q25_append_record_to_csv.py

csv_filename = input("\nEnter CSV file name to append to (press Enter for 'students.csv'): ").strip() or "students.csv"
roll_input = input("Enter Roll No (press Enter for '106'): ").strip() or "106"
name_input = input("Enter Student Name (press Enter for 'Kunal Mehta'): ").strip() or "Kunal Mehta"
dept_input = input("Enter Department (press Enter for 'MCA'): ").strip() or "MCA"
marks_input = input("Enter Marks (press Enter for '91.0'): ").strip() or "91.0"

new_record = [roll_input, name_input, dept_input, marks_input]

try:
    with open(csv_filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(new_record)
    print(f"Success: Record {new_record} appended to '{csv_filename}'.")
except FileNotFoundError:
    print(f"Error: CSV file '{csv_filename}' not found.")
except IOError as err:
    print(f"IOError: Could not append record: {err}")


# ==============================================================================
# Q26: Write a program to copy data from one CSV file to another.
# ==============================================================================
# Q26_copy_csv_file.py

src_csv = input("\nEnter source CSV file (press Enter for 'students.csv'): ").strip() or "students.csv"
dest_csv = input("Enter destination CSV file (press Enter for 'students_copy.csv'): ").strip() or "students_copy.csv"

try:
    with open(src_csv, "r", newline="", encoding="utf-8") as src, open(dest_csv, "w", newline="", encoding="utf-8") as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst)
        row_count = 0
        for row in reader:
            writer.writerow(row)
            row_count += 1
    print(f"Success: Copied {row_count} row(s) from '{src_csv}' to '{dest_csv}'.")
except FileNotFoundError:
    print(f"Error: Source CSV '{src_csv}' not found.")
except IOError as err:
    print(f"IOError: Could not copy CSV: {err}")


# ==============================================================================
# Q27: Write a program to display specific columns (like Name and Marks) from a CSV file.
# ==============================================================================
# Q27_display_specific_columns_csv.py

csv_filename = input("\nEnter CSV file name (press Enter for 'students.csv'): ").strip() or "students.csv"

try:
    with open(csv_filename, "r", newline="", encoding="utf-8") as file:
        dict_reader = csv.DictReader(file)
        print(f"\n--- Specific Columns (Name, Marks) from '{csv_filename}' ---")
        print(f"{'Student Name':<20} {'Marks':<8}")
        print("-" * 30)
        for row in dict_reader:
            name = row.get("Name", "N/A")
            marks = row.get("Marks", "N/A")
            print(f"{name:<20} {marks:<8}")
        print("-" * 30)
except FileNotFoundError:
    print(f"Error: CSV file '{csv_filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q28: Write a program to find and display the highest marks from a CSV file.
# ==============================================================================
# Q28_highest_marks_in_csv.py

csv_filename = input("\nEnter CSV file name (press Enter for 'students.csv'): ").strip() or "students.csv"

try:
    with open(csv_filename, "r", newline="", encoding="utf-8") as file:
        dict_reader = csv.DictReader(file)
        top_student = None
        max_marks = float("-inf")

        for row in dict_reader:
            try:
                marks = float(row["Marks"])
                if marks > max_marks:
                    max_marks = marks
                    top_student = row
            except (ValueError, KeyError):
                continue

    if top_student:
        print(f"\n--- Highest Marks in '{csv_filename}' ---")
        print(f"Roll No    : {top_student.get('Roll_No', 'N/A')}")
        print(f"Name       : {top_student.get('Name', 'N/A')}")
        print(f"Department : {top_student.get('Department', 'N/A')}")
        print(f"Marks      : {max_marks}")
        print("------------------------------------------")
    else:
        print(f"No valid marks records found in '{csv_filename}'.")
except FileNotFoundError:
    print(f"Error: CSV file '{csv_filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q29: Write a program to search a record in a CSV file based on student name.
# ==============================================================================
# Q29_search_record_by_name_csv.py

csv_filename = input("\nEnter CSV file name (press Enter for 'students.csv'): ").strip() or "students.csv"
search_name = input("Enter student name to search (press Enter for 'Shivam'): ").strip() or "Shivam"

try:
    with open(csv_filename, "r", newline="", encoding="utf-8") as file:
        dict_reader = csv.DictReader(file)
        found_records = []
        for row in dict_reader:
            if search_name.lower() in row.get("Name", "").lower():
                found_records.append(row)

    if found_records:
        print(f"\nFound {len(found_records)} matching record(s) for '{search_name}':")
        for rec in found_records:
            print(f"  Roll No: {rec.get('Roll_No')}, Name: {rec.get('Name')}, Dept: {rec.get('Department')}, Marks: {rec.get('Marks')}")
    else:
        print(f"No student matching '{search_name}' was found in '{csv_filename}'.")
except FileNotFoundError:
    print(f"Error: CSV file '{csv_filename}' not found.")
except IOError as err:
    print(f"IOError: {err}")


# ==============================================================================
# Q30: Write a program to combine multiple CSV files into one single file.
# ==============================================================================
# Q30_combine_multiple_csv_files.py

batch1_csv = "students_batch1.csv"
batch2_csv = "students_batch2.csv"
combined_csv = "combined_students.csv"

# Prepare two sample batch CSV files if they don't already exist
if not os.path.exists(batch1_csv):
    with open(batch1_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll_No", "Name", "Department", "Marks"])
        writer.writerow([201, "Amit Kumar", "MCA", 82.0])
        writer.writerow([202, "Kavita Rawat", "MCA", 89.5])

if not os.path.exists(batch2_csv):
    with open(batch2_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll_No", "Name", "Department", "Marks"])
        writer.writerow([203, "Deepak Joshi", "MCA", 76.0])
        writer.writerow([204, "Ananya Sen", "MCA", 94.0])

csv_files_to_combine = [batch1_csv, batch2_csv]

try:
    combined_rows = []
    header_written = False

    for file_path in csv_files_to_combine:
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if not header_written and header:
                combined_rows.append(header)
                header_written = True
            for row in reader:
                combined_rows.append(row)

    with open(combined_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(combined_rows)

    print(f"\nSuccess: Combined {len(csv_files_to_combine)} files into '{combined_csv}'.")
    print(f"--- Combined CSV Data ({len(combined_rows)-1} records) ---")
    with open(combined_csv, "r", newline="", encoding="utf-8") as f:
        for line in f:
            print(line.rstrip())
    print("----------------------------------------------------------")
except IOError as err:
    print(f"IOError: Could not combine CSV files: {err}")

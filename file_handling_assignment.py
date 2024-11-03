
    with open("my_file.txt", 'w') as file:
        file.write("This is the first line.\n")
        file.write("The number 123 is on this line.\n")
        file.write("This is the third line with the number 456.\n")

    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("Contents of 'my_file.txt':\n", content)

    with open("my_file.txt", 'a') as file:
        file.write("This is an appended line with text.\n")
        file.write("Here's another appended line with the number 789.\n")
        file.write("The final appended line.\n")

    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("Updated contents of 'my_file.txt':\n", updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
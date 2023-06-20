my_file_path = "non_existent.txt"

try:
    my_file = open(my_file_path)
except OSError:
    print(f"No file: {my_file_path}")
finally:
    print("Resource released")

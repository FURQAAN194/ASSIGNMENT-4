# task2_write_append_file.py

def write_to_file(filename):
    user_input = input("Enter data to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')

def append_to_file(filename):
    extra_input = input("Enter data to append to the file: ")
    with open(filename, 'a') as file:
        file.write(extra_input + '\n')

def read_file(filename):
    print("\nFinal File Content:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    filename = "output.txt"
    write_to_file(filename)
    append_to_file(filename)
    read_file(filename)

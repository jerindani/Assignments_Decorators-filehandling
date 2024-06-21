def check_file():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, 'r') as file:
            print(file_name, " found and opened successfully.")

    except FileNotFoundError:
        print("Error:", file_name, " not found.")

check_file()

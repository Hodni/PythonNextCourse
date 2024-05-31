def ex01():
    # Read all names from 'names.txt' and find the longest name
    with open('names.txt', "r") as file:
        all_names = [name.strip() for name in file]
    # Print the longest name
    print(max(all_names, key=len))


def ex02():
    # Calculate the total length of all names in 'names.txt'
    with open('names.txt', "r") as file:
        total_length = sum(len(name.strip()) for name in file)
    # Print the total length
    print(total_length)


def ex03():
    # Read all names from 'names.txt', sort them by length, and find the shortest names
    with open('names.txt', "r") as file:
        all_names = sorted((name.strip() for name in file), key=len)
        shortest_length = len(all_names[0])
    # Print the names with the shortest length
    print("\n".join(name for name in all_names if len(name) == shortest_length))


def ex04():
    # Read names from 'names.txt' and write their lengths to 'name_length.txt'
    with open('names.txt') as file_to_read:
        name_lengths = [str(len(line.strip())) for line in file_to_read]

    with open('name_length.txt', 'w') as file_to_write:
        file_to_write.write("\n".join(name_lengths))

    # Read and print the contents of 'name_length.txt'
    with open('name_length.txt') as file:
        print(file.read())


def ex05():
    # Prompt the user to enter a name length and print names of that length from 'names.txt'
    name_length = int(input("Enter name length: "))

    with open('names.txt', "r") as file:
        all_names = [name.strip() for name in file]

    # Print names matching the specified length
    print("\n".join(name for name in all_names if len(name) == name_length))


def main():
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()


if __name__ == "__main__":
    main()

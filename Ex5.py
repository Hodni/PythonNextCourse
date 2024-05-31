def check_id_valid(id_number):
    """Check the validity of an Israeli ID number."""
    id_str = str(id_number)
    id_sum = sum(
        int(digit) if index % 2 == 0 else int(digit) * 2 if int(digit) * 2 < 10 else sum(map(int, str(int(digit) * 2)))
        for index, digit in enumerate(id_str[::-1]))
    return id_sum % 10 == 0


class IDIterator:
    """Iterator for generating valid Israeli ID numbers."""

    def __init__(self, id_number):
        self.id_number = id_number + 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if check_id_valid(self.id_number):
                id_number = self.id_number
                self.id_number += 1
                return id_number
            else:
                self.id_number += 1


def id_generator(id_number):
    """Generator function for generating valid Israeli ID numbers."""
    while True:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1


def main():
    id_input = int(input("Enter ID: "))
    mode = input("Generator or Iterator? (gen/it)? ")

    if mode == "it":
        id_iterator = IDIterator(id_input)
        for _ in range(10):
            print(next(id_iterator))
    elif mode == "gen":
        id_gen = id_generator(id_input)
        for _ in range(10):
            print(next(id_gen))
    else:
        print("Invalid mode input. Please enter 'gen' or 'it'.")


if __name__ == "__main__":
    main()

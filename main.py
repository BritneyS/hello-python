from grokkingalgorithms.scripts.binary_search import binary_search


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Python 🐍')

    # Binary search
    print("🔎 Binary search with a sorted list:")
    my_sorted_list = [1, 3, 5, 7, 9]
    print(binary_search(my_sorted_list, 7))  # if item is 7, should return position 3

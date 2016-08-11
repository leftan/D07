# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(list_of_items):
    try: 
        new_list = sorted(list_of_items)
    except:
        print('The list cannot be sorted.')
        return None
    if list_of_items == new_list:
        return True
    else: 
        return False


def main():
    print(is_sorted([1, 242, 232, 2, 253, 34]))
    print(is_sorted([32, 54, 506, ]))
    print(is_sorted(['apple', 'banana', 'cherry', 'fruit', 999]))
    print(is_sorted(['banana', 'apple', 'cherry', 'fruit']))

if __name__ == main():
    main()
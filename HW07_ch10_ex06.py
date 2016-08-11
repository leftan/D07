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
    list_1 = ['apple', 'bear', 'cat']
    list_2 = ['apple', 'bear', 'apples']
    list_3 = [1,2,3]
    list_4 = [1,45,3]
    list_5 = ['APPLE', 'BEAR', 'APPLES']
    list_6 = ['APPLE', 'BEAR', 'CAT']
    print(is_sorted(list_1))  # True
    print(is_sorted(list_2))  # False
    print(is_sorted(list_3))  # True
    print(is_sorted(list_4))  # False
    print(is_sorted(list_5))  # False
    print(is_sorted(list_6))  # True

if __name__ == main():
    main()
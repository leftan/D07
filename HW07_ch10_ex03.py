# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(list_of_int):
    new_list = []
    new_int = 0
    for each_int in list_of_int:
        new_int += int(each_int)
        new_list.append(new_int)
    return new_list

def main():
    list_1 = [1, 2, 3]
    list_2 = [1, 3, 6]
    list_3 = [1]
    list_4 = [0, 0, 0, 1]
    print(cumulative_sum(list_1))  # [1, 3, 6]
    print(cumulative_sum(list_2))  # [1, 4, 10]
    print(cumulative_sum(list_3))  # [1]
    print(cumulative_sum(list_4))  # [0, 0, 0, 1]

if __name__ == '__main__':
    main()
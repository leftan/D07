# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(nested_list):
    capitalized_list = []
    for each_item in nested_list:
        if isinstance(each_item, str):
            capitalized_list.append(str(each_item).capitalize())
        elif isinstance(each_item, list):
            capitalized_list += [capitalize_nested(each_item)]
    return capitalized_list


def main():
    pass


if __name__ == '__main__':
    main()


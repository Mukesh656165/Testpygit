# Welcome to dictionary tricks 2

# how to remove items using pop method

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break
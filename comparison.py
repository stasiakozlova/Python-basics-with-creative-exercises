test_list = [213, 345, 122, 444, 104, 501, 1002, 101]

odd_list = []
even_list = []

for item in test_list:
    if item % 3 != 0:
        if item > max_item:
            max_item = item

print(max_item)

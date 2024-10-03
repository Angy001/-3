I = [1, 4, 1, 6, "hello","a", 5, "hello"]
counter = {}
for elem in I:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)
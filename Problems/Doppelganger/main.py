from collections.abc import Hashable

# the object_list has already been defined


# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
# object_list = [0, 1, 2, 3, 4, 5]

hash_list = []
index = 0
for _ in range(len(object_list)):
    if isinstance(object_list[index], Hashable) and object_list.count(object_list[index]) > 1:
        hash_list.append(object_list[index])
    index += 1

print(len(hash_list))

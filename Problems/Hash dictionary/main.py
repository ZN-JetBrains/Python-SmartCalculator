from collections.abc import Hashable

# objects = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
objects_dict = dict()

for element in objects:
    if isinstance(element, Hashable):
        objects_dict[element] = hash(element)

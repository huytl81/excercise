# NOTE: list, dict, set, bytearray: mutable => unhashable object
# NOTE: tuple, frozenset, str, bytes, int, decimal, float, complex,bool, range: immutable => hashable object

# a frozenset object with many type of elements
x = frozenset({1,2,"a", 3.9})
print(hash(x))
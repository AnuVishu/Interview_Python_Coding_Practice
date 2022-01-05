test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print({elem for val in test_dict.values() for elem in val})

#or
from itertools import chain

print(set(chain(*(test_dict.values()))))

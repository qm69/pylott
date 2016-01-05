a = [1, 2 , 3 , 4, 6, 5, 6, 9, 9]

import collections

for item, count in collections.Counter(a).items():
    if item == 9 and count > 1:
    	print(item, count)

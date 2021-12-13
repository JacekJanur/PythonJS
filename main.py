
#import sys
#sys.path.append('/iterators')

from iterators.ITcityId import ITcityId

print("test-gita")
cityId = ITcityId()
for x in range(10):
    print(cityId.__next__())

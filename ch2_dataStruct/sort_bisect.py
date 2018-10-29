
## 2.7
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits,reverse=True));
print(sorted(fruits,key=len))
print(sorted(fruits,reverse=True,key=len));
fruits.sort();print(sorted(fruits))


## 2.8
import  bisect
import  sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK,needle)
        offset  = position * '  |'
        print(ROW_FMT.format(needle,position,offset))


if __name__ == '__main__':
    if sys.argv[1]  == "left":
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right

    print("Demo,",bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

def grade(score,breakpoints = [60,70,80,90],grades = 'FDCBA'):
    i = bisect.bisect(breakpoints,score)
    return grades[i]

print ([grade(score) for score in [33,99,77,80,89,90,100]])


## 2.8.2
import  bisect
import  random
my_list = []
for i in range(7):
    newitem = random.randrange(20*7)
    bisect.insort(my_list,newitem)
    print("%02d -> " %newitem, my_list)


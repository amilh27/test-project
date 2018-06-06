# A tuple is a heterogeneous immutable data structure in Python

tup1 = (1, 'a')
tup2 = 1, 'a'
tup3 = ()  # Empty tuple
print tup1 == tup2

tup1 += (3,)

print tup1
print tup1[0]

print tup1 + tup2

print len(tup1)

l = list(tup1)
print l
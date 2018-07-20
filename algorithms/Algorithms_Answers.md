Add your answers to the Algorithms exercises here.

Exercise I:

a) O(n)
b) O(log n) 
c) O(sqrt(n))
d) O(n log n)
e) O(n^3)
f) O(n)
g) O(n)

Exercise II:
a) def biggest_diff(a):
    j = a.index(max(a))
    i = a.index(min(a))
    return max([a[j] - min(a[:j]), max(a[i+1:]) - a[i]])
b)

Exercise III:
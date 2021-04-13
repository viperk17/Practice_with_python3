employees = ['Prashant', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Prashant']

developers = ['Judy', 'Prashant', 'Steven', 'Jane', 'April']

if 'Prashant' in developers:
    print('Found!')

# O(n) for list
# O(1) for a set

s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 7, 8, 9}
s3 = {4, 5, 6}
print(s1)
s1.update([7, 8, 9], s2)
print(s1)

# s1.discard(6)
# print(s1)
# s1.remove(6)
# print(s1)

# s4 = s1.intersection(s1, s2)
# print(s4)

s4 = s1.difference(s2, s3)
print(s4)

s4 = s2.difference(s1, s3)
print(s4)

s4 = s2.symmetric_difference(s1)
print(s4)

l1 = [1, 2, 3, 1, 2, 3]
print(l1)
l2 = list(set(l1))
print(l2)

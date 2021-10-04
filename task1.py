from itertools import permutations

a = input()
print('\n'.join(map(''.join, list(permutations(a, 3)))))

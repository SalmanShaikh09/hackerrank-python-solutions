
# HackerRank: itertools.product()


A = list(map(int, input("Enter number: ").split()))
B = list(map(int, input("Enter number: ").split()))



# Approach 1: Using nested loops
# Logic: Pair each element of A with every element of B.

# for X in A:
#     for Y in B:
#         cartesian = (X, Y)
#         print(cartesian, end=" ")




# Approach 2: Using itertools.product()
# Logic: Generate all possible pairs using the product() function.


from itertools import product

print(*product(A, B))
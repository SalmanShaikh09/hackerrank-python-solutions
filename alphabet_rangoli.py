def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3

    for i in range(size - 1, -size, -1):
        row_letters = [
            alpha[abs(j)]
            for j in range(size - 1, abs(i) - 1, -1)
        ]
        row = "-".join(row_letters + row_letters[-2::-1])
        print(row.center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
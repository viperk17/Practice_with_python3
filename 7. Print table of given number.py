# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
    return "\n"

print(table(3))
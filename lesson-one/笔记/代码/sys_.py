import sys

# print(sys.path)
# sys.path.append('./test')

# from test import Name
# print(Name)

if __name__ == '__main__':
    print("Hello", end=" ")
    if len(sys.argv) > 1:
        print(' '.join(sys.argv[1:]))
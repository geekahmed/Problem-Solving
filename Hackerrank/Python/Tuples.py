if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    hs = hash(tuple(integer_list))
    print(hs)
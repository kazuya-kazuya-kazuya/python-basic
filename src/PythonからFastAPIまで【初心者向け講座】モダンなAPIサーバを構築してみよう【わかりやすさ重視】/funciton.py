# インプットもなし、アウトプットもなし
def test():
    print("テスト")

test()

# インプットあり、アウトプットなし
def get_comment(string):
    print(string)

get_comment("コメント")
get_comment("コメント１２３")

# インプットなし、アウトプットあり
def get_number_of_comment():
    return 5

print(get_number_of_comment())

# インプット２つ、アウトプットあり
def sum_price(int1, int2):
    int3 = int1 + int2
    return int3

total = sum_price(2, 5)
print(total)
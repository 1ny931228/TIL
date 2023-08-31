import sys
sys.stdin = open('input.txt')

T = int(input())

def shift_list(lst_nums, MAX, index, i, int_exchange):
    if i == int_exchange:
        return print(f'#{t}', *lst_nums)
    elif 0 <= index < len(lst_nums):
        lst_nums.pop(index)
        lst_nums[0] = MAX
        i += 1
        return shift_list(lst_nums, MAX, index, i, int_exchange)


for t in range(1, T+1):
    nums, exchange = input().split()

    # print(nums, exchange)
    int_exchange = int(exchange)
    lst_nums = [0] + list(map(int, nums))
    # print(int_exchange,lst_nums)
    # nums의 숫자를 불리하는 작업
    MAX = 0

    # MAX를 찾고 자리를 맨 앞 자리로 보내자 얼마큼? N만큼
    for num in lst_nums:
        if MAX < num:
            MAX = num
    index = lst_nums.index(MAX)

    # print(lst_nums, index)

    shift_list(lst_nums, MAX, index, 0, int_exchange)

    # print(t, MAX)





    print()
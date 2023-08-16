bit = [0, 0, 0, 0]

cnt = 0
for i in range(2):
    bit[0] = i
    cnt += 1
    print(1, bit, cnt)
    for j in range(2):
        bit[1] = j
        cnt += 1
        print(2, bit, cnt)
        for k in range(2):
            bit[2] = k
            cnt += 1
            print(3, bit, cnt)
            for l in range(2):
                bit[3] = l
                cnt += 1
                print(4, bit, cnt)
print(cnt)
#과제 2
if __name__ == '__main__':
    x, y, z, n = (int(input()), int(input()), int(input()), int(input()))

lst = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            
    if x+y+z == n:
        continue
    else:
        lst.append([x, y, z])

print(lst)

#Line 5: ValueError: not enough values to unpack (expected 3, got 2)
#왜 value input가 2개밖에 없는지 이해가 안됨.. 원래 2개가 리미트인가?

#과제 3
def dictionary(x):
    if x.islower():
        return (1, x)
    elif x.isupper():
        return (2, x)
    elif x.isdigit() and int(x) % 2 == 1:
        return (3, x)
    else:
        return (4, x)

print(*sorted(input(),key=getKey),sep='')


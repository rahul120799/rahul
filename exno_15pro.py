n2= int(input())
in2_num = list(map(int, input().split()))
 
no2_of_one = []
for i in in2_num:
    count = 0
    while i:
        i &= (i-1)
        count += 1
    no2_of_one.append(count)
 
result = sorted(zip(no1_of_one, in2_num), reverse=True)
print(*[num for _, num in result], sep='\n')

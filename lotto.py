#0이라는 요소를 46번을 가진다.
count = [0]*46


try :
    file = open("lotto.txt","r")

    lines = file.readlines()

    for line in lines :
        nums= line .split(',')

        for i in nums[2:] :
            count[ int(i) ] += 1 #ctrl+c는 실행중에 정지를 할수있음
            

except FileNotFoundError as a:
    print(a)

else:
    file.close()

print(count)

n=input()
#한자리 수 일 때 처
if len(n)==1:
    n=int(n)
    if n==9:
        print(11)
    else:
        print(n+1)
#홀수인 경우
elif len(n)&1:
    a=int(n[:len(n)//2][::-1])
    b=int(n[len(n)//2+1:])
    if a>b:
        #앞에서부터 중앙수 까지의 수와 뒤에서부터 주앙수까지의 숫자 중
        #앞이 더 클 때 뒤에 수를 앞에서부터 카운트 한 것을 거꾸로 붙여준다.
        print(n[:len(n)//2]+n[len(n)//2]+n[:len(n)//2][::-1])
    else:
        #반대인데 중앙 수가 9인 경우
        if int(n[len(n)//2])==9:
            c=str(int(n[:len(n)//2])+1)
            if len(c)==len(n[:len(n)//2]):
                print(c+"0"+c[::-1])
            elif len(c)>len(n[:len(n)//2]):
                print(c+c[::-1])
        else:
            #특별한 경우가 아니면 주앙수에 1을 더해주고 위와 동일하게 한다.
            print(n[:len(n)//2]+str(int(n[len(n)//2])+1)+n[:len(n)//2][::-1])
#짝수인 경우
else:
    a=int(n[:len(n)//2][::-1])
    b=int(n[len(n)//2:])
    if a>b:
        #앞부분이 더 크면 그대로 뒤집어서 붙여준다.
        print(n[:len(n)//2]+n[:len(n)//2][::-1])
    else:
        c=str(int(n[:len(n)//2])+1)
        if len(c)==len(n[:len(n)//2]):
            print(c+c[::-1])
        elif len(c)>len(n[:len(n)//2]):
            print(c+c[::-1][1:])

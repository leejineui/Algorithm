def solution(n):
    if n % 2 == 0:
        # TypeError: unsupported operand type(s) for //: 'str' and 'int'   : // 는  str int 의 계산을 허용하지 않는다. 하지만 * 는 str int 의 계산을 허용
        # 따라서 // 를 먼저 해수고 str 과 int 의  *의계산이 가능하도록 한다.
        return "수박" * (n//2)
    else:

        return "수박" * (n//2) + "수"
# return 을 한 상태 에서는 굳이 print 를 쓰는 것은 의미가 없는 행위 , 함수를 부를때 확이 하기 위해서 print 를 넣는것 . 함수 안에 return 이 있다면 print 넣지 않기


print(solution(5))

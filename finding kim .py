seoul=["Jane", "young","Kim","lee"]



def kim(seoul):

    for i in range(len(seoul)): # for in 구문에는 list indices must be integers or slices, not str -- for i in seoul 안됨 
                                # len(seoul)은 init 'int' object is not iterable, range로 바꿔줘야 함 
        if seoul[i] == "Kim":
            answer = "김서방은 {}에 있다". format(i)  # print 함수 바로 반환 함수의 결과 return으로 갔을시 null  값 실행한 결괏값 null이(가) 
            return answer  # return 은 항상 if 문 뒤에 

kim(seoul) 




import random
score=[] #입력 횟수 기록 위한 리스트
maxscore=11 #최고 기록 위한 변수, 
            #기회는 10밖에 없으므로 11로 초기화해서 나중에 기록과 비교할 수 있도록 한다
while True: #무한 루프, 3번 선택 시 루프 탈출
    print()
    print("UP&DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료 ")
    select=int(input(">>"))
    #게임시작
    if select==1: 
        randnum=random.randint(1,100) #1~100의 랜덤 숫자(정답) 생성 
                                    #randint(a,b)는 a,b 사이의 랜덤한 정수(int)반환한다
        count=0 #시도 횟수를 세는 변수로 나중에 숫자를 입력할 때마다 1씩 증가할 것이다 
        start=1 #입력할 숫자의 범위의 처음 값, 
                #맨 처음에는 1~100이므로 start를 1로 초기화
        end=100 #입력할 숫자의 범위의 마지막 값,
                # 맨 처음에는 1~100이므로 end를 100으로 초기화 
        print(randnum) #***********제출 전 지우자***************
        while True: #무한 루프, 
                    #숫자를 맞추거나 입력을 10회 이상하면 루프 탈출
            answer=int(input("%d번째 숫자 입력(%d~%d) : " %(count+1, start, end)))
            count+=1 #입력횟수 1 증가
            if answer==randnum: #입력한 숫자와 정답이 일치하면
                score.append(count) #입력횟수를 리스트 score에 넣는다
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %(count))
                break #숫자를 맞췄으니 반복문 탈출
            elif count==10: #입력횟수가 10회를 넘으면
                print("입력횟수를 초과하였습니다. 게임오버!") #게임오버
                count+=1 #+1을 해주는 이유는 이 다음에 count와 maxscore를 비교해서 count가 작으면 최고 기록 갱신이라한다.
                        #maxscore를 11로 초기화 했기때문에 count에 +1를 해주지 않으면 조건을 만족해서 최고 기록 갱신이라 하는 상황이 발생한다.
                break
            elif answer<randnum: #입력한 숫자가 정답보다 작으면
                print("UP") #up 출력
                start=answer #입력할 숫자의 범위의 처음 값을 answer로 바꿈 -> answer~end
            elif answer>randnum: #입력한 숫자가 정답보다 크면
                print("DOWN") #down 출력
                end=answer #입력할 숫자의 범위의 마지막 값을 answer로 바꿈 -> start~end
         #최고기록과 비교
        if count < maxscore: #count가 maxscore보다 작으면 즉, 최고 기록을 갱신하면
            maxscore=count  #maxscore를 count 값으로 바꾼다. 즉, count 값이 최고 기록이 된다
            print("최고기록 갱신~!")   
    #기록 확인
    elif select==2:
        if len(score)==0: #리스트 score의 원소 수가 0이면 현재 기록이 없는 것
            print("아직 기록이 없습니다!! 게임을 해보세요")
        else:
            score.sort() #리스트 score의 원소들을 오름차순으로 정렬
            for i in range (0, len(score)): #리스트 score에 있는 원소들을 출력
                print("%d위 : %d회" %(i+1,score[i]))
    #게임 종료
    elif select==3:
        break
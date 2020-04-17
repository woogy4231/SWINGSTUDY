import random

score=[] #입력 횟수 기록 위한 리스트
names=[] #닉네임 기록 위한 리스트
maxscore=11 #최고 기록 비교 변수, 
            #기회는 10밖에 없으므로 11로 초기화해서 나중에 기록과 비교할 수 있도록 한다

#파일을 불러오는 함수
def openfile():
    score.clear() #리스트 score를 비운다
    names.clear() #리스트 names를 비운다
    f=open("list.txt",'r') #읽기 모드로 파일을 연다
    lines=f.readlines() #파일의 내용을 가져와 리스트에 넣는다
    #각 원소의 내용을 :로 구분해서 앞 부분은 names 리스트에 뒷 부분은 socre 리스트에 넣는다.
    for i in range (0, len(lines)):
        filesplit=lines[i].split(':')
        num=int(filesplit[1])
        name=filesplit[0]
        score.append(num)
        names.append(name)
    f.close()

# 최고 기록인지 비교하고 파일에 작성 함수
def cmp(a,b): # a는 최고 기록, b는 현재 기록 
    #현재 기록 b가 최고 기록이면 파일을 추가 모드로 열어 현재 기록을 작성한다.
    if a>b:
        print("최고기록 갱신~!") 
        print()
        name=input("닉네임을 입력하세요 >> ")
        f=open("list.txt", 'a') #파일을 추가모드로 연다
        data=name+str(':')+str(b) 
        f.write(data) #이름:점수 형식으로 파일에 작성한다.
        f.write("\n")
        f.close()
        return b
    else:
        return a

while True: #무한 루프, 3번 선택 시 루프 탈출
    print()
    print("UP&DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료 ")
    select=int(input(">>"))

    #게임시작
    if select==1: 
        randnum=random.randint(1,100) #1~100의 랜덤 숫자(정답) 생성 
                                    #randint(a,b)는 a,b 사이의 랜덤한 정수(int)반환한다
        count=0 #시도 횟수를 세는 변수
        start=1 #입력할 숫자의 범위의 처음 값, 
                #맨 처음에는 1~100이므로 start를 1로 초기화
        end=100 #입력할 숫자의 범위의 마지막 값,
                #맨 처음에는 1~100이므로 end를 100으로 초기화 
        print(randnum)
        while True: #무한 루프, 숫자를 맞추거나 입력을 10회 이상하면 루프 탈출
            answer=int(input("%d번째 숫자 입력(%d~%d) : " %(count+1, start, end)))
            count+=1
            #입력한 숫자와 정답이 일치하면 루프 탈출
            if answer==randnum:
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %(count))
                openfile() #파일의 내용 가져오는 함수 호출
                #불러온 파일에 기록이 있으면 그 기록에서 최고 기록을 가져와 maxscore로 설정한다.
                if len(score)!=0:
                    ind=len(score)-1    #최고 기록을 텍스트 파일의 맨 마지막 줄에 있을거니까 마지막 기록을 가져온다.
                    maxscore=score[ind] 
                maxscore=cmp(maxscore, count) #2번 피드백)) 최고 기록인지 비교하고 파일을 작성하는 함수 호출
                                                #2번 피드백)) 매개 변수: 최고 기록과 입력 횟수
                break
            #입력횟수가 10회를 넘으면 루프 탈출
            elif count==10:
                print("입력횟수를 초과하였습니다. 게임오버!")
                count+=1
                break
            #1번 피드백)) 범위를 초과하는 숫자를 입력하면 다시 숫자를 입력 받도록 한다.
            elif answer < start or answer > end:
                print("범위를 초과하는 숫자를 입력하셨습니다. 다시 입력해주세요")
                count-=1 #1번 피드백)) 입력 횟수가 증가되지 않도록 한다.
                continue #1번 피드백)) continue 명령어로 while의 시작 부분으로 돌아가 다시 숫자를 입력 받도록 한다.
            #입력한 숫자가 정답보다 작으면 up 출력하고 입력 범위 수정
            elif answer<randnum: 
                print("UP")
                start=answer+1
            #입력한 숫자가 정답보다 크면 down 출력하고 입력 범위 수정
            elif answer>randnum:
                print("DOWN")
                end=answer-1
    #기록 확인
    elif select==2:
        openfile()  #파일의 내용 가져오는 함수 호출
        #기록이 없으면 기록이 없다는 메시지 출력
        if len(score)==0:
            print("아직 기록이 없습니다!! 게임을 해보세요")
        #기록 있으면 기록을 출력
        else:
            print("rank/name/score")
            #리스트 score에 있는 원소들을 출력
            for i in range (len(score)-1, -1,-1): #리스트에 큰 숫자부터 들어가 있으므로 역순으로 출력해야 최고 기록순으로 출력 된다.
                print("%d위. %s %d" %(len(score)-i, names[i], score[i]))

    #게임 종료
    elif select==3:
        break
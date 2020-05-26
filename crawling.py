from bs4 import BeautifulSoup
import urllib.request #HTTP 요청 기능을 담은 모듈

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***")
print("학과 \t\t\t\t\t 홈페이지")

#지정한 url의 웹 문서를 요청하여 본문을 반환
html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html") #웹 서버에 정보를 요청한 후, 돌려받은 응답을 저장하여 응답 객체(HTTPResponse)를 반환
result = BeautifulSoup(html.read(), "html.parser")
search = result.findAll("li") #li 태그만 추출(자율전공학부, 바롬인성교육원, 기초교육원이 필터링 됨)

for s in search:
    if "대학원" in s.text : #대학원을 필터링
        continue

    print(s.text, end="\t\t\t\t") #학과 이름(s.text) 출력
    #학과별 버튼을 눌렀을 때 들어가지는 url를 구한다
    link = s.a.get('href') 
    url="http://www.swu.ac.kr" + link
    
    #지정한 url의 웹 문서를 요청하여 본문을 반환하고 원하는 태그만 추출
    html2 = urllib.request.urlopen(url)
    result2 = BeautifulSoup(html2.read(), "html.parser")
    search2 = result2.find("a", {"class", "btn btn_xl btn_blue_gray"})
   
    #search2가 none이면 학과별 홈페이지가 존재하지 않는다는 메시지 출력
    if search2 is None :
        print("홈페이지가 존재하지 않음")
        continue
    
    #search2가 요람 바로가기이면 학과 홈페이지 존재하지 않는 것이므로 존재하지 않는다는 메시지 출력
    #bacha_28.html은 요람 바로가기 주소다
    if search2['href'] == "bacha_28.html" or search2['href'] == "/www/bacha_28.html":
        print("홈페이지가 존재하지 않음")
    else :
        print(search2['href'])


  

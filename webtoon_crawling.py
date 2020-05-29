from bs4 import BeautifulSoup
import urllib.request
import os
import re

###### 해당 회차 이미지 추출 & 이미지 저장 함수 ######
def donwload_img(epilink, title, epi) :
    #해당 페이지를 html 형식으로 읽는다.
    html = urllib.request.urlopen(epilink) 
    result = BeautifulSoup(html.read(), "html.parser")
    #<div class=wt_viewer ...> 태그 추출해 search에 저장
    search = result.findAll("div",{"class","wt_viewer"})

    index=1
    for s in search:
        #추출한 태그 내용 중 <img>태그 내용을 가져와 img에 저장
        img=s.findAll("img")
        for a in img:
            url=a['src']
            #이미지를 저장할 위치 + 이름 + 파일 유형
            path="c:/Users/woogy/Desktop/"+title+"/"+epi+"/"+str(index)+".jpg"

            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            #이미지 저장
            urllib.request.urlretrieve(url, path)

            index=index+1
        print("'"+epi+"' 이미지 저장 완료")

###### 제목 추출 & 폴더 생성 ######
#해당 페이지를 html 형식으로 읽는다.
html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=738174") 
result = BeautifulSoup(html.read(), "html.parser")
#<div class=detail ...> 태그 추출해 search에 저장
search = result.find("div",{"class","detail"})
#추출한 태그 내용 중 <h2>태그 내용을 가져와 문자열로 바꾼 후 search2에 저장 (문자열로 바꾸는 이유는 replace 함수 등을 사용하기 위함)
search2=str(search.h2)
#search2 문자열 중 :를 -로 변경하고 원하는 문자열만 남도록 자른다.
#    -로 치환하는 이유는 윈도우에서 폴더를 생성 시 이름에 \*/:?"<>|를 사용할 수 없기 때문
search2=search2.replace(":","-")
search2= re.sub('[<>=_"/]|[a-z]|[0-9]|\t|\n|\\s', '', search2)
title=search2[0:11]
#폴더를 생성할 위치로 이동한 후 원하는 이름의 폴더를 생성
os.chdir("c:/Users/woogy/Desktop")
os.mkdir("./"+title)
print(title+" 폴더 생성 완료")


###### 에피소드 제목 추출 & 폴더 생성 ######
#해당 페이지를 html 형식으로 읽는다.
html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=738174") 
result = BeautifulSoup(html.read(), "html.parser")
#<td class=title ...> 태그 추출해 search에 저장
search = result.findAll("td",{"class","title"})
#폴더를 생성할 위치로 이동
os.chdir("c:/Users/woogy/Desktop/" + title)

for s in search:
    #추출한 태그 내용 중 <a>태그 내용을 가져와 문자열로 바꾼 후 epi에 저장 (문자열로 바꾸는 이유는 replace 함수 등을 사용하기 위함)
    epi=str(s.a.text)
    epi=epi.replace(":","-")
    #원하는 이름(epi)으로 폴더를 생성
    os.mkdir(epi)
    print("'"+epi+"' 폴더 생성 완료")

    #해당 회차로 들어가기
    epi_num=re.sub('-|[가-힣]|\\s', '',epi)
    epi_link="https://comic.naver.com/webtoon/detail.nhn?titleId=738174&no="+epi_num+"&weekday=tue"
    
    #해당 회차 이미지 추출 함수 호출
    #매개 변수: 회차별 링크, 웹툰 제목, 회차 제목
    donwload_img(epi_link, title, epi)

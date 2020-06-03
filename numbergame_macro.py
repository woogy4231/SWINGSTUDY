from selenium import webdriver

driver=webdriver.Chrome('/Users/woogy/Downloads/chromedriver_win32/chromedriver.exe') #크롬 드라이버 연결
driver.get('http://zzzscore.com/1to50/?ts=1591018968627') #매크로를 이용할 페이지 열기

#숫자 버튼들에 대한 X 좌표(1부터 25까지)를 btn에 저장
btn= driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
#a가 1부터 50일 때까지 반복
#버튼의 숫자가 a의 값과 같으면 버튼을 클릭
for a in range(1, 51):
    for b in btn:
        if b.text == str(a):
            b.click()
            print("number "+str(a)+" clicked!")



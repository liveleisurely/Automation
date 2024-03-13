# Automation

- 취미로 각종 실생활에 편리한 자동화 코드 모음

## 1.001_DailyNewSearching.py
```
<사용 패키지 버전 목록>
datetime: 표준 라이브러리, 별도의 버전 정보 없음
pandas: 2.0.2
requests: 2.29.0
urllib: 표준 라이브러리, 별도의 버전 정보 없음
re: 표준 라이브러리, 별도의 버전 정보 없음
os: 표준 라이브러리, 별도의 버전 정보 없음
selenium: 4.12.0
BeautifulSoup: 4.12.2
webdriver_manager: 버전 122.0.6261.112(공식 빌드) (64비트
```

- 매일 네이버 뉴스에 특정 키워드 검색하여 크롬 창을 띄워주는 파일
- 윈도우 작업 스케줄러를 이용해서 매일 같은 시간에 창을 띄우게 함
- 작업방법:
  1. 메모장을 키고 아래와 같이 입력 후 저장 -> 파일 확장자를 .bat 파일로 변경
   ex) "C:\Users\abc\anaconda3\pythonw.exe" "C:\001_DailyNewSearching.py"
   (파이썬 경로, py파일 경로)
  3. 윈도우키 -> 작업 스케줄러 -> 오른쪽 메뉴 '작업 만들기'
  4. '일반'탭 -> 영어 이름 아무거나
  5. '트리거'탭 -> 새로만들기 -> 원하는 시간 설정
   ex) 월화수목금 09:00
  6. '동작'탭 -> 새로만들기 -> 프로그램/스크립트에 .bat파일 이름 입력
   ex) newsSearching.bat
    '시작위치(옵션)'에 .bat파일 경로만 입력
   ex) C:\Users\ 
  7. '확인' 으로 저장

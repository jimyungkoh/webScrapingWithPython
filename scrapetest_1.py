"""
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
"""
BeautifulSoup의 두번째 매개변수
html.parser: 일반적으로 사용되는 구문분석기
lxml
- 형식을 정확히 지키지 않은 /"지저분한/" HTML 코드를 분석할 때 html.parser보다 더 나음.
- 닫히지 않은 태그, 계층 구조가 잘못된 태그, <head>나 <body> 태그가 없는 등의 문제에서
    일일히 멈추지 않고 그 문제를 수정한다.
- html.parser처럼 범용적으로 사용하기 어려움
    (따로 설치해야 하고 서브파티 C 언어 라이브러리가 있어야 제대로 동작하므로)
html5lib
- lxml보다 더 다양한 에러 수정할 수 있음
- html.parser, lxml보다 조금 더 느리지만,
    잘못 만들어진 HTML이나 손으로 쓴 HTML 분석시 좋은 선택
"""
bs = BeautifulSoup(html.read(), "lxml")
print(bs.h1)
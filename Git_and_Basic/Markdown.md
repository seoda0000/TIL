# 마크다운 (Markdown)

- 텍스트 기반의 가벼운 마크업(markup) 언어
- Markup : 태그를 이용하여 문서의 구조를 나타낸 것
- 문서의 구조 + 내용
- [README.md](http://README.md) 를 이용하여 공식문서 작성. 깃에서 먼저 띄워줌!
- 개발문서의 시작과 끝
- Typora : 실시간 마크다운 변환(미리보기) 제공

* [Markdown Cheat Sheet | Markdown Guide](https://www.markdownguide.org/cheat-sheet/)

---

### # : 헤딩 (Heading)

- 제목, 소제목 h1~h6
- 문서구조의 기본
- 글자 크기를 키울 때 쓰면 안됨

### 1.2.3.* : 리스트 (List)

1. 숫자 리스트
- 목록 표시하기
- 엔터엔터 혹은 Shift + tabㅇ로 수준 삭제

###

### ` : 코드 블럭

- 일반 텍스트와 다르게 코드를 예쁘게 출력
- ` 세 개 : 코드블럭

```jsx
print("hellllllllllllllllllllllo")
print("hellllllllllllllllllllllo")
```

- 한 개 : 인라인 코드블럭
문장 안에 코드가 `print("hello")` 들어갈 때

### [string보여지는 문구] (url링크) : 링크

* [구글로 이동하기](https://google.com)



### ! [string] (img_url) : 이미지

![penguin](../images/penguin.png)

링크는 상대주소로 나타남. 설정에서 바꾸면 폴더에 복사되게 할 수도 있음.

### 텍스트 강조

* **bold**    ** b ** 
* *italic*    * i * 
* ~~strikeout~~    ~~ s ~~

### 수평선

-세 개 이상

---
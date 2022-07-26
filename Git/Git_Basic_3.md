
# **Git 기초 : gitignore, gitkeep**



### **.gitignore**

- 새 레포지토리에 .gitignore 만들기
- Github에 올리고 싶지 않은 파일 리스트 적기
- 해당 파일들은 Git이 버전관리하지 않음

```
test.txt  # 파일명

folder/  # 폴더명
folder/*  # 폴더명

*.txt  # 확장자
```

- 사이트 활용하기 : [gitignore.io](https://www.toptal.com/developers/gitignore/)

### **.gitkeep**

- 빈 폴더도 Github에 올리기
- .gitkeep 파일을 생성하면 됨
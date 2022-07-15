# Git 기초 2
### 20220715
---

## Git 기초 원리, Visual Studio Code, commit-push-pull-clone

----------

### 커밋은 파일이 아닌 **수정사항**만을 저장!

1. **Working Directory** : 내가 작업하고 있는 실제 디렉토리
    1. 파일 신규 생성 `untracked`
    2. Working Directory → `git add` → Staging Area
    3. `untracked` → `tracked`
2. **Staging Area** : 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳. 특정 버전으로 관리하고 싶은 변경상태들이 잠깐 머무는 곳.
    1. Git으로 버전관리 된 상태 `staged` 
    2. Staging Area → `git commit` → Repository
    3. `tracked` → `committed`
3. **Repository** : 커밋들이 저장되는 곳 (.git sirectory)
    1. 파일 수정 `modified`
    2. Working Directory →`git add` → Staging Area
    3. 반복!

---

# Visual Studio Code

font : D2Coding

![Untitled](https://www.notion.so/hphk-edu/Git-2-a9bbc331bbba454799b297ffa291a2b1#bacf753cd23d4ea5b6f2d1599cb902c6)

메뉴 터미널 클릭시 Git bash 이용 가능

## `ctrl + k → f`

- vsc에서 폴더 닫기

## `ctrl + shift + ``

- VS에서 터미널 열기

## `ctrl + ,`

- 설정 열기

---

# Git Bash 이용하기

## `git status`

- 현재 Git으로 관리되고 있는 파일들의 상태를 알 수 있음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/27505b08-b4fe-4d95-ba7d-d136c15a23db/Untitled.png)

- 코딩 전에 이 화면이 보여야 함. 모든 커밋이 완료됨.

## `git add .`

- 디렉토리의 모든 파일을 **Staging Area에** 올리기

## `git add 파일명`

- 파일을 **Staging Area**에 올리기

## `:q`

- 창 나가기

## `git commit -m "한줄 커밋 메세지"`

- 커밋 메세지 : 영어가 좋긴 하지만 알아볼 수 있어야 함!

## `git log`

- 깃 로그 확인하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/500ff121-3384-40e6-892f-33adc480756a/Untitled.png)

- commit 커밋 아이디
- 보통 앞 네 자리만으로 구분 가능

## ⬆️

- 여태 썼던 명령어 로그 확인 가능

## `git diff 커밋아이디A 커밋아이디B`

- A에서 B로 어떻게 변경되었는지

---

## Local Repository

- 컴퓨터에 있는 레퍼지토리

## Remote Repository

- 어딘가(ex. Github)에 있는 레퍼지토리

## `git remote add origin {remote_repo 주소}`

- origin : repo name 별명. 관례상 origin이라고 적음.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/26ab368f-06d2-4729-9565-872723bdc511/Untitled.png)

## `git clone {remote_repo}`

remote에서 local로 가져오기

## `git push {어디로 push} {push할 branch이름}`

- branch 기본 이름 : master

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d3420a0f-7e59-4fdb-8f4e-36d9723e2620/Untitled.png)

## `git push --set-upstream origin master`

- git push의 기본 경로 설정

## `code .`

- 해당 폴더의 코드 열기

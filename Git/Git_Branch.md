`git checkout -b {branch name}`
브랜치 생성 및 이동

`git fetch origin`
로컬에서 원격 저장소 확인

`git reset --hard origin/develop`
develop으로 상태 변경

`git cherry- pick {commit num}`
해당 commit 변경사항만 떠오기

======================================
`git remote add github {레포주소}`
`git push github master`

레포 옮기기

=====================================
`git filter-branch --tree-filter 'find . -name "*.pt" -exec rm -rf {} +' HEAD~10..HEAD`
최근 10개 커밋 확인해서 pt 파일 업로드한 커밋 수정하기

===
`git push <원격 저장소 이름> -d <원격 브랜치 이름>`
원격 브랜치 삭제

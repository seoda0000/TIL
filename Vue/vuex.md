# State Management

- 상태State : 현재에 대한 정보data
- App이 가지고 있는 Data로 표현
- 여러개의 component를 조합하여 하나의 App을 만듬
    - 여러개의 component가 같은 상태를 유지 필요

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/56d99568-0e0a-4938-b023-c759089af16e/Untitled.png)

## Centralized Store

- 중앙 저장소에 데이터를 모아서 상태 관리
- 각 component는 중앙 저장소의 데이터를 사용
- component의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경 가능
- 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

## Vuex

- state management pattern + Library for vue.js
    - 상태관리 패턴 + 라이브러리
- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경될 수 있도록 규칙 설정
- Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공

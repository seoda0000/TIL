# 프록시

- 지연 로딩 : 엔티티가 실제 사용될 때까지 데이터베이스 조회를 지연하는 방법
- 프록시 객체 : 실제 엔티티 객체 대신에 데이터베이스 조회를 지연할 수 있는 가짜 객체

## 프록시 기초

### 프록시의 특징

프록시 클래스는 실제 클래스를 상속 받아서 만들어진다. 겉 모양이 같다.

실제 객체에 대한 참조(target)을 보관한다. 프록시 객체의 메소드를 호출하면 프록시 객체는 실제 객체의 메소드를 호출한다.

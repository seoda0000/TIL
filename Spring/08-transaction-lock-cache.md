# 트랜잭션과 락

### 🎯 목표

트랜잭션 기초와 JPA가 제공하는 락에 대해 알아보기

### ACID

- 원자성: 트랜잭션 내에서 실행한 작업들은 마치 하나의 작업인 것처럼 모두 성공하든가 모두 실패해야 한다.
- 일관성 : 모든 트랜잭션은 일관성 있는 데이터베이스 상태를 유지해야 한다. 예를 들어 데이터베이스에서 정한 무결성 제약 조건을 항상 만족해야 한다.
- 격리성 : 동시에 실행되는 트랜잭션들이 서로에게 영향을 미치지 않도록 격리한다.
- 지속성 : 트랜잭션을 성공적으로 끝내면 그 결과가 항상 기록되어야 한다. 중간에 시스템에 문제가 발생해도 데이터베이스 로그 등을 사용해서 성공한 트랜잭션 내용을 복구해야 한다.

트랜잭션은 원자성, 일관성, 지속성을 보장한다.

격리성을 완벽하게 보장하려면 트랜잭션을 차례대로 실행해야 한다 → 성능 문제 발생. 격리 수준을 선택해야 한다.

### 트랜잭션 격리 수준

`격리 수준이 낮다` : 동시성 증가, 문제 발생

- READ UNCOMMITED 커밋되지 않은 읽기
- READ COMMITED 커밋된 읽기
- REPEATABLE READ 반복 가능한 읽기
- SERIALIZABLE 직렬화 가능

`격리 수준이 높다`

### 격리 수준에 따른 문제점

| 격리 수준       | DIRTY READ | NON-REPEATABLE READ | PHANTOM READ |
| --------------- | ---------- | ------------------- | ------------ |
| READ UNCOMMITED | o          | o                   | o            |
| READ COMMITED   |            | o                   | o            |
| REPEATABLE READ |            |                     | o            |
| SERIALIZABLE    |            |                     |              |

- DIRTY READ : 트랜잭션 1이 커밋하지 않아도 트랜잭션 1이 수정중인 데이터를 트랜잭션 2가 볼 수 있다. 이때 트랜잭션2가 해당 데이터를 사용하는데 트랜잭션1이 롤백하면 정합성에 심각한 문제가 생긴다.
- NON-REPEATABLE READ : 반복해서 같은 데이터를 읽을 수 없는 상태. 트랜잭션 1이 데이터 A를 조회 중인데 트랜잭션 2가 데이터 A를 수정하고 커밋하면, 트랜잭션1이 다시 데이터 A를 조회했을 때 수정된 데이터가 조회된다.
- PHANTOM READ : 반복 조회 시 결과 집합이 달라지는 상태. 트랜잭션 1이 10살 이하 회원을 조회했는데 트랜잭션 2가 5살 회원을 추가하고 커밋하면, 트랜잭션 1이 다시 10살 이하 회원을 조회했을 때 회원 하나가 추가된다.
- SERIALIZABLE : 가장 엄격한 트랜잭션 격리 수준. 동시성 처리 성능익 급격히 떨어질 수 있다.

- 보통 READ COMMITTED 격리 수준을 기본으로 사용
- 최근에는 락보다는 MVCC를 사용한다.

## 2. 낙관적 락과 비관적 락 기초

JPA 영속성 컨텍스트(1차 캐시)를 적절히 활용(엔티티로 조회)

→ READ COMMITTED 격리 수준이어도 애플리케이션 레벨에서 REPEATABLE READ가 가능

### 낙관적 락

- 트랜잭션 대부분은 충돌이 발생하지 않는다고 낙관적으로 가정.
- JPA가 제공하는 버전 관리 기능을 사용
- 애플리케이션이 제공하는 락
- 트랜잭션을 커밋하기 전까지는 트랜잭션의 충돌을 알 수 없다.

### 비관적 락

- 트랜잭션의 충돌이 발생한다고 가정하고 우선 락을 건다.
- 데이터베이스가 제공하는 락 기능 사용.
- ex) `select for update`

### 두 번의 갱신 분실 문제

- 사용자 A가 공지사항을 수정하고, 사용자 B가 공지사항을 수정했을 때 B의 수정사항만 남게 되었을 때
- 데이터베이스 트랜잭션의 범위를 넘어선 문제

<aside>
💡 마지막 커밋만 인정하기 (기본)

사용자 A의 내용은 무시, 사용자 B의 내용만 인정

</aside>

<aside>
💡 최초 커밋만 인정하기

사용자 A가 수정을 완료했으므로 사용자 B가 수정을 완료할 때 오류 발생

</aside>

<aside>
💡 충돌하는 갱신 내용 병합하기

사용자 A와 사용자 B의 수정사항을 병합

</aside>

## 3. @Version

- JPA에 버전 관리 기능 추가
- 적용 가능한 타입 : `Long`, `Integer`, `Short`, `Timestamp`

```java
@Entity
public class Board {
	@Id
	private String id;
	private String title;

	@Version
	private Integer version; // 버전 관리용 필드
}
```

- 엔티티를 수정할 때마다 버전이 하나씩 자동으로 증가
- 엔티티를 수정할 때 조회 시점과 수정 시점의 버전이 다르면 예외 발생
- `💡 최초 커밋만 인정하기` 적용

### JPA의 버전 정보 비교 방법

엔티티를 수정하고 트랜잭션을 커밋

영속성 컨텍스트를 플러시 → **엔티티의 버전 정보를 검색 조건에 추가**하고 UPDATE 쿼리 실행

```sql
UPDATE BOARD
SET
		TITLE=?,
		VERSION=? (버전 + 1 증가)
WHERE
		ID=?
		AND VERSION=? (버전 비교)
```

- 값 타입(임베디드 타입, 컬렉션) : 해당 엔티티의 값. 수정하면 엔티티의 버전이 증가
- 연관관계 필드 : 외래 키를 관리하는 주인 필드를 수정할 때만 증가
- 버전 관리 필드는 JPA가 직접 관리하므로 개발자가 임의로 수정하면 안된다.

## 4. JPA 락 사용

<aside>
👍 추천 전략 : READ COMMITTED 트랜잭션 격리 수준 + 낙관적 버전 관리

- 두 번의 갱신 내역 분실 문제 예방
</aside>

### 락의 적용 위치

- EntityManager.lock(), EntityManager.find(), EntityManager.refresh()
- Query.setLockMode() (TypeQuery 포함)
- @NameQuery

### 조회하면서 즉시 락 걸기

```java
Board board = em.find(Board.class, id, LockModeType.OPTIMISTIC);
```

### 필요할 때 락 걸기

```java
Board board = em.find(Board.class, id);
em.lock(board, LockModeType.OPTIMISTIC);
```

## 5. JPA 낙관적 락

- 트랜잭션 커밋 시점에 충돌을 알 수 있다.
- 버전 필요
- @Version만 있어도 낙관적 락이 적용된다.

### NONE

### OPTIMISTIC

### OPTIMISTIC_FORCE_INCREMENT

## 6. JPA 비관적 락

- 데이터베이스 트랜잭션 락 메커니즘에 의존
- SQL 쿼리에 `select for update` 구문 사용하며 시작
- 버전 사용 x
- 엔티티가 아닌 스칼라 타입을 조회할 때도 사용 가능
- 데이터를 수정하는 즉시 트랜잭션 충돌 감지 가능

### PERSIMISTIC_WRITE

### PERSIMISTIC_READ

### PERSIMISTIC_FORCE_INCREMENT

## 7. 비관적 락과 타임아웃

- 비관적 락을 사용하면 락을 획득할 때까지 트랜잭션이 대기 (타임아웃 설정 가능)

---

# 2차 캐시

### 🎯 목표

JPA가 제공하는 애플리케이션 범위의 캐시에 대해 알아보기

하이버네이트와 EHCACHE를 사용해 실제 캐시를 적용해보기

## 1. 1차 캐시와 2차 캐시

- 시간 비용과 개선 방안
  네트워크를 통해 **데이터베이스**에 접근 >>> 애플리케이션 서버에서 **내부 메모리**에 접근
  → 조회한 데이터를 **메모리에 캐시**해서 데이터베이스 접근 횟수를 줄이기

### 1차 캐시

- 기본적으로 영속성 컨텍스트 범위의 캐시
  - 컨테이너 환경 : 트랜잭션 범위 / OSIV : 요청 범위
- 영속성 컨텍스트 내부의 엔티티 저장소
  - 엔티티 매니저로 조회/변경하는 모든 엔티티 저장
  - 트랜잭션을 커밋하거나 플러시를 호출 → 1차 캐시에 있는 엔티티의 변경 내역을 데이터베이스에 동기화
  - 영속성 컨텍스트 자체가 사실상 1차 캐시
- 1차 캐시에 같은 엔티티가 있으면 해당 엔티티를 그대로 반환 → 객체 동일성 보장
- 일반적인 웹 애플리케이션 환경 : 트랜잭션을 시작하고 종료할 때까지 유효
- OSIV를 사용(요청의 시작부터 끝까지 같은 영속성 컨텍스트 유지)해도 클라이언트의 요청이 들어올 때부터 종료할 때까지 유효
- → 애플리케이션 전체로 보면 데이터베이스 접근 횟수를 획기적으로 줄이지는 못함

### 2차 캐시 (공유 캐시)

- 애플리케이션에서 공유하는 캐시
  - 애플리케이션 범위
  - 분산 캐시, 클러스터링 환경의 캐시는 더 오래 유지 가능
- 애플리케이션 조회 성능 향상 가능

1. 영속성 컨텍스트는 엔티티가 필요하면 2차 캐시 조회
2. 2차 캐시에 엔티티가 없으면 데이터베이스 조회
3. 결과를 2차 캐시에 보관
4. 2차 캐시는 자신이 보관하고 있는 엔티티를 복사해서 반환
5. 2차 캐시에 저장하고 있는 엔티티를 조회하면 복사본을 만들어 반환

- 동시성 극대화 : 객체의 복사본 반환
  - 여러 곳에서 같은 객체를 동시에 수정하는 문제 예방
- 영속성 유닛 범위의 캐시
- 데이터베이스 기본 키를 기준으로 캐시하지만, 영속성 컨텍스트가 다르면 객체 동일성을 보장하지 않는다.

## 2. JPA 2차 캐시 기능

### 캐시 모드 설정

1. @Cacheable : 엔티티에 2차 캐시 사용 설정 추가
2. persistence.xml에 캐시모드 설정

### 캐시 조회, 저장 방식 설정

- 캐시 조회 모드
  - `USE`: 캐시에서 조회 (기본값)
  - `BYPASS`: 캐시 무시, 데이터베이스 직접 접근
- 캐시 보관 모드
  - `USE`: 조회한 데이터를 캐시에 저장. 이미 캐시에 있으면 최신 상태로 갱신하지 않는다. 트랜잭션을 커밋하면 등록 수정한 엔티티도 캐시에 저장. (기본값)
  - `BYPASS`: 캐시에 저장x
  - `REFRESH`: `USE` + 데이터베이스에서 조회한 엔티티를 최신 상태로 다시 캐시

### JPA 캐시 관리 API

## 3. 하이버네이트와 EHCACHE 적용

### 하이버네이트가 지원하는 캐시

1. 엔티티 캐시 `JPA 표준`
   - 엔티티 단위로 캐시
   - 식별자로 엔티티를 조회하거나 컬렉션이 아닌 연관된 엔티티를 로딩할 때 사용
2. 컬렉션 캐시
   - 엔티티와 연관된 컬렉션을 캐시
   - 컬렉션이 엔티티를 담고 있으면 식별자 값만 캐시 `하이버네이트 기능`
3. 쿼리 캐시
   - 쿼리와 파라미터 정보를 키로 사용해서 캐시
   - 결과가 엔티티면 식별자 값만 캐시 `하이버네이트 기능`

### 환경설정

- pom.xml에 hibernate-ehcache 라이브러리 추가
- ehcache.xml 추가
- persistence.xml에 캐시 정보 추가

### 엔티티 캐시와 컬렉션 캐시

- @Cacheable : 엔티티 캐시
- @Cache : 하이버네이트 전용. 컬렉션 캐시를 적용하거나 캐시와 관련된 세밀한 설정을 할 때 사용

### @Cache

- usage 속성 : 캐시 동시성 전략 설정

### 캐시 영역

- 엔티티 캐시 영역 / 컬렉션 캐시 영역
- 캐시를 적용한 코드는 캐시 영역에 저장
- 영역별로 세부 설정 가능
  - ex) 600초마다 캐시에서 제거

### 쿼리 캐시

- 쿼리와 파라미터 정보를 키로 사용해서 쿼리 결과를 캐시하는 방법
- 영속성 유닛 설정 : hibernate.cache.use_query_cache=true

### 쿼리 캐시 영역

- 쿼리 캐시를 활성화하면 캐시 영역이 추가
  - 쿼리 캐시를 저장하는 영역. 쿼리, 쿼리 결과 집합, 쿼리를 실행한 시점의 타임스탬프 저장.
  - 쿼리 캐시가 유효한지 확인하기 위해 쿼리 대상 테이블의 가장 최근 변경 시간을 저장하는 영역. 테이블 명, 해당 테이블의 최근 변경된 타임스탬프 보관.

### 쿼리 캐시와 컬렉션 캐시의 주의점

- 쿼리 캐시와 컬렉션 캐시는 결과 집합의 식별자 값만 캐시한다.
- 조회 시 식별자 값을 하나씩 엔티티 캐시에 조회해서 실제 엔티티를 찾는다.

<aside>
⚠️ 문제 상황

쿼리 캐시나 컬렉션 캐시만 사용하고 대상 엔티티에 엔티티 캐시를 적용하지 않는 경우

→ 성능상 심각한 문제 발생 (데이터베이스에서 각각 조회한다)

</aside>
# Vue with DRF

## Server & Client

### Server는 정보와 서비스를 제공

- DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당
- 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답

### Client는 사용자의 정보 요청을 처리, server에게 응답 받은 정보를 표현

- Server에게 정보(데이터)를 요청
- 응답 받은 정보를 가공하여 화면에 표현

## Again DRF

---

# CORS

****`CORS_ALLOWED_ORIGINS: Sequence[str]`****

- `[Access-Control-Allow-Origin` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)
- 문자열 array

****`CORS_ALLOWED_ORIGIN_REGEXES: Sequence[str | Pattern[str]]`****

- 정규 표현식

****`CORS_ALLOW_ALL_ORIGINS: bool`****

- 모든 출처 허용. 기본값 False

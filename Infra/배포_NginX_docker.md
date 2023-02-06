# 배포 구조

![Untitled](../images/%EB%B0%B0%ED%8F%AC_Nginx_docker1.png)

# NGINX

- High perormance load balancer, web server, API gateway & reverse proxy
- 비동기 방식이기 때문에 매우 높은 성능
- 정적인 파일(주로 프론트엔드 파일들)을 서비스할 때 뛰어난 성능(vs톰캣)
- load balancer나 API gateway용도로도 사용 가능
- DDOS 공격 방어도 가능

### 포트 요청

HTTPS (80)

HTTP (443)

### NGINX가 분기 처리

프론트엔드 라우터(Webserver) : /

백엔드(API gateway) : /api

```
server {
	listen 80 default_server;
	listen [::]:80 default_server;


	# Frontend 설정
	root /var/www/html/dist;        # Front 빌드 파일 위치
	index index.html index.htm;     # index 파일명
	server_name _;                  # 서버 도메인

	location / {
		try_files $uri $uri /index.html;
	}


	# Backend Proxy 설정
	location /api {
		proxy_pass http://localhost:8399/api/;
		proxy_redirect off;
		charset utf-8;

		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_set_header X-NginX-Proxy true;
	}
}
```

`npm run build` : 정적인 파일 최종 생성

npm run serve : 개발 서버. 최적화가 안되어 있음. 성능이 떨어짐.

### CORS

- Cross-Origin Resource Sharing(CORS)
- 도메인, 포트, 프로토콜이 다를 때 발생한다
- nginx의 설정으 기억해보자
- [https://domain-a.com](https://domain-a.com) 의 프론트 엔드 JS 코드가 XMLHttpRequest를 사용하여 [https://domain-b.com/data.json을](https://domain-b.com/data.json을) 요청하는 경우

# 우리는 왜 도커를 쓰는가?

- 빠르게 필요한 서버를 증설 가능
- 기존에는 VM을 증설하는 방식을 사용
  - VM이 부팅되는 1분이면 서비스 전체가 중지되기에 충분한 시간
- 운영체제를 부팅해야 하는 기존의 방식보다 빠름
- 이미지를 만들어두면 찍어내기만 하면 되는 배포의 편의성(w/ k8s)

### 어디까지 도커화 해야할까?

- 프론트엔드 / 백엔드는 필수적
- 배포의 효율성 / 편의성 고려
- DB / Jenkins / nginx는 선택적

# 임의의 포트를 쓰면 안되는 이유?

- ISP(SKT, KT, LGU 등등)에 따라서 닫혀 있는 포트가 존재
- 고객은 포트가 막혔을 거라는 생각을 하지 못하고 이탈

# gitlab → Jenkins

![Untitled](../images/%EB%B0%B0%ED%8F%AC_Nginx_docker2.png)

- 개발자가 gitlab의 특정 브랜치 (develop or master)에 머지를 하면 이벤트가 트리거되어 Jenkins에서 빌드를 시작한다
- 빌드가 완료되면 도커 이미지가 제작되어 배포된다
- 동일한 도커 이미지로 제작, 배포되기 때문에 동일성이 보장된다

# SSL(→TLS)

- 회원 가입 시에 비밀번호 등의 개인정보가 전송되고, 수시로 유출되어서는 안되는 정보들이 오가기 때문에 암호화가 필요하다
- 매번 데이터를 암호화해서 전송하기 어렵기 때문에 TLS(Transport Layer Security)를 사용한다
- 이론적으로 TLS를 활용한 통신은 안전하다고 볼 수 있다
- WebRTC를 위해서는 SSL 인증서 설치 필요
- 443포트에 JWT, TLS 적용

# Cert Bot

![Untitled](../images/%EB%B0%B0%ED%8F%AC_Nginx_docker3.png)

- https 확산을 위해서 시작된 비영리 프로젝트 (Let’s encrypt)
- 상용 프로그램을 제작할 때는 보통 신뢰할 수 있는 ROOT 인증서 발급자로부터 SSL 인증서를 구매해서 사용
- Cert Bot은 무료 인증서 제공
- Cert Bot은 nginx에 자동으로 설정을 추가해준다

# 사용자 계정 만들기

- 각 프로그램들을 실행할 때는 프로그램에 맞는 권한을 가진 사용자 계정을 만들어서 실행
- ubuntu 계정이나 root 계정으로 실행하는 경우에는 해커의 공격 명령이 그 계정의 권한으로 실행되기 때문에 매우 위험
- 사용자 계정으로 실행하는 경우 해커의 공격을 받더라도 피해 최소화

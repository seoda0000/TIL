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

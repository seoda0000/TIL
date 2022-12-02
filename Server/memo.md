## 리눅스

sudo lsof -i:8888

PID 확인 후 

sudo kill -9 {PID}

## Cloud 9
/environment
### 실행
nohup python3 main.py &

### 종료
ps -ef | grep main.py
kill -9 {num}

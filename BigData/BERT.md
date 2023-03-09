Bidirectional Encoder Representations from Transformers

Bidirectional : 양방향

Encoder : 입력값을 숫자의 형태로 바꿈

Transformer: Encoder(양방향) Decoder(단방향) 구조를 지닌 딥러닝 모델

Decoder:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2d8c55b2-a0e2-4b7a-9e81-879674047679/Untitled.png)

단방향이므로 라벨링 필요 X

이후 무슨 단어가 올지 예측

Encoder:

단방향 Decoder는 문맥 이해에 부족.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f7da92ee-8de4-47fd-9bbd-f9419f2e57e6/Untitled.png)

문장 Encoder에 투입 → 각 토큰들이 Positional Encoding과 더해짐 → 모든 토큰의 행렬 계산을 통해 Attention Vector 생성

Attention Vector : 다른 Token과의 관계를 통해 Token의 의미를 구하기 위해서 사용

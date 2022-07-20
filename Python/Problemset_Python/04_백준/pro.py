while True: #백준 여러줄 입력받기
    try: #백준 여러줄 입력받기

        chicken, c = map(int, input().split())

				# 첫번째 치킨 먹기
        sum_chicken = chicken
        coupon = chicken
				
				# 쿠폰으로 치킨 먹기
        while coupon//c != 0:
            sum_chicken += coupon//c
            coupon = coupon//c + coupon%c
        print(sum_chicken)

    except EOFError: #백준 여러줄 입력받기
        break #백준 여러줄 입력받기

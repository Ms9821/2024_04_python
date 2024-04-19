# 1. 원화 변환기 (대입 연산자)
# "현재 원화를 입력 하면 달러로 바뀌는 프로그램을 작성하세요!"
# * 예시: 1410 -> 1$
won = int(input("원화 입력 하세요:"))
rate = 1400
print(f"달러: {won/rate}$ 입니다.")

# 2. 수학 연산 프로그램 (산술 연산자)
# "사용자로부터 두 개의숫자를 입력받아,이 두 숫자에 대한
# 합,차,곱,몫,나머지,제곱을 계산하는 프로그램을 만들어보세요.
# 입력받은 두 숫자에 대해 다음과 같은 연산 결과를
# 출력해주는 프로그램을 작성해보세요!"
# * 예시 사용자 입력: 12,3
# 프로그램 출력
# "합 15"
# "차 9"
# "곱 36"
# "몫 4"
# "나머지 0"
# 첫 번쨰 수의 두 번째 제곱:1728
first = int(input("첫 번쨰 정수:"))
second = int(input("두 번쨰 정수:"))
print(f"합:{first+second} 차:{first-second} 곱:{first*second}")
print(f"몫:{first//second} 나머지:{first%second} 제곱:{first**second}")

# 3. 원의 둘레와 넓이 계산 프로그램
# "사용자로붕터 원의 반지름을 입력받아, 그 원의 둘레와 넓이를
# 계산하는 프로그램을 만들어보세요. 원의 둘레는 2 * n * 반지름,
# 원의 넓이는 n * 반지름*2 공식을 사용하여 계산하며,결과를
# "원의 둘레는 [둘레]이고,넓이는 [넓이]입니다."라고
# 추력하는 프로그램을 작성해보세요!."
radius = int(input("원의 반지름:"))
p1 = 3.14
print(f"원의 넓이:{radius**2*p1}, 원의 둘레:{radius*2*p1}")
#변수 (variable)
#오른쪽 데이터를 왼쪽의 변수에 넣는다.
name = "조명신"
major = "컴퓨터공학과"
fruit = "사과"

#f문자열 문법
print(f"저는 {name} 입니다")
# 저의 이름은 ~ 저의 전공은 ~이고 제가 좋아하는 과일은 ~ 입니다.
print(f"저의 이름은 {name}이고 저의 전공은 {major}이고 제가 좋아하는 과일은 {fruit}입니다.")

# 변수명 문법 규칙
# 1.시작할 떄 영문자 또는 _로만 가능하다
# ex) 123name(x), name123(o)
# 2.숫자 포함 가능
# 3.특수문자 _빼고 안됨
# 4.예약어 안됨 [추후 배울 것]
# 5.의미 있는 이름으로 지을 것
# - 두 단어 이상 합칠 때
# - 이름 짓는 방식: koreait[x] -> korea_it,koreait
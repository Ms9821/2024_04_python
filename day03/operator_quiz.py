# 1.뉴스 기사 단어 검색 프로그램
# "뉴스 기사를 스크랩해 온후,사용자로부터 입력받은 단어가 그 기사
# 내에 존재하는지 여부를 나타내는 프로그램을 만들어보세요.
# 사용자에게 검색하고 싶은 단어를 입력받고,해당 단어가 뉴스 기사 내에
# 있는지를 확인하여 '검색하신 단어는 뉴스 기사 내에 True or False.'
# 라고 알려주는 프로그램을 작성해보세요.!"
# * 예시: 사용자가 '경제'라는 단어를 입력했다면,프로그램은
# "검색하신 단어는 뉴스 기사 내에 True or False 입니다."
#news = """윤석열 대통령 국정에 대한 지지율이 취임 후 최저치를 기록했다는 여론조사 결과가 나왔다.
#한국갤럽은 지난 16~18일 전국 만 18세 이상 1000명을 대상으로 실시한 여론조사에서 윤 대통령 직무수행에 대한 긍정 평가가 23%를 기록했다고 19일 발표했다.
#
#이 같은 수치는 직전 조사 결과(3월 4주차)보다 무려 11%포인트나 하락한 것이자 취임 후 최저치다. 종전 긍정평가 최저치는 인사, 취학연령 하향 이슈의 영향을 받아 지지율 하락을 겪은 2022년 8월 1주 차, 외교 문제와 비속어 발언 파문의 영향을 받은 9월 5주 차 때 기록한 24%다.
#
#긍정 평가가 크게 줄어든 만큼 부정 평가는 당연히 크게 늘었다. 10%포인트 오른 68%로 역대 최고치를 기록했다."""
#
#word = input("검색 하고 싶은 단어:")
#result = word in news
#print(f"검색하신 단어는 뉴스 기사 내에 {result}")

# 2.비밀번호 검증 프로그램
# "사용자로부터 비밀번호 설정을 입력받아,해당 비밀번호가 느낌표(!)를
# 포함하고 'IT'라는 문자열을 포함하고 있는지를 확인하는 프로그램을
# 만들어보세요.두 조건을 모두 만족하는지를 검사하여 '비밀번호가 요구
# 사항을 True or False'라고 결과를 알려주는 프로그램을 작성해보세요!"
# 예시 * :사용자가 'WelcomeIT!'라는 비밀번호를 설정했다면,
# 프로그램은 "비밀번호가 요구 사항을 True"라고 출력합니다.
# "'사과'좋아"
password = input("비밀 번호 입력:")
result = "!" in password and "IT" in password
print(f"비밀번호가 요구 사항을 {result}")
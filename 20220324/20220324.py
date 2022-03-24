# 1번 첫번째와 세번째 문자 출력

from gettext import find


letters = "python"
print(letters[0])
print(letters[2])
print("\n\n\n")






# 2번 문자열 거꾸로 출력

string = "PYTHON"
i = len(string)-1
while (i >= 0):
    print(string[i])
    i -= 1
print("\n\n\n")






# 3번 "kr" 입력 시 kr만 찾아서 출력

# url = "http://sharebook.kr"

# lookfor = input("찾고싶은 문자열을 입력하세요 : ")

# index_num = url.rfind(lookfor)
# print(f"index = {index_num},    index_name =", lookfor)
# print("\n\n\n")



# 4번 endswith 사용

file_name = "2022_보고서.xlsx"
print("file_name이 액셀 파일인가요?", end = ' ')
print(file_name.endswith("xlsx"))
print("\n\n\n")







# 5번

print("file_name이 2020으로 시작하나요?", end = ' ')
print(file_name.startswith("2020"))
print("\n\n\n")






# 6번 score 입력 받기

# while(1):
#     score = int(input("점수를 입력해주세요 : "))

#     if (score > 100 or score < 0):
#         print("0 ~ 100사이의 점수를 입력하세요")
#     elif (score > 80):
#         print("A학점")
#     elif (score > 60):
#         print("B학점")
#     elif (score > 40):
#         print("C학점")
#     elif (score > 20):
#         print("D학점")
#     else:
#         print("E학점")

#     if (score >= 0 and score <= 100): break




# 7번 리스트 갯수 구하기

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print("cook 리스트의 갯수는 %d개 입니다" % len(cook))
print("\n\n\n")








# 8번

# waring_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# name = input("관심 있는 주식명을 입력하세요 : ")
# if name in waring_investment_list:
#     print("투자 경고 종목입니다!!!!!")
# else:
#     print("투자 경고 종목이 아닙니다^_^")
# print("\n\n\n")






# 9번 
list_tax = [100, 200, 300]
for a in list_tax:
    print(a+10)
print("\n\n\n")





# 10번 

list_name = ["SK하이닉스", "삼성전자", "LG전자"]

i = 0
while (i < len(list_name)):
    print(len(list_name[i]))
    i += 1
print("\n\n\n")
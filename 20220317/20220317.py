# 1번 화면에 Hello World 문자열 출력
from audioop import add
from shutil import move


print("Hello World")



# 2번 Mary`s cosmetic 출력
print("Mary`s cosmetic")


# 3번 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')



# 4번 "C:\Windows" 출력
print('"C:\Windows"')



# 5번 \t와 \n의 역할
print("안녕하세요.\n만나서\t\t반갑습니다.") # \n은 개행문자로서 줄을 바꿔주고, \t는 tap의 역할이다.



# 6번 List 생성
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)



# 7번 List에 "배트맨" 추가
movie_rank += ["배트맨"]
print(movie_rank)   # OR

movie_rank2 = ["닥터", "스플릿", "럭키"]
print(movie_rank2)
movie_rank2.append("배트맨")
print(movie_rank2)



# 8번
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)



# 9번 리스트의 합은?
i = 0
add = 0
a = [1, 2, 3, 4, 5]

while i < len(a):
    add += a[i]
    i += 1

print(add)     # 다른 방법으로는

num = [1, 2, 3, 4, 5]
num_add = sum(num)
print(num_add)



# 10번 리스트 데이터의 갯수 구하기
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print("cook 리스트의 갯수는 %d" % len(cook))



# 11번 리스트의 평균 (위에 구했던 '합과 갯수' 활용)
average = add / len(a)
print(average)




# 12번 print(3 == 5)의 결과 : 3은 5와 같지 않으니 False 예상
print(3 == 5)



# 13번 print(3 < 5) 결과 : 3은 5보다 작으니 True 예상
print(3 < 5)



# 14번 x = 4, print(1 < x < 5) 결과 : x에 들어있는 4는 1과 5 사잇값이 맞으니 True 예상
x = 4
print(1< x < 5)



# 15번 print((3 == 3) and (4 != 3)) 결과 : 3은 3인 동시에 4는 3이 아니므로 True 예상
print((3 == 3) and (4 != 3))

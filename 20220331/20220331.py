# 1번

price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(f"{i} {price_list[i]}")





# 2번
j = 1
for i in range(100, 121, 10):
    print(f"{i} {price_list[j]}")
    j += 1





# 3번
print("월드컵 개최 년도 :", end = " ")
for i in range(2002, 2051, 4):
    print(i, end = ", ")





# 4번
arr = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in arr:
    print(i)



# 5번
ticker = 'btc_krw'
print(ticker.upper())



# 6번

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))



# 7번
a = "hello world"
print(a.split(" "))



# 8번
date = "2020-05-01"
date2 = date.split("-")
print(f"{date2[0]}년 {date2[1]}월 {date2[2]}일")





# 9번
상장주식수 = "5, 969, 782, 550"
change = int(상장주식수.replace(",","").replace(" ", ""))
print(change)







# 10번
a = "hello world"
print(a.split(" "))






#12 번
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1:10:2])






# 13번
list = [3, 100, 23, 44]
for i in range(len(list)):
   if list[i] % 3 == 0:
        print(list[i])

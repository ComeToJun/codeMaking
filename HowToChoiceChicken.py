from collections import Counter
import math

pickChicken = ['마늘', '마늘', '순살양념', '순살양념', '순살양념', '양념', '순살양념', '마늘', '순살고추양념', '순살양념', '순살양념', '순살고추양념', '순살양념', '순살고추양념', '후라이드', '순살양념']
total = len(pickChicken)
c = Counter(pickChicken)
print(c)
TotalChicken = 7
sum = 0

for i, menu in c.items():

    print()
    ratio = menu / total
    result = ratio * TotalChicken
    print(f"{i}을(를) [예상 필요 치킨] {TotalChicken}마리 에서 {result}마리 주문하면 됩니다")

    result = math.ceil(result)
    print(f"올림한 {i}은 치킨은 **{result}마리** 주문하면 됩니다.")
    sum += result

print()
print("*******************************************")
print(f"모두를 충족시킬 수 있는 치킨 마리수는 {sum} 입니다")
print(f"최종결과 = 메뉴의 중복성을 감안하고, 7마리만 주문하기 위해 전)반장님의 양념 -> [순살양념]\n"
      f" 마늘 2마리 ->[1마리] 순살양념 4마리 -> [3마리] 로 하겠습니다.")

print("-----------------------------------------------------------")
print("마늘 [1마리]")
print("순살양념 [3마리]")
print("순살고추양념 [2마리]")
print("후라이드 [1마리]")
print("--------------------------------------------------------------")
print("결과에 의문이 있으신 분은 실력 향상을 위해 파이썬으로 질문해 주시길 바랍니다(찡긋)")

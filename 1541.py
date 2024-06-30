# 음수로 만들 수 있는 경우
# 음수로 만들 수 없는 경우
    # 마이너스가 아직 나오지 않았을 때,
import re
p = re.compile("[\d]{1,}|[\+\-]{1}")
S = input()
arr = p.findall(S)
can_convert = False
summ = 0
for elem in arr:
    if elem == '+':
        pass
    elif elem == '-':
        can_convert = True
    else:
        num = int(elem)
        if can_convert:
            summ -= num
        else:
            summ += num
print(summ)


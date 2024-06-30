def find_croatia(s: str):
    # 'dz=' 가 'z='보다 앞에 와야 함.
    cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for i in cro_alpha:
        find_idx = s.find(i)
        if find_idx != -1:
            return i
    return ''


line = input()
a, b, cnt = 0, 0, 0
target = ''
while b <= len(line):
    target = line[a:b]
    word = find_croatia(target)
    if word:
        a = b
        cnt += len(target) - len(word) + 1
    b += 1
print(cnt + len(line[a:b]))

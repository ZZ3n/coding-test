word = input().upper()
modeAsc = sorted({*word, '?'}, key=word.count)
*others, b, a = modeAsc
isNotBimodal = word.count(b) < word.count(a)
print(-isNotBimodal)
print(modeAsc[-isNotBimodal])

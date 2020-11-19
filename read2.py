data =[]
count = 0
with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		count += 1
		if count % 1000 == 0 :    # % 是用來求餘數 ＃ 7 % 3 = 1
			print(len(data))
print('檔案讀取完，共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new), '筆留言長度小於100')
print(new[0])

good = [d for d in data if 'good' in d ]

print('一共有', len(good), '筆留言提到good')
print(good[0])


bad = ['bad' in d for d in data]
print(bad)


#文字計數
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1


for word in wc:
	if wc[word] > 100:
		print(word, wc[word])


print(len(wc))


while True:
	word = input('請輸入想查詢的字')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('查無此字')
		
print('感謝使用本查詢功能')
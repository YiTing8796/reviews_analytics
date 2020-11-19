data = []
def read_file(filename):
	with open(filename, 'r') as f:
		for line in f:
			data.append(line)
	return data

def word_count(data):
	wc = {}
	for d in data:
		words = d.split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	return wc


def list_print(dic):
	for word in wc:
		if wc[word] > 100:
			print(word, wc[word])


def look_up(word):
	while True:
		word = input('請輸入想查詢的字')
		if word == 'q':
			break
		if word in wc :
			print(word, '出現過的次數為', wc[word])
		else:
			print('查無此字')

	print('感謝使用本查詢功能')


def main():
	read_file('review.txt')
	word_count(data)
	list_print(wc)
	look_up()


main()	







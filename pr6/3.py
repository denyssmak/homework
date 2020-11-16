#через функию  map прореряем количество слов в gg.txt
from collections import Counter
f = open("gg.txt", "r", encoding='UTF-8') 
for str1 in f: 
	str1 = str1.lower()

	def words(str1):
 		return Counter(map(str, str1.split()))
	print(words(str1))
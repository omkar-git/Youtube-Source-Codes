from textblob import TextBlob
def Convert ( string):
	li = list (string. split ())
	return li
strl = input ("Enter your word ")
Words = Convert (str1)	
corrected_words = []
for i in words:
	corrected_words.append (Text8lob (i))
print ("Wrong words: ", Words)
print(" Corrected Words are: ")
for i in corrected_words :
	print (i.correct (), end ="")
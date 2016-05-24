import string
'''
text="The narwhal bacons at midnight."
print ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
'''

text=text.replace(" ","")
let=[]
text=text.translate(None,string.punctuation)
text=text.lower()
for i in text:
    letter=string.lowercase.index(i)+1
    let.append(letter)

str=' '.join(str(e) for e in let)
print str

#replaces each letter with its order in the alphabet
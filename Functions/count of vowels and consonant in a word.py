word=input("Enter any word:")

def word_count(word):
  v= 0
  c=0
  for k in word:
      if(k=='a' or k=='e' or k=='i' or k=='o' or k=='u'or k=='A' or k=='E' or k=='I' or k=='O' or k=='U'):
        v=v+1
      else:
        c=c+1
  print("Vowels in the word:",v)
  print("Consonants in the word:",c)
word_count(word)


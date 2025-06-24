# 8. Given a start word, end word, and a list of valid words, find the mininmum number of steps to
#  transform the word to the end word by changing one letter at a time, where each intermediate word 
# must be in the list. All words are same length, lowercase. Example: start"hot", end="cog",
#  wordlist=["hot","dot","dog",log","lot","cog"] → 5(hit → hot → dot → dog → cog), Return 0 if impossible.

start=input("Enter start word: ")
end=input("Enter end word: ")
wordlist=input("Enter word list comma separated: ").split(',')

if end not in wordlist:
  print(0)
else:
    queue=[(start,1)]
    visit=set()

    while queue:
      current, steps = queue.pop(0)

      for word in wordlist:
         if word in visit:
          continue

         diff=0
         for j in range(len(current)):
           if current[j] != word[j]:
             diff+=1

         if diff==1:
             if word==end:
               print(steps + 1)
               exit()
             queue.append((word, steps + 1))
             visit.add(word)
    print(0)
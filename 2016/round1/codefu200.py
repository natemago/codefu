def mostPopular(ts):
  hashtags = {}
  for tweet in ts:
    words = tweet.split(' ')
    th = set()
    for w in words:
      if w[0] == '#':
        th.add(w.lower())
    for hashtag in th:
      if hashtags.get(hashtag):
        hashtags[hashtag] += 1
      else:
        hashtags[hashtag] = 1
  hashtags = [(key, val) for key,val in hashtags.items()]
  hashtags = sorted(sorted(hashtags, key=lambda n: n[0]), key=lambda n:n[1], reverse=True)
  return hashtags[0][0]

#Test Case 1:
print( mostPopular(["The quick brown #fox jumps over the lazy #dog","#Fox with the best shows on #tv","#Dog finds a #fox and barks at another #dog"]) )



#Test Case 1:
assert  mostPopular(["The quick brown #fox jumps over the lazy #dog","#Fox with the best shows on #tv","#Dog finds a #fox and barks at another #dog"]) == "#fox"

#Test Case 2:
assert  mostPopular(["#jnf Fcif ql sfopj","Mjiy #gtnt ut pfnv","ql #gtnt Mjiy Nuetc pfnv pfnv Vfkbw Mjiy #hdynu xu","Nuetc Nuetc ql #gtnt Xcd Nuetc"]) == "#gtnt"

#Test Case 3:
assert  mostPopular(["#jnf #jnf Vfkbw ql Xcd","sfopj ut Mjiy ql Fcif Xcd sfopj ql #gtnt","pfnv Fcif #Nudnoz sfopj Nuetc Xcd Mjiy Vfkbw #hdynu Mjiy Mjiy"]) == "#gtnt"

#Test Case 4:
assert  mostPopular(["sfopj xu Nuetc #Nudnoz Mjiy ut xu","pfnv Mjiy #gtnt sfopj sfopj sfopj Nuetc sfopj #jnf Xcd ql xu","sfopj ut ut ut Fcif #jnf xu Fcif","xu Fcif #Nudnoz Nuetc Fcif Fcif Mjiy Fcif Vfkbw ql"]) == "#jnf"

#Test Case 5:
assert  mostPopular(["Vfkbw ut ut Vfkbw sfopj ql #jnf sfopj xu","xu ql ql Mjiy sfopj xu #hdynu #Wkfhf ut","#hdynu Fcif Mjiy #Nudnoz Mjiy xu Mjiy xu"]) == "#hdynu"

#Test Case 6:
assert  mostPopular(["Xcd #jnf Mjiy Mjiy ut Vfkbw ut #hdynu xu Vfkbw","#jnf Nuetc #gtnt sfopj Vfkbw Nuetc","#Wkfhf xu xu Mjiy Mjiy pfnv ql Nuetc","sfopj Mjiy Fcif Mjiy sfopj #Nudnoz Nuetc"]) == "#jnf"

#Test Case 7:
assert  mostPopular(["pfnv Vfkbw Fcif Nuetc Vfkbw #Nudnoz","Xcd ut Fcif pfnv sfopj pfnv #Wkfhf Fcif","#gtnt sfopj pfnv ql xu Vfkbw","Fcif ql Nuetc #jnf Nuetc sfopj Vfkbw ql Fcif Vfkbw"]) == "#gtnt"

#Test Case 8:
assert  mostPopular(["Xcd #hdynu Mjiy pfnv ut xu Nuetc pfnv Mjiy #jnf","ql ut ql Nuetc sfopj Mjiy pfnv Xcd Fcif pfnv #jnf","#Wkfhf Vfkbw sfopj Mjiy ql xu","#gtnt Xcd Xcd xu #gtnt pfnv ql ql"]) == "#jnf"

#Test Case 9:
assert  mostPopular(["Fcif ut #gtnt Nuetc xu","#Nudnoz #jnf Mjiy Fcif ql pfnv Nuetc xu ut Xcd Mjiy ql","xu ut ut ql pfnv #jnf ut ut Nuetc pfnv","ql Mjiy ql #jnf Vfkbw xu sfopj Nuetc"]) == "#jnf"

#Test Case 10:
assert  mostPopular(["Mjiy #Nudnoz #jnf pfnv sfopj Vfkbw Xcd Xcd sfopj Mjiy","#hdynu Mjiy xu ql #Nudnoz","Vfkbw ql Mjiy #hdynu xu #jnf","#Nudnoz xu ql pfnv pfnv","#gtnt Nuetc ql #jnf pfnv"]) == "#jnf"


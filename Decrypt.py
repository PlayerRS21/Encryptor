word = input("Enter Your Word to decode it. ")

#          $^$$@#)*!#@)#&!@#%

random_characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

subsituation = [")","!","@","#","$","%","^","&","*","(",")"]

lv1_word = ""

# for i in range (4,len(word)-4):
#     lv1_word = lv1_word + str(word[i])

# print(lv1_word) #trimed word

for i in range(0,len(word)):
    lv1_word = lv1_word + str(subsituation.index(word[i]))

# print(lv1_word)  # numword  =  4644 {23 08 13 20 37} 1235

newword = ""

for i in range(4,len(lv1_word)-4):
    newword = newword + lv1_word[i]

# print(newword) #Trimmed Word 23 08 13 20 37

numword = [newword[i:i+2] for i in range(0, len(newword),2)]

# print(numword)

lastword=""

for i in range(0,len(numword)): #  ['23', '08', '13', '20', '37']
    if int(numword[i][0]) == 0:
        lastword += random_characters[int(numword[i][1])]
    else:
        lastword += random_characters[int(numword[i])]

# print(lastword)

final_word = ""

final_word += lastword[-1]
for i in range(1,len(lastword)-1):
    final_word += lastword[i]

final_word += lastword[0]

print(final_word)
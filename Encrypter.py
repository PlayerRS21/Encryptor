import random
word = input("Enter Your Word to encode it. ")

random_characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

subsituation = [")","!","@","#","$","%","^","&","*","(",")"]

# for i in range(10):
#     print(subsituation[i])

newword = ""
newword = word[-1]
for i in range(1,len(word)-1):
    newword = newword+word[i]

newword = newword + word[0]
# print(newword)
randomword = f"{random.choice(random_characters)}{random.choice(random_characters)}{newword}{random.choice(random_characters)}{random.choice(random_characters)}"
# print(randomword)

numword = ""

for i in range(0,len(randomword)):
    if randomword[i] in random_characters:
        if random_characters.index(randomword[i])<10:
            numword = numword +"0"+ str(random_characters.index(randomword[i]))
        else:
            numword = numword + str(random_characters.index(randomword[i]))

# print(numword)

final_word = ""
for i in range (0,len(numword)):
    value=int(numword[i])
    final_word = f"{final_word}{subsituation[value]}"

print(final_word)

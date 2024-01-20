secretanswer = "Amr"
answer = ""
count = 1
limit = 3

while secretanswer != answer  and  count <= limit :
    answer = input("your name ? ")
    if secretanswer != answer and  count < limit:
        print("try again")
    if secretanswer == answer :
        print ("you win ")
        break
    count +=1
    
if count > limit:
    print ("you lossssse")
        
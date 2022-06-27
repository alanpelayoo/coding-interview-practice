#https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=internal-search

        
def lookup(word,string_i):
    len_w = len(word)
    count =0
    for w in range(len(string_i)):
        if string_i[w] == word[0] and w+len_w <= len(string_i):
            word2 =string_i[w]
            for i in range(1,len_w):
                word2 = word2+string_i[w+i]
            if word2 == word:
                count +=1
    return count

def sols(arr, stringg):
    
    sol = []
    for a in arr:
        substr=""
        for i in range(stringg.index(a),len(stringg)):
            substr=substr+stringg[i]
            sol.append(substr)
    return sol
def retrieveWords(string):
    vowels_l = ["A","E","I","O","U"]
    kevin = []
    stuart =[]
    for letter in string:
        if letter in vowels_l:
            if letter not in kevin:
                kevin.append(letter)
        else:
            if letter not in stuart:
                stuart.append(letter)
    return kevin,stuart



def main(string_i):

    kevin_bw,stuart_bw = retrieveWords(string_i)


    stuart_words= sols(stuart_bw,string_i)
    kevin_words =sols(kevin_bw,string_i)

    sols_k = {}
    sols_s = {}
    total_k =0
    total_s =0
    for w in kevin_words:
        sols_k[w] = lookup(w,string_i)
        total_k = lookup(w,string_i) + total_k
    for w in stuart_words:
        sols_s[w] = lookup(w,string_i)
        total_s = lookup(w,string_i) + total_s
    
    print(sols_k)
    print(sols_s)
    if total_k > total_s:
        print("Kevin",total_k)
    elif total_s > total_k:
        print("Stuart",total_s)

main("ANANAS")
# print(sols_k)
# print(total_k)
# print(sols_s)
# print(total_s)






    
    
import json as j
import difflib as d
useryn="y"
#load json data into program
data=j.load(open("data.json",'r'))
def meaning(w):
    w=w.lower()
    if w in data:
        return(data[w])
    elif len(d.get_close_matches(w,data.keys(),cutoff=0.8))>0:
        yn=input("did you mean "+str(d.get_close_matches(w,data.keys())[0])+"?"+" press y for yes and n for no\n")
        if yn=="y":
            return(data[d.get_close_matches(w,data.keys(),cutoff=0.8)[0]])
        else:
            return "word is not found please double check it"
    elif w.capitalize() in data:
        return data[w.capitalize()]
    else:
        return "word is not found!"           


while useryn=="y":
    word=input("ENTER THE WORD:")
    output=(meaning(word))
    if type(output)==list:
        for i in output:
            print(i)
    else:
        print(output)
    useryn=input("do you want to such for 1 more word?  press y yes and n for no\n")  
input("press any key to exit from dicnary\n")
import difflib 

    
    
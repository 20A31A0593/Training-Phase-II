#To check if the paranthesis is balanced

s=input()
stack=[]
f=0
for i in range(len(s)):
    if(s[i]=="("):
        if(i==len(s)-1):
            print("String is unbalanced")
            f=1
            break
        else:
            stack.append(s[i])
    elif(s[i]==")"):
        if(i==0):
            print("String is unbalanced")
            f=1
            break
        else:
            if(len(stack)==0):
                print("String is unbalanced")
                f=1
                break
            else:
                stack.pop()
if(len(stack)>0):
    print("String is unbalanced")
elif(f!=1):
    print("String is balanced")

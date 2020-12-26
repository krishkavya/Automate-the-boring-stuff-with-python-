def new_spam(list):
    for i in range(0,len(list)):
        if list[i]!=list[-1]:
            list[i]=list[i]+','
        else:
            list[i]='and '+list[i]
        print(list[i],end=" ")
spam = ['apples', 'bananas', 'tofu', 'cats']
new_spam(spam)


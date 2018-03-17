from textblob import TextBlob
f=open('database.txt','r')
i=0;
subject=[]
dict1={}
dict2={}
a=f.read()
f.close()
val=a.split('$')
while(i<len(val)-1):
	subject=val[i].split(':')
	dict1[subject[0]]=TextBlob(subject[1]).sentiment.polarity
	dict2[subject[0]]=TextBlob(subject[2]).sentiment.polarity
	i=i+1
print(dict1)
print(dict2)
print(val)
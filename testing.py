n=int(input('Enter the number of students'))
f2=open("review2.txt",'w+')
l=['Engineering Physics','Engineering Chemistry','Basics of Electronics and Communication','Engineering Graphics','Engineering Mechanics','Basics of Electrical Engineering','Introduction to computation and Problem Solving','C Programming','Differential Equations','Calculus','Design and Engineering','Introduction to Sustainable Engineering']
for i in range(n):
	for j in range(2):
		print("Enter review about your {} class".format(l[j])) 
		p_review1=input()
		print("enter the name of the teacher")
		p_tea=input()
		f=open(p_tea+'.txt','a+')
		f.write(p_review1)
		f.write("\n")
		f.close()
		print("enter the review about {}".format(l[j]))
		p_review2=input()
		print("What are you really interested in\n1.theory classes\n2.practical classes")
		choice=int(input('Enter the preference'))
		if choice==1:
			prefer="theory"
		else:
			prefer="practical"
		f2.write(l[j])
		f2.write(":")
		f2.write(p_review1)
		f2.write(":")
		f2.write(p_tea)
		f2.write(":")
		f2.write(p_review2)	
		f2.write(":")
		f2.write(prefer)
		f2.write("$")
		
f2.close()
from textblob import TextBlob
f=open('review2.txt','r')
i=0
subject=[]
dict1={}
dict2={}
wholelist=[]
studentlist=[]
a=f.read()
f.close()
val=a.split('$')
for j in range (n):
	wholelist.append([])
	while(i<len(val)-1):
		subject=val[i].split(':')
		dict1[subject[0]]=[]
		dict1[subject[0]].append(TextBlob(subject[1]).sentiment.polarity)
		dict1[subject[0]].append(subject[2])
		dict2[subject[0]]=TextBlob(subject[3]).sentiment.polarity
		i=i+1
	wholelist[j].append(dict1)
	wholelist[j].append(dict2)

print(wholelist)

def feedback():
	teacherlist=[]
	teachersentiment={}
	#n=int(input('Enter the number of students'))
	f2=open("review2.txt",'w+')
	l=['Engineering Physics','Engineering Chemistry','Basics of Electronics and Communication','Engineering Graphics','Engineering Mechanics','Basics of Electrical Engineering','Introduction to computation and Problem Solving','C Programming','Differential Equations','Calculus','Design and Engineering','Introduction to Sustainable Engineering']
	for j in range(12):
		print("Enter review about your {} class".format(l[j])) 
		p_review1=input()
		print("enter the name of the teacher")
		p_tea=input()
		teacherlist.append(p_tea)
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
	while(i<len(val)-1):
		subject=val[i].split(':')
		dict1[subject[0]]=[]
		dict1[subject[0]].append(TextBlob(subject[1]).sentiment.polarity)
		dict1[subject[0]].append(subject[2])
		dict2[subject[0]]=TextBlob(subject[3]).sentiment.polarity
		i=i+1
	for i in range(len(teacherlist)):
		e=open(teacherlist[i]+'.txt','r')
		p=e.read()
		j=TextBlob(p)
		tsent=j.sentiment.polarity
		teachersentiment[teacherlist[i]]=tsent
	e.close()
	print(teachersentiment)
	for i in dict1.keys():
		print(i,dict1[i])
	for i in dict2.keys():
		print(i,dict2[i])
def login():
	print("\t\t\tusername:")
	username=input()
	print("\n\t\t\t")
	password=getpass()
	f3=open("confi.txt","r")
	str1=f3.read()
	str1=str1.replace("\n"," ")
	str1=str1.replace("\t"," ")
	l=str1.split(" ")
	for i in range(0,len(l),2):
		if l[i]==str(username):
			if l[i+1]==password:
				print("hello")
				feedback()
			else:
				print("sorry invalid username")
	f3.close()
from getpass import getpass
print("\n\t\t\t\t1.login\n\t\t\t\t2.register\n\t\t\t\t3.exit\n")
x=int(input())
if x==1:
	login()
elif x==2:
	print("\t\t\tusername:")
	username=input()
	print("\n\t\t\t")
	password=getpass()
	f3=open("confi.txt","a+")
	f3.write(str(username))
	f3.write("\t")
	f3.write(str(password))
	f3.write("\n")
	f3.close()
	login()
else:
	exit()


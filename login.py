def feedback():
	teacherlist=[]
	teachersentiment={}
	#n=int(input('Enter the number of students'))
	f2=open("review2.txt",'w+')
	l=['Engineering Physics','Engineering Chemistry','Basics of Electronics and Communication','Engineering Graphics','Engineering Mechanics','Basics of Electrical Engineering','Introduction to computation and Problem Solving','C Programming','Differential Equations','Calculus','Design and Engineering','Introduction to Sustainable Engineering']
	for j in range(3):
		os.system("cls")
		print("\n\n\n\t\tEnter review about your {} class".format(l[j])) 
		p_review1=input()
		os.system("cls")
		print("\n\n\n\t\tenter the name of the teacher")
		p_tea=input()
		teacherlist.append(p_tea)
		f=open(p_tea+'.txt','a+')
		f.write(p_review1)
		f.write("\n")
		f.close()
		os.system("cls")
		print("\n\n\n\t\tenter the review about {}".format(l[j]))
		p_review2=input()
		os.system("cls")
		print("\n\n\n\t\tWhat are you really interested in\n\t\t\t1.theory classes\n\t\t\t2.practical classes")
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
	print("press any key")
	g=input()
	os.system("cls")
	print("\n\t\t\t\tRECOMMENDED COUSES FOR YOU")
	for i in dict2.keys():
		if(dict2[i]>0.3):
			if(i==l[0]):
				print("\n\n\n\t\t\tparticle physics\n\t\t\tquantum physics\n\t\t\tastro physics\n\t\t\tdark matter and dark energy")
			elif(i==l[1]):
				print("\n\n\n\t\t\tAdvanced chemistry\n\t\t\torganic chemistry\n\t\t\tmolecular spectroscopy\n")
			elif(i==l[2]):
				print("\n\n\n\t\t\tAdvanced communication system\n\t\t\tWireless communications\n\t\t\tComplex network designing\n")
			elif(i==l[3]):
				print("\n\n\n\t\t\tAdvanced machine drawing\n\t\t\t3D designing\n\t\t\tComplex CAD designing")
			elif(i==l[4]):
				print("\n\n\n\t\t\tStudy of mechanics in microgravity\n\t\t\textreme temperature mechanics\n\t\t\tmechanics of celestial objects\n")
			elif(i==l[5]):
				pirnt("\n\n\n\t\t\tAdvanced circuit designing\n\t\t\tChip designing\n\t\t\tAdvanced study in semiconductors\n")
			elif(i==l[6]):
				print("\n\t\t\tGraph theory\n\t\t\tArificial intelligence\n\t\t\tData science\n")
			elif(i==l[7]):
				print("\n\t\t\tOperating system designing\n\t\t\tLanguage development\n\t\t\tPattern recongnition\n")
			elif(i==l[8]):
				print("\n\t\t\tApplied mathematics\n\t\t\tAdvanced Linear algebra\n\t\t\tScientific proofing\n")
			elif(i==l[9]):
				print("\n\n\n\t\t\tAdvanced Calculus\n\t\t\tEvent reasoning with calculus\n\t\t\t")
			elif(i==l[10]):
				print("\n\t\t\tSustainable designing\n\t\t\tAdvanced transportation systems\n\t\t\tDesigning cities\n")
			elif(i==l[11]):
				print("\n\t\t\tImpacts of natural disasters\n\t\t\tDeep study in global warming\n\t\t\tPollution control\n")

	print("press any key")
	f=input()
	os.system("cls")
	print("\n\n\n\n\n\t\t\tThank you for using the feedback system")
	d=input()
	mainmenu()
def login():
	os.system("cls")
	username=input("\n\n\n\n\n\nUsername: ")
	password=getpass()
	f3=open("confi.txt","r")
	str1=f3.read()
	str1=str1.replace("\n"," ")
	str1=str1.replace("\t"," ")
	l=str1.split(" ")
	for i in range(0,len(l),2):
		if l[i]==str(username):
			if l[i+1]==password:
				feedback()
			else:
				print("sorry invalid username")
				login()	
	f3.close()
def mainmenu(): 
	os.system("cls")
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
import os
from getpass import getpass
mainmenu()
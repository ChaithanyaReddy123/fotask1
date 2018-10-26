import random
x=["rock","paper","scissor"]
max_score=5
p=0
q=0
while(True):
	a=input()
	b=random.randint(0,2)
	c=x[b]
	print(c)
	if(a==c):
		p=p
		c=c
		print("person score is " + str(p))
		print("computer score is " + str(q))
	if(a=="rock"):
		if(b==1):
			q=q+1
			print("person score is " + str(p))
			print("computer score is " + str(q))
		elif(b==2):
			p=p+1
			print("person score is " + str(p))
			print("computer score is " + str(q))
	if(a=="paper"):
		if(b==0):
			p=p+1
			print("person score is " + str(p))
			print("computer score is " + str(q))
		elif(b==2):
			q=q+1
			print("person score is " + str(p))
			print("computer score is " + str(q))
	if(a=="scissor"):
		if(b==0):
			q=q+1
			print("person score is " + str(p))
			print("computer score is " + str(q))			
		elif(b==1):
			p=p+1
			print("person score is " + str(p))
			print("computer score is " + str(q))
	if(p==max_score):
		print("person won")
		break
	elif(q==max_score):
		print("computer won")
		break


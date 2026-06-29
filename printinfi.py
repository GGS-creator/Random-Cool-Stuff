import subprocess
import os
import time
import sys
global text
class node():
	def __init__(self,val):
		self.val=val
		self.next=None
		self.prev=None
		self.num=None

def insert(head,data):
	new_node=node(data)
	if head is None:
		new_node.num=0
		return new_node
	current=head
	while current.next:
		current=current.next
	
	current.next=new_node
	new_node.prev=current
	new_node.num=current.num + 1
	
	return head
	
def display(head):
	current=head
	while current:
		print(current.num)
		subprocess.run(f'figlet -c {current.val} | lolcat',shell=True)
		current=current.next
	current=head
	while current:
		print(current.num, current.val)
		current=current.next
	print("None")

def deleteat(head,position):
	if head is None:
		print("empty")
		return head
	if position < 0:
		print("invalid")
		return head
	if position==0:
		if head.next:
			head.next.prev=None
		return head.next
	current=head
	count=0
	while current and count<position:
		current=current.next
		count+=1
	if current is None:
		print("Position out of range")
		return head
		
	if current.next:
		current.next.prev=current.prev
	if current.prev:
		current.prev.next=current.next
		
	del current
	return head
		
def printp(n,head):
	current=head
	
	while current :
		if current.num==n:
			subprocess.run(f'figlet -c {current.val} | lolcat',shell=True)
			return
		current=current.next
	
def midcheck(head):
	global text
	text=input("Enter text to type:")
			
	if text=="exit":
		print("Byeee miss you")
		sys.exit(0)	
	elif text=="showall":
		display(head)
		midcheck(head)
		
	elif text=="deldis":
		num=int(input("Enter the text number to delete"))
		head=deleteat(head,num)
		midcheck(head)
		
	elif text=="printp":
		num=int(input("Enter position:"))
		printp(num,head)
		midcheck(head)
		
	elif text=="man":
		print("exit-for exit loop\nshowall-to show all the previous words\ndeldis-delet the specific word in the list\nprintp-prints the word in the position...\nThis is created by Gagan G Saralaya to print cool shit continuously by taking input from users...")
		midcheck(head)
		sys.exit(0)
	elif text=="editcode":
		subprocess.run("mousepad printinfi.py")
		midcheck(head)
	return head

if __name__=="__main__":
	head=None
	
	while True:	
		head=midcheck(head)
		head=insert(head,text)	
		subprocess.run(f'figlet -c {text} | lolcat',shell=True)
		
		time.sleep(1)
		

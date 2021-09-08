import socket
from tkinter import *
count=0
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client.connect(('localhost',6999))
data = client.recv(1024)
print(data.decode())
color=(data.decode().split()[2])
def paint(x,y,color) :
	x1,y1=x*30-7,y*30-7
	x2,y2=x*30+7,y*30+7
	w.create_oval(x1,y1,x2,y2,fill=color)
	root.update()

def send_message(event) :
	data = client.recv(1024)
	print(data.decode())
	msg=str(event.x)+' '+str(event.y)
	client.send(msg.encode('utf-8'))
	data = client.recv(1024)
	if data.decode()== 'OK' : 
		print(data.decode())
	else :
		print(data.decode())
	data = client.recv(1024)
	data=data.decode()
	x=int(data.split()[0])
	y=int(data.split()[1])
	color=(data.split()[2])
	paint(x,y,color)
	data = client.recv(1024)
	print(data.decode())
	if data.decode()[0]=='Y':
		client.close()
	data = client.recv(1024)
	data=data.decode()
	x=int(data.split()[0])
	y=int(data.split()[1])
	color=(data.split()[2])
	paint(x,y,color)
	data = client.recv(1024)
	print(data.decode())
	if data.decode()[0]=='Y':
		client.close()
	

		
root = Tk()
root.title("Gomoku")
root.geometry('700x600')

w=Canvas(root,width=600,height=600,background="white") 
w.pack(side=TOP)

for i in range(1,20):
	w.create_line(i*30,30,i*30,570,width=2)
for i in range(1,20):
	w.create_line(30,i*30,570,i*30,width=2)

w.create_oval(115,115,125,125,fill="black")
w.create_oval(295,115,305,125,fill="black")
w.create_oval(505,115,515,125,fill="black")
w.create_oval(115,295,125,305,fill="black")
w.create_oval(295,295,305,305,fill="black")
w.create_oval(505,295,515,305,fill="black")
w.create_oval(115,505,125,515,fill="black")
w.create_oval(295,505,305,515,fill="black")
w.create_oval(505,505,515,515,fill="black")
w.pack(expand=YES, fill=BOTH)
if count==0:
	root.update()
if color=='white' and count==0:
	data = client.recv(1024)
	print(data.decode())
	data=data.decode()
	x=int(data.split()[0])
	y=int(data.split()[1])
	color=(data.split()[2])
	paint(x,y,color)
	data = client.recv(1024)
	print(data.decode())
	
w.bind("<Button-1>",send_message)


root.mainloop()




		




 



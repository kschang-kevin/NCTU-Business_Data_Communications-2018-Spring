import socket
import time
def win(color) :
	for i in range (0,18) :
		for j in range (0,18) :
			if board[i*19+j] == color :
				if j+1<20 and j+2<20 and j+3<20 and j+4<20 :
					if board[i*19+j+1] == color and board[i*19+j+2] == color and board[i*19+j+3] == color and board[i*19+j+4] == color :
						if color == 1 :
							msg = 'You win'
							connA.send(msg.encode('utf-8'))
							msg = 'You lose'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
						if color == 2 :
							msg = 'You lose'
							connA.send(msg.encode('utf-8'))
							msg = 'You win'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
				if i+1<20 and i+2<20 and i+3<20 and i+4<20 :
					if (board[(i+1)*19+j] == color and board[(i+2)*19+j] == color and board[(i+3)*19+j] == color and board[(i+4)*19+j] == color) : 
						if color == 1 :
							msg = 'You win'
							connA.send(msg.encode('utf-8'))
							msg = 'You lose'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
						if color == 2 :
							msg = 'You lose'
							connA.send(msg.encode('utf-8'))
							msg = 'You win'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
				if j+1<20 and j+2<20 and j+3<20 and j+4<20 and i+1<20 and i+2<20 and i+3<20 and i+4<20:	
					if (board[(i+1)*19+j+1] == color and board[(i+2)*19+j+2] == color and board[(i+3)*19+j+3] == color and board[(i+4)*19+j+4] == color) :
						if color == 1 :
							msg = 'You win'
							connA.send(msg.encode('utf-8'))
							msg = 'You lose'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
						if color == 2 :
							msg = 'You lose'
							connA.send(msg.encode('utf-8'))
							msg = 'You win'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
				if j+1<20 and j+2<20 and j+3<20 and j+4<20 and i-1>1 and i-2>0 and i-3>0 and i-4>0:		
					if (board[(i-1)*19+j+1] == color and board[(i-2)*19+j+2] == color and board[(i-3)*19+j+3] == color and board[(i-4)*19+j+4] == color) :
						if color == 1 :
							msg = 'You win'
							connA.send(msg.encode('utf-8'))
							msg = 'You lose'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
						if color == 2 :
							msg = 'You lose'
							connA.send(msg.encode('utf-8'))
							msg = 'You win'
							connB.send(msg.encode('utf-8'))
							time.sleep(1)
							connA.close()
							connB.close()
	msg = 'Continue'
	connA.send(msg.encode('utf-8'))
	connB.send(msg.encode('utf-8'))
							
	
board = [0 for _ in range(400)]
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6999)) 
server.listen(2)
connA,addrA = server.accept()
connB,addrB = server.accept()
msg = 'You are black'
connA.send(msg.encode('utf-8'))
msg = 'You are white'
connB.send(msg.encode('utf-8'))
while True:
	msg = 'Your turn'
	connA.send(msg.encode('utf-8'))
	while True :
		data = connA.recv(1024)
		print(data.decode())
		x=int(data.split()[0])
		y=int(data.split()[1])
		if x % 30>15 and y % 30>15:
			x,y=int(x/30)+1,int(y/30)+1
		elif x % 30<15 and y % 30>15:
			x,y=int(x/30),int(y/30)+1
		elif x % 30>15 and y % 30<15:
			x,y=int(x/30)+1,int(y/30)
		elif x % 30<15 and y % 30<15:
			x,y=int(x/30),int(y/30)
		if x < 20 and y < 20 :
			if board[x*19+y] == 0 :
				msg = 'OK'
				board[x*19+y] = 1
				connA.send(msg.encode('utf-8'))
				break
			else :
				msg = 'Illegal'
				connA.send(msg.encode('utf-8'))
				msg = 'Again'
				connA.send(msg.encode('utf-8'))
		else :
			msg = 'Illegal'
			connA.send(msg.encode('utf-8'))
			msg = 'Again'
			connA.send(msg.encode('utf-8'))
	msg = str(x)+' '+str(y)+' black'
	connA.send(msg.encode('utf-8'))
	connB.send(msg.encode('utf-8'))
	time.sleep(1)
	win(1)
	time.sleep(1)
	msg = 'Your turn'
	connB.send(msg.encode('utf-8'))
	while True :
		data = connB.recv(1024)
		print(data.decode())
		x=int(data.split()[0])
		y=int(data.split()[1])
		if x % 30>15 and y % 30>15:
			x,y=((int)(x/30)+1),((int)(y/30)+1)
		elif x % 30<15 and y % 30>15:
			x,y=((int)(x/30)),((int)(y/30)+1)
		elif x % 30>15 and y % 30<15:
			x,y=(((int)(x/30)+1)),((int)(y/30))
		elif x % 30<15 and y % 30<15:
			x,y=((int)(x/30)),((int)(y/30))
		if x < 20 and y < 20 and x > 0 and y > 0:
			if board[x*19+y] == 0 :
				msg = 'OK'
				board[x*19+y] = 2
				connB.send(msg.encode('utf-8'))
				break
			else :
				msg = 'Illegal'
				connB.send(msg.encode('utf-8'))
				msg = 'Again'
				connB.send(msg.encode('utf-8'))
		else :
			msg = 'Illegal'
			connB.send(msg.encode('utf-8'))
			msg = 'Again'
			connB.send(msg.encode('utf-8'))
	msg = str(x)+' '+str(y)+' white'
	connA.send(msg.encode('utf-8'))
	connB.send(msg.encode('utf-8'))
	time.sleep(1)
	win(2)
	time.sleep(1)
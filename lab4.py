import MySQLdb

db=MySQLdb.connect('localhost','root','','reservation')
cur=db.cursor()


cur.execute("Select * from username")
data=cur.fetchall()
print (data)

def bookingextralarge():

	name = input('Your name : ')

	time = input('Your time : ')

	vip={}

	

	if (vip):

	  for x in vip:

	    if x==time:

	      print( "Time already taken")

	    else: 

	      vip[name]=time

	      print ("Your table has been reserved under %s" %name)

	      s=vip[name]

	      print ("Your booking time is %d" %s)

	else:

	  vip[name]=time

	  print ("Your table has been reserved under %s" %name)

def small():

	a=11.00 

	b=11.00 

	c=11.00

	d=11.00
	

	while (a <= 22.0):

	  name = input('Your name : ')
	  cur.execute("INSERT INTO small_1(UserName) Values('name','a')")
	  db.commit

	  print ("Your booking has been confirmed under the name %s and you will be sitting at table for small 1"%name )
	  print ("Your booking time is %d" %s)

	  a = a + 1



	while (b <= 22.0):
		name = input('Your name : ')
		cur.execute("INSERT INTO small_2(UserName) Values('name','b')")
		db.commit

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for small 2"%name )
		print ("Your booking time is %d" %s)

		b = b + 1



	while (c <= 22.0):

		name = input('Your name : ')
		cur.execute("INSERT INTO small_3(UserName) Values('name','c')")
		db.commit

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for small 3"%name )
		print ("Your booking time is %d" %s)

		c = c + 1

	

	while (d <= 22.0):

		name = input('Your name : ')
		cur.execute("INSERT INTO small_4(UserName,Tim) Values('name','d')")
		db.commit

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for small 4"%name )
		print ("Your booking time is %d" %s)

		d = d + 1



def medium():

	a=11.00 

	b=11.00 

	c=11.00

	d=11.00

	e=11.00 

	f=11.00 

	g=11.00

	h=11.00


	

	while (a <= 22.0):

		name = input('Your name : ')

		name = input('Your name : ')
		cur.execute("INSERT INTO medium1(UserName,Tim) Values('name','a')")
		db.commit

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium 1"%name )
		print ("Your booking time is %d" %s)

		a = a + 1



	while (b <= 22.0):

		medium_2[name] = b

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium 2"%name )

		s=medium_2[name]

		print ("Your booking time is %d" %s)

		b = b + 1



	while (c <= 22.0):

		medium_3[name] = c

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium 3"%name )

		s=medium_3[name]

		print ("Your booking time is %d" %s)

		c = c + 1

	

	while (d <= 22.0):

		medium_4[name] = d

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium_4"%name )

		s=medium_4[name]

		print ("Your booking time is %d" %s)

		d = d + 1



	while (e <= 22.0):

		name = input('Your name : ')

		medium_5[name] = e

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium 5"%name )

		s=medium_5[name]

		print ("Your booking time is %d" %s)

		e = e + 1



	while (f <= 22.0):

		medium_5[name] = f

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium 6"%name )

		s=medium_6[name]

		print ("Your booking time is %d" %s)

		f = f + 1



	while (g <= 22.0):

		medium_7[name] = g

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium 7"%name )

		s=medium_7[name]

		print ("Your booking time is %d" %s)

		g = g + 1

	

	while (h <= 22.0):

		medium_8[name] = h

		print ("Your booking has been confirmed under the name %s and you will be sitting at table for medium 8"%name )

		s=medium_8[name]

		print ("Your booking time is %d" %s)

		h = h + 1





def large():

	a=11.00

	b=11.00

	c=11.00

	large_1={}

	large_2={}

	large_3={}

	while (a <= 22.0):

	  name = input('Your name : ')

	  large_1[name] = a

	  print ("Your booking has been confirmed under the name %s and you will be sitting at table for large 1"%name )

	  s=large_1[name]

	  print ("Your booking time is %d" %s)

	  a = a + 1



	while (b <= 22.0):

	  name = input('Your name : ')

	  large_2[name] = b

	  print ("Your booking has been confirmed under the name %s and you will be sitting at table for large 2"%name )

	  s=large_2[name]

	  print ("Your booking time is %d" %s)

	  b = b + 1

	

	while (c <= 22.0):

	  name = input('Your name : ')

	  large_3[name] = c

	  print ("Your booking has been confirmed under the name %s and you will be sitting at table for large 3"%name )

	  s=large_3[name]

	  print ("Your booking time is %d" %s)

	  c = c + 1



def resturant():

	print ("Welcome to resturant MingKong")

	

	person = input('Table for : ')

	person = int(person)

	if (person == 2):

	  small()

	elif (person == 4):

		medium()

	elif (person == 6):

		large()

	elif (person == 12):

		bookingextralarge()

	

resturant()
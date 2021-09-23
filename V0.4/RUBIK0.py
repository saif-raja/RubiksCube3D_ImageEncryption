# RUBIKS CUBE BASED ENCYPTION SOFTWARE FOR TEXT FILES
# Developed by Saifuddin M Raja 


import math
chr =[None]
path = input("please enter the name of the file :    ")
chr = open(path)
len1 = chr.length()
mainlist = [None]
side = math.pow(len*(1/3))
side = int(math.ceil(side)) + 1
for xr in range (0 , side)
	sublista =[None]
	for yr in range (0 , side)
		sublistb = [None]
		for zr in range (0 , side)
			a = (zr + ((side)*yr) + ((side)*(side)*xr))
			wrchr = chr[a]
			sublist.append(wrchr)
		sublista.append(sublistb)
	mainlist.append(sublista)
originallist = mainlist
flag is None
while flag is 0
	ina = input('To Encrypt press 1 , to Decrypt press 2')
	if ina is 1
		encrypt()
		flag = 1
	elif ina is 2
		 decrypt()
		flag = 1
	else
		print ('wrong input please renter')
		flag = 0

prntsqnce()
credits()
chr.close()

/// Schema of input for pass key:
dimens = open ion plane degree 
passkey thus has to be having a length in the multiples of 3
where the 1st 4th 7th etc  will represent dimension hence can only logically assume the values of 0,1,2 representing X , Y , Z axes respectively
so modulo operator is  used with divider int 3
as that will yeild values in range 0-2
///

def encrypt()

		passkey = input ('''
	Please enter the passkey...
	
	''')
	nparts= int (len.passkey() /3)
	parts =[None]
	for t in range(0 , nparts)
		part1 = int (passkey % 1000)
		passkey = int(passkey / 1000)
		deg = int (part1 % 10)
		part1/=10
		pln = int (part1 % 10)
			part1/=10
		dim = int( part1 % 10) % 3 
		if dim = 0
			for px in range(0 , deg)
				ringgenX(pln)
		elif dim = 1
			for py in range(0 , deg)
				ringgenY(pln)
		elif dim = 2 
			for pz in range(0, deg)
				ringgenZ(pln)

def decrypt()

		passkey = input ('''
	Please enter the passkey...
	
	''')
	nparts= int (len.passkey() /3)
	parts =[None]
	for t in range(nparts , 0)
		part1 = int (passkey % 1000)
		passkey = int(passkey / 1000)
		deg = int (part1 % 10)
		mdeg = 4 - (deg % 4)
		part1/=10
		pln = int (part1 % 10)
			part1/=10
		dim = int( part1 % 10) % 3 
		if dim = 0
			for px in range(0 , mdeg)
				ringgenX(pln)
		elif dim = 1
			for py in range(0 , mdeg)
				ringgenY(pln)
		elif dim = 2 
			for pz in range(0, mdeg)
				ringgenZ(pln)


		

def credits()
	print ('''
		hi ! this software was developed by 
		Saifuddin M Raja
		V 0.01
		August 2016


				press two keys to exit
			''')
	input()
	input()






def prntsqnce()
	fileout = open ("processedData.txt". w)
	for xe in range(0,side)
		sublist1 = mainlist[xe]
		for ye in range(0,side)
			sublist2 = sublist1[ye]
			for ze in range (0,side)
				block= sublist2[ze]
				print (str(block) + ' ' , fileout )
	fileout.close()

def rvalueat( xe , ye , ze )
	sublist1= mainlist [xe]
	sublist2= sublist1 [ye]
	block   = sublist2 [ze]
	return block


def wvalueat( xi , yi , zi , char )
	sublist1= mainlist [xi]
	sublist2= sublist1 [yi]
	sublist2[zi] = char
	sublist1[yi] = sublist2
	mainlist[xi] = sublist1


def ringgenX(plane)
	rings =[None]
	while (ringo > 0)
		ring = [None]
		for ya in range(0 , ringo)
			ring[ya] = rvalueat(plane , ya , 0)
		for za in range(0 , ringo)
			ring[(za + ringo)] = rvalueat(plane , ringo , za)
		for ya in range(ringo , 0)
			ring[(ya + ringo + ringo)] = rvalueat(plane , ya , ringo)
		for za in range(ringo , 0)
			ring[(za + ringo + ringo + ringo)] = rvalueat(plane , 0 , za)
		
		for zb in range(0 , ringo)
			wvalueat(plane , ringo , zb , ring[zb])
		for yb in range(ringo , 0)
			wvalueat(plane , yb , ringo , ring[(yb + ringo)]
		for zb in range(ringo , 0)
			wvalueat(plane , 0 , zb , ring[(zb + ringo + ringo)]
		for yb in range(0 , ringo)
			wvalueat(plane , yb , 0 , ring[( yb + ringo +ringo + ringo)]
		
		rings.append(ring)		
		ringo = ringo - 1


def ringgenY(plane)
	rings =[None]
	while (ringo > 0)
		ring = [None]
		for xa in range(0 , ringo)
			ring[xa] = rvalueat(xa , plane , 0)
		for za in range(0 , ringo)
			ring[(za + ringo)] = rvalueat(ringo , plane  , za)
		for xa in range(ringo , 0)
			ring[(xa + ringo + ringo)] = rvalueat(xa , plane , ringo)
		for za in range(ringo , 0)
			ring[(za + ringo + ringo + ringo)] = rvalueat(0 , plane , za)
		
		for zb in range( 0 , ringo)
			wvalueat( ringo , plane , zb , ring[zb])
		for xb in range( ringo , 0)
			wvalueat( xb , plane, ringo , ring[(xb + ringo)]
		for zb in range( ringo , 0)
			wvalueat( 0 , plane , zb , ring[(zb + ringo + ringo)]
		for xb in range( 0 , ringo)
			wvalueat( xb , plane , 0 , ring[( xb + ringo +ringo + ringo)]
		
		ring.append(ring)
		ringo = ringo - 1
	
			
def ringgenZ(plane)
	rings =[None]
	while (ringo > 0)
		ring = [None]
		for ya in range(0 , ringo)
			ring[ya] = rvalueat(plane , ya , 0)
		for xa in range(0 , ringo)
			ring[(za + ringo)] = rvalueat(plane , ringo , za)
		for ya in range(ringo , 0)
			ring[(ya + ringo + ringo)] = rvalueat(plane , ya , ringo)
		for xa in range(ringo , 0)
			ring[(za + ringo + ringo + ringo)] = rvalueat(plane , 0 , za)

		for xb in range(0 , ringo)
			wvalueat(xb , ringo , plane , ring[zb])
		for yb in range(ringo , 0)
			wvalueat ( ringo , yb , plane , ring[(yb + ringo)]
		for xb in range(ringo , 0)
			wvalueat (xb , 0 , plane , ring[(zb + ringo + ringo)]
		for yb in range(0 , ringo)
			wvalueat( 0 , yb , plane , ring[( yb + ringo +ringo + ringo)]
		
		ring.append(ring)
		ringo = ringo - 1



///  Editing Log

6:42 PM 16-Aug-16    4.5   2:58 AM 17-Aug-16
12:41 AM 18-Aug-16   f    

///



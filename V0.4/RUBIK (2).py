"""Crypton V0.02
Developed by :
        Saifuddin M raja
        Akshay S Goel
"""

def encrypt():
    passkey = input ('''
	Please enter the passkey...
	
	''')
    countiy=0
    for lenaa in passkey:
        countiy+=1
    passkey=int(passkey)
    nparts= int (countiy /3)
    parts =[None]
    for t in range(0 , nparts):
        part1 = int (passkey % 1000)
        passkey = int(passkey / 1000)
        deg = int (part1 % 10)
        part1/=10
        pln = int (part1 % 10)
        part1/=10
        dim = int( part1 % 10) % 3 
        if dim == 0:
            for px in range(0 , deg):
                ringgenX(pln)
        elif dim == 1:
            for py in range(0 , deg):
                ringgenY(pln)
        elif dim == 2: 
            for pz in range(0, deg):
                ringgenZ(pln)

def decrypt():

	passkey = input ('''
	Please enter the passkey...
	
	''')
	nparts= int (len.passkey() /3)
	parts =[None]
	for t in range(nparts , 0):
		part1 = int (passkey % 1000)
		passkey = int(passkey / 1000)
		deg = int (part1 % 10)
		mdeg = 4 - (deg % 4)
		part1/=10
		pln = int (part1 % 10)
		part1/=10
		dim = int( part1 % 10) % 3 
		if dim == 0:
			for px in range(0 , mdeg):
				ringgenX(pln)
		elif dim == 1:
			for py in range(0 , mdeg):
				ringgenY(pln)
		elif dim == 2:
			for pz in range(0, mdeg):
				ringgenZ(pln)


		

def credits1():
	print ('''
		hi ! this software was developed by 
		Saifuddin M Raja
		V 0.01
		August 2016


				press two keys to exit
			''')
	input()
	input()






def prntsqnce():
        fileout = open ("processedData.txt" , "w")
        for xe in range(0,side):
            sublist1 = mainlist[xe]
            for ye in range(0,side):
                sublist2 = sublist1[ye]
                for ze in range (0,side):
                     if ze >=len1 : break
                     block= sublist2[ze]
                     print (str(block) + '' , fileout )
        fileout.close()

def rvalueat( xe , ye , ze ):
	sublist1= mainlist [xe]
	sublist2= sublist1 [ye]
	block   = sublist2 [ze]
	return block


def wvalueat( xi , yi , zi , char ):
	sublist1= mainlist [xi]
	sublist2= sublist1 [yi]
	sublist2[zi] = char
	sublist1[yi] = sublist2
	mainlist[xi] = sublist1


def ringgenX(plane):
	rings =[None]
	ringo= side
	while (ringo > 0):
		ring = [None]
		for ya in range(0 , ringo):
			ring[ya] = rvalueat(plane , ya , 0)
		for za in range(0 , ringo):
			ring[(za + ringo)] = rvalueat(plane , ringo , za)
		for ya in range(ringo , 0):
			ring[(ya + ringo + ringo)] = rvalueat(plane , ya , ringo)
		for za in range(ringo , 0):
			ring[(za + ringo + ringo + ringo)] = rvalueat(plane , 0 , za)
		for zb in range(0 , ringo):
			wvalueat(plane , ringo , zb , ring[zb])
		for yb in range(ringo , 0):
			wvalueat(plane , yb , ringo , ring[(yb + ringo)])
		for zb in range(ringo , 0):
			wvalueat(plane , 0 , zb , ring[(zb + ringo + ringo)])
		for yb in range(0 , ringo):
			wvalueat(plane , yb , 0 , ring[( yb + ringo +ringo + ringo)])
		rings.append(ring)		
		ringo = ringo - 1


def ringgenY(plane):
	rings =[None]
	ringo=side
	while (ringo > 0):
		ring = [None]
		for xa in range(0 , ringo):
			ring[xa] = rvalueat(xa , plane , 0)
		for za in range(0 , ringo):
			ring[(za + ringo)] = rvalueat(ringo , plane  , za)
		for xa in range(ringo , 0):
			ring[(xa + ringo + ringo)] = rvalueat(xa , plane , ringo)
		for za in range(ringo , 0):
			ring[(za + ringo + ringo + ringo)] = rvalueat(0 , plane , za)
		for zb in range( 0 , ringo):
			wvalueat( ringo , plane , zb , ring[zb])
		for xb in range( ringo , 0):
			wvalueat( xb , plane, ringo , ring[(xb + ringo)])
		for zb in range( ringo , 0):
			wvalueat( 0 , plane , zb , ring[(zb + ringo + ringo)])
		for xb in range( 0 , ringo):
			wvalueat( xb , plane , 0 , ring[( xb + ringo +ringo + ringo)])
		ring.append(ring)
		ringo = ringo - 1
	
			
def ringgenZ(plane):
	rings =[None]
	ringo=side
	while (ringo > 0):
		ring = [None]
		for ya in range(0 , ringo):
			ring[ya] = rvalueat(plane , ya , 0)
		for xa in range(0 , ringo):
			ring[(za + ringo)] = rvalueat(plane , ringo , za)
		for ya in range(ringo , 0):
			ring[(ya + ringo + ringo)] = rvalueat(plane , ya , ringo)
		for xa in range(ringo , 0):
			ring[(za + ringo + ringo + ringo)] = rvalueat(plane , 0 , za)
		for xb in range(0 , ringo):
			wvalueat(xb , ringo , plane , ring[zb])
		for yb in range(ringo , 0):
			wvalueat ( ringo , yb , plane , ring[(yb + ringo)])
		for xb in range(ringo , 0):
			wvalueat (xb , 0 , plane , ring[(zb + ringo + ringo)])
		for yb in range(0 , ringo):
			wvalueat( 0 , yb , plane , ring[( yb + ringo +ringo + ringo)])
		ring.append(ring)
		ringo = ringo - 1



""' figurative main function begins"""' 
import math
chr =[]
path = input("please enter the name of the file :    ")
path1 ="ABRA.txt"
chr = open(path1)
len1 = 0
chrl =[]
for line in chr:
    for chrr in line:
        len1 = len1 +1
        chrl.append(chrr)
print ("length of file : " , len1)
mainlist = []
side = math.pow(len1,(1/3))
side = int(math.ceil(side))
print('the key_ceill_1D is =' , side)
print('cube has dimensions : ', (side*side*side))
for xr in range (0 , side):
	sublista =[]
	for yr in range (0 , side):
		sublistb = []
		for zr in range (0 , side):
			a = (zr + ((side)*yr) + ((side)*(side)*xr))-1
			if a>=len1 : break
			sublistb.append(chrl[a])
		sublista.append(sublistb)
	mainlist.append(sublista)
originallist = mainlist
flag = 00
while flag is 0:
	ina = input('To Encrypt press a , to Decrypt press b')
	if ina is 'a':
		encrypt()
		flag = 1
	elif ina is 'b':
		decrypt()
		flag = 1
	else:
		print ('wrong input please renter')
		flag = 0

prntsqnce()
credits1()
chr.close()

"""Schema of input for pass key:
dimens = open ion plane degree 
passkey thus has to be having a length in the multiples of 3
where the 1st 4th 7th etc  will represent dimension hence can only logically assume the values of 0,1,2 representing X , Y , Z axes respectively
so modulo operator is  used with divider int 3
as that will yeild values in range 0-2"""




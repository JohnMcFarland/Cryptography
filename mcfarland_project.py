#John McFarland
#CryptoMidtem

#Library Imports
import random
import math

#Required Functions


#insertRickandMortyJokeaboutLittlebits
def RandomBits():
	bits = random.getrandbits(32)
	binaryNumber = '{0:07b}'.format(bits).zfill(32)

	return binaryNumber

#rip that last number for bits.
def lastNumber(binaryNumber):
	lastNumber = binaryNumber[31]
	return lastNumber

#I miss c++
def concatenate(b5, b4, b3, b2, b1):
	finalNumber = "1" + b5 + b4 + b3 + b2 + b1 + "1"
	finalNumber = finalNumber.zfill(32)
	return finalNumber

#converting things to binary because binascii is no fun. 
def convertToBinary(lastBit5, lastBit4, lastBit3, lastBit2, lastBit1):	
	firstNumber = "1"
	lastNumber = "1"
	finalNumber = firstNumber + lastBit5 + lastBit4 + lastBit3 + lastBit2 + lastBit1 + lastNumber
	return int(finalNumber, 2)

#finding that random a for MillerRabin
def randomA(binaryNumber):
	n = random.randint(1, binaryNumber)
	return n


#LAZY implementation of Miller-Rabin because I'm new to python and it is annoying. 
def MillerRabinPrime(n, a):
	new = n - 1
	newBinary = '{0:07b}'.format(new)
	firstBit = newBinary[0]
	secondBit = newBinary[1]
	thirdBit = newBinary[2]
	fourthBit = newBinary[3]
	fifthBit = newBinary[4]
	sixthBit = newBinary[5]
	seventhBit = newBinary[6]

	
	#header
	
	header_list = ["i |", "xi |", "z   |", "y  |","y"]
	row_format ="{:>1}" * (len(header_list) + 1)
	print (row_format.format("", *header_list))

	
	#row 1
	
	y = 1
	z = y
	y1 = a * y 

	row_1 = ["6 |", firstBit, "  |", z, "   |", y, "  |", y1]
	row_format ="{:>1}" * (len(row_1) + 1)
	print (row_format.format("", *row_1))
	
    
	#row 2
	
	z = y1
	y = (z * z) % n
	
	if secondBit == '0':
		y2 = y 
	else:
		y2 = (a*y) % n 


	row_2 = ["5 |", secondBit, "  |", z, "  |", y, " |",y2]
	row_format ="{:>1}" * (len(row_2) + 1)
	print (row_format.format("", *row_2))

	
	#row 3
	
	z = y2
	y = (z * z) % n
	
	if thirdBit == '0':
		y2 = y 
	else:
		y2 = (a*y) % n 

	row_3 = ["4 |", thirdBit, "  |", z, "  |", y, " |",y2]
	row_format ="{:>1}" * (len(row_3) + 1)
	print (row_format.format("", *row_3))


	#row 4
	
	z = y2
	y = (z * z) % n

	if fourthBit == '0':
		y2 = y 
	else:
		y2 = (a*y) % n 

	row_4 = ["3 |", fourthBit, "  |", z, "  |", y, " |",y2]
	row_format ="{:>1}" * (len(row_4) + 1)
	print (row_format.format("", *row_4))


	
	#row 5
	z = y2
	y = (z * z) % n

	if fifthBit == '0':
		y2 = y 
	else:
		y2 = (a*y) % n 

	row_5 = ["2 |", fifthBit, "  |", z, "  |", y, " |",y2]
	row_format ="{:>1}" * (len(row_5) + 1)
	print (row_format.format("", *row_5))


	
	#row 6
	

	z = y2
	y = (z * z) % n

	if sixthBit == '0':
		y2 = y 
	else:
		y2 = (a*y) % n 

	row_6 = ["1 |", sixthBit, "  |", z, "  |", y, " |",y2]
	row_format ="{:>1}" * (len(row_6) + 1)
	print (row_format.format("", *row_6))

	
	#row 7
	
	z = y2
	y = (z * z) % n
	
	if seventhBit == '0':
		y2 = y 
	else:
		y2 = (a*y) % n 


	row_7 = ["0 |", seventhBit, "  |", z, "  |", y, " |",y2]
	row_format ="{:>1}" * (len(row_7) + 1)


	return (row_format.format("", *row_7))



def ExtendedEuclideanAlgorithm(p,q,n,r,e):
    
    
    while(
    qi = r/e
    print ("e = ", e)
    header_list = ["i |", "qi |", "r   |", "ri+1  |", "ri+2  |", "si  |", "ti"]
    row_format ="{:>1}" * (len(header_list) + 1)
    print (row_format.format("", *header_list))

    

    header_list1 = ["i |", qi, " |", r , " |", e, " |", ri+2, " |", "si",  " |", "ti"]
    row_format ="{:>1}" * (len(header_list1) + 1)
    print (row_format.format("", *header_list1))

	
def is_prime(n,a):
    
    if a**(n-1) % n != 1:
        print (n, "is not prime because", a , "^" , n-1 , "mod" , n , "!= 1")
    else:
        print(n , "is perhaps prime because" , a , "^" , n-1 , "mod" , n , "= 1")

'''
part 1 = find a random number and convert to whole number
'''

b5 = RandomBits()
b4 = RandomBits()
b3 = RandomBits()
b2 = RandomBits()
b1 = RandomBits()
lastBit5 = lastNumber(b5)
lastBit4 = lastNumber(b4)
lastBit3 = lastNumber(b3)
lastBit2 = lastNumber(b2)
lastBit1 = lastNumber(b1)

print ("b_5 |", b5 , " | ", lastBit5)
print ("b_4 |", b4 , " | ", lastBit4)
print ("b_3 |", b3 , " | ", lastBit3)
print ("b_2 |", b2 , " | ", lastBit2)
print ("b_1 |", b1 , " | ", lastBit1)

num = convertToBinary(lastBit5, lastBit4, lastBit3, lastBit2, lastBit1)
print ("Number |" , num, " | ", concatenate(lastBit5, lastBit4, lastBit3, lastBit2, lastBit1))


'''
part 2 = MillerRabin
'''
for x in range(0,20):
    print (" ")
    a = randomA(num)
    print ("n=", num, ", a=" , a)

    print (MillerRabinPrime(num, a ))

    is_prime(num,a)

'''
part 3 = Extended Euclidean Algorithm 
'''

#d is the private key. It must be the inverse of e mod phi(n)
#https://crypto.stackexchange.com/questions/25218/rsa-why-must-e-be-relative-prime-to-phin
#
#
p =67 #randomprime1
q =73 #randomprime2
n = p * q
r = (p-1) * (q-1)
e =3 #relatively
d = 15

while ((e*d)% r != 1):
    print("e = ",e)
    e+=1

print (" ")
#print (ExtendedEuclideanAlgorithm(p,q,n,r,e))

print("p =", p, " q =",q, " n = ",n," e = ", e , " d = ", d)
print("p = ", "{0:b}".format(p).zfill(32))
print("q = ", "{0:b}".format(q).zfill(32))
print("n = ", "{0:b}".format(n).zfill(32))
print("e = ", "{0:b}".format(e).zfill(32))
print("d = ", "{0:b}".format(d).zfill(32))

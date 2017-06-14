import random

#return greatest common divisor, using extend Euclidean algorithm, runtime?
def gcd(a,b):
	if b>a:
		bt = b
		b = a
		a = bt
	if b==0:
		return a
	else:
		return gcd(b,a%b)

#return a list of coprimes to N, i.e invertible in Zn, ie (Zn)*
def invertibles(n):
	s = [1]
	for i in range(2,n-1):
		if gcd(n,i) == 1:
			s.append(i)
	return s

#return the invertible of x in Zn, using extended Euclidean Algorithm
def invertible(x,n,p0=0,p1=1):
	assert x<n
	assert x !=0
	if x == 1:
		return 1
	else:	
		q0 = int(n/x)
		r0 = n%x
		if r0 == 0:
			return 'no invertible'
		else:
			q1 = int(x/r0)
			r1 = x%r0
			return invertibleM(r0,r1,n,p0,p1,q0,q1)

def invertibleM(a,b,n,p_2,p_1,q_2,q_1):
	if b==0:
		if a == 1:
			return (p_2 - p_1 * q_2) % n
		else:
			return 'no invertible'
	else:
		#print (a,b,n,p_2,p_1,q_2,q_1)
		p0 =  (p_2 - p_1 * q_2) % n
		q0 = int(a/b)
		r = a%b
		return invertibleM(b,r,n,p_1,p0,q_1,q0)

#calculate invertible using Fermat's Theorem, less efficient
def invertiblef(x,n):
	assert isPrime(n), 'Fermat\'s Theorem required n to be prime'
	return x**(n-2)%n

#solving modular linear equations: ax+b = 0in Zn
def lequation(a,b,n):
	ainvert = invertible(a,n)
	if str(ainvert).isdigit():
		return ainvert*(-b)%n
	else:
		return 'x has no solution as a is invertible.'

#generating random primes using Fermat's theorem. With very high probability and efficiency.
def randomPrime(nbits):
	#1.choose random in [2^1024,2^1025-1]
	#2. test if 2^(p-1) = 1 in Zp. if not, do step1 again.
	start = 2**nbits
	while True:
		x = random.randrange(start,2*start-1)
		#print (x)
		if isPrime(x):
			break
	return x

#check whether there exist agenerator taht can power generate all other invertibles.
def isCyclic(p):
	assert isPrime(p), 'Fermat\'s Theorem required n to be prime'
	for g in range(1,p):
		if order(g,p) == p -1:
			return True
	return False

#return order of the generator
def order(g,p):
	o = 1
	n = 1
	for i in range(1,p):
		n = n*g%p
		if n == 1:
			o = i
			break
	return o

def isPrime(n):
	#this is a Monte Carlo Algorithm
	if 2**(n-1) % n == 1:
		return True
	else:
		return False



if __name__ == "__main__":
	#print (invertibles(26))
	#print ([invertible(x,26) for x in invertibles(26)])
	#print (invertible(2,26))
	#print ([(x,invertible(x,26)) for x in range(1,25)]) 
	#print (lequation(3,4,7))
	#print ((invertible(11,23),invertiblef(11,23)))
	#print (isPrime(11),isPrime(15))
	#print ('the random prime number is:',randomPrime(10))
	print (order(3,7),order(2,7),order(1,7))
	print (isCyclic(7))
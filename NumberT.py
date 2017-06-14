# a class for modular arithmetic, a toy implementaion. not really important
#class modArithmetic:



#return greatest common divisor, using extend Euclidean algorithm, runtime?
def gcd(a,b):
	r = 1
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

#return the invertible element of x in Zn, using extended Euclidean Algorithm
def invertible(x,n):
	assert gcd(x,n) == 1
	b = 0

	return b


#solving modular linear equations: ax+b = 0in Zn
def lequation(a,b,n):
	assert gcd(a,n) == 1
	x = 0

	return x

#calculate invertible using Fermat's Theorem, less efficient
def invertiblef(x,n):
	assert gcd(x,n) == 1
	b = 0

	return b

#generating random primes using Fermat's theorem. With very high probability and efficiency.
def randomPrime(nbits):
	#1.choose random in [2^1024,2^1025-1]
	#2. test if 2^(p-1) = 1 in Zp. if not, do step1 again.
	return True

#check whether there exist agenerator taht can power generate all other invertibles.
def isCyclic(p):
	return True

#return order of the generator
def order(g,p):
	return True



if __name__ == "__main__":
	print (invertibles(26))
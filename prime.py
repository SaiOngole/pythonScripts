def prime(n):
	print "The list of primes in the range 1 to ",n
	for i in range(1,n):
		if(i==2 or i==3 or i==5 or i==7):
			print i
		elif(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
			print i

def main():
	n = input("Enter the max: ")
	prime(n)

if __name__ == '__main__':
	main()
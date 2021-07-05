'''
Objectively compare the efficiency of these two algorithms
	-compare the NUMBER OF ASSIGNMENTS each algorithm makes

Describes how quickly runtime will grow relative to the input as the input get
arbitrarily large.
'''



def sum1(n):
	j = 0
	for x in range(n+1): #O(n)
		j += x

	return j

print(sum1(5))

def sum2(n):
	return round((n*(n+1))/2)

print(sum2(5))

def Bigo(n):
	return 45*n**3 + 20*n**2 + 19 #O(n**3)

#Bigo(2) starting to see thaht 19 will not be a scaling or limiting factor
print(Bigo(10))
# 20n**2 = 2000
# 45**3 = 45000  



'''Big O	Name
	1		Constant
	log(n)	Logarithmic
	n		Linear
	nlog(n)	Log Linear
	n**2	Quadratic
	n**3	Cubic
	2**n	Exponential
	'''

#Examples

#O(1) Constant
def func_constant(values):
	print(values[0])

func_constant([1,2,3])

#O(n) Linear
def func_lin(lst):
	for val in lst:
		print(val)

func_lin([1,2,3])

#O(n**2) Quadratic
def func_quad(lst):
	for item1 in lst:
		for item2 in lst:
			print(item1, item2)

lst = [1,2,3,4,5,6]

func_quad(lst)

#O(1 + n/2 + 10)
def x(lst):
	print(lst[0])

	midpoint = len(lst) // 2

	for val in lst[:midpoint]:
		print(val)

	for x in range(10):
		print('number')

x([1,2,3,4,5,6,7,8,9,10])

#Worst Case vs Best Case
def matcher(lst, match):
	for item in lst:
		if item == match:
			return True
		return False

lst = [1,2,3,4,5,6,7,8,9,10]
matcher(lst, 1) #True, Best Case because 1 is at index 0 
matcher(lst, 20) #False, Worst Case because we have to search the whole list

#Space Complecity
def memory(n=10):
	for x in range(n): #Time complexity O(n)
		print('Memory!') #Space complexity O(1)

memory(10)

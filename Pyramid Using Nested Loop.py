##Assignment

space = ' '
starric = '*'

itrvardec = 5
itrvarinc = 1

for i in range(0,5):
	print(space*itrvardec,end="")
	for x in range(0,itrvarinc):
		print(starric, end="")
	itrvarinc = 2+itrvarinc
	print()
	itrvardec = itrvardec-1
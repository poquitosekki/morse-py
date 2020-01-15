import csv

#path = "/Users/poquito/Desktop/morse-py/"

def mtos(m):
	m = m.split(" ")
	print(m)
	result = []
	with open(f"data.csv", "r") as f:
		mread = csv.reader(f)
		for char in m:
			if char == "/":
				result.append(" ")
				continue
			# the second loop (iterating through the CSV file)
			for row in mread:
				if char == row[1]:
					result.append(row[0])
					f.seek(0)
					break
	return "".join(result)

str = input("Enter your morse code : ")
print(mtos(str))

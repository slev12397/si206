import os
import filecmp


def getData(file):

	lst_dics = []
	opened = open(file, 'r')
	lines = opened.readlines()

	for line in lines[:1]:
		label = line.split(',')
		label[4] = label[4].rstrip('\n')
	for line in lines[1:]:
		words = line.split(',')
		dic = {}
		dic[label[0]]=words[0]
		dic[label[1]]=words[1]
		dic[label[2]]=words[2]
		dic[label[3]]=words[3]
		dic[label[4]]=words[4].rstrip('\n')
		lst_dics.append(dic)
	return lst_dics




#Sort based on key/column
def mySort(data,col):
	sor = sorted(data, key = lambda x: x[col])
	fir = sor[0]['First']
	las = sor[0]['Last']
	return fir + ' ' + las

#Create a histogram
def classSizes(data):
	lst = []
	class_dic = {}
	for student in data:
		if student['Class'] not in class_dic.keys():
			class_dic[student['Class']] = 1
		else:
			class_dic[student['Class']] += 1

	for tup in class_dic.items():
		lst.append(tup)
	return sorted(lst, key = lambda x: x[1], reverse = True)




# Find the most common day of the year to be born
def findDay(a):
	dic = {}
	DOBs = []
	for person in a:
		DOBs.append(person['DOB'])
	for date in DOBs:
		elements = date.split('/')
		if elements[1] not in dic:
			dic[elements[1]] = 1
		else:
			dic[elements[1]] += 1

	s = sorted(dic.keys(), key = lambda x : dic[x],reverse = True)
	return int(s[0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	pass

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	pass



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()


##Solution 1



array = [3,5,-4,8,11,1,-1,6,9]
targetSum = 15

"""
array = [4,6]
targetSum = 10
"""
"""
array = [4, 6, 1, -3]
targetSum = 3
"""

def twoNumberSum(array,targetSum):
	for i in range(len(array) -1):
		firstNum = array[i]
		for j in range(i+1,len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				print(str(firstNum) , str(secondNum) + "  MATCH " + str(targetSum)+ " !!!" )
				return [firstNum,secondNum]
			else:
				print(str(firstNum) , str(secondNum) + " no match")
	return[]


twoNumberSum(array,targetSum)

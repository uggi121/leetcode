array = []
for i in range(int(input())):
	array.append(int(input()))
nums = array

memo = {}

def can(i):
    print(i)
    if i < 0 or i >= len(nums):
        print("if")
        return 0
    elif i + nums[i] >= (len(nums) - 1) or memo[i]:
        print("elif")
        memo[i] = 1
        return 1
    else:
        print("else")
        memo[i] = any(can(i + j + 1) for j in range(nums[i]))
        return memo[i]
            
    print(memo)
    
print(can(0))
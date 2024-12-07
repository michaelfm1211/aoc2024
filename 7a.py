def createable(val, nums):
    for i in range(2**(len(nums) - 1)):
        result = nums[0]
        bitstring = bin(i)[2:].rjust(len(nums) - 1, '0')
        for j, op in enumerate(bitstring):
            if op == "0":
                result *= nums[j+1]
            else:
                result += nums[j+1]
        if result == val:
            return True
    return False

total = 0
for line in open("7.txt"):
    val, nums = line.strip().split(": ")
    val = int(val)
    nums = [int(x) for x in nums.split(" ")]
    if createable(val, nums):
        total += val
print(total)

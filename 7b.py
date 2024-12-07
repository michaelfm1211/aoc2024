def isint(x):
    return int(x) == x

# recursion relation psuedocode:
# createable(val, nums) = createable(val - nums[-1], nums[:-1])
#                           || createable(val / nums[-1], nums[:-1])
#                           || createable(val[:-len(nums[-1])], nums[:-1])
def createable(val, nums):
    if len(nums) == 2:
        add = val == nums[0] + nums[1]
        mul = val == nums[0] * nums[1]
        concat = val == int(str(nums[0]) + str(nums[1]))
        # print(val, nums, add, mul, concat)
        return add or mul or concat
    # print("\t+", val - nums[-1], nums[:-1])
    add = createable(val - nums[-1], nums[:-1]) if val - nums[-1] > 0 else False
    # print("\t*", val // nums[-1], nums[:-1])
    mul = createable(val // nums[-1], nums[:-1]) if isint(val /nums[-1]) else False
    v = str(val)
    n = str(nums[-1])
    # print("\t||", int(v[:-len(n)]) if len(v) > len(n) else "NEGATIVE_DIGITS", nums[:-1])
    concat = createable(int(v[:-len(n)]), nums[:-1]) if len(v) > len(n) and v[-len(n):] == n else False
    # print(val, nums, add, mul, concat)
    return add or mul or concat

total = 0
for line in open("7.txt"):
    val, nums = line.strip().split(": ")
    val = int(val)
    nums = [int(x) for x in nums.split(" ")]
    if createable(val, nums):
        total += val
print(total)


def swap_el(nums_list,index1,index2):
    temp = nums_list[index1]
    nums_list[index1] = nums_list[index2]
    nums_list[index2] = temp
    return nums_list

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        output = ""
        flag = True
        iteration = 1
        while(flag):
            # print(iteration)
            iteration = iteration + 1
            for i in range(0,len(nums)):
                if i < len(nums)-1:
                    if int(str(nums[i]) + str(nums[i+1])) < int(str(nums[i+1]) + str(nums[i])):
                        nums = swap_el(nums,i,i+1)
                        break
            else:
                flag = False

        output = "".join([str(i) for i in nums])
        return "0" if int(output)==0 else output
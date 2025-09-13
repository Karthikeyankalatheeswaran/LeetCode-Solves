/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]} 
 */
var twoSum = function(nums, target) {
    let n = nums.length;
    for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
            if(nums[i]+nums[j]===target){
                return [i,j];
            }
        }
    }
};

// class Solution:
    // def twoSum(self ,nums , target):
    //     n = len(nums)
    //     for i in range(n):
    //         for j in range(i+1,n):
    //             if nums[i]+nums[j] == target:
    //                 return [i,j]
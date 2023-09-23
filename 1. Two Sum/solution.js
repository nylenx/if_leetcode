const twoSum = (nums, target)=> {
    let hashMap={}
    for(i=0;i<nums.length;i++){
        if(hashMap[target-nums[i]]!=undefined){
            return([i,hashMap[target-nums[i]]])
        }
        else{
            hashMap[nums[i]]=i
        }
    }
};
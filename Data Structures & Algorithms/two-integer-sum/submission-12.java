class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int num=0; num <nums.length; num++){
            for(int i=num+1; i<nums.length; i++){
              if (nums[num] + nums[i] == target){
                return new int[]{num,i};
              }
            }
        }
        return new int[]{};
    }
    
}

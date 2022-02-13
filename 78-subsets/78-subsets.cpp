class Solution {
    void helper(vector<vector<int>>& res, vector<int>& temp, vector<int>& nums, int pos){
        res.push_back(temp);

        for(int i=pos; i<nums.size(); ++i){
            temp.push_back(nums[i]);
            cout<<i<<""<<nums[i]<<endl;
            helper(res, temp, nums, i + 1);
            temp.pop_back();
        }

    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> temp;
        helper(res, temp, nums, 0);
        return res;
    }
};
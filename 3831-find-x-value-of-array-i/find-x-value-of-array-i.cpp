class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> ans(k, 0);
        vector<long long> dp(k,0);

        for (int i:nums)
        {
            vector<long long> x(k,0);
            int n = i % k;

            x[n]++;    

            for(int j=0; j<k; j++)
            {
                int y = (j * n) % k;
                x[y] = x[y]+ dp[j];
            }

            for (int j=0; j<k; j++)
            {
                ans[j] = ans[j]+ x[j];
            }

            dp = x;



        }
        return ans;

    }
};
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lst=prices[0],ans=0;
        for(auto p:prices)
        {
            lst=min(lst,p);
            ans=max(ans,p-lst);
        }
        return ans;
    }
};

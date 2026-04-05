class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lst=prices[0],ans=0;
        for(auto p:prices)
        {
            if(p>=lst)ans=max(ans,p-lst);
            else lst=p;
        }
        return ans;
    }
};

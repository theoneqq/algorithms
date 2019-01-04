#include <climits>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

int jump(vector<int>& nums) {
    int nums_size = (int) nums.size();
    if (nums_size <= 2) return nums_size - 1;
    unordered_map<int, pair<int, int>> dp;
    dp[nums_size - 1] = make_pair(0, nums_size - 1);
    dp[nums_size - 2] = make_pair(nums[nums_size - 2] == 0? INT_MAX - 1 : 1, nums_size - 2);
    for(int i = (int) nums.size() - 3; i >= 0; i--) {
        int num = nums[i];
        if (num >= nums_size - 1 - i) {
            dp[i] = make_pair(1, i);
        } else {
            dp[i] = make_pair(INT_MAX - 1, i);
            int j = i + 1;
            vector<int> s;
            cout << "i: " << i << " j: ";
            while (j < nums_size && i + nums[i] >= j) {
                cout << j;
                s.push_back(j);
                j += nums[j] == 0? 1 : nums[j];
            }
            for (int k = 0; k < (int) s.size(); ++k) {
                int jumps = dp[s[k]].first;
                int next = dp[s[k]].second;
                if (next == s[k]) jumps++;
                if (k == (int) s.size() - 1) {
                    if (next > i + nums[i]) {
                        jumps++;
                        next = s[k];
                    }
                }
                cout << " jumps: " << jumps << " next: " << next;
                if (jumps < dp[i].first) dp[i] = make_pair(jumps, next);
            }
            cout << " dp: " << dp[i].first << " " << dp[i].second<< endl;
        }
    }
    return dp[0].first;
}

int main() {
    vector<int> nums = {2,4,8,1,0,8,3,0,7,9,9,8,3,1,7,3};
    cout << "result: " << jump(nums) << endl;
    return 0;
}

#include <climits>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int max_gap(vector<int>& nums) {
    int nums_size = (int) nums.size();
    if (nums_size < 2) return 0;
    int min_num = *min_element(nums.begin(), nums.end());
    int max_num = *max_element(nums.begin(), nums.end());
    if (max_num - min_num == 0) return 0;
    double d = 1.0 * (max_num - min_num) / (nums_size - 1);

    vector<int> mins = vector<int>(nums_size, INT_MAX);
    vector<int> maxs = vector<int>(nums_size, INT_MIN);
    for (int i = 0; i < nums_size; ++i) {
        int idx = (int) ((nums[i] - min_num) / d);
        mins[idx] = min(mins[idx], nums[i]);
        maxs[idx] = max(maxs[idx], nums[i]);
    }

    int gap = 0, prev = -1;
    for (int i = 0; i < nums_size; ++i) {
        if (prev == -1) {
            if (mins[i] != INT_MAX) prev = i;
        } else {
            if (maxs[i] != INT_MIN) {
                gap = max(gap, mins[i] - maxs[prev]);
                prev = i;
            }
        }
    }
    return gap;
}

int main() {
    vector<int> nums = { 0, 3, 6, 9 };
    cout << "result: " << max_gap(nums) << endl;
    return 0;
}

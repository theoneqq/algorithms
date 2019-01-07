#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;

string mininum(string s, string t) {
    unordered_map<int, int> chars;
    for (int i = 0; i < (int) t.length(); ++i) {
        int c = (int) t.at(i);
        if (!chars.insert(make_pair(c, 1)).second) chars[c]++;
    }
    int s_length = (int) s.length();
    int t_length = (int) t.length(), left = 0, right = 0, count = 0;
    int min_left = 0, min_right = s_length;
    while (right < s_length) {
        int c = (int) s.at(right);
        if (chars.find(c) != chars.end() && chars[c]-- > 0) count++;
        if (count == t_length) {
            for (; left < right; ++left) {
                int c = s.at(left);
                if (chars.find(c) != chars.end()) {
                    count--;
                    if (chars[c]++ == 0) {
                        if (right - left < min_right - min_left) {
                            min_left = left;
                            min_right = right;
                        }
                        break;
                    }
                }
            }
        }
        right++;
    }
    if (min_right >= s_length) return "";
    else return s.substr(min_left, min_right - min_left + 1);
}

int main() {
    cout << mininum("BCCCCCCA BAAAA", "CA CA") << endl;
    return 0;
}

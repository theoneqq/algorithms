#include <string>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
using namespace std;

string mininum(string s, string t) {
    unordered_set<int> chars;
    for (int i = 0; i < (int) t.length(); ++i) {
        chars.insert((int) t.at(i));
    }
    auto size = chars.size();
    unordered_map<int, int> t_stat;
    int left = 0;
    int right = 0;
    int s_length = (int) s.length();
    int min_left = 0;
    int min_right = s_length;
    while (right < (int) s_length) {
        int c = (int) s.at(right);
        if (chars.find(c) != chars.end()) {
            if (!t_stat.insert(make_pair(c, 1)).second) {
                t_stat[c]++;
            }
            if (t_stat.size() == size) {
                if (right - left < min_right - min_left) {
                    min_left = left;
                    min_right = right;
                }
                for (; left < right; ++left) {
                    int c = s.at(left);
                    auto it = t_stat.find(c);
                    if (it != t_stat.end()) {
                        if (it->second > 1) {
                            t_stat[c]--;
                        } else{
                            if (right - left < min_right - min_left) {
                                min_left = left;
                                min_right = right;
                            }
                            break;
                        }
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
    cout << mininum("AAA BC", " A BB") << endl;
    return 0;
}

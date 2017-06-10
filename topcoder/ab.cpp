#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
string ab(int n, int k);
bool ab(int a, int b, int k, std::vector<int>& res);
void print(const std::vector<int>& res);


int main() {
    ab(5, 5);
    ab(8, 10);
	return 0;
}

void print(const std::vector<int>& res, std::ostringstream& os) {
   for (size_t i = 0; i < res.size(); ++i) {
        for (int j = 0; j < res[i]; ++j) {
            os << "B";
        }
        if (i < res.size() - 1) {
            os << "A";
        }
   }
   os << endl;
   cout << os.str();
}

string ab(int n, int k) {
    std::vector<int> res;
    ostringstream os;
    for (int i = 0; i <= n; ++i) {
        if (ab(i, n - i, k, res)) {
            print(res, os);
            return os.str();
        } 
    }    
    return "";
}


bool ab(int a, int b, int k, std::vector<int>& res) {
    if (a == 0) {
        if (k == 0) {
            res.push_back(b);
            return true;
        } else {
            return false;
        }
	}
	for (int i = 0; i <= b; ++i) {
		if (ab(a - 1, b - i, k - a * i, res)) res.push_back(i);
		if (a + 1 == (int) res.size()) return true;
	}
    return false;
}

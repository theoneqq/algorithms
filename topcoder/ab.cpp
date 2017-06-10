#include <iostream>

string ab(int n, int k);
string ab(int a, int b, int k);



int main() {
	return 0;
}

string ab(int n, int k) {
	
}

bool ab(int a, int b, int k, std::stack<int>& res) {
	if (a == 1) {
		if (b >= k) {
			res.push(k);
			res.push(k - b);
			return true;
		} else {
			return false;
		}
	}
	for (int i = 0; i <= b; ++i) {
		if (ab(a - 1, b - i, k - a * i, res)) res.push(i);
		if (b + 1 == (int) res.size()) return true;
	}
}

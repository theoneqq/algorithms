#include <vector>
#include <cstdlib>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
class solution {
public:
	void construct_sa(const string& S, int *rank, int *sa) {
		int n = S.length();
		for (int i = 0; i <= n; ++i) {
			sa[i] = i;
			rank[i] = i < n ? S[i] : -1;
		}
	
		int k = 1;
		int *tmp = (int *) malloc((n + 1) * sizeof(int));
		auto compare_sa = [=](int i, int j) -> bool {
			if (rank[i] != rank[j]) return rank[i] < rank[j];
			else {
				int ri = i + k <= n ? rank[i + k] : -1;
				int rj = j + k <= n ? rank[j + k] : -1;
				return ri < rj;
			}
		};

		for (; k <= n; k = k << 1) {
			sort(sa, sa + n + 1, compare_sa);
			tmp[sa[0]] = 0;
			for (int i = 1; i <= n; ++i) {
				tmp[sa[i]] = tmp[sa[i - 1]] + (compare_sa(sa[i - 1], sa[i]) ? 1 : 0);
			}
			for (int i = 0; i <= n; ++i) {
				rank[i] = tmp[i];
			}
		}
		free(tmp);
	}

	void construct_lcp(const string& S, int *rank, int *sa, int *lcp) {
		int n = S.length();
		int i = 0;
		int h = 0;
		lcp[0] = 0;
		for (; i < n; ++i) {
			int j = sa[rank[i] - 1];
			if (h > 0) h--;
			for (; j + h < n && i + h < n; h++) {
				if (S[j + h] != S[i + h]) break;
			}
			lcp[rank[i] - 1] = h;
		}
	}

	string longest_duplicate_string(string S) {
		int s_len = S.length();
		int *rank = (int *) malloc((s_len + 1) * sizeof(int));
		int *sa = (int *) malloc((s_len + 1) * sizeof(int));
		int *lcp = (int *) malloc(s_len * sizeof(int));
		construct_sa(S, rank, sa);
		construct_lcp(S, rank, sa, lcp);

		int l = 0;
		int idx = 0;
		for (int i = 0; i < s_len; ++i) {
			if (l < lcp[i]) {
				l = lcp[i];
				idx = sa[i];
			}
		}
		return S.substr(idx, l);
	}
};

int main() {
	solution s = solution();
	cout << "result: " << s.longest_duplicate_string("banana") << endl;
	return 0;
}

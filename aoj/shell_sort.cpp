#include <iostream>
using namespace std;

int count = 0;

void insert_sort(int* a, int length, int interval) {
    for (int i = interval; i < length; ++i) {
        int v = a[i];
        int j = i - interval;
        while (j >= 0 && a[j] > v) {
            a[j + interval] = a[j];
            j -= interval;
            ++count;
        }
        a[j + interval] = v;
    }
}

void shell_sort(int* a, int length) {
    count = 0;
    int m = 0;
    int[] intervals = {};
    for (int i = 0; i < m; ++i) {
        insert_sort(a, length, intervals[i]);
    }
}

int main() {
    int length = 0;
    cin >> length;
    int* a = new int[length];
    for (int i = 0; i < length; ++i) {
        cin >> a[i];
    }

    shell_sort(a, length);

    return 0;
}

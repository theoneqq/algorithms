#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;
bool is_digit(const string& str) {
    return str.length() > 0 && str[0] != '+' && str[0] != '-' && str[0] != '*';
}

inline int compute(const char oprt, int a, int b) {
    if (oprt == '+') {
        return a + b;
    } else if (oprt == '-') {
        return a - b;
    } else {
        return a * b;
    }
}

int main() {
    stack<int> operands;
    vector<string> inputs;
    string cur;
    while (!cin.eof()) {
        cin >> cur;
        inputs.push_back(cur);
    }

    for (int i = 0; i < (int) inputs.size(); ++i) {
        string cur = inputs[i];
        if (is_digit(cur)) {
            operands.push(atoi(cur.c_str()));
        } else {
            int operand_1 = operands.top();
            operands.pop();
            int operand_2 = operands.top();
            operands.pop();
            char oprt = cur[0];
            operands.push(compute(oprt, operand_2, operand_1));
        }
    }

    cout << operands.top() << endl;

    return 0;
}

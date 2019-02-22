#include <cstdio>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <stack>
#include <algorithm>
#include <deque>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <set>
#include <climits>
using namespace std;

int main() {
    int TC, N, num, count, grad, cur_grad;
    cin >> TC;
    for(int i = 0; i < TC; i++) {
        vector<int> seq;
        count = 0;
        cin >> N;
        N++;
        for(int i = 0; i < N; i++) {
            cin >> num;
            seq.push_back(num);
        }
        
        grad = 0;
        for(int i = 1; i < N; i++) {
            if(grad == 0) {
                if(seq[i] > seq[i - 1]) grad = -1;
                else grad = 1;
            } else {
                if(seq[i] > seq[i - 1]) cur_grad = -1;
                else cur_grad = 1;
                if(cur_grad != grad) {
                    count++;
                    grad = 0;
                }
            }
        }
        cout << "Case #" << i + 1<< ": " << count - 1 << endl;
    }
}

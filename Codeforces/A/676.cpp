/* 
  By: Ahmed Moustafa
  Mail: geekahmed1@gmail.com
  Problem Link: https://codeforces.com/contest/676/problem/A
*/
#include <iostream>
#include <cmath>

using namespace std;


int main() {
    int n, p1, pn;
    cin >> n ;
    for (int i = 1 ; i <= n; i++){
        int temp;
        cin >> temp;
        if (temp == 1)
            p1 = i;
        if (temp == n)
            pn = i;
    }
    cout << max(max(abs(n - p1), abs(n-pn)),max(abs(1-p1), (1-pn))) ;



    return 0;
}



//
// Created by Kqx on 2020/12/3.
//

#include "countPrimes.h"

int countPrimes::CountPrimes(int n) {
    vector<int> isPrime(n + 1, 1);
    int ans = 0;

    for (int i = 2; i <= n; ++i) {
        if (isPrime[i]) {
            ans += 1;
            if ((long long) i * i < n) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = 0;
                }
            }
        }
    }
    return ans;
};

bool countPrimes::isPrime(int n) {
    for (int i = 2; i * i < n; ++i) {
        if (n % i == 0)return false;
    }
    return true;
}

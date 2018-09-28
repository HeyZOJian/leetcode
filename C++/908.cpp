#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution
{
  public:
    int smallestRangeI(vector<int> &A, int K)
    {
        if (A.size() == 0)
            return 0;
        int minn = INT_MAX;
        int maxx = INT_MIN;
        for (int i = 0; i < A.size(); i++)
        {
            minn = min(minn, A[i]);
            maxx = max(maxx, A[i]);
        }
        if ((maxx - K) - (minn + K) <= 0)
            return 0;
        return (maxx - K) - (minn + K);
    }
};

int main()
{
    vector<int> A;
    int k;
    int t;
    cin >> t;
    Solution s = Solution();
    while (t--)
    {
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++)
        {
            int num;
            cin >> num;
            A.push_back(num);
        }
        cin >> k;
        cout << s.smallestRangeI(A, k) << endl;
    }
    return 0;
}
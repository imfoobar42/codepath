package DP;

//https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1?
public class KnapSack {
  static int knapsack(int W, int val[], int wt[]) {
    // code here
    // max value that can be obtained with given constraint
    int n = wt.length;
    // 2 things that change here are n and W
    int dp[][] = new int[n + 1][W + 1];
    // initialization - base conditions
    for (int i = 0; i < n + 1; i++) {
      for (int j = 0; j < W + 1; j++) {
        if (i == 0 || j == 0)
          dp[i][j] = 0;
        // if no elements to check
        // if W==0
      }
    }
    for (int i = 1; i < n + 1; i++) {
      for (int j = 1; j < W + 1; j++) {
        // now we check for each element and its choice
        if (wt[i - 1] <= j) {
          dp[i][j] = Math.max(
              val[i - 1] + dp[i - 1][j - wt[i - 1]],
              dp[i - 1][j]);
        } else
          dp[i][j] = dp[i - 1][j]; // we ignore the current element
      }
    }
    return dp[n][W];
  }
}

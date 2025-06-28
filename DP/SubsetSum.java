package DP;

//https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
public class SubsetSum {

  static Boolean isSubsetSum(int arr[], int sum) {
    // code here
    int n = arr.length;
    boolean dp[][] = new boolean[n + 1][sum + 1];
    // initalization
    for (int i = 0; i < n + 1; i++) {
      for (int j = 0; j < sum + 1; j++) {
        if (i == 0)
          dp[i][j] = false; // if no values exist, then return false
        if (j == 0)
          dp[i][j] = true; // if no target sum we can have empty subset
      }
    }
    for (int i = 1; i < n + 1; i++) {
      for (int j = 1; j < sum + 1; j++) {
        if (arr[i - 1] <= j) { // can choose
          dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
        } else
          dp[i][j] = dp[i - 1][j]; // cant choose
      }
    }
    return dp[n][sum];
  }
}
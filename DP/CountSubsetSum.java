package DP;

public class CountSubsetSum {
  // Function to calculate the number of subsets with a given sum
  // same as subset problem
  // https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
  public int perfectSum(int[] nums, int target) {
    int n = nums.length;
    int dp[][] = new int[n + 1][target + 1];

    // initialization
    for (int i = 0; i < n + 1; i++) {
      dp[i][0] = 1; // no values to check for
    }

    for (int j = 1; j < target + 1; j++) {
      dp[0][j] = 0;// for 0 wt, empty subset suffices, hence 1
    }

    for (int i = 1; i < n + 1; i++) {
      for (int j = 0; j < target + 1; j++) {
        if (nums[i - 1] <= j)
          dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]];
        else
          dp[i][j] = dp[i - 1][j];
      }
    }
    return dp[n][target];
  }
}
import java.util.Scanner;

public class DiceCombinationCSES {
  public static void main(String[] args) {
    // input just a positive integer
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    sc.close();
    System.out.println(diceCombination(n));

  }
ws
  public static int diceCombination(int n) {
    int result = 0;
    int MOD = 1000000007;
    // throw a dice outcome will be b/w 1 and 6
    // dp problem - # of ways, # of combination
    // steps
    // 1. define the state
    // dp[i] : # of ways to make a sum of i
    // Parameter that defines the subproblem - here, n
    // 2. diceComb(n-1)+ diceComb(n-2) = diceComb(n)
    // 3. base case : dp[1]=1, dp[2]=2[(1,1),2]...
    // 4. Final subproblem : sum of sub problems

    return result % (10 ^ 9 + 7);
  }
}

public class InfiniteArray {
  private static int binarySearch(int[] arr, int start, int end, int target) {
    int res = -1;
    while (start <= end) {
      int mid = start + (end - start) / 2;
      if (arr[mid] == target)
        return mid;
      else if (arr[mid] < target)
        start = mid + 1;
      else
        end = mid - 1;
    }
    return res;
  }

  public static int searchInfiniteArray(int[] arr, int target) {
    int start = 0;
    // starting at 0
    // idk where the end is
    // but pretty sure my range of search should increase
    // with every search
    int end = 1;
    while (target > arr[end]) {
      start = end + 1;
      end = end * 2;
    }
    return binarySearch(arr, start, end, target);
  }

  public static void main(String args[]) {
    // Your code goes here
    int[] arr = { 3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170 };

    int ans = searchInfiniteArray(arr, 130);

    System.out.println("Element found at index " + ans);
  }

}

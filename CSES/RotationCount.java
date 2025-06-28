public class RotationCount {
  public static int countRotations(int[] arr, int start, int end, int N) {
    int res = -1;
    while (start <= end) {
      int mid = start + (end - start) / 2;
      // in a rotated array the rotation can be given by the index of the minm value
      int prev = (mid + N - 1) % N;
      int next = (mid + 1) % N;
      if (arr[mid] < arr[prev] && arr[mid] < arr[next])
        return mid;
      else if (arr[mid] < arr[end])
        end = mid - 1;// minm lies on left
      else
        start = mid + 1;
    }
    return res;

  }

  public static int pivotMountainArray(int[] arr, int start, int end) {
    while (start < end) {
      int mid = start + (end - start) / 2;
      if (arr[mid] > arr[mid + 1])
        end = mid;
      else
        start = mid + 1;
    }
    return start; // pivot +1 always will be the minm value
  }

  public static void main(String[] args) {
    int arr[] = { 15, 18, 2, 3, 6, 12 };
    int N = arr.length;

    System.out.println(countRotations(arr, 0, N - 1, N));
  }
}

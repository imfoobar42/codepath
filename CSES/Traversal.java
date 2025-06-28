
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Traversal {
  public static ArrayList<Integer> bfsGraph(int V, ArrayList<ArrayList<Integer>> adjList) {
    ArrayList<Integer> bfs = new ArrayList<>(); // list to store result
    boolean visited[] = new boolean[V]; // boolean array to keep track of visited nodes
    Queue<Integer> queue = new LinkedList<>();
    queue.add(0);
    visited[0] = true; // src node marked visited

    while (!queue.isEmpty()) {
      Integer node = queue.poll();
      for (Integer n : adjList.get(node)) {
        if (!visited[n]) {
          visited[n] = true; // mark it visited
          queue.add(n);
        }
      }
    }

    return bfs;
  }

  public static ArrayList<Integer> dfsGraph(int V, ArrayList<ArrayList<Integer>> adjList){
    ArrayList<
  }
}

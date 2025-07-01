
import java.util.ArrayList;

public class CycleDfs {
  private boolean dfs(int src,
      int parent,
      boolean visited[],
      ArrayList<ArrayList<Integer>> adjList) {
    visited[src] = true;
    for (Integer adjNode : adjList.get(src)) {
      if (!visited[adjNode])
        if (dfs(adjNode, src, visited, adjList) == true)
          return true;
        else if (adjNode != parent)
          return true;
    }

    return false;

  }

  public boolean isCyclic(int V, int[][] edges) {
    // using dfs
    // need to convert edges matrix into adjacency list
    ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
    for (int i = 0; i < V; i++) {
      adjList.add(new ArrayList<>());
    }
    // call dfs on all vertices
    for (int i = 0; i < edges.length; i++) {
      int u = edges[i][0];
      int v = edges[i][1];
      adjList.get(u).add(v);
      adjList.get(v).add(u);
    }
    boolean[] visited = new boolean[V]; // visited array

    for (int i = 0; i < V; i++) {
      if (!visited[i]) {
        if (dfs(i, -1, visited, adjList) == true)
          return true;
      }
    }
    return false;
  }
}

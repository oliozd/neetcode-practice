class Solution {
    public int[] topKFrequent(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<>();
    
    for(int i : nums) {
      //Updates the frquency value by 1 everytime a duplicate key is found
      map.put(i, map.getOrDefault(i, 0) + 1); //Defaults to 0 initially
    }
    PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
    for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
      pq.add(entry);
    }
    //Create an output array that stores the most frequent elements
    int[] output = new int[k];
    //iterate over output array and input most frequently appearing keys in descending order
    for(int i= 0; i < k; i++) {
      output[i] = pq.poll().getKey();
    }
    return output;
    }
}

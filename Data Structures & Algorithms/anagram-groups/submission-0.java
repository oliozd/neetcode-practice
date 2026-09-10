class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hMap = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray(); // For each element, convert to chars
            Arrays.sort(chars); // Sort chars so that you can compare them later
            String sortedStr = new String(chars);// Convert them back to Strings

            // If 'sortedStr' is not a key in the map, create a new ArrayList as its value
            if (!hMap.containsKey(sortedStr)) {
                hMap.put(sortedStr, new ArrayList<>());
            }
            // if it contains the 'sortedStr' which will be an anagram to the previous one
            // it will add the unsorted 'str' as an element to its List<String> value
            hMap.get(sortedStr).add(str);
        }
        // Create and return an ArrayList corresponding to the sorted string 'sortedStr' from
        // the map 'hMap'and add the original string 'str' to this ArrayList
        return new ArrayList<>(hMap.values());
        
        
    }
}

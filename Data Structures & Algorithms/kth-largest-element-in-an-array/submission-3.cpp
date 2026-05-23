class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // create priorityqueue
        priority_queue<int, vector<int>, greater<int>>
        minHeap;
        // for loop to push into minHeap, by default
        for (int num : nums) {
            minHeap.push(num);
            // if exceed size of k
            if (minHeap.size() > k) {
                // pop
                minHeap.pop();
            }
        }
        // return the top of minheap
        return minHeap.top();
    }
};

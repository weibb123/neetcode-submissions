class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // create priorityqueue
        priority_queue<int, vector<int>, greater<int>>
        minHeap;
        // for loop to push into minHeap, by default
        for (int num : nums) {
            // if exceed size of k
            minHeap.push(num);
            // pop
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        // return the top of minheap
        return minHeap.top();
    }
};

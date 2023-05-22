class Solution:

    def climbStairs(self, n: int) -> int:
        cur_steps,prev_step = 2,2
        prev_to_prev_step = 1
        if n ==1: 
            cur_steps = prev_to_prev_step
        
        
        for i in range(2,n):
            cur_steps = prev_step + prev_to_prev_step 
            prev_to_prev_step = prev_step 
            prev_step = cur_steps
        return cur_steps


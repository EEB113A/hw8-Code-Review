    def sum_of_smaller(self, now):
        now = self.root
                
        #function to calculate the sum of each node
        def sum_of_node(num):
            if num == 0:
                return 0
            return num + sum_of_node(num -1)
        
        #Travel inorder
        #Find new value and replace the value of the current node with the new value
        def print_inorder(now):
            if now: 
                print_inorder(now.left)            
                now.val = sum_of_node(now.val) 
                print_inorder(now.right)
                       
        print_inorder(now)

#留言板
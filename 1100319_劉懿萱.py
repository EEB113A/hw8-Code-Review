    def sum_of_smaller(self, now):

        self.total=0
        self.sum_and_change(now)
        
    def sum_and_change(self,now):
        if now:
            self.sum_and_change(now.left)       #走訪左節點
            self.total+=now.val                 #將當前走訪到的節點的值加上已走訪的節點的值的總和 
            now.val = self.total                #將此總和覆蓋到當前走訪的節點
            self.sum_and_change(now.right)      #走訪右節點 

#留言板
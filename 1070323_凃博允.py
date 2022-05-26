    def sum_of_smaller(self, now):
        if now is None: #若節點是空的則直接回傳
            return
        else: 
         self.sum_of_smaller(now.left)  #走訪左子
         now.val = sum(filter(lambda x: x<=now.val, lst))
         self.sum_of_smaller(now.right) #走訪右子

#留言板
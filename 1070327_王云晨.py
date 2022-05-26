    def sum_of_smaller(self, now):
        if now is None: #如果節點是空的，直接回傳
            return
        else: 
         self.sum_of_smaller(now.left)  #走訪左節點
         now.val = sum(filter(lambda x: x<=now.val, lst)) #過濾小於現在值的數
         self.sum_of_smaller(now.right) #走訪右節點

#留言板
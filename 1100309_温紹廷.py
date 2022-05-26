    def sum_of_smaller(self, now):
        if now is None:
             return                                                        #如果節點是空的，直接回傳
        self.sum_of_smaller(now.left)                                      #走訪左節點
        now.val = sum(filter(lambda num: num <=now.val,lst))               #用filter從lst找出符合小於自己的數字並再用sum                                                     
        self.sum_of_smaller(now.right)                                     #走訪右節點


#留言板
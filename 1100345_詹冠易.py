    def sum_of_smaller(self, now):
        if now is None: return #如果現在的節點是空的，直接回傳
        self.sum_of_smaller(now.left) #往左子節點走
        now.val = sum(filter(lambda x: x<=now.val, lst))#遞回累加的動作在lst中完成，條件是小於等於now.val的值
        print(now.val) #印出走訪到的節點的新的值                 
        self.sum_of_smaller(now.right)#往右子節點走


#留言板
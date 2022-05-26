    def sum_of_smaller(self, now):
        self.total=0 #設一個類別變數 total
        self.sum(now) 
    def sum(self,now): # 定義一個物件方法 sum
        if now: # 做中序走訪
            self.sum(now.left) 
            self.total+=now.val # 走訪過程中依序相加節點值，並覆蓋掉走到的節點值
            now.val=self.total
            self.sum(now.right) 

#留言板
    def sum_of_smaller(self, now):
        if now.val == 1:                     # 當確認走訪到1的時候才將total設為0
            self.total = 0                   # 將total設為0
        if now.left != None:                 # 如果節點的左邊有值而不是None的話進入函式進行遞迴
            self.sum_of_smaller(now.left)    # 將左邊節點帶入進行遞迴
        self.total += now.val                # 將走訪到的val加入total進行累算
        now.val = self.total                 # 將節點的值改為累算的值   
        if now.right != None:                # 如果節點的右邊有值而不是None的話進入函式進行遞迴
            self.sum_of_smaller(now.right)   # 將右邊節點帶入進行遞迴

#留言板
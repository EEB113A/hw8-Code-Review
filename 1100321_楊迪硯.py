    def sum_of_smaller(self, now):
        if now.val == 1:
           self.total = 0
        if now.left != None:#左邊有值的話進入函示遞迴
           self.sum_of_smaller(now.left)
        self.total += now.val
        now.val = self.total
        if now.right != None:#右邊有值的話進入函示遞迴
            self.sum_of_smaller(now.right)

#留言板
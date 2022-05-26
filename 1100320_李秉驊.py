    def sum_of_smaller(self, now):
        BST.total = 0                       #建立一個類別屬性total等於0，用來存入小於或等於目前節點的值之和。
        if now :                            #當目前的節點不等於None時後才進入
            self.sum_of_smaller(now.left)   #先往左子樹前進，直到左子樹為None時，才到下一個步驟。
            self.total += now.val           #把目前節點的值和total相累加
            now.val = self.total            #再將目前節點的值更新為 total
            self.sum_of_smaller(now.right)  #接著再往右子樹前進，直到右子樹為None時，才回到前一個節點。

#留言板
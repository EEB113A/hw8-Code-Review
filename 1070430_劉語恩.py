    def sum_of_smaller(self, now, previousVal=0):
        if now != None:
            # previousVal 代表中序走訪當前節點的前一個印出值
            # if 當前節點沒有左子樹(代表左子樹回傳0)
            ##  當前節點值 = previousVal + 原當前節點值
            # else (代表左子樹回傳previousVal)
            ##  當前節點值 = 左子樹回傳值 + 原當前節點值
            now.val += self.sum_of_smaller(now.left, previousVal) + (previousVal if now.left==None else 0)
            # print(now.val)
            # if 有右子樹，則表示previousVal來自右子樹回傳值
            # 不然 previousVal 為當前節點值
            previousVal = self.sum_of_smaller(now.right, now.val) if now.right!=None else now.val
            return previousVal # 回傳中序走訪的當前節點
        else: 
            # 如果當前節點為 None 回傳0
            return 0

#留言板
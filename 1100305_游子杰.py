    def sum_of_smaller(self, now):
        # <將你的程式碼寫在這邊>
        # 可直接使用此方法做遞迴演算
        # 也可以把 sum_of_smaller 當主要方法，再寫另一個方法做遞迴演算，最後再在 sum_of_smaller 中呼叫另外寫的方法
        # hint : 使用中序走訪的方式遞迴
        def inorder(now): 
            if now: 
                inorder(now.left) 
                total[0] += now.val 
                now.val = total[0] 
                inorder(now.right) 
        total = [0] 
        inorder(now)

#留言板
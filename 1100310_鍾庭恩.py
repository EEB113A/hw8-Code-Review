    def sum_of_smaller(self, now):
        # <將你的程式碼寫在這邊>
        if now is None:#空節點回傳
            return
        self.sum_of_smaller(now.left)#走訪左節點
        now.val = sum(filter(lambda x: x<=now.val, lst))
        self.sum_of_smaller(now.right)#走訪右節點

#留言板
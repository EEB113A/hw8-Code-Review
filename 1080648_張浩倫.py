    def sum_of_smaller(self, now):
        now = [0]  # 建立now list
        self.sum(self.root, now)  # 呼叫 定義函式

    def sum(self, root, now):    # 使用中序走訪的方法
        if root == None:  # 如果根節點是空的就return
            return
        self.sum(root.left, now)  # 往左子樹走
        now[0] = now[0] + root.val  # 將值加總起來
        root.val = now[0]  # 當前根結點的值等於加總值
        self.sum(root.right, now)  # 往右子樹走

#留言板
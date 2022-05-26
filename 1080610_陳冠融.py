    def sum_of_smaller(self, now):
        now = [0]  # 一開始先給now初始0
        self.inorderTravel(self.root, now)  # 呼叫inorderTravel中序走訪

    # inorderTravel中序走訪
    def inorderTravel(self, root, now):
        if root == None:  # 判斷跟節點是否為None，是None
            return  # 回傳空
        else:  # 判斷跟節點是否為None，不是None
            self.inorderTravel(root.left, now)  # 左子樹
            now[0] += root.val  # now[0]=now[0]+root.val
            root.val = now[0]  # 把到目前為止累加完的給root.val
            self.inorderTravel(root.right, now)  # 右子樹

#留言板
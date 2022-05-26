    def sum_of_smaller(self, now):

        now = [0]  # 建立 now list
        self.addsmaller(self.root, now)  # 呼叫 addsmaller(根節點,儲存用的list)

    def addsmaller(self, root, now):    # 中序走訪
        if root == None:  # 如果根節點為空跳回
            return
        self.addsmaller(root.left, now)  # 往左子樹走
        now[0] = now[0] + root.val  # 儲存累加值
        root.val = now[0]  # 當前根結點的值等於累加值
        self.addsmaller(root.right, now)  # 往右子樹走

        # if now is None:
        #     return  # 如果現在的節點是空的，直接回傳
        # self.sum_of_smaller(now.left)  # 走訪左節點
        # now.val = sum(filter(lambda x: x <= now.val, lst))
        # self.sum_of_smaller(now.right)  # 走訪右節點

#留言板
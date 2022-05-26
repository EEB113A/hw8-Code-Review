    def inorder(self,root): #中序走訪程序，純參考用
        if root == None: return
        self.inorder(root.left) #走訪左節點
        print(root.val)
        self.inorder(root.right) #走訪右節點
    
    def soscalc(self, root, sum): #soscalc為"sum of smaller calculation"的簡寫
        if root == None: return #當根結點為None時，代表走訪完成，回傳結果
        #以下程序和中序走訪的程序一樣，都是用遞迴方式完成。
        self.soscalc(root.left, sum)
        sum[0] += root.val #加總
        root.val = sum[0] #更新節點為加總結果
        self.soscalc(root.right, sum) 
    
    def sum_of_smaller(self, now):
        summation = [0] #初始化節點加總為只有一個0元素的list，用此list暫存加總結果。
        self.soscalc(now, summation) #進入加總程序

#留言板
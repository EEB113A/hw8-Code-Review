    def sum_of_smaller(self, now):
        self.sum=0
        self.inorder(now)

    def inorder(self,p):
        if p:
            self.inorder(p.left)
            p.val+=self.sum
            self.sum=p.val
            self.inorder(p.right)

#留言板
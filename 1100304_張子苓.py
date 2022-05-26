    def inorder(self,n):   #中序走訪
        if n:
            self.inorder(n.left)
            #re.append(n.val)
            n.val += self.val   #中序走訪的結果中，每節點＝第一個數加到自己
            self.val = n.val    #改變物件本身
            self.inorder(n.right)

    def sum_of_smaller(self, now):

        #re = []
        self.val = 0   #歸零，讓每次inorder的結果不受之前影響
        self.inorder(now)

#留言板
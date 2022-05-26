    x = 0
    def sum_of_smaller(self, now):
        if now:
            self.sum_of_smaller(now.left)
            now.val+= self.x
            self.x = now.val
            self.sum_of_smaller(now.right)

#留言板
    def __init__(self):
        self.root = None
        self.value= 0

    def sum_of_smaller(self, now):
        if now:
            self.sum_of_smaller(now.left)
            now.val+=self.value
            self.value=now.val
            self.sum_of_smaller(now.right)

#留言板
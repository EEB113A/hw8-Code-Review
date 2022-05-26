    def sum_of_smaller(self, now):
        def sum(self, node, extra=0):
            if(node == None): return extra
            node.val += self.sum(node.left, extra)
            return self.sum(node.right, node.val)

    def sum_of_smaller(self, now):
        self.sum(now)

#留言板
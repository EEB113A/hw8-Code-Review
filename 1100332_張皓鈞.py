    def sum_of_smaller(self, now):
        if now == None:
            return now  
        self.sum_of_smaller(now.left)  #讀左節點
        now.val = sum(filter(lambda num: num <= now.val, lst))  #找lst比自己小的數 -> sum
        self.sum_of_smaller(now.right)  #讀右節點

#留言板
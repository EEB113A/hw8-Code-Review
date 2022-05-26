    def sum_of_smaller(self, now):
        self.tmp=0#tmp用來暫存所有子節點的和
        self.total(now)
    
    def total(self,now):#total用來遞迴演算，這樣就不會每次遞迴都覆寫掉tmp的值
        if now:
            self.total(now.left)
            now.val+=self.tmp#節點值累加上tmp紀錄的值
            self.tmp=now.val#tmp改成目前節點的值，也就是該節點加上所有更小節點的和
            self.total(now.right)

#留言板
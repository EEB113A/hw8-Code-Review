# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分

    def __init__(self):
        self.root = None
        self.a=0#原本一開始的起始值，主要用來暫存前一個的總值

    def sum_of_smaller(self, now):
        if now:
            self.sum_of_smaller(now.left)#不斷往左走直到左邊沒東西
            now.val=self.a+now.val#原本node的值+前一個node的值就是node的新總和值
            self.a=now.val#將此node的值當作存起，給下一個node+
            self.sum_of_smaller(now.right)#往右走

#留言板
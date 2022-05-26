# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分

    def __init__(self):
        self.root = None
        self.a=0

    def sum_of_smaller(self, now):
        if now:
            self.sum_of_smaller(now.left)#一直往左直到左邊沒東西
            now.val=self.a+now.val#原本node的值家前一個node的值為node的新總和值
            self.a=now.val#把此node值當作存起，給下一個node加
            self.sum_of_smaller(now.right)#往右走訪

#留言板
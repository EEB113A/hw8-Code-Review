# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分

    def __init__(self):
        self.root = None
        self.first = 0                              # 起始值，用於暫存上一個的總值

    def sum_of_smaller(self, now):
        if now:
            self.sum_of_smaller(now.left)           # 往左走訪
            now.val = self.first + now.val          # node的值+前一個node的值為node的new sum
            self.first = now.val                    # 把此node值存取，留給下一個node加
            self.sum_of_smaller(now.right)          # 往右走訪

#留言板
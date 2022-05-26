# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分

    def __init__(self):
        self.root = None
        self.start = 0#起始值設為0(此為額外新增條件)

    def sum_of_smaller(self, now):
        if now:
            self.sum_of_smaller(now.left)#往左走訪
            now.val = self.start + now.val#node的值加上前一個node的值作為node的新值
            self.start = now.val#把此新值存取，留給下一個node作運算
            self.sum_of_smaller(now.right)# 往右走訪

#留言板
# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分
    
    def __init__(self):
        self.root = None
        self.a=0#一開始的起始值，負責用來站存前一個的總值

    def sum_of_smaller(self, now):
        if now: #假設是now，進入迴圈
            self.sum_of_smaller(now.left) #不停往左邊走訪，直到左邊是none
            now.val=self.a+now.val #node值之新總和=把原node值加前node值
            self.a=now.val #把現在的node值儲存，存給下個節點加
            self.sum_of_smaller(now.right) #往右邊走訪


#留言板
# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分

    def __init__(self):
        self.root = None
        self.mem = 0    #先設置一個memory點來存中間需要被計算的點

    def sum_of_smaller(self, now):
        if now:
            self.sum_of_smaller(now.left)       #一直往二元樹的左邊走，走到底為止
            now.val = self.mem + now.val        #將上一個節點加上新的節點並設為新的memory點
            self.mem = now.val                  #存起這個memory點，給下一個會遇到的節點加用的
            self.sum_of_smaller(now.right)      #左邊走完就往右邊開始走

#留言板
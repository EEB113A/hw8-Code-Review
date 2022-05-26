    def sum_of_smaller(self, now):

        self.sum(self.root)                     #呼叫sum函示計算加總過後的結果

    def sum(self, now):  
       
        if now:                             
            self.sum(now.left)
            total = now.val                     #把現在的now.val複製一份出來
            for x in lst:                       #x變數為lst內的數
                if x < total:                   #當x < 現在now的val執行
                    now.val += x                #now.val加上x現在指到的數
            self.sum(now.right)    

#留言板
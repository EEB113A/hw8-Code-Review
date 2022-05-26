    def sum_of_smaller(self, now):
        sum = [0]                    #總和
        def add(now,sum):            #定義方法
            if now:                  #如果now不是None
                add(now.left,sum)    #往左走
                sum[0] += now.val    #總和加now的值
                now.val = sum[0]     #now的值變成總和的值
                add(now.right,sum)   #往右走
        add(now,sum)                 #呼叫自訂的方法

#留言板
    def sum_of_smaller(self, now) : #主function

        def func(now , tmp) : #子function

            if now == None: #如果now為None就return 0
                return 0

            if now.left != None : #如果now的左邊不是None
                func( now.left , tmp ) #執行子function
            now.val = now.val + tmp[0] #修改now.val
            tmp[0] = now.val #把now.val存在tmp

            if now.right != None : #如果now的右邊不是None
                return func(now.right , tmp ) #執行子function，然後回傳
            return now.val #回傳now.val
            
        tmp = [0] #暫存
        func( now , tmp ) #執行子function

#留言板
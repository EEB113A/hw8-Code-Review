    def sum_of_smaller(self, now):#now=bst.root

        self.List=[]  #建一個空的List，裡面裝依序按大小順序放的數字
        self.SUM(self.root)

    def SUM(self,now):
        self.total=0
        if now:   #中序走訪方式
            self.SUM(now.left)
            self.List.append(now.val)  #把最小的數字放進List內
            if self.List!=[] and self.List[-1]==now.val:  #如果List不是空的，且最該List被放進去的最大的數字(最後面的數字)剛好等於now的值
                #total=0   #先設加總等於0
                for i in self.List:  #把該List內的值
                    #total+=i
                    self.total+=i
                    now.val+=i
                now.val+=self.total-now.val
                    #now.val==total
                #print(total)

            #print(self.List)  
            self.SUM(now.right)

#留言板
    def sum_of_smaller(self, now, tmp=0):
        if now.left != None :                          #如果左節點不為空直
            tmp = self.sum_of_smaller(now.left,tmp)    #左節點就繼續尋訪直到左節點為None
        now.val += tmp                                 #尋訪完後自身加當前總和tmp
        tmp = now.val                                  #更新tmp                      
        if now.right != None :                         #如果右節點不為空直
            tmp = self.sum_of_smaller(now.right,tmp)   #右節點就尋訪直到右節點為None
        if now!=self.root:                             #如果參數now不為根節點
            return tmp                                 #回傳

#留言板
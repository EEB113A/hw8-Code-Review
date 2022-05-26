    def sum_of_smaller(self, now):
        self.root = None                             #先將bst清空
        queue1 = [now]                               #用queue1紀錄bst.root去跑迴圈
        while queue1!=[]:
            queue2 = [now]                           #用queue2紀錄bst.root去跑迴圈
            insert_val = queue1[0].val               #用insert_val紀錄節點值
            while queue2!=[]:
                if queue2[0].val < queue1[0].val:    #在queue2搜索比節點值還小的值加進insert_val
                    insert_val += queue2[0].val
                if queue2[0].left:
                    queue2.append(queue2[0].left)
                if queue2[0].right:
                    queue2.append(queue2[0].right)
                queue2.pop(0)
            self.insert(insert_val)                  #將insert_val的值insert進bst裡
            if queue1[0].left:
                queue1.append(queue1[0].left)
            if queue1[0].right:
                queue1.append(queue1[0].right)
            queue1.pop(0)

#留言板
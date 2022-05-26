    def sum_of_smaller(self, now):
        queue = [self.root]      #設queue為[題目]
        all_nodes = []           #all_node為空[]
        while queue != []:       #當queue不為空[]
            if queue[0].left:                   #如果queue[0]往左
                queue.append(queue[0].left)     #就被加到左queue
            if queue[0].right:                  #如果queue[0]往右
                    queue.append(queue[0].right)#就被加到右queue
            all_nodes.append(queue.pop(0).val)  #加進all_nodes

        queue = [self.root]         #設queue為[題目]
        while queue != []:          #當queue不為空[]
            queue[0].val = sum(filter(lambda val: val <= queue[0].val, all_nodes))  #比較全部節點比第一位小的就全部加起來
            if queue[0].left:               #如果queue[0]往左
                queue.append(queue[0].left) #就被加到左queue
            if queue[0].right:              #如果queue[0]往右
                queue.append(queue[0].right)#就被加到右queue
            queue.pop(0)                    #刪除第一位

#留言板
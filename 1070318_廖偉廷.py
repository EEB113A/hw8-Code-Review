    def sum_of_smaller(self, now):
        self.total = 0
        self.List = []
        self.SUM(self.root)
        self.new_list = []
        # 自己與所有比自己小節點值加總
        for i in range(0, len(self.List)):
            self.total = self.total + self.List[i]
            self.new_list.append(self.total)
        self.cover_list(now)
# 中序走訪遞迴
    def SUM(self, now):
        if now:
            self.SUM(now.left)
            self.List.append(now.val)
            self.SUM(now.right)
    def cover_list(self, now):                 
        if now: 
            self.cover_list(now.left)
            self.new_list.append(now.val)            
            self.cover_list(now.right)

#留言板
# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
   
    def step(self, lst_step):
        if self!= None:
            if self.left == None:
                if self.right == None:
                    lst_step.append(self.val+lst_step[-1])
                    self.val = lst_step[-1]
                else:
                    lst_step.append(self.val+lst_step[-1])
                    self.val = lst_step[-1]
                    self.right.step(lst_step)
            else:
                if self.right == None:
                    self.left.step(lst_step)
                    lst_step.append(self.val+lst_step[-1])
                    self.val = lst_step[-1]
                else:
                    self.left.step(lst_step)
                    lst_step.append(self.val+lst_step[-1])
                    self.val = lst_step[-1]
                    self.right.step(lst_step)
        return lst_step

class BST:
    def __init__(self):
        self.root = None

    def sum_of_smaller(self, now):
        lst_step = [0]
        lst_step = now.step(lst_step)

#留言板
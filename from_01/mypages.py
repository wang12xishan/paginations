

class Paginations:
    def __init__(self,count,number,data_count=11,page_range=7):
        #数据总个数 count
        #当前页  number
        #每页显示条数  per_page count_per_page
        #最多显示页面数 page_range
        self.count = count
        try:
            self.number = number
            if self.number <= 0:
                raise Exception
        except Exception as e:
            self.number=1
        self.data_count = data_count
        self.page_range = page_range

    #数据开始索引
    def start_data(self):
       return (self.number-1)*self.data_count
    #数据结束索引
    def end_data(self):
        return self.number * self.data_count


    @property
    def num_pages(self):
        a,b = divmod(self.count,self.data_count)
        if b == 0:
            return a
        else:
            return a+1


    def pager_count_range(self):  #当前页码 从*** 到***  多个对象 可迭代的
        #range（1，12）
        #self.num_pages 页码总数
        temp =int(self.page_range/2)
        start_p =self.number-temp
        end_p = self.number +temp

        if start_p <=0:  # 当前页面小于一半
            start_p=1
            if self.page_range <=self.num_pages:#页面 长度和最大长度进行比较
                end_p = self.page_range
            else:
                end_p = self.num_pages
            # return range(start_p,end_p+1)
        else:
            end_p= min(end_p,self.num_pages)
        # if (end_p+1) >= self.num_pages:
        #     end_p=self.num_pages
        # else:      不用加这句 画蛇添足
        #     end_p = end_p
        return range(start_p,end_p+1)

    def str_page(self):
        page_list=[]
        first = "<li><a href='index2?p=1'>首页</a></li>"
        page_list.append(first)
        if self.number ==1:
            prev_page = "<li><a href='#'>上一页</a></li>"
        else:
            prev_page = "<li><a href='index2?p=%s'>上一页</a></li>"%(self.number-1)
        page_list.append(prev_page)
        for i in self.pager_count_range():
            if i== self.number:
                temp = "<li class='active' ><a href='index2?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='index2?p=%s'>%s</a></li>"%(i,i)
            page_list.append(temp)
        if self.number == self.num_pages:
            next_page = "<li><a href='#'>下一页</a></li>"
        else:
            next_page = "<li><a href='index2?p=%s'>下一页</a></li>"%(self.number+1)
        page_list.append(next_page)
        last = "<li><a href='index2?p=%s'>尾页</a></li>"%self.num_pages
        page_list.append(last)
        return " ".join(page_list)
from django.shortcuts import render
from django.core.paginator import PageNotAnInteger,EmptyPage
from django.core.paginator import Paginator
# Create your views here.
USER_LIST = []
for i in range(1, 666):
    temp = {"root": "root" + "i", "num":i}
    USER_LIST.append(temp)

def index(request):
    per_page_count = 10
    current_page = request.GET.get("p")
    current_page = int(current_page)

    start = (current_page-1)*10
    end = current_page*10
    data=USER_LIST[start:end]

    return render(request,"index.html",{"user_list":data})

class CustomPaginator(Paginator):
    def __init__(self,current_page,per_pager_count,*args,**kwargs):
        #number
        self.current_page = int(current_page)
        #最多显示的页码数目   len（page_range)  range的长度
        self.per_pager_count = per_pager_count
        super(CustomPaginator,self).__init__(*args,**kwargs)

    def pager_count_range(self):  #当前页码 从*** 到***  多个对象 可迭代的
        #range（1，12）
        #self.num_pages 页码总数
        temp =int(self.per_pager_count/2)
        start_p =self.current_page-temp
        end_p = self.current_page +temp

        if start_p <=0:  # 当前页面小于一半
            start_p=1
            if self.per_pager_count <=self.num_pages:#页面 长度和最大长度进行比较
                end_p = self.per_pager_count
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


def index1(request):
    # per_page_count = 11
    #全部数据：USER_LIST， 得出多少数据
    #per_page:每页显示的数目
    #count：数据总个数      len   999
    #num_page：总页数     count/per-age
    #page_range:总页数的索引围，如（1，10）,(1，200）
    #page：page对象（是否具有下一页，是否上一页）
    current_page = request.GET.get("p") # 当前也页数   page.number
    #paginator对象
    paginator = CustomPaginator(current_page,11,USER_LIST,10)#10 为每页数目
    try :
        #Page对象
        posts = paginator.page(current_page)
        #has_next   是否有下一页
        #next_page_number  下一页页码
        #has_previous   是否有上一页
        #previous_page_number 上一页页码
        #object_list     分页之后的数据列表，已经切好的数据
        #number         当前页
        #paginator      返回paginator对象
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "index.html",{"posts":posts})

def index2(request):
    from from_01.mypages import Paginations
    current_page = int(request.GET.get("p")) #获取当前页码
    page_obj = Paginations(666,current_page)
    data_list = USER_LIST[page_obj.start_data():page_obj.end_data()]   #  获取当前页码数据
    return render(request,"index.html",{"data":data_list,"page_obj":page_obj})
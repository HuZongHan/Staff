from django.core.paginator import Paginator


class CustomPaginator(Paginator):
    def __init__(self,current_page, per_pager_num,*args,**kwargs):
        # 当前页
        self.current_page = int(current_page)
        # 最多显示的页码数量 11
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator,self).__init__(*args,**kwargs)   #这样就不用再写self.*args,self.**kwargs
    def pager_num_range(self):
        # 当前页
        #self.current_page
        # 最多显示的页码数量 11
        #self.per_pager_num
        # 总页数
        # self.num_pages
        if self.num_pages < self.per_pager_num:     #如果总页数小于最多显示的页码数
            return range(1,self.num_pages+1)           #就显示当前总页数+1
        # 总页数特别多 5
        part = int(self.per_pager_num/2)            #显示中间页
        if self.current_page <= part:               #如果当前页部分小于中间页
            return range(1,self.per_pager_num+1)    #就显示从第一页到最多显示的页码数+1
        if (self.current_page + part) > self.num_pages:     #页面“溢出”，当前页+中间页的总量超出了总页数
            return range(self.num_pages-self.per_pager_num+1,self.num_pages+1)  #显示的是从总页数-总页数+1到总页数+1
        return range(self.current_page-part,self.current_page+part+1) #以上两种情况都不是，显示从当前页-中间页到当前页+中间页+1
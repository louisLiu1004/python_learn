from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class ="story">
    Once upon a time there were three little sisters; and their names were
    <a href ="http://example.com/elsie" class = "sister" id = "link1">
    <span>Elsie</span>
    </a>
    <a href = "http://example.com/title" class = "sister" id = "link2">Lacie</a>
    <a href = "http://example.com/title" class = "sister" id = "link3">Tillie</a>
    and they live at the bottom of a well
</p>
<p class="title"><b>The Dormouse's story</b></p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'lxml')

# 基本使用
# print(soup.prettify())
# print(soup.title.string)

# 标签选择器
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)
# print(soup.title.name) #获取标签的名称
# print(soup.p['class'])


# 嵌套选择
# print(soup.head.title.string)

# 子节点和子孙节点


#子节点
# print(soup.p.contents)
# print(soup.p.children) #迭代器
# for i in soup.p.children:
#     print(i)


# 子孙节点
# print(soup.p.descendants)
# # for child in soup.p.descendants:
# #     print(child)

# 父节点
# print(soup.a.parent)

# 兄弟节点
# for i in  soup.a.next_siblings: #后面的兄弟节点
#     print(i)
# for i in  soup.a.previous_siblings:  #前面的兄弟节点
#     print(i)

#标准选择器
# for i in soup.find_all('a'):
#     print(i)
# print(soup.find_all(attrs={'id':'link2'}))
# print(soup.find_all(id= 'link3'))
# print(soup.find_all(text= 'Elsie'))


# CSS选择器
# print(soup.select('.story')) #class用 .表示   两个中间用空格隔开
# print(soup.select('#link1')) #id用 #表示   两个中间用空格隔开
# for i in soup.select('#link1'):
#     print(i)
#     print(i.get_text()) #get_text获取其中的文本

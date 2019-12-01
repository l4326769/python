#文档2为访问记录
#文档3为服务器总和
#如果是其他软件生成的文本记得重新创建一个文本并复制内容到新建的txt
f1=open("C:/Users/刘亚威/Desktop/log.txt")
f2=open("C:/Users/刘亚威/Desktop/谷歌全球服务器.txt")
lst1=[]
lst2=[]
lst3=[]
z=0
k=-1
#所有包含googlevdeo的行剪切下来
while 1:
    s=f1.readline()
    if s:
        if "googlevideo"in s:
            lst1.append(s)
    else:
        break
kkk=f2.read()
#去首尾多余部分
for i in range(0,len(lst1)):
    while lst1[i][z]!="r":
        z+=1
    while lst1[i][k]!="m":
        k-=1
    if k==-1:
        k=len(lst1[i])
#判断并输出
    if lst1[i][z:k+1] not in kkk:
        #判断重复 
        if lst1[i][z:k+1] not in lst2:
            lst2.append(lst1[i][z:k+1]) 
    z=0
    k=-1
#杂项删除
for i in range(0,len(lst2)):
    if "ry fail: " in lst2[i]:
        if lst2[i][9:len(lst2[i])] not in lst3:
            lst3.append(lst2[i][9:len(lst2[i])])
    elif"rect connect " in lst2[i]:
        if lst2[i][13:len(lst2[i])] not in lst3:
            lst3.append(lst2[i][13:len(lst2[i])])
    else:
        if lst2[i] not in lst3:
            lst3.append(lst2[i])
for i in range(0,len(lst3)):
    if lst3[i] not in kkk:
        print(lst3[i])


        

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.http import urlquote
from xml.dom.minidom import parse
from django.http import FileResponse
    # url编码模块
import json
def getserverSetting(request):
    serversetings={}
    # 读取文件
    domTree = parse('static\serverconfig.xml')
    # 获取文档元素对象
    rootNode = domTree.documentElement
    properties = rootNode.getElementsByTagName('property')
    for property in properties:
        name=property.getAttribute("name")
        value=property.getAttribute("value")
        serversetings[name]=value
    print(serversetings)
    return HttpResponse(json.dumps(serversetings), content_type='application/json')
def updateSettings(request):
    newsettings=eval(request.body)
    domTree = parse('static\serverconfig.xml')
    # 获取文档元素对象
    rootNode = domTree.documentElement
    properties = rootNode.getElementsByTagName('property')
    for property in properties:
        name = property.getAttribute("name")
        value = property.getAttribute("value")
        property.setAttribute("value",newsettings[name])
    with open('static/updated_customer.xml', 'w',encoding='utf-8') as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, addindent='  ', encoding='utf-8')
    return HttpResponse(content_type='application/json')
def getFile(request):
    filename = 'serverconfig.xml'

    file = open('static/updated_customer.xml', 'rb')
    response = HttpResponse(file, content_type="application/octet-stream")
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    response['Access-Control-Expose-Headers']='Content-Disposition'
    print(response['Content-Disposition'])
    return response



# django-restframework

## 第一版：基础版本v1.0.0介绍


### 1、项目目录结构介绍

这里只介绍app应用目录结构：
    rest_app01                app应用名称
        models                模型包
            __init__.py
            school.py         模型类文件
    router                    路由包
            __init__.py
        urls.py               路由文件
        serializer            序列化组件包
            __init__.py
            serializer.py     序列化文件
        views                 视图包
            __init__.py
            school.py         视图文件

### 2、序列化组件的作用
    2.1 在django的框架设计时，通过request.POST获取数据必须满足两点条件，否则无法通过request.POST值：
        第一：http请求的请求头的Content-Type字段取值必须是application/x-www-form-urlencoded(form表单默认格式);
        第二：数据格式要求多个字段必须通过&进行传递：name=alex&age=18&gender=男
    
    2.2 如果Content-Type的取值为application/json(json格式)，multipart/form-data(文件)等文件格式时，通过request.POST无法获取数据；此时我们只能通过request.body获取字节流数据[通过socket通信传递的数据]，通过反序列化转换成python可以处理的数据类型在进行使用;

    2.3 django-restframework对http请求进行了解析封装，需要通过request.data进行触发，在使用rest_framework进行http请求的数据获取时， 我们使用request.data来获取body体中的数据;


    2.4 django的rest_framework库的提供了serializers组件，该组件中最重要的两个类Serializer和ModelSerializer








        


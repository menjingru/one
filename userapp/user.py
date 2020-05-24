from django.http import HttpResponse
from userapp.models import Person

    #添加
def addPerson(request):
    person1 = Person(name='one',age=20,pwd='123')
    person1.save()
    return HttpResponse("add successful")

    #查询
def selectPerson(request):
    result =''
    # 查询所有
    # list =Person.objects.all()
    # for i in list:
    #     result+=i.name+" "+str(i.age)+" "+i.pwd
    # 查询指定
    result=Person.objects.get(id=1)
    return HttpResponse(result.name)

    #修改
def updatePerson(request):
    person = Person.objects.get(id=1)
    person.name="dsb"
    person.save()
    return HttpResponse("update successful")

    #删除
def delectPerson(request):
    person = Person.objects.get(id=1)
    person.delete()
    # 删除所有
    # Person.objects.all().delete() 不推荐使用
    return HttpResponse("delect successful")
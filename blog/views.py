from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Userdata,Captcha,Blog,Blog_comment
from django.views.decorators.http import require_http_methods
from .forms import LoginForm,RegisterForm,BlogForm,Blog_commentForm
from django.contrib.auth.decorators import login_required
import string,random
from django.core.mail import send_mail
from django.shortcuts import redirect,reverse
from django.urls.base import reverse_lazy
from django.http import FileResponse


# Create your views here.


def index(request):
    text_details = Blog.objects.all()
    
    status = request.session.get('is_login')
    username = ''
    if status:
        username = request.session['username']
    context={
        'title':'首頁',
        'date':datetime.now(),
        'status':status,
        'username':username,
        'text_details':text_details,
    }
    print(datetime.now())
    return render(request,template_name='index.html',context=context)

def send_email_captcha(request):
    email = request.GET.get('email')
    captcha = ''.join(random.sample(string.digits,k=4))
    print(captcha)
    email_captcha = Captcha.objects.update_or_create(email=email,defaults={'captcha':captcha})
    
    # send_mail(subject='captcha',message=captcha,recipient_list=[email],from_email=None)
    return render(request,template_name='captcha.html')


@require_http_methods(['POST','GET'])
def register(request):
    if request.method == 'GET':
        status = request.session.get('is_login')
        username = ''
        if status:
            username = request.session['username']
        context={'title':'Register',
                 'status':status,
                'username':username
        }
        return render(request,template_name='register.html',context=context)
    # elif request.method == 'POST'   //no decorato
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            valid_p = form.cleaned_data.get('valid_p')
            email = form.cleaned_data.get('email')
            captcha = form.cleaned_data.get('captcha')
            user_data = Userdata(name=name,password=password,email=email)
            user_data.save()
            context={
                'title':'首頁',
                'date':datetime.now(),
                # 'students':s_data,
            }
            return redirect('/login')
        print(form.errors.as_json())
        context={
            'errors':form.errors.as_json()
        }
        # a = form.errors.as_json()
        # return JsonResponse(a,safe=False)
        return render(request,template_name='register.html',context=context)


@require_http_methods(['POST','GET'])
def login(request,context={}):
    if request.method == 'GET':
        status = request.session.get('is_login')
        username = ''
        if status:
            username = request.session['username']
        context.update({'title':'Login',
                 'status':status,
                'username':username
        })
        return render(request,template_name='login.html',context=context)
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                userdata = Userdata.objects.get(email=email)
            except:
                context={
                'errors':'email not exist'
                }
                return render(request,template_name='login.html',context=context)
            if userdata and password == userdata.password:

                request.session['is_login'] = True
                request.session['username'] = userdata.name
                return redirect('/')
            context={
            'errors':'password error'
            }
            return render(request,template_name='login.html',context=context)

@require_http_methods(['POST','GET'])        
def logout(request):
    request.session.flush()
    return redirect('/')

# @login_required(login_url=reverse_lazy('blog:login'))
@require_http_methods(['POST','GET'])
def pub_blog(request):
    status = request.session.get('is_login')
    username = ''
    if status:
        username = request.session['username']
    else:
        context={
            'errors':'log in'
        }
        return login(request,context=context)
    if request.method == 'GET':
        context={'title':'pub_blog',
                'status':status,
                'username':username,
                'errors':'aaaa'
        }
        return render(request,template_name='blog.html',context=context)
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            print('aaa')
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            blog = Blog(name=request.session['username'],title=title,text=text)
            blog.save()
            context = {
                'title':'pub_blog',
                'status':status,
                'username':username,
                'pub_success':'pub_success'
            }
            return render(request,template_name='blog.html',context=context)
        context={
            'title':'pub_blog',
            'status':status,
            'username':username,
            'errors':form.errors.as_json()
        }
        print('bbb')
        return render(request,template_name='blog.html',context=context)


@require_http_methods(['GET'])       
def search(request):
    pass
    

@require_http_methods(['GET','POST'])   
def blog_detail(request,blog_id):
    status = request.session.get('is_login')
    username = ''
    if status:
        username = request.session['username']
    else:
        username = '訪客'
    blog = Blog.objects.get(pk=blog_id)
    print(blog.comments.all())
    if request.method == 'GET':
        
        print(blog)
        context = {
            'status':status,
            "username":username,
            "blog":blog
        }
        return render(request,template_name='blog_detail.html',context=context)
    else:
        form = Blog_commentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            blog = Blog.objects.get(pk=blog_id)
            Blog_comment.objects.create(c_name=username,comment=comment,blog_ky=blog)
            print('aaa')
            
        print(form.errors)
        context = {
                'status':status,
                "username":username,
                "blog":blog
            }
        return render(request,template_name='blog_detail.html',context=context)

 
 
# def blog_comment(request):
#     status = request.session.get('is_login')
#     username = ''
#     if status:
#         username = request.session['username']
#     else:
#         username = '訪客'
#     form = Blog_commentForm(request.POST)
#     if form.is_valid():
#         comment = form.cleaned_data.get('comment')
#         blog_id = request.POST.get('blog_id')
#         blog = Blog.objects.get(pk=blog_id)
#         Blog_comment.objects.create(c_name=username,comment=comment,blog_ky=blog)
#         print('aaa')
        
#     print(form.errors)
#     context = {
#             'status':status,
#             "username":username,
#             "blog":blog
#         }
#     return render(request,template_name='blog_detail.html',context=context)

    
# def download_view(request, id):
#     """
#     下載文件
#     :param request:
#     :param id:文件id
#     :return:
#     """


#     # 如果文件存在，就下載文件
#     if file_result:

#         file = list(file_result)[0]

#         # 文件名稱及路徑
#         name = file.name
#         path = file.path

#         # 讀取文件
#         file = open(path, 'rb')
#         response = FileResponse(file)

#         # 使用urlquote對文件名稱進行編碼
#         response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(name)

#         return response
#     else:
#         return HttpResponse('文件不存在!')
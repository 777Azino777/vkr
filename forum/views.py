from django.shortcuts import render,get_object_or_404, loader,HttpResponseRedirect
from forum.models import Article,Comments,News_up,Raz_photo,Bany_photo,Sport_zal_photo,Rooms_photo
from django.core.paginator import Paginator
from django.contrib import auth
from forum.forms import CommentForm,AddArticle,MyRegistrationForm
from django.contrib.auth.models import User

# Create your views here.

def first_pages(request):
    args ={}
    args['username']=auth.get_user(request).username
    args['first_pages'] = 'active'
    return render(request,'index.html',args)

def forum_page(request,page_number=1):
    all_articles  = Article.objects.all()
    current_page = Paginator(all_articles, 6)
    args = {}
    args['article_page'] = current_page.page(page_number)
    #args['articles'] = Article.objects.all()
    args['articles'] = current_page.page(page_number)
    args['username']= auth.get_user(request).username
    args['forum_page'] = 'active'
    return render(request, 'forum.html',args)


def login_user(request):
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            args = {}
            args['login_errors'] = "Неправильный логин или пароль"
            return render(request,'login.html',args)
    return render(request,'login.html')

def Article_comment(request,article_id=1):
    comment_form = CommentForm
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    args['article_number'] = article_id
    args['forum_page'] = 'active'
    return render(request,'forum_article.html',args)

def Addcomment(request,article_id):
    if request.method == 'POST':
        text = request.POST['comments_text']
        Comments.comments_article = Article.objects.get(id=article_id)
        Comments.comments_text = text
        username  = auth.get_user(request).username
        Comments.comments_from = User.objects.get_by_natural_key(username)


    return HttpResponseRedirect('/forum/forum_article/%s' % article_id)


def Addcomment1(request,article_id):
    if request.method == 'POST' and ("pause" not in request.session):
        form =  CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            qwe = auth.get_user(request).username
            comment.comments_from = User.objects.get_by_natural_key(qwe)
            form.save()
            #request.session.set_expiry(60)
            #request.session['pause'] = True
    return HttpResponseRedirect('/forum/forum_article/%s' % article_id)

def registration(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'reg.html', context)
    form1 = MyRegistrationForm
    context = {'form': MyRegistrationForm()}
    return render(request, 'reg.html', context)


def registr_user(request):
    args = {}
    args['form'] = MyRegistrationForm()
    if request.POST:
        newuser_form = MyRegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],password=newuser_form.cleaned_data['password1'])
            auth.login(request,newuser)
            return HttpResponseRedirect('/')
        else:
            args['form'] = newuser_form
    return render(request,'reg.html',args)



def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def News(request):
    args = {}
    args['image_and_text'] =  News_up.objects.all()
    args['username'] = auth.get_user(request).username
    args['new_page'] = 'active'
    return render(request,'news.html',args)

def Photo(request):
    args={}
    args['image_photo'] = Raz_photo.objects.all()
    args['username']=auth.get_user(request).username
    args['photo_page'] = 'active'
    return render(request,'photo.html',args)

def Photo_banay(request):
    args={}
    args['image_photo'] = Bany_photo.objects.all()
    args['username']=auth.get_user(request).username
    args['photo_page'] = 'active'
    return render(request,'photo_banay.html',args)


def Rooms_banay(request):
    args={}
    args['image_photo'] = Rooms_photo.objects.all()
    args['username']=auth.get_user(request).username
    args['photo_page'] = 'active'
    return render(request,'photo_rooms.html',args)


def Sport_banay(request):
    args={}
    args['image_photo'] = Sport_zal_photo.objects.all()
    args['username']=auth.get_user(request).username
    args['photo_page'] = 'active'
    return render(request,'photo_sport.html',args)

def Pravila(request):

    return render(request,'pravila.html')

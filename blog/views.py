from django.shortcuts import render ,redirect
from .models import Post
from .forms import postform
# Create your views here. 

def post_list(request):
    allpost=Post.objects.all()
    return render(request ,'Post/post_list.html',{'posts':allpost})

def post_detial(request,post_id):
    POST=Post.objects.get(id=post_id)
    return render(request,'Post/post_detial.html',{'single_post':POST})
    
def New_post(request):
    if request.method =='POST': ##SAVE
        form=postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=postform()
    return render(request,'Post/newpost.html',{'form':form})

def Edit_post(request,post_id):
    POST=Post.objects.get(id=post_id)
    if request.method =='POST': ##SAVE
        form=postform(request.POST,request.FILES,instance=POST)
        if form.is_valid():
            form.save()
    else:
        form=postform(instance=POST)
    return render(request,'Post/edit_post.html',{'form':form})

def post_delete(request,post_id):
    POST=Post.objects.get(id=post_id)
    POST.delete()
    return redirect('/blog')  


##cbv
from django.views.generic  import ListView ,DetailView, CreateView,UpdateView,DeleteView


class post_lists(ListView):
    model=Post
class detaillist(DetailView):
    pass

class newlist(CreateView):
    pass

class editist(UpdateView):
    pass


class deletelist(DeleteView):
    pass


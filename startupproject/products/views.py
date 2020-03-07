from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Comment
from django.utils import timezone

def home(request):
    products = Product.objects
    return render(request, 'products/home.html',{'products':products})

# @login_required
# def create(request):
#     if request.method == 'POST':
#         if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
#             product = Product()
#             product.title = request.POST['title']
#             product.body = request.POST['body']
#             if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
#                 product.url = request.POST['url']
#             else:
#                 product.url = "http://"  + request.POST['url']
#             product.icon = request.FILES['icon']
#             product.image = request.FILES['image']
#             #product.pub_date = timezone.datetime.now()
#             product.founder = request.user
#             product.save()
#             return redirect('/products/' + str(product.id))
#         else:
#             return render(request, 'products/create.html', {'error': 'All fields are required'})
#     else:   
#         return render(request, 'products/create.html')
    
@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.founder = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'products/create.html')
    
# @login_required()
# def create(request):
#     if request.method == 'POST':
#             product = Product(request.POST)
#             if product.is_clean():
#                 product.save()
#                 return redirect('/products/' + str(product.id))
#             else:
#                 return render(request, 'products/create.html',{'form':form})
#     else:
#         return render(request, 'products/create.html')

@login_required
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    comments = Comment.objects.filter(product=product).order_by('-id')
    
    
    if request.method == 'POST':
        content = request.POST.get("content")
        comment = Comment.objects.create(product=product, user=request.user, content=content)
        comment.save()
        return redirect('/products/' + str(product.id))
    
    
    context = {
        'product' : product,
        'comments': comments
    }
    
    return render(request, 'products/detail.html', context)

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    """function to increase upvote count """
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
                                                                             

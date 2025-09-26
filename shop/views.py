from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .models import LatestNews


def home(request):
    return render(request, 'shop/home.html')


def category_list(request, category_code):
    """List products for a given category code: K, M, or W"""
    products = Product.objects.filter(category=category_code)
    # friendly title
    title_map = {'K': 'Kids', 'M': 'Mens', 'W': 'Womens'}
    context = {'products': products, 'category_title': title_map.get(category_code, 'Products')}
    return render(request, 'shop/products.html', context)


from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'shop/home.html')


def category_list(request, category_code):
    """List products for a given category code: K, M, or W"""
    products = Product.objects.filter(category=category_code)
    # friendly title
    title_map = {'K': 'Kids', 'M': 'Mens', 'W': 'Womens'}
    context = {'products': products, 'category_title': title_map.get(category_code, 'Products')}
    return render(request, 'shop/products.html', context)


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        qty = int(request.POST.get('quantity', '1'))
        product = get_object_or_404(Product, pk=product_id)

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id]['qty'] += qty
        else:
            cart[product_id] = {'name': product.name, 'price': str(product.price), 'qty': qty, 'image': product.image.url if product.image else ''}
        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')


def cart_view(request):
    cart = request.session.get('cart', {})
    # compute totals
    total = 0
    for item in cart.values():
        total += float(item['price']) * item['qty']
    return render(request, 'shop/cart.html', {'cart': cart, 'total': total})


def news_list(request):
    news = LatestNews.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'shop/news_list.html', {'news_list': news})


def news_detail(request, pk):
    n = get_object_or_404(LatestNews, pk=pk)
    return render(request, 'shop/news_detail.html', {'news': n})


def about(request):
    return render(request, 'shop/about.html')


from .models import Product, LatestNews, ContactMessage
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'shop/contact.html', {'form': form})


def management(request):
    return render(request, 'shop/management.html')
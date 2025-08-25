from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalogue/products.html', {'products': products})


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalogue/product_details.html', {'product': product})


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1
    request.session['cart'] = cart
    messages.success(request, f"Added {product.name} to cart.")
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    updated_cart = {}

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
             continue
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })
      
        updated_cart[str(product_id)] = quantity

  
    request.session['cart'] = updated_cart

    return render(request, 'catalogue/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    messages.success(request, "Removed item from cart.")
    return redirect('cart_detail')


@login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "catalogue/create_product.html", {"form": form})


@login_required
def upload_product_image(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "catalogue/upload_image.html", {"form": form, "product": product})

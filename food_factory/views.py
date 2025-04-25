from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from service.models import service, mainpage ,Cart
from contactenquery.models import contactenquery


# Simple hello view
def home_page(request):
    return HttpResponse("Hi, this is the home page")


# Home/index page with mainpage content
def index_page(request):
    mainpage_data = mainpage.objects.all()
    return render(request, "index.html", {"mainpage_data": mainpage_data})


# Menu page with search capability
def menu_page(request):
    query = request.GET.get('servicename', '')
    if query:
        service_data = service.objects.filter(service_title__icontains=query)
    else:
        service_data = service.objects.all()

    return render(request, 'menu.html', {'service_data': service_data})


# Menu detail page
def menu_detail(request, slug):
    menu_detail = get_object_or_404(service, menu_slug=slug)
    return render(request, "menu_detail.html", {"menu_detail": menu_detail})


# Promotion static page
def promotion_page(request):
    return render(request, "promotions.html")


# Contact form with POST handling
def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("text")
        contactenquery.objects.create(name=name, email=email, message=comment)
    return render(request, "contact.html")


# Karaoke static page
def karaoke_page(request):
    return render(request, "karaoke.html")


# Test form with echo preview
def form_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("text")
        context = {"name": name, "email": email, "comment": comment}
        return render(request, "form.html", context)
    return render(request, "form.html")


# Debug form submit with print (can be removed in prod)
def submitform(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("text")
        print(f"Name: {name}, Email: {email}, Comment: {comment}")
        return HttpResponse("Form submitted successfully")
    return render(request, "test.html")


# Optional fallback home function (currently unused)
def home(request):
    return render(request, "index.html")

# cart page
def cart_page(request):
    return render(request,"cart.html")

#add to cart function
def addtocart(request, item_id):
    item = get_object_or_404(service, id=item_id)

    try:
        cart = Cart.objects.get(id=1)  # using a single shared cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(id=1)

    cart.items.add(item)
    cart.save()

    return render(request, "menu.html", {"item": item})

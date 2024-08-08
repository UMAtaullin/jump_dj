from django.http import HttpResponse


def product_list(request):
    return HttpResponse("Страница со списком товаров")


def product_detail(request, pk):
    return HttpResponse(f"product_list {pk}")


def product_category(request, category):
    return HttpResponse(f"Категория {category}")

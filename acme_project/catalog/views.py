from django.http import HttpResponse
from django.shortcuts import render


def product_list(request):
    context = {
        "products": [
            "Iron carrot",
            "Giant mousetrap",
            "Dehydrated boulders",
            "Invisible paint",
        ]
    }
    return render(request, "catalog/block_content_rendered.html", context)


def product_detail(request, pk):
    return HttpResponse(f"product_list {pk}")


def product_category(request, category):
    return HttpResponse(f"Категория {category}")

from django.shortcuts import render

# def home_view(request):
#     return render(request, 'base.html')

def home_view(request):
    return render(request, 'home.html')

def facilities_view(request):
    return render(request, 'facilities.html')


def room_view(request):
    return render(request, 'room.html')

def restaurant_view(request):
    return render(request, 'restaurant.html')

def banquet_view(request):
    return render(request, 'banquet.html')

def contact_view(request):
    return render(request, 'contact.html')


def term_condition_view(request):
    return render(request, 'term_and_condition.html')
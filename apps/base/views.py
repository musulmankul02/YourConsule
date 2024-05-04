from django.shortcuts import redirect, render
from apps.base import models as base
from apps.secondary import models as secondary_models
from apps.contacts import models as contacts_models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.telegram.views import get_text
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    # base
    settings = base.Settings.objects.latest("id")
    slide = base.Slide.objects.all().order_by("id")[:3]
    numbers = base.Numbers.objects.latest("id")
    about = base.About.objects.latest('id')
    # contacts
    review = contacts_models.Review.objects.all()
    service = contacts_models.Service.objects.all().order_by('?')[:3]



    # secondary
    news = secondary_models.News.objects.all().order_by('?')[:2]
    other_legal_informations = secondary_models.Legalinformation.objects.all().order_by("?")[:3]  
    return render(request, "base/index.html", locals())

def contact(request):
    # base
    settings = base.Settings.objects.latest("id")
    contact = contacts_models.Contacts.objects.all()

    #contacts
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Создание объекта Contacts и его сохранение в базе данных
        contacts_models.Contacts.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            message=message
        )
        if contact:
            get_text(f"""Оставоен отзыв
                    Имя ползователя: {first_name}
                    Фамилие ползователя: {last_name}
                    Номер телефона: {phone}
                    Почта ползователя: {email}
                    Сообшение ползователя: {message}
                    """)

        return redirect('index')
    return render(request, "base/contact.html", locals())

def about(request):
    # base
    settings = base.Settings.objects.latest("id")
    numbers = base.Numbers.objects.latest("id")

    #contacts

    #secondary
    about = base.About.objects.latest('id')
    years = secondary_models.Year.objects.all()
    history = secondary_models.History.objects.all()
    team = secondary_models.Team.objects.all().order_by("?")[:4]
    return render(request, "base/about.html", locals())

def blog(request):
    # Получаем настройки и список новостей
    settings = base.Settings.objects.latest("id")
    news_list = secondary_models.News.objects.all()

    # Определяем количество новостей на странице
    items_per_page = 4
    paginator = Paginator(news_list, items_per_page)

    # Получаем номер страницы из параметра GET запроса
    page_number = request.GET.get('page')

    try:
        # Получаем объекты новостей для текущей страницы
        news = paginator.page(page_number)
    except PageNotAnInteger:
        # Если параметр страницы не является целым числом, выводим первую страницу
        news = paginator.page(1)
    except EmptyPage:
        # Если номер страницы вне диапазона, выводим последнюю страницу
        news = paginator.page(paginator.num_pages)

    return render(request, "base/blog.html", locals())

def service(request):
    settings = base.Settings.objects.latest("id")
    service_list = contacts_models.Service.objects.all()

    # Определяем количество элементов на странице
    items_per_page = 6
    paginator = Paginator(service_list, items_per_page)

    page_number = request.GET.get('page')
    try:
        services = paginator.page(page_number)
    except PageNotAnInteger:
        # Если параметр страницы не является целым числом, выводим первую страницу
        services = paginator.page(1)
    except EmptyPage:
        # Если номер страницы вне диапазона (например, пустая страница), выводим последнюю страницу
        services = paginator.page(paginator.num_pages)

    return render(request, "base/service.html", locals())


def team(request):
    # base
    settings = base.Settings.objects.latest("id")

    #contacts 

    #secondary 
    team = secondary_models.Team.objects.all()
    return render(request, "base/team.html", locals())

def testimonial(request):
    settings = base.Settings.objects.latest("id")
        # Получаем все отзывы
    reviews = contacts_models.Review.objects.all()

    # Настройки пагинации: количество отзывов на одной странице
    items_per_page = 6  # Укажите желаемое количество отзывов на странице

    # Создаем объект Paginator
    paginator = Paginator(reviews, items_per_page)

    # Получаем номер страницы из параметра GET запроса (если не указан, по умолчанию 1)
    page_number = request.GET.get('page', 1)

    try:
        # Получаем объекты отзывов для указанной страницы
        reviews_page = paginator.page(page_number)
    except PageNotAnInteger:
        # Если параметр `page` не является целым числом, возвращаем первую страницу
        reviews_page = paginator.page(1)
    except EmptyPage:
        # Если номер страницы находится за пределами доступного диапазона, возвращаем последнюю страницу
        reviews_page = paginator.page(paginator.num_pages)
    return render(request, "base/testimonial.html", locals())

def case_study_details(request, id):
    # base
    settings = base.Settings.objects.latest("id")
    #secondary
    legalinformation = secondary_models.Legalinformation.objects.get(id=id)
    
    # Получаем другие лицензии или разрешения (исключая текущую)
    other_legal_informations = secondary_models.Legalinformation.objects.exclude(id=id)[:3]  # Получаем первые 3 объекта, исключая текущий
    
    return render(request, "base/case-study-details.html",locals())
    

def blog_details(request, id):
    # Получение конкретной новости по id
    news_item = secondary_models.News.objects.get(id=id)

    # Получаем другие данные для передачи в шаблон
    settings = base.Settings.objects.latest("id")
    review = contacts_models.Review.objects.latest("id")
    contact = contacts_models.Contacts.objects.all()

    if request.method == "POST":
        # Обработка данных формы
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Создание объекта Contacts и его сохранение в базе данных
        contacts_models.Contacts.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            message=message
        )
        if contact:
            get_text(f"""Оставоен отзыв
                    Имя ползователя: {first_name}
                    Фамилие ползователя: {last_name}
                    Номер телефона: {phone}
                    Почта ползователя: {email}
                    Сообшение ползователя: {message}
                    """)
        return redirect('index')

    # Передача данных в шаблон
    return render(request, "base/blog_details.html", locals())

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Отправляем сообщение о подписке
            get_text(f"""
                Оставлена подписка:
                Почта: {email}
            """)
        # После обработки формы, выполняем редирект на указанную страницу (например, главную)
        return HttpResponseRedirect(reverse('index'))

    # Если метод запроса не POST, просто рендерим страницу снова (хотя этот случай не должен возникать)
    return HttpResponseRedirect(reverse('index'))
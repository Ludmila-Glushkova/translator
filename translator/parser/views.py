from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def get_html_content(request):
    word = request.GET.get('word')
    contact = request.GET.get('contact')
    if contact == 'rus':
        html = 'https://www.translate.ru/перевод/русский-английский?text='
    else:
        html = 'https://www.translate.ru/перевод/английский-русский?text='
    word = word.replace(" ", "%20")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) " \
                 "AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/44.0.2403.157 Safari/537.36"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = "en-US,en;q=0.5"
    session.headers['Content-Language'] = "en-US,en;q=0.5"
    html_content = session.get(f'{html}{word}').text
    return html_content

def home(request):
    context = dict()
    if 'word' in request.GET:
        html_content = get_html_content(request)
        soup = BeautifulSoup(html_content, 'html.parser')
        context['translate'] = soup.find(
            "textarea",
            attrs={"class": "form-control expand100-360 myscroll", "id": "tText"}).text
    return render(request, 'home.html', {'context': context})




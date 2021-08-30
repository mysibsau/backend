from user_agents import parse
from django.shortcuts import redirect
from django.shortcuts import render


def download(request):
    ua_string = request.headers.get('User-Agent')
    user_agent = parse(ua_string)
    family = user_agent.os.family
    if family == 'Android':
        return redirect('https://play.google.com/store/apps/details?id=com.SibSU.MySibSU')
    if family == 'iOS':
        return redirect('https://apps.apple.com/ru/app/%D0%BC%D0%BE%D0%B9-%D1%81%D0%B8%D0%B1%D0%B3%D1%83/id1531466252')
    return render(request, 'download/index.html')


def user_agreement(request):
    return render(request, 'user_agreement/index.html')


def not_found(request, exception):
    return render(request, 'not_found/index.html', status=404)

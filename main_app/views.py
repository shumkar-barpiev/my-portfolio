from django.shortcuts import render, get_object_or_404
from .models import Social_links_dev_information, \
    My_Languages_dev_information, My_Recent_Works_dev_information, \
    Home_dev_information, About_dev_information, My_Skills_dev_information, \
    Experience_and_starting_dev_information, What_I_do_dev_information
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException


def basepage(request):
    all_projects = My_Recent_Works_dev_information.newmanager.all()
    developer_info = Home_dev_information.objects.first()
    about_info = About_dev_information.objects.first()
    experience_info = Experience_and_starting_dev_information.objects.first()
    skills = My_Skills_dev_information.objects.all()
    languages = My_Languages_dev_information.objects.all()
    what_i_do = What_I_do_dev_information.objects.all()
    social_links = Social_links_dev_information.objects.first()

    if request.method == "POST":
        user_name = request.POST['nameUser']
        subject = request.POST['subject']
        user_message = request.POST['message']
        settings.EMAIL_HOST_USER = request.POST['emailAdressUser']
        settings.EMAIL_HOST_PASSWORD = request.POST['emailAdressPassword']
        try:

            send_mail(
                subject,  # subject
                user_message,  # message
                settings.EMAIL_HOST_USER,  # from mail
                [developer_info.dev_email_account],  # To mail
                fail_silently=False
            )
            return render(request, 'send_message.html', {'username': user_name})
        except SMTPException as error:

            return render(request, 'send_error.html', {'error_message': error, 'username': user_name})
    else:
        return render(request, 'index.html',
                      {'all_projects': all_projects, 'developer': developer_info, 'about_info': about_info,
                       'skills': skills, 'languages': languages, 'experience_info': experience_info,
                       'social_links': social_links, 'what_i_do': what_i_do})


def post_single(request, post):
    post = get_object_or_404(My_Recent_Works_dev_information, slug=post, status='published')
    return render(request, 'single_post.html', {'post': post})

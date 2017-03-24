from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
# from django.template import loader

from .models import Avideo
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

# Create your views here.


@login_required
def video_list(request):
    # all_videos = Avideo.objects.all()[:6]
    all_videos = get_list_or_404(Avideo)[:6]
    # html = ''
    # for video in all_videos:
    #     url = '/media/' + str(video.media_file)
    #     html += '<a href="' + url + '">' + video.name + '</a<br>'
    # index_templ = loader.get_template('SmallVideo/index.html')
    context = {
        'all_videos': all_videos,
        }
    # return HttpResponse(html)
    # return HttpResponse(index_templ.render(context, request))
    return render(request, 'SmallVideo/index.html', context)


@login_required
def to_play(request, video_id):
    video = Avideo.objects.filter(pk=video_id)
    url = '/media/' + str(video[0].media_file)
    return redirect(url)


class UserFormView(View):
    form_class = UserForm
    template_name = 'SmallVideo/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form': form})

    # process data into database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 需要修改秘密的时候,必须这样
            # user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            # 检查用户是否存在
            user = authenticate(username=username, password=password)
            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('SmallVideo:video')

        return render(request, self.template_name, {'form': form})







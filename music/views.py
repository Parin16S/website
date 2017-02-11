#We are going to delete everything in views.py and start from scratch
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album
#from django.http import Http404 #No longer needed after importing get_object_or_404
from django.http import HttpResponse
#from django.template import loader #to import template
#inorder to combine loader and render of template into one line do the below

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums' #pass the result of queryset as all_albums

    def get_queryset(self):
        return Album.objects.all()  #by default the result is stored in object_list

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView): #We dont need to specify the template name because of the naming convention album_form.html
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView): #We dont need to specify the template name because of the naming convention album_form.html
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


'''from django.shortcuts import render, get_object_or_404
from .models import Album, Song'''
'''This index function contains the html code but we dont want this to be here.
we want to seperate html and python so we use template.
the below function is commented jut for reference and original function will be kept below that'''

'''def index(request):#This index function is mentioned in urls.py of music and name should ny same
    all_albums = Album.objects.all()# proper way to connect to the database
    #html = "<h1> This is list of Album</h1>"
    html = ''
    for albuma in all_albums:
        url = '/music/'+str(albuma.id)+'/'
        html += '<a href="'+url+'">'+albuma.album_title +'</a><br>'
    return HttpResponse(html)'''

'''def index(request): #This index function is mentioned in urls.py of music and name should ny same
    all_albums = Album.objects.all()# proper way to connect to the database
    #template = loader.get_template('music/index.html')
    #python by default looks into music/templates/ for template that why we dont give templates
    #Above template variable is reference to the index.html file
    #We are going to create a dictionary(i.e. context) inorder to pass all_albums information to the
    # template index.html and standard naming is context
    context = {
        'all_albums': all_albums,
    }
    #return HttpResponse(template.render(context, request)) We are passing context to index.html
    #instead of retruning HttpResponse we will return render in order to combile template loader and render
    return render(request, 'music/index.html', context)#HttpResponse is built inside render so internally its doing the same thing'''

#This whole Http404 can be generated by a small code given below
'''def detail(request , album_id):
    try:
        albums = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exists")
    return render(request, 'music/detail.html', {'albuma':albums})'''#What is in quotes is the variable sent to detail.html

'''def detail(request, album_id): #as there is a variable in url we are passing that in function detail
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'albuma' : album})'''


    #return HttpResponse("<h2>This is new details admin id:" + str(album_id) +"</h2>")
    # This will excute no matter what id is there so to give output only for valid id we do the above

'''def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExists):
        return render(request, 'music/detail.html', {
            'albuma':album,
            'error_message':'You did not select a valid song' #This error_message is defined in detail.html
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html',{
            'albuma':album
        })'''














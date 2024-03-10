from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
  
  posts = Post.objects.all()
  for obj in posts:
    print(obj.titulo)
  return HttpResponse("lista de post modulos :)")


def storage(resquest, titulo,cuerpo):
  
  #creamos la isntancia
  post = Post (titulo = titulo, cuerpo = cuerpo)
  post.save()
  #trabajar con el modelo
  return HttpResponse("guardamos en el modelo, no guardamos en la vista")

#metodo para buscar por id
def consultar (resquest,id):
  post = Post.objects.get (id=id)
  return HttpResponse (f"Titulo:{post.titulo}, Cuerpo: {post.cuerpo}, fecha:{post.fecha}")

#metodo modificar

def modificar(resquest, titulo,id):
  post = Post.objects.get(id=id)
  post.titulo =titulo
  post.save()
  return HttpResponse ("Post actualizado")

#metodo eliminar

def eliminar (request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return HttpResponse ("Post eliminado")
  






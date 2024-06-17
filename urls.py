from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from routers import tasks_list_point, create_task_point


task_template = APIRouter()
templates = Jinja2Templates(directory='templates')

@task_template.get('/')
def show_homepage(request: Request):
	tasks:dict = {"tasks": tasks_list_point(request)}
	return templates.TemplateResponse(request=request, name='home_page.html', context=tasks)

@task_template.get('/about')
def show_aboutpage(request: Request):
	return templates.TemplateResponse(request=request, name='about_page.html')

@task_template.get('/registration')
def show_registration(request: Request):
	return templates.TemplateResponse(request=request, name='registration.html')

@task_template.get('/login')
def show_login(request: Request):
	return templates.TemplateResponse(request=request, name='login.html')  

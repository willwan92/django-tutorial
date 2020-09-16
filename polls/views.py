from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404('question 不存在')
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	return HttpResponse('你正在查看 question %s 的结果。' % question_id)

def vote(request, question_id):
	return HttpResponse('你正在给question %s 投票。' % question_id)

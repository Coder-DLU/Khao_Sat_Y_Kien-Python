from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from  .models import Question

def index(request):
    myname="Lê Hùng"
    taiSan = ["Điện thoại", "máy tính", "ô tô"]
    context = {"name": myname, "taisan": taiSan}
    return render(request, "polls/index.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    # list_question = get_object_or_404(Question, pk=1)
    context1 = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context1)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("Lỗi không có choice")
    c.vote = int(c.vote) + 1
    c.save()
    return render(request, "polls/result.html", {"q": q})
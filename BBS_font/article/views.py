from django.core.paginator import Paginator
from django.db.models import Count
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index_view(request, article_type):
    article_list = []
    sort_method = request.GET.get("sort_method")
    try:
        pageNum = int(request.GET.get("page", 1))
    except Exception as e:
        return Http404("数据错误")
    if request.method != "GET":
        return Http404("对不起，您请求类型错误，请更正后重试")
    if sort_method == "time" or not sort_method:
        if not article_type or article_type == "news":
            print("article_type:", article_type)
            print("sort_method:", sort_method)
            page_name = "news"
            article_list = Article.objects.filter(article_type="news", is_available=True).\
                annotate(h=Count("heat__id")).order_by("-created_time")

        elif article_type in ["sports", "science", "entertain", "literature"]:
            page_name = article_type
            article_list = Article.objects.filter(article_type=article_type, is_available=True).\
                annotate(h=Count("heat__id")).order_by("-created_time")
            # print(article_list[0].author.name)

    elif sort_method == "heat":
        if not article_type or article_type == "news":
            page_name = "news"
            article_list = Article.objects.filter(article_type="news", is_available=True).\
                annotate(h=Count("heat__id")).order_by("-h")

        elif article_type in ["sports", "science", "entertain", "literature"]:
            page_name = article_type
            article_list = Article.objects.filter(article_type=article_type, is_available=True).\
                annotate(h=Count("heat__id")).order_by("-h")
    pageObj = Paginator(article_list, 3)
    pageContent = pageObj.page(pageNum)
    return render(request, 'index.html', locals())


def article_detail_view(request, article_id):
    if request.method != 'GET':
        return Http404("对不起，请求类型错误，请重试")

    try:
        article_id = int(article_id)
    except ValueError as e:
        return Http404("文章编号错误")

    article = get_object_or_404(Article, id=article_id, is_available=True)
    article_comment = Comments.objects.filter(to_log=article)
    try:
        heat = Heat(article=article)
        heat.save()
    except Exception as e:
        pass
    return render(request, 'article.html', {"article": article,
                                            "article_comment": article_comment})


def new_article_view(request):
    if 'user' in request.session:
        if request.method == 'GET':
            return render(request, 'new_article.html')
        elif request.method == "POST":
            author_name = request.session.get("user").get("user")
            try:
                author=User.objects.get(name=author_name, is_active=True)
            except Exception as e:
                raise Http404("用户信息有误，请更正后重试")
            article_title = request.POST.get("article-title")
            article_type = request.POST.get("article-type")
            article_content = request.POST.get("article-content")
            # if not article_title:
            #     title_error = "请输入文章标题"
            #     return render(request, "new_article.html", locals())
            #
            # if not article_type:
            #     type_error = "请选择文章类型"
            #     return render(request, "new_article.html", locals())
            #
            # if not article_content:
            #     content_error = "请输入文章内容"
            #     return render(request, "new_article.html", locals())

            try:
                article = Article(title=article_title,
                                  article_type=article_type,
                                  content=article_content,
                                  author=author)
                article.save()
            except Exception as e:
                publish_error = "服务器忙，请重试"
                return render(request, "new_article.html", locals())
            return HttpResponseRedirect("/article/news")
    else:
        return HttpResponseRedirect('/user/cookies/')


def article_delete_view(request, article_id):
    if request.method == "GET":
        if not article_id:
            raise Http404("数据错误，请重试")
        try:
            article_id = int(article_id)
        except:
            raise Http404("数据类型错误，请重试")

        try:
            article = Article.objects.get(id=article_id, is_available=True)
        except:
            raise Http404("对不起，文章已不存在")

        else:
            user = request.session.get("user")
            username = user.get("user")
            if username != article.author.name:
                raise Http404("对不起，您没有权限删除此文章")
            else:
                article.is_available = False
                article.save()
                return HttpResponseRedirect("/article/news")

    else:
        raise Http404("对不起，无法满足您的请求")


def article_comment_view(request, article_id):
    if request.method == "POST":
        if not article_id:
            raise Http404("您发布的评论没有指明文章，请重试")
        try:
            article_id = int(article_id)

        except:
            raise Http404("文章编号错误，请更正后重试")

        try:
            article = Article.objects.get(id=article_id, is_available=True)

        except:
            raise Http404("文章不存在，请换一篇评论吧")
        comment_content = request.POST.get("comment-content")
        if not comment_content:
            raise Http404("评论内容不能为空")

        else:
            publisher = request.session.get("user").get("user")
            try:
                visitor = User.objects.get(name=publisher, is_active=True)
            except:
                raise Http404("用户信息错误，请重试")

            try:
                comment = Comments(comment_content=comment_content,
                                   publisher=visitor,
                                   to_log=article)
                comment.save()
            except Exception as e:
                print(e)
                raise Http404("服务器繁忙，请重试")
            url = "/article/detail/"+ str(article.id)
            return HttpResponseRedirect(url)


    else:
        raise Http404("请求类型错误，请更正后重试")

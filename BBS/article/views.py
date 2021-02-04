from models import *
from tool import *
from django.db.models import Count
from django.http import JsonResponse
import datetime


# Create your views here.

"""
time = datetime.datetime.now()
再把time赋值给需要的DatetimeField字段即可
"""


def view_article(obj):
    """
    获取文章的除评论之外的信息
    """
    stars = Stars.objects.filter(to_article=obj)
    article_dict = {'article_id': obj.id,
                    'article_title': obj.title,
                    'article_author': obj.author.username,
                    'article_content': obj.content,
                    'article_created_time': obj.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'article_up': len(stars)
                   }
    return article_dict


def comments_reply(comment):
    """
    查找某个评论的回复
    """
    comment_id = comment.id
    all_replies = Comments.objects.all().count()
    more_replies = False
    if all_replies>3:
        more_replies = True
    replies = Comments.objects.filter(_parent=comment_id).order_by("-created_time").limit(3)
    reply_info_list = []
    for _comment in replies:
        up_count = CommentStars.objects.filter(to_log=_comment).count()
        down_count = CommentDowns.objects.filter(to_log=_comment).count()
        reply_dict = {
            'publisher': _comment.publisher.username,
            'publisher_avatar': _comment.publisher.avatar,
            'reply_content': _comment.comment_content,
            'created_time': _comment.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'up_count': up_count,
            'down_count': down_count
        }
        reply_info_list.append(reply_dict)
    return reply_info_list, more_replies


def get_article_hot_comments(article_obj):
    """
    获取文章热门评论详情
    """
    res = Comments.objects.filter(to_log=article_obj).exist()
    hot_comment_info_list = []
    if res:

        # 查询热门评论且统计点赞点踩数量
        hot_comments_list = Comments.objects.filter(to_log=article_obj).values("id").annotate(c=Count("commentstars__id")).\
            order_by("c").limit(3)

        for comment in hot_comments_list:
            up_count = CommentStars.objects.filter(to_comment=comment).count()
            down_count = CommentDowns.objects.filter(to_comment=comment).count()
            reply_info, more_replies = comments_reply(comment)
            comment_info_dict = {
                'id': comment.id,
                'publisher_name': comment.publisher.username,
                'publisher_avatar:': comment.publisher.avatar,
                'comment_content': comment.content,
                'created_time': comment.created_time.strftime("%Y-%m-%d %H:%M:%S"),
                'up_counts': up_count,
                'down_counts': down_count,
                'replies': reply_info,
                'more_replies': more_replies
            }
            hot_comment_info_list.append(comment_info_dict)
    return hot_comment_info_list


def get_article_other_comments(article_obj):
    res = Comments.objects.filter(to_log=article_obj).exist()
    all_comments = Comments.objects.filter(to_log=article_obj).count()
    more_comments = False
    if all_comments>3:
        more_comments = True
    other_comment_info_list = []
    if res:
        other_comments_list = Comments.objects.filter(to_log=article_obj).order_by("created_time").limit(4)

        for comment in other_comments_list:
            up_count = CommentStars.objects.filter(to_comment=comment).count()
            down_count = CommentDowns.objects.filter(to_comment=comment).count()
            reply_info, more_replies = comments_reply(comment)
            comment_info_dict = {
                'publisher_name':comment.publisher.username,
                'publisher_avatar:': comment.publisher.avatar,
                'comment_content': comment.content,
                'created_time': comment.created_time.strftime("%Y-%m-%d %H:%M:%S"),
                'up_count': up_count,
                'down_count': down_count,
                'replies': reply_info,
                'more_replies': more_replies
            }
            other_comment_info_list.append(comment_info_dict)
    return other_comment_info_list, more_comments


def get_article_list_view(request, article_type):
    pass


@auth("GET")
def get_article_detail_view(request, article_id):
    if request.method != "GET":
        return JsonResponse({'code': 201, 'error': '请求类型错误，错误码201'})

    if not article_id:
        return JsonResponse({'code': 202, 'error': '请求数据错误，错误码202'})

    try:
        article_id = int(article_id)
    except Exception as e:
        return JsonResponse({'code': 203, 'error': '请求数据错误，错误码203'})

    try:
        article = Article.objects.get(id=article_id, is_available=True)

    except Exception as e:
        return JsonResponse({'code': 204, 'error': '请求数据错误，错误码204'})

    if request.user.usernema != article.author:
        if not article.authority:
            return JsonResponse({'code': 205, 'error': '您没有查看该文章的权限，错误码205'})

    article_info_dict = view_article(article) # 获取评论之外的文章信息
    article_hot_comment_list = get_article_hot_comments(article) # 获取热门评论
    article_other_comment_list, more = get_article_other_comments(article) # 获取其他评论
    data = {'article_info': article_info_dict,
            'article_hot_comment_list': article_hot_comment_list,
            'article_other_comment_list': article_other_comment_list,
            'more_comments': more
            }
    return JsonResponse({'code': 200, 'data': data})


@auth("POST")
def up_article_view(request):
    if request.method != "POST":
        return JsonResponse({'code': 206, 'error': '请求类型错误， 错误码206'})

    data = json.loads(request.body.decode())
    if not data:
        return JsonResponse({'code': 207, 'error': '数据错误，错误码207'})

    article_id = data.get('article_id')
    if not article_id:
        return JsonResponse({'code': 208, 'error': '文章数据错误，错误码208'})


    try:
        article = Article.objects.get(id=article_id,
                                      is_available=True)

    except Exception as e:
        return JsonResponse({'code': 209, 'error': '文章不能存在，错误码209'})

    if request.user.username == article.author.username or article.authority == True:
        try:
            star = Stars(visitor=request.user,
                         to_article=article)
            star.save()
        except Exception as e:
            return JsonResponse({'code': 210, 'error': '服务器忙，请稍后重试，错误码210'})

        else:
            return JsonResponse({'code': 200, 'data': '点赞成功！'})

    else:
        return JsonResponse({'code': 211, 'error': '文章权限错误，错误码211'})


@auth("POST")
def up_comment_view(request):
    if request.method != "POST":
        return JsonResponse({'code': 212, 'error': '请求类型错误，错误码212'})

    data = json.loads(request.body.decode())
    if not data:
        return JsonResponse({'code': 213, 'error': '请求数据错误，错误码213'})

    comment_id = data.get("comment-id")
    if not comment_id:
        return JsonResponse({'code': 214, 'error': '请求数据错误，错误码214'})

    _type = data.get("type")
    if not _type:
        return JsonResponse({'code': 215, 'error': '请求数据错误，错误码215'})

    try:
        comment = Comments.objects.get(id=comment_id)

    except Exception as e:
        return JsonResponse({'code': 216, 'error': '评论不存在，请重试，错误码216'})


    if _type == "up":
        try:
            ctime = datetime.datetime.now()
            comment_star = CommentStars(visitor=request.user,
                                        to_comment=comment,
                                        at_time=ctime)
            comment_star.save()
        except Exception as e:
            return JsonResponse({'code': 217, 'error': '服务器忙，请重试217'})
        else:
            return JsonResponse({'code': 200, 'data': '点赞成功！'})

    elif _type == "down":
        try:
            ctime = datetime.datetime.now()
            comment_down = CommentDowns(visitor=request.user,
                                        to_comment=comment,
                                        at_time=ctime)
            comment_down.save()
        except Exception as e:
            return JsonResponse({'code': 218, 'error': '服务器忙，请重试218'})

        else:
            return JsonResponse({'code': 200, 'data': '点踩成功！'})

    else:
        return JsonResponse({'code': 219, 'error': '数据错误，错误码219'})

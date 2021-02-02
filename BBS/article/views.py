from models import *
from tool import *
from django.db.models import Count
from django.http import JsonResponse


# Create your views here.


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
    查找某个评论的所有回复
    """
    comment_id = comment.id
    replies = Comments.objects.filter(_parent=comment_id).order_by("-created_time")
    reply_info_list = []
    for _comment in replies:
        reply_dict = {
            'publisher': _comment.publisher.username,
            'reply_content': _comment.comment_content,
            'created_time': _comment.created_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        reply_info_list.append(reply_dict)
    return reply_info_list


def article_hot_comments(article_obj):
    """
    获取文章热门评论详情
    """
    hot_comments_list = Comments.objects.filter(to_log=article_obj).values("id").annotate(c=Count("commentstars__id")).\
        order_by("c").limit(3)
    comments_ups_count = Comments.objects.filter(to_log=article_obj).values("id").annotate(c=Count("commentstars__id"))\
        .values("comments__id", "c").order_by("c").limit(3)
    hot_comment_info_list = []
    for comment in hot_comments_list:
        down_count = CommentDowns.objects.filter(to_comment=comment).annotate(d_c=Count("id"))
        comment_info_dict = {
            'publisher_name': comment.publisher.username,
            'publisher_avatar:': comment.publisher.avatar,
            'comment_content': comment.content,
            'created_time': comment.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            'up_counts': comments_ups_count['comment__id'],
            'down_counts': down_count
        }
        hot_comment_info_list.append(comment_info_dict)
    return hot_comment_info_list


def get_article_other_comments(article_obj):
    pass


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

    article_info = view_article(article) # 获取评论之外的文章信息
    article_hot_comment = article_hot_comments(article)




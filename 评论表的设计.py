
"""
知乎的comments就是个线性结构，估计是嫌麻烦所以没做成树状结构吧，
回复的其实是“用户”而不是“评论”，这样就可以不要父子关系，也不用考虑万一父结点删掉了子结点该怎么办得问题。


＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

这几天知乎更新了，评论区加入了分页功能，看来我的估计是没错的，知乎的做法其实就是BBS里最常见盖楼的做法，只是略有改动。
首先，帖子是按照时间排序的，帖子里有“作者”和“回复某人”这两个字段，

如果需要查看某条会话线索，只需把某两个人互相回复的帖子拉出来即可。这么做其实挺省事，效率也高，
比搞成个树不知道好到哪里去了，反正你也不是真的需要一棵树

"""


# 我的设计思路： 将评论和回复分开，评论表是则针对主题（文章）， 回复表则是对评论的回复以及回复的回复

# http://blog.csdn.net/ztchun/article/details/71106117

#
class Comment(models.Model):
    """
    分成两张表： 一张表Comment专门记录对文章的评论（按时间逆序）
    另一张表CommentReply专门记录， 对文章的评论的回复， 
    当然，CommentReply要限制在某篇文章下（某两个人的对话可能在多篇文章下）
    """
    COMMENT_STATUS = (
        (0, '显示'),
        (1, '隐藏')
    ) #
    user_id = models.PositiveIntegerField()# 发表评论用户的id
    user_name = models.CharField(max_length=8, blank=True, null=True)
    content = models.TextField(max_length=200)
    article_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField(choices=COMMENT_STATUS, default=0)
    time_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time_created']

		
class Reply(models.Model):
    """
    回复表
    """
    REPLY_TYPE = (
        (0, 'comment'), # 这是对评论A的回复B, 此时reply_id，就是评论A的id
        (1, 'reply')    # 这是对回复A的回复B，此时reply_id， 就是回复A的id
    )
    comment_id = models.PositiveIntegerField() # 评论id,将所有评论和回复都挂在某一篇文章下
    reply_id = models.PositiveIntegerField() # 回复那条评论（或者评论的回复）的id
    reply_type = models.PositiveIntegerField(choices=REPLY_TYPE, default=0)
    content = models.TextField(max_length=200)
    from_uid = models.PositiveIntegerField(default=0, )#发表回复的用户id
    to_uid = models.PositiveIntegerField() # 目标用户的id
    time_reply = models.DateTimeField(default=timezone.now)

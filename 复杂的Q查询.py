Reply.objects.filter(
            Q(Q(from_uid=from_uid) & Q(to_uid=to_uid)) | Q(Q(from_uid=to_uid) & Q(to_uid=from_uid)),
            comment_id=comment_id)

			
			
SELECT "article_reply"."id", "article_reply"."comment_id", "article_reply"."reply_type", "article_reply"."reply_to_id", "article_reply"."content", "article_reply"."from_uid", "article_reply"."to_uid", "article_reply"."time_reply" 

FROM "article_reply" 
WHERE(
		(
			("article_reply"."from_uid" = 16 AND "article_reply"."to_uid" = 19) 
			
			OR 
			
			("article_reply"."from_uid" = 19 AND "article_reply"."to_uid" = 16)
		) 
		AND "article_reply"."comment_id" = 6
	) 
	
ORDER BY "article_reply"."time_reply" DESC

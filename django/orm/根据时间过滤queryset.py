https://docs.djangoproject.com/en/1.9/ref/models/querysets/#date

# 利用时间范围来过滤： django model
procurement_list = AgentRewardProcurementRecord.objcects.filter(time_rewarded=current_date)

上面我的time_rewarded是DateField字段，如果是DateTimeField字段，则需要变成time_rewarded__date=current_date
time_rewarded__month, time_rewarded__day等等

procurement_list = AgentRewardProcurementRecord.objcects.filter(time_rewarded__gte=current_date)

time_rewarded__gte表示>=



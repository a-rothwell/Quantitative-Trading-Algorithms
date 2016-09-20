def initialize(context):
    context.security= sid(1267))
    schedule_function(rebalance, date_rule=date_rules.every_day())
    
def rebalance(context, data):
    fifty_day_data = data.history(context.security,
        fields='price',
        bar_count=50,
        frequency='1d'
    )
    fifty_day_MA = fifty_day_data.mean()
    thund_day_data = data.history(context.security, fields='price', bar_count=200, frequency='1d')
    thund_day_MA = thund_day_data.mean()
    if fifty_day_MA > thund_day_MA:
       order_percent(context.security,.05)
    elif fifty_day_MA < thund_day_MA:
        order_target_percent(context.security,0)
    else:
        print 'equal'
        
def handle_data(context,data):
    """
    Called every minute. Sumbits orders if certian price goals are met
    """
    pass

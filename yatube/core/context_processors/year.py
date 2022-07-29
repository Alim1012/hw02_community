from datetime import datetime


def year(request):
    year_now = datetime.now().year
    return {
       'year_now': year_now
    }

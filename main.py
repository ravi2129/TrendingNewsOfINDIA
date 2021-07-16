from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews=GoogleNews(period='2d')
googlenews.search('INDIA')
result=googlenews.result()
for x in result:
    print("_"*50)
    print("Title--", x['title'])
    print("Date/Time--", x['date'])
    print("Description--", x['desc'])
    print("Link--", x['link'])

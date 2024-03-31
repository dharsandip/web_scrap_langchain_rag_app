from django.shortcuts import render
from App_news_web_scrapping_langchain_LLM_RAG_query import langchain_rag


# Create your views here.
def process_query(request):
    if request.method == 'POST':
        url = request.POST.get('url')
#        url = request.POST['URL']
#        url = "https://usa.nissannews.com/en-US/"
        url = str(url)
        print("url = {}".format(url))
#        query = request.POST['QUERY']
        query = request.POST.get('query')
#        query = "Tell me the top News about Nissan"
        query = str(query)
        answer = langchain_rag(url, query)
        return render(request, 'main.html', {'query': query, 'answer' : answer})
    return render(request, 'main.html')


from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext'] #home에서 넘긴 'fulltext'을 가져옴
    word_list = full_text.split()   #우변은 원문을 공백기준으로 나눠 "리스트"로 만들어 줌
    word_dictionary = {}    #빈 사전을 만듦

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1  #key와 value를 추가함
        else:
            word_dictionary[word] = 1   #원래 key와 value가 없었으므로 int를 하나 지정해줘야 돼서 else문으로 해야 함
    return render(request, 'wordcount/count.html', {"fulltext":full_text, "total":len(word_list), "dictionary":word_dictionary.items()}) #total: 총 단어수는 full_text의 길이 / countTotal: items 메소드를 통해 각 key-value 쌍들을 리턴함 
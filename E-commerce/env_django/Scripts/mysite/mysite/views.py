from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    ab=request.GET.get('text','default')
    lower_case_var=request.GET.get('lower_case','off')
    remove_punc=request.GET.get('remove_punc','off')
    if lower_case_var=="on" and remove_punc=="on" :
        print("dono on hai")
        new_var=ab.lower()
        punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        str1=""
        for i in new_var:
            if i not in punc:
                str1=str1+i
        

        dic_type={"input_text":new_var,"out_text":str1}
        return render(request,'lower.html',dic_type)


    if lower_case_var=="on" and remove_punc=="off" :
        new_var=ab.lower()
        dic_type={"input_text":new_var,"out_text":new_var}
        return render(request,'lower.html',dic_type)


    if lower_case_var=="off" and remove_punc=="on" :
        punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        str1=""
        for i in ab:
            print("yha aa rha hai")
            if i not in punc:
                str1=str1+i
        print("stri 1 hai",str1)

        dic_type={"input_text":ab,"out_text":str1}
        print(dic_type,"dic type is ")
        return render(request,'lower.html',dic_type)
    return HttpResponse(" Please select one of the checkbox")

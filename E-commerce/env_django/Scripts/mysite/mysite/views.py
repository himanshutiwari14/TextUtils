from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')

def analyze(request):
    ab=request.POST.get('text','default')
    print(ab,"generated text is")
    lower_case_var=request.POST.get('lower_case','off')
    print(lower_case_var,"status of lower_case_var")
    remove_punc=request.POST.get('remove_punc','off')
    print(remove_punc,"status of remove_punc")
    if lower_case_var=="on" and remove_punc=="on" :
        print("dono on hai")
        new_var=ab.lower()
        punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        str1=""
        for i in new_var:
            if i not in punc:
                str1=str1+i
        

        dic_type={"input_text":ab,"out_text":str1}
        return render(request,'lower.html',dic_type)


    if lower_case_var=="on" and remove_punc=="off" :
        new_var=ab.lower()
        dic_type={"input_text":ab,"out_text":new_var}
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

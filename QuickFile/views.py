import  os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
#from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime


from . models import CBC, KFT, LFT, Lipid_Profile

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cbc(request):
    if request.method == 'POST' or None:
        cbc = CBC(
            name    = request.POST['name'],
            sex     = request.POST['sex'],
            age     = request.POST['age'],
            date    = request.POST['date'],
            wbc     = request.POST['wbc'],
            hb      = request.POST['hb'],
            rbc     = request.POST['rbc'],
            plt     = request.POST['plt'],
            lym     = request.POST['lym'],
            lym_p   = request.POST['lym_p'],
            hct     = request.POST['hct'],
            pcv     = request.POST['pcv'],
            mch     = request.POST['mch'],
            mchc    = request.POST['mchc'],
            mcv     = request.POST['mcv'],
            rdw     = request.POST['rdw']
            )

        cbc.save()
        return redirect('cbc')
    cbc_lst = CBC.objects.all()
    context = {'cbc_lst': cbc_lst}
    return render(request, 'cbc_root/cbc.html', context)
    

def cbc_profile(request, pk):

    #overview
    cbc = CBC.objects.get(id=pk)

    #update
    if request.method == "POST":
        cbc.name    = request.POST['name']
        cbc.sex     = request.POST['sex']
        cbc.age     = request.POST['age']
        cbc.date    = request.POST['date']
        cbc.wbc     = request.POST['wbc']
        cbc.hb      = request.POST['hb']
        cbc.rbc     = request.POST['rbc']
        cbc.plt     = request.POST['plt']
        cbc.lym     = request.POST['lym']
        cbc.lym_p   = request.POST['lym_p']
        cbc.hct     = request.POST['hct']
        cbc.pcv     = request.POST['pcv']
        cbc.mch     = request.POST['mch']
        cbc.mchc    = request.POST['mchc']
        cbc.mcv     = request.POST['mcv']
        cbc.rdw     = request.POST['rdw']
        cbc.save()

    context = {'cbc':cbc}
    return render(request, 'cbc_root/cbc-profile.html', context)

def delete_cbc(request, pk):     
    #delete
    cbc = CBC.objects.get(id=pk)
    if request.method == "POST":
        cbc.delete()
        return redirect ('index')
    context = {'cbc': cbc}    
    return render(request, 'cbc_root/delete-cbc-profile.html', context)

"""
def link_callback(uri, rel):
            
            #Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
            
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
 """

def generate_cbc_report(request, pk):
    cbc = CBC.objects.get(id = pk)
    template_path = 'cbc_root/cbc-report.html'
    current_time = datetime.now().strftime('%H:%M:%S')
    context = {'cbc': cbc, 'current_time':current_time}
    """
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback = link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    """
    return render(request, "cbc_root/cbc-report.html", context)


#####################KFT###########################

def kft(request):
    if request.method == 'POST' or None:
        kft = KFT(
        name        = request.POST['name'],
        sex         = request.POST['sex'],
        age         = request.POST['age'],
        date        = request.POST['date'],
        sodium      = request.POST['sodium'],
        potassium   = request.POST['potassium'],
        creatinine  = request.POST['creatinine'],
        urea        = request.POST['urea'])
        kft.save()
        return redirect('kft')
    kft_lst = KFT.objects.all()
    context = {'kft_lst': kft_lst}
    return render(request, 'kft_root/kft.html', context)


def kft_profile(request, pk):
    
    #overview
    kft = KFT.objects.get(id=pk)

    #update
    if request.method == "POST":
        kft.name    = request.POST['name']
        kft.sex     = request.POST['sex']
        kft.age     = request.POST['age']
        kft.date    = request.POST['date']
        kft.sodium      = request.POST['sodium']
        kft.potassium   = request.POST['potassium']
        kft.creatinine  = request.POST['creatinine']
        kft.urea        = request.POST['urea']
        kft.save()
    context = {'kft':kft}
    return render(request, 'kft_root/kft-profile.html', context)

###report
def generate_kft_report(request, pk):
    kft = KFT.objects.get(id = pk)
    template_path = 'kft_root/kft-report.html'
    current_time = datetime.now().strftime('%H:%M:%S')
    context = {'kft': kft, 'current_time':current_time}

    return render(request, "kft_root/kft-report.html", context)


def delete_kft(request, pk):     
    #delete
    kft = KFT.objects.get(id=pk)
    if request.method == "POST":
        kft.delete()
        return redirect ('index')
    context = {'kft': kft}    
    return render(request, 'kft_root/delete-kft-profile.html', context)



###END0FKFT######

######LIVERFUNCTION TEST######

def lft(request):
    if request.method == 'POST' or None:
        lft = LFT(
        name        = request.POST['name'],
        sex         = request.POST['sex'],
        age         = request.POST['age'],
        date        = request.POST['date'],
        total_bil   = request.POST['total_bil'],
        direct_bil  = request.POST['direct_bil'],
        alk_phos    = request.POST['alk_phos'],
        gpt         = request.POST['gpt'],
        got         = request.POST['got'],
        ggt         = request.POST['ggt'],
        prot        = request.POST['prot'],
        alb         = request.POST['alb'])
        lft.save()
        return redirect('lft')
    lft_lst = LFT.objects.all()
    context = {'lft_lst': lft_lst}
    return render(request, 'lft_root/lft.html', context)


def lft_profile(request, pk):
    
    #overview
    lft = LFT.objects.get(id=pk)

    #update
    if request.method == "POST":
        lft.name    = request.POST['name']
        lft.sex     = request.POST['sex']
        lft.age     = request.POST['age']
        lft.date    = request.POST['date']
        lft.total_bil   = request.POST['total_bil']
        lft.direct_bil  = request.POST['direct_bil']
        lft.alk_phos    = request.POST['alk_phos']
        lft.gpt         = request.POST['gpt']
        lft.got         = request.POST['got']
        lft.ggt         = request.POST['ggt']
        lft.prot        = request.POST['prot']
        lft.alb         = request.POST['alb']
        lft.save()
    context = {'lft':lft}
    return render(request, 'lft_root/lft-profile.html', context)


def delete_lft(request, pk):     
    #delete
    lft = LFT.objects.get(id=pk)
    if request.method == "POST":
        lft.delete()
        return redirect ('index')
    context = {'lft': lft}    
    return render(request, 'lft_root/delete-lft-profile.html', context)


###report
def generate_lft_report(request, pk):
    lft = LFT.objects.get(id = pk)
    template_path = 'lft_root/lft-report.html'
    current_time = datetime.now().strftime('%H:%M:%S')
    context = {'lft': lft, 'current_time':current_time}

    return render(request, "lft_root/lft-report.html", context)



#####################LIPID PROFILE################################

def lpd(request):
    if request.method == 'POST' or None:
        lpd = Lipid_Profile(
        name        = request.POST['name'],
        sex         = request.POST['sex'],
        age         = request.POST['age'],
        date        = request.POST['date'],
        hdl         = request.POST['hdl'],
        trig        = request.POST['trig'],
        total_chol  = request.POST['total_chol'])
        lpd.save()
        return redirect('lpd')
    lpd_lst = Lipid_Profile.objects.all()
    context = {'lpd_lst': lpd_lst}
    return render(request, 'lpd_root/lpd.html', context)


def lpd_profile(request, pk):

    #overview
    lpd = Lipid_Profile.objects.get(id=pk)
    #update
    if request.method == "POST":
        lpd.name    = request.POST['name']
        lpd.sex     = request.POST['sex']
        lpd.age     = request.POST['age']
        lpd.date    = request.POST['date']
        lpd.hdl         = request.POST['hdl']
        lpd.trig        = request.POST['trig']
        lpd.total_chol  = request.POST['total_chol']
        lpd.save()
    
    context = {'lpd':lpd}
    return render(request, 'lpd_root/lpd-profile.html', context)


def delete_lpd(request, pk):     
    #delete
    lpd = Lipid_Profile.objects.get(id=pk)
    if request.method == "POST":
        lpd.delete()
        return redirect ('index')
    context = {'lpd': lpd}    
    return render(request, 'lpd_root/delete-lpd-profile.html', context)

###report
def generate_lpd_report(request, pk):
    lpd = Lipid_Profile.objects.get(id = pk)
    template_path = 'lpd_root/lpd-report.html'
    ld = lpd.total_chol - lpd.hdl - lpd.trig/2.2
    ldl = round(float(ld),2)
    current_time = datetime.now().strftime('%H:%M:%S')
    context = {'lpd': lpd, 'current_time':current_time, 'ldl': ldl}

    return render(request, "lpd_root/lpd-report.html", context)

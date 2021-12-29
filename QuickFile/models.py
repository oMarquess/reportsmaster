from django.db import models
import uuid

# Create your models here.

SEX_CHOICE = [
    
    ('male', 'Male'),
    ('female', 'Female'),
    ('trans', 'Trans')
]

class ClientInfo (models.Model):
    name         = models.CharField(max_length=20)
    sex          = models.CharField(max_length=10, choices=SEX_CHOICE)
    age          = models.CharField(max_length = 10)
    date         = models.DateField(auto_now=False, auto_now_add=False)
    created_on   = models.DateTimeField(auto_now_add = True)
    report_id    = models.UUIDField(default = uuid.uuid4, editable = False)

    class Meta:
        abstract = True

class CBC (ClientInfo):
    wbc     =       models.FloatField()
    hb      =       models.FloatField()
    rbc     =       models.FloatField()
    plt     =       models.FloatField()
    lym     =       models.FloatField()
    lym_p   =       models.FloatField()
    hct     =       models.FloatField()
    pcv     =       models.FloatField()
    mch     =       models.FloatField()
    mchc    =       models.FloatField()
    mcv     =       models.FloatField()
    rdw     =       models.FloatField()
    

    def __str__(self):
        return str(self.report_id)
    
    class Meta:
        verbose_name_plural = 'CBC'
    
class KFT (ClientInfo):
    sodium      =   models.FloatField()
    potassium   =   models.FloatField()
    creatinine  =   models.FloatField()
    urea        =   models.FloatField()

    def __str__(self):
        return str(self.report_id)

    class Meta:
        verbose_name_plural =   'KFT'

class LFT(ClientInfo):
    total_bil       =       models.FloatField()
    direct_bil      =       models.FloatField()
    alk_phos        =       models.FloatField()
    gpt             =       models.FloatField()
    got             =       models.FloatField()
    ggt             =       models.FloatField()
    prot            =       models.FloatField()
    alb             =       models.FloatField()

    def __str__(self):
        return str(self.report_id)

    class Meta:
        verbose_name_plural =   'LFT'

class Lipid_Profile(ClientInfo):
    hdl             =   models.FloatField()
    trig            =   models.FloatField()
    total_chol      =   models.FloatField()
    #ldl             =   models.FloatField(default=0.0)

    def __str__(self):
        return str(self.report_id)
    class Meta:
        verbose_name_plural = 'Lipid Profile'
            
    

    


    
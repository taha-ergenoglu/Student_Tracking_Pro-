import pandas as pd
from datetime import date
import random 
from faker import Faker
fake=Faker()
data_set = {
    "ogrenciler": [],
    "sinavlar": [],
    "soru_kazanimlari": [],
    "ogrenci_sonuclari": []
}
classes=['8A', '9A', '10A', '11A', '12A']
tyt_turkish_achievement= [
    "Metindeki sözcüklerin ve söz öbeklerinin anlamlarını belirler.",
    "Cümlenin ifade ettiği anlam özelliklerini belirler.",
    "Metnin ana düşüncesini ve yardımcı düşüncelerini kavrar.",
    "Metindeki ses olaylarını ayırt eder.",
    "Metin üzerinde yazım kurallarını ve noktalama işaretlerini uygular.",
    "Paragrafta anlatım biçimleri ve düşünceyi geliştirme yollarını belirler.",
    "Sözcük türlerini (isim, sıfat, zamir, zarf, edat, bağlaç, ünlem) metin içinde ayırt eder.",
    "Fiillerin (eylem) anlam özelliklerini ve çekimlerini kavrar.",
    "Fiilimsilerin (eylemsi) metin içindeki işlevlerini belirler.",
    "Cümlenin ögelerini doğru bir şekilde bulur.",
    "Cümle türlerini (yapısına, anlamına, yükleminin türüne göre) sınıflandırır.",
    "Anlatım bozukluklarının nedenlerini belirler ve düzeltir.",
    "Metnin yapı özelliklerini (giriş, gelişme, sonuç) analiz eder.",
    "Söz sanatlarını (teşbih, istiare, mübalağa vb.) tespit eder.",
    "Deyimler ve atasözlerinin metne kattığı anlamı yorumlar.",
    "Görsel ve işitsel metinleri yorumlar.",
    "Metinler arası karşılaştırma yapar.",
    "Farklı metin türlerinin (makale, deneme, fıkra vb.) özelliklerini kavrar.",
    "Kelimede anlam olaylarını (mecaz, yan anlam, terim anlam) ayırt eder.",
    "Cümlede anlam ilişkilerini (neden-sonuç, amaç-sonuç, koşul vb.) çözer."
]

tyt_math_achievement = [
    "Sayı kümeleri ve aralarındaki ilişkileri kavrar.",
    "Tam sayılarda bölünebilme kurallarını problem çözümlerinde kullanır.",
    "Birinci dereceden bir bilinmeyenli denklem ve eşitsizlikleri çözer.",
    "Üslü ve köklü ifadeleri içeren işlemleri yapar.",
    "Oran ve orantı kavramlarını kullanarak gerçek hayat problemlerini çözer.",
    "Rasyonel sayılarda dört işlem yapar.",
    "EBOB ve EKOK kavramlarını problem çözümlerinde kullanır.",
    "Mutlak değer içeren denklem ve eşitsizlikleri çözer.",
    "Kümelerde temel işlemleri (kesişim, birleşim, fark) yapar.",
    "Kartezyen çarpım kavramını ve özelliklerini açıklar.",
    "Fonksiyon kavramını ve fonksiyon türlerini kavrar.",
    "Fonksiyonlarda bileşke ve ters fonksiyon işlemlerini yapar.",
    "Polinom kavramını açıklar ve polinomlarda işlemler yapar.",
    "İkinci dereceden denklemlerin köklerini bulur.",
    "Sayı, kesir ve yaş problemlerini modelleyerek çözer.",
    "İşçi, hareket ve karışım problemlerini çözer.",
    "Yüzde, kar-zarar ve faiz problemlerini analiz eder.",
    "Mantık kurallarını kullanarak önermelerin doğruluk değerlerini belirler.",
    "Basit olayların olma olasılığını hesaplar.",
    "Verileri tablo ve grafiklerle temsil eder ve yorumlar."
]

tyt_geometry_achievement= [
    "Doğruda açı kavramlarını ve özelliklerini kavrar.",
    "Üçgende açı özellikleri ile ilgili işlemler yapar.",
    "Üçgende açı-kenar bağıntılarını açıklar.",
    "Dik üçgende Pisagor ve Öklid teoremlerini uygulayarak problem çözer.",
    "İkizkenar ve eşkenar üçgenin özelliklerini kullanarak problem çözer.",
    "Üçgende alan hesaplamalarını yapar.",
    "Üçgende benzerlik kurallarını (A.A., K.A.K., K.K.K.) uygular.",
    "Üçgende açıortay ve kenarortay bağıntılarını kavrar.",
    "Çokgenlerin temel elemanlarını ve özelliklerini kavrar.",
    "Dörtgenlerin alan ve çevre hesaplamalarını yapar.",
    "Çemberde açı özelliklerini kullanarak problem çözer.",
    "Çemberde teğet ve kiriş özelliklerini kavrar.",
    "Dairenin çevresini ve alanını hesaplar.",
    "Daire diliminin ve parçasının alanını bulur.",
    "Katı cisimlerin yüzey alanı bağıntılarını hesaplar.",
    "Katı cisimlerin hacim bağıntılarını kullanarak problem çözer.",
    "Analitik düzlemde iki nokta arasındaki uzaklığı hesaplar.",
    "Bir doğrunun eğimini ve denklemini bulur.",
    "İki doğrunun birbirine göre durumlarını inceler.",
    "Dönüşüm geometrisi (öteleme, dönme, simetri) kurallarını uygular."
]

tyt_physics_achievement= [
    "Fiziksel nicelikleri sınıflandırır ve birim sistemlerini kullanır.",
    "Madde ve özkütle kavramlarını ilişkilendirir.",
    "Dayanıklılık, yüzey gerilimi ve kılcallık olaylarını açıklar.",
    "Düzgün doğrusal hareket yapan cisimlerin hareket grafiklerini çizer ve yorumlar.",
    "Newton'ın Hareket Yasaları'nı günlük hayattaki örneklere uygular.",
    "İş, enerji ve güç kavramlarını birbirleriyle ilişkilendirir.",
    "Mekanik enerjinin korunumunu problem çözümlerinde kullanır.",
    "Isı, sıcaklık ve iç enerji kavramlarını ayırt eder.",
    "Hal değişimi ve ısıl denge durumlarını analiz eder.",
    "Katı, sıvı ve gazlarda basınç kavramını açıklar.",
    "Akışkanların basıncını ve Bernoulli ilkesini kavrar.",
    "Kaldırma kuvveti prensibini kullanarak sıvı-cisim dengesini yorumlar.",
    "Elektrik yükleri, elektriklenme çeşitleri ve Coulomb yasasını açıklar.",
    "Elektrik akımı, direnç ve potansiyel fark kavramlarını ilişkilendirir.",
    "Basit elektrik devrelerinde eşdeğer direnç ve akım hesabı yapar.",
    "Mıknatıslar ve manyetik alan kavramlarını açıklar.",
    "Dalgaların temel kavramlarını ve dalga çeşitlerini sınıflandırır.",
    "Yay ve su dalgalarının özelliklerini kavrar.",
    "Ses ve deprem dalgalarının genel özelliklerini listeler.",
    "Gölge oluşumu, yansıma ve kırılma olaylarını açıklar."
]

tyt_chemistry_achievement = [
    "Kimya biliminin gelişim sürecini ve kimya disiplinlerini açıklar.",
    "Atom modellerinin gelişimini ve temel özelliklerini özetler.",
    "Atomun yapısını ve atom altı tanecikleri kavrar.",
    "Periyodik sistemin özelliklerini ve elementlerin yerleşimini kavrar.",
    "Periyodik özelliklerin değişim eğilimlerini yorumlar.",
    "Kimyasal türler arası güçlü etkileşimleri açıklar.",
    "Zayıf etkileşimlerin özelliklerini sınıflandırır.",
    "Maddenin fiziksel hâllerini ve bu hâller arası geçişleri açıklar.",
    "Katı, sıvı ve gazların genel özelliklerini değerlendirir.",
    "Kimyanın temel kanunlarını açıklar ve hesaplamalar yapar.",
    "Mol kavramını ve Avogadro sayısını problem çözümlerinde kullanır.",
    "Kimyasal tepkime türlerini sınıflandırır.",
    "Kimyasal tepkimelerde kütle ve mol ilişkisi hesaplamaları yapar.",
    "Karışımları sınıflandırır ve özelliklerini belirtir.",
    "Çözeltilerin derişim türlerini hesaplar.",
    "Karışımları ayırma yöntemlerini uygular.",
    "Asitler, bazlar ve tuzların genel özelliklerini belirler.",
    "Asit ve bazların tepkimelerini ve pH kavramını açıklar.",
    "Yaygın asit ve bazların günlük hayattaki kullanım alanlarını belirtir.",
    "Çevre kimyası, hava, su ve toprak kirliliğine neden olan maddeleri açıklar."
]

tyt_biology_achievement = [
    "Canlıların ortak özelliklerini kavrar.",
    "Canlıların yapısında bulunan inorganik ve organik bileşikleri sınıflandırır.",
    "Karbonhidrat, yağ ve proteinlerin yapısal özelliklerini açıklar.",
    "Enzimlerin yapısını, çalışmasını ve etki eden faktörleri analiz eder.",
    "Hücre teorisini ve hücrenin temel kısımlarını açıklar.",
    "Hücre zarı ve madde geçişleri süreçlerini kavrar.",
    "Prokaryot ve ökaryot hücre yapılarının farklarını karşılaştırır.",
    "Canlıların sınıflandırılmasında kullanılan kriterleri belirtir.",
    "Canlı alemlerinin (bakteriler, bitkiler, hayvanlar vb.) özelliklerini açıklar.",
    "Virüslerin yapısını ve canlılar alemindeki yerini değerlendirir.",
    "Hücre bölünmesinin (mitoz ve mayoz) aşamalarını kavrar.",
    "Eşeysiz ve eşeyli üreme çeşitlerini ayırt eder.",
    "Kalıtımın genel esaslarını ve Mendel ilkelerini problem çözümlerinde kullanır.",
    "Eş baskınlık, çok alellik ve cinsiyete bağlı kalıtım durumlarını açıklar.",
    "Soy ağaçlarını kullanarak genetik çaprazlama problemlerini çözer.",
    "Mutasyon, modifikasyon ve adaptasyon kavramlarını örneklendirir.",
    "Ekosistemin yapısını ve temel kavramlarını açıklar.",
    "Ekosistemde madde döngülerini ve enerji akışını analiz eder.",
    "Besin zinciri ve besin piramidini yorumlar.",
    "Çevre kirliliğinin nedenlerini ve biyolojik çeşitliliğin önemini kavrar."
]

tyt_history_achievement = [
    "Tarih biliminin konusunu, yöntemini ve ilişkili olduğu bilimleri açıklar.",
    "Zaman ve takvim kavramlarını kavrar, Türklerin kullandığı takvimleri sıralar.",
    "İlk Çağ uygarlıklarının insanlık tarihine katkılarını değerlendirir.",
    "Orta Asya'da kurulan ilk Türk devletlerinin özelliklerini kavrar.",
    "İslamiyet'in doğuşu, yayılışı ve Dört Halife Dönemi'ni analiz eder.",
    "Emeviler ve Abbasiler dönemlerindeki siyasi gelişmeleri yorumlar.",
    "Türklerin İslamiyet'i kabulü ve ilk Türk-İslam devletlerinin kuruluşunu açıklar.",
    "Anadolu'nun Türkleşme sürecini değerlendirir.",
    "Osmanlı Devleti'nin kuruluş sürecindeki gelişmeleri ve iskan politikasını açıklar.",
    "Osmanlı Devleti'nin yükselme dönemindeki fetihleri analiz eder.",
    "Osmanlı devlet idaresi ve toplum yapısı sistemini kavrar.",
    "Yeni Çağ Avrupa'sındaki gelişmelerin Osmanlı'ya etkisini yorumlar.",
    "XVII. ve XVIII. yüzyıllarda Osmanlı Devleti'nin durumunu değerlendirir.",
    "XIX. yüzyıl Osmanlı Devleti'ndeki dağılmayı önleme çabalarını analiz eder.",
    "XX. yüzyıl başlarında Osmanlı Devleti'nin girdiği savaşları özetler.",
    "Mondros Ateşkes Antlaşması ve cemiyetlerin kuruluşunu açıklar.",
    "Milli Mücadele'nin hazırlık dönemini kronolojik olarak sıralar.",
    "TBMM'nin açılışını ve ayaklanmaları değerlendirir.",
    "Kurtuluş Savaşı cephelerindeki askeri başarıları ve diplomatik sonuçları yorumlar.",
    "Mudanya ve Lozan antlaşmalarının Türk tarihindeki önemini açıklar."
]

tyt_geography_achievement = [
    "Doğa ve insan etkileşimini örneklerle açıklar.",
    "Dünya'nın şekli ve boyutlarının sonuçlarını kavrar.",
    "Dünya'nın günlük ve yıllık hareketlerinin etkilerini değerlendirir.",
    "Coğrafi koordinat sistemini kullanarak yerel saat hesaplamaları yapar.",
    "Haritalarda yer şekillerinin gösterim yöntemlerini kullanır.",
    "İklim elemanlarını (sıcaklık, basınç, rüzgar, nem, yağış) açıklar.",
    "Yeryüzündeki büyük iklim tiplerini sınıflandırır.",
    "Türkiye'nin iklim özelliklerini analiz eder.",
    "Dünyanın iç yapısını ve levha tektoniğini açıklar.",
    "İç kuvvetlerin yeryüzünün şekillenmesine etkisini inceler.",
    "Dış kuvvetlerin oluşturduğu yer şekillerini ayırt eder.",
    "Türkiye'nin yeryüzü şekillerinin oluşum süreçlerini değerlendirir.",
    "Dünyadaki ve Türkiye'deki su kaynaklarının dağılışını yorumlar.",
    "Toprak oluşum süreçlerini ve türlerini açıklar.",
    "Doğal bitki örtüsü türlerini ve iklimle olan ilişkisini kavrar.",
    "Nüfusun dağılışını etkileyen faktörleri analiz eder.",
    "Göçlerin nedenlerini ve sonuçlarını açıklar.",
    "Dünyadaki ulaşım ağlarını ve önemini karşılaştırır.",
    "Bölge kavramını ve bölge sınırlarının oluşturulma kriterlerini sınıflandırır.",
    "Doğal afetlerin türlerini, oluşum nedenlerini ve korunma yollarını açıklar."
]
tyt_philosophy_achievement = [
    "Felsefi düşüncenin niteliklerini açıklar.",
    "Felsefenin insan ve toplum hayatındaki rolünü değerlendirir.",
    "Akıl yürütme türlerini ve argümantasyon kavramını kavrar.",
    "Düşünme ve ifade etmede dilin önemini açıklar.",
    "Bilgi felsefesinin (Epistemoloji) temel problemlerini açıklar.",
    "Bilginin doğruluk ölçütlerini değerlendirir.",
    "Varlık felsefesinin (Ontoloji) temel problemlerini açıklar.",
    "Varlığın mahiyetiyle ilgili temel görüşleri sınıflandırır.",
    "Ahlak felsefesinin (Etik) temel kavramlarını açıklar.",
    "Evrensel bir ahlak yasasının olanaklılığını tartışır.",
    "Sanat felsefesinin (Estetik) temel problemlerini açıklar.",
    "Sanat eserinin niteliklerini ve estetik yargıları değerlendirir.",
    "Din felsefesinin konusunu ve temel sorularını açıklar.",
    "Siyaset felsefesinin temel kavramlarını ve problemlerini açıklar.",
    "Devletin kaynağı ve meşruiyeti hakkındaki görüşleri karşılaştırır.",
    "Bilim felsefesinin konusunu ve bilim ile felsefe ilişkisini açıklar.",
    "MÖ 6. yüzyıl - MS 2. yüzyıl felsefesinin genel özelliklerini özetler.",
    "MS 2. yüzyıl - MS 15. yüzyıl felsefesindeki temel problemleri açıklar.",
    "15. yüzyıl - 17. yüzyıl felsefesinin karakteristik özelliklerini kavrar.",
    "18. yüzyıl - 19. yüzyıl felsefesinin genel özelliklerini değerlendirir."
]

tyt_religious_culture_achievement = [
    "İslam'da bilginin kaynaklarını açıklar.",
    "İslam inancında imanın mahiyetini ve şartlarını kavrar.",
    "İslam'da ibadetin amacı ve önemini değerlendirir.",
    "İbadetlerin bireysel ve toplumsal faydalarını açıklar.",
    "Kur'an-ı Kerim'in ana konularını ve temel özelliklerini kavrar.",
    "Hz. Muhammed'in hayatını ve şahsiyetini örnek alır.",
    "Hz. Muhammed'in peygamberlik özelliklerini açıklar.",
    "İslam ahlakının kaynaklarını ve temel prensiplerini kavrar.",
    "İslam ahlakında yer alan bazı tutum ve davranışları değerlendirir.",
    "Kur'an'da geçen temel kavramları anlamlandırır.",
    "İslam düşüncesinde tasavvufi yorum biçimlerini açıklar.",
    "İslam düşüncesindeki itikadi ve fıkhi yorum farklılıklarını kavrar.",
    "Din ve aile, din ve ekonomi, din ve çevre ilişkilerini değerlendirir.",
    "Güncel dini meselelere İslam'ın yaklaşımını açıklar.",
    "Farklı din ve inanç sistemlerinin temel özelliklerini kavrar.",
    "Dinlerin barış, hoşgörü ve bir arada yaşama kültürüne katkısını değerlendirir.",
    "İslam sanatları ve estetik anlayışının özelliklerini açıklar.",
    "Türklerin İslamiyet'i kabul sürecini ve İslam'a katkılarını özetler.",
    "Ahiret inancının insan hayatı üzerindeki etkilerini yorumlar.",
    "Vahiy ve akıl ilişkisini İslam düşüncesi bağlamında değerlendirir."
]

#Ogrenci olusturma
for i in range (1,201):
    student_id=i
    name_surname=fake.name()
    random_class=random.choice(classes)
    random_success_rate=random.randint(10, 98) #Her bir ogrenci için 40-98 aralığında random başarı oranı seçilir. Bu öğrencilerin cevaplarının alındığı kısımda kullanıldı
    ogrenci_sozluk={"Id":student_id,"Name_Surname":name_surname,"Student_Success_Rate":random_success_rate,"Class":random_class}
    data_set["ogrenciler"].append(ogrenci_sozluk)
  
def create_question(exam_id,question_count,achievements,lesson):
    test={"exam_id": exam_id,
          "lesson":lesson,
          "Question_Number":question_count,
          "Question_Achievement":random.choice(achievements),
          "Answer":random.choice(["A","B","C","D","E"])}
    data_set["soru_kazanimlari"].append(test)

#sınav oluşturma
for i in range(1,41):
    exam={"exam_id":str(i),
          "exam_name":"tyt",
          "exam_date":fake.date_between(start_date=date(2026, 9, 10),end_date=date(2027, 6, 10))}
    data_set["sinavlar"].append(exam)
question_count=1

#Verilen kazanımlar rastgele seçilerek sınav id si ile soru_kazanimlari listesine eklenir
for i in range(1,41):
    while question_count<121:
        if 0<question_count and question_count<41:
            create_question(i,question_count, tyt_turkish_achievement,"Türkçe")
        elif 40<question_count and question_count<76:
            create_question(i,question_count, tyt_math_achievement,"Matematik")
        elif 75<question_count and question_count<81:
            create_question(i,question_count, tyt_geometry_achievement,"Geometri")
        elif 80<question_count and question_count<86:
            create_question(i,question_count, tyt_history_achievement,"Tarih")
        elif 85<question_count and question_count<91:
            create_question(i,question_count, tyt_geography_achievement,"Cografya")
        elif 90<question_count and question_count<96:
            create_question(i,question_count, tyt_philosophy_achievement,"Felsefe")
        elif 95<question_count and question_count<101:
            create_question(i,question_count, tyt_religious_culture_achievement,"Din Kültürü ve Ahlak Bilgisi")
        elif 100<question_count and question_count<108:
            create_question(i,question_count, tyt_physics_achievement,"Fizik")
        elif 107<question_count and question_count<115:
            create_question(i,question_count, tyt_chemistry_achievement,"Kimya")
        elif 114<question_count and question_count<121:
            create_question(i,question_count, tyt_biology_achievement,"Biyoloji")
        question_count+=1

#Öğrencilerin cevapları alınır ogrenci_sonuclari listesine eklenir
for x in range(1,41):
    for i in range(1,len(data_set["ogrenciler"])+1):
        
        student_id=data_set["ogrenciler"][i-1]["Id"]
        student_name=data_set["ogrenciler"][i-1]["Name_Surname"]
        student_success=data_set["ogrenciler"][i-1]["Student_Success_Rate"]
        student_class=data_set["ogrenciler"][i-1]["Class"]
        for a in range(1,len(data_set["soru_kazanimlari"])+1):
            options=["A","B","C","D","E",""]
            selection_weights=[]
            trueAnswer=data_set["soru_kazanimlari"][a-1]["Answer"]
            for j in range(0,len(options)):
                if options[j]==trueAnswer:
                    selection_weights.append(student_success)#Doğru cevabın seçim ağırlığına öğrencinin başarı oranı atanır. Çünkü başarılı bir öğrencinin doğru cevabı seçme olasılığı daha yüksektir
                else:
                    incorrect_answe_rate_for_each_options=(100-student_success)/5 #Doğru cevap dışında kalan 4 seçenek ve boş bırakma, seçilme durumlarının ağırlığı hesaplanır
                    selection_weights.append(incorrect_answe_rate_for_each_options)
            answer=random.choices(options,weights=selection_weights,k=1)[0]
            question_achievement=data_set["soru_kazanimlari"][a-1]["Question_Achievement"]
            if trueAnswer == answer:
                result="true"
            elif answer=="":
                result="empty"
            else:
                result="false"
            answer_data={"exam_id": x,
                         "student_id":student_id,
                         "student_name":student_name,
                         "student_class":student_class,
                         "question_number":a,
                         "true_answer":trueAnswer,
                         "student_answer":answer,
                         "result":result,
                         "achievement":question_achievement}
            data_set["ogrenci_sonuclari"].append(answer_data)
        
        
        
df_students=pd.DataFrame(data_set["ogrenciler"])
df_exams=pd.DataFrame(data_set["sinavlar"])
df_questions=pd.DataFrame(data_set["soru_kazanimlari"])
df_student_results=pd.DataFrame(data_set["ogrenci_sonuclari"])        


df_students.to_csv("ogrenciler.csv", index=False, encoding="utf-8")
df_exams.to_csv("sinavlar.csv", index=False, encoding="utf-8")
df_questions.to_csv("soru_kazanimlari.csv", index=False, encoding="utf-8")
df_student_results.to_csv("ogrenci_sonuclari.csv", index=False, encoding="utf-8")      
        
        
        
        
        
        
        
        
        
        
        
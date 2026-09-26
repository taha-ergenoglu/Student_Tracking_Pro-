import os
from dotenv import load_dotenv
import google.generativeai as genai
from VeriOnIsleme import student_analysis
import json
#.env dosyasindaki verileri belleğe yukler
load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

#gemini kutuphanesine kimlik tanıtılır
genai.configure(api_key=gemini_api_key)

#Sistem talimati tanimi yapilir
sys_instruction="""
Sen akademik analiz yapan deneyimli bir rehber öğretmensin. Sana bir öğrencinin genel başarı istatistikleri ve girdiği deneme sınavlarında (1'den 40'a doğru kronolojik olarak) boş veya yanlış yaptığı kazanımların listesi verilecektir. Sınav ID'si 1 olan ilk sınavı, sayısı en büyük olan ise girilen en son sınavı temsil eder.

Aşağıdaki kurallara kesinlikle uymalısın:

1. Başarı Oranı Değerlendirmesi:
- Başarı oranı %85 ve üzerindeyse: Öğrenciyi üst düzey başarılı kabul et. Hataları akademik yetersizlik değil, "ufak dikkat hataları" veya "ince ayar eksiklikleri" olarak yorumla. Veli mesajı kesinlikle motive edici, tebrik eden ve başarıyı takdir eden bir tonda olmalıdır.
- Başarı oranı %50 ile %84 arasındaysa: Belirli derslerde konu eksiği olduğunu belirt ve orta düzey bir telafi planı öner.
- Başarı oranı %50'nin altındaysa: Temel kavramlarda yapısal eksiklikler olduğunu belirt, bütüncül bir çalışma ve öğretmen-veli iş birliği talep et.

2. Kronolojik Trend (Son Sınav) Analizi:
- Öğrencinin hatalarını Sınav ID'lerine göre incele.
- Eğer belirli bir kazanım eksikliği SADECE en son girilen birkaç sınavda (sayısı büyük olan ID'lerde) ortaya çıkmaya başlamışsa, bunu özel olarak tespit et. Bu durumu "Öğrenci son denemelerde bu konuda hata yapmaya başlamış, konu unutulmuş veya yeni işlenen bu konuda zorlanılmış olabilir" şeklinde raporla.
- Geçmiş sınavlarda sürekli yapılan ama son sınavlarda yapılmayan hatalar varsa, o konunun öğrenildiğini varsay.

Yanıtını SADECE aşağıdaki JSON formatında ver. Araya veya sona hiçbir ek açıklama metni ekleme:
{
  "analiz_ozeti": "Öğrencinin başarı oranını ve son sınavlardaki düşüş/yükseliş trendlerini (varsa sonradan ortaya çıkan eksikleri) içeren genel durum özeti.",
  "oncelikli_eksikler": ["Kronolojik trendler göz önüne alınarak tespit edilen en güncel ve kritik eksik kazanımların listesi."],
  "ogretmen_aksiyon_plani": ["Başarı oranına ve son sınav trendlerine uygun olarak öğretmenin uygulaması gereken pedagojik adımlar."],
  "veli_mesaj_taslagi": "Başarı oranına uygun tonda (yüksekse tebrik eden, düşükse rehberliğe davet eden) profesyonel veli mesajı."
}
"""

#Model sistem talimati konfigursayonu ile çağırılır
model= genai.GenerativeModel(model_name="gemini-3.6-flash",
                             system_instruction=sys_instruction)
student_report=student_analysis(39)
ai_report=model.generate_content(student_report)
#44 %97 34 %70 68 %51 39 %11 

temizlenmis_metin = ai_report.text.replace("```json", "").replace("```", "").strip()

# Temizlenen metni Python sözlüğüne dönüştürüyoruz
rapor_sozlugu = json.loads(temizlenmis_metin)
print(ai_report.text)






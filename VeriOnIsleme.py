import pandas as pd

df_student_result=pd.read_csv("ogrenci_sonuclari.csv")


df_missing_topics=df_student_result[(df_student_result["result"]=="false")|(df_student_result["result"]=="empty")]

def student_analysis(target_student_id):
    student_missings=df_missing_topics[df_missing_topics["student_id"]==target_student_id]
    if student_missings.empty:
        return "öğrenci tüm soruları doğru cevaplamıştır eksik kazanım bulunamadı"
    student_name=student_missings.iloc[0]["student_name"]
    student_class=student_missings.iloc[0]["student_class"]
    missing_achivments=student_missings[["achievement","exam_id"]]
    missing_counter=(df_missing_topics["student_id"]==target_student_id).sum() #Ogrencinin toplam hata sayısını verir
    number_of_question_solved=(df_student_result["student_id"]==target_student_id).sum()
    success_rate=((number_of_question_solved-missing_counter)/number_of_question_solved)*100
    
    report=f"{student_class} sınıfıdaki {student_name} adlı öğrencinin geliştirmesi gereken kazanımlar\n"
    report += f"Toplam Soru: {number_of_question_solved}\n"
    report += f"Hata/Boş Sayısı: {missing_counter}\n"
    report += f"Başarı Oranı: %{success_rate:.2f}\n"
    report+="-"*50+"\n"
    for row in missing_achivments.itertuples():
        report+=f"Sınav id:{row.exam_id} Eksik kazanım:{row.achievement}\n"
    return report


oran_listesi=[]
for i in range (1,101): #Sistemde 100 öğrenci olduğu için 101 e kadar çalışır
    missing_counter= (df_missing_topics["student_id"]==i).sum()

    
    
    
    
    
    
    
    
    
    
    
    
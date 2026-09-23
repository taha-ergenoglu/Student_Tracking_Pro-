import pandas as pd

df_student_result=pd.read_csv("ogrenci_sonuclari.csv")
df_question_achivment=pd.read_csv("soru_kazanimlari.csv")

df_merge=pd.merge(df_student_result,
                  df_question_achivment,
                  left_on=["exam_id", "question_number"], 
                  right_on=["exam_id", "Question_Number"], 
                  how="inner")

df_missing_topics=df_merge[(df_merge["result"]=="false")|(df_merge["result"]=="empty")]

def student_analysis(target_student_id):
    student_missings=df_missing_topics[df_missing_topics["student_id"]==target_student_id]
    if student_missings.empty:
        return "öğrenci tüm soruları doğru cevaplamıştır eksik kazanım bulunamadı"
    student_name=student_missings.iloc[0]["student_name"]
    student_class=student_missings.iloc[0]["student_class"]
    missing_achivments=student_missings[["Question_Achievement","lesson"]].drop_duplicates()

    report=f"{student_class} sınıfıdaki {student_name} adlı öğrencinin geliştirmesi gereken kazanımlar\n"
    report+="-"*50+"\n"
    
    for order,row in enumerate(missing_achivments.itertuples(),1):
        report+=f"{order} {row.Question_Achievement}  {row.lesson}\n"
    return report

print(student_analysis(46))
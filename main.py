import pandas as pd
from easygui import fileopenbox
from Enrollment_History_Dataframe import EnrollmentHistoryDataFrame
from Degree_Progress import degreeProgress
from Degree_Completion_Report import DegreeCompletionReport

pd.set_option('display.max_columns', None)

enrollment_history_file = fileopenbox('Upload Ernollment Histories', filetypes='*.csv')
e = EnrollmentHistoryDataFrame(enrollment_history_file=enrollment_history_file)
enrollment_history_df = e.create_dataframe()
student_id_list = e.student_ids()
print(student_id_list)


for student_id in student_id_list:
    degreeProgress(student_id=student_id, enrollment_history=enrollment_history_df,
                   major='Comm_Studies', major_requirements='AAT_Comm.csv',
                   major1='Core', major1_units=3, major1_disciplines=1, major1_no_of_courses=1,
                   major2='ListA', major2_units=6, major2_disciplines=1, major2_no_of_courses=2,
                   major3='ListB', major3_units=3, major3_disciplines=1, major3_no_of_courses=1,
                   major4='ListC', major4_units=3, major4_disciplines=1, major4_no_of_courses=1)
    degreeProgress(student_id=student_id, enrollment_history=enrollment_history_df,
                   major="Business Administration-AST", major_requirements='AAT_BusAdmin.csv',
                   major1='Core', major1_units=15, major1_disciplines=1, major1_no_of_courses=5,
                   major2='ListA', major2_units=4, major2_disciplines=1, major2_no_of_courses=1,
                   major3='ListB', major3_units=6, major3_disciplines=1, major3_no_of_courses=2)
    # sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="English for Transfer-AAT",
    #                      major_course_requirements='AAT_English.csv',
    #                      major1='Core', major1_units=3, major1_disciplines=1,
    #                      major2='ListA', major2_units=6, major2_disciplines=1,
    #                      major3='ListB', major3_units=6, major3_disciplines=1,
    #                      major4='ListC', major4_units=3, major4_disciplines=1)
    # sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Spanish for Transfer-AAT",
    #                      major_course_requirements='AAT_Spanish.csv',
    #                      major1='Core', major1_units=19, major1_disciplines=1,
    #                      major2='ListA', major2_units=3, major2_disciplines=1)

# DegreeCompletionReport.LS_AA_Degrees_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
DegreeCompletionReport.LS_AA_Degrees_df.to_csv(
'C:/Users/family/Desktop/Programming/AAT_LA_Division_Degrees.csv')

#

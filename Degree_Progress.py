from Student_Info import StudentInfo
from GE_Requirements import GeRequirements
from Major_Requirements import MajorRequirements
from Course_Info import CourseInfo
from Major_Progress import MajorProgress
from Degree_Completion_Report import DegreeCompletionReport

gePlansList = ['PlanB', 'PlanC']
planB = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum',
                   'Arts_Hum',
                   'Amer_Hist', 'Amer_Gov', 'Institutions', 'Self_Dev']
planB2021 = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum',
                      'Arts_Hum',
                      'Amer_Hist_Gov', 'Institutions', 'Self_Dev', 'Ethnic_Stds']
planC = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum', 'Soc_Behav1', 'Soc_Behav2',
                'Soc_Behav3',
                   'Phys_Sci', 'Bio_Sci', 'Sci_Labs']

def degreeProgress(student_id, enrollment_history, major, major_requirements, **kwargs):
    courseInfo = CourseInfo(student_id, enrollment_history)
    catalogTerm = courseInfo.calculate_catalog_term()
    currentCourses = courseInfo.current_courses()
    student = StudentInfo(student_id, enrollment_history)
    degreeApplicableDict = student.completed_courses()

    for plan in gePlansList:
        if plan == 'PlanB':
            if catalogTerm >=1219:
                gePlanRequirements = 'PlanB_GE2021.csv'
                areaList = planB2021
                plan='PlanB2021'
            else:
                gePlanRequirements = 'PlanB_GE.csv'
                areaList = planB
        else:
            gePlanRequirements = 'PlanC_GE.csv'
            areaList = planC
        geRequirements = GeRequirements(degreeApplicableDict, gePlanRequirements)
        geDataframe = geRequirements.construct_ge_dataframe()

        for area in areaList:
            # currentCoursesApplied = CurrentCoursesApplied(enrolled_courses=currentCourses, area_name=area,
            #                                               dataframe=geDataframe)
            geCoursesCompleted = geRequirements.ge_courses_completed(area_name=area, ge_dataframe=geDataframe)
            # currentCoursesAppliedDict = currentCoursesApplied.current_ge_courses_applied()
            missingGECourses = geRequirements.ge_requirements_completed(ge_plan_list=areaList)
        majorRequirements = MajorRequirements(degree_applicable_courses=degreeApplicableDict, completed_ge_courses=geCoursesCompleted,
                               major=major, major_requirements=major_requirements)
        majorDataframe = majorRequirements.construct_major_dataframe()
        if len(kwargs) == 20:
                majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                              number_of_disciplines=kwargs['major1_disciplines'], number_of_courses=kwargs['major1_no_of_courses'])
                majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                              number_of_disciplines=kwargs['major2_disciplines'], number_of_courses=kwargs['major2_no_of_courses'])
                majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                              number_of_disciplines=kwargs['major3_disciplines'], number_of_courses=kwargs['major3_no_of_courses'])
                majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                              number_of_disciplines=kwargs['major4_disciplines'], number_of_courses=kwargs['major4_no_of_courses'])
                majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major5'], total_units=kwargs['major5_units'],
                                              number_of_disciplines=kwargs['major5_disciplines'], number_of_courses=kwargs['major5_no_of_courses'])

        if len(kwargs) == 16:
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                          number_of_disciplines=kwargs['major1_disciplines'], number_of_courses=kwargs['major1_no_of_courses'])
            # currentCoursesAppliedDict = currentCoursesApplied.current_major_courses_applied(enrolled_courses=currentCourses, area_name=kwargs['major1'],
            #                                                                dataframe=majorDataframe, currentCoursesAppliedDict=currentCoursesAppliedDict)
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                          number_of_disciplines=kwargs['major2_disciplines'], number_of_courses=kwargs['major2_no_of_courses'])
            # currentCoursesAppliedDict = currentCoursesApplied.current_major_courses_applied(enrolled_courses=currentCourses, area_name=kwargs['major2'],
            #                                    dataframe=majorDataframe, currentCoursesAppliedDict=currentCoursesAppliedDict)
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                          number_of_disciplines=kwargs['major3_disciplines'], number_of_courses=kwargs['major3_no_of_courses'])
            # currentCoursesAppliedDict = currentCoursesApplied.current_major_courses_applied(enrolled_courses=currentCourses, area_name=kwargs['major3'],
            #                                    dataframe=majorDataframe, currentCoursesAppliedDict=currentCoursesAppliedDict)
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                          number_of_disciplines=kwargs['major4_disciplines'], number_of_courses=kwargs['major4_no_of_courses'])
            # currentCoursesAppliedDict = currentCoursesApplied.current_major_courses_applied(enrolled_courses=currentCourses, area_name=kwargs['major4'],
            #                                    dataframe=majorDataframe, currentCoursesAppliedDict=currentCoursesAppliedDict)

        if len(kwargs) == 12:
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                          number_of_disciplines=kwargs['major1_disciplines'], number_of_courses=kwargs['major1_no_of_courses'])
            # currentCoursesAppliedDict = currentCoursesApplied.current_major_courses_applied(enrolled_courses=currentCourses, area_name=kwargs['major1'],
            #                                    dataframe=majorDataframe, currentCoursesAppliedDict=currentCoursesAppliedDict)
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                          number_of_disciplines=kwargs['major2_disciplines'], number_of_courses=kwargs['major2_no_of_courses'])
            # currentCoursesAppliedDict = currentCoursesApplied.current_major_courses_applied(enrolled_courses=currentCourses, area_name=kwargs['major2'],
            #                                    dataframe=majorDataframe, currentCoursesAppliedDict=currentCoursesAppliedDict)
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                          number_of_disciplines=kwargs['major3_disciplines'], number_of_courses=kwargs['major3_no_of_courses'])
            # currentCoursesAppliedDict = currentCoursesApplied.current_major_courses_applied(enrolled_courses=currentCourses, area_name=kwargs['major3'],
            #                                    dataframe=majorDataframe, currentCoursesAppliedDict=currentCoursesAppliedDict)

        if len(kwargs) == 8:
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                          number_of_disciplines=kwargs['major1_disciplines'], number_of_courses=kwargs['major1_no_of_courses'])
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                          number_of_disciplines=kwargs['major2_disciplines'], number_of_courses=kwargs['major2_no_of_courses'])

        if len(kwargs) == 4:
            majorRequirements.major_requirements_completed(majorDataframe, area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                          number_of_disciplines=kwargs['major1_disciplines'], number_of_courses=kwargs['major1_no_of_courses'])

        majorProgress = MajorProgress(student_id=student.student_id,
                                     major_course_dict=majorRequirements.major_course_dict,
                                     major_units=majorRequirements.major_units_list,
                                     area_units=majorRequirements.area_units_dict,
                                     no_of_courses_required=majorRequirements.major_no_courses_dict)
        majorProgress.major_requirements_completed()
        completionReport = DegreeCompletionReport(
            major_requirements_dict=majorRequirements.major_no_courses_dict,
            completed_ge_courses=geRequirements.completed_ge_courses,
            completed_ge_units=geRequirements.completed_ge_units,
            major_course_dict=majorRequirements.major_course_dict,
            area_units_dict=majorRequirements.area_units_dict,
            major_units_list=majorRequirements.major_units_list,
            student_id=student_id,
            student_major=major,
            missing_ge=missingGECourses,
            missing_major_courses=majorProgress.missing_courses_dict2,
            ge_plan=plan,
            catalog_term=catalogTerm,
            current_courses=currentCourses)
        completionReport.degree_completion()
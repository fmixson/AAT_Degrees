from Student_Info import StudentInfo


class CourseInfo():
    def __init__(self, student_id, enrollment_history_df):
        self.student_id = student_id
        self.enrollment_history_df = enrollment_history_df
        self.currentCoursesAppliedDict = {}
        # print('course info', self.student_id)

    def current_courses(self):
        current_term = 1219
        self.enrolled_courses = []

        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, "ID"]:
                if self.enrollment_history_df.loc[i, "Term"] == current_term:
                    if self.enrollment_history_df.loc[i, "Course"] not in self.enrolled_courses:
                        if self.enrollment_history_df.loc[i, 'Enrollment Drop Date'] == 0:
                            self.enrolled_courses.append(self.enrollment_history_df.loc[i, "Course"])
        return self.enrolled_courses



    def first_term(self):
        current_term = 1219
        semester = ''
        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, "ID"]:
                if self.enrollment_history_df.loc[i, 'Term'] != 800:
                    if self.enrollment_history_df.loc[i, 'Term'] <= current_term:
                        current_term = self.enrollment_history_df.loc[i, 'Term']
                        semester = self.enrollment_history_df.loc[i, 'Term Description']
        return semester


    def calculate_catalog_term(self):
        term_list = []
        previous_term = 0
        catalog_term = 0
        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, 'ID']:
                if self.enrollment_history_df.loc[i, 'Term'] not in term_list:
                    term_list.append(self.enrollment_history_df.loc[i, 'Term'])
                    term_list.sort()


        for term in term_list:
            term_difference = term - previous_term
            if term_difference > 10:
                catalog_term = term
            previous_term = term

        return catalog_term


# class CurrentCoursesApplied:
#     gePlansList = ['PlanB', 'PlanC']
#     planB = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum',
#              'Arts_Hum',
#              'Amer_Hist', 'Amer_Gov', 'Institutions', 'Self_Dev']
#     planB2021 = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum',
#                  'Arts_Hum',
#                  'Amer_Hist_Gov', 'Institutions', 'Self_Dev', 'Ethnic_Stds']
#     planC = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum', 'Soc_Behav1', 'Soc_Behav2',
#              'Soc_Behav3',
#              'Phys_Sci', 'Bio_Sci', 'Sci_Labs']
#     currentCoursesAppliedDict = {}
#     currentCoursesAppliedList = []
#     def __init__(self, catalog_term, enrolled_courses, area_name, dataframe):
#         self.catalog_term = catalog_term
#         self.enrolled_courses = enrolled_courses
#         self.area_name = area_name
#         self.dataframe = dataframe
#         self.currentCoursesAppliedList = []
#         # self.currentCoursesAppliedDict = {}
#
#     def current_ge_courses_applied(self):
#
#         for i in range(len(self.dataframe)):
#             for course in self.enrolled_courses:
#                 for plan in CurrentCoursesApplied.gePlanList:
#                     if plan == 'PlanB':
#                         if self.catalogTerm >= 1219:
#                             gePlanRequirements = 'PlanB_GE2021.csv'
#                             areaList = planB2021
#                             plan = 'PlanB2021'
#                         else:
#                             gePlanRequirements = 'PlanB_GE.csv'
#                             areaList = planB
#                     else:
#                         gePlanRequirements = 'PlanC_GE.csv'
#                         areaList = planC
#                     # print('area', self.area_name)
#                 if self.dataframe.loc[i, self.area_name] == course:
#                     # if self.area_name not in CurrentCoursesApplied.currentCoursesAppliedList:
#                         print('pairing', course, self.dataframe.loc[i, self.area_name])
#                         self.currentCoursesAppliedList.append(self.area_name)
#                         print('list', self.currentCoursesAppliedList)
#                         CurrentCoursesApplied.currentCoursesAppliedDict[course] = self.currentCoursesAppliedList
#         # print('current', CurrentCoursesApplied.currentCoursesAppliedDict)
#         return CurrentCoursesApplied.currentCoursesAppliedDict
#
#     def current_major_courses_applied(self, enrolled_courses, area_name, currentCoursesAppliedDict, dataframe):
#         # currentCoursesAppliedList = []
#         for i in range(len(dataframe)):
#             for course in enrolled_courses:
#                 # print('course2', course)
#                 if area_name not in self.currentCoursesAppliedList:
#                     # print('area2', area_name)
#                     if course == self.dataframe.loc[i, self.area_name]:
#                         # print(course, dataframe.loc[i, area_name])
#                         self.currentCoursesAppliedList.append(self.area_name)
#                         # print(currentCoursesAppliedList)
#                         currentCoursesAppliedDict[course] = self.currentCoursesAppliedList
#         # print('current2', currentCoursesAppliedDict)
#         return currentCoursesAppliedDict
#
# # class CurrentCoursesApplied(enrolled_courses, area_name, ge_dataframe, major_dataframe):
# #
# #         currentCoursesAppliedList = []
# #         dataframelist = [ge_dataframe, major_dataframe]
# #         for dataframe in dataframelist:
# #             for i in range(len(dataframe)):
# #                 for course in enrolled_courses:
# #                     if area_name not in currentCoursesAppliedList:
# #                         if course == dataframe.loc[i, area_name]:
# #                             # print(course, dataframe.loc[i, area_name])
# #                             currentCoursesAppliedList.append(area_name)
# #                             # print(currentCoursesAppliedList)
# #                             self.currentCoursesAppliedDict[course] = course
# #             print('current', self.currentCoursesAppliedDict)
# #         return self.currentCoursesAppliedDict
import pandas as pd

from Major_Requirements import MajorRequirements



class DegreeCompletionReport:
    columns = ['Student_ID', 'Major', 'GE_Plan', 'Catalog_Term', 'Current_Courses', 'GE_Courses', 'Missing_GE', 'Major_Courses',
               'Missing_Major', 'Total_Missing', 'GE_Missing', 'Major_Missing', 'GE_Units', 'Total_Major_Units',
                'Degree_Major_Units', 'Elective_Units', 'Degree_Units', 'Elective_Courses']
    LS_AA_Degrees_df = pd.DataFrame(columns=columns)
    # degree_units_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
    # columns2 = ['Student_ID', 'Major', 'Degree_Units', 'GE_Courses', 'Major_Courses', 'Elective_Courses']
    # degree_courses_df = pd.DataFrame(columns=columns2)

    def __init__(self, major_requirements_dict, completed_ge_courses, completed_ge_units, major_course_dict,
                 area_units_dict, major_units_list, student_id, student_major,
                 missing_ge, missing_major_courses, ge_plan, catalog_term, current_courses):
        self.missing_major_courses = missing_major_courses
        self.missing_ge = missing_ge
        self.major_units_list = major_units_list
        self.area_units_dict = area_units_dict
        self.major_course_dict = major_course_dict
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.student_id = student_id
        self.student_major = student_major
        self.major_requirements_dict = major_requirements_dict
        self.ge_plan = ge_plan
        self.catalog_term = catalog_term
        self.current_courses = current_courses
        print('maj course dic', self.missing_major_courses)
        print('comp ge units', completed_ge_units)

    def degree_completion(self):

        print('ge units', self.completed_ge_units)
        length = len(DegreeCompletionReport.LS_AA_Degrees_df)

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Student_ID'] = self.student_id
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major'] = self.student_major
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Plan'] = self.ge_plan
        # currentCourseList = self.current_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Catalog_Term'] = self.catalog_term
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Current_Courses'] = self.current_courses
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Units'] = sum(self.completed_ge_units)
        major_units_total_value = sum(self.area_units_dict.values())
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Major_Units'] = major_units_total_value
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Major_Units'] = sum(self.major_units_list)
        # DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Units'] = sum(self.elective_units)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Units'] = sum(self.completed_ge_units) +\
                                                                              sum(self.major_units_list)
        majorMissingTotal = sum(self.missing_major_courses.values())
        missingMajorList = self.missing_major_courses.items()
        total_missing = len(self.missing_ge) + majorMissingTotal

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Missing'] = total_missing
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Missing'] = len(self.missing_ge)

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Missing'] = (majorMissingTotal)

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_GE'] = self.missing_ge

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_Major'] = missingMajorList

        ge_list = self.completed_ge_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Courses'] = ge_list
        major_list = self.major_course_dict.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Courses'] = major_list
        # DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Courses'] = self.elective_courses



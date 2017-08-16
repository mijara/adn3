from courses.gradematrix import GradeMatrix
from pretests.models import Pretest
from classes.models import Session
from tests.models import Test
from .tableform import TableForm


def session_pks(course):
    return [session.pk for session in course.session_set.all()]


def save_tests(post_data):
    tests_table = TableForm('test')
    tests_table.add_field('percentage', 0)
    tests_table.add_field('show_grade', False, transform={'on': True})
    tests_table.process_and_save(Test, post_data)


def save_pretests(post_data):
    pretests_table = TableForm('pretest')
    pretests_table.add_field('percentage', 0)
    pretests_table.add_field('show_grade', False, transform={'on': True})
    pretests_table.process_and_save(Pretest, post_data)


def save_sessions(post_data, expect_pks):
    table = TableForm('session')
    table.add_field('include_assistance', False, transform={'on': True})
    table.expect_pks(expect_pks)
    table.process_and_save(Session, post_data)


def generate_grades_excel(course):
    grade_matrix = GradeMatrix()

    students = course.get_students()

    for student in students:
        grades = student.get_grades_for_course(course)

        full_name = student.user.get_full_name()

        grade_matrix.set_user(full_name)

        for test_name, grade in grades:
            grade_matrix.add(test_name, grade)

    return grade_matrix.render()

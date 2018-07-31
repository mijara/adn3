from openpyxl.writer.excel import save_virtual_workbook
from adn3.services import get_period_year, get_period_semester
from courses.gradematrix import GradeMatrix
from courses.models import Course
from pretests.models import Pretest
from classes.models import Session
from tests.models import Test
from .tableform import TableForm
import openpyxl


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
        full_name = student.user.get_full_name()
        grade_matrix.set_user(full_name)

        grades = student.get_grades_for_course(course)
        for test_name, grade in grades:
            grade_matrix.add(test_name, grade)

        pretest_grades = student.get_pretest_grades_for_course(course)
        for name, grade in pretest_grades:
            grade_matrix.add_pretest(name, grade)

    return grade_matrix.render()


def get_active_courses():
    return Course.objects.filter(status=True, year=get_period_year(), semester=get_period_semester())


def generate_students_excel(course):
    wb = openpyxl.Workbook()
    ws = wb.active

    agendas = course.agenda_set.all()
    students = []

    for agenda in agendas:
        for user in agenda.inscriptions.all():
            students.append({
                'rol': user.student.rol,
                'agenda': agenda.__str__(),
                'last_name': user.last_name,
                'first_name': user.first_name,
                'email': user.email,
                'campus': user.student.campus.name
            })

    ws.append([
        'Estudiantes inscritos en el curso {course}'.format(course=course)
    ])

    ws.append([
        'ROL USM',
        'Agenda',
        'Apellidos',
        'Nombres',
        'Email',
        'Campus'
    ])

    for student in students:
        ws.append([
            student['rol'],
            student['agenda'],
            student['last_name'],
            student['first_name'],
            student['email'],
            student['campus']
        ])

    return save_virtual_workbook(wb)

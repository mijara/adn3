import openpyxl
from openpyxl.writer.excel import save_virtual_workbook

from attendance.models import Attendance
from pretests.models import PretestUpload
from tests.models import Answer


def _questions_row(student_answers, version):
    row = []
    for question in version.question_set.all():
        answer = Answer.objects.filter(student=student_answers.student, question=question)

        if answer.exists():
            answer = answer.first()
            row.append(question.score if answer.correct else 0)

    # add final grade of this test to the row.
    row.append(student_answers.qualification)
    return row


def _append_test_version(course, version, ws, resume):
    header = ['Rol', 'Nombres', 'Apellidos']
    header += ['P%d' % (i + 1) for i in range(version.question_set.count())] + ['Nota']
    ws.append(header)

    for sa in version.studentsanswers_set.all():
        rol = sa.student.student.rol
        personal = [rol, sa.student.first_name, sa.student.last_name]

        # add test qualification to general view.
        if rol not in resume:
            resume[rol] = personal[:]
        resume[rol].append(sa.qualification)

        # add test specifics to the test worksheet.
        ws.append(personal + _questions_row(sa, version))


def _append_tests(course, wb, resume):
    for test in course.test_set.all():
        for version in test.version_set.all():
            test_ws = wb.create_sheet(test.name + ' - ' + version.get_letter())
            _append_test_version(course, version, test_ws, resume)


def _append_pretests(course, resume):
    for pretest in course.pretest_set.all():
        for student in course.get_students():
            upload = PretestUpload.objects.filter(pretest=pretest, student=student)

            if upload.exists():
                upload = upload.first()
                resume[student.rol].append(upload.qualification)
            else:
                resume[student.rol].append(0)


def _append_assistance(course, resume):
    sessions_count = course.session_set.count()

    for agenda in course.agenda_set.all():
        for student in agenda.inscriptions.all():
            attendance = Attendance.objects.filter(agenda=agenda, user=student). \
                exclude(attended=Attendance.NO_ATTENDED).count()
            resume[student.student.rol].append(attendance * 100 / sessions_count)


def generate_course_grades(course):
    wb = openpyxl.Workbook()

    resume_ws = wb.active
    header = ['Rol', 'Nombres', 'Apellidos']
    header += ['C%d' % (i + 1) for i in range(course.test_set.count())]
    header += ['P%d' % (i + 1) for i in range(course.pretest_set.count())]
    header += ['A', 'F']
    resume_ws.append(header)

    resume_by_student = {}
    _append_tests(course, wb, resume_by_student)
    _append_pretests(course, resume_by_student)
    _append_assistance(course, resume_by_student)

    # get the grade configuration.
    gc = course.grades_config
    print(gc.grade_tests)

    # add the resume table to the worksheet.
    for resume in resume_by_student.values():
        len_tests = course.test_set.count()
        len_pretests = course.pretest_set.count()

        tests = sum(resume[3:(3 + len_tests)]) / len_tests
        pretests = sum(resume[(3 + len_tests):(3 + len_tests + len_pretests)]) / len_pretests
        assistance = resume[-1]

        final = tests * gc.grade_tests / 100 + pretests * gc.grade_pretests / 100 + \
                assistance * gc.grade_assistance / 100
        resume_ws.append(resume + [final])

    return save_virtual_workbook(wb)

import openpyxl
from openpyxl.writer.excel import save_virtual_workbook

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


def generate_course_grades(course):
    wb = openpyxl.Workbook()

    resume_ws = wb.active
    header = ['Rol', 'Nombres', 'Apellidos']
    header += ['C%d' % (i + 1) for i in range(course.test_set.count())]
    resume_ws.append(header)

    resume_by_student = {}

    for test in course.test_set.all():
        for version in test.version_set.all():
            test_ws = wb.create_sheet(test.name + ' - ' + version.get_letter())
            header = ['Rol', 'Nombres', 'Apellidos']
            header += ['P%d' % (i + 1) for i in range(version.question_set.count())] + ['Nota']
            test_ws.append(header)

            for sa in version.studentsanswers_set.all():
                rol = sa.student.student.rol
                personal = [rol, sa.student.first_name, sa.student.last_name]

                # add test qualification to general view.
                if rol not in resume_by_student:
                    resume_by_student[rol] = personal[:]
                resume_by_student[rol].append(sa.qualification)

                # add test specifics to the test worksheet.
                test_ws.append(personal + _questions_row(sa, version))

    for resume in resume_by_student.values():
        resume_ws.append(resume)

    return save_virtual_workbook(wb)

from tests.models import TextQuestion, NumericalQuestion, ChoiceQuestion
from tests.models import StudentsAnswers, TextAnswer, NumericalAnswer, ChoiceAnswer, Alternative
import random

from django.shortcuts import get_object_or_404


def assign_version(test):
    # Randomly assign a version
    versions = test.version_set.all()
    index = random.randint(0, len(versions) - 1)

    return versions[index]


def create_empty_answers(question, student):
    try:
        text_answer = TextAnswer(student=student, question=question.textquestion)
        text_answer.save()
    except TextQuestion.DoesNotExist:
        pass

    try:
        numerical_answer = NumericalAnswer(student=student, question=question.numericalquestion)
        numerical_answer.save()
    except NumericalQuestion.DoesNotExist:
        pass

    try:
        choice_answer = ChoiceAnswer(student=student, question=question.choicequestion)
        choice_answer.save()
    except ChoiceQuestion.DoesNotExist:
        pass


def update_answer(pk, student, _answer, version, sv_pk):
    if pk in ['version', 'csrfmiddlewaretoken']:
        return

    # Text question
    studentanswer = get_object_or_404(StudentsAnswers, pk=sv_pk)
    try:
        answer = TextAnswer.objects.get(pk=pk, student=student)
        answer.text = _answer
        answer.save()
    except:
        pass

    # Choice question
    try:
        answer = ChoiceAnswer.objects.get(pk=pk, student=student)
        answer.alternative = Alternative.objects.get(pk=_answer)

        # Auto-correction
        # TODO: Add condition -> If studentanswer.version.test.auto_correction
        correct_alternative = answer.question.choicequestion.alternative_set.filter(correct=True).first()
        grade = studentanswer.qualification
        if answer.alternative.pk == correct_alternative.pk:
            answer.correct = True
            studentanswer.qualification =  (0 if grade is None else grade) + answer.question.score
            studentanswer.save()
        else:
            answer.correct = False
        print(answer.question.score)

        answer.save()
    except:
        pass

    # Numerical question
    try:
        answer = NumericalAnswer.objects.get(pk=pk, student=student)
        answer.number = float(_answer)

        # Auto-correction
        # TODO: Add condition -> If studentanswer.version.test.auto_correction
        top_limit = answer.question.numericalquestion.top_limit
        bottom_limit = answer.question.numericalquestion.bottom_limit
        grade = studentanswer.qualification
        if answer.number >= bottom_limit and answer.number <= top_limit:
            answer.correct = True
            studentanswer.qualification = (0 if grade is None else grade) + answer.question.score
            studentanswer.save()
        else:
            answer.correct = False

        answer.save()
    except:
        pass


def update_document(version, student, file):
    try:
        extension = file._name.split(".")[-1]
        student_answer = StudentsAnswers.objects.get(student=student, version=version)
        student_answer.document.delete(False)
        student_answer.document.save("DocumentoEstudiante%s.%s" % (student_answer.pk, extension), file)
        student_answer.save()
    except:
        pass


def get_agenda(object):
    sv = get_object_or_404(StudentsAnswers, student=object.request.user, version__pk=object.kwargs['pk'])
    for agenda in sv.version.test.course.agenda_set.all():
        if object.request.user in agenda.inscriptions.all():
            return agenda
    return None


def is_active(user, test):
    for agendatest in test.agendatest_set.filter(active=True):
        if user in agendatest.agenda.inscriptions.all():
            return True
    return False

from tests.models import TextQuestion, NumericalQuestion, ChoiceQuestion
from tests.models import StudentsAnswers, TextAnswer, NumericalAnswer, ChoiceAnswer, Alternative
import random


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


def update_answer(pk, student, _answer, version):
    if pk in ['version', 'csrfmiddlewaretoken']:
        return

    try:
        answer = TextAnswer.objects.get(pk=pk, student=student)
        answer.text = _answer
        answer.save()
    except:
        pass

    try:
        answer = ChoiceAnswer.objects.get(pk=pk, student=student)
        answer.alternative = Alternative.objects.get(pk=_answer)
        answer.save()
    except:
        pass

    try:
        answer = NumericalAnswer.objects.get(pk=pk, student=student)
        answer.number = _answer
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

from copy import deepcopy
from .models import ChoiceQuestion, NumericalQuestion, TextQuestion


def duplicate_question(question, version):
    try:
        q = question.choicequestion
        new_question = ChoiceQuestion(version=version, text=q.text, score=q.score, html=q.html)
        new_question.save()
        print(question)
        for alt in question.choicequestion.alternative_set.all():
            new_alt = deepcopy(alt)
            new_alt.pk = None
            new_alt.question = new_question
            new_alt.save()
        return
    except Exception as a:
        print(a)

    try:
        q = question.numericalquestion
        new_question = NumericalQuestion(version=version, text=q.text,
                                         score=q.score, html=q.html,
                                         top_limit=q.top_limit, bottom_limit=q.bottom_limit)
        new_question.save()
        print(question)
        return
    except Exception as a:
        print(a)

    try:
        q = question.textquestion
        new_question = TextQuestion(version=version, text=q.text, score=q.score, html=q.html)
        new_question.save()
        print(question)
        return
    except Exception as a:
        print(a)

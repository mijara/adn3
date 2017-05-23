from pretests.models import Pretest
from classes.models import Session
from .tableform import TableForm


def session_pks(course):
    return [session.pk for session in course.session_set.all()]


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

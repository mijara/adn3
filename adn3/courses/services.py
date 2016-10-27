from pretests.models import Pretest
from tableform import TableForm


def save_grades(post_data):
    pretests_table = TableForm('pretest')
    pretests_table.add_field('percentage', 0)
    pretests_table.add_field('show_grade', False, transform={'on': True})
    pretests_table.process_and_save(Pretest, post_data)

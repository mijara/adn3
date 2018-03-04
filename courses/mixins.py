from django.contrib.auth.mixins import UserPassesTestMixin

from adn3.services import is_coordinator, is_teacher_of, is_superteacher_of


class IsTeacherOfCourseMixin(UserPassesTestMixin):
    def test_func(self):
        return is_coordinator(self.request.user) or \
               is_teacher_of(self.request.user, self.get_course()) or \
               is_superteacher_of(self.request.user, self.get_course())

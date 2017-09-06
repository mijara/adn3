from django import template
from django.template import Node

register = template.Library()


class CalendarNode(Node):
    def render(self, context):
        days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        blocks = ['1 - 2', '3 - 4', '5 - 6', '7 - 8', '9 - 10', '11 - 12']

        html = '<table class="table">\n'
        html += '<thead>\n'
        html += '<tr class="table-heading">\n'
        html += '<th width="15%">Bloque</th>\n'

        for day in days:
            html += '<th width="17%" class="text-center">{}</th>'.format(day)

        html += '</tr>'
        html += '</thead>'
        html += '<tbody>'

        for b, block in enumerate(blocks):
            html += '<tr>'
            html += '<td>{block}</td>'.format(block=block)

            for d, day in enumerate(days):
                html += '<td><div class="calendar-item">' \
                        '<input type="hidden" name="block" value="{d}-{b}">' \
                        '{day}<br>' \
                        '<div>{block}</div></div></td>'.format(day=day, block=block, d=d, b=b)

        html += '</tbody>'
        html += '</table>'

        return html


class ScheduleNode(Node):
    def render(self, context):
        course = context['view'].get_course()
        software = context['software']

        days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        blocks = ['1 - 2', '3 - 4', '5 - 6', '7 - 8', '9 - 10', '11 - 12']

        html = '<table class="table">\n'
        html += '<thead>\n'
        html += '<tr class="table-heading">\n'
        html += '<th width="15%">Bloque</th>\n'

        for day in days:
            html += '<th width="17%" class="text-center">{}</th>'.format(day)

        html += '</tr>'
        html += '</thead>'
        html += '<tbody>'

        for b, block in enumerate(blocks):
            html += '<tr>'
            html += '<td>{block}</td>'.format(block=block)

            for d, day in enumerate(days):
                flyins = course.flyin_set.filter(software=software, first_preference='%d-%d' % (d, b)).count()

                cls = ''
                if 10 > flyins > 0:
                    cls = 'label-simple'
                elif 10 <= flyins < 20:
                    cls = 'label-warning'
                elif flyins >= 20:
                    cls = 'label-danger'

                html += '<td class="text-center %s"><strong>%s</strong></td>' % (cls, flyins)

        html += '</tbody>'
        html += '</table>'

        return html


@register.tag
def generate_calendar(value, arg):
    return CalendarNode()


@register.tag
def generate_calendar_p1(value, arg):
    return ScheduleNode()

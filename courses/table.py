class Table:
    def __init__(self):
        self.columns = []
        self.rows = {}

    def set(self, *, row, column, value):
        if row not in self.rows:
            self.rows[row] = {}
        _row = self.rows[row]
        _row[column] = value if value is not None else 0

        if column not in self.columns:
            self.columns.append(column)

    def as_html(self):
        html = '<table border="1" cellpadding="3">'

        html += '<tr>'
        html += f'<td>ID</td>'
        for column in self.columns:
            html += f'<td>{column}</td>'
        html += '</tr>'

        for _id, row in self.rows.items():
            html_row = list(self.columns)

            html += '<tr>'
            html += f'<td>{_id}</td>'

            for col, val in row.items():
                print(html_row)
                html_row[html_row.index(col)] = f'<td>{val}</td>'

            html += ''.join(html_row)
            html += '</tr>'
        html += '</table>'

        return html

    def as_excel(self, worksheet):
        worksheet.append(['ID'] + self.columns)

        for _id, row in self.rows.items():
            html_row = list(self.columns)

            for col, val in row.items():
                html_row[html_row.index(col)] = val

            worksheet.append([_id] + html_row)

    def fill_columns(self, columns):
        for col in columns:
            if col not in self.columns:
                self.columns.append(col)

    def fill_blanks(self):
        for row in self.rows.values():
            for column in self.columns:
                if column not in row:
                    row[column] = 0

    def add_row(self, _row):
        self.rows[_row] = {}

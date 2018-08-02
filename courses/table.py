class Table:
    def __init__(self):
        self.columns = []
        self.rows = {}

    def set(self, *, row, column, value):
        if row not in self.rows:
            self.rows[row] = {}
        _row = self.rows[row]
        _row[column] = value

        if column not in self.columns:
            self.columns.append(column)

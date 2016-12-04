var Table = (function ($) {
    var DAYS = 5,
        BLOCKS = 7;

    var self = {};

    self.init = function (mountPoint, data) {
        self.mountPoint = mountPoint;
        self.data = data;
    };

    self.mount = function() {
        makeBlocks();

        var thead = makeHead();
        var tbody = makeBody();

        var table = $('<table class="table table-bordered">').append(thead).append(tbody);
        self.mountPoint.append(table);
    };

    function makeBlocks() {
        // ordered as self.elements[DAY][BLOCK]
        self.elements = [];

        for (var day = 0; day < DAYS; day++) {
            var column = [];

            for (var block = 0; block < BLOCKS; block++) {
                column.push($('<td>'));
            }

            self.elements.push(column);
        }
    }

    function makeHead() {
        var row = $('<tr class="table-heading">');

        row.append('<th>Bloque</th>');
        row.append('<th>Lunes</th>');
        row.append('<th>Martes</th>');
        row.append('<th>Miércoles</th>');
        row.append('<th>Jueves</th>');
        row.append('<th>Viernes</th>');

        return $('<thead>').append(row);
    }

    function makeBody() {
        var body = $('<tbody>');

        for (var block = 0; block < BLOCKS; block++) {
            var row = $('<tr>').append('<th>' + (block * 2 + 1) + ' - ' + (block + 1) * 2 + '</th>');

            for (var day = 0; day < DAYS; day++) {
                row.append(self.elements[day][block]);
            }

            body.append(row);
        }

        return body;
    }

    return self;
})(jQuery);

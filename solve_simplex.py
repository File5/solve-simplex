class AsciiTable:

    def __init__(self, data=[], header=True, separateLines=False):
        self.data = []
        self.colomnWidth = []

        for row in data:
            newRow = []
            
            for i, item in enumerate(row):
                value = str(item)
                newRow.append(value)

                if i < len(self.colomnWidth):
                    self.colomnWidth[i] = max(len(value), self.colomnWidth[i])
                else:
                    self.colomnWidth.append(len(value))

            self.data.append(newRow)

        self.charMap = {
            'top' : '-',
            'left' : '|',
            'corner' : '+'
        }
        self.padding = 1

        self.header = header
        self.separateLines = separateLines

    def __str__(self):

        chars = self.charMap

        def _getHorizontalLine():
            result = chars['corner']

            for width in self.colomnWidth:
                result += chars['top'] * (width + 2 * self.padding) + chars['corner']

            return result

        def _getRowWithData(data):
            result = chars['left']

            for i in range(len(self.colomnWidth)):
                width = self.colomnWidth[i] + self.padding
                formatStr = '{:>' + str(width) + '}' + (' ' * self.padding)

                if i < len(data):
                    result += formatStr.format(data[i])
                else:
                    result += formatStr.format('')

                result += chars['left']

            return result

        output = _getHorizontalLine() + '\n'

        lastI = len(self.data) - 1
        for i, row in enumerate(self.data):
            output += _getRowWithData(row) + '\n'

            if (i == 0 and self.header) or (self.separateLines) or (i == lastI):
                output += _getHorizontalLine() + '\n'

        return output


class SimplexTable(AsciiTable):

    def __init__(self, basisVars, allVars, data):
        self.basis = basisVars
        self.vars = allVars

        BASIS_LABEL = 'Basis'
        VALUES_LABEL = 'Values'
        THETA = 'THETA' # 'θ'
        FUNCTION = 'f(x)'

        colomns = self.vars

        header = [BASIS_LABEL, VALUES_LABEL, *colomns, THETA]

        rows = []
        for i, b in enumerate(self.basis):
            rows.append([b] + data[i])
        rows.append([FUNCTION] + data[len(data) - 1])

        AsciiTable.__init__(self, [header, *rows], True, False)

# DEBUG
if __name__ == '__main__':
    data = [
        [ 95, 0, 6.5, 0, 1, -2.5,  1, 0],
        [ 10, 0,  -2, 1, 0,    1, -1, 0],
        [ 15, 1, 2.5, 0, 0, -0.5,  1, 0],
        [180, 0,   2, 0, 0,    2,  2, 0],
    ]
    table = SimplexTable(['x4','x3','x1'], ['x' + str(i) for i in range(1, 7)], data)
    print(table)

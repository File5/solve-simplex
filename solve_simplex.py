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


class SimplexSolution:

    def __init__(self, funcCoeff, conditions):
        self.funcVarsCount = len(funcCoeff)
        self.aVarsCount = len(conditions)
        allVarsCount = self.funcVarsCount + self.aVarsCount

        self.basis = ['x' + str(i) for i in range(self.funcVarsCount + 1, allVarsCount + 1)]
        self.allVars = ['x' + str(i) for i in range(1, allVarsCount + 1)]

        self.table = []

        for i in range(len(self.basis)):
            row = [conditions[i][-1]]
            row += conditions[i][:-1]

            t = [0] * len(self.basis)
            t[i] = 1

            row += t

            self.table.append(row)

        indexRow = [0]
        indexRow += list(map(lambda x : -x, funcCoeff))
        indexRow += [0] * len(self.basis)
        self.table.append(indexRow)

    def getSolutionVector(self):
        vector = []
        
        for var in self.allVars:
            if var in self.basis:
                i = self.basis.index(var)
                vector.append(self.table[i][0])
            else:
                vector.append(0)

        return vector

    def getFuncValue(self):
        return self.table[-1][0]
                

# DEBUG
if __name__ == '__main__':
    data = [
        [18,  1,  3, 1, 0, 0, 0,     6],
        [16,  2,  1, 0, 1, 0, 0,    16],
        [ 5,  0,  1, 0, 0, 1, 0,     5],
        [ 7,  1,  0, 0, 0, 0, 1, 'INF'],
        [ 0, -2, -3, 0, 0, 0, 0       ],
    ]
    table = SimplexTable(['x3', 'x4', 'x5', 'x6'], ['x' + str(i) for i in range(1, 7)], data)
    print(table)
    funcCoeff = [2, 3]
    conditions = [
        [1, 3, 18],
        [2, 1, 16],
        [0, 1, 5],
        [1, 0, 7]
    ]
    solution = SimplexSolution(funcCoeff, conditions)
    solutionTable = SimplexTable(solution.basis, solution.allVars, solution.table)
    print(solutionTable)
    print(solution.getSolutionVector())
    print(solution.getFuncValue())

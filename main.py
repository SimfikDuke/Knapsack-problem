class MaxBackpack(object):
    def __init__(self, file):
        f = open(file, "r+")
        self.a = list(map(int, f.readline().split()))
        self.w = list(map(int, f.readline().split()))
        self.R = int(f.readline())
        f.close()
        self.sort_args()

    @staticmethod
    def gamma(a, w, R, x=[]):
        out_sum = 0
        out_weight = 0
        for i in range(len(x)):
            out_sum += a[i] * x[i]
            out_weight += w[i] * x[i]
        for i in range(len(x), len(a)):
            if w[i] <= R - out_weight:
                out_weight += w[i]
                out_sum += a[i]
            elif R > out_weight:
                out_sum += a[i] * (R - out_weight) / w[i]
                out_weight += (R - out_weight) / w[i]
        if out_weight > R:
            from math import inf
            out_sum = - inf
        return out_sum

    def sort_args(self):
        for i in range(len(self.a)):
            for j in range(i + 1, len(self.a)):
                if self.a[i] / self.w[i] < self.a[j] / self.w[j]:
                    self.a[i], self.w[i], self.a[j], self.w[j] = self.a[j], self.w[j], self.a[i], self.w[i]

    @staticmethod
    def max_backpack(a, w, R, x=[]):
        if len(a) == len(x):
            return x

        x1 = [i for i in x]
        x2 = [i for i in x]
        x1.append(0)
        x2.append(1)
        gamma_x1 = MaxBackpack.gamma(a, w, R, x1)
        gamma_x2 = MaxBackpack.gamma(a, w, R, x2)

        if gamma_x1 > gamma_x2:
            record_x1 = MaxBackpack.max_backpack(a, w, R, x1)
            if MaxBackpack.gamma(a, w, R, record_x1) < gamma_x2:
                record_x2 = MaxBackpack.max_backpack(a, w, R, x2)
                if MaxBackpack.gamma(a, w, R, record_x2) > MaxBackpack.gamma(a, w, R, record_x1):
                    record = record_x2
                else:
                    record = record_x1
            else:
                record = record_x1
        elif gamma_x1 < gamma_x2:
            record_x2 = MaxBackpack.max_backpack(a, w, R, x2)
            if MaxBackpack.gamma(a, w, R, record_x2) < gamma_x1:
                record_x1 = MaxBackpack.max_backpack(a, w, R, x1)
                if MaxBackpack.gamma(a, w, R, record_x1) > MaxBackpack.gamma(a, w, R, record_x2):
                    record = record_x1
                else:
                    record = record_x2
            else:
                record = record_x2
        else:
            record_x1 = MaxBackpack.max_backpack(a, w, R, x1)
            record_x2 = MaxBackpack.max_backpack(a, w, R, x2)
            if MaxBackpack.gamma(a, w, R, record_x1) < MaxBackpack.gamma(a, w, R, record_x2):
                record = record_x2
            else:
                record = record_x1
        return record

    def task(self):
        out_str = "Входные данные: \n"
        out_str += " ( max("
        for i in range(len(self.a)):
            out_str += str(self.a[i]) + "x" + str(i + 1)
            if i < len(self.a) - 1:
                out_str += " + "
        out_str += ");\n"
        out_str += "<  "
        for i in range(len(self.w)):
            out_str += str(self.w[i]) + "x" + str(i + 1)
            if i < len(self.w) - 1:
                out_str += " + "
        out_str += " <= " + str(self.R) + ";\n"
        out_str += " ( X1...X" + str(len(self.a)) + " из {0,1}.\n"
        result = MaxBackpack.max_backpack(self.a, self.w, self.R)
        max_cost = MaxBackpack.gamma(self.a, self.w, self.R, result)
        result_string = " ".join(map(str, result))
        out_str += "\nОтвет: x* = (" + result_string + ")\n"
        out_str += "Максимальная стоимость рюкзака:" + str(max_cost)
        return out_str

    def __str__(self):
        return self.task()

    def write_to_file(self, file="output.txt"):
        f = open(file, "w+")
        f.write(str(self))
        f.close()


t = MaxBackpack("input.txt")
t.write_to_file()
print(t)
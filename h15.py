class Duo:
    def __init__(self, first, second):
        """Создание пары значений"""
        self.first = first
        self.second = second

    def show(self):
        """Отобразить значения"""
        print("-> Значения:")
        print(f"Первое: {self.first}\nВторое: {self.second}")

    def modify(self, a, b):
        """Изменить оба значения"""
        self.first = a
        self.second = b
        print(f"Значения обновлены на: ({self.first}, {self.second})")

    def total(self):
        """Вернуть сумму"""
        return self.first + self.second

    def larger(self):
        """Вернуть большее из двух"""
        return self.first if self.first > self.second else self.second


class BoundedCounter:
    def __init__(self, lower=0, upper=10, current=None):
        """Инициализация ограниченного счётчика"""
        self.lower = lower
        self.upper = upper
        self.current = current if current is not None else lower

    def up(self):
        if self.current < self.upper:
            self.current += 1
            print(f"[+] Увеличено: {self.current}")
        else:
            print("[!] Достигнут предел сверху")

    def down(self):
        if self.current > self.lower:
            self.current -= 1
            print(f"[-] Уменьшено: {self.current}")
        else:
            print("[!] Достигнут предел снизу")

    def status(self):
        """Показать текущее значение"""
        return f"Текущее значение: {self.current}"


class Poly:
    def __init__(self, coeffs):
        """Создание многочлена по списку коэффициентов"""
        self.coeffs = coeffs

    def at(self, val):
        """Подставить значение в многочлен"""
        return sum(c * (val ** i) for i, c in enumerate(self.coeffs))

    def __str__(self):
        terms = []
        for idx, coef in enumerate(self.coeffs):
            if coef == 0:
                continue
            if idx == 0:
                terms.append(f"{coef}")
            elif idx == 1:
                terms.append(f"{coef}x")
            else:
                terms.append(f"{coef}x^{idx}")
        return " + ".join(terms) if terms else "0"

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        result = [0] * max_len
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result[i] = a + b
        return Poly(result)

    def __sub__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        result = [0] * max_len
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result[i] = a - b
        return Poly(result)

    def __mul__(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]
        return Poly(result)


# --- Демонстрация работы ---
if __name__ == "__main__":
    print("== ПАРА ЗНАЧЕНИЙ ==")
    pair = Duo(7, 13)
    pair.show()
    print(f"Сумма: {pair.total()}")
    print(f"Максимум: {pair.larger()}")
    pair.modify(42, 5)
    pair.show()
    print()

    print("== СЧЁТЧИК ==")
    meter = BoundedCounter(1, 3, 2)
    print(meter.status())
    meter.up()
    meter.up()
    meter.down()
    meter.down()
    meter.down()
    print()

    print("== МНОГОЧЛЕНЫ ==")
    A = Poly([3, 1, 2])    # 3 + x + 2x^2
    B = Poly([1, 0, 4])    # 1 + 0x + 4x^2

    print("A(x):", A)
    print("B(x):", B)
    print("A + B =", A + B)
    print("A - B =", A - B)
    print("A * B =", A * B)
    x_val = 3
    print(f"A({x_val}) = {A.at(x_val)}")
    print(f"B({x_val}) = {B.at(x_val)}")

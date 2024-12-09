class Pyramid:
    def __init__(self, base_area: float, height: float):
        self.base_area = base_area #площадь
        self.height = height #высота

    @staticmethod
    def about():
        return "Команда из 3 разработчиков: реализуем программу для расчета объема правильной пирамиды."

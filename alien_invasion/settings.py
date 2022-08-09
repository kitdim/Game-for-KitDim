class Settings():
    """Класс для хранения настроек"""

    def __init__(self):
        """Инициализация настроек игры"""
        # Параметры игры
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed = 1.5

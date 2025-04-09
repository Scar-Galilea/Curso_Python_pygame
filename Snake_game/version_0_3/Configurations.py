class Configurations:
    """
    Clase que contiene todas las configuraciónes del juego.
    """
    #Configuraciones de pantalla
    _screen_size = (1288, 720)  # Resolución de la pantalla (ancho,alto).
    _game_title = "Snake game en pygame"
    _background = (204, 169, 221)  # Fondo de la pantalla en formato RGB.

    @classmethod
    def get_creen_size(cls) -> tuple[int,int]:
        """
        Getter para screen_size
        """
        return cls._screen_size
    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title
        """
        return cls._game_title
    @classmethod
    def get_background(cls) -> tuple[int,int,int]:
        """
        Getter para _background
        """
        return cls._background
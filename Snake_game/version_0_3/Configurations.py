class Configurations:
    """
    Clase que contiene todas las configuraciónes del juego.
    """
    #Configuraciones de pantalla
    _screen_size = (1288, 720)  # Resolución de la pantalla (ancho,alto).
    _game_title = "Snake game en pygame"
    _background = (204, 169, 221)  # Fondo de la pantalla en formato RGB.

    #Configuraciones de la serpiente.
    _snake_block_size = 40
    _snake_head_color = (255, 255, 255)
    _snake_body_color = (0,255,0)

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

    @classmethod
    def snake_block_size(cls) -> int:
        """
        Getter para _snake_block_size
        """
        return cls._snake_block_size

    @classmethod
    def snake_head_color(cls) -> tuple[int,int,int]:
        """
        Getter para _snake_head_color
        """
        return cls._snake_head_color

    @classmethod
    def snake_body_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_body_color
        """
        return cls._snake_body_color
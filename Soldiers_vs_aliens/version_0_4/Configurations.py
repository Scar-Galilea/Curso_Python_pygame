class Configurations:
    """
    Clase que contiene todas las configuraciónes del juego.
    """
    #Configuraciones de pantalla
    _snake_block_size = 200
    _screen_size = (1288, 720)  # Resolución de la pantalla (ancho,alto).
    _game_title = "Soldiers vs aliens"

    _background_image_path = "../Media/background_image.jpg"
    _fps = 8  # fps del juego.

    _soldiers_image_path = "../Media/soldiers.png"

    _soldier_speed = 12.5

    @classmethod
    def get_screen_size(cls) -> tuple[int,int]:
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
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_snake_block_size(cls) -> int:
        """
        Getter para _background_image_path.
        """
        return cls._snake_block_size

    @classmethod
    def get_soldiers_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._soldiers_image_path

    @classmethod
    def  get_soldier_speed(cls) -> float:
        """
        Getter para _background_image_path.
        """
        return cls._soldier_speed
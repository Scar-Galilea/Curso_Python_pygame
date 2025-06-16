class Configurations:
    """
    Clase que contiene todas las configuraciónes del juego.
    """
    #Configuraciones de pantalla
    _snake_block_size = 200
    _screen_size = (1288, 720)  # Resolución de la pantalla (ancho,alto).
    _game_title = "Soldiers vs aliens"

    _background_image_path = "../Media/background_image.jpg"
    _fps = 15  # fps del juego.

    _soldiers_image_path = "../Media/soldiers.png"

    _frames_per_row = 4  # Número de frames que contiene cada fila de la hoja de frames.
    _soldier_frame_delay = 300  # Tiempo de cada frame del personaje (en ms).
    _soldier_speed = 12.5  # Velocidad (en píxeles) del personaje

    _soldier_sheet_path = "../Media/soldier-idle_shooting_sheet.png"
    _shop_sheet_path = "../Media/shot-sheet.png"

    _soldier_size = (142, 76)

    _shop_size = (32, 32)

    _frames_shop_row = 4

    _num_recortes = 2

    _soldier_frames_per_row = 4  # Número de frames que contiene cada fila de la hoja de frames.

    _soldier_frames_per_column = 2

    _soldier_shooting_frame_delay = 34

    # Aliens
    _aliens_sheet_path = ["../Media/alien1-Sheet.png",
                          "../Media/alien2-Sheet.png",
                          "../Media/alien3-Sheet.png",
                          "../Media/alien4-Sheet.png",
                          "../Media/alien5-Sheet.png"
                          ]

    _aliens_size = (90, 76)

    _speed_aliens_x = 10
    _speed_aliens_y = 10

    @classmethod
    def get_soldier_shooting_frame_delay(cls) -> int:
        """
        Getter para _soldier_shooting_frame_delay.
        """
        return cls._soldier_shooting_frame_delay

    @classmethod
    def get_soldier_frames_per_column(cls) -> int:
        """
        Getter para _soldier_frames_per_column.
        """
        return cls._soldier_frames_per_column

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
    def get_soldiers_image_path(cls) ->  str:
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

    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    @classmethod
    def get_speed_aliens_x(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._speed_aliens_x

    @classmethod
    def get_speed_aliens_y(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._speed_aliens_y

    @classmethod
    def get_frames_shot_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_shop_row


    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_soldier_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._soldier_size

    @classmethod
    def get_aliens_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._aliens_size

    @classmethod
    def get_shop_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._shop_sheet_path

    @classmethod
    def get_shop_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._shop_size

    @classmethod
    def get_num_recortes(cls) -> int:
        """
        Getter para _soldier_size.
        """
        return cls._num_recortes

    @classmethod
    def get_soldier_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._soldier_frames_per_row

    @classmethod
    def get_aliens_sheet_path(cls) -> list[str]:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._aliens_sheet_path


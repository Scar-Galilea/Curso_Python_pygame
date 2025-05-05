class Configurations:
    """
    Clase que contine todas las configuraciones del juego
    """
    #Configuraciones de la pantala
    _screen_size = (1280, 720)
    _game_title = "Snake game en pygame"
    #_background = (224, 176, 255)
    _fps = 8 #fps del juego
    _game_over_screen_time = 4

    #Configuraciones de la serpiente
    _snake_block_size = 45 #Tamaño del bloque de la serpiente
    _snake_head_color = (157, 0, 255)
    _snake_body_color = (76, 40, 130)


    #Configuraciones de la manzana
    _apple_size = _snake_block_size

    _apple_color = (255, 0, 0)

    _background_image_path = "../media/background_image.jpg"

    _body_images_path = ["../media/body1.png",
                        "../media/body2.png",
                        "../media/body3.png"]

    _image_apple_path = ["../media/apple1.png",
                        "../media/apple2.png",
                        "../media/apple3.png",
                        "../media/apple4.png"]

    _background_image_head = [    "../media/head1.png",
                            "../media/head2.png",
                            "../media/head3.png",
                            "../media/head4.png",
                            "../media/head5.png",
                            "../media/head6.png",
                            "../media/head7.png",
                            "../media/head8.png"]



    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para get_game_title
        """
        return cls._game_title
    """
    
    def get_background(cls) -> tuple[int,int, int]:
        return cls._background
    """
    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps
    @classmethod
    def get_snake_block_size(cls) -> int:
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        return cls._snake_body_color

    # Manzana:
    @classmethod
    def get_apple_size(cls) -> int:
        """
        Getter para _apple_size
        """
        return cls._apple_size

    @classmethod
    def get_apple_color(cls) -> tuple[int, int, int]:
        """
        Getter para _apple_color
        """
        return cls._apple_color

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _apple_color
        """
        return cls._game_over_screen_time

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _apple_color
        """
        return cls._background_image_path

    @classmethod
    def get_image_apple_path(cls) -> list[str]:
        """
        Getter para _apple_color
        """
        return cls._image_apple_path

    @classmethod
    def get_background_image_head(cls) -> list[str]:
        """
        Getter para _background_image_head
        """
        return cls._background_image_head

    @classmethod
    def get_body_images_path(cls) -> list[str]:
        """
        Getter para _background_image_body1
        """
        return cls._body_images_path




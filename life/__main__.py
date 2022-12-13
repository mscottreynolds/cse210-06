import constants

from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService


def main():   
    """ Main entry point. Create keyboard and video services. Start game director."""
    # Services
    keyboard_service = KeyboardService()
    video_service = VideoService()
    
    director = Director(keyboard_service, video_service)
    director.start_game()


if __name__ == "__main__":
    main()
    
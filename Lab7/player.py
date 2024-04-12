import pygame
import os

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")

pygame.mixer.init()

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    stop_music()
    global current_index
    current_index = (current_index + 1) % len(playlist)
    play_music(playlist[current_index])

def previous_song():
    stop_music()
    global current_index
    current_index = (current_index - 1) % len(playlist)
    play_music(playlist[current_index])

def load_music_files(directory):
    music_files = []
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            music_files.append(os.path.join(directory, file))
    return music_files

running = True
current_index = 0
playlist = []

music_directory = "player"
playlist = load_music_files(music_directory)

if not playlist:
    print("No music files found in the specified directory.")
    running = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Стоп/Играть
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(playlist[current_index])
            elif event.key == pygame.K_RIGHT:  #След
                next_song()
            elif event.key == pygame.K_LEFT:  # Прошл
                previous_song()

    pygame.display.flip()

pygame.quit()

from pygame import mixer
import pygame
import json

class Sound:
    def __init__(self):
        mixer.init()
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.allowSFX = True

        self.sfx = {
            'soundtrack': mixer.Sound('data/sounds/main_theme.ogg'),
            'coin': mixer.Sound('data/sounds/coin.ogg'),
            'bump': mixer.Sound('data/sounds/bump.ogg'),
            'stomp': mixer.Sound('data/sounds/stomp.ogg'),
            'jump': mixer.Sound('data/sounds/small_jump.ogg'),
            'death': mixer.Sound('data/sounds/death.wav'),
            'kick': mixer.Sound('data/sounds/kick.ogg'),
            'brick_bump': mixer.Sound('data/sounds/brick-bump.ogg'),
            'powerup': mixer.Sound('data/sounds/powerup.ogg'),
            'powerup_appear': mixer.Sound('data/sounds/powerup_appears.ogg'),
            'pipe': mixer.Sound('data/sounds/pipe.ogg')
        }

        self.sfx['soundtrack'].set_volume(0.2)
        self.sfx['coin'].set_volume(0.8)
        self.sfx['bump'].set_volume(0.4)
        self.sfx['stomp'].set_volume(0.4)
        self.sfx['jump'].set_volume(0.7)
        self.sfx['death'].set_volume(0.8)
        self.sfx['kick'].set_volume(0.8)
        self.sfx['brick_bump'].set_volume(0.7)
        self.sfx['powerup'].set_volume(0.8)
        self.sfx['powerup_appear'].set_volume(0.8)
        self.sfx['pipe'].set_volume(0.3)

    def play_sfx(self, sfx_name):
        if self.allowSFX and sfx_name in self.sfx:
            self.sfx_channel.play(self.sfx[sfx_name])

    def play_music(self, music_name):
        if music_name in self.sfx:
            self.music_channel.play(self.sfx[music_name], loops=-1)  # Loop indefinitely

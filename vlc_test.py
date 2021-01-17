import vlc
print(vlc)
def testVlc():
    instance = vlc.Instance('--aout=alsa')
    p = instance.media_player_new()
    m = instance.media_new('harvard.wav')
    p.set_media(m)
    p.play()

if __name__ == '__main__':
    testVlc()

class song :
    def __init__ (self , lyrics ):
        self.lyrics = lyrics
    def sing_me_a_song(self) :
        for lyrics in self.lyrics :
            print(lyrics)
stairway= song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import youtube_dl
from youtube_dl import YoutubeDL
class music(Cog_Extension):
    def __init__(self, bot):
#all the music related stuff
        self.is_playing = False

# 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""
        #self.music_list = []
     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            #try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
              
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            print(self.music_queue)
            #remove the first element as you are currently playing it
            #self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(executable="./ff/bin/ffmpeg.exe", source = m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
            #self.vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\edward\\Desktop\\r\\bin\\ffmpeg.exe", source = m_url, **self.FFMPEG_OPTIONS))
        else:
            self.is_playing = False

    @commands.command(pass_context=True, help="Plays a selected song from youtube",aliases=['play'])
    async def p(self, ctx, *args):
        #print(args)
        
        try:
            voice_channel = ctx.author.voice.channel
        except:
            voice_channel = None

        if voice_channel is None:

            #you need to be connected so that the bot knows where to go
            await ctx.send("Connect to a voice channel!")
        else:
            query = " ".join(args)
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
            else:
                await ctx.send("Song added to the queue")
                await message.add_reaction('⏮')
                await message.add_reaction('◀')
                await message.add_reaction('▶')
                await message.add_reaction('⏭')
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()
    #commands.command(name="p", pass_context=True)(play.callback)

    @commands.command(name="queue", help="Displays the current songs in queue")
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue")

    @commands.command(name="skip", help="Skips the current song being played")
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music()
            
    @commands.command(name="disconnect", help="Disconnecting bot from VC")
    async def dc(self, ctx):
        await self.vc.disconnect()
    @commands.command(pass_context=True)
    async def join(self, ctx):
        vc = ctx.voice_client
        if ctx.author.voice is None:
            await ctx.send("叫尛")
        voice_channel = ctx.author.voice.channel
        if vc is None:
            await voice_channel.connect()
        else:
            await vc.move_to(voice_channel)


def setup(client):
    client.add_cog(music(client))
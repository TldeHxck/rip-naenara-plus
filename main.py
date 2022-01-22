import discum
import re
bot = discum.Client(token=env[0])

atn_sv_hooks = env[1]
mh_sv_hooks = env[2]
mh_rq_hooks = env[3]

serverlist_channels = [env[8], # 
                       env[9]] # 
                       
@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        guildID = m['guild_id'] if 'guild_id' in m else None #because DMs are technically channels too
        channelID = m['channel_id']
        username = m['author']['username']
        discriminator = m['author']['discriminator']
        content = m['content']

        if int(channelID) in serverlist_channels:
            ip = parsing(content)

            print(ip)

bot.gateway.run(auto_reconnect=True)

import discord
import cv2
import numpy as np
import  request

bot=discord.Client(intents=discord.Intent.all())

@bot.event
async def on_member_join(member):
    same_user = False
    user, guild = member, member.guild
    name,user_id,avatar_url = user.name, user.id, user.avatar.url
    name = discord.utils.get(guild.members, name=f"{name}")
    path = fr"C:\Users\waon-pc\Desktop\sibainu_discord\siba_bot\data\avatar_img{user_id}.png"
    
    if avatar_url != None:#デフォルトのアバターはパスする
        s=dl_file(url=avatar_url,dst_path=path)
        if s:
            l=list(csv_read())
            img_avatar_now = cv2.imread(path) 
            for i in range(len(l)):
                
                imgavatar_old = cv2.imread(fr"C:\Users\waon-pc\Desktop\sibainu_discord\siba_bot\data\avatar_img{l[i]}.png") 
                if np.array_equal(img_avatar_now, imgavatar_old):#アバターが一致する場合
                    
                    if int(l[i]) != int(user_id):#自分のアバターはパスする
                        print("おい、同じアバターだぞ")
                        await user.kick(reason="アバターが一致しているため")
                        channel = guild.get_channel(964656541166878720)
                        embed = discord.Embed(title="メンバーをキックしました。",description="アバターが一致している人がいました。") 
                        await channel.send(embed=embed)
                        same_user = True
                        break
                    else:
                        print("同じ人や")
                        same_user = True
                        break
                    
            if same_user is False:
                l.append(user_id)
                csv_write(data=l)
                print("一致してない")

bot.run()

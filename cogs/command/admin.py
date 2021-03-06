import discord
from core.cog_class import Cog_basic
from discord.ext import commands

class Admin(Cog_basic):

    @discord.slash_command(name="join", description="ONLY ADMIN:Let someone in.")
    async def join(self, ctx:discord.ApplicationContext, member:discord.Member):
        if ctx.author.guild_permissions.administrator is False:
            embed = discord.Embed(title="您無使用此指令的權限", colour=discord.Colour.red())
            await ctx.respond(embed=embed, ephemeral=True)
            return
        self.guild = self.bot.get_guild(self.config["HLCT_guild"])
        normal_role = self.guild.get_role(969962597061373994)
        border_channel = self.bot.get_channel(self.config["border_channel"])
        await member.add_roles(normal_role)
        embed=discord.Embed(title="成員加入", description=member.mention)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=member.name)
        await border_channel.send(embed=embed)
        await ctx.respond(f"{member.mention} 已成功加入", ephemeral=True)

    @discord.slash_command(name="status", description="ONLY ADMIN:bot status.")
    async def status(
        self,
        ctx:discord.ApplicationContext,
        status:discord.Option(description="bot status", choices=["online", "offline", "idle", "dnd", "invisible"])
        ):
        if ctx.author.guild_permissions.administrator is False:
            embed = discord.Embed(title="您無使用此指令的權限", colour=discord.Colour.red())
            await ctx.respond(embed=embed, ephemeral=True)
            return
        if status == "online":
            await self.bot.change_presence(status=discord.Status.online)
            await ctx.respond("Change success", ephemeral=True)
            return
        elif status == "offline":
            await self.bot.change_presence(status=discord.Status.offline)
            await ctx.respond("Change success", ephemeral=True)
            return
        elif status == "idle":
            await self.bot.change_presence(status=discord.Status.idle)
            await ctx.respond("Change success", ephemeral=True)
            return
        elif status == "dnd":
            await self.bot.change_presence(status=discord.Status.dnd)
            await ctx.respond("Change success", ephemeral=True)
            return
        elif status == "invisible":
            await self.bot.change_presence(status=discord.Status.invisible)
            await ctx.respond("Change success", ephemeral=True)
            return

        

def setup(bot: discord.Bot):
    bot.add_cog(Admin(bot))

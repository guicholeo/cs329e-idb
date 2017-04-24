from flask import Flask, request, render_template
from os import path
import requests
import threading

app = Flask(__name__)

StatusDict = {"actrollvision":'',"asmongold": '',"curse":'',"dontbesaad20": '',"esl_sc2":'',
              "expertzone":'',"foxrun402":'',"freakhopper":'',"frost":'',"goldglove":'' ,
              "imaqtpie": '',"itsthekellys":'' ,"jaysitty":'',"lobosjr":'' ,"lxthul": '', "mob5tertv": '',
              "nhfslickermo": '', "nick28t": '',"normaldifficulty": '',"phillyboy7897":'',
              "pokimane":'', "prettyboyfredo":'',"weiward":'',"wonderboyhalo": '', "zisteau": ''}
StatusColorDict = StatusDict.copy()


def StreamerStatus():
    for key in StatusDict:
        streams = requests.get('https://api.twitch.tv/kraken/streams/' + key + '?client_id=e6xu67x7c493rmp1osdcrnivd3j8g3')
        streams = streams.json()
        if (streams["stream"] == None):
            StatusDict[key]= "Offline"
            StatusColorDict[key] = '#e81212'#"#FF0000" 
        else:
            StatusDict[key]= "Online"
            StatusColorDict[key] ="#00d100"
    print("Update Complete!\n")

def CheckStatus():
	print("I am Updating Status.\n")
	StreamerStatus()
	threading.Timer(10.0,CheckStatus).start()
	
  
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
	return render_template('about.html')
   
@app.route('/streamers')
def streamers():
	#StreamerStatus()    
	#CheckStatus()
	return render_template('streamers.html', status = StatusDict, color = StatusColorDict)

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/genres')
def genres():
    return render_template('genres.html')

####-----STREAMERS-----####

@app.route('/streamer_actrollvision')
def streamer_actrollvision():
    return render_template('/streamers/streamer_actrollvision.html')

@app.route('/streamer_asmongold')
def streamer_asmongold():
    return render_template('/streamers/streamer_asmongold.html')

@app.route('/streamer_curse')
def streamer_curse():
    return render_template('/streamers/streamer_curse.html')

@app.route('/streamer_dontbesaad20')
def streamer_dontbesaad20():
    return render_template('/streamers/streamer_dontbesaad20.html')

@app.route('/streamer_esl_sc2')
def streamer_esl_sc2():
    return render_template('/streamers/streamer_esl_sc2.html')

@app.route('/streamer_expertzone')
def streamer_expertzone():
    return render_template('/streamers/streamer_expertzone_community.html')

@app.route('/streamer_foxrun402')
def streamer_foxrun402():
    return render_template('/streamers/streamer_foxrun402.html')

@app.route('/streamer_freakhopper')
def streamer_freakhopper():
    return render_template('/streamers/streamer_freakhopper.html')

@app.route('/streamer_frost')
def streamer_frost():
    return render_template('/streamers/streamer_frost_.html')

@app.route('/streamer_goldglove')
def streamer_goldglove():
    return render_template('/streamers/streamer_goldglove.html')

@app.route('/streamer_imaqtpie')
def streamer_imaqtpie():
    return render_template('/streamers/streamer_imaqtpie.html')

@app.route('/streamer_itsthekellys')
def streamer_itsthekellys():
    return render_template('/streamers/streamer_itsthekellys.html')

@app.route('/streamer_jaysitty')
def streamer_jaysitty():
    return render_template('/streamers/streamer_jaysitty.html')

@app.route('/streamer_lobosjr')
def streamer_lobosjr():
    return render_template('/streamers/streamer_lobosjr.html')

@app.route('/streamer_lxthul')
def streamer_lxthul():
    return render_template('/streamers/streamer_lxthul.html')

@app.route('/streamer_mob5stertv')
def streamer_mob5stertv():
    return render_template('/streamers/streamer_mob5stertv.html')

@app.route('/streamer_nhfslickermo')
def streamer_nhfslickermo():
    return render_template('/streamers/streamer_nhfslickermo.html')

@app.route('/streamer_nick28t')
def streamer_nick28t():
    return render_template('/streamers/streamer_nick28t.html')

@app.route('/streamer_NormalDifficulty')
def streamer_NormalDifficulty():
    return render_template('/streamers/streamer_NormalDifficulty.html')

@app.route('/streamer_phillyboy7897')
def streamer_phillyboy7897():
    return render_template('/streamers/streamer_phillyboy7897.html')

@app.route('/streamer_pokimane')
def streamer_pokimane():
    return render_template('/streamers/streamer_pokimane.html')

@app.route('/streamer_prettyboyfredo')
def streamer_prettyboyfredo():
    return render_template('/streamers/streamer_prettyboyfredo.html')

@app.route('/streamer_weiward')
def streamer_weiward():
    return render_template('/streamers/streamer_weiward.html')

@app.route('/streamer_wonderboyhalo')
def streamer_wonderboyhalo():
    return render_template('/streamers/streamer_wonderboyhalo.html')

@app.route('/streamer_zisteau')
def streamer_zisteau():
    return render_template('/streamers/streamer_zisteau.html')


####-----GAMES AND LIVESTREAMS FOR SAID GAMES-----####

@app.route('/civ6')
def civ6():
    return render_template('/games/civ6.html')

@app.route('/civ6_livestreams')
def civ6_livestreams():
    return render_template('/livestreams/civ6_livestreams.html')

@app.route('/darksouls')
def darksouls():
    return render_template('/games/darksouls3.html')

@app.route('/darksouls_livestreams')
def darksouls_livestreams():
    return render_template('/livestreams/darksouls_livestreams.html')

@app.route('/dayz')
def dayz():
    return render_template('/games/dayz.html')

@app.route('/dayz_livestreams')
def dayz_livestreams():
    return render_template('/livestreams/dayz_livestreams.html')

@app.route('/fallout4')
def fallout4():
    return render_template('/games/fallout4.html')

@app.route('/fallout4_livestreams')
def fallout4_livestreams():
    return render_template('/livestreams/fallout4_livestreams.html')

@app.route('/fifa17')
def fifa17():
    return render_template('/games/fifa17.html')

@app.route('/fifa17_livestreams')
def fifa17_livestreams():
    return render_template('/livestreams/fifa17_livestreams.html')

@app.route('/ffvii')
def ffvii():
    return render_template('/games/finalfantasy7.html')

@app.route('/FinalFantasy_livestreams')
def FinalFantasy_livestreams():
    return render_template('/livestreams/ffvii_livestreams.html')

@app.route('/forza')
def forza():
    return render_template('/games/forza.html')

@app.route('/forza_livestreams')
def forza_livestreams():
    return render_template('/livestreams/forza_livestreams.html')

@app.route('/h1z1')
def h1z1():
    return render_template('/games/h1z1.html')

@app.route('/h1z1_livestreams')
def h1z1_livestreams():
    return render_template('/livestreams/h1z1_livestreams.html')

@app.route('/halo5')
def halo5():
    return render_template('/games/halo5.html')

@app.route('/halo5_livestreams')
def halo5_livestreams():
    return render_template('/livestreams/halo5_livestreams.html')

@app.route('/halowars2')
def halowars2():
    return render_template('/games/halowars2.html')

@app.route('/halowars2_livestreams')
def halowars2_livestreams():
    return render_template('/livestreams/halowars2_livestreams.html')

@app.route('/lol')
def lol():
    return render_template('/games/lol.html')

@app.route('/lol_livestreams')
def lol_livestreams():
    return render_template('/livestreams/lol_livestreams.html')

@app.route('/minecraft')
def minecraft():
    return render_template('/games/minecraft.html')

@app.route('/minecraft_livestreams')
def minecraft_livestreams():
    return render_template('/livestreams/minecraft_livestreams.html')

@app.route('/mortal_kombat_x')
def mortal_kombat_x():
    return render_template('/games/mortal_kombat_x.html')

@app.route('/mortal_kombat_x_livestreams')
def mortal_kombat_x_livestreams():
    return render_template('/livestreams/mortal_kombat_x_livestreams.html')

@app.route('/nba2k17')
def nba2k17():
    return render_template('/games/nba2k17.html')

@app.route('/nba2k17_livestreams')
def nba2k17_livestreams():
    return render_template('/livestreams/nba2k17_livestreams.html')

@app.route('/nfs')
def nfs():
    return render_template('/games/nfs.html')

@app.route('/nfs_livestreams')
def nfs_livestreams():
    return render_template('/livestreams/nfs_livestreams.html')

@app.route('/nhl17')
def nhl17():
    return render_template('/games/nhl17.html')

@app.route('/nhl17_livestreams')
def nhl17_livestreams():
    return render_template('/livestreams/nhl17_livestreams.html')

@app.route('/overwatch')
def overwatch():
    return render_template('/games/overwatch.html')

@app.route('/overwatch_livestreams')
def overwatch_livestreams():
    return render_template('/livestreams/overwatch_livestreams.html')

@app.route('/projectcars')
def projectcars():
    return render_template('/games/projectcars.html')

@app.route('/projectcars_livestreams')
def projectcars_livestreams():
    return render_template('/livestreams/projectcars_livestreams.html')

@app.route('/rocketleague')
def rocketleague():
    return render_template('/games/rl.html')

@app.route('/rocketleague_livestreams')
def rocketleague_livestreams():
    return render_template('/livestreams/rl_livestreams.html')

@app.route('/rust')
def rust():
    return render_template('/games/rust.html')

@app.route('/rust_livestreams')
def rust_livestreams():
    return render_template('/livestreams/rust_livestreams.html')

@app.route('/starcraft')
def starcraft():
    return render_template('/games/starcraft.html')

@app.route('/starcraft_livestreams')
def starcraft_livestreams():
    return render_template('/livestreams/starcraft_livestreams.html')

@app.route('/streetfighterv')
def streetfighterv():
    return render_template('/games/streetfighterv.html')

@app.route('/streetfighterv_livestreams')
def streetfighterv_livestreams():
    return render_template('/livestreams/streetfighterv_livestreams.html')

@app.route('/titanfall2')
def titanfall2():
    return render_template('/games/titanfall2.html')

@app.route('/titanfall2_livestreams')
def titanfall2_livestreams():
    return render_template('/livestreams/titanfall2_livestreams.html')

@app.route('/ufc2')
def ufc2():
    return render_template('/games/ufc2.html')

@app.route('/ufc2_livestreams')
def ufc2_livestreams():
    return render_template('/livestreams/ufc2_livestreams.html')

@app.route('/witcher3')
def witcher3():
    return render_template('/games/witcher3.html')

@app.route('/witcher3_livestreams')
def witcher3_livestreams():
    return render_template('/livestreams/witcher3_livestreams.html')

@app.route('/WoW')
def WoW():
    return render_template('/games/wow.html')
    
@app.route('/wow_livestreams')
def wow_livestreams():
    return render_template('/livestreams/WoW_livestreams.html')

@app.route('/wwe2k17')
def wwe2k17():
    return render_template('/games/wwe17.html')

@app.route('/wwe2k17_livestreams')
def wwe2k17_livestreams():
    return render_template('/livestreams/wwe2k17_livestreams.html')




####-----GENRES-----####

@app.route('/fighting')
def fighting():
    return render_template('/genres/fighting.html')

@app.route('/racing')
def racing():
    return render_template('/genres/racing.html')

@app.route('/rpg')
def rpg():
    return render_template('/genres/rpg.html')

@app.route('/shooter')
def shooter():
    return render_template('/genres/shooter.html')

@app.route('/sports')
def sports():
    return render_template('/genres/sports.html')

@app.route('/strategy')
def strategy():
    return render_template('/genres/strategy.html')

@app.route('/survival')
def survival():
    return render_template('/genres/survival.html')



#  #template for the streamers for to just have one page generated
#  #to call this function use this {{ url_for('callStreamer' ,streamer="streamer name goes here")
# @app.route('/streamer/<string:streamer>')
# def callStreamer(streamer):
#     #generates the template with the python api stuff....
#     return render_template('streamerTemplate.html')
	   

if __name__ == "__main__":
    #StreamerStatus()
    CheckStatus()
    #app.run('162.243.121.191','80')
    app.run()    
    #change comment to run on chrome or local.

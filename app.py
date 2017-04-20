from flask import Flask, request, render_template
from os import path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')
   
@app.route('/streamers')
def streamers():
    return render_template('streamers.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/genres')
def genres():
    return render_template('genres.html')

####-----STREAMERS-----####

@app.route('/streamer_curse')
def streamer_curse():
    return render_template('/streamers/streamer_curse.html')

@app.route('/streamer_imaqtpie')
def streamer_imaqtpie():
    return render_template('/streamers/streamer_imaqtpie.html')

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

@app.route('/streamer_wonderboyhalo')
def streamer_wonderboyhalo():
    return render_template('/streamers/streamer_wonderboyhalo.html')

@app.route('/streamer_zisteau')
def streamer_zisteau():
    return render_template('/streamers/streamer_zisteau.html')

@app.route('/streamer_NormalDifficulty')
def streamer_NormalDifficulty():
    return render_template('/streamers/streamer_NormalDifficulty.html')

####-----GAMES AND LIVESTREAMS FOR SAID GAMES-----####


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

@app.route('/overwatch')
def overwatch():
    return render_template('/games/overwatch.html')

@app.route('/overwatch_livestreams')
def overwatch_livestreams():
    return render_template('/livestreams/overwatch_livestreams.html')

@app.route('/rust')
def rust():
    return render_template('/games/rust.html')

@app.route('/rust_livestreams')
def rust_livestreams():
    return render_template('/livestreams/rust_livestreams.html')

@app.route('/streetfighterv')
def streetfighterv():
    return render_template('/games/streetfighterv.html')

@app.route('/streetfighterv_livestreams')
def streetfighterv_livestreams():
    return render_template('/livestreams/streetfighterv_livestreams.html')

@app.route('/ufc2')
def ufc2():
    return render_template('/games/ufc2.html')

@app.route('/ufc2_livestreams')
def ufc2_livestreams():
    return render_template('/livestreams/ufc2_livestreams.html')
    
@app.route('/wwe17')
def wwe17():
    return render_template('/games/wwe17.html')

@app.route('/wwe17_livestreams')
def wwe17_livestreams():
    return render_template('/livestreams/wwe17_livestreams.html')



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
    #app.run('162.243.121.191','80')
    app.run()
    #change comment to run on chrome or local.

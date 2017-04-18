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

@app.route('/fallout4')
def fallout4():
    return render_template('/games/fallout4.html')

@app.route('/fifa17')
def fifa17():
    return render_template('/games/fifa17.html')

@app.route('/forza')
def forza():
    return render_template('/games/forza.html')

@app.route('/h1z1')
def h1z1():
    return render_template('/games/h1z1.html')

@app.route('/halo5')
def halo5():
    return render_template('/games/halo5.html')

@app.route('/halowars2')
def halowars2():
    return render_template('/games/halowars2.html')

@app.route('/lol')
def lol():
    return render_template('/games/lol.html')

@app.route('/minecraft')
def minecraft():
    return render_template('/games/minecraft.html')

@app.route('/mortal_kombat_x')
def mortal_kombat_x():
    return render_template('/games/mortal_kombat_x.html')

@app.route('/overwatch')
def overwatch():
    return render_template('/games/overwatch.html')

@app.route('/rust')
def rust():
    return render_template('/games/rust.html')

@app.route('/streetfighterv')
def streetfighterv():
    return render_template('/games/streetfighterv.html')

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

if __name__ == "__main__":
    #app.run('162.243.121.191','80')
    app.run()
    #change comment to run on chrome or local.

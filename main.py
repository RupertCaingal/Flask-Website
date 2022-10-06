from flask import Flask,render_template
import os

app = Flask(__name__)

imgfolder = os.path.join('static','img')
vidfolder = os.path.join('static','vid')

app.config['UP_FOLDER'] = imgfolder
app.config['UP1_FOLDER'] = vidfolder

@app.route("/")

def mainPage():


    img1 =  [os.path.join(app.config['UP_FOLDER'], 'denim.jpeg'),
             os.path.join(app.config['UP_FOLDER'], 'streetstyle.jpeg'),
             os.path.join(app.config['UP_FOLDER'], 'vintage.jpeg'),
             os.path.join(app.config['UP_FOLDER'], 'chickstyle.jpeg'),
             os.path.join(app.config['UP_FOLDER'], 'casual.jpeg')]


    return render_template('Mainpage-ootd.html', denim = img1[0], ss = img1[1], vintage = img1[2], cs = img1[3], casual = img1[4])




@app.route("/influencers/")
def infPage():
    return  render_template("infpage-ootd.html")

@app.route("/blog/")
def blogPage():
    return  render_template("blog-ootd.html")


if __name__ == '__main__':
    app.run()
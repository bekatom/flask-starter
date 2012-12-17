from flask import Blueprint, request, redirect, render_template, url_for,session, escape,jsonify
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from flaskstarter import  app




#### ERROR HANDLER #########
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/contact',methods=['POST','GET'])
@app.route('/contact')
def contact():
    if request.method =='POST':
        message = 'This is post message'
        return render_template('contact.html',message=message)
    else:
        return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')







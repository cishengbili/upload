#coding:utf-8

import datetime
import io

from flask import Blueprint, request, jsonify, render_template, Response

from wxapp.models import imgInfo
from wxapp import db

wxapp = Blueprint("wxapp", __name__)
wxapp_url_pattern = "/wxapp/%s/"

@wxapp.route(wxapp_url_pattern % "image/upload", methods=["POST", 'GET'])
def img_upload():
    """
    上传图片视图
    """

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"result": "FAIL1"})
        ufile = request.files['file']
        if ufile.filename == '':
            return jsonify({"result": "FAIL2"})
        ufile.save("/tmp/%s"%ufile.filename)
        img = imgInfo(**{"filename": ufile.filename, "create_time": datetime.datetime.now()})
        db.session.add(img)
        db.session.commit()
        return jsonify({"result": "OK", "error_msg": "", 'url': "http://192.168.1.191:9922/wxapp/image/show/?id=%s"%img.id})
    return render_template("imgupload.html") 


@wxapp.route(wxapp_url_pattern % "image/show", methods=["POST", 'GET'])
def img_url():
    """
    图片链接
    """
    
    idl = request.args.get("id")
    img = imgInfo.query.filter_by(id=idl).first()
    if not img:
        return 
    file_open = open("/tmp/%s"%img.filename, 'rb')
    response = Response(file_open, mimetype="image/jpg")
    return response
    

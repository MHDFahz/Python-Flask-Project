<!-- Flask Run -->
    -->goto project directory
    --> export FLASK_APP=flaskblog.py //set an enviroment variable that run flask
    -->flask run
    -->ctrl+c  //stop server

<!-- Without restart server Run -->
    -->export FLASK_DEBUG=1
    -->flask run

<!-- Without environment variable -->
    if __name__ == "__main__":
        app.run(debug=True)
    --> python flaskbog.py

<!-- Template (html file)-->
    //To work with template we want import
    from flask render_template

<!-- find exact location og routes -->
    //to link css from static folder
    import url_for from flask
    <link rel="stylesheet" type="text/css href="{{ url_for('static',filename='main.css')}}">
 <!-- flask_wtf --># Python-Flask-Project

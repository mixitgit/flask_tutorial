import os
from flaskr import create_app
from flaskr.db import init_app, init_db
from gevent.pywsgi import WSGIServer


app_settings = os.getenv('ENV')
port = int(os.getenv('PORT', '5000'))

if __name__ == '__main__':
    app = create_app({})
    init_app(app)
    with app.app_context():
        init_db()
    if app_settings == 'prod':
        server = WSGIServer(('0.0.0.0', port), app)
        server.serve_forever()
    else:
        app.run(debug=True, port=port)

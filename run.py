from debugger import create_app
from debugger import manager


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#if __name__ == '__main__':
    #manager.run()



#serves as an entry point to our application
#it gets a copy of the app package and runs it
import os

from app import create_app

app = create_app(os.getenv('APP_SETTINGS'))

if __name__ == '__main__':
	app.run(debug=True)

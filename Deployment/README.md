# Deploying to a hosting service

- From the command line, use `heroku login` to authenticate to Heroku

- `runtime.txt` tells Heroku what version of Python you want to run

- `requirements.txt` is used by Heroku (through pip) to install dependencies of your application that aren't in the Python standard library.

- `Procfile` is used by Heroku to specify the command line for running your application

- Use `heroku create your-app-name` to tell Heroku about your app and give it a name.

- Finally, use `git push heroku master` to deploy your app!

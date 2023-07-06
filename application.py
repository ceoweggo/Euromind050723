from app import my_first_application_config
application = my_first_application_config()

if __name__ == "__main__":
  from config.config import application_env
  if application_env == 'development':
    application.run(port=5000)
  else:
    # DEPLOYMENT SERVER (SIMILAR TO WSGI)
    from waitress import serve
    serve(application, host="0.0.0.0", port=8080)
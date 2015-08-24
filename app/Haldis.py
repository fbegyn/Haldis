from setup import setup_app, setup_bootstrap, setup_database, setup_routes

app = setup_app()
setup_bootstrap(app)
setup_routes(app)

db = setup_database(app)


if __name__ == "__main__":
    app.run(debug=True)

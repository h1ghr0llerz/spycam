from application import app, db, User, Threshold

if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    # Create inital DB
    # TODO: add the real users
    db.session.add(User(1, [[0]*128], 10.5, 0))
    db.session.add(User(2, [[0.1]*128], 20.5, 1))
    db.session.add(User(3, [[0.2]*128], 30.5, 2))
    db.session.add(User(4, [[0.3]*128], 40.5, 3))
    db.session.add(User(5, [[0.4]*128], 50.5, 4))
    db.session.add(User(6, [[0.5]*128], 60.5, 5))

    db.session.add(Threshold(5)) # TODO: set the real threshold
    
    db.session.commit()

    app.run(debug=True, host='0.0.0.0', port=1337, ssl_context='adhoc')
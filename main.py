from flask import Flask, render_template, url_for, request, render_template
import pandas as pd
app = Flask(__name__)



@app.route("/",methods = {'GET','POST'})
@app.route("/home",methods = {'GET','POST'})
def home():
    response = {'Number': '20.0⌃', 'Name': 'zack moss', 'Age': '24⌃', 'Pos': 'rb', 'Weight': '223⌄','Confrence':'NFC' ,'Division': 'afc east', 'Team': ' buffalo bills '}
    global posts
    tries1 = len(tries)
    invalid = False
    if request.method == 'POST':
        text = request.form['playerName']
        processed_text = text
        guess = processed_text
        if guess not in names:
            invalid = True
            print(invalid)
            return render_template('home.html', posts=posts, result=response, names=names, tries=tries1, invalid = invalid)
        print(guess)
        guessRow = data[data['Name'] == str(guess)]
        print(guessRow)
        if int(guessRow.iloc[0]['Number']) == int(pick.iloc[0]['Number']):
            response['Number'] = str(guessRow.iloc[0]['Number'])
        if int(guessRow.iloc[0]['Number']) > int(pick.iloc[0]['Number']):
            response['Number'] = str(str(guessRow.iloc[0]['Number']) + "⌄")
        if int(guessRow.iloc[0]['Number']) < int(pick.iloc[0]['Number']):
            response['Number'] = str(str(guessRow.iloc[0]['Number']) + "⌃")

        if guessRow.iloc[0]['Name'] == pick.iloc[0]['Name']:
            response['Name'] = guessRow.iloc[0]['Name'].upper()
        else:
            response['Name'] = guessRow.iloc[0]['Name'].lower()

        guessconf= guessRow.iloc[0]['Division'].split()[0]
        print(guessconf)
        pickconf = pick.iloc[0]['Division'].split()[0]
        print(pickconf)
        if guessconf == pickconf:
            response['Confrence'] = guessconf.upper()
        else:
            response['Confrence'] = guessconf.lower()

        if guessRow.iloc[0]['Division'] == pick.iloc[0]['Division']:
            response['Division'] = guessRow.iloc[0]['Division'].upper()
        else:
            response['Division'] = guessRow.iloc[0]['Division'].lower()

        if guessRow.iloc[0]['Team'] == pick.iloc[0]['Team']:
            response['Team'] = guessRow.iloc[0]['Team'].upper()
        else:
            response['Team'] = guessRow.iloc[0]['Team'].lower()

        if int(guessRow.iloc[0]['Age']) == int(pick.iloc[0]['Age']):
            response['Age'] = str(guessRow.iloc[0]['Age'])
        if int(guessRow.iloc[0]['Age']) > int(pick.iloc[0]['Age']):
            response['Age'] = str(str(guessRow.iloc[0]['Age']) + "⌄")
        if int(guessRow.iloc[0]['Age']) < int(pick.iloc[0]['Age']):
            response['Age'] = str(str(guessRow.iloc[0]['Age']) + "⌃")

        if guessRow.iloc[0]['Pos'] == pick.iloc[0]['Pos']:
            response['Pos'] = guessRow.iloc[0]['Pos'].upper()
        else:
            response['Pos'] = guessRow.iloc[0]['Pos'].lower()

        if int(guessRow.iloc[0]['Weight']) == int(pick.iloc[0]['Weight']):
            response['Weight'] = str(guessRow.iloc[0]['Weight'])
        if int(guessRow.iloc[0]['Weight']) > int(pick.iloc[0]['Weight']):
            response['Weight'] = str(str(guessRow.iloc[0]['Weight']) + "⌄")
        if int(guessRow.iloc[0]['Weight']) < int(pick.iloc[0]['Weight']):
            response['Weight'] = str(str(guessRow.iloc[0]['Weight']) + "⌃")


        posts.append(response)
        print(posts)
        if guessRow.iloc[0]['Name'] == pick.iloc[0]['Name']:
            return render_template('winner.html')
        elif len(tries) > 7:
            return render_template('loser.html', result = response, postspick = [pick])
        else:
            print(tries)
            tries.append(1)

            print(tries)
            tries1 = len(tries)
        print(pick)
    return render_template('home.html', posts=posts, result = response, names = names, tries = tries1, invalid = invalid)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    data = pd.read_csv('output.csv')

    starters = ['Kyler Murray', 'Kenyan Drake', 'Larry Fitzgerald', 'DeAndre Hopkins', 'Christian Kirk', 'Maxx Williams', 'D.J. Humphries', 'Justin Pugh', 'Mason Cole', 'J.R. Sweezy', 'Kelvin Beachum', 'Zach Allen', 'Corey Peters', 'Jordan Phillips', 'Haason Reddick', "De'Vondre Campbell", 'Jordan Hicks', 'Markus Golden', 'Patrick Peterson', 'Dre Kirkpatrick', 'Budda Baker+', 'Jalen Thompson', 'Matt Ryan', 'Todd Gurley', 'Keith Smith', 'Julio Jones', 'Calvin Ridley', 'Luke Stocker', 'Jake Matthews', 'James Carpenter', 'Alex Mack', 'Chris Lindstrom', 'Kaleb McGary', 'Steven Means', 'Grady Jarrett', 'Tyeler Davison', 'Dante Fowler', 'Deion Jones', 'Foyesade Oluokun', 'Mykal Walker', 'AJ Terrell', 'Isaiah Oliver', 'Ricardo Allen', 'Keanu Neal', 'Lamar Jackson', 'Mark Ingram', 'Patrick Ricard', 'Miles Boykin', 'Marquise Brown', 'Nick Boyle', 'Orlando Brown Jr.', 'Bradley Bozeman', 'Matt Skura', 'Ben Powers', 'D.J. Fluker', 'Calais Campbell', 'Brandon Williams', 'Derek Wolfe', 'Pernell McPhee', 'Patrick Queen', 'L.J. Fort', 'Matt Judon', 'Marlon Humphrey', 'Marcus Peters', 'Chuck Clark', 'DeShon Elliott', 'Josh Allen', 'Devin Singletary', 'John Brown', 'Gabriel Davis', 'Stefon Diggs+', 'Dawson Knox', 'Dion Dawkins', 'Ike Boettger', 'Mitch Morse', 'Brian Winters', 'Daryl Williams', 'Jerry Hughes', 'Vernon Butler', 'Ed Oliver', 'Mario Addison', 'A.J. Klein', 'Tremaine Edmunds', "Tre'Davious White", 'Levi Wallace', 'Jordan Poyer', 'Micah Hyde', 'Taron Johnson', 'Teddy Bridgewater', 'Mike Davis', 'Robby Anderson', 'D.J. Moore', 'Curtis Samuel', 'Chris Manhertz', 'Russell Okung', 'Chris Reed', 'Matt Paradis', 'John Miller', 'Taylor Moton', 'Brian Burns', 'Bravvion Roy', 'Derrick Brown', 'Stephen Weatherly', 'Shaq Thompson', 'Tahir Whitehead', 'Jeremy Chinn', 'Donte Jackson', 'Rasul Douglas', 'Juston Burris', 'Tre Boston', 'Mitchell Trubisky', 'David Montgomery', 'Anthony Miller', 'Allen Robinson', 'Jimmy Graham', 'Cole Kmet', 'Charles Leno Jr.', 'James Daniels', 'Cody Whitehair', 'Germain Ifedi', 'Bobby Massie', 'Akiem Hicks', 'Brent Urban', 'Bilal Nichols', 'Khalil Mack', 'Roquan Smith', 'Danny Trevathan', 'Robert Quinn', 'Kyle Fuller', 'Jaylon Johnson', 'Tashaun Gipson', 'Eddie Jackson', 'Joe Burrow', 'Giovani Bernard', 'A.J. Green', 'Tee Higgins', 'Cethan Carter', 'Drew Sample', 'Jonah Williams', 'Michael Jordan', 'Trey Hopkins', 'Alex Redmond', 'Bobby Hart', 'Sam Hubbard', 'Mike Daniels', 'Christian Covington', 'Carl Lawson', 'Josh Bynes', 'Germaine Pratt', 'Darius Phillips', 'Mackensie Alexander', 'William Jackson III', 'Vonn Bell', 'Jessie Bates III', 'Baker Mayfield', 'Nick Chubb', 'Odell Beckham Jr.', 'Jarvis Landry', 'Harrison Bryant', 'Austin Hooper', 'Jedrick Wills Jr.', 'Joel Bitonio', 'J.C. Tretter', 'Wyatt Teller', 'Jack Conklin+', 'Myles Garrett+', 'Sheldon Richardson', 'Larry Ogunjobi', 'Olivier Vernon', 'Mack Wilson', 'B.J. Goodson', 'Sione Takitaki', 'Denzel Ward', 'Terrance Mitchell', 'Karl Joseph', 'Andrew Sendejo', 'Andy Dalton', 'Ezekiel Elliott', 'Amari Cooper', 'Michael Gallup', 'CeeDee Lamb', 'Dalton Schultz', 'Brandon Knight', 'Connor Williams', 'Joe Looney', 'Zack Martin', 'Terence Steele', 'DeMarcus Lawrence', 'Antwaun Woods', 'Neville Gallimore', 'Aldon Smith', 'Leighton Vander Esch', 'Jaylon Smith', 'Anthony Brown', 'Trevon Diggs', 'Donovan Wilson', 'Xavier Woods', 'Jourdan Lewis', 'Drew Lock', 'Melvin Gordon', 'Jerry Jeudy', 'Tim Patrick', 'Noah Fant', 'Nick Vannett', 'Garett Bolles', 'Dalton Risner', 'Lloyd Cushenberry III', 'Graham Glasgow', 'Demar Dotson', 'Shelby Harris', 'DeShawn Williams', "Dre'Mont Jones", 'Malik Reed', 'Alexander Johnson', 'Josey Jewell', 'Bradley Chubb', 'A.J. Bouye', 'Bryce Callahan', 'Kareem Jackson', 'Justin Simmons', 'Matthew Stafford', 'Adrian Peterson', 'Kenny Golladay', 'Marvin Jones', 'T.J. Hockenson', 'Jesse James', 'Taylor Decker', 'Jonah Jackson', 'Frank Ragnow', 'Oday Aboushi', 'Tyrell Crosby', 'Trey Flowers', 'Danny Shelton', 'John Penisini', 'Romeo Okwara', 'Christian Jones', 'Jahlani Tavai', 'Jamie Collins', 'Desmond Trufant', 'Amani Oruwariye', 'Jayron Kearse', 'Duron Harmon', 'Aaron Rodgers+', 'Aaron Jones', 'Davante Adams+', 'Marquez Valdes-Scantling', 'Marcedes Lewis', 'Robert Tonyan', 'David Bakhtiari+', 'Elgton Jenkins', 'Corey Linsley+', 'Lucas Patrick', 'Billy Turner', 'Dean Lowry', 'Kenny Clark', 'Kingsley Keke', 'Preston Smith', 'Christian Kirksey', 'Krys Barnes', "Za'Darius Smith", 'Jaire Alexander', 'Kevin King', 'Adrian Amos', 'Darnell Savage Jr.', 'Deshaun Watson', 'David Johnson', 'Brandin Cooks', 'Will Fuller', 'Pharaoh Brown', 'Darren Fells', 'Laremy Tunsil', 'Max Scharping', 'Nick Martin', 'Zach Fulton', 'Tytus Howard', 'J.J. Watt', 'Brandon Dunn', 'P.J. Hall', 'Whitney Mercilus', 'Zach Cunningham', 'Tyrell Adams', 'Brennan Scarlett', 'Bradley Roby', 'Vernon Hargreaves III', 'Justin Reid', 'Eric Murray', 'Philip Rivers', 'Jonathan Taylor', 'T.Y. Hilton', 'Zach Pascal', 'Michael Pittman Jr.', 'Jack Doyle', 'Anthony Castonzo', 'Quenton Nelson+', 'Ryan Kelly', 'Mark Glowinski', 'Braden Smith', 'Justin Houston', 'DeForest Buckner+', 'Grover Stewart', 'Denico Autry', 'Darius Leonard+', 'Anthony Walker', 'Bobby Okereke', 'Kenny Moore', 'Xavier Rhodes', 'Khari Willis', 'Julian Blackmon', 'Gardner Minshew II', 'James Robinson', 'Bruce Miller', 'DJ Chark', 'Laviska Shenault Jr.', "James O'Shaughnessy", 'Cam Robinson', 'Andrew Norwell', 'Brandon Linder', 'A.J. Cann', 'Jawaan Taylor', 'Josh Allen', 'Taven Bryan', 'Doug Costin', 'Adam Gotsis', 'Myles Jack', 'Joe Schobert', 'Kamalei Correa', 'C.J. Henderson', 'Sidney Jones', 'Josh Jones', 'Jarrod Wilson', 'Patrick Mahomes', 'Clyde Edwards-Helaire', 'Tyreek Hill+', 'Demarcus Robinson', 'Sammy Watkins', 'Travis Kelce+', 'Eric Fisher', 'Nick Allegretti', 'Austin Reiter', 'Andrew Wylie', 'Mike Remmers', 'Tanoh Kpassagnon', 'Chris Jones', 'Derrick Nnadi', 'Frank Clark', 'Anthony Hitchens', 'Damien Wilson', 'Willie Gay Jr.', 'Charvarius Ward', 'Bashaud Breeland', 'Tyrann Mathieu+', 'Juan Thornhill', 'Derek Carr', 'Josh Jacobs', 'Nelson Agholor', 'Henry Ruggs III', 'Darren Waller', 'Jason Witten', 'Kolton Miller', 'Denzelle Good', 'Rodney Hudson', 'Gabe Jackson', 'Sam Young', 'Clelin Ferrell', 'Johnathan Hankins', 'Maliek Collins', 'Maxx Crosby', 'Nicholas Morrow', 'Nick Kwiatkoski', 'Cory Littleton', 'Trayvon Mullen', 'Nevin Lawson', 'Johnathan Abram', 'Erik Harris', 'Justin Herbert', 'Austin Ekeler', 'Keenan Allen', 'Jalen Guyton', 'Mike Williams', 'Hunter Henry', 'Sam Tevi', 'Forrest Lamp', 'Dan Feeney', 'Trai Turner', 'Bryan Bulaga', 'Joey Bosa', 'Justin Jones', 'Linval Joseph', 'Melvin Ingram', 'Kyzir White', 'Kenneth Murray', 'Michael Davis', 'Casey Hayward', 'Rayshawn Jenkins', 'Nasir Adderley', 'Chris Harris Jr.', 'Jared Goff', 'Darrell Henderson', 'Cooper Kupp', 'Josh Reynolds', 'Robert Woods', 'Tyler Higbee', 'Andrew Whitworth', 'David Edwards', 'Austin Blythe', 'Austin Corbett', 'Rob Havenstein', 'Michael Brockers', 'Aaron Donald+', 'Sebastian Joseph-Day', 'Samson Ebukam', 'Troy Reeder', 'Kenny Young', 'Leonard Floyd', 'Troy Hill', 'Jalen Ramsey+', 'Jordan Fuller', 'John Johnson', 'Tua Tagovailoa', 'Myles Gaskin', 'DeVante Parker', 'Preston Williams', 'Mike Gesicki', 'Durham Smythe', 'Austin Jackson', 'Ereck Flowers', 'Ted Karras', 'Solomon Kindley', 'Robert Hunt', 'Christian Wilkins', 'Raekwon Davis', 'Emmanuel Ogbah', 'Andrew Van Ginkel', 'Elandon Roberts', 'Jerome Baker', 'Kyle Van Noy', 'Byron Jones', 'Xavien Howard+', 'Bobby McCain', 'Eric Rowe', 'Kirk Cousins', 'Dalvin Cook', 'C.J. Ham', 'Justin Jefferson', 'Adam Thielen', 'Kyle Rudolph', 'Riley Reiff', 'Dakota Dozier', 'Garrett Bradbury', 'Ezra Cleveland', "Brian O'Neill", 'Yannick Ngakoue', 'Ifeadi Odenigbo', 'Shamar Stephen', 'Jaleel Johnson', 'Troy Dye', 'Eric Kendricks', 'Eric Wilson', 'Cameron Dantzler', 'Jeff Gladney', 'Harrison Smith', 'Anthony Harris', 'Cam Newton', 'Damien Harris', 'Jakob Johnson', 'Damiere Byrd', "N'Keal Harry", 'Ryan Izzo', 'Isaiah Wynn', 'Joe Thuney', 'David Andrews', 'Shaq Mason', 'Michael Onwenu', 'Deatrich Wise Jr.', 'Lawrence Guy', 'Byron Cowart', 'John Simon', "Ja'Whaun Bentley", 'Terez Hall', 'Jason McCourty', 'Stephon Gilmore', 'Adrian Phillips', 'Devin McCourty', 'Jonathan Jones', 'Drew Brees', 'Alvin Kamara', 'Michael Burton', 'Emmanuel Sanders', "Tre'Quan Smith", 'Jared Cook', 'Terron Armstead ', 'Andrus Peat', 'Erik McCoy', 'Cesar Ruiz', 'Ryan Ramczyk', 'Cameron Jordan', 'David Onyemata', 'Malcom Brown', 'Trey Hendrickson', 'Kwon Alexander', 'Demario Davis', 'Janoris Jenkins', 'Marshon Lattimore', 'Malcolm Jenkins', 'Marcus Williams', 'Chauncey Gardner-Johnson', 'Daniel Jones', 'Wayne Gallman', 'Sterling Shepard', 'Darius Slayton', 'Evan Engram', 'Kaden Smith', 'Andrew Thomas', 'Shane Lemieux', 'Nick Gates', 'Kevin Zeitler', 'Cameron Fleming', 'Dexter Lawrence', 'Leonard Williams', 'Dalvin Tomlinson', 'Lorenzo Carter', 'Blake Martinez', 'Tae Crowder', 'Kyler Fackrell', 'James Bradberry', 'Isaac Yiadom', 'Jabrill Peppers', 'Logan Ryan', 'Sam Darnold', 'Frank Gore', 'Jamison Crowder', 'Denzel Mims', 'Breshad Perriman', 'Chris Herndon', 'Mekhi Becton', 'Connor McGovern', 'Greg Van Roten', 'George Fant', 'Henry Anderson', 'Folorunso Fatukasi', 'Quinnen Williams', 'Tarell Basham', 'Harvey Langi', 'Neville Hewitt', 'Jordan Jenkins', 'Bryce Hall', 'Blessuan Austin', 'Ashtyn Davis', 'Marcus Maye', 'Carson Wentz', 'Miles Sanders', 'Travis Fulgham', 'Jalen Reagor', 'Zach Ertz', 'Dallas Goedert', 'Jordan Mailata', 'Isaac Seumalo', 'Jason Kelce', 'Nate Herbig', 'Lane Johnson', 'Derek Barnett', 'Javon Hargrave', 'Fletcher Cox', 'Brandon Graham', 'Alex Singleton', 'T.J. Edwards', 'Duke Riley', 'Avonte Maddox', 'Darius Slay', 'Rodney McLeod', 'Jalen Mills', 'Ben Roethlisberger', 'James Conner', 'Diontae Johnson', 'JuJu Smith-Schuster', 'James Washington', 'Vance McDonald', 'Alejandro Villanueva', 'Matt Feiler', 'Maurkice Pouncey', 'David DeCastro', 'Chukwuma Okorafor', 'Stephon Tuitt', 'Cameron Heyward', 'Tyson Alualu', 'T.J. Watt+', 'Robert Spillane', 'Vince Williams', 'Bud Dupree', 'Joe Haden', 'Steven Nelson', 'Terrell Edmunds', 'Minkah Fitzpatrick+', 'Nick Mullens', 'Raheem Mostert', 'Kyle Juszczyk', 'Brandon Aiyuk', 'Richie James', 'George Kittle', 'Trent Williams', 'Laken Tomlinson', 'Ben Garland', 'Daniel Brunskill', 'Mike McGlinchey', 'Arik Armstead', 'Javon Kinlaw', 'D.J. Jones', 'Kerry Hyder', 'Azeez Al-Shaair', 'Fred Warner+', 'Dre Greenlaw', 'Jason Verrett', 'Emmanuel Moseley', 'Tarvarius Moore', 'Jimmie Ward', 'Russell Wilson', 'Chris Carson', 'Tyler Lockett', 'D.K. Metcalf', 'David Moore', 'Greg Olsen', 'Duane Brown', 'Mike Iupati', 'Ethan Pocic', 'Damien Lewis', 'Brandon Shell', 'L.J. Collier', 'Jarran Reed', 'Poona Ford', 'Benson Mayowa', 'Bobby Wagner+', 'K.J. Wright', 'Shaquill Griffin', 'D.J. Reed', 'Jamal Adams', 'Quandre Diggs', 'Ugo Amadi', 'Tom Brady', 'Ronald Jones II', 'Mike Evans', 'Chris Godwin', 'Scott Miller', 'Rob Gronkowski', 'Donovan Smith', 'Ali Marpet', 'Ryan Jensen', 'Alex Cappa', 'Tristan Wirfs', 'Ndamukong Suh', 'Rakeem Nunez-Roches', 'William Gholston', 'Jason Pierre-Paul', 'Devin White', 'Lavonte David', 'Shaquil Barrett', 'Carlton Davis', 'Sean Murphy-Bunting', 'Antoine Winfield Jr.', 'Jordan Whitehead', 'Ryan Tannehill', 'Derrick Henry +', 'Khari Blasingame', 'A.J. Brown', 'Corey Davis', 'Jonnu Smith', 'David Quessenberry', 'Rodger Saffold', 'Ben Jones', 'Nate Davis', 'Dennis Kelly', 'Jack Crawford', 'Jeffery Simmons', 'DaQuan Jones', 'Jadeveon Clowney', 'Rashaan Evans', 'Jayon Brown', 'Harold Landry', 'Johnathan Joseph', 'Malcolm Butler', 'Kenny Vaccaro', 'Kevin Byard', 'Alex Smith', 'Antonio Gibson', 'Terry McLaurin', 'Cam Sims', 'Jeremy Sprinkle', 'Logan Thomas', 'Cornelius Lucas', 'Wes Schweitzer', 'Chase Roullier', 'Brandon Scherff+', 'Morgan Moses', 'Chase Young', 'Daron Payne', 'Jonathan Allen', 'Montez Sweat', 'Cole Holcomb', 'Jonathan Bostic', 'Kevin Pierre-Louis', 'Kendall Fuller', 'Ronald Darby', 'Kamren Curl', 'Troy Apke']
    data = data[data.Number != '']
    names = data['Name'].tolist()
    pickable = data[data['Name'].isin(starters)]
    print(pickable)
    pick = pickable.sample()
    print(pick)
    posts = []
    tries = [1]
    past = pd.DataFrame()
    app.run(host='0.0.0.0')
from flask import Flask, render_template, url_for, request, render_template, make_response, redirect
import pandas as pd
import json
from datetime import datetime, timedelta

app = Flask(__name__)
response = {'Number': '20.0⌃', 'Name': 'zack moss', 'Age': '24⌃','Offense/Defense': 'test', 'Pos': 'rb', 'Weight': '223⌄', 'Confrence': 'NFC',
            'Division': 'afc east', 'Team': ' buffalo bills '}

data = pd.read_csv('output.csv')
starters = ['Kyler Murray', 'Kenyan Drake', 'Larry Fitzgerald', 'DeAndre Hopkins', 'Christian Kirk', 'Maxx Williams',
            'D.J. Humphries', 'Justin Pugh', 'Mason Cole', 'J.R. Sweezy', 'Kelvin Beachum', 'Zach Allen',
            'Corey Peters', 'Jordan Phillips', 'Haason Reddick', "De'Vondre Campbell", 'Jordan Hicks', 'Markus Golden',
            'Patrick Peterson', 'Dre Kirkpatrick', 'Budda Baker+', 'Jalen Thompson', 'Matt Ryan', 'Todd Gurley',
            'Keith Smith', 'Julio Jones', 'Calvin Ridley', 'Luke Stocker', 'Jake Matthews', 'James Carpenter',
            'Alex Mack', 'Chris Lindstrom', 'Kaleb McGary', 'Steven Means', 'Grady Jarrett', 'Tyeler Davison',
            'Dante Fowler', 'Deion Jones', 'Foyesade Oluokun', 'Mykal Walker', 'AJ Terrell', 'Isaiah Oliver',
            'Ricardo Allen', 'Keanu Neal', 'Lamar Jackson', 'Mark Ingram', 'Patrick Ricard', 'Miles Boykin',
            'Marquise Brown', 'Nick Boyle', 'Orlando Brown Jr.', 'Bradley Bozeman', 'Matt Skura', 'Ben Powers',
            'D.J. Fluker', 'Calais Campbell', 'Brandon Williams', 'Derek Wolfe', 'Pernell McPhee', 'Patrick Queen',
            'L.J. Fort', 'Matt Judon', 'Marlon Humphrey', 'Marcus Peters', 'Chuck Clark', 'DeShon Elliott',
            'Josh Allen', 'Devin Singletary', 'John Brown', 'Gabriel Davis', 'Stefon Diggs+', 'Dawson Knox',
            'Dion Dawkins', 'Ike Boettger', 'Mitch Morse', 'Brian Winters', 'Daryl Williams', 'Jerry Hughes',
            'Vernon Butler', 'Ed Oliver', 'Mario Addison', 'A.J. Klein', 'Tremaine Edmunds', "Tre'Davious White",
            'Levi Wallace', 'Jordan Poyer', 'Micah Hyde', 'Taron Johnson', 'Teddy Bridgewater', 'Mike Davis',
            'Robby Anderson', 'D.J. Moore', 'Curtis Samuel', 'Chris Manhertz', 'Russell Okung', 'Chris Reed',
            'Matt Paradis', 'John Miller', 'Taylor Moton', 'Brian Burns', 'Bravvion Roy', 'Derrick Brown',
            'Stephen Weatherly', 'Shaq Thompson', 'Tahir Whitehead', 'Jeremy Chinn', 'Donte Jackson', 'Rasul Douglas',
            'Juston Burris', 'Tre Boston', 'Mitchell Trubisky', 'David Montgomery', 'Anthony Miller', 'Allen Robinson',
            'Jimmy Graham', 'Cole Kmet', 'Charles Leno Jr.', 'James Daniels', 'Cody Whitehair', 'Germain Ifedi',
            'Bobby Massie', 'Akiem Hicks', 'Brent Urban', 'Bilal Nichols', 'Khalil Mack', 'Roquan Smith',
            'Danny Trevathan', 'Robert Quinn', 'Kyle Fuller', 'Jaylon Johnson', 'Tashaun Gipson', 'Eddie Jackson',
            'Joe Burrow', 'Giovani Bernard', 'A.J. Green', 'Tee Higgins', 'Cethan Carter', 'Drew Sample',
            'Jonah Williams', 'Michael Jordan', 'Trey Hopkins', 'Alex Redmond', 'Bobby Hart', 'Sam Hubbard',
            'Mike Daniels', 'Christian Covington', 'Carl Lawson', 'Josh Bynes', 'Germaine Pratt', 'Darius Phillips',
            'Mackensie Alexander', 'William Jackson III', 'Vonn Bell', 'Jessie Bates III', 'Baker Mayfield',
            'Nick Chubb', 'Odell Beckham Jr.', 'Jarvis Landry', 'Harrison Bryant', 'Austin Hooper', 'Jedrick Wills Jr.',
            'Joel Bitonio', 'J.C. Tretter', 'Wyatt Teller', 'Jack Conklin+', 'Myles Garrett+', 'Sheldon Richardson',
            'Larry Ogunjobi', 'Olivier Vernon', 'Mack Wilson', 'B.J. Goodson', 'Sione Takitaki', 'Denzel Ward',
            'Terrance Mitchell', 'Karl Joseph', 'Andrew Sendejo', 'Andy Dalton', 'Ezekiel Elliott', 'Amari Cooper',
            'Michael Gallup', 'CeeDee Lamb', 'Dalton Schultz', 'Brandon Knight', 'Connor Williams', 'Joe Looney',
            'Zack Martin', 'Terence Steele', 'DeMarcus Lawrence', 'Antwaun Woods', 'Neville Gallimore', 'Aldon Smith',
            'Leighton Vander Esch', 'Jaylon Smith', 'Anthony Brown', 'Trevon Diggs', 'Donovan Wilson', 'Xavier Woods',
            'Jourdan Lewis', 'Drew Lock', 'Melvin Gordon', 'Jerry Jeudy', 'Tim Patrick', 'Noah Fant', 'Nick Vannett',
            'Garett Bolles', 'Dalton Risner', 'Lloyd Cushenberry III', 'Graham Glasgow', 'Demar Dotson',
            'Shelby Harris', 'DeShawn Williams', "Dre'Mont Jones", 'Malik Reed', 'Alexander Johnson', 'Josey Jewell',
            'Bradley Chubb', 'A.J. Bouye', 'Bryce Callahan', 'Kareem Jackson', 'Justin Simmons', 'Matthew Stafford',
            'Adrian Peterson', 'Kenny Golladay', 'Marvin Jones', 'T.J. Hockenson', 'Jesse James', 'Taylor Decker',
            'Jonah Jackson', 'Frank Ragnow', 'Oday Aboushi', 'Tyrell Crosby', 'Trey Flowers', 'Danny Shelton',
            'John Penisini', 'Romeo Okwara', 'Christian Jones', 'Jahlani Tavai', 'Jamie Collins', 'Desmond Trufant',
            'Amani Oruwariye', 'Jayron Kearse', 'Duron Harmon', 'Aaron Rodgers+', 'Aaron Jones', 'Davante Adams+',
            'Marquez Valdes-Scantling', 'Marcedes Lewis', 'Robert Tonyan', 'David Bakhtiari+', 'Elgton Jenkins',
            'Corey Linsley+', 'Lucas Patrick', 'Billy Turner', 'Dean Lowry', 'Kenny Clark', 'Kingsley Keke',
            'Preston Smith', 'Christian Kirksey', 'Krys Barnes', "Za'Darius Smith", 'Jaire Alexander', 'Kevin King',
            'Adrian Amos', 'Darnell Savage Jr.', 'Deshaun Watson', 'David Johnson', 'Brandin Cooks', 'Will Fuller',
            'Pharaoh Brown', 'Darren Fells', 'Laremy Tunsil', 'Max Scharping', 'Nick Martin', 'Zach Fulton',
            'Tytus Howard', 'J.J. Watt', 'Brandon Dunn', 'P.J. Hall', 'Whitney Mercilus', 'Zach Cunningham',
            'Tyrell Adams', 'Brennan Scarlett', 'Bradley Roby', 'Vernon Hargreaves III', 'Justin Reid', 'Eric Murray',
            'Philip Rivers', 'Jonathan Taylor', 'T.Y. Hilton', 'Zach Pascal', 'Michael Pittman Jr.', 'Jack Doyle',
            'Anthony Castonzo', 'Quenton Nelson+', 'Ryan Kelly', 'Mark Glowinski', 'Braden Smith', 'Justin Houston',
            'DeForest Buckner+', 'Grover Stewart', 'Denico Autry', 'Darius Leonard+', 'Anthony Walker', 'Bobby Okereke',
            'Kenny Moore', 'Xavier Rhodes', 'Khari Willis', 'Julian Blackmon', 'Gardner Minshew II', 'James Robinson',
            'Bruce Miller', 'DJ Chark', 'Laviska Shenault Jr.', "James O'Shaughnessy", 'Cam Robinson', 'Andrew Norwell',
            'Brandon Linder', 'A.J. Cann', 'Jawaan Taylor', 'Josh Allen', 'Taven Bryan', 'Doug Costin', 'Adam Gotsis',
            'Myles Jack', 'Joe Schobert', 'Kamalei Correa', 'C.J. Henderson', 'Sidney Jones', 'Josh Jones',
            'Jarrod Wilson', 'Patrick Mahomes', 'Clyde Edwards-Helaire', 'Tyreek Hill+', 'Demarcus Robinson',
            'Sammy Watkins', 'Travis Kelce+', 'Eric Fisher', 'Nick Allegretti', 'Austin Reiter', 'Andrew Wylie',
            'Mike Remmers', 'Tanoh Kpassagnon', 'Chris Jones', 'Derrick Nnadi', 'Frank Clark', 'Anthony Hitchens',
            'Damien Wilson', 'Willie Gay Jr.', 'Charvarius Ward', 'Bashaud Breeland', 'Tyrann Mathieu+',
            'Juan Thornhill', 'Derek Carr', 'Josh Jacobs', 'Nelson Agholor', 'Henry Ruggs III', 'Darren Waller',
            'Jason Witten', 'Kolton Miller', 'Denzelle Good', 'Rodney Hudson', 'Gabe Jackson', 'Sam Young',
            'Clelin Ferrell', 'Johnathan Hankins', 'Maliek Collins', 'Maxx Crosby', 'Nicholas Morrow',
            'Nick Kwiatkoski', 'Cory Littleton', 'Trayvon Mullen', 'Nevin Lawson', 'Johnathan Abram', 'Erik Harris',
            'Justin Herbert', 'Austin Ekeler', 'Keenan Allen', 'Jalen Guyton', 'Mike Williams', 'Hunter Henry',
            'Sam Tevi', 'Forrest Lamp', 'Dan Feeney', 'Trai Turner', 'Bryan Bulaga', 'Joey Bosa', 'Justin Jones',
            'Linval Joseph', 'Melvin Ingram', 'Kyzir White', 'Kenneth Murray', 'Michael Davis', 'Casey Hayward',
            'Rayshawn Jenkins', 'Nasir Adderley', 'Chris Harris Jr.', 'Jared Goff', 'Darrell Henderson', 'Cooper Kupp',
            'Josh Reynolds', 'Robert Woods', 'Tyler Higbee', 'Andrew Whitworth', 'David Edwards', 'Austin Blythe',
            'Austin Corbett', 'Rob Havenstein', 'Michael Brockers', 'Aaron Donald+', 'Sebastian Joseph-Day',
            'Samson Ebukam', 'Troy Reeder', 'Kenny Young', 'Leonard Floyd', 'Troy Hill', 'Jalen Ramsey+',
            'Jordan Fuller', 'John Johnson', 'Tua Tagovailoa', 'Myles Gaskin', 'DeVante Parker', 'Preston Williams',
            'Mike Gesicki', 'Durham Smythe', 'Austin Jackson', 'Ereck Flowers', 'Ted Karras', 'Solomon Kindley',
            'Robert Hunt', 'Christian Wilkins', 'Raekwon Davis', 'Emmanuel Ogbah', 'Andrew Van Ginkel',
            'Elandon Roberts', 'Jerome Baker', 'Kyle Van Noy', 'Byron Jones', 'Xavien Howard+', 'Bobby McCain',
            'Eric Rowe', 'Kirk Cousins', 'Dalvin Cook', 'C.J. Ham', 'Justin Jefferson', 'Adam Thielen', 'Kyle Rudolph',
            'Riley Reiff', 'Dakota Dozier', 'Garrett Bradbury', 'Ezra Cleveland', "Brian O'Neill", 'Yannick Ngakoue',
            'Ifeadi Odenigbo', 'Shamar Stephen', 'Jaleel Johnson', 'Troy Dye', 'Eric Kendricks', 'Eric Wilson',
            'Cameron Dantzler', 'Jeff Gladney', 'Harrison Smith', 'Anthony Harris', 'Cam Newton', 'Damien Harris',
            'Jakob Johnson', 'Damiere Byrd', "N'Keal Harry", 'Ryan Izzo', 'Isaiah Wynn', 'Joe Thuney', 'David Andrews',
            'Shaq Mason', 'Michael Onwenu', 'Deatrich Wise Jr.', 'Lawrence Guy', 'Byron Cowart', 'John Simon',
            "Ja'Whaun Bentley", 'Terez Hall', 'Jason McCourty', 'Stephon Gilmore', 'Adrian Phillips', 'Devin McCourty',
            'Jonathan Jones', 'Drew Brees', 'Alvin Kamara', 'Michael Burton', 'Emmanuel Sanders', "Tre'Quan Smith",
            'Jared Cook', 'Terron Armstead ', 'Andrus Peat', 'Erik McCoy', 'Cesar Ruiz', 'Ryan Ramczyk',
            'Cameron Jordan', 'David Onyemata', 'Malcom Brown', 'Trey Hendrickson', 'Kwon Alexander', 'Demario Davis',
            'Janoris Jenkins', 'Marshon Lattimore', 'Malcolm Jenkins', 'Marcus Williams', 'Chauncey Gardner-Johnson',
            'Daniel Jones', 'Wayne Gallman', 'Sterling Shepard', 'Darius Slayton', 'Evan Engram', 'Kaden Smith',
            'Andrew Thomas', 'Shane Lemieux', 'Nick Gates', 'Kevin Zeitler', 'Cameron Fleming', 'Dexter Lawrence',
            'Leonard Williams', 'Dalvin Tomlinson', 'Lorenzo Carter', 'Blake Martinez', 'Tae Crowder', 'Kyler Fackrell',
            'James Bradberry', 'Isaac Yiadom', 'Jabrill Peppers', 'Logan Ryan', 'Sam Darnold', 'Frank Gore',
            'Jamison Crowder', 'Denzel Mims', 'Breshad Perriman', 'Chris Herndon', 'Mekhi Becton', 'Connor McGovern',
            'Greg Van Roten', 'George Fant', 'Henry Anderson', 'Folorunso Fatukasi', 'Quinnen Williams',
            'Tarell Basham', 'Harvey Langi', 'Neville Hewitt', 'Jordan Jenkins', 'Bryce Hall', 'Blessuan Austin',
            'Ashtyn Davis', 'Marcus Maye', 'Carson Wentz', 'Miles Sanders', 'Travis Fulgham', 'Jalen Reagor',
            'Zach Ertz', 'Dallas Goedert', 'Jordan Mailata', 'Isaac Seumalo', 'Jason Kelce', 'Nate Herbig',
            'Lane Johnson', 'Derek Barnett', 'Javon Hargrave', 'Fletcher Cox', 'Brandon Graham', 'Alex Singleton',
            'T.J. Edwards', 'Duke Riley', 'Avonte Maddox', 'Darius Slay', 'Rodney McLeod', 'Jalen Mills',
            'Ben Roethlisberger', 'James Conner', 'Diontae Johnson', 'JuJu Smith-Schuster', 'James Washington',
            'Vance McDonald', 'Alejandro Villanueva', 'Matt Feiler', 'Maurkice Pouncey', 'David DeCastro',
            'Chukwuma Okorafor', 'Stephon Tuitt', 'Cameron Heyward', 'Tyson Alualu', 'T.J. Watt+', 'Robert Spillane',
            'Vince Williams', 'Bud Dupree', 'Joe Haden', 'Steven Nelson', 'Terrell Edmunds', 'Minkah Fitzpatrick+',
            'Nick Mullens', 'Raheem Mostert', 'Kyle Juszczyk', 'Brandon Aiyuk', 'Richie James', 'George Kittle',
            'Trent Williams', 'Laken Tomlinson', 'Ben Garland', 'Daniel Brunskill', 'Mike McGlinchey', 'Arik Armstead',
            'Javon Kinlaw', 'D.J. Jones', 'Kerry Hyder', 'Azeez Al-Shaair', 'Fred Warner+', 'Dre Greenlaw',
            'Jason Verrett', 'Emmanuel Moseley', 'Tarvarius Moore', 'Jimmie Ward', 'Russell Wilson', 'Chris Carson',
            'Tyler Lockett', 'D.K. Metcalf', 'David Moore', 'Greg Olsen', 'Duane Brown', 'Mike Iupati', 'Ethan Pocic',
            'Damien Lewis', 'Brandon Shell', 'L.J. Collier', 'Jarran Reed', 'Poona Ford', 'Benson Mayowa',
            'Bobby Wagner+', 'K.J. Wright', 'Shaquill Griffin', 'D.J. Reed', 'Jamal Adams', 'Quandre Diggs',
            'Ugo Amadi', 'Tom Brady', 'Ronald Jones II', 'Mike Evans', 'Chris Godwin', 'Scott Miller', 'Rob Gronkowski',
            'Donovan Smith', 'Ali Marpet', 'Ryan Jensen', 'Alex Cappa', 'Tristan Wirfs', 'Ndamukong Suh',
            'Rakeem Nunez-Roches', 'William Gholston', 'Jason Pierre-Paul', 'Devin White', 'Lavonte David',
            'Shaquil Barrett', 'Carlton Davis', 'Sean Murphy-Bunting', 'Antoine Winfield Jr.', 'Jordan Whitehead',
            'Ryan Tannehill', 'Derrick Henry +', 'Khari Blasingame', 'A.J. Brown', 'Corey Davis', 'Jonnu Smith',
            'David Quessenberry', 'Rodger Saffold', 'Ben Jones', 'Nate Davis', 'Dennis Kelly', 'Jack Crawford',
            'Jeffery Simmons', 'DaQuan Jones', 'Jadeveon Clowney', 'Rashaan Evans', 'Jayon Brown', 'Harold Landry',
            'Johnathan Joseph', 'Malcolm Butler', 'Kenny Vaccaro', 'Kevin Byard', 'Alex Smith', 'Antonio Gibson',
            'Terry McLaurin', 'Cam Sims', 'Jeremy Sprinkle', 'Logan Thomas', 'Cornelius Lucas', 'Wes Schweitzer',
            'Chase Roullier', 'Brandon Scherff+', 'Morgan Moses', 'Chase Young', 'Daron Payne', 'Jonathan Allen',
            'Montez Sweat', 'Cole Holcomb', 'Jonathan Bostic', 'Kevin Pierre-Louis', 'Kendall Fuller', 'Ronald Darby',
            'Kamren Curl', 'Troy Apke']
data = data[data['Number'] != ' ']
names = data['Name'].tolist()
past = pd.DataFrame()
rows = []
pickable = data[data['Name'].isin(starters)]

@app.route("/",methods = {'GET','POST'})
def hello():
    return redirect("/home", code=302)
@app.route("/home",methods = {'GET','POST'})
def home():
    daily = True
    ip_address = request.remote_addr
    print('IP Adress: ', ip_address)
    pickdailylist = {'03/17/2022': 'Bobby Hart', '03/18/2022': 'Damiere Byrd', '03/19/2022': 'Robert Quinn',
                     '03/20/2022': 'Marquise Brown', '03/21/2022': 'Jack Crawford', '03/22/2022': 'Terry McLaurin',
                     '03/23/2022': 'Josey Jewell', '03/24/2022': 'Lawrence Guy', '03/25/2022': 'Montez Sweat',
                     '03/26/2022': 'Nate Davis', '03/27/2022': 'Denico Autry', '03/28/2022': 'Miles Sanders',
                     '03/29/2022': 'Harrison Smith', '03/30/2022': 'Cameron Heyward', '03/31/2022': 'Myles Gaskin',
                     '04/01/2022': 'Ifeadi Odenigbo', '04/02/2022': 'Yannick Ngakoue', '04/03/2022': 'Clelin Ferrell',
                     '04/04/2022': 'Quinnen Williams', '04/05/2022': 'Ronald Darby', '04/06/2022': 'Jack Crawford',
                     '04/07/2022': 'Calais Campbell', '04/08/2022': 'Justin Pugh', '04/09/2022': 'Adrian Phillips',
                     '04/10/2022': 'Ereck Flowers', '04/11/2022': 'Alejandro Villanueva', '04/12/2022': 'Chris Reed',
                     '04/13/2022': 'Jayron Kearse', '04/14/2022': 'Antonio Gibson', '04/15/2022': 'Austin Blythe',
                     '04/16/2022': 'Sam Tevi', '04/17/2022': 'Brandon Graham', '04/18/2022': 'Whitney Mercilus',
                     '04/19/2022': 'Cam Newton', '04/20/2022': 'Ryan Izzo', '04/21/2022': 'Brandon Linder',
                     '04/22/2022': 'Derek Carr', '04/23/2022': 'Dalton Risner', '04/24/2022': 'Jaylon Johnson',
                     '04/25/2022': 'Stephon Gilmore', '04/26/2022': 'Cameron Jordan', '04/27/2022': 'Harrison Smith',
                     '04/28/2022': 'Cooper Kupp', '04/29/2022': 'Corey Peters', '04/30/2022': 'Cameron Jordan',
                     '05/01/2022': 'Tyson Alualu', '05/02/2022': "Brian O'Neill", '05/03/2022': 'Tyson Alualu',
                     '05/04/2022': 'Joe Haden', '05/05/2022': 'Danny Trevathan', '05/06/2022': 'Jaylon Smith',
                     '05/07/2022': 'Maxx Williams', '05/08/2022': 'Emmanuel Sanders', '05/09/2022': 'Lorenzo Carter',
                     '05/10/2022': 'Derek Barnett', '05/11/2022': 'Shelby Harris', '05/12/2022': 'Sione Takitaki',
                     '05/13/2022': 'Romeo Okwara', '05/14/2022': 'Travis Fulgham', '05/15/2022': 'Foyesade Oluokun',
                     '05/16/2022': 'Jakob Johnson', '05/17/2022': 'Jerry Jeudy', '05/18/2022': 'Eric Kendricks',
                     '05/19/2022': 'Matt Ryan', '05/20/2022': 'Chris Godwin', '05/21/2022': 'Mike Evans',
                     '05/22/2022': 'Calvin Ridley', '05/23/2022': 'Ronald Jones II', '05/24/2022': 'Cameron Dantzler',
                     '05/25/2022': 'Josh Jones', '05/26/2022': 'Jessie Bates III', '05/27/2022': 'Bilal Nichols',
                     '05/28/2022': 'Bravvion Roy', '05/29/2022': 'Mike Remmers', '05/30/2022': 'Maxx Crosby',
                     '05/31/2022': 'Tae Crowder', '06/01/2022': 'Eric Wilson', '06/02/2022': 'Gabe Jackson',
                     '06/03/2022': 'Joe Schobert', '06/04/2022': 'Bryce Callahan', '06/05/2022': 'Logan Thomas',
                     '06/06/2022': 'Josh Allen', '06/07/2022': 'Jason Pierre-Paul', '06/08/2022': 'Javon Kinlaw',
                     '06/09/2022': 'Juan Thornhill', '06/10/2022': 'Raekwon Davis', '06/11/2022': 'Markus Golden',
                     '06/12/2022': 'Patrick Ricard', '06/13/2022': 'Joe Schobert', '06/14/2022': 'Nick Boyle',
                     '06/15/2022': 'George Fant', '06/16/2022': 'Daniel Brunskill', '06/17/2022': 'Lavonte David',
                     '06/18/2022': 'Austin Jackson', '06/19/2022': 'Kwon Alexander', '06/20/2022': 'Brandon Williams',
                     '06/21/2022': 'Matt Ryan', '06/22/2022': 'Jack Doyle', '06/23/2022': 'Bradley Chubb',
                     '06/24/2022': 'Jonathan Jones', '06/25/2022': 'Tremaine Edmunds', '06/26/2022': 'John Penisini',
                     '06/27/2022': 'Josh Reynolds', '06/28/2022': 'Nate Davis', '06/29/2022': 'Dexter Lawrence',
                     '06/30/2022': 'Daron Payne', '07/01/2022': 'Shaquil Barrett', '07/02/2022': 'Kerry Hyder',
                     '07/03/2022': 'Brent Urban', '07/04/2022': 'Alejandro Villanueva', '07/05/2022': 'Greg Van Roten',
                     '07/06/2022': 'Jarvis Landry', '07/07/2022': 'Zach Ertz', '07/08/2022': 'Shane Lemieux',
                     '07/09/2022': 'Andy Dalton', '07/10/2022': 'Tanoh Kpassagnon', '07/11/2022': "N'Keal Harry",
                     '07/12/2022': 'Eric Kendricks', '07/13/2022': "Tre'Davious White", '07/14/2022': 'Bravvion Roy',
                     '07/15/2022': "James O'Shaughnessy", '07/16/2022': 'Giovani Bernard', '07/17/2022': 'Zack Martin',
                     '07/18/2022': 'Jarran Reed', '07/19/2022': 'Xavier Rhodes', '07/20/2022': 'Stephon Tuitt',
                     '07/21/2022': 'Kyle Fuller', '07/22/2022': 'Darren Waller', '07/23/2022': 'Eric Wilson',
                     '07/24/2022': 'Rodney Hudson', '07/25/2022': 'Kelvin Beachum', '07/26/2022': 'Trayvon Mullen',
                     '07/27/2022': 'Mike Williams', '07/28/2022': 'Deion Jones', '07/29/2022': 'Haason Reddick',
                     '07/30/2022': 'Julio Jones', '07/31/2022': 'Corey Peters', '08/01/2022': 'Connor McGovern',
                     '08/02/2022': 'Kevin Zeitler', '08/03/2022': 'Durham Smythe', '08/04/2022': 'Baker Mayfield',
                     '08/05/2022': 'Elgton Jenkins', '08/06/2022': 'Michael Brockers', '08/07/2022': 'Cethan Carter',
                     '08/08/2022': 'Jawaan Taylor', '08/09/2022': 'Kendall Fuller', '08/10/2022': 'Shane Lemieux',
                     '08/11/2022': 'Mike Remmers', '08/12/2022': 'Quinnen Williams', '08/13/2022': 'Tytus Howard',
                     '08/14/2022': 'Carson Wentz', '08/15/2022': 'Jeremy Chinn', '08/16/2022': 'Byron Cowart',
                     '08/17/2022': 'Zach Ertz', '08/18/2022': 'Cam Newton', '08/19/2022': 'Sammy Watkins',
                     '08/20/2022': 'Dan Feeney', '08/21/2022': 'Adam Thielen', '08/22/2022': 'Malcolm Jenkins',
                     '08/23/2022': 'Matt Skura', '08/24/2022': 'Jake Matthews', '08/25/2022': 'Michael Brockers',
                     '08/26/2022': 'Amani Oruwariye', '08/27/2022': 'Lamar Jackson', '08/28/2022': 'Casey Hayward',
                     '08/29/2022': 'Noah Fant', '08/30/2022': 'Amari Cooper', '08/31/2022': 'Alejandro Villanueva',
                     '09/01/2022': 'Zach Allen', '09/02/2022': 'Dalton Risner', '09/03/2022': 'Justin Jones',
                     '09/04/2022': 'DeShon Elliott', '09/05/2022': 'John Brown', '09/06/2022': 'Emmanuel Moseley',
                     '09/07/2022': 'Elgton Jenkins', '09/08/2022': 'Robert Hunt', '09/09/2022': 'Rasul Douglas',
                     '09/10/2022': 'Christian Covington', '09/11/2022': 'Forrest Lamp', '09/12/2022': 'Jared Cook',
                     '09/13/2022': 'Javon Kinlaw', '09/14/2022': 'Matthew Stafford', '09/15/2022': 'Jaylon Johnson',
                     '09/16/2022': 'Malcolm Jenkins', '09/17/2022': 'Zach Ertz', '09/18/2022': 'Duke Riley',
                     '09/19/2022': 'Jordan Jenkins', '09/20/2022': 'Brandon Graham', '09/21/2022': 'Jeffery Simmons',
                     '09/22/2022': 'Daryl Williams', '09/23/2022': 'Nick Gates', '09/24/2022': 'Darius Slay',
                     '09/25/2022': 'Duron Harmon', '09/26/2022': 'Jordan Whitehead', '09/27/2022': 'Stephen Weatherly',
                     '09/28/2022': 'Andrew Norwell', '09/29/2022': 'Shamar Stephen', '09/30/2022': 'Shaq Thompson',
                     '10/01/2022': 'Daniel Jones', '10/02/2022': 'Dan Feeney', '10/03/2022': 'Brandon Graham',
                     '10/04/2022': 'Brandin Cooks', '10/05/2022': 'Danny Shelton', '10/06/2022': 'Kyle Van Noy',
                     '10/07/2022': 'Leonard Floyd', '10/08/2022': 'Romeo Okwara', '10/09/2022': 'Chase Roullier',
                     '10/10/2022': 'Bravvion Roy', '10/11/2022': 'Michael Jordan', '10/12/2022': 'Cameron Jordan',
                     '10/13/2022': 'Ugo Amadi', '10/14/2022': 'Bilal Nichols', '10/15/2022': 'Miles Boykin',
                     '10/16/2022': 'Joel Bitonio', '10/17/2022': 'Dawson Knox', '10/18/2022': 'Hunter Henry',
                     '10/19/2022': 'Andrew Wylie', '10/20/2022': 'David Montgomery', '10/21/2022': 'Stephon Tuitt',
                     '10/22/2022': 'Jerome Baker', '10/23/2022': 'Haason Reddick', '10/24/2022': 'Terrance Mitchell',
                     '10/25/2022': 'Trey Flowers', '10/26/2022': 'Jonnu Smith', '10/27/2022': 'Calvin Ridley',
                     '10/28/2022': 'Jake Matthews', '10/29/2022': 'Rob Gronkowski', '10/30/2022': 'Kareem Jackson',
                     '10/31/2022': 'Stephon Tuitt', '11/01/2022': 'Grover Stewart', '11/02/2022': 'Antonio Gibson',
                     '11/03/2022': 'Kenyan Drake', '11/04/2022': 'Taylor Decker', '11/05/2022': 'Kevin Byard',
                     '11/06/2022': 'Samson Ebukam', '11/07/2022': 'Azeez Al-Shaair', '11/08/2022': 'Garett Bolles',
                     '11/09/2022': 'Jamie Collins', '11/10/2022': 'Diontae Johnson', '11/11/2022': 'Dalvin Cook',
                     '11/12/2022': 'Bradley Roby', '11/13/2022': 'Cory Littleton', '11/14/2022': 'Luke Stocker',
                     '11/15/2022': 'Javon Kinlaw', '11/16/2022': 'Jonathan Taylor', '11/17/2022': 'Jalen Thompson',
                     '11/18/2022': 'Henry Anderson', '11/19/2022': 'Jarran Reed', '11/20/2022': 'Germaine Pratt',
                     '11/21/2022': 'Jonathan Taylor', '11/22/2022': 'Shane Lemieux',
                     '11/23/2022': 'Mackensie Alexander', '11/24/2022': 'Russell Wilson', '11/25/2022': 'Ereck Flowers',
                     '11/26/2022': 'Derek Barnett', '11/27/2022': 'Kyle Juszczyk', '11/28/2022': 'David Montgomery',
                     '11/29/2022': 'Brandon Linder', '11/30/2022': 'Alex Cappa', '12/01/2022': 'Shamar Stephen',
                     '12/02/2022': "Tre'Quan Smith", '12/03/2022': 'Daniel Brunskill', '12/04/2022': 'Zach Ertz',
                     '12/05/2022': 'Ronald Darby', '12/06/2022': 'Forrest Lamp', '12/07/2022': 'David Moore',
                     '12/08/2022': 'Kerry Hyder', '12/09/2022': 'Sean Murphy-Bunting',
                     '12/10/2022': 'DeMarcus Lawrence', '12/11/2022': 'Shaq Thompson', '12/12/2022': 'Benson Mayowa',
                     '12/13/2022': 'Tyeler Davison', '12/14/2022': 'Sam Hubbard', '12/15/2022': 'Adam Gotsis',
                     '12/16/2022': 'Noah Fant', '12/17/2022': 'Graham Glasgow', '12/18/2022': 'Duke Riley',
                     '12/19/2022': 'Tyler Higbee', '12/20/2022': 'Damien Harris', '12/21/2022': 'Bradley Roby',
                     '12/22/2022': "N'Keal Harry", '12/23/2022': 'Trey Flowers', '12/24/2022': 'Daniel Brunskill',
                     '12/25/2022': 'Cole Holcomb', '12/26/2022': 'Tua Tagovailoa', '12/27/2022': 'James Conner',
                     '12/28/2022': 'Brent Urban', '12/29/2022': 'Adrian Amos', '12/30/2022': 'Robert Tonyan',
                     '12/31/2022': 'Mike Daniels', '01/01/2023': 'Tytus Howard', '01/02/2023': 'Denzel Mims',
                     '01/03/2023': 'Jamie Collins', '01/04/2023': 'Kerry Hyder', '01/05/2023': 'Cameron Heyward',
                     '01/06/2023': 'Bradley Chubb', '01/07/2023': 'Kolton Miller', '01/08/2023': 'Rakeem Nunez-Roches',
                     '01/09/2023': 'Taylor Decker', '01/10/2023': 'Denzelle Good', '01/11/2023': 'Erik McCoy',
                     '01/12/2023': 'Nate Davis', '01/13/2023': 'Akiem Hicks', '01/14/2023': 'Steven Nelson',
                     '01/15/2023': 'Carson Wentz', '01/16/2023': 'Sterling Shepard', '01/17/2023': 'Durham Smythe',
                     '01/18/2023': 'Kirk Cousins', '01/19/2023': 'Luke Stocker', '01/20/2023': 'Joe Thuney',
                     '01/21/2023': 'Cethan Carter', '01/22/2023': 'Khari Blasingame', '01/23/2023': 'Garett Bolles',
                     '01/24/2023': 'Connor McGovern', '01/25/2023': 'Chris Herndon', '01/26/2023': 'Justin Jefferson',
                     '01/27/2023': 'Jarrod Wilson', '01/28/2023': 'Marcedes Lewis', '01/29/2023': 'Johnathan Abram',
                     '01/30/2023': 'Mike Daniels', '01/31/2023': 'Ezekiel Elliott', '02/01/2023': 'Nelson Agholor',
                     '02/02/2023': 'Nick Chubb', '02/03/2023': 'Matt Skura', '02/04/2023': 'Cole Holcomb',
                     '02/05/2023': 'Yannick Ngakoue', '02/06/2023': 'Antonio Gibson', '02/07/2023': 'Shane Lemieux',
                     '02/08/2023': 'Terry McLaurin', '02/09/2023': 'David Moore', '02/10/2023': 'Jake Matthews',
                     '02/11/2023': 'Marquez Valdes-Scantling', '02/12/2023': 'Giovani Bernard',
                     '02/13/2023': 'Emmanuel Moseley', '02/14/2023': 'Travis Fulgham', '02/15/2023': 'Nate Davis',
                     '02/16/2023': 'Steven Nelson', '02/17/2023': 'Montez Sweat', '02/18/2023': 'Levi Wallace',
                     '02/19/2023': 'Mekhi Becton', '02/20/2023': 'Jonathan Allen', '02/21/2023': 'Rakeem Nunez-Roches',
                     '02/22/2023': 'Robert Woods', '02/23/2023': 'Terence Steele', '02/24/2023': 'Chris Jones',
                     '02/25/2023': 'Alex Mack', '02/26/2023': 'Gabriel Davis', '02/27/2023': 'Cameron Fleming',
                     '02/28/2023': 'Antonio Gibson', '03/01/2023': 'Leonard Floyd', '03/02/2023': 'Haason Reddick',
                     '03/03/2023': 'Lamar Jackson', '03/04/2023': 'Jordan Hicks', '03/05/2023': 'Shelby Harris',
                     '03/06/2023': 'David Andrews', '03/07/2023': 'Ezekiel Elliott', '03/08/2023': 'Andrew Sendejo',
                     '03/09/2023': 'Travis Fulgham', '03/10/2023': 'Chris Herndon', '03/11/2023': 'Johnathan Hankins'}
    date = datetime.now()
    pickdaily = data[data['Name'] == pickdailylist[date.strftime('%m/%d/%Y')]]
    print(pickdaily)
    names = data['Name'].tolist()
    pickable = data[data['Name'].isin(starters)]
    if not request.cookies.get('rowsdaily'):
        rowsdaily = []
    else:
        rowsdaily= json.loads(request.cookies.get('rowsdaily'))
    if not request.cookies.get('previousDaily'):
        previousDaily = []
    else:
        previousDaily= json.loads(request.cookies.get('previousDaily'))
    if not request.cookies.get('triesdaily'):
        triesdaily = 1
    else:
        triesdaily = int(request.cookies.get('triesdaily'))
    if not request.cookies.get('dailyStatLoss'):
        dailyStatLoss = 0
    else:
        dailyStatLoss = int(request.cookies.get('dailyStatLoss'))
    if not request.cookies.get('dailyStatWin'):
        dailyStatWin = 0
    else:
        dailyStatWin = int(request.cookies.get('dailyStatWin'))


    response = {'Number': '20.0⌃', 'Name': 'zack moss', 'Age': '24⌃','Offense/Defense': 'test', 'Pos': 'rb', 'Weight': '223⌄', 'Confrence': 'NFC',
            'Division': 'afc east', 'Team': ' buffalo bills '}
    invalid = False
    if request.method == 'POST':
        text = request.form['playerName']
        processed_text = text
        guess = processed_text
        row = []
        if guess not in names:
            invalid = True
            print(invalid)
            return render_template('home.html', posts=rowsdaily, result=response, names=names, tries=triesdaily,statLoss=dailyStatLoss,
                                statWin=dailyStatWin, invalid = invalid)
        if guess in previousDaily:
            invalid = True
            print(invalid)
            return render_template('home.html', posts=rowsdaily, result=response, names=names, tries= triesdaily, invalid=invalid, statLoss = dailyStatLoss, statWin = dailyStatWin)
        previousDaily.append(guess)
        print(guess)
        guessRow = data[data['Name'] == str(guess)]

        if int(guessRow.iloc[0]['Number']) == int(pickdaily.iloc[0]['Number']):
            response['Number'] = str(guessRow.iloc[0]['Number'])
            row.append(['Correct',str(guessRow.iloc[0]['Number'])])
        if int(guessRow.iloc[0]['Number']) > int(pickdaily.iloc[0]['Number']):
            response['Number'] = str(str(guessRow.iloc[0]['Number']) + "⌄")
            row.append(['Incorrect',str(str(guessRow.iloc[0]['Number']) + "⌄")])
        if int(guessRow.iloc[0]['Number']) < int(pickdaily.iloc[0]['Number']):
            response['Number'] = str(str(guessRow.iloc[0]['Number']) + "⌃")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Number']) + "⌃")])

        if guessRow.iloc[0]['Name'] == pickdaily.iloc[0]['Name']:
            response['Name'] = guessRow.iloc[0]['Name'].upper()
            row.append(['Correct', guessRow.iloc[0]['Name']])
        else:
            response['Name'] = guessRow.iloc[0]['Name'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Name']])

        if int(guessRow.iloc[0]['Age']) == int(pickdaily.iloc[0]['Age']):
            response['Age'] = str(guessRow.iloc[0]['Age'])
            row.append(['Correct', str(guessRow.iloc[0]['Age'])])
        if int(guessRow.iloc[0]['Age']) > int(pickdaily.iloc[0]['Age']):
            response['Age'] = str(str(guessRow.iloc[0]['Age']) + "⌄")
            row.append(['Incorrect',str(str(guessRow.iloc[0]['Age']) + "⌄")])
        if int(guessRow.iloc[0]['Age']) < int(pickdaily.iloc[0]['Age']):
            response['Age'] = str(str(guessRow.iloc[0]['Age']) + "⌃")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Age']) + "⌃")])
        squad1 = 'error'
        squad2 = "error"
        guesssquad = guessRow.iloc[0]['Pos']
        print(guesssquad)
        offense = ["QB","RB","FB","WR","TE","C","G","OL","OT"]
        if guesssquad in offense:
            squad1 = 'Offense'
            print("test1")
        defense = ["DE","DT","LB","CB","S","OLB","ILB","SS","S","NT","FS"]
        if guesssquad in defense:
            squad1 = "Defense"
            print("test2")
        special= [ "LS","K","P"]
        if guesssquad in special:
            squad1 = "Special"
            print("test3")
        picksquad = pickdaily.iloc[0]['Pos']
        if picksquad in offense:
            squad2 = 'Offense'
        if picksquad in defense:
            squad2 = "Defense"
        if picksquad in special:
            squad2 = "Special"
        if squad1 == squad2:
            response['Offense/Defense'] = squad1.upper()
            row.append(['Correct', squad1])
        else:
            response['Offense/Defense'] = squad1.lower()
            row.append(['Incorrect', squad1])
        print(squad1)
        print(squad2)
        print(row)

        if guessRow.iloc[0]['Pos'] == pickdaily.iloc[0]['Pos']:
            response['Pos'] = guessRow.iloc[0]['Pos'].upper()
            row.append(['Correct', guessRow.iloc[0]['Pos']])
        else:
            response['Pos'] = guessRow.iloc[0]['Pos'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Pos']])

        if int(guessRow.iloc[0]['Weight']) == int(pickdaily.iloc[0]['Weight']):
            response['Weight'] = str(guessRow.iloc[0]['Weight'])
            row.append(['Correct', str(guessRow.iloc[0]['Weight'])])
        if int(guessRow.iloc[0]['Weight']) > int(pickdaily.iloc[0]['Weight']):
            response['Weight'] = str(str(guessRow.iloc[0]['Weight']) + "⌄")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Weight']) + "⌄")])
        if int(guessRow.iloc[0]['Weight']) < int(pickdaily.iloc[0]['Weight']):
            response['Weight'] = str(str(guessRow.iloc[0]['Weight']) + "⌃")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Weight']) + "⌃")])

        guessconf= guessRow.iloc[0]['Division'].split()[0]
        pickconf = pickdaily.iloc[0]['Division'].split()[0]
        if guessconf == pickconf:
            response['Confrence'] = guessconf.upper()
            row.append(['Correct', guessconf])
        else:
            response['Confrence'] = guessconf.lower()
            row.append(['Incorrect', guessconf])

        if guessRow.iloc[0]['Division'] == pickdaily.iloc[0]['Division']:
            response['Division'] = guessRow.iloc[0]['Division'].upper()
            row.append(['Correct', guessRow.iloc[0]['Division']])
        else:
            response['Division'] = guessRow.iloc[0]['Division'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Division']])

        if guessRow.iloc[0]['Team'] == pickdaily.iloc[0]['Team']:
            response['Team'] = guessRow.iloc[0]['Team'].upper()
            row.append(['Correct', guessRow.iloc[0]['Team']])
        else:
            response['Team'] = guessRow.iloc[0]['Team'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Team']])
        rowsdaily.append(row)
        if guessRow.iloc[0]['Name'] == pickdaily.iloc[0]['Name']:
            dailyStatWin += 1
            resp1 = make_response(render_template('winner.html', pick= str(pickdaily.iloc[0]['Name']), statLoss=dailyStatLoss, statWin=dailyStatWin, daily = daily, result= response, posts = rowsdaily))
            resp1.set_cookie('dailyStatWin', str(dailyStatWin))
            previousDaily = []
            resp1.set_cookie('previous', json.dumps(previousDaily))
            return resp1
        elif triesdaily > 7 or len(rows) >8:
            dailyStatLoss += 1
            resp1 = make_response(
                render_template('loser.html', pick=str(pickdaily.iloc[0]['Name']), statLoss=dailyStatLoss,
                                statWin=dailyStatWin, daily=daily, result=response, posts=rowsdaily))
            resp1.set_cookie('dailyStatLoss', str(dailyStatLoss))
            previousDaily = []
            resp1.set_cookie('previous', json.dumps(previousDaily))
            return resp1
        else:
            triesdaily = triesdaily +1

        for row1 in rowsdaily:
            share1= ''
            for row2 in row1:
                if row2[0] == 'Incorrect':
                    share1 += '🟥'
                if row2[0] == 'Correct':
                    share1 += '🟩'
            print(share1)


    resp1 = make_response(render_template('home.html', posts=rowsdaily, result = response, names = names, tries = triesdaily,statLoss=dailyStatLoss,
                                statWin=dailyStatWin, invalid = invalid))
    resp1.set_cookie('rowsdaily', json.dumps(rowsdaily))
    resp1.set_cookie('triesdaily', str(triesdaily))
    resp1.set_cookie('previousDaily', json.dumps(previousDaily))
    return resp1
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/dailyrestart")
def dailyrestart():
    resp1 = make_response("Done")
    resp1.set_cookie('rowsdaily', json.dumps([]))
    resp1.set_cookie('triesdaily', str(1))
    return resp1

@app.route("/test")
def test():
    return render_template('home.html', title='About', names = names, result= response)

@app.route("/unlimited",methods = {'GET','POST'})
def unlimited():
    names = data['Name'].tolist()
    pickable = data[data['Name'].isin(starters)]
    if not request.cookies.get('rows'):
        rows = []
    else:
        rows= json.loads(request.cookies.get('rows'))
    if not request.cookies.get('previous'):
        previous = []
    else:
        previous= json.loads(request.cookies.get('previous'))
    if not request.cookies.get('tries'):
        tries = 1
    else:
        tries = int(request.cookies.get('tries'))
    if not request.cookies.get('pick'):
        pickable = data[data['Name'].isin(starters)]
        pick = pickable.sample()
        print(pick)
    else:
        pick = pd.DataFrame(json.loads(request.cookies.get('pick')))
    if not request.cookies.get('statLoss'):
        statLoss = 0
    else:
        statLoss = int(request.cookies.get('statLoss'))
    if not request.cookies.get('statWin'):
        statWin = 0
    else:
        statWin = int(request.cookies.get('statWin'))



    response = {'Number': '20.0⌃', 'Name': 'zack moss', 'Age': '24⌃',"Offense/Defense": "Offense", 'Pos': 'rb', 'Weight': '223⌄','Confrence':'NFC' ,'Division': 'afc east', 'Team': ' buffalo bills '}
    invalid = False
    if request.method == 'POST':
        try:
            if request.form['submit_button'] == 'Restart':
                pick = pickable.sample()
                tries = 1
                rows = []
                resp1 = make_response(
                    render_template('home.html', posts=rows, result=response, names=names, tries=tries,
                                    invalid=invalid, statLoss = statLoss, statWin = statWin))
                resp1.set_cookie('rows', json.dumps(rows))
                resp1.set_cookie('tries', str(tries))
                resp1.set_cookie('pick', json.dumps(pick.to_dict()))
                return resp1

        except:
            print('Error')
            pass
        text = request.form['playerName']
        processed_text = text
        guess = processed_text
        row = []
        if guess not in names:
            invalid = True
            print(invalid)
            return render_template('home.html', posts=rows, result=response, names=names, tries=tries, invalid = invalid, statLoss = statLoss, statWin = statWin)
        if guess in previous:
            invalid = True
            print(invalid)
            return render_template('home.html', posts=rows, result=response, names=names, tries=tries, invalid=invalid, statLoss = statLoss, statWin = statWin)
        previous.append(guess)
        print(guess)
        guessRow = data[data['Name'] == str(guess)]
        if int(guessRow.iloc[0]['Number']) == int(pick.iloc[0]['Number']):
            response['Number'] = str(guessRow.iloc[0]['Number'])
            row.append(['Correct',str(guessRow.iloc[0]['Number'])])
        if int(guessRow.iloc[0]['Number']) > int(pick.iloc[0]['Number']):
            response['Number'] = str(str(guessRow.iloc[0]['Number']) + "⌄")
            row.append(['Incorrect',str(str(guessRow.iloc[0]['Number']) + "⌄")])
        if int(guessRow.iloc[0]['Number']) < int(pick.iloc[0]['Number']):
            response['Number'] = str(str(guessRow.iloc[0]['Number']) + "⌃")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Number']) + "⌃")])

        if guessRow.iloc[0]['Name'] == pick.iloc[0]['Name']:
            response['Name'] = guessRow.iloc[0]['Name'].upper()
            row.append(['Correct', guessRow.iloc[0]['Name']])
        else:
            response['Name'] = guessRow.iloc[0]['Name'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Name']])

        if int(guessRow.iloc[0]['Age']) == int(pick.iloc[0]['Age']):
            response['Age'] = str(guessRow.iloc[0]['Age'])
            row.append(['Correct', str(guessRow.iloc[0]['Age'])])
        if int(guessRow.iloc[0]['Age']) > int(pick.iloc[0]['Age']):
            response['Age'] = str(str(guessRow.iloc[0]['Age']) + "⌄")
            row.append(['Incorrect',str(str(guessRow.iloc[0]['Age']) + "⌄")])
        if int(guessRow.iloc[0]['Age']) < int(pick.iloc[0]['Age']):
            response['Age'] = str(str(guessRow.iloc[0]['Age']) + "⌃")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Age']) + "⌃")])
        squad1 = 'error'
        squad2 ="error"
        guesssquad = guessRow.iloc[0]['Pos']
        print(guesssquad)
        offense = ["QB", "RB", "FB", "WR", "TE", "C", "G", "OL", "OT"]
        if guesssquad in offense:
            squad1 = 'Offense'
            print("test1")
        defense = ["DE", "DT", "LB", "CB", "S", "OLB", "ILB", "SS", "S", "NT","FS"]
        if guesssquad in defense:
            squad1 = "Defense"
            print("test2")
        special = ["LS", "K", "P"]
        if guesssquad in special:
            squad1 = "Special"
            print("test3")
        picksquad = pick.iloc[0]['Pos']
        print(picksquad)
        if picksquad in offense:
            squad2 = 'Offense'
        if picksquad in defense:
            squad2 = "Defense"
        if picksquad in special:
            squad2 = "Special"
        if squad1 == squad2:
            response['Offense/Defense'] = squad1.upper()
            row.append(['Correct', squad1])
        else:
            response['Offense/Defense'] = squad1.lower()
            row.append(['Incorrect', squad1])
        print(squad2)
        if guessRow.iloc[0]['Pos'] == pick.iloc[0]['Pos']:
            response['Pos'] = guessRow.iloc[0]['Pos'].upper()
            row.append(['Correct', guessRow.iloc[0]['Pos']])
        else:
            response['Pos'] = guessRow.iloc[0]['Pos'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Pos']])

        if int(guessRow.iloc[0]['Weight']) == int(pick.iloc[0]['Weight']):
            response['Weight'] = str(guessRow.iloc[0]['Weight'])
            row.append(['Correct', str(guessRow.iloc[0]['Weight'])])
        if int(guessRow.iloc[0]['Weight']) > int(pick.iloc[0]['Weight']):
            response['Weight'] = str(str(guessRow.iloc[0]['Weight']) + "⌄")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Weight']) + "⌄")])
        if int(guessRow.iloc[0]['Weight']) < int(pick.iloc[0]['Weight']):
            response['Weight'] = str(str(guessRow.iloc[0]['Weight']) + "⌃")
            row.append(['Incorrect', str(str(guessRow.iloc[0]['Weight']) + "⌃")])

        guessconf= guessRow.iloc[0]['Division'].split()[0]
        pickconf = pick.iloc[0]['Division'].split()[0]
        if guessconf == pickconf:
            response['Confrence'] = guessconf.upper()
            row.append(['Correct', guessconf])
        else:
            response['Confrence'] = guessconf.lower()
            row.append(['Incorrect', guessconf])



        if guessRow.iloc[0]['Division'] == pick.iloc[0]['Division']:
            response['Division'] = guessRow.iloc[0]['Division'].upper()
            row.append(['Correct', guessRow.iloc[0]['Division']])
        else:
            response['Division'] = guessRow.iloc[0]['Division'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Division']])

        if guessRow.iloc[0]['Team'] == pick.iloc[0]['Team']:
            response['Team'] = guessRow.iloc[0]['Team'].upper()
            row.append(['Correct', guessRow.iloc[0]['Team']])
        else:
            response['Team'] = guessRow.iloc[0]['Team'].lower()
            row.append(['Incorrect', guessRow.iloc[0]['Team']])
        rows.append(row)
        if guessRow.iloc[0]['Name'] == pick.iloc[0]['Name']:
            statWin += 1
            resp1 = make_response(render_template('winner.html', pick = str(pick.iloc[0]['Name']), statLoss = statLoss, statWin = statWin))
            previous = []
            resp1.set_cookie('previous', json.dumps(previous))
            resp1.set_cookie('statWin', str(statWin))
            return resp1
        elif tries > 7 or len(rows) >8:
            statLoss += 1
            resp1 = make_response(render_template('loser.html', pick = str(pick.iloc[0]['Name']),result = response, posts = rows, statLoss = statLoss, statWin = statWin))
            previous = []
            resp1.set_cookie('previous', json.dumps(previous))
            resp1.set_cookie('statLoss', str(statLoss))
            return resp1
        else:
            tries = tries +1

    print(response)
    resp1 = make_response(render_template('home.html', posts=rows, result = response, names = names, tries = tries, invalid = invalid, statLoss = statLoss, statWin = statWin))
    resp1.set_cookie('rows', json.dumps(rows))
    resp1.set_cookie('tries', str(tries))
    resp1.set_cookie('previous', json.dumps(previous))
    resp1.set_cookie('pick', json.dumps(pick.to_dict()))
    return resp1



if __name__ == '__main__':
    starters = ['Kyler Murray', 'Kenyan Drake', 'Larry Fitzgerald', 'DeAndre Hopkins', 'Christian Kirk', 'Maxx Williams', 'D.J. Humphries', 'Justin Pugh', 'Mason Cole', 'J.R. Sweezy', 'Kelvin Beachum', 'Zach Allen', 'Corey Peters', 'Jordan Phillips', 'Haason Reddick', "De'Vondre Campbell", 'Jordan Hicks', 'Markus Golden', 'Patrick Peterson', 'Dre Kirkpatrick', 'Budda Baker+', 'Jalen Thompson', 'Matt Ryan', 'Todd Gurley', 'Keith Smith', 'Julio Jones', 'Calvin Ridley', 'Luke Stocker', 'Jake Matthews', 'James Carpenter', 'Alex Mack', 'Chris Lindstrom', 'Kaleb McGary', 'Steven Means', 'Grady Jarrett', 'Tyeler Davison', 'Dante Fowler', 'Deion Jones', 'Foyesade Oluokun', 'Mykal Walker', 'AJ Terrell', 'Isaiah Oliver', 'Ricardo Allen', 'Keanu Neal', 'Lamar Jackson', 'Mark Ingram', 'Patrick Ricard', 'Miles Boykin', 'Marquise Brown', 'Nick Boyle', 'Orlando Brown Jr.', 'Bradley Bozeman', 'Matt Skura', 'Ben Powers', 'D.J. Fluker', 'Calais Campbell', 'Brandon Williams', 'Derek Wolfe', 'Pernell McPhee', 'Patrick Queen', 'L.J. Fort', 'Matt Judon', 'Marlon Humphrey', 'Marcus Peters', 'Chuck Clark', 'DeShon Elliott', 'Josh Allen', 'Devin Singletary', 'John Brown', 'Gabriel Davis', 'Stefon Diggs+', 'Dawson Knox', 'Dion Dawkins', 'Ike Boettger', 'Mitch Morse', 'Brian Winters', 'Daryl Williams', 'Jerry Hughes', 'Vernon Butler', 'Ed Oliver', 'Mario Addison', 'A.J. Klein', 'Tremaine Edmunds', "Tre'Davious White", 'Levi Wallace', 'Jordan Poyer', 'Micah Hyde', 'Taron Johnson', 'Teddy Bridgewater', 'Mike Davis', 'Robby Anderson', 'D.J. Moore', 'Curtis Samuel', 'Chris Manhertz', 'Russell Okung', 'Chris Reed', 'Matt Paradis', 'John Miller', 'Taylor Moton', 'Brian Burns', 'Bravvion Roy', 'Derrick Brown', 'Stephen Weatherly', 'Shaq Thompson', 'Tahir Whitehead', 'Jeremy Chinn', 'Donte Jackson', 'Rasul Douglas', 'Juston Burris', 'Tre Boston', 'Mitchell Trubisky', 'David Montgomery', 'Anthony Miller', 'Allen Robinson', 'Jimmy Graham', 'Cole Kmet', 'Charles Leno Jr.', 'James Daniels', 'Cody Whitehair', 'Germain Ifedi', 'Bobby Massie', 'Akiem Hicks', 'Brent Urban', 'Bilal Nichols', 'Khalil Mack', 'Roquan Smith', 'Danny Trevathan', 'Robert Quinn', 'Kyle Fuller', 'Jaylon Johnson', 'Tashaun Gipson', 'Eddie Jackson', 'Joe Burrow', 'Giovani Bernard', 'A.J. Green', 'Tee Higgins', 'Cethan Carter', 'Drew Sample', 'Jonah Williams', 'Michael Jordan', 'Trey Hopkins', 'Alex Redmond', 'Bobby Hart', 'Sam Hubbard', 'Mike Daniels', 'Christian Covington', 'Carl Lawson', 'Josh Bynes', 'Germaine Pratt', 'Darius Phillips', 'Mackensie Alexander', 'William Jackson III', 'Vonn Bell', 'Jessie Bates III', 'Baker Mayfield', 'Nick Chubb', 'Odell Beckham Jr.', 'Jarvis Landry', 'Harrison Bryant', 'Austin Hooper', 'Jedrick Wills Jr.', 'Joel Bitonio', 'J.C. Tretter', 'Wyatt Teller', 'Jack Conklin+', 'Myles Garrett+', 'Sheldon Richardson', 'Larry Ogunjobi', 'Olivier Vernon', 'Mack Wilson', 'B.J. Goodson', 'Sione Takitaki', 'Denzel Ward', 'Terrance Mitchell', 'Karl Joseph', 'Andrew Sendejo', 'Andy Dalton', 'Ezekiel Elliott', 'Amari Cooper', 'Michael Gallup', 'CeeDee Lamb', 'Dalton Schultz', 'Brandon Knight', 'Connor Williams', 'Joe Looney', 'Zack Martin', 'Terence Steele', 'DeMarcus Lawrence', 'Antwaun Woods', 'Neville Gallimore', 'Aldon Smith', 'Leighton Vander Esch', 'Jaylon Smith', 'Anthony Brown', 'Trevon Diggs', 'Donovan Wilson', 'Xavier Woods', 'Jourdan Lewis', 'Drew Lock', 'Melvin Gordon', 'Jerry Jeudy', 'Tim Patrick', 'Noah Fant', 'Nick Vannett', 'Garett Bolles', 'Dalton Risner', 'Lloyd Cushenberry III', 'Graham Glasgow', 'Demar Dotson', 'Shelby Harris', 'DeShawn Williams', "Dre'Mont Jones", 'Malik Reed', 'Alexander Johnson', 'Josey Jewell', 'Bradley Chubb', 'A.J. Bouye', 'Bryce Callahan', 'Kareem Jackson', 'Justin Simmons', 'Matthew Stafford', 'Adrian Peterson', 'Kenny Golladay', 'Marvin Jones', 'T.J. Hockenson', 'Jesse James', 'Taylor Decker', 'Jonah Jackson', 'Frank Ragnow', 'Oday Aboushi', 'Tyrell Crosby', 'Trey Flowers', 'Danny Shelton', 'John Penisini', 'Romeo Okwara', 'Christian Jones', 'Jahlani Tavai', 'Jamie Collins', 'Desmond Trufant', 'Amani Oruwariye', 'Jayron Kearse', 'Duron Harmon', 'Aaron Rodgers+', 'Aaron Jones', 'Davante Adams+', 'Marquez Valdes-Scantling', 'Marcedes Lewis', 'Robert Tonyan', 'David Bakhtiari+', 'Elgton Jenkins', 'Corey Linsley+', 'Lucas Patrick', 'Billy Turner', 'Dean Lowry', 'Kenny Clark', 'Kingsley Keke', 'Preston Smith', 'Christian Kirksey', 'Krys Barnes', "Za'Darius Smith", 'Jaire Alexander', 'Kevin King', 'Adrian Amos', 'Darnell Savage Jr.', 'Deshaun Watson', 'David Johnson', 'Brandin Cooks', 'Will Fuller', 'Pharaoh Brown', 'Darren Fells', 'Laremy Tunsil', 'Max Scharping', 'Nick Martin', 'Zach Fulton', 'Tytus Howard', 'J.J. Watt', 'Brandon Dunn', 'P.J. Hall', 'Whitney Mercilus', 'Zach Cunningham', 'Tyrell Adams', 'Brennan Scarlett', 'Bradley Roby', 'Vernon Hargreaves III', 'Justin Reid', 'Eric Murray', 'Philip Rivers', 'Jonathan Taylor', 'T.Y. Hilton', 'Zach Pascal', 'Michael Pittman Jr.', 'Jack Doyle', 'Anthony Castonzo', 'Quenton Nelson+', 'Ryan Kelly', 'Mark Glowinski', 'Braden Smith', 'Justin Houston', 'DeForest Buckner+', 'Grover Stewart', 'Denico Autry', 'Darius Leonard+', 'Anthony Walker', 'Bobby Okereke', 'Kenny Moore', 'Xavier Rhodes', 'Khari Willis', 'Julian Blackmon', 'Gardner Minshew II', 'James Robinson', 'Bruce Miller', 'DJ Chark', 'Laviska Shenault Jr.', "James O'Shaughnessy", 'Cam Robinson', 'Andrew Norwell', 'Brandon Linder', 'A.J. Cann', 'Jawaan Taylor', 'Josh Allen', 'Taven Bryan', 'Doug Costin', 'Adam Gotsis', 'Myles Jack', 'Joe Schobert', 'Kamalei Correa', 'C.J. Henderson', 'Sidney Jones', 'Josh Jones', 'Jarrod Wilson', 'Patrick Mahomes', 'Clyde Edwards-Helaire', 'Tyreek Hill+', 'Demarcus Robinson', 'Sammy Watkins', 'Travis Kelce+', 'Eric Fisher', 'Nick Allegretti', 'Austin Reiter', 'Andrew Wylie', 'Mike Remmers', 'Tanoh Kpassagnon', 'Chris Jones', 'Derrick Nnadi', 'Frank Clark', 'Anthony Hitchens', 'Damien Wilson', 'Willie Gay Jr.', 'Charvarius Ward', 'Bashaud Breeland', 'Tyrann Mathieu+', 'Juan Thornhill', 'Derek Carr', 'Josh Jacobs', 'Nelson Agholor', 'Henry Ruggs III', 'Darren Waller', 'Jason Witten', 'Kolton Miller', 'Denzelle Good', 'Rodney Hudson', 'Gabe Jackson', 'Sam Young', 'Clelin Ferrell', 'Johnathan Hankins', 'Maliek Collins', 'Maxx Crosby', 'Nicholas Morrow', 'Nick Kwiatkoski', 'Cory Littleton', 'Trayvon Mullen', 'Nevin Lawson', 'Johnathan Abram', 'Erik Harris', 'Justin Herbert', 'Austin Ekeler', 'Keenan Allen', 'Jalen Guyton', 'Mike Williams', 'Hunter Henry', 'Sam Tevi', 'Forrest Lamp', 'Dan Feeney', 'Trai Turner', 'Bryan Bulaga', 'Joey Bosa', 'Justin Jones', 'Linval Joseph', 'Melvin Ingram', 'Kyzir White', 'Kenneth Murray', 'Michael Davis', 'Casey Hayward', 'Rayshawn Jenkins', 'Nasir Adderley', 'Chris Harris Jr.', 'Jared Goff', 'Darrell Henderson', 'Cooper Kupp', 'Josh Reynolds', 'Robert Woods', 'Tyler Higbee', 'Andrew Whitworth', 'David Edwards', 'Austin Blythe', 'Austin Corbett', 'Rob Havenstein', 'Michael Brockers', 'Aaron Donald+', 'Sebastian Joseph-Day', 'Samson Ebukam', 'Troy Reeder', 'Kenny Young', 'Leonard Floyd', 'Troy Hill', 'Jalen Ramsey+', 'Jordan Fuller', 'John Johnson', 'Tua Tagovailoa', 'Myles Gaskin', 'DeVante Parker', 'Preston Williams', 'Mike Gesicki', 'Durham Smythe', 'Austin Jackson', 'Ereck Flowers', 'Ted Karras', 'Solomon Kindley', 'Robert Hunt', 'Christian Wilkins', 'Raekwon Davis', 'Emmanuel Ogbah', 'Andrew Van Ginkel', 'Elandon Roberts', 'Jerome Baker', 'Kyle Van Noy', 'Byron Jones', 'Xavien Howard+', 'Bobby McCain', 'Eric Rowe', 'Kirk Cousins', 'Dalvin Cook', 'C.J. Ham', 'Justin Jefferson', 'Adam Thielen', 'Kyle Rudolph', 'Riley Reiff', 'Dakota Dozier', 'Garrett Bradbury', 'Ezra Cleveland', "Brian O'Neill", 'Yannick Ngakoue', 'Ifeadi Odenigbo', 'Shamar Stephen', 'Jaleel Johnson', 'Troy Dye', 'Eric Kendricks', 'Eric Wilson', 'Cameron Dantzler', 'Jeff Gladney', 'Harrison Smith', 'Anthony Harris', 'Cam Newton', 'Damien Harris', 'Jakob Johnson', 'Damiere Byrd', "N'Keal Harry", 'Ryan Izzo', 'Isaiah Wynn', 'Joe Thuney', 'David Andrews', 'Shaq Mason', 'Michael Onwenu', 'Deatrich Wise Jr.', 'Lawrence Guy', 'Byron Cowart', 'John Simon', "Ja'Whaun Bentley", 'Terez Hall', 'Jason McCourty', 'Stephon Gilmore', 'Adrian Phillips', 'Devin McCourty', 'Jonathan Jones', 'Drew Brees', 'Alvin Kamara', 'Michael Burton', 'Emmanuel Sanders', "Tre'Quan Smith", 'Jared Cook', 'Terron Armstead ', 'Andrus Peat', 'Erik McCoy', 'Cesar Ruiz', 'Ryan Ramczyk', 'Cameron Jordan', 'David Onyemata', 'Malcom Brown', 'Trey Hendrickson', 'Kwon Alexander', 'Demario Davis', 'Janoris Jenkins', 'Marshon Lattimore', 'Malcolm Jenkins', 'Marcus Williams', 'Chauncey Gardner-Johnson', 'Daniel Jones', 'Wayne Gallman', 'Sterling Shepard', 'Darius Slayton', 'Evan Engram', 'Kaden Smith', 'Andrew Thomas', 'Shane Lemieux', 'Nick Gates', 'Kevin Zeitler', 'Cameron Fleming', 'Dexter Lawrence', 'Leonard Williams', 'Dalvin Tomlinson', 'Lorenzo Carter', 'Blake Martinez', 'Tae Crowder', 'Kyler Fackrell', 'James Bradberry', 'Isaac Yiadom', 'Jabrill Peppers', 'Logan Ryan', 'Sam Darnold', 'Frank Gore', 'Jamison Crowder', 'Denzel Mims', 'Breshad Perriman', 'Chris Herndon', 'Mekhi Becton', 'Connor McGovern', 'Greg Van Roten', 'George Fant', 'Henry Anderson', 'Folorunso Fatukasi', 'Quinnen Williams', 'Tarell Basham', 'Harvey Langi', 'Neville Hewitt', 'Jordan Jenkins', 'Bryce Hall', 'Blessuan Austin', 'Ashtyn Davis', 'Marcus Maye', 'Carson Wentz', 'Miles Sanders', 'Travis Fulgham', 'Jalen Reagor', 'Zach Ertz', 'Dallas Goedert', 'Jordan Mailata', 'Isaac Seumalo', 'Jason Kelce', 'Nate Herbig', 'Lane Johnson', 'Derek Barnett', 'Javon Hargrave', 'Fletcher Cox', 'Brandon Graham', 'Alex Singleton', 'T.J. Edwards', 'Duke Riley', 'Avonte Maddox', 'Darius Slay', 'Rodney McLeod', 'Jalen Mills', 'Ben Roethlisberger', 'James Conner', 'Diontae Johnson', 'JuJu Smith-Schuster', 'James Washington', 'Vance McDonald', 'Alejandro Villanueva', 'Matt Feiler', 'Maurkice Pouncey', 'David DeCastro', 'Chukwuma Okorafor', 'Stephon Tuitt', 'Cameron Heyward', 'Tyson Alualu', 'T.J. Watt+', 'Robert Spillane', 'Vince Williams', 'Bud Dupree', 'Joe Haden', 'Steven Nelson', 'Terrell Edmunds', 'Minkah Fitzpatrick+', 'Nick Mullens', 'Raheem Mostert', 'Kyle Juszczyk', 'Brandon Aiyuk', 'Richie James', 'George Kittle', 'Trent Williams', 'Laken Tomlinson', 'Ben Garland', 'Daniel Brunskill', 'Mike McGlinchey', 'Arik Armstead', 'Javon Kinlaw', 'D.J. Jones', 'Kerry Hyder', 'Azeez Al-Shaair', 'Fred Warner+', 'Dre Greenlaw', 'Jason Verrett', 'Emmanuel Moseley', 'Tarvarius Moore', 'Jimmie Ward', 'Russell Wilson', 'Chris Carson', 'Tyler Lockett', 'D.K. Metcalf', 'David Moore', 'Greg Olsen', 'Duane Brown', 'Mike Iupati', 'Ethan Pocic', 'Damien Lewis', 'Brandon Shell', 'L.J. Collier', 'Jarran Reed', 'Poona Ford', 'Benson Mayowa', 'Bobby Wagner+', 'K.J. Wright', 'Shaquill Griffin', 'D.J. Reed', 'Jamal Adams', 'Quandre Diggs', 'Ugo Amadi', 'Tom Brady', 'Ronald Jones II', 'Mike Evans', 'Chris Godwin', 'Scott Miller', 'Rob Gronkowski', 'Donovan Smith', 'Ali Marpet', 'Ryan Jensen', 'Alex Cappa', 'Tristan Wirfs', 'Ndamukong Suh', 'Rakeem Nunez-Roches', 'William Gholston', 'Jason Pierre-Paul', 'Devin White', 'Lavonte David', 'Shaquil Barrett', 'Carlton Davis', 'Sean Murphy-Bunting', 'Antoine Winfield Jr.', 'Jordan Whitehead', 'Ryan Tannehill', 'Derrick Henry +', 'Khari Blasingame', 'A.J. Brown', 'Corey Davis', 'Jonnu Smith', 'David Quessenberry', 'Rodger Saffold', 'Ben Jones', 'Nate Davis', 'Dennis Kelly', 'Jack Crawford', 'Jeffery Simmons', 'DaQuan Jones', 'Jadeveon Clowney', 'Rashaan Evans', 'Jayon Brown', 'Harold Landry', 'Johnathan Joseph', 'Malcolm Butler', 'Kenny Vaccaro', 'Kevin Byard', 'Alex Smith', 'Antonio Gibson', 'Terry McLaurin', 'Cam Sims', 'Jeremy Sprinkle', 'Logan Thomas', 'Cornelius Lucas', 'Wes Schweitzer', 'Chase Roullier', 'Brandon Scherff+', 'Morgan Moses', 'Chase Young', 'Daron Payne', 'Jonathan Allen', 'Montez Sweat', 'Cole Holcomb', 'Jonathan Bostic', 'Kevin Pierre-Louis', 'Kendall Fuller', 'Ronald Darby', 'Kamren Curl', 'Troy Apke']
    names = data['Name'].tolist()
    pickable = data[data['Name'].isin(starters)]
    pick = pickable.sample()
    past = pd.DataFrame()
    app.run(host='0.0.0.0', debug=True)
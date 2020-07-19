from cs50 import SQL
db = SQL('sqlite:///faces.db')

query = db.execute("SELECT * FROM settings ORDER BY id")
for i in range(len(query)):
    exec(query[i]['name'] + " = query[i]['value']")



#--------------------------------

def db_settings_add(key, value):
    db.execute("INSERT INTO settings (name, value) VALUES(?, ?)", key, value)
    exec(key + " = " + value) 

def dbadd(face_encodings, faces_person_id, faces_image_loc):
    for i in range(len(face_encodings)):
        db.execute("INSERT INTO encoding (person_id, image_loc, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", faces_person_id[i], faces_image_loc[i],\
            face_encodings[i][0].item(),\
            face_encodings[i][1].item(),\
            face_encodings[i][2].item(),\
            face_encodings[i][3].item(),\
            face_encodings[i][4].item(),\
            face_encodings[i][5].item(),\
            face_encodings[i][6].item(),\
            face_encodings[i][7].item(),\
            face_encodings[i][8].item(),\
            face_encodings[i][9].item(),\
            face_encodings[i][10].item(),\
            face_encodings[i][11].item(),\
            face_encodings[i][12].item(),\
            face_encodings[i][13].item(),\
            face_encodings[i][14].item(),\
            face_encodings[i][15].item(),\
            face_encodings[i][16].item(),\
            face_encodings[i][17].item(),\
            face_encodings[i][18].item(),\
            face_encodings[i][19].item(),\
            face_encodings[i][20].item(),\
            face_encodings[i][21].item(),\
            face_encodings[i][22].item(),\
            face_encodings[i][23].item(),\
            face_encodings[i][24].item(),\
            face_encodings[i][25].item(),\
            face_encodings[i][26].item(),\
            face_encodings[i][27].item(),\
            face_encodings[i][28].item(),\
            face_encodings[i][29].item(),\
            face_encodings[i][30].item(),\
            face_encodings[i][31].item(),\
            face_encodings[i][32].item(),\
            face_encodings[i][33].item(),\
            face_encodings[i][34].item(),\
            face_encodings[i][35].item(),\
            face_encodings[i][36].item(),\
            face_encodings[i][37].item(),\
            face_encodings[i][38].item(),\
            face_encodings[i][39].item(),\
            face_encodings[i][40].item(),\
            face_encodings[i][41].item(),\
            face_encodings[i][42].item(),\
            face_encodings[i][43].item(),\
            face_encodings[i][44].item(),\
            face_encodings[i][45].item(),\
            face_encodings[i][46].item(),\
            face_encodings[i][47].item(),\
            face_encodings[i][48].item(),\
            face_encodings[i][49].item(),\
            face_encodings[i][50].item(),\
            face_encodings[i][51].item(),\
            face_encodings[i][52].item(),\
            face_encodings[i][53].item(),\
            face_encodings[i][54].item(),\
            face_encodings[i][55].item(),\
            face_encodings[i][56].item(),\
            face_encodings[i][57].item(),\
            face_encodings[i][58].item(),\
            face_encodings[i][59].item(),\
            face_encodings[i][60].item(),\
            face_encodings[i][61].item(),\
            face_encodings[i][62].item(),\
            face_encodings[i][63].item(),\
            face_encodings[i][64].item(),\
            face_encodings[i][65].item(),\
            face_encodings[i][66].item(),\
            face_encodings[i][67].item(),\
            face_encodings[i][68].item(),\
            face_encodings[i][69].item(),\
            face_encodings[i][70].item(),\
            face_encodings[i][71].item(),\
            face_encodings[i][72].item(),\
            face_encodings[i][73].item(),\
            face_encodings[i][74].item(),\
            face_encodings[i][75].item(),\
            face_encodings[i][76].item(),\
            face_encodings[i][77].item(),\
            face_encodings[i][78].item(),\
            face_encodings[i][79].item(),\
            face_encodings[i][80].item(),\
            face_encodings[i][81].item(),\
            face_encodings[i][82].item(),\
            face_encodings[i][83].item(),\
            face_encodings[i][84].item(),\
            face_encodings[i][85].item(),\
            face_encodings[i][86].item(),\
            face_encodings[i][87].item(),\
            face_encodings[i][88].item(),\
            face_encodings[i][89].item(),\
            face_encodings[i][90].item(),\
            face_encodings[i][91].item(),\
            face_encodings[i][92].item(),\
            face_encodings[i][93].item(),\
            face_encodings[i][94].item(),\
            face_encodings[i][95].item(),\
            face_encodings[i][96].item(),\
            face_encodings[i][97].item(),\
            face_encodings[i][98].item(),\
            face_encodings[i][99].item(),\
            face_encodings[i][100].item(),\
            face_encodings[i][101].item(),\
            face_encodings[i][102].item(),\
            face_encodings[i][103].item(),\
            face_encodings[i][104].item(),\
            face_encodings[i][105].item(),\
            face_encodings[i][106].item(),\
            face_encodings[i][107].item(),\
            face_encodings[i][108].item(),\
            face_encodings[i][109].item(),\
            face_encodings[i][110].item(),\
            face_encodings[i][111].item(),\
            face_encodings[i][112].item(),\
            face_encodings[i][113].item(),\
            face_encodings[i][114].item(),\
            face_encodings[i][115].item(),\
            face_encodings[i][116].item(),\
            face_encodings[i][117].item(),\
            face_encodings[i][118].item(),\
            face_encodings[i][119].item(),\
            face_encodings[i][120].item(),\
            face_encodings[i][121].item(),\
            face_encodings[i][122].item(),\
            face_encodings[i][123].item(),\
            face_encodings[i][124].item(),\
            face_encodings[i][125].item(),\
            face_encodings[i][126].item(),\
            face_encodings[i][127].item())
    
def dbget():
    saved_encodings = []
    saved_names = []
    saved_announce = []
    query = db.execute("SELECT * FROM faces LEFT JOIN people ON faces.person_id = people.id LEFT JOIN log ON log.person_id = people.id ORDER BY name ASC")
    for i in range(len(query)):
        saved_names.append(query[i]['name'])
        saved_encodings.append([])
        # Loop from 0 to 127 (128 iterations in total)
        for j in range(128):
            saved_encodings[i].append(query[i][str(j)])
        saved_trusted.append(query[i]['trusted'])
        saved_announce.append(query[i]['announce'])
    return saved_encodings, saved_names, saved_trusted, saved_announce

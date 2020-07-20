from cs50 import SQL
db = SQL('sqlite:///faces.db')

query = db.execute("SELECT * FROM settings ORDER BY id")
for i in range(len(query)):
    exec(query[i]['name'] + " = query[i]['value']")

def dbget():
    ids = []
    names = []
    trusted = []
    announce = []
    encodings = []
    query = db.execute("select * from people join faces on people.id = faces.person_id ORDER BY name")

    for i in range(len(query)):
        ids.append(query[i]['person_id'])
        names.append(query[i]['name'])
        trusted.append(query[i]['trusted'])
        announce.append(query[i]['announce'])
        encodings.append([])
        # Loop from 0 to 127 (128 iterations in total)
        for j in range(128):
            encodings[i].append(query[i][str(j)])
    return ids, names, trusted, announce, encodings

#--------------------------------

def db_settings_add(key, value):
    db.execute("INSERT INTO settings (name, value) VALUES(?, ?)", key, value)
    exec(key + " = " + value) 

def db_person_add(name):
    newid = db.execute("SELECT max(id) AS max FROM people")[0]['max'] + 1
    db.execute("INSERT INTO people VALUES(?, ?, 'False', ?)",newid, name, default_announce)
    return newid

def db_face_add(person_id, image_loc, face_encodings):
    db.execute("INSERT INTO faces (person_id, image_loc, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", person_id, image_loc,\
        face_encodings[0].item(),\
        face_encodings[1].item(),\
        face_encodings[2].item(),\
        face_encodings[3].item(),\
        face_encodings[4].item(),\
        face_encodings[5].item(),\
        face_encodings[6].item(),\
        face_encodings[7].item(),\
        face_encodings[8].item(),\
        face_encodings[9].item(),\
        face_encodings[10].item(),\
        face_encodings[11].item(),\
        face_encodings[12].item(),\
        face_encodings[13].item(),\
        face_encodings[14].item(),\
        face_encodings[15].item(),\
        face_encodings[16].item(),\
        face_encodings[17].item(),\
        face_encodings[18].item(),\
        face_encodings[19].item(),\
        face_encodings[20].item(),\
        face_encodings[21].item(),\
        face_encodings[22].item(),\
        face_encodings[23].item(),\
        face_encodings[24].item(),\
        face_encodings[25].item(),\
        face_encodings[26].item(),\
        face_encodings[27].item(),\
        face_encodings[28].item(),\
        face_encodings[29].item(),\
        face_encodings[30].item(),\
        face_encodings[31].item(),\
        face_encodings[32].item(),\
        face_encodings[33].item(),\
        face_encodings[34].item(),\
        face_encodings[35].item(),\
        face_encodings[36].item(),\
        face_encodings[37].item(),\
        face_encodings[38].item(),\
        face_encodings[39].item(),\
        face_encodings[40].item(),\
        face_encodings[41].item(),\
        face_encodings[42].item(),\
        face_encodings[43].item(),\
        face_encodings[44].item(),\
        face_encodings[45].item(),\
        face_encodings[46].item(),\
        face_encodings[47].item(),\
        face_encodings[48].item(),\
        face_encodings[49].item(),\
        face_encodings[50].item(),\
        face_encodings[51].item(),\
        face_encodings[52].item(),\
        face_encodings[53].item(),\
        face_encodings[54].item(),\
        face_encodings[55].item(),\
        face_encodings[56].item(),\
        face_encodings[57].item(),\
        face_encodings[58].item(),\
        face_encodings[59].item(),\
        face_encodings[60].item(),\
        face_encodings[61].item(),\
        face_encodings[62].item(),\
        face_encodings[63].item(),\
        face_encodings[64].item(),\
        face_encodings[65].item(),\
        face_encodings[66].item(),\
        face_encodings[67].item(),\
        face_encodings[68].item(),\
        face_encodings[69].item(),\
        face_encodings[70].item(),\
        face_encodings[71].item(),\
        face_encodings[72].item(),\
        face_encodings[73].item(),\
        face_encodings[74].item(),\
        face_encodings[75].item(),\
        face_encodings[76].item(),\
        face_encodings[77].item(),\
        face_encodings[78].item(),\
        face_encodings[79].item(),\
        face_encodings[80].item(),\
        face_encodings[81].item(),\
        face_encodings[82].item(),\
        face_encodings[83].item(),\
        face_encodings[84].item(),\
        face_encodings[85].item(),\
        face_encodings[86].item(),\
        face_encodings[87].item(),\
        face_encodings[88].item(),\
        face_encodings[89].item(),\
        face_encodings[90].item(),\
        face_encodings[91].item(),\
        face_encodings[92].item(),\
        face_encodings[93].item(),\
        face_encodings[94].item(),\
        face_encodings[95].item(),\
        face_encodings[96].item(),\
        face_encodings[97].item(),\
        face_encodings[98].item(),\
        face_encodings[99].item(),\
        face_encodings[100].item(),\
        face_encodings[101].item(),\
        face_encodings[102].item(),\
        face_encodings[103].item(),\
        face_encodings[104].item(),\
        face_encodings[105].item(),\
        face_encodings[106].item(),\
        face_encodings[107].item(),\
        face_encodings[108].item(),\
        face_encodings[109].item(),\
        face_encodings[110].item(),\
        face_encodings[111].item(),\
        face_encodings[112].item(),\
        face_encodings[113].item(),\
        face_encodings[114].item(),\
        face_encodings[115].item(),\
        face_encodings[116].item(),\
        face_encodings[117].item(),\
        face_encodings[118].item(),\
        face_encodings[119].item(),\
        face_encodings[120].item(),\
        face_encodings[121].item(),\
        face_encodings[122].item(),\
        face_encodings[123].item(),\
        face_encodings[124].item(),\
        face_encodings[125].item(),\
        face_encodings[126].item(),\
        face_encodings[127].item())


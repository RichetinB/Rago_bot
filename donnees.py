TOP = 'top'
JUNGLE = 'jungle'
MID = 'mid'
ADC = 'adc'
SUPP = 'support'

champions_list = {
    'champion': [
        {'id': 0, 'name': 'aatrox', 'roles': [TOP]},
        {'id': 1, 'name': 'ahri', 'roles': [MID]},
        {'id': 2, 'name': 'akali', 'roles': [MID, TOP]},
        {'id': 3, 'name': 'akshan', 'roles': [MID, TOP]},
        {'id': 4, 'name': 'alistar', 'roles': [SUPP]},
        {'id': 5, 'name': 'amumu', 'roles': [JUNGLE]},
        {'id': 6, 'name': 'anivia', 'roles': [MID, SUPP]},
        {'id': 7, 'name': 'annie', 'roles': [MID, SUPP]},
        {'id': 8, 'name': 'aphelios', 'roles': [ADC]},
        {'id': 9, 'name': 'ashe', 'roles': [ADC, SUPP]},
        {'id': 10, 'name': 'aurelion sol', 'roles': [MID]},
        {'id': 11, 'name': 'azir', 'roles': [MID]},
        {'id': 12, 'name': 'bard', 'roles': [SUPP]},
        {'id': 13, 'name': "bel'veth", 'roles': [JUNGLE]},
        {'id': 14, 'name': 'blitzcrank', 'roles': [SUPP]},
        {'id': 15, 'name': 'brand', 'roles': [SUPP, MID, JUNGLE]},
        {'id': 16, 'name': 'braum', 'roles': [SUPP]},
        {'id': 17, 'name': 'briar', 'roles': [JUNGLE, TOP]},
        {'id': 18, 'name': 'caitlyn', 'roles': [ADC]},
        {'id': 19, 'name': 'camille', 'roles': [TOP]},
        {'id': 20, 'name': 'cassiopea', 'roles': [TOP, MID]},
        {'id': 21, 'name': "cho'gath", 'roles': [TOP, JUNGLE]},
        {'id': 22, 'name': 'corki', 'roles': [MID]},
        {'id': 23, 'name': 'darius', 'roles': [TOP]},
        {'id': 24, 'name': 'diana', 'roles': [MID, JUNGLE]},
        {'id': 25, 'name': 'dr. mundo', 'roles': [TOP, JUNGLE]},
        {'id': 26, 'name': 'draven', 'roles': [ADC]},
        {'id': 27, 'name': 'ekko', 'roles': [MID, JUNGLE]},
        {'id': 28, 'name': 'elise', 'roles': [JUNGLE]},
        {'id': 29, 'name': 'evelyn', 'roles': [JUNGLE]},
        {'id': 30, 'name': 'ezreal', 'roles': [ADC]},
        {'id': 31, 'name': 'fiddlestick', 'roles': [JUNGLE]},
        {'id': 32, 'name': 'fiora', 'roles': [TOP]},
        {'id': 33, 'name': 'fizz', 'roles': [MID]},
        {'id': 34, 'name': 'galio', 'roles': [MID, SUPP, TOP]},
        {'id': 35, 'name': 'gankplank', 'roles': [TOP]},
        {'id': 36, 'name': 'garen', 'roles': [TOP]},
        {'id': 37, 'name': 'gnar', 'roles': [TOP]},
        {'id': 38, 'name': 'gragas', 'roles': [MID, JUNGLE, TOP]},
        {'id': 39, 'name': 'graves', 'roles': [JUNGLE]},
        {'id': 40, 'name': 'gwen', 'roles': [MID, TOP, JUNGLE]},
        {'id': 41, 'name': 'hecarim', 'roles': [JUNGLE]},
        {'id': 42, 'name': 'heimerdinger', 'roles': [MID, SUPP]},
        {'id': 43, 'name': 'hwei', 'roles': [MID, SUPP]},
        {'id': 44, 'name': 'illaoi', 'roles': [TOP]},
        {'id': 45, 'name': 'irelia', 'roles': [MID, TOP]},
        {'id': 46, 'name': 'ivern', 'roles': [JUNGLE, SUPP]},
        {'id': 47, 'name': 'janna', 'roles': [SUPP]},
        {'id': 48, 'name': 'jarvan', 'roles': [TOP, JUNGLE]},
        {'id': 49, 'name': 'jax', 'roles': [TOP, JUNGLE]},
        {'id': 50, 'name': 'jayce', 'roles': [MID, TOP]},
        {'id': 51, 'name': 'jhin', 'roles': [ADC]},
        {'id': 52, 'name': 'jinx', 'roles': [ADC]},
        {'id': 53, 'name': "K'santé", 'roles': [TOP]},
        {'id': 54, 'name': "kai'sa", 'roles': [ADC]},
        {'id': 55, 'name': 'kalista', 'roles': [ADC]},
        {'id': 56, 'name': 'karma', 'roles': [SUPP, MID]},
        {'id': 57, 'name': 'karthus', 'roles': [MID, JUNGLE, ADC]},
        {'id': 58, 'name': 'kasadin', 'roles': [MID]},
        {'id': 59, 'name': 'katarina', 'roles': [MID]},
        {'id': 60, 'name': 'kayle', 'roles': [TOP, MID]},
        {'id': 61, 'name': 'kayn', 'roles': [JUNGLE]},
        {'id': 62, 'name': 'kenen', 'roles': [MID, TOP]},
        {'id': 63, 'name': "kha'zix", 'roles': [JUNGLE]},
        {'id': 64, 'name': 'kindred', 'roles': [JUNGLE]},
        {'id': 65, 'name': 'kled', 'roles': [TOP]},
        {'id': 66, 'name': "kog'maw", 'roles': [ADC, MID]},
        {'id': 67, 'name': 'leblanc', 'roles': [MID]},
        {'id': 68, 'name': 'lee sin', 'roles': [JUNGLE]},
        {'id': 69, 'name': 'leona', 'roles': [SUPP]},
        {'id': 70, 'name': 'lillia', 'roles': [TOP, JUNGLE]},
        {'id': 71, 'name': 'lissandra', 'roles': [MID]},
        {'id': 72, 'name': 'lucian', 'roles': [ADC]},
        {'id': 73, 'name': 'lulu', 'roles': [SUPP]},
        {'id': 74, 'name': 'lux', 'roles': [MID, SUPP]},
        {'id': 75, 'name': 'maitre yi', 'roles': [JUNGLE]},
        {'id': 76, 'name': 'malphite', 'roles': [TOP, MID]},
        {'id': 77, 'name': 'malzahar', 'roles': [MID]},
        {'id': 78, 'name': 'maokai', 'roles': [SUPP, JUNGLE, TOP]},
        {'id': 79, 'name': 'milio', 'roles': [SUPP]},
        {'id': 80, 'name': 'miss fortune', 'roles': [ADC]},
        {'id': 81, 'name': 'mordekaiser', 'roles': [TOP, JUNGLE]},
        {'id': 82, 'name': 'morgana', 'roles': [SUPP, JUNGLE]},
        {'id': 83, 'name': 'naafiri', 'roles': [MID, JUNGLE]},
        {'id': 84, 'name': 'nami', 'roles': [SUPP]},
        {'id': 85, 'name': 'nasus', 'roles': [TOP, JUNGLE]},
        {'id': 86, 'name': 'nautilus', 'roles': [SUPP]},
        {'id': 87, 'name': 'neeko', 'roles': [MID, JUNGLE, SUPP]},
        {'id': 88, 'name': 'nidalee', 'roles': [JUNGLE]},
        {'id': 89, 'name': 'nilah', 'roles': [ADC]},
        {'id': 90, 'name': 'nocturne', 'roles': [JUNGLE]},
        {'id': 91, 'name': 'nunu et willum', 'roles': [JUNGLE]},
        {'id': 92, 'name': 'olaf', 'roles': [TOP, JUNGLE]},
        {'id': 93, 'name': 'oriana', 'roles': [MID]},
        {'id': 94, 'name': 'ornn', 'roles': [TOP]},
        {'id': 95, 'name': 'pantheon', 'roles': [SUPP, MID, TOP, JUNGLE]},
        {'id': 96, 'name': 'poppy', 'roles': [JUNGLE, TOP]},
        {'id': 97, 'name': 'pyke', 'roles': [MID, SUPP]},
        {'id': 98, 'name': 'qiyana', 'roles': [JUNGLE, JUNGLE]},
        {'id': 99, 'name': 'quinn', 'roles': [TOP]},
        {'id': 100, 'name': 'rakan', 'roles': [SUPP]},
        {'id': 101, 'name': 'rammus', 'roles': [TOP, JUNGLE]},
        {'id': 102, 'name': "rek'sai", 'roles': [JUNGLE, TOP]},
        {'id': 103, 'name': 'rell', 'roles': [SUPP, JUNGLE]},
        {'id': 104, 'name': 'renata glasc', 'roles': [SUPP]},
        {'id': 105, 'name': 'renekton', 'roles': [TOP]},
        {'id': 106, 'name': 'rengar', 'roles': [JUNGLE]},
        {'id': 107, 'name': 'riven', 'roles': [TOP]},
        {'id': 108, 'name': 'rumble', 'roles': [MID, TOP]},
        {'id': 109, 'name': 'ryze', 'roles': [MID]},
        {'id': 110, 'name': 'samira', 'roles': [ADC]},
        {'id': 111, 'name': 'sejuani', 'roles': [TOP, JUNGLE]},
        {'id': 112, 'name': 'senna', 'roles': [ADC, SUPP]},
        {'id': 113, 'name': 'seraphine', 'roles': [MID, SUPP, ADC]},
        {'id': 114, 'name': 'sett', 'roles': [TOP]},
        {'id': 115, 'name': 'shaco', 'roles': [JUNGLE]},
        {'id': 116, 'name': 'shen', 'roles': [TOP]},
        {'id': 117, 'name': 'shyvana', 'roles': [JUNGLE]},
        {'id': 118, 'name': 'singed', 'roles': [TOP, JUNGLE]},
        {'id': 119, 'name': 'sion', 'roles': [TOP]},
        {'id': 120, 'name': 'sivir', 'roles': [ADC]},
        {'id': 121, 'name': 'skarner', 'roles': [JUNGLE]},
        {'id': 122, 'name': 'smolder', 'roles': [ADC, MID]},
        {'id': 123, 'name': 'sona', 'roles': [SUPP]},
        {'id': 124, 'name': 'soraka', 'roles': [SUPP]},
        {'id': 125, 'name': 'swain', 'roles': [MID, SUPP]},
        {'id': 126, 'name': 'sylas', 'roles': [MID, JUNGLE]},
        {'id': 127, 'name': 'syndra', 'roles': [MID, SUPP]},
        {'id': 128, 'name': 'tahm kench', 'roles': [SUPP, TOP]},
        {'id': 129, 'name': 'taliyah', 'roles': [MID, JUNGLE]},
        {'id': 130, 'name': 'talon', 'roles': [MID, JUNGLE]},
        {'id': 131, 'name': 'taric', 'roles': [SUPP]},
        {'id': 132, 'name': 'teemo', 'roles': [TOP]},
        {'id': 133, 'name': 'tresh', 'roles': [SUPP]},
        {'id': 134, 'name': 'tristana', 'roles': [ADC, MID]},
        {'id': 135, 'name': 'trundle', 'roles': [TOP, JUNGLE]},
        {'id': 136, 'name': 'tryndamere', 'roles': [MID, TOP]},
        {'id': 137, 'name': 'twisted fate', 'roles': [MID]},
        {'id': 138, 'name': 'twitch', 'roles': [MID, ADC, JUNGLE]},
        {'id': 139, 'name': 'udir', 'roles': [TOP, JUNGLE]},
        {'id': 140, 'name': 'urgot', 'roles': [TOP]},
        {'id': 141, 'name': 'varus', 'roles': [ADC]},
        {'id': 142, 'name': 'vayne', 'roles': [ADC, TOP]},
        {'id': 143, 'name': 'veigar', 'roles': [MID, ADC]},
        {'id': 144, 'name': "vel'koz", 'roles': [MID, SUPP]},
        {'id': 145, 'name': 'vex', 'roles': [MID]},
        {'id': 146, 'name': 'vi', 'roles': [JUNGLE]},
        {'id': 147, 'name': 'viego', 'roles': [JUNGLE]},
        {'id': 148, 'name': 'viktor', 'roles': [MID]},
        {'id': 149, 'name': 'vladimir', 'roles': [MID]},
        {'id': 150, 'name': 'volibear', 'roles': [TOP, JUNGLE]},
        {'id': 151, 'name': 'warwick', 'roles': [JUNGLE, TOP]},
        {'id': 152, 'name': 'wukong', 'roles': [JUNGLE]},
        {'id': 153, 'name': 'xayah', 'roles': [ADC]},
        {'id': 154, 'name': 'xerath', 'roles': [MID, SUPP]},
        {'id': 155, 'name': 'xin zhao', 'roles': [TOP, JUNGLE]},
        {'id': 156, 'name': 'yasuo', 'roles': [MID, TOP]},
        {'id': 157, 'name': 'yone', 'roles': [MID, TOP]},
        {'id': 158, 'name': 'yorick', 'roles': [TOP, JUNGLE]},
        {'id': 159, 'name': 'yuumi', 'roles': [SUPP]},
        {'id': 160, 'name': 'zac', 'roles': [JUNGLE, TOP]},
        {'id': 161, 'name': 'zed', 'roles': [JUNGLE, MID]},
        {'id': 162, 'name': 'zeri', 'roles': [ADC]},
        {'id': 163, 'name': 'ziggs', 'roles': [MID, ADC]},
        {'id': 164, 'name': 'zilean', 'roles': [MID, SUPP]},
        {'id': 165, 'name': 'zoe', 'roles': [MID]}
    ]
}
import typing as t
from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True)
class Language:
    """Language used in a post."""

    name: str  #: English name of Language.
    code1: str  #: ISO 639-1 Code.
    code2: str  #: ISO 639-2 Code.


# language databases:
# - official db: https://www.loc.gov/standards/iso639-2/php/code_list.php
# - bsky app: https://github.com/bluesky-social/social-app/blob/main/src/locale/languages.ts
LANGUAGES: t.Tuple = (
    Language(name='Afar', code1='aa', code2='aar'),
    Language(name='Abkhazian', code1='ab', code2='abk'),
    Language(name='Achinese', code1='', code2='ace'),
    Language(name='Acoli', code1='', code2='ach'),
    Language(name='Adangme', code1='', code2='ada'),
    Language(name='Adyghe; Adygei', code1='', code2='ady'),
    Language(name='Afro-Asiatic languages', code1='', code2='afa'),
    Language(name='Afrihili', code1='', code2='afh'),
    Language(name='Afrikaans', code1='af', code2='afr'),
    Language(name='Ainu', code1='', code2='ain'),
    Language(name='Akan', code1='ak', code2='aka'),
    Language(name='Akkadian', code1='', code2='akk'),
    Language(name='Albanian', code1='sq', code2='alb'),
    Language(name='Aleut', code1='', code2='ale'),
    Language(name='Algonquian languages', code1='', code2='alg'),
    Language(name='Southern Altai', code1='', code2='alt'),
    Language(name='Amharic', code1='am', code2='amh'),
    Language(name='English, Old (ca.450-1100)', code1='', code2='ang'),
    Language(name='Angika', code1='Angika', code2='anp '),
    Language(name='Apache languages', code1='', code2='apa'),
    Language(name='Arabic', code1='ar', code2='ara'),
    Language(name='Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)', code1='', code2='arc'),
    Language(name='Aragonese', code1='an', code2='arg'),
    Language(name='Armenian', code1='hy', code2='arm'),
    Language(name='Mapudungun; Mapuche', code1='', code2='arn'),
    Language(name='Arapaho', code1='', code2='arp'),
    Language(name='Artificial languages', code1='', code2='art'),
    Language(name='Arawak', code1='', code2='arw'),
    Language(name='Assamese', code1='as', code2='asm'),
    Language(name='Asturian; Bable; Leonese; Asturleonese', code1='', code2='ast'),
    Language(name='Athapascan languages', code1='', code2='ath'),
    Language(name='Australian languages', code1='', code2='aus'),
    Language(name='Avaric', code1='av', code2='ava'),
    Language(name='Avestan', code1='ae', code2='ave'),
    Language(name='Awadhi', code1='', code2='awa'),
    Language(name='Aymara', code1='ay', code2='aym'),
    Language(name='Azerbaijani', code1='az', code2='aze'),
    Language(name='Banda languages', code1='', code2='bad'),
    Language(name='Bamileke languages', code1='', code2='bai'),
    Language(name='Bashkir', code1='ba', code2='bak'),
    Language(name='Baluchi', code1='', code2='bal'),
    Language(name='Bambara', code1='bm', code2='bam'),
    Language(name='Balinese', code1='', code2='ban'),
    Language(name='Basque', code1='eu', code2='baq'),
    Language(name='Basa', code1='', code2='bas'),
    Language(name='Baltic languages', code1='', code2='bat'),
    Language(name='Beja; Bedawiyet', code1='', code2='bej'),
    Language(name='Belarusian', code1='be', code2='bel'),
    Language(name='Bemba', code1='', code2='bem'),
    Language(name='Bengali', code1='bn', code2='ben'),
    Language(name='Berber languages', code1='', code2='ber'),
    Language(name='Bhojpuri', code1='', code2='bho'),
    Language(name='Bihari languages', code1='bh', code2='bih'),
    Language(name='Bikol', code1='', code2='bik'),
    Language(name='Bini; Edo', code1='', code2='bin'),
    Language(name='Bislama', code1='bi', code2='bis'),
    Language(name='Siksika', code1='', code2='bla'),
    Language(name='Bantu languages', code1='', code2='bnt'),
    Language(name='Tibetan', code1='bo', code2='bod'),
    Language(name='Bosnian', code1='bs', code2='bos'),
    Language(name='Braj', code1='', code2='bra'),
    Language(name='Breton', code1='br', code2='bre'),
    Language(name='Batak languages', code1='', code2='btk'),
    Language(name='Buriat', code1='', code2='bua'),
    Language(name='Buginese', code1='', code2='bug'),
    Language(name='Bulgarian', code1='bg', code2='bul'),
    Language(name='Burmese', code1='my', code2='bur'),
    Language(name='Blin; Bilin', code1='', code2='byn'),
    Language(name='Caddo', code1='', code2='cad'),
    Language(name='Central American Indian languages', code1='', code2='cai'),
    Language(name='Galibi Carib', code1='', code2='car'),
    Language(name='Catalan; Valencian', code1='ca', code2='cat'),
    Language(name='Caucasian languages', code1='', code2='cau'),
    Language(name='Cebuano', code1='', code2='ceb'),
    Language(name='Celtic languages', code1='', code2='cel'),
    Language(name='Czech', code1='cs', code2='ces'),
    Language(name='Chamorro', code1='ch', code2='cha'),
    Language(name='Chibcha', code1='', code2='chb'),
    Language(name='Chechen', code1='ce', code2='che'),
    Language(name='Chagatai', code1='', code2='chg'),
    Language(name='Chinese', code1='zh', code2='chi'),
    Language(name='Chuukese', code1='', code2='chk'),
    Language(name='Mari', code1='', code2='chm'),
    Language(name='Chinook jargon', code1='', code2='chn'),
    Language(name='Choctaw', code1='', code2='cho'),
    Language(name='Chipewyan; Dene Suline', code1='', code2='chp'),
    Language(name='Cherokee', code1='', code2='chr'),
    Language(
        name='Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic', code1='cu', code2='chu'
    ),
    Language(name='Chuvash', code1='cv', code2='chv'),
    Language(name='Cheyenne', code1='', code2='chy'),
    Language(name='Chamic languages', code1='', code2='cmc'),
    Language(name='Montenegrin', code1='', code2='cnr'),
    Language(name='Coptic', code1='', code2='cop'),
    Language(name='Cornish', code1='kw', code2='cor'),
    Language(name='Corsican', code1='co', code2='cos'),
    Language(name='Creoles and pidgins, English based', code1='', code2='cpe'),
    Language(name='Creoles and pidgins, French-based', code1='', code2='cpf'),
    Language(name='Creoles and pidgins, Portuguese-based', code1='', code2='cpp'),
    Language(name='Cree', code1='cr', code2='cre'),
    Language(name='Crimean Tatar; Crimean Turkish', code1='', code2='crh'),
    Language(name='Creoles and pidgins', code1='', code2='crp'),
    Language(name='Kashubian', code1='', code2='csb'),
    Language(name='Cushitic languages', code1='', code2='cus'),
    Language(name='Welsh', code1='cy', code2='cym'),
    Language(name='Czech', code1='cs', code2='cze'),
    Language(name='Dakota', code1='', code2='dak'),
    Language(name='Danish', code1='da', code2='dan'),
    Language(name='Dargwa', code1='', code2='dar'),
    Language(name='Land Dayak languages', code1='', code2='day'),
    Language(name='Delaware', code1='', code2='del'),
    Language(name='Slave (Athapascan)', code1='', code2='den'),
    Language(name='German', code1='de', code2='deu'),
    Language(name='Dogrib', code1='', code2='dgr'),
    Language(name='Dinka', code1='', code2='din'),
    Language(name='Divehi; Dhivehi; Maldivian', code1='dv', code2='div'),
    Language(name='Dogri', code1='', code2='doi'),
    Language(name='Dravidian languages', code1='', code2='dra'),
    Language(name='Lower Sorbian', code1='', code2='dsb'),
    Language(name='Duala', code1='', code2='dua'),
    Language(name='Dutch, Middle (ca.1050-1350)', code1='', code2='dum'),
    Language(name='Dutch; Flemish', code1='nl', code2='dut'),
    Language(name='Dyula', code1='', code2='dyu'),
    Language(name='Dzongkha', code1='dz', code2='dzo'),
    Language(name='Efik', code1='', code2='efi'),
    Language(name='Egyptian (Ancient)', code1='', code2='egy'),
    Language(name='Ekajuk', code1='', code2='eka'),
    Language(name='Greek, Modern (1453-)', code1='el', code2='ell'),
    Language(name='Elamite', code1='', code2='elx'),
    Language(name='English', code1='en', code2='eng'),
    Language(name='English, Middle (1100-1500)', code1='', code2='enm'),
    Language(name='Esperanto', code1='eo', code2='epo'),
    Language(name='Estonian', code1='et', code2='est'),
    Language(name='Basque', code1='eu', code2='eus'),
    Language(name='Ewe', code1='ee', code2='ewe'),
    Language(name='Ewondo', code1='', code2='ewo'),
    Language(name='Fang', code1='', code2='fan'),
    Language(name='Faroese', code1='fo', code2='fao'),
    Language(name='Persian', code1='fa', code2='fas'),
    Language(name='Fanti', code1='', code2='fat'),
    Language(name='Fijian', code1='fj', code2='fij'),
    Language(name='Filipino; Pilipino', code1='', code2='fil'),
    Language(name='Finnish', code1='fi', code2='fin'),
    Language(name='Finno-Ugrian languages', code1='', code2='fiu'),
    Language(name='Fon', code1='', code2='fon'),
    Language(name='French', code1='fr', code2='fra'),
    Language(name='French', code1='fr', code2='fre'),
    Language(name='French, Middle (ca.1400-1600)', code1='', code2='frm'),
    Language(name='French, Old (842-ca.1400)', code1='', code2='fro'),
    Language(name='Northern Frisian', code1='', code2='frr'),
    Language(name='Eastern Frisian', code1='', code2='frs'),
    Language(name='Western Frisian', code1='fy', code2='fry'),
    Language(name='Fulah', code1='ff', code2='ful'),
    Language(name='Friulian', code1='', code2='fur'),
    Language(name='Ga', code1='', code2='gaa'),
    Language(name='Gayo', code1='', code2='gay'),
    Language(name='Gbaya', code1='', code2='gba'),
    Language(name='Germanic languages', code1='', code2='gem'),
    Language(name='Georgian', code1='ka', code2='geo'),
    Language(name='German', code1='de', code2='ger'),
    Language(name='Geez', code1='', code2='gez'),
    Language(name='Gilbertese', code1='', code2='gil'),
    Language(name='Gaelic; Scottish Gaelic', code1='gd', code2='gla'),
    Language(name='Irish', code1='ga', code2='gle'),
    Language(name='Galician', code1='gl', code2='glg'),
    Language(name='Manx', code1='gv', code2='glv'),
    Language(name='German, Middle High (ca.1050-1500)', code1='', code2='gmh'),
    Language(name='German, Old High (ca.750-1050)', code1='', code2='goh'),
    Language(name='Gondi', code1='', code2='gon'),
    Language(name='Gorontalo', code1='', code2='gor'),
    Language(name='Gothic', code1='', code2='got'),
    Language(name='Grebo', code1='', code2='grb'),
    Language(name='Greek, Ancient (to 1453)', code1='', code2='grc'),
    Language(name='Greek, Modern (1453-)', code1='el', code2='gre'),
    Language(name='Guarani', code1='gn', code2='grn'),
    Language(name='Swiss German; Alemannic; Alsatian', code1='', code2='gsw'),
    Language(name='goudjrati', code1='Gujarati', code2='gujgu'),
    Language(name="Gwich'in", code1='', code2='gwi'),
    Language(name='Haida', code1='', code2='hai'),
    Language(name='Haitian; Haitian Creole', code1='ht', code2='hat'),
    Language(name='Hausa', code1='ha', code2='hau'),
    Language(name='Hawaiian', code1='', code2='haw'),
    Language(name='Hebrew', code1='he', code2='heb'),
    Language(name='Herero', code1='hz', code2='her'),
    Language(name='Hiligaynon', code1='', code2='hil'),
    Language(name='Himachali languages; Western Pahari languages', code1='', code2='him'),
    Language(name='Hindi', code1='hi', code2='hin'),
    Language(name='Hittite', code1='', code2='hit'),
    Language(name='Hmong; Mong', code1='', code2='hmn'),
    Language(name='Hiri Motu', code1='ho', code2='hmo'),
    Language(name='Croatian', code1='hr', code2='hrv'),
    Language(name='Upper Sorbian', code1='', code2='hsb'),
    Language(name='Hungarian', code1='hu', code2='hun'),
    Language(name='Hupa', code1='', code2='hup'),
    Language(name='Armenian', code1='hy', code2='hye'),
    Language(name='Iban', code1='', code2='iba'),
    Language(name='Igbo', code1='ig', code2='ibo'),
    Language(name='Icelandic', code1='is', code2='ice'),
    Language(name='Ido', code1='io', code2='ido'),
    Language(name='Sichuan Yi; Nuosu', code1='ii', code2='iii'),
    Language(name='Ijo languages', code1='', code2='ijo'),
    Language(name='Inuktitut', code1='iu', code2='iku'),
    Language(name='Interlingue; Occidental', code1='ie', code2='ile'),
    Language(name='Iloko', code1='', code2='ilo'),
    Language(name='Interlingua (International Auxiliary Language Association)', code1='ia', code2='ina'),
    Language(name='Indic languages', code1='', code2='inc'),
    Language(name='Indonesian', code1='id', code2='ind'),
    Language(name='Indo-European languages', code1='', code2='ine'),
    Language(name='Ingush', code1='', code2='inh'),
    Language(name='Inupiaq', code1='ik', code2='ipk'),
    Language(name='Iranian languages', code1='', code2='ira'),
    Language(name='Iroquoian languages', code1='', code2='iro'),
    Language(name='Icelandic', code1='is', code2='isl'),
    Language(name='Italian', code1='it', code2='ita'),
    Language(name='Javanese', code1='jv', code2='jav'),
    Language(name='Lojban', code1='', code2='jbo'),
    Language(name='Japanese', code1='ja', code2='jpn'),
    Language(name='Judeo-Persian', code1='', code2='jpr'),
    Language(name='Judeo-Arabic', code1='', code2='jrb'),
    Language(name='Kara-Kalpak', code1='', code2='kaa'),
    Language(name='Kabyle', code1='', code2='kab'),
    Language(name='Kachin; Jingpho', code1='', code2='kac'),
    Language(name='Kalaallisut; Greenlandic', code1='kl', code2='kal'),
    Language(name='Kamba', code1='', code2='kam'),
    Language(name='Kannada', code1='kn', code2='kan'),
    Language(name='Karen languages', code1='', code2='kar'),
    Language(name='Kashmiri', code1='ks', code2='kas'),
    Language(name='Georgian', code1='ka', code2='kat'),
    Language(name='Kanuri', code1='kr', code2='kau'),
    Language(name='Kawi', code1='', code2='kaw'),
    Language(name='Kazakh', code1='kk', code2='kaz'),
    Language(name='Kabardian', code1='', code2='kbd'),
    Language(name='Khasi', code1='', code2='kha'),
    Language(name='Khoisan languages', code1='', code2='khi'),
    Language(name='Central Khmer', code1='km', code2='khm'),
    Language(name='Khotanese; Sakan', code1='', code2='kho'),
    Language(name='Kikuyu; Gikuyu', code1='ki', code2='kik'),
    Language(name='Kinyarwanda', code1='rw', code2='kin'),
    Language(name='Kirghiz; Kyrgyz', code1='ky', code2='kir'),
    Language(name='Kimbundu', code1='', code2='kmb'),
    Language(name='Konkani', code1='', code2='kok'),
    Language(name='Komi', code1='kv', code2='kom'),
    Language(name='Kongo', code1='kg', code2='kon'),
    Language(name='Korean', code1='ko', code2='kor'),
    Language(name='Kosraean', code1='', code2='kos'),
    Language(name='Kpelle', code1='', code2='kpe'),
    Language(name='Karachay-Balkar', code1='', code2='krc'),
    Language(name='Karelian', code1='', code2='krl'),
    Language(name='Kru languages', code1='', code2='kro'),
    Language(name='Kurukh', code1='', code2='kru'),
    Language(name='Kuanyama; Kwanyama', code1='kj', code2='kua'),
    Language(name='Kumyk', code1='', code2='kum'),
    Language(name='Kurdish', code1='ku', code2='kur'),
    Language(name='Kutenai', code1='', code2='kut'),
    Language(name='Ladino', code1='', code2='lad'),
    Language(name='Lahnda', code1='', code2='lah'),
    Language(name='Lamba', code1='', code2='lam'),
    Language(name='Lao', code1='lo', code2='lao'),
    Language(name='Latin', code1='la', code2='lat'),
    Language(name='Latvian', code1='lv', code2='lav'),
    Language(name='Lezghian', code1='', code2='lez'),
    Language(name='Limburgan; Limburger; Limburgish', code1='li', code2='lim'),
    Language(name='Lingala', code1='ln', code2='lin'),
    Language(name='Lithuanian', code1='lt', code2='lit'),
    Language(name='Mongo', code1='', code2='lol'),
    Language(name='Lozi', code1='', code2='loz'),
    Language(name='Luxembourgish; Letzeburgesch', code1='lb', code2='ltz'),
    Language(name='Luba-Lulua', code1='', code2='lua'),
    Language(name='Luba-Katanga', code1='lu', code2='lub'),
    Language(name='Ganda', code1='lg', code2='lug'),
    Language(name='Luiseno', code1='', code2='lui'),
    Language(name='Lunda', code1='', code2='lun'),
    Language(name='luo (Kenya et Tanzanie)', code1=' Luo (Kenya and Tanzania)', code2='luo'),
    Language(name='Lushai', code1='', code2='lus'),
    Language(name='Macedonian', code1='mk', code2='mac'),
    Language(name='Madurese', code1='', code2='mad'),
    Language(name='Magahi', code1='', code2='mag'),
    Language(name='Marshallese', code1='mh', code2='mah'),
    Language(name='Maithili', code1='', code2='mai'),
    Language(name='Makasar', code1='', code2='mak'),
    Language(name='Malayalam', code1='ml', code2='mal'),
    Language(name='Mandingo', code1='', code2='man'),
    Language(name='Maori', code1='mi', code2='mao'),
    Language(name='Austronesian languages', code1='', code2='map'),
    Language(name='Marathi', code1='mr', code2='mar'),
    Language(name='Masai', code1='', code2='mas'),
    Language(name='Malay', code1='ms', code2='may'),
    Language(name='Moksha', code1='', code2='mdf'),
    Language(name='Mandar', code1='', code2='mdr'),
    Language(name='Mende', code1='', code2='men'),
    Language(name='Irish, Middle (900-1200)', code1='', code2='mga'),
    Language(name="Mi'kmaq; Micmac", code1='', code2='mic'),
    Language(name='Minangkabau', code1='', code2='min'),
    Language(name='Uncoded languages', code1='', code2='mis'),
    Language(name='Macedonian', code1='mk', code2='mkd'),
    Language(name='Mon-Khmer languages', code1='', code2='mkh'),
    Language(name='Malagasy', code1='mg', code2='mlg'),
    Language(name='Maltese', code1='mt', code2='mlt'),
    Language(name='Manchu', code1='', code2='mnc'),
    Language(name='Manipuri', code1='', code2='mni'),
    Language(name='Manobo languages', code1='', code2='mno'),
    Language(name='Mohawk', code1='', code2='moh'),
    Language(name='Mongolian', code1='mn', code2='mon'),
    Language(name='Mossi', code1='', code2='mos'),
    Language(name='Maori', code1='mi', code2='mri'),
    Language(name='Malay', code1='ms', code2='msa'),
    Language(name='Multiple languages', code1='', code2='mul'),
    Language(name='Munda languages', code1='', code2='mun'),
    Language(name='Creek', code1='', code2='mus'),
    Language(name='Mirandese', code1='', code2='mwl'),
    Language(name='Marwari', code1='', code2='mwr'),
    Language(name='Burmese', code1='my', code2='mya'),
    Language(name='Mayan languages', code1='', code2='myn'),
    Language(name='Erzya', code1='', code2='myv'),
    Language(name='Nahuatl languages', code1='', code2='nah'),
    Language(name='North American Indian languages', code1='', code2='nai'),
    Language(name='Neapolitan', code1='', code2='nap'),
    Language(name='Nauru', code1='na', code2='nau'),
    Language(name='Navajo; Navaho', code1='nv', code2='nav'),
    Language(name='Ndebele, South; South Ndebele', code1='nr', code2='nbl'),
    Language(name='Ndebele, North; North Ndebele', code1='nd', code2='nde'),
    Language(name='Ndonga', code1='ng', code2='ndo'),
    Language(name='Low German; Low Saxon; German, Low; Saxon, Low', code1='', code2='nds'),
    Language(name='Nepali', code1='ne', code2='nep'),
    Language(name='Nepal Bhasa; Newari', code1='', code2='new'),
    Language(name='Nias', code1='', code2='nia'),
    Language(name='Niger-Kordofanian languages', code1='', code2='nic'),
    Language(name='Niuean', code1='', code2='niu'),
    Language(name='Dutch; Flemish', code1='nl', code2='nld'),
    Language(name='Norwegian Nynorsk; Nynorsk, Norwegian', code1='nn', code2='nno'),
    Language(name='Bokmål, Norwegian; Norwegian Bokmål', code1='nb', code2='nob'),
    Language(name='Nogai', code1='', code2='nog'),
    Language(name='Norse, Old', code1='', code2='non'),
    Language(name='Norwegian', code1='no', code2='nor'),
    Language(name="N'Ko", code1='', code2='nqo'),
    Language(name='Pedi; Sepedi; Northern Sotho', code1='', code2='nso'),
    Language(name='Nubian languages', code1='', code2='nub'),
    Language(name='Classical Newari; Old Newari; Classical Nepal Bhasa', code1='', code2='nwc'),
    Language(name='Chichewa; Chewa; Nyanja', code1='ny', code2='nya'),
    Language(name='Nyamwezi', code1='', code2='nym'),
    Language(name='Nyankole', code1='', code2='nyn'),
    Language(name='Nyoro', code1='', code2='nyo'),
    Language(name='Nzima', code1='', code2='nzi'),
    Language(name='Occitan (post 1500)', code1='oc', code2='oci'),
    Language(name='Ojibwa', code1='oj', code2='oji'),
    Language(name='Oriya', code1='or', code2='ori'),
    Language(name='Oromo', code1='om', code2='orm'),
    Language(name='Osage', code1='', code2='osa'),
    Language(name='Ossetian; Ossetic', code1='os', code2='oss'),
    Language(name='Turkish, Ottoman (1500-1928)', code1='', code2='ota'),
    Language(name='Otomian languages', code1='', code2='oto'),
    Language(name='Papuan languages', code1='', code2='paa'),
    Language(name='Pangasinan', code1='', code2='pag'),
    Language(name='Pahlavi', code1=' ', code2='pal'),
    Language(name='Pampanga; Kapampangan', code1=' ', code2='pam'),
    Language(name='pendjabi', code1='paPanjabi; Punjabi', code2='pan'),
    Language(name='Papiamento', code1=' ', code2='pap'),
    Language(name='Palauan', code1=' ', code2='pau'),
    Language(name='Persian, Old (ca.600-400 B.C.)', code1=' ', code2='peo'),
    Language(name='Persian', code1='fa', code2='per'),
    Language(name='Philippine languages', code1=' ', code2='phi'),
    Language(name='Phoenician', code1=' ', code2='phn'),
    Language(name='Pali', code1='pi', code2='pli'),
    Language(name='Polish', code1='pl', code2='pol'),
    Language(name='Pohnpeian', code1=' ', code2='pon'),
    Language(name='Portuguese', code1='pt', code2='por'),
    Language(name='Prakrit languages', code1=' ', code2='pra'),
    Language(name='Provençal, Old (to 1500);Occitan, Old (to 1500)', code1=' ', code2='pro'),
    Language(name='Pushto; Pashto', code1='ps', code2='pus'),
    Language(name='Quechua', code1='qu', code2='que'),
    Language(name='Rajasthani', code1=' ', code2='raj'),
    Language(name='Rapanui', code1=' ', code2='rap'),
    Language(name='Rarotongan; Cook Islands Maori', code1=' ', code2='rar'),
    Language(name='Romance languages', code1=' ', code2='roa'),
    Language(name='Romansh', code1='rm', code2='roh'),
    Language(name='Romany', code1=' ', code2='rom'),
    Language(name='Romanian; Moldavian; Moldovan', code1='ro', code2='rum'),
    Language(name='Romanian; Moldavian; Moldovan', code1='ro', code2='ron'),
    Language(name='Rundi', code1='rn', code2='run'),
    Language(name='Aromanian; Arumanian; Macedo-Romanian', code1=' ', code2='rup'),
    Language(name='Russian', code1='ru', code2='rus'),
    Language(name='Sandawe', code1=' ', code2='sad'),
    Language(name='Sango', code1='sg', code2='sag'),
    Language(name='Yakut', code1=' ', code2='sah'),
    Language(name='South American Indian languages', code1=' ', code2='sai'),
    Language(name='Salishan languages', code1=' ', code2='sal'),
    Language(name='Samaritan Aramaic', code1=' ', code2='sam'),
    Language(name='Sanskrit', code1='sa', code2='san'),
    Language(name='Sasak', code1=' ', code2='sas'),
    Language(name='Santali', code1=' ', code2='sat'),
    Language(name='Sicilian', code1=' ', code2='scn'),
    Language(name='Scots', code1=' ', code2='sco'),
    Language(name='Selkup', code1=' ', code2='sel'),
    Language(name='Semitic languages', code1=' ', code2='sem'),
    Language(name='Irish, Old (to 900)', code1=' ', code2='sga'),
    Language(name='Sign Languages', code1=' ', code2='sgn'),
    Language(name='Shan', code1=' ', code2='shn'),
    Language(name='Sidamo', code1=' ', code2='sid'),
    Language(name='Sinhala; Sinhalese', code1='si', code2='sin'),
    Language(name='Siouan languages', code1=' ', code2='sio'),
    Language(name='Sino-Tibetan languages', code1=' ', code2='sit'),
    Language(name='Slavic languages', code1=' ', code2='sla'),
    Language(name='Slovak', code1='sk', code2='slo'),
    Language(name='Slovak', code1='sk', code2='slk'),
    Language(name='Slovenian', code1='sl', code2='slv'),
    Language(name='Southern Sami', code1=' ', code2='sma'),
    Language(name='Northern Sami', code1='se', code2='sme'),
    Language(name='Sami languages', code1=' ', code2='smi'),
    Language(name='Lule Sami', code1=' ', code2='smj'),
    Language(name='Inari Sami', code1=' ', code2='smn'),
    Language(name='Samoan', code1='sm', code2='smo'),
    Language(name='Skolt Sami', code1=' ', code2='sms'),
    Language(name='Shona', code1='sn', code2='sna'),
    Language(name='Sindhi', code1='sd', code2='snd'),
    Language(name='Soninke', code1=' ', code2='snk'),
    Language(name='Sogdian', code1=' ', code2='sog'),
    Language(name='Somali', code1='so', code2='som'),
    Language(name='Songhai languages', code1=' ', code2='son'),
    Language(name='Sotho, Southern', code1='st', code2='sot'),
    Language(name='Spanish', code1='es', code2='spa'),
    Language(name='Albanian', code1='sq', code2='sqi'),
    Language(name='Sardinian', code1='sc', code2='srd'),
    Language(name='Sranan Tongo', code1=' ', code2='srn'),
    Language(name='Serbian', code1='sr', code2='srp'),
    Language(name='Serer', code1=' ', code2='srr'),
    Language(name='Nilo-Saharan languages', code1=' ', code2='ssa'),
    Language(name='Swati', code1='ss', code2='ssw'),
    Language(name='Sukuma', code1=' ', code2='suk'),
    Language(name='Sundanese', code1='su', code2='sun'),
    Language(name='Susu', code1=' ', code2='sus'),
    Language(name='Sumerian', code1=' ', code2='sux'),
    Language(name='Swahili', code1='sw', code2='swa'),
    Language(name='Swedish', code1='sv', code2='swe'),
    Language(name='Classical Syriac', code1=' ', code2='syc'),
    Language(name='Syriac', code1=' ', code2='syr'),
    Language(name='Tahitian', code1='ty', code2='tah'),
    Language(name='Tai languages', code1=' ', code2='tai'),
    Language(name='Tamil', code1='ta', code2='tam'),
    Language(name='Tatar', code1='tt', code2='tat'),
    Language(name='Telugu', code1='te', code2='tel'),
    Language(name='Timne', code1=' ', code2='tem'),
    Language(name='Tereno', code1=' ', code2='ter'),
    Language(name='Tetum', code1=' ', code2='tet'),
    Language(name='Tajik', code1='tg', code2='tgk'),
    Language(name='Tagalog', code1='tl', code2='tgl'),
    Language(name='Thai', code1='th', code2='tha'),
    Language(name='Tibetan', code1='bo', code2='tib'),
    Language(name='Tigre', code1=' ', code2='tig'),
    Language(name='Tigrinya', code1='ti', code2='tir'),
    Language(name='Tiv', code1=' ', code2='tiv'),
    Language(name='Tokelau', code1=' ', code2='tkl'),
    Language(name='Klingon; tlhIngan-Hol', code1=' ', code2='tlh'),
    Language(name='Tlingit', code1=' ', code2='tli'),
    Language(name='Tamashek', code1=' ', code2='tmh'),
    Language(name='Tonga (Nyasa)', code1=' ', code2='tog'),
    Language(name='Tonga (Tonga Islands)', code1='to', code2='ton'),
    Language(name='Tok Pisin', code1=' ', code2='tpi'),
    Language(name='Tsimshian', code1=' ', code2='tsi'),
    Language(name='Tswana', code1='tn', code2='tsn'),
    Language(name='Tsonga', code1='ts', code2='tso'),
    Language(name='Turkmen', code1='tk', code2='tuk'),
    Language(name='Tumbuka', code1=' ', code2='tum'),
    Language(name='Tupi languages', code1=' ', code2='tup'),
    Language(name='Turkish', code1='tr', code2='tur'),
    Language(name='Altaic languages', code1=' ', code2='tut'),
    Language(name='Tuvalu', code1=' ', code2='tvl'),
    Language(name='Twi', code1='tw', code2='twi'),
    Language(name='Tuvinian', code1=' ', code2='tyv'),
    Language(name='Udmurt', code1=' ', code2='udm'),
    Language(name='Ugaritic', code1=' ', code2='uga'),
    Language(name='Uighur; Uyghur', code1='ug', code2='uig'),
    Language(name='Ukrainian', code1='uk', code2='ukr'),
    Language(name='Umbundu', code1=' ', code2='umb'),
    Language(name='Undetermined', code1=' ', code2='und'),
    Language(name='Urdu', code1='ur', code2='urd'),
    Language(name='Uzbek', code1='uz', code2='uzb'),
    Language(name='Vai', code1=' ', code2='vai'),
    Language(name='Venda', code1='ve', code2='ven'),
    Language(name='Vietnamese', code1='vi', code2='vie'),
    Language(name='Volapük', code1='vo', code2='vol'),
    Language(name='Votic', code1=' ', code2='vot'),
    Language(name='Wakashan languages', code1=' ', code2='wak'),
    Language(name='Wolaitta; Wolaytta', code1=' ', code2='wal'),
    Language(name='Waray', code1=' ', code2='war'),
    Language(name='Washo', code1=' ', code2='was'),
    Language(name='Welsh', code1='cy', code2='wel'),
    Language(name='Sorbian languages', code1=' ', code2='wen'),
    Language(name='Walloon', code1='wa', code2='wln'),
    Language(name='Wolof', code1='wo', code2='wol'),
    Language(name='Kalmyk; Oirat', code1=' ', code2='xal'),
    Language(name='Xhosa', code1='xh', code2='xho'),
    Language(name='Yao', code1=' ', code2='yao'),
    Language(name='Yapese', code1=' ', code2='yap'),
    Language(name='Yiddish', code1='yi', code2='yid'),
    Language(name='Yoruba', code1='yo', code2='yor'),
    Language(name='Yupik languages', code1=' ', code2='ypk'),
    Language(name='Zapotec', code1=' ', code2='zap'),
    Language(name='Blissymbols; Blissymbolics; Bliss', code1=' ', code2='zbl'),
    Language(name='Zenaga', code1=' ', code2='zen'),
    Language(name='Standard Moroccan Tamazight', code1=' ', code2='zgh'),
    Language(name='Zhuang; Chuang', code1='za', code2='zha'),
    Language(name='Chinese', code1='zh', code2='zho'),
    Language(name='Zande languages', code1=' ', code2='znd'),
    Language(name='Zulu', code1='zu', code2='zul'),
    Language(name='Zuni', code1=' ', code2='zun'),
    Language(name='Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki', code1='', code2='zza'),
)

#: Mapping `code1` to language instance. Use ``LANGUAGES_MAP_CODE1.get('someCode1')``. ``None`` means unknown lang.
LANGUAGES_MAP_CODE1: t.Mapping[str, Language] = MappingProxyType({lang.code1: lang for lang in LANGUAGES})

#: Mapping `code2` to language instance. Use ``LANGUAGES_MAP_CODE2.get('someCode2')``. ``None`` means unknown lang.
LANGUAGES_MAP_CODE2: t.Mapping[str, Language] = MappingProxyType({lang.code2: lang for lang in LANGUAGES})

#: Default language code1 used by SDK.
DEFAULT_LANGUAGE_CODE1 = 'en'
#: Default :obj:`Language` instance used by SDK.
DEFAULT_LANGUAGE: Language = LANGUAGES_MAP_CODE1[DEFAULT_LANGUAGE_CODE1]
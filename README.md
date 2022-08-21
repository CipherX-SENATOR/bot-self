|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

[ API_HASH * API_ID ]
	
	EDIT FILE {

		( config.ini )

			EDIT LINE {

				3 ) api_id = YOUR API ID 
				4 ) api_hash = YOUR API HASH
			}
	}
	
[ PROXY ]
	
	EDIT LINE {

		37 ) app = Client('ER-STR',config_file="config.ini") -> app = Client('ER-STR',config_file="config.ini",proxy=proxy) 
	}

[ EDIT ADMIN ]

	EDIT LINE {

		27 ) admin = ("1469547340") -> admin = ("YOUR_ID") REPLACE ID You
	}

[ EDIT FOSH ENEMY ]

	EDIT LINE {

		20 ) Fosh = ['..','..'] -> Fosh = ['YOUR TEXT'] REPLACE TEXT
	}

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


TeleGram ↬ @EBLETSM

Rubika ↬ @CipherX
import os
import mysql.connector
import config

#TODO: add threshold table
#TODO: add reference table

userHome = config.userHome()

mydb = mysql.connector.connect(
	host='localhost',
	option_files=userHome + '/.mysql/defaults'
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS `nepc`;")
mycursor.execute("CREATE DATABASE IF NOT EXISTS `nepc`;")
mycursor.execute("SET default_storage_engine = INNODB;")


mycursor.execute("CREATE TABLE `nepc`.`species`("
"	`id` INT UNSIGNED NOT NULL auto_increment ,"
"	`name` VARCHAR(40) NOT NULL ,"
"	`long_name` VARCHAR(100) NOT NULL ,"
"	PRIMARY KEY(`id`)"
");"
)

mycursor.execute("CREATE TABLE `nepc`.`processes`("
"	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,"
"	`name` VARCHAR(40) NOT NULL ,"
"	`long_name` VARCHAR(240) NOT NULL ,"
"	`lhs` INT,"
"	`rhs` INT,"
"	`lhs_e` INT,"
"	`rhs_e` INT,"
"	`lhs_hv` INT,"
"	`rhs_hv` INT,"
"	`lhs_v` INT,"
"	`rhs_v` INT,"
"	`lhs_j` INT,"
"	`rhs_j` INT,"
"	PRIMARY KEY(`id`)"
");"
)

mycursor.execute("CREATE TABLE `nepc`.`states`("
"	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,"
"	`specie_id` INT UNSIGNED NOT NULL ,"
"	`name` VARCHAR(100) NOT NULL ,"
"	`long_name` VARCHAR(100) NOT NULL ,"
"	`configuration` JSON NOT NULL ,"
"	PRIMARY KEY(`id`) ,"
"	INDEX `SPECIE_ID`(`specie_id` ASC) ,"
"	CONSTRAINT `specie_id_STATES` FOREIGN KEY(`specie_id`) "
"		REFERENCES `nepc`.`species`(`id`) "
"		ON DELETE RESTRICT ON UPDATE CASCADE"
");"
)

mycursor.execute("CREATE TABLE `nepc`.`cs`("
"	`id` INT UNSIGNED NOT NULL, "
"	`specie_id` INT UNSIGNED NOT NULL, "
"	`process_id` INT UNSIGNED NOT NULL, "
"	`units_e` DOUBLE NOT NULL,"
"	`units_sigma` DOUBLE NOT NULL,"
"	`ref` VARCHAR(1000),"
"	`lhsA_id` INT UNSIGNED NULL ,"
"	`lhsB_id` INT UNSIGNED NULL ,"
"	`rhsA_id` INT UNSIGNED NULL ,"
"	`rhsB_id` INT UNSIGNED NULL ,"
"	`wavelength` DOUBLE NULL ,"
"	`lhs_v` INT NULL ,"
"	`rhs_v` INT NULL ,"
"	`lhs_j` INT NULL ,"
"	`rhs_j` INT NULL ,"
"	`background` VARCHAR(10000) ,"
"	`lpu` DOUBLE NULL ,"
"	`upu` DOUBLE NULL ,"
"	PRIMARY KEY(`id`) ,"
"	INDEX `SPECIE_ID`(`specie_id` ASC) ,"
"	INDEX `PROCESS_ID`(`process_id` ASC) ,"
"	CONSTRAINT `SPECIE_ID_CS` FOREIGN KEY(`specie_id`)"
"		REFERENCES `nepc`.`species`(`id`)"
"		ON DELETE RESTRICT ON UPDATE CASCADE,"
"	CONSTRAINT `PROCESS_ID_CS` FOREIGN KEY(`process_id`)"
"		REFERENCES `nepc`.`processes`(`id`)"
"		ON DELETE RESTRICT ON UPDATE CASCADE,"
"	CONSTRAINT `LHSA_ID_CS` FOREIGN KEY(`lhsA_id`)"
"		REFERENCES `nepc`.`states`(`id`),"
"	CONSTRAINT `LHSB_ID_CS` FOREIGN KEY(`lhsB_id`)"
"		REFERENCES `nepc`.`states`(`id`),"
"	CONSTRAINT `RHSA_ID_CS` FOREIGN KEY(`rhsA_id`)"
"		REFERENCES `nepc`.`states`(`id`),"
"	CONSTRAINT `RHSB_ID_CS` FOREIGN KEY(`rhsB_id`)"
"		REFERENCES `nepc`.`states`(`id`)"
");"
)

mycursor.execute("CREATE TABLE `nepc`.`csdata`("
"	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
"	`cs_id` INT UNSIGNED NOT NULL ,"
"	`e` DOUBLE NOT NULL ,"
"	`sigma` DOUBLE NOT NULL ,"
"	PRIMARY KEY(`id`) ,"
"	INDEX `CS_ID`(`cs_id` ASC) ,"
"	CONSTRAINT `CS_ID_CSDATA` FOREIGN KEY(`cs_id`)"
"		REFERENCES `nepc`.`cs`(`id`)"
"		ON DELETE RESTRICT ON UPDATE CASCADE"
");"
)

#################
### Load data ###
#################

mycursor.execute("LOAD DATA LOCAL INFILE 'processes.tsv'"   
"	INTO TABLE nepc.processes"
"	IGNORE 2 LINES;")

mycursor.execute("LOAD DATA LOCAL INFILE 'species.tsv'"
"	INTO TABLE nepc.species;")

mycursor.execute("LOAD DATA LOCAL INFILE 'n_states.tsv'"
"	INTO TABLE nepc.states"
"	IGNORE 1 LINES"
"	(id,@2s,@2p,@CoreTerm,@3s,@3p,@3d,@4s,name,long_name)"
"	SET configuration = JSON_OBJECT("
"		JSON_OBJECT('order', "
"			JSON_ARRAY('2s', '2p', 'CoreTerm', '3s', '3p', '3d','4s')"
"		),"
"		JSON_OBJECT('occupations',"
"			JSON_OBJECT("
"				'2s',@2s,"
"				'2p',@2p,"
"				'CoreTerm',@CoreTerm,"
"				'3s',@3s,"
"				'3p',@3p,"
"				'3d',@3d,"
"				'4s',@4s"
"			)"
"		)"
"	),"
"	specie_id = (select max(id) from nepc.species where name = 'N');"
)

mycursor.execute("LOAD DATA LOCAL INFILE 'n+_states.tsv'"
"	INTO TABLE nepc.states"
"	IGNORE 1 LINES"
"	(id,@2s,@2p,@CoreTerm,@3s,@3p,@3d,@4s,name,long_name)"
"	SET configuration = JSON_OBJECT("
"		JSON_OBJECT('order', "
"			JSON_ARRAY('2s', '2p', 'CoreTerm', '3s', '3p', '3d','4s')"
"		),"
"		JSON_OBJECT('occupations',"
"			JSON_OBJECT("
"				'2s',@2s,"
"				'2p',@2p,"
"				'CoreTerm',@CoreTerm,"
"				'3s',@3s,"
"				'3p',@3p,"
"				'3d',@3d,"
"				'4s',@4s"
"			)"
"		)"
"	),"
"	specie_id = (select max(id) from nepc.species where name = 'N+');"
)

mycursor.execute("LOAD DATA LOCAL INFILE 'n2_states.tsv'"
"	INTO TABLE nepc.states"
"	IGNORE 1 LINES"
"	(id,@o1,@o2,@o3,@o4,@o5,@o6,name,long_name)"
"	SET configuration = JSON_OBJECT("
"		JSON_OBJECT('order', "
"			JSON_ARRAY('2sigma_u', '1pi_u', '3sigma_g', '1pi_g', '3sigma_u', '3ssigma_g')"
"		),"
"		JSON_OBJECT('occupations',"
"			JSON_OBJECT("
"				'2sigma_u',@o1,"
"				'1pi_u',@o2,"
"				'3sigma_g',@o3,"
"				'1pi_g',@o4,"
"				'3sigma_u',@o5,"
"				'3ssigma_g',@o6"
"			)"
"		)"
"	),"
"	specie_id = (select max(id) from nepc.species where name = 'N2');"
)

directorynames = [userHome + "/projects/cs/data/raw/ext/n2/itikawa/",
	userHome + "/projects/cs/data/raw/ext/n2/zipf/"]

for directoryname in directorynames:
	directory = os.fsencode(directoryname)

	cs_id = 1
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		#print(directoryname + filename + "\n")
		if filename.endswith(".metadata"):
			continue
		else:
			executeTextCS = ("LOAD DATA LOCAL INFILE '" + directoryname + 
				filename + ".metadata' INTO TABLE nepc.cs "
				"(@temp,@specie,@process,units_e,units_sigma,ref,@lhsA,@lhsB,@rhsA,@rhsB,wavelength,lhs_v,rhs_v,lhs_j,rhs_j,background,lpu,upu) "
				"SET id = " + str(cs_id) + ", "
				"specie_id = (select id from nepc.species where name = @specie), "
				"process_id = (select id from nepc.processes where name = @process), "
				"lhsA_id = (select id from nepc.states where name LIKE @lhsA), "
				"lhsB_id = (select id from nepc.states where name LIKE @lhsB), "
				"rhsA_id = (select id from nepc.states where name LIKE @rhsA), "
				"rhsB_id = (select id from nepc.states where name LIKE @rhsB);")
	
			executeTextCSDATA = ("LOAD DATA LOCAL INFILE '" + directoryname + 
				filename + "' INTO TABLE nepc.csdata "
				"(id,e,sigma) "
				"SET cs_id = " + str(cs_id) + ";")
	
			#print("executeTextCS: " + executeTextCS + "\n")
			#print("executeTextCSDATA: " + executeTextCSDATA + "\n")
			mycursor.execute(executeTextCS)
			mycursor.execute(executeTextCSDATA)
			cs_id = cs_id + 1

mycursor.execute("use nepc;")

def printTable(table):
	print("\n=========================\n " + table + ":\n=========================")
	mycursor.execute("select * from " + table + ";")
	for x in mycursor:
		print(x) 

def countTableRows(table):
	print("\nRows in " + table + ": ") 
	mycursor.execute("select count(*) from " + table + ";")
	for x in mycursor:
		print(x) 

printTable("species")
printTable("processes")
printTable("states")
printTable("cs")
#printTable("csdata") 

#TODO: unit test to check for correct number of rows in csdata
countTableRows("csdata")

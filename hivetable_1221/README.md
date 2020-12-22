## First build the Hive Table called "covid_rc_1" with the command:
        hive -f 'zkf0.sql'
This is the table used to store all of the twitter data and it was only built once.
## Second, for each twitter JSON file, I do the following steps to process and import the JSON file to the table "covid_rc_1":

First use the file "date.py" to calculate each JSON file's created time.
        `/afs/cs/s/python-3.6.1/bin/python3 date.py covid19-1593243102545-3-js.json`

Then follow the code from Alex (https://github.com/alexhanna/hadoop/blob/master/hive/jsonToHive3.sh) to fix float and time bugs for each JSON file, and store them in the "ettmp" folder:

`hadoop jar /afs/cs.wisc.edu/u/z/h/zhongkai/double-conversation-1.0-SNAPSHOT.jar org.ahanna.DoubleConversion covidtweets_1/covid19-1593243102545-3-js.json ettmp`

Next, a temporal SQL file is created with the date information calculated in step 2.a:

`cat covid0.sql | sed "s/CURRYEAR/$year/" | sed "s/CURRMONTH/$month/" | sed "s/CURRDAY/$day/" | sed "s/CURRHOUR/$hour/" | sed "s/CURRIND/$ind/" >| covid0tmp.sql`

(The "covid0.sql" is also attached in the "hive_zhongkai.zip". Similarly, I followed the code from Alex "https://github.com/alexhanna/hadoop/blob/master/hive/update3.sql" to build the "covid0.sql")

Finally, the data in each twitter JOSN file is imported to the "covid_rc_1" using:

        hive -f 'covid0tmp.sql'

(I put steps 2.a - 2.e in the "covid.sh" so that it can import each file in the folder /covidtweets_1 recursively)

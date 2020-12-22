cat names0914.txt | while read line
do
    echo $line
    /afs/cs/s/python-3.6.1/bin/python3 date.py $line 
    year=$(cat tmp_year.txt)
    month=$(cat tmp_month.txt)
    day=$(cat tmp_day.txt)
    hour=$(cat tmp_hour.txt)
    ind=$(cat tmp_index.txt) 
    rm tmp_year.txt
    rm tmp_month.txt
    rm tmp_day.txt
    rm tmp_hour.txt
    rm tmp_index.txt
 
    hadoop fs -rm -r -skipTrash ettmp
    hadoop jar /afs/cs.wisc.edu/u/z/h/zhongkai/double-conversation-1.0-SNAPSHOT.jar org.ahanna.DoubleConversion /user/zhongkai/covidtweets_1/$line ettmp
    echo "processing file"   
    cat covid0.sql | sed "s/CURRYEAR/$year/" | sed "s/CURRMONTH/$month/" | sed "s/CURRDAY/$day/" | sed "s/CURRHOUR/$hour/" | sed "s/CURRIND/$ind/" >| covid0tmp.sql
    echo "loading data"
    hive -f 'covid0tmp.sql'
    if [ $? -eq 0 ]
    then 
        echo $line >> success_covid0.log
    else
        echo $line >> failure_covid0.log
    fi
     
    echo "DONE"
    
done


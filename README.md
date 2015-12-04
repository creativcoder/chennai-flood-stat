
#ChennaiRains 

##Visualizing flood stat reports 2015

#### The csv dataset is being fetched [here](https://docs.google.com/spreadsheets/d/1HUL5jcpy5-nsw_b9TFPVhXsGkZ9NiiwfT0Wc5JG-jmY/export?format=csv&id=1HUL5jcpy5-nsw_b9TFPVhXsGkZ9NiiwfT0Wc5JG-jmY&gid=444587373)

To import the database to mongodb issue the command:

`mongoimport -d floodstat -c review --type csv --file flood_stat.csv —headerline`

where

`-d floodstat is our database`

`-c reivew is our collection`

`--file flood_stat.csv is our csv file`


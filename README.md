## Chennai Flood Stat Reviews 2015


Visualizing reviews of help support in various areas


The dataset source is an excel google sheet [here](https://docs.google.com/spreadsheets/d/1HUL5jcpy5-nsw_b9TFPVhXsGkZ9NiiwfT0Wc5JG-jmY/edit#gid=444587373&vpid=A2)


To import the dataset into mongo:


Save the sheet as a csv file


Then fire up your mongo prompt and issue the command:


`mongoimport -d floodstat -c review --type csv --file flood_stat.csv —headerline`

where:

`-d floodstat` is our document

`-c review` is our collection

`--file flood_stat.csv` is the csv file
# sqlalchemy-challenge
In this challenge, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of a climate database. I did so, by completing the following steps:

I used the provided files (climate_starter.ipynb and hawaii.sqlite) to complete my climate analysis and data exploration.

I used the SQLAlchemy create_engine() function to connect to your SQLite database and the SQLAlchemy automap_base() function to reflect your tables into classes, 
and then saved references to the classes named station and measurement.

I linked Python to the database by creating a SQLAlchemy session.

Precipitation Analysis:

I found the most recent date in the dataset 8/23/2017.

Using that date, I got the previous 12 months of precipitation data by querying the previous 12 months of data.

Station Analysis:

I then designed query to calculate the total number of stations in the dataset, which is 9.

I then found the most-active station USC00519281, which had 2772 data points.

Finally the station were listed in descending order.
('USC00519281', 2772)
('USC00519397', 2724)
('USC00513117', 2709)
('USC00519523', 2669)
('USC00516128', 2612)
('USC00514830', 2202)
('USC00511918', 1979)
('USC00517948', 1372)
('USC00518838', 511)

Finally the minimum, maximum and average precipitation were calculated and visualized in a bar chart

Lastly I attempted to design a climate app with a homepage and links to the data.



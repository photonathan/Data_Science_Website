library(dplyr)
con <- dbConnect(odbc::odbc(), .connection_string = "Driver={MySQL ODBC 8.0 Unicode Driver};", 
                 server = "localhost", db = "counts", user = "root", password = rstudioapi::askForPassword("Database password"))

# Reads table counts_full into memory
my_table <- dbReadTable(con, 'counts_full')

# 
head(my_table)
# Creates a list class_list with the classes of each column
class_list <- (lapply(my_table, class))

# Finds size in megabytes
size_in_mb <- object.size(my_table)/1000000

# Stores first date object
date <- my_table$Date[1]
# Returns day of the week
weekdays(date)

# 2019 Peak Bloom Predictions National Park Service: April 2 - 5 
# https://cherryblossomwatch.com/cherry-blossom-watch-april-6-2019/
# Returns the date with the highest count: 2776242
my_table$Date[which.max(my_table$Count)]
# Returns hour 11
my_table$Hour[which.max(my_table$Count)]
# CounterID = 9 = Mt Vernon Trail next to airport
my_table$CounterID[which.max(my_table$Count)]
# Direction = Inbound = Northbound at this counter
# Everyone going to the tidal basen
my_table$Direction[which.max(my_table$Count)]
                   
# Scatter plot
plot(my_table$CounterID, my_table$Count)

## Setting up ability to not pull the entire database into memory by
## making specific queries to MySQL. ``
# Create a link to the count_full table but do not hold the entire table
counts <- tbl(con, 'counts_full')
# Much smaller
object.size(counts)
# Filter by date
counts %>% filter(Date == '2011-09-03')

## Use SQL statements to create dataframes
sql_cmd <- 'SELECT * FROM counts_daily'
my_table <- dbGetQuery(con, sql_cmd)
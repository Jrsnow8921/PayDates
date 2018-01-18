# PayDates
Simple Python script to get pay dates for a current year 


## Install
    git clone git@github.com:Jrsnow8921/PayDates.git
    cd PayDates
    
## Run 
    update main.py:
       PayDates() takes 3 args 
         start = first pay date of the year; this needs to be set to calculate the rest of the dates for the year.
         fx = this is the frequency of pay periods. Ex: weekly = 7 biweekly = 14
         save = set this flag to 1 if you would like to save the pay dates to a text file. (payDates.txt)
    
    Example:
      start = 2018-01-11
      fx = 14 
      save = 1
      
      PayDays(datetime(year=datetime.now().year, month=1, day=11), 14, 1).main()
      
    Once you've updated main.py please run this command in the same dir.
    
    python main.py
  

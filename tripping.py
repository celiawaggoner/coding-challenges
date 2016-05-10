import datetime

property_one = {
                'start_date': "2015-01-01",
                'availability': "NNNNYYNNNNNNNNNNYYYYYNNNNNNNNYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYNNNNYYYYYYYYNNNNNNNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
                'minstay': "6,5,3,6,6,6,4,6,3,3,6,5,3,3,5,6,6,4,5,2,2,6,3,5,4,6,2,6,6,5,2,4,2,2,4,3,2,5,3,4,2,2,5,4,2,6,3,3,3,3,5,6,5,3,6,4,2,3,2,3,2,4,2,2,6,3,6,4,3,5,4,3,3,2,5,3,4,3,4,6,6,4,4,5,2,3,6,3,5,2,2,4,6,5,5,2,6,6,3,6,2,3,3,6,3,2,3,4,4,4,5,2,2,5,2,3,3,6,5,3,3,3,5,2,4,2,6,5,4,4,3,4,3,3,6,5,5,4,3,3,2,4,6,3,3,6,6,4,2,2,3,4,2,6,5,2,6,3,2,4,3,4,5,6,5,3,6,5,6,2,4,3,4,2,3,5,6,3,2,2,2,6,6,2,5,2,3,2,4,4,4,6,6,4,3,2,4,5,5,2,3,2,4,6,6,5,6,2,6,3,2,6,2,6,2,5,5,5,5,4,2,6,3,2,2,2,6,6,5,5,4,4,5,4,2,2,5,5,5,2,6,4,4,4,3,2,6,3,3,2,4,2,6,6,3,6,4,5,4,4,5,6,6,6,6,3,3,5,5,6,3,5,5,6,6,3,2,4,2,3,5,3,4,3,3,3,3,4,5,2,6,5,6,5,5,4,2,3,3,2,4,6,3,2,3,2,3,3,4,5,3,3,6,5,2,6,4,5,5,6,2,4,6,5,2,5,3,4,6,3,3,3,4,5,4,4,4,5,4,3,6,2,2,2,6,4,2,2,6,4,5,3,3,4,2,5,6,5,6,5,3,5,2,2,5",
                'price': "248,109,138,227,104,207,163,119,249,261,162,286,235,205,210,215,259,227,203,183,181,153,140,258,103,198,253,286,254,133,202,142,163,261,205,133,113,152,130,193,153,140,174,282,128,268,114,199,168,254,296,267,224,249,200,207,160,124,108,165,259,293,143,282,267,129,114,268,249,186,255,124,161,247,297,100,113,170,201,239,283,180,142,220,105,294,226,228,101,108,104,187,238,251,106,259,262,120,174,141,231,207,270,193,292,121,250,166,171,287,220,142,176,195,180,215,155,243,116,249,265,164,172,213,151,132,215,235,116,181,260,199,203,189,251,124,128,152,128,188,140,273,176,208,143,143,108,265,269,273,265,182,275,237,188,183,108,234,137,270,106,273,122,105,171,236,213,278,281,102,117,163,277,104,294,252,210,124,203,253,100,220,205,226,100,236,101,150,148,104,205,110,249,175,131,185,210,262,290,271,214,247,158,210,220,156,137,284,245,212,137,237,235,112,158,278,127,132,272,104,103,274,199,260,154,209,186,260,251,247,180,106,107,102,164,290,166,243,234,244,108,182,249,118,99,131,191,231,247,152,120,146,154,223,209,111,116,194,101,212,163,110,257,196,230,250,273,152,116,185,158,276,293,285,219,101,119,159,170,168,147,104,211,137,235,136,136,152,281,176,134,144,130,298,269,272,101,168,141,198,184,154,186,109,230,185,195,282,265,210,290,265,194,120,122,240,256,280,289,164,109,136,213,267,161,265,162,162,182,196,251,204,191,280,199,243,214,255,180,183,200,114,250,159,267,217,213,263,151,115,223,221,244,261,190,166,112,266,291,283,249,135,102,151,113"
                }


def available_ranges(a_property):
    """Take in a property and return an array of all available contiguous date ranges,
       listing only the start and end date of each range."""

    #initialize empty list to save outputs
    available_date_ranges = []

    #create a list from the minstay string
    minstay = a_property['minstay'].split(',')

    #convert the property's start date into a datetime element
    start_date = datetime.datetime.strptime(a_property['start_date'], "%Y-%m-%d")

    #iterate over the availability string
    for start_stay_index, avail in enumerate(a_property['availability']):
        if avail == "Y":
            #establish corresponding minstay value
            min_stay = int(minstay[start_stay_index])
          
            #check if property is available for length of minimum stay
            if a_property['availability'][start_stay_index:start_stay_index+min_stay] == 'Y' * min_stay:
                #determine last day of the stay
                #I subtracted 1 here in order to return a range indicating the nights stayed
                #if you wanted to return a range indicating check in and check out days,
                #you could remove that '- 1'
                end_stay_index = start_stay_index + min_stay - 1

                #format start and end dates using datetime module
                range_start_date = start_date + datetime.timedelta(days=start_stay_index)
                range_start_date = range_start_date.strftime('%Y-%m-%d')
      
                range_end_date = start_date + datetime.timedelta(days=end_stay_index)
                range_end_date = range_end_date.strftime('%Y-%m-%d')
        
                #append a list with the start and end date to the list of all ranges
                available_date_ranges.append([range_start_date, range_end_date])

    return available_date_ranges


def cost_of_booking(a_property, start_date, end_date):
    """Given a property and a start and end date, return the total cost of booking the property for that date range;
       return 0 if the property is unavailable for any date in the range."""
    
    #convert the input dates into datetime elements
    input_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    input_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    #convert the property's start date into a datetime element
    property_start_date = datetime.datetime.strptime(a_property['start_date'], "%Y-%m-%d")

    #find the difference between the start and end dates given and the start date of the property
    start_delta = input_start_date - property_start_date
    end_delta = input_end_date - property_start_date

    #check that the input dates are in bounds
    if start_delta.days < len(a_property['availability']) and end_delta.days < len(a_property['availability']):

        #create a list from the property's price string
        price = a_property['price'].split(',')

        #initialize the total cost to 0
        total_cost = 0

        #iterate over the property's availability for the given date range
        #update the total cost if it is available
        #if it is not available on any date in that range, return 0
        for index, avail in enumerate(a_property['availability'][start_delta.days:end_delta.days + 1]):
            if avail == "Y":
                total_cost += int(price[index + start_delta.days])
            else:
                return 0

        return total_cost
    else:
        return "Whoops! We don't have booking data available for those dates."






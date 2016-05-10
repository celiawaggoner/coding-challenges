import json
import sys
import difflib

#### My ranking system uses Python's difflib module and SequenceMatcher class to
#### filter the results. SequenceMatcher takes in the search term and the value,
#### like a name or an email address, and when coupled with the ratio method,
#### returns a measure of the sequences' similarity as a float in the range of 0 to 1.

#### The contact is added to the output list if the ratio is greater than or equal to 0.4.
#### This number allows for some flexibility, but also returns relevant matches.
#### The output list is then sorted and contacts are printed out in the order from
#### highest match to lowest.

#### If the ratio is the same for multiple contacts, the results are printed out
#### in the order they appear in the data source.


def main(search_term):
    """Given a search term, print out an ordered list of JSON normalized results,
       ranked with the most relevant contacts first"""

    # stringify the command line input
    search_term = str(search_term)

    # convert JSON object into Python dictionary
    json_data = open('./contacts.json').read()
    contacts = json.loads(json_data)

    #initialize empty list to save results
    ranked_list = []

    # iterate over the contacts
    # use difflib to determine the similarity between the seach time and the contact info
    # if the search term is significantly similar, append that contact to the list
    for contact in contacts:
        for value in contact.values():
            ratio = difflib.SequenceMatcher(None, search_term, value).ratio()
            if ratio >= 0.4:
                if contact not in ranked_list:
                    ranked_list.append((ratio, contact))

    # sort the list by highest to lowest ratio
    ranked_list = (sorted(ranked_list))[::-1]

    # check for empty list
    if not ranked_list:
        print "Sorry! We couldn't find any contacts that match that search term."
        return []

    # iterate over the list and print each contact
    else:
        for item in ranked_list:
            item = item[1]
            print json.dumps(item)
        return ranked_list


if __name__ == "__main__":
    main(sys.argv[1])



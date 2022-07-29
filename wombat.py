import requests

GET_UNMARKED_URL = "http://127.0.0.1:5000/datahub/UnmarkedSignals"
FETCH_REJECTED_URL ="http://127.0.0.1:5000/datahub/FetchRejectedSignals"
UPDATE_SIGNALS_URL ="http://127.0.0.1:5000/datahub/UpdateSignals"

# GET_UNMARKED_URL = "https://cts-sdf-api-devel.factset.io/datahub/UnmarkedSignals"
# FETCH_REJECTED_URL="http://https://cts-sdf-api-devel.factset.io/datahub/FetchRejectedSignals"
# UPDATE_SIGNALS_URL="http://https://cts-sdf-api-devel.factset.io/datahub/UpdateSignals"


def main():
    unmarkedData=getUnmarked() 
    lastEmpty=unmarkedData[-1][1] #last item in the list is the latest signal marked as empty
    rejected=getRejected(lastEmpty)
    rejectedList=[]
    for i in rejected:
        rejectedList.append(i[0]) #convert from list of lists to list of objects
    empty, accepted=intersectSignals(unmarkedData, rejectedList)
    update(empty, accepted)

def getUnmarked(): #returns all of the signals unmarked, including the latest signal marked as empty
    response = requests.get(GET_UNMARKED_URL)
    return response.json()

def getRejected(postBody): #get all of the signals 
    try:
        response = requests.post(FETCH_REJECTED_URL, json=postBody)
        return response.json()
    except Exception as e:
        print( 'Error: ' , e)

def update(empty, accepted):
    acceptedyOrEmpty={}
    acceptedyOrEmpty['0']=accepted
    acceptedyOrEmpty['1']=empty
    requests.post(UPDATE_SIGNALS_URL,  json=acceptedyOrEmpty)
    print('Done!')

def intersectSignals(unmarked, rejected):
    emptyIds=[]
    acceptedIds=[]
   
    for i in unmarked:
        if i[1] in rejected:
            emptyIds.append(i[0])
        else:
            acceptedIds.append(i[0])
    print('Rejcted Ids: ', emptyIds)
    return emptyIds, acceptedIds

if __name__ == "__main__":
    main()
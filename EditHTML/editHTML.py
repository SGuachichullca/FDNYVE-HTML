import pandas as pd
from bs4 import BeautifulSoup

def generateEmailHTML(
        currBinNumber:int,
        oldNumOfViolations:int,
        newNumOfViolations:int, 
        viosToAdd:str, 
        viosToDismiss:str,
        novsToAdd:str,
        novsToDismiss:str
        ): #Program assumes that viosToAdd/Dismiss and novsToAdd/Dismiss are already arrays. 

    #Replace these file paths with your own.
    newEmail =  'C:\\Users\\Vivek\\Dropbox\\PC\\Documents\\Python Project\\EditHTML\\newEmail.html'
    emailHTML = 'C:\\Users\\Vivek\\Dropbox\\PC\\Documents\\Python Project\\EditHTML\\FDNYViolationsEmail.html'

    htmlID=["binNo", "oldNo","newNo", "newViolations","oldViolations","newNOV","oldNOV"]

    with open(emailHTML, 'r+') as fp:
        soup = BeautifulSoup(fp, 'html.parser')


    #converts viosToAdd/Dismiss to dataframes, and then to html.
    newVioData = pd.DataFrame({'New VOs': viosToAdd})
    oldVioData = pd.DataFrame({'Old VOs': viosToDismiss})
    newVioDataFrame = newVioData.to_html(justify='center', index=False)
    oldVioDataFrame = oldVioData.to_html(justify='center', index=False)

    newNovData = pd.DataFrame({'New NOVs': novsToAdd})
    oldNovData = pd.DataFrame({'Old NOVs': novsToDismiss})
    newNovDataFrame = newNovData.to_html(justify='center', index=False)
    oldNovDataFrame = oldNovData.to_html(justify='center', index=False)

    #ID tags in the original HTML file.
    updateHTML=[currBinNumber, newNumOfViolations,oldNumOfViolations, newVioDataFrame, oldVioDataFrame, newNovDataFrame, oldNovDataFrame]

    #Loop searches for each ID, appends it with the relevant info 
    for x in range(0,len(updateHTML)):
        print(x)
        findID = soup.find(id=htmlID[x])
        findID.append(BeautifulSoup(str(updateHTML[x]), 'html.parser'))

    #saves html to new file, keeps original html intact..
    fp = open(newEmail,"r+",)
    fp.truncate()
    fp.write(soup.prettify())
    fp.close()


viosToAdd = ['2022-ENFORC-017531-VIOR','2022-ENFORC-017532-VIOR','2022-ENFORC-034770-VIOR','E683401','LD407045']
viosToDismiss = ['2022-ENFORC-05335-VIOR','2022-ENFORC-012342-VIOR']
novsToAdd = []
novsToDismiss = ['2022-ENFORC-012342-VIOR']
generateEmailHTML(12345678, 5, 2, viosToAdd, viosToDismiss, novsToAdd, novsToDismiss)



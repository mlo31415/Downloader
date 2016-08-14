import urllib.request
import os


webDirectory= "Barsoomian_Times"
prefix="Barsoomian_Times"
digitsInIssue=2
digitsInPage=2

outputDirectory="C:\\Users\\mlo\\temp\\downloads"
outputDirectory=os.path.join(outputDirectory, webDirectory)
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

for issue in range(1, 20):
    for page in range(0, 19):
        filename=prefix+str(issue).zfill(digitsInIssue)+'-'+str(page).zfill(digitsInPage)+'.html'
        url = 'http://fanac.org/fanzines/' + webDirectory + '/' + filename
        try:
            response = urllib.request.urlopen(url, data=None)
            webContent = response.read()
            p=os.path.join(outputDirectory, filename)
            with open(p, "w") as f:
                f.writelines(webContent.decode("utf-8") )
                f.close()
        except:
            pass
pass
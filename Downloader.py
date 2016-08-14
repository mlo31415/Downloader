import urllib.request
import os


webDirectory= "FanewsCard"
prefix="Fanews"

outputDirectory="C:\\Users\\mlo\\temp\\downloads"
outputDirectory=os.path.join(outputDirectory, webDirectory)
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

for issue in range(1, 350):
    for page in range(0, 1):
        filename=prefix+str(issue).zfill(3)+'.html'#''-'+str(page).zfill(2)+'.html'
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
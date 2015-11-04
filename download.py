import urllib
 
testfile = urllib.URLopener()
 
testfile.retrieve("http://172.16.9.77:8080//razuna/raz1/dam/index.cfm?fa=c.serve_file&file_id=8B68EBF7F08A4A1D81EFDD613AC7A22B&type=vid", "Animation.mp4")
print "download completed"

from socket import *
import sys
import subprocess

#USAGE: python portScan2.py -h <fileName> -p { <portNum> | <portNum-portNum> }

if __name__ == '__main__':
    #target = raw_input('Enter host to scan: ')
    #targetIP = gethostbyname(sys.argv[2])
    #print 'Starting scan on host ', targetIP

    #40 - working
    #5 read hosts from file
    #10 multiple ports to scan
    #10 makes an html report


    connectionType = SOCK_STREAM
    if len(sys.argv) == 6 and sys.argv[5] == '-udp':
        connectionType = SOCK_DGRAM
    print connectionType
    #get the port range:
    if "-" in sys.argv[4]:
        lowerPortRange = sys.argv[4].split("-")[0]
        upperPortRange = sys.argv[4].split("-")[1]
    else:
        lowerPortRange = sys.argv[4]
        upperPortRange = lowerPortRange
    fileName = open(sys.argv[2])
    out = file('report.html', 'w')
    print "Port scan results: (output also reported in HTML page called report.html)"
    print >> out, "<html><head><title>Port scan report</title></head><body>"
    with open(sys.argv[2]) as fileName:
        print >> out, "<div class='main' style='width: 600px; margin: 0 auto'>"
        for host in fileName:
            print >> out, "<h2> %s open ports:</h2><ul>" %(host)
            print "\n\nHOST: %s" %(host)
            for portNum in range(int(lowerPortRange), int(upperPortRange)+1):
                s = socket(AF_INET, connectionType)
                try:

                    #orig_stdout = sys.stdout
                    #sys.stdout = out
                    result = s.connect_ex((host, portNum))
                    if(result == 0):
                        print >> out, '<li> %d: </li>' % (portNum,)
                        print 'Port %d: OPEN' % (portNum,)
                    s.close()
                    #sys.stdout = orig_stdout


                except gaierror:
                    print "could not connect to host"
                    pass
                except Exception:
                    print 'error'
                    pass
            print >> out, "</ul>"
        print >> out, "</div>"
    print >> out, "</body></html>"
    out.close()
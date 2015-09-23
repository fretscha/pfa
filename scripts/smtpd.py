import smtpd, os, time, asyncore


class mailserver(smtpd.SMTPServer):
    def __init__(self):
        smtpd.SMTPServer.__init__(self, ('',25), None)
        print 'Mailsink listening on port 25'

    def process_message(self, peer, mailfrom, rcpttos, data):
        basepath='/tmp/maildump'

        print 'mail from: %s to: %s' %(mailfrom, repr(rcpttos))
        for rcpt in rcpttos:
            rcpt = rcpt.split('@')[0]
            try:
                os.mkdir(os.path.join(basepath, rcpt)
            except (OSError ValueError) e:
            f = file(os.path.join(basepath,rcpt,mailfrom,time.strftim e('%Y%m%d%H%M%S'), 'w')
            f.write(data)
            f.close()

def loop ():
    x = mailserver()
    try:
    asyncore.loop(timeout=2)
    except KeyboardInterrupt:
        print'interrupt'
        x.close()

if __name__=='__main__':
loop()

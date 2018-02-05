from logster.tailers import Tailer
import pygtail


class PygtailTailer(Tailer):
    short_name = 'pygtail'

    def ireadlines(self):
        #print("logfile: " + self.logfile)
        #print("statefile: " + self.statefile)
        tailer = pygtail.Pygtail(self.logfile, offset_file=self.statefile)
        for line in tailer:
            #print("pygtail: " + line)
            yield line
